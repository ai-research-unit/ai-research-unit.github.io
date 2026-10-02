
# __Hermitian Lie Groups and the Bounded Domain__

## Introduction

A **Hermitian Lie group** is a connected Lie group whose symmetric space carries a complex structure invariant under the group; equivalently the adjoint action of the centre of the maximal compact subalgebra provides an almost complex structure that is integrable. The invariant complex structure turns the symmetric space into a Hermitian manifold, and a theorem of Harish-Chandra identifies it, by a holomorphic embedding, with a **bounded symmetric domain** in a complex vector space, on which the group acts by biholomorphic automorphisms. The bounded domain is the concrete model of the Hermitian symmetric space, and the group acting on it is the analytic object of this article.

This article treats Hermitian Lie groups and the bounded domain with the Harish-Chandra realisation. It is the fourth article of the `- * Theory` group of the category; the Cartan decomposition and the maximal compact subgroup are *The Cartan Decomposition and the Cartan Involution*, the real forms and the symmetric space are *Real Forms of a Complex Lie Group and the Cartan Involution*, and the unitary representations attached to the holomorphic structure appear in *Unitary Representations of a Lie Group*.

The article assumes the Lie group, its Lie algebra and the exponential from *Lie Groups* and *The Lie Algebra and the Exponential Map*, the Cartan decomposition, the maximal compact subgroup and the polar decomposition from *The Cartan Decomposition and the Cartan Involution*, the root data and the classification from *Root Systems and Classification*, and the holomorphic functions and the domains of holomorphy from *Several Complex Variables*, the complex manifolds themselves belonging to the geometry of Part IV and named here and not used. The Bergman kernel and the analytic theory of the domains are used by name from *Hermitian Symmetric Spaces and the Bergman Metric*; the metric, the curvature and the geodesics of the domain as objects of study belong to Part IV, and the metric is named here and not developed. The Hermitian structure is used with its complex-analytic meaning and no physical interpretation.

## The Hermitian Structure

### The Centre of the Maximal Compact Subalgebra

**Definition.** A **Hermitian Lie group** is a connected Lie group $G$ with a Cartan decomposition $\mathrm{G} = \mathrm{K}\oplus\mathrm{P}$ for which the centre $\mathfrak{z}(\mathrm{K})$ of the maximal compact subalgebra is one-dimensional and acts on $\mathrm{P}$ with the eigenvalues $0$ and $\pm i$ under $\operatorname{ad}$; equivalently, $G/K$ carries a $G$-invariant complex structure.

**Proposition.** Let $Z_0$ span $\mathfrak{z}(\mathrm{K})$. Then $\operatorname{ad}_{Z_0}$ has the eigenvalues $0$, $i$ and $-i$, its $0$-eigenspace is $\mathrm{K}$, and the decomposition

$$
\mathrm{P}\otimes\mathbb{C} = \mathrm{P}^{+}\oplus\mathrm{P}^{-}
$$

into the $i$- and the $-i$-eigenspaces gives $\mathrm{P}$ a complex structure by the operator $J = \operatorname{ad}_{Z_0}$ restricted to $\mathrm{P}$; the operator $J$ is $K$-invariant, $J^2 = -\mathrm{id}$, and $[JX,JY] = [X,Y]$ for $X,Y\in\mathrm{P}$.

*Proof.* The operator $\operatorname{ad}_{Z_0}$ commutes with the action of $\mathrm{K}$ and preserves $\mathrm{P}$, since $Z_0$ is central in $\mathrm{K}$; its eigenvalues are purely imaginary because $\mathrm{K}$ is of compact type, and the existence of $Z_0$ with the eigenvalue $i$ on $\mathrm{P}$ is the definition. The identity $J^2 = -\mathrm{id}$ holds on $\mathrm{P}$ by the eigenvalue condition, and the $K$-invariance of the commutator and of the decomposition gives the last statement.

### The Complex Structure

**Definition.** The almost complex structure on $G/K$ is the left translation of $J$ on $\mathrm{P}\cong T_o(G/K)$; it is **integrable** because $G$ acts by the holomorphic maps defined below, so it is a complex structure.

**Theorem.** The almost complex structure $J$ on $G/K$ is integrable, the Hermitian metric $B_\theta$ is $J$-invariant, and the group $G$ acts on $G/K$ by holomorphic isometries; the curvature form of the metric is a positive $(1,1)$-form, so the metric is Kähler.

