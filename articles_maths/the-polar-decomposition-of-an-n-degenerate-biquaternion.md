# __The Polar Decomposition of an N-Degenerate Biquaternion__

## Introduction

The general polar decomposition of *The Polar Decomposition of a Biquaternion* writes every biquaternion as

$$
\tilde Q=\tilde Q_H\,\tilde Q_0,
$$

with $\tilde Q_H$ Hermitian positive semidefinite and $\tilde Q_0$ a partial isometry. The companion article *The Polar Decomposition of an N-Regular Biquaternion* treated the case $\langle\tilde Q\rangle_{\natural}\neq0$, where the factors sharpen: $\tilde Q_H$ is positive definite, $\tilde Q_0$ is unitary, and the pair refines into the four-factor word $\tilde Q=r\zeta\tilde U_{\mathrm b}\tilde u_{\mathrm r}$.

This article treats the complementary case $\langle\tilde Q\rangle_{\natural}=0$. The modulus vanishes, so the modulus–unit form $\tilde Q=\Rho\tilde U$ with $\Rho\neq0$ does not exist, and neither does the four-factor word, whose product has norm $\Rho^{2}=0$ and cannot represent a nonzero element. What survives is the two-factor decomposition: $\tilde Q_H$ is positive semidefinite of rank at most one, and $\tilde Q_0$ is a partial isometry that is not unitary.

The article states why the modulus and the four factors fail (§*The Vanishing of the Modulus*), records the surviving pair (§*The Two-Factor Decomposition*), computes the two factors in closed form (§*The Hermitian Factor*, §*The Partial-Isometry Factor*), describes the two sectors of the null cone (§*The Two Sectors*), and gives four worked examples. The general pair, its uniqueness and the continuity of its Hermitian factor are established in *The Polar Decomposition of a Biquaternion* and are cited, not proved again.

The conventions and the symbols are those of *Conventions in Mathematics*, *N-Regularity and Degeneracy in the Biquaternion Algebra* and *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the symbols are collected in §*Summary of Notation*. The product is the plain product and the conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$.

## The Vanishing of the Modulus

Let $\tilde Q$ be N-degenerate, $\langle\tilde Q\rangle_{\natural}=0$. The modulus of the N-regular article is a square root of the norm,

$$
\Rho^{2}=\langle\tilde Q\rangle_{\natural}=0,
$$

so $\Rho=0$. The modulus–unit decomposition requires $\Rho\neq0$, since it divides by the modulus; at $\Rho=0$ the unit factor $\tilde Q/\Rho$ is undefined.

The four-factor word fails for the same reason, and the failure is visible in the norm. Its factors are constrained by

$$
r=\lvert\Rho\rvert>0,\qquad \lvert\zeta\rvert=1,\qquad \langle\tilde U_{\mathrm b}\rangle_{\natural}=1,\qquad \langle\tilde u_{\mathrm r}\rangle_{\natural}=1,
$$

and the norm is multiplicative, so

$$
\bigl\langle r\zeta\tilde U_{\mathrm b}\tilde u_{\mathrm r}\bigr\rangle_{\natural}=r^{2}\zeta^{2}\langle\tilde U_{\mathrm b}\rangle_{\natural}\langle\tilde u_{\mathrm r}\rangle_{\natural}=\Rho^{2}=0 .
$$

A product of norm zero cannot equal a nonzero element. At the origin the failure is stronger: $\Rho=0$ forces $r=0$, which contradicts $r>0$.

The modulus–unit form and the four-factor word therefore exist exactly on the N-regular elements. The N-degenerate elements are the null cone

$$
\mathcal N=\{\tilde Q:\langle\tilde Q\rangle_{\natural}=0\},
$$

one complex equation, hence two real equations, of real codimension two (*N-Regularity and Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*).

## The Two-Factor Decomposition

The general pair survives on the null cone. Every N-degenerate element is

$$
\boxed{\;\tilde Q=\tilde Q_H\,\tilde Q_0,\qquad \tilde Q_H=\bigl(\tilde Q\tilde Q^{*}\bigr)^{1/2},\quad \tilde Q_0=\tilde Q_H^{+}\tilde Q,\;}
$$

with ${}^{+}$ the Moore–Penrose inverse. The pair exists for every element of the algebra and is unique (*The Polar Decomposition of a Biquaternion*, §*Uniqueness*); on the null cone it takes the following form.

**Proposition.** If $\langle\tilde Q\rangle_{\natural}=0$, then $\tilde Q_H$ is Hermitian positive semidefinite of rank at most one, $\tilde Q_0$ is a partial isometry, and $\tilde Q_0$ is not unitary for $\tilde Q\neq0$. At the origin both factors vanish.

