/**
 * @file Toast notification hook — success and error toast helpers.
 * @module hooks/useCustomToast
 */

import { toast } from "sonner"

/**
 * Purpose: Provide convenience wrappers for success and error toast notifications
 *
 * Structure:
 *     showSuccessToast (function): output - Display success toast with description
 *     showErrorToast (function): output - Display error toast with description
 *
 * Relationships:
 *     Consumes: sonner toast API
 *     Produces: Toast notifications (used by mutations and form handlers)
 */
const useCustomToast = () => {
  const showSuccessToast = (description: string) => {
    toast.success("Success!", {
      description,
    })
  }

  const showErrorToast = (description: string) => {
    toast.error("Something went wrong!", {
      description,
    })
  }

  return { showSuccessToast, showErrorToast }
}

export default useCustomToast
