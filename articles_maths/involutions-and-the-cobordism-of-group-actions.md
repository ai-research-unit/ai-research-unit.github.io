
# __Involutions and the Cobordism of Group Actions__

## Introduction

An involution of a manifold has a **cobordism theory**: two involutions of closed manifolds are equivariantly cobordant when they bound an involution of a manifold with boundary, and the cobordism classes form a graded ring — the **equivariant bordism ring** — in which the fixed set, the quotient and the equivariant characteristic numbers are the invariants. This article is the cobordism theory of the group actions, in the case of the group $\mathbb{Z}/2$ and its generalisations: the equivariant bordism rings, the Conner–Floyd theorem that the unoriented ring is a polynomial algebra detected by the equivariant Stiefel–Whitney numbers, the oriented theory with its equivariant Pontryagin and signature invariants, and the relation to the equivariant surgery of the earlier articles.

The cobordism of involutions sits between the classification and the invariants: it is coarser than the classification of *Involutions on Manifolds and Equivariant Surgery* (cobordism forgets the homotopy type and keeps the characteristic numbers) and finer than the homological invariants of the group (it keeps the equivariant characteristic numbers). The two extremes of the theory are the **free** involutions, whose cobordism reduces to the ordinary cobordism of the quotient, and the **fixed** involutions of a reflection, whose cobordism is the cobordism of the fixed set with its normal data.

**The article assumes** the differential topology of the bordism theory, the Stiefel–Whitney and Pontryagin classes, the equivariant surgery of *Involutions on Manifolds and Equivariant Surgery*, the Smith theory of *Periodic Maps and the Smith Theory*, and the ordinary cobordism rings of *Cobordism and Surgery Theory*.

**The boundaries of the article.** The ordinary cobordism rings and the Thom spectra are *Cobordism and Surgery Theory*; the equivariant surgery obstruction is *Involutions on Manifolds and Equivariant Surgery*; the equivariant signature and the $G$-signature theorem are *Hermitian Pairings and the Equivariant Signature*; the equivariant stable homotopy, the equivariant Thom spectra and the completions are *Stable Homotopy Theory*. The differentiable structures and the transversality are Part III. No analysis is used, and the smooth constructions are treated through their bordism-theoretic consequences.

## Equivariant Bordism

**Definition.** Let $G$ be a finite group. A **$G$-manifold** is a closed manifold with a smooth action of $G$, and two $G$-manifolds $M_0,M_1$ are **$G$-cobordant** if there is a compact $G$-manifold $W$ with $\partial W = M_0\sqcup M_1$ and the induced actions; the classes form the **unoriented $G$-bordism group** $\mathcal{N}_*^{G}$ and, for oriented $G$-manifolds and oriented cobordisms, the **oriented $G$-bordism ring** $\Omega_*^{G}$. For $G = \mathbb{Z}/2$ the elements are the involutions of closed manifolds up to equivariant cobordism.

**Proposition (elementary properties).** The equivariant bordism groups are modules over the ordinary bordism ring $\mathcal{N}_*$ (respectively $\Omega_*$) through the products with trivial actions, and the graded direct sums are graded rings under the product of $G$-manifolds with the diagonal action. The **fixed set** is a bordism invariant: if $M_0$ and $M_1$ are $G$-cobordant, then their fixed sets are cobordant as manifolds with the induced normal data; the **quotient** is a bordism invariant in the free case, where $M/G$ is a closed manifold of the same dimension.

**Proof.** The statements are formal: the product of a $G$-manifold with a manifold with trivial action is a $G$-manifold, giving the module and ring structure; a $G$-cobordism restricts to a cobordism of the fixed sets because the fixed set of the boundary is the boundary of the fixed set of the cobordism; in the free case the quotient of the cobordism is a cobordism of the quotients.

**Proposition (the free case reduces to the quotient).** If $G = \mathbb{Z}/2$ and the actions are free, then the association $M\mapsto M/\mathbb{Z}/2$ is a bijection from free equivariant bordism classes to ordinary bordism classes of closed manifolds of the same dimension; the inverse is the orientation double cover or the connected double cover according to the orientation behaviour.

**Proof.** The quotient of a free action is a manifold and the passage is compatible with the cobordisms; conversely every closed manifold has a free involution on its connected double cover, and the two constructions are inverse on the bordism classes. The statement is the free case of the equivariant theory and it shows that the free part of the equivariant bordism is the ordinary bordism of the quotients.

## The Conner–Floyd Theorem

