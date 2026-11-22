# __The Spin-Two Carrier and the Trace Form at $n=4$__

## Introduction

**The subject.** On the carrier of label two the trace form is nondegenerate, invariant and hyperbolic: in the weight basis the two pairs of opposite weights pair among themselves and the weight-zero vector stands alone with a positive square. The article computes the Gram matrix, the signature and the trace of the form.

**The order of the article.** The first section fixes the invariance and the nondegeneracy. The second computes the Gram matrix in the weight basis. The third computes the signatures. The fourth reads the form through the characteristic polynomial. The fifth draws the boundary.

**It assumes** *Introduction to the Spin-Two Carrier at $n=4$: the Alternating Square* and *The Spin-One Carrier and the Trace Form at $n=4$*. The row at order two has no carrier of label two.

**The result in one line.** In the weight basis the trace form on $V_2$ has the pairings $\langle w_2,w_{-2}\rangle=2$, $\langle w_1,w_{-1}\rangle=2$, $\langle w_0,w_0\rangle=1$ and all other products zero, so in that basis the Gram matrix has three positive and two negative eigenvalues, and the real signature of the form is $(5,5)$.

**Boundaries.** The article treats the bilinear trace form; the Hermitian form is treated in the article on the septet, where it is positive definite.

## Invariance and Nondegeneracy

**Proposition.** The trace form restricts to $V_2$ as a nondegenerate invariant symmetric form, and it is the unique such form up to a scalar.

*Proof.* The trace form is invariant, and its restriction to an irreducible summand is nondegenerate since the radical would be an invariant subspace; the space of invariant bilinear forms on an irreducible module is one-dimensional.

**Corollary.** The carrier is its own dual through the form, so $V_2\cong V_2^{*}$.

*Proof.* A nondegenerate bilinear form gives an isomorphism with the dual.

**Corollary.** The orthogonal complement of $V_2$ is $V_3\oplus V_1\oplus V_0$, and distinct carriers are mutually orthogonal.

*Proof.* Distinct isotypic components are orthogonal for an invariant form.

**The reading.** The quintet is self-dual, and the form is the only invariant bilinear pairing it carries.

## The Gram Matrix

**Proposition.** In the weight basis $w_2,w_1,w_0,w_{-1},w_{-2}$ with $w_2=E_{02}+E_{13}$, $w_1=E_{01}-E_{23}$, $w_{-1}=E_{10}-E_{32}$, $w_{-2}=E_{20}+E_{31}$ and $w_0=\tfrac12\operatorname{diag}(1,-1,-1,1)$, the only nonzero pairings are $\langle w_2,w_{-2}\rangle=\langle w_{-2},w_2\rangle=2$, $\langle w_1,w_{-1}\rangle=\langle w_{-1},w_1\rangle=2$ and $\langle w_0,w_0\rangle=1$.

*Proof.* The pairing is $\langle X,Y\rangle=\operatorname{tr}(XY)$, computed on products of matrix units; a weight-$m$ vector pairs only with a weight-$(-m)$ vector, and the direct computation gives $\operatorname{tr}((E_{02}+E_{13})(E_{20}+E_{31}))=1+1=2$, the same value for the weight-one pair, and $\operatorname{tr}(w_0^{2})=\tfrac14\cdot4=1$.

**Corollary.** The positive-weight and negative-weight vectors are isotropic, and only the weight-zero vector has a nonzero square.

*Proof.* $\operatorname{tr}((E_{02}+E_{13})^{2})=0$, since the product of the two matrix units vanishes and each square vanishes.

**Corollary.** The Gram matrix is the direct sum of two hyperbolic planes and the block $(1)$, so its determinant is $-16$ in this basis.

*Proof.* The hyperbolic plane has Gram matrix with zero diagonal and off-diagonal entries two, of determinant $-4$; two planes and the unit block give $-16$.

**The reading.** The form is hyperbolic on the pairs of opposite weights and positive on the weight-zero direction: the quintet is a space of Lorentz type in five dimensions.

## The Signatures

**Proposition.** In the weight basis the Gram matrix of the form has three positive and two negative eigenvalues, and the real signature of the form is $(5,5)$.

*Proof.* Diagonalising the Gram matrix gives two blocks of type $(+,-)$ and one positive direction, so three positive and two negative entries in that basis; the Hermitian slice is five-real-dimensional, the form is positive definite on it because $\operatorname{tr}(H^{2})=\sum_{ij}|H_{ij}|^{2}$ for Hermitian $H$, and negative definite on its multiple by $i$, which gives five plus and five minus real directions.

**Corollary.** The form is positive definite on the Hermitian slice and the slice is a real Euclidean space of dimension five.

*Proof.* The proposition.

**Corollary.** The isotropic cone of the form is the cone of the nilpotent elements.

