# __Zero Divisors of the Symmetric Plain Sesqualgebra__

## Introduction

The symmetric plain sesqualgebra is the operation $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ on the biquaternion space (*Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*). This article studies its **zero divisors**: the nonzero elements that annihilate a nonzero element.

A zero divisor names a product, and the definition is relative. The definitions are stated once for a general product in *Definitions for the Study of the 12 Algebraic Structures*; here they are read on the block. The block is a **rank-one pairing**: the value of the product is the coefficient of the form $H$ on the two arguments, and the form is non-degenerate. Two consequences follow and they are the whole article. The **criterion** is a single equation, $\tilde P\star\tilde R = 0$ exactly when $H(\tilde P,\tilde R) = 0$. The **set** is therefore the complement of the origin: every nonzero element annihilates a nonzero element, on each side, and the annihilator of an element is a hyperplane. The **two families** of the plain product, the pure and the non-pure, do not exist here, because there is no criterion of the ring-theoretic form to split; the block has one family alone.

**Placement.** The article is the third entry of the *Common Theory* section of the block, after *Norm and Invertibility in the Symmetric Plain Sesqualgebra* and before the square roots of the central values. It uses the product, the class and the placement of the introduction, the definiteness of the form from *Norm and Invertibility in the Symmetric Plain Sesqualgebra*, and the common zero-divisor set of the four general products.

**Boundaries.** The product, its class and its placement among the twelve structures are *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*; the form $H$ and its non-degeneracy are *Norm and Invertibility in the General Plain Algebra* and *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra*. The relative definition of the zero divisor and the vocabulary of the left, the right and the two-sided are *Definitions for the Study of the 12 Algebraic Structures*; the common set of the four general products and the theorem that the four agree are *The Zero Divisors and the Twelve Structures*, and the same set read on the plain product with its two families is *Zero Divisors of the General Plain Algebra*, *Idempotents of the General Plain Algebra* and *Nilpotents of the General Plain Algebra*. Nothing topological and nothing metric appears.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2 = e_3$ and central scalar imaginary $i$. A general element is $\tilde{Q} = \sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; the natural conjugation is $\tilde{Q}^{\natural} = \sum_\mu\varepsilon_\mu Q_\mu e_\mu$ with $\varepsilon = (1,-1,-1,-1)$, the coefficientwise conjugation is $\overline{\tilde{Q}} = \sum_\mu\overline{Q_\mu}e_\mu$, and the Hermitian conjugation is $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$. The product of the block is

$$
\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0, \qquad H(\tilde P,\tilde Q) = \sum_{\mu=0}^{3}P_\mu\overline{Q_\mu},
$$

a sesquilinear form over $(\mathbb{C},\bar{\cdot}\,)$, with Gram matrix the identity on the basis and positive definite. The **orthogonal hyperplane** of a nonzero $\tilde P$ is

$$
\tilde P^{\perp} = \{\tilde X\in\mathbb{B} : H(\tilde P,\tilde X) = 0\},
$$

and it does not depend on whether $H$ is read in the first or the second argument, because $H(\tilde X,\tilde P) = \overline{H(\tilde P,\tilde X)}$.

## The Criterion

**Theorem (the criterion of the block).** For nonzero $\tilde P$ and $\tilde R$,

$$
\tilde P\star\tilde R = 0 \quad\Longleftrightarrow\quad H(\tilde P,\tilde R) = 0 .
$$

*Proof.* The product is $\tilde P\star\tilde R = H(\tilde P,\tilde R)e_0$, and $e_0\neq0$; so the product vanishes exactly when the coefficient does.

**Corollary (the annihilating partners).** For nonzero $\tilde P$, the elements $\tilde R$ with $\tilde P\star\tilde R = 0$ are exactly the nonzero elements of the hyperplane $\tilde P^{\perp}$; the elements with $\tilde R\star\tilde P = 0$ are exactly the same set, because $H(\tilde R,\tilde P) = \overline{H(\tilde P,\tilde R)}$ vanishes together with $H(\tilde P,\tilde R)$.

**Remark (the criterion is one equation, not a cone).** The criterion of the general plain bilinear product is $\tilde{Q}\tilde{Q}^{\natural} = 0$, a quadratic equation in the element alone (*Zero Divisors of the General Plain Algebra*). The criterion of the block is a bilinear equation, $H(\tilde P,\tilde R) = 0$, in the element and its partner; the two are not the same kind of statement, and the block has no equation in one element that decides its zero divisors. This is why the set below is not a cone.

## The Zero Divisor Set

**Theorem (every nonzero element is a two-sided zero divisor).** An element of $\mathbb{B}$ is a zero divisor of the block if and only if it is nonzero.

