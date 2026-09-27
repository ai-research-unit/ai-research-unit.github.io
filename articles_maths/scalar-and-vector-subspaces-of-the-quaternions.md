
# __The Scalar and Vector Subspaces of $\mathbb{H}$__

## Introduction

The quaternion algebra decomposes, as a real vector space, into the direct sum of two distinguished subspaces: the **scalar subspace**, the line of real quaternions, and the **vector subspace**, the three-dimensional space of pure imaginary quaternions. This article defines them, identifies them as the fixed spaces and the eigenspaces of the involutions of the algebra, examines the extent to which they are closed under multiplication, computes the norm form on each, and explains why the subspace lattice that the biquaternion algebra carries has no counterpart here beyond these two.

The article is the quaternion member of the family's subspace pair. Its counterpart, *Biquaternion Vector Subspace*, treats the same questions in an algebra with a central imaginary unit, where the vector subspace sits beside four further distinguished real subspaces and the whole six-subspace lattice is available. Here there is no central unit and no indefinite form, so there are exactly two subspaces, and their relation is the object of the article: the scalar line is a subalgebra, the vector space is not, and the product of two vectors carries both a scalar and a vector part.

The corpus's default base is a commutative ring with identity, but the decomposition into scalar and vector subspaces uses the involution and the factor $\tfrac12$ that produces the two eigenspaces, so it needs a base in which $2$ is invertible. All statements below are therefore stated over a field $F$ of characteristic not $2$; the inner product, the cross product and the norm form of the Euclidean statements are over $F = \mathbb{R}$.

Throughout, $\mathbb{H}$ is the quaternion algebra with basis $e_0 = 1, e_1, e_2, e_3$ and $e_k^2 = -e_0$; a quaternion is $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ with **scalar part** $\operatorname{Sc}(\tilde q) = q_0$ and **vector part** $\mathbf{q} = q_1e_1+q_2e_2+q_3e_3$; the conjugate is $\bar{\tilde q} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$ and the norm form is $N(\tilde q) = \tilde q\bar{\tilde q}$. The scalar subspace is written $\mathbb{R}_{\mathbb{H}} = \{\tilde q : \mathbf{q} = 0\}$ and the vector subspace $\operatorname{Im}\mathbb{H} = \{\tilde q : \bar{\tilde q} = -\tilde q\} = \{\tilde q : \operatorname{Sc}(\tilde q) = 0\}$.

## Definition and Basis

### The Defining Involutions

**Definition.** The **scalar subspace** is the fixed space of quaternion conjugation,

$$
\mathbb{R}_{\mathbb{H}} = \{\tilde q\in\mathbb{H} : \bar{\tilde q} = \tilde q\},
$$

and the **vector subspace** is the fixed space of vector conjugation $-\bar{\tilde q} = -q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$,

$$
\operatorname{Im}\mathbb{H} = \{\tilde q\in\mathbb{H} : -\bar{\tilde q} = \tilde q\}.
$$

**Proposition.** The two subspaces are the eigenspaces of quaternion conjugation, of eigenvalues $+1$ and $-1$ respectively, and they are the images of the projections

$$
\tilde q\mapsto \operatorname{Sc}(\tilde q) = \tfrac12(\tilde q+\bar{\tilde q}), \qquad \tilde q\mapsto \mathbf{q} = \tfrac12(\tilde q-\bar{\tilde q}).
$$

*Proof.* A quaternion is fixed by $\bar{\cdot}$ exactly when $\mathbf{q} = 0$ and fixed by the map $\tilde q\mapsto-\tilde q$ on the vector part exactly when $q_0 = 0$; the two projections are the standard projections onto the $\pm1$ eigenspaces of an involution, and the factor $\tfrac12$ is where the invertibility of $2$ enters. $\square$

### The Condition in Coordinates

Writing $\tilde q = \sum_{\mu=0}^{3} q_\mu e_\mu$, the scalar subspace is the coordinate condition $q_1 = q_2 = q_3 = 0$ and the vector subspace is the condition $q_0 = 0$. Thus

$$
\mathbb{R}_{\mathbb{H}} = \{q_0e_0 : q_0\in F\} \cong F, \qquad
\operatorname{Im}\mathbb{H} = \{q_1e_1+q_2e_2+q_3e_3 : q_k\in F\}\cong F^3 .
$$

### Basis and Dimension

**Theorem.** The scalar subspace has basis $(e_0)$ and dimension $1$; the vector subspace has basis $(e_1,e_2,e_3)$ and dimension $3$. Their direct sum is the whole algebra,

