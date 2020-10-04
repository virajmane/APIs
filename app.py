import wget
from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "<h>Welcome to songs</h>"

@app.route("/api/", methods=['GET'])
def api():
    url = request.args.get('url')
    webtopdf_api = os.environ.get("webtopdf")
    burl = f"https://api.html2pdf.app/v1/generate?apiKey={webtopdf_api}&url={url}"
    return wget.download(burl, out="HTMLtoPDF.pdf")

if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=5000, use_reloader=True, threaded=True)
