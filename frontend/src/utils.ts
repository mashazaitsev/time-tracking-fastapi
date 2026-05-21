/**
 * @file Shared utility functions for error handling and display formatting.
 * @module utils
 */

/**
 * Purpose: Provide shared utility functions for error handling and display formatting
 *
 * Structure:
 *     extractErrorMessage (func): output - Extract human-readable message from API errors
 *     handleError (func): output - Bind error extraction to toast display (use as .bind(showErrorToast))
 *     getInitials (func): output - Extract uppercase initials from name string
 *
 * Relationships:
 *     Consumes: client/ApiError
 *     Produces: Error messages (consumed by mutation onError handlers)
 */

import { AxiosError } from "axios"
import type { ApiError } from "./client"

/** Extract human-readable error message from ApiError or AxiosError. */
function extractErrorMessage(err: ApiError): string {
  if (err instanceof AxiosError) {
    return err.message
  }

  const errDetail = (err.body as any)?.detail
  if (Array.isArray(errDetail) && errDetail.length > 0) {
    return errDetail[0].msg
  }
  return errDetail || "Something went wrong."
}

/** Extract error message and pass to bound toast function. Usage: handleError.bind(showErrorToast) */
export const handleError = function (
  this: (msg: string) => void,
  err: ApiError,
) {
  const errorMessage = extractErrorMessage(err)
  this(errorMessage)
}

/** Extract up to 2 uppercase initials from a name string (e.g., "John Doe" → "JD"). */
export const getInitials = (name: string): string => {
  return name
    .split(" ")
    .slice(0, 2)
    .map((word) => word[0])
    .join("")
    .toUpperCase()
}
