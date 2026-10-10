# __The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra__

## Introduction

The bracket of the antisymmetric plain algebra, $\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf{P}\times\mathbf{Q}$, carries two layers of operators: the **adjoint** of an element, which is its operator on the algebra, and the **derivations** of the bracket, which are the linear maps that obey the Leibniz rule. This article reads both, together with the groups and the Lie algebras they generate.

The first layer is the adjoint map. On the commutator $\tilde P\tilde Q-\tilde Q\tilde P$ of the algebra the adjoint is

$$
\operatorname{ad}_{\tilde P}=[\tilde P,\ \cdot\ ]=\tilde P\,\cdot\,-\,\cdot\,\tilde P,
$$

it vanishes on the centre and is twice the cross-product operator $\mathbf{P}\times$ on the vector subspace, and its trace is zero; the version halved to the block's bracket is $\operatorname{ad}^{\wedge}_{\tilde P}=\tilde P\wedge\cdot=\mathbf{P}\times$, and the two differ by the constant factor $2$ that separates the halved bracket from the commutator. The second layer is the Lie algebra of the derivations, which contains the adjoints as its inner part and one outer derivation, the dilation of the centre. The article then reads the automorphisms of the bracket as linear maps, with the conjugation by a unit and the central scalar as the two generators, the adjoint representation and its kernel, and the structure group of the bracket with its Lie algebra.

The bracket and its structure are used from *The Lie Algebra of the Antisymmetric Plain Algebra*, and the two-dimensional model in which the conjugations are read is *The Antisymmetric Plain Algebra in the $2\times2$ and $4\times4$ Matrix Element Representations*; the invariant form, through which the adjoints are skew and the Casimir is built, is *The Killing Form of the Antisymmetric Plain Algebra*; the reading of the bracket on the remarkable subspaces is *Remarkable Subspaces under the Antisymmetric Plain Algebra of Biquaternions*. The general theory of the derivations of a Lie algebra, of the inner and outer parts and of the derivation algebra as the Lie algebra of the automorphism group is *Derivations of a Lie Algebra*; the associativity that makes $\operatorname{ad}_{\tilde P}$ a derivation is *Associative Algebras*; and the skew-Hermitian case of the same operators, with the group of linear maps preserving its form, is *The Unitary Lie Algebra*. No group of matrices with a topology and no exponential map is read here: the automorphism group is read as a group of linear maps and its Lie algebra as the tangent derivations.

## The Adjoint Map

### Definition and the Two Conventions

**Definition.** For $\tilde P\in\mathbb{B}$ the **adjoint** of $\tilde P$ is the $\mathbb{C}$-linear endomorphism of $\mathbb{B}$

$$
\operatorname{ad}_{\tilde P}(\tilde X)=[\tilde P,\tilde X]=\tilde P\tilde X-\tilde X\tilde P,
$$

the **halved adjoint** is $\operatorname{ad}^{\wedge}_{\tilde P}(\tilde X)=\tilde P\wedge\tilde X$, and the two are related by

$$
\operatorname{ad}_{\tilde P}=2\,\operatorname{ad}^{\wedge}_{\tilde P},\qquad \operatorname{ad}^{\wedge}_{\tilde P}=\tfrac12\operatorname{ad}_{\tilde P}.
$$

**Theorem (the identity with the cross product).** For all $\tilde P,\tilde X$,

$$
\operatorname{ad}^{\wedge}_{\tilde P}(\tilde X)=\mathbf{P}\times\mathbf{X},\qquad
\operatorname{ad}_{\tilde P}(\tilde X)=2\,(\mathbf{P}\times\mathbf{X}),
$$

so the halved adjoint coincides with the operator $\mathbf{P}\times$ on the vector subspace and vanishes on the centre, and the adjoint is twice that operator.

*Proof.* The commutator is twice the half-difference, $[\tilde P,\tilde X]=2(\tilde P\wedge\tilde X)$, and the halved bracket is the cross product of the vector parts; both statements are *Introduction to the Antisymmetric Plain Algebra of Biquaternions*. $\square$

