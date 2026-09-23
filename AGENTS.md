# AGENTS.md

Repo-specific notes for agents working on the *Biquaternion Universe* article series.

## Layout and build

- `articles/*.md` ‚Äî the articles; each is auto-discovered by `build.py` (no registration needed).
- `physics.md`, `maths.md`, `index.md` ‚Äî listing pages. Their entries are **hand-written**:
  adding an article means adding its `<a href="articles/‚Ä¶‚Äã.html">Title</a>` line by hand, in the
  intended reading order. The filename stem must match the link exactly.
- `build.py` ‚Äî builds into `../ai-research-unit-deploy`. Requires `markdown`. Exits 0 on success and
  prunes orphaned HTML, so a renamed article cleans up after itself.
- `build.py` masks `$$‚Ä¶$$` and `$‚Ä¶$` with placeholders before Python-Markdown runs, then restores
  them verbatim. KaTeX (0.16.9, via CDN) renders client-side.

- `articles/the-quaternion-and-antiquaternion-subspaces.md` is the quaternion/antiquaternion
  subspace article. Its title deliberately drops "in the Biquaternion Universe" (its siblings keep
  it), and inside it the `### Definition and Basis` / `### Properties` pair repeats once per half.
  That duplication is intended, mirroring the per-subspace structure of `m-plus-as-...`.
- The sector articles are titled with **subspace**: `m-as-the-material-subspace.md`
  (`$\mathbb{M}_-$ as the Material Subspace`) and `m-plus-as-the-informational-subspace.md`
  (`$\mathbb{M}_+$ as the Informational Subspace`). They were renamed from `...-space`; the **title
  string** "as the Material Space"/"as the Informational Space" appears as a cross-reference in ~100
  articles each, so renaming again means a corpus-wide string replacement. Only the capitalized
  title phrases are references — lowercase prose like "identified M- as the material space"
  describes the interpretation and must **not** be rewritten.
- `articles/*.thinking` and `*.suggestions` are append-only phase logs, not content: never rewrite
  them when propagating a rename.

## Division of labour: conventions vs. the matrix article

`conventions-in-the-biquaternion-universe.md` is the series' **notation authority** (31
`_reserve/SUBAGENT-*.md` briefs call it "the authority for every convention" and cite its sections
by name, so its filename and section names are effectively frozen). It covers **notation, why the
notation is what it is, and how to avoid the mistakes that notation invites** — not derivations.

`the-matrix-representation-in-the-biquaternion-universe.md` holds the matrix **development**: the
general element, the four subspaces as matrices, the conjugations in matrix form, the trace and
the determinant, the ideals as columns, the spin/qubit reading and the groups.

- Do not grow the matrix material in `conventions-...` back. It keeps only: the four basis images
  (they are a convention), the reason they are forced, the one-rule-`Φ` reservation, the
  never-conjugate-entries warning, the unitary-presentation statement, and the `Tr(e_0) = 2`
  normalisation with its must-not-drop-the-factor-2 warning. Everything else points to the matrix
  article.

## Pauli matrices in the matrix article

- The Pauli matrices appear **only in the remark of `## The Representation`** (plus a bibliography
  citation in *Further Reading*). Everywhere else the article writes the algebra's own images:
  $\Phi(e_\mu)$ for the basis and $\Phi(ie_k) = i\,\Phi(e_k)$ where a physicist would reach for
  $\sigma_k$. This is deliberate — the article is about $\Phi$, not about the Pauli algebra — and
  a reviewer must not reintroduce $\sigma_k$ into the exposition.

## Presenting the four subspaces

The four subspaces are $\mathbb{M}_-$ (material), $\mathbb{M}_+$ (informational),
$\mathbb{H}_{\mathbb{B}}$ (quaternion) and $i\mathbb{H}_{\mathbb{B}}$ (antiquaternion); the center
$\mathbb{C}_{\mathbb{B}}$ is a fifth, two-dimensional fixed space and is kept apart from the four.

- Each of the four gets its **own part** with its **own explicit matrix**, written from
  $\Phi(e_\mu)$ with no Pauli matrix, in the order $\mathbb{M}_-$, $\mathbb{M}_+$,
  $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, plus $\mathbb{C}_{\mathbb{B}}$ and a
  closing "How the Four Fit Together". Each part carries: the defining involution, the real
  parameters, the basis and its explicit basis images, the general element's matrix, and the
  determinant with its signature. Do not regroup them by pair (the "halves"
  $\mathbb{H}_{\mathbb{B}}$/$i\mathbb{H}_{\mathbb{B}}$ against the "sectors"
  $\mathbb{M}_-$/$\mathbb{M}_+$) and do not re-list them a second time under a different grouping:
  that is what made these two articles messy before. (In `conventions-...` the four get one
  compact part each, framed as the *parametrisation* convention rather than as matrices.)
