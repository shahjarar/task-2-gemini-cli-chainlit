import chainlit as cl
from agent import create_agent

# Start of chat
@cl.on_chat_start
async def on_chat_start():
    agent = create_agent()
    cl.user_session.set("agent", agent)
    await cl.Message(content="Hello, how can I assist you today?").send()

# Handle user messages
@cl.on_message
async def on_message(message: cl.Message):
    agent = cl.user_session.get("agent")
    
    # Directly run agent (SyncRunner removed)
    # Assuming your 'create_agent()' returns a callable agent object
    try:
        response = agent.run(message.content)  # use your agent's run method
    except AttributeError:
        # Fallback if agent.run doesn't exist
        response = {"final_output": "Agent run method not available."}

    # Debug output (optional)
    if isinstance(response, dict) and "tool_calls" in response:
        for tool_call in response["tool_calls"]:
            print(f"Tool call: {tool_call.get('tool_name')}")
            print(f"Tool input: {tool_call.get('tool_input')}")
            print(f"Tool output: {tool_call.get('tool_output')}")

    # Send response to user
    final_message = response.get("final_output") if isinstance(response, dict) else str(response)
    await cl.Message(content=final_message).send()
