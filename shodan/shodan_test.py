import os
import shodan

key = os.environ.get("SHODAN_API_KEY")
print("API key present?:", bool(key))
if not key:
    print("Set SHODAN_API_KEY and retry.")
    raise SystemExit(1)

api = shodan.Shodan(key)
try:
    info = api.info()
    print("Account info fetched OK:")
    print("  Plan:", info.get("plan"))
    print("  Credits:", info.get("credits"))
except Exception as e:
    print("ERROR TYPE:", type(e).__name__)
    print("ERROR:", e)
