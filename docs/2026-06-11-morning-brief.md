# Morning Brief — 2026-06-11

## Claude Code & Anthropic AI

- **Opus 4.8 is now the default model** in Claude Code. Fast mode is faster and cheaper than before.
- **Nested sub-agents** are now supported up to 5 levels deep, enabling more complex agentic workflows.
- **Plugin marketplace** got a search bar in `/plugin` to make discovery easier.
- **AWS Bedrock region auto-detection** now reads from `~/.aws` config files when `AWS_REGION` is unset.
- **Rate limits doubled** for Claude Code and Claude Opus API — effective immediately.
- **Security hardening**: permission rule loopholes closed, administrator settings for version range enforcement added, background agent stability improved.
- **Chrome integration**: browser tools now load in a single batched call instead of one per tool.

Sources: [Claude Code Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) · [What's New](https://code.claude.com/docs/en/whats-new) · [Releasebot](https://releasebot.io/updates/anthropic/claude-code)

---

## MCP (Model Context Protocol)

- **Spec Release Candidate published** — ships final on 2026-07-28. Key additions: stateless protocol core, Extensions framework, Tasks, MCP Apps, authorization hardening, formal deprecation policy.
- **500+ public MCP servers** now exist in the community registry.
- **Upcoming (H2 2026)**: stateless server operation, automatic discovery via MCP Server Cards, agent-to-agent (A2A) coordination.
- Official SDKs: TypeScript, Python, C#, Java, Swift.

Sources: [MCP Roadmap](https://modelcontextprotocol.io/development/roadmap) · [MCP Servers GitHub](https://github.com/modelcontextprotocol/servers)

---

## Speech Recognition / ASR

- **Meta Omnilingual ASR** (released 2026-06-05): open-source multilingual ASR covering 1,600+ languages including 500+ never served by any prior system. Models range from 300M (on-device) to 7B (max accuracy).
- **Google Chirp 3: Transcription** reached General Availability — state-of-the-art multilingual ASR with speaker diarization and automatic language detection.
- **Apple WWDC 2026 (June 8)**: Siri rebuilt from scratch with a Google Gemini-backed engine, shipping in iOS 27 / macOS 27 Golden Gate / iPadOS 27.
- **Apple SpeechAnalyzer** (iOS 26): replaces `SFSpeechRecognizer` with a fully on-device, concurrency-native Swift API.
- **Industry trend**: on-device-first is the 2026 default; cloud used only for accuracy escalation or advanced features.

Sources: [Meta Omnilingual ASR](https://ai.meta.com/research/publications/omnilingual-asr-open-source-multilingual-speech-recognition-for-1600-languages/) · [Google Speech-to-Text Release Notes](https://docs.cloud.google.com/speech-to-text/docs/release-notes) · [Siri WWDC 2026](https://techstory.in/siri-ai-wwdc-2026-apple-intelligence/) · [iOS Speech Recognition Guide](https://www.forasoft.com/blog/article/speech-recognition-with-neural-networks-on-ios-1621)

---

## Android Development

- **June 2026 Android Feature Drop** is rolling out:
  - Fake call detection in the Phone app (scam number spoofing alerts).
  - Personal Safety app extended to children under 13 (medical info, emergency contacts, crash detection).
  - Circle to Search now finds full clothing outfits on-screen.
  - Google Photos adds virtual wardrobe try-on (US, India, Brazil).
  - **AirDrop compatibility** in Quick Share coming to broader Android ecosystem.
- **Android CLI v1.0 stable**: programmatic version lookup, Journeys support, direct integration with Android Studio for agent workflows.
- **Developer productivity updates** announced on the Android Developers Blog (June 2026).

Sources: [9to5Google June Drop](https://9to5google.com/2026/06/08/june-2026-google-system-updates/) · [Android Authority](https://www.androidauthority.com/june-2026-android-drop-3673129/) · [Android Developers Blog](https://android-developers.googleblog.com/2026/06/android-developer-productivity-updates.html)

---

## App Monetization (IAP / Advertising)

- **Non-gaming IAP surpassed gaming IAP revenue for the first time** — non-game IAP up 21% YoY.
- Global IAP revenue: **$167B** (+10.6% YoY); IAP market projected at **$257B** for 2026.
- In-app advertising remains largest stream (~$390B, ~⅔ of total mobile revenue). iOS CPM ($5.00) is 2.5× Android CPM ($2.00).
- **60%+ of top-grossing apps** now use hybrid monetization (subscriptions + IAP + ads).
- Subscriptions fastest-growing: subscription apps earn 4.6× higher ARPU vs ad-only apps.

Sources: [Sensor Tower State of Mobile 2026](https://sensortower.com/blog/state-of-mobile-2026) · [AppsFlyer Monetization Report](https://www.appsflyer.com/resources/reports/app-marketing-monetization-report/) · [IAP Earning Trends 2026](https://www.crosswayconsulting.com/in-app-purchase-earning-trends-in-2026-app-monetization-guide/)

---

## HuggingFace Trending Models

| Model | Type | Highlight |
|---|---|---|
| **Sapiens2** | Vision transformer | 0.4B–5B params; +24.3 mIoU body segmentation, 45.6% error reduction in normal estimation |
| **LLaDA2** | Discrete diffusion LM | Block-wise iterative text generation; unmasking by confidence |
| **DeepSeek-OCR-2** | OCR VLM | SAM ViT-B + Qwen2 encoder → DeepSeek-V2 MoE LM |
| **Gemma 4 12B Unified** | Multimodal LM | Encoder-free; raw inputs → LM embedding space via linear projection |
| **NucleusMoE-Image** | Sparse MoE | 2B active / 17B total params; image generation |
| **MiniMax (agentic)** | Agent LLM | Optimized for complex multi-step workflows |

Sources: [HuggingFace Papers](https://huggingface.co/papers) · [HuggingFace Models](https://huggingface.co/models) · [State of Open Source HF Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)

---

## GitHub Trending (AI)

- **OpenClaw** (210K+ stars): local AI assistant gateway connecting LLMs to 50+ integrations (WhatsApp, Slack, iMessage, etc.) — fastest-growing OSS project of 2026.
- **Microsoft AutoGen 1.0 GA**: multi-agent conversational architecture; agents write, review, and test code autonomously in sandboxed environments.
- **Ollama**: still dominant for local LLM management (Llama 3, Mistral, Gemma, DeepSeek).
- **n8n**: workflow automation with native AI capabilities gaining traction.
- GitHub now hosts **4.3M+ AI-related repositories** (+178% YoY in LLM-focused projects).

Sources: [GitHub Trending](https://github.com/trending) · [ByteByteGo Top AI Repos](https://blog.bytebytego.com/p/top-ai-github-repositories-in-2026) · [OSSInsight AI Trending](https://ossinsight.io/trending/ai)

---

*Generated 2026-06-11 | Sources: web searches across Anthropic, Meta, Google, Apple, HuggingFace, GitHub, Sensor Tower*
