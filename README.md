# ICanHelp

## Team
- Vlad Udovychenko
- Tomasz Spyrka
- Bartosz Wilk
- Bartosz Gaj
- Łukasz Wróbel

## Idea
**Problem:** Ambulances very often do not have the ability to quickly reach the
the injured person. The profession of a lifeguard is becoming less and less popular.
People more and more often think selfishly and do not look at other people's harm

* *We want to change it* *

**Solution:** We offer an application that supports emergency medical services and promotes ancillary activities among people. Thanks to it, we get people used to subject of first aid, and our heroes prove that helping is great.

# Our mission is to connect people who need help with people who know how and want to give it.

## Technology stack

### Frontend
Kibana, Vue.js, GoogleMap

### Backend
Python(RESTful API)
ElasticSearch

## To start:
### You need to have installed
- yarn / npm
- pip
- docker
- Vue.js
- Python3.5 with libraries elasticsearch flask flask-jsonpify flask-sqlalchemy flask-restful flask-corse
### Start ElasticSearch
docker run -p 9200:9200 -it --name health-db docker.elastic.co/elasticsearch/elasticsearch:6.5.1

### Start Kibana
docker run -it -e ELASTICSEARCH_URL=http://0.0.0.0:9200 -p 5601:5601 --name health-kibana docker.elastic.co/kibana/kibana:6.5.1
 - use ElasticSearch host IP

### Run server
Configure host adress and port
run ./server.py with icanhelp/server/ as CWD

### Start Vue
yarn install / npm install
yarn run serve / npm run self
