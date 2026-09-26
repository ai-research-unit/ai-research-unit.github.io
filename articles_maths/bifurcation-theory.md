
# __Bifurcation Theory__

## Introduction

A **bifurcation** is a change in the topological type of a dynamical system as a parameter varies: one is given a family $\dot x=f(x,\mu)$ of vector fields, or $x\mapsto f(x,\mu)$ of diffeomorphisms, depending on a parameter $\mu$ in a parameter space $\Lambda$, and the parameter values at which the family fails to be locally conjugate to itself for nearby values form the **bifurcation set**; the classification of the possible changes, and the reduction of an arbitrary family near a bifurcation to a polynomial **normal form**, are the content of bifurcation theory. The theory is local where the change occurs at a fixed point or a periodic orbit — there the centre manifold theorem reduces the problem to the directions in which the derivative has neutral eigenvalues, and the Poincaré–Dulac theorem removes the non-resonant terms of the Taylor expansion — and global where a change of connectivity occurs, as in a homoclinic orbit closing onto a saddle. The two ingredients of a bifurcation are therefore a **non-hyperbolicity** of the linearisation, which is the source of the qualitative change, and a **degeneracy** of the nonlinear terms, which decides which of the finitely many models the family realises; the models of codimension one are the saddle-node, the transcritical, the pitchfork and the Hopf bifurcations of an equilibrium, with the fold, the flip and the Neimark–Sacker bifurcations of a fixed point of a map, and beyond them the codimension-two unfoldings and the global bifurcations.

The article begins with the definitions: parameter families, the equivalence of families by parameter-respecting conjugacies, the notion of codimension, and the reduction of a local bifurcation to the centre manifold. It then states the **centre manifold theorem** and the **Poincaré–Dulac normal form theorem** with its resonance condition, and it treats the codimension-one bifurcations of an equilibrium: the **saddle-node** (fold), the **transcritical** and the **pitchfork**, classified by the coefficients of the Taylor expansion in the theorem of Sotomayor, and the **Hopf** bifurcation, with the Andronov–Hopf theorem, the first Lyapunov coefficient and the birth of the limit cycle. The **versal unfoldings** are defined and the miniversal unfolding of each singularity is given, with the Poincaré–Birkhoff normal form for the resonant Hamiltonian case and the Siegel linearisation theorem for the formal case. The article continues with the codimension-two theory — the **Takens–Bogdanov** normal form with the double eigenvalue zero and the homoclinic loop, and the cusp and the other elementary catastrophes — the classification of the codimension-one bifurcations of maps, and the **period doubling** cascade with the universality of Feigenbaum and the renormalisation operator that explains it. It closes with the global bifurcations, the homoclinic and heteroclinic loops and the theorem of Shilnikov, and with the worked example of the logistic family.

The parameter families and their equivalence, the centre manifolds, the normal forms and the genericity are those of *Smooth Dynamical Systems*; the hyperbolicity, the stable and unstable manifolds and the shadowing used in the reduction are those of *Hyperbolic Dynamics and Anosov Systems*; the recurrence and the notion of structural stability are those of *Topological Dynamics*. The existence theory and the linearisation of the differential equations are those of *Ordinary Differential Equations*; the Hamiltonian and Lagrangian structures underlying the Birkhoff normal form are those of *Lagrangian and Hamiltonian Systems*. The chaotic regimes reached after the period-doubling cascade and the arithmetic families lie outside this article.

No physics is invoked.

## Families, Equivalence and Codimension

### Parameter Families

**Definition.** A **parameterised family** of vector fields on a manifold $M$ is a smooth map $f:M\times\Lambda\to TM$, $(x,\mu)\mapsto f(x,\mu) \in T_xM$, with $\Lambda$ an open subset of $\mathbb{R}^k$, the **parameter space**; the family is studied through the solutions of $\dot x=f(x,\mu)$, viewed as a family of flows $\varphi^\mu_t$. A **family of maps** is a smooth map $f:M\times\Lambda\to M$ with $f_\mu=f(\cdot,\mu)$ a diffeomorphism for each $\mu$. A parameter value $\mu_0$ at which the qualitative behaviour changes is a **bifurcation value**, and the set of such values is the **bifurcation set** $\Sigma \subseteq\Lambda$; a **local bifurcation** is one at a fixed point or a periodic orbit, a **global bifurcation** one at which the invariant manifolds of two hyperbolic objects cease to meet transversely.

