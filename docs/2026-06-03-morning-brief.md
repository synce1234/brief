# Morning Brief — 2026-06-03

> Focus areas: Speech Recognition · AI Models (HuggingFace / GitHub) · Android Dev / Monetization · Competitive Intelligence (Google, Apple)

---

## 1. Speech Recognition

### New Papers & Research
- **Endangered Language ASR** — A new arXiv paper ([2603.26248](https://arxiv.org/abs/2603.26248)) presents an ASR system for Ikema Miyakoan built from field recordings, achieving a **15% character error rate** — a notable low-resource milestone.
- **Non-Native English ASR** ([2503.06924](https://arxiv.org/pdf/2503.06924)) benchmarks five leading ASR systems on L2-ARCTIC speakers from six L1 backgrounds, providing practical accuracy and disfluency data.
- **Microsoft Paza** — Microsoft Research released ASR benchmarks and models targeting low-resource languages ([blog post](https://www.microsoft.com/en-us/research/blog/paza-introducing-automatic-speech-recognition-benchmarks-and-models-for-low-resource-languages/)).

### Open-Source Model Landscape (2026)
Top recommended open-source ASR/TTS models ([SiliconFlow roundup](https://www.siliconflow.com/articles/en/fastest-open-source-speech-recognition-models)):
| Model | Highlight |
|---|---|
| **CosyVoice2-0.5B** | 150 ms streaming latency |
| **fishaudio/fish-speech-1.5** | Top multilingual synthesis quality |
| **IndexTTS-2** | Emotional control & duration precision |
| **Fish Audio S2 Pro** | Trained on 10M+ hours, open-weight |

### Upcoming Events
- **Odyssey 2026** — Speaker & Language Recognition Workshop, Lisbon, June 23–26. Topics include diarization, robustness, fairness across accents, generative models.
- **IEEE SLT 2026** — Open call for submissions on ASR, spoken language understanding, LLM integration, and privacy-preserving voice.

---

## 2. AI Models — HuggingFace & GitHub Trending

### HuggingFace
- **State of Open Source, Spring 2026** ([HF blog](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)) — HuggingFace now hosts **2 million+ models**, with users and datasets nearly doubling year-over-year.
- **Holo3.1** ([blog](https://huggingface.co/blog/Hcompany/holo31)) — State-of-the-art **computer-use / browser automation** model. Released March 2026; fast enterprise adoption across automated workflows.
- **SmolDocling** — Compact 256M-param vision-language model for end-to-end document conversion.
- **MiniCPM4** — Efficient on-device LLM featuring sparse attention and optimized inference; strong benchmark performance for its size class.
- **Text-to-Video** boom ([DEV guide](https://dev.to/czmilo/2026-complete-guide-top-text-to-video-models-on-huggingface-49p2)) — Open-source T2V models now match commercial alternatives; multiple options available on HF Hub.

### GitHub Trending
- **OpenClaw** — Local personal AI assistant with 50+ integrations (WhatsApp, Slack, iMessage). Surged past **210k stars** in 2026 ([ByteByteGo](https://blog.bytebytego.com/p/top-ai-github-repositories-in-2026)).
- **nanochat** (Andrej Karpathy) — Full LLM pipeline in one readable codebase: tokenize → pretrain → finetune → eval → inference → chat UI. Gaining traction for educational use.
- **Bumblebee** (Perplexity AI) — Open-source read-only supply chain scanner for npm, PyPI, Go modules, MCP servers, and browser extensions.
- **Microsoft AutoGen 1.0 GA** — Major architectural improvements; GroupChat model positioning for thoroughness-first multi-agent workflows.
- **Ollama** remains the go-to for frictionless local LLM deployment.
- GitHub now hosts **4.3M+ AI-related repos** (178% YoY growth in LLM-focused projects per Octoverse 2025).

---

## 3. Android Development & Monetization

### June 2026 Android Feature Drop
Google rolled out the June feature drop without waiting for Android 17 ([Android Authority](https://www.androidauthority.com/june-2026-android-drop-3673129/), [Google Blog](https://blog.google/products-and-platforms/platforms/android/android-drop-june-2026/)):
- **Fake Call Detection** — Phone app warns when a call spoofs a trusted contact's number; bank partnership program for financial fraud prevention.
- **Circle to Search** — Now decomposes full outfits in photos/videos into individual shoppable items in one pass.
- **Google Photos Digital Wardrobe** — Scans past photos to categorize clothing and suggest mix-and-match looks.
- **Quick Share × iPhone** — Cross-platform file sharing now extended to Samsung Galaxy S24/S25, Z Flip/Fold devices.
- **Google Play Services v26.21** — New Credential Exchange Standard enables passkey/password import-export between third-party managers and Google Password Manager.

### Monetization Landscape (Q1 2026 Data)
([Mobile Marketing Reads](https://www.mobilemarketingreads.com/subscription-revenue-surges-105-yoy-in-q1-2026-outpacing-ads-and-in-app-purchases/), [AndroidDocs](https://androiddocs.com/android-app-monetization/)):
| Model | Q1 2026 YoY Growth |
|---|---|
| Subscriptions | **+105%** |
| IAP (store-based) | +29% |
| Advertising | +14% |

- **60%+ of top-grossing apps** now use hybrid monetization (ads + IAP + subscriptions).
- **US utility app eCPM** averaged $7.40; global average $2.10.
- Freemium 7–14 day trials convert at 4–9%; apps that handle Play Store trial-end gracefully convert **2–3× better**.
- AdMob remains the standard for low-pay-intent utility apps; Google Play Billing subscriptions lead for high-LTV scenarios.

---

## 4. Competitive Intelligence — Google & Apple

### Google
- **Gemini Intelligence** (announced Google I/O, May 2026) — Gemini is now deeply integrated into Android OS, running persistently on-device rather than as a standalone app. **650M+ monthly users** on Gemini across all surfaces ([MacRumors I/O roundup](https://www.macrumors.com/2026/05/19/google-io-2026-recap/)).
- **AI Edge Eloquent Dictation** — Launched April 2026 ([The AI Insider](https://theaiinsider.tech/2026/04/08/google-launches-ai-edge-eloquent-dictation-app-to-advance-on-device-speech-recognition/)) — on-device real-time transcription with filler-word removal and automatic text restructuring. Directly advances on-device ASR.
- **AI Mode in Google Search** — Has shifted user behavior from keyword queries to full conversational prompts; Gemini 3.5 powers the backend.
- **Android XR Glasses** — Previewed at I/O 2026; Android XR is Google's spatial-computing platform.

### Apple
- **WWDC 2026 kicks off June 8** — iOS 27 preview expected. Advanced agentic Siri features are the headline item ([9to5Mac](https://9to5mac.com/2026/05/06/apple-may-have-just-made-one-of-the-most-important-new-siri-announcements/)).
- **Gemini-Powered Siri** — Apple signed a multi-year ~$1B/year deal to license Google Gemini 3 for Siri across 2B+ active devices ([MacRumors](https://www.macrumors.com/2026/04/22/google-gemini-powered-siri-2026/)). This is a landmark shift in the competitive landscape — Apple offloading foundational AI inference to Google.

---

*Brief generated by Claude Code on 2026-06-03. Sources: arXiv, Google Blog, Android Authority, MacRumors, HuggingFace, ByteByteGo, Mobile Marketing Reads, AndroidDocs.*
