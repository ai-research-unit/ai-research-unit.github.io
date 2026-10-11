# __The Square Roots of a Central Value in the Four General Products__

## Introduction

The elements of the biquaternion algebra whose square is a **central value** $\lambda e_0$ are the solutions of one equation per product, the square taken in that product:

$$
\tilde\Xi\tilde\Xi = \lambda e_0 , \qquad \tilde\Xi^{\natural}\tilde\Xi = \lambda e_0 , \qquad \tilde\Xi\tilde\Xi^{*} = \lambda e_0 , \qquad \tilde\Xi^{\natural}\tilde\Xi^{*} = \lambda e_0 .
$$

Each solution is a **square root of the central value** $\lambda$, and the four problems are of four different kinds. The first is the general square-root problem of the algebra, solved by the vector–scalar reduction (*Square Roots of a General Element in the General Plain Algebra*), whose three special values $-1$, $0$ and $+1$ are the subject of *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*. The second is the single complex equation $c(\tilde\Xi) = \lambda$, because the square of that product is already central. The third and the fourth have square with real scalar part, non-negative for the third and indefinite for the fourth, so that the third has no root of a negative value at all while the fourth has roots of every real value. This article sets the four problems side by side, states for each $\lambda$ whether a root exists, and reads the roots through the central square, which decides which of them are units.

The article owns the comparison of the four root problems and the criterion $c(\tilde\Xi\star\tilde\Xi) = c(\tilde\Xi)^{2}$ or $\lvert c(\tilde\Xi)\rvert^{2}$ that it yields. The classification of the roots of $-1$, $0$ and $+1$ for the plain product is quoted from its owner, and the four squares from which the reductions start are *Comparison Between the Four General Products* §*The Squares, the Idempotents and the Roots* and the four group articles.

**Conventions.** $\mathbb{B}$ has basis $e_0,e_1,e_2,e_3$, central scalar imaginary $i$ with $i^2 = -1$, and a general element is $\tilde\Xi = \Xi_0e_0+\mathbf\Xi$ with $\Xi_0\in\mathbb{C}$ and $\mathbf\Xi = \sum_{k=1}^{3}\Xi_ke_k$. The natural conjugation is $\tilde\Xi^{\natural} = \Xi_0-\mathbf\Xi$, the star is $\tilde\Xi^{*} = \overline{\tilde\Xi^{\natural}}$, and the **central square** is $c(\tilde\Xi)e_0 = \tilde\Xi^{\natural}\tilde\Xi = \tilde\Xi\tilde\Xi^{\natural}$ with $c(\tilde\Xi) = \sum_\mu \Xi_\mu^{2}$. A **central value** is an element $\lambda e_0$ with $\lambda\in\mathbb{C}$; the value is called non-zero when $\lambda\neq0$.

## The Plain Product: The Vector-Scalar Reduction

The plain square is $\tilde\Xi^{2} = \bigl(\Xi_0^{2}-(\mathbf\Xi,\mathbf\Xi)\bigr)e_0 + 2\Xi_0\mathbf\Xi$, an element with scalar part $\Xi_0^{2}-(\mathbf\Xi,\mathbf\Xi)$ and vector part $2\Xi_0\mathbf\Xi$, and the equation $\tilde\Xi^{2} = \lambda e_0$ is the pair

$$
\Xi_0^{2}-(\mathbf\Xi,\mathbf\Xi) = \lambda , \qquad 2\Xi_0\mathbf\Xi = 0 .
$$

The second equation is the reduction: $\Xi_0 = 0$ or $\mathbf\Xi = 0$. The case $\mathbf\Xi = 0$ gives $\tilde\Xi = \pm\sqrt\lambda\,e_0$, two central roots; the case $\Xi_0 = 0$ gives the roots in the vector subspace, the solutions of $-(\mathbf\Xi,\mathbf\Xi) = \lambda$, whose structure depends on $\lambda$. For the three special values the classification is the following, and it is the one of *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*.

**Theorem (the three special values, quoted).** In the plain product:

- the roots of $-1$ are the two trivial roots $\pm i$, the family $\pm\hat\mu$ of the pure real unit vectors, and the four-parameter family $\mathbf p+i\mathbf p'$ with $\mathbf p,\mathbf p'$ real, $\sum_k p_k^{2}-\sum_k p'^{2}_k = 1$ and $\sum_k p_kp'_k = 0$;
- the roots of $0$ are $0$ together with the nilpotent cone $\{\Xi_0 = 0,\ (\mathbf\Xi,\mathbf\Xi) = 0\}$, of real dimension four;
- the roots of $+1$ are the products $\tilde\Xi i$ of the roots of $-1$ with $i$.

