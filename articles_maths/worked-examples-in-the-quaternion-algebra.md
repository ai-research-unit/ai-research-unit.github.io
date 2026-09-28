
# __Worked Examples in the Quaternion Algebra__

## Introduction

This article works the constructions of the quaternion algebra on explicit elements. Its purpose is to compute, once and completely, the quantities that the other articles of the family define in general: the three involutions and their fixed-point subspaces, the roots of $-1$, the conjugation action on a concrete element, and the $2\times2$ complex and $4\times4$ real matrix images. Nothing here is new mathematics; the interest is that each general statement is followed through in coordinates, so that the conventions of the family can be read off a single worked example.

The element worked throughout is

$$
\tilde q = 1 + 2e_1 - e_2 + 3e_3,
$$

with scalar part $q_0 = 1$ and vector part $\mathbf{q} = 2e_1 - e_2 + 3e_3$, chosen so that no coordinate vanishes and no two coordinates coincide. The general theory is from *Quaternion Algebra* (the basis, the multiplication and the three involutions), *Quaternion Norm and Invertibility* (the quaternion norm and the unit criterion), *Quaternion Rotations and Reflections* (the conjugation action and the covering of $SO(3)$), *Quaternion 2x2 Matrix Element Representation* and *Quaternion 4x4 Regular Matrix Element Representation* (the matrix images). A few examples with other elements are given where a single example would be misleading.

Throughout, the basis is $e_0 = 1, e_1, e_2, e_3$ with

$$
e_1^2 = e_2^2 = e_3^2 = e_1e_2e_3 = -e_0, \qquad e_1e_2 = e_3, \quad e_2e_3 = e_1, \quad e_3e_1 = e_2,
$$

and the products in the opposite order are the negatives. A quaternion is $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$, the conjugate is $\bar{\tilde q} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$, and the quaternion norm $N$ is that of *Quaternion Norm and Invertibility*, named here and not defined again.

## The Three Involutions

**Definition.** The three **involutions** of the quaternion algebra are the real-linear maps

$$
\bar{\tilde q} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3, \qquad -\bar{\tilde q} = -q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad -\tilde q = -q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3,
$$

called quaternion, vector and total conjugation. Each is an involution: applying it twice returns $\tilde q$.

**Proposition.** The three involutions are $\bar{\cdot}$, $-\bar{\cdot}$ and $-\mathrm{id}$: the second is the negative of the first and the third is the negative of the identity, so the three maps together with the identity form the group $\mathbb{Z}/2\times\mathbb{Z}/2$ of sign changes of the scalar and vector parts.

*Proof.* The first negates the vector part and fixes the scalar part, $q_0-\mathbf{q}$; the second is its negative, $-q_0+\mathbf{q} = -(q_0-\mathbf{q})$, and so negates the scalar part and fixes the vector part; the third negates both, $-q_0-\mathbf{q}$. Composing the sign changes independently in the two parts gives the Klein four-group.

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

*Proof.* $\bar{\tilde q} = \tilde q$ gives $\mathbf{q} = 0$; $-\bar{\tilde q} = \tilde q$ gives $q_0 = 0$; $-\tilde q = \tilde q$ gives $\tilde q = -\tilde q$, so $\tilde q = 0$.

So the scalar axis, the imaginary three-space and the origin are the fixed sets, and they are exactly the images of the projections onto the scalar part, the vector part and zero. The first is a subalgebra isomorphic to $\mathbb{R}$; the second is not, because the product of two of its elements has a scalar part.

## The Roots of Minus One

**Definition.** A **root of $-1$** is a quaternion $\xi$ with $\xi^2 = -1$.

**Theorem.** The roots of $-1$ are the pure imaginary quaternions of norm one.

*Proof.* Write $\xi = x_0+\mathbf{x}$. Then $\xi^2 = x_0^2-N(\mathbf{x})+2x_0\mathbf{x}$, so $\xi^2 = -1$ gives $2x_0\mathbf{x} = 0$ and $x_0^2-N(\mathbf{x}) = -1$. If $x_0\neq0$ then $\mathbf{x} = 0$ and $x_0^2 = -1$, impossible, so $x_0 = 0$ and $N(\mathbf{x}) = 1$.

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

So $\operatorname{Ad}_u$ fixes $e_1$ and carries $e_2$ to $e_3$ and $e_3$ to $-e_2$; its matrix in the basis $(e_1,e_2,e_3)$ is

$$
R_u = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix},
$$

