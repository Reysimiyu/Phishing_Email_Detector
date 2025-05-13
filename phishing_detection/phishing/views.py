from django.shortcuts import render
from .forms import EmailAnalysisForm
from .models import PhishingEmail
import joblib
import language_tool_python

# Load the ML model and vectorizer
model = joblib.load("phishing_model/model.pkl")
vectorizer = joblib.load("phishing_model/vectorizer.pkl")
tool = language_tool_python.LanguageTool('en-US')

#home page
def Home(request):
    return render(request, 'phishing/home.html')

#email analysis function
def analyze_email(request):
    result = None
    grammar_issues = 0

    if request.method == "POST":
        # form = EmailAnalysisForm(request.POST)
        # if form.is_valid():
        
        sender = request.POST.get('sender_email')
        email = request.POST.get('email_body')
        urls = request.POST.get('url_links')
        
        # Grammar checking using LanguageTool
        if sender and email:
            grammar_issues = len(tool.check(email))

            # Combine all available text for prediction
            full_text = f"{sender} {email} {urls}"
            features = vectorizer.transform([full_text])
            prediction = model.predict(features)[0]

            # Handle string labels from the dataset
            if prediction == "Phishing Email":
                result = "Phishing"
            else:
                result = "Legitimate"

                # Save to database
            PhishingEmail.objects.create(
                sender_email=sender,
                email_body=email,
                url_links=urls,
                grammar_issues=grammar_issues,
                prediction=result
            )

        return render(request, "phishing/index.html", {
            "result": result,
            "grammar": grammar_issues
        })

    # else:
        # form = EmailAnalysisForm()

    return render(request, "phishing/index.html")


def dashboard(request):
    emails = PhishingEmail.objects.all().order_by('-created_at')
    phishing_count = emails.filter(prediction="Phishing").count()
    legit_count = emails.filter(prediction="Legitimate").count()

    return render(request, "phishing/dashboard.html", {
        "emails": emails,
        "phishing_count": phishing_count,
        "legit_count": legit_count,
        "chart_labels": ['Phishing', 'Legitimate'],
        "chart_data": [phishing_count, legit_count]
    })
