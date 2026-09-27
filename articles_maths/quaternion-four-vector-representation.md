
# __Quaternion Four-Vector Representation__

## Introduction

The quaternion four-vector representation is the identification of a quaternion with the ordered quadruple of its four real coordinates. It is the simplest of the representations of the algebra and the one on which the others are read: the column vector of coordinates, its dual row vector, the component form of the product, the coordinate forms of the three involutions and of the scalar and vector subspaces, and the norm form as a sum of four positive squares. This article develops those identifications. It is the quaternion member of the family's coordinate-representation pair; its counterpart is the four-vector representation of the biquaternion algebra, where the four coordinates are complex and the norm form has an indefinite complex signature rather than four positive signs.

The article is coordinate bookkeeping on the algebra fixed in *Quaternion Algebra*: the basis $(e_0,e_1,e_2,e_3)$, the multiplication rules, the conjugate and the scalar–vector decomposition are used as given. The matrix forms built from the coordinates are the subject of *Quaternion 4x4 Regular Matrix Representation* and *Quaternion 2x2 Matrix Representation*, and the subspaces in coordinates are from *The Scalar and Vector Subspaces of $\mathbb{H}$*.

The corpus's default base is a commutative ring with identity, and the coordinate description holds over such a base; the positivity and the Euclidean interpretation of the norm form are statements over $\mathbb{R}$, and they are flagged where they occur.

Throughout, a quaternion is $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$, with $q_\mu\in F$, $\operatorname{Sc}(\tilde q) = q_0$ and $\mathbf{q} = q_1e_1+q_2e_2+q_3e_3$; the conjugate is $\bar{\tilde q} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$ and the norm form is $N(\tilde q) = \tilde q\bar{\tilde q}$. The coordinate map is the $F$-linear isomorphism $\varphi : \mathbb{H}\to F^4$.

## The Coordinate Vector

**Definition.** The **coordinate map** sends $\tilde q = \sum_{\mu=0}^{3}q_\mu e_\mu$ to the quadruple

$$
\varphi(\tilde q) = (q_0,q_1,q_2,q_3)\in F^4 .
$$

**Theorem.** The map $\varphi$ is an isomorphism of $F$-vector spaces, and the basis $(e_0,e_1,e_2,e_3)$ is sent to the standard basis $(1,0,0,0),\dots,(0,0,0,1)$. Consequently addition and scalar multiplication are computed coordinatewise.

*Proof.* The map is the unique $F$-linear map sending each basis element to the corresponding standard basis element; it is bijective by the definition of a basis. $\square$

**Definition.** The **column vector** of $\tilde q$ is

$$
[\tilde q] = \begin{pmatrix} q_0 \\ q_1 \\ q_2 \\ q_3 \end{pmatrix},
$$

and the **dual row vector** is $[\tilde q]^{T} = (q_0\ q_1\ q_2\ q_3)$.

**Proposition.** The dual row vector acts on the column vector by matrix multiplication with the standard Euclidean inner product,

$$
[\tilde q]^{T}[p] = q_0p_0+q_1p_1+q_2p_2+q_3p_3 = \operatorname{Sc}(\tilde q\bar p),
$$

and it is the coordinate expression of the inner product of *Quaternion Norm and Invertibility*.

## Multiplication in Components

**Theorem.** The product of $p = p_0+\mathbf{p}$ and $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$, in components, is given by the scalar and vector parts

$$
\operatorname{Sc}(pq) = p_0q_0 - \langle\mathbf{p},\mathbf{q}\rangle, \qquad
\operatorname{Vect}(pq) = p_0\mathbf{q} + q_0\mathbf{p} + \mathbf{p}\times\mathbf{q},
$$

that is, in coordinates,

$$
(pq)_0 = p_0q_0 - p_1q_1 - p_2q_2 - p_3q_3, \qquad
\begin{aligned}
(pq)_1 &= p_0q_1 + p_1q_0 + p_2q_3 - p_3q_2, \\
(pq)_2 &= p_0q_2 - p_1q_3 + p_2q_0 + p_3q_1, \\
(pq)_3 &= p_0q_3 + p_1q_2 - p_2q_1 + p_3q_0 .
\end{aligned}
$$

*Proof.* Expanding $(p_0+\mathbf{p})(q_0+\mathbf{q})$ and using $\mathbf{p}\mathbf{q} = -\langle\mathbf{p},\mathbf{q}\rangle+\mathbf{p}\times\mathbf{q}$ gives the scalar and vector parts; the coordinate formulas are the coordinate form of the inner product and the standard cross product, whose components are $(p_2q_3-p_3q_2,\ p_3q_1-p_1q_3,\ p_1q_2-p_2q_1)$. $\square$

