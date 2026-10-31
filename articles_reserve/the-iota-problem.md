# __The Iota Problem in Part VI and Physics: A Category Audit, Closed in Part VI__

## Introduction

The premise was that $\iota$ is taken three times: for the Clifford comparison, for the interior product, and for the octonion imaginary units. The audit found something else in its restricted scope. The Clifford comparison is written with its subscript, $\iota_{\mathrm{Cl}}$, and is unambiguous wherever it appears. The interior product appears twice. No scanned article uses $\iota$ for an octonion imaginary unit. The bare letter, meanwhile, carried nine readings in Part VI and two more in physics.

Part VI has since been migrated. Its 523 occurrences in 29 articles are replaced object by object, and the category now contains no $\iota$ at all. Physics is untouched: 11 articles, 181 occurrences, 151 of them the single form $\iota_{\mathrm{Cl}}$.

This article records both states. The inventory is kept as the justification of the migration, and every table states what an article carried and what it became.

## Scope and Method

Part VI begins at the heading *PART VI: SYNTHETIC STUDIES* in `maths.md` and runs to the end of that menu. Its 884 articles fall into 24 categories, from Booleans to the structural comparison around biquaternions. The physics menu has 403 articles in 13 categories.

Three file names occur in both folders, so the 884 Part VI entries and the 403 physics entries are 1,287 menu entries over 1,284 distinct files. Counts in this article are counts of articles as the menu lists them, so the two corpora give 1,287.

The scan reads each Markdown file and counts every control sequence `\iota`, keeping the subscript and any nested braces. It counts occurrences, not lines and not articles. The forms $\iota_{\mathrm{Cl}}$, $\iota_\nu$, $\iota_{\nu_1}$ and $\iota_k$ are four spellings.

A spelling is problematic when the scanned corpus gives it more than one reading. Before the migration, four spellings qualified in Part VI: the bare letter, $\iota_k$, $\iota_1$ and $\iota_2$. Physics has one qualifying spelling, the bare letter, with two readings.

The migration replaced by object, not by spelling alone. Each replacement keeps the subscript, so $\iota_{\nu_1}$ became $\operatorname{Ad}_{\nu_1}$ without renumbering. No new symbol carries a hat or a tilde. Each name was checked against the whole corpus before use: $\operatorname{Mat}$, $\operatorname{inc}$, $\operatorname{idem}$ and $\operatorname{coef}$ were unused, and $\operatorname{Ad}$ was already the corpus name for the inner automorphism. After each file was written, its remaining `\iota` count was required to be zero, and the number of replacements was required to equal the number audited.

## The Verdict

| Measure | Part VI before | Part VI now | Physics |
|---|---:|---:|---:|
| Menu articles | 884 | 884 | 403 |
| Articles using $\iota$ | 29 | 0 | 11 |
| Occurrences | 523 | 0 | 181 |
| Distinct spellings | 46 | 0 | 6 |
| Articles with a contested spelling | 20 | 0 | 2 |
| Occurrences in a contested spelling | 180 | 0 | 25 |

The 180 is the count before the migration, distributed over 20 Part VI articles. It is the sum of the bare letter (95), $\iota_k$ (54), $\iota_1$ (16) and $\iota_2$ (15). The migration removes all of them.

Physics is stable. Of its 181 occurrences, 151 are $\iota_{\mathrm{Cl}}$, two are the interior product $\iota_{X_f}$, one is the inner automorphism $\iota_\lambda$, 26 are the Newman–Penrose spinor and its two components, and one is a bare $\iota$ in the Dirac article.

## The Migration

