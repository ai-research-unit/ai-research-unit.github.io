# __The Triangular Decomposition $h\oplus n_+\oplus n_-$__

## Introduction

**The diagonal, the strictly upper triangular part and the strictly lower triangular part cut $M_n(\mathbb{R})$ into three pieces of dimensions $n$, $n(n-1)/2$ and $n(n-1)/2$, and the sum is direct with total $n^{2}$.**

The article defines the standard flag, proves that its stabiliser is the upper triangular algebra, counts the three pieces, proves that the upper triangular algebra is a subalgebra and that the strictly upper triangular part is a nilpotent ideal of index $n$, measures the brackets $[n_+,n_+]$ and $[n_+,n_-]$, and reads the decomposition as the infinitesimal Iwasawa picture. It assumes *The Fine Decomposition against the Diagonal* for the lines $L_{ij}$ and their weights, and *The Two Halves: Symmetric and Antisymmetric* for the antisymmetric part that appears in the Iwasawa sum.

## The Standard Flag

**Definition.** Let $e_1,\dots,e_n$ be the standard basis of $\mathbb{R}^{n}$ and put $V_k=\operatorname{span}\{e_1,\dots,e_k\}$. The chain

$$
0=V_0\subset V_1\subset V_2\subset\dots\subset V_n=\mathbb{R}^{n}
$$

is the standard flag, and $\dim V_k=k$.

**A complete flag is a chain of one subspace of each dimension.** The chain above has $n$ steps and no room for a further subspace: if $V_{k-1}\subset W\subset V_k$ then $W$ is one of the two ends, because the dimensions differ by one.

**The stabiliser is smaller over $\mathbb{R}$ than over $\mathbb{C}$.** Over $\mathbb{C}$ the same chain has the complex upper triangular group as stabiliser, of complex dimension $n(n+1)/2$ and real dimension $n(n+1)$. Over $\mathbb{R}$ the stabiliser has real dimension $n(n+1)/2$, which is also the dimension of the symmetric half.

## The Stabiliser Is the Upper Triangular Algebra

**Definition.** $UT_n=\{A\in M_n(\mathbb{R}):A_{ij}=0\ \text{for}\ i>j\}$.

**Theorem.** $A$ stabilises the standard flag, that is $AV_k\subseteq V_k$ for every $k$, if and only if $A\in UT_n$.

*Proof.* The condition $AV_k\subseteq V_k$ says that the image of $e_j$ lies in $V_j$ for every $j$, hence that the column $j$ of $A$ has no entry below row $j$. That is the condition $A_{ij}=0$ for $i>j$. Conversely, if $A$ is upper triangular then $Ae_j\in V_j$, and a linear combination of $e_1,\dots,e_k$ maps into $V_k$.

**The stabiliser is closed under the product and under inversion.** If $A$ and $B$ stabilise the flag, so does $AB$, because $ABV_k\subseteq AV_k\subseteq V_k$. If $A$ stabilises the flag and is invertible, so does $A^{-1}$, because $A$ induces an isomorphism $V_k\to V_k$ at each step.

**The algebra splits as the diagonal plus the strictly upper part.**

$$
UT_n=h\oplus n_+,\qquad \dim UT_n=n+\frac{n(n-1)}{2}=\frac{n(n+1)}{2}.
$$

The measured dimensions are $3$ at $n=2$, $6$ at $n=3$ and $10$ at $n=4$, equal to $n(n+1)/2$ in each case.

## The Three Pieces

**Definition.** $n_+$ is the set of strictly upper triangular matrices and $n_-$ the set of strictly lower triangular matrices:

$$
n_+=\operatorname{span}\{E_{ij}:i<j\},\qquad n_-=\operatorname{span}\{E_{ij}:i>j\}.
$$

**Each strictly triangular part has dimension $n(n-1)/2$.** The pairs $i<j$ number $\binom{n}{2}$, and the pairs $i>j$ number the same. So

$$
\dim n_+=\dim n_-=\frac{n(n-1)}{2}.
$$

