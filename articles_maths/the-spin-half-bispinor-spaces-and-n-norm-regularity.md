# __The Spin-Half Bispinors and N Norm Regularity__

## Introduction

The spin-half carrier is the plane $\Sigma(\vec u_{\mathrm r})=\mathbb{C}\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})$, and its closures are the two spinor spaces and their sum. This article computes the $N$ norm on all of them, and the answer is the extreme one.

On the plane the norm vanishes identically. Not at one point, not on a line: at every point. The plane is a null plane, and every element of it is norm-degenerate. The same holds for the whole spinor space that contains it, since the norm is multiplicative and the idempotent has norm zero. So the carrier of spin one half is the one carrier on which the predicate fails everywhere, and the failure is structural rather than accidental.

The bispinor read repairs the situation, and the repair is exact. The algebra is the direct sum of the two spinor spaces, each of them null, and the norm of a sum is twice the polar pairing of its two components. So the norm is not lost on the bispinor space: it becomes a pairing between the two halves. An element is norm-regular exactly when its two components pair nontrivially, and no element of a single spinor space is norm-regular at all.

The companion article is *The Spin-Half Bispinors and Spectral Regularity*, where the second predicate is computed and the answer is the opposite: the plane is spectrally regular away from the origin. The two predicates are independent, and this pair of articles is where the independence is sharpest. The spaces themselves are *Introduction to the Spin-Half Bispinors Spaces*. The norm and the predicate are defined in *Relations between the N Norm and Spectral Regularity and Degeneracy*.

Nothing below is a statement of physics. The algebra $\mathbb{B}$ is real, of dimension $8$, with units $e_t,\vec e_x,\vec e_y,\vec e_z$, $e_t$ the identity and $\vec e_k^{2}=-e_t$, and with $i$ an element commuting with the units and $i^2=-e_t$. An element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu=q_\mu+iq'_\mu$ complex. A unit real axis is written $\vec u_{\mathrm r}$, with $\vec u_2,\vec u_3$ an oriented orthonormal pair completing it.

## The Norm and the Predicate

**Definition (the $N$ norm).** For $\tilde Q=Q_te_t+\vec Q$ put

$$
N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}.
$$

It is a complex-valued quadratic form, it is multiplicative, and it vanishes exactly on the elements without an inverse. The polar form is

$$
B(X,Y)=\tfrac12\bigl(N(X+Y)-N(X)-N(Y)\bigr),
$$

symmetric and complex-bilinear, so that $N(X+Y)=N(X)+N(Y)+2B(X,Y)$ for all $X,Y$.

**Definition (the predicate).** An element is **norm-regular** when $N\neq0$ and **norm-degenerate** when $N=0$. The zero locus is the **null cone** $\mathcal N=\{N=0\}$.

## The Norm of the Idempotent

**Theorem.** For the idempotent $\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})=\tfrac12(e_t+i\vec u_{\mathrm r})$,

$$
N\bigl(\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})\bigr)=\tfrac14\bigl(1-\lvert\vec u_{\mathrm r}\rvert^{2}\bigr)=0 .
$$

*Proof.* The coordinates are $Q_t=\tfrac12$ and $Q_k=\tfrac i2 u_k$, so

$$
N=\tfrac14+\sum_k\Bigl(\tfrac i2u_k\Bigr)^{2}=\tfrac14-\tfrac14\sum_k u_k^{2}=\tfrac14\bigl(1-\lvert\vec u_{\mathrm r}\rvert^{2}\bigr),
$$

and the axis is of unit length.

**Remark (an idempotent of norm zero).** An idempotent satisfies $P^{2}=P$, hence $N(P)^{2}=N(P)$ by multiplicativity, so its norm is $0$ or $1$. The two idempotents of an axis are the case $0$. The consequence is that the norm cannot see an idempotent at all, and this is the first sign that the spin-half spaces are null by construction.

## The Plane Is Null

**Theorem.** For every complex $\lambda$,

$$
N\bigl(\lambda\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})\bigr)=\lambda^{2}N\bigl(\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})\bigr)=0 .
$$

**Corollary (every element of the carrier is norm-degenerate).** The intersection of the plane with the null cone is the plane:

$$
\Sigma(\vec u_{\mathrm r})\subseteq\mathcal N .
$$

So the carrier of spin one half contains no norm-regular element, and the origin is not an exception in this: the statement excludes nothing.

**Remark (the cancellation).** The norm of an element is the sum of the squares of its four coordinates, and on the plane those four squares cancel exactly. The scalar coordinate contributes $\tfrac14\lambda^{2}$ and the three vector coordinates contribute $-\tfrac14\lambda^{2}$, and the cancellation is the unit length of the axis written as an identity. On the centre there was one square and no partner to cancel it, and that is the whole difference between the two carriers.