| Object | Old form | New form | Occurrences | Articles |
|---|---|---|---:|---:|
| inner automorphism and its involutions | $\iota_\nu$, $\iota_u$, $\iota_g$, $\iota_k$, $\iota_j$, $\iota_0$–$\iota_3$, $\iota_{\vec e_k}$ | $\operatorname{Ad}_\nu$, $\operatorname{Ad}_u$, $\operatorname{Ad}_g$, $\operatorname{Ad}_k$, $\operatorname{Ad}_j$, $\operatorname{Ad}_0$–$\operatorname{Ad}_3$, $\operatorname{Ad}_{\vec e_k}$ | 417 | 12 |
| 2×2 matrix embedding $\mathbb{H}\to M_2(\mathbb{C})$ | $\iota$ | $\operatorname{Mat}$ | 38 | 5 |
| embedding $\mathbb{N}\to\mathbb{Z}$ | $\iota$ | $\hookrightarrow$ with $n\mapsto[(n,0)]$ | 22 | 1 |
| corner and block embedding | $\iota$, $\iota_k$ | $\operatorname{inc}$, $\operatorname{inc}_k$ | 21 | 3 |
| idempotent representation | $\iota$ | $\operatorname{idem}$ | 9 | 1 |
| inversion on $\mathbb{R}^\times$ and $\mathbb{C}^\times$ | $\iota$ | $(\cdot)^{-1}$ | 8 | 4 |
| generic involution | $\iota$ | $T$ | 3 | 2 |
| coefficient isometry $\mathbb{B}\to\mathbb{R}^8$ | $\iota$ | $\operatorname{coef}$ | 2 | 1 |
| algebra element $1\otimes i$ | $\iota$ | $1\otimes i$ | 2 | 1 |
| unit map $\iota(1)=e_t$ | $\iota$ | $e_t$ | 1 | 1 |
| **Total** | | | **523** | **29** |

The inner automorphism is 80% of the purge, and it is one substitution: `\iota_` became `\operatorname{Ad}_` in twelve files, every subscript unchanged. The choice is not new notation. The corpus already writes $\operatorname{Ad}_{v_1v_2}$ for the same map in *Quaternion Rotations and Reflections*, and *Quaternion Involutions and Projections* wrote $\iota_{\nu_1}\circ\iota_{\nu_2}=\operatorname{Ad}_{\nu_1\nu_2}$ in one formula, naming the same object twice. The migration removes the duplicate name.

The three generic occurrences became $T$, never $\operatorname{Ad}$. They state the definition of an involution, $T^2=\mathrm{id}$, and are not inner automorphisms.

The $M_6(\mathbb{C})$ article had two maps, and the unital one is distinguished by a superscript rather than a hat: $\operatorname{inc}_k(A)=\operatorname{diag}(A,0)$ and $\operatorname{inc}^{\mathrm{un}}_k(A)=\operatorname{diag}(A,I_{6-k})$. The superscript follows the corpus style of $^{\mathrm{opp}}$, $^{\mathrm{lift}}$ and $^{\mathrm{fn}}$.

The eight inversions were written as operations, not named: $q\mapsto q^{-1}$ and $(r\sigma)^{-1}=r^{-1}\sigma^{-1}$. The letter was doing no work that the formula does not do.

## Part VI by Category

Thirteen of the 24 categories used the letter. The other eleven, with 309 articles, did not, and they still do not.

| Category | Articles | Articles using $\iota$ | Occurrences before | Occurrences now | Replacement |
|---|---:|---:|---:|---:|---|
| Integers | 2 | 1 | 22 | 0 | $\hookrightarrow$ |
| Real Numbers | 19 | 2 | 4 | 0 | $(\cdot)^{-1}$ |
| Complex Numbers | 34 | 3 | 6 | 0 | $(\cdot)^{-1}$, $1\otimes i$ |
| Reduced Biquaternions | 83 | 1 | 9 | 0 | $\operatorname{idem}$ |
| Quaternions | 64 | 11 | 353 | 0 | $\operatorname{Ad}$, $\operatorname{Mat}$ |
| Quaternioid Algebraic Structures | 49 | 2 | 75 | 0 | $\operatorname{Ad}$ |
| Split-Quaternions | 46 | 1 | 15 | 0 | $\operatorname{Ad}$ |
| Biquaternions | 153 | 3 | 15 | 0 | $\operatorname{Ad}$, $\operatorname{coef}$, $e_t$ |
| Split-Biquaternions | 41 | 1 | 1 | 0 | $\operatorname{Ad}$ |
| $M_3(\mathbb{C})$ | 23 | 1 | 4 | 0 | $\operatorname{inc}$ |
| $M_5(\mathbb{C})$ | 23 | 1 | 6 | 0 | $\operatorname{inc}$ |
| $M_6(\mathbb{C})$ | 24 | 1 | 11 | 0 | $\operatorname{inc}_k$, $\operatorname{inc}^{\mathrm{un}}_k$ |
| Structural Comparison around Biquaternions | 14 | 1 | 2 | 0 | $\operatorname{Mat}$ |
| Other Part VI categories | 309 | 0 | 0 | 0 | none |
| **Total** | **884** | **29** | **523** | **0** | **—** |

The last row collects the eleven categories that did not use the letter. The articles that did are named one by one in the next table.

