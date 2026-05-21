/**
 * @module Dashboard/TimeSummaryWidget
 *
 * Purpose: Display time tracking summary on the dashboard with total hours and per-project breakdown.
 *
 * Structure:
 *     summary (TimeSummary): input - Fetched time summary data from API
 *     isLoading (boolean): state - Whether the query is in progress
 *
 * Relationships:
 *     Consumes: TimeEntriesService.getSummary, formatDuration
 *     Produces: Dashboard summary card UI
 */

import { useQuery } from "@tanstack/react-query"

import { TimeEntriesService } from "@/client"
import { formatDuration } from "@/components/TimeEntries/columns"
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Skeleton } from "@/components/ui/skeleton"

/**
 * Purpose: Render loading skeleton matching the widget structure.
 */
function TimeSummarySkeleton() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Time Summary</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <Skeleton className="h-8 w-24" />
        <div className="space-y-2">
          <Skeleton className="h-4 w-full" />
          <Skeleton className="h-4 w-3/4" />
          <Skeleton className="h-4 w-1/2" />
        </div>
      </CardContent>
    </Card>
  )
}

/**
 * Purpose: Dashboard widget showing total hours logged and per-project breakdown.
 *
 * Structure:
 *     total_minutes (number): data - Total minutes from TimeSummary
 *     by_project (ProjectSummary[]): data - Per-project breakdown
 *
 * Relationships:
 *     Consumes: TimeEntriesService.getSummary
 *     Produces: Card with formatted total and project list
 */
export function TimeSummaryWidget() {
  const { data: summary, isLoading } = useQuery({
    queryKey: ["time-entries-summary"],
    queryFn: () => TimeEntriesService.getSummary(),
  })

  if (isLoading) {
    return <TimeSummarySkeleton />
  }

  const totalMinutes = summary?.total_minutes ?? 0
  const byProject = summary?.by_project ?? []

  return (
    <Card>
      <CardHeader>
        <CardTitle>Time Summary</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <div className="text-2xl font-bold">
          {totalMinutes === 0 ? (
            <span className="text-muted-foreground text-base font-normal">
              No time logged yet
            </span>
          ) : (
            formatDuration(totalMinutes)
          )}
        </div>
        <ul className="space-y-1">
          {byProject.map((project) => (
            <li
              key={project.project_id}
              className="flex items-center justify-between text-sm"
            >
              <span className="truncate">{project.project_name}</span>
              <span className="text-muted-foreground ml-2 shrink-0">
                {formatDuration(project.total_minutes)}
              </span>
            </li>
          ))}
        </ul>
      </CardContent>
    </Card>
  )
}
