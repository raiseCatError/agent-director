# Case studies

Evidence behind the doctrine, drawn from real projects. The lessons are general; the projects are named only because the evidence is theirs. Do not import project specifics into other prompts.

## Contents
- notMyShell (NMSh)
- MeowDisplay
- Through-lines

## notMyShell (NMSh)

NMSh is a terminal frontend that sits over a persistent, real shell running in a pseudo-terminal.

**1. Product identity as invariants.** The project's agent guide states identity as testable properties: the real shell stays authoritative, raw PTY output stays raw, fullscreen applications use a passthrough path, terminal-host-specific enhancements never become structural dependencies, and automated test passage is not physical terminal validation. Lines like these let a prompt say what must stay true without prescribing code. *Doctrine:* express identity as invariants ([core-method.md](core-method.md)).

**2. Green CI missed real terminal behavior.** Physical bugs showed up in real terminals that automated checks did not catch, notably key routing such as Ctrl+Z and terminal-lifecycle behavior around suspend, resume, and handoff. The project responded structurally: its guide says automated passage is not physical validation, it keeps a physical-QA record per milestone, and its tracker has a "Needs Human Test" state between automated and human validation. *Doctrine:* the evidence ladder and the consolidated human pass; when physical QA finds a bug, add a regression test if it is meaningfully automatable ([validation-and-physical-qa.md](validation-and-physical-qa.md)).

**3. Protected branches and release separation.** The stable branch is protected and work lands through PRs. Release preparation (version and changelog) ran as its own branch and PR, and a later PR documented Homebrew availability separately. The project's guide keeps the package version at the last release during development and treats a bump as part of explicitly authorized release preparation. *Doctrine:* implementation authority is not public authority; release is its own narrow mode ([git-branches-prs-releases.md](git-branches-prs-releases.md)).

**4. Parallel Claude and Codex work.** Several agents worked at once. Isolated worktrees, named ownership, and a recorded base SHA kept each agent's uncommitted work out of the others' way and kept the main checkout understandable. *Doctrine:* [coding-agents.md](coding-agents.md), section "Parallel agents and worktrees".

**5. Long-running work survived through commits.** Large programs advanced as coherent checkpoint commits with pushes at safe points, so a fresh session could resume from the repository and the last report rather than from memory. *Doctrine:* git as durable memory; the low-context protocol.

**6. Context Engine and hostile workspaces.** A feature that reads the user's project directory had to treat the workspace as hostile. The program kept an agent protocol, a lifecycle matrix, and a review handoff with explicit security evidence and limits, and it recorded reproductions of failing assertions on the exact base commit to separate pre-existing failures from new ones. *Doctrine:* entering a directory must not grant execution; bounded, sanitized facts; hostile fixtures; failure classification with base-commit reproduction ([security-provenance-and-ownership.md](security-provenance-and-ownership.md), [failure-handling.md](failure-handling.md)).

**7. Theme Bridge and configuration ownership.** Extending theme colors to external tools was designed as an explicit, initially disabled system. NMSh records what it wrote in an ownership ledger with content hashes; a file the user edited produces a conflict instead of an overwrite; activation inside executable config is an exact reviewed edit, never a generic merge; and tmux configuration uses one managed file that the user's config includes through a reviewed step. *Doctrine:* a product-owned generated fragment plus one explicit include.

**8. Homebrew package validation.** The Homebrew install path was treated as something to validate with a real install, with checksums computed from real artifacts, and the availability documentation followed in its own PR. *Doctrine:* release verification covers the public path; never invent checksums.

**9. The showreel.** A roughly 20-second reel for the product:
- It ran in an isolated sibling checkout so rendering code and large assets never dirtied the product checkout.
- Takes were recorded from the real product in a real terminal host and replayed through a deterministic renderer, and production takes were built from a specific product commit, so captures stayed authentic and re-creatable.
- The brief analyzed two reference films along different dimensions (OpenCode 2's launch film for how to show a real product; the Claude Motion Reel for density and pacing), listed what to borrow (grammar) and what not to (identity), and was later superseded by a creative reset while its product constraints stayed in force.
- The product's existing mascot, Vespyr the cat, kept its real design instead of becoming a generic one.
- The review packet was an animatic with the score, a contact sheet every half second, full-resolution keyframes, matched-pair comparisons against the reference, a table of the three worst moments and their fixes, and a scored rubric with a "what holds it back" column.
- The loop caught: double exposure at scene boundaries, motion blur that smeared content, frames that depended on render history, and a notice that would have shown an absolute local path in frame (hence an automated check).

*Doctrine:* [visual-motion-direction.md](visual-motion-direction.md).

## MeowDisplay

MeowDisplay turns an iPhone or iPad into a display for a Mac and a way to control it.

**1. Exact platform, base, and branch constraints.** Apple-platform work depends on specifics an agent cannot guess: toolchain and deployment targets, how the project file is generated, which branch is the base. Prompts that stated them avoided plausible but wrong builds. *Doctrine:* pin facts; never assume the agent's environment.

**2. Cloud builds versus real-device validation.** A cloud build proves that the code compiles and tests pass on a runner. It does not prove touch, gestures, pairing, or performance on a real iPhone. Reports kept the two apart. *Doctrine:* the evidence ladder.

**3. Release artifacts, privacy, and provenance.** Release verification covered the artifact itself (the privacy manifest present in the archive), required secrets kept out of prompts and logs, rollback steps, and the provenance of bundled assets and dependencies. The binary-upload lane was separate from metadata, screenshots, submission, and release, each a distinct authority. *Doctrine:* release mode and store releases.

**4. Real store screenshots.** Store screenshots had to be real captures of the real app on the required device classes with neutral data, maintained deliberately rather than generated. *Doctrine:* no fake product UI; capture hygiene.

**5. From a static explainer to a product premise.** An early cinematic piece of about 33 seconds was a static feature explainer and was rejected. The stronger version ran roughly 12 to 20 seconds around one premise, controlling a Mac from an iPhone. Real behavior supplied the choreography: an actual Direct Touch interaction on a calculator and actual Control Tray actions. The phone became the active hero, landscape composition became structural, supporting shots were reorganized around the premise, and the music and effects were original or synthesized rather than borrowed from references. The lesson is not the storyboard; it is that factual product behavior should generate the story. *Doctrine:* product truth first; premise before polish.

## Through-lines

- State identity and authority as invariants and boundaries; leave the design to the agent.
- Separate what was verified from what was claimed, and keep the remaining human checks explicit.
- Keep reserved actions (merge, tag, publish, upload, close) separate from implementation.
- Let the real product drive the story, and run a visual critique loop before the final render.
