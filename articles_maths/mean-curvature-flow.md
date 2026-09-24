
# __Mean Curvature Flow__

## Introduction

Mean curvature flow is the evolution of a hypersurface in the direction of its normal with speed equal to its mean curvature:

$$
\frac{\partial F}{\partial t} = -H\nu ,
$$

where $F : M^n\times[0,T)\to\mathbb{R}^{n+1}$ is a family of immersions of a fixed manifold, $\nu$ is a choice of unit normal and $H$ is the mean curvature in that normal direction. The equation moves each point of the surface inward where the surface is convex, with a speed proportional to the curvature, and it is the negative gradient flow of the area functional: the first variation of area is minus the integral of the normal variation against the mean curvature, as computed in the article on minimal surfaces, so the steepest descent of the area is exactly this flow. Its stationary points are the minimal surfaces, its simplest exact solutions are the shrinking spheres and cylinders, and its singularities are resolved by self-similar solitons — all of them objects of the minimal surface theory of this Part.

The flow is a quasilinear parabolic equation for the hypersurface, and for a surface described as a graph it becomes the explicit equation

$$
\frac{\partial u}{\partial t} = \sqrt{1+|\nabla u|^2}\,\operatorname{div}\left(\frac{\nabla u}{\sqrt{1+|\nabla u|^2}}\right),
$$

whose stationary solutions are the minimal graphs. The parabolic character makes the flow well posed for smooth initial data, the maximum principle governs the evolution of the curvature, the area decreases monotonically and a monotone quantity localises the singularities, and the blow-up limits of the singularities are the self-shrinkers. The theory is analogous at every stage to the Ricci flow of the preceding article: the curvature evolves by a reaction-diffusion equation, the maximum principle controls it, a monotone functional excludes collapse, and the singular models are the self-similar solutions. What is different is the ambient setting and the object that evolves: here a submanifold in a fixed space, there a metric on a fixed manifold.

The article treats the definition and the first variation; the graph equation and the curve shortening flow, with the classical theorems of Gage–Hamilton and Grayson; the evolution of the area and of the curvature, with the maximum principle and Huisken's pinching theorem that convex surfaces shrink to round points; the singularity theory, with the definition of self-shrinkers, the monotonicity of the Gaussian area and the tangent flows; the weak solutions of the level-set and varifold theories for nonsmooth data; and the relation to minimal surfaces, with the parabolic analogue of the stability theory. The Riemannian geometry of the ambient space is that of Part II, cited and not re-derived; the functional-analytic background is the semigroup theory of the preceding articles of this Part.

## The Flow and the First Variation

**Definition.** Let $M$ be a compact $n$-dimensional manifold (possibly with boundary) and let $F_0 : M\to\mathbb{R}^{n+1}$ be a smooth immersion. A **mean curvature flow** with initial surface $F_0$ is a smooth family of immersions $F : M\times[0,T)\to\mathbb{R}^{n+1}$ with $F(\cdot,0)=F_0$ and

$$
\frac{\partial F}{\partial t}(x,t) = -H(x,t)\nu(x,t),
$$

where $\nu$ is a unit normal field and $H = \operatorname{tr}\mathrm{II}$ is the mean curvature with respect to $\nu$; the flow is **inward** for a convex surface when $\nu$ is the outward normal.

**Theorem (first variation and the gradient-flow property).** The mean curvature flow is the $L^2$-gradient flow of the area functional: for a variation $F(\cdot,t)$ with variational field $V = \partial_tF$, the first variation of the area is

$$
\frac{d}{dt}\operatorname{Area}(F(\cdot,t)) = -\int_M H\,(V\cdot\nu)\,dA ,
$$

and the choice $V = -H\nu$ makes the area decrease at the maximal rate, giving

$$
\frac{d}{dt}\operatorname{Area} = -\int_M H^2\,dA \le 0 .
$$

