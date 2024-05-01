"""Tests for Deutscher Wetterdienst (DWD) Weather Warnings coordinator."""

from unittest.mock import MagicMock

from homeassistant.components.dwd_weather_warnings.const import CONF_REGION_IDENTIFIER
from homeassistant.core import HomeAssistant

from . import init_integration

from tests.common import MockConfigEntry


async def test_region_coordinator_update(
    hass: HomeAssistant,
    mock_identifier_entry: MockConfigEntry,
    mock_dwdwfsapi: MagicMock,
) -> None:
    """Test coordinator update using a region identifier based entry."""
    entry = await init_integration(hass, mock_identifier_entry)

    region_identifier = entry.data[CONF_REGION_IDENTIFIER]
    assert mock_dwdwfsapi.assert_called_once_with(region_identifier)

    assert mock_dwdwfsapi.update.call_count == 2
