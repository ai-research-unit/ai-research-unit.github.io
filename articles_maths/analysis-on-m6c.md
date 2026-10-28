# __Analysis on $M_6(\mathbb{C})$__

## Introduction

The algebra $M_6(\mathbb{C})$ is a complex vector space of dimension $36$, hence a real manifold of dimension $72$. It carries the smooth structure of $\mathbb{C}^{36}$, the complex structure of multiplication by $\mathrm i$, the Lebesgue measure of $\mathbb{R}^{72}$, and the norms of *The Forms, the Norms and the Singular Set of $M_6(\mathbb{C})$*. The analysis on $M_6$ is the ordinary analysis of a finite-dimensional complex vector space, enriched by the algebra structure: the product, the inverse, the determinant and the exponential are smooth, indeed holomorphic, maps, and their derivatives are the standard formulas.

The **Wirtinger calculus** gives the complex derivatives $\partial/\partial z_{ij}$ and $\partial/\partial\bar z_{ij}$. The holomorphic functions are those with $\partial f/\partial\bar z_{ij}=0$; the determinant is a holomorphic polynomial of degree six, the inverse is holomorphic on $GL_6$, and the exponential is entire. The **holomorphic functional calculus** evaluates a holomorphic function on a matrix through the resolvent and a contour integral,

$$
f(A)=\frac{1}{2\pi\mathrm i}\oint_\Gamma f(z)(zI_6-A)^{-1}\,dz,
$$

and the **Riesz projector**

$$
P=\frac{1}{2\pi\mathrm i}\oint_\Gamma(zI_6-A)^{-1}\,dz
$$

is the spectral projector onto the part of the spectrum inside $\Gamma$. The **Fourier transform** on $\mathbb{C}^{36}$ is the Euclidean Fourier transform of the $72$ real coordinates; the Schwartz space, the inversion theorem, the Plancherel theorem and the Gaussian are the standard ones.

The article also fixes the boundary against **Fueter theory**. The field $\mathbb{C}$ has no zero divisors; the algebra $M_6(\mathbb{C})$ does: the nilpotents satisfy $E_{12}^2=0$. The ordinary matrix analysis is the analysis over the field, with the spectrum, the resolvent and the functional calculus. Fueter theory is the quaternionic or Clifford analysis of the Cauchy–Fueter operator; it needs a different structure, a real division algebra or a Clifford module with a Dirac operator, and neither is the structure used here. The holomorphic functional calculus is not Fueter theory.

The article assumes the trace, the determinant, the norms, the Hermitian structure and the spectral theorem. It proves the derivative formulas, the Wirtinger rules, the resolvent and Riesz formulas, and it states the Fourier theorems with their standard proofs.

## The Smooth Structure

### The Real and Complex Manifolds

**Proposition.** $M_6(\mathbb{C})$ is a complex manifold of complex dimension $36$ and a real manifold of real dimension $72$. The complex structure is the linear map $J(A)=\mathrm iA$, with $J^2=-I$; the real tangent space at every point is $M_6$, and the complex tangent space is its complexification.

**Proof.** The identification $M_6\cong\mathbb{C}^{36}$ by the coordinates $A_{ij}$ is a complex-linear isomorphism; the real coordinates are the real and imaginary parts, $72$ in number. Multiplication by $\mathrm i$ is a real-linear map with $J^2=-I$. The tangent space of a vector space is the vector space itself.

**Corollary (the frame).** The manifold is parallelizable: the coordinate vector fields $\partial/\partial x_{ij}$ and $\partial/\partial y_{ij}$ are a global frame; the Wirtinger fields $\partial/\partial z_{ij}$ and $\partial/\partial\bar z_{ij}$ are a global frame of the complexified tangent bundle.

**Proof.** A vector space has a global basis of constant vector fields; the Wirtinger derivatives are the complex basis.

**Corollary (the measure).** The manifold is oriented, and

$$
dA=\prod_{i,j}dx_{ij}\,dy_{ij}
$$

