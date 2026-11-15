# __The Spectrum of a $2\times2$ Matrix__

## Introduction

**The spectrum of a $2\times2$ matrix is the multiset of the two roots of $\lambda^{2}-t\lambda+\delta$, with $t$ the trace and $\delta$ the determinant, and it is a good invariant of the conjugacy class except at the double root.**

The article defines the spectrum, computes the roots from trace and determinant with the discriminant, describes the eigenspaces, shows by example that the spectrum does not determine the conjugacy class, proves the spectral mapping theorem for polynomials and for the inverse, records the reality properties of the eigenvalues for the two halves, and states the dependence of the eigenvalues on the entries. It assumes *The Element: Rank, Trace, Determinant, Characteristic Polynomial at $n=2$*, *The Minimal Polynomial and the Two Jordan Regimes of $M_2(\mathbb{C})$* and *The Elementary Symmetric Functions: $\operatorname{tr}$ and $\det$ in Dimension Two*.

It defers the diagonalisation and the projections to *Lagrange Idempotents of a $2\times2$ Matrix with Simple Spectrum*, and the two spectral theorems to *Normal $2\times2$ Matrices and the Common Spectral Theorem*.

## The Characteristic Polynomial

**Definition.** The **characteristic polynomial** of a matrix $X$ is

$$
\chi_{X}(\lambda)=\det(\lambda I-X)=\lambda^{2}-t\lambda+\delta,\qquad t=\operatorname{tr}X,\quad \delta=\det X .
$$

**Proposition.** The characteristic polynomial is invariant under conjugation, and its constant term is the determinant while the coefficient of $\lambda$ is minus the trace.

**Proof.** $\det(\lambda I-gXg^{-1})=\det(g(\lambda I-X)g^{-1})=\det(\lambda I-X)$; expanding the two-by-two determinant gives $\lambda^{2}-(\operatorname{tr}X)\lambda+\det X$.

**Corollary.** The spectrum depends only on the conjugacy class, so it is a conjugacy invariant.

**Proof.** The roots of the characteristic polynomial are determined by the polynomial, and the polynomial is invariant.

**Corollary.** The two coefficients are continuous functions of the entries, and so is the unordered pair of roots.

**Proof.** The trace and the determinant are polynomials in the entries, and the roots of a monic quadratic are continuous functions of its coefficients.

## The Two Roots and the Discriminant

**Definition.** The **discriminant** is $\Delta=t^{2}-4\delta$, and the two roots are

$$
\lambda_{\pm}=\frac{t\pm\sqrt{\Delta}}{2}.
$$

**Proposition.** The roots are distinct exactly when $\Delta\ne0$, they coincide exactly when $\Delta=0$, and their sum and product are $t$ and $\delta$.

**Proof.** The quadratic formula gives the roots; they coincide exactly when the square root vanishes; and the sum and the product are read from the coefficients by the elementary symmetric functions.

**Corollary.** The discriminant is itself a conjugacy invariant, and it is the square of the difference of the roots.

**Proof.** $\Delta=(\lambda_{+}-\lambda_{-})^{2}$, and both roots are conjugacy invariants.

**Corollary.** At the double root the matrix satisfies $(X-\lambda I)^{2}=0$, so it is either the scalar $\lambda I$ or a single Jordan block.

**Proof.** The characteristic polynomial is $(\lambda-\lambda_{0})^{2}$, and the minimal polynomial divides it and has the same root, so the minimal polynomial is $\lambda-\lambda_{0}$ or $(\lambda-\lambda_{0})^{2}$; the first case is the scalar and the second is the Jordan block.

## Eigenvectors and Eigenspaces

**Proposition.** For an eigenvalue $\lambda$ the eigenspace $\ker(\lambda I-X)$ is nonzero, it has dimension one when the two roots are distinct, and it has dimension two exactly when $X=\lambda I$.

**Proof.** The kernel is nonzero because the determinant vanishes; with distinct roots the matrix $\lambda I-X$ has rank one, so its kernel has dimension one; with a double root the kernel has dimension two exactly when the matrix is zero.

**Corollary.** With distinct roots the matrix is diagonalisable, with the two eigenspaces as the two coordinate lines of the diagonal form.

**Proof.** Two eigenvectors of distinct eigenvalues are independent, and two independent vectors form a basis in which the matrix is diagonal.

**Corollary.** At a double root the matrix is diagonalisable exactly when it is the scalar, so the spectrum plus the diagonalisability determines the class.

**Proof.** The scalar is diagonal in every basis, and a non-scalar with a double root has a one-dimensional eigenspace and hence a nontrivial Jordan block.

## The Spectrum Is Not a Complete Invariant

**Theorem.** The matrices $I$ and $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ have the same spectrum and are not conjugate.

**Proof.** Both characteristic polynomials are $(\lambda-1)^{2}$, so both spectra are $\{1,1\}$; and $J-I$ has rank one, so $J$ is not the scalar, while every conjugate of $I$ is $I$.

**Corollary.** The spectrum together with the rank of $X-\lambda I$ at the repeated eigenvalue is a complete invariant at order two, because it distinguishes the scalar from the Jordan block.

**Proof.** The rank of $X-\lambda I$ is zero at the scalar and one at the Jordan block, and with distinct roots the rank is one at each eigenvalue.

