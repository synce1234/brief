# Morning Brief — July 13, 2026

## Speech Recognition
- **No major breaking news in the last 24 hours.** Closest fresh item: unverified aggregator reports (July 13) of OpenAI launching **"GPT-Live,"** a full-duplex voice AI that listens/reasons/speaks simultaneously with real-time translation and live search — treat cautiously, no official OpenAI post found yet.
- **ESPnet** shows rolling commits through July 10: PyTorch bumped to 2.9.1, XPU shape-bucketing + `torch.compile` support, a Whisper-tokenizer compatibility fix for Transformers v5, an `espnet3` restructure (components/systems/parallel/utils), and new ASR recipes (Mandarin Tal-zh-adult-teach, Korean kosp2e). No discrete release tag yet.
- Continuity context (past 1–3 weeks, nothing closer surfaced):
  - **NVIDIA Nemotron Speech ASR**: leaderboard-topping open ASR model, ~10x faster in-class, 2nd-fastest streaming latency (0.07s to final transcript) on Artificial Analysis; `Nemotron-3.5-ASR-Streaming-0.6B` (June 4) covers 40 languages at 80ms–1s latency.
  - **SpeechBrain**: last major release March 31 (SpeechLLM ASR/translation recipes, streaming SSL) — nothing newer.
  - **Whisper** (official OpenAI repo): still pinned at v20250625; `whisper.cpp` at v1.8.6 (June 2026).
  - **Interspeech 2026** (Sydney, Sept 27–Oct 1): early-bird registration closes July 15; Audio Reasoning Challenge drew 156 teams from 18 countries.
  - **Papers With Code** revived as paperswithcode.co (HF/Meta-backed); Open ASR Leaderboard remains active (86 systems, 12 datasets).
  - No eess.AS/cs.CL arXiv papers dated exactly July 12–13; nearest recent items ("WhisperPipe," "MURMUR") are late June.
  - Sebastian Raschka's substack has no ASR-specific post recently — latest content is LLM-training focused.

## AI Applications / Trending Models (Claude Code, MCP, Hugging Face, GitHub)
- **MCP 2026-07-28 release candidate is out now** (final spec ships July 28) — largest revision since launch: a stateless protocol core (enables plain round-robin load balancing, no more sticky sessions), a new **MCP Apps** extension (sandboxed server-rendered UI), a **Tasks** extension for long-running work, and OAuth/OIDC-aligned Enterprise-Managed Authorisation now stable.
- **Notable friction**: reports (July 13) that Google, Microsoft, Salesforce, Snowflake, and ServiceNow are backing a rival "shared standard" for agent-to-business-software connections, positioned against MCP — worth watching as a potential fork in the ecosystem.
- **Claude Code**: recent releases add a built-in sandboxed desktop browser (navigate/interact with docs or sites directly), an upgraded `/doctor` that auto-fixes install issues and prunes unused MCP servers/plugins/bloated CLAUDE.md files, improved auto-mode safety on Bedrock/Vertex/Foundry, and a ~400MB cut in auto-updater peak memory.
- **GitHub Trending (today)**: OpenCut (open-source CapCut alternative, 65.9k★, +1,077 today), HKUDS/Vibe-Trading (AI trading agent, +1,148), Shubhamsaboo/awesome-llm-apps (119k★, +1,006), Graphify-Labs/graphify (AI code→knowledge-graph assistant, +1,028), github/spec-kit (Spec-Driven Development, 120.5k★, +508), Nutlope/hallmark (anti-AI-slop design skill for Claude Code/Cursor/Codex, +802).
- **Hugging Face**: no confirmed July 13 trending shakeup; as of early July, top downloads remain DeepSeek V4.1 Flash, Qwen 3.7, GLM-6, Llama 4.5, Gemma 4 — Chinese open-weight models now hold 5 of the top 10 slots, a record.
- **Google Gemini 3.5 Pro**: full architecture rebuild with 2M context and a "Deep Think" reasoning layer, targeting GA around July 17–22; AI Studio whitelist preview ran July 8–12.
- **ByteDance**: Seedance 2.5 (native 30-sec single-pass video, 4K, joint audio-video generation) is in its public-launch window (opened July 3); CapCut integration expected mid-July, API access late July.
- **Research**: ICML 2026 (Seoul, wrapped July 11) Outstanding Paper Awards went to two diffusion-model papers ("The Flexibility Trap," "High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions"); Test of Time Award to DeepMind's async-RL paper.

