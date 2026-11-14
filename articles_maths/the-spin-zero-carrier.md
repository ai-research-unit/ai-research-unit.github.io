# __The Spin-Zero Carrier__

## Introduction

The biquaternion algebra $\mathbb{B}$ carries exactly one carrier of the trivial type, and the carrier is the centre $\mathbb{C}e_t$. The type has complex dimension one and spin $0$, and the subspace that realises it is forced: no axis, no sign and no choice enter.

This article proves three things. The fixed space of the conjugation is the centre, and nothing else. A carrier of the trivial type is a trivial module, hence lies in the fixed space, hence is the centre; so there is one and not a family. And the centre is not a Peirce line of any complete family of idempotents, so the object has no companion nilpotent, no coordinate vector and no weight string of the form $\pm$.

The count of the three types is *The Carriers of the Biquaternion Algebra*, the number attached to a type is *The Spin of a Carrier*, and the spectra of all three are *The Weights of a Carrier*, §*The Three Spectra*. The two other carriers are *The Spin-Half Carriers* and *The Spin-One Carriers*.

Nothing below is a statement of physics. The elements are written $X,Y$; the units are $e_t,\vec e_x,\vec e_y,\vec e_z$ with $e_t^2=e_t$ and $\vec e_k^2=-e_t$; the group of unitary units is $G=\mathrm{U}(2)$; and $*$ is the Hermitian conjugation.

## The Fixed Space of the Conjugation

**Definition (the conjugation).** For a unit $u$ the **conjugation** is $\operatorname{Ad}_u(X)=uXu^{*}$, and its derived form is $\operatorname{ad}_Y(X)=[Y,X]$.

**Proposition (the centre is fixed pointwise).** For every unit $u$ and every $\lambda\in\mathbb{C}$,

$$
\operatorname{Ad}_u(\lambda e_t)=\lambda e_t,\qquad \operatorname{ad}_Y(\lambda e_t)=0 .
$$

*Proof.* $u(\lambda e_t)u^{*}=\lambda\,ue_tu^{*}=\lambda e_t$ because $e_t$ is the unit and $u$ is invertible; and $[Y,\lambda e_t]=0$ because $\lambda e_t$ is central. The two statements are the same computation read on the group and on its algebra.

**Theorem (the fixed space is the centre).** A subspace $W$ on which $G$ acts trivially is contained in $\mathbb{C}e_t$, and the fixed space of $G$ is exactly $\mathbb{C}e_t$.

*Proof.* The fixed elements are the matrices commuting with every unitary, in the model $\mathbb{B}\cong M_2(\mathbb{C})$ of *The $M_2(\mathbb{C})$ Pauli Representation*. The unitary group spans $M_2(\mathbb{C})$ linearly, so the commutant of $G$ in $M_2(\mathbb{C})$ is the commutant of $M_2(\mathbb{C})$, which is $\mathbb{C}\mathrm I_2$. The preimage of $\mathbb{C}\mathrm I_2$ is $\mathbb{C}e_t$. A trivial module consists of fixed vectors, so it lies in that line.

## Uniqueness

**Theorem (one carrier of the trivial type).** There is exactly one carrier of type $\mathcal{V}_1$, and it is $\mathbb{C}e_t$. No parameter and no sign enter, in contrast with the other two types.

*Proof.* A carrier of type $\mathcal{V}_1$ is a nonzero space on which the action is the identity. By the theorem above it lies in $\mathbb{C}e_t$, which is a complex line; a nonzero subspace of a line is the line. So the carrier is $\mathbb{C}e_t$ and the description admits no choice.

**Corollary (why the other two types have families).** The count of carriers is one, a sphere, and a pair, for the three types. The reason is not the dimension of the type but the size of the space of solutions: the trivial type is realised by the unique fixed line, the defining type by the sphere of minimal left ideals, and the adjoint type by the traceless parts of the four halves.

**Remark (a real line inside the centre).** Read over the reals, $\mathbb{C}e_t=\mathbb{R}e_t\oplus\mathbb{R}(ie_t)$ contains a circle of real lines, each invariant and each irreducible as a real space, and all of them trivial. They are not carriers of the complex algebra: the action is complex-linear and a carrier is a complex subspace, so a real line is excluded by the type of the object and not by a failure of invariance. The same remark explains the entry for the third type in the table of *The Carriers of the Biquaternion Algebra*, where a real block stands for the complex carrier inside it.

## Not a Peirce Line

The centre is not one of the four Peirce lines of a complete family. The statement is worth proving, because it is the reason the spin-zero carrier has none of the machinery of the other two.

**Theorem (the centre meets every Peirce line in zero).** Let $\tilde\Pi_{+},\tilde\Pi_{-}$ be a complete family, $\tilde\Pi_{\pm}^{2}=\tilde\Pi_{\pm}$, $\tilde\Pi_{+}\tilde\Pi_{-}=0$, $\tilde\Pi_{+}+\tilde\Pi_{-}=e_t$, and let $\mathbb{B}_{st}=\tilde\Pi_s\mathbb{B}\tilde\Pi_t$ be the four Peirce lines. Then

$$
\mathbb{B}_{st}\cap\mathbb{C}e_t=0
$$

for every pair $(s,t)$, and $e_t$ lies in no Peirce line.

