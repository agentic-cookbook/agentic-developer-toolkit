from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.project_activity import ProjectActivity
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    id: str,
    *,
    limit: Union[Unset, str] = UNSET,
    before: Union[Unset, str] = UNSET,
    before_id: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["before"] = before

    params["beforeId"] = before_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/project/work-items/{id}/activity".format(id=id,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Error, list['ProjectActivity']]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = ProjectActivity.from_dict(response_200_item_data)



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Error, list['ProjectActivity']]]:
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
    limit: Union[Unset, str] = UNSET,
    before: Union[Unset, str] = UNSET,
    before_id: Union[Unset, str] = UNSET,

) -> Response[Union[Error, list['ProjectActivity']]]:
    """ A work item's activity trail (newest first, keyset-paginated)

    Args:
        id (str):
        limit (Union[Unset, str]):
        before (Union[Unset, str]):
        before_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, list['ProjectActivity']]]
     """


    kwargs = _get_kwargs(
        id=id,
limit=limit,
before=before,
before_id=before_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, str] = UNSET,
    before: Union[Unset, str] = UNSET,
    before_id: Union[Unset, str] = UNSET,

) -> Optional[Union[Error, list['ProjectActivity']]]:
    """ A work item's activity trail (newest first, keyset-paginated)

    Args:
        id (str):
        limit (Union[Unset, str]):
        before (Union[Unset, str]):
        before_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, list['ProjectActivity']]
     """


    return sync_detailed(
        id=id,
client=client,
limit=limit,
before=before,
before_id=before_id,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, str] = UNSET,
    before: Union[Unset, str] = UNSET,
    before_id: Union[Unset, str] = UNSET,

) -> Response[Union[Error, list['ProjectActivity']]]:
    """ A work item's activity trail (newest first, keyset-paginated)

    Args:
        id (str):
        limit (Union[Unset, str]):
        before (Union[Unset, str]):
        before_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, list['ProjectActivity']]]
     """


    kwargs = _get_kwargs(
        id=id,
limit=limit,
before=before,
before_id=before_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, str] = UNSET,
    before: Union[Unset, str] = UNSET,
    before_id: Union[Unset, str] = UNSET,

) -> Optional[Union[Error, list['ProjectActivity']]]:
    """ A work item's activity trail (newest first, keyset-paginated)

    Args:
        id (str):
        limit (Union[Unset, str]):
        before (Union[Unset, str]):
        before_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, list['ProjectActivity']]
     """


    return (await asyncio_detailed(
        id=id,
client=client,
limit=limit,
before=before,
before_id=before_id,

    )).parsed
