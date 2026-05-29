/**
 * @module VacationRequests/AddVacationRequest
 *
 * Purpose: Dialog for creating new vacation requests with start date, end date, and reason.
 *
 * Relationships:
 *     Consumes: VacationRequestsService.createVacationRequest API
 *     Used by: Vacation Requests management page
 */

import { zodResolver } from "@hookform/resolvers/zod"
import { useMutation, useQueryClient } from "@tanstack/react-query"
import { Plus } from "lucide-react"
import { useState } from "react"
import { useForm } from "react-hook-form"
import { z } from "zod"

import { VacationRequestsService } from "@/client"
import type { VacationRequestCreate } from "@/client"
import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
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

/**
 * Purpose: Modal dialog for creating a new vacation request with date range and reason.
 *
 * Structure:
 *     isOpen (boolean): internal - Dialog visibility state
 *     formSchema (zod): Validates start_date (required), end_date (required, >= start_date), reason (1–500 chars)
 *
 * Relationships:
 *     Consumes: VacationRequestsService.createVacationRequest API
 *     Produces: New vacation request record, success toast, invalidates "vacation-requests" query cache
 *
 * Flow:
 *     1. Open dialog via trigger button
 *     2. Validate all fields client-side (Zod with refine for date range)
 *     3. Call createVacationRequest API on submit
 *     4. Show success/error toast and close dialog
 */
const AddVacationRequest = () => {
  const [isOpen, setIsOpen] = useState(false)
  const queryClient = useQueryClient()
  const { showSuccessToast, showErrorToast } = useCustomToast()

  const form = useForm<FormData>({
    resolver: zodResolver(formSchema),
    mode: "onBlur",
    criteriaMode: "all",
    defaultValues: {
      start_date: "",
      end_date: "",
      reason: "",
    },
  })

  const mutation = useMutation({
    mutationFn: (data: VacationRequestCreate) =>
      VacationRequestsService.createVacationRequest({ requestBody: data }),
    onSuccess: () => {
      showSuccessToast("Vacation request created successfully")
      form.reset()
      setIsOpen(false)
    },
    onError: handleError.bind(showErrorToast),
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["vacation-requests"] })
    },
  })

  const onSubmit = (data: FormData) => {
    mutation.mutate({
      start_date: data.start_date,
      end_date: data.end_date,
      reason: data.reason,
    })
  }

  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DialogTrigger asChild>
        <Button className="my-4">
          <Plus className="mr-2" />
          Add Vacation Request
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-md">
        <DialogHeader>
          <DialogTitle>Add Vacation Request</DialogTitle>
          <DialogDescription>
            Fill in the details to create a new vacation request.
          </DialogDescription>
        </DialogHeader>
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)}>
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

export default AddVacationRequest
