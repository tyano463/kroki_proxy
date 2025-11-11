from flask import Flask, request, Response
import requests
import urllib.parse

app = Flask(__name__)

@app.route("/graphviz/svg")
def proxy():
    source = request.args.get("source", "")
    dot_code = urllib.parse.unquote(source)
    try:
        res = requests.post(
            "https://kroki-render.onrender.com/graphviz/svg",
            headers={"Content-Type": "text/plain"},
            data=dot_code
        )
        return Response(res.content, mimetype="image/svg+xml")
    except Exception as e:
        return Response("Proxy error", status=500)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