**Definition.** Two families $f_{\mu}$ and $g_{\nu}$, defined on neighbourhoods of $(x_0,\mu_0)$ and $(y_0,\nu_0)$, are **locally equivalent at $C^r$** if there are a homeomorphism $\Phi$ of the form $\Phi(x,\mu)=(H(x,\mu),\phi(\mu))$, with $\phi$ a homeomorphism of the parameter spaces and $H(\cdot,\mu)$ a homeomorphism for each $\mu$, such that $\Phi$ carries the solutions of $\dot x=f(x,\mu)$ to those of $\dot y=g(y,\phi(\mu))$; for $r \ge1$ the requirement is that $H(\cdot,\mu)$ be a $C^r$ diffeomorphism, and there is a version with a reparametrisation of time. The **bifurcation set is invariant** under equivalence, and the theory seeks the normal forms to which families are equivalent.

**Definition.** The **codimension** of a bifurcation is the smallest number of parameters such that the singularity occurs in a family transversal to the corresponding stratum of the space of the objects; equivalently, the codimension is the number of scalar conditions that the coefficients of the family must satisfy at $\mu_0$ beyond the condition of the singularity itself, and each codimension-one bifurcation is the generic (open and dense) transition in a one-parameter family, while codimension-two bifurcations organise the one-parameter transitions in a two-parameter family.

### The Centre Manifold Reduction

**Theorem (centre manifold theorem).** Let $f$ be a family of vector fields with $f(x_0,\mu_0)=0$, and let $A=D_xf(x_0,\mu_0)$ have the splitting of $\mathbb{R}^n$ into the parts with eigenvalues of negative, zero and positive real part. Then for each $\mu$ near $\mu_0$ there is a **centre manifold** $W^c_{\mathrm{loc}}(\mu)$: a $C^r$ invariant manifold tangent at the bifurcating point to the centre subspace $E^c$ of $A$, of dimension $\dim E^c$; it is not in general unique, but the germ of the restriction of the flow to it is unique up to a smooth change of coordinates, and the flow near the bifurcating point is topologically the product of the flow on $W^c_{\mathrm{loc}}$ with the contraction and expansion in the stable and unstable directions. Consequently the local bifurcation at the point is exhibited by the restricted family on $W^c$, which is finite-dimensional and, being tangent to $E^c$, has a linearisation with only neutral eigenvalues; the number of parameters needed to unfold it is the codimension, and the resulting models are the normal forms of the following sections.

*Proof (sketch).* The centre manifold is obtained as the graph over $E^c$ of a function that solves the invariance equation $h'(x)\,f^c(x,h(x))=f^s(x,h(x))$ to the order required; the existence and the finite smoothness follow from a fixed point argument in the space of $C^r$ functions over a small neighbourhood. The non-uniqueness is real (the manifolds differ in the higher-order terms), but the Taylor expansion up to any finite order is unique, and the topological form of the flow is proved from the uniqueness of the germ and the hyperbolicity of the transversal directions, by the standard arguments of Hadamard–Perron and Hartman–Grobman. $\square$

### Normal Forms

**Definition.** Let $f$ have a fixed point at the origin with linearisation $A$. A monomial vector field $P_\alpha(x)=x^\alpha e_i$ (in a coordinate basis of eigenvectors) is **resonant** with $A$ if $\lambda_i=\sum_j\alpha_j\lambda_j$; the **resonance condition** is the linear equation $\langle\alpha,\lambda\rangle=\lambda_i$ on the exponents.

**Theorem (Poincaré–Dulac normal form).** Let $f$ be a smooth (or formal) vector field vanishing at the origin with linearisation $A$. Then there is a formal change of coordinates that transforms $f$ into the **normal form**

