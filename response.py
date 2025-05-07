from openai import OpenAI
client = OpenAI(base_url="<your_base_url>",
                 api_key="<your_api_key>")


def token(messages, model):

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": """you are a document expert and you have to answer the question based on the document provided
                              and provide Indian Recipes based on the Request given"""
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": messages
                    },
                  
                ]
            }
        ],
        stream=True
    )

    for chunk in response:
        if chunk.choices[0].delta.content:
             yield chunk.choices[0].delta.content

