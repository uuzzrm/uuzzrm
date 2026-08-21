<div align="center">
  <img src="https://raw.githubusercontent.com/uuzzrm/uuzzrm/bd5e69a/assets/profile-header.svg" alt="Ruiming Zhao — Prysai AI systems and developer tools" width="100%" />
</div>

<p align="center">
  <a href="https://prysai.com"><strong>Prysai</strong></a>&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="#selected-contributions">Selected work</a>&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="#working-set">Working set</a>&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="#account-star-history">Star history</a>
</p>

<table>
  <tr>
    <td width="62%" valign="top">
      <sub>RUIMING ZHAO · UZZRM</sub><br /><br />
      I build and inspect AI systems that hold up beyond the demo: agents, retrieval, evaluation, and tool use in real developer workflows.<br /><br />
      The standard is simple: fewer impressive demos, more systems that can be tested, understood, and improved.
    </td>
    <td width="38%" valign="top">
      <sub>WORKING FOCUS</sub><br /><br />
      <strong>AI agents</strong><br />
      <strong>Developer tools</strong><br />
      <strong>Reliable delivery</strong><br /><br />
      <sub>Network operations · independent development · image-model training and fine-tuning</sub>
    </td>
  </tr>
</table>

<sub>Six years in network operations and four years as an independent developer inform the work. Since 2024, this has also included full-quantization training and fine-tuning workflows for image AI models.</sub>

## Building with Prysai

<table>
  <tr>
    <td width="28%" valign="top"><sub>PUBLIC FLAGSHIP</sub><br /><br /><a href="https://github.com/Prysai/Prysai-LLM-Playbook"><strong>Prysai LLM<br />Playbook</strong></a></td>
    <td width="72%" valign="top">An evidence-led, six-language learning and practice system for reliable work with LLMs, Codex, skills, tools, and agent workflows.<br /><br /><a href="https://github.com/Prysai/Prysai-LLM-Playbook">repository</a> · <a href="https://docs.prysai.com/llm-playbook/">documentation</a> · <a href="https://github.com/Prysai/Prysai-LLM-Playbook/releases/tag/v0.1.0-alpha">v0.1.0-alpha</a><br /><br /><sub>Public development candidate. Structure and checks are inspectable; learner validation and independent review remain in progress.</sub></td>
  </tr>
</table>

## Selected contributions

A curated, evidence-first record of changes accepted into other projects. The full directory stays available below.

<table>
  <tr>
    <td width="50%" valign="top"><sub>AGENT RUNTIME</sub><br /><br /><a href="https://github.com/microsoft/agent-framework"><strong>Microsoft Agent Framework</strong></a><br /><br />Telemetry configuration, skill-script behavior, prompt-cache usage, and operational visibility.<br /><br /><a href="https://github.com/microsoft/agent-framework/pull/7695">latest merged PR</a></td>
    <td width="50%" valign="top"><sub>RELIABILITY</sub><br /><br /><a href="https://github.com/nullcache/corecoder-ts"><strong>corecoder-ts</strong></a><br /><br />Cancellation, timeouts, context accounting, protocol edge cases, and CLI contracts.<br /><br /><a href="https://github.com/nullcache/corecoder-ts/pull/7">latest merged PR</a></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><sub>SAFETY &amp; OPERATIONS</sub><br /><br /><a href="https://github.com/oomol-lab/open-connector"><strong>Open Connector</strong></a><br /><br />Connector lifecycle support and redaction that keeps credentials out of run logs.<br /><br /><a href="https://github.com/oomol-lab/open-connector/pull/342">latest merged PR</a></td>
    <td width="50%" valign="top"><sub>LANGUAGE ANALYSIS</sub><br /><br /><a href="https://github.com/squid-protocol/gitgalaxy"><strong>GitGalaxy</strong></a><br /><br />Parser correctness across TypeScript, C#, C++, and Go edge cases.<br /><br /><a href="https://github.com/squid-protocol/gitgalaxy/pull/1764">latest merged PR</a></td>
  </tr>
</table>

<details>
<summary><strong>Browse the complete merged contribution directory</strong></summary>

<br />

