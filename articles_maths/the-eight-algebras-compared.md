
# __The Eight Algebras Compared__

## Introduction

This article opens the category that closes the number systems of the corpus. The eight algebras treated in the eight preceding categories are here placed side by side, and the categories themselves are finished: nothing below introduces a result, and every entry of every table is a restatement of a statement proved in one of the source articles and cited to it.

The eight algebras are

$$
\mathbb{R}, \quad \mathbb{C}, \quad \mathbb{D}, \quad \mathbb{D}', \quad \mathbb{H}, \quad \mathbb{H}_{\mathrm{s}}, \quad \mathbb{B}, \quad \mathbb{H}_{\mathbb{D}},
$$

the real numbers $\mathbb{R}$, the complex numbers $\mathbb{C}$, the split complex numbers $\mathbb{D}$ with $j^2 = +1$, the dual numbers $\mathbb{D}'$ with $\varepsilon^2 = 0$, the quaternions $\mathbb{H}$, the split quaternions $\mathbb{H}_{\mathrm{s}} = \mathrm{Cl}_{1,1} \cong M_2(\mathbb{R})$, the biquaternions $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, and the split biquaternions $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$. Two of these are four-dimensional over $\mathbb{R}$ and two are eight-dimensional; the pair that gives the category its name is the last two, the biquaternion systems, whose common feature is a central unit — the complex imaginary $i$ in $\mathbb{B}$, the split complex unit $j$ in $\mathbb{H}_{\mathbb{D}}$ — that commutes with the quaternion units and multiplies the real dimension by two.

The category is a comparison and not a catalogue. The three *Catalogue of …* categories of the corpus sort properties and collect objects; the present one does something else. Each of its thirteen subject articles takes **one subject** — the algebras, their norms and topology, their subspaces, their representations and their polar form, their automorphisms and derivations, their exponential and Lie group structure, their geometry, their analysis, their integration, their spectral theory, their special functions, their harmonic analysis — and states the situation of the eight algebras on that subject as tables with the eight algebras as columns, each table followed by a short explanation. This opening article fixes the columns, the shape of the tables, the marker for an empty cell and the conventions that the thirteen reuse; it is the notation authority of the category.

## The Eight Algebras and the Ladder

### The Ladder

The eight algebras are not a list but a **ladder**: each rung is obtained from a lower one by a single structural change, and the order in which the corpus develops them is exactly the order in which the changes accumulate. The base is the field $\mathbb{R}$. The first rung doubles the dimension by adjoining one square root, and the sign of that square root separates the three two-dimensional systems: $i^2 = -1$ gives the field $\mathbb{C}$ of *Complex Algebra*, $j^2 = +1$ gives the split complex algebra $\mathbb{D}$ of *Split-Complex Algebra*, and $\varepsilon^2 = 0$ gives the dual numbers $\mathbb{D}'$ of *Dual-Numbers Algebra*. The next rung passes to four dimensions with three imaginary units: all three squaring to $-1$ gives the division algebra $\mathbb{H}$ of *Quaternion Algebra*, a mixed signature gives the split quaternion algebra $\mathbb{H}_{\mathrm{s}}$ of *Split-Quaternion Algebra*, which is the matrix algebra $M_2(\mathbb{R})$. The last rung adjoins a central unit that commutes with the quaternion units: the central imaginary $i$ of $\mathbb{C}$ gives the biquaternions $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ of *Biquaternions as a Vector Space over $\mathbb{C}$*, and the split complex unit $j$ of $\mathbb{D}$ gives the split biquaternions $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ of *Split-Biquaternion Algebra*.

The climb of the ladder is a sequence of losses and gains that the tables of this category record one subject at a time. Along it a field becomes a non-field and then a division algebra again and finally a system with zero divisors; commutativity is lost once, at the quaternion rung, and never returns; the norm keeps its definite signature until the split complex rung, becomes indefinite there, and becomes ring-valued over $\mathbb{C}$ or $\mathbb{D}$ at the last rung. The precise rungs at which each property is gained or lost are the content of *Comparison of the Algebras*.

### The Fixed Column Order

Every table of this category lists the eight algebras as columns and in the same order:

| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| introductory column | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |

