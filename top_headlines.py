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
        dict_results['results'][i]['multimedia'][3]['url']])

@app.route('/')
def index():
    return '<h1>Welcome!</h1>'

@app.route('/name/<nm>')
def name(nm):
    return render_template('name.html', name=nm) 

@app.route('/headlines/<nm>')
def headlines(nm):
    list_article = list()
    for result in list_results:
        list_article.append(result[0])

    return render_template('headlines.html', name=nm, list_article=list_article) 

@app.route('/links/<nm>')
def links(nm):
    list_article = list()
    list_url = list()
    for result in list_results:
        list_article.append(result[0])
        list_url.append(result[1])
    num = len(list_results)

    return render_template('links.html', name=nm, list_article=list_article, list_url=list_url, num=num) 

@app.route('/images/<nm>')
def images(nm):
    list_article = list()
    list_url = list()
    list_image = list()
    for result in list_results:
        list_article.append(result[0])
        list_url.append(result[1])
        list_image.append(result[2])
    num = len(list_results)

    return render_template('images.html', name=nm, list_article=list_article, list_url=list_url, list_image=list_image, num=num)

if __name__ == "__main__":
    print('starting Flask app', app.name)  
    app.run(debug=True)

