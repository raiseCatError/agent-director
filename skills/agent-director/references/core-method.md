# Core method

How a conversation becomes a prompt an agent can act on, and what that prompt must contain. Read this before composing, or deciding not to compose, any prompt.

## Contents
- The planning-first loop
- Plan or prompt: reading the moment
- Active-agent check
- Reality pre-flight
- Source of truth and precedence
- Prompt anatomy and scaling
- Exhaustive about what, silent about how
- Scope, non-goals, and ambiguity
- Style of the prompt itself

## The planning-first loop

The user works in a loop. Stay in step with it instead of jumping ahead.

1. Discuss and collect ideas.
2. Refine ambiguous product decisions.
3. Reconcile new ideas with the existing architecture and with work already in flight.
4. Consolidate the requirements.
5. Produce one large implementation prompt, only when the user asks for it or the plan is mature.
6. Review the agent's report.
7. Verify the repository and CI facts the report claims, wherever tools permit.
8. Decide the next checkpoint.

Jumping from step 1 to step 5 yields a confident prompt for the wrong thing. Skipping steps 6 and 7 turns a prompt into a hope. Each pass ends in a decision, never in another prompt by reflex.

## Plan or prompt: reading the moment

| Signal | Do |
|---|---|
| "give me the prompt", "send it", "make the Claude prompt", "write the implementation prompt", "have an agent implement all of this", "consolidate everything we discussed", "give this to Opus" | Write the consolidated prompt now. |
| "we're still planning", "I'm thinking...", "what if...", "should we...", new ideas arriving, earlier decisions being revised | Keep planning (below). |
| A prompt is wanted and the context is nearly empty | Ask at most three questions that would materially change the prompt, then write it. |
| A prompt is wanted while an earlier agent still works on overlapping scope | Run the active-agent check first. |
| The user pastes an agent's report | Review it: [continuation-and-handoffs.md](continuation-and-handoffs.md), section "Reviewing a returned report". |

**Planning mode.** Act as a technical and product partner.
- Keep a short running ledger in the chat (Decided, Open, Deferred, Rejected) and update it when it changes. Keep it in the conversation, not in a file.
- Test each new idea against the code and docs where tools permit: does it already exist in some form, does it contradict an accepted decision, does it belong in the current checkpoint or a later one?
- For each open decision, recommend a default with a one-line reason. Ask only about forks that change product identity, scope, a public contract, or reserved authority.
- Say when the plan looks mature and what would still weaken the prompt, in one or two sentences. Do not push the user toward the prompt.

**Prompt requested with decisions still open.** Write the prompt. Carry each open decision as an instruction: delegated with a default ("choose X unless inspection shows Y; report the choice") or a stop condition ("on reaching Z, stop at a safe checkpoint and report"). Ask first only when a single product decision forks the architecture and has no safe default.

**Readiness check**, for deciding whether to offer a prompt unprompted: outcome observable; product decisions closed or delegated with defaults; relationship to the current branch and in-flight work known; non-goals named; authority settled; validation and physical-QA boundary known.

## Active-agent check

Before an implementation or fix-forward prompt, establish whether another agent is working on overlapping scope. Signals: the user says so; the target checkout holds uncommitted changes the director did not make; the branch or PR changed minutes ago; worktrees exist for the same area.

When one is active:
- Do not write an overlapping prompt. Offer work that does not collide: review interim state, plan the next slice, draft the QA or release checklist, or prepare a prompt that runs in a separate worktree on disjoint scope.
- If the user wants parallel work anyway, apply [coding-agents.md](coding-agents.md), section "Parallel agents and worktrees".
- If it is unclear, ask one question: "Is another agent still working on this branch?"

Treat uncommitted changes the director did not make as someone else's work: read them, and never edit, stash, or switch branches around them.

## Reality pre-flight

With repository access, inspect before writing. Without it, say which facts are unverified and never invent identifiers (SHAs, PR numbers, versions, checksums). Match depth to risk: a one-file fix needs `git status` and a look at the file; a large implementation or release needs the full list.

Typical read-only checks:
- working tree: `git status --short --branch`, untracked and dirty files, who owns them
- branch, upstream tracking, base branch and base SHA, HEAD SHA; confirm the base branch with `git branch -a` and the merge history, because the session's startup git snapshot can guess wrong (naming `main` when only `master` exists, for instance)
- recent relevant commits and the merge history of the base branch
- `git worktree list`, and other branches touching the same area
- open PRs and stacks (`gh pr list`, `gh pr view`); CI status at the exact SHA (`gh pr checks`, `gh run list`)
- package, version, changelog, and tag state
- the current implementation of anything the plan calls "missing" (read or grep before asserting absence)
- tracker claims compared with the code

Keep four kinds of statement apart in the prompt:
1. **Repository facts**: checked, with when or how.
2. **Prompt assumptions**: marked "Assumed:" so the agent verifies them.
3. **Historical plans**: labeled as history, never as authority.
4. **Current implementation**: authoritative for behavior.

Old issue checkboxes, old PR descriptions, and older handoffs are leads, not truth. Current implementation plus the accepted current architecture normally beats stale planning prose. Do not ask the agent to rebuild something that already ships because a tracker is stale: look first, and tell the agent to look first.

Put a "Verified at prompt time" block in the prompt and tell the agent to re-verify at the start, because the repository can move. Include the conflict rule: if the repository contradicts the prompt, trust the repository and report the discrepancy; if the discrepancy changes scope or authority, stop and report before acting.

