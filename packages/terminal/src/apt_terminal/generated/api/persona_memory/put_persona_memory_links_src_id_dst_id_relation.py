from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.put_persona_memory_links_src_id_dst_id_relation_body import PutPersonaMemoryLinksSrcIdDstIdRelationBody
from ...models.put_persona_memory_links_src_id_dst_id_relation_response_200 import PutPersonaMemoryLinksSrcIdDstIdRelationResponse200
from typing import cast



def _get_kwargs(
    src_id: str,
    dst_id: str,
    relation: str,
    *,
    body: PutPersonaMemoryLinksSrcIdDstIdRelationBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/persona-memory/links/{src_id}/{dst_id}/{relation}".format(src_id=src_id,dst_id=dst_id,relation=relation,),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Error, PutPersonaMemoryLinksSrcIdDstIdRelationResponse200]]:
    if response.status_code == 200:
        response_200 = PutPersonaMemoryLinksSrcIdDstIdRelationResponse200.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Error, PutPersonaMemoryLinksSrcIdDstIdRelationResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    src_id: str,
    dst_id: str,
    relation: str,
    *,
    client: AuthenticatedClient,
    body: PutPersonaMemoryLinksSrcIdDstIdRelationBody,

) -> Response[Union[Error, PutPersonaMemoryLinksSrcIdDstIdRelationResponse200]]:
    """ Update links

    Args:
        src_id (str):
        dst_id (str):
        relation (str):
        body (PutPersonaMemoryLinksSrcIdDstIdRelationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PutPersonaMemoryLinksSrcIdDstIdRelationResponse200]]
     """


    kwargs = _get_kwargs(
        src_id=src_id,
dst_id=dst_id,
relation=relation,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    src_id: str,
    dst_id: str,
    relation: str,
    *,
    client: AuthenticatedClient,
    body: PutPersonaMemoryLinksSrcIdDstIdRelationBody,

) -> Optional[Union[Error, PutPersonaMemoryLinksSrcIdDstIdRelationResponse200]]:
    """ Update links

    Args:
        src_id (str):
        dst_id (str):
        relation (str):
        body (PutPersonaMemoryLinksSrcIdDstIdRelationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PutPersonaMemoryLinksSrcIdDstIdRelationResponse200]
     """


    return sync_detailed(
        src_id=src_id,
dst_id=dst_id,
relation=relation,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    src_id: str,
    dst_id: str,
    relation: str,
    *,
    client: AuthenticatedClient,
    body: PutPersonaMemoryLinksSrcIdDstIdRelationBody,

) -> Response[Union[Error, PutPersonaMemoryLinksSrcIdDstIdRelationResponse200]]:
    """ Update links

    Args:
        src_id (str):
        dst_id (str):
        relation (str):
        body (PutPersonaMemoryLinksSrcIdDstIdRelationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PutPersonaMemoryLinksSrcIdDstIdRelationResponse200]]
     """


    kwargs = _get_kwargs(
        src_id=src_id,
dst_id=dst_id,
relation=relation,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    src_id: str,
    dst_id: str,
    relation: str,
    *,
    client: AuthenticatedClient,
    body: PutPersonaMemoryLinksSrcIdDstIdRelationBody,

) -> Optional[Union[Error, PutPersonaMemoryLinksSrcIdDstIdRelationResponse200]]:
    """ Update links

    Args:
        src_id (str):
        dst_id (str):
        relation (str):
        body (PutPersonaMemoryLinksSrcIdDstIdRelationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PutPersonaMemoryLinksSrcIdDstIdRelationResponse200]
     """


    return (await asyncio_detailed(
        src_id=src_id,
dst_id=dst_id,
relation=relation,
client=client,
body=body,

    )).parsed
