from autogen.agentchat.groupchat import GroupChatManager
from autogen.agentchat.groupchat import GroupChat
from typing import Dict, List, Optional, Union, Tuple
import sys


class CharacterGroupMangaer(GroupChatManager):
    
    def __init__(
        self,
        groupchat: GroupChat,
        name: Optional[str] = "",
        # unlimited consecutive auto reply by default
        max_consecutive_auto_reply: Optional[int] = int(1e9),
        human_input_mode: Optional[str] = "NEVER",
        system_message: Optional[Union[str, List]]="",
        **kwargs,
    ):
        super().__init__(
            groupchat=groupchat,
            name=name,
            max_consecutive_auto_reply=max_consecutive_auto_reply,
            human_input_mode=human_input_mode,
            system_message=system_message,
            **kwargs,
        )
# def set_groupmanager(name,system_message,llm_config):
#     group_manager = CharacterGroupMangaer(name=name,system_message=system_message,llm_config=llm_config)
#     return group_manager