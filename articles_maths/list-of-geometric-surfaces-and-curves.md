
# __List of Geometric Surfaces and Curves__

## Introduction

This article lists the surfaces by genus and Euler characteristic and the curves with their genera, their Jacobians and their points. Every entry points to the article that introduces the surface or the curve, and the article introduces nothing and proves nothing.

The list gathers the topological surfaces of Part II classified by their genus and their Euler characteristic, the Riemann surfaces that carry a complex structure, the algebraic curves with their arithmetic and geometric genera, the divisors and the Jacobian of a curve, and the rational points of a curve over a finite field and over a number field. Two invariants organise the whole list: the genus, which is the topological invariant of a surface and the arithmetic invariant of a curve and which decides both the uniformisation of the surface and the finiteness of the rational points of the curve, and the Euler characteristic, which is the genus in its topological form.

The article records examples and non-examples side by side. Beside the surfaces and the curves it lists the singular curves for which the two genera differ, the non-orientable surfaces that carry no complex structure, the curves that have no rational point, and the curves of high genus whose points are finite, each with the failure named and the article that records it.

## Surfaces by Genus and Euler Characteristic

A closed surface is classified by its genus and its orientability, and its Euler characteristic is the genus in numerical form.

| Surface | Euler characteristic | The property it has | Introduced in |
|---|---|---|---|
| the sphere $S^2$ | $2$ | the unique simply connected closed surface | *Low-Dimensional Topology*; *Spherical Geometry* |
| the torus $T^2 = S^1\times S^1$ | $0$ | the orientable surface of genus one, the first of the connected sums of tori | *Low-Dimensional Topology*; *The Fundamental Group and Covering Spaces* |
| the real projective plane $\mathbb{RP}^2$ | $1$ | non-orientable, the sphere modulo the antipodal map | *Low-Dimensional Topology* |
| the Klein bottle | $0$ | non-orientable, $\chi = 0$, not a torus | *Low-Dimensional Topology* |
| the closed orientable surface of genus $g$ | $2 - 2g$ | hyperbolic for $g \geq 2$; hyperbolic area $4\pi(g-1)$ | *Low-Dimensional Topology*; *Hyperbolic Geometry* |
| the connected sum $M\# N$ | $\chi(M) + \chi(N) - 2$ | the operation of the classification of surfaces | *Low-Dimensional Topology* |
| a compact surface with boundary | $2 - 2g - b$ | classified by genus, orientability and boundary number $b$ | *Low-Dimensional Topology* |
| a compact flat surface | $0$ | the torus and the Klein bottle, the two compact flat surfaces | *Symmetry, Point and Crystallographic Groups* |
| a hyperbolic surface | negative | a quotient $\mathbf{H}^2/\Gamma$, the hyperbolic area $4\pi(g-1)$ | *Hyperbolic Geometry* |
| the mapping class group of a surface | — | the group of the isotopy classes of its homeomorphisms | *Mapping Class Groups* |

The closed surfaces are classified by the two discrete invariants, orientability and Euler characteristic, and the uniformisation theorem gives each one exactly one of the three geometries according to the sign of $\chi$. The connected-sum decomposition reduces the classification to the prime surfaces, the sphere and the projective plane being the two starting points, and the hyperbolic area is the first invariant that is geometric rather than topological.

## Riemann Surfaces and Complex Structures

A Riemann surface is a surface with a complex structure, and the complex structure is equivalent to a conformal structure by the uniformisation theorem.

| Object | The property it has | Introduced in |
|---|---|---|
| a Riemann surface | a one-dimensional complex manifold, a surface with a holomorphic atlas | *Teichmüller Theory*; *Algebraic Curves* |
| the genus of a Riemann surface | the topological genus, the number of handles | *Teichmüller Theory* |
| the uniformisation of a surface | the spherical, Euclidean or hyperbolic metric according to the sign of $\chi$ | *Hyperbolic Geometry* |
| the Teichmüller space of a surface | the space of the marked complex structures, of dimension $3g-3+n$ for $2g-2+n > 0$ | *Teichmüller Theory* |
| the Teichmüller metric | the Finsler metric of the extremal quasiconformal dilatation, not Riemannian for $g\geq2$ | *Teichmüller Theory* |
| the moduli space $M_g$ of curves | the coarse moduli space of the curves of genus $g$, of dimension $3g-3$ | *Moduli Spaces* |
| the stable-curve compactification $\overline M_g$ | the projective compactification by the stable curves | *Moduli Spaces* |

The complex structure of a surface is equivalent to a conformal class of metrics, and by uniformisation it is realised by a metric of constant curvature, so that the theory of Riemann surfaces is the theory of hyperbolic surfaces when the genus is at least two. The moduli space is the quotient of the Teichmüller space by the mapping class group, and its dimension $3g-3$ counts the complex moduli of a curve of genus $g$.