- The **relations** between the four — the crossing of the two splits, intersections, spans,
  gradings, norm-form definiteness, subalgebra-vs-module — belong to
  `the-quaternion-and-antiquaternion-subspaces.md`. These articles keep only what a reader
  needs to *parse* the rest (the prime pattern, the naming of material vs informational, and the one
  crossing statement that the prime pattern depends on), and point to the dedicated article for the
  rest. Keep that pointer intact: `m-as-the-material-subspace.md` cites "the conventions article"
  for the crossing, so the crossing statement must stay there in some form.

## The intersections section of the subspaces article

User requirements for `the-quaternion-and-antiquaternion-subspaces.md` (stated explicitly; do not
regress them):

- **Define before tabulating.** Open with the definition of intersection as a set,
  `A n B = {Q : Q in A and Q in B}`, note it is a subspace, then *derive* the one-line rule — every
  element has a unique expansion into the four blocks, and a sum of blocks contains an element iff
  it contains each of its block components, so `A n B` is the sum of the shared blocks. Do not open
  with the assertion "the intersection is the sum of the blocks they share" and leave it unproved.
- **Each intersection gets a real `###` heading, plus an italic subtitle.** A bold run-in lead
  ("`**$M_- \cap H_B = X_m$.** ...`") was rejected: "the intersections are not well commented, no
  title or subtitle". The convention, matching the companion articles' `### The Material Sector
  $M_-$` style:

  ```
  ### $\mathbb{M}_- \cap \mathbb{H}_{\mathbb{B}} = X_{\mathrm{m}}$

  *Dimension $3$ — the space that the material sector and the quaternion half hold in common.*
  ```

  Title = the intersection itself (so it can be scanned for). Subtitle = dimension plus a one-line
  meaning. The equation must render inline, so it is the actual heading text; the subtitle is a
  separate italic line after a blank line. Known cosmetic artifact: because math is masked with NUL
  placeholders before Markdown runs, these headings get ids like `math427` instead of a slug of the
  text. Harmless (no per-article TOC is displayed); if deep links ever matter, switch to a text
  title with the equation in the subtitle.
- **The other commentary paragraphs in that section are `###` too**, not bold leads: "Why the table
  has this shape", "Each half is assembled from one piece of each sector", "A common line is shared
  by triples, not pairs". The orphan sentence "Each intersection is taken in turn." was deleted as
  superseded by the headings.
- **One FULL paragraph per intersection** (all six pairs). The user rejected brief entries here
  explicitly ("MORE DETAILS FULL PARAGRAPHS EACH").
- **Inside each intersection paragraph, use short bold run-in leads.** A wall of unbroken prose was
  rejected ("the intersections are not well commented"). Each paragraph carries 2–5 titles so the
  argument can be skimmed, in the article's existing run-in style (`**Hence the intersection of two
  subspaces is the sum of the blocks they share**`). Current titles, in order: The eigenvalue
  argument / In blocks / Directness / Physical content (M−∩M+); The other generator / In blocks /
  Directness / Why exactly two zeros (H_B∩iH_B); The constraint / The largest intersection / Pure
  quaternions / Norm form and matrix image / Two further remarks (M−∩H_B); The constraint / Three
  features distinguish it + bolded First, Second, Third (M−∩iH_B); The constraint / The vacuum
  direction / The asymmetry (M+∩H_B); The constraint / Observables / Pairing under $i$ / Crossing of
  the splits / The pattern (M+∩iH_B). Keep this layering: `###` heading + italic subtitle + bold
  run-in leads inside the prose. Each paragraph gives: the two defining conditions
  on the coefficients; which coefficients therefore vanish and which survive; the intersection in
  display math with an explicit basis; the dimension and whether it is \(0\), \(1\) or \(3\); the
  norm-form sign; the matrix image under $\Phi$; the involution/centrality remarks where relevant;
  and the physical reading. The four nonzero cases close with the pairing under multiplication by
  $i$: $i(\mathbb{M}_- \cap \mathbb{H}_{\mathbb{B}}) = \mathbb{M}_+ \cap i\mathbb{H}_{\mathbb{B}}$
  and $i(\mathbb{M}_- \cap i\mathbb{H}_{\mathbb{B}}) = \mathbb{M}_+ \cap \mathbb{H}_{\mathbb{B}}$.
