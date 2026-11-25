# Morning Brief — 2026-11-25

> Window: roughly the last 24–72h (Nov 22–25, 2026). Several items come from aggregator newsletters or auto-generated digests, not primary sources. Those are marked *(unconfirmed)*; check the dates before relying on them.

## 🎙️ Speech Recognition

There were no major ASR releases in the last 24h, and nothing new from Whisper, ESPnet, NeMo or SpeechBrain this week. These are the notable releases from the past two weeks:

- **Reson8 Rumble-2-Flash (Nov 18)**: A 0.5B open-weight ASR model (Apache 2.0) with automatic language ID across 40+ languages. It runs on Transformers and vLLM, which makes it a good candidate for small or edge deployments. [nocode.mba](https://www.nocode.mba/ai-release-tracker/2026/11)
- **AssemblyAI realtime agent STT (Nov 18)** *(unconfirmed naming)*: A new streaming model aimed at voice agents. Sources disagree on its name: "STT-3.7-Realtime-Agent" vs "Universal-3.6 Pro Realtime". [AssemblyAI roadmap](https://assemblyai.com/roadmap)
- **Salesforce SOV-Transcribe-1 (Nov 12)**: An open-weight ASR model with 26.6B parameters (Apache 2.0). It is non-streaming and formats output from prompts, and its reported WER is 2.28%. [CASRAI](https://casrai.org/news/salesforce-sov-transcribe-1-open-weight-asr-2026) · [AF.NET](https://af.net/realtime/salesforce-releases-sov-transcribe-1-with-2-28-word-error-rate/)
- **ElevenLabs Scribe v3 / v3 Live (Nov 10)**: Speech-to-text models for recorded and real-time audio, with speaker diarization and context-aware turn detection. [Voice AI News W46](https://www.voiceaispace.com/news/voice-ai-news-2026-11-15-w46)
- **Open ASR Leaderboard snapshot**: NVIDIA Nemotron 3.5 Transcribe leads open models at about 6.10% English WER. Qwen3-ASR 1.7B is close behind at 6.14%. [micdrop.dev](https://micdrop.dev/blog/top-open-source-speech-to-text-models) · [Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR)
- **NemotronLabs VoiceChat 11B** *(date unconfirmed)*: An open full-duplex speech-to-speech model.

### Competitive Landscape (Google / Apple / commercial)
- **Google AI Edge Gallery (Nov 10)**: Adds offline on-device ASR and TTS building blocks, which is directly relevant to on-device Android speech. [CASRAI](https://casrai.org/news/google-ai-edge-gallery-offline-speech-release-2026)
- **Google Speech Recognition & Synthesis app**: A new build, 20261109.02, is rolling out. [APKMirror](https://www.apkmirror.com/apk/google-inc/google-text-to-speech-engine/speech-recognition-synthesis-googletts-google-speech-apk_20261109-02_p0-1017739697-release/)
- **Gemini on Apple CarPlay (Nov 11)**: Gemini Live is rolling out on CarPlay globally. It is a voice assistant, not dictation. [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/googles-next-big-ai-push-230445065.html)
- **Apple**: There was no November speech announcement. The latest is improved systemwide dictation, which came with the late-October iPad mini launch.

## 🤖 AI Applications & Trending Models (HuggingFace / GitHub)

- **Releases around Nov 23–25** *(unconfirmed, from newsletters)*:
  - **AWS Strands Decider v2**: Five decision models, 2B–31B, built on Gemma 4 (Apache 2.0). [Rio Rundown](https://riorundown.substack.com/p/ai-news-nov-24-2026-anthropic-agent)
  - **Tencent HyMT3**: Open translation models in 1.8B, 7B and 30B-A3B sizes, covering 102 languages. They could be useful for speech-translation pipelines. [AI News Log](https://www.ainewslog.com/blog/grok-daily-2026-11-25-en/)
  - **Baidu ERNIE 5.5 Flash Preview**: 280B parameters with a 1M-token context window. Weights are on HuggingFace and ModelScope.
  - **Ant Group Ling-3.2-air**: An open-weight MoE (124B total, 5.5B active) for agent and document workflows.
  - **PrismML Ternary Bonsai 2.5 27B**: A local coding model of about 5.9GB, with ternary weights (Apache 2.0).
- **HuggingFace trending (Nov 23–24)**:
  - **Qwen3.8-27B** and **unsloth/Qwen3.8-27B-GGUF** (7.8M+ downloads) lead the list.
  - **Lightricks/LTX-2.5** is the top video model (text/image-to-video).
  - **facebook/sam3** (Segment Anything 3) is also trending.
  - Sources: [news-radar 11-24](https://github.com/datnguyenquy94/news-radar/issues/1189) · [ai-radar 11-23](https://github.com/HuggerHustle/ai-radar/issues/304) · [HF Trending Papers](https://huggingface.co/papers/trending)
- **Anthropic**: Has reportedly released agents that automate GitHub PR review, plus a system for detecting coordinated misuse. [Rio Rundown](https://riorundown.substack.com/p/ai-news-nov-24-2026-anthropic-agent)

## 📱 Android App Development

- **The Android Developers Blog has moved** to [developer.android.com/blog](https://developer.android.com/blog). The old Blogger site was retired in October. [Notice](https://android-developers.googleblog.com/2026/10/android-developers-blog-is-moving.html)
- **November 2026 Google System Updates (Nov 23)**: The monthly Play services and Play Store changelog. [9to5Google](https://9to5google.com/2026/11/23/november-2026-google-system-updates/)
- **Android Studio Rabbit 2 Patch 2 (Nov 20)**: [Android Studio blog](https://androidstudio.googleblog.com/2026/)
- **Developer verification expands in 2027 (Nov 19)**: Verification has been live since Sep 30 in Brazil, Indonesia, Singapore and Thailand, and expands globally next year. Plan your sideload and distribution accordingly.
- **Jetpack Compose November '26 release (Nov 18)**: Uses BOM `2026.11.01`. `Modifier.clickable` now plays standard interaction sounds by default, so check any custom click handling. [Blog](https://developer.android.com/blog/posts/jetpack-compose-november-2026-release)
- **Google Play adaptive app quality requirements (Nov 18)**: Take effect in **April 2027**, so start large-screen and foldable work now.
- **R8 keep rules for library authors (Nov 17)** and **Play Console channel expansion (Nov 16)**: The channel expansion lets you reach buyers across the store, web and external surfaces.

## 💰 Ads & IAP Trends

There was no AdMob or Play billing policy news in the last 24h. These are the latest data points:
- **Google Play vs iOS**: Google Play outpaced iOS in revenue growth in Q3 2026. [Sensor Tower](https://sensortower.com/blog/q3-2026-digital-market-index)
- **Store subscriptions**: Revenue grew 105% YoY, against 29% for IAP and 14% for ads (Q1 2026). [AppsFlyer](https://www.appsflyer.com/resources/reports/app-marketing-monetization-report/?lang=en-US)
- **AdMob**: Holds about 24% of Android mobile-game ad revenue, the leading share on Android. [Tenjin](https://tenjin.com/tr/?p=11489)
- **Mobile gaming**: IAP dipped 2% in H1 2026 while ad spend climbed. [PocketGamer.biz](https://www.pocketgamer.biz/mobile-gaming-iap-dipped-2-as-ad-spend-climbed-in-h1-2026/)

## ✅ Takeaways
1. **Rumble-2-Flash (0.5B)** and **Qwen3-ASR 1.7B** are worth benchmarking for on-device or low-cost ASR against Google's new offline AI Edge speech stack.
2. Bump Compose to BOM `2026.11.01` and check the new default click sounds.
3. Put the April 2027 Play adaptive-quality deadline and the 2027 developer verification rollout on the roadmap.
