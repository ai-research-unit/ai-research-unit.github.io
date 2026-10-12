# __Nilpotents of the Antisymmetric Plain Sesqualgebra__

## Introduction

A nilpotent is an element some power of which vanishes, and the power is read in a product. This article determines the nilpotents of the antisymmetric plain sesqualgebra $\mathrm{APS}$,

$$
\tilde P\diamond\tilde Q=\operatorname{Vect}\bigl(\tilde P\tilde Q^{*}\bigr)=-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}},
$$

the antisymmetric half of the general plain sesquilinear product of *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions*.

The answer has two parts. The **square-zero elements** are the elements whose plain product with their star is central, $\tilde P\tilde P^{*}\in\mathbb{C}_{\mathbb{B}}$, an honest condition that cuts a quadric in the space and that is the criterion of *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*; and the **index is two**, so there is nothing above the square-zero level. The index-two statement is the content of this article beyond the criterion: the left-nested cube $\tilde P\diamond\tilde P\diamond\tilde P$ vanishes only when the square does, so the nilpotent class of the block is the square-zero class and the notion of a longer vanishing product does not occur. The block is therefore in the position of the plain algebra, where the index is two or nothing, and not in the position of the products of the twelve where the index is unbounded (*Definitions for the Study of the 12 Algebraic Structures*, §*The Nilpotent*).

The definition of the nilpotent, of the index and of the square-zero element is *Definitions for the Study of the 12 Algebraic Structures*, §*The Nilpotent* and §*Powers, the Square and the Roots*; the notation $\tilde\Upsilon$ for a biquaternion-layer nilpotent is *Conventions in Mathematics*, §*The nilpotent convention*. The criterion for the vanishing of the diagonal and the quadric it traces are quoted from *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra* and not recomputed, and the roots of the three central values are *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Sesqualgebra*. The neighbouring classes are *Zero Divisors of the Antisymmetric Plain Sesqualgebra* and *Idempotents of the Antisymmetric Plain Sesqualgebra*; the square-zero sets of the four general products are *The Square-Zero Elements of the Twelve Structures*; and the model of the index-two theorem is *The Antisymmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0=1,e_1,e_2,e_3$ with $e_1e_2=e_3$, central scalar imaginary $i$ and coefficients in $\mathbb{C}$; an element is $\tilde Q=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^{3}Q_ke_k$, and the plain product is $\tilde P\tilde Q$ with star $\tilde Q^{*}=\bar{\tilde Q}^{\natural}$. The projection $\operatorname{Vect}$ removes the scalar part, its kernel is the centre $\mathbb{C}_{\mathbb{B}}$, its image is the vector subspace $\operatorname{Vect}(\mathbb{B})$, and $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ are the real quaternion, anti-quaternion, Hermitian and anti-Hermitian subspaces. Throughout this article **nilpotent**, **index** and **power** are read in $\diamond$, and $c(\tilde Q)=\sum_\mu Q_\mu^{2}$ is the central square of the plain product.

## The Definition

**Definition (nilpotent, index, square-zero element).** Let $\star$ be a product on $\mathbb{B}$. An element $\tilde\Upsilon$ is **nilpotent of $\star$** when some power of it vanishes,

$$
\tilde\Upsilon^{\star k}=0\quad\text{for some }k\geq 1,
$$

the power being the left-nested reading $\tilde\Upsilon^{\star k}=(\cdots((\tilde\Upsilon\star\tilde\Upsilon)\star\tilde\Upsilon)\cdots\star\tilde\Upsilon)$ when $\star$ is not associative; the least such $k$ is the **index of nilpotency**, and an element of index two, $\tilde\Upsilon\star\tilde\Upsilon=0$ with $\tilde\Upsilon\neq0$, is a **square-zero element**. The origin is the trivial nilpotent, and the article is concerned with the others.

The block is not associative, and neither is the general plain sesquilinear product, so the bracketing is specified and the left-nested reading is taken. The square is bracketing-free, and with it the square-zero element: the equation $\tilde\Upsilon\diamond\tilde\Upsilon=0$ involves one product and no choice of bracketing, and it is the same for the right-nested reading. The higher powers are not bracketing-free, and the index-two theorem below says that for the block the choice does not matter: no element has a vanishing higher power without a vanishing square.

