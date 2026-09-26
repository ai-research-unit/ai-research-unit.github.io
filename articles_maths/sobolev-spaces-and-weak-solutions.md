
# __Sobolev Spaces and Weak Solutions__

## Introduction

The classical theory of partial differential equations asks for a solution that is twice differentiable on its domain, and this requirement is at once too strong and too fragile. It is too strong because many equations have solutions that are not of class $C^2$ — the minimiser of an energy need not be smoother than the energy permits — and it is too fragile because the classical conditions cannot be tested against data of limited regularity, which is the situation of every equation met in practice. The remedy is to weaken the notion of derivative, so that a function is credited with a derivative when it is the function's action under integration by parts, and then to ask for solutions in a space of functions that possess these **weak derivatives** up to a fixed order. That space is the **Sobolev space** $W^{k,p}(\Omega)$.

The gain is threefold and accounts for the place of the subject. The Sobolev spaces are complete — $W^{k,p}$ is a Banach space and $H^k = W^{k,2}$ is a Hilbert space — so the fixed-point and projection methods of functional analysis become available. They enjoy **embedding theorems** that recover continuity and integrability at the cost of the derivative count, so a weak solution can still be shown to be a classical one when the data allow. And the boundary conditions can be built into the space itself, as in $W^{k,p}_0(\Omega)$, which removes the need to impose them separately in the analysis. The result is a theory in which the model equations of the preceding article are solved for data that is merely square-integrable, and in which the solutions are shown to be smooth when the data are.

This article constructs the weak derivative and the Sobolev spaces, proves their elementary calculus (the product and chain rules, completeness, the density of smooth functions), and states the embedding, compactness and trace theorems that are the working tools. It then formulates the **weak solution** of an elliptic boundary-value problem, proves existence and uniqueness by the Lax–Milgram theorem, obtains the energy estimates and the elliptic regularity theorem, and records the variational characterisation of the solution as the minimiser of an energy functional, which is the Dirichlet principle and the point of contact with the calculus of variations of this Part. The parabolic and hyperbolic equations are treated by the Galerkin method, in enough detail to show how the same estimates give existence. The setting is a domain $\Omega \subseteq \mathbb{R}^n$ with the regularity stated in each theorem; the integration theory is that of *Measure Theory and Integration*, the Hilbert and Banach space theory that of *Banach and Hilbert Spaces*, and the classical equations being solved are those of *Partial Differential Equations*.

## Weak Derivatives and the Sobolev Spaces

### The Weak Derivative

**Definition.** Let $\Omega \subseteq \mathbb{R}^n$ be open and let $u, w \in L^1_{\mathrm{loc}}(\Omega)$. The function $w$ is the **weak derivative** of $u$ with respect to $x_i$, written $w = \partial_iu$, if

$$
\int_\Omega u\,\partial_i\varphi\,dx = -\int_\Omega w\,\varphi\,dx \qquad \text{for every } \varphi \in C_c^\infty(\Omega).
$$

For a multi-index $\gamma = (\gamma_1,\dots,\gamma_n)$ the weak derivative $\partial^\gamma u$ is defined by iterating the definition, with $|\gamma| = \sum_i\gamma_i$ and $\partial^\gamma = \partial_1^{\gamma_1}\cdots\partial_n^{\gamma_n}$.

**Proposition (uniqueness).** The weak derivative, if it exists, is unique up to equality almost everywhere.

*Proof.* If $w_1$ and $w_2$ both satisfy the definition, then $\int_\Omega(w_1-w_2)\varphi = 0$ for every test function $\varphi$; since the test functions are dense in $L^1_{\mathrm{loc}}$ in the appropriate sense, $w_1-w_2=0$ almost everywhere. $\square$

**Example (a weak derivative that is not classical).** On $\Omega = (-1,1)$ let $u(x)=|x|$. Then $u$ is not differentiable at $0$, but