$$
\mathbb{H} = \mathbb{R}_{\mathbb{H}}\oplus\operatorname{Im}\mathbb{H}, \qquad \dim_F\mathbb{H} = 1+3 = 4 .
$$

*Proof.* The basis elements are linearly independent and each lies in the indicated subspace; the decomposition $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ is unique. $\square$

### The Two Descriptions Coincide

**Proposition.** The vector subspace is the kernel of the scalar-part functional and the derived subspace of the algebra: it is the smallest subspace whose products generate the whole algebra, and it is the Lie algebra of the unit group under the commutator bracket.

*Proof.* The kernel description is the coordinate condition. That the products of elements of $\operatorname{Im}\mathbb{H}$ generate $\mathbb{H}$ follows from $e_je_k\in\mathbb{R}_{\mathbb{H}}\oplus\operatorname{Im}\mathbb{H}$ with the vector components filling out the imaginary basis. The Lie-algebra statement is from *Quaternion Rotations and Reflections*, where $\operatorname{Im}\mathbb{H}$ is identified with the tangent space of $Sp(1)$ and the bracket is $[x,y] = 2(x\times y)$. $\square$

## Algebra and Module Structure

### The Scalar Subspace Is a Subalgebra

**Theorem.** The scalar subspace $\mathbb{R}_{\mathbb{H}}$ is a subalgebra of $\mathbb{H}$ isomorphic to the base field, it is the centre of the algebra, and it is closed under inversion of its non-zero elements.

*Proof.* The product of two scalars is a scalar, the identity is scalar, so it is a subalgebra; it is contained in the centre because scalars commute with every quaternion, and conversely an element of the centre is a scalar, by *Quaternion Algebra*. For a non-zero scalar $s$ the inverse is the scalar $s^{-1} = 1/s$, which lies in the subspace. $\square$

The scalar line is the only one of the two subspaces that is an algebra, and the only one that is closed under inversion; it is also the unique copy of the field inside $\mathbb{H}$ up to the choice of a real unit.

### The Vector Subspace Is Not a Subalgebra

**Theorem.** The vector subspace is not closed under multiplication: the product of two elements of $\operatorname{Im}\mathbb{H}$ lies in the vector subspace exactly when they are orthogonal, and otherwise it has a non-zero scalar part.

*Proof.* For $\mathbf{p},\mathbf{q}\in\operatorname{Im}\mathbb{H}$ the product is

$$
\mathbf{p}\mathbf{q} = -\langle\mathbf{p},\mathbf{q}\rangle + \mathbf{p}\times\mathbf{q},
$$

whose scalar part is the negative inner product $-\langle\mathbf{p},\mathbf{q}\rangle = -\sum_k p_kq_k$ and whose vector part is the cross product. The scalar part vanishes exactly when the two vectors are orthogonal. $\square$

**Corollary.** The vector subspace is closed under inversion but not under multiplication: for $\mathbf{q}\neq0$ the inverse is $-\mathbf{q}/N(\mathbf{q})$, again a vector, while the square $\mathbf{q}^2 = -N(\mathbf{q})$ is a non-zero scalar, not a vector.

*Proof.* For pure $\mathbf{q}$ the conjugate is $\bar{\mathbf{q}} = -\mathbf{q}$, so the inverse formula gives $\mathbf{q}^{-1} = \bar{\mathbf{q}}/N(\mathbf{q}) = -\mathbf{q}/N(\mathbf{q})$, which is pure. The square is $\mathbf{q}^2 = -\langle\mathbf{q},\mathbf{q}\rangle+\mathbf{q}\times\mathbf{q} = -N(\mathbf{q})$, a scalar, so multiplication does not preserve the subspace. $\square$

So the failure of closure of the vector subspace is a failure in the product only; the inverse of a non-zero vector is a vector, and in particular $e_1^{-1} = -e_1$. It is the square, not the inverse, that leaves the subspace.

### The Product of Two Vector Elements

The formula $\mathbf{p}\mathbf{q} = -\langle\mathbf{p},\mathbf{q}\rangle+\mathbf{p}\times\mathbf{q}$ is the quaternion form of the scalar and vector product of three-dimensional vector analysis, and it splits the product into its two parts. It has the immediate consequences

$$
\mathbf{p}\mathbf{q}+\mathbf{q}\mathbf{p} = -2\langle\mathbf{p},\mathbf{q}\rangle, \qquad \mathbf{p}\mathbf{q}-\mathbf{q}\mathbf{p} = 2(\mathbf{p}\times\mathbf{q}),
$$

so that the symmetric part of the product is the scalar inner product and the antisymmetric part is the vector cross product. The cross product is recovered from the commutator by $\mathbf{p}\times\mathbf{q} = \tfrac12(\mathbf{p}\mathbf{q}-\mathbf{q}\mathbf{p})$.