$$
\dot x=Ax+g(x), \qquad g=\sum_{\alpha \text{ resonant}}g_\alpha x^\alpha ,
$$

a vector field whose nonlinear part consists only of the resonant monomials; if a finite number of monomials is prescribed the transformation can be taken polynomial, and the normal form is unique up to the transformations that commute with the resonant structure.

*Proof (sketch).* One eliminates the non-resonant monomials in increasing order of degree by the change $y=x+O(\deg d)$ with the appropriate homogeneous polynomial, whose homological operator $\operatorname{ad}_A(h)=Dh\cdot Ax-Ah(x)$ has spectrum $\langle\alpha,\lambda\rangle-\lambda_i$ on the monomial $x^\alpha e_i$; the operator is invertible exactly when the monomial is non-resonant, so the elimination succeeds precisely on the complement of the resonances. $\square$

**Theorem (Poincaré–Birkhoff normal form).** For a vector field with a non-degenerate quadratic first integral, in particular for a Hamiltonian vector field with a non-degenerate quadratic term at an equilibrium, the normal form at a resonance of the form $\lambda_i+\lambda_j=\lambda_k+\lambda_l$ can be chosen as a function of the quadratic invariants, the **Birkhoff normal form**; for a Hamiltonian with frequencies $\omega_1,\dots,\omega_n$ satisfying the non-resonance condition $\langle m,\omega\rangle\neq0$ for $0<|m|\le K$ the normal form up to order $K$ is integrable, and the system is locally a perturbation of an integrable one. If the frequencies satisfy a Diophantine condition, the formal series converges and the equilibrium is **Siegel linearisable**; the nonlinearisable (resonant) case has the Birkhoff normal form as its classification. The Hamiltonian versions are treated in *Lagrangian and Hamiltonian Systems*.

## Codimension-One Bifurcations of Equilibria

### Saddle-Node, Transcritical and Pitchfork

**Theorem (Sotomayor; classification).** Let $f:M\times\Lambda\to TM$ be a one-parameter family with $f(x_0,\mu_0)=0$ and with $A=D_xf(x_0,\mu_0)$ having the simple eigenvalue $0$ and no other neutral eigenvalue. Then:

(i) **(saddle-node)** if $\frac{\partial f}{\partial\mu}(x_0,\mu_0)\neq0$ and $\frac{\partial^2f}{\partial x^2}(x_0,\mu_0)\neq0$, the family is equivalent near $(x_0,\mu_0)$ to the normal form

$$
\dot x=\mu-x^2,
$$

in which two equilibria exist for $\mu>0$, collide at $\mu=0$ and disappear for $\mu<0$;

(ii) **(transcritical)** if $\frac{\partial f}{\partial\mu}(x_0,\mu_0)=0$ and $\frac{\partial^2f}{\partial x\partial\mu}(x_0,\mu_0)\neq0$ and $\frac{\partial^2f}{\partial x^2}(x_0,\mu_0)\neq0$, the family is equivalent to

$$
\dot x=\mu x-x^2,
$$

in which the two equilibria $x=0$ and $x=\mu$ exchange their stability at $\mu=0$ but persist;

(iii) **(pitchfork)** if in addition the family is invariant under the symmetry $x\mapsto-x$ — equivalently the vector field is odd in the deviation — and the generic nondegeneracy conditions hold, the family is equivalent to

$$
\dot x=\mu x-x^3,
$$

in which the symmetric equilibrium $x=0$ loses stability at $\mu=0$ and a symmetric pair $x=\pm\sqrt\mu$ of stable equilibria appears for $\mu>0$ (the **supercritical** case); with the opposite sign, $\dot x=\mu x+x^3$, the pair exists for $\mu<0$ and is unstable, and the equilibrium keeps a small unstable branch after the bifurcation (the **subcritical** case).

