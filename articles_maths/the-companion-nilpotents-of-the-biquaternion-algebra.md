# __The Companion Nilpotents of the Biquaternion Algebra__

## Introduction

An idempotent $\tilde\Pi$ cuts the algebra into four corners, and two of them are made of elements whose square is zero. For the biquaternion algebra at a unit real axis the two square-zero corners are one-dimensional, and the elements that span them are the **companion nilpotents**. They are the off-diagonal parts of a biquaternion written in the Peirce basis, they multiply the two idempotents into each other, and they carry the whole of the vector information that the idempotents do not carry.

This article defines the companion corner, computes the two nilpotents at an axis, gives the multiplication table of the four corners, writes the Peirce coordinates of a general element, and gives the linear functional that governs the products in the corner where the idempotent sits.

The idempotents are *The Minimal Left Ideals of the Biquaternion Algebra* and *The Square Roots of One and the Idempotents of the Biquaternion Algebra*; the Peirce decomposition in general is *Peirce Decompositions of the Biquaternion Algebra*; the basis adapted to a pair of idempotents is *The Peirce Basis of a Peirce Decomposition of the Biquaternion Algebra*; and the reading of a general element in that basis is *The Special Decomposition of a Biquaternion under a Peirce Basis*.

Nothing below is a statement of physics. The axis $\vec u$ is a unit real vector, $\vec a,\vec b$ complete it to a right-handed orthonormal triple, and the elements are written $\tilde Q$ with coefficients $Q_t,Q_x,Q_y,Q_z$.

## The Companion Corner

**Definition (the corners).** Let $\tilde\Pi$ be an idempotent with complement $\tilde\Pi'=e_t-\tilde\Pi$. The **Peirce corners** of $\tilde\Pi$ are the four subspaces

$$
\tilde\Pi\mathbb{B}\tilde\Pi,\qquad \tilde\Pi\mathbb{B}\tilde\Pi',\qquad \tilde\Pi'\mathbb{B}\tilde\Pi,\qquad \tilde\Pi'\mathbb{B}\tilde\Pi',
$$

and the **companion corner** of $\tilde\Pi$ is $\tilde\Pi'\mathbb{B}\tilde\Pi$, the part that a left multiplication by $\tilde\Pi$ kills and a right multiplication by $\tilde\Pi$ keeps.

**Proposition (the corners are square-zero off the diagonal).** If $x\in\tilde\Pi\mathbb{B}\tilde\Pi'$ then $x^{2}=0$; likewise for $x\in\tilde\Pi'\mathbb{B}\tilde\Pi$. The two diagonal corners are subalgebras with units $\tilde\Pi$ and $\tilde\Pi'$.

*Proof.* For $x=\tilde\Pi a\tilde\Pi'$ one has $x^{2}=\tilde\Pi a\tilde\Pi'\tilde\Pi a\tilde\Pi'=0$ because $\tilde\Pi'\tilde\Pi=0$. A diagonal corner is closed because $\tilde\Pi a\tilde\Pi\tilde\Pi b\tilde\Pi=\tilde\Pi(ab)\tilde\Pi$, and $\tilde\Pi$ is its unit.

**Definition (companion nilpotent).** A **companion nilpotent** of the idempotent $\tilde\Pi$ is a nonzero element of one of the two square-zero corners.

**Remark (why the name).** The nilpotent is the companion of the idempotent in the following sense: the idempotent names a line, the nilpotent names the direction in which the line is deformed, and together they generate a two-dimensional algebra of matrices, the corner $\tilde\Pi\mathbb{B}\tilde\Pi$ plus the nilpotent and its conjugate. The pair is the smallest Peirce datum the algebra admits.

## The Two Nilpotents at an Axis

**Definition.** For a unit real $\vec u$ and the idempotents $\tilde\Pi_{\pm}(\vec u)=\tfrac12(e_t\pm i\vec u)$,

$$
\vec\Upsilon_{-+}(\vec u)=\tfrac12\bigl(i\vec a+\vec b\bigr),\qquad
\vec\Upsilon_{+-}(\vec u)=\tfrac12\bigl(i\vec a-\vec b\bigr),
$$

where $\vec a,\vec b$ are unit real vectors completing $\vec u$ to a right-handed orthonormal triple.

**Proposition (the four relations).**

$$
\vec\Upsilon_{-+}^{2}=0,\qquad \vec\Upsilon_{+-}^{2}=0,\qquad
\vec\Upsilon_{-+}\vec\Upsilon_{+-}=\tilde\Pi_{-},\qquad
\vec\Upsilon_{+-}\vec\Upsilon_{-+}=\tilde\Pi_{+}.
$$

