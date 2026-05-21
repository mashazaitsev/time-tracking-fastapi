/**
 * @module Admin/columns
 *
 * Purpose: Column definitions for the admin users data table.
 *
 * Relationships:
 *     Consumes: UserActionsMenu component, UserPublic type
 *     Used by: Admin users page DataTable
 */

import type { ColumnDef } from "@tanstack/react-table"

import type { UserPublic } from "@/client"
import { Badge } from "@/components/ui/badge"
import { cn } from "@/lib/utils"
import { UserActionsMenu } from "./UserActionsMenu"

/**
 * Purpose: Extended user type with current-user indicator for table rendering.
 *
 * Structure:
 *     isCurrentUser (boolean): Flags whether this row represents the logged-in user
 */
export type UserTableData = UserPublic & {
  isCurrentUser: boolean
}

/**
 * Purpose: TanStack Table column definitions for the admin users table.
 *
 * Structure:
 *     full_name: Displays name with "You" badge for current user
 *     email: User email address
 *     is_superuser: Role badge (Superuser/User)
 *     is_active: Status indicator with colored dot
 *     actions: UserActionsMenu dropdown
 *
 * Relationships:
 *     Consumes: UserActionsMenu component
 *     Used by: Admin page DataTable
 */
export const columns: ColumnDef<UserTableData>[] = [
  {
    accessorKey: "full_name",
    header: "Full Name",
    cell: ({ row }) => {
      const fullName = row.original.full_name
      return (
        <div className="flex items-center gap-2">
          <span
            className={cn("font-medium", !fullName && "text-muted-foreground")}
          >
            {fullName || "N/A"}
          </span>
          {row.original.isCurrentUser && (
            <Badge variant="outline" className="text-xs">
              You
            </Badge>
          )}
        </div>
      )
    },
  },
  {
    accessorKey: "email",
    header: "Email",
    cell: ({ row }) => (
      <span className="text-muted-foreground">{row.original.email}</span>
    ),
  },
  {
    accessorKey: "is_superuser",
    header: "Role",
    cell: ({ row }) => (
      <Badge variant={row.original.is_superuser ? "default" : "secondary"}>
        {row.original.is_superuser ? "Superuser" : "User"}
      </Badge>
    ),
  },
  {
    accessorKey: "is_active",
    header: "Status",
    cell: ({ row }) => (
      <div className="flex items-center gap-2">
        <span
          className={cn(
            "size-2 rounded-full",
            row.original.is_active ? "bg-green-500" : "bg-gray-400",
          )}
        />
        <span className={row.original.is_active ? "" : "text-muted-foreground"}>
          {row.original.is_active ? "Active" : "Inactive"}
        </span>
      </div>
    ),
  },
  {
    id: "actions",
    header: () => <span className="sr-only">Actions</span>,
    cell: ({ row }) => (
      <div className="flex justify-end">
        <UserActionsMenu user={row.original} />
      </div>
    ),
  },
]
