# Morning Brief — November 11, 2026

> **Quiet day.** Very little turned up from the last 24 hours that I could check against a primary source. Items below are labeled **[24h]** when they're from the last day. All other items are recent background from the past few weeks, included so the brief is still useful. Treat third-party dates and numbers as unconfirmed until you check the vendor's own page.

## Speech Recognition
- **No new ASR model, paper or toolkit release confirmed in the last 24h.** I found nothing new dated November 2026 from arXiv eess.AS, Interspeech/ICASSP, Whisper, ESPnet, NeMo or SpeechBrain. To check directly, see the [arXiv eess.AS new listing](https://arxiv.org/list/eess.AS/new) (November IDs start with `2611.`).
- **Recent commercial ASR releases (Sept–Oct 2026):** Microsoft MAI-Transcribe-2 (public preview Sept 3, streaming version Oct 1), AssemblyAI Universal-3.6 Pro Realtime (Sept 29), and Speechmatics Oak 1, a medical-audio model (Oct 14). A comparison page dated "November 2026" also lists Mistral Voxtral 3, NVIDIA Nemotron 3.5 Transcribe and xAI Grok Voice Transcribe 2.0, but I couldn't check those against the vendors. ([gladia.io](https://www.gladia.io/blog/a-review-of-the-best-asr-engines-and-the-models-powering-them), [forasoft.com](https://www.forasoft.com/blog/article/whats-the-top-ai-speech-recognition-software-in-2024))
- **Open-source ASR to watch:** Microsoft VibeVoice-ASR-Streaming ([github](https://github.com/microsoft/VibeVoice)), NVIDIA Nemotron 3.5 ASR Streaming 0.6B, which covers 40 languages ([HF](https://huggingface.co/nvidia/nemotron-speech-streaming-en-0.6b)), and Qwen3-ASR ([github](https://github.com/QwenLM/Qwen3-ASR)).
- **LLM-based ASR research thread (2026):** non-autoregressive and speculative decoding are the main ways papers make LLM-based ASR faster:
  - **NLE** (IBM): turns a CTC transcript into the final text by editing it with a bidirectional LLM, up to about 27× faster. ([arXiv 2603.08397](https://arxiv.org/abs/2603.08397))
  - **Self-speculative decoding**: uses the CTC encoder to draft tokens, with a reported 5.58% WER on the Open ASR Leaderboard. ([arXiv 2603.11243](https://arxiv.org/abs/2603.11243))
  - **NIM4-ASR**: a production-oriented framework with an RL training stage to reduce hallucinations. ([arXiv 2604.18105](https://arxiv.org/html/2604.18105))

## Competitive Landscape (Google / Apple / commercial ASR)
- **No new Google or Apple speech announcements in the last 24h.**
- **Google:** Gemini 3.5 Transcribe (late Aug) is replacing Chirp 3. It detects 85+ languages automatically, labels up to 3 speakers, and gives word-level timestamps. ([9to5google](https://9to5google.com/2026/08/26/gemini-3-5-transcribe/))
- **Google frontier models:** Gemini 4 Carbon was announced Oct 28, two weeks after Gemini 4 Argon. It focuses on cybersecurity and long tasks. Access is staged, with cyber defenders first and developers and consumers later. Intro API pricing is $2 / $10 per million input / output tokens. ([blog.google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/), [9to5google](https://9to5google.com/2026/10/28/gemini-4-carbon-announcement/)). One aggregator lists Carbon as released Nov 10, which may be the date wider access began. Not confirmed. ([llmgateway.io](https://llmgateway.io/timeline))
- **Apple:** I found no new speech announcements. SpeechAnalyzer (iOS 26) is still Apple's main on-device ASR API.

## AI Applications / Trending Models (Hugging Face, GitHub)
- **[24h] Hugging Face trending (Nov 11 digests):**
  - **Qwen3.8 family** leads, with Qwen/Qwen3.8-27B at about 19.6K likes and 7.2M downloads.
  - **Lightricks/LTX-2.5** leads image and video generation.
  - **moonshotai/Kimi-K3.1-Pro** is also on the list.
  - Other trending entries: **MiniMax-H3-Image** and **Ripple-65B-Preview**.

  Numbers differ between digests. ([news-radar digest](https://github.com/datnguyenquy94/news-radar/issues/1055), [HF trending](https://huggingface.co/models?sort=trending))
- **[24h] GitHub trending (Nov 10 report):** agent projects are the strongest trend. **OpenMausBot** (TS, about 19.8K stars) is an open-source alternative to proprietary agent platforms. **debpalash/VoiceStudio**, a fully local voice-cloning, dubbing and transcription suite, is the speech-relevant pick. ([gittok report](https://github.com/Chestnuts-Sisyphus/gittok/issues/1940))
- **[24h, unconfirmed] Meta "Muse Ember 1.0"** is listed by one aggregator as released Nov 10. I found no primary source, and it's unclear whether the weights are open. ([llmgateway.io](https://llmgateway.io/timeline))
- **OpenAI ChatGPT Images 2.6** (Nov 2026) can make animated GIFs. The exact date isn't known.

## Android App Development
- **No new Android or Compose releases confirmed in the last 24h.**
- **Blog move:** an Oct 15 post said the Android Developers Blog is leaving Blogger. New posts now appear at [developer.android.com/blog](https://developer.android.com/blog), so update RSS feeds.
- **Recent posts (Oct 12–13):**
  - Google Play's "More than a store" update.
  - A new frontier model for Android developers.
  - Googlebook Linux Terminal Preview.
- **Jetpack Compose:** the latest stable version is still Compose 1.12 (August '26, BOM `2026.08.00`). It needs compileSdk 37 and AGP 9.1.1+. Releases have come out about every 4 months (April, August), so a new one is plausible soon. ([Android Dev Blog](https://android-developers.googleblog.com/2026/08/jetpack-compose-august-2026-release.html))

## Advertising & IAP Trends
- **Nothing new in the last 24h.** The background numbers haven't changed:
  - H1 2026 mobile game IAP was about $40B, down 2% YoY, while game ad spend rose.
  - Non-game IAP is growing much faster, up about 21% YoY.
  - Hybrid monetization (ads + IAP) is becoming the default.
  - In-app ads take about 55% of mobile ad spend. YouTube is the fastest-growing channel at about 16%.

  ([pocketgamer.biz](https://www.pocketgamer.biz/mobile-gaming-iap-dipped-2-as-ad-spend-climbed-in-h1-2026/), [AppsFlyer](https://www.appsflyer.com/resources/reports/app-marketing-monetization-report/))
- Watch for Q3 2026 Sensor Tower / AppsFlyer reports, which usually come out in November.

---
*Summary: the only same-day items were Hugging Face and GitHub trending (Qwen3.8, LTX-2.5, agent frameworks, VoiceStudio). Speech, Android and ads had no new releases I could confirm in the last 24 hours.*
