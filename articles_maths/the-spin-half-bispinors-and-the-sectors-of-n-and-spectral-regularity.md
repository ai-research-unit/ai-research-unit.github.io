# __The Spin-Half Bispinors and the Sectors of N and Spectral Regularity__

## Introduction

The spin-half carrier is the plane $\Sigma(\vec u_{\mathrm r})=\mathbb{C}\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})$, of real dimension $2$. Its two closures
are the spinor spaces $S_\pm(\vec u_{\mathrm r})=\mathbb{B}\tilde\Pi_{\mathrm{id},\pm}(\vec u_{\mathrm r})$, of real dimension $4$, and their sum, a bispinor space,
which as a set is the whole algebra.

This article places all three levels in the four sectors cut by the two predicates $N\neq0$ and $B^{2}\neq0$. The three levels answer differently,
and the difference is the content of the article. On the plane the norm vanishes everywhere, so the plane meets $\Sigma_{01}$ away from the origin
and $\Sigma_{00}$ at the origin, and nothing else. On a spinor space the same holds with one change: the elements whose scalar coordinate vanishes
form a real plane of square-zero elements, and that plane is the part of $\Sigma_{00}$ the spinor space contains. On a bispinor space all four
sectors are met, and the reason is that the bispinor space is the algebra.

The bispinor case supplies the sharpest statement of the article. Inside a bispinor space the norm is the pairing of the two spinor components,
$N(X_++X_-)=2B(X_+,X_-)$, so the first index of the sector is decided by whether the two components pair at all, and the second index is decided by
$B^{2}$ separately. The two indices therefore come from two different places, which is why the four combinations all occur.

The predicates, the sectors and the strata are defined in *Relations between the N Norm and Spectral Regularity and Degeneracy*, and the definitions
are repeated below. The spaces themselves are *Introduction to the Spin-Half Bispinors Spaces*. The two predicates taken one at a time are *The
Spin-Half Bispinors and N Norm Regularity* and *The Spin-Half Bispinors and Spectral Regularity*.

Nothing below is a statement of physics. The elements are written $X,Y$. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the
basis $e_t,\vec e_x,\vec e_y,\vec e_z$, with $e_t$ the identity, $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, with complex coefficients.
The element $i$ commutes with the units and satisfies $i^{2}=-e_t$. A general element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu=q_\mu+iq'_\mu$ complex
and $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. A unit real axis is written $\vec u_{\mathrm r}$, with $\vec u_2,\vec u_3$ an oriented orthonormal
pair completing it, and $G$ is the group of unitary elements, $G=\mathrm{U}(2)=\{u:uu^{*}=e_t\}$.

## The Two Predicates and the Four Sectors

**Definition (the norm and the square of the vector part).** For $\tilde Q=Q_te_t+\vec Q$,

$$
N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2},\qquad B^{2}(\tilde Q)=Q_x^{2}+Q_y^{2}+Q_z^{2}.
$$

**Theorem (the two conditions differ by the scalar square).** $N(\tilde Q)-B^{2}(\tilde Q)=Q_t^{2}$, and the polar form of the norm is

$$
B(X,Y)=\tfrac12\bigl(N(X+Y)-N(X)-N(Y)\bigr),
$$

symmetric and complex-bilinear.

*Proof.* The difference is the subtraction of two sums of squares. The polar form is the usual polarisation of a quadratic form.

**Definition (the two predicates).** An element is **norm-regular** when $N(\tilde Q)\neq0$ and **spectrally regular** when $B^{2}(\tilde Q)\neq0$.
The zero loci are the **null cone** $\mathcal N=\{N=0\}$ and the **spectral-degenerate cone** $\mathcal S=\{B^{2}=0\}$.

**Definition (the four sectors).** For $i,j\in\{0,1\}$ the sector $\Sigma_{ij}$ is the set of elements with $N\neq0$ if $i=1$ and $N=0$ if $i=0$,
and with $B^{2}\neq0$ if $j=1$ and $B^{2}=0$ if $j=0$.

