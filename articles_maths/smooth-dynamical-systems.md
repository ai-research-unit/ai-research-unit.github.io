
# __Smooth Dynamical Systems__

## Introduction

A **smooth dynamical system** is a smooth manifold $M$ together with a smooth vector field $X$ on it, or a diffeomorphism $f:M\to M$; the continuous-time system produced by the vector field is its **flow** $\varphi_t$, the one-parameter group of diffeomorphisms obtained by solving $\dot x=X(x)$, and the discrete-time system produced by the diffeomorphism is the iteration of $f$. Unlike the topological theory, which assumes only continuity, the smooth theory has a derivative at every point, and the derivative linearises the system: near a fixed point the flow is governed by the spectrum of $DX(p)$, near a periodic orbit by the derivatives of the return map, and the fundamental theorems — the straightening lemma, the linearisation theorem of Hartman and Grobman, the stable manifold theorem, the Poincaré–Bendixson theorem in the plane and the theory of structural stability and genericity — all rest on the analysis of that derivative. The hyperbolicity that arises when no eigenvalue of the linearisation is neutral is the subject, to which this article hands over the stable manifold theorem, the Anosov systems, the Axiom A theory and the measure of maximal entropy; here the smooth foundations, the local and global structure of flows in low dimension, the stability theory and the genericity of the qualitative behaviour are developed.

The article begins with vector fields and flows: the existence and uniqueness of the integral curve through a point, the local flow and the group property, the completeness of the flow, and the straightening lemma that makes every non-singular point look like a translation locally. It continues with the fixed points, their linearisations, the periodic orbits and their return maps, the Floquet theory of the linearised equation along a periodic orbit, and the statement of the Hartman–Grobman theorem, with the details deferred. It then treats stability: the Lyapunov stability and asymptotic stability, the Lyapunov functions and the invariance principle of LaSalle, the exponential stability of a linear system in terms of the spectrum, and the converse theorem of Lyapunov that builds a quadratic Lyapunov function from the resolvent. The planar theory follows: the index of an isolated equilibrium, the Poincaré–Hopf theorem and the Poincaré–Bendixson theorem, with the Dulac criterion and the classification of the limit sets of a planar flow. The article closes with structural stability and genericity — the Whitney topology, the Kupka–Smale theorem on the genericity of hyperbolicity and transversality, the closing lemma of Pugh, the stability conjecture and the suspension and cross-section constructions that identify the discrete and the continuous theories.

The smooth manifolds, the tangent bundle, the vector fields, the differential forms and the flows of vector fields are those of *Smooth Manifolds and Differential Geometry*; the transversality, the Sard theorem and the jet transversality are those of *Differential Topology*; the smooth maps with the Whitney topologies are standard and are not developed here. The existence and uniqueness of the solutions of the differential equation, the dependence on the initial conditions and on parameters, the Floquet theory of the linear equation with periodic coefficients and the variational equation are those of *Ordinary Differential Equations*, where the theory of a first-order system is developed; the Hamiltonian and Lagrangian formulations are those of *Lagrangian and Hamiltonian Systems*. The invariant measures, the ergodicity and the entropy of the smooth systems are those of *Ergodic Theory*, and the topological notions used here are those of *Topological Dynamics*. The hyperbolicity, the Anosov systems, the Axiom A theory, the Gibbs measures, the bifurcations of the families of vector fields and the geodesic flow lie outside this article.

No physics is invoked.

## Vector Fields and Flows

### Integral Curves and the Flow

**Definition.** Let $M$ be a smooth manifold and let $\mathfrak X(M)$ be the space of smooth vector fields on $M$. An **integral curve** of $X \in\mathfrak X(M)$ through $p \in M$ is a smooth curve $\gamma:I\to M$ on an interval $I \ni0$ with $\gamma(0)=p$ and $\gamma'(t)=X(\gamma(t))$; the **local flow** of $X$ is the map $\varphi:\mathcal D\to M$, $\mathcal D$ an open neighbourhood of $\{0\}\times M$ in $\mathbb{R}\times M$, defined by $\varphi(t,p)=\gamma_p(t)$ for the maximal integral curve $\gamma_p$ through $p$. The vector field is **complete** if $\mathcal D=\mathbb{R}\times M$, and then $\varphi_t=\varphi(t,\cdot)$ is a one-parameter group of diffeomorphisms: $\varphi_0=\mathrm{id}$, $\varphi_{s+t}=\varphi_s\circ\varphi_t$, and each $\varphi_t$ is a diffeomorphism of $M$ with inverse $\varphi_{-t}$.