*Proof (sketch).* The centre manifold theorem reduces to dimension one; in the one-dimensional family $g(x,\mu)$ with $g(0,0)=0$, $g_x(0,0)=0$, the implicit function theorem applied to $g$ gives the equilibria, and the sign of the second derivative decides whether the zero set of $g$ is a parabola opening to one side (saddle-node), a crossing of two curves (transcritical) or a symmetric cubic (pitchfork). The equivalence to the normal form is obtained by a parameter-dependent change of coordinates that puts the zero set and the flow direction into the stated polynomial form, together with a reparametrisation of $\mu$. $\square$

**Example (the pitchfork in the antisymmetric logistic family).** The family $x\mapsto\mu x-x^3$ of one-dimensional maps has, for $\mu$ crossing $1$, the same pitchfork structure: the fixed point $x=0$ is stable for $\mu<1$ and unstable for $\mu>1$, and the pair $x=\pm\sqrt{\mu-1}$ of stable fixed points appears at $\mu=1$. The corresponding flow normal form $\dot x=\mu x-x^3$ has the same bifurcation diagram, and the two are related by the discretisation of the flow.

### The Hopf Bifurcation

**Theorem (Andronov–Hopf).** Let $f$ be a one-parameter family with $f(x_0,\mu_0)=0$, and suppose that $A(\mu)=D_xf(x_0,\mu)$ has a simple pair of eigenvalues $\lambda(\mu)=\alpha(\mu)\pm i\omega(\mu)$ with $\alpha(\mu_0)=0$, $\omega(\mu_0)=\omega_0>0$, no other eigenvalue on the imaginary axis, and the **transversality** $\alpha'(\mu_0)\neq0$; suppose further that the **first Lyapunov coefficient** $\ell_1$, computed from the second and third derivatives of $f$ at $(x_0,\mu_0)$, is nonzero. Then the family is equivalent near $(x_0,\mu_0)$ to the normal form in polar coordinates

$$
\dot r=\mu r+\ell_1r^3+O(r^5), \qquad \dot\theta=\omega_0+O(\mu,r^2),
$$

and the phase portrait is as follows: for $\mu$ on the side of $\mu_0$ on which $(\mu-\mu_0)\alpha'(\mu_0)<0$ the equilibrium is stable and there is no closed orbit near it, while on the other side the equilibrium is unstable and there is exactly one limit cycle, of radius $r\approx\sqrt{-(\mu-\mu_0)\alpha'(\mu_0)/\ell_1}$, which is stable when $\ell_1<0$ (**supercritical Hopf**) and unstable when $\ell_1>0$ (**subcritical Hopf**).

*Proof (sketch).* The centre manifold is two-dimensional; in polar coordinates the normal form of Poincaré–Dulac is $\dot r=(\alpha(\mu)+O(\mu^2))r+\ell_1r^3+O(r^4)$ and $\dot\theta=\omega_0+O(\cdot)$, with the lowest resonant term $z|z|^2$ the only one that survives, because the resonances of a purely imaginary eigenvalue $\lambda=i\omega_0$ are the monomials $z|z|^{2k}$. The radius equation is a one-dimensional saddle-node in disguise: its nonzero equilibria exist exactly on the side of $\mu_0$ where the linear coefficient changes sign with $\mu$ and their stability is the sign of $\ell_1$, while the two-dimensional rotation sweeps them into a limit cycle. $\square$

**Example (the model limit cycle).** The planar family in polar coordinates $\dot r=\mu r-r^3$, $\dot\theta=1$ has the circle $r=\sqrt\mu$ as the limit cycle for $\mu>0$, with the equilibrium at the origin stable for $\mu<0$ and unstable for $\mu>0$; the first Lyapunov coefficient is $\ell_1=-1$, so the bifurcation is supercritical, and the radius of the cycle grows as $\sqrt\mu$. The planar family $\dot x=\mu x-y-x(x^2+y^2)$, $\dot y=x+\mu y-y(x^2+y^2)$ is the same bifurcation in Cartesian form.

## Versal Unfoldings and the Codimension-Two Theory

### Versal Unfoldings

