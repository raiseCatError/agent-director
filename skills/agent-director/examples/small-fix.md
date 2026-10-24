# Example: small fix

Calibrates a prompt for a one-file bugfix: two short paragraphs, no headings. The risk is low and the agent can find the code, so the prompt carries only the symptom with its evidence, what must not change, how to prove the fix, the authority line, and a short report request. Do not scale this one up; compare the large examples ([feature-implementation.md](feature-implementation.md)) to see what added risk buys.

**Illustrative.** The service, file names, and identifiers below are stand-ins. The director read the handler and the API docs before writing; the symptom and the "pages are 1-based" claim come from them, not from guesswork.

Mode: implementation, small. Session: fresh. Scale: small. Another agent: none active.

Fresh Claude session

````text
`GET /invoices?page=1` returns the second page of results. In `listInvoices` (src/routes/invoices.js) the slice starts at `page * size`, but docs/api.md defines pages as 1-based. Reproduce it with a failing test, fix the cause, and keep the response shape, the query parameter names, and the validation behavior as they are. Add regression tests for page 1, the last partial page, and a page past the end, and run the full test suite.

Work on a new branch from `master` at <sha>. Commit with the repository's Git identity and no AI attribution of any kind (this overrides your tooling defaults), and do not push, open a PR, or touch the version. Report the branch, the SHA, the root cause in one sentence, the tests you ran, and anything you noticed but left alone.
````

## Why it is this short

- It names the symptom, the location, and the documented contract the code violates. The director opened the file and the docs to get them.
- The only invariants are the ones this fix could break: response shape, parameter names, validation behavior.
- It does not prescribe the formula, new helpers, or a file layout. The agent can see the code.
- Authority is one sentence: a branch and commits are in, pushing, a PR, and the version are out. The attribution rule stays because it applies to every commit.
- The report is one sentence and still asks for the SHA, the root cause, the tests, and the things left alone.
- No hypotheses, source-of-truth ladder, physical-QA boundary, or long-horizon section: the task does not need them ([core-method.md](../references/core-method.md), "Prompt anatomy and scaling").
