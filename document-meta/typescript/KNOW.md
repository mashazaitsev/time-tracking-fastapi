# Typescript Documentation

## Complete Metadata

```json
{
  "type": "typescript",
  "total_files": 89,
  "files": [
  {
    "dependencies": {
      "imports": [
        "@hey-api/openapi-ts"
      ]
    },
    "file": "openapi-ts.config.ts",
    "language": "typescript",
    "lines": 34,
    "path": "frontend/openapi-ts.config.ts",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@playwright/test",
        "dotenv/config"
      ]
    },
    "file": "playwright.config.ts",
    "language": "typescript",
    "lines": 92,
    "path": "frontend/playwright.config.ts",
    "type": "module"
  },
  {
    "classes": [
      {
        "line": 4,
        "methods": [
          "constructor: line 11"
        ],
        "name": "ApiError"
      }
    ],
    "dependencies": {
      "imports": [
        "./ApiRequestOptions",
        "./ApiResult"
      ]
    },
    "file": "ApiError.ts",
    "language": "typescript",
    "lines": 21,
    "path": "frontend/src/client/core/ApiError.ts",
    "type": "module"
  },
  {
    "file": "ApiRequestOptions.ts",
    "language": "typescript",
    "lines": 21,
    "path": "frontend/src/client/core/ApiRequestOptions.ts",
    "type": "module",
    "types": [
      {
        "definition": "type ApiRequestOptions<T = unknown> = {\n\treadonly body?: any;\n\treadonly cookies?: Record<string, unknown>;\n\treadonly errors?: Record<number | string, string>;\n\treadonly formData?: Record<string, unknown> | any[] | Blob | File;\n\treadonly headers?: Record<string, unknown>;\n\treadonly mediaType?: string;\n\treadonly method:\n\t\t| 'DELETE'\n\t\t| 'GET'\n\t\t| 'HEAD'\n\t\t| 'OPTIONS'\n\t\t| 'PATCH'\n\t\t| 'POST'\n\t\t| 'PUT';\n\treadonly path?: Record<string, unknown>;\n\treadonly query?: Record<string, unknown>;\n\treadonly responseHeader?: string;\n\treadonly responseTransformer?: (data: unknown) => Promise<T>;\n\treadonly url: string;\n};",
        "line": 1,
        "name": "ApiRequestOptions"
      }
    ]
  },
  {
    "file": "ApiResult.ts",
    "language": "typescript",
    "lines": 7,
    "path": "frontend/src/client/core/ApiResult.ts",
    "type": "module",
    "types": [
      {
        "definition": "type ApiResult<TData = any> = {\n\treadonly body: TData;\n\treadonly ok: boolean;\n\treadonly status: number;\n\treadonly statusText: string;\n\treadonly url: string;\n};",
        "line": 1,
        "name": "ApiResult"
      }
    ]
  },
  {
    "classes": [
      {
        "line": 1,
        "methods": [
          "constructor: line 2",
          "isCancelled: line 7"
        ],
        "name": "CancelError"
      },
      {
        "line": 20,
        "methods": [
          "constructor: line 29",
          "then: line 87",
          "catch: line 94",
          "finally: line 100",
          "cancel: line 104",
          "isCancelled: line 123"
        ],
        "name": "CancelablePromise"
      }
    ],
    "file": "CancelablePromise.ts",
    "interfaces": [
      {
        "line": 12,
        "name": "OnCancel"
      }
    ],
    "language": "typescript",
    "lines": 126,
    "path": "frontend/src/client/core/CancelablePromise.ts",
    "type": "module"
  },
  {
    "classes": [
      {
        "line": 8,
        "methods": [
          "constructor: line 11",
          "eject: line 15",
          "use: line 22"
        ],
        "name": "Interceptors"
      }
    ],
    "dependencies": {
      "imports": [
        "./ApiRequestOptions",
        "axios"
      ]
    },
    "file": "OpenAPI.ts",
    "language": "typescript",
    "lines": 57,
    "path": "frontend/src/client/core/OpenAPI.ts",
    "type": "module",
    "types": [
      {
        "definition": "type Headers = Record<string, string>;",
        "line": 4,
        "name": "Headers"
      },
      {
        "definition": "type Middleware<T> = (value: T) => T | Promise<T>;",
        "line": 5,
        "name": "Middleware"
      },
      {
        "definition": "type Resolver<T> = (options: ApiRequestOptions<T>) => Promise<T>;",
        "line": 6,
        "name": "Resolver"
      },
      {
        "definition": "type OpenAPIConfig = {\n\tBASE: string;\n\tCREDENTIALS: 'include' | 'omit' | 'same-origin';\n\tENCODE_PATH?: ((path: string) => string) | undefined;\n\tHEADERS?: Headers | Resolver<Headers> | undefined;\n\tPASSWORD?: string | Resolver<string> | undefined;\n\tTOKEN?: string | Resolver<string> | undefined;\n\tUSERNAME?: string | Resolver<string> | undefined;\n\tVERSION: string;\n\tWITH_CREDENTIALS: boolean;\n\tinterceptors: {\n\t\trequest: Interceptors<AxiosRequestConfig>;\n\t\tresponse: Interceptors<AxiosResponse>;\n\t};\n};",
        "line": 27,
        "name": "OpenAPIConfig"
      }
    ]
  },
  {
    "dependencies": {
      "imports": [
        "./ApiError",
        "./ApiRequestOptions",
        "./ApiResult",
        "./CancelablePromise",
        "./OpenAPI",
        "axios"
      ]
    },
    "file": "request.ts",
    "functions": [
      {
        "line": 11,
        "name": "isString",
        "parameters": [
          {
            "name": "value",
            "type": "unknown"
          }
        ],
        "signature": "(value: unknown): value is string => {\n\treturn typeof value === 'string';\n}"
      },
      {
        "line": 15,
        "name": "isStringWithValue",
        "parameters": [
          {
            "name": "value",
            "type": "unknown"
          }
        ],
        "signature": "(value: unknown): value is string => {\n\treturn isString(value) && value !== '';\n}"
      },
      {
        "line": 19,
        "name": "isBlob",
        "parameters": [
          {
            "name": "value",
            "type": "any"
          }
        ],
        "signature": "(value: any): value is Blob => {\n\treturn value instanceof Blob;\n}"
      },
      {
        "line": 23,
        "name": "isFormData",
        "parameters": [
          {
            "name": "value",
            "type": "unknown"
          }
        ],
        "signature": "(value: unknown): value is FormData => {\n\treturn value instanceof FormData;\n}"
      },
      {
        "line": 27,
        "name": "isSuccess",
        "parameters": [
          {
            "name": "status",
            "type": "number"
          }
        ],
        "signature": "(status: number): boolean => {\n\treturn status >= 200 && status < 300;\n}"
      },
      {
        "line": 31,
        "name": "base64",
        "parameters": [
          {
            "name": "str",
            "type": "string"
          }
        ],
        "signature": "(str: string): string => {\n\ttry {\n\t\treturn btoa(str);\n\t} catch (err) {\n\t\t// @ts-ignore\n\t\treturn Buffer.from(str).toString('base64');\n\t}\n}"
      },
      {
        "line": 40,
        "name": "getQueryString",
        "parameters": [
          {
            "name": "params",
            "type": "Record<string, unknown>"
          }
        ],
        "signature": "(params: Record<string, unknown>): string => {\n\tconst qs: string[] = [];\n\n\tconst append = (key: string, value: unknown) => {\n\t\tqs.push(`${encodeURIComponent(key)}=${encodeURIComponent(String(value))}`);\n\t};\n\n\tconst encodePair = (key: string, value: unknown) => {\n\t\tif (value === undefined || value === null) {\n\t\t\treturn;\n\t\t}\n\n\t\tif (value instanceof Date) {\n\t\t\tappend(key, value.toISOString());\n\t\t} else if (Array.isArray(value)) {\n\t\t\tvalue.forEach(v => encodePair(key, v));\n\t\t} else if (typeof value === 'object') {\n\t\t\tObject.entries(value).forEach(([k, v]) => encodePair(`${key}[${k}]`, v));\n\t\t} else {\n\t\t\tappend(key, value);\n\t\t}\n\t};\n\n\tObject.entries(params).forEach(([key, value]) => encodePair(key, value));\n\n\treturn qs.length ? `?${qs.join('&')}` : '';\n}"
      },
      {
        "line": 68,
        "name": "getUrl",
        "parameters": [
          {
            "name": "config",
            "type": "OpenAPIConfig"
          },
          {
            "name": "options",
            "type": "ApiRequestOptions"
          }
        ],
        "signature": "(config: OpenAPIConfig, options: ApiRequestOptions): string => {\n\tconst encoder = config.ENCODE_PATH || encodeURI;\n\n\tconst path = options.url\n\t\t.replace('{api-version}', config.VERSION)\n\t\t.replace(/{(.*?)}/g, (substring: string, group: string) => {\n\t\t\tif (options.path?.hasOwnProperty(group)) {\n\t\t\t\treturn encoder(String(options.path[group]));\n\t\t\t}\n\t\t\treturn substring;\n\t\t});\n\n\tconst url = config.BASE + path;\n\treturn options.query ? url + getQueryString(options.query) : url;\n}"
      },
      {
        "line": 84,
        "name": "getFormData",
        "parameters": [
          {
            "name": "options",
            "type": "ApiRequestOptions"
          }
        ],
        "signature": "(options: ApiRequestOptions): FormData | undefined => {\n\tif (options.formData) {\n\t\tconst formData = new FormData();\n\n\t\tconst process = (key: string, value: unknown) => {\n\t\t\tif (isString(value) || isBlob(value)) {\n\t\t\t\tformData.append(key, value);\n\t\t\t} else {\n\t\t\t\tformData.append(key, JSON.stringify(value));\n\t\t\t}\n\t\t};\n\n\t\tObject.entries(options.formData)\n\t\t\t.filter(([, value]) => value !== undefined && value !== null)\n\t\t\t.forEach(([key, value]) => {\n\t\t\t\tif (Array.isArray(value)) {\n\t\t\t\t\tvalue.forEach(v => process(key, v));\n\t\t\t\t} else {\n\t\t\t\t\tprocess(key, value);\n\t\t\t\t}\n\t\t\t});\n\n\t\treturn formData;\n\t}\n\treturn undefined;\n}"
      },
      {
        "line": 113,
        "name": "resolve",
        "parameters": [
          {
            "name": "options",
            "type": "ApiRequestOptions<T>"
          },
          {
            "name": "resolver",
            "type": "T | Resolver<T>"
          }
        ],
        "signature": "async <T>(options: ApiRequestOptions<T>, resolver?: T | Resolver<T>): Promise<T | undefined> => {\n\tif (typeof resolver === 'function') {\n\t\treturn (resolver as Resolver<T>)(options);\n\t}\n\treturn resolver;\n}"
      },
      {
        "line": 120,
        "name": "getHeaders",
        "parameters": [
          {
            "name": "config",
            "type": "OpenAPIConfig"
          },
          {
            "name": "options",
            "type": "ApiRequestOptions<T>"
          }
        ],
        "signature": "async <T>(config: OpenAPIConfig, options: ApiRequestOptions<T>): Promise<Record<string, string>> => {\n\tconst [token, username, password, additionalHeaders] = await Promise.all([\n\t\t// @ts-ignore\n\t\tresolve(options, config.TOKEN),\n\t\t// @ts-ignore\n\t\tresolve(options, config.USERNAME),\n\t\t// @ts-ignore\n\t\tresolve(options, config.PASSWORD),\n\t\t// @ts-ignore\n\t\tresolve(options, config.HEADERS),\n\t]);\n\n\tconst headers = Object.entries({\n\t\tAccept: 'application/json',\n\t\t...additionalHeaders,\n\t\t...options.headers,\n\t})\n\t.filter(([, value]) => value !== undefined && value !== null)\n\t.reduce((headers, [key, value]) => ({\n\t\t...headers,\n\t\t[key]: String(value),\n\t}), {} as Record<string, string>);\n\n\tif (isStringWithValue(token)) {\n\t\theaders['Authorization'] = `Bearer ${token}`;\n\t}\n\n\tif (isStringWithValue(username) && isStringWithValue(password)) {\n\t\tconst credentials = base64(`${username}:${password}`);\n\t\theaders['Authorization'] = `Basic ${credentials}`;\n\t}\n\n\tif (options.body !== undefined) {\n\t\tif (options.mediaType) {\n\t\t\theaders['Content-Type'] = options.mediaType;\n\t\t} else if (isBlob(options.body)) {\n\t\t\theaders['Content-Type'] = options.body.type || 'application/octet-stream';\n\t\t} else if (isString(options.body)) {\n\t\t\theaders['Content-Type'] = 'text/plain';\n\t\t} else if (!isFormData(options.body)) {\n\t\t\theaders['Content-Type'] = 'application/json';\n\t\t}\n\t} else if (options.formData !== undefined) {\n\t\tif (options.mediaType) {\n\t\t\theaders['Content-Type'] = options.mediaType;\n\t\t}\n\t}\n\n\treturn headers;\n}"
      },
      {
        "line": 171,
        "name": "getRequestBody",
        "parameters": [
          {
            "name": "options",
            "type": "ApiRequestOptions"
          }
        ],
        "signature": "(options: ApiRequestOptions): unknown => {\n\tif (options.body) {\n\t\treturn options.body;\n\t}\n\treturn undefined;\n}"
      },
      {
        "line": 178,
        "name": "sendRequest",
        "parameters": [
          {
            "name": "config",
            "type": "OpenAPIConfig"
          },
          {
            "name": "options",
            "type": "ApiRequestOptions<T>"
          },
          {
            "name": "url",
            "type": "string"
          },
          {
            "name": "body",
            "type": "unknown"
          },
          {
            "name": "formData",
            "type": "FormData | undefined"
          },
          {
            "name": "headers",
            "type": "Record<string, string>"
          },
          {
            "name": "onCancel",
            "type": "OnCancel"
          },
          {
            "name": "axiosClient",
            "type": "AxiosInstance"
          }
        ],
        "signature": "async <T>(\n\tconfig: OpenAPIConfig,\n\toptions: ApiRequestOptions<T>,\n\turl: string,\n\tbody: unknown,\n\tformData: FormData | undefined,\n\theaders: Record<string, string>,\n\tonCancel: OnCancel,\n\taxiosClient: AxiosInstance\n): Promise<AxiosResponse<T>> => {\n\tconst controller = new AbortController();\n\n\tlet requestConfig: AxiosRequestConfig = {\n\t\tdata: body ?? formData,\n\t\theaders,\n\t\tmethod: options.method,\n\t\tsignal: controller.signal,\n\t\turl,\n\t\twithCredentials: config.WITH_CREDENTIALS,\n\t};\n\n\tonCancel(() => controller.abort());\n\n\tfor (const fn of config.interceptors.request._fns) {\n\t\trequestConfig = await fn(requestConfig);\n\t}\n\n\ttry {\n\t\treturn await axiosClient.request(requestConfig);\n\t} catch (error) {\n\t\tconst axiosError = error as AxiosError<T>;\n\t\tif (axiosError.response) {\n\t\t\treturn axiosError.response;\n\t\t}\n\t\tthrow error;\n\t}\n}"
      },
      {
        "line": 216,
        "name": "getResponseHeader",
        "parameters": [
          {
            "name": "response",
            "type": "AxiosResponse<unknown>"
          },
          {
            "name": "responseHeader",
            "type": "string"
          }
        ],
        "signature": "(response: AxiosResponse<unknown>, responseHeader?: string): string | undefined => {\n\tif (responseHeader) {\n\t\tconst content = response.headers[responseHeader];\n\t\tif (isString(content)) {\n\t\t\treturn content;\n\t\t}\n\t}\n\treturn undefined;\n}"
      },
      {
        "line": 226,
        "name": "getResponseBody",
        "parameters": [
          {
            "name": "response",
            "type": "AxiosResponse<unknown>"
          }
        ],
        "signature": "(response: AxiosResponse<unknown>): unknown => {\n\tif (response.status !== 204) {\n\t\treturn response.data;\n\t}\n\treturn undefined;\n}"
      },
      {
        "line": 233,
        "name": "catchErrorCodes",
        "parameters": [
          {
            "name": "options",
            "type": "ApiRequestOptions"
          },
          {
            "name": "result",
            "type": "ApiResult"
          }
        ],
        "signature": "(options: ApiRequestOptions, result: ApiResult): void => {\n\tconst errors: Record<number, string> = {\n\t\t400: 'Bad Request',\n\t\t401: 'Unauthorized',\n\t\t402: 'Payment Required',\n\t\t403: 'Forbidden',\n\t\t404: 'Not Found',\n\t\t405: 'Method Not Allowed',\n\t\t406: 'Not Acceptable',\n\t\t407: 'Proxy Authentication Required',\n\t\t408: 'Request Timeout',\n\t\t409: 'Conflict',\n\t\t410: 'Gone',\n\t\t411: 'Length Required',\n\t\t412: 'Precondition Failed',\n\t\t413: 'Payload Too Large',\n\t\t414: 'URI Too Long',\n\t\t415: 'Unsupported Media Type',\n\t\t416: 'Range Not Satisfiable',\n\t\t417: 'Expectation Failed',\n\t\t418: 'Im a teapot',\n\t\t421: 'Misdirected Request',\n\t\t422: 'Unprocessable Content',\n\t\t423: 'Locked',\n\t\t424: 'Failed Dependency',\n\t\t425: 'Too Early',\n\t\t426: 'Upgrade Required',\n\t\t428: 'Precondition Required',\n\t\t429: 'Too Many Requests',\n\t\t431: 'Request Header Fields Too Large',\n\t\t451: 'Unavailable For Legal Reasons',\n\t\t500: 'Internal Server Error',\n\t\t501: 'Not Implemented',\n\t\t502: 'Bad Gateway',\n\t\t503: 'Service Unavailable',\n\t\t504: 'Gateway Timeout',\n\t\t505: 'HTTP Version Not Supported',\n\t\t506: 'Variant Also Negotiates',\n\t\t507: 'Insufficient Storage',\n\t\t508: 'Loop Detected',\n\t\t510: 'Not Extended',\n\t\t511: 'Network Authentication Required',\n\t\t...options.errors,\n\t}\n\n\tconst error = errors[result.status];\n\tif (error) {\n\t\tthrow new ApiError(options, result, error);\n\t}\n\n\tif (!result.ok) {\n\t\tconst errorStatus = result.status ?? 'unknown';\n\t\tconst errorStatusText = result.statusText ?? 'unknown';\n\t\tconst errorBody = (() => {\n\t\t\ttry {\n\t\t\t\treturn JSON.stringify(result.body, null, 2);\n\t\t\t} catch (e) {\n\t\t\t\treturn undefined;\n\t\t\t}\n\t\t})();\n\n\t\tthrow new ApiError(options, result,\n\t\t\t`Generic Error: status: ${errorStatus}; status text: ${errorStatusText}; body: ${errorBody}`\n\t\t);\n\t}\n}"
      },
      {
        "line": 308,
        "name": "request",
        "parameters": "axiosClient The axios client instance to use",
        "purpose": "Request method",
        "raises": "ApiError",
        "returns": "CancelablePromise<T>",
        "signature": "<T>(config: OpenAPIConfig, options: ApiRequestOptions<T>, axiosClient: AxiosInstance = axios): CancelablePromise<T> => {\n\treturn new CancelablePromise(async (resolve, reject, onCancel) => {\n\t\ttry {\n\t\t\tconst url = getUrl(config, options);\n\t\t\tconst formData = getFormData(options);\n\t\t\tconst body = getRequestBody(options);\n\t\t\tconst headers = await getHeaders(config, options);\n\n\t\t\tif (!onCancel.isCancelled) {\n\t\t\t\tlet response = await sendRequest<T>(config, options, url, body, formData, headers, onCancel, axiosClient);\n\n\t\t\t\tfor (const fn of config.interceptors.response._fns) {\n\t\t\t\t\tresponse = await fn(response);\n\t\t\t\t}\n\n\t\t\t\tconst responseBody = getResponseBody(response);\n\t\t\t\tconst responseHeader = getResponseHeader(response, options.responseHeader);\n\n\t\t\t\tlet transformedBody = responseBody;\n\t\t\t\tif (options.responseTransformer && isSuccess(response.status)) {\n\t\t\t\t\ttransformedBody = await options.responseTransformer(responseBody)\n\t\t\t\t}\n\n\t\t\t\tconst result: ApiResult = {\n\t\t\t\t\turl,\n\t\t\t\t\tok: isSuccess(response.status),\n\t\t\t\t\tstatus: response.status,\n\t\t\t\t\tstatusText: response.statusText,\n\t\t\t\t\tbody: responseHeader ?? transformedBody,\n\t\t\t\t};\n\n\t\t\t\tcatchErrorCodes(options, result);\n\n\t\t\t\tresolve(result.body);\n\t\t\t}\n\t\t} catch (error) {\n\t\t\treject(error);\n\t\t}\n\t});\n}"
      }
    ],
    "language": "typescript",
    "lines": 347,
    "path": "frontend/src/client/core/request.ts",
    "type": "module",
    "types": [
      {
        "definition": "type Resolver<T> = (options: ApiRequestOptions<T>) => Promise<T>;",
        "line": 111,
        "name": "Resolver"
      }
    ]
  },
  {
    "file": "index.ts",
    "language": "typescript",
    "lines": 6,
    "path": "frontend/src/client/index.ts",
    "type": "module"
  },
  {
    "file": "schemas.gen.ts",
    "language": "typescript",
    "lines": 559,
    "path": "frontend/src/client/schemas.gen.ts",
    "type": "module"
  },
  {
    "classes": [
      {
        "line": 8,
        "methods": [
          "readItems: line 18",
          "createItem: line 40",
          "readItem: line 60",
          "updateItem: line 82",
          "deleteItem: line 105"
        ],
        "name": "ItemsService"
      },
      {
        "line": 119,
        "methods": [
          "loginAccessToken: line 128",
          "testToken: line 146",
          "recoverPassword: line 161",
          "resetPassword: line 182",
          "recoverPasswordHtmlContent: line 202"
        ],
        "name": "LoginService"
      },
      {
        "line": 216,
        "methods": [
          "createUser: line 225"
        ],
        "name": "PrivateService"
      },
      {
        "line": 238,
        "methods": [
          "readUsers: line 248",
          "createUser: line 270",
          "readUserMe: line 288",
          "deleteUserMe: line 301",
          "updateUserMe: line 316",
          "updatePasswordMe: line 336",
          "registerUser: line 356",
          "readUserById: line 376",
          "updateUser: line 398",
          "deleteUser: line 421"
        ],
        "name": "UsersService"
      },
      {
        "line": 435,
        "methods": [
          "testEmail: line 444",
          "healthCheck: line 462"
        ],
        "name": "UtilsService"
      }
    ],
    "dependencies": {
      "imports": [
        "./core/CancelablePromise",
        "./core/OpenAPI",
        "./core/request",
        "./types.gen"
      ]
    },
    "file": "sdk.gen.ts",
    "language": "typescript",
    "lines": 468,
    "path": "frontend/src/client/sdk.gen.ts",
    "type": "module"
  },
  {
    "file": "types.gen.ts",
    "language": "typescript",
    "lines": 240,
    "path": "frontend/src/client/types.gen.ts",
    "type": "module",
    "types": [
      {
        "definition": "type Body_login_login_access_token = {\n    grant_type?: (string | null);\n    username: string;\n    password: string;\n    scope?: string;\n    client_id?: (string | null);\n    client_secret?: (string | null);\n};",
        "line": 3,
        "name": "Body_login_login_access_token"
      },
      {
        "definition": "type HTTPValidationError = {\n    detail?: Array<ValidationError>;\n};",
        "line": 12,
        "name": "HTTPValidationError"
      },
      {
        "definition": "type ItemCreate = {\n    title: string;\n    description?: (string | null);\n};",
        "line": 16,
        "name": "ItemCreate"
      },
      {
        "definition": "type ItemPublic = {\n    title: string;\n    description?: (string | null);\n    id: string;\n    owner_id: string;\n    created_at?: (string | null);\n};",
        "line": 21,
        "name": "ItemPublic"
      },
      {
        "definition": "type ItemsPublic = {\n    data: Array<ItemPublic>;\n    count: number;\n};",
        "line": 29,
        "name": "ItemsPublic"
      },
      {
        "definition": "type ItemUpdate = {\n    title?: (string | null);\n    description?: (string | null);\n};",
        "line": 34,
        "name": "ItemUpdate"
      },
      {
        "definition": "type Message = {\n    message: string;\n};",
        "line": 39,
        "name": "Message"
      },
      {
        "definition": "type NewPassword = {\n    token: string;\n    new_password: string;\n};",
        "line": 43,
        "name": "NewPassword"
      },
      {
        "definition": "type PrivateUserCreate = {\n    email: string;\n    password: string;\n    full_name: string;\n    is_verified?: boolean;\n};",
        "line": 48,
        "name": "PrivateUserCreate"
      },
      {
        "definition": "type Token = {\n    access_token: string;\n    token_type?: string;\n};",
        "line": 55,
        "name": "Token"
      },
      {
        "definition": "type UpdatePassword = {\n    current_password: string;\n    new_password: string;\n};",
        "line": 60,
        "name": "UpdatePassword"
      },
      {
        "definition": "type UserCreate = {\n    email: string;\n    is_active?: boolean;\n    is_superuser?: boolean;\n    full_name?: (string | null);\n    password: string;\n};",
        "line": 65,
        "name": "UserCreate"
      },
      {
        "definition": "type UserPublic = {\n    email: string;\n    is_active?: boolean;\n    is_superuser?: boolean;\n    full_name?: (string | null);\n    id: string;\n    created_at?: (string | null);\n};",
        "line": 73,
        "name": "UserPublic"
      },
      {
        "definition": "type UserRegister = {\n    email: string;\n    password: string;\n    full_name?: (string | null);\n};",
        "line": 82,
        "name": "UserRegister"
      },
      {
        "definition": "type UsersPublic = {\n    data: Array<UserPublic>;\n    count: number;\n};",
        "line": 88,
        "name": "UsersPublic"
      },
      {
        "definition": "type UserUpdate = {\n    email?: (string | null);\n    is_active?: boolean;\n    is_superuser?: boolean;\n    full_name?: (string | null);\n    password?: (string | null);\n};",
        "line": 93,
        "name": "UserUpdate"
      },
      {
        "definition": "type UserUpdateMe = {\n    full_name?: (string | null);\n    email?: (string | null);\n};",
        "line": 101,
        "name": "UserUpdateMe"
      },
      {
        "definition": "type ValidationError = {\n    loc: Array<(string | number)>;\n    msg: string;\n    type: string;\n    input?: unknown;\n    ctx?: {\n        [key: string]: unknown;\n    };\n};",
        "line": 106,
        "name": "ValidationError"
      },
      {
        "definition": "type ItemsReadItemsData = {\n    limit?: number;\n    skip?: number;\n};",
        "line": 116,
        "name": "ItemsReadItemsData"
      },
      {
        "definition": "type ItemsReadItemsResponse = (ItemsPublic);",
        "line": 121,
        "name": "ItemsReadItemsResponse"
      },
      {
        "definition": "type ItemsCreateItemData = {\n    requestBody: ItemCreate;\n};",
        "line": 123,
        "name": "ItemsCreateItemData"
      },
      {
        "definition": "type ItemsCreateItemResponse = (ItemPublic);",
        "line": 127,
        "name": "ItemsCreateItemResponse"
      },
      {
        "definition": "type ItemsReadItemData = {\n    id: string;\n};",
        "line": 129,
        "name": "ItemsReadItemData"
      },
      {
        "definition": "type ItemsReadItemResponse = (ItemPublic);",
        "line": 133,
        "name": "ItemsReadItemResponse"
      },
      {
        "definition": "type ItemsUpdateItemData = {\n    id: string;\n    requestBody: ItemUpdate;\n};",
        "line": 135,
        "name": "ItemsUpdateItemData"
      },
      {
        "definition": "type ItemsUpdateItemResponse = (ItemPublic);",
        "line": 140,
        "name": "ItemsUpdateItemResponse"
      },
      {
        "definition": "type ItemsDeleteItemData = {\n    id: string;\n};",
        "line": 142,
        "name": "ItemsDeleteItemData"
      },
      {
        "definition": "type ItemsDeleteItemResponse = (Message);",
        "line": 146,
        "name": "ItemsDeleteItemResponse"
      },
      {
        "definition": "type LoginLoginAccessTokenData = {\n    formData: Body_login_login_access_token;\n};",
        "line": 148,
        "name": "LoginLoginAccessTokenData"
      },
      {
        "definition": "type LoginLoginAccessTokenResponse = (Token);",
        "line": 152,
        "name": "LoginLoginAccessTokenResponse"
      },
      {
        "definition": "type LoginTestTokenResponse = (UserPublic);",
        "line": 154,
        "name": "LoginTestTokenResponse"
      },
      {
        "definition": "type LoginRecoverPasswordData = {\n    email: string;\n};",
        "line": 156,
        "name": "LoginRecoverPasswordData"
      },
      {
        "definition": "type LoginRecoverPasswordResponse = (Message);",
        "line": 160,
        "name": "LoginRecoverPasswordResponse"
      },
      {
        "definition": "type LoginResetPasswordData = {\n    requestBody: NewPassword;\n};",
        "line": 162,
        "name": "LoginResetPasswordData"
      },
      {
        "definition": "type LoginResetPasswordResponse = (Message);",
        "line": 166,
        "name": "LoginResetPasswordResponse"
      },
      {
        "definition": "type LoginRecoverPasswordHtmlContentData = {\n    email: string;\n};",
        "line": 168,
        "name": "LoginRecoverPasswordHtmlContentData"
      },
      {
        "definition": "type LoginRecoverPasswordHtmlContentResponse = (string);",
        "line": 172,
        "name": "LoginRecoverPasswordHtmlContentResponse"
      },
      {
        "definition": "type PrivateCreateUserData = {\n    requestBody: PrivateUserCreate;\n};",
        "line": 174,
        "name": "PrivateCreateUserData"
      },
      {
        "definition": "type PrivateCreateUserResponse = (UserPublic);",
        "line": 178,
        "name": "PrivateCreateUserResponse"
      },
      {
        "definition": "type UsersReadUsersData = {\n    limit?: number;\n    skip?: number;\n};",
        "line": 180,
        "name": "UsersReadUsersData"
      },
      {
        "definition": "type UsersReadUsersResponse = (UsersPublic);",
        "line": 185,
        "name": "UsersReadUsersResponse"
      },
      {
        "definition": "type UsersCreateUserData = {\n    requestBody: UserCreate;\n};",
        "line": 187,
        "name": "UsersCreateUserData"
      },
      {
        "definition": "type UsersCreateUserResponse = (UserPublic);",
        "line": 191,
        "name": "UsersCreateUserResponse"
      },
      {
        "definition": "type UsersReadUserMeResponse = (UserPublic);",
        "line": 193,
        "name": "UsersReadUserMeResponse"
      },
      {
        "definition": "type UsersDeleteUserMeResponse = (Message);",
        "line": 195,
        "name": "UsersDeleteUserMeResponse"
      },
      {
        "definition": "type UsersUpdateUserMeData = {\n    requestBody: UserUpdateMe;\n};",
        "line": 197,
        "name": "UsersUpdateUserMeData"
      },
      {
        "definition": "type UsersUpdateUserMeResponse = (UserPublic);",
        "line": 201,
        "name": "UsersUpdateUserMeResponse"
      },
      {
        "definition": "type UsersUpdatePasswordMeData = {\n    requestBody: UpdatePassword;\n};",
        "line": 203,
        "name": "UsersUpdatePasswordMeData"
      },
      {
        "definition": "type UsersUpdatePasswordMeResponse = (Message);",
        "line": 207,
        "name": "UsersUpdatePasswordMeResponse"
      },
      {
        "definition": "type UsersRegisterUserData = {\n    requestBody: UserRegister;\n};",
        "line": 209,
        "name": "UsersRegisterUserData"
      },
      {
        "definition": "type UsersRegisterUserResponse = (UserPublic);",
        "line": 213,
        "name": "UsersRegisterUserResponse"
      },
      {
        "definition": "type UsersReadUserByIdData = {\n    userId: string;\n};",
        "line": 215,
        "name": "UsersReadUserByIdData"
      },
      {
        "definition": "type UsersReadUserByIdResponse = (UserPublic);",
        "line": 219,
        "name": "UsersReadUserByIdResponse"
      },
      {
        "definition": "type UsersUpdateUserData = {\n    requestBody: UserUpdate;\n    userId: string;\n};",
        "line": 221,
        "name": "UsersUpdateUserData"
      },
      {
        "definition": "type UsersUpdateUserResponse = (UserPublic);",
        "line": 226,
        "name": "UsersUpdateUserResponse"
      },
      {
        "definition": "type UsersDeleteUserData = {\n    userId: string;\n};",
        "line": 228,
        "name": "UsersDeleteUserData"
      },
      {
        "definition": "type UsersDeleteUserResponse = (Message);",
        "line": 232,
        "name": "UsersDeleteUserResponse"
      },
      {
        "definition": "type UtilsTestEmailData = {\n    emailTo: string;\n};",
        "line": 234,
        "name": "UtilsTestEmailData"
      },
      {
        "definition": "type UtilsTestEmailResponse = (Message);",
        "line": 238,
        "name": "UtilsTestEmailResponse"
      },
      {
        "definition": "type UtilsHealthCheckResponse = (boolean);",
        "line": 240,
        "name": "UtilsHealthCheckResponse"
      }
    ]
  },
  {
    "dependencies": {
      "imports": [
        "@/client",
        "@/components/ui/button",
        "@/components/ui/checkbox",
        "@/components/ui/dialog",
        "@/components/ui/form",
        "@/components/ui/input",
        "@/components/ui/loading-button",
        "@/hooks/useCustomToast",
        "@/utils",
        "@hookform/resolvers/zod",
        "@tanstack/react-query",
        "lucide-react",
        "react",
        "react-hook-form",
        "zod"
      ]
    },
    "file": "AddUser.tsx",
    "functions": [
      {
        "flow": "1. Open dialog via trigger button\n2. Validate form fields (email, password, confirm, superuser, active)\n3. Call createUser API on submit\n4. Show success/error toast and close dialog",
        "line": 82,
        "name": "AddUser",
        "purpose": "Modal dialog for creating new user accounts with email, password, and role fields.",
        "relationships": "Consumes: UsersService.createUser API\nProduces: New user record, success toast, invalidates \"users\" query cache",
        "signature": "() => {\n  const [isOpen, setIsOpen] = useState(false)\n  const queryClient = useQueryClient()\n  const { showSuccessToast, showErrorToast } = useCustomToast()\n\n  const form = useForm<FormData>({\n    resolver: zodResolver(formSchema),\n    mode: \"onBlur\",\n    criteriaMode: \"all\",\n    defaultValues: {\n      email: \"\",\n      full_name: \"\",\n      password: \"\",\n      confirm_password: \"\",\n      is_superuser: false,\n      is_active: false,\n    },\n  })\n\n  const mutation = useMutation({\n    mutationFn: (data: UserCreate) =>\n      UsersService.createUser({ requestBody: data }),\n    onSuccess: () => {\n      showSuccessToast(\"User created successfully\")\n      form.reset()\n      setIsOpen(false)\n    },\n    onError: handleError.bind(showErrorToast),\n    onSettled: () => {\n      queryClient.invalidateQueries({ queryKey: [\"users\"] })\n    },\n  })\n\n  const onSubmit = (data: FormData) => {\n    mutation.mutate(data)\n  }\n\n  return (\n    <Dialog open={isOpen} onOpenChange={setIsOpen}>\n      <DialogTrigger asChild>\n        <Button className=\"my-4\">\n          <Plus className=\"mr-2\" />\n          Add User\n        </Button>\n      </DialogTrigger>\n      <DialogContent className=\"sm:max-w-md\">\n        <DialogHeader>\n          <DialogTitle>Add User</DialogTitle>\n          <DialogDescription>\n            Fill in the form below to add a new user to the system.\n          </DialogDescription>\n        </DialogHeader>\n        <Form {...form}>\n          <form onSubmit={form.handleSubmit(onSubmit)}>\n            <div className=\"grid gap-4 py-4\">\n              <FormField\n                control={form.control}\n                name=\"email\"\n                render={({ field }) => (\n                  <FormItem>\n                    <FormLabel>\n                      Email <span className=\"text-destructive\">*</span>\n                    </FormLabel>\n                    <FormControl>\n                      <Input\n                        placeholder=\"Email\"\n                        type=\"email\"\n                        {...field}\n                        required\n                      />\n                    </FormControl>\n                    <FormMessage />\n                  </FormItem>\n                )}\n              />\n\n              <FormField\n                control={form.control}\n                name=\"full_name\"\n                render={({ field }) => (\n                  <FormItem>\n                    <FormLabel>Full Name</FormLabel>\n                    <FormControl>\n                      <Input placeholder=\"Full name\" type=\"text\" {...field} />\n                    </FormControl>\n                    <FormMessage />\n                  </FormItem>\n                )}\n              />\n\n              <FormField\n                control={form.control}\n                name=\"password\"\n                render={({ field }) => (\n                  <FormItem>\n                    <FormLabel>\n                      Set Password <span className=\"text-destructive\">*</span>\n                    </FormLabel>\n                    <FormControl>\n                      <Input\n                        placeholder=\"Password\"\n                        type=\"password\"\n                        {...field}\n                        required\n                      />\n                    </FormControl>\n                    <FormMessage />\n                  </FormItem>\n                )}\n              />\n\n              <FormField\n                control={form.control}\n                name=\"confirm_password\"\n                render={({ field }) => (\n                  <FormItem>\n                    <FormLabel>\n                      Confirm Password{\" \"}\n                      <span className=\"text-destructive\">*</span>\n                    </FormLabel>\n                    <FormControl>\n                      <Input\n                        placeholder=\"Password\"\n                        type=\"password\"\n                        {...field}\n                        required\n                      />\n                    </FormControl>\n                    <FormMessage />\n                  </FormItem>\n                )}\n              />\n\n              <FormField\n                control={form.control}\n                name=\"is_superuser\"\n                render={({ field }) => (\n                  <FormItem className=\"flex items-center gap-3 space-y-0\">\n                    <FormControl>\n                      <Checkbox\n                        checked={field.value}\n                        onCheckedChange={field.onChange}\n                      />\n                    </FormControl>\n                    <FormLabel className=\"font-normal\">Is superuser?</FormLabel>\n                  </FormItem>\n                )}\n              />\n\n              <FormField\n                control={form.control}\n                name=\"is_active\"\n                render={({ field }) => (\n                  <FormItem className=\"flex items-center gap-3 space-y-0\">\n                    <FormControl>\n                      <Checkbox\n                        checked={field.value}\n                        onCheckedChange={field.onChange}\n                      />\n                    </FormControl>\n                    <FormLabel className=\"font-normal\">Is active?</FormLabel>\n                  </FormItem>\n                )}\n              />\n            </div>\n\n            <DialogFooter>\n              <DialogClose asChild>\n                <Button variant=\"outline\" disabled={mutation.isPending}>\n                  Cancel\n                </Button>\n              </DialogClose>\n              <LoadingButton type=\"submit\" loading={mutation.isPending}>\n                Save\n              </LoadingButton>\n            </DialogFooter>\n          </form>\n        </Form>\n      </DialogContent>\n    </Dialog>\n  )\n}",
        "structure": "isOpen (boolean): internal - Dialog visibility state\nformSchema (zod): Validates email, password match, superuser/active flags"
      }
    ],
    "language": "typescript",
    "lines": 266,
    "module": "Admin/AddUser",
    "path": "frontend/src/components/Admin/AddUser.tsx",
    "purpose": "Dialog for creating new user accounts in the admin panel.",
    "relationships": "Consumes: UsersService.createUser API\nUsed by: Admin users management page",
    "type": "module",
    "types": [
      {
        "definition": "type FormData = z.infer<typeof formSchema>",
        "line": 63,
        "name": "FormData"
      }
    ]
  },
  {
    "dependencies": {
      "imports": [
        "@/client",
        "@/components/ui/button",
        "@/components/ui/dialog",
        "@/components/ui/dropdown-menu",
        "@/components/ui/loading-button",
        "@/hooks/useCustomToast",
        "@/utils",
        "@tanstack/react-query",
        "lucide-react",
        "react",
        "react-hook-form"
      ]
    },
    "file": "DeleteUser.tsx",
    "functions": [
      {
        "flow": "1. Render as dropdown menu item\n2. Open confirmation dialog on click\n3. Call deleteUser API on confirm\n4. Show success/error toast and invoke onSuccess callback",
        "line": 61,
        "name": "DeleteUser",
        "purpose": "Destructive confirmation dialog for permanently deleting a user and associated items.",
        "relationships": "Consumes: UsersService.deleteUser API\nProduces: Success toast, invalidates all query caches",
        "signature": "({ id, onSuccess }: DeleteUserProps) => {\n  const [isOpen, setIsOpen] = useState(false)\n  const queryClient = useQueryClient()\n  const { showSuccessToast, showErrorToast } = useCustomToast()\n  const { handleSubmit } = useForm()\n\n  const deleteUser = async (id: string) => {\n    await UsersService.deleteUser({ userId: id })\n  }\n\n  const mutation = useMutation({\n    mutationFn: deleteUser,\n    onSuccess: () => {\n      showSuccessToast(\"The user was deleted successfully\")\n      setIsOpen(false)\n      onSuccess()\n    },\n    onError: handleError.bind(showErrorToast),\n    onSettled: () => {\n      queryClient.invalidateQueries()\n    },\n  })\n\n  const onSubmit = async () => {\n    mutation.mutate(id)\n  }\n\n  return (\n    <Dialog open={isOpen} onOpenChange={setIsOpen}>\n      <DropdownMenuItem\n        variant=\"destructive\"\n        onSelect={(e) => e.preventDefault()}\n        onClick={() => setIsOpen(true)}\n      >\n        <Trash2 />\n        Delete User\n      </DropdownMenuItem>\n      <DialogContent className=\"sm:max-w-md\">\n        <form onSubmit={handleSubmit(onSubmit)}>\n          <DialogHeader>\n            <DialogTitle>Delete User</DialogTitle>\n            <DialogDescription>\n              All items associated with this user will also be{\" \"}\n              <strong>permanently deleted.</strong> Are you sure? You will not\n              be able to undo this action.\n            </DialogDescription>\n          </DialogHeader>\n\n          <DialogFooter className=\"mt-4\">\n            <DialogClose asChild>\n              <Button variant=\"outline\" disabled={mutation.isPending}>\n                Cancel\n              </Button>\n            </DialogClose>\n            <LoadingButton\n              variant=\"destructive\"\n              type=\"submit\"\n              loading={mutation.isPending}\n            >\n              Delete\n            </LoadingButton>\n          </DialogFooter>\n        </form>\n      </DialogContent>\n    </Dialog>\n  )\n}",
        "structure": "id (string): input - User ID to delete\nonSuccess (function): input - Callback on successful deletion"
      }
    ],
    "interfaces": [
      {
        "line": 39,
        "name": "DeleteUserProps",
        "purpose": "Props for DeleteUser dialog component.",
        "structure": "id (string): input - User ID to delete\nonSuccess (function): input - Callback after successful deletion"
      }
    ],
    "language": "typescript",
    "lines": 130,
    "module": "Admin/DeleteUser",
    "path": "frontend/src/components/Admin/DeleteUser.tsx",
    "purpose": "Confirmation dialog for deleting a user account.",
    "relationships": "Consumes: UsersService.deleteUser API\nUsed by: UserActionsMenu dropdown",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/client",
        "@/components/ui/button",
        "@/components/ui/checkbox",
        "@/components/ui/dialog",
        "@/components/ui/dropdown-menu",
        "@/components/ui/form",
        "@/components/ui/input",
        "@/components/ui/loading-button",
        "@/hooks/useCustomToast",
        "@/utils",
        "@hookform/resolvers/zod",
        "@tanstack/react-query",
        "lucide-react",
        "react",
        "react-hook-form",
        "zod"
      ]
    },
    "file": "EditUser.tsx",
    "functions": [
      {
        "flow": "1. Render as dropdown menu item\n2. Open dialog pre-populated with current user data\n3. Validate and strip empty password before submit\n4. Call updateUser API\n5. Show success/error toast and invoke onSuccess callback",
        "line": 95,
        "name": "EditUser",
        "purpose": "Modal dialog for editing user details (email, name, password, role, status).",
        "relationships": "Consumes: UsersService.updateUser API\nProduces: Updated user record, success toast, invalidates \"users\" query cache",
        "signature": "({ user, onSuccess }: EditUserProps) => {\n  const [isOpen, setIsOpen] = useState(false)\n  const queryClient = useQueryClient()\n  const { showSuccessToast, showErrorToast } = useCustomToast()\n\n  const form = useForm<FormData>({\n    resolver: zodResolver(formSchema),\n    mode: \"onBlur\",\n    criteriaMode: \"all\",\n    defaultValues: {\n      email: user.email,\n      full_name: user.full_name ?? undefined,\n      is_superuser: user.is_superuser,\n      is_active: user.is_active,\n    },\n  })\n\n  const mutation = useMutation({\n    mutationFn: (data: FormData) =>\n      UsersService.updateUser({ userId: user.id, requestBody: data }),\n    onSuccess: () => {\n      showSuccessToast(\"User updated successfully\")\n      setIsOpen(false)\n      onSuccess()\n    },\n    onError: handleError.bind(showErrorToast),\n    onSettled: () => {\n      queryClient.invalidateQueries({ queryKey: [\"users\"] })\n    },\n  })\n\n  const onSubmit = (data: FormData) => {\n    // exclude confirm_password from submission data and remove password if empty\n    const { confirm_password: _, ...submitData } = data\n    if (!submitData.password) {\n      delete submitData.password\n    }\n    mutation.mutate(submitData)\n  }\n\n  return (\n    <Dialog open={isOpen} onOpenChange={setIsOpen}>\n      <DropdownMenuItem\n        onSelect={(e) => e.preventDefault()}\n        onClick={() => setIsOpen(true)}\n      >\n        <Pencil />\n        Edit User\n      </DropdownMenuItem>\n      <DialogContent className=\"sm:max-w-md\">\n        <Form {...form}>\n          <form onSubmit={form.handleSubmit(onSubmit)}>\n            <DialogHeader>\n              <DialogTitle>Edit User</DialogTitle>\n              <DialogDescription>\n                Update the user details below.\n              </DialogDescription>\n            </DialogHeader>\n            <div className=\"grid gap-4 py-4\">\n              <FormField\n                control={form.control}\n                name=\"email\"\n                render={({ field }) => (\n                  <FormItem>\n                    <FormLabel>\n                      Email <span className=\"text-destructive\">*</span>\n                    </FormLabel>\n                    <FormControl>\n                      <Input\n                        placeholder=\"Email\"\n                        type=\"email\"\n                        {...field}\n                        required\n                      />\n                    </FormControl>\n                    <FormMessage />\n                  </FormItem>\n                )}\n              />\n\n              <FormField\n                control={form.control}\n                name=\"full_name\"\n                render={({ field }) => (\n                  <FormItem>\n                    <FormLabel>Full Name</FormLabel>\n                    <FormControl>\n                      <Input placeholder=\"Full name\" type=\"text\" {...field} />\n                    </FormControl>\n                    <FormMessage />\n                  </FormItem>\n                )}\n              />\n\n              <FormField\n                control={form.control}\n                name=\"password\"\n                render={({ field }) => (\n                  <FormItem>\n                    <FormLabel>Set Password</FormLabel>\n                    <FormControl>\n                      <Input\n                        placeholder=\"Password\"\n                        type=\"password\"\n                        {...field}\n                      />\n                    </FormControl>\n                    <FormMessage />\n                  </FormItem>\n                )}\n              />\n\n              <FormField\n                control={form.control}\n                name=\"confirm_password\"\n                render={({ field }) => (\n                  <FormItem>\n                    <FormLabel>Confirm Password</FormLabel>\n                    <FormControl>\n                      <Input\n                        placeholder=\"Password\"\n                        type=\"password\"\n                        {...field}\n                      />\n                    </FormControl>\n                    <FormMessage />\n                  </FormItem>\n                )}\n              />\n\n              <FormField\n                control={form.control}\n                name=\"is_superuser\"\n                render={({ field }) => (\n                  <FormItem className=\"flex items-center gap-3 space-y-0\">\n                    <FormControl>\n                      <Checkbox\n                        checked={field.value}\n                        onCheckedChange={field.onChange}\n                      />\n                    </FormControl>\n                    <FormLabel className=\"font-normal\">Is superuser?</FormLabel>\n                  </FormItem>\n                )}\n              />\n\n              <FormField\n                control={form.control}\n                name=\"is_active\"\n                render={({ field }) => (\n                  <FormItem className=\"flex items-center gap-3 space-y-0\">\n                    <FormControl>\n                      <Checkbox\n                        checked={field.value}\n                        onCheckedChange={field.onChange}\n                      />\n                    </FormControl>\n                    <FormLabel className=\"font-normal\">Is active?</FormLabel>\n                  </FormItem>\n                )}\n              />\n            </div>\n\n            <DialogFooter>\n              <DialogClose asChild>\n                <Button variant=\"outline\" disabled={mutation.isPending}>\n                  Cancel\n                </Button>\n              </DialogClose>\n              <LoadingButton type=\"submit\" loading={mutation.isPending}>\n                Save\n              </LoadingButton>\n            </DialogFooter>\n          </form>\n        </Form>\n      </DialogContent>\n    </Dialog>\n  )\n}",
        "structure": "user (UserPublic): input - Existing user data\nonSuccess (function): input - Callback on successful update\nformSchema (zod): Validates email, optional password match, superuser/active flags"
      }
    ],
    "interfaces": [
      {
        "line": 71,
        "name": "EditUserProps",
        "purpose": "Props for EditUser dialog component.",
        "structure": "user (UserPublic): input - User data to pre-populate form\nonSuccess (function): input - Callback after successful update"
      }
    ],
    "language": "typescript",
    "lines": 276,
    "module": "Admin/EditUser",
    "path": "frontend/src/components/Admin/EditUser.tsx",
    "purpose": "Dialog for editing existing user account details.",
    "relationships": "Consumes: UsersService.updateUser API\nUsed by: UserActionsMenu dropdown",
    "type": "module",
    "types": [
      {
        "definition": "type FormData = z.infer<typeof formSchema>",
        "line": 62,
        "name": "FormData"
      }
    ]
  },
  {
    "dependencies": {
      "imports": [
        "./DeleteUser",
        "./EditUser",
        "@/client",
        "@/components/ui/button",
        "@/components/ui/dropdown-menu",
        "@/hooks/useAuth",
        "lucide-react",
        "react"
      ]
    },
    "file": "UserActionsMenu.tsx",
    "functions": [
      {
        "flow": "1. Hide menu if target user is the current logged-in user\n2. Render ellipsis trigger button\n3. Show EditUser and DeleteUser options in dropdown",
        "line": 50,
        "name": "UserActionsMenu",
        "purpose": "Dropdown menu with edit/delete actions for a user table row.",
        "relationships": "Consumes: EditUser, DeleteUser components; useAuth for current user check\nUsed by: Admin users table actions column",
        "signature": "({ user }: UserActionsMenuProps) => {\n  const [open, setOpen] = useState(false)\n  const { user: currentUser } = useAuth()\n\n  if (user.id === currentUser?.id) {\n    return null\n  }\n\n  return (\n    <DropdownMenu open={open} onOpenChange={setOpen}>\n      <DropdownMenuTrigger asChild>\n        <Button variant=\"ghost\" size=\"icon\">\n          <EllipsisVertical />\n        </Button>\n      </DropdownMenuTrigger>\n      <DropdownMenuContent align=\"end\">\n        <EditUser user={user} onSuccess={() => setOpen(false)} />\n        <DeleteUser id={user.id} onSuccess={() => setOpen(false)} />\n      </DropdownMenuContent>\n    </DropdownMenu>\n  )\n}",
        "structure": "user (UserPublic): input - Target user for actions"
      }
    ],
    "interfaces": [
      {
        "line": 31,
        "name": "UserActionsMenuProps",
        "purpose": "Props for UserActionsMenu component.",
        "structure": "user (UserPublic): input - User data for the row actions"
      }
    ],
    "language": "typescript",
    "lines": 72,
    "module": "Admin/UserActionsMenu",
    "path": "frontend/src/components/Admin/UserActionsMenu.tsx",
    "purpose": "Dropdown actions menu for user row operations (edit, delete).",
    "relationships": "Consumes: EditUser, DeleteUser components\nUsed by: Admin users table columns",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "./UserActionsMenu",
        "@/client",
        "@/components/ui/badge",
        "@/lib/utils",
        "@tanstack/react-table"
      ]
    },
    "file": "columns.tsx",
    "language": "typescript",
    "lines": 107,
    "module": "Admin/columns",
    "path": "frontend/src/components/Admin/columns.tsx",
    "purpose": "Column definitions for the admin users data table.",
    "relationships": "Consumes: UserActionsMenu component, UserPublic type\nUsed by: Admin users page DataTable",
    "type": "module",
    "types": [
      {
        "definition": "type UserTableData = UserPublic & {\n  isCurrentUser: boolean\n}",
        "line": 24,
        "name": "UserTableData"
      }
    ]
  },
  {
    "dependencies": {
      "imports": [
        "@/components/theme-provider",
        "@/components/ui/button",
        "@/components/ui/dropdown-menu",
        "@/components/ui/sidebar",
        "lucide-react"
      ]
    },
    "file": "Appearance.tsx",
    "functions": [
      {
        "line": 42,
        "name": "SidebarAppearance",
        "purpose": "Sidebar-integrated theme toggle with icon reflecting current theme.",
        "relationships": "Consumes: useTheme, useSidebar contexts\nUsed by: AppSidebar footer",
        "signature": "() => {\n  const { isMobile } = useSidebar()\n  const { setTheme, theme } = useTheme()\n  const Icon = ICON_MAP[theme]\n\n  return (\n    <SidebarMenuItem>\n      <DropdownMenu modal={false}>\n        <DropdownMenuTrigger asChild>\n          <SidebarMenuButton tooltip=\"Appearance\" data-testid=\"theme-button\">\n            <Icon className=\"size-4 text-muted-foreground\" />\n            <span>Appearance</span>\n            <span className=\"sr-only\">Toggle theme</span>\n          </SidebarMenuButton>\n        </DropdownMenuTrigger>\n        <DropdownMenuContent\n          side={isMobile ? \"top\" : \"right\"}\n          align=\"end\"\n          className=\"w-(--radix-dropdown-menu-trigger-width) min-w-56\"\n        >\n          <DropdownMenuItem\n            data-testid=\"light-mode\"\n            onClick={() => setTheme(\"light\")}\n          >\n            <Sun className=\"mr-2 h-4 w-4\" />\n            Light\n          </DropdownMenuItem>\n          <DropdownMenuItem\n            data-testid=\"dark-mode\"\n            onClick={() => setTheme(\"dark\")}\n          >\n            <Moon className=\"mr-2 h-4 w-4\" />\n            Dark\n          </DropdownMenuItem>\n          <DropdownMenuItem onClick={() => setTheme(\"system\")}>\n            <Monitor className=\"mr-2 h-4 w-4\" />\n            System\n          </DropdownMenuItem>\n        </DropdownMenuContent>\n      </DropdownMenu>\n    </SidebarMenuItem>\n  )\n}"
      },
      {
        "line": 93,
        "name": "Appearance",
        "purpose": "Standalone theme toggle button with sun/moon icon animation.",
        "relationships": "Consumes: useTheme context\nUsed by: AuthLayout header",
        "signature": "() => {\n  const { setTheme } = useTheme()\n\n  return (\n    <div className=\"flex items-center justify-center\">\n      <DropdownMenu modal={false}>\n        <DropdownMenuTrigger asChild>\n          <Button data-testid=\"theme-button\" variant=\"outline\" size=\"icon\">\n            <Sun className=\"h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0\" />\n            <Moon className=\"absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100\" />\n            <span className=\"sr-only\">Toggle theme</span>\n          </Button>\n        </DropdownMenuTrigger>\n        <DropdownMenuContent align=\"end\">\n          <DropdownMenuItem\n            data-testid=\"light-mode\"\n            onClick={() => setTheme(\"light\")}\n          >\n            <Sun className=\"mr-2 h-4 w-4\" />\n            Light\n          </DropdownMenuItem>\n          <DropdownMenuItem\n            data-testid=\"dark-mode\"\n            onClick={() => setTheme(\"dark\")}\n          >\n            <Moon className=\"mr-2 h-4 w-4\" />\n            Dark\n          </DropdownMenuItem>\n          <DropdownMenuItem onClick={() => setTheme(\"system\")}>\n            <Monitor className=\"mr-2 h-4 w-4\" />\n            System\n          </DropdownMenuItem>\n        </DropdownMenuContent>\n      </DropdownMenu>\n    </div>\n  )\n}"
      }
    ],
    "language": "typescript",
    "lines": 130,
    "module": "Common/Appearance",
    "path": "frontend/src/components/Common/Appearance.tsx",
    "purpose": "Theme toggle components for switching between light, dark, and system modes.",
    "relationships": "Consumes: ThemeProvider context (useTheme)\nUsed by: AppSidebar (SidebarAppearance), AuthLayout (Appearance)",
    "type": "module",
    "types": [
      {
        "definition": "type LucideIcon = React.FC<React.SVGProps<SVGSVGElement>>",
        "line": 27,
        "name": "LucideIcon"
      }
    ]
  },
  {
    "dependencies": {
      "imports": [
        "./Footer",
        "@/components/Common/Appearance",
        "@/components/Common/Logo"
      ]
    },
    "file": "AuthLayout.tsx",
    "functions": [
      {
        "line": 35,
        "name": "AuthLayout",
        "purpose": "Split-screen layout with logo panel (left) and auth form (right).",
        "relationships": "Consumes: Logo, Appearance, Footer components\nUsed by: Authentication route pages",
        "signature": "function AuthLayout({ children }: AuthLayoutProps) {",
        "structure": "children (ReactNode): input - Auth form content"
      }
    ],
    "interfaces": [
      {
        "line": 21,
        "name": "AuthLayoutProps",
        "purpose": "Props for AuthLayout component.",
        "structure": "children (ReactNode): input - Auth form content to render"
      }
    ],
    "language": "typescript",
    "lines": 53,
    "module": "Common/AuthLayout",
    "path": "frontend/src/components/Common/AuthLayout.tsx",
    "purpose": "Two-column layout wrapper for authentication pages (login, signup, reset).",
    "relationships": "Consumes: Appearance, Logo, Footer components\nUsed by: Login, Signup, ResetPassword routes",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/components/ui/button",
        "@/components/ui/select",
        "@/components/ui/table",
        "@tanstack/react-table",
        "lucide-react"
      ]
    },
    "file": "DataTable.tsx",
    "functions": [
      {
        "flow": "1. Initialize table with data and column definitions\n2. Render header groups and data rows\n3. Show \"No results\" when empty\n4. Render pagination controls when multiple pages exist",
        "line": 70,
        "name": "DataTable",
        "purpose": "Reusable paginated data table with configurable columns and page size.",
        "relationships": "Consumes: TanStack Table (getCoreRowModel, getPaginationRowModel)\nUsed by: Admin users page, Items page",
        "signature": "function DataTable<TData, TValue>({\n  columns,\n  data,\n}: DataTableProps<TData, TValue>) {",
        "structure": "columns (ColumnDef[]): input - Column definitions\ndata (TData[]): input - Row data"
      }
    ],
    "interfaces": [
      {
        "line": 48,
        "name": "DataTableProps",
        "purpose": "Props for the generic DataTable component.",
        "structure": "columns (ColumnDef[]): input - Column definitions for the table\ndata (TData[]): input - Row data array"
      }
    ],
    "language": "typescript",
    "lines": 228,
    "module": "Common/DataTable",
    "path": "frontend/src/components/Common/DataTable.tsx",
    "purpose": "Generic paginated data table component built on TanStack Table.",
    "relationships": "Consumes: TanStack Table core and pagination models\nUsed by: Admin users page, Items page",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/components/ui/button",
        "@tanstack/react-router"
      ]
    },
    "file": "ErrorComponent.tsx",
    "functions": [
      {
        "line": 19,
        "name": "ErrorComponent",
        "purpose": "Full-screen error page with \"Go Home\" navigation link.",
        "relationships": "Produces: Navigation to root route via Link",
        "signature": "() => {\n  return (\n    <div\n      className=\"flex min-h-screen items-center justify-center flex-col p-4\"\n      data-testid=\"error-component\"\n    >\n      <div className=\"flex items-center z-10\">\n        <div className=\"flex flex-col ml-4 items-center justify-center p-4\">\n          <span className=\"text-6xl md:text-8xl font-bold leading-none mb-4\">\n            Error\n          </span>\n          <span className=\"text-2xl font-bold mb-2\">Oops!</span>\n        </div>\n      </div>\n\n      <p className=\"text-lg text-muted-foreground mb-4 text-center z-10\">\n        Something went wrong. Please try again.\n      </p>\n      <Link to=\"/\">\n        <Button>Go Home</Button>\n      </Link>\n    </div>\n  )\n}"
      }
    ],
    "language": "typescript",
    "lines": 45,
    "module": "Common/ErrorComponent",
    "path": "frontend/src/components/Common/ErrorComponent.tsx",
    "purpose": "Generic error page displayed when an unhandled error occurs.",
    "relationships": "Used by: Router error boundary",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "react-icons/fa",
        "react-icons/fa6"
      ]
    },
    "file": "Footer.tsx",
    "functions": [
      {
        "line": 33,
        "name": "Footer",
        "purpose": "Footer bar with dynamic copyright year and GitHub/X/LinkedIn links.",
        "relationships": "Used by: AuthLayout",
        "signature": "function Footer() {"
      }
    ],
    "language": "typescript",
    "lines": 60,
    "module": "Common/Footer",
    "path": "frontend/src/components/Common/Footer.tsx",
    "purpose": "Application footer with copyright and social media links.",
    "relationships": "Used by: AuthLayout",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "/assets/images/fastapi-icon-light.svg",
        "/assets/images/fastapi-icon.svg",
        "/assets/images/fastapi-logo-light.svg",
        "/assets/images/fastapi-logo.svg",
        "@/components/theme-provider",
        "@/lib/utils",
        "@tanstack/react-router"
      ]
    },
    "file": "Logo.tsx",
    "functions": [
      {
        "line": 45,
        "name": "Logo",
        "purpose": "Renders theme-aware FastAPI logo in full, icon, or responsive (collapsible) mode.",
        "relationships": "Consumes: useTheme for dark/light logo selection\nUsed by: AuthLayout (full), AppSidebar (responsive)",
        "signature": "function Logo({\n  variant = \"full\",\n  className,\n  asLink = true,\n}: LogoProps) {",
        "structure": "variant (\"full\"|\"icon\"|\"responsive\"): input - Display mode, defaults to \"full\"\nasLink (boolean): input - Wraps in Link to \"/\" when true (default)"
      }
    ],
    "interfaces": [
      {
        "line": 28,
        "name": "LogoProps",
        "purpose": "Props for Logo component.",
        "structure": "variant (\"full\"|\"icon\"|\"responsive\"): input - Logo display mode\nclassName (string): input - Additional CSS classes\nasLink (boolean): input - Whether to wrap logo in a home link"
      }
    ],
    "language": "typescript",
    "lines": 90,
    "module": "Common/Logo",
    "path": "frontend/src/components/Common/Logo.tsx",
    "purpose": "Theme-aware FastAPI logo component with full, icon, and responsive variants.",
    "relationships": "Consumes: ThemeProvider context (useTheme)\nUsed by: AuthLayout, AppSidebar",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/components/ui/button",
        "@tanstack/react-router"
      ]
    },
    "file": "NotFound.tsx",
    "functions": [
      {
        "line": 19,
        "name": "NotFound",
        "purpose": "Full-screen 404 page with \"Go Back\" navigation to home.",
        "relationships": "Produces: Navigation to root route via Link",
        "signature": "() => {\n  return (\n    <div\n      className=\"flex min-h-screen items-center justify-center flex-col p-4\"\n      data-testid=\"not-found\"\n    >\n      <div className=\"flex items-center z-10\">\n        <div className=\"flex flex-col ml-4 items-center justify-center p-4\">\n          <span className=\"text-6xl md:text-8xl font-bold leading-none mb-4\">\n            404\n          </span>\n          <span className=\"text-2xl font-bold mb-2\">Oops!</span>\n        </div>\n      </div>\n\n      <p className=\"text-lg text-muted-foreground mb-4 text-center z-10\">\n        The page you are looking for was not found.\n      </p>\n      <div className=\"z-10\">\n        <Link to=\"/\">\n          <Button className=\"mt-4\">Go Back</Button>\n        </Link>\n      </div>\n    </div>\n  )\n}"
      }
    ],
    "language": "typescript",
    "lines": 47,
    "module": "Common/NotFound",
    "path": "frontend/src/components/Common/NotFound.tsx",
    "purpose": "404 page displayed when a route is not matched.",
    "relationships": "Used by: Router notFoundComponent",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/client",
        "@/components/ui/button",
        "@/components/ui/dialog",
        "@/components/ui/form",
        "@/components/ui/input",
        "@/components/ui/loading-button",
        "@/hooks/useCustomToast",
        "@/utils",
        "@hookform/resolvers/zod",
        "@tanstack/react-query",
        "lucide-react",
        "react",
        "react-hook-form",
        "zod"
      ]
    },
    "file": "AddItem.tsx",
    "functions": [
      {
        "flow": "1. Open dialog via trigger button\n2. Validate title (required) and description (optional)\n3. Call createItem API on submit\n4. Show success/error toast and close dialog",
        "line": 67,
        "name": "AddItem",
        "purpose": "Modal dialog for creating a new item with title and optional description.",
        "relationships": "Consumes: ItemsService.createItem API\nProduces: New item record, success toast, invalidates \"items\" query cache",
        "signature": "() => {\n  const [isOpen, setIsOpen] = useState(false)\n  const queryClient = useQueryClient()\n  const { showSuccessToast, showErrorToast } = useCustomToast()\n\n  const form = useForm<FormData>({\n    resolver: zodResolver(formSchema),\n    mode: \"onBlur\",\n    criteriaMode: \"all\",\n    defaultValues: {\n      title: \"\",\n      description: \"\",\n    },\n  })\n\n  const mutation = useMutation({\n    mutationFn: (data: ItemCreate) =>\n      ItemsService.createItem({ requestBody: data }),\n    onSuccess: () => {\n      showSuccessToast(\"Item created successfully\")\n      form.reset()\n      setIsOpen(false)\n    },\n    onError: handleError.bind(showErrorToast),\n    onSettled: () => {\n      queryClient.invalidateQueries({ queryKey: [\"items\"] })\n    },\n  })\n\n  const onSubmit = (data: FormData) => {\n    mutation.mutate(data)\n  }\n\n  return (\n    <Dialog open={isOpen} onOpenChange={setIsOpen}>\n      <DialogTrigger asChild>\n        <Button className=\"my-4\">\n          <Plus className=\"mr-2\" />\n          Add Item\n        </Button>\n      </DialogTrigger>\n      <DialogContent className=\"sm:max-w-md\">\n        <DialogHeader>\n          <DialogTitle>Add Item</DialogTitle>\n          <DialogDescription>\n            Fill in the details to add a new item.\n          </DialogDescription>\n        </DialogHeader>\n        <Form {...form}>\n          <form onSubmit={form.handleSubmit(onSubmit)}>\n            <div className=\"grid gap-4 py-4\">\n              <FormField\n                control={form.control}\n                name=\"title\"\n                render={({ field }) => (\n                  <FormItem>\n                    <FormLabel>\n                      Title <span className=\"text-destructive\">*</span>\n                    </FormLabel>\n                    <FormControl>\n                      <Input\n                        placeholder=\"Title\"\n                        type=\"text\"\n                        {...field}\n                        required\n                      />\n                    </FormControl>\n                    <FormMessage />\n                  </FormItem>\n                )}\n              />\n\n              <FormField\n                control={form.control}\n                name=\"description\"\n                render={({ field }) => (\n                  <FormItem>\n                    <FormLabel>Description</FormLabel>\n                    <FormControl>\n                      <Input placeholder=\"Description\" type=\"text\" {...field} />\n                    </FormControl>\n                    <FormMessage />\n                  </FormItem>\n                )}\n              />\n            </div>\n\n            <DialogFooter>\n              <DialogClose asChild>\n                <Button variant=\"outline\" disabled={mutation.isPending}>\n                  Cancel\n                </Button>\n              </DialogClose>\n              <LoadingButton type=\"submit\" loading={mutation.isPending}>\n                Save\n              </LoadingButton>\n            </DialogFooter>\n          </form>\n        </Form>\n      </DialogContent>\n    </Dialog>\n  )\n}",
        "structure": "isOpen (boolean): internal - Dialog visibility state\nformSchema (zod): Validates required title field"
      }
    ],
    "language": "typescript",
    "lines": 172,
    "module": "Items/AddItem",
    "path": "frontend/src/components/Items/AddItem.tsx",
    "purpose": "Dialog for creating new items with title and description.",
    "relationships": "Consumes: ItemsService.createItem API\nUsed by: Items management page",
    "type": "module",
    "types": [
      {
        "definition": "type FormData = z.infer<typeof formSchema>",
        "line": 48,
        "name": "FormData"
      }
    ]
  },
  {
    "dependencies": {
      "imports": [
        "@/client",
        "@/components/ui/button",
        "@/components/ui/dialog",
        "@/components/ui/dropdown-menu",
        "@/components/ui/loading-button",
        "@/hooks/useCustomToast",
        "@/utils",
        "@tanstack/react-query",
        "lucide-react",
        "react",
        "react-hook-form"
      ]
    },
    "file": "DeleteItem.tsx",
    "functions": [
      {
        "flow": "1. Render as dropdown menu item\n2. Open confirmation dialog on click\n3. Call deleteItem API on confirm\n4. Show success/error toast and invoke onSuccess callback",
        "line": 61,
        "name": "DeleteItem",
        "purpose": "Destructive confirmation dialog for permanently deleting an item.",
        "relationships": "Consumes: ItemsService.deleteItem API\nProduces: Success toast, invalidates all query caches",
        "signature": "({ id, onSuccess }: DeleteItemProps) => {\n  const [isOpen, setIsOpen] = useState(false)\n  const queryClient = useQueryClient()\n  const { showSuccessToast, showErrorToast } = useCustomToast()\n  const { handleSubmit } = useForm()\n\n  const deleteItem = async (id: string) => {\n    await ItemsService.deleteItem({ id: id })\n  }\n\n  const mutation = useMutation({\n    mutationFn: deleteItem,\n    onSuccess: () => {\n      showSuccessToast(\"The item was deleted successfully\")\n      setIsOpen(false)\n      onSuccess()\n    },\n    onError: handleError.bind(showErrorToast),\n    onSettled: () => {\n      queryClient.invalidateQueries()\n    },\n  })\n\n  const onSubmit = async () => {\n    mutation.mutate(id)\n  }\n\n  return (\n    <Dialog open={isOpen} onOpenChange={setIsOpen}>\n      <DropdownMenuItem\n        variant=\"destructive\"\n        onSelect={(e) => e.preventDefault()}\n        onClick={() => setIsOpen(true)}\n      >\n        <Trash2 />\n        Delete Item\n      </DropdownMenuItem>\n      <DialogContent className=\"sm:max-w-md\">\n        <form onSubmit={handleSubmit(onSubmit)}>\n          <DialogHeader>\n            <DialogTitle>Delete Item</DialogTitle>\n            <DialogDescription>\n              This item will be permanently deleted. Are you sure? You will not\n              be able to undo this action.\n            </DialogDescription>\n          </DialogHeader>\n\n          <DialogFooter className=\"mt-4\">\n            <DialogClose asChild>\n              <Button variant=\"outline\" disabled={mutation.isPending}>\n                Cancel\n              </Button>\n            </DialogClose>\n            <LoadingButton\n              variant=\"destructive\"\n              type=\"submit\"\n              loading={mutation.isPending}\n            >\n              Delete\n            </LoadingButton>\n          </DialogFooter>\n        </form>\n      </DialogContent>\n    </Dialog>\n  )\n}",
        "structure": "id (string): input - Item ID to delete\nonSuccess (function): input - Callback on successful deletion"
      }
    ],
    "interfaces": [
      {
        "line": 39,
        "name": "DeleteItemProps",
        "purpose": "Props for DeleteItem dialog component.",
        "structure": "id (string): input - Item ID to delete\nonSuccess (function): input - Callback after successful deletion"
      }
    ],
    "language": "typescript",
    "lines": 129,
    "module": "Items/DeleteItem",
    "path": "frontend/src/components/Items/DeleteItem.tsx",
    "purpose": "Confirmation dialog for deleting an item.",
    "relationships": "Consumes: ItemsService.deleteItem API\nUsed by: ItemActionsMenu dropdown",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/client",
        "@/components/ui/button",
        "@/components/ui/dialog",
        "@/components/ui/dropdown-menu",
        "@/components/ui/form",
        "@/components/ui/input",
        "@/components/ui/loading-button",
        "@/hooks/useCustomToast",
        "@/utils",
        "@hookform/resolvers/zod",
        "@tanstack/react-query",
        "lucide-react",
        "react",
        "react-hook-form",
        "zod"
      ]
    },
    "file": "EditItem.tsx",
    "functions": [
      {
        "flow": "1. Render as dropdown menu item\n2. Open dialog pre-populated with current item data\n3. Validate and submit updated fields\n4. Show success/error toast and invoke onSuccess callback",
        "line": 80,
        "name": "EditItem",
        "purpose": "Modal dialog for editing item title and description.",
        "relationships": "Consumes: ItemsService.updateItem API\nProduces: Updated item record, success toast, invalidates \"items\" query cache",
        "signature": "({ item, onSuccess }: EditItemProps) => {\n  const [isOpen, setIsOpen] = useState(false)\n  const queryClient = useQueryClient()\n  const { showSuccessToast, showErrorToast } = useCustomToast()\n\n  const form = useForm<FormData>({\n    resolver: zodResolver(formSchema),\n    mode: \"onBlur\",\n    criteriaMode: \"all\",\n    defaultValues: {\n      title: item.title,\n      description: item.description ?? undefined,\n    },\n  })\n\n  const mutation = useMutation({\n    mutationFn: (data: FormData) =>\n      ItemsService.updateItem({ id: item.id, requestBody: data }),\n    onSuccess: () => {\n      showSuccessToast(\"Item updated successfully\")\n      setIsOpen(false)\n      onSuccess()\n    },\n    onError: handleError.bind(showErrorToast),\n    onSettled: () => {\n      queryClient.invalidateQueries({ queryKey: [\"items\"] })\n    },\n  })\n\n  const onSubmit = (data: FormData) => {\n    mutation.mutate(data)\n  }\n\n  return (\n    <Dialog open={isOpen} onOpenChange={setIsOpen}>\n      <DropdownMenuItem\n        onSelect={(e) => e.preventDefault()}\n        onClick={() => setIsOpen(true)}\n      >\n        <Pencil />\n        Edit Item\n      </DropdownMenuItem>\n      <DialogContent className=\"sm:max-w-md\">\n        <Form {...form}>\n          <form onSubmit={form.handleSubmit(onSubmit)}>\n            <DialogHeader>\n              <DialogTitle>Edit Item</DialogTitle>\n              <DialogDescription>\n                Update the item details below.\n              </DialogDescription>\n            </DialogHeader>\n            <div className=\"grid gap-4 py-4\">\n              <FormField\n                control={form.control}\n                name=\"title\"\n                render={({ field }) => (\n                  <FormItem>\n                    <FormLabel>\n                      Title <span className=\"text-destructive\">*</span>\n                    </FormLabel>\n                    <FormControl>\n                      <Input placeholder=\"Title\" type=\"text\" {...field} />\n                    </FormControl>\n                    <FormMessage />\n                  </FormItem>\n                )}\n              />\n\n              <FormField\n                control={form.control}\n                name=\"description\"\n                render={({ field }) => (\n                  <FormItem>\n                    <FormLabel>Description</FormLabel>\n                    <FormControl>\n                      <Input placeholder=\"Description\" type=\"text\" {...field} />\n                    </FormControl>\n                    <FormMessage />\n                  </FormItem>\n                )}\n              />\n            </div>\n\n            <DialogFooter>\n              <DialogClose asChild>\n                <Button variant=\"outline\" disabled={mutation.isPending}>\n                  Cancel\n                </Button>\n              </DialogClose>\n              <LoadingButton type=\"submit\" loading={mutation.isPending}>\n                Save\n              </LoadingButton>\n            </DialogFooter>\n          </form>\n        </Form>\n      </DialogContent>\n    </Dialog>\n  )\n}",
        "structure": "item (ItemPublic): input - Existing item data\nonSuccess (function): input - Callback on successful update\nformSchema (zod): Validates required title"
      }
    ],
    "interfaces": [
      {
        "line": 57,
        "name": "EditItemProps",
        "purpose": "Props for EditItem dialog component.",
        "structure": "item (ItemPublic): input - Item data to pre-populate form\nonSuccess (function): input - Callback after successful update"
      }
    ],
    "language": "typescript",
    "lines": 181,
    "module": "Items/EditItem",
    "path": "frontend/src/components/Items/EditItem.tsx",
    "purpose": "Dialog for editing existing item details.",
    "relationships": "Consumes: ItemsService.updateItem API\nUsed by: ItemActionsMenu dropdown",
    "type": "module",
    "types": [
      {
        "definition": "type FormData = z.infer<typeof formSchema>",
        "line": 48,
        "name": "FormData"
      }
    ]
  },
  {
    "dependencies": {
      "imports": [
        "../Items/DeleteItem",
        "../Items/EditItem",
        "@/client",
        "@/components/ui/button",
        "@/components/ui/dropdown-menu",
        "lucide-react",
        "react"
      ]
    },
    "file": "ItemActionsMenu.tsx",
    "functions": [
      {
        "line": 44,
        "name": "ItemActionsMenu",
        "purpose": "Dropdown menu with edit/delete actions for an item table row.",
        "relationships": "Consumes: EditItem, DeleteItem components\nUsed by: Items table actions column",
        "signature": "({ item }: ItemActionsMenuProps) => {\n  const [open, setOpen] = useState(false)\n\n  return (\n    <DropdownMenu open={open} onOpenChange={setOpen}>\n      <DropdownMenuTrigger asChild>\n        <Button variant=\"ghost\" size=\"icon\">\n          <EllipsisVertical />\n        </Button>\n      </DropdownMenuTrigger>\n      <DropdownMenuContent align=\"end\">\n        <EditItem item={item} onSuccess={() => setOpen(false)} />\n        <DeleteItem id={item.id} onSuccess={() => setOpen(false)} />\n      </DropdownMenuContent>\n    </DropdownMenu>\n  )\n}",
        "structure": "item (ItemPublic): input - Target item for actions"
      }
    ],
    "interfaces": [
      {
        "line": 30,
        "name": "ItemActionsMenuProps",
        "purpose": "Props for ItemActionsMenu component.",
        "structure": "item (ItemPublic): input - Item data for the row actions"
      }
    ],
    "language": "typescript",
    "lines": 61,
    "module": "Items/ItemActionsMenu",
    "path": "frontend/src/components/Items/ItemActionsMenu.tsx",
    "purpose": "Dropdown actions menu for item row operations (edit, delete).",
    "relationships": "Consumes: EditItem, DeleteItem components\nUsed by: Items table columns",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "./ItemActionsMenu",
        "@/client",
        "@/components/ui/button",
        "@/hooks/useCopyToClipboard",
        "@/lib/utils",
        "@tanstack/react-table",
        "lucide-react"
      ]
    },
    "file": "columns.tsx",
    "functions": [
      {
        "line": 29,
        "name": "CopyId",
        "purpose": "Inline component displaying an item ID with copy-to-clipboard button.",
        "relationships": "Consumes: useCopyToClipboard hook",
        "signature": "function CopyId({ id }: { id: string }) {",
        "structure": "id (string): input - Item ID to display and copy"
      }
    ],
    "language": "typescript",
    "lines": 106,
    "module": "Items/columns",
    "path": "frontend/src/components/Items/columns.tsx",
    "purpose": "Column definitions for the items data table.",
    "relationships": "Consumes: ItemActionsMenu component, ItemPublic type\nUsed by: Items page DataTable",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/components/ui/skeleton",
        "@/components/ui/table"
      ]
    },
    "file": "PendingItems.tsx",
    "functions": [
      {
        "line": 26,
        "name": "PendingItems",
        "purpose": "Renders 5 skeleton rows matching the items table column layout (ID, Title, Description, Actions).",
        "relationships": "Used by: Items page loading state",
        "signature": "() => (\n  <Table>\n    <TableHeader>\n      <TableRow>\n        <TableHead>ID</TableHead>\n        <TableHead>Title</TableHead>\n        <TableHead>Description</TableHead>\n        <TableHead>\n          <span className=\"sr-only\">Actions</span>\n        </TableHead>\n      </TableRow>\n    </TableHeader>\n    <TableBody>\n      {Array.from({ length: 5 }).map((_, index) => (\n        <TableRow key={index}>\n          <TableCell>\n            <Skeleton className=\"h-4 w-64 font-mono\" />\n          </TableCell>\n          <TableCell>\n            <Skeleton className=\"h-4 w-32\" />\n          </TableCell>\n          <TableCell>\n            <Skeleton className=\"h-4 w-48\" />\n          </TableCell>\n          <TableCell>\n            <div className=\"flex justify-end\">\n              <Skeleton className=\"size-8 rounded-md\" />\n            </div>\n          </TableCell>\n        </TableRow>\n      ))}\n    </TableBody>\n  </Table>\n)"
      }
    ],
    "language": "typescript",
    "lines": 62,
    "module": "Pending/PendingItems",
    "path": "frontend/src/components/Pending/PendingItems.tsx",
    "purpose": "Skeleton loading placeholder for the items table.",
    "relationships": "Used by: Items page during data fetch",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/components/ui/skeleton",
        "@/components/ui/table"
      ]
    },
    "file": "PendingUsers.tsx",
    "functions": [
      {
        "line": 26,
        "name": "PendingUsers",
        "purpose": "Renders 5 skeleton rows matching the users table column layout (Name, Email, Role, Status, Actions).",
        "relationships": "Used by: Admin users page loading state",
        "signature": "() => (\n  <Table>\n    <TableHeader>\n      <TableRow>\n        <TableHead>Full Name</TableHead>\n        <TableHead>Email</TableHead>\n        <TableHead>Role</TableHead>\n        <TableHead>Status</TableHead>\n        <TableHead>\n          <span className=\"sr-only\">Actions</span>\n        </TableHead>\n      </TableRow>\n    </TableHeader>\n    <TableBody>\n      {Array.from({ length: 5 }).map((_, index) => (\n        <TableRow key={index}>\n          <TableCell>\n            <Skeleton className=\"h-4 w-32\" />\n          </TableCell>\n          <TableCell>\n            <Skeleton className=\"h-4 w-40\" />\n          </TableCell>\n          <TableCell>\n            <Skeleton className=\"h-5 w-20 rounded-full\" />\n          </TableCell>\n          <TableCell>\n            <div className=\"flex items-center gap-2\">\n              <Skeleton className=\"size-2 rounded-full\" />\n              <Skeleton className=\"h-4 w-12\" />\n            </div>\n          </TableCell>\n          <TableCell>\n            <div className=\"flex justify-end\">\n              <Skeleton className=\"size-8 rounded-md\" />\n            </div>\n          </TableCell>\n        </TableRow>\n      ))}\n    </TableBody>\n  </Table>\n)"
      }
    ],
    "language": "typescript",
    "lines": 69,
    "module": "Pending/PendingUsers",
    "path": "frontend/src/components/Pending/PendingUsers.tsx",
    "purpose": "Skeleton loading placeholder for the users table.",
    "relationships": "Used by: Admin users page during data fetch",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "./Main",
        "./User",
        "@/components/Common/Appearance",
        "@/components/Common/Logo",
        "@/components/ui/sidebar",
        "@/hooks/useAuth",
        "lucide-react"
      ]
    },
    "file": "AppSidebar.tsx",
    "functions": [
      {
        "flow": "1. Determine nav items based on superuser status\n2. Render Logo in header, Main nav in content, Appearance + User in footer",
        "line": 45,
        "name": "AppSidebar",
        "purpose": "Collapsible sidebar with navigation items, appearance toggle, and user menu.",
        "relationships": "Consumes: useAuth (current user/superuser check), Main, User, SidebarAppearance, Logo\nUsed by: Authenticated app layout",
        "signature": "function AppSidebar() {",
        "structure": "baseItems: Dashboard and Items nav links\nAdmin link: Conditionally added for superusers"
      }
    ],
    "language": "typescript",
    "lines": 69,
    "module": "Sidebar/AppSidebar",
    "path": "frontend/src/components/Sidebar/AppSidebar.tsx",
    "purpose": "Main application sidebar with navigation, theme toggle, and user menu.",
    "relationships": "Consumes: Main, User, SidebarAppearance, Logo components; useAuth hook\nUsed by: Authenticated layout shell",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/components/ui/sidebar",
        "@tanstack/react-router",
        "lucide-react"
      ]
    },
    "file": "Main.tsx",
    "functions": [
      {
        "flow": "1. Determine current path from router state\n2. Render each item as SidebarMenuButton with active state\n3. Auto-close mobile sidebar on navigation",
        "line": 62,
        "name": "Main",
        "purpose": "Renders sidebar navigation menu with active route highlighting.",
        "relationships": "Consumes: TanStack Router (useRouterState), useSidebar context\nUsed by: AppSidebar content area",
        "signature": "function Main({ items }: MainProps) {",
        "structure": "items (Item[]): input - Navigation items with icon, title, path"
      }
    ],
    "interfaces": [
      {
        "line": 43,
        "name": "MainProps",
        "purpose": "Props for Main sidebar navigation component.",
        "structure": "items (Item[]): input - Navigation items to render"
      }
    ],
    "language": "typescript",
    "lines": 100,
    "module": "Sidebar/Main",
    "path": "frontend/src/components/Sidebar/Main.tsx",
    "purpose": "Primary navigation menu rendered inside the sidebar.",
    "relationships": "Consumes: TanStack Router for active route detection\nUsed by: AppSidebar",
    "type": "module",
    "types": [
      {
        "definition": "type Item = {\n  icon: LucideIcon\n  title: string\n  path: string\n}",
        "line": 31,
        "name": "Item"
      }
    ]
  },
  {
    "dependencies": {
      "imports": [
        "@/components/ui/avatar",
        "@/components/ui/dropdown-menu",
        "@/components/ui/sidebar",
        "@/hooks/useAuth",
        "@/utils",
        "@tanstack/react-router",
        "lucide-react"
      ]
    },
    "file": "User.tsx",
    "functions": [
      {
        "line": 51,
        "name": "UserInfo",
        "purpose": "Avatar with name and email display used in sidebar user menu.",
        "signature": "function UserInfo({ fullName, email }: UserInfoProps) {",
        "structure": "fullName (string): input - Displayed name, initials used for avatar\nemail (string): input - Displayed below name"
      },
      {
        "flow": "1. Render avatar trigger with user info\n2. Show dropdown with User Settings link and Log Out action\n3. Auto-close mobile sidebar on settings navigation",
        "line": 82,
        "name": "User",
        "purpose": "Sidebar user dropdown with avatar, settings navigation, and logout.",
        "relationships": "Consumes: useAuth (logout), useSidebar (mobile close), getInitials utility\nUsed by: AppSidebar footer",
        "signature": "function User({ user }: { user: any }) {",
        "structure": "user (any): input - Current user object (null renders nothing)"
      }
    ],
    "interfaces": [
      {
        "line": 39,
        "name": "UserInfoProps",
        "purpose": "Props for UserInfo display component.",
        "structure": "fullName (string): input - User's display name\nemail (string): input - User's email address"
      }
    ],
    "language": "typescript",
    "lines": 137,
    "module": "Sidebar/User",
    "path": "frontend/src/components/Sidebar/User.tsx",
    "purpose": "Sidebar user menu with avatar, settings link, and logout action.",
    "relationships": "Consumes: useAuth hook for logout, useSidebar for mobile handling\nUsed by: AppSidebar footer",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/client",
        "@/components/ui/form",
        "@/components/ui/loading-button",
        "@/components/ui/password-input",
        "@/hooks/useCustomToast",
        "@/utils",
        "@hookform/resolvers/zod",
        "@tanstack/react-query",
        "react-hook-form",
        "zod"
      ]
    },
    "file": "ChangePassword.tsx",
    "functions": [
      {
        "flow": "1. Render current password, new password, confirm password fields\n2. Validate password match and minimum length\n3. Call updatePasswordMe API on submit\n4. Show success/error toast and reset form",
        "line": 67,
        "name": "ChangePassword",
        "purpose": "Password change form with current, new, and confirm password fields.",
        "relationships": "Consumes: UsersService.updatePasswordMe API\nProduces: Success toast, form reset on success",
        "signature": "() => {\n  const { showSuccessToast, showErrorToast } = useCustomToast()\n  const form = useForm<FormData>({\n    resolver: zodResolver(formSchema),\n    mode: \"onSubmit\",\n    criteriaMode: \"all\",\n    defaultValues: {\n      current_password: \"\",\n      new_password: \"\",\n      confirm_password: \"\",\n    },\n  })\n\n  const mutation = useMutation({\n    mutationFn: (data: UpdatePassword) =>\n      UsersService.updatePasswordMe({ requestBody: data }),\n    onSuccess: () => {\n      showSuccessToast(\"Password updated successfully\")\n      form.reset()\n    },\n    onError: handleError.bind(showErrorToast),\n  })\n\n  const onSubmit = async (data: FormData) => {\n    mutation.mutate(data)\n  }\n\n  return (\n    <div className=\"max-w-md\">\n      <h3 className=\"text-lg font-semibold py-4\">Change Password</h3>\n      <Form {...form}>\n        <form\n          onSubmit={form.handleSubmit(onSubmit)}\n          className=\"flex flex-col gap-4\"\n        >\n          <FormField\n            control={form.control}\n            name=\"current_password\"\n            render={({ field, fieldState }) => (\n              <FormItem>\n                <FormLabel>Current Password</FormLabel>\n                <FormControl>\n                  <PasswordInput\n                    data-testid=\"current-password-input\"\n                    placeholder=\"\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\"\n                    aria-invalid={fieldState.invalid}\n                    {...field}\n                  />\n                </FormControl>\n                <FormMessage />\n              </FormItem>\n            )}\n          />\n\n          <FormField\n            control={form.control}\n            name=\"new_password\"\n            render={({ field, fieldState }) => (\n              <FormItem>\n                <FormLabel>New Password</FormLabel>\n                <FormControl>\n                  <PasswordInput\n                    data-testid=\"new-password-input\"\n                    placeholder=\"\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\"\n                    aria-invalid={fieldState.invalid}\n                    {...field}\n                  />\n                </FormControl>\n                <FormMessage />\n              </FormItem>\n            )}\n          />\n\n          <FormField\n            control={form.control}\n            name=\"confirm_password\"\n            render={({ field, fieldState }) => (\n              <FormItem>\n                <FormLabel>Confirm Password</FormLabel>\n                <FormControl>\n                  <PasswordInput\n                    data-testid=\"confirm-password-input\"\n                    placeholder=\"\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\"\n                    aria-invalid={fieldState.invalid}\n                    {...field}\n                  />\n                </FormControl>\n                <FormMessage />\n              </FormItem>\n            )}\n          />\n\n          <LoadingButton\n            type=\"submit\"\n            loading={mutation.isPending}\n            className=\"self-start\"\n          >\n            Update Password\n          </LoadingButton>\n        </form>\n      </Form>\n    </div>\n  )\n}",
        "structure": "formSchema (zod): Validates min 8 chars, password match"
      }
    ],
    "language": "typescript",
    "lines": 173,
    "module": "UserSettings/ChangePassword",
    "path": "frontend/src/components/UserSettings/ChangePassword.tsx",
    "purpose": "Form for changing the current user's password.",
    "relationships": "Consumes: UsersService.updatePasswordMe API\nUsed by: User settings page",
    "type": "module",
    "types": [
      {
        "definition": "type FormData = z.infer<typeof formSchema>",
        "line": 49,
        "name": "FormData"
      }
    ]
  },
  {
    "dependencies": {
      "imports": [
        "./DeleteConfirmation"
      ]
    },
    "file": "DeleteAccount.tsx",
    "functions": [
      {
        "line": 20,
        "name": "DeleteAccount",
        "purpose": "Destructive-styled card with account deletion warning and confirmation trigger.",
        "relationships": "Consumes: DeleteConfirmation dialog component\nUsed by: User settings page",
        "signature": "() => {\n  return (\n    <div className=\"max-w-md mt-4 rounded-lg border border-destructive/50 p-4\">\n      <h3 className=\"font-semibold text-destructive\">Delete Account</h3>\n      <p className=\"mt-1 text-sm text-muted-foreground\">\n        Permanently delete your account and all associated data.\n      </p>\n      <DeleteConfirmation />\n    </div>\n  )\n}"
      }
    ],
    "language": "typescript",
    "lines": 33,
    "module": "UserSettings/DeleteAccount",
    "path": "frontend/src/components/UserSettings/DeleteAccount.tsx",
    "purpose": "Danger zone section for account self-deletion.",
    "relationships": "Consumes: DeleteConfirmation component\nUsed by: User settings page",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/client",
        "@/components/ui/button",
        "@/components/ui/dialog",
        "@/components/ui/loading-button",
        "@/hooks/useAuth",
        "@/hooks/useCustomToast",
        "@/utils",
        "@tanstack/react-query",
        "react-hook-form"
      ]
    },
    "file": "DeleteConfirmation.tsx",
    "functions": [
      {
        "flow": "1. Open dialog via \"Delete Account\" trigger button\n2. Show permanent deletion warning\n3. Call deleteUserMe API on confirm\n4. Show success toast and trigger logout",
        "line": 44,
        "name": "DeleteConfirmation",
        "purpose": "Modal confirmation dialog for permanent account self-deletion.",
        "relationships": "Consumes: UsersService.deleteUserMe API, useAuth (logout)\nProduces: Account deletion, logout, invalidates \"currentUser\" query cache",
        "signature": "() => {\n  const queryClient = useQueryClient()\n  const { showSuccessToast, showErrorToast } = useCustomToast()\n  const { handleSubmit } = useForm()\n  const { logout } = useAuth()\n\n  const mutation = useMutation({\n    mutationFn: () => UsersService.deleteUserMe(),\n    onSuccess: () => {\n      showSuccessToast(\"Your account has been successfully deleted\")\n      logout()\n    },\n    onError: handleError.bind(showErrorToast),\n    onSettled: () => {\n      queryClient.invalidateQueries({ queryKey: [\"currentUser\"] })\n    },\n  })\n\n  const onSubmit = async () => {\n    mutation.mutate()\n  }\n\n  return (\n    <Dialog>\n      <DialogTrigger asChild>\n        <Button variant=\"destructive\" className=\"mt-3\">\n          Delete Account\n        </Button>\n      </DialogTrigger>\n      <DialogContent>\n        <form onSubmit={handleSubmit(onSubmit)}>\n          <DialogHeader>\n            <DialogTitle>Confirmation Required</DialogTitle>\n            <DialogDescription>\n              All your account data will be{\" \"}\n              <strong>permanently deleted.</strong> If you are sure, please\n              click <strong>\"Confirm\"</strong> to proceed. This action cannot be\n              undone.\n            </DialogDescription>\n          </DialogHeader>\n\n          <DialogFooter className=\"mt-4\">\n            <DialogClose asChild>\n              <Button variant=\"outline\" disabled={mutation.isPending}>\n                Cancel\n              </Button>\n            </DialogClose>\n            <LoadingButton\n              variant=\"destructive\"\n              type=\"submit\"\n              loading={mutation.isPending}\n            >\n              Delete\n            </LoadingButton>\n          </DialogFooter>\n        </form>\n      </DialogContent>\n    </Dialog>\n  )\n}"
      }
    ],
    "language": "typescript",
    "lines": 106,
    "module": "UserSettings/DeleteConfirmation",
    "path": "frontend/src/components/UserSettings/DeleteConfirmation.tsx",
    "purpose": "Confirmation dialog for self-deleting the current user's account.",
    "relationships": "Consumes: UsersService.deleteUserMe API, useAuth logout\nUsed by: DeleteAccount component",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/client",
        "@/components/ui/button",
        "@/components/ui/form",
        "@/components/ui/input",
        "@/components/ui/loading-button",
        "@/hooks/useAuth",
        "@/hooks/useCustomToast",
        "@/lib/utils",
        "@/utils",
        "@hookform/resolvers/zod",
        "@tanstack/react-query",
        "react",
        "react-hook-form",
        "zod"
      ]
    },
    "file": "UserInformation.tsx",
    "functions": [
      {
        "flow": "1. Display user info in read-only mode with Edit button\n2. Switch to editable inputs on Edit click\n3. Submit only changed fields to updateUserMe API\n4. Show success/error toast and return to read-only mode",
        "line": 58,
        "name": "UserInformation",
        "purpose": "Toggle-editable form displaying and updating current user's name and email.",
        "relationships": "Consumes: UsersService.updateUserMe API, useAuth (current user data)\nProduces: Updated user profile, success toast, invalidates all query caches",
        "signature": "() => {\n  const queryClient = useQueryClient()\n  const { showSuccessToast, showErrorToast } = useCustomToast()\n  const [editMode, setEditMode] = useState(false)\n  const { user: currentUser } = useAuth()\n\n  const form = useForm<FormData>({\n    resolver: zodResolver(formSchema),\n    mode: \"onBlur\",\n    criteriaMode: \"all\",\n    defaultValues: {\n      full_name: currentUser?.full_name ?? undefined,\n      email: currentUser?.email,\n    },\n  })\n\n  const toggleEditMode = () => {\n    setEditMode(!editMode)\n  }\n\n  const mutation = useMutation({\n    mutationFn: (data: UserUpdateMe) =>\n      UsersService.updateUserMe({ requestBody: data }),\n    onSuccess: () => {\n      showSuccessToast(\"User updated successfully\")\n      toggleEditMode()\n    },\n    onError: handleError.bind(showErrorToast),\n    onSettled: () => {\n      queryClient.invalidateQueries()\n    },\n  })\n\n  const onSubmit = (data: FormData) => {\n    const updateData: UserUpdateMe = {}\n\n    // only include fields that have changed\n    if (data.full_name !== currentUser?.full_name) {\n      updateData.full_name = data.full_name\n    }\n    if (data.email !== currentUser?.email) {\n      updateData.email = data.email\n    }\n\n    mutation.mutate(updateData)\n  }\n\n  const onCancel = () => {\n    form.reset()\n    toggleEditMode()\n  }\n\n  return (\n    <div className=\"max-w-md\">\n      <h3 className=\"text-lg font-semibold py-4\">User Information</h3>\n      <Form {...form}>\n        <form\n          onSubmit={form.handleSubmit(onSubmit)}\n          className=\"flex flex-col gap-4\"\n        >\n          <FormField\n            control={form.control}\n            name=\"full_name\"\n            render={({ field }) =>\n              editMode ? (\n                <FormItem>\n                  <FormLabel>Full name</FormLabel>\n                  <FormControl>\n                    <Input type=\"text\" {...field} />\n                  </FormControl>\n                  <FormMessage />\n                </FormItem>\n              ) : (\n                <FormItem>\n                  <FormLabel>Full name</FormLabel>\n                  <p\n                    className={cn(\n                      \"py-2 truncate max-w-sm\",\n                      !field.value && \"text-muted-foreground\",\n                    )}\n                  >\n                    {field.value || \"N/A\"}\n                  </p>\n                </FormItem>\n              )\n            }\n          />\n\n          <FormField\n            control={form.control}\n            name=\"email\"\n            render={({ field }) =>\n              editMode ? (\n                <FormItem>\n                  <FormLabel>Email</FormLabel>\n                  <FormControl>\n                    <Input type=\"email\" {...field} />\n                  </FormControl>\n                  <FormMessage />\n                </FormItem>\n              ) : (\n                <FormItem>\n                  <FormLabel>Email</FormLabel>\n                  <p className=\"py-2 truncate max-w-sm\">{field.value}</p>\n                </FormItem>\n              )\n            }\n          />\n\n          <div className=\"flex gap-3\">\n            {editMode ? (\n              <>\n                <LoadingButton\n                  type=\"submit\"\n                  loading={mutation.isPending}\n                  disabled={!form.formState.isDirty}\n                >\n                  Save\n                </LoadingButton>\n                <Button\n                  type=\"button\"\n                  variant=\"outline\"\n                  onClick={onCancel}\n                  disabled={mutation.isPending}\n                >\n                  Cancel\n                </Button>\n              </>\n            ) : (\n              <Button type=\"button\" onClick={toggleEditMode}>\n                Edit\n              </Button>\n            )}\n          </div>\n        </form>\n      </Form>\n    </div>\n  )\n}",
        "structure": "editMode (boolean): internal - Toggles between read-only and edit views\nformSchema (zod): Validates email format, optional name (max 30 chars)"
      }
    ],
    "language": "typescript",
    "lines": 199,
    "module": "UserSettings/UserInformation",
    "path": "frontend/src/components/UserSettings/UserInformation.tsx",
    "purpose": "Editable display of current user's profile information (name, email).",
    "relationships": "Consumes: UsersService.updateUserMe API, useAuth hook\nUsed by: User settings page",
    "type": "module",
    "types": [
      {
        "definition": "type FormData = z.infer<typeof formSchema>",
        "line": 39,
        "name": "FormData"
      }
    ]
  },
  {
    "dependencies": {
      "imports": [
        "react"
      ]
    },
    "file": "theme-provider.tsx",
    "functions": [
      {
        "flow": "1. Read persisted theme from localStorage (or use default)\n2. Apply theme class to document root element\n3. Listen for system color-scheme changes when theme is \"system\"\n4. Expose theme, resolvedTheme, and setTheme via context",
        "line": 75,
        "name": "ThemeProvider",
        "purpose": "Context provider managing theme state, localStorage persistence, and system preference detection.",
        "relationships": "Produces: ThemeProviderContext consumed by useTheme hook\nUsed by: App root",
        "signature": "function ThemeProvider({\n  children,\n  defaultTheme = \"system\",\n  storageKey = \"vite-ui-theme\",\n  ...props\n}: ThemeProviderProps) {",
        "structure": "defaultTheme (Theme): input - Fallback theme, defaults to \"system\"\nstorageKey (string): input - localStorage key, defaults to \"vite-ui-theme\""
      },
      {
        "line": 160,
        "name": "useTheme",
        "purpose": "Hook to access theme context (theme, resolvedTheme, setTheme).",
        "raises": "Error if used outside ThemeProvider",
        "relationships": "Consumes: ThemeProviderContext",
        "signature": "() => {\n  const context = useContext(ThemeProviderContext)\n\n  if (context === undefined)\n    throw new Error(\"useTheme must be used within a ThemeProvider\")\n\n  return context\n}"
      }
    ],
    "language": "typescript",
    "lines": 168,
    "module": "theme-provider",
    "path": "frontend/src/components/theme-provider.tsx",
    "purpose": "React context provider for application theme management (dark/light/system).",
    "relationships": "Consumed by: Appearance, SidebarAppearance, Logo components via useTheme hook\nUsed by: App root component",
    "type": "module",
    "types": [
      {
        "definition": "type Theme = \"dark\" | \"light\" | \"system\"",
        "line": 20,
        "name": "Theme"
      },
      {
        "definition": "type ThemeProviderProps = {\n  children: React.ReactNode\n  defaultTheme?: Theme\n  storageKey?: string\n}",
        "line": 30,
        "name": "ThemeProviderProps"
      },
      {
        "definition": "type ThemeProviderState = {\n  theme: Theme\n  resolvedTheme: \"dark\" | \"light\"\n  setTheme: (theme: Theme) => void\n}",
        "line": 44,
        "name": "ThemeProviderState"
      }
    ]
  },
  {
    "dependencies": {
      "imports": [
        "@/lib/utils",
        "class-variance-authority",
        "react"
      ]
    },
    "file": "alert.tsx",
    "functions": [
      {
        "line": 22,
        "name": "Alert",
        "signature": "function Alert({\n  className,\n  variant,\n  ...props\n}: React.ComponentProps<\"div\"> & VariantProps<typeof alertVariants>) {"
      },
      {
        "line": 37,
        "name": "AlertTitle",
        "signature": "function AlertTitle({ className, ...props }: React.ComponentProps<\"div\">) {"
      },
      {
        "line": 50,
        "name": "AlertDescription",
        "signature": "function AlertDescription({\n  className,\n  ...props\n}: React.ComponentProps<\"div\">) {"
      }
    ],
    "language": "typescript",
    "lines": 67,
    "path": "frontend/src/components/ui/alert.tsx",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/lib/utils",
        "@radix-ui/react-avatar",
        "react"
      ]
    },
    "file": "avatar.tsx",
    "functions": [
      {
        "line": 6,
        "name": "Avatar",
        "signature": "function Avatar({\n  className,\n  ...props\n}: React.ComponentProps<typeof AvatarPrimitive.Root>) {"
      },
      {
        "line": 22,
        "name": "AvatarImage",
        "signature": "function AvatarImage({\n  className,\n  ...props\n}: React.ComponentProps<typeof AvatarPrimitive.Image>) {"
      },
      {
        "line": 35,
        "name": "AvatarFallback",
        "signature": "function AvatarFallback({\n  className,\n  ...props\n}: React.ComponentProps<typeof AvatarPrimitive.Fallback>) {"
      }
    ],
    "language": "typescript",
    "lines": 52,
    "path": "frontend/src/components/ui/avatar.tsx",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/lib/utils",
        "@radix-ui/react-slot",
        "class-variance-authority",
        "react"
      ]
    },
    "file": "badge.tsx",
    "functions": [
      {
        "line": 28,
        "name": "Badge",
        "signature": "function Badge({\n  className,\n  variant,\n  asChild = false,\n  ...props\n}: React.ComponentProps<\"span\"> &\n  VariantProps<typeof badgeVariants> & { asChild?: boolean }) {"
      }
    ],
    "language": "typescript",
    "lines": 47,
    "path": "frontend/src/components/ui/badge.tsx",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/components/ui/separator",
        "@/lib/utils",
        "@radix-ui/react-slot",
        "class-variance-authority"
      ]
    },
    "file": "button-group.tsx",
    "functions": [
      {
        "line": 24,
        "name": "ButtonGroup",
        "signature": "function ButtonGroup({\n  className,\n  orientation,\n  ...props\n}: React.ComponentProps<\"div\"> & VariantProps<typeof buttonGroupVariants>) {"
      },
      {
        "line": 40,
        "name": "ButtonGroupText",
        "signature": "function ButtonGroupText({\n  className,\n  asChild = false,\n  ...props\n}: React.ComponentProps<\"div\"> & {\n  asChild?: boolean\n}) {"
      },
      {
        "line": 60,
        "name": "ButtonGroupSeparator",
        "signature": "function ButtonGroupSeparator({\n  className,\n  orientation = \"vertical\",\n  ...props\n}: React.ComponentProps<typeof Separator>) {"
      }
    ],
    "language": "typescript",
    "lines": 84,
    "path": "frontend/src/components/ui/button-group.tsx",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/lib/utils",
        "@radix-ui/react-slot",
        "class-variance-authority",
        "react"
      ]
    },
    "file": "button.tsx",
    "functions": [
      {
        "line": 39,
        "name": "Button",
        "signature": "function Button({\n  className,\n  variant,\n  size,\n  asChild = false,\n  ...props\n}: React.ComponentProps<\"button\"> &\n  VariantProps<typeof buttonVariants> & {\n    asChild?: boolean\n  }) {"
      }
    ],
    "language": "typescript",
    "lines": 61,
    "path": "frontend/src/components/ui/button.tsx",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/lib/utils",
        "react"
      ]
    },
    "file": "card.tsx",
    "functions": [
      {
        "line": 5,
        "name": "Card",
        "signature": "function Card({ className, ...props }: React.ComponentProps<\"div\">) {"
      },
      {
        "line": 18,
        "name": "CardHeader",
        "signature": "function CardHeader({ className, ...props }: React.ComponentProps<\"div\">) {"
      },
      {
        "line": 31,
        "name": "CardTitle",
        "signature": "function CardTitle({ className, ...props }: React.ComponentProps<\"div\">) {"
      },
      {
        "line": 41,
        "name": "CardDescription",
        "signature": "function CardDescription({ className, ...props }: React.ComponentProps<\"div\">) {"
      },
      {
        "line": 51,
        "name": "CardAction",
        "signature": "function CardAction({ className, ...props }: React.ComponentProps<\"div\">) {"
      },
      {
        "line": 64,
        "name": "CardContent",
        "signature": "function CardContent({ className, ...props }: React.ComponentProps<\"div\">) {"
      },
      {
        "line": 74,
        "name": "CardFooter",
        "signature": "function CardFooter({ className, ...props }: React.ComponentProps<\"div\">) {"
      }
    ],
    "language": "typescript",
    "lines": 93,
    "path": "frontend/src/components/ui/card.tsx",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/lib/utils",
        "@radix-ui/react-checkbox",
        "lucide-react",
        "react"
      ]
    },
    "file": "checkbox.tsx",
    "functions": [
      {
        "line": 7,
        "name": "Checkbox",
        "signature": "function Checkbox({\n  className,\n  ...props\n}: React.ComponentProps<typeof CheckboxPrimitive.Root>) {"
      }
    ],
    "language": "typescript",
    "lines": 31,
    "path": "frontend/src/components/ui/checkbox.tsx",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/lib/utils",
        "@radix-ui/react-dialog",
        "lucide-react",
        "react"
      ]
    },
    "file": "dialog.tsx",
    "functions": [
      {
        "line": 7,
        "name": "Dialog",
        "signature": "function Dialog({\n  ...props\n}: React.ComponentProps<typeof DialogPrimitive.Root>) {"
      },
      {
        "line": 13,
        "name": "DialogTrigger",
        "signature": "function DialogTrigger({\n  ...props\n}: React.ComponentProps<typeof DialogPrimitive.Trigger>) {"
      },
      {
        "line": 19,
        "name": "DialogPortal",
        "signature": "function DialogPortal({\n  ...props\n}: React.ComponentProps<typeof DialogPrimitive.Portal>) {"
      },
      {
        "line": 25,
        "name": "DialogClose",
        "signature": "function DialogClose({\n  ...props\n}: React.ComponentProps<typeof DialogPrimitive.Close>) {"
      },
      {
        "line": 31,
        "name": "DialogOverlay",
        "signature": "function DialogOverlay({\n  className,\n  ...props\n}: React.ComponentProps<typeof DialogPrimitive.Overlay>) {"
      },
      {
        "line": 47,
        "name": "DialogContent",
        "signature": "function DialogContent({\n  className,\n  children,\n  showCloseButton = true,\n  ...props\n}: React.ComponentProps<typeof DialogPrimitive.Content> & {\n  showCloseButton?: boolean\n}) {"
      },
      {
        "line": 81,
        "name": "DialogHeader",
        "signature": "function DialogHeader({ className, ...props }: React.ComponentProps<\"div\">) {"
      },
      {
        "line": 91,
        "name": "DialogFooter",
        "signature": "function DialogFooter({ className, ...props }: React.ComponentProps<\"div\">) {"
      },
      {
        "line": 104,
        "name": "DialogTitle",
        "signature": "function DialogTitle({\n  className,\n  ...props\n}: React.ComponentProps<typeof DialogPrimitive.Title>) {"
      },
      {
        "line": 117,
        "name": "DialogDescription",
        "signature": "function DialogDescription({\n  className,\n  ...props\n}: React.ComponentProps<typeof DialogPrimitive.Description>) {"
      }
    ],
    "language": "typescript",
    "lines": 142,
    "path": "frontend/src/components/ui/dialog.tsx",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/lib/utils",
        "@radix-ui/react-dropdown-menu",
        "lucide-react",
        "react"
      ]
    },
    "file": "dropdown-menu.tsx",
    "functions": [
      {
        "line": 9,
        "name": "DropdownMenu",
        "signature": "function DropdownMenu({\n  ...props\n}: React.ComponentProps<typeof DropdownMenuPrimitive.Root>) {"
      },
      {
        "line": 15,
        "name": "DropdownMenuPortal",
        "signature": "function DropdownMenuPortal({\n  ...props\n}: React.ComponentProps<typeof DropdownMenuPrimitive.Portal>) {"
      },
      {
        "line": 23,
        "name": "DropdownMenuTrigger",
        "signature": "function DropdownMenuTrigger({\n  ...props\n}: React.ComponentProps<typeof DropdownMenuPrimitive.Trigger>) {"
      },
      {
        "line": 34,
        "name": "DropdownMenuContent",
        "signature": "function DropdownMenuContent({\n  className,\n  sideOffset = 4,\n  ...props\n}: React.ComponentProps<typeof DropdownMenuPrimitive.Content>) {"
      },
      {
        "line": 54,
        "name": "DropdownMenuGroup",
        "signature": "function DropdownMenuGroup({\n  ...props\n}: React.ComponentProps<typeof DropdownMenuPrimitive.Group>) {"
      },
      {
        "line": 62,
        "name": "DropdownMenuItem",
        "signature": "function DropdownMenuItem({\n  className,\n  inset,\n  variant = \"default\",\n  ...props\n}: React.ComponentProps<typeof DropdownMenuPrimitive.Item> & {\n  inset?: boolean\n  variant?: \"default\" | \"destructive\"\n}) {"
      },
      {
        "line": 85,
        "name": "DropdownMenuCheckboxItem",
        "signature": "function DropdownMenuCheckboxItem({\n  className,\n  children,\n  checked,\n  ...props\n}: React.ComponentProps<typeof DropdownMenuPrimitive.CheckboxItem>) {"
      },
      {
        "line": 111,
        "name": "DropdownMenuRadioGroup",
        "signature": "function DropdownMenuRadioGroup({\n  ...props\n}: React.ComponentProps<typeof DropdownMenuPrimitive.RadioGroup>) {"
      },
      {
        "line": 122,
        "name": "DropdownMenuRadioItem",
        "signature": "function DropdownMenuRadioItem({\n  className,\n  children,\n  ...props\n}: React.ComponentProps<typeof DropdownMenuPrimitive.RadioItem>) {"
      },
      {
        "line": 146,
        "name": "DropdownMenuLabel",
        "signature": "function DropdownMenuLabel({\n  className,\n  inset,\n  ...props\n}: React.ComponentProps<typeof DropdownMenuPrimitive.Label> & {\n  inset?: boolean\n}) {"
      },
      {
        "line": 166,
        "name": "DropdownMenuSeparator",
        "signature": "function DropdownMenuSeparator({\n  className,\n  ...props\n}: React.ComponentProps<typeof DropdownMenuPrimitive.Separator>) {"
      },
      {
        "line": 179,
        "name": "DropdownMenuShortcut",
        "signature": "function DropdownMenuShortcut({\n  className,\n  ...props\n}: React.ComponentProps<\"span\">) {"
      },
      {
        "line": 195,
        "name": "DropdownMenuSub",
        "signature": "function DropdownMenuSub({\n  ...props\n}: React.ComponentProps<typeof DropdownMenuPrimitive.Sub>) {"
      },
      {
        "line": 201,
        "name": "DropdownMenuSubTrigger",
        "signature": "function DropdownMenuSubTrigger({\n  className,\n  inset,\n  children,\n  ...props\n}: React.ComponentProps<typeof DropdownMenuPrimitive.SubTrigger> & {\n  inset?: boolean\n}) {"
      },
      {
        "line": 225,
        "name": "DropdownMenuSubContent",
        "signature": "function DropdownMenuSubContent({\n  className,\n  ...props\n}: React.ComponentProps<typeof DropdownMenuPrimitive.SubContent>) {"
      }
    ],
    "language": "typescript",
    "lines": 258,
    "path": "frontend/src/components/ui/dropdown-menu.tsx",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/components/ui/label",
        "@/lib/utils",
        "@radix-ui/react-label",
        "@radix-ui/react-slot",
        "react",
        "react-hook-form"
      ]
    },
    "file": "form.tsx",
    "functions": [
      {
        "line": 30,
        "name": "FormField",
        "signature": "<\n  TFieldValues extends FieldValues = FieldValues,\n  TName extends FieldPath<TFieldValues> = FieldPath<TFieldValues>,\n>({\n  ...props\n}: ControllerProps<TFieldValues, TName>) => {\n  return (\n    <FormFieldContext.Provider value={{ name: props.name }}>\n      <Controller {...props} />\n    </FormFieldContext.Provider>\n  )\n}"
      },
      {
        "line": 43,
        "name": "useFormField",
        "signature": "() => {\n  const fieldContext = React.useContext(FormFieldContext)\n  const itemContext = React.useContext(FormItemContext)\n  const { getFieldState } = useFormContext()\n  const formState = useFormState({ name: fieldContext.name })\n  const fieldState = getFieldState(fieldContext.name, formState)\n\n  if (!fieldContext) {\n    throw new Error(\"useFormField should be used within <FormField>\")\n  }\n\n  const { id } = itemContext\n\n  return {\n    id,\n    name: fieldContext.name,\n    formItemId: `${id}-form-item`,\n    formDescriptionId: `${id}-form-item-description`,\n    formMessageId: `${id}-form-item-message`,\n    ...fieldState,\n  }\n}"
      },
      {
        "line": 74,
        "name": "FormItem",
        "signature": "function FormItem({ className, ...props }: React.ComponentProps<\"div\">) {"
      },
      {
        "line": 88,
        "name": "FormLabel",
        "signature": "function FormLabel({\n  className,\n  ...props\n}: React.ComponentProps<typeof LabelPrimitive.Root>) {"
      },
      {
        "line": 105,
        "name": "FormControl",
        "signature": "function FormControl({ ...props }: React.ComponentProps<typeof Slot>) {"
      },
      {
        "line": 123,
        "name": "FormDescription",
        "signature": "function FormDescription({ className, ...props }: React.ComponentProps<\"p\">) {"
      },
      {
        "line": 136,
        "name": "FormMessage",
        "signature": "function FormMessage({ className, ...props }: React.ComponentProps<\"p\">) {"
      }
    ],
    "language": "typescript",
    "lines": 166,
    "path": "frontend/src/components/ui/form.tsx",
    "type": "module",
    "types": [
      {
        "definition": "type FormFieldContextValue<\n  TFieldValues extends FieldValues = FieldValues,\n  TName extends FieldPath<TFieldValues> = FieldPath<TFieldValues>,\n> = {\n  name: TName\n}",
        "line": 19,
        "name": "FormFieldContextValue"
      },
      {
        "definition": "type FormItemContextValue = {\n  id: string\n}",
        "line": 66,
        "name": "FormItemContextValue"
      }
    ]
  },
  {
    "dependencies": {
      "imports": [
        "@/lib/utils",
        "react"
      ]
    },
    "file": "input.tsx",
    "functions": [
      {
        "line": 5,
        "name": "Input",
        "signature": "function Input({ className, type, ...props }: React.ComponentProps<\"input\">) {"
      }
    ],
    "language": "typescript",
    "lines": 22,
    "path": "frontend/src/components/ui/input.tsx",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/lib/utils",
        "@radix-ui/react-label",
        "react"
      ]
    },
    "file": "label.tsx",
    "functions": [
      {
        "line": 8,
        "name": "Label",
        "signature": "function Label({\n  className,\n  ...props\n}: React.ComponentProps<typeof LabelPrimitive.Root>) {"
      }
    ],
    "language": "typescript",
    "lines": 25,
    "path": "frontend/src/components/ui/label.tsx",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/lib/utils",
        "@radix-ui/react-slot",
        "class-variance-authority",
        "lucide-react"
      ]
    },
    "file": "loading-button.tsx",
    "functions": [
      {
        "line": 44,
        "name": "LoadingButton",
        "signature": "function LoadingButton({\n  className,\n  loading = false,\n  children,\n  disabled,\n  variant,\n  size,\n  asChild = false,\n  ...props\n}: ButtonProps) {"
      }
    ],
    "interfaces": [
      {
        "line": 37,
        "name": "ButtonProps"
      }
    ],
    "language": "typescript",
    "lines": 68,
    "path": "frontend/src/components/ui/loading-button.tsx",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/components/ui/button",
        "@/lib/utils",
        "lucide-react",
        "react"
      ]
    },
    "file": "pagination.tsx",
    "functions": [
      {
        "line": 11,
        "name": "Pagination",
        "signature": "function Pagination({ className, ...props }: React.ComponentProps<\"nav\">) {"
      },
      {
        "line": 23,
        "name": "PaginationContent",
        "signature": "function PaginationContent({\n  className,\n  ...props\n}: React.ComponentProps<\"ul\">) {"
      },
      {
        "line": 36,
        "name": "PaginationItem",
        "signature": "function PaginationItem({ ...props }: React.ComponentProps<\"li\">) {"
      },
      {
        "line": 45,
        "name": "PaginationLink",
        "signature": "function PaginationLink({\n  className,\n  isActive,\n  size = \"icon\",\n  ...props\n}: PaginationLinkProps) {"
      },
      {
        "line": 68,
        "name": "PaginationPrevious",
        "signature": "function PaginationPrevious({\n  className,\n  ...props\n}: React.ComponentProps<typeof PaginationLink>) {"
      },
      {
        "line": 85,
        "name": "PaginationNext",
        "signature": "function PaginationNext({\n  className,\n  ...props\n}: React.ComponentProps<typeof PaginationLink>) {"
      },
      {
        "line": 102,
        "name": "PaginationEllipsis",
        "signature": "function PaginationEllipsis({\n  className,\n  ...props\n}: React.ComponentProps<\"span\">) {"
      }
    ],
    "language": "typescript",
    "lines": 128,
    "path": "frontend/src/components/ui/pagination.tsx",
    "type": "module",
    "types": [
      {
        "definition": "type PaginationLinkProps = {\n  isActive?: boolean\n} & Pick<React.ComponentProps<typeof Button>, \"size\"> &\n  React.ComponentProps<\"a\">",
        "line": 40,
        "name": "PaginationLinkProps"
      }
    ]
  },
  {
    "dependencies": {
      "imports": [
        "./button",
        "@/lib/utils",
        "lucide-react",
        "react"
      ]
    },
    "file": "password-input.tsx",
    "interfaces": [
      {
        "line": 7,
        "name": "PasswordInputProps"
      }
    ],
    "language": "typescript",
    "lines": 52,
    "path": "frontend/src/components/ui/password-input.tsx",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/lib/utils",
        "@radix-ui/react-select",
        "lucide-react",
        "react"
      ]
    },
    "file": "select.tsx",
    "functions": [
      {
        "line": 7,
        "name": "Select",
        "signature": "function Select({\n  ...props\n}: React.ComponentProps<typeof SelectPrimitive.Root>) {"
      },
      {
        "line": 13,
        "name": "SelectGroup",
        "signature": "function SelectGroup({\n  ...props\n}: React.ComponentProps<typeof SelectPrimitive.Group>) {"
      },
      {
        "line": 19,
        "name": "SelectValue",
        "signature": "function SelectValue({\n  ...props\n}: React.ComponentProps<typeof SelectPrimitive.Value>) {"
      },
      {
        "line": 25,
        "name": "SelectTrigger",
        "signature": "function SelectTrigger({\n  className,\n  size = \"default\",\n  children,\n  ...props\n}: React.ComponentProps<typeof SelectPrimitive.Trigger> & {\n  size?: \"sm\" | \"default\"\n}) {"
      },
      {
        "line": 51,
        "name": "SelectContent",
        "signature": "function SelectContent({\n  className,\n  children,\n  position = \"popper\",\n  align = \"center\",\n  ...props\n}: React.ComponentProps<typeof SelectPrimitive.Content>) {"
      },
      {
        "line": 88,
        "name": "SelectLabel",
        "signature": "function SelectLabel({\n  className,\n  ...props\n}: React.ComponentProps<typeof SelectPrimitive.Label>) {"
      },
      {
        "line": 101,
        "name": "SelectItem",
        "signature": "function SelectItem({\n  className,\n  children,\n  ...props\n}: React.ComponentProps<typeof SelectPrimitive.Item>) {"
      },
      {
        "line": 125,
        "name": "SelectSeparator",
        "signature": "function SelectSeparator({\n  className,\n  ...props\n}: React.ComponentProps<typeof SelectPrimitive.Separator>) {"
      },
      {
        "line": 138,
        "name": "SelectScrollUpButton",
        "signature": "function SelectScrollUpButton({\n  className,\n  ...props\n}: React.ComponentProps<typeof SelectPrimitive.ScrollUpButton>) {"
      },
      {
        "line": 156,
        "name": "SelectScrollDownButton",
        "signature": "function SelectScrollDownButton({\n  className,\n  ...props\n}: React.ComponentProps<typeof SelectPrimitive.ScrollDownButton>) {"
      }
    ],
    "language": "typescript",
    "lines": 186,
    "path": "frontend/src/components/ui/select.tsx",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/lib/utils",
        "@radix-ui/react-separator",
        "react"
      ]
    },
    "file": "separator.tsx",
    "functions": [
      {
        "line": 6,
        "name": "Separator",
        "signature": "function Separator({\n  className,\n  orientation = \"horizontal\",\n  decorative = true,\n  ...props\n}: React.ComponentProps<typeof SeparatorPrimitive.Root>) {"
      }
    ],
    "language": "typescript",
    "lines": 27,
    "path": "frontend/src/components/ui/separator.tsx",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/lib/utils",
        "@radix-ui/react-dialog",
        "lucide-react",
        "react"
      ]
    },
    "file": "sheet.tsx",
    "functions": [
      {
        "line": 9,
        "name": "Sheet",
        "signature": "function Sheet({ ...props }: React.ComponentProps<typeof SheetPrimitive.Root>) {"
      },
      {
        "line": 13,
        "name": "SheetTrigger",
        "signature": "function SheetTrigger({\n  ...props\n}: React.ComponentProps<typeof SheetPrimitive.Trigger>) {"
      },
      {
        "line": 19,
        "name": "SheetClose",
        "signature": "function SheetClose({\n  ...props\n}: React.ComponentProps<typeof SheetPrimitive.Close>) {"
      },
      {
        "line": 25,
        "name": "SheetPortal",
        "signature": "function SheetPortal({\n  ...props\n}: React.ComponentProps<typeof SheetPrimitive.Portal>) {"
      },
      {
        "line": 31,
        "name": "SheetOverlay",
        "signature": "function SheetOverlay({\n  className,\n  ...props\n}: React.ComponentProps<typeof SheetPrimitive.Overlay>) {"
      },
      {
        "line": 47,
        "name": "SheetContent",
        "signature": "function SheetContent({\n  className,\n  children,\n  side = \"right\",\n  ...props\n}: React.ComponentProps<typeof SheetPrimitive.Content> & {\n  side?: \"top\" | \"right\" | \"bottom\" | \"left\"\n}) {"
      },
      {
        "line": 84,
        "name": "SheetHeader",
        "signature": "function SheetHeader({ className, ...props }: React.ComponentProps<\"div\">) {"
      },
      {
        "line": 94,
        "name": "SheetFooter",
        "signature": "function SheetFooter({ className, ...props }: React.ComponentProps<\"div\">) {"
      },
      {
        "line": 104,
        "name": "SheetTitle",
        "signature": "function SheetTitle({\n  className,\n  ...props\n}: React.ComponentProps<typeof SheetPrimitive.Title>) {"
      },
      {
        "line": 117,
        "name": "SheetDescription",
        "signature": "function SheetDescription({\n  className,\n  ...props\n}: React.ComponentProps<typeof SheetPrimitive.Description>) {"
      }
    ],
    "language": "typescript",
    "lines": 140,
    "path": "frontend/src/components/ui/sheet.tsx",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/components/ui/button",
        "@/components/ui/input",
        "@/components/ui/separator",
        "@/components/ui/sheet",
        "@/components/ui/skeleton",
        "@/components/ui/tooltip",
        "@/hooks/useMobile",
        "@/lib/utils",
        "@radix-ui/react-slot",
        "class-variance-authority",
        "lucide-react",
        "react"
      ]
    },
    "file": "sidebar.tsx",
    "functions": [
      {
        "line": 45,
        "name": "useSidebar",
        "signature": "function useSidebar() {"
      },
      {
        "line": 54,
        "name": "SidebarProvider",
        "signature": "function SidebarProvider({\n  defaultOpen = true,\n  open: openProp,\n  onOpenChange: setOpenProp,\n  className,\n  style,\n  children,\n  ...props\n}: React.ComponentProps<\"div\"> & {\n  defaultOpen?: boolean\n  open?: boolean\n  onOpenChange?: (open: boolean) => void\n}) {"
      },
      {
        "line": 70,
        "name": "getInitialOpen",
        "signature": "() => {\n    if (typeof document === \"undefined\") return defaultOpen\n\n    const cookie = document.cookie\n      .split(\"; \")\n      .find((c) => c.startsWith(`${SIDEBAR_COOKIE_NAME}=`))\n\n    if (!cookie) return defaultOpen\n\n    return cookie.split(\"=\")[1] === \"true\"\n  }"
      },
      {
        "line": 108,
        "name": "handleKeyDown",
        "parameters": [
          {
            "name": "event",
            "type": "KeyboardEvent"
          }
        ],
        "signature": "(event: KeyboardEvent) => {\n      if (\n        event.key === SIDEBAR_KEYBOARD_SHORTCUT &&\n        (event.metaKey || event.ctrlKey)\n      ) {\n        event.preventDefault()\n        toggleSidebar()\n      }\n    }"
      },
      {
        "line": 164,
        "name": "Sidebar",
        "signature": "function Sidebar({\n  side = \"left\",\n  variant = \"sidebar\",\n  collapsible = \"offcanvas\",\n  className,\n  children,\n  ...props\n}: React.ComponentProps<\"div\"> & {\n  side?: \"left\" | \"right\"\n  variant?: \"sidebar\" | \"floating\" | \"inset\"\n  collapsible?: \"offcanvas\" | \"icon\" | \"none\"\n}) {"
      },
      {
        "line": 266,
        "name": "SidebarTrigger",
        "signature": "function SidebarTrigger({\n  className,\n  onClick,\n  ...props\n}: React.ComponentProps<typeof Button>) {"
      },
      {
        "line": 293,
        "name": "SidebarRail",
        "signature": "function SidebarRail({ className, ...props }: React.ComponentProps<\"button\">) {"
      },
      {
        "line": 318,
        "name": "SidebarInset",
        "signature": "function SidebarInset({ className, ...props }: React.ComponentProps<\"main\">) {"
      },
      {
        "line": 332,
        "name": "SidebarInput",
        "signature": "function SidebarInput({\n  className,\n  ...props\n}: React.ComponentProps<typeof Input>) {"
      },
      {
        "line": 346,
        "name": "SidebarHeader",
        "signature": "function SidebarHeader({ className, ...props }: React.ComponentProps<\"div\">) {"
      },
      {
        "line": 357,
        "name": "SidebarFooter",
        "signature": "function SidebarFooter({ className, ...props }: React.ComponentProps<\"div\">) {"
      },
      {
        "line": 368,
        "name": "SidebarSeparator",
        "signature": "function SidebarSeparator({\n  className,\n  ...props\n}: React.ComponentProps<typeof Separator>) {"
      },
      {
        "line": 382,
        "name": "SidebarContent",
        "signature": "function SidebarContent({ className, ...props }: React.ComponentProps<\"div\">) {"
      },
      {
        "line": 396,
        "name": "SidebarGroup",
        "signature": "function SidebarGroup({ className, ...props }: React.ComponentProps<\"div\">) {"
      },
      {
        "line": 407,
        "name": "SidebarGroupLabel",
        "signature": "function SidebarGroupLabel({\n  className,\n  asChild = false,\n  ...props\n}: React.ComponentProps<\"div\"> & { asChild?: boolean }) {"
      },
      {
        "line": 428,
        "name": "SidebarGroupAction",
        "signature": "function SidebarGroupAction({\n  className,\n  asChild = false,\n  ...props\n}: React.ComponentProps<\"button\"> & { asChild?: boolean }) {"
      },
      {
        "line": 451,
        "name": "SidebarGroupContent",
        "signature": "function SidebarGroupContent({\n  className,\n  ...props\n}: React.ComponentProps<\"div\">) {"
      },
      {
        "line": 465,
        "name": "SidebarMenu",
        "signature": "function SidebarMenu({ className, ...props }: React.ComponentProps<\"ul\">) {"
      },
      {
        "line": 476,
        "name": "SidebarMenuItem",
        "signature": "function SidebarMenuItem({ className, ...props }: React.ComponentProps<\"li\">) {"
      },
      {
        "line": 509,
        "name": "SidebarMenuButton",
        "signature": "function SidebarMenuButton({\n  asChild = false,\n  isActive = false,\n  variant = \"default\",\n  size = \"default\",\n  tooltip,\n  className,\n  ...props\n}: React.ComponentProps<\"button\"> & {\n  asChild?: boolean\n  isActive?: boolean\n  tooltip?: string | React.ComponentProps<typeof TooltipContent>\n} & VariantProps<typeof sidebarMenuButtonVariants>) {"
      },
      {
        "line": 559,
        "name": "SidebarMenuAction",
        "signature": "function SidebarMenuAction({\n  className,\n  asChild = false,\n  showOnHover = false,\n  ...props\n}: React.ComponentProps<\"button\"> & {\n  asChild?: boolean\n  showOnHover?: boolean\n}) {"
      },
      {
        "line": 591,
        "name": "SidebarMenuBadge",
        "signature": "function SidebarMenuBadge({\n  className,\n  ...props\n}: React.ComponentProps<\"div\">) {"
      },
      {
        "line": 613,
        "name": "SidebarMenuSkeleton",
        "signature": "function SidebarMenuSkeleton({\n  className,\n  showIcon = false,\n  ...props\n}: React.ComponentProps<\"div\"> & {\n  showIcon?: boolean\n}) {"
      },
      {
        "line": 651,
        "name": "SidebarMenuSub",
        "signature": "function SidebarMenuSub({ className, ...props }: React.ComponentProps<\"ul\">) {"
      },
      {
        "line": 666,
        "name": "SidebarMenuSubItem",
        "signature": "function SidebarMenuSubItem({\n  className,\n  ...props\n}: React.ComponentProps<\"li\">) {"
      },
      {
        "line": 680,
        "name": "SidebarMenuSubButton",
        "signature": "function SidebarMenuSubButton({\n  asChild = false,\n  size = \"md\",\n  isActive = false,\n  className,\n  ...props\n}: React.ComponentProps<\"a\"> & {\n  asChild?: boolean\n  size?: \"sm\" | \"md\"\n  isActive?: boolean\n}) {"
      }
    ],
    "language": "typescript",
    "lines": 738,
    "path": "frontend/src/components/ui/sidebar.tsx",
    "type": "module",
    "types": [
      {
        "definition": "type SidebarContextProps = {\n  state: \"expanded\" | \"collapsed\"\n  open: boolean\n  setOpen: (open: boolean) => void\n  openMobile: boolean\n  setOpenMobile: (open: boolean) => void\n  isMobile: boolean\n  toggleSidebar: () => void\n}",
        "line": 33,
        "name": "SidebarContextProps"
      }
    ]
  },
  {
    "dependencies": {
      "imports": [
        "@/lib/utils"
      ]
    },
    "file": "skeleton.tsx",
    "functions": [
      {
        "line": 3,
        "name": "Skeleton",
        "signature": "function Skeleton({ className, ...props }: React.ComponentProps<\"div\">) {"
      }
    ],
    "language": "typescript",
    "lines": 14,
    "path": "frontend/src/components/ui/skeleton.tsx",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "lucide-react",
        "next-themes",
        "sonner"
      ]
    },
    "file": "sonner.tsx",
    "functions": [
      {
        "line": 13,
        "name": "Toaster",
        "signature": "({ ...props }: ToasterProps) => {\n  const { theme = \"system\" } = useTheme()\n\n  return (\n    <Sonner\n      theme={theme as ToasterProps[\"theme\"]}\n      className=\"toaster group\"\n      icons={{\n        success: <CircleCheckIcon className=\"size-4\" />,\n        info: <InfoIcon className=\"size-4\" />,\n        warning: <TriangleAlertIcon className=\"size-4\" />,\n        error: <OctagonXIcon className=\"size-4\" />,\n        loading: <Loader2Icon className=\"size-4 animate-spin\" />,\n      }}\n      style={\n        {\n          \"--normal-bg\": \"var(--popover)\",\n          \"--normal-text\": \"var(--popover-foreground)\",\n          \"--normal-border\": \"var(--border)\",\n          \"--border-radius\": \"var(--radius)\",\n        } as React.CSSProperties\n      }\n      {...props}\n    />\n  )\n}"
      }
    ],
    "language": "typescript",
    "lines": 41,
    "path": "frontend/src/components/ui/sonner.tsx",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/lib/utils",
        "react"
      ]
    },
    "file": "table.tsx",
    "functions": [
      {
        "line": 5,
        "name": "Table",
        "signature": "function Table({ className, ...props }: React.ComponentProps<\"table\">) {"
      },
      {
        "line": 20,
        "name": "TableHeader",
        "signature": "function TableHeader({ className, ...props }: React.ComponentProps<\"thead\">) {"
      },
      {
        "line": 30,
        "name": "TableBody",
        "signature": "function TableBody({ className, ...props }: React.ComponentProps<\"tbody\">) {"
      },
      {
        "line": 40,
        "name": "TableFooter",
        "signature": "function TableFooter({ className, ...props }: React.ComponentProps<\"tfoot\">) {"
      },
      {
        "line": 53,
        "name": "TableRow",
        "signature": "function TableRow({ className, ...props }: React.ComponentProps<\"tr\">) {"
      },
      {
        "line": 66,
        "name": "TableHead",
        "signature": "function TableHead({ className, ...props }: React.ComponentProps<\"th\">) {"
      },
      {
        "line": 79,
        "name": "TableCell",
        "signature": "function TableCell({ className, ...props }: React.ComponentProps<\"td\">) {"
      },
      {
        "line": 92,
        "name": "TableCaption",
        "signature": "function TableCaption({\n  className,\n  ...props\n}: React.ComponentProps<\"caption\">) {"
      }
    ],
    "language": "typescript",
    "lines": 115,
    "path": "frontend/src/components/ui/table.tsx",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/lib/utils",
        "@radix-ui/react-tabs",
        "react"
      ]
    },
    "file": "tabs.tsx",
    "functions": [
      {
        "line": 6,
        "name": "Tabs",
        "signature": "function Tabs({\n  className,\n  ...props\n}: React.ComponentProps<typeof TabsPrimitive.Root>) {"
      },
      {
        "line": 19,
        "name": "TabsList",
        "signature": "function TabsList({\n  className,\n  ...props\n}: React.ComponentProps<typeof TabsPrimitive.List>) {"
      },
      {
        "line": 35,
        "name": "TabsTrigger",
        "signature": "function TabsTrigger({\n  className,\n  ...props\n}: React.ComponentProps<typeof TabsPrimitive.Trigger>) {"
      },
      {
        "line": 51,
        "name": "TabsContent",
        "signature": "function TabsContent({\n  className,\n  ...props\n}: React.ComponentProps<typeof TabsPrimitive.Content>) {"
      }
    ],
    "language": "typescript",
    "lines": 65,
    "path": "frontend/src/components/ui/tabs.tsx",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/lib/utils",
        "@radix-ui/react-tooltip",
        "react"
      ]
    },
    "file": "tooltip.tsx",
    "functions": [
      {
        "line": 6,
        "name": "TooltipProvider",
        "signature": "function TooltipProvider({\n  delayDuration = 0,\n  ...props\n}: React.ComponentProps<typeof TooltipPrimitive.Provider>) {"
      },
      {
        "line": 19,
        "name": "Tooltip",
        "signature": "function Tooltip({\n  ...props\n}: React.ComponentProps<typeof TooltipPrimitive.Root>) {"
      },
      {
        "line": 29,
        "name": "TooltipTrigger",
        "signature": "function TooltipTrigger({\n  ...props\n}: React.ComponentProps<typeof TooltipPrimitive.Trigger>) {"
      },
      {
        "line": 35,
        "name": "TooltipContent",
        "signature": "function TooltipContent({\n  className,\n  sideOffset = 0,\n  children,\n  ...props\n}: React.ComponentProps<typeof TooltipPrimitive.Content>) {"
      }
    ],
    "language": "typescript",
    "lines": 60,
    "path": "frontend/src/components/ui/tooltip.tsx",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "./useCustomToast",
        "@/client",
        "@/utils",
        "@tanstack/react-query",
        "@tanstack/react-router"
      ]
    },
    "file": "useAuth.ts",
    "functions": [
      {
        "line": 37,
        "name": "isLoggedIn",
        "purpose": "Check if user is authenticated by verifying access_token in localStorage.",
        "signature": "() => {\n  return localStorage.getItem(\"access_token\") !== null\n}"
      },
      {
        "line": 54,
        "name": "useAuth",
        "purpose": "Provide authentication state and actions (login, logout, signup)",
        "relationships": "Consumes: LoginService, UsersService, localStorage token\nProduces: Auth state, user data, login/logout/signup actions",
        "signature": "() => {\n  const navigate = useNavigate()\n  const queryClient = useQueryClient()\n  const { showErrorToast } = useCustomToast()\n\n  const { data: user } = useQuery<UserPublic | null, Error>({\n    queryKey: [\"currentUser\"],\n    queryFn: UsersService.readUserMe,\n    enabled: isLoggedIn(),\n  })\n\n  const signUpMutation = useMutation({\n    mutationFn: (data: UserRegister) =>\n      UsersService.registerUser({ requestBody: data }),\n    onSuccess: () => {\n      navigate({ to: \"/login\" })\n    },\n    onError: handleError.bind(showErrorToast),\n    onSettled: () => {\n      queryClient.invalidateQueries({ queryKey: [\"users\"] })\n    },\n  })\n\n  const login = async (data: AccessToken) => {\n    const response = await LoginService.loginAccessToken({\n      formData: data,\n    })\n    localStorage.setItem(\"access_token\", response.access_token)\n  }\n\n  const loginMutation = useMutation({\n    mutationFn: login,\n    onSuccess: () => {\n      navigate({ to: \"/\" })\n    },\n    onError: handleError.bind(showErrorToast),\n  })\n\n  const logout = () => {\n    localStorage.removeItem(\"access_token\")\n    navigate({ to: \"/login\" })\n  }\n\n  return {\n    signUpMutation,\n    loginMutation,\n    logout,\n    user,\n  }\n}",
        "structure": "user (UserPublic | null): output - Current authenticated user\nloginMutation (UseMutationResult): output - Login mutation\nsignUpMutation (UseMutationResult): output - Signup mutation\nlogout (function): output - Clear token and redirect to /login"
      }
    ],
    "language": "typescript",
    "lines": 107,
    "module": "hooks/useAuth",
    "path": "frontend/src/hooks/useAuth.ts",
    "purpose": "Authentication hook \u2014 login, signup, logout, and current user state.",
    "relationships": "Consumes: client/LoginService, client/UsersService\nProduces: Auth state and mutations (consumed by routes and components)",
    "semantics": "Domain: authentication\nLogic: [Token stored in localStorage, login redirects to /, signup redirects to /login,\nlogout clears token and redirects to /login]",
    "structure": "useAuth (hook): output - Returns { signUpMutation, loginMutation, logout, user }\nisLoggedIn (func): output - Check if access_token exists in localStorage",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "react"
      ]
    },
    "file": "useCopyToClipboard.ts",
    "functions": [
      {
        "line": 26,
        "name": "useCopyToClipboard",
        "purpose": "Copy text to clipboard and track copied state",
        "relationships": "Consumes: navigator.clipboard API\nProduces: Clipboard write + copied state",
        "signature": "function useCopyToClipboard(): [CopiedValue, CopyFn] {",
        "structure": "copiedText (string | null): output - Last copied text (resets after 2s)\ncopy (function): output - Async copy function returning success boolean"
      }
    ],
    "language": "typescript",
    "lines": 51,
    "module": "hooks/useCopyToClipboard",
    "path": "frontend/src/hooks/useCopyToClipboard.ts",
    "purpose": "Clipboard hook \u2014 copy text to clipboard with state tracking.",
    "type": "module",
    "types": [
      {
        "definition": "type CopiedValue = string | null",
        "line": 10,
        "name": "CopiedValue"
      },
      {
        "definition": "type CopyFn = (text: string) => Promise<boolean>",
        "line": 13,
        "name": "CopyFn"
      }
    ]
  },
  {
    "dependencies": {
      "imports": [
        "sonner"
      ]
    },
    "file": "useCustomToast.ts",
    "functions": [
      {
        "line": 19,
        "name": "useCustomToast",
        "purpose": "Provide convenience wrappers for success and error toast notifications",
        "relationships": "Consumes: sonner toast API\nProduces: Toast notifications (used by mutations and form handlers)",
        "signature": "() => {\n  const showSuccessToast = (description: string) => {\n    toast.success(\"Success!\", {\n      description,\n    })\n  }\n\n  const showErrorToast = (description: string) => {\n    toast.error(\"Something went wrong!\", {\n      description,\n    })\n  }\n\n  return { showSuccessToast, showErrorToast }\n}",
        "structure": "showSuccessToast (function): output - Display success toast with description\nshowErrorToast (function): output - Display error toast with description"
      }
    ],
    "language": "typescript",
    "lines": 36,
    "module": "hooks/useCustomToast",
    "path": "frontend/src/hooks/useCustomToast.ts",
    "purpose": "Toast notification hook \u2014 success and error toast helpers.",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "react"
      ]
    },
    "file": "useMobile.ts",
    "functions": [
      {
        "line": 21,
        "name": "useIsMobile",
        "purpose": "Detect if viewport is below mobile breakpoint (768px)",
        "relationships": "Consumes: window.matchMedia API\nProduces: Reactive mobile state (used by layout/sidebar components)",
        "signature": "function useIsMobile() {",
        "structure": "isMobile (boolean): output - True if window width < 768px"
      }
    ],
    "language": "typescript",
    "lines": 36,
    "module": "hooks/useMobile",
    "path": "frontend/src/hooks/useMobile.ts",
    "purpose": "Mobile detection hook \u2014 responsive breakpoint observer.",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "clsx",
        "tailwind-merge"
      ]
    },
    "file": "utils.ts",
    "functions": [
      {
        "line": 19,
        "name": "cn",
        "purpose": "Merge CSS class names with Tailwind conflict resolution",
        "relationships": "Consumes: clsx (conditional classes), tailwind-merge (conflict resolution)\nProduces: Merged className string (used by all UI components)",
        "signature": "function cn(...inputs: ClassValue[]) {",
        "structure": "inputs (ClassValue[]): input - Class names, conditionals, arrays"
      }
    ],
    "language": "typescript",
    "lines": 22,
    "module": "lib/utils",
    "path": "frontend/src/lib/utils.ts",
    "purpose": "Tailwind CSS utility \u2014 className merger with clsx + tailwind-merge.",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "./client",
        "./components/theme-provider",
        "./components/ui/sonner",
        "./index.css",
        "./routeTree.gen",
        "@tanstack/react-query",
        "@tanstack/react-router",
        "react",
        "react-dom/client"
      ]
    },
    "file": "main.tsx",
    "functions": [
      {
        "line": 45,
        "name": "handleApiError",
        "parameters": [
          {
            "name": "error",
            "type": "Error"
          }
        ],
        "purpose": "Clear token and redirect to /login on 401/403 API errors.",
        "signature": "(error: Error) => {\n  if (error instanceof ApiError && [401, 403].includes(error.status)) {\n    localStorage.removeItem(\"access_token\")\n    window.location.href = \"/login\"\n  }\n}"
      }
    ],
    "interfaces": [
      {
        "line": 62,
        "name": "Register"
      }
    ],
    "language": "typescript",
    "lines": 77,
    "module": "main",
    "path": "frontend/src/main.tsx",
    "purpose": "Application entry point \u2014 initializes React with router, query client, theme, and API auth.",
    "relationships": "Consumes: client/OpenAPI, routeTree.gen, theme-provider, sonner\nProduces: Rendered React app in #root DOM element",
    "semantics": "Logic: [401/403 API errors clear token and redirect to /login,\nDark theme default, strict mode enabled]",
    "structure": "OpenAPI.BASE (config): input - API base URL from VITE_API_URL env var\nOpenAPI.TOKEN (config): input - JWT token from localStorage\nqueryClient (QueryClient): config - TanStack Query client with auth error handling\nrouter (Router): config - TanStack Router from generated route tree",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "./routes/__root",
        "./routes/_layout",
        "./routes/_layout/admin",
        "./routes/_layout/index",
        "./routes/_layout/items",
        "./routes/_layout/settings",
        "./routes/login",
        "./routes/recover-password",
        "./routes/reset-password",
        "./routes/signup"
      ]
    },
    "file": "routeTree.gen.ts",
    "interfaces": [
      {
        "line": 67,
        "name": "FileRoutesByFullPath"
      },
      {
        "line": 77,
        "name": "FileRoutesByTo"
      },
      {
        "line": 87,
        "name": "FileRoutesById"
      },
      {
        "line": 99,
        "name": "FileRouteTypes"
      },
      {
        "line": 133,
        "name": "RootRouteChildren"
      },
      {
        "line": 142,
        "name": "FileRoutesByPath"
      },
      {
        "line": 209,
        "name": "LayoutRouteChildren"
      }
    ],
    "language": "typescript",
    "lines": 236,
    "path": "frontend/src/routeTree.gen.ts",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/components/Common/ErrorComponent",
        "@/components/Common/NotFound",
        "@tanstack/react-query-devtools",
        "@tanstack/react-router",
        "@tanstack/react-router-devtools"
      ]
    },
    "file": "__root.tsx",
    "language": "typescript",
    "lines": 36,
    "module": "routes/__root",
    "path": "frontend/src/routes/__root.tsx",
    "purpose": "Root route \u2014 top-level layout with devtools and error boundaries.",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/components/Common/Footer",
        "@/components/Sidebar/AppSidebar",
        "@/components/ui/sidebar",
        "@/hooks/useAuth",
        "@tanstack/react-router"
      ]
    },
    "file": "_layout.tsx",
    "functions": [
      {
        "line": 46,
        "name": "Layout",
        "signature": "function Layout() {"
      }
    ],
    "language": "typescript",
    "lines": 66,
    "module": "routes/_layout",
    "path": "frontend/src/routes/_layout.tsx",
    "purpose": "Authenticated layout route \u2014 sidebar + header + footer wrapper with auth guard.",
    "relationships": "Consumes: hooks/useAuth.isLoggedIn, Sidebar/AppSidebar, Common/Footer\nProduces: Layout shell (wraps all /_layout/* child routes)",
    "semantics": "Logic: [Redirects to /login if not authenticated (beforeLoad guard)]",
    "structure": "Route (FileRoute): config - TanStack route with beforeLoad auth check\nLayout (component): output - Sidebar + header + main content + footer",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/client",
        "@/components/Admin/AddUser",
        "@/components/Admin/columns",
        "@/components/Common/DataTable",
        "@/components/Pending/PendingUsers",
        "@/hooks/useAuth",
        "@tanstack/react-query",
        "@tanstack/react-router",
        "react"
      ]
    },
    "file": "admin.tsx",
    "functions": [
      {
        "line": 18,
        "name": "getUsersQueryOptions",
        "purpose": "TanStack Query options for fetching all users (up to 100).",
        "signature": "function getUsersQueryOptions() {"
      },
      {
        "line": 48,
        "name": "UsersTableContent",
        "purpose": "Fetches users via suspense query and renders DataTable with current-user flag.",
        "signature": "function UsersTableContent() {"
      },
      {
        "line": 61,
        "name": "UsersTable",
        "purpose": "Suspense wrapper for UsersTableContent with PendingUsers fallback.",
        "signature": "function UsersTable() {"
      },
      {
        "line": 79,
        "name": "Admin",
        "purpose": "Admin page for managing user accounts (superuser only)",
        "relationships": "Consumes: UsersService.readUsers, useAuth.user, Admin/AddUser, Admin/columns\nProduces: User management table with add-user action",
        "signature": "function Admin() {",
        "structure": "users (UserPublic[]): input - All users fetched via UsersService"
      }
    ],
    "language": "typescript",
    "lines": 95,
    "module": "routes/_layout/admin",
    "path": "frontend/src/routes/_layout/admin.tsx",
    "purpose": "Admin route \u2014 superuser-only user management page.",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/hooks/useAuth",
        "@tanstack/react-router"
      ]
    },
    "file": "index.tsx",
    "functions": [
      {
        "line": 34,
        "name": "Dashboard",
        "purpose": "Dashboard home page displaying welcome greeting",
        "relationships": "Consumes: useAuth.user\nProduces: Greeting UI with user's name or email",
        "signature": "function Dashboard() {",
        "structure": "currentUser (UserPublic): input - Current authenticated user from useAuth"
      }
    ],
    "language": "typescript",
    "lines": 50,
    "module": "routes/_layout/index",
    "path": "frontend/src/routes/_layout/index.tsx",
    "purpose": "Dashboard route \u2014 authenticated home page with user greeting.",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/client",
        "@/components/Common/DataTable",
        "@/components/Items/AddItem",
        "@/components/Items/columns",
        "@/components/Pending/PendingItems",
        "@tanstack/react-query",
        "@tanstack/react-router",
        "lucide-react",
        "react"
      ]
    },
    "file": "items.tsx",
    "functions": [
      {
        "line": 18,
        "name": "getItemsQueryOptions",
        "purpose": "TanStack Query options for fetching all items (up to 100).",
        "signature": "function getItemsQueryOptions() {"
      },
      {
        "line": 40,
        "name": "ItemsTableContent",
        "purpose": "Fetches items via suspense query; shows empty state or DataTable.",
        "signature": "function ItemsTableContent() {"
      },
      {
        "line": 59,
        "name": "ItemsTable",
        "purpose": "Suspense wrapper for ItemsTableContent with PendingItems fallback.",
        "signature": "function ItemsTable() {"
      },
      {
        "line": 77,
        "name": "Items",
        "purpose": "Items listing page with data table and add-item action",
        "relationships": "Consumes: ItemsService.readItems, Items/AddItem, Items/columns\nProduces: Items data table with empty state and add-item button",
        "signature": "function Items() {",
        "structure": "items (ItemPublic[]): input - All items fetched via ItemsService"
      }
    ],
    "language": "typescript",
    "lines": 91,
    "module": "routes/_layout/items",
    "path": "frontend/src/routes/_layout/items.tsx",
    "purpose": "Items route \u2014 CRUD listing page for user items.",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/components/UserSettings/ChangePassword",
        "@/components/UserSettings/DeleteAccount",
        "@/components/UserSettings/UserInformation",
        "@/components/ui/tabs",
        "@/hooks/useAuth",
        "@tanstack/react-router"
      ]
    },
    "file": "settings.tsx",
    "functions": [
      {
        "line": 46,
        "name": "UserSettings",
        "purpose": "User settings page with tabbed sections for profile, password, and account deletion",
        "relationships": "Consumes: useAuth.user, UserSettings/UserInformation, UserSettings/ChangePassword, UserSettings/DeleteAccount\nProduces: Tabbed settings UI (superusers see all tabs; non-superusers see all 3 tabs)",
        "signature": "function UserSettings() {",
        "structure": "currentUser (UserPublic): input - Current user from useAuth\nfinalTabs (TabConfig[]): derived - Tabs filtered by superuser status"
      }
    ],
    "language": "typescript",
    "lines": 82,
    "module": "routes/_layout/settings",
    "path": "frontend/src/routes/_layout/settings.tsx",
    "purpose": "Settings route \u2014 user profile, password, and account management.",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/client",
        "@/components/Common/AuthLayout",
        "@/components/ui/form",
        "@/components/ui/input",
        "@/components/ui/loading-button",
        "@/components/ui/password-input",
        "@/hooks/useAuth",
        "@hookform/resolvers/zod",
        "@tanstack/react-router",
        "react-hook-form",
        "zod"
      ]
    },
    "file": "login.tsx",
    "functions": [
      {
        "flow": "1. Render login form with email + password fields\n2. Validate via Zod schema on blur\n3. Call loginMutation on submit\n4. Redirect to home on success",
        "line": 79,
        "name": "Login",
        "purpose": "Login page with email/password authentication",
        "relationships": "Consumes: useAuth.loginMutation\nProduces: Auth token stored in localStorage, redirect to /",
        "signature": "function Login() {",
        "structure": "username (string): input - User email from form\npassword (string): input - User password from form"
      },
      {
        "line": 91,
        "name": "onSubmit",
        "parameters": [
          {
            "name": "data",
            "type": "FormData"
          }
        ],
        "signature": "(data: FormData) => {\n    if (loginMutation.isPending) return\n    loginMutation.mutate(data)\n  }"
      }
    ],
    "language": "typescript",
    "lines": 169,
    "module": "routes/login",
    "path": "frontend/src/routes/login.tsx",
    "purpose": "Login route \u2014 email/password authentication page.",
    "type": "module",
    "types": [
      {
        "definition": "type FormData = z.infer<typeof formSchema>",
        "line": 39,
        "name": "FormData"
      }
    ]
  },
  {
    "dependencies": {
      "imports": [
        "@/client",
        "@/components/Common/AuthLayout",
        "@/components/ui/form",
        "@/components/ui/input",
        "@/components/ui/loading-button",
        "@/hooks/useAuth",
        "@/hooks/useCustomToast",
        "@/utils",
        "@hookform/resolvers/zod",
        "@tanstack/react-query",
        "@tanstack/react-router",
        "react-hook-form",
        "zod"
      ]
    },
    "file": "recover-password.tsx",
    "language": "typescript",
    "lines": 154,
    "module": "routes/recover-password",
    "path": "frontend/src/routes/recover-password.tsx",
    "purpose": "Recover password route \u2014 sends password recovery email.",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@/client",
        "@/components/Common/AuthLayout",
        "@/components/ui/form",
        "@/components/ui/loading-button",
        "@/components/ui/password-input",
        "@/hooks/useAuth",
        "@/hooks/useCustomToast",
        "@/utils",
        "@hookform/resolvers/zod",
        "@tanstack/react-query",
        "@tanstack/react-router",
        "react-hook-form",
        "zod"
      ]
    },
    "file": "reset-password.tsx",
    "functions": [
      {
        "flow": "1. Extract token from URL search params\n2. Render new password + confirm password form\n3. Validate via Zod (including match check)\n4. Call resetPassword API with token + new password\n5. Show success toast, redirect to /login",
        "line": 99,
        "name": "ResetPassword",
        "purpose": "Reset password page \u2014 sets new password using token from recovery email",
        "relationships": "Consumes: LoginService.resetPassword API, URL search param token\nProduces: Password updated, redirect to /login on success",
        "signature": "function ResetPassword() {",
        "structure": "token (string): input - Reset token from URL search params\nnew_password (string): input - New password (min 8 chars)\nconfirm_password (string): input - Password confirmation (must match)"
      },
      {
        "line": 125,
        "name": "onSubmit",
        "parameters": [
          {
            "name": "data",
            "type": "FormData"
          }
        ],
        "signature": "(data: FormData) => {\n    mutation.mutate({ new_password: data.new_password, token })\n  }"
      }
    ],
    "language": "typescript",
    "lines": 197,
    "module": "routes/reset-password",
    "path": "frontend/src/routes/reset-password.tsx",
    "purpose": "Reset password route \u2014 sets new password using token from recovery email.",
    "type": "module",
    "types": [
      {
        "definition": "type FormData = z.infer<typeof formSchema>",
        "line": 54,
        "name": "FormData"
      }
    ]
  },
  {
    "dependencies": {
      "imports": [
        "@/components/Common/AuthLayout",
        "@/components/ui/form",
        "@/components/ui/input",
        "@/components/ui/loading-button",
        "@/components/ui/password-input",
        "@/hooks/useAuth",
        "@hookform/resolvers/zod",
        "@tanstack/react-router",
        "react-hook-form",
        "zod"
      ]
    },
    "file": "signup.tsx",
    "functions": [
      {
        "flow": "1. Render signup form with 4 fields\n2. Validate via Zod schema (including password match)\n3. Strip confirm_password, call signUpMutation\n4. Redirect to /login on success",
        "line": 88,
        "name": "SignUp",
        "purpose": "Registration page with email, name, password, and confirmation",
        "relationships": "Consumes: useAuth.signUpMutation\nProduces: New user account, redirect to /login on success",
        "signature": "function SignUp() {",
        "structure": "email (string): input - User email\nfull_name (string): input - User display name\npassword (string): input - User password (min 8 chars)\nconfirm_password (string): input - Password confirmation (must match)"
      },
      {
        "line": 102,
        "name": "onSubmit",
        "parameters": [
          {
            "name": "data",
            "type": "FormData"
          }
        ],
        "signature": "(data: FormData) => {\n    if (signUpMutation.isPending) return\n\n    // exclude confirm_password from submission data\n    const { confirm_password: _confirm_password, ...submitData } = data\n    signUpMutation.mutate(submitData)\n  }"
      }
    ],
    "language": "typescript",
    "lines": 218,
    "module": "routes/signup",
    "path": "frontend/src/routes/signup.tsx",
    "purpose": "Signup route \u2014 new user registration page.",
    "type": "module",
    "types": [
      {
        "definition": "type FormData = z.infer<typeof formSchema>",
        "line": 46,
        "name": "FormData"
      }
    ]
  },
  {
    "dependencies": {
      "imports": [
        "./client",
        "axios"
      ]
    },
    "file": "utils.ts",
    "functions": [
      {
        "line": 23,
        "name": "extractErrorMessage",
        "parameters": [
          {
            "name": "err",
            "type": "ApiError"
          }
        ],
        "purpose": "Extract human-readable error message from ApiError or AxiosError.",
        "signature": "function extractErrorMessage(err: ApiError): string {"
      },
      {
        "line": 45,
        "name": "getInitials",
        "parameters": [
          {
            "name": "name",
            "type": "string"
          }
        ],
        "purpose": "Extract up to 2 uppercase initials from a name string (e.g., \"John Doe\" \u2192 \"JD\").",
        "signature": "(name: string): string => {\n  return name\n    .split(\" \")\n    .slice(0, 2)\n    .map((word) => word[0])\n    .join(\"\")\n    .toUpperCase()\n}"
      }
    ],
    "language": "typescript",
    "lines": 53,
    "module": "utils",
    "path": "frontend/src/utils.ts",
    "purpose": "Shared utility functions for error handling and display formatting.",
    "relationships": "Consumes: client/ApiError\nProduces: Error messages (consumed by mutation onError handlers)",
    "structure": "extractErrorMessage (func): output - Extract human-readable message from API errors\nhandleError (func): output - Bind error extraction to toast display (use as .bind(showErrorToast))\ngetInitials (func): output - Extract uppercase initials from name string",
    "type": "module"
  },
  {
    "file": "vite-env.d.ts",
    "interfaces": [
      {
        "line": 3,
        "name": "ImportMetaEnv"
      },
      {
        "line": 7,
        "name": "ImportMeta"
      }
    ],
    "language": "typescript",
    "lines": 10,
    "path": "frontend/src/vite-env.d.ts",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "./config.ts",
        "@playwright/test"
      ]
    },
    "file": "auth.setup.ts",
    "language": "typescript",
    "lines": 14,
    "path": "frontend/tests/auth.setup.ts",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "dotenv",
        "node:path",
        "node:url"
      ]
    },
    "file": "config.ts",
    "functions": [
      {
        "line": 10,
        "name": "getEnvVar",
        "parameters": [
          {
            "name": "name",
            "type": "string"
          }
        ],
        "signature": "function getEnvVar(name: string): string {"
      }
    ],
    "language": "typescript",
    "lines": 20,
    "path": "frontend/tests/config.ts",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@playwright/test"
      ]
    },
    "file": "mailcatcher.ts",
    "functions": [
      {
        "line": 9,
        "name": "findEmail",
        "signature": "async function findEmail({\n  request,\n  filter,\n}: {\n  request: APIRequestContext\n  filter?: (email: Email) => boolean\n}) {"
      },
      {
        "line": 33,
        "name": "findLastEmail",
        "signature": "function findLastEmail({\n  request,\n  filter,\n  timeout = 5000,\n}: {\n  request: APIRequestContext\n  filter?: (email: Email) => boolean\n  timeout?: number\n}) {"
      }
    ],
    "language": "typescript",
    "lines": 63,
    "path": "frontend/tests/utils/mailcatcher.ts",
    "type": "module",
    "types": [
      {
        "definition": "type Email = {\n  id: number\n  recipients: string[]\n  subject: string\n}",
        "line": 3,
        "name": "Email"
      }
    ]
  },
  {
    "dependencies": {
      "imports": [
        "../../src/client"
      ]
    },
    "file": "privateApi.ts",
    "functions": [
      {
        "line": 7,
        "name": "createUser",
        "signature": "async ({\n  email,\n  password,\n}: {\n  email: string\n  password: string\n}) => {\n  return await PrivateService.createUser({\n    requestBody: {\n      email,\n      password,\n      is_verified: true,\n      full_name: \"Test User\",\n    },\n  })\n}"
      }
    ],
    "language": "typescript",
    "lines": 23,
    "path": "frontend/tests/utils/privateApi.ts",
    "type": "module"
  },
  {
    "file": "random.ts",
    "functions": [
      {
        "line": 1,
        "name": "randomEmail",
        "signature": "() =>\n  `test_${Math.random().toString(36).substring(7)}@example.com`"
      },
      {
        "line": 4,
        "name": "randomTeamName",
        "signature": "() =>\n  `Team ${Math.random().toString(36).substring(7)}`"
      },
      {
        "line": 7,
        "name": "randomPassword",
        "signature": "() => `${Math.random().toString(36).substring(2)}`"
      },
      {
        "line": 9,
        "name": "slugify",
        "parameters": [
          {
            "name": "text",
            "type": "string"
          }
        ],
        "signature": "(text: string) =>\n  text\n    .toLowerCase()\n    .replace(/\\s+/g, \"-\")\n    .replace(/[^\\w-]+/g, \"\")"
      },
      {
        "line": 15,
        "name": "randomItemTitle",
        "signature": "() =>\n  `Item ${Math.random().toString(36).substring(7)}`"
      },
      {
        "line": 18,
        "name": "randomItemDescription",
        "signature": "() =>\n  `Description ${Math.random().toString(36).substring(7)}`"
      }
    ],
    "language": "typescript",
    "lines": 20,
    "path": "frontend/tests/utils/random.ts",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@playwright/test"
      ]
    },
    "file": "user.ts",
    "functions": [
      {
        "line": 3,
        "name": "signUpNewUser",
        "parameters": [
          {
            "name": "page",
            "type": "Page"
          },
          {
            "name": "name",
            "type": "string"
          },
          {
            "name": "email",
            "type": "string"
          },
          {
            "name": "password",
            "type": "string"
          }
        ],
        "signature": "async function signUpNewUser(\n  page: Page,\n  name: string,\n  email: string,\n  password: string,\n) {"
      },
      {
        "line": 19,
        "name": "logInUser",
        "parameters": [
          {
            "name": "page",
            "type": "Page"
          },
          {
            "name": "email",
            "type": "string"
          },
          {
            "name": "password",
            "type": "string"
          }
        ],
        "signature": "async function logInUser(page: Page, email: string, password: string) {"
      },
      {
        "line": 31,
        "name": "logOutUser",
        "parameters": [
          {
            "name": "page",
            "type": "Page"
          }
        ],
        "signature": "async function logOutUser(page: Page) {"
      }
    ],
    "language": "typescript",
    "lines": 36,
    "path": "frontend/tests/utils/user.ts",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "@tailwindcss/vite",
        "@tanstack/router-plugin/vite",
        "@vitejs/plugin-react-swc",
        "node:path",
        "vite"
      ]
    },
    "file": "vite.config.ts",
    "language": "typescript",
    "lines": 23,
    "path": "frontend/vite.config.ts",
    "type": "module"
  }
]
}
```

