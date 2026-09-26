
# __Distributions and Fundamental Solutions__

## Introduction

A function that is locally integrable acts on a test function by integration, and the pairing so obtained is linear and continuous; the insight of the theory of distributions is to keep the pairing and forget the function, so that the linear functionals retained are a strictly larger class of objects, closed under differentiation and under the passage to limits, and containing the objects — the delta, the principal value, the finite part — that the classical theory can describe only as limits. The gain is not convenience but closure: every distribution has derivatives of all orders, the derivative being defined by transposing the operation on test functions, and the linear differential operators of analysis act on all of them.

The theory is the analytic content of the dual of a space of smooth functions, and its two structural themes are differentiation and convolution. Differentiation is transposition and therefore always available; convolution is the operation that turns a fundamental solution into a solution, and its existence for a given operator is the question the second half of the article answers. A **fundamental solution** of a linear differential operator $P$ is a distribution $E$ with $PE=\delta$, and the equation $Pu=f$ is then solved by $u=E*f$ whenever the convolution is defined; for an operator with variable coefficients the best that can be expected in general is a **parametrix**, a distribution $E$ with $PE=I-R$ for a smoothing remainder $R$, and ellipticity is the condition that produces one.

Throughout, $\Omega \subseteq \mathbb{R}^n$ is open, $\alpha=(\alpha_1,\dots,\alpha_n) \in \mathbb{N}^n$ is a multi-index with $|\alpha|=\sum_i\alpha_i$ and $\partial^\alpha=\partial_1^{\alpha_1}\cdots\partial_n^{\alpha_n}$, and $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$. The notation for the Fréchet derivative and for linear differential operators is that fixed in the companion article *Differential Calculus on Normed Spaces*; the topological dual and the duality pairing are those of *Duality Theory* and *Locally Convex Spaces*, and the inductive-limit topology of the test-function space is that of *Locally Convex Spaces*. The Fourier transform on $\mathbb{R}^n$, with the constants used below, is the subject of *Fourier Analysis on Euclidean Spaces*, earlier in this Part; only the formulas and their properties are used here. The Bessel-potential spaces $H^s_p$ are those of *Interpolation Theory*, and the weak-derivative Sobolev spaces, together with the elliptic boundary-value theory that follows from the parametrix, belong to Part III. The systematic calculus of symbols and of pseudodifferential operators is deferred, and so is the wavefront-set refinement of the multiplication problem; the distributional setting for the analysis of an algebra-valued function is used in the category of the linear algebras of this Part, where the first-order operator of that theory is assembled.

No physics is invoked.

## Test Functions and Their Topology

### Multi-Indices and Partial Derivatives

**Definition.** A **multi-index** is a vector $\alpha=(\alpha_1,\dots,\alpha_n) \in \mathbb{N}^n$, with $|\alpha|=\alpha_1+\cdots+\alpha_n$, $\alpha!=\alpha_1!\cdots\alpha_n!$, and $x^\alpha=x_1^{\alpha_1}\cdots x_n^{\alpha_n}$ for $x \in \mathbb{R}^n$; the notation $\partial^\alpha=\partial_1^{\alpha_1}\cdots\partial_n^{\alpha_n}$ and $D^\alpha=(-i)^{|\alpha|}\partial^\alpha$ is used for the two conventions of the derivative of order $|\alpha|$. A **linear differential operator** of order at most $m$ on $\Omega$ is an expression

$$
P(x,D)=\sum_{|\alpha|\le m}a_\alpha(x)D^\alpha, \qquad a_\alpha \in C^\infty(\Omega),
$$

acting on $C^m(\Omega)$; its **principal part** is the sum over $|\alpha|=m$ and its **symbol** is the polynomial $P(x,\xi)=\sum_{|\alpha|\le m}a_\alpha(x)\xi^\alpha$, whose leading term $p_m(x,\xi)=\sum_{|\alpha|=m}a_\alpha(x)\xi^\alpha$ is the **principal symbol**. The operator is **elliptic** at $x$ if $p_m(x,\xi)\neq0$ for every $\xi \neq 0$, and **elliptic** if it is so at every $x$.

### The Spaces $\mathcal D$, $\mathcal E$ and $\mathcal S$

**Definition.** The **support** of a continuous function $f$ is $\operatorname{supp}f=\overline{\{x:f(x)\neq0\}}$. For a compact set $K \subseteq \Omega$ let $\mathcal D_K(\Omega)$ be the space of $f \in C^\infty(\Omega)$ with $\operatorname{supp}f \subseteq K$; it carries the seminorms

$$
\|f\|_{K,N}=\sum_{|\alpha|\le N}\sup_{x \in K}|\partial^\alpha f(x)|, \qquad N=0,1,2,\dots,
$$

and is a Fréchet space. The space of **test functions** is $\mathcal D(\Omega)=C_c^\infty(\Omega)=\bigcup_K \mathcal D_K(\Omega)$ with the inductive limit of those Fréchet spaces over the compact sets $K \subseteq \Omega$, the **LF topology** of *Locally Convex Spaces*; a linear functional $u$ on $\mathcal D(\Omega)$ is continuous exactly when for every compact $K$ there are $C$ and $N$ with

