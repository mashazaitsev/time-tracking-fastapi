/**
 * @file Root route — top-level layout with devtools and error boundaries.
 * @module routes/__root
 */

import { ReactQueryDevtools } from "@tanstack/react-query-devtools"
import { createRootRoute, HeadContent, Outlet } from "@tanstack/react-router"
import { TanStackRouterDevtools } from "@tanstack/react-router-devtools"
import ErrorComponent from "@/components/Common/ErrorComponent"
import NotFound from "@/components/Common/NotFound"

/**
 * Purpose: Root route wrapping all pages with HeadContent, Outlet, and devtools
 *
 * Structure:
 *     component: output - Renders HeadContent + Outlet + Router/Query devtools
 *     notFoundComponent: output - Renders NotFound for unmatched routes
 *     errorComponent: output - Renders ErrorComponent for uncaught errors
 *
 * Relationships:
 *     Consumes: Common/NotFound, Common/ErrorComponent
 *     Produces: Root layout shell for all child routes
 */
export const Route = createRootRoute({
  component: () => (
    <>
      <HeadContent />
      <Outlet />
      <TanStackRouterDevtools position="bottom-right" />
      <ReactQueryDevtools initialIsOpen={false} />
    </>
  ),
  notFoundComponent: () => <NotFound />,
  errorComponent: () => <ErrorComponent />,
})
