# The Algebra Block — New Structure

The block ends where a pairing of two different elements begins. Every article below uses
the plain product, the coefficients, and the characteristic polynomial. No article pairs
$Q_1$ with $Q_2$ and takes a scalar part. The reduced norm appears only as the constant
term of $p_Q$, never as a form.

Four sections: the object, the frame, the modules, the element.

Status: **KEEP** (title and body unchanged), **RENAME** (new title, body unchanged),
**SPLIT** (text moved into a new article), **NEW** (written), **TRIM** (sections removed
and re-homed). Executed on 2026-09-27: all 35 articles exist, the menu carries the four
sections, and the forms block follows.

Amended 2026-09-27: *The Spinor Spaces* was inserted as article 16, *The Minimal Left
Ideals* kept only the module layer, and the Peirce models were merged into one pair.
The two Columns, Rows and Spinor Spaces articles were deleted, so *The Frame* has six
articles. The block has 35 articles; the tables below carry the final positions.

## 1. The Algebra

The object, its element, its symmetries.

| # | article | file | status | words |
|---|---|---|---|---|
| 1 | The Biquaternion Algebra | `the-biquaternion-algebra-and-its-vector-spaces.md` | SPLIT, RENAME | 5,000 |
| 2 | The Element, the Coordinates and the Conjugations | `the-element-the-coordinates-and-the-conjugations.md` | SPLIT | 2,200 |
| 3 | The Group of Involutions | `the-group-of-involutions.md` | KEEP | 2,900 |
| 4 | The Six Subspaces | `introduction-to-the-remarkable-subspaces.md` | RENAME, TRIM | 7,000 |
| 5 | The Lattice of the Subspaces | `comparison-of-the-remarkable-subspaces.md` | RENAME | 3,400 |
| 6 | The Three Eigenspace Decompositions | `decompositions-along-the-remarkable-subspaces.md` | RENAME | 1,800 |
| 7 | The Square of an Element | `the-square-of-an-element.md` (new) | NEW | 1,200 |
| 8 | Zero Divisors and Units | `zero-divisors-and-units.md` (new) | NEW | 2,000 |
| 9 | $M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant | `m2c-representation-the-matrix-product-and-the-algebra-structure.md` | RENAME | 2,400 |
| 10 | $M_4(\mathbb{C})_L$ Model : The Product, the Trace and the Determinant | `m4c-representation-the-matrix-product-and-the-algebra-structure.md` | RENAME | 2,500 |
| 11 | $M_2(\mathbb{C})$ Model : The Six Subspaces as Matrix Conditions | existing | KEEP | 2,100 |
| 12 | $M_4(\mathbb{C})_L$ Model : The Six Subspaces as Matrix Conditions | existing | KEEP | 1,700 |

Article 1 owns the product, the axioms, the centre and the presentation. It proves
non-division by the explicit product $(e_t+ie_x)(e_t-ie_x)=0$; no norm is named.

Article 2 owns the scalar–vector split, the three coordinate systems, the four
conjugations and $\mathbb{C}[Q]=\operatorname{span}\{e_t,Q\}$. It states that the
centraliser is two-dimensional for a non-central element but does not identify it with
$\mathbb{C}[X]/(p_Q)$: that needs $p_Q$, in article 22, and is done in article 25.

Article 3 keeps the Klein group, its table and its orbits; the four-map definitions moved
to article 2.

Article 4 loses §*The Roots of Zero and Plus One* and §*The Idempotents and the Ideals in
the Remarkable Subspaces*; both are re-homed in §2 and §3. It keeps the six definitions,
the bases, the dimensions and the derivation $4\times2-2=6$: the four non-identity
conjugations give eight eigenspaces, and the two of the reversal $\flat$ coincide with
those of ${}^{*}$.

Article 5 owns intersections, sums and the lattice. Article 6 owns the three eigenspace
decompositions.

Article 7 states $Q^2=(Q_t^2-B^2)e_t+2Q_t\vec Q$, the cone $B^2=0$, and the three
equations with their destinations: $Q^2=0\to13$, $Q^2=Q\to14$, $Q^2=A\to35$.

Article 8 states $QQ^{\natural}=(Q_t^2+B^2)e_t$, unit $\iff QQ^{\nu}\neq0$, the two families
($Q_t=0$ nilpotent; $Q_t\neq0$ a scalar multiple of the idempotent $Q/(2Q_t)$), and the
chain to the minimal left ideal and the spinor. It is the only article in §1 that counts
zero divisors.

The matrix-product pair 9–10 closes the algebra proper. It reads the product, the
coefficients and the unit group. The six-subspace model pair 11–12 follows it, because it
assumes the matrix product. Subtitles mirror; only the model label changes.

## 2. The Frame

The two families the square produced, then the frame that arranges them.

