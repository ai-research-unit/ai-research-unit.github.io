# __The Space of Idempotents and the Real Flag Varieties__

## Introduction

**An idempotent of rank $r$ is the same data as a subspace of dimension $r$, so the space of idempotents is a real Grassmannian, and a frame is the same data as a complete flag; this is where the algebra of the earlier articles becomes geometry.**

The article proves that the idempotents of rank $r$ form the homogeneous space $\mathrm{GL}_n(\mathbb{R})/P_r$ of dimension $r(n-r)$, identifies the complete frames with the complete flags, computes the dimension $n(n-1)/2$ of the flag variety and proves that it is connected, describes the $n!$ Schubert cells, and reads the Peirce decomposition as a coordinate statement about a flag. It assumes *The Peirce Basis and the Corners over $\mathbb{R}$* for frames and *The Ideals, the Centre and the Simplicity of $M_n(\mathbb{R})$* for the homogeneous space description. It defers the homotopy of these spaces to *The Homotopy of $\mathrm{GL}_n(\mathbb{R})$ and of $\mathrm{SO}(n)$*.

## Idempotents and Projections

**An idempotent is a matrix with $E^{2}=E$, and its image and kernel are complementary.** If $E^{2}=E$ then every vector $v$ splits as $Ev+(v-Ev)$, with $Ev\in\operatorname{im}E$ and $v-Ev\in\ker E$, so

$$
\mathbb{R}^{n}=\operatorname{im}E\oplus\ker E .
$$

Conversely, a direct sum decomposition $\mathbb{R}^{n}=U\oplus W$ determines exactly one idempotent with image $U$ and kernel $W$, namely the projection along $W$ onto $U$. So idempotents are the same data as ordered pairs of complementary subspaces.

**The rank of an idempotent is the dimension of its image.** $\operatorname{tr}E=\dim\operatorname{im}E$ because the trace is the sum of the eigenvalues and the eigenvalues of an idempotent are $0$ and $1$. So $\operatorname{rk}E=r$ says $\dim\operatorname{im}E=r$, and $\ker E$ has dimension $n-r$.

**The idempotent is a projection, not an orthogonal projection.** It is orthogonal exactly when $E^{\mathsf T}=E$, that is when the two summands are orthogonal. The general idempotent is an oblique projection, and this is the reason the space of idempotents is a Grassmannian of subspaces rather than of orthonormal frames.

## The Space of Idempotents of Fixed Rank

**Theorem.** The set $\mathcal{E}_r=\{E:E^{2}=E,\ \operatorname{rk}E=r\}$ is a smooth real manifold of dimension $2r(n-r)$, and the map $E\mapsto\operatorname{im}E$ is a fibre bundle over the Grassmannian $\mathrm{Gr}_r(\mathbb{R}^{n})$ whose fibre has dimension $r(n-r)$.

*Proof.* The map is onto, since every $r$-plane is the image of some projection. The fibre over a fixed $U$ is the set of idempotents with image exactly $U$, and such an idempotent is determined by its kernel, an $(n-r)$-plane $W$ with $\mathbb{R}^{n}=U\oplus W$. The complements to $U$ are the graphs of the linear maps $\mathbb{R}^{n}/U\to U$, that is an affine space of dimension $r(n-r)$. So the total dimension is $r(n-r)+r(n-r)=2r(n-r)$.

**The same count comes from the group.** $\mathrm{GL}_n(\mathbb{R})$ acts transitively on $\mathcal{E}_r$ by $E\mapsto SES^{-1}$, because conjugation preserves the idempotent identity and the rank. The stabiliser of $E_r=\operatorname{diag}(\mathrm{I}_r,0)$ is the **Levi subgroup**

$$
L_r=\left\{\begin{pmatrix}A&0\\ 0&D\end{pmatrix}:A\in\mathrm{GL}_r(\mathbb{R}),\ D\in\mathrm{GL}_{n-r}(\mathbb{R})\right\},
$$

