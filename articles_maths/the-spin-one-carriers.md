# __The Spin-One Carriers__

## Introduction

The biquaternion algebra carries one carrier of the adjoint type, and the subspaces that realise it are two. The type has real dimension three and spin $1$; the two subspaces are the real vector triple $\mathfrak{k}$ and its imaginary partner $\mathfrak{p}=i\mathfrak{k}$. Each is invariant under the conjugation and irreducible, and the central $i$ exchanges them, so they are one type realised twice.

This article proves that both triples are invariant and irreducible, that the action on them is the adjoint one and not a left multiplication, and that the weights are $+1$, $0$ and $-1$, read after complexification. It then lists the four real halves of the algebra that contain the triples and separates the two that are closed under the commutator from the two that are not.

The count of the three types is *The Carriers of the Biquaternion Algebra*, the number attached to a type is *The Spin of a Carrier*, the spectra are *The Weights of a Carrier*, §*The Three Spectra*, and the reason the sector rather than its Hermitian partner is named is *The Spin of a Carrier*, §*Why $\mathbb{B}_{\Phi}$ and Not $\mathbb{B}_{\Psi}$*. The two other carriers are *The Spin-Zero Carrier* and *The Spin-Half Carriers*.

Nothing below is a statement of physics. The elements are written $X,Y$; the units are $e_t,\vec e_x,\vec e_y,\vec e_z$ with $e_t^2=e_t$ and $\vec e_k^{2}=-e_t$; a unit real vector $\vec u$ stands also for the pure quaternion $u_x\vec e_x+u_y\vec e_y+u_z\vec e_z$.

## The Traceless Part

**Definition (the two triples).** The **real vector triple** and its **imaginary partner** are

$$
\mathfrak{k}=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\},\qquad
\mathfrak{p}=i\mathfrak{k}=\operatorname{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}.
$$

Both are real three-dimensional subspaces of $\mathbb{B}$, and they meet only in $0$.

*Proof of the last statement.* Suppose $\sum_k a_k\vec e_k=\sum_k ib_k\vec e_k$ with real coefficients. Reading the coefficients in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ gives $a_k=ib_k$ for each $k$, so $a_k=b_k=0$.

**Theorem (both are invariant, and both are irreducible).** For every unit $u$,

$$
\operatorname{Ad}_u(\mathfrak{k})\subseteq\mathfrak{k},\qquad
\operatorname{Ad}_u(\mathfrak{p})\subseteq\mathfrak{p},
$$

and the two modules are irreducible.

*Proof.* The group of units is stable under the quaternion conjugation, so the conjugation preserves the real and the purely imaginary parts of the coefficients: $u\vec v\,u^{*}$ is a real pure quaternion for $\vec v$ real, and $u(i\vec v)u^{*}=i\,u\vec vu^{*}$ because $i$ is central. Irreducibility: the derivations $\operatorname{ad}_{X}$ with $X\in\mathfrak{k}$ act on $\mathfrak{k}$ as the vector product, $\operatorname{ad}_{\vec e_k}(\vec v)=2\vec e_k\times\vec v$, so the module is the adjoint module of $\mathfrak{so}(3)$ on $\mathbb{R}^{3}$, which is irreducible because the orbit of a nonzero vector spans the space.

**Corollary (the four blocks).** $\mathfrak{k}$ is the traceless part of the anti-Hermitian sector and of the quaternion subspace, and $\mathfrak{p}$ is the traceless part of the Hermitian sector and of the imaginary quaternion subspace:

$$
\mathbb{B}_{\Phi}=\mathbb{R}(ie_t)\oplus\mathfrak{k},\qquad
\mathbb{B}_{H}=\mathbb{R}e_t\oplus\mathfrak{k},\qquad
\mathbb{B}_{\Psi}=\mathbb{R}e_t\oplus\mathfrak{p},\qquad
\mathbb{B}_{iH}=\mathbb{R}(ie_t)\oplus\mathfrak{p}.
$$

*Proof.* A real quaternion is $Q_te_t+\vec v$ with $\vec v\in\mathfrak{k}$; multiplying by $i$ gives $iQ_te_t+i\vec v$ with $i\vec v\in\mathfrak{p}$. The four decompositions are *Subspaces and Decompositions of the Biquaternion Algebra*, §*The Six Remarkable Subspaces*, and the sectors are the two halves of the Hermitian splitting.