## The Spinor Space Is Null

**Theorem.** For every element $X$ of the algebra,

$$
N\bigl(X\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})\bigr)=N(X)\,N\bigl(\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})\bigr)=0 .
$$

**Corollary.** The spinor space $S_+(\vec u_{\mathrm r})=\mathbb{B}\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})$ lies in the null cone, and so does $S_-(\vec u_{\mathrm r})$.

**Remark (the closure does not repair the nullity).** The first closure adds two real dimensions to the plane, and it adds them inside the null cone. This is worth stating because the closure does repair the invariance: the plane is not invariant under the whole group and the spinor space is. The two notions of closure are independent, and here one is repaired and the other is not.

## The Isotropic Dimension

**Definition (isotropic).** A subspace $W$ is **isotropic** for $N$ when $N$ vanishes on it, and **totally isotropic** when in addition the polar form vanishes on it in both arguments.

**Proposition.** The spinor spaces are totally isotropic: $N$ vanishes on $S_\pm$ and $B$ vanishes on $S_\pm\times S_\pm$.

*Proof.* The norm vanishes by the theorem above, and the polar form vanishes because $B(X,Y)=\tfrac12(N(X+Y)-N(X)-N(Y))$ with all three terms zero for $X,Y$ in the same spinor space.

**Theorem (the isotropic dimension is at most half).** If $W\subseteq\mathbb{B}$ is isotropic for a nondegenerate $N$, then $\dim_\mathbb{C}W\le\tfrac12\dim_\mathbb{C}\mathbb{B}=2$, that is $\dim_\mathbb{R}W\le4$.

*Proof.* For an isotropic $W$ one has $W\subseteq W^{\perp}$ for the polar form. The form is nondegenerate, so $\dim W^{\perp}=\dim\mathbb{B}-\dim W$, and the inclusion gives $\dim W\le\dim\mathbb{B}-\dim W$.

**Corollary (the spinor spaces are maximal).** Each spinor space is isotropic of real dimension $4=\tfrac12\dim_\mathbb{R}\mathbb{B}$, hence maximal. The plane is isotropic of real dimension $2$ and is not maximal; the two extra dimensions of the ideal are what the first closure adds.

**Remark (the three isotropic spaces).** The plane is totally isotropic as well, since $B(\lambda\tilde\Pi_{\mathrm{id},+},\mu\tilde\Pi_{\mathrm{id},+})=\lambda\mu N(\tilde\Pi_{\mathrm{id},+})=0$. What separates the plane from the spinor spaces is not the total isotropy but the dimension: the plane has real dimension $2$ and the spinor spaces $4$, and only the second is maximal.

## The Bispinor Read

**Theorem (the norm is the pairing).** Let $X=X_{+}+X_{-}$ with $X_{\pm}\in S_{\pm}(\vec u_{\mathrm r})$. Then

$$
N(X)=2B(X_{+},X_{-}).
$$

*Proof.* The norm is quadratic with polar form $B$, so $N(X_{+}+X_{-})=N(X_{+})+N(X_{-})+2B(X_{+},X_{-})$, and the two pure terms vanish because each spinor space is null.

**Corollary (the norm sees only the mixed part).** An element of a bispinor space is norm-regular exactly when its two components pair nontrivially:

$$
N(X)\neq0\iff B(X_{+},X_{-})\neq0 .
$$

**Theorem (the pairing is nondegenerate).** The form $B$ restricted to $S_+\times S_-$ is nondegenerate: if $X_{+}\in S_+$ satisfies $B(X_{+},Y_{-})=0$ for every $Y_{-}\in S_-$, then $X_{+}=0$.

*Proof.* For such an $X_+$ and for arbitrary $Y=Y_++Y_-$ one has $B(X_+,Y)=B(X_+,Y_-)=0$, since $B$ vanishes on $S_+\times S_+$. The form $B$ is nondegenerate on $\mathbb{B}$, so $X_+=0$.

**Remark (the two spinor spaces are dual).** The display says that the norm, restricted to a bispinor space, is the duality pairing of the two spinor spaces. In a basis of the first and a dual basis of the second the pairing is the identity, up to the factor two, and no other information enters the norm. The spinor spaces carry no norm of their own; what they carry is a pairing with each other.

## The Pairing and the Axis

**The infinity is harmless here.** The family of bispinor spaces is indexed by the axis, and the pairing moves with the axis, since both spinor spaces move. Every statement of this article holds at every axis, and the article writes the axis as a parameter for that reason.

**The pairing is symmetric.** The form $B$ is symmetric, so $B(X_+,X_-)=B(X_-,X_+)$ and the exchange of the two names does not change the value. There is no sign to track here, in contrast with the alternating forms of the exterior algebra. What the exchange does change is the order of the two components in the sum, which is nothing.

