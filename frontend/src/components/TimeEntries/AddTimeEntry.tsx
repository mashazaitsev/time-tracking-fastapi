/**
 * @module TimeEntries/AddTimeEntry
 *
 * Purpose: Dialog for creating new time entries with project, date, duration, and description.
 *
 * Relationships:
 *     Consumes: TimeEntriesService.createTimeEntry API, ProjectsService.readProjects API
 *     Used by: Time Entries management page
 */

import { zodResolver } from "@hookform/resolvers/zod"
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query"
import { Plus } from "lucide-react"
import { useState } from "react"
import { useForm } from "react-hook-form"
import { z } from "zod"

import {
  type TimeEntryCreate,
  ProjectsService,
  TimeEntriesService,
} from "@/client"
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
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import { LoadingButton } from "@/components/ui/loading-button"
import useCustomToast from "@/hooks/useCustomToast"
import { handleError } from "@/utils"

const formSchema = z.object({
  project_id: z.string().min(1, { message: "Project is required" }),
  date: z.string().min(1, { message: "Date is required" }),
  duration_minutes: z.string().min(1, { message: "Duration is required" }),
  description: z
    .string()
    .max(255, { message: "Description must be 255 characters or less" })
    .optional(),
})

type FormData = z.infer<typeof formSchema>

/**
 * Purpose: Modal dialog for creating a new time entry with project select, date, duration, and optional description.
 *
 * Structure:
 *     isOpen (boolean): internal - Dialog visibility state
 *     formSchema (zod): Validates project_id (required), date (required), duration_minutes (min 1), description (optional, max 255)
 *
 * Relationships:
 *     Consumes: TimeEntriesService.createTimeEntry API, ProjectsService.readProjects API
 *     Produces: New time entry record, success toast, invalidates "time-entries" query cache
 *
 * Flow:
 *     1. Open dialog via trigger button
 *     2. Fetch user's projects for select dropdown
 *     3. Validate all fields client-side (Zod min(1) on duration_minutes)
 *     4. Call createTimeEntry API on submit
 *     5. Show success/error toast and close dialog
 */
const AddTimeEntry = () => {
  const [isOpen, setIsOpen] = useState(false)
  const queryClient = useQueryClient()
  const { showSuccessToast, showErrorToast } = useCustomToast()

  const { data: projectsData } = useQuery({
    queryKey: ["projects"],
    queryFn: () => ProjectsService.readProjects({}),
  })

  const form = useForm<FormData>({
    resolver: zodResolver(formSchema),
    mode: "onBlur",
    criteriaMode: "all",
    defaultValues: {
      project_id: "",
      date: "",
      duration_minutes: "",
      description: "",
    },
  })

  const mutation = useMutation({
    mutationFn: (data: TimeEntryCreate) =>
      TimeEntriesService.createTimeEntry({ requestBody: data }),
    onSuccess: () => {
      showSuccessToast("Time entry created successfully")
      form.reset()
      setIsOpen(false)
    },
    onError: handleError.bind(showErrorToast),
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["time-entries"] })
    },
  })

  const onSubmit = (data: FormData) => {
    const minutes = parseInt(data.duration_minutes, 10)
    if (isNaN(minutes) || minutes < 1) return
    mutation.mutate({
      project_id: data.project_id,
      date: data.date,
      duration_minutes: minutes,
      description: data.description || null,
    })
  }

  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DialogTrigger asChild>
        <Button className="my-4">
          <Plus className="mr-2" />
          Add Time Entry
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-md">
        <DialogHeader>
          <DialogTitle>Add Time Entry</DialogTitle>
          <DialogDescription>
            Fill in the details to log a new time entry.
          </DialogDescription>
        </DialogHeader>
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)}>
            <div className="grid gap-4 py-4">
              <FormField
                control={form.control}
                name="project_id"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>
                      Project <span className="text-destructive">*</span>
                    </FormLabel>
                    <Select
                      onValueChange={field.onChange}
                      defaultValue={field.value}
                    >
                      <FormControl>
                        <SelectTrigger>
                          <SelectValue placeholder="Select a project" />
                        </SelectTrigger>
                      </FormControl>
                      <SelectContent>
                        {projectsData?.data.map((project) => (
                          <SelectItem key={project.id} value={project.id}>
                            {project.name}
                          </SelectItem>
                        ))}
                      </SelectContent>
                    </Select>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="date"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>
                      Date <span className="text-destructive">*</span>
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
                name="duration_minutes"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>
                      Duration (minutes){" "}
                      <span className="text-destructive">*</span>
                    </FormLabel>
                    <FormControl>
                      <Input
                        placeholder="e.g. 90"
                        type="number"
                        min={1}
                        {...field}
                        required
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="description"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Description</FormLabel>
                    <FormControl>
                      <Input placeholder="Description" type="text" {...field} />
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

export default AddTimeEntry