*Proof.* The spectrum is $\{\pm s,\pm s\}$ with $s^{2}=q/4$, so $q=0$ forces every eigenvalue to vanish.

**The reading.** The form is indefinite with neutral real signature, and its isotropic cone is exactly the set of rank-two elements.

## The Form and the Spectrum

**Proposition.** For $X\in V_2$ the characteristic polynomial is $(\lambda^{2}-q(X)/4)^{2}$ with $q(X)=\operatorname{tr}(X^{2})$, so the spectrum is $\{\pm s,\pm s\}$ with $s^{2}=q/4$.

*Proof.* The determinant is $q^{2}/16$ and the spectrum is symmetric because the trace and the cube trace vanish; the resulting polynomial $\lambda^{4}-(q/2)\lambda^{2}+q^{2}/16$ is the square of $\lambda^{2}-q/4$, verified numerically on random elements.

**Corollary.** The second and fourth elementary symmetric functions of the spectrum are $q/2$ and $q^{2}/16$.

*Proof.* The expansion of the square.

**Corollary.** The form determines the spectrum up to the sign of $s$, and the carrier has no other spectral invariant.

*Proof.* The characteristic polynomial is a function of $q$ alone.

**The reading.** On the quintet the trace form is not merely a metric: it is the whole spectrum.

## The Boundary

**Against the carrier introduction.** That article identifies the carrier and its weights; this one computes the metric.

**Against the rank article.** The isotropic cone is the rank-two stratum, and the form is the polynomial that cuts it out.

**Against the triplet.** The form on $V_1$ is positive definite in the generator basis, while the form on $V_2$ is hyperbolic.

## A Final Observation

**The weight spaces and orthogonality.** The weight spaces of opposite weights are dual to each other through the form, and the weight-zero space is orthogonal to all of them; this is the statement that the form is hyperbolic on the two pairs and positive on the middle direction, and it is read directly from the weight string.

**The normalisation.** The value two on the extreme pair is the trace of the square of the sum of two matrix units, and the value one on the middle vector is the trace of the square of the traceless diagonal element; both are computed without any choice of scale, so the Gram matrix is canonical.

## The Form and the Hodge Star

**The Hodge star.** On the alternating square the Hodge star is the operator that sends the two-form with the index pair to the complementary pair, and on the six-dimensional square it satisfies the relation of a complex structure; the trace form is the pairing with the star, and the two extreme weight vectors are interchanged by it.

**The middle direction.** The weight-zero element of the carrier is traceless and diagonal, and its square is a multiple of the unit; the trace form takes the value one on it, and it is the unique direction on which the form is positive in the weight basis.

**The signature.** Two hyperbolic pairs and one positive direction give the real signature $(5,5)$ for the complex carrier of dimension five, and the form is nondegenerate with the isotropic cone the nilpotent stratum.

**The reading.** The trace form on the quintet is the Hodge pairing of the alternating square, and its signature records the two hyperbolic pairs and the one positive middle direction.

## The Check of the Values

**On the weight vectors.** The form takes the value two on the pair of extreme vectors and the value one on the middle vector, and it vanishes on every other pair; the three numbers are the whole Gram matrix, and their signs are two positive and one positive with the hyperbolic pairing.

## Summary

The trace form on the carrier of label two is nondegenerate, invariant and unique up to a scalar. In the weight basis the two pairs of opposite weights pair with value two and the weight-zero vector has square one, so the Gram matrix in that basis has three positive and two negative eigenvalues and the real signature $(5,5)$; the form is positive definite on the Hermitian slice.

The characteristic polynomial on the carrier is the square $(\lambda^{2}-q/4)^{2}$, so the spectrum depends only on the value of the form and the isotropic cone is the cone of the nilpotent elements.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $w_2=E_{02}+E_{13}$ | the highest weight vector |
| $w_0=\tfrac12\operatorname{diag}(1,-1,-1,1)$ | the weight-zero vector |
| $(3,2)$, $(5,5)$ | the complex and real signatures |
| $(\lambda^{2}-q/4)^{2}$ | the characteristic polynomial |

## Further Reading

- [Introduction to the Spin-Two Carrier at $n=4$: the Alternating Square](the-spin-two-carrier-of-m4c.html), for the carrier.
- [The Spin-Two Carrier and the Rank Strata at $n=4$](the-spin-two-carrier-and-the-rank-strata-at-n-4.html), for the isotropic cone.
- [The Spin-Three Carrier and the Hermitian Form at $n=4$](the-spin-three-carrier-and-the-hermitian-form-at-n-4.html), for the positive-definite Hermitian form.
- [The Spin-One Carrier and the Trace Form at $n=4$](the-spin-one-carrier-and-the-trace-form-at-n-4.html), for the comparison.
- [The Spin-Zero Carrier and the Determinant at $n=4$](the-spin-zero-carrier-and-the-determinant-at-n-4.html), for the scalar carrier.
