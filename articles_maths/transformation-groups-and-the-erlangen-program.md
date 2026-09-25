
# __Transformation Groups and the Erlangen Program__

## Introduction

This article stands in *Geometry and Manifolds*, immediately after *Homogeneous Spaces*, and it introduces Klein's principle: a geometry is the study of the invariants of a transformation group. The two ingredients are Part II objects and are already available. The homogeneous space $G/H$ belongs to *Homogeneous Spaces*, above, and is cited rather than reintroduced; the Lie group $G$ and its closed subgroups belong to *Lie Groups*, above; and the hierarchy of symmetry groups, $\operatorname{Sym}(X)$ and $\operatorname{Aut}(X)$ and the automorphism groups of structures on $X$, belongs to Part I, in *Transformation Groups*, and is likewise cited. What this article adds is the principle that organises the classical geometries: the passage from a group to the geometry of its invariants, and the pair $(G,H)$ whose coset space is the space of the geometry.

It does not construct $G/H$ again, and it does not develop the structure theory of Lie groups; it reads the classical geometries through the pairs that define them, states the correspondence between a geometry and its automorphism group, and records the limits of the principle. The geometries of constant curvature, and the sphere and the hyperbolic space that carry them, are *Euclidean Geometry*, *Spherical Geometry* and *Hyperbolic Geometry*, earlier in this category.

---

## Klein's Principle

**Definition.** A **Klein geometry** is a pair $(G, H)$ together with the homogeneous space $G/H$, where $G$ is a Lie group and $H$ is a closed subgroup of $G$. The **geometry** of the pair is the study of the structures on $G/H$ that are invariant under the left action of $G$, and its **objects** are the subsets of $G/H \times \cdots \times G/H$ that are invariant under the diagonal action. Two Klein geometries are **isomorphic** if there is an isomorphism of pairs, that is an isomorphism $G \to G'$ carrying $H$ to $H'$.

**Remark.** The pair is more than the space: different pairs can have homeomorphic coset spaces and different geometries. The subgroup $H$ is the structure, in the sense that the invariant structures on $G/H$ correspond to the $H$-invariant structures on the tangent space at the base point: a $G$-invariant tensor field on $G/H$ is the same thing as a tensor on $T_{eH}G/H$ fixed by the isotropy action of $H$.

**Theorem (the principle of Klein).** Let $(G,H)$ be a Klein geometry. Then the group of the automorphisms of the geometry that commute with the action of $G$, that is the group of homeomorphisms $\varphi$ of $G/H$ with $\varphi(gx) = g\varphi(x)$ for every $g \in G$, is $N_G(H)/H$, and the map

$$
G \to \operatorname{Aut}(G/H), \qquad g \mapsto (xH \mapsto gxH) ,
$$

has kernel the largest normal subgroup of $G$ contained in $H$. In particular the action of $G$ on $G/H$ is faithful exactly when $H$ contains no nontrivial normal subgroup of $G$.

**Proof.** That the action is well defined and transitive is the construction of $G/H$ in *Homogeneous Spaces*, above. An element of the kernel fixes $eH$, hence lies in $H$, and therefore lies in every conjugate of $H$, that is in the largest normal subgroup of $G$ inside $H$; conversely such a normal subgroup acts trivially. For the first statement, an equivariant homeomorphism $\varphi$ is determined by the image of the base point, since $G$ acts transitively: if $\varphi(eH) = nH$ then $\varphi(xH) = x\varphi(eH) = xnH$, so $\varphi$ is the map $xH \mapsto xnH$; conversely the map $xH \mapsto xnH$ is well defined exactly when $n$ normalises $H$, since $xH = x'H$ gives $x' = xh$ and $x' nH = xhnH$, which equals $xnH$ for every $h \in H$ exactly when $n^{-1}hn \in H$ for every $h$, that is when $n \in N_G(H)$; and it is equivariant exactly when $gnH = ngH$ for all $g \in G$, which is the same condition. Two such maps coincide exactly when $nH = n'H$. $\square$

**Remark.** The theorem is the exact statement, and it is not the statement that *every* homeomorphism preserving the $G$-invariant structures lies in $N_G(H)/H$. The pair is part of the data: for the Euclidean row of the table below, the group of the pair is $E(n)$ with $H = O(n)$, and $O(n)$ is its own normaliser in $E(n)$, so the only homeomorphism of $\mathbb{R}^n$ equivariant for the whole Euclidean group is the identity, whereas the affine maps of $\mathbb{R}^n$ preserve the flat structure without being equivariant for the action of $E(n)$. What a Klein geometry supplies is the transitive action of $G$ and the geometry on the tangent space at the base point, fixed by the isotropy action of $H$.

**Example.** For the sphere, $G = O(n+1)$ and $H = O(n)$ is the stabiliser of a point, and the kernel is trivial since $O(n)$ contains no nontrivial normal subgroup of $O(n+1)$; the invariant structure is the round metric. For the projective space, $G = PGL(n+1,\mathbb{R})$ and $H$ is the stabiliser of a point of $\mathbb{P}^n$, a parabolic subgroup, and the invariant structure is the incidence relation.

