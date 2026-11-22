# __The Spin-One Carrier and the Spectral Strata at $n=4$__

## Introduction

**The subject.** Every element of the carrier of label one has the spectrum $\pm3\lambda/2,\pm\lambda/2$ for a complex number $\lambda$, so the carrier has exactly two spectral types up to the value of $\lambda$: the semisimple type and the nilpotent type. The article computes the strata and the discriminant.

**The order of the article.** The first section fixes the characteristic polynomial. The second lists the strata. The third computes the discriminant and the locus where it vanishes. The fourth compares with the other carriers. The fifth draws the boundary.

**It assumes** *The Spin-One Carrier of $M_4(\mathbb{C})$: the Adjoint Triplet* and *The Spin-Zero Carrier and the Spectral Strata at $n=4$*. The row at order two is *The Spin-One Carrier and the Spectral Strata*.

**The result in one line.** The characteristic polynomial on the triplet is $\lambda^{4}-(5\lambda^{2}/2)\mu^{2}+(9\lambda^{4}/16)$ in the variable $\mu$, the strata are the semisimple cone $\lambda\neq0$ and the nilpotent cone $\lambda=0$, and the discriminant is proportional to $\lambda^{6}$.

**Boundaries.** The article treats the spectrum as a multiset; the rank and the eigenvectors are treated in the adjacent articles.

## The Characteristic Polynomial

**Proposition.** For $X=aJ_x+bJ_y+cJ_z$ the characteristic polynomial is $\mu^{4}-(5\lambda^{2}/2)\mu^{2}+9\lambda^{4}/16$, where $\lambda^{2}=a^{2}+b^{2}+c^{2}$.

*Proof.* The eigenvalues are $\pm3\lambda/2,\pm\lambda/2$, so the polynomial is $(\mu^{2}-9\lambda^{2}/4)(\mu^{2}-\lambda^{2}/4)$.

**Corollary.** The quadratic coefficient is $-\operatorname{tr}(X^{2})/2=-5\lambda^{2}/2$, and the constant term is $\det X=9\lambda^{4}/16$.

*Proof.* The expansion and the value of the trace form.

**Corollary.** The polynomial depends on the element only through $\lambda^{2}$, so it is constant on the cones $\lambda^{2}=\text{const}$.

*Proof.* The formula.

**The reading.** The spectrum of an element of the triplet is the pair $\pm3\lambda/2,\pm\lambda/2$, and the only parameter is the value of the invariant quadratic form.

## The Strata

**Proposition.** The spectral strata of the carrier are two: the semisimple cone $\lambda\neq0$, where the spectrum has the two distinct pairs, and the nilpotent cone $\lambda=0$, where the spectrum is $\{0,0,0,0\}$.

*Proof.* The spectrum depends on $\lambda^{2}$; for $\lambda\neq0$ the four eigenvalues are distinct unless $\lambda$ is such that $3\lambda/2=\pm\lambda/2$, which never happens.

**Corollary.** The nilpotent cone is the isotropic cone of the quadratic form, of complex dimension two, and its nonzero elements form a single orbit under the copy up to scaling.

*Proof.* The cone $a^{2}+b^{2}+c^{2}=0$ is two-dimensional and irreducible; the copy acts transitively on its nonzero points.

**Corollary.** The semisimple stratum is open and dense, and it is the union of the level sets of $\lambda^{2}$.

*Proof.* The complement of the isotropic cone is open and dense.

**The reading.** The triplet has the smallest possible number of spectral types: two, one open and one of codimension one.

## The Discriminant

**Proposition.** The discriminant of the characteristic polynomial is proportional to $\lambda^{6}$, so it vanishes exactly on the nilpotent cone, with multiplicity six.

*Proof.* The polynomial is $(\mu^{2}-9\lambda^{2}/4)(\mu^{2}-\lambda^{2}/4)$; the discriminant of a product of two quadratics with roots $\pm3\lambda/2$ and $\pm\lambda/2$ is the product of the squared differences, which is a constant times $\lambda^{6}$.

**Corollary.** The discriminant is not identically zero on the carrier, and it is not a square.

*Proof.* It is $\lambda^{6}$ up to a constant, and $\lambda$ is not a polynomial in $a,b,c$.

**Corollary.** The carrier's discriminant locus is the nilpotent cone, and the carrier meets the discriminant locus of the algebra exactly there.

*Proof.* The two statements.

**The reading.** The discriminant is the polynomial whose vanishing detects the collision of eigenvalues, and on the triplet the collision happens only in the nilpotent limit.

## The Other Carriers

**Proposition.** On $V_0$ the discriminant vanishes identically; on $V_1$ it vanishes on a cone of codimension one; on $V_2$ and $V_3$ it vanishes on a hypersurface that does not exhaust the carrier.

*Proof.* The scalars have repeated eigenvalues; the triplet's discriminant is $\lambda^{6}$; on the quintet and the septet the eigenvalues $\pm\alpha,\pm\beta$ are independent, so the discriminant vanishes when $\alpha=\pm\beta$ or $\alpha=0$ or $\beta=0$, which is a hypersurface.

