"""
OIDC configuration loader - simple YAML-based config reader.
Matches the simple pattern used in config.py.
"""

from pathlib import Path
from typing import Dict, Any, Optional, List
import yaml

# Cache the loaded config to avoid repeated file reads
_config_cache: Optional[Dict[str, Any]] = None


def _load_oidc_config() -> Dict[str, Any]:
    """Load OIDC config from YAML file."""
    global _config_cache
    
    if _config_cache is not None:
        return _config_cache
    
    config_path = Path(__file__).parent.parent / "config" / "oidc_providers.yaml"
    
    if not config_path.exists():
        _config_cache = {}
        return _config_cache
    
    try:
        with open(config_path, 'r') as f:
            _config_cache = yaml.safe_load(f) or {}
        return _config_cache
    except Exception as e:
        print(f"Error loading OIDC config: {e}")
        _config_cache = {}
        return _config_cache


def reload_config():
    """Force reload of OIDC configuration from file."""
    global _config_cache
    _config_cache = None
    return _load_oidc_config()


def get_oidc_providers() -> Dict[str, Dict[str, Any]]:
    """Get all OIDC providers from configuration."""
    config = _load_oidc_config()
    return config.get('providers', {})


def get_oidc_provider(provider_id: str) -> Optional[Dict[str, Any]]:
    """Get specific OIDC provider configuration by ID."""
    providers = get_oidc_providers()
    provider = providers.get(provider_id)
    
    if provider:
        # Add provider_id to the config for convenience
        provider['provider_id'] = provider_id
    
    return provider


def get_enabled_oidc_providers() -> List[Dict[str, Any]]:
    """Get list of enabled OIDC providers."""
    providers = get_oidc_providers()
    enabled = []
    
    for provider_id, provider_config in providers.items():
        if provider_config.get('enabled', False):
            # Add provider_id to each config
            provider_config['provider_id'] = provider_id
            enabled.append(provider_config)
    
    # Sort by display_order
    enabled.sort(key=lambda p: p.get('display_order', 999))
    return enabled


def is_oidc_enabled() -> bool:
    """Check if any OIDC provider is enabled."""
    providers = get_oidc_providers()
    return any(p.get('enabled', False) for p in providers.values())


def get_oidc_global_settings() -> Dict[str, Any]:
    """Get global OIDC settings."""
    config = _load_oidc_config()
    return config.get('global_settings', {
        'allow_traditional_login': True  # Default to allowing traditional login
    })
