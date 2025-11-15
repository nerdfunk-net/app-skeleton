import { DashboardLayout } from '@/components/dashboard-layout'

export default function Home() {
  return (
    <DashboardLayout>
      <div className="flex flex-col items-center justify-center min-h-[60vh] space-y-4">
        <h1 className="text-4xl font-bold">Welcome to Your App</h1>
        <p className="text-muted-foreground text-center max-w-md">
          This is a minimal template with authentication, user management, and role-based access control.
        </p>
      </div>
    </DashboardLayout>
  )
}
