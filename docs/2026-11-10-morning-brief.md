# Morning Brief — 2026-11-10

> Covers about 24–72h, from web search only. Some items come from a single secondary source (auto-generated digests, vendor blogs) and are marked as unverified. huggingface.co, 9to5mac.com and hotwired.news could not be opened from the session network, so model cards were not checked directly.

---

## 🎙️ Speech Recognition

### NVIDIA Nemotron-3.5-Transcribe-30B-A4B is trending on HF *(unverified)*
NVIDIA has a new mixture-of-experts transcription model: 30B parameters in total, about 4B active. A daily Hugging Face trending digest (Nov 10) calls it the strongest speech release of the week (~3.1K likes, ~72K downloads). It follows June's Nemotron 3.5 ASR Streaming 0.6B, which covers 40 locales. It's worth benchmarking against Whisper and Qwen3-ASR when the model card can be opened.
- [HF trending digest 2026-11-10](https://github.com/boom7sss/agents-radar-personal/issues/108) · [nemotron-speech-streaming-en-0.6b](https://huggingface.co/nvidia/nemotron-speech-streaming-en-0.6b)

### Competitive and commercial STT moves (late Oct – early Nov)
- **Soniox STT v6** (~Nov 2): adds agent-text context and echo cancellation for voice agents. Soniox says accuracy improved across 60+ languages.
- **Willow.ai Atlas-1**: a new STT model. The vendor says it beats ElevenLabs, Deepgram and OpenAI (no independent benchmark).
- **Deepgram**: Nova-3 multilingual (55 languages) was announced Oct 23. Deepgram is reportedly acquiring Daily, the company behind Pipecat.
- **Pricing**: a Nov 8 comparison puts xAI Grok Voice Transcribe 2.0 and Microsoft MAI-Transcribe-2 at about $0.10/hour, the lowest list prices it found.
- **Google / Apple**: no new STT launch confirmed this week. Chirp 3, with diarization, is still Google's current model.
- [AI product launches Nov 2026](https://blog.mean.ceo/ai-product-launches-news-november-2026/) · [STT API comparison 2026](https://tech-insider.org/speech-to-text-api-comparison-2026/) · [Voice AI News W44](https://www.voiceaispace.com/news/voice-ai-news-2026-11-01-w44) · [Azure Speech LLM 09-2026](https://devblogs.microsoft.com/foundry/announcing-azure-ai-speech-llm-09-2026/)

### Papers
No new arXiv eess.AS / cs.CL ASR paper from the last 24h came up in search. Recent LLM-ASR work to keep in mind:
- **dLLM-ASR**: decodes with a diffusion LLM and reports about a 4.4× speedup with accuracy similar to autoregressive decoding. [arXiv 2601.17902](https://www.arxiv.org/pdf/2601.17902)
- **Index-ASR**: a large LLM-based ASR system focused on noise robustness, hotword customization and fewer hallucinations. [arXiv 2601.00890](https://web3.arxiv.org/pdf/2601.00890)

---

## 🤖 AI Applications & Trending Models

### Anthropic releases Claude Fable 5.2 and Mythos 5.2 (Nov 9)
Anthropic says the models are up to 30% faster than the 5.1 versions and cheaper, at $8 / $40 per million input/output tokens. It still recommends Opus 5.5 for most users.
- [Tom's Guide](https://tomsguide.com/ai/anthropic-just-launched-its-most-powerful-claude-ahead-of-its-ipo-heres-why-its-telling-users-to-stick-with-opus) · [9to5Mac](https://9to5mac.com/2026/11/09/anthropic-upgrades-claude-with-new-fable-5-2-model-details-here)

### Hugging Face trending (Nov 10 digest, unverified)
- **Qwen/Qwen3.8-27B**: multimodal chat model, #1 in likes (~19.5K) and downloads (~7.4M). Unsloth GGUF variants also rank high.
- **Lightricks/LTX-2.5**: video generation (image, text or video to video), ~2.8M downloads.
- **facebook/sam3**: Segment Anything v3 with video mask propagation.
- **moonshotai/Kimi-K3.1-Pro**: new Pro multimodal chat model.
- **LiquidAI/LFM3-1.7B**: small multimodal language model aimed at on-device use, a good fit for Android.
- **black-forest-labs FLUX 3 Klein (ComfyUI)**: image editing.
- [HF trending 2026-11-09](https://github.com/datnguyenquy94/news-radar/issues/1033) · [HF Trending Papers](https://huggingface.co/papers/trending)

### Other model news
- **Natura-1** (Nature Will, Nov 9): reportedly a 50B model for dexterous robot-hand control. Only one source reports it.
- **GPT-6 Cyber** (OpenAI, Nov 5) is the latest entry on AI Release Tracker.
- [AI Weekly](https://aiweekly.co/ai-news-today) · [AI Release Tracker](https://aireleasetracker.com/latest)

### GitHub
No reliable trending snapshot for the last 24h. Recent trend: agent tooling is moving toward execution infrastructure (desktop agents, web-scraping engines for agents). Live view: [OSS Insight AI trending](https://ossinsight.io/trending/ai).

---

## 📱 Android App Development

- **Android Developers Blog has moved** from Blogger to [developer.android.com/blog](https://developer.android.com/blog). Update RSS/bookmarks. ([announcement](https://android-developers.googleblog.com/2026/10/android-developers-blog-is-moving.html))
- **November 2026 Google System Updates** (Nov 9): [9to5Google](https://9to5google.com/2026/11/09/november-2026-google-system-updates/)
- **Android Studio Rabbit 3 Canary** and **AGP 9.5.0** shipped (Nov 5). [Latest updates](https://developer.android.com/latest-updates)
- **Post-Android Developer Summit posts:**
  - Intelligent apps: Gemini Nano, AICore, ML Kit, Android MCP, A2UI (Nov 5). Relevant to on-device speech.
  - Compose for every screen: phones, foldables, wearables, cars, XR, Googlebook (Nov 4).
  - Android XR production tooling and the XREAL AURA launch (Nov 6).
- [Android Weekly](https://androidweekly.net/)

---

## 💰 Ads & IAP

No notable new AdMob or Play Billing announcement in the last 24h. Background still in effect:
- The new Play billing rules (US/UK/EEA, from June 30) allow external billing and web checkout. Subscription fees are 10%. The Apps Experience and Games Level Up programs have run since Sep 30.
- Sensor Tower H1 2026: global IAP revenue was down 2% YoY (~$40B) while ad spend grew. AppLovin and AdMob together hold about 65% of mobile game ad revenue.
- [Adapty: Play billing changes](https://adapty.io/blog/google-play-billing-changes-subscriptions-fees/) · [Sensor Tower ad monetization 2026](https://gameindustrylibrary.com/documents/sensor-tower-mobile-game-ad-monetization-in-2026-sponsored-by-pwn-games)

---

## ✅ Top 3 to act on
1. Look at the **Nemotron-3.5-Transcribe-30B-A4B** model card and benchmark it against your ASR stack.
2. Read the Android **intelligent apps (Gemini Nano / AICore / Android MCP)** post for on-device speech options.
3. Update the Android Developers Blog feed to its new address.
