import streamlit as st
import openai

# Set up your OpenAI API key
openai.api_key = 'your-api-key-here'

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