from __future__ import annotations

from collections.abc import Iterator

import pytest
import respx


@pytest.fixture
def mock_router() -> Iterator[respx.MockRouter]:
    with respx.mock(assert_all_called=False) as router:
        yield router
