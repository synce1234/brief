# Morning Brief — September 28, 2026

## Speech Recognition
- **Sarvam AI Saaras V4** (reported Sept 26) — STT for all 22 Indian languages plus global English accents. New keyterm prompting (up to 50 terms), WebSocket streaming with <150 ms time-to-first-token, batch jobs up to 2 h with optional diarization. ([MarkTechPost](https://www.marktechpost.com/2026/09/26/sarvam-ai-releases-saaras-v4-a-speech-to-text-model-for-all-22-indian-languages-and-global-english/))
- **Meta Omnilingual ASR** — research publication dated Sept 24: ASR for 1,600+ languages, including ~500 low-resource languages not previously transcribed by AI. ([Meta AI](https://ai.meta.com/research/publications/omnilingual-asr-open-source-multilingual-speech-recognition-for-1600-languages/))
- No items strictly in the last 24h surfaced from Interspeech/ICASSP, arXiv eess.AS, Whisper, ESPnet, NeMo or SpeechBrain in this search.

## Competitive Landscape (Google / Apple / commercial ASR)
- Google Cloud Speech-to-Text release notes are the place to check for API changes ([release notes](https://docs.cloud.google.com/speech-to-text/docs/release-notes)); no new Google or Apple ASR announcement was found in the last 24h. See the Sept 3 brief for Gemini 3.5 Transcribe and iOS 27 Siri context.

## AI Applications / Trending Models
- Hugging Face weekly trending (Sept 28): Qwen family dominates — 11 Qwen-based models in the top 30; a 27B multimodal flagship leads, and a 2-bit quantized 27B is the most downloaded. ([digest](https://github.com/kakapez/agents-radar/issues/1614))
- **Apple's first open VLM on Hugging Face** — 9B, built on Qwen3.5 architecture, trending. ([trending digest](https://github.com/kouweizhu/agents-radar/issues/240))
- Chinese open-weight families (DeepSeek, MiniMax, openbmb) remain strong; community fine-tunes/quantizations outpace official base releases in downloads.
- Claude Code: v2.1.273 adds forking remote sessions into local background threads and new gateway headers; MCP fixes (progress notifications during long tool calls, orphaned stdio servers, invalid-URL sign-in). Claude supports MCP 2.0 (stateless core) and plugin bundles (MCP servers + skills). ([Releasebot](https://releasebot.io/updates/anthropic/claude-code), [Big Hat Group](https://www.bighatgroup.com/blog/claude-weekly-2026-09-21/))

## Android App Development
- **Jetpack Compose 1.13.0-alpha03** (Sept 9): Material 2 text-field overloads taking `value`/`onValueChange` deprecated in favor of `TextFieldState`; compileSdk 37.1. Latest stable remains the Aug '26 release (1.12). ([release notes](https://developer.android.com/jetpack/androidx/releases/compose-material), [Aug release](https://android-developers.googleblog.com/2026/08/jetpack-compose-august-2026-release.html))
- **Reminder:** Android Developer Verification takes effect **Sept 30, 2026** (Brazil, Indonesia, Singapore, Thailand) — register Play apps by then (per Sept 3 brief).

## Advertising & IAP Trends
- Q2 2026: Android held 55% of mobile game ad revenue vs 45% iOS; AdMob share on iOS slipped 7%→6% while AppLovin gained. ([Tenjin](https://tenjin.com/blog/ad-mon-gaming-2026/))
- Google Play fee change: developers under $1M/yr pay a flat 10% on all transactions incl. subscriptions (from June 30, 2026 in US/UK/EEA); stricter enforcement on permissions and AI content expected. ([Apptunix](https://www.apptunix.com/blog/google-play-store-statistics/))
- Hybrid ads + IAP monetization and video/interactive formats continue gaining share. ([Liftoff](https://liftoff.ai/blog/in-app-advertising-in-2026-a-complete-guide-for-mobile-marketers/))

---
*Same-day coverage was sparse; items reflect the most recent relevant developments (mostly the last 1–5 days, some older reminders noted).*
