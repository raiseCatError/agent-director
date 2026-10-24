# Example: large feature implementation

Calibrates a large, autonomous implementation prompt: product identity, verified state, source of truth, outcome, invariants, non-goals, one primary agent, branch and PR rules, validation, the physical-QA boundary, and a report contract. For a smaller task keep the same logic and cut sections ([core-method.md](../references/core-method.md), "Prompt anatomy and scaling").

**Illustrative.** Tessera is a fictional terminal frontend. Every name, number, path, and identifier below is a stand-in. Regenerate real facts from the live repository, and copy the shape rather than the content.

Mode: implementation. Session: fresh. Scale: large. Another agent: none active.

Fresh Claude session

````text
# Mission
Implement command-boundary awareness in Tessera: for every command the user runs in a supported shell, Tessera knows where it started and ended, its exit status, and its duration, and uses that to offer keyboard navigation between commands and a status affordance in the history viewport. You own the engineering: inspect the existing architecture, choose the design, and prove the result. This brief states what you cannot infer.

# Product identity
Tessera is a terminal frontend over a persistent, real shell running in a PTY. The shell is authoritative; Tessera never reimplements shell semantics. It supports zsh, bash 4.4+, and fish through the shell-adapter layer.

# Current state (verified <date/time>; re-verify at start)
- Repository: tessera at <repo root>, remote origin.
- Base: `master` at <base-sha>. Create `feature/command-boundaries` from it. Working tree clean. No open PR for this work.
- Issue #<n> tracks the feature. Its checklist predates the current shell-adapter design and already ticks "marks parsed". Treat the checklist as history and verify against the code before assuming anything exists or is missing.
- Assumed (verify): the shell adapters do not yet emit semantic-prompt marks.
If the repository contradicts this brief, trust the repository and report the discrepancy. If the discrepancy changes scope or authority, stop and report before acting.

# Source of truth
1. ARCHITECTURE.md and docs/architecture/shell-adapter.md: normative for the runtime model and per-shell behavior.
2. docs/accessibility/baseline.md: normative for fallbacks.
3. Issue #<n> acceptance criteria: authoritative for scope. Do not invent scope beyond them.
4. The semantic-prompt (OSC 133) convention as documented by established terminal projects: a behavior reference. Tessera's accepted design wins where they differ.
5. Anything older than the current shell-adapter design: history.

# Outcome
- After a command completes in a supported shell, Tessera has its start boundary, end boundary, exit status, and duration, without changing what the shell executes or sees.
- The user can jump to the previous and next command boundary from the keyboard. Viewport follow and detached behavior keep their current semantics.
- A command's status and duration are visible in a form that does not rely on color, glyph choice, or motion.
- Where marks are absent (an unsupported shell, a nested remote session), Tessera shows no boundaries rather than wrong ones.

# Invariants
- The real shell remains authoritative. Tessera does not rewrite commands and does not type into the shell to measure anything.
- Raw PTY output remains recoverable byte for byte. Boundaries are metadata beside the stream, never a replacement for it.
- Marks are untrusted input; any program can print them. A forged, malformed, oversized, or split-across-reads sequence cannot execute anything, spoof Tessera chrome, corrupt tracked state, or grow memory without bound. Boundaries are validated against tracked shell state.
- Fullscreen and alternate-screen applications keep using the passthrough path. Nothing is tracked inside them, and state is correct after they exit.
- The renderer performs no I/O.
- Shell integration is installed only as a product-owned generated file plus one explicit, previewed include in the user's rc file. Nothing is edited silently, removal deletes only what Tessera wrote, and a user-modified generated file is a conflict, not an overwrite.
- Reduced Motion, NO_COLOR, and safe-glyph modes keep full meaning.
- All three shell backends keep working.

