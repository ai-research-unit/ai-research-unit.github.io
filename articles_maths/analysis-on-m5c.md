# __Analysis on $M_5(\mathbb{C})$__

## Introduction

The algebra $M_5(\mathbb{C})$ is a complex vector space of dimension $25$, hence a real manifold of dimension $50$. It carries the smooth structure of $\mathbb{C}^{25}$, the complex structure of multiplication by $i$, the Lebesgue measure of $\mathbb{R}^{50}$, and the norms of *The Forms, the Norms and the Singular Set of $M_5(\mathbb{C})$*. The analysis on $M_5$ is the ordinary analysis of a finite-dimensional complex vector space, enriched by the algebra structure: the product, the inverse, the determinant and the exponential are smooth (indeed holomorphic) maps, and their derivatives are the standard formulas.

The **Wirtinger calculus** gives the complex derivatives $\partial/\partial z_{ij}$ and $\partial/\partial\bar z_{ij}$. The holomorphic functions are those with $\partial f/\partial\bar z_{ij}=0$; the determinant is a holomorphic polynomial, the inverse is holomorphic on $GL_5$, and the exponential is entire. The **holomorphic functional calculus** evaluates a holomorphic function on a matrix through the resolvent and a contour integral,

$$
f(A)=\frac{1}{2\pi i}\oint_\Gamma f(z)(zI-A)^{-1}\,dz,
$$

and the **Riesz projector**

$$
P=\frac{1}{2\pi i}\oint_\Gamma(zI-A)^{-1}\,dz
$$

is the spectral projector onto the part of the spectrum inside $\Gamma$. The **Fourier transform** on $\mathbb{C}^{25}$ is the Euclidean Fourier transform of the $50$ real coordinates; the Schwartz space, the inversion theorem, the Plancherel theorem and the Gaussian are the standard ones.

The article also fixes the boundary against **Fueter theory**. The field $\mathbb{C}$ has no zero divisors; the algebra $M_5(\mathbb{C})$ does: the nilpotents satisfy $E_{12}^2=0$. The ordinary matrix analysis is the analysis over the field, with the spectrum, the resolvent and the functional calculus. Fueter theory is the quaternionic (or Clifford) analysis of the Cauchy–Fueter operator; it needs a different structure, a real division algebra or a Clifford module with a Dirac operator, which $M_5(\mathbb{C})$ does not carry. The holomorphic functional calculus is not Fueter theory.

The article assumes the trace, the determinant, the norms, the Hermitian structure and the spectral theorem. It proves the derivative formulas, the Wirtinger rules, the resolvent and Riesz formulas, and it states the Fourier theorems with their standard proofs.

## The Smooth Structure

### The Real and Complex Manifolds

**Proposition.** $M_5(\mathbb{C})$ is a complex manifold of complex dimension $25$ and a real manifold of real dimension $50$. The complex structure is the linear map $J(A)=iA$, with $J^2=-I$; the real tangent space at every point is $M_5$, and the complex tangent space is the complexification.

**Proof.** The identification $M_5\cong\mathbb{C}^{25}$ by the coordinates $A_{ij}$ is a complex-linear isomorphism; the real coordinates are the real and imaginary parts, $50$ in number. The multiplication by $i$ is a real-linear map with $J^2=-I$, which is the complex structure. The tangent space of a vector space is the vector space itself.

**Corollary.** The manifold is parallelizable: the coordinate vector fields $\partial/\partial x_{ij}$ and $\partial/\partial y_{ij}$ are a global frame. The complex vector fields $\partial/\partial z_{ij}$ and $\partial/\partial\bar z_{ij}$ are a global frame of the complexified tangent bundle.

**Proof.** The vector space has a global basis of constant vector fields; the Wirtinger derivatives are the complex basis.

**Corollary.** The manifold is oriented, and the Lebesgue measure

$$
dA=\prod_{i,j}dx_{ij}\,dy_{ij}
$$

is a translation-invariant volume form. The total volume of a measurable set is its $50$-dimensional Lebesgue measure.

**Proof.** The real coordinates give the standard orientation and the standard Lebesgue measure; translations are isometries of $\mathbb{R}^{50}$.

### The Tangent Space

