import requests, json, sys

def get_json(url):
    try:
        return requests.get(url = url).json()
    except:
        print("Oooops! Problems on the way.\n{}".format(sys.exc_info()[0]))
        return 1
    
def save_json_to_file(json_returned, file_path):
    try:
        with open(file_path, 'w') as outfile:  
            json.dump(json_returned, outfile, indent=1)
        outfile.close()
    except:
        print("Oooops! Problems on the way.\n{}".format(sys.exc_info()[0]))
        return 1
    return 0

def decypher_message(overhead, message, letters_mapping):
    decyphered_message = ""
    try:
        for letter in message:
            if(letter in letters_mapping):
                decyphered_position = (letters_mapping.index(letter) - overhead)%26
                decyphered_message += letters_mapping[decyphered_position]
            elif(letter == " "):
                decyphered_message += " "
            else:
                decyphered_message += format(letter)
    except:
        print("Oooops! Problems on the way.\n{}".format(sys.exc_info()[0]))
        return 1
    return decyphered_message

def generate_shal():
    pass

def update_json(file_path, field, text):
    pass

if __name__ == "__main__":
    url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=12818de9bd8ad7cba554de3c9e391a3363311a6f"
    file_path = "answer.json"
    json_returned = get_json(url)
    letters_mapping = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    if(isinstance(json_returned,dict)):
        if(save_json_to_file(json_returned, file_path) == 0):
            decyphered_message = decypher_message(json_returned["numero_casas"], json_returned["cifrado"], letters_mapping)
            print("{}".format(decyphered_message))
        else:
            print("Error while trying to save the JSON file")
    else:
        print("Oooops! Error while trying to get the JSON")