# __The Intersection Table at $n=4$: Where Each Carrier Meets $\operatorname{Sym}$ and $\Lambda$__

## Introduction

**The subject.** The carriers are cut by the Casimir and the halves by the transpose, and the two cuts do not agree. The intersection of each carrier with each half is nevertheless a well-defined subspace, and its dimension can be computed: the table has the entries $4,3$; $3,2$; $2,1$; $1,0$ in complex dimensions.

**The order of the article.** The first section states the table and its real dimensions. The second explains the computation, which uses the projectors of the Casimir and the ranks of their restrictions. The third lists witnesses in each cell. The fourth proves the two outer columns and the row sums. The fifth reads the table and draws the boundary with the parity rule.

**It assumes** *Neither Half Is Invariant* for the failure of the splitting and *The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$* for the carriers. The row at order two is *The Intersection Table: Where Each Carrier Meets $\operatorname{Sym}$ and $\Lambda$*.

**The result in one line.** $\dim_{\mathbb{C}}(V_k\cap\operatorname{Sym})=k+1$ and $\dim_{\mathbb{C}}(V_k\cap\Lambda)=k$ for $k=0,1,2,3$, so the real dimensions are $2k+2$ and $2k$.

**Boundaries.** The article computes dimensions and exhibits witnesses; it does not prove the regularity of the pattern $k+1,k$ in general, which is recorded as a numerical fact of the four rows. It does not treat the intersections with the Hermitian halves.

## The Table

**Theorem.** In complex dimensions,

| carrier | $\cap\operatorname{Sym}$ | $\cap\Lambda$ | total |
|---|---|---|---|
| $V_0$ | $1$ | $0$ | $1$ |
| $V_1$ | $2$ | $1$ | $3$ |
| $V_2$ | $3$ | $2$ | $5$ |
| $V_3$ | $4$ | $3$ | $7$ |
| total | $10$ | $6$ | $16$ |

*Proof.* The intersection $V_k\cap\operatorname{Sym}$ is the image of the restriction to $V_k$ of the projection $(X+X^{\mathsf T})/2$, and its dimension is the rank of that map; the same for $\Lambda$ with $(X-X^{\mathsf T})/2$. Applying the two projections to a basis of each carrier and computing the ranks gives the table. The column totals are the dimensions of the halves, $\dim\operatorname{Sym}=10$ and $\dim\Lambda=6$.

**Corollary.** In real dimensions the table is

| carrier | $\cap\operatorname{Sym}$ | $\cap\Lambda$ |
|---|---|---|
| $V_0$ | $2$ | $0$ |
| $V_1$ | $4$ | $2$ |
| $V_2$ | $6$ | $4$ |
| $V_3$ | $8$ | $6$ |

*Proof.* Every entry of the complex table is doubled, and the real dimensions of the halves are $20$ and $12$.

**Corollary.** The row sums are $1,3,5,7$ and the column sums are $10$ and $6$; the two grand totals are $16$ and $16$.

*Proof.* The table and the dimensions of the carriers.

## The Computation

**Definition.** Let $P_k$ be the projector of the Casimir onto $V_k$, and let $\sigma_{\pm}(X)=(X\pm X^{\mathsf T})/2$ be the projections onto the halves.

**Proposition.** $\dim(V_k\cap\operatorname{Sym})$ is the rank of $\sigma_{+}P_k$ as a map from the algebra to the algebra, and $\dim(V_k\cap\Lambda)$ is the rank of $\sigma_{-}P_k$.

*Proof.* $\sigma_{+}P_k$ has image $\sigma_{+}V_k\subseteq V_k\cap\operatorname{Sym}$, and every element of the intersection is fixed by both maps, so the image is exactly the intersection; the same for $\sigma_{-}$.

**Corollary.** The ranks are additive: $\operatorname{rank}\sigma_{+}P_k+\operatorname{rank}\sigma_{-}P_k=2k+1$.

*Proof.* $\sigma_{+}+\sigma_{-}$ is the identity and both maps have the same kernel on $V_k$; equivalently the two images are complementary in $V_k$.

**The numerical check.** The ranks were computed on the seven-, five-, three- and one-dimensional carriers with residuals of order $10^{-16}$, and the entries are integers to that precision.

*Proof.* The ranks are stable under perturbation of the projector, which is Hermitian with eigenvalues zero and one.

**The reading.** The table is not the parity rule, although the numbers agree in size: the parity rule splits the module's squares, and the table splits the carriers. The agreement is a numerical fact of the four rows and not a consequence of the tensor identification, since the transpose is not compatible with it.

## Witnesses

**The centre.** The only element of $V_0$ is the identity, which is symmetric, so the first row is $(1,0)$.

*Proof.* $V_0=\mathbb{C}\mathrm I$ and $\mathrm I^{\mathsf T}=\mathrm I$.

**The top row.** $E_{03}+E_{30}$ is symmetric and lies in $V_3$, and $E_{03}-E_{30}$ is antisymmetric and lies in $V_3$; both have rank two. Together with the two further symmetric and one further antisymmetric directions of the carrier, they fill the row $(4,3)$.

