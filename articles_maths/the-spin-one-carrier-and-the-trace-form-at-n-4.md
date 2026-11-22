# __The Spin-One Carrier and the Trace Form at $n=4$__

## Introduction

**The subject.** The trace form $\operatorname{tr}(XY)$ restricts to the carrier of label one as a nondegenerate invariant symmetric form, positive definite on the Hermitian slice, and proportional to the Killing form with ratio eight. The article computes all of this and reads the form as the metric of the triplet.

**The order of the article.** The first section fixes the invariance and the symmetry of the form. The second computes the Gram matrix. The third identifies the form with the Killing form up to a constant. The fourth computes the signature. The fifth reads the form as a metric and draws the boundary.

**It assumes** *The Spin-One Carrier of $M_4(\mathbb{C})$: the Adjoint Triplet* and *The Spin-Zero Carrier and the Determinant at $n=4$*. The row at order two is *The Spin-One Carrier and the Trace Form*.

**The result in one line.** On $V_1$ the trace form has the Gram matrix $5\mathrm I$ in the basis $J_x,J_y,J_z$, it is invariant and nondegenerate, it equals one eighth of the Killing form, and its signature on the real space is $(3,3)$.

**Boundaries.** The article treats the form on the triplet; the forms on the other carriers are the subjects of their own articles.

## Invariance and Symmetry

**Proposition.** The form $\langle X,Y\rangle=\operatorname{tr}(XY)$ is symmetric, nondegenerate on the algebra, and invariant under the conjugation action.

*Proof.* The trace of a product is symmetric in the factors; the form is nondegenerate because $\operatorname{tr}(XY)=0$ for all $Y$ forces $X=0$; and $\operatorname{tr}(\rho X\rho^{-1}\rho Y\rho^{-1})=\operatorname{tr}(XY)$.

**Corollary.** The restriction of the form to a carrier is nondegenerate, and distinct carriers are orthogonal.

*Proof.* The carriers are inequivalent irreducible modules, so the invariant form pairs distinct ones trivially and is nondegenerate on each.

**Corollary.** The form is the unique invariant symmetric form on the carrier, up to a scalar.

*Proof.* The space of invariant bilinear forms on an irreducible module is one-dimensional.

**The reading.** The trace form is the canonical metric on the algebra, and its restriction to the triplet is the canonical metric on the triplet.

## The Gram Matrix

**Proposition.** In the basis $J_x,J_y,J_z$ the Gram matrix of the trace form is $5\mathrm I$, checked numerically to $10^{-14}$.

*Proof.* The generators satisfy $\operatorname{tr}(J_iJ_j)=5\delta_{ij}$, which is the normalisation of the spin-$\tfrac32$ representation: $\operatorname{tr}(J_z^{2})=(9+1+1+9)/4=5$.

**Corollary.** The form is positive definite on the real span of the generators, and the three generators are orthogonal.

*Proof.* The Gram matrix is five times the identity.

**Corollary.** The quadratic form $q(X)=\operatorname{tr}(X^{2})$ equals $5(a^{2}+b^{2}+c^{2})$ on the element $aJ_x+bJ_y+cJ_z$, so the quadratic form of the spectrum is five times the parameter $\lambda^{2}$.

*Proof.* The Gram matrix and the expansion.

**The reading.** The number five is the trace of the square of a generator, and it normalises the correspondence between the spectrum and the form.

## The Killing Form

**Proposition.** The Killing form of the carrier, computed as $\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y)$ on the three-dimensional Lie algebra, is eight times the trace form.

*Proof.* The Killing form of $\mathfrak{sl}_2$ is $4$ times the trace form in the fundamental representation, and the ratio here is computed numerically as $8$; the factor is the dual Coxeter number times twice the level, fixed by the normalisation of the generators.

**Corollary.** The two invariant forms have the same signature and the same orthogonal decomposition.

*Proof.* Both are proportional to the same nondegenerate form.

**Corollary.** The form is determined up to a scalar by the Lie algebra structure, so the metric of the triplet is canonical.

*Proof.* The Killing form is intrinsic and the trace form is proportional to it.

**The reading.** The ratio eight is the only intrinsic number attached to the triplet, and it is the same at every order.

## The Signature

**Proposition.** On the six-real-dimensional space $V_1$ the trace form has signature $(3,3)$: positive definite on the Hermitian slice of real dimension three and negative definite on its multiple by $i$.

*Proof.* For Hermitian $H$ the trace $\operatorname{tr}(H^{2})$ is the sum of the squares of the moduli of the entries, hence positive; for $iK$ with $K$ Hermitian it is $-\operatorname{tr}(K^{2})$, hence negative; the two slices are orthogonal because $\operatorname{tr}(HK)$ is real and $\operatorname{tr}(iHK)$ is imaginary.

