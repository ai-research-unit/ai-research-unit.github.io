# __The Spin-One Anti-Hermitian Subspace and the Sectors of N and Spectral Regularity__

## Introduction

The spin-one carrier is the vector part $\mathfrak{k}=\mathbb{R}\vec e_x\oplus\mathbb{R}\vec e_y\oplus\mathbb{R}\vec e_z$, of real dimension $3$, and
its closure is the anti-Hermitian space $\mathbb{B}_\Phi=\mathbb{R}(ie_t)\oplus\mathfrak{k}$, of real dimension $4$. This article places both in the
four sectors cut by the two predicates $N\neq0$ and $B^{2}\neq0$.

The answer has two parts, and they differ. On the carrier the two predicates are the same function, since the scalar part vanishes there and
$N-B^{2}=Q_t^{2}$. So the carrier meets exactly two sectors: the punctured triple lies in $\Sigma_{11}$ and the origin lies in $\Sigma_{00}$. On the
closure the two predicates separate again, and all four sectors occur: the line $\mathbb{R}(ie_t)$ away from the origin lies in $\Sigma_{10}$, the null
cone away from the origin lies in $\Sigma_{01}$, the rest of the closure away from the null cone lies in $\Sigma_{11}$, and the origin lies in
$\Sigma_{00}$.

The closure is therefore the one proper subspace of the algebra treated in this group of articles that meets all four sectors, and the reason is
geometric. The two predicates on the closure are two real quadratic forms on four real coordinates, $N=\lvert\vec v\rvert^{2}-\lambda^{2}$ and
$B^{2}=\lvert\vec v\rvert^{2}$, and each cuts the closure in a cone; the four sectors are the four combinations of side and side the two cones produce,
and in the orbit space of the two labels they are the four answers read off a half-plane.

The predicates, the sectors and the strata are defined in *Relations between the N Norm and Spectral Regularity and Degeneracy*, and the definitions
are repeated below. The spaces themselves are *Introduction to the Spin-One Anti-Hermitian Subspace*. The two predicates taken one at a time are *The
Spin-One Anti-Hermitian Subspace and N Norm Regularity* and *The Spin-One Anti-Hermitian Subspace and Spectral Regularity*.

Nothing below is a statement of physics. The elements are written $X,Y$. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the
basis $e_t,\vec e_x,\vec e_y,\vec e_z$, with $e_t$ the identity, $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, with complex coefficients. The
element $i$ commutes with the units and satisfies $i^{2}=-e_t$. A general element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu=q_\mu+iq'_\mu$ complex and
$\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. An element of the vector part is written $\vec v$, with
$\lvert\vec v\rvert^{2}=v_x^{2}+v_y^{2}+v_z^{2}$ its positive definite square, and the star is the Hermitian conjugation,

$$
(Q_te_t+\vec Q)^{*}=\bar Q_te_t-\bar{\vec Q},
$$

so that $e_t^{*}=e_t$, $i^{*}=-i$ and $\vec v^{*}=-\vec v$ at a real $\vec v$.

## The Two Predicates and the Four Sectors

**Definition (the norm and the square of the vector part).** For $\tilde Q=Q_te_t+\vec Q$,

$$
N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2},\qquad B^{2}(\tilde Q)=Q_x^{2}+Q_y^{2}+Q_z^{2}.
$$

**Theorem (the two conditions differ by the scalar square).** $N(\tilde Q)-B^{2}(\tilde Q)=Q_t^{2}$.

*Proof.* The three vector squares cancel in the subtraction.

**Definition (the two predicates).** An element is **norm-regular** when $N(\tilde Q)\neq0$ and **spectrally regular** when $B^{2}(\tilde Q)\neq0$. The
zero loci are the **null cone** $\mathcal N=\{N=0\}$ and the **spectral-degenerate cone** $\mathcal S=\{B^{2}=0\}$.

**Definition (the four sectors).** For $i,j\in\{0,1\}$ the sector $\Sigma_{ij}$ is the set of elements with $N\neq0$ if $i=1$ and $N=0$ if $i=0$,
and with $B^{2}\neq0$ if $j=1$ and $B^{2}=0$ if $j=0$.

