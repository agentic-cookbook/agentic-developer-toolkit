from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.eco_managed_row import EcoManagedRow
from ...models.error import Error
from typing import cast



def _get_kwargs(
    ecosystem_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/auth/ecosystems/{ecosystem_id}/pending-users".format(ecosystem_id=ecosystem_id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Error, list['EcoManagedRow']]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_eco_managed_row_list_item_data in (_response_200):
            componentsschemas_eco_managed_row_list_item = EcoManagedRow.from_dict(componentsschemas_eco_managed_row_list_item_data)



            response_200.append(componentsschemas_eco_managed_row_list_item)

        return response_200

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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Error, list['EcoManagedRow']]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ecosystem_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Error, list['EcoManagedRow']]]:
    """ List an ecosystem’s pending users (owner-scoped)

    Args:
        ecosystem_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, list['EcoManagedRow']]]
     """


    kwargs = _get_kwargs(
        ecosystem_id=ecosystem_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    ecosystem_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Error, list['EcoManagedRow']]]:
    """ List an ecosystem’s pending users (owner-scoped)

    Args:
        ecosystem_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, list['EcoManagedRow']]
     """


    return sync_detailed(
        ecosystem_id=ecosystem_id,
client=client,

    ).parsed

async def asyncio_detailed(
    ecosystem_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Error, list['EcoManagedRow']]]:
    """ List an ecosystem’s pending users (owner-scoped)

    Args:
        ecosystem_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, list['EcoManagedRow']]]
     """


    kwargs = _get_kwargs(
        ecosystem_id=ecosystem_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    ecosystem_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Error, list['EcoManagedRow']]]:
    """ List an ecosystem’s pending users (owner-scoped)

    Args:
        ecosystem_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, list['EcoManagedRow']]
     """


    return (await asyncio_detailed(
        ecosystem_id=ecosystem_id,
client=client,

    )).parsed