**Remark (which convention is which).** The menu of the block writes $\operatorname{ad}_{\tilde P}=[\tilde P,\ \cdot\ ]$ for the adjoint and records that it is **twice** the operator $\mathbf{P}\times$ on the vector subspace; the article writes the same, and it records the halved adjoint $\operatorname{ad}^{\wedge}_{\tilde P}=\mathbf{P}\times$ beside it because the block's bracket is the halved one and the Killing form of *The Killing Form of the Antisymmetric Plain Algebra* is taken with the halved adjoint, $\kappa(\tilde P,\tilde Q)=\operatorname{Tr}(\operatorname{ad}^{\wedge}_{\tilde P}\operatorname{ad}^{\wedge}_{\tilde Q})$. With the adjoint as fixed here the same form reads, as the complex trace of the endomorphisms of $\mathbb{B}$, $\operatorname{Tr}(\operatorname{ad}_{\tilde P}\operatorname{ad}_{\tilde Q})=4\kappa(\tilde P,\tilde Q)$; the factor is the factor $2$ of the halving, and the two readings are the same object. **The convention is fixed once: the adjoint of the article is $[\tilde P,\cdot]$, twice $\mathbf{P}\times$, and the form of the block is taken with the half of it.**

### The Vanishing on the Centre

**Theorem.** For $\tilde P\in\mathbb{B}$ the following are equivalent: $\operatorname{ad}_{\tilde P}=0$; $\operatorname{ad}^{\wedge}_{\tilde P}=0$; $\tilde P$ is central; and $\tilde P\in\mathbb{C}_{\mathbb{B}}$. Hence

$$
\ker\operatorname{ad}=\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0,
$$

the centre of the algebra and of the bracket; and every adjoint annihilates the centre, $\operatorname{ad}_{\tilde P}(\tilde X)=0$ for $\tilde X\in\mathbb{C}_{\mathbb{B}}$.

*Proof.* $\operatorname{ad}_{\tilde P}=0$ exactly when $[\tilde P,\tilde X]=0$ for all $\tilde X$, which by the cross-product formula is $\mathbf{P}\times\mathbf{X}=0$ for all $\mathbf{X}$, forcing $\mathbf{P}=0$, that is $\tilde P\in\mathbb{C}e_0$. The last statement is that a central element commutes with everything, so the commutator with it is zero. This is *The Lie Algebra of the Antisymmetric Plain Algebra*, §*The Centre and the Quotient*. Verified on the basis and on general elements. $\square$

**Remark.** **The kernel of the adjoint representation is the centre, and the centre is also annihilated by every adjoint**: the first is the kernel of the map $\tilde P\mapsto\operatorname{ad}_{\tilde P}$, the second is the common kernel of the operators on the algebra, and the two statements together say that the centre is the whole carrier of the invisibility of the bracket.

### The Matrix in the Real Basis and the Trace

**Theorem.** In the real basis $(e_0,ie_0,e_1,e_2,e_3,ie_1,ie_2,ie_3)$ of $\mathbb{B}$, with the centre first and the vector subspace after, the adjoint of $e_1$ is the block-diagonal matrix

$$
\operatorname{ad}_{e_1}=
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

the two zero entries on the centre, and the $6\times6$ part the realification of the operator $2C_{e_1}$ on the complex vector subspace. Its trace is zero and its rank is $4$; the same statements hold for the adjoint of every nonzero vector element, and the adjoint of every central element is zero.

*Proof.* The adjoint is twice the cross product by the vector part, and the cross product by $e_1$ sends $e_2\mapsto e_3$, $e_3\mapsto-e_2$ and fixes $e_1$, with the same action on $ie_1,ie_2,ie_3$ because it is $\mathbb{C}$-linear; doubling and reading the images as columns gives the displayed block. The trace vanishes because the diagonal is zero; the rank is $4$ because the kernel is the complex plane spanned by $e_0$ and $e_1$ (and its real coordinates $ie_0$, $ie_1$), of real dimension four. Computed exactly on the real basis. $\square$

