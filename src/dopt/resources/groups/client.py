# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_headers import remove_none_from_headers
from ...environment import DoptApiEnvironment
from ...errors.bad_request_error import BadRequestError
from ...errors.internal_server_error import InternalServerError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.bad_request_error_response_body import BadRequestErrorResponseBody
from ...types.internal_server_error_response_body import InternalServerErrorResponseBody
from ...types.unauthorized_error_response_body import UnauthorizedErrorResponseBody


class GroupsClient:
    def __init__(self, *, environment: DoptApiEnvironment = DoptApiEnvironment.DEFAULT, api_key: str):
        self._environment = environment
        self.api_key = api_key

    def identify_group(self, *, identifier: str, properties: typing.Dict[str, typing.Any]) -> None:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "identify/group"),
            json=jsonable_encoder({"identifier": identifier, "properties": properties}),
            headers=remove_none_from_headers({"X-Api-Key": self.api_key}),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(BadRequestErrorResponseBody, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(UnauthorizedErrorResponseBody, _response.json())  # type: ignore
            )
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic.parse_obj_as(InternalServerErrorResponseBody, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncGroupsClient:
    def __init__(self, *, environment: DoptApiEnvironment = DoptApiEnvironment.DEFAULT, api_key: str):
        self._environment = environment
        self.api_key = api_key

    async def identify_group(self, *, identifier: str, properties: typing.Dict[str, typing.Any]) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "identify/group"),
                json=jsonable_encoder({"identifier": identifier, "properties": properties}),
                headers=remove_none_from_headers({"X-Api-Key": self.api_key}),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(BadRequestErrorResponseBody, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(UnauthorizedErrorResponseBody, _response.json())  # type: ignore
            )
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic.parse_obj_as(InternalServerErrorResponseBody, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)