import os
import openai
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def test_openai_api_key(model="gpt-4"):
    """Test an OpenAI API key by sending a simple prompt.
    :param model: The model to use for the test. Defaults to gpt-3.5-turbo.
    :return: True if the API key is valid, False otherwise.
    """
    try:
        # Set the API key

        # Create a simple prompt for the model
        response = client.chat.completions.create(model=model,
        messages=[
            {"role": "user", "content": "What is the capital of France?"}
        ],
        max_tokens=10)

        # Get the answer from the response
        answer = response.choices[0].message.content

        # Check that the answer is valid
        if "Paris" in answer.strip():
            print("✅ API key is valid.")
            print("Response:", answer.strip())
            return True
        else:
            print(f"❌ Unexpected response: {answer}")
            return False
    except openai.AuthenticationError:
        print("❌ Invalid OpenAI API key.")
        return False
    except Exception as e:
        print(f"⚠️ Error while testing the API key: {e}")
        return False

test_openai_api_key(model="gpt-3.5-turbo")