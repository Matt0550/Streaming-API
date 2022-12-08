###########################
###### STREAMING API ######
# Developed by: @Matt0550 #
###########################
# CB01 module by: @Matt0550

from flask import Blueprint
from flask import redirect
from bs4 import BeautifulSoup
import requests

URL = 'https://t.me/s/cb01_nuovo_indirizzo_ufficiale/'

app_cb01 = Blueprint('app_cb01', __name__)

@app_cb01.route('/v1/cb01', methods=['GET'])
def cb01():
    try:
        r = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
        if r.status_code != 200:
            return {"message": "Error: " + str(r.status_code), "status": "error"}

        soup = BeautifulSoup(r.text, 'html.parser')
        # Find a link with start with "https://cb01."
        link = soup.find('a', href=lambda href: href and href.startswith('https://cb01.'))
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