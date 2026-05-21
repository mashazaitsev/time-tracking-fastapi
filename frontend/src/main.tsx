/**
 * @file Application entry point — initializes React with router, query client, theme, and API auth.
 * @module main
 */

/**
 * Purpose: Initialize React application with router, query client, theme, and API auth
 *
 * Structure:
 *     OpenAPI.BASE (config): input - API base URL from VITE_API_URL env var
 *     OpenAPI.TOKEN (config): input - JWT token from localStorage
 *     queryClient (QueryClient): config - TanStack Query client with auth error handling
 *     router (Router): config - TanStack Router from generated route tree
 *
 * Relationships:
 *     Consumes: client/OpenAPI, routeTree.gen, theme-provider, sonner
 *     Produces: Rendered React app in #root DOM element
 *
 * Semantics:
 *     Logic: [401/403 API errors clear token and redirect to /login,
 *             Dark theme default, strict mode enabled]
 */

import {
  MutationCache,
  QueryCache,
  QueryClient,
  QueryClientProvider,
} from "@tanstack/react-query"
import { createRouter, RouterProvider } from "@tanstack/react-router"
import { StrictMode } from "react"
import ReactDOM from "react-dom/client"
import { ApiError, OpenAPI } from "./client"
import { ThemeProvider } from "./components/theme-provider"
import { Toaster } from "./components/ui/sonner"
import "./index.css"
import { routeTree } from "./routeTree.gen"

OpenAPI.BASE = import.meta.env.VITE_API_URL
OpenAPI.TOKEN = async () => {
  return localStorage.getItem("access_token") || ""
}

/** Clear token and redirect to /login on 401/403 API errors. */
const handleApiError = (error: Error) => {
  if (error instanceof ApiError && [401, 403].includes(error.status)) {
    localStorage.removeItem("access_token")
    window.location.href = "/login"
  }
}
const queryClient = new QueryClient({
  queryCache: new QueryCache({
    onError: handleApiError,
  }),
  mutationCache: new MutationCache({
    onError: handleApiError,
  }),
})

const router = createRouter({ routeTree })
declare module "@tanstack/react-router" {
  interface Register {
    router: typeof router
  }
}

ReactDOM.createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <QueryClientProvider client={queryClient}>
        <RouterProvider router={router} />
        <Toaster richColors closeButton />
      </QueryClientProvider>
    </ThemeProvider>
  </StrictMode>,
)
