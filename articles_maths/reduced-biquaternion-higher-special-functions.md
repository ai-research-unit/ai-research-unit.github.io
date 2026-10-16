# __Reduced Biquaternion Higher Special Functions__

## Introduction

This article records the higher special functions of a reduced biquaternion variable: the Bessel functions, the orthogonal polynomials, the hypergeometric function, the Gamma function and the Zeta function. The structural fact governing all of them is again the idempotent decomposition, and the general principle is stated once and used throughout: a special function defined by a power series with non-zero radius of convergence, or by an integral of a holomorphic kernel, extends to the reduced biquaternion algebra coefficientwise, so that the reduced biquaternion special function is the pair of the ordinary complex special functions of the two idempotent coordinates. Because the algebra is commutative, the functional equations and the recurrence relations of the complex theory hold in the algebra without ordering corrections. The treatment is purely mathematical.

Throughout the element is $T=A+Bj$ with $A=a+ia'$, $B=b+ib'$, the idempotent coordinates are $q_1=A+B$, $q_2=A-B$, and $T=q_1\Pi_{1}+q_2\Pi_{2}$ with $\Pi_{1,2}=\tfrac12(1\pm j)$. The basis is $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$ and $ji=ij$.

## Bessel Functions

**Definition.** For a complex order $\nu$ the **Bessel function** of the reduced biquaternion variable is
$$
J_{\nu}(T)=J_{\nu}(q_1)\,\Pi_{1}+J_{\nu}(q_2)\,\Pi_{2},
$$
with $J_{\nu}$ the ordinary Bessel function of the first kind on the two coordinates.

**Theorem (the equation and the series).** The function $J_{\nu}(T)$ satisfies the **reduced Bessel equation**
$$
T^{2}F''+TF'+(T^{2}-\nu^{2})F=0,
$$
the products and the second derivative being taken in the algebra; and it has the power series
$$
J_{\nu}(T)=\sum_{n\ge0}\frac{(-1)^{n}}{n!\,\Gamma(n+\nu+1)}\Bigl(\frac{T}{2}\Bigr)^{2n+\nu},
$$
convergent for all $T$ when $\nu$ is an integer and on a disc in each coordinate otherwise.

*Proof.* In the first idempotent coordinate the equation is $q_1^{2}J_{\nu}''+uJ_{\nu}'+(q_1^{2}-\nu^{2})J_{\nu}=0$, which holds classically, and symmetrically in the second; the operator $T\mapsto T^{2}$ acts coefficientwise, so the equation holds on the algebra as the pair of its coordinate equations. The series is the ordinary one in each coordinate, and the powers $(T/2)^{2n+\nu}$ are read as $q_1^{2n+\nu}\Pi_{1}+q_2^{2n+\nu}\Pi_{2}$.

**Corollary (the modified function and the second solution).** The modified Bessel function, $I_{\nu}(T)=I_{\nu}(q_1)\Pi_{1}+I_{\nu}(q_2)\Pi_{2}$, satisfies $T^{2}F''+TF'-(T^{2}+\nu^{2})F=0$, and the second solution of the Bessel equation is the pair of the ordinary second solutions, with the same branch considerations in each coordinate.

*Proof.* The sign change in the equation and in the series is coordinatewise, and the independence of the two solutions is coordinatewise.

## Orthogonal Polynomials

**Definition.** The **Legendre polynomials** of the reduced biquaternion variable are $P_{n}(T)=P_{n}(q_1)\Pi_{1}+P_{n}(q_2)\Pi_{2}$, and the **Hermite polynomials** are $H_{n}(T)=H_{n}(q_1)\Pi_{1}+H_{n}(q_2)\Pi_{2}$, with the ordinary polynomials of the two coordinates.

