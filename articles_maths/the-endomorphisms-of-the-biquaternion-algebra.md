# __The Endomorphisms of the Biquaternion Algebra__

## Introduction

**The object.** The biquaternion algebra $\mathbb{B}$ is a complex vector space of dimension four, and its multiplication is a bilinear map $\mathbb{B}\times\mathbb{B}\to\mathbb{B}$. A third structure is easy to overlook: the complex-linear maps of $\mathbb{B}$ into itself. They form an algebra under composition, the **endomorphism algebra** $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, of complex dimension sixteen. This article opens the group and fixes that ambient object.

**The scope of the word.** Here an **endomorphism** is a $\mathbb{C}$-linear map $\mathbb{B}\to\mathbb{B}$, with no condition of preserving the product. The maps that preserve the product are the **algebra** endomorphisms; for $\mathbb{B}$ every nonzero unital one is invertible, and they form a group. The two uses of the word are separated in §*Endomorphisms of the Algebra*, and confusing them is the first trap of the subject. The article then reads the one involution of the algebra that is itself a complex-linear operator, the quaternion conjugation $D$.

**What the article does not do.** The operators produced by the multiplication itself, the left and the right regular families and their products, are the subject of *Operator Chirality on the Biquaternion Algebra* and *Operators Acting on One Side*. This article needs one display of them, the inner derivation $\tilde Qx-x\tilde Q$, and one pointer: the two summands of that display are the regular operators, and they are defined and studied there, not here. The matrix form of the ambient space is the subject of *Matrix Representations Conventions*; this article states the dimension and leaves the matrix to the article that fixes the frame.

**Boundaries.** The algebra, its basis and its multiplication are *The Biquaternion Algebra*; the matrix model $\mathbb{B}\cong M_2(\mathbb{C})$ is *$M_2(\mathbb{C})$ Pauli Representation*; the ambient operator space in general is *The Operators on an Algebra*; the regular representations are *The Regular Representation as an Algebra of Operators*. The article is pure algebra: no bilinear form, no topology and no norm enters, and every dimension it states is qualified by its field.

## The Carrier and Its Linear Maps

### The Coordinate Column of an Element

**The carrier.** The **carrier** of the biquaternion algebra is the underlying complex vector space of $\mathbb{B}$, with basis

$$
e_t,\ \vec e_x,\ \vec e_y,\ \vec e_z ,
$$

in the order $(t,x,y,z)$. An element is $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, and its **coordinate column** is $(Q_t,Q_x,Q_y,Q_z)^{\mathsf T}\in\mathbb{C}^4$. The carrier is $\mathbb{C}^4$; the algebra is the carrier with its multiplication added.

**A map is read on the coordinates.** A complex-linear map $F:\mathbb{B}\to\mathbb{B}$ is determined by its four values $F(e_t)$, $F(\vec e_x)$, $F(\vec e_y)$ and $F(\vec e_z)$, and each value is a coordinate column. The map is therefore determined by four columns, and every choice of four columns defines one and only one map. This is the whole content of the dimension count below, and it is why the matrix of a map, once a basis is fixed, has the images as its columns.

**Two conventions of writing.** The basis is the coefficient basis and the order is fixed; another frame gives another coordinate column, and a statement about a map is a statement independent of the frame. The elements carry the tilde and the operators do not: an operator is a map, and a map has no scalar part.

### The Sixteen Complex Dimensions

**Definition (operator).** An **operator** on $\mathbb{B}$ is a map $F:\mathbb{B}\to\mathbb{B}$ that is complex-linear,

$$
F(x+\lambda y)=F(x)+\lambda F(y)
$$

for all $x,y\in\mathbb{B}$ and all $\lambda\in\mathbb{C}$. The operators form the **endomorphism algebra** $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ under addition and composition, with the identity map as unit.

**Proposition (dimension).** $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ has complex dimension $16$.

*Proof.* A linear map is determined by the four images $F(e_t),F(\vec e_x),F(\vec e_y),F(\vec e_z)$, and each image has four complex coordinates. The data are therefore $4\times4=16$ complex numbers, and every choice of them defines one and only one linear map.

**The algebra structure.** Addition is pointwise and the product is composition. The unit is the identity map. The algebra is not commutative and it is not a division algebra: it contains the zero map and the projections. Its centre is the scalar maps, because a map commuting with every operator is a scalar multiple of the identity.

**The matrix form, stated and not developed.** A basis of the carrier turns each operator into a $4\times4$ complex matrix, and the algebra into $M_4(\mathbb{C})$. The assignment depends on the basis, and the frame is part of the display. The definition of the matrix, the change of frame and the invariants are *Matrix Representations Conventions*, which stands in §*Conventions in Mathematics* ahead of this article; here only the existence of the identification is used.

