# Example: deterministic real-product showreel

Calibrates a motion prompt: product truth first, references with separate jobs, real captures with a neutral demo identity, a deterministic timeline, a critique loop with contact sheets, audio rules, per-format compositions, and a deliverables list. Rules: [visual-motion-direction.md](../references/visual-motion-direction.md) and [references-and-assets.md](../references/references-and-assets.md).

**Illustrative.** Tessera is a fictional terminal frontend. Every name, number, path, file, and identifier below is a stand-in. Substitute the real product, captures, and references.

Mode: visual and motion. Session: fresh. Scale: large. Another agent: product development continues in the main checkout, so the work is isolated.

Fresh Claude session

````text
Direct and produce a showreel of roughly 20 seconds for Tessera from real product captures. You are the director: premise, story, shot order, motion language, and sound cues are yours to decide. The limits below are not negotiable. The film must be reproducible, and you must review its frames before the final render.

# Where to work
Work in a sibling worktree `../tessera-reel` created from `master` at <base-sha> (or a new project there). Do not modify the main checkout, where product development continues. Keep rendering code, captures, and large assets out of the product repository. Reserved: pushing, uploading, publishing, or posting the film anywhere.

# Product truth first
Before designing, run the product at <product-commit> and list its states and what each one proves. Decide what a viewer should understand after 20 seconds, and derive the premise from what the product really does. Tessera is a frontend over the user's real shell: editor, history, themes, motion, screensavers, and the product's mascot, with the shell still executing everything. Real behavior generates the story. Do not invent screens, features, or claims.
- Use genuine captures for every shot of the product. Record takes in the real terminal host the product runs in, at fixed high resolution, with scripted interactions so takes are repeatable. Record the product commit for every capture. Keep captures replaceable until I freeze the product state. No placeholder may remain in the final.
- Graphic elements may be generated around real UI (callouts, type, light). They may not stand in for it. A screensaver or effect montage may support the reel; it must not replace showing the product.
- The mascot keeps its real design (`assets/brand/`). Do not redesign it or substitute a generic one.

# Demo identity and privacy
Use a neutral identity: user `demo`, host `demo-host`, repository `example-app`. No real username, hostname, local path, email address, token, or unrelated desktop content may appear in any frame. Add an automated scan of captured text and frames, run it before every review and before delivery, and cut or re-record anything it flags.

# References, by job
- Reference A (`refs/launch-film.mp4`): how to present the real product, plainly, at readable scale, one idea per region, with a continuous camera. Borrow the grammar. Do not borrow its palette, type, wordmark treatment, or transitions.
- Reference B (`refs/motion-reel.mp4`): density and pacing, with one idea per section of about 2 seconds, cuts on the beat, and a staccato acceleration before the end. Borrow the pacing. Do not borrow its palette, typefaces, marks, or type cards.
- Reference C (`refs/palette.png`): palette hints only.
Study both films before storyboarding: sample frames at a fixed rate, detect cuts, and read the audio from the waveform and spectrogram. Write a short reference study that lists what you borrow (grammar) and what you refuse (identity). Do not clone either film or average them.

# Production harness
- Build the film on a deterministic timeline, a pure function of time (`draw(t)` or `seek(t)`, or your framework's equivalent). In render mode: no unseeded randomness, no uncontrolled CSS transitions, no timers as the source of truth, no state carried between frames, seeded noise only. Frame `t` must be reproducible regardless of render order or history. Prove it: render a frame twice, out of order, and in a fresh process, and compare.
- Pick the stack that fits (Remotion, HTML/Canvas/SVG, Three.js, Playwright with ffmpeg, or a mix) and justify it in two lines.
- Prefer one continuous camera with disjoint content layers over dissolves between scenes.

# Process (do not skip steps)
1. Product states and premise.
2. Storyboard and shot list against a beat structure.
3. Keyframes, a contact sheet every 0.5 seconds, and an animatic with the score.
4. Look at them. Score the film from 1 to 10 on hook, readability at playback size, product truth, composition, hierarchy, motion quality, variety, pacing, brand accuracy, transitions, sound sync, and ending, each with what holds it back. List the three worst moments with their fixes.
5. Repair, and repeat until the scores stop improving.
6. Only then render the full film.
7. Inspect the final output again.
The first animatic may show that the premise is wrong. If it does, say so and reset, keeping the product constraints.

# Direction, not a storyboard
You may restructure the story, cut weak sections, rewrite supporting copy, reorder shots, invent transitions and choreography, and choose proof points. You may not fabricate features, show fake UI, misrepresent capability, reuse reference material, or violate the brand constraints. Summarize any substantial departure from this brief afterward.
Craft guide: a hook in the first 1 to 2 seconds; one idea per beat; something new every few seconds; product detail large enough to read at playback size; no camera motion without a reason; motivated transitions; a short, strong ending instead of a long logo hold. Avoid a centered title on a gradient, everything fading in, floating glass cards, decorative particles, glow on every edge, fake dashboards, and a montage without a story.

# Audio
Use an original or synthesized score and effects, or silence. Do not extract audio from references. Align major transitions to the beat, put effects on real product interactions, and keep the score on the same timeline as the visuals. State what you made and what you used.

# Formats
Deliver 16:9 (master), 4:5, 1:1, and 9:16 as separate compositions, not crops. Re-lay-out type, product scale, device placement, camera framing, and safe areas per format.

# Deliverables
Masters and per-format renders; a poster frame; the contact sheet, keyframes, and the critique record; the reference study; the source project with a documented render command and pinned versions; the capture list with product commits (none a placeholder); audio provenance; the leak-scan result; the creative-departures summary.

# Report
Worktree path, branch, head SHA, files delivered, the final scores and what still holds the film back, the determinism checks you ran, the leak-scan result, what you could not judge (feel on real displays; list the human checks), and the exact next action. No recap.
````

## Why it is shaped this way

- The harness requirements (determinism, privacy scan, review artifacts, gated render) take more words than style direction, because they decide the result ([visual-motion-direction.md](../references/visual-motion-direction.md)).
- Product truth comes first, so the premise is derived from real behavior instead of imposed.
- Each reference has one job, plus explicit "borrow" and "refuse" lists. The agent studies them by method (sampled frames, scene cuts, audio read from waveform) and records the result.
- The critique loop is a required process with scores and a worst-moments list, and the full render is gated on it.
- Creative freedom is explicit, with a small set of hard limits and a request to summarize departures.
- Isolation, reserved publishing, and the deliverables list are all in the prompt so nothing is left to inference.
- A real reel will also need real asset paths and an exact beat plan. Fill those from the live project; do not copy these placeholders.
