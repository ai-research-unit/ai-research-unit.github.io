# __The Peirce Decomposition in $n$ Dimensions over $\mathbb{R}$__

## Introduction

**A frame of $n$ orthogonal idempotents in $M_n(\mathbb{R})$ cuts the algebra into $n^{2}$ Peirce spaces $A_{kl}=P_kM_n(\mathbb{R})P_l$, whose dimensions are $r_kr_l$ and whose product obeys $A_{kl}A_{lm}\subseteq A_{km}$ and $A_{kl}A_{mn}=0$ for $l\ne m$.**

The article defines the frame, proves the multiplication rule, proves the direct sum and the dimension formula, shows that every real idempotent of rank $r$ is conjugate to $\operatorname{diag}(\mathrm{I}_r,0)$ and that a frame exists with any prescribed ranks, and writes the cases $n=2$ and $n=3$ in full. It assumes *The Peirce Basis in $n$ Dimensions* for the choice of one element per line, and *Lagrange Idempotents of a Real Matrix with Simple Real Spectrum* for the idempotents produced by a matrix.

## Frames

**Definition.** A **frame** is a family $P_1,\dots,P_m$ of elements of $M_n(\mathbb{R})$ with

$$
P_k^{2}=P_k,\qquad P_kP_l=0\ \ (k\ne l),\qquad \sum_{k=1}^{m}P_k=\mathrm{I}.
$$

The first condition makes each $P_k$ a projector, the second makes the family orthogonal, and the third makes it complete.

**The rank of $P_k$ is written $r_k$.** The image $V_k=\operatorname{im}P_k$ has dimension $r_k$, and $P_k$ is the projection onto $V_k$ along $\ker P_k$.

**The images are independent and span.** Orthogonality gives $P_kP_l=0$, so $V_l\subseteq\ker P_k$ for $k\ne l$. Completeness gives $\sum_kv_k=v$ for $v_k=P_kv$, so the sum of the images is the whole space. Hence

$$
\mathbb{R}^{n}=V_1\oplus\cdots\oplus V_m,\qquad \sum_{k=1}^{m}r_k=n.
$$

**A frame in the sense of this article has $m=n$ members.** Then the sum of the ranks is $n$ and the decomposition of $\mathbb{R}^{n}$ has $n$ summands. A family with fewer members is the same construction with fewer indices and gives a coarser decomposition; the count $n$ is what fixes the name.

**Every frame comes from a decomposition of $\mathbb{R}^{n}$.** Given a direct sum $\mathbb{R}^{n}=V_1\oplus\cdots\oplus V_n$, define $P_k$ to be the projection onto $V_k$ along the sum of the others. The result is a frame, and every frame arises this way, with $V_k=\operatorname{im}P_k$.

## The Peirce Spaces

**Definition.** The **Peirce space** of the pair $(k,l)$ is

$$
A_{kl}=P_kM_n(\mathbb{R})P_l=\{P_kXP_l:X\in M_n(\mathbb{R})\}.
$$

The diagonal spaces $A_{kk}$ are the Peirce components of the frame, and the off-diagonal spaces $A_{kl}$ with $k\ne l$ are the mixed components.

**The space $A_{kl}$ is the space of homomorphisms from $V_l$ to $V_k$.** An element $P_kXP_l$ kills $\ker P_l$ and lands in $V_k$, and every linear map $V_l\to V_k$ extended by zero is of that form. So $A_{kl}$ is $\operatorname{Hom}(V_l,V_k)$ read inside $M_n(\mathbb{R})$, and

$$
\dim A_{kl}=r_kr_l.
$$

**The diagonal space $A_{kk}$ consists of the endomorphisms of $V_k$ extended by zero.** It is a subalgebra of $M_n(\mathbb{R})$ with unit $P_k$, isomorphic to $M_{r_k}(\mathbb{R})$.

**The definition is not a choice.** The spaces depend only on the frame, not on any basis. A choice of basis inside each $V_k$ turns $A_{kl}$ into the space of $r_k\times r_l$ arrays, and that is the coordinate picture of the next sections.

## The Multiplication Rule

**Theorem.** For all $k,l,m$,

$$
A_{kl}A_{lm}\subseteq A_{km},\qquad A_{kl}A_{mn}=0\quad(l\ne m).
$$

