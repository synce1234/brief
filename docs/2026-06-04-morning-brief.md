# Morning Brief — June 4, 2026

---

## Speech Recognition

### New Paper: Mega-ASR
- **[Mega-ASR: Towards In-the-wild² Speech Recognition via Scaling up Real-world Acoustic Simulation](https://arxiv.org/abs/2605.19833)** (May 2026, trending on HuggingFace)
  - Achieves **>30% relative WER reduction** in complex acoustic scenarios vs. strong baselines
  - Focuses on robustness via scaling real-world acoustic simulation — directly relevant to production ASR pipelines

### IEEE SLT 2026 — Paper Deadline Approaching
- Submissions due **June 17, 2026** covering ASR, spoken language understanding, multimodal processing, LLM-speech integration, and privacy-preserving voice tech
- [Call for Papers](https://attend.ieee.org/slt-2026/call-for-papers/)

### Microsoft Research: Paza Low-Resource ASR
- Released **PazaBench** and **Paza** models for low-resource languages — end-to-end continuous pipeline for under-represented languages
- [Blog post](https://www.microsoft.com/en-us/research/blog/paza-introducing-automatic-speech-recognition-benchmarks-and-models-for-low-resource-languages/)

---

## Competitive Landscape — Google & Apple ASR

### Google Chirp 3: General Availability
- **Chirp 3: Transcription** reached GA — Google's latest multilingual ASR generative model, claiming state-of-the-art accuracy
- [Google Cloud Speech-to-Text release notes](https://docs.cloud.google.com/speech-to-text/docs/release-notes)

### Google AI Edge Eloquent (On-Device ASR)
- Launched quietly in April 2026 on iOS — runs **Gemma-based ASR fully on-device**, no audio leaves the phone
- Significant signal: Google is competing in the on-device privacy-focused ASR space
- [TechCrunch coverage](https://techcrunch.com/2026/04/07/google-quietly-releases-an-offline-first-ai-dictation-app-on-ios/)

### Apple WWDC 2026 (began June 8) — Agentic Siri Preview
- Apple confirming **Gemini 3-powered Siri** (multi-year deal, ~$1B/year to Google) debuting later this year
- iOS 27 preview with advanced agentic features expected — context-aware speech understanding a key pillar
- [AppleInsider](https://appleinsider.com/articles/26/04/22/google-confirms-context-aware-siri-built-from-gemini-will-debut-in-2026) | [MacRumors](https://www.macrumors.com/2026/04/22/google-gemini-powered-siri-2026/)

### Open ASR Leaderboard — Current Top Models
- **NVIDIA Canary-Qwen 2.5B** leads with 5.63% avg WER (Speech-Augmented LM architecture)
- **Qwen3-ASR**, **Parakeet**, **Moonshine** are close competitors — all using Conformer encoder + LLM decoder
- Industry consensus: "no catch-all model" confirmed across 60+ models on 11 datasets
- [Gladia roundup](https://www.gladia.io/blog/best-open-source-speech-to-text-models)

---

## Trending AI Models — HuggingFace & GitHub

### Trending Papers This Week
| Paper | What it is |
|---|---|
| **Mega-ASR** | Robust real-world ASR via acoustic simulation |
| **SANA-Video** | Small diffusion model for high-res video generation |
| **Echo Infinity** | Real-time infinite video generation |
| **ARIS** | Open-source research harness using cross-model adversarial collaboration |

### Trending Models / Projects
- **Wan2.2-T2V-A14B-GGUF** — quantized 14B video generation model; reflects push to make large video models accessible locally
- **ComfyUI** passed 106k GitHub stars — node-based workflow for image/video pipelines
- **Ollama** crossed 165k stars — local LLM serving dominant
- **Kimi K2.6** — strongest open-weight model for coding, tool use, and long-horizon agent workflows right now
- Leading open-weight LLMs: **Qwen3** (Apache 2.0), **Gemma 4** (Apache 2.0), **Phi-4** and **DeepSeek R1** (MIT)
- [HuggingFace Trending Papers](https://huggingface.co/papers/trending) | [State of Open Source Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)

### Claude Code Updates (June 2026)
- **Parallel tool fix**: a failed Bash command no longer cancels other calls in the same batch
- **MCP timeout fix**: sub-1000ms per-server timeout values were being floored to 1s watchdog, now ignored gracefully
- **LSP workspaceSymbol fix**: now accepts query param and passes it to language server (was returning empty)
- **/mcp UI**: collapses unused claude.ai connectors behind a "Show unused connectors" row
- **Opus 4.8**: defaults to `/effort xhigh` for hard tasks; dynamic workflows can orchestrate tens-to-hundreds of background agents
- [Claude Code Changelog](https://code.claude.com/docs/en/changelog) | [GitHub Releases](https://github.com/anthropics/claude-code/releases)

---

## Android Development

### June 2026 Android Feature Drop (Live Now)
- **Fake Call Detection** built into Phone by Google app natively
- **Credential Exchange standard** (Play Services v26.21) — import/export passwords + passkeys across third-party managers; relevant for app auth flows
- **Play Store**: merged pre-registration + auto-install into single flow; pricing discount display clarified
- **Circle to Search**: can now decompose outfit photos into individual shoppable items
- **Monthly security patch**: 124 vulnerabilities addressed, including high-severity privilege escalation (CVE-2025-48595) in Android Framework
- [9to5Google](https://9to5google.com/2026/06/01/june-2026-google-system-updates/) | [Google Blog](https://blog.google/products-and-platforms/platforms/android/android-drop-june-2026/) | [Android Authority](https://www.androidauthority.com/june-2026-android-drop-3673129/)

---

## Advertising & IAP Trends

### Q1 2026 Numbers
- Global IAP revenue: **$43.5B in Q1 2026** (+9% YoY) — 13th consecutive quarter of growth
- **Subscription revenue up 105% YoY** in Q1 — outpacing both IAP (+29%) and ads (+14%)
- Non-gaming app revenue: **+18% YoY**, surpassing $23B; now exceeds mobile gaming (~$20–21B)
- US market weakest in recent memory: only +3.5% YoY IAP growth; Western Europe offsetting

### In-App Advertising
- In-app ads: **0.56% avg CTR** vs. 0.23% mobile web — 150% higher conversion rate
- Effective hybrid: subscriptions + IAP + ads with AI-driven dynamic paywalls performing best
- [Sensor Tower State of Mobile 2026](https://sensortower.com/blog/state-of-mobile-2026) | [Mobile Marketing Reads](https://www.mobilemarketingreads.com/global-iap-revenue-hits-43-5b-in-q1-2026-marking-13-straight-quarters-of-growth/)

---

*Generated by Claude Code on 2026-06-04.*