**Theorem (existence, uniqueness and smooth dependence).** Let $M$ be a smooth manifold and $X \in\mathfrak X(M)$. Then for every $p \in M$ there is a unique maximal integral curve through $p$, the domain $\mathcal D$ of the flow is open, the flow $\varphi:\mathcal D\to M$ is smooth, and for every $(t,p) \in\mathcal D$ the derivative $D_p\varphi_t$ is the fundamental matrix of the **variational equation**

$$
\dot\Phi(t)=DX(\varphi_t(p))\,\Phi(t), \qquad \Phi(0)=\mathrm{id},
$$

so the derivative of the flow solves the linearised equation along the orbit. If $M$ is compact, every vector field is complete.

*Proof.* In a coordinate chart the equation $\dot x=X(x)$ is a first-order system with a smooth right-hand side, and the existence, uniqueness and smooth dependence on the initial condition are the standard theorems of *Ordinary Differential Equations*; the openness of $\mathcal D$ and the maximality of the curves are the continuation properties of the solutions. For the compact case one covers $M$ by finitely many charts and uses the local existence time, which is bounded below by the compactness. $\square$

**Example (linear and rotational flows).** (i) On $\mathbb{R}^n$ the constant vector field $X(x)=Ax$ has the complete flow $\varphi_t(x)=e^{tA}x$, and the flow is a group of linear maps; the orbit structure is governed by the Jordan form of $A$.

(ii) On $\mathbb{C}\cong\mathbb{R}^2$ the vector field $X(z)=iz$ has the flow $\varphi_t(z)=e^{it}z$, the rotation of the plane; its orbits are the circles centred at the origin and the fixed point at the origin, and the flow is periodic of period $2\pi$.

(iii) On the torus $\mathbb{T}^2$ the constant vector field $X(\theta_1,\theta_2)=(1,\alpha)$ has the flow $\varphi_t(\theta_1,\theta_2)=(\theta_1+t,\theta_2+\alpha t)$; the orbits are dense when $\alpha$ is irrational and periodic when $\alpha$ is rational, which is the Kronecker flow of *Topological Dynamics*.

**Theorem (straightening lemma).** Let $X \in\mathfrak X(M)$ and let $p \in M$ with $X(p)\neq0$. Then there are coordinates $(x_1,\dots,x_n)$ on a neighbourhood of $p$ in which $X=\partial/\partial x_1$, and the flow is the translation $x\mapsto(x_1+t,x_2,\dots,x_n)$.

*Proof.* Choose a hypersurface $N$ through $p$ transverse to $X(p)$ and coordinates $y_2,\dots,y_n$ on $N$; the map $(t,y_2,\dots,y_n)\mapsto\varphi_t(0,y_2,\dots,y_n)$ is a local diffeomorphism at the origin by the inverse function theorem, because its derivative at $p$ is invertible with $X(p)$ as the first column; in these coordinates the flow is the translation in $t$ and the vector field is the first coordinate field. $\square$

### Invariant Sets and Limit Sets

**Definition.** A subset $A \subseteq M$ is **invariant** for the flow if $\varphi_t(A)\subseteq A$ for all $t$ (and $\varphi_t(A)=A$ when the flow is complete and invertible), and a **first integral** of $X$ is a smooth function $H$ with $XH=0$, that is, constant along the orbits. The **$\omega$-limit set** of $p$ for the flow is

$$
\omega(p)=\bigcap_{t\ge0}\overline{\{\varphi(s,p):s\ge t\}},
$$

and the $\alpha$-limit set is defined with $t\to-\infty$.

**Proposition.** Let $M$ be compact and $X \in\mathfrak X(M)$. Then $\omega(p)$ is nonempty, compact, connected and invariant, and it consists of the points that are limits of $\varphi(t_k,p)$ for a sequence $t_k\to+\infty$; if $H$ is a first integral, then $H$ is constant on $\omega(p)$.

*Proof.* The sets $\overline{\varphi([t,\infty)\times\{p\})}$ form a decreasing family of nonempty compact connected sets, so their intersection is nonempty, compact and connected; the invariance follows from the continuity of the flow and the group property; the constancy of a first integral on the limit set follows by continuity along the orbit. $\square$

