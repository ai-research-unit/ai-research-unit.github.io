# __The Upper-Index Problem: What Is Left, What Was Lowered, and the Cost of the Rest__

## Introduction

The corpus states one rule for indices in *Operator and Calculus Conventions*: a contraction is a form, never an index, and no spacetime index is raised or lowered. A component is written low. Indices of another kind — spinor, frame, internal — keep the convention of their own sector. The Minkowski signs sit in the sign vector $\varepsilon$ inside the product, not in a metric that moves indices.

The rule is not yet obeyed everywhere. A scan of the 403 physics articles and the 889 articles of Part VI finds **11 physics articles and nine Part VI articles** that still write at least one raised Greek index of the spacetime alphabet $\mu,\nu,\rho,\lambda,\kappa,\sigma,\tau$. They hold **396 physics occurrences and 59 in Part VI**. The gamma indices are gone: no gamma with a raised spacetime index survives in either corpus.

Two further physics files are screen false positives and are outside the inventory: the Lorentz-group article writes the exponent $z^{\lambda_1-\lambda_2}$, and the bispinor article writes the sign label $\nabla^{\sigma}$ with $\sigma=\pm$. Neither is a spacetime component.

The remainder is not one problem. Four kinds of spacetime index occur, and they cost different things. In the first the superscript is a slot; in the second it is paired with a lower index; in the third it is only a label; in the fourth it is a genuine upper index — a spinor index, a local frame index or an internal-symmetry index — which the spacetime rule does not reach and which must be left alone. A blind lowering is destructive for the first, wrong for the second wherever it is a contraction, correct for the third, and an error for the fourth.

The inventory now stands at **11 files and 396 occurrences**. The last revision reported 78 files and 1,573 occurrences, but that screen counted powers, parameter labels and signs alongside indices; the present count keeps only tokens that are indices, so the two figures are not comparable. The passes in between are not relisted row by row here; the current inventory is the record, and every file absent from it has been repaired.

The examples in this article quote the offending notation. They are the object of study, not the notation of the article.

## The Screen

The count is made on the mathematics regions only, the text between single or double dollars. A superscript counts when its content is one or more spacetime letters, $\mu$, $\nu$, $\rho$, $\lambda$, $\kappa$, $\sigma$ or $\tau$, with nothing else, and it sits on a component symbol. It is a **slot** when a lower index follows it immediately. It is **paired** when the same letter appears as a lower index elsewhere in the same formula; in most entries the pairing is a contraction. It is **plain** otherwise. Superscripts on a closing delimiter and on $\exp$ are excluded, and so is the exponential $e^{\lambda}$ of the matrix articles, since these are powers.

| Corpus | Articles | Index-shaped tokens | Genuine | Articles with a genuine index |
|---|---:|---:|---:|---:|
| Physics | 403 | 398 | 396 | 11 |
| Part VI mathematics | 889 | 172 | 59 | 9 |

The screen is deliberately narrow. Thousands of superscripts that a regex would catch are not indices:

- **exponents** — $x^2$, $a^\lambda$, $e^\lambda$, the Bessel order in $(Q/2)^\nu$, and $z^{\lambda_1-\lambda_2}$;
- **parameter labels** — $\Lambda^\alpha_x$ in the signed-operator articles, $T^\alpha_{a,b}$, $a^{(\alpha)}$, and $\psi^{\mathrm{fop}}$;
- **stars, duals and inverses** — $E_\gamma^*$, $\gamma^*$, $U^{-1}$;
- **sign labels** — $\nabla^{\sigma}$ with $\sigma=\pm$ in the bispinor article.

The last column of the inventory table names the objects that carry the raised index, quoted in the form the article writes them, with the number of occurrences. At most four objects are shown.

## The Kinds

### Class A — the superscript is a slot

The object carries two indices of different kinds, and position distinguishes them: $\Lambda^\mu{}_\nu$ for a Lorentz matrix, $T^\mu{}_\nu$ for a stress tensor with one contravariant and one covariant slot, $\Gamma^\mu{}_{\nu\rho}$ for a connection, $c^\lambda{}_{\mu\rho}$ for structure constants.

Lowering both gives $\Lambda_{\mu\nu}$, and the information of which index is the row and which the column is gone. The corpus has no second slot marker, so the repair is not a relabel. It is a matrix display, a stated slot order, or the cell form $T_{ab}=L_aR_b$. This is the only class where the raised index carries structure that no lowered pair reproduces by itself.

