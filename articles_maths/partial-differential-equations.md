
# __Partial Differential Equations__

## Introduction

A partial differential equation relates a function of several variables to its partial derivatives. Its theory is not a single theory but a family of them, and the first fact of the subject is that the equations divide into three types whose solutions behave in qualitatively different ways. A second-order linear equation with a principal part of elliptic type is governed by a maximum principle and its solutions are as smooth as the data; if the type is parabolic, the equation smooths the data and is irreversible in time; if the type is hyperbolic, information travels at a finite speed and the equation preserves the oscillations of the data. The classification is a statement about the symbol of the operator, that is, about the highest-order part read as a polynomial in the frequencies, and it is what makes the subject a theory of types rather than a list of equations.

This article develops the classical theory of the three types, taken one at a time, in the setting of functions on an open subset of $\mathbb{R}^n$ that are as differentiable as the statements require. The Laplace and Poisson equations carry the elliptic theory, the mean value property, the maximum principle, the fundamental solution and the Dirichlet problem with its Poisson kernel; the heat equation carries the parabolic theory, the smoothing of solutions, the maximum principle and the irreversibility of the time direction; the wave equation carries the hyperbolic theory, the d'Alembert and Kirchhoff formulas, finite propagation speed and the conservation of energy. The first-order theory of characteristics is treated first because it is the source of the geometric picture and because it does not depend on the type classification. The article closes with Hadamard's notion of a well-posed problem and his example of an ill-posed one, with separation of variables and the eigenfunction expansion that reduces a boundary-value problem to a Sturm–Liouville problem, and with the fundamental solutions and Green's functions that unify the three types.

No weak formulation is used: every solution here is classical, of class $C^2$ on its domain, and the existence statements are made by explicit formula, by the maximum principle or by the eigenfunction expansion. The extension of the theory to solutions that possess only derivatives in the distributional sense, and the existence theory that it makes possible for data of low regularity, require the Sobolev spaces and are the subject of the companion article of this category on Sobolev spaces and weak solutions; where the classical theory reaches its limit, the reader is referred there. The ordinary theory of *Ordinary Differential Equations* supplies the Sturm–Liouville expansion used in separation of variables, and the integration theory of *Measure Theory and Integration* supplies the surface and volume integrals.

## First-Order Equations and Characteristics

**Definition.** A **first-order partial differential equation** in the unknown $u : \Omega \to \mathbb{R}$, $\Omega \subseteq \mathbb{R}^n$ open, is an equation

$$
F\bigl(x, u(x), \nabla u(x)\bigr) = 0 ,
$$

and it is **quasilinear** if it is linear in $\nabla u$ with coefficients depending on $x$ and $u$,

$$
\sum_{i=1}^n a_i(x,u)\,\partial_i u = c(x,u),
$$

and **linear** if the coefficients depend on $x$ alone. The **characteristic vector field** of a quasilinear equation is $a(x,u) = (a_1,\dots,a_n)$, and the **characteristic equations** are the ordinary system

$$
\dot x = a(x,u), \qquad \dot u = c(x,u) .
$$

**Theorem (method of characteristics).** Let $u$ be a $C^1$ solution of the quasilinear equation and let $x(t)$ be a solution curve of $\dot x = a(x,u(x(t)))$; then along the curve $u$ solves $\dot u = c$, and the value of $u$ is constant along the curve when $c=0$. Hence a solution is determined by its values on a hypersurface that is transverse to the characteristic field, and the solution is constant along each characteristic curve.

*Proof.* Along $t \mapsto u(x(t))$ one has $\frac{d}{dt}u = \sum_i\partial_iu\,\dot x_i = \sum_ia_i\partial_iu = c$ by the equation; the case $c=0$ gives constancy, and the reduction to the prescribed data on a transversal hypersurface is the statement that the map from data to characteristic curve is invertible when the transversality holds. $\square$

**Example (a linear transport equation).** For $u_t + b\,u_x = 0$ with $b$ constant, the characteristics are the lines $x = x_0 + bt$, and the solution with datum $u(x,0) = f(x)$ is $u(x,t) = f(x-bt)$: the initial profile is translated at speed $b$. The equation is hyperbolic and the solution exists and is unique for all time, with no smoothing and no decay.

