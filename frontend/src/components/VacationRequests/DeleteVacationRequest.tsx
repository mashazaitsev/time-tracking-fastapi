/**
 * @module VacationRequests/DeleteVacationRequest
 *
 * Purpose: Confirmation dialog for deleting a vacation request.
 *
 * Relationships:
 *     Consumes: VacationRequestsService.deleteVacationRequest API
 *     Used by: VacationRequestActionsMenu dropdown
 */

import { useMutation, useQueryClient } from "@tanstack/react-query"
import { Trash2 } from "lucide-react"
import { useState } from "react"
import { useForm } from "react-hook-form"

import { VacationRequestsService } from "@/client"
import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog"
import { DropdownMenuItem } from "@/components/ui/dropdown-menu"
import { LoadingButton } from "@/components/ui/loading-button"
import useCustomToast from "@/hooks/useCustomToast"
import { handleError } from "@/utils"

interface DeleteVacationRequestProps {
  id: string
  onSuccess: () => void
}

/**
 * Purpose: Destructive confirmation dialog for permanently deleting a vacation request.
 *
 * Structure:
 *     id (string): input - Vacation request ID to delete
 *     onSuccess (function): input - Callback on successful deletion
 *
 * Relationships:
 *     Consumes: VacationRequestsService.deleteVacationRequest API
 *     Produces: Success toast, invalidates all query caches
 *
 * Flow:
 *     1. Render as dropdown menu item
 *     2. Open confirmation dialog on click
 *     3. Call deleteVacationRequest API on confirm
 *     4. Show success/error toast and invoke onSuccess callback
 */
const DeleteVacationRequest = ({ id, onSuccess }: DeleteVacationRequestProps) => {
  const [isOpen, setIsOpen] = useState(false)
  const queryClient = useQueryClient()
  const { showSuccessToast, showErrorToast } = useCustomToast()
  const { handleSubmit } = useForm()

  const deleteVacationRequest = async (id: string) => {
    await VacationRequestsService.deleteVacationRequest({ id: id })
  }

  const mutation = useMutation({
    mutationFn: deleteVacationRequest,
    onSuccess: () => {
      showSuccessToast("The vacation request was deleted successfully")
      setIsOpen(false)
      onSuccess()
    },
    onError: handleError.bind(showErrorToast),
    onSettled: () => {
      queryClient.invalidateQueries()
    },
  })

  const onSubmit = async () => {
    mutation.mutate(id)
  }

  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DropdownMenuItem
        variant="destructive"
        onSelect={(e) => e.preventDefault()}
        onClick={() => setIsOpen(true)}
      >
        <Trash2 />
        Delete Vacation Request
      </DropdownMenuItem>
      <DialogContent className="sm:max-w-md">
        <form onSubmit={handleSubmit(onSubmit)}>
          <DialogHeader>
            <DialogTitle>Delete Vacation Request</DialogTitle>
            <DialogDescription>
              This vacation request will be permanently deleted. Are you sure?
              You will not be able to undo this action.
            </DialogDescription>
          </DialogHeader>

          <DialogFooter className="mt-4">
            <DialogClose asChild>
              <Button variant="outline" disabled={mutation.isPending}>
                Cancel
              </Button>
            </DialogClose>
            <LoadingButton
              variant="destructive"
              type="submit"
              loading={mutation.isPending}
            >
              Delete
            </LoadingButton>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  )
}

export default DeleteVacationRequest
