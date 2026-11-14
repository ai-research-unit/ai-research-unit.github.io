# __Introduction to the Carriers of Dimension 4 over R__

## Introduction

The third case is the one the two involutions produce. Applying the Hermitian conjugation and the conjugation of the coefficients to the algebra cuts it into four real subspaces of dimension four, and each of them is a central real line plus a triple. The article shows how the cutting is done, states which of the four survives each of the three tests, and settles which of them the tables name.

The dimension needs one word of care, because it is the only case where the field matters. Over $\mathbb{C}$ the algebra has a single subspace of dimension $4$, namely $\mathbb{B}$ itself, and it is reducible under both actions, so it is not a carrier. Over $\mathbb{R}$ the algebra has four distinguished halves of dimension $4$, and those are the subspaces of this article. The number in the title is therefore a real dimension, and the three cases of the group are $1$ and $2$ over $\mathbb{C}$ and $4$ over $\mathbb{R}$.

The other two cases are *Introduction to the Carrier of Dimension 1 over C and *Introduction to the Carriers of Dimension 2 over C. The definition and the full list are *The Carriers of the Biquaternion Algebra*; the eigenvalue reading is *The Weights of a Carrier*.

Nothing below is a statement of physics. The elements are written $X,Y$; the units are $e_t,\vec e_x,\vec e_y,\vec e_z$ with $e_t^2=e_t$ and $\vec e_k^{2}=-e_t$; $*$ is the Hermitian conjugation; $\bar X$ is the conjugation of the complex coefficients; and $G=\mathrm{U}(2)$ is the group of units of modulus one.

## How the Halves Are Obtained

Write every element in its real and imaginary quaternion parts,

$$
X=q+ip,\qquad q,p\in\mathbb{H},
$$

with $q,p$ real quaternions. The Hermitian conjugation and the coefficient conjugation act by

$$
X^{*}=\bar q-i\bar p,\qquad \bar X=\bar q+i\bar p,
$$

because the Hermitian transpose of the matrix of a real quaternion $q$ is the matrix of its quaternion conjugate $\bar q$.

**Definition (the two involutions).** The two maps

$$
\sigma(X)=X^{*},\qquad \tau(X)=\bar X
$$

are real-linear involutions of $\mathbb{B}$, and they commute up to sign on the imaginary part; their joint sign pattern is a complete set of invariants.

**Theorem (the four halves).** The four subspaces defined by the sign conditions on $(q,p)$ are

$$
\mathbb{B}_{\Phi}=\{X:X^{*}=-X\}=\mathbb{R}(ie_t)\oplus\mathfrak{k},
$$
$$
\mathbb{B}_{\Psi}=\{X:X^{*}=X\}=\mathbb{R}e_t\oplus\mathfrak{p},
$$
$$
\mathbb{B}_{H}=\{X:\bar X=X\}=\mathbb{H}=\mathbb{R}e_t\oplus\mathfrak{k},
$$
$$
\mathbb{B}_{iH}=\{X:\bar X=-X\}=i\mathbb{H}=\mathbb{R}(ie_t)\oplus\mathfrak{p},
$$

where

$$
\mathfrak{k}=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\},\qquad
\mathfrak{p}=i\mathfrak{k}=\operatorname{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}.
$$

*Proof.* For $\mathbb{B}_{\Phi}$: $q+ip$ is anti-Hermitian when $\bar q=-q$ and $\bar p=p$, that is when $q$ is pure and $p$ is a real scalar; those elements are $\vec v+i\lambda e_t$. For $\mathbb{B}_{\Psi}$: Hermitian when $\bar q=q$ and $\bar p=-p$, that is $q=\lambda e_t$ and $p$ pure; those are $\lambda e_t+i\vec v$. For $\mathbb{B}_{H}$ and $\mathbb{B}_{iH}$ the coefficient conjugation acts on $q+ip$ by $\bar q+i\bar p$, so the fixed elements have $p=0$ and the anti-fixed have $q=0$.

