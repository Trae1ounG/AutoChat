from autogen.agentchat.agent import Agent
from autogen.agentchat.assistant_agent import AssistantAgent
from typing import Dict, Optional, Union, List, Tuple, Any
from typing import Callable, Dict, Literal, Optional, Union

class CharacterAgent(AssistantAgent):
    
    def __init__(
        self,
        name: str,
        system_message: Optional[str],
        *args,
        **kwargs,
    ):
        super().__init__(
            name,
            system_message,
            *args,
            **kwargs,
        )
        self.register_reply(Agent, CharacterAgent._generate_huanhuan_assistant_reply)
    def _generate_huanhuan_assistant_reply(
        self,
        messages: Optional[List[Dict]] = None,
        sender: Optional[Agent] = None,
        config: Optional[Any] = None,
    ) -> Tuple[bool, Union[str, Dict, None]]:
        if config is None:
            config = self
        if messages is None:
            messages = self._oai_messages[sender]
        message = messages[-1]
        if "再见" in message.get("content", ""):
            # Terminate the conversation when the code execution succeeds. Although sometimes even when the
            # code execution succeeds, the task is not solved, but it's hard to tell. If the human_input_mode
            # of RetrieveUserProxyAgent is "TERMINATE" or "ALWAYS", user can still continue the conversation.
            return True, "TERMINATE"
        else:
            return False, None

def get_character(name,system_message,description,llm_config):
    characterAgent = CharacterAgent(name=name,system_message=system_message,description=description,llm_config=llm_config)
    characterAgent.description = description
    return characterAgent