$$
|\langle u,\varphi\rangle| \le C\|\varphi\|_{K,N} \qquad \text{for all } \varphi \in \mathcal D_K(\Omega).
$$

The space $\mathcal E(\Omega)=C^\infty(\Omega)$ with the seminorms over compact $K$ and all $\alpha$ is a Fréchet space, and the **Schwartz space** $\mathcal S(\mathbb{R}^n)$ is the set of $f \in C^\infty(\mathbb{R}^n)$ with

$$
\|f\|_{\alpha,\beta}=\sup_{x}|x^\beta\partial^\alpha f(x)|<\infty \quad \text{for all multi-indices } \alpha,\beta,
$$

a Fréchet space in these seminorms. The inclusions $\mathcal D(\Omega) \subseteq \mathcal S(\mathbb{R}^n) \subseteq \mathcal E(\mathbb{R}^n)$ are continuous, for $\Omega=\mathbb{R}^n$.

**Proposition (mollifiers).** There is $\rho \in \mathcal D(\mathbb{R}^n)$ with $\rho \ge 0$, $\operatorname{supp}\rho \subseteq \{|x|\le1\}$ and $\int\rho=1$. For $\varepsilon>0$ put $\rho_\varepsilon(x)=\varepsilon^{-n}\rho(x/\varepsilon)$. Then for $f \in L^p(\mathbb{R}^n)$, $1\le p<\infty$, the convolutions $f*\rho_\varepsilon$ are smooth, $\|f*\rho_\varepsilon\|_p\le\|f\|_p$, and $f*\rho_\varepsilon \to f$ in $L^p$; for $f$ uniformly continuous and bounded the convergence is uniform; and for $f \in L^1_{\mathrm{loc}}$ the convergence is in $L^1_{\mathrm{loc}}$.

*Proof.* The function $\rho(x)=c\exp(-1/(1-|x|^2))$ for $|x|<1$ and $0$ otherwise, with $c$ chosen so that $\int\rho=1$, is the standard bump and lies in $\mathcal D$. Minkowski's integral inequality gives the norm bound and the continuity of translation in $L^p$ gives the convergence; the uniform case is uniform continuity, and the local case follows by testing on compact sets. $\square$

**Corollary (density).** $C_c^\infty(\Omega)$ is dense in $L^p(\Omega)$ for $1\le p<\infty$, dense in $C_0(\Omega)$ in the supremum norm, and $\mathcal D(\mathbb{R}^n)$ is dense in $\mathcal S(\mathbb{R}^n)$.

## Distributions

### Definition and Basic Examples

**Definition.** A **distribution** on $\Omega$ is a continuous linear functional $u:\mathcal D(\Omega) \to \mathbb{K}$; the space of distributions is the dual $\mathcal D'(\Omega)$, and the value of $u$ on $\varphi$ is written $\langle u,\varphi\rangle$. A distribution is of **order** at most $N$ if the integer $N$ of the continuity criterion can be chosen uniformly over compact sets, and of **finite order** if it is of order at most $N$ for some $N$.

**Proposition (locally integrable functions).** Every $f \in L^1_{\mathrm{loc}}(\Omega)$ defines a distribution of order $0$ by

$$
\langle f,\varphi\rangle=\int_\Omega f\varphi\,dx,
$$

and the map $L^1_{\mathrm{loc}}(\Omega) \to \mathcal D'(\Omega)$ is injective.

*Proof.* Continuity is the estimate $|\int_Kf\varphi|\le\|f\|_{L^1(K)}\|\varphi\|_{K,0}$. For injectivity, if $\int f\varphi=0$ for all $\varphi \in \mathcal D(\Omega)$, then given $x$ and a compactly supported test function $\psi$ equal to $1$ near $x$, the regularisations are $f*\rho_\varepsilon(x)=\int f(y)\psi(y)\rho_\varepsilon(x-y)\,dy=0$ for small $\varepsilon$ and for $x$ in a compact subset of the interior of $\{\psi=1\}$; since $f*\rho_\varepsilon\to f$ in $L^1_{\mathrm{loc}}$, the function $f$ vanishes a.e. $\square$

**Example.** (i) The **delta distribution** at $a \in \Omega$ is $\langle\delta_a,\varphi\rangle=\varphi(a)$; it is of order $0$ and is not given by any locally integrable function, since it would have to vanish away from $a$ while integrating to $1$.

(ii) The **Heaviside function** $H=\mathbf{1}_{(0,\infty)}$ on $\mathbb{R}$ is the distribution $\langle H,\varphi\rangle=\int_0^\infty\varphi$.

(iii) The **principal value** of $1/x$ on $\mathbb{R}$ is

$$
\Bigl\langle \mathrm{pv}\frac1x,\varphi\Bigr\rangle=\lim_{\varepsilon \to 0}\int_{|x|>\varepsilon}\frac{\varphi(x)}{x}\,dx,
$$

