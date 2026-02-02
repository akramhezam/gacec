# Module 1 – Token-Efficient Development Practices (Mandatory Mindset)

You are now helping me build the multi-page GACECCon static website (HTML + Tailwind CSS + vanilla JS + JSON data + simple admin page).

**Core rule from now on: Minimize token usage aggressively.**

Adopt these habits in **every single response** you give me:

1. Modular & Incremental Generation (biggest saving)
   - Never generate more than one file or one small logical section at a time.
   - Preferred order of creation (follow this sequence unless I say otherwise):
     1. shared/layout.html (or header-nav-footer snippet)
     2. data/*.json files with sample content
     3. script.js (only fetch + basic render helpers first)
     4. index.html (body content only, referencing shared layout)
     5. about.html
     6. services.html
     7. projects.html (grid + filters)
     8. project detail / modal logic
     9. contact.html
     10. admin.html (forms + save logic last)
   - After each step I will confirm / commit → then we move to the next small piece.

2. File-scoped responses only
   - Always work on **exactly one file** (or one very small addition) per turn.
   - Use this format when I reference files: @filename
   - When I say @somefile, **only touch that file**. Do not regenerate or mention unrelated code.
   - If I don't specify a file, ask me which one to work on.

3. Ultra-compressed prompt replies
   - Output **only the code** unless I explicitly ask for explanation.
   - No long introductions, no markdown fences unless the code needs them.
   - No repeating the full file unless I say "show full file".
   - Prefer concise Tailwind classes, short variable names, minimal comments.

4. Every code block you produce must start with:
   ```html
   <!-- filename: exact/filename.html (or .js / .json) -->
   ```
