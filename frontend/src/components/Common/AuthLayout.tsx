/**
 * @module Common/AuthLayout
 *
 * Purpose: Two-column layout wrapper for authentication pages (login, signup, reset).
 *
 * Relationships:
 *     Consumes: Appearance, Logo, Footer components
 *     Used by: Login, Signup, ResetPassword routes
 */

import { Appearance } from "@/components/Common/Appearance"
import { Logo } from "@/components/Common/Logo"
import { Footer } from "./Footer"

/**
 * Purpose: Props for AuthLayout component.
 *
 * Structure:
 *     children (ReactNode): input - Auth form content to render
 */
interface AuthLayoutProps {
  children: React.ReactNode
}

/**
 * Purpose: Split-screen layout with logo panel (left) and auth form (right).
 *
 * Structure:
 *     children (ReactNode): input - Auth form content
 *
 * Relationships:
 *     Consumes: Logo, Appearance, Footer components
 *     Used by: Authentication route pages
 */
export function AuthLayout({ children }: AuthLayoutProps) {
  return (
    <div className="grid min-h-svh lg:grid-cols-2">
      <div className="bg-muted dark:bg-zinc-900 relative hidden lg:flex lg:items-center lg:justify-center">
        <Logo variant="full" className="h-16" asLink={false} />
      </div>
      <div className="flex flex-col gap-4 p-6 md:p-10">
        <div className="flex justify-end">
          <Appearance />
        </div>
        <div className="flex flex-1 items-center justify-center">
          <div className="w-full max-w-xs">{children}</div>
        </div>
        <Footer />
      </div>
    </div>
  )
}