**Definition.** Let $f_0$ be a vector field with a singularity at the origin. An **unfolding** of $f_0$ is a family $F(x,\mu)$ with $F(x,0)=f_0(x)$; an unfolding $F$ is **versal** if every other unfolding $G$ of $f_0$ is induced from it, that is, $G(x,\nu)=\Psi^*F(x,\phi(\nu))$ up to the changes of coordinates and the reparametrisation, and **miniversal** if it is versal with the least number of parameters. The number of parameters of a miniversal unfolding is the codimension of the singularity, and the miniversal unfolding of a codimension-one bifurcation is the one-parameter normal form of the previous section.

**Theorem (versal unfoldings).** For a vector field $f_0$ with a singularity at the origin and linearisation $A$:

(i) if $A$ has a simple eigenvalue $0$ and no other neutral eigenvalue, the miniversal unfolding has one parameter, $\dot x=\mu+g(x)$ with $g$ the centre part, and the possible classes are the saddle-node, the transcritical and the pitchfork of the classification theorem;

(ii) if $A$ has the double eigenvalue $0$ with a single Jordan block (the **Takens–Bogdanov** singularity), the codimension is two and the miniversal unfolding is, up to smooth equivalence,

$$
\dot x=y, \qquad \dot y=\mu_1+\mu_2y+x^2\pm xy ,
$$

whose bifurcation set in the $(\mu_1,\mu_2)$-plane carries, besides the fold curves and the Hopf curve, a curve of **homoclinic** bifurcations at which the stable and unstable manifolds of a hyperbolic equilibrium form a loop;

(iii) if $A$ has a simple pair of purely imaginary eigenvalues and no other neutral eigenvalue, the miniversal unfolding has one parameter, $\dot z=(\mu+i\omega_0)z+\ell_1z|z|^2$ up to higher order, and it organises the Hopf bifurcation of the previous section; the Hopf singularity with $\ell_1\neq0$ is therefore of codimension one, and the degenerate case $\ell_1=0$, the **generalised Hopf** or Bautin singularity, is of codimension two, its miniversal unfolding carrying the two parameters that control the sign of the cubic coefficient and produce the secondary cycle;

(iv) the classification of the unfoldings of a singularity with a nilpotent or neutral linear part is the **classification of the singularities** of the associated catastrophe, and the elementary catastrophes of Thom — the fold, the cusp, the swallowtail, the butterfly and the three umbilics — are the miniversal unfoldings of the corresponding potential singularities, with the state variables of the potential being the phase variables of the gradient vector field.

*Proof (sketch).* The number and the form of the parameters of a miniversal unfolding are computed from the quotient of the space of vector fields by the infinitesimal action of the changes of coordinates and of the parameter directions; the bases of this quotient, for the nilpotent cases, are the monomials $1,y,xy$ of the Takens–Bogdanov normal form and the corresponding monomials of the higher singularities. $\square$

### Period Doubling and the Bifurcations of Maps

**Theorem (codimension-one bifurcations of a fixed point of a map).** Let $x\mapsto f(x,\mu)$ be a one-parameter family of diffeomorphisms with $f(x_0,\mu_0)=x_0$ and with $A=D_xf(x_0,\mu_0)$ having spectrum on the unit circle.

(i) **(fold, or saddle-node)** if $A$ has the simple eigenvalue $1$ and the transversality and non-degeneracy conditions hold, the family is equivalent to $x\mapsto x+\mu-x^2$, and a stable and an unstable fixed point are born;

(ii) **(flip, or period doubling)** if $A$ has the simple eigenvalue $-1$ and the eigenvalue crosses the unit circle transversally, $\frac{d}{d\mu}\lambda(\mu)|_{\mu_0}\neq0$ for the multiplier $\lambda(\mu)$ near $-1$, the family is equivalent to the normal form $x\mapsto(-1+\mu)x+ax^3$ with $a\neq0$, and a period-two orbit is born from the fixed point, stable when $a<0$ and unstable when $a>0$;

