from flask import Flask, request, jsonify, render_template
from routes.hola import hola_bp
from openai import OpenAI

client = OpenAI()

def call_gpt(text, model='gpt-4o-mini'):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": text}
        ]
    )
    return completion.choices[0].message['content']

app = Flask(__name__)
app.secret_key = 'default_secret_key'

# Registrar el blueprint
app.register_blueprint(hola_bp)

@app.route('/')
def home():
    return render_template('hola.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = call_gpt(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
