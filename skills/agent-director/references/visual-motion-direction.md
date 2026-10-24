# Visual and motion direction

Directing agents that produce films, reels, demos, and other time-based visuals. The prompt is only part of the result. The production harness, the deterministic renderer, the real assets, and the visual critique loop matter more than adjectives.

## Contents
- What the prompt must carry
- Order of work
- Product truth
- Capture hygiene
- Deterministic timeline
- Craft heuristics for a reel
- Defaults to avoid
- Creative freedom and its limits
- The critique loop
- Audio
- Formats as compositions
- Deliverables
- Isolation

## What the prompt must carry

Spend words on: the product truth the film must prove; where the real assets live and how to capture more; the harness requirements (determinism, reproducibility, review artifacts); the references and their jobs ([references-and-assets.md](references-and-assets.md)); the limits (no fake UI, privacy, rights); the deliverables. Spend few words on mood adjectives. Inside those limits, give strong directorial freedom.

## Order of work

product truth, then premise, then states, then shot sequence, then motion language, then audio, then polish.

Story comes before polish. A beautiful render of the wrong film is the most expensive result.

## Product truth

Start from what the product actually does:
- What must a viewer understand afterward?
- Which real UI or state proves each point?
- What sequence of states forms a story?
- Which shots require genuine capture, and which elements can be generated graphically around real UI?

Rules:
- Use real product UI. Never invent screens for final marketing assets.
- Temporary placeholders are acceptable only when final captures are intentionally replaceable, listed, and replaced before delivery.
- Recapture when the implementation changed. Keep captures replaceable until the product state is frozen, and record the product commit each capture came from.
- A screensaver or effect montage can support a product reel. It does not replace showing the product unless the product itself is the visual effect.
- Let factual behavior generate the story. When a first cut is a static feature tour, look for the premise in what the product lets someone do.

## Capture hygiene

- Use a neutral demo identity for user, host, repository, and project names.
- Remove personal data; hide secrets, usernames, and local paths; keep unrelated desktop content out of frame.
- Avoid stale UI; capture from the current build.
- Record in the real host or device the product runs in, at a fixed high resolution and scale, with stable fonts and settings, and script the interactions where possible so takes are repeatable.
- Add an automated scan of footage, stills, and text for local paths, usernames, hostnames, emails, and tokens, and run it before every review and delivery. Cut or fix any shot that would show one (a notice that prints an absolute path, for example).

## Deterministic timeline

Build the film on a pure function of time: `draw(t)` or `seek(t)`, or the framework's equivalent. In render mode:
- no unseeded random numbers (`Math.random` and similar)
- no uncontrolled CSS transitions or animations
- no timers as the source of truth
- no state carried between frames
- procedural noise only from seeded generators
- frame `t` is reproducible regardless of render order or history

Verify rather than assume: render the same frame twice and compare; render frames out of order and compare; render in a fresh process and compare. Watch for hidden history, such as glyph or texture caches whose contents depend on what rendered earlier; warm them in a fixed order or avoid them.

Choose the stack by fit: Remotion, HTML/Canvas/SVG, Three.js, Playwright with ffmpeg, or a combination. Do not mandate a framework without a reason in the prompt. Prefer one continuous camera over dissolves between scenes (disjoint content layers avoid double exposure at boundaries). Apply motion blur by averaging camera time only, so content stays crisp where it should snap.

## Craft heuristics for a reel

- A hook in the first one to two seconds.
- One clear idea per beat or section.
- Continuous visual progression, with new information or a meaningful visual change every few seconds.
- Product detail large enough to read at the intended viewing size (test at that size).
- Controlled depth, bloom, and glow.
- No camera motion without a reason.
- Transitions motivated by the product or the story.
- Actual feature choreography: the real interaction, in order.
- A strong ending or lockup without an overlong logo hold.

A product reel typically runs roughly 12 to 25 seconds. A longer cut needs a reason.

## Defaults to avoid

- a centered title on a generic gradient
- everything fading in
- endless floating glass cards
- decorative particle bursts
- excessive cyan and purple glow
- glow on every UI edge
- fake dashboards
- abstract cyberpunk filler
- effects unrelated to product behavior
- corner-label template aesthetics
- a montage with no narrative

## Creative freedom and its limits

Give the agent real directorial authority. It may restructure the story, shorten weak sections, rewrite supporting copy, reorder shots, invent transitions and motion choreography, emphasize better proof points, and design sound cues.

It may not fabricate product features, invent fake UI, misrepresent capability, reuse unlicensed reference material, or violate brand constraints (including the product's real mascot or logo design).

Require a short summary of any substantial departure from the brief. Do not reduce a strong creative agent to animating a storyboard when a better story can be derived from the real product.

## The critique loop

Before any full render, the agent must look at its own frames. The pipeline:
1. Inspect the product, assets, and references.
2. Define the story and premise.
3. Define the state list.
4. Build the shot list against the timing and beat structure.
5. Render keyframes, a contact sheet, and an animatic with the score.
6. Look at them (open the images; do not assume).
7. Score against explicit criteria.
8. Repair the worst problems.
9. Repeat until the scores stop moving.
10. Render the full film.
11. Inspect the final output again.

The review packet: an animatic with audio; a contact sheet at a fixed interval (about every half second); full-resolution keyframes at the key beats; matched-pair comparisons against the reference where a quality bar exists; and a table of the worst moments with the fix for each.

Criteria: hook; readability at the intended display size; product truth; composition; hierarchy; motion quality; variety; pacing; brand accuracy; transition quality; sound sync; ending strength. Score each (1 to 10, for example) with a "what holds it back" note, and gate the full render on the result. A model must not declare "looks good" without having looked at rendered frames when tools make inspection possible.

Expect a creative reset. A first animatic may show that the premise is wrong. Keep the brief's product constraints, drop the superseded direction, and say which is which.

## Audio

Decide the source: a supplied track, a licensed track, an original or synthesized score, or silence. Prefer supplied, licensed, or original material.

If music exists: measure the beat structure where useful; align major transitions to it on purpose; put sound effects on meaningful product interactions; keep the score on the same timeline as the visuals so edit and sound cannot drift. Treat reference audio as inspiration only, and never rip audio from a reference.

## Formats as compositions

Treat 16:9, 4:5, 1:1, and 9:16 as separate compositions, not crops. Use layout functions or format-aware framing, and reframe typography, UI scale, device placement, camera crop, and safe areas for each. Crop a landscape master only when quality does not matter.

## Deliverables

Specify them in the prompt:
- the master render and each requested format
- the contact sheet, keyframes, and the critique record
- the poster frame
- the source project with a documented render command and pinned versions
- the list of captures, with the product commit and whether each is final
- audio provenance and rights
- the leak-scan result
- the creative-departures summary
- confirmation that no placeholder remains

## Isolation

Do the work in an isolated sibling worktree or project so rendering code, captures, and large assets cannot dirty the primary product checkout ([coding-agents.md](coding-agents.md)). Reserve publishing: the agent does not upload, post, or push the film unless told to.

Example prompt: [../examples/motion-reel.md](../examples/motion-reel.md). Evidence from real reels: [case-studies.md](case-studies.md).
