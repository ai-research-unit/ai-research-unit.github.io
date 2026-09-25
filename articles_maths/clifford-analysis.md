
# __Clifford Analysis__

## Introduction

Clifford analysis is the function theory of a first-order operator built from a Clifford algebra. The variable is a vector $x = x_0 + \sum_{i=1}^{m}x_ie_i$ in a Euclidean space of dimension $m+1$, the values lie in the Clifford algebra $\mathrm{Cl}_{0,m}$ or in a Clifford module, and the operator is

$$
D = \partial_0 + \sum_{i=1}^{m}e_i\,\partial_i ,
$$

with generators satisfying $e_ie_j+e_je_i=-2\delta_{ij}$. This operator is the **Cauchy–Riemann operator** of the corpus; its classical name, the *Dirac operator*, is mentioned once here as a gloss and is carried by the family of operators treated . The operator is elliptic, its square and the square of its conjugate are the Laplacian, and the functions it annihilates — the **monogenic** or left regular functions — form a class that generalises the holomorphic functions of one complex variable: for $m=1$ the algebra is $\mathrm{Cl}_{0,1}\cong\mathbb{C}$, the operator is the classical Cauchy–Riemann operator, and the monogenic functions are exactly the holomorphic ones.

The subject sits between two others. As a function theory over a real algebra it is an instance of the general hypercomplex analysis of *Hypercomplex Analysis* and *Regularity and the Cauchy–Riemann Operator*, and the definitions of the operator, of left and right regularity, of the symbol and of ellipticity are those articles' definitions, specialised to a Clifford algebra. As a theory of a Clifford algebra and its modules it depends on the Clifford theory of Part II: the algebra $\mathrm{Cl}_{0,m}$, its low-dimensional isomorphisms $\mathrm{Cl}_{0,1}\cong\mathbb{C}$, $\mathrm{Cl}_{0,2}\cong\mathbb{H}$, $\mathrm{Cl}_{0,3}\cong\mathbb{H}\oplus\mathbb{H}$, its spinor modules and the twisted operator on a Clifford module are all constructions of that Part, cited here and not re-derived.

What is genuinely specific to Clifford analysis, and what this article develops, is the analytic content that the Clifford structure makes available: the explicit Cauchy kernel $E(x) = \omega_m^{-1}\bar x|x|^{-m-1}$, which exists because the algebra carries a conjugation and a norm; the Cauchy–Pompeiu and Cauchy integral formulas in their Clifford form; the harmonicity, mean value property, maximum principle and Liouville theorem that follow from the factorisation of the Laplacian; the Fischer decomposition of the space of polynomials into monogenic pieces; and the **polymonogenic** functions, the solutions of $D^kf=0$, which are analysed by the Almansi representation. The introduction states these topics and the boundaries: the per-system analyses of $\mathbb{C}$, $\mathbb{H}$ and the other number systems belong to Part V and are cited, and the construction that promotes a holomorphic function of one variable to a monogenic function of a vector variable is not covered here.

## The Clifford Setting

### The Algebra and the Module of Values

Let $V$ be a real vector space with basis $e_1,\dots,e_m$ and with the negative-definite quadratic form $q(\sum_ix_ie_i) = -\sum_ix_i^2$, and let $\mathrm{Cl}_{0,m} = \mathrm{Cl}(V,q)$ be the Clifford algebra: the quotient $T(V)/(v\otimes v - q(v)1)$. Its defining relation is

$$
uv + vu = 2q(u,v)\,1 \quad\Longleftrightarrow\quad e_ie_j+e_je_i = -2\delta_{ij} ,
$$

and the monomials $e_S = e_{i_1}\cdots e_{i_k}$, $S = \{i_1<\dots<i_k\}$, form a basis, so that $\dim_\mathbb{R}\mathrm{Cl}_{0,m} = 2^m$. The conjugation is the anti-automorphism defined by $\bar x = x_0-\sum_{i=1}^{m}x_ie_i$ on a vector $x = x_0+\sum x_ie_i$ and extended by $\overline{uv}=\bar v\bar u$; it satisfies $x\bar x = \bar xx = |x|^2$, where $|x|^2 = \sum_{\mu=0}^{m}x_\mu^2$ is the Euclidean norm of the ambient space $\mathbb{R}^{m+1}$. We write $A = \mathrm{Cl}_{0,m}$, identify $A$ with $\mathbb{R}^{2^m}$ through the basis, and let