**Theorem (Conner–Floyd).** For a finite group $G$ the unoriented equivariant bordism ring $\mathcal{N}_*^{G}$ is a polynomial algebra over $\mathbb{F}_2$, and two $G$-manifolds are $G$-cobordant if and only if they have the same equivariant Stiefel–Whitney numbers, that is, the same values of the Stiefel–Whitney classes of the normal representations evaluated on the fixed sets and of the ordinary Stiefel–Whitney classes of the quotient. For $G = \mathbb{Z}/2$ the generators can be taken to be the classes of the standard involutions: the free classes of the projective spaces and the classes of the reflections of the discs and spheres.

**Proof sketch.** The theorem is proved by the equivariant Pontryagin–Thom construction: the $G$-bordism is the homotopy of the equivariant Thom spectrum, and the equivariant Stiefel–Whitney numbers detect the homotopy classes by the structure of the equivariant cohomology of the classifying spaces; the polynomial algebra statement follows from the splitting of the spectrum into the pieces indexed by the orbit types and the ordinary Thom theorem on each piece. The proof and the explicit generators are those of Conner–Floyd; the present article records the statement and its consequence for the involutions.

**Corollary (the invariants of an involution up to cobordism).** The cobordism class of an involution of a closed manifold is determined by the equivariant Stiefel–Whitney numbers, which are computed from the fixed set (with its normal representations), the quotient and the action on the normal bundles; in particular the cobordism class is determined by data supported on the fixed set and on the quotient separately, which is the equivariant version of the splitting of the homology by the orbit types.

**Proof sketch.** The Stiefel–Whitney numbers are the evaluation of the characteristic classes on the fundamental classes of the fixed sets and of the quotients; the theorem says that these numbers are complete. The computation of the numbers from the fixed data is the content of the "double of the quotient" description in the smooth setting; the derivation is Part III's.

**Remark (the Smith homomorphism).** The passage to the fixed set gives a homomorphism from the equivariant bordism to the ordinary bordism of the fixed sets, shifted in degree by the codimension; it is a module homomorphism for the ordinary bordism, and it is the cobordism-level shadow of the Smith theory of *Periodic Maps and the Smith Theory*. Its image and kernel are computed by Conner–Floyd and are the algebraic skeleton of the equivariant bordism.

## The Oriented Theory and the Signature

**Definition.** The **oriented equivariant bordism ring** $\Omega_*^{G}$ is the bordism of closed oriented $G$-manifolds with orientation-preserving actions, modulo oriented equivariant cobordisms.

**Theorem (the oriented invariants, statement).** For a finite group $G$ the oriented equivariant bordism is detected by the equivariant Pontryagin numbers and the equivariant characteristic classes of the fixed sets, together with the **equivariant signature** in dimensions divisible by four: the multisignature of the fixed sets with their normal representations. In particular an orientation-preserving involution of a closed oriented $4k$-manifold that is equivariantly null-cobordant has vanishing ordinary signature and vanishing equivariant signatures $\sigma(g, M)$ at every element $g$ of the group.

**Proof sketch.** The oriented bordism is the homotopy of the oriented equivariant Thom spectrum; the characteristic numbers detect the homotopy classes rationally and the torsion is detected by the $\mathbb{Z}/2$-valued invariants, and the signature components are the $L$-theoretic part of the rational detection. The details for $\mathbb{Z}/2$ and the relation to the $G$-signature theorem are in the literature; the analytic computation of the $\sigma(g,M)$ is *Hermitian Pairings and the Equivariant Signature*, and the torsion statements are *Stable Homotopy Theory*.

**Corollary (cobordism invariance of the equivariant signature).** The multisignature $\sigma(g,M)$ is an invariant of the oriented equivariant bordism class of $(M,g)$; this is the cobordism-theoretic form of the $G$-signature theorem, and it is the reason the equivariant signature is the natural invariant of an equivariantly null-cobordant manifold.

**Proof.** The signature is a bordism invariant of an oriented manifold, and the equivariant signatures are the signatures of the twisted forms of *The Involution on the Homology*; the equivariant cobordism restricts to the twisted forms on the boundary, so that the twisted signatures add over a cobordism and vanish on a null-cobordism.

**Remark (the tom Dieck splitting).** The equivariant bordism of a finite group splits, after the appropriate completion, as a sum of the bordism of the centralisers or normalisers of the subgroups: the "orbit-type" splitting of the equivariant Thom spectrum. The statement organises the computations of the equivariant bordism rings, and its systematic development belongs to the equivariant stable homotopy of *Stable Homotopy Theory*. The present article uses the splitting only as the reason the free and the fixed parts can be treated separately.

