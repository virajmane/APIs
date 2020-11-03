import wget
from flask import Flask, request, jsonify
import requests
from pyDes import *
import base64
import re
import bs4
from pycricbuzz import Cricbuzz
from cryptography.fernet import Fernet

app = Flask(__name__)

@app.route("/")
def index():
    return """<span style="font-family: verdana; font-size: x-large;">Welcome to APIs</span><div><br /></div><div><span style="font-family: arial;">Here you will get some free APIs. Feel free to use</span></div><div><br /></div><div><ul style="text-align: left;"><li><b><span style="font-family: arial;">WebToPDF: Converts web pages into PDF</span></b></li><ul><li><span style="font-family: arial;">Base Link = https://virajapi.herokuapp.com/webtopdf/?url={Your- URL}</span></li><li><span style="font-family: arial;">Example =&nbsp;&nbsp;<a href="https://virajapi.herokuapp.com/webtopdf/?url=https://www.google.com" target="_blank">https://virajapi.herokuapp.com/webtopdf/?url=https://www.google.com</a></span></li></ul></ul><ul style="text-align: left;"><li><b><span style="font-family: arial;">Bank IFSC Info: Provides Bank Information From IFSC Code</span></b></li><ul><li><span style="font-family: arial;">Base Link =&nbsp;https://virajapi.herokuapp.com/ifsc/?query={IFSC-Code}</span></li><li><span style="font-family: arial;">Example =&nbsp;&nbsp;<a href="https://virajapi.herokuapp.com/ifsc/?query=PYTM0123456" target="_blank">https://virajapi.herokuapp.com/ifsc/?query=PYTM0123456</a></span></li></ul></ul><div><ul><li><b><span style="font-family: arial;">Random Person Info: Gives random information about random person</span></b></li><ul><li><span style="font-family: arial;">Base Link =&nbsp;https://virajapi.herokuapp.com/random/</span></li><li><span style="font-family: arial;">Example =&nbsp;&nbsp;<a href="https://virajapi.herokuapp.com/random/" target="_blank">https://virajapi.herokuapp.com/random/</a></span></li></ul></ul><div><ul><li><b><span style="font-family: arial;">URL Shortner: Shortens the URL</span></b></li><ul><li><span style="font-family: arial;">Base Link =&nbsp;https://virajapi.herokuapp.com/url/?url={Your- URL}</span></li><li><span style="font-family: arial;">Example =&nbsp;&nbsp;<a href="https://virajapi.herokuapp.com/url/?url=https://www.facebook.com" target="_blank">https://virajapi.herokuapp.com/url/?url=https://www.facebook.com</a></span></li></ul></ul><div><ul><li><b><span style="font-family: arial;">Movie API: Provides information about movies from their name</span></b></li><ul><li><span style="font-family: arial;">Base Link =&nbsp;https://virajapi.herokuapp.com/movie/?query={Movie-Name}</span></li><li><span style="font-family: arial;">Example =&nbsp;&nbsp;<a href="https://virajapi.herokuapp.com/movie/?query=Alive" target="_blank">https://virajapi.herokuapp.com/movie/?query=Alive</a></span></li></ul></ul><div><ul><li><b><span style="font-family: arial;">Songs API: Search Songs and get direct download link with other info</span></b></li><ul><li><span style="font-family: arial;">Base Link =&nbsp;https://virajapi.herokuapp.com/songs/?query={Song-Name}</span></li><li><span style="font-family: arial;">Example =&nbsp;&nbsp;<a href="https://virajapi.herokuapp.com/songs/?query=Alone" target="_blank">https://virajapi.herokuapp.com/songs/?query=Alone</a></span></li></ul></ul><div><ul><li><b><span style="font-family: arial;">Corona API: Provides information about Alive, Confirmed, Death cases country-wise</span></b></li><ul><li><span style="font-family: arial;">Base Link =&nbsp;https://virajapi.herokuapp.com/corona/?query={country-name}</span></li><li><span style="font-family: arial;">Example =&nbsp;&nbsp;<a href="https://virajapi.herokuapp.com/corona/?query=india" target="_blank">https://virajapi.herokuapp.com/corona/?query=india</a></span></li></ul></ul><div><ul style="text-align: left;"><li><b><span style="font-family: arial;">Message Encryption API: Encrypts and decrypts messages</span></b></li><ul><li><span style="font-family: arial;">Base Link</span></li><ul><li><span style="font-family: arial;">Encryption =&nbsp;https://virajapi.herokuapp.com/message/?encrypt={Your-Message}</span></li><li><span style="font-family: arial;">Example =&nbsp;<a href="https://virajapi.herokuapp.com/message/?encrypt=Hello" target="_blank">https://virajapi.herokuapp.com/message/?encrypt=Hello</a></span></li><li><span style="font-family: arial;">Decryption =&nbsp;https://virajapi.herokuapp.com/message/?decrypt={Encrypted-Message}</span></li></ul></ul></ul><div><ul style="text-align: left;"><li><span style="font-family: arial;"><b>Instant Mail API: you can instantly generate disposable temporary email address&nbsp;</b></span><b style="font-family: arial;">and immediately receive emails, including attachments</b></li><ul><li><span style="font-family: arial;">Generate Email</span></li><ul><li><span style="font-family: arial;">Base URL =&nbsp;https://virajapi.herokuapp.com/mail/gen/</span></li></ul><li><span style="font-family: arial;">Read Mail:</span></li><ul><li><span style="font-family: arial;">Base URL =&nbsp;https://virajapi.herokuapp.com/mail/msg/?email={Email}</span></li><li><span style="font-family: arial;">Example =&nbsp;&nbsp;<a href="https://virajapi.herokuapp.com/mail/msg/?email=zdd60gc43g@1secmail.com" target="_blank">https://virajapi.herokuapp.com/mail/msg/?email=zdd60gc43g@1secmail.com</a></span></li></ul></ul></ul></div></div></div></div></div></div></div></div>"""
    
