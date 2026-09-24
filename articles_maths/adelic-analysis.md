
# __Adelic Analysis__

## Introduction

The adele ring of a number field is the restricted product of its completions, one factor for each place, and it carries a measure obtained by multiplying the local Haar measures of the factors. That measure, its uniqueness, the self-duality of the additive group of the adeles with respect to a suitable character coming from the product formula, the Fourier transform on the adeles and the Poisson summation formula are the analytic content of the theory. They are what makes the adeles more than a bookkeeping device: the Poisson summation formula on the adeles specialises to the Riemann–Roch theorem for a function field, and the integral of a suitable function against the characters of the idele class group produces the zeta functions and $L$-functions of number theory together with their analytic continuation and functional equations. The method is Tate's thesis, and this article develops it.

The ring of adeles and the group of ideles, with their topologies and their structure, belong to Part II and are constructed in *Adeles and Ideles*; this article takes them as given and puts analysis on them. The local Haar measure is that of *p-adic Integration* at the finite places and the ordinary Lebesgue measure at the Archimedean ones; the local Fourier transform and the local zeta integrals are computed place by place and then multiplied. What results is the analytic machinery: the Tamagawa measure and the finiteness of the volume of the adele class group, the self-dual measure, the Fourier inversion and Plancherel theorems, Poisson summation, the local functional equation of the local zeta integrals, and the global functional equation of the zeta integral, with the completed Riemann zeta function as the worked example. The arithmetic consequences for a single zeta or $L$-function — its Euler product, its analytic continuation, its zeros, its special values — belong to the arithmetic theory, and the analytic proofs of the prime number theorem and the statements about the Riemann hypothesis are not treated here.

The prerequisites are *Adeles and Ideles* for the ring and the group, *p-adic Integration* for the local measures, *Locally Compact Groups and Haar Measure* for the Haar theorem, *Harmonic Analysis on Groups* for the Fourier transform on a locally compact abelian group and for Pontryagin duality, *Measure Theory and Integration* for the general integration theory, *Algebraic Number Theory* for the places, the class number, the regulator and the discriminant, and *Absolute Values, Valuations and Completions* for the local fields. Throughout, $K$ is a number field with ring of integers $\mathcal{O}_K$, discriminant $d_K$, $r_1$ real places and $r_2$ complex places; its completions are $K_v$ for the places $v$, with $v$ finite giving a non-Archimedean local field with residue field of $q_v$ elements and uniformiser $\varpi_v$, and $v$ infinite giving $\mathbb{R}$ or $\mathbb{C}$. The adele ring is $\mathbb{A} = \mathbb{A}_K$, the idele group $\mathbb{A}^\times$, the idele norm $\lvert \cdot \rvert$ and the norm-one subgroup $\mathbb{A}^1$. The local absolute value is normalised by $\lvert \varpi_v \rvert_v = q_v^{-1}$ and $\lvert x \rvert_\infty = \lvert x \rvert$; the product formula $\prod_v \lvert x \rvert_v = 1$ holds for $x \in K^\times$.

## Measures on the Adeles

### The Local Measures and the Restricted Product

**Definition.** At each place $v$ let $\mu_v$ be the Haar measure on $(K_v,+)$ normalised as follows: for finite $v$, $\mu_v(\mathcal{O}_v) = 1$; for a real place, $\mu_v$ is the Lebesgue measure; for a complex place, $\mu_v$ is twice the Lebesgue measure of $\mathbb{R}^2$. These are precisely the measures that are **self-dual** with respect to the local additive characters of the next section.

**Theorem (the Tamagawa measure).** There is a unique Haar measure $\mu$ on the locally compact group $(\mathbb{A},+)$ with the property that
$$
\mu\Bigl(\prod_v A_v\Bigr) = \prod_v \mu_v(A_v)
$$
whenever $A_v$ is a measurable subset of $K_v$ equal to $\mathcal{O}_v$ for almost every finite $v$ and equal to $\{0\}$ for almost every infinite $v$; the product converges because $\mu_v(\mathcal{O}_v) = 1$ for almost every $v$. The measure $\mu$ is translation-invariant, and it is the Tamagawa measure of $\mathbb{A}$.