| sector | conditions | name |
|---|---|---|
| $\Sigma_{11}$ | $N\neq0$, $B^{2}\neq0$ | doubly regular |
| $\Sigma_{10}$ | $N\neq0$, $B^{2}=0$ | norm-regular, spectrally degenerate |
| $\Sigma_{01}$ | $N=0$, $B^{2}\neq0$ | norm-degenerate, spectrally regular |
| $\Sigma_{00}$ | $N=0$, $B^{2}=0$ | doubly degenerate |

**Lemma (a vanishing predicate collapses the partition).** If $N$ vanishes on a subset $W$ then $W\subseteq\Sigma_{01}\cup\Sigma_{00}$, and $W$ meets
neither $\Sigma_{11}$ nor $\Sigma_{10}$.

*Proof.* The first index is $0$ at every point of $W$; the second index is free, which leaves the two sectors named.

The lemma settles the plane and the spinor spaces at one stroke, since both lie in $\mathcal N$.

## The Carrier: The Plane and the Sectors

**The plane and its coordinates.** The idempotent of the axis is $\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})=\tfrac12(e_t+i\vec u_{\mathrm r})$, and the plane is

$$
\Sigma(\vec u_{\mathrm r})=\mathbb{C}\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})=\{\lambda\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r}):\lambda\in\mathbb{C}\},
$$

of real dimension $2$. Its scalar coordinate is $Q_t=\lambda/2$.

**Theorem (the norm vanishes on the plane).** For every complex $\lambda$,

$$
N\bigl(\lambda\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})\bigr)=\lambda^{2}N\bigl(\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})\bigr)=0 .
$$

*Proof.* The norm is multiplicative and the idempotent has norm $\tfrac14(1-\lvert\vec u_{\mathrm r}\rvert^{2})=0$, the axis being of unit length.

**Theorem (the square of the vector part on the plane).** For every complex $\lambda$,

$$
B^{2}\bigl(\lambda\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})\bigr)=-\tfrac14\lambda^{2}=-Q_t^{2}.
$$

*Proof.* The coordinates are $Q_t=\tfrac12\lambda$ and $Q_k=\tfrac i2\lambda u_k$, so the sum of the vector squares is $-\tfrac14\lambda^{2}$ times
the squared length of the axis.

### The Sector $\Sigma_{11}$

**Theorem.** $\Sigma(\vec u_{\mathrm r})\cap\Sigma_{11}=\varnothing$.

*Proof.* The sector requires $N\neq0$ and the norm vanishes on the plane.

### The Sector $\Sigma_{10}$

**Theorem.** $\Sigma(\vec u_{\mathrm r})\cap\Sigma_{10}=\varnothing$.

*Proof.* The sector requires $N\neq0$, and the norm vanishes on the plane. The exclusion is the same one as for $\Sigma_{11}$, read on the other
index.

**Remark (the two exclusions are one).** The two regular sectors differ in the second index and agree in the first, so a subset on which the norm
vanishes misses both. The plane misses the whole of the regular part of the algebra and none of its degenerate part.

### The Sector $\Sigma_{01}$

**Theorem.** The intersection with the sector is the plane minus its origin:

$$
\Sigma(\vec u_{\mathrm r})\cap\Sigma_{01}=\{\lambda\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r}):\lambda\neq0\}.
$$

*Proof.* On the plane $N=0$, so the first index is $0$ and the sector is decided by the second. The value is $B^{2}=-\lambda^{2}/4$, which vanishes
exactly at $\lambda=0$.

**Corollary (the spectrum of an element of the plane).** For $\lambda\neq0$ the spectrum is $\{0,\lambda\}$, with distinct eigenvalues, and the
element is a zero divisor with a full eigenbasis.

**Remark (the carrier lies in one sector).** The punctured plane is contained in a single sector, and its sector is the one in which the norm fails
and the spectrum survives. The claim is not that the plane is special among the planes, since the same holds at every axis; it is that the carrier
is the cleanest inhabitant of $\Sigma_{01}$, and the sector is named for the pattern it shows.

### The Sector $\Sigma_{00}$

**Theorem.** $\Sigma(\vec u_{\mathrm r})\cap\Sigma_{00}=\{0\}$.

*Proof.* The origin is the point $\lambda=0$, where both forms vanish, and it is the only point of the plane where $B^{2}$ vanishes.