The first column carries the thing being compared — the invariant, the property, the object — and the eight following columns carry the eight algebras. A table therefore has **nine columns**. The order is not alphabetical and not by dimension alone: it is the ladder order, and it places the definite systems before the indefinite ones, the commutative before the non-commutative, and the four-dimensional before the eight-dimensional, so that a reading from left to right follows the accumulation of structure. The symbol for each algebra is the one fixed in the shared notation block of the corpus, and no table of this category substitutes another: $\mathbb{D}$ is always the split complex numbers and never the dual numbers, $\mathbb{D}'$ is always the dual numbers and never the split complex numbers, and the four-dimensional $\mathbb{H}_{\mathrm{s}}$ is never confused with the eight-dimensional $\mathbb{H}_{\mathbb{D}}$.

### The Two Biquaternion Systems

The two systems that name the category are distinguished once, in *The Number Systems as Clifford Algebras*, and the distinction is used throughout.

**The biquaternions** $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ are the complexification of the quaternions. They are four-dimensional over $\mathbb{C}$ and eight-dimensional over $\mathbb{R}$, they carry a central scalar imaginary $i$ with $i^2 = -1$ commuting with the quaternion units, and they are isomorphic to the matrix algebra $M_2(\mathbb{C})$ (as in *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, §*The Representation*). They are simple but not a division algebra: the norm is complex-valued and vanishes on a cone of real codimension two.

**The split biquaternions** $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ are the tensor product of the split complex algebra with the quaternions. They are also eight-dimensional over $\mathbb{R}$, they carry a central split complex unit $j$ with $j^2 = +1$ commuting with the quaternion units, and they are isomorphic to the direct sum $\mathbb{H} \oplus \mathbb{H}$ by the idempotent decomposition along $\tilde\Pi_{1,2} = \tfrac12(1 \pm j)$ (as in *Split-Biquaternion Algebra*, §*The Algebra Structure*). They are neither simple nor a division algebra, but they are semisimple; their norm is split complex-valued.

The two systems are built on the same quaternion algebra and differ in the central field adjoined, and every contrast between them in this category traces back to that one difference: $\mathbb{C}$ is a field and $\mathbb{D}$ is not.

### The Exclusion of the Octonions

The ladder stops at $\mathbb{H}_{\mathbb{D}}$. The octonions are **excluded** from this category, and the reason is structural rather than conventional: they are **non-associative**, and the instruments by which every table here compares the eight algebras — the involution lattices, the multiplicative norm, the representation theory, the exponential and the Lie structure — are instruments of associative algebra. In a non-associative system the associativity that a representation must respect is absent, so the notion of a module and of a faithful matrix model fails to have the meaning it has here; the norm remains multiplicative over the octonions by the Hurwitz theorem, but the subspaces cut out by involutions no longer form the algebras and ideals that the subspace tables record; and the exponential of a one-parameter family is not defined without an associative product. Several tables of this category would therefore collapse to a single row, and the column order would be broken. The octonions are treated in their own articles *Octonion Algebra* and *Octonion Element Representations*, and no table below opens a ninth column.

## The Master Table of Defining Data

The following table compares the defining data of the eight algebras: one row per invariant and one column per algebra, in the fixed order. Every entry is a restatement of a result of the eight categories, cited in the explanation that follows.

