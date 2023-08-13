from typing import Mapping
from .models import HeadersResponse, IpResponse, UserAgentResponse


def origin(response: IpResponse, /) -> str:
    return response.origin


def headers(response: HeadersResponse, /) -> Mapping[str, str]:
    return response.headers


def user_agent(response: UserAgentResponse, /) -> str:
    return response.user_agent