**The invariants are basis-free.** The trace, the determinant, the characteristic polynomial, the spectrum and the rank of an operator are those of any of its matrices, and the change of frame leaves them unchanged. They are therefore statements about the operator and not about the display, and the articles that use them say so once.

### The Real and the Complex Reading

**The base field is part of the data.** Read as a real algebra, $\mathbb{B}$ has real dimension $8$, and $\operatorname{End}_{\mathbb{R}}(\mathbb{B})\cong M_8(\mathbb{R})$ has real dimension $64$. The complex-linear maps form a real subspace of dimension $32$, cut out by the real structure $J$, the multiplication by $i$:

$$
\operatorname{End}_{\mathbb{C}}(\mathbb{B})=\{F\in\operatorname{End}_{\mathbb{R}}(\mathbb{B}):FJ=JF\}.
$$

**The three marks, read on the field.** The coefficient conjugation $\bar{\cdot}$ and the Hermitian conjugation ${}^{*}$ conjugate the complex coefficients, so they are **conjugate-linear** and lie in $\operatorname{End}_{\mathbb{R}}(\mathbb{B})\setminus\operatorname{End}_{\mathbb{C}}(\mathbb{B})$. The quaternion conjugation ${}^{\natural}$ fixes the coefficients and changes the sign of the three vector units, so it is $\mathbb{C}$-linear and lies in $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, although it is an anti-automorphism and not an algebra endomorphism.

**The consequence for the operator articles.** An operator statement that uses $\bar{\cdot}$ or ${}^{*}$ is a real-linear statement, even when the carrier is written over $\mathbb{C}$. In particular the four adjoints of *Adjoint Pair of $L$ and $R$ Operators* are not all complex-linear: the plain and the quaternionic adjoints are, and the Hermitian and the Krein adjoints are not. The distinction is not a defect of the notation; it records which conjugation each adjoint carries.

**Every dimension carries its field.** A dimension written without its field is not written in this Part. The complex dimension of the ambient space is $16$ and its real dimension is $32$; the real endomorphism algebra has real dimension $64$. The three numbers answer three different questions, and no one of them substitutes for another.

## Endomorphisms of the Algebra

### The Automorphism Group

**Definition (algebra endomorphism).** An **algebra endomorphism** of $\mathbb{B}$ is a complex-linear map $F$ with

$$
F(xy)=F(x)F(y),\qquad F(e_t)=e_t .
$$

The second condition is unitality. The algebra endomorphisms that are bijective form the **automorphism group** $\operatorname{Aut}_{\mathbb{C}}(\mathbb{B})$.

**Theorem (every nonzero algebra endomorphism is an automorphism).** Let $F:\mathbb{B}\to\mathbb{B}$ be a nonzero unital algebra endomorphism. Then $F$ is bijective.

*Proof.* The kernel of $F$ is a two-sided ideal of $\mathbb{B}$. The algebra is simple, so the kernel is $0$ or $\mathbb{B}$. It is not $\mathbb{B}$, because $F(e_t)=e_t\neq0$. Hence $F$ is injective, and an injective linear map of a finite-dimensional space to itself is bijective.

**Theorem (the automorphism group).** $\operatorname{Aut}_{\mathbb{C}}(\mathbb{B})\cong PGL_2(\mathbb{C})$, of complex dimension $3$.

*Proof.* Fix an isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$. Every automorphism of a central simple algebra is inner, by the Skolem–Noether theorem, so it has the form $x\mapsto uxu^{-1}$ for a unit $u$. The units that give the identity are the central ones, $\mathbb{C}^{\times}\mathrm{I}_2$. Hence the group is $GL_2(\mathbb{C})/\mathbb{C}^{\times}\cong PGL_2(\mathbb{C})$, of complex dimension $4-1=3$.

**A group, not a subspace.** The automorphisms are cut out by a condition quadratic in the operator, so they form a group and not a subspace: the sum of two automorphisms is generally not an automorphism. The complex dimension three is that of the group, and it agrees with the dimension of its tangent space at the identity, computed in the next subsection.

**What an automorphism preserves.** An automorphism preserves the product, the unit and every verbal property of the algebra. It does not preserve a form, a conjugation or a norm, because none of them is part of the algebra structure. The inner automorphisms are written $\operatorname{Ad}_u$ with $\operatorname{Ad}_u(x)=uxu^{-1}$, and the kernel of $u\mapsto\operatorname{Ad}_u$ is the centre.

### The Derivations

**Definition (derivation).** A **derivation** of $\mathbb{B}$ is a complex-linear map $\delta$ with the Leibniz rule

