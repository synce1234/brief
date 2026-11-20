# Morning Brief — 2026-11-20 (Friday)

> Window: about 18–20 Nov 2026, with a few items from the past week where they matter. Many items come from aggregators or single digests and are marked **(unverified)** where I could not confirm them against a primary source.

---

## 🎙️ Speech Recognition

### New models & releases
- **Reson8 Rumble-2-Flash (Nov 18):** A 0.5B open-weight ASR model released under Apache 2.0. It is already trending on Hugging Face. It is small enough that it is worth testing on-device. [CASRAI](https://casrai.org/news/salesforce-sov-transcribe-1-open-weight-asr-2026) · [HF trending digest](https://github.com/datnguyenquy94/news-radar/issues/1146)
- **AssemblyAI STT-3.7 / STT-3.7-Realtime-Agent (Nov 18):** A new commercial STT model for pre-recorded audio, plus a realtime variant tuned for voice agents. **(unverified, from secondary blogs)** [AssemblyAI blog](https://www.assemblyai.com/blog/top-open-source-stt-options-for-voice-applications)
- **Microsoft MAI Realtime 1 (Nov 17):** A speech-to-speech model with limited access. It is part of a batch of 7 new MAI models (coding, security, image, real-time speech) priced below frontier rivals. **(single source)** [The Neuron](https://theneuron.ai/digest/everything-that-happened-in-ai-today-friday-november-20-2026)
- **Salesforce SOV-Transcribe-1 (Nov 12):** A 26.6B open-weight ASR model under Apache 2.0, with weights on Hugging Face. [CASRAI](https://casrai.org/news/salesforce-sov-transcribe-1-open-weight-asr-2026)
- **ElevenLabs Scribe v3 and Scribe v3 Live (Nov 10):** New batch and real-time transcription models. [AI release tracker](https://www.nocode.mba/ai-release-tracker/2026/11)

### Leaderboard
- **NVIDIA Nemotron 3.5 Transcribe** is reported to lead the open models on the HF Open ASR Leaderboard, at 6.10% average WER in English and 4.69% across 7 languages. **(single blog, provisional)** [micdrop.dev](https://micdrop.dev/blog/top-open-source-speech-to-text-models)

### Papers (arXiv eess.AS)
- **Multilingual TASU (arXiv:2611.00692):** Text-only adaptation for multilingual ASR that uses simulated CTC posteriors. Accepted at NCMMSC 2026. [arXiv listing](https://arxiv.org/list/eess.AS/current)
- **arXiv:2611.00690 (Zheng & Harwath):** Speech-to-speech translation, a work in progress. [arXiv listing](https://arxiv.org/list/eess.AS/current)

### Competitive landscape (Google / Apple / commercial)
- **Google AI Edge Gallery adds on-device ASR + TTS (Nov 10):** Offline speech in 100+ languages with 8–9% WER on FLEURS. It ships through ML Kit GenAI on Android and through MediaPipe/LiteRT on iOS, Web and desktop. This is directly relevant to Android speech apps. [Google Developers Blog](https://developers.googleblog.com/on-device-speech-recognition-and-text-to-speech-in-google-ai-edge-gallery/) · [HF blog](https://huggingface.co/blog/litert-community/on-device-speech-recognition-and-text-to-speech-in)
- **Apple:** I found no new speech recognition announcement this month. The Gemini-powered Siri is still pending. [AI Business](https://aibusiness.com/speech-recognition/apple-taps-google-gemini-siri)

---

## 🤖 AI Applications & Trending Models (HF / GitHub)

### Model releases
- **Gemini 4 Neon (Google, Nov 18):** A new Gemini 4 family variant. [LLM Gateway timeline](https://llmgateway.io/timeline)
- **GPT-Live-1.1 (OpenAI):** Now available through the API. **(single digest)** [The Neuron](https://theneuron.ai/digest/everything-that-happened-in-ai-today-friday-november-20-2026)
- **Tencent Hy4 Flash (Nov 16):** Open weights you can download and run locally. [LLM Gateway timeline](https://llmgateway.io/timeline)
- **Earlier this week:** Qwen4 Max (Alibaba) and GPT-6.2 Astra (OpenAI, Nov 17). [LLM Gateway timeline](https://llmgateway.io/timeline)

### Hugging Face trending (Nov 20 digest)
- **Qwen/Qwen3.8-27B:** About 20.7K likes and 6.6M downloads. It is still the most popular base model for fine-tunes, and its Unsloth GGUF build has 7.1M downloads.
- **Lightricks/LTX-2.5** (text/image-to-video), **facebook/sam3** (segmentation), and **DeepSeek-V4.1-Flash-1017** (multimodal reasoning).
- **Speech models trending:** **higurashi-ai/Haru-4B** (full-duplex speech-to-speech, about 3.7K likes), **Zyphra/ZONOS3-Mini** (compact TTS), **n4ze3m/tiny-voca** (tiny TTS with ONNX/GGUF builds, good for mobile), **inworld/voice-isolator** (speech enhancement), and **Reson8/Rumble-2-Flash** (ASR).
- [Source digest](https://github.com/datnguyenquy94/news-radar/issues/1146)

### ByteDance
- No new Seed release in the last 24h. The latest is **Seedream 5.5** (image, Nov 9). **Heads-up:** Seed 2.0 Pro and Seed 2.0 Code Preview are retired on Volcano Engine on **Nov 24**, so migrate before then if you use them. [BytePlus](https://ai.byteplus.com/lumina/en/resource/seedream-5-5-release-date) · [Second Talent](https://www.secondtalent.com/resources/every-doubao-ai-model-explained-compared/)

---

## 📱 Android App Development

- **Jetpack Compose November '26 release (Nov 18):** Requires BOM 2026.11.01, Kotlin 2.2+ and compileSdk 37.1. Behavior change: `Modifier.clickable` now plays the standard system click sounds by default, so check your UI tests and custom feedback. [Android Developers Blog](https://developer.android.com/blog/posts/jetpack-compose-november-2026-release)
- **Android developer verification expanding in 2027 (Nov 19):** It follows the Sep 30 rollout in Brazil, Indonesia, Singapore and Thailand. [Android Developers Blog](https://developer.android.com/blog)
- **Google Play adaptive app quality requirements (Nov 18):** Take effect in April 2027, covering large screens and foldables. [Android Developers Blog](https://developer.android.com/blog)
- **R8 keep rules for library authors (Nov 17):** How to unblock app-level DEX optimization. [Android Developers Blog](https://developer.android.com/blog)
- **Also in the changelog:** Android CLI, Android XR and Android Studio Otter 2 doc updates. [Changelog](https://github.com/fornewid/android-developers-changelog/releases/tag/doc-update-20261119-1527)

## 💰 Ads & IAP
- **Play Console channel expansion (Nov 16):** New tools for reaching buyers across the store, the web and external surfaces. This is relevant to IAP and external-offer strategy. [Android Developers Blog](https://developer.android.com/blog)

---

## ✅ Action items
1. Benchmark **Rumble-2-Flash (0.5B)** and Google's **ML Kit GenAI on-device ASR** against your current speech stack on Android.
2. Before you bump the Compose BOM, check the new `Modifier.clickable` sound behavior.
3. If you use ByteDance Seed 2.0 Pro or Code Preview, migrate before **Nov 24**.
