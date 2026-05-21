/**
 * @module Common/ErrorComponent
 *
 * Purpose: Generic error page displayed when an unhandled error occurs.
 *
 * Relationships:
 *     Used by: Router error boundary
 */

import { Link } from "@tanstack/react-router"
import { Button } from "@/components/ui/button"

/**
 * Purpose: Full-screen error page with "Go Home" navigation link.
 *
 * Relationships:
 *     Produces: Navigation to root route via Link
 */
const ErrorComponent = () => {
  return (
    <div
      className="flex min-h-screen items-center justify-center flex-col p-4"
      data-testid="error-component"
    >
      <div className="flex items-center z-10">
        <div className="flex flex-col ml-4 items-center justify-center p-4">
          <span className="text-6xl md:text-8xl font-bold leading-none mb-4">
            Error
          </span>
          <span className="text-2xl font-bold mb-2">Oops!</span>
        </div>
      </div>

      <p className="text-lg text-muted-foreground mb-4 text-center z-10">
        Something went wrong. Please try again.
      </p>
      <Link to="/">
        <Button>Go Home</Button>
      </Link>
    </div>
  )
}

export default ErrorComponent