**Corollary (the dimensions).** Each half has real dimension $4$, and each is the direct sum of a real line and a real triple. The two triples are $\mathfrak{k}$ and $\mathfrak{p}=i\mathfrak{k}$.

**Remark (the four halves are not four algebras).** The lines are $\mathbb{R}e_t$ in two of them and $\mathbb{R}(ie_t)$ in the other two; the triples are $\mathfrak{k}$ in two and $\mathfrak{p}$ in the other two. The four are the four ways of pairing one line with one triple.

## Invariance

**Theorem (every half is invariant).** For every unit $u$ and every half $\mathbb{B}_{\bullet}$ of the four,

$$
\operatorname{Ad}_u(\mathbb{B}_{\bullet})\subseteq\mathbb{B}_{\bullet}.
$$

*Proof.* The conjugation by a unit preserves the Hermitian conjugation, $\operatorname{Ad}_u(X^{*})=(\operatorname{Ad}_uX)^{*}$, because $u^{*}=u^{-1}$, and it preserves the coefficient conjugation, which is the same operation composed with the quaternionic conjugation. It therefore preserves each sign condition. Equivalently, $\operatorname{Ad}_u$ acts on $\mathfrak{k}$ by the rotation $R\in SO(3)$ and on $\mathfrak{p}$ by the same rotation, and it fixes the two central lines.

**Corollary (the four halves are the blocks of the conjugation).** The group $G$ acts on each half, and the halves are the smallest real subspaces containing the carriers and closed under the two involutions.

## The Bracket Test

**Theorem (two halves are Lie subalgebras).** Of the four halves exactly two are closed under the commutator:

$$
[\mathbb{B}_{\Phi},\mathbb{B}_{\Phi}]\subseteq\mathbb{B}_{\Phi},\qquad
[\mathbb{B}_{H},\mathbb{B}_{H}]\subseteq\mathbb{B}_{H},\qquad
[\mathbb{B}_{\Psi},\mathbb{B}_{\Psi}]=\mathfrak{k},\qquad
[\mathbb{B}_{iH},\mathbb{B}_{iH}]=\mathfrak{k}.
$$

*Proof.* For $\mathbb{B}_{\Phi}$ the sign rule suffices: if $X^{*}=-X$ and $Y^{*}=-Y$ then $[X,Y]^{*}=Y^{*}X^{*}-X^{*}Y^{*}=YX-XY=-[X,Y]$. $\mathbb{B}_{H}=\mathbb{H}$ is a subalgebra, hence closed. For the two failures the scalar part cancels: in $\mathbb{B}_{\Psi}$ one has $[i\vec w,i\vec z]=-[\vec w,\vec z]=-2\,\vec w\times\vec z\in\mathfrak{k}$ for real $\vec w,\vec z$, and in $\mathbb{B}_{iH}$ the same identity holds for $X,Y\in\mathbb{H}$. The witness is $[i\vec e_x,i\vec e_y]=-2\vec e_z$, which lies in $\mathfrak{k}$ and in neither half.

**Corollary (the bracket leaves the halves).** Every bracket of two elements of a half lands in $\mathfrak{k}$, so the derived algebra $[\mathbb{B},\mathbb{B}]=\mathfrak{k}$ is the smallest subspace that contains all four brackets.

## The Product Test

**Proposition (one half is an algebra).** Of the four halves only $\mathbb{B}_{H}$ is closed under the product:

$$
\mathbb{B}_{H}\mathbb{B}_{H}\subseteq\mathbb{B}_{H},\qquad
\mathbb{B}_{\Phi}\mathbb{B}_{\Phi}\not\subseteq\mathbb{B}_{\Phi},\qquad
\mathbb{B}_{\Psi}\mathbb{B}_{\Psi}\not\subseteq\mathbb{B}_{\Psi},\qquad
\mathbb{B}_{iH}\mathbb{B}_{iH}\not\subseteq\mathbb{B}_{iH}.
$$

