# __Introduction to the Spin-One Anti-Hermitian Subspace__

## Introduction

The carrier of spin $1$ is the vector part of the algebra, of real dimension $3$, and its closure is the anti-Hermitian half, of real dimension $4$. This article introduces both: the triple, the action on it, the three weights, and the reason the closure is the anti-Hermitian half and not the Hermitian one.

The case is the opposite of the spin-zero case in one respect and the opposite of the spin-half case in another. The subspace is three-dimensional, so the spectrum has three members instead of one; the action is two-sided, so the eigenvalues are integers instead of halves; and the closure is unique, since it does not depend on an axis. Nothing here is a family.

**The question in one line.** Which real subspace of $\mathbb{B}$ of dimension $3$ is carried onto itself by every unitary element, and which space of dimension $4$ contains it.

**The answer in one line.** The vector part $\mathfrak{k}=\mathbb{R}\vec e_x\oplus\mathbb{R}\vec e_y\oplus\mathbb{R}\vec e_z$, and the anti-Hermitian space $\mathbb{B}_\Phi=\mathbb{R}(ie_t)\oplus\mathfrak{k}$.

Nothing below is a statement of physics. The elements are written $X,Y$; the units are $e_t,\vec e_x,\vec e_y,\vec e_z$ with $e_t$ the identity and $\vec e_k^{2}=-e_t$; $*$ is the Hermitian conjugation; $G=\mathrm{U}(2)$ is the group of invertibles; and $\vec u_{\mathrm r}$ is a unit real axis, with $\vec u_2,\vec u_3$ an oriented orthonormal pair completing it.

## The Subspace

**Definition (the vector part).** The carrier of this article is

$$
\mathfrak{k}=\mathbb{R}\vec e_x\oplus\mathbb{R}\vec e_y\oplus\mathbb{R}\vec e_z
=\{\,\vec v:\vec v^{*}=-\vec v,\ \vec v\ \text{real}\,\},
$$

the real span of the three pure units, of real dimension $3$.

The three units anticommute in pairs and each squares to $-e_t$, so the span is closed under the commutator and under no other product: the product of two pure units is a pure unit, but the product of two elements of $\mathfrak{k}$ need not lie in $\mathfrak{k}$.

**The action.** The conjugation by a unitary element, $\varrho_{\mathrm{ad}}(u)(X)=\operatorname{Ad}_u(X)=uXu^{-1}=uXu^{*}$ for $u\in G$, the second equality because $u^{*}=u^{-1}$ at a unitary element. On the vector part the action is the rotation: for a rotor $\tilde u_{\mathrm r}$ of angle $\theta$ about an axis, $\operatorname{Ad}_{\tilde u_{\mathrm r}}$ turns $\mathfrak{k}$ through the angle $\theta$ about that axis. The map $G\to SO(\mathfrak{k})$ is onto with kernel $\{\pm e_t\}$, and the vector part is the space on which the rotation acts in the way the name suggests.

**The closure.** The anti-Hermitian space is

$$
\mathbb{B}_\Phi=\{\,X:X^{*}=-X\,\}=\mathbb{R}(ie_t)\oplus\mathfrak{k},
$$

of real dimension $4$: the vector part together with the real line of $ie_t$.

## The Star and the Two Halves

**The star is an involution.** The Hermitian conjugation satisfies $X^{**}=X$ for every element, so the algebra splits into the eigenspaces of $+1$ and $-1$:

$$
\mathbb{B}=\mathbb{B}_\Psi\oplus\mathbb{B}_\Phi,
\qquad
\mathbb{B}_\Psi=\{\,X:X^{*}=X\,\},
\qquad
\mathbb{B}_\Phi=\{\,X:X^{*}=-X\,\}.
$$

Both eigenspaces have real dimension $4$, and the display is a direct sum in the category of real vector spaces.

**The two halves explicitly.** With $X=q+ip$ for real quaternions $q$ and $p$, the star is $X^{*}=\bar q-i\bar p$, and the two halves are

$$
\mathbb{B}_\Psi=\mathbb{R}e_t\oplus i\mathfrak{k},
\qquad
\mathbb{B}_\Phi=\mathbb{R}(ie_t)\oplus\mathfrak{k}.
$$

Each is a real line plus a real triple, and the two triples are $\mathfrak{k}$ and $i\mathfrak{k}$. The real line of the first is $e_t$; the real line of the second is $ie_t$.

**Why the carrier forces the choice.** The vector part is $\mathfrak{k}$, and $\mathfrak{k}$ lies in $\mathbb{B}_\Phi$ and meets $\mathbb{B}_\Psi$ only at the origin:

