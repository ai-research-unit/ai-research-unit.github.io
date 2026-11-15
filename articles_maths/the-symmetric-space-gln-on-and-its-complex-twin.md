# __The Symmetric Space $\mathrm{GL}_n/O(n)$ and Its Complex Twin__

## Introduction

**The quotient $\mathrm{GL}_n(\mathbb{R})/\mathrm{O}(n)$ is the space of positive definite real symmetric matrices of dimension $n(n+1)/2$, its complex twin $\mathrm{GL}_n(\mathbb{C})/\mathrm{U}(n)$ is the cone of dimension $n^{2}$, and the second is obtained from the first by complexifying the field and replacing the transpose by the conjugate transpose.**

The article proves the two Cartan decompositions $\mathfrak{gl}_n(\mathbb{R})=\mathfrak{so}(n)\oplus\operatorname{Sym}_n(\mathbb{R})$ and $\mathfrak{gl}_n(\mathbb{C})=\mathfrak{u}(n)\oplus\operatorname{Herm}_n$ with the bracket relations of a symmetric pair, proves that the quotients are the two positive cones and that both are symmetric spaces of rank $n$, proves that the real space is the fixed locus of the conjugation inside the complex one, and proves that the compact duals are the orthogonal and the unitary groups with the dimensions $n(n-1)/2$ and $n^{2}$. It assumes *The Geometry of the Two Halves, and the Return of the Two-Sided Operators* and *The Two Base Fields: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$*. It defers the boundary to *The Cone of Positive Semidefinite Matrices* and the two-by-two case to *Coda: $n=2$ and the Biquaternion Algebra*.

## The Two Symmetric Spaces

**The real space is the space of the positive definite real symmetric matrices.** The group acts on the real symmetric matrices by congruence,

$$
\mathrm{GL}_n(\mathbb{R})\times\operatorname{PSD}_n(\mathbb{R})\to\operatorname{PSD}_n(\mathbb{R}),\qquad (g,P)\mapsto gPg^{\mathsf T},
$$

transitively, since every positive matrix is $gg^{\mathsf T}$, and the stabiliser of the identity is the orthogonal group. Hence

$$
\mathrm{GL}_n(\mathbb{R})/\mathrm{O}(n)\cong\operatorname{PSD}_n(\mathbb{R}),\qquad \dim_{\mathbb{R}}=\tfrac{n(n+1)}{2}.
$$

The computation confirms the dimension $3,6,10$ at $n=2,3,4$, and it is the real half of the subject.

**The complex twin is the cone of the previous articles.** The same argument with the conjugate transpose gives

$$
\mathrm{GL}_n(\mathbb{C})/\mathrm{U}(n)\cong\mathrm{PD}_n,\qquad \dim_{\mathbb{R}}=n^{2},
$$

which gives $4,9,16$ at $n=2,3,4$. The computation confirms the dimensions and the transitivity, and it is the complex half of the subject.

**The two spaces have the same rank.** In both cases a maximal flat is the space of the diagonal positive matrices, of dimension $n$, so the two ranks are equal,

$$
\operatorname{rank}\mathrm{GL}_n(\mathbb{R})/\mathrm{O}(n)=n=\operatorname{rank}\mathrm{GL}_n(\mathbb{C})/\mathrm{U}(n),
$$

which was confirmed at $n=2,3$ by the commuting families of the cones.

**The real space embeds in the complex one.** A real positive symmetric matrix is Hermitian positive definite, so

$$
\operatorname{PSD}_n(\mathbb{R})\subset\mathrm{PD}_n,\qquad \dim=\tfrac{n(n+1)}{2}\ \text{against}\ n^{2},
$$

with codimension $n(n-1)/2$. The computation confirms the inclusion and the codimension $1,3,6$ at $n=2,3,4$, and it is the reason the real space is a totally geodesic subspace of the complex one.

## The Cartan Decompositions

**The involution of the real case is the negative transpose.** The map

