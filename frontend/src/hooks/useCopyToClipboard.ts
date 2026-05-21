/**
 * @file Clipboard hook — copy text to clipboard with state tracking.
 * @module hooks/useCopyToClipboard
 */

// source: https://usehooks-ts.com/react-hook/use-copy-to-clipboard
import { useCallback, useState } from "react"

/** Last successfully copied text, or null. */
type CopiedValue = string | null

/** Async function that copies text and returns success boolean. */
type CopyFn = (text: string) => Promise<boolean>

/**
 * Purpose: Copy text to clipboard and track copied state
 *
 * Structure:
 *     copiedText (string | null): output - Last copied text (resets after 2s)
 *     copy (function): output - Async copy function returning success boolean
 *
 * Relationships:
 *     Consumes: navigator.clipboard API
 *     Produces: Clipboard write + copied state
 */
export function useCopyToClipboard(): [CopiedValue, CopyFn] {
  const [copiedText, setCopiedText] = useState<CopiedValue>(null)

  const copy: CopyFn = useCallback(async (text) => {
    if (!navigator?.clipboard) {
      console.warn("Clipboard not supported")
      return false
    }

    try {
      await navigator.clipboard.writeText(text)
      setCopiedText(text)

      setTimeout(() => setCopiedText(null), 2000)

      return true
    } catch (error) {
      console.warn("Copy failed", error)
      setCopiedText(null)
      return false
    }
  }, [])

  return [copiedText, copy]
}
