import requests, os

key = os.getenv("API_KEY")

default_params= {
    "api_key" : key
}

#url = https://api.nasa.gov/planetary/apod

def get_image_info(date="2021-12-07"):
    default_params["date"] = date
    response = requests.get(f"https://api.nasa.gov/planetary/apod", params=default_params)
    response_json = response.json()
    return response_json['url'], response_json['explanation']