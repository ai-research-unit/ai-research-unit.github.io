# __Square Roots of a General Element in the General Quaternionic Algebra__

## Introduction

The square roots of the three distinguished central values are solved in *Square Roots of One and the Idempotents of the General Quaternionic Algebra* and *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*. This article solves the general problem of the block: for a given element $\tilde q$ of $\mathbb{H}$, find the elements $\tilde\xi$ with

$$
\tilde\xi \star \tilde\xi = \tilde q ,
$$

the square being read in the general quaternionic bilinear product $\tilde\xi \star \tilde\xi = \tilde\xi^{\natural}\tilde\xi$ of *Introduction to the General Quaternionic Algebra of Quaternions*.

The solution is short and it is decisive: since the square of every element is the central element $N(\tilde\xi)e_0$, the right-hand side of the equation must be central, and when it is central the equation reduces to the norm equation of the preceding article. The quaternionic square map is therefore **central-valued**: it is not a map of $\mathbb{H}$ into itself but a map onto the scalar line, and the general square-root problem has a solution exactly for the central elements and for no others. The problem for the plain product on the same space is *Square Roots of a General Element in the General Plain Algebra*, where the map is genuinely $\mathbb{H}$-valued and the answer is not restricted to the scalar line.

## The Reduction

**Theorem (the reduction).** For $\tilde q \in \mathbb{H}$ the equation $\tilde\xi \star \tilde\xi = \tilde q$ has a solution exactly when $\tilde q$ is **central**, that is $\tilde q = \lambda e_0$ for some $\lambda \in \mathbb{R}$. In that case the solutions are the roots of the central value $\lambda$,

$$
\{\tilde\xi : \tilde\xi \star \tilde\xi = \lambda e_0\} = \{\tilde\xi : N(\tilde\xi) = \lambda\} .
$$

*Proof.* The square is $\tilde\xi^{\natural}\tilde\xi = N(\tilde\xi)e_0$, a real multiple of $e_0$; its vector part vanishes identically. A solution therefore forces the vector part of $\tilde q$ to vanish, so $\tilde q = \lambda e_0$ with $\lambda = q_0$; conversely, if $\tilde q = \lambda e_0$ the equation is $N(\tilde\xi) = \lambda$, the reduction of the preceding article.

**Corollary.** The image of the square map $\tilde\xi \mapsto \tilde\xi \star \tilde\xi$ is the scalar line $\mathbb{R}e_0$, and it is the whole scalar line when the base field has square roots of the non-negative values; the fibres of the square map are the level sets of the norm.

*Proof.* The image is contained in the scalar line by the reduction, and every central value is the square of a root when the equation $N(\tilde\xi) = \lambda$ is soluble, which over $\mathbb{R}$ happens exactly for $\lambda \geq 0$.

**Remark (the contrast with the plain square).** The plain square is $\mathbb{H}$-valued and the plain square-root problem is solved element by element; for example $e_1$ is the plain square of $\tilde\xi = (e_0+e_1)/\sqrt{2}$, since $\tilde\xi^2 = (e_0+e_1)^2/2 = e_1$. A non-central element of $\mathbb{H}$ therefore has plain square roots. In the quaternionic product the same element is not a square at all, and no non-central element is. The scalar–vector split, which for the plain square gives the pair $\xi_0^2 - N(\vec\xi) = q_0$ and $2\xi_0\vec\xi = \vec q$, collapses here to the single scalar equation and to the vanishing of the vector part of $\tilde q$.

## The Classification of the Roots

**Theorem (the classification).** Let $\tilde q = \lambda e_0$ be a central element of $\mathbb{H}$ and let the square-root problem be read in the quaternionic product. Then:

1. for $\lambda > 0$ there is a three-dimensional set of roots, the level set $N = \lambda$, and it is nonempty;
2. for $\lambda = 0$ the unique root is $\tilde\xi = 0$;
3. for $\lambda < 0$ there is no root at all.

*Proof.* The root set is $\{\tilde\xi : N(\tilde\xi) = \lambda\}$; the norm is positive definite over $\mathbb{R}$, so it takes each positive value on a set of real dimension three and the value $0$ at the origin alone, and negative values are not taken.