*Proof.* The integrability of a left-invariant almost complex structure on a homogeneous space of a complex Lie group is the vanishing of the Nijenhuis tensor, which is verified from the bracket relations and the eigenvalue condition on $\mathrm{ad}_{Z_0}$; the invariance of the metric under $J$ and $G$ follows from the invariance of $B_\theta$ under the adjoint action; the positivity of the curvature form is the positive definiteness of $B_\theta$ on $\mathrm{P}$ read as a Hermitian form. The geometric theory of the Kähler structure belongs to Part IV.

## The Bounded Domain

### The Harish-Chandra Realisation

**Theorem (Harish-Chandra).** Let $G$ be a Hermitian Lie group of non-compact type. Then there is a $\mathbb{C}$-linear embedding of the complexification of $\mathrm{P}$ into the complexification of $\mathrm{G}$ by which the symmetric space $G/K$ is biholomorphic to a bounded symmetric domain $D\subset\mathbb{C}^n$; the group $G$ acts on $D$ by biholomorphic automorphisms, the stabiliser of the base point is $K$, and $D$ is homogeneous under $G$.

*Proof (sketch).* The embedding is the Harish-Chandra realisation of the symmetric space as a bounded domain: the complexified group $G_{\mathbb{C}}$ acts on the complexified flag manifold, the real group $G$ preserves the bounded domain that is the orbit of the base point, and the isotropy is $K$; the domain is bounded because the orbit lies in a bounded set of the embedding space, and the biholomorphism is the restriction of the embedding. The complete proof is in the references.

**Definition.** A **bounded symmetric domain** is a bounded open connected subset $D\subset\mathbb{C}^n$ such that for every $z\in D$ there is an involutive biholomorphic automorphism of $D$ with $z$ as its isolated fixed point. The Harish-Chandra realisation gives a bijection between the Hermitian Lie groups of non-compact type and the bounded symmetric domains.

### The Bergman Metric and the Kernel

**Theorem.** A bounded symmetric domain carries a canonical Kähler metric, the **Bergman metric**, whose Kähler form is the curvature form of the Bergman kernel; the metric is Hermitian, its automorphism group is a Hermitian Lie group acting transitively, and the metric is the one for which the domain is a symmetric space.

*Proof.* The Bergman space of a bounded domain is a reproducing-kernel Hilbert space of holomorphic functions, the kernel is positive definite, and the metric it defines is Kähler; the invariance of the kernel under the biholomorphic automorphisms gives the invariance of the metric, and the symmetry statement is the existence of the involutive automorphism at each point. The analytic theory of the kernel and the metric is *Hermitian Symmetric Spaces and the Bergman Metric*.

**Corollary.** The bounded symmetric domain is contractible and diffeomorphic to $\mathrm{P}$, the Bergman metric is complete, and the exponential map of the Hermitian Lie group at the base point is the inverse of the Harish-Chandra embedding in the direction of $\mathrm{P}$.

*Proof.* The statement is the polar decomposition of *The Cartan Decomposition and the Cartan Involution*, under which $G/K$ is diffeomorphic to the vector space $\mathrm{P}$, transported to the bounded domain by the embedding; completeness is the homogeneity and the closedness of the automorphism group, and the identification of the exponential is the construction of the embedding.

## The Tube Domain and the Boundary

### The Tube Domain

**Definition.** Let $G$ be a Hermitian Lie group of non-compact type with Cartan decomposition $\mathrm{G} = \mathrm{K}\oplus\mathrm{P}$ and let $\Omega\subseteq\mathrm{P}$ be the open convex cone of the elements $X$ for which $\operatorname{ad}_X$ has only real eigenvalues; the cone is self-dual and homogeneous under $K$, and the **tube domain** over it is

$$
T_\Omega = \mathrm{P} + i\Omega\;\subseteq\;\mathrm{P}\otimes\mathbb{C} ,
$$

a domain of holomorphy in the complexification of $\mathrm{P}$.

**Theorem.** The tube domain is biholomorphic to the bounded symmetric domain, the biholomorphism being the **Cayley transform**

$$
c = (\mathrm{id} - J)(\mathrm{id} + J)^{-1}\big|_{\mathrm{P}} ,
$$

which extends to a biholomorphism of a neighbourhood of the base point with $c(0) = 0$ and carries the tube to the bounded domain; the group $G$ acts on the tube by the affine transformations $X\mapsto \operatorname{Ad}_kX + Y$ with $k\in K$ and $Y\in\mathrm{P}$.

*Proof.* The eigenvalues of $\operatorname{ad}_X$ for $X\in\Omega$ are real, so $\mathrm{id}\pm J$ is invertible on the tube and the Cayley transform is holomorphic there; the image is bounded because the transform sends the self-dual cone to a bounded set, and the inverse transform recovers the tube. The affine action is the restriction of the action of *The Cartan Decomposition and the Cartan Involution* to the abelian part.

