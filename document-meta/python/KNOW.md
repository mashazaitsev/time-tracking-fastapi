# Python Documentation

## Complete Metadata

```json
{
  "type": "python",
  "total_files": 40,
  "files": [
  {
    "dependencies": {
      "imports": [
        "json",
        "pathlib"
      ]
    },
    "file": "update_dotenv.py",
    "language": "python",
    "lines": 26,
    "path": ".copier/update_dotenv.py",
    "type": "module"
  },
  {
    "file": "__init__.py",
    "language": "python",
    "lines": 0,
    "path": "backend/app/__init__.py",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "alembic",
        "app.core.config",
        "app.models",
        "logging.config",
        "os",
        "sqlalchemy"
      ]
    },
    "file": "env.py",
    "functions": [
      {
        "line": 41,
        "name": "get_url",
        "purpose": "Purpose: Return database connection URL from application settings",
        "relationships": "Consumes: settings.SQLALCHEMY_DATABASE_URI\n    Produces: Database URL string",
        "signature": "get_url()",
        "structure": "url (str): output - SQLAlchemy database URI"
      },
      {
        "flow": "1. Get database URL\n    2. Configure Alembic context with URL and metadata\n    3. Run migrations within transaction",
        "line": 55,
        "name": "run_migrations_offline",
        "purpose": "Purpose: Run migrations in offline mode (emit SQL without DB connection)",
        "relationships": "Consumes: get_url(), target_metadata\n    Produces: SQL migration statements",
        "signature": "run_migrations_offline()",
        "structure": "url (str): internal - Database URL from get_url()"
      },
      {
        "flow": "1. Build engine config with database URL\n    2. Create connectable engine with NullPool\n    3. Configure context with connection and run migrations",
        "line": 80,
        "name": "run_migrations_online",
        "purpose": "Purpose: Run migrations in online mode with live database connection",
        "relationships": "Consumes: get_url(), config section, target_metadata\n    Produces: Applied database migrations",
        "signature": "run_migrations_online()",
        "structure": "configuration (dict): internal - Alembic config section\n    connectable (Engine): internal - SQLAlchemy engine"
      }
    ],
    "language": "python",
    "lines": 117,
    "path": "backend/app/alembic/env.py",
    "purpose": "Purpose: Configure Alembic migration environment for online and offline modes\n\nStructure:\n    get_url (func): config - Return database URL from settings\n    run_migrations_offline (func): migration - Run migrations without DB connection\n    run_migrations_online (func): migration - Run migrations with live DB connection\n\nRelationships:\n    Consumes: app.models.SQLModel.metadata, app.core.config.settings.SQLALCHEMY_DATABASE_URI\n    Produces: Database schema migrations\n\nImportant:\n    app.models MUST be imported before target_metadata is set,\n    otherwise Alembic won't detect model changes for autogenerate.",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "alembic",
        "sqlalchemy",
        "sqlmodel.sql.sqltypes"
      ]
    },
    "file": "1a31ce608336_add_cascade_delete_relationships.py",
    "functions": [
      {
        "line": 20,
        "name": "upgrade",
        "signature": "upgrade()"
      },
      {
        "line": 30,
        "name": "downgrade",
        "signature": "downgrade()"
      }
    ],
    "language": "python",
    "lines": 37,
    "path": "backend/app/alembic/versions/1a31ce608336_add_cascade_delete_relationships.py",
    "purpose": "Add cascade delete relationships\n\nRevision ID: 1a31ce608336\nRevises: d98dd8ec85a3\nCreate Date: 2024-07-31 22:24:34.447891",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "alembic",
        "sqlalchemy",
        "sqlmodel.sql.sqltypes"
      ]
    },
    "file": "9c0a54914c78_add_max_length_for_string_varchar_.py",
    "functions": [
      {
        "line": 20,
        "name": "upgrade",
        "signature": "upgrade()"
      },
      {
        "line": 46,
        "name": "downgrade",
        "signature": "downgrade()"
      }
    ],
    "language": "python",
    "lines": 69,
    "path": "backend/app/alembic/versions/9c0a54914c78_add_max_length_for_string_varchar_.py",
    "purpose": "Add max length for string(varchar) fields in User and Items models\n\nRevision ID: 9c0a54914c78\nRevises: e2412789c190\nCreate Date: 2024-06-17 14:42:44.639457",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "alembic",
        "sqlalchemy",
        "sqlalchemy.dialects",
        "sqlmodel.sql.sqltypes"
      ]
    },
    "file": "d98dd8ec85a3_edit_replace_id_integers_in_all_models_.py",
    "functions": [
      {
        "line": 21,
        "name": "upgrade",
        "signature": "upgrade()"
      },
      {
        "line": 57,
        "name": "downgrade",
        "signature": "downgrade()"
      }
    ],
    "language": "python",
    "lines": 90,
    "path": "backend/app/alembic/versions/d98dd8ec85a3_edit_replace_id_integers_in_all_models_.py",
    "purpose": "Edit replace id integers in all models to use UUID instead\n\nRevision ID: d98dd8ec85a3\nRevises: 9c0a54914c78\nCreate Date: 2024-07-19 04:08:04.000976",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "alembic",
        "sqlalchemy",
        "sqlmodel.sql.sqltypes"
      ]
    },
    "file": "e2412789c190_initialize_models.py",
    "functions": [
      {
        "line": 19,
        "name": "upgrade",
        "signature": "upgrade()"
      },
      {
        "line": 49,
        "name": "downgrade",
        "signature": "downgrade()"
      }
    ],
    "language": "python",
    "lines": 54,
    "path": "backend/app/alembic/versions/e2412789c190_initialize_models.py",
    "purpose": "Initialize models\n\nRevision ID: e2412789c190\nRevises:\nCreate Date: 2023-11-24 22:55:43.195942",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "alembic",
        "sqlalchemy",
        "sqlmodel.sql.sqltypes"
      ]
    },
    "file": "fe56fa70289e_add_created_at_to_user_and_item.py",
    "functions": [
      {
        "line": 20,
        "name": "upgrade",
        "signature": "upgrade()"
      },
      {
        "line": 27,
        "name": "downgrade",
        "signature": "downgrade()"
      }
    ],
    "language": "python",
    "lines": 31,
    "path": "backend/app/alembic/versions/fe56fa70289e_add_created_at_to_user_and_item.py",
    "purpose": "Add created_at to User and Item\n\nRevision ID: fe56fa70289e\nRevises: 1a31ce608336\nCreate Date: 2026-01-23 15:50:37.171462",
    "type": "module"
  },
  {
    "file": "__init__.py",
    "language": "python",
    "lines": 0,
    "path": "backend/app/api/__init__.py",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "app.core",
        "app.core.config",
        "app.core.db",
        "app.models",
        "collections.abc",
        "fastapi",
        "fastapi.security",
        "jwt",
        "jwt.exceptions",
        "pydantic",
        "sqlmodel",
        "typing"
      ]
    },
    "file": "deps.py",
    "functions": [
      {
        "line": 38,
        "name": "get_db",
        "purpose": "Purpose: Yield a database session per request, auto-closed on completion",
        "relationships": "Consumes: core.db.engine\n    Produces: Session (via SessionDep alias)",
        "signature": "get_db()",
        "structure": "session (Session): output - SQLModel database session"
      },
      {
        "flow": "1. Decode JWT with SECRET_KEY and validate payload\n    2. Look up user by token subject (user ID)\n    3. Raise 404 if not found, 400 if inactive",
        "line": 57,
        "name": "get_current_user",
        "parameters": [
          {
            "name": "session"
          },
          {
            "name": "token"
          }
        ],
        "purpose": "Purpose: Decode JWT token and return the authenticated active User",
        "relationships": "Consumes: JWT token, User table, core.security.ALGORITHM, settings.SECRET_KEY\n    Produces: Authenticated User object (via CurrentUser alias)",
        "signature": "get_current_user(session, token)",
        "structure": "session (SessionDep): input - Database session\n    token (TokenDep): input - JWT bearer token\n    user (User): output - Authenticated user"
      },
      {
        "line": 96,
        "name": "get_current_active_superuser",
        "parameters": [
          {
            "name": "current_user"
          }
        ],
        "purpose": "Purpose: Enforce superuser role on authenticated user",
        "relationships": "Consumes: CurrentUser dependency\n    Produces: Verified superuser (used as route dependency)",
        "signature": "get_current_active_superuser(current_user)",
        "structure": "current_user (CurrentUser): input - Authenticated user\n    user (User): output - Verified superuser"
      }
    ],
    "language": "python",
    "lines": 112,
    "path": "backend/app/api/deps.py",
    "purpose": "Purpose: Provide FastAPI dependency injection for database sessions and authentication\n\nStructure:\n    get_db (func): dependency - Yield SQLModel session per request\n    get_current_user (func): dependency - Decode JWT and return authenticated User\n    get_current_active_superuser (func): dependency - Enforce superuser role\n    SessionDep (type alias): shorthand - Annotated[Session, Depends(get_db)]\n    TokenDep (type alias): shorthand - Annotated[str, Depends(reusable_oauth2)]\n    CurrentUser (type alias): shorthand - Annotated[User, Depends(get_current_user)]\n\nRelationships:\n    Consumes: core.security.ALGORITHM, core.config.settings.SECRET_KEY, core.db.engine\n    Consumes: models.TokenPayload, models.User\n    Produces: Session, User (injected into route handlers)",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "app.api.routes",
        "app.core.config",
        "fastapi"
      ]
    },
    "file": "main.py",
    "language": "python",
    "lines": 28,
    "path": "backend/app/api/main.py",
    "purpose": "Purpose: Register all API route modules into the main API router\n\nStructure:\n    api_router (APIRouter): output - Combined router with all route modules\n\nRelationships:\n    Consumes: api.routes.login, api.routes.users, api.routes.utils, api.routes.items, api.routes.private\n    Produces: api_router (consumed by app.main)\n\nNote:\n    Private routes only registered when ENVIRONMENT=local.",
    "type": "module"
  },
  {
    "file": "__init__.py",
    "language": "python",
    "lines": 0,
    "path": "backend/app/api/routes/__init__.py",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "app.api.deps",
        "app.models",
        "fastapi",
        "sqlmodel",
        "typing",
        "uuid"
      ]
    },
    "file": "items.py",
    "functions": [
      {
        "flow": "1. Check if superuser (query all) or regular user (query owned only)\n    2. Count matching items and fetch paginated results\n    3. Return ItemsPublic with data and count",
        "line": 35,
        "name": "read_items",
        "parameters": [
          {
            "name": "session"
          },
          {
            "name": "current_user"
          },
          {
            "name": "skip"
          },
          {
            "name": "limit"
          }
        ],
        "purpose": "Purpose: Retrieve paginated list of items for current user",
        "relationships": "Consumes: Item table, current user context\n    Produces: ItemsPublic response",
        "signature": "read_items(session, current_user, skip, limit)",
        "structure": "session (SessionDep): input - Database session\n    current_user (CurrentUser): input - Authenticated user\n    skip (int): input - Pagination offset\n    limit (int): input - Max items per page\n    items (ItemsPublic): output - Paginated items list with count"
      },
      {
        "flow": "1. Fetch item by ID, raise 404 if not found\n    2. Verify ownership or superuser role, raise 403 if denied\n    3. Return item",
        "line": 85,
        "name": "read_item",
        "parameters": [
          {
            "name": "session"
          },
          {
            "name": "current_user"
          },
          {
            "name": "id"
          }
        ],
        "purpose": "Purpose: Retrieve a single item by ID with ownership check",
        "relationships": "Consumes: Item table, current user context\n    Produces: ItemPublic response",
        "signature": "read_item(session, current_user, id)",
        "structure": "session (SessionDep): input - Database session\n    current_user (CurrentUser): input - Authenticated user\n    id (uuid.UUID): input - Item ID\n    item (ItemPublic): output - Item details"
      },
      {
        "flow": "1. Validate input and set owner_id to current user\n    2. Persist item to database\n    3. Return created item",
        "line": 113,
        "name": "create_item",
        "purpose": "Purpose: Create a new item owned by the current user",
        "relationships": "Consumes: ItemCreate schema, current user context\n    Produces: Item table row, ItemPublic response",
        "signature": "create_item()",
        "structure": "session (SessionDep): input - Database session\n    current_user (CurrentUser): input - Authenticated user\n    item_in (ItemCreate): input - Item creation payload\n    item (ItemPublic): output - Created item"
      },
      {
        "flow": "1. Fetch item by ID, raise 404 if not found\n    2. Verify ownership or superuser role, raise 403 if denied\n    3. Apply partial update and persist",
        "line": 142,
        "name": "update_item",
        "purpose": "Purpose: Update an existing item with ownership check",
        "relationships": "Consumes: Item table, ItemUpdate schema, current user context\n    Produces: Updated Item table row, ItemPublic response",
        "signature": "update_item()",
        "structure": "session (SessionDep): input - Database session\n    current_user (CurrentUser): input - Authenticated user\n    id (uuid.UUID): input - Item ID\n    item_in (ItemUpdate): input - Partial update payload\n    item (ItemPublic): output - Updated item"
      },
      {
        "flow": "1. Fetch item by ID, raise 404 if not found\n    2. Verify ownership or superuser role, raise 403 if denied\n    3. Delete item and return confirmation",
        "line": 182,
        "name": "delete_item",
        "parameters": [
          {
            "name": "session"
          },
          {
            "name": "current_user"
          },
          {
            "name": "id"
          }
        ],
        "purpose": "Purpose: Delete an item with ownership check",
        "relationships": "Consumes: Item table, current user context\n    Produces: Message response",
        "signature": "delete_item(session, current_user, id)",
        "structure": "session (SessionDep): input - Database session\n    current_user (CurrentUser): input - Authenticated user\n    id (uuid.UUID): input - Item ID\n    message (Message): output - Deletion confirmation"
      }
    ],
    "language": "python",
    "lines": 210,
    "path": "backend/app/api/routes/items.py",
    "purpose": "Purpose: Provide CRUD API endpoints for Item resources with owner-based access control\n\nStructure:\n    read_items (GET /): endpoint - List items (all for superuser, own for regular user)\n    read_item (GET /{id}): endpoint - Get single item by ID\n    create_item (POST /): endpoint - Create item owned by current user\n    update_item (PUT /{id}): endpoint - Update item (owner or superuser only)\n    delete_item (DELETE /{id}): endpoint - Delete item (owner or superuser only)\n\nRelationships:\n    Consumes: models.Item, models.ItemCreate, models.ItemUpdate, api.deps.CurrentUser\n    Produces: ItemPublic, ItemsPublic, Message responses\n\nSemantics:\n    Domain: content\n    Entity: Item\n    Logic: [Superusers see all items, regular users see only their own,\n            owner or superuser required for read/update/delete of specific items]",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "app",
        "app.api.deps",
        "app.core",
        "app.core.config",
        "app.models",
        "app.utils",
        "datetime",
        "fastapi",
        "fastapi.responses",
        "fastapi.security",
        "typing"
      ]
    },
    "file": "login.py",
    "functions": [
      {
        "flow": "1. Authenticate user via crud, raise 400 if invalid credentials\n    2. Raise 400 if user is inactive\n    3. Create and return JWT access token with configured expiry",
        "line": 45,
        "name": "login_access_token",
        "parameters": [
          {
            "name": "session"
          },
          {
            "name": "form_data"
          }
        ],
        "purpose": "Purpose: Authenticate user via email/password and return JWT access token",
        "relationships": "Consumes: crud.authenticate, core.security.create_access_token\n    Produces: Token response",
        "signature": "login_access_token(session, form_data)",
        "structure": "session (SessionDep): input - Database session\n    form_data (OAuth2PasswordRequestForm): input - Username (email) and password\n    token (Token): output - JWT access token"
      },
      {
        "line": 81,
        "name": "test_token",
        "parameters": [
          {
            "name": "current_user"
          }
        ],
        "purpose": "Purpose: Validate access token and return current user profile",
        "relationships": "Consumes: CurrentUser dependency (validates token implicitly)\n    Produces: UserPublic response",
        "signature": "test_token(current_user)",
        "structure": "current_user (CurrentUser): input - Authenticated user from token\n    user (UserPublic): output - Current user profile"
      },
      {
        "flow": "1. Look up user by email\n    2. If found, generate reset token and send recovery email\n    3. Return same message regardless of email existence (prevents enumeration)",
        "line": 97,
        "name": "recover_password",
        "parameters": [
          {
            "name": "email"
          },
          {
            "name": "session"
          }
        ],
        "purpose": "Purpose: Send password recovery email if user exists",
        "relationships": "Consumes: crud.get_user_by_email, utils.generate_password_reset_token, utils.send_email\n    Produces: Message response, password reset email",
        "signature": "recover_password(email, session)",
        "structure": "email (str): input - User email address\n    session (SessionDep): input - Database session\n    message (Message): output - Generic confirmation message"
      },
      {
        "flow": "1. Verify reset token and extract email, raise 400 if invalid\n    2. Look up user by email, raise 400 if not found or inactive\n    3. Update password hash and return confirmation",
        "line": 133,
        "name": "reset_password",
        "parameters": [
          {
            "name": "session"
          },
          {
            "name": "body"
          }
        ],
        "purpose": "Purpose: Reset user password using a recovery token",
        "relationships": "Consumes: utils.verify_password_reset_token, crud.get_user_by_email, crud.update_user\n    Produces: Message response, updated password hash in User table",
        "signature": "reset_password(session, body)",
        "structure": "session (SessionDep): input - Database session\n    body (NewPassword): input - Reset token and new password\n    message (Message): output - Success confirmation"
      },
      {
        "flow": "1. Look up user by email, raise 404 if not found\n    2. Generate reset token and email content\n    3. Return HTML response with subject in headers",
        "line": 173,
        "name": "recover_password_html_content",
        "parameters": [
          {
            "name": "email"
          },
          {
            "name": "session"
          }
        ],
        "purpose": "Purpose: Preview password recovery email HTML content (superuser only)",
        "relationships": "Consumes: crud.get_user_by_email, utils.generate_password_reset_token, utils.generate_reset_password_email\n    Produces: HTMLResponse with email content and subject header",
        "signature": "recover_password_html_content(email, session)",
        "structure": "email (str): input - Target user email\n    session (SessionDep): input - Database session\n    html (HTMLResponse): output - Rendered email HTML"
      }
    ],
    "language": "python",
    "lines": 205,
    "path": "backend/app/api/routes/login.py",
    "purpose": "Purpose: Provide authentication endpoints for login, token validation, and password recovery\n\nStructure:\n    login_access_token (POST /login/access-token): endpoint - OAuth2 token login\n    test_token (POST /login/test-token): endpoint - Validate access token\n    recover_password (POST /password-recovery/{email}): endpoint - Send password reset email\n    reset_password (POST /reset-password/): endpoint - Reset password with token\n    recover_password_html_content (POST /password-recovery-html-content/{email}): endpoint - Preview reset email HTML (superuser only)\n\nRelationships:\n    Consumes: crud.authenticate, crud.get_user_by_email, crud.update_user\n    Consumes: utils.generate_password_reset_token, utils.generate_reset_password_email, utils.send_email\n    Produces: Token, UserPublic, Message responses\n\nSemantics:\n    Domain: authentication\n    Logic: [Password recovery returns same response regardless of email existence (prevents enumeration),\n            Reset tokens expire per EMAIL_RESET_TOKEN_EXPIRE_HOURS setting]",
    "type": "module"
  },
  {
    "classes": [
      {
        "line": 31,
        "name": "PrivateUserCreate",
        "purpose": "Purpose: Schema for private user creation (bypasses SQLModel validation)\n\nStructure:\n    email (str): input - User email\n    password (str): input - Plain text password\n    full_name (str): input - User display name\n    is_verified (bool): input - Verification status (default False)"
      }
    ],
    "dependencies": {
      "imports": [
        "app.api.deps",
        "app.core.security",
        "app.models",
        "fastapi",
        "pydantic",
        "typing"
      ]
    },
    "file": "private.py",
    "functions": [
      {
        "flow": "1. Build User model with hashed password\n    2. Persist to database\n    3. Return created user",
        "line": 48,
        "name": "create_user",
        "parameters": [
          {
            "name": "user_in"
          },
          {
            "name": "session"
          }
        ],
        "purpose": "Purpose: Create user directly without email uniqueness check (local dev only)",
        "relationships": "Consumes: PrivateUserCreate schema, core.security.get_password_hash\n    Produces: User table row, UserPublic response",
        "signature": "create_user(user_in, session)",
        "structure": "user_in (PrivateUserCreate): input - User creation payload\n    session (SessionDep): input - Database session\n    user (UserPublic): output - Created user"
      }
    ],
    "language": "python",
    "lines": 76,
    "path": "backend/app/api/routes/private.py",
    "purpose": "Purpose: Provide private admin endpoint for user creation (local environment only)\n\nStructure:\n    PrivateUserCreate (class): schema - User creation without SQLModel validation\n    create_user (POST /private/users/): endpoint - Create user directly\n\nRelationships:\n    Consumes: models.User, core.security.get_password_hash\n    Produces: UserPublic response, User table row\n\nNote:\n    Only registered when ENVIRONMENT=local (see api/main.py).",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "app",
        "app.api.deps",
        "app.core.config",
        "app.core.security",
        "app.models",
        "app.utils",
        "fastapi",
        "sqlmodel",
        "typing",
        "uuid"
      ]
    },
    "file": "users.py",
    "functions": [
      {
        "line": 64,
        "name": "read_users",
        "parameters": [
          {
            "name": "session"
          },
          {
            "name": "skip"
          },
          {
            "name": "limit"
          }
        ],
        "purpose": "Purpose: Retrieve paginated list of all users (superuser only)",
        "relationships": "Consumes: User table\n    Produces: UsersPublic response",
        "signature": "read_users(session, skip, limit)",
        "structure": "session (SessionDep): input - Database session\n    skip (int): input - Pagination offset\n    limit (int): input - Max users per page\n    users (UsersPublic): output - Paginated users list with count"
      },
      {
        "flow": "1. Check email uniqueness, raise 400 if duplicate\n    2. Create user via crud\n    3. Send welcome email if SMTP enabled",
        "line": 93,
        "name": "create_user",
        "purpose": "Purpose: Create a new user (superuser only), send welcome email if SMTP configured",
        "relationships": "Consumes: crud.get_user_by_email, crud.create_user, utils.send_email\n    Produces: User table row, UserPublic response, welcome email",
        "signature": "create_user()",
        "structure": "session (SessionDep): input - Database session\n    user_in (UserCreate): input - User creation payload\n    user (UserPublic): output - Created user"
      },
      {
        "flow": "1. If email changing, check uniqueness (raise 409 if taken)\n    2. Apply partial update to current user\n    3. Persist and return updated user",
        "line": 132,
        "name": "update_user_me",
        "purpose": "Purpose: Update own profile (name and email)",
        "relationships": "Consumes: crud.get_user_by_email, User table\n    Produces: Updated User table row, UserPublic response",
        "signature": "update_user_me()",
        "structure": "session (SessionDep): input - Database session\n    user_in (UserUpdateMe): input - Partial profile update\n    current_user (CurrentUser): input - Authenticated user\n    user (UserPublic): output - Updated user profile"
      },
      {
        "flow": "1. Verify current password, raise 400 if incorrect\n    2. Reject if new password equals current, raise 400\n    3. Hash new password, persist, and return confirmation",
        "line": 169,
        "name": "update_password_me",
        "purpose": "Purpose: Change own password with current password verification",
        "relationships": "Consumes: core.security.verify_password, core.security.get_password_hash\n    Produces: Updated password hash in User table, Message response",
        "signature": "update_password_me()",
        "structure": "session (SessionDep): input - Database session\n    body (UpdatePassword): input - Current and new passwords\n    current_user (CurrentUser): input - Authenticated user\n    message (Message): output - Success confirmation"
      },
      {
        "line": 205,
        "name": "read_user_me",
        "parameters": [
          {
            "name": "current_user"
          }
        ],
        "purpose": "Purpose: Get current authenticated user profile",
        "relationships": "Consumes: CurrentUser dependency\n    Produces: UserPublic response",
        "signature": "read_user_me(current_user)",
        "structure": "current_user (CurrentUser): input - Authenticated user\n    user (UserPublic): output - Current user profile"
      },
      {
        "line": 221,
        "name": "delete_user_me",
        "parameters": [
          {
            "name": "session"
          },
          {
            "name": "current_user"
          }
        ],
        "purpose": "Purpose: Delete own account (superusers cannot delete themselves)",
        "relationships": "Consumes: User table\n    Produces: Message response",
        "signature": "delete_user_me(session, current_user)",
        "structure": "session (SessionDep): input - Database session\n    current_user (CurrentUser): input - Authenticated user\n    message (Message): output - Deletion confirmation"
      },
      {
        "flow": "1. Check email uniqueness, raise 400 if duplicate\n    2. Convert to UserCreate and create user via crud\n    3. Return created user",
        "line": 244,
        "name": "register_user",
        "parameters": [
          {
            "name": "session"
          },
          {
            "name": "user_in"
          }
        ],
        "purpose": "Purpose: Public self-registration (no auth required)",
        "relationships": "Consumes: crud.get_user_by_email, crud.create_user\n    Produces: User table row, UserPublic response",
        "signature": "register_user(session, user_in)",
        "structure": "session (SessionDep): input - Database session\n    user_in (UserRegister): input - Registration payload\n    user (UserPublic): output - Created user"
      },
      {
        "flow": "1. Fetch user by ID\n    2. Return immediately if requesting own profile\n    3. Raise 403 if not superuser, raise 404 if user not found",
        "line": 274,
        "name": "read_user_by_id",
        "parameters": [
          {
            "name": "user_id"
          },
          {
            "name": "session"
          },
          {
            "name": "current_user"
          }
        ],
        "purpose": "Purpose: Get user by ID (own profile or superuser only)",
        "relationships": "Consumes: User table, current user context\n    Produces: UserPublic response",
        "signature": "read_user_by_id(user_id, session, current_user)",
        "structure": "user_id (uuid.UUID): input - Target user ID\n    session (SessionDep): input - Database session\n    current_user (CurrentUser): input - Authenticated user\n    user (UserPublic): output - User profile"
      },
      {
        "flow": "1. Fetch user by ID, raise 404 if not found\n    2. If email changing, check uniqueness (raise 409 if taken)\n    3. Update user via crud and return",
        "line": 313,
        "name": "update_user",
        "purpose": "Purpose: Update a user by ID (superuser only)",
        "relationships": "Consumes: crud.get_user_by_email, crud.update_user, User table\n    Produces: Updated User table row, UserPublic response",
        "signature": "update_user()",
        "structure": "session (SessionDep): input - Database session\n    user_id (uuid.UUID): input - Target user ID\n    user_in (UserUpdate): input - Partial update payload\n    user (UserPublic): output - Updated user"
      },
      {
        "flow": "1. Fetch user by ID, raise 404 if not found\n    2. Raise 403 if attempting self-deletion\n    3. Delete user's items, then delete user",
        "line": 356,
        "name": "delete_user",
        "parameters": [
          {
            "name": "session"
          },
          {
            "name": "current_user"
          },
          {
            "name": "user_id"
          }
        ],
        "purpose": "Purpose: Delete a user and their items (superuser only, cannot self-delete)",
        "relationships": "Consumes: User table, Item table\n    Produces: Message response",
        "signature": "delete_user(session, current_user, user_id)",
        "structure": "session (SessionDep): input - Database session\n    current_user (CurrentUser): input - Authenticated superuser\n    user_id (uuid.UUID): input - Target user ID\n    message (Message): output - Deletion confirmation"
      }
    ],
    "language": "python",
    "lines": 388,
    "path": "backend/app/api/routes/users.py",
    "purpose": "Purpose: Provide CRUD API endpoints for User management with role-based access control\n\nStructure:\n    read_users (GET /): endpoint - List users (superuser only)\n    create_user (POST /): endpoint - Create user (superuser only)\n    update_user_me (PATCH /me): endpoint - Update own profile\n    update_password_me (PATCH /me/password): endpoint - Change own password\n    read_user_me (GET /me): endpoint - Get own profile\n    delete_user_me (DELETE /me): endpoint - Delete own account (non-superuser only)\n    register_user (POST /signup): endpoint - Public self-registration\n    read_user_by_id (GET /{user_id}): endpoint - Get user by ID\n    update_user (PATCH /{user_id}): endpoint - Update user (superuser only)\n    delete_user (DELETE /{user_id}): endpoint - Delete user (superuser only)\n\nRelationships:\n    Consumes: crud (create_user, update_user, get_user_by_email), models (User, Item, schemas)\n    Consumes: utils.generate_new_account_email, utils.send_email\n    Produces: UserPublic, UsersPublic, Message responses\n\nSemantics:\n    Domain: identity\n    Entity: User\n    Logic: [Superusers cannot delete themselves, email uniqueness enforced,\n            new account email sent if SMTP configured, items cascade-deleted with user]",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "app.api.deps",
        "app.models",
        "app.utils",
        "fastapi",
        "pydantic.networks"
      ]
    },
    "file": "utils.py",
    "functions": [
      {
        "line": 28,
        "name": "test_email",
        "parameters": [
          {
            "name": "email_to"
          }
        ],
        "purpose": "Purpose: Send test email to verify SMTP configuration (superuser only)",
        "relationships": "Consumes: utils.generate_test_email, utils.send_email\n    Produces: Message response, test email",
        "signature": "test_email(email_to)",
        "structure": "email_to (EmailStr): input - Recipient email address\n    message (Message): output - Success confirmation"
      }
    ],
    "language": "python",
    "lines": 61,
    "path": "backend/app/api/routes/utils.py",
    "purpose": "Purpose: Provide utility endpoints for health checks and email testing\n\nStructure:\n    test_email (POST /utils/test-email/): endpoint - Send test email (superuser only)\n    health_check (GET /utils/health-check/): endpoint - Application health check\n\nRelationships:\n    Consumes: utils.generate_test_email, utils.send_email\n    Produces: Message response, bool response",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "app.core.db",
        "logging",
        "sqlalchemy",
        "sqlmodel",
        "tenacity"
      ]
    },
    "file": "backend_pre_start.py",
    "functions": [
      {
        "line": 40,
        "name": "init",
        "parameters": [
          {
            "name": "db_engine"
          }
        ],
        "purpose": "Purpose: Attempt single DB connection, raising on failure (retried by tenacity)",
        "signature": "init(db_engine)",
        "structure": "db_engine (Engine): input - SQLAlchemy engine to test"
      },
      {
        "line": 56,
        "name": "main",
        "purpose": "Purpose: Entry point \u2014 wait for database readiness with retry logging",
        "signature": "main()"
      }
    ],
    "language": "python",
    "lines": 64,
    "path": "backend/app/backend_pre_start.py",
    "purpose": "Purpose: Wait for database readiness before application startup with retry logic\n\nStructure:\n    init (func): setup - Attempt DB connection with tenacity retry\n    main (func): entry - Script entry point\n\nRelationships:\n    Consumes: core.db.engine\n    Produces: (blocks until DB is ready)\n\nSemantics:\n    Logic: [Retries every 1 second for up to 5 minutes (300 attempts)]\n\nNote:\n    Run via scripts/prestart.sh before alembic migrations and initial_data.",
    "type": "module"
  },
  {
    "file": "__init__.py",
    "language": "python",
    "lines": 0,
    "path": "backend/app/core/__init__.py",
    "type": "module"
  },
  {
    "classes": [
      {
        "line": 50,
        "methods": [
          "all_cors_origins: line 84",
          "SQLALCHEMY_DATABASE_URI: line 100",
          "_set_default_emails_from: line 121",
          "emails_enabled: line 131",
          "_check_default_secret: line 139",
          "_enforce_non_default_secrets: line 152"
        ],
        "name": "Settings",
        "purpose": "Purpose: Centralized application configuration with env var loading and validation\n\nStructure:\n    API_V1_STR (str): config - API version prefix\n    SECRET_KEY (str): config - JWT signing key\n    SQLALCHEMY_DATABASE_URI (computed): config - Full PostgreSQL connection URI\n    emails_enabled (computed): config - Whether email sending is configured\n    all_cors_origins (computed): config - Combined CORS + frontend origins\n\nImportant:\n    env_file points to \"../.env\" (one level above backend/).\n    Default secrets trigger warnings locally, errors in staging/production."
      }
    ],
    "dependencies": {
      "imports": [
        "pydantic",
        "pydantic_settings",
        "secrets",
        "typing",
        "typing_extensions",
        "warnings"
      ]
    },
    "file": "config.py",
    "functions": [
      {
        "line": 41,
        "name": "parse_cors",
        "parameters": [
          {
            "name": "v"
          }
        ],
        "purpose": "Purpose: Parse CORS origins from comma-separated string or list",
        "signature": "parse_cors(v)"
      },
      {
        "line": 84,
        "name": "all_cors_origins",
        "parameters": [
          {
            "name": "self"
          }
        ],
        "purpose": "Purpose: Combine BACKEND_CORS_ORIGINS and FRONTEND_HOST into unified origin list",
        "signature": "all_cors_origins(self)"
      },
      {
        "line": 100,
        "name": "SQLALCHEMY_DATABASE_URI",
        "parameters": [
          {
            "name": "self"
          }
        ],
        "purpose": "Purpose: Build PostgreSQL connection URI from individual POSTGRES_* settings",
        "signature": "SQLALCHEMY_DATABASE_URI(self)"
      },
      {
        "line": 121,
        "name": "_set_default_emails_from",
        "parameters": [
          {
            "name": "self"
          }
        ],
        "purpose": "Purpose: Default EMAILS_FROM_NAME to PROJECT_NAME if not set",
        "signature": "_set_default_emails_from(self)"
      },
      {
        "line": 131,
        "name": "emails_enabled",
        "parameters": [
          {
            "name": "self"
          }
        ],
        "purpose": "Purpose: Check if SMTP is configured (SMTP_HOST and EMAILS_FROM_EMAIL both set)",
        "signature": "emails_enabled(self)"
      },
      {
        "line": 139,
        "name": "_check_default_secret",
        "parameters": [
          {
            "name": "self"
          },
          {
            "name": "var_name"
          },
          {
            "name": "value"
          }
        ],
        "purpose": "Purpose: Warn (local) or raise (staging/production) if secret is still 'changethis'",
        "signature": "_check_default_secret(self, var_name, value)"
      },
      {
        "line": 152,
        "name": "_enforce_non_default_secrets",
        "parameters": [
          {
            "name": "self"
          }
        ],
        "purpose": "Purpose: Validate SECRET_KEY, POSTGRES_PASSWORD, and FIRST_SUPERUSER_PASSWORD are not defaults",
        "signature": "_enforce_non_default_secrets(self)"
      }
    ],
    "language": "python",
    "lines": 163,
    "path": "backend/app/core/config.py",
    "purpose": "Purpose: Load and validate all application settings from environment variables and .env file\n\nStructure:\n    Settings (class): config - Pydantic settings with validation for DB, auth, email, CORS\n    parse_cors (func): config - Parse CORS origins from comma-separated string or list\n    settings (Settings): output - Singleton settings instance\n\nRelationships:\n    Consumes: ../.env file, environment variables\n    Produces: settings (consumed by all backend modules)\n\nSemantics:\n    Domain: configuration\n    Logic: [Warns on default secrets in local, raises in staging/production,\n            SQLALCHEMY_DATABASE_URI computed from POSTGRES_* fields,\n            emails_enabled computed from SMTP_HOST + EMAILS_FROM_EMAIL]\n\nImportant:\n    SECRET_KEY, POSTGRES_PASSWORD, and FIRST_SUPERUSER_PASSWORD MUST NOT be\n    \"changethis\" in staging/production \u2014 validation will raise ValueError.",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "app",
        "app.core.config",
        "app.models",
        "sqlmodel"
      ]
    },
    "file": "db.py",
    "functions": [
      {
        "flow": "1. Check if FIRST_SUPERUSER email exists\n    2. If not, create superuser via crud.create_user",
        "line": 28,
        "name": "init_db",
        "parameters": [
          {
            "name": "session"
          }
        ],
        "purpose": "Purpose: Seed first superuser if not already present",
        "signature": "init_db(session)"
      }
    ],
    "language": "python",
    "lines": 53,
    "path": "backend/app/core/db.py",
    "purpose": "Purpose: Initialize database engine and seed first superuser on startup\n\nStructure:\n    engine (Engine): config - SQLAlchemy engine from settings\n    init_db (func): output - Create first superuser if not exists\n\nRelationships:\n    Consumes: core.config.settings (SQLALCHEMY_DATABASE_URI, FIRST_SUPERUSER, FIRST_SUPERUSER_PASSWORD)\n    Consumes: crud.create_user\n    Produces: first superuser row in user table\n\nImportant:\n    All SQLModel models MUST be imported (via app.models) before init_db runs,\n    otherwise SQLModel fails to initialize relationships.\n    Tables are created by Alembic migrations, NOT by init_db.",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "app.core.config",
        "datetime",
        "jwt",
        "pwdlib",
        "pwdlib.hashers.argon2",
        "pwdlib.hashers.bcrypt",
        "typing"
      ]
    },
    "file": "security.py",
    "functions": [
      {
        "line": 42,
        "name": "create_access_token",
        "parameters": [
          {
            "name": "subject"
          },
          {
            "name": "expires_delta"
          }
        ],
        "purpose": "Purpose: Create signed JWT with subject (user ID) and expiration",
        "signature": "create_access_token(subject, expires_delta)"
      },
      {
        "line": 50,
        "name": "verify_password",
        "parameters": [
          {
            "name": "plain_password"
          },
          {
            "name": "hashed_password"
          }
        ],
        "purpose": "Purpose: Verify password against hash, returning upgraded hash if algorithm changed",
        "returns_doc": "tuple: (verified: bool, updated_hash: str | None) \u2014 updated_hash is non-None\n    when bcrypt hash was verified and needs upgrade to argon2",
        "signature": "verify_password(plain_password, hashed_password)"
      },
      {
        "line": 63,
        "name": "get_password_hash",
        "parameters": [
          {
            "name": "password"
          }
        ],
        "purpose": "Purpose: Hash password using Argon2 (primary hasher)",
        "signature": "get_password_hash(password)"
      }
    ],
    "language": "python",
    "lines": 65,
    "path": "backend/app/core/security.py",
    "purpose": "Purpose: Provide JWT token creation and password hashing/verification\n\nStructure:\n    create_access_token (func): output - Create signed JWT with expiration\n    verify_password (func): output - Verify password and return upgraded hash if applicable\n    get_password_hash (func): output - Hash password with Argon2\n    password_hash (PasswordHash): config - Multi-hasher supporting Argon2 and bcrypt\n    ALGORITHM (str): config - JWT signing algorithm (HS256)\n\nRelationships:\n    Consumes: core.config.settings.SECRET_KEY\n    Produces: JWT tokens, password hashes (consumed by crud, api.deps)\n\nSemantics:\n    Domain: security\n    Logic: [Argon2 is primary hasher, bcrypt supported for legacy upgrade,\n            verify_and_update returns new hash when bcrypt\u2192argon2 upgrade needed]",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "app.core.security",
        "app.models",
        "sqlmodel",
        "typing",
        "uuid"
      ]
    },
    "file": "crud.py",
    "functions": [
      {
        "line": 35,
        "name": "create_user",
        "purpose": "Purpose: Create user with hashed password",
        "relationships": "Consumes: UserCreate schema\n    Produces: user table row",
        "signature": "create_user()"
      },
      {
        "line": 52,
        "name": "update_user",
        "purpose": "Purpose: Update user fields, re-hashing password if changed",
        "relationships": "Consumes: UserUpdate schema, existing User\n    Produces: updated user table row",
        "signature": "update_user()"
      },
      {
        "line": 73,
        "name": "get_user_by_email",
        "purpose": "Purpose: Look up user by email address",
        "signature": "get_user_by_email()"
      },
      {
        "flow": "1. Look up user by email\n    2. If not found, verify against dummy hash (timing-attack prevention)\n    3. Verify password against stored hash\n    4. If hash algorithm upgraded (bcrypt\u2192argon2), persist new hash",
        "important": "MUST run verify_password even when user not found to prevent\n    timing-based email enumeration.",
        "line": 84,
        "name": "authenticate",
        "purpose": "Purpose: Verify email/password credentials and auto-upgrade legacy bcrypt hashes",
        "signature": "authenticate()"
      },
      {
        "line": 113,
        "name": "create_item",
        "purpose": "Purpose: Create item assigned to owner",
        "relationships": "Consumes: ItemCreate schema, owner UUID\n    Produces: item table row",
        "signature": "create_item()"
      }
    ],
    "language": "python",
    "lines": 125,
    "path": "backend/app/crud.py",
    "purpose": "Purpose: Provide CRUD operations for User and Item database entities\n\nStructure:\n    create_user (func): output - Create user with hashed password\n    update_user (func): output - Update user fields, re-hash if password changed\n    get_user_by_email (func): output - Look up user by email\n    authenticate (func): output - Verify email/password, upgrade hash if needed\n    create_item (func): output - Create item with owner assignment\n\nRelationships:\n    Consumes: models.User, models.Item, models.UserCreate, models.UserUpdate, models.ItemCreate\n    Consumes: core.security.get_password_hash, core.security.verify_password\n    Produces: User rows, Item rows\n\nSemantics:\n    Domain: identity, content\n    Logic: [Timing-attack prevention via dummy hash on failed lookup,\n            Auto-upgrade bcrypt\u2192argon2 on successful login]\n\nImportant:\n    authenticate() MUST run verify_password even when user not found\n    to prevent timing-based email enumeration attacks.",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "app.core.db",
        "logging",
        "sqlmodel"
      ]
    },
    "file": "initial_data.py",
    "functions": [
      {
        "line": 27,
        "name": "init",
        "purpose": "Purpose: Open database session and seed initial data via init_db",
        "signature": "init()"
      },
      {
        "line": 33,
        "name": "main",
        "purpose": "Purpose: Entry point \u2014 log and run initial data seeding",
        "signature": "main()"
      }
    ],
    "language": "python",
    "lines": 41,
    "path": "backend/app/initial_data.py",
    "purpose": "Purpose: Seed initial database data (first superuser) on application startup\n\nStructure:\n    init (func): setup - Open session and call init_db\n    main (func): entry - Script entry point with logging\n\nRelationships:\n    Consumes: core.db.engine, core.db.init_db\n    Produces: first superuser in user table\n\nNote:\n    Run via: python app/initial_data.py (or uv run python app/initial_data.py)\n    Also called by scripts/prestart.sh before app starts.",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "app.api.main",
        "app.core.config",
        "fastapi",
        "fastapi.routing",
        "sentry_sdk",
        "starlette.middleware.cors"
      ]
    },
    "file": "main.py",
    "functions": [
      {
        "line": 26,
        "name": "custom_generate_unique_id",
        "parameters": [
          {
            "name": "route"
          }
        ],
        "purpose": "Purpose: Generate OpenAPI operation ID as '{tag}-{name}' for client codegen",
        "signature": "custom_generate_unique_id(route)"
      }
    ],
    "language": "python",
    "lines": 50,
    "path": "backend/app/main.py",
    "purpose": "Purpose: Initialize FastAPI application with CORS, Sentry, and API router\n\nStructure:\n    app (FastAPI): output - Configured FastAPI application instance\n    custom_generate_unique_id (func): config - Generate OpenAPI operation IDs from route tag + name\n\nRelationships:\n    Consumes: core.config.settings, api.main.api_router\n    Produces: FastAPI app (consumed by uvicorn)\n\nSemantics:\n    Domain: application\n    Logic: [Sentry enabled only in non-local environments, CORS origins from settings]",
    "type": "module"
  },
  {
    "classes": [
      {
        "line": 40,
        "name": "UserBase",
        "purpose": "Purpose: Shared user fields for all user schemas"
      },
      {
        "line": 48,
        "name": "UserCreate",
        "purpose": "Purpose: Schema for admin user creation (includes role flags from UserBase)"
      },
      {
        "line": 53,
        "name": "UserRegister",
        "purpose": "Purpose: Schema for public self-registration (no role flags)"
      },
      {
        "line": 60,
        "name": "UserUpdate",
        "purpose": "Purpose: Schema for admin user update (all fields optional)"
      },
      {
        "line": 66,
        "name": "UserUpdateMe",
        "purpose": "Purpose: Schema for self-profile update (name and email only)"
      },
      {
        "line": 72,
        "name": "UpdatePassword",
        "purpose": "Purpose: Schema for authenticated password change"
      },
      {
        "line": 78,
        "name": "User",
        "purpose": "Purpose: User database table with auth credentials and owned items"
      },
      {
        "line": 89,
        "name": "UserPublic",
        "purpose": "Purpose: User response schema (excludes hashed_password)"
      },
      {
        "line": 95,
        "name": "UsersPublic",
        "purpose": "Purpose: Paginated user list response"
      },
      {
        "line": 101,
        "name": "ItemBase",
        "purpose": "Purpose: Shared item fields for all item schemas"
      },
      {
        "line": 107,
        "name": "ItemCreate",
        "purpose": "Purpose: Schema for item creation"
      },
      {
        "line": 112,
        "name": "ItemUpdate",
        "purpose": "Purpose: Schema for item update (all fields optional)"
      },
      {
        "line": 117,
        "name": "Item",
        "purpose": "Purpose: Item database table owned by a User (cascade-deletes with owner)"
      },
      {
        "line": 130,
        "name": "ItemPublic",
        "purpose": "Purpose: Item response schema with owner reference"
      },
      {
        "line": 137,
        "name": "ItemsPublic",
        "purpose": "Purpose: Paginated item list response"
      },
      {
        "line": 143,
        "name": "Message",
        "purpose": "Purpose: Generic API message response"
      },
      {
        "line": 148,
        "name": "Token",
        "purpose": "Purpose: JWT access token response"
      },
      {
        "line": 154,
        "name": "TokenPayload",
        "purpose": "Purpose: Decoded JWT token payload (sub = user ID)"
      },
      {
        "line": 159,
        "name": "NewPassword",
        "purpose": "Purpose: Schema for token-based password reset"
      }
    ],
    "dependencies": {
      "imports": [
        "datetime",
        "pydantic",
        "sqlalchemy",
        "sqlmodel",
        "uuid"
      ]
    },
    "file": "models.py",
    "functions": [
      {
        "line": 35,
        "name": "get_datetime_utc",
        "purpose": "Purpose: Return current UTC datetime for default timestamps",
        "signature": "get_datetime_utc()"
      }
    ],
    "language": "python",
    "lines": 162,
    "path": "backend/app/models.py",
    "purpose": "Purpose: Define all SQLModel database tables and Pydantic API schemas for User and Item entities\n\nStructure:\n    User (table): entity - User account with auth and profile data\n    Item (table): entity - User-owned content item\n    UserBase, UserCreate, UserUpdate, UserRegister, UserUpdateMe, UpdatePassword: schema - User API schemas\n    UserPublic, UsersPublic: schema - User response schemas\n    ItemBase, ItemCreate, ItemUpdate: schema - Item API schemas\n    ItemPublic, ItemsPublic: schema - Item response schemas\n    Token, TokenPayload, NewPassword, Message: schema - Auth and utility schemas\n\nRelationships:\n    Produces: user table, item table\n    Consumes: (consumed by) api.routes, crud, core.db\n\nSemantics:\n    Domain: identity, content\n    Entity: User, Item\n    Logic: [Items cascade-delete with owner, UUIDs as primary keys, created_at auto-set to UTC]\n\nImportant:\n    All SQLModel table classes MUST be imported before Alembic or init_db runs,\n    otherwise relationships fail to initialize. See core/db.py comment.",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "app.core.db",
        "logging",
        "sqlalchemy",
        "sqlmodel",
        "tenacity"
      ]
    },
    "file": "tests_pre_start.py",
    "functions": [
      {
        "line": 40,
        "name": "init",
        "parameters": [
          {
            "name": "db_engine"
          }
        ],
        "purpose": "Purpose: Attempt single DB connection, raising on failure (retried by tenacity)",
        "signature": "init(db_engine)",
        "structure": "db_engine (Engine): input - SQLAlchemy engine to test"
      },
      {
        "line": 56,
        "name": "main",
        "purpose": "Purpose: Entry point \u2014 wait for database readiness with retry logging",
        "signature": "main()"
      }
    ],
    "language": "python",
    "lines": 64,
    "path": "backend/app/tests_pre_start.py",
    "purpose": "Purpose: Wait for database readiness before test suite execution with retry logic\n\nStructure:\n    init (func): setup - Attempt DB connection with tenacity retry\n    main (func): entry - Script entry point\n\nRelationships:\n    Consumes: core.db.engine\n    Produces: (blocks until DB is ready)\n\nSemantics:\n    Logic: [Retries every 1 second for up to 5 minutes (300 attempts)]\n\nNote:\n    Run via scripts/tests-start.sh before pytest.",
    "type": "module"
  },
  {
    "classes": [
      {
        "line": 44,
        "name": "EmailData",
        "purpose": "Purpose: Container for rendered email content and subject"
      }
    ],
    "dependencies": {
      "imports": [
        "app.core",
        "app.core.config",
        "dataclasses",
        "datetime",
        "emails",
        "jinja2",
        "jwt",
        "jwt.exceptions",
        "logging",
        "pathlib",
        "typing"
      ]
    },
    "file": "utils.py",
    "functions": [
      {
        "line": 50,
        "name": "render_email_template",
        "purpose": "Purpose: Render Jinja2 HTML email template from email-templates/build/",
        "signature": "render_email_template()"
      },
      {
        "important": "Asserts emails_enabled \u2014 will raise if SMTP not configured.",
        "line": 59,
        "name": "send_email",
        "purpose": "Purpose: Send email via configured SMTP server",
        "signature": "send_email()"
      },
      {
        "line": 90,
        "name": "generate_test_email",
        "parameters": [
          {
            "name": "email_to"
          }
        ],
        "purpose": "Purpose: Build test email content for SMTP verification",
        "signature": "generate_test_email(email_to)"
      },
      {
        "line": 101,
        "name": "generate_reset_password_email",
        "parameters": [
          {
            "name": "email_to"
          },
          {
            "name": "email"
          },
          {
            "name": "token"
          }
        ],
        "purpose": "Purpose: Build password reset email with frontend reset link",
        "signature": "generate_reset_password_email(email_to, email, token)"
      },
      {
        "line": 119,
        "name": "generate_new_account_email",
        "parameters": [
          {
            "name": "email_to"
          },
          {
            "name": "username"
          },
          {
            "name": "password"
          }
        ],
        "purpose": "Purpose: Build welcome email for newly created accounts",
        "signature": "generate_new_account_email(email_to, username, password)"
      },
      {
        "line": 138,
        "name": "generate_password_reset_token",
        "parameters": [
          {
            "name": "email"
          }
        ],
        "purpose": "Purpose: Create JWT token for password reset with configured expiration",
        "signature": "generate_password_reset_token(email)"
      },
      {
        "line": 152,
        "name": "verify_password_reset_token",
        "parameters": [
          {
            "name": "token"
          }
        ],
        "purpose": "Purpose: Decode and validate password reset JWT, returning email if valid",
        "returns_doc": "str: Email from token subject, or None if token invalid/expired",
        "signature": "verify_password_reset_token(token)"
      }
    ],
    "language": "python",
    "lines": 165,
    "path": "backend/app/utils.py",
    "purpose": "Purpose: Provide email rendering, sending, and password reset token utilities\n\nStructure:\n    EmailData (dataclass): schema - Email content container (html_content, subject)\n    render_email_template (func): output - Render Jinja2 HTML email from template file\n    send_email (func): output - Send email via SMTP\n    generate_test_email (func): output - Build test email content\n    generate_reset_password_email (func): output - Build password reset email with token link\n    generate_new_account_email (func): output - Build new account welcome email\n    generate_password_reset_token (func): output - Create JWT token for password reset\n    verify_password_reset_token (func): output - Decode and validate password reset JWT\n\nRelationships:\n    Consumes: core.config.settings (SMTP_*, EMAILS_*, FRONTEND_HOST, SECRET_KEY)\n    Consumes: email-templates/build/*.html (Jinja2 templates)\n    Produces: EmailData, JWT tokens (consumed by api.routes.login)\n\nSemantics:\n    Domain: communication\n    Logic: [Reset tokens expire per EMAIL_RESET_TOKEN_EXPIRE_HOURS,\n            SMTP TLS/SSL configured from settings, templates in email-templates/build/]",
    "type": "module"
  },
  {
    "file": "__init__.py",
    "language": "python",
    "lines": 0,
    "path": "backend/tests/__init__.py",
    "type": "module"
  },
  {
    "file": "__init__.py",
    "language": "python",
    "lines": 0,
    "path": "backend/tests/api/__init__.py",
    "type": "module"
  },
  {
    "file": "__init__.py",
    "language": "python",
    "lines": 0,
    "path": "backend/tests/api/routes/__init__.py",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "app.core.config",
        "app.core.db",
        "app.main",
        "app.models",
        "collections.abc",
        "fastapi.testclient",
        "pytest",
        "sqlmodel",
        "tests.utils.user",
        "tests.utils.utils"
      ]
    },
    "file": "conftest.py",
    "functions": [
      {
        "line": 16,
        "name": "db",
        "signature": "db()"
      },
      {
        "line": 28,
        "name": "client",
        "signature": "client()"
      },
      {
        "line": 34,
        "name": "superuser_token_headers",
        "parameters": [
          {
            "name": "client"
          }
        ],
        "signature": "superuser_token_headers(client)"
      },
      {
        "line": 39,
        "name": "normal_user_token_headers",
        "parameters": [
          {
            "name": "client"
          },
          {
            "name": "db"
          }
        ],
        "signature": "normal_user_token_headers(client, db)"
      }
    ],
    "language": "python",
    "lines": 42,
    "path": "backend/tests/conftest.py",
    "type": "module"
  },
  {
    "file": "__init__.py",
    "language": "python",
    "lines": 0,
    "path": "backend/tests/crud/__init__.py",
    "type": "module"
  },
  {
    "file": "__init__.py",
    "language": "python",
    "lines": 0,
    "path": "backend/tests/scripts/__init__.py",
    "type": "module"
  },
  {
    "file": "__init__.py",
    "language": "python",
    "lines": 0,
    "path": "backend/tests/utils/__init__.py",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "app",
        "app.models",
        "sqlmodel",
        "tests.utils.user",
        "tests.utils.utils"
      ]
    },
    "file": "item.py",
    "functions": [
      {
        "line": 9,
        "name": "create_random_item",
        "parameters": [
          {
            "name": "db"
          }
        ],
        "signature": "create_random_item(db)"
      }
    ],
    "language": "python",
    "lines": 16,
    "path": "backend/tests/utils/item.py",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "app",
        "app.core.config",
        "app.models",
        "fastapi.testclient",
        "sqlmodel",
        "tests.utils.utils"
      ]
    },
    "file": "user.py",
    "functions": [
      {
        "line": 10,
        "name": "user_authentication_headers",
        "signature": "user_authentication_headers()"
      },
      {
        "line": 22,
        "name": "create_random_user",
        "parameters": [
          {
            "name": "db"
          }
        ],
        "signature": "create_random_user(db)"
      },
      {
        "line": 30,
        "name": "authentication_token_from_email",
        "purpose": "Return a valid token for the user with given email.",
        "signature": "authentication_token_from_email()"
      }
    ],
    "language": "python",
    "lines": 49,
    "path": "backend/tests/utils/user.py",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "app.core.config",
        "fastapi.testclient",
        "random",
        "string"
      ]
    },
    "file": "utils.py",
    "functions": [
      {
        "line": 9,
        "name": "random_lower_string",
        "signature": "random_lower_string()"
      },
      {
        "line": 13,
        "name": "random_email",
        "signature": "random_email()"
      },
      {
        "line": 17,
        "name": "get_superuser_token_headers",
        "parameters": [
          {
            "name": "client"
          }
        ],
        "signature": "get_superuser_token_headers(client)"
      }
    ],
    "language": "python",
    "lines": 26,
    "path": "backend/tests/utils/utils.py",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "pathlib"
      ]
    },
    "file": "__init__.py",
    "functions": [
      {
        "important": "Uses Path(__file__).parent which works with setuptools <70.0.\n    If you upgrade to setuptools 82.0+, this may become a namespace\n    package and __file__ will be None. The constraint in pyproject.toml\n    prevents this issue.",
        "line": 5,
        "name": "get_skills_directory",
        "purpose": "Return path to skills directory for AILA skill discovery.",
        "returns_doc": "Path: Path to skills directory inside this package",
        "signature": "get_skills_directory()"
      }
    ],
    "language": "python",
    "lines": 17,
    "path": "full_stack_fastapi_template/__init__.py",
    "purpose": "Skills provider for full-stack-fastapi-template",
    "type": "module"
  },
  {
    "dependencies": {
      "imports": [
        "pathlib"
      ]
    },
    "file": "post_gen_project.py",
    "language": "python",
    "lines": 8,
    "path": "hooks/post_gen_project.py",
    "type": "module"
  }
]
}
```

