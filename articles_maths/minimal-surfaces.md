
# __Minimal Surfaces__

## Introduction

A minimal surface is a surface whose area is stationary under variations that fix its boundary, and its defining property is the vanishing of the mean curvature. The two descriptions are equivalent: the first variation of the area functional is the integral of the normal component of the variation against the mean curvature vector, so the stationary surfaces are exactly those with $H=0$. The subject is the meeting point of the calculus of variations, the theory of partial differential equations and complex function theory, and it is the model geometric variational problem: its solutions are governed by a quasilinear elliptic equation, its existence theory is the prototype of the Plateau problem, and its classification and regularity theory has been the source of some of the deepest results in the analysis of this Part.

The area functional is deceptively simple. For a graph $u : \Omega \to \mathbb{R}$ over a domain in $\mathbb{R}^n$ the area is $\int_\Omega\sqrt{1+|\nabla u|^2}\,dx$, a convex integrand, and the Euler–Lagrange equation, computed in the general theory of the preceding articles, is the **minimal surface equation**

$$
\nabla\cdot\left(\frac{\nabla u}{\sqrt{1+|\nabla u|^2}}\right) = 0 ,
$$

a quasilinear elliptic equation whose solutions are the minimal graphs. For a parametrised surface the functional is invariant under reparametrisation, so its energy is not coercive on the naive space; this degeneracy is why the existence theory proceeds through the energy functional for maps from a fixed domain, which is coercive, and why the minimiser of the energy in a conformal class is also a minimiser of the area. The last observation, that a minimal surface is a harmonic and conformal immersion, opens the door to complex analysis and to the Weierstrass representation, by which every minimal surface in $\mathbb{R}^3$ is written as an integral of holomorphic data.

The article develops the definition and the first variation, the minimal surface equation and its elliptic character, the classical examples — the plane, the catenoid, the helicoid and the surfaces of Scherk and Enneper — and the classification results that single out the catenoid among surfaces of revolution. It then treats Plateau's problem: the existence of a disc-type minimal surface spanning a given Jordan curve, proved by Douglas and Radó, with the regularity that the solution enjoys in the interior and at the boundary, and with the possible appearance of branch points and of singularities in higher dimensions. The second variation and stability are treated next, with the Jacobi operator $\Delta + |A|^2$ and the classification of stable minimal surfaces in $\mathbb{R}^3$, and the article closes with Bernstein's theorem, the Weierstrass representation and the conformal-harmonic dictionary. The mean curvature of a surface and the curvature of a Riemannian manifold are the notions of Part II, used here without re-derivation. Harmonic maps are not covered here, which generalises the conformal-harmonic description to an arbitrary target, and the parabolic counterpart of the area is the mean curvature flow of this Part.

## The Area Functional and the First Variation

### Parametrised Surfaces and the Area

**Definition.** Let $M$ be a compact two-dimensional manifold with boundary $\partial M$ and let $\phi : M \to \mathbb{R}^n$ be an immersion of class $C^2$. The **area** of $\phi$ is

$$
A(\phi) = \int_M\sqrt{\det\bigl(g_{ij}(x)\bigr)}\,dx, \qquad g_{ij}(x) = \partial_i\phi(x)\cdot\partial_j\phi(x),
$$

where $g$ is the induced (first fundamental) metric. The **mean curvature vector** is the trace of the second fundamental form, $H = g^{ij}\mathrm{II}_{ij}$, and $\phi$ is **minimal** if $H\equiv0$.

**Definition.** A **variation** of $\phi$ is a $C^2$ map $\Phi : M\times(-\varepsilon,\varepsilon)\to\mathbb{R}^n$ with $\Phi(x,0)=\phi(x)$ for all $x$ and $\Phi(x,t)=\phi(x)$ for $x\in\partial M$ and all $t$; the associated **variational field** is $V(x) = \partial_t\Phi(x,t)|_{t=0}$, a vector field along $\phi$ vanishing on $\partial M$. The variation is **normal** if $V$ is everywhere perpendicular to $\phi_*TM$.

**Theorem (first variation of area).** For every variation $\Phi$ of $\phi$,