**Corollary.** The classification is: two distinct roots, one double root with $X$ scalar, one double root with $X$ not scalar.

**Proof.** The three cases are exhaustive because the characteristic polynomial has at most two distinct roots, and the double-root case splits on whether the matrix is the scalar.

## The Spectrum of Functions

**Theorem.** For a polynomial $p$ the spectrum of $p(X)$ is $p$ applied to the spectrum of $X$, and for an invertible $X$ the spectrum of $X^{-1}$ is the reciprocal of the spectrum.

**Proof.** If $Xv=\lambda v$ then $p(X)v=p(\lambda)v$ and $X^{-1}v=\lambda^{-1}v$; when the roots are distinct the two eigenvectors already give both eigenvalues of the image, counted with multiplicity.

**Corollary.** The determinant of $p(X)$ is $p(\lambda_{+})p(\lambda_{-})$, and the trace is the sum of the two values.

**Proof.** The trace and the determinant of a two-by-two matrix are the elementary symmetric functions of its spectrum.

**Corollary.** The spectral mapping holds for the exponential and for every power series that converges on the spectrum.

**Proof.** The polynomial case passes to the limit in the uniform topology on the spectrum, and the exponential is such a limit at order two.

## The Spectral Projections

**Proposition.** With distinct roots the two spectral projections are $\rho_{\pm}=\dfrac{X-\lambda_{\mp}I}{\lambda_{\pm}-\lambda_{\mp}}$, and they satisfy $\rho_{+}+\rho_{-}=I$, $\rho_{\pm}^{2}=\rho_{\pm}$ and $X=\lambda_{+}\rho_{+}+\lambda_{-}\rho_{-}$.

**Proof.** These are the Lagrange idempotents of *Lagrange Idempotents of a $2\times2$ Matrix with Simple Spectrum*, evaluated at the two nodes.

**Corollary.** The spectrum determines the matrix through the two projections, which are polynomials of degree one in the matrix.

**Proof.** The reconstruction writes the matrix as a combination of the identity and itself, with coefficients the two eigenvalues.

**Corollary.** The projections are continuous on the set of matrices with distinct roots and have no limit at the discriminant locus.

**Proof.** The denominators are the difference of the roots, which vanishes on the discriminant locus, while the numerators stay bounded.

## The Reality of the Spectrum

**Proposition.** The eigenvalues of a Hermitian matrix are real, those of a skew-Hermitian matrix are purely imaginary, and those of a unitary matrix have modulus one.

**Proof.** For a Hermitian $X$ and an eigenvector $v$ of norm one, $\lambda=v^{*}Xv$ is real because it equals its conjugate; for a skew-Hermitian $X$ the same computation gives $\lambda=-\bar\lambda$; and for a unitary $X$ it gives $|\lambda|^{2}=v^{*}X^{*}Xv=1$.

**Corollary.** A real symmetric $2\times2$ matrix has a real spectrum, and a real skew-symmetric $2\times2$ matrix has the spectrum $\{\mu i,-\mu i\}$ with $\mu$ real.

**Proof.** The real symmetric case is the Hermitian case, and the real skew-symmetric matrix is $c$ times the rotation by a right angle, whose square is $-c^{2}I$.

**Corollary.** A Hermitian matrix with the spectrum $\{1,1\}$ is the identity, and one with the spectrum $\{0,0\}$ is zero.

**Proof.** A Hermitian matrix is diagonalisable with real eigenvalues, so a double eigenvalue forces the scalar, and the scalar is fixed by the two values.

## Summary

The spectrum of a $2\times2$ matrix is the pair of roots of $\lambda^{2}-t\lambda+\delta$, with the discriminant $\Delta=t^{2}-4\delta$ deciding whether the roots are distinct. With distinct roots the matrix is diagonalisable with two one-dimensional eigenspaces; at a double root it is either the scalar or a single Jordan block.

The spectrum is a conjugacy invariant but not a complete one: the scalar and the Jordan block share the spectrum $\{1,1\}$. The spectrum of a polynomial or of the inverse is the polynomial or the reciprocal applied to the spectrum, the spectral projections reconstruct the matrix with distinct roots, and the two halves carry real, imaginary or unit-modulus spectra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $t,\delta$ | trace and determinant |
| $\chi_{X}$ | the characteristic polynomial |
| $\Delta$ | the discriminant $t^{2}-4\delta$ |
| $\lambda_{\pm}$ | the two eigenvalues |
| $\rho_{\pm}$ | the spectral projections |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the characteristic polynomial, the spectrum and the spectral mapping theorem.
- Sheldon Axler, *Linear Algebra Done Right* (Springer, 2015), for eigenvalues, eigenspaces and diagonalisability.
- [The Element: Rank, Trace, Determinant, Characteristic Polynomial at $n=2$](the-element-rank-trace-determinant-characteristic-polynomial-at-n-2.html), for the coefficients of the characteristic polynomial.
- [The Minimal Polynomial and the Two Jordan Regimes of $M_2(\mathbb{C})$](the-minimal-polynomial-and-the-two-jordan-regimes-of-m2c.html), for the two regimes at the double root.
- [Lagrange Idempotents of a $2\times2$ Matrix with Simple Spectrum](lagrange-idempotents-of-a-2x2-matrix-with-simple-spectrum.html), for the spectral projections.
