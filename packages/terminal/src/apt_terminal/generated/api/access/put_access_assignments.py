from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.access_assignment_envelope import AccessAssignmentEnvelope
from ...models.error import Error
from ...models.put_access_assignments_body import PutAccessAssignmentsBody
from typing import cast



def _get_kwargs(
    *,
    body: PutAccessAssignmentsBody,
    workspace: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["workspace"] = workspace


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/access/assignments",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[AccessAssignmentEnvelope, Error]]:
    if response.status_code == 200:
        response_200 = AccessAssignmentEnvelope.from_dict(response.json())



        return response_200

    if response.status_code == 201:
        response_201 = AccessAssignmentEnvelope.from_dict(response.json())



        return response_201

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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[AccessAssignmentEnvelope, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PutAccessAssignmentsBody,
    workspace: str,

) -> Response[Union[AccessAssignmentEnvelope, Error]]:
    """ Grant (or replace) a role for a subject at a scope — requires M + no-escalation

    Args:
        workspace (str):
        body (PutAccessAssignmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccessAssignmentEnvelope, Error]]
     """


    kwargs = _get_kwargs(
        body=body,
workspace=workspace,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: PutAccessAssignmentsBody,
    workspace: str,

) -> Optional[Union[AccessAssignmentEnvelope, Error]]:
    """ Grant (or replace) a role for a subject at a scope — requires M + no-escalation

    Args:
        workspace (str):
        body (PutAccessAssignmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccessAssignmentEnvelope, Error]
     """


    return sync_detailed(
        client=client,
body=body,
workspace=workspace,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PutAccessAssignmentsBody,
    workspace: str,

) -> Response[Union[AccessAssignmentEnvelope, Error]]:
    """ Grant (or replace) a role for a subject at a scope — requires M + no-escalation

    Args:
        workspace (str):
        body (PutAccessAssignmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccessAssignmentEnvelope, Error]]
     """


    kwargs = _get_kwargs(
        body=body,
workspace=workspace,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PutAccessAssignmentsBody,
    workspace: str,

) -> Optional[Union[AccessAssignmentEnvelope, Error]]:
    """ Grant (or replace) a role for a subject at a scope — requires M + no-escalation

    Args:
        workspace (str):
        body (PutAccessAssignmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccessAssignmentEnvelope, Error]
     """


    return (await asyncio_detailed(
        client=client,
body=body,
workspace=workspace,

    )).parsed
