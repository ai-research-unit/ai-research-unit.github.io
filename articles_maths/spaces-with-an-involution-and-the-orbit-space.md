# __Spaces with an Involution and the Orbit Space__

## Introduction

A space with an involution is an object of a category of its own: the space together with the homeomorphism of order two, and the continuous maps that commute with the two involutions. This article treats that category systematically. It defines the **equivariant category** of spaces with an involution, proves that the **orbit-space construction** $X \mapsto X/\sigma$ is a functor and that it is left adjoint to the functor that puts the trivial involution on a space, examines which constructions the orbit functor preserves and which it does not, and records the separation and compactness properties that the orbit space inherits from the space. The orbit space of an involution is the universal quotient that makes the involution trivial, and the functorial language is the exact way to say what the quotient construction does and does not do.

The article continues *Involutions on a Topological Space and the Fixed Set*, which introduced the involution, its fixed set and its orbit space, and it precedes *The Orbit Space of a Free Involution*, which treats the case $X^{\sigma} = \emptyset$ and the covering property of the orbit map. The input from the operator articles is *The Orbit Map* for the quotient topology and the universal property and *Continuous Maps and the Orbit Map* for the induced map on a quotient and the fixed set.

Nothing analytic and nothing geometric is used. The examples are intervals, discrete sets and the sphere with its antipodal involution; no distance, angle or measure occurs.

## The Category of Spaces with an Involution

### Objects and Morphisms

**Definition.** The category $\mathbf{Top}^{\mathbb{Z}/2}$ of **spaces with an involution** has as objects the pairs $(X, \sigma)$ with $X$ a topological space and $\sigma$ a continuous involution of $X$, and as morphisms $(X,\sigma) \to (Y,\tau)$ the continuous maps $f : X \to Y$ with

$$
f \circ \sigma = \tau \circ f .
$$

Such a map is **equivariant**, and the morphisms are the equivariant maps of *Continuous Maps and the Orbit Map* for the group $\mathbb{Z}/2$. Composition is composition of maps, and the identity is the identity map with the action preserved.

**Proposition.** An isomorphism in $\mathbf{Top}^{\mathbb{Z}/2}$ is an equivariant homeomorphism, that is, a homeomorphism $f$ with $f\sigma = \tau f$ and with equivariant inverse. The category has finite products and coproducts, given by the products and the disjoint unions with the componentwise involution, and it has all limits and colimits, computed on the underlying spaces and equipped with the induced involution.

**Proof.** The inverse of an equivariant bijection is equivariant, because the defining identity can be rearranged. Products and coproducts are the usual ones with the coordinatewise and componentwise involutions, and the general limits and colimits are the limits and colimits of the underlying diagram of spaces with the involution induced by the universal property, which exists because the functors defining the (co)limit are compatible with the action.

### The Trivial and the Free Objects

**Definition.** The **trivial involution** on a space $Y$ is $\mathrm{id}_{Y}$, and $Y_{tr}$ denotes the object $(Y, \mathrm{id}_{Y})$. A space with an involution is **free** when $X^{\sigma} = \emptyset$, and it is **trivial** when $\sigma = \mathrm{id}_{X}$.

The assignment $Y \mapsto Y_{tr}$ is a functor $\mathbf{Top} \to \mathbf{Top}^{\mathbb{Z}/2}$ on all continuous maps, since every map commutes with the identity. The free objects are those with no fixed points; the trivial objects are those on which the involution does nothing. The two classes are the extremes among which the general theory lives: a trivial object is its own orbit space, and a free object is the subject of the next article.

## The Orbit-Space Functor

### The Construction on Objects and Maps

**Definition.** The **orbit space** of $(X,\sigma)$ is $X/\sigma$ with the quotient topology, and the **orbit map** is $\pi : X \to X/\sigma$.

**Theorem.** Let $f : (X,\sigma) \to (Y,\tau)$ be a morphism of $\mathbf{Top}^{\mathbb{Z}/2}$. Then $f$ induces exactly one continuous map

$$
\bar f : X/\sigma \longrightarrow Y/\tau, \qquad \bar f(\{x,\sigma x\}) = \{f(x), \tau f(x)\},
$$

and the assignment $(X,\sigma) \mapsto X/\sigma$, $f \mapsto \bar f$ is a functor, the **orbit-space functor**.

**Proof.** The composite $\pi_{Y} \circ f$ is continuous and constant on the orbits of $\sigma$, because $f(\sigma x) = \tau f(x)$; by the universal property of the quotient of *The Orbit Map* it factors through the orbit map of $X$ by a unique continuous map, which is $\bar f$. Functoriality is the uniqueness of the factorisation, as in *Continuous Maps and the Orbit Map*.

