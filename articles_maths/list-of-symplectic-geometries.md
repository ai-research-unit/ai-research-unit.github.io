
# __List of Symplectic Geometries__

## Introduction

This article lists the symplectic geometries of the corpus: the symplectic manifolds and their forms, the Darboux normal form, the Hamiltonian vector fields and Poisson brackets, the moment maps and the symplectic reduction, and the linear symplectic geometry of the symplectic group. Every entry points to the article that introduces the notion, and the article introduces nothing and proves nothing.

The symplectic geometry is the even-dimensional counterpart of the Riemannian one, and the list is ordered by the objects that replace its chain: a closed nondegenerate two-form replaces the metric, the Darboux theorem replaces the existence of normal coordinates and shows that the local geometry carries no invariant, the Poisson bracket is the bracket of functions that the form defines, and the Hamiltonian vector fields are the symmetries of the form. The moment map and the symplectic reduction are the operations by which a symmetry of a symplectic manifold produces a smaller symplectic manifold, and they are the geometric form of the conserved quantities of the Hamiltonian systems of Part III.

The article records examples and non-examples side by side. Beside the symplectic geometries it lists the contact geometries, which are the odd-dimensional analogues and are not symplectic, the Poisson manifolds that are not symplectic, the odd-dimensional manifolds that carry no symplectic form, and the symplectic forms that are not Kähler, each with the failure named and the article that records it.

## Symplectic Manifolds and Forms

A symplectic manifold is a smooth manifold with a closed nondegenerate two-form, and the form makes the tangent and cotangent bundles isomorphic.

| Object | The property it has | Introduced in |
|---|---|---|
| a symplectic manifold $(M,\omega)$ | a manifold with a closed nondegenerate $2$-form, of even dimension $2m$ | *Symplectic Geometry* |
| the symplectic form $\omega$ | closed, $d\omega = 0$, and nondegenerate, $\omega^{\flat}$ an isomorphism | *Symplectic Geometry* |
| the standard form $\omega_0 = \sum_i dx_i\wedge dy_i$ | the symplectic form of $\mathbb{R}^{2m}$, the local model | *Symplectic Geometry* |
| the symplectic volume form $\omega^{\wedge m}/m!$ | the volume the form defines; a symplectic manifold is orientable | *Symplectic Geometry* |
| the cotangent bundle $T^*Q$ with $\omega = -d\theta$ | the phase space of a mechanical system, a symplectic manifold | *Symplectic Geometry*; *Lagrangian and Hamiltonian Systems* |
| a Lagrangian submanifold | an isotropic submanifold of the maximal dimension $m$ | *Symplectic Geometry* |
| the conormal bundle $\nu^*N$ of a submanifold | a Lagrangian submanifold of $T^*Q$ | *Symplectic Geometry* |
| an isotropic or coisotropic submanifold | $\omega\vert_L = 0$, or $TL^{\perp}\subseteq TL$ | *Symplectic Geometry* |
| a compatible almost complex structure $J$ | $J$ with $\omega(JX,JY) = \omega(X,Y)$ and $g_J$ positive definite | *Symplectic Geometry* |
| a Kähler form $\Omega$ | a symplectic form that is closed and of type $(1,1)$ with respect to an integrable $J$ | *Kähler Geometry* |

The form is the whole geometry: it defines the volume, the orientation, the Lagrangian submanifolds and the almost complex structures compatible with it, and the bundle isomorphism $\omega^{\flat}$ converts functions into vector fields. The cotangent bundle with its tautological form is the universal example, and every symplectic manifold is locally its model by the Darboux theorem.

## The Darboux Theorem and Local Structure

The Darboux theorem states that every symplectic manifold is locally the standard symplectic space, so that the symplectic geometry has no local invariant.

| Object | The property it has | Introduced in |
|---|---|---|
| the Darboux theorem | every point has a chart in which $\omega = \sum_i dx_i\wedge dy_i$ | *Symplectic Geometry*, §The Darboux Theorem |
| the Moser trick | the argument deforming a family of forms to a normal form | *Symplectic Geometry*, §The Darboux Theorem |
| the absence of local invariants | the converse of the Riemannian situation: the curvature has no symplectic analogue | *Symplectic Geometry* |
| the Darboux theorem in contact geometry | the corresponding local normal form in odd dimensions | *Contact Geometry*, §The Darboux Theorem and Stability |
| the symplectic structure of the coadjoint orbit | the orbit of the coadjoint action carries a canonical symplectic form | *Poisson Geometry*, §Casimirs and Symplectic Leaves |

The theorem is the reason symplectic geometry is a global theory: the local model is unique, so the invariants are global and belong to the topology and to the dynamics, in contrast to the Riemannian case where the curvature is a local invariant. The existence of the normal form depends on the closedness and nondegeneracy of the form and on the Poincaré lemma, and it is proved by the Moser deformation argument.

## Hamiltonian Vector Fields and Poisson Brackets

The form converts a function into a vector field and defines a bracket on the functions, so that the symplectic manifold becomes a Lie algebra in two interlocking ways.

