/**
 * @module Items/DeleteItem
 *
 * Purpose: Confirmation dialog for deleting an item.
 *
 * Relationships:
 *     Consumes: ItemsService.deleteItem API
 *     Used by: ItemActionsMenu dropdown
 */

import { useMutation, useQueryClient } from "@tanstack/react-query"
import { Trash2 } from "lucide-react"
import { useState } from "react"
import { useForm } from "react-hook-form"

import { ItemsService } from "@/client"
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

/**
 * Purpose: Props for DeleteItem dialog component.
 *
 * Structure:
 *     id (string): input - Item ID to delete
 *     onSuccess (function): input - Callback after successful deletion
 */
interface DeleteItemProps {
  id: string
  onSuccess: () => void
}

/**
 * Purpose: Destructive confirmation dialog for permanently deleting an item.
 *
 * Structure:
 *     id (string): input - Item ID to delete
 *     onSuccess (function): input - Callback on successful deletion
 *
 * Relationships:
 *     Consumes: ItemsService.deleteItem API
 *     Produces: Success toast, invalidates all query caches
 *
 * Flow:
 *     1. Render as dropdown menu item
 *     2. Open confirmation dialog on click
 *     3. Call deleteItem API on confirm
 *     4. Show success/error toast and invoke onSuccess callback
 */
const DeleteItem = ({ id, onSuccess }: DeleteItemProps) => {
  const [isOpen, setIsOpen] = useState(false)
  const queryClient = useQueryClient()
  const { showSuccessToast, showErrorToast } = useCustomToast()
  const { handleSubmit } = useForm()

  const deleteItem = async (id: string) => {
    await ItemsService.deleteItem({ id: id })
  }

  const mutation = useMutation({
    mutationFn: deleteItem,
    onSuccess: () => {
      showSuccessToast("The item was deleted successfully")
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
        Delete Item
      </DropdownMenuItem>
      <DialogContent className="sm:max-w-md">
        <form onSubmit={handleSubmit(onSubmit)}>
          <DialogHeader>
            <DialogTitle>Delete Item</DialogTitle>
            <DialogDescription>
              This item will be permanently deleted. Are you sure? You will not
              be able to undo this action.
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

export default DeleteItem
