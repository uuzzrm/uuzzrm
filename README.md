<div align="center">
  <img src="https://raw.githubusercontent.com/uuzzrm/uuzzrm/bd5e69a/assets/profile-header.svg" alt="Ruiming Zhao — Prysai AI systems and developer tools" width="100%" />
</div>

<p align="center">
  <a href="https://prysai.com"><strong>Prysai Lab</strong></a>&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="#open-source-contributions">Contributions</a>&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="#core-projects">Core projects</a>&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="#account-star-history">Star history</a>
</p>

<table align="center">
  <tr>
    <td align="center" width="50%"><strong>11</strong><br /><sub>merged pull requests</sub></td>
    <td align="center" width="50%"><strong>10</strong><br /><sub>upstream projects</sub></td>
  </tr>
</table>

## About

I build and inspect AI systems that hold up beyond the demo: agents, retrieval, evaluation, and tool use in real developer workflows.

<p><sub>AI agents · retrieval · evaluation · developer tools · reliable delivery</sub></p>

## Current direction

I work through the full agent engineering loop: choose the right model and context, connect tools safely, measure quality and failure modes, and turn what works into repeatable workflows.

The standard is simple: fewer impressive demos, more systems that can be tested, understood, and improved.

## Building with Prysai

[Prysai](https://prysai.com) is my studio for product experiments and practical work around AI systems and developer tools—small, testable pieces designed to be inspected, measured, and reused.

## Open-source contributions

Ten upstream projects, eleven merged pull requests. The work spans evaluation, AI tooling, compatibility, packaging, performance, privacy, and UX.

<table>
  <tr>
    <th align="left">Upstream project</th>
    <th align="left">What shipped</th>
  </tr>
  <tr>
    <td valign="top"><a href="https://github.com/thangldw/ragops">thangldw/ragops</a><br /><sub><a href="https://github.com/thangldw/ragops/pull/30">PR #30 · merged</a></sub></td>
    <td>Added an offline Phoenix recorded-score adapter with deterministic case-ID joins, synthetic fixtures, documentation, and tests.</td>
  </tr>
  <tr>
    <td valign="top"><a href="https://github.com/ag2ai/ag2">ag2ai/ag2</a><br /><sub><a href="https://github.com/ag2ai/ag2/pull/3148">PR #3148 · merged</a></sub></td>
    <td>Added HEIC and HEIF MIME types to the Gemini image-input type path and covered the public factory with regression tests.</td>
  </tr>
  <tr>
    <td valign="top"><a href="https://github.com/mlflow/mlflow">mlflow/mlflow</a><br /><sub><a href="https://github.com/mlflow/mlflow/pull/25000">PR #25000 · merged</a></sub></td>
    <td>Preserved provider-specific usage metadata in the OpenAI-compatible gateway, with regression coverage for nested usage details.</td>
  </tr>
  <tr>
    <td valign="top"><a href="https://github.com/jupyterlab/jupyter-ai">jupyterlab/jupyter-ai</a><br /><sub><a href="https://github.com/jupyterlab/jupyter-ai/pull/1639">PR #1639 · merged</a></sub></td>
    <td>Added a concise interaction model explaining how chat, personas, ACP agents, model providers, and MCP tools fit together.</td>
  </tr>
  <tr>
    <td valign="top"><a href="https://github.com/MSKazemi/kubeintellect">MSKazemi/kubeintellect</a><br /><sub><a href="https://github.com/MSKazemi/kubeintellect/pull/111">PR #111 · merged</a> · <a href="https://github.com/MSKazemi/kubeintellect/pull/105">#105 · merged</a></sub></td>
    <td>Updated the <code>kube-q</code> Homebrew formula with current release resources and documented v4 data-handling boundaries.</td>
  </tr>
  <tr>
    <td valign="top"><a href="https://github.com/squid-protocol/gitgalaxy">squid-protocol/gitgalaxy</a><br /><sub><a href="https://github.com/squid-protocol/gitgalaxy/pull/1201">PR #1201 · merged</a></sub></td>
    <td>Replaced manual append loops with <code>extend</code>-based recorder code and resolved the related Ruff performance findings.</td>
  </tr>
  <tr>
    <td valign="top"><a href="https://github.com/mastra-ai/mastra">mastra-ai/mastra</a><br /><sub><a href="https://github.com/mastra-ai/mastra/pull/21147">PR #21147 · merged</a></sub></td>
    <td>Fixed CommonJS schema compatibility by bundling the Zod conversion dependencies and adding regression coverage.</td>
  </tr>
  <tr>
    <td valign="top"><a href="https://github.com/felladrin/MiniSearch">felladrin/MiniSearch</a><br /><sub><a href="https://github.com/felladrin/MiniSearch/pull/2324">PR #2324 · merged</a></sub></td>
    <td>Capped staggered result animations and honored <code>prefers-reduced-motion</code>.</td>
  </tr>
  <tr>
    <td valign="top"><a href="https://github.com/seva9523/EvalRepro">seva9523/EvalRepro</a><br /><sub><a href="https://github.com/seva9523/EvalRepro/pull/12">PR #12 · merged</a></sub></td>
    <td>Added <code>--no-id_preview</code> to suppress sample ID previews while preserving sample and field digests.</td>
  </tr>
  <tr>
    <td valign="top"><a href="https://github.com/abenneto/gandharva">abenneto/gandharva</a><br /><sub><a href="https://github.com/abenneto/gandharva/pull/19">PR #19 · merged</a></sub></td>
    <td>Refined README formatting and section headers.</td>
  </tr>
</table>

<sub>Every entry above links to a public pull request confirmed as merged into its upstream repository.</sub>

<!--
Maintenance format for future entries:
1. Confirm the upstream pull request has a non-empty merged_at value.
2. Group multiple merged PRs under the same upstream project.
3. Update the two contribution counts above and keep each PR linked.
Only add a row after the upstream PR is actually merged.
-->

## Core projects

A focused working set of upstream projects I study, use, or contribute to. The selection is about technical leverage, not repository size.

<table>
  <tr>
    <td width="50%" valign="top">
      <strong><a href="https://github.com/thangldw/ragops">RAGOps</a></strong><br />
      <sub>Evaluation infrastructure</sub><br /><br />
      Offline evaluation and explainable release gates for RAG systems and agents.<br /><br />
      <a href="https://github.com/thangldw/ragops">upstream</a> · <a href="https://github.com/uuzzrm/ragops">working fork</a>
    </td>
    <td width="50%" valign="top">
      <strong><a href="https://github.com/pydantic/pydantic-ai">PydanticAI</a></strong><br />
      <sub>Typed agent runtime</sub><br /><br />
      Typed tools, structured outputs, and validation for production-minded agents.<br /><br />
      <a href="https://github.com/pydantic/pydantic-ai">upstream</a> · <a href="https://github.com/uuzzrm/pydantic-ai">working fork</a>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <strong><a href="https://github.com/PrefectHQ/fastmcp">FastMCP</a></strong><br />
      <sub>Tool connectivity</sub><br /><br />
      Protocol infrastructure for connecting MCP servers and clients.<br /><br />
      <a href="https://github.com/PrefectHQ/fastmcp">upstream</a> · <a href="https://github.com/uuzzrm/fastmcp">working fork</a>
    </td>
    <td width="50%" valign="top">
      <strong><a href="https://github.com/promptfoo/promptfoo">Promptfoo</a></strong><br />
      <sub>Quality and safety gates</sub><br /><br />
      Evaluation and red-teaming for prompts, agents, and RAG pipelines.<br /><br />
      <a href="https://github.com/promptfoo/promptfoo">upstream</a> · <a href="https://github.com/uuzzrm/promptfoo">working fork</a>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <strong><a href="https://github.com/browser-use/browser-use">Browser Use</a></strong><br />
      <sub>Real-world execution</sub><br /><br />
      Browser control for tool-using agents and workflow automation.<br /><br />
      <a href="https://github.com/browser-use/browser-use">upstream</a> · <a href="https://github.com/uuzzrm/browser-use">working fork</a>
    </td>
    <td width="50%" valign="top">
      <strong><a href="https://github.com/Priivacy-ai/spec-kitty">Spec Kitty</a></strong><br />
      <sub>Developer workflow</sub><br /><br />
      Spec-driven development and repeatable worktree workflows for serious projects.<br /><br />
      <a href="https://github.com/Priivacy-ai/spec-kitty">upstream</a> · <a href="https://github.com/uuzzrm/spec-kitty">working fork</a>
    </td>
  </tr>
</table>

<sub>These links point to upstream projects and working forks. They are study and contribution paths, not claims of original ownership.</sub>

## Account star history

One account-level signal: the total stars received by all public repositories over time. It is a trend for the account, not the star count of any single project.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/uuzzrm/uuzzrm/main/assets/account-stars-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/uuzzrm/uuzzrm/main/assets/account-stars-light.svg" />
    <img src="https://raw.githubusercontent.com/uuzzrm/uuzzrm/main/assets/account-stars-light.svg" alt="uuzzrm account repository star history" width="100%" />
  </picture>
</p>

<sub>All public repositories are included · forks contribute only their own stars · updated daily by <a href="https://github.com/uuzzrm/uuzzrm/actions/workflows/update-account-stars.yml">GitHub Actions</a>.</sub>

## Current interests

<p><code>AI agents</code> · <code>RAG</code> · <code>LLM evaluation</code> · <code>MCP</code> · <code>developer tools</code> · <code>Codex workflows</code></p>

<hr />

<p align="center"><sub>Building in public, one reliable workflow at a time.</sub></p>