**Proof.** Take $X=P_kX'P_l$ in $A_{kl}$ and $Y=P_mY'P_n$ in $A_{mn}$. Then

$$
XY=P_kX'P_lP_mY'P_n=\delta_{lm}\,P_kX'P_lY'P_n.
$$

When $l=m$ the product is $P_k(X'P_lY')P_n$, which lies in $A_{kn}$. When $l\ne m$ the factor $P_lP_m$ vanishes and the product is zero.

**The rule was checked on a frame of ranks $(1,2,2)$ in $M_5(\mathbb{R})$.** With random elements of each space, every product $A_{kl}A_{lm}$ landed in $A_{km}$ to machine precision, and every product $A_{kl}A_{mn}$ with $l\ne m$ was the zero matrix.

**The rule is the multiplication table of an algebra graded by the index set.** The indices behave like the vertices of a complete graph, the diagonal spaces like the vertices and the mixed spaces like the edges. A product of two edge elements is zero unless the edges meet, and then the product lies on the edge joining the far ends.

## The Direct Sum

**Theorem.** $M_n(\mathbb{R})=\bigoplus_{k,l}A_{kl}$, and the sum is direct.

**Proof of the spanning.** For any $X$, the completeness of the frame gives $X=\mathrm{I}\,X\,\mathrm{I}=\sum_{k,l}P_kXP_l$, which is a sum of one element of each space.

**Proof of the independence.** Suppose $\sum_{k,l}X_{kl}=0$ with $X_{kl}\in A_{kl}$. Multiply on the left by $P_k$ and on the right by $P_l$. Only the term $X_{kl}$ survives, because $P_kA_{pq}P_l=0$ unless $(p,q)=(k,l)$. So $X_{kl}=0$ for every pair, and the sum is direct.

**The dimension count follows.** The direct sum has $n^{2}$ summands, because the index set is the set of pairs. Its dimension is $\sum_{k,l}r_kr_l=\bigl(\sum_kr_k\bigr)^{2}=n^{2}$, which is the dimension of the algebra. So the decomposition is complete, and no space is missing.

**The count is confirmed for eight frames.** The dimensions $\dim A_{kl}$ were computed as ranks of the linear maps $X\mapsto P_kXP_l$ and gave these arrays.

| Ranks | $\dim A_{kl}$ | Sum | $n^{2}$ |
|---|---|---|---|
| $(1,1)$ | all $1$ | $4$ | $4$ |
| $(2,1)$ | $4,2,2,1$ | $9$ | $9$ |
| $(3,2)$ | $9,6;\,6,4$ | $25$ | $25$ |
| $(1,2,3)$ | $1,2,3;\,2,4,6;\,3,6,9$ | $36$ | $36$ |
| $(2,2,2)$ | all $4$ | $36$ | $36$ |
| $(2,2,1)$ | $4,4,2;\,4,4,2;\,2,2,1$ | $25$ | $25$ |
| $(1,3)$ | $1,3;\,3,9$ | $16$ | $16$ |
| $(1,1,1,1)$ | all $1$ | $16$ | $16$ |

In every case the entry $(k,l)$ equals $r_kr_l$ and the total equals $n^{2}$.

**The dimensions are the products of the ranks, and the sum is a square.** Since $\sum_{k,l}r_kr_l=\bigl(\sum_kr_k\bigr)^{2}=n^{2}$, the dimension count of the decomposition is the same computation as the dimension of the algebra. The identity is the discrete version of the expansion of a square.

## Every Rank Is Attainable

**Theorem.** Every idempotent of $M_n(\mathbb{R})$ of rank $r$ is conjugate to $\operatorname{diag}(\mathrm{I}_r,0)$.

**Proof.** Let $P^{2}=P$ and let $V=\operatorname{im}P$ and $W=\ker P$. For $v\in V\cap W$ we have $v=Pv=0$, so the intersection is zero. For any $x$ we have $x=Px+(x-Px)$ with $Px\in V$ and $P(x-Px)=Px-P^{2}x=0$, so $x\in V+W$. Hence $\mathbb{R}^{n}=V\oplus W$. In a basis adapted to this decomposition, $P$ acts as the identity on $V$ and as zero on $W$, so its matrix is $\operatorname{diag}(\mathrm{I}_r,0)$.

