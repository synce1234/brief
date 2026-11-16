# Morning Brief — 2026-11-16 (Monday)

> Window: roughly the past week, since little was published over the weekend. Items marked ⚠️ come from secondary sources I could not confirm against the original announcement.

## 🎙️ Speech Recognition

- **Google adds offline ASR and TTS to AI Edge Gallery (Nov 10)**. Speech recognition and text-to-speech now run fully on the device. Android uses the ML Kit GenAI Speech APIs, and iOS, Web and desktop use MediaPipe/LiteRT. The app ships with NVIDIA **Parakeet-TDT-0.6B-v3**. Secondary coverage reports 100+ languages and about 8–9% WER on FLEURS. This is the item most relevant to Android speech work. [Google Developers Blog](https://developers.googleblog.com/on-device-speech-recognition-and-text-to-speech-in-google-ai-edge-gallery/) · [HF blog repost](https://huggingface.co/blog/litert-community/on-device-speech-recognition-and-text-to-speech-in)
- ⚠️ **Salesforce "SOV-Transcribe-1" (reported Nov 12)**. Reported as a 26.6B-parameter open-weight ASR model under Apache-2.0 that takes natural-language prompts to control transcript formatting. I found this only on one news site and could not confirm it with Salesforce. [CASRAI](https://casrai.org/news/salesforce-sov-transcribe-1-open-weight-asr-2026)
- **Paper: streaming dictation ASR, beyond WER (arXiv, Nov 12)**. Proposes a taxonomy of failures in streaming ASR and argues that average WER hides severe errors. Worth reading if you evaluate streaming or dictation systems. [Summary](https://casrai.org/news/streaming-dictation-asr-failure-taxonomy-beyond-wer-2026)
- **Ranking open ASR models by deployment priority (Scientific Reports)**. Ranks open ASR models on several criteria (accuracy, speed, size) instead of WER alone. [Nature Sci. Rep.](https://www.nature.com/articles/s41598-026-78831-5)
- **NeMo, Whisper, ESPnet, SpeechBrain**: I found no new model releases this week. The current NVIDIA baselines are still Canary-1B-v2 and Parakeet-TDT-0.6B-v3.

### Competitive landscape
- **Google**: on-device speech through ML Kit GenAI and AI Edge Gallery, covered above.
- **Apple**: nothing new. SpeechAnalyzer (WWDC 2025) is still the current framework.
- ⚠️ A November vendor comparison lists recent commercial updates: Mistral Voxtral 3, NVIDIA Nemotron 3.5 Transcribe and xAI Grok Voice Transcribe 2.0. [Forasoft roundup](https://www.forasoft.com/blog/article/whats-the-top-ai-speech-recognition-software-in-2024)

## 🤖 AI Applications and Trending Models

- **Hugging Face trending (digests dated Nov 11)**:
  - **Qwen3.8-27B** still leads the hub, with about 7M+ downloads and about 19K likes.
  - **Lightricks LTX-2.5** (video generation) has about 2.8M downloads, part of a broader rise in multimodal models.
  - **DeepSeek-V4.1-Flash-1017** (image-text-to-text) is also near the top.
  - FP4 and GGUF quantized builds and uncensored fine-tunes keep climbing.
  - [Digest](https://github.com/datnguyenquy94/news-radar/issues/1055) · check [live trending](https://huggingface.co/models?sort=trending)
- **GitHub trending**: agent harnesses, MCP infrastructure and memory layers still lead. I found no reliable roundup for this week. [OSS Insight AI trending](https://ossinsight.io/trending/ai)
- **Sebastian Raschka (Ahead of AI)**: I found no new issue in the index. [Archive](https://magazine.sebastianraschka.com/)

## 📱 Android Development

- **The Android Developers Blog has moved** to developer.android.com/blog, and the Blogger site is retired. Update your RSS feeds. [Notice](https://android-developers.googleblog.com/2026/10/android-developers-blog-is-moving.html)
- Recent posts:
  - Jetpack Compose updates from Android Developer Summit (Nov 4)
  - Production tools for Android XR (Nov 6)
  - Open-source Sign in with Google plugin for Unity (Nov 10)
  - SmileID CameraX case study across more than 18K device types (Nov 11)
  - [developer.android.com/blog](https://developer.android.com/blog)
- **Gemini 4 Argon for Android developers**: available in Android Studio and AI Studio. Introductory Gemini API pricing ends **Nov 30**. [Post](https://android-developers.googleblog.com/2026/10/bringing-gemini-4-argon-to-android-agentic-engineering-antigravity-cli.html)
- **Android Weekly #753** came out Nov 15. [androidweekly.net](https://androidweekly.net/)

## 💰 Ads and IAP Trends

- I found no new reports this week. The latest data is still mid-year:
  - Sensor Tower: mobile IAP was about $40B in H1 2026, down 2% YoY. Gaming is weakening while ad spend grows. [PocketGamer.biz](https://www.pocketgamer.biz/mobile-gaming-iap-dipped-2-as-ad-spend-climbed-in-h1-2026/)
  - Non-gaming subscriptions are the main growth driver. [AppsFlyer report](https://www.appsflyer.com/resources/reports/app-marketing-monetization-report/?lang=en-US)

---
*Generated automatically. Items marked ⚠️ need checking against primary sources.*