$$
\mathfrak{k}\subseteq\mathbb{B}_\Phi,
\qquad
\mathfrak{k}\cap\mathbb{B}_\Psi=\{0\}.
$$

So the half that contains the carrier is the anti-Hermitian one, and there is no choice to make. This is the reason the tables name $\mathbb{B}_\Phi$ and not $\mathbb{B}_\Psi$.

**The second reason.** The anti-Hermitian half is closed under the commutator and the Hermitian half is not:

$$
[\mathbb{B}_\Phi,\mathbb{B}_\Phi]\subseteq\mathbb{B}_\Phi,
\qquad
[\mathbb{B}_\Psi,\mathbb{B}_\Psi]\subseteq\mathbb{B}_\Phi .
$$

The bracket of two anti-Hermitian elements is anti-Hermitian, and the bracket of two Hermitian elements is anti-Hermitian as well. The first half is therefore a Lie algebra under the bracket and the second is not, and a space that is to be read with the bracket has to be the first.

## The Lie Algebra Inside the Space

**The split.** Read with the commutator, the anti-Hermitian space is the Lie algebra of the group that acts, and the display is a split of Lie algebras:

$$
\mathbb{B}_\Phi=\mathfrak{u}(2)=\mathfrak{u}(1)\oplus\mathfrak{su}(2),
$$

with $\mathfrak{k}=\mathfrak{su}(2)$ the second summand and $\mathbb{R}(ie_t)$ a one-dimensional abelian ideal.

**The dimensions.** The right-hand side has dimensions $1+3=4$, which is the dimension of the left-hand side. The triple is the summand on which the bracket does not vanish, and the line is the abelian one.

**What the split says about the carrier.** The carrier is the non-abelian summand. The line is not a second carrier: the action fixes it pointwise, so it carries the trivial carrier, and that carrier is the same one as the spin-zero line of the centre. The vector part is the only carrier inside the space.

## The Action and the Three Numbers

**The generator.** The rotor is $\tilde u_{\mathrm r}=\exp\bigl(\theta A(\vec u_{\mathrm r})\bigr)$ with $A(\vec u_{\mathrm r})=\tfrac12\vec u_{\mathrm r}$, and the derived operator on the vector part is the commutator:

$$
\varrho\bigl(A(\vec u_{\mathrm r})\bigr)(\vec v)=\bigl[\tfrac12\vec u_{\mathrm r},\vec v\bigr].
$$

**The identity that removes the computation.** The quaternion product rule is $\vec u\vec v=-\vec u\cdot\vec v+\vec u\times\vec v$, and the dot product is symmetric while the cross product is antisymmetric, so the difference of the two orders is twice the cross product:

$$
\bigl[\tfrac12\vec u_{\mathrm r},\vec v\bigr]=\vec u_{\mathrm r}\times\vec v .
$$

The operator is the cross product with the whole axis, and the factor one half in the generator is cancelled by the factor two in the commutator. This is the whole of the computation, and it holds at every axis.

**The eigenvalues.** The cross product with a unit vector annihilates the axis and turns the plane perpendicular to it by a quarter turn. With $\vec u_2,\vec u_3$ an oriented pair completing the axis, the three eigenvectors are

$$
\vec u_{\mathrm r}\ \text{with eigenvalue}\ 0,
\qquad
\vec u_2+i\vec u_3\ \text{with eigenvalue}\ -i,
\qquad
\vec u_2-i\vec u_3\ \text{with eigenvalue}\ +i,
$$

so the spectrum is

$$
\{+1,-1,0\},
$$

and the spin is the largest weight, $s=1$. The identity reads $2s+1=3=\dim_\mathbb{R}\mathfrak{k}$.

**The symmetry of the spectrum.** The operator is real, so its eigenvalues come in conjugate pairs or are real; here they are $0$ and the pair $\pm i$. The spectrum is symmetric about zero, and the weight $0$ occurs once.

**The full turn.** The cross product is a quarter turn of the perpendicular plane, and four quarter turns are a full turn, so the operator of a full turn is the identity:

$$
\exp\bigl(2\pi\,C(\vec u_{\mathrm r})\bigr)=\mathrm{id},\qquad C(\vec u_{\mathrm r})(\vec v)=\vec u_{\mathrm r}\times\vec v .
$$

The sign is $(-1)^{2s}=(-1)^{2}=+1$, and the two agree. The case of the vector part is the case in which the action of the rotors descends to the rotation group: the kernel $\{\pm e_t\}$ acts trivially.

## Why the Two Spectra Differ by a Factor of Two

