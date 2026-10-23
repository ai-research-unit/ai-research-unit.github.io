
# __Quaternion Four-Vector Element Representation__

## Introduction

The quaternion four-vector representation is the identification of a quaternion with the ordered quadruple of its four real coordinates. It is the simplest of the representations of the algebra and the one on which the others are read: the column vector of coordinates, its dual row vector, the component form of the product, the coordinate forms of the three involutions and of the scalar and vector subspaces, and the quaternion norm as a sum of four positive squares. This article develops those identifications.

The article is coordinate bookkeeping on the algebra fixed in *Quaternion Algebra*: the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, the multiplication rules, the conjugate and the scalar–vector decomposition are used as given. The matrix forms built from the coordinates are the subject of *Quaternion 4x4 Matrix Element Representation $M_4(\mathbb{R})_L$* and *Quaternion 2x2 Matrix Element Representation*, and the subspaces in coordinates are from *The Scalar and Vector Subspaces of $\mathbb{H}$*.

The corpus's default base is a commutative ring with identity, and the coordinate description holds over such a base; the positivity and the Euclidean interpretation of the quaternion norm are statements over $\mathbb{R}$, and they are flagged where they occur.

Throughout, a quaternion is $\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$, with $q_\mu\in F$, $\mathrm{Sc}(\tilde q) = q_t$ and $\vec q = q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$; the conjugate is $\tilde{q}^{\natural} = q_t e_t - q_x \vec e_x - q_y \vec e_y - q_z \vec e_z$ and the quaternion norm is $\langle\tilde q\rangle_{\natural} = \tilde q\tilde{q}^{\natural}$. The coordinate map is the $F$-linear isomorphism $\varphi : \mathbb{H}\to F^4$.

## The Coordinate Vector

**Definition.** The **coordinate map** sends $\tilde q = \sum_{\mu\in\{t,x,y,z\}}q_\mu e_\mu$ to the quadruple

$$
\varphi(\tilde q) = (q_t,q_x,q_y,q_z)\in F^4.
$$

**Theorem.** The map $\varphi$ is an isomorphism of $F$-vector spaces, and the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ is sent to the standard basis $(1,0,0,0),\dots,(0,0,0,1)$. Consequently addition and scalar multiplication are computed coordinatewise.

*Proof.* The map is the unique $F$-linear map sending each basis element to the corresponding standard basis element; it is bijective by the definition of a basis.

**Definition.** The **column vector** of $\tilde q$ is

$$
[\tilde q] = \begin{pmatrix} q_t \\ q_x \\ q_y \\ q_z \end{pmatrix},
$$

and the **dual row vector** is $[\tilde q]^{T} = (q_t\ q_x\ q_y\ q_z)$.

**Proposition.** The dual row vector acts on the column vector by matrix multiplication with the standard Euclidean inner product,

$$
[\tilde q_1]^{T}[\tilde q_2] = q_{1t}q_{2t}+q_{1x}q_{2x}+q_{1y}q_{2y}+q_{1z}q_{2z} = \mathrm{Sc}(\tilde q_1\tilde q_2^{\natural}),
$$

and it is the coordinate expression of the inner product of *Quaternion Norm and Invertibility*.

## Multiplication in Components

**Theorem.** The product of $\tilde q_2 = q_{2t}e_t+q_{2x}\vec e_x+q_{2y}\vec e_y+q_{2z}\vec e_z$ and $\tilde q_1 = q_{1t} e_t + q_{1x} \vec e_x + q_{1y} \vec e_y + q_{1z} \vec e_z$, in components, is given by the scalar and vector parts

$$ \boxed{\; \mathrm{Sc}(\tilde q_2\tilde q_1) = q_{2t}q_{1t} - \langle\vec q_2,\vec q_1\rangle, \qquad
\mathrm{Vect}(\tilde q_2\tilde q_1) = q_{2t}\vec q_1 + q_{1t}\vec q_2 + \vec q_2\times\vec q_1 \;} ,$$

that is, in coordinates,

$$
(\tilde q_2\tilde q_1)_t = q_{2t}q_{1t} - q_{2x}q_{1x} - q_{2y}q_{1y} - q_{2z}q_{1z}, \qquad
\begin{aligned}
(\tilde q_2\tilde q_1)_x &= q_{2t}q_{1x} + q_{2x}q_{1t} + q_{2y}q_{1z} - q_{2z}q_{1y}, \\
(\tilde q_2\tilde q_1)_y &= q_{2t}q_{1y} - q_{2x}q_{1z} + q_{2y}q_{1t} + q_{2z}q_{1x}, \\
(\tilde q_2\tilde q_1)_z &= q_{2t}q_{1z} + q_{2x}q_{1y} - q_{2y}q_{1x} + q_{2z}q_{1t}.
\end{aligned}
$$

