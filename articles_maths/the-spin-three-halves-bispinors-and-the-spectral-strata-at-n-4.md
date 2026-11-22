# __The Spin-$\tfrac32$ Bispinors and the Spectral Strata at $n=4$__

## Introduction

**The subject.** The spectrum of a bispinor is the spectrum of the corresponding matrix. The article computes the spectra of the pure bispinors, of the traceless ones and of the general ones, and stratifies the bispinor space by the multiplicity pattern of the eigenvalues.

**The order of the article.** The first section fixes the spectrum of a pure bispinor. The second treats the traceless bispinors and the symmetric spectra. The third stratifies by multiplicity. The fourth relates the strata to the carriers and to the ideals. The fifth draws the boundary.

**It assumes** *The Fierz–Kofink Identities and the Classification of Spinors at $n=4$* and *The Spin-$\tfrac32$ Bispinors and the Rank Strata at $n=4$*. The row at order two is *The Spin-$\tfrac12$ Bispinors and the Spectral Strata*.

**The result in one line.** A pure bispinor has the spectrum $\{\omega(\bar\chi,\psi),0,0,0\}$, a traceless bispinor the spectrum $\{\pm\alpha,\pm\beta\}$, and a general bispinor an arbitrary spectrum of four values.

**Boundaries.** The article treats the spectrum as a multiset; the eigenvectors and the Jordan structure beyond the spectrum are treated in the rank articles.

## The Pure Bispinors

**Proposition.** If $X=\psi\bar\chi^{\dagger}$ is a rank-one bispinor then $X^{2}=\omega(\bar\chi,\psi)X$, so the spectrum is $\{\omega(\bar\chi,\psi),0,0,0\}$ and the minimal polynomial divides $\lambda(\lambda-\omega)$.

*Proof.* $XX=\psi(\bar\chi^{\dagger}\psi)\bar\chi^{\dagger}=\omega(\bar\chi,\psi)X$ by the Fierz identity; a rank-one matrix has a one-dimensional image and a three-dimensional kernel, so three eigenvalues are zero and the fourth is the trace.

**Corollary.** The pure bispinor is a projection up to a scalar exactly when $\omega(\bar\chi,\psi)\neq0$, and it is nilpotent exactly when $\omega(\bar\chi,\psi)=0$.

*Proof.* $X^{2}=cX$ with $c=\omega(\bar\chi,\psi)$; if $c=0$ the matrix is nilpotent of index two.

**Corollary.** The trace of a pure bispinor is the pairing of its two factors, and the determinant vanishes.

*Proof.* The trace of $X$ is $\sum_i\psi_i\bar\chi_i=\omega(\bar\chi,\psi)$; the rank is one, so the determinant is zero.

**The reading.** The pure spectrum has one nonzero eigenvalue and a triple zero, and the nonzero eigenvalue is the pairing of the spinors.

## The Traceless Bispinors

**Proposition.** A bispinor in a nontrivial carrier has zero trace and zero cube trace, so its spectrum is $\{\alpha,-\alpha,\beta,-\beta\}$ and its characteristic polynomial is $\lambda^{4}-(\operatorname{tr}X^{2}/2)\lambda^{2}+\det X$.

*Proof.* The carriers are the nontrivial isotypic pieces, on which the trace form is trivial and the cube trace vanishes identically; Newton's identities give the polynomial.

**Corollary.** A traceless bispinor is nilpotent exactly when its spectrum is $\{0,0,0,0\}$, and then all four eigenvalues are zero.

*Proof.* The spectrum is symmetric, so all eigenvalues vanish exactly when $\alpha=\beta=0$.

**Corollary.** A general bispinor, sum of a scalar and a traceless part, has an arbitrary spectrum shifted by the scalar: the eigenvalues are $t\pm\alpha, t\pm\beta$ with $4t=\operatorname{tr}X$.

*Proof.* The decomposition $X=(\operatorname{tr}X/4)\mathrm I+Y$ with $Y$ traceless.

**The reading.** The general spectrum is a scalar shift of a symmetric pair, which is the spectral form of the decomposition of the algebra into the scalars and the traceless part.

## The Strata by Multiplicity

**Proposition.** The multiplicity patterns of four eigenvalues are the five partitions of four, and each pattern defines a locally closed stratum of the bispinor space.

*Proof.* A multiset of four values is described by a partition of four according to the multiplicities; the conditions of equality and inequality of the eigenvalues are algebraic and define locally closed sets.

**Corollary.** The generic stratum is the one with four distinct eigenvalues, of dimension sixteen, and the most degenerate is the single eigenvalue with multiplicity four.

*Proof.* Four distinct eigenvalues is an open condition; the single eigenvalue is the intersection of the conditions of equality.

**Corollary.** The pure bispinors lie in the pattern of one nonzero eigenvalue with multiplicity one and the zero with multiplicity three.

*Proof.* The pure spectrum.

**The reading.** The spectral stratification refines the rank stratification: the pure bispinors of rank one have a fixed pattern, and the other patterns contain bispinors of several ranks.

