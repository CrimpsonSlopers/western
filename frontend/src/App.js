import React, { useEffect } from 'react';
import { Routes, Route } from "react-router-dom";

import { ThemeProvider } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import { theme } from "./theme";

import Dashboard from './pages/Dashboard';
import Home from './pages/Home';

export default function App() {

    return (
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <Routes>
                <Route index element={<Home />} />
                <Route path='autofeeder' element={<Dashboard />} />
            </Routes>
        </ThemeProvider>
    )
} 