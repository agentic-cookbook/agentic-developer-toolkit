from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.post_community_discussion_watches_body import PostCommunityDiscussionWatchesBody
from ...models.post_community_discussion_watches_response_201 import PostCommunityDiscussionWatchesResponse201
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: PostCommunityDiscussionWatchesBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/community/discussion-watches",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PostCommunityDiscussionWatchesResponse201 | None:
    if response.status_code == 201:
        response_201 = PostCommunityDiscussionWatchesResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | PostCommunityDiscussionWatchesResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostCommunityDiscussionWatchesBody | Unset = UNSET,

) -> Response[Error | PostCommunityDiscussionWatchesResponse201]:
    """ Create discussion_watches

    Args:
        body (PostCommunityDiscussionWatchesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PostCommunityDiscussionWatchesResponse201]
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
    body: PostCommunityDiscussionWatchesBody | Unset = UNSET,

) -> Error | PostCommunityDiscussionWatchesResponse201 | None:
    """ Create discussion_watches

    Args:
        body (PostCommunityDiscussionWatchesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PostCommunityDiscussionWatchesResponse201
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostCommunityDiscussionWatchesBody | Unset = UNSET,

) -> Response[Error | PostCommunityDiscussionWatchesResponse201]:
    """ Create discussion_watches

    Args:
        body (PostCommunityDiscussionWatchesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PostCommunityDiscussionWatchesResponse201]
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
    body: PostCommunityDiscussionWatchesBody | Unset = UNSET,

) -> Error | PostCommunityDiscussionWatchesResponse201 | None:
    """ Create discussion_watches

    Args:
        body (PostCommunityDiscussionWatchesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PostCommunityDiscussionWatchesResponse201
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
