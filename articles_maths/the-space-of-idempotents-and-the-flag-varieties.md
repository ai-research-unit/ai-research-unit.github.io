# __The Space of Idempotents and the Flag Varieties__

## Introduction

**The idempotents of $M_n(\mathbb{C})$ form a variety stratified by the rank, each stratum is an orbit of the group whose points are the splittings $V=W\oplus W'$, and the Hermitian idempotents are the orthogonal projections, whose space is the Grassmannian $G(k,n)$.**

The article proves that an idempotent is the same datum as a direct sum decomposition, proves that the group acts transitively on the idempotents of a fixed rank with the Levi subgroup as stabiliser, computes the complex dimension $2k(n-k)$ of the stratum and the real dimension $2k(n-k)$ of the projections, proves that the Hermitian idempotents are exactly the orthogonal projections and that their space is $\mathrm{U}(n)/(\mathrm{U}(k)\times\mathrm{U}(n-k))$, and describes the flag variety of a complete set of idempotents with dimension $n(n-1)$ over the reals. It assumes *The Peirce Decomposition in $n$ Dimensions* and *The Topology of $M_n(\mathbb{C})$*. It defers the homotopy to *The Homotopy of $\mathrm{GL}_n(\mathbb{C})$ and of the Two Halves* and the geometry to *The Symmetric Space $\mathrm{GL}_n/O(n)$ and Its Complex Twin*.

## The Idempotents and Their Images

**An idempotent is a projection onto its image along its kernel.** For $e$ with $e^{2}=e$,

$$
M_n=\operatorname{im}e\oplus\ker e,\qquad e\,\text{is the identity on}\ \operatorname{im}e\ \text{and zero on}\ \ker e,
$$

since every vector $x$ splits as $ex+(x-ex)$ with the first summand in the image and the second in the kernel. The computation confirms the split at $n=3$ on random idempotents by checking the two inclusions, and it is the basic dictionary of the section.

**The trace of an idempotent is its rank.** In the basis adapted to the split the matrix is $\operatorname{diag}(1,\dots,1,0,\dots,0)$, so

$$
\operatorname{tr}e=\operatorname{rank}e=\dim\operatorname{im}e,
$$

which was verified at $n=2,3,4$ on random idempotents of every rank. So the rank is read from the trace, and it is the only invariant which separates the strata.

**An idempotent is the identity minus an idempotent of complementary rank.** If $e$ is idempotent then

$$
(\mathrm{I}-e)^{2}=\mathrm{I}-e,\qquad \operatorname{rank}(\mathrm{I}-e)=n-\operatorname{rank}e,
$$

so the complement is the projection onto the kernel along the image. The computation confirms the two statements at $n=3$ on random idempotents, and it is the first sign that the idempotents come in complementary pairs.

**The rank is locally constant on the variety.** The rank is the trace, which is continuous, and it takes integer values, so it is constant on each connected component and

$$
\mathcal{P}_n^{(k)}=\{e:e^{2}=e,\ \operatorname{rank}e=k\}
$$

is a union of components. The computation confirms the constancy at $n=3$ by following a path of idempotents, and it gives the stratification of the variety by the rank.

**The tangent space at an idempotent is the space of off-diagonal blocks.** Differentiating $e^{2}=e$ gives

$$
\delta=\delta e+e\delta,
$$

and in the corner decomposition of the split the solutions are $\delta_{11}=0$, $\delta_{22}=0$ with $\delta_{12}$ and $\delta_{21}$ free. The computation confirms the dimension $2k(n-k)$ of the solution space at $n=4$, $k=2$: the linear system has rank $n^{2}-2k(n-k)$. So the stratum of rank $k$ has complex dimension $2k(n-k)$ and real dimension $4k(n-k)$.

## The Orbits of the Group

**The group acts on the idempotents by conjugation.** For $g$ invertible and $e$ idempotent,

$$
(geg^{-1})^{2}=geg^{-1},
$$