The rank is one exactly when $\tilde Q\neq0$, and zero at the origin. The partial isometry is not unitary because its final projection $\tilde Q_0\tilde Q_0^{*}=\tilde Q_H/(2a)$ is a rank-one projection, not the identity, for $a>0$. The two factors are functions of $\tilde Q$ alone. The Hermitian factor is the continuous limit of the N-regular Hermitian factor as the element approaches the cone; the isometry factor is not continuous there (*The Polar Decomposition of a Biquaternion*, §*Continuity*).

## The Hermitian Factor

Write the element and its Hermitian square in the coordinates of *The Polar Decomposition of a Biquaternion*, §*Notation*:

$$
\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,\qquad
\tilde Q\tilde Q^{*}=\langle\tilde Q\rangle_{*}e_t+i\vec W,
$$

with $\vec W=W_x\vec e_x+W_y\vec e_y+W_z\vec e_z$ real and

$$
W_x=2\bigl(\operatorname{Im}(Q_x\overline{Q_t})-\operatorname{Im}(Q_y\overline{Q_z})\bigr),\quad
W_y=2\bigl(\operatorname{Im}(Q_y\overline{Q_t})-\operatorname{Im}(Q_z\overline{Q_x})\bigr),\quad
W_z=2\bigl(\operatorname{Im}(Q_z\overline{Q_t})-\operatorname{Im}(Q_x\overline{Q_y})\bigr).
$$

The two identities of that section become, at $\langle\tilde Q\rangle_{\natural}=0$,

$$
\bigl\langle\tilde Q\tilde Q^{*}\bigr\rangle_{\natural}=\langle\tilde Q\rangle_{*}^{2}-\lvert\vec W\rvert^{2}=\bigl\lvert\langle\tilde Q\rangle_{\natural}\bigr\rvert^{2}=0,
$$

so

$$
\lvert\vec W\rvert=\langle\tilde Q\rangle_{*},\qquad
a=\sqrt{\frac{\langle\tilde Q\rangle_{*}}{2}},\qquad
\lvert\vec W\rvert=2a^{2}.
$$

The number $a$ is real and non-negative, and $a=0$ exactly when $\tilde Q=0$.

**Theorem.** For $\tilde Q\neq0$ on the null cone,

$$
\boxed{\;\tilde Q_H=a\,e_t+\frac{i}{2a}\,\vec W\;},\qquad a=\sqrt{\frac{\langle\tilde Q\rangle_{*}}{2}},
$$

and $\tilde Q_H=0$ at the origin.

*Proof.* The element is Hermitian, since $a$ is real and $i\vec W$ is Hermitian. Squaring and using $\vec W^{2}=-\lvert\vec W\rvert^{2}e_t$,

$$
\tilde Q_H^{2}=\Bigl(a^{2}+\frac{\lvert\vec W\rvert^{2}}{4a^{2}}\Bigr)e_t+i\vec W
=2a^{2}e_t+i\vec W
=\langle\tilde Q\rangle_{*}e_t+i\vec W
=\tilde Q\tilde Q^{*},
$$

the third equality by $\lvert\vec W\rvert=2a^{2}$. The spectral values of $\tilde Q_H$ are $a\pm\lvert\vec W\rvert/(2a)=a\pm a$, that is, $0$ and $2a$, so the element is positive semidefinite of rank one. It is the unique square root of $\tilde Q\tilde Q^{*}$ in the cone, by the uniqueness of that root. $\square$

The scalar part of $\tilde Q_H$ is $a$, and its vector part is purely imaginary of length $\lvert\vec W\rvert/(2a)=a$. The factor is the sum of the central element $a e_t$ and a vector part of the same length; its two spectral values are $0$ and $2a$.

## The Partial-Isometry Factor

The Moore–Penrose inverse of the Hermitian factor follows from the quadratic identity it satisfies. Since $\tilde Q_H^{2}=2a\tilde Q_H$ and $a>0$,

$$
\tilde Q_H^{3}=4a^{2}\tilde Q_H,
\qquad
\tilde Q_H^{+}=\frac{\tilde Q_H}{4a^{2}} .
$$

The four Penrose conditions are checked by direct multiplication, as in *The Polar Decomposition of a Biquaternion*, §*The Moore–Penrose Inverse of the Hermitian Factor*. At the origin the inverse is $0$.

**Theorem.** For $\tilde Q\neq0$ on the null cone the isometry factor is

$$
\boxed{\;\tilde Q_0=\tilde Q_H^{+}\tilde Q=\frac{\tilde Q_H\,\tilde Q}{4a^{2}}\;}
$$

and it is a partial isometry of rank one:

$$
\tilde Q_0\tilde Q_0^{*}\tilde Q_0=\tilde Q_0,\qquad
\tilde Q_0^{*}\tilde Q_0\tilde Q_0^{*}=\tilde Q_0^{*},\qquad
\tilde Q_0\tilde Q_0^{*}=\frac{\tilde Q_H}{2a}.
$$