is a translation-invariant volume form, the Lebesgue measure of $\mathbb{R}^{72}$.

**Proof.** The real coordinates give the standard orientation and the standard Lebesgue measure; translations are isometries.

### The Tangent Space

**Definition.** The **tangent space** $T_AM_6$ is $M_6$, with the derivative of a curve $A(t)$ at $t=0$ being $A'(0)$. The **differential** of a smooth map $F:M_6\to W$ at $A$ is the linear map $DF_A:M_6\to W$,

$$
DF_A(H)=\frac{d}{dt}\Big|_{0}F(A+tH).
$$

**Proposition.** The tangent space is $M_6$ at every point; the differential of a linear map is the map itself; the differential of the product is

$$
D(AB)_{(A,B)}(H,K)=HB+AK .
$$

**Proof.** The tangent space of a vector space is the vector space; the derivative of a linear map is itself; the product is bilinear, so the derivative is the sum of the two partial derivatives.

**Corollary (the multiplications).** The left multiplication $L_A(B)=AB$ has differential $DL_A(B)(K)=AK$; the right multiplication $R_B(A)=AB$ has differential $DR_B(A)(H)=HB$.

**Proof.** The product is linear in each factor.

### The Lebesgue Measure

**Definition.** The **Lebesgue measure** on $M_6$ is the translation-invariant measure $dA$ of $\mathbb{R}^{72}$.

**Proposition.** The measure is invariant under translations and under the $*$-unitary group: $d(UA)=dA$ and $d(AU)=dA$ for $U\in U(6)$. It is not invariant under general linear changes of coordinates; the Jacobian of $A\mapsto gA$ is $\lvert\det g\rvert^{12}$.

**Proof.** Translation invariance is the Lebesgue measure on $\mathbb{R}^{72}$; $*$-unitary invariance follows because $A\mapsto UA$ preserves the Frobenius norm. For a general $g$, left multiplication on $M_6$ has complex determinant $(\det g)^6$ (six column blocks, each with determinant $\det g$), so the real Jacobian is $\lvert(\det g)^6\rvert^2=\lvert\det g\rvert^{12}$.

**Corollary (the Gaussian).** The Gaussian integral converges:

$$
\int_{M_6}e^{-\operatorname{tr}(A^*A)}\,dA=\pi^{36}.
$$

**Proof.** The integrand is $\prod_{ij}e^{-\lvert A_{ij}\rvert^2}$; the integral over each complex coordinate is $\pi$; the product over the $36$ coordinates is $\pi^{36}$.

## The Derivatives

### The Product

**Proposition.** The product map $m(A,B)=AB$ is smooth (polynomial), and its differential is

$$
Dm_{(A,B)}(H,K)=HB+AK .
$$

**Proof.** The entries of $AB$ are polynomials of degree two; the derivative is the bilinear part $HB+AK$.

**Corollary.** The product is holomorphic in each variable separately; the algebra is a complex Lie algebra with the commutator.

**Proof.** The entries are polynomials in the entries of $A$ and $B$, hence holomorphic; the commutator is bilinear.

### The Inverse

**Theorem.** The inversion map $\operatorname{inv}:GL_6\to GL_6$, $A\mapsto A^{-1}$, is holomorphic, and its differential is

$$
D(\operatorname{inv})_A(H)=-A^{-1}HA^{-1}.
$$

**Proof.** For small $t$,

$$
(A+tH)^{-1}=A^{-1}-tA^{-1}HA^{-1}+O(t^2),
$$

by the Neumann series $(I+tA^{-1}H)^{-1}=I-tA^{-1}H+O(t^2)$; the derivative is the linear term.

**Corollary.** The inverse is a local diffeomorphism at every invertible $A$; its differential is invertible with inverse $K\mapsto-AKA$.

**Proof.** The differential $H\mapsto-A^{-1}HA^{-1}$ is invertible; the inverse function theorem applies.

### The Determinant

**Theorem.** The determinant is a holomorphic polynomial of degree six, and

