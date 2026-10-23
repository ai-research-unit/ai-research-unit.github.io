
# __Worked Examples in the Split-Quaternion Algebra__

## Introduction

This article collects explicit computations in the split-quaternion algebra $\mathbb{H}_{\mathrm{s}}$, in the order in which the theory is built: the basis products; the three involutions and their eigenspaces; the idempotents and the two minimal left ideals; explicit pairs of zero divisors; and the unit criterion. Every number below is computed from the multiplication table of *Split-Quaternion Algebra*.

The article is a companion to the structural articles of the category. Its purpose is to put the abstract statements on concrete elements, so that the reader can carry each of them back to a computation. It introduces no new result; the statements it illustrates are those of *Split-Quaternion Algebra*, *Split-Quaternion Idempotents and Projections*, *Split-Quaternion Zero Divisors*, *Split-Quaternion Norm and Invertibility* and *Split-Quaternion Rotations and the Lorentz Group*.

## The Basis Products

The multiplication table, whose entry in row $\mu$ and column $\nu$ is $e_\mu e_\nu$, is

| | $1$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $1$ | $1$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $-1$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $\vec e_y$ | $-\vec e_z$ | $+1$ | $-\vec e_x$ |
| $\vec e_z$ | $\vec e_z$ | $\vec e_y$ | $\vec e_x$ | $+1$ |

**Example (a product worked in full).** The entry $\vec e_z^2 = +1$ follows from $\vec e_z = \vec e_x \vec e_y$ and anticommutativity:

$$
\vec e_z^2 = \vec e_x \vec e_y \vec e_x \vec e_y = -\vec e_x^2 \vec e_y^2 = -(-1)(+1) = +1 .
$$

The product of two general elements, worked from the table, is

$$
(q_{1t} e_t + q_{1x} \vec e_x + q_{1y} \vec e_y + q_{1z} \vec e_z)(q_{2t} e_t + q_{2x} \vec e_x + q_{2y} \vec e_y + q_{2z} \vec e_z)
= (q_{1t} q_{2t} - q_{1x} q_{2x} + q_{1y} q_{2y} + q_{1z} q_{2z}) + (q_{1t} q_{2x} + q_{2t} q_{1x} - q_{1y} q_{2z} + q_{2y} q_{1z})\vec e_x
+ (q_{1t} q_{2y} + q_{2t} q_{1y} + q_{1x} q_{2z} - q_{2x} q_{1z})\vec e_y + (q_{1t} q_{2z} + q_{2t} q_{1z} + q_{1x} q_{2y} - q_{2x} q_{1y})\vec e_z .
$$

The product is associative and distributive, so the multiplication table of the four basis elements determines it completely; the table is collected in the summary. The products of the vector basis elements are

$$
\boxed{\;
\vec e_x^2 = -1, \quad \vec e_y^2 = 1, \quad \vec e_z^2 = 1, \qquad
\vec e_x \vec e_y = \vec e_z, \quad \vec e_y \vec e_x = -\vec e_z, \qquad
\vec e_x \vec e_z = -\vec e_y, \quad \vec e_z \vec e_x = \vec e_y, \qquad
\vec e_y \vec e_z = -\vec e_x, \quad \vec e_z \vec e_y = \vec e_x
\;}
$$.

**Example.** For $\tilde q = 2 + \vec e_x$ and $\tilde p = 1 + \vec e_y + \vec e_z$, the table gives

$$
(2 + \vec e_x)(1 + \vec e_y + \vec e_z) = 2 + 2\vec e_y + 2\vec e_z + \vec e_x + \vec e_x \vec e_y + \vec e_x \vec e_z = 2 + \vec e_x + 2\vec e_y + 2\vec e_z - \vec e_y + \vec e_z = 2 + \vec e_x + \vec e_y + 3\vec e_z ,
$$

so the product is $\tilde q \tilde p = 2 + \vec e_x + \vec e_y + 3\vec e_z$; the coefficient of $\vec e_x$ also follows from the general product formula displayed above.

## The Three Involutions and Their Eigenspaces

Three involutions act on the algebra. The **conjugation** ${}^{\natural}$ negates the vector part, the **principal involution** $\alpha$ is the automorphism

$$
\alpha(\vec e_x) = -\vec e_x, \qquad \alpha(\vec e_y) = -\vec e_y, \qquad \alpha(\vec e_z) = \vec e_z,
$$

