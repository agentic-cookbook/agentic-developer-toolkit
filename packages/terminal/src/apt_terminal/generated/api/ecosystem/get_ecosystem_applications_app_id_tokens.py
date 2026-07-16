from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_token import ApiToken
from ...models.error import Error
from typing import cast



def _get_kwargs(
    app_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ecosystem/applications/{app_id}/tokens".format(app_id=app_id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Error, list['ApiToken']]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = ApiToken.from_dict(response_200_item_data)



            response_200.append(response_200_item)

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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Error, list['ApiToken']]]:
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

) -> Response[Union[Error, list['ApiToken']]]:
    """ List an application’s API tokens (metadata only; raw values never returned)

    Args:
        app_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, list['ApiToken']]]
     """


    kwargs = _get_kwargs(
        app_id=app_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    app_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Error, list['ApiToken']]]:
    """ List an application’s API tokens (metadata only; raw values never returned)

    Args:
        app_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, list['ApiToken']]
     """


    return sync_detailed(
        app_id=app_id,
client=client,

    ).parsed

async def asyncio_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Error, list['ApiToken']]]:
    """ List an application’s API tokens (metadata only; raw values never returned)

    Args:
        app_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, list['ApiToken']]]
     """


    kwargs = _get_kwargs(
        app_id=app_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    app_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Error, list['ApiToken']]]:
    """ List an application’s API tokens (metadata only; raw values never returned)

    Args:
        app_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, list['ApiToken']]
     """


    return (await asyncio_detailed(
        app_id=app_id,
client=client,

    )).parsed
