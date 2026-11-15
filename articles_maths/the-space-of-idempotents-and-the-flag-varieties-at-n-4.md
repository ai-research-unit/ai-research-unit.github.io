# __The Space of Idempotents and the Flag Varieties at $n=4$__

## Introduction

**The idempotents of rank $k$ in $M_4(\mathbb{C})$ form the homogeneous space of decompositions $\mathbb{C}^{4}=V\oplus W$ of complex dimension $2k(4-k)$, their images sweep the Grassmannian $\mathrm{Gr}_k(\mathbb{C}^{4})$ of dimension $k(4-k)$, so the four Grassmannians are $\mathbb{P}^{3}$, $\mathrm{Gr}_2$ of dimension $4$, $\mathbb{P}^{3}$ again and two points, the full flag has dimension $6$, the Hermitian idempotents give the Grassmannians themselves through $U(4)$, and $\mathrm{Gr}_2$ sits in $\mathbb{P}^{5}$ as the Klein quadric.**

The article parametrises the idempotents of each rank by their kernel, proves that the parametrisation is an isomorphism onto the Grassmannian, computes the four dimensions, describes the full flag and the Borel, identifies the Hermitian idempotents with the same Grassmannians through the unitary group, reads the two Peirce idempotents as a complementary pair of points of $\mathrm{Gr}_2$, and exhibits the Plücker relation of $\mathrm{Gr}_2$ as the Klein quadric, whose defining equation is the Pfaffian expression of the antisymmetric article.

It assumes *The Ideals, the Centre and the Simplicity of $M_4(\mathbb{C})$*, *The Peirce Decomposition of $\operatorname{Sym}_4$ as a Jordan Algebra* and *The Triangular Decomposition $\mathfrak{h}\oplus\mathfrak{n}_+\oplus\mathfrak{n}_-$. The model at order two is *The Space of Idempotents and the Flag Variety $\mathbb{P}^{1}$*.

## The Idempotents of Rank $k$

**Definition.** An **idempotent** is $E$ with $E^{2}=E$, and its **rank** is the dimension of its image.

**Proposition.** For an idempotent $E$ of rank $k$, $\mathbb{C}^{4}=\operatorname{im}E\oplus\ker E$ with $\dim\operatorname{im}E=k$ and $\dim\ker E=4-k$, and $E$ is the projection onto the first summand along the second.

**Proof.** $E$ fixes its image and kills its kernel; every vector is $Ev+(v-Ev)$ with the first term in the image and the second in the kernel.

**Corollary.** The idempotents of rank $k$ are parametrised by the pairs (a $k$-plane, a complementary $(4-k)$-plane), and two pairs give the same idempotent exactly when they give the same decomposition.

**Proof.** The projection determines and is determined by its image and kernel.

**Corollary.** $\operatorname{tr}E=k$ and $\det E=0$ for $0<k<4$, so the trace of an idempotent is its rank.

**Proof.** The trace is the sum of the eigenvalues, which are $1$ with multiplicity $k$ and $0$ with multiplicity $4-k$.

**The nilpotent part.** $E-\tfrac12\mathrm I_4$ has square $\tfrac14\mathrm I_4$ and eigenvalues $\pm\tfrac12$, so an idempotent is a reflection up to an affine change.

**Proof.** $(E-\tfrac12\mathrm I)^{2}=E-\tfrac12\mathrm I+\tfrac14\mathrm I$? Compute: $E^{2}-E+\tfrac14\mathrm I=\tfrac14\mathrm I$ using $E^{2}=E$.

## The Four Grassmannians

**Theorem.** The idempotents of rank $k$ are in bijection with the ordered decompositions $\mathbb{C}^{4}=V\oplus W$ with $\dim V=k$; they form the homogeneous space $\mathrm{GL}_4/P_{k,4-k}$ of complex dimension $2k(4-k)$, where $P_{k,4-k}$ is the parabolic stabilising a fixed decomposition.

**Proof.** The idempotent determines the pair (image, kernel) and is determined by it; the group acts transitively on decompositions of a fixed type, and the stabiliser has dimension $k^{2}+(4-k)^{2}$, so the orbit has dimension $16-k^{2}-(4-k)^{2}=2k(4-k)$.

**Corollary.** The map from the idempotents of rank $k$ to the Grassmannian $\mathrm{Gr}_k(\mathbb{C}^{4})$, sending the idempotent to its image, is a fibre bundle with affine fibres of dimension $k(4-k)$.

**Proof.** For a fixed image $V$ the projections onto $V$ are parametrised by the complementary subspaces, which form the affine space $\operatorname{Hom}(\mathbb{C}^{4}/V,V)$ of dimension $k(4-k)$; and $k(4-k)+k(4-k)=2k(4-k)$.

