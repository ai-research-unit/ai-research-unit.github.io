
# __Octonion Integration__

## Introduction

This article is the integration slot of the octonion system. It treats the integration of octonion-valued functions: the boundary integrals of hypercomplex analysis, the Stokes and divergence theorems for the octonionic Cauchy–Riemann operator, the Cauchy integral theorem and its invariance under deformation of the contour, the jump formulas for the boundary values of the Cauchy integral, and the exact places where non-associativity changes the classical theory.

The article is the octonion member of the integration slots of this Part and follows the model of the *Quaternion Integration* and *Split-Biquaternion Integration*, together with the Cauchy theory of *Clifford Modules and the Twisted Cauchy–Riemann Operator*. It takes the operator $D$, the kernel $E$, the monogenic class and the Cauchy–Pompeiu formula from *Octonion Analysis* and does not repeat them; the object here is the integral as an operation. The harmonic analysis on $\mathbb{O}$ is the subject, and the functions of the next slot.

**Conventions.** As in *Octonion Analysis*: $\mathbb{O}$ with basis $e_0,\dots,e_7$, variable $x = \sum_kx_ke_k$, partial derivatives $\partial_k$, conjugation $\bar\cdot$, inner product $\langle x,y\rangle = \operatorname{Sc}(x\bar y)$, norm $\lvert x\rvert^2 = x\bar x$; the Cauchy–Riemann operator is $D = \sum_{k=0}^{7}e_k\partial_k$ and its conjugate $\bar D = \partial_0 - \sum_{k\geq1}e_k\partial_k$, with $D\bar D = \bar DD = \Delta_8$; the kernel is $E(x) = \bar x/(\omega_7\lvert x\rvert^8)$, $\omega_7 = \operatorname{vol}S^7 = \pi^4/3$; $\mathcal{M}_L$ and $\mathcal{M}_R$ are the left- and right-monogenic classes. Integrals are taken with respect to the Euclidean volume and surface measures $dV$ and $dS$, and a domain is a bounded connected open set with smooth boundary, oriented as the boundary of the domain, with outward unit normal $n$.

## Integrals of Octonion-Valued Functions

### The Integral and its Elementary Properties

**Definition.** Let $f : \Omega\to\mathbb{O}$ be continuous and integrable on a domain $\Omega$; the **integral** $\int_\Omega f\,dV$ is the octonion whose components are the eight real integrals of the components of $f$ in the basis $e_0,\dots,e_7$. For a surface $\Sigma$ with a chosen orientation and a continuous integrand, $\int_\Sigma f\,dS$ is defined similarly componentwise.

**Proposition.** The integral is $\mathbb{R}$-linear but not $\mathbb{O}$-linear: for a constant octonion $a$,

$$
\int_\Omega af\,dV = a\int_\Omega f\,dV, \qquad \int_\Omega fa\,dV = \left(\int_\Omega f\,dV\right)a ,
$$

so that multiplication by a constant commutes with integration exactly as it commutes with any finite sum, and there is no difficulty of associativity because no product of two variable octonions occurs. In particular the integral of a product is not computable from the integrals of the factors: $\int fg \neq \left(\int f\right)\left(\int g\right)$ in general, and not only because of the inequality of the moduli.

*Proof.* Both identities are the linearity of the componentwise integral with respect to scalar multiplication on the left and on the right, and the multiplication by a constant is a linear map of $\mathbb{O}$. $\square$

**Remark.** The distinction between the two displayed identities matters: because $\mathbb{O}$ is not commutative, the position of the constant relative to the integrand is part of the statement of the integral, and an integral is a sum of values of the function, so a change of the order of the factors inside the integrand changes the value of the integral. This is the first place where the non-commutativity of the octonions appears in integration, before any question of associativity.

### The Divergence Theorem and the Operator $D$

**Theorem (divergence theorem).** Let $\Omega$ be a domain with smooth boundary and $f$ a $C^1$ octonion-valued function on $\bar\Omega$. Then

$$
\int_{\partial\Omega}n(y)f(y)\,dS(y) = \int_\Omega \left(\bar D f\right)(y)\,dV(y), \qquad\text{where } \bar D = \partial_0 - \sum_{k\geq1}e_k\partial_k ,
$$

and, with the operator acting from the right,

$$
\int_{\partial\Omega}f(y)n(y)\,dS(y) = \int_\Omega (fD)(y)\,dV(y) .
$$

