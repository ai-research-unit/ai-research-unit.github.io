# __Two-Fold Coverings and the Borel Construction__

## Introduction

The Borel construction replaces a group action by a fibration: from a space $X$ with an action of a group $G$ it forms the **homotopy quotient** $X \times_{G} EG = (X \times EG)/G$, and it maps to the **classifying space** $BG = EG/G$. For the group of order two the space $E\mathbb{Z}/2$ is the infinite sphere $S^{\infty}$ with the antipodal involution, contractible and free, and $B\mathbb{Z}/2$ is real projective space $\mathbb{RP}^{\infty}$. The Borel construction is the tool that turns the equivariant data of the previous articles into ordinary topological data on the quotient, and for a free involution it recovers the orbit map that *The Orbit Space of a Free Involution* studied: a free involution on $X$ has its orbit map a two-fold covering, and the classifying map of that covering into $\mathbb{RP}^{\infty}$ is the homotopy quotient map $X \times_{\mathbb{Z}/2} E\mathbb{Z}/2 \to B\mathbb{Z}/2$. The universal two-fold covering $S^{\infty} \to \mathbb{RP}^{\infty}$ is then the source of all two-fold coverings, and the classification of the two-fold coverings of a space $B$ by the cohomology group $H^{1}(B;\mathbb{Z}/2)$ is the precise form of that statement.

The article begins with the Borel construction and its fibration property, computes the construction for the group of order two, states the classification of two-fold coverings by homotopy classes into $\mathbb{RP}^{\infty}$ and by $H^{1}$, and describes the nonfree case, where the homotopy quotient is still defined but is no longer the orbit space. It continues *The Orbit Space of a Free Involution*, whose covering theory it extends, and it uses the cohomology of the later articles, which supply the identification of the homotopy classes with $H^{1}(B;\mathbb{Z}/2)$; the classification theorem is stated and its proof is deferred to *Cohomology and the Universal Coefficient Theorem*.

Nothing analytic and nothing geometric is used. The infinite sphere is the union of the finite spheres with the antipodal involution, and the map $S^{\infty} \to \mathbb{RP}^{\infty}$ is the orbit map; no distance and no measure is chosen, and the only homotopy theory used is that of the preceding articles.

## The Homotopy Quotient

### The Borel Construction

**Definition.** Let $G$ act on a space $X$, and let $EG$ be a contractible space on which $G$ acts freely and properly. The **Borel construction**, or **homotopy quotient**, of $X$ by $G$ is

$$
X \times_{G} EG = \frac{X \times EG}{G},
$$

the quotient of the product by the diagonal action $g \cdot (x,e) = (gx, ge)$. The projection to the second factor descends to a map

$$
p : X \times_{G} EG \longrightarrow BG = EG/G ,
$$

the **Borel fibration** of the action.

**Theorem.** The map $p : X \times_{G} EG \to BG$ is a fibration with fibre $X$, well defined up to homotopy; the construction is functorial in the equivariant map $X \to Y$ and natural in the group; and for the trivial action it reduces to $BG$ with fibre $X$: $X \times_{G} EG \simeq X \times BG$ when $G$ acts trivially on $X$.

**Proof.** The diagonal action is free, since the action on the first factor is not needed for freeness: if $g(x,e) = (x,e)$ then $ge = e$ and $e \in EG$ has trivial stabiliser, so $g = e$. Hence the quotient is a fibre bundle with fibre $X$ over $BG$ in the sense of the covering and fibre-bundle theory of this Part, and the projection is a fibration with the homotopy lifting property. Functoriality and naturality are the universal property of the quotient; for the trivial action the product $X \times EG$ has the action only on the second factor, so the quotient is $X \times BG$.

**Remark.** The Borel construction is the replacement of the orbit space $X/G$, which for a nonfree action is not a nice object, by the homotopy quotient, which is; for a free action the two agree up to homotopy, $X \times_{G} EG \simeq X/G$, since the projection $X \times EG \to X$ is $G$-equivariant and a homotopy equivalence (as $EG$ is contractible), and it descends.