**Proof.** Existence and translation invariance follow because the restricted product is locally compact and the product of the local measures is finite on the basic compact open subgroups $\prod_{v \notin S}\mathcal{O}_v \times \prod_{v \in S}\{0\}$ for finite $S$ containing the infinite places, which form a neighbourhood basis of $0$; these subgroups determine the measure, and uniqueness is the uniqueness of the Haar measure of *Locally Compact Groups and Haar Measure*. $\square$

**Remark (the local picture).** At a finite place the measure is that of *p-adic Integration*, with $\mu_v(\mathcal{O}_v) = 1$ and $\mu_v(\mathfrak{p}_v^n) = q_v^{-n}$; the measure of $\mathcal{O}_v^\times$ is $1 - q_v^{-1}$. At the real place the measure is Lebesgue measure, and at a complex place twice the plane Lebesgue measure. The normalisation at the finite places is the one that makes the indicator of the ring of integers self-dual, and the normalisation at the infinite places is the one that makes the Gaussian self-dual; both are needed for the product formula of the next section to take its clean form.

### The Volume of the Adele Class Group

**Theorem (finiteness of the volume).** The quotient $\mathbb{A}/K$ has finite volume for every number field, and it is compact exactly when $K$ is a function field, that is, when $K$ has no infinite place: for a number field $\mathbb{A}/K$ is not compact. With the normalisation above,
$$
\operatorname{vol}(\mathbb{A}/K) = \frac{2^{r_1}(2\pi)^{r_2}\,h\,R}{w\sqrt{\lvert d_K \rvert}},
$$
where $h$ is the class number, $R$ the regulator, $w$ the number of roots of unity in $K$ and $d_K$ the discriminant. In particular $\operatorname{vol}(\mathbb{A}_\mathbb{Q}/\mathbb{Q}) = 1$.

**Proof sketch.** A fundamental domain is the product of a fundamental domain for the ideal class group with a fundamental domain for the unit lattice, whose covolume is the regulator; the factors $2^{r_1}$ and $(2\pi)^{r_2}$ come from the normalisations of the local measures at the infinite places, and $w$ and $\sqrt{\lvert d_K\rvert}$ from the torsion and the discriminant. For $K = \mathbb{Q}$ the fundamental domain is $[0,1) \times \prod_p \mathbb{Z}_p$, of measure $1$. The computation is the analytic form of the finiteness of the class number and Dirichlet's unit theorem. $\square$

**Theorem (the idele class group).** The idele class group $\mathbb{A}^\times/K^\times$ is not compact; its norm-one subgroup $\mathbb{A}^1/K^\times$ is compact, and with the multiplicative measure induced by the product of the local measures $\mu_v^\times$,
$$
\operatorname{vol}\bigl(\mathbb{A}^1/K^\times\bigr) = \frac{2^{r_1}(2\pi)^{r_2}\,h\,R}{w\sqrt{\lvert d_K\rvert}} ,
$$
the same quantity as the additive volume, in accordance with the Tamagawa number $1$ of the multiplicative group.

**Proof sketch.** The exact sequence $1 \to \mathbb{A}^1/K^\times \to \mathbb{A}^\times/K^\times \to \mathbb{R}_{>0} \to 1$, with the last map the norm, reduces the compactness of the middle to that of the first, which is the compactness of the norm-one subgroup; its volume is computed by the same fundamental domain as above, the multiplicative and additive measures agreeing on the units by the local relation $d^\times x = \frac{q_v}{q_v-1}\lvert x\rvert_v^{-1}d\mu_v$ of *p-adic Integration*. $\square$

## Characters and Self-Duality

### The Standard Characters

