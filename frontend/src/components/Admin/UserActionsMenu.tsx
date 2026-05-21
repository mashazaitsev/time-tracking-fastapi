/**
 * @module Admin/UserActionsMenu
 *
 * Purpose: Dropdown actions menu for user row operations (edit, delete).
 *
 * Relationships:
 *     Consumes: EditUser, DeleteUser components
 *     Used by: Admin users table columns
 */

import { EllipsisVertical } from "lucide-react"
import { useState } from "react"

import type { UserPublic } from "@/client"
import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import useAuth from "@/hooks/useAuth"
import DeleteUser from "./DeleteUser"
import EditUser from "./EditUser"

/**
 * Purpose: Props for UserActionsMenu component.
 *
 * Structure:
 *     user (UserPublic): input - User data for the row actions
 */
interface UserActionsMenuProps {
  user: UserPublic
}

/**
 * Purpose: Dropdown menu with edit/delete actions for a user table row.
 *
 * Structure:
 *     user (UserPublic): input - Target user for actions
 *
 * Relationships:
 *     Consumes: EditUser, DeleteUser components; useAuth for current user check
 *     Used by: Admin users table actions column
 *
 * Flow:
 *     1. Hide menu if target user is the current logged-in user
 *     2. Render ellipsis trigger button
 *     3. Show EditUser and DeleteUser options in dropdown
 */
export const UserActionsMenu = ({ user }: UserActionsMenuProps) => {
  const [open, setOpen] = useState(false)
  const { user: currentUser } = useAuth()

  if (user.id === currentUser?.id) {
    return null
  }

  return (
    <DropdownMenu open={open} onOpenChange={setOpen}>
      <DropdownMenuTrigger asChild>
        <Button variant="ghost" size="icon">
          <EllipsisVertical />
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        <EditUser user={user} onSuccess={() => setOpen(false)} />
        <DeleteUser id={user.id} onSuccess={() => setOpen(false)} />
      </DropdownMenuContent>
    </DropdownMenu>
  )
}
