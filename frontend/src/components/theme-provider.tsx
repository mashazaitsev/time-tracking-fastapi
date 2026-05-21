/**
 * @module theme-provider
 *
 * Purpose: React context provider for application theme management (dark/light/system).
 *
 * Relationships:
 *     Consumed by: Appearance, SidebarAppearance, Logo components via useTheme hook
 *     Used by: App root component
 */

import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useState,
} from "react"

/** Purpose: Available theme modes. */
export type Theme = "dark" | "light" | "system"

/**
 * Purpose: Props for ThemeProvider component.
 *
 * Structure:
 *     children (ReactNode): input - App content to wrap
 *     defaultTheme (Theme): input - Initial theme, defaults to "system"
 *     storageKey (string): input - localStorage key for persistence
 */
type ThemeProviderProps = {
  children: React.ReactNode
  defaultTheme?: Theme
  storageKey?: string
}

/**
 * Purpose: Context state shape for theme provider.
 *
 * Structure:
 *     theme (Theme): Current theme setting (may be "system")
 *     resolvedTheme ("dark"|"light"): Actual resolved theme after system detection
 *     setTheme (function): Theme setter with localStorage persistence
 */
type ThemeProviderState = {
  theme: Theme
  resolvedTheme: "dark" | "light"
  setTheme: (theme: Theme) => void
}

const initialState: ThemeProviderState = {
  theme: "system",
  resolvedTheme: "light",
  setTheme: () => null,
}

const ThemeProviderContext = createContext<ThemeProviderState>(initialState)

/**
 * Purpose: Context provider managing theme state, localStorage persistence, and system preference detection.
 *
 * Structure:
 *     defaultTheme (Theme): input - Fallback theme, defaults to "system"
 *     storageKey (string): input - localStorage key, defaults to "vite-ui-theme"
 *
 * Relationships:
 *     Produces: ThemeProviderContext consumed by useTheme hook
 *     Used by: App root
 *
 * Flow:
 *     1. Read persisted theme from localStorage (or use default)
 *     2. Apply theme class to document root element
 *     3. Listen for system color-scheme changes when theme is "system"
 *     4. Expose theme, resolvedTheme, and setTheme via context
 */
export function ThemeProvider({
  children,
  defaultTheme = "system",
  storageKey = "vite-ui-theme",
  ...props
}: ThemeProviderProps) {
  const [theme, setTheme] = useState<Theme>(
    () => (localStorage.getItem(storageKey) as Theme) || defaultTheme,
  )

  const getResolvedTheme = useCallback((theme: Theme): "dark" | "light" => {
    if (theme === "system") {
      return window.matchMedia("(prefers-color-scheme: dark)").matches
        ? "dark"
        : "light"
    }
    return theme
  }, [])

  const [resolvedTheme, setResolvedTheme] = useState<"dark" | "light">(() =>
    getResolvedTheme(theme),
  )

  const updateTheme = useCallback((newTheme: Theme) => {
    const root = window.document.documentElement

    root.classList.remove("light", "dark")

    if (newTheme === "system") {
      const systemTheme = window.matchMedia("(prefers-color-scheme: dark)")
        .matches
        ? "dark"
        : "light"

      root.classList.add(systemTheme)
      return
    }

    root.classList.add(newTheme)
  }, [])

  useEffect(() => {
    updateTheme(theme)
    setResolvedTheme(getResolvedTheme(theme))

    const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)")

    const handleChange = () => {
      if (theme === "system") {
        updateTheme("system")
        setResolvedTheme(getResolvedTheme("system"))
      }
    }

    mediaQuery.addEventListener("change", handleChange)

    return () => {
      mediaQuery.removeEventListener("change", handleChange)
    }
  }, [theme, updateTheme, getResolvedTheme])

  const value = {
    theme,
    resolvedTheme,
    setTheme: (theme: Theme) => {
      localStorage.setItem(storageKey, theme)
      setTheme(theme)
    },
  }

  return (
    <ThemeProviderContext.Provider {...props} value={value}>
      {children}
    </ThemeProviderContext.Provider>
  )
}

/**
 * Purpose: Hook to access theme context (theme, resolvedTheme, setTheme).
 *
 * Relationships:
 *     Consumes: ThemeProviderContext
 *
 * @throws Error if used outside ThemeProvider
 */
export const useTheme = () => {
  const context = useContext(ThemeProviderContext)

  if (context === undefined)
    throw new Error("useTheme must be used within a ThemeProvider")

  return context
}
