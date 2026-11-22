# __The Spin-Three Carrier and the Rank Strata__

## Introduction

**The subject.** The septet is the only carrier of the operator row that realises every rank of a linear map of the four-dimensional algebra. The article proves it, computes the rank of each element of the weight string, shows that the singular locus is a hypersurface of dimension six, and reads the stratification against the spectral one.

**The order of the article.** The rank of the weight vectors comes first, then the theorem that every value from zero to four occurs. The two strata and their dimensions follow, then the agreement with the spectrum, the comparison with the other carriers, and the identification of the singular locus with the zero divisors of the operator algebra.

**It assumes** *Introduction to the Spin-Three Carrier: the Top of the Chain* and *The Spin-Three Carrier and the Hermitian Form*. **The row of the elements is** where an element is a map of a two-dimensional space and its rank is at most two, so the values three and four of this article have no counterpart there.

**The result in one line.** On the weight string the rank is $4-\lvert m\rvert$, so the seven weights realise the ranks $1,2,3,4,3,2,1$; the invertible elements form an open stratum of dimension seven, the singular elements a hypersurface of dimension six, and the carrier meets every rank stratum of the operator space.

**Boundaries.** The carrier and its forms are the two preceding articles; the spectral strata, which are finer, are *The Spin-Three Carrier and the Spectral Strata*; the rank of a two-sided operator is *The Four Ranks of the Two-Sided Operators*.

## The Rank of the Weight Vectors

**Proposition.** Let $v_m$ be the weight vector of weight $m$ in the carrier, normalised in the weight basis. As a linear map of the algebra it has rank $4-\lvert m\rvert$:
$$
\operatorname{rank}v_3=1,\quad \operatorname{rank}v_2=2,\quad \operatorname{rank}v_1=3,\quad \operatorname{rank}v_0=4,\quad \operatorname{rank}v_{-1}=3,\quad \operatorname{rank}v_{-2}=2,\quad \operatorname{rank}v_{-3}=1 .
$$

*Proof.* The module is the symmetric cube of the spinor space, and the highest weight vector of the carrier is built from the cube $s^{\odot3}$ of a spinor; read as an operator it is a pure product, of rank one. The projection onto the carrier along the triplet does not change the rank at the top of the string, because the triplet has no component of weight three. The vector of weight zero is the Cartan operator of the copy, whose four weights are $3,1,-1,-3$ up to the normalisation, all distinct and nonzero, so its rank is four. The intermediate vectors are the images of the highest vector under the powers of the lowering operator, and each power lowers the rank by one, as the explicit chain shows.

**Corollary.** The elements of rank one form the cone over the orbit of the highest weight vector, and that cone has real dimension three.

*Proof.* The orbit of a highest weight vector under the copy is the quotient of the copy by the stabiliser, a two-sphere, and the cone adds one real dimension of scale.

**Corollary.** The carrier contains elements of every rank from zero to four, and it is the only carrier of the row with that property.

*Proof.* The seven weight vectors give the ranks displayed, and the zero operator gives rank zero. The carriers of labels zero, one and two take the ranks four, the ranks three and four, and the ranks two and four respectively, so none of them meets every stratum.

**The reading.** The rank follows the distance from the ends of the string: the further an element is from the extreme weights, the larger its rank. The top carrier is therefore the one whose weight string reads the whole list of possible ranks.

## The Two Strata

**Theorem.** The carrier splits into an open stratum of invertible elements, of dimension seven, and a singular hypersurface of dimension six, whose points are the elements of rank at most three.

*Proof.* The determinant is a homogeneous polynomial of degree four on the seven-dimensional carrier. It is not identically zero, since the weight-zero element is invertible, so its zero set is a hypersurface, of dimension six, and its complement is open and of dimension seven. An element of the carrier is invertible exactly when its determinant does not vanish, and otherwise its rank is at most three.

**Corollary.** The generic element of the carrier has rank four, and the singular elements have rank at most three.

*Proof.* The complement of a hypersurface is open and dense, and every element of it is invertible by the theorem.

**Corollary.** The rank cuts the carrier into exactly two pieces, the invertible elements and the singular ones, and the finer subdivision by the exact value of the rank lies inside the singular piece.

*Proof.* The determinant separates the two pieces; inside the singular piece the value of the rank distinguishes three, two, one and zero, and each of those sets is contained in the zero set of the determinant. The value one is reachable because a two-sided product of two degenerate elements has rank $\operatorname{rank}L_a\operatorname{rank}R_b/4=1$.

