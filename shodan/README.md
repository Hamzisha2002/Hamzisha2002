# Shodan API Demo

This folder contains scripts that demonstrate safe, read-only use of the Shodan API.

## Files
- **shodan_test.py** → Verifies that the API key works and prints account info.
- **shodan_fetch.py** → Performs a safe search query ("apache") and fetches limited metadata.
- **shodan_output.txt** → Sample output of the fetch script.
- **shodan_api_info.txt** → API/account information details.

## How to run
1. Export your Shodan API key as an environment variable:
   - Git Bash:
     ```bash
     export SHODAN_API_KEY="your_api_key"
     ```
   - PowerShell:
     ```powershell
     $env:SHODAN_API_KEY="your_api_key"
     ```
2. Run the scripts:
   ```bash
   python shodan_test.py
   python shodan_fetch.py > shodan_output.txt
