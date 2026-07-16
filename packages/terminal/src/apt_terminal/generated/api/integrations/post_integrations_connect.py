from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.integration_connect_request_type_0 import IntegrationConnectRequestType0
from ...models.integration_connect_request_type_1 import IntegrationConnectRequestType1
from ...models.integration_connect_request_type_2 import IntegrationConnectRequestType2
from ...models.integration_connect_request_type_3 import IntegrationConnectRequestType3
from ...models.integration_connect_request_type_4 import IntegrationConnectRequestType4
from ...models.integration_connection import IntegrationConnection
from ...models.problem_details import ProblemDetails
from typing import cast
from typing import cast, Union



def _get_kwargs(
    *,
    body: Union['IntegrationConnectRequestType0', 'IntegrationConnectRequestType1', 'IntegrationConnectRequestType2', 'IntegrationConnectRequestType3', 'IntegrationConnectRequestType4'],

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/integrations/connect",
    }

    _kwargs["json"]: dict[str, Any]
    if isinstance(body, IntegrationConnectRequestType0):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, IntegrationConnectRequestType1):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, IntegrationConnectRequestType2):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, IntegrationConnectRequestType3):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()



    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[IntegrationConnection, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = IntegrationConnection.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ProblemDetails.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[IntegrationConnection, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union['IntegrationConnectRequestType0', 'IntegrationConnectRequestType1', 'IntegrationConnectRequestType2', 'IntegrationConnectRequestType3', 'IntegrationConnectRequestType4'],

) -> Response[Union[IntegrationConnection, ProblemDetails]]:
    """ Connect an integration (polymorphic by auth method)

     Finishes any auth method's connect flow and persists the connection under the target ecosystem
    `ecosystemId` the client names; the caller must manage it (404/403 otherwise). Returns the redacted
    connection (tokens never echoed).

    Args:
        body (Union['IntegrationConnectRequestType0', 'IntegrationConnectRequestType1',
            'IntegrationConnectRequestType2', 'IntegrationConnectRequestType3',
            'IntegrationConnectRequestType4']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[IntegrationConnection, ProblemDetails]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: Union['IntegrationConnectRequestType0', 'IntegrationConnectRequestType1', 'IntegrationConnectRequestType2', 'IntegrationConnectRequestType3', 'IntegrationConnectRequestType4'],

) -> Optional[Union[IntegrationConnection, ProblemDetails]]:
    """ Connect an integration (polymorphic by auth method)

     Finishes any auth method's connect flow and persists the connection under the target ecosystem
    `ecosystemId` the client names; the caller must manage it (404/403 otherwise). Returns the redacted
    connection (tokens never echoed).

    Args:
        body (Union['IntegrationConnectRequestType0', 'IntegrationConnectRequestType1',
            'IntegrationConnectRequestType2', 'IntegrationConnectRequestType3',
            'IntegrationConnectRequestType4']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[IntegrationConnection, ProblemDetails]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union['IntegrationConnectRequestType0', 'IntegrationConnectRequestType1', 'IntegrationConnectRequestType2', 'IntegrationConnectRequestType3', 'IntegrationConnectRequestType4'],

) -> Response[Union[IntegrationConnection, ProblemDetails]]:
    """ Connect an integration (polymorphic by auth method)

     Finishes any auth method's connect flow and persists the connection under the target ecosystem
    `ecosystemId` the client names; the caller must manage it (404/403 otherwise). Returns the redacted
    connection (tokens never echoed).

    Args:
        body (Union['IntegrationConnectRequestType0', 'IntegrationConnectRequestType1',
            'IntegrationConnectRequestType2', 'IntegrationConnectRequestType3',
            'IntegrationConnectRequestType4']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[IntegrationConnection, ProblemDetails]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union['IntegrationConnectRequestType0', 'IntegrationConnectRequestType1', 'IntegrationConnectRequestType2', 'IntegrationConnectRequestType3', 'IntegrationConnectRequestType4'],

) -> Optional[Union[IntegrationConnection, ProblemDetails]]:
    """ Connect an integration (polymorphic by auth method)

     Finishes any auth method's connect flow and persists the connection under the target ecosystem
    `ecosystemId` the client names; the caller must manage it (404/403 otherwise). Returns the redacted
    connection (tokens never echoed).

    Args:
        body (Union['IntegrationConnectRequestType0', 'IntegrationConnectRequestType1',
            'IntegrationConnectRequestType2', 'IntegrationConnectRequestType3',
            'IntegrationConnectRequestType4']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[IntegrationConnection, ProblemDetails]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