| Object | The property it has | Introduced in |
|---|---|---|
| the Hamiltonian vector field $X_f$ | the field defined by $\iota_{X_f}\omega = df$ | *Symplectic Geometry* |
| the Poisson bracket $\{f,g\} = \omega(X_f,X_g)$ | a Lie bracket on the functions, a derivation in each argument | *Symplectic Geometry*; *Symplectic Forms and Poisson Brackets* |
| the Lie algebra of the Hamiltonian fields | $[X_f,X_g] = -X_{\{f,g\}}$, the Poisson algebra acting by derivations | *Symplectic Forms and Poisson Brackets* |
| the conservation law | a function $f$ with $\{f,H\} = 0$ is constant along the flow of $X_H$ | *Lagrangian and Hamiltonian Systems*, §Conservation Laws and Phase Volume |
| the symplectic vector fields | the fields with $\mathcal{L}_X\omega = 0$, the Lie algebra of $\operatorname{Symp}(M,\omega)$ | *Symplectic Geometry* |
| a Poisson manifold $(P,\pi)$ | a manifold with a Poisson bracket not necessarily from a symplectic form | *Poisson Geometry* |
| the Schouten bracket and the Jacobi identity | the integrability condition for a Poisson tensor | *Poisson Geometry* |
| a Casimir function | a function bracketing to zero with every function | *Poisson Geometry*, §Casimirs and Symplectic Leaves |
| the symplectic leaves of a Poisson manifold | the maximal submanifolds on which the bracket is symplectic | *Poisson Geometry*, §Casimirs and Symplectic Leaves |
| the star product and deformation quantisation | the associative deformation $f*g = fg + \hbar\{f,g\} + O(\hbar^2)$ | *Poisson Geometry*, §Deformation Quantisation |

The bracket makes the functions of a symplectic manifold a Lie algebra, and the Hamiltonian fields are its image under the map $f\mapsto X_f$, whose kernel is the constants. The Poisson manifolds are the degenerate case, in which the bracket may not come from a form and the manifold foliates into the symplectic leaves; the coadjoint orbits of a Lie group are the standard examples, and they are the geometric content of the orbit method.

## Moment Maps and Symplectic Reduction

A symmetry of a symplectic manifold with a Hamiltonian function defines a moment map, and the level set of the moment map quotiented by the group is again symplectic.

