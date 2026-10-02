
# __Involutive Local Rings__

## Introduction

A local ring has one maximal ideal, and an involution of it is therefore severely constrained: an involution is an isomorphism with the opposite ring, and such an isomorphism carries maximal ideals to maximal ideals, so the unique maximal ideal is carried to itself and the involution descends to the residue field. An **involutive local ring** is a local ring with an involution, and the structure it presents is a pair of involutions, the given one on the ring and its **residue involution** on the field, tied by the requirement that the maximal ideal be stable; the questions are what the involution does to the maximal ideal and its powers, what the fixed subring is, and when an involution of the residue field can be lifted back to the ring.

This article treats those three questions in the elementary range: the stability of the maximal ideal, the induced involution on the residue field, the fixed subring and its residue field, and the lifting problem with the completeness hypothesis under which it is soluble. It assumes *Rings* for the local ring, its maximal ideal and its units, *Involutive Rings* for the involution and the fixed set, and *Field and Ring Automorphisms* for the automorphism group; the involution of a valued field and the residue of a valuation are treated with the valued fields of a later category, and the completion is used only as a hypothesis and is named as the boundary. Throughout, $(A, \mathfrak m)$ is a local ring with $1 \neq 0$, $k = A/\mathfrak m$ is its residue field, $\sigma$ is an involution of $A$, and $\sigma_k$ is the induced involution of $k$ when it exists; $A^\sigma$ is the fixed subring.

## The Maximal Ideal and the Residue Involution

**Theorem.** An involution $\sigma$ of a local ring $(A, \mathfrak m)$ carries the maximal ideal to itself, $\sigma(\mathfrak m) = \mathfrak m$, and every power of the maximal ideal likewise, $\sigma(\mathfrak m^n) = \mathfrak m^n$. Consequently $\sigma$ descends to the residue field: the map

$$
\sigma_k(a + \mathfrak m) = \sigma(a) + \mathfrak m
$$

is a well-defined involution of $k$.

**Proof.** $\sigma$ is a ring isomorphism $A \to A^{\mathrm{op}}$, and an isomorphism carries ideals to ideals and maximal ideals to maximal ideals; the opposite ring has the same ideals, so $\sigma(\mathfrak m)$ is a maximal ideal of $A$, and $\mathfrak m$ is the unique one, so $\sigma(\mathfrak m) = \mathfrak m$. For the powers, $\sigma(\mathfrak m^n) = \sigma(\mathfrak m)^n = \mathfrak m^n$. The descent is well defined because $\sigma(\mathfrak m)\subseteq \mathfrak m$: if $a - b \in \mathfrak m$ then $\sigma(a) - \sigma(b) = \sigma(a-b) \in \mathfrak m$. Additivity and the unit are inherited from $\sigma$, the anti-multiplicativity descends because the quotient of an anti-automorphism by a stable ideal is an anti-automorphism, $k$ is a field and therefore commutative, and $\sigma_k^2 = \mathrm{id}$ because $\sigma^2 = \mathrm{id}$.

**Corollary.** The involution permutes the prime ideals of $A$ that contain a given power of $\mathfrak m$, and it fixes $\mathfrak m$ and the powers $\mathfrak m^n$ as sets; the induced map on the associated graded ring $\bigoplus_n \mathfrak m^n/\mathfrak m^{n+1}$ is an involution that is the identity on the scalars of $k$ in the sense of the residue involution.

**Proof.** The powers are stable by the theorem, and the induced map on each quotient is well defined because $\sigma(\mathfrak m^n) = \mathfrak m^n$ and $\sigma(\mathfrak m^{n+1}) = \mathfrak m^{n+1}$; additivity, anti-multiplicativity and order two pass to the graded pieces.

**Remark.** The stability of $\mathfrak m$ is the whole content: a general ideal need not be stable, and the involution of a ring with several maximal ideals permutes them. The local hypothesis buys exactly the stability, and with it the residue involution, which is the coarsest invariant of $\sigma$.

## The Fixed Subring

**Proposition.** The fixed subring $A^\sigma$ is a local ring with maximal ideal

$$
\mathfrak m^\sigma = A^\sigma \cap \mathfrak m = \{a \in \mathfrak m : \sigma(a) = a\},
$$

and its residue field is the fixed field of the residue involution,

$$
A^\sigma/\mathfrak m^\sigma \cong k^{\sigma_k},
$$

when $2$ is invertible in $A$. Without the hypothesis on $2$ the natural map $A^\sigma/\mathfrak m^\sigma \to k^{\sigma_k}$ is still injective, and it is surjective exactly when every element of $k^{\sigma_k}$ has a $\sigma$-fixed lift.