*Proof.* Write $\vec\Upsilon_{-+}=\tfrac12(i\vec a+\vec b)$ and square, using $\vec a^{2}=\vec b^{2}=-e_t$ and $\vec a\vec b+\vec b\vec a=0$ for orthogonal vectors: the two cross terms cancel and the two squares sum to zero. For the products, $\vec\Upsilon_{-+}\vec\Upsilon_{+-}=\tfrac14(i\vec a+\vec b)(i\vec a-\vec b)=\tfrac14\bigl(2e_t-i[\vec a,\vec b]\bigr)$, and $[\vec a,\vec b]=2\vec u$ for a right-handed orthonormal triple, so the product is $\tfrac12(e_t-i\vec u)=\tilde\Pi_{-}$. The other order reverses the sign of the bracket and gives $\tilde\Pi_{+}$.

**Example (the model pair).** At $\vec u=\vec e_z$,

$$
\tilde\Pi_{+}=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
\tilde\Pi_{-}=\begin{pmatrix}0&0\\0&1\end{pmatrix},\quad
\vec\Upsilon_{-+}=\begin{pmatrix}0&0\\1&0\end{pmatrix},\quad
\vec\Upsilon_{+-}=\begin{pmatrix}0&1\\0&0\end{pmatrix},
$$

the four matrix units of $M_2(\mathbb{C})$ in the Pauli representation.

**Remark (the nilpotents are not in the ideals they generate).** $\vec\Upsilon_{+-}$ lies in $S_{-}=\mathbb{B}\tilde\Pi_{-}$ and $\vec\Upsilon_{-+}$ lies in $S_{+}=\mathbb{B}\tilde\Pi_{+}$; the two nilpotents are the second vector of the two bases of *The Minimal Left Ideals of the Biquaternion Algebra*, and neither is a multiple of an idempotent.

**Remark (the isotropic reading).** The four elements $\tilde\Pi_{+},\vec\Upsilon_{-+},\vec\Upsilon_{+-},\tilde\Pi_{-}$ all have vanishing norm, since each is a rank-one matrix in the model and the norm is the determinant; the two nilpotents are nilpotent in the algebra itself, $(\cdot)^{2}=0$, while the two idempotents are not. The isotropic cone therefore contains the whole Peirce basis, and the nilpotency separates the two pairs inside it.

## The Multiplication Table of the Four Corners

**Theorem.** At the axis $\vec u$, with the basis ordered $\tilde\Pi_{+},\vec\Upsilon_{-+},\vec\Upsilon_{+-},\tilde\Pi_{-}$, the multiplication is

| $\cdot$ | $\tilde\Pi_{+}$ | $\vec\Upsilon_{-+}$ | $\vec\Upsilon_{+-}$ | $\tilde\Pi_{-}$ |
|---|---|---|---|---|
| $\tilde\Pi_{+}$ | $\tilde\Pi_{+}$ | $0$ | $\vec\Upsilon_{+-}$ | $0$ |
| $\vec\Upsilon_{-+}$ | $\vec\Upsilon_{-+}$ | $0$ | $\tilde\Pi_{-}$ | $0$ |
| $\vec\Upsilon_{+-}$ | $0$ | $\tilde\Pi_{+}$ | $0$ | $\vec\Upsilon_{+-}$ |
| $\tilde\Pi_{-}$ | $0$ | $\vec\Upsilon_{-+}$ | $0$ | $\tilde\Pi_{-}$ |

*Proof.* Read off the matrix units of the model, or compute from the relation $\tilde\Pi_{+}\vec e_k\tilde\Pi_{+}=\lambda_k\tilde\Pi_{+}$ and the definition of the nilpotents. Each row and each column has one nonzero entry in each diagonal corner and one in an off-diagonal corner, which is the Peirce rule.

**Corollary (the four corners).** $\tilde\Pi_{+}\mathbb{B}\tilde\Pi_{+}=\mathbb{C}\tilde\Pi_{+}$, $\tilde\Pi_{-}\mathbb{B}\tilde\Pi_{-}=\mathbb{C}\tilde\Pi_{-}$, $\tilde\Pi_{+}\mathbb{B}\tilde\Pi_{-}=\mathbb{C}\vec\Upsilon_{+-}$, $\tilde\Pi_{-}\mathbb{B}\tilde\Pi_{+}=\mathbb{C}\vec\Upsilon_{-+}$: four complex lines, that is four complex dimensions and eight real ones, which is the dimension of the algebra.

**Remark (the table is the matrix algebra).** The table is the table of the four matrix units of $M_2(\mathbb{C})$, written in a basis adapted to the axis. The biquaternion algebra is a full matrix algebra, and the Peirce basis at a real axis is exactly the basis of units; that is the content of the corollary.