---

## Files

- **.copier/update_dotenv.py** - TODO
- **backend/app/__init__.py** - TODO
- **backend/app/alembic/env.py** - Purpose: Configure Alembic migration environment for online and offline modes

Structure:
    get_url (func): config - Return database URL from settings
    run_migrations_offline (func): migration - Run migrations without DB connection
    run_migrations_online (func): migration - Run migrations with live DB connection

Relationships:
    Consumes: app.models.SQLModel.metadata, app.core.config.settings.SQLALCHEMY_DATABASE_URI
    Produces: Database schema migrations

Important:
    app.models MUST be imported before target_metadata is set,
    otherwise Alembic won't detect model changes for autogenerate.
- **backend/app/alembic/versions/1a31ce608336_add_cascade_delete_relationships.py** - Add cascade delete relationships

Revision ID: 1a31ce608336
Revises: d98dd8ec85a3
Create Date: 2024-07-31 22:24:34.447891
- **backend/app/alembic/versions/9c0a54914c78_add_max_length_for_string_varchar_.py** - Add max length for string(varchar) fields in User and Items models

Revision ID: 9c0a54914c78
Revises: e2412789c190
Create Date: 2024-06-17 14:42:44.639457
- **backend/app/alembic/versions/d98dd8ec85a3_edit_replace_id_integers_in_all_models_.py** - Edit replace id integers in all models to use UUID instead

