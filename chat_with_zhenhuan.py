import autogen
import json
from characters.CharacterAgent import CharacterAgent
from characters.CharacterGroupManager import CharacterGroupMangaer
from chat_function import *

if __name__ == '__main__':
    config_list_gpt = autogen.config_list_from_json(
    "./OAI_CONFIG_LIST.json",
        filter_dict={
            #选择你使用的模型
            "model": ["gpt-3.5-turbo"],
        },
    )
    #模型配置
    llm_config = {"config_list": config_list_gpt, "cache_seed": 42}

    #角色描述文件
    character_details = './characters/characters_zhenhuanzhuan.json'
    
    #获取角色Agent
    all_agent, all_actual_name = choice_characters(character_details=character_details,llm_config=llm_config)
   
    #获取用户Agent
    user_character, user_actual_name = decide_your_character(default_name="huangshang",default_actual_name="皇上",default_system_message="你现在在《甄嬛传》角色扮演中，你扮演的角色是皇上，你对后宫都很宠爱，需要及时回复后宫")
    all_agent.append(user_character)
    groupchat = autogen.GroupChat(agents=all_agent, messages=[],max_round=int(1e9))
    huanggong = CharacterGroupMangaer(system_message="""你在《甄嬛传》中负责替为所有角色传递消息。""",name='huanggong',groupchat=groupchat, llm_config=llm_config)
    
    #开始聊天
    start_msg = """帮朕传甄嬛该斩！"""
    user_character.initiate_chat(
        huanggong,message=start_msg
    )