$$
D\det_A(H)=\operatorname{tr}(\operatorname{adj}(A)H).
$$

At $A=I_6$, $D\det_{I_6}(H)=\operatorname{tr}H$.

**Proof.** Expand $\det(A+tH)$ in powers of $t$; the linear term is the sum over the positions of $H$ with the cofactor of $A$, which is the trace of the adjugate times $H$. At $A=I_6$, the adjugate is $I_6$.

**Corollary (the submersion).** The determinant is a submersion at every point of rank five; the singular set $\det=0$ is a complex hypersurface of real codimension two, smooth at the rank-five points.

**Proof.** The derivative is nonzero exactly when the adjugate is nonzero, that is at rank five; a nonzero complex-linear functional has kernel of real codimension two; the implicit function theorem gives the smooth hypersurface.

### The Exponential

**Theorem.** The exponential is entire, and its differential is

$$
D\exp_A(H)=e^A\sum_{m=0}^{\infty}\frac{(-1)^m}{(m+1)!}\operatorname{ad}_A^m(H).
$$

At $A=0$, $D\exp_0(H)=H$; for a scalar $A=\lambda I_6$, $D\exp_{\lambda I_6}(H)=e^\lambda H$.

**Proof.** Differentiate $e^{A+tH}$ at $t=0$. The derivative satisfies the differential equation $\frac{d}{dt}e^{A+tH}=e^{A+tH}H$ with the initial value $e^A$; the solution is $e^A$ times the series $\sum_m(-1)^m\operatorname{ad}_A^m(H)/(m+1)!$. At $A=0$ only the $m=0$ term survives; for a scalar, $\operatorname{ad}_A=0$.

**Corollary (the local inverse).** The differential at $0$ is the identity, so the exponential is a local diffeomorphism at $0$; the inverse branch is the logarithm.

**Proof.** $D\exp_0=I$ is invertible; the inverse function theorem gives the local inverse.

**Remark (the noncommutativity).** **The derivative of the exponential is not $e^AH$ unless $A$ is scalar or $H$ commutes with $A$.** The series with the adjoint corrects for the noncommutativity; the first correction is $\frac12[A,H]$. The formula is the analytic form of the Baker–Campbell–Hausdorff expansion.

## The Wirtinger Calculus

### The Complex Derivatives

**Definition.** For a smooth function $f:M_6\to\mathbb{C}$, the **Wirtinger derivatives** are

$$
\frac{\partial f}{\partial z_{ij}}=\frac12\left(\frac{\partial f}{\partial x_{ij}}-\mathrm i\frac{\partial f}{\partial y_{ij}}\right),
\qquad
\frac{\partial f}{\partial\bar z_{ij}}=\frac12\left(\frac{\partial f}{\partial x_{ij}}+\mathrm i\frac{\partial f}{\partial y_{ij}}\right).
$$

**Proposition.** The differential is

$$
df=\sum_{ij}\frac{\partial f}{\partial z_{ij}}dz_{ij}+\sum_{ij}\frac{\partial f}{\partial\bar z_{ij}}d\bar z_{ij},
$$

and the Wirtinger derivatives satisfy

$$
\overline{\frac{\partial f}{\partial z_{ij}}}=\frac{\partial\bar f}{\partial\bar z_{ij}}.
$$

**Proof.** The real differential is $\sum(\partial f/\partial x)dx+(\partial f/\partial y)dy$; substituting $dz=dx+\mathrm i\,dy$ and $d\bar z=dx-\mathrm i\,dy$ gives the formula; the conjugation identity is the definition.

**Corollary (the Cauchy–Riemann equations).** The function $f$ is holomorphic iff $\partial f/\partial\bar z_{ij}=0$ for all $i,j$.

**Proof.** A function is holomorphic iff its differential is complex-linear, that is iff the $d\bar z$ terms vanish.

### Holomorphic Functions

**Theorem.** The determinant, the product, the inverse on $GL_6$, and the exponential are holomorphic.

