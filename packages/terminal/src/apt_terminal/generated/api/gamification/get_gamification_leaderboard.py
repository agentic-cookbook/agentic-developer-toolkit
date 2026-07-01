from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.gamification_leaderboard import GamificationLeaderboard
from ...models.get_gamification_leaderboard_period import GetGamificationLeaderboardPeriod
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    subject_type: Union[Unset, str] = 'user',
    period: Union[Unset, GetGamificationLeaderboardPeriod] = GetGamificationLeaderboardPeriod.ALL,
    page: Union[Unset, str] = UNSET,
    page_size: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["subjectType"] = subject_type

    json_period: Union[Unset, str] = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period

    params["page"] = page

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gamification/leaderboard",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Error, GamificationLeaderboard]]:
    if response.status_code == 200:
        response_200 = GamificationLeaderboard.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Error, GamificationLeaderboard]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    subject_type: Union[Unset, str] = 'user',
    period: Union[Unset, GetGamificationLeaderboardPeriod] = GetGamificationLeaderboardPeriod.ALL,
    page: Union[Unset, str] = UNSET,
    page_size: Union[Unset, str] = UNSET,

) -> Response[Union[Error, GamificationLeaderboard]]:
    """ Ranked leaderboard by summed points for a subject kind

    Args:
        subject_type (Union[Unset, str]):  Default: 'user'.
        period (Union[Unset, GetGamificationLeaderboardPeriod]):  Default:
            GetGamificationLeaderboardPeriod.ALL.
        page (Union[Unset, str]):
        page_size (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GamificationLeaderboard]]
     """


    kwargs = _get_kwargs(
        subject_type=subject_type,
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
    subject_type: Union[Unset, str] = 'user',
    period: Union[Unset, GetGamificationLeaderboardPeriod] = GetGamificationLeaderboardPeriod.ALL,
    page: Union[Unset, str] = UNSET,
    page_size: Union[Unset, str] = UNSET,

) -> Optional[Union[Error, GamificationLeaderboard]]:
    """ Ranked leaderboard by summed points for a subject kind

    Args:
        subject_type (Union[Unset, str]):  Default: 'user'.
        period (Union[Unset, GetGamificationLeaderboardPeriod]):  Default:
            GetGamificationLeaderboardPeriod.ALL.
        page (Union[Unset, str]):
        page_size (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GamificationLeaderboard]
     """


    return sync_detailed(
        client=client,
subject_type=subject_type,
period=period,
page=page,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    subject_type: Union[Unset, str] = 'user',
    period: Union[Unset, GetGamificationLeaderboardPeriod] = GetGamificationLeaderboardPeriod.ALL,
    page: Union[Unset, str] = UNSET,
    page_size: Union[Unset, str] = UNSET,

) -> Response[Union[Error, GamificationLeaderboard]]:
    """ Ranked leaderboard by summed points for a subject kind

    Args:
        subject_type (Union[Unset, str]):  Default: 'user'.
        period (Union[Unset, GetGamificationLeaderboardPeriod]):  Default:
            GetGamificationLeaderboardPeriod.ALL.
        page (Union[Unset, str]):
        page_size (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GamificationLeaderboard]]
     """


    kwargs = _get_kwargs(
        subject_type=subject_type,
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
    subject_type: Union[Unset, str] = 'user',
    period: Union[Unset, GetGamificationLeaderboardPeriod] = GetGamificationLeaderboardPeriod.ALL,
    page: Union[Unset, str] = UNSET,
    page_size: Union[Unset, str] = UNSET,

) -> Optional[Union[Error, GamificationLeaderboard]]:
    """ Ranked leaderboard by summed points for a subject kind

    Args:
        subject_type (Union[Unset, str]):  Default: 'user'.
        period (Union[Unset, GetGamificationLeaderboardPeriod]):  Default:
            GetGamificationLeaderboardPeriod.ALL.
        page (Union[Unset, str]):
        page_size (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GamificationLeaderboard]
     """


    return (await asyncio_detailed(
        client=client,
subject_type=subject_type,
period=period,
page=page,
page_size=page_size,

    )).parsed
