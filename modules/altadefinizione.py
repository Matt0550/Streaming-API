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
        soup = BeautifulSoup(r.text, 'html.parser')
        # Find an h2 with class elementor-heading-title elementor-size-default and get the a tag
        link = soup.find('h2', class_='elementor-heading-title elementor-size-default').find('a')
        # Return the link
        return {"message": link['href'], "status": "success"}

    except Exception as e:
        return {"message": str(e), "status": "error"}
        
@ app_altadefinizione.route('/altadefinizione', methods=['GET'])
def redirect_altadefinizione():
    # Redirect to the link returned by the function altadefinizione
    return redirect(altadefinizione()['message'], code=302)