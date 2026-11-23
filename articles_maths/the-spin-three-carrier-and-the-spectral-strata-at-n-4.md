# __The Spin-Three Carrier and the Spectral Strata at $n=4$__

## Introduction

**The subject.** On the carrier of label three the spectrum is $\{\pm\alpha,\pm\beta\}$ with $\alpha$ and $\beta$ independent, so the carrier realises four spectral strata: the generic one with four distinct eigenvalues, the two strata where the pairs collide or one pair vanishes, and the nilpotent stratum. The article computes them.

**The order of the article.** The first section fixes the spectrum and the two invariant parameters. The second lists the strata and their dimensions. The third computes the discriminant. The fourth contrasts the carrier with the quintet and the triplet. The fifth draws the boundary.

**It assumes** *Introduction to the Spin-Three Carrier at $n=4$: the Top of the Chain* and *The Spin-Two Carrier and the Trace Form at $n=4$*.

**The result in one line.** The spectrum on $V_3$ is $\{\pm\alpha,\pm\beta\}$ with $\alpha^{2}+\beta^{2}=-\operatorname{tr}(X^{2})/2$ and $\alpha^{2}\beta^{2}=\det X$, the strata have dimensions $7,6,6,5$, and the discriminant is proportional to $\alpha^{2}\beta^{2}(\alpha^{2}-\beta^{2})^{4}$.

**Boundaries.** The article treats the spectrum as a multiset; the ranks and the forms are treated in the adjacent articles.

## The Spectrum

**Proposition.** Every element of $V_3$ is traceless with vanishing cube trace, so its characteristic polynomial is $\lambda^{4}+e_2\lambda^{2}+e_4$ and its spectrum is $\{\pm\alpha,\pm\beta\}$ with $\alpha^{2}+\beta^{2}=-e_2=-\operatorname{tr}(X^{2})/2$ and $\alpha^{2}\beta^{2}=e_4=\det X$.

*Proof.* The trace and the cube trace vanish on the carrier; the polynomial is even, so its roots are paired; Newton's identities give the two elementary symmetric functions displayed.

**Corollary.** The two parameters $q=\operatorname{tr}(X^{2})$ and $d=\det X$ are independent on the carrier, unlike on the quintet.

*Proof.* The quadric $\operatorname{tr}(X^{2})=0$ carries the matrix unit $E_{03}$, whose determinant is zero, and also elements of rank four, one of which has determinant $14.1472+45.0994\,i$; the two values of the determinant at the same value of $q$ are different, so no function of $q$ can give the determinant.

**Corollary.** The spectrum has at most four distinct values and its multiplicities are those of a partition of four with parts of size at most two.

*Proof.* The roots come in opposite pairs.

**The reading.** The septet is spectrally two-dimensional: two free parameters, $q$ and $d$, in place of the single parameter of the quintet.

## The Strata

**Proposition.** The spectral strata of the carrier are: the generic stratum, where $\alpha^{2}\neq\beta^{2}$ and both are nonzero, of complex dimension seven; the stratum $\det X=0$, where one pair vanishes, of dimension six; the stratum $\alpha^{2}=\beta^{2}$, where the two pairs collide, of dimension six; and the nilpotent stratum $\alpha=\beta=0$, of dimension five.

*Proof.* The vanishing of the determinant is one equation; the collision of the pairs is the vanishing of the discriminant, also one equation; the nilpotent stratum imposes both, and the conditions are independent since $q$ and $d$ are independent parameters.

**Corollary.** The carrier has one open stratum and three closed ones of codimension one or two.

*Proof.* The dimensions displayed.

**Corollary.** The stratum $\det X=0$ is the union of the strata of rank at most three, and it is a hypersurface cut out by one quartic equation.

*Proof.* Singularity is the vanishing of the determinant, and the ranks below four are realised by $E_{03}$ and by the nilpotents.

**The reading.** The septet has the richest spectral stratification of the four carriers, with one stratum for each way the two pairs can degenerate.

## The Discriminant

**Proposition.** The discriminant of the characteristic polynomial is proportional to $\alpha^{2}\beta^{2}(\alpha^{2}-\beta^{2})^{4}$, so it vanishes exactly on the union of the two hypersurfaces $\det=0$ and $\alpha^{2}=\beta^{2}$.

*Proof.* The discriminant is the product of the squared differences of the roots: the differences are $2\alpha$, $2\beta$, $\alpha+\beta$, $\alpha-\beta$ and their negatives, and the product of their squares gives the formula.

**Corollary.** The discriminant vanishes to order two on the determinant hypersurface and to order four on the collision hypersurface.

*Proof.* The exponents in the formula.

**Corollary.** The discriminant is not a square and not a function of the determinant.

*Proof.* The exponents two and four and the presence of both factors.

**The reading.** The discriminant of the septet is the product of the two independent degenerations, and its two factors are the two ways a symmetric spectrum can fail to be generic.

## The Comparison

