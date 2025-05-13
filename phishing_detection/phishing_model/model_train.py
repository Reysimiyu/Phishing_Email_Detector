import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Sample phishing emails dataset
data = pd.read_csv('phishing_model/Phishing_Email.csv')
data = data.dropna(subset=['Email Text'])


X = data['Email Text']
y = data['Email Type']

vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

print(f"Accuracy: {model.score(X_test, y_test)*100:.2f}%")

# Saving the model and vectorizer
joblib.dump(model, 'phishing_model/model.pkl')
joblib.dump(vectorizer, 'phishing_model/vectorizer.pkl')