**The check at $n=4$ confirms the eigenvalues and the trace.** Random idempotents of ranks $1,2,3$ were built as $S\operatorname{diag}(\mathrm{I}_r,0)S^{-1}$ with $S$ invertible. Each satisfied $P^{2}=P$ to $2\times10^{-16}$, had rank $r$, and had eigenvalues $1$ with multiplicity $r$ and $0$ with multiplicity $n-r$; the traces were $1,2,3$.

**So a frame exists with any prescribed ranks.** Take positive integers $r_1,\dots,r_n$ with sum $n$, take any direct sum $\mathbb{R}^{n}=V_1\oplus\cdots\oplus V_n$ with $\dim V_k=r_k$, and let $P_k$ be the projection onto $V_k$ along the sum of the others. The idempotents are real, orthogonal, of rank $r_k$, and complete.

**The decomposition is therefore a coordinate statement.** Every frame is conjugate to a frame of diagonal blocks, and every array of ranks with sum $n$ occurs. The Peirce decomposition adds nothing to the choice of a decomposition of $\mathbb{R}^{n}$: it is that choice, written as a decomposition of the algebra.

**The stabiliser of a frame is the block diagonal group.** Two decompositions with the same ranks are related by an element of $\mathrm{GL}_n(\mathbb{R})$, and the stabiliser of one of them is $\mathrm{GL}_{r_1}(\mathbb{R})\times\cdots\times\mathrm{GL}_{r_n}(\mathbb{R})$, of dimension $\sum_kr_k^{2}$. So the set of frames with those ranks has dimension

$$
n^{2}-\sum_{k=1}^{n}r_k^{2}.
$$

For $n=3$ with ranks $(2,1)$ the count is $9-5=4$, and with ranks $(1,1,1)$ it is $9-3=6$.

## The Case $n=2$

**A frame of $M_2(\mathbb{R})$ has two idempotents of rank one.** Up to conjugation it is $P_1=E_{11}$ and $P_2=E_{22}$, and the four Peirce spaces are the four lines

$$
A_{11}=\mathbb{R}E_{11},\qquad A_{12}=\mathbb{R}E_{12},\qquad A_{21}=\mathbb{R}E_{21},\qquad A_{22}=\mathbb{R}E_{22}.
$$

Each has dimension $1$, the products of ranks $1\cdot1$, and the four sum to the four-dimensional algebra.

**The multiplication table is the table of the matrix units.** The nonzero products are

$$
E_{11}E_{11}=E_{11},\qquad E_{11}E_{12}=E_{12},\qquad E_{12}E_{21}=E_{11},\qquad E_{21}E_{12}=E_{22},
$$

with the mirror images, and every product whose indices do not match is zero. In the notation of the spaces, $A_{11}A_{12}\subseteq A_{12}$, $A_{12}A_{21}\subseteq A_{11}$, $A_{21}A_{12}\subseteq A_{22}$ and $A_{11}A_{22}=A_{12}A_{12}=0$.

**The two halves of the algebra appear here.** The sum $A_{11}\oplus A_{22}$ is the diagonal subalgebra, of dimension two, and $A_{12}\oplus A_{21}$ is the space of off-diagonal matrices. The trace form has signature $(3,1)$ on $M_2(\mathbb{R})$, and the negative direction lies in the mixed part.

## The Case $n=3$

**A frame of ranks $(2,1)$ gives the blocks $4,2,2,1$.** Take $P_1=\operatorname{diag}(1,1,0)$ and $P_2=\operatorname{diag}(0,0,1)$. Then

$$
A_{11}=\begin{pmatrix}\ast&\ast&0\\ \ast&\ast&0\\ 0&0&0\end{pmatrix},\qquad
A_{12}=\begin{pmatrix}0&0&\ast\\ 0&0&\ast\\ 0&0&0\end{pmatrix},\qquad
A_{21}=\begin{pmatrix}0&0&0\\ 0&0&0\\ \ast&\ast&0\end{pmatrix},\qquad
A_{22}=\begin{pmatrix}0&0&0\\ 0&0&0\\ 0&0&\ast\end{pmatrix},
$$