## The Carriers and the Ideals

**Proposition.** The carrier $V_0$ lies entirely in the stratum of a single eigenvalue with multiplicity four, and every other carrier meets the generic stratum.

*Proof.* The scalars have one eigenvalue; the carriers of positive label contain elements with four distinct eigenvalues, as the numerical spectra $4.912,1.637,-1.637,-4.912$ show.

**Corollary.** The ideals lie in the union of the patterns with at least three zero eigenvalues.

*Proof.* The elements of an ideal have rank at most one, so at least three eigenvalues vanish.

**Corollary.** The spectral strata and the carrier decomposition are independent: the same carrier meets several patterns and the same pattern meets several carriers.

*Proof.* The two previous statements.

**The reading.** The spectrum is a function on the algebra that is constant on neither the carriers nor the ideals, and the two decompositions cut it differently.

## The Boundary

**Against the rank article.** The rank constrains the number of zero eigenvalues from below and does not determine the pattern.

**Against the carrier spectral articles.** Those articles compute the possible spectra inside one carrier; this one stratifies the whole space.

**Against the determinant article.** The determinant is the product of the eigenvalues, the last of the elementary symmetric functions.

## The Ideals and the Spectrum

**Proposition.** Every element of a minimal left ideal has at least three vanishing eigenvalues, and the elements of rank one have exactly three.

*Proof.* An element of the ideal is $\psi\bar\chi^{\dagger}$, of rank one for nonzero factors and zero at the origin; a rank-one matrix has three zero eigenvalues.

**Corollary.** The spectrum of a pure bispinor is the pairing of its factors together with three zeros, and the trace is that pairing.

*Proof.* The square of the rank-one bispinor is the scalar multiple of itself given by the Fierz identity.

**Corollary.** The ideals lie entirely in the closure of the stratum with three zero eigenvalues, and they meet the generic stratum only at the origin.

*Proof.* The proposition and the definition of the strata.

**The reading.** The bispinor space contains the ideals as the locus where the spectrum collapses to a single value and three zeros, and the collapse is the spectral form of the rank condition.

## The Note on Order Two

**The lower analogue.** At order two the algebra has four complex dimensions and its carriers are the scalars and the triplet; there is no carrier of label three, so the spectral stratification computed here has no counterpart in the lower row, and the comparison stops at the statement that the chain has one term fewer.

**The count.** The bispinor space at order two is the algebra itself, of dimension four, and its elements are two-by-two matrices; the strata of that space are the two strata of the present article with the two free eigenvalue pairs replaced by the single pair of a two-by-two matrix, that is the origin and its complement.

## The Check of the Counts

**The eigenvalues.** The four eigenvalues of an element of the ideal are the pairing and three zeros, so the spectrum has one free value and the other three vanish; the trace is the pairing, and the second elementary symmetric function vanishes.

**The partitions.** The partitions realised by the elements of the ideal are $1+1+1+1$ at the nonzero elements of rank one and $0$ at the origin; there is no intermediate partition, and the ideal is the smallest spectral stratum of the bispinor space.

**The comparison with the algebra.** The whole algebra realises every partition of four, while the ideal realises only two; the difference is the measure of how much the rank condition restricts the spectrum.

## Summary

A pure bispinor satisfies $X^{2}=\omega(\bar\chi,\psi)X$, so its spectrum is one pairing and three zeros. A traceless bispinor has the symmetric spectrum $\{\pm\alpha,\pm\beta\}$ and characteristic polynomial $\lambda^{4}-(\operatorname{tr}X^{2}/2)\lambda^{2}+\det X$. A general bispinor is a scalar shift of a traceless one.

The multiplicity patterns are the five partitions of four, and they stratify the bispinor space. The carrier of label zero lies in the most degenerate pattern, the other carriers meet the generic one, and the ideals lie where at least three eigenvalues vanish.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\omega(\bar\chi,\psi)$ | the nonzero eigenvalue of a pure bispinor |
| $\{\pm\alpha,\pm\beta\}$ | the traceless spectrum |
| $t\pm\alpha,t\pm\beta$ | the general spectrum |
| $1+1+1+1,\dots,4$ | the multiplicity patterns |

## Further Reading

- [The Fierz–Kofink Identities and the Classification of Spinors at $n=4$](the-fierz-kofink-identities-at-n-4.html), for the Fierz identity.
- [The Spin-$\tfrac32$ Bispinors and the Rank Strata at $n=4$](the-spin-three-halves-bispinors-and-the-rank-strata-at-n-4.html), for the rank.
- [The Spin-Zero Carrier and the Spectral Strata at $n=4$](the-spin-zero-carrier-and-the-spectral-strata-at-n-4.html), for the symmetric spectra.
- [The Spin-$\tfrac12$ Bispinors and the Spectral Strata](the-spin-half-bispinors-and-the-spectral-strata.html), for the row at order two.
- [The Spin-$\tfrac32$ Bispinors and the Minimal Left Ideals](the-spin-three-halves-bispinors-and-the-minimal-left-ideals-at-n-4.html), for the ideals.