$$
\delta(xy)=\delta(x)y+x\,\delta(y).
$$

The derivations form a subspace $\operatorname{Der}_{\mathbb{C}}(\mathbb{B})$ of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$.

**Proposition (the derivations are the inner ones).** Every derivation of $\mathbb{B}$ is inner,

$$
\delta=\operatorname{ad}_{\tilde Q},\qquad \operatorname{ad}_{\tilde Q}(x)=\tilde Qx-x\tilde Q ,
$$

and $\operatorname{ad}_{\tilde Q}=0$ exactly when $\tilde Q$ is central. Hence $\operatorname{Der}_{\mathbb{C}}(\mathbb{B})\cong\mathbb{B}/\mathbb{C}e_t$, of complex dimension $3$.

*Proof.* The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is central simple, so every derivation is inner; this is the standard theorem for central simple algebras. The kernel of $\tilde Q\mapsto\operatorname{ad}_{\tilde Q}$ is the centre $\mathbb{C}e_t$, by definition of the centre. The complex dimension is $4-1=3$.

**The one display of the regular operators.** The display above is the only place in this article where the regular operators occur, and only through their difference: $\operatorname{ad}_{\tilde Q}(x)=\tilde Qx-x\tilde Q$. The first summand is the left regular operator and the second the right one. They are defined and their laws are proved in *Operators Acting on One Side*, and their matrices are computed in the two matrix articles; this article uses them only to name the inner derivations, and the identity $\operatorname{ad}_{\tilde Q}=L_{\tilde Q}-R_{\tilde Q}$ is their definition there, not a new object here.

**A subspace, against a group.** The derivations are cut out by a condition linear in the operator, so they form a subspace of complex dimension three. The automorphisms are cut out by a condition quadratic in the operator, so they form a group and not a subspace. The two dimensions agree because the derivations are the tangent space of the group at the identity; the general rule is *The Operators on an Algebra*, read on $\mathbb{B}$.

## The Quaternion Conjugation

### D as an Anti-Automorphism

**Definition.** The **quaternion conjugation** is the complex-linear map

$$
D:\mathbb{B}\longrightarrow\mathbb{B},\qquad D(x)=x^{\natural}=x_te_t-x_x\vec e_x-x_y\vec e_y-x_z\vec e_z .
$$

**Proposition.** $D$ is a $\mathbb{C}$-linear involution, $D^2=\mathrm{id}$, and an anti-automorphism, $D(xy)=D(y)D(x)$. Its matrix in the coefficient basis is $\operatorname{diag}(1,-1,-1,-1)$, so its trace is $-2$ and its determinant $-1$. It is not an algebra endomorphism.

*Proof.* Linearity and the square are read on the basis: $D$ fixes $e_t$ and changes the sign of the three vector units. The anti-automorphism is the standard property of the quaternion conjugation, extended by $\mathbb{C}$-linearity. Multiplicativity fails on the first pair of units: $\vec e_x\vec e_y=\vec e_z$, so $D(\vec e_x\vec e_y)=-\vec e_z$, while $D(\vec e_x)D(\vec e_y)=(-\vec e_x)(-\vec e_y)=\vec e_z$.

**An element of the ambient algebra, not of the group.** $D$ is $\mathbb{C}$-linear, so it is an element of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, and it is invertible, with inverse itself. It is not in $\operatorname{Aut}_{\mathbb{C}}(\mathbb{B})$, because it reverses the product. It is therefore the one conjugation of the algebra that lives inside the complex operator algebra, and the reason the corpus can read it as an operator without leaving the complex-linear layer.

**What it is not.** $D$ is not a left or a right multiplication. It fixes the unit and reverses the vector part, and a multiplication by a central scalar does neither. The point matters in §*The Exchange $S$* of *Operators Acting on One Side*, where the two regular families are exchanged: the exchange is not $D$ but the involution that fixes the two idempotents and swaps the two mixed Peirce units, and it reverses one vector unit where $D$ reverses three.

### The Conjugate-Linear Maps Outside End_C(B)

**The two conjugate-linear conjugations.** The coefficient conjugation $\bar{\cdot}$ and the Hermitian conjugation ${}^{*}$ act on the coefficients, so they are conjugate-linear and lie outside $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$. They are real-linear operators of the carrier, of real dimension eight, and they are not elements of the complex operator algebra. The star is the composite of the bar and the quaternion sign, ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, so the two conjugate-linear maps differ by $D$.