$$
w(x) = \operatorname{sgn}(x) = \begin{cases}-1, & x<0,\\ +1, & x>0\end{cases}
$$

is the weak derivative: for every $\varphi \in C_c^\infty(-1,1)$,

$$
\int_{-1}^{1}|x|\,\varphi'(x)\,dx = -\int_{-1}^{1} w(x)\varphi(x)\,dx,
$$

by integrating each piece by parts, the boundary terms vanishing because $\varphi$ is compactly supported and at $0$ cancelling. The computation is exact and shows that the weak derivative records the jumps of $u$ and ignores its points of non-differentiability.

**Definition.** For $1\le p\le\infty$ and $k \in \mathbb{N}$ the **Sobolev space** is

$$
W^{k,p}(\Omega) = \bigl\{u \in L^p(\Omega) : \partial^\gamma u \in L^p(\Omega) \text{ for all } |\gamma|\le k\bigr\},
$$

with the norm

$$
\|u\|_{W^{k,p}} = \Bigl(\sum_{|\gamma|\le k}\|\partial^\gamma u\|_{L^p}^p\Bigr)^{1/p} \ (p<\infty), \qquad
\|u\|_{W^{k,\infty}} = \max_{|\gamma|\le k}\|\partial^\gamma u\|_{L^\infty} .
$$

The notation $H^k(\Omega) = W^{k,2}(\Omega)$ is used when $p=2$, and $W^{k,p}_0(\Omega)$ is the closure of $C_c^\infty(\Omega)$ in $W^{k,p}(\Omega)$.

**Theorem (completeness).** $W^{k,p}(\Omega)$ is a Banach space, separable for $p<\infty$ and reflexive for $1<p<\infty$; $H^k(\Omega)$ is a separable Hilbert space with the inner product

$$
\langle u,v\rangle_{H^k} = \sum_{|\gamma|\le k}\int_\Omega \partial^\gamma u\,\partial^\gamma v\,dx .
$$

*Proof.* The map $u \mapsto (\partial^\gamma u)_{|\gamma|\le k}$ embeds $W^{k,p}$ isometrically as a closed subspace of the product of finitely many copies of $L^p(\Omega)$, which is a Banach space; a Cauchy sequence in $W^{k,p}$ therefore has a limit in each copy, the limits are the weak derivatives of the limit function, and completeness follows. Separability and reflexivity are inherited from $L^p$ for the stated ranges of $p$. $\square$

**Theorem (calculus).** If $u,v \in W^{k,p}(\Omega)\cap L^\infty(\Omega)$ then $uv \in W^{k,p}(\Omega)$ and the product rule holds; if $F \in C^k(\mathbb{R})$ with $F(0)=0$ and $F'$ bounded, then $F\circ u \in W^{k,p}(\Omega)$ for $u \in W^{k,p}(\Omega)$; and the chain rule holds for a $C^k$ diffeomorphism of the domain.

*Proof.* The identities are proved first for smooth approximants and pass to the limit in $L^p$ by the density theorem below; the product rule $\partial_i(uv) = \partial_iu\cdot v + u\cdot\partial_iv$ holds almost everywhere for the approximants and its limit is the weak derivative of the product. $\square$

**Theorem (density, Meyers–Serrin).** $C^\infty(\Omega)\cap W^{k,p}(\Omega)$ is dense in $W^{k,p}(\Omega)$ for every open $\Omega$; if $\Omega$ is bounded with Lipschitz boundary, then $C^\infty(\overline\Omega)$ is dense. Consequently the product and chain rules hold for all $u$ of the space, by approximation.

*Proof.* Quoted as standard. The first statement is proved by localising with a partition of unity subordinate to a cover by balls contained in $\Omega$ and mollifying; the second adds a boundary-flattening argument using the Lipschitz condition, in which the reflected function is mollified and restricted. $\square$

