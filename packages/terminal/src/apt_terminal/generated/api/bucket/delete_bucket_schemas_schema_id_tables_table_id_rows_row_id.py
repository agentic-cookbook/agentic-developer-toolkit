from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from typing import cast



def _get_kwargs(
    schema_id: str,
    table_id: str,
    row_id: str,
    *,
    as_type: str,
    as_id: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["asType"] = as_type

    params["asId"] = as_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/bucket/schemas/{schema_id}/tables/{table_id}/rows/{row_id}".format(schema_id=quote(str(schema_id), safe=""),table_id=quote(str(table_id), safe=""),row_id=quote(str(row_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    schema_id: str,
    table_id: str,
    row_id: str,
    *,
    client: AuthenticatedClient,
    as_type: str,
    as_id: str,

) -> Response[Any | Error]:
    """ Delete a bucket-table row (acting as an app/persona)

    Args:
        schema_id (str):
        table_id (str):
        row_id (str):
        as_type (str):
        as_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        schema_id=schema_id,
table_id=table_id,
row_id=row_id,
as_type=as_type,
as_id=as_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    schema_id: str,
    table_id: str,
    row_id: str,
    *,
    client: AuthenticatedClient,
    as_type: str,
    as_id: str,

) -> Any | Error | None:
    """ Delete a bucket-table row (acting as an app/persona)

    Args:
        schema_id (str):
        table_id (str):
        row_id (str):
        as_type (str):
        as_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        schema_id=schema_id,
table_id=table_id,
row_id=row_id,
client=client,
as_type=as_type,
as_id=as_id,

    ).parsed

async def asyncio_detailed(
    schema_id: str,
    table_id: str,
    row_id: str,
    *,
    client: AuthenticatedClient,
    as_type: str,
    as_id: str,

) -> Response[Any | Error]:
    """ Delete a bucket-table row (acting as an app/persona)

    Args:
        schema_id (str):
        table_id (str):
        row_id (str):
        as_type (str):
        as_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        schema_id=schema_id,
table_id=table_id,
row_id=row_id,
as_type=as_type,
as_id=as_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    schema_id: str,
    table_id: str,
    row_id: str,
    *,
    client: AuthenticatedClient,
    as_type: str,
    as_id: str,

) -> Any | Error | None:
    """ Delete a bucket-table row (acting as an app/persona)

    Args:
        schema_id (str):
        table_id (str):
        row_id (str):
        as_type (str):
        as_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        schema_id=schema_id,
table_id=table_id,
row_id=row_id,
client=client,
as_type=as_type,
as_id=as_id,

    )).parsed
