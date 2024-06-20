from nonebot import get_plugin_config
from pydantic import BaseModel


class Config(BaseModel):
    chatrecorder_record_send_msg: bool = True


plugin_name = 'nonebot_plugin_obastatus'
plugin_version = 'v1.0.1'
plugin_config = get_plugin_config(Config)