
# __Worked Examples in the Quaternion Algebra__

## Introduction

This article works the constructions of the quaternion algebra on explicit elements. Its purpose is to compute, once and completely, the quantities that the other articles of the family define in general: the three involutions and their fixed-point subspaces, the roots of $-1$, the conjugation action on a concrete element, and the $2\times2$ complex and $4\times4$ real matrix images. Nothing here is new mathematics; the interest is that each general statement is followed through in coordinates, so that the conventions of the family can be read off a single worked example.

The element worked throughout is

$$
\tilde q = 1 + 2\vec e_x - \vec e_y + 3\vec e_z,
$$

with scalar part $q_t = 1$ and vector part $\vec q = 2\vec e_x - \vec e_y + 3\vec e_z$, chosen so that no coordinate vanishes and no two coordinates coincide. The general theory is from *Quaternion Algebra* (the basis, the multiplication and the three involutions), *Quaternion Norm and Invertibility* (the quaternion norm and the unit criterion), *Quaternion Rotations and Reflections* (the conjugation action and the covering of $SO(3)$), *Quaternion 2x2 Matrix Element Representation* and *Quaternion 4x4 Matrix Element Representation $M_4(\mathbb{R})_L$* (the matrix images). A few examples with other elements are given where a single example would be misleading.

Throughout, the basis is $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with

$$
\vec e_x^2 = \vec e_y^2 = \vec e_z^2 = \vec e_x\vec e_y\vec e_z = -e_t, \qquad \vec e_x\vec e_y = \vec e_z, \quad \vec e_y\vec e_z = \vec e_x, \quad \vec e_z\vec e_x = \vec e_y,
$$

and the products in the opposite order are the negatives. A quaternion is $\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$, the conjugate is $\tilde{q}^{\natural} = q_t e_t - q_x \vec e_x - q_y \vec e_y - q_z \vec e_z$, and the quaternion norm $\langle\cdot\rangle_{\natural}$ is that of *Quaternion Norm and Invertibility*, named here and not defined again.

## The Three Involutions

**Definition.** The three **involutions** of the quaternion algebra are the real-linear maps

$$
\tilde{q}^{\natural} = q_t e_t - q_x \vec e_x - q_y \vec e_y - q_z \vec e_z, \qquad -\tilde{q}^{\natural} = -q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z, \qquad -\tilde q = -q_t e_t - q_x \vec e_x - q_y \vec e_y - q_z \vec e_z,
$$

called quaternion, vector and total conjugation. Each is an involution: applying it twice returns $\tilde q$.

**Proposition.** The three involutions are ${}^{\natural}$, $-{}^{\natural}$ and $-\mathrm{id}$: the second is the negative of the first and the third is the negative of the identity, so the three maps together with the identity form the group $\mathbb{Z}/2\times\mathbb{Z}/2$ of sign changes of the scalar and vector parts.

*Proof.* The first negates the vector part and fixes the scalar part, $q_t-\vec q$; the second is its negative, $-q_t+\vec q = -(q_t-\vec q)$, and so negates the scalar part and fixes the vector part; the third negates both, $-q_t-\vec q$. Composing the sign changes independently in the two parts gives the Klein four-group.

**Worked values.** For $\tilde q = 1+2\vec e_x-\vec e_y+3\vec e_z$,

$$
\tilde{q}^{\natural} = 1-2\vec e_x+\vec e_y-3\vec e_z, \qquad -\tilde{q}^{\natural} = -1+2\vec e_x-\vec e_y+3\vec e_z, \qquad -\tilde q = -1-2\vec e_x+\vec e_y-3\vec e_z.
$$

**Proposition (fixed-point subspaces).** The fixed points of the three involutions are

$$
\{\tilde q : \tilde{q}^{\natural} = \tilde q\} = \mathbb{R}_{\mathbb{H}} = \mathbb{R}e_t, \qquad
\{\tilde q : -\tilde{q}^{\natural} = \tilde q\} = \operatorname{Im}\mathbb{H}, \qquad
\{\tilde q : -\tilde q = \tilde q\} = \{0\},
$$

of dimensions $1$, $3$ and $0$.

*Proof.* $\tilde{q}^{\natural} = \tilde q$ gives $\vec q = 0$; $-\tilde{q}^{\natural} = \tilde q$ gives $q_t = 0$; $-\tilde q = \tilde q$ gives $\tilde q = -\tilde q$, so $\tilde q = 0$.

