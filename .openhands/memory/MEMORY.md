# Project memory — ai-research-unit

Specification: `PLAN.md` and the `<!-- ... -->` comments in `maths.md` / `physics.md`. Those comments are the
spec, not decoration.

## Layout
- `articles_maths/`, `articles_physics/` — one `.md` per article, plus a `.context` (agent notes).
  `build.py` renders to HTML; KaTeX 0.16.9 from a CDN in `article_template.html` (no local fonts).
- `_reserve/` — archive of old working notes and subagent instructions. Not published. Left untouched.

## Layer rule the user enforces
Each number system is split into flat groups: `OVERVIEW, ALGEBRA, TOPOLOGY, ANALYSIS, GEOMETRY` (plus
`SUBSPACES`, `REPRESENTATIONS` as synthetic articles at the end). Content belongs to a layer:
- **Algebra**: the product, brackets, ideals, idempotents, zero divisors, level sets `{N = 1}`, `GL`/`SL`.
  NOT allowed: metrical readings — norm as a metric, modulus, polar decomposition,
  totally isotropic subspaces, Witt index, inertia law, null quadric, light cone, sphere/hyperboloid names,
  and form-preserving groups (`SO`, `SU`, `Sp`, `U(1)`, `Spin`).
- **Clarified by the user (do not get this wrong twice)**: an explicitly displayed sum of squares being
  non-negative and vanishing only at zero IS Algebra. `Sc(Q̃Q̃†) = Σ|Q_μ|² ≥ 0`, `= 0` iff `Q̃ = 0`, is a fact
  about the coefficients — a sum of non-negative reals vanishes only if each term does — with no open sets, no
  metric and no completeness in it. It is definiteness of the form, not a reading of the algebra, and it stays
  in the algebra article. What is Topology is the metrical object read off a form: signature, definite-metric
  reading, sphere, hyperboloid, light cone, isotropic, compactness.
- **Topology**: the norm as a metric and everything in the list above. Metric is fine here, not in Algebra.
- Naming is allowed in Algebra only as a delegated pointer ("... is made in *X*"), never as a used structure.
- Zero-divisor articles exist only where zero divisors exist (split-complex, dual, split-quaternion,
  biquaternion, split-biquaternion) and belong to the Algebra group. Real, complex and quaternions need none.

## Notation decision (Sep 2026, user-mandated, settled)
**No fraktur in published articles. Every symbol is MAJUSCULE.** Form: `\mathfrak{X}` → `\mathrm{X}` uppercased,
so `\mathrm{G}`, `\mathrm{M}`, `\mathrm{P}`, `\mathrm{H}`, `\mathrm{B}`, `\mathrm{Z}`, `\mathrm{A}_n`,
`\mathrm{G}_2`. The user first asked to strip fraktur, then that the letters be majuscule, not minuscule.
- NEVER do this by letter alone. A blind `\mathrm{x}` → `\mathrm{X}` corrupts pre-existing single-letter roman
  that never came from fraktur: 987 `\mathrm{s}` exist but only 9 were fraktur (the rest are subscripts like
  `\mathbb{H}_{\mathrm{s}}`); `\mathrm{i}` 308 vs 39; `\mathrm{d}` 100 vs 9. Always transform from a known
  pre-state backup.
- **Case-load-bearing pairs kept lowercase on purpose**, because both forms occur in the same file and merging
  destroys meaning: `𝔭` prime vs `𝔓` prime above; `𝔡` discriminant vs `𝔇` different; `𝔪` vs `𝔐`. Files:
  `algebraic-number-theory.md` (d,p), `class-field-theory.md` (p), `global-fields.md` + `.context` (d,p),
  `local-fields.md` (d), `simple-and-semisimple-modules.md` (m). Read `\mathrm{P}` prime,
  `\mathrm{d}_{L/K}` discriminant, `\mathrm{D}_{L/K}` different.
- `\mathbf{}` was NOT usable: it already means vector (`\mathbf{r}` 1624, `\mathbf{v}` 1196, `\mathbf{p}` 1074).
- **Trade-off**: algebra vs group is now upright vs italic (`\mathrm{G}` algebra, italic `G` group), same quiet
  pairing as `\mathrm{SL}` vs italic `SL`. 62 articles carry both. No collision with any pre-existing uppercase
  roman symbol was found — checked, result "none".
