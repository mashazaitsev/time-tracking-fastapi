# Bootstrap: Full Stack FastAPI Template (No Docker)

## Your Task

Install all dependencies and prepare the local development environment for the Full Stack FastAPI Template. This runs everything natively — no Docker required.

---

## Prerequisites

The following tools are needed. Install any that are missing.

### 1. Python 3.10+

```bash
python3 --version
```

If missing: `sudo apt-get install -y python3 python3-pip`

### 2. uv (Python package manager)

```bash
uv --version
```

If missing:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. Node.js 18+ and npm

```bash
node --version && npm --version
```

If missing: `sudo apt-get install -y nodejs npm`

### 4. PostgreSQL 14+

```bash
psql --version
```

If missing:
```bash
sudo apt-get update -qq
sudo apt-get install -y postgresql postgresql-client
```

---

## Setup Steps

### Step 1: Start PostgreSQL and Create Database

```bash
sudo systemctl start postgresql

# Create database and set password (matches .env defaults)
sudo -u postgres psql -c "CREATE DATABASE app;"
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'changethis';"
```

### Step 2: Install Backend Dependencies

```bash
cd backend
uv sync
```

If `uv` is not available, use pip:
```bash
cd backend
pip install -e ".[dev]"
```

### Step 3: Run Database Migrations and Seed Data

```bash
cd backend
uv run alembic upgrade head
uv run python app/initial_data.py
```

### Step 4: Install Frontend Dependencies

```bash
cd frontend
npm install
```

### Step 5: Install Playwright Browsers

Playwright is used for E2E testing. Install the browser binaries:

```bash
cd frontend
npx playwright install --with-deps chromium
```

### Step 6: Install Root Dependencies (Playwright scripting)

The root `package.json` needs the `playwright` package for automation/debugging scripts:

```bash
cd /path/to/project  # project root, not frontend/
npm install playwright --save-dev
```

### Step 7: Start the App

From the project root:

```bash
bash scripts/start.sh
```

### Step 8: Verify

| Service        | URL                        |
|----------------|----------------------------|
| Frontend       | http://localhost:5173       |
| Backend API    | http://localhost:8000       |
| Swagger Docs   | http://localhost:8000/docs  |

Login: `admin@example.com` / `changethis`

---

## Stop the App

```bash
bash scripts/stop.sh
```

---

## Known Issues & Fixes

### IPv6 localhost Resolution (CRITICAL)

Some systems resolve `localhost` to `::1` (IPv6), but uvicorn binds to `127.0.0.1` (IPv4 only). This causes the browser to get 404/connection refused while `curl` works fine.

**Check:** `getent hosts localhost` — if it shows `::1`, you have this issue.

**Fix:** Apply both changes:

1. `frontend/.env` — use `127.0.0.1` instead of `localhost`:
```
VITE_API_URL=http://127.0.0.1:8000
```

2. `.env` — add `127.0.0.1` to CORS origins:
```
BACKEND_CORS_ORIGINS="http://localhost,http://localhost:5173,https://localhost,https://localhost:5173,http://localhost.tiangolo.com,http://127.0.0.1:5173"
```

Then restart both backend and frontend, and access the app at `http://127.0.0.1:5173`.

### Pre-existing recover-password.tsx Bug

`frontend/src/routes/recover-password.tsx` has a broken Zod schema that crashes Vite's TanStack Router code-splitter.

**Fix:** Replace lines 33-35:
```typescript
// BROKEN:
const formSchema = z.object({

type FormData = z.infer<typeof formSchema>

// FIXED:
const formSchema = z.object({
  email: z.string().email(),
})

type FormData = z.infer<typeof formSchema>
```

### Stale Processes on Ports

Repeated restarts can leave orphan processes. Always clean up before starting:
```bash
lsof -ti:8000 -ti:5173 | xargs kill -9 2>/dev/null
```

### Vite Cache

If Vite shows errors that don't match the code on disk, clear the cache:
```bash
cd frontend && rm -rf node_modules/.vite
```

---

## Troubleshooting

**PostgreSQL won't start:**
```bash
sudo systemctl status postgresql
sudo journalctl -u postgresql --no-pager -n 20
```

**Port already in use:**
```bash
lsof -ti:5173 -ti:8000 | xargs kill -9 2>/dev/null
```

**Backend can't connect to database:**
- Verify PostgreSQL is running: `pg_isready`
- Check `.env` values match your PostgreSQL setup
- Ensure `pg_hba.conf` allows password auth for localhost connections

**Migrations fail:**
- Ensure database `app` exists: `sudo -u postgres psql -c "\l"`
- Check `.env` has correct `POSTGRES_*` values

**Login returns "Incorrect email or password":**
- The superuser hasn't been created. Run: `cd backend && uv run python app/initial_data.py`

**Browser shows 404 but curl works:**
- See "IPv6 localhost Resolution" above
