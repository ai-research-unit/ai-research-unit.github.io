# __Analysis on $M_4(\mathbb{C})$__

## Introduction

**$M_4(\mathbb{C})$ is a complex Hilbert space of dimension sixteen, and analysis on it is the analysis of entire functions of sixteen complex variables, together with the functional calculus of the algebra.** The Hilbert space structure is the Frobenius form $\langle A,B\rangle=\operatorname{tr}(A^*B)$; holomorphic functions are the complex-differentiable functions, equivalently the functions with $\partial f/\partial\bar A_{ij}=0$ for all $i,j$; the Laplacian is $\Delta=4\sum_{i,j}\partial^2/\partial A_{ij}\partial\bar A_{ij}$, and the holomorphic functions are harmonic.

The article describes the Hilbert space, the holomorphic and real-analytic functions, the Wirtinger derivatives and the Cauchy–Riemann equations, the Laplacian and harmonic functions, the functional calculus, the Gaussian measure and the heat kernel, and the differential calculus of the determinant and the trace.

The involution and the trace form are *The Involution and the Hermitian Structure of $M_4(\mathbb{C})$*; the spectral theory is *Spectral Theory and the Spectral Projectors of $M_4(\mathbb{C})$*; the exponential is *The Exponential and the Lie Group of $M_4(\mathbb{C})$*; the geometry of the idempotents is *The Geometry of the Idempotents of $M_4(\mathbb{C})$*.

## The Hilbert Space

**The complex Hilbert space.** The algebra is a complex vector space of dimension $16$, with the inner product

$$
\langle A,B\rangle=\operatorname{tr}(A^*B)
$$

and the norm

$$
\lVert A\rVert=\sqrt{\langle A,A\rangle}
=\Bigl(\sum_{i,j=1}^{4}\lvert A_{ij}\rvert^2\Bigr)^{1/2}.
$$

The matrix units $E_{ij}$ form an orthonormal basis:

$$
\langle E_{ij},E_{kl}\rangle=\delta_{ik}\delta_{jl}.
$$

**The identification with $\mathbb{C}^{16}$.** The map $A\mapsto(A_{11},A_{12},\dots,A_{44})$ is a $*$-unitary isomorphism

$$
M_4(\mathbb{C})\cong\mathbb{C}^{16}.
$$

The real space is $\mathbb{R}^{32}$ with the Euclidean inner product

$$
(A,B)_{\mathbb{R}}=\operatorname{Re}\operatorname{tr}(A^*B).
$$

**The topology.** All norms on a finite-dimensional space are equivalent, so the Frobenius norm, the operator norm and the nuclear norm define the same topology. The space is complete, locally compact, and separable. The group $GL_4$ is an open subset, hence a manifold of real dimension $32$.

**The measure.** The Lebesgue measure $dA$ is the product of the Lebesgue measures of the real and imaginary parts of the sixteen entries:

$$
dA=\prod_{i,j=1}^{4}dx_{ij}\,dy_{ij},\qquad A_{ij}=x_{ij}+iy_{ij}.
$$

It is invariant under translations and under the orthogonal group, and it is the Haar measure of the additive group.

**The algebra operations.** The product $(A,B)\mapsto AB$ is a complex-bilinear map, hence holomorphic; the trace and the determinant are holomorphic polynomials; the inverse $A\mapsto A^{-1}$ is holomorphic on $GL_4$; the exponential is holomorphic. These are the basic holomorphic maps of the algebra.

## Holomorphic and Real-Analytic Functions

**Holomorphic functions.** A function $f:M_4\to\mathbb{C}$ is **holomorphic** if it is complex differentiable at every point: for every $A$ there is a complex-linear map $Df(A)$ with

$$
f(A+H)=f(A)+Df(A)(H)+o(\lVert H\rVert).
$$

Equivalently, $f$ is holomorphic in the sixteen complex coordinates $A_{ij}$, with

$$
\frac{\partial f}{\partial\bar A_{ij}}=0,\qquad i,j=1,\dots,4.
$$

The holomorphic functions on the whole space are the **entire functions** of sixteen complex variables.

