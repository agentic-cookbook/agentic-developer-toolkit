from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.markdown_document import MarkdownDocument
from ...models.put_content_markdown_id_body import PutContentMarkdownIdBody
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: PutContentMarkdownIdBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/content/markdown/{id}".format(id=id,),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Error, MarkdownDocument]]:
    if response.status_code == 200:
        response_200 = MarkdownDocument.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Error, MarkdownDocument]]:
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
    body: PutContentMarkdownIdBody,

) -> Response[Union[Error, MarkdownDocument]]:
    """ Update a document; any real change appends a full-state version

    Args:
        id (str):
        body (PutContentMarkdownIdBody): At least one of content/title. Any real change appends a
            full-state version (author attaches to it); a no-op returns the doc unchanged.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MarkdownDocument]]
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
    body: PutContentMarkdownIdBody,

) -> Optional[Union[Error, MarkdownDocument]]:
    """ Update a document; any real change appends a full-state version

    Args:
        id (str):
        body (PutContentMarkdownIdBody): At least one of content/title. Any real change appends a
            full-state version (author attaches to it); a no-op returns the doc unchanged.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MarkdownDocument]
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
    body: PutContentMarkdownIdBody,

) -> Response[Union[Error, MarkdownDocument]]:
    """ Update a document; any real change appends a full-state version

    Args:
        id (str):
        body (PutContentMarkdownIdBody): At least one of content/title. Any real change appends a
            full-state version (author attaches to it); a no-op returns the doc unchanged.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MarkdownDocument]]
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
    body: PutContentMarkdownIdBody,

) -> Optional[Union[Error, MarkdownDocument]]:
    """ Update a document; any real change appends a full-state version

    Args:
        id (str):
        body (PutContentMarkdownIdBody): At least one of content/title. Any real change appends a
            full-state version (author attaches to it); a no-op returns the doc unchanged.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MarkdownDocument]
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
