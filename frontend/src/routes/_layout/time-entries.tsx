/**
 * @file Time Entries route — CRUD listing page for user time entries.
 * @module routes/_layout/time-entries
 *
 * Purpose: Display paginated time entries table with add, edit, and delete actions.
 *
 * Relationships:
 *     Consumes: TimeEntriesService.readTimeEntries, TimeEntries/AddTimeEntry, TimeEntries/columns
 *     Produces: Time entries data table with empty state and add-time-entry button
 */

import { useSuspenseQuery } from "@tanstack/react-query"
import { createFileRoute } from "@tanstack/react-router"
import { Search } from "lucide-react"
import { Suspense } from "react"

import { TimeEntriesService } from "@/client"
import { DataTable } from "@/components/Common/DataTable"
import AddTimeEntry from "@/components/TimeEntries/AddTimeEntry"
import { columns } from "@/components/TimeEntries/columns"
import PendingTimeEntries from "@/components/TimeEntries/PendingTimeEntries"

/** TanStack Query options for fetching all time entries (up to 100). */
function getTimeEntriesQueryOptions() {
  return {
    queryFn: () => TimeEntriesService.readTimeEntries({ skip: 0, limit: 100 }),
    queryKey: ["time-entries"],
  }
}

/**
 * Route config for /_layout/time-entries.
 */
export const Route = createFileRoute("/_layout/time-entries")({
  component: TimeEntries,
  head: () => ({
    meta: [
      {
        title: "Time Entries - FastAPI Template",
      },
    ],
  }),
})

/** Fetches time entries via suspense query; shows empty state or DataTable. */
function TimeEntriesTableContent() {
  const { data: timeEntries } = useSuspenseQuery(getTimeEntriesQueryOptions())

  if (!timeEntries?.data || timeEntries.data.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center text-center py-12">
        <div className="rounded-full bg-muted p-4 mb-4">
          <Search className="h-8 w-8 text-muted-foreground" />
        </div>
        <h3 className="text-lg font-semibold">No time entries</h3>
        <p className="text-muted-foreground">
          Add a new time entry to get started
        </p>
      </div>
    )
  }

  return <DataTable columns={columns} data={timeEntries.data} />
}

/** Suspense wrapper for TimeEntriesTableContent with PendingTimeEntries fallback. */
function TimeEntriesTable() {
  return (
    <Suspense fallback={<PendingTimeEntries />}>
      <TimeEntriesTableContent />
    </Suspense>
  )
}

/**
 * Purpose: Time entries listing page with data table and add-time-entry action.
 *
 * Structure:
 *     timeEntries (TimeEntryPublic[]): input - All time entries fetched via TimeEntriesService
 *
 * Relationships:
 *     Consumes: TimeEntriesService.readTimeEntries, TimeEntries/AddTimeEntry, TimeEntries/columns
 *     Produces: Time entries data table with empty state and add-time-entry button
 */
function TimeEntries() {
  return (
    <div className="flex flex-col gap-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight">Time Entries</h1>
          <p className="text-muted-foreground">
            Log and manage your time entries
          </p>
        </div>
        <AddTimeEntry />
      </div>
      <TimeEntriesTable />
    </div>
  )
}