**The power series.** Every holomorphic function has a convergent power series

$$
f(A)=\sum_{\alpha}c_\alpha A^\alpha
$$

in a polydisc around the origin, with multi-indices $\alpha=(\alpha_{11},\dots,\alpha_{44})$. The radius of convergence is the radius of the largest polydisc on which the series converges. The polynomials are the entire functions with finite expansion.

**Real-analytic functions.** A function $f:M_4\to\mathbb{C}$ is **real-analytic** if it has a convergent Taylor series in the thirty-two real coordinates. Every holomorphic function is real-analytic; the converse is false. The squared norm $\lVert A\rVert^2$ is a real-analytic polynomial but not holomorphic; the function $\bar A_{11}$ is real-analytic but not holomorphic.

**The identity theorem.** If two holomorphic functions agree on a nonempty open subset of a connected domain, they agree everywhere on the domain. The algebra $M_4$ is connected, so the identity theorem applies globally.

**The maximum principle.** If $f$ is holomorphic on a bounded domain and continuous on its closure, then $\lvert f\rvert$ attains its maximum on the boundary. If $f$ is entire and bounded, then $f$ is constant (Liouville's theorem).

**The algebra maps.** The determinant, the trace and the entries are holomorphic polynomials. The inverse is holomorphic on $GL_4$; the resolvent $(zI-A)^{-1}$ is holomorphic in $(z,A)$ on the domain $z\notin\sigma(A)$. The exponential is entire. The spectral projectors are holomorphic in $A$ on the simple-spectrum locus, and the Riesz projectors are holomorphic for a fixed contour.

## The Wirtinger Derivatives and the Cauchy–Riemann Equations

**The Wirtinger derivatives.** For a real-differentiable function $f(A,\bar A)$, define

$$
\frac{\partial f}{\partial A_{ij}}
=\frac12\Bigl(\frac{\partial f}{\partial x_{ij}}-i\frac{\partial f}{\partial y_{ij}}\Bigr),
\qquad
\frac{\partial f}{\partial\bar A_{ij}}
=\frac12\Bigl(\frac{\partial f}{\partial x_{ij}}+i\frac{\partial f}{\partial y_{ij}}\Bigr).
$$

The complex differential is

$$
df=\sum_{i,j}\frac{\partial f}{\partial A_{ij}}dA_{ij}
+\sum_{i,j}\frac{\partial f}{\partial\bar A_{ij}}d\bar A_{ij}.
$$

**The Cauchy–Riemann equations.** The function $f$ is holomorphic exactly when

$$
\frac{\partial f}{\partial\bar A_{ij}}=0,\qquad i,j=1,\dots,4.
$$

These are thirty-two real equations (sixteen complex equations) on the real and imaginary parts of $f$.

**The derivative of the determinant.** The determinant is a holomorphic polynomial, and

$$
\frac{\partial\det}{\partial A_{ij}}=(\operatorname{adj}A)_{ji},
$$

the cofactor of the $(i,j)$ entry. In matrix form, the matrix of partial derivatives is $(\operatorname{adj}A)^{\mathsf T}$, and the gradient under the trace pairing is $\operatorname{adj}A$:

$$
d(\det)_A(B)=\operatorname{tr}(\operatorname{adj}(A)B).
$$

**The derivative of the trace.** The trace is linear:

$$
\frac{\partial\operatorname{tr}}{\partial A_{ij}}=\delta_{ij},
\qquad
d(\operatorname{tr})_A(B)=\operatorname{tr}B.
$$

**The derivative of the inverse.** On $GL_4$,

$$
d(A^{-1})_A(B)=-A^{-1}BA^{-1}.
$$

**The derivative of the squared norm.** For the real function $\lVert A\rVert^2=\operatorname{tr}(A^*A)$,

$$
\frac{\partial\lVert A\rVert^2}{\partial\bar A_{ij}}=A_{ij},
\qquad
\frac{\partial\lVert A\rVert^2}{\partial A_{ij}}=\bar A_{ij}.
$$

The gradient in the real sense is $2A$.

## The Laplacian and Harmonic Functions

**The Laplacian.** The Euclidean Laplacian on $\mathbb{R}^{32}$ is

$$
\Delta=\sum_{i,j=1}^{4}\Bigl(\frac{\partial^2}{\partial x_{ij}^2}+\frac{\partial^2}{\partial y_{ij}^2}\Bigr)
=4\sum_{i,j=1}^{4}\frac{\partial^2}{\partial A_{ij}\partial\bar A_{ij}}.
$$

**Harmonic functions.** A $C^2$ function is **harmonic** if

$$
\Delta f=0.
$$

**Theorem.** Every holomorphic function is harmonic:

$$
\Delta f=4\sum_{i,j}\frac{\partial}{\partial A_{ij}}\frac{\partial f}{\partial\bar A_{ij}}=0,
$$

because $\partial f/\partial\bar A_{ij}=0$. The real and imaginary parts of a holomorphic function are harmonic.

**The mean value property.** A harmonic function satisfies

$$
f(A)=\frac{1}{\lvert S^{31}\rvert}\int_{S^{31}}f(A+r u)\,du
=\frac{1}{\lvert B^{32}\rvert}\int_{B^{32}}f(A+r u)\,du
$$

for every ball of radius $r$ contained in its domain. The average over the sphere and over the ball are equal.

**The maximum principle.** A non-constant harmonic function on a bounded domain has no interior maximum or minimum. A harmonic function on a compact domain attains its extrema on the boundary.

**The Dirichlet problem.** On a ball, the Dirichlet problem for the Laplacian has a unique solution given by the Poisson integral. The Poisson kernel for the ball $B_R(0)\subset\mathbb{R}^{32}$ is

$$
P_R(A,u)=\frac{R^2-\lVert A\rVert^2}{\lvert S^{31}\rvert R\lVert A-Ru\rVert^{32}},
\qquad u\in S^{31},
$$

and the solution with boundary data $\varphi$ is

$$
f(A)=\int_{S^{31}}P_R(A,u)\varphi(Ru)\,du.
$$

**Pluriharmonic functions.** A function is **pluriharmonic** if its restriction to every complex line is harmonic. Holomorphic functions are pluriharmonic; pluriharmonic functions are harmonic. The real part of a holomorphic function is pluriharmonic, and every pluriharmonic function is locally the real part of a holomorphic function.

**The Laplacian of the norm.** For $A\ne0$,

$$
\Delta\lVert A\rVert=\frac{31}{\lVert A\rVert},
$$

the Euclidean formula in dimension $32$. The squared norm satisfies

$$
\Delta\lVert A\rVert^2=64.
$$

## The Functional Calculus

**The polynomial calculus.** For a polynomial $p(t)\in\mathbb{C}[t]$, the matrix $p(A)$ is defined by substitution. The map

$$
\mathbb{C}[t]\longrightarrow M_4,\qquad p\longmapsto p(A),
$$

is an algebra homomorphism, with kernel the ideal generated by the minimal polynomial $m_A$ and image the commutative algebra generated by $A$.

**The holomorphic calculus.** For $f$ holomorphic on an open set containing the spectrum of $A$,

$$
f(A)=\frac{1}{2\pi i}\oint_\gamma f(z)(zI-A)^{-1}\,dz,
$$

with $\gamma$ a contour enclosing the spectrum. The map is an algebra homomorphism and satisfies the spectral mapping theorem

$$
\sigma(f(A))=f(\sigma(A)).
$$

This is the Dunford calculus of *Spectral Theory and the Spectral Projectors of $M_4(\mathbb{C})$*.

**The normal case.** If $A$ is normal, $A=U\Lambda U^*$ with $\Lambda$ diagonal, and for every continuous (or bounded Borel) function $f$ on the spectrum,

$$
f(A)=U\operatorname{diag}(f(\lambda_1),\dots,f(\lambda_4))U^*.
$$

The map $f\mapsto f(A)$ is a $*$-homomorphism from the algebra of continuous functions on the spectrum to the $C^*$-algebra generated by $A$. The spectral measures $E_k$ are the projectors onto the eigenspaces, and

$$
A=\sum_{k=1}^{4}\lambda_kE_k .
$$

**The exponential and the logarithm.** The entire function $e^z$ gives the matrix exponential; the holomorphic logarithm on a domain avoiding the negative real axis gives the matrix logarithm. The resolvent, the spectral projectors, the fractional powers $A^s$ on the positive definite cone and the $*$-unitary group $e^{iK}$ are all instances of the functional calculus.

**The approximation.** By Runge's theorem and the density of polynomials, every holomorphic function on a neighbourhood of the spectrum is uniformly approximated by polynomials on the spectrum; hence the holomorphic calculus is the closure of the polynomial calculus. The finite dimension makes the calculus algebraic: $f(A)$ depends only on $f$ and its derivatives at the eigenvalues, through the Lagrange–Sylvester interpolation formula.

## The Gaussian Measure and the Heat Kernel

**The Gaussian measure.** The **Gaussian measure** on $M_4$ is

$$
d\mu(A)=\pi^{-16}e^{-\lVert A\rVert^2}\,dA.
$$

It is a probability measure, because

$$
\int_{M_4}e^{-\lVert A\rVert^2}\,dA=\pi^{16}.
$$

**The moments.** The entries are independent complex Gaussians with

$$
\mathbb{E}[A_{ij}]=0,\qquad
\mathbb{E}[A_{ij}\bar A_{kl}]=\delta_{ik}\delta_{jl},\qquad
\mathbb{E}[A_{ij}A_{kl}]=0.
$$

The **Wick formula** gives the expectation of a polynomial as the sum over pairings of the entries and their conjugates:

$$
\mathbb{E}\Bigl[\prod_{r=1}^{m}A_{i_rj_r}\prod_{s=1}^{n}\bar A_{k_sl_s}\Bigr]
=\sum_{\text{pairings}}\prod_{\text{pairs}}\delta_{i k}\delta_{j l},
$$

with the sum over the perfect pairings of the $m$ entries with the $n$ conjugates.

**The heat kernel.** The heat kernel of the Euclidean Laplacian on $\mathbb{R}^{32}$ is

$$
K_t(A,B)=(4\pi t)^{-16}e^{-\lVert A-B\rVert^2/(4t)},\qquad t>0.
$$

It satisfies the heat equation

$$
\frac{\partial K_t}{\partial t}=\Delta K_t,
\qquad
\lim_{t\to0^+}K_t(A,B)=\delta(A-B).
$$

The solution of the initial value problem $u(0,A)=u_0(A)$ is

$$
u(t,A)=\int_{M_4}K_t(A,B)u_0(B)\,dB.
$$

The Gaussian measure is the heat kernel at $t=\tfrac14$ from the origin:

$$
\pi^{-16}e^{-\lVert A\rVert^2}=K_{1/4}(A,0).
$$

## The Fourier Transform

**Definition.** For $f\in L^1(M_4)$, the **Fourier transform** is

$$
\hat f(\xi)=\int_{M_4}f(A)e^{-2\pi i\operatorname{Re}\operatorname{tr}(\xi^*A)}\,dA,
\qquad \xi\in M_4.
$$

The exponent is the Euclidean pairing of the real $32$-dimensional spaces; the transform is the ordinary Fourier transform on $\mathbb{R}^{32}$, written in matrix coordinates.

**Inversion and Plancherel.** For $f$ in the Schwartz class,

$$
f(A)=\int_{M_4}\hat f(\xi)e^{2\pi i\operatorname{Re}\operatorname{tr}(\xi^*A)}\,d\xi,
\qquad
\int_{M_4}\lvert f(A)\rvert^2\,dA=\int_{M_4}\lvert\hat f(\xi)\rvert^2\,d\xi .
$$

**Derivatives.** With the Wirtinger derivatives,

$$
\widehat{\frac{\partial f}{\partial A_{ij}}}(\xi)
=\pi i\,\overline{\xi_{ij}}\,\hat f(\xi),
\qquad
\widehat{\frac{\partial f}{\partial\bar A_{ij}}}(\xi)
=\pi i\,\xi_{ij}\,\hat f(\xi).
$$

The Laplacian is the multiplier $-4\pi^2\lVert\xi\rVert^2$:

$$
\widehat{\Delta f}(\xi)=-4\pi^2\lVert\xi\rVert^2\hat f(\xi).
$$

**The heat kernel.** The Fourier transform of the heat kernel is

$$
\widehat{K_t}(\xi)=e^{-4\pi^2t\lVert\xi\rVert^2},
$$

and the Gaussian $e^{-\pi\lVert A\rVert^2}$ is self-dual:

$$
\widehat{e^{-\pi\lVert A\rVert^2}}=e^{-\pi\lVert\xi\rVert^2}.
$$

**The convolution.** The convolution

$$
(f*g)(A)=\int_{M_4}f(A-B)g(B)\,dB
$$

satisfies $\widehat{f*g}=\hat f\hat g$. The algebra product is not translation-invariant, so the Fourier transform does not diagonalise the multiplication of matrices; the spectral theory, not the Fourier transform, is the diagonalisation of the algebra. The Fourier transform is the tool for the translation-invariant analysis: the Laplacian, the heat kernel and the Gaussian measure.

## The Differential Calculus

**The gradient.** For a real $C^1$ function $f$ on $M_4$, the gradient $\nabla f(A)$ is defined by

$$
d f_A(B)=\operatorname{Re}\operatorname{tr}(\nabla f(A)^*B).
$$

For the real function $\operatorname{Re}\det$, the gradient is $\nabla(\operatorname{Re}\det)(A)=\operatorname{adj}(A)^*$; the holomorphic derivative of the determinant itself is $d(\det)_A(B)=\operatorname{tr}(\operatorname{adj}(A)B)$. For $\operatorname{Re}\operatorname{tr}$, the gradient is $I$; for the squared norm, $\nabla\lVert A\rVert^2=2A$.

**The product.** The product map $(A,B)\mapsto AB$ is bilinear, and

$$
d(AB)_{(A,B)}(X,Y)=XB+AY.
$$

**The exponential.** The derivative of the exponential is

$$
d(\exp)_X(Y)=e^X\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+1)!}\operatorname{ad}_X^n(Y)
=e^X\frac{1-e^{-\operatorname{ad}_X}}{\operatorname{ad}_X}(Y),
$$