**Proof.** An element $a \in A^\sigma$ is a unit of $A$ exactly when it is a unit of $A^\sigma$, because $\sigma(a^{-1}) = \sigma(a)^{-1} = a^{-1}$ for a fixed unit $a$; hence the non-units of $A^\sigma$ are $A^\sigma\cap\mathfrak m$, which is therefore the unique maximal ideal and $A^\sigma$ is local. The map $A^\sigma \to k^\sigma$ induced by $A\to k$ has kernel $\mathfrak m^\sigma$, so it is injective onto its image; for surjectivity, given $x \in k^{\sigma_k}$ with a lift $a \in A$, the element $\tfrac12(a+\sigma(a))$ is fixed and has the same image as $a$ because $\sigma(a)\equiv \sigma_k(x) = x\equiv a \pmod{\mathfrak m}$; the computation fails without $\tfrac12$.

**Remark.** The fixed subring of an involution of a local ring is again local: this is one of the few properties that pass from a ring to its fixed ring without an extra hypothesis, and it is what makes the residue field of $A^\sigma$ computable. The image of $\sigma$ on the residue field is the full $k^{\sigma_k}$ when $\sigma$ is nontrivial on $k$, and the two extreme cases are $k^{\sigma_k} = k$ for a trivial residue involution and $k^{\sigma_k}$ of index two in $k$ for a nontrivial one, by the quadratic-extension theorem of *Involutive Rings*.

## Lifting the Residue Involution

**Question.** Given an involution $\tau$ of the residue field $k$, when is it induced by an involution of $A$, that is, when does there exist an involution $\sigma$ of $A$ with $\sigma_k = \tau$?

**Proposition (the obstruction is not in the residue field).** Not every involution of $k$ lifts: if $A = k[[t]]$ with the coefficientwise identity and the residue field $k$ of characteristic $\neq 2$, the involution $\tau$ of $k$ lifts to an involution of $k[[t]]$ if and only if $\tau$ extends to a $k$-linear map of $k[[t]]$ of order two, and the assignment $t \mapsto -t$ lifts the identity; a nontrivial involution of the coefficients extends coefficientwise, so in this example every involution of $k$ lifts.

**Proof.** The coefficientwise extension $\sum c_n t^n \mapsto \sum \tau(c_n)t^n$ is additive, multiplicative and of order two, and induces $\tau$ on $k = k[[t]]/(t)$; the map $t \mapsto -t$ is the case $\tau = \mathrm{id}$. The two constructions show that $k[[t]]$ has an involution inducing each involution of $k$, so for this ring there is no obstruction.

**Theorem (lifting under completeness).** Let $(A, \mathfrak m)$ be a complete Noetherian local ring with residue field $k$ and $2$ invertible in $A$, and let $\tau$ be an involution of $k$. Then $\tau$ is induced by an involution of $A$ when $k$ is perfect and $A$ is the completion of a finitely generated algebra over a coefficient ring on which $\tau$ acts; in particular, over a complete discrete valuation ring with perfect residue field every involution of the residue field lifts.

**Proof (sketch).** One lifts $\tau$ step by step through the powers: an involution of $A/\mathfrak m^{n+1}$ inducing $\tau$ is an involution of a nilpotent extension of $A/\mathfrak m^n$ by the module $\mathfrak m^n/\mathfrak m^{n+1}$, and the obstruction to lifting it lies in the second cohomology of the group $\mathbb{Z}/2$ acting through $\tau$ on that module; the obstruction vanishes when $2$ is invertible and the module is a direct summand with an invertible action, and completeness passes the compatible system of involutions to an involution of $A$. The hypothesis on $k$ supplies the first step, and the hypothesis on $2$ kills the obstruction at each step.

**Remark.** The lifting problem is the local form of the descent along an involutive Galois extension of the residue field, and the obstruction is the same as the one for the descent of a form along a quadratic extension; the forms themselves, their classification and the Brauer classes they define are *Hilbert Algebras* in Part II, and the descent theory is a later category. The elementary content used here is only that an involution of the residue field need not come from an involution of the ring and that completeness removes the obstruction.

## Examples

**(a) A discrete valuation ring with the identity residue involution.** For $A = \mathbb{Z}_{(p)}$ or $\mathbb{Z}_p$ with $\sigma = \mathrm{id}$, the maximal ideal $(p)$ is fixed, the residue involution is the identity of $\mathbb{F}_p$, and $A^\sigma = A$ with residue field $\mathbb{F}_p$.

