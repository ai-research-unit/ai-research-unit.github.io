# __The Spin-Three Carrier and the Spectral Strata__

## Introduction

**The subject.** The elements of the septet have four eigenvalues summing to zero, and the multiplicities they can show are the spectral strata of the carrier. The article computes the characteristic polynomial, lists the strata with their dimensions, identifies the function that cuts them, and compares the spectral stratification with the rank stratification of the preceding article.

**The order of the article.** The spectrum and the vanishing of the trace come first. The multiplicity patterns and their dimensions follow, then the discriminant, the singular types and their identification with the zero divisors, and the comparison with the rank.

**It assumes** *The Spin-Three Carrier and the Rank Strata* and *Introduction to the Spin-Three Carrier: the Top of the Chain*. **The row of the elements is** where a spectrum has four values read from a left multiplication, all equal to the coefficient of the element, and where no coincidence can occur except at zero.

**The result in one line.** On the carrier the trace vanishes identically, the characteristic polynomial is $\lambda^{4}+c_2\lambda^{2}+c_3\lambda+c_4$, the generic spectrum is simple, the coincidence locus is cut by a discriminant of degree twelve and has dimension six, and the singular spectrum is the spectrum of a zero divisor of the operator algebra.

**Boundaries.** The rank stratification is *The Spin-Three Carrier and the Rank Strata*; the forms are *The Spin-Three Carrier and the Hermitian Form*; the spectrum of an element of the algebra itself is *The Spectrum of a Biquaternion*.

## The Spectrum

**Theorem.** Every element of the carrier is traceless, so its characteristic polynomial has the shape
$$
\chi_X(\lambda)=\lambda^{4}+c_2\lambda^{2}+c_3\lambda+c_4 ,
$$
and its four eigenvalues, counted with multiplicity, sum to zero.

*Proof.* The trace is the invariant linear functional of the operator space, and it vanishes on every summand of positive label because the trivial summand is the only one on which it is nonzero. The coefficient of $\lambda^{3}$ in the characteristic polynomial is minus the trace, so it vanishes, and the sum of the roots is zero by the same identity.

**Corollary.** The weight vectors of nonzero weight are nilpotent, and the weight-zero vector is the Cartan operator with the spectrum $\{3c,c,-c,-3c\}$ for a nonzero $c$.

*Proof.* A weight vector of weight $m\neq0$ has all its eigenvalues equal to zero, since its trace and all its higher traces vanish by the weight count; the weight-zero vector is proportional to the Cartan operator, whose spectrum is the four weights of the module up to a common factor.

**Corollary.** The generic element of the carrier has four distinct eigenvalues.

*Proof.* The set of elements with a repeated eigenvalue is the zero set of a nonzero polynomial, the discriminant, and the complement of a hypersurface is open and dense.

**The reading.** The spectrum of an element of the top carrier is the most general that the operator row admits: four values with one relation. The lower carriers impose further relations, the quintet a double root and the triplet the ratio of three.

## The Multiplicity Patterns

**Proposition.** The multiplicity patterns that occur are $1+1+1+1$, $2+1+1$, $2+2$, $3+1$ and $4$, and their strata have dimensions
$$
7,\quad 6,\quad 5,\quad 5,\quad 4
$$
in the carrier.

*Proof.* The simple pattern is open by the corollary above. Each coincidence of two eigenvalues is one equation on the carrier, and the patterns listed impose respectively none, one, two, two and three independent coincidences; a partition of four imposes as many equations as the number of parts minus one, which gives the dimensions displayed.

**Corollary.** The carrier contains elements with a triple eigenvalue, and it contains them in a stratum of dimension five.

*Proof.* The pattern $3+1$ appears in the list, with the dimension computed from two coincidences.

**The reading.** The top carrier is the carrier on which every multiplicity pattern occurs. On the quintet only the patterns $2+2$ and $4$ occur, and on the triplet only $1+1+1$ and $3$; the septet is the only one whose spectral list is complete.

## The Discriminant

**Definition.** The **discriminant** of an element of the carrier is
$$
\Delta(X)=\prod_{i<j}(\lambda_i-\lambda_j)^{2},
$$
a symmetric function of the eigenvalues, hence a polynomial in the coefficients of the characteristic polynomial and therefore in the coordinates of the carrier.

**Proposition.** The discriminant is a homogeneous polynomial of degree twelve in the coordinates of the carrier, it is not identically zero, and its zero set is the union of the strata in which two eigenvalues coincide.

*Proof.* The product of the twelve factors is homogeneous of degree twelve in the eigenvalues, and the eigenvalues are linear in the coordinates. The discriminant is not identically zero because the generic element has a simple spectrum. It vanishes exactly when two eigenvalues coincide, which is the union of the strata other than the simple one.

