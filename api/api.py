from flask import Flask, request, jsonify, send_file
import run, time, detect

app = Flask(__name__)
cache = set()

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route("/api/get_index", methods=['POST'])
def get_link():
    query = request.json['query'] #
    global cache #
    image = run.run(query) #returns map thing
    color = send_file('./array.jpg')
    for i in image:
        cache.add(i)
    testing = jsonify({"image":image}) #return the img
    return testing