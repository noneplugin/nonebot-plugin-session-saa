import pytest
from nonebot import require
from nonebug import App


@pytest.fixture
async def app():
    require("nonebot_plugin_session_saa")

    yield App()
