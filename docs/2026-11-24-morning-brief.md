# Morning Brief — 2026-11-24

> Window: ~last 24h (Nov 23–24, 2026), widened to the past week where nothing dated to the last day turned up. Most sources are third-party trackers and digests. Check vendor pages before acting on anything here.

---

## 🎙️ Speech Recognition

**Nothing major dated to the last 24h.** These releases from the past ~2 weeks are still worth tracking:

- **AssemblyAI STT-3.7 Realtime Agent (Nov 18):** A streaming ASR model built for voice agents, aimed at low-latency turn-taking. It is a commercial competitor. [AssemblyAI](https://www.assemblyai.com/blog/top-open-source-stt-options-for-voice-applications)
- **Salesforce SOV-Transcribe-1 (Nov 12):** A reported 26.6B-parameter open-weight ASR model under Apache-2.0. It takes natural-language prompts to control transcript formatting. *I couldn't confirm this against the HF model card.* [CASRAI](https://casrai.org/news/salesforce-sov-transcribe-1-open-weight-asr-2026)
- **NVIDIA Nemotron 3.5 Transcribe (Oct 28):** An open-weight offline speech LLM covering 40 languages and audio up to 1 hour. It reportedly leads the HF Open ASR Leaderboard with 6.10% English WER. It ships through NeMo Speech 3.0, now a separate repo from the NeMo toolkit. [NeMo Speech](https://github.com/NVIDIA-NeMo/Speech) · [micdrop ranking](https://micdrop.dev/blog/top-open-source-speech-to-text-models)
- **Other commercial moves:** Roundups mention Mistral Voxtral 3, xAI Grok Voice Transcribe 2.0, and Speechmatics/Deepgram updates. These are single-source and unverified. [Fora Soft](https://www.forasoft.com/blog/article/whats-the-top-ai-speech-recognition-software-in-2024)
- **Papers:** I found no new eess.AS papers on LLM-based streaming ASR this week. The most recent relevant one is **Factorized Delayed Streams Modeling for LLM-based Streaming ASR** (arXiv:2610.04333, Oct). It separates the "when to wait" decision from text prediction. [arXiv](https://arxiv.org/pdf/2610.04333)
- **ESPnet / SpeechBrain / Whisper:** No releases found.

## 🤖 AI Applications & Trending Models

- **Z.AI GLM-5.4 (Nov 23–24):** The only notable LLM release dated to the last 24h, according to a live tracker. [BenchLM tracker](https://benchlm.ai/model-updates)
- **OpenAI GPT-6.2 Astra / Sol (Nov 17):** Early reviews of Astra are mixed to harsh. [writingmate weekly](https://writingmate.ai/blog/ai-news-week-of-2026-11-23)
- **Google Gemini 4 Neon (Nov 18):** Priced at $3 / $15 per 1M input/output tokens. [LLM Gateway timeline](https://llmgateway.io/timeline/2026) · [capitalandcompute](https://capitalandcompute.net/blog/new-ai-models-november-2026/)
- **ByteDance Seedance 2.5 Flash (video, Nov 15) and Seedream 5.5 (image, Oct 28):** Trackers listed both on Nov 23. Neither is a new launch. [LLM Gateway](https://llmgateway.io/timeline/2026)
- **Alibaba Qwen4-Max and Tencent Hy4 flash (Nov 16).** [af.net tracker](https://af.net/realtime/ai-model-releases-november-2026/)
- **HF trending (Nov 23):** **Qwen3.8-27B** is still #1 on downloads, including the `unsloth` GGUF quant. **Lightricks/LTX-2.5** leads open video generation, and **facebook/sam3** is trending for video segmentation. [ai-radar digest](https://github.com/HuggerHustle/ai-radar/issues/304) · [HF trending papers](https://huggingface.co/papers/trending)
- **GitHub trending:** Agent tooling still dominates: coding agents, runtimes, sandboxes and memory layers. `mattpocock/skills` is still near the top. [Analytics Vidhya, Oct roundup](https://www.analyticsvidhya.com/?p=258844) · [OSS Insight](https://ossinsight.io/trending/ai)

## 📱 Android Development

- **Jetpack Compose November '26 release (stable):**
  - Version **1.13** across the core modules. Upgrade with BOM **2026.11.01**, which needs Kotlin 2.2+ and compileSdk 37.1.
  - **Progressive blur** via `Modifier.blur { … }` and `BlurRadiusSpec`.
  - **Material 3 1.5.0** is now stable.
  - Migration path to the state-based `BasicTextField`. The undo/redo APIs are no longer experimental.
  - A new static-analysis "skill" for Compose performance, run through the Android CLI.

  [Android Developers](https://developer.android.com/blog/posts/jetpack-compose-november-2026-release)

## 💰 Ads & IAP Trends

- **Sensor Tower Q3 2026:** Global IAP revenue was about $45B (+4.4% YoY) while downloads were flat. ChatGPT is the #1 app by IAP revenue in the US, Japan and the UK, so AI apps now lead non-game monetization. [Sensor Tower](https://sensortower.com/blog/q3-2026-digital-market-index)
- **Mobile gaming IAP fell 2% YoY in H1 2026 while ad spend rose.** The mix keeps shifting toward hybrid ads plus IAP. [PocketGamer.biz](https://www.pocketgamer.biz/mobile-gaming-iap-dipped-2-as-ad-spend-climbed-in-h1-2026/)
- **AdMob** has the largest share of Android gaming ad spend (~22%) and +6% YoY growth. [Tenjin](https://tenjin.com/tr/blog/ad-mon-gaming-2026/)
- **Google Play fees:** One report says the IAP service fee for new installs dropped to 20% in the EEA, UK and US. *Check this against Play Console docs.* [Global Games Forum](https://www.globalgamesforum.com/ctv/apple-google-blink-on-iap-fees-adtech-quietly-rewrites-the-rules)

---

### TL;DR
1. Compose 1.13 / BOM 2026.11.01 is stable, with progressive blur and M3 1.5.
2. ASR is a quiet day. The open leaderboard is led by Nemotron 3.5 Transcribe, and AssemblyAI shipped a realtime agent model on Nov 18.
3. The LLM churn is from last week (GPT-6.2, Gemini 4 Neon, Qwen4-Max). GLM-5.4 is the only release in the last 24h.
4. AI apps (ChatGPT) now top IAP revenue charts.
