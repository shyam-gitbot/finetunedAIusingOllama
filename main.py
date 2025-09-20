import ollama

userInput = input("Ask your question:")
response = ollama.chat(model='tinyllama:latest', messages=[
  {
    'role': 'user',
    'content': userInput,
  },
])

print(response['message']['content'])
