from flask import Flask, request, jsonify
import run, time

app = Flask(__name__)
cache = set()

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route("/api/get_index", methods=['POST'])
def get_link():
    query = request.json['query'] #
    #print("test!")
    global cache #
    image = run.run(query) #returns map thing
    for i in image:
        cache.add(i)
    #serialize
    #print(image['image'])
    #print(image['colors'])
    #print("this is working")
    #json.dumps(list(arr.astype(float)))
    testing = jsonify({"image":image}) #return map of colors + pic
    return testing