**Remark (the role of $\Omega$).** The spaces and the interior results below require no regularity of $\partial\Omega$, because they are local. Every statement about traces, about the boundary values of a Sobolev function and about the density of $C^\infty(\overline\Omega)$ needs $\partial\Omega$ to be at least Lipschitz, and this is the hypothesis under which the theory of boundary-value problems is stated.

## Embedding, Compactness and Traces

### The Sobolev Inequalities

**Theorem (Gagliardo–Nirenberg–Sobolev).** Let $1\le p<n$ and $k\ge1$ with $kp<n$. Then there is a constant $C$ with

$$
\|u\|_{L^{p^*}(\mathbb{R}^n)} \le C\sum_{|\gamma|=k}\|\partial^\gamma u\|_{L^p(\mathbb{R}^n)}, \qquad \frac1{p^*} = \frac1p - \frac{k}{n},
$$

for every $u \in C_c^\infty(\mathbb{R}^n)$; consequently $W^{k,p}(\mathbb{R}^n) \hookrightarrow L^{p^*}(\mathbb{R}^n)$, the embedding being continuous. The exponent $p^*$ is the **Sobolev conjugate** of $p$ at order $k$, and it is the largest $q$ for which such an estimate can hold.

*Proof.* Quoted as standard. For $k=1$ the inequality follows from the one-dimensional fundamental theorem of calculus applied in each coordinate and the Hölder and arithmetic–geometric inequalities; the case $k>1$ follows by iterating it. Sharpness is shown by testing the inequality on the family $u_\varepsilon(x) = \varepsilon^{-n/p^*}\eta(x/\varepsilon)$ for a fixed $\eta \in C_c^\infty$: all the norms on the left are then constant in $\varepsilon$ while the right-hand side stays bounded only for $q\le p^*$. $\square$

**Theorem (Morrey, the case $kp>n$).** If $kp>n$, then there is a constant $C$ with

$$
\|u\|_{C^{m,\gamma}(\mathbb{R}^n)} \le C\|u\|_{W^{k,p}(\mathbb{R}^n)}, \qquad m = k-\lfloor n/p\rfloor-1, \quad \gamma = \lfloor n/p\rfloor+1-\frac np ,
$$

whenever $kp>n$ and $n/p$ is not an integer; the embedding is continuous, so $W^{k,p}$ embeds into a Hölder space and in particular into the continuous functions. In the limiting case $kp=n$, $W^{k,p}$ embeds into $L^q$ for every finite $q$, but not into $L^\infty$.

*Proof.* Quoted as standard. The case $k=1$, $p>n$ is the Morrey inequality, proved by estimating $|u(x)-u(y)|$ by the integral of the derivative along a suitable path; the general case follows by applying it to the derivatives and iterating. $\square$

**Theorem (Rellich–Kondrachov).** Let $\Omega$ be bounded with Lipschitz boundary and let $1\le p<n$. Then the embedding $W^{1,p}(\Omega)\hookrightarrow L^q(\Omega)$ is **compact** for every $q<p^*$, and the embedding $W^{1,p}_0(\Omega)\hookrightarrow L^p(\Omega)$ is compact.

*Proof.* Quoted as standard. The proof approximates a bounded sequence in $W^{1,p}$ by mollifications, which are uniformly bounded and equicontinuous on compact subdomains, extracts a convergent subsequence by Arzelà–Ascoli, and estimates the boundary layer by the boundedness of the $W^{1,p}$ norm and the finiteness of the measure of the layer. $\square$

**Theorem (trace).** Let $\Omega$ be bounded with Lipschitz boundary and $1\le p<\infty$. There is a bounded linear map, the **trace**,

$$
\operatorname{tr} : W^{1,p}(\Omega) \to L^p(\partial\Omega), \qquad
\|{\operatorname{tr}}\,u\|_{L^p(\partial\Omega)} \le C\|u\|_{W^{1,p}(\Omega)},
$$