*Proof.* $\mathbb{B}_{H}=\mathbb{H}$ is the real quaternion algebra. For the three failures: $(ie_t)\vec e_x=i\vec e_x\notin\mathbb{B}_{\Phi}$; $(i\vec e_x)(i\vec e_y)=-\vec e_z\notin\mathbb{B}_{\Psi}$; and the same product, with both factors in $\mathbb{B}_{iH}$, gives $-\vec e_z\notin\mathbb{B}_{iH}$.

## The Triples Inside the Halves

**Theorem (the triples are the traceless parts).** The traceless part of each half, taken with respect to the real trace, is a triple, and

$$
\operatorname{tr}\mathbb{B}_{\Phi}=\mathbb{R}(ie_t),\quad
\operatorname{tr}\mathbb{B}_{\Psi}=\mathbb{R}e_t,\quad
\operatorname{tr}\mathbb{B}_{H}=\mathbb{R}e_t,\quad
\operatorname{tr}\mathbb{B}_{iH}=\mathbb{R}(ie_t).
$$

*Proof.* The trace of $\lambda e_t+\vec v$ is $2\lambda$ and the trace of $\lambda e_t+i\vec v$ is $2\lambda$; the pure parts are traceless.

**Theorem (the two triples are one module).** The central element $i$ carries $\mathfrak{k}$ onto $\mathfrak{p}$ and intertwines the two adjoint actions.

*Proof.* $i(\vec v)=i\vec v$ and $i[a,b]=[ia,ib]$.

**Corollary (the halves are reducible).** Each half is a line plus a triple, so no half is irreducible for the conjugation. The carriers are the triples, and the halves are the smallest real subspaces that contain them and are stable under the two involutions.

## The Dimension Over the Complex Numbers

**Proposition (only one complex subspace of dimension four).** The only complex subspace of $\mathbb{B}$ of complex dimension $4$ is $\mathbb{B}$, and it is reducible for both actions.

*Proof.* A complex subspace of dimension $4$ has real dimension $8$, which is $\dim_{\mathbb{R}}\mathbb{B}$. For left multiplication, $\mathbb{B}=S\oplus S'$ with the two columns of *Introduction to the Carriers of Dimension 2 over C. For the conjugation, $\mathbb{B}=\mathbb{C}e_t\oplus\mathbb{C}(ie_t)\oplus\mathfrak{k}_{\mathbb{C}}$ by *The Tensor Square of the Adjoint Module*.

**Remark (why the halves are real).** None of the four halves is a complex subspace: $i\mathbb{B}_{\Phi}=\mathbb{B}_{\Psi}$, so multiplication by $i$ carries each half onto a different one. A half is a real form, and a real form is not a carrier in the complex category; the triple inside it is.

## Why the Tables Name $\mathbb{B}_{\Phi}$

The three tests leave a tie between $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{H}$: both contain $\mathfrak{k}$, both are closed under the bracket, both have $\mathfrak{k}$ as traceless part, and the product test excludes both from being the answer — it excludes $\mathbb{B}_{\Phi}$ from being an algebra and $\mathbb{B}_{H}$ from being the smallest.

**Theorem (the naming is the Lie algebra of the group).** $\mathbb{B}_{\Phi}$ is the Lie algebra of the group of units of modulus one, and $\mathfrak{k}$ is its derived algebra:

$$
\mathbb{B}_{\Phi}=\mathfrak{u}(2)=\operatorname{Lie}(G),\qquad
[\mathbb{B}_{\Phi},\mathbb{B}_{\Phi}]=\mathfrak{k}=\mathfrak{su}(2).
$$

*Proof.* An element $X$ lies in $\operatorname{Lie}(G)$ exactly when $e^{tX}$ is unitary for real $t$, that is when $X^{*}=-X$ and $\operatorname{tr}X$ is imaginary; those are the anti-Hermitian elements, which are $\mathbb{B}_{\Phi}$. The derived algebra is computed in the previous sections.

