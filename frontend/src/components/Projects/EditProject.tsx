/**
 * @module Projects/EditProject
 *
 * Purpose: Dialog for editing existing project details.
 *
 * Relationships:
 *     Consumes: ProjectsService.updateProject API
 *     Used by: ProjectActionsMenu dropdown
 */

import { zodResolver } from "@hookform/resolvers/zod"
import { useMutation, useQueryClient } from "@tanstack/react-query"
import { Pencil } from "lucide-react"
import { useState } from "react"
import { useForm } from "react-hook-form"
import { z } from "zod"

import { type ProjectPublic, ProjectsService } from "@/client"
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
import { LoadingButton } from "@/components/ui/loading-button"
import useCustomToast from "@/hooks/useCustomToast"
import { handleError } from "@/utils"

const formSchema = z.object({
  name: z
    .string()
    .min(1, { message: "Name is required" })
    .max(255, { message: "Name must be 255 characters or less" }),
  description: z
    .string()
    .max(255, { message: "Description must be 255 characters or less" })
    .optional(),
})

type FormData = z.infer<typeof formSchema>

interface EditProjectProps {
  project: ProjectPublic
  onSuccess: () => void
}

/**
 * Purpose: Modal dialog for editing project name and description.
 *
 * Structure:
 *     project (ProjectPublic): input - Existing project data
 *     onSuccess (function): input - Callback on successful update
 *     formSchema (zod): Validates required name (1-255 chars) and optional description (max 255)
 *
 * Relationships:
 *     Consumes: ProjectsService.updateProject API
 *     Produces: Updated project record, success toast, invalidates "projects" query cache
 *
 * Flow:
 *     1. Render as dropdown menu item
 *     2. Open dialog pre-populated with current project data
 *     3. Validate and submit updated fields
 *     4. Show success/error toast and invoke onSuccess callback
 */
const EditProject = ({ project, onSuccess }: EditProjectProps) => {
  const [isOpen, setIsOpen] = useState(false)
  const queryClient = useQueryClient()
  const { showSuccessToast, showErrorToast } = useCustomToast()

  const form = useForm<FormData>({
    resolver: zodResolver(formSchema),
    mode: "onBlur",
    criteriaMode: "all",
    defaultValues: {
      name: project.name,
      description: project.description ?? undefined,
    },
  })

  const mutation = useMutation({
    mutationFn: (data: FormData) =>
      ProjectsService.updateProject({ id: project.id, requestBody: data }),
    onSuccess: () => {
      showSuccessToast("Project updated successfully")
      setIsOpen(false)
      onSuccess()
    },
    onError: handleError.bind(showErrorToast),
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["projects"] })
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
        Edit Project
      </DropdownMenuItem>
      <DialogContent className="sm:max-w-md">
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)}>
            <DialogHeader>
              <DialogTitle>Edit Project</DialogTitle>
              <DialogDescription>
                Update the project details below.
              </DialogDescription>
            </DialogHeader>
            <div className="grid gap-4 py-4">
              <FormField
                control={form.control}
                name="name"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>
                      Name <span className="text-destructive">*</span>
                    </FormLabel>
                    <FormControl>
                      <Input placeholder="Name" type="text" {...field} />
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

export default EditProject
