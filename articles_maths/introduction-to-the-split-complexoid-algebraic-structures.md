
# __Introduction to the Split-Complexoid Algebraic Structures__

## Introduction

The split-complex numbers are a commutative ring, and that ring is the subject of *Split-Complex Algebra*. The same underlying set, read as an algebra over $\mathbb{R}$, carries structures the ring axioms do not name: a real-linear product structure, a second product beside the multiplication, two pairings with their algebraic norms, a ternary operation, a pair of real matrix models, and a lattice of distinguished subspaces. This category gathers those structures, and this article states what they are and how they hang together.

The guiding distinction is the one the whole synthetic part of the corpus draws: a *number system* is one object and its *algebraic structures* are the several algebras the same carrier admits. For $\mathbb{D}$ the carrier is the plane $\mathbb{D}_{\mathbb{R}}$ of real dimension two, and the structures are obtained from the single datum of the algebra together with its conjugation. The split sign $j^2=+1$ is the whole difference from the complex field, and it is the source of every degeneracy recorded below: the carrier is a ring and not a field, the Hermitian form is indefinite, the commutator lies on the split imaginary line, and no definite multiplicative norm exists. There is no third product and no hidden operation: the count below is exhaustive.

**Conventions.** $A = a + ja'$ and $C = c + jc'$ are elements of $\mathbb{D}$, with $a,a',c,c'\in\mathbb{R}$; $\bar A = a - ja'$ is the conjugate; $j^2 = +1$; the idempotents are $\Pi_{1,2} = \tfrac12(1\pm j)$, the idempotent coordinates are $A_\pm = a\pm a'$, and $A = A_+\Pi_1 + A_-\Pi_2$; $\mathrm{Sc}$, $\mathrm{Re}$ and $\mathrm{Im}$ are read in $\mathbb{D}$. The algebra read over $\mathbb{R}$ is written $\mathbb{D}_{\mathbb{R}}$, with real basis $1, j$. The two products are written $AC$ for the ring product and $A\bar C$ for the sesquilinear one, following *Conventions in Mathematics*; the letters $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ are reserved for forms and norms.

## The Split-Complexoid

**Definition.** The **split-complexoid** is the pair $(\mathbb{D}, \bar\cdot)$ read as an algebra over $\mathbb{R}$: the real vector space $\mathbb{D}_{\mathbb{R}}$ together with the involution $\bar\cdot$. Every structure of this category is built from that pair alone.

**Proposition.** The realification doubles no structure and loses none: $\mathbb{D}_{\mathbb{R}}$ has real basis $1, j$ and real dimension $2$, and the real-linear multiplication by $j$ is the operator $J(A) = jA$, an involution of square $+\operatorname{id}$ with the two real eigenlines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$. A real-linear map of the plane is $\mathbb{D}$-linear exactly when it commutes with $J$ and conjugate-linear exactly when it anticommutes; the $\mathbb{D}$-linear endomorphisms are the multiplications by an element and form the plane $\operatorname{End}_{\mathbb{D}}(\mathbb{D}) \cong \mathbb{D}$, the conjugate-linear ones form the complementary plane, and together they fill $\operatorname{End}_{\mathbb{R}}(\mathbb{D}) \cong M_2(\mathbb{R})$.

**Proof.** That $1, j$ is a real basis and that $\dim_{\mathbb{R}}\mathbb{D} = 2$ is immediate. The map $J$ is $\mathbb{R}$-linear, $J^2(A) = j(jA) = j^2A = A$, and $J(A) = \lambda A$ forces $\lambda = \pm1$ for $A\neq0$, the eigenspaces being $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$. A real-linear $T$ commutes with $J$ exactly when $T(jA) = jT(A)$, which is $\mathbb{D}$-linearity, and anticommutes exactly when $T(jA) = -jT(A)$; the two classes are the $\pm1$ eigenspaces of conjugation by $J$ on $\operatorname{End}_{\mathbb{R}}(\mathbb{D})$, of dimensions $2$ and $2$. The commuting maps are $A\mapsto \lambda A$, and the two-dimensional space is $\mathbb{D}$. The whole development is *The Split-Complexoid as a Vector Space over $\mathbb{R}$*.