*Proof.* The product $\tilde Q_0\tilde Q_0^{*}$ is

$$
\tilde Q_H^{+}\tilde Q\tilde Q^{*}\tilde Q_H^{+}=\tilde Q_H^{+}\tilde Q_H^{2}\tilde Q_H^{+}=\tilde Q_H\tilde Q_H^{+}=\frac{\tilde Q_H}{2a},
$$

using $\tilde Q_H\tilde Q_H^{+}=\tilde Q_H/(2a)$, which is the final projection of the Hermitian factor. This product is a rank-one projection, so the first Penrose identity gives $\tilde Q_0\tilde Q_0^{*}\tilde Q_0=\tilde Q_0$, and the second follows symmetrically. $\square$

The factor $\tilde Q_0$ is not unitary: its product with its conjugate is the rank-one projection $\tilde Q_H/(2a)$, not $e_t$. At the origin, $\tilde Q_H=0$, $\tilde Q_H^{+}=0$ and $\tilde Q_0=0$.

## The Two Sectors

The null cone splits into the two sectors of the spectral problem, $\Sigma_{01}$ and $\Sigma_{00}$.

### The sector $\Sigma_{01}$

$$
\Sigma_{01}=\{\langle\tilde Q\rangle_{\natural}=0,\ B^{2}\neq0\},\qquad B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}.
$$

It is *The N-Degenerate, Spectrally Regular Sector*. The characteristic polynomial is $X^{2}-2Q_tX$, with the two distinct roots $0$ and $2Q_t\neq0$, and the element has the spectral decomposition $\tilde Q=c\,\tilde\Pi$ with $c\neq0$ and $\tilde\Pi$ an idempotent different from $0$ and $e_t$. The idempotent need not be Hermitian. The Hermitian factor is positive semidefinite of rank one, the isometry factor is a partial isometry of rank one, and both are computed by the formulas above.

### The sector $\Sigma_{00}$

$$
\Sigma_{00}=\{\langle\tilde Q\rangle_{\natural}=0,\ B^{2}=0\}.
$$

It is *The N-Degenerate, Spectrally Degenerate Sector*. The two conditions give $Q_t=0$ and $Q_x^{2}+Q_y^{2}+Q_z^{2}=0$, so the element is pure and square-zero:

$$
\tilde Q=\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,\qquad \tilde Q^{2}=0 .
$$

The sector splits into the origin, where $\tilde Q_H=0$ and $\tilde Q_0=0$, and the nonzero nilpotents, where $\tilde Q_H$ has rank one and $\tilde Q_0$ is a partial isometry of rank one. The nonzero nilpotents are the pure elements of the nilpotent cone (*Square Roots of Zero and the Nilpotents of the Biquaternion Algebra*).

The two sectors are disjoint. The origin lies in $\Sigma_{00}$, and it is the only element at which $a=0$. On both sectors the two-factor decomposition exists, and on neither does the four-factor word exist.

## Examples

### Example 1: the sector $\Sigma_{01}$

$$
\tilde Q=e_t+i\vec e_x .
$$

The norm is $\langle\tilde Q\rangle_{\natural}=1+i^{2}=0$, the Hermitian norm is $\langle\tilde Q\rangle_{*}=2$, so $a=1$, and $\vec W=2\vec e_x$. Then

$$
\tilde Q_H=e_t+i\vec e_x,\qquad
\tilde Q_H^{+}=\frac{e_t+i\vec e_x}{4},\qquad
\tilde Q_0=\frac{e_t+i\vec e_x}{2}.
$$

The decomposition reads

$$
e_t+i\vec e_x=\bigl(e_t+i\vec e_x\bigr)\cdot\frac{e_t+i\vec e_x}{2}.
$$

The factor $\tilde Q_0$ is a projection, hence a partial isometry, but not unitary: $\tilde Q_0\tilde Q_0^{*}=\tilde Q_0$ is a rank-one projection, not the identity.

### Example 2: the sector $\Sigma_{01}$

$$
\tilde Q=e_t+\vec e_x+i\vec e_y+i\vec e_z .
$$

The norm is $\langle\tilde Q\rangle_{\natural}=1+1+i^{2}+i^{2}=0$, the Hermitian norm is $4$, so $a=\sqrt2$, and $\vec W=4\vec e_z$. Then

$$
\tilde Q_H=\sqrt2\,e_t+i\sqrt2\,\vec e_z,\qquad
\tilde Q_0=\frac{\tilde Q}{2\sqrt2}.
$$

The decomposition reads

$$
e_t+\vec e_x+i\vec e_y+i\vec e_z
=\bigl(\sqrt2\,e_t+i\sqrt2\,\vec e_z\bigr)\cdot\frac{\tilde Q}{2\sqrt2}.
$$

The factor $\tilde Q_0$ is a partial isometry of rank one, not unitary.

