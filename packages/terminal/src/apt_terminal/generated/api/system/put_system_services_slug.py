from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.system_service import SystemService
from ...models.system_service_upsert import SystemServiceUpsert
from typing import cast



def _get_kwargs(
    slug: str,
    *,
    body: SystemServiceUpsert,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/system/services/{slug}".format(slug=slug,),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Error, SystemService]]:
    if response.status_code == 200:
        response_200 = SystemService.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Error, SystemService]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    slug: str,
    *,
    client: AuthenticatedClient,
    body: SystemServiceUpsert,

) -> Response[Union[Error, SystemService]]:
    """ Create or replace an external-service configuration (admin)

    Args:
        slug (str):
        body (SystemServiceUpsert):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SystemService]]
     """


    kwargs = _get_kwargs(
        slug=slug,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    slug: str,
    *,
    client: AuthenticatedClient,
    body: SystemServiceUpsert,

) -> Optional[Union[Error, SystemService]]:
    """ Create or replace an external-service configuration (admin)

    Args:
        slug (str):
        body (SystemServiceUpsert):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, SystemService]
     """


    return sync_detailed(
        slug=slug,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    slug: str,
    *,
    client: AuthenticatedClient,
    body: SystemServiceUpsert,

) -> Response[Union[Error, SystemService]]:
    """ Create or replace an external-service configuration (admin)

    Args:
        slug (str):
        body (SystemServiceUpsert):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SystemService]]
     """


    kwargs = _get_kwargs(
        slug=slug,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    slug: str,
    *,
    client: AuthenticatedClient,
    body: SystemServiceUpsert,

) -> Optional[Union[Error, SystemService]]:
    """ Create or replace an external-service configuration (admin)

    Args:
        slug (str):
        body (SystemServiceUpsert):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, SystemService]
     """


    return (await asyncio_detailed(
        slug=slug,
client=client,
body=body,

    )).parsed