$$
\theta(X)=-X^{\mathsf T}
$$

is an involution of $\mathfrak{gl}_n(\mathbb{R})$ whose fixed set is $\mathfrak{so}(n)$ and whose anti-fixed set is the symmetric part, so

$$
\mathfrak{gl}_n(\mathbb{R})=\mathfrak{so}(n)\oplus\operatorname{Sym}_n(\mathbb{R}),\qquad \tfrac{n(n-1)}{2}+\tfrac{n(n+1)}{2}=n^{2}.
$$

The computation confirms the dimensions $1+3=4$ and $3+6=9$ at $n=2,3$, and it is the infinitesimal form of the quotient.

**The involution of the complex case is the negative conjugate transpose.** The map

$$
\theta(X)=-X^{*}
$$

has the fixed set $\mathfrak{u}(n)$ and the anti-fixed set $\operatorname{Herm}_n$, so

$$
\mathfrak{gl}_n(\mathbb{C})=\mathfrak{u}(n)\oplus\operatorname{Herm}_n,\qquad n^{2}+n^{2}=2n^{2}.
$$

The computation confirms the dimensions $4+4=8$ and $9+9=18$ at $n=2,3$, and it is the complex form of the same involution.

**The bracket relations of a symmetric pair hold.** In both cases

$$
[\mathfrak{k},\mathfrak{k}]\subset\mathfrak{k},\qquad [\mathfrak{k},\mathfrak{p}]\subset\mathfrak{p},\qquad [\mathfrak{p},\mathfrak{p}]\subset\mathfrak{k},
$$

for $\mathfrak{k}$ the compact part and $\mathfrak{p}$ the complement. The computation confirms the three inclusions at $n=3$ on random triples in both the real and the complex case, and it is the axiom which makes the quotient a symmetric space.

**The two involutions are the same map read over two fields.** The complex involution restricts to the real one on the real matrices,

$$
\theta\big|_{\mathfrak{gl}_n(\mathbb{R})}=\text{the negative transpose},
$$

since the conjugate transpose of a real matrix is its transpose. The computation confirms the restriction at $n=3$ on random real matrices, and it is the reason the two spaces are twins rather than analogues.

## The Real Space and Its Cone

**The real cone is open, convex and pointed.** The positive definite real symmetric matrices satisfy

$$
P>0\iff\operatorname{Spec}(P)\subset(0,\infty),\qquad (1-t)P+tQ>0,
$$

so the real cone has the same convex structure as the complex one. The computation confirms the convexity at $n=3$ on random real positive pairs and a grid of $t$, and it is the reason the real space is a cone and not merely a manifold.

**The exponential is a diffeomorphism of the real symmetric half onto the real cone.** For $S$ real symmetric the exponential is real symmetric positive definite, and conversely, so

$$
\exp:\operatorname{Sym}_n(\mathbb{R})\to\operatorname{PSD}_n(\mathbb{R})
$$

is a bijection with the logarithm as inverse. The computation confirms the two identities at $n=3$ on random real symmetric matrices, and it is the real analogue of the exponential chart of the complex cone.

**The trace metric restricts to the real cone.** The metric $g_P(S,T)=\operatorname{tr}(P^{-1}SP^{-1}T)$ is real on the real symmetric matrices, so the real cone is a totally geodesic submanifold with

$$
K_{\mathbb{R}}=-\tfrac14\|[S,T]\|^{2}\le0.
$$

The computation confirms the negativity at $n=2,3$ on random real planes, and it is the reason the real space has the same curvature formula as the complex one.

**The real cone is the fixed locus of the conjugation.** The conjugation $\sigma(X)=\bar X$ acts on the complex cone by

$$
\sigma(P)=P\iff P\ \text{is real},
$$

so the real cone is the fixed set of an isometric involution of the complex cone. The computation confirms the statement at $n=3$ by testing the fixed points of the conjugation, and it is the precise sense in which the real space sits inside its complex twin.

