# __Equivariant Maps and Equivariant Homotopy__

## Introduction

An **equivariant map** between spaces with an involution is a continuous map that commutes with the two involutions, and an **equivariant homotopy** is a homotopy that is equivariant at every stage. The two notions make the spaces with an involution and their equivariant maps into a category, the category already met in *Spaces with an Involution and the Orbit Space*, and they impose on the homotopy theory of that category the same questions that ordinary homotopy theory imposes on spaces: which maps are equivalences, what a homotopy class is, and which invariants see the difference. This article develops the answers for the involution. The central fact is that an equivariant homotopy descends to the orbit spaces and restricts to the fixed sets, so that the orbit space and the fixed set are both functors on the equivariant homotopy category; a second fact is that the equivariant homotopy classes to a space with the trivial involution are the ordinary homotopy classes from the orbit space.

The article continues *Spaces with an Involution and the Orbit Space*, whose orbit functor and quotient results it uses, and it precedes *Two-Fold Coverings and the Borel Construction*. It keeps the group of order two, and it records constructions that apply to any finite group with the same proofs; the general equivariant homotopy theory, with its equivariant Whitehead theorem and its cell complexes, is used by the later articles of this Part and is cited from the standard references rather than developed.

Nothing analytic and nothing geometric is used. The interval $I = [0,1]$ is the unit interval of the homotopy, read only for its topology; no metric is chosen on any space and no length or angle is read from the constructions.

## Equivariant Maps

### The Morphisms Revisited

**Definition.** Let $(X,\sigma)$ and $(Y,\tau)$ be spaces with involutions. An **equivariant map**, or **$\mathbb{Z}/2$-map**, is a continuous map $f : X \to Y$ with

$$
f \circ \sigma = \tau \circ f .
$$

The equivariant maps are the morphisms of $\mathbf{Top}^{\mathbb{Z}/2}$, and the identity and the composites of equivariant maps are equivariant.

**Proposition.** An equivariant map carries the orbit of $x$ into the orbit of $f(x)$, and it restricts to a map $X^{\sigma} \to Y^{\tau}$ of the fixed sets. If $f$ is a homeomorphism and $f^{-1}$ is equivariant, then $f$ is an isomorphism of spaces with involution.

**Proof.** The first statement is $f(\{x,\sigma x\}) \subseteq \{f(x), \tau f(x)\}$, which is the defining identity read on the orbit; the second is that a fixed point satisfies $f(x) = f(\sigma x) = \tau f(x)$; the third is the definition of an isomorphism in $\mathbf{Top}^{\mathbb{Z}/2}$.

### The Induced Maps on the Orbit Space and the Fixed Set

**Theorem.** An equivariant map $f : (X,\sigma) \to (Y,\tau)$ induces a unique continuous map

$$
\bar f : X/\sigma \longrightarrow Y/\tau, \qquad \bar f(\{x,\sigma x\}) = \{f(x), \tau f(x)\},
$$

and a map $f^{fix} : X^{\sigma} \to Y^{\tau}$ by restriction; the two assignments are functorial, and the square

$$
\begin{array}{ccc}
X & \xrightarrow{\ f\ } & Y \\
\downarrow \pi_{X} & & \downarrow \pi_{Y} \\
X/\sigma & \xrightarrow{\ \bar f\ } & Y/\tau
\end{array}
$$

commutes.

**Proof.** The induced map is that of *Spaces with an Involution and the Orbit Space*; the restriction to the fixed sets is $X^{\sigma} \to Y^{\tau}$ by the proposition; functoriality is that the construction preserves identities and composites; the square commutes by the definition of $\bar f$.

## Equivariant Homotopy

### Definition

**Definition.** Let $f, g : X \to Y$ be equivariant maps, and let $I = [0,1]$ carry the trivial involution. An **equivariant homotopy** from $f$ to $g$ is a continuous map

$$
H : X \times I \longrightarrow Y
$$

equivariant with respect to the involution $\sigma \times \mathrm{id}_{I}$ on $X\times I$ and $\tau$ on $Y$, with $H(x,0) = f(x)$ and $H(x,1) = g(x)$ for all $x$. One writes $f \simeq_{\mathbb{Z}/2} g$, or $f \simeq_{G} g$ when the group is named.

Equivalently, a homotopy is a path $t \mapsto H(\cdot, t)$ in the set of equivariant maps from $X$ to $Y$, with the compact-open topology on that set; the map $H$ is equivariant exactly when each $H(\cdot,t)$ is equivariant.

**Proposition.** Equivariant homotopy is an equivalence relation on the equivariant maps from $X$ to $Y$, compatible with composition: if $f \simeq_{G} f'$ and $g \simeq_{G} g'$ then $g \circ f \simeq_{G} g' \circ f'$. Consequently there is a category whose objects are the spaces with involution and whose morphisms are the equivariant homotopy classes of equivariant maps.