- Multi-letter family names stay as pass 1 left them (`\mathrm{SO}`, `\mathrm{SL}`, `\mathrm{GL}`, `\mathrm{SU}`,
  `\mathrm{Sp}`, `\mathrm{U}`). `_reserve/` deliberately untouched (archive, unpublished) — still has fraktur.
- No script in the repo does this; one-off passes, backups `/tmp/frak*backup`, session-scoped.

## Proof-end mark: removed
The corpus used `$\square$` as the QED end-of-proof mark — 6214 of them, at the end of the last line of a proof
("... and summing gives the result. $\square$"). Every one was removed on 2026-09-27 at the user's request
(the hollow square KaTeX draws reads as a missing-glyph box).
- **The same glyph was doing two jobs — never bulk-operate on it again.** `\Box` (1641 occ.) and the literal
  `U+25A1` (19 occ., in `the-klein-gordon-equation-in-biquaternionic-form.md` and
  `exercise-chirality-and-the-weyl-spinors.md`) are the **d'Alembertian operator** □ = ∂₀² − ∇². Only
  `\square` was the proof mark. A blind "find the square glyph" would have destroyed the wave operator.
- Removal was driven from `/tmp/qed_backup`: inline mark dropped; the spacing command right before a display
  mark (`\qquad`, `\quad`, `\,`, `\ `) dropped with it; a mark alone on its line became nothing. 15 marks sat
  alone between two blank lines — there the mark line AND one blank line must go, or a double blank appears.
- Verification that actually proves the edit: `new` must equal `old` with (mark + the one spacing command before
  it) deleted, compared whitespace-insensitively. Result: 0 files differ. Also no new blank runs, no new
  trailing whitespace, `$` parity intact, menu entries intact.
- **Never put it back.** Articles written after the removal must not carry it: the real-spinors twins did
  (6 marks) and were the only files in the corpus that had, until the 2026-09-27 boundary check removed them.
  After any writing pass run `grep -rl "\\square" articles_maths articles_physics` and expect **0**.

## Maths-corpus boundary rules (`introduction-and-mathematical-conventions`)
- **No physics.** The maths corpus bans *spacetime*, *the speed of light*, *an observer*, *a clock*,
  *a measurement*; it prefers *hyperbolic rotation* to *boost* and *null cone* to *light cone*. Where a
  physical reading exists the maths article “says so with a forward reference and stops” — it must not recount
  the physical result (a charge-conjugation matrix, $KK^{*}=I_4$, the exchange of the chiral halves belong to
  `articles_physics`). Standard vocabulary for the other corpus is **“the physics corpus”** or “the physics
  articles”—*not* “the physics layer” (that phrase existed only in the twins).
- **Article skeleton.** Title as H1, *Introduction* (what it does and what it assumes), thematic sections, then
  *Summary*, *Summary of Notation*, *Further Reading*. Some families insert *Honest Limits* before the Summary.
- **Plumbing.** `articles_maths/<slug>.md` and `articles_physics/<slug>.md`, slug = title lower-cased with
  hyphens. Identical titles across the two menus are the norm (43 pairs); only 3 physics labels carry `†`.
- **An article's layer follows its tools, not its family (user, 2026-09-27).** The *Sylvester equation* pair was
  filed under `### - Topology`; the user rejected that: it belongs to **Analysis**. The intro settles it —
  "the derivative, the smooth structure, a measure or an integral | Part III : Analysis", and Part III owns
  "analytic functions; spectral theory". The article *differentiates* (`d/dt e^{-ta} c e^{-tb}` in its proof) and
  its theorem *integrates* (`int_0^inf e^{-ta} c e^{-tb} dt`), with solvability read off `spec(L_a+R_b)` — so
  Analysis, even though every sibling in its `with hermitian adjoint` family (dagger, Hermitian form, cone,
  adjoint operator) needs only a form and is Topology. The layer wins over the family: do not leave an article in
  a family group when its own content uses a lower-layer tool. Moved 2026-09-27 (biquaternion maths + physics
  entries) to `### - Analysis`, just below *Biquaternion Spectral Theory*.
