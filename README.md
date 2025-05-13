# 🛡️ EmailGuard: AI-Based Phishing Email Detection System

EmailGuard is a web-based application that uses machine learning and natural language processing to detect phishing emails in real time. 
Users can input sender details,email content, and URLs to analyze whether the email is **Phishing** or **Legitimate**. 
The system also logs grammar issues and visualizes statistics through a modern dashboard.

---

## 🚀 Features

- 🔍 Analyze email content, sender, and URLs
- 🧠 ML model trained on real-world phishing dataset
- 📝 Grammar checking using `language-tool-python`
- 📊 Dashboard with Chart.js visualizations
- 📬 Admin alert via email when phishing is detected
- 🖥️ Responsive UI built with Bootstrap
- 🔐 Secure and scalable Django backend

---

## 📦 Tech Stack

- **Backend**: Python, Django
- **ML**: Scikit-learn, TF-IDF, Logistic Regression
- **Grammar Analysis**: LanguageTool (Python)
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Visualization**: Chart.js
- **Deployment**: Localhost (Heroku/AWS optional)

---

## 📁 Project Structure

```
phishing_detection/
├── detection/                # Django app with views, models, templates
├── phishing_detection/       # Project settings and URLs
├── static/                   # Static files (CSS, JS)
├── templates/                # HTML templates
├── model.pkl                 # Trained ML model
├── vectorizer.pkl            # TF-IDF vectorizer
├── requirements.txt
└── manage.py
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/Reysimiyu/Phishing_Email_Detector.git
cd phishing_detection
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations and run the server:

```bash
python manage.py migrate
python manage.py runserver
```

---

## 🧪 Usage

1. Visit `http://127.0.0.1:8000/`
2. Use the navigation bar to:
   - Analyze emails
   - View detection results
   - Explore dashboard analytics
3. Legitimate or Phishing results are displayed instantly.


---

## 📊 Sample Dataset

- Dataset: `Phishing_Email.csv`
- Columns: `Email Text`, `Email Type`
- Labels: `Phishing Email`, `Safe Email`

---

## 📜 License

MIT License — feel free to use, modify, and share.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

---

## 📫 Contact

Developed by Reinhard Siminyu  
Email: simiyurey@gmail.com  
GitHub: github.com/Reysimiyu(https://github.com/Reysimiyu)
