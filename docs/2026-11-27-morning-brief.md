# Morning Brief — 2026-11-27 (Friday)

> Coverage: last 24h where available, plus notable items from the past ~2 weeks (there was no brief between 2026-09-03 and today). Many items come from aggregators. Check them against primary sources before citing.

## 🎙️ Speech Recognition

**Quiet in the last 24h.** I found no new ASR release dated Nov 26–27. These were the notable items from this month:

- **Salesforce SOV-Transcribe-1 (Nov 12):** an open-weight ASR model (~26.6B, Apache 2.0) on Hugging Face. You can shape the transcript format with natural-language prompts. It is non-streaming only. [CASRAI](https://casrai.org/news/salesforce-sov-transcribe-1-open-weight-asr-2026)
- **Reson8 Rumble-2-Flash (Nov 18):** a compact 0.5B ASR model under Apache 2.0. It's worth evaluating for on-device or Android use.
- **NVIDIA Nemotron 3.5 Transcribe:** ranked #1 among open English models on the Open ASR Leaderboard (~6.13% avg WER, Nov 9 snapshot), just ahead of Qwen3-ASR 1.7B. It ships in BF16/FP8/NVFP4/GGUF. A streaming multilingual 0.6B variant is also out. [Tech report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Transcribe-Technical-Report.pdf) · [ThinkScribe ranking](https://thinkscribe.ai/en/blog/open-speech-recognition-models-2026)
- **Zyphra ZONOS3-Mini (Nov 12):** an open-weight TTS model covering 43 languages. It runs locally in the browser and natively.
- **Maya Transcribe (Nov 2):** a Hindi/Hinglish ASR model fine-tuned from Qwen3-ASR 0.6B. It shows Qwen3-ASR becoming a base for fine-tunes. [Qwen3-ASR repo](https://github.com/QwenLM/Qwen3-ASR)
- **Papers (arXiv eess.AS):**
  - *Streaming ASR on a Microcontroller*: a 65.7M transducer quantized to 2/4 bits on ESP32-P4 (arXiv:2610.38739).
  - *VISH-ASR*: Viterbi-guided hotword selection for contextual biasing in speech LLMs (arXiv:2610.27867).
  - Listing: [eess.AS recent](https://arxiv.org/list/eess.AS/recent)
- **Toolkits:** I found no new Whisper, ESPnet or SpeechBrain releases this month. NeMo Speech 3.0 (v3.0.0) is still the current major version.

## 🏢 Competitive Landscape (Google / Apple / Commercial)

- **Google AI Edge Gallery adds offline ASR + TTS (Nov 10):** the models run fully on-device and pair with Gemini Nano and Gemma 4. Reference code for local voice apps is included. This is directly relevant to Android speech work. [CASRAI](https://casrai.org/news/google-ai-edge-gallery-offline-speech-release-2026) · [AlphaSignal](https://alphasignal.ai/news/google-brings-on-device-voice-to-ai-edge-gallery-with-100ms-startup)
- **Gemini voice comes to Apple CarPlay (Nov 11):** it rolls out globally in every supported Gemini Live language. Until now Siri was the only voice assistant on CarPlay. [Bloomberg](https://www.bloomberg.com/news/articles/2026-11-11/google-adds-gemini-voice-ai-assistant-to-apple-carplay)
- **Apple (iOS 27.2):** Siri AI is in beta in FR/JA/KO/PT/ES, and Apple promises more accurate systemwide dictation.
- **Commercial STT:** AssemblyAI launched a realtime voice-agent STT model (Nov 18). Recent roundups also list Mistral Voxtral 3, xAI Grok Voice Transcribe 2.0, Deepgram Nova-3 multilingual and Speechmatics Melia-1. [AssemblyAI](https://www.assemblyai.com/blog/top-open-source-stt-options-for-voice-applications)

## 🤖 AI Applications & Trending Models

**Last 24h (Nov 26):**
- **Anthropic MCP update:** MCP servers can now publish server-provided **skills** (public beta). The update also adds long-running **Tasks** and **Elicitation**. [The Neuron](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-november-26-2026/)
- **Google Gemini "Semantic governance policies":** this case study reports that AgentDojo prompt-injection attack success fell from 48.7% to 0.9%.
- **OpenAI** is reportedly preparing shared ChatGPT usage limits. [creati.ai](https://creati.ai/ai-news/2026-11-26/)

**This week:**
- **Ant Group Ling-3.2-air (Nov 25):** an open-weight multimodal model (text, image, video) under the MIT license.
- **Xiaomi MiMo-V2.6-Flash-MOPD (Nov 23):** it's unclear whether the weights can be downloaded.

**HF trending (Nov 27):** [digest](https://github.com/datnguyenquy94/news-radar/issues/1220)
- **Qwen/Qwen3.8-27B** leads with ~21.9k likes and 6M+ downloads.
- **Lightricks/LTX-2.5** is the top video generation model.
- **moonshotai/Kimi-K3.1-Pro** is also trending.

**GitHub trending:** agents are becoming "handoff-ready workflows". The leaders are Astryx, Modern Web Guidance and anthropics/skills, with Hookshot the top new repo. vercel-labs/agent-desktop is a Rust desktop agent. [Shareuhack 11-18](https://www.shareuhack.com/en/posts/github-trending-weekly-2026-11-18)

## 📱 Android App Development

- **Jetpack Compose 1.13 stable (Nov 18, BOM 2026.11.01):** [Android Developers Blog](https://developer.android.com/blog/posts/jetpack-compose-november-2026-release)
  - Adds **progressive blur**.
  - Cuts experimental APIs from 120 to 58.
  - Adds a new **A2UI renderer** for the Agent-to-UI protocol.
  - Behavior change: clickable elements now play platform interaction sounds by default.
  - Also released: Material 3 1.5.0 stable and Compose 1.14.0-alpha01.
- **Tooling:** Android CLI 1.1 (Nov 13) and Platform-Tools 37.0.3 (Nov 19). The BOM reportedly needs Kotlin 2.2+ and compileSdk 37.1. [dev.to](https://dev.to/mango7777/how-to-trace-jetpack-compose-113-recompositions-and-automate-builds-with-android-cli-11-4amn)

## 💰 Ads & IAP Trends

- **Sensor Tower Q3 2026:** global IAP revenue was **$45B (+4.4% YoY)** while downloads were flat at 37.6B. **ChatGPT** is #1 in IAP revenue in the US, JP, UK, FR and BR. [Sensor Tower](https://sensortower.com/blog/q3-2026-digital-market-index)
- **Ad channels:** in-app ads hold 54.8% of mobile ad spend. YouTube is the fastest-growing channel at over 16%.
- **Gaming vs. non-gaming:** gaming IAP fell 2% YoY in H1 2026 while ad spend rose. Non-gaming subscription revenue through the stores grew +105% YoY in Q1, and 70% of that revenue is organic. [PocketGamer.biz](https://www.pocketgamer.biz/mobile-gaming-iap-dipped-2-as-ad-spend-climbed-in-h1-2026/) · [AppsFlyer](https://appsflyer.com/resources/reports/app-marketing-monetization-report)

---

### ⭐ Top 3 to act on
1. Try Google AI Edge Gallery's on-device ASR/TTS reference code. It's a direct benchmark for Android speech features.
2. Evaluate the compact ASR models: Rumble-2-Flash (0.5B), Nemotron 3.5 streaming 0.6B and Qwen3-ASR 0.6B.
3. Review the Compose 1.13 behavior change: clickable elements now play sounds by default.
