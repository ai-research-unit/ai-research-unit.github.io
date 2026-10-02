# __Equivariant Maps as Operators__

## Introduction

A continuous map acts on the invariants of a space by functoriality, and *Equivariant Maps and Equivariant Homotopy* has treated the action of a map between spaces with an involution on the space level: an equivariant map descends to the orbit spaces, restricts to the fixed sets, and defines a morphism of the equivariant homotopy category. The present article treats the same maps one layer down, as **operators on the equivariant chain complexes**. An equivariant map is then a chain map commuting with the action of the group, the equivariant maps of a fixed source and target form an algebra of operators, and the two invariants that the category uses — the homology of the orbit space and the equivariant homology of the homotopy quotient — are both computed from that algebra by applying the two natural functors on complexes of modules over the group ring, the coinvariants and the bar construction.

The article has four parts. It records the chain complex of a space with an action as a complex of modules over the group ring; it reads an equivariant map as an operator on that complex and proves the functoriality; it follows the operator through the coinvariant complex and the Borel complex and obtains the induced maps on the two homologies; and it records the fixed part, where the norm operator of the group ring acts. The result is that the two invariants are functors on the equivariant homotopy category, so that equivariantly homotopic maps induce the same maps on both, and that the natural transformation from the coinvariant complex to the Borel complex is compatible with the operators.

The equivariant category, its orbit functor, its equivariant homotopy relation and the equivariant homotopy extension property are those of *Spaces with an Involution and the Orbit Space* and *Equivariant Maps and Equivariant Homotopy*, and the Borel construction for the group of order two is that of *Two-Fold Coverings and the Borel Construction*; the article generalises the last construction from the involution to a group and reads it on the chains. The singular complex, its boundary operator and its functoriality are those of *Simplicial and Singular Homology*; the group ring, the invariants and the coinvariants, the bar resolution and the derived functors of these are those of *Group Cohomology*; the classifying space $BG$, the universal space $EG$ and the bar construction are those of *Classifying Spaces and Cohomology Operations*; and the spectral sequence of a fibration is that of *The Leray–Serre Spectral Sequence*, cited only where the operators pass through it. The general homological algebra of complexes over a ring is the planned *Homological Algebra* of Part I, written in parallel.

Nothing analytic and nothing geometric is used: the whole article is the functoriality of the singular complex, the group ring and two exact functors on modules, and no distance, no norm and no measure occurs. Throughout, $G$ is a group — the group of order two when the article is read against the involution articles, a finite group when an average over the group is taken, and a discrete group in general, so that $EG$ and the bar construction are those of a discrete group; $X$ and $Y$ are spaces with a left action of $G$ by homeomorphisms, written $g \cdot x$, and a **$G$-map** is a continuous map $f : X \to Y$ with $f(g \cdot x) = g \cdot f(x)$. The orbit space is written $X/G$, the homotopy quotient $X_G = EG \times_G X$, and the equivariant homology is $H_n^G(X;R)$; coefficients are taken in a commutative ring $R$ with identity and are written after a semicolon. For $G = \mathbb{Z}/2$ the action is the involution $\sigma$ of the Foundations articles, and $X_G$ is the space denoted $X \times_{\mathbb{Z}/2} S^{\infty}$ there.

## Group Actions and Equivariant Chain Complexes

### The Equivariant Category

The objects are the spaces with a left action of $G$ and the morphisms are the $G$-maps, so that the composition of $G$-maps is a $G$-map and the identity is one; this is the **equivariant category** $G\text{-}\mathbf{Top}$, and for $G = \mathbb{Z}/2$ it is the category $\mathbf{Top}^{\mathbb{Z}/2}$ of *Spaces with an Involution and the Orbit Space*. The orbit functor $X \mapsto X/G$ and, for a $G$-map $f$, the induced map $\bar f : X/G \to Y/G$ are those of that article; the equivariant homotopy relation and the equivariant homotopy category are those of *Equivariant Maps and Equivariant Homotopy*.

### The Chain Complex as a Complex of Modules

The singular chain complex $C_*(X;R)$ of *Simplicial and Singular Homology* carries an action of $G$: a group element $g$ is a homeomorphism of $X$, hence induces the chain map

$$
g_\# : C_n(X;R) \longrightarrow C_n(X;R), \qquad g_\#(\eta) = g \circ \eta,
$$