**Remark (the general matrix and the characteristic polynomial).** For a general vector element $\tilde P$ the $6\times6$ part is the realification of the complex operator $2C_{\mathbf{P}}$, whose characteristic polynomial is $\lambda(\lambda^2+4\,\mathbf{P}\cdot\mathbf{P})$; the realification of a complex operator doubles each complex eigenvalue by its conjugate, so the characteristic polynomial of the $6\times6$ block is $\lambda^2(\lambda^2+4\,\mathbf{P}\cdot\mathbf{P})(\lambda^2+4\,\overline{\mathbf{P}\cdot\mathbf{P}})$, which on the real unit directions is $\lambda^2(\lambda^2+4)^2$, with $0$ of multiplicity two and $\pm2i$ of multiplicity two each, and together with the two zero eigenvalues on the centre the adjoint on the real space has characteristic polynomial $\lambda^2$ times that. The trace is zero. The cross-product operator $C_{\mathbf{P}}$ itself has characteristic polynomial $\lambda(\lambda^2+\mathbf{P}\cdot\mathbf{P})$. **The trace of every adjoint vanishes, which is the first invariant of the block and the reason the Killing form is read on the adjoints and not on the operators of the multiplication.** The trace form of the multiplication operators themselves, which does not vanish, is *Two-Sided Operators on the General Plain Algebra of Biquaternions*.

## The Derivations of the Block

### The Inner Derivations

**Definition.** A **derivation** of the bracket is a $\mathbb{C}$-linear map $D:\mathbb{B}\to\mathbb{B}$ with

$$
D(\tilde P\wedge\tilde Q)=D\tilde P\wedge\tilde Q+\tilde P\wedge D\tilde Q
$$

for all $\tilde P,\tilde Q$; the derivations form a Lie algebra $\operatorname{Der}(\mathfrak{g})$ under the commutator of endomorphisms. A derivation is **inner** when it is an adjoint, $D=\operatorname{ad}_{\tilde P}$ for some $\tilde P$.

**Theorem.** Every adjoint is a derivation, because the bracket is the half-commutator of an associative product and the associativity gives the Leibniz rule:

$$
\operatorname{ad}_{\tilde P}(\tilde Q\wedge\tilde R)
=\operatorname{ad}_{\tilde P}\tilde Q\wedge\tilde R+\tilde Q\wedge\operatorname{ad}_{\tilde P}\tilde R.
$$

The inner derivations are the adjoints of the vector subspace; the adjoints of the centre vanish, so

$$
\operatorname{Inn}(\mathfrak{g})=\{\operatorname{ad}_{\tilde P}:\tilde P\in\mathbb{B}\}=\{\operatorname{ad}_{\mathbf{P}}:\mathbf{P}\in\mathrm{Vect}(\mathbb{B})\}\cong\mathfrak{sl}(2,\mathbb{C}),
$$

of complex dimension three and real dimension six.

*Proof.* The Leibniz rule for the commutator is the associativity of the product, $\operatorname{ad}_{\tilde P}(\tilde Q\tilde R)=(\operatorname{ad}_{\tilde P}\tilde Q)\tilde R+\tilde Q(\operatorname{ad}_{\tilde P}\tilde R)$, and the halving carries it to the bracket; this is *Associative Algebras* and *Derivations of a Lie Algebra*. The inner derivations are the image of the adjoint representation, which by the previous section has kernel the centre, so its image is isomorphic to $\mathfrak{g}/\mathbb{C}_{\mathbb{B}}\cong\mathrm{Vect}(\mathbb{B})\cong\mathfrak{sl}(2,\mathbb{C})$; the isomorphism is $\operatorname{ad}_{[\,\tilde P,\tilde Q\,]}=[\operatorname{ad}_{\tilde P},\operatorname{ad}_{\tilde Q}]$. $\square$

**Remark.** **The inner derivations are the adjoints, and there are as many of them as the derived algebra has dimensions: three complex and six real.** The identification of the inner derivations with $\mathfrak{sl}(2,\mathbb{C})$ is the same identification as the one of the derived algebra, read through the adjoint representation; the two are the same space, one acting on the algebra and one acted upon.

### The Outer Derivations

**Theorem.** The outer derivations form a complex line, spanned by the derivation

$$
D_0:\quad D_0(e_0)=e_0,\qquad D_0(ie_0)=ie_0,\qquad D_0(\tilde X)=0\ \text{ on }\ \mathrm{Vect}(\mathbb{B}),
$$

which scales the centre and annihilates the derived algebra; it is the derivation induced by the dual number $\mathbb{C}[\varepsilon]/(\varepsilon^2)$ acting on the centre in the description below. Hence

$$
\operatorname{Der}(\mathfrak{g})=\operatorname{Inn}(\mathfrak{g})\oplus\mathbb{C}D_0\cong\mathfrak{sl}(2,\mathbb{C})\oplus\mathbb{C},
$$