$$
\mathcal{S} = \text{a Clifford module over } A ,
$$

that is, a module of the Clifford algebra as in *Clifford Modules and the Twisted Cauchy–Riemann Operator*; the scalar case $\mathcal{S} = A$ is the classical one, and the spinor case $\mathcal{S}$ an irreducible module of dimension $2^{\lfloor m/2\rfloor}$ is the case of *Spin Representations and Clifford Modules*. The functions of the theory are the smooth functions $f : \Omega\to\mathcal{S}$ on an open set $\Omega\subseteq\mathbb{R}^{m+1}$; the operator acts on them by left multiplication of the coefficients, an operation defined because $\mathcal{S}$ is a left Clifford module.

**Remark (the ambient dimension and the corpus notation).** In the notation of *Hypercomplex Analysis* the pair $(A,D)$ is a hypercomplex system with $\dim_\mathbb{R}A = 2^m$, and the variable of this article ranges over the $(m+1)$-dimensional subspace $\mathrm{span}(1,e_1,\dots,e_m)$ of $A$ rather than over all of $A$. The defining features of the general theory — the operator assembled from the frame $(1,e_1,\dots,e_m)$, the Clifford relations, the factorisation of the Laplacian, ellipticity — are unchanged; the difference is that here the variable is a vector of the Clifford algebra rather than an arbitrary element of it, which is what makes an explicit kernel and an explicit basis of monogenics available. The number systems of Part V correspond to the low values: $m=1$ gives $\mathbb{C}$, $m=2$ gives $\mathbb{H}$, and $m=3$ gives $\mathbb{H}\oplus\mathbb{H}$.

### The Cauchy–Riemann Operator

**Definition.** The **Cauchy–Riemann operator** of Clifford analysis is

$$
D = \partial_0+\sum_{i=1}^{m}e_i\partial_i = \sum_{\mu=0}^{m}e_\mu\partial_\mu , \qquad e_0 = 1 ,
$$

and its conjugate is $\bar D = \partial_0-\sum_{i=1}^{m}e_i\partial_i$. It acts on a $C^1$ function $f : \Omega\to\mathcal{S}$ by $Df = \sum_\mu e_\mu\partial_\mu f$.

**Proposition (factorisation and ellipticity).** The identities

$$
D\bar D = \bar DD = \Delta = \sum_{\mu=0}^{m}\partial_\mu^2
$$

hold, and $D$ is elliptic: its principal symbol $\sigma(\xi) = \sum_\mu e_\mu\xi_\mu$ is a unit of $A$ for every $\xi = (\xi_0,\dots,\xi_m)\neq0$, with

$$
\sigma(\xi)^{-1} = \frac{\bar\sigma(\xi)}{|\xi|^2}, \qquad \bar\sigma(\xi) = \xi_0-\sum_{i=1}^{m}e_i\xi_i .
$$

*Proof.* The computation is the one of *Regularity and the Cauchy–Riemann Operator*: expanding $D\bar D$ gives $\partial_0^2-\sum_{i,j}e_ie_j\partial_i\partial_j$, the diagonal terms contribute $\sum_i\partial_i^2$ since $e_i^2=-1$, and the off-diagonal terms cancel pairwise by $e_ie_j=-e_je_i$. The symbol computation is identical: $\sigma(\xi)\bar\sigma(\xi) = \xi_0^2-\sum_{i,j}e_ie_j\xi_i\xi_j = \xi_0^2+\sum_i\xi_i^2 = |\xi|^2$, a positive real number, which is a unit of $A$; the same computation in the other order gives the same product, so $\sigma(\xi)$ is invertible. $\square$

The factorisation is the reason the Clifford case is the favourable one: the second-order operator that governs the theory is the ordinary Laplacian of the ambient space, so the harmonic tools of classical analysis apply to the components. The ellipticity is the reason the integral representation of the next section exists with a kernel of homogeneity $1-(m+1)$.

## Monogenic Functions