**Proof.** Reflexivity is the constant homotopy; symmetry is the reparametrisation $t \mapsto 1-t$; transitivity is the concatenation of homotopies, reparametrised to the two halves of $I$; both reparametrisations are continuous and equivariant because they do not involve $X$. For composition, $g \circ f$ is homotopic to $g' \circ f$ by composing $g'$ with the homotopy from $f$ to $f'$, and $g' \circ f$ is homotopic to $g' \circ f'$ by composing the homotopy from $g$ to $g'$ with $f'$; both composites are equivariant.

**Definition.** The **equivariant homotopy category** of spaces with involution has the spaces with involution as objects and the equivariant homotopy classes as morphisms.

### Equivariant Homotopy Equivalence

**Definition.** An equivariant map $f : X \to Y$ is an **equivariant homotopy equivalence**, or a **$G$-homotopy equivalence**, when there is an equivariant map $g : Y \to X$ with

$$
g \circ f \simeq_{G} \mathrm{id}_{X}, \qquad f \circ g \simeq_{G} \mathrm{id}_{Y} .
$$

The map $g$ is an equivariant homotopy inverse of $f$, and the spaces are equivariantly homotopy equivalent.

**Proposition.** If $f$ is an equivariant homotopy equivalence, then $f$ is an ordinary homotopy equivalence; the forgetful functor to spaces sends $G$-homotopy equivalences to homotopy equivalences.

**Proof.** An equivariant homotopy is a homotopy when the involutions are forgotten, so the same $g$ is an ordinary homotopy inverse.

The converse fails: an ordinary homotopy equivalence need not be equivariant, and even an equivariant map that is an ordinary homotopy equivalence need not be an equivariant one, since the homotopies can move the fixed sets. The invariants of the next section measure the difference.

## Invariants of Equivariant Homotopy

### Fixed Sets and the Fixed-Set Functor

**Theorem.** Let $f : X \to Y$ be an equivariant map and $H$ an equivariant homotopy from $f$ to $g$. Then $H$ restricts to a homotopy $X^{\sigma} \times I \to Y^{\tau}$ from $f^{fix}$ to $g^{fix}$. Consequently an equivariant homotopy equivalence induces a homotopy equivalence of the fixed sets.

**Proof.** If $x \in X^{\sigma}$ then $\sigma x = x$, so $H(x,t) = H(\sigma x, t) = \tau H(x,t)$, and $H(x,t) \in Y^{\tau}$ for every $t$; the restriction is continuous and has the required endpoint values. For the second statement, apply the restriction to the two homotopies that exhibit the equivalence, and to the two equivariant homotopy inverses.

**Corollary.** An equivariant homotopy equivalence $f$ induces homotopy equivalences $f^{fix} : X^{\sigma} \to Y^{\tau}$ and, for any subgroup of $\mathbb{Z}/2$, on the fixed sets of the subgroup. In particular the fixed set is a homotopy invariant of the equivariant homotopy type, not only of the underlying space.

**Proof.** The group $\mathbb{Z}/2$ has two subgroups: the trivial one, whose fixed set is the whole space, and the whole group, whose fixed set is $X^{\sigma}$. The restriction to the two is the statement.

### Orbit Spaces and Descent

**Theorem.** Let $H$ be an equivariant homotopy from $f$ to $g$. Then $H$ descends to a homotopy

$$
\bar H : (X/\sigma)\times I \longrightarrow Y/\tau, \qquad \bar H(\{x,\sigma x\}, t) = \bar H(x,t),
$$

from $\bar f$ to $\bar g$. Consequently an equivariant homotopy equivalence induces a homotopy equivalence of the orbit spaces.

**Proof.** The map $X \times I \to Y$ is equivariant for $\sigma \times \mathrm{id}$ and $\tau$. The quotient $(X \times I)/(\sigma \times \mathrm{id})$ is $(X/\sigma) \times I$, because the involution is trivial on the factor $I$, and the product comparison map is an isomorphism when one factor carries the trivial action; this is a case of the product formula that holds for a trivial factor. Hence $H$ descends through the quotient to the stated map, which is continuous by the universal property and is a homotopy between the two induced maps.

**Corollary.** The orbit-space functor sends equivariant homotopy equivalences to homotopy equivalences, and it respects homotopy classes: if $f \simeq_{G} g$ then $\bar f \simeq \bar g$.

**Proof.** The descent theorem applied to the homotopy and to the two homotopies of an equivalence.

### Homotopy Classes to a Trivial Object

**Theorem.** Let $Y$ carry the trivial involution. Then the correspondence $f \mapsto \bar f$ is a bijection

$$
[X/\sigma, Y] \ \cong \ [X, Y_{tr}]^{G}
$$

between the ordinary homotopy classes of maps $X/\sigma \to Y$ and the equivariant homotopy classes of equivariant maps $X \to Y_{tr}$.

**Proof.** The correspondence is a bijection at the level of maps by the universal property, and it passes to homotopy classes because the cylinder $(X\times I)/\sigma$ is $(X/\sigma)\times I$ by the descent theorem; a homotopy on either side corresponds to a homotopy on the other.

