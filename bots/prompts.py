
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder,FewShotChatMessagePromptTemplate,PromptTemplate

chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Eres un asistente virtual capaz de ayudar en cualquier tarea"),
        MessagesPlaceholder(variable_name="messages"),
        ("human", "{input}"),
    ]
)