**Theorem (generating functions and recurrences).** The generating functions
$$
(1-2Tz+z^{2})^{-1/2}=\sum_{n\ge0}P_{n}(T)z^{n},\qquad
e^{2Tz-z^{2}}=\sum_{n\ge0}\frac{H_{n}(T)}{n!}z^{n}
$$
hold wherever the left sides are defined, and the three-term recurrences of the complex theory hold coefficientwise, with the same coefficients.

*Proof.* Each identity is proved in each idempotent coordinate by the classical generating-function argument, and the algebra being commutative, the powers and products reassemble without ordering corrections. The radius of the first series is governed by the nearest singularity of the square root, that is by the points where $1-2uz+z^{2}$ or $1-2vz+z^{2}$ vanishes.

**Corollary (Chebyshev and the weight functions).** The Chebyshev polynomials of the first kind, written $\mathrm{C}_{n}$ to avoid the clash with the element glyph $T$, extend as $\mathrm{C}_{n}(T)=\mathrm{C}_{n}(q_1)\Pi_{1}+\mathrm{C}_{n}(q_2)\Pi_{2}$, satisfy the same second-order equation in each coordinate, and their orthogonality relations hold on a product of the two one-variable intervals, the reduced biquaternion orthogonality being the product of the two classical orthogonality statements.

*Proof.* The Chebyshev equation and the orthogonality are coordinatewise, and the bilinear form on the algebra is the sum of the two coordinate bilinear forms.

## Hypergeometric Function

**Definition.** The **hypergeometric function** of the reduced biquaternion variable is
$$
{}_{2}F_{1}(a,b;c;T)={}_{2}F_{1}(a,b;c;q_1)\,\Pi_{1}+{}_{2}F_{1}(a,b;c;q_2)\,\Pi_{2},
$$
the parameters $a,b,c$ being complex and not a pole of the denominators.

**Theorem (the series and the equation).** The series
$$
{}_{2}F_{1}(a,b;c;T)=\sum_{n\ge0}\frac{(a)_{n}(b)_{n}}{(c)_{n}\,n!}\,T^{n},
$$
with the Pochhammer symbols, converges for $\lvert q_1\rvert<1$ and $\lvert q_2\rvert<1$, and the function satisfies the reduced hypergeometric equation
$$
T(1-T)F''+\bigl(c-(a+b+1)T\bigr)F'-ab\,F=0
$$
as the pair of its coordinate equations. The transformation formulas of the complex theory hold coordinatewise.

*Proof.* The equation and the series are the classical ones in each coordinate, read on the algebra through the idempotents; the convergence domain is the product of the two discs, a polydisc in the two complex coordinates.

## The Gamma Function

**Definition.** The **Gamma function** of the reduced biquaternion variable is
$$
\Gamma(T)=\Gamma(q_1)\,\Pi_{1}+\Gamma(q_2)\,\Pi_{2},
$$
defined on the elements whose two coordinates avoid the non-positive integers.

**Theorem (the functional equation and the reflection).** The reduced Gamma satisfies
$$
\Gamma(T+1)=T\,\Gamma(T),\qquad \Gamma(T)\Gamma(1-T)=\frac{\pi}{\sin(\pi T)},
$$
the sine being the reduced sine of the elementary functions, and its poles are the elements with a coordinate at a non-positive integer.

*Proof.* Both identities are classical in each coordinate and hold on the algebra because the multiplication is componentwise; the poles are the union of the two families of coordinate conditions.

