# __The Spin of a Carrier__

## Introduction

A carrier of $\mathbb{B}$ is an invariant subspace, and its type is the isomorphism class of its representation space. The **spin** is the number the type carries:

$$
s=\frac{d-1}{2},\qquad d=\dim_{\mathbb{C}}\bigl(\text{representation space}\bigr),
$$

so that $d=2s+1$. The three carriers of *The Carriers of the Biquaternion Algebra* have $d=1,2,3$ and spins $0,\tfrac12,1$.

This article defines the number, justifies the definition from the spectrum of a generator rather than from a list, and fixes the one choice the table leaves open: which of the four four-dimensional halves names the type of dimension three. All four are invariant under the conjugation and any two that are paired by an involution are the same carrier, exchanged by the central $i$. Two of them are closed under the commutator, $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{H}$, and the table names $\mathbb{B}_{\Phi}$ because the weights are read on Hermitian generators, which live in its partner $\mathbb{B}_{\Psi}$.

The carriers, their subspaces and their types are *The Carriers of the Biquaternion Algebra*; the spectrum of a generator on each carrier is *The Weights of a Carrier*, where the factor $2s+1$ is counted; the products of carriers are *The Tensor Square of the Adjoint Module*; the commutator and its structure are *The Commutator Bracket of the Biquaternion Algebra* and *The Two Symmetric Pairs of the Biquaternion Algebra*.

Nothing below is a statement of physics. The elements are written $\tilde Q$ with coefficients $Q_t,Q_x,Q_y,Q_z$, the real vector triple is $\mathfrak{k}=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$, and $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ are the Hermitian and the anti-Hermitian halves of $\mathbb{B}$.

## The Definition

**Definition (spin).** Let $(W,\rho)$ be a carrier with representation space $V_W$ of complex dimension $d$. The **spin** of the carrier is

$$
s(W)=\frac{d-1}{2}.
$$

A carrier of spin $s$ has a representation space of dimension $2s+1$; the carrier itself may be larger, and it is larger exactly when it carries a trivial summand.

**Why the half-integer shift.** A generator of the rotation algebra acting on a finite-dimensional complex space has a spectrum symmetric about zero and spaced by one, so a space that is irreducible under the algebra has the spectrum $s,s-1,\dots,-s$ for some non-negative half-integer $s$, and $2s+1$ values. The dimension and the largest weight determine each other, and the spin is the largest weight. The count $2s+1$ is the content of *The Weights of a Carrier*; the definition above is its inversion.

**The three values.** The centre has $d=1$ and $s=0$; a minimal left ideal has $d=2$ and $s=\tfrac12$; the material sector has $d=3$ and $s=1$. The values are $0,\tfrac12,1$ and there are no others, because there are no other types.

**Proposition (the spin is a function of the type, and only of it).** Two carriers of the same type have the same spin, whatever their axes, their copies or their dimensions as subspaces; two carriers of different types have different spins.

*Proof.* The spin is defined from $d$, and $d$ is an invariant of the isomorphism class of the representation space. The map $d\mapsto(d-1)/2$ is injective.

## Dimension Does Not Give the Spin

**Proposition (two carriers of one dimension, two spins).** The minimal left ideals and the material sector are both four real-dimensional, and their spins are $\tfrac12$ and $1$.

*Proof.* $S_{\pm}$ is a complex two-dimensional space, so $d=2$ and $s=\tfrac12$. $\mathbb{B}_{\Phi}$ is a real four-dimensional space and not a complex one, since multiplication by $i$ carries it to $\mathbb{B}_{\Psi}$; its representation space is the traceless part $\mathfrak{k}$, of real dimension $3$ and, complexified, of complex dimension $3$, so $d=3$ and $s=1$.

**Remark (what the difference is).** The fourth real dimension of the material sector is the central line $\mathbb{R}(ie_t)$, which the conjugation fixes pointwise. It is a trivial summand of the carrier, and a trivial summand contributes to the dimension of the subspace and not to the dimension of the representation space. The subtraction in $d-1$ is the removal of that summand and of nothing else.

