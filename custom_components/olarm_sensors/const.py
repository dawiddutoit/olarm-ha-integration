"""Module that stores all the constants for the integration."""
import logging

from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.alarm_control_panel import AlarmControlPanelState

VERSION = "2.3.3"

# Rate limit configuration
MIN_SCAN_INTERVAL = 60  # Minimum seconds between update cycles (Olarm API rate limits aggressively)
API_MIN_REQUEST_GAP = 2.0  # Minimum seconds between individual API requests
API_BACKOFF_BASE = 60  # Base seconds to wait after a 429 response
API_BACKOFF_MAX = 300  # Maximum backoff in seconds (5 minutes)
API_MAX_CONSECUTIVE_429 = 3  # After this many consecutive 429s, stop retrying until next cycle

LOGGER = logging.getLogger(__package__)

DOMAIN = "olarm_sensors"
AUTHENTICATION_ERROR = "invalid_credentials"
CONF_DEVICE_FIRMWARE = "olarm_device_firmware"
CONF_ALARM_CODE = "olarm_arm_code"
CONF_OLARM_DEVICES = "selected_olarm_devices"
OLARM_DEVICE_NAMES = "olarm_device_names"
OLARM_DEVICES = "olarm_devices"
OLARM_DEVICE_AMOUNT = "olarm_device_amount"

# Backwards-compatible alias used by alarm_control_panel.py
STATE_ALARM_ARMING = AlarmControlPanelState.ARMING

OLARM_STATE_TO_HA = {
    "disarm": AlarmControlPanelState.DISARMED,
    "notready": AlarmControlPanelState.DISARMED,
    "countdown": AlarmControlPanelState.ARMING,
    "sleep": AlarmControlPanelState.ARMED_NIGHT,
    "stay": AlarmControlPanelState.ARMED_HOME,
    "arm": AlarmControlPanelState.ARMED_AWAY,
    "alarm": AlarmControlPanelState.TRIGGERED,
    "fire": AlarmControlPanelState.TRIGGERED,
    "emergency": AlarmControlPanelState.TRIGGERED,
}
OLARM_CHANGE_TO_HA = {
    "area-disarm": AlarmControlPanelState.DISARMED,
    "area-stay": AlarmControlPanelState.ARMED_HOME,
    "area-sleep": AlarmControlPanelState.ARMED_NIGHT,
    "area-arm": AlarmControlPanelState.ARMED_AWAY,
    None: None,
    "null": None,
}
OLARM_ZONE_TYPE_TO_HA = {
    "": BinarySensorDeviceClass.MOTION,
    0: BinarySensorDeviceClass.MOTION,
    10: BinarySensorDeviceClass.DOOR,
    11: BinarySensorDeviceClass.WINDOW,
    20: BinarySensorDeviceClass.MOTION,
    21: BinarySensorDeviceClass.MOTION,
    90: BinarySensorDeviceClass.PROBLEM,
    50: BinarySensorDeviceClass.SAFETY,
    51: BinarySensorDeviceClass.SAFETY,
    1000: BinarySensorDeviceClass.PLUG,
    1001: BinarySensorDeviceClass.POWER,
}

GITHUB_TOKEN = "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"


class TempEntry:
    """DOCSTRING: Representation of the area number."""

    scan_interval: int = 10
    api_key: str = ""

    def __init__(self, scan_interval: int, api_key: str) -> None:
        """Set up the representation of a config entry."""
        self.scan_interval = scan_interval
        self.api_key = api_key

    @property
    def data(self):
        """Returns the zone number for the api."""
        return {"scan_interval": self.scan_interval, "api_key": self.api_key}


class BypassZone:
    """DOCSTRING: Representation of the area number."""

    zone: int = 0

    def __init__(self, zone: int) -> None:
        """Representation of the area number."""
        self.zone = zone

    @property
    def data(self):
        """Returns the zone number for the api."""
        return {"zone_num": self.zone}
