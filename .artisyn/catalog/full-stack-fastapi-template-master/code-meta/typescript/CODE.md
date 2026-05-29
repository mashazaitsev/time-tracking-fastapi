# Typescript Documentation (104 files)


## frontend

**frontend/openapi-ts.config.ts**

- **Imports:** @hey-api/openapi-ts
**frontend/playwright.config.ts**

- **Imports:** @playwright/test, dotenv/config
**frontend/vite.config.ts**

- **Imports:** @tailwindcss/vite, @tanstack/router-plugin/vite, @vitejs/plugin-react-swc, node:path, vite

## frontend/src

**frontend/src/main.tsx** — Application entry point — initializes React with router, query client, theme, and API auth.

- **Relationships:** Consumes: client/OpenAPI, routeTree.gen, theme-provider, sonner
Produces: Rendered React app in #root DOM element

### (error: Error) => {
  if (error instanceof ApiError && [401, 403].includes(error.status)) {
    localStorage.removeItem("access_token")
    window.location.href = "/login"
  }
} [line 45] — Clear token and redirect to /login on 401/403 API errors.
- **Imports:** ./client, ./components/theme-provider, ./components/ui/sonner, ./index.css, ./routeTree.gen, @tanstack/react-query, @tanstack/react-router, react, react-dom/client
**frontend/src/routeTree.gen.ts**

- **Imports:** 12 external dependencies
**frontend/src/utils.ts** — Shared utility functions for error handling and display formatting.

- **Relationships:** Consumes: client/ApiError
Produces: Error messages (consumed by mutation onError handlers)

### function extractErrorMessage(err: ApiError): string { [line 23] — Extract human-readable error message from ApiError or AxiosError.

### (name: string): string => {
  return name
    .split(" ")
    .slice(0, 2)
    .map((word) => word[0])
    .join("")
    .toUpperCase()
} [line 45] — Extract up to 2 uppercase initials from a name string (e.g., "John Doe" → "JD").
- **Imports:** ./client, axios
**frontend/src/vite-env.d.ts**


## frontend/src/client

**frontend/src/client/index.ts**

**frontend/src/client/schemas.gen.ts**

**frontend/src/client/sdk.gen.ts**


### ItemsService [class, line 8]
- **Methods:**
  - `readItems(d, a, t, a, ., l, i, m, i, t)` [line 34] — Retrieve paginated list of items for current user
  - `createItem(d, a, t, a, ., r, e, q, u, e, s, t, B, o, d, y)` [line 71] — Create a new item owned by the current user
  - `readItem(d, a, t, a, ., i, d)` [line 106] — Retrieve a single item by ID with ownership check
  - `updateItem(d, a, t, a, ., r, e, q, u, e, s, t, B, o, d, y)` [line 144] — Update an existing item with ownership check
  - `deleteItem(d, a, t, a, ., i, d)` [line 182] — Delete an item with ownership check

### LoginService [class, line 196]
- **Methods:**
  - `loginAccessToken(d, a, t, a, ., f, o, r, m, D, a, t, a)` [line 219] — Authenticate user via email/password and return JWT access token
  - `testToken()` [line 245] — Validate access token and return current user profile
  - `recoverPassword(d, a, t, a, ., e, m, a, i, l)` [line 274] — Send password recovery email if user exists
  - `resetPassword(d, a, t, a, ., r, e, q, u, e, s, t, B, o, d, y)` [line 309] — Reset user password using a recovery token
  - `recoverPasswordHtmlContent(d, a, t, a, ., e, m, a, i, l)` [line 343] — Preview password recovery email HTML content (superuser only)

### PrivateService [class, line 357]
- **Methods:**
  - `createUser(d, a, t, a, ., r, e, q, u, e, s, t, B, o, d, y)` [line 380] — Create user directly without email uniqueness check (local dev only)

### ProjectsService [class, line 393]
- **Methods:**
  - `readProjects(d, a, t, a, ., l, i, m, i, t)` [line 415] — Retrieve paginated list of projects for current user
  - `createProject(d, a, t, a, ., r, e, q, u, e, s, t, B, o, d, y)` [line 448] — Create a new project owned by the current user
  - `readProject(d, a, t, a, ., i, d)` [line 479] — Retrieve a single project by ID with ownership check
  - `updateProject(d, a, t, a, ., r, e, q, u, e, s, t, B, o, d, y)` [line 513] — Update an existing project with ownership check
  - `deleteProject(d, a, t, a, ., i, d)` [line 547] — Delete a project with ownership check

### TimeEntriesService [class, line 561]
- **Methods:**
  - `getSummary()` [line 586] — Aggregate total minutes and per-project breakdown for the current user
  - `readTimeEntries(d, a, t, a, ., l, i, m, i, t)` [line 618] — Retrieve paginated list of time entries for current user
  - `createTimeEntry(d, a, t, a, ., r, e, q, u, e, s, t, B, o, d, y)` [line 656] — Create a new time entry owned by the current user after validating project ownership
  - `readTimeEntry(d, a, t, a, ., i, d)` [line 691] — Retrieve a single time entry by ID with ownership check
  - `updateTimeEntry(d, a, t, a, ., r, e, q, u, e, s, t, B, o, d, y)` [line 729] — Partially update an existing time entry with ownership check
  - `deleteTimeEntry(d, a, t, a, ., i, d)` [line 767] — Delete a time entry with ownership check

### UsersService [class, line 781]
- **Methods:**
  - `readUsers(d, a, t, a, ., l, i, m, i, t)` [line 801] — Retrieve paginated list of all users (superuser only)
  - `createUser(d, a, t, a, ., r, e, q, u, e, s, t, B, o, d, y)` [line 837] — Create a new user (superuser only), send welcome email if SMTP configured
  - `readUserMe()` [line 863] — Get current authenticated user profile
  - `deleteUserMe()` [line 885] — Delete own account (superusers cannot delete themselves)
  - `updateUserMe(d, a, t, a, ., r, e, q, u, e, s, t, B, o, d, y)` [line 915] — Update own profile (name and email)
  - `updatePasswordMe(d, a, t, a, ., r, e, q, u, e, s, t, B, o, d, y)` [line 950] — Change own password with current password verification
  - `registerUser(d, a, t, a, ., r, e, q, u, e, s, t, B, o, d, y)` [line 984] — Public self-registration (no auth required)
  - `readUserById(d, a, t, a, ., u, s, e, r, I, d)` [line 1019] — Get user by ID (own profile or superuser only)
  - `updateUser(d, a, t, a, ., r, e, q, u, e, s, t, B, o, d, y)` [line 1056] — Update a user by ID (superuser only)
  - `deleteUser(d, a, t, a, ., u, s, e, r, I, d)` [line 1094] — Delete a user and their items (superuser only, cannot self-delete)

### UtilsService [class, line 1108]
- **Methods:**
  - `testEmail(d, a, t, a, ., e, m, a, i, l, T, o)` [line 1125] — Send test email to verify SMTP configuration (superuser only)
  - `healthCheck()` [line 1151] — Return true if application is running
- **Imports:** ./core/CancelablePromise, ./core/OpenAPI, ./core/request, ./types.gen
**frontend/src/client/types.gen.ts**


## frontend/src/client/core

**frontend/src/client/core/ApiError.ts**


### ApiError [class, line 4]
- **Methods:**
  - constructor: line 11
- **Imports:** ./ApiRequestOptions, ./ApiResult
**frontend/src/client/core/ApiRequestOptions.ts**

**frontend/src/client/core/ApiResult.ts**

**frontend/src/client/core/CancelablePromise.ts**


### CancelError [class, line 1]
- **Methods:**
  - constructor: line 2
  - isCancelled: line 7

### CancelablePromise [class, line 20]
- **Methods:**
  - constructor: line 29
  - then: line 87
  - catch: line 94
  - finally: line 100
  - cancel: line 104
  - isCancelled: line 123
**frontend/src/client/core/OpenAPI.ts**


### Interceptors [class, line 8]
- **Methods:**
  - constructor: line 11
  - eject: line 15
  - use: line 22
- **Imports:** ./ApiRequestOptions, axios
**frontend/src/client/core/request.ts**


### (value: unknown): value is string => {
	return typeof value === 'string';
} [line 11]

### (value: unknown): value is string => {
	return isString(value) && value !== '';
} [line 15]

### (value: any): value is Blob => {
	return value instanceof Blob;
} [line 19]

### (value: unknown): value is FormData => {
	return value instanceof FormData;
} [line 23]

### (status: number): boolean => {
	return status >= 200 && status < 300;
} [line 27]

### (str: string): string => {
	try {
		return btoa(str);
	} catch (err) {
		// @ts-ignore
		return Buffer.from(str).toString('base64');
	}
} [line 31]

### (params: Record<string, unknown>): string => {
	const qs: string[] = [];

	const append = (key: string, value: unknown) => {
		qs.push(`${encodeURIComponent(key)}=${encodeURIComponent(String(value))}`);
	};

	const encodePair = (key: string, value: unknown) => {
		if (value === undefined || value === null) {
			return;
		}

		if (value instanceof Date) {
			append(key, value.toISOString());
		} else if (Array.isArray(value)) {
			value.forEach(v => encodePair(key, v));
		} else if (typeof value === 'object') {
			Object.entries(value).forEach(([k, v]) => encodePair(`${key}[${k}]`, v));
		} else {
			append(key, value);
		}
	};

	Object.entries(params).forEach(([key, value]) => encodePair(key, value));

	return qs.length ? `?${qs.join('&')}` : '';
} [line 40]

### (config: OpenAPIConfig, options: ApiRequestOptions): string => {
	const encoder = config.ENCODE_PATH || encodeURI;

	const path = options.url
		.replace('{api-version}', config.VERSION)
		.replace(/{(.*?)}/g, (substring: string, group: string) => {
			if (options.path?.hasOwnProperty(group)) {
				return encoder(String(options.path[group]));
			}
			return substring;
		});

	const url = config.BASE + path;
	return options.query ? url + getQueryString(options.query) : url;
} [line 68]

### (options: ApiRequestOptions): FormData | undefined => {
	if (options.formData) {
		const formData = new FormData();

		const process = (key: string, value: unknown) => {
			if (isString(value) || isBlob(value)) {
				formData.append(key, value);
			} else {
				formData.append(key, JSON.stringify(value));
			}
		};

		Object.entries(options.formData)
			.filter(([, value]) => value !== undefined && value !== null)
			.forEach(([key, value]) => {
				if (Array.isArray(value)) {
					value.forEach(v => process(key, v));
				} else {
					process(key, value);
				}
			});

		return formData;
	}
	return undefined;
} [line 84]

### async <T>(options: ApiRequestOptions<T>, resolver?: T | Resolver<T>): Promise<T | undefined> => {
	if (typeof resolver === 'function') {
		return (resolver as Resolver<T>)(options);
	}
	return resolver;
} [line 113]

### async <T>(config: OpenAPIConfig, options: ApiRequestOptions<T>): Promise<Record<string, string>> => {
	const [token, username, password, additionalHeaders] = await Promise.all([
		// @ts-ignore
		resolve(options, config.TOKEN),
		// @ts-ignore
		resolve(options, config.USERNAME),
		// @ts-ignore
		resolve(options, config.PASSWORD),
		// @ts-ignore
		resolve(options, config.HEADERS),
	]);

	const headers = Object.entries({
		Accept: 'application/json',
		...additionalHeaders,
		...options.headers,
	})
	.filter(([, value]) => value !== undefined && value !== null)
	.reduce((headers, [key, value]) => ({
		...headers,
		[key]: String(value),
	}), {} as Record<string, string>);

	if (isStringWithValue(token)) {
		headers['Authorization'] = `Bearer ${token}`;
	}

	if (isStringWithValue(username) && isStringWithValue(password)) {
		const credentials = base64(`${username}:${password}`);
		headers['Authorization'] = `Basic ${credentials}`;
	}

	if (options.body !== undefined) {
		if (options.mediaType) {
			headers['Content-Type'] = options.mediaType;
		} else if (isBlob(options.body)) {
			headers['Content-Type'] = options.body.type || 'application/octet-stream';
		} else if (isString(options.body)) {
			headers['Content-Type'] = 'text/plain';
		} else if (!isFormData(options.body)) {
			headers['Content-Type'] = 'application/json';
		}
	} else if (options.formData !== undefined) {
		if (options.mediaType) {
			headers['Content-Type'] = options.mediaType;
		}
	}

	return headers;
} [line 120]

### (options: ApiRequestOptions): unknown => {
	if (options.body) {
		return options.body;
	}
	return undefined;
} [line 171]

### async <T>(
	config: OpenAPIConfig,
	options: ApiRequestOptions<T>,
	url: string,
	body: unknown,
	formData: FormData | undefined,
	headers: Record<string, string>,
	onCancel: OnCancel,
	axiosClient: AxiosInstance
): Promise<AxiosResponse<T>> => {
	const controller = new AbortController();

	let requestConfig: AxiosRequestConfig = {
		data: body ?? formData,
		headers,
		method: options.method,
		signal: controller.signal,
		url,
		withCredentials: config.WITH_CREDENTIALS,
	};

	onCancel(() => controller.abort());

	for (const fn of config.interceptors.request._fns) {
		requestConfig = await fn(requestConfig);
	}

	try {
		return await axiosClient.request(requestConfig);
	} catch (error) {
		const axiosError = error as AxiosError<T>;
		if (axiosError.response) {
			return axiosError.response;
		}
		throw error;
	}
} [line 178]

### (response: AxiosResponse<unknown>, responseHeader?: string): string | undefined => {
	if (responseHeader) {
		const content = response.headers[responseHeader];
		if (isString(content)) {
			return content;
		}
	}
	return undefined;
} [line 216]

### (response: AxiosResponse<unknown>): unknown => {
	if (response.status !== 204) {
		return response.data;
	}
	return undefined;
} [line 226]

