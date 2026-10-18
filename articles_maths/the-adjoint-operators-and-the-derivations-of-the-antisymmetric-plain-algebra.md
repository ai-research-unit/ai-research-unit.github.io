# __The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra__

## Introduction

The bracket of the antisymmetric plain algebra, $\tilde Q_1\wedge\tilde Q_2=\tfrac12(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1)=\vec Q_1\times\vec Q_2$, carries two layers of operators: the **adjoint** of an element, which is its operator on the algebra, and the **derivations** of the bracket, which are the linear maps that obey the Leibniz rule. This article reads both, together with the groups and the Lie algebras they generate.

The first layer is the adjoint map. On the commutator $\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1$ of the algebra the adjoint is

$$
\operatorname{ad}_{\tilde Q_1}=[\tilde Q_1,\ \cdot\ ]=\tilde Q_1\,\cdot\,-\,\cdot\,\tilde Q_1,
$$

it vanishes on the centre and is twice the cross-product operator $\vec Q_1\times$ on the vector subspace, and its trace is zero; the version halved to the block's bracket is $\operatorname{ad}^{\wedge}_{\tilde Q_1}=\tilde Q_1\wedge\cdot=\vec Q_1\times$, and the two differ by the constant factor $2$ that separates the halved bracket from the commutator. The second layer is the Lie algebra of the derivations, which contains the adjoints as its inner part and one outer derivation, the dilation of the centre. The article then reads the automorphisms of the bracket as linear maps, with the conjugation by a unit and the central scalar as the two generators, the adjoint representation and its kernel, and the structure group of the bracket with its Lie algebra.

The bracket and its structure are used from *The Lie Algebra of the Antisymmetric Plain Algebra*, and the two-dimensional model in which the conjugations are read is *Introduction to the Symmetric Plain Algebra*; the invariant form, through which the adjoints are skew and the Casimir is built, is *The Killing Form of the Antisymmetric Plain Algebra*; the reading of the bracket on the remarkable subspaces is *Remarkable Subspaces under the Antisymmetric Plain Algebra*. The general theory of the derivations of a Lie algebra, of the inner and outer parts and of the derivation algebra as the Lie algebra of the automorphism group is *Derivations of a Lie Algebra*; the associativity that makes $\operatorname{ad}_{\tilde Q_1}$ a derivation is *Associative Algebras*; and the skew-Hermitian case of the same operators, with the group of linear maps preserving its form, is *The Unitary Lie Algebra*. No group of matrices with a topology and no exponential map is read here: the automorphism group is read as a group of linear maps and its Lie algebra as the tangent derivations.

## The Adjoint Map

### Definition and the Two Conventions

**Definition.** For $\tilde Q_1\in\mathbb{B}$ the **adjoint** of $\tilde Q_1$ is the $\mathbb{C}$-linear endomorphism of $\mathbb{B}$

$$
\operatorname{ad}_{\tilde Q_1}(\tilde Q_3)=[\tilde Q_1,\tilde Q_3]=\tilde Q_1\tilde Q_3-\tilde Q_3\tilde Q_1,
$$

the **halved adjoint** is $\operatorname{ad}^{\wedge}_{\tilde Q_1}(\tilde Q_3)=\tilde Q_1\wedge\tilde Q_3$, and the two are related by

$$
\operatorname{ad}_{\tilde Q_1}=2\,\operatorname{ad}^{\wedge}_{\tilde Q_1},\qquad \operatorname{ad}^{\wedge}_{\tilde Q_1}=\tfrac12\operatorname{ad}_{\tilde Q_1}.
$$

**Theorem (the identity with the cross product).** For all $\tilde Q_1,\tilde Q_3$,

$$
\operatorname{ad}^{\wedge}_{\tilde Q_1}(\tilde Q_3)=\vec Q_1\times\vec Q_3,\qquad
\operatorname{ad}_{\tilde Q_1}(\tilde Q_3)=2\,(\vec Q_1\times\vec Q_3),
$$

so the halved adjoint coincides with the operator $\vec Q_1\times$ on the vector subspace and vanishes on the centre, and the adjoint is twice that operator.

