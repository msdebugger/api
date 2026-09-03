import requests
import json

def fetch_user_contact():
    url = "https://api.freeapi.app/api/v1/public/randomusers"
    response = requests.get(url)
    data = response.json()
    print(json.dumps(data, indent=4))
    
    if data["success"] and "data" in data:
        contact = data["data"]["data"][0]["phone"]
        return contact    
    else:
        raise Exception("Failed to fetch user data")


fetch_user_contact()

def main():

    try:
        contact = fetch_user_contact()
        print(f"Contact: {contact}")

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()