the formula of *The Exponential and the Lie Group of $M_4(\mathbb{C})$*.

**The Hessian.** The Hessian is the second derivative; at a critical point it determines the local behaviour. For the squared norm, the Hessian is the identity (times $2$); for the determinant, the Hessian at $I$ is

$$
\frac{d^2}{dt^2}\Big|_{t=0}\det(I+tB)=\operatorname{tr}(B)^2-\operatorname{tr}(B^2),
$$

the second coefficient of the characteristic polynomial.

**The critical points of the determinant.** The gradient $\operatorname{adj}(A)^*$ of $\operatorname{Re}\det$ vanishes exactly when $\operatorname{adj}(A)=0$, that is, when $\operatorname{rank}A\le2$. The critical set of the determinant is therefore the variety of rank at most two, of complex dimension $12$; it is the singular locus of the hypersurface $\det=0$.

**The $*$-unitary group.** The modulus $\lvert\det\rvert$ is identically $1$ on $U(4)$, so it has no distinguished critical point there; the closest-$*$-unitary problem of *The Polar Decomposition of $M_4(\mathbb{C})$* is the variational problem for the Frobenius distance to $U(4)$.

**The inverse and implicit function theorems.** The inverse function theorem applies to the holomorphic maps with invertible differential: the exponential near $0$, the inverse on $GL_4$, the resolvent off the spectrum. The implicit function theorem gives the local manifold structure of the level sets $\{\det=c\}$ and of the spectral strata.