*Proof.* The first identity is the classical divergence theorem applied to the eight real components of $f$: the normal component $n_kf$ has divergence $\partial_kf$, and assembling the eight identities with the basis elements and the signs of $\bar D$ gives the display. The order of the factors is the order of the multiplication by the constant basis elements in the assembly. The second identity is the same statement with the roles of the basis elements reversed, that is, it is the first identity applied to the conjugate function and conjugated back, using the conjugacy $\overline{Df} = \bar fD$ of *Octonion Analysis*. $\square$

The divergence theorem is the fundamental integration identity of the octonionic calculus, and it is the form in which the operator meets the integral. Its content is the same as in the real case: what is new is only the bookkeeping of the order of the factors, fixed by the position of $\bar D$ or of $D$ in the identity.

**Corollary (Green's identity).** Let $u$ be real-valued of class $C^1$ and $v$ octonion-valued of class $C^1$ on $\bar\Omega$. Then

$$
\int_{\partial\Omega}u(y)\,n(y)\,v(y)\,dS(y) = \int_\Omega\left[(\bar Du)(y)\,v(y) + u(y)\,(\bar Dv)(y)\right]dV(y) ,
$$

with the multiplication by the scalar $u$ on the left of $v$ in both terms.

*Proof.* Apply the divergence theorem to the product $uv$ and use $\bar D(uv) = (\bar Du)v + u(\bar Dv)$. The product rule in this form holds because $u$ and its partial derivatives are real scalars, hence central and associative with everything. $\square$

**Remark.** For octonion-valued $u$ the same computation acquires associator corrections: the difference between $\bar D(uv)$ and $(\bar Du)v + u(\bar Dv)$ is a sum of terms each of which is an associator with one factor $e_k$ or $\bar e_k$, exactly as in the product rule of *Octonion Analysis* for $D$ in place of $\bar D$, and it vanishes identically only in the associative case. The classical Green identity in its displayed form is therefore a statement about a scalar weight; for two octonion-valued functions it holds only up to those correction terms.

## The Cauchy Integral Theorem

**Theorem (Cauchy integral theorem).** Let $f$ be left-monogenic on a domain $\Omega$ containing a closed hypersurface $\Sigma$ bounding a domain $\Omega_\Sigma$, and let $x\notin\bar\Omega_\Sigma$. Then

$$
\int_\Sigma \frac{\overline{y - x}}{\lvert y - x\rvert^8}\,n(y)\,f(y)\,dS(y) = 0 ,
$$

and more generally the integral $\int_\Sigma K_x(y)\,n(y)f(y)dS(y)$ depends only on the homology class of $\Sigma$ in $\Omega\setminus\{x\}$, where $K_x(y) = \overline{y-x}/\lvert y-x\rvert^8$ and $n$ is the outer normal of the region bounded.

*Proof.* The integrand is $E(y-x)n(y)f(y)$, and its divergence with respect to $y$ is computed by the product rule; for $y\neq x$ the kernel is monogenic on both sides, and the terms combine to a divergence, so Stokes' theorem makes the integral depend only on the homology class. The argument is the standard one of the Cauchy theory of the octonionic operator, with the sources cited; the cancellations happen before any product of two monogenic functions is formed. $\square$

**Corollary.** The kernel is normalised by the sphere: for every $r>0$,

$$
\frac{1}{\omega_7}\int_{\lvert y\rvert = r}\frac{\bar y}{r^8}\,\frac{y}{r}\,dS(y) = e_0 ,
$$

so that the integral of the kernel against the outer normal over a sphere is the identity, independently of the radius.

*Proof.* Apply the Cauchy integral formula of *Octonion Analysis* to the constant function $f = e_0$ and $x = 0$; the left side is the displayed integral. Alternatively, compute it directly: $\bar yy = r^2$, so the integrand is $r^{-7}e_0dS$ and the integral is $\omega_7r^7\cdot r^{-7}e_0 = \omega_7e_0$. $\square$

The corollary exhibits the sphere as the cycle that detects the singularity of the kernel, in exact analogy with the complex and quaternionic cases; it is the source of the Cauchy formula and of the "winding" of a general cycle relative to a point.

**Theorem (homology form of the Cauchy formula).** Let $f$ be left-monogenic on a domain $\Omega$, let $x\in\Omega$, and let $\Sigma\subset\Omega\setminus\{x\}$ be a closed oriented hypersurface homologous in $\Omega\setminus\{x\}$ to a small sphere around $x$ with the linking orientation. Then

$$
f(x) = \frac{1}{\omega_7}\int_\Sigma E(y-x)\,n(y)\,f(y)\,dS(y) .
$$

*Proof.* The difference of the two cycles is a boundary in $\Omega\setminus\{x\}$, and the Cauchy integral over a boundary is zero by the Cauchy integral theorem; hence the integrals over $\Sigma$ and over the small sphere agree, and the latter equals $f(x)$ by the Cauchy formula on a ball. $\square$

The homology form is the reason why the Cauchy integral is a topological object in the octonionic case as in the associative cases: the value at a point is determined by a cycle up to homology, and the entire dependence on the function is through its boundary values on that cycle.

## Boundary Values and Jump Formulas

**Definition.** Let $\Sigma$ be a closed hypersurface bounding a domain $\Omega$ with outward normal $n$ and let $f$ be a Hölder-continuous $\mathbb{O}$-valued function on $\Sigma$. The **Cauchy integral operator** is

$$
(\mathcal{C}f)(x) = \frac{1}{\omega_7}\int_\Sigma E(y-x)\,n(y)\,f(y)\,dS(y), \qquad x\notin\Sigma .
$$

**Theorem (jump formulas).** The function $\mathcal{C}f$ is left-monogenic on the complement of $\Sigma$, vanishes at infinity, and has boundary values from the two sides related by

$$
(\mathcal{C}f)^+(z) = \tfrac12 f(z) + (\mathcal{C}f)(z), \qquad (\mathcal{C}f)^-(z) = -\tfrac12 f(z) + (\mathcal{C}f)(z), \qquad z\in\Sigma ,
$$

where the integrals are principal values and $(\mathcal{C}f)^\pm$ denote the limits from outside and from inside; hence $(\mathcal{C}f)^+ - (\mathcal{C}f)^- = f$.

*Proof.* The standard Plemelj–Sokhotski argument: the singular integral with the kernel $E(y-x)$ has a principal value, and the difference of the two boundary values is the integral of the kernel over an infinitesimal sphere, which is the identity by the normalisation corollary. The monogenicity away from $\Sigma$ is the monogenicity of the kernel composed with the function. The argument uses the associativity of the triple products involved only in the order in which they are written. $\square$

The jump formulas are the boundary-value theory of the octonionic Cauchy integral, and they are the exact analogues of the complex ones, because the singularity of the kernel is detected by the sphere and the sphere integral is a scalar multiple of the identity; what fails in the octonionic case, and fails also for the quaternions, is the possibility of iterating the operator to obtain a product formula for boundary values, since the composition of two Cauchy integrals would require the product of two monogenic functions, which need not be monogenic.

### The Composition and its Failure

**Theorem.** The composition of the Cauchy integral operator with itself does not have the classical form: for $f$ continuous on $\Sigma$, the iterated integral

$$
(\mathcal{C}\mathcal{C}f)(x) = \frac{1}{\omega_7^2}\int_\Sigma E(y-x)n(y)\left(\int_\Sigma E(z-y)n(z)f(z)dS(z)\right)dS(y)
$$

is not in general equal to $\mathcal{C}f$ or to a constant multiple of $f$, and there is no identity of the form $\mathcal{C}^2 = \mathcal{C}$.

*Proof.* The classical proof of the idempotence of the Cauchy transform uses the associativity of the product of the kernel with the function to interchange the order of the two integrations and identify a composition kernel; in the octonionic case the interchange produces associator terms $[E(y-x),n(y),E(z-y)]$, which do not vanish identically, and the composition kernel is not the single kernel. Hence no such identity holds; the failure is the same as the failure of the product of monogenic functions to be monogenic, transferred to the level of the integral. $\square$

This is the integration-theoretic face of the failure of the Leibniz rule of *Octonion Analysis*: the Cauchy integral is a good operator, but it is not an idempotent projector, and the space of boundary values is not an algebra of holomorphic-type functions in the sense of the complex theory. The harmonic analysis takes the place of the missing function algebra in the spectral description.

## Integrals on the Sphere and Orthogonality

**Definition.** For $k\geq0$ let $\mathcal{P}_k$ be the space of octonion-valued homogeneous polynomials of degree $k$ that are left-monogenic, that is, the space of homogeneous solutions of $Df = 0$ of degree $k$.

**Proposition.** Every element of $\mathcal{P}_k$ is harmonic on $\mathbb{R}^8$, hence its restriction to the unit sphere is an eigenfunction of the spherical Laplacian with eigenvalue $-k(k+6)$; the spaces $\mathcal{P}_k$ and $\mathcal{P}_l$ are orthogonal with respect to the $L^2$ inner product on $S^7$ whenever $k\neq l$, and each $\mathcal{P}_k$ is a finite-dimensional real vector space.

*Proof.* Harmonicity is $D\bar D = \Delta_8$; the eigenvalue statement is the standard separation of variables for a homogeneous harmonic polynomial of degree $k$ in eight variables, where the radial equation is $r^{-k-6}(r^8(r^{-k}v)')' = 0$ and gives the shift $k+6$. Orthogonality of different degrees is the standard orthogonality of spherical harmonics; finite-dimensionality is the finite-dimensionality of the space of polynomials of bounded degree. $\square$

The shift $k+6$ is the octonionic case of the general rule $k+n-2$ for spherical harmonics in $n$ variables with $n = 8$; the dimension of $\mathcal{P}_k$ is computed by the theory of the harmonic analysis of the octonions, and the orthogonal decomposition of $L^2(S^7)$ into the spaces $\mathcal{P}_k$ is not covered here.

**Proposition.** For a left-monogenic function $f$ on a ball of radius $r$ the surface integral of $f$ over the sphere is computable from the value at the centre,

$$
\int_{\lvert y\rvert = r}f(y)\,dS(y) = \omega_7r^7f(0),
$$

and more generally the mean value property of *Octonion Analysis* expresses every interior value as a surface integral over a sphere centred at the point.

*Proof.* The mean value property of *Octonion Analysis*, multiplied by the volume of the sphere. $\square$

The expansion of the kernel in monogenic polynomials of increasing degree turns the Cauchy formula into a Taylor expansion of a monogenic function, with the coefficients given by the integrals of the function against the monogenic polynomials of dual degree; the details are those of the associative theory and carry over, since the argument involves only the kernel, the function and the sphere, and never a product of two variable octonions.

### The Stokes Theorem for the Calibration Forms

The constant-coefficient forms of the octonion geometry integrate by a Stokes theorem of the simplest kind, and the integration makes the calibration argument of *Octonion Geometry* quantitative.

**Proposition.** Let $\varphi$ be the associative three-form and $\psi = \ast\varphi$ its dual on $\operatorname{Im}\mathbb{O}\cong\mathbb{R}^7$, and let $\Phi = e^0\wedge\varphi+\psi$ be the Cayley four-form on $\mathbb{R}^8$, all with constant coefficients. Then $d\varphi = 0$, $d\psi = 0$ and $d\Phi = 0$; consequently for a compact oriented submanifold $L$ with boundary,

$$
\int_L d\varphi = \int_{\partial L}\varphi = 0 , \qquad
\int_L d\psi = \int_{\partial L}\psi = 0 , \qquad
\int_L d\Phi = \int_{\partial L}\Phi = 0 ,
$$

so that the integrals of the calibration forms over closed submanifolds depend only on the homology class, and the Stokes theorem for these forms is the divergence theorem of the previous section applied to their coefficient functions.

*Proof.* The forms have constant coefficients, so their exterior derivatives vanish; Stokes' theorem then gives the vanishing of the boundary integrals, and the invariance under homology is the same statement for two homologous cycles. $\square$

**Corollary (calibrated minimality, integral form).** Let $L\subset\operatorname{Im}\mathbb{O}$ be a compact oriented three-dimensional submanifold with $\varphi$ of constant sign on each tangent plane, so that $L$ is calibrated by $\varphi$ in the sense of *Octonion Geometry*. Then for every compact oriented three-dimensional $L'$ homologous to $L$,

$$
\operatorname{vol}(L) = \int_L\varphi = \int_{L'}\varphi \leq \operatorname{vol}(L') ,
$$

with equality exactly when $L'$ is calibrated by $\varphi$ as well; the same argument with $\psi$ gives the coassociative four-folds, and with $\Phi$ the Cayley four-folds of $\mathbb{R}^8$.

*Proof.* The calibration inequality $\lvert\varphi(\xi_1,\xi_2,\xi_3)\rvert\leq1$ on orthonormal triples gives $\varphi\leq$ the volume form on each oriented tangent plane, with equality exactly on calibrated planes; integrating over $L$ gives $\int_L\varphi = \operatorname{vol}(L)$, and over $L'$ gives $\int_{L'}\varphi\leq\operatorname{vol}(L')$; the integrals agree by the homology invariance of the preceding proposition, and equality forces equality in the pointwise inequality almost everywhere. $\square$

The corollary is the integral form of the calibration statement: the constancy of the forms reduces the minimality of the calibrated submanifolds to the Stokes theorem and a pointwise algebraic inequality, and no property of the octonion multiplication beyond the existence of the forms is used. This is the reason why the calibrated submanifolds of the exceptional geometries of *Octonions and Exceptional Geometry* can be studied by the closedness of the forms alone, the multiplication entering only through the identification of their stabilisers.

## Summary

Integration of octonion-valued functions is componentwise, hence $\mathbb{R}$-linear, and multiplication by a constant passes through the integral from either side; the position of a constant factor in the integrand is part of the meaning of the integral, because the algebra is not commutative. The divergence theorem reads

$$
\int_{\partial\Omega}n(y)f(y)dS(y) = \int_\Omega(\bar Df)(y)dV(y), \qquad \int_{\partial\Omega}f(y)n(y)dS(y) = \int_\Omega(fD)(y)dV(y),
$$

with the order of the factors fixed by the operator, and it produces the Green identity for the product of two functions, with the caveat that the identity in its displayed form holds when the associator terms of the product rule vanish.

The Cauchy integral theorem makes the boundary integral of the kernel against a monogenic function depend only on the homology class of the contour; the sphere normalisation shows that the kernel has total mass one against the outer normal, and the homology form of the Cauchy formula recovers $f(x)$ from any cycle linking $x$. The Cauchy integral operator has principal values and satisfies the classical jump formulas on a smooth hypersurface, so that the difference of its boundary values is the density; but the operator is not idempotent, because the classical proof requires the interchange of two integrations through an associative product, and the interchanged terms carry associators. Monogenic homogeneous polynomials are harmonic spherical harmonics with the eigenvalue shift $k+6$ in the exponent, orthogonal across degrees, and their integrals against the kernel give the Taylor coefficients.

The single structural difference from the associative cases is therefore the failure of the composition law: the Leibniz defect of the octonionic analysis destroys the product formula for monogenic functions and hence the idempotence of the Cauchy transform, while leaving the divergence theorem, the normalisation of the kernel, the homology invariance and the jump formulas intact.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{O}$, $e_0,\dots,e_7$ | Octonion algebra and basis, $e_k^2 = -e_0$ for $k\geq1$ |
| $D = \sum_{k=0}^{7}e_k\partial_k$, $\bar D$ | Cauchy–Riemann operator and its conjugate |
| $E(x) = \bar x/(\omega_7\lvert x\rvert^8)$ | Kernel, $DE = ED = \delta_0$ |
| $\omega_7 = \pi^4/3$ | Volume of $S^7$ |
| $n$, $dS$, $dV$ | Outward unit normal, surface and volume measures |
| $\mathcal{M}_L$, $\mathcal{M}_R$ | Left- and right-monogenic functions |
| $\mathcal{C}f$ | Cauchy integral operator with density $f$ |
| $(\mathcal{C}f)^\pm$ | Boundary values from outside and inside |
| $\mathcal{P}_k$ | Left-monogenic homogeneous polynomials of degree $k$ |
| $[x,y,z]$, $[x,y]$ | Associator and commutator |





## Further Reading

- F. Brackx, Richard Delanghe and Frank Sommen, *Clifford Analysis* (Pitman, 1982), for the divergence theorem, the Cauchy integral operator, the Plemelj–Sokhotski formulas and the idempotence of the Cauchy transform in the associative case.
- John Ryan, "Applications of Clifford analysis to inverse scattering", in *Clifford Algebras and their Applications in Mathematical Physics* (Kluwer, 1993), for the boundary-value theory of the hypercomplex Cauchy integral.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the Green identities, the Taylor expansion with the kernel and the spherical harmonic decomposition.
- Rolf Sören Krausshar, *Generalized Analytic Automorphic Forms in Hypercomplex Spaces* (Birkhäuser, 2004), for the octonionic Cauchy integral and the composition defects.
- Guochang Li, *The Cauchy–Riemann Operator in Octonionic Analysis* (Harbin Institute of Technology Press, 2005), for the octonionic Stokes and Green theorems and their order conventions.
- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton University Press, 1971), for the spherical harmonics, the eigenvalues of the spherical Laplacian and the orthogonal decompositions used above.