**Definition.** A choice of a nontrivial additive character of $\mathbb{A}/K$ is made once and for all: at the finite places
$$
\psi_v(x) = e^{-2\pi i \{x\}_v} \quad \text{with } \{x\}_v \in \mathbb{Z}[1/p] \text{ the fractional part of } x,
$$
at the real place $\psi_v(x) = e^{2\pi i x}$, and at a complex place $\psi_v(z) = e^{4\pi i \operatorname{Re} z}$; and $\psi = \prod_v \psi_v$ is the product character on $\mathbb{A}$.

**Theorem.** The product character is well defined, continuous and trivial on $K$:
$$
\psi(x) = 1 \qquad (x \in K),
$$
by the product formula; consequently it induces a character of the compact group $\mathbb{A}/K$ and, by Pontryagin duality, an isomorphism $\mathbb{A} \cong \widehat{\mathbb{A}}$ given by $\xi \mapsto \psi_\xi$ with $\psi_\xi(x) = \psi(\xi x)$.

**Proof.** Almost every factor has $x \in \mathcal{O}_v$ and hence $\{x\}_v = 0$, so the product is finite; continuity is local. For $x \in K$ the identity $\psi(x) = 1$ is the product formula $\prod_v \lvert x \rvert_v = 1$ written in the form $\sum_v \{x\}_v \equiv 0$ modulo the appropriate lattices; the induced character is trivial on $K$ by construction. Pontryagin duality is the duality of *Harmonic Analysis on Groups* applied to the self-dual groups $K_v$ and assembled over the restricted product. $\square$

### Self-Duality and the Fourier Transform

**Definition.** The Fourier transform of a function $f$ on $\mathbb{A}$ for which the integral converges is
$$
\hat f(\xi) = \int_{\mathbb{A}} f(x)\, \psi(\xi x)\, d\mu(x),
$$
and the **Schwartz–Bruhat space** $\mathcal{S}(\mathbb{A})$ is the restricted product of the local Schwartz spaces: locally constant compactly supported functions at the finite places and Schwartz functions at the infinite ones, with the convergence requirement that almost every local factor be the indicator of $\mathcal{O}_v$.

**Theorem (inversion and Plancherel).** For $f \in \mathcal{S}(\mathbb{A})$ the Fourier transform lies in $\mathcal{S}(\mathbb{A})$ and
$$
\hat{\hat f}(x) = f(-x), \qquad \int_{\mathbb{A}} \lvert \hat f(\xi) \rvert^2 \, d\mu(\xi) = \int_{\mathbb{A}} \lvert f(x) \rvert^2 \, d\mu(x).
$$
**Proof sketch.** The local statements are proved place by place: at a finite place the Fourier transform is the $\mu_v$-self-adjoint operator on the space of locally constant compactly supported functions, and the normalisation $\mu_v(\mathcal{O}_v)=1$ combined with the choice of $\psi_v$ gives $\widehat{\mathbf{1}_{\mathcal{O}_v}} = \mathbf{1}_{\mathcal{O}_v}$; at the infinite places the same statement holds for the Gaussian, and both imply inversion by the standard argument. The global transform is the product of the local transforms for factorisable functions, and the general case follows by linearity and a limiting argument. $\square$

## Poisson Summation and Riemann–Roch

**Theorem (Poisson summation).** Let $f \in \mathcal{S}(\mathbb{A})$. Then
$$
\sum_{\gamma \in K} f(\gamma) = \sum_{\gamma \in K} \hat f(\gamma),
$$
both series converging absolutely.

**Proof sketch.** The sum over $K$ of $f$ defines a continuous function $F$ on the compact quotient $\mathbb{A}/K$; its Fourier coefficients on the compact group are the values $\hat f(\gamma)$ of the transform, by the computation of the pairing of $F$ against the character $\psi_\gamma$. The inversion formula for the compact group $\mathbb{A}/K$, applied at $x=0$, identifies the value $F(0)$ with the sum of the coefficients. $\square$

**Corollary (Riemann–Roch).** Let $K$ be a function field of one variable over a finite field, let $D$ be a divisor of $K$ and let $f$ be the indicator of the compact open subgroup of the adeles consisting of the elements integral with respect to $D$. Then the Poisson summation formula becomes the Riemann–Roch theorem: the dimension of the space of functions whose divisor is bounded below by $D$, together with the corresponding dimension for the complementary divisor $K-D$, differs by the fixed amount $\deg D + 1 - g$.

