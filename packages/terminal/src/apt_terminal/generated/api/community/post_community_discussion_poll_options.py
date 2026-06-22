from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.post_community_discussion_poll_options_body import PostCommunityDiscussionPollOptionsBody
from ...models.post_community_discussion_poll_options_response_201 import PostCommunityDiscussionPollOptionsResponse201
from typing import cast



def _get_kwargs(
    *,
    body: PostCommunityDiscussionPollOptionsBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/community/discussion-poll-options",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Error, PostCommunityDiscussionPollOptionsResponse201]]:
    if response.status_code == 201:
        response_201 = PostCommunityDiscussionPollOptionsResponse201.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Error, PostCommunityDiscussionPollOptionsResponse201]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostCommunityDiscussionPollOptionsBody,

) -> Response[Union[Error, PostCommunityDiscussionPollOptionsResponse201]]:
    """ Create discussion_poll_options

    Args:
        body (PostCommunityDiscussionPollOptionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PostCommunityDiscussionPollOptionsResponse201]]
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
    body: PostCommunityDiscussionPollOptionsBody,

) -> Optional[Union[Error, PostCommunityDiscussionPollOptionsResponse201]]:
    """ Create discussion_poll_options

    Args:
        body (PostCommunityDiscussionPollOptionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PostCommunityDiscussionPollOptionsResponse201]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostCommunityDiscussionPollOptionsBody,

) -> Response[Union[Error, PostCommunityDiscussionPollOptionsResponse201]]:
    """ Create discussion_poll_options

    Args:
        body (PostCommunityDiscussionPollOptionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PostCommunityDiscussionPollOptionsResponse201]]
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
    body: PostCommunityDiscussionPollOptionsBody,

) -> Optional[Union[Error, PostCommunityDiscussionPollOptionsResponse201]]:
    """ Create discussion_poll_options

    Args:
        body (PostCommunityDiscussionPollOptionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PostCommunityDiscussionPollOptionsResponse201]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
