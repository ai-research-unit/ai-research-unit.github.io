# __The Companion Nilpotents of the Biquaternion Algebra__

## Introduction

An idempotent $\tilde\Pi_{\mathrm{id}}$ cuts the algebra into four corners, and two of them are made of elements whose square is zero. For the biquaternion algebra at a unit real axis the two square-zero corners are one-dimensional, and the elements that span them are the **companion nilpotents**. They are the off-diagonal parts of a biquaternion written in the Peirce basis, they multiply the two idempotents into each other, and they carry the whole of the vector information that the idempotents do not carry.

This article defines the companion corner, computes the two nilpotents at an axis, gives the multiplication table of the four corners, writes the Peirce coordinates of a general element, and gives the linear functional that governs the products in the corner where the idempotent sits.

The idempotents are *The Minimal Left Ideals of the Biquaternion Algebra* and *The Square Roots of One and the Idempotents of the Biquaternion Algebra*; the Peirce decomposition in general is *Peirce Decompositions of the Biquaternion Algebra*; the basis adapted to a pair of idempotents is *The Peirce Basis of a Peirce Decomposition of the Biquaternion Algebra*; and the reading of a general element in that basis is *The Special Decomposition of a Biquaternion under a Peirce Basis*.

Nothing below is a statement of physics. The axis $\vec u$ is a unit real vector, $\vec a,\vec b$ complete it to a right-handed orthonormal triple, and the elements are written $\tilde Q$ with coefficients $Q_t,Q_x,Q_y,Q_z$.

## The Companion Corner

**Definition (the corners).** Let $\tilde\Pi_{\mathrm{id}}$ be an idempotent with complement $\tilde\Pi_{\mathrm{id}}'=e_t-\tilde\Pi_{\mathrm{id}}$. The **Peirce corners** of $\tilde\Pi_{\mathrm{id}}$ are the four subspaces

$$
\tilde\Pi_{\mathrm{id}}\mathbb{B}\tilde\Pi_{\mathrm{id}},\qquad \tilde\Pi_{\mathrm{id}}\mathbb{B}\tilde\Pi_{\mathrm{id}}',\qquad \tilde\Pi_{\mathrm{id}}'\mathbb{B}\tilde\Pi_{\mathrm{id}},\qquad \tilde\Pi_{\mathrm{id}}'\mathbb{B}\tilde\Pi_{\mathrm{id}}',
$$

and the **companion corner** of $\tilde\Pi_{\mathrm{id}}$ is $\tilde\Pi_{\mathrm{id}}'\mathbb{B}\tilde\Pi_{\mathrm{id}}$, the part that a left multiplication by $\tilde\Pi_{\mathrm{id}}$ kills and a right multiplication by $\tilde\Pi_{\mathrm{id}}$ keeps.

**Proposition (the corners are square-zero off the diagonal).** If $x\in\tilde\Pi_{\mathrm{id}}\mathbb{B}\tilde\Pi_{\mathrm{id}}'$ then $x^{2}=0$; likewise for $x\in\tilde\Pi_{\mathrm{id}}'\mathbb{B}\tilde\Pi_{\mathrm{id}}$. The two diagonal corners are subalgebras with units $\tilde\Pi_{\mathrm{id}}$ and $\tilde\Pi_{\mathrm{id}}'$.

*Proof.* For $x=\tilde\Pi_{\mathrm{id}} a\tilde\Pi_{\mathrm{id}}'$ one has $x^{2}=\tilde\Pi_{\mathrm{id}} a\tilde\Pi_{\mathrm{id}}'\tilde\Pi_{\mathrm{id}} a\tilde\Pi_{\mathrm{id}}'=0$ because $\tilde\Pi_{\mathrm{id}}'\tilde\Pi_{\mathrm{id}}=0$. A diagonal corner is closed because $\tilde\Pi_{\mathrm{id}} a\tilde\Pi_{\mathrm{id}}\tilde\Pi_{\mathrm{id}} b\tilde\Pi_{\mathrm{id}}=\tilde\Pi_{\mathrm{id}}(ab)\tilde\Pi_{\mathrm{id}}$, and $\tilde\Pi_{\mathrm{id}}$ is its unit.

**Definition (companion nilpotent).** A **companion nilpotent** of the idempotent $\tilde\Pi_{\mathrm{id}}$ is a nonzero element of one of the two square-zero corners.

