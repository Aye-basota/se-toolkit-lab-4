# Learning Management Service — Full-Stack Platform

A full-stack learning management system with a tested backend, React frontend, and AI-assisted development workflow.

## Features

- FastAPI backend with comprehensive test suite (unit + e2e)
- React + Vite frontend with data visualization
- Swagger UI for API exploration
- CI/CD with GitHub Actions
- Dockerized deployment

## Tech stack

**Backend:** Python 3.12+, FastAPI, PostgreSQL, pytest  
**Frontend:** React, TypeScript, Vite  
**DevOps:** Docker, Docker Compose, Caddy, GitHub Actions  
**Tools:** AI coding agents for test generation and frontend tuning

## Quick start

```bash
# Backend
cd backend && uv sync && uv run fastapi dev src/app/main.py

# Frontend
cd frontend && npm install && npm run dev

# Full stack
docker compose up --build
```

## Project structure

- `backend/` — FastAPI + tests
- `frontend/` — React application
- `docker-compose.yml` — full stack