**Corollary.** The coincidence locus is a hypersurface of dimension six, and it contains the singular locus of the previous article.

*Proof.* The zero set of a nonzero polynomial is a hypersurface; an element with a vanishing eigenvalue has its zero coinciding with itself, so the singular locus lies in the coincidence locus.

**The reading.** Two different hypersurfaces cut the carrier: the discriminant, of degree twelve, cuts the coincidences of eigenvalues, and the determinant, of degree four, cuts the vanishing of one of them. They meet in the locus where zero is a repeated eigenvalue.

## The Singular Types

**Proposition.** The singular elements of the carrier are the elements with a vanishing eigenvalue, and the nilpotent types that occur are $[2,1,1]$, $[2,2]$ and $[4]$.

*Proof.* The singular elements are those of rank at most three; among the weight vectors, the one of weight three has rank one and square zero, of type $[2,1,1]$; the one of weight two has rank two and square zero, of type $[2,2]$; and the one of weight one has rank three, square of rank two and cube of rank one, a single block of size four. Every nilpotent of the carrier is conjugate to one of these under the copy.

**Corollary.** The singular spectral types are exactly the zero divisors of the operator algebra that the carrier contains.

*Proof.* A vanishing eigenvalue is a nontrivial kernel, and a nontrivial kernel is a zero divisor of the endomorphism algebra; conversely a zero divisor has a nontrivial kernel and a vanishing eigenvalue.

**Corollary.** The algebra of biquaternions contributes no singular type, since it has no zero divisors at all.

*Proof.* An element of nonvanishing norm is invertible and has a spectrum of four nonzero values; an element of vanishing norm is a zero divisor, and its spectrum contains zero. A two-sided product of two degenerate elements is neither, and its rank is $\operatorname{rank}L_a\operatorname{rank}R_b/4=1$.

**The reading.** The singular spectral types of the carrier are properties of the operator algebra and not of the algebra. The distinction is the one between an element and an operator on elements, and it appears here as the difference between a spectrum with no zero and a spectrum with one.

## The Comparison with the Rank

**Proposition.** The rank stratification is coarser than the spectral stratification on the carrier, and neither determines the other.

*Proof.* Two elements with the same rank can have different multiplicity patterns, since the rank records only the number of nonzero eigenvalues; two elements with the same pattern can have different ranks, since the pattern records multiplicities and not the vanishing of a value.

**Corollary.** The spectral strata refine the singular locus, and the refinement is proper.

*Proof.* The singular locus is the stratum on which some eigenvalue vanishes, and it contains elements of several patterns, which the finer stratification separates.

**Corollary.** The spectral stratification is the finer of the two on the top carrier, and it is the finer of the two on every carrier of the row.

*Proof.* The rank is a function of the spectrum, namely the number of nonzero eigenvalues, while the spectrum retains the values themselves.

**The reading.** The rank is the shadow of the spectrum under the map that forgets the values. On the top carrier the shadow is faithful enough to cut the same hypersurface, and the finer information is the one carried by the multiplicities.

## The Trace and the Determinant

**Proposition.** On the carrier the trace vanishes identically, so it separates no stratum; the determinant separates the singular stratum and the discriminant separates the coincidence stratum.

*Proof.* The trace is zero by the theorem of the first section. The determinant vanishes exactly on the singular stratum, and the discriminant exactly on the coincidence stratum, both by the propositions above.

**Corollary.** The two functions that separate the strata of codimension one are the determinant and the discriminant, of degrees four and twelve.

*Proof.* The two hypersurfaces are cut by those two polynomials.

**The reading.** On a carrier with a nonzero trace the trace would be one of the separating functions. Here it is identically zero, and the carrier is cut by the determinant and by the discriminant alone. The top carrier carries the finest spectral stratification of the row, and that is why it is the last: a finer stratification needs a longer weight string.

## Further Reading

- [The Spin-Three Carrier and the Rank Strata](the-spin-three-carrier-and-the-rank-strata.html), for the coarser stratification.
- [Introduction to the Spin-Three Carrier: the Top of the Chain](introduction-to-the-spin-three-carrier-the-top-of-the-chain.html), for the carrier and the weights.
- [The Spectrum of a Biquaternion](the-spectrum-of-a-biquaternion.html), for the spectrum of an element of the algebra.
- [The Spin-Three Carrier and the Hermitian Form](the-spin-three-carrier-and-the-hermitian-form.html), for the isotropic directions of the form.
- [Zero Divisors and Invertibles in the Biquaternion Algebra](zero-divisors-and-invertibles-in-the-biquaternion-algebra.html), for the zero divisors and the invertibles.
