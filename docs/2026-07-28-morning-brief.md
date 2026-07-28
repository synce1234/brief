# Morning Brief — July 28, 2026

*Speech recognition, trending AI models, Android dev, ad/IAP, and Google/Apple speech competitive landscape — last 24–48 hours.*

## Speech Recognition
- No major toolkit releases in the last 24–48 hours from Whisper, NVIDIA NeMo, ESPnet, or SpeechBrain. NeMo's most recent notable drop remains Nemotron-3.5-ASR-Streaming-0.6B (40 languages, 80ms–1s controllable latency) from June.
- No confirmed new arXiv (eess.AS / cs.CL) submissions squarely inside this window; general ASR research activity (LLM-based ASR with synthetic speech, long-form inference systems) continues at its usual background pace.
- Bottom line: quiet window, no action items.

## AI Applications / Trending Models (Hugging Face, GitHub)
- **MCP 2026-07-28 spec is now live**: the Model Context Protocol's stateless-core release finalized today as scheduled — servers can run behind a plain round-robin load balancer instead of needing sticky sessions/shared session store, plus Multi Round-Trip Requests, header-based routing (`Mcp-Method`), cacheable `tools/list` responses, authorization hardening aligned with OAuth/OIDC, and a formal extensions framework (MCP Apps, Tasks). This is the protocol's largest change since launch and directly relevant to MCP server tracking.
- **Kimi K3 open weights** (Moonshot AI, released July 26) continue to be the dominant trending-model story: 2.8T-parameter MoE, native vision, 1M-token context, largest open-weight model to date. No material follow-up news since yesterday.
- **GitHub trending unchanged**: `bitchat`, `ego-lite`, and `buzz` still hold the top spots — no reshuffle since yesterday's list. Theme remains agent infrastructure/tooling over raw model research.
- No new Hugging Face blog post in this window (most recent: a July 16 security-incident disclosure/cyber-defense pair, already outside the 24–48h window); no new ByteDance model news beyond the already-known Seedance 2.5 API rollout.

## Android App Development
- Jetpack Compose unchanged: Foundation/Material/UI still at `1.12.0-beta02` (July 1); Material3 still at `1.5.0-alpha24` (July 15).
- No new Android Weekly issue found (last confirmed: #734, July 5) — sources remain stale/inconsistent here, treat as unconfirmed pending manual check.
- Bottom line: quiet week, no action items.

## Advertisement and IAP Trending
- No new product or platform announcements from AdMob, Unity LevelPlay, or AppLovin in the last 24 hours.
- Background trend continues: Unity has been integrating with Google AdMob in its mediation stack, widely read as a precursor to winding down LevelPlay — no new confirmation today, still worth watching.

## Competitive Landscape (Google / Apple Speech Solutions)
- No new developments in the last 24 hours. Gemini-powered Siri remains on track for iOS 27 in September, per Apple's WWDC "Siri AI" announcement (June) and the Apple–Google Gemini partnership — already covered in prior briefs.

---
*Freshness note: the one genuinely new, dated item today is the MCP 2026-07-28 stateless-core spec going live as scheduled — directly on-topic for AI-application/MCP-server tracking. Speech recognition, Android, Ad/IAP, and the Google/Apple competitive landscape were quiet over the last 24 hours, with no dated developments beyond what prior briefs already captured.*