**Example (a conservation law).** For $u_t + u\,u_x = 0$ with datum $u(x,0)=f(x)$, the characteristics are the lines $x = f(x_0)t + x_0$, which cross when $f' < 0$; the classical solution then ceases to exist at the first crossing time $t_* = -1/\inf f'$, and beyond it the equation must be interpreted in a weaker sense. This is the simplest instance of the formation of a singularity in a hyperbolic equation.

**Definition.** A **complete integral** of a first-order equation is a family $u(x;c)$ of solutions depending on $n$ parameters $c$ such that $\det(\partial^2 u/\partial x_i\partial c_j) \neq 0$. The **envelope** of a one-parameter subfamily is obtained by eliminating the parameter between $u = u(x;c)$ and $\partial_cu(x;c)=0$, and it is again a solution; the general solution is assembled from the data and the characteristics, or from complete integrals and their envelopes.

## Classification of Second-Order Equations

### The Principal Symbol

**Definition.** A **second-order linear differential operator** on $\Omega \subseteq \mathbb{R}^n$ is

$$
Lu = \sum_{i,j=1}^{n}a_{ij}(x)\,\partial_i\partial_ju + \sum_{i=1}^{n}b_i(x)\,\partial_iu + c(x)u ,
$$

with $a_{ij} = a_{ji}$; its **principal part** is the sum with the second derivatives, and its **principal symbol** is the quadratic form

$$
\sigma(x,\xi) = \sum_{i,j=1}^n a_{ij}(x)\,\xi_i\xi_j , \qquad \xi \in \mathbb{R}^n .
$$

The operator is **elliptic** at $x$ if $\sigma(x,\xi) \neq 0$ for every $\xi \neq 0$; it is **hyperbolic** at $x$ if $\sigma$ is nondegenerate with signature $(1,n-1)$; and it is **parabolic** at $x$ if $\sigma$ is degenerate of rank $n-1$ with the rank drop corresponding to a distinguished direction. For $n=2$ the classification is read from the discriminant.

**Theorem (two-dimensional classification).** Let $a_{11}u_{xx} + 2a_{12}u_{xy} + a_{22}u_{yy} + \cdots = 0$ and put $\Delta = a_{12}^2 - a_{11}a_{22}$. Then the equation is elliptic if $\Delta<0$, parabolic if $\Delta=0$, hyperbolic if $\Delta>0$, and in each case a $C^2$ change of variables brings the principal part to the canonical form

$$
u_{\xi\xi} + u_{\eta\eta}, \qquad u_{\xi\xi}, \qquad u_{\xi\xi} - u_{\eta\eta}
$$

respectively.

*Proof.* Writing $\xi = \xi(x,y)$ and $\eta=\eta(x,y)$ transforms the coefficients by the chain rule, and the new principal part is the old form evaluated on $(\xi_x,\xi_y)$ and $(\eta_x,\eta_y)$; the equation for the level curves of $\xi,\eta$ is the ordinary differential equation $a_{11}(dy)^2 - 2a_{12}dx\,dy + a_{22}(dx)^2=0$, whose characteristic polynomial has discriminant $\Delta$ and hence two, one or no real families of solutions, giving the hyperbolic, parabolic and elliptic cases. A second change diagonalises the resulting form. $\square$

**Remark.** The classification is invariant under a change of independent variables, because the transformation acts on $\xi$ by an invertible linear map and therefore preserves the signature of the symbol. It is a pointwise classification, so an equation can change type across a curve, as the Tricomi equation $y\,u_{xx} + u_{yy} = 0$ does across $y=0$.

## The Laplace and Poisson Equations

### Harmonic Functions and the Mean Value Property

**Definition.** The **Laplacian** on $\mathbb{R}^n$ is $\Delta = \sum_i\partial_i^2$. A $C^2$ function $u$ with $\Delta u = 0$ on an open set is **harmonic** there; the equation $\Delta u = f$ is the **Poisson equation**, and the equation $\Delta u = 0$ the **Laplace equation**. The **Dirichlet problem** on a bounded domain $\Omega$ with boundary datum $g$ asks for a harmonic $u$ on $\Omega$ with $u|_{\partial\Omega}=g$.

