
# __Introduction to the Complexoid Algebraic Structures__

## Introduction

The complex numbers are a field, and that field is the subject of *The Complex Numbers ($\mathbb{C}$)*. The same underlying set, read as an algebra over $\mathbb{R}$, carries structures the field axioms do not name: a real-linear complex structure, a second product beside the multiplication, two pairings with their algebraic norms, a ternary operation, a pair of matrix models, and a subspace lattice. This category gathers those structures, and this article states what they are and how they hang together.

The guiding distinction is the one the whole synthetic part of the corpus draws: a *number system* is one object and its *algebraic structures* are the several algebras the same carrier admits. For $\mathbb{C}$ the carrier is the plane $\mathbb{C}_{\mathbb{R}}$ of real dimension two, and the structures are obtained from the single datum of the field together with its conjugation. There is no third product and no hidden operation: the count below is exhaustive.

**Conventions.** $A = a + ia'$ and $C = c + ic'$ are elements of $\mathbb{C}$, with $a,a',c,c'\in\mathbb{R}$; $\bar A = a - ia'$ is the conjugate; $i^2 = -1$; $\mathrm{Sc}$, $\mathrm{Re}$ and $\mathrm{Im}$ are read in $\mathbb{C}$. The algebra $\mathbb{C}$ read over $\mathbb{R}$ is written $\mathbb{C}_{\mathbb{R}}$, with real basis $1, i$. The two products are written by juxtaposition: $AC$ for the field product and $A\bar C$ for the sesquilinear one, following *Conventions in Mathematics*.

## The Complexoid

**Definition.** The **complexoid** is the pair $(\mathbb{C}, \bar{\cdot})$ read as an algebra over $\mathbb{R}$: the real vector space $\mathbb{C}_{\mathbb{R}}$ together with the involution $\bar{\cdot}$. Every structure of this category is built from that pair alone.

**Proposition.** The realification doubles no structure and loses none: $\mathbb{C}_{\mathbb{R}}$ has real basis $1, i$ and real dimension $2$, its real-linear multiplication by $i$ is the complex structure $J(A) = iA$ with $J^2 = -\operatorname{id}$ and no real eigenvector, and a real-linear map of the plane is complex-linear exactly when it commutes with $J$ and conjugate-linear exactly when it anticommutes. The complex-linear endomorphisms are multiplication by a complex number and form $\operatorname{End}_{\mathbb{C}}(\mathbb{C})\cong\mathbb{C}$; the conjugate-linear ones form the complementary plane; together they fill $\operatorname{End}_{\mathbb{R}}(\mathbb{C})\cong M_2(\mathbb{R})$.

**Proof.** That $1, i$ is a real basis and that $\dim_{\mathbb{R}}\mathbb{C} = 2$ is immediate. The map $J$ is $\mathbb{R}$-linear, $J^2(A) = i(iA) = -A$, and $J(A) = \lambda A$ forces $\lambda = \pm i\notin\mathbb{R}$ for $A\neq0$. A real-linear $T$ commutes with $J$ exactly when $T(iA) = iT(A)$, which is $\mathbb{C}$-linearity, and anticommutes exactly when $T(iA) = -iT(A)$, which is conjugate-linearity; the two classes are the $\pm1$ eigenspaces of conjugation by $J$ on $\operatorname{End}_{\mathbb{R}}(\mathbb{C})$, of dimensions $2$ and $2$. The complex-linear maps are $A\mapsto \lambda A$, and the two-dimensional space is $\mathbb{C}$. The whole development is *The Complexoid as a Vector Space over $\mathbb{R}$*.

**Remark.** The complexification $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$ is **not** the complex reading: it is the sum of the space and its conjugate, of complex dimension two, whereas $\mathbb{C}$ over itself is the line of complex dimension one. What returns the complex reading is $J$, not a scalar extension.

## The Two Products

**Definition.** The **two products** of the complex space are the **general plain bilinear** product and the **general plain sesquilinear** product,

$$
AC = (ac - a'c') + i(ac' + a'c), \qquad\qquad A\bar C = (ac + a'c') + i(a'c - ac') .
$$

**Theorem.** The product $AC$ is $\mathbb{C}$-bilinear, associative, commutative, unital and without zero divisors; it is the multiplication of the field. The product $A\bar C$ is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second, conjugate-commutative, right-unital but not left-unital, and not associative.

**Proof.** The formulas are the field multiplication and the same multiplication with $C$ replaced by $\bar C$. Bilinearity, associativity, commutativity and the unit $1$ for $AC$ are the field axioms. For $A\bar C$, linearity in $A$ and conjugate-linearity in $C$ are read from the formula, conjugate-commutativity $A\bar C = \overline{C\bar A}$ follows by conjugating, the right unit is $1$ since $A\bar 1 = A$, and $1$ is not a left unit since $1\bar i = -i \neq i$; associativity fails at the witness $(1, 1, i)$, where $(1\cdot\bar 1)\cdot i = i$ against $1\cdot(\bar 1\cdot i) = -i$. The two products and their property table are *The Two Products of the Complexoid Space* and *Relations and Comparison Between the Two Products*.