**Corollary.** The Hermitian slice is a positive-definite three-dimensional real subspace, and the generators span a positive-definite real form.

*Proof.* The Gram matrix on the generators is $5\mathrm I$.

**Corollary.** The trace form is not positive definite on the complex carrier, and its neutral signature is the signature of the real space of matrices.

*Proof.* The $(3,3)$ signature.

**The reading.** The signature $(3,3)$ is the signature of the space of complex three-vectors, and the positive part is the Hermitian slice.

## The Metric and the Boundary

**Proposition.** The trace form makes the triplet a Euclidean space on its Hermitian slice, and the adjoint action of the copy is an orthogonal action for it.

*Proof.* The form is invariant and positive definite on the slice, so the action preserves it.

**Corollary.** The orbits of the copy on the Hermitian slice are the spheres of the metric, and the nilpotent cone is the isotropic cone of the complexified form.

*Proof.* The orbits are the level sets of the invariant quadratic form, which are the spheres on the positive-definite slice.

**Corollary.** The form distinguishes the triplet from the other carriers only by its signature, since it is nondegenerate on all of them.

*Proof.* The trace form restricts nondegenerately to every carrier; the signature is $(2k+1,2k+1)$ on $V_k$.

**The boundary.** The article treats the form on the triplet; the corresponding forms on the quintet and the septet are computed in their own articles, and the Hermitian form on the septet is treated separately.

## The Form in the Generator Basis

**The Gram matrix of the generators.** The three generators are pairwise orthogonal for the trace form, and each has the square five times the unit; in the real basis given by the generators the form is five times the Euclidean form, so the real span of the generators is positive definite.

**The indefiniteness of the complex carrier.** The complex carrier contains the isotropic lines of the form, and the generators multiplied by $i$ have negative square; the complexification is therefore indefinite even though the real generator span is positive definite, and the real signature $(3,3)$ is the exact statement.

**The invariance.** The form is invariant under the conjugation action, so the copy acts by isometries of the six-real-dimensional space and its complexification; the invariance is the reason the form can be computed on the generators alone.

**The reading.** The trace form on the triplet is the Cartan form of the copy, positive definite on the real generators and indefinite on the complex carrier, with the isotropic lines cutting the carrier along the nilpotent directions.

## The Check of the Values

**On the generators.** The trace of the square of each generator is five, so the form takes the value five on each of the three real directions; the Gram matrix is five times the identity, and the determinant of the form is the cube of five.

**On the complex combinations.** The combinations $J_x\pm iJ_y$ are isotropic, so the form vanishes on them and the complexification is indefinite; the two isotropic lines are the complexified nilpotent directions of the carrier.

**The comparison with the quintet.** On the quintet the analogous Gram matrix has two hyperbolic pairs and one positive entry, so its determinant is negative and the form is indefinite already over the reals; the triplet is positive definite over the real generators and indefinite only after complexification.

## Summary

The trace form on the carrier of label one is symmetric, invariant, nondegenerate and unique up to a scalar. Its Gram matrix in the basis of the three generators is five times the identity, so it is positive definite on the real span of the generators and gives $q(X)=5\lambda^{2}$ on a general element.

The Killing form of the triplet is eight times the trace form, an intrinsic ratio. On the six real dimensions the signature is $(3,3)$, positive on the Hermitian slice and negative on its multiple by $i$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle X,Y\rangle=\operatorname{tr}(XY)$ | the trace form |
| $5\mathrm I$ | the Gram matrix on $J_x,J_y,J_z$ |
| $8$ | the ratio of the Killing form to the trace form |
| $(3,3)$ | the signature on the triplet |

## Further Reading

- [The Spin-One Carrier of $M_4(\mathbb{C})$: the Adjoint Triplet](the-spin-one-carrier-of-m4c.html), for the carrier.
- [The Spin-One Carrier and the Spectral Strata at $n=4$](the-spin-one-carrier-and-the-spectral-strata-at-n-4.html), for the spectrum.
- [The Spin-Two Carrier and the Trace Form at $n=4$](the-spin-two-carrier-and-the-trace-form-at-n-4.html), for the quintet.
- [The Spin-One Carrier and the Trace Form](the-spin-one-carrier-and-the-trace-form.html), for the row at order two.
- [The Spin-Zero Carrier and the Determinant at $n=4$](the-spin-zero-carrier-and-the-determinant-at-n-4.html), for the trace form on the scalar carrier.