**Proof sketch.** For the function field case $\mathbb{A}/K$ is compact and the Poisson summation formula is an identity between two finite sums; specialising $f$ to the indicator of the elements bounded by $D$ and computing both sides gives the theorem of Riemann–Roch with the correction term $1 - g$. $\square$

The corollary is the reason that Poisson summation on the adeles is described as the analytic form of the Riemann–Roch theorem; in the number field case the corresponding statement is the subject of the next section.

## Local Zeta Integrals

### Definitions and Convergence

**Definition.** Let $v$ be a place, $\chi_v$ a continuous homomorphism $K_v^\times \to \mathbb{C}^\times$ (a **quasicharacter**) and $\Phi_v$ a Schwartz–Bruhat function on $K_v$. The **local zeta integral** is
$$
Z_v(s, \chi_v, \Phi_v) = \int_{K_v^\times} \Phi_v(x)\,\chi_v(x)\,\lvert x \rvert_v^{s} \, d^\times x ,
$$
with $d^\times x$ the local multiplicative measure of *p-adic Integration* at a finite place and its Archimedean analogue at an infinite place.

**Theorem (convergence and rationality).** The integral converges absolutely for $\Re s$ sufficiently large, and the function so defined is a rational function of $q_v^{-s}$ at a finite place and a meromorphic function of $s$ at an infinite place. If $\chi_v$ is unramified and $\Phi_v$ is the indicator of $\mathcal{O}_v$, then
$$
Z_v(s, \chi_v, \mathbf{1}_{\mathcal{O}_v}) = \frac{1}{1 - \chi_v(\varpi_v) q_v^{-s}} .
$$
**Proof.** For $\Phi_v = \mathbf{1}_{\mathcal{O}_v}$ the integrand is supported on $\mathcal{O}_v$ and constant on the spheres $\varpi_v^n\mathcal{O}_v^\times$ with $\chi_v(\varpi_v^n) = \chi_v(\varpi_v)^n$; the spheres have multiplicative measure $1$ and $\lvert x \rvert_v^s = q_v^{-ns}$ there, giving $\sum_{n \geq 0} \chi_v(\varpi_v)^n q_v^{-ns}$, which converges for $\lvert \chi_v(\varpi_v) q_v^{-s} \rvert < 1$. The general case is a finite sum of such terms, one for each sphere on which $\Phi_v$ is supported. $\square$

### The Local Functional Equation

**Definition.** The **local $L$-factor** attached to $\chi_v$ is $L_v(s,\chi_v) = (1-\chi_v(\varpi_v)q_v^{-s})^{-1}$ when $\chi_v$ is unramified and $L_v = 1$ when it is ramified; the **local zeta integral normalised by the $L$-factor** is $\zeta_v(s,\chi_v,\Phi_v) = Z_v(s,\chi_v,\Phi_v)/L_v(s,\chi_v)$.

