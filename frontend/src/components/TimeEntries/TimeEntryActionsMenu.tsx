/**
 * @module TimeEntries/TimeEntryActionsMenu
 *
 * Purpose: Dropdown actions menu for time entry row operations (edit, delete).
 *
 * Relationships:
 *     Consumes: EditTimeEntry, DeleteTimeEntry components
 *     Used by: Time entries table columns
 */

import { EllipsisVertical } from "lucide-react"
import { useState } from "react"

import type { TimeEntryPublic } from "@/client"
import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import DeleteTimeEntry from "./DeleteTimeEntry"
import EditTimeEntry from "./EditTimeEntry"

interface TimeEntryActionsMenuProps {
  timeEntry: TimeEntryPublic
}

/**
 * Purpose: Dropdown menu with edit/delete actions for a time entry table row.
 *
 * Structure:
 *     timeEntry (TimeEntryPublic): input - Target time entry for actions
 *
 * Relationships:
 *     Consumes: EditTimeEntry, DeleteTimeEntry components
 *     Used by: Time entries table actions column
 */
export const TimeEntryActionsMenu = ({
  timeEntry,
}: TimeEntryActionsMenuProps) => {
  const [open, setOpen] = useState(false)

  return (
    <DropdownMenu open={open} onOpenChange={setOpen}>
      <DropdownMenuTrigger asChild>
        <Button variant="ghost" size="icon">
          <EllipsisVertical />
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        <EditTimeEntry timeEntry={timeEntry} onSuccess={() => setOpen(false)} />
        <DeleteTimeEntry id={timeEntry.id} onSuccess={() => setOpen(false)} />
      </DropdownMenuContent>
    </DropdownMenu>
  )
}