## The Three Carriers Compared

| carrier | norm on it | null locus in it |
| --- | --- | --- |
| centre $\mathbb{C}e_t$ | $\lambda^{2}$ | $\{0\}$ |
| spinor plane $\Sigma$ | $0$ | the whole plane |
| vector part $\mathfrak{k}$ | $\lvert\vec v\rvert^{2}$ | $\{0\}$ |

**Where the carrier sits.** Every nonzero element of the plane is norm-degenerate and, as the companion article shows, spectrally regular. So the plane away from the origin lies in the sector $\Sigma_{01}$, the sector of the null and spectrally regular elements. The centre lies in $\Sigma_{10}$ and the vector part in $\Sigma_{11}$. The sector $\Sigma_{00}$, in which both predicates fail, is met by no carrier except at the origin.

## Summary

The norm of the idempotent is zero, and by multiplicativity the norm vanishes on the plane, on both spinor spaces, and on every element of a single ideal. The plane is an isotropic plane of real dimension $2$, the spinor spaces are maximal isotropic subspaces of real dimension $4$, and the isotropic dimension of the algebra is at most half of $8$. On a bispinor space the norm becomes the pairing of the two spinor spaces, $N(X_++X_-)=2B(X_+,X_-)$, and it is nondegenerate. So no element of a single spinor space is norm-regular, and norm regularity inside the spin-half family is a two-sided notion.

## The Boxed Summary

| the point | in plain words |
| --- | --- |
| the carrier | The spin-half carrier is a complex line inside the algebra, and its closure is an ideal. |
| the key element | The element that generates the plane has zero norm, and the norm respects products. |
| what follows | The norm vanishes on the whole plane, on the whole ideal that plane generates, and on the other ideal as well. |
| the answer | No element of a single ideal is norm-regular. Not one. |
| the geometry | The plane is an isotropic plane of real dimension two. Each ideal is a maximal isotropic subspace of real dimension four, which is half of the algebra. |
| the whole algebra | On the whole algebra the norm is the pairing of the two halves, so it is nonzero exactly when the two halves pair. |
| the moral | Norm regularity in the spin-half family is a two-sided notion. One half on its own never supplies it. |
| against the other carriers | On the centre and on the vector part the norm separates points. On the plane and on the ideals it separates nothing. |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, real, of dimension $8$ |
| $N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the $N$ norm, complex-valued and multiplicative |
| $B(X,Y)=\tfrac12\bigl(N(X+Y)-N(X)-N(Y)\bigr)$ | the polar form of the norm |
| $\mathcal N=\{N=0\}$ | the null cone |
| norm-regular | $N\neq0$ |
| $\tilde\Pi_{\mathrm{id},\pm}(\vec u_{\mathrm r})=\tfrac12(e_t\pm i\vec u_{\mathrm r})$ | the two idempotents of the axis, a Peirce basis |
| $\Sigma(\vec u_{\mathrm r})=\mathbb{C}\tilde\Pi_{\mathrm{id},+}$ | the spinor plane, $\dim_\mathbb{R}=2$, null |
| $S_\pm(\vec u_{\mathrm r})=\mathbb{B}\tilde\Pi_{\mathrm{id},\pm}$ | the spinor spaces, $\dim_\mathbb{R}=4$, maximal isotropic |
| $S_+\oplus S_-=\mathbb{B}$ | a bispinor space, $\dim_\mathbb{R}=8$ |
| isotropic | $N$ vanishes on the subspace |
| $\Sigma_{ij}$ | the sector with $N\neq0$ for $i=1$ and $B^{2}\neq0$ for $j=1$ |

## Further Reading

- [Introduction to the Spin-Half Bispinors Spaces](the-spin-half-bispinor-spaces.html), for the plane, the two spinor spaces and the family of bispinor spaces
- [The Spin-Half Bispinors and Spectral Regularity](the-spin-half-bispinor-spaces-and-spectral-regularity.html), for the other predicate on the same spaces
- [Primitive Idempotents and Minimal Left Ideals](primitive-idempotents-and-minimal-left-ideals.html), for the idempotents as the generators of the ideals
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the norm, its multiplicativity and its zero locus
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html), for the definitions of the two predicates and the four sectors
- [The N-Degenerate, Spectrally Regular Sector](the-n-degenerate-spectrally-regular-sector.html), for the sector in which the plane away from the origin lies
- [The Minimal Left Ideals of the Biquaternion Algebra](the-minimal-left-ideals-of-the-biquaternion-algebra.html), for the idempotents and the splitting of the algebra
- [From the Spin to the Carriers and the Closures](the-carriers-the-representation-the-spin-and-the-closure.html), for the three carriers taken together
