#!/usr/bin/env python3
# vim: set fileencoding=utf-8
import soco

# device = soco.discovery.any_soco()
device = soco.discovery.by_name("<Playername>")

playstatus = device.get_current_transport_info()['current_transport_state']

print (playstatus)
print (device.player_name)

if 1==2 and playstatus == "PLAYING":
 print ("music playing, so we leave the players alone")
else:
 print ("splitting group")
 for player in device.group:
  if (player.player_name == "Kid#1" or player.player_name == "Kid#2" or player.player_name == "Kid#3"):
   player.unjoin()
   player.volume = 6
