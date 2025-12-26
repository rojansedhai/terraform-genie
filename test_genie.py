import requests
import json
import os

# ==========================================
# CONFIGURATION
# ==========================================
# 1. Export your key first: export GENIE_API_KEY="your_key_here"
API_KEY = os.getenv("GENIE_API_KEY")

# 2. Update this URL after 'terraform apply'
API_URL = "Enter your API Gateway URL here" 
# ==========================================

if not API_KEY:
    raise ValueError("❌ Error: GENIE_API_KEY environment variable is not set.")

payload = {
    "description": "Create me a backup plan for an RDS instance with daily backups and a retention period of 7 days."
}

headers = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY
}

print(f"Testing API: {API_URL}...")
try:
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        print("\n✅ SUCCESS! Here is your Terraform Code:\n")
        print("------------------------------------------------")
        print(data['terraform_code'])
        print("------------------------------------------------")
    elif response.status_code == 403:
        print("\n❌ SECURITY CHECK PASSED: Access Forbidden (403).")
        print("Did you export the correct API Key?")
    else:
        print(f"\n❌ Error {response.status_code}: {response.text}")

except Exception as e:
    print(f"Connection Error: {e}")