## The Two Forms and Their Algebraic Norms

**Definition.** The **two forms** are the scalar parts of the two products,

$$
\langle A,C\rangle = AC, \qquad\qquad \langle A,C\rangle_{*} = A\bar C ,
$$

named the **general plain bilinear form** and the **Hermitian form**; their **algebraic norms** are the values at the two equal arguments, $\langle A\rangle = A^2$ and $\langle A\rangle_{*} = \lvert A\rvert^2$.

**Theorem.** $\langle\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{*}$ have the same Gram matrix $[1]$ in the basis $1$ and are separated by their symmetry alone, $\langle\cdot,\cdot\rangle$ symmetric and $\langle\cdot\rangle_{*}$ conjugate-symmetric. Their algebraic norms are $\langle A\rangle = A^2$, complex-valued and anisotropic, and $\langle A\rangle_{*} = \lvert A\rvert^2 = a^2 + a'^2$, real-valued and positive definite. **Both are multiplicative**, and $\langle\cdot,\cdot\rangle_{*}$ alone is definite.

**Proof.** The Gram matrix is $[\langle 1,1\rangle] = [1]$ and $[\langle 1,1\rangle_{*}] = [1]$. Symmetry of $\langle\cdot,\cdot\rangle$ is commutativity of the field; conjugate-symmetry $\langle A,C\rangle_{*} = \overline{\langle C,A\rangle_{*}}$ is conjugate-commutativity. The forms are $\langle A\rangle = (a+ia')^2$, which vanishes only at $A = 0$ over $\mathbb{C}$ but takes complex values and is anisotropic over $\mathbb{R}$, and $\langle A\rangle_{*} = A\bar A = a^2+a'^2 \geq 0$, zero only at the origin. Multiplicativity is $\langle AC\rangle = A^2C^2$ and $\langle AC\rangle_{*} = A\bar AC\bar C = \langle A\rangle_{*}\langle C\rangle_{*}$. That the complex space is the **degenerate base** of the general four-form construction, where the four forms $\langle\cdot,\cdot\rangle, \langle\cdot,\cdot\rangle_{\natural}, \langle\cdot,\cdot\rangle_{*}, \langle\cdot,\cdot\rangle_{\natural*}$ collapse to the two settings of the second slot with $B = N$ and $H = K$, is *The Two Forms and the Two Algebraic Norms of the Complexoid Space*.

## The General Plain Sesqualgebra and the Ternary Product

**Definition.** The **general plain sesqualgebra (GPS)** over $\mathbb{C}$ is the pair $(\mathbb{C}, \star)$ with the sesquilinear product $A\star C = A\bar C$.

**Theorem.** The associator of $\star$ is $[A,B,C] = A\bar \langle \bar C - C\rangle$, nonzero but confined to the anti-self-adjoint part of the third slot; its **ternary product** $\{A,B,C\} = A\bar BC$ is symmetric in the outer slots, Hermitian-symmetric, $\overline{\{A,B,C\}} = \{\bar A,\bar B,\bar C\}$, and satisfies the Jordan triple identity, so that the structure is a **$J^{*}$-algebra** (a Jordan triple with an involution).

**Proof.** The associator is $[A,B,C] = (A\bar B)\bar C - A\bar B\bar C = A\bar \langle \bar C - C\rangle$, which vanishes exactly when $C$ is real, that is, on the self-adjoint part of the third slot. Outer symmetry is $\{A,B,C\} = A\bar BC = C\bar BA = \{C,B,A\}$ by commutativity, and Hermitian symmetry follows by conjugating the three entries. The Jordan triple identity is checked directly and was verified on random complex triples; it is the axiom of *Jordan Triples with an Involution* and *Algebraic J\*-Algebras*. The article is *The Ternary Product of the Complexoid Space*, and the positivity of the associated Hermitian form is *The Hermitian Form and the Positivity of the Complexoid Algebra*.

## The Remarkable Subspaces

**Theorem.** The complex algebra carries exactly one nontrivial involution, the conjugation, and it splits the algebra as the direct sum of its fixed and anti-fixed subspaces,

$$
\mathbb{C} = \mathbb{R}_{\mathbb{C}} \oplus i\mathbb{R}_{\mathbb{C}}, \qquad \mathbb{R}_{\mathbb{C}} = \mathbb{R}1, \qquad i\mathbb{R}_{\mathbb{C}} = \mathbb{R} i ,
$$

of real dimension one each. The real subspace is closed under multiplication and is a field isomorphic to $\mathbb{R}$; the imaginary subspace is not closed, $(ia')(ib') = -a'b'\in\mathbb{R}1$. The commutator bracket vanishes identically and there is no Lie-algebra slot, which is the commutativity of the field.

**Proof.** An element $A$ satisfies $\bar A = A$ exactly when $A\in\mathbb{R}1$ and $\bar A = -A$ exactly when $A\in\mathbb{R} i$; the two are the coordinate blocks of the basis $1, i$ and meet only at the origin. Closure of the real line and non-closure of the imaginary line are the sign in $i^2 = -1$; the bracket $[A,C] = AC - CA = 0$ because the field is commutative. The lattice and the two blocks are *Complexoid Subspaces*, *Decompositions and Comparison of the Remarkable Subspaces of the Complexoid*, and *Remarkable Subspaces of the Complexoid and the Two Forms*.

## The Matrix Models

**Theorem.** The complex algebra has two real matrix models. The **regular representation** sends $A = a+ia'$ to the Cayley matrix $\mathsf M_2(A) = aI + a'J$ in $M_2(\mathbb{R})$, multiplicative and faithful, of determinant $\langle A\rangle_{*} = a^2+a'^2$ and trace the algebra trace $2a$. The **doubled model** sends $A$ to $\operatorname{diag}(\mathsf M_2(A),\mathsf M_2(A))$ in $M_4(\mathbb{R})$, equivalently to the scalar matrix $A I_2$ of $M_2(\mathbb{C})$, of determinant $\langle A\rangle_{*}^2$ and trace $4a$.

**Proof.** Multiplication by $A$ is the $\mathbb{R}$-linear map $C\mapsto AC$, whose matrix in the basis $1, i$ is $aI + a'J$ because $J$ is multiplication by $i$ and $A = a + a'i$. It is multiplicative since multiplication is associative. Its determinant is $\det(aI+a'J) = a^2+a'^2 = \langle A\rangle_{*}$, and its trace is $2a$. The doubled model is that model on the module $\mathbb{C}\oplus\mathbb{C}$, whose determinant and trace are squared and doubled by the module rank. The commutants are $\mathbb{C}$ and $M_2(\mathbb{C})$ respectively, of real dimensions two and eight. The models are *The Matrix Element Representations of the Complexoid*.

## Comparisons with the Field

**Theorem.** The two products, read on one and the same pair, coincide exactly when the second slot is real and are opposite exactly when it is purely imaginary; their half sum and half difference split the second factor into its real and imaginary parts. The bar is an automorphism of the bilinear product, $\overline{AC} = \bar A\bar C$, and converts the sesquilinear product into a bilinear one of the conjugate pair, $\overline{A\bar C} = \bar A C$.

**Proof.** $A\bar C = AC$ is $A(\bar C - C) = 0$, that is, $C$ real; $A\bar C = -AC$ is $A(\bar C + C) = 0$, that is, $C$ purely imaginary. The two displayed identities are conjugation applied to the two products; they are the rows of the comparison table of *Relations and Comparison Between the Two Products*.

**Remark (the adjoints).** The two pairings carry two adjoints of an $\mathbb{R}$-linear map: the transpose keeps the parameter of the form and the adjoint conjugates it, so that multiplication by $A$ has transpose itself and adjoint the multiplication by $\bar A$, and the two agree exactly for real $A$. This is the complex instance of the adjoint bookkeeping of the sesqualgebra layer.

## Summary

The complexoid is the pair $(\mathbb{C},\bar\cdot)$ read over $\mathbb{R}$: the plane $\mathbb{C}_{\mathbb{R}}$ of real dimension two with the complex structure $J$. From that pair alone the category reads off every structure the field carries beside its field axioms. The carrier has two products — the field product $AC$ and the sesquilinear product $A\bar C$ — whose scalar parts are two forms, the symmetric $\langle\cdot,\cdot\rangle$ and the conjugate-symmetric $\langle\cdot,\cdot\rangle_{*}$, with the same Gram matrix $[1]$. Their algebraic norms are $\langle A\rangle = A^2$, complex and anisotropic, and $\langle A\rangle_{*} = \lvert A\rvert^2$, real and positive definite; both are multiplicative, and $\langle\cdot,\cdot\rangle_{*}$ alone is definite. The complex space is the degenerate base of the general four-form construction: the four forms collapse to two, $B = N$ and $H = K$.

The sesquilinear product is non-associative and conjugate-commutative, with associator confined to the anti-self-adjoint part of the third slot, and its ternary product $\{A,B,C\} = A\bar BC$ is a $J^{*}$-algebra. The conjugation splits the algebra into the real and the imaginary axes, and the field's commutativity removes the Lie slot. Two matrix models realise the algebra over $\mathbb{R}$, of determinants $\langle\cdot,\cdot\rangle_{*}$ and $H^2$. The comparison of the two products reads: they coincide on the real part of the second slot and oppose on the imaginary part.

| Structure | Object | Carrier | What it is |
|---|---|---|---|
| Field | $\mathbb{C}$ | $\mathbb{C}_{\mathbb{R}}$ | the product $AC$ |
| General plain sesqualgebra (GPS) | $(\mathbb{C},\star)$ | $\mathbb{C}_{\mathbb{R}}$ | the product $A\bar C$ |
| Two products | — | $\mathbb{C}_{\mathbb{R}}$ | $AC$, $A\bar C$ |
| Two forms | $B, H$ | $\mathbb{C}_{\mathbb{R}}$ | $AC$, $A\bar C$ as forms, Gram $[1]$ |
| Two algebraic norms | $\langle A\rangle, \langle A\rangle_{*}$ | $\mathbb{C}$ | $A^2$ anisotropic; $\lvert A\rvert^2$ definite |
| Ternary product | $\{A,B,C\}$ | $\mathbb{C}$ | $A\bar BC$, a $J^{*}$-algebra |
| Subspaces | $\mathbb{R}_{\mathbb{C}}, i\mathbb{R}_{\mathbb{C}}$ | $\mathbb{C}_{\mathbb{R}}$ | fixed and anti-fixed lines |
| Matrix models | $\mathsf M_2, \mathsf M_4$ | $M_2(\mathbb{R}), M_4(\mathbb{R})$ | determinants $\langle\cdot,\cdot\rangle_{*}$, $H^2$ |
| Realification | $J$ | $\mathbb{C}_{\mathbb{R}}$ | multiplication by $i$, $J^2 = -\operatorname{id}$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A = a + ia'$ | element of $\mathbb{C}$ |
| $\mathbb{C}_{\mathbb{R}}$ | $\mathbb{C}$ read as a real vector space, basis $1, i$ |
| $J(A) = iA$ | the real-linear complex structure, $J^2 = -\operatorname{id}$ |
| $AC$, $A\bar C$ | the two products |
| $\langle A,C\rangle = AC$, $\langle A,C\rangle_{*} = A\bar C$ | the two forms |
| $\langle A\rangle = A^2$, $\langle A\rangle_{*} = \lvert A\rvert^2$ | the two algebraic norms |
| $A\star C = A\bar C$ | the sesquilinear product of the GPS |
| $\{A,B,C\} = A\bar BC$ | the ternary product, $J^{*}$-algebra |
| $\mathbb{R}_{\mathbb{C}}$, $i\mathbb{R}_{\mathbb{C}}$ | real and imaginary axes |
| $\mathsf M_2(A) = aI + a'J$ | the Cayley matrix model |

## Further Reading

- *The Complex Numbers ($\mathbb{C}$)* (`articles_maths/the-complex-numbers.md`), for the field itself: construction, algebraic closedness, conjugation, norm and trace, and the roots of unity.
- *The Complexoid as a Vector Space over $\mathbb{R}$* (`articles_maths/the-complexoid-as-a-vector-space-over-r.md`), *Complexoid Subspaces* (`articles_maths/complexoid-subspaces.md`) and *Decompositions and Comparison of the Remarkable Subspaces of the Complexoid* (`articles_maths/decompositions-and-comparison-of-the-remarkable-subspaces-of-the-complexoid.md`), for the real and complex readings of the carrier, the involution and its two blocks.
- *The Two Products of the Complexoid Space* (`articles_maths/the-two-products-of-the-complexoid-space.md`), *Relations and Comparison Between the Two Products* (`articles_maths/relations-and-comparison-between-the-two-products.md`) and *The Two Forms and the Two Algebraic Norms of the Complexoid Space* (`articles_maths/the-two-forms-and-the-two-algebraic-norms-of-the-complexoid-space.md`), for the two products, their comparison, and their forms and algebraic norms.
- *The Sesquilinear Product of the Complexoid Space* (`articles_maths/the-sesquilinear-product-of-the-complexoid-space.md`) and *The Hermitian Form and the Positivity of the Complexoid Algebra* (`articles_maths/the-hermitian-form-and-the-positivity-of-the-complexoid-algebra.md`), for the GPS, the ternarisation and the positivity of the form.
- *The Ternary Product of the Complexoid Space* (`articles_maths/the-ternary-product-of-the-complexoid-space.md`), for the ternary operation in full.
- *The Matrix Element Representations of the Complexoid* (`articles_maths/the-matrix-element-representations-of-the-complexoid.md`), for the two matrix models and their commutants.
- *Jordan Triples with an Involution*, *Algebraic J\*-Algebras*, *Hermitian Forms over Algebras and Norms* and *The Norm Defined by a Form*, for the general theory of a sesqualgebra, of a ternary product and of an algebraic norm.