*Proof.* The commutator is twice the half-difference, $[\tilde Q_1,\tilde Q_3]=2(\tilde Q_1\wedge\tilde Q_3)$, and the halved bracket is the cross product of the vector parts; both statements are *Introduction to the Antisymmetric Plain Algebra*.

**Remark (which convention is which).** The menu of the block writes $\operatorname{ad}_{\tilde Q_1}=[\tilde Q_1,\ \cdot\ ]$ for the adjoint and records that it is **twice** the operator $\vec Q_1\times$ on the vector subspace; the article writes the same, and it records the halved adjoint $\operatorname{ad}^{\wedge}_{\tilde Q_1}=\vec Q_1\times$ beside it because the block's bracket is the halved one and the Killing form of *The Killing Form of the Antisymmetric Plain Algebra* is taken with the halved adjoint, $\kappa(\tilde Q_1,\tilde Q_2)=\operatorname{Tr}(\operatorname{ad}^{\wedge}_{\tilde Q_1}\operatorname{ad}^{\wedge}_{\tilde Q_2})$. With the adjoint as fixed here the same form reads, as the complex trace of the endomorphisms of $\mathbb{B}$, $\operatorname{Tr}(\operatorname{ad}_{\tilde Q_1}\operatorname{ad}_{\tilde Q_2})=4\kappa(\tilde Q_1,\tilde Q_2)$; the factor is the factor $2$ of the halving, and the two readings are the same object. **The convention is fixed once: the adjoint of the article is $[\tilde Q_1,\cdot]$, twice $\vec Q_1\times$, and the form of the block is taken with the half of it.**

### The Vanishing on the Centre

**Theorem.** For $\tilde Q_1\in\mathbb{B}$ the following are equivalent: $\operatorname{ad}_{\tilde Q_1}=0$; $\operatorname{ad}^{\wedge}_{\tilde Q_1}=0$; $\tilde Q_1$ is central; and $\tilde Q_1\in\mathbb{C}_{\mathbb{B}}$. Hence

$$
\ker\operatorname{ad}=\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t,
$$

the centre of the algebra and of the bracket; and every adjoint annihilates the centre, $\operatorname{ad}_{\tilde Q_1}(\tilde Q_3)=0$ for $\tilde Q_3\in\mathbb{C}_{\mathbb{B}}$.

*Proof.* $\operatorname{ad}_{\tilde Q_1}=0$ exactly when $[\tilde Q_1,\tilde Q_3]=0$ for all $\tilde Q_3$, which by the cross-product formula is $\vec Q_1\times\vec Q_3=0$ for all $\vec Q_3$, forcing $\vec Q_1=0$, that is $\tilde Q_1\in\mathbb{C}e_t$. The last statement is that a central element commutes with everything, so the commutator with it is zero. This is *The Lie Algebra of the Antisymmetric Plain Algebra*, §*The Centre and the Quotient*.

**Remark.** **The kernel of the adjoint representation is the centre, and the centre is also annihilated by every adjoint**: the first is the kernel of the map $\tilde Q_1\mapsto\operatorname{ad}_{\tilde Q_1}$, the second is the common kernel of the operators on the algebra, and the two statements together say that the centre is the whole carrier of the invisibility of the bracket.

### The Matrix in the Real Basis and the Trace

**Theorem.** In the real basis $(e_t,ie_t,\vec e_x,\vec e_y,\vec e_z,i\vec e_x,i\vec e_y,i\vec e_z)$ of $\mathbb{B}$, with the centre first and the vector subspace after, the adjoint of $\vec e_x$ is the block-diagonal matrix

$$
\operatorname{ad}_{\vec e_x}=
\begin{pmatrix}
0 & & & & & & & \\
& 0 & & & & & & \\
& & 0 & 0 & 0 & 0 & 0 & 0\\
& & 0 & 0 & -2 & 0 & 0 & 0\\
& & 0 & 2 & 0 & 0 & 0 & 0\\
& & 0 & 0 & 0 & 0 & 0 & 0\\
& & 0 & 0 & 0 & 0 & 0 & -2\\
& & 0 & 0 & 0 & 0 & 2 & 0
\end{pmatrix},
$$

