# Reporting contracts

What to ask an agent to send back, so the next decision needs no archaeology, and the honesty rules for reports.

## Contents
- Principles
- Implementation report
- Audit report
- Release report
- Design and motion reports
- Status vocabulary
- Wording block

## Principles

- Request only evidence that helps continuation. Lead with machine-checkable facts (branch, SHA, PR, CI), then decisions, then gaps.
- Size the contract to the risk: two lines for a small fix, the full list for a feature program or a release.
- No celebratory summaries, and no recap of the prompt.
- Never claim "fully verified" while physical, real-host, device, or manual validation is outstanding.
- Ask for decisions and evidence, not a narration of reasoning.

## Implementation report

Ask for the fields that apply:
- starting and base SHA; branch; resulting HEAD
- commits or checkpoints, one line each
- PR link or number and its state
- files and subsystems changed
- major architecture decisions, and any departure from a hypothesis in the prompt
- migrations (data, config, public contract)
- security and privacy properties, with the fixtures that prove them
- compatibility impact (shells, platforms, versions)
- tests run and results; CI status at the exact SHA
- packaging or install validation, when packaging changed
- physical QA actually performed; physical QA still required (the exact list)
- known limitations
- intentionally deferred scope
- genuine blockers
- the exact next action

## Audit report

The findings format is in [audit-and-review.md](audit-and-review.md). Add: the commit range reviewed, what was run and where, proof that the repository was left unchanged, and what could not be verified.

## Release report

- release commit SHA, tag, release URL
- assets with names and computed checksums
- CI status at the exact SHA
- install validation: environment, command, observed version and behavior
- package-manager PRs opened (links) and their state
- actions deliberately not taken
- anything that differed from the verified facts

## Design and motion reports

- Design: what was built and where; the viewports and states checked, with screenshots; accessibility and performance results as automation evidence; decisions and departures from the brief; the human visual-check list.
- Motion: master and per-format renders; contact sheet and keyframes; the critique record with scores and the worst moments fixed; captures used with the product commit each came from; audio provenance; creative departures from the brief; leak-scan results; the reproduction command for the render.

## Status vocabulary

Require one of these for each check:
- **verified** (how: test name, command, host)
- **reported only** (stated by someone else, not re-checked)
- **not run** (why)
- **requires human** (exact steps)

## Wording block

> Finish with a short report: base and head SHA, branch, PR, commits, what changed and the decisions you made (with departures from any hypothesis), tests and CI at the exact SHA, what you verified physically and what still needs a human (exact steps), known limitations, deferred scope, blockers, and the exact next action. Distinguish verified from reported-only. No summary of the task and no celebration.
