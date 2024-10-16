import openai
from langchain.prompts import (
    ChatPromptTemplate, 
    MessagesPlaceholder, 
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate
)
from langchain.chains import ConversationChain
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.environ.get("OPENAI_API_KEY")

# creating a prompt template for the conversation. 
# The prompt template is a list of messages that will be used to generate the conversation.
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("The following is a friendly conversation between a human and an AI. \
         The AI is talkative and provides lots of specific details from its context. \
            If the AI does not know the answer to a question, it truthfully says it does not know."),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}")
])

# creating a LLM 
llm = ChatOpenAI(temperature=0, openai_api_key=os.environ.get("OPENAI_API_KEY"))
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)


def get_response(prompt, podcaster, guest):
    _prompt = f"""

    Generate a podcast between {podcaster} and {guest}. They are discussing about {prompt}.
    
    """

    response = conversation.predict(input=_prompt)
    
    return response