the two zero entries on the centre, and the $6\times6$ part the realification of the operator $2C_{\vec e_x}$ on the complex vector subspace. Its trace is zero and its rank is $4$; the same statements hold for the adjoint of every nonzero vector element, and the adjoint of every central element is zero.

*Proof.* The adjoint is twice the cross product by the vector part, and the cross product by $\vec e_x$ sends $\vec e_y\mapsto \vec e_z$, $\vec e_z\mapsto-\vec e_y$ and fixes $\vec e_x$, with the same action on $i\vec e_x,i\vec e_y,i\vec e_z$ because it is $\mathbb{C}$-linear; doubling and reading the images as columns gives the displayed block. The trace vanishes because the diagonal is zero; the rank is $4$ because the kernel is the complex plane spanned by $e_t$ and $\vec e_x$ (and its real coordinates $ie_t$, $i\vec e_x$), of real dimension four. Computed exactly on the real basis.

**Remark (the general matrix and the characteristic polynomial).** For a general vector element $\tilde Q_1$ the $6\times6$ part is the realification of the complex operator $2C_{\vec Q_1}$, whose characteristic polynomial is $\lambda(\lambda^2+4\,\vec Q_1\cdot\vec Q_1)$; the realification of a complex operator doubles each complex eigenvalue by its conjugate, so the characteristic polynomial of the $6\times6$ block is $\lambda^2(\lambda^2+4\,\vec Q_1\cdot\vec Q_1)(\lambda^2+4\,\overline{\vec Q_1\cdot\vec Q_1})$, which on the real unit directions is $\lambda^2(\lambda^2+4)^2$, with $0$ of multiplicity two and $\pm2i$ of multiplicity two each, and together with the two zero eigenvalues on the centre the adjoint on the real space has characteristic polynomial $\lambda^2$ times that. The trace is zero. The cross-product operator $C_{\vec Q_1}$ itself has characteristic polynomial $\lambda(\lambda^2+\vec Q_1\cdot\vec Q_1)$. **The trace of every adjoint vanishes, which is the first invariant of the block and the reason the Killing form is read on the adjoints and not on the operators of the multiplication.** The trace form of the multiplication operators themselves, which does not vanish, is *Two-Sided Operators on the Biquaternion Algebra*.

## The Derivations of the Block

### The Inner Derivations

**Definition.** A **derivation** of the bracket is a $\mathbb{C}$-linear map $D:\mathbb{B}\to\mathbb{B}$ with

$$
D(\tilde Q_1\wedge\tilde Q_2)=D\tilde Q_1\wedge\tilde Q_2+\tilde Q_1\wedge D\tilde Q_2
$$

for all $\tilde Q_1,\tilde Q_2$; the derivations form a Lie algebra $\operatorname{Der}(\mathfrak{g})$ under the commutator of endomorphisms. A derivation is **inner** when it is an adjoint, $D=\operatorname{ad}_{\tilde Q_1}$ for some $\tilde Q_1$.

**Theorem.** Every adjoint is a derivation, because the bracket is the half-commutator of an associative product and the associativity gives the Leibniz rule:

$$
\operatorname{ad}_{\tilde Q_1}(\tilde Q_2\wedge\tilde Q_4)
=\operatorname{ad}_{\tilde Q_1}\tilde Q_2\wedge\tilde Q_4+\tilde Q_2\wedge\operatorname{ad}_{\tilde Q_1}\tilde Q_4.
$$

The inner derivations are the adjoints of the vector subspace; the adjoints of the centre vanish, so

$$
\operatorname{Inn}(\mathfrak{g})=\{\operatorname{ad}_{\tilde Q_1}:\tilde Q_1\in\mathbb{B}\}=\{\operatorname{ad}_{\vec Q_1}:\vec Q_1\in\mathrm{Vect}(\mathbb{B})\}\cong\mathfrak{sl}(2,\mathbb{C}),
$$

of complex dimension three and real dimension six.