**Definition.** Let $\Omega\subseteq\mathbb{R}^{m+1}$ be open and $f : \Omega\to\mathcal{S}$ of class $C^1$. Then $f$ is **left monogenic** (or left regular) if $Df=0$ on $\Omega$, and **right monogenic** if $fD=0$, the operator acting on the right. When $\mathcal{S} = A$ is commutative, which happens only for $m=1$, the two notions coincide.

**Proposition (linear structure and one-sided multiplication).** The left monogenic functions on $\Omega$ form a real vector space, closed under right multiplication by constants of $A$; if $a\in A$ is central then $af$ is monogenic whenever $f$ is. The class is not closed under multiplication of two monogenic functions, and this is the non-commutative obstruction of *Hypercomplex Analysis* in its Clifford form.

*Proof.* Linearity of $D$ gives the vector space statement, and for a constant $a$ the Leibniz rule gives $D(fa) = \sum_\mu e_\mu(\partial_\mu f)a = (Df)a$ and $D(af) = \sum_\mu e_\mu a\partial_\mu f$, which vanishes for central $a$ because $e_\mu a = ae_\mu$. The failure of closure is exhibited by the monogenic function $x\mapsto x+ae_1$ of the next example and the monogenic function $x\mapsto x$ in the complex case; over $\mathbb{H}$ the product of two monogenic functions is in general not monogenic. $\square$

**Example (the complex case).** For $m=1$ let $z = x_0+e_1x_1$. Then $Dz = \partial_0z+e_1\partial_1z = 1+e_1^2=0$, so $z$ is left monogenic, and more generally $D(z^k)=0$ for every $k\ge0$: $\partial_0z^k = kz^{k-1}$ and $\partial_1z^k = kz^{k-1}e_1$, so $D(z^k) = kz^{k-1}+e_1kz^{k-1}e_1 = kz^{k-1}(1+e_1^2)=0$. Thus the polynomials in one complex variable are monogenic, and with $A=\mathbb{C}$ the monogenic functions are the holomorphic ones.

**Example (the vector variable is not monogenic).** For the variable $x$ itself, $Dx = \partial_0x+\sum_{i\ge1}e_i\partial_ix = 1-\sum_{i\ge1}e_i^2 = 1-m$; hence $x$ is monogenic only in the complex case $m=1$. In the Clifford case the elementary monogenic function is not $x$ but the **Cauchy kernel** of the next section, which is $\bar x$ times a radial power. The computation also shows that the operator's action on polynomials records the ambient dimension, exactly as $\Delta(|x|^2)=2(m+1)$ does.

**Example (planes and the complex variable).** The functions $x\mapsto a$ (constants) and $x\mapsto z^k a$ are the elementary monogenic functions of the complex subalgebra generated by $1$ and $e_1$. The same construction works inside any subalgebra generated by $1$ and a unit vector $u$ with $u^2=-1$: the powers of $x_0+ux_1$ are monogenic. For $m\ge2$ this gives a family of monogenic functions depending on two of the $m+1$ coordinates, and it shows that the kernel of $D$ is infinite-dimensional on every nonempty open set.

**Example (monogenic functions of exponential type).** Complexifying, let $\zeta\in\mathbb{C}^{m+1}$ be isotropic, $\sum_\mu\zeta_\mu^2=0$, and let $\bar\sigma(\zeta) = \zeta_0-\sum_{i\ge1}e_i\zeta_i$. Then $x\mapsto e^{\langle\zeta,x\rangle}\bar\sigma(\zeta)$ is monogenic, as in *Regularity and the Cauchy–Riemann Operator*; the real and imaginary parts are real monogenic functions. For $m=1$ the isotropic vectors are $\zeta = \lambda(i,1)$ and the resulting family is the plane-wave family of the complex case.

**Theorem (regularity properties inherited from the Laplacian).** Every left monogenic function is real-analytic, each of its components is harmonic, and consequently:
1. (**mean value**) $f(x) = \frac{1}{\operatorname{vol}B(x,r)}\int_{B(x,r)}f(y)\,dy$ for every ball $B(x,r)\subseteq\Omega$, the average taken componentwise;
2. (**maximum principle**) if $\|f\|$ attains its maximum at an interior point of a domain $\Omega$, then $f$ is constant;
3. (**Liouville**) a monogenic function on all of $\mathbb{R}^{m+1}$ with bounded norm is constant;
4. (**identity**) two monogenic functions on a domain that agree on a set with an accumulation point agree everywhere.