**Remark (what the nilpotents do to the vector part).** The two vectors transverse to the axis are carried by the nilpotents and the axis direction by the idempotents:

$$
\vec e_x=-i\vec\Upsilon_{-+}-i\vec\Upsilon_{+-},\qquad
\vec e_y=\vec\Upsilon_{-+}-\vec\Upsilon_{+-},\qquad
\vec e_z=-i\tilde\Pi_{+}+i\tilde\Pi_{-},
$$

so the two vector directions transverse to the axis are carried by the nilpotents and the axis direction by the idempotents.

## Peirce Coordinates

**Theorem (the coordinates).** Every biquaternion has the unique expansion

$$
\tilde Q=\bigl(Q_t-iQ_z\bigr)\tilde\Pi_{+}+\bigl(-iQ_x+Q_y\bigr)\vec\Upsilon_{-+}+\bigl(-iQ_x-Q_y\bigr)\vec\Upsilon_{+-}+\bigl(Q_t+iQ_z\bigr)\tilde\Pi_{-}.
$$

*Proof.* The four basis elements $e_t,\vec e_x,\vec e_y,\vec e_z$ expand with the coefficients

$$
e_t=\tilde\Pi_{+}+\tilde\Pi_{-},\quad
\vec e_x=-i\vec\Upsilon_{-+}-i\vec\Upsilon_{+-},\quad
\vec e_y=\vec\Upsilon_{-+}-\vec\Upsilon_{+-},\quad
\vec e_z=-i\tilde\Pi_{+}+i\tilde\Pi_{-},
$$

and the expansion of a linear combination is the linear combination of the expansions; uniqueness is the independence of the four Peirce elements.

**Corollary (the Peirce components).** With the notation $\tilde Q_{++},\tilde Q_{-+},\tilde Q_{+-},\tilde Q_{--}$ for the four coefficients, $\tilde Q_{++}=Q_t-iQ_z$ and $\tilde Q_{--}=Q_t+iQ_z$ depend only on the scalar part and the axial component, while $\tilde Q_{-+}=-iQ_x+Q_y$ and $\tilde Q_{+-}=-iQ_x-Q_y$ depend only on the two transverse components.

**Remark (what the coordinates separate).** The scalar part and the component along the axis go to the diagonal corners; the two components transverse to the axis go to the off-diagonal corners. The axis is the only direction the diagonal corners see, and the plane perpendicular to it is the only thing the nilpotents see. This is the algebraic content of the split of a four-vector into a time component, an axial component and a transverse plane.

## The Peirce Functional

**Definition.** The **Peirce functional** at the idempotent $\tilde\Pi_{+}$ is the linear map $\lambda:\mathbb{B}\to\mathbb{C}$ defined by

$$
\tilde\Pi_{+}\tilde Q\tilde\Pi_{+}=\lambda(\tilde Q)\,\tilde\Pi_{+}.
$$

**Proposition (the values).** At $\vec u=\vec e_z$,

$$
\lambda(e_t)=1,\qquad \lambda(\vec e_x)=0,\qquad \lambda(\vec e_y)=0,\qquad \lambda(\vec e_z)=-i,
$$

so that $\lambda(\tilde Q)=Q_t-iQ_z$; the functional is $\mathbb{C}$-linear, $\lambda(i\tilde Q)=i\lambda(\tilde Q)$, and its kernel is the three-dimensional complex subspace of the elements with $Q_t=iQ_z$.

*Proof.* Multiply the four basis elements on both sides by $\tilde\Pi_{+}$ and use the table; the values follow, and the linearity is the linearity of the map $\tilde Q\mapsto\tilde\Pi_{+}\tilde Q\tilde\Pi_{+}$ composed with the identification of the corner with $\mathbb{C}$.

**Proposition (the functional is not multiplicative).** $\lambda(\vec e_x\vec e_y)=\lambda(\vec e_z)=-i$, while $\lambda(\vec e_x)\lambda(\vec e_y)=0$; so $\lambda$ is not an algebra homomorphism.

*Proof.* $\vec e_x\vec e_y=\vec e_z$ and the values are those of the proposition. The failure is forced: an algebra homomorphism $\mathbb{B}\to\mathbb{C}$ would be a nontrivial two-sided ideal as its kernel, and $\mathbb{B}$ is simple.

**Proposition (the product in a corner ideal).** For $a,b\in\mathbb{B}$ and an idempotent $\tilde\Pi$,

$$
a\tilde\Pi\cdot b\tilde\Pi=\lambda_{\tilde\Pi}(b)\,a\tilde\Pi .
$$