**Corollary.** The dimensions over $\mathbb{C}$ are
$$
\dim\mathrm{Gr}_1=3,\quad \dim\mathrm{Gr}_2=4,\quad \dim\mathrm{Gr}_3=3,\quad \dim\mathrm{Gr}_0=\dim\mathrm{Gr}_4=0 ,
$$
while the idempotents themselves have dimensions $6$, $8$, $6$ and $0$.

**Proof.** $\dim\mathrm{Gr}_k=k(4-k)$ and $\dim$ of the idempotent space is $2k(4-k)$.

**Corollary.** The real dimensions of the Grassmannians are twice the complex ones, namely $6$, $8$, $6$ and $0$.

**Proof.** The complex dimension counts each complex parameter twice.

**Corollary.** The first and the last Grassmannians are projective three-spaces, $\mathbb{P}^{3}=\mathrm{Gr}_1=\mathrm{Gr}_3$, and the middle one is the quadric Grassmannian of four complex dimensions.

**Proof.** $k=1$ is the space of lines and $k=3$ the space of hyperplanes, which are dual projective spaces of dimension three.

**The homogeneous description.** $\mathrm{Gr}_k=\mathrm{GL}_4/Q_k$, where $Q_k$ is the parabolic subgroup stabilising a fixed $k$-plane.

**Proof.** The general linear group acts transitively on $k$-planes, and the stabiliser is the parabolic.

**Corollary.** $\dim Q_k=16-k(4-k)$, so $\dim Q_1=13$, $\dim Q_2=12$ and $\dim Q_3=13$, and the parabolic of the decomposition is smaller than the parabolic of the plane.

**Proof.** The orbit-stabiliser theorem with $\dim\mathrm{GL}_4=16$, and $k^{2}+(4-k)^{2}>k(4-k)$.

## The Full Flag

**Definition.** A **full flag** in $\mathbb{C}^{4}$ is a chain $0\subset V_1\subset V_2\subset V_3\subset\mathbb{C}^{4}$ with $\dim V_k=k$.

**Proposition.** The full flags form the homogeneous space $\mathrm{GL}_4/B$, where $B$ is the Borel subgroup of upper triangular matrices, of complex dimension $6$.

**Proof.** The general linear group acts transitively, the stabiliser of the standard flag is the group of upper triangular matrices, and $16-10=6$.

**Corollary.** The dimension is also $1+2+3=6$, the sum of the dimensions of the three steps.

**Proof.** The flag is the choice of a line in $\mathbb{C}^{4}$, a line in the quotient, and a line in the next quotient.

**Corollary.** The Borel has dimension $10$, equal to $4+6$, the diagonal and the strictly upper part.

**Proof.** The triangular decomposition of the algebra.

**The partial flags.** The flags of type $(k)$ are the Grassmannians, and the flags of type $(1,2)$ or $(2,3)$ have dimension $3+2=5$; the full flag is the finest.

**Proof.** The dimensions of the successive choices.

**Corollary.** The incidence relations between the Grassmannians are the projections of the partial flag varieties onto their factors.

**Proof.** A flag of type $(1,2)$ is a pair (a line, a plane containing it).

## The Hermitian Idempotents

**Theorem.** The Hermitian idempotents of rank $k$ are the orthogonal projections onto $k$-planes, and they form the homogeneous space $U(4)/(U(k)\times U(4-k))$, which is again $\mathrm{Gr}_k(\mathbb{C}^{4})$.

**Proof.** A Hermitian idempotent is an orthogonal projection, determined by its image; the unitary group acts transitively on $k$-planes and the stabiliser of one is the product of the two unitary groups of the plane and its complement.

**Corollary.** The real dimension of the space of Hermitian idempotents of rank $k$ is $2k(4-k)$, so $6$, $8$ and $6$ for $k=1,2,3$.

**Proof.** The complex dimension of the Grassmannian is $k(4-k)$, doubled.

**Corollary.** The Hermitian idempotents form a submanifold of $\operatorname{Herm}_4$ of real dimension $2k(4-k)$, and they are characterised by the two equations $E^{2}=E$ and $E^{\ast}=E$.

**Proof.** The two conditions, and the dimension count inside the sixteen-dimensional Hermitian space.

**The Peirce pair.** The two idempotents $E$ and $\mathrm I_4-E$ are two points of the Grassmannian, one for the image and one for the kernel, and the Peirce decomposition is the pair read together with the two mixed blocks.

**Proof.** The Peirce spaces are the four combinations of the two projections.

