import React, { useEffect } from 'react';
import { Routes, Route } from "react-router-dom";

import { ThemeProvider } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import { theme } from "./theme";

import Dashboard from './pages/Dashboard';

export default function App() {

    return (
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <Routes>
                <Route index element={<Dashboard />} />
            </Routes>
        </ThemeProvider>
    )
} 