## Source of truth and precedence

When sources can disagree, say which wins in this task. The agent will not guess the order. Typical precedences:
- the user's latest explicit decision > earlier discussion
- current accepted architecture > abandoned proposal
- current code > stale issue checklist or old PR description
- official SDK or spec > third-party article
- real product behavior > marketing copy
- accepted design decision > generic upstream convention
- exact current branch > old handoff branch

A project may designate its own authority (tracker acceptance criteria, an agent protocol document, an architecture file). Honor it and name it. Reference types and authority labels: [references-and-assets.md](references-and-assets.md). Never silently promote inspiration to specification.

## Prompt anatomy and scaling

Compose from the sections the task needs. Include a section when its "include when" holds; omit it otherwise.

| Section | Include when |
|---|---|
| Session label and mission | always |
| Current state (verified facts) | the task touches a repository |
| Product identity | the agent could "improve" the product into something else; large tasks |
| Source of truth | several documents or references can disagree, or stale artifacts exist |
| Relevant history | past decisions or incidents the agent cannot see |
| Desired outcome | always; observable and testable |
| Scope and non-goals | scope leakage is plausible |
| Invariants | something must not regress; product, security, or protocol identity |
| References and how to read them | any reference is supplied |
| Security and privacy | hostile input, secrets, personal data |
| Compatibility and accessibility | UI work (terminal UIs included) or several platforms; see [design-and-frontend.md](design-and-frontend.md), section "Accessibility and fallbacks" |
| Git and worktree authority | commits, branches, or PRs are involved |
| Autonomy boundary | implementation: delegated and reserved actions |
| Validation | implementation, always |
| Physical-QA boundary | behavior automation cannot prove |
| Failure handling | CI, flaky, or platform risk; long runs |
| Long-horizon behavior | likely to outlast one context or usage window |
| Report contract | always; sized to risk |

Scale to risk:
- **Small** (one-file fix, doc tweak, one failing test): one to three short paragraphs. Symptom with evidence, outcome, any invariant worth stating, how to validate, a two-line report. No headings. Read the code first and describe only what you saw; label anything else as an assumption. Example: [../examples/small-fix.md](../examples/small-fix.md).
- **Standard** (bounded feature, multi-file bugfix): headed sections for mission, state, outcome, invariants, non-goals, authority, validation, report; roughly 25 to 60 lines.
- **Large or high-risk** (new subsystem, transport or protocol rewrite, terminal lifecycle, security-sensitive parser, release, full film): the menu as needed; roughly 100 to 300 lines.

Length is earned by what the agent cannot infer and by what a mistake costs. A longer prompt for the same risk is padding.

## Exhaustive about what, silent about how

The agent can read the code. It cannot read the user's mind, other conversations, or the consequences of a mistake.

**State what the agent cannot safely infer:** why the work matters and the product identity; decisions made elsewhere; taste; where scope ends; what must not change; what authority it holds and lacks; who else is active; which documents are authoritative; what "done" means to the user; which checks only a human can perform; incidents that taught the team a rule.

**Leave to the agent:** file, type, and function names; module boundaries; algorithms; test layout; internal ordering; local refactors.

**Name exact details only when** a public contract, accepted architecture, security boundary, migration rule, user-visible vocabulary, or integration point (branch or PR name) requires them.

Treat an architecture suggestion as a hypothesis unless it is already accepted. Label it ("Hypothesis, not required: ...") and ask the agent to report any departure.

Prefer an outcome with invariants over a build order:

> Weak: "Create `ContextCache` in `src/context/cache.ts` with get, set, and evict, and call it from `Engine.run()`."
>
> Strong: "Facts gathered for a workspace must not be recomputed on every keystroke, and a stale fact must never outlive a workspace change that invalidates it. Inspect the current engine, choose the design, and prove invalidation with tests, including a workspace that changes while a probe is running."

When the target is clearly less capable than a frontier model, add explicit ordering only for fragile operations and keep the rest outcome-based.

Do not ask for hidden reasoning. Ask the agent to inspect, verify, compare, test, and decide, then report the decision and the evidence. "Think step by step", "show your chain of thought", and "narrate your reasoning" add length without evidence, and continuation needs decisions, not narration.

## Scope, non-goals, and ambiguity

- Name the neighboring work that must not enter, wherever leakage is plausible: deferred backlog, adjacent features, tempting refactors, renames, dependency swaps.
- Do not write "while you're here". Related fixes are welcome only under the conditions in [coding-agents.md](coding-agents.md), section "Extra work".
- On ambiguity: inspect existing behavior and docs first; infer from established patterns when the risk is low; choose among reasonable engineering approaches and proceed; ask only when a genuine product decision cannot be derived safely. Do not invent business or product intent, and do not stop repeatedly over trivial preferences.

## Style of the prompt itself

- Open with the mission in one to three sentences.
- State facts as facts with provenance; mark assumptions.
- Use plain headings in large prompts and short paragraphs in small ones.
- Phrase invariants as properties that hold ("the real shell remains authoritative"), then add prohibitions for hard boundaries.
- Reserve emphatic language for real boundaries (authority, security, attribution) and give the reason in a clause.
- Use the user's vocabulary and carry their decisions verbatim. Do not rename product concepts.
- Skip persona filler ("you are a world-class engineer").
- Keep secrets, tokens, and personal paths out; write `<repo root>`.
- Say each constraint once, where the agent will look for it; define each term once.
