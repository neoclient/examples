from typing import Mapping, Optional, Sequence

import neoclient
from neoclient import Header, Path, follow_redirects, Response, middleware, State
from neoclient.decorators import request_depends
from neoclient.dependencies import status_code

from .dependencies import cookies, headers, origin, state_to_path_params, user_agent
from .models import FullResponse, PartialResponse
from .middleware import basic_auth

# def log_request(call_next, request):
#     print("Sending Request:", request.__dict__)

#     return call_next(request)


# @neoclient.middleware(log_request)
@neoclient.base_url("https://httpbin.org/")
class HttpBin(neoclient.Service):
    # <HTTP Methods>: Testing different HTTP verbs

    @neoclient.delete("/delete")
    def delete(self) -> FullResponse:
        ...

    @neoclient.get("/get")
    def get(self, **params: str) -> PartialResponse:
        ...

    @neoclient.patch("/patch")
    def patch(self) -> FullResponse:
        ...

    @neoclient.post("/post")
    def post(self) -> FullResponse:
        ...

    # </HTTP Methods>

    # <Auth>: Auth methods

    # TODO: Currently blocked/related by/to: #158, #161, #162
    # @request_depends(state_to_path_params)
    # @middleware(basic_auth)
    # @neoclient.get("/basic-auth/{user}/{passwd}")
    # def basic_auth(self, user: str = State(), passwd: str = State()) -> Response:
    #     ...

    # TODO: Implement remaining auth operations

    # </Auth>

    # <Status codes>: Generate responses with given status code

    @neoclient.delete("/status/{codes}", response=status_code)
    def status_delete(self, codes: Sequence[str] = Path(delimiter=",")) -> int:
        """Return status code or random status code if more than one are given"""
        ...

    @neoclient.get("/status/{codes}", response=status_code)
    def status_get(self, codes: Sequence[str] = Path(delimiter=",")) -> int:
        """Return status code or random status code if more than one are given"""
        ...

    @neoclient.patch("/status/{codes}", response=status_code)
    def status_patch(self, codes: Sequence[str] = Path(delimiter=",")) -> int:
        """Return status code or random status code if more than one are given"""
        ...

    @neoclient.post("/status/{codes}", response=status_code)
    def status_post(self, codes: Sequence[str] = Path(delimiter=",")) -> int:
        """Return status code or random status code if more than one are given"""
        ...

    @neoclient.put("/status/{codes}", response=status_code)
    def status_put(self, codes: Sequence[str] = Path(delimiter=",")) -> int:
        """Return status code or random status code if more than one are given"""
        ...

    # </Status codes>

    # <Request inspection>: Inspect the request data

    @neoclient.get("/headers", response=headers)
    def headers(self) -> Mapping[str, str]:
        """Return the incoming request's HTTP headers."""
        ...

    @neoclient.get("/ip", response=origin)
    def ip(self) -> str:
        """Returns the requester's IP Address."""
        ...

    # TODO: Pydantic models currently broken (#150)
    # @neoclient.get("/user-agent", response=user_agent)
    # def user_agent(self) -> str:
    #     """ Return the incoming requests's User-Agent header. """
    #     ...

    # </Request inspection>

    # <Response inspection>: Inspect the response data like caching and headers

    # TODO: Body resolver currently very naive (#59)
    # @neoclient.get("/cache")
    # def cache(
    #     self,
    #     *,
    #     if_modified_since: Optional[str] = Header(default=None),
    #     if_none_match: Optional[str] = Header(default=None),
    # ) -> Optional[GetResponse]:
    #     ...

    @neoclient.get("/cache/{value}")
    def cache_set(self, value: int, /) -> PartialResponse:
        """Sets a Cache-Control header for n seconds."""
        ...

    # TODO: Body resolver currently very naive (#59)
    # @neoclient.get("/etag/{etag}")
    # def etag(
    #     self,
    #     etag: str,
    #     /,
    #     *,
    #     if_none_match: Optional[str] = Header(default=None),
    #     if_match: Optional[str] = Header(default=None),
    # ) -> Optional[GetResponse]:
    #     ...

    @neoclient.get("/response-headers")
    def response_headers_get(self, **params: str) -> Mapping[str, str]:
        ...

    @neoclient.post("/response-headers")
    def response_headers_post(self, **params: str) -> Mapping[str, str]:
        ...

    # </Response inspection>

    # <Response formats>: Returns responses in different data formats
    # TODO
    # </Response formats>

    # <Dynamic data>: Generates random and dynamic data
    # TODO
    # </Dynamic data>

    # <Cookies>: Creates, reads and deletes Cookies

    @neoclient.get("/cookies", response=cookies)
    def cookies_list(self) -> Mapping[str, str]:
        """Returns cookie data."""
        ...

    @follow_redirects(True)
    @neoclient.get("/cookies/delete", response=cookies)
    def cookies_delete(self, *cookies: str) -> Mapping[str, str]:
        """Deletes cookie(s) as provided by the query string and redirects to cookie list."""
        ...

    @follow_redirects(True)
    @neoclient.get("/cookies/set", response=cookies)
    def cookies_set(self, **cookies: str) -> Mapping[str, str]:
        """Sets cookie(s) as provided by the query string and redirects to cookie list."""
        ...

    # </Cookies>

    # <Images>: Returns different image formats
    # TODO
    # </Images>

    # <Redirects>: Returns different redirect responses
    # TODO
    # </Redirects>

    # <Anything>: Returns anything that is passed to request
    # TODO
    # </Anything>
