from flask import Flask, render_template, jsonify, request
import socket
from threading import Thread
import time
import datetime

app = Flask(__name__)

def check_single_service(service, host, port):
    start_time = time.time()
    try:
        with socket.create_connection((host, port), timeout=5) as sock:
            response_time = round((time.time() - start_time) * 1000, 2)
            return {
                "status": "Accessible",
                "response_time": f"{response_time}ms",
                "last_checked": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "details": "Connection successful",
                "host": host,
                "port": port
            }
    except socket.timeout:
        return {
            "status": "Timeout",
            "response_time": "N/A",
            "last_checked": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "details": "Connection timed out after 5 seconds",
            "host": host,
            "port": port
        }
    except socket.gaierror:
        return {
            "status": "DNS Error",
            "response_time": "N/A",
            "last_checked": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "details": "Could not resolve hostname",
            "host": host,
            "port": port
        }
    except socket.error as e:
        return {
            "status": "Unreachable",
            "response_time": "N/A",
            "last_checked": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "details": f"Connection failed: {str(e)}",
            "host": host,
            "port": port
        }

def check_network_ports():
    gaming_services = {
        "Game Launchers": {
            "Steam": ("store.steampowered.com", 443),
            "Epic Games": ("launcher.epicgames.com", 443),
            "Battle.net": ("us.actual.battle.net", 443),
            "Origin": ("origin-a.akamaihd.net", 443),
            "GOG Galaxy": ("gog.com", 443),
            "Ubisoft Connect": ("connect.ubisoft.com", 443),
            "Xbox PC App": ("xbox.com", 443),
            "Amazon Games": ("gaming.amazon.com", 443),
            "Itch.io": ("itch.io", 443)
        },
        "Popular Games": {
            "World of Warcraft": ("us.logon.battle.net", 1119),
            "League of Legends": ("riotgames.com", 443),
            "Fortnite": ("fortnitepublic-service-prod11.ol.epicgames.com", 5222),
            "Minecraft": ("session.minecraft.net", 443),
            "Valorant": ("valorant.secure.dyn.riotcdn.net", 443),
            "CS:GO": ("api.steampowered.com", 443),
            "Dota 2": ("api.steampowered.com", 443),
            "Apex Legends": ("origin-a.akamaihd.net", 443),
            "GTA Online": ("socialclub.rockstargames.com", 443),
            "Rainbow Six Siege": ("ubisoft-uplay-savegames.s3.amazonaws.com", 443),
            "Overwatch": ("overwatch.blizzard.com", 443)
        },
        "Game Development": {
            "Unity": ("unity.com", 443),
            "Unreal Engine": ("unrealengine.com", 443),
            "GitHub Gaming": ("github.com", 443),
            "Game Dev Stack Exchange": ("gamedev.stackexchange.com", 443)
        },
        "Gaming Communities": {
            "Discord": ("discord.com", 443),
            "Twitch": ("twitch.tv", 443),
            "TeamSpeak": ("teamspeak.com", 443),
            "Reddit Gaming": ("reddit.com", 443),
            "Steam Community": ("steamcommunity.com", 443),
            "Xbox Live": ("xbox.live.com", 443),
            "PlayStation Network": ("playstation.com", 443)
        },
        "Gaming Voice Chat": {
            "Discord Voice": ("discord.media", 443),
            "TeamSpeak Voice": ("voice.teamspeak.com", 9987),
            "Mumble": ("mumble.info", 64738),
            "Ventrilo": ("ventrilo.com", 3784)
        }
    }
    
    results = {}
    threads = []
    
    def check_service(category, service, host, port):
        if category not in results:
            results[category] = {}
        results[category][service] = check_single_service(service, host, port)
    
    for category, services in gaming_services.items():
        for service, (host, port) in services.items():
            thread = Thread(target=check_service, args=(category, service, host, port))
            thread.start()
            threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    return results

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check')
def check():
    client_info = {
        "ip": request.remote_addr,
        "test_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "location": request.headers.get('X-Real-IP', request.remote_addr)
    }
    
    results = check_network_ports()
    return jsonify({
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "services": results,
        "client_info": client_info
    })

if __name__ == '__main__':
    app.run(debug=True) 