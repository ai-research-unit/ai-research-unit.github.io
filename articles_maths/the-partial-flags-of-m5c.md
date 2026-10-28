# __The Partial Flags of $M_5(\mathbb{C})$__

## Introduction

A **flag** in $V=\mathbb{C}^5$ is a chain of subspaces

$$
0\subset V_1\subset V_2\subset\cdots\subset V_4\subset V_5=V,
\qquad \dim V_k=k .
$$

The full flag variety $\mathcal{F}$ is the set of such chains; it has dimension

$$
0+1+2+3+4=10 .
$$

A **partial flag** is a chain with some of the dimensions omitted, for example a single two-plane (a point of the Grassmannian $\mathrm{Gr}(2,5)$, of dimension $6$) or a line inside a three-plane (a flag of type $(1,3)$, of dimension $8$). The partial flags are the quotients of the full flag variety by the parabolic subgroups of $GL_5$; the full flag is the case of the Borel.

The root set of *Roots of Unity and the Lagrange Idempotents of $M_5(\mathbb{C})$* is $PGL_5/T$, of dimension $20$. It is **not** the full flag variety: a root determines an ordered splitting $V=L_1\oplus\cdots\oplus L_5$ into five lines, and the flag is only the chain of partial sums $V_k=L_1\oplus\cdots\oplus L_k$. The map "forget the splitting" is a fibration

$$
PGL_5/T\longrightarrow PGL_5/B\cong\mathcal{F}
$$

with fibre the unipotent radical $B/T$, of dimension $10$. The count is

$$
20=10+10:
$$

the root set is a ten-dimensional bundle over the ten-dimensional full flag variety. The root set is not the flag variety, and the difference is exactly the splitting data that the root remembers and the flag forgets.

This article develops the flags, the partial flags, the incidence and the dimension counts, and then compares them with the root set. It assumes the root and the gauge of the preceding articles; it uses no form and no topology. The full flag variety is the model for the **ordered** structures of the root; the partial flag of the rank-two projection is the Grassmannian $\mathrm{Gr}(2,5)$ of *The Rank-Two Split of $M_5(\mathbb{C})$*, read geometrically.

## Flags and Partial Flags

### The Full Flag

**Definition.** A **full flag** of $V=\mathbb{C}^5$ is a chain

$$
F:\quad 0\subset V_1\subset V_2\subset V_3\subset V_4\subset V_5=V,
\qquad \dim V_k=k .
$$

The **standard flag** $F_0$ is the chain $V_k=\operatorname{span}(e_1,\dots,e_k)$ of the standard basis.

**Proposition.** A full flag is equivalently an ordered basis $(v_1,\dots,v_5)$ considered up to the following equivalence: two bases give the same flag if they differ by an upper triangular matrix with nonzero diagonal. The flag is the chain of partial spans, not the basis.

**Proof.** Given a basis, the partial spans $V_k=\operatorname{span}(v_1,\dots,v_k)$ form a flag. Conversely, given a flag, choose $v_k\in V_k\setminus V_{k-1}$; the resulting basis has the flag as its partial spans. A change of basis preserving every $V_k$ is upper triangular in the flag basis, and its diagonal entries are nonzero because it preserves the successive quotients $V_k/V_{k-1}$.

**Corollary.** A full flag is a point of the quotient $GL_5/B$, where $B$ is the Borel subgroup of upper triangular matrices.

**Proof.** The standard flag has stabiliser $B$: a matrix preserves every $V_k$ exactly when it is upper triangular. The set of flags is the orbit of the standard flag, $GL_5/B$.

### The Partial Flags

**Definition.** A **partial flag of type** $(d_1,\dots,d_s)$ with $1\le d_1<\cdots<d_s\le4$ is a chain

$$
0\subset V_{d_1}\subset\cdots\subset V_{d_s}\subset V,
\qquad \dim V_{d_i}=d_i .
$$

The full flag is the type $(1,2,3,4)$; a single subspace of dimension $d$ is the type $(d)$; the type $(1,3)$ is a line inside a three-plane.

**Proposition.** A partial flag of type $(d_1,\dots,d_s)$ is a point of the quotient $GL_5/P$, where $P$ is the parabolic subgroup of block upper triangular matrices with diagonal blocks of sizes $d_1,d_2-d_1,\dots,5-d_s$.

**Proof.** The standard partial flag with $V_{d_i}=\operatorname{span}(e_1,\dots,e_{d_i})$ has stabiliser the block upper triangular matrices with the stated diagonal blocks: a matrix preserves each $V_{d_i}$ exactly when its entries below the diagonal blocks vanish. The set of partial flags is the orbit, $GL_5/P$.

