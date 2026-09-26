
# __List of Riemannian Geometries__

## Introduction

This article lists the Riemannian geometries of the corpus: the metrics, the connections they determine, the curvatures those connections carry, the geodesics and the comparison theorems that relate a geometry to the constant-curvature models, and the model spaces and space forms themselves. Every entry points to the article that introduces the notion, and the article introduces nothing and proves nothing.

The list is ordered along the chain by which a Riemannian geometry is built: a metric on a manifold determines a unique torsion-free connection, the connection determines the curvature tensor, the curvature controls the geodesics through the Jacobi equation, and the comparison theorems translate hypotheses on the curvature into statements about the metric. The last section records the model spaces of constant curvature and their space forms, which are the geometries at which the comparison is made, and the Einstein metrics and the Ricci flow, which are the geometries singled out by a condition on the Ricci tensor.

The article records examples and non-examples side by side. Beside the Riemannian geometries it lists the metrics that are indefinite and so Lorentzian or pseudo-Riemannian, the metric spaces that are not Riemannian, the manifolds that fail completeness, and the structures that are not metrics at all, each with the failure named and the article that records it.

## Riemannian Metrics

A Riemannian metric is a smoothly varying positive-definite inner product on each tangent space, and it makes the manifold a metric space by the length functional.

| Object | The property it has | Introduced in |
|---|---|---|
| a Riemannian metric $g$ | a positive-definite symmetric bilinear form on each tangent space, varying smoothly | *Riemannian Geometry* |
| the first fundamental form $ds^2 = \sum_{ij}g_{ij}dx^idx^j$ | the metric in local coordinates | *Riemannian Geometry* |
| the length $L_g(\gamma)$ | the integral of the speed, defining the geometry | *Riemannian Geometry* |
| the Riemannian distance $d_g(p,q)$ | the infimum of the lengths of the curves joining the points | *Riemannian Geometry* |
| the volume form $\mathrm{vol}_g = \sqrt{\det(g_{ij})}\,dx^1\wedge\cdots\wedge dx^n$ | the measure the metric induces | *Curvature and Geodesics* |
| the pullback of a metric by an immersion | the induced metric on a submanifold, the first fundamental form | *Riemannian Geometry* |
| the isometry group $\operatorname{Isom}(M,g)$ | a Lie group by Myers–Steenrod, acting by metric-preserving diffeomorphisms | *Riemannian Geometry*; *Homogeneous Spaces* |

The metric and the distance determine each other, and the topology of the manifold is recovered from the metric because the metric topology of $d_g$ is the given topology. The metric is the only datum: the connection, the curvature, the geodesics, the volume and the isometry group are all functions of $g$.

## The Levi-Civita Connection and Geodesics

The fundamental theorem of Riemannian geometry gives the metric a unique torsion-free connection, and the geodesics are its straight lines.

