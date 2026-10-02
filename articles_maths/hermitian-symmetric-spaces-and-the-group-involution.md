
# __Hermitian Symmetric Spaces and the Group Involution__

## Introduction

Of the symmetric spaces, some carry an invariant complex structure for which the geodesic symmetry is complex-antisymmetric; these are the **Hermitian symmetric spaces**. The condition is not metrically visible at the level of one geodesic; it is a condition on the **involution** of the group: the symmetric space $G/K$ is Hermitian exactly when the Cartan involution is the inner automorphism by an element of the centre of $K$, and that central element is the complex structure of the tangent space. The classification of the irreducible Hermitian symmetric spaces therefore becomes a classification of the symmetric pairs whose involution is of this inner type, and it produces four infinite families and two exceptional spaces — the classification of Cartan.

The article treats the complex structure carried by the involution, the characterisation of the Hermitian case by a central element of the isotropy, the classification into the six types, and the bounded domains the noncompact types realise. The symmetric spaces, the symmetric pairs, the Cartan involution, the rank and the irreducibility are *Riemannian Symmetric Spaces and the Involution*; the homogeneous space $G/K$ and the isotropy representation are *Transformation Groups*; the unitary and orthogonal groups and their involutions are the two previous articles of this group; the Lie algebras and the real forms are *The Cartan Decomposition and the Cartan Involution*, *Real Forms of a Complex Lie Group and the Cartan Involution* and *The Orthogonal Lie Algebra*; the exceptional Lie groups are *Lie Groups*. The invariant Kähler metric, the Bergman kernel and the boundary theory of the domains are *Hermitian Symmetric Spaces and the Bergman Metric* and *The Bergman Operator*, below this Part, and the Hermitian manifolds with an isometric involution are *Hermitian Manifolds and the Geodesic Involution*, in *Foundations of Geometry*; both are named and not developed. The involution on the **elements** of the group is read here; the **adjoint** is the group `- * Operator Theory`.

The article has four sections: the complex structure and the involution; the characterisation by the centre of the isotropy; the classification; and the worked cases. Throughout, $G$ is a connected semisimple real Lie group with finite centre, $\theta$ a Cartan involution, $K = G^{\theta}$ the maximal compact subgroup, $X = G/K$ the symmetric space, and $\mathfrak{g} = \mathfrak{k}\oplus\mathfrak{p}$ the Cartan decomposition.

## The Complex Structure and the Involution

### The Hermitian Condition

**Definition.** A symmetric space $X = G/K$ is **Hermitian** when it carries a $G$-invariant almost complex structure $J$ such that $J$ is integrable and the geodesic symmetry $s_o$ at the base point is complex-antisymmetric, $ds_o \circ J = -J \circ ds_o$; the triple $(X, J, g)$ of the complex structure, the invariant metric and the form is a Hermitian symmetric space.

**Proposition.** The invariant almost complex structures on $X$ correspond to the complex structures $J_o$ on $\mathfrak{p}$ commuting with the isotropy representation $\operatorname{Ad}|_K$; the integrability of $J_o$ is automatic when $X$ is symmetric, and the complex-antisymmetry of the geodesic symmetry is the condition $J_o[s_o] = -[s_o]$, i.e., that $J_o$ anticommutes with $ds_o$, which is the map $-\mathrm{id}$ on $\mathfrak{p}$ composed with the involution.

**Proof.** An invariant tensor on $G/K$ is determined by its value at $o$, and its invariance is the commutation with the isotropy representation; the torsion of the almost complex structure vanishes because $\nabla J \equiv 0$ is forced by the homogeneity, so the Nijenhuis tensor vanishes, the standard integrability of the invariant structure. The antisymmetry is the evaluation of the relation $s_o^2 = \mathrm{id}$ together with the definition, *Riemannian Symmetric Spaces and the Involution* and *Kähler Geometry*, below this Part.

### The Central Element

**Theorem (the Hermitian involution).** The symmetric space $G/K$ is Hermitian exactly when there is $z \in Z(K)$, the centre of $K$, with

$$
\theta = \operatorname{Ad}(z), \qquad \operatorname{Ad}(z)|_{\mathfrak{p}} = -\mathrm{id}, \qquad \operatorname{Ad}(z)|_{\mathfrak{k}} = \mathrm{id},
$$

and then the complex structure on $\mathfrak{p}$ is $\mathrm{ad}(Z)$ for $Z = \log$-type generator of the circle $z$, with $\mathrm{ad}(Z)^2 = -\mathrm{id}$ on $\mathfrak{p}$ and $\mathrm{ad}(Z)|_{\mathfrak{k}} = 0$. Equivalently, the involution $\theta$ is **inner** and is the adjoint action of an element of the centre of $K$; a pair with this property is a **Hermitian symmetric pair** and $\theta$ a **Hermitian involution**.