## Plane Curves and their Genera

An algebraic curve is given by a polynomial equation, and its genus is computed from its degree and its singularities.

| Curve | The property it has | Introduced in |
|---|---|---|
| an affine or projective plane curve | the zero set of a polynomial of degree $d$ in two or three variables | *Algebraic Curves*, §Plane Curves |
| the arithmetic genus $p_a(C) = (d-1)(d-2)/2$ | the genus of a plane curve of degree $d$ before the singularities are resolved | *Algebraic Curves* |
| the geometric genus $g = p_a - \sum_P\delta_P$ | the genus after the singularities are accounted for | *Algebraic Curves* |
| a rational curve | a curve of genus $0$, birational to the projective line | *Algebraic Curves* |
| a nonsingular plane cubic with a rational point | an elliptic curve of genus $1$, with the group law of the chord and the tangent | *Elliptic Curves* |
| the Weierstrass form $y^2 = x^3 + a_4x + a_6$ | the standard equation of an elliptic curve, with discriminant $\Delta$ and $j$-invariant | *Elliptic Curves* |
| the Hermitian curve $y^q + y = x^{q+1}$ | a curve over $\mathbb{F}_{q^2}$ of maximal genus, meeting the Hasse–Weil bound | *Algebraic Curves*, §Curves over Finite Fields |
| the function field $K(C)$ | the field of transcendence degree one determining the curve up to birational equivalence | *Algebraic Curves* |
| the canonical divisor $K_C$ and the genus | the divisor of a rational form, of degree $2g-2$ | *Algebraic Curves* |

The genus of a plane curve is determined by its degree and its singularities, and it is the invariant that governs both the geometry and the arithmetic. A nonsingular cubic is an elliptic curve as soon as it has a rational point, and the group law on it is the geometric form of the identification of the points with the divisor classes of degree zero.

## Jacobians and Divisor Classes

The divisor classes of a curve form a group, and the degree-zero part is the Jacobian, the group of the divisor classes of degree zero attached to the curve.

| Object | The property it has | Introduced in |
|---|---|---|
| the divisor $\operatorname{div}(f)$ of a function | the formal sum of the zeros and poles, of degree zero | *Algebraic Curves* |
| the divisor class group $\operatorname{Pic}^0(C)$ | the degree-zero divisors modulo the principal ones | *Algebraic Curves* |
| the Riemann–Roch theorem | $\ell(D) - \ell(K_C - D) = \deg D + 1 - g$ | *Algebraic Curves*, §Divisors and Linear Systems |
| the space $L(D)$ and its dimension $\ell(D)$ | the functions with poles bounded by the divisor | *Algebraic Curves* |
| the Jacobian of a curve | the moduli space of the line bundles of a fixed degree, of dimension $g$ | *Moduli Spaces*; *Algebraic Curves* |
| the identification of the points with $\operatorname{Pic}^0$ | the map $P \mapsto$ the class of $P - O$, the origin of the elliptic group law | *Algebraic Curves* |
| the linear flow on the Jacobian | the straight-line motion of the divisor under an integrable flow | *Integrable Systems* |

The Riemann–Roch theorem computes the dimension of the space of the functions with prescribed poles, and it is the tool by which the genus and the divisor classes are related. The Jacobian is the moduli space of the line bundles of degree zero on the curve, and it is the ambient variety of the elliptic group law in the case $g=1$ and of the finite-gap flow in the theory of integrable systems.

## The Points of a Curve

The rational points of a curve are governed by the genus: a curve of genus zero is either the line or has none, a curve of genus one is an elliptic curve with a finitely generated group of points, and a curve of genus at least two has only finitely many points over a number field.

| Object | The property it has | Introduced in |
|---|---|---|
| the set $C(\mathbb{F}_q)$ of rational points | the points defined over a finite field | *Algebraic Curves*, §Curves over Finite Fields |
| the zeta function $Z(C,T)$ | the generating function of the numbers of points, rational with a functional equation | *Algebraic Curves* |
| the Hasse–Weil bound | $\lvert C(\mathbb{F}_q)\rvert \leq q + 1 + 2g\sqrt q$ | *Algebraic Curves* |
| the roots $\alpha_i$ of the numerator | the reciprocal roots, of absolute value $\sqrt q$ | *Algebraic Curves* |
| the group $E(K)$ of points of an elliptic curve | an abelian group under the chord-and-tangent law | *Elliptic Curves* |
| the Mordell–Weil theorem | $E(K)$ is finitely generated over a number field | *Elliptic Curves* |
| the torsion subgroup $E(K)_{\mathrm{tors}}$ and the rank $r$ | the finite part and the free rank of $E(K)$ | *Elliptic Curves* |
| the Tate module $T_\ell(E)$ | the inverse limit of the $\ell^n$-torsion, a Galois representation | *Elliptic Curves* |
| the Frobenius endomorphism and $a_q = q+1-\lvert E(\mathbb{F}_q)\rvert$ | the trace of Frobenius, determining the zeta function | *Elliptic Curves* |
| the theorem of Faltings | the set $C(K)$ is finite for a curve of genus $g \geq 2$ over a number field | *Algebraic Curves*, §The Arithmetic of a General Curve |