**Definition.** The **tangent space** $T_AM_5$ is $M_5$, with the derivative of a curve $A(t)$ at $t=0$ being $A'(0)$. The **differential** of a smooth map $F:M_5\to W$ at $A$ is the linear map $DF_A:M_5\to W$ given by $DF_A(H)=\frac{d}{dt}|_{0}F(A+tH)$.

**Proposition.** The tangent space is $M_5$ at every point; the differential of a linear map is the map itself; the differential of the product is

$$
D(AB)_{(A,B)}(H,K)=HB+AK .
$$

**Proof.** The tangent space of a vector space is the vector space; the derivative of a linear map is itself; the product is bilinear, so the derivative is the sum of the two partial derivatives.

**Corollary.** The left multiplication $L_A(B)=AB$ has differential $DL_A(B)(K)=AK$; the right multiplication $R_B(A)=AB$ has differential $DR_B(A)(H)=HB$.

**Proof.** The product is linear in each factor; the partial derivatives are the displayed maps.

### The Lebesgue Measure

**Definition.** The **Lebesgue measure** on $M_5$ is the translation-invariant measure $dA$ of $\mathbb{R}^{50}$.

**Proposition.** The measure is invariant under translations and under the $*$-unitary group: $d(UA)=dA$ and $d(AU)=dA$ for $U\in U(5)$. It is not invariant under general linear changes of coordinates; the Jacobian is $|\det g|^{10}$ for $A\mapsto gA$ (or $A\mapsto Ag$).

**Proof.** The translation invariance is the Lebesgue measure on $\mathbb{R}^{50}$; the $*$-unitary invariance is the orthogonality of the real linear map $A\mapsto UA$ (the Frobenius norm is preserved). For a general $g$, the left multiplication $L_g$ on $M_5$ has complex determinant $(\det g)^5$ (five column blocks, each with determinant $\det g$), so its real Jacobian is $|(\det g)^5|^2=|\det g|^{10}$.

**Corollary.** The Gaussian integral converges:

$$
\int_{M_5}e^{-\operatorname{tr}(A^*A)}\,dA=\pi^{25}.
$$

**Proof.** The integrand is $\prod_{ij}e^{-|A_{ij}|^2}$; the integral over each complex coordinate is $\pi$; the product over the $25$ coordinates is $\pi^{25}$.

## The Derivatives

### The Product

**Proposition.** The product map $m(A,B)=AB$ is smooth (polynomial) and its differential is

$$
Dm_{(A,B)}(H,K)=HB+AK .
$$

**Proof.** The entries of $AB$ are polynomials of degree $2$; the derivative is the bilinear part, which is $HB+AK$.

**Corollary.** The product is holomorphic in each variable separately; the algebra is a complex Lie algebra with the commutator.

**Proof.** The entries are polynomials in the entries of $A$ and $B$, hence holomorphic; the commutator is bilinear.

### The Inverse

**Theorem.** The inversion map $\operatorname{inv}:GL_5\to GL_5$, $A\mapsto A^{-1}$, is smooth (holomorphic), and its differential is

$$
D(\operatorname{inv})_A(H)=-A^{-1}HA^{-1}.
$$

**Proof.** For small $t$,

$$
(A+tH)^{-1}=A^{-1}-tA^{-1}HA^{-1}+O(t^2),
$$

by the Neumann series $(I+tA^{-1}H)^{-1}=I-tA^{-1}H+O(t^2)$. The derivative is the linear term.

**Corollary.** The inverse is a local diffeomorphism at every invertible $A$; its differential is invertible with inverse $-A(\cdot)A$.

**Proof.** The differential $H\mapsto-A^{-1}HA^{-1}$ is invertible, with inverse $K\mapsto-AKA$; the inverse function theorem applies.

### The Determinant

**Theorem.** The determinant is a holomorphic polynomial of degree $5$, and

$$
D\det_A(H)=\operatorname{tr}(\operatorname{adj}(A)H).
$$

At $A=I$, $D\det_I(H)=\operatorname{tr}H$.

**Proof.** Expand $\det(A+tH)$ in powers of $t$; the linear term is the sum over the positions of $H$ with the cofactor of $A$, which is the trace of the adjugate times $H$. At $A=I$, the adjugate is $I$.

**Corollary.** The determinant is a submersion at every point of rank $4$; the singular set $\det=0$ is a complex hypersurface of real codimension $2$, smooth at the rank-$4$ points.