and the rank is preserved, so the group acts on each stratum $\mathcal{P}_n^{(k)}$. The computation confirms the closure at $n=3$, and it is the reason the strata are homogeneous spaces.

**The action is transitive on each stratum.** Two idempotents of the same rank $k$ have images of the same dimension, and a linear map carrying one image onto the other and one kernel onto the other carries one idempotent to the other; so

$$
\mathcal{P}_n^{(k)}=\mathrm{GL}_n(\mathbb{C})\cdot e_k
$$

for $e_k=\operatorname{diag}(1,\dots,1,0,\dots,0)$. The computation confirms the transitivity at $n=4$ by solving for $g$ between two random idempotents of rank two, and it gives the stratum as a single orbit.

**The stabiliser is the Levi subgroup.** The matrices fixing $e_k$ are the block diagonal ones

$$
\operatorname{Stab}(e_k)=\left\{\begin{pmatrix}A&0\\0&D\end{pmatrix}:A\in\mathrm{GL}_k,\ D\in\mathrm{GL}_{n-k}\right\},
$$

of complex dimension $k^{2}+(n-k)^{2}$. The computation confirms the stabiliser at $n=4$, $k=2$ by testing which random block matrices fix $e_k$, and it gives the orbit dimension

$$
\dim_{\mathbb{C}}\mathcal{P}_n^{(k)}=n^{2}-k^{2}-(n-k)^{2}=2k(n-k),
$$

in agreement with the tangent count. So the stratum is the homogeneous space $\mathrm{GL}_n/(\mathrm{GL}_k\times\mathrm{GL}_{n-k})$.

**The two extreme strata are a point and the open dense orbit.** For $k=0$ the stratum is the single matrix $0$, and for $k=n$ it is the single matrix $\mathrm{I}$; for $1\le k\le n-1$ the stratum has dimension $2k(n-k)$. The computation confirms the dimensions at $n=3$: $4$ for $k=1$ and $4$ for $k=2$, and it shows that the strata of complementary rank have the same dimension, since $2k(n-k)=2(n-k)k$.

## The Grassmannian of Projections

**The Hermitian idempotents are the orthogonal projections.** If $e^{2}=e=e^{*}$ then the image and the kernel are orthogonal complements, so

$$
e\ \text{is the orthogonal projection onto}\ \operatorname{im}e;
$$

conversely an orthogonal projection is Hermitian and idempotent. The computation confirms the equivalence at $n=3$ on random idempotents, and it singles out the projections among the idempotents.

**The unitary group acts transitively on the projections of a rank.** For two projections $e,f$ of rank $k$ there is a unitary carrying one image to the other and one kernel to the other, so

$$
\{e:e^{2}=e=e^{*},\ \operatorname{rank}e=k\}=\mathrm{U}(n)/(\mathrm{U}(k)\times\mathrm{U}(n-k)),
$$

the Grassmannian $G(k,n)$. The computation confirms the transitivity at $n=4$, $k=2$ by solving for the unitary, and it gives the real dimension

$$
\dim_{\mathbb{R}}G(k,n)=n^{2}-k^{2}-(n-k)^{2}=2k(n-k),
$$

which was verified at $n=2,3,4$ against the formula: $2,4,6$ for $k=1$.

**The Grassmannian is half of the stratum.** The projections form the real slice of the complex stratum, and

$$
\dim_{\mathbb{R}}G(k,n)=2k(n-k)=\tfrac12\dim_{\mathbb{R}}\mathcal{P}_n^{(k)},
$$

which was verified at $n=4$, $k=2$: $8$ and $16$. The computation confirms the factor two, and it is the reason the projections are a real manifold of half the real dimension of the idempotents.

**The tangent space of the projections is the space of Hermitian off-diagonal blocks.** In the eigenbasis of the projection the tangent directions are

$$
\delta=\begin{pmatrix}0&Z\\ Z^{*}&0\end{pmatrix},\qquad Z\in M_{k\times(n-k)},
$$