a distribution of order $1$; the limit exists because the odd kernel annihilates the constant, $\int_{\varepsilon<|x|<1}\varphi(x)/x\,dx=\int_{\varepsilon<|x|<1}(\varphi(x)-\varphi(0))/x\,dx$, and the integrand is bounded on $|x|<1$, so the integrals converge as $\varepsilon\downarrow0$ by dominated convergence.

(iv) The **finite part** $\mathrm{pf}(1/x^2)$ and the regularisations of $1/|x|$ on $\mathbb{R}^n$ for $n\ge2$ are defined by subtracting the divergent terms, and are the standard devices for the non-integrable singularities of a fundamental solution.

### Support, Order and the Structure Theorem

**Definition.** The **support** of $u \in \mathcal D'(\Omega)$ is the complement in $\Omega$ of the union of the open sets $U$ such that $\langle u,\varphi\rangle=0$ for every $\varphi \in \mathcal D(U)$. The distributions of compact support form the dual $\mathcal E'(\Omega)$ of $\mathcal E(\Omega)$, under the identification $\langle u,\varphi\rangle$ for $\varphi \in C^\infty(\Omega)$; every $u \in \mathcal E'(\Omega)$ is a distribution of finite order, and the smallest compact set containing the support controls the estimates.

**Theorem (structure of compactly supported distributions).** Every $u \in \mathcal E'(\Omega)$ of order at most $N$ is a finite sum

$$
u=\sum_{|\alpha|\le N}(-1)^{|\alpha|}\partial^\alpha\mu_\alpha
$$

of derivatives of complex measures $\mu_\alpha$ of compact support; if $u$ is real and $N=0$ then the representing measure is unique and $u$ is a signed measure, and a distribution of order $0$ that is positive, meaning $\langle u,\varphi\rangle\ge0$ for $\varphi\ge0$, is a positive measure on $\Omega$.

The theorem is proved by the Hahn–Banach extension theorem of *Normed and Banach Spaces* applied to the restriction of $u$ to $\mathcal D_K$ for a compact $K$ containing the support, and by the Riesz representation theorem for $C(K)$, the derivatives being transposed back from the measured functional. It is the exact measure-theoretic description of a distribution of compact support and is the starting point of the theory of positive distributions and of Radon measures.

**Corollary.** A distribution of order $0$ is integration against a complex measure, and a positive distribution is a positive Radon measure. A distribution $u$ with $\operatorname{supp}u=\{a\}$ is a finite linear combination of $\delta_a$ and its derivatives, $\sum_{|\alpha|\le N}c_\alpha\partial^\alpha\delta_a$.

## Differentiation and Multiplication

### Differentiation of Distributions

**Definition.** The derivative of $u \in \mathcal D'(\Omega)$ with respect to the multi-index $\alpha$ is the distribution

$$
\langle \partial^\alpha u,\varphi\rangle=(-1)^{|\alpha|}\langle u,\partial^\alpha\varphi\rangle, \qquad \varphi \in \mathcal D(\Omega).
$$

The sign is the one that makes the definition the transposition of the classical formula $\int(\partial^\alpha f)\varphi=(-1)^{|\alpha|}\int f\partial^\alpha\varphi$ for $f \in C^{|\alpha|}$, so that the distributional derivative extends the classical one.

**Theorem.** Every distribution has derivatives of all orders; $\partial^\alpha:\mathcal D'(\Omega)\to\mathcal D'(\Omega)$ is linear and continuous in the weak-$*$ topology; the derivatives commute, $\partial^\alpha\partial^\beta=\partial^{\alpha+\beta}$; and the Leibniz rule

$$
\partial^\alpha(\varphi u)=\sum_{\beta\le\alpha}\binom{\alpha}{\beta}(\partial^{\alpha-\beta}\varphi)(\partial^\beta u)
$$

holds for $\varphi \in C^\infty(\Omega)$ and $u \in \mathcal D'(\Omega)$. A distribution with all derivatives zero on a connected $\Omega$ is given by a constant function.

*Proof.* The functional $\varphi \mapsto(-1)^{|\alpha|}\langle u,\partial^\alpha\varphi\rangle$ is a composite of $u$ with a continuous map of $\mathcal D(\Omega)$ into itself, hence continuous; the commutativity is the commutativity of partial derivatives on test functions, and the Leibniz rule is the identity $\partial^\alpha(\varphi\psi)=\sum_{\beta\le\alpha}\binom\alpha\beta\partial^{\alpha-\beta}\varphi\,\partial^\beta\psi$ transposed. The last statement reduces to $\partial_ju=0$ for all $j$, which forces $u$ to be constant by applying the classical mean value theorem to the test functions against which $u$ is paired. $\square$

**Example.** (i) $H'=\delta$ on $\mathbb{R}$: $\langle H',\varphi\rangle=-\int_0^\infty\varphi'=-\varphi(0)+\varphi(\infty)=-\varphi(0)$, using $\varphi$ compactly supported. More generally the derivative of the indicator of an interval with endpoints $a<b$ is $\delta_a-\delta_b$.