### Modules over the Other Subspace

**Proposition.** The algebra $\mathbb{H}$ is a free module of rank four over the scalar line $\mathbb{R}_{\mathbb{H}}\cong F$, and the bracket $\operatorname{ad}_x(y) = [x,y]$ of an element of the vector subspace annihilates the scalar line and preserves the vector subspace, where it acts as $\mathbf{y}\mapsto 2(\mathbf{x}\times\mathbf{y})$.

*Proof.* Over $\mathbb{R}_{\mathbb{H}}\cong F$ the algebra is free of rank four, the scalar line being the centre. For $x\in\operatorname{Im}\mathbb{H}$ the bracket is the commutator of the algebra, and $\operatorname{ad}_x(1) = 0$ while $\operatorname{ad}_x(\mathbf{y}) = x\mathbf{y}-\mathbf{y}x = 2(x\times\mathbf{y})$ lies in the vector subspace; the bracket is $F$-bilinear and antisymmetric. $\square$

## The Norm Form

### The Norm Form on Each Subspace

**Theorem.** On the scalar subspace the norm form is the square of the scalar, $N(s) = s^2$, and on the vector subspace it is the square of the Euclidean norm, $N(\mathbf{q}) = |\mathbf{q}|^2 = \langle\mathbf{q},\mathbf{q}\rangle$. Together,

$$
N(\tilde q) = N(q_0)+N(\mathbf{q}) = q_0^2+|\mathbf{q}|^2,
$$

an orthogonal sum, and the two subspaces are orthogonal for the associated inner product.

*Proof.* For $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ the conjugate is $q_0-\mathbf{q}$ and $\tilde q\bar{\tilde q} = q_0^2+\mathbf{q}\bar{\mathbf{q}} + \text{cross terms}$; the cross terms cancel because $q_0$ is central and $\bar{\mathbf{q}} = -\mathbf{q}$, leaving $q_0^2-\mathbf{q}^2 = q_0^2+N(\mathbf{q})$. Orthogonality is $\operatorname{Sc}(s\bar{\mathbf{q}}) = s\operatorname{Sc}(\mathbf{q}) = 0$. $\square$

### Units and the Two Subspaces

**Proposition.** An element of the scalar subspace is a unit exactly when it is non-zero; an element of the vector subspace is a unit exactly when it is non-zero, with inverse $-\mathbf{q}/N(\mathbf{q})$, and its square is the negative scalar $-N(\mathbf{q})$. The unit sphere of the vector subspace is the root sphere of $-1$.

*Proof.* Invertibility is $N\neq0$ by *Quaternion Norm and Invertibility*, and over $\mathbb{R}$ the norm form of either subspace vanishes only at zero. The inverse and the square are as computed above, and $N(\mathbf{q}) = 1$ in the vector subspace is the root condition $\mathbf{q}^2 = -1$. $\square$

## The Two-Subspace Lattice and the Absence of the Full Lattice

The biquaternion algebra carries six distinguished real subspaces beside the centre: the centre subspace $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\operatorname{Vect}(\mathbb{B})$, the quaternion subsystem $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subsystem $i\mathbb{H}_{\mathbb{B}}$, and the Hermitian and anti-Hermitian subspaces $\mathbb{M}_\pm$. They form a lattice, and the lattice is generated by the indefinite norm form and by the central imaginary unit $i$ that doubles every subspace.

**Definition.** The **subspace lattice** of an algebra is the set of its real subspaces distinguished by the involutions and conjugations of the algebra, partially ordered by inclusion.

**Proposition.** In the quaternion algebra the distinguished subspaces of this kind are exactly two, the scalar and the vector subspace, and the lattice is the chain

$$
0\subsetneq\mathbb{R}_{\mathbb{H}}\subsetneq\mathbb{H}, \qquad 0\subsetneq\operatorname{Im}\mathbb{H}\subsetneq\mathbb{H}
$$

together with the intersections $\mathbb{R}_{\mathbb{H}}\cap\operatorname{Im}\mathbb{H} = 0$ and the sums $\mathbb{R}_{\mathbb{H}}+\operatorname{Im}\mathbb{H} = \mathbb{H}$.

*Proof.* The quaternion algebra has one non-trivial involution, quaternion conjugation, and it has no central imaginary unit; the distinguishing involutions of the biquaternion case are therefore unavailable. The only subspaces singled out by conjugation are its $\pm1$ eigenspaces, together with the whole algebra and the zero subspace. $\square$

