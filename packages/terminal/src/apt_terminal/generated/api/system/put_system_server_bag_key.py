from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.put_system_server_bag_key_body import PutSystemServerBagKeyBody
from ...models.put_system_server_bag_key_response_200 import PutSystemServerBagKeyResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    key: str,
    *,
    body: PutSystemServerBagKeyBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/system/server-bag/{key}".format(key=quote(str(key), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PutSystemServerBagKeyResponse200 | None:
    if response.status_code == 200:
        response_200 = PutSystemServerBagKeyResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | PutSystemServerBagKeyResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key: str,
    *,
    client: AuthenticatedClient,
    body: PutSystemServerBagKeyBody | Unset = UNSET,

) -> Response[Error | PutSystemServerBagKeyResponse200]:
    """ Update server_bag

    Args:
        key (str):
        body (PutSystemServerBagKeyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PutSystemServerBagKeyResponse200]
     """


    kwargs = _get_kwargs(
        key=key,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    key: str,
    *,
    client: AuthenticatedClient,
    body: PutSystemServerBagKeyBody | Unset = UNSET,

) -> Error | PutSystemServerBagKeyResponse200 | None:
    """ Update server_bag

    Args:
        key (str):
        body (PutSystemServerBagKeyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PutSystemServerBagKeyResponse200
     """


    return sync_detailed(
        key=key,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    key: str,
    *,
    client: AuthenticatedClient,
    body: PutSystemServerBagKeyBody | Unset = UNSET,

) -> Response[Error | PutSystemServerBagKeyResponse200]:
    """ Update server_bag

    Args:
        key (str):
        body (PutSystemServerBagKeyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PutSystemServerBagKeyResponse200]
     """


    kwargs = _get_kwargs(
        key=key,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    key: str,
    *,
    client: AuthenticatedClient,
    body: PutSystemServerBagKeyBody | Unset = UNSET,

) -> Error | PutSystemServerBagKeyResponse200 | None:
    """ Update server_bag

    Args:
        key (str):
        body (PutSystemServerBagKeyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PutSystemServerBagKeyResponse200
     """


    return (await asyncio_detailed(
        key=key,
client=client,
body=body,

    )).parsed
