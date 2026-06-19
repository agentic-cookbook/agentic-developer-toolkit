from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.post_community_discussion_polls_body import PostCommunityDiscussionPollsBody
from ...models.post_community_discussion_polls_response_201 import PostCommunityDiscussionPollsResponse201
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: PostCommunityDiscussionPollsBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/community/discussion-polls",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PostCommunityDiscussionPollsResponse201 | None:
    if response.status_code == 201:
        response_201 = PostCommunityDiscussionPollsResponse201.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | PostCommunityDiscussionPollsResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostCommunityDiscussionPollsBody | Unset = UNSET,

) -> Response[Error | PostCommunityDiscussionPollsResponse201]:
    """ Create discussion_polls

    Args:
        body (PostCommunityDiscussionPollsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PostCommunityDiscussionPollsResponse201]
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
    body: PostCommunityDiscussionPollsBody | Unset = UNSET,

) -> Error | PostCommunityDiscussionPollsResponse201 | None:
    """ Create discussion_polls

    Args:
        body (PostCommunityDiscussionPollsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PostCommunityDiscussionPollsResponse201
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostCommunityDiscussionPollsBody | Unset = UNSET,

) -> Response[Error | PostCommunityDiscussionPollsResponse201]:
    """ Create discussion_polls

    Args:
        body (PostCommunityDiscussionPollsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PostCommunityDiscussionPollsResponse201]
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
    body: PostCommunityDiscussionPollsBody | Unset = UNSET,

) -> Error | PostCommunityDiscussionPollsResponse201 | None:
    """ Create discussion_polls

    Args:
        body (PostCommunityDiscussionPollsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PostCommunityDiscussionPollsResponse201
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