### The Dimension Formula

**Theorem.** The dimension of the partial flag variety of type $(d_1,\dots,d_s)$ is

$$
\dim= \sum_{i=1}^{s}d_i(d_{i+1}-d_i),
\qquad d_{s+1}=5 .
$$

For the full flag $(1,2,3,4)$ this is

$$
1\cdot1+2\cdot1+3\cdot1+4\cdot1=10 .
$$

For a single subspace $(d)$ it is $d(5-d)$, the dimension of the Grassmannian $\mathrm{Gr}(d,5)$.

**Proof.** The parabolic $P$ is block upper triangular with diagonal blocks of sizes $d_1,d_2-d_1,\dots,5-d_s$. The number of free entries is the sum of the squares of the block sizes plus the entries above the diagonal blocks; equivalently, the dimension of $P$ is

$$
\dim P=25-\sum_{i=1}^{s}d_i(d_{i+1}-d_i),
$$

by counting the entries below the diagonal blocks, which are the only forced zeros. The flag variety $GL_5/P$ has dimension $25-\dim P$, which is the stated sum.

**Corollary.** The dimensions of the partial flags of $V=\mathbb{C}^5$ include

| Type | Dimension |
|---|---|
| $(4)$ | $4$ |
| $(1)$ or $(3)$ | $4$ |
| $(2)$ | $6$ |
| $(1,2)$ or $(3,4)$ | $7$ |
| $(1,3)$ or $(2,4)$ | $8$ |
| $(1,2,3)$ or $(2,3,4)$ | $9$ |
| $(1,2,3,4)$ | $10$ |

**Proof.** Evaluate the formula: $(1,2)$ gives $1\cdot1+2\cdot3=7$; $(1,3)$ gives $1\cdot2+3\cdot2=8$; $(1,2,3)$ gives $1+2+3\cdot2=9$; the full flag gives $10$. The single subspace $(1)$ or $(4)$ gives $1\cdot4=4$; $(2)$ gives $2\cdot3=6$; $(3)$ gives $3\cdot2=6$.

**Remark.** **The full flag has dimension $10$, and it is the largest of the flag varieties of $V$.** Every partial flag is a quotient of the full flag by forgetting some of the subspaces; the dimensions decrease as the type is coarsened. The full flag is the finest, and the single subspace is the coarsest.

## The Full Flag Variety

### The Borel and the Unipotent Radical

**Definition.** The **Borel subgroup** $B\subset GL_5$ is the group of upper triangular matrices; its **unipotent radical** $U$ is the group of upper triangular matrices with all diagonal entries $1$.

**Proposition.** $\dim B=15$, $\dim U=10$, $\dim T=5$, and $B=U\rtimes T$, where $T$ is the diagonal torus. The full flag variety has dimension

$$
\dim GL_5-\dim B=25-15=10=\dim U .
$$

**Proof.** An upper triangular $5\times5$ matrix has $15$ entries on and above the diagonal, so $\dim B=15$; the unipotent radical has the $10$ off-diagonal entries, so $\dim U=10$; the diagonal torus has dimension $5$. The quotient $GL_5/B$ has dimension $25-15=10$.

**Corollary.** The tangent space of the full flag variety at the standard flag is the space of strictly lower triangular matrices, of dimension $10$.

**Proof.** The quotient $GL_5/B$ has tangent space $\mathfrak{gl}_5/\mathfrak{b}$, where $\mathfrak{b}$ is the Borel; the quotient is isomorphic to the strictly lower triangular matrices, of dimension $10$.

### The Incidence

**Definition.** The **incidence variety** of a partial flag of type $(d,e)$ with $d<e$ is the set of pairs $(V_d,V_e)$ with $V_d\subset V_e\subset V$, $\dim V_d=d$, $\dim V_e=e$.

**Proposition.** The incidence variety of type $(d,e)$ is the partial flag variety of type $(d,e)$, of dimension

$$
d(e-d)+e(5-e).
$$

For $(1,2)$ it has dimension $1\cdot1+2\cdot3=7$; the projection to the line $\mathbb{P}^4$ has fibre $\mathbb{P}^3$, so $4+3=7$.

**Proof.** The type $(d,e)$ is the partial flag with the two subspaces; the dimension formula gives the number. For $(1,2)$, a line in $\mathbb{C}^5$ is a point of $\mathbb{P}^4$ (dimension $4$), and the two-planes containing it form the projective space of lines in the quotient $\mathbb{C}^5/L$, of dimension $3$; the total is $4+3=7$.

