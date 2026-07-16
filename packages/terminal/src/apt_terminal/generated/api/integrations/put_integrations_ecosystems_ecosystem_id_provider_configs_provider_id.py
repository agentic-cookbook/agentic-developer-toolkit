from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.integration_provider_config import IntegrationProviderConfig
from ...models.problem_details import ProblemDetails
from ...models.put_integrations_ecosystems_ecosystem_id_provider_configs_provider_id_body import PutIntegrationsEcosystemsEcosystemIdProviderConfigsProviderIdBody
from typing import cast



def _get_kwargs(
    ecosystem_id: str,
    provider_id: str,
    *,
    body: PutIntegrationsEcosystemsEcosystemIdProviderConfigsProviderIdBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/integrations/ecosystems/{ecosystem_id}/provider-configs/{provider_id}".format(ecosystem_id=ecosystem_id,provider_id=provider_id,),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[IntegrationProviderConfig, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = IntegrationProviderConfig.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ProblemDetails.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())



        return response_404

    if response.status_code == 503:
        response_503 = ProblemDetails.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[IntegrationProviderConfig, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ecosystem_id: str,
    provider_id: str,
    *,
    client: AuthenticatedClient,
    body: PutIntegrationsEcosystemsEcosystemIdProviderConfigsProviderIdBody,

) -> Response[Union[IntegrationProviderConfig, ProblemDetails]]:
    """ Upsert an ecosystem's provider config

     Replaces the non-secret config; a blank/absent clientSecret preserves the stored encrypted secret, a
    present one is encrypted at rest. The change invalidates the resolver cache so the ecosystem's new
    creds drive its flows immediately. The ecosystemId must be the caller's own ecosystem (403
    otherwise).

    Args:
        ecosystem_id (str):
        provider_id (str):
        body (PutIntegrationsEcosystemsEcosystemIdProviderConfigsProviderIdBody): OAuth providers
            send clientId/scopes/…/clientSecret; api_key providers send the spec-driven `fields` map
            (+ optional `enabled`). The route branches by auth method.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[IntegrationProviderConfig, ProblemDetails]]
     """


    kwargs = _get_kwargs(
        ecosystem_id=ecosystem_id,
provider_id=provider_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    ecosystem_id: str,
    provider_id: str,
    *,
    client: AuthenticatedClient,
    body: PutIntegrationsEcosystemsEcosystemIdProviderConfigsProviderIdBody,

) -> Optional[Union[IntegrationProviderConfig, ProblemDetails]]:
    """ Upsert an ecosystem's provider config

     Replaces the non-secret config; a blank/absent clientSecret preserves the stored encrypted secret, a
    present one is encrypted at rest. The change invalidates the resolver cache so the ecosystem's new
    creds drive its flows immediately. The ecosystemId must be the caller's own ecosystem (403
    otherwise).

    Args:
        ecosystem_id (str):
        provider_id (str):
        body (PutIntegrationsEcosystemsEcosystemIdProviderConfigsProviderIdBody): OAuth providers
            send clientId/scopes/…/clientSecret; api_key providers send the spec-driven `fields` map
            (+ optional `enabled`). The route branches by auth method.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[IntegrationProviderConfig, ProblemDetails]
     """


    return sync_detailed(
        ecosystem_id=ecosystem_id,
provider_id=provider_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    ecosystem_id: str,
    provider_id: str,
    *,
    client: AuthenticatedClient,
    body: PutIntegrationsEcosystemsEcosystemIdProviderConfigsProviderIdBody,

) -> Response[Union[IntegrationProviderConfig, ProblemDetails]]:
    """ Upsert an ecosystem's provider config

     Replaces the non-secret config; a blank/absent clientSecret preserves the stored encrypted secret, a
    present one is encrypted at rest. The change invalidates the resolver cache so the ecosystem's new
    creds drive its flows immediately. The ecosystemId must be the caller's own ecosystem (403
    otherwise).

    Args:
        ecosystem_id (str):
        provider_id (str):
        body (PutIntegrationsEcosystemsEcosystemIdProviderConfigsProviderIdBody): OAuth providers
            send clientId/scopes/…/clientSecret; api_key providers send the spec-driven `fields` map
            (+ optional `enabled`). The route branches by auth method.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[IntegrationProviderConfig, ProblemDetails]]
     """


    kwargs = _get_kwargs(
        ecosystem_id=ecosystem_id,
provider_id=provider_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    ecosystem_id: str,
    provider_id: str,
    *,
    client: AuthenticatedClient,
    body: PutIntegrationsEcosystemsEcosystemIdProviderConfigsProviderIdBody,

) -> Optional[Union[IntegrationProviderConfig, ProblemDetails]]:
    """ Upsert an ecosystem's provider config

     Replaces the non-secret config; a blank/absent clientSecret preserves the stored encrypted secret, a
    present one is encrypted at rest. The change invalidates the resolver cache so the ecosystem's new
    creds drive its flows immediately. The ecosystemId must be the caller's own ecosystem (403
    otherwise).

    Args:
        ecosystem_id (str):
        provider_id (str):
        body (PutIntegrationsEcosystemsEcosystemIdProviderConfigsProviderIdBody): OAuth providers
            send clientId/scopes/…/clientSecret; api_key providers send the spec-driven `fields` map
            (+ optional `enabled`). The route branches by auth method.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[IntegrationProviderConfig, ProblemDetails]
     """


    return (await asyncio_detailed(
        ecosystem_id=ecosystem_id,
provider_id=provider_id,
client=client,
body=body,

    )).parsed
