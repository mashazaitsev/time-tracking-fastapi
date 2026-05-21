/**
 * @module Projects/ProjectActionsMenu
 *
 * Purpose: Dropdown actions menu for project row operations (edit, delete).
 *
 * Relationships:
 *     Consumes: EditProject, DeleteProject components
 *     Used by: Projects table columns
 */

import { EllipsisVertical } from "lucide-react"
import { useState } from "react"

import type { ProjectPublic } from "@/client"
import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import DeleteProject from "./DeleteProject"
import EditProject from "./EditProject"

interface ProjectActionsMenuProps {
  project: ProjectPublic
}

/**
 * Purpose: Dropdown menu with edit/delete actions for a project table row.
 *
 * Structure:
 *     project (ProjectPublic): input - Target project for actions
 *
 * Relationships:
 *     Consumes: EditProject, DeleteProject components
 *     Used by: Projects table actions column
 */
export const ProjectActionsMenu = ({ project }: ProjectActionsMenuProps) => {
  const [open, setOpen] = useState(false)

  return (
    <DropdownMenu open={open} onOpenChange={setOpen}>
      <DropdownMenuTrigger asChild>
        <Button variant="ghost" size="icon">
          <EllipsisVertical />
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        <EditProject project={project} onSuccess={() => setOpen(false)} />
        <DeleteProject id={project.id} onSuccess={() => setOpen(false)} />
      </DropdownMenuContent>
    </DropdownMenu>
  )
}
