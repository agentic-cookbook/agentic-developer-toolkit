from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_community_discussion_thread_tags_thread_id_tag_id_response_200 import GetCommunityDiscussionThreadTagsThreadIdTagIdResponse200
from typing import cast



def _get_kwargs(
    thread_id: str,
    tag_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/community/discussion-thread-tags/{thread_id}/{tag_id}".format(thread_id=quote(str(thread_id), safe=""),tag_id=quote(str(tag_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetCommunityDiscussionThreadTagsThreadIdTagIdResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCommunityDiscussionThreadTagsThreadIdTagIdResponse200.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetCommunityDiscussionThreadTagsThreadIdTagIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    thread_id: str,
    tag_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Error | GetCommunityDiscussionThreadTagsThreadIdTagIdResponse200]:
    """ Get discussion_thread_tags by id

    Args:
        thread_id (str):
        tag_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetCommunityDiscussionThreadTagsThreadIdTagIdResponse200]
     """


    kwargs = _get_kwargs(
        thread_id=thread_id,
tag_id=tag_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    thread_id: str,
    tag_id: str,
    *,
    client: AuthenticatedClient,

) -> Error | GetCommunityDiscussionThreadTagsThreadIdTagIdResponse200 | None:
    """ Get discussion_thread_tags by id

    Args:
        thread_id (str):
        tag_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetCommunityDiscussionThreadTagsThreadIdTagIdResponse200
     """


    return sync_detailed(
        thread_id=thread_id,
tag_id=tag_id,
client=client,

    ).parsed

async def asyncio_detailed(
    thread_id: str,
    tag_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Error | GetCommunityDiscussionThreadTagsThreadIdTagIdResponse200]:
    """ Get discussion_thread_tags by id

    Args:
        thread_id (str):
        tag_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetCommunityDiscussionThreadTagsThreadIdTagIdResponse200]
     """


    kwargs = _get_kwargs(
        thread_id=thread_id,
tag_id=tag_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    thread_id: str,
    tag_id: str,
    *,
    client: AuthenticatedClient,

) -> Error | GetCommunityDiscussionThreadTagsThreadIdTagIdResponse200 | None:
    """ Get discussion_thread_tags by id

    Args:
        thread_id (str):
        tag_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetCommunityDiscussionThreadTagsThreadIdTagIdResponse200
     """


    return (await asyncio_detailed(
        thread_id=thread_id,
tag_id=tag_id,
client=client,

    )).parsed
