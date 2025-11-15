# App Template

A minimal full-stack application template with authentication, user management, and role-based access control (RBAC).

## Features

- **Authentication**: JWT-based authentication with login/logout
- **User Management**: Create, read, update, and delete users
- **RBAC**: Role-based access control with permissions and roles
- **Profile Management**: User profile viewing and editing
- **Modern UI**: Next.js 15 with Tailwind CSS and Radix UI components
- **FastAPI Backend**: Python FastAPI with SQLite database
- **Sidebar Navigation**: Collapsible sidebar with role-based menu items

## Tech Stack

### Frontend
- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **UI Components**: Radix UI
- **State Management**: Zustand
- **Icons**: Lucide React

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.9+
- **Database**: SQLite
- **Authentication**: JWT with passlib
- **ORM**: SQLAlchemy

## Project Structure

```
app-template/
├── frontend/                # Next.js frontend application
│   ├── src/
│   │   ├── app/            # Next.js app router pages
│   │   │   ├── auth/       # Authentication pages
│   │   │   ├── profile/    # Profile page
│   │   │   ├── settings/   # Settings pages
│   │   │   │   └── permissions/  # User & permissions management
│   │   │   ├── login/      # Login page
│   │   │   ├── layout.tsx  # Root layout
│   │   │   └── page.tsx    # Home page
│   │   ├── components/     # React components
│   │   │   ├── app-sidebar.tsx    # Main sidebar
│   │   │   ├── dashboard-layout.tsx  # Dashboard wrapper
│   │   │   ├── auth/       # Auth components
│   │   │   ├── profile/    # Profile components
│   │   │   ├── settings/   # Settings components
│   │   │   ├── shared/     # Shared components
│   │   │   └── ui/         # UI primitives
│   │   ├── contexts/       # React contexts
│   │   ├── hooks/          # Custom hooks
│   │   └── lib/            # Utilities
│   └── package.json
│
├── backend/                # FastAPI backend application
│   ├── routers/           # API route handlers
│   │   ├── auth.py        # Authentication endpoints
│   │   ├── profile.py     # Profile endpoints
│   │   ├── user_management.py  # User CRUD endpoints
│   │   └── rbac.py        # RBAC endpoints
│   ├── models/            # Pydantic models
│   │   ├── auth.py        # Auth models
│   │   ├── user_management.py  # User models
│   │   └── rbac.py        # RBAC models
│   ├── services/          # Business logic
│   │   └── user_management.py  # User service
│   ├── core/              # Core utilities
│   │   ├── auth.py        # Auth utilities
│   │   └── config.py      # Configuration
│   ├── config.py          # Settings
│   ├── user_db_manager.py # User database operations
│   ├── rbac_manager.py    # RBAC database operations
│   ├── profile_manager.py # Profile operations
│   ├── health.py          # Health check endpoints
│   ├── main.py            # Application entry point
│   └── requirements.txt
│
├── config/                # Configuration files
│   └── oidc_providers.yaml.example  # OIDC config example
│
├── data/                  # Data storage
│   └── settings/          # App settings and databases
│       ├── users.db       # User database
│       └── rbac.db        # RBAC database
│
└── LICENSE
```

## Getting Started

### Prerequisites

- **Node.js**: 18+ and npm
- **Python**: 3.9+
- **pip**: Python package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd app-template
   ```

2. **Setup Backend**
   ```bash
   cd backend
   
   # Create virtual environment (optional but recommended)
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Create .env file (optional)
   cat > .env << EOF
   SECRET_KEY=your-secret-key-change-in-production
   INITIAL_USERNAME=admin
   INITIAL_PASSWORD=admin
   BACKEND_SERVER_PORT=8000
   EOF
   ```

3. **Setup Frontend**
   ```bash
   cd ../frontend
   
   # Install dependencies
   npm install
   ```

### Running the Application

1. **Start Backend** (from `backend/` directory)
   ```bash
   python start.py
   # Or use uvicorn directly:
   # uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```
   
   Backend will run at: http://localhost:8000
   API docs: http://localhost:8000/docs

2. **Start Frontend** (from `frontend/` directory)
   ```bash
   npm run dev
   ```
   
   Frontend will run at: http://localhost:3000

3. **Login**
   - Navigate to http://localhost:3000/login
   - Default credentials: `admin` / `admin`
   - Change these in production!

## Default Users

The system comes with a default admin user:
- **Username**: admin
- **Password**: admin
- **Role**: admin
- **Permissions**: Full access

**Important**: Change the default password immediately in production!

## Database

The application uses SQLite databases stored in `data/settings/`:
- `users.db`: User accounts and authentication
- `rbac.db`: Roles, permissions, and access control

These databases are automatically created on first run.

## API Documentation

Once the backend is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Configuration

### Backend Configuration

Edit `backend/.env` or set environment variables:

```bash
# Server
BACKEND_SERVER_HOST=127.0.0.1
BACKEND_SERVER_PORT=8000
DEBUG=true

# Authentication
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10

# Initial Admin User
INITIAL_USERNAME=admin
INITIAL_PASSWORD=admin

# Data Storage
DATA_DIRECTORY=../data
```

### Frontend Configuration

The frontend connects to the backend at `http://localhost:8000` by default.

To change this, update the API base URL in frontend code if needed.

## User Roles and Permissions

### Built-in Roles

- **admin**: Full system access
- **operator**: Standard user access
- **viewer**: Read-only access

### Permission System

Permissions are organized by resource and action:
- **Resource**: The entity being accessed (e.g., users, settings)
- **Action**: The operation (read, write, delete, admin)

Admins can create custom roles and assign permissions through the UI at `/settings/permissions`.

## Development

### Backend Development

```bash
cd backend

# Run with auto-reload
uvicorn main:app --reload

# Run tests (if available)
pytest

# Format code
black .
```

### Frontend Development

```bash
cd frontend

# Run development server
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Lint code
npm run lint

# Type check
npm run type-check
```

## Building for Production

### Backend

```bash
cd backend

# The application can run with uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000

# Or use gunicorn for production
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Frontend

```bash
cd frontend

# Build
npm run build

# Start production server
npm start
```

## Customization

This template is designed to be easily customizable:

1. **Branding**: Update titles in `frontend/src/app/layout.tsx` and `backend/main.py`
2. **Styling**: Modify Tailwind config in `frontend/tailwind.config.ts`
3. **Permissions**: Add custom permissions via the UI or database
4. **Routes**: Add new pages in `frontend/src/app/` and routes in `backend/routers/`
5. **Components**: Create reusable components in `frontend/src/components/`

## Security Notes

- Change default admin password immediately
- Use strong `SECRET_KEY` in production
- Enable HTTPS in production
- Regularly update dependencies
- Review and customize CORS settings in `backend/main.py`
- Never commit `.env` files or secrets to version control

## License

See [LICENSE](LICENSE) file for details.

## Support

For issues and questions, please open an issue in the repository.