(iii) **(Neimark–Sacker)** if $A$ has a simple pair of eigenvalues $e^{\pm i\theta_0}$ on the unit circle with $\theta_0$ not a rational multiple of $2\pi$ and the transversality and non-degeneracy conditions hold, the family is equivalent to $z\mapsto e^{i\theta_0}(1+\mu)z+c\,z|z|^2$ and an invariant circle is born from the fixed point.

The proof follows the reduction of the discrete case to the Poincaré return map of the suspension, so that the centre manifold theorem and the normal form theorem are applied to the map instead of the flow, with the resonance condition for the multiplier $\lambda$ read as $\lambda=\prod_j\lambda_j^{\alpha_j}$.

**Theorem (Feigenbaum universality; period-doubling cascade).** Let $f_\mu$ be a one-parameter family of unimodal maps with a quadratic critical point, and let $\mu_1<\mu_2<\cdots$ be the values at which the period of the attracting orbit doubles. Then the ratios of successive intervals converge,

$$
\delta=\lim_{n\to\infty}\frac{\mu_n-\mu_{n-1}}{\mu_{n+1}-\mu_n}=4.669201609\ldots,
$$

the **Feigenbaum constant**, and the rescaled return maps converge to a universal limit: the **doubling (renormalisation) operator** $\mathcal T$, which rescales the second iterate $f\circ f$ of a unimodal map back to the unit interval and acts on the space of unimodal maps, has a fixed point $f^*$ with scaling factor $\alpha=-2.502907875\ldots$, and the universality means that every one-parameter family with a quadratic critical point is governed by the same fixed point of $\mathcal T$ and hence by the same sequence of ratios. Consequently the cascade accumulates at the finite parameter $\mu_\infty$, beyond which the limiting dynamics carries an invariant Cantor set on which the map is chaotic, and within whose parameter windows attracting cycles of every period occur, the family ceasing to be hyperbolic at $\mu_\infty$; the chaotic regime and the measure-theoretic aspects are treated .

**Example (the logistic family).** For the family $x\mapsto\mu x(1-x)$ the period-doubling values are approximately

$$
\mu_1=3, \qquad \mu_2=1+\sqrt6\approx3.449489743, \qquad \mu_3\approx3.544090360, \qquad \mu_4\approx3.564407266, \qquad \mu_5\approx3.568759420,
$$

with the accumulation at $\mu_\infty\approx3.569946$. The first two values are exact: the fixed point $x^*=1-1/\mu$ has multiplier $2-\mu$, which equals $-1$ at $\mu=3$, and solving $f_\mu^2(x)=x$ for the two-cycle and imposing that its multiplier $\mu^2(1-2x)(1-2y)$, which by $x+y=\frac{\mu+1}{\mu}$ and $xy=\frac{\mu+1}{\mu^2}$ equals $4+2\mu-\mu^2$, is $-1$ gives the quadratic $\mu^2-2\mu-5=0$, that is $\mu=1+\sqrt6$. The later values are obtained by continuing the attracting cycle and locating each transition by bisection on its multiplier; in double precision this returns the multiplier $-1$ at $3.544090360$, $3.564407266$ and $3.568759420$, and the successive ratios $(3.449489743-3)/(3.544090360-3.449489743)\approx4.7514$, then $4.6563$ and $4.6682$, converging to the Feigenbaum constant $\delta=4.669201609\ldots$ of the theorem above.

## Global Bifurcations

**Definition.** A **homoclinic orbit** of a flow is an orbit that converges to the same hyperbolic equilibrium in both time directions, so that it lies in the intersection $W^s(p)\cap W^u(p)$ of the stable and unstable manifolds of $p$; a **heteroclinic orbit** joins two distinct equilibria or periodic orbits. A **homoclinic bifurcation** is a parameter value at which the intersection ceases to be transverse or a loop of a homoclinic orbit is destroyed or created.

