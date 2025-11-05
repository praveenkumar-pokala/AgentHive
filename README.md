# Enhanced WhatsApp Agent

This repository is an **enhanced, from‑scratch re‑implementation** inspired by
`WhatsappAgent` – but with a clearer architecture, modern tooling, and an easy
path to plug into a real WhatsApp integration (Twilio or Meta Cloud API).

It is designed as a small yet realistic **Agentic WhatsApp backend**:

- 🧠 **Multi‑agent reasoning** (router, FAQ agent, small‑talk agent, task agent)
- ⚙️ **FastAPI** webhook for inbound WhatsApp messages
- 📦 Clean separation between:
  - API layer (`api/fastapi_app.py`)
  - Agents (`agents/`)
  - LLM client + tools (`services/`)
- 🧪 Local simulation endpoint so you can test without WhatsApp or Twilio

> Out of the box, this runs as an HTTP API that you can point a WhatsApp provider
> to. For security and production use, you must still configure your own secrets,
> verify signatures, and host it yourself.
