from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.post_community_discussion_edits_body import PostCommunityDiscussionEditsBody
from ...models.post_community_discussion_edits_response_201 import PostCommunityDiscussionEditsResponse201
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: PostCommunityDiscussionEditsBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/community/discussion-edits",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PostCommunityDiscussionEditsResponse201 | None:
    if response.status_code == 201:
        response_201 = PostCommunityDiscussionEditsResponse201.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | PostCommunityDiscussionEditsResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostCommunityDiscussionEditsBody | Unset = UNSET,

) -> Response[Error | PostCommunityDiscussionEditsResponse201]:
    """ Create discussion_edits

    Args:
        body (PostCommunityDiscussionEditsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PostCommunityDiscussionEditsResponse201]
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
    body: PostCommunityDiscussionEditsBody | Unset = UNSET,

) -> Error | PostCommunityDiscussionEditsResponse201 | None:
    """ Create discussion_edits

    Args:
        body (PostCommunityDiscussionEditsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PostCommunityDiscussionEditsResponse201
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostCommunityDiscussionEditsBody | Unset = UNSET,

) -> Response[Error | PostCommunityDiscussionEditsResponse201]:
    """ Create discussion_edits

    Args:
        body (PostCommunityDiscussionEditsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PostCommunityDiscussionEditsResponse201]
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
    body: PostCommunityDiscussionEditsBody | Unset = UNSET,

) -> Error | PostCommunityDiscussionEditsResponse201 | None:
    """ Create discussion_edits

    Args:
        body (PostCommunityDiscussionEditsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PostCommunityDiscussionEditsResponse201
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
