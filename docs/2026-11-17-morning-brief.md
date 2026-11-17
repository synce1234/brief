# Morning Brief — 2026-11-17

_Window: about Nov 10–17, 2026. Very few items were dated in the last 24 hours, so this brief covers the past week. Most items come from secondary coverage, so check primary sources before acting on them._

---

## 🎙️ Speech Recognition

### Salesforce SOV-Transcribe-1: open-weight ASR, ~2.3% WER (Nov 12)
A 26.6B-parameter MoE (4.6B active) speech-augmented LM for non-streaming ASR, released under Apache 2.0 on Hugging Face (`salesforce-sovereign-intelligence/SOV-Transcribe-1`). You can steer output formatting with natural-language prompts, and it supports context biasing for domain terms. It reportedly scores about 2.28% WER on the Artificial Analysis non-streaming board, ahead of Voxtral Small and NVIDIA Nemotron 3.5 Transcribe (both 2.8%). A companion DFlash draft model gives a 2–3x decode speedup via speculative decoding, and vLLM serving is supported.
- [AlphaSignal](https://alphasignal.ai/news/salesforce-s-sov-transcribe-1-beats-every-open-weight-speech-model-at-2-3-error) · [OrcaRouter guide](https://www.orcarouter.ai/blog/sov-transcribe-1-salesforce-open-weights-speech-model)

### Open-weight ASR leaderboard keeps shifting
The open-weight ASR leaderboard has changed quickly over the past few months: Cohere Transcribe, NVIDIA Nemotron 3.5 ASR (600M, 40 languages, streaming), Mistral Voxtral, and now SOV-Transcribe. The trend is toward LLM-based, promptable ASR that supports biasing.
- [NVIDIA Nemotron promptable transcription](https://thenewstack.io/nvidia-nemotron-promptable-transcription/?p=22841900)

### Research (arXiv eess.AS, mid-Nov)
- The recent listings include an aligner-encoder ASR method and **Earlybird**, a 29M-parameter streaming ASR model. Both look relevant to on-device and Android work. [arXiv eess.AS recent](https://arxiv.org/list/eess.AS/recent)

### Toolkits (Whisper / ESPnet / NeMo / SpeechBrain)
- I found no new releases this week.

### Competitive landscape (Google / Apple / commercial)
- I found no new announcements from Google or Apple in the last 24 hours. For context: Google's on-device **AI Edge Eloquent** dictation app (iOS, Gemma-based ASR) launched in April, with an Android version still pending. Apple announced system-wide dictation at WWDC 2026.

---

## 🤖 AI Applications & Trending Models

### Alibaba Qwen4-Max-Preview (Nov 11, wider coverage Nov 16)
Alibaba's new flagship is aimed at coding and agent workflows, with a reported 1M-token context. Access is a limited preview through Token Plan, Qwen App and QwenStudio from Nov 11 to 25. There are no weights, model card or published benchmarks yet. Alibaba says smaller Qwen4 models are coming (Qwen4-Flash, Qwen4-Plus and Qwen4-27B were named at Apsara).
- [Bloomberg](https://bloomberg.com/news/articles/2026-11-16/alibaba-unveils-new-flagship-ai-model-in-riposte-to-us-rivals) · [AI-TLDR](https://ai-tldr.dev/releases/qwen-qwen4-max-preview/)

### Hugging Face trending (Nov 17)
- **Qwen/Qwen3.8-27B**: the leading model of the week (multimodal, ~6.7M downloads), with many GGUF and uncensored derivatives.
- **Edge0/Edge0-145B (NVFP4)**: a 145B open MoE for coding and reasoning, sized to run locally.
- **Lightricks/LTX-2.5**: text- and image-to-video.
- **MiniMaxAI/MiniMax-H3-Image**: text-to-image.
- **Zyphra/ZONOS3-Mini**: a compact TTS model (speech-adjacent).
- **thinkingmachines/Inkling-2-Small**: a small vision-language model.
- **speridlabs/idol**: image-to-3D via Gaussian splatting.
- [Trending digest](https://github.com/datnguyenquy94/news-radar/issues/1116) · [HF trending](https://huggingface.co/models?sort=trending)

### Google: Gemini 4 Hydrogen (~Nov 12–13)
Google released a faster Gemini 4 variant. Sources give different dates.
- [Digital Trends](https://digitaltrends.com/cool-tech/googles-next-gen-gemini-4-hydrogen-ai-model-is-here-touting-faster-intelligence-for-all)

### ByteDance Seed: Seedream 5.5 (Nov 9)
An image generation and editing model that supports up to 100 consecutive edit rounds and native RGBA (transparent) output. It is rolling out across CapCut, Doubao, BytePlus and Volcano Ark, and API pricing is under half of Seedream 5.0 Pro.
- [FourWeekMBA](https://fourweekmba.com/ai-bytedance-releases-seedream-5-5-with-up-to-100-edit-rounds/)

---

## 📱 Android App Development

- **Jetpack Compose**: 1.12.1 stable, with **1.13.0-rc01** available. Material3 is 1.4.0 stable, with 1.5.0-rc01. [Latest updates](https://developer.android.com/latest-updates)
- **Android Studio**: a new stable release (Nov 5) and an RC (Nov 11) are listed. Check the version numbers on the updates page.
- **Android Developers Blog** has moved from Blogger to [developer.android.com/blog](https://developer.android.com/blog) (announced Oct 15). Update your RSS feed.
- I found no blog posts from the last 24 hours.

## 💰 Ads & IAP
- I found nothing notable this week.

---

## TL;DR
1. **SOV-Transcribe-1** is the new open-weight ASR SOTA (~2.3% WER, Apache 2.0). Worth benchmarking against your current stack.
2. **Qwen4-Max** preview is live until Nov 25, and smaller open Qwen4 models are expected soon.
3. Compose 1.13 RC is out, and the Android blog has a new URL.
