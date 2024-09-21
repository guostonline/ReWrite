import streamlit as st
import openai

# Set up your OpenAI API key
openai.api_key = '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'

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use other models like "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
user_input = input("Enter your message: ")
response = chat_with_gpt(user_input)
print("ChatGPT:", response)