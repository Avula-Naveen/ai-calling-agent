ok and also tell me steps how to add.

# AI Calling Agent

Production outbound voice platform for **campaign-based lead qualification**. Built for the [10000 Coders](https://10000coders.in) sales team — automated dialing, bilingual voice conversations, and structured outcomes in one operator console.

**Live:** https://ai-agent.10000coders.in

---

## What it does

- **Campaign dialer** — Upload contacts (CSV / Excel), start/pause/resume, and dial the queue with concurrent calls and safe lease locking
- **AI voice agent** — Real-time phone conversations over SIP (Telugu + English mix, configurable per campaign)
- **Prompt Studio** — Edit system instructions and knowledge base without redeploying code
- **Post-call intelligence** — Transcripts, summaries, and LLM-classified outcomes (`interested`, `not_interested`, `callback`, etc.)
- **Operator dashboard** — Live queue stats, call logs, analytics, and role-based access for sales agents and admins

---

## How it works

```mermaid
flowchart LR
  subgraph UI["Operator UI (Next.js)"]
    Dash[Dashboard]
    Contacts[Contact lists]
    Prompt[Prompt Studio]
    Logs[Call logs & analytics]
  end

  subgraph API["Control plane (FastAPI)"]
    Auth[Auth & admin]
    Dialer[Campaign dialer]
    DB[(Supabase / Postgres)]
  end

  subgraph Voice["Voice worker (LiveKit Agent)"]
    SIP[SIP outbound call]
    LLM[ realtime voice]
    Analysis[Post-call analysis]
  end

  Dash --> API
  Contacts --> API
  Prompt --> API
  API --> DB
  Dialer -->|dispatch job| Voice
  SIP --> Gemini
  STT-LLM-TTS --> Analysis
  Analysis -->|webhook: outcome + transcript| API
  API --> Logs

1. Operator configures the campaign and uploads contacts.
2.API acquires a dialer lease and dispatches a LiveKit worker per contact.
3.Worker places the PSTN call, runs the AI session, then PATCHes structured results to the API.
4.UI polls for queue progress, outcomes, and transcripts.

:: This is my actual behaviour of a calling agent 
