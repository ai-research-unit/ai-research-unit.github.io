
# __The Hodge Star and the Real Structure of the Exterior Algebra__

## Introduction

When the finite-dimensional vector space $V$ carries a nondegenerate symmetric bilinear form and an orientation, the exterior algebra receives a further order-two-up-to-sign operator, the **Hodge star** $\star:\Lambda^kV\to\Lambda^{m-k}V$, determined by $\alpha\wedge\star\beta=\langle\alpha,\beta\rangle\theta$ for the volume element $\theta$ of the orientation. Its square is a sign, $\star\star=(-1)^{k(m-k)}$ on $\Lambda^kV$ for a form with discriminant one, and that sign decides the nature of the operator: where it is $+1$ the star is an **involution** and splits the component into two real subspaces; where it is $-1$ the star is a **complex structure**, an operator whose square is $-1$, and endows the component with the structure of a complex vector space. This article, the fifth of the `- * Theory` group, establishes the square of the star, constructs the real and the complex structures it defines, treats the middle degree where the two cases separate according to $m$ modulo four, and records the compatibility of the star with the grade involution, the reversion and the reversal of *Involutions of the Exterior Algebra*. The star in general, its formula in an orthogonal basis and its isometry property are the theory that this entry cites; the exterior algebra and its order-two maps are *The Exterior Algebra* and *Involutions of the Exterior Algebra*; the adjoint of the star belongs to the `- * Operator Theory` group and is deferred.

The base is a field $K$ of characteristic not two, $V$ has dimension $m$, the form is written $\langle\cdot,\cdot\rangle$, the volume element $\theta$ and the star $\star$. The form is used only through its nondegeneracy and the sign $\star^2=\pm1$; no length is formed from it.

## The Square of the Star

**Theorem.** With the form having discriminant one, the star satisfies

$$
\star\star=(-1)^{k(m-k)}\,\mathrm{id}\quad\text{on }\Lambda^kV ,
$$

so that $\star^2=\mathrm{id}$ when $k(m-k)$ is even and $\star^2=-\mathrm{id}$ when $k(m-k)$ is odd.

**Proof.** The star sends a basis $k$-vector to a scalar times the complementary basis vector; applying it twice returns the original vector, and the two signs of the two reorderings multiply to $(-1)^{k(m-k)}$, as computed in the theory of the Hodge star. $\square$

**Corollary.** On the components $\Lambda^0V$ and $\Lambda^mV$ the star has square $+1$; on $\Lambda^1V$ and $\Lambda^{m-1}V$ it has square $(-1)^{m-1}$; the sign depends only on $k$ and on the parity of $m$.

## The Real Structure

**Definition.** A **real structure** on a vector space is an involutive linear operator, that is an operator $J$ with $J^2=\mathrm{id}$; a **complex structure** is a linear operator $J$ with $J^2=-\mathrm{id}$, which makes the space a complex vector space with $J$ as multiplication by $i$.

**Theorem.** On a component $\Lambda^kV$ with $\star^2=\mathrm{id}$ the star is a real structure, and the component splits as the direct sum of the two eigenspaces

$$
\Lambda^kV=\Lambda^k_+V\oplus\Lambda^k_-V,\qquad \Lambda^k_\pm V=\{x:\star x=\pm x\},
$$

the **self-dual** and **anti-self-dual** parts; the projections are $\tfrac12(\mathrm{id}\pm\star)$.

**Proof.** An involutive linear operator is diagonalisable with eigenvalues $\pm1$ in characteristic not two, and the eigenspaces are the ranges of the spectral projections. $\square$

**Corollary.** The self-dual and anti-self-dual parts have equal dimension $\tfrac12\dim\Lambda^kV$ when $\star^2=\mathrm{id}$ and the component has even dimension; they are the eigenspaces of the star and are interchanged by any orientation-reversing isometry, while an orientation-preserving isometry preserves each.

## The Complex Structure

**Theorem.** On a component $\Lambda^kV$ with $\star^2=-\mathrm{id}$ the star is a complex structure, and $\Lambda^kV$ becomes a vector space over $\mathbb{C}$ with $i$ acting as $\star$; the complex dimension is $\tfrac12\dim\Lambda^kV$.

**Proof.** A linear operator with square $-1$ defines the structure of a module over $K[i]$ with $i$ acting as the operator, equivalently a complex vector space; the dimension halves because the minimal polynomial divides $T^2+1$. $\square$

**Corollary.** The star is then invertible with $\star^{-1}=-\star$, and the components $\Lambda^kV$ and $\Lambda^{m-k}V$ are exchanged by a complex-linear isomorphism, since $\star$ is complex-linear for its own complex structure.

## The Middle Degree

**Theorem.** Let $m$ be even and $k=m/2$. Then $\star^2=(-1)^{m^2/4}\mathrm{id}$ on the middle component, so