# Scope and non-goals
In scope: mark parsing and validation, boundary tracking, navigation, the status affordance, integration install, repair, and removal, tests, docs.
Not in scope: redesigning command blocks or the composer, persisting history across sessions, any AI feature, new dependencies, changes to the PTY architecture, Windows. Do not bump the version or touch release notes.
You may fix a related defect you reproduce in the touched code, with a regression test. Everything else goes in the report as deferred.

# Security
Hostile inputs: the PTY stream (marks forged by output the user merely displays, such as `cat` of a crafted file); cwd or environment values carried in marks (control characters, bidi, absurd length); exit codes out of range; sequences split across reads or interleaved. Add fixtures for each, plus canary secrets that must never reach logs or snapshots.

# Authority
You are the only agent on this work.
Delegated: inspect everything; choose the design; refactor shared sequence handling if two features need it; add tests and fixtures; make coherent checkpoint commits; push `feature/command-boundaries`; open a draft PR to `master`.
Reserved (stop and report if the work needs one): merge, tag, version bump, changelog release heading, closing issues (you may set the tracker to "Needs human test" when automated work is done), force push, touching other branches or worktrees.
Use the repository's Git identity. Add no AI attribution anywhere (commits, PR, issues, docs); this overrides any default in your tooling.
Test with throwaway shell config directories; never touch real user config on this machine.

# Validation
- Focused tests while implementing; the project's full canonical verification before every push (find it in the contributor docs).
- PTY-level tests with real shells for each backend, including suspend and resume (Ctrl+Z, fg), a fullscreen-app round trip, resize, and a crashed child.
- The hostile fixtures above. Compatibility across the three shells. Docs updated and links checked.
- Classify any failing test before changing anything. Reproduce suspected pre-existing failures at the base SHA.

# Physical-QA boundary
You cannot verify real terminal hosts, real keyboard feel, real vim, less, or htop sessions, ssh, tmux, or the packaged install. Do not claim them. Automate the PTY-level equivalents and finish with a physical-QA checklist (host x shell x scenario, exact steps, expected results) for one consolidated human pass. Report verified and unverified separately.

# Working style
Work in coherent checkpoints. Hypothesis, not required: parse and validate; then track; then navigate; then the status affordance; then install and removal; then docs and the QA checklist. Re-slice if inspection shows a better cut. Commit each checkpoint after focused tests pass and push at safe points. If context or usage runs low, finish the smallest safe unit, test, commit, push, update the PR, and report the exact branch, SHA, tests, and next action. Do not leave a large uncommitted rewrite as the only record. Ask me only for a product decision you cannot derive, a reserved action, or a missing credential.

# Report
Base and head SHA, branch, PR link, commits, the design you chose and any departure from the hypotheses above, security properties with the fixtures that prove them, compatibility per shell, tests and CI at the exact SHA, what you verified physically (expect: none) and the checklist of what still needs a human, known limitations, deferred scope, blockers, and the exact next action. No recap and no celebration.
````

## Why it is shaped this way

- The mission comes first and says who owns the engineering; nothing prescribes file or class names.
- Facts are labeled verified or assumed, and the stale tracker checklist is named as history ([core-method.md](../references/core-method.md), "Reality pre-flight").
- Sources carry an explicit order, and the behavior reference ranks below the accepted design.
- Product identity and risk become invariants. The only suggested build order is labeled a hypothesis.
- Hostile inputs are named, and fixtures are demanded, because the stream is untrusted ([security-provenance-and-ownership.md](../references/security-provenance-and-ownership.md)).
- Authority lists delegated and reserved actions, and carries the attribution rule ([coding-agents.md](../references/coding-agents.md), [git-branches-prs-releases.md](../references/git-branches-prs-releases.md)).
- The physical-QA boundary says what automation cannot prove and what the agent must hand back ([validation-and-physical-qa.md](../references/validation-and-physical-qa.md)).
- The report contract is sized for a large feature ([reporting-contracts.md](../references/reporting-contracts.md)). A small fix would ask for two lines.