## The Biquaternion Case

**At $n=2$ the analysis is the same in four complex variables.** The biquaternion algebra is $M_2(\mathbb{C})\cong\mathbb{C}^4$; the Hilbert space has complex dimension $4$ and real dimension $8$; the Gaussian measure is

$$
d\mu(A)=\pi^{-4}e^{-\lVert A\rVert^2}\,dA,
$$

and the heat kernel is $(4\pi t)^{-4}e^{-\lVert A-B\rVert^2/(4t)}$. The holomorphic functions are the entire functions of four complex variables, and the functional calculus is the same.

**The comparison.** The full algebra has sixteen complex variables; the biquaternion algebra has four. The positive definite Frobenius form is the same in both cases. The biquaternion norm $N(\tilde Q)=Q_t^2+B^2$ is a different, complex-valued object; the analysis of its null cone is not the analysis of the positive definite Hilbert space.

## Zero Divisors and the Boundary against Fueter Theory

**The zero divisors.** The full matrix algebra is not a division algebra. An element $A$ is a zero divisor exactly when it is singular: if $A$ is singular, choose a nonzero $B$ with $\operatorname{im}B\subseteq\ker A$, and then $AB=0$. The zero divisors are the singular set

$$
\{A:\det A=0\},
$$

a complex hypersurface of real codimension two. What is absent in the full algebra is a **null cone** of its positive definite trace form: the trace form $\langle A,B\rangle=\operatorname{tr}(A^*B)$ is positive definite, so its only isotropic vector is $0$. The singular set is the determinantal hypersurface, not the isotropic cone of a form. The biquaternion algebra, by contrast, has the complex-valued norm and its null cone.