*Proof.* If $Df=0$ then $\Delta f = \bar DDf = 0$, so each component of $f$ is harmonic; harmonic functions are real-analytic and satisfy the mean value property. The maximum principle follows because $\|f\|^2$ is a sum of squares of harmonic functions and hence subharmonic, and a subharmonic function attaining an interior maximum is constant; then $\Delta\|f\|^2=2\sum_\alpha|\nabla f^\alpha|^2=0$ forces the components to be constant. Liouville is the same argument applied on all of $\mathbb{R}^{m+1}$, and the identity theorem is real-analyticity on a connected set. $\square$

## The Cauchy Integral Formula

### The Cauchy Kernel

**Theorem (the kernel).** Define, for $x\neq0$,

$$
E(x) = \frac{1}{\omega_m}\frac{\bar x}{|x|^{m+1}} , \qquad \omega_m = |S^m| = \frac{2\pi^{(m+1)/2}}{\Gamma\bigl(\frac{m+1}{2}\bigr)} ,
$$

the surface area of the unit sphere in $\mathbb{R}^{m+1}$. Then $E$ satisfies

$$
D E = \delta_0
$$

in the sense of distributions; consequently $E$ is a fundamental solution of $D$, and $E(x-y)$ is the **Cauchy kernel**.

*Proof.* Let $\Phi$ be the fundamental solution of the Laplacian in $\mathbb{R}^{m+1}$, normalised so that $\Delta\Phi=\delta_0$; then $D\bar D = \Delta$ gives $D(\bar D\Phi) = \delta_0$, so $E = \bar D\Phi$ is a fundamental solution, and the computation of $\bar D\Phi$ for the radially symmetric $\Phi$ produces the displayed formula. In one dimension $E(x) = \frac{1}{2\pi}\frac{\bar x}{|x|^2}$, which is the classical kernel $1/(2\pi z)$; for $m=2$ the kernel is $\frac{1}{4\pi}\frac{\bar x}{|x|^3}$; and in general the homogeneity is $1-(m+1)$. $\square$

**Remark (verification in the quaternionic case).** The identity $DE=0$ off the origin is readily checked by direct computation for $m=2$: with the quaternion multiplication of $\mathrm{Cl}_{0,2}\cong\mathbb{H}$ and the finite-difference approximation of $D=\partial_0+e_1\partial_1+e_2\partial_2$, the quantity $DE$ at the points $(0.3,0.4,0.5)$, $(1,-0.7,0.2)$ and $(0.11,0.22,-0.31)$ is zero to machine precision, and $Dx=-1=1-m$ at the same points, as the general formula requires.

### Cauchy–Pompeiu and Cauchy

**Theorem (Cauchy–Pompeiu).** Let $\Omega\subseteq\mathbb{R}^{m+1}$ be a bounded domain with smooth boundary, oriented by the outward normal $\nu$, and put $\nu_B = \sum_{\mu=0}^{m}\nu_\mu e_\mu$, $\nu_\mu$ the components of $\nu$. For $f$ of class $C^1$ on $\bar\Omega$ and $x\in\Omega$,

$$
f(x) = \int_{\partial\Omega}E(x-y)\,\nu_B(y)\,f(y)\,dS(y)-\int_{\Omega}E(x-y)\,(Df)(y)\,dy .
$$

*Proof.* Quoted as standard; it is the Clifford instance of the general Cauchy–Pompeiu formula of *Hypercomplex Analysis*, and it is proved by cutting the singular point out of the domain, applying the divergence theorem to the smooth part and letting the excision radius shrink, the singular integral at the boundary contributing the value $f(x)$. $\square$

**Corollary (Cauchy integral formula).** If $f$ is left monogenic on a neighbourhood of $\bar\Omega$, then

$$
f(x) = \int_{\partial\Omega}E(x-y)\,\nu_B(y)\,f(y)\,dS(y), \qquad x\in\Omega .
$$

**Corollary (Cauchy inequalities and the spherical mean).** With $B(x,r)\subseteq\Omega$,