**Proof.** The derivative is nonzero exactly when the adjugate is nonzero, i.e., at rank $4$; the nonzero complex-linear functional has kernel of real codimension $2$; the implicit function theorem gives the smooth hypersurface.

### The Exponential

**Theorem.** The exponential is entire, and its differential is

$$
D\exp_A(H)=e^A\sum_{m=0}^{\infty}\frac{(-1)^m}{(m+1)!}\operatorname{ad}_A^m(H).
$$

At $A=0$, $D\exp_0(H)=H$; for a scalar $A=\lambda I$, $D\exp_{\lambda I}(H)=e^\lambda H$.

**Proof.** Differentiate $e^{A+tH}$ at $t=0$. The derivative satisfies the differential equation $\frac{d}{dt}e^{A+tH}=e^{A+tH}H$ with the initial value $e^A$; the solution is $e^A$ times the series $\sum_m(-1)^m\operatorname{ad}_A^m(H)/(m+1)!$, which is the standard formula for the derivative of the exponential. At $A=0$ only the $m=0$ term survives; for a scalar, $\operatorname{ad}_A=0$.

**Corollary.** The differential at $0$ is the identity, so the exponential is a local diffeomorphism at $0$; the inverse branch is the logarithm.

**Proof.** $D\exp_0=I$ is invertible; the inverse function theorem gives the local inverse.

**Remark.** **The derivative of the exponential is not $e^A H$ unless $A$ is scalar or $H$ commutes with $A$.** The series with the adjoint corrects for the noncommutativity; the first correction is $\frac12[A,H]$. The formula is the analytic form of the Baker–Campbell–Hausdorff expansion.

## The Wirtinger Calculus

### The Complex Derivatives

**Definition.** For a smooth function $f:M_5\to\mathbb{C}$, the **Wirtinger derivatives** are

$$
\frac{\partial f}{\partial z_{ij}}=\frac12\left(\frac{\partial f}{\partial x_{ij}}-i\frac{\partial f}{\partial y_{ij}}\right),\qquad
\frac{\partial f}{\partial\bar z_{ij}}=\frac12\left(\frac{\partial f}{\partial x_{ij}}+i\frac{\partial f}{\partial y_{ij}}\right).
$$

**Proposition.** The differential is

$$
df=\sum_{ij}\frac{\partial f}{\partial z_{ij}}dz_{ij}+\sum_{ij}\frac{\partial f}{\partial\bar z_{ij}}d\bar z_{ij},
$$

and the Wirtinger derivatives satisfy $\overline{\partial f/\partial z_{ij}}=\partial\bar f/\partial\bar z_{ij}$.

**Proof.** The real differential is $\sum(\partial f/\partial x)dx+(\partial f/\partial y)dy$; substituting $dz=dx+i\,dy$ and $d\bar z=dx-i\,dy$ gives the formula; the conjugation identity is the definition.

**Corollary.** The function $f$ is holomorphic iff $\partial f/\partial\bar z_{ij}=0$ for all $i,j$; equivalently, the Cauchy–Riemann equations hold.

**Proof.** A function is holomorphic iff its differential is complex-linear, i.e., the $d\bar z$ terms vanish; this is the Cauchy–Riemann condition.

### Holomorphic Functions

**Theorem.** The determinant, the product, the inverse on $GL_5$, and the exponential are holomorphic.

**Proof.** The determinant and the product are polynomials in the entries, hence holomorphic. The inverse is rational with denominator $\det A$, hence holomorphic on $GL_5$. The exponential is a uniformly convergent series of polynomials, hence holomorphic.

**Corollary.** The logarithm is holomorphic on a neighborhood of $I$, and the square root is holomorphic on a neighborhood of $I$ in the positive definite cone.

**Proof.** The logarithm series $\log(I+N)=\sum(-1)^{m+1}N^m/m$ converges for $\|N\|<1$ and is holomorphic; the square root is the exponential of half the logarithm, or the binomial series $(I+N)^{1/2}$.

**Corollary.** A holomorphic function of a matrix, defined by a power series with positive radius, is holomorphic in the entries on the domain of convergence.

**Proof.** The power series converges uniformly on compact sets; each term is a polynomial; the sum is holomorphic.

### The Matrix Functions

**Proposition.** The functional calculus for polynomials and entire functions is holomorphic in $A$: if $f$ is entire, then $A\mapsto f(A)$ is entire.

