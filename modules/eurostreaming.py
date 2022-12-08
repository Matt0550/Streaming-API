###########################
###### STREAMING API ######
# Developed by: @Matt0550 #
###########################
# Eurostreaming module by: @Matt0550

from flask import Blueprint
from flask import redirect
from bs4 import BeautifulSoup
import requests

URL = 'https://t.me/joinchat/UO4tlY9mcDKL7wl2'

app_eurostreaming = Blueprint('app_eurostreaming', __name__)

@app_eurostreaming.route('/v1/eurostreaming', methods=['GET'])
def eurostreaming():
    try:
        r = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
        if r.status_code != 200:
            return {"message": "Error: " + str(r.status_code), "status": "error"}
        soup = BeautifulSoup(r.text, 'html.parser')
        # Find a div with class tgme_page_description and find any text which contains "https://eurostreaming."
        link = soup.find('div', class_='tgme_page_description').find(text=lambda text: text and "https://eurostreaming." in text)
        # Remove all text before "https://eurostreaming." 
        link = link[link.find("https://eurostreaming."):]
        
        # Return the link
        return {"message": link, "status": "success"}

    except Exception as e:
        print(e)
        return {"message": str(e), "status": "error"}


@ app_eurostreaming.route('/eurostreaming', methods=['GET'])
def redirect_eurostreaming():
    link = eurostreaming()['message']
    if link.startswith('https://' or 'http://'):
        return redirect(link, code=302)
    else:
        return "<h1>Error</h1><p>The link returned by the API is not valid.</p>" + link, 500