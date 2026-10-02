# __Equivariant Cohomology__

## Introduction

A group acting on a space has invariants that no single space records: the fixed set, the orbit space and the equivariant families of cohomology classes are not functors of the underlying space alone. **Equivariant cohomology** is the cohomology theory that sees the action, and the **Borel construction** produces it from ordinary cohomology by replacing the space $X$ with the homotopy quotient $X_G = EG\times_G X$. The construction is the one introduced for the group of order two in *Two-Fold Coverings and the Borel Construction*, generalised here to an arbitrary group: the diagonal action on $X\times EG$ is free, its quotient fibres over the classifying space $BG$ with fibre $X$, and the cohomology of the total space,

$$
H_G^*(X;R) = H^*(X_G;R) = H^*(EG\times_G X;R),
$$

is the equivariant cohomology. It is a contravariant functor of the $G$-space, homotopy invariant on the equivariant homotopy category, and a module over the ring $H^*(BG;R)$ of the base of the Borel fibration; the two extreme cases are the free action, for which it is the cohomology of the orbit space, and the trivial action, for which it is the cohomology of a product.

The article develops the Borel model. It defines the construction and proves its functoriality and homotopy invariance; it computes the two extreme cases; it obtains the spectral sequence of the Borel fibration, its edge maps and the resulting module structure and transgression; it computes the rings $H_G^*(\mathrm{pt};R)$ for the classical groups; and it compares the equivariant cohomology with the cohomology of the orbit space, the comparison being the subject of the sibling article *The Cohomology of an Orbit Space*. The Borel construction for $\mathbb{Z}/2$ and the identification of its cohomology with that of the homotopy quotient are those of *Two-Fold Coverings and the Borel Construction*; the classifying space and the universal space are those of *Classifying Spaces and Cohomology Operations*; the spectral sequence of a fibration is that of *The Leray–Serre Spectral Sequence*; the cohomology ring and the universal coefficient theorem are those of *Cup and Cap Products* and *Cohomology and the Universal Coefficient Theorem*. The **Bredon** equivariant cohomology, in which the coefficients are systems of modules over the orbit category, is the other model of the theory and is used in *Equivariant Obstruction Theory*; the Borel model of this article is the one that reduces to ordinary cohomology of a single space and computes the classic rings.

Nothing analytic and nothing geometric is used. The group is a topological group, discrete or compact Lie, so that $EG$ and $BG$ of *Classifying Spaces and Cohomology Operations* may be taken, and the spaces are compactly generated when a convenient category of spaces is needed; the theory is the cohomology of the homotopy quotient, and no distance, no norm, no smooth structure and no measure is chosen. Throughout, $G$ is a topological group acting on the left on a space $X$, $EG \to BG$ is the universal principal $G$-bundle, $X_G = EG\times_G X$ is the **homotopy quotient** with the diagonal action, and the **Borel fibration** is the projection

$$
p : X_G \longrightarrow BG
$$

with fibre $X$. The coefficient ring is $R$, commutative with identity $1 \neq 0$, and is suppressed in the notation when it is clear. The equivariant cohomology is written $H_G^*(X;R)$ and the cohomology of the group is $H^*(G;R) = H^*(BG;R)$.

## The Borel Construction

### The Construction and the Fibration

**Definition.** Let $G$ act on $X$ and let $EG$ be a contractible free $G$-space. The **Borel construction** on $X$ is the quotient

$$
X_G = EG \times_G X = \frac{EG\times X}{G},
$$

with the diagonal action $g\cdot(e,x) = (ge,gx)$, and the **equivariant cohomology** is

$$
H_G^n(X;R) = H^n(X_G;R) = H^n(EG\times_G X;R).
$$

**Theorem.** The diagonal action is free, so $X_G$ is the base of a fibre bundle with fibre $X$ and the projection $p : X_G \to BG$, $[e,x]\mapsto[e]$, is a fibration with fibre $X$. The construction is natural in the group and in the space: an equivariant map $f : X \to Y$ induces $\mathrm{id}\times_G f : X_G \to Y_G$, giving $H_G^*(f) : H_G^*(Y;R)\to H_G^*(X;R)$, contravariantly and functorially; and a homomorphism $\alpha : H \to G$ induces a map $X_H \to X_G$ from the induced $H$-action.