| invariant | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|---|---|---|---|
| presentation | the base field | $\mathbb{R}[i]/(i^2+1)$ | $\mathbb{R}[j]/(j^2-1)$ | $\mathbb{R}[\varepsilon]/(\varepsilon^2)$ | $e_k^2=-1$, $e_ke_l=-e_le_k$ | $e_1^2=-1$, $e_2^2=e_3^2=+1$ | $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | $\mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$ |
| real dimension | $1$ | $2$ | $2$ | $2$ | $4$ | $4$ | $8$ | $8$ |
| commutative | yes | yes | yes | yes | no | no | no | no |
| associative | yes | yes | yes | yes | yes | yes | yes | yes |
| division algebra | yes | yes | no | no | yes | no | no | no |
| zero divisors | none | none | two null lines | one nilpotent line | none | null cone | zero-divisor cone | zero-divisor set |
| conjugations | $1$ | $2$ | $2$ | $2$ | $3$ | $3$ | $4$ | $4$ |
| involution group | trivial | $\mathbb{Z}/2$ | $\mathbb{Z}/2$ | $\mathbb{Z}/2$ | $(\mathbb{Z}/2)^2$ | $(\mathbb{Z}/2)^2$ | $(\mathbb{Z}/2)^2$ | $(\mathbb{Z}/2)^2$ |
| norm signature | $(1,0)$ | $(2,0)$ | $(1,1)$ | $(1,0)$ degenerate | $(4,0)$ | $(2,2)$ | complex-valued | split complex-valued, anisotropic |
| minimal faithful matrix model | $M_1(\mathbb{R})$ | $M_2(\mathbb{R})$ | $M_2(\mathbb{R})$ | $M_2(\mathbb{R})$ | $M_4(\mathbb{R})$ | $M_2(\mathbb{R})$ | $M_2(\mathbb{C})$ | $M_4(\mathbb{C})$ |
| $\operatorname{Aut}$ over $\mathbb{R}$ | $1$ | $\mathbb{Z}/2$ | $\mathbb{Z}/2$ | $\mathbb{R}^{\times}$ | $SO(3)$ | $PGL_2(\mathbb{R})$ | $PGL(2,\mathbb{C})\rtimes\mathbb{Z}/2$ | $(SO(3)\times SO(3))\rtimes\mathbb{Z}/2$ |
| $\operatorname{Der}$ over $\mathbb{R}$ | $0$ | $0$ | $0$ | $\mathbb{R}$, dim $1$ | $\mathrm{SO}(3)$, dim $3$ | $\mathrm{SL}_2(\mathbb{R})$, dim $3$ | $\mathrm{SO}(1,3)$, dim $6$ | $\mathrm{SO}(4)$, dim $6$ |
| exponential type | injective, onto $\mathbb{R}_{>0}$ | surjective, kernel $2\pi i\mathbb{Z}$ | injective, onto identity component | injective, onto identity component | surjective, not injective | not surjective | surjective, not injective | surjective, not injective |
| topology | contractible; $\mathbb{R}^{\times}$ two components | contractible; $\mathbb{C}^{\times}\simeq S^1$ | contractible; $\mathbb{D}^{\times}$ four components | contractible; units $\simeq S^0$ | contractible; $\mathbb{H}^{\times}\simeq S^3$ | contractible; $\mathbb{H}_{\mathrm{s}}^{\times}\simeq S^1$ | contractible; $\mathbb{B}^{\times}\simeq S^1\times S^3$ | contractible; units $\simeq S^3\times S^3$ |

The table divides at three rungs. The first is the passage from $\mathbb{R}$ to $\mathbb{C}$: the dimension doubles, the norm gains a second positive sign, a single nontrivial conjugation appears, and the group of units, still disconnected in $\mathbb{R}$, becomes connected — the unit circle $S^1$ is compact and the exponential becomes surjective with the discrete kernel $2\pi i\mathbb{Z}$, as in *Complex Exponential and Lie Group Structure*, §*The Exponential: Series and Closed Form*. The second is the passage from the definite two-dimensional systems to the indefinite ones: $\mathbb{D}$ and $\mathbb{D}'$ lose the division property, acquire zero divisors, and their norms become isotropic — of signature $(1,1)$ for $\mathbb{D}$ and degenerate of rank one for $\mathbb{D}'$ — while $\mathbb{H}$ remains a division algebra with the definite norm $(4,0)$. The third is the passage to the eight-dimensional systems: $\mathbb{B}$ and $\mathbb{H}_{\mathbb{D}}$ are the only two whose norm is **ring-valued**, the complex-valued $\sum_\mu Q_\mu^2$ of *Biquaternion Norm and Invertibility*, §*The Biquaternion Norm*, and the split complex-valued form of *Split-Biquaternion Norm and Invertibility*, §*The Split-Biquaternion Norm*, so that the question of a real signature separates into a question about the sectors on which the form is real. No real signature is attached to the norm of these two, and the master table records that as the entry "complex-valued" or "split complex-valued" rather than as a pair of integers.

The division column follows the norm column, and the link is the invertibility criterion of *Comparison of Norms and Invertibility*: an element is invertible precisely when its norm is invertible, which for a scalar-valued norm means nonzero and for the split complex-valued norm of $\mathbb{H}_{\mathbb{D}}$ means invertible in $\mathbb{D}$. The algebras with a definite norm — $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ — are the division algebras; the algebras with an isotropic or degenerate norm have zero divisors. The one case that needs its own statement is $\mathbb{H}_{\mathbb{D}}$: its norm is **anisotropic**, vanishing only at the origin, so it does not detect the zero divisors directly. What detects them is the split complex-valuedness: $\tilde{Q}$ is invertible exactly when both idempotent components $\tilde{Q}_\pm$ are nonzero, which is the condition that $N(\tilde{Q})$ be a unit of $\mathbb{D}$ and not merely nonzero, and the zero divisors are the elements with exactly one component zero. The dual numbers are the other case requiring care: their norm $a^2$ is degenerate of rank one, its vanishing set is the nilpotent line $\mathrm{M}$, and $\mathrm{M}$ is one-dimensional rather than a cone.

