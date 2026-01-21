from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

PROXIES = {
    'http': 'socks5h://tor:9050',
    'https': 'socks5h://tor:9050'
}

@app.route('/api/users')
def get_users():
    try:
        response = requests.get('https://randomuser.me/api/?results=5', proxies=PROXIES)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- NOUVELLE ROUTE POUR LES IMAGES ---
@app.route('/api/proxy-image')
def proxy_image():
    image_url = request.args.get('url')
    if not image_url:
        return "URL manquante", 400
    
    try:
        # On télécharge l'image via Tor
        img_response = requests.get(image_url, proxies=PROXIES, stream=True)
        
        # On renvoie l'image brute au navigateur avec le type MIME approprié
        return Response(
            img_response.content,
            mimetype=img_response.headers.get('Content-Type')
        )
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)