and the assignment $g \mapsto g_\#$ is a group homomorphism into the automorphisms of the graded module, because $(gh) \circ \eta = g \circ (h \circ \eta)$ and the identity acts as the identity. The action commutes with the boundary, $g_\# \partial = \partial g_\#$, because the homeomorphism $g$ carries the faces of a simplex to the faces of its image; so $C_*(X;R)$ is a complex of left $R[G]$-modules with $R[G]$-linear boundary.

**Definition.** An **equivariant operator** on the chain complex is an $R[G]$-linear endomorphism of the graded module commuting with $\partial$, that is an endomorphism of the complex of $R[G]$-modules. A **chain map of degree $0$** between two such complexes is a degree-preserving $R[G]$-linear map commuting with $\partial$.

An equivariant operator is thus a chain map $C_*(X;R) \to C_*(X;R)$, and the equivariant operators form a graded unital $R$-algebra under composition, the **operator algebra of the action**, written

$$
\mathcal{E}(X;R) = \operatorname{End}_{R[G]}\bigl(C_*(X;R)\bigr).
$$

## Equivariant Maps as Operators

### The Induced Chain Map

**Theorem.** A $G$-map $f : X \to Y$ induces a chain map of complexes of $R[G]$-modules

$$
f_\# : C_*(X;R) \longrightarrow C_*(Y;R), \qquad f_\#(\eta) = f \circ \eta,
$$

and $f_\#$ is an element of $\operatorname{Hom}_{R[G]}(C_*(X;R), C_*(Y;R))$: it is $R$-linear, it commutes with $\partial$, and it commutes with the action, $f_\# \, g_\# = g_\# \, f_\#$ for every $g \in G$.

*Proof.* The map on simplices is additive, so $f_\#$ is $R$-linear; the boundary commutes with composition of maps, so $f_\#\partial = \partial f_\#$; and the action commutes because $f(g \cdot x) = g \cdot f(x)$, that is $f \circ g = g \circ f$ on the underlying points, whence $f_\#(g \circ \eta) = g \circ (f_\# \eta)$. $\square$

**Corollary.** An equivariant homeomorphism induces an isomorphism of the operator complexes, and the assignment $X \mapsto C_*(X;R)$, $f \mapsto f_\#$ is a functor from $G\text{-}\mathbf{Top}$ to the category of complexes of $R[G]$-modules: $(g \circ f)_\# = g_\# \circ f_\#$ and $(\mathrm{id}_X)_\# = \mathrm{id}$.

*Proof.* Both identities are the associativity of composition. $\square$

So a $G$-map is exactly an operator between the equivariant complexes that intertwines the two actions, and the functor sends the equivariant category to the category of differential graded modules over the group ring.

### Functoriality and the Operator Algebra

The functor is additive and preserves composition, so on a fixed space it produces a map of monoids

$$
\operatorname{Homeo}_G(X) \longrightarrow \mathcal{E}(X;R), \qquad f \mapsto f_\#,
$$

from the $G$-equivariant self-homeomorphisms to the equivariant operators. This map is not injective in general — a self-homotopy equivalence that is not a homeomorphism may induce the identity on chains — and it is not surjective: a general equivariant operator need not come from a map of spaces. The gap is the same as the gap between maps and chain maps in the ordinary theory, and it is what the homotopy invariance below measures.

**Proposition.** The assignment is compatible with the operator algebra: for $G$-maps $f : X \to Y$ and $h : Y \to Z$ the composites satisfy $(h \circ f)_\# = h_\# \circ f_\#$, and for an equivariant operator $T \in \mathcal{E}(Y;R)$ the composite $T \circ f_\#$ is again an intertwining operator. Consequently the operators of $\mathcal{E}(X;R)$ act on the homology of any $G$-space mapping equivariantly to $X$, by postcomposition.

*Proof.* The first two statements are associativity of composition; the third is the definition of the action. $\square$

### Equivariant Homotopy and Chain Homotopy

**Theorem.** Let $H : X \times I \to Y$ be an equivariant homotopy from $f$ to $g$, the interval carrying the trivial action. Then there is a degree-one $R[G]$-linear map (a **homotopy operator**)

$$
P : C_n(X;R) \longrightarrow C_{n+1}(Y;R), \qquad \partial P + P\partial = g_\# - f_\#,
$$

which intertwines the actions. Consequently $f_\#$ and $g_\#$ induce the same map on every invariant built from the complex, and in particular the same map on the coinvariants and on the Borel complex.