Revision ID: d98dd8ec85a3
Revises: 9c0a54914c78
Create Date: 2024-07-19 04:08:04.000976
- **backend/app/alembic/versions/e2412789c190_initialize_models.py** - Initialize models

Revision ID: e2412789c190
Revises:
Create Date: 2023-11-24 22:55:43.195942
- **backend/app/alembic/versions/fe56fa70289e_add_created_at_to_user_and_item.py** - Add created_at to User and Item

Revision ID: fe56fa70289e
Revises: 1a31ce608336
Create Date: 2026-01-23 15:50:37.171462
- **backend/app/api/__init__.py** - TODO
- **backend/app/api/deps.py** - Purpose: Provide FastAPI dependency injection for database sessions and authentication

Structure:
    get_db (func): dependency - Yield SQLModel session per request
    get_current_user (func): dependency - Decode JWT and return authenticated User
    get_current_active_superuser (func): dependency - Enforce superuser role
    SessionDep (type alias): shorthand - Annotated[Session, Depends(get_db)]
    TokenDep (type alias): shorthand - Annotated[str, Depends(reusable_oauth2)]
    CurrentUser (type alias): shorthand - Annotated[User, Depends(get_current_user)]

Relationships:
    Consumes: core.security.ALGORITHM, core.config.settings.SECRET_KEY, core.db.engine
    Consumes: models.TokenPayload, models.User
    Produces: Session, User (injected into route handlers)