### The Adjunction with the Trivial Involution

**Theorem.** The orbit-space functor is left adjoint to the trivial-involution functor:

$$
(-)/\sigma \ \dashv \ (-)_{tr}, \qquad \mathbf{Top}(X/\sigma,\, Y) \ \cong \ \mathbf{Top}^{\mathbb{Z}/2}((X,\sigma),\, Y_{tr})
$$

naturally in the space $Y$ and the object $(X,\sigma)$.

**Proof.** A continuous map $g : X/\sigma \to Y$ corresponds to the equivariant map $g \circ \pi : X \to Y_{tr}$, and every equivariant map $X \to Y_{tr}$ is constant on orbits, hence of this form by the universal property; the correspondence is a bijection, and naturality is the naturality of the universal property.

**Corollary.** The orbit functor preserves all colimits, and it takes the initial object $\emptyset$ to $\emptyset$ and the coproduct of a family to the coproduct of the quotients: for spaces with involutions $(X_{i},\sigma_{i})$,

$$
\Bigl(\bigsqcup_{i} X_{i}\Bigr)/\sigma \ \cong \ \bigsqcup_{i} (X_{i}/\sigma_{i}) .
$$

For a pushout of equivariant maps the orbit space of the pushout is the pushout of the orbit spaces.

**Proof.** A left adjoint preserves colimits; the displayed isomorphism is the coproduct case, with the involution acting componentwise and the orbit map acting componentwise.

## Preservation Properties

### What the Functor Preserves

**Theorem.** The orbit functor preserves colimits, finite coproducts, quotients by invariant subsets and the initial object. It need not preserve limits: in particular it does not preserve products.

**Proof.** The colimit statement is the adjunction. A quotient $X/A$ by an invariant subset $A$ is a colimit and is preserved; a concrete check is that $(X/A)/\sigma = (X/\sigma)/(A/\sigma)$.

### Failure for Products

**Theorem.** The orbit functor does not preserve products in general. For $(X,\sigma)$ the comparison map

$$
(X \times X)/(\sigma \times \sigma) \longrightarrow (X/\sigma) \times (X/\sigma), \qquad \text{orbit of } (x,y) \mapsto (\text{orbit of } x,\ \text{orbit of } y),
$$

is always continuous and surjective, and it need not be injective; when it is injective it need not be a homeomorphism.

**Proof.** The map is continuous by the universal property and is the canonical comparison map of a left adjoint, which preserves colimits and not necessarily limits. For the failure of injectivity, take $X = \{a,b\}$ discrete with $\sigma$ exchanging $a$ and $b$. Then $X/\sigma$ is a point, so $(X/\sigma)\times(X/\sigma)$ is a point. But $X \times X$ has four points and $\sigma\times\sigma$ identifies $(a,a)$ with $(b,b)$ and $(a,b)$ with $(b,a)$, so $(X\times X)/(\sigma\times\sigma)$ has two points; the comparison map sends these two points onto the single point of $(X/\sigma)\times(X/\sigma)$ and is not injective.

The failure is the familiar one that a quotient of a product is not the product of the quotients: the involution on the product has orbits that need not be products of orbits, and the comparison map merges the extra orbits.

### Failure for Subspaces

**Theorem.** An invariant subspace $A \subseteq X$ has the orbit space $A/\sigma$ mapping continuously and bijectively onto its image in $X/\sigma$, but the map $A/\sigma \to X/\sigma$ need not be a homeomorphism onto its image: the quotient topology of $A/\sigma$ can be strictly finer than the subspace topology.

**Proof.** Injectivity is that an orbit in $A$ is an orbit in $X$, and continuity is the functoriality. For the failure, take $X = [0,1]$ with $\sigma(x) = 1-x$ and $A = \{0\} \cup [\tfrac13,\tfrac23] \cup \{1\}$, which is invariant. In $A$ the point $0$ is isolated, so its orbit $\{0,1\}$ is open in the quotient topology of $A/\sigma$, and the corresponding point is isolated in $A/\sigma$. In $X/\sigma$, which is the interval $[0,\tfrac12]$, the same point corresponds to the class of $0$, and the point $0$ is not isolated there; hence the bijection $A/\sigma \to X/\sigma$ is not a homeomorphism onto its image.

## Separation and Compactness of the Orbit Space

**Theorem.** Let $(X,\sigma)$ be a space with an involution.

1. If $X$ is $T_{1}$, then $X/\sigma$ is $T_{1}$.
2. If $X$ is Hausdorff, then $X/\sigma$ is Hausdorff.
3. If $X$ is compact, then $X/\sigma$ is compact.
4. If $X$ is normal, then $X/\sigma$ is normal.