**Corollary.** The carrier of label one is the first carrier whose discriminant is neither identically zero nor a proper hypersurface of the full dimension.

*Proof.* The comparison.

**Corollary.** The number of spectral types increases with the label: one type on $V_0$, two on $V_1$, and more on $V_2$ and $V_3$.

*Proof.* The multiplicities of the eigenvalues.

**The reading.** The triplet occupies the middle of the spectral scale: more rigid than the higher carriers and less degenerate than the scalars.

## The Boundary

**Against the trace form article.** That article gives the quadratic coefficient of the polynomial through the metric; this one gives the whole polynomial.

**Against the rank article.** The nilpotent cone is the union of the rank-three stratum and the origin.

**Against the biquaternion row.** At order two the carrier of label one is the adjoint of $\mathfrak{su}(2)$ and its spectrum is $\{0,\pm\mu\}$, a different pattern with the same two types.

## The Spectrum and the Metric

**The eigenvalues in terms of the form.** The trace form gives $q(X)=\operatorname{tr}(X^{2})=5(a^{2}+b^{2}+c^{2})=5\lambda^{2}$, so $\lambda=\sqrt{q/5}$ and the spectrum is $\{\pm\tfrac32\sqrt{q/5},\pm\tfrac12\sqrt{q/5}\}$. The metric determines the spectrum completely, and the ratio three is the only remaining datum.

**The nilpotent cone and the isotropic cone.** The cone $\lambda=0$ is the isotropic cone of the trace form, cut out by the single quadratic equation $q=0$ in a carrier of dimension three; the semisimple stratum is its complement.

**The comparison with the module.** The module has the weights $\pm\tfrac32,\pm\tfrac12$ under the same Cartan element, and the spectrum of the element $aJ_x+bJ_y+cJ_z$ on the module is what the eigenvalues above record: the triplet acts on the module through the same three generators, and the eigenvalues are the weights multiplied by the parameter.

**The reading.** On the triplet the metric and the spectrum are the same object, read at two levels: the invariant quadratic form gives the parameter, and the module gives the four eigenvalues.

## The Strata in the Projective Carrier

**The projective picture.** The carrier is a complex space of dimension three, and the semisimple stratum is the complement of a quadric cone; in the projective plane the cone is a conic, and the two strata are the interior and the exterior of the conic, distinguished by the sign of the invariant form.

**The real picture.** On the real form the conic is an ellipse, and the semisimple locus splits into two components on which the parameter $\lambda$ is real and of either sign; the nilpotent cone is the ellipse itself, and the origin is the only element with no projective class.

## The Note on Order Two

**The lower analogue.** At order two the triplet is the space of imaginary quaternions, and the copy acts on it by the adjoint representation; every nonzero element is semisimple, so the only spectral stratum below the origin is the whole space minus the origin, and the nilpotent cone is a single point.

**The comparison.** The reason is the dimension: in three dimensions the adjoint element $x$ has the eigenvalues $0,\pm i|x|$ with $|x|^{2}$ the invariant form, so one eigenvalue is always zero and the other two never are; the rank is two off the origin, and the finer stratification appears only at order four.

## The Check of the Ratio

**The two eigenvalues.** The ratio of the two nonzero eigenvalues is three at every point of the carrier, so the projective spectrum is constant and the only variable is the scale; the carrier therefore has a single projective spectral class.

## Summary

On the carrier of label one the characteristic polynomial is $\mu^{4}-(5\lambda^{2}/2)\mu^{2}+9\lambda^{4}/16$, with the spectrum $\pm3\lambda/2,\pm\lambda/2$. The spectral strata are the semisimple cone and the nilpotent cone, and the discriminant is proportional to $\lambda^{6}$, vanishing on the nilpotent cone with multiplicity six.

Among the four carriers the triplet is the first with a nondegenerate discriminant: the scalars have a vanishing discriminant, and the higher carriers have a discriminant hypersurface cut out by three conditions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\lambda^{2}=a^{2}+b^{2}+c^{2}$ | the invariant parameter |
| $\pm3\lambda/2,\pm\lambda/2$ | the spectrum |
| $\lambda^{6}$ | the discriminant up to a constant |
| $\lambda=0$ | the nilpotent cone |

## Further Reading

- [The Spin-One Carrier of $M_4(\mathbb{C})$: the Adjoint Triplet](the-spin-one-carrier-of-m4c.html), for the carrier.
- [The Spin-One Carrier and the Trace Form at $n=4$](the-spin-one-carrier-and-the-trace-form-at-n-4.html), for the metric.
- [The Spin-One Carrier and the Rank Strata at $n=4$](the-spin-one-carrier-and-the-rank-strata-at-n-4.html), for the rank.
- [The Spin-One Carrier and the Spectral Strata](the-spin-one-carrier-and-the-spectral-strata.html), for the row at order two.
- [The Spin-Zero Carrier and the Spectral Strata at $n=4$](the-spin-zero-carrier-and-the-spectral-strata-at-n-4.html), for the comparison.
