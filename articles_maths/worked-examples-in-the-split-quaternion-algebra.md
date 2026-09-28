
# __Worked Examples in the Split-Quaternion Algebra__

## Introduction

This article collects explicit computations in the split-quaternion algebra $\mathbb{H}_{\mathrm{s}}$, in the order in which the theory is built: the basis products; the three involutions and their eigenspaces; the idempotents and the two minimal left ideals; explicit pairs of zero divisors; and the unit criterion. Every number below is computed from the multiplication table of *Split-Quaternion Algebra*.

The article is a companion to the structural articles of the category. Its purpose is to put the abstract statements on concrete elements, so that the reader can carry each of them back to a computation. It introduces no new result; the statements it illustrates are those of *Split-Quaternion Algebra*, *Split-Quaternion Idempotents and Projections*, *Split-Quaternion Zero Divisors*, *Split-Quaternion Norm and Invertibility* and *Split-Quaternion Rotations and the Lorentz Group*.

**Conventions.** A split-quaternion is $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$, with $q_0, q_1, q_2, q_3 \in \mathbb{R}$ and the products $e_1^2 = -1$, $e_2^2 = +1$, $e_3 = e_1 e_2$, $e_1 e_2 = -e_2 e_1$. Its conjugation is $\bar{\tilde q} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$ and its central product is $N(\tilde q) = \tilde q\bar{\tilde q} = q_0^2 + q_1^2 - q_2^2 - q_3^2$, formed and evaluated algebraically and read metrically in *Split-Quaternion Norm and Invertibility*. The elements $\tilde\pi_\pm = \tfrac{1}{2}(1 \pm e_2)$ are the standard idempotents.

## The Basis Products

The multiplication table, whose entry in row $i$ and column $j$ is $e_i e_j$, is

| | $1$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $1$ | $1$ | $e_1$ | $e_2$ | $e_3$ |
| $e_1$ | $e_1$ | $-1$ | $e_3$ | $-e_2$ |
| $e_2$ | $e_2$ | $-e_3$ | $+1$ | $-e_1$ |
| $e_3$ | $e_3$ | $e_2$ | $e_1$ | $+1$ |

**Example (a product worked in full).** The entry $e_3^2 = +1$ follows from $e_3 = e_1 e_2$ and anticommutativity:

$$
e_3^2 = e_1 e_2 e_1 e_2 = -e_1^2 e_2^2 = -(-1)(+1) = +1 .
$$

The product of two general elements, worked from the table, is

$$
(q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3)(q_0' e_0 + q_1' e_1 + q_2' e_2 + q_3' e_3)
= (q_0 q_0' - q_1 q_1' + q_2 q_2' + q_3 q_3') + (q_0 q_1' + q_0' q_1 - q_2 q_3' + q_2' q_3)e_1
+ (q_0 q_2' + q_0' q_2 + q_1 q_3' - q_1' q_3)e_2 + (q_0 q_3' + q_0' q_3 + q_1 q_2' - q_1' q_2)e_3 .
$$

The product is associative and distributive, so the multiplication table of the four basis elements determines it completely; the table is collected in the summary. The products of the vector basis elements are

$$
e_1^2 = -1, \quad e_2^2 = 1, \quad e_3^2 = 1, \qquad
e_1e_2 = e_3, \quad e_2e_1 = -e_3, \qquad
e_1e_3 = -e_2, \quad e_3e_1 = e_2, \qquad
e_2e_3 = -e_1, \quad e_3e_2 = e_1 .
$$

**Example.** For $\tilde q = 2 + e_1$ and $y = 1 + e_2 + e_3$, the table gives

$$
(2 + e_1)(1 + e_2 + e_3) = 2 + 2e_2 + 2e_3 + e_1 + e_1e_2 + e_1e_3 = 2 + e_1 + 2e_2 + 2e_3 - e_2 + e_3 = 2 + e_1 + e_2 + 3e_3 ,
$$

so the product is $\tilde q y = 2 + e_1 + e_2 + 3e_3$; the coefficient of $e_1$ also follows from the general product formula displayed above.