of complex dimension four and real dimension eight.

*Proof.* For the bracket of two vector elements the image lies in the vector subspace, on which $D_0$ vanishes, and both terms of the Leibniz rule vanish; for the bracket of a central element with anything the bracket is zero on both sides; so $D_0$ is a derivation. For the converse, a derivation preserves the centre, because the centre is the kernel of the adjoint representation and a derivation commutes with the adjoints: $D\operatorname{ad}_{\tilde P}=\operatorname{ad}_{D\tilde P}+\operatorname{ad}_{\tilde P}D$, so an element annihilated by every adjoint is carried to an element annihilated by every adjoint. A derivation also preserves the derived algebra, by the Leibniz rule and the stability of the image. Its restriction to the simple derived algebra is an inner derivation of that algebra, $D|_{\mathrm{Vect}}=\operatorname{ad}_{\mathbf{P}}$ for some vector $\mathbf{P}$, by *Derivations of a Lie Algebra*, since $\mathfrak{sl}(2,\mathbb{C})$ has no outer derivation; the difference $D-\operatorname{ad}_{\mathbf{P}}$ is then a derivation vanishing on the derived algebra and preserving the one-dimensional centre, so it acts on the centre by a scalar $\nu$ and is $\nu D_0$; hence every derivation is $\operatorname{ad}_{\mathbf{P}}+\nu D_0$. Computed exactly on the basis. $\square$

**Remark (the derivation algebra is the tangent algebra of the automorphisms).** The dual numbers give the reason the outer derivation has dimension one: over $\mathbb{C}[\varepsilon]/(\varepsilon^2)$ the automorphism $\mathrm{id}+\varepsilon D$ of the bracket is a derivation exactly when $D$ obeys the Leibniz rule, and the derivations of the simple derived algebra are its inner ones, of dimension three, together with the derivation that scales the one-dimensional centre. **The derivation algebra is $\mathfrak{sl}(2,\mathbb{C})\oplus\mathbb{C}$, of complex dimension four.** The inner derivations are the adjoints and the outer line is the centre scaling; the general theory is *Derivations of a Lie Algebra*, and the same algebra is the Lie algebra of the group of the next section.

## The Automorphisms of the Bracket

### The Group

**Definition.** An **automorphism of the bracket** is an invertible $\mathbb{C}$-linear map $T:\mathbb{B}\to\mathbb{B}$ with

$$
T(\tilde P\wedge\tilde Q)=T\tilde P\wedge T\tilde Q
$$

for all $\tilde P,\tilde Q$; the automorphisms form the group $\operatorname{Aut}(\mathfrak{g})$.

**Theorem.** Every automorphism preserves the centre and the derived algebra, and it is the direct sum of an invertible scalar on the centre and an automorphism of the derived algebra:

$$
T(\tilde P)=\alpha\,P_0e_0\oplus A(\mathbf{P}),\qquad \alpha\in\mathbb{C}^{\times},\qquad A\in\operatorname{Aut}\bigl(\mathrm{Vect}(\mathbb{B}),\wedge\bigr),
$$

so that

$$
\operatorname{Aut}(\mathfrak{g})\cong\mathbb{C}^{\times}\times\operatorname{Aut}\bigl(\mathrm{Vect}(\mathbb{B}),\wedge\bigr)\cong\mathbb{C}^{\times}\times PGL(2,\mathbb{C}),
$$

of complex dimension four.

*Proof.* The centre is the kernel of the adjoint representation, an intrinsic subspace, so an automorphism preserves it; the derived algebra is intrinsically $[\mathfrak{g},\mathfrak{g}]$, so it is preserved too, and it is complementary to the centre. On the centre the automorphism is an invertible scalar; on the derived algebra it is a bracket automorphism, and the automorphism group of $\mathfrak{sl}(2,\mathbb{C})$ is the adjoint group $PGL(2,\mathbb{C})=\operatorname{PSL}(2,\mathbb{C})$, of complex dimension three, acting by conjugation in the two-dimensional model, *The Antisymmetric Plain Algebra in the $2\times2$ and $4\times4$ Matrix Element Representations*. Any pair $(\alpha,A)$ is an automorphism because the bracket never mixes the centre with the derived algebra. Computed on the basis. $\square$

### The Two Examples