**Corollary.** For a target with the trivial involution the equivariant homotopy class of an equivariant map is determined by the homotopy class of the induced map on the orbit space, and conversely; equivalently, the fixed-set and orbit-space invariants of the source determine the equivariant homotopy class of every map into a trivial object.

**Proof.** The assertion is the bijection of the theorem, read as the statement that no information beyond the induced map on the orbit space is carried by an equivariant map into a trivial object.

## The Homotopy Extension Property

The equivariant theory needs one technical tool to be usable: the equivariant homotopy extension property, which demands the extension of an equivariant homotopy from an invariant subspace.

**Definition.** A pair $(X,A)$ of spaces with involution, with $A$ invariant, has the **equivariant homotopy extension property** when for every space with involution $Y$ and every pair of maps $X \times \{0\} \to Y$ and $A \times I \to Y$ that agree on $A \times \{0\}$, there is an equivariant extension $X \times I \to Y$.

**Theorem (sketch).** If $(X,A)$ is a pair of spaces with involution and $A$ is a retract by deformation of an invariant open neighbourhood, then $(X,A)$ has the equivariant homotopy extension property; and the corresponding statement holds for the cell complexes of the later articles, where the cells are attached equivariantly.

**Proof sketch.** Take a continuous function $\varphi : X \to I$ with $\varphi = 0$ on $A$ and $\varphi = 1$ off the neighbourhood, chosen invariant by averaging over the group; the ordinary homotopy extension, carried out with the retraction of the neighbourhood onto $A$ and the bump function $\varphi$, is then equivariant because every ingredient is. The construction is the standard one for a $G$-space and is given in the references.

**Remark.** The property is the technical hypothesis that makes the equivariant homotopy category behave like the ordinary one: the equivariant Whitehead theorem, which says that an equivariant map between appropriate cell complexes that is an equivariant homotopy equivalence on all fixed sets is an equivariant homotopy equivalence, requires it. The theorem is cited from the references and is not proved here.

## Summary

An equivariant map between spaces with an involution commutes with the involutions; it induces a map on the orbit spaces and restricts to the fixed sets, and both assignments are functorial. An equivariant homotopy is a homotopy that is equivariant at every stage, and it is an equivalence relation compatible with composition, so the spaces with involution and the equivariant homotopy classes form a homotopy category. An equivariant homotopy equivalence is an equivariant map with an equivariant homotopy inverse; it is an ordinary homotopy equivalence, and it induces homotopy equivalences on the fixed sets and on the orbit spaces, the first by restricting the homotopy and the second by descending it through the quotient, which is legitimate because the cylinder of $X$ has orbit space $(X/\sigma)\times I$. For a target with the trivial involution the induced-map correspondence is a bijection on homotopy classes, $[X/\sigma, Y] \cong [X, Y_{tr}]^{G}$, and the equivariant homotopy type of the fixed set and of the orbit space are invariants of the equivariant homotopy type. The equivariant homotopy extension property and the equivariant Whitehead theorem are the technical tools of the subject; they are stated and cited, and the former is sketched.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(X,\sigma)$, $(Y,\tau)$ | Spaces with involutions, with the involutions written $\sigma$, $\tau$ |
| equivariant map | Continuous $f$ with $f\sigma = \tau f$ |
| $\bar f$ | The induced map $X/\sigma \to Y/\tau$ |
| $f^{fix}$ | The restriction $X^{\sigma} \to Y^{\tau}$ |
| $I = [0,1]$ | The unit interval with the trivial involution |
| $H : X\times I \to Y$ | An equivariant homotopy |
| $f \simeq_{G} g$ | Equivariantly homotopic equivariant maps |
| $G$-homotopy equivalence | Equivariant $f$ with an equivariant homotopy inverse |
| $[X,Y]^{G}$ | Equivariant homotopy classes of equivariant maps |
| $[X/\sigma, Y] \cong [X, Y_{tr}]^{G}$ | The homotopy-class adjunction for trivial target |
| equivariant HEP | Equivariant homotopy extension property for an invariant pair |
| equivariant Whitehead theorem | Cited: equivariant homotopy equivalence detected on fixed sets |

## Further Reading

- Tammo tom Dieck, *Transformation Groups* (de Gruyter, 1987), for equivariant homotopy, equivariant homotopy equivalences and the equivariant Whitehead theorem.
- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for equivariant maps, equivariant homotopy and the homotopy extension property for $G$-spaces.
- Glen E. Bredon, *Equivariant Cohomology Theories* (Springer Lecture Notes, 1967), for the equivariant homotopy category and its invariants.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the ordinary homotopy extension property and the Whitehead theorem that the equivariant version generalises.
- Saunders Mac Lane, *Categories for the Working Mathematician*, 2nd ed. (Springer, 1998), for the homotopy category as a quotient category and for naturality of the induced maps.
- Ryszard Engelking, *General Topology* (Heldermann, revised ed. 1989), for the compact-open topology on the set of maps and the adjunction that makes a homotopy a path of maps.
