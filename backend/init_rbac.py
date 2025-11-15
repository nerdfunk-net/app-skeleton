"""
Initialize RBAC system with default roles and permissions.
Run this once to set up the RBAC database.
"""

import sys
import os

# Add backend directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import after path is set
import rbac_manager as rbac
from user_db_manager import get_user_by_username

def init_rbac():
    """Initialize RBAC system with default roles and permissions."""
    
    print("Initializing RBAC system...")
    
    # Create default permissions
    permissions = [
        ("users", "read", "View users"),
        ("users", "write", "Create and edit users"),
        ("users", "delete", "Delete users"),
        ("users", "admin", "Full user management"),
        ("settings", "read", "View settings"),
        ("settings", "write", "Modify settings"),
        ("rbac", "read", "View roles and permissions"),
        ("rbac", "write", "Manage roles and permissions"),
    ]
    
    for resource, action, description in permissions:
        try:
            rbac.create_permission(resource, action, description)
            print(f"✓ Created permission: {resource}:{action}")
        except ValueError as e:
            if "already exists" in str(e):
                print(f"  Permission already exists: {resource}:{action}")
            else:
                print(f"✗ Error creating permission {resource}:{action}: {e}")
    
    # Create default roles
    roles = [
        ("admin", "Administrator with full access", True),
        ("operator", "Standard user with read/write access", True),
        ("viewer", "Read-only access", True),
    ]
    
    for name, description, is_system in roles:
        try:
            role = rbac.create_role(name, description, is_system)
            print(f"✓ Created role: {name}")
        except ValueError as e:
            if "already exists" in str(e):
                role = rbac.get_role_by_name(name)
                print(f"  Role already exists: {name}")
            else:
                print(f"✗ Error creating role {name}: {e}")
                continue
    
    # Assign permissions to admin role
    admin_role = rbac.get_role_by_name("admin")
    if admin_role:
        all_permissions = rbac.list_permissions()
        for perm in all_permissions:
            try:
                rbac.assign_permission_to_role(admin_role["id"], perm["id"])
            except ValueError:
                pass  # Already assigned
        print(f"✓ Assigned all permissions to admin role")
    
    # Assign permissions to operator role
    operator_role = rbac.get_role_by_name("operator")
    if operator_role:
        operator_perms = ["users:read", "users:write", "settings:read", "settings:write", "rbac:read"]
        for perm_str in operator_perms:
            resource, action = perm_str.split(":")
            perm = rbac.get_permission(resource, action)
            if perm:
                try:
                    rbac.assign_permission_to_role(operator_role["id"], perm["id"])
                except ValueError:
                    pass
        print(f"✓ Assigned operator permissions")
    
    # Assign permissions to viewer role
    viewer_role = rbac.get_role_by_name("viewer")
    if viewer_role:
        viewer_perms = ["users:read", "settings:read", "rbac:read"]
        for perm_str in viewer_perms:
            resource, action = perm_str.split(":")
            perm = rbac.get_permission(resource, action)
            if perm:
                try:
                    rbac.assign_permission_to_role(viewer_role["id"], perm["id"])
                except ValueError:
                    pass
        print(f"✓ Assigned viewer permissions")
    
    # Assign admin role to admin user
    admin_user = get_user_by_username("admin")
    if admin_user and admin_role:
        try:
            rbac.assign_role_to_user(admin_user["id"], admin_role["id"])
            print(f"✓ Assigned admin role to admin user")
        except ValueError as e:
            if "already has" in str(e):
                print(f"  Admin user already has admin role")
            else:
                print(f"✗ Error assigning role: {e}")
    
    print("\nRBAC initialization complete!")
    print("\nDefault roles created:")
    print("  - admin: Full access to everything")
    print("  - operator: Read/write access to users and settings")
    print("  - viewer: Read-only access")
    print("\nThe 'admin' user has been assigned the admin role.")


if __name__ == "__main__":
    init_rbac()