- **Every table is a Markdown table. Do not use LaTeX `array` for tables.** This was tried and
  reverted. The array was adopted at one point because the user liked the crossing rules (a
  horizontal `\hline` meeting the vertical column separator `|`), and the two-by-two grid was written
  as `\begin{array}{c|cc}` with `\substack` cells. The user then asked why the intersection tables
  could not use the same format as *Summary of Notation*, "and the inside is full of formulas" —
  because that table renders fine with formulas in it. The resolution: use Markdown tables
  everywhere, and get the ruled look from CSS instead.

  Why the array lost:
  - A KaTeX `array` is a **display math object, not a `<table>`**. No `<th>`/`<td>`, no row/column
    semantics, nothing for a screen reader to announce — wrong markup for a data table.
  - It **cannot wrap text**. `p{}`, `\parbox`, `\makecell`, `\shortstack` are all unsupported, so
    any cell long enough to need wrapping overflows. Markdown cells wrap freely.
  - It is **centred** (display math) and uses **KaTeX's own black rules**, so it did not match the
    other tables and ignored the site stylesheet.
  - The only thing it bought was the crossing rules — and CSS reproduces those.

  The difference is easy to miss because the Markdown tables are now *bordered*, so they look like
  arrays. That resemblance caused real confusion: "Summary of Notation" was read as an array when it
  is an ordinary Markdown table whose cells hold *inline* math. Inline math is just text and wraps;
  a display `array` does not. When explaining, name the formats explicitly rather than pointing at
  how they look.

  The grid keeps T and X inside each cell via `<br>`, which works fine in a Markdown cell:

  ```markdown
  | | material space $X_{\mathrm{m}}$ | informational space $X_{\mathrm{i}}$ |
  |---|---|---|
  | **material time** $T_{\mathrm{m}}$ | $\mathbb{M}_-$<br>$(T_{\mathrm{m}},\,X_{\mathrm{m}})$ | $i\mathbb{H}_{\mathbb{B}}$<br>$(T_{\mathrm{m}},\,X_{\mathrm{i}})$ |
  | **informational time** $T_{\mathrm{i}}$ | $\mathbb{H}_{\mathbb{B}}$<br>$(T_{\mathrm{i}},\,X_{\mathrm{m}})$ | $\mathbb{M}_+$<br>$(T_{\mathrm{i}},\,X_{\mathrm{i}})$ |
  ```

  Rows are the temporal blocks, columns the spatial ones, and each cell carries the subspace with its
  two blocks — T and X shown *at the intersection*. Same row → shared time → dimension 1; same column
  → shared space → dimension 3; differing in both → 0. The two zeros are the two splits, which are the
  two diagonals. This is what makes the dimensions $\{0,1,3\}$ rather than any of $2$ or $4$.
- **Markdown tables are styled by `assets/css/article.css`**, so all nine tables in the article look
  alike. Before this the site had *no* table CSS at all, which is part of why the unstyled Markdown
  grid looked so poor next to the bordered array. This CSS is also what makes the all-Markdown
  approach viable — without it the tables would be unruled.
- **Tables are wrapped in `<div class="table-scroll">` by `build.py`.** A `<table>` cannot clip its
  own overflow, and `display:block` + `overflow-x:auto` on the table does not contain the scroll in
  Chrome (the anonymous table box escapes), which gave the page a horizontal scrollbar on mobile.
  The wrapper needs `contain: paint` as well — without it Chrome still counts the table's overflow
  in the document's scrollable area even though the wrapper clips. Verified: no page-level
  horizontal scroll, wrapper scrolls internally.
- **The all-Markdown rule extends to the whole corpus.** 13 grid tables in 8 other articles were
  converted from `array` to Markdown tables, so the series no longer mixes the two formats:
  `canonical-quantization-of-the-biquaternion-rarita-schwinger-field`,
  `contextuality-and-the-kochen-specker-theorem-in-biquaternionic-form` (the Mermin–Peres square),
  `frame-dependent-entanglement-...`, `grand-unification-...`,
  `quantum-error-correction-and-the-stabilizer-formalism-...`,
  `spin-entropy-and-the-lorentz-group-...` (four tables), `superdense-coding-...`,
  `the-wigner-rotation-...` (two tables). Three `array` blocks were **deliberately left alone**
  because they are equation layout, not grids: two in `bilinear-and-quadratic-forms.md` (stacked
  text over a `\longleftrightarrow`) and one in `the-newman-penrose-formalism-...` (an aligned list
  of PND conditions). The test for "is this a table" is a rule in the column spec or a `\hline` —
  no rules means it is a formula.
