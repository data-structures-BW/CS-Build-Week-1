from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
import json

# instantiate pusher
# pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))

@csrf_exempt
@api_view(["GET"])
def initialize(request):
    user = request.user
    player = user.player
    player_id = player.id
    uuid = player.uuid
    room = player.room()
    players = room.playerNames(player_id)
    return JsonResponse({'uuid': uuid, 'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players}, safe=True)


# @csrf_exempt
@api_view(["POST"])
def move(request):
    dirs={"n": "north", "s": "south", "e": "east", "w": "west"}
    reverse_dirs = {"n": "south", "s": "north", "e": "west", "w": "east"}
    player = request.user.player
    player_id = player.id
    player_uuid = player.uuid
    data = json.loads(request.body)
    direction = data['direction']
    room = player.room()
    nextRoomID = None
    if direction == "n":
        nextRoomID = room.n_to
    elif direction == "s":
        nextRoomID = room.s_to
    elif direction == "e":
        nextRoomID = room.e_to
    elif direction == "w":
        nextRoomID = room.w_to
    if nextRoomID is not None and nextRoomID > 0:
        nextRoom = Room.objects.get(id=nextRoomID)
        player.currentRoom=nextRoomID
        player.save()
        players = nextRoom.playerNames(player_id)
        currentPlayerUUIDs = room.playerUUIDs(player_id)
        nextPlayerUUIDs = nextRoom.playerUUIDs(player_id)
        # for p_uuid in currentPlayerUUIDs:
        #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has walked {dirs[direction]}.'})
        # for p_uuid in nextPlayerUUIDs:
        #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has entered from the {reverse_dirs[direction]}.'})
        return JsonResponse({'name':player.user.username, 'title':nextRoom.title, 'description':nextRoom.description, 'players':players, 'error_msg':""}, safe=True)
    else:
        players = room.playerNames(player_id)
        return JsonResponse({'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players, 'error_msg':"You cannot move that way."}, safe=True)


@csrf_exempt
@api_view(["POST"])
def say(request):
    # IMPLEMENT
    return JsonResponse({'error':"Not yet implemented"}, safe=True, status=500)

@csrf_exempt
@api_view(["GET"])
def getallrooms(request):
    print(request.body)
    get_rooms = Room.objects.all()

    rooms = [{"id": 0, "x": 0, "y": 0, "Title": "Origin", "n": 1, "s": 11, "e": 21, "w": 31,
              "description": "Here is the Origin, You may travel North, West, East or South."},
              #north
              {"id": 1, "x": 0, "y": 1, "Title": "Hallway N1", "n": 2, "s": 0, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 2, "x": 0, "y": 2, "Title": "Hallway N2", "n": 3, "s": 1, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 3, "x": 0, "y": 3, "Title": "Hallway N3", "n": 4, "s": 2, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 4, "x": 0, "y": 4, "Title": "Hallway N4", "n": 5, "s": 3, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 5, "x": 0, "y": 5, "Title": "Hallway N5", "n": 6, "s": 4, "e": 116, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 6, "x": 0, "y": 6, "Title": "Hallway N6", "n": 7, "s": 5, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 7, "x": 0, "y": 7, "Title": "Hallway N7", "n": 7, "s": 6, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 8, "x": 0, "y": 8, "Title": "Hallway N8", "n": 8, "s": 7, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 9, "x": 0, "y": 9, "Title": "Hallway N9", "n": 9, "s": 8, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 10, "x": 0, "y": 10, "Title": "Hallway N10", "n": 41, "s": 9, "e": 117, "w": -1,
              "description": "This is a room! What will you find in here?"},
              #south
              {"id": 11, "x": 0, "y": -1, "Title": "Hallway S1", "n": 0, "s": 12, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 12, "x": 0, "y": -2, "Title": "Hallway S2", "n": 11, "s": 13, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 13, "x": 0, "y": -3, "Title": "Hallway S3", "n": 12, "s": 14, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 14, "x": 0, "y": -4, "Title": "Hallway S4", "n": 13, "s": 15, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 15, "x": 0, "y": -5, "Title": "Hallway S5", "n": 14, "s": 16, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 16, "x": 0, "y": -6, "Title": "Hallway S6", "n": 15, "s": 17, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 17, "x": 0, "y": -7, "Title": "Hallway S7", "n": 16, "s": 18, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 18, "x": 0, "y": -8, "Title": "Hallway S8", "n": 17, "s": 19, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 19, "x": 0, "y": -9, "Title": "Hallway S9", "n": 18, "s": 20, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 20, "x": 0, "y": -10, "Title": "Hallway S10", "n": 19, "s": 56, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              #east
              {"id": 21, "x": -1, "y": 0, "Title": "Hallway E1", "n": -1, "s": -1, "e": 22, "w": 0,
              "description": "This is a room! What will you find in here?"},
              {"id": 22, "x": -2, "y": 0, "Title": "Hallway E2", "n": -1, "s": -1, "e": 23, "w": 22,
              "description": "This is a room! What will you find in here?"},
              {"id": 23, "x": -3, "y": 0, "Title": "Hallway E3", "n": -1, "s": -1, "e": 24, "w": 23,
              "description": "This is a room! What will you find in here?"},
              {"id": 24, "x": -4, "y": 0, "Title": "Hallway E4", "n": -1, "s": -1, "e": 25, "w": 24,
              "description": "This is a room! What will you find in here?"},
              {"id": 25, "x": -5, "y": 0, "Title": "Hallway E5", "n": -1, "s": -1, "e": 26, "w": 25,
              "description": "This is a room! What will you find in here?"},
              {"id": 26, "x": -6, "y": 0, "Title": "Hallway E6", "n": -1, "s": -1, "e": 27, "w": 26,
              "description": "This is a room! What will you find in here?"},
              {"id": 27, "x": -7, "y": 0, "Title": "Hallway E7", "n": -1, "s": -1, "e": 28, "w": 27,
              "description": "This is a room! What will you find in here?"},
              {"id": 28, "x": -8, "y": 0, "Title": "Hallway E8", "n": -1, "s": -1, "e": 29, "w": 28,
              "description": "This is a room! What will you find in here?"},
              {"id": 29, "x": -9, "y": 0, "Title": "Hallway E9", "n": -1, "s": -1, "e": 30, "w": 29,
              "description": "This is a room! What will you find in here?"},
              {"id": 30, "x": -10, "y": 0, "Title": "Hallway E10", "n": -1, "s": -1, "e": 31, "w": 71,
              "description": "This is a room! What will you find in here?"},
              #west
              {"id": 31, "x": 1, "y": 0, "Title": "Hallway W1", "n": -1, "s": -1, "e": 0, "w": 32,
              "description": "This is a room! What will you find in here?"},
              {"id": 32, "x": 2, "y": 0, "Title": "Hallway W2", "n": -1, "s": -1, "e": 31, "w": 33,
              "description": "This is a room! What will you find in here?"},
              {"id": 33, "x": 3, "y": 0, "Title": "Hallway W3", "n": -1, "s": -1, "e": 32, "w": 34,
              "description": "This is a room! What will you find in here?"},
              {"id": 34, "x": 4, "y": 0, "Title": "Hallway W4", "n": -1, "s": -1, "e": 33, "w": 35,
              "description": "This is a room! What will you find in here?"},
              {"id": 35, "x": 5, "y": 0, "Title": "Hallway W5", "n": -1, "s": -1, "e": 34, "w": 36,
              "description": "This is a room! What will you find in here?"},
              {"id": 36, "x": 6, "y": 0, "Title": "Hallway W6", "n": -1, "s": -1, "e": 35, "w": 37,
              "description": "This is a room! What will you find in here?"},
              {"id": 37, "x": 7, "y": 0, "Title": "Hallway W7", "n": -1, "s": -1, "e": 36, "w": 38,
              "description": "This is a room! What will you find in here?"},
              {"id": 38, "x": 8, "y": 0, "Title": "Hallway W8", "n": -1, "s": -1, "e": 37, "w": 39,
              "description": "This is a room! What will you find in here?"},
              {"id": 39, "x": 9, "y": 0, "Title": "Hallway W9", "n": -1, "s": -1, "e": 38, "w": 40,
              "description": "This is a room! What will you find in here?"},
              {"id": 40, "x": 10, "y": 0, "Title": "Hallway W10", "n": -1, "s": -1, "e": 39, "w": 86,
              "description": "This is a room! What will you find in here?"},
              #north origin
              {"id": 41, "x": 0, "y": 11, "Title": "Hallway N11", "n": 42, "s": 10, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 42, "x": 0, "y": 12, "Title": "Hallway N12", "n": 43, "s": 41, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 43, "x": 0, "y": 13, "Title": "Hallway N13", "n": 44, "s": 42, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 44, "x": 0, "y": 14, "Title": "Hallway N14", "n": 45, "s": 43, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 45, "x": 0, "y": 15, "Title": "Hallway N15", "n": 46, "s": 44, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 46, "x": 0, "y": 16, "Title": "Hallway N16", "n": 47, "s": 45, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 47, "x": 0, "y": 17, "Title": "Hallway N17", "n": 48, "s": 46, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 48, "x": 0, "y": 18, "Title": "Hallway N18", "n": 49, "s": 47, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 49, "x": 0, "y": 19, "Title": "Hallway N19", "n": 50, "s": 48, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 50, "x": 0, "y": 20, "Title": "Hallway N20", "n": 51, "s": 49, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 51, "x": 0, "y": 21, "Title": "Hallway N21", "n": 52, "s": 50, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 52, "x": 0, "y": 22, "Title": "Hallway N22", "n": 53, "s": 51, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 53, "x": 0, "y": 23, "Title": "Hallway N23", "n": 54, "s": 52, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 54, "x": 0, "y": 24, "Title": "Hallway N24", "n": 55, "s": 53, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 55, "x": 0, "y": 25, "Title": "Hallway N25", "n": -1, "s": 54, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              #south origin
              {"id": 56, "x": 0, "y": -11, "Title": "Merchant 10", "n": 20, "s": 57, "e": -1, "w": 86,
              "description": "This is a room! What will you find in here?"},
              {"id": 57, "x": 0, "y": -12, "Title": "Merchant 9", "n": 56, "s": 58, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 58, "x": 0, "y": -13, "Title": "Merchant 8", "n": 57, "s": 59, "e": -1, "w": 88,
              "description": "This is a room! What will you find in here?"},
              {"id": 59, "x": 0, "y": -14, "Title": "Merchant 7", "n": 58, "s": 60, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 60, "x": 0, "y": -15, "Title": "Merchant 6", "n": 59, "s": 61, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 61, "x": 0, "y": -16, "Title": "Merchant 5", "n": 60, "s": 62, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 62, "x": 0, "y": -17, "Title": "Merchant 4", "n": 61, "s": 63, "e": -1, "w": 92,
              "description": "This is a room! What will you find in here?"},
              {"id": 63, "x": 0, "y": -18, "Title": "Merchant 4", "n": 62, "s": 64, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 64, "x": 0, "y": -19, "Title": "Merchant 4", "n": 63, "s": 65, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 65, "x": 0, "y": -20, "Title": "Merchant 3", "n": 64, "s": 66, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 66, "x": 0, "y": -21, "Title": "Merchant 3", "n": 65, "s": 67, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 67, "x": 0, "y": -22, "Title": "Merchant 3", "n": 66, "s": 68, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 68, "x": 0, "y": -23, "Title": "Merchant 2", "n": 67, "s": 69, "e": -1, "w": 98,
              "description": "This is a room! What will you find in here?"},
              {"id": 69, "x": 0, "y": -24, "Title": "Merchant 2", "n": 68, "s": 70, "e": -1, "w": -1,
              "description": "This is a room! What will you find in here?"},
              {"id": 70, "x": 3, "y": -25, "Title": "Merchant 1", "n": 2 , "s": 32, "e": 23, "w": 12,
              "description": "This is a room! What will you find in here?"},
              #east origin
              {"id": 71, "x": -11, "y": 21, "Title": "Merchant 2", "n":64 , "s":64 , "e":56 , "w": 54,
              "description": "This is a room! What will you find in here?"},
              {"id": 72, "x": -12, "y": 12, "Title": "Merchant 3", "n":12 , "s":2 , "e": 4, "w": 42 ,
              "description": "This is a room! What will you find in here?"},
              {"id": 73, "x": -13, "y": 87, "Title": "Merchant 4", "n": 42, "s": 45, "e": 64, "w": 2,
              "description": "This is a room! What will you find in here?"},
              {"id": 74, "x": -14, "y": -1, "Title": "Merchant 5", "n": 5 ,"s":4 , "e":4 , "w":3 ,
              "description": "This is a room! What will you find in here?"},
              {"id": 75, "x": -15, "y": 57, "Title": "Merchant 6", "n": 65, "s": 23, "e":12 , "w": 32,
              "description": "This is a room! What will you find in here?"},
              {"id": 76, "x": -16, "y": 32, "Title": "Merchant 7", "n": 12, "s": 54, "e": 23, "w":12 ,
              "description": "This is a room! What will you find in here?"},
              {"id": 77, "x": -17, "y": 12, "Title": "Merchant 8", "n":53 , "s": 12, "e":32 , "w":34 ,
              "description": "This is a room! What will you find in here?"},
              {"id": 78, "x": -18, "y": 75, "Title": "Merchant 9", "n": 12, "s": 23, "e": 43, "w": 23,
              "description": "This is a room! What will you find in here?"},
              {"id": 79, "x": -19, "y": 23, "Title": "Entrance 1", "n": 34, "s":4 , "e":3 , "w": 1,
              "description": "This is a room! What will you find in here?"},
              {"id": 80, "x": -20, "y": 76, "Title": "Entrance 2", "n":12 , "s":2 , "e": -5, "w":12 ,
              "description": "This is a room! What will you find in here?"},
              {"id": 81, "x": -21, "y": 12, "Title": "Entrance 3", "n": 32, "s":56 , "e": 2, "w":8 ,
              "description": "This is a room! What will you find in here?"},
              {"id": 82, "x": -22, "y": 3, "Title": "Entrance 4", "n":-5 , "s": -6, "e": -7, "w": 2,
              "description": "This is a room! What will you find in here?"},
              {"id": 83, "x": -23, "y": -13, "Title": "Entrance 5", "n": 12, "s": 32, "e":12 , "w":12 ,
              "description": "This is a room! What will you find in here?"},
              {"id": 84, "x": -24, "y": -10, "Title": "Armory 1", "n":43 , "s":23 , "e": 23, "w": 32,
              "description": "This is a room! What will you find in here?"},
              {"id": 85, "x": -25, "y": 98, "Title": "Armory 2", "n": 76, "s": 34, "e": 21, "w": 34,
              "description": "This is a room! What will you find in here?"},
              #west origin
              {"id": 86, "x": 11, "y": 45, "Title": "Armory 3", "n": 12, "s":32 , "e":12 , "w":23 ,
              "description": "This is a room! What will you find in here?"},
              {"id": 87, "x": 12, "y": 23, "Title": "Armory 4", "n":4 , "s": 12, "e": 23, "w": 34,
              "description": "This is a room! What will you find in here?"},
              {"id": 88, "x": 13, "y": 3, "Title": "Cave of Storms 1", "n": 34, "s": 12, "e": 23, "w":3 ,
              "description": "This is a room! What will you find in here?"},
              {"id": 89, "x": 14, "y": 4, "Title": "Cave of Storms 2", "n": 12, "s": 65, "e":23 , "w": 12,
              "description": "This is a room! What will you find in here?"},
              {"id": 90, "x": 15, "y": 13, "Title": "Cave of Storms 3", "n": 12, "s":23 , "e":12 , "w": 32,
              "description": "This is a room! What will you find in here?"},
              {"id": 91, "x": 16, "y": 86, "Title": "Cave of Storms 4", "n":22 , "s":34 , "e":42 , "w": 23,
              "description": "This is a room! What will you find in here?"},
              {"id": 92, "x": 17, "y": 23, "Title": "Cave of Storms 5", "n":4 , "s": 2, "e": 3, "w": 42,
              "description": "This is a room! What will you find in here?"},
              {"id": 93, "x": 18, "y": 23, "Title": "Dining Room 1", "n": 54, "s": 34, "e": 23, "w": 12,
              "description": "This is a room! What will you find in here?"},
              {"id": 94, "x": 19, "y": 56, "Title": "Dining room 2", "n": 65, "s": 63, "e": 87, "w": 12,
              "description": "This is a room! What will you find in here?"},
              {"id": 95, "x": 20, "y": 34, "Title": "Dining Room 3", "n": 10 , "s": 21, "e":3 , "w": 2,
              "description": "This is a room! What will you find in here?"},
              {"id": 96, "x": 21, "y": 86, "Title": "Dining Room 4", "n": 14, "s": , 32"e": 45, "w": 64,
              "description": "This is a room! What will you find in here?"},
              {"id": 97, "x": 22, "y": 12, "Title": "Bedroom 1", "n": 34, "s": 54 , "e": 45, "w": 65,
              "description": "This is a room! What will you find in here?"},
              {"id": 98, "x": 23, "y": 43, "Title": "Bedroom 2", "n": 12 , "s":43 , "e": 12, "w":11 ,
              "description": "This is a room! What will you find in here?"},
              {"id": 99, "x": 24, "y": 2, "Title": "Bedroom 3", "n":23 , "s": 31, "e":23 , "w": 1,
              "description": "This is a room! What will you find in here?"},
              {"id": 100, "x": 25, "y": 59, "Title": "Bedroom 4", "n":23 , "s":11 , "e":43 , "w": 21,
              "description": "This is a room! What will you find in here?"}],
    }

    for room in get_rooms.values():
        id = str(room['id'])
        coordinates = {"x": room['x'], "y": room['y']}
        title = {"title": room['title']}
        description = {"description": room['description']}
        connections = {'n': room['n_to'], 'e': room['e_to'], 'w': room['w_to'], 's': room['s_to']}
        connections = { k: v for k, v in connections.items() if v != 0}
        
        modified_room = [coordinates, connections, title, description, {"items": []}]
        rooms[id] = modified_room
        
    return JsonResponse({"rooms": rooms}, safe=True, status=200)

@csrf_exempt
@api_view(["GET"])
def getroom(request):
    print(request.body)
    room = Room.objects.get(id=json.loads(request.body)['id'])
    return JsonResponse({'id': room.id, 'n_to': room.n_to,'s_to': room.s_to, 'e_to': room.e_to, 'w_to': room.w_to, 'x': room.x, 'y': room.y}, safe=True,status=200)