**Remark (the plane is null and its apex is the only doubly degenerate point).** The whole plane lies in the null cone, and one point of it lies in
the spectral-degenerate cone. The two cones meet the plane in a line and in a point, and the point is the origin of the line.

**The intersections in one table.**

| sector | condition on $\lambda$ | intersection | dimension over $\mathbb{R}$ |
|---|---|---|---|
| $\Sigma_{11}$ | impossible, $N=0$ | $\varnothing$ | — |
| $\Sigma_{10}$ | impossible, $N=0$ | $\varnothing$ | — |
| $\Sigma_{01}$ | $\lambda\neq0$ | $\mathbb{C}^{\times}\tilde\Pi_{\mathrm{id},+}$ | $2$ |
| $\Sigma_{00}$ | $\lambda=0$ | $\{0\}$ | $0$ |

## The First Closure: The Spinor Space and the Sectors

**The space and its coordinates.** The spinor space is $S_+(\vec u_{\mathrm r})=\mathbb{B}\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})$, of real dimension $4$,
with the complex basis $\tilde\Pi_{\mathrm{id},+}$ and $\vec u_2\tilde\Pi_{\mathrm{id},+}$. An element is

$$
Y=\alpha\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})+\beta\,\vec u_2\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r}),
$$

with $\alpha,\beta$ complex, and its scalar coordinate is $Q_t(Y)=\alpha/2$. The second spinor space $S_-(\vec u_{\mathrm r})$ is the same space at the
complementary idempotent.

**Theorem (the norm vanishes on the ideal).** For every element $Y$ of $S_+(\vec u_{\mathrm r})$,

$$
N(Y)=0,\qquad B^{2}(Y)=-Q_t(Y)^{2}.
$$

*Proof.* The space is $\mathbb{B}\tilde\Pi_{\mathrm{id},+}$, the norm is multiplicative and $N(\tilde\Pi_{\mathrm{id},+})=0$, so the norm vanishes. For the second display, the two
eigenvalues have product $N(Y)=0$ and sum $2Q_t(Y)$, so they are $0$ and $2Q_t(Y)$; the discriminant identity
$(\lambda_1-\lambda_2)^{2}=-4B^{2}$ then reads $4Q_t(Y)^{2}=-4B^{2}(Y)$, whence $B^{2}=-Q_t^{2}$.

**Corollary (one number decides the sector).** Inside a spinor space the sector of an element is decided by the single complex number $Q_t(Y)$: the
element lies in $\Sigma_{01}$ when $Q_t(Y)\neq0$ and in $\Sigma_{00}$ when $Q_t(Y)=0$.

### The Sector $\Sigma_{11}$

**Theorem.** $S_+(\vec u_{\mathrm r})\cap\Sigma_{11}=\varnothing$.

*Proof.* The norm vanishes on the ideal.

### The Sector $\Sigma_{10}$

**Theorem.** $S_+(\vec u_{\mathrm r})\cap\Sigma_{10}=\varnothing$.

*Proof.* The norm vanishes on the ideal.

**Remark (the closure repairs invariance and not nullity).** The first closure adds the transverse direction, and it adds it inside the null cone. The
plane is not invariant under the whole group and the spinor space is, so the closure repairs the invariance; it does not repair the norm, and the
ideal is as null as the plane.

### The Sector $\Sigma_{01}$

**Theorem.** The intersection is the ideal minus a real plane:

$$
S_+(\vec u_{\mathrm r})\cap\Sigma_{01}=\{Y\in S_+(\vec u_{\mathrm r}):Q_t(Y)\neq0\}.
$$

*Proof.* On the ideal $N=0$ and $B^{2}=-Q_t^{2}$, so the second index is $1$ exactly when $Q_t\neq0$.

**Corollary (what the sector adds).** The part of the ideal in $\Sigma_{01}$ is the complement of the complex line $\mathbb{C}\vec u_2\tilde\Pi_{\mathrm{id},+}$,
which is a real plane, and it is non-empty and open in the ideal.

### The Sector $\Sigma_{00}$

**Theorem (the degenerate part of the ideal is a real plane).** In the basis above,

