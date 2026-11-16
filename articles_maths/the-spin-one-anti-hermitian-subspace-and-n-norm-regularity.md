# __The Spin-One Anti-Hermitian Subspace and N Norm Regularity__

## Introduction

The spin-one carrier is the vector part $\mathfrak{k}=\mathbb{R}\{\vec e_x,\vec e_y,\vec e_z\}$, and its closure is the anti-Hermitian subspace $\mathbb{B}_{\Phi}=\mathbb{R}(ie_t)\oplus\mathfrak{k}$. This article computes the $N$ norm on the closure and on the carrier.

The answer is the third of the three possible answers, and it is the one in the middle. On the closure the norm is real and indefinite, of signature $(3,1)$, and its null locus is a genuine cone of real dimension $3$ with two nappes. On the carrier the same formula restricts to a positive definite form, so the carrier is norm-regular away from the origin and the cone touches it only at that point. The extra line $\mathbb{R}(ie_t)$ is negative definite, and the indefiniteness of the closure comes entirely from adding the two pieces together.

Two further results are worth stating at the outset. The splitting of the closure into the negative line and the positive triple is orthogonal for the polar form, so the norm of a sum is the sum of the norms of the parts. And the norm is invariant under the conjugation action of the group, so it is constant on the orbits; it is one of the two numbers that label an orbit, and it does not separate the orbits from one another.

The companion article is *The Spin-One Anti-Hermitian Subspace and Spectral Regularity*, where the second predicate is computed: the degenerate locus there is the extra line, and the carrier is regular away from the origin. The subspace itself is *Introduction to the Spin-One Anti-Hermitian Subspace*. The norm and the predicate are defined in *Relations between the N Norm and Spectral Regularity and Degeneracy*.

Nothing below is a statement of physics. The algebra $\mathbb{B}$ is real, of dimension $8$, with units $e_t,\vec e_x,\vec e_y,\vec e_z$, $e_t$ the identity and $\vec e_k^{2}=-e_t$, and with $i$ an element commuting with the units and $i^2=-e_t$. An element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu=q_\mu+iq'_\mu$ complex. The pure part is $\mathfrak{k}=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$, an element of it is written $\vec v$ with $\lvert\vec v\rvert^{2}=v_x^{2}+v_y^{2}+v_z^{2}$, and the star is the Hermitian conjugation.

## The Norm and the Predicate

**Definition (the $N$ norm).** For $\tilde Q=Q_te_t+\vec Q$ put

$$
N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2},
$$

a complex-valued quadratic form, multiplicative, vanishing exactly on the elements without an inverse. The **polar form** is

$$
B(X,Y)=\tfrac12\bigl(N(X+Y)-N(X)-N(Y)\bigr)=\sum_\mu Q_\mu(X)Q_\mu(Y).
$$

**Definition (the predicate).** An element is **norm-regular** when $N\neq0$ and **norm-degenerate** when $N=0$. The zero locus is the **null cone** $\mathcal N=\{N=0\}$.

**Definition (the closure).** The anti-Hermitian subspace is

$$
\mathbb{B}_{\Phi}=\{X:X^{*}=-X\}=\mathbb{R}(ie_t)\oplus\mathfrak{k},
$$

of real dimension $4$. An element is written $X=i\lambda+\vec v$ with real $\lambda$ and real $\vec v$.

## The Norm on the Closure

**Theorem (the formula).** For real $\lambda$ and real $\vec v$,

$$
N(i\lambda+\vec v)=\lvert\vec v\rvert^{2}-\lambda^{2}.
$$

*Proof.* The coordinates are $Q_t=i\lambda$, real imaginary part $\lambda$ and vanishing real part, and $Q_k=v_k$ real. So $Q_t^{2}=-\lambda^{2}$ and $Q_x^{2}+Q_y^{2}+Q_z^{2}=\lvert\vec v\rvert^{2}$.

**Corollary (the norm is real on the closure).** The value $N(i\lambda+\vec v)$ is a real number for every element of $\mathbb{B}_{\Phi}$, and the closure is contained in the real locus of the norm.

**Corollary (the splitting is orthogonal).** For the two summands,

$$
N(i\lambda)=-\lambda^{2},\qquad N(\vec v)=\lvert\vec v\rvert^{2},\qquad B(i\lambda,\vec v)=0 .
$$

So the norm of a sum is the sum of the norms, and the polar form couples the two summands to nothing.

**Theorem (the signature).** The form $N$ on the closure has signature $(3,1)$: it is negative definite on the line $\mathbb{R}(ie_t)$ and positive definite on the triple $\mathfrak{k}$.