**Proof.** If $G/K$ is Hermitian, the complex structure $J_o$ on $\mathfrak{p}$ commutes with $\operatorname{Ad}|_K$ and satisfies $J_o^2 = -\mathrm{id}$; since the isotropy representation of an irreducible symmetric space is irreducible, Schur's lemma gives a central element $Z \in \mathfrak{k}$ with $\mathrm{ad}(Z)|_{\mathfrak{p}} = J_o$ and $\mathrm{ad}(Z)|_{\mathfrak{k}} = 0$, because $Z$ central acts trivially on $\mathfrak{k}$; then $z = \exp(\pi Z)$ lies in $Z(K)$ and $\operatorname{Ad}(z)|_{\mathfrak{p}} = e^{\pi J_o} = -\mathrm{id}$, $\operatorname{Ad}(z)|_{\mathfrak{k}} = \mathrm{id}$, so $\theta = \operatorname{Ad}(z)$. Conversely, if $\theta = \operatorname{Ad}(z)$ with $z \in Z(K)$ and $\operatorname{Ad}(z)|_{\mathfrak{p}} = -\mathrm{id}$, then $Z = $ the generator of the circle through $z$ has $\mathrm{ad}(Z)|_{\mathfrak{p}}$ an invariant complex structure and $\mathrm{ad}(Z)|_{\mathfrak{k}} = 0$, which is integrable and complex-antisymmetric. The argument is Cartan's, and is given in *Riemannian Symmetric Spaces and the Involution*.

**Remark.** The condition is a condition on the **involution**: it must be inner, and the inner element must lie in the centre of the isotropy. The complex structure is the logarithm of that central element read on the tangent space, so the geometry of the Hermitian symmetric space is carried by the involution of the group. This is the sense of the group `- * Theory` of this category: the involution on the elements is the object, and the complex structure is its geometric trace.

## The Characterisation by the Centre of the Isotropy

**Proposition.** For an irreducible symmetric space the following are equivalent:

1. $G/K$ is Hermitian;
2. the involution $\theta$ is inner, $\theta = \operatorname{Ad}(z)$ for some $z \in Z(K)$;
3. the centre $\mathfrak{z}(\mathfrak{k})$ is nonzero, of dimension one;
4. the isotropy representation $\operatorname{Ad}|_K$ on $\mathfrak{p}$ admits an invariant complex structure.

When these hold, the centre of $\mathfrak{k}$ is one-dimensional and generated by $Z$ with $\mathrm{ad}(Z)^2 = -\mathrm{id}$ on $\mathfrak{p}$.

**Proof.** The equivalence of 1 and 2 is the theorem; 2 gives 3 because a central $z$ has a logarithm in the centre of $\mathfrak{k}$, and 3 gives 4 by Schur's lemma as in the theorem; 4 gives 1 by the integrability of the invariant structure. The one-dimensionality of $\mathfrak{z}(\mathfrak{k})$ is the irreducibility of the isotropy representation: a larger centre would decompose $\mathfrak{p}$ into the eigenspaces of $\mathrm{ad}(Z)$, all invariant.

**Corollary (the compact dual).** A Hermitian symmetric space of compact type has the same complex structure and the opposite curvature; the duality $G/K \leftrightarrow G^c/K$ preserves the involution, the centre of the isotropy and the complex structure, and reverses the sign of the curvature. The compact type consists of the complex Grassmannians and their spin and symplectic analogues.

**Proof.** The compact dual is built from the same $\mathfrak{k}$ and the same complexification with $\mathfrak{p}$ replaced by $i\mathfrak{p}$; the involution and the centre of $\mathfrak{k}$ are unchanged, so the complex structure is unchanged, and the curvature changes sign, *Riemannian Symmetric Spaces and the Involution*.

## The Classification

### The Six Types

