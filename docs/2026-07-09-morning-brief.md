# Morning Brief — July 9, 2026

## Speech Recognition
- **No major breaking news in the last 24 hours** in speech recognition specifically. Most recent activity is from the past 1–2 weeks (included below for continuity):
  - **NVIDIA NeMo**: `Nemotron-3.5-ASR` / `Nemotron-3.5-ASR-Streaming-0.6B` continues to be the most-discussed recent release — 40 languages, controllable latency (80ms–1120ms chunks), now also appearing in Azure AI Foundry alongside VibeVoice-ASR and MiniMax M2.5.
  - **Qwen3 ASR** (Alibaba) — Whisper-style audio encoder + Qwen3 language-model decoder, automatic language detection, multilingual transcription — still trending on Hugging Face.
  - **ESPnet**: recent fix for Whisper tokenizer compatibility with Transformers v5 (switched to `extra_special_tokens`); the ESPnet3 paper (redesigned infra for scalable speech/audio research in the foundation-model era) continues to circulate.
  - Interspeech/ICASSP-track arXiv papers trickling in on multi-speaker ASR, room-acoustics robustness (`Whisper-RIR-Mega`), and multilingual dialect ID — nothing dated in the last 24h specifically.

## AI Applications / Trending Models (Claude Code, MCP, Hugging Face)
- **Claude Code v2.1.205 shipped July 8, v2.1.204 followed July 9.** v2.1.205: added an auto-mode rule blocking tampering with session transcript files, fixed `--json-schema` silently falling back to unstructured output on invalid schemas, fixed background agents getting stuck showing "failed"/"completed" after being resumed via SendMessage, fixed a Windows worktree-removal bug that could delete files outside the worktree through NTFS junctions/symlinks, added a confirmation prompt before `rm -rf` on unresolved variables in auto mode, streamed auto-update binary downloads to disk (~400MB lower peak memory), and expanded `/doctor` into a full setup-verification tool. July 9's v2.1.204 fixed hook events not streaming during `SessionStart` hooks in headless sessions — a bug that could idle-reap remote workers mid-hook.
  - Also this week: VS Code 1.128 shipped a further boost to Claude integration.
- **MCP 2026-07-28 release candidate published.** The largest MCP spec revision since launch: a stateless protocol core, an Extensions framework, a Tasks extension for long-running work, MCP Apps (server-rendered UI), OAuth/OIDC-aligned authorization hardening, and a formal deprecation policy. Final spec lands July 28; a 10-week validation window is open for SDK/client maintainers (Tier 1 SDKs expected to ship support within it). Practical effect: remote MCP servers that needed sticky sessions + shared session store can move to plain round-robin load balancing.
- No new SOTA open-weight model drop specifically in the last 24 hours — the leaderboard is still led by Qwen 3 235B-A22B (reasoning/coding), DeepSeek R1 (math reasoning), and Llama 4 Scout (10M-token context).

## Competitive Landscape (Google / Apple Speech Solutions)
- No new developments in the last 24 hours beyond what's previously been reported: Siri's rebuild ("Siri AI") continues to run on a custom version of Google Gemini hosted in Apple's data centers (confirmed at WWDC 2026), with "Full Conversational Siri" still slated for iOS 27 this fall. Google's live speech-to-speech translation (Gemini-powered, 70+ languages, preserves intonation/pacing) continues rolling out to Android in the US, Mexico, and India, with iOS and more regions still pending.

## Android App Development
- **Android Bench overhauled — Claude Fable 5 tops the leaderboard (July 8).** Google adopted the "Harbor" framework as the new benchmarking-agent backbone and added eight models to the leaderboard: Claude Fable 5, Claude Sonnet 5, Claude Opus 4.8, GLM 5.2, Kimi K2.7 Code, MiniMax M3, Qwen 3.7 Plus, and Qwen 3.7 Max. Claude Fable 5 leads overall (84.5), ahead of GPT 5.5 (80.2) and Claude Sonnet 5 (76.2, 3rd); among open-weight models GLM 5.2 (72.2) leads Kimi K2.7 Code (70.4). Tasks probe Jetpack Compose migrations, wearable networking, and platform API updates.
- Other early-July items for context: Google Play launched its first Indie Games Fund in Africa ($1M, 10 studios, July 6); the Android Developer ID Status API went globally available with early access opening for the Android Developer Console API. No newer Jetpack Compose release since the `1.12.0-beta02` build on July 1 (Credential Manager autofill integration, Dialogs from Android Services).

---
*No item above required exclusion — nothing in your focus areas came back empty; see notes above where "last 24 hours" had limited direct news and slightly older context was included for continuity.*
