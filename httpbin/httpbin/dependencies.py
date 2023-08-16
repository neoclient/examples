from typing import Mapping

from neoclient import PreRequest

from .models import CookiesResponse, HeadersResponse, IpResponse, UserAgentResponse


def origin(response: IpResponse, /) -> str:
    return response.origin


def headers(response: HeadersResponse, /) -> Mapping[str, str]:
    return response.headers


def user_agent(response: UserAgentResponse, /) -> str:
    return response.user_agent


def cookies(response: CookiesResponse, /) -> Mapping[str, str]:
    return response.cookies


# NOTE: Parameter inference for `State` currently doesn't work (#162)
# AND cannot currently depend on the entire state (#161)
# state: State, path_params: Mapping[str, str] = PathParams(),
# def state_to_path_params(request: PreRequest) -> None:
#     print("state:", request.state)
#     print("path params:", request.path_params)
