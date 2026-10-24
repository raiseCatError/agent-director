# Failure handling

What to demand when things break, and how to read a failure report. The governing rule: fix the layer that is actually wrong.

## Contents
- Classify before fixing
- Reproduce first
- What never to do
- CI-only failures
- Wrong assumption in the task
- Blockers and stop conditions
- Git operation failures
- When context or usage runs out

## Classify before fixing

Before anyone "fixes CI", assign the failure one class:

| Class | Typical evidence | Fix at |
|---|---|---|
| 1. Product bug | Reproduces locally; the behavior is wrong against the spec or invariants | Product code, plus a regression test |
| 2. Stale or incorrect test | The test asserts behavior the accepted design replaced, or is wrong on its own terms | The test; say why the old assertion was wrong |
| 3. Environment or tooling failure | Missing tool, wrong version, permissions, network, runner image | The environment or the tooling |
| 4. Timing or flaky | Passes and fails on the same commit; order or load dependent | The race or missing synchronization, not the timeout |
| 5. Platform limitation | Fails only on a platform that lacks a capability | Capability detection and a tested fallback |
| 6. Wrong assumption in the task | The prompt or plan asked for something the repository contradicts | The plan; report before building on it |

Ask the agent to name the class in its report with the evidence. A failure with no class has not been understood.

## Reproduce first

- Reproduce before changing anything: locally if possible, otherwise by matching the CI environment (image, versions).
- Reduce to the smallest failing case.
- To show a failure is not caused by the change, reproduce it at the exact base commit and report both results.
- For flaky tests, run repeatedly and note the failure rate; find the order or timing dependency.

## What never to do

- raise a timeout to hide a lifecycle bug
- change intentional product behavior to satisfy an obsolete snapshot
- weaken, skip, or delete a legitimate test to get green
- add retry loops around a race
- bypass hooks or verification (`--no-verify`) unless the user authorizes it
- claim an "environment problem" without evidence

## CI-only failures

When a failure appears only in CI, state the evidence precisely: job, step, log lines, runner image and tool versions, what was tried locally, and how the local environment differs. If the failure cannot be reproduced locally, say so; do not call it flaky or environmental without evidence. Try to match the environment (container, version pinning) before concluding.

## Wrong assumption in the task

If inspection shows the prompt's premise is false (the feature exists, the dependency is gone, the tracker is stale), stop and report when the correction changes scope or authority; otherwise adjust, continue, and report the difference. Do not build on a premise known to be false.

## Blockers and stop conditions

A genuine blocker is a product decision the agent cannot derive, a reserved action, a missing credential, or an ambiguity that cannot be responsibly inferred. On a blocker, the agent:
1. stops at the smallest safe checkpoint (committed, tested, tree understandable)
2. reports what is blocked, the evidence, the options, and a recommendation
3. does not improvise around authority or drift to unrelated scope while waiting

Write stop conditions into high-risk prompts explicitly (in a release, for example: any mismatch with the verified facts).

## Git operation failures

- Amend or rewrite blocked or unsafe: preserve the work and make the smallest safe new commit.
- Push rejected: fetch and inspect; never force.
- Merge or rebase conflict: resolve within the owned scope; read both sides; do not take one side wholesale.
- Hook failure: fix the cause.
- Protected branch rejects a direct push: use a PR, if authorized.

## When context or usage runs out

Follow the low-context protocol in [coding-agents.md](coding-agents.md), section "Long-horizon work": finish the smallest safe unit, test, commit, push if allowed, report the exact state, and stop. For the next session, see [continuation-and-handoffs.md](continuation-and-handoffs.md).
