# GitHub AI Reviewer Bot (Explainable)

This is a prototype GitHub App that performs explainable AI-powered code reviews on pull requests.  
Unlike traditional bots that only give ✅/❌ feedback, this bot summarizes changes, explains why certain rules are violated, and links relevant docs so developers can learn while fixing issues.

---

## Features
- **AI-powered PR review**: Summarizes changes in natural language
- **Explainable feedback**: Explains *why* issues matter, not just what failed
- **Documentation links**: Directs contributors to resources
- **Configurable**: Easily extend rules and behavior

---

## Tech Stack
- Python 3.11+
- [FastAPI](https://fastapi.tiangolo.com/) for the bot server
- GitHub Actions / Webhooks
- OpenAI API (for explainable feedback)

---

## Setup
1. Clone this repo:
   ```bash
   git clone https://github.com/your-org/github-ai-reviewer.git
   cd github-ai-reviewer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run locally:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Configure your GitHub App:
   - Add webhook URL (e.g., `http://localhost:8000/webhook`)
   - Grant access to **Pull Requests**
   - Install the app on your repo

---

## Development
To test locally:
```bash
pytest
```

---

## Roadmap
- [ ] Add inline comment support
- [ ] Support multiple languages beyond Python
- [ ] Improve summarization with fine-tuned LLM
- [ ] Add caching for repeated reviews

---

## License
MIT
