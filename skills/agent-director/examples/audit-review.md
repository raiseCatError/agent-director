# Example: report-only audit

Calibrates a review prompt that forbids modification, scopes the audit to reachable behavior, ranks priorities, states accepted limitations, and demands reproducible evidence. Rules: [audit-and-review.md](../references/audit-and-review.md).

**Illustrative.** Tessera is a fictional terminal frontend. Every name, number, path, and identifier below is a stand-in. Regenerate real facts from the live repository.

Mode: audit, report-only. Session: fresh (fresh eyes on code another session wrote). Scale: standard to large. Another agent: none active on this PR.

Fresh Claude session

````text
Report-only audit of PR #<n> in Tessera (`<base-sha>..<head-sha>`, branch `feature/command-boundaries`).

# Hard rule: do not edit the repository
No edits, commits, pushes, branch changes, stashes, PR or issue comments, or tracker updates. Build and test in a scratch worktree (`git worktree add <scratch> <head-sha>`) or send outputs outside the tree. Remove every artifact. Finish by proving that the original checkout's HEAD and `git status` are unchanged.

# What the change does
Adds command-boundary tracking from shell-integration marks in the PTY stream, keyboard navigation between commands, a status affordance, and an installer for the shell-integration snippet (a product-owned generated file plus one reviewed include). The accepted design is in docs/design/command-boundaries.md. Treat the docs as intent, not proof.

# Scope
The diff, plus everything reachable from it. Trace from the real entry points (bytes arriving from the PTY, keyboard commands, install, repair, and remove actions, shell lifecycle events) into the changed code, and run behavior when that is safe. Out of scope: unrelated subsystems, style, naming, and refactors that are not defects.

# Threat and failure model
- Hostile input: program output that forges, splits, interleaves, or floods marks; crafted cwd or environment values (control characters, bidi, long strings); symlinked or unreadable paths in the installer; a user-modified generated file; a hostile rc file.
- Lifecycle and races: suspend and resume (Ctrl+Z, fg), fullscreen app round trips, resize storms, child crash, rapid command sequences, shutdown during a pending mark.
- Protocol and state: boundaries attributed to the wrong command; stale state after passthrough; unbounded memory.
- Release defects: files missing from packaging, version or docs mismatches, install or removal leaving debris.

# Priorities
Security, races and lifecycle, protocol correctness, data loss, release defects, compatibility across the three shells. Then test gaps, reported separately from defects. No style comments. No speculative findings without a reachable path.

# Accepted limitations (do not re-report; flag a new defect that interacts with one)
- Marks inside tmux are tracked only when passthrough is enabled.
- Remote shells without the integration show no boundaries.
- Boundary timing is accurate to within one frame.

# Method
Reproduce each finding at `<head-sha>` before reporting it. If you cannot, mark it plausible and say what blocked you. Distinguish code defects from test gaps. Say what you could not verify, for example anything that needs a real terminal host.

# Finding format
ID; severity (Critical: exploitable or data-destroying. High: wrong behavior on a common path, or a reliable crash. Medium: wrong behavior in a plausible edge case, or a missing guard. Low: minor); location (file:line at `<head-sha>`); category (code defect, test gap, doc mismatch, accepted-limitation interaction); reachable scenario (preconditions, steps, observed versus expected); evidence (command, fixture, or trace); impact; confidence (confirmed or plausible); suggested direction (not a patch).

# Report
1. Findings by severity, duplicates grouped.
2. Test gaps.
3. Areas examined with no findings (a few lines).
4. What you could not verify, and why.
5. Proof the repository is unchanged.
Report only findings that survive verification. No recap of the diff and no celebration.
````

## Why it is shaped this way

- "Do not edit the repository" is stated in words and made concrete: scratch worktree, artifact removal, and proof of an unchanged tree at the end.
- Scope is reachable behavior, not just the diff, so the agent follows real entry points.
- The threat model and priorities keep the report on security, lifecycle, protocol, and release defects, not style.
- Accepted limitations are listed so they are not re-reported, with a request to flag interactions.
- Every finding must be reproduced at a named SHA, and severity is defined in the prompt so ratings are comparable.
- After this report, triage with the user and send a fix prompt that cites finding IDs ([audit-and-review.md](../references/audit-and-review.md), "After the audit").
