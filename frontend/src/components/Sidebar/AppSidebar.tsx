/**
 * @module Sidebar/AppSidebar
 *
 * Purpose: Main application sidebar with navigation, theme toggle, and user menu.
 *
 * Relationships:
 *     Consumes: Main, User, SidebarAppearance, Logo components; useAuth hook
 *     Used by: Authenticated layout shell
 */

import { Briefcase, Clock, FolderOpen, Home, Users } from "lucide-react"

import { SidebarAppearance } from "@/components/Common/Appearance"
import { Logo } from "@/components/Common/Logo"
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
} from "@/components/ui/sidebar"
import useAuth from "@/hooks/useAuth"
import { type Item, Main } from "./Main"
import { User } from "./User"

const baseItems: Item[] = [
  { icon: Home, title: "Dashboard", path: "/" },
  { icon: Briefcase, title: "Items", path: "/items" },
  { icon: FolderOpen, title: "Projects", path: "/projects" },
  { icon: Clock, title: "Time Entries", path: "/time-entries" },
]

/**
 * Purpose: Collapsible sidebar with navigation items, appearance toggle, and user menu.
 *
 * Structure:
 *     baseItems: Dashboard and Items nav links
 *     Admin link: Conditionally added for superusers
 *
 * Relationships:
 *     Consumes: useAuth (current user/superuser check), Main, User, SidebarAppearance, Logo
 *     Used by: Authenticated app layout
 *
 * Flow:
 *     1. Determine nav items based on superuser status
 *     2. Render Logo in header, Main nav in content, Appearance + User in footer
 */
export function AppSidebar() {
  const { user: currentUser } = useAuth()

  const items = currentUser?.is_superuser
    ? [...baseItems, { icon: Users, title: "Admin", path: "/admin" }]
    : baseItems

  return (
    <Sidebar collapsible="icon">
      <SidebarHeader className="px-4 py-6 group-data-[collapsible=icon]:px-0 group-data-[collapsible=icon]:items-center">
        <Logo variant="responsive" />
      </SidebarHeader>
      <SidebarContent>
        <Main items={items} />
      </SidebarContent>
      <SidebarFooter>
        <SidebarAppearance />
        <User user={currentUser} />
      </SidebarFooter>
    </Sidebar>
  )
}

export default AppSidebar
