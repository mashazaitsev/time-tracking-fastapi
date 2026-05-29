/**
 * @module VacationRequests/EditVacationRequest
 *
 * Purpose: Dialog for editing existing vacation request details.
 *
 * Relationships:
 *     Consumes: VacationRequestsService.updateVacationRequest API
 *     Used by: VacationRequestActionsMenu dropdown
 */

import { zodResolver } from "@hookform/resolvers/zod"
import { useMutation, useQueryClient } from "@tanstack/react-query"
import { Pencil } from "lucide-react"
import { useState } from "react"
import { useForm } from "react-hook-form"
import { z } from "zod"

import { VacationRequestsService } from "@/client"
import type { VacationRequestPublic } from "@/client"
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
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"
import { LoadingButton } from "@/components/ui/loading-button"
import useCustomToast from "@/hooks/useCustomToast"
import { handleError } from "@/utils"

const formSchema = z
  .object({
    start_date: z.string().min(1, "Start date is required"),
    end_date: z.string().min(1, "End date is required"),
    reason: z
      .string()
      .min(1, "Reason is required")
      .max(500, "Reason must be 500 characters or less"),
  })
  .refine((data) => data.end_date >= data.start_date, {
    message: "End date must be on or after start date",
    path: ["end_date"],
  })

type FormData = z.infer<typeof formSchema>

interface EditVacationRequestProps {
  vacationRequest: VacationRequestPublic
  onSuccess: () => void
}

/**
 * Purpose: Modal dialog for editing vacation request dates and reason.
 *
 * Structure:
 *     vacationRequest (VacationRequestPublic): input - Existing vacation request data
 *     onSuccess (function): input - Callback on successful update
 *     formSchema (zod): Validates start_date, end_date (>= start_date), reason (1–500 chars)
 *
 * Relationships:
 *     Consumes: VacationRequestsService.updateVacationRequest API
 *     Produces: Updated vacation request record, success toast, invalidates "vacation-requests" query cache
 *
 * Flow:
 *     1. Render as dropdown menu item
 *     2. Open dialog pre-populated with current vacation request data
 *     3. Validate and submit updated fields
 *     4. Show success/error toast and invoke onSuccess callback
 */
const EditVacationRequest = ({
  vacationRequest,
  onSuccess,
}: EditVacationRequestProps) => {
  const [isOpen, setIsOpen] = useState(false)
  const queryClient = useQueryClient()
  const { showSuccessToast, showErrorToast } = useCustomToast()

  const form = useForm<FormData>({
    resolver: zodResolver(formSchema),
    mode: "onBlur",
    criteriaMode: "all",
    defaultValues: {
      start_date: vacationRequest.start_date,
      end_date: vacationRequest.end_date,
      reason: vacationRequest.reason,
    },
  })

  const mutation = useMutation({
    mutationFn: (data: FormData) => {
      return VacationRequestsService.updateVacationRequest({
        id: vacationRequest.id,
        requestBody: {
          start_date: data.start_date,
          end_date: data.end_date,
          reason: data.reason,
        },
      })
    },
    onSuccess: () => {
      showSuccessToast("Vacation request updated successfully")
      setIsOpen(false)
      onSuccess()
    },
    onError: handleError.bind(showErrorToast),
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["vacation-requests"] })
    },
  })

  const onSubmit = (data: FormData) => {
    mutation.mutate(data)
  }

  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DropdownMenuItem
        onSelect={(e) => e.preventDefault()}
        onClick={() => setIsOpen(true)}
      >
        <Pencil />
        Edit Vacation Request
      </DropdownMenuItem>
      <DialogContent className="sm:max-w-md">
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)}>
            <DialogHeader>
              <DialogTitle>Edit Vacation Request</DialogTitle>
              <DialogDescription>
                Update the vacation request details below.
              </DialogDescription>
            </DialogHeader>
            <div className="grid gap-4 py-4">
              <FormField
                control={form.control}
                name="start_date"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>
                      Start Date <span className="text-destructive">*</span>
                    </FormLabel>
                    <FormControl>
                      <Input type="date" {...field} required />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="end_date"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>
                      End Date <span className="text-destructive">*</span>
                    </FormLabel>
                    <FormControl>
                      <Input type="date" {...field} required />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="reason"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>
                      Reason <span className="text-destructive">*</span>
                    </FormLabel>
                    <FormControl>
                      <Textarea
                        placeholder="Reason for vacation request"
                        {...field}
                        required
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
            </div>

            <DialogFooter>
              <DialogClose asChild>
                <Button variant="outline" disabled={mutation.isPending}>
                  Cancel
                </Button>
              </DialogClose>
              <LoadingButton type="submit" loading={mutation.isPending}>
                Save
              </LoadingButton>
            </DialogFooter>
          </form>
        </Form>
      </DialogContent>
    </Dialog>
  )
}

export default EditVacationRequest
