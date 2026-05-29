/**
 * @file Vacation Requests route — listing page for all vacation requests.
 * @module routes/_layout/vacation-requests
 *
 * Purpose: Display vacation requests table with add, edit, and delete actions.
 *
 * Relationships:
 *     Consumes: VacationRequestsService.readVacationRequests, VacationRequests/AddVacationRequest, VacationRequests/columns
 *     Produces: Vacation requests data table with empty state and add-vacation-request button
 */

import { useSuspenseQuery } from "@tanstack/react-query"
import { createFileRoute } from "@tanstack/react-router"
import { Search } from "lucide-react"
import { Suspense } from "react"

import { VacationRequestsService } from "@/client"
import { DataTable } from "@/components/Common/DataTable"
import AddVacationRequest from "@/components/VacationRequests/AddVacationRequest"
import { columns } from "@/components/VacationRequests/columns"
import PendingVacationRequests from "@/components/VacationRequests/PendingVacationRequests"

/** TanStack Query options for fetching all vacation requests (up to 100). */
function getVacationRequestsQueryOptions() {
  return {
    queryFn: () =>
      VacationRequestsService.readVacationRequests({ skip: 0, limit: 100 }),
    queryKey: ["vacation-requests"],
  }
}

/**
 * Route config for /_layout/vacation-requests.
 */
export const Route = createFileRoute("/_layout/vacation-requests")({
  component: VacationRequests,
  head: () => ({
    meta: [
      {
        title: "Vacation Requests - FastAPI Template",
      },
    ],
  }),
})

/** Fetches vacation requests via suspense query; shows empty state or DataTable. */
function VacationRequestsTableContent() {
  const { data: vacationRequests } = useSuspenseQuery(
    getVacationRequestsQueryOptions(),
  )

  if (!vacationRequests?.data || vacationRequests.data.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center text-center py-12">
        <div className="rounded-full bg-muted p-4 mb-4">
          <Search className="h-8 w-8 text-muted-foreground" />
        </div>
        <h3 className="text-lg font-semibold">No vacation requests</h3>
        <p className="text-muted-foreground">
          Add a new vacation request to get started
        </p>
      </div>
    )
  }

  return <DataTable columns={columns} data={vacationRequests.data} />
}

/** Suspense wrapper for VacationRequestsTableContent with PendingVacationRequests fallback. */
function VacationRequestsTable() {
  return (
    <Suspense fallback={<PendingVacationRequests />}>
      <VacationRequestsTableContent />
    </Suspense>
  )
}

/**
 * Purpose: Vacation requests listing page with data table and add-vacation-request action.
 *
 * Structure:
 *     vacationRequests (VacationRequestPublic[]): input - All vacation requests fetched via VacationRequestsService
 *
 * Relationships:
 *     Consumes: VacationRequestsService.readVacationRequests, VacationRequests/AddVacationRequest, VacationRequests/columns
 *     Produces: Vacation requests data table with empty state and add-vacation-request button
 */
function VacationRequests() {
  return (
    <div className="flex flex-col gap-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight">
            Vacation Requests
          </h1>
          <p className="text-muted-foreground">
            View and manage vacation requests
          </p>
        </div>
        <AddVacationRequest />
      </div>
      <VacationRequestsTable />
    </div>
  )
}
