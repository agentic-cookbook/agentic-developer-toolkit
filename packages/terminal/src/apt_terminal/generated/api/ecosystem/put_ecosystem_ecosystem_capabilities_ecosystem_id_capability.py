from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.put_ecosystem_ecosystem_capabilities_ecosystem_id_capability_body import PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityBody
from ...models.put_ecosystem_ecosystem_capabilities_ecosystem_id_capability_response_200 import PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    ecosystem_id: str,
    capability: str,
    *,
    body: PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/ecosystem/ecosystem-capabilities/{ecosystem_id}/{capability}".format(ecosystem_id=quote(str(ecosystem_id), safe=""),capability=quote(str(capability), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200 | None:
    if response.status_code == 200:
        response_200 = PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200]:
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
    body: PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityBody | Unset = UNSET,

) -> Response[Error | PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200]:
    """ Update ecosystem_capabilities

    Args:
        ecosystem_id (str):
        capability (str):
        body (PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200]
     """


    kwargs = _get_kwargs(
        ecosystem_id=ecosystem_id,
capability=capability,
body=body,

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
    body: PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityBody | Unset = UNSET,

) -> Error | PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200 | None:
    """ Update ecosystem_capabilities

    Args:
        ecosystem_id (str):
        capability (str):
        body (PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200
     """


    return sync_detailed(
        ecosystem_id=ecosystem_id,
capability=capability,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    ecosystem_id: str,
    capability: str,
    *,
    client: AuthenticatedClient,
    body: PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityBody | Unset = UNSET,

) -> Response[Error | PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200]:
    """ Update ecosystem_capabilities

    Args:
        ecosystem_id (str):
        capability (str):
        body (PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200]
     """


    kwargs = _get_kwargs(
        ecosystem_id=ecosystem_id,
capability=capability,
body=body,

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
    body: PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityBody | Unset = UNSET,

) -> Error | PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200 | None:
    """ Update ecosystem_capabilities

    Args:
        ecosystem_id (str):
        capability (str):
        body (PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200
     """


    return (await asyncio_detailed(
        ecosystem_id=ecosystem_id,
capability=capability,
client=client,
body=body,

    )).parsed
