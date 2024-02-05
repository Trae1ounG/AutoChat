import autogen
import json
from characters.CharacterAgent import CharacterAgent, get_character
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
    llm_config = {"config_list": config_list_gpt, "cache_seed": 43}

    #角色描述文件
    character_details = './characters/characters_guobao.json'
    
    #获取角色Agent
    all_agent, all_actual_name = choice_characters(character_details,llm_config)
    
    #获取用户Agent
    user_character, user_actual_name = decide_your_character(default_name="shangguanziyi",default_actual_name="上官子怡",default_system_message="""你将扮演《果宝特攻》中的上官子怡，每次只代表自己角色说一句话。一个漂亮稳重的草莓，橙留香的女朋友。上官世家的小姐，家里几代为官，地位尊贵。上官金虹（上官子怡的母亲）的掌上明珠。父亲张三丰，朝廷的海军大臣。她原本叫张子怡，却因为父母离异而改姓上官。称呼：子怡姐、子怡、子怡小姐。性格：优雅，成熟""")
    all_agent.append(user_character)
    groupchat = autogen.GroupChat(agents=all_agent, messages=[],max_round=int(1e9))
    guodong = CharacterGroupMangaer(system_message="作为果冻武术学院的跑腿小弟，负责传递消息",name='guodong',groupchat=groupchat, llm_config=llm_config)

    #开始聊天
    start_msg = """橙留香，东方求败来了！"""
    user_character.initiate_chat(
        guodong,message=start_msg
    )