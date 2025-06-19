"""Sinopé GT130 zigbee and wifi support (Instance 2)."""

from datetime import timedelta
import logging

from homeassistant import discovery
from homeassistant.const import (
    CONF_SCAN_INTERVAL,
    CONF_HOST,
    CONF_PORT,
    CONF_USERNAME,
    CONF_PASSWORD,
    CONF_TIMEOUT,
)
from homeassistant.helpers import discovery as helpers_discovery

from .const import (
    DOMAIN as DOMAIN2,  # Use DOMAIN2 for clarity
    CONF_HOMEKIT_MODE,
    CONF_IGNORE_MIWI,
    CONF_STAT_INTERVAL,
    CONF_NOTIFY,
    DEFAULT_HOMEKIT_MODE,
    DEFAULT_IGNORE_MIWI,
    DEFAULT_STAT_INTERVAL,
    DEFAULT_NOTIFY,
)

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(seconds=30)

def setup(hass, hass_config):
    """Set up neviweb130_2."""
    data = Neviweb130Data(hass, hass_config[DOMAIN2])
    hass.data[DOMAIN2] = data

    # Load platforms
    discovery.load_platform(hass, "climate", DOMAIN2, {}, hass_config)
    discovery.load_platform(hass, "light", DOMAIN2, {}, hass_config)
    discovery.load_platform(hass, "switch", DOMAIN2, {}, hass_config)
    discovery.load_platform(hass, "sensor", DOMAIN2, {}, hass_config)
    discovery.load_platform(hass, "valve", DOMAIN2, {}, hass_config)

    # Configuration options
    SCAN_INTERVAL = hass_config[DOMAIN2].get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL)
    HOMEKIT_MODE = hass_config[DOMAIN2].get(CONF_HOMEKIT_MODE, DEFAULT_HOMEKIT_MODE)
    IGNORE_MIWI = hass_config[DOMAIN2].get(CONF_IGNORE_MIWI, DEFAULT_IGNORE_MIWI)
    STAT_INTERVAL = hass_config[DOMAIN2].get(CONF_STAT_INTERVAL, DEFAULT_STAT_INTERVAL)
    NOTIFY = hass_config[DOMAIN2].get(CONF_NOTIFY, DEFAULT_NOTIFY)

    return True