## The Three Involutions and Their Eigenspaces

Three involutions act on the algebra. The **conjugation** $\bar{\cdot}$ negates the vector part, the **principal involution** $\alpha$ is the automorphism

$$
\alpha(e_1) = -e_1, \qquad \alpha(e_2) = -e_2, \qquad \alpha(e_3) = e_3,
$$

and the **reversal** $\rho$ is the anti-automorphism

$$
\rho(e_1) = e_1, \qquad \rho(e_2) = e_2, \qquad \rho(e_3) = -e_3 .
$$

On a general element they read

$$
\bar{\tilde q} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3, \qquad
\alpha(\tilde q) = q_0 - q_1 e_1 - q_2 e_2 + q_3 e_3, \qquad
\rho(\tilde q) = q_0 + q_1 e_1 + q_2 e_2 - q_3 e_3,
$$

and the three are related by $\bar{\tilde q} = \alpha(\rho(\tilde q)) = \rho(\alpha(\tilde q))$.

**Example (eigenspaces).** Each involution is diagonalisable with eigenvalues $\pm 1$.

| involution | $+1$ eigenspace | $-1$ eigenspace | dimensions |
|---|---|---|---|
| $\bar{\cdot}$ | $S = \mathbb{R}\cdot 1$ | $V = \operatorname{span}\{e_1,e_2,e_3\}$ | $1, 3$ |
| $\alpha$ | $\operatorname{span}\{1, e_3\}$ | $\operatorname{span}\{e_1, e_2\}$ | $2, 2$ |
| $\rho$ | $\operatorname{span}\{1, e_1, e_2\}$ | $\mathbb{R} e_3$ | $3, 1$ |

**Example (the common eigenspaces).** Since $\alpha$ and $\rho$ commute, they are simultaneously diagonalisable, and the common eigenspaces of the pair $(\alpha, \rho)$ are

$$
\mathbb{H}_{\mathrm{s}} = \mathbb{R}\cdot 1 \oplus \operatorname{span}\{e_1, e_2\} \oplus \mathbb{R} e_3,
$$

on which the sign pair $(\alpha, \rho)$ is $(+,+)$, $(-,+)$ and $(+,-)$ respectively. The plane $\operatorname{span}\{e_1,e_2\}$ is not split further: on it the conjugation also acts as $-1$, so no eigenspace of any of the three involutions cuts it. This is the finest decomposition produced by the involutions, and it is recorded in *Split-Quaternion Subspaces and the Involutions*.

## The Idempotents and the Two Minimal Left Ideals

**Example (the standard idempotents).** With $\tilde\pi_+ = \tfrac{1}{2}(1 + e_2)$ and $\tilde\pi_- = \tfrac{1}{2}(1 - e_2)$,

$$
\tilde\pi_+^2 = \tfrac{1}{4}(1 + 2e_2 + e_2^2) = \tfrac{1}{4}(2 + 2e_2) = \tilde\pi_+,
$$

and $\tilde\pi_-^2 = \tilde\pi_-$ likewise. Moreover

$$
\tilde\pi_+ \tilde\pi_- = \tfrac{1}{4}(1 - e_2^2) = 0, \qquad \tilde\pi_+ + \tilde\pi_- = 1, \qquad N(\tilde\pi_+) = N(\tilde\pi_-) = 0 .
$$

They are not central, since $e_1 \tilde\pi_+ = \tfrac{1}{2}(e_1 + e_3)$ while $\tilde\pi_+ e_1 = \tfrac{1}{2}(e_1 - e_3)$.

**Example (the two minimal left ideals).** The reductions $e_2 \tilde\pi_+ = \tilde\pi_+$ and $e_3 \tilde\pi_+ = \tfrac{1}{2}(e_3 + e_1) = e_1 \tilde\pi_+$ give

