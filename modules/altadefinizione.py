###########################
###### STREAMING API ######
# Developed by: @Matt0550 #
###########################
# Altadefinizione module by: @Matt0550

from flask import Blueprint
from flask import redirect
from bs4 import BeautifulSoup
import requests

URL = 'https://altadefinizione.nuovo.live/'

app_altadefinizione = Blueprint('app_altadefinizione', __name__)

@app_altadefinizione.route('/v1/altadefinizione', methods=['GET'])
def altadefinizione():
    try:
        r = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
        if r.status_code != 200:
            return {"message": "Error: " + str(r.status_code), "status": "error"}
            
        soup = BeautifulSoup(r.text, 'html.parser')
        # Find an h2 with class elementor-heading-title elementor-size-default and get the a tag
        link = soup.find('h2', class_='elementor-heading-title elementor-size-default').find('a')
        # Return the link
        return {"message": link['href'], "status": "success"}

    except Exception as e:
        return {"message": str(e), "status": "error"}
        
@ app_altadefinizione.route('/altadefinizione', methods=['GET'])
def redirect_altadefinizione():
    link = altadefinizione()['message']
    if link.startswith('https://' or 'http://'):
        return redirect(link, code=302)
    else:
        return "<h1>Error</h1><p>The link returned by the API is not valid.</p>" + link, 500