- **A converted table needs a blank line on each side.** The `$$` block it replaces sat between two
  blank lines, but the replacement text does not inherit them: drop straight into
  `... function is` + `| header |` and Python-Markdown sees paragraph continuation, so the whole
  table renders as literal pipe characters in the prose. This failed silently — build exit 0, zero
  KaTeX errors, and a page-overflow probe that passed because there was no table to overflow. Only
  comparing the rendered `<table>` count against a count of the Markdown tables caught it. Do that
  comparison after any table work.
- **A table with no header row needs the generated `<thead>` removed.** Markdown requires a header,
  so a header-less grid (the bare Mermin–Peres square) is written with an empty one, `| | | |`.
  `build.py:drop_empty_thead()` strips a `<thead>` whose cells are all empty, because otherwise it
  renders as a shaded band above the data. It deliberately matches only an *entirely* empty header
  row — `grand-unification-...` has a legitimately empty top-left corner cell and must keep it.
- **Numeric columns are right-aligned** (`---:` in the separator) when every body cell is a plain
  number or a degree value. This is detected at conversion time, not by CSS. Python-Markdown emits
  `style="text-align: right"` inline, which wins over the stylesheet's `text-align: left`. Columns
  holding expressions (`2+1+1=4`) stay left.
- **Markdown cannot rule in the middle of a table**, so the magic square's `\hline`-separated
  row/column products became an explicit **row product** column and **column product** row with bold
  labels. Any future table relying on mid-table rules needs the same treatment.
- **Inline math may contain `|` — do not escape it.** `build.py:protect_math()` masks `$...$` before
  Markdown runs, so a cell like `$|\mathbf{r}|$` survives table parsing intact. Escaping it as
  `\|` would be wrong: KaTeX reads `\|` as the double-bar `‖`, changing the glyph. This is why
  arrays with absolute values convert cleanly.
- Also: the **sign-pattern table rows each get their own paragraph** (see below).

## The sign-pattern section needs a FULL paragraph per block and per involution

In `the-quaternion-and-antiquaternion-subspaces.md`, `## The Involutions as Sign Patterns` is not
just a table. The user rejected brief entries here and asked for **more detail, full paragraphs**.

- **One full paragraph per block row** (four of them). Each gives: the block with its dimension,
  coordinate and parameter (`T_m = R(ie_0)`, dim 1, `ict`, `q'_0 = ct`; `T_i = R(e_0)`, dim 1,
  `ct'`, `q_0 = ct'`; `X_m = R(e_1,e_2,e_3)`, dim 3, `x, y, z`, `q_k`; `X_i = R(ie_1,ie_2,ie_3)`,
  dim 3, `ix', iy', iz'`, `q'_k`); **the row of signs**; the derivation of each sign from what the
  basis element *is* (real/imaginary × scalar/pure quaternion); the general element of the block in
  display math; **a display showing what all four involutions do to that coordinate**; the norm-form
  contribution ($T_m -1$, $T_i +1$, $X_m +3$, $X_i -3$ — verified); the matrix image; and the role.
- **One full paragraph per involution** (four of them), replacing the old one-line bullets: its
  definition, its column of signs, its fixed space in blocks, and its distinguishing role.
- Sign rows to preserve: `T_m (-,+,-,+)`, `T_i (+,+,+,-)`, `X_m (+,-,-,+)`, `X_i (-,-,+,-)`.
- The two sector paragraphs must stay internally consistent: every block paragraph's statements
  about $N$ and $\Phi$ must agree with the norm-form and matrix articles.

## Intersection facts (verified exactly, keep if rewriting)

Verified two independent ways — shared-block identification, and rational Gaussian elimination on
the eight real coordinates — before the prose was written. Intersections: `M- n M+ = 0`,
`H_B n iH_B = 0`, `M- n H_B = X_m (3)`, `M- n iH_B = T_m (1)`, `M+ n H_B = T_i (1)`,
`M+ n iH_B = X_i (3)`; every triple intersection is `0`.

Correction worth keeping: it is **not** true that "each subspace meets each of the other three in
exactly one block" — each meets only two of the other three (its split partner meets it only at
the origin). The earlier version of this section overstated it.


