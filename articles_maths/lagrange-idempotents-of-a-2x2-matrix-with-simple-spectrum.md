# __Lagrange Idempotents of a $2\times2$ Matrix with Simple Spectrum__

## Introduction

**A two-by-two matrix with two distinct eigenvalues has exactly two Lagrange idempotents $\rho_{\pm}$, each of rank one and trace one, and they reconstruct the matrix as $\lambda_{+}\rho_{+}+\lambda_{-}\rho_{-}$.**

The article defines the idempotents by interpolation at the two eigenvalues, proves the four identities that characterise them, exhibits the involution $\rho_{+}-\rho_{-}$ as the normalised shift of the matrix, writes the idempotents in the trace and the determinant through the discriminant, and identifies them with the spectral projectors of the resolvent. It assumes *The Elementary Symmetric Functions: $\operatorname{tr}$ and $\det$ in Dimension Two* and *The Minimal Polynomial and the Two Jordan Regimes of $M_2(\mathbb{C})$*, and it defers the general spectral theory to *The Spectrum of a $2\times2$ Matrix*.

On the biquaternion side the same pair is $\tilde\Pi_{\pm}=\tfrac12(e_t\pm\tilde{Ζ})$ in *The Square Roots of One and the Idempotents of the Biquaternion Algebra* and *The Peirce Basis of the Biquaternion Algebra*, and the translation is the one of *$M_2(\mathbb{C})$ Pauli Representation*.

## The Interpolation Problem

**The Lagrange problem asks for a polynomial of degree one taking prescribed values at two points.** For two distinct numbers $\lambda_{+}$ and $\lambda_{-}$ there are exactly two such polynomials for the two values $1$ and $0$.

**Proposition.** The polynomials are $\ell_{+}(z)=\dfrac{z-\lambda_{-}}{\lambda_{+}-\lambda_{-}}$ and $\ell_{-}(z)=\dfrac{z-\lambda_{+}}{\lambda_{-}-\lambda_{+}}$.

**Proof.** Each is of degree one, $\ell_{+}(\lambda_{+})=1$ and $\ell_{+}(\lambda_{-})=0$, and the two conditions determine a polynomial of degree one uniquely.

**Corollary.** For every $z$ one has $\ell_{+}(z)+\ell_{-}(z)=1$ and $\ell_{+}(z)\ell_{-}(z)=0$ exactly at $z=\lambda_{\pm}$.

**Proof.** The two numerators add to $\lambda_{+}-\lambda_{-}$ up to the denominator, and the product vanishes at the two nodes.

**Definition.** The **Lagrange idempotents** of a matrix $X$ with simple spectrum are $\rho_{\pm}=\ell_{\pm}(X)$.

**Corollary.** The idempotents are polynomials of degree one in $X$, so they commute with $X$ and with every matrix that commutes with $X$.

**Proof.** A polynomial in $X$ commutes with $X$, and it commutes with everything in the centraliser of $X$.

## The Four Identities

**Theorem.** For a matrix with two distinct eigenvalues the Lagrange idempotents satisfy

$$
\rho_{+}+\rho_{-}=I,\qquad \rho_{+}\rho_{-}=0,\qquad \rho_{\pm}^{2}=\rho_{\pm},\qquad X=\lambda_{+}\rho_{+}+\lambda_{-}\rho_{-}.
$$

**Proof.** The first two follow from the two scalar identities of interpolation applied to $X$; the third follows from the second and the first; the fourth is the interpolation of the identity function $z\mapsto z$, which is of degree one and takes the values $\lambda_{\pm}$ at the two nodes.

**Corollary.** Each idempotent has rank one, trace one and determinant zero.

**Proof.** The trace is additive and $\operatorname{tr}(I)=2$, so $\operatorname{tr}\rho_{+}+\operatorname{tr}\rho_{-}=2$; the products $X\rho_{\pm}=\lambda_{\pm}\rho_{\pm}$ show that the image of $\rho_{\pm}$ lies in the eigenspace of $\lambda_{\pm}$, which is one-dimensional; hence the rank is one and the trace is the rank.

**Corollary.** $X\rho_{\pm}=\lambda_{\pm}\rho_{\pm}$ and $\rho_{\pm}X=\lambda_{\pm}\rho_{\pm}$, so the columns of $\rho_{+}$ are eigenvectors of $\lambda_{+}$ and its rows are left eigenvectors.

**Proof.** Multiply the reconstruction identity by $\rho_{\pm}$ and use orthogonality and idempotence.

**Corollary.** The pair is unique: any two idempotents summing to the identity and satisfying the reconstruction identity are the Lagrange ones.

