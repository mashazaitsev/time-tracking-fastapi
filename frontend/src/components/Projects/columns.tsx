/**
 * @module Projects/columns
 *
 * Purpose: Column definitions for the projects data table.
 *
 * Relationships:
 *     Consumes: ProjectActionsMenu component, ProjectPublic type
 *     Used by: Projects page DataTable
 */

import type { ColumnDef } from "@tanstack/react-table"

import type { ProjectPublic } from "@/client"
import { cn } from "@/lib/utils"
import { ProjectActionsMenu } from "./ProjectActionsMenu"

/**
 * Purpose: TanStack Table column definitions for the projects table.
 *
 * Structure:
 *     name: Project name
 *     description: Truncated description with fallback text
 *     created_at: Formatted creation date
 *     actions: ProjectActionsMenu dropdown
 *
 * Relationships:
 *     Consumes: ProjectActionsMenu component
 *     Used by: Projects page DataTable
 */
export const columns: ColumnDef<ProjectPublic>[] = [
  {
    accessorKey: "name",
    header: "Name",
    cell: ({ row }) => (
      <span className="font-medium">{row.original.name}</span>
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
    accessorKey: "created_at",
    header: "Created",
    cell: ({ row }) => {
      const createdAt = row.original.created_at
      return (
        <span className="text-muted-foreground">
          {createdAt ? new Date(createdAt).toLocaleDateString() : "—"}
        </span>
      )
    },
  },
  {
    id: "actions",
    header: () => <span className="sr-only">Actions</span>,
    cell: ({ row }) => (
      <div className="flex justify-end">
        <ProjectActionsMenu project={row.original} />
      </div>
    ),
  },
]
