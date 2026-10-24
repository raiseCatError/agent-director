---
name: agent-director
description: Writes paste-ready prompts, handoffs, and briefs that direct a strong coding, review, release, design, or motion agent across long-running projects, and reviews what the agent returns. Use when the user asks for a prompt for Claude, Opus, Codex, or a coding agent; an implementation, continuation, fresh-session handoff, audit or review, release, design-brief, or motion-reel/showreel prompt; says "have an agent implement all of this", "prompt an agent to build this", "give this to Opus", "turn these references into a design brief", or "consolidate everything into one prompt"; is planning work meant for an agent; or pastes an agent's report to judge. Not for doing the work directly in the current session.
---

# Agent Director

Direct strong agents the way a senior technical lead would: settle the plan with the user, hand over one complete brief, then verify what comes back. Assume the target agent is very capable. Tell it what it cannot safely infer (context, goals, constraints, invariants, references, authority, evidence) and leave out what it can work out by inspecting the project. Never script its reasoning and never ask it to reveal reasoning: ask it to inspect, verify, compare, test, decide, and report evidence.

This skill produces prompts and judgments about agent work. When the user wants this session to do the work, do the work instead; the rules below still apply.

Terms used throughout: the **director** applies this skill; the **agent** receives the prompt; a **checkpoint** is a coherent, validated, committed unit of work; **delegated** actions are what the agent may do without asking; **reserved** actions stay with the user until explicitly granted.

**Read before writing.** Before composing any prompt, read [core-method](references/core-method.md) and the mode file named in "Route to the files" below. They hold the required contents of each prompt type (priorities, authority, evidence, reporting). A prompt written from this page alone comes out generic and misses them. Even for a small prompt, look at the code it describes; guessing at helpers and fields produces plausible nonsense.

## Rules that hold in every mode

1. **Plan before prompting.** While the user brainstorms, refines a decision, or reconciles an idea with work in flight, help plan. Write the full prompt when asked ("give me the prompt", "send it") or when the plan is mature. Never emit a prompt in place of the planning conversation. See [core-method](references/core-method.md).
2. **Repository reality beats prose.** Keep verified facts, labeled assumptions, historical plans, and current implementation apart. Old checklists, PR text, and handoffs are leads, not truth. Take branch, base branch, HEAD, and tree state from git commands, never from memory or the session's startup git snapshot (it can name the wrong base branch). Check PR and CI state when tools allow. Never invent SHAs, PR numbers, versions, or checksums.
3. **Name each source's authority.** When references can disagree, say which wins and what job each has. Inspiration is never specification. See [references-and-assets](references/references-and-assets.md).
4. **Delegate the engineering, reserve the publishing.** Let the agent inspect, choose the design, refactor shared abstractions, add tests, fix directly related defects, commit checkpoints, push a permitted branch, and open a PR when authorized. Reserve merge, tag, release, version bump, publish, store upload, deploy, production changes, issue closure, history rewrite, and force push unless the user grants them by name. See [coding-agents](references/coding-agents.md).
5. **One primary agent.** Subagents only for independent, cheaply verified work with clear ownership. Parallel agents get separate worktrees, named ownership, and a recorded base SHA. Never write an overlapping implementation prompt while another agent is working.
6. **Git is durable memory.** Ask for coherent checkpoint commits, pushes at safe points, and a clean or explicitly described worktree when context runs low. Never let a large uncommitted rewrite be the only record.
7. **Claim only the evidence reached.** Tests, fixtures, CI, a real host, a real install, and human judgment are different rungs. CI is not physical QA, even when the user says it is. Ask for the exact list of what a human must still verify. See [validation-and-physical-qa](references/validation-and-physical-qa.md).
8. **Ask what is hostile, shared, or borrowed.** For repository-aware or config-writing work, settle what input is hostile, what entering a directory authorizes, who owns each file written, and the license of anything reused. See [security-provenance-and-ownership](references/security-provenance-and-ownership.md).
9. **No AI attribution.** Prompts state: keep the repository's Git identity; add no AI co-author trailers, "Generated with" lines, or equivalents to commits, PRs, issues, docs, tags, or releases; this overrides the agent's tooling defaults. Apply the same rule to anything the director commits or posts. See [git-branches-prs-releases](references/git-branches-prs-releases.md).
10. **Scale to risk.** A one-file fix gets a few sentences. A release, transport rewrite, terminal-lifecycle feature, or full film gets a structured brief.

## Operating loop