@app.route("/webtopdf/", methods=['GET'])
def webtopdf():
    url = request.args.get('url')
    webtopdf_api = "05c0b0d5b1077237d91512b78724700dac85fa83ae7a527f4b858ef52f7dbf91"
    burl = f"https://api.html2pdf.app/v1/generate?apiKey={webtopdf_api}&url={url}"
    return f"<a href={burl} download>Click Here</a>"

@app.route("/ifsc/", methods=['GET'])
def ifsc():
    query = request.args.get('query')
    base_url = f"https://ifsc.razorpay.com/{query}"
    result = requests.get(base_url).json()
    return result

@app.route("/random/", methods=['GET'])
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

@app.route("/movie/", methods=['GET'])
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

@app.route("/cricket/", methods=['GET'])
def cricket():
    c = Cricbuzz()
    match = c.matches()
    mid = (match[0]['id'])
    livescore = c.livescore(mid=mid)
    scorecard = c.scorecard(mid=mid)
    matchinfo = c.matchinfo(mid=mid)
    commentary = c.commentary(mid=mid)

    result = [{"matches": match, "livescore": livescore, "scorecard": scorecard, "matchinfo": matchinfo,
              "commentary": commentary}]
    return result

@app.route("/message/", methods=['GET'])
def endecy():
    encr_msg = request.args.get("encrypt")
    decr_msg = request.args.get("decrypt")

    def keygen():
        key = Fernet.generate_key()
        return key

    def encrypt(message):
        key = keygen()
        en_msg = message.encode()
        f = Fernet(key)
        result = f.encrypt(en_msg)
        final = "{} {}".format(result,key)
        return final
    def decrypt(message):
        try:
            en_msg,key = message.split("' b'")
            en_msg = bytes(en_msg[1:], 'utf-8')
            key = bytes(key[:-1], 'utf-8')
            f = Fernet(key)
            result = f.decrypt(en_msg)
            ultimate =  result.decode('utf-8')
            return ultimate
        except ValueError:
            print("Incorrect Values")

    if encr_msg==None and decr_msg!=None:
        res = {"decrypted_message": decrypt(decr_msg)}
    elif decr_msg==None and encr_msg!=None:
        res = {"encrypted_message": encrypt(encr_msg)}
    return jsonify(res)

@app.route("/mail/")
def mail():
    return "Mail API is working"

@app.route("/mail/gen/")
def generate():
    base_url = "https://www.1secmail.com/api/v1/?action=genRandomMailbox"
    mail = list(requests.get(base_url).json())
    result = {}
    result["mail"] = mail[0]
    return jsonify(result)

@app.route("/mail/msg/", methods=["GET"])
def msg():
    mail = str(request.args.get("email"))
    sep_data = mail.split("@")
    username = sep_data[0]
    domain = sep_data[1]
    req = (requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain}").json())
    count=1
    req_new = {}
    for i in req:
        req_new[f"msg{count}"] = i
        count+=1
    msg_id = []
    for i in range(0,count-1):
        msg_id.append(req[i]["id"])
    final = {}
    count2 = 1
    for i in msg_id:
        final[f"msg{count2}"] = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain}&id={int(i)}").json()
        count2+=1
    return jsonify(final)

@app.route("/insta/<string:url>")
def instagram(url):
    url1 = url
    if "?" in url1:
        url1 = url1.split("?")[0] + "?__a=1"
        r = requests.get(url1).json()
        if (r["graphql"]["shortcode_media"]["is_video"] == False):
            result = r["graphql"]["shortcode_media"]["display_url"]
        elif (r["graphql"]["shortcode_media"]["is_video"] == True):
            result = r["graphql"]["shortcode_media"]["video_url"]
        else:
            result = "Not Found"
    elif "?" not in url1:
        url1 = url1 + "?__a=1"
        result = r["graphql"]["user"]["profile_pic_url_hd"]
    else:
        result = "None"
    return result

if __name__ == "__main__":
    #app.debug = True
    app.run(host='0.0.0.0', port=5000, use_reloader=True, threaded=True)
