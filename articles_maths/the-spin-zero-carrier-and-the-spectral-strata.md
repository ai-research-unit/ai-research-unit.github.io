# __The Spin-Zero Carrier and the Spectral Strata__

## Introduction

**The subject.** A scalar operator has one eigenvalue and one only, of multiplicity equal to the dimension on which it acts. The article describes the spectrum of the carrier, shows that its discriminant vanishes identically, splits the carrier into the singular point and the invertible part, compares the result with the carrier of the elements, and places the carrier inside the spectral classification of the sixteen-dimensional space.

**The order of the article.** The spectrum comes first; the discriminant second. The singular locus follows, then the comparison with the elements, then the position in the classification, and the reading closes.

**It assumes** *The Spin-Zero Carrier: the Scalars*, *The Spectrum of a Biquaternion* and *The Spin-Zero Carrier and the Determinant*. **The row of the spin-zero carrier is** where the scalar biquaternion also has a single spectral point, of multiplicity four.

**The result in one line.** The spectrum of the operator of multiplication by $\lambda$ is the single point $\lambda$ with multiplicity sixteen, its discriminant vanishes for every $\lambda$, and the carrier is the unique line of the space on which the spectral stratification has only the two strata of the origin and the rest.

**Boundaries.** The determinant is *The Spin-Zero Carrier and the Determinant*; the rank is *The Spin-Zero Carrier and the Rank Strata*; the spectrum of an element is *The Spectrum of a Biquaternion*.

## The Spectrum

**Definition.** The spectrum of an operator is the set of the roots of its characteristic polynomial, counted with multiplicity; a **spectral stratum** is the set of the operators with a given multiplicity pattern.

**Theorem.** The operator of left composition with $\lambda\mathrm I$ on the sixteen-dimensional space has the single eigenvalue $\lambda$, of algebraic multiplicity sixteen.

*Proof.* Left composition with a scalar operator acts on every vector of the space by the multiplication by $\lambda$, so every vector is an eigenvector with the eigenvalue $\lambda$; the characteristic polynomial is $(t-\lambda)^{16}$.

**Corollary.** The geometric multiplicity is also sixteen, so the operator is diagonalisable for every $\lambda$.

*Proof.* Every vector of the space is an eigenvector.

**Corollary.** The trace is $16\lambda$ and the determinant is $\lambda^{16}$, in agreement with the elementary computation.

*Proof.* The sum and the product of the eigenvalues.

**The reading.** One eigenvalue, sixteen times, and no structure. The carrier is spectrally the most degenerate line of the space, and its spectrum is the spectrum of a homothety.

## The Discriminant

**Proposition.** The discriminant of the characteristic polynomial of a scalar operator vanishes identically on the carrier.

*Proof.* The discriminant is the product of the squared differences of the roots, and with a single root every difference is zero.

**Corollary.** The carrier is contained in the discriminant locus of the space, and no point of it is spectrally simple.

*Proof.* The vanishing of the discriminant is the defining condition of the locus.

**Corollary.** The discriminant is not a good coordinate on the carrier, since it cannot separate its points; the multiplier is.

*Proof.* The discriminant is identically zero on the carrier.

**The reading.** The discriminant detects the collision of eigenvalues, and on the carrier every eigenvalue has collided with every other. The carrier is the extreme case of the discriminant locus, not a generic point of it.

## The Singular Locus

**Theorem.** The carrier meets the singular locus of the algebra of the operators at the single point of the zero operator, and away from it every scalar operator is invertible.

*Proof.* The operator is invertible exactly when its determinant does not vanish, and the determinant of the carrier is $\lambda^{16}$.

**Corollary.** The singular locus of the space is the set of the non-invertible operators, and its intersection with the carrier is the origin.

*Proof.* The two strata of the carrier.

**Corollary.** The two spectral strata of the carrier inside the invertible part coincide, since the spectrum has one point for every multiplier.

*Proof.* The spectrum depends only on the multiplier.

