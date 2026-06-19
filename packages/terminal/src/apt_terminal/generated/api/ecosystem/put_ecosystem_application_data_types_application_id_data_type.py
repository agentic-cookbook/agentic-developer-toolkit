from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.put_ecosystem_application_data_types_application_id_data_type_body import PutEcosystemApplicationDataTypesApplicationIdDataTypeBody
from ...models.put_ecosystem_application_data_types_application_id_data_type_response_200 import PutEcosystemApplicationDataTypesApplicationIdDataTypeResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    application_id: str,
    data_type: str,
    *,
    body: PutEcosystemApplicationDataTypesApplicationIdDataTypeBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/ecosystem/application-data-types/{application_id}/{data_type}".format(application_id=quote(str(application_id), safe=""),data_type=quote(str(data_type), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PutEcosystemApplicationDataTypesApplicationIdDataTypeResponse200 | None:
    if response.status_code == 200:
        response_200 = PutEcosystemApplicationDataTypesApplicationIdDataTypeResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | PutEcosystemApplicationDataTypesApplicationIdDataTypeResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    application_id: str,
    data_type: str,
    *,
    client: AuthenticatedClient,
    body: PutEcosystemApplicationDataTypesApplicationIdDataTypeBody | Unset = UNSET,

) -> Response[Error | PutEcosystemApplicationDataTypesApplicationIdDataTypeResponse200]:
    """ Update application_data_types

    Args:
        application_id (str):
        data_type (str):
        body (PutEcosystemApplicationDataTypesApplicationIdDataTypeBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PutEcosystemApplicationDataTypesApplicationIdDataTypeResponse200]
     """


    kwargs = _get_kwargs(
        application_id=application_id,
data_type=data_type,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    application_id: str,
    data_type: str,
    *,
    client: AuthenticatedClient,
    body: PutEcosystemApplicationDataTypesApplicationIdDataTypeBody | Unset = UNSET,

) -> Error | PutEcosystemApplicationDataTypesApplicationIdDataTypeResponse200 | None:
    """ Update application_data_types

    Args:
        application_id (str):
        data_type (str):
        body (PutEcosystemApplicationDataTypesApplicationIdDataTypeBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PutEcosystemApplicationDataTypesApplicationIdDataTypeResponse200
     """


    return sync_detailed(
        application_id=application_id,
data_type=data_type,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    application_id: str,
    data_type: str,
    *,
    client: AuthenticatedClient,
    body: PutEcosystemApplicationDataTypesApplicationIdDataTypeBody | Unset = UNSET,

) -> Response[Error | PutEcosystemApplicationDataTypesApplicationIdDataTypeResponse200]:
    """ Update application_data_types

    Args:
        application_id (str):
        data_type (str):
        body (PutEcosystemApplicationDataTypesApplicationIdDataTypeBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PutEcosystemApplicationDataTypesApplicationIdDataTypeResponse200]
     """


    kwargs = _get_kwargs(
        application_id=application_id,
data_type=data_type,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    application_id: str,
    data_type: str,
    *,
    client: AuthenticatedClient,
    body: PutEcosystemApplicationDataTypesApplicationIdDataTypeBody | Unset = UNSET,

) -> Error | PutEcosystemApplicationDataTypesApplicationIdDataTypeResponse200 | None:
    """ Update application_data_types

    Args:
        application_id (str):
        data_type (str):
        body (PutEcosystemApplicationDataTypesApplicationIdDataTypeBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PutEcosystemApplicationDataTypesApplicationIdDataTypeResponse200
     """


    return (await asyncio_detailed(
        application_id=application_id,
data_type=data_type,
client=client,
body=body,

    )).parsed
