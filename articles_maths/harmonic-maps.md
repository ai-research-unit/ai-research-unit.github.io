
# __Harmonic Maps__

## Introduction

A harmonic map is a map between Riemannian manifolds that is a critical point of the energy, the integral of the squared norm of its differential. The notion generalises at once the harmonic functions — the case in which the target is the real line — the geodesics — the case in which the source is a curve — and the minimal surfaces — the case of a conformal map of a surface. The last of these is the reason the theory belongs here: a conformal harmonic map of a surface is a minimal immersion, so the Weierstrass representation of the preceding article is a chapter of the theory of harmonic maps, and the general theory extends it to an arbitrary Riemannian target, where the harmonic map equation is a nonlinear elliptic system and where the geometric properties of the target curvature govern the existence, the regularity and the rigidity of the solutions.

The energy is

$$
E(\digamma_{\mathrm{map}}) = \frac12\int_M|d\digamma_{\mathrm{map}}|^2\,dV_g ,
$$

the norm of the differential being taken with respect to the metric of the source and that of the target. Its Euler–Lagrange operator is the **tension field** $\tau(\digamma_{\mathrm{map}}) = \operatorname{trace}_g\nabla d\digamma_{\mathrm{map}}$, and $\digamma_{\mathrm{map}}$ is harmonic when $\tau(\digamma_{\mathrm{map}})=0$; in local coordinates the equation is

$$
\Delta_g\digamma_{\mathrm{map},\alpha} + g_{ij}\,\Gamma_{\alpha\beta\gamma}(\digamma_{\mathrm{map}})\,\partial/\partial x_i\,\digamma_{\mathrm{map},\beta}\partial/\partial x_j\,\digamma_{\mathrm{map},\gamma} = 0 ,
$$

a semilinear elliptic system whose nonlinearity is quadratic in the gradient and whose coefficients are the Christoffel symbols of the target. The system is the Laplace equation when the target is flat, the geodesic equation when the source is one-dimensional, and the minimal surface equation when the source is a surface and the map is conformal.

The article treats the definition and the first variation, the examples, the existence theory of Eells and Sampson for targets of nonpositive curvature, in which the harmonic map flow deforms a map into a harmonic representative of its homotopy class, the regularity theory, in which harmonic maps from surfaces are always smooth while maps from higher-dimensional domains may have singularities, the Bochner formula and the vanishing theorems it gives, and the second variation and stability. The Riemannian structures of the source and the target, their Laplacians and their curvature tensors, are those of Part II, and the variational techniques are those of the calculus of variations of this Part; the conformal case is the minimal surface theory of the preceding article, and the parabolic evolution of a map is treated here only as the harmonic map flow, the mean curvature flow of a surface being a separate subject.

## The Energy and the Tension Field

### Definitions

**Definition.** Let $(M,g)$ and $(N,h)$ be Riemannian manifolds, $M$ compact and without boundary unless stated, and let $\digamma_{\mathrm{map}} : M \to N$ be a map of class $C^1$. The **energy** of $\digamma_{\mathrm{map}}$ is

$$
E(\digamma_{\mathrm{map}}) = \frac12\int_M|d\digamma_{\mathrm{map}}|^2\,dV_g, \qquad |d\digamma_{\mathrm{map}}|^2 = \sum_{i,j,\alpha,\beta}(g^{-1})_{ij}(x)\,h_{\alpha\beta}(\digamma_{\mathrm{map}}(x))\,\partial/\partial x_i\,\digamma_{\mathrm{map},\alpha}\,\partial/\partial x_j\,\digamma_{\mathrm{map},\beta} ,
$$

in local coordinates $x$ on $M$ and $\digamma_{\mathrm{map}}$ on $N$; a map with finite energy is an element of the Sobolev space $W^{1,2}(M,N)$ of maps whose local expressions lie in $W^{1,2}$.

**Definition.** The **tension field** of $\digamma_{\mathrm{map}}$ is the section of the pull-back bundle $\digamma_{\mathrm{map}}^*TN$ defined by

$$
\tau(\digamma_{\mathrm{map}}) = \operatorname{trace}_g(\nabla d\digamma_{\mathrm{map}}) ,
$$

where $\nabla$ is the connection on $T^*M\otimes\digamma_{\mathrm{map}}^*TN$ induced by the Levi-Civita connections of $g$ and $h$. The map is **harmonic** if $\tau(\digamma_{\mathrm{map}})=0$.

