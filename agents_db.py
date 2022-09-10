import requests

def list_agent():
    url = "https://ccai.epacific.net/api/v1/accounts/1/agents"

    header = {
        "api_access_token": "78ARRSX2ofwSwVJJGivJiBTP"
    }
    
    response = requests.get(url, headers=header)

    data = response.json()

    return data


if __name__ == "__main__":
    print(list_agent())