*Proof.* Let $\tilde P\neq0$. The functional $H(\tilde P,\cdot\,)$ is not identically zero, because $H$ is non-degenerate: there is a $\tilde X$ with $H(\tilde P,\tilde X)\neq0$. Hence its kernel $\tilde P^{\perp}$ is a proper subspace, of complex dimension $3$, and it contains nonzero elements; choosing such a nonzero $\tilde R$ gives $\tilde P\star\tilde R = 0$ by the criterion, so $\tilde P$ is a right zero divisor. The same argument with the first argument gives a nonzero $\tilde L$ with $\tilde L\star\tilde P = 0$, so $\tilde P$ is also a left zero divisor, hence a two-sided one. The zero element is excluded by the definition, since a zero divisor is required to be nonzero.

**Corollary (the set and its shape).** The zero-divisor set of the block is

$$
\mathcal{Z}_\star = \mathbb{B}\setminus\{0\},
$$

the complement of the origin, of complex dimension four (real dimension eight). It is not a cone, because it contains the origin's complement in every complex line through the origin but not the origin itself; it is a **punctured space**.

*Proof.* The first is the theorem. The set is the complement of a point in $\mathbb{C}^{4}$, of complex dimension four, and it is the union of the punctured complex lines through the origin; it is not a cone, because the scalar $0$ carries every element of the set out of it.

**Remark (the sharpness).** The set is as large as a zero-divisor set can be: it is the whole complement of the origin. A product with a non-degenerate coefficient form and a one-dimensional central image can have no smaller set, because the criterion $H(\tilde P,\tilde R) = 0$ has a nonzero solution $\tilde R$ for every nonzero $\tilde P$. The proof needs only the non-degeneracy of the form and the rank-one shape; no positivity is used.

## The Two Annihilators

**Definition.** For $\tilde P\in\mathbb{B}$ the **right annihilator** of $\tilde P$ in the block is $B_\star(\tilde P) = \{\tilde R : \tilde P\star\tilde R = 0\}$, the **left annihilator** is $A_\star(\tilde P) = \{\tilde R : \tilde R\star\tilde P = 0\}$, and the **two-sided annihilator** of the block is the set of the elements that annihilate every element on each side.

**Theorem (the annihilator is the orthogonal hyperplane).** For $\tilde P\neq0$,

$$
A_\star(\tilde P) = B_\star(\tilde P) = \tilde P^{\perp},
$$

a complex subspace of dimension three; for $\tilde P = 0$ both annihilators are all of $\mathbb{B}$. The two-sided annihilator of the block is $\{0\}$.

*Proof.* The first display is the criterion and the conjugacy of $H$. The dimension is that of the kernel of a nonzero functional on $\mathbb{C}^{4}$. For the two-sided annihilator, an element $\tilde A$ with $\tilde A\star\tilde R = 0$ for all $\tilde R$ satisfies $H(\tilde A,\tilde R) = 0$ for all $\tilde R$, which by non-degeneracy forces $\tilde A = 0$; the left case is identical.

**Remark (the annihilator is a hyperplane, not a line).** An element of the block annihilates a hyperplane of the space, not a subspace of the image: the annihilator is a three-dimensional hyperplane in $\mathbb{B}$ and not the central line $\mathbb{C}e_0$. The contrast with the general plain algebra is total: there the annihilator of a generic zero divisor is a line, and it collapses to nothing off the zero-divisor cone, whereas here it exists for every nonzero element and is always a hyperplane.

## The Families

The plain product splits its zero divisors into two disjoint families, the pure and the non-pure, and the split is the criterion read on the scalar coordinate: the pure family has $P_0 = 0$ and is the nonzero nilpotents, and the non-pure family has $P_0\neq0$ and is the nonzero complex multiples of the nontrivial idempotents (*Zero Divisors of the General Plain Algebra*). **The block has no such split.** Its criterion is bilinear, not quadratic, and it does not separate the elements by the scalar coordinate or by any other elementwise condition: the set is homogeneous over the whole punctured space.

| the split | general plain algebra | symmetric plain sesqualgebra |
|---|---|---|
| criterion | $Q_0^{2}+(\mathbf Q,\mathbf Q) = 0$, one element | $H(\tilde P,\tilde R) = 0$, an element and a partner |
| pure family | $P_0 = 0$, $(\mathbf P,\mathbf P) = 0$ | absent |
| non-pure family | $P_0\neq0$, complex multiples of idempotents | absent |
| the set | a complex cone of dimension $3$, the origin removed | the whole punctured space, dimension $4$ |

**Remark (the nearest substitute).** The dichotomy that survives is between the zero element, which is not a zero divisor, and every other element, which is one. The two families of the plain product are not visible to the block, and the block's own structural split is the one it shares with every rank-one pairing: nothing. The article therefore does not subdivide, and the subdivision of the parent is left to *Idempotents of the General Plain Algebra* and *Nilpotents of the General Plain Algebra*.

## The Comparison with the Four General Products