### The Siegel Domain

**Theorem (the Siegel upper half-plane).** For $G = Sp(n,\mathbb{R})$ the cone is the cone of the positive definite symmetric matrices, the tube domain is the Siegel upper half-plane

$$
\mathcal{H}_n = \bigl\{Z\in\operatorname{Sym}_n(\mathbb{C}) : \operatorname{Im}Z>0\bigr\} ,
$$

and the group acts by the fractional linear transformations $Z\mapsto (AZ+B)(CZ+D)^{-1}$; the bounded realisation is the corresponding bounded symmetric domain of rank $n$.

*Proof.* The identification of the cone with the positive definite matrices is the structure of the symplectic group; the fractional linear formula is the action on the tube, and the boundedness of the realisation is the previous theorem.

### The Boundary Components

**Theorem.** The boundary of the bounded symmetric domain in its Harish-Chandra realisation is a union of finitely many $G$-orbits, the **boundary components**; each boundary component is itself a symmetric space $G/Q$ for a parabolic subgroup $Q$, the orbits are partially ordered by the inclusion of their closures, and the unique closed orbit is the **Shilov boundary**, the orbit of the compact dual of $G/K$.

*Proof.* The boundary is a closed $G$-invariant subset and therefore a union of orbits; the stabiliser of a boundary point is a parabolic subgroup because the orbit map is proper in the Harish-Chandra realisation, and the boundary component is the symmetric space of the parabolic; the closed orbit is the smallest, the one of the compact dual. The proof is in the references.

**Proposition.** The rank of the domain is the number of the boundary components of maximal dimension, and the Shilov boundary is the symmetric space of the maximal compact subgroup of the compact dual; the boundary components are the flag manifolds of the parabolic subgroups of the complexified group.

*Proof.* The rank is the number of the simple factors of the parabolic components, read from the Satake diagram; the Shilov boundary is the orbit of the compact dual by the definition, and it is a compact symmetric space.

## The Hermitian Lie Algebras

### The Classification

**Theorem (classification).** The Hermitian Lie algebras of non-compact type are classified by their maximal compact subalgebra $\mathrm{K}$, which has a one-dimensional centre, and by the representation of $\mathrm{K}$ on $\mathrm{P}$; the irreducible ones are the algebras of the four infinite families $\mathrm{su}(p,q)$, $\mathrm{so}(2,n)$, $\mathrm{sp}(n,\mathbb{R})$ and $\mathrm{so}^{*}(2n)$ and the two exceptional algebras $\mathfrak{e}_{6(-14)}$ and $\mathfrak{e}_{7(-25)}$, and the corresponding bounded domains are irreducible.

*Proof.* The classification of the Hermitian Lie algebras is the classification of the pairs $(\mathrm{G},\mathrm{K})$ with $\dim\mathfrak{z}(\mathrm{K}) = 1$ and the eigenvalue condition; it is read from the Satake diagrams of *Real Forms of a Complex Lie Group and the Cartan Involution* by the additional requirement on the centre, and the list is the standard classification. The proof is in the references.

### The Rank and the Symmetry

**Definition.** The **rank** of a bounded symmetric domain — and of the Hermitian Lie group — is the dimension of a maximal abelian subspace of $\mathrm{P}$; thus rank one gives the complex hyperbolic balls and the higher rank gives the bounded symmetric domains that are not balls.

**Theorem.** A bounded symmetric domain of rank one is biholomorphic to the unit ball of $\mathbb{C}^n$, and every bounded symmetric domain is biholomorphic to a product of irreducible ones; the rank is the number of factors in the polydisc case and controls the dimension of the maximal polydisc contained in the domain.

*Proof.* The rank-one statement is the classification of the rank-one Hermitian Lie algebras, which are $\mathrm{su}(1,n)$ up to the exceptional case, and the ball is the associated domain; the product decomposition is the decomposition of the semisimple algebra into its simple factors, and the polydisc statement follows from the rank. The details are in the references.

## Examples

### The Unit Disc

For $G = SU(1,1)\cong SL_2(\mathbb{R})$ the symmetric space is the hyperbolic plane, the maximal compact subgroup is $SO(2)$, the rank is one, and the bounded domain is the unit disc of $\mathbb{C}$; the Harish-Chandra realisation is the Cayley transform from the upper half-plane to the disc, and the Bergman metric is the Poincaré metric, whose geometry belongs to Part IV.

### The Siegel Upper Half-Plane

