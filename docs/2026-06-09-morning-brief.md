# Morning Brief — 2026-06-09

> Generated: 2026-06-09 | Focus: Speech Recognition · AI Models · Android Dev · Ads/IAP

---

## 1. Speech Recognition

### [HOT] Apple WWDC 2026: Siri Rebuilt on Google Gemini
Yesterday (June 8) Apple opened WWDC 2026 with its most significant Siri overhaul yet. The new **Siri AI** runs on a custom 1.2-trillion-parameter Gemini model hosted in Apple's data centers (via a ~$1B/year Google deal). On-device tasks (dictation, voice, personal context) still run Apple Silicon foundation models; only complex world-knowledge queries route to the cloud via Private Cloud Compute. Ships in beta later this year with iOS 27 / macOS 27 (Golden Gate).
- [TechCrunch — WWDC 2026 full recap](https://techcrunch.com/2026/06/09/wwdc-2026-everything-announced-on-siri-ai-os-27-apple-intelligence-and-more/)
- [TechTimes — Siri rebuilt on Gemini](https://www.techtimes.com/articles/317985/20260608/apple-wwdc-2026-siri-rebuilt-gemini-homeos-previewed-cook-farewell-keynote.htm)

### Google Chirp 3 Now GA
Google Cloud Speech-to-Text V2 now has **Chirp 3: Transcription** in General Availability — their latest multilingual ASR generative model with improved accuracy, speaker diarization, and automatic language detection.
- [Google Cloud Release Notes](https://docs.cloud.google.com/speech-to-text/docs/release-notes)

### Google Eloquent: Silent Launch of Offline Dictation App for iOS
Google quietly dropped **AI Edge Eloquent** on the iOS App Store (April 2026) with no announcement. It uses on-device Gemma-based ASR with optional Gemini cloud cleanup — no subscription, no usage caps. Worth watching as a direct competitor to on-device Whisper deployments.
- [The Next Web](https://thenextweb.com/news/google-offline-dictation-app-ios)

### Notable ASR Architecture Trend
Every model hitting state-of-the-art in 2025–2026 uses **Conformer encoder + LLM decoder**:
- **Qwen3-ASR** (Jan 2026): 1.7B params, Conformer + Qwen decoder, 52 languages incl. 22 Chinese dialects
- **NVIDIA Canary-Qwen**: Cache-Aware FastConformer for real-time streaming ASR
- **Cohere Transcribe** (March 2026): Reached #1 on HuggingFace Open ASR Leaderboard
- [ASR Deep Dive 2025–2026 — Ruoqi Jin](https://ruoqijin.com/blog/asr-deep-dive-2025-2026)

### Upcoming Conferences
- **Odyssey 2026** — June 23–26, Lisbon: Speaker & language recognition, deepfake detection, health/emotion from speech
- **IEEE SLT 2026**: Submissions due June 17; focus on privacy, fairness, deepfake detection
- [Odyssey 2026](https://odyssey2026.inesc-id.pt/2025/11/21/call-for-papers/) | [SLT 2026](https://attend.ieee.org/slt-2026/call-for-papers/)

---

## 2. Trending AI Models (HuggingFace / GitHub)

### HuggingFace Trending (Speech & Audio)
- **Unified Streaming Audio Model** (NUS, June 3): End-to-end framework combining offline + real-time audio instruction following — one model for multiple audio interaction modes.
- **SimulU**: Training-free policy for long-form simultaneous speech-to-speech translation.
- **MOSS-TTS**: New TTS technical report trending this week.
- **Microsoft VibeVoice**: Generates up to 90 min of multi-speaker (up to 4 speakers) conversational audio (podcasts) from text.
- [HuggingFace Trending Papers](https://huggingface.co/papers/trending)

### HuggingFace Trending (General AI)
- **Holo3.1** (Hcompany, June 2): State-of-the-art computer-use agent checkpoint — fast local inference, minimal performance degradation vs cloud. [Blog post](https://huggingface.co/blog/Hcompany/holo31)
- **YOLO26**: NMS-free real-time unified model — detection, segmentation, pose estimation in one.
- **UniCorn**: Self-play multimodal self-improvement framework, SOTA on text-to-image.
- **LongCat-Video** (13.6B): DiT-based long video generation.
- [HuggingFace Models](https://huggingface.co/models)

### GitHub Trending
- **OpenClaw** (210k+ stars): Local-first personal AI assistant connecting models to 50+ integrations (WhatsApp, Slack, Signal, etc.) — fastest-growing repo in GitHub history.
- **mvanhorn/last30days-skill**: AI agent skill for synthesizing news/trends from Reddit, X, YouTube, HN — relevant tool to watch.
- **Langflow / Dify / Flowise**: Visual AI agent builders remain dominant (146k / 136k / 51k stars).
- [GitHub Trending](https://github.com/trending)

---

## 3. Android Development

### Google I/O 2026 Key Takeaways (from May)
- **Android CLI is stable**: Any AI agent (Claude Code, Codex, Antigravity) can now programmatically drive core Android tasks.
- **Jetpack Compose is the standard**: View toolkit enters maintenance mode — all new UI should be Compose.
- **AI Studio → Android apps**: Build native Android apps directly by prompting in AI Studio; shrinks setup from weeks to minutes.
- **React Native / iOS → Kotlin migration agent**: Android Studio agent automates code migration.
- **Play Shorts**: Full-screen short-video feed for app discovery, rolling out in the US.
- **Ask Play**: AI-powered natural-language app discovery overlay.
- [Google I/O 2026 Developer Blog](https://developers.googleblog.com/all-the-news-from-the-google-io-2026-developer-keynote/)
- [Android Show I/O Edition](https://www.android.com/new-features-on-android/io-2026/)

---

## 4. Ads & IAP Trends

### Subscriptions Outpacing Ads and IAP (Q1 2026)
Subscription revenue surged **+105% YoY** in Q1 2026, outpacing both ads and one-time IAP. Hybrid models (IAA + IAP) remain the dominant strategy — users who engage with rewarded ads are **4.5x more likely** to make an IAP.

### IAP Market
- Global IAP revenue hit ~$167B (up 10.6% YoY).
- Projected to reach **$257B** in 2026 — 48% of all mobile app earnings.
- Google Play doubled iOS App Store's IAP growth rate despite lower ARPU per user.
- AI-driven hyper-personalization of IAP pricing and timing is the key emerging lever.
- [SensorTower State of Mobile 2026](https://sensortower.com/blog/state-of-mobile-2026)
- [Mobile Marketing Reads — Q1 Subscription Surge](https://www.mobilemarketingreads.com/subscription-revenue-surges-105-yoy-in-q1-2026-outpacing-ads-and-in-app-purchases/)

---

*Sources: TechCrunch, TechTimes, Google Cloud Docs, The Next Web, HuggingFace, GitHub, Android Developers Blog, SensorTower, Mobile Marketing Reads*