---

## Files

- **frontend/openapi-ts.config.ts** - TODO
- **frontend/playwright.config.ts** - TODO
- **frontend/src/client/core/ApiError.ts** - TODO
- **frontend/src/client/core/ApiRequestOptions.ts** - TODO
- **frontend/src/client/core/ApiResult.ts** - TODO
- **frontend/src/client/core/CancelablePromise.ts** - TODO
- **frontend/src/client/core/OpenAPI.ts** - TODO
- **frontend/src/client/core/request.ts** - TODO
- **frontend/src/client/index.ts** - TODO
- **frontend/src/client/schemas.gen.ts** - TODO
- **frontend/src/client/sdk.gen.ts** - TODO
- **frontend/src/client/types.gen.ts** - TODO
- **frontend/src/components/Admin/AddUser.tsx** - Dialog for creating new user accounts in the admin panel.
- **frontend/src/components/Admin/DeleteUser.tsx** - Confirmation dialog for deleting a user account.
- **frontend/src/components/Admin/EditUser.tsx** - Dialog for editing existing user account details.
- **frontend/src/components/Admin/UserActionsMenu.tsx** - Dropdown actions menu for user row operations (edit, delete).
- **frontend/src/components/Admin/columns.tsx** - Column definitions for the admin users data table.
- **frontend/src/components/Common/Appearance.tsx** - Theme toggle components for switching between light, dark, and system modes.
- **frontend/src/components/Common/AuthLayout.tsx** - Two-column layout wrapper for authentication pages (login, signup, reset).
- **frontend/src/components/Common/DataTable.tsx** - Generic paginated data table component built on TanStack Table.
- **frontend/src/components/Common/ErrorComponent.tsx** - Generic error page displayed when an unhandled error occurs.
- **frontend/src/components/Common/Footer.tsx** - Application footer with copyright and social media links.
- **frontend/src/components/Common/Logo.tsx** - Theme-aware FastAPI logo component with full, icon, and responsive variants.
- **frontend/src/components/Common/NotFound.tsx** - 404 page displayed when a route is not matched.
- **frontend/src/components/Items/AddItem.tsx** - Dialog for creating new items with title and description.
- **frontend/src/components/Items/DeleteItem.tsx** - Confirmation dialog for deleting an item.
- **frontend/src/components/Items/EditItem.tsx** - Dialog for editing existing item details.
- **frontend/src/components/Items/ItemActionsMenu.tsx** - Dropdown actions menu for item row operations (edit, delete).
- **frontend/src/components/Items/columns.tsx** - Column definitions for the items data table.
- **frontend/src/components/Pending/PendingItems.tsx** - Skeleton loading placeholder for the items table.
- **frontend/src/components/Pending/PendingUsers.tsx** - Skeleton loading placeholder for the users table.
- **frontend/src/components/Sidebar/AppSidebar.tsx** - Main application sidebar with navigation, theme toggle, and user menu.
- **frontend/src/components/Sidebar/Main.tsx** - Primary navigation menu rendered inside the sidebar.
- **frontend/src/components/Sidebar/User.tsx** - Sidebar user menu with avatar, settings link, and logout action.
- **frontend/src/components/UserSettings/ChangePassword.tsx** - Form for changing the current user's password.
- **frontend/src/components/UserSettings/DeleteAccount.tsx** - Danger zone section for account self-deletion.
- **frontend/src/components/UserSettings/DeleteConfirmation.tsx** - Confirmation dialog for self-deleting the current user's account.
- **frontend/src/components/UserSettings/UserInformation.tsx** - Editable display of current user's profile information (name, email).
- **frontend/src/components/theme-provider.tsx** - React context provider for application theme management (dark/light/system).
- **frontend/src/components/ui/alert.tsx** - TODO
- **frontend/src/components/ui/avatar.tsx** - TODO
- **frontend/src/components/ui/badge.tsx** - TODO
- **frontend/src/components/ui/button-group.tsx** - TODO
- **frontend/src/components/ui/button.tsx** - TODO
- **frontend/src/components/ui/card.tsx** - TODO
- **frontend/src/components/ui/checkbox.tsx** - TODO
- **frontend/src/components/ui/dialog.tsx** - TODO
- **frontend/src/components/ui/dropdown-menu.tsx** - TODO
- **frontend/src/components/ui/form.tsx** - TODO
- **frontend/src/components/ui/input.tsx** - TODO
- **frontend/src/components/ui/label.tsx** - TODO
- **frontend/src/components/ui/loading-button.tsx** - TODO
- **frontend/src/components/ui/pagination.tsx** - TODO
- **frontend/src/components/ui/password-input.tsx** - TODO
- **frontend/src/components/ui/select.tsx** - TODO
- **frontend/src/components/ui/separator.tsx** - TODO
- **frontend/src/components/ui/sheet.tsx** - TODO
- **frontend/src/components/ui/sidebar.tsx** - TODO
- **frontend/src/components/ui/skeleton.tsx** - TODO
- **frontend/src/components/ui/sonner.tsx** - TODO
- **frontend/src/components/ui/table.tsx** - TODO
- **frontend/src/components/ui/tabs.tsx** - TODO
- **frontend/src/components/ui/tooltip.tsx** - TODO
- **frontend/src/hooks/useAuth.ts** - Authentication hook — login, signup, logout, and current user state.
- **frontend/src/hooks/useCopyToClipboard.ts** - Clipboard hook — copy text to clipboard with state tracking.
- **frontend/src/hooks/useCustomToast.ts** - Toast notification hook — success and error toast helpers.
- **frontend/src/hooks/useMobile.ts** - Mobile detection hook — responsive breakpoint observer.
- **frontend/src/lib/utils.ts** - Tailwind CSS utility — className merger with clsx + tailwind-merge.
- **frontend/src/main.tsx** - Application entry point — initializes React with router, query client, theme, and API auth.
- **frontend/src/routeTree.gen.ts** - TODO
- **frontend/src/routes/__root.tsx** - Root route — top-level layout with devtools and error boundaries.
- **frontend/src/routes/_layout.tsx** - Authenticated layout route — sidebar + header + footer wrapper with auth guard.
- **frontend/src/routes/_layout/admin.tsx** - Admin route — superuser-only user management page.
- **frontend/src/routes/_layout/index.tsx** - Dashboard route — authenticated home page with user greeting.
- **frontend/src/routes/_layout/items.tsx** - Items route — CRUD listing page for user items.
- **frontend/src/routes/_layout/settings.tsx** - Settings route — user profile, password, and account management.
- **frontend/src/routes/login.tsx** - Login route — email/password authentication page.
- **frontend/src/routes/recover-password.tsx** - Recover password route — sends password recovery email.
- **frontend/src/routes/reset-password.tsx** - Reset password route — sets new password using token from recovery email.
- **frontend/src/routes/signup.tsx** - Signup route — new user registration page.
- **frontend/src/utils.ts** - Shared utility functions for error handling and display formatting.
- **frontend/src/vite-env.d.ts** - TODO
- **frontend/tests/auth.setup.ts** - TODO
- **frontend/tests/config.ts** - TODO
- **frontend/tests/utils/mailcatcher.ts** - TODO
- **frontend/tests/utils/privateApi.ts** - TODO
- **frontend/tests/utils/random.ts** - TODO
- **frontend/tests/utils/user.ts** - TODO
- **frontend/vite.config.ts** - TODO