**Remark (the same phenomenon in the centre).** The centre is two real-dimensional and its spin is $0$, and again the whole of it is a trivial summand: $d=1$ and $s=0$. A carrier whose representation space is trivial has spin zero whatever its real dimension, and the two occurrences are the line $\mathbb{C}e_t$ and the line $\mathbb{R}(ie_t)$.

## Why $\mathbb{B}_{\Phi}$ and Not $\mathbb{B}_{\Psi}$

The two Hermitian halves are both four real-dimensional, both invariant under conjugation by $G=\mathrm{U}(2)$, and both split as a central line plus a real vector triple. Invariance therefore does not separate them, and it is not the criterion. What separates them is the product that the conjugation differentiates to: the bracket is anti-Hermitian on both halves, so it stays inside the anti-Hermitian one and leaves the Hermitian one.

**Lemma (the sign rule).** Let $X,Y\in\mathbb{B}$, both anti-Hermitian or both Hermitian. Then $(XY)^{*}=Y^{*}X^{*}=YX$, so that

$$
XY\ \text{is Hermitian}\iff XY=YX,\qquad
XY\ \text{is anti-Hermitian}\iff XY=-YX .
$$

Consequently the commutator is anti-Hermitian and the anticommutator is Hermitian, for two anti-Hermitian elements and for two Hermitian elements alike:

$$
[X,Y]^{*}=-[X,Y],\qquad \{X,Y\}^{*}=\{X,Y\}.
$$

*Proof.* Compute $(XY)^{*}=Y^{*}X^{*}$ and substitute $X^{*}=\pm X$, $Y^{*}=\pm Y$; the two signs cancel in the product, so $Y^{*}X^{*}=YX$ in both cases. Splitting $XY=\tfrac12\{X,Y\}+\tfrac12[X,Y]$, the involution fixes the first part and reverses the second, which gives both statements.

**Theorem (the anti-Hermitian sector is closed under the bracket).** $\mathbb{B}_{\Phi}$ is closed under the commutator, and $\mathbb{B}_{\Psi}$ is not:

$$
[\mathbb{B}_{\Phi},\mathbb{B}_{\Phi}]\subseteq\mathbb{B}_{\Phi},\qquad
[\mathbb{B}_{\Psi},\mathbb{B}_{\Psi}]=\mathfrak{k}\not\subseteq\mathbb{B}_{\Psi}.
$$

*Proof.* The first inclusion is the lemma applied to two anti-Hermitian elements. For the second, the bracket of two Hermitian elements is anti-Hermitian by the lemma, and the bracket sees only the vector parts: $\tilde Q_1\wedge\tilde Q_2=\vec Q_1\times\vec Q_2$ with $\vec Q_1,\vec Q_2\in i\mathfrak{k}$, so the value is $-\vec p\times\vec q\in\mathfrak{k}$, a real vector. A witness is $i\vec e_x,i\vec e_y\in\mathbb{B}_{\Psi}$ with $(i\vec e_x)\wedge(i\vec e_y)=-\vec e_z\notin\mathbb{B}_{\Psi}$.

**Theorem (the two sectors are the same carrier).** Both sectors are invariant under the conjugation, and the two are isomorphic as modules:

$$
\operatorname{Ad}_u(\mathbb{B}_{\Psi})\subseteq\mathbb{B}_{\Psi},\qquad
\operatorname{Ad}_u(\mathbb{B}_{\Phi})\subseteq\mathbb{B}_{\Phi},\qquad
i:\mathbb{B}_{\Psi}\xrightarrow{\ \sim\ }\mathbb{B}_{\Phi}.
$$

*Proof.* The conjugation commutes with the involution, $(uQu^{*})^{*}=uQ^{*}u^{*}$, so it carries fixed elements to fixed elements and anti-fixed to anti-fixed. The number $i$ is central, so $u(iQ)u^{*}=i\,uQu^{*}$ and multiplication by $i$ intertwines the two actions; it is invertible, hence an isomorphism of carriers.

**Theorem (what separates them).** Of the two sectors only $\mathbb{B}_{\Phi}$ is closed under the commutator, by the preceding theorem. Hence the bracket is a product on $\mathbb{B}_{\Phi}$ and not on $\mathbb{B}_{\Psi}$, and the adjoint representation $\operatorname{ad}:\mathbb{B}_{\Phi}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B}_{\Phi})$, $X\mapsto[X,\cdot]$, is defined, whereas the same formula on $\mathbb{B}_{\Psi}$ carries $\mathbb{B}_{\Psi}$ out of itself.

