# Morning Brief — 2026-11-18

Window: roughly the last 24 hours (Nov 17–18, 2026). Some items come from secondary trackers and are marked **unverified**. arxiv.org and a few news sites could not be reached from the session, so paper coverage is thin.

---

## 🎙️ Speech Recognition

### Microsoft MAI launches at Ignite 2026 include transcription and voice (Nov 17)
Microsoft announced a family of MAI models at Ignite covering coding, security, images, **voice, transcription** and routing. It also showed **MAI Realtime**, its first live speech-to-speech model, starting at about $0.01 per audio minute. This adds to the MAI-Transcribe line (Transcribe-2 at $0.10/hr; Transcribe-2-Streaming, launched Oct 1, at ~2.5% WER on the Artificial Analysis streaming leaderboard). These are direct competitors to Google and Apple's commercial ASR.
- [TestingCatalog](https://www.testingcatalog.com/microsoft-launches-seven-mai-models-at-ignite-2026/) · [American Bazaar](https://americanbazaaronline.com/2026/11/18/microsoft-takes-aim-at-openai-and-anthropic-with-6-new-ai-models-at-a-fraction-of-the-cost-492589/) · [SiliconANGLE (Transcribe-2-Streaming)](https://siliconangle.com/2026/10/01/microsoft-targets-ultra-realistic-voice-agents-with-its-first-streaming-transcription-model/)

### Salesforce SOV-Transcribe-1, an open-weight ASR model (unverified)
A single write-up describes a 26.6B-parameter, Apache-2.0, prompt-controllable ASR model. No Hugging Face page or second source confirmed it.
- [CASRAI](https://casrai.org/news/salesforce-sov-transcribe-1-open-weight-asr-2026)

### Open ASR leaderboard snapshot (secondary source)
NVIDIA Nemotron 3.5 Transcribe (~6.10% English WER) and Qwen3-ASR 1.7B (~6.14%) are reported as the top open models. Mistral Voxtral 3 and xAI Grok Voice Transcribe 2.0 are listed as recent commercial entries.
- [micdrop.dev roundup](https://micdrop.dev/blog/top-open-source-speech-to-text-models) · [Forasoft Nov 2026 comparison](https://www.forasoft.com/blog/article/whats-the-top-ai-speech-recognition-software-in-2024)

### Competitors: Google
- The **November 2026 Pixel Drop** ships **Rambler**, a Gemini-powered dictation feature that removes filler words and rewrites what you meant to say. Google also announced Gemini on Apple CarPlay with voice replies. [The Mobile Indian](https://themobileindian.com/news/google-releases-november-2026-pixel-drop-with-new-features-also-announces-gemini-on-apple-carplay) · [Engadget](https://www.engadget.com/2171038/everything-announced-at-android-show-google-io-2026/)
- Google **AI Edge Gallery** added offline on-device speech recognition and synthesis (Nov 10, outside the 24h window). [CASRAI](https://casrai.org/news/google-ai-edge-gallery-offline-speech-release-2026)
- No new release found from Apple, OpenAI Whisper, ESPnet, NeMo or SpeechBrain in this window.

---

## 🤖 AI Applications & Trending Models (Hugging Face / GitHub)

- **OpenAI GPT-6.2 (Astra / Sol)** appeared on OpenRouter and in release trackers on Nov 17. [pricepertoken](https://pricepertoken.com/news/model-releases) · [llm-stats](https://llm-stats.com/llm-updates)
- **Microsoft MAI Code 2 / MAI Code 2 Flash** are coding models now live in GitHub Copilot. Microsoft claims about 98% of GPT-6.1 Sol's performance at 40% of the price. [Interesting Engineering](https://interestingengineering.com/ai-robotics/microsoft-seven-mai-models-launch)
- **Qwen3.8-27B** (Alibaba, multimodal) is reported as the top Hugging Face trending model on Nov 17, with over 6.7M downloads. This comes from an auto-generated digest and is **unverified**. [news-radar digest](https://github.com/datnguyenquy94/news-radar/issues/1116)
- **HF trending paper:** *π^4: A Foundation Model for 4D Scene Geometry and Motion* (Shanghai AI Lab). [HF Papers](https://huggingface.co/papers/trending)
- **GitHub trending:** no fresh weekly list was found. Recent months were dominated by coding agents, agent runtimes, memory layers and MCP servers.

---

## 📱 Android App Development

### Jetpack Compose November '26 release (stable, Nov 18)
BOM `2026.11.01` brings Compose 1.13 and Material 3 1.5.0, and requires Kotlin 2.2+ and compileSdk 37.1.
- **Graphics:** progressive blur (`Modifier.blur { BlurRadiusSpec }`), `PolygonShape` and `MorphPolygonShape` in foundation, and blur/scrim options for dialogs and popups.
- **Layouts:** **FlexBox and Grid are now stable** and FlexBox supersedes FlowRow/FlowColumn. `LazyLayoutCacheWindow` is stable. **ConstraintLayout-compose is deprecated.**
- **Animation:** new `CapturedAnimatedVisibility`, and `DeferredTransition` is stable.
- **Text:** value-based `BasicTextField` and `VisualTransformation` are deprecated in favor of `TextFieldState`. New `LineHeightStyle.Mode.PerLine`.
- **Material:** **Compose Material 2 is deprecated.** Experimental APIs were cut from 120 to 58.
- **Performance and tooling:** `computedStateOf`, recomposition tracing in Perfetto, a performance-audit skill in the Android CLI, and `TestFailurePolicy` for auto screenshots on test failure.
- **Behavior changes:** clickables now play system sounds by default, and `onFocusedBoundsChanged` no longer has any effect.
- **AI:** the A2UI renderer (`material3-a2ui:1.0.0-alpha02`) renders Agent-to-UI protocol output as native Compose.
- Note: the androidx release pages still list 1.13.0-rc01, so confirm the BOM mapping before upgrading.
- [Android Developers Blog](https://developer.android.com/blog/posts/jetpack-compose-november-2026-release)

---

## 💰 Ads & IAP Trends

- **Sensor Tower Q3 2026 Digital Market Index:** ChatGPT has passed TikTok as the #1 app by global IAP revenue, and ChatGPT ad activity is growing. [Sensor Tower](https://sensortower.com/blog/q3-2026-digital-market-index)
- **Context:** mobile gaming IAP was down about 2% in H1 2026 while ad spend rose. All-app IAP was up 5.3% YoY to $43.6B in Q2. Subscriptions are the fastest-growing model (AppsFlyer reports +105% YoY). [PocketGamer.biz](https://www.pocketgamer.biz/mobile-gaming-iap-dipped-2-as-ad-spend-climbed-in-h1-2026/) · [AppsFlyer](https://www.appsflyer.com/resources/reports/app-marketing-monetization-report/)

---

## ✅ Key Takeaways
1. **Microsoft is moving fast in speech.** MAI Realtime and the MAI transcription/voice models compete with Google and Apple on price.
2. **Compose Nov '26 brings real migration work.** Material 2, ConstraintLayout-compose and value-based text fields are deprecated, and FlexBox/Grid are stable.
3. **Frontier LLM releases continue** with GPT-6.2 and MAI Code 2. Verify Qwen3.8-27B on Hugging Face directly.
