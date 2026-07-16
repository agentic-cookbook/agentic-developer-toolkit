from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.put_ecosystem_applications_app_id_schema_grants_body import PutEcosystemApplicationsAppIdSchemaGrantsBody
from typing import cast



def _get_kwargs(
    app_id: str,
    *,
    body: PutEcosystemApplicationsAppIdSchemaGrantsBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/ecosystem/applications/{app_id}/schema-grants".format(app_id=app_id,),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, Error]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: PutEcosystemApplicationsAppIdSchemaGrantsBody,

) -> Response[Union[Any, Error]]:
    """ Reconcile an application’s schema permissions

     Persists the app’s grants as per-app bucket access-groups. Buckets must belong to the app’s
    ecosystem (404 otherwise); each table must belong to its bucket.

    Args:
        app_id (str):
        body (PutEcosystemApplicationsAppIdSchemaGrantsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
     """


    kwargs = _get_kwargs(
        app_id=app_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: PutEcosystemApplicationsAppIdSchemaGrantsBody,

) -> Optional[Union[Any, Error]]:
    """ Reconcile an application’s schema permissions

     Persists the app’s grants as per-app bucket access-groups. Buckets must belong to the app’s
    ecosystem (404 otherwise); each table must belong to its bucket.

    Args:
        app_id (str):
        body (PutEcosystemApplicationsAppIdSchemaGrantsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error]
     """


    return sync_detailed(
        app_id=app_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: PutEcosystemApplicationsAppIdSchemaGrantsBody,

) -> Response[Union[Any, Error]]:
    """ Reconcile an application’s schema permissions

     Persists the app’s grants as per-app bucket access-groups. Buckets must belong to the app’s
    ecosystem (404 otherwise); each table must belong to its bucket.

    Args:
        app_id (str):
        body (PutEcosystemApplicationsAppIdSchemaGrantsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
     """


    kwargs = _get_kwargs(
        app_id=app_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: PutEcosystemApplicationsAppIdSchemaGrantsBody,

) -> Optional[Union[Any, Error]]:
    """ Reconcile an application’s schema permissions

     Persists the app’s grants as per-app bucket access-groups. Buckets must belong to the app’s
    ecosystem (404 otherwise); each table must belong to its bucket.

    Args:
        app_id (str):
        body (PutEcosystemApplicationsAppIdSchemaGrantsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error]
     """


    return (await asyncio_detailed(
        app_id=app_id,
client=client,
body=body,

    )).parsed