*Proof.* The action on the product is free because it is free on the second factor: if $g(e,x)=(e,x)$ then $ge=e$, and $EG$ has trivial stabilisers, so $g=1$. Local triviality is that of the bundle $EG\times_G X\to BG$ along $EG\to BG$, with fibre $X$; the functoriality is the universal property of the quotient. $\square$

### Homotopy Invariance

**Theorem.** The construction is homotopy invariant on the equivariant homotopy category: if $f$ and $g$ are equivariantly homotopic $G$-maps then $H_G^*(f) = H_G^*(g)$, and an equivariant homotopy equivalence induces an isomorphism in equivariant cohomology.

*Proof.* An equivariant homotopy $X\times I\to Y$ with the trivial action on $I$ induces $\mathrm{id}\times_G H : X_G\times I\to Y_G$, an ordinary homotopy between the induced maps; homotopic maps induce the same map in cohomology. $\square$

So $H_G^*(X;R)$ depends only on the equivariant homotopy type of $X$ and not on the free resolution $EG$ chosen, since any two models of $EG$ are $G$-homotopy equivalent and the construction is homotopy invariant.

## The Two Extreme Cases

### The Free Action and the Orbit Space

**Theorem.** If $G$ acts freely on $X$, then the projection $EG\times X\to X$, $(e,x)\mapsto x$, is a $G$-equivariant homotopy equivalence, and it descends to a homotopy equivalence

$$
X_G = EG\times_G X \ \simeq\ X/G .
$$

Hence $H_G^*(X;R) \cong H^*(X/G;R)$ for a free action, and the Borel fibration is the composite $X/G \to BG$ classifying the principal bundle $X\to X/G$.

*Proof.* The projection $EG\times X\to X$ is a homotopy equivalence because $EG$ is contractible, it is $G$-equivariant for the diagonal action and the action on $X$, and it descends because the action is free; a descended homotopy equivalence is a homotopy equivalence of the quotients of *Equivariant Maps and Equivariant Homotopy*. $\square$

### The Trivial Action

**Theorem.** If $G$ acts trivially on $X$, then $X_G = X\times BG$ and

$$
H_G^*(X;R) \cong H^*(X;R)\otimes_R H^*(BG;R)
$$

when the Künneth sequence of *Cup and Cap Products* splits, in particular over a field; the fibration is the projection $X\times BG\to BG$ and the module structure over $H^*(BG;R)$ is the multiplication on the second factor.

*Proof.* For the trivial action the diagonal action is only on the first factor of $EG\times X$, so the quotient is $X\times BG$; the cohomology is that of a product and the Künneth theorem applies. $\square$

The two cases are the anchors of the theory: a free action has the equivariant cohomology of its orbit space, and a trivial action has the equivariant cohomology of the product with the classifying space, so the equivariant groups interpolate between the two according to how far the action is from free.

## The Spectral Sequence and the Module Structure

### The Serre Spectral Sequence of the Borel Fibration

**Theorem.** The Borel fibration $p : X_G \to BG$ has a cohomological Serre spectral sequence of *The Leray–Serre Spectral Sequence*,

$$
E_2^{p,q} = H^p\bigl(BG;\, \mathcal{H}^q(X;R)\bigr) \ \Longrightarrow \ H_G^{p+q}(X;R),
$$

where $\mathcal{H}^q(X;R)$ is the local system on $BG$ determined by the action of $\pi_1(BG)$ on the cohomology of the fibre; the system is trivial and the formula reads

$$
E_2^{p,q} = H^p(BG;R)\otimes_R H^q(X;R) \ \Longrightarrow \ H_G^{p+q}(X;R)
$$

