# __The Square Roots of a Central Value in the Four Products__

## Introduction

The elements of the biquaternion algebra whose square is a **central value** $\lambda e_0$ are the solutions of one equation per product, the square taken in that product:

$$
\tilde P\tilde P = \lambda e_0 , \qquad \tilde P^{\natural}\tilde P = \lambda e_0 , \qquad \tilde P\tilde P^{*} = \lambda e_0 , \qquad \tilde P^{\natural}\tilde P^{*} = \lambda e_0 .
$$

Each solution is a **square root of the central value** $\lambda$, and the four problems are of four different kinds. The first is the general square-root problem of the algebra, solved by the vector–scalar reduction (*Biquaternion Square Roots of a General Element*), whose three special values $-1$, $0$ and $+1$ are the subject of *Biquaternion Square Roots of Minus One, Zero and Plus One*. The second is the single complex equation $c(\tilde P) = \lambda$, because the square of that product is already central. The third and the fourth have square with real scalar part, non-negative for the third and indefinite for the fourth, so that the third has no root of a negative value at all while the fourth has roots of every real value. This article sets the four problems side by side, states for each $\lambda$ whether a root exists, and reads the roots through the central square, which decides which of them are units.

The article owns the comparison of the four root problems and the criterion $c(\tilde P\star\tilde P) = c(\tilde P)^{2}$ or $\lvert c(\tilde P)\rvert^{2}$ that it yields. The classification of the roots of $-1$, $0$ and $+1$ for the plain product is quoted from its owner, and the four squares from which the reductions start are *Comparison Between the Four Biquaternion Products* §*The Squares, the Idempotents and the Roots* and the four group articles.

**Conventions.** $\mathbb{B}$ has basis $e_0,e_1,e_2,e_3$, central scalar imaginary $i$ with $i^2 = -1$, and a general element is $\tilde P = P_0e_0+\mathbf P$ with $P_0\in\mathbb{C}$ and $\mathbf P = \sum_{k=1}^{3}P_ke_k$. The natural conjugation is $\tilde P^{\natural} = P_0-\mathbf P$, the star is $\tilde P^{*} = \overline{\tilde P^{\natural}}$, and the **central square** is $c(\tilde P)e_0 = \tilde P^{\natural}\tilde P = \tilde P\tilde P^{\natural}$ with $c(\tilde P) = \sum_\mu P_\mu^{2}$. A **central value** is an element $\lambda e_0$ with $\lambda\in\mathbb{C}$; the value is called non-zero when $\lambda\neq0$.

## The Plain Product: The Vector-Scalar Reduction

The plain square is $\tilde P^{2} = \bigl(P_0^{2}-(\mathbf P,\mathbf P)\bigr)e_0 + 2P_0\mathbf P$, an element with scalar part $P_0^{2}-(\mathbf P,\mathbf P)$ and vector part $2P_0\mathbf P$, and the equation $\tilde P^{2} = \lambda e_0$ is the pair

$$
P_0^{2}-(\mathbf P,\mathbf P) = \lambda , \qquad 2P_0\mathbf P = 0 .
$$

The second equation is the reduction: $P_0 = 0$ or $\mathbf P = 0$. The case $\mathbf P = 0$ gives $\tilde P = \pm\sqrt\lambda\,e_0$, two central roots; the case $P_0 = 0$ gives the roots in the vector subspace, the solutions of $-(\mathbf P,\mathbf P) = \lambda$, whose structure depends on $\lambda$. For the three special values the classification is the following, and it is the one of *Biquaternion Square Roots of Minus One, Zero and Plus One*.

**Theorem (the three special values, quoted).** In the plain product:

- the roots of $-1$ are the two trivial roots $\pm i$, the two-sphere $\pm\hat\mu$ of the pure real unit vectors, and the four-parameter family $\mathbf p+i\mathbf p'$ with $\mathbf p,\mathbf p'$ real, $\sum_k p_k^{2}-\sum_k p'^{2}_k = 1$ and $\sum_k p_kp'_k = 0$;
- the roots of $0$ are $0$ together with the nilpotent cone $\{P_0 = 0,\ (\mathbf P,\mathbf P) = 0\}$, of real dimension four;
- the roots of $+1$ are the products $\tilde P i$ of the roots of $-1$ with $i$.

All roots of $-1$ other than $\pm i$ are pure, hence lie in the vector subspace, and only the roots of $0$ fail to be units: the roots of $-1$ and of $+1$ are units, and the nonzero roots of $0$ are the nilpotents of the algebra.