**Corollary.** The solution set is never a finite set except at $\lambda = 0$, and the number of roots of a positive central value is the cardinality of the continuum; the article states the count by dimension rather than by cardinality, as the corpus does.

## Worked Examples

Each example is recomputed from the closed form $\tilde\xi \star \tilde\xi = N(\tilde\xi)e_0$.

| right-hand side | equation | root set |
|---|---|---|
| $\tilde q = e_0$ | $N(\tilde\xi) = 1$ | the norm-one level set, real dimension three |
| $\tilde q = 4e_0$ | $N(\tilde\xi) = 4$ | the level set $N = 4$, real dimension three |
| $\tilde q = 0$ | $N(\tilde\xi) = 0$ | the single element $0$ |
| $\tilde q = -e_0$ | $N(\tilde\xi) = -1$ | empty |
| $\tilde q = e_1$ | $N(\tilde\xi)e_0 = e_1$ | empty, the two sides having different vector parts |
| $\tilde q = e_0 + e_1$ | $N(\tilde\xi)e_0 = e_0 + e_1$ | empty, for the same reason |

**Proposition (the worked examples).** The five rows are correct, and the closed form decides all of them without a case distinction beyond the sign of the value and the vanishing of the vector part of $\tilde q$.

*Proof.* In the first three rows $\tilde q$ is central, $\lambda = 1, 4, 0$, and the classification applies; in the last three rows $\tilde q$ is non-central or the value is negative, and the reduction or the definiteness of the norm excludes a solution. The example $\tilde q = 4e_0$ has the explicit root $\tilde\xi = 2e_0$, and the example $\tilde q = e_1$ has no root because the vector part of the left-hand side always vanishes while the right-hand side is $e_1$.

## The Central Values

**Corollary (the specialisation).** Substituting $\lambda = -1, 0, +1$ recovers the three root sets of *Square Roots of One and the Idempotents of the General Quaternionic Algebra* (the signed values) and *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra* (the value $0$): the empty set, the single element $0$, and the norm-one level set. The general problem therefore contains the distinguished ones, and the comparison made there against the plain product applies verbatim to the positive central values.

*Proof.* The classification above at the three values gives the three root sets, which are those of the quoted article; the general theory of the root of a central value across the products is *Square Roots of a General Element in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, below this article in this category.

**Remark.** The reduction has a second reading, as a statement about the multiplication operators of the block. The square map is the diagonal of the symmetrised product, and its collapse onto the scalar line is the statement that the symmetrisation of the quaternionic product is scalar-valued; the obstruction to solving the general square-root problem is therefore the same obstruction that makes the symmetrised product unfit to be the multiplication of an algebra, and it is read in *The Symmetrised Quaternionic Product and the Hermitian Subspace*, below this article in this category.

## Summary

The square in the general quaternionic algebra is always central, $\tilde\xi \star \tilde\xi = N(\tilde\xi)e_0$, so the general square-root problem $\tilde\xi \star \tilde\xi = \tilde q$ has a solution exactly when $\tilde q$ is central, $\tilde q = \lambda e_0$, and then the roots are the level set of the norm at $\lambda$. For $\lambda > 0$ the root set has real dimension three, for $\lambda = 0$ it is the single element $0$, and for $\lambda < 0$ it is empty. The worked examples confirm the reduction: $e_0$ and $4e_0$ have three-dimensional root sets, $0$ has one root, and $-e_0$, $e_1$ and $e_0 + e_1$ have none. The specialisation to $\lambda = -1, 0, +1$ recovers the three distinguished root sets. The plain product on the same space has a genuinely $\mathbb{H}$-valued square, and the collapse of the quaternionic square onto the scalar line is the whole difference between the two problems.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\xi \star \tilde\xi = N(\tilde\xi)e_0$ | the square in the quaternionic product |
| $\tilde q = \lambda e_0$ | a central element, the only soluble right-hand sides |
| $\{\tilde\xi : N(\tilde\xi) = \lambda\}$ | the root set of the central value $\lambda$ |
| $\mathbb{R}e_0$ | the scalar line, the image of the square map |
| $\tilde\xi^2$ | the plain square, for contrast |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the square map of a nonassociative product and the central values in its image.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the diagonal of a symmetrised product and the quadratic representation it generates.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for square roots in the quaternion algebra.
- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the classical treatment of the quaternion square.