- **backend/app/api/main.py** - Purpose: Register all API route modules into the main API router

Structure:
    api_router (APIRouter): output - Combined router with all route modules

Relationships:
    Consumes: api.routes.login, api.routes.users, api.routes.utils, api.routes.items, api.routes.private
    Produces: api_router (consumed by app.main)

Note:
    Private routes only registered when ENVIRONMENT=local.
- **backend/app/api/routes/__init__.py** - TODO
- **backend/app/api/routes/items.py** - Purpose: Provide CRUD API endpoints for Item resources with owner-based access control

Structure:
    read_items (GET /): endpoint - List items (all for superuser, own for regular user)
    read_item (GET /{id}): endpoint - Get single item by ID
    create_item (POST /): endpoint - Create item owned by current user
    update_item (PUT /{id}): endpoint - Update item (owner or superuser only)
    delete_item (DELETE /{id}): endpoint - Delete item (owner or superuser only)

Relationships:
    Consumes: models.Item, models.ItemCreate, models.ItemUpdate, api.deps.CurrentUser
    Produces: ItemPublic, ItemsPublic, Message responses

Semantics:
    Domain: content
    Entity: Item
    Logic: [Superusers see all items, regular users see only their own,
            owner or superuser required for read/update/delete of specific items]
- **backend/app/api/routes/login.py** - Purpose: Provide authentication endpoints for login, token validation, and password recovery

