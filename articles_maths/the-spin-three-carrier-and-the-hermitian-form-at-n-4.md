# __The Spin-Three Carrier and the Hermitian Form at $n=4$__

## Introduction

**The subject.** The carrier of label three carries two forms of different kinds: the complex bilinear trace form, indefinite of real signature $(7,7)$, and the Hermitian form $\operatorname{tr}(XY^{\dagger})$, which is positive definite. The article computes both and explains why the integer label guarantees the existence of the invariant symmetric form and of an invariant real structure.

**The order of the article.** The first section defines the Hermitian form and proves its positivity. The second computes its Gram matrix. The third treats the real structure attached to the integer label. The fourth compares the two forms and reads the real signature. The fifth draws the boundary.

**It assumes** *Introduction to the Spin-Three Carrier at $n=4$: the Top of the Chain* and *The Frobenius–Schur Indicator of the Module at $n=4$*. The row at order two is *The Spin-Zero Carrier and the Hermitian Form*.

**The result in one line.** The Hermitian form $\operatorname{tr}(XY^{\dagger})$ is positive definite on the septet, of complex dimension seven; the bilinear trace form has real signature $(7,7)$; both are invariant, and the integer label is what makes the symmetric invariant bilinear form exist.

**Boundaries.** The article treats the forms on the septet; the corresponding forms on the quintet are treated in the article on its trace form.

## The Hermitian Form

**Proposition.** The form $\langle X,Y\rangle_{H}=\operatorname{tr}(XY^{\dagger})$ is Hermitian, positive definite on the algebra, and invariant under the conjugation action of the copy.

*Proof.* Linearity in the first argument and conjugate-linearity in the second follow from the trace; positivity follows from $\operatorname{tr}(XX^{\dagger})=\sum_{ij}|X_{ij}|^{2}$, which vanishes only for $X=0$; invariance follows from $\operatorname{tr}(\rho X\rho^{-1}(\rho Y\rho^{-1})^{\dagger})=\operatorname{tr}(XY^{\dagger})$ for unitary $\rho$.

**Corollary.** The restriction of the form to $V_3$ is positive definite, so the carrier is a Hilbert space of complex dimension seven.

*Proof.* A restriction of a positive definite form to a subspace is positive definite.

**Corollary.** The carriers are orthogonal for the Hermitian form as well, and each is a Hilbert summand of the algebra.

*Proof.* The isotypic components are orthogonal for any invariant form.

**The reading.** The septet carries a genuine Hilbert structure, unlike its bilinear trace form, which is indefinite.

## The Gram Matrix

**Proposition.** In the basis of the weight vectors the Hermitian Gram matrix is diagonal with positive entries, the entry of the highest weight vector $E_{03}$ being one.

*Proof.* The weight vectors pair only with themselves for the Hermitian form, because the form is antilinear in the second argument and the weights are opposite; $E_{03}$ is a matrix unit, so $\operatorname{tr}(E_{03}E_{03}^{\dagger})=1$.

**Corollary.** The Hermitian form is a positive-definite diagonal form in the weight basis, and its determinant is a positive real number.

*Proof.* The Gram matrix is diagonal with positive entries.

**Corollary.** The form is not the complexification of a real bilinear form on a real subspace of dimension seven.

*Proof.* A real bilinear form would give a symmetric complex bilinear form; the Hermitian form is conjugate-symmetric, not symmetric.

**The reading.** The Hermitian form is the Euclidean metric of the septet, and the weight basis diagonalises it.

## The Real Structure

**Proposition.** The label three being an integer, the Frobenius–Schur indicator of $V_3$ is $+1$: the carrier carries an invariant real structure $T$ with $T^{2}=+1$ and an invariant symmetric bilinear form, and the real form has dimension seven.

*Proof.* The indicator is $(-1)^{2j}=+1$ for the integer label; an invariant symmetric form and a real structure exist exactly in that case.

**Corollary.** The real form of the septet is the set of fixed points of $T$, of real dimension seven, and the trace form is real on it.

*Proof.* The fixed points of an anti-linear involution with $T^{2}=+1$ form a real form of half the real dimension, and the form takes real values there.

**Corollary.** The carrier is the real type carrier, in contrast with the module, which is quaternionic.

*Proof.* The indicator of the module is $(-1)^{3}=-1$, and that of the septet is $+1$.

**The reading.** The integer label is the reason the septet has a real form and an invariant symmetric form, while the module of half-integer label has neither.