All roots of $-1$ other than $\pm i$ are pure, hence lie in the vector subspace, and only the roots of $0$ fail to be units: the roots of $-1$ and of $+1$ are units, and the nonzero roots of $0$ are the nilpotents of the algebra, written $\tilde\Upsilon$ where the nilpotency is the point (§*The nilpotent convention* of *Conventions in Mathematics*).

The reduction is a general statement about every $\lambda$: writing $\lambda = \lambda_1+i\lambda_2$, the roots in the vector subspace solve the two real equations $\sum_k(\operatorname{Re}\mathbf\Xi)_k^{2}-\sum_k(\operatorname{Im}\mathbf\Xi)_k^{2} = -\lambda_1$ and $\sum_k(\operatorname{Re}\mathbf\Xi)_k(\operatorname{Im}\mathbf\Xi)_k = -\tfrac12\lambda_2$, and a root exists for every $\lambda$ because $\mathbf\Xi = \sqrt{-\lambda}\,e_1$ solves the pair when the square root is branched. The plain product therefore has roots of every central value, and its root sets are the two central points $\pm\sqrt\lambda\,e_0$ together with the quadric cut out on the vector subspace (*Square Roots of a General Element in the General Plain Algebra*).

## The Natural Product: One Complex Equation

The square of the natural product is already central,

$$
\tilde\Xi^{\natural}\tilde\Xi = c(\tilde\Xi)e_0 ,
$$

so the equation $\tilde\Xi^{\natural}\tilde\Xi = \lambda e_0$ is the single complex equation $c(\tilde\Xi) = \lambda$.

**Theorem (the roots of the natural product, quoted).** The roots of the central value $\lambda$ in the general quaternionic bilinear product are exactly the solutions of $c(\tilde\Xi) = \lambda$: the zero-divisor set when $\lambda = 0$, and the nondegenerate complex quadric $c(\tilde\Xi) = \lambda$ when $\lambda\neq0$. Each set is of real dimension six in $\mathbb{B}\cong\mathbb{R}^{8}$.

**Proof.** The square is central by *Introduction to the General Quaternionic Algebra of Biquaternions* §*The Square Lies in the Scalar Line*, and the vanishing of the central square is the zero-divisor criterion (*Zero Divisors of the General Plain Algebra*). The set $\{c = \lambda\}$ is a nondegenerate quadric in the four complex coordinates, of complex dimension three when $\lambda\neq0$ and a cone of the same dimension when $\lambda = 0$, hence of real dimension six in both cases.

The natural product is the only one of the four whose root sets are solutions of a single scalar equation, and the reason is the one the comparison table records: the square of the natural product is the central element $c(\tilde\Xi)e_0$, the central square itself. Its roots of $0$ are the whole zero-divisor cone, the largest square-zero set of the four, and its roots of a non-zero value are quadrics, so that this product has a root of every central value without exception.

## The General Plain Sesquilinear Product: No Root of a Negative

The square of the general plain sesquilinear product is Hermitian, and its scalar part is the sum of the modulus squares.

**Theorem (the roots of the sesquilinear product).** In the general plain sesquilinear product the scalar part of the square is $\sum_\mu\lvert \Xi_\mu\rvert^{2}$, a non-negative real number. The roots of the central value $\lambda$ are therefore of three kinds: no root at all when $\lambda$ is not a non-negative real number; the single root $\tilde\Xi = 0$ when $\lambda = 0$; and, when $\lambda$ is a positive real number, a non-empty set of real dimension four, which for $\lambda = 1$ is the **unitary group** $\{\tilde U : \tilde U\tilde U^{*} = e_0\}\cong U(2)$ of *The Unitary Group of the Biquaternion Algebra*.

**Proof.** The scalar part is $\sum_\mu Q_\mu\overline{Q_\mu}$, of *The Squares and the Positive Cone of the Biquaternion Sesqualgebra*, and it is $\mathrm{Sc}(\lambda e_0) = \lambda$ for a root, so $\lambda$ is real and $\geq0$, with equality only at $\tilde\Xi = 0$. For $\lambda>0$ the element $\sqrt\lambda\,e_0$ is a root, so the set is non-empty; for $\lambda = 1$ the equation $\tilde\Xi\tilde\Xi^{*} = e_0$ is, under the isomorphism $\Phi$, the equation $\Phi(\tilde\Xi)\Phi(\tilde\Xi)^{\dagger} = I$, because $\Phi(\tilde\Xi^{*}) = \Phi(\tilde\Xi)^{\dagger}$; a complex two-by-two matrix is unitary exactly when the product with its conjugate transpose is the identity, so the roots are the elements whose matrix is unitary, and the unitary group of the algebra is $U(2)$ of real dimension four.