(ii) $\frac{d}{dx}\mathrm{pv}\frac1x=-\mathrm{pf}\frac{1}{x^2}$ on $\mathbb{R}$, and $\frac{d}{dx}\log|x|=\mathrm{pv}\frac1x$: transposing the integration by parts gives $\langle(\log|x|)',\varphi\rangle=-\int\log|x|\,\varphi'(x)\,dx=\lim_\varepsilon\int_{|x|>\varepsilon}\varphi(x)/x\,dx$, the divergent boundary terms cancelling.

(iii) $x\delta'=-\delta$ and $x\delta=0$: $\langle x\delta,\varphi\rangle=\langle\delta,x\varphi\rangle=0$, and $\langle x\delta',\varphi\rangle=\langle\delta',x\varphi\rangle=-\varphi(0)$. The first identity exhibits the division problem, and the second shows that a product of distributions is not detected by its vanishing on test functions supported away from the origin.

(iv) For $\alpha \in \mathbb{N}^n$, $\partial^\alpha\delta_a$ is the distribution $\varphi \mapsto(-1)^{|\alpha|}\partial^\alpha\varphi(a)$, and every distribution supported at $a$ is a finite combination of these, by the corollary above.

### Multiplication and Its Limits

**Definition.** For $\varphi \in C^\infty(\Omega)$ and $u \in \mathcal D'(\Omega)$ the product is $\langle\varphi u,\psi\rangle=\langle u,\varphi\psi\rangle$. It is a distribution, the map $(\varphi,u)\mapsto\varphi u$ is bilinear and separately continuous, and the Leibniz rule above holds.

The product of two distributions is in general undefined: the formula $\int fg\,\varphi$ has no meaning for distributions, and the natural attempts fail. The standard pair of examples fixes the point.

**Example.** Let $u=\mathrm{pv}(1/x)$ and $v=\delta$ on $\mathbb{R}$, so that $xu=1$ and $xv=0$. If a product $uv$ existed and the multiplication by a smooth function were associative with it, then applying the identity $\varphi(uv)=(\varphi u)v$ to $\varphi(x)=x$ would give the contradiction $0=(xv)u=x(uv)=(xu)v=1\cdot v=\delta$. There is thus no distribution that deserves the name $\delta\cdot\mathrm{pv}(1/x)$, and the same obstruction appears for $\delta H$, $\delta\delta$ and every pair whose singular directions are opposed.

