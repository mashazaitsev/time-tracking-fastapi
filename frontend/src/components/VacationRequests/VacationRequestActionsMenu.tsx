/**
 * @module VacationRequests/VacationRequestActionsMenu
 *
 * Purpose: Dropdown actions menu for vacation request row operations (edit, delete).
 *
 * Relationships:
 *     Consumes: EditVacationRequest, DeleteVacationRequest components
 *     Used by: Vacation requests table columns
 */

import { EllipsisVertical } from "lucide-react"
import { useState } from "react"

import type { VacationRequestPublic } from "@/client"
import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import DeleteVacationRequest from "./DeleteVacationRequest"
import EditVacationRequest from "./EditVacationRequest"

interface VacationRequestActionsMenuProps {
  vacationRequest: VacationRequestPublic
}

/**
 * Purpose: Dropdown menu with edit/delete actions for a vacation request table row.
 *
 * Structure:
 *     vacationRequest (VacationRequestPublic): input - Target vacation request for actions
 *
 * Relationships:
 *     Consumes: EditVacationRequest, DeleteVacationRequest components
 *     Used by: Vacation requests table actions column
 */
export const VacationRequestActionsMenu = ({
  vacationRequest,
}: VacationRequestActionsMenuProps) => {
  const [open, setOpen] = useState(false)

  return (
    <DropdownMenu open={open} onOpenChange={setOpen}>
      <DropdownMenuTrigger asChild>
        <Button variant="ghost" size="icon">
          <EllipsisVertical />
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        <EditVacationRequest
          vacationRequest={vacationRequest}
          onSuccess={() => setOpen(false)}
        />
        <DeleteVacationRequest
          id={vacationRequest.id}
          onSuccess={() => setOpen(false)}
        />
      </DropdownMenuContent>
    </DropdownMenu>
  )
}