### (options: ApiRequestOptions, result: ApiResult): void => {
	const errors: Record<number, string> = {
		400: 'Bad Request',
		401: 'Unauthorized',
		402: 'Payment Required',
		403: 'Forbidden',
		404: 'Not Found',
		405: 'Method Not Allowed',
		406: 'Not Acceptable',
		407: 'Proxy Authentication Required',
		408: 'Request Timeout',
		409: 'Conflict',
		410: 'Gone',
		411: 'Length Required',
		412: 'Precondition Failed',
		413: 'Payload Too Large',
		414: 'URI Too Long',
		415: 'Unsupported Media Type',
		416: 'Range Not Satisfiable',
		417: 'Expectation Failed',
		418: 'Im a teapot',
		421: 'Misdirected Request',
		422: 'Unprocessable Content',
		423: 'Locked',
		424: 'Failed Dependency',
		425: 'Too Early',
		426: 'Upgrade Required',
		428: 'Precondition Required',
		429: 'Too Many Requests',
		431: 'Request Header Fields Too Large',
		451: 'Unavailable For Legal Reasons',
		500: 'Internal Server Error',
		501: 'Not Implemented',
		502: 'Bad Gateway',
		503: 'Service Unavailable',
		504: 'Gateway Timeout',
		505: 'HTTP Version Not Supported',
		506: 'Variant Also Negotiates',
		507: 'Insufficient Storage',
		508: 'Loop Detected',
		510: 'Not Extended',
		511: 'Network Authentication Required',
		...options.errors,
	}

	const error = errors[result.status];
	if (error) {
		throw new ApiError(options, result, error);
	}

	if (!result.ok) {
		const errorStatus = result.status ?? 'unknown';
		const errorStatusText = result.statusText ?? 'unknown';
		const errorBody = (() => {
			try {
				return JSON.stringify(result.body, null, 2);
			} catch (e) {
				return undefined;
			}
		})();

		throw new ApiError(options, result,
			`Generic Error: status: ${errorStatus}; status text: ${errorStatusText}; body: ${errorBody}`
		);
	}
} [line 233]

### <T>(config: OpenAPIConfig, options: ApiRequestOptions<T>, axiosClient: AxiosInstance = axios): CancelablePromise<T> => {
	return new CancelablePromise(async (resolve, reject, onCancel) => {
		try {
			const url = getUrl(config, options);
			const formData = getFormData(options);
			const body = getRequestBody(options);
			const headers = await getHeaders(config, options);

			if (!onCancel.isCancelled) {
				let response = await sendRequest<T>(config, options, url, body, formData, headers, onCancel, axiosClient);

				for (const fn of config.interceptors.response._fns) {
					response = await fn(response);
				}

				const responseBody = getResponseBody(response);
				const responseHeader = getResponseHeader(response, options.responseHeader);

				let transformedBody = responseBody;
				if (options.responseTransformer && isSuccess(response.status)) {
					transformedBody = await options.responseTransformer(responseBody)
				}

				const result: ApiResult = {
					url,
					ok: isSuccess(response.status),
					status: response.status,
					statusText: response.statusText,
					body: responseHeader ?? transformedBody,
				};

				catchErrorCodes(options, result);

				resolve(result.body);
			}
		} catch (error) {
			reject(error);
		}
	});
} [line 308] — Request method
- **Imports:** ./ApiError, ./ApiRequestOptions, ./ApiResult, ./CancelablePromise, ./OpenAPI, axios

## frontend/src/components

**frontend/src/components/theme-provider.tsx** — React context provider for application theme management (dark/light/system).

- **Relationships:** Consumed by: Appearance, SidebarAppearance, Logo components via useTheme hook
Used by: App root component

### function ThemeProvider({
  children,
  defaultTheme = "system",
  storageKey = "vite-ui-theme",
  ...props
}: ThemeProviderProps) { [line 75] — Context provider managing theme state, localStorage persistence, and system preference detection.
- **Relationships:** Produces: ThemeProviderContext consumed by useTheme hook
Used by: App root
- **Flow:** 1. Read persisted theme from localStorage (or use default)
2. Apply theme class to document root element
3. Listen for system color-scheme changes when theme is "system"
4. Expose theme, resolvedTheme, and setTheme via context

### () => {
  const context = useContext(ThemeProviderContext)

  if (context === undefined)
    throw new Error("useTheme must be used within a ThemeProvider")

  return context
} [line 160] — Hook to access theme context (theme, resolvedTheme, setTheme).
- **Relationships:** Consumes: ThemeProviderContext
- **Imports:** react

## frontend/src/components/Admin

**frontend/src/components/Admin/AddUser.tsx** — Dialog for creating new user accounts in the admin panel.

- **Relationships:** Consumes: UsersService.createUser API
Used by: Admin users management page

### () => {
  const [isOpen, setIsOpen] = useState(false)
  const queryClient = useQueryClient()
  const { showSuccessToast, showErrorToast } = useCustomToast()

  const form = useForm<FormData>({
    resolver: zodResolver(formSchema),
    mode: "onBlur",
    criteriaMode: "all",
    defaultValues: {
      email: "",
      full_name: "",
      password: "",
      confirm_password: "",
      is_superuser: false,
      is_active: false,
    },
  })

  const mutation = useMutation({
    mutationFn: (data: UserCreate) =>
      UsersService.createUser({ requestBody: data }),
    onSuccess: () => {
      showSuccessToast("User created successfully")
      form.reset()
      setIsOpen(false)
    },
    onError: handleError.bind(showErrorToast),
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["users"] })
    },
  })

  const onSubmit = (data: FormData) => {
    mutation.mutate(data)
  }

  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DialogTrigger asChild>
        <Button className="my-4">
          <Plus className="mr-2" />
          Add User
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-md">
        <DialogHeader>
          <DialogTitle>Add User</DialogTitle>
          <DialogDescription>
            Fill in the form below to add a new user to the system.
          </DialogDescription>
        </DialogHeader>
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)}>
            <div className="grid gap-4 py-4">
              <FormField
                control={form.control}
                name="email"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>
                      Email <span className="text-destructive">*</span>
                    </FormLabel>
                    <FormControl>
                      <Input
                        placeholder="Email"
                        type="email"
                        {...field}
                        required
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="full_name"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Full Name</FormLabel>
                    <FormControl>
                      <Input placeholder="Full name" type="text" {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="password"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>
                      Set Password <span className="text-destructive">*</span>
                    </FormLabel>
                    <FormControl>
                      <Input
                        placeholder="Password"
                        type="password"
                        {...field}
                        required
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="confirm_password"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>
                      Confirm Password{" "}
                      <span className="text-destructive">*</span>
                    </FormLabel>
                    <FormControl>
                      <Input
                        placeholder="Password"
                        type="password"
                        {...field}
                        required
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="is_superuser"
                render={({ field }) => (
                  <FormItem className="flex items-center gap-3 space-y-0">
                    <FormControl>
                      <Checkbox
                        checked={field.value}
                        onCheckedChange={field.onChange}
                      />
                    </FormControl>
                    <FormLabel className="font-normal">Is superuser?</FormLabel>
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="is_active"
                render={({ field }) => (
                  <FormItem className="flex items-center gap-3 space-y-0">
                    <FormControl>
                      <Checkbox
                        checked={field.value}
                        onCheckedChange={field.onChange}
                      />
                    </FormControl>
                    <FormLabel className="font-normal">Is active?</FormLabel>
                  </FormItem>
                )}
              />
            </div>

            <DialogFooter>
              <DialogClose asChild>
                <Button variant="outline" disabled={mutation.isPending}>
                  Cancel
                </Button>
              </DialogClose>
              <LoadingButton type="submit" loading={mutation.isPending}>
                Save
              </LoadingButton>
            </DialogFooter>
          </form>
        </Form>
      </DialogContent>
    </Dialog>
  )
} [line 82] — Modal dialog for creating new user accounts with email, password, and role fields.
- **Relationships:** Consumes: UsersService.createUser API
Produces: New user record, success toast, invalidates "users" query cache
- **Flow:** 1. Open dialog via trigger button
2. Validate form fields (email, password, confirm, superuser, active)
3. Call createUser API on submit
4. Show success/error toast and close dialog
- **Imports:** 15 external dependencies
**frontend/src/components/Admin/DeleteUser.tsx** — Confirmation dialog for deleting a user account.

- **Relationships:** Consumes: UsersService.deleteUser API
Used by: UserActionsMenu dropdown

### ({ id, onSuccess }: DeleteUserProps) => {
  const [isOpen, setIsOpen] = useState(false)
  const queryClient = useQueryClient()
  const { showSuccessToast, showErrorToast } = useCustomToast()
  const { handleSubmit } = useForm()

  const deleteUser = async (id: string) => {
    await UsersService.deleteUser({ userId: id })
  }

  const mutation = useMutation({
    mutationFn: deleteUser,
    onSuccess: () => {
      showSuccessToast("The user was deleted successfully")
      setIsOpen(false)
      onSuccess()
    },
    onError: handleError.bind(showErrorToast),
    onSettled: () => {
      queryClient.invalidateQueries()
    },
  })

  const onSubmit = async () => {
    mutation.mutate(id)
  }

  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DropdownMenuItem
        variant="destructive"
        onSelect={(e) => e.preventDefault()}
        onClick={() => setIsOpen(true)}
      >
        <Trash2 />
        Delete User
      </DropdownMenuItem>
      <DialogContent className="sm:max-w-md">
        <form onSubmit={handleSubmit(onSubmit)}>
          <DialogHeader>
            <DialogTitle>Delete User</DialogTitle>
            <DialogDescription>
              All items associated with this user will also be{" "}
              <strong>permanently deleted.</strong> Are you sure? You will not
              be able to undo this action.
            </DialogDescription>
          </DialogHeader>

          <DialogFooter className="mt-4">
            <DialogClose asChild>
              <Button variant="outline" disabled={mutation.isPending}>
                Cancel
              </Button>
            </DialogClose>
            <LoadingButton
              variant="destructive"
              type="submit"
              loading={mutation.isPending}
            >
              Delete
            </LoadingButton>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  )
} [line 61] — Destructive confirmation dialog for permanently deleting a user and associated items.
- **Relationships:** Consumes: UsersService.deleteUser API
Produces: Success toast, invalidates all query caches
- **Flow:** 1. Render as dropdown menu item
2. Open confirmation dialog on click
3. Call deleteUser API on confirm
4. Show success/error toast and invoke onSuccess callback
- **Imports:** 11 external dependencies
**frontend/src/components/Admin/EditUser.tsx** — Dialog for editing existing user account details.

- **Relationships:** Consumes: UsersService.updateUser API
Used by: UserActionsMenu dropdown

### ({ user, onSuccess }: EditUserProps) => {
  const [isOpen, setIsOpen] = useState(false)
  const queryClient = useQueryClient()
  const { showSuccessToast, showErrorToast } = useCustomToast()

  const form = useForm<FormData>({
    resolver: zodResolver(formSchema),
    mode: "onBlur",
    criteriaMode: "all",
    defaultValues: {
      email: user.email,
      full_name: user.full_name ?? undefined,
      is_superuser: user.is_superuser,
      is_active: user.is_active,
    },
  })

  const mutation = useMutation({
    mutationFn: (data: FormData) =>
      UsersService.updateUser({ userId: user.id, requestBody: data }),
    onSuccess: () => {
      showSuccessToast("User updated successfully")
      setIsOpen(false)
      onSuccess()
    },
    onError: handleError.bind(showErrorToast),
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["users"] })
    },
  })

  const onSubmit = (data: FormData) => {
    // exclude confirm_password from submission data and remove password if empty
    const { confirm_password: _, ...submitData } = data
    if (!submitData.password) {
      delete submitData.password
    }
    mutation.mutate(submitData)
  }

  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DropdownMenuItem
        onSelect={(e) => e.preventDefault()}
        onClick={() => setIsOpen(true)}
      >
        <Pencil />
        Edit User
      </DropdownMenuItem>
      <DialogContent className="sm:max-w-md">
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)}>
            <DialogHeader>
              <DialogTitle>Edit User</DialogTitle>
              <DialogDescription>
                Update the user details below.
              </DialogDescription>
            </DialogHeader>
            <div className="grid gap-4 py-4">
              <FormField
                control={form.control}
                name="email"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>
                      Email <span className="text-destructive">*</span>
                    </FormLabel>
                    <FormControl>
                      <Input
                        placeholder="Email"
                        type="email"
                        {...field}
                        required
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="full_name"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Full Name</FormLabel>
                    <FormControl>
                      <Input placeholder="Full name" type="text" {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="password"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Set Password</FormLabel>
                    <FormControl>
                      <Input
                        placeholder="Password"
                        type="password"
                        {...field}
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="confirm_password"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Confirm Password</FormLabel>
                    <FormControl>
                      <Input
                        placeholder="Password"
                        type="password"
                        {...field}
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="is_superuser"
                render={({ field }) => (
                  <FormItem className="flex items-center gap-3 space-y-0">
                    <FormControl>
                      <Checkbox
                        checked={field.value}
                        onCheckedChange={field.onChange}
                      />
                    </FormControl>
                    <FormLabel className="font-normal">Is superuser?</FormLabel>
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="is_active"
                render={({ field }) => (
                  <FormItem className="flex items-center gap-3 space-y-0">
                    <FormControl>
                      <Checkbox
                        checked={field.value}
                        onCheckedChange={field.onChange}
                      />
                    </FormControl>
                    <FormLabel className="font-normal">Is active?</FormLabel>
                  </FormItem>
                )}
              />
            </div>

            <DialogFooter>
              <DialogClose asChild>
                <Button variant="outline" disabled={mutation.isPending}>
                  Cancel
                </Button>
              </DialogClose>
              <LoadingButton type="submit" loading={mutation.isPending}>
                Save
              </LoadingButton>
            </DialogFooter>
          </form>
        </Form>
      </DialogContent>
    </Dialog>
  )
} [line 95] — Modal dialog for editing user details (email, name, password, role, status).
- **Relationships:** Consumes: UsersService.updateUser API
Produces: Updated user record, success toast, invalidates "users" query cache
- **Flow:** 1. Render as dropdown menu item
2. Open dialog pre-populated with current user data
3. Validate and strip empty password before submit
4. Call updateUser API
5. Show success/error toast and invoke onSuccess callback
- **Imports:** 16 external dependencies
**frontend/src/components/Admin/UserActionsMenu.tsx** — Dropdown actions menu for user row operations (edit, delete).

- **Relationships:** Consumes: EditUser, DeleteUser components
Used by: Admin users table columns

### ({ user }: UserActionsMenuProps) => {
  const [open, setOpen] = useState(false)
  const { user: currentUser } = useAuth()

  if (user.id === currentUser?.id) {
    return null
  }

  return (
    <DropdownMenu open={open} onOpenChange={setOpen}>
      <DropdownMenuTrigger asChild>
        <Button variant="ghost" size="icon">
          <EllipsisVertical />
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        <EditUser user={user} onSuccess={() => setOpen(false)} />
        <DeleteUser id={user.id} onSuccess={() => setOpen(false)} />
      </DropdownMenuContent>
    </DropdownMenu>
  )
} [line 50] — Dropdown menu with edit/delete actions for a user table row.
- **Relationships:** Consumes: EditUser, DeleteUser components; useAuth for current user check
Used by: Admin users table actions column
- **Flow:** 1. Hide menu if target user is the current logged-in user
2. Render ellipsis trigger button
3. Show EditUser and DeleteUser options in dropdown
- **Imports:** ./DeleteUser, ./EditUser, @/client, @/components/ui/button, @/components/ui/dropdown-menu, @/hooks/useAuth, lucide-react, react
**frontend/src/components/Admin/columns.tsx** — Column definitions for the admin users data table.

