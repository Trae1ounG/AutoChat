import json
from characters.CharacterAgent import CharacterAgent, get_character
import autogen

def choice_characters(character_details,llm_config,choose_all=True):
    """
    选择参与角色
    Args:
        character_details : json文件存放处
        llm_config : Agent配置字典
        choose_all (bool, optional): 是否选择所有角色. Defaults to True.

    Returns:
        所有被选择的Agent列表
    """
    with open(character_details,'r',encoding='utf-8') as f:
        character_ = json.load(f)
    selected_list = []
    if not choose_all:
        for idx in range(len(character_)):
            print(f"是否选择角色:{character_[idx]['actual_name']}\n请输入Y/F")
            user_input = input()
            while True:
                if user_input not in ('Y','F'):
                    print("输入错误,请输入Y/F")
                    user_input = input()
                    continue
                else:
                    break
            if user_input == 'Y':
                selected_list.append(idx)
                print(f"选择{character_[idx]['actual_name']}成功")
    else:
        selected_list = range(len(character_))
    selected_character = [character_[selected_idx] for selected_idx in selected_list]
    all_agent = []
    all_actual_name = []
    for character in selected_character:
        name, actual_name, system_message, description = character.values()
        all_agent.append(get_character(name,system_message,description,llm_config))
        all_actual_name.append(actual_name)
    print(f'已选择角色:{",".join(all_actual_name)}')
    return all_agent, all_actual_name

def decide_your_character(default_name, default_actual_name, default_system_message):
    """
    定制用户角色
    Args:
        default_name (String): 角色名描述(英文)
        default_actual_name (String): 角色名(中文)
        default_system_message (String): 默认角色系统消息

    Returns:
        user_character: 用户角色的Agent
        default_actual_name: 用户角色名
    """
    user_character = autogen.UserProxyAgent(
        name=default_name,
        is_termination_msg= lambda x: x.get('content',None).rstrip().endswith("TERMINATE") ,
        human_input_mode="ALWAYS",
        system_message=default_system_message,
        max_consecutive_auto_reply=10000,
        code_execution_config= {
            'use_docker':False,
            "work_dir" : f'./chat_as_{default_name}'
        }
    )
    return user_character, default_actual_name