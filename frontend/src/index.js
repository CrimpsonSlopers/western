import React from "react";
import { createRoot } from "react-dom/client";
import { RouterProvider } from "react-router-dom";

import { router } from "./App";

const rootElement = document.getElementById("root");
const root = createRoot(rootElement);
root.render(
    <RouterProvider router={router} />
);