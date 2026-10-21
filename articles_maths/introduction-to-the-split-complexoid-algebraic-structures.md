
# __Introduction to the Split-Complexoid Algebraic Structures__

## Introduction

The split-complex numbers are a commutative ring, and that ring is the subject of *Split-Complex Algebra*. The same underlying set, read as an algebra over $\mathbb{R}$, carries structures the ring axioms do not name: a real-linear product structure, a second product beside the multiplication, two pairings with their algebraic norms, a ternary operation, a pair of real matrix models, and a lattice of distinguished subspaces. This category gathers those structures, and this article states what they are and how they hang together.

The guiding distinction is the one the whole synthetic part of the corpus draws: a *number system* is one object and its *algebraic structures* are the several algebras the same carrier admits. For $\mathbb{D}$ the carrier is the plane $\mathbb{D}_{\mathbb{R}}$ of real dimension two, and the structures are obtained from the single datum of the algebra together with its conjugation. The split sign $j^2=+1$ is the whole difference from the complex field, and it is the source of every degeneracy recorded below: the carrier is a ring and not a field, the Hermitian form is indefinite, the commutator lies on the split imaginary line, and no definite multiplicative norm exists. There is no third product and no hidden operation: the count below is exhaustive.

**Conventions.** $Q_1 = q_1 + jq'_1$ and $Q_2 = q_2 + jq'_2$ are elements of $\mathbb{D}$, with $q_1,q'_1,q_2,q'_2\in\mathbb{R}$; $\bar Q_1 = q_1 - jq'_1$ is the conjugate; $j^2 = +1$; the idempotents are $\Pi_1 = \tfrac12(1+j)$ and $\Pi_2 = \tfrac12(1-j)$, the idempotent coordinates are $q_{1+} = q_1+q'_1$ and $q_{1-} = q_1-q'_1$, and $Q_1 = q_{1+}\Pi_1 + q_{1-}\Pi_2$; $\mathrm{Sc}$, $\mathrm{Re}$ and $\mathrm{Im}$ are read in $\mathbb{D}$. The algebra read over $\mathbb{R}$ is written $\mathbb{D}_{\mathbb{R}}$, with real basis $1, j$. The two products are written $Q_1Q_2$ for the ring product and $Q_1\bar Q_2$ for the sesquilinear one, following *Conventions in Mathematics*; the letters $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ are reserved for forms and norms.

## The Split-Complexoid

**Definition.** The **split-complexoid** is the pair $(\mathbb{D}, \bar\cdot)$ read as an algebra over $\mathbb{R}$: the real vector space $\mathbb{D}_{\mathbb{R}}$ together with the involution $\bar\cdot$. Every structure of this category is built from that pair alone.

**Proposition.** The realification doubles no structure and loses none: $\mathbb{D}_{\mathbb{R}}$ has real basis $1, j$ and real dimension $2$, and the real-linear multiplication by $j$ is the operator $J(Q_1) = jQ_1$, an involution of square $+\operatorname{id}$ with the two real eigenlines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$. A real-linear map of the plane is $\mathbb{D}$-linear exactly when it commutes with $J$ and conjugate-linear exactly when it anticommutes; the $\mathbb{D}$-linear endomorphisms are the multiplications by an element and form the plane $\operatorname{End}_{\mathbb{D}}(\mathbb{D}) \cong \mathbb{D}$, the conjugate-linear ones form the complementary plane, and together they fill $\operatorname{End}_{\mathbb{R}}(\mathbb{D}) \cong M_2(\mathbb{R})$.

**Proof.** That $1, j$ is a real basis and that $\dim_{\mathbb{R}}\mathbb{D} = 2$ is immediate. The map $J$ is $\mathbb{R}$-linear, $J^2(Q_1) = j(jQ_1) = j^2Q_1 = Q_1$, and $J(Q_1) = \lambda Q_1$ forces $\lambda = +1$ or $\lambda=-1$ for $Q_1\neq0$, the eigenspaces being $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$. A real-linear $T$ commutes with $J$ exactly when $T(jQ_1) = jT(Q_1)$, which is $\mathbb{D}$-linearity, and anticommutes exactly when $T(jQ_1) = -jT(Q_1)$; the two classes are the $+1$ and $-1$ eigenspaces of conjugation by $J$ on $\operatorname{End}_{\mathbb{R}}(\mathbb{D})$, of dimensions $2$ and $2$. The commuting maps are $Q_1\mapsto \lambda Q_1$, and the two-dimensional space is $\mathbb{D}$. The whole development is *The Split-Complexoid as a Vector Space over $\mathbb{R}$*.