## The Complex Twin

**The complexification of the real space is the complex space.** Complexifying the Lie algebra and the complement,

$$
\mathfrak{gl}_n(\mathbb{R})\otimes\mathbb{C}=\mathfrak{gl}_n(\mathbb{C}),\qquad \operatorname{Sym}_n(\mathbb{R})\otimes\mathbb{C}=\operatorname{Herm}_n,
$$

so the complex twin is the complexification of the real one. The computation confirms the dimension identity $2\cdot\tfrac{n(n+1)}{2}=n^{2}+n$ against $n^{2}+n$ at $n=2,3,4$, and it is the reason the two spaces are called twins.

**The complex twin carries a complex structure.** The map $J:S\mapsto iS$ on the Hermitian half satisfies $J^{2}=-\mathrm{id}$ and is orthogonal for the trace metric at the identity, which was confirmed at $n=3$ on random Hermitian matrices. So the complex cone is a complex manifold while the real cone is not.

**The real space is a real form of the complex one.** The real cone is the fixed set of the conjugation and spans the complex cone over $\mathbb{C}$, so $\mathrm{PD}_n=\operatorname{PSD}_n(\mathbb{R})\otimes_{\mathbb{R}}\mathbb{C}$, which was confirmed at $n=2,3$ by writing a random Hermitian positive matrix as a complex combination of real ones.

**The curvature of the twin is the same formula.** In both cases

$$
K=-\tfrac14\|[X,Y]\|^{2}
$$

for orthonormal pairs, so the complex twin differs from the real space by the size of the complement, not by the shape of the curvature. The computation confirms the formula at $n=2$ in both cases with the value $-1/2$ on the traceless part, and it is the reason the two spaces are geometrically parallel.

## The Compact Duals

**The compact dual of the real space is the orthogonal group.** The compact part of the real decomposition is $\mathfrak{so}(n)$, of dimension $n(n-1)/2$, and it exponentiates to

$$
\mathrm{O}(n),\qquad \dim=\tfrac{n(n-1)}{2},\qquad \text{two components},
$$

the second reflection being the sign of the determinant. The computation confirms the dimension $1,3,6$ at $n=2,3,4$ and the two components by the signs of the determinants, and it is the compact twin of the real cone.

**The compact dual of the complex space is the unitary group.** The compact part of the complex decomposition is $\mathfrak{u}(n)$, of dimension $n^{2}$, and it exponentiates to

$$
\mathrm{U}(n),\qquad \dim=n^{2},\qquad \text{connected},
$$

which gives $4,9,16$ at $n=2,3,4$. The computation confirms the dimension and the connectedness by the determinant winding, and it is the compact twin of the complex cone.

**The compact duals are totally geodesic submanifolds of the groups.** The inclusions

$$
\mathrm{O}(n)\subset\mathrm{GL}_n(\mathbb{R}),\qquad \mathrm{U}(n)\subset\mathrm{GL}_n(\mathbb{C})
$$

are the fixed sets of the two involutions $g\mapsto(g^{\mathsf T})^{-1}$ and $g\mapsto(g^{*})^{-1}$, so each compact dual is the fixed locus of an involution of the group. The computation confirms the statement at $n=3$ on random orthogonal and unitary matrices, and it is the reason the compact dual is the symmetric space of the compact form.

## The Case $n=2$

**At $n=2$ the real space is a hyperbolic plane and the complex twin a hyperbolic three-space times a line.** The values are

$$
\dim\mathrm{GL}_2(\mathbb{R})/\mathrm{O}(2)=3,\qquad \dim\mathrm{GL}_2(\mathbb{C})/\mathrm{U}(2)=4,
$$

which were recomputed at $n=2$, with the curvature $-1/2$ on the traceless part in both cases, confirmed on eight random traceless planes of each space. So the real space is the hyperbolic plane of constant curvature and the complex twin is the product of a hyperbolic three-space with a line.