**Theorem (multiplication in Hörmander's sense).** Two distributions have a product when their wavefront sets satisfy the transversality condition $\mathrm{WF}(u)\cap\mathrm{WF}(v)^{-}=\varnothing$, where $\mathrm{WF}(v)^-$ reverses the sign of the frequency variable; then $uv$ is defined, and the product of a distribution with a smooth function is the case in which one wavefront set is empty. The wavefront set, this criterion and the microlocal description of the regularity of $uv$ are the subject of of this category, and are not developed here.

The upshot is that the set of distributions is not an algebra, and that the failure is localised in the frequency directions: two distributions may be multiplied wherever their singular directions do not oppose one another. This is the precise sense in which the theory is closed under differentiation but not under multiplication, and it is why the pseudodifferential calculus keeps a symbol as an auxiliary object rather than only the operator.

## Tempered Distributions and the Fourier Transform

### The Schwartz Space and Its Dual

**Definition.** The **Fourier transform** of $f \in \mathcal S(\mathbb{R}^n)$ is

$$
\hat f(\xi)=\mathcal Ff(\xi)=\int_{\mathbb{R}^n}f(x)e^{-ix\cdot\xi}\,dx,
\qquad
\mathcal F^{-1}g(x)=\frac{1}{(2\pi)^n}\int_{\mathbb{R}^n}g(\xi)e^{ix\cdot\xi}\,d\xi .
$$

**Theorem.** $\mathcal F$ maps $\mathcal S(\mathbb{R}^n)$ isomorphically onto itself, with $\mathcal F^{-1}$ the inverse, $\|\hat f\|_2=(2\pi)^{n/2}\|f\|_2$, and the identities

$$
\widehat{\partial_jf}(\xi)=i\xi_j\hat f(\xi), \qquad \widehat{x_jf}(\xi)=i\partial_j\hat f(\xi), \qquad \widehat{(f*g)}=\hat f\hat g .
$$

*Proof.* These are the standard properties: differentiation under the integral sign for the first, integration by parts for the second and the convolution theorem by Fubini; inversion follows from the Fourier inversion theorem, and the $L^2$ identity is Plancherel's theorem. Their proofs, with the normalisation used here, belong to *Fourier Analysis on Euclidean Spaces*. $\square$

**Definition.** A **tempered distribution** is a continuous linear functional on $\mathcal S(\mathbb{R}^n)$; the space is $\mathcal S'(\mathbb{R}^n)$. Every tempered distribution is a distribution, since $\mathcal D \subseteq \mathcal S$ continuously, and every compactly supported distribution is tempered, since $\mathcal S \subseteq \mathcal E$; the inclusions

$$
\mathcal E'(\mathbb{R}^n) \subseteq \mathcal S'(\mathbb{R}^n) \subseteq \mathcal D'(\mathbb{R}^n)
$$

are strict.

**Definition.** The **Fourier transform** of $u \in \mathcal S'(\mathbb{R}^n)$ is defined by transposition,

$$
\langle\hat u,\varphi\rangle=\langle u,\hat\varphi\rangle, \qquad \varphi \in \mathcal S(\mathbb{R}^n),
$$

and is again tempered. The transform is a linear isomorphism of $\mathcal S'$ with itself, and it intertwines differentiation with multiplication:

$$
\widehat{\partial^\alpha u}=i^{|\alpha|}\xi^\alpha\hat u, \qquad \widehat{x^\alpha u}=i^{|\alpha|}\partial^\alpha\hat u, \qquad \widehat{u*v}=\hat u\,\hat v
$$

for $u \in \mathcal S'$ and $v \in \mathcal E'$, the convolution being defined in the next section.

**Example.** $\hat\delta=1$ and $\hat1=(2\pi)^n\delta$, since $\langle\hat\delta,\varphi\rangle=\langle\delta,\hat\varphi\rangle=\hat\varphi(0)=\int\varphi$; the transform of a Gaussian $e^{-|x|^2/2}$ is $(2\pi)^{n/2}e^{-|\xi|^2/2}$; and the transform of a function of compact support is smooth (indeed entire) with at most polynomial growth of all derivatives, which is why the two dual spaces differ.

## Convolution

### Convolution with a Test Function

**Definition.** For $u \in \mathcal D'(\mathbb{R}^n)$ and $\varphi \in \mathcal D(\mathbb{R}^n)$ the **convolution** is the function

$$
(u*\varphi)(x)=\langle u,\varphi(x-\cdot)\rangle=\langle u,\tau_x\check\varphi\rangle,
$$

where $\check\varphi(y)=\varphi(-y)$.

**Theorem.** For $u \in \mathcal D'$ and $\varphi \in \mathcal D$ the function $u*\varphi$ lies in $C^\infty(\mathbb{R}^n)$, and

$$
\partial^\alpha(u*\varphi)=(\partial^\alpha u)*\varphi=u*\partial^\alpha\varphi, \qquad \operatorname{supp}(u*\varphi) \subseteq \overline{\operatorname{supp}u+\operatorname{supp}\varphi}.
$$

If $u=\delta_a$ then $u*\varphi=\tau_a\varphi$, where $\tau_a\varphi(x)=\varphi(x-a)$; if $u=f \in L^1_{\mathrm{loc}}$ then $u*\varphi$ is the classical convolution $\int f(y)\varphi(x-y)\,dy$.

*Proof.* The map $x \mapsto \tau_{-x}\check\varphi$ is $C^\infty$ from $\mathbb{R}^n$ into $\mathcal D$, with derivative computed by the chain rule of *Differential Calculus on Normed Spaces*; differentiating under the continuous linear functional $u$ gives smoothness and the first identity, and the second is the transposed Leibniz formula. The support statement is the statement that $\varphi(x-\cdot)$ vanishes on $\operatorname{supp}u$ unless $x$ is a sum of a point of $\operatorname{supp}u$ and a point of $\operatorname{supp}\varphi$. $\square$

**Corollary (regularisation).** Choosing $\rho_\varepsilon$ as above, $u*\rho_\varepsilon \in C^\infty$ and $u*\rho_\varepsilon \to u$ in $\mathcal D'$; hence $C^\infty(\Omega)$ is dense in $\mathcal D'(\Omega)$ in the weak-$*$ topology.

### Convolution of Distributions

**Definition.** Let $u,v \in \mathcal D'(\mathbb{R}^n)$ and suppose one of them has compact support. Then $u*v$ is the distribution

$$
\langle u*v,\varphi\rangle=\bigl\langle u_x,\langle v_y,\varphi(x+y)\rangle\bigr\rangle, \qquad \varphi \in \mathcal D(\mathbb{R}^n),
$$

the pairing being rigorous because the compact support makes $\langle v_y,\varphi(x+y)\rangle$ a test function of $x$. When neither factor has compact support the convolution may still be defined if the supports are suitably bounded, but it is not defined in general.

**Theorem.** The convolution is bilinear, commutative and associative whenever the supports permit, continuous in the weak-$*$ topology, and satisfies

$$
\delta*u=u, \qquad \delta_a*u=\tau_au, \qquad (\partial^\alpha\delta)*u=\partial^\alpha u, \qquad (\partial^\alpha u)*v=\partial^\alpha(u*v),
$$

and $\operatorname{supp}(u*v) \subseteq \overline{\operatorname{supp}u+\operatorname{supp}v}$. The space $\mathcal E'(\mathbb{R}^n)$ of compactly supported distributions is a commutative algebra under convolution, with identity $\delta$; the space $L^1(\mathbb{R}^n)$ is a subalgebra, and the Fourier transform converts convolution into multiplication, $\widehat{u*v}=\hat u\hat v$ for $u \in \mathcal S'$ and $v \in \mathcal E'$.

*Proof.* Bilinearity and continuity follow from the definition and the continuity of the pairings; the associativity, when the supports permit, is Fubini for the iterated pairing. The remaining identities are verified directly on test functions, and the Fourier statement is the convolution theorem transposed. $\square$

**Example.** On $\mathbb{R}$, $H*H=xH$: $\langle H*H,\varphi\rangle=\int_0^\infty\int_0^\infty\varphi(x+y)\,dy\,dx=\int_0^\infty t\varphi(t)\,dt$. Similarly $\delta'*H=H'=\delta$, which is the identity $(\partial\delta)*u=\partial u$ in the simplest case.

## Fundamental Solutions and Parametrices

### The Definition and the Basic Mechanism

**Definition.** Let $P=P(x,D)$ be a linear differential operator on $\Omega$. A **fundamental solution** of $P$ at a point $x_0$ is a distribution $E$ on a neighbourhood of $x_0$ with

$$
PE=\delta_{x_0}.
$$

A **parametrix** of $P$ near $x_0$ is a distribution $E$ with $PE=\delta_{x_0}-R$, where $R$ is a smoothing operator: $R\varphi \in C^\infty$ for every distribution $\varphi$ for which the pairing is defined.

**Theorem (construction from a fundamental solution).** Let $P$ have constant coefficients and let $E$ be a fundamental solution of $P$ at $0$. Then for every $f \in \mathcal E'(\mathbb{R}^n)$ the distribution $u=E*f \in \mathcal D'(\mathbb{R}^n)$ satisfies $Pu=f$, and it is the unique solution in $\mathcal S'(\mathbb{R}^n)$ when $P$ has no nonzero tempered solution of $Pu=0$. If $f \in C_c^\infty$, then $u \in C^\infty$ away from the singular support of $E$.

*Proof.* By the identities of the convolution section, $P(E*f)=(PE)*f=\delta*f=f$; uniqueness follows because the difference of two solutions is a solution of the homogeneous equation and the transform converts it into a distribution supported at the origin, which is a combination of derivatives of $\delta$ and is excluded by the hypothesis. The smoothness statement is the regularity of the convolution of $E$ with a smooth compactly supported function away from the singularities of $E$. $\square$

### Existence for Constant Coefficients

**Theorem (Ehrenpreis–Malgrange).** Every nonzero linear differential operator with constant coefficients on $\mathbb{R}^n$ has a fundamental solution.

*Proof (sketch).* One has to define $\mathcal F^{-1}(1/P(\xi))$ as a tempered distribution even though $1/P(\xi)$ may fail to be locally integrable near the real zeros of the polynomial $P(\xi)$. One writes $1/P(\xi)$ as a limit of locally integrable functions obtained by translating the polynomial, $1/P(\xi+i\eta)$ for $\eta$ in a suitable dense set, and uses an a priori estimate for the translated operator to extract a convergent subsequence in $\mathcal S'$; the limit $E$ satisfies $P(\xi)\hat E=1$ in $\mathcal S'$, which is $PE=\delta$. The argument is standard and is proved in full in the works cited below. $\square$

### The Laplacian and the Heat Operator

**Example (Laplacian).** Let $\omega_n$ be the surface area of the unit sphere $S^{n-1}$, so that $\omega_2=2\pi$ and $\omega_3=4\pi$. The **Newtonian potential** is

$$
E(x)=\begin{cases}\dfrac{1}{(n-2)\omega_n}|x|^{2-n}, & n\ge3,\\[4pt] -\dfrac{1}{2\pi}\log|x|, & n=2,\end{cases}
$$

and it satisfies $-\Delta E=\delta$. For $n\ge3$ one has $\Delta|x|^{2-n}=0$ away from the origin, and the distributional identity is determined by the flux across a small sphere: the radial derivative is $(2-n)r^{1-n}$ and its integral over the sphere of radius $r$ is $(2-n)\omega_n$, independent of $r$, so $-\Delta E=\delta$. For $n=2$ the radial derivative of $-\frac{1}{2\pi}\log r$ is $-\frac{1}{2\pi r}$ and its flux over a circle of radius $r$ is $-1$, giving $-\Delta E=\delta$. Hence the Poisson equation $-\Delta u=f$ is solved by $u=E*f$ whenever the convolution is defined.

**Example (heat operator).** On $\mathbb{R}^n \times \mathbb{R}$ the **heat kernel**

$$
E(x,t)=\begin{cases}(4\pi t)^{-n/2}e^{-|x|^2/(4t)}, & t>0,\\ 0, & t\le0,\end{cases}
$$

satisfies $(\partial_t-\Delta)E=\delta$; it is smooth away from the orig, its integral over $x$ equals $1$ for every $t>0$ (verified by the Gaussian integral, whose value is $\pi^{n/2}$ in $n$ dimensions after the change of variable), and it tends to $\delta$ as $t \downarrow 0$, so that $E$ is the fundamental solution of the heat operator. The solution of the Cauchy problem $u_t-\Delta u=0$, $u(\cdot,0)=u_0$, is $u=E(t)*u_0$ where the convolution is in the space variables, and the equation is the model of the parabolic theory.

**Example (wave operator).** On $\mathbb{R}^{1+d}$ with coordinates $(t,x)$, the operator $\Box=\partial_t^2-\Delta_x$ has a fundamental solution supported in the cone $\{(t,x):|x|\le t\}$, the characteristic cone of the quadratic form $\mathrm{diag}(1,-1,\dots,-1)$, given in each dimension by an explicit formula: $\frac12H(t-|x|)$ for $d=1$, $\frac{1}{2\pi}(t^2-|x|^2)^{-1/2}H(t-|x|)$ for $d=2$, and $\frac{1}{4\pi t}\delta(t-|x|)$ for $d=3$. The support property is finite propagation speed, and the formulas are those of the wave-equation article of the differential-equations extension; they are quoted here as the standard fundamental solutions.

### Elliptic Operators and the Parametrix

**Definition.** Let $P$ be elliptic of order $m$ on $\Omega$, with principal symbol $p_m$. A **parametrix** of $P$ on $\Omega$ is a distribution $E$ with $PE=\delta-R$ where $R$ has $C^\infty$ kernel, and $E$ is **properly supported** if the projections of $\operatorname{supp}E$ to the two factors of $\Omega \times \Omega$ are proper.

**Theorem (parametrix and elliptic regularity).** Let $P$ be elliptic of order $m$ with coefficients in $C^\infty(\Omega)$. Then $P$ has a properly supported parametrix $E$ on every compactly contained open subset. Consequently, for $u \in \mathcal D'(\Omega)$ and $s \in \mathbb{R}$,

$$
Pu \in H^s_{\mathrm{loc}}(\Omega) \implies u \in H^{s+m}_{\mathrm{loc}}(\Omega),
$$

and in particular $Pu \in C^\infty(\Omega)$ implies $u \in C^\infty(\Omega)$: an elliptic operator does not create singularities, and it removes them.

*Proof (sketch).* The construction freezes the coefficients at a point $x_0$ and inverts the principal symbol by the Fourier formula: a local parametrix is $E_0(x)=\mathcal F^{-1}(\chi(\xi)/p_m(x_0,\xi))$ with $\chi$ a cutoff vanishing near $\xi=0$, and the operator $I-PE_0$ has order $-1$; iterating the construction and summing a Neumann series over the local pieces gives a parametrix with a smoothing remainder. The regularity statement follows from $u=E(Pu)+Ru$, the mapping property of $E$ of order $-m$ on the Bessel-potential spaces of *Interpolation Theory*, and the smoothing of $R$. The complete pro, with the calculus of symbols, is not covered here. $\square$

The theorem explains the role of ellipticity: it is the condition under which the principal symbol can be inverted for large frequencies, and it is the analytic content of the parametrix. The calculus that makes the construction systematic — composition of symbols, the asymptotic expansion of a product, the parametrix of a general operator and the index theory that follows — is developed; the classical classification of a second-order equation into elliptic, parabolic and hyperbolic types and the explicit solution formulas are given, and the boundary-value theory lies outside this article.

## Weak Derivatives and the Passage to Other Settings

**Definition.** Let $f \in L^1_{\mathrm{loc}}(\Omega)$ and let $\alpha$ be a multi-index. A function $g \in L^1_{\mathrm{loc}}(\Omega)$ is the **weak derivative** $\partial^\alpha f$ if the distribution $\partial^\alpha f$ defined by transposition equals the distribution $g$; that is, if

$$
\int_\Omega f\,\partial^\alpha\varphi=(-1)^{|\alpha|}\int_\Omega g\varphi \qquad \text{for every } \varphi \in \mathcal D(\Omega).
$$

**Theorem.** The weak derivative, when it exists, is unique; it agrees with the classical derivative wherever the latter is continuous; and the Sobolev space $W^{k,p}(\Omega)$ of functions whose weak derivatives of order at most $k$ lie in $L^p$ is a Banach space under $\|f\|_{W^{k,p}}=(\sum_{|\alpha|\le k}\|\partial^\alpha f\|_p^p)^{1/p}$. The identification of $W^{k,p}$ with the Bessel-potential space $H^k_p$ for $1<p<\infty$ and the embedding theorems are the content.

This is the first of the two passages that the theory of distributions makes possible. The second is the one used by the analysis of an algebra-valued function: when the ground algebra is no longer a field, the first-order operator $D=\sum_ie_i\partial_i$ assembled from a frame of the algebra is a linear differential operator to which the definitions of this article apply verbatim, so the notions of weak solution, of fundamental solution and of regularity by parametrix are available there as here. The class of functions annihilated by $D$, its Cauchy integral formula and the failure of the classical theorems are treated, in the category of the linear algebras of this Part, and the operator itself is not covered here.

## Summary

A distribution is a continuous linear functional on the test functions $C_c^\infty(\Omega)$ with the LF topology, equivalently a functional that on each $\mathcal D_K$ is bounded by finitely many seminorms $\|f\|_{K,N}$. Every locally integrable function is a distribution and the map is injective; the delta, the Heaviside function, the principal value and the finite part are the standard distributions that are not functions. A distribution of compact support has finite order and is a finite sum of derivatives of measures, by the structure theorem; a distribution of order $0$ is integration against a measure, and a positive one is a positive Radon measure; a distribution supported at a point is a combination of $\delta$ and its derivatives.

Differentiation is defined by transposition, $\langle\partial^\alpha u,\varphi\rangle=(-1)^{|\alpha|}\langle u,\partial^\alpha\varphi\rangle$, so every distribution is infinitely differentiable, the derivatives commute and the Leibniz rule holds against smooth coefficients; the classical rules are recovered, with $H'=\delta$, $(\log|x|)'=\mathrm{pv}(1/x)$ and $x\delta'=-\delta$. Multiplication by a smooth function is defined and is only that: the product of two distributions is in general undefined, and the obstruction is localised in the frequency directions, the product being definable exactly when the wavefront sets are transverse.

The Fourier transform is an isomorphism of the Schwartz space and, by transposition, of the tempered distributions, intertwining $\partial^\alpha$ with multiplication by $i^{|\alpha|}\xi^\alpha$ and convolution with multiplication of symbols. Convolution of a distribution with a test function produces a smooth function and regularises; convolution of two distributions is defined when one has compact support, and $\mathcal E'$ is a commutative algebra under it with identity $\delta$, with $\mathcal S'$ acting on $\mathcal E'$ by convolution and the transform converting it into products. A fundamental solution is a distribution $E$ with $PE=\delta$, and it solves $Pu=f$ by $u=E*f$; every nonzero constant-coefficient operator has one, by Ehrenpreis–Malgrange, with the Laplacian, the heat operator and the wave operator as the worked cases. For variable coefficients the general construction yields a parametrix with a smoothing remainder, and ellipticity — the nonvanishing of the principal symbol off the zero section — produces one and gives the elliptic regularity $Pu \in H^s_{\mathrm{loc}}\Rightarrow u \in H^{s+m}_{\mathrm{loc}}$. Finally the distributional derivative is the weak derivative of a locally integrable function, so the distributional setting contains the Sobolev theory and extends verbatim to the first-order operators of the algebra-valued analysis of this Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Omega$ | open subset of $\mathbb{R}^n$ |
| $\alpha$, $|\alpha|$ | multi-index and its order |
| $\partial^\alpha$, $D^\alpha=(-i)^{|\alpha|}\partial^\alpha$ | derivative of order $|\alpha|$ |
| $\mathcal D(\Omega)=C_c^\infty(\Omega)$ | test functions with the LF topology |
| $\mathcal D_K(\Omega)$ | test functions supported in a compact set $K$ |
| $\mathcal E(\Omega)=C^\infty(\Omega)$ | smooth functions, Fréchet |
| $\mathcal S(\mathbb{R}^n)$ | Schwartz space, Fréchet |
| $\mathcal D'$, $\mathcal E'$, $\mathcal S'$ | distributions, compactly supported and tempered distributions |
| $\langle u,\varphi\rangle$ | duality pairing |
| $\delta$, $\delta_a$ | delta distribution at $0$ and at $a$ |
| $H$, $\mathrm{pv}\frac1x$, $\mathrm{pf}\frac1{x^2}$ | Heaviside function, principal value, finite part |
| $\operatorname{supp}u$ | support of a distribution |
| $\check\varphi$, $\tau_a\varphi$ | reflection and translation of a test function |
| $u*\varphi$, $u*v$ | convolution |
| $\hat u=\mathcal Fu$ | Fourier transform of a distribution |
| $P(x,D)$, $p_m(x,\xi)$ | differential operator and principal symbol |
| $E$, $R$ | fundamental solution or parametrix, and smoothing remainder |
| $W^{k,p}$, $H^s_p$ | Sobolev and Bessel-potential spaces |
| $\rho_\varepsilon$ | mollifier |





## Further Reading

- Laurent Schwartz, *Théorie des distributions* (Hermann, 1950–51; revised 1966), for the original development and the LF topology of the test functions.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* (Springer, 2nd ed. 1990), for distributions, the structure theorem, convolution and the wavefront-set criterion for products.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II* (Springer, 1983), for the parametrix, elliptic regularity and the calculus of operators.
- Israel M. Gelfand and Georgi E. Shilov, *Generalized Functions*, vols. 1–2 (Academic Press, 1964–68), for the elementary theory, the structure theorem and the regularisations.
- Leon Ehrenpreis, "Solution of some problems of division I", *American Journal of Mathematics* 76 (1954), 883–903, for the existence of fundamental solutions for constant-coefficient operators.
- Bernard Malgrange, "Existence et approximation des solutions des équations aux dérivées partielles et des équations de convolution", *Annales de l'Institut Fourier* 6 (1956), 271–355, for the same theorem and the convolution equations.
- Fritz John, *Partial Differential Equations*, 4th ed. (Springer, 1991), for the fundamental solutions of the classical operators and the wave-equation formulas.
- Walter Rudin, *Functional Analysis* (McGraw-Hill, 2nd ed. 1991), for distributions as the dual of the test-function space and the measure-theoretic structure theorem.
- Kôsaku Yosida, *Functional Analysis* (Springer, 6th ed. 1980), for the distributional derivative and the weak-derivative correspondence.
