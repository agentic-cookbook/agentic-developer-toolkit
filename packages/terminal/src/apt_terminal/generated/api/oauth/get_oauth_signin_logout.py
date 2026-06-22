from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    client_id: Union[Unset, str] = UNSET,
    return_: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["clientId"] = client_id

    params["return"] = return_


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/oauth/signin/logout",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, Error]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 302:
        response_302 = cast(Any, None)
        return response_302

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

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
    *,
    client: Union[AuthenticatedClient, Client],
    client_id: Union[Unset, str] = UNSET,
    return_: Union[Unset, str] = UNSET,

) -> Response[Union[Any, Error]]:
    """ Central single-logout (browser) — revoke + clear the SSO cookie, then 302 back

    Args:
        client_id (Union[Unset, str]):
        return_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
return_=return_,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    client_id: Union[Unset, str] = UNSET,
    return_: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, Error]]:
    """ Central single-logout (browser) — revoke + clear the SSO cookie, then 302 back

    Args:
        client_id (Union[Unset, str]):
        return_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error]
     """


    return sync_detailed(
        client=client,
client_id=client_id,
return_=return_,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    client_id: Union[Unset, str] = UNSET,
    return_: Union[Unset, str] = UNSET,

) -> Response[Union[Any, Error]]:
    """ Central single-logout (browser) — revoke + clear the SSO cookie, then 302 back

    Args:
        client_id (Union[Unset, str]):
        return_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
return_=return_,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    client_id: Union[Unset, str] = UNSET,
    return_: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, Error]]:
    """ Central single-logout (browser) — revoke + clear the SSO cookie, then 302 back

    Args:
        client_id (Union[Unset, str]):
        return_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error]
     """


    return (await asyncio_detailed(
        client=client,
client_id=client_id,
return_=return_,

    )).parsed
