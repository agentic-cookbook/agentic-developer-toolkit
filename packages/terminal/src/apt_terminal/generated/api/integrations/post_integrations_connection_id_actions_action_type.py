from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.integration_action_request_type_0 import IntegrationActionRequestType0
from ...models.integration_action_request_type_1 import IntegrationActionRequestType1
from ...models.integration_action_result import IntegrationActionResult
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union



def _get_kwargs(
    connection_id: str,
    action_type: str,
    *,
    body: Union['IntegrationActionRequestType0', 'IntegrationActionRequestType1'],
    idempotency_key: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/integrations/{connection_id}/actions/{action_type}".format(connection_id=connection_id,action_type=action_type,),
    }

    _kwargs["json"]: dict[str, Any]
    if isinstance(body, IntegrationActionRequestType0):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()



    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[IntegrationActionResult, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = IntegrationActionResult.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ProblemDetails.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = ProblemDetails.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = ProblemDetails.from_dict(response.json())



        return response_422

    if response.status_code == 503:
        response_503 = ProblemDetails.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[IntegrationActionResult, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    connection_id: str,
    action_type: str,
    *,
    client: AuthenticatedClient,
    body: Union['IntegrationActionRequestType0', 'IntegrationActionRequestType1'],
    idempotency_key: Union[Unset, str] = UNSET,

) -> Response[Union[IntegrationActionResult, ProblemDetails]]:
    """ Act as the user (outbound action)

     Performs one outbound action (e.g. send an email, post a status) as the connection, and records
    exactly one action-log row. The provider is derived from the connection (never in the URL). 404 when
    not the caller's; 422 when no action handler is registered for its provider:actionType; 400 on an
    unknown actionType or invalid body. An optional `Idempotency-Key` header makes a repeat collapse
    onto the first row (no re-perform).

    Args:
        connection_id (str):
        action_type (str):
        idempotency_key (Union[Unset, str]):
        body (Union['IntegrationActionRequestType0', 'IntegrationActionRequestType1']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[IntegrationActionResult, ProblemDetails]]
     """


    kwargs = _get_kwargs(
        connection_id=connection_id,
action_type=action_type,
body=body,
idempotency_key=idempotency_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    connection_id: str,
    action_type: str,
    *,
    client: AuthenticatedClient,
    body: Union['IntegrationActionRequestType0', 'IntegrationActionRequestType1'],
    idempotency_key: Union[Unset, str] = UNSET,

) -> Optional[Union[IntegrationActionResult, ProblemDetails]]:
    """ Act as the user (outbound action)

     Performs one outbound action (e.g. send an email, post a status) as the connection, and records
    exactly one action-log row. The provider is derived from the connection (never in the URL). 404 when
    not the caller's; 422 when no action handler is registered for its provider:actionType; 400 on an
    unknown actionType or invalid body. An optional `Idempotency-Key` header makes a repeat collapse
    onto the first row (no re-perform).

    Args:
        connection_id (str):
        action_type (str):
        idempotency_key (Union[Unset, str]):
        body (Union['IntegrationActionRequestType0', 'IntegrationActionRequestType1']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[IntegrationActionResult, ProblemDetails]
     """


    return sync_detailed(
        connection_id=connection_id,
action_type=action_type,
client=client,
body=body,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    connection_id: str,
    action_type: str,
    *,
    client: AuthenticatedClient,
    body: Union['IntegrationActionRequestType0', 'IntegrationActionRequestType1'],
    idempotency_key: Union[Unset, str] = UNSET,

) -> Response[Union[IntegrationActionResult, ProblemDetails]]:
    """ Act as the user (outbound action)

     Performs one outbound action (e.g. send an email, post a status) as the connection, and records
    exactly one action-log row. The provider is derived from the connection (never in the URL). 404 when
    not the caller's; 422 when no action handler is registered for its provider:actionType; 400 on an
    unknown actionType or invalid body. An optional `Idempotency-Key` header makes a repeat collapse
    onto the first row (no re-perform).

    Args:
        connection_id (str):
        action_type (str):
        idempotency_key (Union[Unset, str]):
        body (Union['IntegrationActionRequestType0', 'IntegrationActionRequestType1']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[IntegrationActionResult, ProblemDetails]]
     """


    kwargs = _get_kwargs(
        connection_id=connection_id,
action_type=action_type,
body=body,
idempotency_key=idempotency_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    connection_id: str,
    action_type: str,
    *,
    client: AuthenticatedClient,
    body: Union['IntegrationActionRequestType0', 'IntegrationActionRequestType1'],
    idempotency_key: Union[Unset, str] = UNSET,

) -> Optional[Union[IntegrationActionResult, ProblemDetails]]:
    """ Act as the user (outbound action)

     Performs one outbound action (e.g. send an email, post a status) as the connection, and records
    exactly one action-log row. The provider is derived from the connection (never in the URL). 404 when
    not the caller's; 422 when no action handler is registered for its provider:actionType; 400 on an
    unknown actionType or invalid body. An optional `Idempotency-Key` header makes a repeat collapse
    onto the first row (no re-perform).

    Args:
        connection_id (str):
        action_type (str):
        idempotency_key (Union[Unset, str]):
        body (Union['IntegrationActionRequestType0', 'IntegrationActionRequestType1']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[IntegrationActionResult, ProblemDetails]
     """


    return (await asyncio_detailed(
        connection_id=connection_id,
action_type=action_type,
client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
