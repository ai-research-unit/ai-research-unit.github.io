# __Distributions on Surfaces, Layers, and Jump Conditions__

## Introduction

A function that is smooth on each side of a hypersurface but discontinuous across it is not a classical solution of a differential equation, and its derivatives are distributions rather than functions. The terms they produce are concentrated on the surface, and the calculus of those terms is the subject of this article. It is the part of distribution theory in which the support of a distribution, instead of being a point or all of space, is a surface of codimension one, and it is the tool that turns a discontinuous field into a set of equations for its jump.

Three objects carry the theory. The **surface delta** $\delta_S$ is the distribution that integrates a test function over the surface; it is the layer of order zero, the **single layer**. Its normal derivative $\partial_n\delta_S$ is the layer of order one, the **double layer**, and the two are the first terms of the general expansion of a distribution supported on $S$. The **jump formula**,
$$
\partial_j u = \{\partial_j u\} + [u]\,n_j\,\delta_S,
$$
separates the classical derivative of a piecewise smooth function from the layer its jump creates, where $\{\partial_j u\}$ is the classical derivative away from the surface and $[u]$ is the jump. The **jump conditions** of a differential equation are the equations obtained by collecting the layers in $Pu=f$, and the **characteristic** of the principal symbol in the normal direction decides whether a jump is possible at all.

The article is organised as follows. The surface delta and the coarea formula are established first; the jump formula and its corollaries for the gradient, the divergence and the rotor follow; the layer expansion of a distribution supported on a surface is then given, with the single and double layers as its first terms. The surface differential operators and the two layer identities are treated next, and the article closes with the jump conditions of first- and second-order equations, with the Rankine–Hugoniot condition of a conservation law, and with the trace problem that decides when a restriction to the surface exists.

Throughout, $S \subseteq \mathbb{R}^n$ is a hypersurface of class $C^2$, $n \ge 2$, described near a point by a defining function $\varphi$ with $S = \{\varphi = 0\}$ and $\nabla\varphi \neq 0$ on $S$. The unit normal is
$$
n = \frac{\nabla\varphi}{|\nabla\varphi|},
$$
oriented so that $\varphi$ increases across $S$ in the direction of $n$. The **jump** of a function across $S$ is
$$
[u] = u^{+} - u^{-}, \qquad u^{\pm}(x) = \lim_{\varepsilon \to +0} u(x \pm \varepsilon n),
$$
the value on the far side minus the value on the near side with respect to $n$. The distributional notation, the multiplication by a smooth function and the differentiation by transposition are those of the companion article *Distributions and Fundamental Solutions*; the coarea formula and the surface measure are those of *Geometric Measure Theory* and *Measure Theory and Integration*; Stokes' theorem on a surface is that of *Differential Forms and Stokes' Theorem*; the characteristics of a first-order equation and the classification of the second-order types are those of *Partial Differential Equations*; and the traces of a Sobolev function are those of *Sobolev Spaces and Weak Solutions*. The restriction of a distribution and the wavefront set that governs it are used in one closing section and belong to *Microlocal Analysis*; the boundary behaviour of the layer potentials and the integral equations of the Dirichlet problem belong to *Potential Theory*.

No physics is invoked.

## The Surface Delta and the Coarea Formula

### The Surface Measure and the Delta

**Definition.** The **surface delta** of $S$ is the distribution
$$
\langle \delta_S, \psi \rangle = \int_S \psi\, dS, \qquad \psi \in \mathcal{D}(\mathbb{R}^n),
$$
where $dS$ is the surface measure of $S$. It is a positive measure on $\mathbb{R}^n$ of order $0$, its support is exactly $S$, and it is singular with respect to Lebesgue measure.

A distribution of order zero supported on a hypersurface is integration against a measure carried by that hypersurface, by the structure theorem of *Distributions and Fundamental Solutions*; $\delta_S$ is the case in which the measure is the surface measure itself, and a general such measure is $g\,\delta_S$ for a density $g$ on $S$.

### The Coarea Formula

**Proposition (the surface delta as a composed delta).** Let $\varphi$ be a defining function of $S$ with $\nabla\varphi \neq 0$ on $S$. Then
$$
\delta_S = |\nabla\varphi|\,\delta \circ \varphi,
$$
where $\delta$ is the delta on the real line and $\delta \circ \varphi$ is the distribution $\psi \mapsto \langle \delta, \psi \rangle$ composed with $\varphi$.

*Proof.* The coarea formula applied to the level sets of $\varphi$ states that for $\psi \in C_c^\infty(\mathbb{R}^n)$
$$
\int_{\mathbb{R}^n} \psi(x)\,\delta(\varphi(x))\,dx = \int_{\mathbb{R}} \delta(t)\left(\int_{\{\varphi = t\}} \frac{\psi}{|\nabla\varphi|}\, dS_t\right) dt = \int_S \frac{\psi}{|\nabla\varphi|}\, dS,
$$
because the coarea measure of the level set $\{\varphi = t\}$ is $dS_t/|\nabla\varphi|$. Multiplying both sides by $|\nabla\varphi|$ gives the stated identity.
$\square$

