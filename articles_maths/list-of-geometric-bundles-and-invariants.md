
# __List of Geometric Bundles and Invariants__

## Introduction

This article lists the bundles of the corpus — the fibre, vector and principal bundles — the connections carried on them, and the characteristic classes and characteristic numbers that measure each bundle. Every entry points to the article that introduces the object, and the article introduces nothing and proves nothing.

The list follows the chain that the two articles of the theme set out. A fibre bundle is a local product with transition functions; a principal bundle carries the structure group and the associated bundles are built from it; a connection on a bundle is the rule of parallel transport, and its curvature is the local measure of the failure of the transport to commute; the invariant polynomials of the curvature give the characteristic classes, and the evaluation of those classes on a manifold gives the characteristic numbers that the index theorem computes. The invariants of the list are the classes and numbers that are independent of the connection, and the classifying spaces and K-theory are the functors in which the classes are naturally indexed.

The article records examples and non-examples side by side. Beside the bundles and their invariants it lists the structures that are not bundles, the bundles that carry no Euler class because they are not orientable, and the characteristic classes that vanish for a flat connection, each with the failure named and the article that records it.

## Fibre, Vector and Principal Bundles

A fibre bundle is a map that is locally a product, and the structure of the bundle is encoded in its transition functions and in its structure group.

| Object | The property it has | Introduced in |
|---|---|---|
| a fibre bundle $\pi : E \to B$ | locally a product $U\times F$, with fibre $F$ | *Fibre Bundles, Connections and Curvature* |
| the transition functions $g_{\alpha\beta}$ | the clutching data, with $g_{\alpha\beta}g_{\beta\gamma} = g_{\alpha\gamma}$ | *Fibre Bundles, Connections and Curvature* |
| a principal $G$-bundle $P \to M$ | a bundle with a free transitive right action of the structure group $G$ | *Fibre Bundles, Connections and Curvature* |
| the associated bundle $P\times_G F$ | the bundle with fibre $F$ built from a $G$-space and a principal bundle | *Fibre Bundles, Connections and Curvature* |
| the frame bundle of $M$ | the principal bundle of the frames, whose associated bundles are the tensor bundles | *Fibre Bundles, Connections and Curvature* |
| the tangent and cotangent bundles $TM$, $T^*M$ | the vector bundles of the tangent and cotangent spaces | *Smooth Manifolds and Differential Geometry* |
| a vector bundle $E \to B$ | a fibre bundle with a vector space as fibre and linear transitions | *Fibre Bundles, Connections and Curvature*; *Characteristic Classes* |
| the section space $\Gamma(E)$ | the smooth sections of a bundle; the fields of the theory | *Fibre Bundles, Connections and Curvature* |
| the tautological bundle $\gamma_k$ on a Grassmannian | the rank-$k$ bundle whose fibre is the subspace itself | *Grassmannians and Stiefel Manifolds* |
| a line bundle and its class in $H^2(B;\mathbb{Z})$ | the isomorphism classes of complex line bundles | *Characteristic Classes* |
| the canonical bundle $K_M$ | the top exterior power of the holomorphic cotangent bundle | *Kähler Geometry* |
| the normal bundle and the tubular neighbourhood | the bundle of the normal directions of a submanifold, and its disc bundle | *Differential Topology* |
| the Hopf fibration $S^3 \to S^2$ | the principal $U(1)$-bundle of the three-sphere over the sphere | *Spherical Geometry*, §The Three-Sphere and the Hopf Fibration; *Homotopy Groups and Fibrations* |

The transition functions are the complete cocycle data of the bundle, and the principal bundle is the frame bundle of a vector bundle, so that the geometry of a vector bundle and the geometry of its frame bundle carry the same information. The associated-bundle construction produces from a representation of the structure group the tensor, spinor and density bundles that the corpus uses on manifolds.

## Connections and Curvature

A connection is a rule of parallel transport, given locally by a connection form, and its curvature measures the failure of the transport to commute.

