from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.community_member import CommunityMember
from ...models.error import Error
from ...models.post_communities_id_members_body import PostCommunitiesIdMembersBody
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: PostCommunitiesIdMembersBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/communities/{id}/members".format(id=id,),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[CommunityMember, Error]]:
    if response.status_code == 201:
        response_201 = CommunityMember.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[CommunityMember, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostCommunitiesIdMembersBody,

) -> Response[Union[CommunityMember, Error]]:
    """ Grant a membership role (community admin only; idempotent upsert; the grantee must be a real
    customer → 404)

    Args:
        id (str):
        body (PostCommunitiesIdMembersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommunityMember, Error]]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostCommunitiesIdMembersBody,

) -> Optional[Union[CommunityMember, Error]]:
    """ Grant a membership role (community admin only; idempotent upsert; the grantee must be a real
    customer → 404)

    Args:
        id (str):
        body (PostCommunitiesIdMembersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommunityMember, Error]
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostCommunitiesIdMembersBody,

) -> Response[Union[CommunityMember, Error]]:
    """ Grant a membership role (community admin only; idempotent upsert; the grantee must be a real
    customer → 404)

    Args:
        id (str):
        body (PostCommunitiesIdMembersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommunityMember, Error]]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostCommunitiesIdMembersBody,

) -> Optional[Union[CommunityMember, Error]]:
    """ Grant a membership role (community admin only; idempotent upsert; the grantee must be a real
    customer → 404)

    Args:
        id (str):
        body (PostCommunitiesIdMembersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommunityMember, Error]
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
