#########################################
##### Name: Hiroyuki Makino         #####
##### Uniqname: mhiro               #####
#########################################

from requests_oauthlib import OAuth1
import json
import requests
import secrets as secrets 
from flask import Flask, render_template
app = Flask(__name__)

client_key = secrets.api_key

def make_request():
    '''Make a request to NY Times API using the baseurl and api_key
    
    Parameters
    ----------
    None
    
    Returns
    -------
    dict
        the data returned from making the request in the form of 
        a dictionary
    '''
    baseurl = "https://api.nytimes.com/svc/topstories/v2/technology.json?api-key="
    url = baseurl + client_key
    response = requests.get(url)
    ret = json.loads(response.text)
    return ret

dict_results = make_request()
list_results = list()

for i in range(5):
    list_results.append([dict_results['results'][i]['title'], dict_results['results'][i]['url'],
        dict_results['results'][i]['multimedia'][1]['url']])

@app.route('/')
def index():
    return '<h1>Welcome!</h1>'

@app.route('/name/<nm>')
def name(nm):
    return render_template('name.html', name=nm) 

@app.route('/headlines/<nm>')
def headlines(nm):
    article1 = list_results[0][0]
    article2 = list_results[1][0]
    article3 = list_results[2][0]
    article4 = list_results[3][0]
    article5 = list_results[4][0]
    return render_template('headlines.html', name=nm, article1=article1,
     article2=article2, article3=article3, article4=article4, article5=article5) 


if __name__ == "__main__":
    print('starting Flask app', app.name)  
    app.run(debug=True)

