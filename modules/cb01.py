###########################
###### STREAMING API ######
# Developed by: @Matt0550 #
###########################
# CB01 module by: @Matt0550

from flask import Blueprint
from flask import redirect
from bs4 import BeautifulSoup
import requests

URL = 'https://api.feedly.com/v3/mixes/contents?streamId=feed%2Fhttps%3A%2F%2Fcb01.uno%2Ffeed%2F&count=3&hours=20&backfill=true&ck=1703878041437&ct=feedly.desktop&cv=31.0.2046'

app_cb01 = Blueprint('app_cb01', __name__)

@app_cb01.route('/v1/cb01', methods=['GET'])
def cb01():
    try:
        r = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
        
        if r.status_code != 200:
            return {"message": "Error: " + str(r.status_code), "status": "error"}

        # Parse as json
        r = r.json()
        link = r['alternate'][0]
        # Return the link
        return {"message": link['href'], "status": "success"}

    except Exception as e:
        return {"message": str(e), "status": "error"}


@ app_cb01.route('/cb01', methods=['GET'])
def redirect_cb01():
    link = cb01()['message']
    if link.startswith('https://' or 'http://'):
        return redirect(link, code=302)
    else:
        return "<h1>Error</h1><p>The link returned by the API is not valid.</p>" + link, 500