**Proof.** The reconstruction identity forces $X\rho_{\pm}=\lambda_{\pm}\rho_{\pm}$, and an idempotent with a one-dimensional image spanned by an eigenvector is determined by that eigenvector.

## The Involution of the Pair

**Theorem.** The difference $\zeta=\rho_{+}-\rho_{-}$ is an involution: $\zeta^{2}=I$, and $\rho_{\pm}=\tfrac12(I\pm\zeta)$.

**Proof.** Expand $\zeta^{2}=\rho_{+}+\rho_{-}$ using orthogonality and idempotence, which gives $I$; the second formula is the sum and the difference of the two.

**Corollary.** In terms of the matrix, $\zeta=\dfrac{2X-(\operatorname{tr}X)I}{\sqrt{\Delta}}$ with $\Delta=(\operatorname{tr}X)^{2}-4\det X$ and the sign of the square root fixed by $\lambda_{+}-\lambda_{-}$.

**Proof.** Adding the two formulas $\rho_{\pm}=\pm\dfrac{X-\lambda_{\mp}I}{\lambda_{+}-\lambda_{-}}$ gives $\zeta=\dfrac{2X-(\lambda_{+}+\lambda_{-})I}{\lambda_{+}-\lambda_{-}}$, and the denominator is the square root of the discriminant.

**Corollary.** The involution $\zeta$ has trace zero and determinant $-1$, and it is the normalised traceless part of the matrix.

**Proof.** $\operatorname{tr}\zeta=\operatorname{tr}\rho_{+}-\operatorname{tr}\rho_{-}=1-1=0$; an involution with trace zero has the eigenvalues $\pm1$, so its determinant is $-1$.

**The involution separates the two eigenvalues without diagonalising.** The matrix is recovered as $X=\tfrac12(\operatorname{tr}X)I+\tfrac12\sqrt{\Delta}\,\zeta$, which is the spectral decomposition written in the basis of the identity and the involution.

**Proof.** Substitute $\rho_{\pm}=\tfrac12(I\pm\zeta)$ into the reconstruction identity and collect the two terms.

## The Coordinates in Trace and Determinant

**Proposition.** With $t=\operatorname{tr}X$ and $\delta=\det X$ the eigenvalues are the roots of $z^{2}-tz+\delta$, namely $\lambda_{\pm}=\tfrac12\bigl(t\pm\sqrt{t^{2}-4\delta}\bigr)$.

**Proof.** The characteristic polynomial is $z^{2}-tz+\delta$ by *The Elementary Symmetric Functions: $\operatorname{tr}$ and $\det$ in Dimension Two*, and the quadratic formula gives the two roots.

**Corollary.** The idempotents are

$$
\rho_{\pm}=\frac{X-\lambda_{\mp}I}{\lambda_{+}-\lambda_{-}}=\pm\frac{2X-tI\mp\sqrt{\Delta}\,I}{2\sqrt{\Delta}}.
$$

**Proof.** Substitute the roots into the definition and clear the denominators.

**Corollary.** The idempotents are rational functions of $X$ with the discriminant in the denominator, so they are defined exactly where the spectrum is simple.

**Proof.** The square root appears only through $\sqrt{\Delta}$, which divides, and the denominator vanishes exactly when the two eigenvalues coincide.

## Simple Spectrum and the Discriminant

**Theorem.** The spectrum is simple exactly when the discriminant $\Delta=t^{2}-4\delta$ is nonzero, and then the two idempotents exist and are distinct.

**Proof.** The eigenvalues coincide exactly when the square root vanishes, which is the vanishing of the discriminant; and the two idempotents differ by the involution, which is nonzero when the eigenvalues differ.

**Corollary.** At $\Delta=0$ the two formulas degenerate, and the pair is replaced by the Jordan regime of *The Minimal Polynomial and the Two Jordan Regimes of $M_2(\mathbb{C})$*.

**Proof.** The denominator of both idempotents is $\sqrt{\Delta}$, which vanishes at the double eigenvalue, while the matrix still has a single eigenvalue and possibly a nontrivial Jordan block.

**Corollary.** The discriminant is the square of the difference of the eigenvalues, so it is the invariant that measures the distance from the diagonalisable case.

**Proof.** $(\lambda_{+}-\lambda_{-})^{2}=(\lambda_{+}+\lambda_{-})^{2}-4\lambda_{+}\lambda_{-}=t^{2}-4\delta$.

## The Spectral Projectors