The identity is the reason a surface is described by a distribution at all: it converts the codimension-one geometry into a one-dimensional delta composed with the defining function, and it is the form in which a surface is entered into a differential operator. Its normalisation is the thing to check: for the unit sphere in $\mathbb{R}^3$, with $\varphi(x) = |x| - 1$ and $|\nabla\varphi| = 1$, the pairing of $\delta_S$ with the constant $1$ is the area $4\pi$.

### The Chain Rule with the Heaviside Function

**Proposition.** Let $H(t) = \mathbf{1}_{t>0}$ be the Heaviside function. Then, in $\mathcal{D}'(\mathbb{R}^n)$,
$$
\partial_j H(\varphi) = n_j\,\delta_S, \qquad \nabla H(\varphi) = n\,\delta_S .
$$

*Proof.* The chain rule for the composition of a distribution with a smooth function whose gradient does not vanish gives $\partial_j H(\varphi) = \varphi_j\,(\delta \circ \varphi)$. By the proposition above, $\delta \circ \varphi = \delta_S/|\nabla\varphi|$, so $\partial_j H(\varphi) = \varphi_j \delta_S/|\nabla\varphi| = n_j \delta_S$.
$\square$

Thus $H(\varphi)$ is the indicator of the side $\{\varphi > 0\}$, its gradient is the **normal layer** $n\,\delta_S$, and the two-sided classical derivative of $H(\varphi)$ is zero. The layer is exactly the term produced by the discontinuity of the indicator, and the formula is the building block of the jump formula below.

## The Jump Formula

### Piecewise Smooth Functions

**Definition.** A function $u$ on a neighbourhood $U$ of a point of $S$ is **piecewise smooth** across $S$ if $u = u^{+}H(\varphi) + u^{-}(1 - H(\varphi))$, with $u^{+}$ and $u^{-}$ of class $C^2$ on $U$. Its **classical derivative away from $S$** is
$$
\{\partial_j u\} = H(\varphi)\,\partial_j u^{+} + (1 - H(\varphi))\,\partial_j u^{-},
$$
and its **jump** is $[u] = u^{+}|_S - u^{-}|_S$, a function on $S$.

The definition applies unchanged when the two extensions are smooth on the two closed sides and the derivatives are declared to be the one-sided ones; it is local and it does not require $S$ to be closed.

### The Jump Formula

**Theorem (jump formula).** Let $u$ be piecewise smooth across $S$. Then, in $\mathcal{D}'(U)$,
$$
\partial_j u = \{\partial_j u\} + [u]\,n_j\,\delta_S .
$$

*Proof.* Differentiate the product $u = u^{+}H(\varphi) + u^{-}(1 - H(\varphi))$ by the Leibniz rule:
$$
\partial_j u = H(\varphi)\,\partial_j u^{+} + (1 - H(\varphi))\,\partial_j u^{-} + (u^{+} - u^{-})\,\partial_j H(\varphi).
$$
The first two terms are $\{\partial_j u\}$ and the last is $(u^{+} - u^{-})n_j \delta_S = [u]n_j\delta_S$ by the chain rule above.
$\square$

The formula is the distributional content of the divergence theorem with a discontinuous integrand, and it is valid whatever the orientation of $n$: reversing $n$ reverses both the sign of $n_j$ and the sign of $[u]$, since the two traces are interchanged.

### The Gradient, the Divergence and the Rotor

**Corollary.** For a piecewise smooth scalar $u$ and a piecewise smooth vector field $A$,
$$
\nabla u = \{\nabla u\} + [u]\,n\,\delta_S,
$$
$$
\mathrm{div}\,A = \{\mathrm{div}\,A\} + (n \cdot [A])\,\delta_S,
$$
and, for $n = 3$,
$$
\mathrm{rot}\,A = \{\mathrm{rot}\,A\} + n \times [A]\,\delta_S .
$$

*Proof.* The first two are the component forms of the jump formula. For the rotor, write $(\mathrm{rot}\,A)_i = \epsilon_{ijk}\partial_j A_k$; the jump formula makes the singular part $\epsilon_{ijk}[A_k]n_j\delta_S = (n \times [A])_i\delta_S$, which is the stated tangential vector.
$\square$

The divergence and the rotor therefore see the **normal** and the **tangential** parts of the jump respectively. The singular part of the divergence is a simple layer with density $n\cdot[A]$, and the singular part of the rotor is a tangential simple layer $n\times[A]$. The two are exactly the surface charge and the surface current of a discontinuous field.

### The Jump of a Product

**Corollary.** For piecewise smooth $u$ and $v$, the jump of the product is
$$
[uv] = u^{+}[v] + [u]\,v^{-}.
$$