**Remark (why the name).** The nilpotent is the companion of the idempotent in the following sense: the idempotent names a line, the nilpotent names the direction in which the line is deformed, and together they generate a two-dimensional algebra of matrices, the corner $\tilde\Pi_{\mathrm{id}}\mathbb{B}\tilde\Pi_{\mathrm{id}}$ plus the nilpotent and its conjugate. The pair is the smallest Peirce datum the algebra admits.

## The Two Nilpotents at an Axis

**Definition.** For a unit real $\vec u$ and the idempotents $\tilde\Pi_{\mathrm{id},\pm}(\vec u)=\tfrac12(e_t\pm i\vec u)$,

$$
\vec\Pi_{\mathrm{nil},-+}(\vec u)=\tfrac12\bigl(i\vec a+\vec b\bigr),\qquad
\vec\Pi_{\mathrm{nil},+-}(\vec u)=\tfrac12\bigl(i\vec a-\vec b\bigr),
$$

where $\vec a,\vec b$ are unit real vectors completing $\vec u$ to a right-handed orthonormal triple.

**Proposition (the four relations).**

$$
\vec\Pi_{\mathrm{nil},-+}^{2}=0,\qquad \vec\Pi_{\mathrm{nil},+-}^{2}=0,\qquad
\vec\Pi_{\mathrm{nil},-+}\vec\Pi_{\mathrm{nil},+-}=\tilde\Pi_{\mathrm{id},-},\qquad
\vec\Pi_{\mathrm{nil},+-}\vec\Pi_{\mathrm{nil},-+}=\tilde\Pi_{\mathrm{id},+}.
$$

*Proof.* Write $\vec\Pi_{\mathrm{nil},-+}=\tfrac12(i\vec a+\vec b)$ and square, using $\vec a^{2}=\vec b^{2}=-e_t$ and $\vec a\vec b+\vec b\vec a=0$ for orthogonal vectors: the two cross terms cancel and the two squares sum to zero. For the products, $\vec\Pi_{\mathrm{nil},-+}\vec\Pi_{\mathrm{nil},+-}=\tfrac14(i\vec a+\vec b)(i\vec a-\vec b)=\tfrac14\bigl(2e_t-i[\vec a,\vec b]\bigr)$, and $[\vec a,\vec b]=2\vec u$ for a right-handed orthonormal triple, so the product is $\tfrac12(e_t-i\vec u)=\tilde\Pi_{\mathrm{id},-}$. The other order reverses the sign of the bracket and gives $\tilde\Pi_{\mathrm{id},+}$.

**Example (the model pair).** At $\vec u=\vec e_z$,

$$
\tilde\Pi_{\mathrm{id},+}=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
\tilde\Pi_{\mathrm{id},-}=\begin{pmatrix}0&0\\0&1\end{pmatrix},\quad
\vec\Pi_{\mathrm{nil},-+}=\begin{pmatrix}0&0\\1&0\end{pmatrix},\quad
\vec\Pi_{\mathrm{nil},+-}=\begin{pmatrix}0&1\\0&0\end{pmatrix},
$$

the four matrix units of $M_2(\mathbb{C})$ in the Pauli representation.

**Remark (the nilpotents are not in the ideals they generate).** $\vec\Pi_{\mathrm{nil},+-}$ lies in $S_{-}=\mathbb{B}\tilde\Pi_{\mathrm{id},-}$ and $\vec\Pi_{\mathrm{nil},-+}$ lies in $S_{+}=\mathbb{B}\tilde\Pi_{\mathrm{id},+}$; the two nilpotents are the second vector of the two bases of *The Minimal Left Ideals of the Biquaternion Algebra*, and neither is a multiple of an idempotent.

**Remark (the isotropic reading).** The four elements $\tilde\Pi_{\mathrm{id},+},\vec\Pi_{\mathrm{nil},-+},\vec\Pi_{\mathrm{nil},+-},\tilde\Pi_{\mathrm{id},-}$ all have vanishing norm, since each is a rank-one matrix in the model and the norm is the determinant; the two nilpotents are nilpotent in the algebra itself, $(\cdot)^{2}=0$, while the two idempotents are not. The isotropic cone therefore contains the whole Peirce basis, and the nilpotency separates the two pairs inside it.

## The Multiplication Table of the Four Corners

**Theorem.** At the axis $\vec u$, with the basis ordered $\tilde\Pi_{\mathrm{id},+},\vec\Pi_{\mathrm{nil},-+},\vec\Pi_{\mathrm{nil},+-},\tilde\Pi_{\mathrm{id},-}$, the multiplication is

