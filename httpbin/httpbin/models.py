from dataclasses import dataclass
from pydantic import BaseModel, Field
from typing import Any, Mapping, Optional


class FullResponse(BaseModel):
    args: Mapping[str, str]
    data: str
    files: dict  # TODO: type me
    form: dict  # TODO: type me
    headers: Mapping[str, str]
    json_: Optional[Any] = Field(alias="json")  # TODO: type me
    origin: str
    url: str


class GetResponse(BaseModel):
    args: Mapping[str, str]
    headers: Mapping[str, str]
    origin: str
    url: str


@dataclass
class IpResponse:
    origin: str


@dataclass
class HeadersResponse:
    headers: Mapping[str, str]


class UserAgentResponse(BaseModel):
    user_agent: str = Field(alias="user-agent")