**Proposition.** The idempotents are the residues of the resolvent: $\rho_{\pm}=\dfrac{1}{2\pi i}\oint_{\gamma_{\pm}}(zI-X)^{-1}\,dz$ around a small circle enclosing $\lambda_{\pm}$ alone.

**Proof.** The spectral decomposition writes $zI-X=(z-\lambda_{+})\rho_{+}+(z-\lambda_{-})\rho_{-}$ with orthogonal idempotents, so the inverse is $\dfrac{\rho_{+}}{z-\lambda_{+}}+\dfrac{\rho_{-}}{z-\lambda_{-}}$; the residue at $\lambda_{+}$ is $\rho_{+}$ and the residue at $\lambda_{-}$ is $\rho_{-}$.

**Corollary.** The inverse is a sum of two simple fractions, so the resolvent has two simple poles and no other singularity.

**Corollary.** The projection is the derivative of the reconstruction: $\rho_{+}=\dfrac{X-\lambda_{-}I}{\lambda_{+}-\lambda_{-}}$ is the Lagrange polynomial evaluated at the matrix, and the two readings agree.

**Proof.** Both are polynomials in $X$ taking the values $1$ and $0$ at the two eigenvalues, and such a polynomial of degree one is unique.

**Corollary.** The trace of $\rho_{+}X$ is $\lambda_{+}$, so the eigenvalue is read as a trace against the projector.

**Proof.** $\operatorname{tr}(\rho_{+}X)=\lambda_{+}\operatorname{tr}(\rho_{+})=\lambda_{+}$, since $\operatorname{tr}\rho_{+}=1$.

## The Corpus Translation

**Proposition.** Under the matrix model the pair $\rho_{\pm}$ is the pair $\tilde\Pi_{\pm}$, and the involution $\zeta$ is the root of one $\tilde{Ζ}$.

**Proof.** The corpus defines $\tilde\Pi_{\pm}=\tfrac12(e_t\pm\tilde{Ζ})$ with $\tilde{Ζ}^{2}=e_t$, which is the pair of identities proved above for $\rho_{\pm}$ and $\zeta$.

**Corollary.** The reconstruction $X=\tfrac12(\operatorname{tr}X)I+\tfrac12\sqrt{\Delta}\,\zeta$ is the corpus's polar form of the element in its root and its modulus.

**Proof.** The coefficient of the identity is the scalar part and the coefficient of the involution is the modulus, both read on the matrix side.

## Summary

A two-by-two matrix with two distinct eigenvalues has the Lagrange idempotents $\rho_{\pm}=\ell_{\pm}(X)$, the unique polynomials of degree one in $X$ taking the values $1$ and $0$ at the two eigenvalues. They satisfy $\rho_{+}+\rho_{-}=I$, $\rho_{+}\rho_{-}=0$, $\rho_{\pm}^{2}=\rho_{\pm}$ and $X=\lambda_{+}\rho_{+}+\lambda_{-}\rho_{-}$, each has rank one and trace one, and their difference is the involution $\zeta=(2X-tI)/\sqrt{\Delta}$ with $\rho_{\pm}=\tfrac12(I\pm\zeta)$.

The pair exists exactly where the discriminant $\Delta=t^{2}-4\delta$ is nonzero, and the same objects are the spectral projectors of the resolvent, the residues at the two poles. On the biquaternion side the pair is $\tilde\Pi_{\pm}$ and the involution is the root of one $\tilde{Ζ}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\lambda_{\pm}$ | the two eigenvalues |
| $\rho_{\pm}$ | the Lagrange idempotents |
| $\zeta$ | $\rho_{+}-\rho_{-}$, the involution |
| $t,\delta$ | the trace and the determinant |
| $\Delta$ | $t^{2}-4\delta$, the discriminant |
| $\ell_{\pm}$ | the interpolating polynomials of degree one |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the spectral projectors and the Lagrange interpolation of a matrix.
- Nicholas J. Higham, *Functions of Matrices* (SIAM, 2008), for the resolvent, the residues and the polynomial interpolation of matrix functions.
- [The Elementary Symmetric Functions: $\operatorname{tr}$ and $\det$ in Dimension Two](the-elementary-symmetric-functions-trace-and-determinant-in-dimension-two.html), for the characteristic polynomial and the discriminant.
- [The Minimal Polynomial and the Two Jordan Regimes of $M_2(\mathbb{C})$](the-minimal-polynomial-and-the-two-jordan-regimes-of-m2c.html), for the degenerate case of a double eigenvalue.
- [The Peirce Basis of the Biquaternion Algebra](the-peirce-basis-of-the-biquaternion-algebra.html), for the pair used as the frame of the Peirce decomposition.