when the action of the fundamental group is trivial, in particular for a connected group $G$ or when $X$ has trivial monodromy. The spectral sequence converges to the equivariant cohomology, is natural in equivariant maps, and its edge maps are the pullback $H^*(BG;R)\to H_G^*(X;R)$ along $X_G\to BG$ and the map $H_G^*(X;R)\to H^*(X;R)^G$ to the invariants.

*Proof.* The Serre spectral sequence of the fibration with fibre $X$ and base $BG$, with local coefficients in the cohomology of the fibre; the triviality of the monodromy in the stated cases, and the edge maps are the standard edge homomorphisms. $\square$

### The Module Structure and the Transgression

**Theorem.** The cohomology of the base acts on the equivariant cohomology: the pullback $H^*(BG;R)\to H_G^*(X;R)$ along the projection makes $H_G^*(X;R)$ a graded module over the graded ring $H^*(BG;R)$, and this module structure is natural. When the spectral sequence collapses at $E_2$, the module is free,

$$
H_G^*(X;R) \cong H^*(BG;R)\otimes_R H^*(X;R),
$$

as a module over $H^*(BG;R)$. A class of $H^*(X;R)$ that survives to the $E_\infty$ page and a class of $H^*(BG;R)$ that transgresses combine by the transgression differential, and the product structure couples the two.

*Proof.* The action is the ring structure on the cohomology of $X_G$ and the naturality of the pullback along $X_G\to BG$; the collapse at $E_2$ identifies the associated graded with $H^*(BG)\otimes H^*(X)$, and the module is free because the base is the ring and the fibre contributes central coefficients. The transgression is the standard differential of the spectral sequence. $\square$

The module structure is the precise sense in which the equivariant cohomology is not merely a group but a structure over the cohomology of the group, and it is what the computations below use: the ring $H^*(BG;R)$ is known for the classical groups, and the equivariant groups are modules over it.

## Computations

### The Group Rings

The following rings are the ones from which the equivariant cohomology of a point is read, $H_G^*(\mathrm{pt};R) = H^*(BG;R)$; they are computed in *Classifying Spaces and Cohomology Operations* and in the cohomology computations of *Cohomology and the Universal Coefficient Theorem*, and no more than their statements is used.

1. $G = \mathbb{Z}/2$: $B\mathbb{Z}/2 = \mathbb{RP}^{\infty}$ and $H^*(\mathbb{RP}^{\infty};\mathbb{F}_2) = \mathbb{F}_2[x]$ with $|x|=1$; over $\mathbb{Z}$ the ring has $2$-torsion.
2. $G = S^1$: $BS^1 = \mathbb{CP}^{\infty}$ and $H^*(BS^1;\mathbb{Z}) = \mathbb{Z}[c]$ with $|c| = 2$, a polynomial ring on one even generator.
3. $G = T^n$ a torus: $BT^n = (\mathbb{CP}^{\infty})^n$ and $H^*(BT^n;\mathbb{Z}) = \mathbb{Z}[c_1,\dots,c_n]$ with each $|c_i| = 2$.
4. $G$ a compact connected Lie group: $H^*(BG;\mathbb{Q}) = \mathbb{Q}[c_1,\dots,c_r]$ with the generators of even degree, $r$ the rank, by the theorem of Borel and Hopf.

### Homogeneous Spaces

**Theorem.** Let $H \leq G$ be a closed subgroup and let $X = G/H$ with the left action of $G$. Then the homotopy quotient is

$$
(G/H)_G = EG\times_G (G/H) \cong BH,
$$

and hence $H_G^*(G/H;R) \cong H^*(BH;R)$.

*Proof.* The action of $G$ on $G/H$ is transitive, so the map $EG\times G/H\to BH$ sending $(e,gH)$ to the class of $g$ is a homeomorphism on the quotient, since $EG\times G/H \cong EG/H$ with $H$ acting by the restriction on the right. $\square$

