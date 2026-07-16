from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.markdown_document import MarkdownDocument
from ...models.post_content_markdown_body import PostContentMarkdownBody
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    body: PostContentMarkdownBody,
    workspace: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["workspace"] = workspace


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/content/markdown",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Error, MarkdownDocument]]:
    if response.status_code == 201:
        response_201 = MarkdownDocument.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Error, MarkdownDocument]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostContentMarkdownBody,
    workspace: Union[Unset, str] = UNSET,

) -> Response[Union[Error, MarkdownDocument]]:
    """ Create a markdown document (writes the head + version 1)

    Args:
        workspace (Union[Unset, str]):
        body (PostContentMarkdownBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MarkdownDocument]]
     """


    kwargs = _get_kwargs(
        body=body,
workspace=workspace,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: PostContentMarkdownBody,
    workspace: Union[Unset, str] = UNSET,

) -> Optional[Union[Error, MarkdownDocument]]:
    """ Create a markdown document (writes the head + version 1)

    Args:
        workspace (Union[Unset, str]):
        body (PostContentMarkdownBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MarkdownDocument]
     """


    return sync_detailed(
        client=client,
body=body,
workspace=workspace,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostContentMarkdownBody,
    workspace: Union[Unset, str] = UNSET,

) -> Response[Union[Error, MarkdownDocument]]:
    """ Create a markdown document (writes the head + version 1)

    Args:
        workspace (Union[Unset, str]):
        body (PostContentMarkdownBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MarkdownDocument]]
     """


    kwargs = _get_kwargs(
        body=body,
workspace=workspace,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostContentMarkdownBody,
    workspace: Union[Unset, str] = UNSET,

) -> Optional[Union[Error, MarkdownDocument]]:
    """ Create a markdown document (writes the head + version 1)

    Args:
        workspace (Union[Unset, str]):
        body (PostContentMarkdownBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MarkdownDocument]
     """


    return (await asyncio_detailed(
        client=client,
body=body,
workspace=workspace,

    )).parsed