## The Action Is the Adjoint One

The generator of the rotation is a Hermitian element, and it does not act on the triple by left multiplication. The distinction is the reason the third carrier is read with the bracket and not with the product.

**Proposition (the triple is not a left ideal).** For a unit real $\vec u$ and a real pure quaternion $\vec v$,

$$
\tilde S(\vec u)\vec v=\tfrac12 i\Bigl(-(\vec u\cdot\vec v)\,e_t+(\vec u\times\vec v)\cdot\vec e\Bigr),
$$

so left multiplication carries $\mathfrak{k}$ into $\mathbb{R}(ie_t)\oplus\mathfrak{p}$ and not into itself. At $\vec u\perp\vec v$ the central term vanishes and the image is $i(\vec u\times\vec v)\cdot\vec e\in\mathfrak{p}$; at $\vec u\parallel\vec v$ the image is the central $-\tfrac12 i e_t$.

*Proof.* Multiply the real product, $\vec u\cdot\vec e$ times $\vec v$, by the scalar $\tfrac12 i$. The real product has scalar part $-(\vec u\cdot\vec v)$ and vector part $(\vec u\times\vec v)\cdot\vec e$, by the multiplication rule of the basis units; the scalar $\tfrac12 i$ multiplies both parts. Two witnesses: $\tilde S(\vec e_z)\vec e_x=\tfrac12 i\vec e_y$, and $\tilde S(\vec e_x)\vec e_x=-\tfrac12 i e_t$.

**Theorem (the bracket with a real parameter stays inside).** For real $\vec u$ and $\vec v$,

$$
[\vec u\cdot\vec e,\vec v]=2(\vec u\times\vec v)\cdot\vec e\in\mathfrak{k},
$$

so the bracket is a product on the triple and $\mathfrak{k}$ is a real Lie algebra, of structure constants $2\epsilon_{ijk}$.

*Proof.* For pure quaternions the commutator is twice the vector product, $\vec p\vec q-\vec q\vec p=2\,\vec p\times\vec q$: the scalar parts of the two products cancel and the vector parts add. The vector product of two real vectors is a real vector, so the value lies in $\mathfrak{k}$.

**Theorem (the Hermitian generator leaves the real triple).** The derivation with the Hermitian parameter does not preserve $\mathfrak{k}$ as a real space:

$$
\operatorname{ad}_{\tilde S(\vec u)}\vec v=i\,[\tfrac12\vec u\cdot\vec e,\vec v]\in\mathfrak{p},
$$

while it does preserve the complexification $\mathfrak{k}_{\mathbb{C}}=\mathbb{C}\otimes_{\mathbb{R}}\mathfrak{k}$.

*Proof.* $\tilde S(\vec u)=i\,\tfrac12\vec u\cdot\vec e$, so its derivation is $i$ times a real derivation; applying that to a real vector gives an imaginary one, which is a complex multiple of a real vector and therefore lies in $\mathfrak{k}_{\mathbb{C}}$ but not in $\mathfrak{k}$. A witness: $\operatorname{ad}_{\tilde S(\vec e_z)}\vec e_x=i\vec e_y$.

**Remark (how the two statements fit).** The Hermitian generator does not preserve the real triple; it carries it into the imaginary triple. The anti-Hermitian generator $g(\vec u)=-\tfrac12\vec u\cdot\vec e$ preserves the real triple, and the two are related by $\tilde S=-ig$. The weights are therefore read on the complexification, where the two triples are one complex space of dimension three and the factor $i$ is a scalar. This is the computation of *The Weights of a Carrier*, §*The Three Spectra*, and it is the only carrier for which the complexification is needed.

## The Weights

**Theorem (the weight string).** On $\mathfrak{k}_{\mathbb{C}}$ the generator $\tilde S(\vec u)$ acts by $\operatorname{ad}$ with the three eigenvalues $+1$, $0$ and $-1$. At $\vec u=\vec e_z$ the eigenvectors are

$$
v_{+}=\vec e_x+i\vec e_y,\qquad v_{0}=\vec e_z,\qquad v_{-}=\vec e_x-i\vec e_y .
$$

