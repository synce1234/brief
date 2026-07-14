# Morning Brief — July 14, 2026

## Speech Recognition
- **Quiet 24–48h window overall** — no new model releases, benchmark results, or notable commits from Whisper, ESPnet, NVIDIA NeMo, or SpeechBrain landed dated July 12–14.
- **arXiv (in-window)**:
  - *"VoxENES 2026: Benchmarking Generalization of Speech Spoofing Detectors Against LLM-Era TTS and Voice Conversion"* — arXiv:2607.11706, posted July 13. Benchmarks anti-spoofing/deepfake detectors against newer LLM-driven TTS/voice-conversion systems; relevant if your ASR pipeline needs liveness/spoofing safeguards. https://arxiv.org/abs/2607.11706
  - *"Data Augmentation for L2 English Speaking Assessment using TTS"* — arXiv:2607.10790, posted July 12. Uses TTS-generated data to augment non-native speech assessment training sets; tangential but relevant to accent-robustness pipelines. https://arxiv.org/abs/2607.10790
- No new Interspeech/ICASSP activity or Papers With Code leaderboard movement in-window.
- **Bottom line**: nothing field-moving broke in the last two days for core ASR.

## AI Applications / Trending Models (Claude Code, MCP, Hugging Face, GitHub)
- **Claude Code v2.1.207–209 shipped July 12–14**: auto mode now on by default on Bedrock/Vertex/Foundry (default model bumped to Opus 4.8 there), ~7x faster tool-pool assembly, up to 79x smaller session transcripts in edit-heavy sessions, MCP-stdio/LSP/hook memory-leak fixes, screen-reader mode, and a hotfix for `/model` being blocked in background agent sessions. The weekly usage-limit boost (50% increase for Pro/Max/Team/Enterprise) was also extended to July 19.
- **MCP**: no new spec changes or major server announcements in this specific window (the next full spec finalizes July 28).
- **GitHub Trending (July 13–14)**:
  - **OpenCut** (open-source CapCut alternative, Next.js + Rust local GPU video processing) hit **#1 on GitHub Trending July 13**, +4,349 stars in a day (~69k total).
  - **Graphify** (YC S26) — turns a codebase into a queryable knowledge graph for AI coding assistants via tree-sitter (no embeddings/vector store); +1,858 stars today (~81–86k total).
  - **awesome-llm-apps** — curated agent/RAG app collection, +1,104 stars today.
- **arXiv**: *"Extending LLM Context via Associative Recurrent Memory"* (arXiv:2607.11614, July 13) — evaluates ARMT for constant-memory long-context scaling with two new long-context benchmarks.
- **Frontier models (dates uncertain, flagged as such)**: reporting on **GPT-5.6** rollout is inconsistent (default-in-ChatGPT since July 9 per some sources, GA scheduled July 17 per others); **Gemini 3.5 Pro** is targeting a July 17 launch — both imminent but not yet confirmed released as of today.
- No Hugging Face blog post or Google/ByteDance announcement confirmed dated exactly July 12–14.

## Advertisement and IAP Trending
- No dedicated news story in the strict 24–48h window.
- Context: hybrid ad+IAP monetization remains the gaming-industry default; subscription revenue reportedly grew ~105% YoY in Q1 2026 while ad-revenue share compressed (~63%→56%) per Liftoff/AppsFlyer's "State of App Monetization 2026."

## Android App Development
- **Google Play / system update roundup (9to5Google, July 13)**: Play Store layout improved for tablets/foldables (less scrolling); EU Play Store now adds AI-generated-image labels (compliance-relevant if you publish AI-generated content); Google One gets a native in-app storefront for smoother purchases.
- **Android Studio "Quail 2" RC 2** released, moving the cycle closer to stable (stable Quail 2 shipped late June with a redesigned multi-chat Agent Mode, LeakCanary built into the Profiler for ~5x faster heap analysis, and one-click "Fix with Agent" leak remediation).
- **Pixel update (July 7)**: bug-fix-only patch (bootloop fix, widget contrast fix); Samsung's One UI 9 (Android 17) launches July 22 with the Z Fold 8/Flip 8 — worth planning compatibility testing now.
- **Jetpack Compose**: no new stable release in-window; most recent dated builds are `compose-ui`/`material` 1.12.0-beta02 and Material3 Adaptive 1.0.0-alpha01 (Posture APIs, PaneScaffoldDirective) from July 1.
- Android Weekly / ProAndroidDev: no issue confirmed newer than Android Weekly #734 (July 5); nothing dated July 10–14 surfaced.

## Competitive Landscape (Google / Apple Speech Solutions)
- **Nothing squarely dated July 12–14** for Google/Apple/Amazon/Microsoft speech recognition specifically — the niche was quiet this exact window.
- Closest adjacent context (outside window, included for continuity only):
  - Apple **iOS 27 beta 3** (July 6) enabled Siri voice "Pace"/"Expressivity" customization sliders and more accurate on-device dictation — first hands-on signal of Apple's rebuilt Siri/dictation pipeline.
  - Google Cloud's **Chirp 3** transcription model (Speech-to-Text API V2) — diarization, auto language ID, built-in denoiser — reached GA slightly before this window.
  - OpenAI's **GPT-Live-1 / GPT-Live-1 mini** (July 8) — new full-duplex conversational voice models; relevant as competitive pressure even though OpenAI isn't in the tracked vendor set.
- **Bottom line**: no new Google/Apple product launched in the last 24–48h.

---
*Freshness note: this was a broadly quiet 24–48-hour window across every focus area except Claude Code (three releases shipped July 12–14) and GitHub trending repos. Where nothing dated July 12–14 was found, the closest recent items were included for continuity and explicitly flagged as outside the window rather than presented as new.*