- **A wrong place is a worse error than a wrong word.** Same session: my *wording* fixes to that article
  (removing "relaxation", "perturbative", "systems theory", "time-ordered") were reverted by the user as
  "total garbage"; the real defect was the layer placement, which I never questioned because the article sat
  where its family sits. Check a twin's *menu group*, not only its prose.
- **Every category name the intro quotes exists in `maths.md`** (checked); its Symbols table writes Lie
  algebras and ideals as `\mathrm{G}, \mathrm{H}, \mathrm{SL}_n` / `\mathrm{M}, \mathrm{P}` (65 corpus uses
  of `\mathrm{G}`), so the old gloss “in Fraktur” was wrong and was dropped 2026-09-27.

## Terminology: "norm", never "norm form" (user-mandated)
The quadratic form `N(Q) = Q Q̄` is called the **norm**. The phrase "norm form" is banned. The user asked
first for the Part VI biquaternion articles, then all of Part VI, then the rest of maths.
**Maths is now clean: 1 residual in the whole corpus**, and it is a false positive — "the elements of zero norm
form a cone" is the English verb (see trap 3 below). Guarded by a boundary-safe regex
`(?i)(?<![A-Za-z])norm[ \t-]*\n?[ \t-]*forms?(?![A-Za-z])`; a `\b`-anchored one silently misses
`Norm Forms__` in an H1 because `_` is a word character.
- Part VI pass (`maths.md` from line 1819): 312 files, 1934 occurrences, 64 in menu comments, 68 headings.
- Parts I–V pass + the rename: 80 files, 302 occurrences, 9 in `maths.md` (menu comments).
- **Renamed** the Topology article **`quadratic-forms-over-algebras-and-norm-forms` → `...-and-norms`**
  (title *Quadratic Forms over Algebras and Norms*), both `.md` and `.context`, its H1, its `## Norm Forms of
  Field Extensions` → `## Norms of Field Extensions` and the three `## The Norm Form of …` headings, the
  `maths.md` href + label + comment, and ~14 cross-references (including two Part VI octonion articles and
  `biquaternion-hermitian-subspace`, which the Part VI pass had deliberately protected).
**Never do this with a blind replace — three traps, all present in this corpus:**
1. *Self-reference.* Sentences contrast the object with an analytic norm: "the norm form … is not a norm",
   "It is not a norm in the analytic sense". After renaming they contradict themselves. Rewritten as "fails to
   be a norm in the analytic sense", "not the value of the norm", "not a condition on the norm", and in
   `topological-algebras-and-banach-algebras` (the sharpest case) as "the norm $N$ of an algebra is a
   quadratic form that may vanish …" against "a norm in the analytic sense".
2. *Hyphenated adjectives.* "norm-form conjugation", "norm-form content", "norm-form condition", "norm-form
   square root", "unit-norm-form subgroup", "norm-versus-norm-form distinction" → each rewritten
   ("the conjugation that defines the norm", "unit-norm subgroup", "norm-versus-quadratic-form distinction").
3. *Verb "form".* "the elements of zero norm form form a cone" — the noun-phrase regex ate one "form" and the
   result is correct English. Treat any `norm form a/an/the` as ambiguous and look at it.
- **Naming the object (settled).** The user chose **"biquaternion norm"** for physics. The corpus's own pattern
  is "<algebra> norm" — the Part VI family is *Real / Complex / Split-Complex / Quaternion / Split-Quaternion /
  **Biquaternion** / Split-Biquaternion / Octonion Norm and Invertibility* — so "biquaternion norm" already
  existed as a name (125 uses). **"complex norm" was rejected: it is taken twice** — (a) the article *Complex
  Norm and Invertibility* means the norm on ℂ, $N(z)=z\bar z$; (b) inside the biquaternion articles "the
  complex norm of the vector part" already denotes a *different* object, $B=\sqrt{Q_1^2+Q_2^2+Q_3^2}$ (58 uses).
  "complex biquaternion norm" is unambiguous but breaks the family pattern and is false for
  split-biquaternions. Mathematics keeps plain "norm"; physics says "biquaternion norm" (its "norm" is already
  taken by the Euclidean/Hermitian norm — 98 lines use both terms together).
