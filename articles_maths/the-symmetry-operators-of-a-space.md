
# __The Symmetry Operators of a Space__

## Introduction

A **symmetry operator** of a space $X$ is an operator on $X$ that preserves the chosen structure: an isometry of the chosen distance or form, read as an operator rather than as a point of a group. The operators of *Operators on a Symmetry Group* are built from a given symmetry group and act on its functions; this article starts one step earlier and asks which operators of $X$ are symmetries, that the group they form is a group, and what the action of that group organises — the orbits, which are the geometric figures the structure singles out, and the invariants, which are the functions that the symmetries cannot change. The two articles are the two directions of the same datum: the earlier one takes a symmetry group as given and builds its operator layer, this one takes the space and the structure and extracts the maximal symmetry group with its orbit decomposition.

The article stays inside the operator layer and uses no involution on the elements and no adjoint; those are the group `- * Theory` and the group `- * Operator Theory` of this category. The isometries of a form and the group they form are *Isometries and Orthogonal Transformations*; the realisation of the symmetry of a figure and the finiteness of a point group are *Symmetry, Point and Crystallographic Groups*; the quotient of a space by a group of operators, the orbit map and the invariant functions are *Group Actions and Structure*; and the automorphism group of a structure with the hierarchy of its symmetry groups is *Transformation Groups*. The measure that makes the averaging over a compact symmetry group rigorous is the Haar measure of *Locally Compact Groups and Haar Measure*, in Part III. None of that is re-derived.

The article has five sections: the symmetry operators and the group they form; the two levels of symmetry, the structural and the metric; the orbits; the invariants and the orbit space; and the worked cases. Throughout, $X$ is a space with a chosen distance, or a finite-dimensional space $V$ over a field of characteristic not $2$ with a chosen non-degenerate quadratic form $Q$ and its polar form $B$, and $G = \operatorname{Sym}(X)$ is the group of symmetry operators.

## The Symmetry Operators and the Group They Form

### Symmetry Operators

**Definition.** A **symmetry operator** of $X$ is a bijection $T : X \to X$ preserving the chosen structure: a distance-preserving bijection $d(Tx, Ty) = d(x, y)$ when $X$ is metric, or a linear isomorphism $T \in GL(V)$ with $Q(Tv) = Q(v)$ for all $v$ when $X = V$ is a quadratic space. The symmetry operators form the **symmetry group** $\operatorname{Sym}(X)$ under composition, and for a quadratic space $\operatorname{Sym}(V, Q) = \operatorname{O}(V, Q)$ is the orthogonal group, a subgroup of $GL(V)$.

**Proposition.** The symmetry operators are closed under composition and under inversion, contain the identity, and form a group; for a quadratic space the condition $Q(Tv) = Q(v)$ is equivalent to the preservation of the polar form, $B(Tu, Tv) = B(u, v)$ for all $u, v$, and is verified on a spanning set.

**Proof.** The composite of two structure-preserving bijections preserves the structure and the inverse of one does, so the set is a group. The equivalence of the two preservation conditions is the polarisation identity $B(u,v) = \tfrac12\bigl(Q(u+v) - Q(u) - Q(v)\bigr)$, valid because the characteristic is not two, applied to $Tu, Tv$; a form identity holding on a spanning set of pairs holds everywhere by linearity of the form in each argument.

**Remark (the group is not intrinsic to the set).** The same set $X$ with a different chosen form has a different symmetry group: $V = \mathbb{R}^2$ with $x^2+y^2$ has $\operatorname{O}(2)$ of dimension one as a manifold, while $V$ with $x^2-y^2$ has $\operatorname{O}(1,1)$, and with the degenerate form $x^2$ the symmetry group is larger and not reductive. The dependence on the chosen form is the boundary test of the part, and the example shows that "the symmetry operators of a space" is a misleading abbreviation for "of a space with its chosen structure".

### The Two Levels of Symmetry

**Definition.** Let $X$ carry a coarser structure and a finer structure, as a smooth manifold carries its smooth structure and its metric. The **structural symmetry group** $\operatorname{Aut}(X, \text{structure})$ is the group of bijections preserving the coarse structure, and the **metric symmetry group** $\operatorname{Isom}(X, g) \subseteq \operatorname{Aut}(X, \text{structure})$ is the subgroup preserving the finer one; the inclusion is the hierarchy

