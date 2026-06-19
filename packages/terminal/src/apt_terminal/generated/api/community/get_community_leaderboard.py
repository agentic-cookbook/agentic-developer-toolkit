from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.community_leaderboard import CommunityLeaderboard
from ...models.error import Error
from ...models.get_community_leaderboard_period import GetCommunityLeaderboardPeriod
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    period: GetCommunityLeaderboardPeriod | Unset = GetCommunityLeaderboardPeriod.ALL,
    page: str | Unset = UNSET,
    page_size: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period

    params["page"] = page

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/community/leaderboard",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CommunityLeaderboard | Error | None:
    if response.status_code == 200:
        response_200 = CommunityLeaderboard.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CommunityLeaderboard | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    period: GetCommunityLeaderboardPeriod | Unset = GetCommunityLeaderboardPeriod.ALL,
    page: str | Unset = UNSET,
    page_size: str | Unset = UNSET,

) -> Response[CommunityLeaderboard | Error]:
    """ Ranked leaderboard by summed points for the caller’s ecosystem

    Args:
        period (GetCommunityLeaderboardPeriod | Unset):  Default:
            GetCommunityLeaderboardPeriod.ALL.
        page (str | Unset):
        page_size (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommunityLeaderboard | Error]
     """


    kwargs = _get_kwargs(
        period=period,
page=page,
page_size=page_size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    period: GetCommunityLeaderboardPeriod | Unset = GetCommunityLeaderboardPeriod.ALL,
    page: str | Unset = UNSET,
    page_size: str | Unset = UNSET,

) -> CommunityLeaderboard | Error | None:
    """ Ranked leaderboard by summed points for the caller’s ecosystem

    Args:
        period (GetCommunityLeaderboardPeriod | Unset):  Default:
            GetCommunityLeaderboardPeriod.ALL.
        page (str | Unset):
        page_size (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommunityLeaderboard | Error
     """


    return sync_detailed(
        client=client,
period=period,
page=page,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    period: GetCommunityLeaderboardPeriod | Unset = GetCommunityLeaderboardPeriod.ALL,
    page: str | Unset = UNSET,
    page_size: str | Unset = UNSET,

) -> Response[CommunityLeaderboard | Error]:
    """ Ranked leaderboard by summed points for the caller’s ecosystem

    Args:
        period (GetCommunityLeaderboardPeriod | Unset):  Default:
            GetCommunityLeaderboardPeriod.ALL.
        page (str | Unset):
        page_size (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommunityLeaderboard | Error]
     """


    kwargs = _get_kwargs(
        period=period,
page=page,
page_size=page_size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    period: GetCommunityLeaderboardPeriod | Unset = GetCommunityLeaderboardPeriod.ALL,
    page: str | Unset = UNSET,
    page_size: str | Unset = UNSET,

) -> CommunityLeaderboard | Error | None:
    """ Ranked leaderboard by summed points for the caller’s ecosystem

    Args:
        period (GetCommunityLeaderboardPeriod | Unset):  Default:
            GetCommunityLeaderboardPeriod.ALL.
        page (str | Unset):
        page_size (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommunityLeaderboard | Error
     """


    return (await asyncio_detailed(
        client=client,
period=period,
page=page,
page_size=page_size,

    )).parsed
