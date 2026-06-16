# 2026-06-16 Morning Brief

> **Generated:** 2026-06-16 | Focus: Speech Recognition · AI Models · Android · Ads/IAP

---

## 🎙️ Speech Recognition

### New arxiv Papers (Past ~72 hours)

- **[Recursive-Transformer for ASR](https://arxiv.org/abs/2606.09357)** — Systematic study of Recursive-Transformer applied to ASR encoders. Key result: comparable accuracy to standard Transformers while reducing parameter count by **66%**. Recursion in latent space with limited loops is the sweet spot.

- **[Parameter-Efficient Continual Learning for ASR](https://arxiv.org/abs/2606.09342)** — PECL method based on PEFT for ASR continual learning. Enables adapting ASR models to new domains without catastrophic forgetting.

- **[Personalized Federated Learning for Dysarthric ASR](https://arxiv.org/abs/2606.13253v1)** — Two aggregation strategies for personalization in federated setups; statistically significant WER reductions on dysarthric datasets.

- **[Bias in Phoneme-Based ASR](https://arxiv.org/abs/2606.11639v1)** — Performance disparities across languages and demographic groups in IPA transcription models, informing development of more inclusive phoneme-based systems.

- **[Code-Switching ASR to Unseen Language Pairs](https://arxiv.org/abs/2606.05846)** — Investigates generalizing code-switching capabilities to unseen language pairs via model merging and domain generalization.

- **LaSR: Context-Aware Speech Recognition via Latent Reasoning** (cs.CL) — New approach to context-aware ASR using latent reasoning mechanisms.

### Commercial / Competitive

- **Apple WWDC 2026 (June 8) — Siri AI powered by Google Gemini** — Apple rebuilt Siri from the ground up with a custom Google Gemini integration, announced at WWDC on June 8. Key capabilities: deep system-wide context awareness, on-screen understanding, conversational back-and-forth, user-adjustable voice expressiveness and speech rate. Apple also shipped a new generation Apple Foundation Models with speech + text + image multimodal understanding.
  - Sources: [CNBC](https://www.cnbc.com/2026/06/08/apple-wwdc-2026-live-updates.html) · [Tom's Guide](https://www.tomsguide.com/news/live/wwdc-2026-live-news-updates) · [Engadget](https://www.engadget.com/2189698/everything-announced-at-apples-wwdc-2026-keynote/)

---

## 🤖 AI Models & Trending (HuggingFace / GitHub)

### Notable Releases

- **Kimi K2.7-Code** (Moonshot AI, June 12) — 1 trillion-parameter MoE coding model released on HuggingFace under Modified MIT license. 32B active params, 256K context. **30% fewer reasoning tokens** vs K2.6, with +21.8% on Kimi Code Bench v2, +31.5% on MLS Bench Lite. API at $0.95/M tokens. Strong for coding and long-horizon agentic workflows.
  - Source: [CryptoBriefing](https://cryptobriefing.com/kimi-k2-7-code-open-source-release/) · [explainx.ai](https://www.explainx.ai/blog/kimi-k2-7-code-open-source-coding-model-2026)

### HuggingFace Trending (June 2026)

- Chinese frontier convergence shipped **6 competitive releases in ~2 weeks**: Qwen 3.7, DeepSeek V4.1, Hunyuan Large 3, ERNIE 5.1, Doubao Pro, GLM-6.
- **DeepSeek V4.1 Flash** is the top trending model on HuggingFace; Chinese open-weight models now hold 5 of the top 10 slots.
- **Gemma 4** holds #3 thanks to Apache 2.0 commercial clarity.
- Embedding models (NV-Embed, BGE-M3, Sentence-Transformers) dominate long-tail downloads.
- Trending TTS: A **2B continuous autoregressive TTS model** trained on multilingual corpus achieves SOTA on multiple benchmarks with low-latency via specialized distillation.
- Source: [Presenc AI June Report](https://presenc.ai/research/huggingface-trending-models-june-2026) · [HuggingFace Spring 2026 State of OS](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)

---

## 📱 Android App Development

### Jetpack Compose

- **compose-material3 1.5.0-alpha21** (June 3) — Added shapes to TimePicker component API, `compressionLimit` to `animateWidth`, bottom sheet improvements.
- **Wear Compose 1.7.0-alpha04** (June 3) — Added `RevealState.drag()`, `SwipeToRevealDragScope`, exposed custom `flingBehavior` in `SwipeToReveal`.
- Stable is Compose **1.10.6** (March 25, 2026); April '26 release (1.11) added Grid layout API, shared element debug tools, trackpad events.
- Source: [Android Developers Release Notes](https://developer.android.com/jetpack/androidx/versions/all-channel)

---

## 💰 Ads / IAP Trends

- **Subscription revenue surged 105% YoY in Q1 2026**, outpacing IAP (+29%) and ads (+14%).
- IAP market projected at **$257B in 2026** (48.2% of all mobile app earnings).
- Non-gaming apps surpassed games in total spending for the first time in 2025.
- Rewarded ads drive IAP: users who see rewarded ads are **4.5× more likely to make an IAP**.
- Platform gap: iOS CPM ~$5.00 vs Android ~$2.00 (2.5× difference).
- Source: [Mobile Marketing Reads](https://www.mobilemarketingreads.com/subscription-revenue-surges-105-yoy-in-q1-2026-outpacing-ads-and-in-app-purchases/) · [AppsFinboard](https://appsfinboard.com/blog/mobile-app-monetization-strategies-2026/)

---

*Brief auto-generated by Claude Code on 2026-06-16.*
