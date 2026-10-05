# __The Six Subspaces and the Products__

**This article is very temporary and is to be rewritten later.**

## Introduction

The biquaternion algebra is associative and not commutative, and the product of two elements taken from two of the six distinguished subspaces need not stay in a subspace of the list: the product of two pure vectors has a scalar part, and the product of two Hermitian elements has an imaginary vector part. This article records, for each ordered pair of the six, the real span of all products of an element of the first by an element of the second.

The six subspaces are those of *Introduction to the Six Subspaces*, and the four coordinate blocks $A_1 = \mathbb{R}e_0$, $A_2 = \mathbb{R}(ie_0)$, $B_1 = \operatorname{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$, $B_2 = \operatorname{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$ are those of *Comparison of the Six Subspaces*. An entry of a table below is written $\mathbb{B}$ when the product spans the whole algebra.

| $\cdot$ | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
|---|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{B}$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{B}$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{B}$ | $\mathbb{B}$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{B}$ | $\mathbb{B}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{H}_{\mathbb{B}}$ | $\mathbb{B}$ | $\mathbb{B}$ |
| $\mathbb{M}_+$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{R}e_0 \oplus \mathrm{Vect}(\mathbb{B})$ | $\mathbb{R}(ie_0) \oplus \mathrm{Vect}(\mathbb{B})$ |
| $\mathbb{M}_-$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{R}(ie_0) \oplus \mathrm{Vect}(\mathbb{B})$ | $\mathbb{R}e_0 \oplus \mathrm{Vect}(\mathbb{B})$ |

Each entry is exact: it is the real span of the products, not merely a subspace containing them. The algebra is filled by the product in almost every case; the seven exceptional cells are the four involving the centre and the vector subspace, the four involving the two quaternion subspaces, and the four involving the two Hermitian subspaces.

The table is symmetric although the product is not. The reason is that quaternion conjugation is an anti-automorphism, $(\tilde{P}\tilde{Q})^{\natural} = \tilde{Q}^{\natural}\tilde{P}^{\natural}$, and it maps each of the six subspaces to itself; it therefore carries the span of $U \cdot V$ onto the span of $V \cdot U$, and each entry of the table is invariant under it, so the two spans coincide.

The product splits into its two halves, the symmetrized product $\tilde{P} \circ \tilde{Q} = \tfrac{1}{2}(\tilde{P}\tilde{Q} + \tilde{Q}\tilde{P})$ and the commutator $[\tilde{P},\tilde{Q}] = \tilde{P}\tilde{Q} - \tilde{Q}\tilde{P}$. The restriction of each half to the six is a separate theme, treated in *The Six Subspaces and the Jordan Algebra* and in *The Six Subspaces and the Lie Algebra*; only the full product is tabulated here.

Throughout, an element of the vector subspace is written $\mathbf{P}$ and its complex dot and cross products are $(\mathbf{P},\mathbf{Q})$ and $\mathbf{P} \times \mathbf{Q}$, so that $\mathbf{P}\mathbf{Q} = -(\mathbf{P},\mathbf{Q})e_0 + \mathbf{P} \times \mathbf{Q}$.

## The Centre Subspace

A central element is $Ae_0$ with $A \in \mathbb{C}$, and multiplication by it is a scaling of the complex coefficients: $Ae_0\tilde{Q} = \tilde{Q}Ae_0 = A\tilde{Q}$. The product of two central elements is central, and the centre is a subalgebra:

$$
Ae_0 \cdot Be_0 = ABe_0 , \qquad \mathbb{C}_{\mathbb{B}} \cdot \mathbb{C}_{\mathbb{B}} = \mathbb{C}_{\mathbb{B}} .
$$

Multiplication by a central element stabilizes a subspace $U$ exactly when $U$ is stable under multiplication by the central imaginary unit, that is, when $iU = U$. This is so for the centre and the vector subspace, and for neither of the other four: if $U$ is one of $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ or $\mathbb{M}_-$, then multiplication by $ie_0$ carries $U$ onto the other member of its decomposition, by *Comparison of the Six Subspaces*, §*The Complex Structure and the Six Subspaces*. Hence

$$
\mathbb{C}_{\mathbb{B}} \cdot \mathbb{C}_{\mathbb{B}} = \mathbb{C}_{\mathbb{B}} , \qquad \mathbb{C}_{\mathbb{B}} \cdot \mathrm{Vect}(\mathbb{B}) = \mathrm{Vect}(\mathbb{B}) , \qquad \mathbb{C}_{\mathbb{B}} \cdot U = \mathbb{B} \quad \text{for the other four } U .
$$

The last case is not an accident of dimension: $e_0$ and $ie_0$ together span the centre, and $(ie_0)e_1 = ie_1$ is an anti-quaternion element, so a product of a quaternion-subspace element by a central one already leaves $\mathbb{H}_{\mathbb{B}}$.

## The Vector Subspace

For pure vectors the product is the scalar–vector formula without the mixed terms,

$$
\mathbf{P}\mathbf{Q} = -(\mathbf{P},\mathbf{Q})e_0 + \mathbf{P} \times \mathbf{Q} ,
$$

so the scalar part of $\mathbf{P}\mathbf{Q}$ is the negated complex dot product and the vector part is the complex cross product. The product of two pure vectors therefore lies in $\mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$, and it attains the whole of it:

$$
\mathrm{Vect}(\mathbb{B}) \cdot \mathrm{Vect}(\mathbb{B}) = \mathbb{B} .
$$

That the span is all of $\mathbb{B}$ is read from four products: $e_1e_1 = -e_0$ gives the block $A_1$, $e_1(ie_1) = -ie_0$ gives $A_2$, $e_1e_2 = e_3$ gives $B_1$ and $e_1(ie_2) = ie_3$ gives $B_2$. The vector subspace is the only one of the six whose self-product spans the algebra while its elements are the pure vectors of the scalar–vector decomposition.

With the centre the product stays in the vector subspace, since $Ae_0 \cdot \mathbf{P} = A\mathbf{P}$ is again a pure vector; with each of the other four the product spans the algebra.

## The Quaternion Subspace

The quaternion subspace is a subalgebra, being the image of the real quaternion algebra under $h \mapsto he_0$:

$$
\mathbb{H}_{\mathbb{B}} \cdot \mathbb{H}_{\mathbb{B}} = \mathbb{H}_{\mathbb{B}} .
$$

It is the only non-commutative one of the six, and the only one of the four four-dimensional subspaces closed under the product. Its product with the anti-quaternion subspace stays in the anti-quaternion subspace,

$$
\mathbb{H}_{\mathbb{B}} \cdot i\mathbb{H}_{\mathbb{B}} = i\mathbb{H}_{\mathbb{B}} \cdot \mathbb{H}_{\mathbb{B}} = i\mathbb{H}_{\mathbb{B}} ,
$$

which is the statement that $i\mathbb{H}_{\mathbb{B}}$ is generated by $ie_0$ as a module over $\mathbb{H}_{\mathbb{B}}$ on either side. With the centre, the vector subspace and the two Hermitian subspaces the product spans the algebra. The case of the vector subspace is instructive: $e_1 \in \mathbb{H}_{\mathbb{B}}$, $ie_1 \in \mathrm{Vect}(\mathbb{B})$ and $e_1(ie_1) = -ie_0$ is central, so $\mathbb{H}_{\mathbb{B}} \cdot \mathrm{Vect}(\mathbb{B})$ already meets two blocks outside the two factors.

## The Anti-Quaternion Subspace

The anti-quaternion subspace is not a subalgebra, and the square of its generator returns to the quaternion subspace:

$$
(ie_0)^2 = -e_0 , \qquad i\mathbb{H}_{\mathbb{B}} \cdot i\mathbb{H}_{\mathbb{B}} = \mathbb{H}_{\mathbb{B}} .
$$

Together with the previous section this gives the gradation of the quaternion decomposition:

$$
\mathbb{H}_{\mathbb{B}} \cdot \mathbb{H}_{\mathbb{B}} \subseteq \mathbb{H}_{\mathbb{B}} , \qquad \mathbb{H}_{\mathbb{B}} \cdot i\mathbb{H}_{\mathbb{B}} \subseteq i\mathbb{H}_{\mathbb{B}} , \qquad i\mathbb{H}_{\mathbb{B}} \cdot \mathbb{H}_{\mathbb{B}} \subseteq i\mathbb{H}_{\mathbb{B}} , \qquad i\mathbb{H}_{\mathbb{B}} \cdot i\mathbb{H}_{\mathbb{B}} \subseteq \mathbb{H}_{\mathbb{B}} ,
$$

and all four containments are equalities of spans. The quaternion and anti-quaternion subspaces are the even and the odd part of a $\mathbb{Z}/2$-graded algebra. The anti-quaternion subspace is a two-sided module over the quaternion subspace, which is the module structure that *Modules over the Biquaternion Algebra* develops. With the centre, the vector subspace and the two Hermitian subspaces the product spans the algebra.

## The Hermitian Subspace

Write a Hermitian element as $a_0e_0 + i\mathbf{p}$ with $a_0 \in \mathbb{R}$ and $\mathbf{p}$ a real vector, and let $b_0e_0 + i\mathbf{r}$ be a second. Multiplying, the scalar part is $a_0b_0 + (\mathbf{p},\mathbf{r})$, which is real, and the vector part is $-\mathbf{p} \times \mathbf{r} + i(a_0\mathbf{r} + b_0\mathbf{p})$, whose two terms are a real and an imaginary vector. Hence

$$
\mathbb{M}_+ \cdot \mathbb{M}_+ \subseteq \mathbb{R}e_0 \oplus \mathrm{Vect}(\mathbb{B}) , \qquad \mathbb{M}_+ \cdot \mathbb{M}_+ = \mathbb{R}e_0 \oplus \mathrm{Vect}(\mathbb{B}) .
$$

The product of two Hermitian elements therefore has a **real** scalar part, which is why its span misses the block $A_2$ and is of dimension seven rather than eight; the vector part, by contrast, is unrestricted, since $-\mathbf{p} \times \mathbf{r}$ ranges over the whole of $B_1$ and $i(a_0\mathbf{r} + b_0\mathbf{p})$ over the whole of $B_2$. A witness that the product leaves $\mathbb{M}_+$ itself is

$$
(e_0 + ie_1)(e_0 + ie_2) = e_0 + ie_1 + ie_2 - e_3 ,
$$

which lies in $\mathbb{R}e_0 \oplus \mathrm{Vect}(\mathbb{B})$ and in none of the six subspaces. With an anti-Hermitian element the scalar part becomes purely imaginary instead: writing that element as $ib'_0e_0 + \mathbf{q}$,

$$
\mathbb{M}_+ \cdot \mathbb{M}_- \subseteq \mathbb{R}(ie_0) \oplus \mathrm{Vect}(\mathbb{B}) , \qquad \mathbb{M}_+ \cdot \mathbb{M}_- = \mathbb{R}(ie_0) \oplus \mathrm{Vect}(\mathbb{B}) ,
$$

so the product of a Hermitian by an anti-Hermitian element has a purely imaginary scalar part. With the centre, the vector subspace and the two quaternion subspaces the product spans the algebra.

## The Anti-Hermitian Subspace

Write an anti-Hermitian element as $ib'_0e_0 + \mathbf{q}$ with $b'_0 \in \mathbb{R}$ and $\mathbf{q}$ a real vector. The product of two of them has the real scalar part $-b'_0c'_0 - (\mathbf{q},\mathbf{r})$ and the vector part $\mathbf{q} \times \mathbf{r} + i(b'_0\mathbf{r} + c'_0\mathbf{q})$, whence

$$
\mathbb{M}_- \cdot \mathbb{M}_- = \mathbb{R}e_0 \oplus \mathrm{Vect}(\mathbb{B}) , \qquad \mathbb{M}_- \cdot \mathbb{M}_+ = \mathbb{R}(ie_0) \oplus \mathrm{Vect}(\mathbb{B}) .
$$

The two sectors behave alike in this respect: two elements from the same sector, both Hermitian or both anti-Hermitian, multiply to a product with real scalar part, and two from opposite sectors to one with purely imaginary scalar part. The anti-Hermitian subspace is not a subalgebra for the same reason as the Hermitian one, and a witness is $e_1e_2 = e_3$: both factors are anti-Hermitian and the product is a pure vector with no imaginary scalar part, so it is not anti-Hermitian. With the centre, the vector subspace and the two quaternion subspaces the product spans the algebra.

## Summary

The product of two elements of the six distinguished subspaces is tabulated above by the real span of all products, and the algebra is filled by the product in almost every case. The centre is a subalgebra and multiplies another subspace into itself exactly for the centre and the vector subspace, and into the whole algebra for the other four, because multiplication by the central imaginary unit exchanges the two members of each of the two remaining decompositions. The vector subspace is closed under the product only against the centre: with itself it spans the whole algebra, its product with itself being the negated complex dot product in the scalar part and the complex cross product in the vector part. The quaternion subspace is a subalgebra, and it is the only non-commutative one of the six; with the anti-quaternion subspace the product stays in the anti-quaternion subspace, and the quaternion decomposition is a $\mathbb{Z}/2$-gradation whose even part is $\mathbb{H}_{\mathbb{B}}$ and whose odd part is $i\mathbb{H}_{\mathbb{B}}$. The Hermitian and the anti-Hermitian subspaces are not subalgebras, and the product of two elements from the same sector has a real scalar part while the product of two from opposite sectors has a purely imaginary one; in each case the span is the whole vector subspace together with one scalar line, of dimension seven. The product has two halves, the symmetrized product and the commutator, whose restrictions to the six are *The Six Subspaces and the Jordan Algebra* and *The Six Subspaces and the Lie Algebra*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B})$ | the centre and the vector subspace |
| $\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+, \mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |
| $A_1, A_2, B_1, B_2$ | the four coordinate blocks |
| $(\mathbf{P},\mathbf{Q})$, $\mathbf{P} \times \mathbf{Q}$ | the complex dot and cross products |
| $\tilde{P} \circ \tilde{Q}$ | the symmetrized product $\tfrac{1}{2}(\tilde{P}\tilde{Q} + \tilde{Q}\tilde{P})$ |
| $[\tilde{P},\tilde{Q}]$ | the commutator $\tilde{P}\tilde{Q} - \tilde{Q}\tilde{P}$ |

## Further Reading

- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six subspaces themselves, one to a section
- *Comparison of the Six Subspaces* (`articles_maths/comparison-of-the-six-subspaces.md`), for the blocks, the intersections, the sums and the action of the central imaginary unit
- *The Four Biquaternion Complex Products* (`articles_maths/the-four-biquaternion-complex-products.md`), for the product and the scalar–vector formula
- *Decomposition of the Multiplication* (`articles_maths/decomposition-of-the-multiplication.md`), for the two halves
- *Biquaternion Jordan Algebra* (`articles_maths/biquaternion-jordan-algebra.md`), for the symmetrized product and the Jordan structure of the whole algebra
- *Biquaternion Lie Algebra* (`articles_maths/biquaternion-lie-algebra.md`), for the commutator and the Lie structure of the whole algebra