| Object | The property it has | Introduced in |
|---|---|---|
| a Hamiltonian action of a Lie group | an action preserving $\omega$ and admitting a moment map | *Symplectic Geometry*, §Symplectic Reduction |
| the moment map $\mu : M \to \mathfrak{g}^*$ | the map with $d\mu_X = \iota_{X^{\#}}\omega$, encoding the conserved quantities | *Symplectic Geometry*, §Symplectic Reduction |
| the fundamental vector field $X^{\#}$ | the field of the infinitesimal action, Hamiltonian with potential $\mu_X$ | *Symplectic Geometry*; *Homogeneous Spaces* |
| the equivariance of the moment map | the compatibility of $\mu$ with the coadjoint action | *Symplectic Geometry* |
| the symplectic quotient $M/\!/G = \mu^{-1}(0)/G$ | the reduced symplectic manifold, of dimension $\dim M - 2\dim G$ | *Symplectic Geometry*, §Symplectic Reduction |
| the Marsden–Weinstein reduction | the theorem that the quotient is symplectic when $0$ is regular and $G$ acts freely | *Symplectic Geometry* |
| the reduced Hamiltonian system | the Hamiltonian system obtained from a symmetric one by reduction | *Lagrangian and Hamiltonian Systems* |
| the orbit method | the construction of the representations from the coadjoint orbits | *Poisson Geometry*, §Casimirs and Symplectic Leaves |

The moment map is the geometric form of the conserved quantity of a symmetry, and the symplectic reduction is the operation that removes the symmetry and produces the reduced phase space. The quotient is the geometric counterpart of the procedure by which a mechanical system with a symmetry is reduced to a system of fewer degrees of freedom.

## The Symplectic Group and Linear Symplectic Geometry

The linear symplectic geometry is the geometry of a vector space with an alternating nondegenerate form, and its automorphism group is the symplectic group.

| Object | The property it has | Introduced in |
|---|---|---|
| a symplectic vector space $(V,\omega)$ | a vector space with a nondegenerate alternating form, of dimension $2n$ | *Symplectic Forms and Poisson Brackets* |
| a symplectic basis | a basis with $\omega(e_i,f_j) = \delta_{ij}$ and $\omega(e_i,e_j) = \omega(f_i,f_j) = 0$ | *Symplectic Forms and Poisson Brackets* |
| the symplectic group $Sp(2n,K)$ | the matrices with $A^{\mathsf{T}}JA = J$, contained in $SL$ | *Symplectic Forms and Poisson Brackets*; *The Unitary and Symplectic Groups* |
| the symplectic Lie algebra $\mathfrak{sp}(2n,K)$ | $X^{\mathsf{T}}J + JX = 0$, of dimension $n(2n+1)$ | *Symplectic Forms and Poisson Brackets* |
| the Lagrangian Grassmannian $\operatorname{Lag}(V)$ | the variety of the Lagrangian subspaces, of dimension $\tfrac12n(n+1)$ | *Symplectic Forms and Poisson Brackets* |
| the Pfaffian $\operatorname{Pf}(\Omega)$ | the square root of $\det\Omega$, invariant up to $\det A$ | *Symplectic Forms and Poisson Brackets* |
| the Liouville form $\omega^{\wedge n}/n!$ | the volume form of the linear symplectic space | *Symplectic Forms and Poisson Brackets* |

The symplectic group is the isometry group of the alternating form, and its linear geometry is the model of the symplectic geometry at a point: the Darboux theorem identifies the tangent space at one point with the linear symplectic space, and the Lagrangian Grassmannian is the manifold of the Lagrangian subspaces through that point.

## Warnings

An object that a reader may expect among the symplectic geometries, and does not find, is recorded with the reason.

| Object | Why it is not listed as a symplectic geometry | Introduced in |
|---|---|---|
| a contact manifold | odd-dimensional, with a maximally nonintegrable hyperplane field instead of a closed form | *Contact Geometry* |
| the Reeb vector field | the odd-dimensional analogue of the Hamiltonian field, belonging to the contact geometry | *Contact Geometry*, §The Reeb Vector Field |
| an odd-dimensional manifold | no nondegenerate alternating form exists on an odd-dimensional space | *Symplectic Forms and Poisson Brackets*, §Non-Degeneracy and the Symplectic Basis |
| a Poisson manifold that is not symplectic | the Poisson tensor may be degenerate; it foliates into symplectic leaves but is not a symplectic manifold | *Poisson Geometry* |
| a symplectic form that is not Kähler | the compatible almost complex structure need not be integrable | *Symplectic Geometry*, §Compatible Almost Complex Structures |
| the symplectomorphism group | infinite-dimensional, its study belongs to the diffeomorphism groups | *Diffeomorphism Groups* |
| a Riemannian metric as a symplectic form | a metric is symmetric and nondegenerate but not alternating | *Riemannian Geometry* |

## Summary

This article has listed the symplectic geometries of the corpus. The symplectic manifolds and their forms open the list, with the standard form, the volume, the cotangent bundle and the Lagrangian submanifolds; the Darboux theorem and the absence of a local invariant follow; the Hamiltonian vector fields and the Poisson bracket are recorded with the Poisson manifolds, the Casimir functions, the symplectic leaves and the star product; the moment maps and the symplectic reduction follow with the coadjoint orbits and the orbit method; and the linear symplectic geometry closes the list with the symplectic group, its Lie algebra, the symplectic basis and the Lagrangian Grassmannian. Beside the examples stand the non-examples: a contact manifold is odd-dimensional and is not symplectic, a Poisson manifold may be degenerate, an odd-dimensional manifold carries no symplectic form, and a compatible almost complex structure need not be integrable.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following, and they are the symbols of the articles that introduce them.

| Symbol | Meaning |
|---|---|
| $\omega$, $\omega_0$, $\omega^{\wedge m}/m!$ | Symplectic form, standard form, symplectic volume |
| $T^*Q$, $\theta = \sum_i p_i\,dq^i$ | Cotangent bundle and tautological form |
| $X_f$, $\{f,g\}$ | Hamiltonian vector field, Poisson bracket |
| $(P,\pi)$, Schouten bracket, Casimir | Poisson manifold and its structures |
| $\mu : M \to \mathfrak{g}^*$, $M/\!/G$ | Moment map, symplectic quotient |
| $Sp(2n,K)$, $\mathfrak{sp}(2n,K)$, $J$ | Symplectic group, Lie algebra, matrix of the form |
| $\operatorname{Lag}(V)$, $\operatorname{Pf}(\Omega)$ | Lagrangian Grassmannian, Pfaffian |
| $g_J$, $J$ | Compatible metric and almost complex structure |
| $\mathbb{R}$ | The standard number systems of the corpus |
| $\operatorname{Symp}(M,\omega)$, $\mathcal{L}_X$ | The symplectomorphism group of $(M,\omega)$; the Lie derivative |

## Further Reading

- Vladimir I. Arnold, *Mathematical Methods of Classical Mechanics* (Springer, 2nd ed. 1989), for the symplectic form, the Hamiltonian systems and the reduction.
- Ralph Abraham and Jerrold E. Marsden, *Foundations of Mechanics* (Benjamin/Cummings, 2nd ed. 1978), for the moment maps, the symplectic reduction and the Hamiltonian actions.
- Victor Guillemin and Shlomo Sternberg, *Symplectic Techniques in Physics* (Cambridge University Press, 1984), for the moment map, the coadjoint orbits and the reduction in the geometric form.
- Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology* (Oxford University Press, 3rd ed. 2017), for the global symplectic geometry, the Darboux theorem and the symplectomorphism group.