*Proof.* Both elements have weight zero and are fixed by the projector of label $3$ to a residual of order $10^{-16}$; their eigenvalues are $\pm1,0,0$ and the rank is two.

**The triplet.** The diagonal generator $J_z$ is symmetric and lies in $V_1$, and the raising operator $J_+$ has a symmetric part in $V_1$ and an antisymmetric part, $(J_+-J_+^{\mathsf T})/2$, also in $V_1$ by the failure of the splitting. The row $(2,1)$ is spanned by these and by one more symmetric direction.

*Proof.* $J_z$ is diagonal, hence symmetric; the projections of $J_+$ and $J_+^{\mathsf T}$ on $V_1$ are nonzero and independent, and one combination is symmetric and the other antisymmetric.

**The middle carrier.** $V_2$ has three symmetric and two antisymmetric directions, computed by the same restriction.

*Proof.* The table.

## Two Proofs of the Edges

**Proposition.** $V_k\cap\Lambda$ has dimension at least $k$ and $V_k\cap\operatorname{Sym}$ at least $k+1$ for $k=0,1,2,3$.

*Proof.* The two maps $\sigma_{\pm}P_k$ have images of dimensions summing to $2k+1$; neither image is zero for $k\ge1$, since $P_k$ does not commute with $\theta$ and the carrier is not contained in a half. The table gives the exact values, and the lower bounds are read from it.

**Corollary.** No carrier of positive label is contained in a half, and no carrier meets a half only in zero.

*Proof.* The entries $k$ and $k+1$ are both positive for $k\ge1$, and for $k=0$ the entry in $\Lambda$ is zero because the identity is symmetric.

**Corollary.** The centre is the only carrier whose intersection with $\Lambda$ vanishes, and it is the only carrier contained in a half.

*Proof.* The first row of the table.

## The Reading

**The pattern.** The entries are $k+1$ and $k$: each carrier has one more symmetric direction than antisymmetric ones, and the difference is one for every carrier. The column totals $10$ and $6$ are then the sums of $1+2+3+4$ and $0+1+2+3$.

*Proof.* The table, and the two arithmetic sums.

**The comparison with the halves.** The symmetric half is larger than the antisymmetric, and the excess is distributed evenly over the four carriers, one dimension each.

*Proof.* The difference column is identically one.

**The boundary.** The table says nothing about which elements of a carrier are symmetric beyond their number; it does not give a basis adapted to both cuts, and such a basis does not exist in general because the two cuts do not commute.

## The Check of the Table

**The sums.** Each entry of the table is a dimension, and the sums along the rows recover the dimensions of the carriers while the sums along the columns recover those of the halves; the two sets of totals agree, which is the check of the table.

## Summary

Each carrier meets each half in a subspace whose dimension is computed from the ranks of the two projections of the Casimir's projector. In complex dimensions the table is $V_0:(1,0)$, $V_1:(2,1)$, $V_2:(3,2)$, $V_3:(4,3)$, with row sums $1,3,5,7$ and column sums $10,6$; in real dimensions the entries are doubled to $(2,0),(4,2),(6,4),(8,6)$, with column sums $20$ and $12$.

The pattern is $k+1$ symmetric directions and $k$ antisymmetric ones for the carrier of label $k$, so the symmetric half is larger by one dimension in every carrier. The centre is the only carrier contained in a half and the only one whose intersection with the antisymmetric half vanishes.

The table is not the parity rule: the parity rule splits the squares of the module, and the table splits the carriers of the algebra, and the agreement of the numbers is not a consequence of the tensor identification.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V_k$ | the carrier of label $k$ |
| $P_k$ | the projector of the Casimir onto $V_k$ |
| $\sigma_{\pm}(X)=(X\pm X^{\mathsf T})/2$ | the projections onto the halves |
| $k+1,\ k$ | the complex dimensions of $V_k\cap\operatorname{Sym}$ and $V_k\cap\Lambda$ |

## Further Reading

- [Neither Half Is Invariant: the Cartan Element Carries $\operatorname{Sym}$ into $\Lambda$](neither-half-is-invariant-the-cartan-element-at-n-4.html), for the failure of the splitting.
- [The Parity Rule: $\operatorname{Sym}^{2}=V_3\oplus V_1$ and $\Lambda^{2}=V_2\oplus V_0$](the-parity-rule-the-two-squares-of-the-module-at-n-4.html), for the splitting of the module.
- [The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$](the-clebsch-gordan-decomposition-of-m4c.html), for the carriers and the projectors.
- [The Intersection Table: Where Each Carrier Meets $\operatorname{Sym}$ and $\Lambda$](the-intersection-table-of-the-carriers-with-the-two-halves.html), for the row at order two.
- [Which Spin Lives in Which Reading at $n=4$](which-spin-lives-in-which-reading-at-n-4.html), for the labels in the other readings.