| $\cdot$ | $\tilde\Pi_{\mathrm{id},+}$ | $\vec\Pi_{\mathrm{nil},-+}$ | $\vec\Pi_{\mathrm{nil},+-}$ | $\tilde\Pi_{\mathrm{id},-}$ |
|---|---|---|---|---|
| $\tilde\Pi_{\mathrm{id},+}$ | $\tilde\Pi_{\mathrm{id},+}$ | $0$ | $\vec\Pi_{\mathrm{nil},+-}$ | $0$ |
| $\vec\Pi_{\mathrm{nil},-+}$ | $\vec\Pi_{\mathrm{nil},-+}$ | $0$ | $\tilde\Pi_{\mathrm{id},-}$ | $0$ |
| $\vec\Pi_{\mathrm{nil},+-}$ | $0$ | $\tilde\Pi_{\mathrm{id},+}$ | $0$ | $\vec\Pi_{\mathrm{nil},+-}$ |
| $\tilde\Pi_{\mathrm{id},-}$ | $0$ | $\vec\Pi_{\mathrm{nil},-+}$ | $0$ | $\tilde\Pi_{\mathrm{id},-}$ |

*Proof.* Read off the matrix units of the model, or compute from the relation $\tilde\Pi_{\mathrm{id},+}\vec e_k\tilde\Pi_{\mathrm{id},+}=\lambda_k\tilde\Pi_{\mathrm{id},+}$ and the definition of the nilpotents. Each row and each column has one nonzero entry in each diagonal corner and one in an off-diagonal corner, which is the Peirce rule.

**Corollary (the four corners).** $\tilde\Pi_{\mathrm{id},+}\mathbb{B}\tilde\Pi_{\mathrm{id},+}=\mathbb{C}\tilde\Pi_{\mathrm{id},+}$, $\tilde\Pi_{\mathrm{id},-}\mathbb{B}\tilde\Pi_{\mathrm{id},-}=\mathbb{C}\tilde\Pi_{\mathrm{id},-}$, $\tilde\Pi_{\mathrm{id},+}\mathbb{B}\tilde\Pi_{\mathrm{id},-}=\mathbb{C}\vec\Pi_{\mathrm{nil},+-}$, $\tilde\Pi_{\mathrm{id},-}\mathbb{B}\tilde\Pi_{\mathrm{id},+}=\mathbb{C}\vec\Pi_{\mathrm{nil},-+}$: four complex lines, that is four complex dimensions and eight real ones, which is the dimension of the algebra.

**Remark (the table is the matrix algebra).** The table is the table of the four matrix units of $M_2(\mathbb{C})$, written in a basis adapted to the axis. The biquaternion algebra is a full matrix algebra, and the Peirce basis at a real axis is exactly the basis of units; that is the content of the corollary.

**Remark (what the nilpotents do to the vector part).** The two vectors transverse to the axis are carried by the nilpotents and the axis direction by the idempotents:

$$
\vec e_x=-i\vec\Pi_{\mathrm{nil},-+}-i\vec\Pi_{\mathrm{nil},+-},\qquad
\vec e_y=\vec\Pi_{\mathrm{nil},-+}-\vec\Pi_{\mathrm{nil},+-},\qquad
\vec e_z=-i\tilde\Pi_{\mathrm{id},+}+i\tilde\Pi_{\mathrm{id},-},
$$

so the two vector directions transverse to the axis are carried by the nilpotents and the axis direction by the idempotents.

## Peirce Coordinates

**Theorem (the coordinates).** Every biquaternion has the unique expansion

$$
\tilde Q=\bigl(Q_t-iQ_z\bigr)\tilde\Pi_{\mathrm{id},+}+\bigl(-iQ_x+Q_y\bigr)\vec\Pi_{\mathrm{nil},-+}+\bigl(-iQ_x-Q_y\bigr)\vec\Pi_{\mathrm{nil},+-}+\bigl(Q_t+iQ_z\bigr)\tilde\Pi_{\mathrm{id},-}.
$$

*Proof.* The four basis elements $e_t,\vec e_x,\vec e_y,\vec e_z$ expand with the coefficients

$$
e_t=\tilde\Pi_{\mathrm{id},+}+\tilde\Pi_{\mathrm{id},-},\quad
\vec e_x=-i\vec\Pi_{\mathrm{nil},-+}-i\vec\Pi_{\mathrm{nil},+-},\quad
\vec e_y=\vec\Pi_{\mathrm{nil},-+}-\vec\Pi_{\mathrm{nil},+-},\quad
\vec e_z=-i\tilde\Pi_{\mathrm{id},+}+i\tilde\Pi_{\mathrm{id},-},
$$