of dimension $r^{2}+(n-r)^{2}$. Hence

$$
\dim\mathcal{E}_r=n^{2}-r^{2}-(n-r)^{2}=2r(n-r).
$$

**The stabiliser is the Levi and not the parabolic.** The parabolic $P_r$ of block upper triangular matrices has dimension $r^{2}+r(n-r)+(n-r)^{2}$ and stabilises the subspace $U$; the idempotent also remembers the kernel, so the stabiliser is the smaller group $L_r$. The difference $r(n-r)$ is exactly the dimension of the fibre, which is the space of complements to $U$.

**The dimension is verified by counting the tangent space.** Linearising $E^{2}=E$ at $E$ gives the equation $HE+EH=H$ for the tangent vector $H$. For $E=\operatorname{diag}(\mathrm{I}_r,0)$ the solution space has dimension $2r(n-r)$, measured as $2,4,4,6,8,6$ at $(n,r)=(2,1),(3,1),(3,2),(4,1),(4,2),(4,3)$.

**The orthogonal idempotents form the Grassmannian, of dimension $r(n-r)$.** Imposing $E^{\mathsf T}=E$ halves the dimension, because the kernel is then the orthogonal complement of the image and no extra data remains. So the inclusion $\mathrm{Gr}_r\subset\mathcal{E}_r$ has codimension $r(n-r)$, and at $n=2$ it is the inclusion of a circle in a surface.

**The dimensional check at small $n$.** At $n=2$ the rank-one idempotents form a surface of dimension $2$: a line and a complementary line, that is a circle's worth of lines and a circle's worth of kernels. At $n=3$ the rank-one idempotents form a manifold of dimension $4$ over the projective plane, and the rank-two idempotents another copy, exchanged by $E\mapsto\mathrm{I}-E$.

## Frames and Flags

**A frame is a complete set of orthogonal idempotents summing to $\mathrm{I}$.** $P_1,\dots,P_n$ with $P_kP_l=\delta_{kl}P_k$ and $\sum_kP_k=\mathrm{I}$. Each $P_k$ has rank $r_k\ge1$ in general, and $\sum_kr_k=n$.

**A frame with all ranks equal to one is the same data as a complete flag.** Given such a frame, put $V_k=\operatorname{im}(P_1+\cdots+P_k)$. Then

$$
0=V_0\subset V_1\subset V_2\subset\cdots\subset V_n=\mathbb{R}^{n},\qquad \dim V_k=k,
$$

a complete flag. Conversely a complete flag gives the frame with $P_k$ the projection onto $V_k$ along $V_{k-1}\oplus V_{k+1}\cap\cdots$; the construction is the one of the Peirce basis, where $P_k$ is the projection onto the $k$-th line along the sum of the others.

**Theorem.** The set $\mathcal{F}$ of complete flags is a smooth manifold of dimension $n(n-1)/2$, diffeomorphic to $\mathrm{GL}_n(\mathbb{R})/B$ with $B$ the upper triangular group.

*Proof.* $\mathrm{GL}_n(\mathbb{R})$ acts transitively on flags, since any basis can be sent to the standard one. The stabiliser of the standard flag is the group of upper triangular matrices, of dimension $n(n+1)/2$. Hence $\dim\mathcal{F}=n^{2}-n(n+1)/2=n(n-1)/2$.

**The dimension is the dimension of the strictly upper triangular part, and that is not an accident.** The flag variety is the orbit of the standard flag under the unipotent radical $N$ of $B$; $N$ acts simply transitively on the open cell, so the open Schubert cell is a copy of $\mathbb{R}^{n(n-1)/2}$.

**A general frame with ranks $r_1,\dots,r_n$ is a flag with a grading.** The data is a flag together with a decomposition of each successive quotient $V_k/V_{k-1}$ into a direct sum of the prescribed dimensions. The dimension of that space is $n(n-1)/2$ plus the dimensions of the graded pieces, and the Peirce decomposition is the coordinate form of this data.