**The reading.** The top carrier is the one on which the determinant is a genuine function of degree four, not a power of a single quadratic invariant. Its zero set is therefore a hypersurface, and the rank stratification has one stratum of each dimension below the top.

## The Agreement with the Spectrum

**Proposition.** The singular locus of the carrier is the set of elements with a vanishing eigenvalue, and on the carrier this is the same set as the set of elements of rank at most three.

*Proof.* An eigenvalue is a root of the characteristic polynomial, and
$$
\det X=\prod_{i=1}^{4}\lambda_i,\qquad \operatorname{rank}X=\#\{\,i:\lambda_i\neq0\,\},
$$
so a vanishing determinant is a vanishing eigenvalue, and a vanishing eigenvalue is a nontrivial kernel.

**Corollary.** The rank and the spectrum cut the same hypersurface, and they differ only in the refinement inside it.

*Proof.* The two conditions are equivalent by the proposition; the spectrum records the multiplicities of the remaining eigenvalues, and the rank records only the number of nonzero ones.

**The reading.** On the septet the coarse spectral predicate and the coarse rank predicate agree. This is not true of every carrier: on the quintet the rank takes only even values, so the vanishing of an eigenvalue already forces the rank down by two.

## The Comparison with the Other Carriers

**Proposition.** The four carriers realise the following ranks as their elements vary:

| carrier | dimension | ranks realised |
|---|---|---|
| $V_3$ | $7$ | $0,1,2,3,4$ |
| $V_2$ | $5$ | $0,2,4$ |
| $V_1$ | $3$ | $0,3,4$ |
| $V_0$ | $1$ | $0,4$ |

*Proof.* The septet by the first proposition; the quintet because its elements satisfy a quadratic equation with a double root, so the rank is even; the triplet because its elements have the spectrum $\{3c,c,-c,-3c\}$ at the Cartan direction and are nilpotent of rank three at the two nilpotent directions; the singlet because it consists of the multiples of the identity.

**Corollary.** The top carrier is the only one that meets every rank stratum of the operator space, and the three lower carriers miss at least two values each.

*Proof.* The table: the missing values are one and three for the quintet, one and two for the triplet, and one, two and three for the singlet.

**The reading.** The rank of an element of a carrier is constrained by the label. The higher the label, the more ranks occur, and the top carrier is the one on which the constraint disappears.

## The Singular Locus and the Zero Divisors

**Proposition.** The singular locus of the carrier is the set of its elements that are zero divisors of the operator algebra, and it has dimension six.

*Proof.* An element of rank at most three has a nonzero kernel, so it annihilates a nonzero operator and is a zero divisor of the operator algebra; conversely a zero divisor has a nontrivial kernel and cannot be invertible. The dimension is that of the hypersurface of the determinant.

**Corollary.** The algebra of biquaternions has no zero divisors, and the carrier of its operators has a singular locus of codimension one.

*Proof.* Every element of nonvanishing norm is invertible, so its left multiplication is a bijection; the elements of vanishing norm form a hypersurface, and the septet meets it in a hypersurface of its own.

**Corollary.** The intersection of the carrier with the singular set of the whole operator space is the determinant hypersurface, and no two-sided operator with two nonzero parameters lies in it.

*Proof.* A two-sided operator with two nonzero parameters is a product of two bijections; the carrier contains singular elements by the theorem.

**The reading.** The top carrier is the carrier that meets the singular set of the operator algebra in the largest possible way, and it is the only one for which that intersection has codimension one.

## Further Reading

- [The Spin-Three Carrier and the Spectral Strata](the-spin-three-carrier-and-the-spectral-strata.html), for the finer stratification.
- [Introduction to the Spin-Three Carrier: the Top of the Chain](introduction-to-the-spin-three-carrier-the-top-of-the-chain.html), for the carrier and the weight string.
- [The Spin-Three Carrier and the Hermitian Form](the-spin-three-carrier-and-the-hermitian-form.html), for the form and its isotropic vectors.
- [The Spin-Two Carrier and the Rank Strata](the-spin-two-carrier-and-the-rank-strata.html), for the middle carrier.
- [The Four Ranks of the Two-Sided Operators](the-four-ranks-of-the-two-sided-operators.html), for the rank of a product.