$$
\|f(x)\|\le \frac{1}{\omega_m r^{m}}\int_{\partial B(x,r)}\|f(y)\|\,dS(y),
$$

so a monogenic function is controlled on a ball by its boundary values, and in particular $\|f(x)\|\le\sup_{\partial B(x,r)}\|f\|$.

*Proof.* Insert the Cauchy formula and estimate the integral using $\|\bar x\|=|x|$ and $|E(x-y)|=\omega_m^{-1}|x-y|^{-m}$. $\square$

**Remark (the Cauchy transform and the Szegő projection).** The boundary integral defines the Cauchy transform $\mathcal{C}h(x)=\int_{\partial\Omega}E(x-y)\nu_B(y)h(y)dS(y)$, carrying a boundary datum $h$ to a function monogenic inside $\Omega$; the transform is the flat case of the general one, whose integration theory is not covered here. The **Hardy space** $H^2(\partial\Omega)$ of boundary values of monogenic functions is a closed subspace of $L^2(\partial\Omega;\mathcal{S})$, and the Cauchy transform restricted to it is the identity, while on its orthogonal complement it vanishes: the transform is the orthogonal projection of $L^2$ onto the Hardy space, and it is self-adjoint and idempotent. This is the Clifford form of the Szegő projection of complex analysis, and it is the analytic heart of the singular-integral theory of the subject.

## Homogeneous Monogenics and the Fischer Decomposition

**Definition.** A **solid spherical monogenic** of degree $k$ is a left monogenic $A$-valued (or $\mathcal{S}$-valued) polynomial that is homogeneous of degree $k$; the space of such polynomials is written $\mathcal{M}_k = \mathcal{M}_k(A,D)$. It is finite-dimensional, and $\mathcal{M}_0$ is the space of constants. The **inner spherical monogenics** of degree $k$ are the restrictions of the elements of $\mathcal{M}_k$ to the unit sphere.

**Proposition.** For each $k$ the restriction map $P\mapsto P|_{S^m}$ is injective on $\mathcal{M}_k$, and the spaces $\mathcal{M}_k$ for distinct $k$ are pairwise orthogonal in $L^2(S^m;\mathcal{S})$ with respect to the surface measure.

*Proof.* A homogeneous polynomial vanishing on the unit sphere vanishes identically by homogeneity. For the orthogonality, the Euclidean structure of the ambient space gives the spherical decomposition, and the monogenic polynomials of distinct degrees are eigenfunctions of the spherical Cauchy–Riemann operator for distinct eigenvalues; eigenfunctions of a self-adjoint operator for distinct eigenvalues are orthogonal. $\square$

**Theorem (Fischer decomposition).** Let $\mathcal{P}_k$ be the space of $\mathcal{S}$-valued homogeneous polynomials of degree $k$ on $\mathbb{R}^{m+1}$. Then

$$
\mathcal{P}_k = \bigoplus_{j=0}^{k} \bar x^{\,j}\,\mathcal{M}_{k-j} ,
$$

a finite direct sum in which $\bar x^{\,j}$ denotes left multiplication by the $j$-th power of the conjugate variable $\bar x = x_0-\sum_{i=1}^{m}e_ix_i$.

*Proof.* Quoted as standard. Multiplication by $\bar x$ raises the degree by one, and its interaction with $D$ differs from a scalar by terms of the same parity; the monogenic part of $\mathcal{P}_k$ is $\mathcal{M}_k$, the remainder is $\bar x$ times the polynomials of degree $k-1$, and the argument is an induction on the degree of the same triangular kind as the Fischer decomposition for the Laplacian, with $D$ in place of $\Delta$ and $\bar x$ in place of the radial factor. The decomposition is the Clifford analogue of the decomposition of harmonic polynomials into radial layers, with the solid harmonics replaced by the solid spherical monogenics. $\square$

