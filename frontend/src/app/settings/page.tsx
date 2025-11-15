import Link from 'next/link'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Users } from 'lucide-react'

const settingsPages = [
  {
    title: 'User Management',
    description: 'Manage system users and permissions',
    href: '/settings/permissions',
    icon: Users,
    color: 'text-indigo-600',
    bgColor: 'bg-indigo-100'
  }
]

export default function SettingsPage() {
  return (
    <div className="space-y-6">
      {/* Page Header */}
      <div className="border-b border-gray-200 pb-4">
        <div className="flex items-center space-x-3">
          <div className="bg-gray-100 p-2 rounded-lg">
            <Users className="h-6 w-6 text-gray-600" />
          </div>
          <div>
            <h1 className="text-2xl font-semibold text-gray-900">Settings</h1>
            <p className="text-gray-600">Configure your application settings</p>
          </div>
        </div>
      </div>

      {/* Settings Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {settingsPages.map((setting) => {
          const IconComponent = setting.icon
          return (
            <Link key={setting.href} href={setting.href}>
              <Card className="hover:shadow-lg transition-shadow cursor-pointer group">
                <CardHeader>
                  <div className="flex items-center space-x-3">
                    <div className={`p-2 rounded-lg ${setting.bgColor} group-hover:scale-110 transition-transform`}>
                      <IconComponent className={`h-6 w-6 ${setting.color}`} />
                    </div>
                    <div>
                      <CardTitle className="text-lg">{setting.title}</CardTitle>
                    </div>
                  </div>
                </CardHeader>
                <CardContent>
                  <CardDescription className="text-gray-600">
                    {setting.description}
                  </CardDescription>
                </CardContent>
              </Card>
            </Link>
          )
        })}
      </div>
    </div>
  )
}