| sector | conditions | name |
|---|---|---|
| $\Sigma_{11}$ | $N\neq0$, $B^{2}\neq0$ | doubly regular |
| $\Sigma_{10}$ | $N\neq0$, $B^{2}=0$ | norm-regular, spectrally degenerate |
| $\Sigma_{01}$ | $N=0$, $B^{2}\neq0$ | norm-degenerate, spectrally regular |
| $\Sigma_{00}$ | $N=0$, $B^{2}=0$ | doubly degenerate |

**Definition (the strata of $\Sigma_{10}$).** The sector $\Sigma_{10}$ splits into the **scalar stratum**
$\Sigma_{10}^{\mathrm{s}}=\{Q_te_t:Q_t\in\mathbb{C}^{\times}\}$ and the **Jordan stratum**, whose elements are $Q_t(e_t+\vec\Pi_{\mathrm{nil}})$ with
$\vec\Pi_{\mathrm{nil}}$ a nonzero pure nilpotent.

**Definition (the two spaces).** The carrier is

$$
\mathfrak{k}=\{\vec v:\vec v^{*}=-\vec v,\ \vec v\ \text{real}\}=\mathbb{R}\vec e_x\oplus\mathbb{R}\vec e_y\oplus\mathbb{R}\vec e_z,
$$

of real dimension $3$. The closure is the anti-Hermitian space

$$
\mathbb{B}_\Phi=\{X:X^{*}=-X\}=\mathbb{R}(ie_t)\oplus\mathfrak{k},
$$

of real dimension $4$. An element of the closure is written $X=i\lambda+\vec v$ with real $\lambda$ and real $\vec v$.

## The Carrier: The Vector Part and the Sectors

**Theorem (the two predicates coincide on the carrier).** For real $\vec v$,

$$
N(\vec v)=B^{2}(\vec v)=\lvert\vec v\rvert^{2}.
$$

*Proof.* The scalar coordinate vanishes, so the sum of the four squares is the sum of the three. The theorem relating the two conditions then gives
$N-B^{2}=Q_t^{2}=0$.

**Corollary (the two forms are positive definite on the carrier).** Both vanish at $\vec v=0$ and at no other point, and both are positive there.

**Lemma (one predicate decides both indices).** On the carrier the first and the second index of the sector are equal. So the carrier meets only
$\Sigma_{11}$ and $\Sigma_{00}$, and the two remaining sectors are met by no element of it.

*Proof.* The two indices are the truth values of $N\neq0$ and $B^{2}\neq0$, and the two functions coincide.

### The Sector $\Sigma_{11}$

**Theorem.** The intersection is the carrier with its origin removed:

$$
\mathfrak{k}\cap\Sigma_{11}=\{\vec v:\vec v\neq0\}.
$$

*Proof.* Both predicates hold exactly when $\lvert\vec v\rvert^{2}\neq0$, which is $\vec v\neq0$.

**Corollary (the spectrum of an element of the carrier).** For $\vec v\neq0$ the spectrum is $\{i\lvert\vec v\rvert,-i\lvert\vec v\rvert\}$, purely
imaginary and distinct, and the element is invertible with a separated spectrum.

**Remark (the carrier is the positive one).** The carrier is the only one of the three on which both predicates are positive definite forms. The
centre carries a complex square, whose real part is indefinite, and the plane carries the zero form. So the carrier is the one place where the sector
test is the test of a length.

### The Sector $\Sigma_{10}$

**Theorem.** $\mathfrak{k}\cap\Sigma_{10}=\varnothing$.

*Proof.* The sector requires $B^{2}=0$ and $\vec v=0$ is the only such point, where the first predicate fails as well.

### The Sector $\Sigma_{01}$

**Theorem.** $\mathfrak{k}\cap\Sigma_{01}=\varnothing$.

*Proof.* The sector requires $N=0$, and the norm vanishes only at the origin, where $B^{2}=0$ too.

