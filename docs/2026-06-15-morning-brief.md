# Morning Brief — 2026-06-15

> Auto-generated daily brief covering speech recognition, AI models, Claude Code / MCP, and Android development.

---

## 🎙️ Speech Recognition

Three new papers on arXiv this week worth reading:

### [Pretrained self-supervised speech models can recognize unseen consonants](https://arxiv.org/abs/2606.11542) *(Jun 10)*
Researchers fine-tuned Wav2Vec2 and HuBERT on click-rich Khoisan languages. Fine-tuned models consistently outperformed on click phonemes, suggesting that large pre-trained SSL models transfer surprisingly well to typologically rare sounds.

### [Towards Deep Contextual Reasoning for ASR via Metadata-Driven Reasoning Chains](https://arxiv.org/abs/2606.10838) *(Jun 9)*
Proposes using Speech-LLMs with metadata-driven reasoning chains to handle rare, domain-specific terms where keyword biasing falls short. Reports meaningful gains on rare words and named entities.

### [Rethinking Depth: A study of the Recursive-Transformer for Speech Recognition](https://arxiv.org/abs/2606.09357) *(Jun 8)*
Layer sharing via depth recursion (Recursive-Transformer) achieves comparable ASR performance while **cutting parameter count by 66%**. Relevant for on-device / Android deployment.

*No major releases from Whisper, ESPnet, NeMo, or SpeechBrain repos this week.*

---

## 🤖 Trending AI Models (HuggingFace / GitHub)

**Top downloads on HuggingFace (mid-June snapshot):**
| Rank | Model | Notable |
|------|-------|---------|
| 1 | DeepSeek V4.1 Flash | Surged to #1 within a week of release |
| 2 | Qwen 3.7 | — |
| 3 | Gemma 4 | Apache 2.0; strong commercial clarity |
| 4 | GLM-6 | — |
| 5 | Llama 4.5 | — |

Chinese open-weight models now hold 5 of the top 10 download slots — the highest concentration on record. Embedding models (NV-Embed, BGE-M3, Sentence-Transformers) dominate the long-tail.

**Kimi K2.6** is gaining traction as a strong open-weight option for coding, tool use, and long-horizon agentic workflows.

**Trending GitHub AI repos:**
- Pure-Rust WebGPU inference engine — OpenAI-API-compatible, GGUF-native
- [LeRobot](https://github.com/huggingface/lerobot) — end-to-end learning for robotics, gaining new stars

**Sources:** [Presenc AI HuggingFace Trending June 2026](https://presenc.ai/research/huggingface-trending-models-june-2026) · [HuggingFace State of Open Source Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)

---

## 🛠️ Claude Code & MCP Servers

### Claude Fable 5 launched — June 9, 2026
Anthropic released **Claude Fable 5** (same underlying model as Claude Mythos 5), their most capable publicly available model to date:
- **1M token** context window, 128K max output tokens
- Pricing: **$10 / M input · $50 / M output** (2× Opus 4.x rates)
- Available on Claude API, Amazon Bedrock, Vertex AI, Microsoft Foundry
- Knowledge cut-off: January 2026
- Note: briefly suspended after U.S. government export directive; re-availability may be region-gated

**Sources:** [Anthropic announcement](https://www.anthropic.com/news/claude-fable-5-mythos-5) · [TechCrunch](https://techcrunch.com/2026/06/09/anthropic-released-claude-fable-5-its-most-powerful-model-publicly-days-after-warning-ai-is-getting-too-dangerous/)

### Claude Code updates (June 8 changelog)
- **`--safe-mode` flag** — starts Claude Code with all customizations + MCP servers disabled (useful for debugging)
- **`/cd` command** — move a session to a new working directory without restarting
- **`disableBundledSkills` setting** — opt out of built-in skills
- Fixed: MCP per-server timeout config values below 1000 ms were being floored to 1 s
- Fixed: Enterprise managed MCP policies now enforced correctly on reconnect and IDE-typed configs
- **Nested sub-agents** — agents can now spawn their own sub-agents for task decomposition

**Source:** [Claude Code changelog](https://code.claude.com/docs/en/changelog)

### MCP ecosystem
- Anthropic released **20+ new legal MCP connectors** and 12 practice-area plugins (research, contracts, discovery, matter management, legal aid)
- Claude Managed Agents now support **self-hosted sandboxes** with private MCP server access
- Community consensus: Context7, GitHub MCP, and Playwright MCP cover ~80% of Claude Code workflows

---

## 🤖 Android Development

### Jetpack Compose Material3 1.5.0-alpha21 *(June 3, 2026)*
- New **Condition APIs** for adaptive layouts
- **Pane Scaffold Directive APIs** and **Adaptive Pane Scaffold APIs**
- Changes to bottom sheets and text fields
- Compose BOM alpha: `2026.05.02`

**Compose 1.11** (stable from April '26 release) is the current stable baseline:
- Shared element debug tools
- Trackpad event support
- Core Compose modules versioned at 1.11

No new stable Compose release in the last 24 hours. Next stable drop expected later in June.

**Sources:** [Android Developers Blog — April '26 release](https://android-developers.googleblog.com/2026/04/jetpack-compose-april-2026-updates.html) · [androidx releases](https://developer.android.com/jetpack/androidx/versions/all-channel)

---

*Generated: 2026-06-15 | Sources: arXiv, HuggingFace, Anthropic, Android Developers Blog*