**Theorem (first variation and the harmonic map equation).** For every variation $\digamma_{\mathrm{map},t}$ of $\digamma_{\mathrm{map}}$ with variational field $V = \partial/\partial t\,\digamma_{\mathrm{map},t}|_{t=0}$ compactly supported,

$$
\frac{d}{dt}E(\digamma_{\mathrm{map},t})\Bigr|_{t=0} = -\int_M h\bigl(\tau(\digamma_{\mathrm{map}}),V\bigr)dV_g .
$$

Hence $\digamma_{\mathrm{map}}$ is a critical point of the energy if and only if $\tau(\digamma_{\mathrm{map}})=0$, and in local coordinates this is the system

$$
\boxed{\;\Delta_g\digamma_{\mathrm{map},\alpha} + g_{ij}\,\Gamma_{\alpha\beta\gamma}(\digamma_{\mathrm{map}})\,\partial/\partial x_i\,\digamma_{\mathrm{map},\beta}\partial/\partial x_j\,\digamma_{\mathrm{map},\gamma} = 0, \qquad \alpha = 1,\dots,\dim N\;} ,
$$

where $\Delta_g$ is the Laplace–Beltrami operator of $(M,g)$ and $\Gamma$ the Christoffel symbols of $(N,h)$.

*Proof.* The derivative of the energy is

$$
\frac{d}{dt}E(\digamma_{\mathrm{map},t})\Bigr|_{t=0} = \int_M \sum_{i,j,\alpha,\beta}(g^{-1})_{ij}h_{\alpha\beta}\bigl(\partial/\partial x_i\,V_\alpha\partial/\partial x_j\,\digamma_{\mathrm{map},\beta} + \dots\bigr) ,
$$

and integrating by parts on $M$, which has no boundary or on which $V$ vanishes, produces the integral of $V$ against the trace of $\nabla d\digamma_{\mathrm{map}}$ with the sign displayed; the arbitrariness of $V$ gives the equation.

**Proposition (the three classical cases).** If $N = \mathbb{R}$ then harmonicity is $\Delta_gu=0$, the harmonic functions; if $M = \mathbb{R}$ or $S^1$ then harmonicity is the geodesic equation of $(N,h)$; if $\dim M = 2$ and $\digamma_{\mathrm{map}}$ is a conformal immersion then harmonicity is the vanishing of the mean curvature of the image, so the image is a minimal surface.

*Proof.* The first two are immediate from the coordinate form, in which the Christoffel term vanishes for a flat target and the Laplace term vanishes for a one-dimensional source. For the third, the energy of a conformal immersion agrees with the area, $E(\digamma_{\mathrm{map}})=A(\digamma_{\mathrm{map}})$, so critical points of the energy are critical points of the area in the conformal class, which are the minimal surfaces by the first variation formula of the preceding article.

### Examples

**Example (the identity and the inclusion).** The identity map of a Riemannian manifold is harmonic exactly when the manifold is a harmonic Riemannian manifold; more importantly, the identity map of $S^m$ with its round metric is harmonic because $\nabla d\digamma_{\mathrm{map}} = 0$ for the identity and the tension field is the trace of a tensor that vanishes. An isometric immersion is harmonic exactly when its image is minimal, by the conformal case above.

**Example (holomorphic maps).** If $M$ and $N$ are Kähler manifolds and $\digamma_{\mathrm{map}}$ is holomorphic, then the energy splits as $E(\digamma_{\mathrm{map}}) = \int|\partial\digamma_{\mathrm{map}}|^2 = \tfrac12\int|d\digamma_{\mathrm{map}}|^2$ and the $(1,1)$-type part of $\nabla d\digamma_{\mathrm{map}}$ is constrained by the Cauchy–Riemann equations; the tension field vanishes because the holomorphic part contributes nothing and the antiholomorphic part vanishes identically. Hence a holomorphic map between Kähler manifolds is harmonic, and a holomorphic map of Riemann surfaces is a minimal branched immersion after composition with a conformal parametrisation of its image.

**Example (maps into a sphere).** For $\digamma_{\mathrm{map}} : M \to S^n\subset\mathbb{R}^{n+1}$ the tension field is $\tau(\digamma_{\mathrm{map}}) = \Delta\digamma_{\mathrm{map}} + |d\digamma_{\mathrm{map}}|^2\digamma_{\mathrm{map}}$, so the harmonic map equation is