## Examples

**Example (the free involutions).** The antipodal map of $S^{2n+1}$ is a free orientation-preserving involution with quotient $\mathbb{RP}^{2n+1}$; its equivariant bordism class is the class of the quotient, and the free classes are the images of the ordinary bordism under the double cover. The example shows the reduction of the free part to the ordinary bordism.

**Example (the reflections).** The reflection of $S^n$ in an equator has fixed set $S^{n-1}$ and quotient the disc; its equivariant bordism class is a standard "fixed" generator, and its equivariant Stiefel–Whitney numbers are those of the fixed sphere with the trivial normal line. The classes of the reflections and the free projective classes generate the unoriented equivariant bordism of $\mathbb{Z}/2$ by Conner–Floyd.

**Example (the null-cobordant involutions).** An orientation-preserving involution of an even-dimensional closed oriented manifold bounds an equivariant null-cobordism exactly when its ordinary and equivariant signatures vanish and its equivariant characteristic numbers vanish; the statement is the dimension-by-dimension form of the oriented detection theorem, and the dimension four is the first in which the signature components are nontrivial.

**Example (the involution on the double of a manifold with boundary).** Let $\Sigma$ be a compact manifold with boundary and let $M$ be its double; the reflection swapping the two copies is an involution with fixed set the boundary. The class of the involution is the "boundary" class, and it is a boundary of the equivariant cobordism — the trace being $\Sigma\times[0,1]$ with the reflection — so the construction exhibits the fixed-set classes of the reflections as the boundaries. The example is the cobordism-level statement of the double construction used in the surface classification.

## The Module Structure and the Comparison

**Proposition (the equivariant bordism as a module over the ordinary bordism).** The product of a $G$-manifold with a manifold of trivial action makes $\mathcal{N}_*^{G}$ a graded module over the ordinary bordism ring $\mathcal{N}_*$ and makes $\mathcal{N}_*^{G}$ a graded algebra over $\mathcal{N}_*$; the forgetful map $\mathcal{N}_*^{G}\to\mathcal{N}_*$, which forgets the action, is a homomorphism of $\mathcal{N}_*$-modules and of rings, and it is surjective because the trivial action on a manifold provides a section.

**Proof.** The product with the trivial action is a $G$-manifold with the action on the first factor only; the associativity and the distributivity give the module and the algebra structure; the forgetful map is compatible with the products because forgetting the action of a product is forgetting the action on the factor. The trivial action gives the section $M\mapsto M$ with the trivial $G$-action, so the forgetful map is surjective.

**Remark (the kernel and the equivariant refinement).** The kernel of the forgetful map consists of the $G$-manifolds equivariantly cobordant to a manifold with the trivial action; it is the "purely equivariant" part of the bordism, detected by the equivariant Stiefel–Whitney numbers of the nontrivial representations. For $\mathbb{Z}/2$ the kernel is spanned by the free classes and by the classes of the reflections, which is the content of the splitting of the equivariant bordism into the free and the fixed parts.

## The Fixed-Set Data in Cobordism

**Proposition (the fixed set of an involution, structurally).** Let a smooth involution act on a closed $n$-manifold $M$. Then the fixed set $F$ is a disjoint union of closed submanifolds, and the normal bundle of each component splits as a sum of line bundles on which the involution acts by $-1$; the codimension of a component can be any integer between $0$ and $n$, and the whole normal representation is a sum of copies of the sign representation. The fixed set is a bordism invariant: a $G$-cobordism restricts to a cobordism of the fixed sets with their normal data.

**Proof.** At a fixed point the differential of the involution is an involution of the tangent space, hence diagonalisable with eigenvalues $\pm1$; the $+1$ eigenspace is the tangent space of the fixed set and the $-1$ eigenspace the normal direction, so the normal bundle splits into the eigen-line-bundles and the representation is a sum of signs. The bordism invariance is the restriction of a $G$-cobordism to the fixed sets, as in the elementary properties above.

**Theorem (the equivariant numbers of the fixed set).** The equivariant Stiefel–Whitney numbers of an involution are the ordinary Stiefel–Whitney numbers of the fixed components evaluated against the characteristic classes of their normal bundles, together with the ordinary numbers of the quotient; hence the cobordism class of the involution is determined by the fixed-set data and the quotient data separately, and the fixed-set part of the determination is an invariant of the Smith theory of *Periodic Maps and the Smith Theory*.