*Proof.* The Leibniz rule for the commutator is the associativity of the product, $\operatorname{ad}_{\tilde Q_1}(\tilde Q_2\tilde Q_4)=(\operatorname{ad}_{\tilde Q_1}\tilde Q_2)\tilde Q_4+\tilde Q_2(\operatorname{ad}_{\tilde Q_1}\tilde Q_4)$, and the halving carries it to the bracket; this is *Associative Algebras* and *Derivations of a Lie Algebra*. The inner derivations are the image of the adjoint representation, which by the previous section has kernel the centre, so its image is isomorphic to $\mathfrak{g}/\mathbb{C}_{\mathbb{B}}\cong\mathrm{Vect}(\mathbb{B})\cong\mathfrak{sl}(2,\mathbb{C})$; the isomorphism is $\operatorname{ad}_{[\,\tilde Q_1,\tilde Q_2\,]}=[\operatorname{ad}_{\tilde Q_1},\operatorname{ad}_{\tilde Q_2}]$.

**Remark.** **The inner derivations are the adjoints, and there are as many of them as the derived algebra has dimensions: three complex and six real.** The identification of the inner derivations with $\mathfrak{sl}(2,\mathbb{C})$ is the same identification as the one of the derived algebra, read through the adjoint representation; the two are the same space, one acting on the algebra and one acted upon.

### The Outer Derivations

**Theorem.** The outer derivations form a complex line, spanned by the derivation

$$
D_0:\quad D_0(e_t)=e_t,\qquad D_0(ie_t)=ie_t,\qquad D_0(\tilde Q_3)=0\ \text{ on }\ \mathrm{Vect}(\mathbb{B}),
$$

which scales the centre and annihilates the derived algebra; it is the derivation induced by the dual number $\mathbb{C}[\varepsilon]/(\varepsilon^2)$ acting on the centre in the description below. Hence

$$
\operatorname{Der}(\mathfrak{g})=\operatorname{Inn}(\mathfrak{g})\oplus\mathbb{C}D_0\cong\mathfrak{sl}(2,\mathbb{C})\oplus\mathbb{C},
$$

of complex dimension four and real dimension eight.

*Proof.* For the bracket of two vector elements the image lies in the vector subspace, on which $D_0$ vanishes, and both terms of the Leibniz rule vanish; for the bracket of a central element with anything the bracket is zero on both sides; so $D_0$ is a derivation. For the converse, a derivation preserves the centre, because the centre is the kernel of the adjoint representation and a derivation commutes with the adjoints: $D\operatorname{ad}_{\tilde Q_1}=\operatorname{ad}_{D\tilde Q_1}+\operatorname{ad}_{\tilde Q_1}D$, so an element annihilated by every adjoint is carried to an element annihilated by every adjoint. A derivation also preserves the derived algebra, by the Leibniz rule and the stability of the image. Its restriction to the simple derived algebra is an inner derivation of that algebra, $D|_{\mathrm{Vect}}=\operatorname{ad}_{\vec Q_1}$ for some vector $\vec Q_1$, by *Derivations of a Lie Algebra*, since $\mathfrak{sl}(2,\mathbb{C})$ has no outer derivation; the difference $D-\operatorname{ad}_{\vec Q_1}$ is then a derivation vanishing on the derived algebra and preserving the one-dimensional centre, so it acts on the centre by a scalar $\nu$ and is $\nu D_0$; hence every derivation is $\operatorname{ad}_{\vec Q_1}+\nu D_0$. Computed exactly on the basis.

**Remark (the derivation algebra is the tangent algebra of the automorphisms).** The dual numbers give the reason the outer derivation has dimension one: over $\mathbb{C}[\varepsilon]/(\varepsilon^2)$ the automorphism $\mathrm{id}+\varepsilon D$ of the bracket is a derivation exactly when $D$ obeys the Leibniz rule, and the derivations of the simple derived algebra are its inner ones, of dimension three, together with the derivation that scales the one-dimensional centre. **The derivation algebra is $\mathfrak{sl}(2,\mathbb{C})\oplus\mathbb{C}$, of complex dimension four.** The inner derivations are the adjoints and the outer line is the centre scaling; the general theory is *Derivations of a Lie Algebra*, and the same algebra is the Lie algebra of the group of the next section.

## The Automorphisms of the Bracket

### The Group

**Definition.** An **automorphism of the bracket** is an invertible $\mathbb{C}$-linear map $T:\mathbb{B}\to\mathbb{B}$ with