**Proof.** The determinant and the product are polynomials in the entries; the inverse is rational with denominator $\det A$, hence holomorphic on $GL_6$; the exponential is a uniformly convergent series of polynomials, hence holomorphic.

**Corollary (the logarithm and the square root).** The logarithm is holomorphic on a neighborhood of $I_6$, and the square root is holomorphic on a neighborhood of $I_6$ in the positive definite cone.

**Proof.** The logarithm series $\log(I+N)=\sum(-1)^{m+1}N^m/m$ converges for $\lVert N\rVert<1$ and is holomorphic; the square root is the exponential of half the logarithm, or the binomial series.

**Corollary (the matrix functions).** A holomorphic function of a matrix, defined by a power series with positive radius, is holomorphic in the entries on the domain of convergence.

**Proof.** The power series converges uniformly on compact sets; each term is a polynomial; the sum is holomorphic.

### The Matrix Functions

**Proposition.** The functional calculus for polynomials and entire functions is holomorphic in $A$: if $f$ is entire, then $A\mapsto f(A)$ is entire.

**Proof.** $f(A)=\sum c_mA^m$; each $A^m$ is a polynomial in the entries; the series converges uniformly on compact sets.

**Corollary.** The exponential, the sine and the cosine, and every entire function of $A$ are entire matrix functions.

**Proof.** Their series converge uniformly on compact sets.

## The Holomorphic Functional Calculus

### The Resolvent

**Definition.** The **resolvent** of $A$ is

$$
R(z)=(zI_6-A)^{-1},
\qquad
z\in\rho(A)=\mathbb{C}\setminus\sigma(A).
$$

**Theorem (the resolvent identity).**

$$
R(z)-R(w)=(w-z)R(z)R(w).
$$

**Proof.** Multiply by $(zI_6-A)(wI_6-A)$; the difference of the two factors is $(w-z)I_6$.

**Corollary (the analyticity).** $R(z)$ is holomorphic on the open set $\rho(A)$, and its poles are the eigenvalues of $A$, with pole order the largest Jordan block.

**Proof.** The inverse is holomorphic on the invertible locus; the Laurent expansion at an eigenvalue is finite with order the largest block.

### The Contour Integral

**Theorem (the Dunford calculus).** Let $f$ be holomorphic on a neighborhood of $\sigma(A)$, and let $\Gamma$ be a finite union of positively oriented Jordan curves enclosing $\sigma(A)$ inside the domain of $f$. Then

$$
f(A)=\frac{1}{2\pi\mathrm i}\oint_\Gamma f(z)R(z)\,dz
$$

defines an algebra homomorphism $f\mapsto f(A)$ that agrees with the polynomial calculus.

**Proof.** The integral converges because $R(z)$ is continuous on $\Gamma$; the homomorphism property follows from the resolvent identity and the Cauchy theorem; on polynomials, the integral reproduces $A^n$ by the expansion at infinity.

**Corollary (the spectral mapping).**

$$
\sigma(f(A))=f(\sigma(A)).
$$

**Proof.** In the Jordan basis, $f(A)$ has the eigenvalues $f(\lambda_i)$ with the same block structure.

### The Riesz Projector

**Definition.** The **Riesz projector** of a contour $\Gamma$ is

$$
P_\Gamma=\frac{1}{2\pi\mathrm i}\oint_\Gamma R(z)\,dz.
$$

**Theorem.** $P_\Gamma$ is an idempotent that commutes with $A$, its image is the sum of the generalized eigenspaces of the eigenvalues inside $\Gamma$, and its rank is the sum of the algebraic multiplicities of those eigenvalues.

**Proof.** The residue of the resolvent at an eigenvalue is the projector onto its generalized eigenspace; the contour integral sums the residues inside $\Gamma$. The idempotence follows from the resolvent identity; the rank is the trace, which is the sum of the multiplicities.

**Corollary (the spectral decomposition).** For contours $\Gamma_i$ around the distinct eigenvalues,