So the equivariant cohomology of a homogeneous space is the cohomology of the classifying space of its isotropy group, and the Borel fibration $BH\to BG$ is the map induced by the inclusion $H\to G$. For the free case $H=1$ this is $H_G^*(G;R) \cong H^*(\mathrm{pt};R)$.

### Free Circle Actions on the Odd Spheres

**Example.** Let $S^1$ act on $S^{2n+1}\subset\mathbb{C}^{n+1}$ by scalar multiplication, the standard free action with orbit space $\mathbb{CP}^n$. Then the Borel construction gives $H_{S^1}^*(S^{2n+1};\mathbb{Z}) \cong H^*(\mathbb{CP}^n;\mathbb{Z}) = \mathbb{Z}[h]/(h^{n+1})$ with $|h|=2$; as a module over $H^*(BS^1;\mathbb{Z})=\mathbb{Z}[c]$ the ring is $\mathbb{Z}[c]/(c^{n+1})$ after the identification $h=c$, and the Borel fibration is the inclusion of $\mathbb{CP}^n$ in $\mathbb{CP}^\infty$ followed by the projection to a point. The free case identifies the equivariant cohomology with the cohomology of the orbit space, and the module structure over the polynomial ring is the truncation.

**Example.** For the antipodal action of $\mathbb{Z}/2$ on $S^n$, the action is free and $S^n_{\mathbb{Z}/2} = \mathbb{RP}^n$; the equivariant cohomology is $H^*(\mathbb{RP}^n;\mathbb{F}_2) = \mathbb{F}_2[x]/(x^{n+1})$, a module over $\mathbb{F}_2[x] = H^*(B\mathbb{Z}/2;\mathbb{F}_2)$ by the truncation, the Borel fibration being $\mathbb{RP}^n\to\mathbb{RP}^\infty$. For the non-free involution with fixed set $F$, the module is no longer the truncation and the spectral sequence carries the fixed-set information, which is the subject of *The Mod 2 Cohomology of an Involution*.

## The Comparison with the Orbit Space

**Theorem.** The equivariant projection $X\times EG\to X$ induces a natural map

$$
c : X_G \longrightarrow X/G
$$

when the orbit space is formed, and a map in cohomology $H^*(X/G;R)\to H_G^*(X;R)$, the **comparison map**; for a free action $c$ is a homotopy equivalence and the comparison is an isomorphism. For a finite group $G$ acting on a nice space, the comparison is an isomorphism with rational coefficients,

$$
H^*(X/G;\mathbb{Q}) \cong H_G^*(X;\mathbb{Q}),
$$

and with field coefficients of characteristic not dividing $|G|$.

*Proof.* The map $c$ exists because the equivariant projection is constant on the orbits; the free case is the theorem above. For a finite $G$ the transfer and the averaging argument of *The Transfer Map* split the action on the rational cohomology, so the invariants and the coinvariants agree and the Leray–Serre spectral sequence of $EG\times_G X\to X/G$ degenerates; the transfer argument with the group order inverted gives the stated characteristic restriction. $\square$

The general comparison, the exact sequence that measures the failure of the isomorphism in the presence of fixed points, and the relation to the cohomology of the orbit space are the subject of *The Cohomology of an Orbit Space*. The essential point is that the Borel construction and the orbit space agree for a free action and differ in a controlled way otherwise, the difference being carried by the cohomology of the group.

## The Localization Theorem

**Theorem (localization; standard).** Let $T$ be a torus acting on a finite-dimensional $T$-CW complex $X$ and let $F = X^T$ be the fixed set. Then the inclusion $F\hookrightarrow X$ induces an isomorphism after localizing at the multiplicative set of nonzero elements of $H^*(BT;\mathbb{Q})$ that restrict nontrivially to $H^*(BT)$ through every subtorus:

$$
H_T^*(X;\mathbb{Q})[\mathcal{S}^{-1}] \;\cong\; H_T^*(F;\mathbb{Q})[\mathcal{S}^{-1}] ,
$$

and since the action on $F$ is trivial there, the right side is $H^*(F;\mathbb{Q})\otimes H^*(BT;\mathbb{Q})$ localized. In particular, for a torus action the rational equivariant cohomology is determined by the fixed set.

