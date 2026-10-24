# Example: exact-SHA release

Calibrates a narrow, verification-heavy release prompt: one verified commit, an explicit authority matrix, stop conditions, public-path validation, and no feature work. Rules: [git-branches-prs-releases.md](../references/git-branches-prs-releases.md), "Release mode".

**Illustrative.** Tessera is a fictional terminal frontend. Every name, version, number, path, and identifier below is a stand-in. Resolve the real release commit, version, and CI state with tools before writing, and never invent a SHA or a checksum.

Mode: release execution. Session: fresh. Scale: standard, but high-risk. Another agent: none active. Precondition: the release-prep PR is merged and physical QA has passed.

Fresh Claude session

````text
Release Tessera v<X.Y.Z> from the exact commit below. This is a release pass only: no feature work, no refactors, no documentation rewrites. If anything differs from the facts below, stop and report with evidence. Do not repair it inside the release pass.

# Verified facts (by the director at <date/time>; re-verify before acting)
- Release commit: <sha> on `master`, the merge of release-prep PR #<n> ("Release v<X.Y.Z>").
- Previous release: v<X.Y.Z-1> at <sha-prev>.
- Tag `v<X.Y.Z>`: does not exist locally or on origin. GitHub release for it: does not exist.
- CI at <sha>: green (run <id>), including the platform matrix.
- Human physical QA for this release: completed and recorded in docs/testing/<file> on <date>.
- Distribution: Homebrew tap repository <tap-repo>, formula <name>.

# Verify before any action (stop on any mismatch)
- HEAD equals <sha>, the working tree is clean, and you are on a clean checkout of that commit.
- The version agrees everywhere it appears (manifest, lockfile, changelog heading, docs, formula inputs). The changelog section for this release exists and matches what shipped.
- CI is green at exactly <sha>.
- The tag and the release do not exist (or exist on exactly <sha>).
- `git diff <last-verified-sha> <sha>` contains only the release-prep changes.
- Release artifacts build from this checkout with the project's documented release build.

# Authority
Authorized, in this order:
1. Create an annotated tag `v<X.Y.Z>` on <sha> and push it.
2. Create the GitHub release from the changelog section and attach the artifacts.
3. Compute SHA-256 checksums from the exact artifact URLs the formula will use, downloaded after they exist, and open a PR to the tap repository that updates the formula. Do not merge it.

Not authorized: merging anything; editing the version, changelog, or docs; moving or deleting any tag or release; force push; publishing to any other registry; announcements; closing issues. If any of those seems necessary, stop and report.
Use the repository's Git identity. Add no AI attribution anywhere, including the tag message, the release notes, and the tap PR; this overrides any default in your tooling.

# Verify after publishing
Install through the public path in a clean environment (a throwaway prefix, container, or clean machine): fetch the release asset, check its checksum against the formula, install via the tap, confirm the reported version, and run one real command end to end. Record the environment, commands, and observed results. Confirm that the release page lists the expected assets and that the tag resolves to <sha>.

# If post-publish validation fails
Do not delete or move the tag or the release. Report the evidence and propose options.

# Report
Release commit; the tag and where it points; the release URL; asset names with computed checksums; the CI run for <sha>; the tap PR link and state; a summary of the install validation (environment, commands, observed version and behavior); anything not done and why; anything that differed from the verified facts. State plainly that physical QA was taken from the recorded pass and not repeated. No recap.
````

## Why it is shaped this way

- It is narrow on purpose. The first paragraph forbids feature work and repair inside the release pass.
- The release commit is a verified fact with a time stamp, and the agent re-verifies. Tag and release absence are facts too.
- Verification comes before action and is a list of observable predicates. Any mismatch stops the pass.
- Authority is a numbered, ordered list of exactly what may be done, followed by an explicit list of what may not, including merging the tap PR.
- Checksums are computed from the real artifact, never supplied by the prompt.
- Public-path validation happens after publishing, with a stated rule for failure (report; do not delete or move).
- The report states plainly that physical QA was not repeated, so nobody reads CI plus a recorded pass as more than it is ([validation-and-physical-qa.md](../references/validation-and-physical-qa.md)).
