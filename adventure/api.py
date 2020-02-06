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
        {
  "494": [
    {
      "x": 1,
      "y": 8
    },
    {
      "e": 457
    },
    {
      "title": "Room 494"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "492": [
    {
      "x": 1,
      "y": 20
    },
    {
      "e": 400
    },
    {
      "title": "Room 492"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "493": [
    {
      "x": 2,
      "y": 5
    },
    {
      "e": 478
    },
    {
      "title": "Room 493"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "457": [
    {
      "x": 2,
      "y": 8
    },
    {
      "e": 355,
      "w": 494
    },
    {
      "title": "Room 457"
    },
    {
      "description": "There are exits to the east west "
    },
  ],
  "484": [
    {
      "x": 2,
      "y": 9
    },
    {
      "n": 482
    },
    {
      "title": "Room 484"
    },
    {
      "description": "There are exits to the north "
    },
  ],
  "482": [
    {
      "x": 2,
      "y": 10
    },
    {
      "s": 484,
      "e": 404
    },
    {
      "title": "Room 482"
    },
    {
      "description": "There are exits to the south east "
    },
  ],
  "486": [
    {
      "x": 2,
      "y": 13
    },
    {
      "e": 462
    },
    {
      "title": "Room 486"
    },
    {
      "description": "There are exits to the east "
    },

  ],
  "479": [
    {
      "x": 2,
      "y": 15
    },
    {
      "e": 418
    },
    {
      "title": "Room 479"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "465": [
    {
      "x": 2,
      "y": 16
    },
    {
      "e": 368
    },
    {
      "title": "Room 465"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "414": [
    {
      "x": 2,
      "y": 19
    },
    {
      "e": 365
    },
    {
      "title": "Room 414"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "400": [
    {
      "x": 2,
      "y": 20
    },
    {
      "e": 399,
      "w": 492
    },
    {
      "title": "Room 400"
    },
    {
      "description": "There are exits to the east west "
    },
  ],
  "451": [
    {
      "x": 2,
      "y": 21
    },
    {
      "e": 429
    },
    {
      "title": "Room 451"
    },
    {
      "description": "There are exits to the east "
    },

  ],
  "452": [
    {
      "x": 2,
      "y": 22
    },
    {
      "e": 428
    },
    {
      "title": "Room 452"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "478": [
    {
      "x": 3,
      "y": 5
    },
    {
      "e": 413,
      "w": 493
    },
    {
      "title": "Room 478"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "393": [
    {
      "x": 3,
      "y": 6
    },
    {
      "e": 375
    },
    {
      "title": "Room 393"
    },
    {
      "description": "There are exits to the east "
    },

  ],
  "437": [
    {
      "x": 3,
      "y": 7
    },
    {
      "e": 347
    },
    {
      "title": "Room 437"
    },
    {
      "description": "There are exits to the east "
    },

  ],
  "355": [
    {
      "x": 3,
      "y": 8
    },
    {
      "e": 312,
      "w": 457
    },
    {
      "title": "Room 355"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "433": [
    {
      "x": 3,
      "y": 9
    },
    {
      "e": 372
    },
    {
      "title": "Room 433"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "404": [
    {
      "x": 3,
      "y": 10
    },
    {
      "n": 339,
      "w": 482
    },
    {
      "title": "Room 404"
    },
    {
      "description": "There are exits to the north west "
    },
  ],
  "339": [
    {
      "x": 3,
      "y": 11
    },
    {
      "s": 404,
      "e": 314
    },
    {
      "title": "Room 339"
    },
    {
      "description": "There are exits to the south east "
    },

  ],
  "367": [
    {
      "x": 3,
      "y": 12
    },
    {
      "n": 462,
      "e": 344
    },
    {
      "title": "Room 367"
    },
    {
      "description": "There are exits to the north east "
    },
  ],
  "462": [
    {
      "x": 3,
      "y": 13
    },
    {
      "s": 367,
      "w": 486
    },
    {
      "title": "Room 462"
    },
    {
      "description": "There are exits to the south west "
    },
  ],
  "463": [
    {
      "x": 3,
      "y": 14
    },
    {
      "e": 458,
      "n": 418
    },
    {
      "title": "Room 463"
    },
    {
      "description": "There are exits to the north east "
    },
  ],
  "418": [
    {
      "x": 3,
      "y": 15
    },
    {
      "e": 349,
      "w": 479,
      "s": 463
    },
    {
      "title": "Room 418"
    },
    {
      "description": "There are exits to the south east west "
    },
  ],
  "368": [
    {
      "x": 3,
      "y": 16
    },
    {
      "n": 436,
      "e": 284,
      "w": 465
    },
    {
      "title": "Room 368"
    },
    {
      "description": "There are exits to the north east west "
    },

  ],
  "436": [
    {
      "x": 3,
      "y": 17
    },
    {
      "s": 368
    },
    {
      "title": "Room 436"
    },
    {
      "description": "There are exits to the south "
    },
  ],
  "447": [
    {
      "x": 3,
      "y": 18
    },
    {
      "n": 365
    },
    {
      "title": "Room 447"
    },
    {
      "description": "There are exits to the north "
    },
  ],
  "365": [
    {
      "x": 3,
      "y": 19
    },
    {
      "s": 447,
      "e": 333,
      "w": 414
    },
    {
      "title": "Room 365"
    },
    {
      "description": "There are exits to the south east west "
    },
  ],
  "399": [
    {
      "x": 3,
      "y": 20
    },
    {
      "e": 358,
      "w": 400
    },
    {
      "title": "Room 399"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "429": [
    {
      "x": 3,
      "y": 21
    },
    {
      "n": 428,
      "w": 451
    },
    {
      "title": "Room 429"
    },
    {
      "description": "There are exits to the north west "
    },
  ],
  "428": [
    {
      "x": 3,
      "y": 22
    },
    {
      "s": 429,
      "e": 411,
      "w": 452
    },
    {
      "title": "Room 428"
    },
    {
      "description": "There are exits to the south east west "
    },

  ],
  "419": [
    {
      "x": 4,
      "y": 4
    },
    {
      "n": 413
    },
    {
      "title": "Room 419"
    },
    {
      "description": "There are exits to the north "
    },
  ],
  "413": [
    {
      "x": 4,
      "y": 5
    },
    {
      "n": 375,
      "s": 419,
      "w": 478
    },
    {
      "title": "Room 413"
    },
    {
      "description": "There are exits to the north south west "
    },
  ],
  "375": [
    {
      "x": 4,
      "y": 6
    },
    {
      "n": 347,
      "s": 413,
      "w": 393
    },
    {
      "title": "Room 375"
    },
    {
      "description": "There are exits to the north south west "
    },
  ],
  "347": [
    {
      "x": 4,
      "y": 7
    },
    {
      "n": 312,
      "s": 375,
      "w": 437
    },
    {
      "title": "Room 347"
    },
    {
      "description": "There are exits to the north south west "
    },

  ],
  "312": [
    {
      "x": 4,
      "y": 8
    },
    {
      "s": 347,
      "e": 299,
      "w": 355
    },
    {
      "title": "Room 312"
    },
    {
      "description": "There are exits to the south east west "
    },

  ],
  "372": [
    {
      "x": 4,
      "y": 9
    },
    {
      "e": 263,
      "w": 433
    },
    {
      "title": "Room 372"
    },
    {
      "description": "There are exits to the east west "
    },
  ],
  "258": [
    {
      "x": 4,
      "y": 10
    },
    {
      "e": 236
    },
    {
      "title": "Room 258"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "314": [
    {
      "x": 4,
      "y": 11
    },
    {
      "e": 220,
      "w": 339
    },
    {
      "title": "Room 314"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "344": [
    {
      "x": 4,
      "y": 12
    },
    {
      "n": 359,
      "e": 230,
      "w": 367
    },
    {
      "title": "Room 344"
    },
    {
      "description": "There are exits to the north east west "
    },
  ],
  "359": [
    {
      "x": 4,
      "y": 13
    },
    {
      "n": 458,
      "s": 344
    },
    {
      "title": "Room 359"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "458": [
    {
      "x": 4,
      "y": 14
    },
    {
      "s": 359,
      "w": 463
    },
    {
      "title": "Room 458"
    },
    {
      "description": "There are exits to the south west "
    },

  ],
  "349": [
    {
      "x": 4,
      "y": 15
    },
    {
      "n": 284,
      "w": 418
    },
    {
      "title": "Room 349"
    },
    {
      "description": "There are exits to the north west "
    },

  ],
  "284": [
    {
      "x": 4,
      "y": 16
    },
    {
      "n": 470,
      "s": 349,
      "e": 254,
      "w": 368
    },
    {
      "title": "Room 284"
    },
    {
      "description": "There are exits to the north south east west "
    },
  ],
  "470": [
    {
      "x": 4,
      "y": 17
    },
    {
      "s": 284
    },
    {
      "title": "Room 470"
    },
    {
      "description": "There are exits to the south "
    },
  ],
  "301": [
    {
      "x": 4,
      "y": 18
    },
    {
      "e": 187
    },
    {
      "title": "Room 301"
    },
    {
      "description": "There are exits to the east "
    },

  ],
  "333": [
    {
      "x": 4,
      "y": 19
    },
    {
      "n": 358,
      "e": 303,
      "w": 365
    },
    {
      "title": "Room 333"
    },
    {
      "description": "There are exits to the north east west "
    },
  ],
  "358": [
    {
      "x": 4,
      "y": 20
    },
    {
      "n": 397,
      "s": 333,
      "w": 399
    },
    {
      "title": "Room 358"
    },
    {
      "description": "There are exits to the north south west "
    },
  ],
  "397": [
    {
      "x": 4,
      "y": 21
    },
    {
      "s": 358
    },
    {
      "title": "Room 397"
    },
    {
      "description": "There are exits to the south "
    },
  ],
  "411": [
    {
      "x": 4,
      "y": 22
    },
    {
      "e": 324,
      "w": 428
    },
    {
      "title": "Room 411"
    },
    {
      "description": "There are exits to the east west "
    },
  ],
  "396": [
    {
      "x": 4,
      "y": 23
    },
    {
      "e": 391
    },
    {
      "title": "Room 396"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "449": [
    {
      "x": 5,
      "y": 4
    },
    {
      "n": 432,
      "e": 450
    },
    {
      "title": "Room 449"
    },
    {
      "description": "There are exits to the north east "
    },
  ],
  "432": [
    {
      "x": 5,
      "y": 5
    },
    {
      "n": 405,
      "s": 449,
      "e": 473
    },
    {
      "title": "Room 432"
    },
    {
      "description": "There are exits to the north south east "
    },

  ],
  "405": [
    {
      "x": 5,
      "y": 6
    },
    {
      "n": 356,
      "s": 432
    },
    {
      "title": "Room 405"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "356": [
    {
      "x": 5,
      "y": 7
    },
    {
      "n": 299,
      "s": 405
    },
    {
      "title": "Room 356"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "299": [
    {
      "x": 5,
      "y": 8
    },
    {
      "n": 263,
      "s": 356,
      "w": 312
    },
    {
      "title": "Room 299"
    },
    {
      "description": "There are exits to the north south west "
    },
  ],
  "263": [
    {
      "x": 5,
      "y": 9
    },
    {
      "n": 236,
      "s": 299,
      "w": 372
    },
    {
      "title": "Room 263"
    },
    {
      "description": "There are exits to the north south west "
    },
  ],
  "236": [
    {
      "x": 5,
      "y": 10
    },
    {
      "s": 263,
      "e": 216,
      "w": 258
    },
    {
      "title": "Room 236"
    },
    {
      "description": "There are exits to the south east west "
    },

  ],
  "220": [
    {
      "x": 5,
      "y": 11
    },
    {
      "n": 230,
      "e": 215,
      "w": 314
    },
    {
      "title": "Room 220"
    },
    {
      "description": "There are exits to the north east west "
    },

  ],
  "230": [
    {
      "x": 5,
      "y": 12
    },
    {
      "s": 220,
      "w": 344
    },
    {
      "title": "Room 230"
    },
    {
      "description": "There are exits to the south west "
    },

  ],
  "266": [
    {
      "x": 5,
      "y": 13
    },
    {
      "n": 379,
      "e": 260
    },
    {
      "title": "Room 266"
    },
    {
      "description": "There are exits to the north east "
    },
  ],
  "379": [
    {
      "x": 5,
      "y": 14
    },
    {
      "s": 266
    },
    {
      "title": "Room 379"
    },
    {
      "description": "There are exits to the south "
    },
  ],
  "274": [
    {
      "x": 5,
      "y": 15
    },
    {
      "e": 222
    },
    {
      "title": "Room 274"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "254": [
    {
      "x": 5,
      "y": 16
    },
    {
      "e": 205,
      "w": 284
    },
    {
      "title": "Room 254"
    },
    {
      "description": "There are exits to the east west "
    },
  ],
  "227": [
    {
      "x": 5,
      "y": 17
    },
    {
      "e": 194
    },
    {
      "title": "Room 227"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "187": [
    {
      "x": 5,
      "y": 18
    },
    {
      "n": 303,
      "e": 167,
      "w": 301
    },
    {
      "title": "Room 187"
    },
    {
      "description": "There are exits to the north east west "
    },

  ],
  "303": [
    {
      "x": 5,
      "y": 19
    },
    {
      "n": 352,
      "s": 187,
      "w": 333
    },
    {
      "title": "Room 303"
    },
    {
      "description": "There are exits to the north south west "
    },
  ],
  "352": [
    {
      "x": 5,
      "y": 20
    },
    {
      "s": 303
    },
    {
      "title": "Room 352"
    },
    {
      "description": "There are exits to the south "
    },

  ],
  "357": [
    {
      "x": 5,
      "y": 21
    },
    {
      "e": 342
    },
    {
      "title": "Room 357"
    },
    {
      "description": "There are exits to the east "
    },

  ],
  "324": [
    {
      "x": 5,
      "y": 22
    },
    {
      "n": 391,
      "e": 289,
      "w": 411
    },
    {
      "title": "Room 324"
    },
    {
      "description": "There are exits to the north east west "
    },

  ],
  "391": [
    {
      "x": 5,
      "y": 23
    },
    {
      "n": 489,
      "s": 324,
      "w": 396
    },
    {
      "title": "Room 391"
    },
    {
      "description": "There are exits to the north south west "
    },
  ],
  "489": [
    {
      "x": 5,
      "y": 24
    },
    {
      "n": 491,
      "s": 391
    },
    {
      "title": "Room 489"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "491": [
    {
      "x": 5,
      "y": 25
    },
    {
      "s": 489
    },
    {
      "title": "Room 491"
    },
    {
      "description": "There are exits to the south "
    },
  ],
  "450": [
    {
      "x": 6,
      "y": 4
    },
    {
      "w": 449
    },
    {
      "title": "Room 450"
    },
    {
      "description": "There are exits to the west "
    },
  ],
  "473": [
    {
      "x": 6,
      "y": 5
    },
    {
      "w": 432
    },
    {
      "title": "Room 473"
    },
    {
      "description": "There are exits to the west "
    },
  ],
  "423": [
    {
      "x": 6,
      "y": 6
    },
    {
      "e": 395
    },
    {
      "title": "Room 423"
    },
    {
      "description": "There are exits to the east "
    },

  ],
  "469": [
    {
      "x": 6,
      "y": 7
    },
    {
      "e": 362
    },
    {
      "title": "Room 469"
    },
    {
      "description": "There are exits to the east "
    },

  ],
  "310": [
    {
      "x": 6,
      "y": 8
    },
    {
      "n": 271
    },
    {
      "title": "Room 310"
    },
    {
      "description": "There are exits to the north "
    },

  ],
  "271": [
    {
      "x": 6,
      "y": 9
    },
    {
      "s": 310,
      "e": 217
    },
    {
      "title": "Room 271"
    },
    {
      "description": "There are exits to the south east "
    },
  ],
  "216": [
    {
      "x": 6,
      "y": 10
    },
    {
      "e": 213,
      "w": 236
    },
    {
      "title": "Room 216"
    },
    {
      "description": "There are exits to the east west "
    },
  ],
  "215": [
    {
      "x": 6,
      "y": 11
    },
    {
      "n": 243,
      "e": 177,
      "w": 220
    },
    {
      "title": "Room 215"
    },
    {
      "description": "There are exits to the north east west "
    },
  ],
  "243": [
    {
      "x": 6,
      "y": 12
    },
    {
      "s": 215
    },
    {
      "title": "Room 243"
    },
    {
      "description": "There are exits to the south "
    },

  ],
  "260": [
    {
      "x": 6,
      "y": 13
    },
    {
      "n": 226,
      "w": 266
    },
    {
      "title": "Room 260"
    },
    {
      "description": "There are exits to the north west "
    },
  ],
  "226": [
    {
      "x": 6,
      "y": 14
    },
    {
      "s": 260,
      "e": 225
    },
    {
      "title": "Room 226"
    },
    {
      "description": "There are exits to the south east "
    },

  ],
  "222": [
    {
      "x": 6,
      "y": 15
    },
    {
      "e": 190,
      "w": 274
    },
    {
      "title": "Room 222"
    },
    {
      "description": "There are exits to the east west "
    },
  ],
  "205": [
    {
      "x": 6,
      "y": 16
    },
    {
      "e": 162,
      "w": 254
    },
    {
      "title": "Room 205"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "194": [
    {
      "x": 6,
      "y": 17
    },
    {
      "e": 128,
      "w": 227
    },
    {
      "title": "Room 194"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "167": [
    {
      "x": 6,
      "y": 18
    },
    {
      "e": 108,
      "w": 187
    },
    {
      "title": "Room 167"
    },
    {
      "description": "There are exits to the east west "
    },
  ],
  "171": [
    {
      "x": 6,
      "y": 19
    },
    {
      "e": 168
    },
    {
      "title": "Room 171"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "297": [
    {
      "x": 6,
      "y": 20
    },
    {
      "e": 207
    },
    {
      "title": "Room 297"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "342": [
    {
      "x": 6,
      "y": 21
    },
    {
      "e": 221,
      "w": 357
    },
    {
      "title": "Room 342"
    },
    {
      "description": "There are exits to the east west "
    },
  ],
  "289": [
    {
      "x": 6,
      "y": 22
    },
    {
      "n": 319,
      "e": 250,
      "w": 324
    },
    {
      "title": "Room 289"
    },
    {
      "description": "There are exits to the north east west "
    },
  ],
  "319": [
    {
      "x": 6,
      "y": 23
    },
    {
      "n": 441,
      "s": 289
    },
    {
      "title": "Room 319"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "441": [
    {
      "x": 6,
      "y": 24
    },
    {
      "s": 319
    },
    {
      "title": "Room 441"
    },
    {
      "description": "There are exits to the south "
    },
  ],
  "453": [
    {
      "x": 6,
      "y": 25
    },
    {
      "e": 351
    },
    {
      "title": "Room 453"
    },
    {
      "description": "There are exits to the east "
    },

  ],
  "395": [
    {
      "x": 7,
      "y": 6
    },
    {
      "n": 362,
      "w": 423
    },
    {
      "title": "Room 395"
    },
    {
      "description": "There are exits to the north west "
    },
  ],
  "362": [
    {
      "x": 7,
      "y": 7
    },
    {
      "n": 327,
      "s": 395,
      "w": 469
    },
    {
      "title": "Room 362"
    },
    {
      "description": "There are exits to the north south west "
    },

  ],
  "327": [
    {
      "x": 7,
      "y": 8
    },
    {
      "s": 362,
      "e": 256
    },
    {
      "title": "Room 327"
    },
    {
      "description": "There are exits to the south east "
    },
  ],
  "217": [
    {
      "x": 7,
      "y": 9
    },
    {
      "n": 213,
      "w": 271
    },
    {
      "title": "Room 217"
    },
    {
      "description": "There are exits to the north west "
    },
  ],
  "213": [
    {
      "x": 7,
      "y": 10
    },
    {
      "s": 217,
      "e": 209,
      "w": 216
    },
    {
      "title": "Room 213"
    },
    {
      "description": "There are exits to the south east west "
    },
  ],
  "177": [
    {
      "x": 7,
      "y": 11
    },
    {
      "e": 156,
      "w": 215
    },
    {
      "title": "Room 177"
    },
    {
      "description": "There are exits to the east west "
    },
  ],
  "180": [
    {
      "x": 7,
      "y": 12
    },
    {
      "e": 164
    },
    {
      "title": "Room 180"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "235": [
    {
      "x": 7,
      "y": 13
    },
    {
      "e": 158
    },
    {
      "title": "Room 235"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "225": [
    {
      "x": 7,
      "y": 14
    },
    {
      "e": 105,
      "w": 226
    },
    {
      "title": "Room 225"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "190": [
    {
      "x": 7,
      "y": 15
    },
    {
      "e": 129,
      "w": 222
    },
    {
      "title": "Room 190"
    },
    {
      "description": "There are exits to the east west "
    },
  ],
  "162": [
    {
      "x": 7,
      "y": 16
    },
    {
      "n": 128,
      "w": 205
    },
    {
      "title": "Room 162"
    },
    {
      "description": "There are exits to the north west "
    },
  ],
  "128": [
    {
      "x": 7,
      "y": 17
    },
    {
      "s": 162,
      "e": 92,
      "w": 194
    },
    {
      "title": "Room 128"
    },
    {
      "description": "There are exits to the south east west "
    },

  ],
  "108": [
    {
      "x": 7,
      "y": 18
    },
    {
      "e": 81,
      "w": 167
    },
    {
      "title": "Room 108"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "168": [
    {
      "x": 7,
      "y": 19
    },
    {
      "n": 207,
      "e": 137,
      "w": 171
    },
    {
      "title": "Room 168"
    },
    {
      "description": "There are exits to the north east west "
    },

  ],
  "207": [
    {
      "x": 7,
      "y": 20
    },
    {
      "s": 168,
      "w": 297
    },
    {
      "title": "Room 207"
    },
    {
      "description": "There are exits to the south west "
    },

  ],
  "221": [
    {
      "x": 7,
      "y": 21
    },
    {
      "n": 250,
      "e": 174,
      "w": 342
    },
    {
      "title": "Room 221"
    },
    {
      "description": "There are exits to the north east west "
    },
  ],
  "250": [
    {
      "x": 7,
      "y": 22
    },
    {
      "n": 295,
      "s": 221,
      "w": 289
    },
    {
      "title": "Room 250"
    },
    {
      "description": "There are exits to the north south west "
    },
  ],
  "295": [
    {
      "x": 7,
      "y": 23
    },
    {
      "n": 332,
      "s": 250
    },
    {
      "title": "Room 295"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "332": [
    {
      "x": 7,
      "y": 24
    },
    {
      "n": 351,
      "s": 295
    },
    {
      "title": "Room 332"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "351": [
    {
      "x": 7,
      "y": 25
    },
    {
      "n": 417,
      "s": 332,
      "w": 453
    },
    {
      "title": "Room 351"
    },
    {
      "description": "There are exits to the north south west "
    },

  ],
  "417": [
    {
      "x": 7,
      "y": 26
    },
    {
      "n": 442,
      "s": 351
    },
    {
      "title": "Room 417"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "442": [
    {
      "x": 7,
      "y": 27
    },
    {
      "s": 417
    },
    {
      "title": "Room 442"
    },
    {
      "description": "There are exits to the south "
    },
  ],
  "410": [
    {
      "x": 8,
      "y": 5
    },
    {
      "e": 406
    },
    {
      "title": "Room 410"
    },
    {
      "description": "There are exits to the east "
    },

  ],
  "323": [
    {
      "x": 8,
      "y": 6
    },
    {
      "n": 279
    },
    {
      "title": "Room 323"
    },
    {
      "description": "There are exits to the north "
    },
  ],
  "279": [
    {
      "x": 8,
      "y": 7
    },
    {
      "n": 256,
      "s": 323
    },
    {
      "title": "Room 279"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "256": [
    {
      "x": 8,
      "y": 8
    },
    {
      "n": 241,
      "s": 279,
      "w": 327
    },
    {
      "title": "Room 256"
    },
    {
      "description": "There are exits to the north south west "
    },
  ],
  "241": [
    {
      "x": 8,
      "y": 9
    },
    {
      "s": 256,
      "e": 193
    },
    {
      "title": "Room 241"
    },
    {
      "description": "There are exits to the south east "
    },
  ],
  "209": [
    {
      "x": 8,
      "y": 10
    },
    {
      "n": 156,
      "w": 213
    },
    {
      "title": "Room 209"
    },
    {
      "description": "There are exits to the north west "
    },
  ],
  "156": [
    {
      "x": 8,
      "y": 11
    },
    {
      "s": 209,
      "e": 149,
      "w": 177
    },
    {
      "title": "Room 156"
    },
    {
      "description": "There are exits to the south east west "
    },

  ],
  "164": [
    {
      "x": 8,
      "y": 12
    },
    {
      "n": 158,
      "w": 180
    },
    {
      "title": "Room 164"
    },
    {
      "description": "There are exits to the north west "
    },
  ],
  "158": [
    {
      "x": 8,
      "y": 13
    },
    {
      "s": 164,
      "e": 126,
      "w": 235
    },
    {
      "title": "Room 158"
    },
    {
      "description": "There are exits to the south east west "
    },
  ],
  "105": [
    {
      "x": 8,
      "y": 14
    },
    {
      "n": 129,
      "e": 104,
      "w": 225
    },
    {
      "title": "Room 105"
    },
    {
      "description": "There are exits to the north east west "
    },
  ],
  "129": [
    {
      "x": 8,
      "y": 15
    },
    {
      "s": 105,
      "w": 190
    },
    {
      "title": "Room 129"
    },
    {
      "description": "There are exits to the south west "
    },
  ],
  "100": [
    {
      "x": 8,
      "y": 16
    },
    {
      "n": 92
    },
    {
      "title": "Room 100"
    },
    {
      "description": "There are exits to the north "
    },

  ],
  "92": [
    {
      "x": 8,
      "y": 17
    },
    {
      "n": 81,
      "s": 100,
      "w": 128
    },
    {
      "title": "Room 92"
    },
    {
      "description": "There are exits to the north south west "
    },
  ],
  "81": [
    {
      "x": 8,
      "y": 18
    },
    {
      "n": 137,
      "s": 92,
      "e": 45,
      "w": 108
    },
    {
      "title": "Room 81"
    },
    {
      "description": "There are exits to the north south east west "
    },

  ],
  "137": [
    {
      "x": 8,
      "y": 19
    },
    {
      "s": 81,
      "w": 168
    },
    {
      "title": "Room 137"
    },
    {
      "description": "There are exits to the south west "
    },

  ],
  "124": [
    {
      "x": 8,
      "y": 20
    },
    {
      "n": 174,
      "e": 112
    },
    {
      "title": "Room 124"
    },
    {
      "description": "There are exits to the north east "
    },
  ],
  "174": [
    {
      "x": 8,
      "y": 21
    },
    {
      "n": 277,
      "s": 124,
      "w": 221
    },
    {
      "title": "Room 174"
    },
    {
      "description": "There are exits to the north south west "
    },

  ],
  "277": [
    {
      "x": 8,
      "y": 22
    },
    {
      "n": 331,
      "s": 174
    },
    {
      "title": "Room 277"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "331": [
    {
      "x": 8,
      "y": 23
    },
    {
      "n": 387,
      "s": 277
    },
    {
      "title": "Room 331"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "387": [
    {
      "x": 8,
      "y": 24
    },
    {
      "n": 444,
      "s": 331
    },
    {
      "title": "Room 387"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "444": [
    {
      "x": 8,
      "y": 25
    },
    {
      "s": 387
    },
    {
      "title": "Room 444"
    },
    {
      "description": "There are exits to the south "
    },
  ],
  "422": [
    {
      "x": 8,
      "y": 26
    },
    {
      "n": 461,
      "e": 394
    },
    {
      "title": "Room 422"
    },
    {
      "description": "There are exits to the north east "
    },
  ],
  "461": [
    {
      "x": 8,
      "y": 27
    },
    {
      "s": 422
    },
    {
      "title": "Room 461"
    },
    {
      "description": "There are exits to the south "
    },

  ],
  "406": [
    {
      "x": 9,
      "y": 5
    },
    {
      "n": 315,
      "w": 410
    },
    {
      "title": "Room 406"
    },
    {
      "description": "There are exits to the north west "
    },
  ],
  "315": [
    {
      "x": 9,
      "y": 6
    },
    {
      "n": 269,
      "s": 406,
      "e": 335
    },
    {
      "title": "Room 315"
    },
    {
      "description": "There are exits to the north south east "
    },
  ],
  "269": [
    {
      "x": 9,
      "y": 7
    },
    {
      "n": 203,
      "s": 315
    },
    {
      "title": "Room 269"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "203": [
    {
      "x": 9,
      "y": 8
    },
    {
      "n": 193,
      "s": 269
    },
    {
      "title": "Room 203"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "193": [
    {
      "x": 9,
      "y": 9
    },
    {
      "n": 191,
      "s": 203,
      "w": 241
    },
    {
      "title": "Room 193"
    },
    {
      "description": "There are exits to the north south west "
    },
  ],
  "191": [
    {
      "x": 9,
      "y": 10
    },
    {
      "n": 149,
      "s": 193
    },
    {
      "title": "Room 191"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "149": [
    {
      "x": 9,
      "y": 11
    },
    {
      "n": 135,
      "s": 191,
      "w": 156
    },
    {
      "title": "Room 149"
    },
    {
      "description": "There are exits to the north south west "
    },
  ],
  "135": [
    {
      "x": 9,
      "y": 12
    },
    {
      "n": 126,
      "s": 149
    },
    {
      "title": "Room 135"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "126": [
    {
      "x": 9,
      "y": 13
    },
    {
      "n": 104,
      "s": 135,
      "w": 158
    },
    {
      "title": "Room 126"
    },
    {
      "description": "There are exits to the north south west "
    },

  ],
  "104": [
    {
      "x": 9,
      "y": 14
    },
    {
      "n": 89,
      "s": 126,
      "w": 105
    },
    {
      "title": "Room 104"
    },
    {
      "description": "There are exits to the north south west "
    },
  ],
  "89": [
    {
      "x": 9,
      "y": 15
    },
    {
      "n": 72,
      "s": 104
    },
    {
      "title": "Room 89"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "72": [
    {
      "x": 9,
      "y": 16
    },
    {
      "n": 69,
      "s": 89
    },
    {
      "title": "Room 72"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "69": [
    {
      "x": 9,
      "y": 17
    },
    {
      "s": 72,
      "e": 41
    },
    {
      "title": "Room 69"
    },
    {
      "description": "There are exits to the south east "
    },

  ],
  "45": [
    {
      "x": 9,
      "y": 18
    },
    {
      "n": 85,
      "e": 40,
      "w": 81
    },
    {
      "title": "Room 45"
    },
    {
      "description": "There are exits to the north east west "
    },

  ],
  "85": [
    {
      "x": 9,
      "y": 19
    },
    {
      "s": 45
    },
    {
      "title": "Room 85"
    },
    {
      "description": "There are exits to the south "
    },
  ],
  "112": [
    {
      "x": 9,
      "y": 20
    },
    {
      "n": 210,
      "e": 106,
      "w": 124
    },
    {
      "title": "Room 112"
    },
    {
      "description": "There are exits to the north east west "
    },

  ],
  "210": [
    {
      "x": 9,
      "y": 21
    },
    {
      "s": 112
    },
    {
      "title": "Room 210"
    },
    {
      "description": "There are exits to the south "
    },

  ],
  "208": [
    {
      "x": 9,
      "y": 22
    },
    {
      "n": 307,
      "e": 166
    },
    {
      "title": "Room 208"
    },
    {
      "description": "There are exits to the north east "
    },

  ],
  "307": [
    {
      "x": 9,
      "y": 23
    },
    {
      "s": 208
    },
    {
      "title": "Room 307"
    },
    {
      "description": "There are exits to the south "
    },

  ],
  "341": [
    {
      "x": 9,
      "y": 24
    },
    {
      "e": 316
    },
    {
      "title": "Room 341"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "374": [
    {
      "x": 9,
      "y": 25
    },
    {
      "e": 340
    },
    {
      "title": "Room 374"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "394": [
    {
      "x": 9,
      "y": 26
    },
    {
      "n": 426,
      "e": 318,
      "w": 422
    },
    {
      "title": "Room 394"
    },
    {
      "description": "There are exits to the north east west "
    },

  ],
  "426": [
    {
      "x": 9,
      "y": 27
    },
    {
      "s": 394
    },
    {
      "title": "Room 426"
    },
    {
      "description": "There are exits to the south "
    },

  ],
  "477": [
    {
      "x": 9,
      "y": 29
    },
    {
      "e": 443
    },
    {
      "title": "Room 477"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "485": [
    {
      "x": 10,
      "y": 3
    },
    {
      "e": 481
    },
    {
      "title": "Room 485"
    },
    {
      "description": "There are exits to the east "
    },

  ],
  "346": [
    {
      "x": 10,
      "y": 5
    },
    {
      "n": 335
    },
    {
      "title": "Room 346"
    },
    {
      "description": "There are exits to the north "
    },

  ],
  "335": [
    {
      "x": 10,
      "y": 6
    },
    {
      "s": 346,
      "e": 378,
      "w": 315
    },
    {
      "title": "Room 335"
    },
    {
      "description": "There are exits to the south east west "
    },
  ],
  "369": [
    {
      "x": 10,
      "y": 7
    },
    {
      "n": 247
    },
    {
      "title": "Room 369"
    },
    {
      "description": "There are exits to the north "
    },
  ],
  "247": [
    {
      "x": 10,
      "y": 8
    },
    {
      "s": 369,
      "e": 234
    },
    {
      "title": "Room 247"
    },
    {
      "description": "There are exits to the south east "
    },

  ],
  "151": [
    {
      "x": 10,
      "y": 9
    },
    {
      "n": 188,
      "e": 133
    },
    {
      "title": "Room 151"
    },
    {
      "description": "There are exits to the north east "
    },
  ],
  "188": [
    {
      "x": 10,
      "y": 10
    },
    {
      "s": 151
    },
    {
      "title": "Room 188"
    },
    {
      "description": "There are exits to the south "
    },

  ],
  "183": [
    {
      "x": 10,
      "y": 11
    },
    {
      "n": 145
    },
    {
      "title": "Room 183"
    },
    {
      "description": "There are exits to the north "
    },

  ],
  "145": [
    {
      "x": 10,
      "y": 12
    },
    {
      "s": 183,
      "e": 113
    },
    {
      "title": "Room 145"
    },
    {
      "description": "There are exits to the south east "
    },
  ],
  "122": [
    {
      "x": 10,
      "y": 13
    },
    {
      "n": 99
    },
    {
      "title": "Room 122"
    },
    {
      "description": "There are exits to the north "
    },
  ],
  "99": [
    {
      "x": 10,
      "y": 14
    },
    {
      "n": 83,
      "s": 122
    },
    {
      "title": "Room 99"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "83": [
    {
      "x": 10,
      "y": 15
    },
    {
      "s": 99,
      "e": 80
    },
    {
      "title": "Room 83"
    },
    {
      "description": "There are exits to the south east "
    },

  ],
  "76": [
    {
      "x": 10,
      "y": 16
    },
    {
      "n": 41
    },
    {
      "title": "Room 76"
    },
    {
      "description": "There are exits to the north "
    },

  ],
  "41": [
    {
      "x": 10,
      "y": 17
    },
    {
      "s": 76,
      "e": 36,
      "w": 69
    },
    {
      "title": "Room 41"
    },
    {
      "description": "There are exits to the south east west "
    },
  ],
  "40": [
    {
      "x": 10,
      "y": 18
    },
    {
      "n": 74,
      "e": 19,
      "w": 45
    },
    {
      "title": "Room 40"
    },
    {
      "description": "There are exits to the north east west "
    },
  ],
  "74": [
    {
      "x": 10,
      "y": 19
    },
    {
      "s": 40
    },
    {
      "title": "Room 74"
    },
    {
      "description": "There are exits to the south "
    },

  ],
  "106": [
    {
      "x": 10,
      "y": 20
    },
    {
      "n": 161,
      "e": 79,
      "w": 112
    },
    {
      "title": "Room 106"
    },
    {
      "description": "There are exits to the north east west "
    },

  ],
  "161": [
    {
      "x": 10,
      "y": 21
    },
    {
      "n": 166,
      "s": 106
    },
    {
      "title": "Room 161"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "166": [
    {
      "x": 10,
      "y": 22
    },
    {
      "s": 161,
      "w": 208
    },
    {
      "title": "Room 166"
    },
    {
      "description": "There are exits to the south west "
    },

  ],
  "292": [
    {
      "x": 10,
      "y": 23
    },
    {
      "n": 316,
      "e": 185
    },
    {
      "title": "Room 292"
    },
    {
      "description": "There are exits to the north east "
    },

  ],
  "316": [
    {
      "x": 10,
      "y": 24
    },
    {
      "s": 292,
      "w": 341
    },
    {
      "title": "Room 316"
    },
    {
      "description": "There are exits to the south west "
    },

  ],
  "340": [
    {
      "x": 10,
      "y": 25
    },
    {
      "n": 318,
      "w": 374
    },
    {
      "title": "Room 340"
    },
    {
      "description": "There are exits to the north west "
    },

  ],
  "318": [
    {
      "x": 10,
      "y": 26
    },
    {
      "s": 340,
      "e": 199,
      "w": 394
    },
    {
      "title": "Room 318"
    },
    {
      "description": "There are exits to the south east west "
    },
  ],
  "392": [
    {
      "x": 10,
      "y": 27
    },
    {
      "n": 408,
      "e": 281
    },
    {
      "title": "Room 392"
    },
    {
      "description": "There are exits to the north east "
    },

  ],
  "408": [
    {
      "x": 10,
      "y": 28
    },
    {
      "n": 443,
      "s": 392
    },
    {
      "title": "Room 408"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "443": [
    {
      "x": 10,
      "y": 29
    },
    {
      "s": 408,
      "w": 477
    },
    {
      "title": "Room 443"
    },
    {
      "description": "There are exits to the south west "
    },

  ],
  "481": [
    {
      "x": 11,
      "y": 3
    },
    {
      "n": 472,
      "w": 485
    },
    {
      "title": "Room 481"
    },
    {
      "description": "There are exits to the north west "
    },

  ],
  "472": [
    {
      "x": 11,
      "y": 4
    },
    {
      "n": 466,
      "s": 481,
      "e": 495
    },
    {
      "title": "Room 472"
    },
    {
      "description": "There are exits to the north south east "
    },

  ],
  "466": [
    {
      "x": 11,
      "y": 5
    },
    {
      "n": 378,
      "s": 472
    },
    {
      "title": "Room 466"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "378": [
    {
      "x": 11,
      "y": 6
    },
    {
      "s": 466,
      "w": 335
    },
    {
      "title": "Room 378"
    },
    {
      "description": "There are exits to the south west "
    },

  ],
  "280": [
    {
      "x": 11,
      "y": 7
    },
    {
      "n": 234
    },
    {
      "title": "Room 280"
    },
    {
      "description": "There are exits to the north "
    },

  ],
  "234": [
    {
      "x": 11,
      "y": 8
    },
    {
      "n": 133,
      "s": 280,
      "e": 259,
      "w": 247
    },
    {
      "title": "Room 234"
    },
    {
      "description": "There are exits to the north south east west "
    },

  ],
  "133": [
    {
      "x": 11,
      "y": 9
    },
    {
      "s": 234,
      "e": 118,
      "w": 151
    },
    {
      "title": "Room 133"
    },
    {
      "description": "There are exits to the south east west "
    },
  ],
  "157": [
    {
      "x": 11,
      "y": 10
    },
    {
      "e": 110
    },
    {
      "title": "Room 157"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "153": [
    {
      "x": 11,
      "y": 11
    },
    {
      "e": 97
    },
    {
      "title": "Room 153"
    },
    {
      "description": "There are exits to the east "
    },

  ],
  "113": [
    {
      "x": 11,
      "y": 12
    },
    {
      "e": 94,
      "w": 145
    },
    {
      "title": "Room 113"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "68": [
    {
      "x": 11,
      "y": 13
    },
    {
      "e": 57
    },
    {
      "title": "Room 68"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "58": [
    {
      "x": 11,
      "y": 14
    },
    {
      "e": 23
    },
    {
      "title": "Room 58"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "80": [
    {
      "x": 11,
      "y": 15
    },
    {
      "n": 11,
      "w": 83
    },
    {
      "title": "Room 80"
    },
    {
      "description": "There are exits to the north west "
    },
  ],
  "11": [
    {
      "x": 11,
      "y": 16
    },
    {
      "s": 80,
      "e": 3
    },
    {
      "title": "Room 11"
    },
    {
      "description": "There are exits to the south east "
    },

  ],
  "36": [
    {
      "x": 11,
      "y": 17
    },
    {
      "e": 21,
      "w": 41
    },
    {
      "title": "Room 36"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "19": [
    {
      "x": 11,
      "y": 18
    },
    {
      "n": 32,
      "e": 15,
      "w": 40
    },
    {
      "title": "Room 19"
    },
    {
      "description": "There are exits to the north east west "
    },
  ],
  "32": [
    {
      "x": 11,
      "y": 19
    },
    {
      "s": 19
    },
    {
      "title": "Room 32"
    },
    {
      "description": "There are exits to the south "
    },

  ],
  "79": [
    {
      "x": 11,
      "y": 20
    },
    {
      "e": 46,
      "w": 106
    },
    {
      "title": "Room 79"
    },
    {
      "description": "There are exits to the east west "
    },
  ],
  "63": [
    {
      "x": 11,
      "y": 21
    },
    {
      "n": 140,
      "e": 61
    },
    {
      "title": "Room 63"
    },
    {
      "description": "There are exits to the north east "
    },

  ],
  "140": [
    {
      "x": 11,
      "y": 22
    },
    {
      "s": 63
    },
    {
      "title": "Room 140"
    },
    {
      "description": "There are exits to the south "
    },
  ],
  "185": [
    {
      "x": 11,
      "y": 23
    },
    {
      "n": 195,
      "e": 155,
      "w": 292
    },
    {
      "title": "Room 185"
    },
    {
      "description": "There are exits to the north east west "
    },

  ],
  "195": [
    {
      "x": 11,
      "y": 24
    },
    {
      "s": 185
    },
    {
      "title": "Room 195"
    },
    {
      "description": "There are exits to the south "
    },
  ],
  "328": [
    {
      "x": 11,
      "y": 25
    },
    {
      "e": 200
    },
    {
      "title": "Room 328"
    },
    {
      "description": "There are exits to the east "
    },

  ],
  "199": [
    {
      "x": 11,
      "y": 26
    },
    {
      "n": 281,
      "e": 197,
      "w": 318
    },
    {
      "title": "Room 199"
    },
    {
      "description": "There are exits to the north east west "
    },
  ],
  "281": [
    {
      "x": 11,
      "y": 27
    },
    {
      "n": 350,
      "s": 199,
      "w": 392
    },
    {
      "title": "Room 281"
    },
    {
      "description": "There are exits to the north south west "
    },

  ],
  "350": [
    {
      "x": 11,
      "y": 28
    },
    {
      "n": 425,
      "s": 281
    },
    {
      "title": "Room 350"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "425": [
    {
      "x": 11,
      "y": 29
    },
    {
      "n": 434,
      "s": 350
    },
    {
      "title": "Room 425"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "434": [
    {
      "x": 11,
      "y": 30
    },
    {
      "s": 425
    },
    {
      "title": "Room 434"
    },
    {
      "description": "There are exits to the south "
    },
  ],
  "495": [
    {
      "x": 12,
      "y": 4
    },
    {
      "w": 472
    },
    {
      "title": "Room 495"
    },
    {
      "description": "There are exits to the west "
    },

  ],
  "415": [
    {
      "x": 12,
      "y": 5
    },
    {
      "n": 306
    },
    {
      "title": "Room 415"
    },
    {
      "description": "There are exits to the north "
    },
  ],
  "306": [
    {
      "x": 12,
      "y": 6
    },
    {
      "n": 291,
      "s": 415
    },
    {
      "title": "Room 306"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "291": [
    {
      "x": 12,
      "y": 7
    },
    {
      "n": 259,
      "s": 306
    },
    {
      "title": "Room 291"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "259": [
    {
      "x": 12,
      "y": 8
    },
    {
      "s": 291,
      "w": 234
    },
    {
      "title": "Room 259"
    },
    {
      "description": "There are exits to the south west "
    },

  ],
  "118": [
    {
      "x": 12,
      "y": 9
    },
    {
      "n": 110,
      "e": 218,
      "w": 133
    },
    {
      "title": "Room 118"
    },
    {
      "description": "There are exits to the north east west "
    },
  ],
  "110": [
    {
      "x": 12,
      "y": 10
    },
    {
      "n": 97,
      "s": 118,
      "w": 157
    },
    {
      "title": "Room 110"
    },
    {
      "description": "There are exits to the north south west "
    },

  ],
  "97": [
    {
      "x": 12,
      "y": 11
    },
    {
      "n": 94,
      "s": 110,
      "w": 153
    },
    {
      "title": "Room 97"
    },
    {
      "description": "There are exits to the north south west "
    },
  ],
  "94": [
    {
      "x": 12,
      "y": 12
    },
    {
      "n": 57,
      "s": 97,
      "w": 113
    },
    {
      "title": "Room 94"
    },
    {
      "description": "There are exits to the north south west "
    },
  ],
  "57": [
    {
      "x": 12,
      "y": 13
    },
    {
      "n": 23,
      "s": 94,
      "w": 68
    },
    {
      "title": "Room 57"
    },
    {
      "description": "There are exits to the north south west "
    },

  ],
  "23": [
    {
      "x": 12,
      "y": 14
    },
    {
      "s": 57,
      "e": 6,
      "w": 58
    },
    {
      "title": "Room 23"
    },
    {
      "description": "There are exits to the south east west "
    },
  ],
  "16": [
    {
      "x": 12,
      "y": 15
    },
    {
      "e": 8
    },
    {
      "title": "Room 16"
    },
    {
      "description": "There are exits to the east "
    },

  ],
  "3": [
    {
      "x": 12,
      "y": 16
    },
    {
      "n": 21,
      "e": 0,
      "w": 11
    },
    {
      "title": "Room 3"
    },
    {
      "description": "There are exits to the north east west "
    },
  ],
  "21": [
    {
      "x": 12,
      "y": 17
    },
    {
      "s": 3,
      "w": 36
    },
    {
      "title": "Room 21"
    },
    {
      "description": "There are exits to the south west "
    },
  ],
  "15": [
    {
      "x": 12,
      "y": 18
    },
    {
      "e": 13,
      "w": 19
    },
    {
      "title": "Room 15"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "47": [
    {
      "x": 12,
      "y": 19
    },
    {
      "e": 14
    },
    {
      "title": "Room 47"
    },
    {
      "description": "There are exits to the east "
    },
  ],
  "46": [
    {
      "x": 12,
      "y": 20
    },
    {
      "n": 61,
      "e": 17,
      "w": 79
    },
    {
      "title": "Room 46"
    },
    {
      "description": "There are exits to the north east west "
    },
  ],
  "61": [
    {
      "x": 12,
      "y": 21
    },
    {
      "n": 82,
      "s": 46,
      "w": 63
    },
    {
      "title": "Room 61"
    },
    {
      "description": "There are exits to the north south west "
    },
  ],
  "82": [
    {
      "x": 12,
      "y": 22
    },
    {
      "n": 155,
      "s": 61
    },
    {
      "title": "Room 82"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "155": [
    {
      "x": 12,
      "y": 23
    },
    {
      "s": 82,
      "w": 185
    },
    {
      "title": "Room 155"
    },
    {
      "description": "There are exits to the south west "
    },

  ],
  "175": [
    {
      "x": 12,
      "y": 24
    },
    {
      "n": 200,
      "e": 141
    },
    {
      "title": "Room 175"
    },
    {
      "description": "There are exits to the north east "
    },

  ],
  "200": [
    {
      "x": 12,
      "y": 25
    },
    {
      "s": 175,
      "e": 204,
      "w": 328
    },
    {
      "title": "Room 200"
    },
    {
      "description": "There are exits to the south east west "
    },

  ],
  "197": [
    {
      "x": 12,
      "y": 26
    },
    {
      "e": 165,
      "w": 199
    },
    {
      "title": "Room 197"
    },
    {
      "description": "There are exits to the east west "
    },
  ],
  "223": [
    {
      "x": 12,
      "y": 27
    },
    {
      "n": 483,
      "e": 169
    },
    {
      "title": "Room 223"
    },
    {
      "description": "There are exits to the north east "
    },

  ],
  "483": [
    {
      "x": 12,
      "y": 28
    },
    {
      "s": 223
    },
    {
      "title": "Room 483"
    },
    {
      "description": "There are exits to the south "
    },
  ],
  "488": [
    {
      "x": 13,
      "y": 4
    },
    {
      "n": 409
    },
    {
      "title": "Room 488"
    },
    {
      "description": "There are exits to the north "
    },
  ],
  "409": [
    {
      "x": 13,
      "y": 5
    },
    {
      "n": 345,
      "s": 488
    },
    {
      "title": "Room 409"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "345": [
    {
      "x": 13,
      "y": 6
    },
    {
      "n": 261,
      "s": 409
    },
    {
      "title": "Room 345"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "261": [
    {
      "x": 13,
      "y": 7
    },
    {
      "n": 252,
      "s": 345
    },
    {
      "title": "Room 261"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "252": [
    {
      "x": 13,
      "y": 8
    },
    {
      "n": 218,
      "s": 261
    },
    {
      "title": "Room 252"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "218": [
    {
      "x": 13,
      "y": 9
    },
    {
      "n": 144,
      "s": 252,
      "w": 118
    },
    {
      "title": "Room 218"
    },
    {
      "description": "There are exits to the north south west "
    },

  ],
  "144": [
    {
      "x": 13,
      "y": 10
    },
    {
      "n": 134,
      "s": 218
    },
    {
      "title": "Room 144"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "134": [
    {
      "x": 13,
      "y": 11
    },
    {
      "n": 65,
      "s": 144
    },
    {
      "title": "Room 134"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "65": [
    {
      "x": 13,
      "y": 12
    },
    {
      "n": 62,
      "s": 134
    },
    {
      "title": "Room 65"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "62": [
    {
      "x": 13,
      "y": 13
    },
    {
      "n": 6,
      "s": 65
    },
    {
      "title": "Room 62"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "6": [
    {
      "x": 13,
      "y": 14
    },
    {
      "s": 62,
      "e": 5,
      "w": 23
    },
    {
      "title": "Room 6"
    },
    {
      "description": "There are exits to the south east west "
    },
  ],
  "8": [
    {
      "x": 13,
      "y": 15
    },
    {
      "n": 0,
      "w": 16
    },
    {
      "title": "Room 8"
    },
    {
      "description": "There are exits to the north west "
    },

  ],
  "0": [
    {
      "x": 13,
      "y": 16
    },
    {
      "n": 4,
      "s": 8,
      "e": 1,
      "w": 3
    },
    {
      "title": "Room 0"
    },
    {
      "description": "There are exits to the north south east west "
    },
  ],
  "4": [
    {
      "x": 13,
      "y": 17
    },
    {
      "s": 0
    },
    {
      "title": "Room 4"
    },
    {
      "description": "There are exits to the south "
    },
  ],
  "13": [
    {
      "x": 13,
      "y": 18
    },
    {
      "n": 14,
      "e": 9,
      "w": 15
    },
    {
      "title": "Room 13"
    },
    {
      "description": "There are exits to the north east west "
    },

  ],
  "14": [
    {
      "x": 13,
      "y": 19
    },
    {
      "n": 17,
      "s": 13,
      "w": 47
    },
    {
      "title": "Room 14"
    },
    {
      "description": "There are exits to the north south west "
    },

  ],
  "17": [
    {
      "x": 13,
      "y": 20
    },
    {
      "n": 33,
      "s": 14,
      "e": 28,
      "w": 46
    },
    {
      "title": "Room 17"
    },
    {
      "description": "There are exits to the north south east west "
    },
  ],
  "33": [
    {
      "x": 13,
      "y": 21
    },
    {
      "s": 17
    },
    {
      "title": "Room 33"
    },
    {
      "description": "There are exits to the south "
    },
  ],
  "102": [
    {
      "x": 13,
      "y": 22
    },
    {
      "n": 107,
      "e": 64
    },
    {
      "title": "Room 102"
    },
    {
      "description": "There are exits to the north east "
    },

  ],
  "107": [
    {
      "x": 13,
      "y": 23
    },
    {
      "n": 141,
      "s": 102
    },
    {
      "title": "Room 107"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "141": [
    {
      "x": 13,
      "y": 24
    },
    {
      "s": 107,
      "w": 175
    },
    {
      "title": "Room 141"
    },
    {
      "description": "There are exits to the south west "
    },

  ],
  "204": [
    {
      "x": 13,
      "y": 25
    },
    {
      "w": 200
    },
    {
      "title": "Room 204"
    },
    {
      "description": "There are exits to the west "
    },

  ],
  "165": [
    {
      "x": 13,
      "y": 26
    },
    {
      "n": 169,
      "e": 163,
      "w": 197
    },
    {
      "title": "Room 165"
    },
    {
      "description": "There are exits to the north east west "
    },
  ],
  "169": [
    {
      "x": 13,
      "y": 27
    },
    {
      "n": 385,
      "s": 165,
      "w": 223
    },
    {
      "title": "Room 169"
    },
    {
      "description": "There are exits to the north south west "
    },

  ],
  "385": [
    {
      "x": 13,
      "y": 28
    },
    {
      "s": 169
    },
    {
      "title": "Room 385"
    },
    {
      "description": "There are exits to the south "
    },
  ],
  "497": [
    {
      "x": 13,
      "y": 30
    },
    {
      "e": 366
    },
    {
      "title": "Room 497"
    },
    {
      "description": "There are exits to the east "
    },

  ],
  "424": [
    {
      "x": 14,
      "y": 4
    },
    {
      "n": 322
    },
    {
      "title": "Room 424"
    },
    {
      "description": "There are exits to the north "
    },
  ],
  "322": [
    {
      "x": 14,
      "y": 5
    },
    {
      "s": 424,
      "e": 276
    },
    {
      "title": "Room 322"
    },
    {
      "description": "There are exits to the south east "
    },
  ],
  "290": [
    {
      "x": 14,
      "y": 6
    },
    {
      "n": 264
    },
    {
      "title": "Room 290"
    },
    {
      "description": "There are exits to the north "
    },
  ],
  "264": [
    {
      "x": 14,
      "y": 7
    },
    {
      "n": 244,
      "s": 290
    },
    {
      "title": "Room 264"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "244": [
    {
      "x": 14,
      "y": 8
    },
    {
      "s": 264,
      "e": 232
    },
    {
      "title": "Room 244"
    },
    {
      "description": "There are exits to the south east "
    },

  ],
  "181": [
    {
      "x": 14,
      "y": 9
    },
    {
      "n": 179
    },
    {
      "title": "Room 181"
    },
    {
      "description": "There are exits to the north "
    },

  ],
  "179": [
    {
      "x": 14,
      "y": 10
    },
    {
      "n": 96,
      "s": 181,
      "e": 201
    },
    {
      "title": "Room 179"
    },
    {
      "description": "There are exits to the north south east "
    },
  ],
  "96": [
    {
      "x": 14,
      "y": 11
    },
    {
      "n": 66,
      "s": 179
    },
    {
      "title": "Room 96"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "66": [
    {
      "x": 14,
      "y": 12
    },
    {
      "n": 50,
      "s": 96
    },
    {
      "title": "Room 66"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "50": [
    {
      "x": 14,
      "y": 13
    },
    {
      "n": 5,
      "s": 66,
      "e": 70
    },
    {
      "title": "Room 50"
    },
    {
      "description": "There are exits to the north south east "
    },

  ],
  "5": [
    {
      "x": 14,
      "y": 14
    },
    {
      "n": 2,
      "s": 50,
      "w": 6
    },
    {
      "title": "Room 5"
    },
    {
      "description": "There are exits to the north south west "
    },
  ],
  "2": [
    {
      "x": 14,
      "y": 15
    },
    {
      "n": 1,
      "s": 5,
      "e": 10
    },
    {
      "title": "Room 2"
    },
    {
      "description": "There are exits to the north south east "
    },
  ],
  "1": [
    {
      "x": 14,
      "y": 16
    },
    {
      "n": 7,
      "s": 2,
      "e": 22,
      "w": 0
    },
    {
      "title": "Room 1"
    },
    {
      "description": "There are exits to the north south east west "
    },

  ],
  "7": [
    {
      "x": 14,
      "y": 17
    },
    {
      "n": 9,
      "s": 1,
      "e": 12
    },
    {
      "title": "Room 7"
    },
    {
      "description": "There are exits to the north south east "
    },
  ],
  "9": [
    {
      "x": 14,
      "y": 18
    },
    {
      "s": 7,
      "w": 13
    },
    {
      "title": "Room 9"
    },
    {
      "description": "There are exits to the south west "
    },
  ],
  "30": [
    {
      "x": 14,
      "y": 19
    },
    {
      "n": 28
    },
    {
      "title": "Room 30"
    },
    {
      "description": "There are exits to the north "
    },
  ],
  "28": [
    {
      "x": 14,
      "y": 20
    },
    {
      "n": 60,
      "s": 30,
      "w": 17
    },
    {
      "title": "Room 28"
    },
    {
      "description": "There are exits to the north south west "
    },

  ],
  "60": [
    {
      "x": 14,
      "y": 21
    },
    {
      "n": 64,
      "s": 28
    },
    {
      "title": "Room 60"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "64": [
    {
      "x": 14,
      "y": 22
    },
    {
      "n": 111,
      "s": 60,
      "w": 102
    },
    {
      "title": "Room 64"
    },
    {
      "description": "There are exits to the north south west "
    },

  ],
  "111": [
    {
      "x": 14,
      "y": 23
    },
    {
      "n": 121,
      "s": 64,
      "e": 114
    },
    {
      "title": "Room 111"
    },
    {
      "description": "There are exits to the north south east "
    },
  ],
  "121": [
    {
      "x": 14,
      "y": 24
    },
    {
      "n": 148,
      "s": 111,
      "e": 123
    },
    {
      "title": "Room 121"
    },
    {
      "description": "There are exits to the north south east "
    },
  ],
  "148": [
    {
      "x": 14,
      "y": 25
    },
    {
      "n": 163,
      "s": 121,
      "e": 178
    },
    {
      "title": "Room 148"
    },
    {
      "description": "There are exits to the north south east "
    },

  ],
  "163": [
    {
      "x": 14,
      "y": 26
    },
    {
      "n": 257,
      "s": 148,
      "e": 228,
      "w": 165
    },
    {
      "title": "Room 163"
    },
    {
      "description": "There are exits to the north south east west "
    },

  ],
  "257": [
    {
      "x": 14,
      "y": 27
    },
    {
      "n": 388,
      "s": 163
    },
    {
      "title": "Room 257"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "388": [
    {
      "x": 14,
      "y": 28
    },
    {
      "s": 257,
      "n": 386
    },
    {
      "title": "Room 388"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "386": [
    {
      "x": 14,
      "y": 29
    },
    {
      "e": 354,
      "s": 388
    },
    {
      "title": "Room 386"
    },
    {
      "description": "There are exits to the south east "
    },
  ],
  "366": [
    {
      "x": 14,
      "y": 30
    },
    {
      "e": 361,
      "w": 497
    },
    {
      "title": "Room 366"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "467": [
    {
      "x": 15,
      "y": 3
    },
    {
      "n": 459
    },
    {
      "title": "Room 467"
    },
    {
      "description": "There are exits to the north "
    },

  ],
  "459": [
    {
      "x": 15,
      "y": 4
    },
    {
      "n": 276,
      "s": 467
    },
    {
      "title": "Room 459"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "276": [
    {
      "x": 15,
      "y": 5
    },
    {
      "n": 268,
      "s": 459,
      "w": 322
    },
    {
      "title": "Room 276"
    },
    {
      "description": "There are exits to the north south west "
    },
  ],
  "268": [
    {
      "x": 15,
      "y": 6
    },
    {
      "n": 265,
      "s": 276
    },
    {
      "title": "Room 268"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "265": [
    {
      "x": 15,
      "y": 7
    },
    {
      "n": 232,
      "s": 268,
      "e": 273
    },
    {
      "title": "Room 265"
    },
    {
      "description": "There are exits to the north south east "
    },
  ],
  "232": [
    {
      "x": 15,
      "y": 8
    },
    {
      "n": 206,
      "s": 265,
      "w": 244
    },
    {
      "title": "Room 232"
    },
    {
      "description": "There are exits to the north south west "
    },

  ],
  "206": [
    {
      "x": 15,
      "y": 9
    },
    {
      "n": 201,
      "s": 232
    },
    {
      "title": "Room 206"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "201": [
    {
      "x": 15,
      "y": 10
    },
    {
      "s": 206,
      "w": 179
    },
    {
      "title": "Room 201"
    },
    {
      "description": "There are exits to the south west "
    },
  ],
  "159": [
    {
      "x": 15,
      "y": 11
    },
    {
      "n": 116
    },
    {
      "title": "Room 159"
    },
    {
      "description": "There are exits to the north "
    },
  ],
  "116": [
    {
      "x": 15,
      "y": 12
    },
    {
      "n": 70,
      "s": 159
    },
    {
      "title": "Room 116"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "70": [
    {
      "x": 15,
      "y": 13
    },
    {
      "s": 116,
      "e": 87,
      "w": 50
    },
    {
      "title": "Room 70"
    },
    {
      "description": "There are exits to the south east west "
    },

  ],
  "38": [
    {
      "x": 15,
      "y": 14
    },
    {
      "n": 10
    },
    {
      "title": "Room 38"
    },
    {
      "description": "There are exits to the north "
    },

  ],
  "10": [
    {
      "x": 15,
      "y": 15
    },
    {
      "s": 38,
      "w": 2
    },
    {
      "title": "Room 10"
    },
    {
      "description": "There are exits to the south west "
    },

  ],
  "22": [
    {
      "x": 15,
      "y": 16
    },
    {
      "w": 1
    },
    {
      "title": "Room 22"
    },
    {
      "description": "There are exits to the west "
    },

  ],
  "12": [
    {
      "x": 15,
      "y": 17
    },
    {
      "n": 20,
      "e": 18,
      "w": 7
    },
    {
      "title": "Room 12"
    },
    {
      "description": "There are exits to the north east west "
    },

  ],
  "20": [
    {
      "x": 15,
      "y": 18
    },
    {
      "n": 31,
      "s": 12,
      "e": 26
    },
    {
      "title": "Room 20"
    },
    {
      "description": "There are exits to the north south east "
    },
  ],
  "31": [
    {
      "x": 15,
      "y": 19
    },
    {
      "n": 37,
      "s": 20
    },
    {
      "title": "Room 31"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "37": [
    {
      "x": 15,
      "y": 20
    },
    {
      "n": 91,
      "s": 31,
      "e": 42
    },
    {
      "title": "Room 37"
    },
    {
      "description": "There are exits to the north south east "
    },
  ],
  "91": [
    {
      "x": 15,
      "y": 21
    },
    {
      "n": 101,
      "s": 37
    },
    {
      "title": "Room 91"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "101": [
    {
      "x": 15,
      "y": 22
    },
    {
      "s": 91
    },
    {
      "title": "Room 101"
    },
    {
      "description": "There are exits to the south "
    },

  ],
  "114": [
    {
      "x": 15,
      "y": 23
    },
    {
      "e": 120,
      "w": 111
    },
    {
      "title": "Room 114"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "123": [
    {
      "x": 15,
      "y": 24
    },
    {
      "e": 138,
      "w": 121
    },
    {
      "title": "Room 123"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "178": [
    {
      "x": 15,
      "y": 25
    },
    {
      "w": 148
    },
    {
      "title": "Room 178"
    },
    {
      "description": "There are exits to the west "
    },

  ],
  "228": [
    {
      "x": 15,
      "y": 26
    },
    {
      "n": 253,
      "w": 163
    },
    {
      "title": "Room 228"
    },
    {
      "description": "There are exits to the north west "
    },

  ],
  "253": [
    {
      "x": 15,
      "y": 27
    },
    {
      "n": 285,
      "s": 228
    },
    {
      "title": "Room 253"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "285": [
    {
      "x": 15,
      "y": 28
    },
    {
      "s": 253
    },
    {
      "title": "Room 285"
    },
    {
      "description": "There are exits to the south "
    },
  ],
  "354": [
    {
      "x": 15,
      "y": 29
    },
    {
      "n": 361,
      "e": 321,
      "w": 386
    },
    {
      "title": "Room 354"
    },
    {
      "description": "There are exits to the north east west "
    },
  ],
  "361": [
    {
      "x": 15,
      "y": 30
    },
    {
      "s": 354,
      "w": 366
    },
    {
      "title": "Room 361"
    },
    {
      "description": "There are exits to the south west "
    },
  ],
  "455": [
    {
      "x": 16,
      "y": 4
    },
    {
      "n": 382
    },
    {
      "title": "Room 455"
    },
    {
      "description": "There are exits to the north "
    },
  ],
  "382": [
    {
      "x": 16,
      "y": 5
    },
    {
      "n": 296,
      "s": 455
    },
    {
      "title": "Room 382"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "296": [
    {
      "x": 16,
      "y": 6
    },
    {
      "n": 273,
      "s": 382,
      "e": 308
    },
    {
      "title": "Room 296"
    },
    {
      "description": "There are exits to the north south east "
    },
  ],
  "273": [
    {
      "x": 16,
      "y": 7
    },
    {
      "s": 296,
      "e": 298,
      "w": 265
    },
    {
      "title": "Room 273"
    },
    {
      "description": "There are exits to the south east west "
    },

  ],
  "237": [
    {
      "x": 16,
      "y": 8
    },
    {
      "n": 229,
      "e": 370
    },
    {
      "title": "Room 237"
    },
    {
      "description": "There are exits to the north east "
    },
  ],
  "229": [
    {
      "x": 16,
      "y": 9
    },
    {
      "n": 212,
      "s": 237
    },
    {
      "title": "Room 229"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "212": [
    {
      "x": 16,
      "y": 10
    },
    {
      "n": 127,
      "s": 229
    },
    {
      "title": "Room 212"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "127": [
    {
      "x": 16,
      "y": 11
    },
    {
      "n": 117,
      "s": 212,
      "e": 173
    },
    {
      "title": "Room 127"
    },
    {
      "description": "There are exits to the north south east "
    },

  ],
  "117": [
    {
      "x": 16,
      "y": 12
    },
    {
      "n": 87,
      "s": 127,
      "e": 170
    },
    {
      "title": "Room 117"
    },
    {
      "description": "There are exits to the north south east "
    },
  ],
  "87": [
    {
      "x": 16,
      "y": 13
    },
    {
      "s": 117,
      "w": 70
    },
    {
      "title": "Room 87"
    },
    {
      "description": "There are exits to the south west "
    },
  ],
  "54": [
    {
      "x": 16,
      "y": 14
    },
    {
      "n": 29
    },
    {
      "title": "Room 54"
    },
    {
      "description": "There are exits to the north "
    },
  ],
  "29": [
    {
      "x": 16,
      "y": 15
    },
    {
      "n": 24,
      "s": 54
    },
    {
      "title": "Room 29"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "24": [
    {
      "x": 16,
      "y": 16
    },
    {
      "n": 18,
      "s": 29,
      "e": 25
    },
    {
      "title": "Room 24"
    },
    {
      "description": "There are exits to the north south east "
    },
  ],
  "18": [
    {
      "x": 16,
      "y": 17
    },
    {
      "s": 24,
      "e": 34,
      "w": 12
    },
    {
      "title": "Room 18"
    },
    {
      "description": "There are exits to the south east west "
    },

  ],
  "26": [
    {
      "x": 16,
      "y": 18
    },
    {
      "n": 27,
      "w": 20
    },
    {
      "title": "Room 26"
    },
    {
      "description": "There are exits to the north west "
    },

  ],
  "27": [
    {
      "x": 16,
      "y": 19
    },
    {
      "s": 26,
      "e": 55
    },
    {
      "title": "Room 27"
    },
    {
      "description": "There are exits to the south east "
    },
  ],
  "42": [
    {
      "x": 16,
      "y": 20
    },
    {
      "n": 51,
      "w": 37
    },
    {
      "title": "Room 42"
    },
    {
      "description": "There are exits to the north west "
    },

  ],
  "51": [
    {
      "x": 16,
      "y": 21
    },
    {
      "n": 93,
      "s": 42
    },
    {
      "title": "Room 51"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "93": [
    {
      "x": 16,
      "y": 22
    },
    {
      "s": 51
    },
    {
      "title": "Room 93"
    },
    {
      "description": "There are exits to the south "
    },

  ],
  "120": [
    {
      "x": 16,
      "y": 23
    },
    {
      "w": 114
    },
    {
      "title": "Room 120"
    },
    {
      "description": "There are exits to the west "
    },
  ],
  "138": [
    {
      "x": 16,
      "y": 24
    },
    {
      "n": 143,
      "e": 139,
      "w": 123
    },
    {
      "title": "Room 138"
    },
    {
      "description": "There are exits to the north east west "
    },

  ],
  "143": [
    {
      "x": 16,
      "y": 25
    },
    {
      "s": 138
    },
    {
      "title": "Room 143"
    },
    {
      "description": "There are exits to the south "
    },

  ],
  "233": [
    {
      "x": 16,
      "y": 26
    },
    {
      "n": 240,
      "e": 152
    },
    {
      "title": "Room 233"
    },
    {
      "description": "There are exits to the north east "
    },

  ],
  "240": [
    {
      "x": 16,
      "y": 27
    },
    {
      "n": 304,
      "s": 233
    },
    {
      "title": "Room 240"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "304": [
    {
      "x": 16,
      "y": 28
    },
    {
      "n": 321,
      "s": 240
    },
    {
      "title": "Room 304"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "321": [
    {
      "x": 16,
      "y": 29
    },
    {
      "n": 334,
      "s": 304,
      "w": 354
    },
    {
      "title": "Room 321"
    },
    {
      "description": "There are exits to the north south west "
    },
  ],
  "334": [
    {
      "x": 16,
      "y": 30
    },
    {
      "s": 321,
      "e": 384
    },
    {
      "title": "Room 334"
    },
    {
      "description": "There are exits to the south east "
    },
  ],
  "416": [
    {
      "x": 17,
      "y": 4
    },
    {
      "n": 317
    },
    {
      "title": "Room 416"
    },
    {
      "description": "There are exits to the north "
    },
  ],
  "317": [
    {
      "x": 17,
      "y": 5
    },
    {
      "n": 308,
      "s": 416
    },
    {
      "title": "Room 317"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "308": [
    {
      "x": 17,
      "y": 6
    },
    {
      "s": 317,
      "e": 337,
      "w": 296
    },
    {
      "title": "Room 308"
    },
    {
      "description": "There are exits to the south east west "
    },

  ],
  "298": [
    {
      "x": 17,
      "y": 7
    },
    {
      "e": 360,
      "w": 273
    },
    {
      "title": "Room 298"
    },
    {
      "description": "There are exits to the east west "
    },
  ],
  "370": [
    {
      "x": 17,
      "y": 8
    },
    {
      "w": 237
    },
    {
      "title": "Room 370"
    },
    {
      "description": "There are exits to the west "
    },
  ],
  "267": [
    {
      "x": 17,
      "y": 9
    },
    {
      "n": 202,
      "e": 302
    },
    {
      "title": "Room 267"
    },
    {
      "description": "There are exits to the north east "
    },
  ],
  "202": [
    {
      "x": 17,
      "y": 10
    },
    {
      "n": 173,
      "s": 267,
      "e": 249
    },
    {
      "title": "Room 202"
    },
    {
      "description": "There are exits to the north south east "
    },

  ],
  "173": [
    {
      "x": 17,
      "y": 11
    },
    {
      "s": 202,
      "w": 127
    },
    {
      "title": "Room 173"
    },
    {
      "description": "There are exits to the south west "
    },
  ],
  "170": [
    {
      "x": 17,
      "y": 12
    },
    {
      "n": 182,
      "w": 117
    },
    {
      "title": "Room 170"
    },
    {
      "description": "There are exits to the north west "
    },
  ],
  "182": [
    {
      "x": 17,
      "y": 13
    },
    {
      "s": 170,
      "e": 211
    },
    {
      "title": "Room 182"
    },
    {
      "description": "There are exits to the south east "
    },
  ],
  "77": [
    {
      "x": 17,
      "y": 14
    },
    {
      "n": 43,
      "e": 130
    },
    {
      "title": "Room 77"
    },
    {
      "description": "There are exits to the north east "
    },

  ],
  "43": [
    {
      "x": 17,
      "y": 15
    },
    {
      "n": 25,
      "s": 77,
      "e": 49
    },
    {
      "title": "Room 43"
    },
    {
      "description": "There are exits to the north south east "
    },
  ],
  "25": [
    {
      "x": 17,
      "y": 16
    },
    {
      "s": 43,
      "w": 24
    },
    {
      "title": "Room 25"
    },
    {
      "description": "There are exits to the south west "
    },
  ],
  "34": [
    {
      "x": 17,
      "y": 17
    },
    {
      "n": 35,
      "e": 39,
      "w": 18
    },
    {
      "title": "Room 34"
    },
    {
      "description": "There are exits to the north east west "
    },
  ],
  "35": [
    {
      "x": 17,
      "y": 18
    },
    {
      "s": 34,
      "e": 44
    },
    {
      "title": "Room 35"
    },
    {
      "description": "There are exits to the south east "
    },
  ],
  "55": [
    {
      "x": 17,
      "y": 19
    },
    {
      "n": 56,
      "w": 27
    },
    {
      "title": "Room 55"
    },
    {
      "description": "There are exits to the north west "
    },

  ],
  "56": [
    {
      "x": 17,
      "y": 20
    },
    {
      "n": 73,
      "s": 55,
      "e": 67
    },
    {
      "title": "Room 56"
    },
    {
      "description": "There are exits to the north south east "
    },
  ],
  "73": [
    {
      "x": 17,
      "y": 21
    },
    {
      "n": 132,
      "s": 56
    },
    {
      "title": "Room 73"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "132": [
    {
      "x": 17,
      "y": 22
    },
    {
      "n": 172,
      "s": 73
    },
    {
      "title": "Room 132"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "172": [
    {
      "x": 17,
      "y": 23
    },
    {
      "s": 132
    },
    {
      "title": "Room 172"
    },
    {
      "description": "There are exits to the south "
    },

  ],
  "139": [
    {
      "x": 17,
      "y": 24
    },
    {
      "n": 147,
      "e": 176,
      "w": 138
    },
    {
      "title": "Room 139"
    },
    {
      "description": "There are exits to the north east west "
    },

  ],
  "147": [
    {
      "x": 17,
      "y": 25
    },
    {
      "n": 152,
      "s": 139,
      "e": 154
    },
    {
      "title": "Room 147"
    },
    {
      "description": "There are exits to the north south east "
    },

  ],
  "152": [
    {
      "x": 17,
      "y": 26
    },
    {
      "n": 196,
      "s": 147,
      "w": 233
    },
    {
      "title": "Room 152"
    },
    {
      "description": "There are exits to the north south west "
    },
  ],
  "196": [
    {
      "x": 17,
      "y": 27
    },
    {
      "n": 278,
      "s": 152,
      "e": 224
    },
    {
      "title": "Room 196"
    },
    {
      "description": "There are exits to the north south east "
    },
  ],
  "278": [
    {
      "x": 17,
      "y": 28
    },
    {
      "n": 338,
      "s": 196
    },
    {
      "title": "Room 278"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "338": [
    {
      "x": 17,
      "y": 29
    },
    {
      "s": 278
    },
    {
      "title": "Room 338"
    },
    {
      "description": "There are exits to the south "
    },

  ],
  "384": [
    {
      "x": 17,
      "y": 30
    },
    {
      "e": 435,
      "w": 334
    },
    {
      "title": "Room 384"
    },
    {
      "description": "There are exits to the east west "
    },
  ],
  "460": [
    {
      "x": 18,
      "y": 4
    },
    {
      "n": 383
    },
    {
      "title": "Room 460"
    },
    {
      "description": "There are exits to the north "
    },

  ],
  "383": [
    {
      "x": 18,
      "y": 5
    },
    {
      "n": 337,
      "s": 460
    },
    {
      "title": "Room 383"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "337": [
    {
      "x": 18,
      "y": 6
    },
    {
      "s": 383,
      "w": 308
    },
    {
      "title": "Room 337"
    },
    {
      "description": "There are exits to the south west "
    },

  ],
  "360": [
    {
      "x": 18,
      "y": 7
    },
    {
      "n": 364,
      "w": 298
    },
    {
      "title": "Room 360"
    },
    {
      "description": "There are exits to the north west "
    },

  ],
  "364": [
    {
      "x": 18,
      "y": 8
    },
    {
      "s": 360,
      "e": 401
    },
    {
      "title": "Room 364"
    },
    {
      "description": "There are exits to the south east "
    },
  ],
  "302": [
    {
      "x": 18,
      "y": 9
    },
    {
      "e": 402,
      "w": 267
    },
    {
      "title": "Room 302"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "249": [
    {
      "x": 18,
      "y": 10
    },
    {
      "w": 202
    },
    {
      "title": "Room 249"
    },
    {
      "description": "There are exits to the west "
    },

  ],
  "272": [
    {
      "x": 18,
      "y": 11
    },
    {
      "n": 248
    },
    {
      "title": "Room 272"
    },
    {
      "description": "There are exits to the north "
    },

  ],
  "248": [
    {
      "x": 18,
      "y": 12
    },
    {
      "n": 211,
      "s": 272
    },
    {
      "title": "Room 248"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "211": [
    {
      "x": 18,
      "y": 13
    },
    {
      "s": 248,
      "w": 182
    },
    {
      "title": "Room 211"
    },
    {
      "description": "There are exits to the south west "
    },

  ],
  "130": [
    {
      "x": 18,
      "y": 14
    },
    {
      "w": 77
    },
    {
      "title": "Room 130"
    },
    {
      "description": "There are exits to the west "
    },

  ],
  "49": [
    {
      "x": 18,
      "y": 15
    },
    {
      "e": 119,
      "w": 43
    },
    {
      "title": "Room 49"
    },
    {
      "description": "There are exits to the east west "
    },
  ],
  "52": [
    {
      "x": 18,
      "y": 16
    },
    {
      "n": 39
    },
    {
      "title": "Room 52"
    },
    {
      "description": "There are exits to the north "
    },
  ],
  "39": [
    {
      "x": 18,
      "y": 17
    },
    {
      "s": 52,
      "e": 71,
      "w": 34
    },
    {
      "title": "Room 39"
    },
    {
      "description": "There are exits to the south east west "
    },

  ],
  "44": [
    {
      "x": 18,
      "y": 18
    },
    {
      "n": 48,
      "e": 59,
      "w": 35
    },
    {
      "title": "Room 44"
    },
    {
      "description": "There are exits to the north east west "
    },

  ],
  "48": [
    {
      "x": 18,
      "y": 19
    },
    {
      "s": 44,
      "e": 53
    },
    {
      "title": "Room 48"
    },
    {
      "description": "There are exits to the south east "
    },
  ],
  "67": [
    {
      "x": 18,
      "y": 20
    },
    {
      "n": 84,
      "w": 56
    },
    {
      "title": "Room 67"
    },
    {
      "description": "There are exits to the north west "
    },

  ],
  "84": [
    {
      "x": 18,
      "y": 21
    },
    {
      "n": 86,
      "s": 67
    },
    {
      "title": "Room 84"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "86": [
    {
      "x": 18,
      "y": 22
    },
    {
      "n": 146,
      "s": 84,
      "e": 95
    },
    {
      "title": "Room 86"
    },
    {
      "description": "There are exits to the north south east "
    },

  ],
  "146": [
    {
      "x": 18,
      "y": 23
    },
    {
      "s": 86
    },
    {
      "title": "Room 146"
    },
    {
      "description": "There are exits to the south "
    },
  ],
  "176": [
    {
      "x": 18,
      "y": 24
    },
    {
      "w": 139
    },
    {
      "title": "Room 176"
    },
    {
      "description": "There are exits to the west "
    },

  ],
  "154": [
    {
      "x": 18,
      "y": 25
    },
    {
      "n": 192,
      "e": 184,
      "w": 147
    },
    {
      "title": "Room 154"
    },
    {
      "description": "There are exits to the north east west "
    },

  ],
  "192": [
    {
      "x": 18,
      "y": 26
    },
    {
      "s": 154,
      "e": 239
    },
    {
      "title": "Room 192"
    },
    {
      "description": "There are exits to the south east "
    },

  ],
  "224": [
    {
      "x": 18,
      "y": 27
    },
    {
      "n": 287,
      "w": 196
    },
    {
      "title": "Room 224"
    },
    {
      "description": "There are exits to the north west "
    },
  ],
  "287": [
    {
      "x": 18,
      "y": 28
    },
    {
      "n": 313,
      "s": 224,
      "e": 353
    },
    {
      "title": "Room 287"
    },
    {
      "description": "There are exits to the north south east "
    },
  ],
  "313": [
    {
      "x": 18,
      "y": 29
    },
    {
      "s": 287
    },
    {
      "title": "Room 313"
    },
    {
      "description": "There are exits to the south "
    },
  ],
  "435": [
    {
      "x": 18,
      "y": 30
    },
    {
      "w": 384
    },
    {
      "title": "Room 435"
    },
    {
      "description": "There are exits to the west "
    },

  ],
  "464": [
    {
      "x": 19,
      "y": 6
    },
    {
      "n": 420
    },
    {
      "title": "Room 464"
    },
    {
      "description": "There are exits to the north "
    },

  ],
  "420": [
    {
      "x": 19,
      "y": 7
    },
    {
      "n": 401,
      "s": 464
    },
    {
      "title": "Room 420"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "401": [
    {
      "x": 19,
      "y": 8
    },
    {
      "s": 420,
      "e": 427,
      "w": 364
    },
    {
      "title": "Room 401"
    },
    {
      "description": "There are exits to the south east west "
    },

  ],
  "402": [
    {
      "x": 19,
      "y": 9
    },
    {
      "e": 403,
      "w": 302
    },
    {
      "title": "Room 402"
    },
    {
      "description": "There are exits to the east west "
    },
  ],
  "371": [
    {
      "x": 19,
      "y": 10
    },
    {
      "n": 309,
      "e": 430
    },
    {
      "title": "Room 371"
    },
    {
      "description": "There are exits to the north east "
    },
  ],
  "309": [
    {
      "x": 19,
      "y": 11
    },
    {
      "n": 286,
      "s": 371,
      "e": 377
    },
    {
      "title": "Room 309"
    },
    {
      "description": "There are exits to the north south east "
    },
  ],
  "286": [
    {
      "x": 19,
      "y": 12
    },
    {
      "n": 242,
      "s": 309,
      "e": 288
    },
    {
      "title": "Room 286"
    },
    {
      "description": "There are exits to the north south east "
    },

  ],
  "242": [
    {
      "x": 19,
      "y": 13
    },
    {
      "n": 219,
      "s": 286
    },
    {
      "title": "Room 242"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "219": [
    {
      "x": 19,
      "y": 14
    },
    {
      "n": 119,
      "s": 242,
      "e": 305
    },
    {
      "title": "Room 219"
    },
    {
      "description": "There are exits to the north south east "
    },

  ],
  "119": [
    {
      "x": 19,
      "y": 15
    },
    {
      "s": 219,
      "e": 131,
      "w": 49
    },
    {
      "title": "Room 119"
    },
    {
      "description": "There are exits to the south east west "
    },
  ],
  "115": [
    {
      "x": 19,
      "y": 16
    },
    {
      "n": 71,
      "e": 160
    },
    {
      "title": "Room 115"
    },
    {
      "description": "There are exits to the north east "
    },
  ],
  "71": [
    {
      "x": 19,
      "y": 17
    },
    {
      "s": 115,
      "e": 150,
      "w": 39
    },
    {
      "title": "Room 71"
    },
    {
      "description": "There are exits to the south east west "
    },

  ],
  "59": [
    {
      "x": 19,
      "y": 18
    },
    {
      "e": 189,
      "w": 44
    },
    {
      "title": "Room 59"
    },
    {
      "description": "There are exits to the east west "
    },
  ],
  "53": [
    {
      "x": 19,
      "y": 19
    },
    {
      "n": 75,
      "w": 48
    },
    {
      "title": "Room 53"
    },
    {
      "description": "There are exits to the north west "
    },

  ],
  "75": [
    {
      "x": 19,
      "y": 20
    },
    {
      "n": 78,
      "s": 53,
      "e": 88
    },
    {
      "title": "Room 75"
    },
    {
      "description": "There are exits to the north south east "
    },
  ],
  "78": [
    {
      "x": 19,
      "y": 21
    },
    {
      "s": 75,
      "e": 90
    },
    {
      "title": "Room 78"
    },
    {
      "description": "There are exits to the south east "
    },

  ],
  "95": [
    {
      "x": 19,
      "y": 22
    },
    {
      "n": 109,
      "w": 86
    },
    {
      "title": "Room 95"
    },
    {
      "description": "There are exits to the north west "
    },

  ],
  "109": [
    {
      "x": 19,
      "y": 23
    },
    {
      "n": 136,
      "s": 95
    },
    {
      "title": "Room 109"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "136": [
    {
      "x": 19,
      "y": 24
    },
    {
      "s": 109,
      "e": 231
    },
    {
      "title": "Room 136"
    },
    {
      "description": "There are exits to the south east "
    },

  ],
  "184": [
    {
      "x": 19,
      "y": 25
    },
    {
      "w": 154
    },
    {
      "title": "Room 184"
    },
    {
      "description": "There are exits to the west "
    },
  ],
  "239": [
    {
      "x": 19,
      "y": 26
    },
    {
      "n": 255,
      "e": 336,
      "w": 192
    },
    {
      "title": "Room 239"
    },
    {
      "description": "There are exits to the north east west "
    },

  ],
  "255": [
    {
      "x": 19,
      "y": 27
    },
    {
      "s": 239
    },
    {
      "title": "Room 255"
    },
    {
      "description": "There are exits to the south "
    },
  ],
  "353": [
    {
      "x": 19,
      "y": 28
    },
    {
      "n": 380,
      "w": 287
    },
    {
      "title": "Room 353"
    },
    {
      "description": "There are exits to the north west "
    },
  ],
  "380": [
    {
      "x": 19,
      "y": 29
    },
    {
      "n": 476,
      "s": 353,
      "e": 445
    },
    {
      "title": "Room 380"
    },
    {
      "description": "There are exits to the north south east "
    },

  ],
  "476": [
    {
      "x": 19,
      "y": 30
    },
    {
      "s": 380
    },
    {
      "title": "Room 476"
    },
    {
      "description": "There are exits to the south "
    },

  ],
  "496": [
    {
      "x": 20,
      "y": 4
    },
    {
      "n": 475
    },
    {
      "title": "Room 496"
    },
    {
      "description": "There are exits to the north "
    },

  ],
  "475": [
    {
      "x": 20,
      "y": 5
    },
    {
      "n": 448,
      "s": 496
    },
    {
      "title": "Room 475"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "448": [
    {
      "x": 20,
      "y": 6
    },
    {
      "n": 438,
      "s": 475,
      "e": 490
    },
    {
      "title": "Room 448"
    },
    {
      "description": "There are exits to the north south east "
    },

  ],
  "438": [
    {
      "x": 20,
      "y": 7
    },
    {
      "n": 427,
      "s": 448
    },
    {
      "title": "Room 438"
    },
    {
      "description": "There are exits to the north south "
    },

  ],
  "427": [
    {
      "x": 20,
      "y": 8
    },
    {
      "s": 438,
      "e": 474,
      "w": 401
    },
    {
      "title": "Room 427"
    },
    {
      "description": "There are exits to the south east west "
    },
  ],
  "403": [
    {
      "x": 20,
      "y": 9
    },
    {
      "e": 439,
      "w": 402
    },
    {
      "title": "Room 403"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "430": [
    {
      "x": 20,
      "y": 10
    },
    {
      "e": 440,
      "w": 371
    },
    {
      "title": "Room 430"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "377": [
    {
      "x": 20,
      "y": 11
    },
    {
      "e": 456,
      "w": 309
    },
    {
      "title": "Room 377"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "288": [
    {
      "x": 20,
      "y": 12
    },
    {
      "n": 326,
      "e": 498,
      "w": 286
    },
    {
      "title": "Room 288"
    },
    {
      "description": "There are exits to the north east west "
    },
  ],
  "326": [
    {
      "x": 20,
      "y": 13
    },
    {
      "s": 288
    },
    {
      "title": "Room 326"
    },
    {
      "description": "There are exits to the south "
    },
  ],
  "305": [
    {
      "x": 20,
      "y": 14
    },
    {
      "e": 330,
      "w": 219
    },
    {
      "title": "Room 305"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "131": [
    {
      "x": 20,
      "y": 15
    },
    {
      "e": 329,
      "w": 119
    },
    {
      "title": "Room 131"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "160": [
    {
      "x": 20,
      "y": 16
    },
    {
      "e": 214,
      "w": 115
    },
    {
      "title": "Room 160"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "150": [
    {
      "x": 20,
      "y": 17
    },
    {
      "e": 251,
      "w": 71
    },
    {
      "title": "Room 150"
    },
    {
      "description": "There are exits to the east west "
    },
  ],
  "189": [
    {
      "x": 20,
      "y": 18
    },
    {
      "e": 275,
      "w": 59
    },
    {
      "title": "Room 189"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "103": [
    {
      "x": 20,
      "y": 19
    },
    {
      "n": 88
    },
    {
      "title": "Room 103"
    },
    {
      "description": "There are exits to the north "
    },
  ],
  "88": [
    {
      "x": 20,
      "y": 20
    },
    {
      "s": 103,
      "e": 125,
      "w": 75
    },
    {
      "title": "Room 88"
    },
    {
      "description": "There are exits to the south east west "
    },
    {
      "items": []
    }
  ],
  "90": [
    {
      "x": 20,
      "y": 21
    },
    {
      "n": 98,
      "e": 142,
      "w": 78
    },
    {
      "title": "Room 90"
    },
    {
      "description": "There are exits to the north east west "
    },
    {
      "items": []
    }
  ],
  "98": [
    {
      "x": 20,
      "y": 22
    },
    {
      "n": 186,
      "s": 90
    },
    {
      "title": "Room 98"
    },
    {
      "description": "There are exits to the north south "
    },
  ],
  "186": [
    {
      "x": 20,
      "y": 23
    },
    {
      "s": 98,
      "e": 262
    },
    {
      "title": "Room 186"
    },
    {
      "description": "There are exits to the south east "
    },
    {
      "items": []
    }
  ],
  "231": [
    {
      "x": 20,
      "y": 24
    },
    {
      "n": 282,
      "e": 294,
      "w": 136
    },
    {
      "title": "Room 231"
    },
    {
      "description": "There are exits to the north east west "
    },
    {
      "items": []
    }
  ],
  "282": [
    {
      "x": 20,
      "y": 25
    },
    {
      "s": 231
    },
    {
      "title": "Room 282"
    },
    {
      "description": "There are exits to the south "
    },

  ],
  "336": [
    {
      "x": 20,
      "y": 26
    },
    {
      "n": 373,
      "e": 421,
      "w": 239
    },
    {
      "title": "Room 336"
    },
    {
      "description": "There are exits to the north east west "
    },

  ],
  "373": [
    {
      "x": 20,
      "y": 27
    },
    {
      "s": 336
    },
    {
      "title": "Room 373"
    },
    {
      "description": "There are exits to the south "
    },
  ],
  "480": [
    {
      "x": 20,
      "y": 28
    },
    {
      "n": 445
    },
    {
      "title": "Room 480"
    },
    {
      "description": "There are exits to the north "
    },

  ],
  "445": [
    {
      "x": 20,
      "y": 29
    },
    {
      "s": 480,
      "e": 446,
      "w": 380
    },
    {
      "title": "Room 445"
    },
    {
      "description": "There are exits to the south east west "
    },
  ],
  "490": [
    {
      "x": 21,
      "y": 6
    },
    {
      "w": 448
    },
    {
      "title": "Room 490"
    },
    {
      "description": "There are exits to the west "
    },
  ],
  "474": [
    {
      "x": 21,
      "y": 8
    },
    {
      "w": 427
    },
    {
      "title": "Room 474"
    },
    {
      "description": "There are exits to the west "
    },
  ],
  "439": [
    {
      "x": 21,
      "y": 9
    },
    {
      "w": 403
    },
    {
      "title": "Room 439"
    },
    {
      "description": "There are exits to the west "
    },
  ],
  "440": [
    {
      "x": 21,
      "y": 10
    },
    {
      "w": 430
    },
    {
      "title": "Room 440"
    },
    {
      "description": "There are exits to the west "
    },
  ],
  "456": [
    {
      "x": 21,
      "y": 11
    },
    {
      "w": 377
    },
    {
      "title": "Room 456"
    },
    {
      "description": "There are exits to the west "
    },
  ],
  "498": [
    {
      "x": 21,
      "y": 12
    },
    {
      "w": 288
    },
    {
      "title": "Room 498"
    },
    {
      "description": "There are exits to the west "
    },
  ],
  "348": [
    {
      "x": 21,
      "y": 13
    },
    {
      "n": 330
    },
    {
      "title": "Room 348"
    },
    {
      "description": "There are exits to the north "
    },

  ],
  "330": [
    {
      "x": 21,
      "y": 14
    },
    {
      "s": 348,
      "e": 454,
      "w": 305
    },
    {
      "title": "Room 330"
    },
    {
      "description": "There are exits to the south east west "
    },
  ],
  "329": [
    {
      "x": 21,
      "y": 15
    },
    {
      "e": 407,
      "w": 131
    },
    {
      "title": "Room 329"
    },
    {
      "description": "There are exits to the east west "
    },
    {
      "items": []
    }
  ],
  "214": [
    {
      "x": 21,
      "y": 16
    },
    {
      "e": 246,
      "w": 160
    },
    {
      "title": "Room 214"
    },
    {
      "description": "There are exits to the east west "
    },
    {
      "items": []
    }
  ],
  "251": [
    {
      "x": 21,
      "y": 17
    },
    {
      "w": 150
    },
    {
      "title": "Room 251"
    },
    {
      "description": "There are exits to the west "
    },
  ],
  "275": [
    {
      "x": 21,
      "y": 18
    },
    {
      "e": 283,
      "w": 189
    },
    {
      "title": "Room 275"
    },
    {
      "description": "There are exits to the east west "
    },
    {
      "items": []
    }
  ],
  "198": [
    {
      "x": 21,
      "y": 19
    },
    {
      "n": 125,
      "e": 270
    },
    {
      "title": "Room 198"
    },
    {
      "description": "There are exits to the north east "
    },
    {
      "items": []
    }
  ],
  "125": [
    {
      "x": 21,
      "y": 20
    },
    {
      "s": 198,
      "e": 238,
      "w": 88
    },
    {
      "title": "Room 125"
    },
    {
      "description": "There are exits to the south east west "
    },
  ],
  "142": [
    {
      "x": 21,
      "y": 21
    },
    {
      "n": 245,
      "w": 90
    },
    {
      "title": "Room 142"
    },
    {
      "description": "There are exits to the north west "
    },
  ],
  "245": [
    {
      "x": 21,
      "y": 22
    },
    {
      "s": 142,
      "e": 343
    },
    {
      "title": "Room 245"
    },
    {
      "description": "There are exits to the south east "
    },
    {
      "items": []
    }
  ],
  "262": [
    {
      "x": 21,
      "y": 23
    },
    {
      "e": 390,
      "w": 186
    },
    {
      "title": "Room 262"
    },
    {
      "description": "There are exits to the east west "
    },

  ],
  "294": [
    {
      "x": 21,
      "y": 24
    },
    {
      "n": 363,
      "e": 311,
      "w": 231
    },
    {
      "title": "Room 294"
    },
    {
      "description": "There are exits to the north east west "
    },
  ],
  "363": [
    {
      "x": 21,
      "y": 25
    },
    {
      "s": 294
    },
    {
      "title": "Room 363"
    },
    {
      "description": "There are exits to the south "
    },

  ],
  "421": [
    {
      "x": 21,
      "y": 26
    },
    {
      "w": 336
    },
    {
      "title": "Room 421"
    },
    {
      "description": "There are exits to the west "
    },

  ],
  "446": [
    {
      "x": 21,
      "y": 29
    },
    {
      "w": 445
    },
    {
      "title": "Room 446"
    },
    {
      "description": "There are exits to the west "
    },

  ],
  "454": [
    {
      "x": 22,
      "y": 14
    },
    {
      "w": 330
    },
    {
      "title": "Room 454"
    },
    {
      "description": "There are exits to the west "
    },

  ],
  "407": [
    {
      "x": 22,
      "y": 15
    },
    {
      "w": 329
    },
    {
      "title": "Room 407"
    },
    {
      "description": "There are exits to the west "
    },
  ],
  "246": [
    {
      "x": 22,
      "y": 16
    },
    {
      "n": 325,
      "e": 412,
      "w": 214
    },
    {
      "title": "Room 246"
    },
    {
      "description": "There are exits to the north east west "
    },
    {
      "items": []
    }
  ],
  "325": [
    {
      "x": 22,
      "y": 17
    },
    {
      "s": 246
    },
    {
      "title": "Room 325"
    },
    {
      "description": "There are exits to the south "
    },
    {
      "items": []
    }
  ],
  "283": [
    {
      "x": 22,
      "y": 18
    },
    {
      "e": 376,
      "w": 275
    },
    {
      "title": "Room 283"
    },
    {
      "description": "There are exits to the east west "
    },
  ],
  "270": [
    {
      "x": 22,
      "y": 19
    },
    {
      "e": 300,
      "w": 198
    },
    {
      "title": "Room 270"
    },
    {
      "description": "There are exits to the east west "
    },
    {
      "items": []
    }
  ],
  "238": [
    {
      "x": 22,
      "y": 20
    },
    {
      "n": 381,
      "e": 293,
      "w": 125
    },
    {
      "title": "Room 238"
    },
    {
      "description": "There are exits to the north east west "
    },
  ],
  "381": [
    {
      "x": 22,
      "y": 21
    },
    {
      "s": 238,
      "e": 431
    },
    {
      "title": "Room 381"
    },
    {
      "description": "There are exits to the south east "
    },
  ],
  "343": [
    {
      "x": 22,
      "y": 22
    },
    {
      "w": 245
    },
    {
      "title": "Room 343"
    },
    {
      "description": "There are exits to the west "
    },
    {
      "items": []
    }
  ],
  "390": [
    {
      "x": 22,
      "y": 23
    },
    {
      "e": 398,
      "w": 262
    },
    {
      "title": "Room 390"
    },
    {
      "description": "There are exits to the east west "
    },
    {
      "items": []
    }
  ],
  "311": [
    {
      "x": 22,
      "y": 24
    },
    {
      "n": 389,
      "e": 499,
      "w": 294
    },
    {
      "title": "Room 311"
    },
    {
      "description": "There are exits to the north east west "
    },
  ],
  "389": [
    {
      "x": 22,
      "y": 25
    },
    {
      "s": 311
    },
    {
      "title": "Room 389"
    },
    {
      "description": "There are exits to the south "
    },

  ],
  "412": [
    {
      "x": 23,
      "y": 16
    },
    {
      "w": 246
    },
    {
      "title": "Room 412"
    },
    {
      "description": "There are exits to the west "
    },
  ],
  "468": [
    {
      "x": 23,
      "y": 17
    },
    {
      "n": 376
    },
    {
      "title": "Room 468"
    },
    {
      "description": "There are exits to the north "
    },
  ],
  "376": [
    {
      "x": 23,
      "y": 18
    },
    {
      "s": 468,
      "w": 283
    },
    {
      "title": "Room 376"
    },
    {
      "description": "There are exits to the south west "
    },

  ],
  "300": [
    {
      "x": 23,
      "y": 19
    },
    {
      "e": 320,
      "w": 270
    },
    {
      "title": "Room 300"
    },
    {
      "description": "There are exits to the east west "
    },
  ],
  "293": [
    {
      "x": 23,
      "y": 20
    },
    {
      "w": 238
    },
    {
      "title": "Room 293"
    },
    {
      "description": "There are exits to the west "
    },
    {
      "items": []
    }
  ],
  "431": [
    {
      "x": 23,
      "y": 21
    },
    {
      "w": 381
    },
    {
      "title": "Room 431"
    },
    {
      "description": "There are exits to the west "
    },
  ],
  "487": [
    {
      "x": 23,
      "y": 22
    },
    {
      "n": 398
    },
    {
      "title": "Room 487"
    },
    {
      "description": "There are exits to the north "
    },
    {
      "items": []
    }
  ],
  "398": [
    {
      "x": 23,
      "y": 23
    },
    {
      "s": 487,
      "w": 390
    },
    {
      "title": "Room 398"
    },
    {
      "description": "There are exits to the south west "
    },
    {
      "items": []
    }
  ],
  "499": [
    {
      "x": 23,
      "y": 24
    },
    {
      "w": 311
    },
    {
      "title": "Room 499"
    },
    {
      "description": "There are exits to the west "
    },

  ],
  "471": [
    {
      "x": 24,
      "y": 18
    },
    {
      "n": 320
    },
    {
      "title": "Room 471"
    },
    {
      "description": "There are exits to the north "
    },
  ],
  "320": [
    {
      "x": 24,
      "y": 19
    },
    {
      "s": 471,
      "w": 300
    },
    {
      "title": "Room 320"
    },
    {
      "description": "There are exits to the south west "
    },
  ]
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