- **Relationships:** Consumes: UserActionsMenu component, UserPublic type
Used by: Admin users page DataTable
- **Imports:** ./UserActionsMenu, @/client, @/components/ui/badge, @/lib/utils, @tanstack/react-table

## frontend/src/components/Common

**frontend/src/components/Common/Appearance.tsx** — Theme toggle components for switching between light, dark, and system modes.

- **Relationships:** Consumes: ThemeProvider context (useTheme)
Used by: AppSidebar (SidebarAppearance), AuthLayout (Appearance)

### () => {
  const { isMobile } = useSidebar()
  const { setTheme, theme } = useTheme()
  const Icon = ICON_MAP[theme]

  return (
    <SidebarMenuItem>
      <DropdownMenu modal={false}>
        <DropdownMenuTrigger asChild>
          <SidebarMenuButton tooltip="Appearance" data-testid="theme-button">
            <Icon className="size-4 text-muted-foreground" />
            <span>Appearance</span>
            <span className="sr-only">Toggle theme</span>
          </SidebarMenuButton>
        </DropdownMenuTrigger>
        <DropdownMenuContent
          side={isMobile ? "top" : "right"}
          align="end"
          className="w-(--radix-dropdown-menu-trigger-width) min-w-56"
        >
          <DropdownMenuItem
            data-testid="light-mode"
            onClick={() => setTheme("light")}
          >
            <Sun className="mr-2 h-4 w-4" />
            Light
          </DropdownMenuItem>
          <DropdownMenuItem
            data-testid="dark-mode"
            onClick={() => setTheme("dark")}
          >
            <Moon className="mr-2 h-4 w-4" />
            Dark
          </DropdownMenuItem>
          <DropdownMenuItem onClick={() => setTheme("system")}>
            <Monitor className="mr-2 h-4 w-4" />
            System
          </DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </SidebarMenuItem>
  )
} [line 42] — Sidebar-integrated theme toggle with icon reflecting current theme.
- **Relationships:** Consumes: useTheme, useSidebar contexts
Used by: AppSidebar footer

### () => {
  const { setTheme } = useTheme()

  return (
    <div className="flex items-center justify-center">
      <DropdownMenu modal={false}>
        <DropdownMenuTrigger asChild>
          <Button data-testid="theme-button" variant="outline" size="icon">
            <Sun className="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
            <Moon className="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100" />
            <span className="sr-only">Toggle theme</span>
          </Button>
        </DropdownMenuTrigger>
        <DropdownMenuContent align="end">
          <DropdownMenuItem
            data-testid="light-mode"
            onClick={() => setTheme("light")}
          >
            <Sun className="mr-2 h-4 w-4" />
            Light
          </DropdownMenuItem>
          <DropdownMenuItem
            data-testid="dark-mode"
            onClick={() => setTheme("dark")}
          >
            <Moon className="mr-2 h-4 w-4" />
            Dark
          </DropdownMenuItem>
          <DropdownMenuItem onClick={() => setTheme("system")}>
            <Monitor className="mr-2 h-4 w-4" />
            System
          </DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </div>
  )
} [line 93] — Standalone theme toggle button with sun/moon icon animation.
- **Relationships:** Consumes: useTheme context
Used by: AuthLayout header
- **Imports:** @/components/theme-provider, @/components/ui/button, @/components/ui/dropdown-menu, @/components/ui/sidebar, lucide-react
**frontend/src/components/Common/AuthLayout.tsx** — Two-column layout wrapper for authentication pages (login, signup, reset).

- **Relationships:** Consumes: Appearance, Logo, Footer components
Used by: Login, Signup, ResetPassword routes

### function AuthLayout({ children }: AuthLayoutProps) { [line 35] — Split-screen layout with logo panel (left) and auth form (right).
- **Relationships:** Consumes: Logo, Appearance, Footer components
Used by: Authentication route pages
- **Imports:** ./Footer, @/components/Common/Appearance, @/components/Common/Logo
**frontend/src/components/Common/DataTable.tsx** — Generic paginated data table component built on TanStack Table.

- **Relationships:** Consumes: TanStack Table core and pagination models
Used by: Admin users page, Items page

### function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) { [line 70] — Reusable paginated data table with configurable columns and page size.
- **Relationships:** Consumes: TanStack Table (getCoreRowModel, getPaginationRowModel)
Used by: Admin users page, Items page
- **Flow:** 1. Initialize table with data and column definitions
2. Render header groups and data rows
3. Show "No results" when empty
4. Render pagination controls when multiple pages exist
- **Imports:** @/components/ui/button, @/components/ui/select, @/components/ui/table, @tanstack/react-table, lucide-react
**frontend/src/components/Common/ErrorComponent.tsx** — Generic error page displayed when an unhandled error occurs.

- **Relationships:** Used by: Router error boundary

### () => {
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
} [line 19] — Full-screen error page with "Go Home" navigation link.
- **Relationships:** Produces: Navigation to root route via Link
- **Imports:** @/components/ui/button, @tanstack/react-router
**frontend/src/components/Common/Footer.tsx** — Application footer with copyright and social media links.

- **Relationships:** Used by: AuthLayout

### function Footer() { [line 33] — Footer bar with dynamic copyright year and GitHub/X/LinkedIn links.
- **Relationships:** Used by: AuthLayout
- **Imports:** react-icons/fa, react-icons/fa6
**frontend/src/components/Common/Logo.tsx** — Theme-aware FastAPI logo component with full, icon, and responsive variants.

- **Relationships:** Consumes: ThemeProvider context (useTheme)
Used by: AuthLayout, AppSidebar

### function Logo({
  variant = "full",
  className,
  asLink = true,
}: LogoProps) { [line 45] — Renders theme-aware FastAPI logo in full, icon, or responsive (collapsible) mode.
- **Relationships:** Consumes: useTheme for dark/light logo selection
Used by: AuthLayout (full), AppSidebar (responsive)
- **Imports:** /assets/images/fastapi-icon-light.svg, /assets/images/fastapi-icon.svg, /assets/images/fastapi-logo-light.svg, /assets/images/fastapi-logo.svg, @/components/theme-provider, @/lib/utils, @tanstack/react-router
**frontend/src/components/Common/NotFound.tsx** — 404 page displayed when a route is not matched.

- **Relationships:** Used by: Router notFoundComponent

### () => {
  return (
    <div
      className="flex min-h-screen items-center justify-center flex-col p-4"
      data-testid="not-found"
    >
      <div className="flex items-center z-10">
        <div className="flex flex-col ml-4 items-center justify-center p-4">
          <span className="text-6xl md:text-8xl font-bold leading-none mb-4">
            404
          </span>
          <span className="text-2xl font-bold mb-2">Oops!</span>
        </div>
      </div>

      <p className="text-lg text-muted-foreground mb-4 text-center z-10">
        The page you are looking for was not found.
      </p>
      <div className="z-10">
        <Link to="/">
          <Button className="mt-4">Go Back</Button>
        </Link>
      </div>
    </div>
  )
} [line 19] — Full-screen 404 page with "Go Back" navigation to home.
- **Relationships:** Produces: Navigation to root route via Link
- **Imports:** @/components/ui/button, @tanstack/react-router

## frontend/src/components/Dashboard

**frontend/src/components/Dashboard/TimeSummaryWidget.tsx** — Display time tracking summary on the dashboard with total hours and per-project breakdown.

- **Relationships:** Consumes: TimeEntriesService.getSummary, formatDuration
Produces: Dashboard summary card UI

### function TimeSummarySkeleton() { [line 30] — Render loading skeleton matching the widget structure.

### function TimeSummaryWidget() { [line 59] — Dashboard widget showing total hours logged and per-project breakdown.
- **Relationships:** Consumes: TimeEntriesService.getSummary
Produces: Card with formatted total and project list
- **Imports:** @/client, @/components/TimeEntries/columns, @/components/ui/card, @/components/ui/skeleton, @tanstack/react-query

## frontend/src/components/Items

**frontend/src/components/Items/AddItem.tsx** — Dialog for creating new items with title and description.

- **Relationships:** Consumes: ItemsService.createItem API
Used by: Items management page

### () => {
  const [isOpen, setIsOpen] = useState(false)
  const queryClient = useQueryClient()
  const { showSuccessToast, showErrorToast } = useCustomToast()

  const form = useForm<FormData>({
    resolver: zodResolver(formSchema),
    mode: "onBlur",
    criteriaMode: "all",
    defaultValues: {
      title: "",
      description: "",
    },
  })

  const mutation = useMutation({
    mutationFn: (data: ItemCreate) =>
      ItemsService.createItem({ requestBody: data }),
    onSuccess: () => {
      showSuccessToast("Item created successfully")
      form.reset()
      setIsOpen(false)
    },
    onError: handleError.bind(showErrorToast),
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["items"] })
    },
  })

  const onSubmit = (data: FormData) => {
    mutation.mutate(data)
  }

  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DialogTrigger asChild>
        <Button className="my-4">
          <Plus className="mr-2" />
          Add Item
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-md">
        <DialogHeader>
          <DialogTitle>Add Item</DialogTitle>
          <DialogDescription>
            Fill in the details to add a new item.
          </DialogDescription>
        </DialogHeader>
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)}>
            <div className="grid gap-4 py-4">
              <FormField
                control={form.control}
                name="title"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>
                      Title <span className="text-destructive">*</span>
                    </FormLabel>
                    <FormControl>
                      <Input
                        placeholder="Title"
                        type="text"
                        {...field}
                        required
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="description"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Description</FormLabel>
                    <FormControl>
                      <Input placeholder="Description" type="text" {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
            </div>

            <DialogFooter>
              <DialogClose asChild>
                <Button variant="outline" disabled={mutation.isPending}>
                  Cancel
                </Button>
              </DialogClose>
              <LoadingButton type="submit" loading={mutation.isPending}>
                Save
              </LoadingButton>
            </DialogFooter>
          </form>
        </Form>
      </DialogContent>
    </Dialog>
  )
} [line 67] — Modal dialog for creating a new item with title and optional description.
- **Relationships:** Consumes: ItemsService.createItem API
Produces: New item record, success toast, invalidates "items" query cache
- **Flow:** 1. Open dialog via trigger button
2. Validate title (required) and description (optional)
3. Call createItem API on submit
4. Show success/error toast and close dialog
- **Imports:** 14 external dependencies
**frontend/src/components/Items/DeleteItem.tsx** — Confirmation dialog for deleting an item.

- **Relationships:** Consumes: ItemsService.deleteItem API
Used by: ItemActionsMenu dropdown

### ({ id, onSuccess }: DeleteItemProps) => {
  const [isOpen, setIsOpen] = useState(false)
  const queryClient = useQueryClient()
  const { showSuccessToast, showErrorToast } = useCustomToast()
  const { handleSubmit } = useForm()

  const deleteItem = async (id: string) => {
    await ItemsService.deleteItem({ id: id })
  }

  const mutation = useMutation({
    mutationFn: deleteItem,
    onSuccess: () => {
      showSuccessToast("The item was deleted successfully")
      setIsOpen(false)
      onSuccess()
    },
    onError: handleError.bind(showErrorToast),
    onSettled: () => {
      queryClient.invalidateQueries()
    },
  })

  const onSubmit = async () => {
    mutation.mutate(id)
  }

  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DropdownMenuItem
        variant="destructive"
        onSelect={(e) => e.preventDefault()}
        onClick={() => setIsOpen(true)}
      >
        <Trash2 />
        Delete Item
      </DropdownMenuItem>
      <DialogContent className="sm:max-w-md">
        <form onSubmit={handleSubmit(onSubmit)}>
          <DialogHeader>
            <DialogTitle>Delete Item</DialogTitle>
            <DialogDescription>
              This item will be permanently deleted. Are you sure? You will not
              be able to undo this action.
            </DialogDescription>
          </DialogHeader>

          <DialogFooter className="mt-4">
            <DialogClose asChild>
              <Button variant="outline" disabled={mutation.isPending}>
                Cancel
              </Button>
            </DialogClose>
            <LoadingButton
              variant="destructive"
              type="submit"
              loading={mutation.isPending}
            >
              Delete
            </LoadingButton>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  )
} [line 61] — Destructive confirmation dialog for permanently deleting an item.
- **Relationships:** Consumes: ItemsService.deleteItem API
Produces: Success toast, invalidates all query caches
- **Flow:** 1. Render as dropdown menu item
2. Open confirmation dialog on click
3. Call deleteItem API on confirm
4. Show success/error toast and invoke onSuccess callback
- **Imports:** 11 external dependencies
**frontend/src/components/Items/EditItem.tsx** — Dialog for editing existing item details.

- **Relationships:** Consumes: ItemsService.updateItem API
Used by: ItemActionsMenu dropdown

### ({ item, onSuccess }: EditItemProps) => {
  const [isOpen, setIsOpen] = useState(false)
  const queryClient = useQueryClient()
  const { showSuccessToast, showErrorToast } = useCustomToast()

  const form = useForm<FormData>({
    resolver: zodResolver(formSchema),
    mode: "onBlur",
    criteriaMode: "all",
    defaultValues: {
      title: item.title,
      description: item.description ?? undefined,
    },
  })

  const mutation = useMutation({
    mutationFn: (data: FormData) =>
      ItemsService.updateItem({ id: item.id, requestBody: data }),
    onSuccess: () => {
      showSuccessToast("Item updated successfully")
      setIsOpen(false)
      onSuccess()
    },
    onError: handleError.bind(showErrorToast),
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["items"] })
    },
  })

  const onSubmit = (data: FormData) => {
    mutation.mutate(data)
  }

  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DropdownMenuItem
        onSelect={(e) => e.preventDefault()}
        onClick={() => setIsOpen(true)}
      >
        <Pencil />
        Edit Item
      </DropdownMenuItem>
      <DialogContent className="sm:max-w-md">
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)}>
            <DialogHeader>
              <DialogTitle>Edit Item</DialogTitle>
              <DialogDescription>
                Update the item details below.
              </DialogDescription>
            </DialogHeader>
            <div className="grid gap-4 py-4">
              <FormField
                control={form.control}
                name="title"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>
                      Title <span className="text-destructive">*</span>
                    </FormLabel>
                    <FormControl>
                      <Input placeholder="Title" type="text" {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="description"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Description</FormLabel>
                    <FormControl>
                      <Input placeholder="Description" type="text" {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
            </div>

            <DialogFooter>
              <DialogClose asChild>
                <Button variant="outline" disabled={mutation.isPending}>
                  Cancel
                </Button>
              </DialogClose>
              <LoadingButton type="submit" loading={mutation.isPending}>
                Save
              </LoadingButton>
            </DialogFooter>
          </form>
        </Form>
      </DialogContent>
    </Dialog>
  )
} [line 80] — Modal dialog for editing item title and description.
- **Relationships:** Consumes: ItemsService.updateItem API
Produces: Updated item record, success toast, invalidates "items" query cache
- **Flow:** 1. Render as dropdown menu item
2. Open dialog pre-populated with current item data
3. Validate and submit updated fields
4. Show success/error toast and invoke onSuccess callback
- **Imports:** 15 external dependencies
**frontend/src/components/Items/ItemActionsMenu.tsx** — Dropdown actions menu for item row operations (edit, delete).

