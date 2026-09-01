import requests

def fetch_country():

    url = "https://api.freeapi.app/api/v1/public/randomusers"

    response = requests.get(url)

    data = response.json()

    # print(data)

    if data["success"] and "data" in data:
        country = data["data"]["data"][0]["location"]["country"]
        return country

    else:
        raise Exception("Failed to fetch user data")


def main():

    try:
        country = fetch_country()
        print(f"Country: {country}")

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()