## The Two Forms Compared

**Proposition.** The bilinear trace form on the septet is nondegenerate with real signature $(7,7)$, positive definite on the seven-real-dimensional Hermitian slice and negative definite on the slice multiplied by $i$, while the Hermitian form is positive definite on the whole carrier.

*Proof.* The Hermitian slice of the carrier is seven-real-dimensional and the trace form is positive definite there, being $\sum_{ij}|H_{ij}|^{2}$ for Hermitian $H$; on the slice multiplied by $i$ it is negative definite; the two slices are orthogonal and span the fourteen real dimensions.

**Corollary.** The two forms agree on the Hermitian slice and differ by the sign on the imaginary slice.

*Proof.* For Hermitian $H$ the two forms coincide, since $H^{\dagger}=H$; for $iH$ the trace form changes sign and the Hermitian form does not.

**Corollary.** The real form of the septet is a Euclidean space for the trace form, of dimension seven.

*Proof.* The trace form is positive definite on the Hermitian slice, which is a real form.

**The reading.** The septet is a Euclidean real space of dimension seven with a complexification of neutral signature, and the two forms encode the same positivity on the real slice.

## The Boundary

**Against the carrier introduction.** That article identifies the carrier and its weights; this one computes its two forms.

**Against the trace form of the quintet.** The quintet's trace form is hyperbolic, and its isotropic cone is the nilpotent cone; the septet's Hermitian form is positive definite.

**Against the module.** The module has no invariant symmetric form at all, so no Hermitian form of this kind is available on it.

## The Positivity and the Weight String

**The positivity in the weight basis.** The Hermitian form is diagonal in the weight basis with positive entries, so the weight vectors are orthogonal but not normalised; the normalisation of the highest weight vector is one, and the normalisations of the others are the squared norms of the matrix units.

**The real slice and the weight string.** On the Hermitian slice the trace form and the Hermitian form agree, and the weight string of the slice is the weight string of the carrier with the reality condition imposed; the seven real dimensions are spanned by the Hermitian combinations of the weight vectors and their partners.

## The Slice and the Estimates

**The size of the slice.** The Hermitian slice of the carrier has seven real dimensions, one for each weight of the carrier, and it is a real form of the complex carrier; the trace form and the Hermitian form agree on it and are positive definite there.

**The positivity estimate.** For a Hermitian element the trace of the square is the sum of the squares of the four real eigenvalues, hence non-negative, and it vanishes only at the origin; the Hermitian form is the sum of the squares of the sixteen real and imaginary parts of the entries, so the two positive forms differ only by the restriction.

**The comparison with the quintet.** On the quintet the Hermitian slice is five-real-dimensional and the trace form has the spectrum $\{\pm a,\pm a,0\}$, so it is degenerate there; on the septet no zero eigenvalue occurs, and the slice is strictly positive.

**The reading.** The positivity of the septet's two forms on its real slice is the sharpest difference between the top carrier and the quintet, whose real slice is isotropic along a line.

## Summary

The Hermitian form $\operatorname{tr}(XY^{\dagger})$ is positive definite and invariant on the septet, of complex dimension seven, with a diagonal Gram matrix in the weight basis and value one on the highest weight vector $E_{03}$.

The integer label gives the carrier a real structure and an invariant symmetric bilinear form; the trace form is nondegenerate of real signature $(7,7)$ and is positive definite on the seven-real-dimensional Hermitian slice.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{tr}(XY^{\dagger})$ | the Hermitian form |
| $T^{2}=+1$ | the real structure of the septet |
| $(7,7)$ | the real signature of the trace form |
| $7$ | the real dimension of the form |

## Further Reading

- [Introduction to the Spin-Three Carrier at $n=4$: the Top of the Chain](introduction-to-the-spin-three-carrier-of-m4c.html), for the carrier.
- [The Spin-Three Carrier and the Rank Strata at $n=4$](the-spin-three-carrier-and-the-rank-strata-at-n-4.html), for the ranks.
- [The Spin-Three Carrier and the Spectral Strata at $n=4$](the-spin-three-carrier-and-the-spectral-strata-at-n-4.html), for the spectra.
- [The Spin-Two Carrier and the Trace Form at $n=4$](the-spin-two-carrier-and-the-trace-form-at-n-4.html), for the comparison.
- [The Frobenius–Schur Indicator of the Module at $n=4$](the-frobenius-schur-indicator-of-the-module-at-n-4.html), for the indicator.
