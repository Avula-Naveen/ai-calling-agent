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
    LLM[AI realtime voice]
    Analysis[Post-call analysis]
  end

  Dash --> API
  Contacts --> API
  Prompt --> API
  API --> DB
  Dialer -->|dispatch job| Voice
  SIP --> Gemini
  AI --> Analysis
  Analysis -->|webhook: outcome + transcript| API
  API --> Logs
