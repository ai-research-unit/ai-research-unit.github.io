
# __Worked Examples in the Quaternion Algebra__

## Introduction

This article works the constructions of the quaternion algebra on explicit elements. Its purpose is to compute, once and completely, the quantities that the other articles of the family define in general: the three involutions and their fixed-point subspaces, the roots of $-1$, the norm criterion for a unit together with the inverse, the conjugation action on a concrete element. Nothing here is new mathematics; the interest is that each general statement is followed through in coordinates, so that the conventions of the family can be read off a single worked example.

The element worked throughout is

$$
\tilde q = 1 + 2e_1 - e_2 + 3e_3,
$$

with scalar part $q_0 = 1$ and vector part $\mathbf{q} = 2e_1 - e_2 + 3e_3$, chosen so that no coordinate vanishes and no two coordinates coincide. The general theory is from *Quaternion Algebra* (the basis, the multiplication and the three involutions), *Quaternion Norm and Invertibility* (the norm form, the inverse and the unit criterion), *Quaternion Rotations and Reflections* (the conjugation action and the covering of $SO(3)$). A few examples with other elements are given where a single example would be misleading.

Throughout, the basis is $e_0 = 1, e_1, e_2, e_3$ with

$$
e_1^2 = e_2^2 = e_3^2 = e_1e_2e_3 = -e_0, \qquad e_1e_2 = e_3, \quad e_2e_3 = e_1, \quad e_3e_1 = e_2,
$$

and the products in the opposite order are the negatives. A quaternion is $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$, the conjugate is $\bar{\tilde q} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$, and the norm form is $N(\tilde q) = \tilde q\bar{\tilde q}$.

## The Three Involutions

**Definition.** The three **involutions** of the quaternion algebra are the real-linear maps

$$
\bar{\tilde q} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3, \qquad -\bar{\tilde q} = -q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad -\tilde q = -q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3,
$$

called quaternion, vector and total conjugation. Each is an involution: applying it twice returns $\tilde q$.

**Proposition.** The three involutions are $\bar{\cdot}$, $-\bar{\cdot}$ and $-\mathrm{id}$: the second is the negative of the first and the third is the negative of the identity, so the three maps together with the identity form the group $\mathbb{Z}/2\times\mathbb{Z}/2$ of sign changes of the scalar and vector parts.

*Proof.* The first negates the vector part and fixes the scalar part, $q_0-\mathbf{q}$; the second is its negative, $-q_0+\mathbf{q} = -(q_0-\mathbf{q})$, and so negates the scalar part and fixes the vector part; the third negates both, $-q_0-\mathbf{q}$. Composing the sign changes independently in the two parts gives the Klein four-group. $\square$

**Worked values.** For $\tilde q = 1+2e_1-e_2+3e_3$,

$$
\bar{\tilde q} = 1-2e_1+e_2-3e_3, \qquad -\bar{\tilde q} = -1+2e_1-e_2+3e_3, \qquad -\tilde q = -1-2e_1+e_2-3e_3 .
$$

**Proposition (fixed-point subspaces).** The fixed points of the three involutions are

$$
\{\tilde q : \bar{\tilde q} = \tilde q\} = \mathbb{R}_{\mathbb{H}} = \mathbb{R}e_0, \qquad
\{\tilde q : -\bar{\tilde q} = \tilde q\} = \operatorname{Im}\mathbb{H}, \qquad
\{\tilde q : -\tilde q = \tilde q\} = \{0\},
$$

of dimensions $1$, $3$ and $0$.

*Proof.* $\bar{\tilde q} = \tilde q$ gives $\mathbf{q} = 0$; $-\bar{\tilde q} = \tilde q$ gives $q_0 = 0$; $-\tilde q = \tilde q$ gives $\tilde q = -\tilde q$, so $\tilde q = 0$. $\square$

So the scalar axis, the imaginary three-space and the origin are the fixed sets, and they are exactly the images of the projections onto the scalar part, the vector part and zero. The first is a subalgebra isomorphic to $\mathbb{R}$; the second is not, because the product of two of its elements has a scalar part.

