<div align="center">
  <img src="https://raw.githubusercontent.com/uuzzrm/uuzzrm/bd5e69a/assets/profile-header.svg" alt="Ruiming Zhao — Prysai AI systems and developer tools" width="100%" />
</div>

<p align="center">
  <a href="https://prysai.com"><strong>Prysai Lab</strong></a>&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/uuzzrm?tab=repositories">Repositories</a>&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/uuzzrm/uuzzrm#core-projects">Core projects</a>
</p>

## About

I build and inspect AI systems that hold up beyond the demo: agents, retrieval, evaluation, and tool use in real developer workflows.

## Current direction

I follow the full agent engineering loop:

- choose the right model and context
- connect tools safely and make behavior observable
- evaluate quality, regressions, and failure modes
- turn useful experiments into repeatable workflows

The goal is simple: fewer impressive demos, more systems that can be tested, understood, and improved.

## Building with Prysai

[Prysai](https://prysai.com) is the home for product experiments and practical work around AI systems and developer tools. The emphasis is on small, testable pieces that can be inspected, measured, and reused.

## Open-source contributions

Six upstream projects, seven merged pull requests — documentation, packaging, compatibility, performance, privacy, and UX fixes that are now part of other projects.

<table>
  <tr>
    <th align="left">Project</th>
    <th align="left">Contribution</th>
    <th align="left">Merged PRs</th>
  </tr>
  <tr>
    <td><a href="https://github.com/MSKazemi/kubeintellect">MSKazemi/kubeintellect</a></td>
    <td>Documented v4 data-handling boundaries and updated the <code>kube-q</code> Homebrew formula with current release resources.</td>
    <td><a href="https://github.com/MSKazemi/kubeintellect/pull/105">#105</a> · <a href="https://github.com/MSKazemi/kubeintellect/pull/111">#111</a></td>
  </tr>
  <tr>
    <td><a href="https://github.com/mastra-ai/mastra">mastra-ai/mastra</a></td>
    <td>Fixed CommonJS schema compatibility by bundling the Zod conversion dependencies and adding regression coverage.</td>
    <td><a href="https://github.com/mastra-ai/mastra/pull/21147">#21147</a></td>
  </tr>
  <tr>
    <td><a href="https://github.com/squid-protocol/gitgalaxy">squid-protocol/gitgalaxy</a></td>
    <td>Replaced manual append loops with <code>extend</code>-based recorder code and resolved the related Ruff performance findings.</td>
    <td><a href="https://github.com/squid-protocol/gitgalaxy/pull/1201">#1201</a></td>
  </tr>
  <tr>
    <td><a href="https://github.com/abenneto/gandharva">abenneto/gandharva</a></td>
    <td>Refined README formatting and section headers.</td>
    <td><a href="https://github.com/abenneto/gandharva/pull/19">#19</a></td>
  </tr>
  <tr>
    <td><a href="https://github.com/seva9523/EvalRepro">seva9523/EvalRepro</a></td>
    <td>Added <code>--no-id-preview</code> to suppress sample ID previews while preserving sample and field digests.</td>
    <td><a href="https://github.com/seva9523/EvalRepro/pull/12">#12</a></td>
  </tr>
  <tr>
    <td><a href="https://github.com/felladrin/MiniSearch">felladrin/MiniSearch</a></td>
    <td>Capped staggered result animations and honored <code>prefers-reduced-motion</code>.</td>
    <td><a href="https://github.com/felladrin/MiniSearch/pull/2324">#2324</a></td>
  </tr>
</table>

<sub>All entries above are public PRs confirmed as merged into their upstream repositories.</sub>

<!--
Maintenance format for future entries:
<tr>
  <td><a href="UPSTREAM_REPOSITORY_URL">owner/repository</a></td>
  <td>One-line description of the merged change.</td>
  <td><a href="MERGED_PR_URL">#123</a></td>
</tr>
Only add a row after the upstream PR shows a merged state.
-->

## Core projects

A compact working set of upstream projects I currently study, use, or contribute to. They are selected for technical leverage, not repository size or star count.

<table>
  <tr>
    <td width="50%" valign="top">
      <strong><a href="https://github.com/thangldw/ragops">RAGOps</a></strong><br />
      <sub>Evaluation infrastructure</sub><br /><br />
      Offline regression tests and explainable release gates for RAG systems and AI agents.<br /><br />
      <a href="https://github.com/thangldw/ragops">upstream</a> · <a href="https://github.com/uuzzrm/ragops">working fork</a>
    </td>
    <td width="50%" valign="top">
      <strong><a href="https://github.com/pydantic/pydantic-ai">PydanticAI</a></strong><br />
      <sub>Typed agent runtime</sub><br /><br />
      Explicit dependencies, tools, structured outputs, and validation for production-minded agents.<br /><br />
      <a href="https://github.com/pydantic/pydantic-ai">upstream</a> · <a href="https://github.com/uuzzrm/pydantic-ai">working fork</a>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <strong><a href="https://github.com/PrefectHQ/fastmcp">FastMCP</a></strong><br />
      <sub>Tool connectivity</sub><br /><br />
      A practical protocol layer for building and connecting MCP servers and clients.<br /><br />
      <a href="https://github.com/PrefectHQ/fastmcp">upstream</a> · <a href="https://github.com/uuzzrm/fastmcp">working fork</a>
    </td>
    <td width="50%" valign="top">
      <strong><a href="https://github.com/promptfoo/promptfoo">Promptfoo</a></strong><br />
      <sub>Quality and safety gates</sub><br /><br />
      Evaluation, comparison, and red-teaming for prompts, agents, and RAG pipelines.<br /><br />
      <a href="https://github.com/promptfoo/promptfoo">upstream</a> · <a href="https://github.com/uuzzrm/promptfoo">working fork</a>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <strong><a href="https://github.com/browser-use/browser-use">Browser Use</a></strong><br />
      <sub>Real-world execution</sub><br /><br />
      Browser control as a practical interface for tool-using agents and workflow automation.<br /><br />
      <a href="https://github.com/browser-use/browser-use">upstream</a> · <a href="https://github.com/uuzzrm/browser-use">working fork</a>
    </td>
    <td width="50%" valign="top">
      <strong><a href="https://github.com/Priivacy-ai/spec-kitty">Spec Kitty</a></strong><br />
      <sub>Developer workflow</sub><br /><br />
      Spec-driven development, worktrees, and repeatable workflows for serious software projects.<br /><br />
      <a href="https://github.com/Priivacy-ai/spec-kitty">upstream</a> · <a href="https://github.com/uuzzrm/spec-kitty">working fork</a>
    </td>
  </tr>
</table>

<sub>These links point to upstream projects and my working forks. They are study and contribution paths, not claims of original ownership.</sub>

## Account star history

This tracks the total stars received by my public repositories over time. It is an account-level view, not the star count of any single project.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/uuzzrm/uuzzrm/main/assets/account-stars-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/uuzzrm/uuzzrm/main/assets/account-stars-light.svg" />
    <img src="https://raw.githubusercontent.com/uuzzrm/uuzzrm/main/assets/account-stars-light.svg" alt="uuzzrm account repository star history" width="100%" />
  </picture>
</p>

<sub>All public repositories · forks count only their own stars · updated daily by <a href="https://github.com/uuzzrm/uuzzrm/actions/workflows/update-account-stars.yml">GitHub Actions</a>.</sub>

## Current interests

`AI Agents` · `RAG` · `LLM Evaluation` · `MCP` · `Developer Tools` · `Codex Workflows`

<hr />

<p align="center"><sub>Building in public, one reliable workflow at a time.</sub></p>
