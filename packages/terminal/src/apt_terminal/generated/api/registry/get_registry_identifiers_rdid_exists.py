from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_registry_identifiers_rdid_exists_response_200 import GetRegistryIdentifiersRdidExistsResponse200
from typing import cast



def _get_kwargs(
    rdid: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/registry/identifiers/{rdid}/exists".format(rdid=rdid,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Error, GetRegistryIdentifiersRdidExistsResponse200]]:
    if response.status_code == 200:
        response_200 = GetRegistryIdentifiersRdidExistsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Error, GetRegistryIdentifiersRdidExistsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rdid: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Error, GetRegistryIdentifiersRdidExistsResponse200]]:
    """ Check whether an rdid is taken (never 404)

    Args:
        rdid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GetRegistryIdentifiersRdidExistsResponse200]]
     """


    kwargs = _get_kwargs(
        rdid=rdid,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    rdid: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Error, GetRegistryIdentifiersRdidExistsResponse200]]:
    """ Check whether an rdid is taken (never 404)

    Args:
        rdid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GetRegistryIdentifiersRdidExistsResponse200]
     """


    return sync_detailed(
        rdid=rdid,
client=client,

    ).parsed

async def asyncio_detailed(
    rdid: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Error, GetRegistryIdentifiersRdidExistsResponse200]]:
    """ Check whether an rdid is taken (never 404)

    Args:
        rdid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GetRegistryIdentifiersRdidExistsResponse200]]
     """


    kwargs = _get_kwargs(
        rdid=rdid,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    rdid: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Error, GetRegistryIdentifiersRdidExistsResponse200]]:
    """ Check whether an rdid is taken (never 404)

    Args:
        rdid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GetRegistryIdentifiersRdidExistsResponse200]
     """


    return (await asyncio_detailed(
        rdid=rdid,
client=client,

    )).parsed
