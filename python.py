import requests


# Making a GET request
r = requests.get('https://usda.gov/topics/opioids')

# check status code for response received
# success code - 200
# print(r)

# print content of request
# print(r.content)

htmlData = r.content




from openai import OpenAI
client = OpenAI(api_key="XXX-XXXX")


custom_string = "Hello, can you please parse this html and provide a description of what this webpage holds in the main content:"

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text":  f"{custom_string}\n{htmlData}"
        }
      ]
    },
  ],
  temperature=1,
  max_tokens=512,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)



assistant_message = response.choices[0].message.content
print("Assistant response:")
print(assistant_message)










