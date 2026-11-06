# AAZHI — setup for new creators

This gets your Claude Code working exactly like Ananthu's: the same characters and IDs, the same rules, the same agents, and one shared set of learnings. Anything you make or learn is pushed to `main` and is available to everyone straight away.

## One-time setup

1. **Repo access.** Send Ananthu your GitHub username and accept the invite to `ananthuvj99/Aazhi-bible` (you need write access to push).
2. **Install Claude Code** from Anthropic's documentation at code.claude.com/docs.
3. **Get the repo:**

   ```
   git clone https://github.com/ananthuvj99/Aazhi-bible.git
   cd Aazhi-bible
   git config user.name "<Your Name>"
   ```

   The name you set is how Claude credits every character, location and lesson you add, so use your real name. Everyone works directly on `main`; there is no branch to make (own-branch mode is optional, see `CLAUDE.md`).

   **Sign in to GitHub so Claude can push for you.** Either install the GitHub CLI and run `gh auth login --web` then `gh auth setup-git` (you approve in the browser, no token to copy), or use your own fine-grained token (this repo only, Contents read/write). Never paste a token into a chat.

4. **Start Claude Code inside the folder** by running `claude`. It reads `CLAUDE.md` and loads the shared agents from `.claude/skills/` automatically. When it asks whether to trust the folder and use the project's Higgsfield server, say yes, and sign in with your own Higgsfield account when the browser opens. If Higgsfield doesn't appear, run:

   ```
   claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp
   ```

5. **Platform.** Use your own account on the Techjays film platform. Every reference you upload there uses exactly its ID from `INDEX.md`.

## Your first message in every session

```
Read CLAUDE.md and follow it for this whole session. Pull main, read INDEX.md and learnings/INDEX.md, then tell me what changed since my last session.
```

## Every shot

1. Describe the scene and attach any references you have.
2. Claude gives you a breakdown: what each shot needs, what already exists (whoever made it), and what is missing.
3. Approve or reject any new image Claude makes. Upload approved images to the platform under their IDs.
4. Claude writes the prompt, runs the continuity and QA checks, fixes small things itself and asks you about bigger ones.
5. Copy the final prompt, attach the listed IDs, and generate.
6. Report back:
   - **Good take:** say so and what you liked. Claude records it as a win.
   - **Bad take:** send the first, middle and last frames, the issue category and one line on what's wrong. Claude records the lesson and fixes the prompt.
7. For the next shot, upload the last frame of the approved take, or ask Claude to help place the characters.

Issue categories: position, elements, characters, sizes, angles, in-frame, dialogue, timing, light, platform.

## Adding a character, location or prop

Give Claude the sheet and say who or what it is and which look. Claude checks `INDEX.md` first. If it's new, Claude makes its folder (for example `characters/claramother/`), writes the card with your name as creator, and adds the `INDEX.md` row, then pushes to `main` — from then on everyone's Claude can use it.

## The agents

All of them live in the repo under `.claude/skills/`:

| Agent | What it does |
|---|---|
| `aazhi-scene-breakdown` | Lists every reference each shot needs, reuses existing assets, flags what's missing |
| `seedance-2-5-prompt-writer` | Writes the prompt in Seedance 2.5 format |
| `aazhi-continuity-director` | Checks the prompt against everything already locked, with director's notes |
| `aazhi-prompt-qa` | Checks the prompt against your request and the reference IDs, scores it out of 100 |
| `aazhi-malayalam-dialogue` | Turns dictated lines into natural spoken coastal Malayalam |

Online: github.com/ananthuvj99/Aazhi-bible/tree/main/.claude/skills

## Seeing who did what, and undoing it

- Ask Claude "show activity" (or run `bash tools/activity.sh`) for every change on every branch: who, when, what, and a commit code.
- To undo a change, give Claude its commit code; Claude reverts it on `main` with a new commit (history is never erased). Anyone can undo their own work; undoing someone else's needs that creator (or Ananthu) to agree first.
- Assets that any shot has used are never deleted, only marked retired.

## Rules everyone keeps

- Everyone pushes straight to `main` after every piece of feedback: pull first, never force-push, and on a conflict keep both sides. Work on your own shots; editing someone else's approved shot needs their agreement.
- Never paste an access token into a chat or commit one to the repo.
- Dialogue in Malayalam only, with one emotion for the whole scene.
- New assets are saved once you approve the image, and pushed to `main` straight away. Changing or removing an existing rule needs that rule's creator (or Ananthu) to agree first.

Questions go to Ananthu.