$$
S_+(\vec u_{\mathrm r})\cap\Sigma_{00}=\mathbb{C}\bigl(\vec u_2-i\vec u_3\bigr),
$$

of real dimension $2$. The basis element $\vec u_2\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})$ equals $\tfrac12(\vec u_2-i\vec u_3)$, so its complex
multiples are the complex multiples of $\vec u_2-i\vec u_3$.

*Proof.* By the display of the previous theorem the intersection is the set $Q_t=0$, that is $\alpha=0$. And the second basis element satisfies
$\vec u_2\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})=\tfrac12(\vec u_2-i\vec u_3)$, whose scalar coordinate is zero, so the complex multiples of that
element are exactly the set.

**Theorem (the degenerate part is the square-zero part).** For an element $Y$ of the ideal,

$$
Y^{2}=0\iff Y\in\Sigma_{00}.
$$

*Proof.* On the ideal the quadratic relation $Y^{2}-2Q_t(Y)Y+N(Y)e_t=0$ reduces to $Y^{2}=2Q_t(Y)Y$. If $Q_t(Y)=0$ the square vanishes; conversely a
non-zero square-zero element forces $Q_t(Y)Y=0$, hence $Q_t(Y)=0$.

**Remark (the degenerate plane is not the carrier).** The degenerate plane is spanned by a square-zero element and the carrier is spanned by an
idempotent, so the two planes of the ideal meet only at the origin. The family of degenerate planes is indexed by the axis like the family of carriers,
and no member of one family is a member of the other.

**The intersections in one table.**

| sector | condition on $\alpha$ | intersection | dimension over $\mathbb{R}$ |
|---|---|---|---|
| $\Sigma_{11}$ | impossible, $N=0$ | $\varnothing$ | — |
| $\Sigma_{10}$ | impossible, $N=0$ | $\varnothing$ | — |
| $\Sigma_{01}$ | $\alpha\neq0$ | the ideal minus a plane | $4$ |
| $\Sigma_{00}$ | $\alpha=0$ | $\mathbb{C}(\vec u_2-i\vec u_3)$ | $2$ |

## The Second Closure: The Bispinor Space and the Sectors

**The space.** A bispinor space is the sum $\mathbb{B}=S_+(\vec u_{\mathrm r})\oplus S_-(\vec u_{\mathrm r})$, and as a set it is the whole algebra.
Since the sectors partition the algebra, a bispinor space meets all four of them. What the spinor coordinates add is a description of each
intersection, and that description is the content of this section.

**Theorem (the norm is the pairing).** Let $X=X_++X_-$ with $X_\pm\in S_\pm(\vec u_{\mathrm r})$. Then

$$
N(X)=2B(X_+,X_-).
$$

*Proof.* The norm is quadratic with polar form $B$, so $N(X_++X_-)=N(X_+)+N(X_-)+2B(X_+,X_-)$, and the two pure terms vanish because each spinor
space is null.

**Corollary (the two indices come from two places).** The first index is decided by the pairing of the two components and the second by $B^{2}$
alone. Nothing forces the two decisions to agree, and the four combinations all occur.

### The Sector $\Sigma_{11}$

**Theorem.** The intersection is the set of elements whose two components pair nontrivially and whose square of the vector part is nonzero:

$$
\mathbb{B}\cap\Sigma_{11}=\{X:N(X)\neq0,\ B^{2}(X)\neq0\}=\{X:B(X_+,X_-)\neq0,\ B^{2}(X)\neq0\}.
$$

It is open and dense in the algebra, of real dimension $8$, and its complement is the union of the two cones, of real codimension $2$.

*Proof.* The first equality is the definition of the sector and the second is the theorem above. The two cones are the zero loci of non-zero
polynomials in four complex variables, so their union is a complex hypersurface, and its complement is open, dense and of real dimension $8$.

**Witness.** The element $e_t+2\vec e_x$ has $N=1+4=5$ and $B^{2}=4$, so it lies in the sector.

### The Sector $\Sigma_{10}$

**Theorem.** The intersection is the set of elements whose components pair and whose square of the vector part vanishes:

