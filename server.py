from flask import Flask
from flask import request
import simplejson as json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

#Messenger Chatbot
@app.route('/facebook', methods=['POST','GET'])
def facebook():
  #print request.get_json()['status']['result']
  #pprint(request.data)

  #location_data= json.loads(request.data)['originalRequest']['data']['postback']['data']
  #lat= location_data['lat']
  #lon= location_data['long']

  for x in json.loads(request.data)['result']['contexts']:
    if x.get('name')=='generic':
      sabor= x.get('parameters')['Sabor'].encode('ascii', 'ignore').decode('ascii')
      tamano= x.get('parameters')['Tamano'].encode('ascii', 'ignore').decode('ascii')

  print('Cliente con coordenadas ({},{}) acaba de pedir una pizza de {}, tamano {}'.format(lat, lon, sabor, tamano))


  return 'pepito'