## Advertisement and IAP Trending
- **AdMob**: Android SDK release notes refreshed July 8 (minor dependency/nullable-annotation fixes); the legacy Mobile Ads SDK is now in maintenance mode as Google pushes developers toward the GMA Next-Gen SDK.
- **AppLovin**: stock jumped ~11% (July 1) on analyst upgrades tied to its June 30 opening of its self-serve ad platform to non-gaming/e-commerce advertisers for the first time in 14 years; Q2 earnings land Aug 5.
- **Google Play Terms of Service update (effective July 29)**: auto-renewal charges can now be processed up to 2 days before the billing date (was 1 day); new "System Services" transparency section added; account liability for shared credentials tightened.
- **Google Play expanded billing choice**: external links/alternative billing now allowed in US/UK/EU (10% service fee on first $1M/year) — rollout began June 30 and is continuing through July.
- **Android system update (July)**: adds a native, non-web storefront for Google One purchases — faster IAP/subscription checkout flow, relevant if you're benchmarking checkout UX.
- **Apple App Store Connect**: now supports bundling multiple IAPs/subscriptions into one review submission, plus new "group purchases" (shared subscription seats); an updated age-rating questionnaire for social-media apps is rolling out this month.
- No new Meta Audience Network or Unity Ads news found in this window.

## Android App Development
- **Android Bench (LLM coding-agent benchmark) update, July 12**: Google adopted the "Harbor" evaluation framework and added 8 models to the leaderboard — Claude Fable 5, Claude Sonnet 5, Claude Opus 4.8, GLM 5.2, Kimi K2.7 Code, MiniMax M3, Qwen 3.7 Plus, Qwen 3.7 Max; community task contributions now open via GitHub. Tasks probe Jetpack Compose migrations, wearable networking, platform API updates.
- **Android Studio "Quail 2" RC 2** shipped to the Beta channel in July.
- **Android 17 first post-launch update** rolling out in phases since ~July 7–8 to Pixel 6–10 series: fixes boot-loop bug, app-crash issue, misaligned system widgets, wallpaper shape-effect bug, Pixel 10 Pro Fold nav-button alignment. No security fixes in this patch.
- **Google Play services (July update)**: new native Google One storefront for IAP (see above), new API for more reliable work-profile setup, plus Maps/Android Auto/TV/Wear utility additions.
- No new Jetpack Compose stable/alpha release found dated in the last 24–48h — last dated build is `compose-ui 1.12.0-beta02` / `material3 1.5.0-alpha23` from July 1. Android Weekly #735 (due ~July 12) not yet indexed at search time.

## Competitive Landscape (Google / Apple Speech Solutions)
- **iOS 27 public beta — reported "this week."** Bloomberg's Mark Gurman, MacRumors (July 12), and Forbes (July 12) all point to imminent release; TechTimes (July 13) says it "arrives this week" without a confirmed exact day. It carries Apple's revamped **Siri AI**, upgraded on-device dictation, and voice customization.
- Continuity context: iOS 27 beta 3 (July 6) enabled Siri voice "Pace" and "Expressivity" sliders plus more accurate on-device dictation. Google Cloud's **Chirp 3** ASR model reached GA in Speech-to-Text API V2 (85+ languages, diarization, denoising). **Gemini 3.5 Live Translate** (near real-time speech-to-speech, 70+ languages) is live in Google Translate and in private preview in Google Meet.
- **Bottom line**: no major new product launched in the last 24–48h; the one genuinely fresh signal is the imminent iOS 27 public beta carrying Siri AI's dictation/voice upgrades.

---
*Freshness note: true last-24-hour news was thin across every focus area this morning. Where nothing dated July 12–13 was found, the most recent relevant items (past 1–3 weeks) were included for continuity and explicitly dated above rather than omitted.*
