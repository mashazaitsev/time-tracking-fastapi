/**
 * @module Items/columns
 *
 * Purpose: Column definitions for the items data table.
 *
 * Relationships:
 *     Consumes: ItemActionsMenu component, ItemPublic type
 *     Used by: Items page DataTable
 */

import type { ColumnDef } from "@tanstack/react-table"
import { Check, Copy } from "lucide-react"

import type { ItemPublic } from "@/client"
import { Button } from "@/components/ui/button"
import { useCopyToClipboard } from "@/hooks/useCopyToClipboard"
import { cn } from "@/lib/utils"
import { ItemActionsMenu } from "./ItemActionsMenu"

/**
 * Purpose: Inline component displaying an item ID with copy-to-clipboard button.
 *
 * Structure:
 *     id (string): input - Item ID to display and copy
 *
 * Relationships:
 *     Consumes: useCopyToClipboard hook
 */
function CopyId({ id }: { id: string }) {
  const [copiedText, copy] = useCopyToClipboard()
  const isCopied = copiedText === id

  return (
    <div className="flex items-center gap-1.5 group">
      <span className="font-mono text-xs text-muted-foreground">{id}</span>
      <Button
        variant="ghost"
        size="icon"
        className="size-6 opacity-0 group-hover:opacity-100 transition-opacity"
        onClick={() => copy(id)}
      >
        {isCopied ? (
          <Check className="size-3 text-green-500" />
        ) : (
          <Copy className="size-3" />
        )}
        <span className="sr-only">Copy ID</span>
      </Button>
    </div>
  )
}

/**
 * Purpose: TanStack Table column definitions for the items table.
 *
 * Structure:
 *     id: Copyable item ID (mono font)
 *     title: Item title
 *     description: Truncated description with fallback text
 *     actions: ItemActionsMenu dropdown
 *
 * Relationships:
 *     Consumes: CopyId helper, ItemActionsMenu component
 *     Used by: Items page DataTable
 */
export const columns: ColumnDef<ItemPublic>[] = [
  {
    accessorKey: "id",
    header: "ID",
    cell: ({ row }) => <CopyId id={row.original.id} />,
  },
  {
    accessorKey: "title",
    header: "Title",
    cell: ({ row }) => (
      <span className="font-medium">{row.original.title}</span>
    ),
  },
  {
    accessorKey: "description",
    header: "Description",
    cell: ({ row }) => {
      const description = row.original.description
      return (
        <span
          className={cn(
            "max-w-xs truncate block text-muted-foreground",
            !description && "italic",
          )}
        >
          {description || "No description"}
        </span>
      )
    },
  },
  {
    id: "actions",
    header: () => <span className="sr-only">Actions</span>,
    cell: ({ row }) => (
      <div className="flex justify-end">
        <ItemActionsMenu item={row.original} />
      </div>
    ),
  },
]