**Proposition.** The scalar part of the product is symmetric and the vector part is neither symmetric nor antisymmetric as a whole: the symmetric part of the vector component is $p_0\mathbf{q}+q_0\mathbf{p}$ and the antisymmetric part is the cross product $\mathbf{p}\times\mathbf{q}$.

*Proof.* The scalar formula is symmetric in $p$ and $\tilde q$; in the vector formula the terms $p_0\mathbf{q}+q_0\mathbf{p}$ exchange under the swap while the cross product changes sign. $\square$

**Remark.** The four coordinate functions of the product are the components of the matrix product $L_p[\tilde q]$ with the left regular matrix $L_p$ of *Quaternion 4x4 Regular Matrix Representation*, so the coordinate multiplication rule and the left regular representation carry the same information in different notation.

## The Three Involutions in Coordinates

**Theorem.** The three involutions act on the coordinate vector by the diagonal sign matrices

$$
\varphi(\bar{\tilde q}) = \operatorname{diag}(1,-1,-1,-1)\,[\tilde q], \qquad
\varphi(-\bar{\tilde q}) = \operatorname{diag}(-1,1,1,1)\,[\tilde q], \qquad
\varphi(-\tilde q) = -[\tilde q] .
$$

*Proof.* Quaternion conjugation negates the three vector coordinates; vector conjugation negates the scalar coordinate; total conjugation is the negation of all four. $\square$

**Corollary.** The scalar subspace is the coordinate set $q_1 = q_2 = q_3 = 0$, the vector subspace is the set $q_0 = 0$, and the two are the $\pm1$ eigenspaces of the first two sign matrices. The composition of the three involutions generates the Klein four-group of sign changes described in *Worked Examples in the Quaternion Algebra*.

## The Subspaces in Coordinates

**Definition.** The **scalar coordinate** is $q_0$ and the **vector coordinates** are $(q_1,q_2,q_3)$.

**Theorem.** In coordinates the scalar subspace is the first coordinate axis $\{(q_0,0,0,0)\}$ and the vector subspace is the hyperplane $\{(0,q_1,q_2,q_3)\}$, and

$$
\mathbb{H} = \mathbb{R}_{\mathbb{H}}\oplus\operatorname{Im}\mathbb{H}, \qquad
F^4 = \varphi(\mathbb{R}_{\mathbb{H}})\oplus\varphi(\operatorname{Im}\mathbb{H})
$$

is the orthogonal decomposition, in the algebra and in coordinates, into the two summands.

*Proof.* The conditions are the coordinate forms of $\mathbf{q} = 0$ and $q_0 = 0$; orthogonality of the two coordinate images is $q_0\cdot 0+0\cdot(q_1+q_2+q_3) = 0$ for the standard inner product. $\square$

**Proposition.** On the vector coordinates the product law reduces to the scalar and vector products of three-dimensional vector analysis: the scalar coordinate of the product of two vectors is minus the inner product, and the three vector coordinates are the components of the cross product.

*Proof.* Set $p_0 = q_0 = 0$ in the component formula; the scalar becomes $-p_1q_1-p_2q_2-p_3q_3$ and the vector part becomes the cross product. $\square$

## The Norm Form in Coordinates

**Theorem.** The norm form in coordinates is the sum of the four squares of the coordinates,

$$
N(\tilde q) = q_0^2+q_1^2+q_2^2+q_3^2 = [\tilde q]^{T}[\tilde q],
$$

and the associated bilinear form is the standard Euclidean inner product $\operatorname{Sc}(p\bar{\tilde q}) = [p]^{T}[\tilde q]$.

*Proof.* $\tilde q\bar{\tilde q} = (q_0+\mathbf{q})(q_0-\mathbf{q}) = q_0^2-\mathbf{q}^2 = q_0^2+N(\mathbf{q}) = \sum_\mu q_\mu^2$, and $[\tilde q]^T[\tilde q]$ is that sum. The bilinear form is the polarisation, which is $\operatorname{Sc}(p\bar{\tilde q})$. $\square$

**Corollary.** Over $F = \mathbb{R}$ the norm form is positive definite, the coordinate map is an isometry $\mathbb{H}\to\mathbb{R}^4$, and the modulus is the Euclidean length $|\tilde q| = \sqrt{q_0^2+q_1^2+q_2^2+q_3^2}$. In particular the four signs of the norm form are all positive.

*Proof.* The sum of four squares of real numbers is non-negative and vanishes only at the origin; the remaining statements are the definitions. $\square$

## Relation to the Biquaternion Four-Vector Representation

