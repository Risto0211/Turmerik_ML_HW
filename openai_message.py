import os
from openai import OpenAI


os.environ['OPENAI_API_KEY'] = "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"


def generate_response(sentiment, user_feedback):
    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
    if sentiment['compound'] >= 0.1:  # positive sentiment
        prompt = f"Write a concise personalized message to who may be interested in clinical trials. Highlight the benefits of participating in the upcoming trial. The user said: {user_feedback}."
    elif sentiment['compound'] <= -0.1:  # negative sentiment
        prompt = f"Write a concise personalized message to who may be skeptical about clinical trials. Address their concerns by emphasizing that the upcoming trial avoids the issues they mentioned. The user said: {user_feedback}."
    else:  # neutral sentiment
        prompt = f"Write a concise personalized message to who may be neutral about clinical trials. The user said: {user_feedback}. Provide information about the benefits and encourage them to participate."

    responce = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=300
    )

    return responce.choices[0].text.strip()
