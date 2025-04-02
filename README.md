# RestroGPT 🍽️🤖

RestroGPT is an AI-powered restaurant chatbot that helps users interact with restaurant menus and get instant responses to their queries. This project uses **Flask**, **Groq API**, and **PyMuPDF** to extract menu data from a PDF and respond to user queries.

## 🚀 Live Demo
**[RestroGPT on Vercel](https://restro-gpt.vercel.app/)**

## 📜 Features
- 📜 Extracts menu data from a **PDF file**.
- 💬 Answers queries about the restaurant using **Groq AI**.
- 🌐 Deployed on **Vercel** for easy access.
- 🔥 Supports CORS for API integration.

## 🛠️ Tech Stack
- **Backend**: Flask, Python
- **AI API**: Groq
- **PDF Processing**: PyMuPDF
- **Deployment**: Vercel
- **Frontend**: HTML, JavaScript (for rendering responses)

## 📂 Project Structure
```
📦 RestroGPT
 ┣ 📂 static          # Static files (CSS, JS, Images)
 ┣ 📂 templates       # HTML templates
 ┣ 📜 app.py         # Main Flask application
 ┣ 📜 requirements.txt  # Dependencies
 ┣ 📜 vercel.json     # Vercel deployment config
 ┣ 📜 restaurant-menu.pdf # Sample restaurant menu
 ┗ 📜 README.md       # Project documentation
```

## 🏗️ Setup Instructions

### 1️⃣ Clone the repository
```sh
git clone https://github.com/Kaustubh2026/RestroGPT.git
cd RestroGPT
```

### 2️⃣ Create a virtual environment (optional but recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set up your **Groq API Key**
Create a `.env` file and add your API key:
```sh
GROQ_API_KEY=your_groq_api_key_here
```

### 5️⃣ Run the Flask server
```sh
python app.py
```
Access the chatbot at: `http://127.0.0.1:5000/`

## 🚀 Deploy on Vercel
1. Install Vercel CLI:
   ```sh
   npm install -g vercel
   ```
2. Deploy the project:
   ```sh
   vercel --prod
   ```

## 🔗 Embed in Other Websites

### Option 1: Embed with `<iframe>`
```html
<iframe src="https://restro-gpt.vercel.app/" width="100%" height="600px" style="border:none;"></iframe>
```

### Option 2: Open Chatbot in a New Tab
```html
<a href="https://restro-gpt.vercel.app/" target="_blank">Chat with RestroGPT</a>
```

### Option 3: Floating Chat Button
```html
<button class="chatbot-button" onclick="window.open('https://restro-gpt.vercel.app/', '_blank', 'width=400,height=600');">💬 Chat</button>
```

## 📜 License
This project is licensed under the **MIT License**.

## 👨‍💻 Author
Developed by **Kaustubh** 🚀

---
💡 **Feel free to contribute!** Open a PR or raise an issue if you find a bug. 🚀
