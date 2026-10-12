# __Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Sesqualgebra__

## Introduction

This article solves the three central root equations of the antisymmetric plain sesqualgebra $\mathrm{APS}$,

$$
\tilde\Xi\diamond\tilde\Xi=-e_0,\qquad
\tilde\Xi\diamond\tilde\Xi=0,\qquad
\tilde\Xi\diamond\tilde\Xi=+e_0,
$$

for the product $\tilde\Xi\diamond\tilde Q=\operatorname{Vect}(\tilde\Xi\tilde Q^{*})$ of *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions*.

The answer is a **parity**, and it removes two thirds of the question. Every value of the block is a pure vector, so its scalar part vanishes; the values $-e_0$ and $+e_0$ are central with scalar part $-1$ and $+1$, so the two equations are contradictory for **every** element and the block has **no root of $-1$ and no root of $+1$**. The remaining equation, the root of $0$, asks for the elements of vanishing square: these are the nonzero square-zero elements, and they form a proper quadric in the block, the complex cone on the real unit sphere of the quaternion subspace. The definition of the root, of the index and of the square-zero element is *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots* and §*The Nilpotent*; throughout this article the square is the square of $\diamond$ and, unqualified, **root** means a root in $\diamond$.

The root of $0$ is one half of the nilpotent theory of the block, and it is developed as such in *Nilpotents of the Antisymmetric Plain Sesqualgebra*; the criterion for the vanishing of the diagonal and the quadric it traces are *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*, and they are quoted here rather than recomputed. The three central values in the four general products are *Square Roots of Minus One, Zero and Plus One*, and the general classification of the square roots of an arbitrary element is *Square Roots of a General Element in the Antisymmetric Plain Sesqualgebra*; the present article is the central specialisation of that classification. The roots of $-1$ and $+1$ in the plain algebra, and the idempotent that the root of $+1$ halves, are *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* and *Idempotents of the General Plain Algebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$, central scalar imaginary $i$ and coefficients in $\mathbb{C}$; an element is $\tilde Q=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^{3}Q_ke_k$. The projection $\operatorname{Vect}$ removes the scalar part and has kernel the centre $\mathbb{C}_{\mathbb{B}}$, and its image is the vector subspace $\operatorname{Vect}(\mathbb{B})$; the conjugations are ${}^{\natural}$, the coefficientwise $\bar{\cdot}$ and the star ${}^{*}$, and the parent sesquilinear product is $\tilde\Xi\tilde Q^{*}$. The element $\tilde\Upsilon$ denotes a nilpotent of the biquaternion layer, and the square-zero element is the case of index two (*Conventions in Mathematics*, §*The nilpotent convention*).

## The Equation and the Definition

A root of a central value belongs to a product, and the definition is stated for a general product in *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots*.

**Definition (root of a central value).** Let $\star$ be a product on $\mathbb{B}$ and let $\lambda\in\mathbb{C}$. A **root of $\lambda$ in $\star$** is a nonzero element $\tilde\Xi$ with

$$
\tilde\Xi\star\tilde\Xi=\lambda e_0 .
$$

The root of $0$ is a nonzero nilpotent of index two, and the roots of $+1$ halve into the idempotents, the map $\xi\mapsto\tfrac12(e_0+\xi)$ carrying a root $\xi$ of $+1$ to an idempotent.

Written on the block, the equation is

$$
\tilde\Xi\diamond\tilde\Xi=\lambda e_0 ,
\qquad
\tilde\Xi\diamond\tilde\Xi=\operatorname{Vect}\bigl(\tilde\Xi\tilde\Xi^{*}\bigr).
$$

The left member is a **value of the block** and the right member is a **central element**, and that opposition is the whole content of the next section.

## The Parity Obstruction

**Theorem (no root of $-1$ and no root of $+1$).** For every $\tilde\Xi$ the value $\tilde\Xi\diamond\tilde\Xi$ is a pure vector, and no pure vector is a nonzero central element. Consequently the equations $\tilde\Xi\diamond\tilde\Xi=-e_0$ and $\tilde\Xi\diamond\tilde\Xi=+e_0$ have no solution, and the block has neither a root of $-1$ nor a root of $+1$.

*Proof.* The value $\tilde\Xi\diamond\tilde\Xi$ lies in the image of the block, which is the vector subspace $\operatorname{Vect}(\mathbb{B})$, so its scalar part vanishes. The element $\lambda e_0$ with $\lambda\neq0$ is central with scalar part $\lambda$, and the centre meets the vector subspace at the origin; hence $\operatorname{Vect}(\tilde\Xi\tilde\Xi^{*})=\lambda e_0$ with $\lambda\neq0$ is impossible. The case $\lambda=0$ is not excluded by the parity and is treated in the next section.