## The Real Points Are Connected

**Theorem.** The real flag variety $\mathrm{GL}_n(\mathbb{R})/B$ is connected, and so is the real Grassmannian $\mathrm{Gr}_r(\mathbb{R}^{n})$ for every $r$.

*Proof.* A homogeneous space $G/H$ is connected when $H$ meets every connected component of $G$. The upper triangular group $B$ contains $\operatorname{diag}(-1,1,\dots,1)$, whose determinant is $-1$, so $B$ meets both components of $\mathrm{GL}_n(\mathbb{R})$. Hence the quotient is connected. For the Grassmannian, $-\mathrm{I}$ lies in the identity component of $\mathrm{GL}_n(\mathbb{R})$ when $n$ is even and in the other component when $n$ is odd, and it acts trivially on subspaces, so again the two components of the group have the same orbits.

**So the two components of $\mathrm{GL}_n(\mathbb{R})$ do not show up in the flag variety.** The sign of the determinant of a change of basis is irrelevant to the flag it produces, because replacing a basis vector by its negative changes the determinant and not the flag. The obstruction that cuts the group in two is invisible to the geometry of subspaces.

**What the components do obstruct is a basis adapted to the flag.** The space of *oriented* flags, that is flags with a chosen orientation of the ambient space and of each successive quotient, is a covering of the flag variety, and its group of deck transformations is the group of sign changes. The covering is trivial over each Schubert cell, so it does not create components of the flag variety itself.

**The complex flag variety is connected too, and of twice the real dimension.** Over $\mathbb{C}$ the group $\mathrm{GL}_n(\mathbb{C})$ is connected, so the quotient is connected and the dimension over $\mathbb{C}$ is $n(n-1)/2$, that is real dimension $n(n-1)$. The real flag variety is a real form of it, of half the real dimension, and the real phenomenon is the halving of the dimension, not a splitting into components.

**The Grassmannian is connected but not simply connected.** For $0<r<n$ the fundamental group of $\mathrm{Gr}_r(\mathbb{R}^{n})$ is $\mathbb{Z}/2$, generated by a loop that rotates an $r$-plane through a full turn and returns it with the opposite orientation. For $r=1$ this is the double cover $S^{n-1}\to\mathbb{RP}^{n-1}$, and for $r=n-1$ it is the same statement for hyperplanes.

## Schubert Cells

**The Schubert cell of a permutation is a copy of a coordinate space.** For $w\in S_n$ put