**Remark.** The complexification $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{D}\cong\mathbb{C}\times\mathbb{C}$ is **not** a field: the polynomial $x^2-1$ already factors over $\mathbb{R}$, and the extension of scalars carries the zero divisors with it. The complex field is the other rung of the ladder, where the adjoined root does not exist over $\mathbb{R}$; the passage between the two rungs is *The Realification and the Effect of the Change of Scalars on the Split-Complexoid*.

## The Two Products

**Definition.** The **two products** of the split-complex space are the **general plain bilinear** product and the **general plain sesquilinear** product,

$$
Q_1Q_2 = (q_1q_2 + q'_1q'_2) + (q_1q'_2 + q'_1q_2)j, \qquad\qquad Q_1\bar Q_2 = (q_1q_2 - q'_1q'_2) + (q'_1q_2 - q_1q'_2)j .
$$

**Theorem.** The product $Q_1Q_2$ is $\mathbb{D}$-bilinear, associative, commutative and unital; it is the multiplication of the algebra, and $\mathbb{D}$ is a ring with zero divisors and not a field. The product $Q_1\bar Q_2$ is $\mathbb{D}$-linear in the first slot and conjugate-linear in the second, conjugate-commutative, right-unital but not left-unital, and not associative.

**Proof.** The formulas are the ring multiplication and the same multiplication with $Q_2$ replaced by $\bar Q_2$. Bilinearity, associativity, commutativity and the two-sided unit $1$ for $Q_1Q_2$ are the ring axioms, and the zero divisors $\Pi_1\Pi_2=0$ show that the ring is not a field. For $Q_1\bar Q_2$, linearity in $Q_1$ and conjugate-linearity in $Q_2$ are read from the formula, conjugate-commutativity $Q_1\bar Q_2 = \overline{Q_2\bar Q_1}$ follows by conjugating, the right unit is $1$ since $Q_1\bar 1 = Q_1$, and $1$ is not a left unit since $1\bar j = -j \neq j$; associativity fails at the witness $(1,1,j)$, where $(1\star1)\star j = -j$ against $1\star(1\star j) = j$. The two products and their property table are *The Two Products of the Split-Complexoid Space* and *Relations and Comparison Between the Two Products of the Split-Complexoid Space*.

**Remark (the idempotent coordinates).** With $Q_1 = q_{1+}\Pi_1 + q_{1-}\Pi_2$ and $Q_2 = q_{2+}\Pi_1 + q_{2-}\Pi_2$ the ring product is componentwise and the sesquilinear one exchanges the two coordinates of the second factor,

$$
Q_1Q_2 \leftrightarrow (q_{1+}q_{2+}, q_{1-}q_{2-}), \qquad\qquad Q_1\bar Q_2 \leftrightarrow (q_{1+}q_{2-}, q_{1-}q_{2+}),
$$

which is the reason $\mathbb{D}\cong\mathbb{R}\times\mathbb{R}$ and the reason the sesquilinear product has no left unit and cannot be associative.

## The Two Forms and Their Algebraic Norms

**Definition.** The **two forms** are the scalar parts of the two products,

$$
\langle Q_1,Q_2\rangle = Q_1Q_2, \qquad\qquad \langle Q_1,Q_2\rangle_{*} = Q_1\bar Q_2 ,
$$

named the **general plain bilinear form** and the **Hermitian form**; their **algebraic norms** are the values at the two equal arguments, $\langle Q_1\rangle = Q_1^2$ and $\langle Q_1\rangle_{*} = Q_1\bar Q_1 = \langle Q_1\rangle_{\natural}$.