$$
\frac{d}{dt}A(\phi_t)\Bigr|_{t=0} = -\int_M V\cdot H\,dA ,
$$

where $dA = \sqrt{\det(g_{ij})}\,dx$ is the area element and $H$ is the mean curvature vector. Hence a surface is a critical point of the area functional for all variations fixing the boundary if and only if $H\equiv0$.

*Proof.* Quoted as standard and used in the preceding article in its one-dimensional form. The derivative of the induced metric is $\partial_tg_{ij} = \partial_iV\cdot\partial_j\phi + \partial_jV\cdot\partial_i\phi$, and the derivative of the volume element is the trace of that with respect to $g$; integrating by parts on $M$ and using the vanishing of $V$ on $\partial M$ produces the integral of $V$ against the trace of the second fundamental form, with the sign displayed. Since $V$ is an arbitrary field along $\phi$ vanishing on the boundary, the integral vanishes for all such $V$ exactly when $H=0$. $\square$

**Remark (the degeneracy of the area).** The area functional is invariant under reparametrisation: $A(\phi\circ\psi) = A(\phi)$ for every diffeomorphism $\psi$ of $M$. Its first variation therefore vanishes in the directions tangent to the reparametrisation group, and the functional is not coercive on a space of maps without a constraint on the parametrisation. This is why the existence theory of Plateau's problem is carried out for the **energy**

$$
E(\phi) = \frac12\int_M|\nabla\phi|^2\,dA ,
$$

which is coercive on $W^{1,2}(M,\mathbb{R}^n)$ and agrees with the area on conformal maps, $E(\phi) = A(\phi)$ for $\phi$ conformal.

### The Minimal Surface Equation

**Definition.** A **minimal graph** over an open set $\Omega \subseteq \mathbb{R}^n$ is the graph of a $C^2$ function $u : \Omega \to \mathbb{R}$ whose induced area is stationary among graphs with the same boundary values; equivalently, $u$ satisfies the **minimal surface equation**

$$
\operatorname{div}\left(\frac{\nabla u}{\sqrt{1+|\nabla u|^2}}\right) = 0 .
$$

**Theorem (Euler–Lagrange equation of the graph area).** The area of the graph of $u$ is $A(u) = \int_\Omega\sqrt{1+|\nabla u|^2}\,dx$, and its first variation vanishes for every compactly supported $v$ exactly when the minimal surface equation holds.

*Proof.* The integrand is $L(x,u,\nabla u) = \sqrt{1+|\nabla u|^2}$, with $L_{u}=0$ and $L_{p} = p/\sqrt{1+|p|^2}$; the Euler–Lagrange equation of the preceding article gives the displayed equation, and the equation is elliptic because $L_{pp} = (1+|p|^2)^{-1/2}(I - pp^{\mathrm{T}}/(1+|p|^2))$ is positive definite for every $p$. $\square$

The minimal surface equation is a quasilinear elliptic equation in divergence form, and it is the model of a **non-uniformly** elliptic equation: the eigenvalues of $L_{pp}$ are $1/(1+|p|^2)^{3/2}$ and $1/(1+|p|^2)^{1/2}$, so the ellipticity degenerates as $|\nabla u|\to\infty$. Every regularity theorem for minimal graphs must therefore control the gradient, and the theory begins with the gradient estimate.

**Theorem (gradient estimate).** For a minimal graph over a ball $B_R(x_0)$, the gradient satisfies

$$
|\nabla u(x_0)| \le C\exp\left(\frac{C}{R}\sup_{B_R(x_0)}|u|\right),
$$

with a constant $C$ depending only on $n$, so that a bounded minimal graph has a gradient bounded on compact subsets.

*Proof.* Quoted as standard (the Bombieri–De Giorgi–Giusti gradient estimate, in the form for the minimal surface equation on a ball). The proof uses a cut-off function, the once-integrated form of the equation and the Bochner-type identity for the function $\log(1+|\nabla u|^2)$. $\square$

## Examples and Classification

