#!/usr/bin/env python3
import soco

device = soco.discovery.by_name("Kid#1")
if device is not None:
  print("Setting timer on Kid#1")
  device.set_sleep_timer(3600)

device = soco.discovery.by_name("Kid#2")
if device is not None:
  print("Setting timer on Kid#2")
  device.set_sleep_timer(3600)
