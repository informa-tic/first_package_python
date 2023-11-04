import requests

def give_me_a_joke():
    try:
        return requests.get("https://api.chucknorris.io/jokes/random").json().get("value")
    except Exception as ex:
        return "no joke for me"

print(give_me_a_joke())