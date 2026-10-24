# Example: same-session continuation

Calibrates a short continuation from an accepted checkpoint. The agent already knows the project, so the prompt carries only what changed, the next outcome, and what stays in force. Rules: [continuation-and-handoffs.md](../references/continuation-and-handoffs.md), "Same-session continuation".

**Illustrative.** Tessera is a fictional terminal frontend. Every name, number, and identifier below is a stand-in.

Mode: continuation after human QA. Session: same. Scale: small. Another agent: none active.

Same Claude session

````text
Checkpoint accepted at <sha> (slices 1 and 2: mark parsing and boundary tracking, navigation). Since your last report I ran the first physical pass on two hosts and found three issues:

1. After Ctrl+Z then `fg`, the next command's boundary is attributed to the suspended job.
2. Under tmux, jump-to-previous skips one command when the previous command printed no trailing newline.
3. With NO_COLOR and safe glyphs, the status glyph is invisible, so exit status has no visible form.

Next, in this order:
- Reproduce each at PTY level before changing anything, and add a regression test wherever the bug is meaningfully automatable. Tell me which ones you could not automate.
- Fix them at the right layer. For 3, status needs a text form in every glyph mode; fold that into slice 3's definition of done.
- Then continue with slice 3 (the status affordance), unless these fixes show its design must change. If so, say what and why before building.

Unchanged: invariants, non-goals, branch, and authority (still no merge, tag, or version bump). Commit each fix as its own checkpoint, push, update the draft PR, and report as before. Add which findings you reproduced automatically and which I must re-test by hand.
````

## Why it is shaped this way

- It opens with the accepted SHA and the new facts, and restates nothing the agent already holds.
- Human QA findings arrive as numbered, concrete observations. The agent reproduces them before fixing, which follows [validation-and-physical-qa.md](../references/validation-and-physical-qa.md) ("When physical QA finds a bug").
- The ordering is explicit because the fixes may change the next slice, and the agent is invited to say so.
- One "Unchanged" line stops silence from reading as revoked authority or dropped invariants.
- The report request names only the delta: which findings were reproduced automatically and which need a human re-test.