- if $m\equiv0\pmod 4$, the star is a real structure and the middle component splits into the self-dual and anti-self-dual parts;
- if $m\equiv2\pmod 4$, the star is a complex structure and the middle component is a complex vector space of dimension half its dimension.

**Proof.** Put $k=m/2$ in the square formula: $k(m-k)=m^2/4$, which is even exactly when $m$ is divisible by four, and odd exactly when $m\equiv2\pmod4$. $\square$

**Corollary.** The classical cases are $m=4$, where $\Lambda^2$ splits into two three-dimensional parts, and $m=6$, where $\Lambda^3$ is a complex space of dimension ten; the first gives the self-dual and anti-self-dual bivectors of the four-dimensional theory, the second the complex structure on the middle forms.

## Compatibility with the Other Order-Two Maps

**Proposition.** The star commutes with the grade involution, $\star\alpha=(-1)^{m-k}\alpha\star$ on $\Lambda^kV$, and with the reversion and the reversal up to the degree signs; on the even-dimensional middle component the star commutes with $\alpha$ exactly when $m$ is even.

**Proof.** The star sends $\Lambda^kV$ to $\Lambda^{m-k}V$, on which the grade involution acts by $(-1)^{m-k}$, whereas it acts by $(-1)^k$ on $\Lambda^kV$; the two differ by $(-1)^{m}$; the reversion and the reversal are treated by the same computation with their own signs. $\square$

**Corollary.** The three maps $\alpha,r,\alpha r$ of *Involutions of the Exterior Algebra* preserve the self-dual and anti-self-dual parts when they commute with the star, and interchange them when they anticommute; the star thus refines the group $(\mathbb{Z}/2)^2$ generated by them into a larger diagonalisable family.

## Worked Case: $\mathbb{R}^4$ and $\mathbb{R}^6$

For $V=\mathbb{R}^4$ the star on $\Lambda^2$ has square $+1$, so $\Lambda^2$ splits into the self-dual and anti-self-dual bivectors, each of dimension three; on $\Lambda^1$ the star maps to $\Lambda^3$ and has square $(-1)^{1\cdot3}=-1$, so it is a complex structure on the six-dimensional space $\Lambda^1\oplus\Lambda^3$ viewed with the induced operator.

For $V=\mathbb{R}^6$ the middle degree is $\Lambda^3$, of dimension twenty, and the star has square $(-1)^{9}=-1$, so it is a complex structure and $\Lambda^3$ is a complex space of dimension ten; the components $\Lambda^k$ and $\Lambda^{6-k}$ pair into complex spaces of total dimension $2\binom{6}{k}$ for $k\neq3$.

**Verified.** The squares of the star were recomputed for $m=4$ and $m=6$ on the basis elements of the exterior algebra, and the middle-degree signs $(-1)^{m^2/4}$ were checked against the general formula.

## Summary

With a nondegenerate symmetric bilinear form of discriminant one and an orientation, the **Hodge star** on $\Lambda^kV$ satisfies $\star^2=(-1)^{k(m-k)}\mathrm{id}$. Where the square is $+1$ the star is an involutive **real structure**, and the component splits into the **self-dual** and **anti-self-dual** eigenspaces of equal dimension; where the square is $-1$ the star is a **complex structure**, and the component becomes a complex vector space of half its dimension, with $\star^{-1}=-\star$. In the middle degree $k=m/2$ the square is $(-1)^{m^2/4}$, so the component carries a real structure when $m\equiv0\pmod4$ and a complex structure when $m\equiv2\pmod4$; the cases $m=4$ (self-dual bivectors) and $m=6$ (a complex middle space of dimension ten) are the classical instances. The star commutes or anticommutes with the grade involution, the reversion and the reversal according to the degree signs, refining the group they generate. The adjoint of the star belongs to the `- * Operator Theory` group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | the base field, of characteristic not two |
| $V$ | a finite-dimensional space with a nondegenerate symmetric form |
| $\langle\cdot,\cdot\rangle$ | the form and its determinant extension |
| $\theta$ | the volume element of the orientation |
| $\star$ | the Hodge star, $\Lambda^kV\to\Lambda^{m-k}V$ |
| $\Lambda^k_\pm V$ | the self-dual and anti-self-dual parts |
| $\alpha,r,\alpha r$ | the grade involution, reversion and reversal |

## Further Reading

- Werner Greub, *Multilinear Algebra*, Universitext (Springer, 2nd ed. 1978), for the Hodge star and its square.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the star, the self-dual forms and the complex structures on the middle exterior power.
- Frank W. Warner, *Foundations of Differentiable Manifolds and Lie Groups*, Graduate Texts in Mathematics 94 (Springer, 1983), for the star and its use in Hodge theory.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works, Volume 2 (Springer, 1997), for the order-two maps and the star.