**Proof.** $f(A)=\sum c_mA^m$; each $A^m$ is a polynomial in the entries; the series converges uniformly on compact sets.

**Corollary.** The exponential, the sine and the cosine, and every entire function of $A$ are entire matrix functions.

**Proof.** The exponential series, the sine and cosine series, and any entire series converge uniformly on compact sets.

## The Holomorphic Functional Calculus

### The Resolvent

**Definition.** The **resolvent set** of $A$ is $\rho(A)=\{z\in\mathbb{C}:zI-A\text{ is invertible}\}$; the **spectrum** is $\sigma(A)=\mathbb{C}\setminus\rho(A)$; the **resolvent** is

$$
R(z)=(zI-A)^{-1}.
$$

**Proposition.** The spectrum is the set of eigenvalues, a finite subset of at most $5$ points. The resolvent is holomorphic on $\rho(A)$, and it satisfies the **resolvent identity**

$$
R(z)-R(w)=(w-z)R(z)R(w).
$$

**Proof.** $zI-A$ is invertible iff $z$ is not an eigenvalue; the characteristic polynomial has degree $5$, so there are at most $5$ eigenvalues. The resolvent identity follows from

$$
(zI-A)^{-1}-(wI-A)^{-1}=(zI-A)^{-1}[(wI-A)-(zI-A)](wI-A)^{-1}.
$$

The analyticity is the holomorphic dependence of the inverse on $z$.

**Corollary.** The resolvent has the Neumann series at infinity,

$$
R(z)=z^{-1}I+z^{-2}A+z^{-3}A^2+\cdots,
$$

for $|z|>\|A\|$; and at a point $z_0\notin\sigma(A)$,

$$
R(z)=\sum_{m\ge0}(z_0-z)^mR(z_0)^{m+1}
$$

for $|z-z_0|$ small. The spectral radius is $\rho(A)=\lim_m\|A^m\|^{1/m}$.

**Proof.** The Neumann series is the geometric series for $(zI-A)^{-1}=z^{-1}(I-z^{-1}A)^{-1}$; the second is the geometric series for $(zI-A)^{-1}=(z_0I-A+(z-z_0)I)^{-1}$; the spectral radius formula is the standard Gelfand formula.

### The Contour Integral

**Theorem.** Let $f$ be holomorphic on an open set containing the spectrum $\sigma(A)$, and let $\Gamma$ be a finite union of positively oriented Jordan curves in the domain, enclosing the spectrum and no point of $\mathbb{C}\setminus\Omega$. Then

$$
f(A)=\frac{1}{2\pi i}\oint_\Gamma f(z)(zI-A)^{-1}\,dz
$$

is well defined, independent of the contour, and defines an algebra homomorphism $f\mapsto f(A)$ extending the polynomial calculus.

**Proof.** The resolvent is holomorphic on a neighborhood of $\Gamma$; the integral converges. The independence of the contour is the Cauchy theorem applied to the resolvent, which is holomorphic in the region between two contours. The homomorphism property follows from the resolvent identity and the Cauchy integral formula; the polynomial case is the Cauchy integral formula for the polynomial $f$.

**Corollary.** The spectral mapping theorem holds:

$$
\sigma(f(A))=f(\sigma(A)).
$$

**Proof.** For $w\notin f(\sigma(A))$, the function $1/(f(z)-w)$ is holomorphic on a neighborhood of the spectrum; the functional calculus gives $(f(A)-wI)^{-1}$, so $w\notin\sigma(f(A))$. Conversely, if $w=f(\lambda)$ for an eigenvalue $\lambda$, then $f(A)-wI$ has the eigenvector of $\lambda$ in its kernel, so $w\in\sigma(f(A))$.

### The Riesz Projector

**Definition.** For a contour $\Gamma$ enclosing a spectral set $\sigma_1\subset\sigma(A)$ and no other point of the spectrum, the **Riesz projector** is

$$
P=\frac{1}{2\pi i}\oint_\Gamma(zI-A)^{-1}\,dz .
$$

**Theorem.** $P$ is a projection, $P^2=P$, it commutes with $A$, and its image is the direct sum of the generalized eigenspaces of the eigenvalues inside $\Gamma$. The complementary projection $I-P$ is the Riesz projector of the complementary spectral set.

**Proof.** The idempotence follows from the resolvent identity and the Cauchy theorem:

