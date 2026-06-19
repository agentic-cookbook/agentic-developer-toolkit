from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_ecosystem_ecosystem_capabilities_ecosystem_id_capability_response_200 import GetEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200
from typing import cast



def _get_kwargs(
    ecosystem_id: str,
    capability: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ecosystem/ecosystem-capabilities/{ecosystem_id}/{capability}".format(ecosystem_id=quote(str(ecosystem_id), safe=""),capability=quote(str(capability), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200 | None:
    if response.status_code == 200:
        response_200 = GetEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ecosystem_id: str,
    capability: str,
    *,
    client: AuthenticatedClient,

) -> Response[Error | GetEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200]:
    """ Get ecosystem_capabilities by id

    Args:
        ecosystem_id (str):
        capability (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200]
     """


    kwargs = _get_kwargs(
        ecosystem_id=ecosystem_id,
capability=capability,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    ecosystem_id: str,
    capability: str,
    *,
    client: AuthenticatedClient,

) -> Error | GetEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200 | None:
    """ Get ecosystem_capabilities by id

    Args:
        ecosystem_id (str):
        capability (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200
     """


    return sync_detailed(
        ecosystem_id=ecosystem_id,
capability=capability,
client=client,

    ).parsed

async def asyncio_detailed(
    ecosystem_id: str,
    capability: str,
    *,
    client: AuthenticatedClient,

) -> Response[Error | GetEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200]:
    """ Get ecosystem_capabilities by id

    Args:
        ecosystem_id (str):
        capability (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200]
     """


    kwargs = _get_kwargs(
        ecosystem_id=ecosystem_id,
capability=capability,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    ecosystem_id: str,
    capability: str,
    *,
    client: AuthenticatedClient,

) -> Error | GetEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200 | None:
    """ Get ecosystem_capabilities by id

    Args:
        ecosystem_id (str):
        capability (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200
     """


    return (await asyncio_detailed(
        ecosystem_id=ecosystem_id,
capability=capability,
client=client,

    )).parsed
