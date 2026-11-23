# Morning Brief — 2026-11-23 (Monday)

> Window: last 24h plus the past week (the weekend was quiet, so notable items from Nov 10–22 are included). Items backed by only one secondary source are marked ⚠️.

---

## 🎙️ Speech Recognition

**AssemblyAI STT‑3.7 Realtime‑Agent (Nov 18)**
A managed streaming speech-to-text model built for voice agents. It is a commercial competitor to watch for low-latency agent pipelines. ⚠️ Source is a vendor roundup.
- https://www.assemblyai.com/blog/top-open-source-stt-options-for-voice-applications

**Salesforce SOV‑Transcribe‑1: 26.6B open-weight ASR, Apache 2.0 (Nov 12)** ⚠️
Reported as an unusually large open-weight ASR model under a permissive license. Only one site reports it, so check the Hugging Face model card before relying on it.
- https://casrai.org/news/salesforce-sov-transcribe-1-open-weight-asr-2026

**Google AI Edge Gallery adds offline on-device ASR and TTS (Nov 10)**
- Ships Parakeet‑TDT 0.6B, PocketTTS 100M, Kokoro‑82M and Phonon 31M as `.litertlm` bundles.
- Android gets streaming partial and final transcripts from the mic or external audio, such as smart glasses.
- Google claims 8–9% WER on FLEURS.
- Directly useful as reference code for on-device Android ASR.
- https://developers.googleblog.com/on-device-speech-recognition-and-text-to-speech-in-google-ai-edge-gallery/

**Open ASR Leaderboard: NVIDIA Nemotron 3.5 Transcribe still leads open models**
- 30B mixture-of-experts model with about 4B active parameters, released Oct 28.
- 40 languages, OpenMDW‑1.1 license, offline only (no streaming).
- Average English WER on the leaderboard: 5.33% in the model card, about 6.10% in a November roundup.
- https://www.unite.ai/?p=497054
- https://micdrop.dev/blog/top-open-source-speech-to-text-models

**Speechmatics real-time speaker diarization (Nov 12); Deepgram Nova‑3 multilingual update** ⚠️ Vendor claims.
- https://www.forasoft.com/blog/article/whats-the-top-ai-speech-recognition-software-in-2024

**Papers:** No standout LLM-based ASR preprint from the last 24h showed up. Check the arXiv eess.AS listing directly.
- https://arxiv.org/list/eess.AS/new

**Competitor watch (Google/Apple):** Nothing new from Apple. Google's latest cloud ASR model is still Gemini 3.5 Transcribe (Aug 26).

---

## 🤖 AI Applications / Trending Models (Hugging Face, GitHub)

**Hugging Face trending (Nov 22 snapshot)**
- **Qwen/Qwen3.8‑27B** is still #1, with about 20.8K likes and 6.3M downloads; the GGUF builds also rank high.
- **thinkingmachines/Inkling‑2‑Mini / Small** are new base and conversational models that are climbing quickly.
- **Lightricks/LTX‑2.5** (video generation) and **facebook/sam3** (segmentation, including video) remain popular.
- **Speech and audio models trending:**
  - `Zyphra/ZONOS3-Mini`: compact TTS, about 154K downloads.
  - `n4ze3m/tiny-voca`: tiny TTS with ONNX and GGUF builds, suitable for on-device use.
  - `inworld/voice-isolator`: speech enhancement and voice isolation.
- https://github.com/datnguyenquy94/news-radar/issues/1167

**Frontier model releases last week** ⚠️ Aggregator-reported.
- OpenAI GPT‑6.2 Astra and Sol (Nov 17)
- Google Gemini 4 Neon (Nov 18)
- Alibaba Qwen4‑Max (Nov 16)
- No tracked model release on Nov 22.
- https://llm-stats.com/llm-updates
- https://pricepertoken.com/news/model-releases

**GitHub trending:** Agent tooling (memory, workspaces, safety sandboxes) keeps dominating.
- https://ossinsight.io/trending/ai
- https://www.shareuhack.com/en/posts/github-trending-weekly-2026-11-07

---

## 📱 Android Development

**Jetpack Compose November '26 release (stable): Compose 1.13**
- BOM `2026.11.01`, which requires Kotlin 2.2+ and compileSdk 37.1.
- New progressive blur modifier and per-line line height.
- Material 3 **1.5.0** is stable, and the experimental `material3-a2ui:1.0.0-alpha02` (A2UI renderer) is available.
- https://developer.android.com/blog/posts/jetpack-compose-november-2026-release

**Reminder:** The Android Developers Blog has moved off Blogger to `developer.android.com/blog`, so update RSS feeds.

---

## 💰 Ads & IAP
No notable developments found in the last 24h.

---

### TL;DR
1. On-device ASR is getting easy on Android. Google's AI Edge Gallery gives you Parakeet streaming as reference code.
2. Nemotron 3.5 Transcribe remains the open model to beat. Check the claimed Salesforce 26.6B release.
3. Upgrade to Compose BOM 2026.11.01 to get 1.13 and M3 1.5.0.