*Proof.* Expand $u^{+}v^{+} - u^{-}v^{-} = u^{+}(v^{+} - v^{-}) + (u^{+} - u^{-})v^{-}$.
$\square$

There is no classical Leibniz rule for $[uv]$ alone, because the product rule involves both the jump and one of the traces; the formula above is the correct replacement and it reduces to $[uv] = [u]v$ when $v$ is continuous across $S$.

## Layers and the Structure Theorem

### Single and Double Layers

**Definition.** Let $g$ be smooth on $S$. The **single layer** of density $g$ is the distribution $g\,\delta_S$, with
$$
\langle g\,\delta_S, \psi \rangle = \int_S g\,\psi\, dS .
$$
The **double layer** of density $g$ is the distribution $g\,\partial_n\delta_S$, where $\partial_n = n \cdot \nabla$ is the normal derivative, with
$$
\langle g\,\partial_n\delta_S, \psi \rangle = -\int_S \bigl(g\,\partial_n \psi + \psi\,\partial_n g\bigr) dS .
$$

The single layer is a measure and has order $0$; the double layer has order $1$ and is not a measure. The two names are the classical ones of potential theory, where $g\delta_S$ is the density of a distribution of charge on $S$ and $g\partial_n\delta_S$ is the density of a distribution of dipoles normal to $S$.

### The Structure of a Distribution Supported on a Surface

**Theorem (layer expansion).** Let $u \in \mathcal{D}'(\mathbb{R}^n)$ with $\operatorname{supp} u \subseteq S$. Then $u$ is locally a finite sum
$$
u = \sum_{k=0}^{N} \partial_n^{\,k}(g_k\,\delta_S),
$$
with densities $g_k$ that are distributions on $S$.