$$
\mathbb{B}\cap\Sigma_{10}=\{X:B(X_+,X_-)\neq0,\ B^{2}(X)=0\}.
$$

It is of real dimension $6$, and it consists of invertible elements with a repeated eigenvalue.

*Proof.* The first index is $1$ and the second is $0$ by the two conditions, and $N\neq0$ is the invertibility condition. On $B^{2}=0$ the two eigenvalues
coincide, by the criterion of the spectral predicate.

**Witness.** The identity $e_t$ has $N=1$ and $B^{2}=0$, and its components are the two idempotents, which pair to $\tfrac12$. So $e_t=\tilde\Pi_{\mathrm{id},++}\tilde\Pi_{\mathrm{id},-}$
is the simplest element of the sector, and it is the element on which the first index survives and the second fails.

### The Sector $\Sigma_{01}$

**Theorem.** The intersection is the null cone with its apex removed:

$$
\mathbb{B}\cap\Sigma_{01}=\{X:N(X)=0,\ B^{2}(X)\neq0\}=\{X:B(X_+,X_-)=0,\ B^{2}(X)\neq0\}.
$$

It is of real dimension $6$ and it contains the punctured plane and the two ideals minus their degenerate planes.

*Proof.* The first index is $0$ by the vanishing of the pairing and the second is $1$ by the non-vanishing of $B^{2}$.

**Witness.** The idempotent $\tilde\Pi_{\mathrm{id},+}$ has $N=0$ and $B^{2}=-\tfrac14$, so it lies in the sector, and it is one of its two pure components.

### The Sector $\Sigma_{00}$

**Theorem.** The intersection is the nilpotent cone:

$$
\mathbb{B}\cap\Sigma_{00}=\{X:X^{2}=0\},
$$

the origin together with the nonzero pure nilpotents, of real dimension $4$.

*Proof.* The sector is $\{N=0,B^{2}=0\}$, which forces $Q_t=0$ and $\vec Q^{2}=0$, and these two conditions are equivalent to $X^{2}=0$.

**Witness.** The element $\vec u_2-i\vec u_3$ is a nonzero pure nilpotent, so its square vanishes and it lies in the sector; it is at once the
generator of the degenerate plane of the ideal and a member of the sector of the doubly degenerate elements.

**The intersections in one table.**

| sector | condition in the spinor coordinates | intersection | dimension over $\mathbb{R}$ |
|---|---|---|---|
| $\Sigma_{11}$ | $B(X_+,X_-)\neq0$, $B^{2}\neq0$ | open dense set | $8$ |
| $\Sigma_{10}$ | $B(X_+,X_-)\neq0$, $B^{2}=0$ | invertible elements with a repeated eigenvalue | $6$ |
| $\Sigma_{01}$ | $B(X_+,X_-)=0$, $B^{2}\neq0$ | null cone minus its apex | $6$ |
| $\Sigma_{00}$ | $B(X_+,X_-)=0$, $B^{2}=0$ | nilpotent cone | $4$ |

## The Pairing Decides the First Index

**The statement.** The first index of the sector is the vanishing or the non-vanishing of the pairing of the two spinor components, and the second is
the vanishing or the non-vanishing of $B^{2}$. Neither index refers to the other, and the four combinations are the four sectors.

**Why the pairing alone is not enough.** A reader might expect the norm to decide the sector, since it decides invertibility. It decides one of the
two indices only, and the other is free. The elements $\tilde\Pi_{\mathrm{id},+}$ and $\vec u_2-i\vec u_3$ have the same first index, both being null, and
different second indices, $-\tfrac14$ and $0$. The elements $e_t$ and $e_t+2\vec e_x$ have the same first index, both being invertible, and different
second indices, $0$ and $4$. Neither index is a function of the other.

**The pairing at the carrier.** On the plane the two components are $\lambda\tilde\Pi_{\mathrm{id},+}$ and $0$, so the pairing vanishes and the norm vanishes with
it. The plane is the case in which one of the two components is absent, and the bispinor read is the case in which both are present.

## The Axis Does Not Matter