**The ordinary matrix analysis.** Because the algebra is a full matrix algebra, the analysis of its elements is the ordinary matrix analysis: rank, determinant, characteristic polynomial, Jordan form, spectral projectors, singular values, polar decomposition and the Schatten norms. The Frobenius form is definite; the operator and nuclear norms are the Schatten norms; the exponential and the logarithm are the matrix functions. There is no division-algebra norm and no null cone to divide by.

**The boundary against Fueter theory.** Fueter's quaternionic analysis uses the Cauchy–Fueter operator and the quaternionic multiplication; it requires a quaternionic structure on the space. The full algebra $M_4(\mathbb{C})$ has the complex structure of $\mathbb{C}^{16}$ and the ordinary Cauchy–Riemann equations; it does not carry a complex-linear quaternionic structure; the quaternionic structure of the regular model is real-linear and lives on the biquaternion subalgebra. The biquaternion algebra $\mathbb{B}$ carries the quaternionic structure, and its regular model $M_4(\mathbb{C})_{\mathbb{B},L}$ carries the Fueter theory; the full algebra's analysis is the ordinary several-complex-variable analysis. The two analyses meet through the biquaternion subalgebra and the regular representation. The positive definite Frobenius form does not produce a Cauchy–Fueter operator; the Fueter operator needs the quaternionic units, not the complex structure. This is the boundary between the ordinary matrix analysis of the full algebra and the quaternionic analysis of the biquaternion algebra.