*Proof.* The first variation formula of the article on minimal surfaces gives the derivative as the integral of $V$ against the mean curvature vector with a minus sign; the normal component of $V$ is $V\cdot\nu$ and the tangential part contributes nothing to the first order, because the area is invariant under reparametrisation. Choosing $V=-H\nu$ makes the integrand negative, $-(H)^2$, and Cauchy–Schwarz shows that this choice maximises the rate. $\square$

**Corollary (stationary surfaces).** A surface is stationary for the area if and only if $H\equiv0$; the stationary points of the mean curvature flow are exactly the minimal surfaces.

**Theorem (short-time existence).** For a compact smoothly immersed initial surface $F_0 : M\to\mathbb{R}^{n+1}$ there is $T>0$ and a smooth solution of the mean curvature flow on $[0,T)$; the solution is unique, and it extends beyond $T$ unless the second fundamental form becomes unbounded as $t\to T^-$.

*Proof.* Quoted as standard. The flow is a quasilinear parabolic system for the immersion; the linearisation is the heat operator for the normal component with lower-order terms, and the standard parabolic existence and continuation theory gives the short-time solution and the blow-up criterion. The tangential components of the motion are diffeomorphisms of $M$, so the flow is well defined up to the choice of parametrisation. $\square$

**Example (the shrinking sphere).** For the round sphere of radius $r_0$ in $\mathbb{R}^{n+1}$ the flow is the shrinking family of concentric spheres with radius

$$
r(t) = \sqrt{r_0^2-2nt} ,
$$

which becomes extinct at $T = r_0^2/(2n)$. The solution is self-similar: it is a rescaling of the initial sphere, and its speed at each point is proportional to the curvature.

*Proof.* A sphere of radius $r$ has $H=n/r$ with the outward normal, so the flow moves each point inward with speed $n/r$, and $\dot r=-n/r$; integrating gives $r^2 = r_0^2-2nt$. The exactness of the family is verified by substituting the ansatz into the flow. $\square$

## The Graph Equation and Curve Shortening

**Theorem (the equation for a graph).** If the surface is the graph of a function $u : \Omega\to\mathbb{R}$ and the normal is chosen upward, then the mean curvature flow is

$$
\frac{\partial u}{\partial t} = \sqrt{1+|\nabla u|^2}\,\operatorname{div}\left(\frac{\nabla u}{\sqrt{1+|\nabla u|^2}}\right),
$$

a quasilinear parabolic equation whose principal part is the mean curvature operator and whose stationary equation is the minimal surface equation.

*Proof.* For a graph the unit normal is $\nu = (-\nabla u,1)/\sqrt{1+|\nabla u|^2}$ and the mean curvature with the upward normal is $H = -\operatorname{div}(\nabla u/\sqrt{1+|\nabla u|^2})$. Write $W=\sqrt{1+|\nabla u|^2}$, so that $\nu\cdot e_{n+1}=1/W$. The surface moves with normal velocity $-H$, while the velocity of the parametrisation $\partial_tF=(0,\partial_tu)$ is vertical; its normal component is $\partial_tu/W$, so matching the normal components gives $\partial_tu/W=-H$ and hence

$$
\partial_tu = -HW = W\operatorname{div}\Bigl(\frac{\nabla u}{W}\Bigr),
$$

which is the displayed equation. The equation is parabolic because $\operatorname{div}(\nabla u/W)$ has the Hessian of $u$ as its principal part with the positive definite coefficient matrix $(1/W)(I-\nabla u\otimes\nabla u/W^2)$. $\square$

**Example (curve shortening in the plane).** For a closed embedded curve $\gamma : S^1\to\mathbb{R}^2$ the flow

$$
\frac{\partial\gamma}{\partial t} = \kappa N
$$

with $\kappa$ the curvature and $N$ the inward normal shrinks the curve; a circle of radius $r_0$ shrinks by $r(t)=\sqrt{r_0^2-2t}$ and becomes extinct at $t=r_0^2/2$. The flow is the one-dimensional mean curvature flow, and it is the model case in which the theory is most complete.

**Theorem (Gage–Hamilton, Grayson).** Under curve shortening flow a convex embedded closed plane curve remains convex, shrinks to a point in finite time, after rescaling about the extinction point so that the enclosed area is constant, converges to a round circle; moreover every embedded closed plane curve becomes convex after finite time, so the conclusion holds for arbitrary embedded initial curves.

