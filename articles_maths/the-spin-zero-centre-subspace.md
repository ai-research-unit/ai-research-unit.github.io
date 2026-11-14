# __Introduction to the Spin-Zero Centre Subspace__

## Introduction

One carrier of the biquaternion algebra under the rotation action has spin $0$, and its subspace is the centre. This article introduces that carrier: it states the subspace, the action on it, the two numbers that make the label $0$ unavoidable, and the place the subspace takes among the four spaces of the algebra.

The carrier is the smallest of the three and the one with no argument. The rotation does not move it. An element of the centre is a complex multiple of the identity, and every conjugation by a unitary element fixes it, so the operator of the action is the identity at every axis and the generator is zero.

**The question in one line.** A carrier is a real subspace that the group carries onto itself and that has no invariant real subspace. Which subspace of $\mathbb{B}$ is fixed by every unitary element, of real dimension $1$.

**The answer in one line.** The real line $\mathbb{R}e_t$, and its closure $\mathbb{C}e_t$ of real dimension $2$.

Nothing below is a statement of physics. The elements are written $X,Y$; the units are $e_t,\vec e_x,\vec e_y,\vec e_z$ with $e_t$ the identity and $\vec e_k^{2}=-e_t$; $*$ is the Hermitian conjugation; $G=\mathrm{U}(2)$ is the group of units, the elements with $XX^{*}=e_t$; and a unit real axis is written $\vec u_{\mathrm r}$.

## The Subspace

**Definition (the fixed line).** The carrier of this article is

$$
\mathbb{R}e_t=\{\,te_t:t\in\mathbb{R}\,\},
$$

the real line of the identity, of real dimension $1$.

The subspace is not built and not chosen. It is the set of real multiples of the identity of the algebra, and the identity is the one element the algebra supplies without a choice.

**The closure.** The smallest complex subspace containing the line is

$$
\mathbb{C}e_t=\mathbb{R}e_t\oplus\mathbb{R}(ie_t),
$$

of real dimension $2$ and complex dimension $1$. This is the centre of the algebra, and it is the space the tables name when they name the spin-zero space. The line is the carrier; the centre is its closure.

## Why Every Unitary Element Fixes It

**Proposition (the centre is the fixed space).** For every unitary element $u$ and every real $t$,

$$
u\,(te_t)\,u^{*}=t\,uu^{*}=te_t .
$$

*Proof.* The identity is central, so it commutes with every element, and $uu^{*}=e_t$ by the definition of $G$. The two facts give the display, and the line is fixed pointwise.

**Proposition (nothing else is fixed).** If $X$ satisfies $uXu^{*}=X$ for every unitary element $u$, then $X\in\mathbb{C}e_t$.

*Proof.* Take $u$ with $uu^{*}=e_t$. The condition is $uX=Xu$, so $X$ commutes with every unitary element. The unitary elements span $\mathbb{B}$ over $\mathbb{C}$, so $X$ commutes with every element, and an element of $\mathbb{B}$ that commutes with everything is a complex multiple of $e_t$. The other direction is the proposition above.

The two statements together say that the fixed space of the conjugation is exactly the centre, and that the centre is not the line but its closure. The line is the carrier; the centre is the space of fixed points, and the difference between the two is the element $ie_t$.

## The Only Invariant Complex Line

The propositions above say that the centre is a fixed space. They do not yet say that it is the only complex line the conjugation preserves, and the difference matters: a carrier is invariant as well as irreducible, so the uniqueness of the line is part of the statement that this carrier is the spin-zero carrier of the algebra.

**Theorem (no other complex line is fixed).** Let $W$ be a complex line whose elements are all fixed by the conjugation. Then $W=\mathbb{B}_C$.

*Proof.* The fixed elements are those of $\mathbb{B}_C$, by the proposition above, so $W$ is a complex line inside $\mathbb{B}_C$. The centre is itself a complex line, so $W=\mathbb{B}_C$.

**Theorem (no other complex line is invariant).** Let $W$ be a complex line with $uWu^{*}\subseteq W$ for every unitary element $u$. Then $W=\mathbb{B}_C$.

