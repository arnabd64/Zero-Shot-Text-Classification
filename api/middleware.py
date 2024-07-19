import secrets
import time
from typing import Awaitable, Callable

from fastapi import Request
from starlette.middleware.base import (BaseHTTPMiddleware,
                                       RequestResponseEndpoint)
from starlette.responses import Response


class ResponseTime(BaseHTTPMiddleware):

    """
    Adds a custom header that contains the time
    taken by the server to process the HTTP request
    and send the request to the client.
    """

    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
        start_time = time.perf_counter()
        response = await call_next(request)
        end_time = time.perf_counter()
        response.headers['X-Process-Time-Milliseconds'] = str(1000 * (end_time - start_time))
        return response
    

class ResponseID(BaseHTTPMiddleware):

    """
    Assigns a unique response id to every responses
    sent by the server
    """
    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
        response = await call_next(request)
        response.headers['X-Response-ID'] = secrets.token_hex(16)
        return response