**The three pieces are the graded pieces of the fine grading grouped by the sign of the weight.** A line $L_{ij}$ lies in $n_+$ when $\varepsilon_i-\varepsilon_j$ is positive, in $n_-$ when it is negative, and the diagonal is the zero weight. This is the grouping announced in *The Fine Decomposition against the Diagonal*.

**Theorem.** $M_n(\mathbb{R})=h\oplus n_+\oplus n_-$ and the sum is direct.

*Proof.* Every matrix is the sum of its diagonal, its strictly upper part and its strictly lower part, and each of the three is read off from a disjoint set of entries. So the three subspaces span and their pairwise intersections are zero.

**The dimension count closes.**

$$
n+\frac{n(n-1)}{2}+\frac{n(n-1)}{2}=n+n(n-1)=n^{2}.
$$

Measured as the rank of the union of the three bases, the sum has dimension $4$ at $n=2$, $9$ at $n=3$ and $16$ at $n=4$.

## The Upper Triangular Algebra

**Proposition.** $UT_n$ is a subalgebra of $M_n(\mathbb{R})$, and $n_+$ is a two-sided ideal of it.

*Proof.* The product of two upper triangular matrices is upper triangular: $(AB)_{ij}=\sum_{k}A_{ik}B_{kj}$, and a term is nonzero only when $i\le k\le j$, which forces $i\le j$. If in addition $A\in n_+$ then $i<k\le j$ and the entry vanishes for $i\ge j$, so $n_+\cdot UT_n\subseteq n_+$; the other side is the same computation.

**The ideal $n_+$ is also an ideal for the commutator.** For $H\in h$ and $X\in n_+$ the bracket $[H,X]$ is strictly upper triangular, and for $U\in UT_n$ and $X\in n_+$ the bracket $[U,X]=UX-XU$ lies in $n_+$ because both products do.

**The quotient $UT_n/n_+$ is the diagonal.** $h$ maps isomorphically onto the quotient, so the diagonal is the reductive part of the triangular algebra and $n_+$ is its nilpotent radical.

## Nilpotence and the Index

**Theorem.** $n_+^{n}=0$ and $n_+^{n-1}\ne0$.

*Proof.* A product of $m$ strictly upper triangular matrices is a sum of products $E_{i_0i_1}E_{i_1i_2}\cdots E_{i_{m-1}i_m}$ with $i_0<i_1<\dots<i_m$, and such a chain has length at most $n-1$ because the indices run from $1$ to $n$ and increase. So every product of $n$ factors vanishes. For the second claim take the shift $N=\sum_{k=1}^{n-1}E_{k,k+1}$. Then $N^{m}=E_{1,m+1}$ for $m\le n-1$, so $N^{n-1}=E_{1n}\ne0$ and $N^{n}=0$.

**The index is exactly $n$, and the measurement agrees.** On the sum $N$ of all strictly upper matrix units, the powers had norm $1.7$ and then $0$ at $n=3$, and norms $2.4$, $2.4$, $1.0$ and then $0$ at $n=4$. The first vanishing power is the $n$-th in each case.

**Nilpotence is what makes the exponential a polynomial.** For $N\in n_+$ the series $\exp N=\sum_{m<n}N^{m}/m!$ is a finite sum, so $\exp$ is defined on $n_+$ without any convergence question, and its image lies in $UT_n$ with diagonal $\mathrm{I}$. The group $n_+$ generated this way is the unipotent radical of the triangular group.

## The Bracket of $n_+$ with Itself

**Proposition.** $[n_+,n_+]\subseteq n_+$, and the inclusion is strict for $n\ge3$.

*Proof.* Both products of two strictly upper triangular matrices are strictly upper triangular, so the bracket is. For strictness, count: $[E_{ij},E_{kl}]$ is nonzero only when $j=k$ or $l=i$, and for $i<j<k$ the only bracket that reaches the far corner is $[E_{ij},E_{jk}]=E_{ik}$. At $n=3$ the brackets of the three units span the single line $\mathbb{R}E_{13}$.

**Measured, the span of the brackets is short of the whole.** The brackets of the standard basis of $n_+$ span dimension $1$ out of $3$ at $n=3$, and dimension $3$ out of $6$ at $n=4$. At $n=2$ the span is $0$ out of $1$.