$$
T(\tilde Q_1\wedge\tilde Q_2)=T\tilde Q_1\wedge T\tilde Q_2
$$

for all $\tilde Q_1,\tilde Q_2$; the automorphisms form the group $\operatorname{Aut}(\mathfrak{g})$.

**Theorem.** Every automorphism preserves the centre and the derived algebra, and it is the direct sum of an invertible scalar on the centre and an automorphism of the derived algebra:

$$
T(\tilde Q_1)=\alpha\,Q_{1t}e_t\oplus A(\vec Q_1),\qquad \alpha\in\mathbb{C}^{\times},\qquad A\in\operatorname{Aut}\bigl(\mathrm{Vect}(\mathbb{B}),\wedge\bigr),
$$

so that

$$
\operatorname{Aut}(\mathfrak{g})\cong\mathbb{C}^{\times}\times\operatorname{Aut}\bigl(\mathrm{Vect}(\mathbb{B}),\wedge\bigr)\cong\mathbb{C}^{\times}\times PGL(2,\mathbb{C}),
$$

of complex dimension four.

*Proof.* The centre is the kernel of the adjoint representation, an intrinsic subspace, so an automorphism preserves it; the derived algebra is intrinsically $[\mathfrak{g},\mathfrak{g}]$, so it is preserved too, and it is complementary to the centre. On the centre the automorphism is an invertible scalar; on the derived algebra it is a bracket automorphism, and the automorphism group of $\mathfrak{sl}(2,\mathbb{C})$ is the adjoint group $PGL(2,\mathbb{C})=\operatorname{PSL}(2,\mathbb{C})$, of complex dimension three, acting by conjugation in the two-dimensional model, *Introduction to the Symmetric Plain Algebra*. Any pair $(\alpha,A)$ is an automorphism because the bracket never mixes the centre with the derived algebra. Computed on the basis.

### The Two Examples

**Theorem (the conjugation by a unit).** Let $\tilde U$ be invertible in $\mathbb{B}$ and put $T_{\tilde U}(\tilde Q_1)=\tilde U\tilde Q_1\tilde U^{-1}$. Then $T_{\tilde U}$ is an automorphism of the bracket, it is the identity on the centre, and on the derived algebra it is the conjugation by the image of $\tilde U$ in $PGL(2,\mathbb{C})$. The assignment descends to the group of units modulo the centre.

*Proof.* The map is invertible and multiplicative for the plain product, so it carries the commutator to the commutator and the halved bracket to the halved bracket; on the centre it is the identity because the centre commutes with $\tilde U$; the kernel of the assignment is the group of units whose conjugation is trivial, which is the centre. This is *The Lie Algebra of the Antisymmetric Plain Algebra*'s identification of the derived algebra and the models of *Introduction to the Symmetric Plain Algebra*. Computed on general units.

**Theorem (the central scalar).** For $\lambda\in\mathbb{C}^{\times}$ let $T_\lambda$ multiply the centre by $\lambda$ and fix the derived algebra. Then $T_\lambda$ is an automorphism of the bracket; $T_\lambda$ is the identity exactly for $\lambda=1$.

*Proof.* The bracket of two vector elements is a vector element and is fixed; a bracket with a central element vanishes on both sides; so the map preserves the bracket.

**Remark.** The two families generate the automorphism group: **every automorphism of the bracket is the product of a conjugation by a unit and a central scalar**, the conjugation moving the derived algebra and the central scalar moving the centre, and the two families commute because the conjugation is the identity on the centre. The Lie algebra of the automorphism group is $\operatorname{Der}(\mathfrak{g})$, as the previous section records by the dual numbers, and it is of complex dimension four.

## The Adjoint Representation

**Theorem.** The map $\operatorname{ad}:\mathfrak{g}\to\operatorname{End}(\mathbb{B})$, $\tilde Q_1\mapsto\operatorname{ad}_{\tilde Q_1}$, is a representation of the bracket,

