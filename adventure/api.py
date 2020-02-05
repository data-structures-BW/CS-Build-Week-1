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

    rooms = {
        "1": [
    {
      "x": 1,
      "y": 1
    },
    {
      "n": 2
    },
    {
      "title": "Room 1"
    },
    {
      "description": "There are exits to the north "
    },
    {
      "items": []
    }
  ],
  "2": [
    {
      "x": 1,
      "y": 2
    },
    {
      "a": 1
    },
    {
      "title": "Room 2"
    },
    {
      "description": "There are exits to the north "
    },
    {
      "items": []
    }
  ],
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