Structure:
    login_access_token (POST /login/access-token): endpoint - OAuth2 token login
    test_token (POST /login/test-token): endpoint - Validate access token
    recover_password (POST /password-recovery/{email}): endpoint - Send password reset email
    reset_password (POST /reset-password/): endpoint - Reset password with token
    recover_password_html_content (POST /password-recovery-html-content/{email}): endpoint - Preview reset email HTML (superuser only)

Relationships:
    Consumes: crud.authenticate, crud.get_user_by_email, crud.update_user
    Consumes: utils.generate_password_reset_token, utils.generate_reset_password_email, utils.send_email
    Produces: Token, UserPublic, Message responses

Semantics:
    Domain: authentication
    Logic: [Password recovery returns same response regardless of email existence (prevents enumeration),
            Reset tokens expire per EMAIL_RESET_TOKEN_EXPIRE_HOURS setting]
- **backend/app/api/routes/private.py** - Purpose: Provide private admin endpoint for user creation (local environment only)

Structure:
    PrivateUserCreate (class): schema - User creation without SQLModel validation
    create_user (POST /private/users/): endpoint - Create user directly

Relationships:
    Consumes: models.User, core.security.get_password_hash
    Produces: UserPublic response, User table row

Note:
    Only registered when ENVIRONMENT=local (see api/main.py).
