# Frontend - App Template

A modern, minimal web application frontend built with Next.js, TypeScript, and Tailwind CSS.

## Features

- 🔐 **JWT Authentication**: Secure login system with persistent sessions
- 📱 **Responsive Layout**: Desktop-first design with mobile compatibility
- 🧭 **Sidebar Navigation**: Collapsible navigation with role-based access
- ⚡ **Modern Stack**: Next.js 15 with App Router, TypeScript, and Radix UI

## Technology Stack

- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS v4
- **UI Components**: Radix UI
- **Icons**: Lucide React
- **State Management**: Zustand
- **Authentication**: JWT with localStorage persistence

## Project Structure

```
src/
├── app/
│   ├── auth/              # Auth pages (OIDC callback)
│   ├── login/            # Login page
│   ├── profile/          # User profile page
│   ├── settings/         # Settings pages
│   │   └── permissions/  # User & permissions management
│   ├── layout.tsx        # Root layout with auth
│   └── page.tsx          # Dashboard home
├── components/
│   ├── auth/             # Auth components
│   ├── profile/          # Profile components
│   ├── settings/         # Settings components
│   │   └── permissions/  # User & RBAC management
│   ├── shared/           # Shared utilities
│   ├── ui/               # Radix UI components
│   ├── app-sidebar.tsx   # Main navigation sidebar
│   └── dashboard-layout.tsx  # Main layout wrapper
├── contexts/             # React contexts
├── hooks/                # Custom React hooks
└── lib/
    ├── auth-store.ts     # Authentication state
    └── utils.ts          # Utilities
```

## Getting Started

### Prerequisites

- Node.js 18+
- npm or yarn

### Installation

```bash
# Install dependencies
npm install
```

### Development

```bash
# Start development server
npm run dev

# Open http://localhost:3000
```

### Build

```bash
# Build for production
npm run build

# Start production server
npm start
```

## Scripts

- `npm run dev` - Start development server with Turbopack
- `npm run build` - Build for production
- `npm start` - Start production server
- `npm run lint` - Run ESLint
- `npm run lint:fix` - Fix ESLint issues
- `npm run type-check` - Run TypeScript type checking
- `npm run format` - Format code with Prettier
- `npm run check` - Run all checks (type-check, lint, format)

## Authentication

The app uses JWT-based authentication:

1. User logs in at `/login`
2. JWT token is stored in localStorage
3. Token is sent with all API requests
4. Token auto-refreshes before expiration
5. User is redirected to login on token expiry

## API Integration

The frontend connects to the backend API at `http://localhost:8000` by default.

API endpoints:
- `POST /auth/login` - Login
- `POST /auth/refresh` - Refresh token
- `GET /profile` - Get user profile
- `GET /user-management` - List users (admin)
- `GET /api/rbac/*` - RBAC endpoints

## Environment Variables

Create `.env.local` for local overrides:

```bash
# Backend API URL (if different from localhost:8000)
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Customization

### Styling

- Tailwind config: `tailwind.config.ts`
- Global styles: `src/app/globals.css`
- Color scheme: Defined in globals.css CSS variables

### Components

- UI primitives: `src/components/ui/` (Radix UI)
- Custom components: `src/components/`
- Layout: `src/components/dashboard-layout.tsx`
- Sidebar: `src/components/app-sidebar.tsx`

### Routes

Add new pages in `src/app/`:
- Create `src/app/your-page/page.tsx`
- Wrap with `<DashboardLayout>` for authenticated pages
- Add to sidebar in `src/components/app-sidebar.tsx`

## Code Quality

This project uses:
- **TypeScript** for type safety
- **ESLint** for linting
- **Prettier** for code formatting
- **Strict mode** for React

Run checks before committing:
```bash
npm run check
```

## License

See [LICENSE](../LICENSE) file for details.