- **Physics: DONE.** 2484 phrase occurrences across 712 files; 325 rewritten in `articles_physics` + `physics.md`.
  Five articles renamed (`.md` + `.context`, titles, H1s, hrefs, labels, comments):
  `von-neumann-entropy-and-the-biquaternion-norm`, `fisher-information-and-the-biquaternion-norm`,
  `the-fubini-study-geometry-and-the-biquaternion-norm`, `the-symplectic-form-and-the-biquaternion-norm-cone`,
  `the-lorentz-group-as-biquaternion-norm-automorphisms`. 12 cross-references updated; 313/313 menu entries
  resolve. **Maths untouched.** Backup `/tmp/normform3_backup` (the true original).
  Three extra traps beyond the maths list: (i) `unit norm form`/`unit-norm-form` is "unit norm", NOT
  "unit-biquaternion-norm" — 119 of them, and the spaced form must keep its space ("an element of unit norm");
  (ii) title case must be preserved word-by-word — `### Why Matrix-Unitarity and Not Unit Norm Form` must give
  `... Unit Norm`, so each output word takes its capital from the input word it replaces; (iii) `norm form form
  a single orbit` is noun + verb, so only the first "norm form" is replaced (3 such cases, all in
  `causality-and-the-light-cone-...`; they are the only remaining "norm form" in physics and are correct).
  **Method that saved this: revert to the backup and re-run the whole script after each rule fix — never patch a
  half-applied corpus in place**, because the rules are not idempotent ("biquaternion norm form" would become
  "biquaternion norm" and eat the verb).
- **Maths: DONE, both categories.** 47 `biquaternion-*` articles (306 lines) and 34 `split-biquaternion-*`
  articles (235 lines), `.md` + `.context`. `maths.md` was never touched: its menu labels are the article titles,
  *Biquaternion Norm and Invertibility* and *Split-Biquaternion Norm and Invertibility*, already the right form.
  Sentence case is preserved (`## The Norm` → `## The Split-Biquaternion Norm`), and the split compound takes two
  capitals when the replaced word did: `Split-Biquaternion`, never `Split-biquaternion`.
  Rule that worked: rewrite only `the/its/whose/their/own + norm(s)`, preserving the case of the
  original head word (`## The Norm` → `## The Biquaternion Norm`, not `Biquaternion norm`), plus bold
  `**Norm.**`, table cell `| Norm |` and list item `- Norm ...`. Everything else is out of scope.
  **`this`/`that` must be dropped from the determiner list**: in the split articles both hits are the Euclidean
  norm ("continuous in that norm", "use this norm").
  Protected because it is a *different* object or a generic use: Euclidean (42), complex (23, = the vector-part
  quantity $B$), real (16, = the absolute determinant), unit (15), vanishing / non-vanishing / zero / nonzero
  (33), semi-, genuine, usual, metric, commutator, Frobenius, reduced, Clifford, quaternion; hyphenated
  compounds (`norm-one`, `unit-norm`); generic `a norm`, `norms` in lists.
