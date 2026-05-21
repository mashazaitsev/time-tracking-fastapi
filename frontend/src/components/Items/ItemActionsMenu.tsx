/**
 * @module Items/ItemActionsMenu
 *
 * Purpose: Dropdown actions menu for item row operations (edit, delete).
 *
 * Relationships:
 *     Consumes: EditItem, DeleteItem components
 *     Used by: Items table columns
 */

import { EllipsisVertical } from "lucide-react"
import { useState } from "react"

import type { ItemPublic } from "@/client"
import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import DeleteItem from "../Items/DeleteItem"
import EditItem from "../Items/EditItem"

/**
 * Purpose: Props for ItemActionsMenu component.
 *
 * Structure:
 *     item (ItemPublic): input - Item data for the row actions
 */
interface ItemActionsMenuProps {
  item: ItemPublic
}

/**
 * Purpose: Dropdown menu with edit/delete actions for an item table row.
 *
 * Structure:
 *     item (ItemPublic): input - Target item for actions
 *
 * Relationships:
 *     Consumes: EditItem, DeleteItem components
 *     Used by: Items table actions column
 */
export const ItemActionsMenu = ({ item }: ItemActionsMenuProps) => {
  const [open, setOpen] = useState(false)

  return (
    <DropdownMenu open={open} onOpenChange={setOpen}>
      <DropdownMenuTrigger asChild>
        <Button variant="ghost" size="icon">
          <EllipsisVertical />
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        <EditItem item={item} onSuccess={() => setOpen(false)} />
        <DeleteItem id={item.id} onSuccess={() => setOpen(false)} />
      </DropdownMenuContent>
    </DropdownMenu>
  )
}
