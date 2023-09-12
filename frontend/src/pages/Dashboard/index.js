import React, { useState, useEffect } from 'react';

import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import LinearProgress from '@mui/material/LinearProgress';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';


export default function Dashboard() {
    const [progress, setProgress] = useState(0);
    const [auctions, setAuctions] = useState([]);
    const [isFetching, setIsFetching] = useState(false);

    useEffect(() => {
        const fetchAuctions = async () => {
            try {
                const response = await fetch('/api/auction');
                if (response.ok) {
                    const data = await response.json();
                    setAuctions(data.results);
                    console.log(data.results)
                } else {
                    console.error(`Request failed for item ${i}: ${response.status}`);
                }
            } catch (error) {
                console.error(`Request failed for item ${i}: ${error.message}`);
            }

        };

        fetchAuctions();
    }, []);

    const handleUpdate = async () => {
        setIsFetching(true);
        for (let i = 0; i < auctions.length; i++) {
            try {
                const response = await fetch('/api/update/' + auctions[i].slug, {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json"
                    }
                });
                if (response.ok) {
                } else {
                    console.error(`Request failed for item ${i}: ${response.status}`);
                }
            } catch (error) {
                console.error(`Request failed for item ${i}: ${error.message}`);
            }
            const newProgress = ((i + 1) / auctions.length) * 100;
            setProgress(newProgress);
        }

        setIsFetching(false);
    }

    return (
        <Box component="main" sx={{ padding: 3, overflow: "auto", height: "100vh" }}>
            <AppBar sx={{ background: 'transparent', boxShadow: 'none' }}>
                <Toolbar>
                    <Typography variant='h4' component='div' sx={{ flexGrow: 1, color: 'black' }}>
                        WESTERN
                    </Typography>
                    <Typography variant='body2' component='div' sx={{ marginRight: '20px' }}>
                        <a href='/' style={{ color: 'black', textDecoration: 'none', fontWeight: 'light' }}>Dashboard</a>
                    </Typography>
                </Toolbar>
            </AppBar>
            <Toolbar />
            <Card>
                <CardContent>
                    <LinearProgress variant="determinate" value={progress} />
                </CardContent>
                <CardActions>
                    <Button size="small" disabled={isFetching} onClick={handleUpdate} variant="contained">Update</Button>
                </CardActions>
            </Card>
        </Box>
    )
}