import requests, json

def get_json(url):
    r = requests.get(url = url)
    data = r.json
    print("{}".format(json.dumps(data)))

if __name__ == "__main__":
    url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=12818de9bd8ad7cba554de3c9e391a3363311a6f"
    get_json(url)