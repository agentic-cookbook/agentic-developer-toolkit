from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_project_projects_id_artifacts_direction import GetProjectProjectsIdArtifactsDirection
from ...models.get_project_projects_id_artifacts_response_200 import GetProjectProjectsIdArtifactsResponse200
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    id: str,
    *,
    direction: Union[Unset, GetProjectProjectsIdArtifactsDirection] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_direction: Union[Unset, str] = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction.value

    params["direction"] = json_direction


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/project/projects/{id}/artifacts".format(id=id,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Error, GetProjectProjectsIdArtifactsResponse200]]:
    if response.status_code == 200:
        response_200 = GetProjectProjectsIdArtifactsResponse200.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Error, GetProjectProjectsIdArtifactsResponse200]]:
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
    direction: Union[Unset, GetProjectProjectsIdArtifactsDirection] = UNSET,

) -> Response[Union[Error, GetProjectProjectsIdArtifactsResponse200]]:
    """ List a project's artifacts (newest first), optionally filtered by direction

    Args:
        id (str):
        direction (Union[Unset, GetProjectProjectsIdArtifactsDirection]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GetProjectProjectsIdArtifactsResponse200]]
     """


    kwargs = _get_kwargs(
        id=id,
direction=direction,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    direction: Union[Unset, GetProjectProjectsIdArtifactsDirection] = UNSET,

) -> Optional[Union[Error, GetProjectProjectsIdArtifactsResponse200]]:
    """ List a project's artifacts (newest first), optionally filtered by direction

    Args:
        id (str):
        direction (Union[Unset, GetProjectProjectsIdArtifactsDirection]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GetProjectProjectsIdArtifactsResponse200]
     """


    return sync_detailed(
        id=id,
client=client,
direction=direction,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    direction: Union[Unset, GetProjectProjectsIdArtifactsDirection] = UNSET,

) -> Response[Union[Error, GetProjectProjectsIdArtifactsResponse200]]:
    """ List a project's artifacts (newest first), optionally filtered by direction

    Args:
        id (str):
        direction (Union[Unset, GetProjectProjectsIdArtifactsDirection]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GetProjectProjectsIdArtifactsResponse200]]
     """


    kwargs = _get_kwargs(
        id=id,
direction=direction,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    direction: Union[Unset, GetProjectProjectsIdArtifactsDirection] = UNSET,

) -> Optional[Union[Error, GetProjectProjectsIdArtifactsResponse200]]:
    """ List a project's artifacts (newest first), optionally filtered by direction

    Args:
        id (str):
        direction (Union[Unset, GetProjectProjectsIdArtifactsDirection]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GetProjectProjectsIdArtifactsResponse200]
     """


    return (await asyncio_detailed(
        id=id,
client=client,
direction=direction,

    )).parsed