| # | article | file | status | words |
|---|---|---|---|---|
| 13 | Nilpotents | `square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.md` | RENAME | 4,800 |
| 14 | Idempotents | `square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.md` | RENAME | 6,700 |
| 15 | The Peirce Decomposition | `ideals-peirce-decompositions-and-spinors-in-the-biquaternion-algebra.md` | SPLIT | 5,100 |
| 16 | The Spinor Spaces | `the-spinor-spaces.md` (new) | NEW | 1,400 |
| 17 | $M_2(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes | existing | KEEP | 2,300 |
| 18 | $M_4(\mathbb{C})_L$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes | existing | KEEP | 1,800 |

Article 14 defines idempotents without the word *family* for the $Q_t\neq0$ half: the
trivial idempotents $0,e_t$; the nontrivial ones, all with $Q_t=\tfrac12$ and
$\vec Q\neq0$, obtained as $Q/(2Q_t)$; the halving map; the four-parameter family;
primitive and complete pairs; the Hermitian subfamily.

Article 15 takes §*Idempotents and Orthogonal Idempotents*, §*The Peirce Decompositions*,
§*The Peirce Coordinates and the Matrix Model* and §*The Real Structure* of
`ideals-peirce-decompositions-and-spinors-in-the-biquaternion-algebra.md`. It owns the
four corners, the corner rule, the matrix units, the reciprocal $\mathbb{C}^\times$ and
the notion of a frame.

Article 16 owns the two planes $S_\pm$, the two couples and the two actions, with no form and no module. The Peirce model pair 17–18 owns the Cayley block forms.

## 3. The Modules

The algebra acting on itself and on its ideals.

| # | article | file | status | words |
|---|---|---|---|---|
| 19 | The Regular Module | `the-regular-module.md` (new) | SPLIT | 6,000 |
| 20 | The Minimal Left Ideals | `the-minimal-left-ideals.md` (new) | SPLIT | 1,400 |
| 21 | The Category of Modules | `modules-over-the-biquaternion-algebra.md` | SPLIT | 7,400 |

Article 19 takes §*The Three Regular Modules*, §*The Submodules Are the Ideals*, §*The
Four Properties of the Regular Object*, §*The Endomorphisms of the Regular Object* and
§*The Defining Module* of `modules-over-the-biquaternion-algebra.md`, plus §*The
Two-Sided Ideals* and §*Artinian, Semisimple, and Length Two* of the Peirce article. It
states: simple as an algebra (the two-sided ideals are $0$ and $\mathbb{B}$); length two
as a left module; radical zero.

Article 20 takes §*The Decomposition into Minimal Left and Right Ideals* and the minimality. It owns the two copies as ideals, $\mathbb{C}^2$, the simple module and the classification. The couples, the chirality and the two actions are article 16.

Article 21 takes §*The Category of Left Modules*, §*Projectivity and the Parity of
Freeness*, §*The Commutant of an Element*, §*Morita Equivalence with the Complex Field*,
§*Torsion*, §*Real Structures* and §*The Biquaternion Case* of the module article, plus
§*The Lattice of Left Ideals*, §*The Projective Line and the Möbius Action* and §*The
Radical*. It owns the lattice of left ideals as $\mathbb{P}^1$ through the $M_2$ model,
and the double centraliser.

## 4. The Element

Intrinsic data, then normal forms.

| # | article | file | status | words |
|---|---|---|---|---|
| 22 | The Spectrum | `spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.md` | RENAME | 5,600 |
| 23 | $M_2(\mathbb{C})$ Model : The Spectral Projectors | `m2c-representation-the-spectral-projectors-and-the-nilpotents.md` | RENAME | 1,700 |
| 24 | $M_4(\mathbb{C})_L$ Model : The Spectral Projectors | `m4c-representation-the-spectral-projectors-and-the-nilpotents.md` | RENAME | 1,300 |
| 25 | The Centraliser | `the-centraliser.md` (new) | SPLIT | 1,600 |
| 26 | $M_2(\mathbb{C})$ Model : The Centraliser and the Double Centraliser | existing | KEEP | 1,200 |
| 27 | $M_4(\mathbb{C})_L$ Model : The Centraliser and the Double Centraliser | existing | KEEP | 1,900 |
| 28 | The Semisimple–Nilpotent Split | `the-jordan-chevalley-decomposition-of-a-biquaternion.md` | RENAME, TRIM | 2,900 |
| 29 | The Eigenbasis | `the-spectrally-regular-sector-and-construction-of-the-eigenbasis-of-a-biquaternion.md` | RENAME | 6,800 |
| 30 | $M_2(\mathbb{C})$ Model : The Eigenbasis and the Diagonalising Matrix | existing | KEEP | 2,600 |
| 31 | $M_4(\mathbb{C})_L$ Model : The Eigenbasis and the Diagonalising Matrix | existing | KEEP | 1,600 |
| 32 | The Jordan Normal Form | `the-spectrally-degenerate-sector-and-construction-of-the-jordan-basis-of-a-biquaternion.md` | RENAME, TRIM | 5,500 |
| 33 | $M_2(\mathbb{C})$ Model : The Jordan Basis and the Jordanising Matrix | `m2c-representation-the-jordan-basis-and-the-jordanising-matrix.md` | KEEP | 2,900 |
| 34 | $M_4(\mathbb{C})_L$ Model : The Jordan Basis and the Jordanising Matrix | `m4c-representation-the-jordan-basis-and-the-jordanising-matrix.md` | KEEP | 1,900 |
| 35 | Square Roots of an Element | `square-roots-of-a-general-element-in-the-biquaternion-algebra.md` | MOVE, RENAME | 2,900 |

*Worked Examples* — `worked-examples-of-eigenbasis-of-a-biquaternion.md`, KEEP,
unnumbered, at position 56, after the two N-polar articles.

Article 22 owns the criterion, the characteristic polynomial, the discriminant, and the
cone $B^2=0$ as the degeneracy locus.

Article 25 takes §*The Two Frames* of the Jordan–Chevalley article and expands it:
$C(Q)=\mathbb{C}[Q]$ off the scalar line, all of $\mathbb{B}$ at the scalar, the dual
numbers on the cone, the dimension count.

Article 28 takes the remainder of the Jordan–Chevalley article: existence by the
discriminant, uniqueness from the centraliser, and the four types (scalar, semisimple,
Jordan, nilpotent) that name the normal forms of 29 and 32.

Article 32 loses §*The Definite Form*, §*The Polar Decomposition on the Sector* and the
$N$-language of §*The Norm inside the Sector*. The first two need $H$ and belong after the
forms; the third is a theorem about the coincidence $N=Q_t^2$ on the cone, not a
definition.

Article 35 moves from §2 to §4: its classification is by the discriminant of $p_Q$, so it
belongs after article 22, not after the idempotents.

## What leaves the block

Everything that pairs two elements. In reading order this is the next block, not a
residue:

- *The Four General Products and Their Relations* and *Symmetric and Antisymmetric
  Decomposition of the Four General Products*, with their two trace companions. This is
  the first article of the forms block: the four products are the four forms.
- *The Four Forms and the Four Algebraic Norms*, with its four companions.
- The $H$, $N$, $K$ sections and *The Spectral Strata*.
- *Remarkable Subspaces and the Four General Products, Forms and Norms* and *The Polar
  Decomposition and Remarkable Subspaces*.
- *The Conjugations and the Adjoints* ($M_2$ and $M_4$): adjoints are forms.
- *Operators* and the matrix worked examples.

## Deviations from the 29-article list

Three, all forced by the corpus.

1. **The Four Conjugations and the Six Subspaces are two articles, not one.** The merged
   article would be 10,700 words, and the two existing articles have different subjects
   (the group and its orbits; the six fixed spaces). +1.
2. **The Six Subspaces keeps its model pair.** Two existing articles, 3,800 words,
   already read it. Dropping them would delete work; keeping them adds a pair. +2.
3. **Two form-free subspace articles rejoin the block**: *The Lattice of the Subspaces*
   and *The Three Eigenspace Decompositions*. Both use only the conjugations. Leaving
   them in the old *Remarkable Subspaces* section would split the symmetries across two
   sections. +2.

*The Centraliser* is unchanged in count: it was article 21 of the approved list and is
article 25 here. The five additions are in §1; *The Spinor Spaces* is an addition in §2.

Total: 35 articles: 12 in §1, 6 in §2, 3 in §3, 14 in §4, plus the unnumbered worked
examples.

The 29-article version is obtained by merging 3–4, dropping 11–12, and folding 5–6 into 4.
That version is shorter and loses four finished articles.

## The rules

1. **Boundary.** No article pairs two different elements. The reduced norm is the
   constant term of $p_Q$, not a form.
2. **Companions.** A pair is one subtitle with its $M_2$ and $M_4$ articles. Pairs close
   the group they read. Subtitles mirror; only the model label changes.
3. **Equations.** Article 7 sends $Q^2=0\to13$, $Q^2=Q\to14$, $Q^2=A\to35$. No other
   article announces them.
4. **Naming.** One name per concept; the owner is the article that states it, not every
   article that uses it.
5. **Forward destinations.** Real forms, adjoints, polar decompositions, the four
   products and the Killing form go to the forms block. The block names them; it does not
   define them.

## The work

| operation | count | notes |
|---|---|---|
| new text | 6 articles | 2, 7, 8, 19, 20, 25; 2 is a split with expansion |
| splits | 4 files | algebra, Peirce, modules, Jordan–Chevalley |
| renames | 13 | title and menu line; file rename optional |
| trims | 3 | subspaces, semisimple–nilpotent, Jordan normal form |
| unchanged | 13 | companions, models and worked examples |
