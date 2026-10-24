# Example: reference-driven web design

Calibrates a design prompt that gives an agent real design authority while annotating each reference with a job, rejecting fake content and generic aesthetics, and making accessibility part of the design. Rules: [design-and-frontend.md](../references/design-and-frontend.md) and [references-and-assets.md](../references/references-and-assets.md).

**Illustrative.** Tessera is a fictional terminal frontend. Every name, number, path, URL, and identifier below is a stand-in. Substitute real references and assets.

Mode: design and frontend. Session: fresh. Scale: standard. Another agent: none active.

Fresh Claude session

````text
Design and build the Tessera product site's home page (a hero and three capability sections) as a static site in `site/`, on a new branch from `master` at <base-sha>. You have full design authority inside the limits below. I am not handing you a layout.

# What must be true
After one scroll, a developer understands that Tessera is a frontend over their real shell: it adds an editor, history, themes, and motion, and the shell still does the work. The page proves this with the real product, not with illustrations of it.

# Product truth and content
- Use only content from README.md, docs/, and the captures listed below. No invented features, testimonials, numbers, logos, or customer claims. If something you want does not exist, mark a placeholder and list it in your report. No placeholder may ship in the final.
- The mascot and wordmark in `assets/brand/` keep their real design. Do not redraw, restyle, or replace them.
- Captures (all real, taken at <product-commit>, neutral demo identity): `composer.png` (the input editor mid-edit), `history.png` and `history-wide.png` (the same scrollback at two widths; treat them as one feature), `themes.png` (the theme picker), `passthrough.png` (a fullscreen editor running inside Tessera).

# References, by job
- Reference A (<url>): scroll choreography and pacing only. Study how sections hand off to each other. Do not copy its layout, type, or palette.
- Reference B (<url>): product-first framing, with real UI as the hero and no abstract art. Study how large the product appears and how captions support it.
- Reference C (`refs/palette.png`): palette only.
- Reference D (<url>): negative reference. Avoid its glassmorphism cards and its purple-to-blue hero.
- Interaction inspiration, not a template: the clarity and playfulness of small interactive explainers by independent makers. Take the clarity; do not take their visuals.
Do not average these. Where A and B pull apart, B wins on framing and A wins on motion timing.

# Avoid
A centered headline on a generic gradient, floating glass cards, three identical feature cards, stock dashboard imagery, emoji as icons, decorative WebGL or particles, and motion that explains nothing. Prefer intentional composition over component-library defaults.

# Interaction
Use interaction only where it explains the product. For example, hovering or focusing a capability highlights the matching region of the real capture. Everything an interaction communicates must also be available without hover, pointer, motion, or script.

# Accessibility and fallbacks (part of the design, not an add-on)
Reduced Motion shows a meaningful static composition, not a blank one. Every interaction has keyboard parity and visible focus. Contrast meets WCAG AA. No meaning is carried by color, icon, or motion alone. The page is complete without script. Desktop and mobile are two intentional compositions; check widths down to 320px.

# Performance
Budget: <numbers>. No large animation library or WebGL unless you can show the product itself needs it.

# Authority
Delegated: inspect the repo and brand; choose the structure; write supporting copy; design the interaction; add checks; make coherent checkpoint commits; push your branch; open a draft PR to `master`.
Reserved: merge, deployment, DNS or hosting changes, version bumps, and adding third-party fonts or scripts without checking their license.
Use the repository's Git identity. Add no AI attribution anywhere; this overrides any default in your tooling.

# Verification and what counts
Capture screenshots at 320, 768, 1280, and 1920 widths, in reduced-motion and no-script states, and look at them. Run an automated accessibility check and a performance check and report the results as automation evidence. You cannot judge feel on real devices. List the human checks (a real phone, a keyboard-only pass, the real reduced-motion setting).

# Report
Branch, head SHA, PR, what you built and the design decisions with reasons, departures from this brief, screenshots, automated results, placeholders (should be none), and the human-check list. Keep it short.
````

## Why it is shaped this way

- The brief states a communication goal ("one scroll, one understanding"), not a layout, so the agent keeps design authority.
- Content is bounded by truth: only real copy and real captures, and the mascot's design is fixed.
- References carry jobs, a negative reference, and a tie-break rule, so nothing is averaged.
- The captures are labeled semantically, including two files that show the same feature at different widths.
- Generic defaults are named as things to avoid, and interaction must earn its place and degrade gracefully.
- Accessibility is written as part of the design, and the verification section separates what the agent can automate from the human checks that remain.