- **Relationships:** Consumes: EditItem, DeleteItem components
Used by: Items table columns

### ({ item }: ItemActionsMenuProps) => {
  const [open, setOpen] = useState(false)

  return (
    <DropdownMenu open={open} onOpenChange={setOpen}>
      <DropdownMenuTrigger asChild>
        <Button variant="ghost" size="icon">
          <EllipsisVertical />
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        <EditItem item={item} onSuccess={() => setOpen(false)} />
        <DeleteItem id={item.id} onSuccess={() => setOpen(false)} />
      </DropdownMenuContent>
    </DropdownMenu>
  )
} [line 44] — Dropdown menu with edit/delete actions for an item table row.
- **Relationships:** Consumes: EditItem, DeleteItem components
Used by: Items table actions column
- **Imports:** ../Items/DeleteItem, ../Items/EditItem, @/client, @/components/ui/button, @/components/ui/dropdown-menu, lucide-react, react
**frontend/src/components/Items/columns.tsx** — Column definitions for the items data table.

- **Relationships:** Consumes: ItemActionsMenu component, ItemPublic type
Used by: Items page DataTable

### function CopyId({ id }: { id: string }) { [line 29] — Inline component displaying an item ID with copy-to-clipboard button.
- **Relationships:** Consumes: useCopyToClipboard hook
- **Imports:** ./ItemActionsMenu, @/client, @/components/ui/button, @/hooks/useCopyToClipboard, @/lib/utils, @tanstack/react-table, lucide-react

## frontend/src/components/Pending

**frontend/src/components/Pending/PendingItems.tsx** — Skeleton loading placeholder for the items table.

- **Relationships:** Used by: Items page during data fetch

### () => (
  <Table>
    <TableHeader>
      <TableRow>
        <TableHead>ID</TableHead>
        <TableHead>Title</TableHead>
        <TableHead>Description</TableHead>
        <TableHead>
          <span className="sr-only">Actions</span>
        </TableHead>
      </TableRow>
    </TableHeader>
    <TableBody>
      {Array.from({ length: 5 }).map((_, index) => (
        <TableRow key={index}>
          <TableCell>
            <Skeleton className="h-4 w-64 font-mono" />
          </TableCell>
          <TableCell>
            <Skeleton className="h-4 w-32" />
          </TableCell>
          <TableCell>
            <Skeleton className="h-4 w-48" />
          </TableCell>
          <TableCell>
            <div className="flex justify-end">
              <Skeleton className="size-8 rounded-md" />
            </div>
          </TableCell>
        </TableRow>
      ))}
    </TableBody>
  </Table>
) [line 26] — Renders 5 skeleton rows matching the items table column layout (ID, Title, Description, Actions).
- **Relationships:** Used by: Items page loading state
- **Imports:** @/components/ui/skeleton, @/components/ui/table
**frontend/src/components/Pending/PendingUsers.tsx** — Skeleton loading placeholder for the users table.

- **Relationships:** Used by: Admin users page during data fetch

### () => (
  <Table>
    <TableHeader>
      <TableRow>
        <TableHead>Full Name</TableHead>
        <TableHead>Email</TableHead>
        <TableHead>Role</TableHead>
        <TableHead>Status</TableHead>
        <TableHead>
          <span className="sr-only">Actions</span>
        </TableHead>
      </TableRow>
    </TableHeader>
    <TableBody>
      {Array.from({ length: 5 }).map((_, index) => (
        <TableRow key={index}>
          <TableCell>
            <Skeleton className="h-4 w-32" />
          </TableCell>
          <TableCell>
            <Skeleton className="h-4 w-40" />
          </TableCell>
          <TableCell>
            <Skeleton className="h-5 w-20 rounded-full" />
          </TableCell>
          <TableCell>
            <div className="flex items-center gap-2">
              <Skeleton className="size-2 rounded-full" />
              <Skeleton className="h-4 w-12" />
            </div>
          </TableCell>
          <TableCell>
            <div className="flex justify-end">
              <Skeleton className="size-8 rounded-md" />
            </div>
          </TableCell>
        </TableRow>
      ))}
    </TableBody>
  </Table>
) [line 26] — Renders 5 skeleton rows matching the users table column layout (Name, Email, Role, Status, Actions).
- **Relationships:** Used by: Admin users page loading state
- **Imports:** @/components/ui/skeleton, @/components/ui/table

## frontend/src/components/Projects

**frontend/src/components/Projects/AddProject.tsx** — Dialog for creating new projects with name and description.

- **Relationships:** Consumes: ProjectsService.createProject API
Used by: Projects management page

### () => {
  const [isOpen, setIsOpen] = useState(false)
  const queryClient = useQueryClient()
  const { showSuccessToast, showErrorToast } = useCustomToast()

  const form = useForm<FormData>({
    resolver: zodResolver(formSchema),
    mode: "onBlur",
    criteriaMode: "all",
    defaultValues: {
      name: "",
      description: "",
    },
  })

  const mutation = useMutation({
    mutationFn: (data: ProjectCreate) =>
      ProjectsService.createProject({ requestBody: data }),
    onSuccess: () => {
      showSuccessToast("Project created successfully")
      form.reset()
      setIsOpen(false)
    },
    onError: handleError.bind(showErrorToast),
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["projects"] })
    },
  })

  const onSubmit = (data: FormData) => {
    mutation.mutate(data)
  }

  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DialogTrigger asChild>
        <Button className="my-4">
          <Plus className="mr-2" />
          Add Project
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-md">
        <DialogHeader>
          <DialogTitle>Add Project</DialogTitle>
          <DialogDescription>
            Fill in the details to add a new project.
          </DialogDescription>
        </DialogHeader>
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)}>
            <div className="grid gap-4 py-4">
              <FormField
                control={form.control}
                name="name"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>
                      Name <span className="text-destructive">*</span>
                    </FormLabel>
                    <FormControl>
                      <Input
                        placeholder="Name"
                        type="text"
                        {...field}
                        required
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="description"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Description</FormLabel>
                    <FormControl>
                      <Input placeholder="Description" type="text" {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
            </div>

            <DialogFooter>
              <DialogClose asChild>
                <Button variant="outline" disabled={mutation.isPending}>
                  Cancel
                </Button>
              </DialogClose>
              <LoadingButton type="submit" loading={mutation.isPending}>
                Save
              </LoadingButton>
            </DialogFooter>
          </form>
        </Form>
      </DialogContent>
    </Dialog>
  )
} [line 73] — Modal dialog for creating a new project with name and optional description.
- **Relationships:** Consumes: ProjectsService.createProject API
Produces: New project record, success toast, invalidates "projects" query cache
- **Flow:** 1. Open dialog via trigger button
2. Validate name (required, max 255) and description (optional, max 255)
3. Call createProject API on submit
4. Show success/error toast and close dialog
- **Imports:** 14 external dependencies
**frontend/src/components/Projects/DeleteProject.tsx** — Confirmation dialog for deleting a project.

- **Relationships:** Consumes: ProjectsService.deleteProject API
Used by: ProjectActionsMenu dropdown

### ({ id, onSuccess }: DeleteProjectProps) => {
  const [isOpen, setIsOpen] = useState(false)
  const queryClient = useQueryClient()
  const { showSuccessToast, showErrorToast } = useCustomToast()
  const { handleSubmit } = useForm()

  const deleteProject = async (id: string) => {
    await ProjectsService.deleteProject({ id: id })
  }

  const mutation = useMutation({
    mutationFn: deleteProject,
    onSuccess: () => {
      showSuccessToast("The project was deleted successfully")
      setIsOpen(false)
      onSuccess()
    },
    onError: handleError.bind(showErrorToast),
    onSettled: () => {
      queryClient.invalidateQueries()
    },
  })

  const onSubmit = async () => {
    mutation.mutate(id)
  }

  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DropdownMenuItem
        variant="destructive"
        onSelect={(e) => e.preventDefault()}
        onClick={() => setIsOpen(true)}
      >
        <Trash2 />
        Delete Project
      </DropdownMenuItem>
      <DialogContent className="sm:max-w-md">
        <form onSubmit={handleSubmit(onSubmit)}>
          <DialogHeader>
            <DialogTitle>Delete Project</DialogTitle>
            <DialogDescription>
              This project will be permanently deleted. Are you sure? You will
              not be able to undo this action.
            </DialogDescription>
          </DialogHeader>

          <DialogFooter className="mt-4">
            <DialogClose asChild>
              <Button variant="outline" disabled={mutation.isPending}>
                Cancel
              </Button>
            </DialogClose>
            <LoadingButton
              variant="destructive"
              type="submit"
              loading={mutation.isPending}
            >
              Delete
            </LoadingButton>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  )
} [line 54] — Destructive confirmation dialog for permanently deleting a project.
- **Relationships:** Consumes: ProjectsService.deleteProject API
Produces: Success toast, invalidates all query caches
- **Flow:** 1. Render as dropdown menu item
2. Open confirmation dialog on click
3. Call deleteProject API on confirm
4. Show success/error toast and invoke onSuccess callback
- **Imports:** 11 external dependencies
**frontend/src/components/Projects/EditProject.tsx** — Dialog for editing existing project details.

- **Relationships:** Consumes: ProjectsService.updateProject API
Used by: ProjectActionsMenu dropdown

### ({ project, onSuccess }: EditProjectProps) => {
  const [isOpen, setIsOpen] = useState(false)
  const queryClient = useQueryClient()
  const { showSuccessToast, showErrorToast } = useCustomToast()

  const form = useForm<FormData>({
    resolver: zodResolver(formSchema),
    mode: "onBlur",
    criteriaMode: "all",
    defaultValues: {
      name: project.name,
      description: project.description ?? undefined,
    },
  })

  const mutation = useMutation({
    mutationFn: (data: FormData) =>
      ProjectsService.updateProject({ id: project.id, requestBody: data }),
    onSuccess: () => {
      showSuccessToast("Project updated successfully")
      setIsOpen(false)
      onSuccess()
    },
    onError: handleError.bind(showErrorToast),
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["projects"] })
    },
  })

  const onSubmit = (data: FormData) => {
    mutation.mutate(data)
  }

  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DropdownMenuItem
        onSelect={(e) => e.preventDefault()}
        onClick={() => setIsOpen(true)}
      >
        <Pencil />
        Edit Project
      </DropdownMenuItem>
      <DialogContent className="sm:max-w-md">
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)}>
            <DialogHeader>
              <DialogTitle>Edit Project</DialogTitle>
              <DialogDescription>
                Update the project details below.
              </DialogDescription>
            </DialogHeader>
            <div className="grid gap-4 py-4">
              <FormField
                control={form.control}
                name="name"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>
                      Name <span className="text-destructive">*</span>
                    </FormLabel>
                    <FormControl>
                      <Input placeholder="Name" type="text" {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="description"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Description</FormLabel>
                    <FormControl>
                      <Input placeholder="Description" type="text" {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
            </div>

            <DialogFooter>
              <DialogClose asChild>
                <Button variant="outline" disabled={mutation.isPending}>
                  Cancel
                </Button>
              </DialogClose>
              <LoadingButton type="submit" loading={mutation.isPending}>
                Save
              </LoadingButton>
            </DialogFooter>
          </form>
        </Form>
      </DialogContent>
    </Dialog>
  )
} [line 79] — Modal dialog for editing project name and description.
- **Relationships:** Consumes: ProjectsService.updateProject API
Produces: Updated project record, success toast, invalidates "projects" query cache
- **Flow:** 1. Render as dropdown menu item
2. Open dialog pre-populated with current project data
3. Validate and submit updated fields
4. Show success/error toast and invoke onSuccess callback
- **Imports:** 15 external dependencies
**frontend/src/components/Projects/PendingProjects.tsx** — Skeleton loading placeholder for the projects table.

- **Relationships:** Used by: Projects page during data fetch

### () => (
  <Table>
    <TableHeader>
      <TableRow>
        <TableHead>Name</TableHead>
        <TableHead>Description</TableHead>
        <TableHead>Created</TableHead>
        <TableHead>
          <span className="sr-only">Actions</span>
        </TableHead>
      </TableRow>
    </TableHeader>
    <TableBody>
      {Array.from({ length: 5 }).map((_, index) => (
        <TableRow key={index}>
          <TableCell>
            <Skeleton className="h-4 w-32" />
          </TableCell>
          <TableCell>
            <Skeleton className="h-4 w-48" />
          </TableCell>
          <TableCell>
            <Skeleton className="h-4 w-24" />
          </TableCell>
          <TableCell>
            <div className="flex justify-end">
              <Skeleton className="size-8 rounded-md" />
            </div>
          </TableCell>
        </TableRow>
      ))}
    </TableBody>
  </Table>
) [line 26] — Renders 5 skeleton rows matching the projects table column layout (Name, Description, Created, Actions).
- **Relationships:** Used by: Projects page loading state
- **Imports:** @/components/ui/skeleton, @/components/ui/table
**frontend/src/components/Projects/ProjectActionsMenu.tsx** — Dropdown actions menu for project row operations (edit, delete).

- **Relationships:** Consumes: EditProject, DeleteProject components
Used by: Projects table columns

### ({ project }: ProjectActionsMenuProps) => {
  const [open, setOpen] = useState(false)

  return (
    <DropdownMenu open={open} onOpenChange={setOpen}>
      <DropdownMenuTrigger asChild>
        <Button variant="ghost" size="icon">
          <EllipsisVertical />
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        <EditProject project={project} onSuccess={() => setOpen(false)} />
        <DeleteProject id={project.id} onSuccess={() => setOpen(false)} />
      </DropdownMenuContent>
    </DropdownMenu>
  )
} [line 38] — Dropdown menu with edit/delete actions for a project table row.
- **Relationships:** Consumes: EditProject, DeleteProject components
Used by: Projects table actions column
- **Imports:** ./DeleteProject, ./EditProject, @/client, @/components/ui/button, @/components/ui/dropdown-menu, lucide-react, react
**frontend/src/components/Projects/columns.tsx** — Column definitions for the projects data table.

