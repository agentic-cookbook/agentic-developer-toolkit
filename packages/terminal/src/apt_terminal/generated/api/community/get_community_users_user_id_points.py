from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.community_points_page import CommunityPointsPage
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    user_id: str,
    *,
    page: Union[Unset, str] = UNSET,
    page_size: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/community/users/{user_id}/points".format(user_id=user_id,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[CommunityPointsPage, Error]]:
    if response.status_code == 200:
        response_200 = CommunityPointsPage.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[CommunityPointsPage, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, str] = UNSET,
    page_size: Union[Unset, str] = UNSET,

) -> Response[Union[CommunityPointsPage, Error]]:
    """ A user’s point ledger (newest first)

    Args:
        user_id (str):
        page (Union[Unset, str]):
        page_size (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommunityPointsPage, Error]]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
page=page,
page_size=page_size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, str] = UNSET,
    page_size: Union[Unset, str] = UNSET,

) -> Optional[Union[CommunityPointsPage, Error]]:
    """ A user’s point ledger (newest first)

    Args:
        user_id (str):
        page (Union[Unset, str]):
        page_size (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommunityPointsPage, Error]
     """


    return sync_detailed(
        user_id=user_id,
client=client,
page=page,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, str] = UNSET,
    page_size: Union[Unset, str] = UNSET,

) -> Response[Union[CommunityPointsPage, Error]]:
    """ A user’s point ledger (newest first)

    Args:
        user_id (str):
        page (Union[Unset, str]):
        page_size (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommunityPointsPage, Error]]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
page=page,
page_size=page_size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, str] = UNSET,
    page_size: Union[Unset, str] = UNSET,

) -> Optional[Union[CommunityPointsPage, Error]]:
    """ A user’s point ledger (newest first)

    Args:
        user_id (str):
        page (Union[Unset, str]):
        page_size (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommunityPointsPage, Error]
     """


    return (await asyncio_detailed(
        user_id=user_id,
client=client,
page=page,
page_size=page_size,

    )).parsed
