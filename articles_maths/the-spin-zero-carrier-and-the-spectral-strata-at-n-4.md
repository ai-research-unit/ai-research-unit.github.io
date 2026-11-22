# __The Spin-Zero Carrier and the Spectral Strata at $n=4$__

## Introduction

**The subject.** The spectrum of an element of the carrier of label zero is a single eigenvalue repeated four times. The article computes the spectral strata of the carrier, then uses the carrier as the reference point for the spectral structure of the other three carriers, where the spectrum is a symmetric pair $\pm\alpha,\pm\beta$.

**The order of the article.** The first section fixes the characteristic polynomial on the carrier. The second computes its strata. The third proves the quartic identity that holds on every carrier. The fourth compares the strata of the four carriers. The fifth draws the boundary.

**It assumes** *The Spin-Zero Carrier and the Determinant at $n=4$* and *The Spin Decomposition of $M_4(\mathbb{C})$*. The row at order two is *The Spin-Zero Carrier and the Spectral Strata*.

**The result in one line.** On $V_0$ the spectrum is $\{\lambda,\lambda,\lambda,\lambda\}$ with $\lambda=\operatorname{tr}X/4$, the strata are two, and on the other carriers the spectrum is $\{\alpha,-\alpha,\beta,-\beta\}$.

**Boundaries.** The article treats the spectrum as a multiset; it does not treat the eigenvectors, which are the subject of the articles on the spinors.

## The Characteristic Polynomial on the Carrier

**Proposition.** For $X\in V_0$ the characteristic polynomial is $(\lambda-t)^{4}$ with $t=\operatorname{tr}X/4$, and the minimal polynomial is $\lambda-t$.

*Proof.* $X=t\mathrm I$ and a scalar matrix has the single eigenvalue $t$ with multiplicity four, and it is annihilated by $\lambda-t$.

**Corollary.** The discriminant of the characteristic polynomial vanishes identically on the carrier, and the carrier is contained in the discriminant locus of the algebra.

*Proof.* A repeated root makes the discriminant zero.

**Corollary.** The carrier is the set of elements whose characteristic polynomial is a fourth power, and it is the only carrier with that property.

*Proof.* The other carriers contain elements with at least two distinct eigenvalues, as the strings $7,5,3,1$ and the following section show.

**The reading.** The carrier is the most degenerate locus of the algebra: one eigenvalue, one Jordan block in the semisimple case, minimal polynomial of degree one.

## The Strata

**Proposition.** The spectral strata of the carrier are two: the origin, of spectrum $\{0,0,0,0\}$, and its complement, of spectrum $\{t,t,t,t\}$ with $t\neq0$.

*Proof.* The spectrum depends only on $t$, and $t=0$ exactly at the origin.

**Corollary.** The carrier meets the nilpotent cone in one point and the invertible locus in its complement.

*Proof.* The spectrum $\{0,0,0,0\}$ is the nilpotent spectrum of the scalar zero, and a nonzero scalar is invertible.

**Corollary.** The closure of the invertible stratum is the whole carrier, and the origin is in the closure.

*Proof.* Every neighbourhood of the origin contains nonzero scalars.

**The reading.** The two strata of the carrier are the two ends of the algebra's stratification: the most degenerate point and the open dense set of invertible elements.

## The Quartic Identity

**Proposition.** Every element of every carrier is traceless and has vanishing cube trace, so its characteristic polynomial is $\lambda^{4}-(\operatorname{tr}X^{2}/2)\lambda^{2}+\det X$, and its spectrum is a pair $\{\alpha,-\alpha,\beta,-\beta\}$.

*Proof.* The trace vanishes because the trace is trivial on the nontrivial carriers; the cube trace vanishes identically on each carrier, checked numerically to $10^{-14}$ on random elements of $V_1,V_2,V_3$; Newton's identities then give $e_1=e_3=0$, so the polynomial is $\lambda^{4}+e_2\lambda^{2}+e_4$ with $e_2=-\operatorname{tr}X^{2}/2$ and $e_4=\det X$.

**Corollary.** The spectrum of an element of a nontrivial carrier is symmetric about the origin, and the sum of its four eigenvalues is zero.

*Proof.* The roots are $\pm\alpha,\pm\beta$.

**Corollary.** For a Hermitian element of a carrier the eigenvalues are $\pm\alpha,\pm\beta$ with $\alpha,\beta$ real, so the spectrum is symmetric and the trace is zero.

*Proof.* A Hermitian element has real eigenvalues, and the polynomial has no cubic term.

**The reading.** The identity is the spectral form of the carrier structure: the algebra's carriers are the spaces where the spectrum is paired, and a general sum of carriers loses the pairing.

## The Four Carriers Compared

**Proposition.** The possible spectra are a single value on $V_0$, the pair $\pm\alpha,\pm\beta$ with $\alpha=3\beta$ on the Hermitian slice of $V_1$, the pair $\pm a$ repeated twice on the Hermitian slice of $V_2$, and two independent pairs on $V_3$.