agreeing with the restriction for $u \in C(\overline\Omega)$, and its kernel is exactly $W^{1,p}_0(\Omega)$. For $p<n$ the trace actually maps into $L^q(\partial\Omega)$ for $q \le \frac{p(n-1)}{n-p}$.

*Proof.* Quoted as standard (the trace theorem). The estimate is proved for smooth functions by a boundary-flattening change of variables and the fundamental theorem of calculus in the normal direction, and extended to $W^{1,p}$ by the density of $C^\infty(\overline\Omega)$. The identification of the kernel uses the same density: a function whose trace vanishes is a limit of smooth compactly supported functions. $\square$

**Theorem (Poincaré and Friedrichs).** If $\Omega$ is bounded in one direction with width $L$, then for $u \in W^{1,p}_0(\Omega)$,

$$
\|u\|_{L^p(\Omega)} \le L\|\nabla u\|_{L^p(\Omega)}, \qquad 1\le p<\infty ,
$$

and for $u \in W^{1,p}(\Omega)$ with $\int_\Omega u = 0$ the same inequality holds with a constant depending only on $\Omega$. On the interval $(0,L)$ with $p=2$ the sharp constant is $L/\pi$.

*Proof.* Extend $u$ by zero to a slab of width $L$ in which $\Omega$ lies and apply the fundamental theorem of calculus along the direction of the slab; the case of zero mean follows by subtracting the mean and using the same argument. On $(0,L)$ the function is expanded in the Dirichlet sine series, and comparing $\sum b_k^2(k\pi/L)^2 \ge (\pi/L)^2\sum b_k^2$ gives the sharp constant $L/\pi$. $\square$

### The Spaces $H^{-1}$ and the Weak Formulation

**Definition.** The **dual space** $H^{-1}(\Omega)$ is the space of bounded linear functionals on $H^1_0(\Omega)$, normed by $\|F\|_{H^{-1}} = \sup\{|F(v)| : \|v\|_{H^1_0}\le1\}$. Every $f \in L^2(\Omega)$ defines an element of $H^{-1}$ by $F(v) = \int_\Omega fv$, and by the Riesz representation theorem on the Hilbert space $H^1_0$ every element of $H^{-1}$ is of the form $F(v) = \langle u, v\rangle_{H^1_0}$ for a unique $u \in H^1_0$.

**Definition.** Let $a : H\times H \to \mathbb{R}$ be a bilinear form on a real Hilbert space $H$. It is **bounded** if $|a(u,v)| \le M\|u\|\|v\|$ and **coercive** if $a(u,u) \ge m\|u\|^2$ for some $m>0$.

**Theorem (Lax–Milgram).** Let $a$ be a bounded coercive bilinear form on the Hilbert space $H$ and let $F \in H^*$. Then there is a unique $u \in H$ with

$$
a(u,v) = F(v) \qquad \text{for every } v \in H ,
$$

and $\|u\| \le m^{-1}\|F\|_{H^*}$.

*Proof.* For each $u$ the functional $v \mapsto a(u,v)$ is bounded, so there is $Au \in H$ with $a(u,v) = \langle Au,v\rangle$; $A$ is bounded with $\|A\|\le M$ and coercive, $\langle Au,u\rangle \ge m\|u\|^2$, hence injective with closed range. The range is also dense: if $a(u,w)=0$ for every $u$, then taking $u=w$ gives $0=a(w,w)\ge m\|w\|^2$, so $w=0$. A closed dense subspace is all of $H$, so $A$ is bijective and $u = A^{-1}R^{-1}F$ with $R$ the Riesz map. The norm bound follows from coercivity applied to the equation with $v=u$. $\square$

## Weak Solutions of Elliptic Problems

### Existence

**Definition.** Let $\Omega$ be bounded with Lipschitz boundary, let $f \in L^2(\Omega)$ and let $A$ be a bounded measurable matrix field on $\Omega$ satisfying the ellipticity condition

