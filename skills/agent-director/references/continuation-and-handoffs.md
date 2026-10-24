# Continuation and handoffs

Moving work between sessions without losing accuracy, and reading what an agent sends back.

## Contents
- Fresh or same session
- Fresh-session handoff
- Same-session continuation
- Recovering after compaction or a usage limit
- Reviewing a returned report
- Choosing the next checkpoint

## Fresh or same session

Decide for every prompt and label it ("Fresh Claude session" or "Same Claude session"; use the agent's name if the user named another).

Same session fits when the agent holds accurate, valuable context, the context is not near its limit, and the next work builds directly on the last checkpoint.

Fresh session fits when the previous session finished, compacted, hit a usage limit, or drifted; a different agent or model takes over; a new phase begins (review, release); or fresh eyes matter (an audit of code the same agent wrote).

When it is unclear, write the fresh-safe prompt. It works in both cases; a same-session prompt pasted into a fresh session fails.

## Fresh-session handoff

The agent starts with nothing. Give it enough durable state to reconstruct the task, and tell it to verify before trusting.

Contents, in order of usefulness:
1. **Mission and product identity**, briefly.
2. **Repository and state**: name and location, branch, upstream, base branch and SHA, HEAD SHA, working-tree state (and who owns any uncommitted work), worktrees, PR number and state and base, CI at HEAD. Mark each fact verified, with when.
3. **Source of truth**: which documents and issues are authoritative, which are history.
4. **Completed and accepted work**: checkpoints with SHAs; what is proven and how.
5. **Decisions already made**, each with a one-clause reason, so the agent does not reopen them.
6. **Remaining work and the immediate next outcome**.
7. **Invariants and non-goals** that matter most.
8. **Authority**: delegated and reserved, unchanged or changed.
9. **Validation expectations** and the **human-QA status**: done, pending, and the exact pending list.
10. **Known limitations accepted**, and defects known but deferred.
11. **First moves**: reconstruct state from the repository, report any delta from the handoff, then continue.

Rules:
- Point to durable artifacts (docs, PR, issue, commit) instead of re-pasting their contents.
- Summarize decisions; do not paste chat transcripts.
- State what is stale: abandoned branches, superseded plans, wrong tracker checkboxes.
- If the previous session's worktree holds uncommitted work, say so, tell the agent to read the diff before deciding to keep, commit, or discard it, and to discard nothing unread.
- Include the conflict rule: the repository beats the handoff; report discrepancies; stop if a discrepancy changes scope or authority.

State block template:

```
Repository: <name> (<path or remote>)
Branch: <name> tracking <upstream>; base <branch> @ <sha>; HEAD <sha> (verified <when>)
Working tree: <clean | uncommitted: what, owned by whom>
Worktrees and other agents: <none | list with ownership>
PR: <#, state, base, CI at HEAD>
Accepted checkpoints: <sha: summary> ...
In progress: <...>
Remaining: <...>
Decisions made: <decision, reason> ...
Source of truth: <authoritative> / history: <stale>
Accepted limitations: <...>
Human QA: <done | pending: list>
```

A complete example: [../examples/fresh-session-handoff.md](../examples/fresh-session-handoff.md).

## Same-session continuation

The agent already knows the project. Describe only what changed.

Include: the accepted checkpoint (SHA); what is new since the last report (user decisions, QA findings, review comments, new constraints); the next outcome; anything whose authority or scope changed. State what remains unchanged in one line, so silence is not read as revocation.

Omit: the project encyclopedia, restated invariants, repeated history.

Add a two- or three-line pin of the highest-risk invariants only when the session has been compacted or the next slice touches them. A pin is a reminder, not a restatement.

Example: [../examples/continuation.md](../examples/continuation.md).

## Recovering after compaction or a usage limit

When the user returns after a compaction or a limit:
1. Rebuild state from durable sources: `git log`, `git status`, the branch and PR, CI, the last report. Ask the user to paste the last report if it is not available.
2. Compare the last report with the repository. The repository wins.
3. Decide fresh or same. After a limit or a degraded context, choose fresh.
4. Write the handoff from the verified state, not from memory of the conversation.

Ask agents in long prompts to leave the repository recoverable ([coding-agents.md](coding-agents.md), section "Long-horizon work"); that is what makes this step cheap.

## Reviewing a returned report

An agent's report is a set of claims. Extract them and check what tools allow before deciding anything.

1. **Extract**: branch, resulting HEAD, commits, PR, files and subsystems, tests run, CI status, packaging or install validation, physical QA performed and still required, limitations, deferred scope, blockers, next action.
2. **Verify**: compare `git rev-parse` of the branch with the reported HEAD; `git status` for cleanliness; `gh pr view` and `gh pr checks` for the PR and for CI at that exact SHA; the diff stat for scope; a cheap re-run of the key test when that is affordable.
3. **Classify each claim**: verified, reported only, or contradicted.
4. **Scope audit**: did the work respect the non-goals? Is any extra work justified under the extra-work conditions?
5. **Failures**: classify before reacting ([failure-handling.md](failure-handling.md)).
6. **Evidence audit**: strike any "fully verified" that rests on CI or mocks where the boundary was physical ([validation-and-physical-qa.md](validation-and-physical-qa.md)).
7. **Tell the user plainly**: what is verified, what is only claimed, what is wrong, and what human QA is outstanding.

## Choosing the next checkpoint

| The report shows | Next step |
|---|---|
| Done, verified, no outstanding physical QA | Accept; start the next slice or call it PR-ready. |
| Done, physical QA pending | Produce one consolidated human checklist; hold release; write no new prompt on the same scope until findings arrive. |
| A product bug | Same-session fix-forward prompt with the diagnosis. |
| A stale test or a tooling failure | Narrow prompt that fixes the right layer. |
| Unrequested changes | Ask for the extras to be reverted in a new commit, or accept them with reasons. |
| Blocked on a product decision | Return to planning with the user. |
| Context or usage exhausted mid-slice | Fresh handoff from the last pushed checkpoint. |
| Merged by the user and QA passed | Release mode ([git-branches-prs-releases.md](git-branches-prs-releases.md)). |

If another agent is still working on the same scope, do not write an overlapping prompt: see [core-method.md](core-method.md), section "Active-agent check".