**Theorem (mean value property).** If $u$ is harmonic on an open set containing the closed ball $\overline{B}(x,r)$, then

$$
u(x) = \frac{1}{\omega_{n-1}r^{n-1}}\int_{\partial B(x,r)}u\,dS = \frac{n}{\omega_{n-1}r^{n}}\int_{B(x,r)}u\,dy ,
$$

where $\omega_{n-1}$ is the area of the unit sphere in $\mathbb{R}^n$. Conversely, a continuous function with the mean value property is harmonic.

*Proof.* Let $\varphi(r) = \frac{1}{\omega_{n-1}r^{n-1}}\int_{\partial B(x,r)}u\,dS$. Differentiating with respect to $r$ and applying the divergence theorem gives $\varphi'(r) = \frac{1}{\omega_{n-1}r^{n-1}}\int_{B(x,r)}\Delta u\,dy = 0$, so $\varphi$ is constant, and its limit as $r\to0$ is $u(x)$ by continuity; this is the surface form, and integrating in $r$ gives the volume form. Conversely, a continuous function with the mean value property satisfies $\Delta u = 0$ in the distributional sense, and by elliptic regularity, established below by the representation formula, it is harmonic. $\square$

**Theorem (maximum principle).** A harmonic function on a connected open set attains its maximum and minimum only on the boundary, in the sense that if $\Omega$ is connected and bounded with $u$ continuous on $\overline\Omega$ and harmonic on $\Omega$, then $\sup_\Omega u = \sup_{\partial\Omega}u$ and $\inf_\Omega u = \inf_{\partial\Omega}u$; if the extremum is attained at an interior point the function is constant.

*Proof.* If $u$ attained a strict interior maximum at $x_0$, then for small $r$ the mean value property would give $u(x_0)\le \max_{\partial B(x_0,r)}u$ with equality only if $u$ is constant on the sphere; iterating along a chain of balls from $x_0$ to any other point of $\Omega$ shows $u$ constant, contradicting the strict maximum unless $u$ is constant. Applying this to $-u$ gives the minimum. $\square$

**Corollary (uniqueness and stability of the Dirichlet problem).** The Dirichlet problem has at most one solution, and its solution depends monotonically and uniformly on the boundary datum: if $u_1,u_2$ solve it with data $g_1,g_2$, then $\|u_1-u_2\|_\infty \le \|g_1-g_2\|_\infty$.

*Proof.* The difference $w=u_1-u_2$ is harmonic with boundary datum $g_1-g_2$, so by the maximum principle $\sup_\Omega|w| \le \sup_{\partial\Omega}|g_1-g_2|$. $\square$

### The Fundamental Solution and Green's Function

**Definition.** A **fundamental solution** of the Laplacian on $\mathbb{R}^n$ is a function $\Phi$ with $\Delta\Phi = \delta_0$ in the distributional sense; for $n \ge 3$, and for $n=2$ with a logarithm,

$$
\Phi(x) = \frac{1}{n(n-2)\omega_{n-1}}\frac{1}{|x|^{n-2}} \quad (n \ge 3), \qquad \Phi(x) = \frac{1}{2\pi}\log|x| \quad (n=2).
$$