## The Roots of Minus One

**Definition.** A **root of $-1$** is a quaternion $\xi$ with $\xi^2 = -1$.

**Theorem.** The roots of $-1$ are the pure imaginary quaternions of norm one.

*Proof.* Write $\xi = x_0+\mathbf{x}$. Then $\xi^2 = x_0^2-N(\mathbf{x})+2x_0\mathbf{x}$, so $\xi^2 = -1$ gives $2x_0\mathbf{x} = 0$ and $x_0^2-N(\mathbf{x}) = -1$. If $x_0\neq0$ then $\mathbf{x} = 0$ and $x_0^2 = -1$, impossible, so $x_0 = 0$ and $N(\mathbf{x}) = 1$. $\square$

**Worked roots.** The element

$$
\xi = \frac{e_1+e_2+e_3}{\sqrt3}
$$

is a root of $-1$: its square is

$$
\xi^2 = \tfrac13\bigl(e_1^2+e_2^2+e_3^2+e_1e_2+e_2e_1+e_2e_3+e_3e_2+e_3e_1+e_1e_3\bigr) = \tfrac13(-3+0) = -1,
$$

because the off-diagonal products cancel in pairs and each square is $-1$. The element $e_2$ is a root, and so is the whole sphere $u_1e_1+u_2e_2+u_3e_3$ with $u_1^2+u_2^2+u_3^2 = 1$.

**The roots of $+1$.** For comparison, $\eta^2 = 1$ has only the solutions $\eta = \pm1$, because $(\eta-1)(\eta+1) = 0$ and there are no zero divisors; in particular $e_2$ is a root of $-1$ but no pure quaternion is a root of $+1$.

## The Norm Criterion for a Unit

**Theorem.** The element $\tilde q$ is a unit if and only if $N(\tilde q)\neq 0$, and then $\tilde q^{-1} = \bar{\tilde q}/N(\tilde q)$.

**Worked computation.** For the chosen element,

$$
N(\tilde q) = 1^2 + 2^2 + (-1)^2 + 3^2 = 15 \neq 0,
$$

so $\tilde q$ is a unit, with inverse

$$
\tilde q^{-1} = \frac{\bar{\tilde q}}{15} = \frac{1}{15}\bigl(1-2e_1+e_2-3e_3\bigr).
$$

The verification is the product

$$
\tilde q\,\tilde q^{-1} = \frac{\tilde q\bar{\tilde q}}{15} = \frac{N(\tilde q)}{15} = 1 .
$$

**A second element.** For $p = 1 + e_1 + e_2 + e_3$ one has $N(p) = 4$, so $p^{-1} = \tfrac14(1-e_1-e_2-e_3)$; and the multiplicativity of the norm form is checked on the pair by

$$
N(qp) = N(\tilde q)N(p) = 15\cdot4 = 60, \qquad |qp| = |\tilde q|\,|p| = \sqrt{15}\cdot2 = 2\sqrt{15}.
$$

There is no non-zero element of $\mathbb{H}$ with $N = 0$, so over $\mathbb{R}$ the unit criterion is simply $\tilde q\neq0$; the worked element is a unit for the trivial reason that it is not zero, and the content of the computation is the explicit inverse.

## The Conjugation Action

**Definition.** For a unit quaternion $u$ the **conjugation action**, or adjoint action, is $\operatorname{Ad}_u(x) = uxu^{-1} = ux\bar u$.

**Worked computation.** Take the unit quaternion

$$
u = \exp\!\Bigl(\frac{\pi}{4}e_1\Bigr) = \cos\frac{\pi}{4} + e_1\sin\frac{\pi}{4} = \frac{1+e_1}{\sqrt2},
$$

so that $u^{-1} = \bar u = (1-e_1)/\sqrt2$. Then on the imaginary basis,