**Proof.** (1) In a $T_{1}$ space the points are closed, hence so are the finite orbits, and a quotient of a space with closed orbits has closed points. (2) Let $\{x,\sigma x\}$ and $\{y, \sigma y\}$ be distinct orbits. Since $X$ is Hausdorff, the two finite sets can be separated by disjoint open sets; intersecting the two open sets with the images of their translates under $\sigma$ (there are finitely many) gives disjoint invariant open sets containing the two orbits, and their images are disjoint open neighbourhoods in $X/\sigma$. (3) The orbit space is a continuous image of a compact space. (4) In a normal space, disjoint closed invariant sets have disjoint invariant open neighbourhoods, by applying normality to the two closed sets and intersecting with the finitely many translates; the images of the invariant open sets separate the images of the closed sets, so $X/\sigma$ is normal.

**Corollary.** The orbit space of a compact Hausdorff space with a continuous involution is compact Hausdorff; the orbit space of a Hausdorff space is Hausdorff. In particular the antipodal quotient of the sphere is compact Hausdorff.

**Proof.** Combine the clauses (2) and (3). The last statement is the sphere case.

**Remark.** The separation clauses are special cases of the corresponding facts for a finite group action, which hold because a finite group action has finitely many translates and the quotient map is closed. The action of an infinite group has no such finiteness, and its orbit spaces can fail to be Hausdorff even for a Hausdorff space; the contrast is one of the reasons the involution case is the tractable one.

## Summary

Spaces with a continuous involution and their equivariant maps form the category $\mathbf{Top}^{\mathbb{Z}/2}$, with limits and colimits computed on the underlying spaces with the induced involution. The orbit-space construction is a functor from this category to the category of spaces, and it is left adjoint to the functor that assigns the trivial involution; the bijection $\mathbf{Top}(X/\sigma, Y) \cong \mathbf{Top}^{\mathbb{Z}/2}((X,\sigma), Y_{tr})$ is the universal property of the quotient. As a left adjoint the orbit functor preserves all colimits, in particular coproducts and quotients by invariant sets; it does not preserve limits, and the natural comparison map $(X\times X)/(\sigma\times\sigma) \to (X/\sigma)\times(X/\sigma)$ is not an isomorphism for a nontrivial involution. An invariant subspace has the orbit space mapping bijectively and continuously onto its image in the ambient orbit space, but the map need not be an embedding, because the quotient topology can be strictly finer than the subspace topology. The orbit space of a $T_{1}$ (respectively Hausdorff, compact, normal) space is again $T_{1}$ (respectively Hausdorff, compact, normal), the Hausdorff and normal cases because a finite group action admits finitely many translates and produces invariant neighbourhoods.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbf{Top}^{\mathbb{Z}/2}$ | The category of spaces with a continuous involution and equivariant maps |
| $(X,\sigma) \to (Y,\tau)$ | A morphism is a continuous $f$ with $f\sigma = \tau f$ |
| $Y_{tr}$ | The space $Y$ with the trivial involution; the functor $(-)_{tr}$ |
| $(-)/\sigma$ | The orbit-space functor; left adjoint to $(-)_{tr}$ |
| $\pi : X \to X/\sigma$ | The orbit map; the unit of the adjunction |
| $\bar f : X/\sigma \to Y/\tau$ | The induced map of a morphism $f$ |
| $(X\times X)/(\sigma\times\sigma) \to (X/\sigma)^2$ | The comparison map; not an isomorphism in general |
| $A/\sigma \to X/\sigma$ | For invariant $A$; bijective and continuous, not always an embedding |
| $T_1$, Hausdorff, compact, normal | Inherited by the orbit space |

## Further Reading

- Tammo tom Dieck, *Transformation Groups* (de Gruyter, 1987), for the category of spaces with an action, the orbit functor and its adjunction with the trivial action.
- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for quotient spaces by finite group actions and their separation properties.
- Saunders Mac Lane, *Categories for the Working Mathematician*, 2nd ed. (Springer, 1998), for adjunctions, preservation of colimits and the comparison maps of a left adjoint.
- Nicolas Bourbaki, *General Topology*, Chapters 1–4 (Springer, 1995), for quotients, invariant open sets and the separation axioms.
- Ryszard Engelking, *General Topology* (Heldermann, revised ed. 1989), for the quotient of a normal space by a finite group action and the inheritance of the separation axioms.
- John L. Kelley, *General Topology* (Van Nostrand, 1955; reprinted Springer, 1975), for quotient maps and product quotients.
