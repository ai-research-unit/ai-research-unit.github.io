# __The Peirce Decomposition and the Two Halves at $n=2$__

## Introduction

**At a symmetric rank-one idempotent the transpose fixes the two diagonal corners and exchanges the two mixed ones, so the symmetric half is the two diagonal lines together with the diagonal of the mixed block, of dimension three, and the antisymmetric half is the single off-diagonal of that block, of dimension one.**

The article computes the action of the transpose and of the conjugate transpose on the four Peirce spaces, writes the symmetric and the antisymmetric halves in Peirce coordinates, counts the dimensions in the two splittings, and compares the Peirce orthogonality with the orthogonality of the halves for the trace form. It assumes *The Peirce Decomposition in Two Dimensions*, *The Peirce Basis and the Corners at $n=2$*, *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$* and *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian at $n=2$*.

It defers the Hermitian idempotents and the sphere to *The Spectral Theorem: the Hermitian Case and the Sphere of Idempotents*, and the corner recursion to *The Peirce Decomposition and the Corner Recursion of $M_2(\mathbb{C})$*.

## The Transpose on the Corners

**Proposition.** At a symmetric idempotent $e$ the transpose fixes $A_{11}$ and $A_{00}$ and exchanges $A_{12}$ and $A_{21}$.

**Proof.** For $x\in A_{11}$ one has $x=\lambda e$, and $e^{\mathsf T}=e$ gives $\lambda e^{\mathsf T}=\lambda e$, so $x^{\mathsf T}\in A_{11}$; for $x=ey(1-e)$ the transpose is $(1-e)y^{\mathsf T}e$, which lies in $A_{21}$; and the same computation in the other order gives the exchange.

**Corollary.** The transpose acts on the four-dimensional space with the eigenvalues $+1$ on $A_{11}$, $A_{00}$ and on the diagonal of $A_{12}\oplus A_{21}$, and $-1$ on the off-diagonal of that block.

**Proof.** The exchange of two one-dimensional spaces has the two eigenvalues $\pm1$, with the eigenvectors the sum and the difference of a generator and its transpose, and the diagonal corners are fixed pointwise.

**Corollary.** The two eigenvectors in the mixed block are $E_{12}+E_{21}$ and $E_{12}-E_{21}$, the first symmetric and the second antisymmetric.

**Proof.** The transpose of $E_{12}$ is $E_{21}$, so the sum is fixed and the difference changes sign.

## The Symmetric Half in Peirce Coordinates

**Theorem.** The symmetric half is $A_{11}\oplus A_{00}\oplus(A_{12}\oplus A_{21})^{+}$, of dimension $1+1+1=3$.

**Proof.** A symmetric element has a symmetric part in each corner; the diagonal corners are one-dimensional and entirely symmetric; the mixed block splits into a symmetric line and an antisymmetric line; the sum of the dimensions is three, which is the dimension of the symmetric half.

**Corollary.** In Peirce coordinates a symmetric element is $x_{0}e+x_{1}f+t\,\varsigma$ with $\varsigma=E_{12}+E_{21}$, so it is determined by three numbers.

**Proof.** The mixed component of a symmetric element is a multiple of the symmetric generator, and the two diagonal components are multiples of $e$ and $f$.

**Corollary.** The antisymmetric half is the single line of $\varsigma'=E_{12}-E_{21}$, and its square is $-e-f$.

**Proof.** The antisymmetric part of the mixed block is one-dimensional; and $(E_{12}-E_{21})^{2}=-E_{11}-E_{22}$ by the multiplication of the matrix units.

**Corollary.** The Jordan Peirce space $V_{1}$ of *The Peirce Decomposition of $\operatorname{Sym}_2$ as a Jordan Algebra* is exactly the symmetric line of the mixed block.

**Proof.** The Jordan space $V_{1}$ is spanned by $\varsigma$, which is the symmetric generator of the mixed block.

## The Star and the Hermitian Case

**Proposition.** At a Hermitian idempotent $e$ the conjugate transpose exchanges $A_{12}$ and $A_{21}$ and fixes the two diagonal corners.

**Proof.** For $x=ey(1-e)$ the conjugate transpose is $(1-e)y^{*}e$, which lies in the corner with the indices exchanged; and $e^{*}=e$ makes the diagonal corners stable.

**Corollary.** The Hermitian half is the two diagonal lines together with the diagonal of the mixed block under the star, of real dimension four.

**Proof.** Each diagonal corner is a complex line all of whose elements are Hermitian up to a real scalar, and the mixed block contributes two real dimensions, one from the diagonal and one from the antidiagonal, which gives four real dimensions in total.