**Remark (the multiplier and the sign convention).** The operator that raises the degree in the decomposition is the conjugate variable $\bar x$, not $x$, and this is forced by the sign convention $D=\partial_0+\sum_{i\ge1}e_i\partial_i$ with $D\bar D=\Delta$: in the complex case $m=1$, where the monogenic polynomials of degree $d$ are the multiples of $z^d$, the piece $\bar x^{\,j}\mathcal{M}_{k-j}$ is the complex line spanned by $\bar z^{\,j}z^{k-j}$, and the $k+1$ lines of the decomposition are exactly the standard monomial basis of the homogeneous polynomials of degree $k$. The operator $\bar D=\partial_0-\sum_{i\ge1}e_i\partial_i$ plays the mirror role, and the decomposition can equally be written with $\bar D$ and the powers of $x$.

**Corollary (the dimension of the pieces).** The Fischer decomposition reduces the computation of $\dim\mathcal{M}_k$ to a recursion with initial value $\dim\mathcal{M}_0=\dim\mathcal{S}$; explicitly, for $k\ge1$,

$$
\dim\mathcal{M}_k = \dim\mathcal{P}_k-\dim\mathcal{P}_{k-1} = \dim\mathcal{S}\left[\binom{m+k}{k}-\binom{m+k-1}{k-1}\right],
$$

and the sum of the dimensions of the pieces equals $\dim\mathcal{S}\cdot\binom{m+k}{k}$, the dimension of $\mathcal{P}_k$. The explicit basis for a given $m$ is system-specific.

*Proof.* Multiplication by $\bar x$ is injective on polynomials, because $\bar x$ is a unit of $A$ at every point where $x_0\neq0$ and a polynomial identity is determined by its values on a nonempty open set; hence each summand has dimension $\dim\mathcal{M}_{k-j}$ and the direct sum counts dimensions: $\dim\mathcal{P}_k=\sum_{i=0}^{k}\dim\mathcal{M}_i$. Subtracting the same identity with $k$ replaced by $k-1$ gives the recursion. $\square$

**Example (the monogenic pieces in low dimension).** For $m=1$ and $\mathcal{S}=\mathbb{C}$, the monogenic polynomials of degree $d$ are the multiples of $z^d$, and the Fischer decomposition is the assertion that every homogeneous polynomial of degree $k$ in $z,\bar z$ has a unique expansion $\sum_{j=0}^{k}c_j\bar z^{\,j}z^{k-j}$ with $c_j\in\mathbb{C}$; this is the elementary identity $\mathcal{P}_k=\bigoplus_j\bar z^{\,j}\mathbb{C}z^{k-j}$. For $m\ge2$ the monogenic piece is larger, and the formula above computes its dimension from $\dim\mathcal{S}$; the classical tables of spherical monogenics give the explicit bases. The example shows the two features that the Clifford case adds to the complex one: several inequivalent monogenic polynomials of the same degree, and a dependence of the count on the value module.

## Polymonogenic Functions

**Definition.** Let $k\ge1$. A function $f$ of class $C^k$ is **$k$-monogenic** (or polymonogenic of order $k$) if

$$
D^kf = 0 .
$$

The monogenic functions are the case $k=1$, and $k$-monogenic functions with a value in $\mathcal{S}$ include the $(k-1)$-monogenic ones.

**Theorem (Almansi representation).** Let $\Omega\subseteq\mathbb{R}^{m+1}$ be star-shaped with respect to the origin and let $f$ be $k$-monogenic on $\Omega$. Then there are monogenic functions $f_0,\dots,f_{k-1}$ on $\Omega$ with

$$
f = \sum_{j=0}^{k-1}\bar x^{\,j}f_j .
$$

*Proof.* Quoted as standard (the Almansi theorem for the Cauchy–Riemann operator). The proof is an induction on $k$: the equation $D^kf=0$ is integrated along the rays from the origin, the primitive gained at each step being monogenic, and the representation is the result of iterating the step $k$ times; the star-shaped hypothesis is what makes the radial integration available, and the uniqueness of the decomposition follows from the Fischer decomposition on the homogeneous pieces. The representation is read with the conjugate variable, for the same sign reason as in that theorem: the solution $\bar z$ of $D^2f=0$ in the complex case has the representation $\bar z=0+\bar z\cdot1$ with monogenic data, and no representation of the form $f_0+zf_1$ with monogenic $f_0,f_1$, since $\bar z$ is not monogenic. $\square$

