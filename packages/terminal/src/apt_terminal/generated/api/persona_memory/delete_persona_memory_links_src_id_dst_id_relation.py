from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from typing import cast



def _get_kwargs(
    src_id: str,
    dst_id: str,
    relation: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/persona-memory/links/{src_id}/{dst_id}/{relation}".format(src_id=quote(str(src_id), safe=""),dst_id=quote(str(dst_id), safe=""),relation=quote(str(relation), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    src_id: str,
    dst_id: str,
    relation: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | Error]:
    """ Delete links

    Args:
        src_id (str):
        dst_id (str):
        relation (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        src_id=src_id,
dst_id=dst_id,
relation=relation,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    src_id: str,
    dst_id: str,
    relation: str,
    *,
    client: AuthenticatedClient,

) -> Any | Error | None:
    """ Delete links

    Args:
        src_id (str):
        dst_id (str):
        relation (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        src_id=src_id,
dst_id=dst_id,
relation=relation,
client=client,

    ).parsed

async def asyncio_detailed(
    src_id: str,
    dst_id: str,
    relation: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | Error]:
    """ Delete links

    Args:
        src_id (str):
        dst_id (str):
        relation (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        src_id=src_id,
dst_id=dst_id,
relation=relation,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    src_id: str,
    dst_id: str,
    relation: str,
    *,
    client: AuthenticatedClient,

) -> Any | Error | None:
    """ Delete links

    Args:
        src_id (str):
        dst_id (str):
        relation (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        src_id=src_id,
dst_id=dst_id,
relation=relation,
client=client,

    )).parsed