**The deficiency has a one-line cause.** A Lie algebra generated by one element is spanned by that element alone, since $[x,x]=0$, so it is abelian. For $n\ge3$ the algebra $n_+$ is not abelian, and its derived algebra is strictly smaller than itself.

**Iterating the bracket walks away from the diagonal.** The $m$-th term of the lower central series of $n_+$ is spanned by the units $E_{ij}$ with $j-i\ge m$, so each step removes one superdiagonal. The unit $E_{1n}$ survives to the last step, and the series reaches zero at $m=n$, which is the index.

## The Bracket of $n_+$ with $n_-$

**The bracket of the two triangular parts is not confined to the diagonal.** With $i<j$ and $k>l$,

$$
[E_{ij},E_{kl}]=\delta_{jk}E_{il}-\delta_{li}E_{kj},
$$

and the right-hand side lies in $h$ only when both indices meet, namely when $j=k$ and $i=l$, which is the pair $[E_{ij},E_{ji}]=E_{ii}-E_{jj}$.

**What the bracket spans has a diagonal part of dimension $n-1$.** The diagonal components are the differences $E_{ii}-E_{jj}$, and they span the trace-zero diagonal, of dimension $n-1$. Measured, that diagonal part has dimension $1$ at $n=2$, $2$ at $n=3$ and $3$ at $n=4$.

**The whole bracket is larger than its diagonal part.** Measured as the span of all brackets $[E_{ij},E_{kl}]$ with $i<j$ and $k>l$, the dimension is $1$ at $n=2$, $6$ at $n=3$ and $13$ at $n=4$. The remaining components lie in $n_+$ and in $n_-$: at $n=3$ the span is the diagonal of trace zero together with $E_{12}$, $E_{21}$, $E_{23}$, $E_{32}$.

**So the triangular decomposition is not a symmetric pair.** A symmetric pair needs $[n_+,n_-]\subseteq h$, and here the bracket leaves $h$ as soon as $n\ge3$. The pair that does satisfy the three inclusions is $(UT_n,n_+)$, and the pair $(\mathfrak{gl}_n(\mathbb{R}),\mathfrak{so}(n))$ of *Symmetric Pairs and Cartan Pairs: the Reductivity Criterion over $\mathbb{R}$* is another.

**The correct statement about $[n_+,n_-]$ is therefore an inclusion into the whole algebra, with a diagonal shadow of dimension $n-1$.** The shadow is what the trace detects: the trace of a bracket is zero, so every diagonal component has trace zero.

## Abelian Only at $n\le2$

**Proposition.** $n_+$ is abelian if and only if $n\le2$.

*Proof.* $n_+$ has dimension $n(n-1)/2$, which is $0$ for $n=1$ and $1$ for $n=2$; a space of dimension at most one is abelian. For $n\ge3$ the units $E_{12}$ and $E_{23}$ are in $n_+$ and $[E_{12},E_{23}]=E_{13}\ne0$, so $n_+$ is not abelian.

**The same holds for $n_-$, by transposition.** The transpose exchanges $n_+$ and $n_-$ and changes the sign of the bracket, so the two are abelian at the same orders.

**The measurement at $n=2$ gives the value zero.** The bracket span has dimension $0$ at $n=2$ and dimension $1$ at $n=3$, which is the statement in numbers.

**The first non-abelian case is $n=3$, and it is the smallest nilpotent Heisenberg-like example.** There $n_+$ has basis $E_{12}$, $E_{23}$, $E_{13}$ with $[E_{12},E_{23}]=E_{13}$ and $E_{13}$ central, which is the three-dimensional Heisenberg algebra in upper triangular form.

## The Infinitesimal Bruhat and Iwasawa Picture

**The quotient $\mathfrak{gl}_n(\mathbb{R})/(h\oplus n_+)$ is $n_-$.** The subspace $h\oplus n_+$ is the Lie algebra of the stabiliser of the flag, of dimension $n(n+1)/2$, so the quotient has dimension $n^{2}-n(n+1)/2=n(n-1)/2$, which is the dimension of $n_-$. The map $n_-\to\mathfrak{gl}_n/(h\oplus n_+)$ is an isomorphism of vector spaces, and it identifies $n_-$ with the tangent space of the flag variety $\mathrm{GL}_n(\mathbb{R})/UT_n$ at the base point.

