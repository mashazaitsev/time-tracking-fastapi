/**
 * @file Projects route — CRUD listing page for user projects.
 * @module routes/_layout/projects
 *
 * Purpose: Display paginated projects table with add, edit, and delete actions.
 *
 * Relationships:
 *     Consumes: ProjectsService.readProjects, Projects/AddProject, Projects/columns
 *     Produces: Projects data table with empty state and add-project button
 */

import { useSuspenseQuery } from "@tanstack/react-query"
import { createFileRoute } from "@tanstack/react-router"
import { Search } from "lucide-react"
import { Suspense } from "react"

import { ProjectsService } from "@/client"
import { DataTable } from "@/components/Common/DataTable"
import AddProject from "@/components/Projects/AddProject"
import { columns } from "@/components/Projects/columns"
import PendingProjects from "@/components/Projects/PendingProjects"

/** TanStack Query options for fetching all projects (up to 100). */
function getProjectsQueryOptions() {
  return {
    queryFn: () => ProjectsService.readProjects({ skip: 0, limit: 100 }),
    queryKey: ["projects"],
  }
}

/**
 * Route config for /_layout/projects.
 */
export const Route = createFileRoute("/_layout/projects")({
  component: Projects,
  head: () => ({
    meta: [
      {
        title: "Projects - FastAPI Template",
      },
    ],
  }),
})

/** Fetches projects via suspense query; shows empty state or DataTable. */
function ProjectsTableContent() {
  const { data: projects } = useSuspenseQuery(getProjectsQueryOptions())

  if (!projects?.data || projects.data.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center text-center py-12">
        <div className="rounded-full bg-muted p-4 mb-4">
          <Search className="h-8 w-8 text-muted-foreground" />
        </div>
        <h3 className="text-lg font-semibold">No projects</h3>
        <p className="text-muted-foreground">
          Add a new project to get started
        </p>
      </div>
    )
  }

  return <DataTable columns={columns} data={projects.data} />
}

/** Suspense wrapper for ProjectsTableContent with PendingProjects fallback. */
function ProjectsTable() {
  return (
    <Suspense fallback={<PendingProjects />}>
      <ProjectsTableContent />
    </Suspense>
  )
}

/**
 * Purpose: Projects listing page with data table and add-project action.
 *
 * Structure:
 *     projects (ProjectPublic[]): input - All projects fetched via ProjectsService
 *
 * Relationships:
 *     Consumes: ProjectsService.readProjects, Projects/AddProject, Projects/columns
 *     Produces: Projects data table with empty state and add-project button
 */
function Projects() {
  return (
    <div className="flex flex-col gap-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight">Projects</h1>
          <p className="text-muted-foreground">
            Create and manage your projects
          </p>
        </div>
        <AddProject />
      </div>
      <ProjectsTable />
    </div>
  )
}