$$
\operatorname{ad}_{[\tilde Q_1,\tilde Q_2]}=[\operatorname{ad}_{\tilde Q_1},\operatorname{ad}_{\tilde Q_2}],
\qquad\text{equivalently}\qquad
\operatorname{ad}^{\wedge}_{\tilde Q_1\wedge\tilde Q_2}=[\operatorname{ad}^{\wedge}_{\tilde Q_1},\operatorname{ad}^{\wedge}_{\tilde Q_2}],
$$

its kernel is the centre $\mathbb{C}_{\mathbb{B}}$, and its image is the Lie algebra of the inner derivations, identified with the derived algebra:

$$
\operatorname{ad}(\mathfrak{g})\cong\mathfrak{g}/\mathbb{C}_{\mathbb{B}}\cong\mathrm{Vect}(\mathbb{B})\cong\mathfrak{sl}(2,\mathbb{C}),
$$

of complex dimension three and real dimension six.

*Proof.* The identity $\operatorname{ad}_{[\,\tilde Q_1,\tilde Q_2\,]}=[\operatorname{ad}_{\tilde Q_1},\operatorname{ad}_{\tilde Q_2}]$ is the Jacobi identity, and it holds for the halved bracket with the factor carried along; the kernel is the centre by the vanishing theorem, and the image is the quotient by the kernel, which is the derived algebra by *The Lie Algebra of the Antisymmetric Plain Algebra*.

**Remark.** **The adjoint representation is faithful exactly on the derived algebra and kills exactly the centre**, and its image is the inner derivation algebra. The representation is the matrix model of the adjoints; its matrices in the real basis are the ones computed above, and their vanishing trace is the trace form of the representation.

## The Structure Group

**Definition.** A **similarity of the bracket** is an invertible $\mathbb{C}$-linear map $T$ with

$$
T(\tilde Q_1\wedge\tilde Q_2)=\lambda\,(T\tilde Q_1\wedge T\tilde Q_2)
$$

for a nonzero scalar $\lambda$ depending on $T$; the similarities form the **structure group** $\operatorname{Str}(\mathfrak{g})$.

**Theorem.** In the decomposition of an automorphism into a scalar on the centre and a linear map on the derived algebra, the similarities are the maps

$$
T=\bigl(\alpha\ \text{on the centre},\ \mu A\ \text{on the derived algebra}\bigr),\qquad \alpha,\mu\in\mathbb{C}^{\times},\ A\in PGL(2,\mathbb{C}),
$$

and the multiplier is $\lambda=1/\mu$. Hence

$$
\operatorname{Str}(\mathfrak{g})\cong\mathbb{C}^{\times}\times\mathbb{C}^{\times}\times PGL(2,\mathbb{C}),
$$

of complex dimension five; it contains the automorphism group as the subgroup $\alpha$ arbitrary, $\mu=1$.

*Proof.* For two vector elements, $T(\tilde Q_1\wedge\tilde Q_2)=\mu A(\tilde Q_1\wedge\tilde Q_2)$ and $T\tilde Q_1\wedge T\tilde Q_2=\mu^2\,(A\tilde Q_1\wedge A\tilde Q_2)=\mu^2A(\tilde Q_1\wedge\tilde Q_2)$; the multiplier is therefore $1/\mu$, independent of the elements. For a bracket with a central element both sides vanish; for two central elements both sides vanish. Conversely, a similarity preserves the centre and the derived algebra by the same intrinsic argument as an automorphism, so it has the displayed form. Computed exactly on general elements, where the identity $T(\tilde Q_1\wedge\tilde Q_2)=\mu^{-1}(T\tilde Q_1\wedge T\tilde Q_2)$ was verified for $A$ a conjugation.

**Remark (the Lie algebra of the structure group).** The structure group has the same dimension as its Lie algebra of tangent maps, and that algebra is

$$
\operatorname{Der}(\mathfrak{g})\oplus\mathbb{C}\,D_{\mathrm{dil}},
$$

where $D_{\mathrm{dil}}$ is the **dilation** of the derived algebra (the identity on $\mathrm{Vect}(\mathbb{B})$ and zero on the centre), a map that is not a derivation but obeys the infinitesimal similarity rule. **The structure group of the bracket is the automorphism group times the dilations, of complex dimension four plus one; the extra dimension is the one that scales the bracket itself.** The central scalars form the subgroup that scales only the centre, and they are already automorphisms, which is why the structure group contributes two scalar factors and the automorphism group only one.

