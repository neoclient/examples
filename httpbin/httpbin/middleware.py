from neoclient import Request, Response
from neoclient.typing import CallNext
from neoclient.auths import Auth, BasicAuth


def basic_auth(call_next: CallNext, request: Request, /) -> Response:
    user: str = request.state.user
    passwd: str = request.state.passwd

    auth: Auth = BasicAuth(user, passwd)

    request = auth.auth(request)

    return call_next(request)