**Proof sketch.** The total Stiefel–Whitney class of $M$ restricts to the fixed set as the product of the class of the fixed component and the class of the normal bundle with the signs of the summands; the evaluation on the fundamental class of the fixed component gives the stated numbers, and the completeness is Conner–Floyd's theorem. The quotient numbers are computed from the same data by the Smith sequences.

**Example (the fixed spheres and the codimension).** The reflection of $S^n$ has the fixed equator $S^{n-1}$ of codimension one, and the free antipodal involution has empty fixed set; the two extremes realise the two ends of the fixed-set dichotomy, and the intermediate cases are the fixed submanifolds of intermediate codimension with the normal sums of sign representations. The example shows the freedom of the codimension in the fixed-set data of the cobordism.

## Summary

Two involutions of closed manifolds are equivariantly cobordant when they bound an involution of a manifold with boundary; the classes form the equivariant bordism rings, modules and algebras over the ordinary bordism, with the fixed set and the quotient as bordism invariants. In the free case the equivariant bordism is the ordinary bordism of the quotients, through the double cover. The Conner–Floyd theorem states that the unoriented equivariant bordism of a finite group is a polynomial algebra over $\mathbb{F}_2$ and that its invariants are the equivariant Stiefel–Whitney numbers, computable from the fixed data and the quotient; the passage to the fixed set is the Smith homomorphism. The oriented equivariant bordism is detected by the equivariant Pontryagin numbers together with the equivariant signatures in dimensions divisible by four, and the equivariant signature is a bordism invariant, which is the cobordism-theoretic form of the $G$-signature theorem. The free involutions, the reflections, the null-cobordant involutions and the involutions on the double of a manifold with boundary are the standard examples, and the splitting by the orbit types organises the computation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$-manifold, $G$-cobordism | a closed manifold with a $G$-action; a $G$-manifold with boundary realising the cobordism |
| $\mathcal{N}_*^{G}$ | the unoriented equivariant bordism ring |
| $\Omega_*^{G}$ | the oriented equivariant bordism ring |
| $M/G$, $F = M^{G}$ | the quotient and the fixed set; bordism invariants |
| free case $M\mapsto M/\mathbb{Z}/2$ | the free equivariant bordism is the ordinary bordism of the quotients |
| equivariant Stiefel–Whitney numbers | the Conner–Floyd invariants detecting the unoriented equivariant bordism |
| Smith homomorphism | the passage from the equivariant bordism to the ordinary bordism of the fixed sets |
| $\sigma(g,M)$ | the equivariant signature, an oriented equivariant bordism invariant in dimensions $4k$ |
| equivariant Pontryagin numbers | the rational invariants of the oriented equivariant bordism |
| orbit-type splitting | the tom Dieck decomposition organising the equivariant bordism |
| forgetful map $\mathcal{N}_*^{G}\to\mathcal{N}_*$ | forgetting the action; surjective, with the trivial action as a section |
| normal bundle of a fixed component | a sum of line bundles with the $-1$ action of the involution |
| $F$ and $M\setminus F$ | the fixed set and the free part; the two orbit types of the action |

## Further Reading

- Pierre E. Conner and Edwin E. Floyd, *Differentiable Periodic Maps* (Springer, 1964), for the equivariant bordism rings, the Conner–Floyd classes and the structure theorems for $\mathbb{Z}/p$ actions.
- Pierre E. Conner, *Differentiable Periodic Maps*, second edition (Springer Lecture Notes 738, 1979), for the systematic theory and the Smith homomorphisms.
- Tammo tom Dieck, "Bordism of $G$-Manifolds and Integrality Theorems", *Topology* 9 (1970), 345–358, for the splitting of the equivariant bordism and the integrality.
- Tammo tom Dieck, *Transformation Groups and Representation Theory* (Springer Lecture Notes 766, 1979), for the equivariant homotopy, the Thom spectra and the bordism.
- R. E. Stong, *Notes on Cobordism Theory* (Princeton University Press, 1968), for the ordinary cobordism rings and the characteristic numbers used as the comparison.
- Michael F. Atiyah and Isadore M. Singer, "The Index of Elliptic Operators: III", *Annals of Mathematics* 87 (1968), 546–604, for the $G$-signature theorem, whose equivariant signature is the oriented invariant here.
- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for the Smith theory and the fixed-set techniques underlying the equivariant cobordism.
