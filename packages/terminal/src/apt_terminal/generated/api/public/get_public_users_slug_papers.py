from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_public_users_slug_papers_response_200 import GetPublicUsersSlugPapersResponse200
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    slug: str,
    *,
    q: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["q"] = q


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/public/users/{slug}/papers".format(slug=slug,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Error, GetPublicUsersSlugPapersResponse200]]:
    if response.status_code == 200:
        response_200 = GetPublicUsersSlugPapersResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Error, GetPublicUsersSlugPapersResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    slug: str,
    *,
    client: Union[AuthenticatedClient, Client],
    q: Union[Unset, str] = UNSET,

) -> Response[Union[Error, GetPublicUsersSlugPapersResponse200]]:
    """ List an author's published papers (metadata only)

    Args:
        slug (str):
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GetPublicUsersSlugPapersResponse200]]
     """


    kwargs = _get_kwargs(
        slug=slug,
q=q,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    slug: str,
    *,
    client: Union[AuthenticatedClient, Client],
    q: Union[Unset, str] = UNSET,

) -> Optional[Union[Error, GetPublicUsersSlugPapersResponse200]]:
    """ List an author's published papers (metadata only)

    Args:
        slug (str):
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GetPublicUsersSlugPapersResponse200]
     """


    return sync_detailed(
        slug=slug,
client=client,
q=q,

    ).parsed

async def asyncio_detailed(
    slug: str,
    *,
    client: Union[AuthenticatedClient, Client],
    q: Union[Unset, str] = UNSET,

) -> Response[Union[Error, GetPublicUsersSlugPapersResponse200]]:
    """ List an author's published papers (metadata only)

    Args:
        slug (str):
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GetPublicUsersSlugPapersResponse200]]
     """


    kwargs = _get_kwargs(
        slug=slug,
q=q,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    slug: str,
    *,
    client: Union[AuthenticatedClient, Client],
    q: Union[Unset, str] = UNSET,

) -> Optional[Union[Error, GetPublicUsersSlugPapersResponse200]]:
    """ List an author's published papers (metadata only)

    Args:
        slug (str):
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GetPublicUsersSlugPapersResponse200]
     """


    return (await asyncio_detailed(
        slug=slug,
client=client,
q=q,

    )).parsed
