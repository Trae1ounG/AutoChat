import autogen
from characters.huanhuan_assistant_agent import HuanHuanAssistant
from characters.huafei_assistant_agent import HuaFeiAssistant
from characters.HuangGong_group_manager import HuangGongChatMangaer
from characters.taijian_assistant_agent import TaiJianAssistant
from characters.wenshichu_assistant_agent import WenShiChuAssistant
config_list_gpt = autogen.config_list_from_json(
    "./OAI_CONFIG_LIST.json",
    filter_dict={
        #选择你使用的模型
        "model": ["gpt-4-1106-preview"],
    },
)

llm_config = {"config_list": config_list_gpt, "cache_seed": 42}

#角色：皇上
emperor = autogen.UserProxyAgent(
    name='Emperor',
    is_termination_msg= lambda x: x.get('content',None).rstrip().endswith("TERMINATE") ,
    human_input_mode="ALWAYS",
    system_message="你现在在《甄嬛传》角色扮演中，你扮演的角色是皇上，你对后宫都很宠爱，需要及时回复后宫",
    max_consecutive_auto_reply=10000,
    code_execution_config= {
        'use_docker':False,
        "work_dir" : 'zhenhuanzhuan'
    }
)
#角色：甄嬛
huanhuan = HuanHuanAssistant(
    name='Zhenhuan',
    llm_config=llm_config
)
#角色：华妃
huafei = HuaFeiAssistant(
    name='Huafei',
    llm_config=llm_config
)
#角色：太监
taijian = TaiJianAssistant(
    name='Taijian',
    llm_config=llm_config
)
#角色：温实初
wenshichu = WenShiChuAssistant(
    name='wenshichu',
    llm_config=llm_config
)
groupchat = autogen.GroupChat(agents=[emperor, huanhuan, huafei,taijian,wenshichu], messages=[],max_round=int(1e9))
huanggong = HuangGongChatMangaer(name='huanggong',groupchat=groupchat, llm_config=llm_config)


start_msg = """帮朕传甄嬛该斩！"""
emperor.initiate_chat(
    huanggong,message=start_msg
)