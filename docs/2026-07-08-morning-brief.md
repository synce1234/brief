# Morning Brief — July 8, 2026

## Speech Recognition
- **No major breaking news in the last 24 hours** in speech recognition specifically. Most recent activity is from the past 1–2 weeks (included below for continuity):
  - **NVIDIA NeMo**: `Nemotron-3.5-ASR-Streaming-0.6B` released — 40 languages, controllable latency (80ms–1s), 240–2,400 concurrent streams on 1×H100.
  - **ESPnet3** released — redesigned framework for scalable speech/audio research; adds fine-tuning support for models not natively built into ESPnet (e.g. Whisper), and simplifies new Hugging Face dataset integration to ~46 lines of code.
  - **Google Speech-to-Text (Chirp 3)** reached General Availability — new multilingual, generative ASR model with speaker diarization and automatic language detection, available in Speech-to-Text API V2.
  - New arXiv papers of note: *Omnilingual ASR* (open, 1600+ language coverage), *Whisfusion* (parallel ASR decoding via masked diffusion), *MURMUR* (efficient long-form ASR inference).

## AI Applications / Trending Models (Hugging Face, GitHub)
- **OpenAI GPT-5.6** (Sol, Terra, Luna) confirmed for **public rollout on July 10**, ending the government-limited preview window. Sol is tuned for biology, chemistry, and cybersecurity work.
- **OpenAI GPT-Live** — new full-duplex voice model family (GPT-Live-1 and GPT-Live-1 mini) rolling out to ChatGPT globally; can listen and speak simultaneously for more natural conversation.
- **xAI (SpaceXAI)** reportedly preparing a new model in partnership with Anysphere/Cursor, positioned to compete with Opus 4.8 and GPT-5.5 on inference speed — could land as early as this week.
- **Hugging Face trending**: `OmniFlatten` (real-time full-duplex spoken dialogue via post-training on existing text models), `PixWorld` (pixel-space diffusion for 3D reconstruction), `SmolDocling` (256M-param document-conversion VLM).
- **GitHub trending (AI)**: `openai/codex-plugin-cc` currently #1; agent frameworks, MCP servers, and visual LLM-app builders (Langflow, Dify, Flowise) continue to dominate trending lists.

## Competitive Landscape (Google / Apple Speech Solutions)
- **Apple + Google**: Siri's rebuild ("Siri AI") is running on a **custom version of Google Gemini** hosted in Apple's data centers, confirmed at WWDC 2026. Rollout is phased — Phase 1 (Spring 2026, iOS 26.4) shipped improved context awareness; Phase 2 (iOS 27, September 2026, alongside iPhone 18) brings "Full Conversational Siri."
- **Google Gemini Audio**: Gemini 2.5 Flash Native Audio upgraded for sharper function calling and smoother live-voice conversations, now live in AI Studio, Vertex AI, Gemini Live, and Search Live. Google also launched a live speech-to-speech translation beta in Google Translate that preserves speaker intonation and pacing.

## Android App Development
- **Jetpack Compose**: `androidx.compose.ui` and `androidx.compose.foundation` `1.12.0-beta02` shipped July 1 — incremental bug fixes/updates ahead of the next stable line (following the April '26 1.11 stable release with shared-element debug tools and trackpad event support).
- No other major Android-platform announcements surfaced in the last 24 hours.

---
*No item above required exclusion — nothing in your focus areas came back empty; see notes above where "last 24 hours" had limited direct news and slightly older context was included for continuity.*