*Proof.* $\operatorname{ad}_{\tilde S}\vec e_x=i\vec e_y$ and $\operatorname{ad}_{\tilde S}\vec e_y=-i\vec e_x$, so $\operatorname{ad}_{\tilde S}v_{+}=i\vec e_y+\vec e_x=v_{+}$ and $\operatorname{ad}_{\tilde S}v_{-}=-v_{-}$; and $\operatorname{ad}_{\tilde S}\vec e_z=0$ by the vanishing of the vector product of a vector with itself. The three vectors are a basis of the complexification, so the string is complete.

**Corollary (the number).** The spin is $1$, the dimension of the representation space is $2s+1=3$, and the value of the quadratic element is $2$.

*Proof.* The string is simple and spaced by one, so the highest weight is the spin and the length of the string is the dimension. The quadratic element is not the central element $\tfrac34e_t$ here: on the adjoint module the central element acts by $0$, and the value $2=s(s+1)$ is the one of the composed operators $\operatorname{ad}_{\tilde S_k}^{2}$, each of which is the projection onto the plane perpendicular to $\vec e_k$. The three projections sum to $2$ on a three-dimensional space. The two objects and their disagreement are *The Weights of a Carrier*, §*The Central Element and Its Values*.

| quantity | value on $\mathfrak{k}$ |
|---|---|
| the weight string | $+1,0,-1$ |
| the highest weight, that is the spin | $1$ |
| the real dimension of the representation space | $3$ |
| the value of the composite quadratic element | $2$ |
| the value of the central element $\tfrac34e_t$ | $0$ |
| the sign of $-e_t$ | $+1$ |

**Remark (why the string is read on the complexification).** The real triple is a real module and its generator is the anti-Hermitian $g(\vec u)$, whose eigenvalues are $0$ and $\pm i$. The weights are $-i$ times those eigenvalues, and multiplying by $-i$ is what turns a real module into a complex one. The pass to $\mathfrak{k}_{\mathbb{C}}$ performs that multiplication once and for all.

## The Two Carriers

**Theorem (the central $i$ exchanges the triples).** Multiplication by $i$ is an isomorphism of modules

$$
i:\mathfrak{k}\xrightarrow{\ \sim\ }\mathfrak{p},\qquad i\bigl(\operatorname{Ad}_u\vec v\bigr)=\operatorname{Ad}_u\bigl(i\vec v\bigr),
$$

and the two modules have the same weights, the same dimension and the same spin.

*Proof.* $i$ is central and invertible, so $u(i\vec v)u^{*}=i\,u\vec vu^{*}$; the identity displayed is that equation read as the intertwining. The weights agree because the two actions are the same action read through $i$.

**Corollary (two subspaces, one type).** The type $\mathcal{V}_3$ is realised by exactly two subspaces of the algebra, $\mathfrak{k}$ and $\mathfrak{p}$, and they are isomorphic. The count of carriers of this type is therefore two, and the count of types is one.

*Proof.* Let $W$ be a real three-dimensional subspace that is invariant and irreducible under the conjugation. The four blocks of the algebra under the action are $\mathbb{R}e_t$, $\mathbb{R}(ie_t)$, $\mathfrak{k}$ and $\mathfrak{p}$, the first two trivial and the last two irreducible of dimension three. An irreducible three-dimensional invariant subspace is one of the last two; a sum of two of them is reducible; and no other combination has dimension three.

**Remark (the table records the block).** The table of *The Carriers of the Biquaternion Algebra* names $\mathbb{B}_{\Phi}$ for this type, with the entry "spin $1$, on its traceless part". The sector is recorded because it is the smallest real subspace closed under the conjugation and under the commutator at once, and because the entries of that table are the blocks that the conjugations cut out; the carrier is the traceless part of the block. The choice between $\mathbb{B}_{\Phi}$ and the other three blocks is settled in *The Spin of a Carrier*, §*Why $\mathbb{B}_{\Phi}$ and Not $\mathbb{B}_{\Psi}$*.

## The Four Halves

Each of the four blocks of the corollary is a real four-dimensional subspace, invariant under the conjugation and splitting as a trivial line plus one of the two triples. The four are not carriers, because they are reducible; they are the halves of the algebra that contain the carriers.

**Proposition (invariance and splitting).** The four subspaces $\mathbb{B}_{\Phi}$, $\mathbb{B}_{H}$, $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{iH}$ are invariant under $\operatorname{Ad}_u$ for every unit $u$, and each is the direct sum of its traceless part and a central real line.