and the **reversal** $\rho$ is the anti-automorphism

$$
\rho(\vec e_x) = \vec e_x, \qquad \rho(\vec e_y) = \vec e_y, \qquad \rho(\vec e_z) = -\vec e_z .
$$

On a general element they read

$$
\tilde{q}^{\natural} = q_t e_t - q_x \vec e_x - q_y \vec e_y - q_z \vec e_z, \qquad
\alpha(\tilde q) = q_t - q_x \vec e_x - q_y \vec e_y + q_z \vec e_z, \qquad
\rho(\tilde q) = q_t + q_x \vec e_x + q_y \vec e_y - q_z \vec e_z,
$$

and the three are related by $\tilde{q}^{\natural} = \alpha(\rho(\tilde q)) = \rho(\alpha(\tilde q))$.

**Example (eigenspaces).** Each involution is diagonalisable with eigenvalues $\pm 1$.

| involution | $+1$ eigenspace | $-1$ eigenspace | dimensions |
|---|---|---|---|
| ${}^{\natural}$ | $S = \mathbb{R}\cdot 1$ | $V = \operatorname{span}\{\vec e_x,\vec e_y,\vec e_z\}$ | $1, 3$ |
| $\alpha$ | $\operatorname{span}\{1, \vec e_z\}$ | $\operatorname{span}\{\vec e_x, \vec e_y\}$ | $2, 2$ |
| $\rho$ | $\operatorname{span}\{1, \vec e_x, \vec e_y\}$ | $\mathbb{R} \vec e_z$ | $3, 1$ |

**Example (the common eigenspaces).** Since $\alpha$ and $\rho$ commute, they are simultaneously diagonalisable, and the common eigenspaces of the pair $(\alpha, \rho)$ are

$$
\mathbb{H}_{\mathrm{s}} = \mathbb{R}\cdot 1 \oplus \operatorname{span}\{\vec e_x, \vec e_y\} \oplus \mathbb{R} \vec e_z,
$$

on which the sign pair $(\alpha, \rho)$ is $(+,+)$, $(-,+)$ and $(+,-)$ respectively. The plane $\operatorname{span}\{\vec e_x,\vec e_y\}$ is not split further: on it the conjugation also acts as $-1$, so no eigenspace of any of the three involutions cuts it. This is the finest decomposition produced by the involutions, and it is recorded in *Split-Quaternion Subspaces and the Involutions*.

## The Idempotents and the Two Minimal Left Ideals

**Example (the standard idempotents).** With $\tilde\pi_1 = \tfrac{1}{2}(1 + \vec e_y)$ and $\tilde\pi_2 = \tfrac{1}{2}(1 - \vec e_y)$,

$$
\tilde\pi_1^2 = \tfrac{1}{4}(1 + 2\vec e_y + \vec e_y^2) = \tfrac{1}{4}(2 + 2\vec e_y) = \tilde\pi_1,
$$

and $\tilde\pi_2^2 = \tilde\pi_2$ likewise. Moreover

$$
\boxed{\;
\tilde\pi_1 \tilde\pi_2 = \tfrac{1}{4}(1 - \vec e_y^2) = 0, \qquad \tilde\pi_1 + \tilde\pi_2 = 1, \qquad \langle\tilde\pi_1\rangle_{\natural} = \langle\tilde\pi_2\rangle_{\natural} = 0
\;}
$$.

They are not central, since $\vec e_x \tilde\pi_1 = \tfrac{1}{2}(\vec e_x + \vec e_z)$ while $\tilde\pi_1 \vec e_x = \tfrac{1}{2}(\vec e_x - \vec e_z)$.

**Example (the two minimal left ideals).** The reductions $\vec e_y \tilde\pi_1 = \tilde\pi_1$ and $\vec e_z \tilde\pi_1 = \tfrac{1}{2}(\vec e_z + \vec e_x) = \vec e_x \tilde\pi_1$ give

$$
\mathbb{H}_{\mathrm{s}} \tilde\pi_1 = \operatorname{span}\{\tilde\pi_1, \vec e_x \tilde\pi_1\} = \operatorname{span}\big\{\tfrac{1}{2}(1 + \vec e_y),\, \tfrac{1}{2}(\vec e_x + \vec e_z)\big\},
$$

$$
\mathbb{H}_{\mathrm{s}} \tilde\pi_2 = \operatorname{span}\{\tilde\pi_2, \vec e_x \tilde\pi_2\} = \operatorname{span}\big\{\tfrac{1}{2}(1 - \vec e_y),\, \tfrac{1}{2}(\vec e_x - \vec e_z)\big\},
$$

