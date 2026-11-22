# __The Spin-$\tfrac32$ Bispinors and the Spectral Strata__

## Introduction

**The subject.** A bispinor names an operator, and the spectrum of that operator refines the rank. This article computes the spectrum, proves that its characteristic polynomial is a square, describes the three strata it cuts, and shows why the stratification by spectrum is finer than the stratification by rank, and where the two agree.

**The order of the article.** *The Spectrum of a Bispinor* states and proves the square form of the characteristic polynomial. *The Three Strata* names them. *The Discriminant* computes the function that cuts them. *The Degenerate Locus* identifies the operators on the middle stratum. *Finer than the Rank* proves the comparison and locates the agreement.

**It assumes** *The Spin-$\tfrac32$ Bispinors and the Rank Strata*, *The Spectrum of a Biquaternion* and *The Spin-$\tfrac32$ Bispinors and the Minimal Left Ideals*. **The row of the elements is** where the same two numbers $a_t$ and $N(a)$ give the spectrum of the element itself, with each value once instead of twice.

**The result in one line.** The operator of a bispinor has the spectrum of the named element with each value taken twice, so its characteristic polynomial is a square and it has at most two distinct eigenvalues.

**Boundaries.** The rank is *The Spin-$\tfrac32$ Bispinors and the Rank Strata*; the classification of the operators of the whole space, where four distinct eigenvalues do occur, is *The Fierz–Kofink Identities and the Classification of Spinors*; the spectral strata of the carriers are *The Spin-One Carrier and the Spectral Strata*.

Nothing below is a statement of physics. The units are $e_t,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_k^2=-e_t$ and the products cyclic; $a=a_te_t+a_x\vec e_x+a_y\vec e_y+a_z\vec e_z$ is an element with complex coefficients; $N(a)=a_t^2+B^2(a)$ is the norm, with $B^2(a)=a_x^2+a_y^2+a_z^2$ the square of the vector part; the module of the operators is $V_{3/2}$; and $L_a$, $R_b$ are the one-sided operators.

## The Spectrum of a Bispinor

**Definition.** The **operator of a bispinor** is $T_\psi=L_{a_\psi}$, the left multiplication by the element of the algebra that the bispinor names under a fixed identification of the module with the algebra. Its **spectrum** is the spectrum of that operator on the four-dimensional algebra, counted with multiplicity.

**Proposition.** The characteristic polynomial of $T_\psi$ is

$$
\chi(t)=\bigl(t^2-2a_t\,t+N(a)\bigr)^{2},
$$

so the spectrum is $\lambda_+,\lambda_+,\lambda_-,\lambda_-$, where $\lambda_\pm=a_t\pm\sqrt{a_t^2-N(a)}$; its sum is $4a_t$ and its product is $N(a)^2$.

*Proof.* Left multiplication commutes with the right multiplication by the same element, and the two together generate, at a regular element, the full commutant of the algebra in its own endomorphisms. The element satisfies its own quadratic equation $a^2-2a_ta+N(a)=0$, which is the statement that the polynomial $t^2-2a_tt+N(a)$ annihilates $L_a$. That polynomial has degree two and the algebra has dimension four, so its square annihilates $L_a$; both are monic of degree four, hence they are equal. The sum and the product are read from the two coefficients.

**Corollary.** The four values counted with multiplicity are the two values of the element itself, each taken twice. The spectrum has at most two distinct entries, and it has two exactly when $B^2(a)\neq0$.

*Proof.* The two roots coincide exactly when the discriminant $4a_t^2-4N(a)=-4B^2(a)$ vanishes.

**The reading.** The doubling is the price of the operator row: an element has two eigenvalues, and its left multiplication has each of them twice, because the algebra is four-dimensional and the left multiplication acts on two copies of the same pattern. Four distinct values cannot occur at this row.

## The Three Strata

**Theorem.** The module is the disjoint union of three spectral strata:

$$
\Sigma_0=\{0\},\qquad \Sigma_1=\{a\neq0:\ B^2(a)=0\},\qquad \Sigma_2=\{a:\ B^2(a)\neq0\},
$$

