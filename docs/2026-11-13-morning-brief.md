# Morning Brief — 2026-11-13 (Friday)

> Coverage: about Nov 12–13, 2026. Date labels in the search results were often inconsistent, so items outside the 24-hour window are marked as recent context.

---

## 🎙️ Speech Recognition

### New ranking of open ASR models (Nature Scientific Reports, Nov 12)
A peer-reviewed study ranks open ASR models against several criteria under different deployment priorities (accuracy, latency, cost, footprint). It is useful for choosing between Whisper, Parakeet/Nemotron, Qwen3-ASR and similar models. It evaluates models and releases none.
[nature.com](https://www.nature.com/articles/s41598-026-78831-5)

### NVIDIA Nemotron 3.5 Transcribe is trending on Hugging Face (recent context, released late Oct)
A speech-augmented LLM (SALM) with about 4.3B active parameters (30B-A4B MoE) and a frozen Nemotron 3 diarization component. You can steer its output with text instructions (verbatim or cleaned-up text) and give it context terms to improve recognition of names and jargon. Reports say it ranks #1 on the HF Open ASR leaderboard. It ships under the OpenMDW-1.1 license with a fine-tuning toolkit in NeMo, in BF16, FP8 and NVFP4 builds plus a GGUF build and a speculative-decoding draft model. In the Nov 11 HF trending digest it had about 3.1k likes and about 72k downloads.
[NVIDIA Research](https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Transcribe/) · [Tech report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Transcribe-Technical-Report.pdf) · [The New Stack](https://thenewstack.io/nvidia-nemotron-promptable-transcription/?p=22841900)

### Commercial / competitive watch (unverified)
A November 2026 vendor comparison names Mistral Voxtral 3 and xAI Grok Voice Transcribe 2.0 as new commercial STT entrants. It cites no primary sources, so treat both as unconfirmed.
[Forasoft](https://www.forasoft.com/blog/article/whats-the-top-ai-speech-recognition-software-in-2024)

### Papers
I found no notable new arXiv eess.AS / cs.CL ASR papers dated in the last 24 hours. Recent background reading: Uni-ASR, a single LLM-based model for both streaming and non-streaming recognition ([arXiv:2603.11123](https://arxiv.org/abs/2603.11123)).

---

## 🤖 AI Applications & Trending Models

### ByteDance Seed: Seedream 5.5 (Nov 9, recent context)
An image generation and editing model that ByteDance says stays stable over up to 100 rounds of editing and outputs native RGBA transparency. It is rolling out in Dreamina, CapCut, BytePlus, Doubao and Volcano Engine Ark. ByteDance says a Pro version will follow. ByteDance claims it beats GPT Image 2.5, but no third-party benchmark has confirmed that yet.
[LetsDataScience](https://letsdatascience.com/news/bytedance-seed-launches-seedream-55-with-100-round-stable-ed-92d2e6e8)

### Hugging Face trending (digest of Nov 11)
- **Qwen3.8-27B** leads in likes and downloads and is becoming the default community base model.
- **NVIDIA Nemotron-3.5-Transcribe-30B-A4B** is an ASR model (see above).
- **webAI-Official/TwIL-8B** is an 8B instruct model built on Granite.
- MiniMax-H3-Image, NousResearch/Arete-27B and Lightricks/LTX-2.5 also show up on the HF front page.

[news-radar digest](https://github.com/datnguyenquy94/news-radar/issues/1055) · [HF trending](https://huggingface.co/models?sort=trending)

### Google: "Gemini 4 Hydrogen" (rumor)
A single blog post says Google released "Gemini 4 Hydrogen" (thought to be Gemini 4 Flash) on Nov 12. I found **no official Google confirmation**. The Gemini API docs reportedly list only `gemini-4-argon` (announced Sep 30). Treat this as a rumor for now.
[kie.ai explainer](https://kie.ai/blog/what-is-gemini-4-hydrogen) · [Gemini 4 Argon (official)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)

### GitHub
I found no reliable trending list for this week. Through 2026 the trend has stayed the same: agent runtimes, MCP servers, memory layers and on-device inference. Check [github.com/trending](https://github.com/trending?since=weekly) for the live list.

---

## 📱 Android App Development

### The Android Developers Blog has moved
Official posts now appear at **developer.android.com/blog**, and the Blogger site is retired. Update your RSS feed.
[Announcement](https://android-developers.googleblog.com/2026/10/android-developers-blog-is-moving.html) · [New blog](https://developer.android.com/blog)

### Recent posts
- **Nov 11:** SmileID used CameraX across more than 18,000 device types for identity verification.
- **Nov 10:** Google released an open-source Sign in with Google plugin for Unity.
- **Nov 6 / Nov 4:** Android Developer Summit follow-ups on Android XR tooling and Jetpack Compose adaptive layouts.
- **Nov 5:** Android Studio Rabbit 3 Canary 3.
- **Gemini 4 Argon** is available in Android Studio. Its introductory pricing ends **Nov 30**.

[9to5Google: Nov Google System Updates](https://9to5google.com/2026/11/09/november-2026-google-system-updates/) · [Android Studio releases](https://androidstudio.googleblog.com/2026/)

---

## 💰 Ads & IAP

- **Play Billing Library deadline has passed.** The extended deadline for Billing Library 8 or later was **Nov 1, 2026**, and app updates now require PBL 8+. The current version is PBL 9. Flutter apps need `in_app_purchase` 3.3.0+ and Unity apps need Unity IAP 5.0.0+.
- Google Play's fee overhaul continues: the billing fee is now separate from the service fee, and alternative and external billing options are allowed alongside Play Billing. Check what comes due in Q4.
- I found no AdMob-specific announcements in the last 24 hours.

[Foresight Mobile](https://foresightmobile.com/blog/google-play-billing-library-8-migration) · [AppsOps: fee overhaul](https://appsops.store/news/google-play-billing-choice-quality-fee-tiers-2026)

---

## TL;DR
1. 🎙️ A new Nature study ranks open ASR models by deployment priority, and Nemotron 3.5 Transcribe is still the top open ASR model on HF.
2. 🤖 ByteDance released Seedream 5.5. "Gemini 4 Hydrogen" is unconfirmed.
3. 📱 The Android Dev Blog moved to developer.android.com/blog, and Gemini 4 Argon's promo pricing in Android Studio ends Nov 30.
4. 💰 The Play Billing Library 8 deadline (Nov 1) has passed, so make sure your apps are on PBL 8+.