**Theorem (the conjugation by a unit).** Let $\tilde U$ be invertible in $\mathbb{B}$ and put $T_{\tilde U}(\tilde P)=\tilde U\tilde P\tilde U^{-1}$. Then $T_{\tilde U}$ is an automorphism of the bracket, it is the identity on the centre, and on the derived algebra it is the conjugation by the image of $\tilde U$ in $PGL(2,\mathbb{C})$. The assignment descends to the group of units modulo the centre.

*Proof.* The map is invertible and multiplicative for the plain product, so it carries the commutator to the commutator and the halved bracket to the halved bracket; on the centre it is the identity because the centre commutes with $\tilde U$; the kernel of the assignment is the group of units whose conjugation is trivial, which is the centre. This is *The Lie Algebra of the Antisymmetric Plain Algebra*'s identification of the derived algebra and the model of *The Antisymmetric Plain Algebra in the $2\times2$ and $4\times4$ Matrix Element Representations*. Computed on general units. $\square$

**Theorem (the central scalar).** For $\lambda\in\mathbb{C}^{\times}$ let $T_\lambda$ multiply the centre by $\lambda$ and fix the derived algebra. Then $T_\lambda$ is an automorphism of the bracket; $T_\lambda$ is the identity exactly for $\lambda=1$.

*Proof.* The bracket of two vector elements is a vector element and is fixed; a bracket with a central element vanishes on both sides; so the map preserves the bracket. $\square$

**Remark.** The two families generate the automorphism group: **every automorphism of the bracket is the product of a conjugation by a unit and a central scalar**, the conjugation moving the derived algebra and the central scalar moving the centre, and the two families commute because the conjugation is the identity on the centre. The Lie algebra of the automorphism group is $\operatorname{Der}(\mathfrak{g})$, as the previous section records by the dual numbers, and it is of complex dimension four.

## The Adjoint Representation

**Theorem.** The map $\operatorname{ad}:\mathfrak{g}\to\operatorname{End}(\mathbb{B})$, $\tilde P\mapsto\operatorname{ad}_{\tilde P}$, is a representation of the bracket,

$$
\operatorname{ad}_{[\tilde P,\tilde Q]}=[\operatorname{ad}_{\tilde P},\operatorname{ad}_{\tilde Q}],
\qquad\text{equivalently}\qquad
\operatorname{ad}^{\wedge}_{\tilde P\wedge\tilde Q}=[\operatorname{ad}^{\wedge}_{\tilde P},\operatorname{ad}^{\wedge}_{\tilde Q}],
$$

its kernel is the centre $\mathbb{C}_{\mathbb{B}}$, and its image is the Lie algebra of the inner derivations, identified with the derived algebra:

$$
\operatorname{ad}(\mathfrak{g})\cong\mathfrak{g}/\mathbb{C}_{\mathbb{B}}\cong\mathrm{Vect}(\mathbb{B})\cong\mathfrak{sl}(2,\mathbb{C}),
$$

of complex dimension three and real dimension six.

*Proof.* The identity $\operatorname{ad}_{[\,\tilde P,\tilde Q\,]}=[\operatorname{ad}_{\tilde P},\operatorname{ad}_{\tilde Q}]$ is the Jacobi identity, and it holds for the halved bracket with the factor carried along; the kernel is the centre by the vanishing theorem, and the image is the quotient by the kernel, which is the derived algebra by *The Lie Algebra of the Antisymmetric Plain Algebra*. Verified on the basis. $\square$

**Remark.** **The adjoint representation is faithful exactly on the derived algebra and kills exactly the centre**, and its image is the inner derivation algebra. The representation is the matrix model of the adjoints; its matrices in the real basis are the ones computed above, and their vanishing trace is the trace form of the representation.

## The Structure Group

**Definition.** A **similarity of the bracket** is an invertible $\mathbb{C}$-linear map $T$ with

$$
T(\tilde P\wedge\tilde Q)=\lambda\,(T\tilde P\wedge T\tilde Q)
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

*Proof.* For two vector elements, $T(\tilde P\wedge\tilde Q)=\mu A(\tilde P\wedge\tilde Q)$ and $T\tilde P\wedge T\tilde Q=\mu^2\,(A\tilde P\wedge A\tilde Q)=\mu^2A(\tilde P\wedge\tilde Q)$; the multiplier is therefore $1/\mu$, independent of the elements. For a bracket with a central element both sides vanish; for two central elements both sides vanish. Conversely, a similarity preserves the centre and the derived algebra by the same intrinsic argument as an automorphism, so it has the displayed form. Computed exactly on general elements, where the identity $T(\tilde P\wedge\tilde Q)=\mu^{-1}(T\tilde P\wedge T\tilde Q)$ was verified for $A$ a conjugation. $\square$

