# Morning Brief — 2026-06-09

> Auto-generated | Focus areas: Speech Recognition · AI/HuggingFace · Claude Code & MCP · Android Dev (Ads/IAP)

---

## 1. Speech Recognition & Competitive Intelligence

### Apple WWDC 2026: Siri rebuilt on Google Gemini (announced June 8)
The headline story of the last 24 hours. Apple has completely overhauled Siri, now powered by a custom ~1.2T-parameter Google Gemini model licensed for ~$1 billion/year. Key architecture:
- **On-device** — Apple's own small model handles simple requests (speed + privacy)
- **Private Cloud Compute** — mid-complexity tasks
- **Gemini cloud** — heaviest reasoning queries

New "Siri AI" promises more conversational, context-aware interactions and major improvements to voice dictation. This is a direct competitive shift vs. standalone ASR pipelines.

*Sources: [Business Standard](https://www.business-standard.com/amp/technology/tech-news/wwdc-2026-apple-unveils-siri-ai-gemini-powered-apple-intelligence-more-126060900042_1.html) · [NPR](https://www.npr.org/2026/06/08/nx-s1-5847937/apple-wwdc-2026-siri-ai-tim-cook) · [TechJournal](https://techjournal.org/wwdc-2026-siri-gemini-ios-27)*

### ByteDance: Seed Speech 2 & Seed Full-Duplex LLM
- **Seed Speech 2 TTS** — conversational speech system combining expressive TTS + strong multilingual ASR + prompt-controlled emotion and contextual reasoning. Targets voice agents and customer support.
- **Seed Full-Duplex Speech LLM** — live on Doubao App; 12% improvement in conversational fluency; attentive listening with interference suppression for natural real-time interaction.

*Sources: [AI Adoption Agency](https://aiadoptionagency.com/bytedance-seed-speech-2-tts-ai-voice-agents-guide/)*

### IEEE SLT 2026 Call for Papers (deadline June 17)
Theme: "Spoken Language Technology for Social Wellbeing in the Digital Privacy Era." Topics include robustness against adversarial attacks, fairness/bias in speech systems, and privacy-preserving voice technologies.

*Sources: [IEEE SLT 2026](https://attend.ieee.org/slt-2026/call-for-papers/)*

---

## 2. AI / HuggingFace Trending Models

Notable models surfaced in the last ~48 hours:

| Model | What it is |
|---|---|
| **KVarN** (June 2) | Calibration-free KV-cache quantizer using Hadamard rotation + dual-scaling variance normalization — reduces error accumulation in autoregressive LLM decoding |
| **Sapiens2** | High-res vision transformers (0.4B–5B params) pretrained on ~1B human images; +4 mAP pose estimation, 45.6% error reduction in surface normal estimation |
| **YOLO26** | Unified real-time vision model (detection + segmentation + pose); NMS-free inference, improved training strategies |
| **DeepSeek-OCR-2** | OCR-specialised VLM: SAM ViT-B vision encoder + Qwen2 hybrid attention + DeepSeek-V2 MoE language model |
| **LongCat-Video** | 13.6B DiT-based long video generation model (June 3) |

HuggingFace's "State of Open Source Spring 2026" report notes the platform has crossed **2 million hosted models**.

*Sources: [HuggingFace Papers](https://huggingface.co/papers) · [HuggingFace Models](https://huggingface.co/models) · [HuggingFace Blog](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)*

---

## 3. Claude Code & MCP Servers

### Claude Code — recent changelog highlights
- **`fallbackModel` setting** — configure up to 3 fallback models tried in order when primary is overloaded/unavailable
- **Glob patterns in deny rules** — broader tool-name filtering
- **`/code-review` command** — reports correctness bugs at a configurable effort level
- **MCP tool rendering fixes** — `/mcp tools` list and detail views now handle long/multi-line names and descriptions correctly
- Improved retries, cross-session message security, and more reliable thinking controls

*Sources: [Claude Code Changelog](https://code.claude.com/docs/en/changelog) · [Releasebot – Claude Code](https://releasebot.io/updates/anthropic/claude-code)*

### MCP Ecosystem
- Official registry now lists **9,400+ servers**
- **Streamable HTTP** has replaced old HTTP+SSE transport as the standard for remote MCP servers (per Nov 2025 MCP spec)
- **OAuth 2.1** is now the auth standard for remote MCP servers
- **AWS MCP Server** became generally available; a fix was shipped June 5
- A curated list of 7 recommended MCP servers for Claude Code in 2026 is circulating on Medium

*Sources: [AWS Blog](https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/) · [Releasebot – Anthropic](https://releasebot.io/updates/anthropic) · [Medium – MCP Servers 2026](https://medium.com/ai-analytics-diaries/the-7-mcp-servers-every-developer-should-add-to-claude-code-in-2026-1ba8687f41f7)*

---

## 4. Android Development — Ads & IAP

### IAP Commission Reduction (rolling out by June 30)
Following the Epic Games antitrust settlement, Google is lowering Play Store service fees:
- **20%** on transactions from existing installs (down from 30%)
- **15%** on transactions from new app installs
- **10%** on recurring subscriptions

Rollout applies to EEA, UK, and US. Significant for IAP-heavy apps.

*Sources: [Android Developers Blog](https://android-developers.googleblog.com/2026/03/a-new-era-for-choice-and-openness.html)*

### June 2026 Android Feature Drop (released June 2)
- **Google Play Books** — new AI-powered "Book Insights" feature
- **Phone by Google** — Fake Call Detection now built natively into the app
- **Quick Share** — AirDrop expansion underway
- **Android 17** release imminent

*Sources: [9to5Google – June Drop](https://9to5google.com/2026/06/02/june-2026-android-drop/) · [Google Blog](https://blog.google/products-and-platforms/platforms/android/android-drop-june-2026/)*

### Google Buying Android App Code from Developers
Google is inviting select Play Store developers to a "confidential content offer pilot," purchasing app code to train internal AI/developer tooling. Details remain limited.

*Sources: [9to5Google](https://9to5google.com/2026/06/03/google-android-app-code-ai-models/)*

---

*Brief generated on 2026-06-09. Next brief tomorrow morning.*