**This is the infinitesimal Bruhat statement.** The flag variety has dimension $n(n-1)/2$, and the tangent space at the base point is the strictly lower triangular part, whose entries are the $n(n-1)/2$ coordinates of a first-order deformation of the flag.

**The Iwasawa decomposition of the Lie algebra uses the other triangular part.** With $\mathfrak{k}=\mathfrak{so}(n)=\operatorname{Skew}_n$, $\mathfrak{a}=h$ and $\mathfrak{n}=n_+$,

$$
\mathfrak{gl}_n(\mathbb{R})=\mathfrak{k}\oplus\mathfrak{a}\oplus\mathfrak{n},\qquad \frac{n(n-1)}{2}+n+\frac{n(n-1)}{2}=n^{2},
$$

and the measured dimension of the sum is $4$, $9$, $16$ at $n=2,3,4$. The three pieces are the compact part, the split part and the nilpotent part, and the antisymmetric half of *The Two Halves: Symmetric and Antisymmetric* is the compact one.

**The two triangular decompositions are mirror images.** $h\oplus n_+$ is the stabiliser of the flag and $h\oplus n_-$ the stabiliser of the opposite flag, built from $e_n,e_{n-1},\dots,e_1$. The intersection of the two is $h$, and the two nilpotent parts are exchanged by the transpose. So the algebra has two dual triangular readings of the same grading, and the diagonal is what they share.

## Summary

The standard flag has stabiliser $UT_n=h\oplus n_+$, of dimension $n+n(n-1)/2=n(n+1)/2$. The three pieces $h$, $n_+$ and $n_-$ have dimensions $n$, $n(n-1)/2$ and $n(n-1)/2$, and their direct sum is the whole algebra of dimension $n^{2}$, measured as $4$, $9$, $16$ at $n=2,3,4$. $UT_n$ is a subalgebra and $n_+$ is a nilpotent ideal of index $n$, with $n_+^{n}=0$ and $n_+^{n-1}\ne0$. The bracket $[n_+,n_+]$ is strictly smaller than $n_+$ for $n\ge3$, spanning $1$ of $3$ dimensions at $n=3$. The bracket $[n_+,n_-]$ is not contained in $h$: its diagonal part is the trace-zero diagonal of dimension $n-1$, and its whole span has dimension $1$, $6$, $13$ at $n=2,3,4$. The two triangular parts are abelian only at $n\le2$. The Iwasawa sum $\mathfrak{so}(n)\oplus h\oplus n_+$ is the algebra, and the quotient by $h\oplus n_+$ is the tangent space of the flag variety.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V_k$ | the span of $e_1,\dots,e_k$, the steps of the standard flag |
| $h$ | the diagonal subalgebra, of dimension $n$ |
| $n_+$ | the strictly upper triangular part, of dimension $n(n-1)/2$ |
| $n_-$ | the strictly lower triangular part, of dimension $n(n-1)/2$ |
| $UT_n=h\oplus n_+$ | the upper triangular algebra, the stabiliser of the flag |
| $N=\sum_k E_{k,k+1}$ | the shift, with $N^{n-1}=E_{1n}$ and $N^{n}=0$ |
| $[X,Y]=XY-YX$ | the commutator, under which $n_+$ is a nilpotent ideal |

## Further Reading

- James E. Humphreys, *Linear Algebraic Groups* (Springer, 1975), for the flag variety, the Borel subgroups and the Bruhat decomposition.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, 2002), for the Iwasawa decomposition at the level of Lie algebras.
- [The Fine Decomposition against the Diagonal](the-fine-decomposition-against-the-diagonal-over-r.html), for the lines that the triangular parts collect.
- [Symmetric Pairs and Cartan Pairs: the Reductivity Criterion over $\mathbb{R}$](symmetric-pairs-and-cartan-pairs-the-reductivity-criterion-over-r.html), for the pairs that do satisfy the three inclusions.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the matrix units and the trace.