$$
\operatorname{Sym}(X) = \operatorname{Isom}(X, g) \;\subseteq\; \operatorname{Aut}(X, \text{structure}) \;\subseteq\; \operatorname{Sym}(X^{\mathrm{set}}) = \operatorname{Bij}(X),
$$

and each inclusion can be strict. This is *Transformation Groups*, where the automorphism group of a structure is defined for a general structure; the metric case is the specialisation to the Riemannian or quadratic structure, and the properness of the inclusion is the difference between the differentiable and the isometric classification of a manifold.

**Proposition.** A symmetry operator is determined by its value and its differential at a single point when $X$ is connected: if two isometries agree at $p$ and have the same differential there, they agree everywhere.

**Proof.** The isometry $T_1^{-1}T_2$ fixes $p$ and has identity differential at $p$; the set of its fixed points is closed and the set of points where its differential is the identity is open, and a closed and open subset of a connected manifold is everything.

**Remark.** The rigidity is the geometric content of the second level: the finer the structure, the smaller the symmetry group and the more a single jet determines. The extreme cases are the smooth structure, whose automorphism group is enormous, and the metric, whose group is a finite-dimensional Lie group by the theorem of Myers–Steenrod; the theorem that $\operatorname{Isom}(X,g)$ is a Lie group, and the quotient theory of its orbits, are *Transformation Groups*.

## The Orbits

### Orbits of the Symmetry Group

**Definition.** The **orbit** of $x \in X$ under the symmetry group is

$$
G \cdot x = \{Tx : T \in G\},
$$

and the orbits partition $X$, because the relation $x \sim y$ iff $y \in G\cdot x$ is an equivalence relation. The orbit of $x$ is the figure that the chosen structure and the group jointly single out at $x$; the action is **transitive** when there is one orbit, in which case $X$ is a **homogeneous** space of $G$ and is identified with $G/G_x$ by the orbit–stabiliser theorem, $G_x$ the stabiliser of $x$.

**Proposition.** The orbit $G\cdot x$ is the smallest $G$-stable subset containing $x$, and it is invariant in the sense that $T(G \cdot x) = G \cdot x$ for every $T \in G$. If the action is transitive then every point is carried to every other by a symmetry operator, so no point is distinguished.

**Proof.** Stability is the group law; minimality is that any $G$-stable subset containing $x$ contains $T x$ for every $T$; transitivity is the definition.

### The Orbit Map and Its Fibres

**Definition.** The **orbit map** is the surjection

$$
\theta : X \longrightarrow X/G, \qquad \theta(x) = G \cdot x,
$$

onto the set $X/G$ of orbits, and its fibres are the orbits. The map is $G$-equivariant when $X/G$ carries the trivial action, $\theta(Tx) = \theta(x)$.

**Proposition.** For a group action the orbit map is the universal $G$-invariant map out of $X$: a map $f : X \to Y$ is invariant, $f(Tx) = f(x)$ for all $T \in G$, exactly when it factors as $f = \bar f \circ \theta$ through a map $\bar f : X/G \to Y$. Hence the invariant functions on $X$ are exactly the functions on the orbit space $X/G$, and the orbit space is the sharpest quotient on which the symmetry acts trivially.

**Proof.** If $f$ is invariant it is constant on each orbit, so $\bar f$ is well defined on $X/G$; conversely a map through $\theta$ is invariant because $\theta$ is. The identification of invariant functions with functions on $X/G$ is the same statement for $Y$ the scalars.

**Remark.** The quotient $X/G$ is a set, not in general a space with the structure of $X$: it is a smooth manifold when the action is free and proper, and otherwise an orbifold or a stratified space, and the regularity of the quotient is the content of the differentiable slice theorem, *Group Actions and Structure* for the finite case and *Transformation Groups* for the smooth one. The set-theoretic statement above needs no regularity and is what the invariants see.

### Transitivity and the Classification of Orbits

**Proposition.** The orbits of $G$ on $X$ are the transitive $G$-sets appearing in the decomposition, and each orbit is isomorphic as a $G$-set to $G/G_x$; the orbits are classified up to isomorphism by the conjugacy classes of the stabilisers.

**Proof.** This is the orbit–stabiliser theorem together with the observation that $G/T G_x T^{-1} = G_{Tx}$; two points have isomorphic orbits exactly when their stabilisers are conjugate.