<table>
  <tr>
    <th align="left">Proof of work</th>
  </tr>
  <tr>
    <td><sub>COLLABORATION &amp; TEST RELIABILITY</sub><br /><a href="https://github.com/jupyterlab/jupyter-chat"><strong>jupyterlab/jupyter-chat</strong></a> · <a href="https://github.com/jupyterlab/jupyter-chat/pull/521">PR #521</a> · <a href="https://github.com/jupyterlab/jupyter-chat/pull/486">#486</a> · merged<br /><br />Eliminated SQLite YStore lock contention in parallel UI tests, then made internal chat ID and timestamp mutations synchronous while retaining observer delivery without background-task leakage.</td>
  </tr>
  <tr>
    <td><sub>AGENT RUNTIME &amp; OPERATIONS</sub><br /><a href="https://github.com/microsoft/agent-framework"><strong>microsoft/agent-framework</strong></a> · <a href="https://github.com/microsoft/agent-framework/pull/7695">PR #7695</a> · <a href="https://github.com/microsoft/agent-framework/pull/7625">#7625</a> · <a href="https://github.com/microsoft/agent-framework/pull/7622">#7622</a> · <a href="https://github.com/microsoft/agent-framework/pull/7597">#7597</a> · merged<br /><br />Made rejected MCP skill archives visible at the operational warning level, preserved Mistral prompt-cache usage details, clarified supported skill-script arguments, and forwarded GitHub Copilot telemetry configuration to its CLI client.</td>
  </tr>
  <tr>
    <td><sub>AGENT CLI &amp; INTEGRATION</sub><br /><a href="https://github.com/gnt-ai/gnt"><strong>gnt-ai/gnt</strong></a> · <a href="https://github.com/gnt-ai/gnt/pull/183">PR #183</a> · <a href="https://github.com/gnt-ai/gnt/pull/182">#182</a> · <a href="https://github.com/gnt-ai/gnt/pull/178">#178</a> · <a href="https://github.com/gnt-ai/gnt/pull/177">#177</a> · <a href="https://github.com/gnt-ai/gnt/pull/176">#176</a> · <a href="https://github.com/gnt-ai/gnt/pull/175">#175</a> · <a href="https://github.com/gnt-ai/gnt/pull/174">#174</a> · <a href="https://github.com/gnt-ai/gnt/pull/173">#173</a> · <a href="https://github.com/gnt-ai/gnt/pull/172">#172</a> · <a href="https://github.com/gnt-ai/gnt/pull/168">#168</a> · <a href="https://github.com/gnt-ai/gnt/pull/164">#164</a> · <a href="https://github.com/gnt-ai/gnt/pull/163">#163</a> · <a href="https://github.com/gnt-ai/gnt/pull/162">#162</a> · <a href="https://github.com/gnt-ai/gnt/pull/138">#138</a> · merged<br /><br />Expanded CLI automation with JSON output and connector coverage; added guarded Cline and OpenAI Agents SDK integrations; and strengthened terminal formatting, repository conventions, documentation, and review output.</td>
  </tr>
  <tr>
    <td><sub>ROUTING &amp; OBSERVABILITY</sub><br /><a href="https://github.com/vllm-project/semantic-router"><strong>vllm-project/semantic-router</strong></a> · <a href="https://github.com/vllm-project/semantic-router/pull/2907">PR #2907</a> · <a href="https://github.com/vllm-project/semantic-router/pull/2896">#2896</a> · <a href="https://github.com/vllm-project/semantic-router/pull/2874">#2874</a> · merged<br /><br />Corrected Router Replay attribution, wired configured Milvus consistency through cache reads and collection setup, and removed a racy Dashboard assertion while retaining stable lifecycle guarantees.</td>
  </tr>
  <tr>
    <td><sub>VOICE AI &amp; CONFIGURATION</sub><br /><a href="https://github.com/livekit/agents"><strong>livekit/agents</strong></a> · <a href="https://github.com/livekit/agents/pull/6866">PR #6866</a> · <a href="https://github.com/livekit/agents/pull/6810">#6810</a> · merged<br /><br />Added explicit Google Speech-to-Text project selection while preserving credential-based discovery, and corrected the final sentence span so tokenization includes the input's last character.</td>
  </tr>
  <tr>
    <td><sub>CONNECTORS &amp; PRODUCT INTEGRATION</sub><br /><a href="https://github.com/oomol-lab/open-connector"><strong>oomol-lab/open-connector</strong></a> · <a href="https://github.com/oomol-lab/open-connector/pull/342">PR #342</a> · <a href="https://github.com/oomol-lab/open-connector/pull/332">#332</a> · <a href="https://github.com/oomol-lab/open-connector/pull/300">#300</a> · merged<br /><br />Expanded the Resend connector from basic sending into batch, scheduling, retrieval, cancellation, and attachment workflows; made run-log summaries resilient to malformed values; and redacted credentials in protocol-relative and non-HTTP URLs.</td>
  </tr>
  <tr>
    <td><sub>VOICE AI &amp; AUDIO PIPELINES</sub><br /><a href="https://github.com/pipecat-ai/pipecat"><strong>pipecat-ai/pipecat</strong></a> · <a href="https://github.com/pipecat-ai/pipecat/pull/5298">PR #5298</a> · merged<br /><br />Made AssemblyAI speech recognition inherit the pipeline input sample rate unless callers provide an explicit override.</td>
  </tr>
  <tr>
    <td><sub>EVALUATION &amp; OBSERVABILITY</sub><br /><a href="https://github.com/thangldw/ragops"><strong>thangldw/ragops</strong></a> · <a href="https://github.com/thangldw/ragops/pull/30">PR #30</a> · merged<br /><br />Added an offline Phoenix recorded-score adapter with deterministic case-ID joins, synthetic fixtures, documentation, and tests.</td>
  </tr>
  <tr>
    <td><sub>AGENT TOOLING &amp; COMPATIBILITY</sub><br /><a href="https://github.com/ag2ai/ag2"><strong>ag2ai/ag2</strong></a> · <a href="https://github.com/ag2ai/ag2/pull/3160">PR #3160</a> · <a href="https://github.com/ag2ai/ag2/pull/3148">#3148</a> · merged<br /><br />Added HEIC and HEIF MIME types to the Gemini image-input path, and made persistent sub-agent delegation reuse one stream instance so its turn lock actually serializes concurrent work.</td>
  </tr>
  <tr>
    <td><sub>AGENT TOOLING &amp; COMPATIBILITY</sub><br /><a href="https://github.com/mlflow/mlflow"><strong>mlflow/mlflow</strong></a> · <a href="https://github.com/mlflow/mlflow/pull/25010">PR #25010</a> · <a href="https://github.com/mlflow/mlflow/pull/25000">#25000</a> · merged<br /><br />Preserved provider-specific usage metadata across Gemini, Anthropic, and OpenAI-compatible gateway adapters, with regression coverage for normalized and nested usage details.</td>
  </tr>
  <tr>
    <td><sub>AGENT TOOLING &amp; DOCUMENTATION</sub><br /><a href="https://github.com/jupyterlab/jupyter-ai"><strong>jupyterlab/jupyter-ai</strong></a> · <a href="https://github.com/jupyterlab/jupyter-ai/pull/1639">PR #1639</a> · merged<br /><br />Added a concise interaction model explaining how chat, personas, ACP agents, model providers, and MCP tools fit together.</td>
  </tr>
  <tr>
    <td><sub>MEMORY &amp; OPERATIONS</sub><br /><a href="https://github.com/MSKazemi/kubeintellect"><strong>MSKazemi/kubeintellect</strong></a> · <a href="https://github.com/MSKazemi/kubeintellect/pull/116">PR #116</a> · <a href="https://github.com/MSKazemi/kubeintellect/pull/111">#111</a> · <a href="https://github.com/MSKazemi/kubeintellect/pull/105">#105</a> · merged<br /><br />Made the memory-recall similarity floor configurable, updated the <code>kube-q</code> Homebrew formula, and documented v4 data-handling boundaries.</td>
  </tr>
  <tr>
    <td><sub>LANGUAGE ANALYSIS &amp; RELIABILITY</sub><br /><a href="https://github.com/squid-protocol/gitgalaxy"><strong>squid-protocol/gitgalaxy</strong></a> · <a href="https://github.com/squid-protocol/gitgalaxy/pull/1764">PR #1764</a> · <a href="https://github.com/squid-protocol/gitgalaxy/pull/1761">#1761</a> · <a href="https://github.com/squid-protocol/gitgalaxy/pull/1760">#1760</a> · <a href="https://github.com/squid-protocol/gitgalaxy/pull/1724">#1724</a> · <a href="https://github.com/squid-protocol/gitgalaxy/pull/1710">#1710</a> · <a href="https://github.com/squid-protocol/gitgalaxy/pull/1657">#1657</a> · <a href="https://github.com/squid-protocol/gitgalaxy/pull/1655">#1655</a> · <a href="https://github.com/squid-protocol/gitgalaxy/pull/1654">#1654</a> · <a href="https://github.com/squid-protocol/gitgalaxy/pull/1639">#1639</a> · <a href="https://github.com/squid-protocol/gitgalaxy/pull/1201">#1201</a> · merged<br /><br />Improved detector correctness across TypeScript, C#, C++, and Go: recovered missed bodyless functions, retained unknown macro branches, eliminated phantom matches, recognized <code>readonly</code>/<code>ref</code> structs, and prevented silent archetype-metric dimension truncation.</td>
  </tr>
  <tr>
    <td><sub>AGENT TOOLING &amp; COMPATIBILITY</sub><br /><a href="https://github.com/mastra-ai/mastra"><strong>mastra-ai/mastra</strong></a> · <a href="https://github.com/mastra-ai/mastra/pull/21559">PR #21559</a> · <a href="https://github.com/mastra-ai/mastra/pull/21281">#21281</a> · <a href="https://github.com/mastra-ai/mastra/pull/21147">#21147</a> · merged<br /><br />Kept array text-streams valid for batched first chunks, resolved dynamic models once per assigned-tool batch, and fixed CommonJS schema compatibility by bundling the Zod conversion dependencies.</td>
  </tr>
  <tr>
    <td><sub>RELIABILITY &amp; EXPERIENCE</sub><br /><a href="https://github.com/felladrin/MiniSearch"><strong>felladrin/MiniSearch</strong></a> · <a href="https://github.com/felladrin/MiniSearch/pull/2390">PR #2390</a> · <a href="https://github.com/felladrin/MiniSearch/pull/2387">#2387</a> · <a href="https://github.com/felladrin/MiniSearch/pull/2386">#2386</a> · <a href="https://github.com/felladrin/MiniSearch/pull/2385">#2385</a> · <a href="https://github.com/felladrin/MiniSearch/pull/2377">#2377</a> · <a href="https://github.com/felladrin/MiniSearch/pull/2375">#2375</a> · <a href="https://github.com/felladrin/MiniSearch/pull/2372">#2372</a> · <a href="https://github.com/felladrin/MiniSearch/pull/2370">#2370</a> · <a href="https://github.com/felladrin/MiniSearch/pull/2367">#2367</a> · <a href="https://github.com/felladrin/MiniSearch/pull/2339">#2339</a> · <a href="https://github.com/felladrin/MiniSearch/pull/2324">#2324</a> · merged<br /><br />Reworked the search experience with a proper landing page, clearer result hierarchy, and reduced-motion-aware drawers; hardened it end-to-end for IME and non-Latin follow-ups, failure states, early rate limiting, SSRF-safe capped thumbnail fetches, and robust error handling.</td>
  </tr>
  <tr>
    <td><sub>AGENT ORCHESTRATION &amp; CLI</sub><br /><a href="https://github.com/a5c-ai/babysitter"><strong>a5c-ai/babysitter</strong></a> · <a href="https://github.com/a5c-ai/babysitter/pull/1727">PR #1727</a> · merged<br /><br />Made process-backed run creation safely adopt the active session-start bare run while retaining explicit-run and cross-boundary create-new safeguards.</td>
  </tr>
  <tr>
    <td><sub>AGENT RUNTIME &amp; RELIABILITY</sub><br /><a href="https://github.com/nullcache/corecoder-ts"><strong>nullcache/corecoder-ts</strong></a> · <a href="https://github.com/nullcache/corecoder-ts/pull/7">PR #7</a> · <a href="https://github.com/nullcache/corecoder-ts/pull/6">#6</a> · <a href="https://github.com/nullcache/corecoder-ts/pull/5">#5</a> · <a href="https://github.com/nullcache/corecoder-ts/pull/3">#3</a> · <a href="https://github.com/nullcache/corecoder-ts/pull/2">#2</a> · <a href="https://github.com/nullcache/corecoder-ts/pull/1">#1</a> · merged<br /><br />Hardened agent execution around cancellation, retry aborts, SSE and tool-input edge cases, request timeouts, context calibration, and CLI contracts; also documented installation, providers, tools, and runtime controls.</td>
  </tr>
  <tr>
    <td><sub>AGENT TOOLING &amp; QUALITY GATES</sub><br /><a href="https://github.com/wshobson/agents"><strong>wshobson/agents</strong></a> · <a href="https://github.com/wshobson/agents/pull/662">PR #662</a> · merged<br /><br />Made plugin evaluation preserve and resolve nested skill references relative to the current skill, preventing valid helpers from being incorrectly penalized.</td>
  </tr>
  <tr>
    <td><sub>PRIVACY &amp; EVALUATION</sub><br /><a href="https://github.com/seva9523/EvalRepro"><strong>seva9523/EvalRepro</strong></a> · <a href="https://github.com/seva9523/EvalRepro/pull/12">PR #12</a> · merged<br /><br />Added <code>--no-id_preview</code> to suppress sample ID previews while preserving sample and field digests.</td>
  </tr>
  <tr>
    <td><sub>DOCUMENTATION &amp; DEVELOPER EXPERIENCE</sub><br /><a href="https://github.com/abenneto/gandharva"><strong>abenneto/gandharva</strong></a> · <a href="https://github.com/abenneto/gandharva/pull/19">PR #19</a> · merged<br /><br />Refined README formatting and section headers.</td>
  </tr>