**Remark.** The complexification $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{D}\cong\mathbb{C}\times\mathbb{C}$ is **not** a field: the polynomial $x^2-1$ already factors over $\mathbb{R}$, and the extension of scalars carries the zero divisors with it. The complex field is the other rung of the ladder, where the adjoined root does not exist over $\mathbb{R}$; the passage between the two rungs is *The Realification and the Effect of the Change of Scalars on the Split-Complexoid*.

## The Two Products

**Definition.** The **two products** of the split-complex space are the **general plain bilinear** product and the **general plain sesquilinear** product,

$$
AC = (ac + a'c') + (ac' + a'c)j, \qquad\qquad A\bar C = (ac - a'c') + (a'c - ac')j .
$$

**Theorem.** The product $AC$ is $\mathbb{D}$-bilinear, associative, commutative and unital; it is the multiplication of the algebra, and $\mathbb{D}$ is a ring with zero divisors and not a field. The product $A\bar C$ is $\mathbb{D}$-linear in the first slot and conjugate-linear in the second, conjugate-commutative, right-unital but not left-unital, and not associative.

**Proof.** The formulas are the ring multiplication and the same multiplication with $C$ replaced by $\bar C$. Bilinearity, associativity, commutativity and the two-sided unit $1$ for $AC$ are the ring axioms, and the zero divisors $\Pi_1\Pi_2=0$ show that the ring is not a field. For $A\bar C$, linearity in $A$ and conjugate-linearity in $C$ are read from the formula, conjugate-commutativity $A\bar C = \overline{C\bar A}$ follows by conjugating, the right unit is $1$ since $A\bar 1 = A$, and $1$ is not a left unit since $1\bar j = -j \neq j$; associativity fails at the witness $(1,1,j)$, where $(1\star1)\star j = -j$ against $1\star(1\star j) = j$. The two products and their property table are *The Two Products of the Split-Complexoid Space* and *Relations and Comparison Between the Two Products of the Split-Complexoid Space*.

**Remark (the idempotent coordinates).** With $A = A_+\Pi_1 + A_-\Pi_2$ and $C = C_+\Pi_1 + C_-\Pi_2$ the ring product is componentwise and the sesquilinear one exchanges the two coordinates of the second factor,

$$
AC \leftrightarrow (A_+C_+, A_-C_-), \qquad\qquad A\bar C \leftrightarrow (A_+C_-, A_-C_+),
$$

which is the reason $\mathbb{D}\cong\mathbb{R}\times\mathbb{R}$ and the reason the sesquilinear product has no left unit and cannot be associative.

## The Two Forms and Their Algebraic Norms

**Definition.** The **two forms** are the scalar parts of the two products,

$$
\langle A,C\rangle = AC, \qquad\qquad \langle A,C\rangle_{*} = A\bar C ,
$$

named the **general plain bilinear form** and the **Hermitian form**; their **algebraic norms** are the values at the two equal arguments, $\langle A\rangle = A^2$ and $\langle A\rangle_{*} = A\bar A = \langle A\rangle_{\natural}$.

**Theorem.** $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{*}$ have the same Gram matrix $[1]$ in the basis $1$ and are separated by their symmetry alone, $\langle\cdot,\cdot\rangle$ symmetric and $\langle\cdot\rangle_{*}$ conjugate-symmetric. Their algebraic norms are $\langle A\rangle = A^2$, $\mathbb{D}$-valued and anisotropic, and $\langle A\rangle_{*} = a^2 - a'^2$, real and indefinite. **Both are multiplicative**, and **neither is a definite real norm**: the $\mathbb{D}$-valued $\langle\cdot\rangle$ defines no order and the real $\langle\cdot\rangle_{*}$ is indefinite, while what is definite is the realified *form* $\operatorname{Re}B$, of signature $(2,0)$, against the indefinite realification $\operatorname{Re}H$ of signature $(1,1)$.

