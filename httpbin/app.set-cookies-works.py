from neoclient import get, follow_redirects


@follow_redirects(True)
@get("https://httpbin.org/cookies/set")
def set_cookies(**cookies: str):
    ...


# d = set_cookies(name="sam")