*Proof (local).* Flatten the surface: near a point choose coordinates $(x',x_n)$ in which $\varphi = x_n$ and $S = \{x_n = 0\}$, so that $n = e_n$ and $\delta_S = \delta(x_n)$. A distribution on $\mathbb{R}^n$ supported in the hyperplane $x_n = 0$ is a finite sum of derivatives of the delta in the normal variable, acting on the tangential variables as a parameter,
$$
u = \sum_{k=0}^{N} g_k(x')\,\delta^{(k)}(x_n),
$$
with $g_k \in \mathcal{D}'(\mathbb{R}^{n-1})$; this is the structure theorem applied in the normal variable with the tangential dependence retained. Since $\delta^{(k)}(x_n) = \partial_n^{\,k}\delta(x_n)$ in these coordinates, the display is the stated expansion. The densities are unique because the coefficients of a distribution supported on a hyperplane are determined by its pairings with the test functions $\psi(x')x_n^{k}$.
$\square$

The expansion is the surface analogue of the statement that a distribution supported at a point is a combination of $\delta$ and its derivatives. Its order-zero term is the single layer, its order-one term the double layer, and the higher terms the layers of higher order. Every layer is thus a normal derivative of a single layer, and a differential operator produces layers only up to the order of the operator: a first-order operator can produce at most a single layer, a second-order operator at most a double layer.

### The Laplacian of a Piecewise Smooth Function

**Example.** Let $S = \{x_n = 0\}$ locally and let $u$ be piecewise smooth across it. Then
$$
\Delta u = \{\Delta u\} + [\partial_n u]\,\delta_S + [u]\,\partial_n\delta_S .
$$

*Proof.* Apply $\partial_j$ to the jump formula and sum over $j$. The term $\partial_j([u]n_j\delta_S)$ is $[u]\partial_n\delta_S$ when the density $[u]$ is extended constantly along $n$, and the term $[\partial_j u]n_j\delta_S$ is $[\partial_n u]\delta_S$. The remaining contributions vanish in the flat coordinates in which $n$ is constant.
$\square$

This is the layer decomposition of a second-order operator. For $\Delta u = f$ with $f$ continuous across $S$, the double-layer and single-layer coefficients must vanish separately, giving $[u] = 0$ and $[\partial_n u] = 0$: a piecewise harmonic function with a continuous Laplacian is continuous together with its normal derivative. If $f = g\delta_S$ has a single-layer source, the double layer still vanishes and the single-layer condition reads $[\partial_n u] = g$. This is the distributional form of the transmission conditions of an interface.

## Surface Differential Operators

### The Tangential Gradient and the Surface Divergence

**Definition.** The **tangential projection** at a point of $S$ is $P = \mathrm{I} - n \otimes n$, the orthogonal projection onto the tangent space. For a smooth function $f$ on a neighbourhood of $S$, the **tangential gradient** is
$$
\nabla_S f = P\,\nabla f = \nabla f - (\partial_n f)\,n .
$$
For a vector field $a$ tangent to $S$ (so $a \cdot n = 0$), the **surface divergence** $\mathrm{div}_S\,a$ is the scalar function on $S$ defined by the integration by parts
$$
\int_S (\mathrm{div}_S\,a)\,\psi\, dS = -\int_S a \cdot \nabla_S \psi\, dS
$$
for every smooth $\psi$ on $S$.

The definition is intrinsic: it uses only the tangential field and the surface measure, and it does not depend on how $a$ is extended off $S$. The surface divergence theorem, obtained from Stokes' theorem for the $(n-1)$-form dual to $a$, is
$$
\int_S \mathrm{div}_S\,a\, dS = \oint_{\partial S} a \cdot m\, d\ell,
$$
with $m$ the outward co-normal in $S$ and $d\ell$ the measure on $\partial S$; on a closed surface the integral vanishes.

### The Surface Rotor

**Definition.** Let $n = 3$ and let $S$ be oriented by $n$. For a vector field $a$ tangent to $S$, the **surface rotor** is the scalar function
$$
\mathrm{rot}_S\,a = (\mathrm{rot}\,a)\cdot n,
$$
and for a smooth function $f$ the **rotated tangential gradient** is the tangential vector
$$
\mathrm{rot}_S\,f = n \times \nabla_S f .
$$
Stokes' theorem on the oriented surface with boundary gives
$$
\oint_{\partial S} a \cdot d\ell = \int_S \mathrm{rot}_S\,a\, dS,
$$
which is the definition of the surface rotor read as a circulation density, and the two operators are adjoint on a closed surface by the same integration by parts.

The rotor enters the calculus of a discontinuous field through the jump formula, not through the surface operator alone: the singular part of the spatial rotor $\mathrm{rot}\,A$ is the tangential layer $n \times [A]\,\delta_S$, whose density is the tangential vector rotated from the jump. That density is a surface current, and its surface divergence is what appears in the surface conservation law below.

### The Two Layer Identities

Two identities separate the behaviour of a tangential layer from that of a normal one, and they are the reason a surface current closes into a surface conservation law while a normal layer produces a double layer.

**Proposition.** Let $a$ be a vector field tangent to $S$, extended so that it is constant along $n$. Then
$$
\mathrm{div}(a\,\delta_S) = (\mathrm{div}_S\,a)\,\delta_S .
$$
For the normal layer, with $n$ extended off $S$,
$$
\mathrm{div}(n\,\delta_S) = \partial_n \delta_S + (\mathrm{div}_S\,n)\,\delta_S .
$$

*Proof.* In flat local coordinates $S = \{x_n = 0\}$, $n = e_n$ and $\delta_S = \delta(x_n)$. For the first identity, $a_n = 0$ and $\partial_n a = 0$, so $\mathrm{div}\,a = \mathrm{div}_S\,a$ and, since the tangential derivatives of $\delta(x_n)$ vanish, $\mathrm{div}(a\delta_S) = (\mathrm{div}\,a)\delta_S = (\mathrm{div}_S a)\delta_S$. For the second, the normal component $n_n = 1$ contributes $\partial_n\delta(x_n) = \partial_n\delta_S$, and the tangential variation of $n$ contributes $(\mathrm{div}_S\,n)\delta_S$, which is the mean-curvature term and vanishes in the flat coordinates.
$\square$

Both identities are of first order: a tangential layer is differentiated into a tangential layer, and a normal layer is differentiated into a double layer plus a curvature layer. There is no double layer in the divergence of a surface current, and this is why the surface charge and the surface current are ordinary simple layers.

## Jump Conditions for Linear Equations

### The Singular Part and the Principal Symbol

Let
$$
P = \sum_{|\alpha| \le m} a_\alpha(x)\,\partial^\alpha
$$
be a linear differential operator of order $m$ with smooth coefficients, acting on scalar functions or componentwise on a system, and let $u$ be piecewise smooth across $S$ with $Pu = f$. Collecting the layers of highest order in $Pu$, the **singular part** of $Pu$ is determined by the **principal symbol** evaluated on $n$:
$$
\text{singular part of } Pu = \sigma_P(n)\,[u]\,\partial_n^{\,m-1}\delta_S + \text{terms of lower layer order},
\qquad \sigma_P(n) = \sum_{|\alpha| = m} a_\alpha(x)\,n^\alpha .
$$
For a system, $\sigma_P(n)$ is the principal-symbol matrix and $[u]$ the vector of jumps. Since the source $f$ is a fixed distribution, the singular part of $Pu$ is the singular part of $f$; when $f$ is continuous across $S$ it has no singular part, and the layers in $Pu$ must cancel among themselves at each layer order.

**Definition.** The normal $n$ is **characteristic** for $P$ at a point of $S$ if $\sigma_P(n)$ is not invertible, that is $\det \sigma_P(n) = 0$ for a system and $\sigma_P(n) = 0$ for a scalar operator; it is **non-characteristic** if $\sigma_P(n)$ is invertible.

### First-Order Equations and Characteristics

**Theorem (first-order jump condition).** Let $P = \sum_j a_j\partial_j + b$ be of first order and let $u$ be piecewise smooth with $Pu = f$, the source $f$ being continuous across $S$. Then
$$
\sigma_P(n)\,[u] = 0 .
$$
Consequently, if $n$ is non-characteristic, then $[u] = 0$ and the solution is continuous across $S$; if $n$ is characteristic, then $[u]$ lies in the kernel of $\sigma_P(n)$ and the jump is admissible.

*Proof.* By the jump formula the singular part of $Pu$ is $(\sum_j a_j n_j)[u]\delta_S = \sigma_P(n)[u]\delta_S$. Since $f$ is continuous, its singular part vanishes, and the coefficient of the single layer $\delta_S$ must vanish.
$\square$

The dichotomy is the whole content of the wavefront analysis of a first-order system: a non-characteristic surface cannot carry a jump, and a characteristic surface can, its admissible jumps being the kernel of the principal symbol in the normal direction. The linear transport equation $u_t + a\,u_x = 0$ has $\sigma_P(\nu) = \nu_t + a\nu_x$, which vanishes on the lines $x = at$; the jump of a piecewise constant solution $u = u^{-}$ for $x < at$ and $u^{+}$ for $x > at$ is admissible and propagates along the characteristic without change.

### Second-Order Equations and Transmission

**Theorem (second-order jump condition).** Let $P = \sum_{j,k} a_{jk}\partial_j\partial_k + \sum_j b_j\partial_j + c$ be of second order with $a_{jk} = a_{kj}$ and let $u$ be piecewise smooth with $Pu = f$, the source $f$ being continuous across $S$. Then
$$
\sigma_P(n)\,[u]\,\partial_n\delta_S + \Bigl(\sum_{j,k}a_{jk}n_j\,[\partial_k u] + \cdots\Bigr)\delta_S = 0 ,
$$
where the displayed first term is the double layer. If $n$ is non-characteristic, then $[u] = 0$, and the single-layer condition then determines $[\partial_n u]$ in terms of the lower-order coefficients and the source; if $n$ is characteristic, the double-layer coefficient vanishes and the leading condition on $[u]$ disappears.

*Proof.* Apply $\partial_j\partial_k$ to the jump formula and contract with $a_{jk}$. The double layer $\partial_n\delta_S$ arises from the second derivative of the single layer, and its coefficient is $\sum_{jk}a_{jk}n_jn_k[u] = \sigma_P(n)[u]$; the single layer $\delta_S$ collects the first derivatives of $u$ and the lower-order coefficients.
$\square$

The wave operator $\Box = \partial_t^2 - c^2\Delta$ on $\mathbb{R} \times \mathbb{R}^3$ has $\sigma_\Box(\nu) = \nu_t^2 - c^2|\nu|^2$, whose zero set is the light cone $|\nu_t| = c|\nu|$. A surface of constant phase is characteristic exactly when it moves at the speed $c$. On a non-characteristic surface a piecewise solution is continuous, with its normal derivative fixed by the source; on a characteristic surface the continuity is not forced at leading order, and the jumps are the waves that travel on the cone. The elliptic Laplacian has $\sigma_\Delta(\nu) = |\nu|^2 \neq 0$ for every real $\nu \neq 0$, so every surface is non-characteristic and both $[u]$ and $[\partial_n u]$ vanish for a continuous source; the example of the previous section is the flat-coordinate form of this statement.

### The Rankine–Hugoniot Condition

**Theorem (Rankine–Hugoniot).** Let $u$ be a piecewise smooth solution of the conservation law
$$
\partial_t u + \sum_{j=1}^{n} \partial_j f_j(u) = 0,
$$
with flux $f = (f_1,\dots,f_n)$. Let $S$ be a non-characteristic surface of the equation, and write $\nu = (\nu_t,\nu_x)$ for its normal. Then
$$
[u]\,\nu_t + \sum_{j=1}^{n} [f_j(u)]\,\nu_{x_j} = 0 .
$$

*Proof.* The equation is the divergence of the vector field $(u, f(u))$. By the jump formula for the divergence in $\mathbb{R}^{n+1}$, applied in the spacetime variables, the singular part of the divergence is $[u]\nu_t\delta_S + \sum_j[f_j(u)]\nu_{x_j}\delta_S$, and it must vanish.
$\square$

For a plane shock $x = st$ in one space dimension, the normal direction is $(-s,1)$ in $(x,t)$ up to scale, and the condition becomes
$$
[f(u)] = s\,[u], \qquad s = \frac{f(u^{+}) - f(u^{-})}{u^{+} - u^{-}} .
$$
For Burgers' equation $f(u) = u^2/2$ this gives the classical shock speed $s = (u^{+} + u^{-})/2$, verified by the identity $(u^{+2} - u^{-2})/2 = \tfrac12(u^{+} + u^{-})(u^{+} - u^{-})$. The Rankine–Hugoniot condition is the nonlinear replacement for the kernel condition of the linear first-order equation: it is one scalar equation for the jump $[u]$ and the shock speed, and it does not by itself select the physically admissible shock, which is the role of the entropy conditions of *Partial Differential Equations*.

## Traces and Restriction

### The Restriction Problem

The jump formula presupposes that the two traces $u^{\pm}$ exist. For a distribution the restriction to a surface is not automatic: the pairing $\langle u, \psi\,\delta_S\rangle$ need not be defined, because the product of $u$ with $\delta_S$ requires that their wavefront sets be transverse, and the wavefront set of $\delta_S$ is the conormal bundle $N(S)$ of $S$. The restriction $u|_S$ is therefore defined when
$$
\operatorname{WF}(u) \cap N(S) = \varnothing ,
$$
the conormal directions being exactly those in which the delta is singular. This is the criterion of *Microlocal Analysis*, and it is the reason a piecewise smooth function, whose singularities are transversal to $S$, has well-defined traces while a general distribution need not.

### The Trace of a Sobolev Function

For functions in a Sobolev space, the trace exists at lower regularity than pointwise restriction. The trace theorem of *Sobolev Spaces and Weak Solutions* states that for a bounded domain $\Omega$ with Lipschitz boundary there is a bounded linear map
$$
\operatorname{tr} : W^{1,p}(\Omega) \to L^p(\partial\Omega), \qquad \|\operatorname{tr} u\|_{L^p(\partial\Omega)} \le C\,\|u\|_{W^{1,p}(\Omega)},
$$
agreeing with the restriction for continuous functions, with kernel $W^{1,p}_0(\Omega)$; on $H^s$ with $s > 1/2$ the trace is defined and the threshold $s = 1/2$ is sharp. The traces $u^{\pm}$ used in the jump formula are of this kind when the two sides are Sobolev domains: they exist, they are functions on $S$, and the jump formula is then an identity between distributions for every pair of functions whose one-sided traces exist.

### The Distributional Boundary Value

The simplest instance of a trace is the boundary value of a holomorphic function, and it is the one-dimensional model of the whole construction. For $f$ holomorphic on a neighbourhood of the real axis cut along it, the two limits $f^{\pm}(x) = \lim_{\varepsilon\to+0} f(x \pm i\varepsilon)$ are distributions on $\mathbb{R}$, the pair $(f^{+}, f^{-})$ is a piecewise smooth function across the line, and the Sokhotski–Plemelj formula
$$
f^{+} - f^{-} = \text{the density of the jump}, \qquad \frac{1}{x \pm i0} = \mathrm{pv}\frac1x \mp i\pi\delta
$$
expresses the jump of the boundary value through a delta. This is the jump formula for the holomorphic function, and it is the origin of the layer densities used in potential theory.

## Applications

### Transmission Problems

Two media separated by an interface $S$, with the differential equation holding on each side, form a transmission problem: the equation is imposed on the two open regions and the coupling is the jump conditions on $S$. The jump conditions are read from the singular part exactly as above. For a second-order equation they relate the jump of the solution and of its co-normal derivative to the surface data: a single-layer source produces a jump in the normal derivative and a double-layer source a jump in the solution, which is the mechanism of the classical integral equations of *Potential Theory*. For a first-order system they constrain the normal component of the conserved flux and the tangential components of the field, and the interface conditions of the system are the components of the algebraic condition $\sigma_P(n)[u] = 0$ together with the surface conservation law.

### Conservation Laws and Shock Fronts

A conservation law with a nonlinear flux propagates a discontinuity of its solution as a shock front, and the front satisfies the Rankine–Hugoniot condition of the previous section. The distributional treatment is the one given: the shock is a characteristic surface of the quasilinear equation, the jump is admissible, and the amplitude of the jump evolves according to the transport equation obtained at the next layer order. The classical theory of discontinuous solutions, with the entropy selection, is the content of *Partial Differential Equations* and of the hyperbolic systems treated by the method of characteristics; the layer calculus here supplies the equations that the front must satisfy.

### First-Order Systems of Mathematical Physics

The first-order systems of mathematical physics — the Maxwell system, the equations of elasticity, the linearised Euler equations — are all of the form $\sum_j a_j\partial_j u + bu = f$ with a principal symbol that is symmetric or antisymmetric in a suitable inner product, and their jump conditions are the kernel condition $\sigma_P(n)[u] = 0$ together with the surface conservation law. For the Maxwell system the principal symbol in the normal direction is singular on the light cone, and its kernel — one complex dimension, that is two real dimensions — is spanned by the two transverse polarisations of the wave front: the count of polarisations is the dimension of the kernel, and it is computed from the principal symbol alone. The electromagnetic reading of this calculus, with the fields, the sources and the energy balance in the biquaternion formulation, is the subject of the electromagnetism articles of the corpus; the algebra of the layers is that developed here.

## Biquaternion-Valued Distributions

Everything so far is scalar-valued. Two of the corpus's articles that use this calculus — the shock article and the record of the electro-gravimagnetic programme — carry it with **biquaternion-valued** densities, and the algebra-valued theory is the scalar theory applied to each component with the product of the algebra carried along. It is worth one section, because the algebra adds exactly one new ingredient: the normal in the jump formula multiplies a biquaternion gap.

**Test biquaternions and the dual.** A **test biquaternion** is $\Phi = \phi + \Phi_1e_1 + \Phi_2e_2 + \Phi_3e_3$ with each of the four components in $\mathcal{D}(\mathbb{R}^4)$; call the space $\mathcal{B}(M)$, the algebra-valued analogue of $\mathcal{D}$. Its dual $\mathcal{B}'(M)$ is the space of continuous linear functionals on it, with the pairing
$$
(\hat F, \Phi) = (\hat f, \phi) + \sum_{j=1}^{3}(\hat F_j, \Phi_j),
$$
each bracket being the scalar pairing of *Distributions and Fundamental Solutions*. A biquaternion-valued function $F$ defines a functional by integration against it, and a functional that cannot be so written is **singular**. The scalar distributions are the purely scalar elements of $\mathcal{B}'(M)$ and the vector distributions the purely vector ones, so the scalar theory sits inside this one and no statement above is lost.

**Layers with biquaternion density.** The layer of order zero with density $F$ is integration over the surface,
$$
(F\delta_S, \Phi) = \int_S (F, \Phi)\,dS ,
$$
where the integrand is the algebra's scalar product, so the density may be any biquaternion and its four components integrate separately; $F\delta_S$ is the algebra-valued case of the surface delta of the earlier sections. This is the object from which the shock article's front sources and the electro-gravimagnetic record's surface terms are built.

**The jump formula.** For a biquaternion field with a finite gap on a hypersurface $S$, the distributional derivative carries the gap times the scalar normal,
$$
\partial_j \hat F = \partial_j F + n_j\,[F]_S\,\delta_S , \qquad j = ict, x, y, z ,
$$
which is the componentwise jump formula with the same normal $n_j$ multiplying the biquaternion gap $[F]_S$. Because the multiplication is by a scalar, no order of factors is in question, and the identity is the scalar theorem of the section *The Jump Formula* applied to the four components at once.

**Convolution and its two rules.** The **convolution** of two biquaternion-valued functions is the algebra's product with each coefficient convolved,
$$
(A * B) = a * b - \sum_j (A_j * B_j) + \sum_j \left(a * A_j + b * B_j\right)e_j + \sum_{j,k,l}\epsilon_{jkl}\,(A_j * B_k)e_l ,
$$
the first two terms the scalar part and the last two the vector part; it is the quaternion product of the algebra with convolution in each slot, so the same formula reads the convolution of two distributions once each coefficient convolution is taken in the sense of *Distributions and Fundamental Solutions*. Two rules follow. Differentiation passes through the convolution,
$$
\partial_j(A * B) = (\partial_j A) * B = A * (\partial_j B),
$$
and the generalized Fourier transform turns convolution into the algebra's product,
$$
\mathcal{F}[A * B] = \hat A \circ \hat B ,
$$
where the product on the right is the algebra's and the transform is the coefficientwise one of *Biquaternion Continuous Harmonic Analysis*. The second rule is why the algebra-valued transform is entrywise on the sum of two fields and not on their convolution: the product that survives is the non-commutative one. Both rules were checked on random biquaternion sequences with the finite circular convolution, the discrete avatar of the continuous statement. This is the algebra-valued case of the convolution theorem the harmonic-analysis articles develop, and it is the rule the shifted-gradient solution constructions of the electromagnetism articles use when they convolve a scalar potential with a source.

## Summary

A distribution supported on a hypersurface $S$ is built from the surface delta $\delta_S$ and its normal derivatives. The surface delta is defined by integration over $S$ and equals $|\nabla\varphi|\,\delta\circ\varphi$ for a defining function $\varphi$, by the coarea formula; its normal derivative is the double layer, and every distribution supported on $S$ is locally a finite sum of layers $\partial_n^{\,k}(g_k\delta_S)$, the single layer being the term of order zero and the double layer the term of order one.

A piecewise smooth function $u$ has a classical derivative away from $S$ and a jump $[u]$ across it, and the jump formula $\partial_ju = \{\partial_ju\} + [u]n_j\delta_S$ relates them. Its corollaries are the layer decomposition of the gradient, of the divergence, $\mathrm{div}\,A = \{\mathrm{div}\,A\} + (n\cdot[A])\delta_S$, and of the rotor, $\mathrm{rot}\,A = \{\mathrm{rot}\,A\} + n\times[A]\delta_S$, together with the jump of a product $[uv] = u^{+}[v] + [u]v^{-}$. The divergence and the rotor see the normal and the tangential parts of the jump, and the singular parts are the surface charge and the surface current.

The surface operators $\nabla_S$, $\mathrm{div}_S$ and $\mathrm{rot}_S$ are the intrinsic operators of $S$, defined by integration by parts and Stokes' theorem. A tangential simple layer is differentiated into a tangential simple layer, $\mathrm{div}(a\delta_S) = (\mathrm{div}_S\,a)\delta_S$, whereas a normal layer is differentiated into a double layer, $\mathrm{div}(n\delta_S) = \partial_n\delta_S + (\mathrm{div}_S\,n)\delta_S$; this is why surface charges and surface currents are simple layers and double layers arise only from the normal direction or from a second derivative.

The jump conditions of a linear operator are read from the singular part of $Pu$, whose highest layer carries the principal symbol evaluated on the normal. A non-characteristic surface forces the jump to vanish; a characteristic surface admits the jumps in the kernel of $\sigma_P(n)$, and for a second-order operator the double-layer condition is the continuity of the solution. The nonlinear instance is the Rankine–Hugoniot condition $[u]\nu_t + \sum_j[f_j(u)]\nu_{x_j} = 0$ of a conservation law. The traces on which all of this rests exist for Sobolev functions above the threshold $s = 1/2$ and, for a distribution, exactly when its wavefront set avoids the conormal bundle of $S$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S$, $\varphi$, $n$ | hypersurface, defining function with $S = \{\varphi = 0\}$, unit normal $\nabla\varphi/\lvert\nabla\varphi\rvert$ |
| $H$ | Heaviside function, $H(t) = \mathbf{1}_{t>0}$ |
| $\delta_S$ | surface delta, $\langle\delta_S,\psi\rangle = \int_S\psi\,dS$; the single layer of unit density |
| $\partial_n$ | normal derivative, $\partial_n = n\cdot\nabla$ |
| single layer $g\delta_S$ | layer of order $0$, a measure on $S$ with density $g$ |
| double layer $g\partial_n\delta_S$ | layer of order $1$, a normal derivative of a single layer |
| $[u] = u^{+} - u^{-}$ | jump across $S$ |
| $\{\partial^\alpha u\}$ | classical derivative away from $S$ |
| $\nabla_S$, $P = \mathrm{I} - n\otimes n$ | tangential gradient and tangential projection |
| $\mathrm{div}_S$, $\mathrm{rot}_S$ | surface divergence and surface rotor |
| $\sigma_P(n)$ | principal symbol of $P$ evaluated on $n$ |
| characteristic / non-characteristic | $\sigma_P(n)$ not invertible / invertible |
| $N(S)$, $\operatorname{WF}(u)$ | conormal bundle of $S$ and wavefront set of $u$ |
| $\operatorname{tr}$ | trace operator on a Sobolev space |
| $\mathcal{B}(M)$, $\mathcal{B}'(M)$ | test biquaternions (components in $\mathcal{D}$) and their dual, the generalized biquaternions |
| $F\delta_S$, $[F]_S$ | layer with biquaternion density; biquaternion gap across $S$ |

## Further Reading

- Laurent Schwartz, *Théorie des distributions* (Hermann, 1950–51; revised 1966), for distributions of surface type and the calculus of layers.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* (Springer, 2nd ed. 1990), for the wavefront set, the conormal bundle and the criterion for restriction and product.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators III* (Springer, 1985), for the propagation of singularities and the Cauchy problem for hyperbolic operators.
- Herbert Federer, *Geometric Measure Theory* (Springer, 1969), for the coarea formula, rectifiable sets and the measure-theoretic surface.
- David Gilbarg and Neil S. Trudinger, *Elliptic Partial Differential Equations of Second Order* (Springer, 2nd ed. 1983), for the jump relations of single- and double-layer potentials and the transmission problems of potential theory.
- Martin Costabel, "Boundary integral operators on Lipschitz domains: elementary results", *SIAM Journal on Mathematical Analysis* **19** (1988), 613–626, for the layer potentials on a nonsmooth surface and the trace theory they rest on.
- Olga A. Oleinik, "Discontinuous solutions of non-linear differential equations", *Uspekhi Matematicheskikh Nauk* **12** (1957), 3–73, for the classical generalised solutions and the Rankine–Hugoniot conditions.
- Sergei L. Sobolev, *Applications of Functional Analysis in Mathematical Physics* (American Mathematical Society, 1963), for the trace theorem and the boundary values of a Sobolev function.
- Gerald B. Whitham, *Linear and Nonlinear Waves* (Wiley, 1974), for conservation laws, shock fronts and the Rankine–Hugoniot condition.
- L. A. Alexeyeva, "Biquaternions algebra and its applications by solving of some theoretical physics equations", *Clifford Analysis, Clifford Algebras and Their Applications* **7** (2012), 19–39 (arXiv:1302.0523), for the algebra-valued test space and its dual, the layer with biquaternion density, and the biquaternion convolution with its two rules.