**The reading.** Inside the carrier the spectral data is one complex number, and the singular locus is the value zero of that number. The carrier is a line whose spectral classification is the classification of the complex numbers: one stratum of invertibles and one point.

## The Comparison with the Elements

**Proposition.** On the algebra the left multiplication by $X$ has the spectrum of $X$ repeated four times, so the spectral reading of the elements is the spectral reading of the carrier at the level of one copy.

*Proof.* The left multiplication acts on the algebra as the multiplication by $X$, and the eigenvalues of that map are the eigenvalues of $X$, each repeated with the multiplicity of the module.

**Corollary.** For a scalar biquaternion the spectrum is the single point $\lambda$, of multiplicity four, and the discriminant vanishes there as well.

*Proof.* The spectrum of the scalar and the fourfold repetition.

**Corollary.** The carrier of the elements and the carrier of the operators are spectrally the same line, read at two different multiplicities.

*Proof.* The exponents four and sixteen.

**The reading.** The two rows agree on the carrier in everything except the multiplicity. The agreement is the reason the carrier is the natural place to compare the rows, and the multiplicity is the only thing that changes.

## The Position in the Classification

**Theorem.** The carrier is the unique line of the space whose spectral stratification consists of a single invertible stratum and a single singular point.

*Proof.* A line of operators with a spectrum depending on one parameter and degenerating only at one value must consist of the homotheties, and the homotheties form the carrier.

**Corollary.** Every other carrier has a spectrum that varies in more than one direction, so its spectral stratification has more than two strata.

*Proof.* The other carriers contain operators with different eigenvalue patterns.

**Corollary.** The carrier is the base point of the spectral classification: every other stratum of the space has the carrier in its closure.

*Proof.* A general operator can be deformed to a homothety by scaling its traceless part.

**The reading.** The spin-zero carrier is spectrally the most degenerate point of the whole row: one eigenvalue, one stratum of invertibles, one singularity, and the closure of everything else.

**A numerical check.** The characteristic polynomial of the carrier is $(t-\lambda)^{16}$, whose coefficient of $t^{15}$ is $-16\lambda$ and whose constant term is $\lambda^{16}$; the trace and the determinant of the carrier are these two numbers up to sign, in agreement with the elementary computation of the two invariants.

## The Spectral Projectors

**Definition.** For a value $\lambda$ the **spectral projector** of an operator is the operator that projects onto the sum of the generalised eigenspaces of $\lambda$ along the sum of the others.

**Proposition.** On the scalar carrier the spectral projector of $\lambda$ is the identity for every nonzero $\lambda$, and it is zero at $\lambda=0$.

*Proof.* The operator of multiplication by $\lambda$ has the single eigenvalue $\lambda$ with multiplicity sixteen, so the whole space is its eigenspace when $\lambda\neq0$; at $\lambda=0$ the operator is zero and every vector is in the kernel.

**Corollary.** The rank of the spectral projector is sixteen or zero, and it agrees with the rank of the operator itself.

*Proof.* The projector is the identity or zero, and the operator is a homothety with the same multiplier.

**Corollary.** The carrier is the only line of the space on which the spectral projectors do not depend on the operator beyond a single parameter.

*Proof.* On a carrier of positive label the operator has several eigenvalues, and its projectors are sums of eigenspaces of the conjugation element that defines the carrier.

**The reading.** The spectral picture of the carrier is as simple as it can be: one eigenvalue, one projector, no generalised part. The spectral strata are the two sets cut by the vanishing of the multiplier, and the projectors are the identity and zero, in agreement with the rank strata computed separately.

## Further Reading

- [The Spin-Zero Carrier: the Scalars](the-spin-zero-carrier-of-the-biquaternion-operators.html), for the carrier itself.
- [The Spin-Zero Carrier and the Determinant](the-spin-zero-carrier-and-the-determinant.html), for the exponent sixteen.
- [The Spectrum of a Biquaternion](the-spectrum-of-a-biquaternion.html), for the spectral reading of the elements.
- [The Spin-Zero Carrier and the Rank Strata](the-spin-zero-carrier-and-the-rank-strata.html), for the rank stratification.
