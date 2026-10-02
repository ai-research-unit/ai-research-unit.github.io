
# __The Convolution Operator on a Symmetric Space__

## Introduction

On a symmetric space $X = G/K$ the invariant integral operators are the operators that every symmetry of $X$ leaves fixed, and the simplest of them is the **convolution operator**: fix a function $f$ on the group and average the translate $u(g^{-1}\cdot x)$ against $f$,

$$
(C_f u)(x) = \int_G f(g)\,u(g^{-1}\cdot x)\,dg .
$$

The operator is $G$-invariant by construction, and on a symmetric space it is diagonalised by a small, geometrically determined family of functions: the **spherical functions** $\phi_\lambda$, the $K$-invariant eigenfunctions of every invariant differential operator of $X$, which are also the matrix coefficients of the spherical representations. The eigenvalues are the values of the **spherical transform** $\hat f(\lambda)$, and the statement that the convolution operator is multiplication by $\hat f$ in the spherical basis is the geometry's form of the convolution theorem.

This article treats the convolution operator from the side of the symmetric space: the invariant measure the metric supplies, the invariance that makes the operator an invariant operator, the spherical functions as the eigenfunctions, and the spherical transform as the eigenvalue assignment. The harmonic analysis that the operator belongs to is Part III and is cited, not developed: the Haar measure and the convolution algebra are *Locally Compact Groups and Haar Measure*, *The Convolution Algebra $L^1(G)$* and *Convolution on a Group*; the spherical functions and the zonal spherical function are *Spherical Functions and the Zonal Spherical Function*; the decomposition of the regular representation and the inversion are *The Plancherel Theorem* and *Noncommutative Harmonic Analysis*; and the compact case is *Analysis on Compact Groups* and *The Peter–Weyl Theorem*. The symmetric space itself, its geodesic symmetry, the symmetric pair and the rank, are *Riemannian Symmetric Spaces and the Involution* and *Transformation Groups*, cited and not re-derived.

The article has five sections: the symmetric space and its invariant measure; the invariant operators; the spherical functions; the spherical transform and the convolution theorem; and the worked cases. Throughout, $G$ is a connected semisimple Lie group with finite centre, $\sigma$ the Cartan involution, $K = G^\sigma$ a maximal compact subgroup, and $X = G/K$ the symmetric space of noncompact type; the compact and Euclidean cases are obtained by the Cartan duality of *Riemannian Symmetric Spaces and the Involution* and are stated where they differ.

## The Symmetric Space and Its Invariant Measure

### The Space and Its Geometry

A symmetric space is a connected Riemannian manifold in which every point is the isolated fixed point of an involutive isometry, the geodesic symmetry; it is homogeneous, $X = G/K$, with $G$ the identity component of the isometry group and $K$ the stabiliser of a point, and the differential of the geodesic symmetry is the **Cartan involution** $\sigma$ of the Lie algebra $\mathrm G = \mathrm K \oplus \mathrm P$ with $[\mathrm K,\mathrm P]\subseteq\mathrm P$ and $[\mathrm P,\mathrm P]\subseteq\mathrm K$. The isotropy complement $\mathrm P$ is the tangent space at the base point $o = eK$, and the geodesics through $o$ are the images of the one-parameter subgroups $\exp(tX)$, $X \in \mathrm P$. The **rank** is the dimension of a maximal abelian subspace $\mathrm A \subseteq \mathrm P$; the nonzero weights of $\mathrm A$ on the complexified Lie algebra form the restricted root system $\Sigma$, with the positive system $\Sigma_+$ and the half-sum $\rho = \tfrac12\sum_{\alpha\in\Sigma_+}m_\alpha\alpha$, where $m_\alpha$ is the multiplicity. These are the objects of *Riemannian Symmetric Spaces and the Involution*, and the curvature signs are opposite in the compact and the noncompact type.

### The Invariant Measure

**Definition.** The **invariant measure** of $X$ is the $G$-invariant Radon measure $dx$ induced by the Haar measure of $G$: for $f \in C_c(X)$,

$$
\int_X f(x)\,dx = \int_G f(g\cdot o)\,dg,
$$

well defined because the Haar measure is invariant under right translation by $K$. In the **polar coordinates** of the Cartan decomposition $G = K\exp(\mathrm A_+)K$ it reads

