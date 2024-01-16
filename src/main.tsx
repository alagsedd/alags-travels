import React from "react";
import ReactDOM from "react-dom/client";
import "../src/styles/Global.css";
import { RouterProvider } from "react-router-dom";
import { router } from "./routes/Router.tsx";
import { ChakraProvider } from "@chakra-ui/react";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <ChakraProvider>
      {" "}
      <RouterProvider router={router} />
    </ChakraProvider>
  </React.StrictMode>
);
