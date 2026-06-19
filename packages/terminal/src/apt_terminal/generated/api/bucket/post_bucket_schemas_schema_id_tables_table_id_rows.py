from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bucket_row import BucketRow
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    schema_id: str,
    table_id: str,
    *,
    body: BucketRow | Unset = UNSET,
    as_type: str,
    as_id: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["asType"] = as_type

    params["asId"] = as_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/bucket/schemas/{schema_id}/tables/{table_id}/rows".format(schema_id=quote(str(schema_id), safe=""),table_id=quote(str(table_id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BucketRow | Error | None:
    if response.status_code == 201:
        response_201 = BucketRow.from_dict(response.json())



        return response_201

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BucketRow | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    schema_id: str,
    table_id: str,
    *,
    client: AuthenticatedClient,
    body: BucketRow | Unset = UNSET,
    as_type: str,
    as_id: str,

) -> Response[BucketRow | Error]:
    """ Create a bucket-table row (acting as an app/persona)

    Args:
        schema_id (str):
        table_id (str):
        as_type (str):
        as_id (str):
        body (BucketRow | Unset): A bucket-table row. Intentionally open — the column set is
            defined at runtime by the developer-managed table this bucket points at, so no fixed
            property schema applies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BucketRow | Error]
     """


    kwargs = _get_kwargs(
        schema_id=schema_id,
table_id=table_id,
body=body,
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
    *,
    client: AuthenticatedClient,
    body: BucketRow | Unset = UNSET,
    as_type: str,
    as_id: str,

) -> BucketRow | Error | None:
    """ Create a bucket-table row (acting as an app/persona)

    Args:
        schema_id (str):
        table_id (str):
        as_type (str):
        as_id (str):
        body (BucketRow | Unset): A bucket-table row. Intentionally open — the column set is
            defined at runtime by the developer-managed table this bucket points at, so no fixed
            property schema applies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BucketRow | Error
     """


    return sync_detailed(
        schema_id=schema_id,
table_id=table_id,
client=client,
body=body,
as_type=as_type,
as_id=as_id,

    ).parsed

async def asyncio_detailed(
    schema_id: str,
    table_id: str,
    *,
    client: AuthenticatedClient,
    body: BucketRow | Unset = UNSET,
    as_type: str,
    as_id: str,

) -> Response[BucketRow | Error]:
    """ Create a bucket-table row (acting as an app/persona)

    Args:
        schema_id (str):
        table_id (str):
        as_type (str):
        as_id (str):
        body (BucketRow | Unset): A bucket-table row. Intentionally open — the column set is
            defined at runtime by the developer-managed table this bucket points at, so no fixed
            property schema applies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BucketRow | Error]
     """


    kwargs = _get_kwargs(
        schema_id=schema_id,
table_id=table_id,
body=body,
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
    *,
    client: AuthenticatedClient,
    body: BucketRow | Unset = UNSET,
    as_type: str,
    as_id: str,

) -> BucketRow | Error | None:
    """ Create a bucket-table row (acting as an app/persona)

    Args:
        schema_id (str):
        table_id (str):
        as_type (str):
        as_id (str):
        body (BucketRow | Unset): A bucket-table row. Intentionally open — the column set is
            defined at runtime by the developer-managed table this bucket points at, so no fixed
            property schema applies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BucketRow | Error
     """


    return (await asyncio_detailed(
        schema_id=schema_id,
table_id=table_id,
client=client,
body=body,
as_type=as_type,
as_id=as_id,

    )).parsed
