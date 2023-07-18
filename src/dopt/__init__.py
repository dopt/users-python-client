# This file was auto-generated by Fern from our API Definition.

from .environment import DoptApiEnvironment
from .errors import BadRequestError, InternalServerError, UnauthorizedError
from .resources import groups, users
from .types import (
    BadRequestErrorResponseBody,
    BadRequestErrorResponseBodyCode,
    IdentifyBatchRequestBody,
    IdentifyBatchRequestBodyItem,
    IdentifyBatchRequestBodyItemGroupsItem,
    IdentifyBatchResponseBody,
    IdentifyRequestBody,
    IdentifyRequestParams,
    IdentifySegmentRequestBody,
    IdentifySegmentRequestBodyIdentifySegmentRequestBody,
    IdentifySegmentResponseBody,
    IdentifyUserRequestBodyGroupsItem,
    InternalServerErrorResponseBody,
    NotFoundErrorResponseBody,
    SegmentCommon,
    SegmentGroup,
    SegmentIdentify,
    TimeoutErrorResponseBody,
    UnauthorizedErrorResponseBody,
)

__all__ = [
    "BadRequestError",
    "BadRequestErrorResponseBody",
    "BadRequestErrorResponseBodyCode",
    "DoptApiEnvironment",
    "IdentifyBatchRequestBody",
    "IdentifyBatchRequestBodyItem",
    "IdentifyBatchRequestBodyItemGroupsItem",
    "IdentifyBatchResponseBody",
    "IdentifyRequestBody",
    "IdentifyRequestParams",
    "IdentifySegmentRequestBody",
    "IdentifySegmentRequestBodyIdentifySegmentRequestBody",
    "IdentifySegmentResponseBody",
    "IdentifyUserRequestBodyGroupsItem",
    "InternalServerError",
    "InternalServerErrorResponseBody",
    "NotFoundErrorResponseBody",
    "SegmentCommon",
    "SegmentGroup",
    "SegmentIdentify",
    "TimeoutErrorResponseBody",
    "UnauthorizedError",
    "UnauthorizedErrorResponseBody",
    "groups",
    "users",
]