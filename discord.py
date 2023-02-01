#--GitHub.com/░█▀▄▀█ █▀▀█ ░█▀▄▀█ ░█▀▀█ ░█──░█ ░█─── ░█▀▀▀█--
#--------─────░█░█░█ █▄▄▀ ░█░█░█ ░█▄▄▀ ─░█░█─ ░█─── ─▀▀▀▄▄--
#---────---──-░█──░█ ▀─▀▀ ░█──░█ ░█─░█ ──▀▄▀─ ░█▄▄█ ░█▄▄▄█--
#--──-----──---------────-------──---──────-----------------

# Discord: Mr.Marvellous#3730
# Discord has to be running before this is--duh

import config
import time
import lib.rpc as rpc
from sys import argv
from trakt.users import User
from calendar import timegm
from pypresence import Presence

def signal_handler(sig, frame):
    runtime = round((time.time() - start)/60/60, 2)
    print('\n', time.strftime("%Y-%m-%d %H:%M:%S @ %Z"), ': Ctrl+C pressed; exiting after', runtime, 'hours')
    try:
        rpc_obj.close()
    except:
        pass
    exit(0)

start = time.time()

if len(argv) != 1:
    print("Usage: $ python discord.py")
else:
    username = config.username
    trakturl = "https://trakt.tv/users/" + username
    version = "2.0"
    largetext = "trakcord v" + version + " by MrMRVLS"

    trakt_connected = False
    while not trakt_connected:
        try:
            me = User(username)
            trakt_connected = True
            print("--GitHub.com/░█▀▄▀█ █▀▀█ ░█▀▄▀█ ░█▀▀█ ░█──░█ ░█─── ░█▀▀▀█--")
            print("--------─────░█░█░█ █▄▄▀ ░█░█░█ ░█▄▄▀ ─░█░█─ ░█─── ─▀▀▀▄▄--")
            print("---────---──-░█──░█ ▀─▀▀ ░█──░█ ░█─░█ ──▀▄▀─ ░█▄▄█ ░█▄▄▄█--")
            print("--──-----──---------────-------──---──────-----------------\n")
            print(time.strftime("%Y-%m-%d %H:%M:%S @ %Z"), ": Successfully connected with the Server!")
        except Exception:
            print(time.strftime("%Y-%m-%d %H:%M:%S @ %Z"), ": Server Connection Failure.")
            time.sleep(15)

    client_id_show = '813396375302832178'
    client_id_movie = '793174395401011221'

    while True:
        try:
            watching = me.watching

            if watching:
                try:
                    imdb_URL = "https://www.imdb.com/title/" + watching.imdb
                    info = 1
                except:
                    imdb_URL = "https://www.imdb.com"
                    info = 0
                timestamp = int(timegm(time.strptime(watching.started_at, "%Y-%m-%dT%H:%M:%S.000Z")))            
                rating_dump = watching.ratings
                ratings = str( round([value for value in rating_dump.values()][0], 1))
                
                if watching.media_type == "episodes":
                    rating = "⭐R: " + ratings + "/10"
                    rpc_obj = rpc.DiscordIpcClient.for_platform(client_id_show)
                    activity = {
                        "timestamps": {
                            "start": timestamp
                        },
                        "assets": {
                            "small_text": "Playing Now !",
                            "small_image": "play",
                            "large_text": largetext,
                            "large_image": "trakt"
                        }
                    }
                    if info == 0:
                        episode_info = "❓・Info not available"
                        rating = "⭐ Rating: " + ratings + "/10"
                        activity["buttons"] = [
                            {
                            "label": rating, 
                            "url": imdb_URL
                            }, 
                            {
                            "label": "🍿・Trakt Profile", 
                             "url": trakturl
                            }
                        ]
                    else:
                        episode_info = "📺・Info | " + rating
                        activity["buttons"] = [
                            {
                            "label": episode_info, 
                            "url": imdb_URL
                            }, 
                            {
                            "label": "🍿・Trakt Profile", 
                            "url": trakturl
                            }
                        ]
                    details = watching.show
                    state = "".join(("S", str(watching.season),":", "E", str(watching.episode), " (", watching.title  , ")"))
                    activity["details"] = details
                    activity["state"] = state
                    print(time.strftime("%Y-%m-%d %H:%M:%S @ %Z"), ": Trakt: playing", details, state)
                    
                else:
                    rpc_obj = rpc.DiscordIpcClient.for_platform(client_id_movie)
                    activity = {
                        "timestamps": {
                            "start": timestamp
                        },
                        "assets": {
                            "small_text": "Playing Now !",
                            "small_image": "play",
                            "large_text": largetext,
                            "large_image": "trakt"
                        }
                    }
                    if info == 0:
                        movie_info = "❓・Info not available"
                        activity["buttons"] = [
                            {
                            "label": "🍿・Trakt Profile", 
                            "url": trakturl
                            }
                        ]
                    else:
                        movie_info = "📺・Movie Info"
                        activity["buttons"] = [
                            {
                            "label": movie_info, 
                            "url": imdb_URL
                            }, 
                            {
                            "label": "🍿・Trakt Profile", 
                            "url": trakturl
                            }
                        ]
                    rating = "⭐ Rating: " + ratings + "/10"
                    details  = "".join((watching.title, " (", str(watching.year), ")"))
                    activity["state"] = rating
                    activity["details"] = details
                    print(time.strftime("%Y-%m-%d %H:%M:%S @ %Z"), ": Trakt: playing", details)
                try:
                    rpc_obj.set_activity(activity)
                except:
                    rpc_obj = rpc.DiscordIpcClient.for_platform(client_id_show)
            else:
                try:
                    print(time.strftime("%Y-%m-%d %H:%M:%S @ %Z"), ": Trakt: not playing.")
                    rpc_obj.close()
                except:
                    pass
        except:
            print(time.strftime("%Y-%m-%d %H:%M:%S @ %Z"), ": API Error! Check again later.")
        time.sleep(15)