**Remark (the two empty intersections are empty for one reason).** Since the two predicates agree on the carrier, a point cannot satisfy one of them
and fail the other; a sector defined by disagreement is empty by construction. This is the structural reason why the two extreme carriers each lose one predicate and the carrier
of spin one loses neither.

### The Sector $\Sigma_{00}$

**Theorem.** $\mathfrak{k}\cap\Sigma_{00}=\{0\}$.

*Proof.* The origin is the only point where $\lvert\vec v\rvert^{2}$ vanishes.

**The intersections in one table.**

| sector | condition on $\vec v$ | intersection | dimension over $\mathbb{R}$ |
|---|---|---|---|
| $\Sigma_{11}$ | $\vec v\neq0$ | $\mathfrak{k}\setminus\{0\}$ | $3$ |
| $\Sigma_{10}$ | impossible | $\varnothing$ | — |
| $\Sigma_{01}$ | impossible | $\varnothing$ | — |
| $\Sigma_{00}$ | $\vec v=0$ | $\{0\}$ | $0$ |

## The Closure: The Anti-Hermitian Space and the Sectors

**Theorem (the two predicates on the closure).** For real $\lambda$ and real $\vec v$,

$$
N(i\lambda+\vec v)=\lvert\vec v\rvert^{2}-\lambda^{2},\qquad B^{2}(i\lambda+\vec v)=\lvert\vec v\rvert^{2}.
$$

*Proof.* The scalar coordinate is $Q_t=i\lambda$, so $Q_t^{2}=-\lambda^{2}$, and the three vector coordinates are $v_x,v_y,v_z$ real.

**Corollary (the difference of the conditions is the scalar square).** On the closure $N-B^{2}=-\lambda^{2}$, so the two predicates differ exactly
on the line, in agreement with the general identity $N-B^{2}=Q_t^{2}$.

**Corollary (the second index reads the vector part alone).** $B^{2}$ is the positive definite form on the triple and does not see $\lambda$. So the
second predicate fails exactly on the line.

**Proposition (the spectrum on the closure).** For real $\lambda$ and real $\vec v$ the spectrum of $X=i\lambda+\vec v$ is

$$
\{i(\lambda+\lvert\vec v\rvert),\ i(\lambda-\lvert\vec v\rvert)\}.
$$

It is purely imaginary, and the two eigenvalues coincide exactly when $\vec v=0$, that is exactly when $B^{2}=0$. So the second predicate is the
condition of a separated spectrum on the closure, and $\Sigma_{10}$ is exactly the part of the closure on which the two eigenvalues coincide.

*Proof.* The characteristic polynomial is $\zeta^{2}-2Q_t\zeta+N$. At $Q_t=i\lambda$ and $N=\lvert\vec v\rvert^{2}-\lambda^{2}$ the roots are
$Q_t\pm\sqrt{Q_t^{2}-N}=i\lambda\pm\sqrt{-\lvert\vec v\rvert^{2}}=i(\lambda\pm\lvert\vec v\rvert)$, taking $i\lvert\vec v\rvert$ for the square root
of $-\lvert\vec v\rvert^{2}$. The two roots differ by $2i\lvert\vec v\rvert$, which vanishes exactly when $\vec v$ does.

### The Sector $\Sigma_{11}$

**Theorem.** The intersection is the part of the closure off the two cones:

$$
\mathbb{B}_\Phi\cap\Sigma_{11}=\{i\lambda+\vec v:\vec v\neq0,\ \lvert\vec v\rvert^{2}\neq\lambda^{2}\}.
$$

*Proof.* The two conditions $N\neq0$ and $B^{2}\neq0$ are $\lvert\vec v\rvert^{2}\neq\lambda^{2}$ and $\vec v\neq0$.

**Corollary (the sector is open in the closure).** It is the complement of the union of a cone and a line, hence open and of real dimension $4$.

**Witness.** The element $2ie_t+\vec e_x$ has $N=1-4=-3$ and $B^{2}=1$, so it lies in the sector, with $\lvert\vec v\rvert<\lvert\lambda\rvert$. The
element $\vec e_x$ has the same $B^{2}$ and $N=1$, and it lies in the sector too, with $\lambda=0$.