with the stars denoting free entries. The dimensions are $4$, $2$, $2$ and $1$, and their sum is $9$. The space $A_{11}$ is a copy of $M_2(\mathbb{R})$ with unit $P_1$, and $A_{22}$ is a copy of $M_1(\mathbb{R})$ with unit $P_2$.

**The mixed spaces multiply into the diagonal ones.** A product of an element of $A_{12}$ with an element of $A_{21}$ is a $2\times2$ block in the upper left corner, so it lies in $A_{11}$; the reverse order lies in $A_{22}$. This is the multiplication rule with $m\ne l$ avoided and with the two diagonal cases separated.

**A frame of three lines gives the nine lines of the matrix units.** Take $P_k=E_{kk}$. Then $A_{kl}=\mathbb{R}E_{kl}$, every space has dimension $1$, and the multiplication is the rule $E_{kl}E_{lm}=E_{km}$ and $E_{kl}E_{mn}=0$ for $l\ne m$. This is the finest Peirce decomposition, and it is the one that makes the algebra a system of matrix units.

**The two frames are conjugate and the ranks are all that changes.** The frame of ranks $(2,1)$ and the frame of three lines both decompose the same algebra, and the second is a refinement of the first: each line of the fine frame lies inside one of the four spaces of the coarse one. The refinement exists because a rank-two idempotent can be split into two orthogonal idempotents of rank one.

## Summary

A frame in $M_n(\mathbb{R})$ is a family $P_1,\dots,P_n$ of orthogonal idempotents with sum $\mathrm{I}$ and ranks $r_k$ summing to $n$. The Peirce spaces $A_{kl}=P_kM_n(\mathbb{R})P_l$ are the spaces of homomorphisms $V_l\to V_k$, of dimension $r_kr_l$, and they multiply by $A_{kl}A_{lm}\subseteq A_{km}$ with $A_{kl}A_{mn}=0$ for $l\ne m$. The algebra is their direct sum, and the dimensions add to $\bigl(\sum_kr_k\bigr)^{2}=n^{2}$; the eight frames checked numerically give the entry $r_kr_l$ in each position and the total $n^{2}$. Every real idempotent of rank $r$ is conjugate to $\operatorname{diag}(\mathrm{I}_r,0)$, by the splitting $\mathbb{R}^{n}=\operatorname{im}P\oplus\ker P$, so a frame exists with any prescribed ranks, and the set of frames with those ranks has dimension $n^{2}-\sum_kr_k^{2}$. The Peirce decomposition is therefore a coordinate statement: it is the choice of a direct sum decomposition of $\mathbb{R}^{n}$, written as a decomposition of the algebra. At $n=2$ the four spaces are lines and the table is the table of matrix units; at $n=3$ a frame of ranks $(2,1)$ gives blocks of dimensions $4,2,2,1$, and a frame of three lines gives the nine matrix units.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P_k$ | a member of the frame, an idempotent |
| $r_k$ | the rank of $P_k$, the dimension of $V_k$ |
| $V_k=\operatorname{im}P_k$ | the $k$-th summand of $\mathbb{R}^{n}$ |
| $A_{kl}=P_kM_n(\mathbb{R})P_l$ | the Peirce space of the pair $(k,l)$ |
| $A_{kk}$ | a Peirce component, isomorphic to $M_{r_k}(\mathbb{R})$ |
| $E_{ij}$ | the matrix unit, the finest Peirce basis |
| $\mathrm{I}$ | the identity matrix, $\sum_kP_k$ |
| $\mathrm{GL}_{r_k}(\mathbb{R})$ | the group acting on $V_k$, the block of the stabiliser |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for Peirce decompositions, frames and the multiplication rule.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for Peirce decompositions relative to idempotents in central simple algebras.
- [The Peirce Decomposition in $n$ Dimensions](the-peirce-decomposition-in-n-dimensions.html), for the lines and the products over the complex field.
- [The Peirce Basis in $n$ Dimensions](the-peirce-basis-in-n-dimensions.html), for the choice of one element per line and the gauge.
- [Lagrange Idempotents of a Real Matrix with Simple Real Spectrum](lagrange-idempotents-of-a-real-matrix-with-simple-real-spectrum.html), for a frame produced by a single matrix.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the matrix units and the two halves.