**Remark (the Lie algebra of the structure group).** The structure group has the same dimension as its Lie algebra of tangent maps, and that algebra is

$$
\operatorname{Der}(\mathfrak{g})\oplus\mathbb{C}\,D_{\mathrm{dil}},
$$

where $D_{\mathrm{dil}}$ is the **dilation** of the derived algebra (the identity on $\mathrm{Vect}(\mathbb{B})$ and zero on the centre), a map that is not a derivation but obeys the infinitesimal similarity rule. **The structure group of the bracket is the automorphism group times the dilations, of complex dimension four plus one; the extra dimension is the one that scales the bracket itself.** The central scalars form the subgroup that scales only the centre, and they are already automorphisms, which is why the structure group contributes two scalar factors and the automorphism group only one.

## Worked Examples

**A central adjoint.** $\operatorname{ad}_{e_0+ie_0}=0$, because both coordinates are central: the adjoint representation kills the centre.

**A vector adjoint.** $\operatorname{ad}_{e_1}(e_2)=2e_3$ and $\operatorname{ad}_{e_1}(e_3)=-2e_2$: the adjoint of $e_1$ is twice the cross product by $e_1$, and it fixes $e_1$ and the centre.

**The trace.** $\operatorname{Tr}(\operatorname{ad}_{e_1})=0$ and $\operatorname{Tr}(\operatorname{ad}_{ie_1})=0$: every adjoint has vanishing trace, the diagonal of the displayed matrix being zero.

**A derivation.** $\operatorname{ad}_{e_3}$ sends $e_1\mapsto 2e_2$ and $e_2\mapsto-2e_1$, and it obeys the Leibniz rule on the pair $e_1,e_2$: $\operatorname{ad}_{e_3}(e_1\wedge e_2)=\operatorname{ad}_{e_3}e_3=0$, and $\operatorname{ad}_{e_3}e_1\wedge e_2+e_1\wedge\operatorname{ad}_{e_3}e_2=2e_2\wedge e_2+e_1\wedge(-2e_1)=0$.

**The outer derivation.** $D_0(e_0)=e_0$ and $D_0(e_1)=0$: the centre scaling, which is not inner because an inner derivation vanishes on the centre.

**The conjugation by a unit.** For $\tilde U=e_1$, a unit with $e_1^{-1}=-e_1$, the conjugation fixes $e_1$ and reverses the sign on the plane orthogonal to it: $e_1e_2e_1^{-1}=(e_1e_2)(-e_1)=-e_3e_1=-e_2$, and $e_1e_3e_1^{-1}=-e_3$. It is a nontrivial automorphism of the derived algebra and the identity on the centre.

**The central scalar.** $T_\lambda(e_0)=\lambda e_0$, $T_\lambda(e_1)=e_1$ is an automorphism for every $\lambda\neq0$; the adjoint representation is unchanged by it, since the centre is in its kernel.

**A similarity.** $T$ that fixes the centre and multiplies the derived algebra by $\mu$ satisfies $T(\tilde P\wedge\tilde Q)=\mu^{-1}(T\tilde P\wedge T\tilde Q)$: the multiplier is the reciprocal of the dilation, as the theorem states.

## Summary

