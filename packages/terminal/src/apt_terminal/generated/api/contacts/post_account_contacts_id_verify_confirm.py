from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.post_account_contacts_id_verify_confirm_body import PostAccountContactsIdVerifyConfirmBody
from ...models.post_account_contacts_id_verify_confirm_response_200 import PostAccountContactsIdVerifyConfirmResponse200
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: PostAccountContactsIdVerifyConfirmBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/account/contacts/{id}/verify/confirm".format(id=id,),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Error, PostAccountContactsIdVerifyConfirmResponse200]]:
    if response.status_code == 200:
        response_200 = PostAccountContactsIdVerifyConfirmResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Error, PostAccountContactsIdVerifyConfirmResponse200]]:
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
    body: PostAccountContactsIdVerifyConfirmBody,

) -> Response[Union[Error, PostAccountContactsIdVerifyConfirmResponse200]]:
    """ Confirm a contact with the code that was sent

    Args:
        id (str):
        body (PostAccountContactsIdVerifyConfirmBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PostAccountContactsIdVerifyConfirmResponse200]]
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
    body: PostAccountContactsIdVerifyConfirmBody,

) -> Optional[Union[Error, PostAccountContactsIdVerifyConfirmResponse200]]:
    """ Confirm a contact with the code that was sent

    Args:
        id (str):
        body (PostAccountContactsIdVerifyConfirmBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PostAccountContactsIdVerifyConfirmResponse200]
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
    body: PostAccountContactsIdVerifyConfirmBody,

) -> Response[Union[Error, PostAccountContactsIdVerifyConfirmResponse200]]:
    """ Confirm a contact with the code that was sent

    Args:
        id (str):
        body (PostAccountContactsIdVerifyConfirmBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PostAccountContactsIdVerifyConfirmResponse200]]
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
    body: PostAccountContactsIdVerifyConfirmBody,

) -> Optional[Union[Error, PostAccountContactsIdVerifyConfirmResponse200]]:
    """ Confirm a contact with the code that was sent

    Args:
        id (str):
        body (PostAccountContactsIdVerifyConfirmBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PostAccountContactsIdVerifyConfirmResponse200]
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