**Proof.** The Gram matrix is $[\langle 1,1\rangle] = [1]$ and $[\langle 1,1\rangle_{*}] = [1]$. Symmetry of $\langle\cdot,\cdot\rangle$ is commutativity of the ring; conjugate-symmetry $\langle A,C\rangle_{*} = \overline{\langle C,A\rangle_{*}}$ is conjugate-commutativity. The form $\langle A\rangle = (a+ja')^2$ vanishes only at $A = 0$ but takes values in $\mathbb{D}$ and defines no order; $\langle A\rangle_{*} = a^2-a'^2$ is real, changes sign, and vanishes exactly on the union of the two null lines, which is the zero-divisor set. Multiplicativity is $\langle AC\rangle = A^2C^2$ and $\langle AC\rangle_{*} = A\bar AC\bar C = \langle A\rangle_{*}\langle C\rangle_{*}$. The two realified signatures are computed from the real parts $\operatorname{Re}\langle A,C\rangle = ac+a'c'$ and $\operatorname{Re}\langle A,C\rangle_{*} = ac-a'c'$. That no definite multiplicative norm exists, because $\Pi_1\Pi_2=0$ would force $\nu(\Pi_1)\nu(\Pi_2)=0$, is the theorem of *The Two Forms and the Two Algebraic Norms of the Split-Complexoid Space*.

## The General Plain Sesqualgebra and the Ternary Product

**Definition.** The **general plain sesqualgebra (GPS)** over $\mathbb{D}$ is the pair $(\mathbb{D}, \star)$ with the sesquilinear product $A\star C = A\bar C$.

**Theorem.** The associator of $\star$ is $[A,C,D] = A\bar C(\bar D - D)$, nonzero but confined to the anti-self-adjoint part of the third slot; its **ternary product** $\{A,C,D\} = A\bar CD$ is symmetric in the outer slots, Hermitian-symmetric, $\overline{\{A,C,D\}} = \{\bar A,\bar C,\bar D\}$, and satisfies the Jordan triple identity, so that the structure is a **$J^{*}$-algebra** (a Jordan triple with an involution).

**Proof.** The associator is $[A,C,D] = (A\bar C)\bar D - A\bar C D = A\bar C(\bar D - D)$, which vanishes exactly when $D$ is real, with the witness $[j,j,j] = 2j$. Outer symmetry is $\{A,C,D\} = A\bar CD = D\bar CA = \{D,C,A\}$ by commutativity, and Hermitian symmetry follows by conjugating the three entries. The Jordan triple identity is the model computation $xy^{*}z$ of an associative algebra with a sesquilinear involution; it is the axiom of *Jordan Triples with an Involution* and *Algebraic J\*-Algebras*. The article is *The Sesquilinear Product of the Split-Complexoid Space*, and the form theory of the second slot is *The Hermitian Form and the Cone of the Split-Complexoid Algebra*.

## The Remarkable Subspaces

**Theorem.** The algebra carries exactly one nontrivial involution, the conjugation, and it splits the algebra as the direct sum of its fixed and anti-fixed subspaces,

$$
\mathbb{D} = \mathbb{R}_{\mathbb{D}} \oplus j\mathbb{R}_{\mathbb{D}}, \qquad \mathbb{R}_{\mathbb{D}} = \mathbb{R}1, \qquad j\mathbb{R}_{\mathbb{D}} = \mathbb{R}j ,
$$

of real dimension one each; the idempotent basis gives the finer decomposition $\mathbb{D} = \mathbb{R}\Pi_1 \oplus \mathbb{R}\Pi_2$, whose two lines are the minimal ideals. The real line is closed under the product and is a copy of $\mathbb{R}$; the split imaginary line is not closed, since $j^2 = +1$ lands in $\mathbb{R}1$; the idempotent lines carry the vanishing of the norm. The four lines are pairwise independent, and every pair of distinct ones spans the algebra.

**Proof.** An element satisfies $\bar A = A$ exactly when $A\in\mathbb{R}1$ and $\bar A = -A$ exactly when $A\in\mathbb{R}j$; the two are the coordinate blocks of the basis $1, j$ and meet only at the origin. The idempotent lines are the eigenspaces of $J$ and, since $\Pi_1\Pi_2=0$, the two minimal ideals; the norm vanishes on them because $\langle \Pi_1\rangle_{\natural} = \Pi_1\bar\Pi_1 = \Pi_1\Pi_2 = 0$. That every pair of distinct lines spans $\mathbb{D}$ is the dimension count in the plane. The lattice, its collapse to a single edge, and the two decompositions are *Split-Complexoid Subspaces*, *Decompositions and Comparison of the Remarkable Subspaces of the Split-Complexoid* and *Remarkable Subspaces of the Split-Complexoid and the Two Forms*.

## The Matrix Models

**Theorem.** The algebra has two real matrix models. The **regular representation** sends $A = a+ja'$ to the hyperbolic matrix $\mathsf M_2(A) = aI + a'J$ in $M_2(\mathbb{R})$, multiplicative and faithful, of determinant $\langle A\rangle_{\natural} = a^2-a'^2$ and trace the algebra trace $2a$. The **doubled model** sends $A$ to $\operatorname{diag}(\mathsf M_2(A),\mathsf M_2(A))$ in $M_4(\mathbb{R})$, of determinant $\langle A\rangle_{\natural}^2$ and trace $4a$.

**Proof.** Multiplication by $A$ is the $\mathbb{R}$-linear map $C\mapsto AC$, whose matrix in the basis $1, j$ is $aI + a'J$ because $J$ is multiplication by $j$ and $A = a + a'j$; it is multiplicative since the product is associative. Its determinant is $\det(aI+a'J) = a^2-a'^2 = \langle A\rangle_{\natural}$, and its trace is $2a$. The doubled model is that model on the module $\mathbb{D}\oplus\mathbb{D}$, whose determinant and trace are squared and doubled by the module rank. The commutant of the $2\times2$ image is the image itself, of real dimension two; the commutant of the $4\times4$ image is the ring of $2\times2$ matrices over $\mathbb{D}$, of real dimension eight. The models are *The Matrix Element Representations of the Split-Complexoid*.

## Comparisons with the Ring

**Theorem.** The two products, read on one and the same pair, coincide exactly when the second slot is real and are opposite exactly when it is purely split imaginary; their half sum and half difference split the second factor into its real and split imaginary parts. The bar is an automorphism of the bilinear product, $\overline{AC} = \bar A\bar C$, and converts the sesquilinear product into a bilinear one of the conjugate pair, $\overline{A\bar C} = \bar AC$.

**Proof.** $A\bar C = AC$ is $A(\bar C - C) = 0$, that is, $C$ real; $A\bar C = -AC$ is $A(\bar C + C) = 0$, that is, $C$ purely split imaginary. The two displayed identities are conjugation applied to the two products; they are the rows of the comparison table of *Relations and Comparison Between the Two Products of the Split-Complexoid Space*.

**Remark (the adjoints).** The two pairings carry two adjoints of an $\mathbb{R}$-linear map: the transpose keeps the parameter of the form and the adjoint conjugates it, so that the ordinary multiplication by $\langle\cdot,\cdot\rangle$ has adjoint the multiplication by $\bar B$, the sesquilinear right multiplication $R_C(X) = X\bar C$ has adjoint the ordinary multiplication by $C$, and the left multiplication of $\star$ is self-adjoint. This is the split instance of the adjoint bookkeeping of the sesqualgebra layer.

## Summary

The split-complexoid is the pair $(\mathbb{D},\bar\cdot)$ read over $\mathbb{R}$: the plane $\mathbb{D}_{\mathbb{R}}$ of real dimension two with the product structure $J$. From that pair alone the category reads off every structure the algebra carries beside its ring axioms. The carrier has two products — the ring product $AC$ and the sesquilinear product $A\bar C$ — whose scalar parts are two forms, the symmetric $\langle\cdot,\cdot\rangle$ and the conjugate-symmetric $\langle\cdot,\cdot\rangle_{*}$, with the same Gram matrix $[1]$. Their algebraic norms are $\langle A\rangle = A^2$, $\mathbb{D}$-valued and anisotropic, and $\langle A\rangle_{*} = a^2-a'^2$, real and indefinite; both are multiplicative, and neither is definite. The realified signatures are $(2,0)$ for $\langle\cdot,\cdot\rangle$, which is the Euclidean form, and $(1,1)$ for $\langle\cdot,\cdot\rangle_{*}$, and the split sign exchanges them with respect to the complex case.

The sesquilinear product is non-associative and conjugate-commutative, with associator confined to the anti-self-adjoint part of the third slot, and its ternary product $\{A,C,D\} = A\bar CD$ is a $J^{*}$-algebra. The conjugation splits the algebra into the real and the split imaginary axes, and its commutativity removes the Lie slot and collapses the involution lattice to a single edge. Two matrix models realise the algebra over $\mathbb{R}$, of determinants $\langle\cdot\rangle_{\natural}$ and $N^2$. The comparison of the two products reads: they coincide on the real part of the second slot and oppose on the split imaginary part.

| Structure | Object | Carrier | What it is |
|---|---|---|---|
| Ring | $\mathbb{D}$ | $\mathbb{D}_{\mathbb{R}}$ | the product $AC$, $\mathbb{D}\cong\mathbb{R}\times\mathbb{R}$ |
| General plain sesqualgebra (GPS) | $(\mathbb{D},\star)$ | $\mathbb{D}_{\mathbb{R}}$ | the product $A\bar C$ |
| Two products | — | $\mathbb{D}_{\mathbb{R}}$ | $AC$, $A\bar C$ |
| Two forms | $B, H$ | $\mathbb{D}_{\mathbb{R}}$ | $AC$, $A\bar C$ as forms, Gram $[1]$ |
| Two algebraic norms | $\langle A\rangle, \langle A\rangle_{*}$ | $\mathbb{D}$ | $A^2$ anisotropic; $a^2-a'^2$ indefinite |
| Ternary product | $\{A,C,D\}$ | $\mathbb{D}$ | $A\bar CD$, a $J^{*}$-algebra |
| Subspaces | $\mathbb{R}_{\mathbb{D}}, j\mathbb{R}_{\mathbb{D}}$ | $\mathbb{D}_{\mathbb{R}}$ | fixed and anti-fixed lines |
| Matrix models | $\mathsf M_2, \mathsf M_4$ | $M_2(\mathbb{R}), M_4(\mathbb{R})$ | determinants $\langle\cdot\rangle_{\natural}$, $N^2$ |
| Realification | $J$ | $\mathbb{D}_{\mathbb{R}}$ | multiplication by $j$, $J^2 = +\operatorname{id}$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A = a + ja'$ | element of $\mathbb{D}$ |
| $\mathbb{D}_{\mathbb{R}}$ | $\mathbb{D}$ read as a real vector space, basis $1, j$ |
| $J(A) = jA$ | the real-linear product structure, $J^2 = +\operatorname{id}$ |
| $\Pi_{1,2} = \tfrac12(1\pm j)$ | the idempotents, the eigenlines of $J$ |
| $AC$, $A\bar C$ | the two products |
| $\langle A,C\rangle = AC$, $\langle A,C\rangle_{*} = A\bar C$ | the two forms |
| $\langle A\rangle = A^2$, $\langle A\rangle_{*} = \langle A\rangle_{\natural} = a^2-a'^2$ | the two algebraic norms |
| $A\star C = A\bar C$ | the sesquilinear product of the GPS |
| $\{A,C,D\} = A\bar CD$ | the ternary product, $J^{*}$-algebra |
| $\mathbb{R}_{\mathbb{D}}$, $j\mathbb{R}_{\mathbb{D}}$ | real and split imaginary axes |
| $\mathsf M_2(A) = aI + a'J$ | the hyperbolic matrix model |

## Further Reading

- *Split-Complex Algebra* (`articles_maths/split-complex-algebra.md`), *Split-Complex Norm and Invertibility* (`articles_maths/split-complex-norm-and-invertibility.md`) and *The Specificities of the Split-Complex Algebra* (`articles_maths/the-specificities-of-the-split-complex-algebra.md`), for the ring itself: construction, zero divisors, idempotents, ideals, the norm and the group of units.
- *The Split-Complexoid as a Vector Space over $\mathbb{R}$* (`articles_maths/the-split-complexoid-as-a-vector-space-over-r.md`), *Split-Complexoid Subspaces* (`articles_maths/split-complexoid-subspaces.md`) and *Decompositions and Comparison of the Remarkable Subspaces of the Split-Complexoid* (`articles_maths/decompositions-and-comparison-of-the-remarkable-subspaces-of-the-split-complexoid.md`), for the real reading of the carrier, the involution and its two blocks.
- *The Two Products of the Split-Complexoid Space* (`articles_maths/the-two-products-of-the-split-complexoid-space.md`), *Relations and Comparison Between the Two Products of the Split-Complexoid Space* (`articles_maths/relations-and-comparison-between-the-two-products-of-the-split-complexoid-space.md`) and *The Two Forms and the Two Algebraic Norms of the Split-Complexoid Space* (`articles_maths/the-two-forms-and-the-two-algebraic-norms-of-the-split-complexoid-space.md`), for the two products, their comparison, and their forms and algebraic norms.
- *Remarkable Subspaces and the Two Products of the Split-Complexoid Space* (`articles_maths/remarkable-subspaces-and-the-two-products-of-the-split-complexoid-space.md`) and *Remarkable Subspaces of the Split-Complexoid and the Two Forms* (`articles_maths/remarkable-subspaces-of-the-split-complexoid-and-the-two-forms.md`), for the products and the forms read on the distinguished subspaces.
- *The Sesquilinear Product of the Split-Complexoid Space* (`articles_maths/the-sesquilinear-product-of-the-split-complexoid-space.md`) and *The Hermitian Form and the Cone of the Split-Complexoid Algebra* (`articles_maths/the-hermitian-form-and-the-cone-of-the-split-complexoid-algebra.md`), for the GPS, the ternarisation and the indefinite cone.
- *The Matrix Element Representations of the Split-Complexoid* (`articles_maths/the-matrix-element-representations-of-the-split-complexoid.md`) and *The Realification and the Effect of the Change of Scalars on the Split-Complexoid* (`articles_maths/the-realification-and-the-effect-of-the-change-of-scalars-on-the-split-complexoid.md`), for the two matrix models and the two scalar readings.
- *Introduction to the Complexoid Algebraic Structures* (`articles_maths/introduction-to-the-complexoid-algebraic-structures.md`), for the complex rung of the same ladder, where the carrier is a field and the Hermitian form is definite.
- *Hermitian Forms over Algebras and Norms*, *The Norm Defined by a Form*, *Jordan Triples with an Involution* and *Algebraic J*-Algebras, for the general theory of a sesqualgebra, of a ternary product and of an algebraic norm.
