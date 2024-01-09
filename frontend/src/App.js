import React from 'react';
import {
    Route,
    createBrowserRouter,
    createRoutesFromElements,
    defer
} from "react-router-dom";

import AutoFeeder from './pages/AutoFeeder';
import HomePage from './pages/HomePage';
import { AuthLayout } from "./components/AuthLayout";
import { HomeLayout } from './components/HomeLayout';
import { ProtectedLayout } from './components/ProtectedLayout';

const getUserData = () =>
    new Promise((resolve, reject) => {
        fetch('api/authenticate')
            .then(response => {
                if (response.status === 200) {
                    return response.json();
                } else {
                    return null
                }
            })
            .then(user => {
                resolve(user);
            })
            .catch(error => {
                reject(error);
            });
    });

export const router = createBrowserRouter(
    createRoutesFromElements(
        <Route
            element={<AuthLayout />}
            loader={() => defer({ userPromise: getUserData() })}
        >
            <Route element={<HomeLayout />}>
                <Route path="/" element={<HomePage />} />
            </Route>

            <Route path="/autofeeder" element={<ProtectedLayout />}>
                <Route index element={<AutoFeeder />} />

            </Route>
        </Route>
    )
);