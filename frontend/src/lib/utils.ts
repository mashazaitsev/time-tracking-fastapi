/**
 * @file Tailwind CSS utility — className merger with clsx + tailwind-merge.
 * @module lib/utils
 */

import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

/**
 * Purpose: Merge CSS class names with Tailwind conflict resolution
 *
 * Structure:
 *     inputs (ClassValue[]): input - Class names, conditionals, arrays
 *
 * Relationships:
 *     Consumes: clsx (conditional classes), tailwind-merge (conflict resolution)
 *     Produces: Merged className string (used by all UI components)
 */
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
