# Shodan API Demo

This folder contains scripts and output files demonstrating safe use of the **Shodan API**.

## 📂 Files
- **shodan_test.py** → Verifies that the API key is set and prints account info (plan, credits).
- **shodan_fetch.py** → Fetches certificate/host metadata from Shodan using a sample query.
- **shodan_test_output.txt** → Output from running `shodan_test.py` (shows API key is present and account info).
- **shodan_output.txt** → Example output of `shodan_fetch.py` with a test query.

## 🚀 How to Run
1. **Set your Shodan API key** (don’t hardcode it in scripts):
   - **Git Bash**:
     ```bash
     export SHODAN_API_KEY="your_api_key_here"
     ```
   - **PowerShell**:
     ```powershell
     $env:SHODAN_API_KEY="your_api_key_here"
     ```

2. **Run the scripts**:
   ```bash
   # Test your key and see account info
   python shodan_test.py

   # Fetch data and save to output file
   python shodan_fetch.py > shodan_output.txt