The reduction is a general statement about every $\lambda$: writing $\lambda = \lambda_1+i\lambda_2$, the roots in the vector subspace solve the two real equations $\sum_k(\operatorname{Re}\mathbf P)_k^{2}-\sum_k(\operatorname{Im}\mathbf P)_k^{2} = -\lambda_1$ and $\sum_k(\operatorname{Re}\mathbf P)_k(\operatorname{Im}\mathbf P)_k = -\tfrac12\lambda_2$, and a root exists for every $\lambda$ because $\mathbf P = \sqrt{-\lambda}\,e_1$ solves the pair when the square root is branched. The plain product therefore has roots of every central value, and its root sets are the two central points $\pm\sqrt\lambda\,e_0$ together with the quadric cut out on the vector subspace (*Biquaternion Square Roots of a General Element*).

## The Natural Product: One Complex Equation

The square of the natural product is already central,

$$
\tilde P^{\natural}\tilde P = c(\tilde P)e_0 ,
$$

so the equation $\tilde P^{\natural}\tilde P = \lambda e_0$ is the single complex equation $c(\tilde P) = \lambda$.

**Theorem (the roots of the natural product, quoted).** The roots of the central value $\lambda$ in the complex quaternionic bilinear product are exactly the solutions of $c(\tilde P) = \lambda$: the zero-divisor set when $\lambda = 0$, and the nondegenerate complex quadric $c(\tilde P) = \lambda$ when $\lambda\neq0$. Each set is of real dimension six in $\mathbb{B}\cong\mathbb{R}^{8}$.

**Proof.** The square is central by *Biquaternions as a General Quaternionic Algebra (GQA) over $\mathbb{C}$* §*The Square Lies in the Scalar Line*, and the vanishing of the central square is the zero-divisor criterion (*Biquaternion Zero Divisors*). The set $\{c = \lambda\}$ is a nondegenerate quadric in the four complex coordinates, of complex dimension three when $\lambda\neq0$ and a cone of the same dimension when $\lambda = 0$, hence of real dimension six in both cases. $\square$

The natural product is the only one of the four whose root sets are solutions of a single scalar equation, and the reason is the one the comparison table records: the square of the natural product is the central element $c(\tilde P)e_0$, the central square itself. Its roots of $0$ are the whole zero-divisor cone, the largest square-zero set of the four, and its roots of a non-zero value are quadrics, so that this product has a root of every central value without exception.

## The Complex Sesquilinear Product: No Root of a Negative

The square of the complex sesquilinear product is Hermitian, and its scalar part is the sum of the modulus squares.

**Theorem (the roots of the sesquilinear product).** In the complex sesquilinear product the scalar part of the square is $\sum_\mu\lvert P_\mu\rvert^{2}$, a non-negative real number. The roots of the central value $\lambda$ are therefore of three kinds: no root at all when $\lambda$ is not a non-negative real number; the single root $\tilde P = 0$ when $\lambda = 0$; and, when $\lambda$ is a positive real number, a non-empty set of real dimension four, which for $\lambda = 1$ is the **unitary group** $\{\tilde U : \tilde U\tilde U^{*} = e_0\}\cong U(2)$ of *The Unitary Group of the Biquaternion Algebra*.

**Proof.** The scalar part is $\sum_\mu Q_\mu\overline{Q_\mu}$, of *The Squares and the Positive Cone of the Biquaternion Sesqualgebra*, and it is $\mathrm{Sc}(\lambda e_0) = \lambda$ for a root, so $\lambda$ is real and $\geq0$, with equality only at $\tilde P = 0$. For $\lambda>0$ the element $\sqrt\lambda\,e_0$ is a root, so the set is non-empty; for $\lambda = 1$ the equation $\tilde P\tilde P^{*} = e_0$ is, under the isomorphism $\Phi$, the equation $\Phi(\tilde P)\Phi(\tilde P)^{\dagger} = I$, because $\Phi(\tilde P^{*}) = \Phi(\tilde P)^{\dagger}$; a complex two-by-two matrix is unitary exactly when the product with its conjugate transpose is the identity, so the roots are the elements whose matrix is unitary, and the unitary group of the algebra is $U(2)$ of real dimension four. $\square$