$$
P^2=\frac{1}{(2\pi i)^2}\oint_\Gamma\oint_\Gamma R(z)R(w)\,dz\,dw
=\frac{1}{2\pi i}\oint_\Gamma R(z)\,dz=P,
$$

because $R(z)R(w)=(R(z)-R(w))/(w-z)$ and the inner integral picks the residue at $w=z$. The commutation with $A$ is the commutation of $A$ with the resolvent. The image is the generalized eigenspace by the contour integral of the resolvent, which is the spectral projection.

**Corollary.** For a simple spectrum, the Riesz projector of a single eigenvalue $\lambda_k$ is the Lagrange projector

$$
P_k=\frac{1}{2\pi i}\oint_{\Gamma_k}(zI-A)^{-1}\,dz
=\prod_{l\ne k}\frac{A-\lambda_lI}{\lambda_k-\lambda_l}.
$$

**Proof.** The contour around $\lambda_k$ alone picks the residue of the resolvent at $\lambda_k$, which is the spectral projector; the Lagrange formula is the polynomial expression of the same projector.

**Remark.** **The Riesz projector is the analytic form of the spectral projector.** It is the contour integral of the resolvent; the Lagrange polynomial is the algebraic form. The two agree at a simple spectrum, and the contour form extends to the repeated spectrum, where it projects onto the generalized eigenspace.

## The Fourier Transform

### The Schwartz Space

**Definition.** The **Schwartz space** $\mathcal{S}(\mathbb{C}^{25})$ is the space of smooth functions $f$ on $\mathbb{R}^{50}$ such that every derivative multiplied by every polynomial is bounded.

**Proposition.** $\mathcal{S}$ is a Fréchet space, stable under differentiation and under multiplication by polynomials, and the Fourier transform

$$
\hat f(\xi)=\int_{\mathbb{R}^{50}}f(x)e^{-2\pi i\langle\xi,x\rangle}\,dx
$$

maps $\mathcal{S}$ into itself.

**Proof.** The derivatives of $\hat f$ multiply by powers of $\xi$; the decay at infinity follows from integration by parts; the standard Schwartz estimates give the stability.

**Corollary.** The Fourier transform extends to a $*$-unitary operator on $L^2(\mathbb{R}^{50})$ (Plancherel), and the inversion formula holds:

$$
f(x)=\int_{\mathbb{R}^{50}}\hat f(\xi)e^{2\pi i\langle\xi,x\rangle}\,d\xi .
$$

**Proof.** The inversion and Plancherel theorems for the Euclidean Fourier transform; the Gaussian is the standard test function.

### The Inversion and Plancherel

**Theorem.** The Fourier transform is an isomorphism of $\mathcal{S}$ with itself, and it extends to a $*$-unitary isomorphism of $L^2$; the Plancherel identity is

$$
\|f\|_2=\|\hat f\|_2 .
$$

**Proof.** The inversion formula on the Schwartz space; the density of $\mathcal{S}$ in $L^2$; the unitarity follows from the inversion and the $L^2$ pairing.

**Corollary.** The Fourier transform converts differentiation into multiplication: $\widehat{\partial_jf}(\xi)=2\pi i\xi_j\hat f(\xi)$, and convolution into product.

**Proof.** Integration by parts; the convolution theorem is the standard one.

### The Gaussian and the Heat Kernel

**Proposition.** The Gaussian Fourier transform is

$$
\int_{\mathbb{R}^{50}}e^{-\pi|x|^2}e^{-2\pi i\langle\xi,x\rangle}\,dx=e^{-\pi|\xi|^2}.
$$

**Proof.** The integral factors over the $50$ coordinates; the one-dimensional formula $\int_{\mathbb{R}}e^{-\pi x^2}e^{-2\pi i\xi x}dx=e^{-\pi\xi^2}$ is the standard Gaussian integral.

**Corollary.** The heat kernel on $\mathbb{R}^{50}$ is

$$
p_t(x)=\frac{1}{(4\pi t)^{25}}e^{-|x|^2/(4t)},
$$

and it satisfies $\partial_tp_t=\Delta p_t$, with $p_t\to\delta_0$ as $t\to0$.

**Proof.** The Fourier transform of $p_t$ is $e^{-4\pi^2t|\xi|^2}$, which solves the Fourier-transformed heat equation; the inversion gives the displayed kernel.

