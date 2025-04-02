from flask import Flask, request, jsonify, render_template
import fitz  # PyMuPDF
import os
import groq
from flask_cors import CORS

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

# ✅ Load Groq API Key
GROQ_API_KEY = "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"
client = groq.Groq(api_key=GROQ_API_KEY)

# ✅ Extract text from PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# ✅ Load restaurant menu
PDF_PATH = "restaurant-menu.pdf"
restaurant_data = extract_text_from_pdf(PDF_PATH)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    if any(word in restaurant_data.lower() for word in user_input.lower().split()):
        prompt = f"Based on the restaurant info:\n{restaurant_data}\n\nQ: {user_input}"
        
        try:
            response = client.chat.completions.create(
                model="llama3-70b-8192",  # ✅ Use the new supported model
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            bot_reply = response.choices[0].message.content.strip()
        except Exception as e:
            bot_reply = f"❌ Error: {str(e)}"

        return jsonify({"response": bot_reply})
    
    return jsonify({"response": "❌ I can only answer questions related to the restaurant."})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