### The Correspondence with Automorphism Groups

**Remark.** The principle supplies a map in the other direction as well. Given a space $X$ with a notion of structure, the geometry of $X$ is studied through the group $\operatorname{Aut}(X)$ of the transformations preserving the structure, and the hierarchy

$$
\operatorname{Sym}(X) \supset \operatorname{Aut}(X, \text{structure}) \supset \cdots
$$

of Part I, in *Transformation Groups*, records the specialisations: a set has only the symmetric group, a space with more structure has the smaller group that preserves it, and the Klein geometries are the case in which the group acts transitively and the structure is recovered from the pair.

**Proposition.** An isomorphism of pairs, that is an isomorphism of Lie groups $\gamma : G \to G'$ with $\gamma(H) = H'$, induces an isomorphism of the Klein geometries, and it induces an isomorphism of the transformation groups of the coset spaces. Conversely an equivariant isomorphism of the geometries, that is a homeomorphism $\varphi : G/H \to G'/H'$ with $\varphi(gx) = \gamma(g)\varphi(x)$ for an isomorphism $\gamma : G \to G'$, is induced by an isomorphism of pairs after the kernels of the two actions are divided out.

**Proof.** For the first statement, $\gamma$ carries the left action of $G$ on $G/H$ to the left action of $G'$ on $G'/H'$, hence carries the $G$-invariant structures to the $G'$-invariant structures. For the second, the kernel of the action of $G$ on $G/H$ is the largest normal subgroup of $G$ inside $H$, by the theorem above, and the same holds for the pair $(G',H')$; dividing by these kernels gives an isomorphism of transformation groups carrying $H$ to $H'$ and the base point to the base point. $\square$

**Remark.** The proposition is the sense in which a Klein geometry determines its pair: not the group itself, which is only determined up to the largest normal subgroup inside $H$, but the transformation group acting faithfully, together with the stabiliser of a base point.

---

## The Classical Geometries Read through Their Groups

**Theorem.** Each of the following is a Klein geometry, and the invariant structure named in the last column is what the geometry studies.

| geometry | $G$ | $H$ | $G/H$ | invariant structure |
|---|---|---|---|---|
| Euclidean | $E(n) = \mathbb{R}^n \rtimes O(n)$ | $O(n)$ | $\mathbb{R}^n$ | the flat metric, lines, distances, angles |
| spherical | $O(n+1)$ | $O(n)$ | $S^n$ | the round metric, great circles, angles |
| hyperbolic | $O(n,1)$ | $O(n)$ | $\mathbb{H}^n$ | the hyperbolic metric, geodesics, angles |
| affine | $GL(n,\mathbb{R}) \rtimes \mathbb{R}^n$ | $GL(n,\mathbb{R})$ | $\mathbb{A}^n$ | parallelism, the affine structure, ratios on a line |
| projective | $PGL(n+1,\mathbb{R})$ | the stabiliser of a point | $\mathbb{P}^n$ | incidence, the cross ratio |
| conformal | $O(n+1,1)$ | the stabiliser of a point and a scale | the conformal sphere | the conformal class of the metric, angles |
| Möbius | the Möbius group, $PSL(2,\mathbb{C})$ | the stabiliser of a point | $\mathbb{C}P^1$ | the complex structure, circles, angles |

**Proof.** In each row $G$ is a Lie group acting transitively on the space, the stabiliser of a base point is the closed subgroup $H$ displayed, and the space is the coset space. For the Euclidean row the translations form a normal subgroup and $E(n)/O(n) = \mathbb{R}^n$; for the spherical and hyperbolic rows the stabiliser of a point is the orthogonal group of the tangent space, of dimension $n$; for the affine row the stabiliser of the origin is $GL(n,\mathbb{R})$; for the projective row the stabiliser of a point is the group of matrices preserving a line, which is parabolic; for the conformal row the stabiliser of a point of the sphere inside $O(n+1,1)$ is the group of similarities of $\mathbb{R}^n$; and the Möbius group acts on the Riemann sphere by Möbius transformations, transitively, with stabiliser the maps $z \mapsto az + b$, that is the rotations and scalings together with the translations. The invariant structure is in each case the structure on the tangent space at the base point fixed by the isotropy action, by the theorem of the previous section; the classical geometries themselves are *Euclidean Geometry*, *Spherical Geometry*, *Hyperbolic Geometry*, *Conformal Geometry* and *Möbius and Lie Sphere Geometry*, all earlier in this category. $\square$

**Remark.** The table is the content of the Erlangen program in the classical cases, and it explains why the classification of the geometries of constant curvature is a classification of Klein geometries: a complete connected Riemannian manifold of constant curvature $\kappa$ is, up to isometry, a quotient of the simply connected space of curvature $\kappa$, which is the coset space of one of the first three rows with the metric that the pair determines.

---

## The Limits of the Principle

**Theorem (the principle is not universal).** There are Riemannian manifolds that are not Klein geometries, because they carry no transitive group of isometries, and there are Klein geometries that are not of constant curvature.