*Proof.* On the line the value is $-\lambda^{2}$, which is negative for $\lambda\neq0$. On the triple the value is $\lvert\vec v\rvert^{2}$, which is positive for $\vec v\neq0$ and vanishes only at $\vec v=0$. The two summands are orthogonal and of real dimensions $1$ and $3$.

**Corollary (the carrier is norm-regular away from the origin).** On $\mathfrak{k}$ the norm is positive definite, so

$$
\mathfrak{k}\cap\mathcal N=\{0\},
$$

and every nonzero element of the carrier is norm-regular.

**Corollary (the line is norm-regular away from the origin).** On the line the norm is negative definite, so $\mathbb{R}(ie_t)\cap\mathcal N=\{0\}$.

**Remark (where the indefiniteness comes from).** Neither summand is indefinite: each is definite, one positive and one negative, and each is norm-regular away from the origin. The indefiniteness of the closure is exactly the difference of the two signs, and it is created by the addition and not by either piece.

## The Null Cone

**Definition (the cone).** On the closure the null locus is

$$
\mathcal N\cap\mathbb{B}_{\Phi}=\{i\lambda+\vec v:\lvert\vec v\rvert^{2}=\lambda^{2}\}.
$$

**Theorem (the cone is a cone of real dimension 3).** The set above is a cone with vertex at the origin. It is the union of two nappes, the nappe $\lambda=\lvert\vec v\rvert$ and the nappe $\lambda=-\lvert\vec v\rvert$, and each nappe meets each sphere $\lambda^{2}+\lvert\vec v\rvert^{2}=r^{2}$ of the closure in a sphere of dimension $2$.

*Proof.* The condition is homogeneous of degree two, so the set is a cone. For fixed $\lvert\lambda\rvert=r$ the condition is $\lvert\vec v\rvert=r$, a sphere of dimension $2$ in the triple, and the two signs of $\lambda$ give the two nappes. The cone has real dimension $1+2=3$.

**Corollary (the cone is not a subspace).** The set is closed under multiplication by a real scalar and not under addition: the sum of two null elements need not be null.

**Remark (the null lines).** Every nonzero null element spans a null line, and the null lines of the closure are parametrised by the unit sphere in the triple: to a unit vector $\vec u$ corresponds the line spanned by $ie_t+\vec u$ and its opposite. A null line is a zero divisor of the algebra, and the cone is the union of its null lines.

**Remark (the cone against the two other carriers).** The cone is a curved set of real dimension $3$ inside the four-dimensional closure. It meets the carrier at the origin, it meets the line at the origin, and it separates the closure into the region where the norm is positive and the region where it is negative.

## Invariance Under the Group

**Theorem (the norm is invariant).** For every unitary element $u$ and every $X$,

$$
N(uXu^{*})=N(X).
$$

*Proof.* The norm is multiplicative, so $N(uXu^{*})=N(u)N(X)N(u^{*})=N(X)N(u)N(u^{*})$, and $uu^{*}=e_t$ gives $N(u)N(u^{*})=N(e_t)=1$.

**Corollary (the norm is constant on the orbits).** The conjugation action of the group preserves the closure, since the conjugate of an anti-Hermitian element is anti-Hermitian, and it preserves the norm. So the norm is a function of the orbit.

**Remark (the norm does not separate the orbits).** The orbits of the conjugation on the closure are labelled by two numbers, the parameter $\lambda$ of the centre and the modulus $\lvert\vec v\rvert$ of the triple. The norm is the difference of their squares, so it is one function of the two labels and not an enumeration of them. Two orbits with the same difference and different labels are distinct and carry the same norm, so the norm does not separate the orbits.

**Corollary (the cone is a union of orbits).** The null cone is the set of orbits whose two labels have equal modulus, and each nappe is a union of orbits. The cone is therefore invariant under the group, as it must be, since it is the zero locus of an invariant.

## The Two Halves and the Sign

**Why the anti-Hermitian half and not its partner.** The other half of real dimension $4$ with the same shape is $\mathbb{B}_{\Psi}=\mathbb{R}e_t\oplus i\mathfrak{k}$, with elements $\lambda+i\vec v$. Its norm is

$$
N(\lambda+i\vec v)=\lambda^{2}-\lvert\vec v\rvert^{2},
$$

which is the negative of the norm on the closure at the corresponding coordinates. Both halves carry indefinite forms of signature $(3,1)$ and $(1,3)$, and the choice between them is not a choice of sign but a choice of which triple is real. The carrier $\mathfrak{k}$ is real and lies in $\mathbb{B}_{\Phi}$; the triple $i\mathfrak{k}$ is imaginary and lies in $\mathbb{B}_{\Psi}$, and on that half it is negative definite. So the carrier sits in the half where its own triple is the positive one.

