from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

#represent origin
all_rooms = [{"id": 0, "x": 0, "y": 0, "Title": "Origin", "n": 1, "s": 11, "e": 21, "w": 31,
              "description": "Here is the Origin, You may travel North, West, East or South."},
              #north
              {"id": 1, "x": 0, "y": 1, "Title": "Hallway N1", "n": 2, "s": 0, "e": -1, "w": -1,
              "description": ""},
              {"id": 2, "x": 0, "y": 2, "Title": "Hallway N2", "n": 3, "s": 1, "e": -1, "w": -1,
              "description": ""},
              {"id": 3, "x": 0, "y": 3, "Title": "Hallway N3", "n": 4, "s": 2, "e": -1, "w": -1,
              "description": ""},
              {"id": 4, "x": 0, "y": 4, "Title": "Hallway N4", "n": 5, "s": 3, "e": -1, "w": -1,
              "description": ""},
              {"id": 5, "x": 0, "y": 5, "Title": "Hallway N5", "n": 6, "s": 4, "e": 116, "w": -1,
              "description": ""},
              {"id": 6, "x": 0, "y": 6, "Title": "Hallway N6", "n": 7, "s": 5, "e": -1, "w": -1,
              "description": ""},
              {"id": 7, "x": 0, "y": 7, "Title": "Hallway N7", "n": 7, "s": 6, "e": -1, "w": -1,
              "description": ""},
              {"id": 8, "x": 0, "y": 8, "Title": "Hallway N8", "n": 8, "s": 7, "e": -1, "w": -1,
              "description": ""},
              {"id": 9, "x": 0, "y": 9, "Title": "Hallway N9", "n": 9, "s": 8, "e": -1, "w": -1,
              "description": ""},
              {"id": 10, "x": 0, "y": 10, "Title": "Hallway N10", "n": 41, "s": 9, "e": 117, "w": -1,
              "description": ""},
              #south
              {"id": 11, "x": 0, "y": -1, "Title": "Hallway S1", "n": 0, "s": 12, "e": -1, "w": -1,
              "description": ""},
              {"id": 12, "x": 0, "y": -2, "Title": "Hallway S2", "n": 11, "s": 13, "e": -1, "w": -1,
              "description": ""},
              {"id": 13, "x": 0, "y": -3, "Title": "Hallway S3", "n": 12, "s": 14, "e": -1, "w": -1,
              "description": ""},
              {"id": 14, "x": 0, "y": -4, "Title": "Hallway S4", "n": 13, "s": 15, "e": -1, "w": -1,
              "description": ""},
              {"id": 15, "x": 0, "y": -5, "Title": "Hallway S5", "n": 14, "s": 16, "e": -1, "w": -1,
              "description": ""},
              {"id": 16, "x": 0, "y": -6, "Title": "Hallway S6", "n": 15, "s": 17, "e": -1, "w": -1,
              "description": ""},
              {"id": 17, "x": 0, "y": -7, "Title": "Hallway S7", "n": 16, "s": 18, "e": -1, "w": -1,
              "description": ""},
              {"id": 18, "x": 0, "y": -8, "Title": "Hallway S8", "n": 17, "s": 19, "e": -1, "w": -1,
              "description": ""},
              {"id": 19, "x": 0, "y": -9, "Title": "Hallway S9", "n": 18, "s": 20, "e": -1, "w": -1,
              "description": ""},
              {"id": 20, "x": 0, "y": -10, "Title": "Hallway S10", "n": 19, "s": 56, "e": -1, "w": -1,
              "description": ""},
              #east
              {"id": 21, "x": -1, "y": 0, "Title": "Hallway E1", "n": -1, "s": -1, "e": 22, "w": 0,
              "description": ""},
              {"id": 22, "x": -2, "y": 0, "Title": "Hallway E2", "n": -1, "s": -1, "e": 23, "w": 22,
              "description": ""},
              {"id": 23, "x": -3, "y": 0, "Title": "Hallway E3", "n": -1, "s": -1, "e": 24, "w": 23,
              "description": ""},
              {"id": 24, "x": -4, "y": 0, "Title": "Hallway E4", "n": -1, "s": -1, "e": 25, "w": 24,
              "description": ""},
              {"id": 25, "x": -5, "y": 0, "Title": "Hallway E5", "n": -1, "s": -1, "e": 26, "w": 25,
              "description": ""},
              {"id": 26, "x": -6, "y": 0, "Title": "Hallway E6", "n": -1, "s": -1, "e": 27, "w": 26,
              "description": ""},
              {"id": 27, "x": -7, "y": 0, "Title": "Hallway E7", "n": -1, "s": -1, "e": 28, "w": 27,
              "description": ""},
              {"id": 28, "x": -8, "y": 0, "Title": "Hallway E8", "n": -1, "s": -1, "e": 29, "w": 28,
              "description": ""},
              {"id": 29, "x": -9, "y": 0, "Title": "Hallway E9", "n": -1, "s": -1, "e": 30, "w": 29,
              "description": ""},
              {"id": 30, "x": -10, "y": 0, "Title": "Hallway E10", "n": -1, "s": -1, "e": 31, "w": 71,
              "description": ""},
              #west
              {"id": 31, "x": 1, "y": 0, "Title": "Hallway W1", "n": -1, "s": -1, "e": 0, "w": 32,
              "description": ""},
              {"id": 32, "x": 2, "y": 0, "Title": "Hallway W2", "n": -1, "s": -1, "e": 31, "w": 33,
              "description": ""},
              {"id": 33, "x": 3, "y": 0, "Title": "Hallway W3", "n": -1, "s": -1, "e": 32, "w": 34,
              "description": ""},
              {"id": 34, "x": 4, "y": 0, "Title": "Hallway W4", "n": -1, "s": -1, "e": 33, "w": 35,
              "description": ""},
              {"id": 35, "x": 5, "y": 0, "Title": "Hallway W5", "n": -1, "s": -1, "e": 34, "w": 36,
              "description": ""},
              {"id": 36, "x": 6, "y": 0, "Title": "Hallway W6", "n": -1, "s": -1, "e": 35, "w": 37,
              "description": ""},
              {"id": 37, "x": 7, "y": 0, "Title": "Hallway W7", "n": -1, "s": -1, "e": 36, "w": 38,
              "description": ""},
              {"id": 38, "x": 8, "y": 0, "Title": "Hallway W8", "n": -1, "s": -1, "e": 37, "w": 39,
              "description": ""},
              {"id": 39, "x": 9, "y": 0, "Title": "Hallway W9", "n": -1, "s": -1, "e": 38, "w": 40,
              "description": ""},
              {"id": 40, "x": 10, "y": 0, "Title": "Hallway W10", "n": -1, "s": -1, "e": 39, "w": 86,
              "description": ""},
              #north origin
              {"id": 41, "x": 0, "y": 11, "Title": "Hallway N1", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 42, "x": 0, "y": 12, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 43, "x": 0, "y": 13, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 44, "x": 0, "y": 14, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 45, "x": 0, "y": 15, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 46, "x": 0, "y": 16, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 47, "x": 0, "y": 17, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 48, "x": 0, "y": 18, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 49, "x": 0, "y": 19, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 50, "x": 0, "y": 20, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 51, "x": 0, "y": 21, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 52, "x": 0, "y": 22, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 53, "x": 0, "y": 23, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 54, "x": 0, "y": 24, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 55, "x": 0, "y": 25, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              #south origin
              {"id": 56, "x": 0, "y": -11, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 57, "x": 0, "y": -12, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 58, "x": 0, "y": -13, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 59, "x": 0, "y": -14, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 60, "x": 0, "y": -15, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 61, "x": 0, "y": -16, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 62, "x": 0, "y": -17, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 63, "x": 0, "y": -18, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 64, "x": 0, "y": -19, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 65, "x": 0, "y": -20, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 66, "x": 0, "y": -21, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 67, "x": 0, "y": -22, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 68, "x": 0, "y": -23, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 69, "x": 0, "y": -24, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 70, "x": 0, "y": -25, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              #east origin
              {"id": 71, "x": -11, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 72, "x": -12, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 73, "x": -13, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 74, "x": -14, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 75, "x": -15, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 76, "x": -16, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 77, "x": -17, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 78, "x": -18, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 79, "x": -19, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 80, "x": -20, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 81, "x": -21, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 82, "x": -22, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 83, "x": -23, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 84, "x": -24, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 85, "x": -25, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              #west origin
              {"id": 86, "x": 11, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 87, "x": 12, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 88, "x": 13, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 89, "x": 14, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 90, "x": 15, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 91, "x": 16, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 92, "x": 17, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 93, "x": 18, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 94, "x": 19, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 95, "x": 20, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 96, "x": 21, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 97, "x": 22, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 98, "x": 23, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 99, "x": 24, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""},
              {"id": 100, "x": 25, "y": 0, "Title": "", "n": , "s": , "e": , "w": ,
              "description": ""}]

# r_outside = Room(title="Outside Cave Entrance",
#                description="North of you, the cave mount beckons")

# r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
# passages run north and east.""")

# r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm.""")

# r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
# to north. The smell of gold permeates the air.""")

# r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south.""")

# r_outside.save()
# r_foyer.save()
# r_overlook.save()
# r_narrow.save()
# r_treasure.save()

# # Link rooms together
# r_outside.connectRooms(r_foyer, "n")
# r_foyer.connectRooms(r_outside, "s")

# r_foyer.connectRooms(r_overlook, "n")
# r_overlook.connectRooms(r_foyer, "s")

# r_foyer.connectRooms(r_narrow, "e")
# r_narrow.connectRooms(r_foyer, "w")

# r_narrow.connectRooms(r_treasure, "n")
# r_treasure.connectRooms(r_narrow, "s")

players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()