The distribution is uneven. Quaternions holds 353 of the 523 occurrences: 314 are the inner automorphism, 36 the matrix embedding, and 3 a generic involution. The Quaternioid category adds 75, Split-Quaternions 15, Biquaternions 15. The elementary categories account for 32: 22 for the embedding of the natural numbers, 8 for inversion, 2 for the adjoined imaginary.

## The Files

Every article that used the letter is listed, with its count before the migration, the spellings it used, and the notation that replaced them. The column of spellings is the record of the defect; it is not a list of forms still in use.

| Article | Occurrences before | Spellings before | Notation now |
|---|---:|---|---|
| [Quaternion Augmented Statistics](../articles_maths/quaternion-augmented-statistics.html) | 138 | $\iota_j$ (39), $\iota_k$ (36), $\iota_1$ (13), $\iota_2$ (12), $\iota$ (2), and 13 more | $\operatorname{Ad}$ 136; $T$ 2 |
| [Quaternion Involutions and Projections](../articles_maths/quaternion-involutions-and-projections.html) | 97 | $\iota_\nu$ (26), $\iota_{\nu_1}$ (17), $\iota_{\nu_2}$ (15), $\iota_{\nu_3}$ (12), $\iota$ (1), and 10 more | $\operatorname{Ad}$ 96; $T$ 1 |
| [The Group of Involutions of the Quaternioid](../articles_maths/the-group-of-involutions-of-the-quaternioid.html) | 70 | $\iota_\nu$ (30), $\iota_{\nu_1}$ (8), $\iota_{\nu_2}$ (8), $\iota_{\nu_3}$ (8), and 9 more | $\operatorname{Ad}$ |
| [The Generalised Hamilton–Rodrigues Calculus](../articles_maths/the-generalised-hamilton-rodrigues-calculus.html) | 35 | $\iota_j$ (14), $\iota_{\tilde q_1^{-1}}$ (5), $\iota_k$ (4), $\iota_0$ (2), and 9 more | $\operatorname{Ad}$ |
| [Quaternion Automorphisms and Derivations](../articles_maths/quaternion-automorphisms-and-derivations.html) | 23 | $\iota_u$ (14), $\iota_{\exp(ta)}$ (2), $\iota_{\lambda u}$ (1), $\iota_v$ (1), and 5 more | $\operatorname{Ad}$ |
| [The Integers ($\mathbb{Z}$)](../articles_maths/the-integers.html) | 22 | $\iota$ (22) | $\hookrightarrow$ |
| [Quaternion Other Algebraic Element Representations](../articles_maths/quaternion-other-algebraic-element-representations.html) | 16 | $\iota$ (16) | $\operatorname{Mat}$ |
| [Decompositions Along the Remarkable Subspaces of the Quaternions](../articles_maths/decompositions-along-the-remarkable-subspaces-of-the-quaternions.html) | 15 | $\iota_\nu$ (15) | $\operatorname{Ad}$ |
| [Split-Quaternion Automorphisms and Derivations](../articles_maths/split-quaternion-automorphisms-and-derivations.html) | 15 | $\iota_g$ (8), $\iota_{\vec e_z}$ (5), $\iota_{\lambda g}$ (1), $\iota_{\exp(ta)}$ (1) | $\operatorname{Ad}$ |
| [Modulus–Unit Polar Decomposition of Quaternions](../articles_maths/modulus-unit-polar-decomposition-of-quaternions.html) | 12 | $\iota$ (12) | $\operatorname{Mat}$ |
| [Biquaternion Automorphisms and Derivations](../articles_maths/biquaternion-automorphisms-and-derivations.html) | 12 | $\iota_g$ (7), $\iota_{\vec e_x}$ (3), $\iota_{\lambda g}$ (1), $\iota_{g^{*}}$ (1) | $\operatorname{Ad}$ |
| [The $M_3\oplus M_3$ and $M_2\oplus M_4$ Corners of $M_6(\mathbb{C})$](../articles_maths/the-m3-m3-and-m2-m4-corners-of-m6c.html) | 11 | $\iota_k$ (11) | $\operatorname{inc}_k$, $\operatorname{inc}^{\mathrm{un}}_k$ |
| [Reduced Biquaternion Versors and the Orthogonal Group](../articles_maths/reduced-biquaternion-other-algebraic-element-representations.html) | 9 | $\iota$ (9) | $\operatorname{idem}$ |
| [Comparison of the Remarkable Subspaces of the Quaternions](../articles_maths/comparison-of-the-remarkable-subspaces-of-the-quaternions.html) | 6 | $\iota_\nu$ (6) | $\operatorname{Ad}$ |
| [The $M_2\oplus M_3$ Corner of $M_5(\mathbb{C})$](../articles_maths/the-m2-m3-corner-of-m5c.html) | 6 | $\iota$ (6) | $\operatorname{inc}$ |
| [Exponential Polar Decomposition of Quaternions](../articles_maths/exponential-polar-decomposition-of-quaternions.html) | 5 | $\iota$ (5) | $\operatorname{Mat}$ |
| [The Quaternioid as a Vector Space over $\mathbb{C}$](../articles_maths/the-quaternioid-as-a-vector-space-over-c.html) | 5 | $\iota_a$ (5) | $\operatorname{Ad}$ |
| [The $M_2$ Corner of $M_3(\mathbb{C})$](../articles_maths/the-m2-corner-of-m3c.html) | 4 | $\iota$ (4) | $\operatorname{inc}$ |
| [Real Norm and Invertibility](../articles_maths/real-norm-and-invertibility.html) | 3 | $\iota$ (3) | $(\cdot)^{-1}$ |
| [Complex Norm and Invertibility](../articles_maths/complex-norm-and-invertibility.html) | 3 | $\iota$ (3) | $(\cdot)^{-1}$ |
| [Rational-Chart Polar Decomposition of Quaternions](../articles_maths/rational-chart-polar-decomposition-of-quaternions.html) | 3 | $\iota$ (3) | $\operatorname{Mat}$ |
| [Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Quaternions](../articles_maths/introduction-to-the-2x2-matrix-element-representation-of-quaternions.html) | 3 | $\iota_\nu$ (3) | $\operatorname{Ad}$ |
| [Spectral Regularity and Degeneracy in the Complex Algebra](../articles_maths/spectral-regularity-and-degeneracy-in-the-complex-algebra.html) | 2 | $\iota$ (2) | $1\otimes i$ |
| [The Euclidean Topology of the Biquaternion Algebra](../articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.html) | 2 | $\iota$ (2) | $\operatorname{coef}$ |
| [Comparison of Element Representations and Matrix Models](../articles_maths/comparison-of-element-representations-and-matrix-models.html) | 2 | $\iota$ (2) | $\operatorname{Mat}$ |
| [Real Polar Decomposition](../articles_maths/real-polar-decomposition.html) | 1 | $\iota$ (1) | $(\cdot)^{-1}$ |
| [Complex Exponential and Lie Group Structure](../articles_maths/complex-exponential-and-lie-group-structure.html) | 1 | $\iota$ (1) | $(\cdot)^{-1}$ |
| [The Tomita Operator and the J-Modular Pair for the Biquaternion Algebra](../articles_maths/the-tomita-operator-and-the-j-modular-pair-for-the-biquaternion-algebra.html) | 1 | $\iota$ (1) | $e_t$ |
| [Split-Biquaternion Automorphisms and Derivations](../articles_maths/split-biquaternion-automorphisms-and-derivations.html) | 1 | $\iota_{u}$ (1) | $\operatorname{Ad}$ |