*Proof.* Quoted as standard (Gage–Hamilton for the convex case, Grayson for the reduction to it). The convexity is preserved by the maximum principle applied to the curvature, which satisfies $\partial_t\kappa = \kappa_{ss}+\kappa^3$ in the arclength parameter $s$; the convergence to a circle uses the monotonicity of an isoperimetric ratio; the elimination of the non-convex case is a separate argument controlling the number of inflections. $\square$

**Remark (non-embedded curves and singularities).** An immersed but non-embedded plane curve need not become convex: a figure-eight curve shrinks to a crossing point and the flow becomes singular there before extinction, the crossing point forming a self-similar singularity. The example shows that the global regularity conclusion of Grayson's theorem is a property of embeddedness, and it is the first indication that the flow can develop a singularity whose model is not the shrinking circle.

## Evolution of Area and Curvature

**Theorem (evolution of the curvature).** Along a mean curvature flow of hypersurfaces in $\mathbb{R}^{n+1}$,

$$
\frac{\partial H}{\partial t} = \Delta H + H|A|^2 , \qquad
\frac{\partial |A|^2}{\partial t} = \Delta|A|^2 - 2|\nabla A|^2 + 2|A|^4 ,
$$

where $|A|^2$ is the squared norm of the second fundamental form and $\Delta$ is the Laplace–Beltrami operator of the evolving surface; in a general ambient Riemannian manifold the equation for $H$ acquires the additional term $H\,\mathrm{Ric}(\nu,\nu)$.

*Proof.* Quoted as standard (Huisken). The computations differentiate the structure equations of the immersion with respect to time, using the evolution of the induced metric and of the normal; the reaction terms are quadratic in the second fundamental form, as required by scaling, and the term $-2|\nabla A|^2$ in the second equation is what makes the maximum principle for $|A|^2$ effective. $\square$

**Corollary (the maximum principle for the curvature).** Along a mean curvature flow, $\max_MH$ is nonincreasing and $\min_MH$ is nondecreasing when $H$ is signed appropriately, so a strictly convex initial hypersurface remains strictly convex; the corresponding statement for $|A|^2$ requires the pinching cone used in Huisken's theorem below.

*Proof.* The equation $\partial_tH=\Delta H+H|A|^2$ is a differential inequality $\partial_t H\ge\Delta H+H|A|^2$ whose zeroth-order term has a definite sign when $H$ has a definite sign; the maximum principle applied to $-H$ gives the nonincrease of the maximum, and the minimum is treated by the same argument with the sign of the reaction term reversed. $\square$