- **Relationships:** Consumes: ProjectActionsMenu component, ProjectPublic type
Used by: Projects page DataTable
- **Imports:** ./ProjectActionsMenu, @/client, @/lib/utils, @tanstack/react-table

## frontend/src/components/Sidebar

**frontend/src/components/Sidebar/AppSidebar.tsx** — Main application sidebar with navigation, theme toggle, and user menu.

- **Relationships:** Consumes: Main, User, SidebarAppearance, Logo components; useAuth hook
Used by: Authenticated layout shell

### function AppSidebar() { [line 47] — Collapsible sidebar with navigation items, appearance toggle, and user menu.
- **Relationships:** Consumes: useAuth (current user/superuser check), Main, User, SidebarAppearance, Logo
Used by: Authenticated app layout
- **Flow:** 1. Determine nav items based on superuser status
2. Render Logo in header, Main nav in content, Appearance + User in footer
- **Imports:** ./Main, ./User, @/components/Common/Appearance, @/components/Common/Logo, @/components/ui/sidebar, @/hooks/useAuth, lucide-react
**frontend/src/components/Sidebar/Main.tsx** — Primary navigation menu rendered inside the sidebar.

- **Relationships:** Consumes: TanStack Router for active route detection
Used by: AppSidebar

### function Main({ items }: MainProps) { [line 62] — Renders sidebar navigation menu with active route highlighting.
- **Relationships:** Consumes: TanStack Router (useRouterState), useSidebar context
Used by: AppSidebar content area
- **Flow:** 1. Determine current path from router state
2. Render each item as SidebarMenuButton with active state
3. Auto-close mobile sidebar on navigation
- **Imports:** @/components/ui/sidebar, @tanstack/react-router, lucide-react
**frontend/src/components/Sidebar/User.tsx** — Sidebar user menu with avatar, settings link, and logout action.

- **Relationships:** Consumes: useAuth hook for logout, useSidebar for mobile handling
Used by: AppSidebar footer

### function UserInfo({ fullName, email }: UserInfoProps) { [line 51] — Avatar with name and email display used in sidebar user menu.

### function User({ user }: { user: any }) { [line 82] — Sidebar user dropdown with avatar, settings navigation, and logout.
- **Relationships:** Consumes: useAuth (logout), useSidebar (mobile close), getInitials utility
Used by: AppSidebar footer
- **Flow:** 1. Render avatar trigger with user info
2. Show dropdown with User Settings link and Log Out action
3. Auto-close mobile sidebar on settings navigation
- **Imports:** @/components/ui/avatar, @/components/ui/dropdown-menu, @/components/ui/sidebar, @/hooks/useAuth, @/utils, @tanstack/react-router, lucide-react

## frontend/src/components/TimeEntries

**frontend/src/components/TimeEntries/AddTimeEntry.tsx** — Dialog for creating new time entries with project, date, duration, and description.

- **Relationships:** Consumes: TimeEntriesService.createTimeEntry API, ProjectsService.readProjects API
Used by: Time Entries management page

### () => {
  const [isOpen, setIsOpen] = useState(false)
  const queryClient = useQueryClient()
  const { showSuccessToast, showErrorToast } = useCustomToast()

  const { data: projectsData } = useQuery({
    queryKey: ["projects"],
    queryFn: () => ProjectsService.readProjects({}),
  })

  const form = useForm<FormData>({
    resolver: zodResolver(formSchema),
    mode: "onBlur",
    criteriaMode: "all",
    defaultValues: {
      project_id: "",
      date: "",
      duration_minutes: "",
      description: "",
    },
  })

  const mutation = useMutation({
    mutationFn: (data: TimeEntryCreate) =>
      TimeEntriesService.createTimeEntry({ requestBody: data }),
    onSuccess: () => {
      showSuccessToast("Time entry created successfully")
      form.reset()
      setIsOpen(false)
    },
    onError: handleError.bind(showErrorToast),
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["time-entries"] })
    },
  })

  const onSubmit = (data: FormData) => {
    const minutes = parseInt(data.duration_minutes, 10)
    if (isNaN(minutes) || minutes < 1) return
    mutation.mutate({
      project_id: data.project_id,
      date: data.date,
      duration_minutes: minutes,
      description: data.description || null,
    })
  }

  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DialogTrigger asChild>
        <Button className="my-4">
          <Plus className="mr-2" />
          Add Time Entry
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-md">
        <DialogHeader>
          <DialogTitle>Add Time Entry</DialogTitle>
          <DialogDescription>
            Fill in the details to log a new time entry.
          </DialogDescription>
        </DialogHeader>
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)}>
            <div className="grid gap-4 py-4">
              <FormField
                control={form.control}
                name="project_id"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>
                      Project <span className="text-destructive">*</span>
                    </FormLabel>
                    <Select
                      onValueChange={field.onChange}
                      defaultValue={field.value}
                    >
                      <FormControl>
                        <SelectTrigger>
                          <SelectValue placeholder="Select a project" />
                        </SelectTrigger>
                      </FormControl>
                      <SelectContent>
                        {projectsData?.data.map((project) => (
                          <SelectItem key={project.id} value={project.id}>
                            {project.name}
                          </SelectItem>
                        ))}
                      </SelectContent>
                    </Select>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="date"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>
                      Date <span className="text-destructive">*</span>
                    </FormLabel>
                    <FormControl>
                      <Input type="date" {...field} required />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="duration_minutes"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>
                      Duration (minutes){" "}
                      <span className="text-destructive">*</span>
                    </FormLabel>
                    <FormControl>
                      <Input
                        placeholder="e.g. 90"
                        type="number"
                        min={1}
                        {...field}
                        required
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="description"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Description</FormLabel>
                    <FormControl>
                      <Input placeholder="Description" type="text" {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
            </div>

            <DialogFooter>
              <DialogClose asChild>
                <Button variant="outline" disabled={mutation.isPending}>
                  Cancel
                </Button>
              </DialogClose>
              <LoadingButton type="submit" loading={mutation.isPending}>
                Save
              </LoadingButton>
            </DialogFooter>
          </form>
        </Form>
      </DialogContent>
    </Dialog>
  )
} [line 84] — Modal dialog for creating a new time entry with project select, date, duration, and optional description.
- **Relationships:** Consumes: TimeEntriesService.createTimeEntry API, ProjectsService.readProjects API
Produces: New time entry record, success toast, invalidates "time-entries" query cache
- **Flow:** 1. Open dialog via trigger button
2. Fetch user's projects for select dropdown
3. Validate all fields client-side (Zod min(1) on duration_minutes)
4. Call createTimeEntry API on submit
5. Show success/error toast and close dialog
- **Imports:** 15 external dependencies
**frontend/src/components/TimeEntries/DeleteTimeEntry.tsx** — Confirmation dialog for deleting a time entry.

- **Relationships:** Consumes: TimeEntriesService.deleteTimeEntry API
Used by: TimeEntryActionsMenu dropdown

### ({ id, onSuccess }: DeleteTimeEntryProps) => {
  const [isOpen, setIsOpen] = useState(false)
  const queryClient = useQueryClient()
  const { showSuccessToast, showErrorToast } = useCustomToast()
  const { handleSubmit } = useForm()

  const deleteTimeEntry = async (id: string) => {
    await TimeEntriesService.deleteTimeEntry({ id: id })
  }

  const mutation = useMutation({
    mutationFn: deleteTimeEntry,
    onSuccess: () => {
      showSuccessToast("The time entry was deleted successfully")
      setIsOpen(false)
      onSuccess()
    },
    onError: handleError.bind(showErrorToast),
    onSettled: () => {
      queryClient.invalidateQueries()
    },
  })

  const onSubmit = async () => {
    mutation.mutate(id)
  }

  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DropdownMenuItem
        variant="destructive"
        onSelect={(e) => e.preventDefault()}
        onClick={() => setIsOpen(true)}
      >
        <Trash2 />
        Delete Time Entry
      </DropdownMenuItem>
      <DialogContent className="sm:max-w-md">
        <form onSubmit={handleSubmit(onSubmit)}>
          <DialogHeader>
            <DialogTitle>Delete Time Entry</DialogTitle>
            <DialogDescription>
              This time entry will be permanently deleted. Are you sure? You will
              not be able to undo this action.
            </DialogDescription>
          </DialogHeader>

          <DialogFooter className="mt-4">
            <DialogClose asChild>
              <Button variant="outline" disabled={mutation.isPending}>
                Cancel
              </Button>
            </DialogClose>
            <LoadingButton
              variant="destructive"
              type="submit"
              loading={mutation.isPending}
            >
              Delete
            </LoadingButton>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  )
} [line 54] — Destructive confirmation dialog for permanently deleting a time entry.
- **Relationships:** Consumes: TimeEntriesService.deleteTimeEntry API
Produces: Success toast, invalidates all query caches
- **Flow:** 1. Render as dropdown menu item
2. Open confirmation dialog on click
3. Call deleteTimeEntry API on confirm
4. Show success/error toast and invoke onSuccess callback
- **Imports:** 11 external dependencies
**frontend/src/components/TimeEntries/EditTimeEntry.tsx** — Dialog for editing existing time entry details.

- **Relationships:** Consumes: TimeEntriesService.updateTimeEntry API, ProjectsService.readProjects API
Used by: TimeEntryActionsMenu dropdown

### ({ timeEntry, onSuccess }: EditTimeEntryProps) => {
  const [isOpen, setIsOpen] = useState(false)
  const queryClient = useQueryClient()
  const { showSuccessToast, showErrorToast } = useCustomToast()

  const { data: projectsData } = useQuery({
    queryKey: ["projects"],
    queryFn: () => ProjectsService.readProjects({}),
  })

  const form = useForm<FormData>({
    resolver: zodResolver(formSchema),
    mode: "onBlur",
    criteriaMode: "all",
    defaultValues: {
      project_id: timeEntry.project_id,
      date: timeEntry.date,
      duration_minutes: String(timeEntry.duration_minutes),
      description: timeEntry.description ?? undefined,
    },
  })

  const mutation = useMutation({
    mutationFn: (data: FormData) => {
      const minutes = parseInt(data.duration_minutes, 10)
      return TimeEntriesService.updateTimeEntry({
        id: timeEntry.id,
        requestBody: {
          project_id: data.project_id,
          date: data.date,
          duration_minutes: minutes,
          description: data.description || null,
        },
      })
    },
    onSuccess: () => {
      showSuccessToast("Time entry updated successfully")
      setIsOpen(false)
      onSuccess()
    },
    onError: handleError.bind(showErrorToast),
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["time-entries"] })
    },
  })

  const onSubmit = (data: FormData) => {
    mutation.mutate(data)
  }

  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DropdownMenuItem
        onSelect={(e) => e.preventDefault()}
        onClick={() => setIsOpen(true)}
      >
        <Pencil />
        Edit Time Entry
      </DropdownMenuItem>
      <DialogContent className="sm:max-w-md">
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)}>
            <DialogHeader>
              <DialogTitle>Edit Time Entry</DialogTitle>
              <DialogDescription>
                Update the time entry details below.
              </DialogDescription>
            </DialogHeader>
            <div className="grid gap-4 py-4">
              <FormField
                control={form.control}
                name="project_id"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>
                      Project <span className="text-destructive">*</span>
                    </FormLabel>
                    <Select
                      onValueChange={field.onChange}
                      defaultValue={field.value}
                    >
                      <FormControl>
                        <SelectTrigger>
                          <SelectValue placeholder="Select a project" />
                        </SelectTrigger>
                      </FormControl>
                      <SelectContent>
                        {projectsData?.data.map((project) => (
                          <SelectItem key={project.id} value={project.id}>
                            {project.name}
                          </SelectItem>
                        ))}
                      </SelectContent>
                    </Select>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="date"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>
                      Date <span className="text-destructive">*</span>
                    </FormLabel>
                    <FormControl>
                      <Input type="date" {...field} required />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="duration_minutes"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>
                      Duration (minutes){" "}
                      <span className="text-destructive">*</span>
                    </FormLabel>
                    <FormControl>
                      <Input
                        placeholder="e.g. 90"
                        type="number"
                        min={1}
                        {...field}
                        required
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="description"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Description</FormLabel>
                    <FormControl>
                      <Input placeholder="Description" type="text" {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
            </div>

            <DialogFooter>
              <DialogClose asChild>
                <Button variant="outline" disabled={mutation.isPending}>
                  Cancel
                </Button>
              </DialogClose>
              <LoadingButton type="submit" loading={mutation.isPending}>
                Save
              </LoadingButton>
            </DialogFooter>
          </form>
        </Form>
      </DialogContent>
    </Dialog>
  )
} [line 85] — Modal dialog for editing time entry project, date, duration, and description.
- **Relationships:** Consumes: TimeEntriesService.updateTimeEntry API, ProjectsService.readProjects API
Produces: Updated time entry record, success toast, invalidates "time-entries" query cache
- **Flow:** 1. Render as dropdown menu item
2. Open dialog pre-populated with current time entry data
3. Validate and submit updated fields
4. Show success/error toast and invoke onSuccess callback
- **Imports:** 16 external dependencies
**frontend/src/components/TimeEntries/PendingTimeEntries.tsx** — Skeleton loading placeholder for the time entries table.

- **Relationships:** Used by: Time Entries page during data fetch

### () => (
  <Table>
    <TableHeader>
      <TableRow>
        <TableHead>Project</TableHead>
        <TableHead>Date</TableHead>
        <TableHead>Duration</TableHead>
        <TableHead>Description</TableHead>
        <TableHead>
          <span className="sr-only">Actions</span>
        </TableHead>
      </TableRow>
    </TableHeader>
    <TableBody>
      {Array.from({ length: 5 }).map((_, index) => (
        <TableRow key={index}>
          <TableCell>
            <Skeleton className="h-4 w-28" />
          </TableCell>
          <TableCell>
            <Skeleton className="h-4 w-24" />
          </TableCell>
          <TableCell>
            <Skeleton className="h-4 w-16" />
          </TableCell>
          <TableCell>
            <Skeleton className="h-4 w-48" />
          </TableCell>
          <TableCell>
            <div className="flex justify-end">
              <Skeleton className="size-8 rounded-md" />
            </div>
          </TableCell>
        </TableRow>
      ))}
    </TableBody>
  </Table>
) [line 26] — Renders 5 skeleton rows matching the time entries table column layout (Project, Date, Duration, Description, Actions).
- **Relationships:** Used by: Time Entries page loading state
- **Imports:** @/components/ui/skeleton, @/components/ui/table
**frontend/src/components/TimeEntries/TimeEntryActionsMenu.tsx** — Dropdown actions menu for time entry row operations (edit, delete).

