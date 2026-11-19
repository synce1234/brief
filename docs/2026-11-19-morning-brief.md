# Morning Brief — 2026-11-19

> Window: roughly the last 24–48 hours (Nov 17–19, 2026). Several items come from secondary or aggregator sources and are marked as such. arxiv.org could not be reached from this session, so no preprint scan is included.

---

## 🎙️ Speech Recognition

**OpenAI ChatGPT "Live Dictation" rolls out (Nov 18)**
ChatGPT now shows text as you speak and drops the old 10-minute recording cap. It is rolling out on all plans across web, desktop, iOS and Android. This is a direct competitor to Google and Apple system dictation.
Sources: [tbreak](https://tbreak.com/chatgpt-live-dictation/), [UC Today](https://uctoday.com/in-brief/chatgpt-dictation-now-types-as-you-talk-no-10-minute-cap-uTAHu0TWwT-mcrADMDc5AtA), [TokenPost](https://www.tokenpost.com/news/technology/61456)

**Salesforce SOV-Transcribe-1, an open-weight ASR model (Nov 12, recent)**
A 26.6B-parameter model under Apache 2.0, with weights on Hugging Face. You control the transcription format with natural-language prompts. Only one source covers it so far, so check the model card.
Source: [CASRAI](https://casrai.org/news/salesforce-sov-transcribe-1-open-weight-asr-2026)

**Meta Omnilingual ASR (around Nov 10, recent)**
An open model family covering more than 1,600 languages, from 300M models for on-device use up to 7B. It comes with a paper, a GitHub repo and an HF demo.
Sources: [Meta AI](https://ai.meta.com/research/publications/omnilingual-asr-open-source-multilingual-speech-recognition-for-1600-languages/), [VentureBeat](https://venturebeat.com/ai/meta-returns-to-open-source-ai-with-omnilingual-asr-models-that-can)

**Context: NVIDIA Nemotron 3.5 Transcribe (Oct 28)**
A third-party guide reports it as the #1 open model on the Open ASR Leaderboard, at about 6.10% English WER.
Source: [micdrop.dev](https://micdrop.dev/blog/top-open-source-speech-to-text-models)

**Competitive landscape (Google / Apple)**
Neither Google nor Apple made a speech or dictation announcement in the last 24h. Their latest items are Gemini system-wide dictation on macOS (July) and Siri AI dictation in the macOS 27 beta (WWDC).
Source: [HotHardware](https://hothardware.com/news/google-now-lets-mac-users-talk-to-gemini-in-virtually-any-app)

---

## 🤖 AI Applications & Trending Models

**Google Gemini 4 Neon (Nov 18, reported)**
A new member of the Gemini 4 family with stronger multimodal reasoning. It is available in AI Studio, the Gemini API and Vertex AI. So far it is reported only by secondary sites.
Source: [emergent.sh](https://emergent.sh/news/google-launches-gemini-4-neon-next-gen-ai)

**Other LLM releases this week (aggregator)**
- OpenAI GPT-6.2 Astra and GPT-6.2 Sol (Nov 17)
- Alibaba Qwen4 Max and Tencent Hy4 Flash (Nov 16)

Source: [LLM Gateway timeline](https://llmgateway.io/timeline)

**Hugging Face trending (Nov 18 digest)**
- **Qwen/Qwen3.8-27B** leads (about 20.5K likes, 6.9M downloads), with many GGUF and finetune variants.
- **Lightricks/LTX-2.5:** video generation (image-to-video, text-to-video, video-to-video).
- **MiniMaxAI/MiniMax-H3-Image** and **flux-3-image-klein:** image generation and editing.
- **facebook/sam3:** segmentation. **speridlabs/idol:** image-to-3D with Gaussian splatting.
- **Speech/audio:** **Zyphra/ZONOS3-Mini**, a compact TTS model, and **n4ze3m/tiny-voca**, a tiny on-device TTS model in ONNX and GGUF.

Source: [HF trending digest 2026-11-18](https://github.com/datnguyenquy94/news-radar/issues/1126)

**GitHub speech repos with momentum**
**hexgrad/kokoro** gained about 1.3K stars Nov 13–15, and **coqui-ai/TTS** gained about 244 stars that week. **OpenBMB/VoxCPM** and **supertone-inc/supertonic** (on-device TTS) are also trending.
Source: [Trendshift](https://trendshift.io/repositories/235035)

---

## 📱 Android App Development

Nothing new in the last 24h.
- The Android Developers Blog is moving off Blogger (notice dated Oct 15).
- The latest Compose release is still **August '26 (Compose 1.12)**, which brought mesh gradients, HDR, Grid named areas and compileSdk 37 (needs AGP 9.1.1+). A quarterly release could be due soon.

Sources: [Android Developers Blog](https://developer.android.com/blog), [Compose Aug '26 release](https://android-developers.googleblog.com/2026/08/jetpack-compose-august-2026-release.html)

---

## 💰 Ads & IAP

No notable AdMob or Google Play monetization policy changes in the last 24h.

---

## ⚡ TL;DR
1. **ChatGPT Live Dictation** shipped Nov 18. It is a consumer dictation competitor to Google and Apple.
2. **Open ASR is moving fast:** Salesforce SOV-Transcribe-1 (26.6B, Apache 2.0) and Meta Omnilingual ASR (1,600+ languages) are both worth benchmarking.
3. **Gemini 4 Neon** and **GPT-6.2** shipped this week. **Qwen3.8-27B** leads HF trending.
4. Android, Ads and IAP: quiet.
