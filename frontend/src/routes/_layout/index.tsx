/**
 * @file Dashboard route — authenticated home page with user greeting and time summary.
 * @module routes/_layout/index
 */

import { createFileRoute } from "@tanstack/react-router"

import { TimeSummaryWidget } from "@/components/Dashboard/TimeSummaryWidget"
import useAuth from "@/hooks/useAuth"

/**
 * Route config for /_layout/ (dashboard index).
 */
export const Route = createFileRoute("/_layout/")({
  component: Dashboard,
  head: () => ({
    meta: [
      {
        title: "Dashboard - FastAPI Template",
      },
    ],
  }),
})

/**
 * Purpose: Dashboard home page displaying welcome greeting and time tracking summary.
 *
 * Structure:
 *     currentUser (UserPublic): input - Current authenticated user from useAuth
 *
 * Relationships:
 *     Consumes: useAuth.user, TimeSummaryWidget
 *     Produces: Greeting UI + time summary widget
 */
function Dashboard() {
  const { user: currentUser } = useAuth()

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-2xl truncate max-w-sm">
          Hi, {currentUser?.full_name || currentUser?.email} 👋
        </h1>
        <p className="text-muted-foreground">
          Welcome back, nice to see you again!!!
        </p>
      </div>
      <TimeSummaryWidget />
    </div>
  )
}