## Symbols for an element of the algebra

- In `conventions-in-the-biquaternion-universe.md` **and**
  `the-matrix-representation-in-the-biquaternion-universe.md` there is a **single** symbol for an
  element of the algebra: $\tilde{Q}$. It is used for the general element, for an element of each of
  the four subspaces (in the matrix article, for whichever subspace the part is about), and for the
  material and informational coordinates alike. Do **not** reintroduce $\tilde{X}$ (material element
  / four-position) or $\tilde{H}$ (Hermitian element / observable) in either article. Where two
  generic operands are needed, subscript it ($\tilde{Q}_1, \tilde{Q}_2$).
  $\tilde{P}$ stays reserved for an idempotent, $\tilde{S}_k$ for the spin operators and
  $\tilde{R}$ for a rotor, in both articles.
- This is local to those two articles. The rest of the corpus still writes $\tilde{X}$ for the
  material four-position (~1 900 occurrences in 118 of the articles), because there the sector is
  fixed by context. If the $\tilde{Q}$-only rule is ever to apply series-wide, that is a separate,
  corpus-wide pass — do not half-apply it.

## LaTeX gotchas (these silently produce red error text on the live site)

1. **Never write `q'_0^2`.** The `'` is parsed as `^\prime`, so a following `^` is a *double
   superscript* ‚Äî KaTeX refuses it. Use `q'^2_0` (the form already used in the
   material/informational-sector articles) or `{q'_0}^2`. This affects only primed symbols;
   `q_0^2` is fine.
2. **Display math inside a list item needs a 4-space indent** to nest inside the `<li>`.
   At 0 or 2 spaces the list splits and the equation falls outside the item.
3. Inline math must not contain a newline (the protection regex is `\$[^$\n]+?\$`).
4. `aligned`/`array`/`cases` are supported and used across the corpus. To check a formula before
   committing, render it with the site's KaTeX version rather than trusting the source.

## Conventions (do not break)

- Sectors: `M- = iq'_0e_0 + q_ke_k = ict¬∑e_0 + x`, `M+ = q_0e_0 + iq'_ke_k = ct'¬∑e_0 + i x'`,
  with the uniform coefficient `Q_Œº = q_Œº + iq'_Œº`, `q'_0 = ct`, `q_0 = ct'`, `q_k = x_k`,
  `q'_k = x'_k`.
- The prime marks the coefficient that enters with `i`; the primed parameters `q'_0, q'_k` span
  `iH_B`.
- `H_B` = fixed space of complex conjugation `*`; `iH_B` = **anti**-fixed space of `*`. Both
  articles must keep saying "anti-fixed" for `iH_B`.
- The fixed spaces of the involutions are `M-`, `M+`, `H_B` (each real dimension 4) and `C_B`
  (real dimension **2**). `C_B` is not four-dimensional, and `iH_B` is not a fixed space.
- `H_B` is **not** contained in a sector: `H_B ∩ M+ = T_i` and `H_B ∩ M- = X_m`, so `H_B` and
  `iH_B` meet both sectors, as does `C_B`. Do not write that the center is "the one subspace that
  straddles the two sectors" — that claim was wrong and has been removed. What is unique to `C_B`
  is that it has no spatial part (hence dimension 2, and all its intersections are temporal lines).
- Span arithmetic: `M- + H_B` and `M+ + iH_B` are 5-dimensional (they share a whole **space** and
  differ in time); `M- + iH_B` and `M+ + H_B` are 7-dimensional (they share a **time** and differ
  in space). Only the two splits reach 8.
- Both coordinate writings (parameter form and physical coordinates) must remain present.
- `articles/biquaternion-zero-divisors.md` is off-limits unless explicitly asked.

## Known pre-existing issue (not yet fixed)

29 formulas in 5 articles outside the M¬±/conventions/matrix group fail to render in KaTeX:
`\slashed` (14, in `the-index-theorem-‚Ä¶`) and `\dddot` (5, in `the-relativistic-quadrupole-‚Ä¶` and
`the-vibrating-ellipsoid-‚Ä¶`) are not KaTeX control sequences, plus 6 in
`gravitational-waves-in-biquaternionic-form.md` and 4 in
`the-einstein-field-equations-under-the-biquaternion-framework-a-research-agenda.md` (cause not yet
diagnosed). Also: the corpus is split on the M‚àí scalar notation ‚Äî 7 articles write `iq'_0e_0`
(intended) and 11 write `iq_0e_0` (same meaning under `q_0 = ct`).
