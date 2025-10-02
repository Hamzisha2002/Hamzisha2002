import os
import shodan

def main():
    api_key = os.environ.get("SHODAN_API_KEY")
    if not api_key:
        print("ERROR: SHODAN_API_KEY environment variable not set.")
        print("In Git Bash run: export SHODAN_API_KEY=your_key_here")
        return

    api = shodan.Shodan(api_key)
    try:
        query = "apache"   # example search
        results = api.search(query)

        print(f"Results found: {results['total']}")
        print("Showing up to 5 results:")
        for service in results['matches'][:5]:
            print("-----------")
            print("IP:", service.get('ip_str'))
            print("Port:", service.get('port'))
            print("Org:", service.get('org', 'n/a'))
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()