## The Square-Zero Elements

### The Criterion

**Theorem (the square-zero criterion; quoted).** A nonzero element $\tilde P$ of the block is square-zero, $\tilde P\diamond\tilde P=0$, if and only if

$$
\tilde P\tilde P^{*}\in\mathbb{C}_{\mathbb{B}}
\iff
\operatorname{Vect}\bigl(\tilde P\tilde P^{*}\bigr)=0 ,
$$

that is, if and only if the element is $0$ or a complex multiple $\rho\tilde u$ of a real unit quaternion $\tilde u$, $\rho\in\mathbb{C}^{*}$, $\tilde u\tilde u^{*}=e_0$. The set is the complex cone on the real unit sphere of the quaternion subspace, of real dimension five, and it contains the centre $\mathbb{C}_{\mathbb{B}}$, the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$.

The criterion, its parametrisation and its dimension are the theorem of *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*; they are quoted here because the diagonal of the block is the object of that article.

### The Shape of the Set

The square-zero set is the cone over the real unit sphere, and it is a **complex cone**: if $\tilde P$ is square-zero and $\rho\in\mathbb{C}$ then $\rho\tilde P$ is square-zero, because the diagonal of $\rho\tilde P$ is $\operatorname{Vect}(\rho\tilde P(\rho\tilde P)^{*})=|\rho|^{2}\operatorname{Vect}(\tilde P\tilde P^{*})=|\rho|^{2}\,\tilde P\diamond\tilde P=0$. Scaling by a complex number therefore moves a square-zero element along the complex line through it and inside the set, and the set is a union of complex lines except at the origin. It is a proper subset of the zero-divisor set, which is the whole space without the origin, and the contrast is the content of the next section.

## The Index Is Two

**Theorem (index two).** If $\tilde P\diamond\tilde P\diamond\tilde P=0$ for the left-nested cube, then $\tilde P\diamond\tilde P=0$. The nilpotents of the block are therefore exactly the square-zero elements, and there is no element of index greater than two.

*Proof.* Work in the $2\times2$ realization of *The Antisymmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, in which the block is the traceless part of the conjugate-transposed product,

$$
\mathsf{M}_2(\tilde P\diamond\tilde Q)=M-\tfrac12\operatorname{Tr}(M)\,I ,
\qquad
M=\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}.
$$

Write $M=\mathsf{M}_2(\tilde P)$, $A=MM^{\dagger}$, a Hermitian positive semidefinite matrix, $t=\operatorname{Tr}A$, and $N=A-\tfrac12t\,I$, the traceless part of $A$, which is $\mathsf{M}_2(\tilde P\diamond\tilde P)$. The left-nested cube is then the traceless part of $NM^{\dagger}$, and it vanishes exactly when $NM^{\dagger}$ is a scalar matrix, $NM^{\dagger}=\mu I$.

If $M$ is singular and nonzero, then $A$ has a single nonzero eigenvalue $t>0$, so $N$ has the eigenvalues $\pm\tfrac12t$ and is invertible and nonzero; but then $\operatorname{rank}(NM^{\dagger})=\operatorname{rank}(M^{\dagger})=\operatorname{rank}M=1$, while a scalar matrix of rank one is the zero matrix, forcing $M^{\dagger}=0$, a contradiction. So a singular $M$ with $NM^{\dagger}$ scalar has $N=0$, and the theorem holds in that case.

If $M$ is invertible, then $N\neq0$ would give $N=\mu(M^{\dagger})^{-1}$ and, $N$ being Hermitian, $\mu(M^{\dagger})^{-1}=\bar\mu M^{-1}$, so $M=\nu M^{\dagger}$ with $|\nu|=1$. Writing $\nu=e^{i\theta}$ and $H=e^{-i\theta/2}M$, the matrix $H$ is Hermitian, $A=H^{2}$, $t=\operatorname{Tr}(H^{2})$ and $N=H^{2}-\tfrac12\operatorname{Tr}(H^{2})I$; the scalar condition becomes $H^{3}-\tfrac12\operatorname{Tr}(H^{2})H=\gamma I$, and the eigenvalues $h_1,h_2$ of $H$ satisfy

