from distutils.log import debug
from gevent import monkey; monkey.patch_all()
from flask import Flask, Response, render_template, stream_with_context, request
from gevent.pywsgi import WSGIServer
from werkzeug.utils import secure_filename
import os
import json
import time

import data_read

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route("/")
def render_index():
    return render_template("index.html")

@app.route("/home")
def render_home():
    return render_template("index.html")

@app.route("/file-upload", methods = ['POST'])
def file_upload():
    f = request.files['file']
    if request.method == 'POST' and secure_filename(f.filename) != '':
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],"video.mp4"))
        print(secure_filename(f.filename))
        print("File Upload Success")
        # print("Criminal Name",data_read.criminalname())
        print(data_read.activitytype())
        return render_template("dashboard.html",data_criminal = data_read.criminalname(),data_face = data_read.criminalcount(),data_activity = data_read.activitytype(),data = json.dumps(data_read.activity(2)))
    else:
        return "NO file detected"


@app.route("/listen")
def listen():

    def respond_to_client():
        while True:

            chart_data = []

            for r in range(2,14) :
                chart_data.append(data_read.activity(r))
            
            _data = json.dumps({"data" : chart_data})
            yield f"id: 1\ndata: {_data}\nevent: online\n\n"
            # print(data_read.activity(2))
            time.sleep(3)
    return Response(respond_to_client(), mimetype='text/event-stream')



if __name__ == "__main__":
    app.run(debug=True)
    http_server = WSGIServer(app)
    http_server.serve_forever() 