### The Borel Construction of a Free Involution

**Theorem.** Let $\sigma$ be a free continuous involution of a space $X$ with orbit map $\pi : X \to X/\sigma$. Then there is a homotopy equivalence

$$
X \times_{\mathbb{Z}/2} S^{\infty} \ \simeq \ X/\sigma ,
$$

and under it the Borel fibration $X \times_{\mathbb{Z}/2} S^{\infty} \to \mathbb{RP}^{\infty}$ corresponds to a map $X/\sigma \to \mathbb{RP}^{\infty}$.

**Proof.** The projection $X \times S^{\infty} \to X$ is equivariant for $\sigma \times$ (antipodal) and $\sigma$, and it is a homotopy equivalence because $S^{\infty}$ is contractible; a homotopy equivalence that is equivariant for a free action descends, by *Equivariant Maps and Equivariant Homotopy*, to a homotopy equivalence of the quotients, which are $X \times_{\mathbb{Z}/2} S^{\infty}$ and $X/\sigma$.

The statement says that the orbit map of a free involution is the Borel construction: the equivariant homotopy type of the free action is the homotopy type of the orbit space together with the map to $\mathbb{RP}^{\infty}$ that classifies the covering.

## The Classifying Space of the Group of Order Two

### The Infinite Sphere and Real Projective Space

**Definition.** The **infinite sphere** $S^{\infty}$ is the union of the finite spheres $S^{n}$ under the inclusions $S^{n} \subset S^{n+1}$, with the weak (colimit) topology, and the antipodal involution acts on it freely. The orbit space is **real projective space** $\mathbb{RP}^{\infty} = S^{\infty}/\mathbb{Z}/2$, the union of the finite projective spaces $\mathbb{RP}^{n}$.

**Theorem.** The infinite sphere is contractible, the antipodal involution on it is free, and the orbit map

$$
S^{\infty} \longrightarrow \mathbb{RP}^{\infty}
$$

is a two-fold covering. Consequently $E\mathbb{Z}/2 = S^{\infty}$ and $B\mathbb{Z}/2 = \mathbb{RP}^{\infty}$, and the orbit map is the **universal two-fold covering**.

**Proof.** The sphere $S^{\infty}$ is the union of the spheres $S^{n}$, and a map $S^{k} \to S^{\infty}$ has image in a finite sphere $S^{n}$ by compactness; an iteration of the standard contraction of the upper hemisphere onto the lower one extends a null-homotopy from $S^{n}$ to $S^{n+1}$ and hence to the colimit, giving the contractibility of $S^{\infty}$. Freeness is that $x \neq -x$ on every sphere, and the covering statement is the theorem of *The Orbit Space of a Free Involution* for the antipodal involution of a Hausdorff space.

**Remark.** The finite sphere $S^{n}$ is not contractible, and the passage to the infinite union is what makes $E\mathbb{Z}/2$ contractible; the construction $EG$ is the standard one of taking the colimit of a free action on the spheres or the simplices. The space $\mathbb{RP}^{\infty}$ is the classifying space of the group of order two, and it is the base of the universal two-fold covering.

### The Universal Property

**Theorem.** Let $B$ be a space and let $f : B \to \mathbb{RP}^{\infty}$ be continuous. Then the pullback

$$
f^{*}\bigl(S^{\infty} \to \mathbb{RP}^{\infty}\bigr) = \{(b, e) \in B \times S^{\infty} : f(b) = [e]\}
$$

is a two-fold covering of $B$, and it is the total space of the covering classified by $f$.

**Proof.** The pullback of a covering along a continuous map is a covering of the same degree, since the evenly covered neighbourhoods pull back; the degree is two because the fibre of $S^{\infty} \to \mathbb{RP}^{\infty}$ has two points.

## The Classification of Two-Fold Coverings

### The Classification Theorem

**Theorem (classification; proof deferred).** Let $B$ be connected and paracompact, and let $B$ have the homotopy type of a cell complex. Then the two-fold coverings of $B$ are classified up to equivalence over $B$ by the homotopy classes of maps $B \to \mathbb{RP}^{\infty}$:

