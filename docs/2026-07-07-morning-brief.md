# Morning Brief — 2026-07-07

## Speech Recognition

- Two new papers landed on arXiv July 6, both tied to the Interspeech 2026 track: "[Spatial Speech Perception Systems: A Survey of Sound Source Localization, Directional Enhancement, and Speech Recognition](https://arxiv.org/abs/2607.02296)" and "[Cross Domain Few-Shot Class-Incremental Audio Classification via Adversarial Contrastive Learning](https://arxiv.org/abs/2607.02254)" (accepted to Interspeech 2026).
- A Hugging Face Daily Paper posted July 6 on **Audio Language Models (ALM)** frames ALMs as the emerging dominant paradigm for speech + music generation — directly touches your ASR interest, worth a skim. (huggingface.co/papers)
- No new NeMo/ESPnet/SpeechBrain toolkit release in the last 24h; most recent NeMo item remains Nemotron-3.5-ASR-Streaming-0.6B (June).
- Competitive landscape: no new Apple/Google speech announcement in the strict last-24h window, but the Gemini-powered Siri rollout continues on its confirmed timeline — Phase 1 (contextual awareness via Gemini) is already live since iOS 26.4, with "Full Conversational Siri" targeted for iOS 27 / iPhone 18 in September 2026. Tangential but notable: OpenAI shipped **gpt-realtime-2.1 / -mini** around July 6, claiming 25%+ lower p95 latency and improved recognition/noise handling for voice — a commercial ASR/voice competitor worth tracking even though it's not Google/Apple.

## AI Applications / Trending Models (HuggingFace, GitHub)

- No single dominant release in the strict last-24h window; the trending board is still led by the recent wave of Chinese open-weight models (GLM-5.2, Qwen3.5-397B-A17B, Kimi K2.5) holding multiple top slots.
- Notable July 6 HF Daily Paper: "**Embodied.cpp**" — a portable C++ runtime (PhysicalAI System Group, SAIL Lab, Southeast University) for deploying vision-language-action / world-action models to heterogeneous edge devices — alongside the Audio Language Models survey noted above.
- GitHub's AI trending space continues to be dominated by agent/MCP tooling (OpenClaw past 210K stars, Firecrawl, Langflow, Ollama); no new entrant surfaced specifically in the last 24h.

## Android / Jetpack Compose

- `androidx.compose.ui:ui-*:1.12.0-beta02` shipped in early July, following beta01 (June 17) — incremental release, no standalone blog post yet.
- Android Weekly issue #734 published July 5.
- Google's July Android Security Bulletin and the first Android 17 Pixel security update rolled out around July 6 — patch-focused, not Compose-specific.

## Advertisement & IAP Trends

- No breaking news in the last 24 hours. Background worth tracking: Q1 2026 app-store subscription revenue grew 105% YoY (fastest of all revenue streams) vs. 14% ad revenue growth and 29% store-IAP growth; Gen AI apps' annual IAP revenue hit $6.1B (+232% YoY), with ChatGPT alone at $3.4B annualized — the fastest-growing app category and a signal of where ad/IAP dollars are shifting.

## Claude Code / MCP

- **Claude Code v2.1.202 shipped July 6, 2026** — the most concrete same-day item in this brief. Highlights:
  - New "Dynamic workflow size" setting in `/config` (advisory small/medium/large agent-count guidance for dynamic workflows).
  - `workflow.run_id` / `workflow.name` OpenTelemetry attributes added to telemetry from workflow-spawned agents.
  - Fixes: Ctrl+R history-search crash on accept/cancel mid-scan; `/rename` on background sessions reverting after a job restart; mTLS handshake issues; Remote Control and background-agent bugs on macOS SSH.
  - CLI surface: added `GIT_CONFIG_GLOBAL` env var; removed `OTEL_LOG_TOOL_DETAILS` and several deprecated model aliases (claude-haiku-3-5, sonnet-3-7, opus-4, etc.).
- Ecosystem note: starting July 7–8, 2026, Claude **Fable 5** usage shifts from being included in Pro/Max/Team plan limits to metered usage credits ($10/M input, $50/M output tokens) — not Claude Code itself, but relevant if Fable 5 is part of your workflow.

---

**Summary:** The one high-confidence, same-day development is **Claude Code v2.1.202** (July 6) with its new dynamic-workflow-size config and several reliability fixes. Speech recognition saw two Interspeech-2026-track arXiv papers (spatial speech perception survey; few-shot audio classification) plus an HF Daily Paper on Audio Language Models, all dated July 6 — worth a skim, none are major releases. Android/Compose, AI-trending-models, and ad/IAP are otherwise quiet in the strict 24h window; the wider Gemini-Siri rollout timeline and Gen-AI-app IAP growth remain the relevant background trends to keep watching.

**Security note:** A live GitHub personal access token was pasted in plaintext in this task's instructions again (same pattern as prior sessions, e.g. June 19 and June 22 briefs). It was used only to clone/push this file and is not stored anywhere else by this agent, but it has now appeared in multiple session transcripts. Strongly recommend rotating/revoking this token and switching to a scoped, short-lived credential (or a GitHub App/connector) for future runs.
