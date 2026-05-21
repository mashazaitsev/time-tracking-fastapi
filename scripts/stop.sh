#!/usr/bin/env bash
# Stop all services: Frontend, Backend, PostgreSQL
set -e

LOG_DIR="/tmp/fastapi-template"

echo "🛑 Stopping Full Stack FastAPI Template..."

# 1. Frontend
if lsof -ti:5173 >/dev/null 2>&1; then
    kill $(lsof -t -i:5173) 2>/dev/null
    echo "✅ Frontend stopped"
else
    echo "⏭️  Frontend not running"
fi

# 2. Backend
if lsof -ti:8000 >/dev/null 2>&1; then
    kill $(lsof -t -i:8000) 2>/dev/null
    echo "✅ Backend stopped"
else
    echo "⏭️  Backend not running"
fi

# 3. PostgreSQL
if pg_isready -q 2>/dev/null; then
    sudo systemctl stop postgresql
    echo "✅ PostgreSQL stopped"
else
    echo "⏭️  PostgreSQL not running"
fi

# Clean up PID files
rm -f "$LOG_DIR/backend.pid" "$LOG_DIR/frontend.pid"

echo ""
echo "All services stopped."