The columns of transformation data separate differently. The automorphism and derivation rows are small for the finite-dimensional cases: $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{D}$ have finite automorphism groups and zero derivation spaces, because there is no continuous family of automorphisms of a field or of a product of two fields; $\mathbb{D}'$ is the first with a positive-dimensional automorphism group $\mathbb{R}^{\times}$ and a nonzero derivation space, generated by the single derivation $\partial_\varepsilon$ in the nilpotent direction, as in *Dual-Numbers Automorphisms and Derivations*, §*The Derivation Space*. The four higher systems all have automorphism groups of dimension three or six and derivations of matching dimension, and the split biquaternions have the largest, $\mathrm{SO}(4)$ of dimension six, because they are the product of two quaternion algebras and each factor contributes its own $\mathrm{SO}(3)$. The topology row is the most uniform: all eight algebras are contractible as spaces, since each is a real vector space, and all differences lie in the group of units, which is disconnected for $\mathbb{R}$, $\mathbb{D}$, $\mathbb{D}'$ and $\mathbb{H}_{\mathrm{s}}$ and connected for the other four.

## The Conventions of the Comparison Tables

Every subject article of this category keeps the following conventions, and this article is their authority.

**The shape.** Each table has nine columns, the first carrying the compared item and the eight following carrying the eight algebras in the fixed order above. A table is introduced by a sentence that fixes what it compares and in what order, and it is followed by a short explanation — never more than a paragraph — that states what the table shows: what is preserved along the ladder, what is lost and at which rung, which rows are the same in all eight columns, and which rows divide them. No table is left unexplained, and no explanation is left without its table.

**The empty cell.** A row may have no entry for some algebra, and that is part of the mathematics of the category. $\mathbb{R}$ has no nontrivial involution, no zero divisors and no nontrivial spectral theory; the definite systems have no null quadric; the systems without the division property carry no Cauchy integral formula. In every such place the cell carries the marker **—**, and the reason for the emptiness is stated in a sentence under the table. An empty cell is **stated and never filled**: it is not left blank, it is not filled by analogy from a neighbouring column, and the row is not dropped. If a row is meaningful for some of the eight algebras, it stays, with its empty cells marked and explained.

**The content.** Every entry is a restatement of a result already proved in one of the source articles of Table B of the category, and it is cited inline in italics with its section, in the corpus form "*Quaternion Norm and Invertibility*, §*The Quaternion Norm*". A statement that no source article contains is not made: it is left out.

**The form.** Tables are Markdown, never a LaTeX `array` and never an image. Cell text is short enough that the row stays readable; where a cell needs more than a few words, the detail is carried by the explanation under the table. Display mathematics uses the double-dollar fences and stands outside the tables.

## The Tables of the Category and Their Sources

The thirteen subject articles and the source articles that supply their entries, one subject per row, are the following, in the order of the menu. The map is a navigation table and not a comparison table: it has two columns, the subject and its sources, the sources named per algebra.

