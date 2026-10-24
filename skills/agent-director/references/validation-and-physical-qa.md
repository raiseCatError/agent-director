# Validation and physical QA

What to demand as evidence, and where automation stops. The governing rule: claim only the evidence actually reached.

## Contents
- The evidence ladder
- What automation commonly misses
- Test discipline
- Tests are not the specification
- Terminal and PTY software
- The physical-QA protocol
- Wording blocks

## The evidence ladder

Six rungs, from cheapest to strongest. A claim may be made only up to the highest rung actually reached.

| Rung | Proves | Does not prove |
|---|---|---|
| 1. Unit or integration test | The logic and contract under test, on the test host | Behavior on real terminals, devices, or installs |
| 2. Simulated fixture or mocked platform | Handling of recorded or synthetic inputs | That the real platform behaves like the fixture |
| 3. CI platform run | Build and tests on independent runners and OS images | The user's machine, terminal host, hardware, or feel |
| 4. Real application, terminal, or device, driven for real | Behavior in that real host | Other hosts; the packaged install |
| 5. Real packaged install through the public path | PATH, environment, packaging, upgrade | Human judgment |
| 6. Human visual or tactile judgment | Feel, readability, taste, whether it works for a person | Exhaustive regression |

Rungs 4 to 6 are **physical QA**. Never write "fully verified" while a higher rung relevant to the change is outstanding. Never present a mocked platform behavior as real platform validation. CI is rung 3, not physical QA.

When the user says "CI is green, so QA is done", treat it as an inference to correct, not a fact to record. Say in one line that CI is not physical QA, ask whether a human pass on a real host or install has happened, and mark physical QA outstanding until it has.

## What automation commonly misses

- the real executable's PATH and install environment
- terminal rendering edge cases
- key routing, for example Ctrl+Z and other job-control keys
- selection and mouse ownership
- real fullscreen and passthrough behavior
- viewport feel
- real-device UI
- window-manager and terminal-host behavior

For each change, ask which of these it could affect and put them on the physical list.

## Test discipline

Ask for, in proportion to the change:
- focused tests while implementing a slice
- the project's full canonical verification at every durable checkpoint, before push
- build and typecheck where the project has them
- diff checks (whitespace and conflict markers)
- compatibility tests across supported shells, platforms, or versions
- targeted regression tests for every defect fixed
- packaging and install tests whenever packaging changed
- documentation, link, and asset checks whenever docs or assets changed

Point the agent at the project's own verification entry points rather than naming commands the director has not verified. The agent discovers them in the repository (contributor docs, scripts, CI configuration).

## Tests are not the specification

- Treat a failing test as information first, and classify it before changing anything ([failure-handling.md](failure-handling.md)).
- Do not weaken a legitimate test to get green.
- Do not hard-code current fixtures into production behavior.
- Do not bend intentional product behavior to satisfy a stale snapshot.
- Specify behavior in the prompt through outcomes and invariants; let tests prove them.

## Terminal and PTY software

For terminal frontends and anything that wraps a shell:
- drive a real PTY with a real shell in tests, and assert on emitted bytes and escape sequences as well as internal state
- cover the lifecycle: start, resize, suspend and resume (Ctrl+Z, `fg`), foreground-application handoff, exit, crash, signals, orphaned processes
- cover each supported shell backend
- clean up child processes and temporary config directories in every test
- test with untrusted output on the stream ([security-provenance-and-ownership.md](security-provenance-and-ownership.md))

## The physical-QA protocol

Automate aggressively first. Then ask for one consolidated human pass at a meaningful milestone (release candidate, presentation, end of a feature program), not after every small patch.

Ask the agent to produce the checklist for that pass:
- a host and shell matrix (terminal emulators, OS versions, devices, shells)
- exact steps and the expected result for each
- what to record on failure (host, version, steps, screen capture, logs)
- which items are blockers and which are observations

When physical QA finds a bug:
1. reproduce it at the lowest automatable level
2. add a regression test when the bug is meaningfully automatable (a PTY-level test for a key-routing bug, for instance)
3. fix at the right layer
4. record any bug that cannot be automated, so the next human pass re-checks it

Track the state honestly. Where the project has a "needs human test" status, set it; do not close work that requires human validation until the validation has occurred.

## Wording blocks

**Physical-QA boundary**
> You cannot verify <list: real terminal hosts, key feel, fullscreen apps, ssh or tmux, the packaged install>. Do not claim them. Cover what can be automated (PTY-level tests, fixtures) and finish with a physical-QA checklist: host and shell matrix, exact steps, expected results. Report separately what you verified and what still needs a human.

**Honest status**
> State each check as one of: verified (how), reported only, not run (why), or requires human (exact steps).
