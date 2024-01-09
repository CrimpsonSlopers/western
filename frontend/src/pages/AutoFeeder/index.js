import React, { useState, useEffect } from 'react';

import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import LinearProgress from '@mui/material/LinearProgress';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Checkbox from '@mui/material/Checkbox';
import Card from '@mui/material/Card';


function not(a, b) {
    return a.filter((value) => b.findIndex((item) => item.slug === value.slug) === -1);
}

function intersection(a, b) {
    return a.filter((value) => b.findIndex((item) => item.slug === value.slug) !== -1);
}


export default function AutoFeeder() {
    const [progress, setProgress] = useState(0);
    const [isFetching, setIsFetching] = useState(false);
    const [checked, setChecked] = useState([]);
    const [left, setLeft] = useState([]);
    const [right, setRight] = useState([]);

    useEffect(() => {
        const fetchAuctions = async () => {
            try {
                const response = await fetch('/api/auction');
                if (response.ok) {
                    const data = await response.json();
                    setLeft(data.results);
                } else {
                    console.error(`Request failed for item ${i}: ${response.status}`);
                }
            } catch (error) {
                console.error(`Request failed for item ${i}: ${error.message}`);
            }

        };

        fetchAuctions();
    }, []);

    useEffect(() => {
        console.log(checked)
    }, [checked])

    const leftChecked = intersection(checked, left);
    const rightChecked = intersection(checked, right);

    const handleToggle = (value) => () => {
        console.log(value)
        const currentIndex = checked.indexOf(value);
        const newChecked = [...checked];

        if (currentIndex === -1) {
            newChecked.push(value);
        } else {
            newChecked.splice(currentIndex, 1);
        }

        setChecked(newChecked);
    };

    const handleAllRight = () => {
        setRight(right.concat(left));
        setLeft([]);
    };

    const handleCheckedRight = () => {
        setRight(right.concat(leftChecked));
        setLeft(not(left, leftChecked));
        setChecked(not(checked, leftChecked));
    };

    const handleCheckedLeft = () => {
        setLeft(left.concat(rightChecked));
        setRight(not(right, rightChecked));
        setChecked(not(checked, rightChecked));
    };

    const handleAllDirects = () => {
        const leftDirects = left.filter((value) => value.market === 'direct');
        setRight(right.concat(leftDirects));
        setLeft(not(left, leftChecked));
        setChecked(not(checked, leftChecked));
    };

    const handleAllLeft = () => {
        setLeft(left.concat(right));
        setRight([]);
    };

    const handleUpdate = async () => {
        setIsFetching(true);
        for (let i = 0; i < right.length; i++) {
            try {
                const response = await fetch('/api/update/' + right[i].slug, {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json"
                    }
                });
                if (response.ok) {
                } else {
                    console.error(`Request failed for item ${i.name}: ${response.status}`);
                }
            } catch (error) {
                console.error(`Request failed for item ${i.name}: ${error.message}`);
            }
            const newProgress = ((i + 1) / right.length) * 100;
            setProgress(newProgress);
        }
        setProgress(0);
        setIsFetching(false);
    }

    const customList = (items) => (
        <Card variant={"outlined"} sx={{ width: 350, height: "80vh", overflow: 'auto' }}>
            <List dense component="div" role="list">
                {items.map((value) => {
                    const labelId = `transfer-list-item-${value.slug}-label`;
                    return (
                        <ListItem
                            key={value.slug}
                            role="listitem"
                            onClick={handleToggle(value)}
                        >
                            <ListItemIcon>
                                <Checkbox
                                    checked={checked.findIndex((item) => item.slug === value.slug) !== -1}
                                    tabIndex={-1}
                                    disableRipple
                                    inputProps={{
                                        'aria-labelledby': labelId,
                                    }}
                                />
                            </ListItemIcon>
                            <ListItemText id={labelId} primary={`${value.name} (${value.slug})`} />
                        </ListItem>
                    );
                })}
            </List>
        </Card>
    );

    return (
        <Box sx={{ overflow: "hidden", height: "100vh" }}>
            <AppBar sx={{ background: 'white', boxShadow: 'none' }}>
                <Toolbar>
                    <Typography variant='h4' component='div' sx={{ flexGrow: 1, color: 'black', fontWeight: 'bold' }}>
                        <a href='/' style={{ color: 'black', textDecoration: 'none' }}>WESTERN</a>
                    </Typography>
                    <Typography variant='body2' component='div' sx={{ marginRight: '20px', fontWeight: 'bold' }}>
                        <a href='/admin/' style={{ color: 'black', textDecoration: 'none' }}>Admin</a>
                    </Typography>
                </Toolbar>
            </AppBar>
            <Toolbar />
            <Grid container spacing={3} px={1}>
                <Grid item xs={12} md={7}>
                    <Grid container spacing={2} justifyContent="center" alignItems="center">
                        <Grid item>{customList(left)}</Grid>
                        <Grid item>
                            <Grid container direction="column" alignItems="center">
                                <Button
                                    sx={{ my: 0.5 }}
                                    variant="outlined"
                                    size="small"
                                    onClick={handleAllRight}
                                    disabled={left.length === 0}
                                    aria-label="move all right"
                                >
                                    ≫
                                </Button>
                                <Button
                                    sx={{ my: 0.5 }}
                                    variant="outlined"
                                    size="small"
                                    onClick={handleCheckedRight}
                                    disabled={leftChecked.length === 0}
                                    aria-label="move selected right"
                                >
                                    &gt;
                                </Button>
                                <Button
                                    sx={{ my: 0.5 }}
                                    variant="outlined"
                                    size="small"
                                    onClick={handleCheckedLeft}
                                    disabled={rightChecked.length === 0}
                                    aria-label="move selected left"
                                >
                                    &lt;
                                </Button>
                                <Button
                                    sx={{ my: 0.5 }}
                                    variant="outlined"
                                    size="small"
                                    onClick={handleAllLeft}
                                    disabled={right.length === 0}
                                    aria-label="move all left"
                                >
                                    ≪
                                </Button>
                                <Button
                                    sx={{ my: 0.5 }}
                                    variant="outlined"
                                    size="small"
                                    onClick={handleAllDirects}
                                    aria-label="move all directs right"
                                >
                                    Directs ≫
                                </Button>
                            </Grid>
                        </Grid>
                        <Grid item>{customList(right)}</Grid>
                    </Grid>
                    <Grid
                        container
                        justifyContent="center"
                        alignItems="center"
                        spacing={2}
                        py={2}
                    >
                        <Grid item xs>
                            <LinearProgress variant="determinate" value={progress} />
                        </Grid>
                        <Grid item xs={"auto"}>
                            <Button size="small" disabled={isFetching} onClick={handleUpdate} variant="contained">Update</Button>
                        </Grid>
                    </Grid>
                </Grid>
            </Grid>
        </Box>
    )
}