from neoclient import get, Body


def response(headers=Body(embed=True)):
    return headers


@get("https://httpbin.org/headers", response=response)
def headers():
    ...