**Proposition.** On the triplet the spectrum is $\pm3\lambda/2,\pm\lambda/2$, one parameter; on the quintet it is $\{\pm s,\pm s\}$, one parameter; on the septet it is $\{\pm\alpha,\pm\beta\}$, two parameters; on the scalars it is $\{t,t,t,t\}$, one parameter.

*Proof.* The four computations.

**Corollary.** The number of spectral parameters is two for the septet and one for each of the other carriers, so the septet is the only carrier whose spectrum is not a function of a single invariant.

*Proof.* The comparison.

**Corollary.** The septet is the carrier whose spectral strata have the largest dimensions, since its carrier has the largest dimension.

*Proof.* The dimensions $7,6,6,5$ against $3,2$ for the triplet and $5,4,4$ for the quintet.

**The reading.** The septet is the least rigid carrier, and its spectral strata are the model for the generic behaviour of the algebra.

## The Boundary

**Against the rank article.** The rank strata refine the determinant hypersurface, which is one of the spectral strata.

**Against the Hermitian form article.** The Hermitian slice has the spectrum $\{\pm a,\pm b\}$ with $a$ and $b$ real and independent.

**Against the quintet.** The quintet has the spectrum $\{\pm s,\pm s\}$ and only two strata, and its discriminant is a power of the trace form.

## A Final Observation

**The two parameters.** The trace of the square and the determinant are independent on the septet, and each of them is an invariant polynomial of degree two and four respectively; the intermediate symmetric functions vanish identically, so the ring of invariant polynomials on the carrier is generated by two elements and has no odd generator.

**The Hermitian slice.** On the Hermitian slice the two parameters become real and positive: the trace of the square is a sum of squares and the determinant is a product of two positive numbers, so every Hermitian element of the carrier has the spectrum $\{\pm a,\pm b\}$ with $a$ and $b$ real.

## The Strata and the Weight String

**The strata in the weight basis.** In the weight basis the two parameters are the two elementary symmetric functions of the squared eigenvalues, and the strata are the loci where one of them degenerates; the highest weight vector has both parameters zero, so it lies in the smallest stratum.

**The nilpotent stratum.** The nilpotent stratum is the intersection of the two hypersurfaces, and it contains the matrix unit $E_{03}$ of the highest weight; the stratum therefore meets the extreme weight spaces, which is why the septet's spectral picture and its weight picture are different.

**The generic stratum.** The generic element has four distinct eigenvalues, and the four eigenspaces are lines that vary with the element; the carrier is therefore the space of all symmetric spectra, and the generic stratum is its open dense part.

**The reading.** The spectral strata of the septet are organised by the weight string, and the highest weight vector is the element where the two degenerations meet.

## The Check of the Counts

**The eigenvalues.** The four eigenvalues are the two pairs $\pm\alpha$ and $\pm\beta$, so the spectrum has two free values and the trace and the cube trace vanish; the two elementary symmetric functions are the sums of squares and the product of squares.

**The partitions.** The partitions realised are $1+1+1+1$ generically, $2+1+1$ when one pair vanishes, $2+2$ when the pairs coincide, and $4$ at the origin; the three degenerate partitions correspond to the three closed strata.

**The comparison with the algebra.** The whole algebra realises the same four partitions, because the septet is the generic carrier; the other carriers realise proper subsets, and the scalar carrier realises only one.

## Summary

The spectrum on the carrier of label three is $\{\pm\alpha,\pm\beta\}$ with the two parameters $\operatorname{tr}(X^{2})$ and $\det X$ independent. The spectral strata are the generic stratum of dimension seven, the determinant hypersurface and the collision hypersurface of dimension six, and the nilpotent stratum of dimension five.

The discriminant is proportional to $\alpha^{2}\beta^{2}(\alpha^{2}-\beta^{2})^{4}$, the product of the two independent degenerations, so the septet is the only carrier whose spectrum is not a function of one invariant.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\{\pm\alpha,\pm\beta\}$ | the spectrum |
| $\operatorname{tr}(X^{2})$, $\det X$ | the two independent parameters |
| $7,6,6,5$ | the dimensions of the strata |
| $\alpha^{2}\beta^{2}(\alpha^{2}-\beta^{2})^{4}$ | the discriminant |

## Further Reading

- [Introduction to the Spin-Three Carrier at $n=4$: the Top of the Chain](introduction-to-the-spin-three-carrier-of-m4c.html), for the carrier.
- [The Spin-Three Carrier and the Rank Strata at $n=4$](the-spin-three-carrier-and-the-rank-strata-at-n-4.html), for the ranks.
- [The Spin-Three Carrier and the Hermitian Form at $n=4$](the-spin-three-carrier-and-the-hermitian-form-at-n-4.html), for the Hermitian slice.
- [The Spin-Two Carrier and the Trace Form at $n=4$](the-spin-two-carrier-and-the-trace-form-at-n-4.html), for the comparison.
- [The Spin-Zero Carrier and the Spectral Strata at $n=4$](the-spin-zero-carrier-and-the-spectral-strata-at-n-4.html), for the scalars.