| Object | The property it has | Introduced in |
|---|---|---|
| a connection $\nabla$ | a derivation of the sections, $\nabla(fs) = df\otimes s + f\nabla s$ | *Fibre Bundles, Connections and Curvature* |
| the connection form in a frame $\omega = (\omega^i_{\ j})$ | $\nabla = d+\omega$, matrix-valued in the frame | *Fibre Bundles, Connections and Curvature* |
| the change of frame $\omega' = g^{-1}\omega g + g^{-1}dg$ | the transformation of the connection, the gauge transformation rule | *Fibre Bundles, Connections and Curvature* |
| a connection form on a principal bundle $\omega \in \Omega^1(P;\mathfrak{g})$ | $\omega(A^{\#}) = A$ and $R_g^*\omega = \operatorname{Ad}(g^{-1})\omega$ | *Fibre Bundles, Connections and Curvature* |
| the horizontal subspace $H_pP = \ker\omega_p$ | the complement to the vertical, defining the transport | *Fibre Bundles, Connections and Curvature* |
| the curvature $R = d\omega + \omega\wedge\omega$ | the $\operatorname{End}(E)$-valued $2$-form measuring noncommutation | *Fibre Bundles, Connections and Curvature* |
| the curvature of a principal connection $\Omega = d\omega + \frac12[\omega,\omega]$ | the $\mathfrak{g}$-valued curvature form | *Fibre Bundles, Connections and Curvature* |
| the Bianchi identity $d^\nabla R = 0$ | the differential condition the curvature satisfies | *Fibre Bundles, Connections and Curvature* |
| the holonomy group of a connection | the group of the parallel transports around loops | *Fibre Bundles, Connections and Curvature* |
| a flat connection | the connection with $R = 0$, locally trivial or a Maurer–Cartan form | *Fibre Bundles, Connections and Curvature* |
| a gauge transformation | a change of frame, acting on the connection by the transformation rule | *Fibre Bundles, Connections and Curvature* |
| the Levi-Civita connection | the metric, torsion-free connection of the tangent bundle | *Riemannian Geometry* |

The curvature is tensorial, so its value at a point depends only on the vectors and not on the extension of the sections, and the Bianchi identity makes it the closed form of the connection. A flat connection has a global system of parallel sections after the passage to the universal cover, and the holonomy group is the algebraic invariant of a connection that the characteristic classes do not see; the Levi-Civita connection is the case in which the connection is determined by a metric.

## Characteristic Classes

The invariant polynomials of the curvature are closed and their de Rham classes are independent of the connection, and they are the characteristic classes of the bundle.

| Class | The property it measures | Introduced in |
|---|---|---|
| the Chern–Weil homomorphism | the map $S^\bullet(\mathfrak{g}^*)^G \to H^{\mathrm{ev}}_{dR}(M)$ from invariant polynomials to cohomology | *Fibre Bundles, Connections and Curvature* |
| the first Chern class $c_1(L)$ | the class of $\frac{i}{2\pi}\mathcal{F}$, the curvature of a line bundle | *Fibre Bundles, Connections and Curvature* |
| the Euler class $e(E)$ | the class of a real oriented bundle of even rank, the obstruction to a nowhere-zero section | *Characteristic Classes* |
| the Stiefel–Whitney classes $w_i(E) \in H^i(B;\mathbb{Z}/2)$ | the $\mathbb{Z}/2$ classes; $w_1$ is orientability and $w_2$ is the spin obstruction | *Characteristic Classes* |
| the Chern classes $c_i(E) \in H^{2i}(B;\mathbb{Z})$ | the integral classes of a complex bundle, with $c(E\oplus F) = c(E)c(F)$ | *Characteristic Classes* |
| the Pontryagin classes $p_i(E)$ | the real classes, $p_i(E) = (-1)^ic_{2i}(E\otimes\mathbb{C})$ | *Characteristic Classes* |
| the Chern roots and the splitting principle | the formal factorisation $c(E) = \prod_i(1+x_i)$ | *Characteristic Classes* |
| the Chern character $\operatorname{ch}(E)$ | the rational class with $K^0(B)\otimes\mathbb{Q} \cong H^{\mathrm{ev}}(B;\mathbb{Q})$ | *Characteristic Classes* |
| the relations $p_i \equiv w_{2i}^2$ and $e \equiv w_n \pmod 2$ | the compatibility of the integral and $\mathbb{Z}/2$ classes | *Characteristic Classes* |
| the Hirzebruch $L$-polynomial $L_k(p_1,\ldots,p_k)$ | the multiplicative polynomial $\sum_kL_k = \prod_j\frac{x_j}{\tanh x_j}$ | *Characteristic Classes* |
| the Todd class | the multiplicative class of the index theorem for the Dolbeault complex | *The Atiyah–Singer Index Theorem and K-Theory* |
| the $\hat A$-genus | the multiplicative class of the Dirac operator | *Spin Geometry*; *The Atiyah–Singer Index Theorem and K-Theory* |

The characteristic classes are the cohomological invariants of a bundle, they are natural under pullback, and they are computable from any connection by the invariant polynomials of its curvature. The splitting principle reduces the computation to the case of a sum of line bundles, and the multiplicative sequences — the $L$-polynomial, the Todd class and the $\hat A$-genus — are the generating series in which the classical index theorems are stated.

## Characteristic Numbers and the Index Theorem

A characteristic number is the evaluation of a characteristic class of the tangent bundle on the fundamental class, and the index theorem identifies it with the index of an elliptic operator.

| Object | The property it has | Introduced in |
|---|---|---|
| a characteristic number $\langle\kappa(TM),[M]\rangle$ | the evaluation of a class of $TM$ on the fundamental class of a closed manifold | *Characteristic Classes* |
| the Gauss–Bonnet theorem $\int_Me(TM) = \chi(M)$ | the Euler class integrates to the Euler characteristic | *Fibre Bundles, Connections and Curvature*; *Riemannian Geometry* |
| the signature theorem | $\operatorname{sign}(M) = \langle L_k,[M]\rangle$ for a closed manifold of dimension $4k$ | *Characteristic Classes* |
| the $\hat A$-genus of a spin manifold | the characteristic number of the Dirac operator | *Spin Geometry* |
| the index of an elliptic operator | the difference of the dimensions of the kernel and cokernel | *The Atiyah–Singer Index Theorem and K-Theory* |
| the Atiyah–Singer index theorem | the index is the evaluation of a characteristic class of the symbol | *The Atiyah–Singer Index Theorem and K-Theory* |
| the index of the Dirac operator | $\hat A$-genus on a spin manifold, with the twisted version by a bundle | *The Atiyah–Singer Index Theorem and K-Theory*; *Spin Geometry* |
| the Riemann–Roch theorem | the holomorphic Euler characteristic as a Todd-class number | *Algebraic Curves*; *The Atiyah–Singer Index Theorem and K-Theory* |
| the cobordism invariance of the characteristic numbers | the numbers vanish on a boundary, defining the cobordism ring | *Cobordism and Surgery Theory* |

The characteristic numbers are the topological invariants of a closed manifold, and they are the integrals that appear on the analytic side of the index theorems. The theorem of Atiyah and Singer computes the index of an elliptic operator from the symbol, and its special cases are the Gauss–Bonnet, signature and Riemann–Roch theorems, each of which identifies a characteristic number with an analytic index.

## Classifying Spaces and K-Theory

The isomorphism classes of bundles over a base are classified by maps into a universal base, and K-theory is the cohomology theory in which the classes live.

| Object | The property it has | Introduced in |
|---|---|---|
| the classifying space $BO(n)$, $BU(n)$ | the base of the universal bundle, with $\mathbf{Vect}_n^{\mathbb{K}}(B) \cong [B, BO(n)]$ | *Characteristic Classes* |
| the universal bundle and the universal classes | the bundle whose classes pull back to all the classes of the base | *Characteristic Classes* |
| the classifying map | the map $B \to BO(n)$ whose pullback is the bundle | *Characteristic Classes* |
| the Stiefel–Whitney and Chern classes as universal classes | the generators of $H^*(BO(n))$ and $H^*(BU(n))$ | *Characteristic Classes* |
| the K-theory group $K^0(B)$ | the Grothendieck group of the vector bundles, a cohomology theory | *Topological K-Theory* |
| the Chern character $K^0(B)\otimes\mathbb{Q} \cong H^{\mathrm{ev}}(B;\mathbb{Q})$ | the rational isomorphism between K-theory and cohomology | *Characteristic Classes*; *Topological K-Theory* |

The classifying space is the universal base of the rank-$n$ bundles, so that the characteristic classes are the pullbacks of the universal classes, and the homotopy classification of the bundles replaces the topological one. K-theory is the generalised cohomology theory in which the classes are the stable classes of bundles, and the index theorem is naturally a statement in it.

## Warnings

An object that a reader may expect among the geometric bundles and invariants, and does not find, is recorded with the reason.

| Object | Why it is not listed as a bundle or a characteristic class | Introduced in |
|---|---|---|
| a sheaf on a space | a presheaf with a gluing condition; a locally free sheaf is a bundle, but a general sheaf is not | *Sheaves and the de Rham Complex* |
| a distribution or a foliation | a subbundle of the tangent bundle with an integrability condition, not itself a bundle over the base | *Fibre Bundles, Connections and Curvature* |
| the Euler class of a non-orientable bundle | the construction needs an orientation; only the reduction modulo two survives | *Characteristic Classes* |
| the integral Chern classes of a flat complex bundle | they vanish in real cohomology by Chern–Weil, since the curvature is zero | *Fibre Bundles, Connections and Curvature* |
| a Möbius band as a trivial bundle | the non-orientable real line bundle over the circle, non-trivial | *Topological K-Theory* |
| the tangent bundle of $S^2$ as a trivial bundle | it is non-trivial, obstructed by the Euler class | *Characteristic Classes* |

## Summary

This article has listed the bundles of the corpus and the invariants that measure them. The fibre, vector and principal bundles open the list, with the transition functions, the associated bundles, the frame and tautological bundles and the line bundles; the connections and their curvature follow, with the connection form, the gauge transformation rule, the Bianchi identity, the holonomy and the flat case; the characteristic classes are recorded, Chern, Stiefel–Whitney, Pontryagin and Euler, with the Chern–Weil homomorphism, the splitting principle, the Chern character and the multiplicative sequences; the characteristic numbers, the Gauss–Bonnet, signature and Riemann–Roch theorems and the Atiyah–Singer index theorem follow; and the classifying spaces and K-theory close the list. Beside the examples stand the non-examples: a sheaf and a foliation are not bundles, a non-orientable bundle has no Euler class, and the real Chern classes of a flat bundle vanish.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following, and they are the symbols of the articles that introduce them.

| Symbol | Meaning |
|---|---|
| $\pi : E \to B$, $g_{\alpha\beta}$, $P\times_GF$ | Fibre bundle, transition functions, associated bundle |
| $TM$, $T^*M$, $\Gamma(E)$, $K_M$ | Tangent and cotangent bundles, sections, canonical bundle |
| $\nabla$, $\omega$, $R$, $\Omega$ | Connection, connection form, curvature, curvature form |
| $c_i$, $w_i$, $p_i$, $e(E)$ | Chern, Stiefel–Whitney, Pontryagin and Euler classes |
| $\operatorname{ch}$, $L_k$, $\hat A$, Todd | Chern character, $L$-polynomial, $\hat A$-genus, Todd class |
| $BO(n)$, $BU(n)$, $K^0(B)$ | Classifying spaces and K-theory |
| $\langle\kappa(TM),[M]\rangle$ | Characteristic number |
| $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{C}$ | The standard number systems of the corpus |
| $\operatorname{Ad}$, $\operatorname{End}$ | Adjoint action of the structure group on $\mathfrak{g}$; endomorphism bundle of a vector bundle |
| $\mathbb{K}$ | The field of scalars of a bundle or of a classifying space |
| $\mathcal{F}$, $\operatorname{sign}(M)$ | The curvature of a line bundle, $\frac{i}{2\pi}\mathcal{F} = c_1(L)$; the signature of a closed manifold of dimension $4k$ |

## Further Reading

- John W. Milnor and James D. Stasheff, *Characteristic Classes* (Princeton University Press, 1974), for the bundle theory and the Stiefel–Whitney, Chern, Pontryagin and Euler classes.
- Shiing-Shen Chern, *Complex Manifolds without Potential Theory* (Springer, 2nd ed. 1979), for the Chern–Weil theory and the invariant polynomials of the curvature.
- Michael F. Atiyah and Isadore M. Singer, "The Index of Elliptic Operators I", *Annals of Mathematics* 87 (1968), 484–530, for the index theorem and its characteristic-class form.
- Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology* (Springer, 1982), for the classifying spaces, the Chern–Weil homomorphism and the spectral sequence of a fibration.