*Proof.* Expanding $(q_{2t}+\vec q_2)(q_{1t}+\vec q_1)$ and using $\vec q_2\vec q_1 = -\langle\vec q_2,\vec q_1\rangle+\vec q_2\times\vec q_1$ gives the scalar and vector parts; the coordinate formulas are the coordinate form of the inner product and the standard cross product, whose components are $(q_{2y}q_{1z}-q_{2z}q_{1y},\ q_{2z}q_{1x}-q_{2x}q_{1z},\ q_{2x}q_{1y}-q_{2y}q_{1x})$.

**Proposition.** The scalar part of the product is symmetric and the vector part is neither symmetric nor antisymmetric as a whole: the symmetric part of the vector component is $q_{2t}\vec q_1+q_{1t}\vec q_2$ and the antisymmetric part is the cross product $\vec q_2\times\vec q_1$.

*Proof.* The scalar formula is symmetric in $\tilde q_2$ and $\tilde q_1$; in the vector formula the terms $q_{2t}\vec q_1+q_{1t}\vec q_2$ exchange under the swap while the cross product changes sign.

**Remark.** The four coordinate functions of the product are the components of the matrix product $L_{\tilde q_2}[\tilde q_1]$ with the left regular matrix $L_{\tilde q_2}$ of *Quaternion 4x4 Matrix Element Representation $M_4(\mathbb{R})_L$*, so the coordinate multiplication rule and the left regular representation carry the same information in different notation.

## The Three Involutions in Coordinates

**Theorem.** The three involutions act on the coordinate vector by the diagonal sign matrices

$$ \boxed{\; \varphi(\tilde{q}^{\natural}) = \operatorname{diag}(1,-1,-1,-1)\,[\tilde q], \qquad
\varphi(-\tilde{q}^{\natural}) = \operatorname{diag}(-1,1,1,1)\,[\tilde q], \qquad
\varphi(-\tilde q) = -[\tilde q] \;} .$$

*Proof.* Quaternion conjugation negates the three vector coordinates; vector conjugation negates the scalar coordinate; total conjugation is the negation of all four.

**Corollary.** The scalar subspace is the coordinate set $q_x = q_y = q_z = 0$, the vector subspace is the set $q_t = 0$, and the two are the $\pm1$ eigenspaces of the first two sign matrices. The composition of the three involutions generates the Klein four-group of sign changes described in *Worked Examples in the Quaternion Algebra*.

## The Subspaces in Coordinates

**Definition.** The **scalar coordinate** is $q_t$ and the **vector coordinates** are $(q_x,q_y,q_z)$.

**Theorem.** In coordinates the scalar subspace is the first coordinate axis $\{(q_t,0,0,0)\}$ and the vector subspace is the hyperplane $\{(0,q_x,q_y,q_z)\}$, and

$$
\mathbb{H} = \mathbb{R}_{\mathbb{H}}\oplus\operatorname{Im}\mathbb{H}, \qquad
F^4 = \varphi(\mathbb{R}_{\mathbb{H}})\oplus\varphi(\operatorname{Im}\mathbb{H})
$$

is the orthogonal decomposition, in the algebra and in coordinates, into the two summands.

*Proof.* The conditions are the coordinate forms of $\vec q = 0$ and $q_t = 0$; orthogonality of the two coordinate images is $q_t\cdot 0+0\cdot(q_x+q_y+q_z) = 0$ for the standard inner product.

**Proposition.** On the vector coordinates the product law reduces to the scalar and vector products of three-dimensional vector analysis: the scalar coordinate of the product of two vectors is minus the inner product, and the three vector coordinates are the components of the cross product.

*Proof.* Set $q_{2t} = q_{1t} = 0$ in the component formula; the scalar becomes $-q_{2x}q_{1x}-q_{2y}q_{1y}-q_{2z}q_{1z}$ and the vector part becomes the cross product.

## The Quaternion Norm in Coordinates

**Theorem.** The quaternion norm in coordinates is the sum of the four squares of the coordinates,

