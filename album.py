import requests
import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/album", methods=['POST'])
def album():
    url = "https://1001albumsgenerator.com/api/v1/groups/companyx"
    resp = requests.get(url)
    if(resp.ok):
        jData = json.loads(resp.content)
        return jsonify(
            response_type='in_channel',
            text=jData["currentAlbum"]["name"] + " - " + jData["currentAlbum"]["artist"] + " https://open.spotify.com/album/"+jData["currentAlbum"]["spotifyId"],
        )
    else:
        # If response code is not ok (200), print the resulting http error code with description
        resp.raise_for_status()
        return jsonify(
            response_type='in_channel',
            text="error",
        )