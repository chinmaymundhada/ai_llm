import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def post_to_slack(answers):
    client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))
    channel = os.getenv("SLACK_CHANNEL")

    message = "\n".join([f"Q: {q}\nA: {a}" for q, a in answers.items()])

    try:
        response = client.chat_postMessage(channel=channel, text=message)
        assert response["ok"]
    except SlackApiError as e:
        print(f"Error posting to Slack: {e.response['error']}")