*Proof.* Let $w$ generate $W$. For a unitary element $u$ the element $uwu^{*}$ lies in $W$ and is nonzero, since $u$ is invertible, so $uwu^{*}=\chi(u)w$ for a nonzero complex number $\chi(u)$, and $\chi$ is a homomorphism of $G$ into the multiplicative group of $\mathbb{C}$. The norm is multiplicative and $N(uu^{*})=1$, so $N(uwu^{*})=N(w)$ and $\chi(u)^{2}=1$: the character takes values in $\{\pm1\}$. The group $G=\mathrm U(2)$ is connected, so $\chi$ is constant, and $\chi(e_t)=1$ gives $\chi=1$. Every element of $W$ is therefore fixed, and $W=\mathbb{B}_C$ by the previous theorem.

**Corollary (three descriptions, one line).** The real line $\mathbb{R}e_t$, the fixed space of the group, and the only invariant complex line are the same subspace read three ways. The first is the carrier, the second is its space of fixed points, and the third is its closure.

**Remark (why the character argument is not a detour).** Without the invariance of the norm the conclusion fails: a complex line can be scaled by an arbitrary nonzero scalar by a conjugation, and the scaling would be a character with values outside the unit circle. The norm is what reduces the character to a sign, and the connectedness of the group is what reduces the sign to $1$.

## The Action and the Two Numbers

**The action.** The conjugation by a unitary element, $\varrho_{\mathrm{ad}}(u)(X)=\operatorname{Ad}_u(X)=uXu^{-1}=uXu^{*}$ for $u\in G$, the second equality because $u^{*}=u^{-1}$ at a unitary element. On this space the action is trivial: $\varrho_{\mathrm{ad}}(u)$ is the identity operator for every unit $u$.

**The generator.** Write a rotor as $u=\exp\bigl(\theta_{\mathrm{axr}}A(\vec u_{\mathrm r})\bigr)$ with $A(\vec u_{\mathrm r})=\tfrac12\vec u_{\mathrm r}$. The derived operator is the commutator, and on a central element the commutator vanishes:

$$
\varrho\bigl(A(\vec u_{\mathrm r})\bigr)(te_t)=\tfrac12\bigl[\vec u_{\mathrm r},te_t\bigr]=0 .
$$

So the operator of the generator is the zero operator, at every axis, with no computation.

**The weights.** By definition a weight is a real $\lambda$ for which $i\lambda$ is an eigenvalue of that operator. The operator is zero, so the only eigenvalue is $0$, and the spectrum is

$$
\{0\},
$$

with multiplicity $1$ on the line.

**The spin.** The spin is the largest weight, so $s=0$. The identity that relates the dimension to the spin is

$$
2s+1=1=\dim_\mathbb{R}\mathbb{R}e_t ,
$$

and it holds here in the degenerate way: the spectrum has one member, the space has one dimension.

**The full turn.** A rotation through the full angle is the rotor $-e_t$. On a central element it acts as $(-e_t)X(-e_t)^{*}=e_tXe_t=X$, so the operator of a full turn is $+1$. The sign is $(-1)^{2s}=(-1)^{0}=+1$, and the two agree.

## The Centre as a Space of Multiplicity Two

**Why the closure doubles the carrier.** The centre carries the trivial carrier twice. The two lines $\mathbb{R}e_t$ and $\mathbb{R}(ie_t)$ are each fixed pointwise, and they are the real and the imaginary part of one complex line. A reader who asks for the spin-zero carrier of the algebra is answered by the line; a reader who asks for the subspace that carries it is answered by the centre, and the centre contains two copies of the line.

**The two copies are not two carriers.** The carrier is the module, and the module is one-dimensional. The multiplicity two belongs to the space and not to the carrier: the space is a complex line and the module is a real line, and the factor of two is the price of reading a real space complexly.

**The intersection with the anti-Hermitian space.** The centre meets the anti-Hermitian space in the line $\mathbb{R}(ie_t)$:

$$
\mathbb{C}e_t\cap\mathbb{B}_\Phi=\mathbb{R}(ie_t),
$$

