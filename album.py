import os
import requests
import json
from flask import abort, Flask, jsonify, request


# client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
# user_id = "U01JKKZFVJS"


app = Flask(__name__)

# def is_request_valid(request):
#     is_token_valid = request.form['token'] == os.environ[token']
#     is_team_id_valid = request.form['team_id'] == os.environ['team_id']
#     print("not valid")
#     return is_token_valid and is_team_id_valid

# @app.route('/hello-there', methods=['POST'])
# def hello_there():
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

    # return jsonify(
    #     response_type='in_channel',
    #     text='<https://youtu.be/frszEJb0aOo|General Kenobi!>',
    # )
    # print("yo")
    # if not is_request_valid(request):
    #     abort(400)