**Remark (the two exclusions are different).** $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{iH}$ are excluded by a computation: their brackets leave them. $\mathbb{B}_{H}$ is excluded by no computation at all. It is the Hermitian translate $i\mathbb{B}_{\Phi}$ of the Lie algebra, it carries no group of its own, and its inclusion would make the table name an algebra rather than the Lie algebra of an action.

**Remark (the acting group is the real one).** The central phase of $G$ acts trivially on the algebra: for $u=\lambda s$ with $\lvert\lambda\rvert=1$ and $\det s=1$, one has $\operatorname{Ad}_u=\operatorname{Ad}_s$ because $\lambda$ cancels. The acting group is therefore $\mathrm{Sp}(1)$, whose Lie algebra is $\mathfrak{k}$ itself. Read this way, the carrier is the whole Lie algebra of the group that acts, and the block $\mathbb{B}_{\Phi}$ is a convenience of the table.

## Summary

The half of the algebra is obtained by applying the Hermitian conjugation and the coefficient conjugation: the four joint sign conditions produce $\mathbb{B}_{\Phi}$, $\mathbb{B}_{\Psi}$, $\mathbb{B}_{H}$ and $\mathbb{B}_{iH}$, each of real dimension $4$, each a central real line plus a real triple.

All four are invariant under the conjugation. Exactly two, $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{H}$, are closed under the bracket, and exactly one, $\mathbb{B}_{H}$, is closed under the product. The carriers are the two triples $\mathfrak{k}$ and $\mathfrak{p}=i\mathfrak{k}$, not the halves. The table names $\mathbb{B}_{\Phi}$ because it is the Lie algebra of the group of units and $\mathfrak{k}$ is its derived algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X=q+ip$ | the real and imaginary quaternion parts |
| $X^{*}=\bar q-i\bar p$ | the Hermitian conjugation |
| $\bar X=\bar q+i\bar p$ | the conjugation of the coefficients |
| $\mathbb{B}_{\Phi}$ | the anti-Hermitian half, $\mathbb{R}(ie_t)\oplus\mathfrak{k}$, $\mathfrak{u}(2)$ |
| $\mathbb{B}_{\Psi}$ | the Hermitian half, $\mathbb{R}e_t\oplus\mathfrak{p}$ |
| $\mathbb{B}_{H}=\mathbb{H}$ | the real quaternions, $\mathbb{R}e_t\oplus\mathfrak{k}$ |
| $\mathbb{B}_{iH}=i\mathbb{H}$ | the imaginary quaternions, $\mathbb{R}(ie_t)\oplus\mathfrak{p}$ |
| $\mathfrak{k}$ | the real pure quaternions, the real triple |
| $\mathfrak{p}=i\mathfrak{k}$ | the imaginary triple |
| $G=\mathrm{U}(2)$ | the group of units of modulus one |

## Further Reading

- [The Carriers of the Biquaternion Algebra](the-carriers-of-the-biquaternion-algebra.html), for the definition and the list of all the subspaces.
- [The Carriers of Dimension 1 over C](the-carrier-of-dimension-1.html), for the centre.
- [Introduction to the Peirce Basis over C](the-peirce-basis-over-c.html), for the idempotents, the four corners and the two summands.
- [The Tensor Square of the Adjoint Module](the-tensor-square-of-the-adjoint-module.html), for $\mathbb{B}=\mathcal{V}_1\oplus\mathcal{V}_1\oplus\mathcal{V}_3$ and the two trivial lines.
- [The Weights of a Carrier](the-weights-of-a-carrier.html), for the eigenvalues on the triples.
- [The Adjoint Action of a Lie Algebra](the-adjoint-action-of-a-lie-algebra.html), for the rotation $R\in SO(3)$ attached to a unit.
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the rules that express every product with two inserted conjugations.
- [Remarkable Subspaces and the Four General Products, Forms and Norms](remarkable-subspaces-and-the-four-general-products-forms-and-norms.html), for the six remarkable subspaces among the halves and the triples.