- **Relationships:** Consumes: EditTimeEntry, DeleteTimeEntry components
Used by: Time entries table columns

### ({
  timeEntry,
}: TimeEntryActionsMenuProps) => {
  const [open, setOpen] = useState(false)

  return (
    <DropdownMenu open={open} onOpenChange={setOpen}>
      <DropdownMenuTrigger asChild>
        <Button variant="ghost" size="icon">
          <EllipsisVertical />
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        <EditTimeEntry timeEntry={timeEntry} onSuccess={() => setOpen(false)} />
        <DeleteTimeEntry id={timeEntry.id} onSuccess={() => setOpen(false)} />
      </DropdownMenuContent>
    </DropdownMenu>
  )
} [line 38] — Dropdown menu with edit/delete actions for a time entry table row.
- **Relationships:** Consumes: EditTimeEntry, DeleteTimeEntry components
Used by: Time entries table actions column
- **Imports:** ./DeleteTimeEntry, ./EditTimeEntry, @/client, @/components/ui/button, @/components/ui/dropdown-menu, lucide-react, react
**frontend/src/components/TimeEntries/columns.tsx** — Column definitions for the time entries data table.

- **Relationships:** Consumes: TimeEntryActionsMenu component, TimeEntryPublic type
Used by: Time Entries page DataTable

### function formatDuration(minutes: number): string { [line 24] — Format duration in minutes to "Xh Ym" string.

### function parseDuration(formatted: string): number { [line 39] — Parse "Xh Ym" formatted string back to minutes.
- **Imports:** ./TimeEntryActionsMenu, @/client, @/lib/utils, @tanstack/react-table

## frontend/src/components/UserSettings

**frontend/src/components/UserSettings/ChangePassword.tsx** — Form for changing the current user's password.

- **Relationships:** Consumes: UsersService.updatePasswordMe API
Used by: User settings page

### () => {
  const { showSuccessToast, showErrorToast } = useCustomToast()
  const form = useForm<FormData>({
    resolver: zodResolver(formSchema),
    mode: "onSubmit",
    criteriaMode: "all",
    defaultValues: {
      current_password: "",
      new_password: "",
      confirm_password: "",
    },
  })

  const mutation = useMutation({
    mutationFn: (data: UpdatePassword) =>
      UsersService.updatePasswordMe({ requestBody: data }),
    onSuccess: () => {
      showSuccessToast("Password updated successfully")
      form.reset()
    },
    onError: handleError.bind(showErrorToast),
  })

  const onSubmit = async (data: FormData) => {
    mutation.mutate(data)
  }

  return (
    <div className="max-w-md">
      <h3 className="text-lg font-semibold py-4">Change Password</h3>
      <Form {...form}>
        <form
          onSubmit={form.handleSubmit(onSubmit)}
          className="flex flex-col gap-4"
        >
          <FormField
            control={form.control}
            name="current_password"
            render={({ field, fieldState }) => (
              <FormItem>
                <FormLabel>Current Password</FormLabel>
                <FormControl>
                  <PasswordInput
                    data-testid="current-password-input"
                    placeholder="••••••••"
                    aria-invalid={fieldState.invalid}
                    {...field}
                  />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            control={form.control}
            name="new_password"
            render={({ field, fieldState }) => (
              <FormItem>
                <FormLabel>New Password</FormLabel>
                <FormControl>
                  <PasswordInput
                    data-testid="new-password-input"
                    placeholder="••••••••"
                    aria-invalid={fieldState.invalid}
                    {...field}
                  />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            control={form.control}
            name="confirm_password"
            render={({ field, fieldState }) => (
              <FormItem>
                <FormLabel>Confirm Password</FormLabel>
                <FormControl>
                  <PasswordInput
                    data-testid="confirm-password-input"
                    placeholder="••••••••"
                    aria-invalid={fieldState.invalid}
                    {...field}
                  />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />

          <LoadingButton
            type="submit"
            loading={mutation.isPending}
            className="self-start"
          >
            Update Password
          </LoadingButton>
        </form>
      </Form>
    </div>
  )
} [line 67] — Password change form with current, new, and confirm password fields.
- **Relationships:** Consumes: UsersService.updatePasswordMe API
Produces: Success toast, form reset on success
- **Flow:** 1. Render current password, new password, confirm password fields
2. Validate password match and minimum length
3. Call updatePasswordMe API on submit
4. Show success/error toast and reset form
- **Imports:** @/client, @/components/ui/form, @/components/ui/loading-button, @/components/ui/password-input, @/hooks/useCustomToast, @/utils, @hookform/resolvers/zod, @tanstack/react-query, react-hook-form, zod
**frontend/src/components/UserSettings/DeleteAccount.tsx** — Danger zone section for account self-deletion.

- **Relationships:** Consumes: DeleteConfirmation component
Used by: User settings page

### () => {
  return (
    <div className="max-w-md mt-4 rounded-lg border border-destructive/50 p-4">
      <h3 className="font-semibold text-destructive">Delete Account</h3>
      <p className="mt-1 text-sm text-muted-foreground">
        Permanently delete your account and all associated data.
      </p>
      <DeleteConfirmation />
    </div>
  )
} [line 20] — Destructive-styled card with account deletion warning and confirmation trigger.
- **Relationships:** Consumes: DeleteConfirmation dialog component
Used by: User settings page
- **Imports:** ./DeleteConfirmation
**frontend/src/components/UserSettings/DeleteConfirmation.tsx** — Confirmation dialog for self-deleting the current user's account.

- **Relationships:** Consumes: UsersService.deleteUserMe API, useAuth logout
Used by: DeleteAccount component

### () => {
  const queryClient = useQueryClient()
  const { showSuccessToast, showErrorToast } = useCustomToast()
  const { handleSubmit } = useForm()
  const { logout } = useAuth()

  const mutation = useMutation({
    mutationFn: () => UsersService.deleteUserMe(),
    onSuccess: () => {
      showSuccessToast("Your account has been successfully deleted")
      logout()
    },
    onError: handleError.bind(showErrorToast),
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["currentUser"] })
    },
  })

  const onSubmit = async () => {
    mutation.mutate()
  }

  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="destructive" className="mt-3">
          Delete Account
        </Button>
      </DialogTrigger>
      <DialogContent>
        <form onSubmit={handleSubmit(onSubmit)}>
          <DialogHeader>
            <DialogTitle>Confirmation Required</DialogTitle>
            <DialogDescription>
              All your account data will be{" "}
              <strong>permanently deleted.</strong> If you are sure, please
              click <strong>"Confirm"</strong> to proceed. This action cannot be
              undone.
            </DialogDescription>
          </DialogHeader>

          <DialogFooter className="mt-4">
            <DialogClose asChild>
              <Button variant="outline" disabled={mutation.isPending}>
                Cancel
              </Button>
            </DialogClose>
            <LoadingButton
              variant="destructive"
              type="submit"
              loading={mutation.isPending}
            >
              Delete
            </LoadingButton>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  )
} [line 44] — Modal confirmation dialog for permanent account self-deletion.
- **Relationships:** Consumes: UsersService.deleteUserMe API, useAuth (logout)
Produces: Account deletion, logout, invalidates "currentUser" query cache
- **Flow:** 1. Open dialog via "Delete Account" trigger button
2. Show permanent deletion warning
3. Call deleteUserMe API on confirm
4. Show success toast and trigger logout
- **Imports:** @/client, @/components/ui/button, @/components/ui/dialog, @/components/ui/loading-button, @/hooks/useAuth, @/hooks/useCustomToast, @/utils, @tanstack/react-query, react-hook-form
**frontend/src/components/UserSettings/UserInformation.tsx** — Editable display of current user's profile information (name, email).

- **Relationships:** Consumes: UsersService.updateUserMe API, useAuth hook
Used by: User settings page

### () => {
  const queryClient = useQueryClient()
  const { showSuccessToast, showErrorToast } = useCustomToast()
  const [editMode, setEditMode] = useState(false)
  const { user: currentUser } = useAuth()

  const form = useForm<FormData>({
    resolver: zodResolver(formSchema),
    mode: "onBlur",
    criteriaMode: "all",
    defaultValues: {
      full_name: currentUser?.full_name ?? undefined,
      email: currentUser?.email,
    },
  })

  const toggleEditMode = () => {
    setEditMode(!editMode)
  }

  const mutation = useMutation({
    mutationFn: (data: UserUpdateMe) =>
      UsersService.updateUserMe({ requestBody: data }),
    onSuccess: () => {
      showSuccessToast("User updated successfully")
      toggleEditMode()
    },
    onError: handleError.bind(showErrorToast),
    onSettled: () => {
      queryClient.invalidateQueries()
    },
  })

  const onSubmit = (data: FormData) => {
    const updateData: UserUpdateMe = {}

    // only include fields that have changed
    if (data.full_name !== currentUser?.full_name) {
      updateData.full_name = data.full_name
    }
    if (data.email !== currentUser?.email) {
      updateData.email = data.email
    }

    mutation.mutate(updateData)
  }

  const onCancel = () => {
    form.reset()
    toggleEditMode()
  }

  return (
    <div className="max-w-md">
      <h3 className="text-lg font-semibold py-4">User Information</h3>
      <Form {...form}>
        <form
          onSubmit={form.handleSubmit(onSubmit)}
          className="flex flex-col gap-4"
        >
          <FormField
            control={form.control}
            name="full_name"
            render={({ field }) =>
              editMode ? (
                <FormItem>
                  <FormLabel>Full name</FormLabel>
                  <FormControl>
                    <Input type="text" {...field} />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              ) : (
                <FormItem>
                  <FormLabel>Full name</FormLabel>
                  <p
                    className={cn(
                      "py-2 truncate max-w-sm",
                      !field.value && "text-muted-foreground",
                    )}
                  >
                    {field.value || "N/A"}
                  </p>
                </FormItem>
              )
            }
          />

          <FormField
            control={form.control}
            name="email"
            render={({ field }) =>
              editMode ? (
                <FormItem>
                  <FormLabel>Email</FormLabel>
                  <FormControl>
                    <Input type="email" {...field} />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              ) : (
                <FormItem>
                  <FormLabel>Email</FormLabel>
                  <p className="py-2 truncate max-w-sm">{field.value}</p>
                </FormItem>
              )
            }
          />

          <div className="flex gap-3">
            {editMode ? (
              <>
                <LoadingButton
                  type="submit"
                  loading={mutation.isPending}
                  disabled={!form.formState.isDirty}
                >
                  Save
                </LoadingButton>
                <Button
                  type="button"
                  variant="outline"
                  onClick={onCancel}
                  disabled={mutation.isPending}
                >
                  Cancel
                </Button>
              </>
            ) : (
              <Button type="button" onClick={toggleEditMode}>
                Edit
              </Button>
            )}
          </div>
        </form>
      </Form>
    </div>
  )
} [line 58] — Toggle-editable form displaying and updating current user's name and email.
- **Relationships:** Consumes: UsersService.updateUserMe API, useAuth (current user data)
Produces: Updated user profile, success toast, invalidates all query caches
- **Flow:** 1. Display user info in read-only mode with Edit button
2. Switch to editable inputs on Edit click
3. Submit only changed fields to updateUserMe API
4. Show success/error toast and return to read-only mode
- **Imports:** 14 external dependencies

## frontend/src/components/ui

**frontend/src/components/ui/alert.tsx**


