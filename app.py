import wget
from flask import Flask, request, jsonify
import requests
from pyDes import *
import base64
import re
import bs4

app = Flask(__name__)

@app.route("/")
def index():
    return """<span style="font-family: verdana; font-size: large;">Welcome to APIs</span><div><br /></div><div>Here you will get some free APIs. Feel free to use</div><div><br /></div><div><ul><li>WebToPDF: Converts web pages into PDF</li></ul></div>"""

@app.route("/webtopdf/", methods=['GET'])
def webtopdf():
    url = request.args.get('url')
    webtopdf_api = "05c0b0d5b1077237d91512b78724700dac85fa83ae7a527f4b858ef52f7dbf91"
    burl = f"https://api.html2pdf.app/v1/generate?apiKey={webtopdf_api}&url={url}"
    return wget.download(burl, out="HTMLtoPDF.pdf")

@app.route("/ifsc/", methods=['GET'])
def ifsc():
    query = request.args.get('query')
    base_url = f"https://ifsc.razorpay.com/{query}"
    result = requests.get(base_url).json()
    return result

@app.route("/random", methods=['GET'])
def RandomPerson():
    base_url = "https://pipl.ir/v1/getPerson"
    result = requests.get(base_url).json()
    return result

@app.route("/url/", methods=['GET'])
def URLShortner():
    query = request.args.get('url')
    exp = {"url": query}
    base_url = "https://cleanuri.com/api/v1/shorten"
    result = requests.post(base_url, data=exp).json()
    return result

@app.route("/api/movie/", methods=['GET'])
def Movie():
    query = request.args.get("query")
    base_url = f"http://www.omdbapi.com/?apikey=fc5d782f&s={query}"
    result = requests.get(base_url).json()
    return result

@app.route("/songs/", methods=['GET'])
def Songs():
    song_name = request.args.get('query')
    des_cipher = des(b"38346591", ECB, b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    search_base_url = "https://www.jiosaavn.com/api.php?__call=autocomplete.get&_format=json&_marker=0&cc=in&includeMetaTags=1&query="
    song_details_base_url = "https://www.jiosaavn.com/api.php?__call=song.getDetails&cc=in&_marker=0%3F_marker%3D0&_format=json&pids="
    url = search_base_url + song_name
    song = requests.get(url).json()
    pid = []
    urls = []
    for i in range(len(song["albums"]["data"])):
        pid = (song["albums"]["data"][i]["more_info"]["song_pids"])
        pid_sep = pid.split(", ")
        url2 = song_details_base_url + pid_sep[0]
        song_info = requests.get(url2).json()
        encrypted_url = song_info[pid_sep[0]]["encrypted_media_url"]
        enc_url = base64.b64decode(encrypted_url.strip())
        dec_url = des_cipher.decrypt(enc_url, padmode=PAD_PKCS5).decode('utf-8')
        urls.append(dec_url)
    songs_list = {}
    for i in range(len(song["albums"]["data"])):
        songs_list["song" + str(i + 1)] = {"Title": song["albums"]["data"][i]["title"],
                                           "Image": song["albums"]["data"][i]["image"],
                                           "Artist": song["albums"]["data"][i]["music"],
                                           "Description": song["albums"]["data"][i]["description"],
                                           "URL": urls[i]}
    return jsonify(songs_list)

@app.route("/corona/", methods=['GET'])
def corona():
    country = request.args.get("query")
    exp = re.compile("(\d.*[0-9])")
    base_url = f"https://www.worldometers.info/coronavirus/country/{country.lower()}/"
    req = requests.get(base_url)
    bs = bs4.BeautifulSoup(req.text, 'html.parser')
    soup = bs.find_all("div", class_='maincounter-number')
    a = []
    for i in soup:
        a.append(str(i))
    res = []
    for i in a:
        res += exp.findall(i)
    result = {"Active Cases ": res[0],
    "Death Cases ": res[1],
    "Recovered ": res[3]}
    return jsonify(result)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000, use_reloader=True, threaded=True)