*Proof.* $a\tilde\Pi b\tilde\Pi=a(\tilde\Pi b\tilde\Pi)=\lambda_{\tilde\Pi}(b)\,a\tilde\Pi$; the product depends on $b$ only through the scalar $\lambda_{\tilde\Pi}(b)$, and on $a$ only through the vector $a\tilde\Pi$.

**Remark (what the functional governs).** Every product inside the ideal $S_{+}=\mathbb{B}\tilde\Pi_{+}$ is governed by the single functional $\lambda$, which is why the ideal, as an algebra under the product, is degenerate: the product of two elements of $S_{+}$ is again in $S_{+}$ only through the scalar $\lambda$. The commutator of two elements of $S_{+}$ is

$$
[a\tilde\Pi,b\tilde\Pi]=\bigl(\lambda(b)a-\lambda(a)b\bigr)\tilde\Pi,
$$

by the same computation with the two orders subtracted; this is the formula that *The Bracket on the Peirce Ideals of the Biquaternion Algebra* uses to describe the Lie structure of the carrier.

## Summary

An idempotent of $\mathbb{B}$ has four Peirce corners; the two off-diagonal ones are square-zero, and their nonzero elements are the companion nilpotents. At a unit real axis the two nilpotents are $\vec\Upsilon_{-+}=\tfrac12(i\vec a+\vec b)$ and $\vec\Upsilon_{+-}=\tfrac12(i\vec a-\vec b)$, they satisfy $\vec\Upsilon_{-+}^{2}=\vec\Upsilon_{+-}^{2}=0$, $\vec\Upsilon_{-+}\vec\Upsilon_{+-}=\tilde\Pi_{-}$ and $\vec\Upsilon_{+-}\vec\Upsilon_{-+}=\tilde\Pi_{+}$, and with the two idempotents they form the four matrix units of the algebra in the Peirce basis.

Every biquaternion has a unique Peirce expansion, with the scalar part and the axial component in the diagonal corners and the two transverse components in the off-diagonal ones. The products inside a corner ideal are governed by the Peirce functional $\lambda(\tilde Q)=Q_t-iQ_z$, a complex-linear functional that is not multiplicative, and its failure to be multiplicative is the simplicity of the algebra.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\Pi_{\pm}(\vec u)$ | the idempotents at the axis $\vec u$ |
| $\tilde\Pi'=e_t-\tilde\Pi$ | the complementary idempotent |
| $\tilde\Pi\mathbb{B}\tilde\Pi'$ | a square-zero corner, the companion corner of $\tilde\Pi$ |
| $\vec\Upsilon_{-+},\vec\Upsilon_{+-}$ | the companion nilpotents at the axis |
| $\vec a,\vec b$ | unit real vectors completing the axis to a right-handed triple |
| $\tilde Q_{++},\tilde Q_{-+},\tilde Q_{+-},\tilde Q_{--}$ | the Peirce coordinates in the four corners |
| $\lambda_{\tilde\Pi}(\tilde Q)$ | the Peirce functional, defined by $\tilde\Pi\tilde Q\tilde\Pi=\lambda\tilde\Pi$ |
| $i\tilde\Pi_{\pm}$ | the isotropic elements of the pair, $(i\tilde\Pi_{\pm})^{2}=0$ |

## Further Reading

- [The Minimal Left Ideals of the Biquaternion Algebra](the-minimal-left-ideals-of-the-biquaternion-algebra.html), for the ideals, their bases and the sphere of axes
- [The Carriers of the Biquaternion Algebra](the-carriers-of-the-biquaternion-algebra.html), for the ideals as carriers
- [The Weights of a Carrier](the-weights-of-a-carrier.html), for the weight of $\vec\Upsilon_{-+}$
- [Peirce Decompositions of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the Peirce decomposition in the whole algebra
- [The Peirce Basis of a Peirce Decomposition of the Biquaternion Algebra](the-peirce-basis-of-the-biquaternion-algebra.html), for the basis of the four corners
- [The Special Decomposition of a Biquaternion under a Peirce Basis](the-special-decomposition-of-a-biquaternion-under-a-peirce-basis.html), for the reading of an element in that basis
- [The Square Roots of Zero and the Nilpotents of the Biquaternion Algebra](nilpotents.html), for the nilpotents of the whole algebra
- [The Square Roots of One and the Idempotents of the Biquaternion Algebra](idempotents.html), for the classification of the idempotents
- [The $M_2(\mathbb{C})$ Pauli Representation](m2c-pauli-representation.html), for the matrix model in which the table is the table of matrix units
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition and the Peirce constants.