## The Three Carriers Compared

| carrier | norm on it | null locus in it |
| --- | --- | --- |
| centre $\mathbb{C}e_t$ | $\lambda^{2}$ | $\{0\}$ |
| spinor plane $\Sigma$ | $0$ | the whole plane |
| vector part $\mathfrak{k}$ | $\lvert\vec v\rvert^{2}$ | $\{0\}$ |

**Where the carrier sits.** The carrier is norm-regular away from the origin and, as the companion article shows, spectrally regular there too, so $\mathfrak{k}$ away from the origin lies in the sector $\Sigma_{11}$, the sector of the fully regular elements. The centre lies in $\Sigma_{10}$ and the plane in $\Sigma_{01}$.

**The positive carrier.** Among the three carriers the vector part is the only one on which the norm is positive definite. The centre carries a complex square, whose real part is indefinite; the plane carries zero. The positivity of the vector part is what makes it the natural home of a length, and it is the reason the cone of the closure is a cone over a sphere rather than a pair of lines.

## Summary

On the closure the norm is $N(i\lambda+\vec v)=\lvert\vec v\rvert^{2}-\lambda^{2}$, a real form of signature $(3,1)$ that vanishes on a cone of real dimension $3$ with two nappes. The line $\mathbb{R}(ie_t)$ is negative definite and the triple $\mathfrak{k}$ is positive definite, the two are orthogonal for the polar form, and the carrier is norm-regular at every point except the origin. The norm is invariant under the conjugation action of the group and is constant on the orbits, which are labelled by the pair $(\lambda,\lvert\vec v\rvert)$; the norm is the difference of the two squares and does not separate the orbits. The carrier away from the origin lies in the sector $\Sigma_{11}$.

## The Boxed Summary

| the point | in plain words |
| --- | --- |
| the carrier | The carrier of spin one is the real three-dimensional space of pure vector elements, and its closure is the anti-Hermitian space. |
| the norm on the closure | Vector length squared minus scalar square, a real form of signature (3,1). |
| what vanishes there | A cone of real dimension three, with two nappes. |
| the split | The line along the imaginary identity is negative definite, the vector part is positive definite, and the two are perpendicular for the polar form. |
| the norm on the carrier | Vector length squared. It is positive definite, and it vanishes at the origin alone. |
| the answer | The carrier is norm-regular at every point except the origin. |
| under conjugation | The norm is unchanged, so it is constant on the orbits. The orbits are labelled by the scalar coordinate and the vector length, and the norm is the difference of their squares, so it does not separate the orbits. |
| the sector | Away from the origin the carrier lies in the doubly regular sector. |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, real, of dimension $8$ |
| $\tilde Q=Q_te_t+\vec Q$ | an element, with $Q_\mu$ complex |
| $N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the $N$ norm, complex-valued and multiplicative |
| $B(X,Y)=\tfrac12\bigl(N(X+Y)-N(X)-N(Y)\bigr)$ | the polar form of the norm |
| $\mathcal N=\{N=0\}$ | the null cone |
| $\mathbb{B}_{\Phi}=\mathbb{R}(ie_t)\oplus\mathfrak{k}$ | the anti-Hermitian subspace, the closure, $\dim_\mathbb{R}=4$ |
| $\mathfrak{k}=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ | the vector part, the carrier, $\dim_\mathbb{R}=3$ |
| $i\lambda+\vec v$ | an element of the closure, with $\lambda$ and $\vec v$ real |
| $\lvert\vec v\rvert^{2}=v_x^{2}+v_y^{2}+v_z^{2}$ | the positive definite form on the triple |
| signature $(3,1)$ | three positive directions, one negative |
| $\Sigma_{ij}$ | the sector with $N\neq0$ for $i=1$ and $B^{2}\neq0$ for $j=1$ |

## Further Reading

- [Introduction to the Spin-One Anti-Hermitian Subspace](the-spin-one-anti-hermitian-subspace.html), for the carrier, the closure and the action on it
- [The Spin-One Anti-Hermitian Subspace and Spectral Regularity](the-spin-one-anti-hermitian-subspace-and-spectral-regularity.html), for the other predicate on the same space
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the norm, its multiplicativity and its zero locus
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html), for the definitions of the two predicates and the four sectors
- [The N-Regular Sector](the-n-regular-sector.html), for the open set on which the norm does not vanish
- [The Topology of the Zero Divisor Cone](the-topology-of-the-zero-divisor-cone.html), for the cone as a union of null lines
- [From the Spin to the Carriers and the Closures](the-carriers-the-representation-the-spin-and-the-closure.html), for the three carriers taken together
