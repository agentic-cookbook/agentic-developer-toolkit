from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.put_oauth_clients_slug_providers_provider_slug_body import PutOauthClientsSlugProvidersProviderSlugBody
from ...models.put_oauth_clients_slug_providers_provider_slug_response_200 import PutOauthClientsSlugProvidersProviderSlugResponse200
from typing import cast



def _get_kwargs(
    slug: str,
    provider_slug: str,
    *,
    body: PutOauthClientsSlugProvidersProviderSlugBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/oauth/clients/{slug}/providers/{provider_slug}".format(slug=slug,provider_slug=provider_slug,),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Error, PutOauthClientsSlugProvidersProviderSlugResponse200]]:
    if response.status_code == 200:
        response_200 = PutOauthClientsSlugProvidersProviderSlugResponse200.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Error, PutOauthClientsSlugProvidersProviderSlugResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    slug: str,
    provider_slug: str,
    *,
    client: AuthenticatedClient,
    body: PutOauthClientsSlugProvidersProviderSlugBody,

) -> Response[Union[Error, PutOauthClientsSlugProvidersProviderSlugResponse200]]:
    """ Link a provider to a client, optional per-client credential override (admin)

    Args:
        slug (str):
        provider_slug (str):
        body (PutOauthClientsSlugProvidersProviderSlugBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PutOauthClientsSlugProvidersProviderSlugResponse200]]
     """


    kwargs = _get_kwargs(
        slug=slug,
provider_slug=provider_slug,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    slug: str,
    provider_slug: str,
    *,
    client: AuthenticatedClient,
    body: PutOauthClientsSlugProvidersProviderSlugBody,

) -> Optional[Union[Error, PutOauthClientsSlugProvidersProviderSlugResponse200]]:
    """ Link a provider to a client, optional per-client credential override (admin)

    Args:
        slug (str):
        provider_slug (str):
        body (PutOauthClientsSlugProvidersProviderSlugBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PutOauthClientsSlugProvidersProviderSlugResponse200]
     """


    return sync_detailed(
        slug=slug,
provider_slug=provider_slug,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    slug: str,
    provider_slug: str,
    *,
    client: AuthenticatedClient,
    body: PutOauthClientsSlugProvidersProviderSlugBody,

) -> Response[Union[Error, PutOauthClientsSlugProvidersProviderSlugResponse200]]:
    """ Link a provider to a client, optional per-client credential override (admin)

    Args:
        slug (str):
        provider_slug (str):
        body (PutOauthClientsSlugProvidersProviderSlugBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PutOauthClientsSlugProvidersProviderSlugResponse200]]
     """


    kwargs = _get_kwargs(
        slug=slug,
provider_slug=provider_slug,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    slug: str,
    provider_slug: str,
    *,
    client: AuthenticatedClient,
    body: PutOauthClientsSlugProvidersProviderSlugBody,

) -> Optional[Union[Error, PutOauthClientsSlugProvidersProviderSlugResponse200]]:
    """ Link a provider to a client, optional per-client credential override (admin)

    Args:
        slug (str):
        provider_slug (str):
        body (PutOauthClientsSlugProvidersProviderSlugBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PutOauthClientsSlugProvidersProviderSlugResponse200]
     """


    return (await asyncio_detailed(
        slug=slug,
provider_slug=provider_slug,
client=client,
body=body,

    )).parsed