$$
P_iP_j=\delta_{ij}P_i,\qquad
\sum_iP_i=I_6,\qquad
A=\sum_i(\lambda_iP_i+N_i),
$$

with $N_i=(A-\lambda_iI_6)P_i$ nilpotent.

**Proof.** The projectors are the residues; the decomposition is the Jordan decomposition in the spectral form.

## The Fourier Transform

### The Schwartz Space

**Definition.** The **Schwartz space** $\mathcal{S}(\mathbb{C}^{36})$ is the space of smooth functions $f$ on $\mathbb{R}^{72}$ such that every derivative multiplied by every polynomial is bounded.

**Proposition.** $\mathcal{S}$ is a Fréchet space, stable under differentiation and multiplication by polynomials, and the Fourier transform

$$
\hat f(\xi)=\int_{\mathbb{R}^{72}}f(x)e^{-2\pi\mathrm i\langle\xi,x\rangle}\,dx
$$

maps $\mathcal{S}$ into itself.

**Proof.** The derivatives of $\hat f$ multiply by powers of $\xi$; the decay at infinity follows from integration by parts; the standard Schwartz estimates give the stability.

**Corollary (Plancherel and inversion).** The Fourier transform extends to a $*$-unitary operator on $L^2(\mathbb{R}^{72})$, and

$$
f(x)=\int_{\mathbb{R}^{72}}\hat f(\xi)e^{2\pi\mathrm i\langle\xi,x\rangle}\,d\xi .
$$

**Proof.** The inversion and Plancherel theorems for the Euclidean Fourier transform; the Gaussian is the standard test function.

### The Inversion and Plancherel

**Theorem.** The Fourier transform is an isomorphism of $\mathcal{S}$ with itself, and it extends to a $*$-unitary isomorphism of $L^2$; the Plancherel identity is

$$
\lVert f\rVert_2=\lVert\hat f\rVert_2 .
$$

**Proof.** The inversion formula on the Schwartz space; the density of $\mathcal{S}$ in $L^2$; unitarity follows from the inversion and the $L^2$ pairing.

**Corollary (differentiation and convolution).** The Fourier transform converts differentiation into multiplication,

$$
\widehat{\partial_jf}(\xi)=2\pi\mathrm i\xi_j\hat f(\xi),
$$

and convolution into product.

**Proof.** Integration by parts; the convolution theorem.

### The Gaussian and the Heat Kernel

**Proposition.** The Gaussian Fourier transform is

$$
\int_{\mathbb{R}^{72}}e^{-\pi\lvert x\rvert^2}e^{-2\pi\mathrm i\langle\xi,x\rangle}\,dx
=e^{-\pi\lvert\xi\rvert^2}.
$$

**Proof.** The integral factors over the $72$ coordinates; the one-dimensional formula is the standard Gaussian integral.

**Corollary (the heat kernel).** The heat kernel on $\mathbb{R}^{72}$ is

$$
p_t(x)=\frac{1}{(4\pi t)^{36}}e^{-\lvert x\rvert^2/(4t)},
$$

and it satisfies $\partial_tp_t=\Delta p_t$, with $p_t\to\delta_0$ as $t\to0$.

**Proof.** The Fourier transform of $p_t$ is $e^{-4\pi^2t\lvert\xi\rvert^2}$, which solves the Fourier-transformed heat equation; the inversion gives the displayed kernel.

**Remark (the Euclidean transform).** **The Fourier transform is the Euclidean analysis of the vector space, not the group Fourier transform of $GL_6$.** It uses the additive structure of $\mathbb{C}^{36}$; the multiplicative structure enters through the algebra of matrix functions, not through the Fourier transform. The group Fourier transform of $U(6)$ is a different object, defined by the irreducible representations; it is not needed here.

## Zero Divisors and Ordinary Matrix Analysis

### The Field and the Algebra