The four general products of the space, $\tilde P\tilde Q$, $\tilde P^{\natural}\tilde Q$, $\tilde P\tilde Q^{*}$ and $\tilde P^{\natural}\tilde Q^{*}$, select one common zero-divisor set, the nonzero elements of the isotropic cone $\{c(\tilde P) = \sum_\mu P_\mu^{2} = 0\}$, and the coincidence is a theorem of the space (*The Zero Divisors and the Twelve Structures*). The block is a part of one of them, the general plain sesquilinear product, and its set is strictly larger.

**Theorem (the block's set contains the common set, strictly).** Every zero divisor of the four general products is a zero divisor of the block, and there are block zero divisors that are not zero divisors of any general product.

*Proof.* The common set is the nonzero isotropic cone, a proper subset of $\mathbb{B}\setminus\{0\}$, which is the block's set; the inclusion follows. For the strictness, the element $e_0$ has $c(e_0) = 1\neq0$, so it is not a zero divisor of any of the four general products; but $e_0\star e_1 = H(e_0,e_1)e_0 = 0$, so $e_0$ is a zero divisor of the block.

**Remark (the coincidence theorem does not extend to the parts).** The four general products agree with one another, but the symmetric and antisymmetric parts of a product do not inherit the agreement: each part has its own coefficient form, and the block's form is definite while the parent's is isotropic. The transfer of a classification from the parent to the part is therefore not legitimate, and the block computes its set from its own criterion. The zero-divisor set of the block is the same as that of its sibling $\mathrm{SQA}$, because both are rank-one pairings with a non-degenerate form; the sibling is read in *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*.

## The Zero Divisors and the Remarkable Subspaces

**Proposition (the set meets every subspace in its punctured self).** For every subspace $W$ of $\mathbb{B}$, the zero divisors of the block that lie in $W$ are the nonzero elements of $W$; in particular every nonzero element of each remarkable subspace $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$ is a zero divisor of the block.

*Proof.* The zero-divisor set is the complement of the origin, so its intersection with $W$ is $W\setminus\{0\}$.

**Remark (the question is emptied).** In the plain product the question "which remarkable subspaces contain zero divisors" is answered by the vanishing of the polynomial $c$ on each, and the answer varies from subspace to subspace (*Zero Divisors of the General Plain Algebra*). In the block the answer is the same for all of them, because the condition is not a polynomial in the element but the non-vanishing of the element itself. The block therefore has no preferred subspace for its zero divisors, and its subspaces are distinguished by other invariants, the closure or non-closure under the product, the images and the annihilators of their elements.

## Summary

The zero divisors of the symmetric plain sesqualgebra obey one criterion, $\tilde P\star\tilde R = 0$ exactly when $H(\tilde P,\tilde R) = 0$, and the criterion makes the set the **complement of the origin**: every nonzero element is a two-sided zero divisor, and the zero element is the only element that is not. The annihilator of a nonzero element is the **orthogonal hyperplane** $\tilde P^{\perp}$, of complex dimension three, and it is the same on the left and on the right; the two-sided annihilator of the block is $\{0\}$. The **two families** of the plain product, the pure and the non-pure, do not exist: the block's criterion is bilinear and splits nothing, and its dichotomy is only the zero element against the rest. The block's set strictly contains the common zero-divisor set of the four general products, the nonzero isotropic cone, the element $e_0$ being a block zero divisor and not a general-product one; the coincidence theorem of the four general products does not extend to their parts. Every remarkable subspace meets the set in its punctured self, so no subspace is preferred.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ | the product of the block |
| $H(\tilde P,\tilde Q) = \sum_\mu P_\mu\overline{Q_\mu}$ | the Hermitian form defining the block, non-degenerate and definite |
| $\tilde P^{\perp} = \{\tilde X : H(\tilde P,\tilde X) = 0\}$ | the orthogonal hyperplane, of complex dimension three |
| $\tilde P\star\tilde R = 0\Leftrightarrow H(\tilde P,\tilde R) = 0$ | the criterion of the block |
| $A_\star(\tilde P) = B_\star(\tilde P) = \tilde P^{\perp}$ | the left and the right annihilators, equal |
| $\mathcal{Z}_\star = \mathbb{B}\setminus\{0\}$ | the zero-divisor set, the punctured space |
| $\{c = 0\}\setminus\{0\}$ | the common set of the four general products, strictly smaller |

## Further Reading

- *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the product, its class and its table.
- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the relative definition of the zero divisor and the left, right and two-sided vocabulary.
- *The Zero Divisors and the Twelve Structures* (`articles_maths/the-zero-divisors-and-the-twelve-structures.md`), for the common set of the four general products and the theorem that the four agree.
- *The Annihilating Elements of the Twelve Structures* (`articles_maths/the-annihilating-elements-of-the-twelve-structures.md`), for the annihilators read product by product.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the two families of the parent and their criteria.
- *Norm and Invertibility in the Symmetric Plain Sesqualgebra* (`articles_maths/norm-and-invertibility-in-the-symmetric-plain-sesqualgebra.md`), for the definiteness and the absence of an invertible element.
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the remarkable subspaces the set meets.