**Theorem.** $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{*}$ have the same Gram matrix $[1]$ in the basis $1$ and are separated by their symmetry alone, $\langle\cdot,\cdot\rangle$ symmetric and $\langle\cdot\rangle_{*}$ conjugate-symmetric. Their algebraic norms are $\langle Q_1\rangle = Q_1^2$, $\mathbb{D}$-valued and anisotropic, and $\langle Q_1\rangle_{*} = q_1^2 - q'^2_1$, real and indefinite. **Both are multiplicative**, and **neither is a definite real norm**: the $\mathbb{D}$-valued $\langle\cdot\rangle$ defines no order and the real $\langle\cdot\rangle_{*}$ is indefinite, while what is definite is the realified *form* $\operatorname{Re}B$, of signature $(2,0)$, against the indefinite realification $\operatorname{Re}H$ of signature $(1,1)$.

**Proof.** The Gram matrix is $[\langle 1,1\rangle] = [1]$ and $[\langle 1,1\rangle_{*}] = [1]$. Symmetry of $\langle\cdot,\cdot\rangle$ is commutativity of the ring; conjugate-symmetry $\langle Q_1,Q_2\rangle_{*} = \overline{\langle Q_2,Q_1\rangle_{*}}$ is conjugate-commutativity. The form $\langle Q_1\rangle = (q_1+jq'_1)^2$ vanishes only at $Q_1 = 0$ but takes values in $\mathbb{D}$ and defines no order; $\langle Q_1\rangle_{*} = q_1^2-q'^2_1$ is real, changes sign, and vanishes exactly on the union of the two null lines, which is the zero-divisor set. Multiplicativity is $\langle Q_1Q_2\rangle = Q_1^2Q_2^2$ and $\langle Q_1Q_2\rangle_{*} = Q_1\bar Q_1Q_2\bar Q_2 = \langle Q_1\rangle_{*}\langle Q_2\rangle_{*}$. The two realified signatures are computed from the real parts $\operatorname{Re}\langle Q_1,Q_2\rangle = q_1q_2+q'_1q'_2$ and $\operatorname{Re}\langle Q_1,Q_2\rangle_{*} = q_1q_2-q'_1q'_2$. That no definite multiplicative norm exists, because $\Pi_1\Pi_2=0$ would force $\nu(\Pi_1)\nu(\Pi_2)=0$, is the theorem of *The Two Forms and the Two Algebraic Norms of the Split-Complexoid Space*.

## The General Plain Sesqualgebra and the Ternary Product

**Definition.** The **general plain sesqualgebra (GPS)** over $\mathbb{D}$ is the pair $(\mathbb{D}, \star)$ with the sesquilinear product $Q_1\star Q_2 = Q_1\bar Q_2$.

**Theorem.** The associator of $\star$ is $[Q_1,Q_2,Q_3] = Q_1\bar Q_2(\bar Q_3 - Q_3)$, nonzero but confined to the anti-self-adjoint part of the third slot; its **ternary product** $\{Q_1,Q_2,Q_3\} = Q_1\bar Q_2Q_3$ is symmetric in the outer slots, Hermitian-symmetric, $\overline{\{Q_1,Q_2,Q_3\}} = \{\bar Q_1,\bar Q_2,\bar Q_3\}$, and satisfies the Jordan triple identity, so that the structure is a **$J^{*}$-algebra** (a Jordan triple with an involution).

**Proof.** The associator is $[Q_1,Q_2,Q_3] = (Q_1\bar Q_2)\bar Q_3 - Q_1\bar Q_2 Q_3 = Q_1\bar Q_2(\bar Q_3 - Q_3)$, which vanishes exactly when $Q_3$ is real, with the witness $[j,j,j] = 2j$. Outer symmetry is $\{Q_1,Q_2,Q_3\} = Q_1\bar Q_2Q_3 = Q_3\bar Q_2Q_1 = \{Q_3,Q_2,Q_1\}$ by commutativity, and Hermitian symmetry follows by conjugating the three entries. The Jordan triple identity is the model computation $xy^{*}z$ of an associative algebra with a sesquilinear involution; it is the axiom of *Jordan Triples with an Involution* and *Algebraic J\*-Algebras*. The article is *The Sesquilinear Product of the Split-Complexoid Space*, and the form theory of the second slot is *The Hermitian Form and the Cone of the Split-Complexoid Algebra*.

## The Remarkable Subspaces

**Theorem.** The algebra carries exactly one nontrivial involution, the conjugation, and it splits the algebra as the direct sum of its fixed and anti-fixed subspaces,

$$
\mathbb{D} = \mathbb{R}_{\mathbb{D}} \oplus j\mathbb{R}_{\mathbb{D}}, \qquad \mathbb{R}_{\mathbb{D}} = \mathbb{R}1, \qquad j\mathbb{R}_{\mathbb{D}} = \mathbb{R}j ,
$$

of real dimension one each; the idempotent basis gives the finer decomposition $\mathbb{D} = \mathbb{R}\Pi_1 \oplus \mathbb{R}\Pi_2$, whose two lines are the minimal ideals. The real line is closed under the product and is a copy of $\mathbb{R}$; the split imaginary line is not closed, since $j^2 = +1$ lands in $\mathbb{R}1$; the idempotent lines carry the vanishing of the norm. The four lines are pairwise independent, and every pair of distinct ones spans the algebra.

**Proof.** An element satisfies $\bar Q_1 = Q_1$ exactly when $Q_1\in\mathbb{R}1$ and $\bar Q_1 = -Q_1$ exactly when $Q_1\in\mathbb{R}j$; the two are the coordinate blocks of the basis $1, j$ and meet only at the origin. The idempotent lines are the eigenspaces of $J$ and, since $\Pi_1\Pi_2=0$, the two minimal ideals; the norm vanishes on them because $\langle \Pi_1\rangle_{\natural} = \Pi_1\bar\Pi_1 = \Pi_1\Pi_2 = 0$. That every pair of distinct lines spans $\mathbb{D}$ is the dimension count in the plane. The lattice, its collapse to a single edge, and the two decompositions are *Split-Complexoid Subspaces*, *Decompositions and Comparison of the Remarkable Subspaces of the Split-Complexoid* and *Remarkable Subspaces of the Split-Complexoid and the Two Forms*.

## The Matrix Models

**Theorem.** The algebra has two real matrix models. The **regular representation** sends $Q_1 = q_1+jq'_1$ to the hyperbolic matrix $\mathsf M_2(Q_1) = q_1I + q'_1J$ in $M_2(\mathbb{R})$, multiplicative and faithful, of determinant $\langle Q_1\rangle_{\natural} = q_1^2-q'^2_1$ and trace the algebra trace $2q_1$. The **doubled model** sends $Q_1$ to $\operatorname{diag}(\mathsf M_2(Q_1),\mathsf M_2(Q_1))$ in $M_4(\mathbb{R})$, of determinant $\langle Q_1\rangle_{\natural}^2$ and trace $4q_1$.

**Proof.** Multiplication by $Q_1$ is the $\mathbb{R}$-linear map $Q_2\mapsto Q_1Q_2$, whose matrix in the basis $1, j$ is $q_1I + q'_1J$ because $J$ is multiplication by $j$ and $Q_1 = q_1 + q'_1j$; it is multiplicative since the product is associative. Its determinant is $\det(q_1I+q'_1J) = q_1^2-q'^2_1 = \langle Q_1\rangle_{\natural}$, and its trace is $2q_1$. The doubled model is that model on the module $\mathbb{D}\oplus\mathbb{D}$, whose determinant and trace are squared and doubled by the module rank. The commutant of the $2\times2$ image is the image itself, of real dimension two; the commutant of the $4\times4$ image is the ring of $2\times2$ matrices over $\mathbb{D}$, of real dimension eight. The models are *The Matrix Element Representations of the Split-Complexoid*.

## Comparisons with the Ring

**Theorem.** The two products, read on one and the same pair, coincide exactly when the second slot is real and are opposite exactly when it is purely split imaginary; their half sum and half difference split the second factor into its real and split imaginary parts. The bar is an automorphism of the bilinear product, $\overline{Q_1Q_2} = \bar Q_1\bar Q_2$, and converts the sesquilinear product into a bilinear one of the conjugate pair, $\overline{Q_1\bar Q_2} = \bar Q_1Q_2$.

**Proof.** $Q_1\bar Q_2 = Q_1Q_2$ is $Q_1(\bar Q_2 - Q_2) = 0$, that is, $Q_2$ real; $Q_1\bar Q_2 = -Q_1Q_2$ is $Q_1(\bar Q_2 + Q_2) = 0$, that is, $Q_2$ purely split imaginary. The two displayed identities are conjugation applied to the two products; they are the rows of the comparison table of *Relations and Comparison Between the Two Products of the Split-Complexoid Space*.

**Remark (the adjoints).** The two pairings carry two adjoints of an $\mathbb{R}$-linear map: the transpose keeps the parameter of the form and the adjoint conjugates it, so that the ordinary multiplication by $Q$ has adjoint the multiplication by $\bar Q$, the sesquilinear right multiplication $R_{Q_2}(X) = X\bar Q_2$ has adjoint the ordinary multiplication by $Q_2$, and the left multiplication of $\star$ is self-adjoint. This is the split instance of the adjoint bookkeeping of the sesqualgebra layer.

## Summary

The split-complexoid is the pair $(\mathbb{D},\bar\cdot)$ read over $\mathbb{R}$: the plane $\mathbb{D}_{\mathbb{R}}$ of real dimension two with the product structure $J$. From that pair alone the category reads off every structure the algebra carries beside its ring axioms. The carrier has two products — the ring product $Q_1Q_2$ and the sesquilinear product $Q_1\bar Q_2$ — whose scalar parts are two forms, the symmetric $\langle\cdot,\cdot\rangle$ and the conjugate-symmetric $\langle\cdot,\cdot\rangle_{*}$, with the same Gram matrix $[1]$. Their algebraic norms are $\langle Q_1\rangle = Q_1^2$, $\mathbb{D}$-valued and anisotropic, and $\langle Q_1\rangle_{*} = q_1^2-q'^2_1$, real and indefinite; both are multiplicative, and neither is definite. The realified signatures are $(2,0)$ for $\langle\cdot,\cdot\rangle$, which is the Euclidean form, and $(1,1)$ for $\langle\cdot,\cdot\rangle_{*}$, and the split sign exchanges them with respect to the complex case.

The sesquilinear product is non-associative and conjugate-commutative, with associator confined to the anti-self-adjoint part of the third slot, and its ternary product $\{Q_1,Q_2,Q_3\} = Q_1\bar Q_2Q_3$ is a $J^{*}$-algebra. The conjugation splits the algebra into the real and the split imaginary axes, and its commutativity removes the Lie slot and collapses the involution lattice to a single edge. Two matrix models realise the algebra over $\mathbb{R}$, of determinants $\langle\cdot\rangle_{\natural}$ and $\langle\cdot\rangle_{\natural}^2$. The comparison of the two products reads: they coincide on the real part of the second slot and oppose on the split imaginary part.

| Structure | Object | Carrier | What it is |
|---|---|---|---|
| Ring | $\mathbb{D}$ | $\mathbb{D}_{\mathbb{R}}$ | the product $Q_1Q_2$, $\mathbb{D}\cong\mathbb{R}\times\mathbb{R}$ |
| General plain sesqualgebra (GPS) | $(\mathbb{D},\star)$ | $\mathbb{D}_{\mathbb{R}}$ | the product $Q_1\bar Q_2$ |
| Two products | — | $\mathbb{D}_{\mathbb{R}}$ | $Q_1Q_2$, $Q_1\bar Q_2$ |
| Two forms | $B, H$ | $\mathbb{D}_{\mathbb{R}}$ | $Q_1Q_2$, $Q_1\bar Q_2$ as forms, Gram $[1]$ |
| Two algebraic norms | $\langle Q_1\rangle, \langle Q_1\rangle_{*}$ | $\mathbb{D}$ | $Q_1^2$ anisotropic; $q_1^2-q'^2_1$ indefinite |
| Ternary product | $\{Q_1,Q_2,Q_3\}$ | $\mathbb{D}$ | $Q_1\bar Q_2Q_3$, a $J^{*}$-algebra |
| Subspaces | $\mathbb{R}_{\mathbb{D}}, j\mathbb{R}_{\mathbb{D}}$ | $\mathbb{D}_{\mathbb{R}}$ | fixed and anti-fixed lines |
| Matrix models | $\mathsf M_2, \mathsf M_4$ | $M_2(\mathbb{R}), M_4(\mathbb{R})$ | determinants $\langle\cdot\rangle_{\natural}$, $\langle\cdot\rangle_{\natural}^2$ |
| Realification | $J$ | $\mathbb{D}_{\mathbb{R}}$ | multiplication by $j$, $J^2 = +\operatorname{id}$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q_1 = q_1 + jq'_1$ | element of $\mathbb{D}$ |
| $\mathbb{D}_{\mathbb{R}}$ | $\mathbb{D}$ read as a real vector space, basis $1, j$ |
| $J(Q_1) = jQ_1$ | the real-linear product structure, $J^2 = +\operatorname{id}$ |
| $\Pi_1 = \tfrac12(1+j)$, $\Pi_2 = \tfrac12(1-j)$ | the idempotents, the eigenlines of $J$ |
| $Q_1Q_2$, $Q_1\bar Q_2$ | the two products |
| $\langle Q_1,Q_2\rangle = Q_1Q_2$, $\langle Q_1,Q_2\rangle_{*} = Q_1\bar Q_2$ | the two forms |
| $\langle Q_1\rangle = Q_1^2$, $\langle Q_1\rangle_{*} = \langle Q_1\rangle_{\natural} = q_1^2-q'^2_1$ | the two algebraic norms |
| $Q_1\star Q_2 = Q_1\bar Q_2$ | the sesquilinear product of the GPS |
| $\{Q_1,Q_2,Q_3\} = Q_1\bar Q_2Q_3$ | the ternary product, $J^{*}$-algebra |
| $\mathbb{R}_{\mathbb{D}}$, $j\mathbb{R}_{\mathbb{D}}$ | real and split imaginary axes |
| $\mathsf M_2(Q_1) = q_1I + q'_1J$ | the hyperbolic matrix model |

## Further Reading

- [Split-Complex Algebra](split-complex-algebra.html), [Split-Complex Norm and Invertibility](split-complex-norm-and-invertibility.html) and [The Specificities of the Split-Complex Algebra](the-specificities-of-the-split-complex-algebra.html), for the ring itself: construction, zero divisors, idempotents, ideals, the norm and the group of units.
- [The Split-Complexoid as a Vector Space over $\mathbb{R}$](the-split-complexoid-as-a-vector-space-over-r.html), [Split-Complexoid Subspaces](split-complexoid-subspaces.html) and [Decompositions and Comparison of the Remarkable Subspaces of the Split-Complexoid](decompositions-and-comparison-of-the-remarkable-subspaces-of-the-split-complexoid.html), for the real reading of the carrier, the involution and its two blocks.
- [The Two Products of the Split-Complexoid Space](the-two-products-of-the-split-complexoid-space.html), [Relations and Comparison Between the Two Products of the Split-Complexoid Space](relations-and-comparison-between-the-two-products-of-the-split-complexoid-space.html) and [The Two Forms and the Two Algebraic Norms of the Split-Complexoid Space](the-two-forms-and-the-two-algebraic-norms-of-the-split-complexoid-space.html), for the two products, their comparison, and their forms and algebraic norms.
- [Remarkable Subspaces and the Two Products of the Split-Complexoid Space](remarkable-subspaces-and-the-two-products-of-the-split-complexoid-space.html) and [Remarkable Subspaces of the Split-Complexoid and the Two Forms](remarkable-subspaces-of-the-split-complexoid-and-the-two-forms.html), for the products and the forms read on the distinguished subspaces.
- [The Sesquilinear Product of the Split-Complexoid Space](the-sesquilinear-product-of-the-split-complexoid-space.html) and [The Hermitian Form and the Cone of the Split-Complexoid Algebra](the-hermitian-form-and-the-cone-of-the-split-complexoid-algebra.html), for the GPS, the ternarisation and the indefinite cone.
- [The Matrix Element Representations of the Split-Complexoid](the-matrix-element-representations-of-the-split-complexoid.html) and [The Realification and the Effect of the Change of Scalars on the Split-Complexoid](the-realification-and-the-effect-of-the-change-of-scalars-on-the-split-complexoid.html), for the two matrix models and the two scalar readings.
- [Introduction to the Complexoid Algebraic Structures](introduction-to-the-complexoid-algebraic-structures.html), for the complex rung of the same ladder, where the carrier is a field and the Hermitian form is definite.
- [Hermitian Forms over Algebras and Norms](hermitian-forms-over-algebras-and-norms.html), [The Norm Defined by a Form](the-norm-defined-by-a-form.html), [Jordan Triples with an Involution](jordan-triples-with-an-involution.html) and *Algebraic J*-Algebras, for the general theory of a sesqualgebra, of a ternary product and of an algebraic norm.
