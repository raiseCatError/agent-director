# Audit and review

Prompts for reviewing code, a PR, or a release candidate, and for judging an audit's output.

## Contents
- Decide the mode
- Scope
- Priorities
- Findings format
- Verification before reporting
- Known limitations
- Output shape
- After the audit

## Decide the mode

- **Report-only**: the agent finds and reports; it changes nothing. Say so in words: "Do not edit the repository."
- **Audit and fix**: the agent also fixes what it finds. Keep findings and fixes separate in the report; the fixes follow [coding-agents.md](coding-agents.md).

When the user says "don't change anything", choose report-only and make it concrete:
- no edits, commits, pushes, branch changes, stashes, PR comments, issue changes, or tracker updates
- builds and tests run in a scratch worktree or with outputs outside the tree, and every artifact is removed
- the agent proves at the end that HEAD and `git status` are unchanged

Prefer a fresh session for an audit of code the same agent wrote.

## Scope

State the exact range (base and head SHAs, or the PR), the subsystems, and the threat or failure model. Ask the agent to inspect reachable behavior, not only the diff: trace from real entry points (inputs, commands, lifecycle events) into the changed code, and run it when that is safe.

If the working tree is dirty, say whether uncommitted work is in scope. What merges is the committed range, so review uncommitted changes separately, label each finding committed or uncommitted, and test the exact head in a scratch export rather than in the dirty checkout.

## Priorities

In order: security, races and lifecycle, protocol correctness, data loss, release and packaging defects, compatibility. Then test gaps, reported separately from code defects. Style and speculative concerns stay out unless they create a concrete risk; a flood of nits hides the real findings.

## Findings format

Each finding carries:
- ID and severity (define the scale in the prompt: Critical, High, Medium, Low)
- location: file and line at a named SHA
- category: code defect, test gap, spec or doc mismatch, or accepted-limitation interaction
- reachable scenario: preconditions, steps, observed versus expected
- evidence: a reproduction command, failing fixture, or trace; if unproven, what would confirm it
- impact
- confidence: confirmed or plausible
- suggested direction (not a patch)

## Verification before reporting

Reproduce each finding at the head SHA before reporting it. Mark a finding plausible only when reproduction is not possible, and say what blocked it. Drop findings that depend on an unreachable path.

## Known limitations

List the accepted limitations in the prompt so the reviewer does not re-report them. Ask the reviewer to flag a new defect that interacts with one.

## Output shape

1. Findings, ordered by severity, duplicates grouped
2. Test gaps
3. Areas examined with no findings (a few lines)
4. What could not be verified, and why (for example, no real host)
5. Proof the repository is unchanged (report-only)

## After the audit

Triage with the user. Turn accepted findings into a fix prompt (implementation mode) that cites finding IDs rather than pasting the whole report, and keep rejected findings with the reason so they are not raised again. Example prompt: [../examples/audit-review.md](../examples/audit-review.md).