$$
u\,e_1\,u^{-1} = e_1, \qquad u\,e_2\,u^{-1} = e_3, \qquad u\,e_3\,u^{-1} = -e_2 .
$$

For instance, $ue_2 = \tfrac{1}{\sqrt2}(e_2+e_1e_2) = \tfrac{1}{\sqrt2}(e_2+e_3)$, and multiplying on the right by $u^{-1}$ gives

$$
ue_2u^{-1} = \tfrac12(e_2+e_3)(1-e_1) = \tfrac12\bigl(e_2+e_3-e_2e_1-e_3e_1\bigr) = \tfrac12(e_2+e_3+e_3-e_2) = e_3 .
$$

So $\operatorname{Ad}_u$ fixes the axis $e_1$ and rotates the plane spanned by $e_2,e_3$ through $+\pi/2$: it is the quarter turn about $e_1$. Its matrix in the basis $(e_1,e_2,e_3)$ is

$$
R_u = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix},
$$

which agrees with the general formula $R_q = \bigl(1-2(q_2^2+q_3^2),\,2(q_1q_2-q_0q_3),\,2(q_1q_3+q_0q_2);\ \dots\bigr)$ at $q_0 = q_1 = 1/\sqrt2$, $q_2 = q_3 = 0$. Since $u$ and $-u$ give the same matrix and no other unit does, the map $Sp(1)\to SO(3)$ is two-to-one with kernel $\{\pm1\}$, in agreement with *Quaternion Rotations and Reflections*.

## Summary

The three involutions of the quaternion algebra are quaternion, vector and total conjugation, given by negating the vector part, the scalar part, or both, with fixed-point subspaces the scalar line, the imaginary three-space and the origin. The roots of $-1$ are the pure imaginary quaternions of norm one, forming a two-sphere, while the roots of $+1$ are only $\pm1$; the element $(e_1+e_2+e_3)/\sqrt3$ is a worked root of the first equation.

For the worked element $\tilde q = 1+2e_1-e_2+3e_3$ the norm form is $N(\tilde q) = 15$, so $\tilde q$ is a unit with $\tilde q^{-1} = \bar{\tilde q}/15$, and multiplicativity is checked against $p = 1+e_1+e_2+e_3$. The conjugation action of the unit $u = (1+e_1)/\sqrt2$ maps $e_1$ to $e_1$ and $e_2$ to $e_3$, a quarter turn about the first axis, with matrix $R_u$ matching the general formula and the two-to-one covering $Sp(1)\to SO(3)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Basis, $e_k^2 = -e_0$, $e_1e_2 = e_3$ |
| $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ | Worked element $\tilde q = 1+2e_1-e_2+3e_3$ |
| $\bar{\tilde q}, -\bar{\tilde q}, -\tilde q$ | Quaternion, vector and total conjugation |
| $\mathbb{R}_{\mathbb{H}} = \mathbb{R}e_0$ | Fixed space of $\bar{\cdot}$ |
| $\operatorname{Im}\mathbb{H}$ | Fixed space of $\tilde{\cdot}$ |
| $N(\tilde q) = \tilde q\bar{\tilde q}$ | Norm form, $N(\tilde q) = 15$ for the worked element |
| $\tilde q^{-1} = \bar{\tilde q}/N(\tilde q)$ | Inverse, $\tilde q^{-1} = \bar{\tilde q}/15$ |
| $\operatorname{Ad}_u(x) = ux\bar u$ | Conjugation action |
| $R_u$ | Matrix of $\operatorname{Ad}_u$ on $\operatorname{Im}\mathbb{H}$ |
| $\lvert \tilde q\rvert = \sqrt{N(\tilde q)}$ | Modulus |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original computational treatment of the quaternion algebra.
- Peter Guthrie Tait, *An Elementary Treatise on Quaternions* (Cambridge University Press, 3rd ed. 1890), for a systematic collection of worked quaternion and vector computations.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for explicit computations with quaternion units and their products.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for worked examples of the adjoint action and the covering of the rotation group.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quaternion units and the associated Clifford algebra.
