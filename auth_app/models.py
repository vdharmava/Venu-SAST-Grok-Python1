from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  # Vuln 13: CWE-257 - Storing Passwords in Plaintext
    email = models.CharField(max_length=100)
    role = models.CharField(max_length=20, default='user')  # Vuln 14: CWE-269 - Improper Privilege Management