*Proof.* Invariance: the conjugations $*$ and ${}^{\natural}$ commute with the conjugation by a unit, $(uXu^{*})^{*}=uX^{*}u^{*}$ and $(uXu^{*})^{\natural}=uX^{\natural}u^{*}$, so each half of each pairing is preserved. The splitting is the corollary above; the line is central, hence fixed.

**Theorem (two of the four are closed under the commutator).** Of the four halves exactly two are closed under the bracket:

$$
[\mathbb{B}_{\Phi},\mathbb{B}_{\Phi}]\subseteq\mathbb{B}_{\Phi},\qquad
[\mathbb{B}_{H},\mathbb{B}_{H}]\subseteq\mathbb{B}_{H},\qquad
[\mathbb{B}_{\Psi},\mathbb{B}_{\Psi}]=\mathfrak{k},\qquad
[\mathbb{B}_{iH},\mathbb{B}_{iH}]=\mathfrak{p}.
$$

*Proof.* $\mathbb{B}_{\Phi}$ is closed by the sign rule: two anti-Hermitian elements have an anti-Hermitian product, so their commutator is anti-Hermitian. $\mathbb{B}_{H}\cong\mathbb{H}$ is a subalgebra, hence closed under the bracket. For the two failures: two Hermitian elements have an anti-Hermitian bracket, and the bracket of two elements of $\mathbb{B}_{iH}$ is $-1$ times the bracket of two real quaternions, hence a real pure quaternion. The witnesses are $[i\vec e_x,i\vec e_y]=-2\vec e_z\in\mathfrak{k}$ and $[\vec e_x,\vec e_y]=2\vec e_z$.

**Remark (the double criterion).** A half is a carrier of the adjoint action when it is invariant under the conjugation and closed under the bracket. The first condition holds for all four halves; the second holds for $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{H}$ alone. So the criterion does not separate the two sectors, and it does not separate the two quaternion halves; it separates the pair $\{\mathbb{B}_{\Phi},\mathbb{B}_{H}\}$ from the pair $\{\mathbb{B}_{\Psi},\mathbb{B}_{iH}\}$, and the passage from one pair to the other is the choice of the involution.

## The Group and the Module

**Theorem (the module is the adjoint one of the rotation algebra).** The action of $G=\mathrm{U}(2)$ on $\mathfrak{k}$ factors through $SO(3)$, the conjugation by the real unit $\cos\tfrac{\theta}{2}+\vec u\sin\tfrac{\theta}{2}$ being the rotation of angle $\theta$ about $\vec u$, and the three derivations $\operatorname{ad}_{\tilde S_k}$ on $\mathfrak{k}_{\mathbb{C}}$ satisfy $[\operatorname{ad}_{\tilde S_i},\operatorname{ad}_{\tilde S_j}]=i\epsilon_{ijk}\operatorname{ad}_{\tilde S_k}$.

*Proof.* A real unit quaternion acts on real pure quaternions by conjugation, which is the rotation of angle twice its half-angle about its axis, by *Quaternion Rotations and Reflections*, §*The Adjoint Action on the Imaginary Quaternions*. A general unitary is a real unit times a central phase of modulus one, and the central phase acts trivially, so the action factors through the real units and hence through $SO(3)$. The commutator identity is the one of *The Weights of a Carrier*, §*The Generator*.

**Corollary (the module is irreducible as a complex module too).** $\mathfrak{k}_{\mathbb{C}}\cong\mathcal{V}_3$ is the irreducible complex module of dimension three, of highest weight $1$.

*Proof.* The weights are simple and spaced by one, so the criterion of *The Weights of a Carrier*, §*The Criterion*, applies and gives irreducibility and the dimension.

## The Intersections with the Other Carriers

**Proposition (the intersections).** With $\mathfrak{k}$, $\mathfrak{p}$, $S_{\pm}(\vec u)$ and $\mathbb{C}e_t$ as above,

$$
\mathfrak{k}\cap\mathfrak{p}=0,\qquad
\mathfrak{k}\cap\mathbb{C}e_t=0,\qquad
\mathfrak{p}\cap\mathbb{C}e_t=0,
$$

and the two triples meet no spin-half carrier.

*Proof.* The first three are the linear independence of the four blocks: an element of the intersection has coefficients supported on two disjoint sets of coordinates. For the last, a nonzero element of a minimal left ideal has rank one in the model, and a nonzero pure quaternion is invertible, hence of rank two, by the argument of *The Spin-Half Carriers*, §*The Intersections with the Other Carriers*.

