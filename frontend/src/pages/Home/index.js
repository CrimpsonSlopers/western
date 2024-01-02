import React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';

const Home = () => {
    return (
        <Box
            sx={{
                width: '100%',
                height: '100vh',
                backgroundImage: `url('static/Landing.jpg')`,
                backgroundSize: 'cover',
                backgroundPosition: 'center',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'flex-start',
                alignItems: 'flex-start',
                gap: '2.5rem',
                inlineFlex: 'inline-flex',
            }}
        >
            <Box
                sx={{
                    padding: '1rem 4rem',
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center',
                    alignSelf: 'stretch',
                }}
            >
                <Box
                    sx={{
                        display: 'flex',
                        justifyContent: 'flex-start',
                        alignItems: 'flex-start',
                    }}
                >
                    <Typography
                        sx={{
                            color: 'white',
                            fontSize: '32px',
                            fontWeight: 900,
                            fontFamily: 'Brandon Grotesque',
                        }}
                    >
                        WESTERN FUTURES
                    </Typography>
                </Box>
                <Box
                    sx={{
                        display: 'flex',
                        gap: '1rem',
                        alignItems: 'center',
                    }}
                >
                    <Link
                        href="autofeeder"
                        underline="none"
                        color="white"
                        sx={{
                            fontSize: '1.5rem',
                            fontWeight: 'bold',
                            fontFamily: 'Brandon Grotesque',
                        }}
                    >
                        autofeeder
                    </Link>
                    <Link
                        href="admin/"
                        underline="none"
                        color="white"
                        sx={{
                            fontSize: '1.5rem',
                            fontWeight: 'bold',
                            fontFamily: 'Brandon Grotesque',
                        }}
                    >
                        admin
                    </Link>
                </Box>
            </Box>
            {/* Other content goes here */}
        </Box>
    );
};

export default Home;
