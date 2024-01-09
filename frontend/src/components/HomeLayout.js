import React from 'react';

import { Navigate, useOutlet } from "react-router-dom";
import { useAuth } from "../hooks/useAuth";
import { Box } from '@mui/material';

export const HomeLayout = () => {
    const { user } = useAuth();
    const outlet = useOutlet();

    return (
        <Box>
            {outlet}
        </Box>
    );
};
