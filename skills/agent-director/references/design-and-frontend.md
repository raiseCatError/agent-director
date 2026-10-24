# Design and frontend

Directing agents on product, web, and interface design. Product and brand come first; references play defined roles; accessibility is part of the architecture.

## Contents
- Start from the real product
- Briefing a design task
- Avoiding generic output
- Composition and interaction
- Accessibility and fallbacks
- Verification
- Taste lessons (history, not law)

## Start from the real product

Before any design work, the agent inspects the existing product, brand, copy, tokens, components, and screenshots. It uses real content only: no invented features, testimonials, metrics, logos, or screens. Where content does not exist, it uses clearly marked placeholders, and the prompt says when they must be replaced. The product's existing identity (mascot, wordmark, terminology) stays intact.

## Briefing a design task

Include what applies:
- audience, and the job the page or screen must do
- the content inventory (what is true and available) and the product truth to prove
- brand constraints and existing design tokens
- references by role ([references-and-assets.md](references-and-assets.md)), including a negative reference
- composition and interaction intent: what should the visitor feel and do
- technical constraints: stack, performance budget, browser and device support
- accessibility requirements (see below)
- states to cover: default, hover, focus, empty, loading, error, reduced motion, no script
- deliverables: code location and branch, screenshots at named breakpoints and states, a short rationale, departures from the brief
- authority: no publishing or deployment unless granted

Example: [../examples/visual-design.md](../examples/visual-design.md).

## Avoiding generic output

Name the defaults to avoid for this task. Common ones: purple-to-blue gradient heroes, glassmorphism card grids, a centered headline over abstract shapes, three identical feature cards, stock-dashboard imagery, emoji as icons, and decorative motion that explains nothing. Ask for intentional composition over component-library defaults, and for the product's own visual language.

## Composition and interaction

- Treat desktop and mobile as two intentional compositions, not one layout squeezed.
- Create interaction for a purpose (it explains, confirms, or delights in service of the product), not because animation is available.
- Prefer progressive enhancement: a complete page without script, then enhancement.
- Treat performance as a design constraint: weight, layout stability, interaction latency.
- Keep function and UX stronger than decorative spectacle. Heavy, gratuitous WebGL is not sophistication.
- Preserve a usable non-motion and reduced-motion state.

## Accessibility and fallbacks

Make these part of the normal architecture rather than a separate renderer wherever possible:
- Reduced Motion: meaningful, not merely "off"
- `NO_COLOR` and low-color modes
- safe or ASCII glyph modes
- keyboard parity for every pointer interaction
- visible focus
- a plain-text representation where practical
- narrow widths and resizing
- absence of optional tools or capabilities
- unsupported platform and capability states, with a tested fallback

Never let meaning depend solely on color, an icon, or motion. These apply to terminal and TUI products as much as to web pages.

## Verification

- Render and capture at the named breakpoints and states, and look at the screenshots.
- Run automated accessibility and performance checks and report them as automation evidence ([validation-and-physical-qa.md](validation-and-physical-qa.md)); they do not replace a human look.
- Test reduced-motion and no-script states, and keyboard-only navigation.
- Ask for a real-device pass when mobile feel matters, and list it as outstanding if it was not done.

## Taste lessons (history, not law)

These come from the user's own work. Treat them as lessons, not rules for every project:
- Playful, polished interaction can be valuable. The clarity and playfulness of makers such as Neal.fun or Tim Holman is something to learn from, not a template to copy.
- Heavy, gratuitous WebGL is not automatically sophistication.
- Function and UX should stay stronger than decorative spectacle.