### The Sector $\Sigma_{10}$

**Theorem.** The intersection is the line minus its origin:

$$
\mathbb{B}_\Phi\cap\Sigma_{10}=\{i\lambda:\lambda\neq0\}=\mathbb{R}(ie_t)\setminus\{0\}.
$$

*Proof.* The sector requires $B^{2}=0$, which on the closure is $\vec v=0$, and $N\neq0$, which there is $-\lambda^{2}\neq0$.

**Corollary (the sector is met in the scalar stratum).** The elements of the intersection are the central elements $i\lambda e_t$, so

$$
\mathbb{B}_\Phi\cap\Sigma_{10}=\Sigma_{10}^{\mathrm{s}}\cap\mathbb{B}_\Phi .
$$

The closure meets $\Sigma_{10}$ in central elements and in no Jordan element, and in this it agrees with the centre.

**Remark (the line is a copy of the spin-zero carrier).** The line $\mathbb{R}(ie_t)$ is fixed pointwise by every conjugation, so it carries the
trivial module; its sector is the sector of the centre away from the origin. The two spaces are different subspaces with the same module, and the
sector is a property of the module.

### The Sector $\Sigma_{01}$

**Theorem.** The intersection is the null cone of the closure without its apex:

$$
\mathbb{B}_\Phi\cap\Sigma_{01}=\{i\lambda+\vec v:\lvert\vec v\rvert^{2}=\lambda^{2},\ \vec v\neq0\}.
$$

It is of real dimension $3$, with two nappes, and each radial slice is a sphere of dimension $2$.

*Proof.* The conditions are $N=0$ and $B^{2}\neq0$, that is $\lvert\vec v\rvert^{2}=\lambda^{2}$ and $\vec v\neq0$. The condition is homogeneous of
degree two on four real coordinates, so the set is a cone; fixing $\lvert\lambda\rvert=r$ leaves the sphere of radius $r$ in the triple, and the two
signs of $\lambda$ give the two nappes.

**Corollary (the elements are zero divisors).** Every element of the intersection is a nonzero element of the null cone, hence not invertible, and the
null cone of the closure is the union of its null lines.

**Witness.** The element $ie_t+\vec e_x$ has $N=0$ and $B^{2}=1$, so it lies in the sector, and it is not central.

### The Sector $\Sigma_{00}$

**Theorem.** $\mathbb{B}_\Phi\cap\Sigma_{00}=\{0\}$.

*Proof.* The sector requires $N=0$ and $B^{2}=0$; the second gives $\vec v=0$ and then the first gives $\lambda=0$.

**Remark (the square-zero elements of the closure are only the origin).** The algebra has a cone of nonzero square-zero elements, and the closure
contains one of them only at the origin. The reason is real and twofold. A real vector of square-zero length is the zero vector, since
$v_x^{2}+v_y^{2}+v_z^{2}$ is a sum of squares of real numbers, so $\vec v=0$; and the scalar part contributes $-\lambda^{2}$. Explicitly, for
$X=i\lambda+\vec v$,

$$
X^{2}=-(\lambda^{2}+\lvert\vec v\rvert^{2})e_t+2i\lambda\vec v,
$$

which vanishes only when $\lambda=0$ and $\vec v=0$. The nonzero nilpotents of the algebra are complex and lie outside the closure.

**The intersections in one table.**

| sector | condition on $(\lambda,\vec v)$ | intersection | dimension over $\mathbb{R}$ |
|---|---|---|---|
| $\Sigma_{11}$ | $\vec v\neq0$, $\lvert\vec v\rvert\neq\lvert\lambda\rvert$ | off both cones | $4$ |
| $\Sigma_{10}$ | $\vec v=0$, $\lambda\neq0$ | $\mathbb{R}(ie_t)\setminus\{0\}$ | $1$ |
| $\Sigma_{01}$ | $\lvert\vec v\rvert=\lvert\lambda\rvert$, $\vec v\neq0$ | null cone minus apex | $3$ |
| $\Sigma_{00}$ | $\lambda=0$, $\vec v=0$ | $\{0\}$ | $0$ |