**Corollary (the Beta integral and the Stirling form).** The Beta function extends as $\mathrm{B}(T,W)=\mathrm{B}(q_1,w)\Pi_{1}+\mathrm{B}(q_2,w')\Pi_{2}$, where $W=w\Pi_{1}+w'\Pi_{2}$ and $\mathrm{B}$ is the ordinary Beta function, with the classical integral representation in each coordinate, and the Stirling asymptotic expansion of the Gamma function holds coefficientwise with the same coefficients.

*Proof.* The Beta integral is a one-variable integral in each coordinate, and the asymptotic expansion is a one-variable asymptotic expansion in each coordinate.

## The Zeta Function

**Definition.** The **Zeta function** of the reduced biquaternion variable is
$$
\zeta(T)=\zeta(q_1)\,\Pi_{1}+\zeta(q_2)\,\Pi_{2},
$$
defined for $\operatorname{Re}q_1>1$ and $\operatorname{Re}q_2>1$ and continued meromorphically coordinatewise.

**Theorem (the series and the zeros).** The Dirichlet series $\zeta(T)=\sum_{n\ge1}n^{-T}$, with $n^{-T}=n^{-q_1}\Pi_{1}+n^{-q_2}\Pi_{2}$, converges for $\operatorname{Re}q_1>1$ and $\operatorname{Re}q_2>1$; the functional equation holds coordinatewise; the element $\zeta(T)$ is a zero divisor exactly on the union of the two families of complex lines $\{q_1=\rho\}$ and $\{q_2=\rho\}$ for the zeros $\rho$ of the ordinary Zeta function; and $\zeta(T)=0$ exactly when both coordinates are ordinary zeros, that is on the coordinatewise product of the ordinary zero set with itself.

*Proof.* The series splits in the two coordinates into the two ordinary Dirichlet series, each convergent in its half-plane; the functional equation is coordinatewise; an idempotent combination $g_{1}(q_1)\Pi_{1}+g_{2}(q_2)\Pi_{2}$ is zero exactly when both components vanish, so the zeros are the coordinatewise product of the two ordinary zero sets, and it is a zero divisor as soon as one component vanishes, which is the union of the two families of complex lines.

**Corollary (the Euler product).** The Euler product
$$
\zeta(T)=\prod_{p}\bigl(1-p^{-T}\bigr)^{-1}
$$
holds in the region of convergence, the product over the primes, each factor defined by the geometric series $1+p^{-T}+p^{-2T}+\cdots$ in the algebra.

*Proof.* Each factor is the geometric series in the algebra, convergent because $p^{-q_1}$ and $p^{-q_2}$ have modulus less than one in the region, and the product reassembles the Dirichlet series by unique factorisation of the integers.

## Special Functions from the Analysis

**The Cauchy kernel.** The kernel $G(T)=(2\pi i)^{-1}(\Pi_{1}/q_1+\Pi_{2}/q_2)$ of *Reduced Biquaternion Integration* is the pair of the one-variable kernels, and its powers $G^{n}$ are the pairs of the powers.

**The fundamental solution.** The function $1/(\pi q_1)\Pi_{1}+1/(\pi q_2)\Pi_{2}$ is the pair of the one-variable fundamental solutions of the two Cauchy–Riemann operators, and it is the special function at the root of the integral theory.

**The exponential family.** The exponentials, the trigonometric and the hyperbolic functions of *Reduced Biquaternion Elementary Functions* are the first members of the family, and every one of them is the coefficientwise extension of its complex prototype.

## The General Principle

**Theorem (the extension principle).** Let $F$ be a complex function defined on a domain of $\mathbb{C}$ by a power series with a non-zero radius of convergence, or by an integral of the form $F(z)=\int K(z,w)\,g(w)\,\mathrm{d}w$ with a holomorphic kernel. Then there is a unique extension to the reduced biquaternion algebra given by
$$
F(T)=F(q_1)\,\Pi_{1}+F(q_2)\,\Pi_{2},
$$
it is defined on the elements whose two coordinates lie in the domain of $F$, it commutes with the pointwise operations and with the two-factor differentiation, and every functional equation, recurrence and series representation of $F$ holds on the algebra coefficientwise.

*Proof.* Each coordinate is a complex number in the domain of $F$, so the values $F(q_1)$ and $F(q_2)$ are defined; a convergent series is evaluated in each coordinate termwise; a holomorphic integral is evaluated coordinatewise; the identities of the one-variable theory hold in each coordinate because the algebra is commutative and the multiplication is componentwise, and they reassemble in the algebra. The uniqueness is the fact that a function on the algebra is determined by its two coordinate functions.

**Corollary (limits of the principle).** The principle fails only where a coordinate leaves the domain of the one-variable function: for the logarithm and the powers at a vanishing coordinate, for the Gamma function at a non-positive integer coordinate, for the hypergeometric function outside the polydisc, and generally where the algebra element is not a unit. These are the places where the special function is singular, and they are unions of coordinate conditions rather than a single hypersurface.

*Proof.* Each failure is the failure of the one-variable prototype in one of the coordinates; the corresponding set in the algebra is the union of the two coordinate conditions, which is the reason the singular sets of the reduced biquaternion special functions are unions of complex lines rather than hypersurfaces.

## Summary

The higher special functions of a reduced biquaternion variable are the coefficientwise extensions of the complex special functions to the two idempotent coordinates. The Bessel functions $J_{\nu}(T)=J_{\nu}(q_1)\Pi_{1}+J_{\nu}(q_2)\Pi_{2}$ satisfy the reduced Bessel equation componentwise, with the modified function and the second solution obtained by the same sign changes as in the complex case. The Legendre and Hermite polynomials and the Chebyshev polynomials have their generating functions and three-term recurrences coordinatewise, and their orthogonality is the product of the two one-variable statements. The hypergeometric function is the pair of the hypergeometric functions on the polydisc $\lvert q_1\rvert<1$, $\lvert q_2\rvert<1$, and its transformation formulas hold coordinatewise. The Gamma function extends off the elements with a non-positive integer coordinate and satisfies the functional equation and the reflection formula; the Zeta function is the pair of the ordinary Zeta functions, with the Euler product in the region of convergence and the zero divisors forming the union of the two families of complex lines through the ordinary zeros, the element itself vanishing only where both coordinates are ordinary zeros. The Cauchy kernel and the fundamental solution of the analysis are the corresponding pairs. The general principle is that any function defined by a power series with a non-zero radius, or by a holomorphic integral, extends coordinatewise and preserves every functional equation, the only failures being where a coordinate leaves the domain of the one-variable prototype.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J_{\nu}(T)=J_{\nu}(q_1)\Pi_{1}+J_{\nu}(q_2)\Pi_{2}$ | Bessel function |
| $I_{\nu}(T)$ | Modified Bessel function |
| $P_{n}(T),\ H_{n}(T),\ \mathrm{C}_{n}(T)$ | Legendre, Hermite and Chebyshev polynomials |
| ${}_{2}F_{1}(a,b;c;T)$ | Hypergeometric function |
| $(a)_{n}$ | Pochhammer symbol |
| $\Gamma(T)=\Gamma(q_1)\Pi_{1}+\Gamma(q_2)\Pi_{2}$ | Gamma function |
| $\mathrm{B}(T,W)$ | Beta function |
| $\zeta(T)=\zeta(q_1)\Pi_{1}+\zeta(q_2)\Pi_{2}$ | Zeta function |
| $q_1=A+B$, $q_2=A-B$ | Idempotent coordinates |

## Further Reading

- G. N. Watson, *A Treatise on the Theory of Bessel Functions*, 2nd edition (Cambridge University Press, 1944), for the Bessel functions, their equations and their series.
- Earl D. Rainville, *Special Functions* (Macmillan, 1960), for the hypergeometric function, the orthogonal polynomials and their generating functions.
- E. T. Whittaker and G. N. Watson, *A Course of Modern Analysis*, 4th edition (Cambridge University Press, 1927), for the Gamma function, the Zeta function and the analytic continuation.
- G. Baley Price, *An Introduction to Multicomplex Spaces and Functions* (Marcel Dekker, 1991), for the extension of the special functions to the multicomplex algebra.
- M. Elena Luna-Elizarrarás, Michael Shapiro, Daniele C. Struppa and Adrian Vajiac, *Bicomplex Holomorphic Functions* (Birkhäuser, 2015), for the idempotent reduction of the analytic functions of the commutative algebra.