$$
\Delta\digamma_{\mathrm{map}} + |d\digamma_{\mathrm{map}}|^2\digamma_{\mathrm{map}} = 0 ,
$$

an equation in which the nonlinearity is the second derivative of the constraint $|\digamma_{\mathrm{map}}|^2=1$; for $M=S^2$ it is equivalent to the equation satisfied by the eigenfunctions of the Laplacian, and every nontrivial harmonic map $S^2\to S^n$ is a rational curve in a suitable sense.

**Example (a family of maps into the circle).** For $\digamma_{\mathrm{map}} : S^1\to S^1$ of degree $k$, written $\digamma_{\mathrm{map}}(\exp(i\theta)) = \exp(ik\theta)$, the energy is $E = \pi k^2$ and the map is harmonic for every $k$, since the geodesic equation on the circle is solved by the constant-speed parametrisations; the example shows that on a curved target there are harmonic maps of arbitrarily large energy, in contrast with the flat case where harmonic maps are rigid.

## Existence: the Harmonic Map Flow

### The Flow and Its Short-Time Behaviour

**Definition.** The **harmonic map flow** with initial map $\digamma_{\mathrm{map},0}$ is the parabolic system

$$
\frac{\partial\digamma_{\mathrm{map},t}}{\partial t} = \tau(\digamma_{\mathrm{map},t}), \qquad \digamma_{\mathrm{map},0} = \digamma_{\mathrm{map}} ,
$$

a section equation for $\digamma_{\mathrm{map}} : M\times[0,T)\to N$; it is the gradient flow of the energy with respect to the $L^2$ metric on the space of maps.

**Theorem (short-time existence).** If $N$ is compact and $\digamma_{\mathrm{map},0} \in W^{1,2}(M,N)$ with $M$ compact, then the harmonic map flow has a solution on a maximal interval $[0,T_*)$ with $T_* = \infty$ or with the energy and the gradient blowing up as $t\to T_*^-$; the solution is smooth for $t>0$.

*Proof.* The equation is quasilinear parabolic after choosing a suitable gauge, and the linearisation is the heat equation coupled to a first-order term; the standard parabolic existence theory gives a smooth short-time solution, and the maximal interval follows from the same continuation argument as for an ordinary equation.

### The Eells–Sampson Theorem

**Theorem (Eells–Sampson).** Let $M$ be a compact Riemannian manifold and let $N$ be a complete Riemannian manifold of nonpositive sectional curvature. Then every continuous map $\digamma_{\mathrm{map},0} : M\to N$ is homotopic to a harmonic map, and the harmonic map flow starting from any smooth $\digamma_{\mathrm{map},0}$ exists for all time and converges to a harmonic map in the homotopy class of $\digamma_{\mathrm{map},0}$.

*Proof.* The energy is nonincreasing along the flow, $\frac{d}{dt}E(\digamma_{\mathrm{map},t}) = -\int|\tau(\digamma_{\mathrm{map},t})|^2\le0$, so the flow stays in a bounded energy class. For a target of nonpositive curvature the **Bochner estimate** for the flow,