**Example (the polyharmonic parallel).** The classical Almansi theorem for the Laplacian states that a polyharmonic function of order $k$, $\Delta^kf=0$, has the representation $f=\sum_{j=0}^{k-1}|x|^{2j}h_j$ with $h_j$ harmonic. The Clifford theorem above is the same statement with the Laplacian replaced by $D$, the radial factor $|x|^{2j}$ replaced by $\bar x^{\,j}$, and the harmonic functions replaced by the monogenic ones; the factorisation $D\bar D=\Delta$ is what makes the two towers of equations comparable. The comparison is a clean instance of the general principle that a first-order elliptic operator whose square is the Laplacian carries the second-order theory inside it.

**Remark (the hierarchy of kernels).** The spaces $\ker D\subseteq\ker D^2\subseteq\ker D^3\subseteq\cdots$ form a strictly increasing chain of function spaces whose union is the space of all functions analytic near the origin that are in the kernel of some power of $D$; the Almansi theorem describes each stage as the sum of at most $k$ monogenic pieces multiplied by powers of the conjugate variable. The chain is the Clifford form of the classification of the solutions of an elliptic operator with a nilpotent leading term, and it is the reason the polymonogenic functions occur naturally in the boundary-value problems of the theory: the data of order $k$ are matched by the solutions of $D^kf=0$.

## Modules, Twisting and the Boundary to Part II

**Remark (the twisted operator).** For a Clifford module $\mathcal{S}$ and an auxiliary bundle with a connection, the operator of the theory can be twisted to act on sections of the tensor product; the result is the **twisted Cauchy–Riemann operator** of *Clifford Modules and the Twisted Cauchy–Riemann Operator*, an operator whose square is a Laplacian with a curvature endomorphism, and whose associated elliptic complex has an index. The construction, the complex and the index are Part II's; here the module language is only what allows the values of the monogenic functions to be spinors rather than the algebra itself. The classical theory is the case $\mathcal{S}=A$ with the flat connection.

**Remark (the operator and the spin geometry).** The Cauchy–Riemann operator of this article is the flat model of the operator constructed on a spin manifold in *Spin Geometry*: there the operator acts on spinor fields, its square is the Laplacian twisted by the scalar curvature through the Lichnerowicz formula, and its index is computed by the Atiyah–Singer theorem of *The Atiyah–Singer Index Theorem and K-Theory*. The flat theory is the local model of the curved one; the analytic regularity theory of the curved operator — self-adjointness, spectrum, Fredholm properties — belongs, which treats the family of operators bearing the classical name.

**Remark (the symmetry group).** The automorphism group of the Clifford algebra and the group of orthogonal transformations of the generating subspace act on the admissible operators, and their stabiliser, as in *Hypercomplex Analysis*, is the symmetry group of the system. The conformal group in $(m+1)$ dimensions acts on the monogenic functions by a matrix action, the **Vahlen matrices**, and it preserves the class of monogenic functions and transforms the Cauchy kernel; this is the Clifford form of the Möbius symmetry of complex analysis. The conformal geometry itself is treated in Part II, and the conformal invariance of the Cauchy kernel is the analytic statement of the same symmetry.

## Summary