The largest single file is *Quaternion Augmented Statistics*, with 138 occurrences and 18 spellings. It is also the file where the bare letter had a second meaning: two occurrences defined a generic involution, and those became $T$, while the 136 subscripted ones became $\operatorname{Ad}$.

*Quaternion Involutions and Projections* follows with 97 occurrences and 15 spellings; one bare occurrence, in a remark quoting the definition of the statistics article, became $T$. The remaining 96 became $\operatorname{Ad}$.

Four files have one occurrence each, among them *Split-Biquaternion Automorphisms and Derivations* and *The Tomita Operator and the J-Modular Pair for the Biquaternion Algebra*. The Tomita article held the only undefined use in the scope: $\xi=\iota(1)=e_t$ introduced a map that the article never named. It now reads $\xi=e_t$, the unit.

## Physics

Physics was not migrated. Its letter is dominated by one declared form; the other uses are local and standard, except one bare occurrence.

| Category | Articles | Articles using $\iota$ | Occurrences | Occurrences in a contested spelling | Main reading |
|---|---:|---:|---:|---:|---|
| Biquaternion Universe Conventions | 8 | 1 | 33 | 0 | the Clifford comparison |
| Biquaternion Non Relativistic Non Quantum Theory | 25 | 1 | 2 | 0 | the interior product |
| Biquaternion Relativistic Quantum Theory | 50 | 5 | 72 | 1 | the Clifford comparison; one bare occurrence |
| Biquaternion Quantum Fields | 68 | 1 | 31 | 0 | the Clifford comparison |
| Biquaternion Particle Physics and Gauge Fields | 52 | 1 | 1 | 0 | the inner automorphism, trivial on the centre |
| Biquaternion Gravity and Cosmology | 11 | 2 | 42 | 24 | the Clifford comparison; the Newman–Penrose spinor |
| Other physics categories | 189 | 0 | 0 | 0 | none |
| **Total** | **403** | **11** | **181** | **25** | **—** |

