/**
 * @module TimeEntries/columns
 *
 * Purpose: Column definitions for the time entries data table.
 *
 * Relationships:
 *     Consumes: TimeEntryActionsMenu component, TimeEntryPublic type
 *     Used by: Time Entries page DataTable
 */

import type { ColumnDef } from "@tanstack/react-table"

import type { TimeEntryPublic } from "@/client"
import { cn } from "@/lib/utils"
import { TimeEntryActionsMenu } from "./TimeEntryActionsMenu"

/**
 * Purpose: Format duration in minutes to "Xh Ym" string.
 *
 * Structure:
 *     minutes (number): input - Duration in minutes (≥ 1)
 *     formatted (string): output - e.g. "3h 45m"
 */
export function formatDuration(minutes: number): string {
  const hours = Math.floor(minutes / 60)
  const mins = minutes % 60
  if (hours === 0) return `${mins}m`
  if (mins === 0) return `${hours}h`
  return `${hours}h ${mins}m`
}

/**
 * Purpose: Parse "Xh Ym" formatted string back to minutes.
 *
 * Structure:
 *     formatted (string): input - Duration string like "3h 45m"
 *     minutes (number): output - Total minutes
 */
export function parseDuration(formatted: string): number {
  let total = 0
  const hoursMatch = formatted.match(/(\d+)h/)
  const minsMatch = formatted.match(/(\d+)m/)
  if (hoursMatch) total += parseInt(hoursMatch[1], 10) * 60
  if (minsMatch) total += parseInt(minsMatch[1], 10)
  return total
}

/**
 * Purpose: TanStack Table column definitions for the time entries table.
 *
 * Structure:
 *     project_name: Resolved project name (from project_id for now)
 *     date: Entry date
 *     duration_minutes: Formatted as "Xh Ym"
 *     description: Truncated description with fallback text
 *     actions: TimeEntryActionsMenu dropdown
 *
 * Relationships:
 *     Consumes: TimeEntryActionsMenu component
 *     Used by: Time Entries page DataTable
 */
export const columns: ColumnDef<TimeEntryPublic>[] = [
  {
    accessorKey: "project_id",
    header: "Project",
    cell: ({ row }) => (
      <span className="font-medium">{row.original.project_id}</span>
    ),
  },
  {
    accessorKey: "date",
    header: "Date",
    cell: ({ row }) => (
      <span className="text-muted-foreground">
        {new Date(row.original.date).toLocaleDateString()}
      </span>
    ),
  },
  {
    accessorKey: "duration_minutes",
    header: "Duration",
    cell: ({ row }) => (
      <span className="text-muted-foreground">
        {formatDuration(row.original.duration_minutes)}
      </span>
    ),
  },
  {
    accessorKey: "description",
    header: "Description",
    cell: ({ row }) => {
      const description = row.original.description
      return (
        <span
          className={cn(
            "max-w-xs truncate block text-muted-foreground",
            !description && "italic",
          )}
        >
          {description || "No description"}
        </span>
      )
    },
  },
  {
    id: "actions",
    header: () => <span className="sr-only">Actions</span>,
    cell: ({ row }) => (
      <div className="flex justify-end">
        <TimeEntryActionsMenu timeEntry={row.original} />
      </div>
    ),
  },
]
