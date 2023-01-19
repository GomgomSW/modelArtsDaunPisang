from flask import Flask
from flask import render_template, request
import requests

app = Flask(__name__)
url = url = "https://01516f373f434921a874bf502a986a58.apig.ap-southeast-3.huaweicloudapis.com/v1/infers/43ce3a2e-4413-4672-a482-f581d50e3f3c"
headers = {"X-Apig-AppCode" : "85619715500e42d3890b5c47cba491b07378b01efe4449888b920a666dff0a31"}
dataFiles = {"images": ("1615455264273.jpg", open("1615455264273.jpg","rb"), "image/jpg", {})}

@app.route('/', methods=['GET'])
def index():
    return"Hello world from Flask"

@app.route('/test', methods=['GET'])
def call_modelArts_API():
    print("/test process")
    response = requests.post(url, headers=headers, files=dataFiles)
    jsonResult = response.json()
    result = jsonResult['predicted_label']
    arScores = jsonResult['scores']
    predicted_score = 0
    for score in arScores:
        if score[0]==result:
            predicted_score = float(score[1])
    resp = {}
    resp['result'] = result
    resp['score']=predicted_score
    return resp

if __name__=="__main__":
    app.run('0.0.0.0', port=8000, debug=True)