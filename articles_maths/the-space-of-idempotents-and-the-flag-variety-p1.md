# __The Space of Idempotents and the Flag Variety $\mathbb{P}^1$__

## Introduction

**The idempotents of $M_2(\mathbb{C})$ are the two trivial ones and the rank-one ones, and a rank-one idempotent is exactly a pair of complementary lines, one for the image and one for the kernel, so the space of rank-one idempotents is the complement of the incidence divisor in $\mathbb{P}^{1}\times\mathbb{P}^{1}$, a complex surface fibred over the flag variety $\mathbb{P}^{1}$.**

The article classifies the idempotents, proves the correspondence between rank-one idempotents and pairs of complementary lines, identifies the flag variety and the minimal left ideals with $\mathbb{P}^{1}$, describes the surface as a bundle over $\mathbb{P}^{1}$, and shows that the Hermitian idempotents form the sphere $S^{2}$. It assumes *The Space of Idempotents and the Peirce Decomposition*, *The Minimal Left Ideals of the Biquaternion Algebra* and *The Spectral Theorem: the Hermitian Case and the Sphere of Idempotents*.

It follows the biquaternion article *The Square Roots of One and the Idempotents of the Biquaternion Algebra* for the same classification in the biquaternion coordinates.

## The Idempotents

**A matrix is an idempotent exactly when it acts as the identity on its image and as zero on a complement.**

**Proposition.** An idempotent $P$ satisfies $P|_{\operatorname{im}P}=\mathrm{id}$ and $\ker P$ is a complement of $\operatorname{im}P$, and conversely a projection onto a subspace along a complement is an idempotent.

**Proof.** From $P^{2}=P$ the image is fixed pointwise, and for a vector $v$ the difference $v-Pv$ lies in the kernel, so the space is the sum of the image and the kernel, whose intersection is zero.

**Corollary.** The idempotents of $M_2(\mathbb{C})$ are the zero matrix, the identity, and the projections of rank one.

**Proof.** The two ranks are zero, two and one, and the projections of rank zero and two are the trivial ones.

**Corollary.** Two idempotents of the same rank are conjugate exactly when their pairs of image and kernel can be matched, so the conjugation classes are the three ranks.

**Proof.** Conjugation carries the image onto the image and the kernel onto the kernel, and any two pairs of complementary lines can be matched by an invertible matrix.

## Rank-One Idempotents and Pairs of Lines

**Theorem.** The rank-one idempotents are exactly the matrices $uv^{\mathsf T}/(v^{\mathsf T}u)$ with $u$ and $v$ nonzero and $v^{\mathsf T}u$ nonzero, and they are in bijection with the pairs $(L,K)$ of a line and a hyperplane with $L$ not contained in $K$.**

**Proof.** A rank-one idempotent is $uv^{\mathsf T}$ with $v^{\mathsf T}u=1$, its image is the line spanned by $u$, and its kernel is the hyperplane $v^{\perp}$, which does not contain $u$; conversely a line $L$ and a hyperplane $K$ with $L$ not contained in $K$ define the projection onto $L$ along $K$, which is a rank-one idempotent.

**Corollary.** The scale of the two vectors is free, so the same idempotent is described by any nonzero multiple of $u$ and the reciprocal multiple of $v$.

**Proof.** The product $uv^{\mathsf T}$ is unchanged when $u$ is multiplied by a nonzero scalar and $v$ by its inverse.

**Corollary.** The trace of a rank-one idempotent is one, its determinant is zero, and its spectrum is $1,0$.

**Proof.** The trace of $uv^{\mathsf T}$ with $v^{\mathsf T}u=1$ is one, and the eigenvalue along the image is one.

## The Flag Variety

**Proposition.** The complete flags of the plane are the pairs (line, plane), and for the plane the plane is the whole space, so the flag variety is the projective line $\mathbb{P}^{1}$.

**Proof.** A complete flag has dimensions zero, one and two; the only free choice is the line, and the set of lines is $\mathbb{P}^{1}$.

**Corollary.** The projective line also parametrises the hyperplanes, the minimal left ideals and the minimal right ideals, since each of these is determined by a line.

**Proof.** In the plane a hyperplane is a line, and the minimal left ideals are the sets of matrices with columns in a fixed line.

**Corollary.** The rank-one idempotents project onto the flag variety by the image, and the fibre over a line is the set of hyperplanes not containing it, a complex line.

**Proof.** Fixing the image leaves the kernel free among the hyperplanes not containing the image, and that set is $\mathbb{P}^{1}$ minus a point.

