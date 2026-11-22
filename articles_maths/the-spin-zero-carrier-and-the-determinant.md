# __The Spin-Zero Carrier and the Determinant__

## Introduction

**The subject.** The determinant is the only multiplicative invariant of the algebra of the operators, and on the spin-zero carrier it is a power of a single complex number. The article computes the exponent, splits the carrier into its invertible part and its singular point, shows that the determinant alone does not separate the points of the carrier, and compares the exponent with the exponent of the row of the elements.

**The order of the article.** The determinant of a scalar operator comes first; the two strata second. The multiplicative property follows, then the comparison with the elements, then the two invariants, and the reading closes.

**It assumes** *The Spin-Zero Carrier: the Scalars*, *The Element Rank, Trace, Determinant and Characteristic Polynomial* and *The Algebraic Norms $H,N,K$ of a Biquaternion*. **The row of the spin-zero carrier is** where the determinant of a scalar is the square of a square, with the exponent four.

**The result in one line.** The determinant of the operator of multiplication by $\lambda$ is $\lambda^{16}$ on the sixteen-dimensional space and $\lambda^{4}$ on the algebra, so it vanishes only at the origin of the carrier, where the operator is singular.

**Boundaries.** The carrier is *The Spin-Zero Carrier: the Scalars*; the spectra are *The Spin-Zero Carrier and the Spectral Strata*; the rank is *The Spin-Zero Carrier and the Rank Strata*.

## The Determinant of a Scalar Operator

**Definition.** The determinant of an operator is the product of its eigenvalues, each counted with its algebraic multiplicity, and the characteristic polynomial is the polynomial whose roots are those eigenvalues.

**Theorem.** The operator of left composition with $\lambda\mathrm I$ on the sixteen-dimensional space has the determinant $\lambda^{16}$, and the operator $\lambda\mathrm I$ as a map of the algebra has the determinant $\lambda^{4}$.

*Proof.* Left composition with a scalar operator acts on the four copies of the module in the space of the operators, and it acts on each copy as the multiplication by $\lambda$. The determinant of the fourfold repetition is the fourth power of the determinant on one copy, which is $\lambda^{4}$; the determinant on the algebra is the fourth power of the multiplier, since the algebra has dimension four.

**Corollary.** The determinant of a scalar operator is the fourth power of the determinant of the same scalar read as a map of the algebra, so the two readings differ by the exponent of the space.

*Proof.* $\lambda^{16}=(\lambda^{4})^{4}$.

**Corollary.** The determinant of the carrier is a single power, and its degree is the dimension of the space in the first reading and of the algebra in the second.

*Proof.* The two exponents are sixteen and four.

**The reading.** The exponent is the only thing the determinant remembers about the carrier. It is the dimension of the space in which the operator acts, and the choice of reading is the choice of that dimension.

## The Two Strata

**Proposition.** The carrier splits into the invertible scalars, for which $\lambda\neq0$, and the single singular point, for which $\lambda=0$.

*Proof.* The determinant vanishes exactly when the multiplier vanishes, and it is the only condition for the singularity of a scalar operator.

**Corollary.** The invertible stratum of the carrier is the punctured line, of complex dimension one and real dimension two minus a point.

*Proof.* The multiplier ranges over the complex numbers minus the origin.

**Corollary.** The singular stratum is a single point, the zero operator, and it is the only operator of the carrier that is not invertible.

*Proof.* The zero operator is the only scalar operator of vanishing multiplier.

**The reading.** Two strata, one open and one closed, and no others. The carrier is the simplest stratified object of the theory: a punctured line and a point, with the determinant as the coordinate that separates them.

## The Multiplicative Invariant

**Theorem.** The determinant is multiplicative, and it is the only multiplicative invariant of the algebra of the operators that is a polynomial of degree one in each factor.

*Proof.* The determinant of a product is the product of the determinants, since the product acts by composition. An invariant that is multiplicative and polynomial of degree one in each factor is determined by its values on the generators, and those values are the determinant's.

**Corollary.** The determinant of a product of two scalar operators is the product of their determinants, so the restriction of the determinant to the carrier is a character of the multiplicative group of the scalars.

*Proof.* $\det(\lambda\mu\,\mathrm I)=\lambda^{16}\mu^{16}$.

**Corollary.** The determinant is trivial on no element of the carrier except the units of modulus one to the appropriate power, and it is injective on the carrier only after the sixteenth root is taken.

*Proof.* The kernel of the determinant on the punctured line is the group of the sixteenth roots of unity.

**The reading.** The determinant is the multiplicative invariant, and on the carrier it is a power map. The kernel is finite, of order sixteen, and this is the only place of the theory where a finite group of that order appears from a single invariant.

## The Comparison with the Elements

**Proposition.** On the algebra the determinant of the left multiplication by $X$ is the square of the algebraic norm, and its degree in $X$ is four.

*Proof.* The left multiplication by $X$ is, in the complex two-dimensional description, the map $Y\mapsto XY$ on the algebra of two-by-two complex combinations, and its determinant is $\det(X)^{2}$; the determinant of $X$ is the algebraic norm $N(X)$, a quadratic form in the four coefficients, so the square is of degree four.

**Corollary.** The exponent on the elements is four and the exponent on the operators is sixteen, and the ratio is the dimension of the module.

*Proof.* The determinant of the left multiplication adds two powers of the norm per factor, and the space of the operators repeats the module four times.

**Corollary.** For a scalar $X=\lambda$ the algebraic norm is $\lambda^{2}$ and the determinant of the left multiplication is $\lambda^{4}$, in agreement with the carrier computation.

*Proof.* The norm of a scalar biquaternion is the square of its complex value.

**The reading.** The two rows differ by the exponent and by nothing else: the invariant is the same determinant, raised to the dimension of the space in which it acts. At the elements the exponent is four, at the operators sixteen, and the algebraic norm is the square root in the first case and the fourth root in the second.

## The Two Invariants

**Proposition.** The trace and the determinant separate the points of the carrier, since the trace gives the multiplier and the determinant gives its sixteenth power.

*Proof.* The pair $(\operatorname{tr},\det)=(16\lambda,\lambda^{16})$ determines $\lambda$, and no other operator of the carrier shares both values.

**Corollary.** The two invariants are independent on the carrier and dependent on its image under the determinant, which is a sixteenth power.

*Proof.* The trace is linear and the determinant has degree sixteen.

**Corollary.** Away from the carrier the trace and the determinant do not separate the points, since the traceless part is invisible to both.

*Proof.* The traceless hyperplane has dimension fifteen and both invariants are constant on its translates along the scalar direction.

**The reading.** The carrier is the line on which the two classical invariants are a coordinate system. Elsewhere they need help, and the help is the rest of the characteristic polynomial.

## Further Reading

- [The Spin-Zero Carrier: the Scalars](the-spin-zero-carrier-of-the-biquaternion-operators.html), for the carrier itself.
- [The Element Rank, Trace, Determinant and Characteristic Polynomial](the-element-rank-trace-determinant-characteristic-polynomial.html), for the determinant in general.
- [The Spin-Zero Carrier and the Spectral Strata](the-spin-zero-carrier-and-the-spectral-strata.html), for the eigenvalues.
- [The Spin-Zero Carrier and the Rank Strata](the-spin-zero-carrier-and-the-rank-strata.html), for the rank.
