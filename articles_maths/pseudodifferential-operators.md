
# __Pseudodifferential Operators__

## Introduction

A linear differential operator of order $m$ has a symbol $\sum_{|\alpha|\le m}a_\alpha(x)\xi^\alpha$, a polynomial in the frequency variable whose highest-order part, the principal symbol, decides whether the operator is elliptic and whether it can be inverted to leading order. The single idea of pseudodifferential theory is to allow the symbol to be any smooth function of $x$ and $\xi$ of the appropriate growth, and to define the operator by the Fourier inversion formula

$$
a(x,D)u(x)=\frac{1}{(2\pi)^n}\int_{\mathbb{R}^n}\int_{\mathbb{R}^n}e^{i(x-y)\cdot\xi}\,a(x,\xi)\,u(y)\,dy\,d\xi .
$$

The class of operators so obtained is closed under composition, under transposition and under the construction of parametrices, and it contains the differential operators, the inverses of elliptic operators and the smoothing operators, together with a calculus of symbols in which composition corresponds to an asymptotic expansion to all orders. The calculus is the natural home of the elliptic regularity of *Distributions and Fundamental Solutions*, and it is the technical foundation of the microlocal analysis: the principal symbol lives on the cotangent bundle, and its vanishing set is where the operator fails to be invertible.

The article begins with the **symbol classes** $S^m$ and the asymptotic summation that makes them an algebra; it defines the **quantisation** $a\mapsto a(x,D)$; it proves that the class is closed under composition and adjoint, with the Leibniz-type expansions

$$
c(x,\xi)\sim\sum_\alpha\frac{1}{\alpha!}\,\partial_\xi^\alpha a(x,\xi)\,D_x^\alpha b(x,\xi), \qquad [a(x,D),b(x,D)] \sim \frac1i\{a,b\}(x,D),
$$

where $\{a,b\}$ is the Poisson bracket; it characterises **ellipticity** and constructs the **parametrix** by solving the composition equation order by order; it records the continuity on $L^2$ and on the Sobolev spaces, and Gårding's inequality; and it treats the **Weyl quantisation** and the invariance of the principal symbol under changes of coordinates, which is what allows the calculus to be carried to a manifold.

Throughout, $\mathbb{K}=\mathbb{C}$ for symbols and operators, $x \in \mathbb{R}^n$ is the space variable and $\xi \in \mathbb{R}^n$ the frequency variable, $\alpha,\beta$ are multi-indices, and $D^\alpha=(-i)^{|\alpha|}\partial^\alpha$ is the derivative convention fixed in *Distributions and Fundamental Solutions*, so that the symbol of the differential operator $\sum_{|\alpha|\le m}a_\alpha(x)D^\alpha$ is $\sum a_\alpha(x)\xi^\alpha$. The Fourier transform and its normalisation, the distributions $\mathcal D'$, $\mathcal S'$ and their pairings, and the kernel $K(x,y)$ of an operator are those of *Distributions and Fundamental Solutions* and *The Schwartz Kernel Theorem*. The Bessel-potential spaces $H^s_p$ and their interpolation are those of *Interpolation Theory*. Ellipticity, the parametrix and elliptic regularity were stated for differential operators in *Distributions and Fundamental Solutions*; here they are proved in the symbol calculus. The Fredholm property of an elliptic operator, the index and its invariance are those of *Fredholm Theory*. The wavefront set, the propagation of singularities and the microlocal elliptic regularity are not covered here; the $\hbar$-dependent form of the calculus, the semiclassical defect measures and Egorov's theorem are not covered here; and the elliptic boundary-value problems and the classical classification of second-order equations are those andin the extension of this Part. The principal symbols of the classical operators, and the Cauchy–Riemann operator $e_\mu\partial_\mu$, are treated in the algebra-valued analysis of this Part .

No physics is invoked.

## Symbol Classes

### Definition and Elementary Properties

**Definition.** For $m \in \mathbb{R}$ the **symbol class** $S^m=S^m(\mathbb{R}^n\times\mathbb{R}^n)$ is the set of $a \in C^\infty(\mathbb{R}^n\times\mathbb{R}^n)$ such that for all multi-indices $\alpha,\beta$ there is $C_{\alpha,\beta}$ with