*Proof.* The map $\operatorname{ad}$ has codomain $\operatorname{End}_{\mathbb{C}}(\mathbb{B}_{\Phi})$ only if $[X,Y]\in\mathbb{B}_{\Phi}$ for $X,Y\in\mathbb{B}_{\Phi}$, which is the closure of the preceding theorem. On $\mathbb{B}_{\Psi}$ the bracket of two elements is a real vector, by the witness $[i\vec e_x,i\vec e_y]=-2\vec e_z$, which lies in $\mathfrak{k}\subseteq\mathbb{B}_{\Phi}$.

**Corollary (four sectors, two brackets).** The four four-dimensional subspaces $\mathbb{B}_{\Psi}$, $\mathbb{B}_{\Phi}$, $\mathbb{B}_{H}$ and $\mathbb{B}_{iH}$ are all invariant under the conjugation, and exactly two of them are closed under the commutator:

$$
[\mathbb{B}_{\Phi},\mathbb{B}_{\Phi}]\subseteq\mathbb{B}_{\Phi},\qquad
[\mathbb{B}_{H},\mathbb{B}_{H}]\subseteq\mathbb{B}_{H},\qquad
[\mathbb{B}_{\Psi},\mathbb{B}_{\Psi}]=[\mathbb{B}_{iH},\mathbb{B}_{iH}]=\mathfrak{k}.
$$

*Proof.* Invariance: the group of unitaries is stable under both involutions, and $\mathbb{B}\cong M_2(\mathbb{C})$ gives $(uQu^{*})^{*}=uQ^{*}u^{*}$ and $(uQu^{*})^{\natural}=uQ^{\natural}u^{*}$, so each of the four halves of the two pairings is preserved. Closure: $\mathbb{B}_{H}\cong\mathbb{H}$ is a subalgebra of $\mathbb{B}$ under the multiplication, hence closed under the bracket, and $\mathbb{B}_{\Phi}$ is closed by the theorem above. Failure: two Hermitian elements have an anti-Hermitian bracket, and two elements of $\mathbb{B}_{iH}$ are $i$ times real quaternions, so their bracket is $-1$ times the bracket of two real quaternions, a real vector in $\mathfrak{k}$; in both cases the result lies in the closed half of the other pairing.

**Remark (the quaternion subspace is closed too).** $\mathbb{B}_{H}=\mathbb{R}e_t\oplus\mathfrak{k}$ is closed under the bracket and invariant under the conjugation, so it is a carrier of the same type as $\mathbb{B}_{\Phi}$: one trivial line and the same triple $\mathfrak{k}$, the same weights $\{0,\pm1\}$, the same spin. It is not named because it belongs to the other pairing. The algebra carries two commuting involutions, $*$ and ${}^{\natural}$, and four four-dimensional halves; the table reads the $*$-pair, $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$, because the weights are eigenvalues of Hermitian elements and the Hermitian generators $\tilde S_k=\tfrac12 i\vec e_k$ lie in $\mathbb{B}_{\Psi}$, so the sector that pairs with them is $\mathbb{B}_{\Phi}$. A reader who read the ${}^{\natural}$-pair would name $\mathbb{B}_{H}$ and write the same table.

**Remark (the choice of letter, and its warrant).** The table names one sector for the type $\mathcal{V}_3$ and the naming is a convention with a warrant. It is a convention because the two sectors are the same carrier, exchanged by the central $i$, so no count of types distinguishes them. It is warranted twice over. The adjoint action is the bracket, so the sector that is named must be closed under it, and $\mathbb{B}_{\Psi}$ is not. And the weights are read as eigenvalues of the Hermitian generators $\tilde S_k=\tfrac12 i\vec e_k$, which lie in $\mathbb{B}_{\Psi}$; a sector that carries them is the other half of the same pairing, $\mathbb{B}_{\Phi}$. The unnamed candidates supply carriers of the same type — $\mathfrak{p}=i\mathfrak{k}$ for $\mathbb{B}_{\Psi}$, and the whole of $\mathbb{B}_{H}$ — and the count of types is unchanged by the choice.