**Proof.** For the first statement, the isometry group of a generic Riemannian metric on a compact manifold is trivial, a standard consequence of the fact that the isometries of a metric form a compact Lie group whose dimension is a lower semicontinuous function of the metric, so that a generic metric admits no nontrivial isometry; on a manifold of dimension at least two a metric with trivial isometry group is not homogeneous, and hence is not the coset space of a transitive group action. For the second statement, the product $S^2 \times S^2$ with the product metric is acted on transitively by $O(3) \times O(3)$, so it is a Klein geometry, while its sectional curvature takes the value $1$ on the planes tangent to a factor and the value $0$ on the planes spanned by a vector of each factor, so it is not of constant curvature. $\square$

**Remark.** The two failures are different in kind. A Klein geometry is homogeneous by definition, so homogeneity is what a Riemannian manifold must have to be presented by a pair; and homogeneity does not force constant curvature, as the product of two spheres shows. Constant curvature enters through the classification of the space forms of the next remark, and not through the definition of a Klein geometry.

**Remark.** The principle is wider than the $(G,H)$ form of it, since a geometry is the study of the invariants of its automorphism group and that group need not be a Lie group acting transitively. Symplectic geometry is the study of the invariants of the group of symplectomorphisms, which is infinite-dimensional and therefore not the group of a pair of the table above, and Riemannian geometry is the study of the invariants of the isometry group, which is a Lie group and rarely transitive. Both are read through the correspondence $G \to \operatorname{Aut}(X)$ of the hierarchy of *Transformation Groups* of Part I, and they are *Symplectic Geometry* and *Riemannian Geometry*, earlier in this category. A **Klein geometry** in the sense of this article is the case in which the automorphism group is a Lie group acting transitively on the space, so that the space is the coset space $G/H$.

**Remark.** The right generalisation is Cartan's: a manifold with a principal bundle and a Cartan connection whose model is a Klein geometry $(G,H)$ is a **Cartan geometry**, in which the pair survives as the model and the manifold need not be homogeneous. A general Riemannian manifold is then a Cartan geometry modelled on the Euclidean pair, and the classical geometries are the case in which the development is globally injective. The theory of the connections involved is *Fibre Bundles, Connections and Curvature*, earlier in this category, and the Cartan geometries with their model pairs belong to *Symmetric Spaces*, the next entry after this article.

---

## Summary

A Klein geometry is a pair $(G,H)$, with $G$ a Lie group and $H$ a closed subgroup, together with the homogeneous space $G/H$ of *Homogeneous Spaces*; the geometry is the study of the $G$-invariant structures on it, and those structures correspond to the structures on the tangent space at the base point fixed by $H$. The action of $G$ on $G/H$ has kernel the largest normal subgroup of $G$ inside $H$, and the automorphisms of the geometry commuting with $G$ form $N_G(H)/H$, so that a Klein geometry determines its pair up to the kernel. Euclidean, spherical, hyperbolic, affine, projective, conformal and Möbius geometry are the Klein geometries of the table, and the classification of the geometries of constant curvature is the classification of the first three rows. The principle is an organising definition of the classical geometries and not a theorem about all manifolds: a generic Riemannian metric admits no transitive group of isometries while homogeneity does not force constant curvature, and the correct generalisation is Cartan's, in which the model pair survives as a Cartan connection and is developed in *Symmetric Spaces*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$ | A Lie group |
| $H$ | A closed subgroup, the isotropy subgroup of a Klein geometry |
| $G/H$ | The homogeneous space of *Homogeneous Spaces*, the space of the geometry |
| Klein geometry | The pair $(G,H)$ together with $G/H$; two words, never hyphenated |
| $\operatorname{Sym}(X)$, $\operatorname{Aut}(X)$ | The symmetry and automorphism groups of a structure, as in Part I's *Transformation Groups* |
| $N_G(H)/H$ | The automorphisms of the Klein geometry commuting with $G$ |
| $E(n) = \mathbb{R}^n \rtimes O(n)$ | The Euclidean group |
| $O(n+1)$, $O(n,1)$, $PGL(n+1,\mathbb{R})$, $PSL(2,\mathbb{C})$ | The groups of the spherical, hyperbolic, projective and Möbius geometries |
| $\kappa$ | The constant curvature of a space form |
| Cartan geometry | The generalisation of a Klein geometry by a Cartan connection, developed in *Symmetric Spaces* |

## Further Reading

- É. Cartan, *La théorie des groupes finis et continus et la géométrie différentielle traitées par la méthode du repère mobile* (Gauthier-Villars, 1937), for the generalisation of the Erlangen program to inhomogeneous spaces.
- S. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for homogeneous spaces, the isotropy action and the invariant structures on $G/H$.
- F. Klein, *Vergleichende Betrachtungen über neuere geometrische Forschungen* (Erlanger Programm, 1872), for the original statement of the principle.
- R. W. Sharpe, *Differential Geometry: Cartan's Generalization of Klein's Erlangen Program* (Springer, 1997), for Cartan geometries modelled on a Klein geometry.