## Fixed Points, Periodic Orbits and Linearisation

### Fixed Points and the Linearisation

**Definition.** A point $p \in M$ is a **fixed point** (or equilibrium) of $X$ if $X(p)=0$; the **linearisation** at $p$ is the endomorphism $A=DX(p)$ of $T_pM$, and $p$ is **hyperbolic** if no eigenvalue of $A$ has zero real part. The **stable** and **unstable** subspaces of a hyperbolic fixed point are the $A$-invariant subspaces

$$
E^s=\bigoplus_{\operatorname{Re}\lambda<0}\ker(A-\lambda)^{\nu(\lambda)},
\qquad
E^u=\bigoplus_{\operatorname{Re}\lambda>0}\ker(A-\lambda)^{\nu(\lambda)} ,
$$

and the **centre subspace** $E^c$ collects the eigenvalues on the imaginary axis.

**Theorem (Hartman–Grobman).** Let $p$ be a hyperbolic fixed point of $X \in\mathfrak X(M)$. Then there is a homeomorphism taking a neighbourhood of $p$ to a neighbourhood of the origin in $T_pM$ that carries the flow of $X$ to the flow of the linear field $y\mapsto Ay$ with $A=DX(p)$; in particular the local topological structure of the flow at a hyperbolic fixed point is that of its linearisation.

*Proof (sketch).* One writes the equation as $\dot x=Ax+g(x)$ with $g=O(\|x\|^2)$ and constructs the homeomorphism as a limit of conjugacies between the nonlinear flow truncated at large frequency and the linear flow, using the hyperbolicity to invert $A$ on the complement of the neutral spectrum and a fixed point argument in the Banach space of bounded maps. The details are the standard proof, cited below; the refinement to a $C^1$ linearisation fails in general, and the obstruction is the resonance of the eigenvalues. $\square$

**Theorem (stable manifold theorem).** Let $p$ be a hyperbolic fixed point of $X$ with $A=DX(p)$ and decomposition $T_pM=E^s\oplus E^u$. Then there are smooth *immersed* submanifolds $W^s(p)$ and $W^u(p)$, tangent at $p$ to $E^s$ and $E^u$, with

$$
W^s(p)=\{q:\varphi_t(q)\to p \text{ as } t\to+\infty\}, \qquad W^u(p)=\{q:\varphi_t(q)\to p \text{ as } t\to-\infty\},
$$

of the same dimensions as $E^s$ and $E^u$; they are invariant and their tangent spaces vary smoothly. The theorem, its global form and the Hadamard–Perron construction of the manifolds are developed.

### Periodic Orbits and the Return Map

**Definition.** A point $p$ is **periodic** of period $T>0$ if $\varphi_T(p)=p$ and $\varphi_t(p)\neq p$ for $0<t<T$; the orbit $\{\varphi_t(p):t \in\mathbb{R}\}$ is a **periodic orbit** (or closed orbit). A **cross-section** at $p$ is a smooth hypersurface $\Sigma$ through $p$ transverse to $X(p)$; the **Poincaré return map** (first return map) $P:\Sigma_0\to\Sigma$ is defined on a neighbourhood $\Sigma_0$ of $p$ in $\Sigma$ by $P(q)=\varphi_{\tau(q)}(q)$, where $\tau(q)>0$ is the first return time to $\Sigma$.

**Theorem (return map).** Let $p$ be a periodic point of period $T$ and let $\Sigma$ be a cross-section at $p$. Then the return map $P$ is a smooth diffeomorphism from a neighbourhood of $p$ in $\Sigma$ onto its image, its derivative at $p$ is obtained from $D_p\varphi_T$ by restricting to $T_p\Sigma$ and projecting along $X(p)$; the **Floquet multipliers** of the periodic orbit are the eigenvalues of $D_p\varphi_T$ on the full tangent space $T_pM$, one of which equals $1$, the eigenvector being $X(p)$, so that the nontrivial multiplier data are the $n-1$ eigenvalues of the derivative of the return map on $T_p\Sigma$, and the orbit is **hyperbolic** when those $n-1$ multipliers lie off the unit circle. The linearised equation along the periodic orbit, its fundamental matrix and the Floquet multipliers are the Floquet theory of an equation with periodic coefficients, developed in *Ordinary Differential Equations*.

