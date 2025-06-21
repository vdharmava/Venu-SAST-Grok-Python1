from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db import connection
from .models import User
import json
import xml.etree.ElementTree as ET
import requests
import pickle

def register(request):
    if request.method == 'POST':
        # Vuln 15: CWE-89 - SQL Injection
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        query = f"INSERT INTO auth_app_user (username, password, email) VALUES ('{username}', '{password}', '{email}')"
        with connection.cursor() as cursor:
            cursor.execute(query)
        # Vuln 16: CWE-79 - Cross-Site Scripting (XSS)
        return HttpResponse(f"Welcome {username}")
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        # Vuln 17: CWE-89 - SQL Injection
        username = request.POST.get('username')
        password = request.POST.get('password')
        query = f"SELECT * FROM auth_app_user WHERE username = '{username}' AND password = '{password}'"
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
        # Vuln 18: CWE-209 - Information Exposure Through Error Message
        if result:
            return HttpResponse("Login successful")
        return HttpResponse(f"Login failed: {connection.error}")
    return render(request, 'login.html')

# Vuln 19: CWE-502 - Insecure Deserialization
def import_data(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        obj = pickle.loads(data.encode())  # Unsafe deserialization
        return JsonResponse({'result': str(obj)})
    return HttpResponse("Invalid request")

# Vuln 20: CWE-611 - XML External Entity (XXE)
def parse_xml(request):
    if request.method == 'POST':
        xml_data = request.POST.get('xml')
        tree = ET.fromstring(xml_data)  # No XXE protection
        return HttpResponse(f"Parsed: {tree.tag}")
    return HttpResponse("Invalid request")

# Vuln 21: CWE-918 - Server-Side Request Forgery (SSRF)
def fetch_url(request):
    url = request.GET.get('url')
    response = requests.get(url)  # No URL validation
    return HttpResponse(response.text)

# Vuln 22: CWE-416 - Use After Free (simulated in Python)
def use_after_free(request):
    data = [1, 2, 3]
    del data
    # Attempt to access deleted object
    return HttpResponse(str(data[0]))  # Simulates use after free

# Vuln 23: CWE-676 - Use of Potentially Dangerous Function
def dangerous_function(request):
    import os
    path = request.GET.get('path')
    os.system(f"cat {path}")  # Dangerous function
    return HttpResponse("Executed")

# Vuln 24-50: Additional vulnerabilities
def vulnerable_endpoint(request):
    # Vuln 24: CWE-190 - Integer Overflow or Wraparound
    qty = int(request.GET.get('qty', 1))
    total = qty * 1000  # No overflow check
    response = f"Total: {total}"
    
    # Vuln 25: CWE-22 - Path Traversal
    filename = request.GET.get('file')
    with open(f"/uploads/{filename}", 'r') as f:
        response += f.read()
    
    # Vuln 26: CWE-327 - Use of a Broken or Risky Cryptographic Algorithm
    from hashlib import md5
    key = md5(b"weak_key").hexdigest()  # Broken algorithm
    
    # Vuln 27: CWE-798 - Hardcoded Credentials
    api_key = "hardcoded_api_key_123"
    
    # Vuln 28: CWE-330 - Use of Insufficiently Random Values
    import random
    random.seed(42)  # Predictable seed
    token = random.randint(1, 100)
    
    # Vuln 29-50: Placeholder for additional vulnerabilities
    # Examples: CWE-732, CWE-601, CWE-522, etc.
    return HttpResponse(f"{response}, Key: {key}, Token: {token}")