**Theorem (the pattern is the same at every axis).** Let $\vec u_{\mathrm r}'$ be a second unit real axis and let $u$ be an invertible element with
$\operatorname{Ad}_u(\vec u_{\mathrm r})=\vec u_{\mathrm r}'$. Then

$$
\operatorname{Ad}_u\bigl(\tilde\Pi_{\mathrm{id},\pm}(\vec u_{\mathrm r})\bigr)=\tilde\Pi_{\mathrm{id},\pm}(\vec u_{\mathrm r}'),\qquad
\operatorname{Ad}_u\bigl(S_\pm(\vec u_{\mathrm r})\bigr)=S_\pm(\vec u_{\mathrm r}'),
$$

and $\operatorname{Ad}_u$ carries each of the four intersections of this article to the corresponding intersection at the axis $\vec u_{\mathrm r}'$.

*Proof.* The conjugation by a unitary element is an automorphism of the algebra, so it carries an idempotent to an idempotent and a left ideal to a left ideal; it
carries $\vec u_{\mathrm r}$ to $\vec u_{\mathrm r}'$, so it carries the idempotent of one axis to the idempotent of the other. Both predicates are
invariant under it, by multiplicativity of the norm and invariance of the trace, so the sectors are preserved.

**Corollary.** The number of sectors met, the dimensions of the intersections and the strata they occupy do not depend on the axis. The family of
bispinor spaces is infinite and its sectorial description is one description.

**Remark (what the invariance does not say).** The invariance is under conjugation, which is the action of the group on the algebra. It does not say
that the plane is invariant under the whole group, and it is not: the plane is invariant only under the rotations about its own axis, which is why the
first closure exists.

## The Three Levels Compared

| level | dimension over $\mathbb{R}$ | sectors met | $\Sigma_{11}$ | $\Sigma_{10}$ | $\Sigma_{01}$ | $\Sigma_{00}$ |
|---|---|---|---|---|---|---|
| plane $\Sigma$ | $2$ | two | $\varnothing$ | $\varnothing$ | $\mathbb{C}^{\times}\tilde\Pi_{\mathrm{id},+}$ | $\{0\}$ |
| spinor space $S_+$ | $4$ | two | $\varnothing$ | $\varnothing$ | $Q_t\neq0$ | $\mathbb{C}(\vec u_2-i\vec u_3)$ |
| bispinor space $\mathbb{B}$ | $8$ | four | open dense | $B^{2}=0$, pairing nonzero | null minus apex | nilpotent cone |

**Remark (the count grows with the level).** The plane meets two sectors, the spinor space meets the same two with a larger doubly degenerate part, and
the bispinor space meets all four. The growth is not a growth in dimension alone: the first closure keeps the norm vanished and only enlarges the part
of $\Sigma_{00}$, while the second closure restores the norm and with it the two regular sectors.

**Remark (the degenerate part grows first).** Between the plane and the ideal the doubly degenerate part jumps from a point to a real plane, and the
sector $\Sigma_{01}$ loses exactly that plane. The ideal is therefore the level at which the square-zero elements become a space of their own.

## Summary

The spin-half family has three levels, and this article places each in the four sectors. On the plane the norm vanishes identically and the square of
the vector part is $-Q_t^{2}$, so the punctured plane lies in $\Sigma_{01}$, the origin lies in $\Sigma_{00}$, and the two regular sectors are met
by nothing. On a spinor space the same two sectors occur, the elements with a vanishing scalar coordinate forming the real plane
$\mathbb{C}(\vec u_2-i\vec u_3)$, which is exactly the set of square-zero elements of the ideal. On a bispinor space all four sectors are met, because
the bispinor space is the algebra.

The bispinor read is what distinguishes the two indices. The norm is the pairing of the two components, $N(X)=2B(X_+,X_-)$, so the first index asks
whether the components pair and the second asks whether $B^{2}$ survives; the four combinations are the four sectors, and the sector $\Sigma_{10}$ is
the one in which an invertible element has a repeated eigenvalue whose norm survives.

Both predicates are invariant under scaling by a nonzero complex scalar and under conjugation by a unitary element, so the sector belongs to the
orbit, and a unitary element carrying one axis to another carries the four intersections of one bispinor space to those of the other. The description is therefore the same at every
axis.

## The Boxed Summary

| the point | in plain words |
| --- | --- |
| the family | Three levels: the plane, the ideal that plane generates, and the sum of the two ideals. Each level has its own answer. |
| the plane | The norm vanishes identically, and the square of the vector part vanishes at the origin alone. |
| the sectors of the plane | The punctured plane lies in the norm-degenerate spectrally regular sector, and the origin lies in the doubly degenerate sector. The two sectors that need a nonzero norm are met by nothing. |
| an ideal | The same two sectors occur, and the doubly degenerate part of an ideal is a real plane, exactly the elements whose square vanishes. |
| the sum | All four sectors occur, because the sum of the two ideals is the whole algebra. |
| why | The norm on the sum is the pairing of the two components. The first question asks whether the components pair, the second asks whether the spectral condition survives, and the two answers are independent. |
| the sector worth naming | The one where the norm is nonzero and the two eigenvalues coincide. |
| why the answer is stable | Both conditions survive scaling and conjugation, so the answer belongs to the orbit and is the same at every axis. |

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, real dimension $8$ |
| $\tilde Q=Q_te_t+\vec Q$ | a general element, with $Q_\mu$ complex |
| $N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the norm, the first predicate |
| $B^{2}(\tilde Q)=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the square of the vector part, the second predicate |
| $B(X,Y)$ | the polar form of the norm, $\tfrac12\bigl(N(X+Y)-N(X)-N(Y)\bigr)$ |
| $\mathcal N$, $\mathcal S$ | the null cone and the spectral-degenerate cone |
| $\Sigma_{ij}$ | the sector with $N\neq0$ for $i=1$ and $B^{2}\neq0$ for $j=1$ |
| $\vec u_{\mathrm r}$, $\vec u_2,\vec u_3$ | a unit real axis and an oriented orthonormal pair completing it |
| $\tilde\Pi_{\mathrm{id},\pm}(\vec u_{\mathrm r})=\tfrac12(e_t\pm i\vec u_{\mathrm r})$ | the two idempotents of the axis |
| $\Sigma(\vec u_{\mathrm r})=\mathbb{C}\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})$ | the spinor plane, the carrier, real dimension $2$ |
| $S_\pm(\vec u_{\mathrm r})=\mathbb{B}\tilde\Pi_{\mathrm{id},\pm}(\vec u_{\mathrm r})$ | the spinor spaces, real dimension $4$ |
| $\mathbb{B}=S_+\oplus S_-$ | a bispinor space, real dimension $8$ |
| $\vec u_2-i\vec u_3$ | the square-zero element spanning the degenerate plane of the ideal |
| $\alpha,\beta$ | the coordinates of an element of the ideal |

