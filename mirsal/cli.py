import sys
from flask import Flask, send_file
from pyngrok import ngrok
import os

app = Flask(__name__)
log_file = None

@app.route("/log")
def serve_raw_log():
    return send_file(log_file, mimetype="text/plain")

@app.route("/")
def index():
    return f"""
    <html>
    <head>
        <title>{log_file}</title>
        <meta http-equiv="refresh" content="30">
        <style>
            body {{
                background-color: #111;
                color: #0f0;
                font-family: monospace;
                margin: 0;
                padding: 0;
            }}
            .header {{
                background-color: #222;
                padding: 15px;
                font-size: 18px;
                border-bottom: 1px solid #444;
            }}
            iframe {{
                width: 100%;
                height: calc(100vh - 50px);
                border: none;
                background-color: #111;
                display: none;
            }}
            #spinner {{
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                color: #0f0;
                font-size: 16px;
                font-family: monospace;
            }}
        </style>
    </head>
    <body>
        <div class="header">📄 {os.path.basename(log_file)}</div>
        <div id="spinner">⏳ Loading log file...</div>
        <iframe id="logframe" src="/log"></iframe>
        <script>
            const iframe = document.getElementById("logframe");
            const spinner = document.getElementById("spinner");
            iframe.onload = () => {{
                spinner.style.display = "none";
                iframe.style.display = "block";
                const doc = iframe.contentDocument || iframe.contentWindow.document;
                iframe.contentWindow.scrollTo(0, doc.body.scrollHeight);
            }};
        </script>
    </body>
    </html>
    """


def main():
    global log_file
    if len(sys.argv) != 2:
        print("Usage: mirsal <log_file>")
        sys.exit(1)
    log_file = os.path.abspath(sys.argv[1])
    public_url = ngrok.connect(8000)
    print(f"🚀 Log viewer is live at: {public_url}")
    app.run(port=8000)