| Article | Occurrences | Problematic symbol | Reading |
|---|---:|---|---|
| [The Reflection and the Rotation in Biquaternionic Form](../articles_physics/the-reflection-and-the-rotation-in-biquaternionic-form.html) | 37 | none | the Clifford comparison $\iota_{\mathrm{Cl}}$ |
| [Conventions of the Matrix Models](../articles_physics/conventions-of-the-matrix-models.html) | 33 | none | the Clifford comparison $\iota_{\mathrm{Cl}}$ |
| [The Anomalous Magnetic Moment in Biquaternionic Form](../articles_physics/the-anomalous-magnetic-moment-in-biquaternionic-form.html) | 31 | none | the Clifford comparison $\iota_{\mathrm{Cl}}$ |
| [The Newman–Penrose Formalism in Biquaternionic Form](../articles_physics/the-newman-penrose-formalism-in-biquaternionic-form.html) | 26 | $\iota$, $\iota_1$, $\iota_2$ | the Newman–Penrose spinor $\iota=(0,1)^T$, declared in the article, and its components |
| [The Rarita–Schwinger Equation: Spin 3/2 in Biquaternionic Form](../articles_physics/the-rarita-schwinger-equation-spin-3-2-in-biquaternionic-form.html) | 20 | none | the Clifford comparison $\iota_{\mathrm{Cl}}$ |
| [Curved Spacetime and the Biquaternion Framework](../articles_physics/curved-spacetime-and-the-biquaternion-framework.html) | 16 | none | the Clifford comparison $\iota_{\mathrm{Cl}}$ |
| [The Dirac Path Integral in Biquaternionic Form](../articles_physics/the-dirac-path-integral-in-biquaternionic-form.html) | 7 | none | the Clifford comparison $\iota_{\mathrm{Cl}}$ |
| [The Foldy–Wouthuysen Transformation in Biquaternionic Form](../articles_physics/the-foldy-wouthuysen-transformation-in-biquaternionic-form.html) | 6 | none | the Clifford comparison $\iota_{\mathrm{Cl}}$ |
| [The Symplectic Form and the Biquaternion Norm Cone](../articles_physics/the-symplectic-form-and-the-biquaternion-norm-cone.html) | 2 | none | the interior product $\iota_{X_f}$ |
| [The Dirac Equation in Biquaternionic Form](../articles_physics/the-dirac-equation-in-biquaternionic-form.html) | 2 | $\iota$ (bare, once) | the Clifford comparison, written $\iota_{\mathrm{Cl}}$ once and bare once |
| [Gauge Redundancy and the Information in the Gauge Orbit in Biquaternionic Form](../articles_physics/gauge-redundancy-and-the-information-in-the-gauge-orbit-in-biquaternionic-form.html) | 1 | none | the inner automorphism $\iota_\lambda$, the identity because $\lambda$ is central |

The one defect in the Clifford notation is *The Dirac Equation in Biquaternionic Form*: it writes the Clifford comparison as $\iota_{\mathrm{Cl}}$ once and bare $\iota$ once for the complexified extension. The fix is local and is not applied here: write $\iota_{\mathrm{Cl}}$ both times, or declare the extension.

The Newman–Penrose article is a different case. It uses $\iota$ for the second spinor of the dyad, $(0,1)^T$, and writes $\iota_1,\iota_2$ for its components. The object is declared in a display before it is used, the notation is standard in general relativity, and the article never mixes it with the Clifford map. It is not a defect inside physics. It was a cross-corpus collision with the quaternion axis involutions, and the Part VI migration has removed the other side of that collision.

## Outside the Scope