## The Invariants

### Invariant Functions and the Fixed Space

**Definition.** A function $f : X \to k$ is **invariant** when $f(Tx) = f(x)$ for every symmetry operator $T$ and every $x$; the invariant functions form the subspace $\mathcal{F}(X)^G$ of the functions on $X$, and by the orbit-map proposition it is the space of functions on the orbit space $X/G$. When $X = V$ is a quadratic space and $k$ a field, the invariant functions are the **invariants of the form**, and the invariant polynomials form the **ring of invariants** $k[V]^G$.

**Proposition.** The invariant functions are the common fixed space of the action operators: $\mathcal{F}(X)^G = \bigcap_{T \in G}\ker(\pi(T) - \mathrm{id})$. The invariant polynomials are closed under multiplication and addition, so the ring of invariants is a subalgebra of the polynomial ring.

**Proof.** The first statement is the definition of invariance rewritten; the second is that the product and the sum of invariant polynomials are invariant, the action on polynomials being by the substitution $f \mapsto f(T^{-1}\cdot)$.

### The Polynomial Invariants of the Classical Forms

**Theorem (first fundamental theorem, examples).** For the classical symmetry groups acting on their defining spaces, the invariant polynomials are generated by the form:

- $\operatorname{O}(V, Q)$ on a quadratic space: $k[V]^{\operatorname{O}(V,Q)} = k[Q]$, the polynomials in the quadratic form;
- $\operatorname{U}(n)$ on $\mathbb{C}^n$ with the standard Hermitian form: the invariants are the polynomials in the Hermitian norm $\lVert z\rVert^2$;
- for a finite reflection group $W$ on $V$: the invariants are a polynomial ring $k[V]^W = k[f_1, \ldots, f_n]$ on $n$ algebraically independent invariants, the fundamental degrees summing to the order of $W$.

**Proof sketch.** The invariants are characterised by the averaging operator $\pi \mapsto \frac{1}{\lvert G\rvert}\sum_{T}\pi(T)$ for a finite group, which projects onto the invariants and shows that the invariant polynomials separate the orbits when the action is finite; for the full orthogonal group the classical reduction to the symmetric algebra and the Weyl integration formula identify the algebra of invariants with the symmetric algebra of the invariants of the defining representation, giving $k[Q]$; the reflection-group statement is Chevalley's theorem, whose proof uses the Jacobian and the pseudoreflections.

**Remark.** The theorem is quoted, not proved; the invariant theory of the classical groups is its own subject and the reader is referred to Weyl's *The Classical Groups*. For the present article the consequence is what matters: the invariants of a form are the functions of the form, so the orbit of a vector under the orthogonal group is determined by the value of $Q$ at the vector.

### Invariants Separate Closed Orbits

**Proposition.** Let $G$ be a compact symmetry group acting continuously on a compact space $X$. Then the invariant continuous functions separate the orbits: two points lie in the same orbit if and only if every invariant function takes the same value at them.

**Proof.** If the orbits are distinct, compactness makes them disjoint compact sets; a continuous function taking the value $0$ on one and $1$ on the other is constructed by Urysohn, and its average over $G$ against the Haar measure is invariant, continuous, and still separates them.

**Remark.** The averaging uses the Haar measure of *Locally Compact Groups and Haar Measure*, Part III; the proposition is the source of the maxim that a compact symmetry group is detected by its invariants, while a noncompact one in general is not.

## Worked Cases

**Example (the sphere).** Let $X = \mathbb{R}^n$ with the Euclidean form and $G = \operatorname{O}(n)$. The orbits are the spheres $\lVert x\rVert = r$, the origin alone being the orbit of radius $0$, so the orbit space is $[0, \infty)$ and the invariant functions are the functions of $r = \lVert x\rVert$, equivalently of the quadratic form $Q(x) = \lVert x\rVert^2$; the ring of invariants is $k[Q]$. The unit sphere $S^{n-1}$ is the orbit of radius one, and it is homogeneous, being $SO(n)/SO(n-1)$.

**Example (the hyperbolic plane).** Let $X = \mathbb{R}^2$ with the form $Q(x) = x_1^2 - x_2^2$ of signature $(1,1)$ and $G = \operatorname{O}(1,1)$ its symmetry group. The orbits are the four families of level sets of $Q$: the two-sheeted hyperbolas $Q = r^2 > 0$, the upper and the lower branch being separate orbits of the identity component; the two hyperbolas $Q = -r^2 < 0$; the four rays $Q = 0$ off the origin; and the origin. The invariant functions are the functions of $Q$, which do not separate the two branches of a hyperbola, and the identity component separates them by a sign.