$$
\{\text{two-fold coverings of } B\} \big/{\cong} \ \longleftrightarrow \ [B, \mathbb{RP}^{\infty}] \ \cong \ H^{1}(B;\mathbb{Z}/2) .
$$

The class of a covering is its **classifying map**, and the trivial covering corresponds to the null-homotopic maps and to the zero class in $H^{1}$.

**Proof sketch.** The forward map sends a covering to its classifying map, which is constructed by gluing the local trivialisations of the covering over the cells of $B$; the map is well defined on equivalence classes and homotopy classes, and the pullback construction shows that the assignment has the stated image. The identification $[B,\mathbb{RP}^{\infty}] \cong H^{1}(B;\mathbb{Z}/2)$ is the universal coefficient theorem and the representability of $H^{1}$ by $\mathbb{RP}^{\infty}$, proved in *Cohomology and the Universal Coefficient Theorem*. The proof of the classification itself is the standard obstruction theory of covering spaces, given in the references.

**Remark.** The theorem refines the classification of *The Orbit Space of a Free Involution*, where the two-fold coverings of a connected base were identified with free involutions on the total space; the cohomological classification records in addition the class of the covering in the cohomology of the base.

### The Classifying Map of an Involution

**Theorem.** Let $\sigma$ be a free continuous involution of a Hausdorff space $X$, and let $\pi : X \to X/\sigma$ be the two-fold covering. Then the classifying map of this covering is the composite

$$
X/\sigma \ \longrightarrow \ \mathbb{RP}^{\infty}
$$

obtained from the Borel construction of the previous section, and two free involutions on $X$ with homeomorphic orbit spaces give equivalent coverings exactly when their classifying maps are homotopic.

**Proof.** The classifying map of the covering is by definition the map whose pullback gives it; the Borel construction identifies the total space with $X/\sigma$ up to homotopy, and the pullback along the classifying map is the universal covering restricted; the uniqueness is the classification theorem.

## The Nonfree Case

### The Homotopy Quotient of a Nonfree Action

**Definition.** For a space $X$ with an involution, free or not, the **homotopy quotient** is $X \times_{\mathbb{Z}/2} S^{\infty}$ and the **Borel fibration** is the map to $\mathbb{RP}^{\infty}$; the **equivariant cohomology** is

$$
H^{*}_{\mathbb{Z}/2}(X) = H^{*}(X \times_{\mathbb{Z}/2} S^{\infty}) ,
$$

with coefficients in a ring, the cohomology of the homotopy quotient.

**Theorem.** For a free involution the group $H^{*}_{\mathbb{Z}/2}(X)$ is the cohomology of the orbit space $H^{*}(X/\sigma)$; for the trivial involution it is the cohomology of $X \times \mathbb{RP}^{\infty}$; and in general the Borel fibration gives a spectral sequence, the **Serre spectral sequence**, from the cohomology of the base $\mathbb{RP}^{\infty}$ with local coefficients in the cohomology of the fibre $X$ to the equivariant cohomology of $X$.

**Proof.** The free case is the homotopy equivalence $X \times_{\mathbb{Z}/2} S^{\infty} \simeq X/\sigma$; the trivial case is the trivial-action formula of the construction; the spectral sequence is the Serre spectral sequence of the Borel fibration, whose proof belongs to *Spectral Sequences* later in this Part.

### Homotopy Fixed Points

**Definition.** The **homotopy fixed points** of the involution on $X$ are the space of equivariant maps

$$
X^{h\mathbb{Z}/2} = \mathrm{Map}_{\mathbb{Z}/2}(S^{\infty}, X) ,
$$

with the compact-open topology, where $S^{\infty}$ carries the antipodal involution and the action on the mapping space is by precomposition.

**Proposition.** The homotopy fixed points contain the fixed points, $X^{\mathbb{Z}/2} \subseteq X^{h\mathbb{Z}/2}$, the inclusion being by the constant maps, and it is a homotopy invariant of the equivariant homotopy type, whereas the fixed set need not be.

