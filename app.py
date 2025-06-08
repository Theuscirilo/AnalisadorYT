from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)


os.environ["OPENAI_API_KEY"] = "Sua Chave aqui"  

client = OpenAI()  

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analisar", methods=["POST"])
def analisar():
    data = request.get_json()
    url = data.get("url", "")

    if not url:
        return jsonify({"error": "URL não fornecida"}), 400

    prompt = f"Resuma o conteúdo deste vídeo do YouTube: {url}"

    try:
        response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)
        resumo = response.choices[0].message.content
        return jsonify({"resumo": resumo})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
