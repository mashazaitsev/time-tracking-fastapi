/**
 * @module VacationRequests/columns
 *
 * Purpose: Column definitions for the vacation requests data table.
 *
 * Relationships:
 *     Consumes: VacationRequestActionsMenu component, VacationRequestPublic type, useAuth hook
 *     Used by: Vacation Requests page DataTable
 */

import type { ColumnDef } from "@tanstack/react-table"

import type { VacationRequestPublic } from "@/client"
import { Badge } from "@/components/ui/badge"
import { cn } from "@/lib/utils"
import useAuth from "@/hooks/useAuth"
import { VacationRequestActionsMenu } from "./VacationRequestActionsMenu"

/**
 * Purpose: TanStack Table column definitions for the vacation requests table.
 *
 * Structure:
 *     owner_id: Requester identifier
 *     start_date: Vacation start date
 *     end_date: Vacation end date
 *     reason: Truncated reason text
 *     status: Badge displaying request status
 *     created_at: Creation timestamp
 *     actions: Conditional actions menu (only for owner)
 *
 * Relationships:
 *     Consumes: VacationRequestActionsMenu, useAuth
 *     Used by: Vacation Requests page DataTable
 */
export const columns: ColumnDef<VacationRequestPublic>[] = [
  {
    accessorKey: "owner_id",
    header: "Requester",
    cell: ({ row }) => (
      <span className="font-medium">{row.original.owner_id}</span>
    ),
  },
  {
    accessorKey: "start_date",
    header: "Start Date",
    cell: ({ row }) => (
      <span className="text-muted-foreground">
        {new Date(row.original.start_date).toLocaleDateString()}
      </span>
    ),
  },
  {
    accessorKey: "end_date",
    header: "End Date",
    cell: ({ row }) => (
      <span className="text-muted-foreground">
        {new Date(row.original.end_date).toLocaleDateString()}
      </span>
    ),
  },
  {
    accessorKey: "reason",
    header: "Reason",
    cell: ({ row }) => {
      const reason = row.original.reason
      return (
        <span
          className={cn(
            "max-w-xs truncate block text-muted-foreground",
            !reason && "italic",
          )}
        >
          {reason || "No reason"}
        </span>
      )
    },
  },
  {
    accessorKey: "status",
    header: "Status",
    cell: ({ row }) => {
      const status = row.original.status
      return (
        <Badge
          variant={
            status === "approved"
              ? "default"
              : status === "rejected"
                ? "destructive"
                : "secondary"
          }
        >
          {status}
        </Badge>
      )
    },
  },
  {
    accessorKey: "created_at",
    header: "Created",
    cell: ({ row }) => (
      <span className="text-muted-foreground">
        {row.original.created_at
          ? new Date(row.original.created_at).toLocaleDateString()
          : "—"}
      </span>
    ),
  },
  {
    id: "actions",
    header: () => <span className="sr-only">Actions</span>,
    cell: function ActionsCell({ row }) {
      const { user } = useAuth()
      if (row.original.owner_id !== user?.id) {
        return null
      }
      return (
        <div className="flex justify-end">
          <VacationRequestActionsMenu vacationRequest={row.original} />
        </div>
      )
    },
  },
]