**Theorem (Shilnikov).** Let $p$ be a hyperbolic equilibrium of a three-dimensional flow with a real eigenvalue $\rho>0$ and a pair $\lambda_1,\lambda_2$ with $\operatorname{Re}\lambda_i<0$ satisfying the **saddle condition** $\rho>|\operatorname{Re}\lambda_i|$, and suppose the flow has a homoclinic orbit to $p$ at $\mu=0$. Then in any neighbourhood of the homoclinic orbit and for an open set of parameters near $0$, the flow has an invariant Cantor set on which the return map is conjugate to a full shift on two symbols, and consequently the flow has uncountably many orbits and infinitely many periodic orbits of arbitrarily large period, and positive topological entropy. The construction is the same as in the horseshoe: the return map near the homoclinic orbit contracts in one direction and expands in the other, and the invariant set is the horseshoe. In the complementary case $\rho<|\operatorname{Re}\lambda_i|$ the return map produces a countable family of horseshoes in place of the single conjugacy to the full shift, and the conclusion of infinitely many periodic orbits persists; this is Shilnikov's second case, and the two cases are the two sides of the saddle condition.

**Theorem (the Takens–Bogdanov bifurcation set).** The two-parameter unfolding of the double-zero singularity of the previous section has, in the $(\mu_1,\mu_2)$-plane, curves of saddle-node bifurcations, a curve of Hopf bifurcations, and a curve of homoclinic bifurcations ending at the origin; the homoclinic curve is the global counterpart of the local Hopf curve, and the transition from a small limit cycle to a large homoclinic loop as the parameters cross the curves is the organising picture of the two-parameter family.

**Example (the global bifurcation of a planar family).** In the Liénard-type family $\dot x=y$, $\dot y=-x+\mu(1-x^2)y$ a stable limit cycle is born at the Hopf bifurcation at $\mu=0$ and persists for all $\mu>0$, so the bifurcation at $\mu=0$ is the only one; in the family $\dot x=y$, $\dot y=\mu_1+x^2-xy$ of Takens–Bogdanov type the limit cycle born at the Hopf curve is destroyed at a homoclinic loop for a finite value of the parameter, so the Hopf and homoclinic curves bound the interval of parameters in which the cycle exists, and the two bifurcations are the endpoints of that interval. The planar theory and the Poincaré–Bendixson theorem used here are those of *Smooth Dynamical Systems*.

## Summary

A **bifurcation** is a change of the topological type of a parameter family of vector fields or diffeomorphisms; the **codimension** is the number of parameters needed to unfold the singularity, the local theory reduces to the **centre manifold** $W^c$ tangent to the neutral eigenspace, and the **Poincaré–Dulac theorem** removes all non-resonant monomials from the Taylor expansion, leaving the resonant normal form; for a Hamiltonian family with a non-degenerate quadratic part the surviving form is the **Birkhoff normal form**, and the Diophantine case is **Siegel linearisable**. A **versal unfolding** induces all others, a **miniversal** one has as many parameters as the codimension, and the **Sotomayor classification** gives the codimension-one bifurcations of an equilibrium with a simple eigenvalue zero: the **saddle-node** $\dot x=\mu-x^2$, in which two equilibria collide and disappear, the **transcritical** $\dot x=\mu x-x^2$, in which two equilibria exchange stability, and the **pitchfork** $\dot x=\mu x-x^3$ in the presence of a symmetry, supercritical or subcritical according to the sign of the cubic term. The **Andronov–Hopf theorem** gives the birth of a limit cycle from a simple pair of imaginary eigenvalues crossing the axis transversally, with the **first Lyapunov coefficient** deciding the supercritical and subcritical cases, and the normal form $\dot r=\mu r+\ell_1r^3$, $\dot\theta=\omega_0$ in polar coordinates.