**Corollary.** A Peirce decomposition of $M_4$ is a pair of complementary points of $\mathrm{Gr}_k$ together with the identification of the mixed blocks, which is the off-diagonal part of the flag.

**Proof.** The two projectors cut the algebra into four blocks, and the off-diagonal ones are the spaces $\operatorname{Hom}$ between the two parts.

## The Plücker Embedding and the Klein Quadric

**Theorem.** The Plücker map embeds $\mathrm{Gr}_2(\mathbb{C}^{4})$ into $\mathbb{P}(\Lambda^{2}\mathbb{C}^{4})=\mathbb{P}^{5}$ by the six minors of the $2\times4$ matrix of a basis, and the image is the quadric
$$
p_{12}p_{34}-p_{13}p_{24}+p_{14}p_{23}=0 .
$$

**Proof.** The six minors are the coordinates of the decomposable bivector of the plane; a bivector is decomposable exactly when its wedge with itself vanishes, which in four dimensions is the single relation displayed.

**Corollary.** The relation is the Plücker relation, and its left side is the Pfaffian expression of the antisymmetric article applied to the matrix of the six coordinates.

**Proof.** The three terms are the three pairings of the four indices into two pairs.

**Corollary.** The Klein quadric is of dimension four in $\mathbb{P}^{5}$, in agreement with $\dim\mathrm{Gr}_2=4$, and it is the image of the Grassmannian under an embedding.

**Proof.** A nondegenerate quadric hypersurface in $\mathbb{P}^{5}$ has dimension four.

**Corollary.** The two families of planes on the Klein quadric are the two rulings of the Grassmannian, one by the planes through a fixed line and one by the planes inside a fixed hyperplane.

**Proof.** The classical two rulings of a quadric fourfold in $\mathbb{P}^{5}$.

**The other Grassmannians.** $\mathrm{Gr}_1=\mathbb{P}^{3}$ sits in $\mathbb{P}^{3}$ trivially and $\mathrm{Gr}_3$ likewise, so the only nontrivial Plücker embedding at order four is the middle one.

**Proof.** The first and the last are already projective spaces.

## Summary

The idempotents of rank $k$ are the projections onto $k$-planes and form the Grassmannian $\mathrm{Gr}_k(\mathbb{C}^{4})=\mathrm{GL}_4/P_k$, of complex dimension $k(4-k)$: three for $k=1$ and $k=3$, four for $k=2$, and a point for $k=0$ and $k=4$. The full flag has complex dimension six and is $\mathrm{GL}_4/B$.

The Hermitian idempotents are the orthogonal projections onto $k$-planes and form the same Grassmannians through $U(4)$, of real dimension $2k(4-k)$ inside $\operatorname{Herm}_4$. The two Peirce idempotents are a complementary pair of points, and the Peirce decomposition is that pair together with the mixed blocks.

$\mathrm{Gr}_2$ embeds in $\mathbb{P}^{5}$ as the Klein quadric, whose single equation is the Plücker relation, the same expression as the Pfaffian of an antisymmetric matrix. The two rulings of the quadric are the two families of planes through a line and inside a hyperplane.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Gr}_k(\mathbb{C}^{4})$ | the Grassmannian of $k$-planes |
| $k(4-k)$ | its complex dimension |
| $\mathrm{GL}_4/P_k$ | the homogeneous description |
| $\mathrm{GL}_4/B$ | the full flag, dimension $6$ |
| $U(4)/(U(k)\times U(4-k))$ | the Hermitian idempotents |
| Klein quadric | the Plücker image of $\mathrm{Gr}_2$ in $\mathbb{P}^{5}$ |

## Further Reading

- Joe Harris, *Algebraic Geometry: A First Course* (Springer, 1992), for Grassmannians, Plücker embeddings and quadrics.
- [The Triangular Decomposition $\mathfrak{h}\oplus\mathfrak{n}_+\oplus\mathfrak{n}_-$ of $M_4(\mathbb{C})$](the-triangular-decomposition-h-n-plus-n-minus-of-m4c.html), for the Borel and the flag it stabilises.
- [The Peirce Decomposition of $\operatorname{Sym}_4$ as a Jordan Algebra](the-peirce-decomposition-of-sym-4-as-a-jordan-algebra.html), for the Peirce spaces at a Hermitian idempotent.
- [The Spectral Theorem: the Hermitian Case at $n=4$](the-spectral-theorem-the-hermitian-case-at-n-4.html), for the orthogonal projections.
- [The Space of Idempotents and the Flag Variety $\mathbb{P}^{1}$](the-space-of-idempotents-and-the-flag-variety-p1.html), for the case at order two.
