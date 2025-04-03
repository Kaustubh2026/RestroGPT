# import os
# import fitz  # PyMuPDF
# import groq
# from flask import Flask, request, jsonify, render_template
# from flask_cors import CORS
# from dotenv import load_dotenv

# # ✅ Load environment variables
# load_dotenv()

# # ✅ Initialize Flask app
# app = Flask(__name__, static_folder="static", template_folder="templates")
# CORS(app)

# # ✅ Secure API Key (DO NOT hardcode API keys in code)
# GROQ_API_KEY = "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"
# if not GROQ_API_KEY:
#     raise ValueError("⚠️ GROQ_API_KEY is missing! Set it in the environment variables.")

# client = groq.Groq(api_key=GROQ_API_KEY)

# # ✅ Extract text from PDF
# def extract_text_from_pdf(pdf_path):
#     if not os.path.exists(pdf_path):
#         return "Menu not available."
    
#     doc = fitz.open(pdf_path)
#     text = "".join(page.get_text() for page in doc)
#     return text.strip()

# # ✅ Load restaurant menu
# PDF_PATH = "restaurant-menu.pdf"
# restaurant_data = extract_text_from_pdf(PDF_PATH)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/chat", methods=["POST"])
# def chat():
#     user_input = request.json.get("message", "").strip()
    
#     if not user_input:
#         return jsonify({"error": "No message provided"}), 400

#     if any(word in restaurant_data.lower() for word in user_input.lower().split()):
#         prompt = f"Based on the restaurant info:\n{restaurant_data}\n\nQ: {user_input}"
        
#         try:
#             response = client.chat.completions.create(
#                 model="llama3-70b-8192",  # ✅ Using an active model
#                 messages=[{"role": "user", "content": prompt}],
#                 temperature=0.7
#             )
#             bot_reply = response.choices[0].message.content.strip()
#         except Exception as e:
#             bot_reply = f"❌ Error: {str(e)}"

#         return jsonify({"response": bot_reply})
    
#     return jsonify({"response": "❌ I can only answer questions related to the restaurant."})

# # ✅ Ensure the correct port for Vercel deployment
# if __name__ == "__main__":
#     port = int(os.getenv("PORT", 8080))
#     app.run(host="0.0.0.0", port=port, debug=True)
import os
import fitz  # PyMuPDF
import groq
import pytesseract  # OCR for scanned PDFs
from PIL import Image
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

# ✅ Initialize Flask app
app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app, resources={r"/*": {"origins": "*"}})  # Adjust CORS for security

# ✅ Secure API Key
GROQ_API_KEY = "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"
if not GROQ_API_KEY:
    raise ValueError("⚠️ GROQ_API_KEY is missing! Set it in the environment variables.")

client = groq.Groq(api_key=GROQ_API_KEY)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

extracted_text = "No PDF uploaded yet. Please upload a PDF first."

# ✅ Extract text from PDF (with OCR for scanned PDFs)
def extract_text_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        return "PDF not found."

    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        page_text = page.get_text()
        if page_text.strip():
            text += page_text + "\n"
        else:
            # Handle scanned pages (OCR)
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            text += pytesseract.image_to_string(img) + "\n"

    return text.strip() if text.strip() else "❌ No readable text found in PDF."

# ✅ Home Page
@app.route("/")
def home():
    return render_template("index.html")

# ✅ Upload PDF Endpoint
@app.route("/upload", methods=["POST"])
def upload_pdf():
    global extracted_text

    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    extracted_text = extract_text_from_pdf(file_path)

    return jsonify({"message": "File uploaded successfully", "extracted_text": extracted_text})

# ✅ Chatbot Endpoint
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").strip()
    
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    prompt = f"Based on the provided PDF:\n{extracted_text}\n\nQ: {user_input}"

    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",  # ✅ Using a supported model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        bot_reply = response.choices[0].message.content.strip()
    except Exception as e:
        bot_reply = f"❌ Error: {str(e)}"

    return jsonify({"response": bot_reply})

# ✅ Ensure the correct port for deployment
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