The obstruction is not the non-vanishing of the diagonal, and the distinction is worth keeping. A root of $+1$ would need the diagonal to be the central element $e_0$, and it is the **centrality** that fails, not the non-vanishing; the diagonal may vanish, and it does so on the quadric of the next section, and a vanishing diagonal is the root of $0$ and not of $\pm1$.

**Remark (the reading against the parent).** The same parity governs the two siblings. In the general plain sesquilinear product $\tilde\Xi\tilde Q^{*}$ the square is $\tilde\Xi\tilde\Xi^{*}$, which is Hermitian and generally has a nonvanishing scalar part, so the central equations are not immediately contradictory; in the block the projection is applied before the equation, and the scalar part is removed. The three central values of the four general products, and the contrast of the plain product, whose roots of $-1$ fill a quadric and whose roots of $+1$ halve into the idempotents, are *Square Roots of Minus One, Zero and Plus One*.

## The Roots of Zero

The equation $\tilde\Xi\diamond\tilde\Xi=0$ is the equation of the **square-zero element** of the block, and its solutions are the nonzero nilpotents.

**Theorem (the roots of $0$).** A nonzero element $\tilde\Xi$ satisfies $\tilde\Xi\diamond\tilde\Xi=0$ if and only if the plain product $\tilde\Xi\tilde\Xi^{*}$ is central, that is if and only if

$$
\tilde\Xi\tilde\Xi^{*}\in\mathbb{C}_{\mathbb{B}}
\iff
\operatorname{Vect}\bigl(\tilde\Xi\tilde\Xi^{*}\bigr)=0 ,
$$

and the roots of $0$ are exactly the nonzero elements of this set. The set is the **complex cone on the real unit sphere** of the quaternion subspace,

$$
\bigl\{\tilde\Xi\neq0:\ \tilde\Xi\tilde\Xi^{*}\ \text{central}\bigr\},
$$

of real dimension five, and it contains the centre, the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$.

*Proof.* By definition $\tilde\Xi\diamond\tilde\Xi=\operatorname{Vect}(\tilde\Xi\tilde\Xi^{*})$, which vanishes exactly when $\tilde\Xi\tilde\Xi^{*}$ is central. The identification of the set, its parametrisation and its dimension are *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*, where the criterion is computed; the three subspaces are read from the real basis, on which the diagonal vanishes identically, $e_\mu\diamond e_\mu=0$.

**Corollary (the three central values).** The block carries the nonzero roots of $0$ and no other root of a central value. The three equations read

| central value $\lambda$ | equation | solutions in the block |
|---|---|---|
| $-1$ | $\tilde\Xi\diamond\tilde\Xi=-e_0$ | none |
| $0$ | $\tilde\Xi\diamond\tilde\Xi=0$ | the nonzero square-zero elements, a real five-dimensional cone |
| $+1$ | $\tilde\Xi\diamond\tilde\Xi=+e_0$ | none |

The rows are the parity theorem and the theorem above; the middle row is quoted from the Specific Theory article named.

**Remark (no idempotent by halving).** The idempotents of the plain algebra are the halves of its roots of $+1$, $\tilde\Pi=\tfrac12(e_0+\xi)$. The construction needs the root $\xi$ of $+1$ and the unit $e_0$, and the block supplies neither: it has no root of $+1$ by the parity, and it has no unit by the absence recorded in *Norm and Invertibility in the Antisymmetric Plain Sesqualgebra*. The idempotents of the block are therefore not produced by the halving map, and they are computed directly in *Idempotents of the Antisymmetric Plain Sesqualgebra*: the only one is the origin.

## The Comparison with the Other Products

The parity is shared by the antisymmetric blocks and not by the general products, and the root-of-$0$ set separates the three antisymmetric blocks one from another.

### The Three Central Values in the Four General Products

In the four general products the equation $\tilde\Xi\star\tilde\Xi=\lambda e_0$ is not contradictory, and the roots are computed product by product in *Square Roots of Minus One, Zero and Plus One*. The plain product has a quadric of roots of $-1$ and the idempotents among its roots of $+1$; the natural product has the same two; the plain sesquilinear product has the Hermitian roots; and the quaternionic sesquilinear product has the family already quoted. The block is not among the four, and the parity that removes both signs is its own.

### The Two Failing Siblings