**Remark.** **The Fourier transform is the Euclidean analysis of the vector space, not the group Fourier transform of $GL_5$.** It uses the additive structure of $\mathbb{C}^{25}$; the multiplicative structure enters through the algebra of matrix functions, not through the Fourier transform. The group Fourier transform of $U(5)$ is a different object, defined by the irreducible representations; it is not needed here.

## Zero Divisors and Ordinary Matrix Analysis

### The Field and the Algebra

**Proposition.** The field $\mathbb{C}$ has no zero divisors: if $zw=0$, then $z=0$ or $w=0$. The algebra $M_5(\mathbb{C})$ has zero divisors: $E_{12}\ne0$ and $E_{12}^2=0$; more generally, every nilpotent is a zero divisor.

**Proof.** The field is an integral domain; the matrix unit $E_{12}$ squares to zero, and $E_{12}E_{21}=E_{11}\ne0$ while $E_{12}E_{34}=0$; the nilpotents are nonzero with zero powers.

**Corollary.** The algebra is not a division algebra; it is a full matrix algebra, and its invertible elements are exactly the matrices with nonzero determinant. The ordinary matrix analysis is the analysis over the field $\mathbb{C}$, with the spectrum, the resolvent and the functional calculus; the zero divisors are the singular directions.

**Proof.** A matrix is invertible iff $\det\ne0$; the nilpotents are singular; the analysis is the complex analysis of the entries.

**Remark.** **The absence of zero divisors is a property of the field, not of the algebra.** The scalar field $\mathbb{C}$ has no zero divisors, and this is what makes the ordinary linear algebra and the holomorphic functional calculus work. The algebra $M_5(\mathbb{C})$ has zero divisors; the nilpotents are the simplest, and they are the source of the Jordan decomposition and the non-semisimple spectral theory. The biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$ also has zero divisors; the quaternion division algebra $\mathbb{H}$ has none, and that is a different story.

### The Boundary Against Fueter Theory

**Definition.** **Fueter theory** is the quaternionic analysis of the Cauchy–Fueter operator

$$
\bar\partial=\partial_{q_0}+i\partial_{q_1}+j\partial_{q_2}+k\partial_{q_3},
$$

acting on functions of a quaternion variable $q=q_0+q_1i+q_2j+q_3k$; the Fueter-regular functions are the solutions of $\bar\partial f=0$.

**Theorem.** The holomorphic functional calculus on $M_5(\mathbb{C})$ is not Fueter theory. Fueter theory needs the quaternion (or Clifford) algebra and its Dirac operator; $M_5(\mathbb{C})$ is a complex matrix algebra, not a Clifford algebra, and its analysis is the ordinary complex analysis of $\mathbb{C}^{25}$.

**Proof.** The Fueter operator uses the multiplication and the conjugates of the quaternion algebra; the regularity is a first-order system with four real variables. The holomorphic functional calculus uses the resolvent of a matrix and the Cauchy integral in the complex plane; it is the analysis of the spectrum, not of a Dirac operator. The algebra $M_5(\mathbb{C})$ has no quaternionic or Clifford structure of the required kind; its zero divisors and its complex dimension $25$ are the boundary.

**Corollary.** The biquaternion article's spinor analysis is the $M_2$ case; the $M_5$ analysis is the ordinary matrix analysis, and the two are separated by the dimension and the algebra. The Fueter theory belongs to the quaternionic side, not to the $M_5$ side.

**Proof.** The biquaternion algebra is $M_2(\mathbb{C})$; its spinors are two-dimensional; the $M_5$ carrier is five-dimensional; the Fueter operator is defined on the quaternions, not on $M_5$.

**Remark.** **The boundary is structural, not a matter of notation.** The Wirtinger calculus, the resolvent and the Fourier transform are the tools of the complex analysis of $M_5$; the Cauchy–Fueter operator and the Clifford modules are the tools of the quaternionic analysis. The two theories share the idea of a first-order operator and a Cauchy integral, but they act on different structures. The article stops at the boundary; the quaternionic side is the biquaternion corpus.

## Summary

$M_5(\mathbb{C})$ is a complex manifold of dimension $25$ and a real manifold of dimension $50$, with the Lebesgue measure and the Gaussian integral $\int e^{-\operatorname{tr}(A^*A)}dA=\pi^{25}$. The product, the inverse, the determinant and the exponential are holomorphic, with derivatives