The adjoint of the block is $\operatorname{ad}_{\tilde P}=[\tilde P,\cdot]$, equal to twice the operator $\mathbf{P}\times$ on the vector subspace, vanishing on the centre, of matrix block diagonal in the real basis with zeroes on the centre and the realification of $2C_{\mathbf{P}}$ on the derived algebra, and of trace zero; the halved adjoint $\operatorname{ad}^{\wedge}_{\tilde P}=\mathbf{P}\times$ is the version of the block's own bracket, and the two differ by the factor $2$ of the halving. The adjoints are derivations, and the inner derivations are exactly the adjoints of the derived algebra, identified with $\mathfrak{sl}(2,\mathbb{C})$; the outer derivations form one complex line, spanned by the scaling of the centre, so $\operatorname{Der}(\mathfrak{g})\cong\mathfrak{sl}(2,\mathbb{C})\oplus\mathbb{C}$ has complex dimension four. The automorphisms of the bracket are the pairs of an invertible scalar on the centre and an automorphism of the derived algebra, $\operatorname{Aut}(\mathfrak{g})\cong\mathbb{C}^{\times}\times PGL(2,\mathbb{C})$, generated by the conjugation by a unit and the central scalar, with Lie algebra $\operatorname{Der}(\mathfrak{g})$. The adjoint representation has kernel the centre and image the derived algebra. The structure group of the bracket, of maps with $T(\tilde P\wedge\tilde Q)=\lambda(T\tilde P\wedge T\tilde Q)$, is $\mathbb{C}^{\times}\times\mathbb{C}^{\times}\times PGL(2,\mathbb{C})$, of complex dimension five, with Lie algebra the derivations together with the dilation of the derived algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{ad}_{\tilde P}(\tilde X)=[\tilde P,\tilde X]=\tilde P\tilde X-\tilde X\tilde P$ | the adjoint of the block, twice $\mathbf{P}\times$ on the vector subspace |
| $\operatorname{ad}^{\wedge}_{\tilde P}(\tilde X)=\tilde P\wedge\tilde X=\mathbf{P}\times\mathbf{X}$ | the halved adjoint, the adjoint of the block's own bracket |
| $\ker\operatorname{ad}=\mathbb{C}_{\mathbb{B}}$ | the kernel of the adjoint representation, the centre |
| $\operatorname{Tr}\operatorname{ad}_{\tilde P}=0$ | every adjoint has vanishing trace |
| $\operatorname{Der}(\mathfrak{g})$ | the derivation algebra |
| $\operatorname{Inn}(\mathfrak{g})=\operatorname{ad}(\mathrm{Vect}(\mathbb{B}))\cong\mathfrak{sl}(2,\mathbb{C})$ | the inner derivations, the adjoints |
| $D_0$ | the outer derivation scaling the centre, annihilating the derived algebra |
| $\operatorname{Der}(\mathfrak{g})\cong\mathfrak{sl}(2,\mathbb{C})\oplus\mathbb{C}$ | the derivation algebra, of complex dimension four |
| $\operatorname{Aut}(\mathfrak{g})\cong\mathbb{C}^{\times}\times PGL(2,\mathbb{C})$ | the automorphism group of the bracket |
| $T_{\tilde U}(\tilde P)=\tilde U\tilde P\tilde U^{-1}$; $T_\lambda$ on the centre | the conjugation by a unit and the central scalar |
| $\operatorname{Str}(\mathfrak{g})\cong\mathbb{C}^{\times}\times\mathbb{C}^{\times}\times PGL(2,\mathbb{C})$ | the structure group of the bracket, of complex dimension five |

## Further Reading

- *Introduction to the Antisymmetric Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-biquaternions.md`), for the bracket and the cross-product formula
- *The Lie Algebra of the Antisymmetric Plain Algebra* (`articles_maths/the-lie-algebra-of-the-antisymmetric-plain-algebra.md`), for the centre, the derived algebra, the identifications and the enveloping algebra
- *The Killing Form of the Antisymmetric Plain Algebra* (`articles_maths/the-killing-form-of-the-antisymmetric-plain-algebra.md`), for the invariant form, the radical and the Casimir element
- *Remarkable Subspaces under the Antisymmetric Plain Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-antisymmetric-plain-algebra-of-biquaternions.md`), for the bracket read on the remarkable subspaces
- *The Antisymmetric Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-antisymmetric-plain-algebra-in-the-2x2-matrix-element-representation.md`), for the conjugations in the realization
- *The Antisymmetric Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/the-antisymmetric-plain-algebra-in-the-4x4-matrix-element-representation.md`), for the conjugations in the regular model
- *Derivations of a Lie Algebra* (`articles_maths/derivations-of-a-lie-algebra.md`), for the inner and outer derivations and the derivation algebra as the Lie algebra of the automorphism group
- *Associative Algebras* (`articles_maths/associative-algebras.md`), for the associativity behind the Leibniz rule
- *Two-Sided Operators on the General Plain Algebra of Biquaternions* (`articles_maths/two-sided-operators-on-the-general-plain-algebra-of-biquaternions.md`), for the operators of the multiplication and their trace form