- **backend/app/api/routes/users.py** - Purpose: Provide CRUD API endpoints for User management with role-based access control

Structure:
    read_users (GET /): endpoint - List users (superuser only)
    create_user (POST /): endpoint - Create user (superuser only)
    update_user_me (PATCH /me): endpoint - Update own profile
    update_password_me (PATCH /me/password): endpoint - Change own password
    read_user_me (GET /me): endpoint - Get own profile
    delete_user_me (DELETE /me): endpoint - Delete own account (non-superuser only)
    register_user (POST /signup): endpoint - Public self-registration
    read_user_by_id (GET /{user_id}): endpoint - Get user by ID
    update_user (PATCH /{user_id}): endpoint - Update user (superuser only)
    delete_user (DELETE /{user_id}): endpoint - Delete user (superuser only)

Relationships:
    Consumes: crud (create_user, update_user, get_user_by_email), models (User, Item, schemas)
    Consumes: utils.generate_new_account_email, utils.send_email
    Produces: UserPublic, UsersPublic, Message responses

Semantics:
    Domain: identity
    Entity: User
    Logic: [Superusers cannot delete themselves, email uniqueness enforced,
            new account email sent if SMTP configured, items cascade-deleted with user]
- **backend/app/api/routes/utils.py** - Purpose: Provide utility endpoints for health checks and email testing