and it agrees with the general formula $R_q = \bigl(1-2(q_2^2+q_3^2),\,2(q_1q_2-q_0q_3),\,2(q_1q_3+q_0q_2);\ \dots\bigr)$ at $q_0 = q_1 = 1/\sqrt2$, $q_2 = q_3 = 0$. The reading of $R_u$ as the quarter turn about $e_1$, and of the assignment $u\mapsto R_u$ as the two-to-one covering $Sp(1)\to SO(3)$ with kernel $\{\pm1\}$, is in *Quaternion Rotations and Reflections*.

## The Matrix Images

**The $2\times2$ complex image.** Under the isomorphism $\Phi$ of *Quaternion 2x2 Matrix Element Representation*, fixed by

$$
e_0\mapsto I, \qquad e_1\mapsto \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}, \qquad e_2\mapsto \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad e_3\mapsto \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix},
$$

the worked element has image

$$
\Phi(\tilde q) = \begin{pmatrix} 1-3i & 1-2i \\ -1-2i & 1+3i \end{pmatrix}.
$$

Its trace is $2q_0 = 2$ and its determinant is $N(\tilde q) = 15$, in agreement with the general identities $\operatorname{tr}\Phi(\tilde Q) = 2Q_0$ and $\det\Phi(\tilde Q) = N(\tilde Q)$.

**The $4\times4$ real image.** Under the left regular representation of *Quaternion 4x4 Regular Matrix Element Representation*, whose Cayley matrix has the four products $\tilde q e_k$ for columns, the worked element has image

$$
L_q = \begin{pmatrix}
1 & -2 & 1 & -3 \\
2 & 1 & -3 & -1 \\
-1 & 3 & 1 & -2 \\
3 & 1 & 2 & 1
\end{pmatrix}.
$$

Its trace is $4q_0 = 4$, its determinant is $N(\tilde q)^2 = 225$, and $L_q^{T}L_q = 15\,I = N(\tilde q)I$.

## Summary

The three involutions of the quaternion algebra are quaternion, vector and total conjugation, given by negating the vector part, the scalar part, or both, with fixed-point subspaces the scalar line, the imaginary three-space and the origin. The roots of $-1$ are the pure imaginary quaternions of norm one, forming a two-sphere, while the roots of $+1$ are only $\pm1$; the element $(e_1+e_2+e_3)/\sqrt3$ is a worked root of the first equation.

The conjugation action of the unit $u = (1+e_1)/\sqrt2$ maps $e_1$ to $e_1$ and $e_2$ to $e_3$, with matrix $R_u$ matching the general formula; the geometric reading of $R_u$ and the covering $Sp(1)\to SO(3)$ are in *Quaternion Rotations and Reflections*. For the worked element $\tilde q = 1+2e_1-e_2+3e_3$, whose quaternion norm is $N(\tilde q) = 15$, the $2\times2$ complex image $\Phi(\tilde q)$ has trace $2$ and determinant $15$, and the $4\times4$ real Cayley image $L_q$ has trace $4$, determinant $225$ and $L_q^{T}L_q = 15\,I$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Basis, $e_k^2 = -e_0$, $e_1e_2 = e_3$ |
| $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ | Worked element $\tilde q = 1+2e_1-e_2+3e_3$ |
| $\bar{\tilde q}, -\bar{\tilde q}, -\tilde q$ | Quaternion, vector and total conjugation |
| $\mathbb{R}_{\mathbb{H}} = \mathbb{R}e_0$ | Fixed space of $\bar{\cdot}$ |
| $\operatorname{Im}\mathbb{H}$ | Fixed space of $\tilde{\cdot}$ |
| $N$ | Quaternion norm, from *Quaternion Norm and Invertibility*; $N(\tilde q) = 15$ for the worked element |
| $\operatorname{Ad}_u(x) = ux\bar u$ | Conjugation action |
| $R_u$ | Matrix of $\operatorname{Ad}_u$ on $\operatorname{Im}\mathbb{H}$ |
| $\Phi$ | The isomorphism $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C})$ |
| $L_q$ | Cayley matrix of left multiplication by $\tilde q$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original computational treatment of the quaternion algebra.
- Peter Guthrie Tait, *An Elementary Treatise on Quaternions* (Cambridge University Press, 3rd ed. 1890), for a systematic collection of worked quaternion and vector computations.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for explicit computations with quaternion units and their products.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for worked examples of the adjoint action and the covering of the rotation group.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quaternion units and the associated Clifford algebra.