Beyond codimension one, the **Takens–Bogdanov** unfolding $\dot x=y$, $\dot y=\mu_1+\mu_2y+x^2\pm xy$ organises the fold, Hopf and homoclinic curves of a two-parameter family, and the classification of the unfoldings of potential singularities is the **catastrophe theory** of Thom. For a fixed point of a map the codimension-one bifurcations are the **fold**, the **flip** and the **Neimark–Sacker** bifurcations, and the **flip** iterates into the **period-doubling cascade**, whose parameter ratios converge to the **Feigenbaum constant** $\delta=4.669201609\ldots$ by the universality of the doubling operator $\mathcal T$, which rescales the second iterate $f\circ f$ back to the interval and is normalised by $\mathcal Tf(x)=\alpha f(f(x/\alpha))$ with $\alpha=1/f(1)$; at the fixed point $\alpha=1/f^*(1)=-2.502907875\ldots$; for the logistic family the doubling values start at $3$, $1+\sqrt6\approx3.449490$, $3.544090$, $3.564407$ and accumulate at $3.569946$. The **global** bifurcations concern the non-transverse intersections of stable and unstable manifolds: the **homoclinic** and **heteroclinic** loops, and the theorem of **Shilnikov**, which produces a horseshoe, infinitely many periodic orbits and positive entropy in a neighbourhood of a saddle-type homoclinic orbit.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mu$, $\Lambda$ | parameter and parameter space |
| $f(x,\mu)$, $f_\mu$ | parameter family of fields or maps |
| $\Sigma$ | bifurcation set |
| $A=D_xf(x_0,\mu_0)$ | linearisation at the singularity |
| $W^c_{\mathrm{loc}}$ | local centre manifold |
| $\lambda(\mu)=\alpha(\mu)\pm i\omega(\mu)$ | critical eigenvalue pair |
| $\ell_1$ | first Lyapunov coefficient |
| $\mu_1<\mu_2<\cdots$, $\mu_\infty$ | period-doubling values and accumulation |
| $\delta$, $\alpha$ | Feigenbaum constants $4.6692\ldots$, $-2.5029\ldots$ |
| $\mathcal T$ | doubling (renormalisation) operator |
| $\rho,\lambda_1,\lambda_2$ | saddle eigenvalues of Shilnikov's theorem |





## Further Reading

- Henri Poincaré, "Sur les propriétés des fonctions définies par les équations aux différences partielles", *Journal de l'École Polytechnique* 50 (1879), 1–60, and *Les méthodes nouvelles de la mécanique céleste* (Gauthier-Villars, 1892–1899), for the normal-form and resonance theory.
- John E. Marsden and Marjorie McCracken, *The Hopf Bifurcation and Its Applications* (Springer, 1976), for the Andronov–Hopf theorem, its proof and the normal forms of the bifurcation.
- Jorge Sotomayor, "Generic one-parameter families of vector fields on two-dimensional manifolds", *Publications Mathématiques de l'IHÉS* 43 (1974), 5–46, for the classification of the codimension-one bifurcations.
- Vladimir I. Arnol'd, *Geometrical Methods in the Theory of Ordinary Differential Equations* (Springer, 1983), for the versal unfoldings, the Poincaré–Dulac and Birkhoff normal forms and the singularity classification.
- Floris Takens, "Forced oscillations and bifurcations", in *Applications of Global Analysis I* (Rijksuniversiteit Utrecht, 1974), for the Takens–Bogdanov singularity and its unfolding.
- René Thom, *Structural Stability and Morphogenesis* (Benjamin, 1975), for catastrophe theory and the elementary catastrophes.
- Mitchell J. Feigenbaum, "Quantitative universality for a class of nonlinear transformations", *Journal of Statistical Physics* 19 (1978), 25–52, for the universality of the period-doubling cascade and the constants $\delta,\alpha$.
- Pierre Collet and Jean-Pierre Eckmann, *Iterated Maps on the Interval as Dynamical Systems* (Birkhäuser, 1980), for the renormalisation operator, the doubling operator and the proof of the universality.
- Leonid P. Shilnikov, "A case of the existence of a denumerable set of periodic motions", *Soviet Mathematics Doklady* 6 (1965), 163–166, for the homoclinic theorem and the horseshoe.
- John Guckenheimer and Philip Holmes, *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields* (Springer, 1983), for a systematic account of the local and global bifurcations and their unfoldings.
