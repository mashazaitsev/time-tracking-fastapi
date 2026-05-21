/**
 * @file Authentication hook — login, signup, logout, and current user state.
 * @module hooks/useAuth
 */

/**
 * Purpose: Provide authentication hook for login, signup, logout, and current user state
 *
 * Structure:
 *     useAuth (hook): output - Returns { signUpMutation, loginMutation, logout, user }
 *     isLoggedIn (func): output - Check if access_token exists in localStorage
 *
 * Relationships:
 *     Consumes: client/LoginService, client/UsersService
 *     Produces: Auth state and mutations (consumed by routes and components)
 *
 * Semantics:
 *     Domain: authentication
 *     Logic: [Token stored in localStorage, login redirects to /, signup redirects to /login,
 *             logout clears token and redirects to /login]
 */

import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query"
import { useNavigate } from "@tanstack/react-router"

import {
  type Body_login_login_access_token as AccessToken,
  LoginService,
  type UserPublic,
  type UserRegister,
  UsersService,
} from "@/client"
import { handleError } from "@/utils"
import useCustomToast from "./useCustomToast"

/** Check if user is authenticated by verifying access_token in localStorage. */
const isLoggedIn = () => {
  return localStorage.getItem("access_token") !== null
}

/**
 * Purpose: Provide authentication state and actions (login, logout, signup)
 *
 * Structure:
 *     user (UserPublic | null): output - Current authenticated user
 *     loginMutation (UseMutationResult): output - Login mutation
 *     signUpMutation (UseMutationResult): output - Signup mutation
 *     logout (function): output - Clear token and redirect to /login
 *
 * Relationships:
 *     Consumes: LoginService, UsersService, localStorage token
 *     Produces: Auth state, user data, login/logout/signup actions
 */
const useAuth = () => {
  const navigate = useNavigate()
  const queryClient = useQueryClient()
  const { showErrorToast } = useCustomToast()

  const { data: user } = useQuery<UserPublic | null, Error>({
    queryKey: ["currentUser"],
    queryFn: UsersService.readUserMe,
    enabled: isLoggedIn(),
  })

  const signUpMutation = useMutation({
    mutationFn: (data: UserRegister) =>
      UsersService.registerUser({ requestBody: data }),
    onSuccess: () => {
      navigate({ to: "/login" })
    },
    onError: handleError.bind(showErrorToast),
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["users"] })
    },
  })

  const login = async (data: AccessToken) => {
    const response = await LoginService.loginAccessToken({
      formData: data,
    })
    localStorage.setItem("access_token", response.access_token)
  }

  const loginMutation = useMutation({
    mutationFn: login,
    onSuccess: () => {
      navigate({ to: "/" })
    },
    onError: handleError.bind(showErrorToast),
  })

  const logout = () => {
    localStorage.removeItem("access_token")
    navigate({ to: "/login" })
  }

  return {
    signUpMutation,
    loginMutation,
    logout,
    user,
  }
}

export { isLoggedIn }
export default useAuth