Three physics articles are in this class, with 32 slot occurrences: 29 in *The Algebrodynamical Programme*, 2 in *The Trace Anomaly* and 1 in *The Electric Dipole Moment*. Part VI contributes five slots in three articles.

The worked example is *Torsion, Contorsion and the Spin Connection*, repaired in this pass. Every display is now all-low, with the slot order declared once: in $\Gamma_{\lambda\mu\nu}$, $T_{\lambda\mu\nu}$, $K_{\lambda\mu\nu}$ and $\sigma_{\lambda\mu\nu}$ the first index is the output and the last two are the inputs; in the mixed objects $e_{a\mu}$ and $\omega_{ab\mu}$ the frame slot comes first. The Christoffel formula uses $(g^{-1})_{\lambda\rho}$ for the inverse metric, which the lowering cannot conflate with $g_{\lambda\rho}$.

### Class B — the superscript is paired with a lower index

The raised index is paired with a lowered one in the same formula: $F_{\mu\nu}F^{\mu\nu}$, $\partial_\mu T^{\mu\nu}$, $D_\mu F^{\mu\nu}=J^\nu$, $p^\mu x_\mu$, $j^\mu=\bar\psi\gamma_\mu\psi$.

Lowering both sides is not a relabel here. The corpus reads a repeated label as a sum over the four values, and the Minkowski signs come from $\varepsilon$. The invariant is
$$
F_{\mu\nu}F^{\mu\nu}=\sum_{\mu,\nu}\varepsilon_\mu\varepsilon_\nu F_{\mu\nu}F_{\mu\nu},
$$
so a blind lowering produces a sixteen-term sum with no signs and a different value. The repair is the explicit sum with $\varepsilon$, the quaternionic form $\langle\tilde F,\tilde F\rangle_\natural$, or the cell product. The contraction has to be rewritten, not relettered. Not every pairing is a contraction: in the definition $\Sigma^{\mu\nu}=\tfrac{i}{2}[\gamma_\mu,\gamma_\nu]$ the lower letters only name the generators, and lowering is safe. The scan counts both, so every Class B entry has to be read.

Eleven physics articles are in this class, with 139 paired occurrences. Part VI contributes 36. This is the bulk of the problem: imported tensor formulas that were never translated into the form language.

### Class C — the superscript is only a label