| subject | source articles, by algebra |
|---|---|
| *Comparison of the Algebras* | *Real Algebra*; *Complex Algebra*; *Split-Complex Algebra*; *Dual-Numbers Algebra*; *Quaternion Algebra*; *Split-Quaternion Algebra*; *Biquaternions as a Vector Space over $\mathbb{C}$*; *Split-Biquaternion Algebra* |
| *Comparison of Norms and Invertibility* | *Real Norm and Invertibility*; *Complex Norm and Invertibility*; *Split-Complex Norm and Invertibility*; *Dual-Numbers Norm and Invertibility*; *Quaternion Norm and Invertibility*; *Split-Quaternion Norm and Invertibility*; *Biquaternion Norm and Invertibility*; *Split-Biquaternion Norm and Invertibility* |
| *Comparison of Analysis* | the analysis, regular-function and Fueter series of the six systems that have them |
| *Comparison of Integration* | *Real Integration*; *Complex Integration*; the split-complex, dual, quaternion, split-quaternion, biquaternion and split-biquaternion integration articles |
| *Comparison of Spectral Theory* | $\mathbb{R}, \mathbb{C}, \mathbb{D}, \mathbb{D}'$ have no source; the quaternion, split-quaternion, biquaternion and split-biquaternion spectral theory articles |
| *Comparison of the Exponential and Lie Group Structure* | the exponential-and-lie-group article of each of the eight algebras |
| *Comparison of Special Functions* | the special-function series of the eight algebras |
| *Comparison of Harmonic Analysis* | the harmonic-analysis series of the eight algebras |
| *Comparison of Geometry* | *Real Line Geometry and Isometries*; *Rotations and Reflections in the Complex Plane*; the split-complex, dual, quaternion, split-quaternion, biquaternion and split-biquaternion geometry series |
| *Comparison of Automorphisms and Derivations* | the automorphism-and-derivation article of each of the eight algebras |
| *Comparison of Subspaces and Involutions* | $\mathbb{R}$ has no source; *Complex Subspaces*; *Split-Complex Subspaces*; *Dual-Number Subspaces*; *The Scalar and Vector Subspaces of $\mathbb{H}$*; the split-quaternion subspace series; the biquaternion subspace series; the split-biquaternion subspace series |
| *Comparison of Element Representations and Matrix Models* | *Real Element Representations* and *Real Regular Element Representation*; the complex, split-complex and dual representation series; the quaternion and split-quaternion representation series; the biquaternion and split-biquaternion representation series |
| *Comparison of the Polar Element Representation* | the polar-representation article of each of the eight algebras |

The first column names the article; the second names the sources that supply its entries. A source named for an algebra is cited in the tables of that article under that algebra's column; where the first column shows no source, the corresponding column of that article's tables is empty and marked. The subjects are grouped as the menu groups them, by subject family: this overview, then Algebra, Topology, Analysis — carrying the six subjects from analysis to harmonic analysis — Geometry, Subspaces and Representations.

## The Place of the Category

The category belongs to Part VI. It stands at the close of the block of number systems — after the eight categories whose systems it compares — and before the octonions, which are the subject of their own articles and which it excludes. No other category is moved, and it is placed where it is because a comparison can only be written once the things compared have been built. Its two namesakes, the biquaternion systems $\mathbb{B}$ and $\mathbb{H}_{\mathbb{D}}$, are the highest rungs of the ladder and the two systems in which every phenomenon of the category — the ring-valued norm, the four conjugations, the zero divisors, the non-compact unit groups, the ring-valued analysis — appears at once.

**What the eight are, and what the doubling of a two-dimensional system gives.** The eight are the systems the corpus's ladder produces by doubling: the field $\mathbb{R}$; the three two-dimensional systems obtained from it by adjoining one commuting unit; the two four-dimensional quaternion systems $\mathbb{H}$ and $\mathbb{H}_{\mathrm{s}}$, obtained by adjoining two units that anticommute; and the two eight-dimensional systems $\mathbb{B}$ and $\mathbb{H}_{\mathbb{D}}$, obtained from $\mathbb{H}$ by adjoining a central unit with square $-1$ and $+1$. The doubling of a *two-dimensional* system is a construction the ladder does not contain, and the most important of those doublings is
$$\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C} \;\cong\; \mathbb{C}\oplus\mathbb{C},$$
the four-dimensional commutative algebra with the two idempotents $\tfrac12(1\pm e)$, called the **reduced biquaternion** in the engineering literature and the double-complex, tessarine or commutative hypercomplex algebra elsewhere. It is the complex analogue of the split biquaternions — the same idempotent decomposition, the same componentwise ring-valued norm, the same zero divisors, with $\mathbb{C}$ where $\mathbb{H}_{\mathbb{D}}$ has $\mathbb{H}$ — and it is recorded with the four-dimensional algebras in *List of Algebras by Dimension* and with the reductions in *Harmonic Analysis over Hypercomplex Systems*. No column is opened for it, for the reason no ninth column is opened at all: the columns are the eight systems on which the block of number systems is built.
The category does not touch the eight categories it compares. The source articles are complete and are read-only in this pass; no result is moved out of a source article and into a comparison, and no source article is corrected here. Where a comparison meets a statement it cannot support from a source, the statement is not written into the article.

## Summary