Structure:
    test_email (POST /utils/test-email/): endpoint - Send test email (superuser only)
    health_check (GET /utils/health-check/): endpoint - Application health check

Relationships:
    Consumes: utils.generate_test_email, utils.send_email
    Produces: Message response, bool response
- **backend/app/backend_pre_start.py** - Purpose: Wait for database readiness before application startup with retry logic

Structure:
    init (func): setup - Attempt DB connection with tenacity retry
    main (func): entry - Script entry point

Relationships:
    Consumes: core.db.engine
    Produces: (blocks until DB is ready)

Semantics:
    Logic: [Retries every 1 second for up to 5 minutes (300 attempts)]

Note:
    Run via scripts/prestart.sh before alembic migrations and initial_data.
- **backend/app/core/__init__.py** - TODO
- **backend/app/core/config.py** - Purpose: Load and validate all application settings from environment variables and .env file

Structure:
    Settings (class): config - Pydantic settings with validation for DB, auth, email, CORS
    parse_cors (func): config - Parse CORS origins from comma-separated string or list
    settings (Settings): output - Singleton settings instance

Relationships:
    Consumes: ../.env file, environment variables
    Produces: settings (consumed by all backend modules)

Semantics:
    Domain: configuration
    Logic: [Warns on default secrets in local, raises in staging/production,
            SQLALCHEMY_DATABASE_URI computed from POSTGRES_* fields,
            emails_enabled computed from SMTP_HOST + EMAILS_FROM_EMAIL]