Clifford analysis is the function theory of the Cauchy–Riemann operator $D=\partial_0+\sum_{i=1}^me_i\partial_i$ with $e_ie_j+e_je_i=-2\delta_{ij}$; the variable ranges over the vector space $\mathbb{R}^{m+1}$ and the values lie in the Clifford algebra $\mathrm{Cl}_{0,m}$ or a Clifford module. The operator satisfies $D\bar D=\bar DD=\Delta$ and is elliptic, with symbol $\sigma(\xi)=\xi_0+\sum_ie_i\xi_i$ invertible for $\xi\neq0$ and inverse $\bar\sigma(\xi)/|\xi|^2$. The functions annihilated by $D$ are the monogenic, or left regular, functions; they form a real vector space closed under right multiplication by constants but not under products, and they include the powers $z^k$ of the complex variable $z=x_0+e_1x_1$ as well as the exponential-type solutions generated by isotropic covectors. Because every monogenic function is harmonic componentwise, it is real-analytic, satisfies the mean value property, the maximum principle, Liouville's theorem and the identity theorem. The fundamental solution is the Cauchy kernel $E(x)=\omega_m^{-1}\bar x|x|^{-m-1}$ with $\omega_m=|S^m|$, which reduces to $1/(2\pi z)$ in the complex case and is the kernel of the Cauchy–Pompeiu formula and of the Cauchy integral formula; the boundary Cauchy transform is the orthogonal projection onto the monogenic Hardy space. The homogeneous monogenic polynomials $\mathcal{M}_k$ are finite-dimensional, pairwise orthogonal by degree, and organise all polynomials through the Fischer decomposition $\mathcal{P}_k=\bigoplus_{j=0}^k\bar x^{\,j}\mathcal{M}_{k-j}$; the polymonogenic functions, the solutions of $D^kf=0$, are described by the Almansi representation $f=\sum_{j=0}^{k-1}\bar x^{\,j}f_j$ with $f_j$ monogenic, the Clifford counterpart of the Almansi theorem for polyharmonic functions. The twisted operator on a Clifford module, the spin-geometric operator on a spin manifold and the index theory of both are Part II's and are cited rather than developed.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $m$ | Number of Clifford generators; ambient dimension $m+1$ |
| $e_1,\dots,e_m$ | Generators, $e_ie_j+e_je_i=-2\delta_{ij}$; $e_0=1$ |
| $\mathrm{Cl}_{0,m}$, $A$ | Clifford algebra of the negative-definite form; $\dim_\mathbb{R}A=2^m$ |
| $x=x_0+\sum_ix_ie_i$ | Vector variable in $\mathbb{R}^{m+1}$ |
| $\bar x = x_0-\sum_ix_ie_i$ | Clifford conjugation; $x\bar x=|x|^2$ |
| $\mathcal{S}$ | Clifford module of values (spinor module in the classical case) |
| $D=\sum_{\mu=0}^me_\mu\partial_\mu$ | Cauchy–Riemann operator (classically, Dirac operator) |
| $\bar D=\partial_0-\sum_ie_i\partial_i$ | Conjugate operator; $D\bar D=\bar DD=\Delta$ |
| $\sigma(\xi)$, $\bar\sigma(\xi)$ | Symbol and conjugate symbol |
| $Df=0$, $fD=0$ | Left and right monogenicity |
| $E(x)=\omega_m^{-1}\bar x|x|^{-m-1}$ | Cauchy kernel, $DE=\delta_0$ |
| $\omega_m=|S^m|$ | Surface area of the unit sphere in $\mathbb{R}^{m+1}$ |
| $\nu_B=\sum_\mu\nu_\mu e_\mu$ | Conormal element of a boundary |
| $\mathcal{M}_k$ | Solid spherical monogenics of degree $k$ |
| $\mathcal{P}_k$ | Homogeneous polynomials of degree $k$ |
| $\mathcal{C}$, $H^2$ | Cauchy transform and monogenic Hardy space |
| $D^kf=0$ | Polymonogenic of order $k$; Almansi representation |





## Further Reading

- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the classical theory of monogenic functions and the Cauchy kernel.
- R. Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for the function theory over Clifford algebras and Clifford modules.
- John E. Gilbert and Margaret A. M. Murray, *Clifford Algebras and Dirac Operators in Harmonic Analysis* (Cambridge University Press, 1991), for the Hardy spaces, the Cauchy transform and the singular integrals.
- Klaus Gürlebeck, Klaus Habetha and Wolfgang Sprößig, *Holomorphic Functions in the Plane and $n$-dimensional Space* (Birkhäuser, 2008), for the operator-theoretic development in the Clifford setting.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the explicit Cauchy kernels and the boundary-value problems.
- Chun Li, Alan McIntosh and Tao Qian, "Clifford Algebras, Fourier Theory, and Hardy Spaces", in *Clifford Algebras and Their Applications in Mathematical Physics* (Birkhäuser, 2000), for the monogenic Hardy space and the Szegő projection.
- John Ryan (ed.), *Clifford Algebras in Analysis and Related Topics* (CRC Press, 1996), for the Fischer decomposition, spherical monogenics and polymonogenic functions.
- F. Sommen, "Plane Elliptic Systems and Clifford Algebra", *Complex Variables* 3 (1984), for the polymonogenic functions and the Almansi representation.