$$
h_1^{3}-h_2^{3}-\tfrac12\bigl(h_1^{2}+h_2^{2}\bigr)(h_1-h_2)
=\tfrac12(h_1-h_2)(h_1+h_2)^{2}=0 ,
$$

so $h_1=h_2$ or $h_1+h_2=0$. In the first case $H$ is scalar, hence $A=H^{2}$ is scalar and $N=0$; in the second $H$ is traceless, hence $H^{2}=\tfrac12\operatorname{Tr}(H^{2})I$ and again $N=0$. Both cases contradict $N\neq0$, so $N=0$ and $\tilde P\diamond\tilde P=0$.

The same argument applies to the other bracketing of the cube. The square is bracketing-free, and a vanishing left-nested cube forces a vanishing square; a vanishing right-nested cube is the mirror statement, obtained by reading the model with the reversed product. So the index of a nilpotent of the block, read with the left-nested power of the definition, is two, and the cube certifies it in either bracketing.

## The Nilpotents and the Other Classes

### The Nilpotents and the Zero Divisors

Every nilpotent is a zero divisor, and in the block the implication carries no information.

**Proposition.** Every nonzero square-zero element of the block is a two-sided zero divisor.

*Proof.* If $\tilde\Upsilon\diamond\tilde\Upsilon=0$ with $\tilde\Upsilon\neq0$, the element $\tilde\Upsilon$ is its own annihilating partner, on the left and on the right by the conjugate-alternation, so it is a two-sided zero divisor by the definition of *Zero Divisors of the Antisymmetric Plain Sesqualgebra*.

The converse fails, and the failure is extreme: the zero-divisor set of the block is the whole space with the origin removed, while the square-zero set is the five-dimensional cone. **The block is the first structure of the twelve in which the nilpotents are a thin subset of the zero divisors rather than a generating family**: in the plain algebra every zero divisor is a nilpotent or a complex multiple of an idempotent, and in the block the idempotents are gone and the nilpotents do not cover.

### The Nilpotents and the Idempotents

The two classes are disjoint in the block, as they are in every product, and the block is the degenerate case in which one of the two is trivial.

**Proposition.** No nilpotent of the block is an idempotent, and the only idempotent is the origin.

*Proof.* A nonzero element cannot satisfy $\tilde\Pi^{2}=\tilde\Pi$ and $\tilde\Pi^{2}=0$ at once, and the only idempotent of the block is the origin (*Idempotents of the Antisymmetric Plain Sesqualgebra*).

### The Nilpotents and the Conjugations

**Proposition.** The star and the natural conjugation both preserve the square-zero set:
$$
(\tilde\Upsilon^{*})\diamond(\tilde\Upsilon^{*})=0,
\qquad
(\tilde\Upsilon^{\natural})\diamond(\tilde\Upsilon^{\natural})=0
$$
for every square-zero $\tilde\Upsilon$.

*Proof.* The criterion $\tilde\Upsilon\tilde\Upsilon^{*}\in\mathbb{C}_{\mathbb{B}}$ is carried to its star and to its natural conjugate by the identities $(\tilde\Upsilon\tilde\Upsilon^{*})^{*}=\tilde\Upsilon\tilde\Upsilon^{*}$ and, for a central element, $\lambda^{\natural}=\lambda$; and the natural conjugation of a central element is central. So each of the two images satisfies the criterion.

The star therefore pairs the nilpotents two by two through the involution $\tilde\Upsilon\mapsto\tilde\Upsilon^{*}$, and fixes those with $\tilde\Upsilon^{*}=\tilde\Upsilon$, the Hermitian nilpotents, which for the block are the real scalars and the purely imaginary vectors, $\mathbb{R}e_0\cup i\mathbb{R}^{3}$. The natural conjugation stabilises the real quaternion subspace, and it fixes the centre. This is the same bipartite structure that the standard pair $\tilde\Upsilon_1,\tilde\Upsilon_2$ carries in the plain algebra (*Idempotents of the General Plain Algebra*), here written on the cone.

### The Nilpotents and the Remarkable Subspaces