**Corollary.** The incidence correspondence is a bundle over the Grassmannian $\mathrm{Gr}(d,5)$ with fibre the Grassmannian $\mathrm{Gr}(e-d,5-d)$, of dimension $(e-d)(5-e)$; the total dimension is $d(5-d)+(e-d)(5-e)$, which equals $d(e-d)+e(5-e)$.

**Proof.** Fix $V_d$; the subspaces $V_e$ containing it correspond to the $(e-d)$-dimensional subspaces of $V/V_d\cong\mathbb{C}^{5-d}$, a Grassmannian of dimension $(e-d)((5-d)-(e-d))=(e-d)(5-e)$. Add the dimension $d(5-d)$ of the base.

## The Root Set and the Flag Variety

### The Map

**Definition.** The **splitting map** sends an ordered direct-sum decomposition

$$
V=L_1\oplus L_2\oplus\cdots\oplus L_5,\qquad \dim L_k=1,
$$

to the full flag

$$
V_k=L_1\oplus\cdots\oplus L_k,\qquad k=1,\dots,5 .
$$

**Proposition.** The splittings are the points of $PGL_5/T$, of dimension $20$; the full flags are the points of $PGL_5/B$, of dimension $10$; the splitting map is a fibration with fibre $B/T\cong U$, of dimension $10$.

**Proof.** An ordered splitting is an ordered basis modulo the diagonal torus, hence a point of $GL_5/T$ modulo scalars, $PGL_5/T$. The flag is the chain of partial sums, a point of $PGL_5/B$. The fibre over the standard flag is the set of bases whose partial spans are the standard flag, i.e., the upper triangular matrices modulo the diagonal, which is $U$. The dimensions are $20$, $10$ and $10$; the bundle is locally trivial.

**Corollary.** The root set $PGL_5/T$ is a $10$-dimensional bundle over the full flag variety $PGL_5/B$:

$$
20=10+10 .
$$

The root set is **not** the flag variety; it is the total space of the splitting bundle.

**Proof.** The root set is exactly the set of splittings, by the spectral decomposition of a root: a root $H$ determines the five lines $L_k=\ker(H-\zeta_kI)$, and conversely an ordered splitting with distinct scalars $\zeta_k$ determines the root $H=\sum_k\zeta_kP_k$. The splitting map forgets the labels and the lines, keeping only the chain.

### Why They Differ

**Theorem.** The root set and the full flag variety are different spaces: they have different dimensions ($20$ and $10$), and the root set carries the data of the five lines, while the flag carries only the chain of partial sums. The fibre of the splitting map is the unipotent radical $U$, of dimension $10$.

**Proof.** The dimensions are computed above. The fibre is nontrivial: over the standard flag, the bases $(v_1,\dots,v_5)$ with $v_k\in V_k\setminus V_{k-1}$ form the upper triangular matrices modulo the diagonal, which is $U$, of dimension $10$. A point of $U$ changes the splitting without changing the flag.

**Corollary.** The root set is not a partial flag variety either. The maps to the partial flags are the compositions

$$
PGL_5/T\longrightarrow PGL_5/P\longrightarrow PGL_5/B,
$$

and the fibres have dimensions $14$ (for the rank-two parabolic), $10$ (for the Borel), and so on.

**Proof.** The dimension of $PGL_5/P$ for the rank-two parabolic is $6$, and $20-6=14$; for the Borel it is $10$, and $20-10=10$. The fibres are $P/T$, of the stated dimensions.

**Remark.** **The flag variety is the space of chains; the root set is the space of ordered splittings.** The root remembers the five lines and their order; the flag remembers only the chain of their partial sums. This is the geometric content of the difference between the root and the flag, and it is the reason the root set has dimension $20$ rather than $10$.

## The Rank-Two Partial Flag

### The Grassmannian

**Definition.** The **Grassmannian** $\mathrm{Gr}(2,5)$ is the set of two-dimensional subspaces of $\mathbb{C}^5$.

**Proposition.** $\mathrm{Gr}(2,5)$ is the partial flag variety of type $(2)$, of dimension $2\cdot3=6$. It is the quotient $GL_5/P$ for the parabolic $P$ of block upper triangular matrices with diagonal blocks $2$ and $3$.

**Proof.** The dimension formula for $(2)$ gives $2(5-2)=6$. The stabiliser of the standard two-plane is the parabolic with blocks $2$ and $3$; the quotient is the Grassmannian.