**The real space is the fixed set of the conjugation inside the complex one.** At $n=2$,

$$
\operatorname{PSD}_2(\mathbb{R})=\{P\in\mathrm{PD}_2:P=\bar P\},
$$

of real dimension three inside the four-dimensional cone. The computation confirms the statement at $n=2$ by testing the fixed points, and it is the smallest instance of the twin relation.

**The biquaternion algebra gives the two spaces at once.** The real symmetric matrices are the fixed points of the conjugation of the biquaternion algebra, and the Hermitian ones are the fixed points of the conjugate transpose, so

$$
\operatorname{Sym}_2(\mathbb{R})\subset\operatorname{Herm}_2,\qquad \dim 3\ \text{against}\ 4,
$$

which was confirmed at $n=2$. So the coda of the corpus carries both spaces in one algebra, and the twin relation is visible in the two real forms of the same complex algebra.

## Summary

The quotient $\mathrm{GL}_n(\mathbb{R})/\mathrm{O}(n)$ is the cone of the positive definite real symmetric matrices of dimension $n(n+1)/2$, and its complex twin $\mathrm{GL}_n(\mathbb{C})/\mathrm{U}(n)$ is the cone of the positive definite Hermitian matrices of dimension $n^{2}$; the two Cartan decompositions $\mathfrak{gl}_n(\mathbb{R})=\mathfrak{so}(n)\oplus\operatorname{Sym}_n(\mathbb{R})$ and $\mathfrak{gl}_n(\mathbb{C})=\mathfrak{u}(n)\oplus\operatorname{Herm}_n$ are the two restrictions of the single involution $X\mapsto-X^{*}$, and both satisfy the bracket relations $[\mathfrak{k},\mathfrak{k}]\subset\mathfrak{k}$, $[\mathfrak{k},\mathfrak{p}]\subset\mathfrak{p}$, $[\mathfrak{p},\mathfrak{p}]\subset\mathfrak{k}$. Both spaces have rank $n$, both carry the trace metric with the curvature $-\tfrac14\|[X,Y]\|^{2}$, and both are exponential images of their complements; the real space is the fixed locus of the conjugation inside the complex one and the complex one is its complexification. The compact duals are the orthogonal group of dimension $n(n-1)/2$ with two components and the unitary group of dimension $n^{2}$, which is connected.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{GL}_n(\mathbb{R})/\mathrm{O}(n)\cong\operatorname{PSD}_n(\mathbb{R})$ | the real space, dimension $n(n+1)/2$ |
| $\mathrm{GL}_n(\mathbb{C})/\mathrm{U}(n)\cong\mathrm{PD}_n$ | the complex twin, dimension $n^{2}$ |
| $\theta(X)=-X^{\mathsf T}$ | the involution of the real case |
| $\theta(X)=-X^{*}$ | the involution of the complex case |
| $\mathfrak{k}\oplus\mathfrak{p}$ | the Cartan decomposition |
| $[\mathfrak{p},\mathfrak{p}]\subset\mathfrak{k}$ | the bracket relation of a symmetric pair |
| $\operatorname{rank}=n$ | the common rank of the two spaces |
| $K=-\tfrac14\|[X,Y]\|^{2}$ | the common curvature formula |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for the symmetric spaces and their duality.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, 2002), for the Cartan decompositions and the real forms.
- Rajendra Bhatia, *Positive Definite Matrices* (Princeton, 2007), for the real and the complex cones.
- [The Geometry of the Two Halves, and the Return of the Two-Sided Operators](the-geometry-of-the-two-halves-and-the-return-of-the-two-sided-operators.html), for the trace metric and the curvature.
- [The Two Base Fields: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$](the-two-base-fields-mnr-inside-mnc.html), for the real matrices inside the complex ones.
- [The Cartan Decomposition of $\mathrm{GL}_n(\mathbb{C})$](the-cartan-decomposition-of-glnc.html), for the decomposition of the group.