$$
\Omega_w=\{V_\bullet:\dim(V_p\cap F_q)=\#\{i\le p:w(i)\le q\}\ \text{for all}\ p,q\},
$$

where $F_q$ is the standard coordinate flag. Then $\Omega_w\cong\mathbb{R}^{\ell(w)}$, with $\ell(w)$ the number of inversions of $w$, and the cells partition the flag variety.

**The dimensions of the cells are the numbers $0,1,\dots,n(n-1)/2$.** The inversion count ranges from $0$ for the identity to $n(n-1)/2$ for the longest element, and every integer in between occurs. So the flag variety has a cell decomposition with one cell in each dimension from $0$ to $n(n-1)/2$, and the Euler characteristic is $n(n-1)/2+1$.

**At $n=3$ the six cells have dimensions $0,1,1,2,2,3$.** The identity gives a point, the two adjacent transpositions give two lines, the two $3$-cycles give two planes, and the longest element gives an open cell of dimension $3$. The Euler characteristic is $6$, which is also the number of permutations.

**The cells are the same as the Bruhat decomposition of the group.** $\mathrm{GL}_n(\mathbb{R})=\bigsqcup_w BwB$, and the cell $\Omega_w$ is the image of $BwB$; the dimension of $BwB$ is $n(n+1)/2+\ell(w)$, and subtracting the dimension of $B$ gives $\ell(w)$. So the Schubert cells and the Bruhat cells are the same objects seen from the group and from the flag variety.

## The Peirce Decomposition as Flag Coordinates

**The Peirce decomposition is what a frame does to the algebra, and the flag is the frame read as geometry.** With $P_k$ the projection onto $V_k$ along the complementary flag, the corner $A_{kl}=P_kM_nP_l$ consists of the maps that send $V_l$ into $V_k$ and kill the other summands. So the corner is $\operatorname{Hom}(V_l,V_k)$ composed with the projections, of dimension $r_kr_l$.

**The multiplication rule is the composition of maps.** $A_{kl}A_{lm}$ is a map $V_m\to V_l\to V_k$, hence lies in $A_{km}$, and $A_{kl}A_{mn}=0$ for $l\ne m$ because the intermediate map must land in $V_l$ and start in $V_m$ with $l\ne m$. The abstract rule $A_{kl}A_{lm}\subseteq A_{km}$ is therefore the composition of homomorphisms between the lines of a flag.

**The diagonal corners are the endomorphism algebras of the lines.** $A_{kk}=\operatorname{End}(V_k)\cong M_{r_k}(\mathbb{R})$, and the block diagonal subalgebra $\bigoplus_kA_{kk}$ is the Levi factor of the parabolic stabilising the flag. The off-diagonal corners are the nilpotent directions.

**So the whole of the Peirce theory is the geometry of a flag.** The abstract algebra statements of *The Peirce Decomposition in $n$ Dimensions over $\mathbb{R}$* are the coordinate form of the incidence geometry of subspaces, and the two languages can be translated at will. This is why the rank vector $(r_1,\dots,r_n)$ has a geometric meaning: it is the sequence of dimensions of the successive quotients of the flag.

## Summary

Idempotents of rank $r$ are the projections onto $r$-planes, and they form a smooth manifold $\mathcal{E}_r\cong\mathrm{GL}_n(\mathbb{R})/P_r$ of dimension $r(n-r)$, diffeomorphic to the real Grassmannian. Complete frames of rank-one idempotents are complete flags, and the flag variety is $\mathrm{GL}_n(\mathbb{R})/B$ of dimension $n(n-1)/2$. The flag variety and the Grassmannian are connected over $\mathbb{R}$ and over $\mathbb{C}$. The Schubert cells are copies of $\mathbb{R}^{\ell(w)}$, one for each permutation, and the Peirce decomposition is the coordinate form of the flag: $A_{kl}=\operatorname{Hom}(V_l,V_k)$ and the multiplication rule is composition.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{E}_r$ | the idempotents of rank $r$, of dimension $r(n-r)$ |
| $\mathrm{Gr}_r(\mathbb{R}^{n})$ | the Grassmannian of $r$-planes, of dimension $r(n-r)$ |
| $\mathcal{F}$ | the complete flags, of dimension $n(n-1)/2$ |
| $P_r$, $B$, $N$ | the parabolic, the upper triangular group, its unipotent radical |
| $\Omega_w$ | the Schubert cell of the permutation $w$, of dimension $\ell(w)$ |
| $\ell(w)$ | the number of inversions of $w$ |

## Further Reading

- William Fulton, *Young Tableaux* (Cambridge, 1997), for the flag variety, the Schubert cells and the Bruhat decomposition.
- Armand Borel, *Linear Algebraic Groups* (Springer, 1991), for the homogeneous space description of flags and Grassmannians.
- [The Peirce Basis and the Corners over $\mathbb{R}$](the-peirce-basis-and-the-corners-over-r.html), for the frame and its corners.
- [The Geometry of the Idempotents of $M_3(\mathbb{C})$](the-geometry-of-the-idempotents-of-m3c.html), for the complex case at $n=3$.
- [The Ideals, the Centre and the Simplicity of $M_n(\mathbb{R})$](the-ideals-the-centre-and-the-simplicity-of-mnr.html), for the parabolic subgroups.
