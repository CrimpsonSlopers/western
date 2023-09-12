import asyncio
import pandas as pd
import requests

from requests.auth import HTTPBasicAuth

from datetime import date, timedelta

from api.models import Sale

WEIGHT_RANGES = [(700, 749), (750, 799), (800, 849), (850, 899), (700, 899)]
MARS_API_AUTH = HTTPBasicAuth("rscaGmY9VNZo5Me5ttCYrjJhUxSF2sFX", "")

VIDEO_REGIONS = {"South Central": "SC", "North Central": "NC"}


def flatten(df: pd.DataFrame):
    h = df["head_count"].sum()
    w = (df["avg_weight"] * df["head_count"]).sum()
    p = (df["avg_price"] * df["avg_weight"] * df["head_count"]).sum()

    return (int(h), (w / h) if h else 0.0, (p / w) if h else 0.0)


def process_sale(df, report_date, auction_name, final_ind, region=""):
    try:
        sale = Sale(
            date=report_date,
            auction_id=auction_name,
            final_ind=final_ind,
            region=region,
        )
        for i, weight_rng in enumerate(WEIGHT_RANGES):
            h, w, p = flatten(
                df[
                    df["avg_weight"].between(
                        weight_rng[0], weight_rng[1], inclusive="left"
                    )
                ]
            )
            setattr(sale, f"head{i+1}", h)
            setattr(sale, f"weight{i+1}", w)
            setattr(sale, f"price{i+1}", p)

        sale.save()
        return True
    except:
        print(f"Error adding sale to {auction_name} on {report_date}")
        return False


def make_request(auction):
    start = (auction.last_final_sale_date + timedelta(days=1)).strftime("%m/%d/%Y")
    end = (date.today() + timedelta(days=30)).strftime("%m/%d/%Y")
    response = requests.get(auction.mmn_url.format(start, end), auth=MARS_API_AUTH)

    if response.status_code >= 400:
        return None

    else:
        result = response.json()
        if "results" in result and len(result["results"]) == 0:
            return None

        df = pd.DataFrame.from_dict(result["results"])
        df["report_end_date"] = pd.to_datetime(
            df["report_end_date"], format="%m/%d/%Y"
        ).dt.date

        for report_date, group in df.groupby("report_end_date"):
            report_date = report_date + timedelta(days=auction.offset)
            final_ind = group["final_ind"].iloc[0].lower()

            if auction.market in ("live", "special"):
                process_sale(group, report_date, auction.name, final_ind)

            elif auction.market in ("direct", "video"):
                group.rename(
                    columns={
                        "wtd_avg_wt": "avg_weight",
                        "wtd_avg_price": "avg_price",
                    },
                    inplace=True,
                )
                group["avg_weight"] = group["avg_weight"].astype(float)
                group["head_count"] = group["head_count"].astype(int)
                group["avg_price"] = group["avg_price"].astype(float)

                if auction.market == "direct":
                    process_sale(group, report_date, auction.name, final_ind)

                else:
                    for region, region_group in group.groupby("region_name"):
                        process_sale(
                            region_group,
                            report_date,
                            auction.name,
                            final_ind,
                            region=region,
                        )

                if final_ind == "final":
                    auction.last_final_sale_date = report_date
                    auction.save()


async def update_autofeeder(auctions):
    tasks = [make_request(auction) for auction in auctions]

    results = []
    for task in asyncio.as_completed(tasks):
        response = await task
        if response:
            results += response

    return results