The theorem is the sharpest existence statement of the four: the complex sesquilinear product is the only one of the four with central values that have **no** root, and it is the only one whose root of $0$ is the element $0$ alone. The two facts have one source, the definiteness of the scalar part $\sum_\mu\lvert P_\mu\rvert^{2}$, which is the same definiteness that makes the product's square-zero set the smallest of the four.

## The Complex Quaternionic Sesquilinear Product: Every Real Value

The square of the fourth product has scalar part the Krein form, indefinite, positive on the scalar coordinate and negative on the three vector coordinates.

**Theorem (the roots of the fourth product).** In the complex quaternionic sesquilinear product the scalar part of the square is the Krein value $\lvert P_0\rvert^{2}-\sum_k\lvert P_k\rvert^{2}$, a real number for every $\tilde P$. A root of the central value $\lambda$ exists exactly when $\lambda$ is real, and every real value has roots, among them $\sqrt\lambda\,e_0$ for $\lambda>0$, the elements $\pm e_k$ for $\lambda=-1$, the elements $\pm e_0$ and $\pm i$ for $\lambda=+1$, and the square-zero elements, among them $e_0+ie_1$, for $\lambda = 0$.

**Proof.** The scalar part is the Krein form of *The Square of the Quaternionic Sesquilinear Product and the Two Halves*, real for every $\tilde P$, so a non-real $\lambda$ has no root; for real $\lambda$ the displayed elements have the squares computed in the same article and in *The Four Biquaternion Complex Products* §*The Complex Quaternionic Sesquilinear Product $\tilde P^{\natural}\tilde Q^{*}$*: $e_k\star e_k = -e_0$, $e_0\star e_0 = e_0$, $i\star i = e_0$, and $(e_0+ie_1)\star(e_0+ie_1) = 0$. $\square$

The fourth product is the one whose root sets are indefinite, and the comparison is with its sibling sesquilinear product: the same equation, read through the two conjugations instead of the one, changes the non-negative sum $\sum_\mu\lvert P_\mu\rvert^{2}$ into the indefinite Krein form, and the change turns the empty root sets of the sibling into non-empty ones. The root of $-1$ that the complex sesquilinear product does not have is the root $e_k$ of the fourth product; the root of $0$ that the complex sesquilinear product has only at the origin is the square-zero family of the fourth product; and the two facts are one fact about a sign.

## The Roots Are Units, or Zero Divisors

The central square decides the nature of every root, and it decides it the same way for all four products.

**Theorem (a root of a non-zero central value is a unit).** Let $\tilde P$ be a root of the central value $\lambda$ in any one of the four products. Then $c(\tilde P\star\tilde P) = c(\tilde P)^{2}$ when the product is one of the two bilinear ones and $c(\tilde P\star\tilde P) = c(\tilde P)\overline{c(\tilde P)} = \lvert c(\tilde P)\rvert^{2}$ when it is one of the two sesquilinear ones. Consequently

$$
c(\tilde P)^{2} = \lambda^{2} \quad\text{or}\quad \lvert c(\tilde P)\rvert^{2} = \lambda^{2} , \qquad c(\tilde P)\neq0 \iff \lambda\neq0 ,
$$

and every root of a non-zero central value is a unit, while every non-zero root of $0$ is a zero divisor.

**Proof.** The four multiplicative laws are those of *The Annihilating Elements of the Four Products*: $c$ is multiplicative for the two bilinear products and satisfies $c(f(\tilde P,\tilde Q)) = c(\tilde P)\overline{c(\tilde Q)}$ for the two sesquilinear ones, so the central square of the square is $c(\tilde P)^{2}$ or $c(\tilde P)\overline{c(\tilde P)} = \lvert c(\tilde P)\rvert^{2}$ according to the pair. The value of the square is $\lambda e_0$, whose central square is $\lambda^{2}e_0$, and the criterion of invertibility is $c\neq0$ (*Biquaternion Norm and Invertibility*). $\square$

The theorem is the reason the three central values $-1$, $0$, $+1$ are the interesting ones. The roots of $-1$ and of $+1$ lie in the group of units for the four products wherever they exist; the roots of $0$ are the zero divisors wherever they exist, except in the complex sesquilinear product, where they collapse to the origin, and except for the element $0$ itself, which is neither. The roots of $-1$ of the plain product are the parameter set of the idempotents (*Biquaternion Idempotents and Projections*), so the classification of the previous article in this group is the classification of these roots read through the idempotent map; and the roots of $0$ of the natural product are the whole cone of the previous article. The four root problems are therefore the four ways the same two questions — where is the square zero, and where is it minus the unit — are answered.