**Theorem (Poincaré section).** Let $\Sigma \subseteq M$ be a codimension-one submanifold transverse to a complete flow $\varphi_t$ on $M$. Then the return map $P$ is defined on the set of points of $\Sigma$ whose forward orbit meets $\Sigma$ again, and the qualitative behaviour of the flow near $\Sigma$ is determined by that of $P$: periodic orbits of the flow crossing $\Sigma$ correspond to periodic points of $P$, invariant sets correspond to invariant sets, and the stability of a periodic orbit is that of the corresponding fixed point of $P$.

*Proof.* The existence and smoothness of the return time $\tau(q)$ follow from the transversality of $\Sigma$ to $X$ and the implicit function theorem applied to the equation $h(\varphi_\tau(q))=0$, where $h$ is a local defining function of $\Sigma$ with $dh\neq0$, which is solvable near the return time because $\frac{\partial}{\partial\tau}h(\varphi_\tau(q))=dh(X)\neq0$ by transversality; the correspondence of the invariant sets is by definition of the return map, and the derivative computation is the chain rule. $\square$

**Example (the linear flow on the torus and the rotation).** The constant flow on $\mathbb{T}^2$ with vector field $(1,\alpha)$ has the cross-section $\{\theta_1=0\}=\mathbb{T}$ and the return map the rotation $R_\alpha$ of the circle; the periodic orbits correspond to the periodic points of $R_\alpha$, and the topological structure of the flow is that of the suspension of $R_\alpha$, as constructed below.

## Stability and Lyapunov Functions

### Lyapunov Stability

**Definition.** Let $p$ be a fixed point of $X$ and let $d$ be a metric inducing the topology of $M$. The point is **Lyapunov stable** if for every $\epsilon>0$ there is $\delta>0$ such that $d(q,p)<\delta$ implies $d(\varphi_t(q),p)<\epsilon$ for all $t \ge0$; it is **asymptotically stable** if it is Lyapunov stable and there is $\delta>0$ such that $d(q,p)<\delta$ implies $\varphi_t(q)\to p$ as $t\to+\infty$; it is **exponentially stable** if the convergence is bounded by $Ce^{-\lambda t}$ with $\lambda>0$.

**Theorem (linear stability).** Let $p$ be a fixed point of $X$ and $A=DX(p)$. If every eigenvalue of $A$ has negative real part, then $p$ is exponentially stable; if some eigenvalue has positive real part, then $p$ is unstable; if eigenvalues lie on the imaginary axis the linearisation decides nothing, and the stability depends on the nonlinear terms.

*Proof.* In coordinates the equation is $\dot x=Ax+g(x)$ with $g=O(\|x\|^2)$. If the spectrum lies in the open left half-plane, there is an inner product whose quadratic form $x\mapsto\langle x,x\rangle$ satisfies $\frac{d}{dt}\langle x,x\rangle\le-\lambda\|x\|^2$ for small $\|x\|$, which gives the exponential decay; a positive eigenvalue produces growth along the corresponding unstable manifold, whence instability. The neutral case is decided by the higher-order terms: the systems $\dot x=x^2$ and $\dot x=-x^3$ on the line have the same linearisation at the origin and different stability. $\square$

**Theorem (Lyapunov functions).** Let $p$ be a fixed point and let $V:U\to[0,\infty)$ be a smooth function on a neighbourhood $U$ of $p$ with $V(p)=0$, $V(q)>0$ for $q \neq p$, and $\dot V(q)=\langle\nabla V(q),X(q)\rangle\le0$. Then $p$ is Lyapunov stable. If in addition $\dot V<0$ off $p$, then $p$ is asymptotically stable.

*Proof.* The function $V$ is nonincreasing along orbits, so the sublevel sets $\{V\le\alpha\}$ are invariant; for each $\epsilon$ choose $\alpha$ with $\{V\le\alpha\}\subseteq B(p,\epsilon)$, which is possible by the continuity of $V$ and the fact that $p$ is the strict minimum, and this gives stability. The strict decrease in the second case forces every orbit in a small sublevel set to converge to $p$ by a compactness argument. $\square$

**Theorem (LaSalle invariance principle).** Let $V$ be a smooth function on a neighbourhood of a compact invariant set $K$ with $\dot V\le0$ on $K$, and let $E=\{q \in K:\dot V(q)=0\}$; let $M$ be the largest invariant subset of $E$. Then every orbit in $K$ converges to $M$ as $t\to+\infty$.

