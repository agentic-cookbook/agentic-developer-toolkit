from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ai_processing_webhook_endpoint import AiProcessingWebhookEndpoint
from ...models.error import Error
from ...models.patch_ai_processing_webhooks_id_body import PatchAiProcessingWebhooksIdBody
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: PatchAiProcessingWebhooksIdBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/ai-processing/webhooks/{id}".format(id=id,),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[AiProcessingWebhookEndpoint, Error]]:
    if response.status_code == 200:
        response_200 = AiProcessingWebhookEndpoint.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[AiProcessingWebhookEndpoint, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchAiProcessingWebhooksIdBody,

) -> Response[Union[AiProcessingWebhookEndpoint, Error]]:
    """ Update a webhook endpoint (active / eventTypes)

     Toggle `active` or replace `eventTypes`. The URL and secret are immutable after creation. Returns
    404 when not found or owned by another ecosystem.

    Args:
        id (str):
        body (PatchAiProcessingWebhooksIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AiProcessingWebhookEndpoint, Error]]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchAiProcessingWebhooksIdBody,

) -> Optional[Union[AiProcessingWebhookEndpoint, Error]]:
    """ Update a webhook endpoint (active / eventTypes)

     Toggle `active` or replace `eventTypes`. The URL and secret are immutable after creation. Returns
    404 when not found or owned by another ecosystem.

    Args:
        id (str):
        body (PatchAiProcessingWebhooksIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AiProcessingWebhookEndpoint, Error]
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchAiProcessingWebhooksIdBody,

) -> Response[Union[AiProcessingWebhookEndpoint, Error]]:
    """ Update a webhook endpoint (active / eventTypes)

     Toggle `active` or replace `eventTypes`. The URL and secret are immutable after creation. Returns
    404 when not found or owned by another ecosystem.

    Args:
        id (str):
        body (PatchAiProcessingWebhooksIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AiProcessingWebhookEndpoint, Error]]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchAiProcessingWebhooksIdBody,

) -> Optional[Union[AiProcessingWebhookEndpoint, Error]]:
    """ Update a webhook endpoint (active / eventTypes)

     Toggle `active` or replace `eventTypes`. The URL and secret are immutable after creation. Returns
    404 when not found or owned by another ecosystem.

    Args:
        id (str):
        body (PatchAiProcessingWebhooksIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AiProcessingWebhookEndpoint, Error]
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