The category compares the eight algebras $\mathbb{R}, \mathbb{C}, \mathbb{D}, \mathbb{D}', \mathbb{H}, \mathbb{H}_{\mathrm{s}}, \mathbb{B}, \mathbb{H}_{\mathbb{D}}$ on one subject at a time, in tables of nine columns with the eight algebras in a fixed ladder order, each table introduced by a sentence and followed by a short explanation. This opening article fixes the columns, states the master table of defining data — dimension, commutativity, associativity, the division property, the zero divisors, the conjugations, the involution group, the signature of the norm, the minimal faithful matrix model, $\operatorname{Aut}$, $\operatorname{Der}$, the exponential type and the topology — fixes the empty-cell marker and the rule that an empty cell is stated and never filled, and maps each table of the category to the article that supplies it. The ladder climbs from the field $\mathbb{R}$ through the three two-dimensional systems $\mathbb{C}, \mathbb{D}, \mathbb{D}'$, the two four-dimensional systems $\mathbb{H}, \mathbb{H}_{\mathrm{s}}$, and the two eight-dimensional biquaternion systems $\mathbb{B}, \mathbb{H}_{\mathbb{D}}$, which give the category its name and its two central units. The octonions are excluded because they are non-associative and the instruments of the comparison do not survive, and no ninth column is opened. The category closes the block of the number systems in Part VI and introduces no mathematics of its own.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{R}$ | the real numbers, dimension $1$ |
| $\mathbb{C}$ | the complex numbers, $i^2=-1$, dimension $2$ |
| $\mathbb{D}$ | the split complex numbers, $j^2=+1$, dimension $2$ |
| $\mathbb{D}'$ | the dual numbers, $\varepsilon^2=0$, dimension $2$ |
| $\mathbb{H}$ | the quaternions, $e_k^2=-1$, dimension $4$ |
| $\mathbb{H}_{\mathrm{s}}$ | the split quaternions, $\mathrm{Cl}_{1,1}\cong M_2(\mathbb{R})$, dimension $4$ |
| $\mathbb{B}$ | the biquaternions, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, dimension $8$ |
| $\mathbb{H}_{\mathbb{D}}$ | the split biquaternions, $\mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$, dimension $8$ |
| $e_0=1,e_1,e_2,e_3$ | the algebra basis |
| $i$ | the central scalar imaginary of $\mathbb{B}$, $i^2=-1$ |
| $j$ | the central split complex unit of $\mathbb{H}_{\mathbb{D}}$, $j^2=+1$ |
| $\varepsilon$ | the dual unit of $\mathbb{D}'$, $\varepsilon^2=0$ |
| $\tilde\Pi_{1,2}=\tfrac12(1\pm j)$ | the idempotents of $\mathbb{D}$ and of $\mathbb{H}_{\mathbb{D}}$ |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$, ${}^{\flat}$ | quaternion, complex, Hermitian and anti-Hermitian conjugation |
| $N(\tilde{Q})=\tilde{Q}\tilde{Q}^{\natural}$ | the norm |
| $\operatorname{Aut}$, $\operatorname{Der}$ | the automorphism group and derivation space |
| $M_n(F)$ | the algebra of $n\times n$ matrices over $F$ |
| $S^n$ | the unit sphere of $\mathbb{R}^{n+1}$ |
| `—` | the marker of an empty cell, stated and never filled |
| Part VI | the part of the corpus that gathers the number systems, this comparison category and the octonions |

## Further Reading

- William Kingdon Clifford, "Preliminary Sketch of Biquaternions", *Proceedings of the London Mathematical Society* **4** (1873) 381–395, for the origin of the split complex, dual and biquaternion systems in one construction.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the Cayley–Dickson ladder, the Hurwitz theorem and the place of the octonions.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the low-dimensional classification $\mathrm{Cl}_{1,1}\cong M_2(\mathbb{R})$ and the split forms.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the identification of the transformation groups of the low-dimensional algebras.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the general structure theory of finite-dimensional associative algebras.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for signatures, isotropy and the theory of indefinite quadratic forms.
- John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288 (Springer, 2021), for the norm and the group of units of a quaternion algebra and its splittings.

- Soo-Chang Pei, Ja-Han Chang and Jian-Jiun Ding, "Commutative reduced biquaternions and their Fourier transform for signal and image processing applications", *IEEE Transactions on Signal Processing* **52** (2004) 2012–2022, for the reduced biquaternion algebra — the commutative four-dimensional algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$, equivalently the double-complex, tessarine or commutative hypercomplex algebra — and for its defining data, its idempotent decomposition and its norm, the commutative counterpart of the two biquaternion columns.
