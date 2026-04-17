# Vulnerable Container Security Report
## ThousandEyes API Integration — Security Research Project

---

## 1. Project Overview

This project demonstrates the implementation of a vulnerable Docker container
that simulates API calls to the ThousandEyes v6 API. The container is built
with intentional security vulnerabilities for educational and research purposes.

**API Reference:** https://developer.thousandeyes.com/v6/
**Base API URL:** https://api.thousandeyes.com/v6

> Note: A ThousandEyes trial account requires a corporate email address.
> The ThousandEyes API v6 response format was replicated using official
> documentation at developer.thousandeyes.com/v6 to demonstrate API
> integration functionality.

---

## 2. API Implementation

### Endpoint Used
GET /v6/tests.json

### Sample API Response
The /tests endpoint returns all configured tests:

```json
{
  "tests": [
    {
      "testId": 1001,
      "testName": "Google DNS Test",
      "type": "dns-server",
      "interval": 300,
      "domain": "google.com",
      "enabled": 1
    }
  ]
}