## Worked Examples

**A central adjoint.** $\operatorname{ad}_{e_t+ie_t}=0$, because both coordinates are central: the adjoint representation kills the centre.

**A vector adjoint.** $\operatorname{ad}_{\vec e_x}(\vec e_y)=2\vec e_z$ and $\operatorname{ad}_{\vec e_x}(\vec e_z)=-2\vec e_y$: the adjoint of $\vec e_x$ is twice the cross product by $\vec e_x$, and it fixes $\vec e_x$ and the centre.

**The trace.** $\operatorname{Tr}(\operatorname{ad}_{\vec e_x})=0$ and $\operatorname{Tr}(\operatorname{ad}_{i\vec e_x})=0$: every adjoint has vanishing trace, the diagonal of the displayed matrix being zero.

**A derivation.** $\operatorname{ad}_{\vec e_z}$ sends $\vec e_x\mapsto 2\vec e_y$ and $\vec e_y\mapsto-2\vec e_x$, and it obeys the Leibniz rule on the pair $\vec e_x,\vec e_y$: $\operatorname{ad}_{\vec e_z}(\vec e_x\wedge \vec e_y)=\operatorname{ad}_{\vec e_z}\vec e_z=0$, and $\operatorname{ad}_{\vec e_z}\vec e_x\wedge \vec e_y+\vec e_x\wedge\operatorname{ad}_{\vec e_z}\vec e_y=2\vec e_y\wedge \vec e_y+\vec e_x\wedge(-2\vec e_x)=0$.

**The outer derivation.** $D_0(e_t)=e_t$ and $D_0(\vec e_x)=0$: the centre scaling, which is not inner because an inner derivation vanishes on the centre.

**The conjugation by a unit.** For $\tilde U=\vec e_x$, a unit with $\vec e_x^{-1}=-\vec e_x$, the conjugation fixes $\vec e_x$ and reverses the sign on the plane orthogonal to it: $\vec e_x\vec e_y\vec e_x^{-1}=(\vec e_x\vec e_y)(-\vec e_x)=-\vec e_z\vec e_x=-\vec e_y$, and $\vec e_x\vec e_z\vec e_x^{-1}=-\vec e_z$. It is a nontrivial automorphism of the derived algebra and the identity on the centre.

**The central scalar.** $T_\lambda(e_t)=\lambda e_t$, $T_\lambda(\vec e_x)=\vec e_x$ is an automorphism for every $\lambda\neq0$; the adjoint representation is unchanged by it, since the centre is in its kernel.

**A similarity.** $T$ that fixes the centre and multiplies the derived algebra by $\mu$ satisfies $T(\tilde Q_1\wedge\tilde Q_2)=\mu^{-1}(T\tilde Q_1\wedge T\tilde Q_2)$: the multiplier is the reciprocal of the dilation, as the theorem states.

## Summary

