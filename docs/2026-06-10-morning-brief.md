# Morning Brief — June 10, 2026

> Focus areas: Speech Recognition · AI Models (HuggingFace / GitHub) · Android Development · Claude Code & MCP

---

## 1. Speech Recognition

### NVIDIA Nemotron 3.5 ASR Streaming 0.6B *(June 4)*
NVIDIA released a new streaming ASR model extending English to **40 language-locales** in a single 600M-parameter checkpoint. Supports language-ID prompt conditioning, automatic language detection, punctuation/capitalization, and configurable low-latency streaming chunk sizes.
- [Model on HuggingFace](https://huggingface.co/nvidia/nemotron-speech-streaming-en-0.6b)

### Far Field ASR (FFASR) Leaderboard *(June 9)*
Treble Technologies and Hugging Face launched the **industry's first open, community-driven benchmark** for evaluating ASR models under realistic far-field acoustic conditions. Addresses a long-standing gap in real-world evaluation for smart speakers, meeting rooms, and open environments.
- [Announcement](https://finance.yahoo.com/sectors/technology/articles/treble-technologies-hugging-face-address-100900767.html)

### Meta Omnilingual ASR *(recent)*
Meta open-sourced a suite of ASR models covering **1,600+ languages**, with their 7B-LLM-ASR system achieving character error rates (CER) below 10 for 78% of those languages — state-of-the-art at unprecedented scale.
- [Meta AI Blog](https://ai.meta.com/blog/omnilingual-asr-advancing-automatic-speech-recognition/)

### Google Chirp 3 *(GA)*
Google announced **General Availability** of Chirp 3: Transcription in the Speech-to-Text API V2 — the latest generation multilingual ASR model with improved accuracy and language coverage.
- [Google Cloud Release Notes](https://docs.cloud.google.com/speech-to-text/docs/release-notes)

---

## 2. AI Models — HuggingFace & GitHub Trending

### HuggingFace Notable Models
| Model | Description |
|-------|-------------|
| **Sapiens2** | Human-centric vision transformers (0.4B–5B params) pretrained on ~1B curated human images; +4 mAP in pose estimation, +24.3 mIoU in body-part segmentation |
| **DeepSeek-OCR-2** | OCR-focused VLM combining SAM ViT-B + Qwen2 encoder with DeepSeek-V2 MoE language model |
| **LLaDA2** | Discrete diffusion language models using block-wise iterative refinement (masked→unmasked) |
| **NucleusMoE-Image** | 2B active / 17B total params sparse MoE for image generation |

### GitHub Trending AI
- **OpenClaw** — 210k+ stars; local AI assistant gateway connecting to 50+ integrations (WhatsApp, Telegram, Slack, Signal, iMessage). Fastest-growing open-source project of 2026.
- **ComfyUI** — 106k+ stars; node-based visual workflow for image generation pipelines, growing rapidly with open-source video models coming online.

---

## 3. Claude Code Updates

### Claude Fable 5 Released *(v2.1.170 — June 9)*
Claude **Fable 5** — a Mythos-class model — is now available for general use, exceeding capabilities of all prior models. Available in Claude Code on supported plans.

### v2.1.169 — June 8 (40+ fixes)
Key additions:
- **`--safe-mode` flag**: Starts Claude Code with all customizations disabled (CLAUDE.md, plugins, skills, hooks, MCP servers) for clean troubleshooting.
- **`/cd` command**: Move a session to a new working directory without breaking the prompt cache.
- **`disableBundledSkills`** setting + env var to hide built-in skills.
- **`post-session` lifecycle hook** for self-hosted runners: snapshot uncommitted work or export logs after a session ends.
- Fixed background agents ignoring project-level `env` values.
- Improved `TaskCreate` reliability with automatic malformed input repair.
- Reduced CPU usage during streaming and spinner animations.

### v2.1.166 — June 6
- **`fallbackModel` setting**: Configure up to 3 fallback models when the primary is unavailable.
- **Glob patterns in deny rules**: Use `"*"` to deny all tools in a rule position.
- `MAX_THINKING_TOKENS=0` now disables thinking on default-thinking models.

**Full changelog**: [code.claude.com/docs/en/changelog](https://code.claude.com/docs/en/changelog)

---

## 4. MCP (Model Context Protocol)

### Upcoming Spec Release Candidate *(ships July 28, 2026)*
The next MCP specification RC introduces:
- **Stateless protocol core** — cleaner transport contracts
- **Extensions framework** — opt-in capability negotiation
- **Tasks** — long-running async operations
- **MCP Apps** — higher-level application model
- **Authorization hardening** + formal deprecation policy

Community size: **97M+ monthly SDK downloads**, 81k+ GitHub stars, 500+ public servers, supported by Anthropic, OpenAI, Google, Microsoft, AWS.
- [MCP Roadmap](https://modelcontextprotocol.io/development/roadmap)

---

## 5. Android Development

### Google Play Policy Updates *(effective now / upcoming)*
- **Health & Fitness**: Updated guidelines support **Android 16 granular permissions** and new Health Connect data types (Menstrual Cycle Phases, Alcohol Consumption, Symptoms). Prohibited: using sensitive health data for employment/insurance eligibility.
- **Location Permissions**: Location button is now the **recommended minimum scope** for precise location access.
- **Contacts Permissions**: New policy — apps that don't need broad access must use the Android Contact Picker instead.
- **Target API Level deadline**: All new apps and updates must target **Android 16 (API level 36)** by **August 31, 2026**.
- **Identity verification**: Starting 2026, all developers must verify identity and register apps, even those distributed outside the Play Store.

**Source**: [Play Console Policy Announcements](https://support.google.com/googleplay/android-developer/answer/16926792?hl=en)

---

*Generated: 2026-06-10 | Sources: HuggingFace, GitHub, Anthropic Docs, Google Play Console, Meta AI, NVIDIA*