In the biquaternion algebra the four coordinates are complex numbers and the coordinate map is an isomorphism $\mathbb{B}\to\mathbb{C}^4$; the four-vector representation there carries the complex conjugate on each coordinate and an indefinite norm form, because the complex norm is not positive. The two representations share their bookkeeping — the coordinate vector, the dual row, the component product and the two subspaces — and differ in the field of the coordinates and in the sign pattern of the norm form.

| Feature | $\mathbb{H}$ | $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
|---|---|---|
| Coordinate field | $\mathbb{R}$ | $\mathbb{C}$ |
| Coordinates of $\tilde q$ | four reals $q_0,q_1,q_2,q_3$ | four complex numbers |
| Additional conjugation | none | complex conjugation of each coordinate |
| Norm form | $\sum_\mu q_\mu^2$ | $\sum_\mu q_\mu^2$ with complex $q_\mu$ |
| Sign pattern of $N$ | four positive signs | indefinite, values in $\mathbb{C}$ |
| Inner product | Euclidean, positive definite | Hermitian, indefinite |

The table makes the point of the comparison: the quaternion coordinate description is the real one, with four positive signs, and it becomes the biquaternion description by extending the coordinate field. The extra structure of the biquaternion case — the further conjugation and the indefinite form — is exactly what the complexification supplies, and it is not available over $\mathbb{R}$. The biquaternion account is in *Biquaternion Four-Vector Representation*.

## Summary

The four-vector representation identifies a quaternion with the quadruple of its coordinates in the basis $(e_0,e_1,e_2,e_3)$; the column vector $[\tilde q]$ and the dual row $[\tilde q]^T$ carry the algebra, the row acting on the column by the Euclidean inner product $\operatorname{Sc}(\tilde q\bar p)$. The product is computed in components by $(pq)_0 = p_0q_0-\langle\mathbf{p},\mathbf{q}\rangle$ and $(pq)_k$ the three components of $p_0\mathbf{q}+q_0\mathbf{p}+\mathbf{p}\times\mathbf{q}$, so that the coordinate rule is the three-dimensional scalar and vector product extended by the scalar coordinates.

The three involutions are the diagonal sign matrices $\operatorname{diag}(1,-1,-1,-1)$, $\operatorname{diag}(-1,1,1,1)$ and $-I$, whose fixed coordinate sets are the first axis, the hyperplane $q_0 = 0$ and the origin. The scalar and vector subspaces are the first axis and that hyperplane, an orthogonal decomposition of the coordinate space, and the norm form is the sum of the four positive squares $[\tilde q]^T[\tilde q]$.

The biquaternion four-vector representation has the same shape over the complex field, with four complex coordinates, an additional coordinatewise conjugation and an indefinite norm form. The quaternion case is the real case, and its four positive signs are the whole of the difference.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra |
| $F$ | Base field; $\mathbb{R}$ for the positive-definite statements |
| $e_0 = 1, e_1, e_2, e_3$ | Basis, $e_k^2 = -e_0$ |
| $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ | Quaternion with coordinates $q_\mu$ |
| $\varphi : \mathbb{H}\to F^4$ | Coordinate isomorphism |
| $[\tilde q] = (q_0,q_1,q_2,q_3)^T$ | Column vector of coordinates |
| $[\tilde q]^{T} = (q_0\ q_1\ q_2\ q_3)$ | Dual row vector |
| $[\tilde q]^{T}[p] = \operatorname{Sc}(\tilde q\bar p)$ | Euclidean inner product in coordinates |
| $\operatorname{diag}(1,-1,-1,-1)$ | Matrix of quaternion conjugation |
| $\operatorname{diag}(-1,1,1,1)$ | Matrix of vector conjugation |
| $\mathbb{R}_{\mathbb{H}}, \operatorname{Im}\mathbb{H}$ | Scalar axis and vector hyperplane in coordinates |
| $N(\tilde q) = \sum_{\mu=0}^{3}q_\mu^2 = [\tilde q]^{T}[\tilde q]$ | Norm form, four positive signs |
| $\mathbf{p}\times\mathbf{q}$ | Cross product in the vector coordinates |
| $\mathbb{B}$ | Biquaternion algebra, four complex coordinates, indefinite form |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original coordinate treatment of quaternion multiplication.
- Peter Guthrie Tait, *An Elementary Treatise on Quaternions* (Cambridge University Press, 3rd ed. 1890), for coordinate computations with the vector product.
- Josiah Willard Gibbs and Edwin Bidwell Wilson, *Vector Analysis* (Scribner, 1901), for the scalar and vector products recovered from the coordinate rule.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the coordinate and matrix descriptions of the quaternion algebra.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge University Press, 2003), for the component form of quaternion and Clifford products.
