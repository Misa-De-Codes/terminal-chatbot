import os
from dotenv import load_dotenv
from google import genai
from colorama import Fore, Style, init

init(autoreset=True)

# Ensure history.py exists
if not os.path.exists(".history/history.py"):
    with open(".history/history.py", "w") as f:
        f.write("data = []\n")


try:
    from history import data
except:
    data = []


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client()

prompt = input(f"{Fore.GREEN}-->>  {Style.RESET_ALL}").strip().lower()

while True:
    if prompt == "q":
        break
    elif prompt == "":
        prompt = input(f"{Fore.GREEN}-->>  {Style.RESET_ALL}").strip().lower()
        continue

    elif prompt == "--history":
        for i, entry in enumerate(data):
            if entry is None:
                continue
            print(Fore.YELLOW + "-" * 50)
            print(f"{Fore.CYAN}[{i + 1}]")
            print(f"🧠 {Fore.GREEN}Prompt   : {entry['prompt']}")
            print(f"🤖 {Fore.WHITE}Response : {entry['response']}")
        prompt = input(f"{Fore.GREEN}-->>  {Style.RESET_ALL}").strip().lower()
        continue

    data.append({"prompt": prompt})
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )

    data[-1]["response"] = response.text or ""

    print(f"🤖 {Fore.MAGENTA}Susie: {Fore.WHITE}{response.text}")
    prompt = input(f"{Fore.GREEN}-->>  {Style.RESET_ALL}").strip().lower()


with open(".history/history.py", 'w') as f:
    f.write(f"data = {repr(data)}\n")