$$
|\partial_\xi^\alpha\partial_x^\beta a(x,\xi)| \le C_{\alpha,\beta}\,(1+|\xi|)^{m-|\alpha|}
$$

for all $x,\xi$; the class $S^m_{1,0}$ of Hörmander is the one used here and is written $S^m$. Set $S^\infty=\bigcup_mS^m$ and $S^{-\infty}=\bigcap_mS^m$. The **order** of $a$ is the infimum of the $m$ with $a \in S^m$; a symbol in $S^{-\infty}$ is called **smoothing**.

The derivatives in $x$ are unrestricted, the derivatives in $\xi$ gain a power of $(1+|\xi|)^{-1}$ each time, and the definition is an estimate on $a$ and all of its derivatives; this is the exact regularity needed for the composition formula and for the parametrix.

**Proposition.** (i) $S^m \subseteq S^{m'}$ for $m \le m'$, and $S^{-\infty}=\bigcap_mS^m$. (ii) If $a \in S^m$ and $b \in S^{m'}$ then the pointwise product $ab \in S^{m+m'}$. (iii) $\partial_x^\beta a \in S^m$, $\partial_\xi^\alpha a \in S^{m-|\alpha|}$, and $S^m$ is a Fréchet space in the seminorms of the definition. (iv) If $a \in S^m$ and $a$ is a polynomial of degree $m$ in $\xi$ with coefficients in $C^\infty(\mathbb{R}^n)$ of at most polynomial growth, then $a$ is the symbol of a differential operator of order $m$.

*Proof.* (i)–(iii) are immediate from the product rule and the definition; (iv) because a polynomial of degree $m$ in $\xi$ satisfies the estimates with $|\alpha|\le m$ and has zero $\xi$-derivatives of higher order. $\square$

**Example.** (i) The monomial $\xi^\alpha$ lies in $S^{|\alpha|}$; the symbol of a differential operator $\sum_{|\alpha|\le m}a_\alpha\xi^\alpha$ with $a_\alpha \in C^\infty$ of polynomial growth lies in $S^m$.

(ii) The **Bessel symbol** $(1+|\xi|^2)^{s/2}$ lies in $S^s$, and the operator it defines is the Bessel potential $\langle D\rangle^s$ of *Interpolation Theory* up to the convention of the constant.

(iii) The function $a(\xi)=\chi(|\xi|)|\xi|^m$ with $\chi$ a smooth cutoff vanishing near $0$ lies in $S^m$ and is elliptic; the function $a(\xi)=\sin|\xi|^2$ is in $S^0$ but in no lower class, since its derivatives do not decay.

(iv) If $a \in S^m$ and $A$ is a constant-coefficient differential operator in the $x$ variables, then $a$, $Aa$ and $\partial_\xi^\alpha a$ remain in the corresponding classes, while $\frac{1}{a}$ is in $S^{-m}$ only under the ellipticity hypothesis below.

### Asymptotic Expansion

**Definition.** Let $a_j \in S^{m_j}$ with $m_j \to -\infty$. One writes

$$
a \sim \sum_{j=0}^{\infty}a_j
$$

if $a-\sum_{j<N}a_j \in S^{m_N}$ for every $N$; the relation determines the class of $a$ modulo $S^{-\infty}$.

**Theorem (asymptotic summation).** Given $a_j \in S^{m_j}$ with $m_j \downarrow -\infty$, there exists $a \in S^{m_0}$ with $a \sim\sum_ja_j$; any two such $a$ differ by an element of $S^{-\infty}$.

*Proof (sketch).* Choose a cutoff $\chi \in C^\infty(\mathbb{R}^n)$, vanishing for $|\xi|\le1$ and equal to $1$ for $|\xi|\ge2$, and a sequence $t_j \downarrow0$ tending to $0$ fast enough that the series

$$
a(x,\xi)=\sum_{j=0}^{\infty}\chi(t_j\xi)\,a_j(x,\xi)
$$

converges in $C^\infty$ on compact sets and satisfies the estimates of $S^{m_0}$; the rapid decrease of the tails (by the choice of $t_j$) gives $a-\sum_{j<N}a_j \in S^{m_N}$. The difference of two such sums is in $S^{m_N}$ for every $N$ and hence in $S^{-\infty}$. $\square$

The theorem is what makes the calculus possible: every computation below produces a formal series of symbols, and the series is summed by this device, with the resulting ambiguity confined to the smoothing class, which is harmless for all statements of a local or asymptotic nature.

## Quantisation

### The Fourier Definition

**Definition.** For $a \in S^m$ the **operator with symbol** $a$, in **left quantisation**, is

$$
a(x,D)u(x)=\frac{1}{(2\pi)^n}\int_{\mathbb{R}^n}\int_{\mathbb{R}^n}e^{i(x-y)\cdot\xi}a(x,\xi)\,u(y)\,dy\,d\xi, \qquad u \in \mathcal S(\mathbb{R}^n),
$$

the integral being understood as the iterated integral, which converges absolutely after regularisation and defines the oscillatory integral; equivalently, in terms of the Fourier transform,

$$
\widehat{a(x,D)u}(\xi)=\frac{1}{(2\pi)^n}\int_{\mathbb{R}^n}\hat a(\xi-\eta,\eta)\,\hat u(\eta)\,d\eta,
$$

where $\hat a(\cdot,\eta)$ is the Fourier transform of $a(\cdot,\eta)$ in the first variable. The operator extends to a continuous map $\mathcal S(\mathbb{R}^n)\to C^\infty(\mathbb{R}^n)$ and to a continuous map $\mathcal E'(\mathbb{R}^n)\to\mathcal D'(\mathbb{R}^n)$.

**Theorem (kernel).** The operator $a(x,D)$ has kernel

$$
K_a(x,y)=\frac{1}{(2\pi)^n}\int_{\mathbb{R}^n}e^{i(x-y)\cdot\xi}a(x,\xi)\,d\xi,
$$

a distribution on $\mathbb{R}^n\times\mathbb{R}^n$, in the sense of *The Schwartz Kernel Theorem*:

$$
\langle a(x,D)u,v\rangle=\langle K_a,v\otimes u\rangle ,
$$

The kernel is smooth off the diagonal $x=y$; the singularities of $a(x,D)$ are carried by the diagonal, and the symbol is the fibre transform of the kernel along the diagonal, which is the reason the symbol is the right object for the calculus.

**Example.** (i) $a(x,\xi)=\xi^\alpha$ gives $a(x,D)=D^\alpha$, since $\xi^\alpha e^{i(x-y)\xi}=(-i)^{|\alpha|}\partial_x^\alpha e^{i(x-y)\xi}$ and the integral reproduces $D^\alpha u$. Hence every differential operator $P=\sum_{|\alpha|\le m}a_\alpha(x)D^\alpha$ is the operator with symbol $\sum a_\alpha(x)\xi^\alpha$, and the class of pseudodifferential operators contains the differential operators.

(ii) $a(x,\xi)=a(x)$ independent of $\xi$ gives the operator of multiplication by $a$; its kernel is $a(x)\delta(x-y)$.

(iii) $a(x,\xi)=\chi(\xi)$ with $\chi$ smooth, supported where $|\xi|$ is large and $\chi=0$ near $0$, gives a smoothing-type operator whose kernel is the inverse Fourier transform of $\chi$; if $\chi\in C_c^\infty$ the operator is smoothing with a Schwartz kernel.

(iv) The inverse of an elliptic operator, when it exists, has a symbol in $S^{-m}$; this is the content of the parametrix construction below.

### Weyl and Other Quantisations

**Definition.** The **Weyl quantisation** of $a \in S^m$ is

$$
a^w(x,D)u(x)=\frac{1}{(2\pi)^n}\int_{\mathbb{R}^n}\int_{\mathbb{R}^n}e^{i(x-y)\cdot\xi}\,a\!\left(\frac{x+y}{2},\xi\right)u(y)\,dy\,d\xi ,
$$

and the Weyl symbol of an operator is the function $a$ producing it. The two quantisations differ by a series of lower-order terms: expanding $a((x+y)/2,\xi)$ about $x$ and integrating by parts in $\xi$ gives

$$
a^w(x,D)=a(x,D)+\frac{1}{2i}\sum_{j=1}^{n}\partial_{x_j}\partial_{\xi_j}a(x,D)+\cdots,
$$

the next correction being of order $m-2$, so that the principal symbols agree. The Weyl quantisation has the formal advantage that the adjoint has symbol $\overline a$: $(a^w)^*=\overline a^{\,w}$ for $a \in S^m$ on $\mathcal S$, so that real symbols give symmetric operators.

**Example (verification).** For $n=1$ and $a(x,\xi)=x\xi$ one computes directly that $a(x,D)=xD$ and that $a^w=xD-\frac{i}{2}I$; the displayed correction term is $\frac{1}{2i}\partial_x\partial_\xi(x\xi)=\frac{1}{2i}$, giving $a^w=xD+\frac{1}{2i}I=xD-\frac{i}{2}I$, in agreement. This is the simplest instance of the subprincipal correction.

## Composition and Adjoint

### The Composition Theorem

**Theorem (composition).** Let $a \in S^m$ and $b \in S^{m'}$. Then $a(x,D)b(x,D)=c(x,D)$ for a symbol $c \in S^{m+m'}$, unique modulo $S^{-\infty}$, with

$$
c(x,\xi)\sim\sum_{\alpha}\frac{1}{\alpha!}\,\partial_\xi^\alpha a(x,\xi)\,D_x^\alpha b(x,\xi),
$$

the sum over all multi-indices $\alpha$, where $D_x^\alpha=(-i)^{|\alpha|}\partial_x^\alpha$ acts on the $x$-variable of $b$. In particular the leading term is $c \equiv ab \bmod S^{m+m'-1}$.

*Proof (sketch).* Use the representation $a(x,D)v(x)=\frac{1}{(2\pi)^n}\int e^{ix\cdot\eta}a(x,\eta)\hat v(\eta)\,d\eta$, valid after regularisation. Then $\widehat{b(x,D)u}(\eta)=\frac{1}{(2\pi)^n}\int\hat b(\eta-\zeta,\zeta)\hat u(\zeta)\,d\zeta$, and substituting $\eta=\zeta+\theta$ gives

$$
a(x,D)b(x,D)u(x)=\frac{1}{(2\pi)^{2n}}\int\int e^{ix\cdot\zeta}\,e^{ix\cdot\theta}\,a(x,\zeta+\theta)\,\hat b(\theta,\zeta)\,\hat u(\zeta)\,d\zeta\,d\theta .
$$

Taylor expansion of $a(x,\zeta+\theta)$ in $\theta$ about $\zeta$ contributes the terms $\frac{1}{\alpha!}\partial_\xi^\alpha a(x,\zeta)\theta^\alpha$, and the inverse Fourier transform in $\theta$ of $\theta^\alpha\hat b(\theta,\zeta)$ is $D_x^\alpha b(x,\zeta)$; the remainder after $N$ terms is in $S^{m+m'-N}$. $\square$

**Example.** For $a=\xi_j$ and $b=x_k$, the composition is $D_jM_{x_k}$, and

$$
D_j(x_ku)=-i\partial_j(x_ku)=-i\delta_{jk}u+x_kD_ju=M_{x_k}D_ju-i\delta_{jk}u .
$$

The formula gives $c=\xi_jx_k+\frac{1}{1!}\partial_{\xi_j}\xi_j\,D_{x_j}x_k=x_k\xi_j+(-i)\delta_{jk}$, in agreement with the direct computation. The subprincipal term is what makes the calculus noncommutative.

**Corollary (leading order).** The principal symbol of a product is the product of the principal symbols, $\sigma_{m+m'}(a(x,D)b(x,D))=\sigma_m(a)\sigma_{m'}(b)$; the map $a\mapsto\sigma_m(a)$ is a homomorphism from the operators of order $m$ modulo smoothing to the functions on $T^*\mathbb{R}^n$ that are positively homogeneous of degree $m$ in $\xi$ modulo lower order.

**Corollary (commutator).** The commutator has leading order $m+m'-1$ and

$$
[a(x,D),b(x,D)] \;\sim\; \frac1i\{a,b\}(x,D) \pmod{S^{m+m'-2}}, \qquad \{a,b\}=\sum_{j=1}^{n}\bigl(\partial_{\xi_j}a\,\partial_{x_j}b-\partial_{x_j}a\,\partial_{\xi_j}b\bigr),
$$

the **Poisson bracket** of $a$ and $b$. For $a=\xi_j$, $b=x_k$ the bracket is $\delta_{jk}$ and the commutator is $-i\delta_{jk}I$, as computed above.

### The Adjoint

**Theorem (adjoint).** For $a \in S^m$ the formal adjoint of $a(x,D)$ with respect to the $L^2$ inner product is $a(x,D)^*=a^*(x,D)$ with

$$
a^*(x,\xi)\sim\sum_{\alpha}\frac{1}{\alpha!}\,\partial_\xi^\alpha D_x^\alpha\,\overline{a(x,\xi)} ,
$$

so that $a^* \in S^m$ and $a^* \equiv\overline a \bmod S^{m-1}$. In particular $a(x,D)$ is symmetric on $\mathcal S$ to leading order exactly when $a$ is real modulo $S^{m-1}$.

*Proof (sketch).* The identity $\langle a(x,D)u,v\rangle=\langle u,a(x,D)^*v\rangle$ is integrated by parts in $x$ and $\xi$; the boundary terms vanish for Schwartz functions, and the resulting symbol is the displayed transpose, which is computed by the same Taylor expansion as the composition theorem applied to the kernel $\overline{K_a(y,x)}$. $\square$

**Corollary (the calculus is an algebra).** The operators of the form $a(x,D)$ with $a \in S^\infty$, modulo the smoothing operators $S^{-\infty}(x,D)$, form an algebra with involution under composition and adjoint, filtered by the order, with associated graded algebra the symbols modulo lower order; the principal-symbol map is an isomorphism of the graded pieces onto the homogeneous functions on $T^*\mathbb{R}^n$ of the appropriate degree.

## Ellipticity and Parametrices

### Elliptic Symbols

**Definition.** A symbol $a \in S^m$ is **elliptic** if there is $c>0$ with

$$
|a(x,\xi)| \ge c\,(1+|\xi|)^m \qquad \text{for } |\xi| \text{ large},
$$

uniformly in $x$; if the estimate is required only on a subset of $\mathbb{R}^n_x$ one says that $a$ is elliptic there. The **principal symbol** $\sigma_m(a)$ is the class of $a$ in $S^m/S^{m-1}$, represented by the positively homogeneous function $a_m(x,\xi)=\lim_{t\to\infty}t^{-m}a(x,t\xi)$ for $\xi \neq0$; the ellipticity of $a$ is the nonvanishing of $a_m(x,\xi)$ for every $\xi \neq0$.

**Theorem (parametrix).** Let $a \in S^m$ be elliptic. Then there is $b \in S^{-m}$ with

$$
a(x,D)b(x,D)=I-R_1, \qquad b(x,D)a(x,D)=I-R_2, \qquad R_1,R_2 \in S^{-\infty}(x,D).
$$

*Proof (sketch).* Set $b_0$ equal to $a^{-1}$ for large $|\xi|$ and to $0$ for small $|\xi|$, cut off smoothly; then $b_0 \in S^{-m}$ and $ab_0-1=:r_0 \in S^{-1}$. If $b_N \in S^{-m}$ has been chosen with $ab_N=1+r_N$ and $r_N \in S^{-N}$, set $b_{N+1}=b_N-r_Na^{-1}$ with $a^{-1}$ again cut off for large $|\xi|$; then $b_{N+1} \in S^{-m}$ and

$$
ab_{N+1}=1+r_N-r_N(aa^{-1})=1+r_N-r_N(1+r_0)=1-r_Nr_0 \in 1+S^{-N-1},
$$

so the remainder improves by one order at each step. The recursion produces symbols $b_N$ with remainders in $S^{-N}$ for every $N$, and asymptotic summation gives $b \sim\sum_j(b_j-b_{j-1}) \in S^{-m}$ with $ab-1 \in S^{-\infty}$, which is the first identity. The second follows by the same argument on the other side, and the resulting left and right parametrices differ by a smoothing operator by associativity of composition. $\square$

### Elliptic Regularity

**Theorem (elliptic regularity, pseudodifferential form).** Let $a \in S^m$ be elliptic, properly supported, with bounded derivatives $|\partial_\xi^\alpha\partial_x^\beta a|\le C_{\alpha\beta}$, and let $R$ be smoothing. Then for every $s \in \mathbb{R}$ and $1<p<\infty$ the operator $a(x,D)$ maps $H^{s}_p$ continuously into $H^{s-m}_p$, and for $p=2$ no boundedness of the derivatives is required; consequently

$$
a(x,D)u \in H^{s-m}_p \implies u \in H^{s}_p, \qquad a(x,D)u \in C^\infty \implies u \in C^\infty ,
$$

the implications holding locally and, with proper support, globally.

*Proof.* The parametrix $b \in S^{-m}$ gives $u=b(au)+R_2u$; the first term is in $H^s_p$ because an operator of order at most $0$ whose symbol has bounded derivatives is bounded on $L^p$ for $1<p<\infty$ by the Calderón–Zygmund theory, and the $H^s_p$ norms are the $L^p$ norms of the Bessel potentials, so $b$ gains the $m$ orders of regularity; the second term is smoothing and lies in every $H^s_p$. $\square$

**Corollary (Fredholm property).** An elliptic operator $a(x,D)$ of order $m$ on a closed manifold, acting between $H^s$ and $H^{s-m}$, is Fredholm, with a parametrix in the sense of *Fredholm Theory*; its index is invariant under perturbations in the smoothing class.

## Continuity and Gårding's Inequality

### Boundedness on $L^2$ and Sobolev Spaces

**Theorem (Calderón–Vaillancourt).** Let $a \in S^0$. Then $a(x,D)$ extends to a bounded operator on $L^2(\mathbb{R}^n)$, with

$$
\|a(x,D)\|_{L^2\to L^2} \le C\sup_{|\alpha|+|\beta|\le N}\sup_{x,\xi}(1+|\xi|)^{|\alpha|}|\partial_\xi^\alpha\partial_x^\beta a(x,\xi)|
$$

for a constant $C$ and an integer $N$ depending only on the dimension.

*Proof (sketch).* Refine the symbol by a partition of the frequency space into dyadic annuli, write $a=\sum_ka_k$ with $a_k$ supported in $2^k\le|\xi|\le2^{k+1}$, and use the almost-orthogonality of the resulting frequency-localised pieces together with the Cotlar–Stein lemma; the estimates of the symbol class control the norms of the localised pieces and the overlaps. The detailed argument is the Calderón–Vaillancourt theorem quoted below. $\square$

**Theorem (continuity on Sobolev spaces).** Let $a \in S^m$. Then $a(x,D)$ maps $H^s_2$ continuously into $H^{s-m}_2$ for every $s \in \mathbb{R}$, and this follows from the $S^0$ boundedness applied to $a(x,D)\langle D\rangle^{-m}$ and the commutation of $\langle D\rangle^s$ with the calculus up to lower order. If in addition the derivatives of $a$ are bounded, $|\partial_\xi^\alpha\partial_x^\beta a|\le C_{\alpha\beta}$ for $|\alpha|+|\beta|\le N$, then the same continuity holds on $H^s_p$ for every $1<p<\infty$ and every $s$; the $L^2$ case is common to both hypotheses, and it is the case guaranteed by the preceding theorem for the full class $S^0$.

### Gårding's Inequality

**Theorem (Gårding).** Let $a \in S^1$ with $\operatorname{Re}a(x,\xi)\ge0$ for large $|\xi|$, and suppose $a(x,D)$ is properly supported. Then there is $C$ with

$$
\operatorname{Re}\langle a(x,D)u,u\rangle \ge -C\|u\|_{L^2}^2 \qquad \text{for all } u \in \mathcal S .
$$

More generally, if $a \in S^m$ is elliptic with $\operatorname{Re}a\ge c(1+|\xi|)^m>0$, then for all $u$,

$$
\operatorname{Re}\langle a(x,D)u,u\rangle \ge c'\|u\|_{H^{m/2}}^2-C\|u\|_{L^2}^2 .
$$

*Proof (sketch).* The sharp Gårding inequality is proved by writing $\operatorname{Re}a$ as a sum of squares modulo a symbol of order $0$, using a partition of the frequency space and a square-root argument for the positive homogeneous part; the elliptic case follows by applying the first to the order-one symbol $a(x,\xi)(1+|\xi|^2)^{-m/2}\langle\xi\rangle^{m}$ composed with a Bessel potential. The inequality is the analytic form of the positivity of an elliptic operator and it is the starting point of the existence theory for the Dirichlet problem, which belongs. $\square$

## Invariance and Operators on Manifolds

### Changes of Variables

The principal symbol is invariant in a precise sense, and this is what makes the calculus geometric.

**Theorem (invariance of the principal symbol).** Let $\kappa:\Omega\to\tilde\Omega$ be a diffeomorphism of open sets and let $T=a(x,D)$ be a pseudodifferential operator on $\tilde\Omega$; define the transported operator $\kappa^*T$ on $\Omega$ by $\kappa^*Tu=(T(u\circ\kappa^{-1}))\circ\kappa$. Then $\kappa^*T$ is pseudodifferential of order $m$, and its principal symbol is

$$
\sigma_m(\kappa^*T)(x,\xi)=\sigma_m(T)\bigl(\kappa(x),\,(d\kappa(x))^{-T}\xi\bigr),
$$

the action of the cotangent lift of $\kappa$; that is, the principal symbol is a function on the cotangent bundle $T^*M$, and a pseudodifferential operator of order $m$ on a manifold is defined by requiring that in every coordinate chart it be given by a symbol in $S^m$ and that the principal symbols so obtained agree as a function on $T^*M$.

*Proof (sketch).* The chain rule changes the differentiation operators by the Jacobian, and the frequency variable transforms by the inverse transpose of the differential; the lower-order terms depend on the second derivatives of $\kappa$ and illustrate why only the principal symbol is invariant. $\square$

### Pseudodifferential Operators on a Manifold

**Definition.** A **pseudodifferential operator** of order $m$ on a smooth manifold $M$ is a continuous linear map $T:\mathcal D(M)\to\mathcal D'(M)$ whose kernel is smooth off the diagonal and which in each coordinate chart is given by a symbol in $S^m$; the **principal symbol** is the well-defined function $\sigma_m(T) \in C^\infty(T^*M\setminus0)$, homogeneous of degree $m$ in the fibre variable, obtained from the local symbols by the invariance theorem. The operator is **elliptic** if $\sigma_m(T)$ does not vanish on the complement of the zero section.

**Theorem.** The pseudodifferential operators of finite order on $M$ form a filtered algebra under composition and adjoint, containing the differential operators, with principal-symbol map a homomorphism onto the homogeneous functions, and with a parametrix for every elliptic operator. Every elliptic operator on a closed manifold is Fredholm between the Sobolev spaces $H^s(M)$ and $H^{s-m}(M)$, and its kernel consists of smooth functions.

The index of such an operator depends only on its principal symbol and is computed by the Atiyah–Singer theorem in *The Atiyah–Singer Index Theorem and K-Theory*; the wavefront set and the propagation of singularities refine the local statement to one on the cotangent bundle and are developed; and the $\hbar$-dependent calculus, in which the symbols are functions on phase space and the composition is governed by the Poisson bracket to leading order, is developed.

## Summary

A symbol of order $m$ is a smooth function $a(x,\xi)$ satisfying $|\partial_\xi^\alpha\partial_x^\beta a|\le C(1+|\xi|)^{m-|\alpha|}$; the classes $S^m$ are nested, closed under products and differentiation, form a Fréchet space, and admit asymptotic summation, so that any formal series with decreasing orders is represented by a symbol unique modulo the smoothing class $S^{-\infty}$. The quantisation $a\mapsto a(x,D)$ is defined by the Fourier inversion integral, its kernel is $K_a(x,y)=\frac{1}{(2\pi)^n}\int e^{i(x-y)\xi}a(x,\xi)d\xi$ and is smooth off the diagonal, and it contains the differential operators as the polynomial symbols. The Weyl quantisation differs from the left quantisation by $\frac{1}{2i}\sum_j\partial_{x_j}\partial_{\xi_j}a$ plus lower order and has the advantage that the adjoint is the conjugate symbol.

The calculus is closed: $a(x,D)b(x,D)=c(x,D)$ with $c\sim\sum_\alpha\frac{1}{\alpha!}\partial_\xi^\alpha a\,D_x^\alpha b$, the leading term is the product of the principal symbols, and the commutator has leading order $m+m'-1$ with symbol $\frac1i\{a,b\}$, the Poisson bracket. The adjoint is $a^*(x,\xi)\sim\sum_\alpha\frac{1}{\alpha!}\partial_\xi^\alpha D_x^\alpha\overline{a}$. An elliptic symbol, one bounded below by $c(1+|\xi|)^m$ for large $|\xi|$, has a parametrix $b \in S^{-m}$ with $ab-1$ and $ba-1$ smoothing; hence an elliptic operator is invertible modulo smoothing, is Fredholm between Sobolev spaces, and obeys the elliptic regularity $au \in H^{s-m}_p\Rightarrow u \in H^s_p$, with the smooth case included.

On $L^2$ the operators of order $0$ are bounded, by Calderón–Vaillancourt, and operators of order $m$ map $H^s_2$ to $H^{s-m}_2$, the $L^p$ version holding for the symbols whose derivatives are bounded, as for the elliptic operators; Gårding's inequality turns the ellipticity and a positivity hypothesis on the symbol into a lower bound for the quadratic form, $\operatorname{Re}\langle au,u\rangle\ge c'\|u\|^2_{H^{m/2}}-C\|u\|^2_{L^2}$. The principal symbol is invariant under diffeomorphisms and transforms by the cotangent lift, so the calculus is defined on any smooth manifold, where the operators form a filtered algebra with elliptic parametrices and Fredholm operators of finite index. The wavefront set and the propagation of singularities, the semiclassical calculus and the index theorem are not covered here' subjects.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $x$, $\xi$ | space and frequency variables in $\mathbb{R}^n$ |
| $\alpha,\beta$ | multi-indices |
| $D^\alpha=(-i)^{|\alpha|}\partial^\alpha$ | derivative convention |
| $S^m$, $S^\infty$, $S^{-\infty}$ | symbol classes, smoothing class |
| $a\sim\sum_ja_j$ | asymptotic expansion |
| $a(x,D)=\mathrm{Op}(a)$ | operator with symbol $a$ (left quantisation) |
| $a^w(x,D)$ | Weyl quantisation |
| $K_a(x,y)$ | kernel of $a(x,D)$, image variable first |
| $c(x,\xi)$ | composition symbol |
| $\{a,b\}$ | Poisson bracket |
| $a^*$ | symbol of the formal adjoint |
| $\sigma_m(a)$, $a_m$ | principal symbol |
| $H^s_p$, $\langle D\rangle^s$ | Bessel-potential spaces and Bessel potentials |
| $T^*M$, $\sigma_m(T)$ | cotangent bundle and principal symbol on a manifold |
| $R_1,R_2$ | smoothing remainders |
| $M_{x_k}$ | operator of multiplication by $x_k$ |







## Further Reading

- Lars Hörmander, *The Analysis of Linear Partial Differential Operators III* (Springer, 1985), for the calculus of pseudodifferential operators, composition, parametrices and Gårding's inequality.
- Lars Hörmander, "Pseudo-differential operators", *Communications on Pure and Applied Mathematics* 18 (1965), 501–517, for the original systematic calculus and the symbol classes.
- Joseph J. Kohn and Louis Nirenberg, "An algebra of pseudo-differential operators", *Communications on Pure and Applied Mathematics* 18 (1965), 269–305, for the algebra of operators and the parametrix construction.
- Alberto P. Calderón and Rémi Vaillancourt, "A class of bounded pseudo-differential operators", *Proceedings of the National Academy of Sciences* 69 (1972), 1185–1187, for the $L^2$ boundedness of operators with symbols in $S^0$.
- Louis Boutet de Monvel, "Boundary problems for pseudo-differential operators", *Acta Mathematica* 126 (1971), 11–51, for the calculus with boundary and the algebra of boundary problems.
- François Trèves, *Introduction to Pseudodifferential and Fourier Integral Operators*, vol. 1 (Plenum, 1980), for a detailed treatment of the calculus and its applications.
- Michael E. Taylor, *Pseudodifferential Operators* (Princeton University Press, 1981), for the calculus on manifolds, the principal symbol and elliptic regularity.
- Lars Hörmander, "The Weyl calculus of pseudo-differential operators", *Communications on Pure and Applied Mathematics* 32 (1979), 359–443, for the Weyl quantisation and its invariance and positivity properties.
- Lars Gårding, "Dirichlet's problem for linear elliptic partial differential equations", *Mathematica Scandinavica* 1 (1953), 55–72, for the inequality bearing his name.