The theorem is the sharpest existence statement of the four: the general plain sesquilinear product is the only one of the four general products with central values that have **no** root, and it is the only one whose root of $0$ is the element $0$ alone. The two facts have one source, the definiteness of the scalar part $\sum_\mu\lvert \Xi_\mu\rvert^{2}$, which is the same definiteness that makes the product's square-zero set the smallest of the four.

## The General Quaternionic Sesquilinear Product: Every Real Value

The square of the fourth product has scalar part the Krein form, indefinite, positive on the scalar coordinate and negative on the three vector coordinates.

**Theorem (the roots of the fourth product).** In the general quaternionic sesquilinear product the scalar part of the square is the Krein value $\lvert \Xi_0\rvert^{2}-\sum_k\lvert \Xi_k\rvert^{2}$, a real number for every $\tilde\Xi$. A root of the central value $\lambda$ exists exactly when $\lambda$ is real, and every real value has roots, among them $\sqrt\lambda\,e_0$ for $\lambda>0$, the elements $\pm e_k$ for $\lambda=-1$, the elements $\pm e_0$ and $\pm i$ for $\lambda=+1$, and the square-zero elements, among them $e_0+ie_1$, for $\lambda = 0$.

**Proof.** The scalar part is the Krein form of *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*, real for every $\tilde\Xi$, so a non-real $\lambda$ has no root; for real $\lambda$ the displayed elements have the squares computed in the same article and in *The Four General Products of the Biquaternion $\mathbb{C}$ Space* §*The General Quaternionic Sesquilinear Product $\tilde\Xi^{\natural}\tilde Q^{*}$*: $e_k\star e_k = -e_0$, $e_0\star e_0 = e_0$, $i\star i = e_0$, and $(e_0+ie_1)\star(e_0+ie_1) = 0$.

The fourth product is the one whose root sets are indefinite, and the comparison is with its sibling sesquilinear product: the same equation, read through the two conjugations instead of the one, changes the non-negative sum $\sum_\mu\lvert \Xi_\mu\rvert^{2}$ into the indefinite Krein form, and the change turns the empty root sets of the sibling into non-empty ones. The root of $-1$ that the general plain sesquilinear product does not have is the root $e_k$ of the fourth product; the root of $0$ that the general plain sesquilinear product has only at the origin is the square-zero family of the fourth product; and the two facts are one fact about a sign.

## The Roots Are Units, or Zero Divisors

The central square decides the nature of every root, and it decides it the same way for all four general products.

**Theorem (a root of a non-zero central value is a unit).** Let $\tilde\Xi$ be a root of the central value $\lambda$ in any one of the four general products. Then $c(\tilde\Xi\star\tilde\Xi) = c(\tilde\Xi)^{2}$ when the product is one of the two bilinear ones and $c(\tilde\Xi\star\tilde\Xi) = c(\tilde\Xi)\overline{c(\tilde\Xi)} = \lvert c(\tilde\Xi)\rvert^{2}$ when it is one of the two sesquilinear ones. Consequently

$$
c(\tilde\Xi)^{2} = \lambda^{2} \quad\text{or}\quad \lvert c(\tilde\Xi)\rvert^{2} = \lambda^{2} , \qquad c(\tilde\Xi)\neq0 \iff \lambda\neq0 ,
$$

and every root of a non-zero central value is a unit, while every non-zero root of $0$ is a zero divisor.

**Proof.** The four multiplicative laws are those of *The Annihilating Elements of the Four General Products*: $c$ is multiplicative for the two bilinear products and satisfies $c(f(\tilde\Xi,\tilde Q)) = c(\tilde\Xi)\overline{c(\tilde Q)}$ for the two sesquilinear ones, so the central square of the square is $c(\tilde\Xi)^{2}$ or $c(\tilde\Xi)\overline{c(\tilde\Xi)} = \lvert c(\tilde\Xi)\rvert^{2}$ according to the pair. The value of the square is $\lambda e_0$, whose central square is $\lambda^{2}e_0$, and the criterion of invertibility is $c\neq0$ (*Norm and Invertibility in the General Plain Algebra*).