each of real dimension $2$, with $\mathbb{H}_{\mathrm{s}} = \mathbb{H}_{\mathrm{s}} \tilde\pi_1 \oplus \mathbb{H}_{\mathrm{s}} \tilde\pi_2$. The four spanning elements are the vectors $\tilde\pi_1$, $\tilde p = \tfrac{1}{2}(\vec e_x+\vec e_z)$, $\tilde\pi_2$, $-\tilde q = \tfrac{1}{2}(\vec e_x-\vec e_z)$ of the matrix-unit basis $\{\tilde\pi_1, \tilde q, \tilde p, \tilde\pi_2\}$ of *Split-Quaternion Ideals and Peirce Decomposition*.

**Example (the split-complex subalgebra).** The idempotents lie in the subalgebra $\operatorname{span}\{1, \vec e_y\} \cong \mathbb{D}$, and in that commutative algebra they are central; in $\mathbb{H}_{\mathrm{s}}$ they are not, and the decomposition they give is a decomposition of modules and not of algebras, because $\tilde\pi_1 \vec e_z \tilde\pi_2 = \tfrac{1}{2}(\vec e_z - \vec e_x) \neq 0$.

## Explicit Zero-Divisor Pairs

**Example (two split-complex pairs).** Let $\lambda, \mu$ be real. Then

$$
(1 + \vec e_y)(1 - \vec e_y) = 1 - \vec e_y^2 = 0, \qquad (1 + \vec e_z)(1 - \vec e_z) = 1 - \vec e_z^2 = 0,
$$

so $(1+\vec e_y)$ with $(1-\vec e_y)$, and $(1+\vec e_z)$ with $(1-\vec e_z)$, are explicit pairs of nonzero zero divisors.

**Example (a nilpotent pair).** The element $\vec e_x + \vec e_z$ is nonzero and

$$
(\vec e_x + \vec e_z)^2 = \vec e_x^2 + \vec e_x \vec e_z + \vec e_z \vec e_x + \vec e_z^2 = -1 + (-\vec e_y) + \vec e_y + 1 = 0,
$$

so $\vec e_x + \vec e_z$ is a nonzero nilpotent and the pair $(\vec e_x+\vec e_z, \vec e_x+\vec e_z)$ is a zero-divisor pair.

Every nilpotent lies in the vector subspace $V$ and on the level set $N = 0$, $q_x^2 = q_y^2 + q_z^2$; the element $1 + \vec e_y$ shows that the zero divisor set is strictly larger than the nilpotent set, since $(1+\vec e_y)^2 = 2(1+\vec e_y) \neq 0$.

**Example (a mixed pair).** The idempotent $\tilde\pi_2$ annihilates $1 + \vec e_y$:

$$
(1 + \vec e_y) \tilde\pi_2 = 2 \tilde\pi_1 \tilde\pi_2 = 0,
$$

a pair in which neither factor is a nilpotent.

## The Unit Criterion Worked

**Criterion (from *Split-Quaternion Norm and Invertibility*).** A nonzero $\tilde q$ is invertible if and only if $\langle\tilde q\rangle_{\natural} \neq 0$, and then $\tilde q^{-1} = \tilde{q}^{\natural}/\langle\tilde q\rangle_{\natural}$. It is recalled here only to be applied.

**Example (a unit of positive norm).** For $\tilde q = 2 + \vec e_x$, the split-quaternion norm is $\langle\tilde q\rangle_{\natural} = 4 + 1 = 5$, and

$$
\boxed{\;
\tilde q^{-1} = \frac{\tilde{q}^{\natural}}{\langle\tilde q\rangle_{\natural}} = \frac{2 - \vec e_x}{5}, \qquad
(2 + \vec e_x)\frac{2 - \vec e_x}{5} = \frac{4 - \vec e_x^2}{5} = \frac{5}{5} = 1
\;}
$$.

**Example (a unit of norm one).** For $\tilde p = 1 + \vec e_x + \vec e_y$, the split-quaternion norm is $\langle\tilde p\rangle_{\natural} = 1 + 1 - 1 = 1$, so $\tilde p^{-1} = \tilde p^{\natural} = 1 - \vec e_x - \vec e_y$; indeed $\tilde p \tilde p^{\natural} = (1+\vec e_x+\vec e_y)(1-\vec e_x-\vec e_y) = 1$. Since $\langle\tilde p\rangle_{\natural} = 1$, the element is a unit split-quaternion.