*Proof.* The function $V$ is nonincreasing and bounded below, so it converges along an orbit to a limit $c$; the $\omega$-limit set is nonempty, compact, invariant and contained in $V^{-1}(c)$, and on it $\dot V=0$ because $V$ is constant; hence $\omega$-limit sets are contained in $M$, which is the assertion. $\square$

**Theorem (converse of Lyapunov).** Let $p$ be an exponentially stable fixed point of $X$ and let $A=DX(p)$ have its spectrum in the open left half-plane. Then for every symmetric positive definite matrix $Q$ there is a unique symmetric positive definite $P$ with $A^{\mathsf T}P+PA=-Q$, and $V(x)=x^{\mathsf T}Px$ is a Lyapunov function with $\dot V\le-\lambda\|x\|^2$ on a neighbourhood of $p$.

*Proof.* The Lyapunov equation has the solution $P=\int_0^\infty e^{tA^{\mathsf T}}Qe^{tA}\,dt$, convergent because the spectrum is in the left half-plane, and the stated inequality follows by differentiating $V$ along the linearised field and then using the smoothness of $X$ to absorb the nonlinear terms in a small neighbourhood. $\square$

## The Poincaré–Bendixson Theory in the Plane

### The Index of an Equilibrium

**Definition.** Let $X$ be a smooth vector field on an open set $U \subseteq\mathbb{R}^2$ and let $p$ be an isolated zero of $X$. The **index** $\operatorname{ind}_p(X)$ is the degree of the map $z\mapsto X(z)/|X(z)|$ from a small positively oriented circle around $p$ to the unit circle; equivalently, the winding number of $X$ along that circle. For a domain $\Omega$ with smooth boundary and finitely many zeros in its interior, $\operatorname{ind}_\Omega(X)$ is the winding number of $X$ along $\partial\Omega$.

**Theorem (index and the Poincaré–Hopf theorem).** (i) The index of an isolated zero is an integer, independent of the circle chosen small enough, and invariant under smooth changes of coordinates and under homotopies of $X$ that do not introduce zeros on the circle. (ii) If $\Omega$ is a domain with finitely many zeros of $X$ in its interior and no zeros on its boundary, then

$$
\operatorname{ind}_\Omega(X)=\sum_{p:X(p)=0}\operatorname{ind}_p(X).
$$

(iii) If $M$ is a closed oriented surface and $X$ a smooth vector field on $M$ with finitely many zeros, then the sum of the indices of the zeros equals the Euler characteristic $\chi(M)$; in particular the sphere has no nonvanishing vector field, and the index of a source, a sink or a saddle is $+1,+1,-1$ respectively. The theorem is the Poincaré–Hopf theorem of *Differential Topology* and *Degree Theory and the Brouwer Fixed Point Theorem*, where the degree and the winding number are developed.

### The Poincaré–Bendixson Theorem

**Theorem (Poincaré–Bendixson).** Let $X$ be a smooth vector field on an open set $U \subseteq\mathbb{R}^2$ and let $p \in U$ be such that $\varphi_t(p)$ is defined for all $t \ge0$ and its forward orbit is contained in a compact subset of $U$. If $\omega(p)$ contains no fixed point, then $\omega(p)$ is a periodic orbit.

**Corollary (trichotomy of limit sets).** For a planar flow, every compact $\omega$-limit set either contains a fixed point, or is a periodic orbit, or consists of fixed points together with orbits connecting them.

*Proof (sketch).* The limit set is compact, connected and invariant. If it contains no fixed point, take $q \in\omega(p)$; the orbit of $q$ is contained in $\omega(p)$ and meets a small transverse segment $\Sigma$ at $q$. The orbit returns to $\Sigma$ infinitely often, and the monotonicity of the sequence of intersections along $\Sigma$ — a consequence of the Jordan curve theorem in the plane — forces the intersections to converge to $q$; hence the orbit is periodic, and the whole limit set is that periodic orbit. The corollary follows by applying the argument to a limit set that contains a fixed point and otherwise choosing a point whose orbit returns to a transverse segment. $\square$