## Summary

The algebra $M_4(\mathbb{C})$ is a complex Hilbert space of dimension $16$ with the Frobenius form $\langle A,B\rangle=\operatorname{tr}(A^*B)$ and the Lebesgue measure on $\mathbb{R}^{32}$. The holomorphic functions are the entire functions of the sixteen complex coordinates, characterised by the Cauchy–Riemann equations $\partial f/\partial\bar A_{ij}=0$; the real-analytic functions are the convergent series in the thirty-two real coordinates. The Wirtinger derivatives give the complex differential, the derivative of the determinant $d(\det)_A(B)=\operatorname{tr}(\operatorname{adj}(A)B)$ and the derivative of the inverse $d(A^{-1})_A(B)=-A^{-1}BA^{-1}$. The Laplacian is $\Delta=4\sum\partial^2/\partial A_{ij}\partial\bar A_{ij}$; the holomorphic functions are harmonic, with the mean value property, the maximum principle and the Poisson integral. The functional calculus is the polynomial, holomorphic and normal $C^*$-calculus; the Gaussian measure $\pi^{-16}e^{-\lVert A\rVert^2}dA$ has the Wick moments, and the heat kernel is $(4\pi t)^{-16}e^{-\lVert A-B\rVert^2/(4t)}$. The Fourier transform on $\mathbb{C}^{16}$ converts the Wirtinger derivatives into multiplication by $\pi i\bar\xi_{ij}$ and the Laplacian into $-4\pi^2\lVert\xi\rVert^2$; it diagonalises the translation-invariant analysis but not the algebra product. The full algebra has the ordinary zero divisors of the singular set, not a null cone; its analysis is the ordinary matrix analysis, and the boundary against Fueter theory is the quaternionic structure carried by the biquaternion algebra and its regular model. The critical set of the determinant is the rank-at-most-two variety, and the closest-$*$-unitary problem for the Frobenius distance is the variational problem of the polar decomposition.