**Their fixed spaces.** The bar fixes the elements with real coefficients, the real quaternions $\mathbb{H}$; the star fixes the Hermitian subspace $\mathbb{B}_{\Psi}$. The two fixed spaces are not the same, and neither is a complex subspace of $\mathbb{B}$: a conjugate-linear map has a real fixed space, and the complex structure carries it to the anti-fixed space. The quaternion conjugation $D$ is complex-linear, so its fixed space is complex: it is the centre $\mathbb{C}e_t$.

**Why the distinction is kept.** An operator built with the bar or the star is a real-linear operator, and a statement about it is a statement over $\mathbb{R}$. An operator built with the quaternion sign is complex-linear, and a statement about it is a statement over $\mathbb{C}$. The four adjoints of *Adjoint Pair of $L$ and $R$ Operators* separate along this line: the plain and the quaternionic adjoints are complex-linear, the Hermitian and the Krein adjoints are conjugate-linear. Writing a dagger over the distinction, as *Operator and Calculus Conventions* records, does not make the four one.

## Summary

The ambient object of the group is $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, the complex-linear maps of the carrier into itself. It has complex dimension $16$, and a choice of basis identifies it with $M_4(\mathbb{C})$; the identification depends on the basis, and the trace, the determinant, the spectrum and the rank do not. Read over the reals the carrier has dimension $8$, the real endomorphism algebra has real dimension $64$, and the complex-linear maps form the real subspace of dimension $32$ that commutes with the multiplication by $i$.

Inside the ambient algebra the article separates three objects. The **automorphisms** are the bijective multiplicative maps; every nonzero unital algebra endomorphism is one, and the group is $PGL_2(\mathbb{C})$, of complex dimension $3$. The **derivations** are the maps with the Leibniz rule; every one is inner, $\operatorname{ad}_{\tilde Q}(x)=\tilde Qx-x\tilde Q$, and they form a subspace of complex dimension $3$. The two dimensions agree because the derivations are the tangent space of the group at the identity, but one object is a subspace and the other a group.

The **quaternion conjugation** $D$ is the one conjugation that is complex-linear. It is an involution and an anti-automorphism, of matrix $\operatorname{diag}(1,-1,-1,-1)$, trace $-2$ and determinant $-1$; it lies in the ambient algebra and not in the automorphism group. The coefficient bar and the Hermitian star are conjugate-linear, so they lie outside the ambient algebra and every statement that uses them is real-linear. The four adjoints of the corpus separate along that line.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra, complex dimension $4$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | The coefficient basis |
| $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ | The complex-linear operators, complex dimension $16$ |
| $\operatorname{End}_{\mathbb{R}}(\mathbb{B})$ | The real-linear operators, real dimension $64$ |
| $\operatorname{Aut}_{\mathbb{C}}(\mathbb{B})$ | The automorphism group, $PGL_2(\mathbb{C})$, complex dimension $3$ |
| $\operatorname{Der}_{\mathbb{C}}(\mathbb{B})$ | The derivations, complex dimension $3$ |
| $\operatorname{ad}_{\tilde Q}$ | The inner derivation, $\operatorname{ad}_{\tilde Q}(x)=\tilde Qx-x\tilde Q$ |
| $D$ | The quaternion conjugation, $\operatorname{diag}(1,-1,-1,-1)$ |
| $\bar{\cdot}$, ${}^{*}$ | The conjugate-linear conjugations |
| $\mathbb{H}$, $\mathbb{B}_{\Psi}$ | The fixed spaces of the bar and of the star |

## Further Reading

- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the algebra, its basis and its multiplication.
- [The SVD Decomposition of Endomorphisms of the Biquaternion Algebra](the-svd-decomposition-of-endomorphisms-of-the-biquaternion-algebra.html), for the shortest expression of an endomorphism as a sum of rank-one endomorphisms, the bound four, the orthogonal decomposition with weights, and the two-sided operators as a proper subfamily of the atoms.
- [The Operators on an Algebra](the-operators-on-an-algebra.html), for the ambient operator space in general and the subspace-group rule.
- [The Regular Representation as an Algebra of Operators](the-regular-representation-as-an-algebra-of-operators.html), for the regular representations and their double centraliser.
- [Matrix Representations Conventions](matrix-representations-conventions.html), for the matrix in a basis, the change of frame and the invariants.
- [Operators Acting on One Side](operators-acting-on-one-side.html), for the two summands of the display and the exchange of the two families.
- [The Derivations and the Automorphisms of $M_4(\mathbb{C})$](the-derivations-and-the-automorphisms-of-m4c.html), for the same two objects at matrix level.
- [Algebra and Element Conventions](algebra-and-element-conventions.html), for the element, the basis and the three conjugations.
- [Operator Family Conventions](operator-family-conventions.html), for the letters and the adjoint signs used in the groups that follow.