## Summary

The four products of *The Four Biquaternion Complex Products* give four square-root problems for a central value $\lambda e_0$, and they differ in whether a root exists and in what the roots are. The plain product reduces to the pair $P_0^{2}-(\mathbf P,\mathbf P) = \lambda$, $2P_0\mathbf P = 0$; the natural product reduces to the single complex equation $c(\tilde P) = \lambda$; the complex sesquilinear product has square with scalar part $\sum_\mu\lvert P_\mu\rvert^{2}$; and the complex quaternionic sesquilinear product has square with scalar part the Krein value $\lvert P_0\rvert^{2}-\sum_k\lvert P_k\rvert^{2}$.

The plain product has roots of every value, its roots of $-1$ splitting into the trivial pair $\pm i$, the two-sphere of pure real unit vectors and a four-parameter family, its roots of $0$ being the nilpotent cone, and its roots of $+1$ the products of the roots of $-1$ with $i$. The natural product has roots of every value, the roots of a non-zero value being a quadric of real dimension six and the roots of $0$ the whole zero-divisor cone. The complex sesquilinear product has no root of a non-real or negative value, its only root of $0$ is $\tilde P = 0$, and its roots of $1$ are the unitary group $\cong U(2)$; and the complex quaternionic sesquilinear product has roots of every real value and none of a non-real one, the roots of $\pm1$ being units and the roots of $0$ a proper subfamily of the cone.

For all four products the central square of a square is $c(\tilde P)^{2}$ or $\lvert c(\tilde P)\rvert^{2}$, so a root of a non-zero central value is a unit and a non-zero root of $0$ is a zero divisor. The four idempotent sets, which are the roots of the central value $-1$ read through the map $\xi\mapsto\tfrac12(e_0+\xi i)$ for the algebra, are *The Idempotents of the Four Products*; the squares and the four scalar parts from which the reductions start are *Relations Between the Four Biquaternion Products* §*The Four Scalar Parts*; and the four root sets themselves are tabulated in *Comparison Between the Four Biquaternion Products*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\lambda e_0$ | a central value, $\lambda\in\mathbb{C}$ |
| $\tilde P\star\tilde P$ | the square in the product at hand |
| $c(\tilde P)e_0 = \tilde P^{\natural}\tilde P$ | the central square; $c(\tilde P) = \sum_\mu P_\mu^{2}$ |
| $\lvert P_0\rvert^{2}-\sum_k\lvert P_k\rvert^{2}$ | the Krein form, the scalar part of the fourth product's square |
| $\pm\hat\mu$ | the pure real unit vectors, the real roots of $-1$ |

## Further Reading

- *Biquaternion Square Roots of Minus One, Zero and Plus One* (`articles_maths/biquaternion-square-roots-of-minus-one-zero-and-plus-one.md`), for the classification of the three special values in the plain product.
- *Biquaternion Square Roots of a General Element* (`articles_maths/biquaternion-square-roots-of-a-general-element.md`), for the vector–scalar reduction for an arbitrary value.
- *Relations Between the Four Biquaternion Products* (`articles_maths/relations-between-the-four-biquaternion-products.md`), for the four scalar parts of the four squares.
- *The Square of the Quaternionic Sesquilinear Product and the Two Halves* (`articles_maths/the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.md`), for the Krein scalar part and the square-zero subfamily.
- *The Squares and the Positive Cone of the Biquaternion Sesqualgebra* (`articles_maths/the-squares-and-the-positive-cone-of-the-biquaternion-sesqualgebra.md`), for the non-negative scalar part of the complex sesquilinear square.
- *Biquaternions as a General Quaternionic Algebra (GQA) over $\mathbb{C}$* (`articles_maths/biquaternions-as-a-general-quaternionic-algebra-gqa-over-c.md`), for the central square of the natural product.
- *The Unitary Group of the Biquaternion Algebra* (`articles_maths/the-unitary-group-of-the-biquaternion-algebra.md`), for the unitary group and its dimension.
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the criterion $c\neq0$ with which the roots are classified as units or zero divisors.
- *The Idempotents of the Four Products* (`articles_maths/the-idempotents-of-the-four-products.md`), for the idempotent reading of the roots of $1$.
- *Comparison Between the Four Biquaternion Products* (`articles_maths/comparison-between-the-four-biquaternion-products.md`), for the tabulation of the four root problems.
