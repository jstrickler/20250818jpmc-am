import requests

URL = "https://github.com/jstrickler/20250818jpmc-am/blob/main/c2f_simple.py"

response = requests.get(URL)
if response.ok:  # status code < 400
    print(response.text)