*Proof.* The theorem of Atiyah–Bott and Borel; the localization uses the Euler classes of the normal directions to the fixed set and the fact that on the complement of the fixed set the equivariant Euler class is invertible in the localized ring. The statement is quoted, and the equivariant $K$-theory version is used in *Equivariant K-Theory*. $\square$

## Summary

Equivariant cohomology in the Borel model is the ordinary cohomology of the homotopy quotient $X_G = EG\times_G X$; the diagonal action is free, the projection $X_G\to BG$ is a fibration with fibre $X$, and the construction is natural in the equivariant map and homotopy invariant on the equivariant homotopy category. For a free action the homotopy quotient is the orbit space and $H_G^*(X;R)\cong H^*(X/G;R)$; for a trivial action it is $X\times BG$ and the equivariant cohomology is the product with $H^*(BG;R)$; for a homogeneous space $G/H$ it is $H^*(BH;R)$. The Serre spectral sequence of the Borel fibration has $E_2^{p,q}=H^p(BG;\mathcal{H}^q(X;R))$ and converges to $H_G^{p+q}(X;R)$, with the trivial monodromy giving $H^*(BG;R)\otimes H^*(X;R)$; the cohomology of the base makes the equivariant cohomology a module over $H^*(BG;R)$, and the module is free when the sequence collapses. The rings $H^*(BG;R)$ are polynomial for the classical groups, and the localization theorem computes the rational equivariant cohomology of a torus action from the fixed set. The comparison with the cohomology of the orbit space is the isomorphism for free actions and the transfer isomorphism for finite groups with the group order inverted; the general comparison is the subject of *The Cohomology of an Orbit Space*. Nothing analytic and nothing geometric was used beyond the classifying spaces and the fibration.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $X$ | Topological group and a left $G$-space |
| $EG$, $BG$ | Universal $G$-bundle; classifying space, from *Classifying Spaces and Cohomology Operations* |
| $X_G = EG\times_G X$ | Homotopy quotient, or Borel construction |
| $p : X_G \to BG$ | Borel fibration, with fibre $X$ |
| $H_G^*(X;R)$ | Equivariant cohomology $H^*(X_G;R)$ |
| $H^*(G;R) = H^*(BG;R)$ | Cohomology of the group; the base ring |
| $H_G^*(f)$, $\mathrm{id}\times_G f$ | Contravariant functoriality in equivariant maps |
| $E_2^{p,q} = H^p(BG;\mathcal{H}^q(X))$ | Serre spectral sequence of the Borel fibration |
| $\mathcal{H}^q(X;R)$ | Local system of the fibre cohomology over $BG$ |
| $H^*(BG;R)\otimes H^*(X;R)$ | $E_2$ page and $H_G^*$ when the monodromy is trivial |
| $c : X_G \to X/G$ | Comparison map with the orbit space |
| $H^*(X/G;\mathbb{Q})\cong H_G^*(X;\mathbb{Q})$ | Comparison isomorphism for a finite group |
| $F = X^T$, localization | Fixed set of a torus; localization theorem |

## Further Reading

- Armand Borel, *Seminar on Transformation Groups* (Annals of Mathematics Studies 46, 1960), for the homotopy quotient, the Borel fibration and the equivariant cohomology.
- Wu-yi Hsiang, *Cohomology Theory of Topological Transformation Groups* (Springer, 1975), for the computations of the equivariant cohomology rings of the classical transformation groups.
- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for the Borel construction, the spectral sequence and the comparison with the orbit space.
- Michael F. Atiyah and Raoul Bott, "The moment map and equivariant cohomology", *Topology* 23 (1984), 1–28, for the localization theorem and its applications.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the Serre spectral sequence, the classifying spaces and the cohomology of the classical groups.
- Tammo tom Dieck, *Transformation Groups* (de Gruyter, 1987), for equivariant cohomology, the orbit category and the relation between the Borel and Bredon models.
