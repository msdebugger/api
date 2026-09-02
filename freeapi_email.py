import requests
import json

def get_user_email():
    url = "https://api.freeapi.app/api/v1/public/randomusers"
    response = requests.get(url)

    data = response.json()

    print(json.dumps(data, indent=4))


    if data["success"] and "data" in data:
        email = data["data"]["data"][0]["email"]
        return email

    else:
        raise Exception("Failed to fetch user data")

get_user_email()


def main():

    try:
        email = get_user_email()
        print(f"Email: {email}")

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()