
# __The Calculus of Variations__

## Introduction

The calculus of variations studies the extrema of functionals — maps from a space of functions to the real numbers — rather than the extrema of functions of finitely many variables. Its central object is the integral functional

$$
J(u) = \int_a^b L\bigl(x, u(x), u'(x)\bigr)\,dx,
$$

and its central result is that a minimiser of $J$, if it is smooth enough to be differentiated, satisfies the **Euler–Lagrange equation** $\frac{d}{dx}L_{u'} = L_u$, a differential equation of the second order. The subject is therefore a bridge: it converts a problem of minimising an integral into a problem of solving a differential equation, and conversely it explains the differential equations of mechanics and geometry as the stationarity conditions of an energy. Its three classical problems — the brachistochrone, the geodesic and the isoperimetric problem — are the historical source of the theory, and its modern form is the **direct method**, in which the existence of a minimiser is proved without solving the Euler–Lagrange equation, by a compactness argument in a Sobolev space.

The equation was found in the 1750s, in the study of the tautochrone problem — the curve along which a weighted particle falls to a fixed point in a fixed time, independently of the starting point. Lagrange solved the problem in 1755 and sent the solution to Euler, the two developed the method and applied it to mechanics, and Euler coined the name *calculus of variations* in 1766.

The article develops the theory in the following order. After fixing the notion of the first variation, it derives the Euler–Lagrange equation together with the natural boundary conditions, records the two classical reductions of the equation to a first integral, and works the geodesic and brachistochrone examples. It then collects the forms the equation takes beyond the scalar case of a single variable: the functional derivative, of which the bracket of the derivation is the density; the higher-derivative equation of Euler and Poisson; the system of equations for several unknown functions; the partial-differential equation for several variables, which turns the functional into a field theory; and the multi-index equation for several functions of several variables with higher derivatives. It then states the second variation and the Legendre condition, which distinguish a minimum from a general stationary point, and proves the direct method of the calculus of variations: a coercive, sequentially weakly lower semicontinuous functional on a reflexive Sobolev space attains its minimum, and convexity of the integrand in the gradient supplies the lower semicontinuity. The Euler–Lagrange equation of a minimiser is then a weak solution of an elliptic equation, and the regularity theory of the preceding article applies to it. Variational problems with constraints are treated by the Lagrange multiplier rule, with the isoperimetric problem as the example, and the article closes with the Hamiltonian reformulation, the connection with conservation laws, and the second variation in its geometric form, where the minimising property of a geodesic is decided by the index of a Jacobi field.

The setting is that of the Sobolev spaces $W^{1,p}$ and of the weak solutions of the preceding article, whose embedding, compactness and regularity theorems are used throughout. The classical differential equations of the first articles of this Part appear as the Euler–Lagrange equations of the models. The connection between a holonomic constraint and a differential-algebraic equation is the one established in the article of this category on differential-algebraic equations, and the Hamiltonian reformulation developed in full belongs to the article of this Part on Lagrangian and Hamiltonian systems.

## The First Variation and the Euler–Lagrange Equation

### Functionals and Variations

**Definition.** Let $\Omega \subseteq \mathbb{R}^n$ be a bounded domain and let $L : \Omega\times\mathbb{R}\times\mathbb{R}^n \to \mathbb{R}$, the **Lagrangian**, be measurable in its first argument and of class $C^1$ in the remaining arguments. The **variational functional** is

$$
J(u) = \int_\Omega L\bigl(x, u(x), \nabla u(x)\bigr)\,dx ,
$$

defined on a set $\mathcal{A}$ of admissible functions, typically $W^{1,p}(\Omega)$ or a subset determined by boundary data, and the problem of the calculus of variations is to find $u \in \mathcal{A}$ minimising $J$ or, more generally, with $J$ stationary at $u$.

**Definition.** Let $u \in \mathcal{A}$ and let $v$ range over the admissible variations, that is, over the directions in which $\mathcal{A}$ is locally a translate of a vector space. The **first variation** of $J$ at $u$ in the direction $v$ is the derivative

$$
\delta J(u;v) = \frac{d}{dt}J(u+tv)\Bigr|_{t=0} = \lim_{t\to0}\frac{J(u+tv)-J(u)}{t},
$$

and $u$ is a **stationary point** if $\delta J(u;v) = 0$ for every admissible $v$. A **local minimum** satisfies $J(u) \le J(u+v)$ for all sufficiently small $\|v\|$, and a **global minimum** satisfies the same inequality for all admissible $v$.

**Theorem (the first variation of an integral functional).** Let $L$ be of class $C^1$ and let $u$ be admissible with $\delta J(u;v)$ finite for all $v$. Then

$$
\delta J(u;v) = \int_\Omega\Bigl(L_u\bigl(x,u,\nabla u\bigr)\,v + L_p\bigl(x,u,\nabla u\bigr)\cdot\nabla v\Bigr)dx ,
$$

where $L_u$ and $L_p$ denote the partial derivatives of $L$ with respect to its second argument and its third argument.

*Proof.* Differentiate under the integral sign: $\frac{d}{dt}L(x,u+tv,\nabla u+t\nabla v)|_{t=0} = L_u v + L_p\cdot\nabla v$, and the domination required to interchange derivative and integral holds on the interval of $t$ for which $u+tv$ remains in a compact subset of the domain of $L$, since $L$ is $C^1$ and $v$ is bounded.

### Derivation of the Equation

**Theorem (the fundamental lemma of the calculus of variations).** Let $g$ be continuous on the bounded domain $\Omega$ and suppose that $\int_\Omega g\,v\,dx = 0$ for every $v\in C_c^\infty(\Omega)$. Then $g\equiv0$ on $\Omega$.

*Proof.* Suppose $g(x_0)\ne0$ at some point. By continuity $g$ has a fixed sign on a ball $B\subset\Omega$ about $x_0$. Choose $v\in C_c^\infty(\Omega)$ with $v\ge0$, supported in $B$ and positive at $x_0$, for instance a smooth bump; then $gv$ has a fixed sign on $B$ and is not identically zero there, so $\int_\Omega gv\,dx\ne0$, a contradiction. Hence $g=0$. ∎

The lemma is the step that converts the vanishing of an integral against every variation into the vanishing of its density, and the derivation of the Euler–Lagrange equation rests on it.

**Theorem (Euler–Lagrange equation).** Let $\Omega$ be bounded, let $L$ be of class $C^1$ and let $u$ be a stationary point of $J$ of class $C^2$ with respect to variations $v \in C_c^\infty(\Omega)$, that is, with $v$ vanishing near $\partial\Omega$. Then

$$
L_{u}\bigl(x,u,\nabla u\bigr) - \sum_{i=1}^{n}\frac{\partial}{\partial x_i}\Bigl(L_{p_i}\bigl(x,u,\nabla u\bigr)\Bigr) = 0
$$

at every point of $\Omega$.

*Proof.* For $v \in C_c^\infty(\Omega)$ the first variation vanishes, and the divergence theorem applied to the second term, whose boundary contribution vanishes because $v$ is compactly supported, gives

$$
0 = \delta J(u;v) = \int_\Omega\Bigl(L_u - \sum_i\partial_iL_{p_i}\Bigr)v\,dx .
$$

Since $v$ is arbitrary and the bracket is continuous, the fundamental lemma gives that it vanishes identically.

**Remark (the du Bois-Reymond argument).** The proof above assumes that $u$ is of class $C^2$, so that the bracket $L_u-\partial_iL_{p_i}$ is continuous and may be read off from the vanishing of the integral. When $u$ is only Lipschitz, or merely of class $W^{1,1}$, the same conclusion is reached by the argument of du Bois-Reymond: the vanishing of the first variation against all compactly supported smooth $v$ forces the bracket, interpreted as a distribution, to be the derivative of a constant, and the equation is recovered after a further integration by parts; the regularity of a minimiser, beyond the weak differentiability assumed, is then a separate theorem, quoted as standard and depending on the strict convexity of $L$ in $p$.

**Remark (higher-order integrands).** Nothing above requires the integrand to depend on $u$ and its first derivatives only. For $L(x,u,u',\dots,u^{(N)})$, the same variation with $v$ and its derivatives up to order $N-1$ compactly supported gives the **higher-order Euler–Lagrange equation**, sometimes called the **Euler–Poisson equation**

$$
L_u-\frac{d}{dx}L_{u'}+\frac{d^2}{dx^2}L_{u''}-\dots+(-1)^N\frac{d^N}{dx^N}L_{u^{(N)}}=0 ,
$$

each integration by parts moving one derivative off $v$ and onto the corresponding $L_{u^{(j)}}$ with the sign $(-1)^j$. If the variations do not vanish on $\partial\Omega$, the natural boundary conditions involve $v,v',\dots,v^{(N-1)}$ there. The canonical formulation of such integrands, and the reason they are avoided in the time variable beyond first order, is the Ostrogradsky construction treated in the article of this Part on Lagrangian and Hamiltonian systems.

**Theorem (natural boundary conditions).** If the admissible variations do not vanish on $\partial\Omega$, then stationarity additionally requires

$$
\sum_i L_{p_i}\bigl(x,u,\nabla u\bigr)\nu_i = 0 \qquad \text{on } \partial\Omega ,
$$

where $\nu$ is the outward unit normal; if the functional contains a boundary term, the corresponding condition involves the boundary integrand.

*Proof.* The divergence theorem now leaves a boundary integral $\int_{\partial\Omega}(L_p\cdot\nu)v\,dS$, which must vanish for every admissible boundary value $v$ of the variation; since $v|_{\partial\Omega}$ is arbitrary, the normal component of $L_p$ vanishes.

**Theorem (the Beltrami identity).** If $L$ does not depend explicitly on $x$, then along every $C^2$ solution of the Euler–Lagrange equation,

$$
L(u,u') - \sum_i u_i'\,L_{p_i}(u,u') = \text{constant} .
$$

*Proof.* Differentiate the left-hand side with respect to $x$: the derivative is $\sum_iL_{u_i}u_i' + \sum_iL_{p_i}u_i'' - \sum_iu_i''L_{p_i} - \sum_iu_i'\frac{d}{dx}L_{p_i} = \sum_iu_i'\bigl(L_{u_i} - \frac{d}{dx}L_{p_i}\bigr) = 0$ by the Euler–Lagrange equation.

**Remark (the two classical reductions).** If $L$ does not depend on $u$ but only on $u'$, the Euler–Lagrange equation integrates once to $L_{p_i} = c_i$; if $L$ does not depend on $x$, the Beltrami identity gives the first integral. Both are instances of the general principle that a symmetry of the Lagrangian produces a conservation law for the Euler–Lagrange equation, the theorem of Noether, stated in its general form in the article of this Part on Lagrangian and Hamiltonian systems; in the case of a one-parameter group of translations the conserved quantity is exactly the first integral above.

### The Geodesic and the Brachistochrone

**Example (geodesics).** On a Riemannian manifold $(M,g)$ the **energy** of a curve $x : [a,b]\to M$ with local coordinates $x^i$ is

$$
E(x) = \frac12\int_a^b g_{ij}(x)\dot x^i\dot x^j\,dt ,
$$

and the **length** is $\int\sqrt{g_{ij}\dot x^i\dot x^j}\,dt$. The Euler–Lagrange equation of the energy is

$$
\ddot x^k + \Gamma^k_{ij}(x)\dot x^i\dot x^j = 0, \qquad \Gamma^k_{ij} = \frac12g^{kl}\bigl(\partial_ig_{jl} + \partial_jg_{il} - \partial_lg_{ij}\bigr),
$$

the **geodesic equation**; the metric and the Levi-Civita connection are those of Part II, and the derivation is the computation of $L_{u^k} - \frac{d}{dt}L_{p_k}$ for $L = \frac12g_{ij}(x)p_ip_j$. Because the integrand of the length is homogeneous of degree one in $\dot x$, the length and the energy have the same stationary curves up to reparametrisation; a geodesic is a curve of stationary energy and, being a critical point of a length functional that is not strictly convex, is locally minimising only up to the first conjugate point.

**Example (the brachistochrone).** The problem asks for the curve $y(x)$ joining two points in a vertical plane down which a particle descends in the least time; the time is proportional to

$$
J(y) = \int_0^{x_1}\sqrt{\frac{1+y'(x)^2}{y(x)}}\,dx ,
$$

and the integrand does not depend explicitly on $x$, so the Beltrami identity applies:

$$
\sqrt{\frac{1+y'^2}{y}} - y'\frac{y'}{\sqrt{y(1+y'^2)}} = c ,
$$

which simplifies to $y(1+y'^2) = 2R$ for a constant $R$. The solution is the cycloid

$$
x = R(\theta-\sin\theta), \qquad y = R(1-\cos\theta),
$$

the two constants $R$ and the phase being fixed by the endpoints; the computation is a standard illustration of the Beltrami reduction, and it shows that the minimiser exists for a suitable pair of endpoints even though the integrand is singular at $y=0$.

## Generalizations of the Equation

### The Functional Derivative

**Definition.** Let $J(u)=\int_\Omega L(x,u,\nabla u)\,dx$ and let $\delta J(u;v)$ be its first variation. The **functional derivative** of $J$ at $u$ is the density $\delta J/\delta u$ defined by the requirement that
$$
\delta J(u;v) = \int_\Omega \frac{\delta J}{\delta u}(x)\,v(x)\,dx
$$
for every admissible variation $v$. For the integral functional above it is the Euler–Lagrange expression
$$
\frac{\delta J}{\delta u} = L_u(x,u,\nabla u) - \sum_{i=1}^n\frac{\partial}{\partial x_i}\Bigl(L_{p_i}(x,u,\nabla u)\Bigr),
$$
and in the scalar one-variable case it is $L_u - \frac{d}{dx}L_{u'}$.

*Proof.* The first variation is $\int(L_uv + L_p\cdot\nabla v)$; integrating the second term by parts, the boundary contribution vanishing for compactly supported $v$, gives $\int(L_u-\nabla\cdot L_p)v$. The identification of the density is then unique by the fundamental lemma. ∎

The functional derivative is the object whose vanishing is the stationarity condition: a differentiable functional has an extremum only where $\delta J/\delta u=0$, and the Euler–Lagrange equation is that condition written out. It is the object that the physics articles of the corpus write when they vary an action with respect to a field.

**Remark (the discrete approximation).** The equation may also be obtained by discretising the functional rather than by differentiating it. Divide $[a,b]$ into $N$ segments of length $h$ with nodes $x_m$, interpolate $u$ at the nodes by the values $y_m=u(x_m)$ with $y_0,y_N$ fixed, and replace the functional by
$$
J_h = h\sum_{m=0}^{N-1}L\Bigl(x_m,y_m,\frac{y_{m+1}-y_m}{h}\Bigr),
$$
a function of the interior values $y_1,\dots,y_{N-1}$. A variation of $y_m$ changes $L$ at the node $m$ and at the node $m-1$, through the difference quotient, and stationarity in $y_m$ gives
$$
\frac{L_p(x_m,y_m,\cdot)-L_p(x_{m-1},y_{m-1},\cdot)}{h}=L_u(x_m,y_m,\cdot),
$$
which is the finite-difference form of the equation; letting $h\to0$ along a smooth extremal recovers $L_u=\frac{d}{dx}L_{u'}$.

### Several Functions and Several Variables

**Theorem (several functions of one variable).** Let $L(x,u_1,\dots,u_p,u_1',\dots,u_p')$ be of class $C^1$ and let $J(u)=\int_a^bL\,dx$ be stationary with each $u_i$ fixed at both endpoints. Then, for each $i$,
$$
\frac{\partial L}{\partial u_i}-\frac{d}{dx}\Bigl(\frac{\partial L}{\partial u_i'}\Bigr)=0 .
$$

*Proof.* Vary one component at a time. The chosen component plays the role of the scalar $u$ and the remaining components are fixed parameters, so the scalar derivation applies to each index in turn. ∎

**Theorem (one function of several variables).** Let $\Omega\subseteq\mathbb{R}^m$ be a bounded domain, let $L(x,u,\nabla u)$ be of class $C^1$ and let $J(u)=\int_\Omega L\,dx$ be stationary with $u$ fixed on $\partial\Omega$. Then, in the weak sense on $\Omega$,
$$
\frac{\partial L}{\partial u}-\sum_{j=1}^m\frac{\partial}{\partial x_j}\Bigl(\frac{\partial L}{\partial u_{x_j}}\Bigr)=0 .
$$

*Proof.* The divergence theorem replaces the integration by parts of the scalar case. The boundary term carries the normal component of $L_p$ and vanishes because the variation vanishes on $\partial\Omega$; the interior variation is arbitrary and the fundamental lemma applies over $\Omega$. ∎

**Example (the minimal-surface equation).** For $m=2$ and $L=\sqrt{1+u_{x_1}^2+u_{x_2}^2}$, the area integrand of a graph, the equation is $\nabla\cdot(\nabla u/\sqrt{1+|\nabla u|^2})=0$, the equation of a soap film spanning a wire; the functional, its first variation and its solutions are treated in *Minimal Surfaces*. With a potential and a target metric entering $L$, the same equation defines a harmonic map, the subject of *Harmonic Maps*.

### Several Functions of Several Variables with Higher Derivatives

**Theorem (the multi-index form).** Let $\Omega\subseteq\mathbb{R}^m$ and let $L$ depend on the functions $u_1,\dots,u_p$ and on their partial derivatives $\partial^\alpha u_i$ up to order $|\alpha|\le n$, each distinct partial derivative entering $L$ once. If $J(u)=\int_\Omega L\,dx$ is stationary with $u_i$ and its derivatives of order below $n$ fixed on $\partial\Omega$, then, for each $i$,
$$
\sum_{\alpha}(-1)^{|\alpha|}\partial^\alpha\Bigl(\frac{\partial L}{\partial(\partial^\alpha u_i)}\Bigr)=0,
$$
the sum being over the multi-indices $\alpha=(\alpha_1,\dots,\alpha_m)$ with $|\alpha|\le n$, where $\partial^\alpha=\partial^{|\alpha|}/\partial x_1^{\alpha_1}\cdots\partial x_m^{\alpha_m}$, and where each multi-index is counted once, so that a mixed derivative such as $\partial^2u/\partial x_1\partial x_2$ contributes a single term.

*Proof.* Integrate by parts once for each multi-index, in the form $\int_\Omega L_{\partial^\alpha u_i}\,\delta(\partial^\alpha u_i)\,dx = (-1)^{|\alpha|}\int_\Omega\partial^\alpha\bigl(L_{\partial^\alpha u_i}\bigr)\,\delta u_i\,dx$ together with boundary terms carrying the derivatives of $u_i$ of order below $n$, which vanish by the boundary hypothesis. The remaining variation $\delta u_i$ is arbitrary and the fundamental lemma gives the equation. The sum runs over multi-indices rather than ordinary indices because the distinct partial derivatives are treated as independent variables of $L$, one per multi-index. ∎

**Remark (the specialisations).** The cases of the theorem recover the equations already written: $m=1$, $n=1$, $p=1$ is the original Euler–Lagrange equation, $p>1$ is the system of the several-functions theorem, $m>1$ with $n=1$ is the partial-differential equation, and $m=1$ with $n>1$ is the higher-order equation of the remark above. A variational equation whose integrand carries a derivative of fractional order is a fractional boundary-value problem with boundary terms at both ends, as noted in *Fractional Differential Equations*.

## The Second Variation

**Definition.** The **second variation** of $J$ at $u$ in the direction $v$ is

$$
\delta^2J(u;v) = \frac{d^2}{dt^2}J(u+tv)\Bigr|_{t=0}
= \int_\Omega\Bigl(L_{uu}v^2 + 2L_{up}\cdot v\nabla v + \nabla v\cdot L_{pp}\nabla v\Bigr)dx ,
$$

with $L_{uu}$, $L_{up}$ and $L_{pp}$ evaluated at $(x,u,\nabla u)$ and $L_{pp}$ the Hessian matrix in the gradient variables.

**Theorem (necessary and sufficient conditions).** If $u$ is a local minimum of class $C^2$, then the Euler–Lagrange equation holds and the second variation is nonnegative: $\delta^2J(u;v)\ge0$ for every admissible $v$. Conversely, if $u$ satisfies the Euler–Lagrange equation and the **strengthened Legendre condition** $L_{pp}(x,u,\nabla u)\ge\theta I$ for some $\theta>0$ and the second variation is positive for every nonzero admissible $v$, then $u$ is a local minimum in the $W^{1,\infty}$ topology.

*Proof.* The first derivative of $J$ along $u+tv$ vanishes at $t=0$ by stationarity, and the second derivative is the displayed quadratic form in $v$; a local minimum has nonnegative second derivative at a stationary point by Taylor's formula in $t$, which proves necessity. For sufficiency, the strengthened convexity in the gradient variables bounds $J(u+v)-J(u)$ below by a positive multiple of $\|v\|_{W^{1,2}}^2$ for small $v$, whence the minimum.

**Definition.** For the one-dimensional problem the **Legendre condition** is $L_{pp}\ge0$ and the **strengthened Legendre condition** is $L_{pp}>0$; the **Jacobi equation** is the linearisation of the Euler–Lagrange equation along a solution, and a **conjugate point** is a zero of a nontrivial Jacobi field vanishing at the initial point. A solution is a local minimum of the length or energy if the strengthened Legendre condition holds and there is no conjugate point in the open interval.

**Theorem (Jacobi).** Let $u$ be a solution of the scalar Euler–Lagrange equation on $[a,b]$ with $L_{pp}>0$, and suppose no point of $(a,b]$ is conjugate to $a$. Then $u$ is a local minimum of $J$ among curves with the same endpoints; if a conjugate point lies in $(a,b)$, then $u$ is not a minimum.

*Proof.* Quoted as standard (the Jacobi condition). The second variation is a quadratic form whose associated Sturm–Liouville problem has no zero eigenvalue precisely when there is no conjugate point, by the Sturm oscillation theory; the positivity of the quadratic form is then equivalent to the absence of conjugacy, and the strengthened Legendre condition supplies the ellipticity of that Sturm–Liouville problem.

The conjugate-point theory is what makes the geodesic example precise: a geodesic minimises length up to its first conjugate point and not beyond, and the conjugate points are computed from the curvature through the Jacobi equation, which is the subject of the geometry of Part II.

## The Direct Method

### Existence of Minimisers

**Definition.** Let $V$ be a reflexive Banach space and let $J : V \to \mathbb{R}\cup\{+\infty\}$. The functional is **coercive** if $J(u)\to+\infty$ as $\|u\|\to\infty$, and **sequentially weakly lower semicontinuous** if $u_m \rightharpoonup u$ implies $J(u) \le \liminf_mJ(u_m)$.

**Theorem (direct method).** Let $V$ be a reflexive Banach space and let $J$ be coercive and sequentially weakly lower semicontinuous. Then $J$ attains its minimum on $V$.

*Proof.* Let $(u_m)$ be a minimising sequence; coercivity keeps it bounded, and reflexivity (the Banach–Alaoglu theorem, in the form of *Banach and Hilbert Spaces*) gives a weakly convergent subsequence $u_{m_k}\rightharpoonup u$. Weak lower semicontinuity gives $J(u)\le\liminf_kJ(u_{m_k}) = \inf_VJ$, so $u$ is a minimiser.

**Theorem (Tonelli).** Let $\Omega$ be bounded, let $1<p<\infty$ and let $L : \Omega\times\mathbb{R}\times\mathbb{R}^n\to\mathbb{R}$ satisfy a growth condition

$$
L(x,s,p) \ge \alpha|p|^p - \beta(s) , \qquad \beta \in L^1(\Omega),
$$

with $\alpha>0$, and let $L$ be convex in $p$ for each $(x,s)$. Then $J$ is sequentially weakly lower semicontinuous on $W^{1,p}(\Omega)$; in particular, if $J$ is coercive, it has a minimiser.

*Proof.* Quoted as standard. Convexity of $L$ in $p$ gives, for each $(x,s)$ and every $q$, the affine lower bound $L(x,s,p) \ge L(x,s,q) + L_p(x,s,q)\cdot(p-q)$; integrating along a weakly convergent sequence and passing to the limit in the linear terms, whose coefficients are fixed $L^1$ functions, leaves the convex part $\int L$ and gives the lower semicontinuity. The growth condition makes $J$ well defined and coercive on the reflexive space $W^{1,p}$.

**Remark (why convexity and not just stationarity).** A stationary point of a nonconvex functional need not be a minimum: the Euler–Lagrange equation is a necessary condition only. The direct method supplies existence by compactness, and convexity is the hypothesis that makes the functional's sublevel sets convex and the weak limit a minimiser. For a nonconvex problem the minimiser may fail to exist, or may exist but fail to satisfy the Euler–Lagrange equation in the classical sense; the existence theory then proceeds through relaxation, in which the functional is replaced by its lower convex envelope on an enlarged space.

### Regularity of Minimisers

**Theorem (regularity).** Let $L$ be of class $C^\infty$, strictly convex and uniformly elliptic in $p$, that is, $L_{pp}(x,s,p)\ge\theta I$ for some $\theta>0$, and let $u \in W^{1,2}(\Omega)$ minimise $J$ among functions with given boundary values on a smooth domain. Then $u$ is of class $C^\infty(\overline\Omega)$ in the interior and, if the boundary data are smooth, up to the boundary; more generally $u$ solves the weak form of the elliptic equation

$$
-\nabla\cdot\bigl(L_p(x,u,\nabla u)\bigr) + L_u(x,u,\nabla u) = 0
$$

and inherits the regularity theorem of the preceding article.

*Proof.* The weak form of the equation is exactly the vanishing of the first variation, so $u$ is a weak solution of a quasilinear elliptic equation; since $L$ is uniformly convex in the gradient, the linearised operator is uniformly elliptic with bounded measurable coefficients, and the difference-quotient argument of the preceding article applies. For the full regularity, including the case of non-smooth coefficients and the resolution of Hilbert's nineteenth problem, the argument is the De Giorgi–Nash–Moser theory, quoted as standard.

## Constrained Problems

### The Lagrange Multiplier Rule

**Theorem (Lagrange multipliers).** Let $J, K_1,\dots,K_m$ be $C^1$ functionals on an open subset of a Banach space $V$ and let $u$ be a stationary point of $J$ subject to the constraints $K_j(u)=0$, with the derivatives $DK_j(u)$ linearly independent. Then there are constants $\lambda_1,\dots,\lambda_m$ with

$$
DJ(u) = \sum_{j=1}^m\lambda_j\,DK_j(u),
$$

so that $u$ is a stationary point of the unconstrained functional $J - \sum_j\lambda_jK_j$.

*Proof.* Quoted as standard (the Lagrange multiplier rule in Banach space, the Lyusternik form). The surjectivity of the derivative of the constraint map $K=(K_1,\dots,K_m)$ onto $\mathbb{R}^m$ permits the implicit function theorem to write the constraint set as a graph over the kernel of $DK(u)$, reducing the problem to an unconstrained one on that kernel, and the abstract multiplier rule gives the coefficients.

**Example (the isoperimetric problem).** Among closed plane curves of fixed length $\ell$, find the one enclosing the greatest area. With the curves parametrised by arclength and $A$ and $\ell$ the area and length functionals, the multiplier rule applied to $A - \lambda\ell$ gives the Euler–Lagrange equation of a constant-curvature curve, whose only closed solution is the circle, with $\ell = 2\pi r$ and $A = \pi r^2$; the example is the prototype of a constrained variational problem and its solution is the circle. The computation is exact for the radial family and the circle is the unique smooth maximiser.

**Theorem (variational problem with a holonomic constraint).** Let $J(u) = \int_a^bL(x,u,u')dx$ be stationary subject to the pointwise constraint $G(x,u(x))=0$ with $G$ of full rank. Then the Euler–Lagrange equation acquires a multiplier, $L_u - \frac{d}{dx}L_{u'} = \lambda\,G_u$, and the constrained problem is a differential-algebraic system of the type studied in the article of this category on differential-algebraic equations, with the multiplier $\lambda$ determined by the constraint and its derivatives.

*Proof.* The constraint is imposed pointwise, so the admissible variations $v$ satisfy $G_uv=0$ at each point; the multiplier rule in its pointwise form gives $L_u - \frac{d}{dx}L_{u'} = \lambda G_u$ with $\lambda$ a functions of $x$, and the resulting system of the Euler–Lagrange equation together with $G=0$ is a differential-algebraic system whose index is computed as in that article.

## The Hamiltonian Reformulation

**Theorem (Legendre transform).** Let $L(x,u,p)$ be strictly convex and superlinear in $p$, and define the **conjugate** or **Hamiltonian** function

$$
H(x,u,p^*) = \sup_{p}\bigl(p\cdot p^* - L(x,u,p)\bigr) = p\cdot p^* - L(x,u,p)\big|_{\,p^* = L_p(x,u,p)} ,
$$

the supremum being attained at the unique $p$ solving $p^*=L_p$. Then the Euler–Lagrange equation $L_u = \frac{d}{dx}L_{u'}$ is equivalent to the system

$$
u' = H_{p^*}, \qquad (p^*)' = -H_u ,
$$

the **Hamiltonian system**, and along solutions $H$ is constant when $L$ does not depend explicitly on $x$.

*Proof.* The envelope theorem gives $H_{p^*} = p$ and $H_u = -L_u$ at the stationary point of the supremum, so the Euler–Lagrange equation $(p^*)' = L_u = -H_u$ together with the definition $u' = p = H_{p^*}$. The constancy of $H$ for an autonomous $L$ is the computation $\frac{d}{dx}H = H_uu' + H_{p^*}(p^*)' = H_uH_{p^*} - H_{p^*}H_u = 0$.

The Legendre transform converts the second-order Euler–Lagrange equation into a first-order system in twice as many variables, and the Hamiltonian system is the form in which the conservation laws and the geometry of the solution space are read. The development of the Hamiltonian formalism — symplectic structure, canonical transformations, Poisson brackets — belongs to the article of this Part on Lagrangian and Hamiltonian systems; the variational derivation given here is the input to it.

### The Hamilton–Jacobi Equation and Noether's Theorem

**Definition.** Let $S = S(x,u)$ be a $C^2$ function, the **action as a function of the endpoint**, with $S_u\neq0$. The **Hamilton–Jacobi equation** associated with the Lagrangian $L(x,u,p)$ is

$$
S_x + H\bigl(x, u, S_u\bigr) = 0 ,
$$

where $H$ is the Hamiltonian of the Legendre transform above and the conjugate momentum has been replaced by $S_u$.

**Theorem (the action solves the Hamilton–Jacobi equation).** Fix an initial point $(x_0,u_0)$ and let $\mathcal{S}(x,u)$ be the value of the functional $J$ evaluated at the extremal joining $(x_0,u_0)$ to $(x,u)$, for $(x,u)$ near a point at which the extremals do not focus. Then $\mathcal{S}$ is differentiable and satisfies the Hamilton–Jacobi equation, and along an extremal $u(x)$ one has $\mathcal{S}_u(x,u(x)) = L_p(x,u(x),u'(x))$.

*Proof.* The derivative of $\mathcal{S}$ with respect to the endpoint is the boundary term obtained by differentiating the integral along the extremal: $\mathcal{S}_x = L - u'L_p$ and $\mathcal{S}_u = L_p$. Substituting $p^* = L_p = \mathcal{S}_u$ into the identity $L - u'\mathcal{S}_u$ and using the definition of $H$ as the Legendre transform gives $\mathcal{S}_x = -H(x,u,\mathcal{S}_u)$.

**Theorem (Noether).** Let $G$ be a one-parameter group of transformations of the variables $(x,u)$ leaving the functional $J$ invariant, with infinitesimal generator $(\xi,\eta)$. Then the quantity

$$
N = \xi\Bigl(L - \sum_iu_i'L_{p_i}\Bigr) + \sum_i\eta_iL_{p_i}
$$

is constant along every solution of the Euler–Lagrange equation.

*Proof.* Quoted as standard. The invariance of the integral under the group means that the derivative of $J$ with respect to the group parameter vanishes identically for every curve, not merely at an extremal; writing this derivative as an integral, integrating by parts and using the Euler–Lagrange equation leaves only the boundary term, which is the derivative of the displayed quantity.

**Example (translation invariance).** For $L$ independent of $x$ the group is the translation $x\mapsto x+\varepsilon$ with $\xi=1$, $\eta=0$, and Noether's quantity is $L-\sum_iu_i'L_{p_i}$, the Beltrami first integral. For $L$ independent of a component $u_i$ the group is the translation of that component with $\eta_i=1$, and the conserved quantity is the conjugate momentum $L_{p_i}$. The Beltrami identity of the first section is thus the translation case of Noether's theorem.

## Summary

The calculus of variations seeks the extrema of an integral functional $J(u)=\int_\Omega L(x,u,\nabla u)dx$. Its first variation is $\delta J(u;v) = \int(L_uv + L_p\cdot\nabla v)$, and on a stationary point with vanishing boundary variations it vanishes for every smooth $v$ exactly when the Euler–Lagrange equation $L_u - \nabla\cdot L_p = 0$ holds; when the variations do not vanish on the boundary, the natural boundary condition $L_p\cdot\nu=0$ is added. The geodesic equation of a Riemannian metric and the cycloid of the brachistochrone are the two classical examples, the first reduced by the homogeneity of the length and the second by the Beltrami identity $L - u'\cdot L_{u'} = $ constant, which is the first integral produced by the absence of an explicit dependence on the independent variable.

The second variation decides the nature of a stationary point: it is nonnegative at a local minimum, and the strengthened Legendre condition $L_{pp}>0$ together with the absence of a conjugate point in the interval makes the stationary point a local minimum, by the Jacobi condition. The direct method proves existence without solving the equation: a coercive, sequentially weakly lower semicontinuous functional on a reflexive space attains its minimum, and Tonelli's theorem supplies the lower semicontinuity from the convexity of $L$ in the gradient together with a growth condition. A minimiser of a uniformly convex Lagrangian is a weak solution of a quasilinear elliptic equation and is smooth by the regularity theory of the preceding article. Constrained problems are handled by the Lagrange multiplier rule; the isoperimetric problem yields the circle, and a holonomic constraint yields a multiplier and a differential-algebraic system. Beyond the scalar case the same derivation gives the functional derivative $\delta J/\delta u = L_u - \nabla\cdot L_p$, whose vanishing is the stationarity condition; the system of one equation for each of several unknown functions; the partial-differential equation for one function of several variables, whose area case is the minimal-surface equation; and the multi-index equation for several functions of several variables with higher derivatives. Finally the Legendre transform converts the Euler–Lagrange equation into a Hamiltonian system, the form in which the theory of this Part on Lagrangian and Hamiltonian systems proceeds.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J(u)$ | Variational functional $\int_\Omega L(x,u,\nabla u)dx$ |
| $L(x,s,p)$ | Lagrangian; $L_u$, $L_p$ its partial derivatives, $L_{pp}$ the Hessian in $p$ |
| $\delta J(u;v)$, $\delta^2J(u;v)$ | First and second variations |
| $\mathcal{A}$ | Admissible class of functions |
| Euler–Lagrange equation | $L_u - \nabla\cdot L_p = 0$ |
| Fundamental lemma | $\int_\Omega gv = 0$ for all $v\in C_c^\infty$ implies $g=0$ |
| Functional derivative | $\delta J/\delta u = L_u - \nabla\cdot L_p$ |
| Higher-order equation | $\sum_{k=0}^{N}(-1)^k\frac{d^k}{dx^k}L_{u^{(k)}}=0$ |
| Multi-index form | $\sum_\alpha(-1)^{|\alpha|}\partial^\alpha L_{\partial^\alpha u}=0$ |
| Natural boundary condition | $L_p\cdot\nu = 0$ on $\partial\Omega$ |
| Beltrami identity | $L - \sum_iu_i'L_{p_i} = $ constant for autonomous $L$ |
| $g_{ij}$, $\Gamma^k_{ij}$ | Metric and Christoffel symbols of Part II |
| Legendre condition | $L_{pp}\ge0$; strengthened when $L_{pp}>0$ |
| Jacobi equation, conjugate point | Linearisation along a solution; zero of a Jacobi field |
| coercive, weakly lower semicontinuous | Hypotheses of the direct method |
| $K_j$, $\lambda_j$ | Constraint functionals and their Lagrange multipliers |
| $H(x,u,p^*)$ | Hamiltonian, the Legendre transform of $L$ |
| $p^* = L_p$ | Conjugate momentum |

## Further Reading

- Oskar Bolza, *Lectures on the Calculus of Variations* (University of Chicago Press, 1904), for the classical theory of the first and second variation.
- I. M. Gelfand and Sergei V. Fomin, *Calculus of Variations* (Prentice-Hall, 1963), for the Euler–Lagrange equation, the natural boundary conditions, the functional derivative and the several-variable forms.
- Mariano Giaquinta and Stefan Hildebrandt, *Calculus of Variations I: The Lagrangian Formalism* (Springer, 1996), for the second variation and the Jacobi condition.
- Enrico Giusti, *Direct Methods in the Calculus of Variations* (World Scientific, 2003), for the direct method and Tonelli's theorem.
- Bernard Dacorogna, *Direct Methods in the Calculus of Variations* (Springer, 2nd ed. 2008), for lower semicontinuity and relaxation.
- Leonida Tonelli, *Fondamenti di calcolo delle variazioni* (Zanichelli, 1921), for the original existence theory.
- Ennio De Giorgi, "Sulla differenziabilità e l'analiticità degli integrali multipli regolari", *Memorie della Accademia delle Scienze di Torino* 3 (1957), for the regularity of minimisers.
- Jurgen Jost and Xinwei Li-Jost, *Calculus of Variations* (Cambridge University Press, 1998), for a modern treatment including the Hamiltonian formulation.
- Richard Courant and David Hilbert, *Methods of Mathematical Physics*, Vol. I (Interscience, 1953), for the functional derivative, the higher-order and multi-index generalisations and the polygonal approximation.
- Richard Courant, *Differential and Integral Calculus*, Vol. II (Blackie, 1936), for the tautochrone and the historical calculus of variations.
