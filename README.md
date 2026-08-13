<div align="center">
  <img src="https://raw.githubusercontent.com/uuzzrm/uuzzrm/bd5e69a/assets/profile-header.svg" alt="Ruiming Zhao — Prysai AI systems and developer tools" width="100%" />
</div>

<p align="center">
  <a href="https://prysai.com"><strong>Prysai Lab</strong></a>&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="#open-source-contributions">Contributions</a>&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="#core-projects">Core projects</a>&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="#account-star-history">Star history</a>
</p>

## About

I build and inspect AI systems that hold up beyond the demo: agents, retrieval, evaluation, and tool use in real developer workflows.

My background includes six years in network operations and four years as an independent developer, overlapping within the same broader period. This combination informs my current scope across operational continuity, technical implementation, and delivery coordination.

Since 2024, I have also been developing full-quantization training and fine-tuning workflows for image AI models.

<p><sub>AI agents · retrieval · evaluation · developer tools · reliable delivery</sub></p>

## Current direction

I work through the full agent engineering loop: choose the right model and context, connect tools safely, measure quality and failure modes, and turn what works into repeatable workflows.

The standard is simple: fewer impressive demos, more systems that can be tested, understood, and improved.

## Building with Prysai

[Prysai](https://prysai.com) is my studio for product experiments and practical work around AI systems and developer tools—small, testable pieces designed to be inspected, measured, and reused.

## Open-source contributions

A selective record of changes that made it into other people's codebases, docs, and releases. Each entry links directly to the merged work.

<table>
  <tr>
    <th align="left">Proof of work</th>
  </tr>
  <tr>
    <td><sub>AGENT RUNTIME &amp; OPERATIONS</sub><br /><a href="https://github.com/microsoft/agent-framework"><strong>microsoft/agent-framework</strong></a> · <a href="https://github.com/microsoft/agent-framework/pull/7622">PR #7622</a> · <a href="https://github.com/microsoft/agent-framework/pull/7597">#7597</a> · merged<br /><br />Made rejected MCP skill archives visible at the operational warning level and preserved Mistral prompt-cache usage details across regular and streaming responses.</td>
  </tr>
  <tr>
    <td><sub>AGENT INTEGRATION &amp; SAFETY</sub><br /><a href="https://github.com/gnt-ai/gnt"><strong>gnt-ai/gnt</strong></a> · <a href="https://github.com/gnt-ai/gnt/pull/138">PR #138</a> · merged<br /><br />Documented a secure Goose-to-gnt MCP integration, including secret handling, persistent instructions, and human authorization boundaries.</td>
  </tr>
  <tr>
    <td><sub>ROUTING &amp; OBSERVABILITY</sub><br /><a href="https://github.com/vllm-project/semantic-router"><strong>vllm-project/semantic-router</strong></a> · <a href="https://github.com/vllm-project/semantic-router/pull/2874">PR #2874</a> · merged<br /><br />Corrected Router Replay attribution so multi-model Looper executions record the model that produced the final response.</td>
  </tr>
  <tr>
    <td><sub>VOICE AI &amp; CONFIGURATION</sub><br /><a href="https://github.com/livekit/agents"><strong>livekit/agents</strong></a> · <a href="https://github.com/livekit/agents/pull/6810">PR #6810</a> · merged<br /><br />Added explicit Google Speech-to-Text project selection while preserving credential-based discovery for existing callers.</td>
  </tr>
  <tr>
    <td><sub>CONNECTORS &amp; PRODUCT INTEGRATION</sub><br /><a href="https://github.com/oomol-lab/open-connector"><strong>oomol-lab/open-connector</strong></a> · <a href="https://github.com/oomol-lab/open-connector/pull/300">PR #300</a> · merged<br /><br />Expanded the Resend connector from basic sending into batch, scheduling, retrieval, cancellation, and attachment workflows with shared validation and pagination.</td>
  </tr>
  <tr>
    <td><sub>VOICE AI &amp; AUDIO PIPELINES</sub><br /><a href="https://github.com/pipecat-ai/pipecat"><strong>pipecat-ai/pipecat</strong></a> · <a href="https://github.com/pipecat-ai/pipecat/pull/5298">PR #5298</a> · merged<br /><br />Made AssemblyAI speech recognition inherit the pipeline input sample rate unless callers provide an explicit override.</td>
  </tr>
  <tr>
    <td><sub>EVALUATION &amp; OBSERVABILITY</sub><br /><a href="https://github.com/thangldw/ragops"><strong>thangldw/ragops</strong></a> · <a href="https://github.com/thangldw/ragops/pull/30">PR #30</a> · merged<br /><br />Added an offline Phoenix recorded-score adapter with deterministic case-ID joins, synthetic fixtures, documentation, and tests.</td>
  </tr>
  <tr>
    <td><sub>AGENT TOOLING &amp; COMPATIBILITY</sub><br /><a href="https://github.com/ag2ai/ag2"><strong>ag2ai/ag2</strong></a> · <a href="https://github.com/ag2ai/ag2/pull/3148">PR #3148</a> · merged<br /><br />Added HEIC and HEIF MIME types to the Gemini image-input type path and covered the public factory with regression tests.</td>
  </tr>
  <tr>
    <td><sub>AGENT TOOLING &amp; COMPATIBILITY</sub><br /><a href="https://github.com/mlflow/mlflow"><strong>mlflow/mlflow</strong></a> · <a href="https://github.com/mlflow/mlflow/pull/25010">PR #25010</a> · <a href="https://github.com/mlflow/mlflow/pull/25000">#25000</a> · merged<br /><br />Preserved provider-specific usage metadata across Gemini, Anthropic, and OpenAI-compatible gateway adapters, with regression coverage for normalized and nested usage details.</td>
  </tr>
  <tr>
    <td><sub>AGENT TOOLING &amp; DOCUMENTATION</sub><br /><a href="https://github.com/jupyterlab/jupyter-ai"><strong>jupyterlab/jupyter-ai</strong></a> · <a href="https://github.com/jupyterlab/jupyter-ai/pull/1639">PR #1639</a> · merged<br /><br />Added a concise interaction model explaining how chat, personas, ACP agents, model providers, and MCP tools fit together.</td>
  </tr>
  <tr>
    <td><sub>PACKAGING &amp; OPERATIONS</sub><br /><a href="https://github.com/MSKazemi/kubeintellect"><strong>MSKazemi/kubeintellect</strong></a> · <a href="https://github.com/MSKazemi/kubeintellect/pull/111">PR #111</a> · <a href="https://github.com/MSKazemi/kubeintellect/pull/105">#105</a> · merged<br /><br />Updated the <code>kube-q</code> Homebrew formula with current release resources and documented v4 data-handling boundaries.</td>
  </tr>
  <tr>
    <td><sub>PERFORMANCE &amp; DELIVERY</sub><br /><a href="https://github.com/squid-protocol/gitgalaxy"><strong>squid-protocol/gitgalaxy</strong></a> · <a href="https://github.com/squid-protocol/gitgalaxy/pull/1201">PR #1201</a> · merged<br /><br />Replaced manual append loops with <code>extend</code>-based recorder code and resolved the related Ruff performance findings.</td>
  </tr>
  <tr>
    <td><sub>AGENT TOOLING &amp; COMPATIBILITY</sub><br /><a href="https://github.com/mastra-ai/mastra"><strong>mastra-ai/mastra</strong></a> · <a href="https://github.com/mastra-ai/mastra/pull/21281">PR #21281</a> · <a href="https://github.com/mastra-ai/mastra/pull/21147">#21147</a> · merged<br /><br />Resolved dynamic models once per assigned-tool batch and fixed CommonJS schema compatibility by bundling the Zod conversion dependencies.</td>
  </tr>
  <tr>
    <td><sub>RELIABILITY &amp; EXPERIENCE</sub><br /><a href="https://github.com/felladrin/MiniSearch"><strong>felladrin/MiniSearch</strong></a> · <a href="https://github.com/felladrin/MiniSearch/pull/2339">PR #2339</a> · <a href="https://github.com/felladrin/MiniSearch/pull/2324">#2324</a> · merged<br /><br />Made pre-stream inference failures return the intended 503 response, capped staggered result animations, and honored <code>prefers-reduced-motion</code>.</td>
  </tr>
  <tr>
    <td><sub>PRIVACY &amp; EVALUATION</sub><br /><a href="https://github.com/seva9523/EvalRepro"><strong>seva9523/EvalRepro</strong></a> · <a href="https://github.com/seva9523/EvalRepro/pull/12">PR #12</a> · merged<br /><br />Added <code>--no-id_preview</code> to suppress sample ID previews while preserving sample and field digests.</td>
  </tr>
  <tr>
    <td><sub>DOCUMENTATION &amp; DEVELOPER EXPERIENCE</sub><br /><a href="https://github.com/abenneto/gandharva"><strong>abenneto/gandharva</strong></a> · <a href="https://github.com/abenneto/gandharva/pull/19">PR #19</a> · merged<br /><br />Refined README formatting and section headers.</td>
  </tr>
</table>

<sub>Every entry above links to a public pull request confirmed as merged into its upstream repository.</sub>

<!--
Maintenance format for future entries:
1. Confirm the upstream pull request has a non-empty merged_at value.
2. Group multiple merged PRs under the same upstream project.
3. Keep every merged PR linked and update the summary sentence when the totals change.
Only add an entry after the upstream PR is actually merged.
-->

## Core projects

A focused working set of upstream projects I study, use, or contribute to. The selection is about technical leverage, not repository size.

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

<sub>These links point to upstream projects and my forks. They are study and contribution paths, not claims of original ownership.</sub>

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

## Current interests

<p><code>AI agents</code> · <code>RAG</code> · <code>LLM evaluation</code> · <code>MCP</code> · <code>developer tools</code> · <code>Codex workflows</code></p>

<hr />

<p align="center"><sub>Building in public, one reliable workflow at a time.</sub></p>