$$
\int_X f(x)\,dx = \int_K\int_{\mathrm A_+} f\bigl(k\exp H\cdot o\bigr)\,\delta(H)\,dH\,dk,
\qquad
\delta(H) = \prod_{\alpha\in\Sigma_+}\bigl(\sinh\alpha(H)\bigr)^{m_\alpha},
$$

and the function $\delta$ is the Jacobian of the exponential map, the geometric density of the space.

**Remark.** The measure is the datum that makes the averaging rigorous, and it is supplied by the metric, so it is a geometric object: a different invariant metric on the same manifold gives a different $\delta$ and a different convolution operator. The Haar measure is *Locally Compact Groups and Haar Measure*, Part III.

### The Convolution of Functions

**Definition.** The **convolution** of $f, h \in L^1(G)$ is

$$
(f * h)(g) = \int_G f(g_1)\,h(g_1^{-1}g)\,dg_1,
$$

an associative product making $L^1(G)$ a Banach algebra, *The Convolution Algebra $L^1(G)$* and *Convolution on a Group*. The convolution of two $K$-bi-invariant functions, $f(kgk') = f(g)$, is again $K$-bi-invariant, so the $K$-bi-invariant functions form a subalgebra; in the geometry they are the **radial functions** of $X$, the functions of the distance from the base point.

## The Invariant Operators

### The Invariance of the Convolution Operator

**Definition.** The **convolution operator** of the kernel $f \in L^1(G)$ acts on the functions on $X$ by

$$
(C_f u)(x) = \int_G f(g)\,u(g^{-1}\cdot x)\,dg .
$$

**Proposition.** For every $f$ the operator $C_f$ is $G$-invariant, $C_f\pi(a) = \pi(a)C_f$ for all $a \in G$, and $f \mapsto C_f$ is a homomorphism of the convolution algebra, $C_f C_h = C_{f*h}$. When $f$ is $K$-bi-invariant the operator preserves the $K$-invariant functions, so it acts on the radial functions alone.

**Proof.** For the invariance, $C_f\pi(a)u(x) = \int f(g)u(a^{-1}g^{-1}x)dg = \int f(ag^{-1})u(g^{-1}x)dg$ after $g \mapsto ag^{-1}$, and the invariance of the measure and of $f$ give $\pi(a)C_f$; the homomorphism is the associativity of convolution, and the last statement is that the average over $K$ of a $K$-bi-invariant kernel is the same kernel.

**Remark.** By the converse of the invariance, every operator on $X$ commuting with $G$ and defined by an integral kernel against the invariant measure is a convolution operator, so the $C_f$ are the whole integral part of the commutant of the action. The differential part of the commutant, the $G$-invariant differential operators, is the algebra $\mathbb{D}(G/K)$ generated by the Casimir operator and the higher invariants of the symmetric pair; the convolution operators with $K$-finite kernel are the integral operators whose Schwartz kernels are eigenfunctions, and the two algebras share their eigenfunctions, the spherical functions.

### The Algebra of Invariant Differential Operators

**Definition.** The algebra of **invariant differential operators** $\mathbb{D}(G/K)$ is the algebra of differential operators on $X$ commuting with the action of $G$; it is commutative, and it is isomorphic to the algebra of $W$-invariant polynomials on $\mathrm A$, where $W$ is the Weyl group of the restricted root system, through the Harish-Chandra isomorphism.

**Proposition.** Every operator in $\mathbb{D}(G/K)$ preserves the $K$-invariant functions and acts on the radial functions as a differential operator in the single radial variable on $\mathrm A$; the joint eigenfunctions of $\mathbb{D}(G/K)$ on the radial functions are the spherical functions.

**Proof sketch.** The invariance under $K$ makes an invariant operator act on radial functions by a radial operator, and the Harish-Chandra isomorphism identifies the algebra with the symmetric polynomials on $\mathrm A$; the Cartan decomposition turns the Laplacian into the radial operator with the density $\delta$, and the joint eigenfunction equation is a regular singular ODE whose solutions are the spherical functions.

## The Spherical Functions

### Definition

**Definition.** A **spherical function** of the symmetric space $X$ is a $K$-invariant eigenfunction of every operator in $\mathbb{D}(G/K)$ normalised by $\phi(e) = 1$. For $\lambda \in \mathrm A^*_{\mathbb C}$ the **elementary spherical function** is

$$
\phi_\lambda(g) = \int_K e^{\langle i\lambda + \rho,\, H(gk)\rangle}\,dk,
\qquad g \in G,
$$

where $H(g)$ is the $\mathrm A$-component of $g$ in the Cartan decomposition and $\rho$ is the half-sum of the positive restricted roots. The function $\phi_\lambda$ is the **matrix coefficient** $\langle \pi_\lambda(g)v, v\rangle$ of the spherical principal series, $v$ the $K$-fixed unit vector.

**Proposition.** For every $\lambda$ the function $\phi_\lambda$ is $K$-bi-invariant, satisfies $\phi_\lambda(e) = 1$, is an eigenfunction of the algebra $\mathbb{D}(G/K)$, and satisfies the functional equation $\int_K \phi_\lambda(xky)\,dk = \phi_\lambda(x)\phi_\lambda(y)$: the last is the identity that makes the spherical functions the characters of the commutative convolution algebra of the radial functions.

**Proof sketch.** The $K$-bi-invariance is the invariance of $dk$; the normalisation is the volume of $K$; the eigenfunction property is that $\langle i\lambda+\rho, H(gk)\rangle$ is the phase of the spherical representation and the Casimir acts by the constant $\langle\lambda,\lambda\rangle + \langle\rho,\rho\rangle$; the functional equation is the multiplication rule of the matrix coefficients of the spherical function, obtained by inserting $\int_K dk$ and using the invariance of the Cartan decomposition.

### The Geometry of the Parameter

**Proposition.** Two elementary spherical functions coincide exactly when the parameters are related by the Weyl group: $\phi_\lambda = \phi_\mu$ if and only if $\mu = w\lambda$ for some $w \in W$. Consequently the spectral parameter $\lambda$ is a point of the quotient $\mathrm A^*_{\mathbb C}/W$, and the spherical transform sees only this quotient.

**Proof.** The Harish-Chandra isomorphism identifies the eigenvalues of $\mathbb{D}(G/K)$ with the $W$-invariant polynomials on $\mathrm A$, and the elementary spherical function is determined by its system of eigenvalues; different Weyl chambers give the same system.

**Remark.** The geometry is visible in the parameter. The rank of the symmetric space is the dimension of $\lambda$; the boundary $\langle\lambda,\lambda\rangle = \langle\rho,\rho\rangle$ is the bottom of the spectrum of the Laplacian; for the noncompact type the spectrum is continuous and fills the region beyond this bottom, for the compact type it is discrete and given by the dominant weights, and for the Euclidean type the spherical functions are the characters and the spectrum is the full dual. The three cases are the three types of *Riemannian Symmetric Spaces and the Involution*.

## The Spherical Transform and the Convolution Theorem

### The Spherical Transform

**Definition.** The **spherical transform** of a $K$-bi-invariant function $f$ is

$$
\hat f(\lambda) = \int_G f(g)\,\phi_{-\lambda}(g)\,dg,
$$

and the **spherical Plancherel measure** $d\mu(\lambda)$ on the quotient $\mathrm A^*_{\mathbb C}/W$ is the measure with respect to which the transform is an isometry of $L^2(K\backslash G/K)$ onto its image:

$$
\int_G \lvert f(g)\rvert^2\,dg = \int_{\mathrm A^*_{\mathbb C}/W} \bigl\lvert \hat f(\lambda)\bigr\rvert^2\,d\mu(\lambda).
$$

The measure is absolutely continuous with the density $\lvert \mathbf c(\lambda)\rvert^{-2}$, where $\mathbf c$ is the Harish-Chandra $\mathbf c$-function, the meromorphic function carrying the asymptotics of the spherical functions; both the transform and the measure are *Spherical Functions and the Zonal Spherical Function* and *The Plancherel Theorem*, cited and not re-derived.

### The Convolution Theorem

**Theorem (spherical convolution theorem).** Let $f, h$ be $K$-bi-invariant functions in $L^1(G)$. Then the spherical transforms multiply:

$$
\widehat{f*h}(\lambda) = \hat f(\lambda)\,\hat h(\lambda) ,
$$

and the convolution operator acts on the elementary spherical functions by the scalar $\hat f$:

$$
C_f \phi_\lambda = \hat f(\lambda)\,\phi_\lambda ,
\qquad
C_f \phi_\lambda(x) = \int_G f(g)\,\phi_\lambda(g^{-1}\cdot x)\,dg .
$$

The eigenvalue assignment $\lambda \mapsto \hat f(\lambda)$ is the **spherical symbol** of the convolution operator, and it is a function on the spectral quotient $\mathrm A^*_{\mathbb C}/W$.

**Proof.** Insert the functional equation of the spherical functions into the definition of the convolution: $(f*h)(g) = \int f(g_1)h(g_1^{-1}g)dg_1$ gives, after applying $\int_K \cdot\,dk$ and the functional equation $\int_K \phi_\lambda(xky)dk = \phi_\lambda(x)\phi_\lambda(y)$, the product of the two transforms. The operator statement is the same computation read as an operator on the radial functions, and the symbol is the eigenvalue assignment by the previous proposition.

**Corollary.** The convolution operators with $K$-bi-invariant kernels commute with each other and with $\mathbb{D}(G/K)$, and they are simultaneously diagonalised by the spherical functions; the joint spectrum is the image of the convolution algebra under the spherical transform, a closed subalgebra of the bounded continuous functions on the spectral quotient.

**Remark.** The theorem is the geometric form of the convolution theorem of the abelian group $\mathbb{R}^n$, in which the spherical functions are the characters and the spherical transform is the Fourier transform. The new content of the non-abelian case is that the characters are organised by the Weyl group, that the measure is the Harish-Chandra $\mathbf c$-function rather than the Lebesgue measure, and that the spectrum of the Laplacian has a bottom at $\langle\rho,\rho\rangle$ that the flat case does not have.

## Worked Cases

**Example (Euclidean space).** Let $X = \mathbb{R}^n = E(n)/O(n)$, the flat symmetric space of the Euclidean type. The spherical functions are the characters $e^{i\langle\lambda,x\rangle}$ averaged over $O(n)$,

$$
\phi_\lambda(x) = \int_{O(n)} e^{i\langle\lambda, kx\rangle}\,dk,
$$

proportional to the Bessel function $J_{(n-2)/2}(\lvert\lambda\rvert\lvert x\rvert)/(\lvert\lambda\rvert\lvert x\rvert)^{(n-2)/2}$, and the spherical transform is the radial Fourier transform; the convolution operator is the radial part of the ordinary convolution, and its symbol is the Fourier–Bessel transform of the radial kernel. The rank is one and the Weyl group is $\{\pm1\}$, so the spectral quotient is the half-line.

**Example (the hyperbolic plane).** Let $X = \mathbb{H}^2 = SL(2,\mathbb{R})/SO(2)$ of rank one. The restricted root system is of type $A_1$ with multiplicity one, $\rho = \tfrac12$, and the spherical functions are the Legendre functions

$$
\phi_\lambda(g) = P_{-\frac12 + i\lambda}\bigl(\cosh r(g)\bigr),
$$

where $r$ is the hyperbolic distance from the base point; the spherical transform is the Harish-Chandra transform with density $\lvert \mathbf c(\lambda)\rvert^{-2} = \lambda\tanh(\pi\lambda)$, and the bottom of the spectrum of the Laplacian is $\tfrac14$ at $\lambda = 0$, the constant function. The convolution operator is the radial integral operator whose kernel is a function of the hyperbolic distance, and the convolution theorem says its eigenvalues are the Legendre transform of the kernel.

**Example (the sphere).** Let $X = S^n = SO(n+1)/SO(n)$ of compact type. The spherical functions are the zonal spherical harmonics

$$
\phi_k(x) = \frac{P_k^{(n-1)/2}(\cos\theta)}{\binom{k+n-2}{k}},
$$

with $\theta$ the geodesic distance and $P_k$ the Gegenbauer polynomial; the spectrum is discrete, the parameter $k \geq 0$ an integer, and the convolution operator is the zonal spherical harmonic projection, with eigenvalues the Gegenbauer transform of the kernel. This is the spherical case of *Analysis on Compact Groups* and *The Peter–Weyl Theorem*.

## Summary

On a symmetric space $X = G/K$ the convolution operator $C_f u(x) = \int_G f(g)u(g^{-1}\cdot x)\,dg$ is the general $G$-invariant integral operator on the space, and it is a homomorphism of the convolution algebra, $C_f C_h = C_{f*h}$. The invariant measure is the geometric density $\delta(H) = \prod_{\alpha\in\Sigma_+}(\sinh\alpha(H))^{m_\alpha}$ in the polar coordinates of the Cartan decomposition, and it is supplied by the metric. The spherical functions $\phi_\lambda(g) = \int_K e^{\langle i\lambda+\rho, H(gk)\rangle}dk$ are the $K$-bi-invariant eigenfunctions of the algebra of invariant differential operators, normalised by $\phi_\lambda(e)=1$, they satisfy the functional equation, and they depend on the parameter only through its Weyl orbit, so the spectral parameter lives in $\mathrm A^*_{\mathbb C}/W$. The spherical transform $\hat f(\lambda) = \int_G f(g)\phi_{-\lambda}(g)dg$ turns convolution into multiplication, $\widehat{f*h} = \hat f\,\hat h$, and diagonalises the convolution operator, $C_f\phi_\lambda = \hat f(\lambda)\phi_\lambda$; the Plancherel measure is the Harish-Chandra density $\lvert\mathbf c(\lambda)\rvert^{-2}$. In the Euclidean case the spherical functions are the radial Bessel functions, in the hyperbolic case the Legendre functions with a spectral bottom at $\rho$, and in the compact case the zonal spherical harmonics with discrete spectrum.

The harmonic analysis of the spherical functions and of the Plancherel measure is Part III and is cited; the article's content is the operator $C_f$ read off the symmetric space, its invariance, and its symbol. The involution on the elements of the symmetry group and the adjoint of an operator are the later groups of this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X = G/K$ | the symmetric space; $K$ the fixed group of the Cartan involution |
| $\mathrm G = \mathrm K\oplus\mathrm P$ | Cartan decomposition; $\mathrm P$ the isotropy complement |
| $\mathrm A$, $\Sigma$, $\rho$ | maximal abelian subspace, restricted roots, half-sum |
| $\delta(H)$ | Jacobian $\prod_{\alpha\in\Sigma_+}(\sinh\alpha(H))^{m_\alpha}$; the invariant density |
| $dx$, $dg$ | invariant measure on $X$; Haar measure on $G$ |
| $C_f$ | the convolution operator with kernel $f$ |
| $*$ | convolution, $(f*h)(g) = \int_G f(g_1)h(g_1^{-1}g)\,dg_1$ |
| $\mathbb{D}(G/K)$ | the algebra of invariant differential operators |
| $\phi_\lambda$ | the elementary spherical function; a joint eigenfunction |
| $\hat f(\lambda)$ | the spherical transform; the spherical symbol of $C_f$ |
| $d\mu(\lambda)$ | the spherical Plancherel measure; density $\lvert\mathbf c(\lambda)\rvert^{-2}$ |
| $\mathbf c(\lambda)$ | the Harish-Chandra $\mathbf c$-function |
| $W$ | the Weyl group of the restricted root system |
| $P_\nu$, $J_\nu$ | Legendre and Bessel functions appearing as spherical functions |

## Further Reading

- Sigurdur Helgason, *Groups and Geometric Analysis* (Academic Press, 1984), for the convolution operator, the spherical functions, the spherical transform and the Plancherel formula on a symmetric space.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the Cartan decomposition, the invariant measure and the algebra of invariant differential operators.
- Harish-Chandra, *Collected Papers* (Springer, 1984), for the original construction of the spherical functions, the $\mathbf c$-function and the Plancherel measure.
- Garth Warner, *Harmonic Analysis on Semi-Simple Lie Groups I* (Springer, 1972), for the spherical principal series, the matrix-coefficient formula and the functional equation.
- Robert S. Strichartz, "Harmonic analysis on symmetric spaces", in *Studies in Harmonic Analysis* (Mathematical Association of America, 1976), for the operator-theoretic reading of the convolution theorem.