**Proposition.** The field $\mathbb{C}$ has no zero divisors: if $zw=0$, then $z=0$ or $w=0$. The algebra $M_6(\mathbb{C})$ has zero divisors: $E_{12}\neq0$ and $E_{12}^2=0$; more generally, every nilpotent is a zero divisor, and every singular matrix is a zero divisor.

**Proof.** The field is an integral domain. In $M_6$, $E_{12}E_{12}=0$; if $A$ is singular, choose a nonzero $B$ with $\operatorname{im}B\subseteq\ker A$, and then $AB=0$.

**Corollary (the singular set).** The zero divisors are the singular set

$$
\Sigma=\{A:\det A=0\},
$$

a complex hypersurface of real codimension two. The invertible elements are exactly the matrices with nonzero determinant.

**Proof.** This is *The Forms, the Norms and the Singular Set of $M_6(\mathbb{C})$*.

**Remark (what is absent).** **The absence of zero divisors is a property of the field, not of the algebra.** The scalar field $\mathbb{C}$ is an integral domain, and this is what makes the ordinary linear algebra and the holomorphic functional calculus work. The algebra $M_6(\mathbb{C})$ has zero divisors; the nilpotents are the simplest, and they are the source of the Jordan decomposition and the non-semisimple spectral theory. There is no null cone of an indefinite form: the trace form is definite, and its only isotropic vector is $0$.

### The Ordinary Matrix Analysis

**Theorem (the analysis over the field).** The ordinary matrix analysis of $M_6(\mathbb{C})$ consists of the spectrum, the resolvent, the Dunford calculus, the Jordan form, the singular value decomposition and the determinant. All of it is the analysis of the field $\mathbb{C}$ applied to the finite-dimensional algebra.

**Proof.** The spectrum is the zero set of the characteristic polynomial over $\mathbb{C}$; the resolvent is the inverse in $M_6(\mathbb{C})$; the functional calculus is the Cauchy integral over $\mathbb{C}$; the Jordan form and the SVD are the canonical forms over $\mathbb{C}$.

**Corollary (the boundary).** The analysis does not need a division algebra structure on $M_6$; it needs the field $\mathbb{C}$ and the finite dimension. The singular set is handled by the determinant, not by a null cone.

**Proof.** The determinant detects invertibility; the resolvent is defined off the spectrum; the singular directions are the kernel directions, and the polar decomposition and the SVD organise them.

### The Boundary Against Fueter Theory

**Theorem (the Fueter boundary).** Fueter theory is the quaternionic or Clifford analysis of the Cauchy–Fueter operator

$$
Df=\sum_{\mu=0}^{3}e_\mu\frac{\partial f}{\partial x_\mu},
$$

acting on functions with values in a quaternion or Clifford algebra. It is a first-order theory in four real variables with values in a division algebra or a Clifford module. The analysis of this article is the holomorphic functional calculus on the complex matrix algebra $M_6(\mathbb{C})$, which is a different theory.

**Proof.** The Fueter operator uses the multiplication and the conjugates of the quaternion algebra; its regularity is a first-order system in four real variables. The holomorphic functional calculus uses the resolvent and the Cauchy integral in the complex plane; the two theories have different operators and different function spaces.

**Corollary (the two analyses).** The holomorphic functional calculus and the Fueter calculus are different theories: the first is the analysis of the spectrum of a matrix over $\mathbb{C}$, the second is the analysis of a Dirac operator over a quaternionic or Clifford module.

**Proof.** The first is commutative in the scalar variable and uses the Cauchy kernel $1/(z-A)$; the second is a first-order operator with a noncommutative coefficient algebra.

**Remark (where the quaternionic structure lives).** The quaternionic structure lives in the biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$, which is the $n=2$ case of the present family, not in $M_6(\mathbb{C})$. **The boundary is the dimension and the algebra: $M_6$ has the ordinary complex analysis, and Fueter theory needs another structure.**

## Summary