**The two operators.** The same generator $A(\vec u_{\mathrm r})=\tfrac12\vec u_{\mathrm r}$ acts on the vector part by the commutator and on the plane by a single multiplication. The two spectra are $\{\pm1,0\}$ and $\{\pm\tfrac12\}$, and the ratio is two.

**The reason.** The commutator consumes the axis twice, once on each side of the product, and the single multiplication consumes it once. In the identity above the two consumptions appear as the cancellation of the one half: the commutator with one half of the axis equals the cross product with the whole axis.

**The consequence.** The vector part is the carrier of integer weights and the plane the carrier of half-integer weights, and the difference is a property of the actions and not of the spaces. The two spaces are different, and the two actions are different in kind, one two-sided and one one-sided.

## The Space Among the Four

**The dimensions.** The four spaces of the algebra are the centre, of real dimension $2$; a spinor space, of real dimension $4$; a bispinor space, of real dimension $8$; and this space, of real dimension $4$.

**The overlaps.** The anti-Hermitian space meets the centre in the line $\mathbb{R}(ie_t)$ and meets the vector part in the whole triple; it meets $\mathbb{B}_\Psi$ only at the origin, since the two halves are the eigenspaces of the star with distinct eigenvalues. The anti-Hermitian space is the only closure that is a Lie algebra under the bracket.

**What it is not.** The space is not a complex subspace: multiplication by $i$ carries it to the other half, $\mathbb{B}_\Psi$. A reader who expects a complex space of dimension $2$ will not find one here, and the reason is that the star is conjugate-linear in $i$: it fixes $ie_t$ and reverses $i\mathfrak{k}$.

**The limits.** This article treats the vector part and its closure. It does not treat the commutator as a structure beyond the split displayed, it does not treat the exponential map of the group, and it does not treat the action of the general invertible elements, which does not preserve the pure part.

## Summary

The spin-one carrier is the vector part $\mathfrak{k}$, of real dimension $3$. Its closure is the anti-Hermitian space $\mathbb{B}_\Phi=\mathbb{R}(ie_t)\oplus\mathfrak{k}$, of real dimension $4$. The action is the conjugation by a unitary element, the generator $\tfrac12\vec u_{\mathrm r}$ acts by the cross product with the whole axis, the spectrum is $\{+1,-1,0\}$, the spin is $1$, the identity reads $2s+1=3=3$, and a full turn acts as $+1$. The space is $\mathfrak{u}(2)=\mathfrak{u}(1)\oplus\mathfrak{su}(2)$, it is a Lie algebra under the bracket, and it is the half that contains the carrier.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, real, of dimension $8$ |
| $\mathfrak{k}$ | the vector part, $\mathbb{R}\vec e_x\oplus\mathbb{R}\vec e_y\oplus\mathbb{R}\vec e_z$, $\dim_\mathbb{R}=3$ |
| $\mathfrak{p}=i\mathfrak{k}$ | the imaginary triple, the other three-dimensional summand |
| $\mathbb{B}_\Phi$ | the anti-Hermitian space, $\mathbb{R}(ie_t)\oplus\mathfrak{k}$, $\dim_\mathbb{R}=4$ |
| $\mathbb{B}_\Psi$ | the Hermitian space, $\mathbb{R}e_t\oplus i\mathfrak{k}$, $\dim_\mathbb{R}=4$ |
| $\vec u_{\mathrm r}$ | a unit real axis, the axis of the rotation |
| $\vec u_2,\vec u_3$ | an oriented orthonormal pair completing the axis |
| $A(\vec u_{\mathrm r})=\tfrac12\vec u_{\mathrm r}$ | the generator along the axis |
| $\times$ | the cross product of $\mathfrak{k}$ |
| $[\cdot,\cdot]$ | the commutator, the bracket of the algebra |
| $\operatorname{Ad}_u(X)=uXu^{-1}=uXu^{*}$ | the inner automorphism, on $G$ the conjugation by a unitary element |
| $G=\mathrm{U}(2)$ | the group of unitary elements, $uu^{*}=e_t$ |

## Further Reading

- [The Spin-One Anti-Hermitian Subspace and N Norm Regularity](the-spin-one-anti-hermitian-subspace-and-n-norm-regularity.html), for the indefinite form of signature $(3,1)$ and its null cone
- [The Spin-One Anti-Hermitian Subspace and Spectral Regularity](the-spin-one-anti-hermitian-subspace-and-spectral-regularity.html), for the purely imaginary spectrum and the degenerate line of the closure
- [From the Spin to the Carriers and the Closures](the-carriers-the-representation-the-spin-and-the-closure.html), for the three carriers, the spin table and the four closures
- [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html), for the two Hermitian halves and the pure part
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), for the rotor, the two-to-one cover and the action on the vector part
