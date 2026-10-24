# Agent Director

An [Agent Skill](https://agentskills.io) for directing capable coding agents across long-running projects. It plans with you, writes one paste-ready prompt, handoff, or brief for another agent session, and checks the report that comes back against the repository.

It covers implementation, continuation, fresh-session handoffs, audits, releases, design briefs, and motion work such as product showreels.

## Why it exists

Strong agents rarely fail for lack of skill. They fail on what the prompt left out or got wrong:

- a prompt written before the plan was settled
- facts taken from a stale issue checklist instead of the repository
- several references with no stated job, so the result averages them
- implementation authority quietly treated as permission to merge, tag, or publish
- green CI reported as if someone had tested the real terminal, device, or install
- a large uncommitted rewrite lost when the context ran out
- a second agent started in a checkout another agent is still using
- fake UI in a product film, and full renders made before anyone looked at a frame

Agent Director writes prompts that are exhaustive about context, goals, invariants, references, authority, and evidence, and silent about implementation details the agent can work out by reading the code.

## When to use it

Use it when you want text to hand to another agent session, or a judgment about what an agent did:

- "Give me the implementation prompt for Opus."
- "Consolidate everything we discussed into one prompt."
- "I'm out of usage. Write the handoff for a fresh session."
- "Give me a prompt to review this PR, but it must not change anything."
- "We passed QA. Give me the release prompt."
- "Turn these references into a design brief."
- "Make a 20-second showreel prompt from these captures and these two reference videos."
- Pasting an agent's final report and asking whether it holds up.

Don't use it when you want the current session to do the work itself. Fixing a bug, reviewing a file, or explaining a command needs no prompt for another agent. The skill's description says so, and in testing it did not trigger on those requests.

## What it does

Before writing, the skill reads the conversation and the repository: branch, base, HEAD, tree state, PRs, and CI where tools allow. It then names the mode and the session (fresh or same), checks whether another agent is already working on the same scope, and works out which actions are delegated and which stay with you.

The output is a session label and one fenced prompt, plus at most three lines on open decisions, assumptions, and anything it could not verify. Prompts scale with risk. A one-file fix gets two short paragraphs. A release or a terminal-lifecycle feature gets a structured brief.

While you are still planning, it keeps planning: it keeps a short ledger of decided and open questions, recommends defaults, and holds the prompt until you ask for it.

## Example: the NMSh showreel

https://github.com/user-attachments/assets/7f2cbe74-ad86-4d13-bbe3-04e334cff81b

[4K on YouTube](https://youtu.be/zIzq_88R5OI) · [X post](https://x.com/raiseCatError/status/2107187652181303325?s=20) · [notMyShell](https://github.com/raiseCatError/notMyShell). The inline player works on github.com; elsewhere, use the YouTube link.

The reel for [notMyShell](https://github.com/raiseCatError/notMyShell), a terminal frontend over a real shell, was produced by Claude Code. The skill's motion method is distilled from that work:

- **Isolation.** The film was made in a sibling checkout, so rendering code and large assets never touched the product repository while development continued.
- **Product truth before polish.** Every product shot came from takes recorded in a real terminal, built from a pinned product commit and replayed through a deterministic renderer. No screens were mocked up.
- **References with separate jobs.** One real-product launch film set how to present the product; one motion reel set density and pacing. A written study listed what to borrow (structure, rhythm) and what not to copy (each brand's palette, type, and marks).
- **The real identity.** The product's mascot kept its real design instead of becoming a generic character.
- **A review loop before the final render.** Each round produced an animatic with the score, a contact sheet every half second, full-resolution keyframes, side-by-side comparisons with the reference, a table of the three worst moments with fixes, and scores with a "what holds it back" note. The loop caught double exposures at scene boundaries, history-dependent frames, and a notice that would have shown a local path on screen.

The skill asks for the same production discipline, not the same film: [references/visual-motion-direction.md](skills/agent-director/references/visual-motion-direction.md) and the worked prompt in [examples/motion-reel.md](skills/agent-director/examples/motion-reel.md).

## How it was developed

The doctrine comes from many Claude Code and Codex sessions on two public projects, [notMyShell](https://github.com/raiseCatError/notMyShell) and [MeowDisplay](https://github.com/raiseCatError/meowdisplay). The lessons are recorded in [references/case-studies.md](skills/agent-director/references/case-studies.md). They include green CI that missed real terminal bugs, release work kept apart from implementation, parallel agents in separate worktrees, hostile-workspace security, ownership of the user config files a tool edits, and the shift from a static feature explainer to a product-premise reel.

The skill follows the [Agent Skills specification](https://agentskills.io/specification) and Anthropic's [skill authoring guidance](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices). `SKILL.md` is a short router, about 100 lines, with the most important rules first. Detail lives in reference files linked directly from it and loaded only when needed.

It was tested with headless Claude Code sessions in scratch repositories, on Sonnet, Haiku, and Opus. The scenarios covered planning, prompt writing, handoffs, report-only audits, releases, showreels, judging a fabricated agent report, a second agent arriving while another is mid-work, and prompts that should not trigger the skill. Failures found during testing were fixed and re-tested:

- taking the base branch from a stale session snapshot
- skipping the reference files
- describing code the director had not read
- accepting "CI is green, so QA is done"

The scenarios are kept in [evals/evals.json](skills/agent-director/evals/evals.json) for re-testing after edits.

## Installation

The skill is the directory `skills/agent-director/`. Every installation method puts that directory, unchanged, where an agent looks for skills.

### Claude Code

Personal installation, available in all your projects:

```bash
git clone https://github.com/raiseCatError/agent-director.git
mkdir -p ~/.claude/skills
cp -R agent-director/skills/agent-director ~/.claude/skills/
```

To pull updates with `git pull`, symlink instead of copying. Claude Code follows symlinked skill folders:

```bash
ln -s "$PWD/agent-director/skills/agent-director" ~/.claude/skills/agent-director
```

For a single project, copy it to `.claude/skills/agent-director/` in that repository. If you run Claude Code with `CLAUDE_CONFIG_DIR`, personal skills live in `$CLAUDE_CONFIG_DIR/skills/`. Claude Code picks up new skills in a running session. Check with `/skills`, or invoke it directly with `/agent-director`.

See [Extend Claude with skills](https://code.claude.com/docs/en/skills).

### Codex

Codex reads user skills from `~/.agents/skills` and repository skills from `.agents/skills`:

```bash
mkdir -p ~/.agents/skills
cp -R agent-director/skills/agent-director ~/.agents/skills/
```

See [Build skills](https://learn.chatgpt.com/docs/build-skills). The frontmatter meets Codex's documented requirements (`name` and `description`), but the skill has not been tested in Codex. Its wording assumes an agent with git and optionally `gh`, as in Claude Code.

### The `skills` CLI

[vercel-labs/skills](https://github.com/vercel-labs/skills) installs a skill into one or more agents:

```bash
npx skills add raiseCatError/agent-director -g -a claude-code
```

Omit `-a` to choose agents interactively, and `-g` to install into the current project instead. Tested with a clean home directory and no Git credentials: it copies the skill, unchanged, to `~/.claude/skills/agent-director`. If you run Claude Code with `CLAUDE_CONFIG_DIR`, check where the skill landed, or use the manual install.

### Other agents

The frontmatter uses only the spec's `name` and `description` fields, so any tool that implements the Agent Skills spec should be able to load the directory as-is. Tested so far: Claude Code with a manual install, a symlinked install, and the `skills` CLI. Codex, claude.ai uploads, and the Claude API have not been tried.

## Opinionated defaults

These reflect how the author works. Change them in `SKILL.md` and the referenced files if yours differ:

- **No AI attribution.** Generated prompts tell agents to keep the repository's Git identity and add no AI co-author trailers or "Generated with" lines. This is rule 9 in `SKILL.md`, detailed in `references/git-branches-prs-releases.md`.
- **Reserved actions.** Merge, tag, release, version bump, publish, deploy, issue closure, history rewrite, and force push stay with the user unless granted by name.
- **One primary agent.** Subagents only for independent, cheaply verified work.

## Structure

```
skills/agent-director/
├── SKILL.md            router and rules that hold in every mode
├── references/         loaded on demand
│   ├── core-method.md                    planning loop, reality checks, prompt anatomy and scaling
│   ├── coding-agents.md                  delegated vs reserved actions, parallel agents, long runs
│   ├── continuation-and-handoffs.md      fresh vs same session, reviewing returned reports
│   ├── git-branches-prs-releases.md      git hygiene, attribution, release mode
│   ├── validation-and-physical-qa.md     evidence ladder; what CI cannot prove
│   ├── audit-and-review.md               report-only and fix-mode reviews
│   ├── references-and-assets.md          giving each reference one job
│   ├── visual-motion-direction.md        films, reels, deterministic rendering, critique loop
│   ├── design-and-frontend.md            design briefs, accessibility and fallbacks
│   ├── security-provenance-and-ownership.md
│   ├── failure-handling.md
│   ├── reporting-contracts.md
│   ├── anti-patterns.md
│   └── case-studies.md
├── examples/           sample prompts: feature, continuation, handoff, audit,
│                       release, design, motion reel, small fix
└── evals/evals.json    17 behavioral and trigger scenarios
```

The examples use a fictional product, Tessera, so no real project's SHAs or versions are baked in.

## Scope

In scope: deciding when a prompt is due, writing it, and judging what comes back. It does not run or schedule agents, does not touch your repository beyond read-only inspection, and does not replace project-specific instructions such as `AGENTS.md`, `CLAUDE.md`, or your release process. Generated prompts point the agent at those files.

## Validation

```bash
python3 scripts/validate.py .
```

The validator uses only the Python standard library and runs in CI on every push. It checks:

- the frontmatter against the spec, plus Anthropic's naming rules
- that `SKILL.md` stays under 500 lines and that every reference and example file is linked from it
- that relative links resolve and code fences are balanced
- that `evals.json` parses
- that nothing looks like a secret, an absolute personal path, or an email address

Behavioral checks, meaning whether the skill does the right thing, need a model. Run the prompts in `evals/evals.json` in headless sessions against small scratch repositories shaped as described there, and grade the transcripts by hand.

## License

[MIT](LICENSE)