$$
\lambda|\xi|^2 \le \xi\cdot A(x)\xi \le \Lambda|\xi|^2 \qquad (x \in \Omega,\ \xi \in \mathbb{R}^n)
$$

for constants $0<\lambda\le\Lambda$. A function $u \in H^1_0(\Omega)$ is a **weak solution** of the Dirichlet problem

$$
-\nabla\cdot(A\nabla u) + cu = f \ \text{in }\Omega, \qquad u = 0 \ \text{on }\partial\Omega,
$$

with $c \ge 0$ a bounded function, if

$$
a(u,v) := \int_\Omega\bigl(A\nabla u\cdot\nabla v + c\,uv\bigr)dx = \int_\Omega fv\,dx \qquad \text{for every } v \in H^1_0(\Omega).
$$

**Theorem (existence and uniqueness).** Under the ellipticity condition, and with $c\ge0$ bounded, the Dirichlet problem has a unique weak solution $u \in H^1_0(\Omega)$ for every $f \in L^2(\Omega)$, and

$$
\|u\|_{H^1_0} \le \frac{1+C_P^2}{\lambda}\|f\|_{L^2},
$$

where $C_P$ is the Poincaré constant of $\Omega$.

*Proof.* The form $a$ is bounded with $M \le \Lambda + \|c\|_\infty$ by Cauchy–Schwarz, and coercive with $m = \lambda\min(1,C_P^{-2})$ after adding the positive term $cu$ if $c$ is not identically zero; the functional $v\mapsto\int fv$ is bounded on $H^1_0$ with norm at most $\|f\|_{L^2}$. Lax–Milgram gives a unique $u$, and the estimate is the coercivity inequality applied with $v=u$. $\square$

**Example (the Laplacian on an interval).** For $-\Delta$ on $(0,L)$ with $f \in L^2$, the weak solution is $u(x) = \int_0^L G(x,s)f(s)ds$ with $G$ the Green function of the preceding article; the weak formulation, tested against $v \in H^1_0$, is the integrated form of the equation, and for $f$ continuous the solution is the classical one of class $C^2$. The example shows that the weak formulation contains the classical theory and extends it to data that is only square-integrable.

### Regularity

**Theorem (interior regularity).** Let $u \in H^1(\Omega)$ be a weak solution of $-\nabla\cdot(A\nabla u) + cu = f$ in the sense that the weak formulation holds for all $v \in H^1_0(\Omega)$, with $A$ Lipschitz and uniformly elliptic, $c$ bounded and $f \in L^2(\Omega)$. Then for every subdomain $\Omega'\Subset\Omega$ one has $u \in H^2(\Omega')$ and