So the scalar axis, the imaginary three-space and the origin are the fixed sets, and they are exactly the images of the projections onto the scalar part, the vector part and zero. The first is a subalgebra isomorphic to $\mathbb{R}$; the second is not, because the product of two of its elements has a scalar part.

## The Roots of Minus One

**Definition.** A **root of $-1$** is a quaternion $\tilde\xi$ with $\tilde\xi^2 = -1$.

**Theorem.** The roots of $-1$ are the pure imaginary quaternions of norm one.

*Proof.* Write $\tilde\xi = \xi_t+\vec\xi$. Then $\tilde\xi^2 = \xi_t^2-\langle \vec\xi\rangle_{\natural}+2\xi_t\vec\xi$, so $\tilde\xi^2 = -1$ gives $2\xi_t\vec\xi = 0$ and $\xi_t^2-\langle \vec\xi\rangle_{\natural} = -1$. If $\xi_t\neq0$ then $\vec\xi = 0$ and $\xi_t^2 = -1$, impossible, so $\xi_t = 0$ and $\langle \vec\xi\rangle_{\natural} = 1$.

**Worked roots.** The element

$$
\tilde\xi = \frac{\vec e_x+\vec e_y+\vec e_z}{\sqrt3}
$$

is a root of $-1$: its square is

$$
\tilde\xi^2 = \tfrac13\bigl(\vec e_x^2+\vec e_y^2+\vec e_z^2+\vec e_x\vec e_y+\vec e_y\vec e_x+\vec e_y\vec e_z+\vec e_z\vec e_y+\vec e_z\vec e_x+\vec e_x\vec e_z\bigr) = \tfrac13(-3+0) = -1,
$$

because the off-diagonal products cancel in pairs and each square is $-1$. The element $\vec e_y$ is a root, and so is the whole sphere $u_x\vec e_x+u_y\vec e_y+u_z\vec e_z$ with $u_x^2+u_y^2+u_z^2 = 1$.

**The roots of $+1$.** For comparison, $\eta^2 = 1$ has only the solutions $\eta = \pm1$, because $(\eta-1)(\eta+1) = 0$ and there are no zero divisors; in particular $\vec e_y$ is a root of $-1$ but no pure quaternion is a root of $+1$.

## The Conjugation Action

**Definition.** For a unit quaternion $u$ the **conjugation action**, or adjoint action, is $\operatorname{Ad}_u(\tilde q) = u\tilde q u^{-1} = u\tilde q u^{\natural}$.

**Worked computation.** Take the unit quaternion

$$
u = \exp\!\Bigl(\frac{\pi}{4}\vec e_x\Bigr) = \cos\frac{\pi}{4} + \vec e_x\sin\frac{\pi}{4} = \frac{1+\vec e_x}{\sqrt2},
$$

so that $u^{-1} = u^{\natural} = (1-\vec e_x)/\sqrt2$. Then on the imaginary basis,

$$
u\,\vec e_x\,u^{-1} = \vec e_x, \qquad u\,\vec e_y\,u^{-1} = \vec e_z, \qquad u\,\vec e_z\,u^{-1} = -\vec e_y.
$$

For instance, $u\vec e_y = \tfrac{1}{\sqrt2}(\vec e_y+\vec e_x\vec e_y) = \tfrac{1}{\sqrt2}(\vec e_y+\vec e_z)$, and multiplying on the right by $u^{-1}$ gives

$$
u\vec e_yu^{-1} = \tfrac12(\vec e_y+\vec e_z)(1-\vec e_x) = \tfrac12\bigl(\vec e_y+\vec e_z-\vec e_y\vec e_x-\vec e_z\vec e_x\bigr) = \tfrac12(\vec e_y+\vec e_z+\vec e_z-\vec e_y) = \vec e_z.
$$

So $\operatorname{Ad}_u$ fixes $\vec e_x$ and carries $\vec e_y$ to $\vec e_z$ and $\vec e_z$ to $-\vec e_y$; its matrix in the basis $(\vec e_x,\vec e_y,\vec e_z)$ is

$$
R_u = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix},
$$

and it agrees with the general formula $R_{\tilde q} = \bigl(1-2(q_y^2+q_z^2),\,2(q_xq_y-q_tq_z),\,2(q_xq_z+q_tq_y);\ \dots\bigr)$ at $q_t = q_x = 1/\sqrt2$, $q_y = q_z = 0$. The reading of $R_u$ as the quarter turn about $\vec e_x$, and of the assignment $u\mapsto R_u$ as the two-to-one covering $Sp(1)\to SO(3)$ with kernel $\{\pm1\}$, is in *Quaternion Rotations and Reflections*.