**Theorem (Green's representation formula).** For $u \in C^2(\overline\Omega)$ and for each $x \in \Omega$, the second Green identity in the form

$$
u(x) = \int_{\partial\Omega}\Bigl(u(y)\,\frac{\partial\Phi}{\partial\nu_y}(x-y) - \Phi(x-y)\,\frac{\partial u}{\partial\nu}(y)\Bigr)dS(y) + \int_\Omega \Phi(x-y)\,\Delta u(y)\,dy
$$

expresses $u$ in terms of its boundary values, its normal derivative and its Laplacian. If $u$ is harmonic and $H(x,y)$ is the **harmonic corrector** solving the Dirichlet problem $\Delta_yH=0$ with $H(x,y) = \Phi(x-y)$ for $y \in \partial\Omega$, then with the **Green's function** $G(x,y) = \Phi(x-y) - H(x,y)$,

$$
u(x) = -\int_{\partial\Omega}u(y)\,\frac{\partial G}{\partial\nu_y}(x,y)\,dS(y),
$$

so a harmonic function is determined by its boundary values alone.

*Proof.* The second Green identity applied to $u$ and $\Phi(x-\cdot)$ on $\Omega \setminus B(x,\varepsilon)$, together with the behaviour of $\Phi$ at $x$ as $\varepsilon\to0$, gives the representation formula; the corrector has the same boundary values as $\Phi(x-\cdot)$ and is harmonic, so subtracting it removes the normal-derivative term and gives the Green formula. $\square$

**Theorem (Poisson kernel for the ball).** For the ball $B(0,R)$ in $\mathbb{R}^n$,

$$
u(x) = \frac{R^2-|x|^2}{\omega_{n-1}R}\int_{\partial B(0,R)}\frac{g(y)}{|x-y|^n}\,dS(y)
$$

is the harmonic function in $B(0,R)$ with continuous boundary values $g$, and for $n=2$ this is the classical Poisson formula.

*Proof.* The Poisson kernel $P(x,y) = \frac{R^2-|x|^2}{\omega_{n-1}R|x-y|^n}$ is obtained from the Green function of the ball, itself computed by the method of images for the sphere; the kernel is positive with total integral one, so the formula is the boundary-value problem solved by convolution with an approximate identity, and the limit $x\to\partial B$ is $g$. $\square$

**Example.** For a ball in $\mathbb{R}^2$ the value at the centre is the mean of the boundary values, $u(0) = \frac{1}{2\pi R}\int_{\partial B}g\,dS$, which is the mean value property; the formula is exact and follows from the kernel at $x=0$.

## The Heat Equation

### The Fundamental Solution and Smoothing

**Definition.** For $t>0$ the **heat kernel** on $\mathbb{R}^n$ is

$$
K_t(x) = \frac{1}{(4\pi t)^{n/2}}\exp\Bigl(-\frac{|x|^2}{4t}\Bigr),
$$

and the **heat equation** is $u_t = \Delta u$; the **Cauchy problem** asks for $u \in C^2(\mathbb{R}^n\times(0,\infty)) \cap C(\mathbb{R}^n\times[0,\infty))$ with $u(x,0)=f(x)$.

**Theorem (solution by convolution).** If $f$ is continuous and bounded, then

$$
u(x,t) = (K_t * f)(x) = \int_{\mathbb{R}^n}K_t(x-y)f(y)\,dy
$$

solves the Cauchy problem, and $\|u(\cdot,t)\|_\infty \le \|f\|_\infty$ with $u(\cdot,t)\to f$ uniformly on compact sets as $t\to0^+$.

*Proof.* The kernel solves $K_t = \Delta K$ by direct differentiation, and differentiating under the integral gives $u_t = \Delta u$; the kernel is positive with total integral one, so it is an approximate identity as $t\to0^+$, giving the stated convergence and the sup bound. $\square$

**Theorem (smoothing).** If $f$ is merely bounded and continuous, then $u(\cdot,t)$ is of class $C^\infty$ for every $t>0$, and all its derivatives are bounded on $\mathbb{R}^n\times[\varepsilon,\infty)$ for every $\varepsilon>0$. In particular no singularity of $f$ propagates, and the solution is analytic in $x$ for $t>0$.

*Proof.* The kernel $K_t(x-y)$ is $C^\infty$ in $(x,t)$ for $t>0$, and every derivative is integrable against the bounded $f$, so differentiation under the integral is legitimate. $\square$

**Theorem (maximum principle).** If $u$ solves $u_t=\Delta u$ in a bounded cylinder $\Omega\times(0,T)$ and is continuous on its closure, then

$$
\max_{\overline\Omega\times[0,T]}u = \max\Bigl(\max_{\partial\Omega\times[0,T]}u,\ \max_{\overline\Omega\times\{0\}}u\Bigr),
$$

with the same statement for the minimum; consequently the solution is unique and depends monotonically on its data.

*Proof.* If $u$ attained an interior maximum at $(x_0,t_0)$ with $t_0>0$, then $u_t(x_0,t_0)\ge0$ and $\Delta u(x_0,t_0)\le0$, so $u_t-\Delta u \ge 0$ there; to exclude equality one applies the argument to $u-\varepsilon t$ and lets $\varepsilon\to0$. The uniqueness follows by applying the principle to the difference of two solutions. $\square$

**Theorem (irreversibility).** The backward problem $u_t = \Delta u$ for $t<0$ with datum at $t=0$ is not well posed: the solution operator $K_t$ for $t>0$ has no bounded inverse on $L^2(\mathbb{R}^n)$, and its inverse amplifies high frequencies by the factor $e^{|\xi|^2|t|}$.

*Proof.* The Fourier transform diagonalises the equation, $\hat u(\xi,t) = e^{-|\xi|^2t}\hat f(\xi)$; the multiplier $e^{-|\xi|^2t}$ is bounded for $t>0$ with norm $1$, but for the backward direction the multiplier is $e^{|\xi|^2|t|}$, which is unbounded, so arbitrarily small high-frequency data can be amplified beyond any bound. $\square$

## The Wave Equation

### d'Alembert's Formula and Finite Propagation

**Definition.** The **wave equation** with speed $c>0$ is $u_{tt} = c^2\Delta u$; the Cauchy problem asks for $u(x,0)=f(x)$ and $u_t(x,0)=g(x)$.

**Theorem (d'Alembert, $n=1$).** The solution of the Cauchy problem on $\mathbb{R}$ with $f \in C^2$ and $g \in C^1$ is

$$
u(x,t) = \frac{f(x-ct)+f(x+ct)}{2} + \frac{1}{2c}\int_{x-ct}^{x+ct}g(s)\,ds .
$$

*Proof.* Change to characteristic coordinates $\xi = x-ct$, $\eta = x+ct$, in which the equation becomes $u_{\xi\eta}=0$ with general solution $u = F(\xi)+G(\eta)$; the initial conditions determine $F$ and $G$ and give the displayed formula. $\square$

**Theorem (finite propagation speed).** If $u$ solves the wave equation in $\mathbb{R}^n\times(0,\infty)$ and $u$ and $u_t$ vanish on the ball $B(x_0,r)$ at $t=0$, then $u$ vanishes on the cone $\{(x,t) : |x-x_0|\le r-ct,\ 0\le t\le r/c\}$. Consequently the value $u(x,t)$ depends only on the data in the ball $B(x,ct)$.

*Proof.* The energy

$$
E(t) = \frac12\int_{B(x_0,r-ct)}\Bigl(u_t^2 + c^2|\nabla u|^2\Bigr)dx
$$

satisfies $E'(t) \le 0$, because differentiating in $t$ and applying the divergence theorem gives the flux across the boundary sphere, which is nonpositive by the sign of the cone; since $E(0)=0$ the energy vanishes and the solution is constant on the cone, hence zero. $\square$

**Theorem (Kirchhoff, $n=3$).** For $f \in C^3$ and $g \in C^2$ on $\mathbb{R}^3$ the solution is

$$
u(x,t) = \frac{1}{4\pi c^2 t}\int_{\partial B(x,ct)}g\,dS + \frac{\partial}{\partial t}\Bigl(\frac{1}{4\pi c^2t}\int_{\partial B(x,ct)}f\,dS\Bigr),
$$

a formula involving only the data on the *sphere* of radius $ct$, which is Huygens' principle: in three dimensions a disturbance is transmitted as a sharp wave front and leaves no tail. In two dimensions the corresponding formula integrates over the *disc*, so a tail remains; the dimension is visible in the solution.

*Proof.* Quoted as standard (the Kirchhoff and Poisson formulas). The sphere appears because $n=3$ is odd and the fundamental solution of the wave operator is a distribution supported on the light cone; the disc appears for the descent to $n=2$ by the method of descent, in which the data are extended independently of a third coordinate. $\square$

## Well-Posedness and Separation of Variables

### Hadamard's Notion

**Definition.** A problem consisting of a differential equation together with auxiliary data is **well posed** in the sense of Hadamard if a solution exists, the solution is unique, and the solution depends continuously on the data in a topology fixed in advance. A problem that fails any one of the three is **ill posed**.

**Theorem (Hadamard's example).** The Cauchy problem for the Laplace equation $\Delta u = 0$ in the upper half-plane with $u(x,0)=0$ and $u_y(x,0)=\frac1n\sin(nx)$ has the solution

$$
u_n(x,y) = \frac{1}{n^2}\sin(nx)\sinh(ny),
$$

which is small in $C^1$ on the real axis and arbitrarily large at any fixed $y>0$ as $n\to\infty$. Hence the Cauchy problem for an elliptic equation is ill posed.

*Proof.* Both $u_n$ and its derivative at $y=0$ are $O(1/n)$ uniformly in $x$, while $\sinh(ny)$ grows exponentially at fixed $y$; so the data converge to zero in $C^1$ whereas the solutions do not converge to zero pointwise away from the axis. $\square$

The example explains the classification in terms of the auxiliary data a type can accept: an elliptic equation needs boundary data on the whole boundary and is well posed as a Dirichlet problem; a parabolic equation needs data at one time and is well posed forward in time; a hyperbolic equation needs Cauchy data and is well posed for all time, with the oscillations of the data preserved rather than damped.

### Separation of Variables

**Theorem (eigenfunction expansion).** Let $\Omega$ be a bounded domain with smooth boundary, and let $(\lambda_k,\varphi_k)$ be the eigenvalues and orthonormal eigenfunctions of $-\Delta$ with homogeneous Dirichlet boundary conditions, so that

$$
-\Delta\varphi_k = \lambda_k\varphi_k \quad \text{in } \Omega, \qquad \varphi_k = 0 \quad \text{on } \partial\Omega .
$$

Then the eigenvalues are positive with $\lambda_k \to \infty$ and the $\varphi_k$ form an orthonormal basis of $L^2(\Omega)$. The solution of the heat equation with datum $f = \sum_kc_k\varphi_k$ is

$$
u(x,t) = \sum_k c_k e^{-\lambda_kt}\varphi_k(x),
$$

and the solution of the wave equation with $u(\cdot,0)=f$, $u_t(\cdot,0)=g$ is

$$
u(x,t) = \sum_k\Bigl(c_k\cos(c\sqrt{\lambda_k}\,t) + d_k\,\frac{\sin(c\sqrt{\lambda_k}\,t)}{c\sqrt{\lambda_k}}\Bigr)\varphi_k(x),
$$

with $d_k$ the coefficients of $g$, and $u_t$ obtained by termwise differentiation.

*Proof.* The eigenfunction problem is a Sturm–Liouville problem after separation of variables, and its spectral theory is that of *Ordinary Differential Equations*: the eigenvalues are positive because $-\Delta$ is a positive operator, they tend to infinity by the compactness of the resolvent, and the eigenfunctions are complete. Substituting the series into the equation and using the orthonormality of the $\varphi_k$ decouples the equation into ordinary equations in $t$ for each coefficient, solved by the displayed exponentials and trigonometric functions; the convergence of the series to a classical solution follows from the decay of the coefficients once the data are smooth enough. $\square$

**Example (the vibrating string).** On $\Omega = (0,L)$ the eigenvalues are $\lambda_k = k^2\pi^2/L^2$ with $\varphi_k(x) = \sqrt{2/L}\sin(k\pi x/L)$; the solution of the wave equation is a superposition of standing waves with frequencies $ck\pi/L$, and the slowest mode dominates. The exhibited series is the Fourier sine series, and the general theory of such expansions on an interval is the classical theory of the Sturm–Liouville problem of *Ordinary Differential Equations*.

## Summary

A second-order linear partial differential equation is classified at each point by its principal symbol $\sigma(x,\xi) = \sum a_{ij}\xi_i\xi_j$ as elliptic, parabolic or hyperbolic according to the definiteness, degeneracy or hyperbolicity of that quadratic form, and in two variables by the sign of the discriminant $a_{12}^2-a_{11}a_{22}$. A quasilinear first-order equation is solved by the method of characteristics, its solution being constant along the characteristic curves; the characteristics may cross, and the classical solution then ceases to exist.

The Laplace equation is the model elliptic equation. Its solutions are characterised by the mean value property, they obey the maximum principle, so the Dirichlet problem has at most one solution and depends uniformly on its data, and they are represented by the fundamental solution $\Phi$ and the Green function $G$; on a ball the representation is the Poisson kernel. The heat equation is the model parabolic equation: its Cauchy problem is solved by convolution with the heat kernel, its solutions are $C^\infty$ for positive time whatever the regularity of the data, the maximum principle gives uniqueness in a cylinder, and the backward problem is ill posed because the inverse multiplier $e^{|\xi|^2|t|}$ amplifies high frequencies without bound. The wave equation is the model hyperbolic equation: its one-dimensional solution is d'Alembert's formula, its energy is conserved and confined to the cone of influence, so information travels at speed $c$, and in three dimensions the Kirchhoff formula is supported on the sphere, which is Huygens' principle.

Hadamard's notion of a well-posed problem — existence, uniqueness and continuous dependence — separates the types: the Dirichlet problem is well posed for the elliptic equation, the Cauchy problem forward in time for the parabolic equation, and the Cauchy problem for all time for the hyperbolic equation, whereas the Cauchy problem for an elliptic equation is ill posed, as Hadamard's example shows. Separation of variables reduces a boundary-value problem on a product domain to the Sturm–Liouville eigenfunction expansion of the transversal operator, and the resulting series solves the heat and wave equations mode by mode. The three model equations are unified by their fundamental solutions, which are the kernels of the inverse operators, and by the Green functions that incorporate the boundary conditions; the distributional treatment of the fundamental solutions, and the existence theory for data of low regularity, belong to the companion articles *Distributions and Fundamental Solutions* .

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Omega \subseteq \mathbb{R}^n$ | Open domain; $x = (x_1,\dots,x_n)$ its variable |
| $\partial_i$, $\nabla$, $\Delta$ | Partial derivative, gradient, Laplacian |
| $\sigma(x,\xi)$ | Principal symbol of a second-order operator |
| $\Delta = a_{12}^2-a_{11}a_{22}$ | Discriminant classifying a planar equation |
| elliptic, parabolic, hyperbolic | Types of the principal symbol |
| $\Phi$ | Fundamental solution of the Laplacian |
| $G(x,y)$, $H(x,y)$ | Green function and harmonic corrector |
| $P(x,y)$ | Poisson kernel of a ball |
| $K_t(x)$ | Heat kernel, $(4\pi t)^{-n/2}e^{-|x|^2/4t}$ |
| $c$ | Wave speed |
| $E(t)$ | Energy of a solution of the wave equation |
| characteristic curves | Integral curves of $\dot x = a(x,u)$ |
| complete integral | Family of solutions with $n$ parameters |
| well posed (Hadamard) | Existence, uniqueness and continuous dependence on the data |
| $\lambda_k$, $\varphi_k$ | Dirichlet eigenvalues and eigenfunctions of $-\Delta$ |



## Further Reading

- Lawrence C. Evans, *Partial Differential Equations* (American Mathematical Society, 2nd ed. 2010), for the classification, the three model equations and the representation formulas.
- Fritz John, *Partial Differential Equations* (Springer, 4th ed. 1991), for the classical theory, the method of characteristics and Hadamard's example.
- David Gilbarg and Neil S. Trudinger, *Elliptic Partial Differential Equations of Second Order* (Springer, 2nd ed. 1983), for the maximum principle and the Dirichlet problem.
- Gerald B. Folland, *Introduction to Partial Differential Equations* (Princeton University Press, 2nd ed. 1995), for the distributional treatment of fundamental solutions.
- Peter D. Lax, *Hyperbolic Partial Differential Equations* (Courant Institute, 2006), for finite propagation speed and Huygens' principle.
- Murray H. Protter and Hans F. Weinberger, *Maximum Principles in Differential Equations* (Springer, 1984), for the maximum principle in all three types.
- Richard Courant and David Hilbert, *Methods of Mathematical Physics II* (Interscience, 1962), for the classical representation formulas and the method of descent.
- Sigurdur Helgason, *The Radon Transform* (Birkhäuser, 2nd ed. 1999), for the geometric forms of the wave representation.