$$ \boxed{\; \langle\tilde q\rangle_{\natural} = q_t^2+q_x^2+q_y^2+q_z^2 = [\tilde q]^{T}[\tilde q] \;} ,$$

and the associated bilinear form is the standard Euclidean inner product $\mathrm{Sc}(\tilde q_2\tilde q_1^{\natural}) = [\tilde q_2]^{T}[\tilde q_1]$.

*Proof.* $\tilde q\tilde{q}^{\natural} = (q_t+\vec q)(q_t-\vec q) = q_t^2-\vec q^2 = q_t^2+\langle \vec q\rangle_{\natural} = \sum_\mu q_\mu^2$, and $[\tilde q]^T[\tilde q]$ is that sum. The bilinear form is the polarisation, which is $\mathrm{Sc}(\tilde q_2\tilde q_1^{\natural})$.

**Corollary.** Over $F = \mathbb{R}$ the quaternion norm is positive definite, the coordinate map is an isometry $\mathbb{H}\to\mathbb{R}^4$, and the modulus is the Euclidean length $|\tilde q| = \sqrt{q_t^2+q_x^2+q_y^2+q_z^2}$. In particular the four signs of the quaternion norm are all positive.

*Proof.* The sum of four squares of real numbers is non-negative and vanishes only at the origin; the remaining statements are the definitions.

## Summary

The four-vector representation identifies a quaternion with the quadruple of its coordinates in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$; the column vector $[\tilde q_1]$ and the dual row $[\tilde q_1]^T$ carry the algebra, the row acting on the column by the Euclidean inner product $\mathrm{Sc}(\tilde q_1\tilde q_2^{\natural})$. The product is computed in components by $(\tilde q_2\tilde q_1)_t = q_{2t}q_{1t}-\langle\vec q_2,\vec q_1\rangle$ and $(\tilde q_2\tilde q_1)_k$ the three components of $q_{2t}\vec q_1+q_{1t}\vec q_2+\vec q_2\times\vec q_1$, so that the coordinate rule is the three-dimensional scalar and vector product extended by the scalar coordinates.

The three involutions are the diagonal sign matrices $\operatorname{diag}(1,-1,-1,-1)$, $\operatorname{diag}(-1,1,1,1)$ and $-I$, whose fixed coordinate sets are the first axis, the hyperplane $q_t = 0$ and the origin. The scalar and vector subspaces are the first axis and that hyperplane, an orthogonal decomposition of the coordinate space, and the quaternion norm is the sum of the four positive squares $[\tilde q]^T[\tilde q]$.

The quaternion case is the real case, and its four positive signs are the whole of the difference.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra |
| $F$ | Base field; $\mathbb{R}$ for the positive-definite statements |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Basis, $\vec e_k^2 = -e_t$ |
| $\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$ | Quaternion with coordinates $q_\mu$ |
| $\varphi : \mathbb{H}\to F^4$ | Coordinate isomorphism |
| $[\tilde q] = (q_t,q_x,q_y,q_z)^T$ | Column vector of coordinates |
| $[\tilde q]^{T} = (q_t\ q_x\ q_y\ q_z)$ | Dual row vector |
| $[\tilde q_1]^{T}[\tilde q_2] = \mathrm{Sc}(\tilde q_1\tilde q_2^{\natural})$ | Euclidean inner product in coordinates |
| $\operatorname{diag}(1,-1,-1,-1)$ | Matrix of quaternion conjugation |
| $\operatorname{diag}(-1,1,1,1)$ | Matrix of vector conjugation |
| $\mathbb{R}_{\mathbb{H}}, \operatorname{Im}\mathbb{H}$ | Scalar axis and vector hyperplane in coordinates |
| $\langle\tilde q\rangle_{\natural} = \sum_{\mu\in\{t,x,y,z\}}q_\mu^2 = [\tilde q]^{T}[\tilde q]$ | Quaternion norm, four positive signs |
| $\vec q_2\times\vec q_1$ | Cross product in the vector coordinates |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original coordinate treatment of quaternion multiplication.
- Peter Guthrie Tait, *An Elementary Treatise on Quaternions* (Cambridge University Press, 3rd ed. 1890), for coordinate computations with the vector product.
- Josiah Willard Gibbs and Edwin Bidwell Wilson, *Vector Analysis* (Scribner, 1901), for the scalar and vector products recovered from the coordinate rule.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the coordinate and matrix descriptions of the quaternion algebra.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge University Press, 2003), for the component form of quaternion and Clifford products.