Important:
    SECRET_KEY, POSTGRES_PASSWORD, and FIRST_SUPERUSER_PASSWORD MUST NOT be
    "changethis" in staging/production — validation will raise ValueError.
- **backend/app/core/db.py** - Purpose: Initialize database engine and seed first superuser on startup

Structure:
    engine (Engine): config - SQLAlchemy engine from settings
    init_db (func): output - Create first superuser if not exists

Relationships:
    Consumes: core.config.settings (SQLALCHEMY_DATABASE_URI, FIRST_SUPERUSER, FIRST_SUPERUSER_PASSWORD)
    Consumes: crud.create_user
    Produces: first superuser row in user table

Important:
    All SQLModel models MUST be imported (via app.models) before init_db runs,
    otherwise SQLModel fails to initialize relationships.
    Tables are created by Alembic migrations, NOT by init_db.
- **backend/app/core/security.py** - Purpose: Provide JWT token creation and password hashing/verification

Structure:
    create_access_token (func): output - Create signed JWT with expiration
    verify_password (func): output - Verify password and return upgraded hash if applicable
    get_password_hash (func): output - Hash password with Argon2
    password_hash (PasswordHash): config - Multi-hasher supporting Argon2 and bcrypt
    ALGORITHM (str): config - JWT signing algorithm (HS256)

Relationships:
    Consumes: core.config.settings.SECRET_KEY
    Produces: JWT tokens, password hashes (consumed by crud, api.deps)

Semantics:
    Domain: security
    Logic: [Argon2 is primary hasher, bcrypt supported for legacy upgrade,
            verify_and_update returns new hash when bcrypt→argon2 upgrade needed]
- **backend/app/crud.py** - Purpose: Provide CRUD operations for User and Item database entities

Structure:
    create_user (func): output - Create user with hashed password
    update_user (func): output - Update user fields, re-hash if password changed
    get_user_by_email (func): output - Look up user by email
    authenticate (func): output - Verify email/password, upgrade hash if needed
    create_item (func): output - Create item with owner assignment

Relationships:
    Consumes: models.User, models.Item, models.UserCreate, models.UserUpdate, models.ItemCreate
    Consumes: core.security.get_password_hash, core.security.verify_password
    Produces: User rows, Item rows

Semantics:
    Domain: identity, content
    Logic: [Timing-attack prevention via dummy hash on failed lookup,
            Auto-upgrade bcrypt→argon2 on successful login]

Important:
    authenticate() MUST run verify_password even when user not found
    to prevent timing-based email enumeration attacks.
- **backend/app/initial_data.py** - Purpose: Seed initial database data (first superuser) on application startup

Structure:
    init (func): setup - Open session and call init_db
    main (func): entry - Script entry point with logging

Relationships:
    Consumes: core.db.engine, core.db.init_db
    Produces: first superuser in user table

Note:
    Run via: python app/initial_data.py (or uv run python app/initial_data.py)
    Also called by scripts/prestart.sh before app starts.
- **backend/app/main.py** - Purpose: Initialize FastAPI application with CORS, Sentry, and API router

Structure:
    app (FastAPI): output - Configured FastAPI application instance
    custom_generate_unique_id (func): config - Generate OpenAPI operation IDs from route tag + name

Relationships:
    Consumes: core.config.settings, api.main.api_router
    Produces: FastAPI app (consumed by uvicorn)

Semantics:
    Domain: application
    Logic: [Sentry enabled only in non-local environments, CORS origins from settings]
- **backend/app/models.py** - Purpose: Define all SQLModel database tables and Pydantic API schemas for User and Item entities

Structure:
    User (table): entity - User account with auth and profile data
    Item (table): entity - User-owned content item
    UserBase, UserCreate, UserUpdate, UserRegister, UserUpdateMe, UpdatePassword: schema - User API schemas
    UserPublic, UsersPublic: schema - User response schemas
    ItemBase, ItemCreate, ItemUpdate: schema - Item API schemas
    ItemPublic, ItemsPublic: schema - Item response schemas
    Token, TokenPayload, NewPassword, Message: schema - Auth and utility schemas

Relationships:
    Produces: user table, item table
    Consumes: (consumed by) api.routes, crud, core.db

Semantics:
    Domain: identity, content
    Entity: User, Item
    Logic: [Items cascade-delete with owner, UUIDs as primary keys, created_at auto-set to UTC]

Important:
    All SQLModel table classes MUST be imported before Alembic or init_db runs,
    otherwise relationships fail to initialize. See core/db.py comment.
- **backend/app/tests_pre_start.py** - Purpose: Wait for database readiness before test suite execution with retry logic

Structure:
    init (func): setup - Attempt DB connection with tenacity retry
    main (func): entry - Script entry point

Relationships:
    Consumes: core.db.engine
    Produces: (blocks until DB is ready)

Semantics:
    Logic: [Retries every 1 second for up to 5 minutes (300 attempts)]

Note:
    Run via scripts/tests-start.sh before pytest.
- **backend/app/utils.py** - Purpose: Provide email rendering, sending, and password reset token utilities

Structure:
    EmailData (dataclass): schema - Email content container (html_content, subject)
    render_email_template (func): output - Render Jinja2 HTML email from template file
    send_email (func): output - Send email via SMTP
    generate_test_email (func): output - Build test email content
    generate_reset_password_email (func): output - Build password reset email with token link
    generate_new_account_email (func): output - Build new account welcome email
    generate_password_reset_token (func): output - Create JWT token for password reset
    verify_password_reset_token (func): output - Decode and validate password reset JWT

Relationships:
    Consumes: core.config.settings (SMTP_*, EMAILS_*, FRONTEND_HOST, SECRET_KEY)
    Consumes: email-templates/build/*.html (Jinja2 templates)
    Produces: EmailData, JWT tokens (consumed by api.routes.login)

Semantics:
    Domain: communication
    Logic: [Reset tokens expire per EMAIL_RESET_TOKEN_EXPIRE_HOURS,
            SMTP TLS/SSL configured from settings, templates in email-templates/build/]
- **backend/tests/__init__.py** - TODO
- **backend/tests/api/__init__.py** - TODO
- **backend/tests/api/routes/__init__.py** - TODO
- **backend/tests/conftest.py** - TODO
- **backend/tests/crud/__init__.py** - TODO
- **backend/tests/scripts/__init__.py** - TODO
- **backend/tests/utils/__init__.py** - TODO
- **backend/tests/utils/item.py** - TODO
- **backend/tests/utils/user.py** - TODO
- **backend/tests/utils/utils.py** - TODO
- **full_stack_fastapi_template/__init__.py** - Skills provider for full-stack-fastapi-template
- **hooks/post_gen_project.py** - TODO
