# Morning Brief — 2026-11-12

Window: roughly Nov 9–12, 2026. Some items come from aggregators; where I couldn't confirm a date or claim, it's marked *(unverified)*.

---

## 🎙️ Speech Recognition

### Google adds on-device ASR + TTS to AI Edge Gallery (Nov 10)
Google released on-device speech recognition and text-to-speech in its open-source AI Edge Gallery app. The **ML Kit GenAI Speech Recognition API** streams partial and final transcripts. Google says it covers 100+ languages at about 8–9% WER on FLEURS and runs about 10× faster than real time. The **ML Kit TTS** API uses a small diffusion model on the NPU and starts speaking in about 100 ms. It outputs 24 kHz audio with 8 voices and 21 locales. MediaPipe ASR/TTS tasks also run open-weight models; secondary sources name Parakeet-TDT 0.6B, Kokoro-82M and PocketTTS *(unverified)*.
**Why it matters:** This is a strong free option for Android ASR that runs offline, and it gives you a baseline to benchmark your own streaming models against.
- [Google Developers Blog](https://developers.googleblog.com/on-device-speech-recognition-and-text-to-speech-in-google-ai-edge-gallery/) · [AlphaSignal](https://alphasignal.ai/news/google-brings-on-device-voice-to-ai-edge-gallery-with-100ms-startup)

### Competitive: Gemini voice comes to Apple CarPlay (Nov 11)
Gemini Live now works hands-free in CarPlay, in every language Gemini Live supports, and chats sync to the Gemini app on iPhone. Earlier this year Apple opened CarPlay to third-party AI assistants (ChatGPT, Claude, Grok, Perplexity). I found no Apple speech recognition announcement of its own this week.
- [Bloomberg](https://www.bloomberg.com/news/articles/2026-11-11/google-adds-gemini-voice-ai-assistant-to-apple-carplay) · [PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2026/google-brings-gemini-live-to-apple-carplay/)

### Other commercial STT (context)
A Nov 2026 roundup lists Mistral Voxtral 3, NVIDIA Nemotron 3.5 Transcribe and xAI Grok Voice Transcribe 2.0 ($0.10/hr) *(release dates unverified)*. AssemblyAI's current streaming model is Universal-3.6 Pro Realtime, released Sep 29.
- [Forasoft roundup](https://www.forasoft.com/blog/article/whats-the-top-ai-speech-recognition-software-in-2024) · [AssemblyAI](https://www.assemblyai.com/blog/top-open-source-stt-options-for-voice-applications)

**Papers:** I found no notable new streaming-ASR SOTA papers on arXiv in the last 24h. Check the eess.AS/cs.SD listings directly.

---

## 🤖 AI Applications & Trending Models

### Hugging Face trending (Nov 11 digests)
- **Qwen3.8-27B** is the top trending model, with about 7.2M downloads.
- **Qwen3.8-Flash-Next** quants are climbing: the unsloth GGUF has about 2M downloads and there is also an FP4 variant. Alibaba says this model previews the Qwen4 architecture.
- **DeepSeek-V4.1-Flash-1017** has about 5.5K likes.
- **Qwen3.5-4B-3D-Coder**, a small model that generates Three.js code, is trending.
- [news-radar HF digest 11-11](https://github.com/datnguyenquy94/news-radar/issues/1055)

### Model launches
- **Gemini 4 Hydrogen (Nov 12):** Now in Google Search for all users. Developer pricing is $1.50 / $7.50 per 1M tokens (input / output). [PPC Land](https://ppc.land/google-search-gains-gemini-4-hydrogen-for-all-users-not-just-subscribers)
- **ByteDance Seedream 5.5 (Nov 9):** An image editing model that stays stable over up to 100 edit rounds, supports native transparent output and costs about ¥0.28 per edit through the API. It is rolling out on Doubao and Volcano Ark, with a Pro version to follow. [Let's Data Science](https://letsdatascience.com/news/bytedance-seed-launches-seedream-55-with-100-round-stable-ed-92d2e6e8)
- **Meta Muse Ember (Nov 9):** A low-cost model priced at $0.10 / $0.50 per 1M tokens (input / output). [LLM Stats](https://llm-stats.com/ai-news)
- **Anthropic (Nov 9–11):** Trackers report a Claude Mythos 5.2 release and an IPO roadshow *(aggregator reports)*. [LLM Stats](https://llm-stats.com/ai-news)
- **Qwen4:** Alibaba has announced the Max, Plus, Flash and 27B tiers, but I found no confirmed release yet. [Tech Insider](https://tech-insider.org/qwen4-four-variants-no-confirmed-open-weights-alibaba-2026/)

### GitHub trending
I found no fresh weekly roundup. Check [GitHub Trending](https://github.com/trending) directly.

---

## 📱 Android App Development

### Jetpack Compose 1.13.0-rc01 / Material3 1.5.0-rc01 (Nov 4)
- Compose now compiles against **API 37** and requires **AGP 9.2.0+**.
- `snapshotFlow` moves to `androidx.compose.runtime`, and `setContent` moves to `androidx.activity.compose`.
- **FlexBox** APIs are now stable. `Modifier.border` now consistently uses the outline size when drawing borders.
- Stable remains 1.12.1 (Material3 1.4.0).
- [Compose release notes](https://developer.android.com/jetpack/androidx/releases/compose) · [Android Developers Blog](https://developer.android.com/blog)

---

## 💰 Ads & IAP

There were no new policy changes in the last 24h. Ongoing items to keep in mind:
- Google Play is moving chargeback costs onto developers in 2026. [PocketGamer.biz](https://www.pocketgamer.biz/google-play-to-shift-chargeback-costs-to-android-developers-in-2026/)
- AdMob replaced its "Ads on Dynamic Content" policy with "Ads in Private Communications", which affects messaging-heavy apps. [Search Engine Land](https://searchengineland.com/google-admob-ad-placement-rules-444236)
- The extended deadline for target API 36 was Nov 1, 2026.

---

## ⚡ Top 3 Takeaways
1. **Google's on-device ML Kit ASR** (100+ languages, ~10× real time) is now a direct free competitor on Android. Benchmark it.
2. **Compose 1.13 RC** requires AGP 9.2 and API 37. Plan the upgrade.
3. **The Qwen3.8 family dominates HF trending.** Flash-Next previews the Qwen4 architecture.