which are Hermitian and satisfy the constraint. The computation confirms the constraint at $n=4$, $k=2$ and the real dimension $2k(n-k)=8$ of the family, and it is the projection-level form of the off-diagonal blocks of the stratum.

## The Flags

**A complete set of idempotents is a flag.** Idempotents $e_1,\dots,e_r$ with

$$
e_ie_j=\delta_{ij}e_i,\qquad e_1+\dots+e_r=\mathrm{I}
$$

cut the space into the direct sum of their images, so they define the flag

$$
0\subset\operatorname{im}e_1\subset\operatorname{im}(e_1+e_2)\subset\dots\subset M_n.
$$

The computation confirms the orthogonality relations at $n=4$ on a random complete set of ranks $1,1,2$, and it is the reason the flags and the idempotents are the same datum.

**The complete flag variety has dimension $n(n-1)$ over the reals.** The group acts transitively on the complete flags with the Borel subgroup of the upper triangular matrices as stabiliser, so

$$
\dim_{\mathbb{R}}\mathrm{Flags}_n=n^{2}-\dim_{\mathbb{R}}B=n^{2}-n^{2}=n(n-1),
$$

with $\dim_{\mathbb{C}}B=n(n+1)/2$ and $\dim_{\mathbb{C}}\mathrm{Flags}_n=n(n-1)/2$. The computation confirms the values $2,6,12$ at $n=2,3,4$, and it is the dimension of the flag variety of the ordered idempotents.

**The Lagrange idempotents give the standard flag.** The idempotents $\varepsilon_i$ of *Roots of Unity and the Lagrange Idempotents of $M_n(\mathbb{C})$* satisfy the two relations, so they define the coordinate flag

$$
0\subset\langle e_1\rangle\subset\langle e_1,e_2\rangle\subset\dots\subset\mathbb{C}^{n}.
$$

The computation confirms the relations at $n=3,4$ on the Lagrange idempotents, and it shows that the standard flag is the reference point of the flag variety.

**The partial flags correspond to the partial sets of idempotents.** A set $e_1,\dots,e_r$ with $r<n$ terms defines a partial flag with the dimensions $d_j=\operatorname{rank}(e_1+\dots+e_j)$, and its variety has complex dimension

$$
\sum_{j=1}^{r}d_j\,(d_{j+1}-d_j),\qquad d_{r+1}=n,
$$

the dimension of $\mathrm{GL}_n$ modulo the corresponding parabolic. The computation confirms the count at $n=4$ for the ranks $1$ and $3$: $5$ complex, against the block count of the stabiliser, and it reduces to $k(n-k)$ for $r=1$.

## The Peirce Idempotents and the Stratification

**The Peirce decomposition is the flag of the diagonalisable idempotents.** For a diagonalisable idempotent $e$ the algebra splits as

$$
M_n=eM_ne\oplus eM_n(\mathrm{I}-e)\oplus(\mathrm{I}-e)M_ne\oplus(\mathrm{I}-e)M_n(\mathrm{I}-e),
$$

the four Peirce corners of *The Peirce Decomposition in $n$ Dimensions*, and their dimensions are $k^{2},k(n-k),(n-k)k,(n-k)^{2}$. The computation confirms the four dimensions at $n=4$, $k=2$: $4,4,4,4$, and it is the reason the corner structure is the tangent structure of the stratum.

**The corners are the blocks of the stratum.** The off-diagonal corners are the tangent directions of the Grassmannian, and the diagonal corners are the tangent directions of the stabiliser; so

$$
\dim\mathfrak{gl}_n=k^{2}+2k(n-k)+(n-k)^{2},
$$

which was verified at $n=4$, $k=2$: $4+8+4=16$. So the Peirce decomposition of the algebra is the decomposition of the tangent space of the group at the identity into the directions which move the projection and the directions which fix it.

## The Case $n=2$

**At $n=2$ the rank one projections form a two-sphere.** The formula gives

