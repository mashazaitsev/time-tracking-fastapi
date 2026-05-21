/**
 * @file Authenticated layout route — sidebar + header + footer wrapper with auth guard.
 * @module routes/_layout
 */

/**
 * Purpose: Provide authenticated layout wrapper with sidebar navigation and auth guard
 *
 * Structure:
 *     Route (FileRoute): config - TanStack route with beforeLoad auth check
 *     Layout (component): output - Sidebar + header + main content + footer
 *
 * Relationships:
 *     Consumes: hooks/useAuth.isLoggedIn, Sidebar/AppSidebar, Common/Footer
 *     Produces: Layout shell (wraps all /_layout/* child routes)
 *
 * Semantics:
 *     Logic: [Redirects to /login if not authenticated (beforeLoad guard)]
 */

import { createFileRoute, Outlet, redirect } from "@tanstack/react-router"

import { Footer } from "@/components/Common/Footer"
import AppSidebar from "@/components/Sidebar/AppSidebar"
import {
  SidebarInset,
  SidebarProvider,
  SidebarTrigger,
} from "@/components/ui/sidebar"
import { isLoggedIn } from "@/hooks/useAuth"

/**
 * Route config for /_layout. Redirects to /login if not authenticated.
 */
export const Route = createFileRoute("/_layout")({
  component: Layout,
  beforeLoad: async () => {
    if (!isLoggedIn()) {
      throw redirect({
        to: "/login",
      })
    }
  },
})

function Layout() {
  return (
    <SidebarProvider>
      <AppSidebar />
      <SidebarInset>
        <header className="sticky top-0 z-10 flex h-16 shrink-0 items-center gap-2 border-b px-4">
          <SidebarTrigger className="-ml-1 text-muted-foreground" />
        </header>
        <main className="flex-1 p-6 md:p-8">
          <div className="mx-auto max-w-7xl">
            <Outlet />
          </div>
        </main>
        <Footer />
      </SidebarInset>
    </SidebarProvider>
  )
}

export default Layout
