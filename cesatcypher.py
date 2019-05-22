import requests, json

def get_json(url):
    return requests.get(url = url).json()   

def save_json_to_file(json_returned, file_path):
    with open(file_path, 'w') as outfile:  
        json.dump(json_returned, outfile)

if __name__ == "__main__":
    url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=12818de9bd8ad7cba554de3c9e391a3363311a6f"
    file_path = "return.json"
    json_returned = get_json(url)
    save_json_to_file(json_returned, file_path)