### Example 3: the sector $\Sigma_{00}$, a nonzero nilpotent

$$
\tilde Q=\vec e_x+i\vec e_y .
$$

The norm is $\langle\tilde Q\rangle_{\natural}=1+i^{2}=0$, and $B^{2}=1+i^{2}=0$, so $\tilde Q^{2}=0$. The Hermitian norm is $2$, so $a=1$, and $\vec W=2\vec e_z$. Then

$$
\tilde Q_H=e_t+i\vec e_z,\qquad
\tilde Q_H^{+}=\frac{e_t+i\vec e_z}{4},\qquad
\tilde Q_0=\frac{\vec e_x+i\vec e_y}{2}.
$$

The decomposition reads

$$
\vec e_x+i\vec e_y=\bigl(e_t+i\vec e_z\bigr)\cdot\frac{\vec e_x+i\vec e_y}{2}.
$$

The Hermitian factor has rank one, and the isometry factor is a partial isometry of rank one, not unitary.

### Example 4: the origin

$$
\tilde Q=0 .
$$

Then $\langle\tilde Q\rangle_{\natural}=0$, $B^{2}=0$, and

$$
\tilde Q_H=0,\qquad \tilde Q_H^{+}=0,\qquad \tilde Q_0=0 .
$$

The decomposition reads $0=0\cdot0$.

## Summary

On the null cone the modulus–unit form and the four-factor word do not exist: the modulus vanishes, and the norm of the four-factor product is $\Rho^{2}=0$, so it cannot represent a nonzero element. The general pair survives.

| item | result |
|---|---|
| domain | $\langle\tilde Q\rangle_{\natural}=0$ |
| decomposition | $\tilde Q=\tilde Q_H\tilde Q_0$ |
| Hermitian factor | $\tilde Q_H=a e_t+i\vec W/(2a)$, $a=\sqrt{\langle\tilde Q\rangle_{*}/2}$ ($a>0$) |
| Hermitian square | $\tilde Q\tilde Q^{*}=\langle\tilde Q\rangle_{*}e_t+i\vec W$, $\lvert\vec W\rvert=2a^{2}$ |
| spectral values | $0$ and $2a$; rank one, or zero at the origin |
| inverse | $\tilde Q_H^{+}=\tilde Q_H/(4a^{2})$, or $0$ at the origin |
| isometry factor | $\tilde Q_0=\tilde Q_H\tilde Q/(4a^{2})$, a partial isometry of rank one |
| projections | $\tilde Q_0\tilde Q_0^{*}=\tilde Q_H/(2a)$ |
| sectors | $\Sigma_{01}$ ($B^{2}\neq0$) and $\Sigma_{00}$ ($B^{2}=0$), the latter split into the origin and the nilpotents |

The factorization exists for every element of the null cone, including the origin. The four-factor refinement is the privilege of the N-regular elements, where the modulus is nonzero.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q$ | an N-degenerate biquaternion |
| $N=\langle\tilde Q\rangle_{\natural}$ | the quaternionic norm, zero on the null cone |
| $\langle\tilde Q\rangle_{*}$ | the Hermitian norm, $\sum_\mu\lvert Q_\mu\rvert^{2}$ |
| $\tilde Q\tilde Q^{*}$ | $\langle\tilde Q\rangle_{*}e_t+i\vec W$ |
| $\vec W$ | $W_x\vec e_x+W_y\vec e_y+W_z\vec e_z$, real |
| $a$ | $\sqrt{\langle\tilde Q\rangle_{*}/2}$, the scalar part of $\tilde Q_H$ |
| $\tilde Q_H$ | $a e_t+i\vec W/(2a)$, rank one |
| $\tilde Q_H^{+}$ | $\tilde Q_H/(4a^{2})$, the Moore–Penrose inverse |
| $\tilde Q_0$ | $\tilde Q_H^{+}\tilde Q$, the partial isometry |
| $B^{2}$ | $Q_x^{2}+Q_y^{2}+Q_z^{2}$ |
| $\Sigma_{01}$ | $\{N=0,\ B^{2}\neq0\}$ |
| $\Sigma_{00}$ | $\{N=0,\ B^{2}=0\}$ |

## Further Reading

- Roger Penrose, "A generalized inverse for matrices", *Proceedings of the Cambridge Philosophical Society* **51** (1955) 406–413. The four equations and the generalized inverse.
- Gene H. Golub and Charles F. Van Loan, *Matrix Computations*, 4th edition (Johns Hopkins University Press, 2013). The singular value decomposition, the Moore–Penrose inverse and the rank-one limits.
- Nicholas J. Higham, *Functions of Matrices: Theory and Computation* (SIAM, 2008). The matrix square root and the polar factor at a rank drop.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998). Algebras with involution, the Hermitian cone and the partial isometries of a rank-one factor.