**Theorem (Dulac's criterion).** Let $X$ be a smooth vector field on a simply connected open set $U \subseteq\mathbb{R}^2$. If there is a smooth positive function $g$ on $U$ with $\operatorname{div}(gX)$ of one sign and not identically zero on $U$, then $X$ has no periodic orbit in $U$.

*Proof.* A periodic orbit bounds a disc $D$ in $U$ by the Jordan curve theorem; the divergence theorem gives $\int_D\operatorname{div}(gX)\,dx=0$ because the boundary integral of $gX$ along the periodic orbit vanishes, contradicting the strict one-signedness of the divergence. $\square$

**Example (limit cycle).** The vector field in polar coordinates $\dot r=r(1-r)$, $\dot\theta=1$ has the unit circle $r=1$ as a periodic orbit, and every orbit with $r>0$ converges to it as $t\to+\infty$; the circle is a **limit cycle**, that is, a periodic orbit that is the $\omega$-limit set of a point outside it. The linearisation of the return map around the circle has multiplier $e^{-2\pi}<1$, so the cycles attract, and the example is the standard model of a stable limit cycle.

## Structural Stability and Genericity

### The Whitney Topology and Structural Stability

**Definition.** For $r \in\mathbb{N}_0\cup\{\infty\}$ the **Whitney $C^r$ topology** on the space $\mathfrak X^r(M)$ of $C^r$ vector fields is the topology generated by the sets $\{Y:\|Y-X\|_{C^r}<\epsilon\}$ with respect to a finite atlas and the norms of the derivatives up to order $r$; the space of $C^r$ diffeomorphisms carries the induced $C^r$ topology. A vector field $X$ is **structurally stable** if there is a neighbourhood $\mathcal U$ of $X$ in the $C^1$ topology such that every $Y \in\mathcal U$ is topologically conjugate to $X$, that is, there is a homeomorphism $h$ with $h\circ\varphi^X_t=\varphi^Y_t\circ h$ for all $t$; the diffeomorphism version is defined with conjugacy of the maps.

**Theorem (Kupka–Smale).** For $r \ge1$ there is a residual (dense $G_\delta$) subset of $\mathfrak X^r(M)$ consisting of vector fields all of whose fixed points and periodic orbits are hyperbolic and whose stable and unstable manifolds intersect transversely; such a field is called **Kupka–Smale**. The proof uses the jet transversality theorem of *Differential Topology*: hyperbolicity of the periodic orbits is generated by small perturbations of the derivatives along the orbits, and the transversality of the invariant manifolds by the Sard and Thom transversality theorems applied to the evaluation maps.

**Theorem (the closing lemma; Pugh).** Let $p$ be a point that is recurrent for $X$ in the sense that it lies in its own $\omega$-limit set, and let $r \ge1$. Then arbitrarily $C^1$-close to $X$ there is a vector field $Y$ having a periodic orbit through $p$. Consequently, for a residual subset of $\mathfrak X^1(M)$, the periodic orbits are dense in the non-wandering set, which is the general density theorem.

The closing lemma is the tool by which genericity statements about periodic orbits are proved; its proof is delicate and is cited below. The corresponding statements for diffeomorphisms are the closing lemma of Pugh and the $C^1$-generic theory of the dynamics.

**Theorem (stability conjecture).** A $C^1$ diffeomorphism of a compact manifold is structurally stable if and only if it satisfies Axiom A and the strong transversality condition; structural stability is an open property in the $C^1$ topology, and the analogous statements hold for flows. The Axiom A condition — that the non-wandering set is hyperbolic and that the periodic points are dense in it — and the spectral decomposition of the non-wandering set are developed; the sufficiency is due to Robbin and Robinson and the necessity to Mañé, so that the conjecture of Palis and Smale is settled for diffeomorphisms in the $C^1$ topology. For flows the statement needs a modification: the geometric Lorenz attractor is structurally stable although it is not hyperbolic, the singularity being an indispensable part of the attractor, so Axiom A is not necessary for a flow either, and the classification of the robust attractors of a flow must allow the singularly hyperbolic ones. The Lorenz attractor and its structural stability belong.

**Example (Morse–Smale and the horseshoe).** (i) A **Morse–Smale** vector field has a non-wandering set consisting of finitely many hyperbolic fixed points and periodic orbits, and the stable and unstable manifolds of distinct orbits meet transversely; the gradients of Morse functions are the basic examples and the invariant set is a finite union of points and closed orbits.

(ii) The **Smale horseshoe** is a diffeomorphism of the disc that stretches, folds and reinserts it so that the invariant set is a Cantor set on which the map is conjugate to the full two-sided two-shift; it is the model of a hyperbolic set with infinitely many periodic orbits and is the first example of the chaotic behaviour treated .

### Suspensions and Cross-Sections

**Definition.** Let $f:N\to N$ be a diffeomorphism and let $\tau:N\to(0,\infty)$ be a smooth function (the **roof**). The **suspension** of $f$ with roof $\tau$ is the flow on the quotient $M=\{(x,s):x \in N,\ 0\le s\le\tau(x)\}/\sim$ with $(x,\tau(x))\sim(f(x),0)$, defined by translation in $s$ modulo the identification.

**Theorem (suspension and return map).** The suspension of $(f,\tau)$ is a smooth flow whose return map to the section $N\times\{0\}$ is $f$, and whose periods are the sums $\sum_{k}\tau(f^kx)$ over the periodic orbits of $f$. Conversely, if $X$ is a complete flow on $M$ and $\Sigma \subseteq M$ is a closed hypersurface transverse to $X$ meeting every orbit, then the return map $P$ of $\Sigma$ is a diffeomorphism and the flow is the suspension of $P$ with the return time as roof. The two constructions are inverse to one another up to conjugacy, and they identify the dynamics of a flow with that of the discrete system of its return map.

*Proof.* The quotient is a smooth manifold because $f$ is a diffeomorphism and $\tau$ is smooth; the flow is constructed from the translation in $s$, and the identification produces a smooth vector field transverse to the section, whose return map is manifestly $f$. The converse is the content of the Poincaré section theorem together with the smoothness of the return time. $\square$

**Corollary (transfer of properties).** The suspension of a hyperbolic diffeomorphism is a hyperbolic flow, the suspension of an Anosov diffeomorphism is an Anosov flow, and the entropy of the suspension of $(P,\tau)$ with respect to an invariant measure $m$ of $P$ is $h_m(P)/\int\tau\,dm$ by Abramov's formula, so that the entropy per unit time is the entropy of the return map divided by its mean return time whenever the roof is constant; consequently the discrete and the continuous theories have the same catalogue of examples, and many results stated for a diffeomorphism have a flow version obtained by suspension. The precise statements about hyperbolicity, the Anosov property and the entropy belong and *Ergodic Theory*.

## Summary

A smooth dynamical system is a vector field $X$ on a smooth manifold $M$, whose **flow** $\varphi_t$ solves $\dot x=X(x)$ and is a one-parameter group of local diffeomorphisms; the local flow is smooth in $(t,p)$, the derivative $D_p\varphi_t$ satisfies the variational equation $\dot\Phi=DX(\varphi_t(p))\Phi$, and the flow is complete when $M$ is compact. The **straightening lemma** makes the flow a translation near every non-singular point, and the limit sets $\omega(p)$ are nonempty, compact, connected and invariant over a compact manifold. A fixed point is **hyperbolic** when no eigenvalue of $A=DX(p)$ is purely imaginary; the **Hartman–Grobman theorem** linearises the flow topologically at a hyperbolic fixed point, and the **stable manifold theorem** produces the invariant manifolds $W^s(p)$, $W^u(p)$ tangent to the stable and unstable subspaces, whose global theory belongs. A **periodic orbit** has a **Poincaré return map** on a transverse section, with derivative whose eigenvalues are the **Floquet multipliers**; one multiplier is $1$ and the orbit is hyperbolic when the others are off the unit circle.

For stability, **Lyapunov stability** is proved from a **Lyapunov function** $V\ge0$ with $\dot V\le0$, asymptotic stability from the strict version, the **LaSalle invariance principle** from the largest invariant subset of $\{\dot V=0\}$, and the stability of a linear system is read from the spectrum of $A$, with the hyperbolic cases decided by the linearisation and the neutral cases by the higher-order terms; the **converse theorem** solves the Lyapunov equation $A^{\mathsf T}P+PA=-Q$. In the plane the **index** of an isolated zero of a vector field is an integer, the indices of the zeros in a domain add to the winding number of the field on the boundary, the sum of the indices on a closed surface is the Euler characteristic (**Poincaré–Hopf**), and the **Poincaré–Bendixson theorem** states that a compact $\omega$-limit set with no fixed point is a periodic orbit; **Dulac's criterion** excludes periodic orbits from a simply connected region carrying a positive factor $g$ with $\operatorname{div}(gX)$ of one sign.

Structural stability in the **Whitney $C^1$ topology** means conjugacy with all nearby fields; the **Kupka–Smale theorem** gives a residual set of fields with hyperbolic periodic orbits and transversal intersections of their invariant manifolds, the **closing lemma** of Pugh turns recurrent points into periodic orbits under a small perturbation, and the **stability conjecture**, proved for diffeomorphisms by Robbin and Robinson for the sufficiency and by Mañé for the necessity, identifies the structurally stable diffeomorphisms with those satisfying Axiom A and strong transversality, a condition whose hyperbolic content is developed; for flows the characterisation fails, the geometric Lorenz attractor being structurally stable without being hyperbolic. The **suspension** of a diffeomorphism with a roof function is a flow whose return map is the diffeomorphism, and every flow with a closed transverse section is such a suspension, so the discrete and continuous theories share their examples; the **Morse–Smale** fields and the **Smale horseshoe** are the fundamental models of the finite and the infinite dynamical complexity respectively.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M$ | smooth manifold |
| $\mathfrak X(M)$, $\mathfrak X^r(M)$ | smooth and $C^r$ vector fields |
| $X$, $A=DX(p)$ | vector field and its linearisation |
| $\varphi_t$, $\varphi(t,p)$ | flow of $X$ |
| $\mathcal D$ | domain of the local flow |
| $E^s$, $E^u$, $E^c$ | stable, unstable, centre subspaces |
| $W^s(p)$, $W^u(p)$ | stable and unstable manifolds |
| $\Sigma$, $P$ | cross-section, Poincaré return map |
| $T$, Floquet multipliers | period and multipliers of a periodic orbit |
| $V$, $\dot V$ | Lyapunov function and its derivative along $X$ |
| $\operatorname{ind}_p(X)$ | index of an isolated equilibrium |
| $\chi(M)$ | Euler characteristic |
| $\tau$, $N$ | roof function and base of a suspension |
| $\Omega(X)$ | non-wandering set |
| $C^r$ topology | Whitney topology on fields and diffeomorphisms |





## Further Reading

- Philip Hartman, "A lemma in the theory of structural stability of differential equations", *Proceedings of the American Mathematical Society* 11 (1960), 610–620, and David M. Grobman, "Homeomorphism of systems of differential equations", *Doklady Akademii Nauk SSSR* 128 (1959), 880–881, for the linearisation theorem at a hyperbolic equilibrium.
- Morris W. Hirsch, Charles C. Pugh and Michael Shub, *Invariant Manifolds* (Springer, 1977), for the stable manifold theorem and the Hadamard–Perron construction.
- Solomon Lefschetz, *Differential Equations: Geometric Theory* (Interscience, 1957), for the Poincaré–Bendixson theory and the index of a planar equilibrium.
- Philip Hartman, *Ordinary Differential Equations* (Wiley, 1964), for the existence theory, the variational equation and the Floquet theory.
- Ivan G. Malkin, *Theory of Stability of Motion* (United States Atomic Energy Commission, 1952), and Joseph P. LaSalle, "An extension of Liapunov's direct method", *Journal of Mathematical Analysis and Applications* 3 (1961), 434–444, for the Lyapunov stability theory and the invariance principle.
- Maurício M. Peixoto, "Structural stability on two-dimensional manifolds", *Topology* 1 (1962), 101–120, for the planar structural stability and the Morse–Smale theory.
- Jacob Palis and Stephen Smale, "Structural stability theorems", in *Global Analysis* (American Mathematical Society, 1970), 223–231, for the stability conjecture and the Axiom A theory.
- Ricardo Mañé, "A proof of the $C^1$ stability conjecture", *Publications Mathématiques de l'IHÉS* 66 (1988), 161–210, for the solution of the stability conjecture.
- John Guckenheimer and Robert F. Williams, "Structural stability of Lorenz attractors", *Publications Mathématiques de l'IHÉS* 50 (1979), 59–72, for the structural stability of a flow that is not hyperbolic, which modifies the stability conjecture in the continuous case.
- Charles C. Pugh, "The closing lemma", *American Journal of Mathematics* 89 (1967), 956–1009, and "An improved closing lemma and a general density theorem", *American Journal of Mathematics* 89 (1967), 1010–1021, for the closing lemma and the density of the periodic orbits.