</table>

<sub>Every entry above links to a public pull request confirmed as merged into its upstream repository.</sub>

</details>

<!--
Maintenance format for future entries:
1. Confirm the upstream pull request has a non-empty merged_at value.
2. Group multiple merged PRs under the same upstream project.
3. Keep every merged PR linked and update the summary sentence when the totals change.
Only add an entry after the upstream PR is actually merged.
-->

## Working set

A focused upstream working set. These are study and contribution paths, not claims of original ownership.

<table>
  <tr>
    <td width="50%" valign="top">
      <strong><a href="https://github.com/thangldw/ragops">RAGOps</a></strong><br />
      <sub>Evaluation infrastructure</sub><br /><br />
      Offline evaluation and explainable release gates for RAG systems and agents.<br /><br />
      <a href="https://github.com/thangldw/ragops">upstream</a> · <a href="https://github.com/uuzzrm/ragops">my fork</a>
    </td>
    <td width="50%" valign="top">
      <strong><a href="https://github.com/pydantic/pydantic-ai">PydanticAI</a></strong><br />
      <sub>Typed agent runtime</sub><br /><br />
      Typed tools, structured outputs, and validation for production-minded agents.<br /><br />
      <a href="https://github.com/pydantic/pydantic-ai">upstream</a> · <a href="https://github.com/uuzzrm/pydantic-ai">my fork</a>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <strong><a href="https://github.com/PrefectHQ/fastmcp">FastMCP</a></strong><br />
      <sub>Tool connectivity</sub><br /><br />
      Protocol infrastructure for connecting MCP servers and clients.<br /><br />
      <a href="https://github.com/PrefectHQ/fastmcp">upstream</a> · <a href="https://github.com/uuzzrm/fastmcp">my fork</a>
    </td>
    <td width="50%" valign="top">
      <strong><a href="https://github.com/promptfoo/promptfoo">Promptfoo</a></strong><br />
      <sub>Quality and safety gates</sub><br /><br />
      Evaluation and red-teaming for prompts, agents, and RAG pipelines.<br /><br />
      <a href="https://github.com/promptfoo/promptfoo">upstream</a> · <a href="https://github.com/uuzzrm/promptfoo">my fork</a>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <strong><a href="https://github.com/browser-use/browser-use">Browser Use</a></strong><br />
      <sub>Real-world execution</sub><br /><br />
      Browser control for tool-using agents and workflow automation.<br /><br />
      <a href="https://github.com/browser-use/browser-use">upstream</a> · <a href="https://github.com/uuzzrm/browser-use">my fork</a>
    </td>
    <td width="50%" valign="top">
      <strong><a href="https://github.com/Priivacy-ai/spec-kitty">Spec Kitty</a></strong><br />
      <sub>Developer workflow</sub><br /><br />
      Spec-driven development and repeatable worktree workflows for serious projects.<br /><br />
      <a href="https://github.com/Priivacy-ai/spec-kitty">upstream</a> · <a href="https://github.com/uuzzrm/spec-kitty">my fork</a>
    </td>
  </tr>
</table>

## Account star history

One account-level signal: the total stars received by all public repositories over time. It is a trend for the account, not the star count of any single project.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/uuzzrm/uuzzrm/main/assets/account-stars-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/uuzzrm/uuzzrm/main/assets/account-stars-light.svg" />
    <img src="https://raw.githubusercontent.com/uuzzrm/uuzzrm/main/assets/account-stars-light.svg" alt="uuzzrm account repository star history" width="100%" />
  </picture>
</p>

<sub>All public repositories are included · forks contribute only their own stars · refreshed daily by <a href="https://github.com/uuzzrm/uuzzrm/actions/workflows/update-account-stars.yml">GitHub Actions</a>.</sub>

<hr />

<p align="center"><sub>AI agents · retrieval · evaluation · MCP · developer tools · reliable workflows</sub></p>
