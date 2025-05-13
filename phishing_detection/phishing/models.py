from django.db import models

class PhishingEmail(models.Model):
    sender_email = models.EmailField()
    email_body = models.TextField()
    url_links = models.TextField(blank=True)
    grammar_issues = models.IntegerField(default=0)
    prediction = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender_email} - {self.prediction}"