The theorem is the reason the three central values $-1$, $0$, $+1$ are the interesting ones. The roots of $-1$ and of $+1$ lie in the group of units for the four general products wherever they exist; the roots of $0$ are the zero divisors wherever they exist, except in the general plain sesquilinear product, where they collapse to the origin, and except for the element $0$ itself, which is neither. The roots of $-1$ of the plain product are the parameter set of the idempotents (*Idempotents of the General Plain Algebra*), so the classification of the previous article in this group is the classification of these roots read through the idempotent map; and the roots of $0$ of the natural product are the whole cone of the previous article. The four root problems are therefore the four ways the same two questions — where is the square zero, and where is it minus the unit — are answered.

## Summary

The four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* give four square-root problems for a central value $\lambda e_0$, and they differ in whether a root exists and in what the roots are. The plain product reduces to the pair $\Xi_0^{2}-(\mathbf\Xi,\mathbf\Xi) = \lambda$, $2\Xi_0\mathbf\Xi = 0$; the natural product reduces to the single complex equation $c(\tilde\Xi) = \lambda$; the general plain sesquilinear product has square with scalar part $\sum_\mu\lvert \Xi_\mu\rvert^{2}$; and the general quaternionic sesquilinear product has square with scalar part the Krein value $\lvert \Xi_0\rvert^{2}-\sum_k\lvert \Xi_k\rvert^{2}$.

The plain product has roots of every value, its roots of $-1$ splitting into the trivial pair $\pm i$, the family of pure real unit vectors and a four-parameter family, its roots of $0$ being the nilpotent cone, and its roots of $+1$ the products of the roots of $-1$ with $i$. The natural product has roots of every value, the roots of a non-zero value being a quadric of real dimension six and the roots of $0$ the whole zero-divisor cone. The general plain sesquilinear product has no root of a non-real or negative value, its only root of $0$ is $\tilde\Xi = 0$, and its roots of $1$ are the unitary group $\cong U(2)$; and the general quaternionic sesquilinear product has roots of every real value and none of a non-real one, the roots of $\pm1$ being units and the roots of $0$ a proper subfamily of the cone.

For all four general products the central square of a square is $c(\tilde\Xi)^{2}$ or $\lvert c(\tilde\Xi)\rvert^{2}$, so a root of a non-zero central value is a unit and a non-zero root of $0$ is a zero divisor. The four idempotent sets, which are the roots of the central value $-1$ read through the map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi i)$ for the algebra, are *The Idempotents of the Four General Products*; the squares and the four scalar parts from which the reductions start are *Relations Between the Four General Products* §*The Four Scalar Parts*; and the four root sets themselves are tabulated in *Comparison Between the Four General Products*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\lambda e_0$ | a central value, $\lambda\in\mathbb{C}$ |
| $\tilde\Xi\star\tilde\Xi$ | the square in the product at hand |
| $c(\tilde\Xi)e_0 = \tilde\Xi^{\natural}\tilde\Xi$ | the central square; $c(\tilde\Xi) = \sum_\mu \Xi_\mu^{2}$ |
| $\lvert \Xi_0\rvert^{2}-\sum_k\lvert \Xi_k\rvert^{2}$ | the Krein form, the scalar part of the fourth product's square |
| $\pm\hat\mu$ | the pure real unit vectors, the real roots of $-1$ |

## Further Reading

- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra.md`), for the classification of the three special values in the plain product.
- *Square Roots of a General Element in the General Plain Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-general-plain-algebra.md`), for the vector–scalar reduction for an arbitrary value.
- *Relations Between the Four General Products* (`articles_maths/relations-between-the-four-general-products.md`), for the four scalar parts of the four squares.
- *The Square of the General Quaternionic Sesquilinear Product and the Two Halves* (`articles_maths/the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.md`), for the Krein scalar part and the square-zero subfamily.
- *The Squares and the Positive Cone of the Biquaternion Sesqualgebra* (`articles_maths/the-squares-and-the-positive-cone-of-the-biquaternion-sesqualgebra.md`), for the non-negative scalar part of the general plain sesquilinear square.
- *Introduction to the General Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-biquaternions.md`), for the central square of the natural product.
- *The Unitary Group of the Biquaternion Algebra* (`articles_maths/the-unitary-group-of-the-biquaternion-algebra.md`), for the unitary group and its dimension.
- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra.md`), for the criterion $c\neq0$ with which the roots are classified as units or zero divisors.
- *The Idempotents of the Four General Products* (`articles_maths/the-idempotents-of-the-four-general-products.md`), for the idempotent reading of the roots of $1$.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the tabulation of the four root problems.
