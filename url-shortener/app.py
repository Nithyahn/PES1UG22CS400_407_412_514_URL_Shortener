from flask import Flask, request, redirect, jsonify
import string, random

app = Flask(__name__)
url_mapping = {}

def generate_short_id(num_chars=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=num_chars))

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    long_url = data.get('url')
    short_id = generate_short_id()
    url_mapping[short_id] = long_url
    return jsonify({'short_url': f'http://localhost:5000/{short_id}'})

@app.route('/<short_id>')
def redirect_url(short_id):
    long_url = url_mapping.get(short_id)
    if long_url:
        return redirect(long_url)
    return jsonify({'error': 'URL not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