**Example (the plane).** The graph $u(x) = a\cdot x + b$ satisfies the minimal surface equation, because the gradient is constant and the divergence of a constant vector field vanishes. The plane is the simplest minimal surface and the reference case.

**Example (the catenoid).** The surface of revolution generated by the catenary $x_1 = \cosh x_3$, that is

$$
\sigma(t,\theta) = \bigl(\cosh t\cos\theta,\ \cosh t\sin\theta,\ t\bigr),
$$

is minimal: its principal curvatures are $\pm1/\cosh^2t$, whose sum is zero. It is the unique minimal surface of revolution in $\mathbb{R}^3$ besides the plane, and it satisfies the area growth $A(\sigma\cap B_R) \sim 2\pi R^2$ as $R\to\infty$, which is that of a plane but with an excess governed by its two ends.

**Example (the helicoid).** The surface

$$
\sigma(t,\theta) = \bigl(t\cos\theta,\ t\sin\theta,\ c\theta\bigr)
$$

is minimal for every $c\neq0$; it is ruled but not a plane, it is the unique ruled minimal surface in $\mathbb{R}^3$ that is not a plane, and it is not stable. The catenoid and the helicoid are locally isometric and are the two members of an isometric deformation that stretches the catenoid into the helicoid while keeping the mean curvature zero.