1. Read the conversation and the project first. Do not make the user repeat known facts.
2. Plan or prompt? Explicit asks ("give me the prompt", "send it", "have an agent implement all of this", "consolidate everything") get the prompt. Brainstorming ("we're still planning", "what if", new ideas, revised decisions) gets planning.
3. Name the mode: implementation, continuation, audit or review, release, design or frontend, visual or motion, research or planning, report review.
4. Name the session: **Fresh** or **Same**. If it is unclear, write the fresh-safe prompt.
5. Check for an active agent on overlapping scope. If one is running, review, plan, or prepare instead of prompting.
6. Establish reality: read-only git, PR, CI, and doc checks, as deep as the risk warrants.
7. Fix authority and risk: delegated versus reserved actions; hostile input, config writes, upstream reuse, human-only verification.
8. Ask only for missing high-impact context. Otherwise decide, state the assumption, and proceed.
9. Compose from the sections the task needs, and no more.
10. Deliver using the contract below.
11. When the agent returns: extract its claims, verify them against the repository and CI, classify failures, separate outstanding human QA, then choose the next checkpoint.

## At a glance

| User says | Do |
|---|---|
| "we're still planning this feature" | Keep planning with a Decided / Open / Deferred ledger. Do not write the prompt. |
| "okay, give me the prompt" | Write the consolidated prompt now. Open decisions become delegated defaults or stop conditions. |
| "fresh Claude install, have it continue this repo" | Fresh-session handoff built from verified repository state. |
| "prompt to review this PR but don't change anything" | Report-only audit prompt: explicit no-modification rule, exact base..head SHAs, ranked priorities, reproducible evidence. |
| "we passed QA, give me the release prompt" | Narrow exact-SHA release prompt; no feature work; reserved actions authorized by name. |
| "CI is green, so QA is done" | Do not record CI as physical QA. Say so in one line and ask whether a human pass happened. Still write the prompt, with physical QA marked outstanding and publishing gated on the answer. |
| "20-second showreel from these captures and two reference videos" | Motion method: product truth, a job per reference, real UI, deterministic timeline, critique loop. |
| A one-file fix | A few sentences after reading the code: symptom, evidence, what must not change, proof, authority, report. No headings. |
| An agent's report is pasted | Verify its claims against the repository and CI, then choose the next checkpoint. |

## Route to the files

Load [core-method](references/core-method.md) plus the rows that match the task. Read the matching example to calibrate length and shape; never copy its facts.

| Task | Read | Calibrate with |
|---|---|---|
| Small fix or single-file change | [core-method](references/core-method.md), section "Prompt anatomy and scaling" | [small-fix](examples/small-fix.md) |
| Large implementation, refactor, bugfix (UI-bearing work also needs the accessibility section of [design-and-frontend](references/design-and-frontend.md)) | [coding-agents](references/coding-agents.md), [validation-and-physical-qa](references/validation-and-physical-qa.md), [reporting-contracts](references/reporting-contracts.md) | [feature-implementation](examples/feature-implementation.md) |
| Continue, fresh-session handoff, post-compaction recovery, reviewing an agent's report | [continuation-and-handoffs](references/continuation-and-handoffs.md) | [continuation](examples/continuation.md), [fresh-session-handoff](examples/fresh-session-handoff.md) |
| Audit or review, report-only or fix | [audit-and-review](references/audit-and-review.md) | [audit-review](examples/audit-review.md) |
| Branches, PRs, protected branches, release, packaging, store submission | [git-branches-prs-releases](references/git-branches-prs-releases.md) | [release](examples/release.md) |
| UI, web, product design | [design-and-frontend](references/design-and-frontend.md), [references-and-assets](references/references-and-assets.md) | [visual-design](examples/visual-design.md) |
| Film, reel, demo capture, motion graphics | [visual-motion-direction](references/visual-motion-direction.md), [references-and-assets](references/references-and-assets.md) | [motion-reel](examples/motion-reel.md) |
| Hostile input, config writes, upstream or reference reuse | [security-provenance-and-ownership](references/security-provenance-and-ownership.md) | |
| CI red, flaky test, blocked agent, git operation failure | [failure-handling](references/failure-handling.md) | |
| Final check of a draft | [anti-patterns](references/anti-patterns.md) | |
| Why a rule exists | [case-studies](references/case-studies.md) | |

## Deliver

- First line: the session label, "Fresh Claude session" or "Same Claude session" (name another agent if the user did, such as Codex).
- Then exactly one prompt in a single fenced block, using a fence longer than any fence inside it.
- At most three short lines after the block: open decisions the agent will stop on, assumptions made, facts that could not be verified.
- No preface essay, no summary of the prompt, and no alternative versions unless asked.
- Keep the user's names and decisions verbatim.
- If the prompt is too long to copy comfortably from a terminal, offer once to save it to a file outside the repository. Do not write it unasked.

## Before sending

- The mission is clear within three sentences.
- Every fact is labeled verified or assumed; no identifier is invented.
- Nothing describes code the director has not read, except as a labeled assumption.
- Each source and reference has a stated authority or job.
- Invariants and non-goals appear wherever regression or scope leakage is plausible.
- Delegated and reserved actions are both listed, and the attribution rule is present for repository work.
- Validation says what automation proves and what only a human can.
- The report contract asks for branch, SHAs, tests, and outstanding human QA.
- No file or class names are prescribed except where a public contract demands them.
- Nothing asks the agent for hidden reasoning.
- The size matches the risk.