For $G = Sp(n,\mathbb{R})$ the symmetric space is the Siegel upper half-plane of symmetric complex matrices with positive definite imaginary part, a Hermitian symmetric space of rank $n$; the group acts by the fractional linear transformations $Z\mapsto (AZ+B)(CZ+D)^{-1}$, the maximal compact subgroup is the unitary group $U(n)$, and the bounded realisation is the corresponding bounded symmetric domain.

### The Orthogonal Case

For $G = SO(2,n)$ the symmetric space is the complex quadric, of rank two for $n\geq3$; the maximal compact subgroup is $SO(2)\times SO(n)$ with the one-dimensional centre of the first factor, and the bounded domain is the bounded realisation of the quadric; the case $n = 2$ is a product of two discs and the case $n = 1$ is degenerate.

### The Complex Case

For a complex semisimple group regarded as a real Hermitian group, the symmetric space is the space of the maximal compact subgroups, the complex structure is the one of the complex group itself, and the bounded domain is the Harish-Chandra realisation of the complex symmetric space; the group $\mathrm{G}^{\mathbb{R}}$ acts on its compact dual by the complex structure, which is the content of the example of *The Cartan Decomposition and the Cartan Involution*.

## Summary

A **Hermitian Lie group** is a connected Lie group with a Cartan decomposition whose maximal compact subalgebra has a one-dimensional centre acting on the complement with the eigenvalues $0$ and $\pm i$; the operator $J = \operatorname{ad}_{Z_0}$ is an invariant complex structure on the symmetric space, the metric $B_\theta$ is Kähler for it, and the group acts by holomorphic isometries. The **Harish-Chandra realisation** embeds the symmetric space biholomorphically as a **bounded symmetric domain** $D\subset\mathbb{C}^n$, on which $G$ acts transitively by biholomorphic automorphisms with stabiliser $K$; the bounded symmetric domains are exactly the domains with an involutive biholomorphic automorphism having an isolated fixed point at each point, and they carry the canonical Bergman metric, which is complete and makes the domain a symmetric space diffeomorphic to the vector space $\mathrm{P}$. The irreducible Hermitian Lie algebras of non-compact type are the four infinite families $\mathrm{su}(p,q)$, $\mathrm{so}(2,n)$, $\mathrm{sp}(n,\mathbb{R})$, $\mathrm{so}^{*}(2n)$ and the two exceptional algebras, the rank of the domain is the dimension of a maximal abelian subspace of $\mathrm{P}$, the rank-one case is the unit ball, and the general domain is a product of irreducible ones. The metric, the curvature and the geodesics as objects of study are Part IV, and the holomorphic discrete series of representations attached to the domain is the subject of *Unitary Representations of a Lie Group* and of the harmonic analysis of the group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{G} = \mathrm{K}\oplus\mathrm{P}$ | the Cartan decomposition of a Hermitian Lie group |
| $\mathfrak{z}(\mathrm{K})$ | the centre of the maximal compact subalgebra, one-dimensional |
| $Z_0$ | a generator of the centre |
| $J = \operatorname{ad}_{Z_0}$ on $\mathrm{P}$ | the invariant complex structure, $J^2 = -\mathrm{id}$ |
| $\mathrm{P}\otimes\mathbb{C} = \mathrm{P}^+\oplus\mathrm{P}^-$ | the $\pm i$-eigenspaces of $J$ |
| $G/K$ | the Hermitian symmetric space |
| $D\subset\mathbb{C}^n$ | the bounded symmetric domain |
| Harish-Chandra realisation | the biholomorphism $G/K\to D$ |
| Bergman metric | the canonical complete Kähler metric on $D$ |
| $\mathrm{su}(p,q)$, $\mathrm{so}(2,n)$, $\mathrm{sp}(n,\mathbb{R})$, $\mathrm{so}^{*}(2n)$ | the classical Hermitian Lie algebras |
| rank | the dimension of a maximal abelian subspace of $\mathrm{P}$ |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for the Hermitian symmetric spaces, the Harish-Chandra realisation and the bounded domains.
- Ottmar Loos, *Bounded Symmetric Domains and Jordan Pairs* (University of California, Irvine, 1977), for the algebraic classification of the bounded symmetric domains.
- Ichiro Satake, *Algebraic Structures of Symmetric Domains* (Princeton University Press, 1980), for the classification, the Hermitian Lie algebras and the Harish-Chandra embedding.
- Soji Kaneyuki and Makoto Kozai, "Parabolic subgroups of semisimple Lie groups and Siegel domains", *Journal of Mathematics of Kyoto University* **11** (1971), for the boundary structure of the bounded domains.
- Steven G. Krantz, *Function Theory of Several Complex Variables* (AMS Chelsea, second edition, 2001), for the Bergman kernel, the Bergman metric and the holomorphic automorphisms of the domains.
