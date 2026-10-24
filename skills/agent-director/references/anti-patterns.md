# Anti-patterns

Mistakes this method exists to prevent. Use as a last pass over a draft prompt or plan. Each row gives the mistake, why it hurts, and the correction.

## Contents
- Process
- Writing the prompt
- Repository and git
- Verification
- Security, ownership, provenance
- Visual and motion work

## Process

| Mistake | Why it hurts | Instead |
|---|---|---|
| Generating a giant prompt before requirements are mature | Locks in guesses; the agent faithfully executes the wrong plan | Keep planning; use the readiness check ([core-method.md](core-method.md)) |
| Writing a new prompt while an agent is working on overlapping scope | Collisions, duplicate work, conflicting commits | Review, plan, or isolate in a separate worktree |
| Reflexively writing the next prompt after every report | Skips verification and the decision | Verify the report, then choose the checkpoint |
| Merging, tagging, or releasing because implementation is done | Implementation authority is not public authority | Reserve those actions; use release mode |
| Spawning many agents to rediscover one repository | Cost, noise, integration debt | One primary agent; subagents only when independent and cheap to verify |

## Writing the prompt

| Mistake | Why it hurts | Instead |
|---|---|---|
| Forcing a powerful model through a file-by-file plan | Brittle; blocks better designs | Outcome, invariants, and proof; hypotheses labeled |
| "Make it like this" with no explanation | The agent imitates the wrong dimension | Annotate the reference with a job |
| Several references with no roles | An averaged, muddy result | One job per reference |
| Stating no branch or base | The agent works from the wrong commit | Pin branch, base SHA, and HEAD |
| Asking for hidden reasoning ("think step by step", "show your chain of thought") | Length without evidence | Ask for decisions and evidence |
| Padding a small task with ceremony | Wastes attention and hides the real constraint | Scale to risk |
| "While you're here" cleanup | Scope leakage | Name non-goals; allow only conditioned related fixes |
| Relying on stale issue checkboxes or old PR text | Rebuilds what exists or skips what is missing | Verify against the code; label history |

## Repository and git

| Mistake | Why it hurts | Instead |
|---|---|---|
| Parallel agents sharing a dirty checkout | Lost or entangled work | Separate worktrees and named ownership |
| Long uncommitted work before a compaction | Everything is lost with the context | Coherent checkpoint commits; the low-context protocol |
| AI attribution in commits, PRs, issues, docs, tags, or releases | Violates the user's standing rule | State the rule; override tooling defaults |
| Force-pushing or rewriting published history to fix attribution | Destroys shared history | Leave it; add the smallest safe new commit |
| Trusting contributor docs for the base branch | Docs drift | Check merge history and protection rules |

## Verification

| Mistake | Why it hurts | Instead |
|---|---|---|
| Treating CI as physical QA | CI cannot see the real terminal, device, or install | The evidence ladder; list what a human must check |
| Claiming mocked platform behavior as real validation | The mock may differ from the platform | Say which rung was reached |
| Raising timeouts to hide lifecycle bugs | The bug remains and resurfaces | Classify; fix the race |
| Changing product behavior to satisfy stale tests | Regresses intentional behavior | Fix the test when the test is wrong |
| Weakening legitimate tests to get green | Hides defects | Fix the product or document the limitation |
| Vague final reports without SHA, tests, and remaining human QA | The next step needs archaeology | The reporting contract |
| Repeating a full manual regression after every tiny patch | Burns the user's time | One consolidated pass at a milestone |

## Security, ownership, provenance

| Mistake | Why it hurts | Instead |
|---|---|---|
| Letting entry into a directory grant execution authority | Untrusted repositories run code | Explicit trust boundaries; bounded probes |
| Silently rewriting user configuration | Destroys user work and trust | Generated fragment, one reviewed include, proof of ownership |
| Forgetting removal and the user-modified case | Leaves debris or overwrites edits | Install, repair, uninstall; conflict on modification |
| Using upstream code without license or provenance analysis | Legal and trust risk | Classify reuse; inspect licenses; keep notices |
| Letting a reference become a runtime dependency | The product breaks when the reference moves | Reuse only what is licensed; do not depend on availability |

## Visual and motion work

| Mistake | Why it hurts | Instead |
|---|---|---|
| Fake product UI in demos or marketing | Misrepresents the product | Real captures; replace placeholders before delivery |
| Generic AI visual styling | Forgettable and off-brand | Real product truth and a distinct direction |
| Motion with no product story | Pretty and meaningless | Premise, states, and sequence first |
| Rendering the full film before inspecting keyframes | Wastes time; defects ship | Keyframes, contact sheet, animatic, critique, then render |
| Unseeded or history-dependent render pipelines | Frames differ from run to run | A deterministic timeline; seeded noise |
| Borrowing audio or media from references without rights | Legal exposure | Supplied, licensed, or original audio |
| Cropping every format from one master | Weak vertical and square versions | Compose per format |