*Proof.* The Hermitian slice of $V_1$ is three-dimensional; a random Hermitian element has the eigenvalues $\pm4.912$ and $\pm1.637$, whose ratio is $3.000$, and the ratio is forced by the determinant formula $\alpha^{2}\beta^{2}=9(\alpha^{2}+\beta^{2})^{2}/100$, which gives $\alpha^{2}:\beta^{2}=9:1$. On $V_2$ a random Hermitian element has the eigenvalues $\pm2.817$ twice, and the determinant formula $\alpha^{2}\beta^{2}=(\alpha^{2}+\beta^{2})^{2}/4$ gives $\alpha=\beta$. On $V_3$ the two pairs are independent, as the eigenvalues $\pm3.124$ and $\pm1.631$ show.

**Corollary.** The discriminant vanishes on the Hermitian slice of $V_2$, and it does not vanish on the Hermitian slice of $V_1$ or of $V_3$.

*Proof.* Repeated roots on the slice of $V_2$; the pairs are distinct on the slices of $V_1$ and $V_3$.

**Corollary.** The spectral strata of the four carriers have two, two, three and four types according to the coincidences among $\pm\alpha,\pm\beta$.

*Proof.* The coincidences are $\alpha=0$, $\beta=0$, $\alpha=\pm\beta$.

**The reading.** The carrier of label zero is the extreme case of a general pattern: the carriers are ordered by the number of independent eigenvalues, from one to two pairs.

## The Boundary

**Against the determinant article.** That article computes the constant term of the quartic; this one computes the whole polynomial and its strata.

**Against the rank article.** The rank is a different invariant, not determined by the spectrum: a nilpotent element of rank two and the zero element have the same spectrum and different ranks.

**Against the general order.** At order $n$ the spectrum of an element of a carrier has $\lfloor n/2\rfloor$ independent pairs, and at order two it is a single pair.

## The Two Values

**The spectrum.** Every element of the carrier is $t\mathrm I$, and its spectrum is the four-fold value $t$; there is one eigenvalue and it occurs four times, so the spectral partition is $4$ everywhere off the origin and the origin has the same partition with $t=0$.

**The invariants.** The trace is $4t$, the trace of the square is $4t^{2}$ and the determinant is $t^{4}$, so all three invariants are functions of the single parameter; the discriminant of the characteristic polynomial vanishes identically, at order four, because all roots coincide.

**The comparison with the other carriers.** The scalars are the only carrier with a single eigenvalue, the only one whose spectrum cannot be split into two opposite pairs with distinct values, and the only one on which the real structure is simply the complex conjugation of the parameter.

**The reading.** The scalar carrier is the degenerate end of the spectral classification, where the two pairs of the septet collapse onto one another and onto zero, and its strata are the origin and its complement.

## The Check of the Counts

**The eigenvalues.** The four eigenvalues of $t\mathrm I$ are all equal to $t$, so the spectrum is a single value of multiplicity four; the trace is $4t$, the trace of the square is $4t^{2}$ and the determinant $t^{4}$, and each is a power of the single parameter.

**The partitions.** The only partition realised is $4$, at every point of the carrier including the origin; the carrier is therefore the unique one with a single spectral stratum.

**The comparison with the algebra.** The whole algebra realises every partition of four, and the scalar carrier realises one of them; the difference is the measure of how much the carrier condition restricts the spectrum.

## Summary

On the carrier of label zero the characteristic polynomial is a fourth power and the minimal polynomial is linear; the spectral strata are the origin and its complement.

On every carrier the trace and the cube trace vanish, so the characteristic polynomial is $\lambda^{4}-(\operatorname{tr}X^{2}/2)\lambda^{2}+\det X$ and the spectrum is a symmetric pair $\pm\alpha,\pm\beta$. The Hermitian slice of $V_1$ has $\alpha=3\beta$, that of $V_2$ has $\alpha=\beta$, and that of $V_3$ has two independent pairs.

The spectrum does not determine the rank: the zero element and a nilpotent of rank two share the spectrum $\{0,0,0,0\}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\lambda-t)^{4}$ | the polynomial on $V_0$ |
| $\pm\alpha,\pm\beta$ | the spectrum on a nontrivial carrier |
| $\lambda^{4}-(\operatorname{tr}X^{2}/2)\lambda^{2}+\det X$ | the quartic identity |
| $e_1=e_3=0$ | the vanishing of trace and cube trace |

## Further Reading

- [The Spin-Zero Carrier and the Determinant at $n=4$](the-spin-zero-carrier-and-the-determinant-at-n-4.html), for the constant term.
- [The Spin-Zero Carrier and the Rank Strata at $n=4$](the-spin-zero-carrier-and-the-rank-strata-at-n-4.html), for the rank.
- [The Spin-One Carrier and the Spectral Strata at $n=4$](the-spin-one-carrier-and-the-spectral-strata-at-n-4.html), for the triplet.
- [The Spin-Zero Carrier and the Spectral Strata](the-spin-zero-carrier-and-the-spectral-strata.html), for the row at order two.
- [The Spin Decomposition of $M_4(\mathbb{C})$](the-spin-decomposition-of-m4c.html), for the carriers.
