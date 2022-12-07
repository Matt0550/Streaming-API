###########################
###### STREAMING API ######
# Developed by: @Matt0550 #
###########################
# Eurostreaming module by: @Matt0550

from flask import Blueprint
from flask import redirect
from bs4 import BeautifulSoup
import requests

URL = 'https://www.eurostreaming-nuovo-indirizzo.online/'

app_eurostreaming = Blueprint('app_eurostreaming', __name__)

@app_eurostreaming.route('/v1/eurostreaming', methods=['GET'])
def eurostreaming():
    try:
        r = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        # Find a link with start with "https://eurostreaming."
        link = soup.find('a', href=lambda href: href and href.startswith('https://eurostreaming.'))
        # Return the link
        return {"message": link['href'], "status": "success"}

    except Exception as e:
        return {"message": str(e), "status": "error"}


@ app_eurostreaming.route('/eurostreaming', methods=['GET'])
def redirect_eurostreaming():
    # Redirect to the link returned by the function eurostreaming
    return redirect(eurostreaming()['message'], code=302)