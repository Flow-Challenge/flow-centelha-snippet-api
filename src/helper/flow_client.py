from helper.env import get_key_from_env
import openai


model = get_key_from_env("FLOW_MODEL")
flow_temperature = float(get_key_from_env("FLOW_MODEL_TEMPERATURE"))

def create_flow_client():
    flow_tenant = get_key_from_env("FLOW_TENANT")
    flow_token = get_key_from_env("FLOW_TOKEN")

    headers = {
        "FlowTenant": flow_tenant,
        "FlowAgent": "lithia_2024_flow_last_year_challenge",
        "Authorization": f"Bearer {flow_token}",
    }

    client = openai.Client(
        api_key="please-ignore", default_headers=headers)

    client.base_url = "https://flow.ciandt.com/ai-orchestration-api/v1/openai"

    return client


def call_flow(client, messages) -> str:

    return client.chat.completions.create(
            messages=messages,
            model=model,
            temperature=flow_temperature
        ).choices[0].message.content


def create_user_message(content):
    return {
        "role": "user",
        "content": content,
    }


def create_assistant_message(content):
    return {
        "role": "assistant",
        "content": content,
    }