### function Alert({
  className,
  variant,
  ...props
}: React.ComponentProps<"div"> & VariantProps<typeof alertVariants>) { [line 22]

### function AlertTitle({ className, ...props }: React.ComponentProps<"div">) { [line 37]

### function AlertDescription({
  className,
  ...props
}: React.ComponentProps<"div">) { [line 50]
- **Imports:** @/lib/utils, class-variance-authority, react
**frontend/src/components/ui/avatar.tsx**


### function Avatar({
  className,
  ...props
}: React.ComponentProps<typeof AvatarPrimitive.Root>) { [line 6]

### function AvatarImage({
  className,
  ...props
}: React.ComponentProps<typeof AvatarPrimitive.Image>) { [line 22]

### function AvatarFallback({
  className,
  ...props
}: React.ComponentProps<typeof AvatarPrimitive.Fallback>) { [line 35]
- **Imports:** @/lib/utils, @radix-ui/react-avatar, react
**frontend/src/components/ui/badge.tsx**


### function Badge({
  className,
  variant,
  asChild = false,
  ...props
}: React.ComponentProps<"span"> &
  VariantProps<typeof badgeVariants> & { asChild?: boolean }) { [line 28]
- **Imports:** @/lib/utils, @radix-ui/react-slot, class-variance-authority, react
**frontend/src/components/ui/button-group.tsx**


### function ButtonGroup({
  className,
  orientation,
  ...props
}: React.ComponentProps<"div"> & VariantProps<typeof buttonGroupVariants>) { [line 24]

### function ButtonGroupText({
  className,
  asChild = false,
  ...props
}: React.ComponentProps<"div"> & {
  asChild?: boolean
}) { [line 40]

### function ButtonGroupSeparator({
  className,
  orientation = "vertical",
  ...props
}: React.ComponentProps<typeof Separator>) { [line 60]
- **Imports:** @/components/ui/separator, @/lib/utils, @radix-ui/react-slot, class-variance-authority
**frontend/src/components/ui/button.tsx**


### function Button({
  className,
  variant,
  size,
  asChild = false,
  ...props
}: React.ComponentProps<"button"> &
  VariantProps<typeof buttonVariants> & {
    asChild?: boolean
  }) { [line 39]
- **Imports:** @/lib/utils, @radix-ui/react-slot, class-variance-authority, react
**frontend/src/components/ui/card.tsx**


### function Card({ className, ...props }: React.ComponentProps<"div">) { [line 5]

### function CardHeader({ className, ...props }: React.ComponentProps<"div">) { [line 18]

### function CardTitle({ className, ...props }: React.ComponentProps<"div">) { [line 31]

### function CardDescription({ className, ...props }: React.ComponentProps<"div">) { [line 41]

### function CardAction({ className, ...props }: React.ComponentProps<"div">) { [line 51]

### function CardContent({ className, ...props }: React.ComponentProps<"div">) { [line 64]

### function CardFooter({ className, ...props }: React.ComponentProps<"div">) { [line 74]
- **Imports:** @/lib/utils, react
**frontend/src/components/ui/checkbox.tsx**


### function Checkbox({
  className,
  ...props
}: React.ComponentProps<typeof CheckboxPrimitive.Root>) { [line 7]
- **Imports:** @/lib/utils, @radix-ui/react-checkbox, lucide-react, react
**frontend/src/components/ui/dialog.tsx**


### function Dialog({
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Root>) { [line 7]

### function DialogTrigger({
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Trigger>) { [line 13]

### function DialogPortal({
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Portal>) { [line 19]

### function DialogClose({
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Close>) { [line 25]

### function DialogOverlay({
  className,
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Overlay>) { [line 31]

### function DialogContent({
  className,
  children,
  showCloseButton = true,
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Content> & {
  showCloseButton?: boolean
}) { [line 47]

### function DialogHeader({ className, ...props }: React.ComponentProps<"div">) { [line 81]

### function DialogFooter({ className, ...props }: React.ComponentProps<"div">) { [line 91]

### function DialogTitle({
  className,
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Title>) { [line 104]

### function DialogDescription({
  className,
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Description>) { [line 117]
- **Imports:** @/lib/utils, @radix-ui/react-dialog, lucide-react, react
**frontend/src/components/ui/dropdown-menu.tsx**


### function DropdownMenu({
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Root>) { [line 9]

### function DropdownMenuPortal({
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Portal>) { [line 15]

### function DropdownMenuTrigger({
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Trigger>) { [line 23]

### function DropdownMenuContent({
  className,
  sideOffset = 4,
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Content>) { [line 34]

### function DropdownMenuGroup({
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Group>) { [line 54]

### function DropdownMenuItem({
  className,
  inset,
  variant = "default",
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Item> & {
  inset?: boolean
  variant?: "default" | "destructive"
}) { [line 62]

### function DropdownMenuCheckboxItem({
  className,
  children,
  checked,
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.CheckboxItem>) { [line 85]

### function DropdownMenuRadioGroup({
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.RadioGroup>) { [line 111]

### function DropdownMenuRadioItem({
  className,
  children,
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.RadioItem>) { [line 122]

### function DropdownMenuLabel({
  className,
  inset,
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Label> & {
  inset?: boolean
}) { [line 146]

### function DropdownMenuSeparator({
  className,
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Separator>) { [line 166]

### function DropdownMenuShortcut({
  className,
  ...props
}: React.ComponentProps<"span">) { [line 179]

### function DropdownMenuSub({
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Sub>) { [line 195]

### function DropdownMenuSubTrigger({
  className,
  inset,
  children,
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.SubTrigger> & {
  inset?: boolean
}) { [line 201]

### function DropdownMenuSubContent({
  className,
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.SubContent>) { [line 225]
- **Imports:** @/lib/utils, @radix-ui/react-dropdown-menu, lucide-react, react
**frontend/src/components/ui/form.tsx**


### <
  TFieldValues extends FieldValues = FieldValues,
  TName extends FieldPath<TFieldValues> = FieldPath<TFieldValues>,
>({
  ...props
}: ControllerProps<TFieldValues, TName>) => {
  return (
    <FormFieldContext.Provider value={{ name: props.name }}>
      <Controller {...props} />
    </FormFieldContext.Provider>
  )
} [line 30]

### () => {
  const fieldContext = React.useContext(FormFieldContext)
  const itemContext = React.useContext(FormItemContext)
  const { getFieldState } = useFormContext()
  const formState = useFormState({ name: fieldContext.name })
  const fieldState = getFieldState(fieldContext.name, formState)

  if (!fieldContext) {
    throw new Error("useFormField should be used within <FormField>")
  }

  const { id } = itemContext

  return {
    id,
    name: fieldContext.name,
    formItemId: `${id}-form-item`,
    formDescriptionId: `${id}-form-item-description`,
    formMessageId: `${id}-form-item-message`,
    ...fieldState,
  }
} [line 43]

### function FormItem({ className, ...props }: React.ComponentProps<"div">) { [line 74]

### function FormLabel({
  className,
  ...props
}: React.ComponentProps<typeof LabelPrimitive.Root>) { [line 88]

### function FormControl({ ...props }: React.ComponentProps<typeof Slot>) { [line 105]

### function FormDescription({ className, ...props }: React.ComponentProps<"p">) { [line 123]

### function FormMessage({ className, ...props }: React.ComponentProps<"p">) { [line 136]
- **Imports:** @/components/ui/label, @/lib/utils, @radix-ui/react-label, @radix-ui/react-slot, react, react-hook-form
**frontend/src/components/ui/input.tsx**


### function Input({ className, type, ...props }: React.ComponentProps<"input">) { [line 5]
- **Imports:** @/lib/utils, react
**frontend/src/components/ui/label.tsx**


### function Label({
  className,
  ...props
}: React.ComponentProps<typeof LabelPrimitive.Root>) { [line 8]
- **Imports:** @/lib/utils, @radix-ui/react-label, react
**frontend/src/components/ui/loading-button.tsx**


### function LoadingButton({
  className,
  loading = false,
  children,
  disabled,
  variant,
  size,
  asChild = false,
  ...props
}: ButtonProps) { [line 44]
- **Imports:** @/lib/utils, @radix-ui/react-slot, class-variance-authority, lucide-react
**frontend/src/components/ui/pagination.tsx**


### function Pagination({ className, ...props }: React.ComponentProps<"nav">) { [line 11]

### function PaginationContent({
  className,
  ...props
}: React.ComponentProps<"ul">) { [line 23]

### function PaginationItem({ ...props }: React.ComponentProps<"li">) { [line 36]

### function PaginationLink({
  className,
  isActive,
  size = "icon",
  ...props
}: PaginationLinkProps) { [line 45]

### function PaginationPrevious({
  className,
  ...props
}: React.ComponentProps<typeof PaginationLink>) { [line 68]

### function PaginationNext({
  className,
  ...props
}: React.ComponentProps<typeof PaginationLink>) { [line 85]

### function PaginationEllipsis({
  className,
  ...props
}: React.ComponentProps<"span">) { [line 102]
- **Imports:** @/components/ui/button, @/lib/utils, lucide-react, react
**frontend/src/components/ui/password-input.tsx**

- **Imports:** ./button, @/lib/utils, lucide-react, react
**frontend/src/components/ui/select.tsx**


### function Select({
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Root>) { [line 7]

### function SelectGroup({
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Group>) { [line 13]

### function SelectValue({
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Value>) { [line 19]

### function SelectTrigger({
  className,
  size = "default",
  children,
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Trigger> & {
  size?: "sm" | "default"
}) { [line 25]

### function SelectContent({
  className,
  children,
  position = "popper",
  align = "center",
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Content>) { [line 51]

### function SelectLabel({
  className,
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Label>) { [line 88]

### function SelectItem({
  className,
  children,
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Item>) { [line 101]

### function SelectSeparator({
  className,
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Separator>) { [line 125]

### function SelectScrollUpButton({
  className,
  ...props
}: React.ComponentProps<typeof SelectPrimitive.ScrollUpButton>) { [line 138]

### function SelectScrollDownButton({
  className,
  ...props
}: React.ComponentProps<typeof SelectPrimitive.ScrollDownButton>) { [line 156]
- **Imports:** @/lib/utils, @radix-ui/react-select, lucide-react, react
**frontend/src/components/ui/separator.tsx**


### function Separator({
  className,
  orientation = "horizontal",
  decorative = true,
  ...props
}: React.ComponentProps<typeof SeparatorPrimitive.Root>) { [line 6]
- **Imports:** @/lib/utils, @radix-ui/react-separator, react
**frontend/src/components/ui/sheet.tsx**


### function Sheet({ ...props }: React.ComponentProps<typeof SheetPrimitive.Root>) { [line 9]

### function SheetTrigger({
  ...props
}: React.ComponentProps<typeof SheetPrimitive.Trigger>) { [line 13]

### function SheetClose({
  ...props
}: React.ComponentProps<typeof SheetPrimitive.Close>) { [line 19]

### function SheetPortal({
  ...props
}: React.ComponentProps<typeof SheetPrimitive.Portal>) { [line 25]

### function SheetOverlay({
  className,
  ...props
}: React.ComponentProps<typeof SheetPrimitive.Overlay>) { [line 31]

### function SheetContent({
  className,
  children,
  side = "right",
  ...props
}: React.ComponentProps<typeof SheetPrimitive.Content> & {
  side?: "top" | "right" | "bottom" | "left"
}) { [line 47]

### function SheetHeader({ className, ...props }: React.ComponentProps<"div">) { [line 84]

### function SheetFooter({ className, ...props }: React.ComponentProps<"div">) { [line 94]

### function SheetTitle({
  className,
  ...props
}: React.ComponentProps<typeof SheetPrimitive.Title>) { [line 104]

### function SheetDescription({
  className,
  ...props
}: React.ComponentProps<typeof SheetPrimitive.Description>) { [line 117]
- **Imports:** @/lib/utils, @radix-ui/react-dialog, lucide-react, react
**frontend/src/components/ui/sidebar.tsx**


### function useSidebar() { [line 45]

### function SidebarProvider({
  defaultOpen = true,
  open: openProp,
  onOpenChange: setOpenProp,
  className,
  style,
  children,
  ...props
}: React.ComponentProps<"div"> & {
  defaultOpen?: boolean
  open?: boolean
  onOpenChange?: (open: boolean) => void
}) { [line 54]

### () => {
    if (typeof document === "undefined") return defaultOpen

    const cookie = document.cookie
      .split("; ")
      .find((c) => c.startsWith(`${SIDEBAR_COOKIE_NAME}=`))

    if (!cookie) return defaultOpen

    return cookie.split("=")[1] === "true"
  } [line 70]

### (event: KeyboardEvent) => {
      if (
        event.key === SIDEBAR_KEYBOARD_SHORTCUT &&
        (event.metaKey || event.ctrlKey)
      ) {
        event.preventDefault()
        toggleSidebar()
      }
    } [line 108]

### function Sidebar({
  side = "left",
  variant = "sidebar",
  collapsible = "offcanvas",
  className,
  children,
  ...props
}: React.ComponentProps<"div"> & {
  side?: "left" | "right"
  variant?: "sidebar" | "floating" | "inset"
  collapsible?: "offcanvas" | "icon" | "none"
}) { [line 164]

### function SidebarTrigger({
  className,
  onClick,
  ...props
}: React.ComponentProps<typeof Button>) { [line 266]

### function SidebarRail({ className, ...props }: React.ComponentProps<"button">) { [line 293]

### function SidebarInset({ className, ...props }: React.ComponentProps<"main">) { [line 318]

### function SidebarInput({
  className,
  ...props
}: React.ComponentProps<typeof Input>) { [line 332]

### function SidebarHeader({ className, ...props }: React.ComponentProps<"div">) { [line 346]

### function SidebarFooter({ className, ...props }: React.ComponentProps<"div">) { [line 357]

### function SidebarSeparator({
  className,
  ...props
}: React.ComponentProps<typeof Separator>) { [line 368]

### function SidebarContent({ className, ...props }: React.ComponentProps<"div">) { [line 382]

### function SidebarGroup({ className, ...props }: React.ComponentProps<"div">) { [line 396]

### function SidebarGroupLabel({
  className,
  asChild = false,
  ...props
}: React.ComponentProps<"div"> & { asChild?: boolean }) { [line 407]

### function SidebarGroupAction({
  className,
  asChild = false,
  ...props
}: React.ComponentProps<"button"> & { asChild?: boolean }) { [line 428]

### function SidebarGroupContent({
  className,
  ...props
}: React.ComponentProps<"div">) { [line 451]

### function SidebarMenu({ className, ...props }: React.ComponentProps<"ul">) { [line 465]

### function SidebarMenuItem({ className, ...props }: React.ComponentProps<"li">) { [line 476]

### function SidebarMenuButton({
  asChild = false,
  isActive = false,
  variant = "default",
  size = "default",
  tooltip,
  className,
  ...props
}: React.ComponentProps<"button"> & {
  asChild?: boolean
  isActive?: boolean
  tooltip?: string | React.ComponentProps<typeof TooltipContent>
} & VariantProps<typeof sidebarMenuButtonVariants>) { [line 509]

### function SidebarMenuAction({
  className,
  asChild = false,
  showOnHover = false,
  ...props
}: React.ComponentProps<"button"> & {
  asChild?: boolean
  showOnHover?: boolean
}) { [line 559]

### function SidebarMenuBadge({
  className,
  ...props
}: React.ComponentProps<"div">) { [line 591]

### function SidebarMenuSkeleton({
  className,
  showIcon = false,
  ...props
}: React.ComponentProps<"div"> & {
  showIcon?: boolean
}) { [line 613]

### function SidebarMenuSub({ className, ...props }: React.ComponentProps<"ul">) { [line 651]

### function SidebarMenuSubItem({
  className,
  ...props
}: React.ComponentProps<"li">) { [line 666]

### function SidebarMenuSubButton({
  asChild = false,
  size = "md",
  isActive = false,
  className,
  ...props
}: React.ComponentProps<"a"> & {
  asChild?: boolean
  size?: "sm" | "md"
  isActive?: boolean
}) { [line 680]
- **Imports:** 12 external dependencies
**frontend/src/components/ui/skeleton.tsx**


### function Skeleton({ className, ...props }: React.ComponentProps<"div">) { [line 3]
- **Imports:** @/lib/utils
**frontend/src/components/ui/sonner.tsx**


### ({ ...props }: ToasterProps) => {
  const { theme = "system" } = useTheme()

  return (
    <Sonner
      theme={theme as ToasterProps["theme"]}
      className="toaster group"
      icons={{
        success: <CircleCheckIcon className="size-4" />,
        info: <InfoIcon className="size-4" />,
        warning: <TriangleAlertIcon className="size-4" />,
        error: <OctagonXIcon className="size-4" />,
        loading: <Loader2Icon className="size-4 animate-spin" />,
      }}
      style={
        {
          "--normal-bg": "var(--popover)",
          "--normal-text": "var(--popover-foreground)",
          "--normal-border": "var(--border)",
          "--border-radius": "var(--radius)",
        } as React.CSSProperties
      }
      {...props}
    />
  )
} [line 13]
- **Imports:** lucide-react, next-themes, sonner
**frontend/src/components/ui/table.tsx**


### function Table({ className, ...props }: React.ComponentProps<"table">) { [line 5]

### function TableHeader({ className, ...props }: React.ComponentProps<"thead">) { [line 20]

