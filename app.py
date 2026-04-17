from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Hardcoded credentials - intentional vulnerability
API_TOKEN = "mock-token-12345-thousandeyes"
BASE_URL = "https://api.thousandeyes.com/v6"

def get_tests():
    # Simulated ThousandEyes API response
    # Based on official API docs: developer.thousandeyes.com/v6
    mock_response = {
        "tests": [
            {
                "testId": 1001,
                "testName": "Google DNS Test",
                "type": "dns-server",
                "interval": 300,
                "domain": "google.com",
                "enabled": 1,
                "createdDate": "2024-01-15 10:00:00",
                "modifiedDate": "2024-03-01 12:00:00",
                "alertsEnabled": 1
            },
            {
                "testId": 1002,
                "testName": "Cloudflare HTTP Test",
                "type": "http-server",
                "interval": 60,
                "domain": "cloudflare.com",
                "enabled": 1,
                "createdDate": "2024-01-20 09:00:00",
                "modifiedDate": "2024-03-05 11:00:00",
                "alertsEnabled": 1
            },
            {
                "testId": 1003,
                "testName": "GitHub Page Load Test",
                "type": "page-load",
                "interval": 900,
                "domain": "github.com",
                "enabled": 1,
                "createdDate": "2024-02-01 08:00:00",
                "modifiedDate": "2024-03-10 14:00:00",
                "alertsEnabled": 0
            },
            {
                "testId": 1004,
                "testName": "AWS Network Test",
                "type": "network",
                "interval": 120,
                "domain": "aws.amazon.com",
                "enabled": 1,
                "createdDate": "2024-02-10 07:00:00",
                "modifiedDate": "2024-03-12 09:00:00",
                "alertsEnabled": 1
            }
        ]
    }
    return mock_response

@app.route("/")
def home():
    return """
    <html>
    <head><title>ThousandEyes API - Test Results</title></head>
    <body style="font-family: Arial; background: #1a1a2e; color: #eee; padding: 40px;">
        <h1 style="color: #e94560;">ThousandEyes API Integration</h1>
        <p>Vulnerable Container Demo — Security Research Project</p>
        <a href="/tests" style="background:#e94560; color:white; padding:10px 20px;
        text-decoration:none; border-radius:5px;">View All Tests</a>
        <br><br>
        <a href="/health" style="background:#0f3460; color:white; padding:10px 20px;
        text-decoration:none; border-radius:5px;">Health Check</a>
    </body>
    </html>
    """

@app.route("/tests")
def list_tests():
    data = get_tests()
    return jsonify(data)

@app.route("/health")
def health():
    return jsonify({
        "status": "running",
        "api_token": API_TOKEN,
        "base_url": BASE_URL
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)