## The Sector Reads Two Numbers

**The two numbers.** On the closure the two predicates are functions of the pair $(\lambda,\lvert\vec v\rvert)$:

$$
N=\lvert\vec v\rvert^{2}-\lambda^{2},\qquad B^{2}=\lvert\vec v\rvert^{2}.
$$

The pair is the pair of orbit invariants of the conjugation action, so the sector is a function of the orbit, as it must be, and here the function is
visible in coordinates.

**Theorem (the sector is a region of the orbit space).** Let the orbit space be the closed half-plane $\{(\lambda,r):\lambda\in\mathbb{R},r\ge0\}$, the
pair of invariants of an element. Two curves of it are the zero loci: the line $r=0$, where $B^{2}$ vanishes, and the V $r=\lvert\lambda\rvert$, where
$N$ vanishes. The V is not a line but the union of the two rays $r=\lambda$ with $\lambda\ge0$ and $r=-\lambda$ with $\lambda\le0$. The two curves
cross at the origin, and together they cut the half-plane into eight connected pieces, which collect into the four sectors:

| region of the orbit space | sector |
|---|---|
| $\lambda=0$, $r=0$ | $\Sigma_{00}$ |
| $\lambda\neq0$, $r=0$ | $\Sigma_{10}$ |
| $r=\lvert\lambda\rvert>0$ | $\Sigma_{01}$ |
| $r>0$ and $r\neq\lvert\lambda\rvert$ | $\Sigma_{11}$ |

*Proof.* Substitute the pair in the two predicates and read the two truth values. The line $r=0$ is the vanishing of $B^{2}$, and the V
$r=\lvert\lambda\rvert$ is the vanishing of $N$. The two curves cross at the origin.

**The eight pieces and the four sectors.** The eight pieces are the origin, the two rays of the line away from it, the two rays of the V away from
it, and the three open pieces, one above the V and one inside each of its arms. A sector is a pair of truth values and not a connected set, so the
eight pieces collect into four sectors: the origin is $\Sigma_{00}$, the two rays of the line are $\Sigma_{10}$, the two rays of the V are
$\Sigma_{01}$, and the three open pieces are $\Sigma_{11}$. There are eight pieces and four sectors, so a sector is not a connected set.

**Corollary (the closure is the case in which the sector is decided by two numbers).** On the centre the sector depends on one number and on the
plane on one number; here it depends on two, and the four sectors are its four combinations, drawn in a half-plane and not in four quarters of one.
This is why the closure meets all four sectors and the three carriers meet two each.

**Remark (the two cones are the two curves of the picture).** The null cone is the pair of half-lines $r=\lvert\lambda\rvert$ with $\lambda\ge0$
and with $\lambda\le0$, one for each nappe, and their union is the V. The degenerate cone is the line $r=0$. The V and the line cross at the
origin, so the sector stratification of the closure is the stratification of a half-plane by two curves that cross there, and nothing more.

## The Carrier Where the Two Conditions Coincide

**The identity.** The general identity of the article is $N-B^{2}=Q_t^{2}$. On the carrier $Q_t=0$, so the identity reads $N=B^{2}$ and the two
predicates are one predicate.

**The consequence for the sectors.** A sector defined by the disagreement of the two conditions is empty on the carrier, which is the content of the
two empty intersections above. The carrier has two cells, the punctured triple and the origin, and the two are separated by a single quadratic
equation.

**The contrast with the centre.** On the centre the identity reads $N-B^{2}=N$, since $B^{2}=0$: the two conditions differ by the whole norm and the
sector $\Sigma_{10}$ is the generic one. The centre and the carrier are the two extremes of the same identity, and the plane sits between them, with
$N=0$ and $B^{2}=-Q_t^{2}$.

**The reading.** The size of $Q_t$ measures how far the two predicates are from coinciding on a subspace. The carrier is the subspace on which $Q_t$
vanishes identically, and it is the only one of the three carriers of which that is true.

