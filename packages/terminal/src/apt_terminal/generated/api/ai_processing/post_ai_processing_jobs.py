from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.post_ai_processing_jobs_body import PostAiProcessingJobsBody
from ...models.post_ai_processing_jobs_response_201 import PostAiProcessingJobsResponse201
from typing import cast



def _get_kwargs(
    *,
    body: PostAiProcessingJobsBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ai-processing/jobs",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Error, PostAiProcessingJobsResponse201]]:
    if response.status_code == 201:
        response_201 = PostAiProcessingJobsResponse201.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Error, PostAiProcessingJobsResponse201]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostAiProcessingJobsBody,

) -> Response[Union[Error, PostAiProcessingJobsResponse201]]:
    """ Enqueue an ad-hoc job (management)

     Ad-hoc / explicit enqueue path (task family 3). Requires a user JWT. The caller's ecosystemId
    becomes the owning ecosystem. Returns { id, deduped }.

    Args:
        body (PostAiProcessingJobsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PostAiProcessingJobsResponse201]]
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
    body: PostAiProcessingJobsBody,

) -> Optional[Union[Error, PostAiProcessingJobsResponse201]]:
    """ Enqueue an ad-hoc job (management)

     Ad-hoc / explicit enqueue path (task family 3). Requires a user JWT. The caller's ecosystemId
    becomes the owning ecosystem. Returns { id, deduped }.

    Args:
        body (PostAiProcessingJobsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PostAiProcessingJobsResponse201]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostAiProcessingJobsBody,

) -> Response[Union[Error, PostAiProcessingJobsResponse201]]:
    """ Enqueue an ad-hoc job (management)

     Ad-hoc / explicit enqueue path (task family 3). Requires a user JWT. The caller's ecosystemId
    becomes the owning ecosystem. Returns { id, deduped }.

    Args:
        body (PostAiProcessingJobsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PostAiProcessingJobsResponse201]]
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
    body: PostAiProcessingJobsBody,

) -> Optional[Union[Error, PostAiProcessingJobsResponse201]]:
    """ Enqueue an ad-hoc job (management)

     Ad-hoc / explicit enqueue path (task family 3). Requires a user JWT. The caller's ecosystemId
    becomes the owning ecosystem. Returns { id, deduped }.

    Args:
        body (PostAiProcessingJobsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PostAiProcessingJobsResponse201]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