**Example (the symmetry operators of a figure).** Let $F$ be a figure in the plane and $G = \operatorname{Sym}(F)$ its symmetry group, *Symmetry, Point and Crystallographic Groups*. The orbits of $G$ on the vertices of $F$ are the vertex orbits, and the orbit–stabiliser theorem gives their sizes; the invariant functions on the vertex set are exactly the functions constant on the vertex orbits, one dimension for each orbit, and for the regular $n$-gon the two orbits — vertices and edges — give the invariant functions of the figure. The crystallographic restriction, that a finite-order rotation of a lattice has order $1, 2, 3, 4$ or $6$, is a statement about which symmetry operators a two-dimensional lattice admits.

**Example (a noncompact group with few invariants).** Let $X = \mathbb{R}^2$ with $G = \mathbb{R}^2$ acting by translations. The action is transitive and free, the orbit space is a single point, and the only invariant functions are the constants: a noncompact symmetry group can have arbitrarily complicated orbits with no separating invariants, the opposite of the compact case.

## Summary

A symmetry operator of a space is an operator preserving the chosen structure, and the symmetry operators form a group $\operatorname{Sym}(X)$, a subgroup of the automorphism group of any coarser structure on $X$; for a quadratic space it is the orthogonal group $\operatorname{O}(V, Q)$, whose condition is the preservation of the polar form. The symmetry group is determined by the chosen form and not by the underlying set, and a connected space has a rigid symmetry group, an isometry being determined by its value and differential at one point. The orbits of the symmetry group are the elementary figures the structure and the group single out; they partition the space, the orbit map is the universal invariant map, and the invariant functions are exactly the functions on the orbit space. The invariant polynomials of the classical forms are generated by the form — the polynomials in $Q$ for the orthogonal group, in the Hermitian norm for the unitary group, and a polynomial ring on $n$ fundamental invariants for a finite reflection group — and for a compact group the invariants separate the orbits, by averaging against the Haar measure, while for a noncompact group they need not.

No involution on the elements of the group and no adjoint of an operator is taken here; those are the group `- * Theory` and the group `- * Operator Theory` of this category. The convolution and translation operators of the symmetry group are the two following articles of the present group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X$ | a space with a chosen distance, or a quadratic space |
| $Q$, $B$ | the chosen quadratic form and its polar form |
| $T$ | a symmetry operator; a structure-preserving bijection |
| $\operatorname{Sym}(X)$, $\operatorname{O}(V,Q)$ | the symmetry group; the orthogonal group |
| $\operatorname{Aut}(X,\text{structure})$ | the automorphisms of a coarser structure |
| $G \cdot x$, $G_x$ | the orbit and the stabiliser of $x$ |
| $X/G$, $\theta$ | the orbit space and the orbit map |
| $\mathcal{F}(X)^G$ | the invariant functions |
| $k[V]^G$ | the ring of invariant polynomials |
| $\frac{1}{\lvert G\rvert}\sum_T \pi(T)$ | the averaging projector onto the invariants |
| $\operatorname{Isom}(X,g)$ | the isometry group, a Lie group in the smooth case |

## Further Reading

- Hermann Weyl, *The Classical Groups: Their Invariants and Representations* (Princeton, 1939), for the invariant theory of the classical groups and the fundamental theorems.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 1971), for the orthogonal and unitary groups, their generation and their structure.
- Claude Chevalley, "Invariants of finite groups generated by reflections", *American Journal of Mathematics* **77** (1955), 778–782, for the theorem that the invariants of a finite reflection group form a polynomial ring.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the isometry group of a Riemannian manifold, the rigidity of a single jet and the orbit theory.
- John A. Wolf, *Spaces of Constant Curvature* (McGraw–Hill, 1967), for the model geometries and their symmetry groups, and for the orbits that the classical forms single out.
- Ludwig Bieberbach, "Über die Bewegungsgruppen der euklidischen Räume", *Mathematische Annalen* **70** (1911), 297–336, for the crystallographic groups and the finite point-group part of the symmetry of a discrete set.
