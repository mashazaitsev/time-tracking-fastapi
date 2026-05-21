/**
 * @module Sidebar/Main
 *
 * Purpose: Primary navigation menu rendered inside the sidebar.
 *
 * Relationships:
 *     Consumes: TanStack Router for active route detection
 *     Used by: AppSidebar
 */

import { Link as RouterLink, useRouterState } from "@tanstack/react-router"
import type { LucideIcon } from "lucide-react"

import {
  SidebarGroup,
  SidebarGroupContent,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  useSidebar,
} from "@/components/ui/sidebar"

/**
 * Purpose: Navigation item descriptor for sidebar menu entries.
 *
 * Structure:
 *     icon (LucideIcon): Sidebar menu icon
 *     title (string): Display label
 *     path (string): Route path
 */
export type Item = {
  icon: LucideIcon
  title: string
  path: string
}

/**
 * Purpose: Props for Main sidebar navigation component.
 *
 * Structure:
 *     items (Item[]): input - Navigation items to render
 */
interface MainProps {
  items: Item[]
}

/**
 * Purpose: Renders sidebar navigation menu with active route highlighting.
 *
 * Structure:
 *     items (Item[]): input - Navigation items with icon, title, path
 *
 * Relationships:
 *     Consumes: TanStack Router (useRouterState), useSidebar context
 *     Used by: AppSidebar content area
 *
 * Flow:
 *     1. Determine current path from router state
 *     2. Render each item as SidebarMenuButton with active state
 *     3. Auto-close mobile sidebar on navigation
 */
export function Main({ items }: MainProps) {
  const { isMobile, setOpenMobile } = useSidebar()
  const router = useRouterState()
  const currentPath = router.location.pathname

  const handleMenuClick = () => {
    if (isMobile) {
      setOpenMobile(false)
    }
  }

  return (
    <SidebarGroup>
      <SidebarGroupContent>
        <SidebarMenu>
          {items.map((item) => {
            const isActive = currentPath === item.path

            return (
              <SidebarMenuItem key={item.title}>
                <SidebarMenuButton
                  tooltip={item.title}
                  isActive={isActive}
                  asChild
                >
                  <RouterLink to={item.path} onClick={handleMenuClick}>
                    <item.icon />
                    <span>{item.title}</span>
                  </RouterLink>
                </SidebarMenuButton>
              </SidebarMenuItem>
            )
          })}
        </SidebarMenu>
      </SidebarGroupContent>
    </SidebarGroup>
  )
}