The algebra $M_6(\mathbb{C})$ is a complex manifold of dimension $36$ and a real manifold of dimension $72$, with the Lebesgue measure of $\mathbb{R}^{72}$ and the Gaussian normalisation $\pi^{36}$. The product, the inverse, the determinant and the exponential are holomorphic, with derivatives

$$
D(AB)=HB+AK,\qquad
D(A^{-1})=-A^{-1}HA^{-1},\qquad
D\det_A(H)=\operatorname{tr}(\operatorname{adj}(A)H),
$$

and

$$
D\exp_A(H)=e^A\sum_{m=0}^{\infty}\frac{(-1)^m}{(m+1)!}\operatorname{ad}_A^m(H).
$$

$$
\boxed{\ \dim_{\mathbb{C}}M_6=36,\quad \dim_{\mathbb{R}}=72,\quad \int e^{-\operatorname{tr}(A^*A)}dA=\pi^{36},\quad f(A)=\frac{1}{2\pi\mathrm i}\oint fR\,dz .\ }
$$

The Wirtinger calculus gives the holomorphic functions; the Dunford calculus gives the spectral projectors and the spectral mapping theorem; the Fourier transform on $\mathbb{C}^{36}$ gives the Schwartz space, the inversion, the Plancherel theorem, the Gaussian and the heat kernel $(4\pi t)^{-36}e^{-\lvert x\rvert^2/(4t)}$.

The field $\mathbb{C}$ has no zero divisors; the algebra $M_6$ has the nilpotent zero divisors and the singular set of real codimension two. The ordinary matrix analysis is the analysis over the field; the boundary against Fueter theory is the passage from the holomorphic functional calculus to a Dirac operator on a quaternionic or Clifford module.

| Object | Data |
|---|---|
| Complex dimension | $36$ |
| Real dimension | $72$ |
| Gaussian integral | $\pi^{36}$ |
| Determinant derivative | $\operatorname{tr}(\operatorname{adj}(A)H)$ |
| Exponential derivative | $e^A\sum(-1)^m\operatorname{ad}_A^m/(m+1)!$ |
| Fourier space | $\mathbb{R}^{72}$ |
| Heat kernel | $(4\pi t)^{-36}e^{-\lvert x\rvert^2/(4t)}$ |
| Zero divisors | the singular set, real codimension $2$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $z_{ij}=x_{ij}+\mathrm i y_{ij}$ | the complex coordinates |
| $\partial/\partial z_{ij}$, $\partial/\partial\bar z_{ij}$ | the Wirtinger derivatives |
| $R(z)=(zI_6-A)^{-1}$ | the resolvent |
| $P_\Gamma$ | the Riesz projector |
| $\mathcal{S}(\mathbb{C}^{36})$ | the Schwartz space |
| $\hat f$ | the Fourier transform |
| $\Delta$ | the Laplacian on $\mathbb{R}^{72}$ |

## Further Reading

- [The Forms, the Norms and the Singular Set of $M_6(\mathbb{C})$](the-forms-the-norms-and-the-singular-set-of-m6c.html), for the determinant, the singular set and the norms.
- [Spectral Theory and the Spectral Projectors of $M_6(\mathbb{C})$](spectral-theory-and-the-spectral-projectors-of-m6c.html), for the resolvent and the Dunford calculus.
- [The Exponential and the Lie Group of $M_6(\mathbb{C})$](the-exponential-and-the-lie-group-of-m6c.html), for the exponential and the logarithm.
- [The Polar Decomposition of $M_6(\mathbb{C})$](the-polar-decomposition-of-m6c.html), for the positive cone and the singular values.
- [The Involution and the Hermitian Structure of $M_6(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m6c.html), for the Hermitian form and the $*$-unitary group.
- [Analysis on $M_5(\mathbb{C})$](analysis-on-m5c.html), for the same analysis in the neighbouring dimension.
- [Holomorphic Functional Calculus](holomorphic-functional-calculus.html), for the Dunford calculus in a Banach algebra.
- [Fueter Theory](fueter-theory.html), for the quaternionic analysis and its Cauchy–Fueter operator.
