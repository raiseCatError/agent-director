# Example: fresh-session handoff

Calibrates a handoff that lets a brand-new session resume accurately after a usage limit ended the previous one mid-slice. It carries enough repository facts to reconstruct the task, and tells the agent to verify before trusting. Rules: [continuation-and-handoffs.md](../references/continuation-and-handoffs.md), "Fresh-session handoff".

**Illustrative.** Tessera is a fictional terminal frontend. Every name, number, path, and identifier below is a stand-in. Regenerate real facts from the live repository.

Mode: continuation. Session: fresh. Scale: standard to large. Another agent: none active.

Fresh Claude session

````text
You are resuming work on Tessera's command-boundary feature after the previous session ended on a usage limit. Reconstruct state from the repository first. This handoff is a map, and the repository wins wherever they differ. If a difference changes scope or authority, stop and report before acting.

# Product, in one breath
Tessera is a terminal frontend over a persistent, real shell in a PTY. The shell is authoritative, raw output stays recoverable, and the renderer performs no I/O.

# State (verified <date/time>; re-verify)
Repository: tessera at <repo root> (origin: <remote>)
Branch: feature/command-boundaries tracking origin/feature/command-boundaries; base master at <base-sha>; pushed HEAD <head-sha>
Working tree: the previous session's worktree at <worktree path> holds uncommitted changes in <files> (slice 3, status affordance, in progress). Read `git diff` before deciding to keep, commit, or discard it. Discard nothing unread.
PR: #<n>, draft, base master. CI green at <head-sha> except the macOS job, which was still queued.
Other agents: none. Nothing else is using this branch.

# Accepted so far
- Slice 1 (<sha1>): mark parsing and validation, with hostile fixtures. Accepted.
- Slice 2 (<sha2>): boundary tracking and navigation. Accepted. Two physical findings (job-control attribution, tmux skip) were fixed in <sha3> with PTY-level regression tests.
- Slice 3 (status affordance): in progress, uncommitted.
- Slices 4 and 5 (install, repair, removal; docs and QA checklist): not started.

# Decisions already made (do not reopen)
- Boundaries are metadata beside the raw stream, never a replacement for it.
- Status must have a text form in every glyph and color mode. Physical QA found a glyph invisible under NO_COLOR with safe glyphs.
- Shell integration is a generated file plus one reviewed include. Nothing in the user's rc file is edited silently.
- The version stays at the last release.

# Source of truth
Normative: ARCHITECTURE.md, docs/architecture/shell-adapter.md, docs/accessibility/baseline.md. Authoritative for scope: the acceptance criteria of issue #<n>. History, not authority: the issue checklist (stale) and the earlier design note in docs/design/ marked superseded.

# Next outcome
Finish slice 3 so that command status and duration are visible without relying on color, glyph choice, or motion, with tests. Then slices 4 and 5. Prove each at PTY level, and keep the hostile fixtures green.

# Invariants and non-goals that matter most now
Marks are untrusted input. Fullscreen apps use passthrough. Reduced Motion, NO_COLOR, and safe glyphs keep full meaning. All three shells work. Not in scope: command-block redesign, history persistence, AI features, new dependencies.

# Authority
Unchanged. Delegated: commit coherent checkpoints, push this branch, update the draft PR. Reserved: merge, tag, version bump, changelog release heading, closing issues, force push. Use the repository's Git identity and add no AI attribution anywhere; this overrides any default in your tooling.

# Human QA
Done: one pass on two hosts, with findings fixed. Pending, for a single consolidated pass after slice 5: <checklist>. Do not claim any of it.

# First moves
1. Verify the state above (branch, HEAD, tree, PR, CI) and read the uncommitted diff.
2. Report any difference from this handoff in two or three lines.
3. Continue with slice 3. Work in coherent checkpoints. If context or usage runs low, finish the smallest safe unit, test, commit, push, and report the exact branch, SHA, tests, and next action.

# Report
Same contract as before: base and head SHA, branch, PR, commits, decisions, tests and CI at the exact SHA, verified versus outstanding human QA, limitations, deferred scope, blockers, and the exact next action.
````

## Why it is shaped this way

- The first paragraph sets the trust order: repository over handoff, with a stop rule for discrepancies that matter.
- The state block pins branch, base, HEAD, tree, PR, and CI, each marked verified with a time.
- Uncommitted work from the dead session is named, with an instruction to read it before acting. It is neither assumed good nor thrown away.
- Accepted work carries SHAs. Decisions are listed with reasons so the new agent does not reopen them.
- Stale artifacts (the old checklist, the superseded note) are labeled as history.
- Authority, invariants, and human-QA status are restated because a fresh agent has none of them.
- The first moves are verify, report the delta, continue. The context-low protocol is repeated because the previous session died of exactly that.