and the expansion of a linear combination is the linear combination of the expansions; uniqueness is the independence of the four Peirce elements.

**Corollary (the Peirce components).** With the notation $\tilde Q_{++},\tilde Q_{-+},\tilde Q_{+-},\tilde Q_{--}$ for the four coefficients, $\tilde Q_{++}=Q_t-iQ_z$ and $\tilde Q_{--}=Q_t+iQ_z$ depend only on the scalar part and the axial component, while $\tilde Q_{-+}=-iQ_x+Q_y$ and $\tilde Q_{+-}=-iQ_x-Q_y$ depend only on the two transverse components.

**Remark (what the coordinates separate).** The scalar part and the component along the axis go to the diagonal corners; the two components transverse to the axis go to the off-diagonal corners. The axis is the only direction the diagonal corners see, and the plane perpendicular to it is the only thing the nilpotents see. This is the algebraic content of the split of a four-vector into a time component, an axial component and a transverse plane.

## The Peirce Functional

**Definition.** The **Peirce functional** at the idempotent $\tilde\Pi_{\mathrm{id},+}$ is the linear map $\lambda:\mathbb{B}\to\mathbb{C}$ defined by

$$
\tilde\Pi_{\mathrm{id},+}\tilde Q\tilde\Pi_{\mathrm{id},+}=\lambda(\tilde Q)\,\tilde\Pi_{\mathrm{id},+}.
$$

**Proposition (the values).** At $\vec u=\vec e_z$,

$$
\lambda(e_t)=1,\qquad \lambda(\vec e_x)=0,\qquad \lambda(\vec e_y)=0,\qquad \lambda(\vec e_z)=-i,
$$

so that $\lambda(\tilde Q)=Q_t-iQ_z$; the functional is $\mathbb{C}$-linear, $\lambda(i\tilde Q)=i\lambda(\tilde Q)$, and its kernel is the three-dimensional complex subspace of the elements with $Q_t=iQ_z$.

*Proof.* Multiply the four basis elements on both sides by $\tilde\Pi_{\mathrm{id},+}$ and use the table; the values follow, and the linearity is the linearity of the map $\tilde Q\mapsto\tilde\Pi_{\mathrm{id},+}\tilde Q\tilde\Pi_{\mathrm{id},+}$ composed with the identification of the corner with $\mathbb{C}$.

**Proposition (the functional is not multiplicative).** $\lambda(\vec e_x\vec e_y)=\lambda(\vec e_z)=-i$, while $\lambda(\vec e_x)\lambda(\vec e_y)=0$; so $\lambda$ is not an algebra homomorphism.

*Proof.* $\vec e_x\vec e_y=\vec e_z$ and the values are those of the proposition. The failure is forced: an algebra homomorphism $\mathbb{B}\to\mathbb{C}$ would be a nontrivial two-sided ideal as its kernel, and $\mathbb{B}$ is simple.

**Proposition (the product in a corner ideal).** For $a,b\in\mathbb{B}$ and an idempotent $\tilde\Pi_{\mathrm{id}}$,

$$
a\tilde\Pi_{\mathrm{id}}\cdot b\tilde\Pi_{\mathrm{id}}=\lambda_{\tilde\Pi_{\mathrm{id}}}(b)\,a\tilde\Pi_{\mathrm{id}} .
$$

*Proof.* $a\tilde\Pi_{\mathrm{id}} b\tilde\Pi_{\mathrm{id}}=a(\tilde\Pi_{\mathrm{id}} b\tilde\Pi_{\mathrm{id}})=\lambda_{\tilde\Pi_{\mathrm{id}}}(b)\,a\tilde\Pi_{\mathrm{id}}$; the product depends on $b$ only through the scalar $\lambda_{\tilde\Pi_{\mathrm{id}}}(b)$, and on $a$ only through the vector $a\tilde\Pi_{\mathrm{id}}$.

**Remark (what the functional governs).** Every product inside the ideal $S_{+}=\mathbb{B}\tilde\Pi_{\mathrm{id},+}$ is governed by the single functional $\lambda$, which is why the ideal, as an algebra under the product, is degenerate: the product of two elements of $S_{+}$ is again in $S_{+}$ only through the scalar $\lambda$. The commutator of two elements of $S_{+}$ is