## The Closure Meets All Four

**The count.** The three closures of the three carriers are the centre $\mathbb{C}e_t$, the spinor space $S_+$, and the anti-Hermitian space
$\mathbb{B}_\Phi$; the bispinor space is the algebra itself and meets everything. Of the three proper closures, two meet two sectors each and one meets
four, and the one is the anti-Hermitian space.

| space | dimension over $\mathbb{R}$ | sectors met |
|---|---|---|
| centre $\mathbb{C}e_t$ | $2$ | $\Sigma_{10}$, $\Sigma_{00}$ |
| spinor space $S_+$ | $4$ | $\Sigma_{01}$, $\Sigma_{00}$ |
| anti-Hermitian space $\mathbb{B}_\Phi$ | $4$ | $\Sigma_{11}$, $\Sigma_{10}$, $\Sigma_{01}$, $\Sigma_{00}$ |

**Theorem (the closure is the only proper one that meets all four).** The anti-Hermitian space meets each of the four sectors, and no other proper
subspace among the closures of the three carriers does.

*Proof.* The four intersections are computed above, and each is non-empty: the origin for $\Sigma_{00}$, the punctured line for $\Sigma_{10}$, the
punctured null cone for $\Sigma_{01}$, and the open rest for $\Sigma_{11}$. The centre lies in the degenerate cone, so it misses $\Sigma_{11}$ and
$\Sigma_{01}$; the spinor space lies in the null cone, so it misses $\Sigma_{11}$ and $\Sigma_{10}$.

**Remark (why the closure and not a carrier).** On each carrier the two conditions are not independent: on the centre one of them is identically
true, on the plane the other is, and on the vector part they coincide. A pair of independent conditions is what produces four cells, and the carrier
of spin one does not supply such a pair inside its own three dimensions. The closure does, and the two conditions there are two real forms on four
real coordinates.

**Remark (the two degenerate loci meet only at the origin).** On the closure the null cone and the degenerate line are not disjoint: they meet, and
they meet at the origin alone, so the intersection of the two cones inside the closure is the apex. The four sectors are therefore separated by two
curves that cross once, which is the picture of the previous section and the reason the count is four.

## Summary

The vector part $\mathfrak{k}$ carries $N=B^{2}=\lvert\vec v\rvert^{2}$, so its two predicates are one function: the punctured triple lies in
$\Sigma_{11}$, the origin lies in $\Sigma_{00}$, and $\Sigma_{10}$ and $\Sigma_{01}$ are met by nothing. The carrier is the one space of the group on
which the two conditions coincide, and it is the only one on which both are positive definite.

The anti-Hermitian closure carries $N=\lvert\vec v\rvert^{2}-\lambda^{2}$ and $B^{2}=\lvert\vec v\rvert^{2}$, so its sector is a function of the pair
$(\lambda,\lvert\vec v\rvert)$ that labels the orbits, and the four sectors are the four combinations of the two truth values, which the line $r=0$
and the V $r=\lvert\lambda\rvert$ separate. All four are met: the origin in $\Sigma_{00}$, the line $\mathbb{R}(ie_t)$ minus the origin in $\Sigma_{10}$, the null cone
minus its apex in $\Sigma_{01}$, and the rest in $\Sigma_{11}$.

Two statements make the closure singular. It meets $\Sigma_{10}$ in central elements alone, since the intersection is the scalar stratum; and it
contains no nonzero square-zero element, because the square of $i\lambda+\vec v$ is $-(\lambda^{2}+\lvert\vec v\rvert^{2})e_t+2i\lambda\vec v$, which
vanishes only at the origin. Of the three proper closures of the three
carriers it is the only one that meets all four sectors.

## The Boxed Summary