Part VI is clean. Mathematics is not. Outside Part VI, 156 maths articles still use the letter, for 1,632 occurrences. They were not scanned for this audit and were not migrated.

The largest blocks are the same kinds of map under other names. *Curves and Surfaces in the Biquaternion Moving Frame* uses 119 occurrences. *Involutive Groups* uses 78 for the inversion $\iota(g)=g^{-1}$. *The Lie Derivative* uses 59 and *The Exterior Derivative* 49 for the interior product $\iota_X$. *The Signature Operator and the Involution* uses 43. *The Completion Operator* uses $\iota_R$ for the completion map of a ring.

Those uses are stable inside their articles, and several are standard. They matter here for one reason: the claim of this article is about Part VI and physics, not about the mathematical corpus as a whole. A reader who wants one letter for one object across all of mathematics will not get it from this migration.

## Verification

The migration was checked by recomputation, not by reading.

- All 884 Part VI files were rescanned: zero occurrences of `\iota`, and zero occurrences of the Unicode character.
- The per-file counts sum to 523, and the replacement table sums to 523: 417 + 38 + 22 + 21 + 9 + 8 + 3 + 2 + 2 + 1.
- Each of the 29 files was checked after writing: its remaining `\iota` count is zero, and its number of replacements equals its audited count.
- No replacement introduced a hat: `\widehat` does not occur in any of the 29 files.
- No empty subscript: `\operatorname{Ad}_}` does not occur in any of the 29 files.
- Every changed line keeps an even number of `$`, and every file keeps balanced braces.
- The 29 links in the file table resolve to existing articles.

## Summary of Notation

| Form | Reading | Where |
|---|---|---|
| $\operatorname{Ad}_\nu$ | the inner automorphism, and the involution about the axis $\nu$ | Part VI, 417 occurrences |
| $\operatorname{Mat}$ | the 2×2 matrix embedding $\mathbb{H}\to M_2(\mathbb{C})$ | Part VI, 38 |
| $\hookrightarrow$ | the embedding $\mathbb{N}\to\mathbb{Z}$, $n\mapsto[(n,0)]$ | *The Integers*, 22 |
| $\operatorname{inc}_k$, $\operatorname{inc}^{\mathrm{un}}_k$ | the corner and unital embeddings $M_k(\mathbb{C})\to M_6(\mathbb{C})$ | $M_6(\mathbb{C})$, 11 |
| $\operatorname{idem}$ | the idempotent-coordinate representation | Reduced Biquaternions, 9 |
| $(\cdot)^{-1}$ | inversion on $\mathbb{R}^\times$ and $\mathbb{C}^\times$ | Real and Complex Numbers, 8 |
| $T$ | a generic involution, $T^2=\mathrm{id}$ | 3 |
| $\operatorname{coef}$ | the coefficient isometry $\mathbb{B}\to\mathbb{R}^8$ | Biquaternions, 2 |
| $1\otimes i$ | the adjoined imaginary of the complexified algebra | Complex Numbers, 2 |
| $e_t$ | the unit of the biquaternion algebra | 1 |
| $\iota_{\mathrm{Cl}}$ | the Clifford comparison | physics, 151 |
| $\iota_X$ | the interior product | physics, 2 |
| $\iota$ | the Newman–Penrose spinor | physics, 26, declared locally |

## Further Reading

The conventions fix the forms that the migration respected:

- [Conventions of the Indices, the Notation and the Corpus](../articles_maths/conventions-of-the-indices-the-notation-and-the-corpus.html) gives the subscript rules and the admitted forms.
- [Conventions of the Matrix Models](../articles_maths/conventions-of-the-matrix-models.html) and its [physics counterpart](../articles_physics/conventions-of-the-matrix-models.html) define $\iota_{\mathrm{Cl}}$ and its cells.

The exemplars of the audit, now migrated, are:

- [The Integers](../articles_maths/the-integers.html) for the embedding $\mathbb{N}\to\mathbb{Z}$, now written with $\hookrightarrow$.
- [Quaternion Involutions and Projections](../articles_maths/quaternion-involutions-and-projections.html) for the axis family, now $\operatorname{Ad}_\nu$.
- [The Newman–Penrose Formalism in Biquaternionic Form](../articles_physics/the-newman-penrose-formalism-in-biquaternionic-form.html) for the spinor $\iota$, kept and declared.

[The Upper Indexes Problem](the-upper-indexes-problem.html) applies the same audit method to the index conventions and is the model for this inventory.