$$
\mathbb{H}_{\mathrm{s}} \tilde\pi_+ = \operatorname{span}\{\tilde\pi_+, e_1 \tilde\pi_+\} = \operatorname{span}\big\{\tfrac{1}{2}(1 + e_2),\, \tfrac{1}{2}(e_1 + e_3)\big\},
$$

$$
\mathbb{H}_{\mathrm{s}} \tilde\pi_- = \operatorname{span}\{\tilde\pi_-, e_1 \tilde\pi_-\} = \operatorname{span}\big\{\tfrac{1}{2}(1 - e_2),\, \tfrac{1}{2}(e_1 - e_3)\big\},
$$

each of real dimension $2$, with $\mathbb{H}_{\mathrm{s}} = \mathbb{H}_{\mathrm{s}} \tilde\pi_+ \oplus \mathbb{H}_{\mathrm{s}} \tilde\pi_-$. The four spanning elements are the vectors $\tilde\pi_+$, $y = \tfrac{1}{2}(e_1+e_3)$, $\tilde\pi_-$, $-\tilde q = \tfrac{1}{2}(e_1-e_3)$ of the matrix-unit basis $\{\tilde\pi_+, \tilde q, y, \tilde\pi_-\}$ of *Split-Quaternion Ideals and Peirce Decomposition*.

**Example (the split-complex subalgebra).** The idempotents lie in the subalgebra $\operatorname{span}\{1, e_2\} \cong \mathbb{D}$, and in that commutative algebra they are central; in $\mathbb{H}_{\mathrm{s}}$ they are not, and the decomposition they give is a decomposition of modules and not of algebras, because $\tilde\pi_+ e_3 \tilde\pi_- = \tfrac{1}{2}(e_3 - e_1) \neq 0$.

## Explicit Zero-Divisor Pairs

**Example (two split-complex pairs).** Let $\lambda, \mu$ be real. Then

$$
(1 + e_2)(1 - e_2) = 1 - e_2^2 = 0, \qquad (1 + e_3)(1 - e_3) = 1 - e_3^2 = 0,
$$

so $(1+e_2)$ with $(1-e_2)$, and $(1+e_3)$ with $(1-e_3)$, are explicit pairs of nonzero zero divisors.

**Example (a nilpotent pair).** The element $e_1 + e_3$ is nonzero and

$$
(e_1 + e_3)^2 = e_1^2 + e_1 e_3 + e_3 e_1 + e_3^2 = -1 + (-e_2) + e_2 + 1 = 0,
$$

so $e_1 + e_3$ is a nonzero nilpotent and the pair $(e_1+e_3, e_1+e_3)$ is a zero-divisor pair.

Every nilpotent lies in the vector subspace $V$ and on the level set $N = 0$, $q_1^2 = q_2^2 + q_3^2$; the element $1 + e_2$ shows that the zero divisor set is strictly larger than the nilpotent set, since $(1+e_2)^2 = 2(1+e_2) \neq 0$.

**Example (a mixed pair).** The idempotent $\tilde\pi_-$ annihilates $1 + e_2$:

$$
(1 + e_2) \tilde\pi_- = 2 \tilde\pi_+ \tilde\pi_- = 0,
$$

a pair in which neither factor is a nilpotent.

## The Unit Criterion Worked

**Criterion (from *Split-Quaternion Norm and Invertibility*).** A nonzero $\tilde q$ is invertible if and only if $N(\tilde q) \neq 0$, and then $\tilde q^{-1} = \bar{\tilde q}/N(\tilde q)$. It is recalled here only to be applied.

**Example (a unit of positive norm).** For $\tilde q = 2 + e_1$, the split-quaternion norm is $N(\tilde q) = 4 + 1 = 5$, and

$$
\tilde q^{-1} = \frac{\bar{\tilde q}}{N(\tilde q)} = \frac{2 - e_1}{5}, \qquad
(2 + e_1)\frac{2 - e_1}{5} = \frac{4 - e_1^2}{5} = \frac{5}{5} = 1 .
$$

