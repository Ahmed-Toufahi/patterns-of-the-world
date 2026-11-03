import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

sys.stdout.reconfigure(encoding="utf-8")

load_dotenv(Path(__file__).with_name(".env"))

client = OpenAI(
    base_url=os.environ["BASETEN_BASE_URL"],
    api_key=os.environ["BASETEN_API_KEY"],
)

response = client.chat.completions.create(
    model=os.environ["BASETEN_MODEL"],
    messages=[{"role": "user", "content": "Hello!"}],
)
print(response.choices[0].message.content)