The square-zero set contains three subspaces entire: the centre $\mathbb{C}_{\mathbb{B}}$, the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$. It does not contain the Hermitian subspace $\mathbb{M}_+$ or the anti-Hermitian subspace $\mathbb{M}_-$, and the intersection is computed by the criterion: a Hermitian element is $a e_0+i\mathbf u$ with $a\in\mathbb{R}$ and $\mathbf u\in\mathbb{R}^{3}$, its diagonal is $2ia\mathbf u$, so it is square-zero exactly when $a=0$ or $\mathbf u=0$, and the intersection is the union of the real scalars and the purely imaginary vectors; the witness $e_0+ie_1$ shows that a Hermitian element with both a scalar and a vector part is not square-zero. The reading of the classes on the remarkable subspaces, with the dimensions of each intersection, is *Remarkable Subspaces under the Antisymmetric Plain Sesqualgebra of Biquaternions*.

## Summary

The nilpotents of the block are exactly its square-zero elements, and they are selected by the criterion $\tilde P\tilde P^{*}\in\mathbb{C}_{\mathbb{B}}$, equivalently $\operatorname{Vect}(\tilde P\tilde P^{*})=0$: the nonzero elements are the complex multiples of the real unit quaternions, the complex cone on the real unit sphere of the quaternion subspace, of real dimension five, containing the centre, the real quaternion subspace and the anti-quaternion subspace. The criterion, its parametrisation and the quadric are *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*.

The **index is two**: the left-nested cube vanishes only when the square does, by the $2\times2$ model of the theorem, in which the block is the traceless part of $MM^{\dagger}$ and the cube is the traceless part of $NM^{\dagger}$ with $N$ the traceless part of $A=MM^{\dagger}$, the equation being $NM^{\dagger}=\mu I$; the singularity of $M$ and, in the invertible case, the comparison of the two eigenvalues of the Hermitian matrix $H=\nu^{-1/2}M$ both force $N=0$. There is therefore no nilpotent of index greater than two and the notion of a longer vanishing product does not occur.

Every nilpotent is a zero divisor, here trivially, since a square-zero element annihilates itself; but the zero divisors are the whole space without the origin and the nilpotents are a thin cone inside them, which is the sharpest difference from the plain algebra, where the zero divisors are generated by the nilpotents and the idempotents. The block has one idempotent, the origin, so the two classes are disjoint in the void; the star preserves the square-zero set and pairs its elements through the involution $\tilde\Upsilon\mapsto\tilde\Upsilon^{*}$, and the natural conjugation preserves it as well, stabilising the real quaternion subspace and fixing the centre.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\diamond$ | the product of the block, $\tilde P\diamond\tilde Q=\operatorname{Vect}(\tilde P\tilde Q^{*})$ |
| $\tilde\Upsilon$ | a nilpotent of the biquaternion layer |
| $\tilde P\diamond\tilde P=0$ | the square-zero condition, equivalent to $\tilde P\tilde P^{*}\in\mathbb{C}_{\mathbb{B}}$ |
| $\rho\tilde u$, $\rho\in\mathbb{C}^{*}$, $\tilde u\tilde u^{*}=e_0$ | the parametrisation of the nonzero square-zero elements |
| $c(\tilde Q)=\sum_\mu Q_\mu^{2}$ | the central square of the plain product, whose vanishing cuts the plain cone |
| index two | the statement that a vanishing cube forces a vanishing square |
| $A=MM^{\dagger}$, $N=A-\tfrac12\operatorname{Tr}(A)I$ | the Hermitian square and its traceless part in the $2\times2$ model |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*The Nilpotent* and §*Powers, the Square and the Roots*, for the nilpotent, the index and the square-zero element.
- *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-vector-part-of-the-square-and-the-jacobi-failure-of-the-antisymmetric-plain-sesqualgebra.md`), for the criterion for the vanishing of the diagonal and the quadric it traces.
- *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Sesqualgebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-antisymmetric-plain-sesqualgebra.md`), for the roots of $0$ as the nonzero nilpotents.
- *Zero Divisors of the Antisymmetric Plain Sesqualgebra* (`articles_maths/zero-divisors-of-the-antisymmetric-plain-sesqualgebra.md`), for the full zero-divisor set and the annihilators.
- *Idempotents of the Antisymmetric Plain Sesqualgebra* (`articles_maths/idempotents-of-the-antisymmetric-plain-sesqualgebra.md`), for the unique idempotent.
- *The Antisymmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-antisymmetric-plain-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the model of the index-two theorem.
