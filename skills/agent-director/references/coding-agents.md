# Coding agents

Directing an implementation agent: what authority to grant and withhold, how many agents to use, and how to keep long runs recoverable. For prompt structure see [core-method.md](core-method.md); for branches, PRs, and releases see [git-branches-prs-releases.md](git-branches-prs-releases.md).

## Contents
- Default posture: action
- Delegated and reserved actions
- Deciding versus asking
- Extra work
- One primary agent
- Parallel agents and worktrees
- Long-horizon work
- Wording blocks

## Default posture: action

An implementation prompt hands a capable agent a job, not a questionnaire. The agent inspects the repository, chooses the architecture, writes tests, and carries the work to a checkpoint. Approval for each reasonable engineering choice is overhead the user did not sign up for. After the outcome and the invariants, tell the agent to inspect first: does the capability already exist in some form, what does the current architecture suggest, and which tests already cover the area.

## Delegated and reserved actions

Authority comes in two kinds. Say both in every implementation prompt.

**Delegated** (grant by default for implementation work):
- inspect the codebase and investigate the architecture
- choose implementation details and the internal design
- refactor a genuinely shared abstraction when several requested features need it
- add tests and fixtures
- fix directly related defects discovered along the way (conditions below)
- make coherent checkpoint commits
- push the permitted feature branch
- open or update a PR when the prompt authorizes it

**Reserved** (withhold unless the user grants it by name):
- merge
- tag, release, or version bump
- package publish (npm, Homebrew, registries)
- App Store or TestFlight upload, store submission
- deployment or any production mutation
- issue closure, or tracker status changes beyond what the project's workflow requires
- destructive history rewriting and force push
- changes to repository settings, branch protection, or CI secrets

Implementation authority never implies public authority. Permission to commit does not include push; permission to push a feature branch does not include merge; permission to open a PR does not include closing its issue. Grant each by name, and when one is withheld, say what to do instead: stop and report.

## Deciding versus asking

The agent asks the user only for:
- a genuine product decision it cannot derive from the product, docs, and established patterns
- a reserved action
- an unavailable secret or credential
- an ambiguity that cannot be responsibly inferred

Everything else it decides, records in the report, and moves on. Make blockers cheap: tell the agent that on a blocker it stops at the smallest safe checkpoint and reports what is blocked, the evidence, the options, and a recommendation.

## Extra work

Welcome:
- a regression test for a bug uncovered by the requested change
- making a shared abstraction correct because several requested features depend on it
- repairing a directly related stale test
- improving error reporting that the feature needs in order to be truthful
- a missing security fixture around a parser the change introduces
- (creative work) a stronger shot or story that communicates the real product better

Unwelcome:
- unrelated refactors
- a dependency swap because it is fashionable
- reviving deferred backlog
- casually changing product terminology
- a new framework for convenience
- publishing or releasing without authority
- a broad redesign because the touched screen looked old

A related bug fix is in bounds when all four hold: it was reproduced during the task; it lives in the touched subsystem; regression coverage can accompany it; and it does not materially widen the product scope. Anything else goes in the report as deferred.

## One primary agent

Default to one strong agent. Swarms re-derive the same repository, multiply cost, and create integration work. Allow subagents only when all of these hold: the work is independent, parallelism materially helps, ownership boundaries are clear, and the result is cheap to verify (for example, read-only research on a large dependency, or an independent platform test matrix). The primary agent owns integration and the report.

Do not instruct the agent to spawn helpers as a matter of routine. If subagents are permitted, say for what, and that the primary agent remains responsible.

## Parallel agents and worktrees

When more than one coding agent is active:
- give each its own branch and its own worktree (`git worktree add <path> -b <branch> <base-sha>`)
- record the exact base SHA for each
- assign ownership by subsystem or directory, and name it
- never switch branches in a checkout that holds another agent's uncommitted work
- avoid shared dirty working directories
- do not merge or rebase another agent's work unless that is the task
- leave integration decisions to the user

For creative or demo work that runs beside product development (a film, a site, captured assets), use a sibling worktree or project so rendering code, captures, and large assets cannot dirty the primary implementation checkout. Treat this as a reusable pattern, not a fixed path.

## Long-horizon work

Treat git as durable agent memory. Context windows and usage limits end; commits do not.

- Divide the work into coherent architectural checkpoints. A slice is done when it is internally coherent, tested, and leaves the tree explainable.
- Run focused validation during a slice and the full canonical verification at durable checkpoints.
- Commit only coherent slices. Keep commits bisectable and the history readable.
- Push at meaningful safe points. Keep the worktree understandable.
- Do not create planning or scratch files as a habit. A design note the repository would keep is fine; endless private scratchpads are not.

If context or usage runs low:
1. finish the smallest safe coherent unit
2. test it
3. commit it
4. push if the prompt allows
5. update or open the PR if the prompt allows
6. leave the worktree clean, or describe exactly what is left uncommitted and why
7. report the exact branch, SHA, tests, and next action
8. stop

Never leave a large uncommitted architectural rewrite as the only durable state before a compaction.

## Wording blocks

Adapt, do not paste blindly.

**Authority**
> You may inspect and change anything needed on branch `<branch>` (from `<base>` at `<sha>`), add tests and fixtures, commit coherent checkpoints, push that branch, and open a draft PR to `<base>`. You may not merge, tag, bump the version, edit release notes, close issues, force-push, or touch other branches or worktrees. If the work needs one of those, stop at a safe checkpoint and report.

**One agent**
> You are the only agent on this work. Do not spawn subagents unless a task is independent, parallelism clearly helps, and the result is cheap to verify; you remain responsible for integration.

**Parallel**
> Another agent is working on `<scope>` in `<worktree>`. Stay inside your own worktree and branch, do not touch theirs, and do not merge or rebase their work.

**Long horizon**
> Work in coherent checkpoints and commit each one after it passes focused validation; run full verification before pushing. If context or usage runs low, finish the smallest safe unit, test, commit, push, update the PR, and report the exact branch, SHA, tests, and next action. Do not leave a large uncommitted rewrite as the only record.