## Further Reading

- [Introduction to the Spin-Half Bispinors Spaces](the-spin-half-bispinor-spaces.html), for the plane, the two spinor spaces and the family of
bispinor spaces.
- [The Spin-Half Bispinors and N Norm Regularity](the-spin-half-bispinors-and-n-norm-regularity.html), for the nullity of the plane and
of the ideals, and the pairing of the two halves.
- [The Spin-Half Bispinors and Spectral Regularity](the-spin-half-bispinors-and-spectral-regularity.html), for the spectrum
$\{0,\lambda\}$ of the plane and the degenerate plane inside an ideal.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html),
for the two predicates, the four sectors and the strata.
- [The N-Degenerate, Spectrally Regular Sector](the-n-degenerate-spectrally-regular-sector.html), for the sector that contains the punctured plane.
- [The N-Degenerate, Spectrally Degenerate Sector](the-n-degenerate-spectrally-degenerate-sector.html), for the sector that contains the square-zero
plane of the ideal.
- [The Spin-Zero Centre Subspace and the Sectors of N and Spectral Regularity](the-spin-zero-centre-subspace-and-the-sectors-of-n-and-spectral-regularity.html),
for the same question answered on the centre.
- [The Spin-One Anti-Hermitian Subspace and the Sectors of N and Spectral Regularity](the-spin-one-anti-hermitian-subspace-and-the-sectors-of-n-and-spectral-regularity.html),
for the same question answered on the vector part and on the anti-Hermitian space.