**Corollary.** The anti-Hermitian half is the complementary real space, of real dimension four, and the two halves are the eigenspaces of the star with the eigenvalues $+1$ and $-1$.

**Proof.** The star is an involution of the real space, so its eigenspaces have dimensions four and four and sum to eight.

## The Two Counts

**Proposition.** The Peirce splitting and the splitting into halves are transverse: the symmetric half is not a sum of Peirce spaces, and no mixed corner is contained in a half.

**Proof.** The symmetric half meets the mixed block in one of its two real lines, so it contains an element with a nonzero component in each mixed corner and is not a sum of Peirce spaces; and each mixed corner contains a symmetric and an antisymmetric element, so it is not contained in a half.

**Corollary.** The four counts are $1+1+1+1$ for the Peirce splitting, $3+1$ for the real halves, $4+4$ for the complex halves and $2+2$ for the two sides of the diagonal.

**Proof.** The Peirce splitting is over the complex field; the real halves are the symmetric and the antisymmetric; the complex halves are the Hermitian and the anti-Hermitian; and the two sides of the diagonal are the upper and the lower triangles.

**Corollary.** The only Peirce space that lies inside a half is a diagonal corner, and only in the symmetric or the Hermitian half.

**Proof.** The diagonal corner is a line of a symmetric matrix at a symmetric idempotent, and it is Hermitian at a Hermitian idempotent; the mixed corners are not stable under the transpose or the star.

## The Orthogonality of the Splittings

**Proposition.** The two halves are orthogonal for the trace form, and the four Peirce spaces are orthogonal except the two mixed ones.

**Proof.** The first statement is *The Two Halves as Orthogonal Complements at $n=2$*, and the second is *The Peirce Decomposition in Two Dimensions*.

**Corollary.** The two orthogonalities are different: the halves are orthogonal for the trace form, while the mixed Peirce spaces pair to one.

**Proof.** The trace of the product of a symmetric and an antisymmetric matrix vanishes, and the trace of $E_{12}E_{21}$ equals one.

**Corollary.** No Peirce splitting is orthogonal for the trace form, so the Peirce decomposition is not the spectral decomposition of a self-adjoint operator.

**Proof.** The single nonzero pairing between the two mixed spaces shows that they are not orthogonal, and an orthogonal decomposition into eigenspaces of a self-adjoint operator would have all the pairings zero.

## The Trace Form on the Corners

**Proposition.** The trace form pairs the diagonal corners with each other and the mixed corners with each other, and it is degenerate on each corner separately.

**Proof.** $\operatorname{tr}(ee)=1$ pairs $A_{11}$ with itself, $\operatorname{tr}(ef)=0$ kills the pairing of the two diagonal corners, and $\operatorname{tr}(E_{12}E_{21})=1$ pairs the two mixed corners; restricted to a single mixed corner the form vanishes because the corner is square-zero.

**Corollary.** The four-dimensional trace form is the sum of a two-dimensional form on the mixed block and a form on the diagonal pair, and the second is degenerate.

**Proof.** The mixed block carries the hyperbolic form with the two isotropic lines $A_{12}$ and $A_{21}$, and the diagonal pair carries the form $\operatorname{diag}(1,0)$ in the basis $e,f$.

## Summary

At a symmetric rank-one idempotent the transpose fixes the two diagonal corners and exchanges the two mixed ones, so the symmetric half is the two diagonal lines together with the symmetric line of the mixed block, of dimension three, and the antisymmetric half is the antisymmetric line of that block, of dimension one.

At a Hermitian idempotent the conjugate transpose does the same, and the Hermitian and anti-Hermitian halves have real dimension four each. The Peirce splitting and the splitting into halves are transverse, the halves are orthogonal for the trace form while the two mixed corners are not, and the trace form pairs the mixed corners with each other and is degenerate on the diagonal pair.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A_{ij}$ | the Peirce spaces |
| $\varsigma$ | $E_{12}+E_{21}$, the symmetric generator |
| $\varsigma'$ | $E_{12}-E_{21}$, the antisymmetric generator |
| $e,f$ | the idempotent and its complement |
| $x^{*}$ | the conjugate transpose |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce spaces and their behaviour under an involution.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the transpose and the conjugate transpose as involutions of the matrix space.
- [The Peirce Decomposition in Two Dimensions](the-peirce-decomposition-in-two-dimensions.html), for the four spaces used here.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$](the-two-halves-over-r-symmetric-and-antisymmetric-at-n-2.html), for the real halves.
- [The Peirce Decomposition of $\operatorname{Sym}_2$ as a Jordan Algebra](the-peirce-decomposition-of-sym-2-as-a-jordan-algebra.html), for the Jordan reading of the mixed block.
