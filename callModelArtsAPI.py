import requests

url = "https://01516f373f434921a874bf502a986a58.apig.ap-southeast-3.huaweicloudapis.com/v1/infers/43ce3a2e-4413-4672-a482-f581d50e3f3c"
headers = {"X-Apig-AppCode" : "85619715500e42d3890b5c47cba491b07378b01efe4449888b920a666dff0a31"}
dataFiles = {"images": ("1615455264273.jpg", open("1615455264273.jpg","rb"), "image/jpg", {})}

try:
    response = requests.post(url, headers = headers, files=dataFiles)
    print(response.text)
    print(response.status_code)
    jsonResult = response.json()
    result = jsonResult['predicted_label']
    arScores = jsonResult['scores']
    predicted_score = 0
    for score in arScores:
        if score[0] == result:
            predicted_score = float(score[1])
    print("Leafs Condition is: %s. The Accuracy for current situation is %.2f" %(result,predicted_score))
except IOError as e:
    print("Error: ",str(e))