of real dimension $1$. The imaginary unit line of the centre is the fixed direction of the anti-Hermitian space, and the two spaces are not disjoint. This is the only overlap the centre has with the other closures.

## Why the Subspace Is Not a Peirce Corner

**The test.** The centre is not one of the four Peirce corners of a basis. A corner is a set $\tilde\Pi_\epsilon\mathbb{B}\tilde\Pi_\delta$ for a pair of idempotents of one axis, of real dimension $2$, and its elements have a product that is not central.

**The reason.** A corner is a space of products, and the centre is a space of fixed points. The two are different constructions, and they coincide in no case: a corner of real dimension $2$ contains an element with a non-central product, while every element of the centre has a central product.

**What this says about the naming.** The four spaces of the algebra are reached by four different rules, and the centre is reached by the rule of the fixed points. Its dimension happens to agree with the dimension of a corner, and the agreement is a coincidence of small numbers: the algebra has eight real dimensions and the two constructions cut it in different ways.

## The Carrier in the List of Three

**The three carriers.** The algebra has three carriers under the rotation action: this line, of real dimension $1$ and spin $0$; a spinor plane, of real dimension $2$ and spin $\tfrac12$; and the vector part, of real dimension $3$ and spin $1$. The list is proved in *The Carriers, the Representation, the Spin and the Closure*, §*Three and No More* and is not reproved here.

**The arithmetic.** The three dimensions are $1,2,3$ and the three spins are $0,\tfrac12,1$, and the identity $2s+1=\dim_\mathbb{R}$ holds in all three cases. The line is the case $s=0$, and it is the only case in which the spectrum has a single member.

**The limits.** This article treats the fixed line and its closure. It does not treat the action of the general invertible elements, which is not the conjugation by a unitary element; it does not treat products of carriers; and it does not prove the trichotomy.

## Summary

The carrier of spin $0$ is the real line $\mathbb{R}e_t$, of real dimension $1$. Its closure is the centre $\mathbb{C}e_t$, of real dimension $2$. The action on it is trivial, the generator is zero, the spectrum is $\{0\}$, the spin is $0$, the identity $2s+1=\dim_\mathbb{R}$ reads $1=1$, and the operator of a full turn is $+1$. The centre is the fixed space of the conjugation, it contains two copies of the carrier, and it meets the anti-Hermitian space in the line $\mathbb{R}(ie_t)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, real, of dimension $8$ |
| $e_t$ | the identity of the algebra |
| $i$ | the complex unit, an element of $\mathbb{B}$ |
| $\mathbb{R}e_t$ | the fixed line, the carrier of spin $0$, $\dim_\mathbb{R}=1$ |
| $\mathbb{C}e_t$ | the centre, the closure, $\dim_\mathbb{R}=2$ |
| $\mathbb{R}(ie_t)$ | the fixed line of the anti-Hermitian space |
| $A(\vec u_{\mathrm r})=\tfrac12\vec u_{\mathrm r}$ | the generator along the unit real axis |
| $\theta_{\mathrm{axr}}$ | the rotation angle, twice the rotor angle |
| $\varrho$ | the representation of the action on the carrier |
| $\mathbb{B}_\Phi$ | the anti-Hermitian space, $\mathbb{R}(ie_t)\oplus\mathfrak{k}$ |
| $G=\mathrm{U}(2)$ | the group of unitary elements, $uu^{*}=e_t$ |

## Further Reading

- [The Spin-Zero Centre Subspace and N Norm Regularity](the-spin-zero-centre-subspace-and-n-norm-regularity.html), for the $N$ norm on the centre and the isotropic lines of its real part
- [The Spin-Zero Centre Subspace and Spectral Regularity](the-spin-zero-centre-subspace-and-spectral-regularity.html), for the double eigenvalue of a central element and the degenerate cone
- [The Carriers, the Representation, the Spin and the Closure](the-carriers-the-representation-the-spin-and-the-closure.html), for the three carriers, the completeness of the list, the spin table and the four closures
- [The Centre and the Zero Divisors of a Sesqualgebra](the-centre-and-the-zero-divisors-of-a-sesqualgebra.html), for the centre of a related algebra
- [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html), for the centre and the pure part among the subspaces of the algebra
