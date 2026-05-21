#!/usr/bin/env bash
# Start all services: PostgreSQL, Backend, Frontend
set -e

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
BACKEND_DIR="$ROOT_DIR/backend"
FRONTEND_DIR="$ROOT_DIR/frontend"
LOG_DIR="/tmp/fastapi-template"

mkdir -p "$LOG_DIR"

echo "🚀 Starting Full Stack FastAPI Template..."

# 1. PostgreSQL
echo "📦 Starting PostgreSQL..."
if ! pg_isready -q 2>/dev/null; then
    sudo systemctl start postgresql
    sleep 2
    if ! pg_isready -q 2>/dev/null; then
        echo "❌ PostgreSQL failed to start"
        exit 1
    fi
fi
echo "✅ PostgreSQL is running"

# 2. Backend
echo "📦 Starting Backend..."
if lsof -ti:8000 >/dev/null 2>&1; then
    echo "⚠️  Port 8000 already in use, killing existing process..."
    kill $(lsof -t -i:8000) 2>/dev/null
    sleep 1
fi

cd "$BACKEND_DIR"
nohup uv run fastapi dev app/main.py > "$LOG_DIR/backend.log" 2>&1 &
echo $! > "$LOG_DIR/backend.pid"

# Wait for backend to be ready
echo "   Waiting for backend..."
for i in $(seq 1 30); do
    if curl -s http://localhost:8000/api/v1/utils/health-check/ >/dev/null 2>&1; then
        echo "✅ Backend is running at http://localhost:8000"
        break
    fi
    if [ "$i" -eq 30 ]; then
        echo "❌ Backend failed to start. Check $LOG_DIR/backend.log"
        exit 1
    fi
    sleep 1
done

# 3. Frontend
echo "📦 Starting Frontend..."
if lsof -ti:5173 >/dev/null 2>&1; then
    echo "⚠️  Port 5173 already in use, killing existing process..."
    kill $(lsof -t -i:5173) 2>/dev/null
    sleep 1
fi

cd "$FRONTEND_DIR"
nohup npm run dev > "$LOG_DIR/frontend.log" 2>&1 &
echo $! > "$LOG_DIR/frontend.pid"

# Wait for frontend to be ready
echo "   Waiting for frontend..."
for i in $(seq 1 30); do
    if curl -s -o /dev/null http://localhost:5173 2>/dev/null; then
        echo "✅ Frontend is running at http://localhost:5173"
        break
    fi
    if [ "$i" -eq 30 ]; then
        echo "❌ Frontend failed to start. Check $LOG_DIR/frontend.log"
        exit 1
    fi
    sleep 1
done

echo ""
echo "========================================="
echo "  All services running!"
echo "========================================="
echo "  Frontend:     http://localhost:5173"
echo "  Backend API:  http://localhost:8000"
echo "  Swagger Docs: http://localhost:8000/docs"
echo ""
echo "  Login: admin@example.com / changethis"
echo ""
echo "  Logs: $LOG_DIR/"
echo "  Stop: bash $ROOT_DIR/scripts/stop.sh"
echo "========================================="
