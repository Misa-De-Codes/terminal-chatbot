## Gemini CLI Chatbot

A terminal chatbot using Google Gemini API. Stores chat history in `history.py`.

---

### ⚙️ Setup

```bash

git clone <your-repo>
cd <your-repo>
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate.bat
pip install -r requirements.txt
touch .env

```

Add your API key to `.env`:

```env
GEMINI_API_KEY=your_key_here
```

---

### 💬 Usage

```bash
python main.py
```

* Type prompts after `-->>`
* `--history` → show past chats
* `q` → quit
