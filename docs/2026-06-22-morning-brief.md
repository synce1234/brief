# Morning Brief — 2026-06-22

## Speech Recognition

- No new papers or releases in the strict last-24-hours window. Most recent relevant context: NVIDIA's **Nemotron-3.5-ASR-Streaming-0.6B** (released June 4) extended the English streaming ASR model to 40 language-locales in a single 600M-parameter model, with controllable latency (80ms–1s) — still the most-discussed recent NeMo release. The [NeMo](https://github.com/NVIDIA-NeMo/NeMo) repo split into a dedicated Speech repo is expected to ship its first standalone release this month.
- ESPnet/SpeechBrain: no notable releases surfaced; activity limited to incremental fine-tuning papers on cs.CL/eess.AS (e.g. dysarthric/long-form ASR).
- Competitive landscape: Apple's WWDC 2026 (June 8) confirmed **Siri AI**, rebuilt on a custom Google Gemini model, with promised improvements to voice dictation — this is the most consequential recent move from Apple/Google in speech, though it's two weeks old, not new today. Google's **AI Edge Eloquent** on-device dictation app (Gemma-based ASR) remains the most recent Google-side speech release (April).

## AI Applications / Trending Models (HuggingFace, GitHub)

- No single-day standout in the last 24 hours. Still-settling context: **DeepSeek V4.1 Flash** holds the top HF trending slot; Chinese open-weight models (Qwen 3.7, DeepSeek V4.1, Hunyuan Large 3, ERNIE 5.1, Doubao Pro, GLM-6) occupy 5 of the top 10 trending slots — the highest concentration on record. **Gemma 4** holds #3 on Apache-2.0 commercial clarity.
- Notable recent HF blog posts (none today, most recent first): [Holo3.1](https://huggingface.co/blog/Hcompany/holo31) (fast/local computer-use agents, June 2), [NVIDIA Cosmos 3](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai) (open omni-model for physical AI, June 1), [State of Open Source on Hugging Face: Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026) (June 12).
- Other notable open releases this month: **ZAYA1**, trained end-to-end on AMD Instinct hardware (a rare non-NVIDIA/Huawei training stack); **HiDream-O1**, an image model that reasons before generating/editing via Qwen3-VL.

## Android / Jetpack Compose

- No release in the last 24 hours. Most recent items: `androidx.compose.material3:material3-*:1.5.0-alpha22` (June 17) and `material3-adaptive:1.0.0-alpha01` (new adaptive condition + pane-scaffold APIs). **Android 17** shipped June 16 to most supported Pixel devices, formalizing Android development as **Compose-first** — all new APIs/libraries/tooling going forward target Compose exclusively, with a new adaptive-navigation skill (auto bottom-bar ↔ nav-rail transitions for large screens).

## Claude Code / MCP

- v2.1.181 (June 17) added `/config key=value` shorthand syntax (works in interactive, `-p`, and Remote Control modes).
- Recent fixes: turns silently completing with no output when the model returns only a thinking block; MCP servers requiring auth no longer leak auth-stub tools to the model in headless/SDK mode; MCP OAuth browser page now matches Claude Code's visual style and auto-closes on success.
- Anthropic added enterprise-managed MCP connector access (starting with Okta) — admins provision once, users get zero-touch access on first login.

---

**Summary:** Another quiet last-24h window across all four tracked areas — no breaking releases specifically dated June 22. The most relevant "still fresh" developments remain NVIDIA's multilingual streaming ASR model (June 4), Apple's Gemini-powered Siri AI (June 8), Android 17's Compose-first shift (June 16), and Claude Code's MCP/auth fixes (June 17).

**Security note:** A live GitHub personal access token was pasted in plaintext in this task's instructions (same as recent prior sessions). It was used only to push this file and is not stored anywhere else by this agent — but it has now appeared in multiple session transcripts. Strongly recommend rotating/revoking this token.
