from neoclient import Service, base_url, follow_redirects, get


@base_url("https://httpbin.org/")
class HttpBin(Service):
    @follow_redirects(True)
    @get("/cookies/set")
    def set_cookies(self, **cookies: str):
        ...


httpbin: HttpBin = HttpBin()

# d = set_cookies(name="sam")