**Theorem (Tate's local functional equation).** There is a meromorphic function $\gamma_v(s,\chi_v)$, independent of $\Phi_v$, with
$$
Z_v(1-s, \chi_v^{-1}, \hat\Phi_v) = \gamma_v(s,\chi_v)\,Z_v(s,\chi_v,\Phi_v)
$$
for all $\Phi_v$, where $\hat\Phi_v$ is the local Fourier transform. Writing $\gamma_v(s,\chi_v) = \epsilon_v(s,\chi_v)\,L_v(1-s,\chi_v^{-1})/L_v(s,\chi_v)$, the factor $\epsilon_v(s,\chi_v)$ is a monomial in $q_v^{-s}$ times a Gauss sum, and it is the **local root number**; equivalently, the normalised integrals $\zeta_v = Z_v/L_v$ satisfy
$$
\zeta_v(1-s, \chi_v^{-1}, \hat\Phi_v) = \epsilon_v(s,\chi_v)\,\zeta_v(s,\chi_v,\Phi_v).
$$

**Proof sketch.** For $\Phi_v = \mathbf{1}_{\mathcal{O}_v}$ both sides are computed directly from the previous theorem, using $\hat\Phi_v = \mathbf{1}_{\mathcal{O}_v}$ in the unramified case and the explicit Fourier transform of the indicator of a fractional ideal in the ramified case; the quotient then defines $\gamma_v$ and, by linearity and continuity, extends to all $\Phi_v$. The independence of $\Phi_v$ is the substance: the space of Schwartz–Bruhat functions is spanned by such indicators. $\square$

## The Global Zeta Integral and Tate's Thesis

### Factorisable Functions and Euler Products

**Definition.** A function $\Phi$ on $\mathbb{A}$ is **factorisable** if $\Phi = \prod_v \Phi_v$ with $\Phi_v$ a local Schwartz–Bruhat function equal to $\mathbf{1}_{\mathcal{O}_v}$ for almost all $v$; a quasicharacter $\chi$ of $\mathbb{A}^\times$ trivial on $K^\times$ is a **Hecke character**, and it is factorisable with the same meaning. The **global zeta integral** is
$$
Z(s,\chi,\Phi) = \int_{\mathbb{A}^\times} \Phi(x)\,\chi(x)\,\lvert x \rvert^{s} \, d^\times x .
$$
**Theorem (Euler product).** For $s$ with $\Re s$ large the integral converges absolutely, and if $\Phi$ and $\chi$ are factorisable then
$$
Z(s,\chi,\Phi) = \prod_v Z_v(s,\chi_v,\Phi_v),
$$
the product converging absolutely and locally uniformly in the half-plane of convergence.

**Proof.** Convergence follows from the rapid decay of $\Phi$ and the growth of $\lvert x \rvert^s$; the factorisation is the multiplicativity of the measure and of the integrand under the identification of the restricted product with the product of the local pieces, and the absolute convergence justifies the interchange of product and integral by the dominated convergence theorem applied to the local factors. $\square$

### The Functional Equation

**Theorem (Tate).** Let $\chi$ be a Hecke character and let $\Phi \in \mathcal{S}(\mathbb{A})$ be nonzero. Then $Z(s,\chi,\Phi)$ extends to a meromorphic function on $\mathbb{C}$ and satisfies the global functional equation
$$
Z(1-s, \chi^{-1}, \hat\Phi) = Z(s,\chi,\Phi),
$$
with the self-dual measure and the additive character fixed above. Equivalently, the normalised integral $\zeta(s,\chi,\Phi) = Z(s,\chi,\Phi)/L(s,\chi)$ satisfies
$$
\zeta(1-s, \chi^{-1}, \hat\Phi) = \epsilon(s,\chi)\,\zeta(s,\chi,\Phi), \qquad \epsilon(s,\chi) = \prod_v \epsilon_v(s,\chi_v),
$$
and for a factorisable $\Phi$ the normalised integral is the product $\prod_v \zeta_v(s,\chi_v,\Phi_v)$ of the local ones. When $\Phi_v = \mathbf{1}_{\mathcal{O}_v}$ at every finite place and $\Phi_v$ is the standard Gaussian at every infinite place, the unnormalised product
$$
\Lambda(s,\chi) = \prod_v Z_v(s,\chi_v,\Phi_v)
$$
is the completed $L$-function of $\chi$ and satisfies
$$
\Lambda(s,\chi) = \epsilon(s,\chi)\,\Lambda(1-s,\chi^{-1}),
$$
with the global root number satisfying $\epsilon(s,\chi)\epsilon(1-s,\chi^{-1}) = 1$.

**Proof sketch.** The functional equation for the global integral is the Poisson summation formula applied to the function $x \mapsto \Phi(x)\chi(x)\lvert x \rvert^s$ and to its transform: Poisson summation gives an identity between the sum over $K^\times$ of a function and the sum over $K^\times$ of its transform, and the two sides are the integrals over the two fundamental domains obtained by truncating $\mathbb{A}^\times/K^\times$ at $\lvert x \rvert$ large and small. The contribution of the truncations is an integral over the compact set $\mathbb{A}^1/K^\times$, which is finite by the finiteness of the volume, and it converges and is holomorphic; the remaining terms give exactly the transformation $s \mapsto 1-s$. Multiplying the local functional equations over the places gives the functional equation of the normalised integral, with $\epsilon(s,\chi)$ the product of the local root numbers, and inserting $\prod_v L_v(s,\chi_v) = L(s,\chi)$ gives the functional equation of the completed $L$-function. The doubling identity for $\epsilon$ follows by applying the functional equation twice. $\square$

### The Completed Zeta Function

**Corollary (the Riemann zeta function).** Take $K = \mathbb{Q}$, $\chi = 1$ and $\Phi = \prod_v \Phi_v$ with $\Phi_\infty(x) = e^{-\pi x^2}$ and $\Phi_p = \mathbf{1}_{\mathbb{Z}_p}$. Then the global zeta integral is
$$
Z(s) = \pi^{-s/2}\Gamma(s/2)\,\zeta(s) = \Lambda(s),
$$
the completed Riemann zeta function, and the functional equation of the theorem becomes $\Lambda(s) = \Lambda(1-s)$; the Euler product of the theorem becomes $\zeta(s) = \prod_p (1-p^{-s})^{-1}$.

**Proof sketch.** The Archimedean integral is $\int_{\mathbb{R}^\times} e^{-\pi x^2}\lvert x \rvert^{s}d^\times x = \pi^{-s/2}\Gamma(s/2)$; the local integrals at the finite places are $(1-p^{-s})^{-1}$ by the local computation; the product over the places is the Euler product of $\zeta$. The Gaussian is self-dual, so the root number is $1$, and the functional equation reads $\Lambda(s) = \Lambda(1-s)$. $\square$

The corollary is the prototype. The analytic continuation, the special values, the distribution of the zeros and the arithmetic applications of $\zeta$ and of the Hecke $L$-functions $L(s,\chi)$ are the subject , which take this article's local and global functional equations as their analytic input; the analytic proof of the prime number theorem belongs and the statements about the zeros. What this article supplies is the adelic integration, the Fourier transform, the Poisson summation formula and the two functional equations, local and global.

## Summary

The adele ring of a number field carries a Haar measure obtained by multiplying the local Haar measures of its completions: at a finite place the measure with $\mu_v(\mathcal{O}_v) = 1$, at a real place the Lebesgue measure and at a complex place twice the plane Lebesgue measure, chosen so that every local measure is self-dual with respect to the standard local additive character. The product of the local measures is a well-defined Haar measure on the restricted product, the Tamagawa measure, and the volume of $\mathbb{A}/K$ is finite and equal to $\frac{2^{r_1}(2\pi)^{r_2}hR}{w\sqrt{\lvert d_K\rvert}}$, which is $1$ for $\mathbb{Q}$; the compactness of $\mathbb{A}/K$ characterises the function fields, and the norm-one idele class group is compact with the same volume. The product of the standard local characters is a character of $\mathbb{A}/K$ by the product formula, and it makes $\mathbb{A}$ self-dual; the Fourier transform on the Schwartz–Bruhat space satisfies inversion and Plancherel, and the Poisson summation formula $\sum_K f = \sum_K \hat f$ holds, specialising to the Riemann–Roch theorem for a function field.

The local zeta integrals $Z_v(s,\chi_v,\Phi_v) = \int \Phi_v\chi_v\lvert x\rvert_v^s d^\times x$ converge for $\Re s$ large, are rational in $q_v^{-s}$, and satisfy Tate's local functional equation with the local $\gamma$- and $\epsilon$-factors. The global zeta integral of a Hecke character and a factorisable function is the product of the local integrals, and it satisfies the global functional equation $Z(1-s,\chi^{-1},\hat\Phi) = Z(s,\chi,\Phi)$, from which the functional equation $\Lambda(s,\chi) = \epsilon(s,\chi)\Lambda(1-s,\chi^{-1})$ of the completed Hecke $L$-function follows by multiplying the local equations over the places. The completed Riemann zeta function is the case $K = \mathbb{Q}$, $\chi = 1$, $\Phi_\infty$ the Gaussian, and $\Phi_p$ the indicator of $\mathbb{Z}_p$, and its functional equation $\Lambda(s) = \Lambda(1-s)$ is the simplest instance of the whole theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$, $v$ | Number field, a place |
| $K_v$ | Completion at $v$; $\mathbb{R}$ or $\mathbb{C}$ for $v$ infinite |
| $\mathcal{O}_v$, $\varpi_v$, $q_v$ | Ring of integers, uniformiser, residue cardinality at a finite place |
| $\mathbb{A} = \mathbb{A}_K$ | Adele ring, restricted product of the $K_v$ |
| $\mathbb{A}^\times$, $\mathbb{A}^1$ | Idele group, norm-one ideles |
| $d_K$, $r_1$, $r_2$, $h$, $R$, $w$ | Discriminant, real and complex places, class number, regulator, roots of unity |
| $\lvert x \rvert$, $\lvert x \rvert_v$ | Idele norm and local absolute values, $\lvert\varpi_v\rvert_v = q_v^{-1}$ |
| $\mu_v$, $\mu$ | Local Haar measures, the Tamagawa measure on $\mathbb{A}$ |
| $d^\times x$ | Multiplicative measure on $\mathbb{A}^\times$ |
| $\psi_v$, $\psi$ | Standard local additive characters, their product on $\mathbb{A}/K$ |
| $\hat f$, $\mathcal{S}(\mathbb{A})$ | Fourier transform, Schwartz–Bruhat space |
| Poisson summation | $\sum_{\gamma\in K} f(\gamma) = \sum_{\gamma\in K}\hat f(\gamma)$ |
| $\chi$, $\chi_v$ | Hecke character, its local components |
| $\Phi$, $\Phi_v$ | Factorisable test function, local components |
| $Z_v$, $Z$ | Local and global zeta integrals |
| $L_v$, $L(s,\chi)$ | Local $L$-factor, global Hecke $L$-function |
| $\gamma_v$, $\epsilon_v$ | Local $\gamma$- and $\epsilon$-factors |
| $\Lambda(s,\chi)$ | Completed $L$-function |
| $\Lambda(s) = \pi^{-s/2}\Gamma(s/2)\zeta(s)$ | Completed Riemann zeta function |



## Further Reading

- John Tate, *Fourier Analysis in Number Fields and Hecke's Zeta-Functions* (doctoral thesis, Princeton, 1950; reprinted in Cassels–Fröhlich, *Algebraic Number Theory*), for the whole method of this article.
- J. W. S. Cassels and Albrecht Fröhlich (eds.), *Algebraic Number Theory* (Academic Press, 1967), for Tate's thesis and the standard normalisations of the local measures and characters.
- André Weil, *Basic Number Theory* (Springer, 1967), for the adelic formulation and the Poisson summation formula.
- Serge Lang, *Algebraic Number Theory* (2nd ed., Springer, 1994), for the adele ring, the finiteness of the volume and the class number formula.
- Dinakar Ramakrishnan and Robert J. Valenza, *Fourier Analysis on Number Fields* (Springer, 1999), for a modern systematic treatment of the local and global Fourier analysis and of Tate's thesis.
- Dorian Goldfeld and Joseph Hundley, *Automorphic Representations and $L$-Functions for the General Linear Group* (Cambridge University Press, 2011), for the extension of the zeta integrals to the higher-rank case.
- Daniel Bump, *Automorphic Forms and Representations* (Cambridge University Press, 1997), for the representation-theoretic reading of Hecke characters and zeta integrals.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (2nd ed., CRC Press, 2016), for the Pontryagin duality and the Fourier transform on locally compact abelian groups.
