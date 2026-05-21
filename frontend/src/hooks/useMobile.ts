/**
 * @file Mobile detection hook — responsive breakpoint observer.
 * @module hooks/useMobile
 */

import * as React from "react"

/** Breakpoint threshold in pixels for mobile detection. */
const MOBILE_BREAKPOINT = 768

/**
 * Purpose: Detect if viewport is below mobile breakpoint (768px)
 *
 * Structure:
 *     isMobile (boolean): output - True if window width < 768px
 *
 * Relationships:
 *     Consumes: window.matchMedia API
 *     Produces: Reactive mobile state (used by layout/sidebar components)
 */
export function useIsMobile() {
  const [isMobile, setIsMobile] = React.useState<boolean | undefined>(undefined)

  React.useEffect(() => {
    const mql = window.matchMedia(`(max-width: ${MOBILE_BREAKPOINT - 1}px)`)
    const onChange = () => {
      setIsMobile(window.innerWidth < MOBILE_BREAKPOINT)
    }
    mql.addEventListener("change", onChange)
    setIsMobile(window.innerWidth < MOBILE_BREAKPOINT)
    return () => mql.removeEventListener("change", onChange)
  }, [])

  return !!isMobile
}