## The Matrix Images

**The $2\times2$ complex image.** Under the isomorphism $\mathsf{M}_2$ of *Quaternion 2x2 Matrix Element Representation*, fixed by

$$
e_t\mapsto I, \qquad \vec e_x\mapsto \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}, \qquad \vec e_y\mapsto \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad \vec e_z\mapsto \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix},
$$

the worked element has image

$$
\mathsf{M}_2(\tilde q) = \begin{pmatrix} 1-3i & 1-2i \\ -1-2i & 1+3i \end{pmatrix}.
$$

Its trace is $2q_t = 2$ and its determinant is $\langle\tilde q\rangle_{\natural} = 15$, in agreement with the general identities $\operatorname{tr}\mathsf{M}_2(\tilde q) = 2q_t$ and $\det\mathsf{M}_2(\tilde q) = \langle\tilde q\rangle_{\natural}$.

$$
\mathsf{M}_4(\tilde q) = \begin{pmatrix}
1 & -2 & 1 & -3 \\
2 & 1 & -3 & -1 \\
-1 & 3 & 1 & -2 \\
3 & 1 & 2 & 1
\end{pmatrix}.
$$

Its trace is $4q_t = 4$, its determinant is $\langle\tilde q\rangle_{\natural}^2 = 225$, and $\mathsf{M}_4(\tilde q)^{T}\mathsf{M}_4(\tilde q) = 15\,I = \langle\tilde q\rangle_{\natural}I$.

## Summary

The three involutions of the quaternion algebra are quaternion, vector and total conjugation, given by negating the vector part, the scalar part, or both, with fixed-point subspaces the scalar line, the imaginary three-space and the origin. The roots of $-1$ are the pure imaginary quaternions of norm one, forming a two-sphere, while the roots of $+1$ are only $\pm1$; the element $(\vec e_x+\vec e_y+\vec e_z)/\sqrt3$ is a worked root of the first equation.

The conjugation action of the unit $u = (1+\vec e_x)/\sqrt2$ maps $\vec e_x$ to $\vec e_x$ and $\vec e_y$ to $\vec e_z$, with matrix $R_u$ matching the general formula; the geometric reading of $R_u$ and the covering $Sp(1)\to SO(3)$ are in *Quaternion Rotations and Reflections*. For the worked element $\tilde q = 1+2\vec e_x-\vec e_y+3\vec e_z$, whose quaternion norm is $\langle\tilde q\rangle_{\natural} = 15$, the $2\times2$ complex image $\mathsf{M}_2(\tilde q)$ has trace $2$ and determinant $15$, and the $4\times4$ real Cayley image $\mathsf{M}_4(\tilde q)$ has trace $4$, determinant $225$ and $\mathsf{M}_4(\tilde q)^{T}\mathsf{M}_4(\tilde q) = 15\,I$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Basis, $\vec e_k^2 = -e_t$, $\vec e_x\vec e_y = \vec e_z$ |
| $\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$ | Worked element $\tilde q = 1+2\vec e_x-\vec e_y+3\vec e_z$ |
| $\tilde{q}^{\natural}, -\tilde{q}^{\natural}, -\tilde q$ | Quaternion, vector and total conjugation |
| $\mathbb{R}_{\mathbb{H}} = \mathbb{R}e_t$ | Fixed space of ${}^{\natural}$ |
| $\operatorname{Im}\mathbb{H}$ | Fixed space of $\tilde{\cdot}$ |
| $\langle\cdot\rangle_{\natural}$ | Quaternion norm, from *Quaternion Norm and Invertibility*; $\langle\tilde q\rangle_{\natural} = 15$ for the worked element |
| $\operatorname{Ad}_u(\tilde q) = u\tilde q u^{\natural}$ | Conjugation action |
| $R_u$ | Matrix of $\operatorname{Ad}_u$ on $\operatorname{Im}\mathbb{H}$ |
| $\mathsf{M}_2$ | The isomorphism $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C})$ |
| $\mathsf{M}_4(\tilde q)$ | Cayley matrix of left multiplication by $\tilde q$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original computational treatment of the quaternion algebra.
- Peter Guthrie Tait, *An Elementary Treatise on Quaternions* (Cambridge University Press, 3rd ed. 1890), for a systematic collection of worked quaternion and vector computations.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for explicit computations with quaternion units and their products.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for worked examples of the adjoint action and the covering of the rotation group.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quaternion units and the associated Clifford algebra.
