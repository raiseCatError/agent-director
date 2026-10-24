# References and assets

How to hand an agent references and assets so that each one does exactly one job.

## Contents
- Annotating a reference
- Reference types and authority
- Separate jobs, no averaging
- Borrowed grammar and withheld identity
- Labeling images, video, and audio
- Telling the agent how to inspect
- Assets and their handling

## Annotating a reference

For each meaningful reference, write:

```
Reference:                 <name, path, or URL>
Type:                      <see the table below>
Authority:                 <normative | implementation | behavior | inspiration | negative | compatibility | provenance>
Use for:                   <the one or two things it informs>
Do not copy:               <what must not carry over>
Specific details to study: <timestamps, sections, screens, components>
Details to ignore:         <...>
Licensing/provenance:      <license, reuse class, notices>
Expected inspection method: <how the agent should look at it>
```

Skip fields that add nothing. A reference with no stated job invites the agent to imitate everything.

## Reference types and authority

| Type | Meaning |
|---|---|
| Source of truth (normative) | Defines required behavior; conflicts are resolved in its favor |
| Architecture reference | Explains accepted structure and boundaries |
| Behavior reference | Shows how a real product or protocol behaves; study it, do not assume equivalence |
| Implementation reference | Shows how something was built; adapt ideas, subject to licensing |
| Compatibility reference | Defines what must keep working (versions, shells, platforms) |
| Visual or motion reference | Inspiration for look, pacing, and framing; never a template |
| Palette, typography, or framing reference | Inspiration for one named dimension only |
| Negative reference | Shows what to avoid, with the reason |
| Licensing or provenance reference | Governs what may be reused and which notices to keep |

Never silently treat inspiration as specification. Say which reference wins when two disagree.

## Separate jobs, no averaging

Give each reference its own job. Do not ask the agent to blend unrelated references into an average.

> Reference A: motion density and transitions only.
> Reference B: product-first framing: real UI as the hero.
> Reference C: palette only.
> Reference D: negative reference: avoid its glassmorphism and its layout.

If two references pull in opposite directions, decide for the agent which dimension each controls.

## Borrowed grammar and withheld identity

For visual and motion references, split the analysis into what the work borrows and what it must not:
- **Borrowed (grammar):** structural devices such as one idea per section, cuts on the beat, real UI at a readable scale, a continuous camera as connective tissue, a bookended open and close.
- **Not borrowed (identity):** another brand's palette, typefaces, marks, signature transitions, type cards, and layouts.

Write both lists into the prompt, or require the agent to produce them from its inspection before building. Do not clone another brand's film or site.

## Labeling images, video, and audio

The agent will not infer your taxonomy.
- Label every supplied image or clip with what it shows and the role it plays ("Images 1 to 3: the same feature in three states; treat them as one feature, not three").
- When two similar images represent the same thing, say so.
- Distinguish final assets from placeholders, and current product states from stale ones.
- Say which items are references to study and which are assets to ship.

## Telling the agent how to inspect

Name the method when a reference needs more than a glance:
- video: sample frames at a stated rate, detect scene cuts, read audio from the waveform or spectrogram
- images: open each one; extract the palette; measure proportions
- specs and docs: read the named sections; run the examples
- upstream projects: read the source under the stated reuse class; run it in a sandbox, never in the primary checkout
- live products: use them and note the exact behavior and timing

Ask the agent to record its findings (a short reference study, for instance) when later work depends on them.

## Assets and their handling

- State where assets live, who owns them, and their licenses.
- Keep third-party media out of the repository unless the license allows it and the notice is preserved.
- Mark placeholders explicitly and say when they must be replaced; for final marketing material, no placeholder may remain.
- Keep personal data out of captures and assets (names, paths, hostnames, accounts); see [visual-motion-direction.md](visual-motion-direction.md), section "Capture hygiene".
- Prefer supplied, licensed, or original audio. Do not extract audio from a visual reference.
- Reuse classes and license checks: [security-provenance-and-ownership.md](security-provenance-and-ownership.md).
