# Configuration Directory

This directory contains YAML configuration files for the application template.

## Files

### `oidc_providers.yaml`
**OpenID Connect (OIDC) / Single Sign-On (SSO) Configuration**

⚠️ **OIDC is DISABLED by default** - requires external identity provider setup.

Configure multiple identity providers (Keycloak, Azure AD, Okta, etc.) for SSO authentication.

- **Example**: `oidc_providers.yaml.example` - Copy this file and customize it
- **Status**: OIDC is disabled by default; enable providers after setup

**Quick Setup:**
```bash
# 1. Set up an OIDC provider (Keycloak, Azure AD, Okta, Auth0, etc.)
# 2. Get your client_id, client_secret, and discovery_url from the provider
# 3. Edit the configuration file
vim oidc_providers.yaml

# 4. Enable at least one provider by setting enabled: true
# 5. Update discovery_url, client_id, client_secret, and redirect_uri
# 6. Restart the backend
cd ../backend
python start.py
```

## Security Notes

- **Never commit secrets**: Add `oidc_providers.yaml` to `.gitignore`
- **Use strong secrets**: Generate secure client secrets from your OIDC provider
- **HTTPS in production**: Always use HTTPS URLs for production deployments
- **Restrict permissions**: Ensure configuration files are readable only by the application user


## Getting Help

- **OIDC Setup**: See `OIDC_SETUP.md` in the project root
- **Example Configurations**: Check `*.example` files in this directory
- **Troubleshooting**: Enable DEBUG logging in backend and check logs