- **Trap in maths the physics pass did not have: the articles contain change-logs and meta-sentences that quote
  the word "norm".** These must not be touched: the Part I/III boundary rule ("a norm is a distance and a form is
  the distance its norm reads off", "(distance, metric, norm, form, open set, …)"), "the norm was removed from
  the Conventions", "the phrase \"its norm\" was dropped", "norm, the Hermitian form", "the norm article", and
  the naming notes in `.context` (e.g. "using \"norm\" with no caveat", "The 'quaternion norm' notation row was
  purged"). Also `the norm on $\mathbb{H}$` is the Euclidean norm on ℍ, and `the norm of the pure biquaternion`
  is $B$ — both stay plain. Because these live in `.context` as well as in the `.md` changelog tails, verify by
  comparing meta-phrase *counts* against the backup, not by eyeballing the diff.
- **Trap specific to the split-biquaternion articles: 13 sentences use "the norm" for a *different* algebra.**
  The split articles constantly contrast with the biquaternion algebra, the quaternions and the split complex
  numbers, so "In $\mathbb{B}$ the norm is complex…", "In $\mathbb{H}$ there is none: the norm is positive
  definite", "The biquaternion case replaces $\mathbb{D}$ by $\mathbb{C}$: the norm there is complex", "unlike the
  biquaternion case, where the norm is the determinant of a $2\times2$ complex matrix", and "the null cone of the
  norm $r^2-s^2$" (𝔻's norm) all mean the *other* object. They stay plain — renaming them would be false. A
  longer protect phrase also swallows a shorter one on the same line, so protect the whole sentence, not a prefix
  (a prefix let the second "the norm" through: "the square root of the norm requires a branch: the norm is a
  complex number").
  Also left plain, deliberately: `reduced norm` (28 uses) is a *different* object, Δ = N_ℍ(Q₊)N_ℍ(Q₋), the
  determinant; `quaternion norm` (21) and `complex norm` (22) are the component norms.
- Backups: `/tmp/normform_backup`, `/tmp/normform2_backup`, `/tmp/normform3_backup`, `/tmp/maths_md_pre_normform`,
  `/tmp/maths_bn_backup_articles` + `/tmp/maths_bn_backup_maths.md`, `/tmp/splitbn_backup_articles`.

- **Maths Part VI — Quaternions + Split-Quaternions: DONE (second maths pass).** 85 files (`.md` + `.context`),
  364 lines; `maths.md` untouched. Script `/tmp/qbn.py` (dry run → `/tmp/qfrags.txt`), backup
  `/tmp/am_backup_1015`, then 6 hand-fixes. Scope = every slug under `## Quaternions` and `## Split-Quaternions`.
  - Rules: `the/its/whose/their/own + norm(s)` → `quaternion norm` / `split-quaternion norm`; "the norm of the
    algebra / of $\mathbb{H}$ / of the split-quaternion algebra" **folds** to `the quaternion norm` (otherwise
    "the quaternion norm of the quaternion algebra"); headings keep Title Case on the whole compound.
  - `§*The Norm*` citations **follow** the renamed sections (`## The Norm` → `## The Quaternion Norm`,
    `## The Split-Quaternion Norm`); historical mentions stay plain ("no longer has a §*The Norm*", "a section
    that no longer exists", "whose article has no §*The Norm*", "*Quaternion Algebra* §*The Norm* cited" — that
    one spans a line break). Quoted text of other files stays verbatim: menu comments, the *Before* side of edit
    records, and `"§*The Norm and the Determinant Form*"` (a title that lives only in the comparison article).
  - Cross-algebra sentences stay plain: ℍ's norm inside the split articles (definite/positive), 𝔹's inside the
    quaternion ones (indefinite/complex-valued), ℍ_𝔻's third class in `split-quaternion-norm-and-invertibility`.
  - Re-run after the apply = 0 changed lines (fixed point; no "norm norm"). Audit: all 28 remaining
    determiner+norm uses classified, none missed; only `Euclidean`/`Real`/`Clifford`/`reduced`/`unit-norm`/
    `Norm Functionals`/`Conormal`/`Normal` headings remain.
  - **Dangling citations fixed (same day).** `comparison-of-norms-and-invertibility.md` carried 5 distinct stale
    pointers (7 occurrences) — the renames and the earlier restructures invalidated them. All repointed to the
    section that actually holds the claim, not merely to the name-successor: quaternion → §*The Quaternion Norm*;
    biquaternion → §*The Biquaternion Norm as a Semi-Norm* (L28), §*The Unique Real Norm, and the Polar Scale*
    (L53), §*Relation Between the Biquaternion Norm and the Hermitian Form* (L41); split-biquaternion →
    §*The Split-Biquaternion Norm*; split-quaternion → §*Isotropy* (L26) and §*The Split-Quaternion Norm* (L41).
    Result: 36 citations, 0 stale. **Audit recipe**: map menu labels→slugs from `maths.md`, then match
    `\*([^*]+)\*, §\*([^*]+)\*` — NOT a paren-greedy pattern, which misattributes the second citation in
    `(*A*, §*X*; *B*, §*Y*)` and invents phantom stale ones.
  - `maths.md` menu comments: patched the two named entries (Quaternion, Split-Quaternion) to "the quaternion
    norm" / "the split-quaternion norm". The Biquaternion and Split-Biquaternion entries still say "the norm";
    those belong to the pending Biquaternions restructure.

## Recurring gotchas
- 4+ blank-line runs exist in many articles (350 in `articles_maths`), pre-existing, not damage from edits.
  The four originally noticed: `split-complex-integration`, `quaternion-algebra`,
  `split-biquaternion-rotations-and-the-lorentz-group`, `split-biquaternion-geometry`.
- Menu labels and article H1s legitimately differ in a few places (short menu label vs H1 subtitle), e.g.
  `vector-spaces`, `algebras`, `lie-algebras`; the physics menu appends a `†`. Not faults.
- Verify by script, not by eye: menu entry count, H1 == menu label, even `$` count, no new blank runs.
  Back up every touched file (`/tmp/fracbackup*` during a session).
- Reality types (biquaternion corpus): for `Cl_{3,0}` (`c(gamma_k)=sigma_k`) the conjugate module `S-bar` is
  **inequivalent to `S` as a complex module** and isomorphic only as a real representation — that inequivalence
  *is* the complex type (`real-spinors-and-reality-conditions-with-inner-conjugation` §Dimension Three says so;
  do not "correct" it). `eps = i sigma_2 = Phi(-e_2)` is not an `S -> S-bar` intertwiner; it realises
  `eps c-bar(v) eps^{-1} = c(*(v))`, so it is a C-intertwiner only for the `e_k` (`Cl_{0,3}`) reading. Never
  write "`S-bar ≅ S` because `B` is simple": simplicity gives uniqueness, not self-conjugacy. Details in the
  2026-09-27 daily log.
- **Sesquialgebra operator theory (`x ⋆ y = x y^*`)**: the mixed composites are `L_a R_b = S_{ab,1}`,
  `R_b L_a = S_{a,b^*}`, so `[L_a,R_b] = S_{ab,1} - S_{a,b^*}` — NOT `S_{a,b}` (the outer involution:
  `L_aR_b(x)=a(xb^*)^*=ab x^*`). Also `R_a = *∘L_a`, not `L_{a^*}`; `ad_a = L_a-R_a = S_{a,1}-T_{1,a^*}`. The ternary
  pair operator is `Θ_{x,y}=T_{x⋆y,1}` (ordinary left multiplication, linear in `z`), NOT `L_{x⋆y}`; its Lie
  companion is `ad_{[x,y]}` with the envelope commutator. Caught by recomputation; details in the 2026-09-27 log.
- **Sandbox python has no numpy.** Use pure Python: exact arithmetic over `F_{p^2}` (p=7, `i^2=-1`, Frobenius
  as the involution) for algebraic identities, and the closed-form `2×2` largest singular value for operator norms.
- **Very large heredoc commands in the terminal are silently dropped** (exit 0, nothing printed, no files created).
  Use the file editor to create long files, or split the heredoc into smaller commands.

## 2026-09-27 (physical readings in the head categories)
- All 62 articles of *Biquaternion Universe* (10) and *Biquaternion Mathematical Physics* (52) gained a brief
  `## Physical Readings` section before `## Summary` (2-4 sentences each), the clause `physical readings` in their
  `physics.md` comment, and a `## 2026-09-27 (physical readings)` note in their `.context`. The 62 texts are in
  `/tmp/rc/add_readings.py` + `/tmp/rc/add_readings2.py` (the inserter is idempotent: it skips files that already
  have the section). Full detail in the 2026-09-27 daily log.
- The pass rests on two reusable readings: the **invariant content** of a change of the local complex structure is
  the sesquilinear row (probability form, gauge calibration) plus the zero-divisor cone, while the interval and the
  composition move; and the **period $2\pi$** of the central phase makes the quarter turn a clock whose reference and
  rate are supplied and whose arrow is not.
- Review of the two newest articles (same day): *The Celestial Sphere of the Null Cone* — the rank-one factorisation
  needs $\tilde H=-i\tilde P$ and "positive" (future null gives eigenvalues $(2,0)$, past $(0,-2)$). *The Monoid of
  Acting Maps* — "the idempotents lie in $\mathbb{M}_+$" is false (idempotents need not be Hermitian; the corpus's
  word is **projector**), and the minimal-idempotent identity needs a factor two:
  $\tilde\Pi\tilde Q\tilde\Pi=\mathrm{Tr}(\tilde\Pi\tilde Q)\tilde\Pi=2\,\mathrm{Sc}(\tilde\Pi\tilde Q)\tilde\Pi$.
- Two `physics.md` comments wrote $^{\dagger}$ on an element (sandwich action; $4\times4$ regular operator) where
  the articles write $^{*}$; corrected. The dagger belongs to operators only (Conventions, "the dagger is the
  general adjoint").