**Remark (what changes if the other sector is named).** No number changes: the same types, the same weights $\{0,\pm1\}$, the same spin. What changes is the algebra structure that comes with the name. In $\mathbb{B}_{\Phi}$ the bracket is a product and the sector is a Lie algebra; in $\mathbb{B}_{\Psi}$ the bracket produces an element of the other sector, so the sector has no bracket of its own, and the derived algebra of its bracket lies outside it. The convention of the corpus names the sector that keeps its own bracket.

## The Sector and the Traceless Part

**Proposition.** $\mathbb{B}_{\Phi}=\mathbb{R}(ie_t)\oplus\mathfrak{k}$ is a direct sum of two invariant subspaces of the adjoint action, the first trivial and the second irreducible of real dimension $3$.

*Proof.* The line is central, hence fixed. The triple is the derived algebra, $[\mathbb{B}_{\Phi},\mathbb{B}_{\Phi}]=\mathfrak{k}$, hence invariant; it is irreducible because it is the adjoint module of $\mathrm{SU}(2)$ on its Lie algebra, of dimension $3$. The sum is direct because a real vector is never a multiple of $ie_t$.

**Corollary.** The carrier is the traceless part $\mathfrak{k}$: invariant, closed under the bracket, irreducible, of type $\mathcal{V}_3$. The sector is named rather than the triple because the entries of the table are the blocks that the conjugations cut out, and $\mathfrak{k}$ is the traceless part of a block and not a block. The sector carries the carrier; the carrier is the traceless part of the sector.

**Remark (the two real forms).** $\mathfrak{k}$ and $\mathfrak{p}=\operatorname{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}$ are two real forms of the same complex three-dimensional module, and the conjugation by $G$ preserves each. The complex carrier is one object and the real picture shows two copies of the same matrix; the weights are integer in the complex picture and the two copies are what the real structure makes of one weight string. The details are *The Two Symmetric Pairs of the Biquaternion Algebra*, §*The Hermitian Pair*.

## A Remark on Other Readings of the Same Number

Earlier versions of this corpus reached the number $s$ by other routes, and the routes are still in the literature. They are recorded here as readings of the definition, not as definitions.

| legacy reading | the object | how it computes $s$ | why the definition replaces it |
|---|---|---|---|
| the highest weight | the largest eigenvalue of a fixed generator on the carrier | $s$ is the largest eigenvalue | it presupposes a chosen generator, and the carrier is defined before any generator is chosen |
| the Casimir eigenvalue | the scalar by which a central element of the enveloping algebra acts | $s$ is recovered from $\lambda=s(s+1)$ | the scalar determines $s$ only up to sign, and it is a function of the type, not a definition of it |
| the tensor degree | the number of factors of the defining module in a decomposition of a tensor power | $s$ is half the number of factors | the decomposition is a theorem about the carrier, and it needs the type to be stated |
| the Peirce index | the sign with which right multiplication by $i\vec u$ acts on the copy | returns $+$ or $-$ | it separates copies of one type and does not change $s$ |
| the central sign | the two signs with which $-e_t$ acts | returns $+$ or $-$ | it separates the integrality classes of the carriers, integer and half-integer, and is a consequence of the type |

**Remark.** The first three rows are one number read three ways: the carrier fixes the dimension, the dimension is the length of the weight string, and the Casimir is a polynomial in the length. The last two rows are signs, they belong to the copies and to the integrality classes, and neither of them is a value of $s$. The definition adopted here is the first column: the carrier comes first, and the readings are computed from it when a reading is wanted.

**Remark (what is not claimed).** The definition is not a property of an element: an element of $\mathbb{B}$ belongs to whatever carrier its coordinates put it in, and the same element can be read in two carriers when the two meet, on the line $\mathbb{R}(ie_t)$ shared by the centre and the sector and on the lines $\mathbb{R}(i\tilde\Pi_{\pm})$ shared by the ideals and the sector. The definition is not a property of a module either: there is one simple module and there are three carriers, and a module-theoretic statement can say $\tfrac12$ any number of times but cannot say $0$ or $1$ without leaving the module category.