The adjoint of the block is $\operatorname{ad}_{\tilde Q_1}=[\tilde Q_1,\cdot]$, equal to twice the operator $\vec Q_1\times$ on the vector subspace, vanishing on the centre, of matrix block diagonal in the real basis with zeroes on the centre and the realification of $2C_{\vec Q_1}$ on the derived algebra, and of trace zero; the halved adjoint $\operatorname{ad}^{\wedge}_{\tilde Q_1}=\vec Q_1\times$ is the version of the block's own bracket, and the two differ by the factor $2$ of the halving. The adjoints are derivations, and the inner derivations are exactly the adjoints of the derived algebra, identified with $\mathfrak{sl}(2,\mathbb{C})$; the outer derivations form one complex line, spanned by the scaling of the centre, so $\operatorname{Der}(\mathfrak{g})\cong\mathfrak{sl}(2,\mathbb{C})\oplus\mathbb{C}$ has complex dimension four. The automorphisms of the bracket are the pairs of an invertible scalar on the centre and an automorphism of the derived algebra, $\operatorname{Aut}(\mathfrak{g})\cong\mathbb{C}^{\times}\times PGL(2,\mathbb{C})$, generated by the conjugation by a unit and the central scalar, with Lie algebra $\operatorname{Der}(\mathfrak{g})$. The adjoint representation has kernel the centre and image the derived algebra. The structure group of the bracket, of maps with $T(\tilde Q_1\wedge\tilde Q_2)=\lambda(T\tilde Q_1\wedge T\tilde Q_2)$, is $\mathbb{C}^{\times}\times\mathbb{C}^{\times}\times PGL(2,\mathbb{C})$, of complex dimension five, with Lie algebra the derivations together with the dilation of the derived algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{ad}_{\tilde Q_1}(\tilde Q_3)=[\tilde Q_1,\tilde Q_3]=\tilde Q_1\tilde Q_3-\tilde Q_3\tilde Q_1$ | the adjoint of the block, twice $\vec Q_1\times$ on the vector subspace |
| $\operatorname{ad}^{\wedge}_{\tilde Q_1}(\tilde Q_3)=\tilde Q_1\wedge\tilde Q_3=\vec Q_1\times\vec Q_3$ | the halved adjoint, the adjoint of the block's own bracket |
| $\ker\operatorname{ad}=\mathbb{C}_{\mathbb{B}}$ | the kernel of the adjoint representation, the centre |
| $\operatorname{Tr}\operatorname{ad}_{\tilde Q_1}=0$ | every adjoint has vanishing trace |
| $\operatorname{Der}(\mathfrak{g})$ | the derivation algebra |
| $\operatorname{Inn}(\mathfrak{g})=\operatorname{ad}(\mathrm{Vect}(\mathbb{B}))\cong\mathfrak{sl}(2,\mathbb{C})$ | the inner derivations, the adjoints |
| $D_0$ | the outer derivation scaling the centre, annihilating the derived algebra |
| $\operatorname{Der}(\mathfrak{g})\cong\mathfrak{sl}(2,\mathbb{C})\oplus\mathbb{C}$ | the derivation algebra, of complex dimension four |
| $\operatorname{Aut}(\mathfrak{g})\cong\mathbb{C}^{\times}\times PGL(2,\mathbb{C})$ | the automorphism group of the bracket |
| $T_{\tilde U}(\tilde Q_1)=\tilde U\tilde Q_1\tilde U^{-1}$; $T_\lambda$ on the centre | the conjugation by a unit and the central scalar |
| $\operatorname{Str}(\mathfrak{g})\cong\mathbb{C}^{\times}\times\mathbb{C}^{\times}\times PGL(2,\mathbb{C})$ | the structure group of the bracket, of complex dimension five |

## Further Reading

- *Introduction to the Antisymmetric Plain Algebra* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra.md`), for the bracket and the cross-product formula
- *The Lie Algebra of the Antisymmetric Plain Algebra* (`articles_maths/the-lie-algebra-of-the-antisymmetric-plain-algebra.md`), for the centre, the derived algebra, the identifications and the enveloping algebra
- *The Killing Form of the Antisymmetric Plain Algebra* (`articles_maths/the-killing-form-of-the-antisymmetric-plain-algebra.md`), for the invariant form, the radical and the Casimir element
- *Remarkable Subspaces under the Antisymmetric Plain Algebra* (`articles_maths/remarkable-subspaces-under-the-antisymmetric-plain-algebra.md`), for the bracket read on the remarkable subspaces
- *Introduction to the Symmetric Plain Algebra* (`articles_maths/introduction-to-the-symmetric-plain-algebra-of-quaternioid.md`), for the conjugations in the realization
- *Introduction to the Symmetric Plain Algebra* (`articles_maths/introduction-to-the-symmetric-plain-algebra-of-quaternioid.md`), for the conjugations in the regular model
- *Derivations of a Lie Algebra* (`articles_maths/derivations-of-a-lie-algebra.md`), for the inner and outer derivations and the derivation algebra as the Lie algebra of the automorphism group
- *Associative Algebras* (`articles_maths/associative-algebras.md`), for the associativity behind the Leibniz rule
- *Two-Sided Operators on the Biquaternion Algebra* (`articles_maths/two-sided-operators-on-the-biquaternion-algebra.md`), for the operators of the multiplication and their trace form
