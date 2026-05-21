/**
 * @module Common/Logo
 *
 * Purpose: Theme-aware FastAPI logo component with full, icon, and responsive variants.
 *
 * Relationships:
 *     Consumes: ThemeProvider context (useTheme)
 *     Used by: AuthLayout, AppSidebar
 */

import { Link } from "@tanstack/react-router"

import { useTheme } from "@/components/theme-provider"
import { cn } from "@/lib/utils"
import icon from "/assets/images/fastapi-icon.svg"
import iconLight from "/assets/images/fastapi-icon-light.svg"
import logo from "/assets/images/fastapi-logo.svg"
import logoLight from "/assets/images/fastapi-logo-light.svg"

/**
 * Purpose: Props for Logo component.
 *
 * Structure:
 *     variant ("full"|"icon"|"responsive"): input - Logo display mode
 *     className (string): input - Additional CSS classes
 *     asLink (boolean): input - Whether to wrap logo in a home link
 */
interface LogoProps {
  variant?: "full" | "icon" | "responsive"
  className?: string
  asLink?: boolean
}

/**
 * Purpose: Renders theme-aware FastAPI logo in full, icon, or responsive (collapsible) mode.
 *
 * Structure:
 *     variant ("full"|"icon"|"responsive"): input - Display mode, defaults to "full"
 *     asLink (boolean): input - Wraps in Link to "/" when true (default)
 *
 * Relationships:
 *     Consumes: useTheme for dark/light logo selection
 *     Used by: AuthLayout (full), AppSidebar (responsive)
 */
export function Logo({
  variant = "full",
  className,
  asLink = true,
}: LogoProps) {
  const { resolvedTheme } = useTheme()
  const isDark = resolvedTheme === "dark"

  const fullLogo = isDark ? logoLight : logo
  const iconLogo = isDark ? iconLight : icon

  const content =
    variant === "responsive" ? (
      <>
        <img
          src={fullLogo}
          alt="FastAPI"
          className={cn(
            "h-6 w-auto group-data-[collapsible=icon]:hidden",
            className,
          )}
        />
        <img
          src={iconLogo}
          alt="FastAPI"
          className={cn(
            "size-5 hidden group-data-[collapsible=icon]:block",
            className,
          )}
        />
      </>
    ) : (
      <img
        src={variant === "full" ? fullLogo : iconLogo}
        alt="FastAPI"
        className={cn(variant === "full" ? "h-6 w-auto" : "size-5", className)}
      />
    )

  if (!asLink) {
    return content
  }

  return <Link to="/">{content}</Link>
}
