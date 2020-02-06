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
        "1": [{"x": 0,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "2": [{"x": 0,"y": 2},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "3": [{"x": 0,"y": 3},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "4": [{"x": 0, "y":4 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "5": [{"x": 0,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "6": [{"x": 0,"y": 2},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "7": [{"x": 0,"y": 3},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "8": [{"x": 0, "y": 4 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "9": [{"x": 0,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "10": [{"x": 1,"y": 2},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "11": [{"x": 1,"y": 3},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "12": [{"x": 1, "y": 4 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "13": [{"x": 1,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "14": [{"x": 1,"y": 2},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "15": [{"x": 1,"y": 3},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "16": [{"x": 1, "y": 4 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "17": [{"x": 97,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "18": [{"x": 34,"y": 2},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "19": [{"x": 76,"y": 3},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "20": [{"x": 34, "y": 4 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "21": [{"x": 1,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "22": [{"x": 1,"y": 98},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "23": [{"x": 1,"y": 45},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "24": [{"x": 1, "y": 34 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "25": [{"x": 1,"y": 56},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "26": [{"x": 0,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "27": [{"x": 0,"y": 2},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "28": [{"x": 0,"y": 3},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "29": [{"x": 0, "y":4 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "30": [{"x": 0,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "31": [{"x": 0,"y": 2},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "32": [{"x": 0,"y": 3},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "33": [{"x": 0, "y": 4 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "34": [{"x": 0,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "35": [{"x": 1,"y": 2},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "36": [{"x": 1,"y": 3},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "37": [{"x": 1, "y": 4 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "38": [{"x": 1,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "39": [{"x": 1,"y": 2},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "40": [{"x": 1,"y": 3},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "41": [{"x": 1, "y": 4 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "42": [{"x": 97,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "43": [{"x": 34,"y": 2},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "44": [{"x": 76,"y": 3},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "45": [{"x": 34, "y": 4 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "46": [{"x": 1,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "47": [{"x": 1,"y": 98},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "48": [{"x": 1,"y": 45},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "49": [{"x": 1, "y": 34 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "50": [{"x": 1,"y": 56},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "51: [{"x": 0,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "52": [{"x": 0,"y": 2},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "53": [{"x": 0,"y": 3},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "54": [{"x": 0, "y":4 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "55": [{"x": 0,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "56": [{"x": 0,"y": 2},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "57": [{"x": 0,"y": 3},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "58": [{"x": 0, "y": 4 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "59": [{"x": 0,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "60": [{"x": 1,"y": 2},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "61": [{"x": 1,"y": 3},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "62": [{"x": 1, "y": 4 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "63": [{"x": 1,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "64": [{"x": 1,"y": 2},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "65": [{"x": 1,"y": 3},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "66": [{"x": 1, "y": 4 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "67": [{"x": 97,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "68": [{"x": 34,"y": 2},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "69": [{"x": 76,"y": 3},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "70": [{"x": 34, "y": 4 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "71": [{"x": 1,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "72": [{"x": 1,"y": 98},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "73": [{"x": 1,"y": 45},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "74": [{"x": 1, "y": 34 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "75": [{"x": 1,"y": 56},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "76": [{"x": 0,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "77": [{"x": 0,"y": 2},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "78": [{"x": 0,"y": 3},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "79": [{"x": 0, "y":4 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "80": [{"x": 0,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "81": [{"x": 0,"y": 2},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "82": [{"x": 0,"y": 3},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "83": [{"x": 0, "y": 4 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "84": [{"x": 0,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "85": [{"x": 1,"y": 2},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "86": [{"x": 1,"y": 3},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "87": [{"x": 1, "y": 4 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "88": [{"x": 1,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "89": [{"x": 1,"y": 2},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "90": [{"x": 1,"y": 3},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "91": [{"x": 1, "y": 4 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "92": [{"x": 97,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "93": [{"x": 34,"y": 2},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "94": [{"x": 76,"y": 3},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "95": [{"x": 34, "y": 4 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "96": [{"x": 1,"y": 1},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],
        "97": [{"x": 1,"y": 98},{"a": 1},{"title": "Room 2"},{"description": "There are exits to the north "},{"items": []}],  
        "98": [{"x": 1,"y": 45},{"a": 1},{"title": "Room 3"},{"description": "There are exits to the north "},{"items": []}], 
        "99": [{"x": 1, "y": 34 }, {"a": 1},{"title": "Room 4"},{"description": "There are exits to the north "},{"items": []}],
        "100": [{"x": 1,"y": 56},{"n": 2},{"title": "Room 1"},{ "description": "There are exits to the north "},{"items": []}],

        
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
