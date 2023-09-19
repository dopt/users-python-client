# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...errors.bad_request_error import BadRequestError
from ...errors.internal_server_error import InternalServerError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.bad_request_error_response_body import BadRequestErrorResponseBody
from ...types.identify_batch_request_body_item import IdentifyBatchRequestBodyItem
from ...types.identify_batch_response_body import IdentifyBatchResponseBody
from ...types.identify_user_request_body_groups_item import IdentifyUserRequestBodyGroupsItem
from ...types.internal_server_error_response_body import InternalServerErrorResponseBody
from ...types.unauthorized_error_response_body import UnauthorizedErrorResponseBody

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class UsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def identify_user(
        self,
        *,
        identifier: str,
        properties: typing.Dict[str, typing.Any],
        groups: typing.Optional[typing.List[IdentifyUserRequestBodyGroupsItem]] = OMIT,
    ) -> None:
        """
        Identifies a user to the Dopt user API

        Parameters:
            - identifier: str. <span style="white-space: nowrap">`non-empty`</span>

            - properties: typing.Dict[str, typing.Any].

            - groups: typing.Optional[typing.List[IdentifyUserRequestBodyGroupsItem]].
        """
        _request: typing.Dict[str, typing.Any] = {"identifier": identifier, "properties": properties}
        if groups is not OMIT:
            _request["groups"] = groups
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "identify"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
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

    def identify_users(self, *, request: typing.List[IdentifyBatchRequestBodyItem]) -> IdentifyBatchResponseBody:
        """
        Identifies users to the Dopt users API (limited to 100 users per request)

        Parameters:
            - request: typing.List[IdentifyBatchRequestBodyItem].
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "identify/batch"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(IdentifyBatchResponseBody, _response.json())  # type: ignore
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


class AsyncUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def identify_user(
        self,
        *,
        identifier: str,
        properties: typing.Dict[str, typing.Any],
        groups: typing.Optional[typing.List[IdentifyUserRequestBodyGroupsItem]] = OMIT,
    ) -> None:
        """
        Identifies a user to the Dopt user API

        Parameters:
            - identifier: str. <span style="white-space: nowrap">`non-empty`</span>

            - properties: typing.Dict[str, typing.Any].

            - groups: typing.Optional[typing.List[IdentifyUserRequestBodyGroupsItem]].
        """
        _request: typing.Dict[str, typing.Any] = {"identifier": identifier, "properties": properties}
        if groups is not OMIT:
            _request["groups"] = groups
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "identify"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
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

    async def identify_users(self, *, request: typing.List[IdentifyBatchRequestBodyItem]) -> IdentifyBatchResponseBody:
        """
        Identifies users to the Dopt users API (limited to 100 users per request)

        Parameters:
            - request: typing.List[IdentifyBatchRequestBodyItem].
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "identify/batch"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(IdentifyBatchResponseBody, _response.json())  # type: ignore
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