$$
\boxed{\;\frac{\partial}{\partial t}|d\digamma_{\mathrm{map}}|^2 - \Delta|d\digamma_{\mathrm{map}}|^2 \le -C|d\digamma_{\mathrm{map}}|^4 + C'|d\digamma_{\mathrm{map}}|^2\;} ,
$$

bounds the gradient in terms of the energy, and the maximum principle then gives uniform gradient bounds independent of $t$. The higher derivatives are bounded by the parabolic regularity theory, and a subsequence converges to a limit map whose tension field vanishes, since $\int_0^\infty\|\tau(\digamma_{\mathrm{map},t})\|^2dt < \infty$ forces a sequence $t_j\to\infty$ with $\tau(\digamma_{\mathrm{map},t_j})\to0$.

**Corollary (existence of harmonic representatives).** In each homotopy class of maps $M\to N$ with $N$ compact and nonpositively curved there is a harmonic map, and the harmonic map minimises the energy in its class; for $N$ a compact quotient of a symmetric space of noncompact type the minimiser is unique with respect to the action of the isometry group.

*Proof.* The flow converges in the given class; a limit of the flow is critical and, by the convexity of the energy along geodesic homotopies of an NPC target, it is the minimiser. Uniqueness follows from the strict convexity of the distance-squared function on an NPC space.

**Remark (the positive-curvature case).** For a positively curved target the flow can develop a singularity in finite time and the energy can concentrate; the existence of harmonic maps in a given homotopy class then depends on the class, and there are classes with more than one harmonic representative. The flow through a singularity is the object of the general theory of the harmonic map flow, and the bubbling analysis at the singularity is the source of the compactness theorem below.

## Regularity and Singularities

**Theorem (regularity in dimension two).** Let $\dim M = 2$ and let $\digamma_{\mathrm{map}} \in W^{1,2}(M,N)$ be a weak harmonic map into a compact target, that is, a weak solution of $\tau(\digamma_{\mathrm{map}})=0$. Then $\digamma_{\mathrm{map}}$ is smooth.

*Proof.* Quoted as standard (Morrey's regularity for harmonic maps from surfaces). The equation is conformally invariant in dimension two, so the energy controls the modulus of continuity: a decay of the energy over small balls implies a Hölder bound for the map (the **Morrey lemma**), while a concentration of energy would create a bubble whose existence is excluded by the energy gap of a harmonic sphere. The bootstrap then gives $C^\infty$, and the argument is the two-dimensional case of the general theory.

**Theorem (partial regularity).** Let $\dim M = m\ge3$ and let $\digamma_{\mathrm{map}} \in W^{1,2}(M,N)$ be a weak harmonic map. Then there is a closed set $\Sigma \subseteq M$ of Hausdorff dimension at most $m-3$ such that $\digamma_{\mathrm{map}}$ is smooth on $M\setminus\Sigma$; in particular for $m=3$ the singular set is discrete. The result is sharp: the map $x\mapsto x/|x|$ from $B^3\subset\mathbb{R}^3$ to $S^2$ is harmonic away from the origin and is not continuous there.

*Proof.* Quoted as standard (Schoen–Uhlenbeck partial regularity). The proof introduces a monotone quantity (the normalised energy), shows its convergence at small scales, and uses the epsilon-regularity theorem: a point at which the normalised energy is small is a regular point, so the singular set is contained in the set of points where the energy does not decay, whose dimension is bounded by the codimension argument.

**Theorem (energy gap and compactness).** There is a constant $\varepsilon_0>0$, depending only on the target, such that a harmonic map $\digamma_{\mathrm{map}} : S^2\to N$ with $E(\digamma_{\mathrm{map}})<\varepsilon_0$ is constant; consequently the bubbling of a sequence of harmonic maps can occur only at points of energy concentration, and the bubbles are harmonic maps of $S^2$ with energy bounded below by $\varepsilon_0$ (Sacks–Uhlenbeck).

*Proof.* Quoted as standard. The gap follows from the regularity theorem applied to the conformally rescaled map: an energy below $\varepsilon_0$ on $S^2$ gives estimates on the whole sphere, and the only such harmonic maps are constant.

## The Bochner Formula and Rigidity

**Theorem (Bochner formula for maps).** For a harmonic map $\digamma_{\mathrm{map}} : (M,g)\to(N,h)$,

$$
\boxed{\;\frac12\Delta|d\digamma_{\mathrm{map}}|^2 = |\nabla d\digamma_{\mathrm{map}}|^2 + \bigl\langle d\digamma_{\mathrm{map}},\operatorname{Ric}^M\bigr\rangle - \bigl\langle R^N(d\digamma_{\mathrm{map}},d\digamma_{\mathrm{map}})d\digamma_{\mathrm{map}},d\digamma_{\mathrm{map}}\bigr\rangle\;} ,
$$

where the inner products contract the appropriate pairs of indices, $\operatorname{Ric}^M$ is the Ricci curvature of the source and $R^N$ the Riemann curvature tensor of the target.

*Proof.* The identity is the Weitzenböck formula applied to the bundle-valued $1$-form $d\digamma_{\mathrm{map}}$, combined with the harmonicity equation $\operatorname{trace}\nabla d\digamma_{\mathrm{map}} = 0$, which eliminates the term involving the divergence; the curvature terms are those of the source and the pull-back of the target connection.

**Theorem (Eells–Wood vanishing).** Let $M$ be compact with $\operatorname{Ric}^M\ge0$ and let $N$ have nonpositive sectional curvature. Then every harmonic map $\digamma_{\mathrm{map}} : M\to N$ is totally geodesic; if in addition $\operatorname{Ric}^M>0$ at some point, $\digamma_{\mathrm{map}}$ is constant.

*Proof.* In the Bochner formula the source term $\langle d\digamma_{\mathrm{map}},\operatorname{Ric}^M\rangle\ge0$ and the target term $-\langle R^N(d\digamma_{\mathrm{map}},d\digamma_{\mathrm{map}})d\digamma_{\mathrm{map}},d\digamma_{\mathrm{map}}\rangle\ge0$ by the sign of the target curvature; hence $\Delta|d\digamma_{\mathrm{map}}|^2\ge0$ and $|d\digamma_{\mathrm{map}}|^2$ is subharmonic on a compact manifold, so it is constant, and $\nabla d\digamma_{\mathrm{map}}=0$. Under the strict positivity of the Ricci curvature the same computation forces $d\digamma_{\mathrm{map}}=0$.

**Corollary (harmonic maps from spheres).** A harmonic map $\digamma_{\mathrm{map}} : S^m\to N$ with $m\ge2$ into a manifold of nonpositive sectional curvature is constant.

*Proof.* The round sphere has $\operatorname{Ric}^{S^m} = (m-1)g>0$, so the strict form of the vanishing theorem applies.

## Second Variation and Stability

**Definition.** Let $\digamma_{\mathrm{map}}$ be a harmonic map and let $V$ be a variational field along $\digamma_{\mathrm{map}}$ (a section of $\digamma_{\mathrm{map}}^*TN$). The **index form** or **Hessian** of the energy at $\digamma_{\mathrm{map}}$ is

$$
H_\digamma_{\mathrm{map}}(V,V) = \int_M\Bigl(|\nabla V|^2 - \sum_{i=1}^{m}h\bigl(R^N(V,d\digamma_{\mathrm{map}}(e_i))d\digamma_{\mathrm{map}}(e_i),V\bigr)\Bigr)dV_g ,
$$

where $(e_i)$ is a $g$-orthonormal frame and $\nabla$ the connection along $\digamma_{\mathrm{map}}$. The map is **stable** if $H_\digamma_{\mathrm{map}}(V,V)\ge0$ for every compactly supported $V$, and the **index** is the number of negative directions in a maximal negative subspace.

**Theorem (second variation).** The second derivative of the energy along a variation with field $V$ is $\frac{d^2}{dt^2}E(\digamma_{\mathrm{map},t})|_{t=0} = H_\digamma_{\mathrm{map}}(V,V)$; consequently a stable harmonic map is a local minimum of the energy, and a harmonic map with negative index is not.

*Proof.* Expanding the energy to second order in the variation and integrating by parts, the first-order term vanishes by harmonicity and the second-order term is the displayed quadratic form, the curvature term arising from the second derivative of the target metric along the geodesic from $\digamma_{\mathrm{map}}(x)$ in the direction $V(x)$.

**Example (maps into a sphere).** For $\digamma_{\mathrm{map}} : M \to S^n$ the second variation simplifies to

$$
H_\digamma_{\mathrm{map}}(V,V) = \int_M\Bigl(|\nabla V|^2 - |d\digamma_{\mathrm{map}}|^2|V|^2\Bigr)dV_g ,
$$

with $V$ restricted to be perpendicular to $\digamma_{\mathrm{map}}$. The identity map of $S^m$ is unstable for every $m\ge2$: the variations induced by the conformal vector fields of the round sphere give null directions, and there are further directions of negative energy, so the index is positive. The computation is the harmonic-map analogue of the instability of a non-minimising geodesic and of the helicoid among minimal surfaces.

## Summary

A harmonic map $\digamma_{\mathrm{map}} : (M,g)\to(N,h)$ is a critical point of the energy $E(\digamma_{\mathrm{map}}) = \frac12\int|d\digamma_{\mathrm{map}}|^2dV_g$, and its Euler–Lagrange equation is the vanishing of the tension field, $\tau(\digamma_{\mathrm{map}}) = \operatorname{trace}_g\nabla d\digamma_{\mathrm{map}} = 0$, which in coordinates reads $\Delta_g\digamma_{\mathrm{map},\alpha} + g_{ij}\Gamma_{\alpha\beta\gamma}\partial/\partial x_i\,\digamma_{\mathrm{map},\beta}\partial/\partial x_j\,\digamma_{\mathrm{map},\gamma}=0$. The theory specialises to harmonic functions for a flat target, to geodesics for a one-dimensional source, and to minimal surfaces for a conformal source of dimension two, and it includes the holomorphic maps between Kähler manifolds. The harmonic map flow $\partial/\partial t\,\digamma_{\mathrm{map}}=\tau(\digamma_{\mathrm{map}})$ is the gradient flow of the energy and is quasilinear parabolic; for a compact target of nonpositive curvature it exists for all time and converges, which is the Eells–Sampson theorem and gives a harmonic representative in every homotopy class. Harmonic maps from surfaces are smooth; from higher-dimensional domains they are smooth off a closed singular set of codimension at least three, and the result is sharp, as the map $x/|x|$ shows in dimension three. The Bochner formula for the energy density combines the Ricci curvature of the source and the Riemann curvature of the target and gives the Eells–Wood vanishing theorem; and the second variation defines the index form and stability, the identity map of a sphere being unstable.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(M,g)$, $(N,h)$ | Riemannian source and target |
| $\digamma_{\mathrm{map}} : M\to N$ | Map; local components $\digamma_{\mathrm{map},\alpha}$ |
| $E(\digamma_{\mathrm{map}})$ | Energy $\frac12\int_M|d\digamma_{\mathrm{map}}|^2\,dV_g$ |
| $|d\digamma_{\mathrm{map}}|^2$ | $\sum_{i,j,\alpha,\beta}(g^{-1})_{ij}h_{\alpha\beta}\partial/\partial x_i\,\digamma_{\mathrm{map},\alpha}\partial/\partial x_j\,\digamma_{\mathrm{map},\beta}$ |
| $\tau(\digamma_{\mathrm{map}})$ | Tension field, the trace of $\nabla d\digamma_{\mathrm{map}}$ |
| $\Delta_g$ | Laplace–Beltrami operator of the source |
| $\Gamma_{\alpha\beta\gamma}$ | Christoffel symbols of the target |
| $W^{1,2}(M,N)$ | Sobolev space of finite-energy maps |
| harmonic map flow | $\partial/\partial t\,\digamma_{\mathrm{map}} = \tau(\digamma_{\mathrm{map}})$ |
| $R^N$, $\operatorname{Ric}^M$ | Riemann curvature of the target, Ricci curvature of the source |
| $H_\digamma_{\mathrm{map}}(V,V)$ | Index form (Hessian) of the energy at $\digamma_{\mathrm{map}}$ |
| index, stable | Number of negative directions; $H_\digamma_{\mathrm{map}}\ge0$ |
| $\Sigma$ | Singular set of a weakly harmonic map |

## Further Reading

- James Eells and Joseph H. Sampson, "Harmonic Mappings of Riemannian Manifolds", *American Journal of Mathematics* 86 (1964), for the existence theorem and the harmonic map flow.
- James Eells and Luc Lemaire, *A Report on Harmonic Maps* and its sequels (Cambridge University Press, 1978; 1988), for the state of the theory and the many examples.
- Richard Schoen and Karen Uhlenbeck, "A Regularity Theory for Harmonic Maps", *Journal of Differential Geometry* 17 (1982), for the partial regularity theorem.
- Jonathan Sacks and Karen Uhlenbeck, "The Minimal Immersions of Closed Riemann Surfaces", *Transactions of the American Mathematical Society* 271 (1982), for the bubbling and the energy gap.
- Charles B. Morrey, "The Problem of Plateau on a Riemannian Manifold", *Annals of Mathematics* 49 (1948), for the two-dimensional regularity.
- Frédéric Hélein, *Harmonic Maps, Conservation Laws and Moving Frames* (Cambridge University Press, 2nd ed. 2002), for the direct approach to two-dimensional regularity.
- James Eells and John C. Wood, "Restrictions on Harmonic Maps of Surfaces", *Topology* 15 (1976), for the vanishing and rigidity theorems.
- Richard S. Hamilton, *Harmonic Maps of Manifolds with Boundary* (Springer, 1975), for the boundary value and flow theory.
- Paul Baird and John C. Wood, *Harmonic Morphisms between Riemannian Manifolds* (Oxford University Press, 2003), for the pull-back theory and the morphisms.
