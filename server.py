from flask import Flask, render_template, Response, request

import json


app = Flask(__name__)
build = None
deploy = None

@app.route("/health")
def status():
    """
    assess availability of API
    """
    return Response("OK", status=200, mimetype='text/plain')

@app.route("/set_build_time", methods=['POST'])
def set_build_time_req():
    global build
    print("test")
    data = request.get_json(force=True)
    build = str(data["built_at"])
    return Response("OK", status=200, mimetype='text/plain')

@app.route("/set_deploy_time", methods=['POST'])
def set_deploy_time_req():
    global deploy
    data = request.get_json(force=True)
    deploy = str(data["deploy_at"])
    return Response("OK", status=200, mimetype='text/plain')

@app.route("/")
def display():
    """
    assess output of API
    """
    global build
    global deploy
    if build is None :
        build = "Build has not started yet"
    if deploy is None:
        deploy = "Deployment has not started yet"
    display_message = {"hello:": "world", "built_at": f"{build}", "deployed_at:" : f"{deploy}"}
    value =  (json.dumps(display_message, indent=4))
    return Response(value, status=200, mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)