**Example (a unit of norm one).** For $y = 1 + e_1 + e_2$, the split-quaternion norm is $N(y) = 1 + 1 - 1 = 1$, so $y^{-1} = \bar{y} = 1 - e_1 - e_2$; indeed $y\bar{y} = (1+e_1+e_2)(1-e_1-e_2) = 1$. Since $N(y) = 1$, the element is a unit split-quaternion.

**Example (a unit of negative norm).** For $z = e_2$, the split-quaternion norm is $N(z) = -1$, and $z^{-1} = \bar{z}/N(z) = (-e_2)/(-1) = e_2$, consistent with $e_2^2 = 1$. 

**Example (a non-unit).** For $w = 1 + e_3$, the split-quaternion norm is $N(w) = 1 - 1 = 0$, so $w$ is not invertible; and indeed $(1+e_3)(1-e_3) = 0$. 

The four examples realise the three-way classification of *Split-Quaternion Norm and Invertibility* by the value of $N$: a positive value ($N = 5$ and $N = 1$), a negative value ($N = -1$), and the value zero ($N = 0$, the zero divisors).

## The Action of the Unit Group

The action of a unit on the vector subspace by conjugation, the elliptic and hyperbolic one-parameter subgroups it produces, and the classification of the vectors of $V$ by their orbits, use the multiplication table above and nothing else; they are computations of the Geometry group and are carried out in *Split-Quaternion Rotations and the Lorentz Group*. They are not repeated here, and the multiplication table of §*The Basis Products* is what they consume.

## Summary

The basis products are collected in one table, and the multiplication table determines the algebra. The three involutions — conjugation, the principal involution $\alpha$ and the reversal $\rho$ — are diagonalisable; their individual eigenspaces and their common refinement $\mathbb{R}\cdot 1 \oplus \operatorname{span}\{e_1,e_2\} \oplus \mathbb{R} e_3$ are listed, and the plane $\operatorname{span}\{e_1,e_2\}$ does not split further.

The idempotents $\tilde\pi_\pm$ are verified to be orthogonal, complete and of zero norm, and they give the two minimal left ideals $\mathbb{H}_{\mathrm{s}} \tilde\pi_\pm = \operatorname{span}\{\tilde\pi_\pm, e_1 \tilde\pi_\pm\}$. Explicit zero-divisor pairs are $(1+e_2)(1-e_2) = 0$, $(1+e_3)(1-e_3) = 0$, the nilpotent $(e_1+e_3)^2 = 0$, and the mixed pair $(1+e_2)\tilde\pi_- = 0$. The unit criterion is carried through on four elements: $2+e_1$ (positive norm), $1+e_1+e_2$ (norm one), $e_2$ (negative norm), and the non-unit $1+e_3$ (zero norm). The action of the unit group on the vector subspace is not worked here; it is the subject of *Split-Quaternion Rotations and the Lorentz Group*.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra | *Split-Quaternion Algebra* |
| $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ | a general split-quaternion | *Split-Quaternion Algebra* |
| $\bar{\cdot}$, $\alpha$, $\rho$ | conjugation, principal involution, reversal | *Split-Quaternion Algebra* |
| $\tilde\pi_\pm = \tfrac{1}{2}(1\pm e_2)$ | the standard idempotents | *Split-Quaternion Idempotents and Projections* |
| $\mathbb{H}_{\mathrm{s}} \tilde\pi_\pm$ | the two minimal left ideals | *Split-Quaternion Idempotents and Projections* |
| $N(\tilde q) = \tilde q\bar{\tilde q} = q_0^2+q_1^2-q_2^2-q_3^2$ | the central product, formed and evaluated algebraically | *Split-Quaternion Algebra* |
| $\tilde q^{-1} = \bar{\tilde q}/N(\tilde q)$ | the inverse of a unit | *Split-Quaternion Norm and Invertibility* |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for worked computations with the coquaternions and their matrix models.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the explicit idempotents, zero divisors and split forms.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the action of $\mathrm{SL}_2(\mathbb{R})$ on the $(2,1)$-form and the Lorentz group.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the isotropic forms and the geometry of their null cones.