**Theorem (Huisken's pinching theorem).** Let $F_0 : M^n\to\mathbb{R}^{n+1}$ be a compact, strictly convex immersed hypersurface. Then the mean curvature flow becomes extinct at a finite time $T$, and, after rescaling about the extinction point so that the enclosed volume is constant,

$$
|A|^2 - \frac1nH^2 \longrightarrow 0 \qquad \text{and} \qquad \frac{H^2}{n|A|^2}\longrightarrow1 ,
$$

so the rescaled surfaces converge to a round sphere; consequently $M$ is diffeomorphic to $S^n$.

*Proof.* Quoted as standard (Huisken 1984). The maximum principle is applied to the quantity $|A|^2/H^2 - 1/n$, whose evolution is a reaction-diffusion equation with a favourable reaction term for a convex surface; the estimate gives the pinching, and the convergence of the rescaled surfaces to a sphere follows from the pinching together with the area bound and the compactness of immersions with bounded curvature. $\square$

**Theorem (finiteness of the extinction).** A compact mean curvature flow cannot exist for all time with the curvature bounded; the flow either becomes extinct at a finite time or its curvature becomes unbounded at a finite time. For a closed convex plane curve the extinction is finite, and the extinction time is bounded above in terms of the initial area, the bound being attained by the circle.

*Proof.* The decrease of the area is the first variation formula. The extinction statements are quoted as standard: for curves, the Gauss–Bonnet theorem turns the decrease of the area into a lower bound for the rate of decrease, and integrating gives the finite extinction time; in higher dimension the corresponding statement is that a bounded-curvature solution on a finite time interval can be extended, which is the continuation criterion of the short-time existence theorem. $\square$

## Singularities and Self-Shrinkers

**Definition.** A **self-shrinker** is a hypersurface $M\subseteq\mathbb{R}^{n+1}$ satisfying

$$
H - \frac12\langle x,\nu\rangle = 0 ,
$$

the equation of a surface that moves by homothetic contraction along the radial vector field, with the same normal convention as in the flow; a **self-expander** satisfies $H+\frac12\langle x,\nu\rangle=0$ and a **translator** satisfies $H+\langle v,\nu\rangle=0$ for a fixed vector $v$. These are the self-similar solutions of the mean curvature flow: a self-shrinker generates the solution $F(x,t)=\sqrt{c-t}\,x$ for $t<c$, a translator generates $F(x,t)=x+tv$.

**Example (spheres, cylinders and other shrinkers).** The round sphere $S^n(\sqrt{2n})$ is a self-shrinker: with the outward normal one has $H=n/r$ and $\frac12\langle x,\nu\rangle=r/2$, and the equation $n/r=r/2$ gives $r^2=2n$; the sphere generates the shrinking sphere of the previous sections. The cylinder $S^k(\sqrt{2k})\times\mathbb{R}^{n-k}$ is a self-shrinker and is the model of a neck singularity; the **Angenent torus** is an embedded self-shrinking torus in $\mathbb{R}^3$, and there are further shrinkers obtained from algebraic and variational constructions.

**Theorem (Huisken's monotonicity).** For a mean curvature flow $F(\cdot,t)$ on $[0,T)$ and a point $x_0$ with $t_0>T$, the **Gaussian area**

$$
\Phi_{x_0,t_0}(t) = \int_M (4\pi(t_0-t))^{-n/2}\exp\left(-\frac{|F(x,t)-x_0|^2}{4(t_0-t)}\right)dA
$$

is nonincreasing in $t$, and it is constant exactly when the flow is a self-shrinker centred at $(x_0,t_0)$.

*Proof.* Quoted as standard (Huisken). The derivative of $\Phi$ is a sum of a nonnegative term and a perfect square built from the self-shrinker equation; integrating by parts gives
$\frac{d}{dt}\Phi_{x_0,t_0} = -\int_M\left|H-\frac{\langle F-x_0,\nu\rangle}{2(t_0-t)}\right|^2(4\pi(t_0-t))^{-n/2}e^{-|F-x_0|^2/4(t_0-t)}dA\le0$,
which also identifies the equality case. $\square$

**Theorem (blow-up limits are self-shrinkers).** Let $F$ be a mean curvature flow that becomes singular at $T<\infty$, let $(x_j,t_j)$ be a sequence of points and times with $t_j\to T$ along which the curvature is maximal at the scale of the blow-up, and rescale the flow about $(x_j,t_j)$ by the factor $|A|(x_j,t_j)$. Then every smooth limit of the rescaled flows, after passing to a subsequence, is a self-shrinker (for a Type I singularity); for a Type II singularity the limit is an ancient solution which, in the generic case, is a translator.

*Proof.* Quoted as standard (Huisken, Ilmanen and others). The monotonicity of the Gaussian area is applied to the rescaled flows: the Gaussian area of the blow-up sequence is bounded by the initial value, which gives the local area bounds needed for compactness; the limit flow has a Gaussian area that is constant in time, and the equality case of the monotonicity theorem makes it a self-shrinker. $\square$

**Remark (neckpinch and dumbbell).** For a dumbbell surface in $\mathbb{R}^3$ — two large spheres joined by a thin neck — the flow shrinks the neck faster than the spheres, and the neck pinches off at a point where the curvature blows up; the blow-up limit is the cylinder $S^1\times\mathbb{R}$, the basic nonspherical self-shrinker, and after the pinch the flow continues as two components. The example is the prototype of a singularity that the level-set and varifold weak solutions handle, and it is the reason the strong solutions of the smooth theory require a hypothesis such as convexity or mean convexity.

## Weak Solutions

**Definition.** A **level-set flow** is a weak solution of the mean curvature flow defined by the evolution of a function $u : \mathbb{R}^{n+1}\times[0,\infty)\to\mathbb{R}$ whose level sets are the evolving surfaces; it is given by the **viscosity solution** of the degenerate parabolic equation

$$
u_t = |\nabla u|\operatorname{div}\left(\frac{\nabla u}{|\nabla u|}\right),
$$

which is the level-set form of the flow and which is independent of the choice of $u$ differing by a monotone reparametrisation.

**Theorem (well-posedness of the level-set flow).** For every continuous $u_0$ that changes sign, the level-set equation has a unique viscosity solution, and the zero level set agrees with the classical mean curvature flow wherever the latter is smooth; the solution is stable under the addition of a small constant, which selects the level set in the sense of an evolution of closed sets.

*Proof.* Quoted as standard (Evans–Spruck, Chen–Giga–Goto). The equation is degenerate parabolic and is understood in the viscosity sense; the comparison principle for viscosity solutions gives uniqueness, and the agreement with the smooth flow follows from the fact that the smooth immersion satisfies the equation after composition with a suitable reparametrisation. $\square$

**Remark (varifold solutions).** An alternative weak formulation is that of **Brakke**, in which the flow is a family of varifolds satisfying the transport inequality for the area; the Brakke flow exists for a large class of initial data, it is the natural setting for the monotonicity of the Gaussian area, and the two weak theories agree where both are defined. The varifold setting is the measure-theoretic one, and the regularity theory that upgrades a weak solution to a smooth one away from a small singular set belongs to the geometric measure theory of this Part.

## Relation to Minimal Surfaces and Stability

**Remark (the parabolic analogue of minimal surface theory).** The mean curvature flow is to the minimal surface equation as the heat equation is to Laplace's equation: the stationary solutions of the flow are the minimal surfaces, and the flow selects a minimal surface as its large-time limit when such a limit exists, exactly as the heat flow selects a harmonic function. The second variation of the area, which defines stability for a minimal surface, has a parabolic counterpart: the linearisation of the flow about a minimal surface is the heat equation for the normal component with the potential $|A|^2$,

$$
\partial_tf = \Delta f + |A|^2f ,
$$

whose stability is decided by the sign of the Jacobi operator of the minimal surface theory. A stable minimal surface is thus linearly stable under the flow, and an unstable one has growing normal modes; the helicoid is the standard instance on the unstable side, and the detailed correspondence between the spectral properties of $\Delta+|A|^2$ and the linear stability of the flow is the bridge between the two articles.

**Remark (related flows).** The mean curvature flow is one of a family of geometric evolution equations. The curve shortening flow is its one-dimensional case; the **inverse mean curvature flow**, in which the speed is $1/H$ and the area increases, is used in the study of the mass of an asymptotically flat manifold; the **Willmore flow** decreases the functional $\int H^2dA$ and has the Willmore surfaces as stationary points. Each is a parabolic evolution of a submanifold with a self-similar singularity theory of its own, and the pattern — gradient flow, curvature evolution, maximum principle, monotone quantity, solitons — is the same as in the Ricci flow of the preceding article.

## Summary

Mean curvature flow moves a hypersurface in the direction of its normal with speed equal to the mean curvature, and it is the $L^2$-gradient flow of the area, which decreases at the rate $-\int H^2dA$; its stationary surfaces are the minimal surfaces. For a graph the equation is $u_t=\sqrt{1+|\nabla u|^2}\operatorname{div}(\nabla u/\sqrt{1+|\nabla u|^2})$, a quasilinear parabolic equation; in two dimensions the curve shortening flow shrinks a circle by $r(t)=\sqrt{r_0^2-2t}$ and, by the theorems of Gage–Hamilton and Grayson, shrinks every embedded closed plane curve to a round point. The curvature evolves by $\partial_tH=\Delta H+H|A|^2$ and $\partial_t|A|^2=\Delta|A|^2-2|\nabla A|^2+2|A|^4$, the maximum principle controls the flow of a convex surface, and Huisken's theorem states that a compact strictly convex hypersurface becomes extinct in finite time and converges, after rescaling, to a round sphere. Singularities are modelled by the self-similar solutions: the self-shrinkers satisfy $H-\frac12\langle x,\nu\rangle=0$, the sphere $S^n(\sqrt{2n})$ and the cylinder $S^k(\sqrt{2k})\times\mathbb{R}^{n-k}$ being the basic examples; Huisken's monotonicity of the Gaussian area localises the singularities, and the blow-up limits of a Type I singularity are self-shrinkers, while the dumbbell neckpinch is the prototype that requires the weak theories. The level-set and Brakke varifold formulations provide well-posed weak solutions for nonsmooth data, and the linearisation about a minimal surface is the heat equation with potential $|A|^2$, which ties the stability theory of minimal surfaces to that of the flow.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F(x,t)$, $M$, $n$ | Evolving immersion, its manifold and dimension |
| $\nu$, $H$ | Unit normal and mean curvature |
| $\partial_tF=-H\nu$ | Mean curvature flow equation |
| $\mathrm{II}$, $A$, $|A|^2$ | Second fundamental form, its squared norm |
| $dA$ | Area element; $\frac{d}{dt}\operatorname{Area}=-\int H^2dA$ |
| $u(x,t)$ | Graph function; graph mean curvature equation |
| $\kappa$, $N$ | Curvature and normal of a plane curve |
| $\Delta$ | Laplace–Beltrami operator of the evolving surface |
| self-shrinker | $H-\frac12\langle x,\nu\rangle=0$; centre of self-similarity |
| translator | $H+\langle v,\nu\rangle=0$ |
| $\Phi_{x_0,t_0}$ | Huisken's Gaussian area, monotone in $t$ |
| level-set equation | $u_t=|\nabla u|\operatorname{div}(\nabla u/|\nabla u|)$ |
| Brakke flow | Varifold weak solution of the flow |



## Further Reading

- Gerhard Huisken, "Flow by Mean Curvature of Convex Surfaces into Spheres", *Journal of Differential Geometry* 20 (1984), for the curvature evolution and the pinching theorem.
- Gerhard Huisken, "Asymptotic Behavior for Singularities of the Mean Curvature Flow", *Journal of Differential Geometry* 31 (1990), for the monotonicity of the Gaussian area and the self-shrinker analysis.
- Matthew A. Grayson, "The Heat Equation Shrinks Embedded Plane Curves to Round Points", *Journal of Differential Geometry* 26 (1987), and Michael E. Gage and Richard S. Hamilton, "The Heat Equation Shrinking Convex Plane Curves", *Journal of Differential Geometry* 23 (1986), for the curve shortening theorems.
- Kenneth A. Brakke, *The Motion of a Surface by Its Mean Curvature* (Princeton University Press, 1978), for the varifold weak solution.
- Lawrence C. Evans and Joel Spruck, "Motion of Level Sets by Mean Curvature I", *Journal of Differential Geometry* 33 (1991), and Yun-Gang Chen, Yoshikazu Giga and Shun'ichi Goto, "Uniqueness and Existence of Viscosity Solutions of Generalized Mean Curvature Flow Equations", *Journal of Differential Geometry* 33 (1991), for the level-set formulation.
- Klaus Ecker, *Regularity Theory for Mean Curvature Flow* (Birkhäuser, 2004), for the local regularity and the blow-up analysis.
- Xianglong Li and collaborators, and Tobias H. Colding and William P. Minicozzi II, "Generic Mean Curvature Flow I: Generic Singularities", *Annals of Mathematics* 175 (2012), for the classification of generic singularities.
- Sigurd Angenent, "Shrinking Doughnuts", in *Nonlinear Diffusion Equations and Their Equilibrium States* (Springer, 1992), for the self-shrinking torus.
