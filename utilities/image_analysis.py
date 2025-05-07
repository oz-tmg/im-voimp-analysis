import openai


response = openai.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {"role": "user", "content": [
            {"type": "text", "text": "Describe this image"},
            {"type": "image_url", "image_url": {"url": "https://your.image.url"}}
        ]}
    ],
    max_tokens=1000
)

print(response.choices[0].message.content)