## The Bundle over the Flag Variety

**Proposition.** The space of rank-one idempotents is the complement of the incidence divisor in $\mathbb{P}^{1}\times\mathbb{P}^{1}$, and it is a complex surface fibred over $\mathbb{P}^{1}$ with fibre a complex line.

**Proof.** The product $\mathbb{P}^{1}\times\mathbb{P}^{1}$ parametrises the pairs of a line and a hyperplane, and the incidence set, where the line lies in the hyperplane, is a copy of $\mathbb{P}^{1}$; the complement is the set of complementary pairs, and the projection to the first factor has the stated fibre.

**Corollary.** The surface is connected, and it is not compact, because the fibre is a line with one point removed from the projective line.

**Proof.** The base is connected and the fibres are connected, and each fibre is missing a point.

**Corollary.** The closure of the surface in the projective compactification is the quadric surface of decomposable elements, and the incidence divisor is the boundary at infinity.

**Proof.** The closure adds the pairs where the line lies in the hyperplane, which is the incidence set.

## The Hermitian Idempotents

**Proposition.** The Hermitian idempotents are exactly the matrices $\tfrac12(I+\vec n\cdot\vec\sigma)$ with $\vec n$ a unit vector, so they form a two-sphere.

**Proof.** This is *The Spectral Theorem: the Hermitian Case and the Sphere of Idempotents*: a Hermitian idempotent has the eigenvalues one and zero, and the spectral theorem writes it as the average of the identity and a traceless Hermitian matrix of norm one.

**Corollary.** The map from the sphere to the space of idempotents is injective, and its image is a real two-dimensional submanifold.

**Proof.** A unit vector is recovered from the idempotent by the formula $\vec n\cdot\vec\sigma=2P-I$, and the sphere has real dimension two.

**Corollary.** The antipodal points of the sphere correspond to the two idempotents with the same image and the two opposite kernels, which are orthogonal.

**Proof.** Changing the sign of the normal vector exchanges the eigenvalue one with the eigenvalue zero.

## The Two Families of Projections

**Proposition.** The rank-one idempotents split into the Hermitian ones and the non-Hermitian ones, and the non-Hermitian ones have an image and a kernel that are not orthogonal.

**Proof.** A projection is Hermitian exactly when its kernel is the orthogonal complement of its image, and the Hermitian ones are the sphere of the previous section.

**Corollary.** The sphere sits inside the surface as the set of pairs of complementary orthogonal lines, which is a real circle's worth of pairs over each line.

**Proof.** For a fixed line the orthogonal complement is a single line, so the orthogonality condition removes one real dimension from the fibre.

**Corollary.** The two trivial idempotents are Hermitian and lie outside the surface, since their rank is not one.

**Proof.** The zero matrix and the identity have ranks zero and two, and they are Hermitian.

## Summary

The idempotents of the matrix algebra are the zero matrix, the identity, and the rank-one projections. A rank-one projection is a pair of complementary lines, so the space of rank-one idempotents is the complement of the incidence divisor in $\mathbb{P}^{1}\times\mathbb{P}^{1}$, a complex surface fibred over the flag variety $\mathbb{P}^{1}$ with fibre a complex line.

The Hermitian idempotents are the projections onto a line along its orthogonal complement, and they form the two-sphere. The closure of the surface is the quadric of decomposable elements, and the incidence divisor is its boundary.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P^{2}=P$ | the idempotent condition |
| $uv^{\mathsf T}/(v^{\mathsf T}u)$ | the general rank-one idempotent |
| $\mathbb{P}^{1}$ | the flag variety, the set of lines |
| $\mathbb{P}^{1}\times\mathbb{P}^{1}$ | the pairs of line and hyperplane |
| $\tfrac12(I+\vec n\cdot\vec\sigma)$ | the Hermitian idempotent of normal $\vec n$ |

## Further Reading

- William Fulton, *Young Tableaux* (Cambridge University Press, 1997), for flag varieties at small rank.
- Igor R. Shafarevich, *Basic Algebraic Geometry* (Springer, 2013), for incidence divisors and quadric surfaces.
- [The Spectral Theorem: the Hermitian Case and the Sphere of Idempotents](the-spectral-theorem-the-hermitian-case-and-the-sphere-of-idempotents.html), for the Hermitian idempotents.
- [The Minimal Left Ideals of the Biquaternion Algebra](the-minimal-left-ideals-of-the-biquaternion-algebra.html), for the ideals parametrised by the lines.
- [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), for the quadric surface that closes the space of idempotents.
