from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_public_communities_id_topics_response_200 import GetPublicCommunitiesIdTopicsResponse200
from ...models.get_public_communities_id_topics_sort import GetPublicCommunitiesIdTopicsSort
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    id: str,
    *,
    category: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetPublicCommunitiesIdTopicsSort] = UNSET,
    page: Union[Unset, str] = UNSET,
    page_size: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["category"] = category

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["page"] = page

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/public/communities/{id}/topics".format(id=id,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Error, GetPublicCommunitiesIdTopicsResponse200]]:
    if response.status_code == 200:
        response_200 = GetPublicCommunitiesIdTopicsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Error, GetPublicCommunitiesIdTopicsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    category: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetPublicCommunitiesIdTopicsSort] = UNSET,
    page: Union[Unset, str] = UNSET,
    page_size: Union[Unset, str] = UNSET,

) -> Response[Union[Error, GetPublicCommunitiesIdTopicsResponse200]]:
    """ List a PUBLIC hub community’s public topics (author id omitted)

    Args:
        id (str):
        category (Union[Unset, str]):
        sort (Union[Unset, GetPublicCommunitiesIdTopicsSort]):
        page (Union[Unset, str]):
        page_size (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GetPublicCommunitiesIdTopicsResponse200]]
     """


    kwargs = _get_kwargs(
        id=id,
category=category,
sort=sort,
page=page,
page_size=page_size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    category: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetPublicCommunitiesIdTopicsSort] = UNSET,
    page: Union[Unset, str] = UNSET,
    page_size: Union[Unset, str] = UNSET,

) -> Optional[Union[Error, GetPublicCommunitiesIdTopicsResponse200]]:
    """ List a PUBLIC hub community’s public topics (author id omitted)

    Args:
        id (str):
        category (Union[Unset, str]):
        sort (Union[Unset, GetPublicCommunitiesIdTopicsSort]):
        page (Union[Unset, str]):
        page_size (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GetPublicCommunitiesIdTopicsResponse200]
     """


    return sync_detailed(
        id=id,
client=client,
category=category,
sort=sort,
page=page,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    category: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetPublicCommunitiesIdTopicsSort] = UNSET,
    page: Union[Unset, str] = UNSET,
    page_size: Union[Unset, str] = UNSET,

) -> Response[Union[Error, GetPublicCommunitiesIdTopicsResponse200]]:
    """ List a PUBLIC hub community’s public topics (author id omitted)

    Args:
        id (str):
        category (Union[Unset, str]):
        sort (Union[Unset, GetPublicCommunitiesIdTopicsSort]):
        page (Union[Unset, str]):
        page_size (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GetPublicCommunitiesIdTopicsResponse200]]
     """


    kwargs = _get_kwargs(
        id=id,
category=category,
sort=sort,
page=page,
page_size=page_size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    category: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetPublicCommunitiesIdTopicsSort] = UNSET,
    page: Union[Unset, str] = UNSET,
    page_size: Union[Unset, str] = UNSET,

) -> Optional[Union[Error, GetPublicCommunitiesIdTopicsResponse200]]:
    """ List a PUBLIC hub community’s public topics (author id omitted)

    Args:
        id (str):
        category (Union[Unset, str]):
        sort (Union[Unset, GetPublicCommunitiesIdTopicsSort]):
        page (Union[Unset, str]):
        page_size (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GetPublicCommunitiesIdTopicsResponse200]
     """


    return (await asyncio_detailed(
        id=id,
client=client,
category=category,
sort=sort,
page=page,
page_size=page_size,

    )).parsed