**(b) A local ring with a nontrivial residue involution.** For $p \equiv 3 \pmod 4$ the ring $A = \mathbb{Z}_p[i] = \mathbb{Z}_p[x]/(x^2+1)$ is the unramified quadratic extension of $\mathbb{Z}_p$: it is a discrete valuation ring whose maximal ideal is $(p)$ and whose residue field is $\mathbb{F}_{p^2}$. The conjugation $i \mapsto -i$ is an involution of $A$ fixing $(p)$, the residue involution is the Frobenius $x \mapsto x^p$ of $\mathbb{F}_{p^2}$ over $\mathbb{F}_p$, and the fixed subring is $\mathbb{Z}_p$; the two maximal ideals $\mathfrak m^\sigma = (p)$ and $\mathfrak m = (p)$ coincide, and the fixed and ambient residue fields are $\mathbb{F}_p$ and $\mathbb{F}_{p^2}$.

**(c) The power-series ring.** For $A = k[[t]]$ with $k$ a field of characteristic $\neq 2$, the involution $t \mapsto -t$ has fixed subring $k[[t^2]]$, with maximal ideal $(t^2)$, and residue field $k$; the involution $t \mapsto -t$ induces the identity on $k$. The coefficientwise conjugation over $k = \mathbb{C}$ has fixed subring $\mathbb{R}[[t]]$.

**(d) The dual numbers.** For $A = k[x]/(x^2)$ with $x \mapsto -x$ and $2$ invertible, the maximal ideal $(x)$ is fixed with $\mathfrak m^2 = 0$, the residue field is $k$ with the identity involution, and the fixed subring is $k[x^2] = k$, since $x^2 = 0$; so the fixed ring has the same residue field as $A$ and its maximal ideal is $0$.

**(e) A general local ring and the fixed maximal ideal.** In every case the fixed subring is local by the proposition, and the two invariants of the involution at the residue are whether $\sigma_k$ is trivial or a quadratic involution; the lifting question is settled by completeness and the invertibility of $2$, and no other elementary invariant of the local pair is used here.

## Summary

An involution of a local ring $(A,\mathfrak m)$ fixes the maximal ideal, $\sigma(\mathfrak m) = \mathfrak m$, and each of its powers, and it descends to an involution $\sigma_k$ of the residue field $k = A/\mathfrak m$; the induced map on the associated graded ring is likewise an involution. The fixed subring $A^\sigma$ is local with maximal ideal $\mathfrak m^\sigma = A^\sigma\cap\mathfrak m$, and for $2$ invertible its residue field is the fixed field $k^{\sigma_k}$ of the residue involution; the natural map is injective in general and surjective exactly when every fixed residue has a fixed lift.

Not every involution of the residue field need lift, and the lifting of a given $\tau$ is a step-by-step problem whose obstruction lies in the cohomology of the order-two action on the successive quotients of the maximal ideal; over a complete Noetherian local ring with $2$ invertible and perfect residue field the obstruction vanishes. The examples are the discrete valuation rings with the identity residue involution, the ring $\mathbb{Z}_p[i]$ whose residue involution is the Frobenius of $\mathbb{F}_{p^2}$, the power series rings whose fixed subring is $k[[t^2]]$, and the dual numbers, where the fixed ring is the field $k$ itself.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(A,\mathfrak m)$ | Local ring with unique maximal ideal |
| $k = A/\mathfrak m$ | Residue field |
| $\sigma$ | Involution of $A$; fixes $\mathfrak m$ and its powers |
| $\sigma_k$ | Residue involution of $k$ |
| $\mathfrak m^\sigma = A^\sigma\cap\mathfrak m$ | Maximal ideal of the fixed subring |
| $A^\sigma/\mathfrak m^\sigma \cong k^{\sigma_k}$ | Residue field of the fixed subring, $2$ invertible |
| $k[[t]]$, $t \mapsto -t$ | Example; fixed subring $k[[t^2]]$ |
| $\mathbb{Z}_p[i]$, $p\equiv 3 \pmod 4$ | Local ring whose residue involution is the Frobenius |

## Further Reading

- Michael Atiyah and Ian Macdonald, *Introduction to Commutative Algebra* (Addison-Wesley, 1969), for local rings, the maximal ideal, the residue field and the powers of the maximal ideal.
- Nicolas Bourbaki, *Commutative Algebra* (Springer, 1989), for the maximal ideal, completions and the lifting of structure through nilpotent extensions.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the fixed subring and the passage of the involution to a quotient.
- Jean-Pierre Serre, *Local Fields*, Graduate Texts in Mathematics 67 (Springer, 1979), for the discrete valuation rings, their residue fields and the Frobenius of a finite residue field.