| Object | The property it has | Introduced in |
|---|---|---|
| the Levi-Civita connection $\nabla$ | the unique connection with $\nabla g = 0$ and zero torsion | *Riemannian Geometry*; *Curvature and Geodesics* |
| the Christoffel symbols $\Gamma^k_{ij}$ | the coefficients of the connection in a chart | *Curvature and Geodesics* |
| the connection form $\theta^i_{\ j}$ | the connection in a frame, matrix-valued | *Curvature and Geodesics* |
| parallel transport $P_\gamma$ | the isometry of tangent spaces along a curve, defined by $\nabla$ | *Curvature and Geodesics* |
| the holonomy group $\operatorname{Hol}_p$ | the group of parallel transports around the loops at $p$ | *Curvature and Geodesics* |
| the geodesic equation $\nabla_{\gamma'}\gamma' = 0$ | the equation of a curve whose velocity is parallel | *Curvature and Geodesics* |
| the exponential map $\exp_p : T_pM \to M$ | the map sending a tangent vector to the endpoint of its geodesic | *Curvature and Geodesics* |
| normal coordinates and the Gauss lemma | coordinates in which the metric is Euclidean to first order at $p$ | *Curvature and Geodesics* |
| the injectivity radius and the cut locus | the range in which the exponential map is a diffeomorphism | *Riemannian Geometry* |
| the completeness theorem of Hopf–Rinow | metric completeness, geodesic completeness and finite compactness agree | *Riemannian Geometry* |

Parallel transport is the only invariant of the connection that is local along curves, and the holonomy group measures the failure of transport to return a tangent vector to itself around a closed loop. The exponential map is the bridge from the tangent space to the manifold, and the completeness theorem makes the geodesics of a complete metric global, so that the geometry is controlled by the curvature along them.

## Curvature

The curvature tensor is the failure of second covariant derivatives to commute, and its traces are the sectional, Ricci and scalar curvatures.

| Object | The property it has | Introduced in |
|---|---|---|
| the curvature tensor $R(X,Y)Z$ | the commutator of covariant derivatives, an algebraic curvature tensor | *Curvature and Geodesics* |
| the curvature form $\mathcal{R} = d\theta + \theta\wedge\theta$ | the matrix-valued two-form of the connection in a frame | *Curvature and Geodesics* |
| the sectional curvature $K(\sigma) = R(v,w,w,v)$ | the curvature of a two-plane, the value that determines $R$ | *Curvature and Geodesics* |
| the Ricci tensor $\operatorname{Ric}(X,Y)$ | the trace of the curvature, the average of the sectional curvatures | *Curvature and Geodesics* |
| the scalar curvature $S$ | the trace of the Ricci tensor | *Curvature and Geodesics* |
| the Einstein tensor $G = \operatorname{Ric} - \frac12Sg$ | the divergence-free combination of the curvature | *Curvature and Geodesics* |
| the Jacobi equation $\frac{D^2J}{dt^2} + R(J,\gamma')\gamma' = 0$ | the linearised geodesic equation, governing the geodesic deviation | *Riemannian Geometry* |
| conjugate points | the zeros of a Jacobi field, the limit of the minimising range | *Riemannian Geometry* |
| the Weyl tensor and its conformal flatness | the trace-free part of the curvature, controlling the conformal geometry | *Conformal Geometry* |
| the Bianchi identities | the algebraic and differential symmetries of the curvature | *Curvature and Geodesics* |

The curvature tensor is the local invariant of the metric, the sectional curvature determines it completely, and the Ricci and scalar curvatures are its two traces. The Bianchi identities and the second Bianchi identity are the source of the divergence-free Einstein tensor and of the contracted identity that makes the curvature the natural object of the variational principles of the field equations.

## Comparison Theorems

The comparison theorems translate a curvature bound into a statement about the geometry, by comparing the manifold with the constant-curvature model of the bound.

| Theorem | The comparison it makes | Introduced in |
|---|---|---|
| the comparison field $s_{\tilde K}(t)$ | the Jacobi field of the constant-curvature model, the standard of comparison | *Riemannian Geometry* |
| the Rauch comparison theorem | a curvature bound compares Jacobi fields and the exponential map with the model | *Riemannian Geometry* |
| the Bishop–Gromov volume comparison | a Ricci bound compares the volumes of balls with the model | *Gromov–Hausdorff Convergence* |
| the Cartan–Hadamard theorem | $K \leq 0$, complete and simply connected implies $\exp_p$ is a diffeomorphism | *Riemannian Geometry* |
| the Bonnet–Myers theorem | $\operatorname{Ric} \geq (n-1)k > 0$ implies compactness and a diameter bound | *Riemannian Geometry* |
| the Gauss–Bonnet theorem | $\int_M K\,\mathrm{vol}_g = 2\pi\chi(M)$ for a compact oriented surface | *Curvature and Geodesics* |
| the Gauss–Bonnet–Chern theorem | the Pfaffian of the curvature integrates to the Euler characteristic in every even dimension | *Curvature and Geodesics* |
| the Gauss equation | the curvature of a submanifold in terms of the ambient curvature and the second fundamental form | *Riemannian Geometry* |
| the minimal surface equation | the Euler–Lagrange equation $H = 0$ of the area functional | *Minimal Surfaces* |

The comparison field is the Jacobi field of the model, and every comparison theorem is a statement that a curvature inequality makes the Jacobi fields, the volumes or the exponential map monotone relative to the model. The Gauss–Bonnet theorem is the boundary case in which the comparison integrates to a topological invariant, and it is the first instance of the principle that the integral of a curvature is a characteristic number.

## Model Spaces, Space Forms and Einstein Geometries

The geometries of constant curvature are the models of the comparison, and the Einstein metrics and the Ricci flow are the geometries selected by a condition on the Ricci tensor.

| Geometry | The property it has | Introduced in |
|---|---|---|
| the round sphere $S^n_r$ | constant curvature $1/r^2$, the positive model | *Curvature and Geodesics*; *Spherical Geometry* |
| Euclidean space $\mathbb{R}^n$ | constant curvature $0$, the flat model | *Curvature and Geodesics*; *Euclidean Geometry* |
| hyperbolic space $\mathbf{H}^n_r$ | constant curvature $-1/r^2$, the negative model | *Curvature and Geodesics*; *Hyperbolic Geometry* |
| a space form | a complete connected manifold of constant curvature, a quotient of a model | *Riemannian Geometry* |
| a homogeneous metric | a $G$-invariant metric on $G/H$, determined on $\mathfrak{m}$ | *Homogeneous Spaces* |
| a normal homogeneous space | a homogeneous metric from the Killing form, with Nomizu's curvature formula | *Homogeneous Spaces* |
| a symmetric space with its invariant metric | the metric with $\nabla R = 0$ | *Symmetric Spaces* |
| an Einstein metric | $\operatorname{Ric} = \lambda g$, with $\lambda = S/n$ | *Riemannian Geometry* |
| a Kähler–Einstein metric | a Kähler metric with $\rho = \lambda\Omega$ | *Kähler Geometry* |
| a Calabi–Yau metric | a Ricci-flat Kähler metric, $c_1 = 0$ | *Calabi–Yau Manifolds* |
| the Ricci flow | the evolution $\partial_tg = -2\operatorname{Ric}$, deforming a metric to an Einstein one | *Ricci Flow* |
| the Ricci flow with surgery | the flow continued through singularities, used to prove geometrisation | *Ricci Flow*; *Low-Dimensional Topology* |

The three model spaces are the complete simply connected geometries of constant curvature, and the space-form theorem says that every complete constant-curvature geometry is a quotient of one of them. The Einstein condition is the weakest curvature condition that singles out a geometry, and the Ricci flow is the parabolic equation that deforms an arbitrary metric towards it; the flow with surgery is the tool by which the geometrisation of three-manifolds is proved.

## Warnings

An object that a reader may expect among the Riemannian geometries, and does not find, is recorded with the reason.

| Object | Why it is not listed as a Riemannian geometry | Introduced in |
|---|---|---|
| a pseudo-Riemannian metric | the form is indefinite, so the length is not positive and the metric is not Riemannian | *Pseudo-Riemannian and Lorentzian Geometry* |
| a Lorentzian metric | the signature $(n-1,1)$ special case of the pseudo-Riemannian case; the model of Part III | *Pseudo-Riemannian and Lorentzian Geometry* |
| a general metric space | no manifold and no metric tensor; the geometry is not defined by a Riemannian metric | *Metric, Uniform and Complete Spaces* |
| an incomplete Riemannian manifold | defined and Riemannian, but the comparison theorems that need completeness do not apply | *Riemannian Geometry* |
| a Finsler metric | a norm on each tangent space, not a bilinear form; the Teichmüller metric is Finsler and not Riemannian for $g \geq 2$ | *Teichmüller Theory* |
| a Kähler metric as a Riemannian metric only | it is Riemannian, but its geometry is the complex one of the Kähler article | *Kähler Geometry* |

## Summary

This article has listed the Riemannian geometries of the corpus along the chain from the metric to the comparison theorems. The metrics open the list, with the first fundamental form, the length, the distance and the volume; the Levi-Civita connection and the geodesics follow, with the Christoffel symbols, parallel transport, the holonomy group, the exponential map and the Hopf–Rinow theorem; the curvature tensor and its traces are gathered, with the Jacobi equation and the Weyl tensor; the comparison theorems, Rauch, Bishop–Gromov, Cartan–Hadamard, Bonnet–Myers and Gauss–Bonnet, are recorded with the comparison each makes; and the model spaces, the space forms, the Einstein and Kähler–Einstein and Calabi–Yau metrics and the Ricci flow close the list. Beside the examples stand the non-examples: a pseudo-Riemannian or Lorentzian metric is indefinite, a general metric space has no metric tensor, an incomplete manifold fails the hypotheses of the comparison theorems, and a Finsler metric such as the Teichmüller metric is not a bilinear form.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following, and they are the symbols of the articles that introduce them.

| Symbol | Meaning |
|---|---|
| $(M,g)$, $g_{ij}$, $ds^2$ | Riemannian manifold, metric coefficients, first fundamental form |
| $L_g$, $d_g$, $\mathrm{vol}_g$ | Length, distance, volume form |
| $\nabla$, $\Gamma^k_{ij}$, $\theta^i_{\ j}$ | Levi-Civita connection, Christoffel symbols, connection form |
| $R$, $\mathcal{R}$, $K(\sigma)$ | Curvature tensor, curvature form, sectional curvature |
| $\operatorname{Ric}$, $S$, $G$ | Ricci tensor, scalar curvature, Einstein tensor |
| $\exp_p$, $\operatorname{inj}(p)$ | Exponential map, injectivity radius |
| $J$, $\operatorname{Hol}_p$ | Jacobi field, holonomy group |
| $S^n_r$, $\mathbf{H}^n_r$, $\mathbb{R}^n$ | Model spaces of constant curvature |
| $\operatorname{Isom}(M,g)$ | Isometry group, a Lie group by Myers–Steenrod |
| $\mathfrak{m}$ | The isotropy complement of $\mathfrak{h}$ in $\mathfrak{g}$ |

## Further Reading

- Manfredo do Carmo, *Riemannian Geometry* (Birkhäuser, 1992), for the metric, the Levi-Civita connection, the curvature and the comparison theorems.
- Jeff Cheeger and David Ebin, *Comparison Theorems in Riemannian Geometry* (North-Holland, 1975), for the Rauch, Bishop–Gromov and Cartan–Hadamard theorems in their standard form.
- Sylvestre Gallot, Dominique Hulin and Jacques Lafontaine, *Riemannian Geometry* (Springer, 3rd ed. 2004), for the curvature, the geodesics and the comparison theory with the models.
- Peter Petersen, *Riemannian Geometry* (Springer, 3rd ed. 2016), for the Einstein metrics, the holonomy and the modern comparison theory.