$$
[a\tilde\Pi_{\mathrm{id}},b\tilde\Pi_{\mathrm{id}}]=\bigl(\lambda(b)a-\lambda(a)b\bigr)\tilde\Pi_{\mathrm{id}},
$$

by the same computation with the two orders subtracted; this is the formula that *The Bracket on the Peirce Ideals of the Biquaternion Algebra* uses to describe the Lie structure of the carrier.

## Summary

An idempotent of $\mathbb{B}$ has four Peirce corners; the two off-diagonal ones are square-zero, and their nonzero elements are the companion nilpotents. At a unit real axis the two nilpotents are $\vec\Pi_{\mathrm{nil},-+}=\tfrac12(i\vec a+\vec b)$ and $\vec\Pi_{\mathrm{nil},+-}=\tfrac12(i\vec a-\vec b)$, they satisfy $\vec\Pi_{\mathrm{nil},-+}^{2}=\vec\Pi_{\mathrm{nil},+-}^{2}=0$, $\vec\Pi_{\mathrm{nil},-+}\vec\Pi_{\mathrm{nil},+-}=\tilde\Pi_{\mathrm{id},-}$ and $\vec\Pi_{\mathrm{nil},+-}\vec\Pi_{\mathrm{nil},-+}=\tilde\Pi_{\mathrm{id},+}$, and with the two idempotents they form the four matrix units of the algebra in the Peirce basis.

Every biquaternion has a unique Peirce expansion, with the scalar part and the axial component in the diagonal corners and the two transverse components in the off-diagonal ones. The products inside a corner ideal are governed by the Peirce functional $\lambda(\tilde Q)=Q_t-iQ_z$, a complex-linear functional that is not multiplicative, and its failure to be multiplicative is the simplicity of the algebra.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\Pi_{\mathrm{id},\pm}(\vec u)$ | the idempotents at the axis $\vec u$ |
| $\tilde\Pi_{\mathrm{id}}'=e_t-\tilde\Pi_{\mathrm{id}}$ | the complementary idempotent |
| $\tilde\Pi_{\mathrm{id}}\mathbb{B}\tilde\Pi_{\mathrm{id}}'$ | a square-zero corner, the companion corner of $\tilde\Pi_{\mathrm{id}}$ |
| $\vec\Pi_{\mathrm{nil},-+},\vec\Pi_{\mathrm{nil},+-}$ | the companion nilpotents at the axis |
| $\vec a,\vec b$ | unit real vectors completing the axis to a right-handed triple |
| $\tilde Q_{++},\tilde Q_{-+},\tilde Q_{+-},\tilde Q_{--}$ | the Peirce coordinates in the four corners |
| $\lambda_{\tilde\Pi_{\mathrm{id}}}(\tilde Q)$ | the Peirce functional, defined by $\tilde\Pi_{\mathrm{id}}\tilde Q\tilde\Pi_{\mathrm{id}}=\lambda\tilde\Pi_{\mathrm{id}}$ |
| $i\tilde\Pi_{\mathrm{id},\pm}$ | the isotropic elements of the pair, $(i\tilde\Pi_{\mathrm{id},\pm})^{2}=0$ |

## Further Reading

- [The Minimal Left Ideals of the Biquaternion Algebra](the-minimal-left-ideals-of-the-biquaternion-algebra.html), for the ideals, their bases and the sphere of axes
- [From the Spin to the Carriers and the Closures](the-carriers-the-representation-the-spin-and-the-closure.html), for the ideals as carriers and for the weight of $\vec\Pi_{\mathrm{nil},-+}$
- [Peirce Decompositions of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the Peirce decomposition in the whole algebra
- [The Peirce Basis of a Peirce Decomposition of the Biquaternion Algebra](the-peirce-basis-of-the-biquaternion-algebra.html), for the basis of the four corners
- [The Special Decomposition of a Biquaternion under a Peirce Basis](the-special-decomposition-of-a-biquaternion-under-a-peirce-basis.html), for the reading of an element in that basis
- [The Square Roots of Zero and the Nilpotents of the Biquaternion Algebra](the-square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.html), for the nilpotents of the whole algebra
- [The Square Roots of One and the Idempotents of the Biquaternion Algebra](the-square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the classification of the idempotents
- [The $M_2(\mathbb{C})$ Pauli Representation](m2c-pauli-representation.html), for the matrix model in which the table is the table of matrix units
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition and the Peirce constants.
