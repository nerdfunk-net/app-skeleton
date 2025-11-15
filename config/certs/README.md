# SSL/TLS Certificates Directory

This directory stores custom CA certificates for OIDC providers using self-signed certificates.

## Adding a CA Certificate

### Option 1: Export from Keycloak/Browser

1. **From Browser:**
   - Navigate to your Keycloak URL: `https://keycloak:7443`
   - Click the padlock icon in the address bar
   - View certificate → Details → Export
   - Save as `ca.cert.pem` (PEM format)

2. **From Keycloak Server:**
   ```bash
   # Copy from Keycloak container/server
   docker cp keycloak:/opt/keycloak/conf/server.crt.pem ./ca.cert.pem
   # OR
   kubectl cp keycloak-pod:/path/to/cert.pem ./ca.cert.pem
   ```

### Option 2: Extract from Server

```bash
# Get certificate from server
openssl s_client -connect keycloak:7443 -showcerts </dev/null 2>/dev/null | \
  openssl x509 -outform PEM > ca.cert.pem
```

### Option 3: Use System CA Bundle (macOS)

```bash
# If certificate is in system keychain
security find-certificate -a -p -c "Your Keycloak CA" > ca.cert.pem
```

## Converting Certificate Formats

If your certificate is not in PEM format:

```bash
# DER to PEM
openssl x509 -inform der -in certificate.cer -out ca.cert.pem

# PFX/P12 to PEM
openssl pkcs12 -in certificate.pfx -out ca.cert.pem -nodes

# CRT to PEM (usually just rename)
cp certificate.crt ca.cert.pem
```

## Verifying Certificate

```bash
# Check certificate details
openssl x509 -in ca.cert.pem -text -noout

# Test with curl
curl --cacert ca.cert.pem https://keycloak:7443/realms/cockpit/.well-known/openid-configuration
```

## Disabling Certificate Verification (NOT RECOMMENDED)

If you want to disable certificate verification entirely (development only):

1. Comment out `ca_cert_path` in `oidc_providers.yaml`
2. Modify `oidc_service.py` to use `verify=False` (security risk!)

**Note:** Never disable certificate verification in production!

## Files in this Directory

- `ca.cert.pem` - CA certificate for corporate Keycloak (Git ignored)
- `*.pem` - Other CA certificates (Git ignored)
- `README.md` - This file

All `.pem` and `.crt` files are automatically ignored by Git for security.