*Proof.* An element of $\mathbb{B}_{st}$ satisfies $X=\tilde\Pi_sX\tilde\Pi_t$. Take $X=\lambda e_t$ with $\lambda\neq0$; then $\tilde\Pi_s\tilde\Pi_t=\lambda e_t$, and the left side is $\delta_{st}\tilde\Pi_s$, which is an idempotent of rank one and not the unit. A nonzero multiple of $e_t$ is not idempotent, so no such $X$ exists. The same computation at $\lambda=0$ gives only the zero element.

**Corollary (no companion, no coordinates, no string).** The centre has no companion nilpotent, no Peirce coordinate vector, and no weight string of the form $+\lambda,-\lambda$. Its weight string is the single number $0$.

*Proof.* The companion nilpotents of a family lie in the mixed lines $\mathbb{B}_{-+}$ and $\mathbb{B}_{+-}$, and the coordinates of *The Companion Nilpotents of the Biquaternion Algebra* are taken in a Peirce column. The centre lies in no corner and in no column, so neither applies. The string is computed in §*The Readings* below.

**Remark (what the centre is, in Peirce language).** The centre is the diagonal corner of the degenerate family $(e_t)$, whose complement is $0$. That family is not a complete family of two nonzero idempotents, and it has no mixed lines, so the Peirce decomposition it gives is the trivial one, $\mathbb{B}=\mathbb{B}_{++}$.

## The Readings

The carrier is one object and it has four readings. They agree, and each is computed in one line.

**The weight.** The generator of *The Weights of a Carrier* is $\tilde S(\vec u)=\tfrac12 i\vec u\cdot\vec e$, Hermitian. On $\mathbb{C}e_t$ it acts by the commutator, which is zero, so the weight string is $\{0\}$ and its single member is the highest weight. The spin is $(1-1)/2=0$.

**The quadratic element.** The element $C=\sum_k\tilde S_k^{2}=\tfrac34 e_t$ is central, so $\operatorname{ad}_C=0$ and $C$ acts by the scalar $0$ on this carrier. The same scalar read as $s(s+1)$ at $s=0$ is $0$.

**The integrality class.** Left multiplication by $-e_t$ is the scalar $-1$ on the two ideals; on the centre the action is the conjugation, and $-e_t$ is central, so it acts by $+1$. The centre therefore belongs to the integer class, as it must for spin $0$.

**The triviality.** The kernel of the action is the whole of $G$, since every unit acts as the identity. The centre is the only carrier on which the action has a nonzero kernel.

| reading | value on $\mathbb{C}e_t$ |
|---|---|
| the weight string | $0$ |
| the highest weight, that is the spin | $0$ |
| the quadratic element | $0$ |
| the sign of $-e_t$ | $+1$ |
| the kernel of the action | $G$ |

## Summary

The spin-zero carrier of $\mathbb{B}$ is the centre $\mathbb{C}e_t$, and there is exactly one. The conjugation fixes it pointwise and its derived form kills it, so the module is trivial; the fixed space of $G$ is exactly the centre, so a trivial carrier is a complex line inside a complex line, which is the line itself.

The carrier is not a Peirce line. Every corner of a complete family is an idempotent of rank one, and no corner contains a nonzero central element, so the centre has no companion nilpotent, no coordinate vector and no weight string of the form $\pm$. Its readings are the weight $0$, the spin $0$, the value $0$ of the quadratic element and the sign $+1$ of $-e_t$.

Read over the reals the centre contains a circle of invariant real lines, all trivial; they are the same carrier read in a smaller category and are not counted separately.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, $M_2(\mathbb{C})$, complex dimension four |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the units, $e_t^2=e_t$ and $\vec e_k^{2}=-e_t$ |
| $G=\mathrm{U}(2)$ | the group of unitary units |
| $\operatorname{Ad}_u(X)=uXu^{*}$ | the conjugation by a unit |
| $\operatorname{ad}_Y(X)=[Y,X]$ | the commutator, the derived form of the conjugation |
| $\mathbb{C}e_t$ | the centre, the fixed space of $G$, the spin-zero carrier |
| $\tilde S_k=\tfrac12 i\vec e_k$ | the Hermitian generators |
| $C=\sum_k\tilde S_k^{2}=\tfrac34e_t$ | the quadratic element |
| $\mathcal{V}_1$ | the trivial type, of complex dimension one |
| $\tilde\Pi_{\pm}$, $\mathbb{B}_{st}$ | a complete family and its four Peirce lines |

## Further Reading

- [The Carriers of the Biquaternion Algebra](the-carriers-of-the-biquaternion-algebra.html), for the definition of a carrier, the table of the three types and the completeness of the count.
- [The Spin of a Carrier](the-spin-of-a-carrier.html), for the spin as a function of the type and the three values $0,\tfrac12,1$.
- [The Weights of a Carrier](the-weights-of-a-carrier.html), for the three spectra, the quadratic element and the integrality class.
- [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html), for the centre among the six remarkable subspaces and the decompositions cut by the conjugations.
- [Peirce Decompositions of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the complete family, the four corners and the reason the centre lies in none of them.
- [The Companion Nilpotents of the Biquaternion Algebra](the-companion-nilpotents-of-the-biquaternion-algebra.html), for the companion corner and the coordinate vector of a Peirce carrier.
- [The Spin-Half Carriers](the-spin-half-carriers.html), for the sphere of minimal left ideals.
- [The Spin-One Carriers](the-spin-one-carriers.html), for the two traceless parts and the four halves.
- [The Tensor Square of the Adjoint Module](the-tensor-square-of-the-adjoint-module.html), for the trivial summand beside the adjoint one.