**Corollary.** The rank-two projection $P$ of *The Rank-Two Split of $M_5(\mathbb{C})$* determines a point of $\mathrm{Gr}(2,5)$, its image $\operatorname{im}P$; the map $P\mapsto\operatorname{im}P$ from rank-two projections to the Grassmannian is surjective, with fibre the set of complements, of dimension $6$.

**Proof.** Every two-plane is the image of a rank-two projection; the complements of a fixed two-plane are the graphs of linear maps from the two-plane to a complement, of dimension $2\cdot3=6$.

### The Fibre of the Root Set

**Proposition.** The map from the root set to the Grassmannian,

$$
PGL_5/T\longrightarrow PGL_5/P\cong\mathrm{Gr}(2,5),
$$

has fibre dimension $14$; the total is $6+14=20$.

**Proof.** The parabolic $P$ of the rank-two block has dimension $18$ in $PGL_5$; the torus $T$ has dimension $4$; the fibre $P/T$ has dimension $14$. The base has dimension $6$; the sum is $20$.

**Corollary.** The rank-two split is the **partial** flag of the two-plane, not the full flag: it remembers the two-plane and forgets the splitting of the two-plane and of its complement. The full flag remembers the chain of all dimensions; the root set remembers all five lines.

**Proof.** The partial flag of type $(2)$ is the single subspace; the root set maps to it by forgetting the lines inside the two-plane and inside the complement. The full flag maps to the same Grassmannian by remembering the chain inside the two-plane and inside the complement.

## Summary

A full flag of $\mathbb{C}^5$ has dimension $10$; a partial flag of type $(d_1,\dots,d_s)$ has dimension $\sum_i d_i(d_{i+1}-d_i)$ with $d_{s+1}=5$. The Grassmannian $\mathrm{Gr}(2,5)$ has dimension $6$; the incidence of a line in a two-plane has dimension $7$; the full flag is the finest, of dimension $10$.

$$
\boxed{\ \dim\mathcal{F}=10,\qquad \dim\mathrm{Gr}(2,5)=6,\qquad \dim(PGL_5/T)=20=10+10.\ }
$$

The root set $PGL_5/T$ is the space of ordered splittings into five lines; it is a $10$-dimensional bundle over the full flag variety $PGL_5/B$, with fibre the unipotent radical $U$ of dimension $10$. The root set is **not** the flag variety: the flag forgets the splitting, and the root remembers it. The rank-two split is the partial flag of the two-plane, of dimension $6$; the root set maps to it with fibre dimension $14$.

| Space | Dimension |
|---|---|
| Full flag $\mathcal{F}=PGL_5/B$ | $10$ |
| Partial flag $(1,2)$ | $7$ |
| Partial flag $(1,3)$ | $8$ |
| Partial flag $(1,2,3)$ | $9$ |
| Grassmannian $\mathrm{Gr}(2,5)$ | $6$ |
| Root set $PGL_5/T$ | $20$ |
| Fibre of the splitting map | $10$ |
| Fibre over $\mathrm{Gr}(2,5)$ | $14$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V=\mathbb{C}^5$ | The five-dimensional space |
| $\mathcal{F}$ | The full flag variety |
| $V_k$ | The $k$-dimensional subspace of a flag |
| $(d_1,\dots,d_s)$ | The type of a partial flag |
| $B$ | The Borel subgroup of upper triangular matrices |
| $U$ | The unipotent radical of $B$, dimension $10$ |
| $P$ | A parabolic subgroup |
| $\mathrm{Gr}(d,5)$ | The Grassmannian of $d$-planes, dimension $d(5-d)$ |
| $PGL_5/T$ | The root set, the space of ordered splittings, dimension $20$ |

## Further Reading

- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the flag varieties, the Borel and parabolic subgroups and the dimension formula.
- Michel Demazure and Pierre Gabriel, *Groupes algébriques, Tome I* (North-Holland, 1970), for the flag varieties, the parabolic subgroups and the incidence correspondences.
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the Grassmannians, the incidence varieties and their dimensions.
- [Roots of Unity and the Lagrange Idempotents of $M_5(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-of-m5c.html), for the root set and its dimension $20$.
- [The Frame, the Simple Nilpotents and the Gauge of $M_5(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-of-m5c.html), for the frame bundle and the four-parameter gauge.
- [The Rank-Two Split of $M_5(\mathbb{C})$](the-rank-two-split-of-m5c.html), for the rank-two projection and the Grassmannian of its image.
- [The Adjoint Action, the Orbits and the Flag Variety of $M_5(\mathbb{C})$](the-adjoint-action-the-orbits-and-the-flag-variety-of-m5c.html), for the conjugacy class of the root and the flag-variety picture.
