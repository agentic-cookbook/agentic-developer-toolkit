from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_ecosystem_application_data_types_application_id_data_type_response_200 import GetEcosystemApplicationDataTypesApplicationIdDataTypeResponse200
from typing import cast



def _get_kwargs(
    application_id: str,
    data_type: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ecosystem/application-data-types/{application_id}/{data_type}".format(application_id=quote(str(application_id), safe=""),data_type=quote(str(data_type), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetEcosystemApplicationDataTypesApplicationIdDataTypeResponse200 | None:
    if response.status_code == 200:
        response_200 = GetEcosystemApplicationDataTypesApplicationIdDataTypeResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetEcosystemApplicationDataTypesApplicationIdDataTypeResponse200]:
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

) -> Response[Error | GetEcosystemApplicationDataTypesApplicationIdDataTypeResponse200]:
    """ Get application_data_types by id

    Args:
        application_id (str):
        data_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetEcosystemApplicationDataTypesApplicationIdDataTypeResponse200]
     """


    kwargs = _get_kwargs(
        application_id=application_id,
data_type=data_type,

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

) -> Error | GetEcosystemApplicationDataTypesApplicationIdDataTypeResponse200 | None:
    """ Get application_data_types by id

    Args:
        application_id (str):
        data_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetEcosystemApplicationDataTypesApplicationIdDataTypeResponse200
     """


    return sync_detailed(
        application_id=application_id,
data_type=data_type,
client=client,

    ).parsed

async def asyncio_detailed(
    application_id: str,
    data_type: str,
    *,
    client: AuthenticatedClient,

) -> Response[Error | GetEcosystemApplicationDataTypesApplicationIdDataTypeResponse200]:
    """ Get application_data_types by id

    Args:
        application_id (str):
        data_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetEcosystemApplicationDataTypesApplicationIdDataTypeResponse200]
     """


    kwargs = _get_kwargs(
        application_id=application_id,
data_type=data_type,

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

) -> Error | GetEcosystemApplicationDataTypesApplicationIdDataTypeResponse200 | None:
    """ Get application_data_types by id

    Args:
        application_id (str):
        data_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetEcosystemApplicationDataTypesApplicationIdDataTypeResponse200
     """


    return (await asyncio_detailed(
        application_id=application_id,
data_type=data_type,
client=client,

    )).parsed