$$
D(AB)=HB+AK,\qquad D(\operatorname{inv})_A(H)=-A^{-1}HA^{-1},\qquad D\det_A(H)=\operatorname{tr}(\operatorname{adj}(A)H),
$$

and

$$
D\exp_A(H)=e^A\sum_{m\ge0}\frac{(-1)^m}{(m+1)!}\operatorname{ad}_A^m(H).
$$

$$
\boxed{\ f(A)=\frac{1}{2\pi i}\oint_\Gamma f(z)(zI-A)^{-1}dz;\qquad P=\frac{1}{2\pi i}\oint_\Gamma(zI-A)^{-1}dz;\qquad \widehat f(\xi)=\int f(x)e^{-2\pi i\langle\xi,x\rangle}dx.\ }
$$

The Wirtinger calculus gives the holomorphic functions; the holomorphic functional calculus gives the spectral projectors and the spectral mapping theorem; the Fourier transform on $\mathbb{C}^{25}$ gives the Schwartz space, the inversion, the Plancherel theorem, the Gaussian and the heat kernel. The field $\mathbb{C}$ has no zero divisors; the algebra $M_5$ has the nilpotent zero divisors; the ordinary matrix analysis is the analysis over the field, and the boundary against Fueter theory is the quaternionic/Clifford structure that $M_5$ does not carry.

| Object | Formula |
|---|---|
| Complex dimension | $25$ |
| Real dimension | $50$ |
| Lebesgue measure | $\prod_{ij}dx_{ij}dy_{ij}$ |
| Gaussian integral | $\pi^{25}$ |
| Derivative of inverse | $-A^{-1}HA^{-1}$ |
| Derivative of determinant | $\operatorname{tr}(\operatorname{adj}(A)H)$ |
| Derivative of exponential | $e^A\sum(-1)^m\operatorname{ad}_A^m(H)/(m+1)!$ |
| Resolvent | $(zI-A)^{-1}$ |
| Riesz projector | $\frac{1}{2\pi i}\oint_\Gamma(zI-A)^{-1}dz$ |
| Fourier transform | $\int f(x)e^{-2\pi i\langle\xi,x\rangle}dx$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $z_{ij}=x_{ij}+iy_{ij}$ | The complex coordinates |
| $\partial/\partial z_{ij}$, $\partial/\partial\bar z_{ij}$ | The Wirtinger derivatives |
| $R(z)=(zI-A)^{-1}$ | The resolvent |
| $\sigma(A)$, $\rho(A)$ | The spectrum and the resolvent set |
| $P$ | The Riesz projector |
| $\mathcal{S}(\mathbb{C}^{25})$ | The Schwartz space |
| $\hat f$ | The Fourier transform |

## Further Reading

- Walter Rudin, *Functional Analysis* (McGraw-Hill, second edition, 1991), for the holomorphic functional calculus, the resolvent and the spectral mapping theorem.
- Elias M. Stein and Rami Shakarchi, *Fourier Analysis: An Introduction* (Princeton University Press, 2003), for the Schwartz space, the Fourier inversion, the Plancherel theorem and the Gaussian.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2013), for the derivatives of the inverse, the determinant and the exponential.
- Rolf Nevanlinna and Veikko Paatero, *Introduction to Complex Analysis* (Addison-Wesley, 1969), for the Wirtinger calculus and the Cauchy integral.
- Rudolf Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u=0$ und $\Delta\Delta u=0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* 7 (1934), 307–330, for the Fueter operator and the quaternionic analysis.
- [The Element, the Coordinates and the Trace of $M_5(\mathbb{C})$](the-element-the-coordinates-and-the-trace-of-m5c.html), for the trace, the determinant and the Jordan decomposition.
- [The Involution and the Hermitian Structure of $M_5(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m5c.html), for the Hermitian form, the norms and the real codimension $2$.
- [Spectral Theory and the Spectral Projectors of $M_5(\mathbb{C})$](spectral-theory-and-the-spectral-projectors-of-m5c.html), for the spectral theorem and the projectors.
- [The Exponential and the Lie Group of $M_5(\mathbb{C})$](the-exponential-and-the-lie-group-of-m5c.html), for the exponential and the logarithm.
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the biquaternion side and the boundary against Fueter theory.