A single component is named, with no partner and no slot: $x^\mu=(ct',\vec x)$, $p^\mu=(E,\vec p)$, $A^\nu$ alone in a definition, $u^\mu$ for a four-velocity. Nothing is lost by writing the index low, because no second occurrence depends on its height. The repair is local and safe.

In physics, 225 of the 396 occurrences are plain labels, spread over all eleven files: the count is dominated by the quoted source articles, not by the corpus's own formulas. In Part VI, 18 remain, in four articles.

### Class D — not an index

The superscript is an exponent, a parameter label, a star, a dual, an inverse or a sign. No action is required, and touching these would be an error. They are outside the inventory. The two physics false positives named in the introduction are in this class.

| Class | Role of the superscript | Lowering is | Repair | Physics articles | Part VI articles |
|---|---|---|---|---|---|
| A | a slot | destructive | matrix, slot order, cell form | 3 (32 occ.) | 3 (5 occ.) |
| B | a pairing | wrong if a contraction | explicit sum with $\varepsilon$, or the form | 11 | 6 |
| C | a label | safe | local relabel | 11 (225 occ.) | 4 (18 occ.) |
| D | not an index | not applicable | none | excluded | excluded |
| E | an index of another kind | kept, role declared | declare the height; relabel world errors | 11 (63 occ.) | 0 |

### Class E — an index of another kind

Some upper indices are not spacetime components. They are outside the spacetime pass. Their height is part of another convention — the Weyl bar, the frame/world slot, the internal basis — and the repair is to declare which, not to lower blindly. Only the tokens that are world indices written with the wrong letter are debt.

**Spinor indices.** In Weyl notation the bar marks the conjugate representation: $\xi^\alpha$ and $\bar\xi^{\bar\alpha}$. The height and the bar together carry the conjugation; lowering the first and keeping the second is the convention, not a repair. Seven occurrences: five in *Charge Conjugation and the Division Ring*, one in *The Spinor Helicity Formalism*, and the vector-spinor slot $\psi_\mu{}^\alpha$ in *The Rarita–Schwinger Equation*. They stay.

**Frame indices.** A tetrad carries a local-frame index and a world index, $h^\alpha{}_{\mu}$. The height separates them: the frame slot is first, the world slot second, and the order is declared once at the definition. Lowering both would erase the distinction that the frame convention exists to keep. Twenty-six occurrences in *The Algebrodynamical Programme* are of this kind: sixteen tetrad legs $h^\alpha{}_{\mu}$ and $h^\beta{}_{\nu}$, and ten structure functions $C^\alpha{}_{\mu\nu}$ and $C^\beta{}_{\mu\alpha}$. They stay, with the slot order declared.

**Internal-symmetry indices.** In the SU(3) article $\alpha,\beta$ label a basis of the algebra, $d_{\alpha\beta}H^{\alpha\beta}$. The height is part of the basis convention, not a spacetime position. One occurrence, kept.

**World indices written with the wrong letter.** Seventeen occurrences: six deformation-tensor slots $\theta^{\alpha\beta}$ in *Maxwell's Theory on Non-Commutative Spaces*, four stress slots in *Nonlinear Maxwell Equations*, six potential slots $A^\alpha$ and $b^\alpha$ and one curvature slot $R^\alpha{}_{\mu\alpha\nu}$ in *The Algebrodynamical Programme*. These are world indices under the wrong letter. Relabelling them to $\mu,\nu$ is Class C, and these seventeen are the only debt in this section.

**Spin components.** Five occurrences, $\sigma^\alpha$ with $\alpha=x,y,z$: two in *Kramers Degeneracy* and three in *The Jordan–Wigner Transformation*. The label names a spatial component, not a spacetime index. Kept.

**Sobolev exponents.** Five in *Scattering for the Quaternionic Dirac Operator*. These are powers, not indices, and stay.

**Operator labels.** Two in *Electromagnetism in Media*. These label the left and right multiplication operators and stay.

The screen finds 63 $\alpha$ and $\beta$ tokens in eleven physics articles. The earlier plan to lower all of them is withdrawn: lowering the frame and spinor heights would erase the distinctions those conventions carry. Seventeen are debt, and forty-six are kept.

| Kind | Tokens | Action |
|---|---:|---|
| spinor $\alpha$ | 7 | keep; the bar and height carry the conjugation |
| tetrad leg $h^\alpha{}_{\mu}$ | 16 | keep; declare frame-first slot order |
| structure function $C^\alpha{}_{\mu\nu}$ | 10 | keep; declare output-first slot order |
| world index mis-lettered $\alpha,\beta$ | 17 | relabel to the spacetime letter |
| spin component $\sigma^\alpha$ | 5 | keep; a spatial label |
| internal-symmetry label | 1 | keep; a basis label |
| Sobolev exponent $H^\alpha$ | 5 | stay; a power, not an index |
| operator label $M^\alpha$ | 2 | stay; a left/right operator name |
| **total** | **63** | 17 relabelled, 46 kept |

The tetrad and structure rows are Class A in the frame sector: they need a declared slot order, not a relabel. The world-index row is Class C. The remaining rows are Class D or a separate convention.

## The Quotation Rule

An article may quote an external display in the source's notation if it says so, names the source, and keeps its own displays in corpus form. The exemption is display-by-display; a declaration in the introduction does not license the article's own prose.

Two physics articles currently invoke the rule. *Matter Makes Space* writes "the source's $q^\mu$ keep the source's notation"; *Maxwell's Theory on Non-Commutative Spaces* writes "formulas quoted from the source keep the source's $x^\mu$". They hold 98 occurrences between them. Those occurrences stay in the inventory as quoted forms, and they are not counted as debt until the declaration is checked display by display. *Relativistic Mechanics* quotes the printed displays of de Haas in one paragraph and says so; the rest of that article is its own notation and is debt.

The rule does not cover a source's slots when the article's own argument depends on the slot structure. *The Algebrodynamical Programme* reports Kassandrov's equations, but it also uses them, so it is repaired as the article's own notation, not exempted as quotation.

## What Was Already Lowered

**The last full revision** cleared the long tail: the articles whose raised index carried no structure, the numeric time components, and the four-index alternating symbol. That pass lowered 104 four-index symbols in seventeen articles and eleven normalisations $\epsilon_{0123}=+1$, and it moved the complex time coordinate of *Why Complexify Spacetime?* to the $\mathbb{B}$ frame rather than lowering it.

**The previous revision** rewrote eight articles display by display: *Canonical Quantization of the Biquaternion Graviton Field*, *Radiation from Accelerated Charges*, *The Lorentz Force*, *The Dirac Equation — Solutions and the Non-Relativistic Limit*, *The Classical Spinning Particle*, *Linearized Gravity*, *The Yang–Mills Equation* and *The Rarita–Schwinger Equation*. They are absent from the inventory below.

**This pass** repaired two:

| Article | Occurrences | What was done |
|---|---:|---|
| [Torsion, Contorsion and the Spin Connection in Biquaternionic Form](../articles_physics/torsion-contorsion-and-the-spin-connection-in-biquaternionic-form.html) | 36 | slots lowered with a declared order; tetrad and spin connection lowered with the frame slot declared; Christoffel formula rewritten with $(g^{-1})_{\lambda\rho}$; the $\Sigma\Sigma$ and $AA$ contractions written with explicit $\varepsilon$ sums |
| [Conformal Invariance and the Massless Limit in Biquaternionic Form](../articles_physics/conformal-invariance-and-the-massless-limit-in-biquaternionic-form.html) | 2 | the fixed non-commutative tensor $\theta^{\mu\nu}$ relabelled $\theta_{\mu\nu}$ |

The torsion article is the model for Class A. Its contraction
$$
\sum_{\lambda,\mu,\nu}\varepsilon_\lambda\varepsilon_\mu\varepsilon_\nu\,\Sigma_{\lambda\mu\nu}\Sigma_{\lambda\mu\nu}
=6\sum_\rho\varepsilon_\rho\,A_\rho A_\rho
$$
shows what a paired lowering costs when the frame is $\mathbb{M}_-$: one explicit weight per summed slot, and no inverse metric left implicit.

## The Frames of the Inventory

The frame matters because the two weights coincide in $\mathbb{M}_-$ and differ in $\mathbb{B}$. In $\mathbb{M}_-$, $g=\varepsilon=\mathrm{diag}(1,-1,-1,-1)$, so a paired index lowers as a relabel under one explicit $\varepsilon$ sum. In $\mathbb{B}$, $g=\mathrm{diag}(1,1,1,1)$ and $\varepsilon=\mathrm{diag}(1,-1,-1,-1)$, so each display must say which contraction it means.

Of the 396 occurrences, 165 are read in $\mathbb{M}_-$ and 231 in $\mathbb{B}$. The $\mathbb{M}_-$ group holds 30 slots, 58 pairs and 77 plain labels; the $\mathbb{B}$ group holds 2 slots, 81 pairs and 148 plain labels. The $\mathbb{B}$ pairs are the expensive ones.

## The Physics Inventory

After the Frame column, the columns give the total number of raised Greek indices, then how many are slots, paired, and plain, then the objects that carry them. A row can have all three kinds. The table is ordered by total.

| Article | Frame | Raised | Slot | Paired | Plain | Objects (quoted form) |
|---|---|---:|---:|---:|---:|---:|
| [The Algebrodynamical Programme: Nonlinear Cauchy–Riemann Conditions, Self-Quantized Charge, and Induced Causal Geometry](../articles_physics/the-algebrodynamical-programme-nonlinear-cauchy-riemann-and-self-quantized-charge.html) | $\mathbb{M}_-$ | 84 | 29 | 28 | 27 | $A^{\mu}$ (13), $\varepsilon^{\rho}$ (6), $A^{\lambda}$ (6), $\Gamma^{\mu}$ (5), +7 more |
| [Matter Makes Space — An External Construction from Quaternionic Spinors](../articles_physics/matter-makes-space-an-external-construction-from-quaternionic-spinors.html) | $\mathbb{B}$ | 51 | 0 | 9 | 42 | $q^{\mu}$ (12), $T^{\rho}$ (6), $S^{\mu}$ (6), $q^{\nu}$ (4), +5 more |
| [Maxwell's Theory on Non-Commutative Spaces and Quaternions](../articles_physics/maxwells-theory-on-non-commutative-spaces-and-quaternions.html) | $\mathbb{B}$ | 47 | 0 | 10 | 37 | $\theta^{\mu\nu}$ (13), $x^{\mu}$ (11), $x^{\nu}$ (4), $i\theta^{\mu\nu}$ (4), +6 more |
| [The Electric Dipole Moment and the Biquaternion Anti-Hermitian Structure](../articles_physics/the-electric-dipole-moment-and-the-biquaternion-anti-hermitian-structure.html) | $\mathbb{M}_-$ | 30 | 1 | 10 | 19 | $\sigma^{\mu\nu}$ (28), $\Gamma^{\mu}$ (2) |
| [The Einstein Field Equations under the Biquaternion Framework — A Research Agenda](../articles_physics/the-einstein-field-equations-under-the-biquaternion-framework-a-research-agenda.html) | $\mathbb{B}$ | 30 | 0 | 6 | 24 | $\eta^{\mu\nu}$ (5), $s^{\mu}$ (3), $R^{\mu\nu}$ (3), $k^{\mu}$ (3), +5 more |
| [The Dirac Path Integral in Biquaternionic Form](../articles_physics/the-dirac-path-integral-in-biquaternionic-form.html) | $\mathbb{B}$ | 27 | 0 | 14 | 13 | $dx^{\mu}$ (10), $\psi^{\mu}$ (8), $F^{\mu\nu}$ (4), $g^{\mu\nu}$ (3) |
| [Relativistic Mechanics in Biquaternionic Form](../articles_physics/relativistic-mechanics-in-biquaternionic-form.html) | $\mathbb{B}$ | 27 | 0 | 12 | 15 | $T^{\nu\mu}$ (7), $V^{\nu}$ (5), $\partial^{\mu}$ (3), $G^{\mu}$ (3), +5 more |
| [Dual Equivalence of the Dirac and Topologically Massive Gauge Fields](../articles_physics/dual-equivalence-of-the-dirac-and-topologically-massive-gauge-fields.html) | $\mathbb{M}_-$ | 27 | 0 | 12 | 15 | $c^{\nu\mu\lambda}$ (4), $H^{\mu\nu}$ (4), $c^{\mu\nu\lambda}$ (3), $K^{\mu}$ (3), +5 more |
| [The Trace Anomaly in Biquaternionic Form](../articles_physics/the-trace-anomaly-in-biquaternionic-form.html) | $\mathbb{B}$ | 25 | 2 | 17 | 6 | $T^{\mu}$ (16), $T^{\mu\nu}$ (6), $\eta^{\mu\nu}$ (1), $\partial^{\mu}$ (1) |
| [Triality and the Ding Construction for the Dirac Spinor in Biquaternionic Form](../articles_physics/triality-and-the-ding-construction-for-the-dirac-spinor-in-biquaternionic-form.html) | $\mathbb{M}_-$ | 24 | 0 | 8 | 16 | $B^{\mu}$ (6), $N^{\mu}$ (4), $t^{\nu\mu\lambda}$ (3), $A^{\mu}$ (2), +4 more |
| [The Nonlinear Dirac Equation and the Thirring Model in Biquaternionic Form](../articles_physics/the-nonlinear-dirac-equation-and-the-thirring-model-in-biquaternionic-form.html) | $\mathbb{B}$ | 24 | 0 | 13 | 11 | $A^{\mu}$ (10), $V^{\mu}$ (8), $T^{\mu\nu}$ (2), $\sigma^{\mu\nu}$ (2), +2 more |
| [The Lorentz Group in Biquaternionic Form — Structure and Representations](../articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.html) | — | (1) | (1) | 0 | 0 | $z^{\lambda_1-\lambda_2}$, an exponent — excluded |
| [Bispinor Fields and the Fundamental Solution of the Generalized Maxwell Equation](../articles_physics/bispinor-fields-and-the-fundamental-solution-of-the-generalized-maxwell-dirac-equation.html) | — | (1) | 0 | 0 | (1) | $\nabla^{\sigma}$, a sign label — excluded |

The last two rows are shown only to record why they are not in the total. The genuine total is 396.

## The Part VI Inventory

Nine of the 889 Part VI articles carry a genuine raised spacetime index. Three are Class A, in the matrix and Clifford group of $M_4(\mathbb{C})$; six are Class B, led by the split-biquaternion element representations and the first-order root. The plain labels sit in four of the same files.

| Article | Frame | Raised | Slot | Paired | Plain | Objects (quoted form) |
|---|---|---:|---:|---:|---:|---:|
| [Split-Biquaternion Algebraic Element Representations](../articles_maths/split-biquaternion-algebraic-element-representations.html) | $\mathbb{B}$ | 17 | 0 | 10 | 7 | $Q^{\mu}$ (10), $q^{\mu}$ (7) |
| [The First-Order Root of the Biquaternion D'Alembertian](../articles_maths/the-first-order-root-of-the-biquaternion-d-alembertian.html) | $\mathbb{B}$ | 25 | 0 | 18 | 7 | $x^{\mu}$ (15), $g^{\mu\nu}$ (10) |
| [Split-Quaternion Higher Special Functions](../articles_maths/split-quaternion-higher-special-functions.html) | $\mathbb{B}$ | 4 | 0 | 3 | 1 | $\tilde\xi^{\nu}$ (4) |
| [The Killing Form of the Antisymmetric Plain Algebra](../articles_maths/the-killing-form-of-the-antisymmetric-plain-algebra-of-quaternioid.html) | $\mathbb{B}$ | 4 | 0 | 1 | 3 | $h^{\mu\nu}$ (3), $\delta^{\mu\nu}$ (1) |
| [$M_4(\mathbb{C})_{\mathcal{T}}$ Representation: The Two-Sided Operators on the Biquaternion Algebra](../articles_maths/m4c-representation-the-two-sided-operators-on-the-biquaternion-algebra.html) | $\mathbb{B}$ | 2 | 0 | 2 | 0 | $\Sigma^{\mu\nu}$ (2) |
| [The Clifford Group and the Frame Stabiliser](../articles_maths/the-clifford-group-and-the-frame-stabiliser.html) | — | 2 | 2 | 0 | 0 | $\Lambda^{\mu}{}_{\nu}$ (2) |
| [The Fierz–Kofink Identities and the Classification of Spinors](../articles_maths/the-fierz-kofink-identities-and-the-classification-of-spinors.html) | $\mathbb{M}_-$ | 2 | 0 | 2 | 0 | $J^{\mu}$ (1), $\eta^{\mu\nu}$ (1) |
| [The Matrix Algebra $M_4(\mathbb{C})$](../articles_maths/the-matrix-algebra-m4c.html) | $\mathbb{B}$ | 2 | 2 | 0 | 0 | $c^{\lambda}{}_{\mu\rho}$ (2) |
| [The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$](../articles_maths/the-gamma-frame-and-the-complexified-dirac-algebra-of-m4c.html) | — | 1 | 1 | 0 | 0 | $\Lambda^{\mu}{}_{\nu}$ (1) |

The other 113 index-shaped tokens in the Part VI list are not indices: 73 are exponentials $e^{\lambda}$ or $e^{\mu}$ of the functional calculus, and 40 are parameter labels and powers. Three files that a loose screen reports are in that residue rather than in the table: $U^{\mu}$ in *The Escape Radius and the Green's Function* is the potential of a measure $\mu$, $\tilde q^{\nu}$ in *Quaternion Involutions and Projections* is the source's notation for an involution about a unit vector $\nu$, and $a^{\lambda}$ in *Split-Biquaternion Element Representation Theory* is the value of a character.

## What a Pass Would Cost

The 396 physics occurrences divide as 32 slots, 139 paired and 225 plain labels. The 59 Part VI occurrences divide as 5 slots, 36 paired and 18 plain. Only the plain labels, 243 in all, can be lowered mechanically. Of the 98 occurrences in the two articles that declare a quotation exception, 79 are plain labels and cannot be touched until the declaration is checked.

The Frame column splits the work by kind of decision, not by difficulty. The 135 non-slot $\mathbb{M}_-$ occurrences lower as relabels under one explicit $\varepsilon$ sum, because the two weights coincide there; the 30 slots do not. The 229 non-slot $\mathbb{B}$ occurrences do not either: $g$ and $\varepsilon$ differ, so each display must declare which contraction it means. A pass in the order A, B, C is still the cheap order. Class A is 3 physics articles and 32 slots (plus 5 in Part VI), and every one needs a decision about the slot before any edit. Class B is 11 physics and 6 Part VI articles holding 175 paired occurrences. Most are textbook formulas quoted in the middle of a biquaternion argument, and the decision is editorial before it is technical.

The two declared quotation articles, *Matter Makes Space* and *Maxwell's Theory on Non-Commutative Spaces*, are held out of the debt pending a display-by-display check. That leaves 298 physics occurrences in nine articles as the own-notation core.

## Recommendation

1. Finish Class A. The algebrodynamical slots (29) are the largest single item; the trace anomaly (2) and the EDM (1) are small. The torsion article shows the repair: declare the slot order once, then lower.
2. Declare the algebrodynamical frame slots once. Its $h^\alpha{}_{\mu}$ is frame-first and its $C^\alpha{}_{\mu\nu}$ is output-first; the heights stay, because they separate the frame sector from the world sector.
3. Repair the $\mathbb{B}$-frame pairs article by article. Each display must choose between $g$ and $\varepsilon$; a script cannot make that choice.
4. Lower the plain labels last and mechanically. The EDM's $\sigma^{\mu\nu}$ is the trap: lowering it is not a relabel while the Hodge identity is written with mixed heights, because $g$ changes the sign of the spatial pair. Check that identity before touching the file.
5. Keep the quotation rule. It is now stated, and two articles invoke it; the rest of the inventory is own notation.
6. Keep numeric components in the same pass as the Greek ones. An article that lowers $x^\mu$ and leaves $x^0$ is half converted.

## Summary

The gamma indices are gone. **11 physics articles and nine Part VI articles** still carry a raised index of the spacetime alphabet $\mu,\nu,\rho,\lambda,\kappa,\sigma,\tau$: **396 physics occurrences and 59 in Part VI**. Two more physics files are screen false positives.

The remaining occurrences fall into three kinds. Class A, the slot, occurs in 3 physics and 3 Part VI articles, 37 occurrences; lowering destroys the row-column distinction. Class B, the pairing, occurs in 11 physics and 6 Part VI articles, 175 occurrences; where it is a contraction, lowering drops the signs of $g$ and changes the value unless the sum carries the sign vector. Class C, the plain label, occurs in 11 physics and 4 Part VI articles, 243 occurrences; lowering is safe, and 98 of the physics ones are declared quotations.

Indices of another kind — spinor, frame, internal — are counted separately: 63 $\alpha$ and $\beta$ tokens in eleven physics articles. Seventeen are mis-lettered world indices and are debt; the other 46 are frame, spinor, internal, or not indices, and stay.

The frame divides the remainder by kind of decision. 165 occurrences read in $\mathbb{M}_-$, where the two weights coincide and a paired index lowers as a relabel; 231 in $\mathbb{B}$, where $g$ and $\varepsilon$ differ and each display must choose its contraction.

A scan that counts every caret reports tens of thousands of false positives, and a scan that counts every Greek letter mixes exponents into the total. The real count is 396 physics occurrences and 59 in Part VI, plus 63 $\alpha/\beta$ tokens, of which 17 are debt. The work is concentrated in Class A and Class B, and Class B needs an editorial decision before it needs an edit.

## Summary of Notation

| Token | Meaning |
|---|---|
| $\gamma_\mu$ | gamma cell; the index is a label, never raised |
| $T_{\mu\nu}=L_\mu R_\nu$ | cell of the two-sided algebra |
| $\varepsilon=(1,-1,-1,-1)$ | sign vector inside the product, the metric of the series |
| $Q_t=ict'$ | time coordinate of the $\mathbb{B}$ frame |
| $x_0=ct'$ | time coordinate of the $\mathbb{M}_-$ frame |
| $\tilde R=ict'e_t+x\vec e_x+y\vec e_y+z\vec e_z$ | material four-position |
| $\mu,\nu,\rho,\lambda,\kappa,\sigma,\tau$ | spacetime component labels, always low |
| $\xi^\alpha$, $\xi_\alpha$ | Weyl spinor index, raised with $\epsilon_{\alpha\beta}$; kept |
| $h^\alpha{}_{\mu}$ | tetrad: $\alpha$ local frame, $\mu$ world; both kept distinct |
| Frame (column) | the frame the article's displays are read in; — marks an algebraic label, not a spacetime index |

## Further Reading

- [Operator and Calculus Conventions](../articles_physics/conventions-of-the-operators-and-the-calculus.html) — the rule: a contraction is a form, never an index.
- [Matrix Representations Conventions](../articles_physics/conventions-of-the-matrix-models.html) — the gamma set, the $\mathbb{B}$ frame and the $\mathbb{M}_-$ frame, and the low-index rule.
- [Torsion, Contorsion and the Spin Connection in Biquaternionic Form](../articles_physics/torsion-contorsion-and-the-spin-connection-in-biquaternionic-form.html) — the worked Class A repair, with the slot order declared once.
- [The First-Order Root of the Biquaternion D'Alembertian](../articles_maths/the-first-order-root-of-the-biquaternion-d-alembertian.html) — the largest Part VI case of a raised index inside a derivative.
