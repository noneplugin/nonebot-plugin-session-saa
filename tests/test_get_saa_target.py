from nonebug.app import App


def test_target_qq(app: App):
    from nonebot_plugin_saa import TargetQQGroup, TargetQQPrivate
    from nonebot_plugin_session import Session, SessionLevel

    from nonebot_plugin_session_saa import get_saa_target

    session = Session(
        bot_id="2233",
        bot_type="OneBot V11",
        platform="qq",
        level=SessionLevel.LEVEL2,
        id1="3344",
        id2="1122",
        id3=None,
    )
    target = get_saa_target(session)
    assert target
    assert isinstance(target, TargetQQGroup)
    assert str(target.group_id) == "1122"

    session = Session(
        bot_id="2233",
        bot_type="OneBot V11",
        platform="qq",
        level=SessionLevel.LEVEL1,
        id1="3344",
        id2=None,
        id3=None,
    )
    target = get_saa_target(session)
    assert target
    assert isinstance(target, TargetQQPrivate)
    assert str(target.user_id) == "3344"


def test_target_qqguild(app: App):
    from nonebot_plugin_saa import TargetQQGuildChannel, TargetQQGuildDirect
    from nonebot_plugin_session import Session, SessionLevel

    from nonebot_plugin_session_saa import get_saa_target

    session = Session(
        bot_id="2233",
        bot_type="QQGuild",
        platform="qqguild",
        level=SessionLevel.LEVEL1,
        id1="3344",
        id2=None,
        id3="1122",
    )
    target = get_saa_target(session)
    assert target
    assert isinstance(target, TargetQQGuildDirect)
    assert str(target.recipient_id) == "3344"
    assert str(target.source_guild_id) == "1122"

    session = Session(
        bot_id="2233",
        bot_type="QQGuild",
        platform="qqguild",
        level=SessionLevel.LEVEL3,
        id1=None,
        id2="3344",
        id3="1122",
    )
    target = get_saa_target(session)
    assert target
    assert isinstance(target, TargetQQGuildChannel)
    assert str(target.channel_id) == "3344"


def test_target_kaiheila(app: App):
    from nonebot_plugin_saa import TargetKaiheilaChannel, TargetKaiheilaPrivate
    from nonebot_plugin_session import Session, SessionLevel

    from nonebot_plugin_session_saa import get_saa_target

    session = Session(
        bot_id="2233",
        bot_type="Kaiheila",
        platform="kaiheila",
        level=SessionLevel.LEVEL1,
        id1="3344",
        id2=None,
        id3=None,
    )
    target = get_saa_target(session)
    assert target
    assert isinstance(target, TargetKaiheilaPrivate)
    assert target.user_id == "3344"

    session = Session(
        bot_id="2233",
        bot_type="Kaiheila",
        platform="kaiheila",
        level=SessionLevel.LEVEL3,
        id1="5566",
        id2="3344",
        id3="1122",
    )
    target = get_saa_target(session)
    assert target
    assert isinstance(target, TargetKaiheilaChannel)
    assert target.channel_id == "3344"


def test_target_feishu(app: App):
    from nonebot_plugin_saa import TargetFeishuGroup, TargetFeishuPrivate
    from nonebot_plugin_session import Session, SessionLevel

    from nonebot_plugin_session_saa import get_saa_target

    session = Session(
        bot_id="2233",
        bot_type="Feishu",
        platform="feishu",
        level=SessionLevel.LEVEL1,
        id1="3344",
        id2=None,
        id3=None,
    )
    target = get_saa_target(session)
    assert target
    assert isinstance(target, TargetFeishuPrivate)
    assert target.open_id == "3344"

    session = Session(
        bot_id="2233",
        bot_type="Feishu",
        platform="feishu",
        level=SessionLevel.LEVEL2,
        id1="5566",
        id2="3344",
        id3=None,
    )
    target = get_saa_target(session)
    assert target
    assert isinstance(target, TargetFeishuGroup)
    assert target.chat_id == "3344"


def test_target_onebot_v12_unknown(app: App):
    from nonebot_plugin_saa import TargetOB12Unknow
    from nonebot_plugin_session import Session, SessionLevel

    from nonebot_plugin_session_saa import get_saa_target

    session = Session(
        bot_id="2233",
        bot_type="OneBot V12",
        platform="onebot_v12",
        level=SessionLevel.LEVEL1,
        id1="3344",
        id2=None,
        id3=None,
    )
    target = get_saa_target(session)
    assert target
    assert isinstance(target, TargetOB12Unknow)
    assert target.user_id == "3344"
    assert target.detail_type == "private"

    session = Session(
        bot_id="2233",
        bot_type="OneBot V12",
        platform="onebot_v12",
        level=SessionLevel.LEVEL2,
        id1="5566",
        id2="3344",
        id3=None,
    )
    target = get_saa_target(session)
    assert target
    assert isinstance(target, TargetOB12Unknow)
    assert target.group_id == "3344"
    assert target.detail_type == "group"

    session = Session(
        bot_id="2233",
        bot_type="OneBot V12",
        platform="onebot_v12",
        level=SessionLevel.LEVEL3,
        id1="5566",
        id2="3344",
        id3="1122",
    )
    target = get_saa_target(session)
    assert target
    assert isinstance(target, TargetOB12Unknow)
    assert target.channel_id == "3344"
    assert target.guild_id == "1122"
    assert target.detail_type == "channel"
