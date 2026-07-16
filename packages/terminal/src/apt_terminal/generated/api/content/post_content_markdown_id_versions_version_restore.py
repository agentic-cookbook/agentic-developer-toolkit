from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.markdown_document import MarkdownDocument
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    id: str,
    version: str,
    *,
    workspace: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["workspace"] = workspace


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/content/markdown/{id}/versions/{version}/restore".format(id=id,version=version,),
        "params": params,
    }


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
    version: str,
    *,
    client: AuthenticatedClient,
    workspace: Union[Unset, str] = UNSET,

) -> Response[Union[Error, MarkdownDocument]]:
    """ Restore a version (re-applies its full state as a new version; non-destructive)

    Args:
        id (str):
        version (str):
        workspace (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MarkdownDocument]]
     """


    kwargs = _get_kwargs(
        id=id,
version=version,
workspace=workspace,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    version: str,
    *,
    client: AuthenticatedClient,
    workspace: Union[Unset, str] = UNSET,

) -> Optional[Union[Error, MarkdownDocument]]:
    """ Restore a version (re-applies its full state as a new version; non-destructive)

    Args:
        id (str):
        version (str):
        workspace (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MarkdownDocument]
     """


    return sync_detailed(
        id=id,
version=version,
client=client,
workspace=workspace,

    ).parsed

async def asyncio_detailed(
    id: str,
    version: str,
    *,
    client: AuthenticatedClient,
    workspace: Union[Unset, str] = UNSET,

) -> Response[Union[Error, MarkdownDocument]]:
    """ Restore a version (re-applies its full state as a new version; non-destructive)

    Args:
        id (str):
        version (str):
        workspace (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MarkdownDocument]]
     """


    kwargs = _get_kwargs(
        id=id,
version=version,
workspace=workspace,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    version: str,
    *,
    client: AuthenticatedClient,
    workspace: Union[Unset, str] = UNSET,

) -> Optional[Union[Error, MarkdownDocument]]:
    """ Restore a version (re-applies its full state as a new version; non-destructive)

    Args:
        id (str):
        version (str):
        workspace (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MarkdownDocument]
     """


    return (await asyncio_detailed(
        id=id,
version=version,
client=client,
workspace=workspace,

    )).parsed