of complex dimensions $0$, $3$ and $4$, with spectrum $(0,0,0,0)$, $(\lambda,\lambda,\lambda,\lambda)$ and $(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$ respectively.

*Proof.* The partition of the spectrum is $(4)$ on the first two strata and $(2,2)$ on the third. The locus $B^2=0$ in the four-dimensional module is a quadric cone through the origin, of dimension three, and the complement of a cone in four dimensions is open and dense. The origin is the only point where the two roots vanish together with $a$.

**Corollary.** The stratum $\Sigma_2$ is open and dense, and the two others are its complement, of dimension three.

*Proof.* A non-zero polynomial does not vanish on an open dense set, and its zero locus in a four-dimensional space is a hypersurface of dimension three.

**The reading.** The generic bispinor is regular, with two distinct values each twice. The two singular strata are the origin and the cone of elements with an isotropic vector part, and the cone is the spectral-degenerate cone of the row of the elements, seen here through the operator.

## The Discriminant

**Definition.** The **discriminant** of the operator of a bispinor is

$$
\Delta(a)=\prod_{i<j}\bigl(\lambda_i-\lambda_j\bigr)^{2},
$$

the product over the six pairs of the four values counted with multiplicity.

**Proposition.** $\Delta(a)=256\,B^2(a)^{4}$, a fourth power, and it vanishes exactly on the cone $B^2=0$.

*Proof.* The four values are $\lambda_+,\lambda_+,\lambda_-,\lambda_-$, so each of the two distinct differences $\lambda_+-\lambda_-$ and $\lambda_--\lambda_+$ occurs four times among the six pairs, and the product is $(\lambda_+-\lambda_-)^{8}$. The square of the difference is $-4B^2(a)$, by the discriminant of the quadratic, so the product is $(-4B^2)^4=256B^8$.

**Corollary.** The discriminant is a perfect fourth power of the quadratic form of the vector part, and it is even in the coefficients of the element.

*Proof.* $B^2$ is quadratic and even, and a fourth power of an even function is even.

**The reading.** The discriminant does not merely detect a coincidence: at this row it is a power of one quadratic form, so the whole spectral stratification is the stratification by the sign of that form.

## The Degenerate Locus

**Proposition.** On $\Sigma_1$ the element is $a=c\,e_t+v$ with $c\neq0$ and $v^2=B^2(v)=0$, and the operator is

$$
L_a=c\,\mathrm{id}+L_v,\qquad L_v^2=L_{v^2}=0 .
$$

It is a non-zero scalar plus a square-zero operator, and it is semisimple only when $v=0$.

*Proof.* The split of the element gives the split of the operator, and the square of the left multiplication by the vector part is the left multiplication by $v^2=-B^2(v)e_t$, which vanishes on the cone. The scalar part cannot vanish when $a\neq0$, since then $N(a)=a_t^2$ would be zero. A semisimple operator with a single eigenvalue is a scalar, so the vector part must vanish.

**Corollary.** On $\Sigma_1$ the operator has Jordan blocks of size at most two, and its spectrum is a single value of multiplicity four.

*Proof.* $L_v$ is square-zero, so its Jordan blocks have size one or two, and the scalar part shifts the eigenvalue without changing the block sizes.

**The reading.** The middle stratum is where the two languages meet: the spectrum is a single value, as for a scalar, and the operator is not a scalar. The spectrum alone does not separate the scalars from the rest of the cone.

## Finer than the Rank

**Theorem.** The spectral stratification refines the rank stratification: the three spectral strata are contained in the two rank strata, and the middle one is split between them only at the origin.

*Proof.* The rank is four on $\Sigma_1\setminus\{0\}$ and on $\Sigma_2$, and zero at the origin. The spectral stratification separates $\Sigma_1\setminus\{0\}$ from $\Sigma_2$, which the rank does not, and both from the origin, which the rank also does.

**Corollary.** The two stratifications agree exactly on the carrier of the scalars, where both reduce to the pair: the origin and the scalars.

*Proof.* On the scalar line the spectrum is a single non-zero value repeated four times and the rank is four, so the spectral stratum and the rank stratum are the same set; off the line the spectral stratification is strictly finer.

**The reading.** Fineness is a comparison of partitions, and here it reads three against two. The rank answers the question of invertibility; the spectrum answers the question of the coincidence of the two values, which is asked inside the invertible set.

## Invariance along the Orbit

**Proposition.** The spectral type is invariant under the conjugation action of the group of the copy, so each stratum is a union of orbits and the type is constant on an orbit.

*Proof.* Conjugation preserves the spectrum with multiplicity. An element of the group carries $a$ to $gag^{-1}$, whose left multiplication is a conjugate of $L_a$ by the invertible operator of conjugation, and conjugate operators have equal characteristic polynomials.

**Corollary.** The regular stratum is open and is a union of orbits labelled by the two invariants $a_t$ and $B^2$, and the cone is the union of the orbits on which $N(a)=a_t^2$.

*Proof.* The group acts transitively on the elements with given scalar part and given square of the vector part, and the cone is the locus of the equality of the two invariants.

**The reading.** The spectrum is the invariant of the orbit, and the strata are the level sets of the invariant. Nothing in the argument uses a basis, and nothing uses an array: the characteristic polynomial is a polynomial in the operator, and its discriminant is a polynomial in the element.

## Further Reading

- [The Spin-$\tfrac32$ Bispinors and the Rank Strata](the-spin-three-halves-bispinors-and-the-rank-strata.html), for the coarser invariant and the two values it takes
- [The Spectrum of a Biquaternion](the-spectrum-of-a-biquaternion.html), for the two eigenvalues of an element and their coincidences
- [The Spin-$\tfrac32$ Bispinors and the Minimal Left Ideals](the-spin-three-halves-bispinors-and-the-minimal-left-ideals.html), for the ideals that the strata cut
- [N Regularity and N Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the cone of the degenerate norm
- [The Fierz–Kofink Identities and the Classification of Spinors](the-fierz-kofink-identities-and-the-classification-of-spinors-of-the-operators.html), for the five classes of the whole operator space