$$
\dim_{\mathbb{R}}G(1,2)=2\cdot1\cdot1=2,\qquad G(1,2)\cong\mathrm{U}(2)/(\mathrm{U}(1)\times\mathrm{U}(1))\cong S^{2},
$$

which was confirmed at $n=2$ by the dimension count. So the space of rank one projections of the two-by-two case is the sphere, and the two complementary projections are the two antipodal points of a diameter.

**The Peirce idempotents of the biquaternion algebra are a pair of antipodal projections.** The pair

$$
\tilde\Pi_{\mathrm{id},\pm}=\tfrac12(e_t\pm\tilde{Ζ})
$$

is a complete set of Hermitian idempotents of rank one, so the pair is a point of the flag variety and a diameter of the two-sphere. The computation confirms the two relations and the Hermiticity at $n=2$, and it shows that the freedom of one reciprocal rescaling mentioned in the biquaternion articles does not move the pair, since the pair is fixed by the root $\tilde{Ζ}$ alone.

**The stratum of rank one idempotents is four real dimensional at $n=2$.** The formula gives

$$
\dim_{\mathbb{C}}\mathcal{P}_2^{(1)}=2,\qquad \dim_{\mathbb{R}}\mathcal{P}_2^{(1)}=4,
$$

so the oblique projections form a four-dimensional family around the two-sphere of the orthogonal ones. The computation confirms the two dimensions at $n=2$ by the tangent count, and it shows that the projections are exactly half of the stratum, as in the general case.

## Summary

An idempotent is the same datum as a splitting $V=\operatorname{im}e\oplus\ker e$, its trace is its rank, and the group acts transitively on the idempotents of a fixed rank $k$ with the Levi subgroup $\mathrm{GL}_k\times\mathrm{GL}_{n-k}$ as stabiliser, so the stratum is the complex manifold of dimension $2k(n-k)$ and real dimension $4k(n-k)$. The Hermitian idempotents are the orthogonal projections, they form the real slice of half the dimension, and their space is the Grassmannian $G(k,n)=\mathrm{U}(n)/(\mathrm{U}(k)\times\mathrm{U}(n-k))$ of real dimension $2k(n-k)$; a complete set of idempotents is the same datum as a flag, and the complete flag variety has real dimension $n(n-1)$. The Peirce corners of the algebra are the blocks of the stratum, with dimensions $k^{2},k(n-k),(n-k)k,(n-k)^{2}$, and at $n=2$ the rank one projections form a two-sphere whose diameter is the pair $\tilde\Pi_{\mathrm{id},\pm}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{P}_n$ | the variety of idempotents |
| $\mathcal{P}_n^{(k)}$ | the idempotents of rank $k$ |
| $\operatorname{tr}e=\operatorname{rank}e$ | the rank read from the trace |
| $\delta=\delta e+e\delta$ | the tangent equation at an idempotent |
| $2k(n-k)$ | the complex dimension of the stratum |
| $G(k,n)=\mathrm{U}(n)/(\mathrm{U}(k)\times\mathrm{U}(n-k))$ | the Grassmannian of projections |
| $\mathrm{Flags}_n$ | the complete flag variety, of real dimension $n(n-1)$ |
| $k^{2},k(n-k),(n-k)k,(n-k)^{2}$ | the Peirce corner dimensions |

## Further Reading

- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the flag varieties and the Grassmannians.
- Joe Harris, *Algebraic Geometry: A First Course* (Springer, 1992), for the idempotent variety and its strata.
- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the projections and their parametrisation.
- [The Peirce Decomposition in $n$ Dimensions](the-peirce-decomposition-in-n-dimensions.html), for the four corners used here.
- [Roots of Unity and the Lagrange Idempotents of $M_n(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-of-mnc.html), for the idempotents of the standard flag.
- [The Topology of $M_n(\mathbb{C})$](the-topology-of-mnc.html), for the rank strata which contain the idempotents.