**Example (Scherk's surfaces).** The graph

$$
u(x_1,x_2) = \frac{1}{a}\log\frac{\cos(ax_1)}{\cos(ax_2)}, \qquad |a|\,|x_1|,\ |a|\,|x_2| < \frac\pi2,
$$

satisfies the minimal surface equation, as does the surface $e^{x_3} = \cos x_1/\cos x_2$ in $\mathbb{R}^3$. Scherk's first and second surfaces are the classical translation-invariant examples and show that a minimal surface can have a boundary at finite height.

**Example (Enneper's surface).** The parametrisation

$$
\sigma(u,v) = \Bigl(u - \frac{u^3}{3} + uv^2,\ v - \frac{v^3}{3} + u^2v,\ u^2-v^2\Bigr)
$$

is conformal with $\sigma_{uu}+\sigma_{vv}=0$, so it is minimal, and it is one of the first examples produced by the Weierstrass representation below. It has a curve of self-intersections and is not embedded.

## Plateau's Problem

### Statement and Existence

**Definition.** Let $\Gamma \subset \mathbb{R}^n$ be a closed Jordan curve. **Plateau's problem** asks for a continuous map $\phi : D \to \mathbb{R}^n$ from the closed disc, smooth on the open disc, that is a conformal minimal immersion of the open disc and maps $\partial D$ homeomorphically onto $\Gamma$. Such a $\phi$ is a **minimal disc** or a **solution of Plateau's problem**.

**Theorem (Douglas–Radó).** For every rectifiable Jordan curve $\Gamma \subset \mathbb{R}^n$, Plateau's problem has a solution; the solution minimises the energy $E$ among all $W^{1,2}$ maps of the disc whose boundary values are a (suitably normalised) parametrisation of $\Gamma$.

*Proof.* Quoted as standard (the theorem of Douglas and Radó, 1931). The proof minimises $E$ over the class of admissible maps, uses the coercivity of the energy and its weak lower semicontinuity on the reflexive space $W^{1,2}(D,\mathbb{R}^n)$ by the direct method of the preceding articles, and then shows that a minimiser with a suitably normalised boundary parametrisation is conformal; the conformality makes it a critical point of the area and hence minimal. The existence of the minimiser requires care because the class of admissible boundary parametrisations is not closed under weak limits, and it is exactly this difficulty that the **Douglas condition** resolves. $\square$

**Theorem (regularity).** A solution of Plateau's problem is real analytic on the open disc; it is an immersion except possibly at finitely many interior **branch points**, where $\nabla\phi$ vanishes and the surface has a conical or umbilic-like singularity, and it is embedded near a sufficiently smooth Jordan curve except possibly finitely many boundary branch points (Gulliver–Osserman–Spruck).

*Proof.* Quoted as standard. Interior analyticity is a consequence of the elliptic regularity of the minimal surface equation and of the conformality, the branch points are isolated by analyticity, and the boundary regularity is proved by a reflection argument when the curve is analytic, with the general smooth case following by approximation. $\square$

**Remark (dimensions and singularities).** In $\mathbb{R}^3$ a minimal disc has no interior singularity other than the branch points described; in higher codimension the situation is different, and there are minimal surfaces with isolated singularities. The cone over $S^3\times S^3$ in $\mathbb{R}^8$, the **Simons cone** $\{|x'|=|x''|\}$ with $x',x''\in\mathbb{R}^4$, is a stable minimal cone that is not flat, and it is the boundary case of the Bernstein theorem below: its existence is the reason the theorem holds in dimensions $n\le7$ and fails at $n=8$.

### The Isoperimetric Inequality

**Theorem (isoperimetric inequality for minimal surfaces).** Let $\phi : D\to\mathbb{R}^n$ be a minimal disc with boundary a closed curve of length $L$. Then

$$
A(\phi) \le \frac{L^2}{4\pi} ,
$$

with equality only for the planar disc.

*Proof.* Quoted as standard. The proof uses the conformal parametrisation, the harmonicity of the coordinate functions, and the Wirtinger inequality on the boundary circle applied to the Fourier expansion of the boundary parametrisation. $\square$

## Stability and the Second Variation

**Definition.** Let $\phi : M \to \mathbb{R}^n$ be a minimal immersion and consider a normal variation with field $V = f\nu$ for a function $f$ vanishing on $\partial M$ and a unit normal $\nu$. The **second variation** of the area is

$$
\frac{d^2}{dt^2}A(\phi_t)\Bigr|_{t=0} = \int_M\Bigl(|\nabla f|^2 - |A|^2f^2\Bigr)dA ,
$$

where $|A|^2$ is the squared norm of the second fundamental form. The **Jacobi operator** is $L = \Delta_M + |A|^2$ (with $\Delta_M$ the Laplace–Beltrami operator, here with the sign making $L$ consistent with the formula), and $\phi$ is **stable** if the second variation is nonnegative for every such $f$, equivalently if the first eigenvalue of $-L$ is nonnegative.

**Theorem (stability criterion).** A minimal surface is stable if and only if

$$
\int_M|A|^2f^2\,dA \le \int_M|\nabla f|^2\,dA
$$

for every compactly supported $f$; the plane and the catenoid are stable, the helicoid is not, and a complete stable minimal surface in $\mathbb{R}^3$ is a plane (do Carmo–Peng, Fischer-Colbrie–Schoen).

*Proof.* Quoted as standard. The first inequality is the second variation formula with the normalisation of the variation, and the stability inequality for a general normal variation follows by linearity; the classification of the stable complete surfaces uses the stability inequality tested against a logarithmic cut-off and the Gauss equation to bound the total curvature. $\square$

**Remark (stability and minimisation).** Stability is a local condition, and a stable minimal surface need not minimise area globally: the catenoid is stable and locally area-minimising, but a large enough bounding curve has a doubly connected minimal surface of smaller area. The distinction between a minimal surface and an area-minimising one is exactly the distinction between the first and the second variation, and it is the reason the existence theory of Plateau's problem is stated for minimisers of the energy rather than for stationary surfaces in general.

## Bernstein's Theorem and the Weierstrass Representation

### Minimal Graphs and Bernstein's Theorem

**Theorem (Bernstein).** Every entire solution $u : \mathbb{R}^2 \to \mathbb{R}$ of the minimal surface equation is an affine function; equivalently, every complete minimal graph in $\mathbb{R}^3$ is a plane.

*Proof.* Quoted as standard (Bernstein, 1915). The proof uses the conformal structure of the graph, the fact that the Gauss map of a minimal graph is quasiconformal with a bounded distortion given by the gradient estimate of the preceding section, and Liouville's theorem for the resulting bounded holomorphic function. $\square$

**Theorem (Bernstein in higher dimensions).** Every entire solution of the minimal surface equation on $\mathbb{R}^n$ is affine for $n\le7$ (Bombieri–De Giorgi–Giusti, using the theorems of Simons and of Almgren), and for $n\ge8$ there are entire non-affine solutions, whose graphs are asymptotic to the Simons cone; the Simons cone is area-minimising for $n\ge8$.

*Proof.* Quoted as standard. The dimension $n=8$ is critical because the stability of the Simons cone changes there, and the monotonicity and dimension-reduction arguments of geometric measure theory show that any non-flat minimal cone of least area in $\mathbb{R}^{n}$ gives rise to a non-affine entire solution in dimension $n$. $\square$

### The Weierstrass Representation

**Definition.** A **conformal minimal immersion** $\phi : M \to \mathbb{R}^3$ of a Riemann surface $M$ has, in a local conformal coordinate $z$, the **Weierstrass data** $(g,\omega)$ consisting of a meromorphic function $g$ (the Gauss map, after stereographic projection) and a holomorphic $1$-form $\omega$; the immersion is recovered by

$$
\phi(z) = \operatorname{Re}\int^z\Bigl(\tfrac12(1-g^2)\omega,\ \tfrac{i}{2}(1+g^2)\omega,\ g\,\omega\Bigr) ,
$$

and the induced metric is $\tfrac14(1+|g|^2)^2|\omega|^2$, so that $\phi$ is conformal exactly when this expression is positive, which requires that $\omega$ have no zeros or poles other than those of $g$.

**Theorem (Weierstrass representation).** Every conformal minimal immersion of a simply connected Riemann surface into $\mathbb{R}^3$ arises from Weierstrass data $(g,\omega)$ as above, and conversely every pair $(g,\omega)$ for which the metric $\tfrac14(1+|g|^2)^2|\omega|^2$ is nondegenerate defines a conformal minimal immersion; the immersion is single-valued on $M$ exactly when the periods of the holomorphic form vanish over a basis of $H_1(M,\mathbb{Z})$.

*Proof.* Quoted as standard. The harmonicity and conformality of $\phi$ imply that its coordinate functions are harmonic and that $\partial_z\phi$ is holomorphic with $\partial_z\phi\cdot\partial_z\phi = 0$; a holomorphic null vector in $\mathbb{C}^3$ is determined up to scale by its third component and its stereographically projected direction, which are $g$ and $\omega$, and integrating gives the formula. The period condition is the statement that the integral of the $1$-form over closed loops depends only on the homotopy class. $\square$

**Example (the catenoid and the helicoid in Weierstrass data).** For the catenoid, $g(z)=z$ and $\omega = dz/z^2$; for the helicoid, $g(z)=z$ and $\omega = i\,dz/z^2$. The two surfaces differ only by the constant phase of the Weierstrass form, which is the conformal form of the isometric deformation between them; the computation is exact and exhibits the power of the representation.

**Remark (the harmonic–conformal dictionary).** The content of the Weierstrass representation is that a minimal surface in $\mathbb{R}^3$ is the same thing as a conformal harmonic map of a Riemann surface into $\mathbb{R}^3$; harmonicity is the Euler–Lagrange equation of the energy and conformality is the constraint, and the harmonicity of each coordinate is the Laplace equation. The general theory of harmonic maps into a Riemannian target, where the energy is $\int|\nabla\phi|^2$ and the tension field replaces the Laplace equation, is not covered here; the present theory is the case of the flat target $\mathbb{R}^3$ with the conformality constraint that makes the energy equal to the area.

## Summary

A minimal surface is a surface whose area is stationary under variations fixing the boundary, equivalently a surface whose mean curvature vector vanishes; the equivalence is the first variation formula $\frac{d}{dt}A|_{t=0} = -\int V\cdot H\,dA$. For a graph the area is $\int_\Omega\sqrt{1+|\nabla u|^2}dx$ and its Euler–Lagrange equation is the minimal surface equation $\nabla\cdot(\nabla u/\sqrt{1+|\nabla u|^2})=0$, a quasilinear elliptic equation whose ellipticity degenerates as the gradient grows; a gradient estimate, exponential in the supremum of $u$, restores the regularity theory. The classical examples are the plane, the catenoid, the helicoid, Scherk's surfaces and Enneper's surface; the catenoid is the only minimal surface of revolution besides the plane, and the helicoid is the only ruled one besides the plane.

Plateau's problem asks for a minimal disc spanning a Jordan curve and is solved by Douglas and Radó, who minimise the energy over maps of the disc and show that a minimiser is conformal and hence minimal; the solution is analytic in the interior, an immersion away from finitely many branch points, and regular at a smooth boundary except possibly at finitely many points. The second variation of area is $\int(|\nabla f|^2-|A|^2f^2)dA$ and defines stability through the Jacobi operator $\Delta+|A|^2$; the plane and the catenoid are stable, the helicoid is not, and a complete stable minimal surface in $\mathbb{R}^3$ is a plane. Bernstein's theorem states that every entire minimal graph in $\mathbb{R}^3$ is a plane; the statement extends to $\mathbb{R}^n$ for $n\le7$ and fails at $n=8$, where the Simons cone is the counterexample. Finally the Weierstrass representation writes every conformal minimal immersion into $\mathbb{R}^3$ as an integral of two holomorphic pieces of data, the Gauss map and a holomorphic $1$-form, and exhibits minimal surfaces as conformal harmonic maps; the general target, where only harmonicity is required, is the subject of the theory of harmonic maps.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M$, $\partial M$ | Two-dimensional surface and its boundary |
| $\phi : M\to\mathbb{R}^n$ | Parametrised immersion |
| $g_{ij}$, $dA$ | Induced metric and area element |
| $A(\phi)$, $E(\phi)$ | Area and energy functionals |
| $H$, $\mathrm{II}$, $|A|^2$ | Mean curvature vector, second fundamental form, its squared norm |
| $V$ | Variational field along $\phi$ |
| $u : \Omega\to\mathbb{R}$ | Function whose graph is a minimal graph |
| minimal surface equation | $\nabla\cdot(\nabla u/\sqrt{1+|\nabla u|^2})=0$ |
| $\Gamma$, $D$ | Jordan curve and disc of Plateau's problem |
| $L$, $A$ | Length of a closed curve and area of a minimal disc |
| $f$, $\nu$ | Normal variation function and unit normal |
| Jacobi operator | $\Delta_M+|A|^2$ |
| stability inequality | $\int|A|^2f^2\le\int|\nabla f|^2$ |
| $(g,\omega)$ | Weierstrass data: Gauss map and holomorphic $1$-form |
| Simons cone | The stable non-flat minimal cone in $\mathbb{R}^8$ |



## Further Reading

- Jesse Douglas, "Solution of the Problem of Plateau", *Transactions of the American Mathematical Society* 33 (1931), for the existence theorem.
- Tibor Radó, *On the Problem of Plateau* (Springer, 1933), for the classical solution of the disc problem.
- Robert Osserman, *A Survey of Minimal Surfaces* (Dover, 2nd ed. 1986), for the Weierstrass representation and the classical examples.
- Johannes C. C. Nitsche, *Lectures on Minimal Surfaces* (Cambridge University Press, 1989), for the boundary regularity and the Plateau problem.
- Enrico Bombieri, Ennio De Giorgi and Enrico Giusti, "Minimal Cones and the Bernstein Problem", *Inventiones Mathematicae* 7 (1969), for the dimension threshold.
- Manfredo do Carmo and Chia-Kuei Peng, "Stable Complete Minimal Surfaces in $\mathbb{R}^3$ are Planes", *Bulletin of the American Mathematical Society* 1 (1979), for the stability classification.
- Doris Fischer-Colbrie and Richard Schoen, "The Structure of Complete Stable Minimal Surfaces in 3-Manifolds of Non-Negative Scalar Curvature", *Communications on Pure and Applied Mathematics* 33 (1980), for the stable case.
- Leon Simon, *Lectures on Geometric Measure Theory* (Australian National University, 1983), for the measure-theoretic existence and regularity theory.
- Tobias H. Colding and William P. Minicozzi II, *A Course in Minimal Surfaces* (American Mathematical Society, 2011), for a modern unified treatment.