*Proof.* The standard prism operator of *Simplicial and Singular Homology* for the homotopy $H$ is $P(\eta)(x,t) = H(\eta(x), t)$; it is $R$-linear and satisfies the displayed identity. It intertwines the actions because $H$ does: for $g \in G$,

$$
P(g_\#\eta)(x,t) = H(g \cdot \eta(x), t) = g \cdot H(\eta(x), t) = g_\# (P\eta)(x,t),
$$

using that $g$ acts trivially on the interval. $\square$

**Corollary (homotopy invariance).** The functor on chain complexes sends equivariantly homotopic $G$-maps to $R[G]$-chain-homotopic maps; it therefore descends to the equivariant homotopy category as a functor to the homotopy category of complexes of $R[G]$-modules.

*Proof.* The prism operator is the chain homotopy, and a chain homotopy induces the zero map on homology. $\square$

## The Two Derived Complexes

### Coinvariants and the Orbit Complex

The **coinvariant complex** is $C_*(X;R)_G = C_*(X;R) \otimes_{R[G]} R$, the quotient by the submodule generated by $gm - m$; it is the complex of *Group Cohomology* with the action forgotten. A $G$-map $f$ induces a map of coinvariant complexes, $\bar f_\# : C_*(X;R)_G \to C_*(Y;R)_G$, because an intertwining operator descends to the tensor product over the group ring; this is the chain-level form of the induced map $\bar f$ on the orbit spaces.

**Theorem.** If $G$ is finite and acts freely on $X$, then the orbit map $\pi : X \to X/G$ induces an isomorphism of complexes $C_*(X;R)_G \cong C_*(X/G;R)$ up to the transfer of *The Transfer Map*, and hence an isomorphism in homology $H_n(C_*(X;R)_G) \cong H_n(X/G;R)$. The induced maps agree, so that on free actions the coinvariant functor computes the homology of the orbit space and is natural in the $G$-maps.

*Proof.* The transfer $\tau : C_*(X/G;R) \to C_*(X;R)$ of the covering $X \to X/G$ is $G$-equivariant and satisfies $p_\# \tau = |G|$, from which $\tau$ followed by the quotient $C_*(X;R) \to C_*(X;R)_G$ is an isomorphism when $|G|$ is inverted; integrally it is a chain homotopy equivalence, and the naturality is that of the transfer. The details are those of *The Transfer Map*. $\square$

For a non-free action the coinvariant complex computes the derived functor $H_*(X;R)_G$ of the coinvariants, which is not the homology of the orbit space; the Borel complex is the invariant that keeps the correct information.

### The Borel Complex

**Definition.** The **Borel complex** of the action is

$$
C_*^G(X;R) = C_*(EG \times_G X; R),
$$

the singular complex of the homotopy quotient of *Two-Fold Coverings and the Borel Construction* generalised to $G$, and the **equivariant homology** is

$$
H_n^G(X;R) = H_n\bigl(C_*^G(X;R)\bigr) = H_n(EG \times_G X; R).
$$

**Theorem.** The Borel complex computes the homology of $G$ with coefficients in the complex of the space,

$$
H_n^G(X;R) \cong H_n\bigl(G; C_*(X;R)\bigr) = \operatorname{Tor}^{R[G]}_n\bigl(R, C_*(X;R)\bigr),
$$

in the sense of *Group Cohomology*, and for a free action it reduces to the homology of the orbit space, $H_n^G(X;R) \cong H_n(X/G;R)$.

*Proof.* The homotopy quotient $EG \times_G X$ is the geometric realisation of the two-sided bar construction $R \otimes_{R[G]} C_*(X;R)$, whose homology is the derived functor $\operatorname{Tor}$; the free case is the homotopy equivalence $EG \times_G X \simeq X/G$ of *Two-Fold Coverings and the Borel Construction*. $\square$

A $G$-map $f : X \to Y$ induces $\mathrm{id} \times_G f : EG \times_G X \to EG \times_G Y$, hence a map of Borel complexes and a map

$$
H_n^G(f) : H_n^G(X;R) \longrightarrow H_n^G(Y;R).
$$

## Induced Maps on Equivariant Homology

### Functoriality and Homotopy Invariance

**Theorem.** The assignments $X \mapsto H_n^G(X;R)$ and $f \mapsto H_n^G(f)$ are functorial on $G\text{-}\mathbf{Top}$, and $H_n^G(f) = H_n^G(g)$ whenever $f$ and $g$ are equivariantly homotopic. Hence the equivariant homology is a functor on the equivariant homotopy category.

*Proof.* Functoriality is that of the Borel construction; homotopy invariance follows from the chain homotopy of the previous section, which passes to the quotient $EG \times_G (-)$ because the homotopy operator is $R[G]$-linear. $\square$

**Corollary.** An equivariant homotopy equivalence induces an isomorphism in equivariant homology, and the same statements hold for the coinvariant complex in the free case. The maps induced by two $G$-maps that are equivariantly homotopic agree on every invariant constructed functorially from the complex.

*Proof.* An equivariant homotopy equivalence has an equivariant homotopy inverse, and a functor on the equivariant homotopy category sends invertible morphisms to isomorphisms. $\square$

### Naturality and the Comparison

The orbit space and the homotopy quotient are related by the **comparison map**

$$
c : X_G = EG \times_G X \longrightarrow X/G,
$$

induced by the equivariant projection $X \times EG \to X$ when the action is free (and by the quotient map in general, when the latter is defined). It is natural for $G$-maps, so it intertwines the operators: $c \circ (\mathrm{id} \times_G f) = \bar f \circ c$. For a free action it is a homotopy equivalence, and then the two invariants coincide and the two induced maps agree.

**Remark.** The passage from the Borel complex to the cohomology of the base is the Borel fibration $X_G \to BG$, and a $G$-map induces a map of the fibrations, hence a map of the Leray–Serre spectral sequences of *The Leray–Serre Spectral Sequence*; the induced maps on the equivariant homology are the edge maps of the resulting comparison, and the higher pages carry the operators just as the complexes do. This is the chain-level content of the statement of *Two-Fold Coverings and the Borel Construction* that the Borel fibration computes the equivariant cohomology, and the spectral sequence is not reproduced here.

## The Fixed Part

### Invariants and the Norm Operator

The group ring acts on the complex, and the **norm operator** is the endomorphism

$$
N = \sum_{g \in G} g_\# \in \mathcal{E}(X;R),
$$

which is $R[G]$-linear because it is a central element of $R[G]$, and which satisfies $N^2 = |G|\, N$ when $G$ is finite. Its image lies in the fixed subcomplex $C_*(X;R)^G = \{c : g_\# c = c \ \forall g\}$, and when $|G|$ is invertible in $R$ the operator $|G|^{-1}N$ is an idempotent projecting onto the fixed part. The operators that the article has studied are all intertwiners for the action, so they preserve the fixed subcomplex and the norm operator commutes with them; the homology of the fixed part is the invariant part $H_n(X;R)^G$ of the homology, and it is the target of the transfer of the following articles of this Part.

**Proposition.** A $G$-map $f$ satisfies $f_\# N_X = N_Y f_\#$, so it carries the fixed subcomplex to the fixed subcomplex and induces a map on the invariant homology. When $|G|$ is invertible in $R$, $H_n(X;R)^G$ is a direct summand of $H_n(X;R)$ and the induced map restricts to it.

*Proof.* The identity is $f_\# g_\# = g_\# f_\#$ summed over $g$; the summand statement is the idempotent $|G|^{-1}N$ of the previous paragraph. $\square$

## Examples

**Example (the involution and the projective space).** For $G = \mathbb{Z}/2$ acting antipodally on $S^n$, the action is free, the coinvariant complex is the complex of $\mathbb{RP}^n$, and the equivariant homology is $H_n^{\mathbb{Z}/2}(S^n;R) \cong H_n(\mathbb{RP}^n;R)$. The antipodal map is the operator generating the action, and the norm $N = 1 + \sigma_\#$ acts as $2$ on the invariant chains; over $\mathbb{F}_2$ it acts as zero, which is the vanishing that the mod-2 theory of this category exploits.

**Example (the trivial action).** If $G$ acts trivially on $X$, then $EG \times_G X \simeq X \times BG$, and the equivariant homology is $H_n^G(X;R) \cong \bigoplus_{p+q=n} H_p(X;R) \otimes H_q(BG;R)$ when the Künneth sequence of *Simplicial and Singular Homology* splits, with the operators acting on the two factors separately. The coinvariant complex has homology $H_*(X;R) \otimes_R R[G]$-coinvariants, and for a finite $G$ the two invariants differ by the group homology of $G$.

**Example (a $G$-map of free actions).** Let $X \to Y$ be a $G$-map of free $G$-spaces, so it descends to $\bar f : X/G \to Y/G$. The operators on the two sides are the same chain map, read on the coinvariant complexes; the induced map $H_*(X/G) \to H_*(Y/G)$ is the one obtained from $f_\#$ by the isomorphism of the free case, and the transfer of *The Transfer Map* intertwines the two. This is the sense in which the induced map on the orbit space is an operator on the equivariant complex and not a new construction.

## Summary

A space with an action of a group $G$ has its singular complex promoted to a complex of modules over the group ring $R[G]$, with the group acting by homeomorphisms and the boundary acting $R[G]$-linearly; a $G$-map is exactly a chain map intertwining the two actions, so the $G$-maps appear as operators, the equivariant operators form the graded algebra $\mathcal{E}(X;R) = \operatorname{End}_{R[G]}(C_*(X;R))$, and the assignment is functorial from $G\text{-}\mathbf{Top}$ to complexes of $R[G]$-modules. An equivariant homotopy supplies a degree-one intertwining homotopy operator $\partial P + P\partial = g_\# - f_\#$, so equivariantly homotopic maps induce the same maps on every invariant, and the construction descends to the equivariant homotopy category. Two functors on complexes of $R[G]$-modules carry the operator to the two invariants: the coinvariants, which give the homology of the orbit space in the free case, and the bar construction $C_*(EG \times_G X;R)$, which gives the equivariant homology $H_n^G(X;R) \cong \operatorname{Tor}^{R[G]}_n(R, C_*(X;R))$ and reduces to the orbit space for a free action. The norm operator $N = \sum_g g_\#$ is central in the equivariant operator algebra, descends to an idempotent projecting onto the fixed part when $|G|$ is invertible, and commutes with every induced operator; the passage between the two invariants is the natural comparison $X_G \to X/G$, whose fibrational form is the Borel fibration and whose higher pages are the Leray–Serre spectral sequence. Nothing analytic and nothing geometric was used: the article is the group ring acting on the singular complex and two of its derived functors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$ | Group acting on the spaces; $\mathbb{Z}/2$ in the involution case |
| $G\text{-}\mathbf{Top}$ | Category of $G$-spaces and $G$-maps; $\mathbf{Top}^{\mathbb{Z}/2}$ for $G=\mathbb{Z}/2$ |
| $g \cdot x$, $g_\#$ | The action on points and the induced chain map |
| $C_*(X;R)$ | Singular complex as a complex of $R[G]$-modules |
| $R[G]$ | Group ring, as in *Group Cohomology* |
| $\mathcal{E}(X;R) = \operatorname{End}_{R[G]}(C_*(X;R))$ | The algebra of equivariant operators |
| $f_\#$ | Chain map induced by a $G$-map $f$; an intertwining operator |
| $P$, $\partial P + P\partial = g_\# - f_\#$ | Homotopy operator of an equivariant homotopy |
| $C_*(X;R)_G$, $M_G$ | Coinvariants; $(X/G)$-homology in the free case |
| $X_G = EG \times_G X$, $C_*^G(X;R)$ | Homotopy quotient and its singular complex, the Borel complex |
| $H_n^G(X;R)$ | Equivariant homology $\operatorname{Tor}^{R[G]}_n(R, C_*(X;R))$ |
| $c : X_G \to X/G$ | Comparison map; a homotopy equivalence for a free action |
| $N = \sum_{g \in G} g_\#$, $C_*(X;R)^G$ | Norm operator and fixed subcomplex |
| $M^G$ | Invariants; the derived functor of *Group Cohomology* |

## Further Reading

- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for equivariant maps, the equivariant chain complex and the Borel construction.
- Tammo tom Dieck, *Transformation Groups* (de Gruyter, 1987), for the equivariant homotopy category and the functoriality of equivariant homology.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the prism operator, chain homotopy and the free-action identification of orbit homology.
- Kenneth S. Brown, *Cohomology of Groups* (Springer, 1982), for the bar construction, group homology and the derived-functor description $\operatorname{Tor}^{R[G]}_n(R, C_*(X;R))$.
- Armand Borel, *Seminar on Transformation Groups* (Annals of Mathematics Studies 46, 1960), for the homotopy quotient, the Borel fibration and the comparison with the orbit space.
- Saunders Mac Lane, *Homology* (Springer, 1995), for the two-sided bar construction and the homogeneity of derived functors in two variables.