**Theorem (Cartan's classification).** The irreducible Hermitian symmetric spaces fall into six types, four infinite families and two exceptional spaces; the noncompact types, their compact duals, their dimensions and their ranks are:

| Type | Noncompact $G/K$ | Compact dual | $\dim_{\mathbb{R}}$ | rank |
|---|---|---|---|---|
| A III | $SU(p,q)/S(U(p)\times U(q))$ | $SU(p+q)/S(U(p)\times U(q))$ | $2pq$ | $\min(p,q)$ |
| B D I | $SO(2,n)/(SO(2)\times SO(n))$ | $SO(2+n)/(SO(2)\times SO(n))$ | $2n$ | $2$ |
| C I | $Sp(2n,\mathbb{R})/U(n)$ | $Sp(n)/U(n)$ | $n(n+1)$ | $n$ |
| D III | $SO^{*}(2n)/U(n)$ | $SO(2n)/U(n)$ | $n(n-1)$ | $\lfloor n/2\rfloor$ |
| E III | $E_{6(-14)}/(Spin(10)\times U(1))$ | $E_6/(Spin(10)\times U(1))$ | $32$ | $2$ |
| E VII | $E_{7(-25)}/(E_6\times U(1))$ | $E_7/(E_6\times U(1))$ | $54$ | $3$ |

the group $G$ is the identity component, the compact dual is the compact real form of the complexification with the same $K$, and the list is complete for the irreducible case; the reducible Hermitian symmetric spaces are products of the types.

**Proof.** The classification of the irreducible symmetric spaces is by the real forms of the complexified pair and the Satake diagram, *Real Forms of a Complex Lie Group and the Cartan Involution* and *Riemannian Symmetric Spaces and the Involution*; the Hermitian condition selects the pairs whose Satake diagram has a suitable symmetry, equivalently whose $\mathfrak{k}$ has a one-dimensional centre, which is a property visible on the diagram. The types A III, B D I, C I, D III are the classical families, and the exceptional pairs E III and E VII are the two exceptional Hermitian symmetric spaces, of rank two and three. The dimensions and the ranks are computed from the dimensions of the groups and their maximal compact subgroups. This is Cartan's classification, quoted.

**Remark.** The table is the classification the **involution** gives: the type is a property of the pair $(G,\theta)$, not of the abstract Lie algebra, and the two members of a dual pair — A III noncompact and A III compact — carry the same involution type and opposite curvature. The bounded domains that the noncompact types realise are the **Hermitian symmetric domains**, and they are the domains of the classification, *Hermitian Symmetric Spaces and the Bergman Metric*, below this Part.

### The Complex Structure of the Types

**Proposition.** In each type the complex structure is the isotropy element:

- **A III**: $\mathfrak{p}\cong\mathbb{C}^{pq}$ with the multiplication by $i$ on the entries of the matrix $Z$; the domain is the matrix unit ball of *The Unitary Group and the Hermitian Symmetric Space*.
- **B D I**: $\mathfrak{p}\cong\mathbb{C}^{n}$ with the complex structure of $\mathbb{C}^n$; the domain is the tube over the Lorentz cone, $\{z : \operatorname{Im} z \in \Omega\}$ with $\Omega$ the positive cone of a form of signature $(1,n-1)$.
- **C I**: $\mathfrak{p}\cong\mathbb{C}^{n(n+1)/2}$ with the complex structure of the symmetric matrices; the domain is the Siegel upper half space $\{Z = Z^{t} : \operatorname{Im} Z > 0\}$.
- **D III**: $\mathfrak{p}\cong\mathbb{C}^{n(n-1)/2}$; the compact dual $SO(2n)/U(n)$ is the manifold of orthogonal complex structures on $\mathbb{R}^{2n}$, the **isotropic Grassmannian**, and the noncompact dual is the same manifold with the opposite complex structure.

**Proof.** In each case the central element $Z \in \mathfrak{z}(\mathfrak{k})$ is exhibited and the adjoint action on $\mathfrak{p}$ is computed; the identification of the domain is the Harish-Chandra embedding of *Riemannian Symmetric Spaces and the Involution* for the type. The isotropic Grassmannian is the quotient $SO(2n)/U(n)$, whose points are the complex structures on $\mathbb{R}^{2n}$ compatible with the metric; the Grassmannians and the flag manifolds as homogeneous spaces are the subject of *Geometry on Linear Spaces*, below this Part.

## Worked Cases

**Example (the disc and the ball).** Type A III with $\min(p,q) = 1$ gives the complex hyperbolic spaces: $SU(1,n)/S(U(1)\times U(n))$ is the unit ball of $\mathbb{C}^n$ with the complex structure of $\mathbb{C}^n$ and rank one, the smallest-rank Hermitian symmetric space of the family. The disc $SU(1,1)/U(1)$ is the case $n = 1$, the Poincaré disc with the involution $\theta(g) = JgJ^{-1}$.

**Example (the Siegel upper half space).** Type C I, $Sp(2n,\mathbb{R})/U(n)$, realises the Siegel upper half space $\mathfrak{H}_n = \{Z \in \mathbb{C}^{n\times n} : Z = Z^{t},\ \operatorname{Im} Z > 0\}$, of dimension $n(n+1)$ and rank $n$; the involution is the conjugation by the form matrix $\Omega = \begin{pmatrix}0 & I \\ -I & 0\end{pmatrix}$ and the central element of $U(n)$ acts by the complex structure on the symmetric matrices. The domain is the source of the theory of modular forms of degree $n$, which is arithmetic and lies outside this article.

**Example (the tube domain).** Type B D I, $SO(2,n)/(SO(2)\times SO(n))$, realises the tube $\{z \in \mathbb{C}^{n} : \operatorname{Im} z \in \Omega\}$ over the Lorentz cone $\Omega = \{x : x_1^2 > x_2^2 + \cdots + x_n^2,\ x_1 > 0\}$ of a form of signature $(1,n-1)$; it has dimension $2n$ and rank two, and its complex structure is the complex structure of $\mathbb{C}^n$. For $n = 2$ the tube is the product of two discs, and for $n = 3$ it is the tube over the cone of positive-definite $2\times 2$ matrices.

**Example (the isotropic Grassmannian).** Type D III, with compact dual $SO(2n)/U(n)$, is the manifold of complex structures $J$ on $\mathbb{R}^{2n}$ with $J^2 = -\mathrm{id}$ and $J \in SO(2n)$; the involution is the conjugation by such a $J$, the isotropy $U(n)$ is the stabiliser of one complex structure, and the rank is $\lfloor n/2\rfloor$. The space is the only classical Hermitian symmetric space whose compact dual is a quotient of the rotation group by the unitary group.

**Example (the exceptional spaces).** Types E III and E VII are the two exceptional Hermitian symmetric spaces, of dimensions $32$ and $54$ and ranks $2$ and $3$, with isotropy groups $Spin(10)\times U(1)$ and $E_6\times U(1)$; they have no classical description as a Grassmannian and their domains are the exceptional bounded symmetric domains. They show that the Hermitian condition is not a property of the classical families alone.

## Summary

A symmetric space $G/K$ is Hermitian exactly when its Cartan involution is inner, $\theta = \operatorname{Ad}(z)$ for an element $z$ of the centre of the maximal compact subgroup $K$, and then the logarithm $Z \in \mathfrak{z}(\mathfrak{k})$ has $\mathrm{ad}(Z)|_{\mathfrak{p}}$ an invariant complex structure with $\mathrm{ad}(Z)^2 = -\mathrm{id}$ on $\mathfrak{p}$ and $\mathrm{ad}(Z) = 0$ on $\mathfrak{k}$; equivalently the isotropy representation admits an invariant complex structure, equivalently the centre of $\mathfrak{k}$ is one-dimensional. The compact dual shares the involution and the complex structure and reverses the curvature. Cartan's classification of the irreducible Hermitian symmetric spaces has six types — the four infinite families A III $SU(p,q)/S(U(p)\times U(q))$, B D I $SO(2,n)/(SO(2)\times SO(n))$, C I $Sp(2n,\mathbb{R})/U(n)$ and D III $SO^{*}(2n)/U(n)$, and the two exceptional spaces E III and E VII of ranks two and three — with the dimensions and ranks of the table; the reducible cases are products. The complex structure of each type is the isotropy element, and the noncompact types realise the bounded symmetric domains: the matrix unit ball, the Siegel upper half space and the tube over the Lorentz cone. The invariant Kähler metric and the Bergman kernel are *Hermitian Symmetric Spaces and the Bergman Metric*, below this Part. The object classified is the involution on the elements; no adjoint is taken.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X = G/K$, $\theta$ | a symmetric space and its Cartan involution |
| $\mathfrak{g} = \mathfrak{k}\oplus\mathfrak{p}$ | the Cartan decomposition |
| $J_o$ | the invariant complex structure on $\mathfrak{p}$ |
| $Z \in \mathfrak{z}(\mathfrak{k})$ | the central element with $\mathrm{ad}(Z)^2 = -\mathrm{id}$ on $\mathfrak{p}$ |
| $\theta = \operatorname{Ad}(z)$ | the Hermitian involution; $z \in Z(K)$ |
| A III, B D I, C I, D III | the four infinite families of Hermitian symmetric spaces |
| E III, E VII | the two exceptional Hermitian symmetric spaces |
| $\mathfrak{H}_n = \{Z = Z^{t} : \operatorname{Im} Z > 0\}$ | the Siegel upper half space; type C I |
| $SO(2n)/U(n)$ | the isotropic Grassmannian; the compact dual of D III |
| $\Omega$ | the Lorentz cone of a form of signature $(1,n-1)$ |
| $\lfloor n/2\rfloor$ | the rank of type D III |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the Hermitian symmetric spaces, the central element of the isotropy and the classification.
- Elie Cartan, "Sur les domaines bornés homogènes de l'espace de $n$ variables complexes", *Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg* **11** (1935), 116–162, for the classification of the Hermitian symmetric domains.
- Ichiro Satake, *Algebraic Structures of Symmetric Domains* (Princeton University Press, 1980), for the classification, the Satake diagrams and the bounded domains.
- Ottmar Loos, *Bounded Symmetric Domains and Jordan Pairs* (University of California, Irvine, 1977), for the Jordan-theoretic classification of the domains and the tube realisations.
- Joseph A. Wolf, *Spaces of Constant Curvature* (American Mathematical Society, sixth edition, 2011), for the Hermitian symmetric spaces of the classical groups and their complex structures.