**Proof.** A fixed point $x$ defines the constant equivariant map $e \mapsto x$; conversely an equivariant map need not be constant, so the inclusion is not an equality in general. Functoriality gives the homotopy invariance from *Equivariant Maps and Equivariant Homotopy*.

**Remark.** The pair of constructions, the homotopy fixed points on one side and the homotopy quotient on the other, are the two homotopy-invariant replacements of the fixed set and the orbit space; the exact relation between them, and the comparison with the honest fixed set and orbit space, is the content of the equivariant homotopy theory and of the Borel and the cohomological constructions that the later articles use.

## Summary

The Borel construction of a space $X$ with an action of the group of order two is the homotopy quotient $X \times_{\mathbb{Z}/2} S^{\infty}$, the quotient of the product by the diagonal action; it fibres over $\mathbb{RP}^{\infty}$, and for a free action it is homotopy equivalent to the orbit space, so that the orbit map of a free involution is the Borel construction. The infinite sphere is contractible and its antipodal involution is free, so $E\mathbb{Z}/2 = S^{\infty}$ and $B\mathbb{Z}/2 = \mathbb{RP}^{\infty}$; the antipodal orbit map is the universal two-fold covering, and the pullback of the universal covering along a map $B \to \mathbb{RP}^{\infty}$ is a two-fold covering of $B$. The two-fold coverings of a connected paracompact base are classified by the homotopy classes of such maps and hence by $H^{1}(B;\mathbb{Z}/2)$, with the trivial covering corresponding to the zero class; the proof of the classification uses the covering theory and the universal coefficient theorem and is deferred. For a nonfree action the homotopy quotient is still defined, the equivariant cohomology is its cohomology, and the Borel fibration gives a spectral sequence relating it to the cohomology of the fibre and the base; the homotopy fixed points are the dual invariant that replaces the fixed set.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $EG$ | A contractible space on which $G$ acts freely and properly |
| $BG = EG/G$ | The classifying space of $G$ |
| $X \times_{G} EG$ | The Borel construction, or homotopy quotient |
| $p : X\times_{G} EG \to BG$ | The Borel fibration, with fibre $X$ |
| $S^{\infty}$ | The infinite sphere, $E\mathbb{Z}/2$, with the antipodal involution |
| $\mathbb{RP}^{\infty}$ | Real projective space, $B\mathbb{Z}/2$ |
| $S^{\infty} \to \mathbb{RP}^{\infty}$ | The universal two-fold covering |
| classifying map | The map $B \to \mathbb{RP}^{\infty}$ whose pullback is a given covering |
| $H^{1}(B;\mathbb{Z}/2)$ | The classification set of two-fold coverings of a connected paracompact $B$ |
| $H^{*}_{\mathbb{Z}/2}(X)$ | Equivariant cohomology $H^{*}(X \times_{\mathbb{Z}/2} S^{\infty})$ |
| $X^{h\mathbb{Z}/2}$ | Homotopy fixed points $\mathrm{Map}_{\mathbb{Z}/2}(S^{\infty}, X)$ |
| Borel fibration | $X \times_{\mathbb{Z}/2} S^{\infty} \to \mathbb{RP}^{\infty}$; Serre spectral sequence |

## Further Reading

- Armand Borel, *Seminar on Transformation Groups* (Annals of Mathematics Studies 46, Princeton, 1960), for the Borel construction and equivariant cohomology.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the classification of coverings, $EG$ and $BG$, and the universal two-fold covering.
- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for the Borel construction, the classification of $G$-bundles and equivariant cohomology.
- Tammo tom Dieck, *Transformation Groups* (de Gruyter, 1987), for the homotopy quotient, the classifying space of a finite group and the equivariant homology theories.
- Dale Husemoller, *Fibre Bundles* (Springer, 3rd ed. 1994), for principal bundles, classifying spaces and the classification of two-fold coverings.
- Jean-Pierre Serre, "Homologie singulière des espaces fibrés", *Annals of Mathematics* 54 (1951), 425–505, for the spectral sequence of a fibration used in the nonfree case.