| carrier | intersection with $\mathfrak{k}$ |
|---|---|
| $\mathfrak{p}$ | $0$ |
| $\mathbb{C}e_t$ | $0$ |
| $S_{\pm}(\vec u)$ | $0$ |

## Summary

The spin-one carriers are the real vector triple $\mathfrak{k}$ and its imaginary partner $\mathfrak{p}=i\mathfrak{k}$, two real three-dimensional subspaces, invariant under the conjugation, irreducible, exchanged by the central $i$, and of the one type $\mathcal{V}_3$.

The action on them is the adjoint action and not a left multiplication: the Hermitian generator carries $\mathfrak{k}$ into $\mathfrak{p}$, and the bracket of two real vectors is a real vector. The weights are $+1$, $0$ and $-1$, read on the complexification; the spin is $1$, the dimension is $3$, and the composite quadratic element is $2$ while the central element $\tfrac34e_t$ is $0$.

Four real halves of the algebra contain the triples: $\mathbb{B}_{\Phi}=\mathbb{R}(ie_t)\oplus\mathfrak{k}$, $\mathbb{B}_{H}=\mathbb{R}e_t\oplus\mathfrak{k}$, $\mathbb{B}_{\Psi}=\mathbb{R}e_t\oplus\mathfrak{p}$ and $\mathbb{B}_{iH}=\mathbb{R}(ie_t)\oplus\mathfrak{p}$. All four are invariant; exactly two, $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{H}$, are closed under the commutator. The table of carriers names $\mathbb{B}_{\Phi}$, and the naming is a convention whose warrant is the bracket.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, $M_2(\mathbb{C})$, complex dimension four |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the units, $e_t^2=e_t$ and $\vec e_k^{2}=-e_t$ |
| $\mathfrak{k}=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ | the real vector triple, the traceless part of the anti-Hermitian sector |
| $\mathfrak{p}=i\mathfrak{k}$ | its imaginary partner, the traceless part of the Hermitian sector |
| $\operatorname{Ad}_u(X)=uXu^{*}$ | the conjugation by a unit |
| $\operatorname{ad}_Y(X)=[Y,X]$ | the commutator |
| $\tilde S_k=\tfrac12 i\vec e_k$, $g_k=-\tfrac12\vec e_k$ | the Hermitian and anti-Hermitian generators, $\tilde S_k=-ig_k$ |
| $\mathbb{B}_{\Psi},\mathbb{B}_{\Phi},\mathbb{B}_{H},\mathbb{B}_{iH}$ | the four real halves of dimension four |
| $\mathfrak{k}_{\mathbb{C}}$ | the complexification of the triple, the complex module $\mathcal{V}_3$ |
| $\mathcal{V}_3$ | the adjoint type, of real dimension three |
| $v_{+},v_{0},v_{-}$ | the weight vectors $\vec e_x+i\vec e_y$, $\vec e_z$, $\vec e_x-i\vec e_y$ |
| $G=\mathrm{U}(2)$ | the group of unitary units |

## Further Reading

- [The Carriers of the Biquaternion Algebra](the-carriers-of-the-biquaternion-algebra.html), for the definition of a carrier, the table of the three types and the completeness of the count.
- [The Spin of a Carrier](the-spin-of-a-carrier.html), for the spin as a function of the type and for the choice of the sector over its Hermitian partner.
- [The Weights of a Carrier](the-weights-of-a-carrier.html), for the three spectra, the criterion and the two quadratic elements.
- [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html), for the six remarkable subspaces, the four coordinate blocks and the decompositions of the algebra.
- [Quaternion Rotations and Reflections](quaternion-rotations-and-reflections.html), for the conjugation by a real unit as the rotation of twice its half-angle, and for the double cover.
- [Biquaternion Versors and the Orthogonal Group](biquaternion-versors-and-the-orthogonal-group.html), for the versors and the orthogonal group generated by them.
- [The Spin-Zero Carrier](the-spin-zero-carrier.html), for the unique trivial carrier.
- [The Spin-Half Carriers](the-spin-half-carriers.html), for the sphere of minimal left ideals.
- [The Tensor Square of the Adjoint Module](the-tensor-square-of-the-adjoint-module.html), for the products of the adjoint type, where $\mathcal{V}_3\otimes\mathcal{V}_3$ splits as $\mathcal{V}_1\oplus\mathcal{V}_3\oplus\mathcal{V}_5$.