**Example (a unit of negative norm).** For $\tilde q_1 = \vec e_y$, the split-quaternion norm is $\langle\tilde q_1\rangle_{\natural} = -1$, and $\tilde q_1^{-1} = \bar{\tilde q_1}/\langle\tilde q_1\rangle_{\natural} = (-\vec e_y)/(-1) = \vec e_y$, consistent with $\vec e_y^2 = 1$. 

**Example (a non-unit).** For $w = 1 + \vec e_z$, the split-quaternion norm is $\langle w\rangle_{\natural} = 1 - 1 = 0$, so $w$ is not invertible; and indeed $(1+\vec e_z)(1-\vec e_z) = 0$. 

The four examples realise the three-way classification of *Split-Quaternion Norm and Invertibility* by the value of $\langle\cdot\rangle_{\natural}$: a positive value ($N = 5$ and $N = 1$), a negative value ($N = -1$), and the value zero ($N = 0$, the zero divisors).

## The Action of the Unit Group

The action of a unit on the vector subspace by conjugation, the elliptic and hyperbolic one-parameter subgroups it produces, and the classification of the vectors of $V$ by their orbits, use the multiplication table above and nothing else; they are computations of the Geometry group and are carried out in *Split-Quaternion Rotations and the Lorentz Group*. They are not repeated here, and the multiplication table of §*The Basis Products* is what they consume.

## Summary

The basis products are collected in one table, and the multiplication table determines the algebra. The three involutions — conjugation, the principal involution $\alpha$ and the reversal $\rho$ — are diagonalisable; their individual eigenspaces and their common refinement $\mathbb{R}\cdot 1 \oplus \operatorname{span}\{\vec e_x,\vec e_y\} \oplus \mathbb{R} \vec e_z$ are listed, and the plane $\operatorname{span}\{\vec e_x,\vec e_y\}$ does not split further.

The idempotents $\tilde\pi_{1,2}$ are verified to be orthogonal, complete and of zero norm, and they give the two minimal left ideals $\mathbb{H}_{\mathrm{s}} \tilde\pi_{1,2} = \operatorname{span}\{\tilde\pi_{1,2}, \vec e_x \tilde\pi_{1,2}\}$. Explicit zero-divisor pairs are $(1+\vec e_y)(1-\vec e_y) = 0$, $(1+\vec e_z)(1-\vec e_z) = 0$, the nilpotent $(\vec e_x+\vec e_z)^2 = 0$, and the mixed pair $(1+\vec e_y)\tilde\pi_2 = 0$. The unit criterion is carried through on four elements: $2+\vec e_x$ (positive norm), $1+\vec e_x+\vec e_y$ (norm one), $\vec e_y$ (negative norm), and the non-unit $1+\vec e_z$ (zero norm). The action of the unit group on the vector subspace is not worked here; it is the subject of *Split-Quaternion Rotations and the Lorentz Group*.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra | *Split-Quaternion Algebra* |
| $\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$ | a general split-quaternion | *Split-Quaternion Algebra* |
| ${}^{\natural}$, $\alpha$, $\rho$ | conjugation, principal involution, reversal | *Split-Quaternion Algebra* |
| $\tilde\pi_{1,2} = \tfrac{1}{2}(1\pm \vec e_y)$ | the standard idempotents | *Split-Quaternion Idempotents and Projections* |
| $\mathbb{H}_{\mathrm{s}} \tilde\pi_{1,2}$ | the two minimal left ideals | *Split-Quaternion Idempotents and Projections* |
| $\langle\tilde q\rangle_{\natural} = \tilde q\tilde{q}^{\natural} = q_t^2+q_x^2-q_y^2-q_z^2$ | the central product, formed and evaluated algebraically | *Split-Quaternion Algebra* |
| $\tilde q^{-1} = \tilde{q}^{\natural}/\langle\tilde q\rangle_{\natural}$ | the inverse of a unit | *Split-Quaternion Norm and Invertibility* |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for worked computations with the coquaternions and their matrix models.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the explicit idempotents, zero divisors and split forms.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the action of $\mathrm{SL}_2(\mathbb{R})$ on the $(2,1)$-form and the Lorentz group.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the isotropic forms and the geometry of their null cones.