### function TableBody({ className, ...props }: React.ComponentProps<"tbody">) { [line 30]

### function TableFooter({ className, ...props }: React.ComponentProps<"tfoot">) { [line 40]

### function TableRow({ className, ...props }: React.ComponentProps<"tr">) { [line 53]

### function TableHead({ className, ...props }: React.ComponentProps<"th">) { [line 66]

### function TableCell({ className, ...props }: React.ComponentProps<"td">) { [line 79]

### function TableCaption({
  className,
  ...props
}: React.ComponentProps<"caption">) { [line 92]
- **Imports:** @/lib/utils, react
**frontend/src/components/ui/tabs.tsx**


### function Tabs({
  className,
  ...props
}: React.ComponentProps<typeof TabsPrimitive.Root>) { [line 6]

### function TabsList({
  className,
  ...props
}: React.ComponentProps<typeof TabsPrimitive.List>) { [line 19]

### function TabsTrigger({
  className,
  ...props
}: React.ComponentProps<typeof TabsPrimitive.Trigger>) { [line 35]

### function TabsContent({
  className,
  ...props
}: React.ComponentProps<typeof TabsPrimitive.Content>) { [line 51]
- **Imports:** @/lib/utils, @radix-ui/react-tabs, react
**frontend/src/components/ui/tooltip.tsx**


### function TooltipProvider({
  delayDuration = 0,
  ...props
}: React.ComponentProps<typeof TooltipPrimitive.Provider>) { [line 6]

### function Tooltip({
  ...props
}: React.ComponentProps<typeof TooltipPrimitive.Root>) { [line 19]

### function TooltipTrigger({
  ...props
}: React.ComponentProps<typeof TooltipPrimitive.Trigger>) { [line 29]

### function TooltipContent({
  className,
  sideOffset = 0,
  children,
  ...props
}: React.ComponentProps<typeof TooltipPrimitive.Content>) { [line 35]
- **Imports:** @/lib/utils, @radix-ui/react-tooltip, react

## frontend/src/hooks

**frontend/src/hooks/useAuth.ts** — Authentication hook — login, signup, logout, and current user state.

- **Relationships:** Consumes: client/LoginService, client/UsersService
Produces: Auth state and mutations (consumed by routes and components)

### () => {
  return localStorage.getItem("access_token") !== null
} [line 37] — Check if user is authenticated by verifying access_token in localStorage.

### () => {
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
} [line 54] — Provide authentication state and actions (login, logout, signup)
- **Relationships:** Consumes: LoginService, UsersService, localStorage token
Produces: Auth state, user data, login/logout/signup actions
- **Imports:** ./useCustomToast, @/client, @/utils, @tanstack/react-query, @tanstack/react-router
**frontend/src/hooks/useCopyToClipboard.ts** — Clipboard hook — copy text to clipboard with state tracking.


### function useCopyToClipboard(): [CopiedValue, CopyFn] { [line 26] — Copy text to clipboard and track copied state
- **Relationships:** Consumes: navigator.clipboard API
Produces: Clipboard write + copied state
- **Imports:** react
**frontend/src/hooks/useCustomToast.ts** — Toast notification hook — success and error toast helpers.


### () => {
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
} [line 19] — Provide convenience wrappers for success and error toast notifications
- **Relationships:** Consumes: sonner toast API
Produces: Toast notifications (used by mutations and form handlers)
- **Imports:** sonner
**frontend/src/hooks/useMobile.ts** — Mobile detection hook — responsive breakpoint observer.


### function useIsMobile() { [line 21] — Detect if viewport is below mobile breakpoint (768px)
- **Relationships:** Consumes: window.matchMedia API
Produces: Reactive mobile state (used by layout/sidebar components)
- **Imports:** react

## frontend/src/lib

**frontend/src/lib/utils.ts** — Tailwind CSS utility — className merger with clsx + tailwind-merge.


### function cn(...inputs: ClassValue[]) { [line 19] — Merge CSS class names with Tailwind conflict resolution
- **Relationships:** Consumes: clsx (conditional classes), tailwind-merge (conflict resolution)
Produces: Merged className string (used by all UI components)
- **Imports:** clsx, tailwind-merge

## frontend/src/routes

**frontend/src/routes/__root.tsx** — Root route — top-level layout with devtools and error boundaries.

- **Imports:** @/components/Common/ErrorComponent, @/components/Common/NotFound, @tanstack/react-query-devtools, @tanstack/react-router, @tanstack/react-router-devtools
**frontend/src/routes/_layout.tsx** — Authenticated layout route — sidebar + header + footer wrapper with auth guard.

- **Relationships:** Consumes: hooks/useAuth.isLoggedIn, Sidebar/AppSidebar, Common/Footer
Produces: Layout shell (wraps all /_layout/* child routes)

### function Layout() { [line 46]
- **Imports:** @/components/Common/Footer, @/components/Sidebar/AppSidebar, @/components/ui/sidebar, @/hooks/useAuth, @tanstack/react-router
**frontend/src/routes/login.tsx** — Login route — email/password authentication page.


### function Login() { [line 79] — Login page with email/password authentication
- **Relationships:** Consumes: useAuth.loginMutation
Produces: Auth token stored in localStorage, redirect to /
- **Flow:** 1. Render login form with email + password fields
2. Validate via Zod schema on blur
3. Call loginMutation on submit
4. Redirect to home on success

### (data: FormData) => {
    if (loginMutation.isPending) return
    loginMutation.mutate(data)
  } [line 91]
- **Imports:** 11 external dependencies
**frontend/src/routes/recover-password.tsx** — Recover password route — sends password recovery email.


### function RecoverPassword() { [line 76] — Password recovery page — sends reset email to user
- **Relationships:** Consumes: LoginService.recoverPassword API
Produces: Recovery email sent, success toast notification
- **Flow:** 1. Render email input form
2. Validate email via Zod
3. Call recoverPassword API
4. Show success toast, reset form

### async (data: FormData) => {
    await LoginService.recoverPassword({
      email: data.email,
    })
  } [line 85]

### async (data: FormData) => {
    if (mutation.isPending) return
    mutation.mutate(data)
  } [line 100]
- **Imports:** 13 external dependencies
**frontend/src/routes/reset-password.tsx** — Reset password route — sets new password using token from recovery email.


### function ResetPassword() { [line 99] — Reset password page — sets new password using token from recovery email
- **Relationships:** Consumes: LoginService.resetPassword API, URL search param token
Produces: Password updated, redirect to /login on success
- **Flow:** 1. Extract token from URL search params
2. Render new password + confirm password form
3. Validate via Zod (including match check)
4. Call resetPassword API with token + new password
5. Show success toast, redirect to /login

### (data: FormData) => {
    mutation.mutate({ new_password: data.new_password, token })
  } [line 125]
- **Imports:** 13 external dependencies
**frontend/src/routes/signup.tsx** — Signup route — new user registration page.


### function SignUp() { [line 88] — Registration page with email, name, password, and confirmation
- **Relationships:** Consumes: useAuth.signUpMutation
Produces: New user account, redirect to /login on success
- **Flow:** 1. Render signup form with 4 fields
2. Validate via Zod schema (including password match)
3. Strip confirm_password, call signUpMutation
4. Redirect to /login on success

### (data: FormData) => {
    if (signUpMutation.isPending) return

    // exclude confirm_password from submission data
    const { confirm_password: _confirm_password, ...submitData } = data
    signUpMutation.mutate(submitData)
  } [line 102]
- **Imports:** @/components/Common/AuthLayout, @/components/ui/form, @/components/ui/input, @/components/ui/loading-button, @/components/ui/password-input, @/hooks/useAuth, @hookform/resolvers/zod, @tanstack/react-router, react-hook-form, zod

## frontend/src/routes/_layout

**frontend/src/routes/_layout/admin.tsx** — Admin route — superuser-only user management page.


### function getUsersQueryOptions() { [line 18] — TanStack Query options for fetching all users (up to 100).

### function UsersTableContent() { [line 48] — Fetches users via suspense query and renders DataTable with current-user flag.

### function UsersTable() { [line 61] — Suspense wrapper for UsersTableContent with PendingUsers fallback.

### function Admin() { [line 79] — Admin page for managing user accounts (superuser only)
- **Relationships:** Consumes: UsersService.readUsers, useAuth.user, Admin/AddUser, Admin/columns
Produces: User management table with add-user action
- **Imports:** @/client, @/components/Admin/AddUser, @/components/Admin/columns, @/components/Common/DataTable, @/components/Pending/PendingUsers, @/hooks/useAuth, @tanstack/react-query, @tanstack/react-router, react
**frontend/src/routes/_layout/index.tsx** — Dashboard route — authenticated home page with user greeting and time summary.


### function Dashboard() { [line 35] — Dashboard home page displaying welcome greeting and time tracking summary.
- **Relationships:** Consumes: useAuth.user, TimeSummaryWidget
Produces: Greeting UI + time summary widget
- **Imports:** @/components/Dashboard/TimeSummaryWidget, @/hooks/useAuth, @tanstack/react-router
**frontend/src/routes/_layout/items.tsx** — Items route — CRUD listing page for user items.


### function getItemsQueryOptions() { [line 18] — TanStack Query options for fetching all items (up to 100).

### function ItemsTableContent() { [line 40] — Fetches items via suspense query; shows empty state or DataTable.

### function ItemsTable() { [line 59] — Suspense wrapper for ItemsTableContent with PendingItems fallback.

### function Items() { [line 77] — Items listing page with data table and add-item action
- **Relationships:** Consumes: ItemsService.readItems, Items/AddItem, Items/columns
Produces: Items data table with empty state and add-item button
- **Imports:** @/client, @/components/Common/DataTable, @/components/Items/AddItem, @/components/Items/columns, @/components/Pending/PendingItems, @tanstack/react-query, @tanstack/react-router, lucide-react, react
**frontend/src/routes/_layout/projects.tsx** — Display paginated projects table with add, edit, and delete actions.

- **Relationships:** Consumes: ProjectsService.readProjects, Projects/AddProject, Projects/columns
Produces: Projects data table with empty state and add-project button

### function getProjectsQueryOptions() { [line 24] — TanStack Query options for fetching all projects (up to 100).

### function ProjectsTableContent() { [line 46] — Fetches projects via suspense query; shows empty state or DataTable.

### function ProjectsTable() { [line 67] — Suspense wrapper for ProjectsTableContent with PendingProjects fallback.

### function Projects() { [line 85] — Projects listing page with data table and add-project action.
- **Relationships:** Consumes: ProjectsService.readProjects, Projects/AddProject, Projects/columns
Produces: Projects data table with empty state and add-project button
- **Imports:** @/client, @/components/Common/DataTable, @/components/Projects/AddProject, @/components/Projects/PendingProjects, @/components/Projects/columns, @tanstack/react-query, @tanstack/react-router, lucide-react, react
**frontend/src/routes/_layout/settings.tsx** — Settings route — user profile, password, and account management.


### function UserSettings() { [line 46] — User settings page with tabbed sections for profile, password, and account deletion
- **Relationships:** Consumes: useAuth.user, UserSettings/UserInformation, UserSettings/ChangePassword, UserSettings/DeleteAccount
Produces: Tabbed settings UI (superusers see all tabs; non-superusers see all 3 tabs)
- **Imports:** @/components/UserSettings/ChangePassword, @/components/UserSettings/DeleteAccount, @/components/UserSettings/UserInformation, @/components/ui/tabs, @/hooks/useAuth, @tanstack/react-router
**frontend/src/routes/_layout/time-entries.tsx** — Display paginated time entries table with add, edit, and delete actions.

- **Relationships:** Consumes: TimeEntriesService.readTimeEntries, TimeEntries/AddTimeEntry, TimeEntries/columns
Produces: Time entries data table with empty state and add-time-entry button

### function getTimeEntriesQueryOptions() { [line 24] — TanStack Query options for fetching all time entries (up to 100).

### function TimeEntriesTableContent() { [line 46] — Fetches time entries via suspense query; shows empty state or DataTable.

### function TimeEntriesTable() { [line 67] — Suspense wrapper for TimeEntriesTableContent with PendingTimeEntries fallback.

### function TimeEntries() { [line 85] — Time entries listing page with data table and add-time-entry action.
- **Relationships:** Consumes: TimeEntriesService.readTimeEntries, TimeEntries/AddTimeEntry, TimeEntries/columns
Produces: Time entries data table with empty state and add-time-entry button
- **Imports:** @/client, @/components/Common/DataTable, @/components/TimeEntries/AddTimeEntry, @/components/TimeEntries/PendingTimeEntries, @/components/TimeEntries/columns, @tanstack/react-query, @tanstack/react-router, lucide-react, react

## frontend/tests

**frontend/tests/auth.setup.ts**

- **Imports:** ./config.ts, @playwright/test
**frontend/tests/config.ts**


### function getEnvVar(name: string): string { [line 10]
- **Imports:** dotenv, node:path, node:url

## frontend/tests/utils

**frontend/tests/utils/mailcatcher.ts**


### async function findEmail({
  request,
  filter,
}: {
  request: APIRequestContext
  filter?: (email: Email) => boolean
}) { [line 9]

### function findLastEmail({
  request,
  filter,
  timeout = 5000,
}: {
  request: APIRequestContext
  filter?: (email: Email) => boolean
  timeout?: number
}) { [line 33]
- **Imports:** @playwright/test
**frontend/tests/utils/privateApi.ts**


### async ({
  email,
  password,
}: {
  email: string
  password: string
}) => {
  return await PrivateService.createUser({
    requestBody: {
      email,
      password,
      is_verified: true,
      full_name: "Test User",
    },
  })
} [line 7]
- **Imports:** ../../src/client
**frontend/tests/utils/random.ts**


### () =>
  `test_${Math.random().toString(36).substring(7)}@example.com` [line 1]

### () =>
  `Team ${Math.random().toString(36).substring(7)}` [line 4]

### () => `${Math.random().toString(36).substring(2)}` [line 7]

### (text: string) =>
  text
    .toLowerCase()
    .replace(/\s+/g, "-")
    .replace(/[^\w-]+/g, "") [line 9]

### () =>
  `Item ${Math.random().toString(36).substring(7)}` [line 15]

### () =>
  `Description ${Math.random().toString(36).substring(7)}` [line 18]
**frontend/tests/utils/user.ts**


### async function signUpNewUser(
  page: Page,
  name: string,
  email: string,
  password: string,
) { [line 3]

### async function logInUser(page: Page, email: string, password: string) { [line 19]

### async function logOutUser(page: Page) { [line 31]
- **Imports:** @playwright/test
