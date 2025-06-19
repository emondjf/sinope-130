from .const import (
    # ...existing code...
    DOMAIN as DOMAIN2,  # Use DOMAIN2 for clarity
    # ...existing code...
)

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN2: vol.Schema(
            # ...existing code...
        )
    },
    extra=vol.ALLOW_EXTRA,
)