**Theorem.** The full six-subspace lattice of the biquaternion algebra has no counterpart in the quaternion algebra; the lattice grows to its biquaternion size exactly when the coefficient field is enlarged to $\mathbb{C}$, bringing a central imaginary unit and an indefinite norm form, and then the three complex generators $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$ appear beside the three that survive.

*Proof.* The biquaternion subspaces are defined by the additional involutions $\tilde q\mapsto iq$, the Hermitian conjugation $\dagger$ and the anti-Hermitian conjugation $\flat$, each of which uses the central unit $i$ of complexification. In the real quaternion algebra there is no central imaginary unit, so those maps are not defined, and the only involutions available are the two of quaternion and vector conjugation of the algebra, which produce the scalar and vector subspaces and no more. $\square$

The reason the full lattice needs an indefinite form is the same statement in another guise: the Hermitian decomposition of the biquaternion case separates the elements on which the complex norm form is positive from those on which it is indefinite, and that separation is meaningful only when there are elements of negative norm. In $\mathbb{H}$ the norm form is definite, every element has non-negative norm, and the Hermitian decomposition collapses to the single scalar–vector decomposition described here.

## Summary

The quaternion algebra decomposes as $\mathbb{H} = \mathbb{R}_{\mathbb{H}}\oplus\operatorname{Im}\mathbb{H}$, the fixed spaces of quaternion conjugation being the scalar line of dimension one and the vector three-space of dimension three, and the two subspaces being the eigenspaces of the involution with eigenvalues $+1$ and $-1$. The scalar subspace is a subalgebra, indeed the centre, closed under inversion; the vector subspace is not, its product law being $\mathbf{p}\mathbf{q} = -\langle\mathbf{p},\mathbf{q}\rangle+\mathbf{p}\times\mathbf{q}$, so that the scalar part of the product is minus the inner product and the vector part is the cross product.

The norm form is the orthogonal sum of its restrictions, $N(\tilde q) = q_0^2+|\mathbf{q}|^2$, and it is positive definite on each summand; an element of either subspace is a unit exactly when it is non-zero, the unit sphere of the vector subspace being precisely the root sphere of $-1$.

The distinguished subspace lattice of the quaternion algebra consists of these two subspaces and their trivial combinations, and there is no fuller lattice: the six-subspace lattice of the biquaternion algebra is generated by a central imaginary unit and an indefinite norm form, neither of which exists here. Complexification supplies both, and it is exactly then that the lattice grows.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra |
| $F$ | Base field of characteristic not $2$ |
| $e_0 = 1, e_1, e_2, e_3$ | Basis, $e_k^2 = -e_0$ |
| $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ | Quaternion, scalar part $q_0$, vector part $\mathbf{q}$ |
| $\bar{\tilde q} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$, $-\bar{\tilde q} = -q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ | Quaternion and vector conjugation |
| $\mathbb{R}_{\mathbb{H}} = \{\tilde q : \bar{\tilde q} = \tilde q\}$ | Scalar subspace, the centre, basis $(e_0)$ |
| $\operatorname{Im}\mathbb{H} = \{\tilde q : -\bar{\tilde q} = \tilde q\}$ | Vector subspace, basis $(e_1,e_2,e_3)$ |
| $\operatorname{Sc}(\tilde q) = \tfrac12(\tilde q+\bar{\tilde q})$ | Scalar-part projection |
| $\mathbf{q} = \tfrac12(\tilde q-\bar{\tilde q})$ | Vector-part projection |
| $N(\tilde q) = \tilde q\bar{\tilde q} = q_0^2+\lvert\mathbf{q}\rvert^2$ | Norm form, the orthogonal sum of its restrictions |
| $\langle\mathbf{p},\mathbf{q}\rangle = \sum_k p_kq_k$ | Inner product on $\operatorname{Im}\mathbb{H}$ |
| $\mathbf{p}\times\mathbf{q} = \tfrac12(\mathbf{p}\mathbf{q}-\mathbf{q}\mathbf{p})$ | Cross product on $\operatorname{Im}\mathbb{H}$ |
| $\mathbb{C}_{\mathbb{B}},\operatorname{Vect}(\mathbb{B}),\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}},\mathbb{M}_\pm$ | The six biquaternion subspaces, absent here |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original scalar–vector decomposition and the product law of vectors.
- Peter Guthrie Tait, *An Elementary Treatise on Quaternions* (Cambridge University Press, 3rd ed. 1890), for the algebraic treatment of the scalar and vector parts.
- Josiah Willard Gibbs and Edwin Bidwell Wilson, *Vector Analysis* (Scribner, 1901), for the scalar and vector products of three-dimensional vector analysis.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the eigenspace decomposition of the quaternion algebra.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the scalar–vector split and its role in the division algebras.