The genus separates the arithmetic of curves: for genus zero the curve is the projective line or a conic with no point, for genus one the curve is elliptic and its points form the finitely generated group of the Mordell–Weil theorem, and for higher genus the theorem of Faltings makes the set of rational points finite. The zeta function of a curve over a finite field packages the numbers of points, and the Hasse–Weil bound is the arithmetic form of the Riemann hypothesis in dimension one.

## Warnings

An object that a reader may expect among the surfaces and curves, and does not find, is recorded with the reason.

| Object | Why it is not listed as a surface or a curve of the list | Introduced in |
|---|---|---|
| a singular plane curve | its arithmetic genus differs from its geometric genus; only the resolved curve has the genus of the list | *Algebraic Curves* |
| a non-orientable surface | it carries no complex structure and is not a Riemann surface | *Low-Dimensional Topology*; *Teichmüller Theory* |
| a curve of genus zero with no rational point | a conic, not isomorphic to the projective line over the base field | *Algebraic Curves* |
| a curve of genus at least two with infinitely many rational points | it cannot exist over a number field, by the theorem of Faltings | *Algebraic Curves*, §The Arithmetic of a General Curve |
| a higher-dimensional analogue of a Riemann surface | a complex manifold of dimension at least two, treated in the Kähler geometry | *Kähler Geometry* |

## Summary

This article has listed the surfaces and curves of the corpus. The surfaces are classified by genus and Euler characteristic, with the sphere, the torus, the projective plane, the Klein bottle, the genus-$g$ surfaces, the connected sums and the hyperbolic surfaces; the Riemann surfaces follow, with the complex structure, the uniformisation, the Teichmüller space and the moduli space of curves; the plane curves are recorded with their arithmetic and geometric genera, the Weierstrass form, the Hermitian curve and the canonical divisor; the divisors, the Riemann–Roch theorem and the Jacobian follow; and the points of a curve close the list, with the zeta function, the Hasse–Weil bound, the Mordell–Weil theorem and the Tate module. Beside the examples stand the non-examples: a singular curve has two genera that differ, a non-orientable surface is not a Riemann surface, a conic without a rational point is not the line, and a curve of genus at least two has only finitely many rational points.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following, and they are the symbols of the articles that introduce them.

| Symbol | Meaning |
|---|---|
| $\chi$, $g$, $b$ | Euler characteristic, genus, number of boundary components |
| $M\# N$ | Connected sum of surfaces |
| $M_g$, $\overline M_g$ | Moduli space of curves of genus $g$; its compactification |
| $d$, $p_a(C)$, $\delta_P$ | Degree of a plane curve, arithmetic genus, delta invariant |
| $K_C$, $L(D)$, $\ell(D)$ | Canonical divisor, space of functions, its dimension |
| $\operatorname{Div}^0(C)$, $\operatorname{Pic}^0(C)$ | Degree-zero divisors and their class group |
| $C(\mathbb{F}_q)$, $Z(C,T)$, $\alpha_i$ | Rational points, zeta function, reciprocal roots |
| $E$, $O$, $\Delta$, $j$, $E(K)$, $E[n]$, $T_\ell(E)$ | Elliptic curve and its invariants, points, torsion, Tate module |
| $\mathbf{H}^2$ | The hyperbolic plane, the model of the hyperbolic surfaces |
| $\operatorname{div}(f)$ | The divisor of a rational function, of degree zero |

## Further Reading

- Robin Hartshorne, *Algebraic Geometry* (Springer, 1977), for the curves, their genera, the divisors and the Riemann–Roch theorem.
- Joseph H. Silverman, *The Arithmetic of Elliptic Curves* (Springer, 2nd ed. 2009), for the elliptic curves, the group law, the Mordell–Weil theorem and the Tate module.
- Rick Miranda, *Algebraic Curves and Riemann Surfaces* (American Mathematical Society, 1995), for the Riemann surfaces, the Jacobians and the divisor theory.
- Benson Farb and Dan Margalit, *A Primer on Mapping Class Groups* (Princeton University Press, 2012), for the surfaces, the uniformisation and the moduli of the hyperbolic structures.