Among the antisymmetrisations the parity holds for all three, and the root-of-$0$ set distinguishes them. The bilinear sibling $\mathrm{APA}=\mathbf\Xi\times\mathbf{Q}$ is **alternating**, so $\tilde\Xi\star\tilde\Xi=0$ for every element and the root-of-$0$ set is the whole space with the origin removed. The quaternionic sesquilinear sibling $\mathrm{AQS}=\mathbf\Xi\times\overline{\mathbf{Q}}$ has the diagonal $\mathbf\Xi\times\overline{\mathbf\Xi}$, which vanishes exactly when the two real parts of $\mathbf\Xi$ are linearly dependent; its diagonal reads the vector part alone and leaves the scalar part free, so its root-of-$0$ set is the union of the complex planes $\mathbb{C}e_0\oplus\mathbb{C}\mathbf v$ over the real directions $\mathbf v$, of real dimension six. The block's set is the smaller one, the real five-dimensional cone on the real unit sphere, because the block's projection constrains the scalar part as well.

| block | $\tilde\Xi\star\tilde\Xi$ | roots of $0$ | roots of $\pm1$ |
|---|---|---|---|
| $\mathrm{APA}$ | $0$ identically | all nonzero elements, real dimension eight | none |
| $\mathrm{AQA}$ | $0$ identically | all nonzero elements, real dimension eight | none |
| $\mathrm{AQS}$ | $\mathbf\Xi\times\overline{\mathbf\Xi}$ | pairs with dependent real parts, real dimension six | none |
| $\mathrm{APS}$ | $\operatorname{Vect}(\tilde\Xi\tilde\Xi^{*})$ | the cone on the real unit sphere, real dimension five | none |

The bilinear and the quaternionic bilinear siblings $\mathrm{APA}$ and $\mathrm{AQA}$ are alternating, so their diagonal vanishes identically; the two sesquilinear siblings $\mathrm{APS}$ and $\mathrm{AQS}$ have a nonvanishing diagonal, and $\mathrm{AQS}$, whose diagonal reads the vector part alone, is the larger of the two sets, against the block, whose projection constrains the scalar part as well. The dimensions are the ones recorded for the sets in the sibling articles, and the block's is the one of *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*.

## Summary

The equation $\tilde\Xi\diamond\tilde\Xi=\lambda e_0$ is contradictory for both nonzero central values, because every value of the block is a pure vector and $\pm e_0$ are central: the block has **no root of $-1$ and no root of $+1$**. The obstruction is the centrality and not the non-vanishing of the diagonal, and it is a parity of the scalar part.

For $\lambda=0$ the roots are the nonzero elements with $\tilde\Xi\tilde\Xi^{*}$ central, that is the nonzero square-zero elements, and they form the complex cone on the real unit sphere of the quaternion subspace, of real dimension five, the centre, the real quaternion subspace and the anti-quaternion subspace lying inside it; the criterion and the quadric are *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*, and the class is *Nilpotents of the Antisymmetric Plain Sesqualgebra*.

The four general products have roots of the two nonzero central values, and their roots are *Square Roots of Minus One, Zero and Plus One*; the parity is shared with the three antisymmetric blocks, and the root-of-$0$ set separates them, the two alternating blocks filling the whole space and the quaternionic sesquilinear block carrying a real six-dimensional quadric against the block's real five-dimensional cone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi\diamond\tilde\Xi=\operatorname{Vect}(\tilde\Xi\tilde\Xi^{*})$ | the diagonal of the block, a pure vector |
| $\lambda e_0$ | the central value, with $\lambda\in\mathbb{C}$ |
| root of $\lambda$ in $\diamond$ | a nonzero $\tilde\Xi$ with $\tilde\Xi\diamond\tilde\Xi=\lambda e_0$ |
| $\tilde\Xi\tilde\Xi^{*}\in\mathbb{C}_{\mathbb{B}}$ | the criterion for the vanishing of the diagonal, hence for a root of $0$ |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}$ | the real quaternion, anti-quaternion and central subspaces, inside the square-zero set |
| $\mathrm{AQA}$, $\mathrm{AQS}$ | the alternating and the quaternionic sesquilinear siblings, with the same parity |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*Powers, the Square and the Roots* and §*The Nilpotent*, for the root of a central value and the square-zero element.
- *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-vector-part-of-the-square-and-the-jacobi-failure-of-the-antisymmetric-plain-sesqualgebra.md`), for the criterion for the vanishing of the diagonal and the quadric it traces.
- *Nilpotents of the Antisymmetric Plain Sesqualgebra* (`articles_maths/nilpotents-of-the-antisymmetric-plain-sesqualgebra.md`), for the square-zero class, its index and its conjugations.
- *Square Roots of Minus One, Zero and Plus One* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one.md`), for the roots of $-1$, $0$ and $+1$ in the four general products.
- *Square Roots of a General Element in the Antisymmetric Plain Sesqualgebra* (`articles_maths/square-roots-of-a-general-element-in-the-antisymmetric-plain-sesqualgebra.md`), for the classification of which the three central values are the degenerate data.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra.md`), for the same three equations in the plain product.