## Summary

The spin of a carrier is $s=(d-1)/2$, where $d$ is the complex dimension of its representation space, so that $d=2s+1$ is the length of the weight string of a generator. The three carriers have spins $0$, $\tfrac12$ and $1$.

The definition uses the representation space and not the subspace, because two carriers are four real-dimensional and one of them carries a trivial line: the centre contributes $d=1$ from a real two-dimensional carrier, and the material sector contributes $d=3$ from a real four-dimensional one.

The third carrier is named by $\mathbb{B}_{\Phi}$ and not by $\mathbb{B}_{\Psi}$. The two sectors are the same carrier, since the conjugation commutes with the involution and the central $i$ intertwines the two actions; what separates them is the product. Two anti-Hermitian elements have an anti-Hermitian bracket, so $\mathbb{B}_{\Phi}$ is closed under the commutator and carries the adjoint representation of itself; two Hermitian elements have an anti-Hermitian bracket, so $\mathbb{B}_{\Psi}$ is not closed, its bracket landing in the real vector triple. The Hermitian half is closed under the symmetrised product instead. The other closed candidate, the quaternion subspace $\mathbb{B}_{H}$, gives the same type and the same numbers, and is not named because it belongs to the other pairing of involutions; the choice is a convention, and the warrant is that the Hermitian generators live in $\mathbb{B}_{\Psi}$ and the adjoint action lives in $\mathbb{B}_{\Phi}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $s$ | the spin of a carrier, $s=(d-1)/2$ |
| $d$ | the complex dimension of the representation space, $d=2s+1$ |
| $\mathcal{V}_d$ | the type of the carrier whose representation space has dimension $d$ |
| $\mathbb{B}_{C}$ | the centre, a carrier of type $\mathcal{V}_1$ and spin $0$ |
| $S_{\pm}$ | the minimal left ideals, carriers of type $\mathcal{V}_2$ and spin $\tfrac12$ |
| $\mathbb{B}_{\Phi}$ | the anti-Hermitian sector, a carrier of type $\mathcal{V}_3$ and spin $1$ |
| $\mathbb{B}_{\Psi}$ | the Hermitian sector, not closed under the commutator, hence not an adjoint carrier |
| $\mathfrak{k}$, $\mathfrak{p}$ | the real and the imaginary vector triples, the two real forms of the adjoint module |
| $\{X,Y\}$ | the anticommutator $XY+YX$, the product that closes $\mathbb{B}_{\Psi}$ |
| trivial summand | the part of a carrier on which the action is the identity |

## Further Reading

- [The Carriers of the Biquaternion Algebra](the-carriers-of-the-biquaternion-algebra.html), for the definition of a carrier, the three types and the proof that there are no others
- [The Weights of a Carrier](the-weights-of-a-carrier.html), for the spectrum of a generator and the count $2s+1$
- [The Tensor Square of the Adjoint Module](the-tensor-square-of-the-adjoint-module.html), for the products of carriers and the absence of a higher type
- [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html), for the two Hermitian halves, their bases and their dimensions
- *The Commutator Bracket of the Biquaternion Algebra*, for the bracket, its alternation and the formula in the vector parts
- *The Two Symmetric Pairs of the Biquaternion Algebra*, for the closure of the two halves under the two products
- *The Bracket on the Subspaces of the Biquaternion Algebra*, for the identification $\mathfrak{k}\cong\mathfrak{su}(2)$
- [Introduction to the Carrier of Dimension 1 over C](the-carrier-of-dimension-1.html), [Introduction to the Peirce Basis over C](the-peirce-basis-over-c.html) and [Introduction to the Carriers of Dimension 4 over R](the-carriers-of-dimension-4.html), for the carriers of each type listed one type to an article
- [The Minimal Left Ideals of the Biquaternion Algebra](the-minimal-left-ideals-of-the-biquaternion-algebra.html), for the two-dimensional carrier
- Hermann Weyl, *The Theory of Groups and Quantum Mechanics* (Dover, 1950), for the weight strings and their length.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for the classification of the irreducible representations of $\mathfrak{su}(2)$ by their dimension.