$$
\|u\|_{H^2(\Omega')} \le C\bigl(\|u\|_{L^2(\Omega)} + \|f\|_{L^2(\Omega)}\bigr),
$$

with $C$ depending on $\Omega'$, $\Omega$, the ellipticity constants and the bounds on the coefficients. If $f \in H^k(\Omega)$ for all $k$, then $u \in H^{k+2}_{\mathrm{loc}}(\Omega)$ and hence, by the embedding theorem, $u \in C^\infty(\Omega)$: **Weyl's lemma**, that a weak solution of an elliptic equation with smooth coefficients is smooth.

*Proof.* Quoted as standard. One takes difference quotients of the weak formulation in a direction $e_i$, uses the ellipticity to bound the $L^2$ norms of the difference quotients of $\nabla u$ by the data, and concludes that $\partial_i\nabla u \in L^2_{\mathrm{loc}}$; iterating gives the higher derivatives, and the Morrey embedding gives continuity. $\square$

**Theorem (boundary regularity).** If in addition $\Omega$ has $C^{k+2}$ boundary, $A \in C^{k+1}(\overline\Omega)$, $c\in C^k(\overline\Omega)$ and $f \in H^k(\Omega)$, then the weak solution with zero boundary values lies in $H^{k+2}(\Omega)\cap H^1_0(\Omega)$, with the corresponding estimate; in particular for $k=0$ and $\Omega$ of class $C^2$ the solution lies in $H^2(\Omega)$.

*Proof.* Quoted as standard. The boundary is flattened by a $C^{k+2}$ diffeomorphism, the equation is transformed and the direction normal to the boundary is treated first, using the vanishing of the trace and the difference-quotient technique in the tangential directions; the normal derivative is then recovered from the equation itself. $\square$

**Corollary (Fredholm alternative for the elliptic problem).** For a bounded Lipschitz domain and bounded elliptic coefficients, the operator $u \mapsto -\nabla\cdot(A\nabla u)+cu$, considered from $H^1_0(\Omega)$ to $H^{-1}(\Omega)$, is a bounded linear operator whose range is closed with finite-dimensional cokernel; the equation $Lu=f$ has a solution for every $f$ if and only if the homogeneous equation $Lu=0$ has only the zero solution, and in that case the solution is unique.

*Proof.* By the Riesz representation theorem the equation is equivalent to $Au=F$ with $A$ the bounded operator generated by $a$; the Rellich–Kondrachov theorem makes $A$ a compact perturbation of the coercive operator, so the standard Fredholm theory of compact operators on a Hilbert space applies and gives closed range, finite-dimensional kernel and cokernel, and the alternative. $\square$

## Parabolic and Hyperbolic Equations

### The Galerkin Method

**Definition.** Let $V$ be a separable Hilbert space dense and continuously embedded in a Hilbert space $H$, with $V^*$ the dual, and let $a(t;\cdot,\cdot)$ be bounded coercive symmetric forms on $V$ depending measurably on $t \in (0,T)$. A function

$$
u \in L^2(0,T;V), \qquad u' \in L^2(0,T;V^*)
$$

is a **weak solution** of the parabolic problem $u' + A(t)u = f$, $u(0)=u_0 \in H$, if

$$
\langle u'(t),v\rangle + a(t;u(t),v) = \langle f(t),v\rangle \qquad \text{for every } v \in V,
$$

for almost every $t$, the pairing being between $V^*$ and $V$.

**Theorem (Galerkin existence).** Under the boundedness and coercivity hypotheses there is a unique weak solution for every $f \in L^2(0,T;V^*)$ and $u_0 \in H$, and the energy estimate

$$
\|u(t)\|_H^2 + m\int_0^t\|u(s)\|_V^2\,ds \le \|u_0\|_H^2 + \frac1m\int_0^t\|f(s)\|^2_{V^*}\,ds
$$

holds for almost every $t$.

*Proof.* Choose an orthonormal basis $(w_j)$ of $V$ and seek the finite-dimensional Galerkin approximations $u_m(t) = \sum_{j\le m}d_j(t)w_j$ solving the projected system, an ordinary linear system in $d_j$; the energy estimate, valid at each level and uniform in $m$, bounds the approximations in $L^\infty(0,T;H)\cap L^2(0,T;V)$. A weak-compactness argument (Banach–Alaoglu) extracts a limit $u$, and the limit satisfies the weak formulation after passage to the limit in each projection; uniqueness follows from the estimate applied to the difference of two solutions with $f=0$ and $u_0=0$. $\square$

**Example (the heat equation).** For $V = H^1_0(\Omega)$, $H = L^2(\Omega)$ and $a(u,v) = \int\nabla u\cdot\nabla v$, the parabolic theorem gives the weak solution of $u_t=\Delta u$ with $u(0)=u_0\in L^2(\Omega)$, which is unique and lies in $L^2(0,T;H^1_0)\cap C([0,T];L^2)$; the energy estimate is the decay $\|u(t)\|_{L^2}^2 + 2\int_0^t\|\nabla u\|^2 \le \|u_0\|^2$. For $u_0$ continuous and bounded this is the classical solution of the preceding article obtained by convolution.

**Remark (hyperbolic equations).** For the wave equation the formulation is two-sided in time: $u \in L^2(0,T;H^1_0)$ with $u' \in L^2(0,T;L^2)$ and $u'' \in L^2(0,T;H^{-1})$, and the Galerkin argument with the second-order equation in $t$ gives existence and uniqueness for data $(u_0,u_1) \in H^1_0\times L^2$ together with the energy identity

$$
\frac12\|u'(t)\|_{L^2}^2 + \frac12\|\nabla u(t)\|_{L^2}^2 = \frac12\|u_1\|_{L^2}^2 + \frac12\|\nabla u_0\|_{L^2}^2 ,
$$

which is the conservation of energy of the classical theory, now proved for weak solutions and without any regularity of the data beyond square-integrability.

## The Variational Characterisation

**Theorem (Dirichlet principle).** Let $\Omega$ be bounded, $A$ uniformly elliptic and symmetric, and define on $H^1_0(\Omega)$

$$
J(v) = \frac12\int_\Omega A\nabla v\cdot\nabla v\,dx - \int_\Omega fv\,dx, \qquad f \in L^2(\Omega).
$$

Then $J$ is coercive and strictly convex, it attains its minimum at a unique $u \in H^1_0(\Omega)$, and $u$ is exactly the weak solution of $-\nabla\cdot(A\nabla u)=f$, $u|_{\partial\Omega}=0$.

*Proof.* Coercivity follows from the ellipticity and the Poincaré inequality: $J(v) \ge \frac\lambda2\|\nabla v\|^2 - \|f\|\|v\| \ge \frac\lambda4\|\nabla v\|^2 - C\|f\|^2$, so $J$ tends to infinity at infinity and is bounded below. Strict convexity follows from the strict positivity of the quadratic part. A minimising sequence is bounded in $H^1_0$, hence has a weakly convergent subsequence by reflexivity, and $J$ is weakly lower semicontinuous because the quadratic part is; the limit $u$ minimises. At a minimiser, $J(u+tv)\ge J(u)$ for all $t$ gives $a(u,v)-\int fv=0$ on differentiating at $t=0$, and the symmetry of $A$ is used exactly here, to identify the derivative of the quadratic part. Conversely a weak solution minimises $J$ because $J(u+v)-J(u) = \frac12\int A\nabla v\cdot\nabla v\ge0$; uniqueness is strict convexity. $\square$

The Dirichlet principle is the origin of the subject and the reason for the name of the space: the weak solution is the minimiser of an energy, and the minimisation can be carried out in $H^1_0$ even when no classical minimiser exists. The general theory of minimisation problems of this kind — lower semicontinuity, convexity, the Euler–Lagrange equation, and the direct method of the calculus of variations in which a minimiser is found by compactness — is developed in the article of this Part on the calculus of variations, where the present theorem appears as the model case.

## Summary

The weak derivative of $u \in L^1_{\mathrm{loc}}(\Omega)$ is the function $w$ for which $\int u\,\partial_i\varphi = -\int w\varphi$ for every test function $\varphi \in C_c^\infty(\Omega)$; it is unique when it exists and it exists for functions that are not classically differentiable, as $|x|$ shows. The Sobolev space $W^{k,p}(\Omega)$ consists of the $L^p$ functions whose weak derivatives up to order $k$ lie in $L^p$; it is a Banach space, separable and reflexive for $1<p<\infty$, and $H^k = W^{k,2}$ is a Hilbert space. Smooth functions are dense, the product and chain rules hold, and $W^{k,p}_0$ is the closure of the compactly supported smooth functions, which is how the Dirichlet boundary condition is imposed.

The embedding theorems are the working tools: $W^{k,p}\hookrightarrow L^{p^*}$ with $1/p^* = 1/p-k/n$ when $kp<n$, with $p^*$ sharp; $W^{k,p}\hookrightarrow C^{m,\gamma}$ when $kp>n$; the embeddings are compact into $L^q$ for $q<p^*$ on a bounded Lipschitz domain by Rellich–Kondrachov; the trace map restricts $W^{1,p}(\Omega)$ to $L^p(\partial\Omega)$ with kernel $W^{1,p}_0$; and the Poincaré inequality controls the $L^p$ norm by the gradient for a function vanishing on the boundary, with the sharp constant $L/\pi$ on the interval $(0,L)$.

An elliptic Dirichlet problem with uniformly elliptic coefficients and $L^2$ data has a unique weak solution in $H^1_0(\Omega)$ by the Lax–Milgram theorem, with the energy estimate $\|u\|_{H^1}\le C\lambda^{-1}\|f\|_{L^2}$; the solution is $H^2$ in the interior and near a smooth boundary when the data allow, and is $C^\infty$ when the data are, which is Weyl's lemma; the inhomogeneous problem satisfies the Fredholm alternative. The parabolic and hyperbolic equations are solved weakly by the Galerkin method, with the energy estimates that the method is built on. Finally the weak solution of a symmetric elliptic problem is the unique minimiser of the Dirichlet energy $J$, the Dirichlet principle, which is the model case of the direct method of the calculus of variations.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Omega \subseteq \mathbb{R}^n$ | Open domain; $\partial\Omega$ its boundary, Lipschitz unless stated |
| $C_c^\infty(\Omega)$ | Smooth compactly supported test functions |
| $\partial^\gamma$ | Weak derivative for the multi-index $\gamma$ |
| $W^{k,p}(\Omega)$, $W^{k,p}_0(\Omega)$ | Sobolev spaces, with and without zero boundary values |
| $H^k(\Omega) = W^{k,2}(\Omega)$ | Sobolev–Hilbert space |
| $p^* = np/(n-p)$ | Sobolev conjugate exponent |
| $\operatorname{tr}$ | Trace map $W^{1,p}(\Omega)\to L^p(\partial\Omega)$ |
| $C_P$ | Poincaré constant |
| $H^{-1}(\Omega)$ | Dual of $H^1_0(\Omega)$ |
| $a(u,v)$ | Bilinear form (energy form) of the elliptic problem |
| $M$, $m$ | Boundedness and coercivity constants of $a$ |
| $A(x)$, $\lambda$, $\Lambda$ | Coefficient matrix and ellipticity constants |
| Lax–Milgram | Unique solvability of $a(u,v)=F(v)$ |
| $u \in L^2(0,T;V)$ | Bochner space of $V$-valued square-integrable functions |
| $J(v)$ | Dirichlet energy functional |

## Further Reading

- Robert A. Adams and John J. F. Fournier, *Sobolev Spaces* (Academic Press, 2nd ed. 2003), for the spaces, the embedding theorems and the trace theorem.
- David Gilbarg and Neil S. Trudinger, *Elliptic Partial Differential Equations of Second Order* (Springer, 2nd ed. 1983), for weak solutions, the Lax–Milgram theory and regularity.
- Lawrence C. Evans, *Partial Differential Equations* (American Mathematical Society, 2nd ed. 2010), for the weak formulation and the Galerkin method for parabolic and hyperbolic problems.
- Haïm Brezis, *Functional Analysis, Sobolev Spaces and Partial Differential Equations* (Springer, 2011), for the Hilbert-space treatment and the variational characterisation.
- John L. Lions and Enrico Magenes, *Non-Homogeneous Boundary Value Problems and Applications I* (Springer, 1972), for the interpolation and trace theory.
- Olga A. Ladyzhenskaya, *The Boundary Value Problems of Mathematical Physics* (Springer, 1985), for the energy estimates in the classical form.
- Kosaku Yosida, *Functional Analysis* (Springer, 6th ed. 1980), for the Lax–Milgram theorem and the Fredholm alternative in Banach space.
- Enrico Giusti, *Direct Methods in the Calculus of Variations* (World Scientific, 2003), for the direct method continued in the variational article.
