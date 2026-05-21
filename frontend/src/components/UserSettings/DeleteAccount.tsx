/**
 * @module UserSettings/DeleteAccount
 *
 * Purpose: Danger zone section for account self-deletion.
 *
 * Relationships:
 *     Consumes: DeleteConfirmation component
 *     Used by: User settings page
 */

import DeleteConfirmation from "./DeleteConfirmation"

/**
 * Purpose: Destructive-styled card with account deletion warning and confirmation trigger.
 *
 * Relationships:
 *     Consumes: DeleteConfirmation dialog component
 *     Used by: User settings page
 */
const DeleteAccount = () => {
  return (
    <div className="max-w-md mt-4 rounded-lg border border-destructive/50 p-4">
      <h3 className="font-semibold text-destructive">Delete Account</h3>
      <p className="mt-1 text-sm text-muted-foreground">
        Permanently delete your account and all associated data.
      </p>
      <DeleteConfirmation />
    </div>
  )
}

export default DeleteAccount
