#!/usr/bin/env python3
import soco

#device = soco.discovery.any_soco()
device = soco.discovery.by_name("<Playername>")

device.group.coordinator.partymode()

devices = soco.discover()
# Set (default) volume
for device in devices:
 device.volume = 12