$$
\boxed{\ \dim_\mathbb{C}M_4=16,\quad \langle A,B\rangle=\operatorname{tr}(A^*B),\quad \Delta=4\sum_{i,j}\partial_{A_{ij}}\partial_{\bar A_{ij}},\quad d\mu=\pi^{-16}e^{-\lVert A\rVert^2}dA. }
$$

| Object | Formula |
|---|---|
| Hilbert norm | $\lVert A\rVert^2=\sum_{i,j}\lvert A_{ij}\rvert^2$ |
| Wirtinger derivative | $\partial_{\bar A_{ij}}=\frac12(\partial_{x_{ij}}+i\partial_{y_{ij}})$ |
| Laplacian | $\Delta=4\sum\partial_{A_{ij}}\partial_{\bar A_{ij}}$ |
| Gaussian measure | $\pi^{-16}e^{-\lVert A\rVert^2}dA$ |
| Heat kernel | $(4\pi t)^{-16}e^{-\lVert A-B\rVert^2/(4t)}$ |
| Gradient of $\operatorname{Re}\det$ | $\operatorname{adj}(A)^*$ |
| Gradient of $\operatorname{tr}$ | $I$ |
| Fourier transform | $\hat f(\xi)=\int f(A)e^{-2\pi i\operatorname{Re}\operatorname{tr}(\xi^*A)}dA$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle A,B\rangle=\operatorname{tr}(A^*B)$ | the Frobenius inner product |
| $\partial_{A_{ij}},\partial_{\bar A_{ij}}$ | the Wirtinger derivatives |
| $\Delta$ | the Euclidean Laplacian on $\mathbb{R}^{32}$ |
| $d\mu$ | the Gaussian probability measure |
| $K_t(A,B)$ | the heat kernel |
| $f(A)$ | the functional calculus |
| $\operatorname{adj}(A)$ | the adjugate; $\operatorname{adj}(A)^*$ is the gradient of $\operatorname{Re}\det$ |

## Further Reading

- [The Sylvester Operator and the Kronecker Sum of $M_4(\mathbb{C})$](the-sylvester-operator-and-the-kronecker-sum-of-m4c.html), for the contour integral for the Sylvester equation.
- Walter Rudin, *Function Theory in the Unit Ball of $\mathbb{C}^n$* (Springer, 1980), for holomorphic functions, the Cauchy–Riemann equations, harmonic functions and the Poisson integral in several variables.
- Lars Hörmander, *An Introduction to Complex Analysis in Several Variables* (North-Holland, 1990), for the several-variable Cauchy–Riemann theory.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the functional calculus, the derivative of the determinant and the matrix exponential.
- Gerald B. Folland, *Real Analysis* (Wiley, 1999), for the Fourier transform, the Gaussian measure, the heat kernel and the Laplacian.
- Rudolf Fueter and the quaternionic analysis tradition, for the Cauchy–Fueter operator; see the biquaternion corpus for the regular model.
- [The Involution and the Hermitian Structure of $M_4(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m4c.html), for the Frobenius form.
- [Spectral Theory and the Spectral Projectors of $M_4(\mathbb{C})$](spectral-theory-and-the-spectral-projectors-of-m4c.html), for the Dunford calculus.
- [The Exponential and the Lie Group of $M_4(\mathbb{C})$](the-exponential-and-the-lie-group-of-m4c.html), for the matrix exponential.
- [The Geometry of the Idempotents of $M_4(\mathbb{C})$](the-geometry-of-the-idempotents-of-m4c.html), for the critical sets and the spectral strata.