| the point | in plain words |
| --- | --- |
| the carrier | The carrier of spin one is the real three-dimensional space of pure vector elements, and its closure is the anti-Hermitian space. |
| the coincidence | On the vector part the two conditions are one and the same function, the square of the vector length. |
| the sectors of the carrier | Away from the origin the doubly regular sector; at the origin the doubly degenerate sector; the two mixed sectors are met by nothing. |
| what is unique to it | It is the one space of the three on which the two conditions coincide, and the only one on which both are positive definite. |
| the closure | There the norm is vector length squared minus scalar square, while the spectral quantity is vector length squared alone. |
| the four sectors of the closure | The four combinations of the two answers, read in the half-plane of the two orbit labels. The curve where the norm vanishes is a V and the curve where the spectral quantity vanishes is a line, and the two cross at the origin. |
| all four are met | The origin is doubly degenerate; the imaginary line without its origin is norm-regular and spectrally degenerate; the null cone without its apex is norm-degenerate and spectrally regular; the rest is doubly regular. |
| two singular facts | It meets the norm-regular spectrally degenerate sector in central elements alone, and it contains no nonzero element whose square vanishes. A real vector of zero length is zero, and the scalar part adds a negative square, so the square of an element of the closure vanishes only at the origin. |
| against the other closures | Of the three closures it is the only one that meets all four sectors. |

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, real dimension $8$ |
| $\tilde Q=Q_te_t+\vec Q$ | a general element, with $Q_\mu$ complex |
| $N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the norm, the first predicate |
| $B^{2}(\tilde Q)=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the square of the vector part, the second predicate |
| $N-B^{2}=Q_t^{2}$ | the difference of the two conditions |
| $\mathcal N$, $\mathcal S$ | the null cone and the spectral-degenerate cone |
| $\Sigma_{ij}$ | the sector with $N\neq0$ for $i=1$ and $B^{2}\neq0$ for $j=1$ |
| $\Sigma_{10}^{\mathrm{s}}$ | the scalar stratum of $\Sigma_{10}$ |
| $\mathfrak{k}=\mathbb{R}\vec e_x\oplus\mathbb{R}\vec e_y\oplus\mathbb{R}\vec e_z$ | the vector part, the carrier, real dimension $3$ |
| $\mathbb{B}_\Phi=\mathbb{R}(ie_t)\oplus\mathfrak{k}$ | the anti-Hermitian space, the closure, real dimension $4$ |
| $i\lambda+\vec v$ | an element of the closure, with $\lambda$ and $\vec v$ real |
| $\lvert\vec v\rvert^{2}=v_x^{2}+v_y^{2}+v_z^{2}$ | the positive definite form on the triple |
| $(\lambda,\lvert\vec v\rvert)$ | the pair of orbit invariants of the closure |

## Further Reading

- [Introduction to the Spin-One Anti-Hermitian Subspace](the-spin-one-anti-hermitian-subspace.html), for the carrier, the closure and the action on
it.
- [The Spin-One Anti-Hermitian Subspace and N Norm Regularity](the-spin-one-anti-hermitian-subspace-and-n-norm-regularity.html), for the norm alone,
the inertia $(3,1)$ and the null cone.
- [The Spin-One Anti-Hermitian Subspace and Spectral Regularity](the-spin-one-anti-hermitian-subspace-and-spectral-regularity.html), for the second
predicate alone, the purely imaginary spectrum and the degenerate line.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html),
for the two predicates, the four sectors and the strata.
- [The N-Regular, Spectrally Regular Sector](the-n-regular-spectrally-regular-sector.html), for the sector that contains the carrier.
- [The N-Degenerate, Spectrally Regular Sector](the-n-degenerate-spectrally-regular-sector.html), for the sector that contains the null cone of the
closure.
- [The N-Regular, Spectrally Degenerate Sector](the-n-regular-spectrally-degenerate-sector.html), for the sector that contains the line
$\mathbb{R}(ie_t)$.
- [The Spin-Zero Centre Subspace and the Sectors of N and Spectral Regularity](the-spin-zero-centre-subspace-and-the-sectors-of-n-and-spectral-regularity.html),
for the same question answered on the centre.
- [The Spin-Half Bispinors and the Sectors of N and Spectral Regularity](the-spin-half-bispinors-and-the-sectors-of-n-and-spectral-regularity.html),
for the same question answered on the plane, the spinor spaces and the bispinor space.
