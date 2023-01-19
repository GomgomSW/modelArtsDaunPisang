from flask import Flask
from flask import render_template, request
import requests

app = Flask(__name__)
url = url = "https://01516f373f434921a874bf502a986a58.apig.ap-southeast-3.huaweicloudapis.com/v1/infers/43ce3a2e-4413-4672-a482-f581d50e3f3c"
headers = {"X-Apig-AppCode" : "85619715500e42d3890b5c47cba491b07378b01efe4449888b920a666dff0a31"}
dataFiles = {"images": ("1615455264273.jpg", open("1615455264273.jpg","rb"), "image/jpg", {})}

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/recognize', methods = ['POST'])
def call_modelArts():
    f = request.files['imgFilename']
    print('recognize: '+f.filename)
    files = {"images": (f.filename, f.read(), f.content_type)}
    resp = requests.post(url, headers=headers, files=files)
    print('Result: '+resp.text)
    jsonResult = resp.json()
    result = jsonResult['predicted_label']
    arScores = jsonResult['scores']
    predicted_score = 0
    for score in arScores:
        if score[0]==result:
            predicted_score = float(score[1])
    print("Leafs Condition is: %s. The Accuracy for current situation is %.2f" %(result,predicted_score))

    if resp.status_code == 200:     
        strStatus = "Success"
    else:
        strStatus = "Failed"
    return render_template("result.html", leaf=result, status=strStatus, accuracy=predicted_score)

if __name__ == "__main__":
    app.run('0.0.0.0', port=8000, debug=True)