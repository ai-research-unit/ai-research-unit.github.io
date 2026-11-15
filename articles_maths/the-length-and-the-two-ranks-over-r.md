# __The Length and the Two Ranks__

## Introduction

**The length of an operator is the least number of two-sided operators whose sum it is, and it is a rank: the rank of the operator written in the basis of the $n^{2}$ matrix-unit two-sided operators.** So an operator carries two ranks. The first is the rank of the map on $\mathbb{R}^{n^{2}}$. The second is the length. The two are the ranks of two matrices that differ by a partial transposition, and neither bounds the other beyond the inequality $\text{length}\ge\operatorname{rank}/n^{2}$.

The article defines the length, proves that it equals the rank of the coefficient matrix, computes it for the identity operator, for the transpose and for the two-sided operators, gives the bound $\ell(T)\le n^{2}$ with equality on the complement of a hypersurface, and compares the count with the complex case. It assumes *The Two-Sided Operators and the Real Segre Cone* for the bilinear map $(A,B)\mapsto T_{A,B}$, its cone and its rank formula, and it defers the topology of the operator space to *The Symmetric and Antisymmetric Parts of the Operator Space*.

Throughout $n\ge2$, $M_n=M_n(\mathbb{R})$ and $\ell(T)$ is the length.

## The Definition

**Definition.** Let $T\in\operatorname{End}(M_n)$. The **length** $\ell(T)$ is the least integer $k$ such that

$$
T=T_{A_1,B_1}+\cdots+T_{A_k,B_k}
$$

for some $A_i,B_i\in M_n$. The length of the zero operator is $0$.

**The two-sided operator is the length-one case.** $\ell(T)=1$ exactly when $T=T_{A,B}$ for some nonzero pair, since a single summand is a two-sided operator. So the set of operators of length one is the real Segre cone of *The Two-Sided Operators and the Real Segre Cone*, minus the origin.

**The length is finite and at most $n^{2}$.** The $n^{2}$ operators $T_{E_{ij},E_{kl}}$, for fixed $(i,j)$ and varying $(k,l)$, already span the space of operators of the form $X\mapsto E_{ij}XC$. Hence every $T$ is a sum of $n^{2}$ two-sided operators, all with a left factor equal to a matrix unit. The bound is attained, as the transpose below shows.

## The Coefficient Matrix

**Definition.** Write $c_{(ij),(kl)}$ for the coefficient of $T_{E_{ij},E_{kl}}$ in $T$:

$$
T=\sum_{i,j,k,l}c_{(ij),(kl)}\,T_{E_{ij},E_{kl}} .
$$

The array $c$ is the **coefficient matrix** of $T$. It is an $n^{2}\times n^{2}$ matrix, with rows indexed by the pair $(i,j)$ and columns by the pair $(k,l)$, and it is unique because the $n^{4}$ operators $T_{E_{ij},E_{kl}}$ are a basis.

**The coefficient matrix is the operator in the basis of matrix units.** Evaluating on $X$,

$$
T(X)=\sum_{i,j,k,l}c_{(ij),(kl)}X_{jk}E_{il},
$$

because $E_{ij}XE_{kl}=X_{jk}E_{il}$. So the entries of $X$ enter with the middle index of the first factor and the first index of the second.

**The two-sided operators are exactly the coefficient matrices of rank one.** For $T_{A,B}$ the coefficient is $A_{ij}B_{kl}$, so

$$
c_{(ij),(kl)}=A_{ij}B_{kl},
$$

which is the outer product of the vector of entries of $A$ with the vector of entries of $B$. Conversely, a coefficient matrix of the form $c=uv^{\mathsf T}$ is the matrix of the two-sided operator $T_{A,B}$ with $A_{ij}=u_{ij}$ and $B_{kl}=v_{kl}$. So

$$
\{T_{A,B}\}=\{T:\operatorname{rank}c(T)=1\}\cup\{0\},
$$

which is the statement that the cone of the two-sided operators is the cone of the rank-one elements of the operator algebra.

## The Length Is a Matrix Rank

**Theorem.** $\ell(T)=\operatorname{rank}c(T)$.

*Proof.* A decomposition with $k$ summands gives $c(T)=\sum_{i\le k}u_iv_i^{\mathsf T}$, a sum of $k$ matrices of rank one, so $\operatorname{rank}c(T)\le k$ and hence $\operatorname{rank}c(T)\le\ell(T)$. Conversely let $c$ have rank $r$ and write $c=\sum_{i\le r}u_iv_i^{\mathsf T}$ with $u_i,v_i\in\mathbb{R}^{n^{2}}$. Reading $u_i$ and $v_i$ as matrices $A_i$ and $B_i$ gives $c=\sum_{i\le r}c(T_{A_i,B_i})$, and the coefficient matrix determines the operator, so $T=\sum_{i\le r}T_{A_i,B_i}$ and $\ell(T)\le r$.

**Three consequences follow at once.** The length is an integer between $0$ and $n^{2}$. It is one exactly on the cone of the two-sided operators. And it is a *rank*, so it obeys the semicontinuity of ranks: the sets $\{\ell\le k\}$ are closed, and they are the determinantal varieties of the coefficient matrix.

**The length is computed from the coefficients, not from the image.** The operator $T(X)=\operatorname{tr}(X)\mathrm{I}$ has rank one as a map on $\mathbb{R}^{n^{2}}$, and its coefficient matrix is $\sum_{i,j}E_{ij}\otimes E_{ij}$ read in the basis, of rank $n^{2}$. So $\ell=n^{2}$ for an operator of linear rank one. Measured at $n=3$, the coefficient rank is $9$ and the operator rank is $1$.

## The Two Ranks

**The two ranks are the ranks of two matrices.** The **linear rank** is $\operatorname{rk}T=\dim\operatorname{im}T$, the rank of the matrix of $T$ on $\mathbb{R}^{n^{2}}$. The **length** is $\ell(T)=\operatorname{rank}c(T)$. Both are ranks of $n^{2}\times n^{2}$ matrices, and the two matrices are partial transposes of each other: the entry of the operator matrix in the row $(i,l)$ and the column $(j,k)$ is the entry of $c(T)$ in the row $(i,j)$ and the column $(k,l)$. Passing from one to the other swaps $j$ and $l$, one index of the row with one index of the column.

**Partial transposition does not preserve rank.** For $T_{A,B}$ the first matrix is the Kronecker product $B^{\mathsf T}\otimes A$ and the second is the outer product of the entries of $A$ with the entries of $B$; the first has rank $(\operatorname{rk}A)(\operatorname{rk}B)$ and the second rank one. So the two ranks coincide on the cone and separate away from it.

**The comparison table at $n=3$.** Measured on four operators:

| Operator | Length | Linear rank |
|---|---|---|
| identity | $1$ | $9$ |
| transpose | $9$ | $9$ |
| $X\mapsto\operatorname{tr}(X)\mathrm{I}$ | $9$ | $1$ |
| random $T_{A,B}$ | $1$ | $9$ |

The table shows that the length and the linear rank are independent: each can be large while the other is small.

**One inequality holds in general.** Since $\operatorname{rank}T_{A,B}=(\operatorname{rk}A)(\operatorname{rk}B)\le n^{2}$ and the rank is subadditive,

$$
\operatorname{rk}T\le n^{2}\,\ell(T),\qquad\text{that is}\qquad \ell(T)\ge\frac{\operatorname{rk}T}{n^{2}} .
$$

The bound is attained by the transpose, where both sides are $n^{2}$, and it is far from attained by the identity, where the right side is $1$ and the left is $n^{2}$.

## The Identity and the Transpose

**The identity operator has length one.** $T_{\mathrm{I},\mathrm{I}}(X)=\mathrm{I}\,X\,\mathrm{I}=X$, so the identity is a single two-sided operator and $\ell(\operatorname{id})=1$. Its coefficient matrix is the outer product of the vector of entries of $\mathrm{I}$ with itself, of rank one. Measured at $n=2$ and $n=3$, the coefficient rank is $1$ in both cases and the linear rank is $n^{2}$.

**The matrix $\mathrm{I}$ is not the identity operator.** The matrix $\mathrm{I}$ is an element of $M_n$, and as a sum of rank-one matrices it needs $n$ terms: $\mathrm{I}=E_{11}+\cdots+E_{nn}$, with each $E_{ii}$ of rank one. That count is the length of the matrix in the module $M_n$, a different object from the length of the operator in $\operatorname{End}(M_n)$. The identity operator is one term, not $n$.

**The transpose has length $n^{2}$.** $\tau(X)=X^{\mathsf T}$ is

$$
\tau=\sum_{i,j}T_{E_{ij},E_{ij}},
$$

since $E_{ij}XE_{ij}=X_{ji}E_{ij}$ and the sum over $i,j$ reproduces $X^{\mathsf T}$. So $\ell(\tau)\le n^{2}$. For the lower bound, the coefficient matrix of $\tau$ has entries $\delta_{ik}\delta_{jl}$, which is the identity matrix of order $n^{2}$; its rank is $n^{2}$, and the theorem gives $\ell(\tau)=n^{2}$. Measured at $n=2$ and $n=3$, the coefficient rank is $4$ and $9$.

**The transpose is the extreme case.** It has the largest possible length, and its length equals its linear rank. It is also the operator whose coefficient matrix is the identity, so it is the case in which the basis of the two-sided operators and the operator itself are aligned.

## The Hypersurface of Shorter Length

**The operators of length less than $n^{2}$ form a hypersurface.** By the theorem, $\{\ell\le k\}$ is the set of operators whose coefficient matrix has rank at most $k$, the determinantal variety of dimension

$$
k(2n^{2}-k)
$$

inside $\mathbb{R}^{n^{4}}$. At $k=n^{2}-1$ the dimension is $(n^{2}-1)(n^{2}+1)=n^{4}-1$, a hypersurface, defined by $\det c=0$. So a generic operator has length exactly $n^{2}$: the length is maximal exactly when $\det c\ne0$.

**The generic value is the maximum.** The polynomial $\det c$ is not identically zero, since the transpose has $\det c=1$. Hence the complement of the hypersurface is a nonempty open set, dense in the operator space, and every operator in it has length $n^{2}$.

**The strata are the strata of a determinantal variety.** The operators of length at most $k$ have dimension $k(2n^{2}-k)$, and the operators of length exactly $k$ have dimension $k(2n^{2}-k)-(k-1)(2n^{2}-k+1)=2n^{2}-2k+1$. At $k=1$ this is $2n^{2}-1$, the dimension of the Segre cone, and at $k=n^{2}$ it is $1$, the open cone of the operators of full length.

## The Length over $\mathbb{C}$

**The length does not change under complexification.** The coefficient matrix of $T$ has real entries, and the rank of a real matrix is the same whether it is read over $\mathbb{R}$ or over $\mathbb{C}$: the rank is the largest order of a nonvanishing minor, and the minors are the same real polynomials. So $\ell_{\mathbb{C}}(T)=\ell_{\mathbb{R}}(T)$ for every real operator $T$, and the two-sided operators over $\mathbb{C}$ have length one as well.

**What changes is the geometry of the cone, not the count.** Over $\mathbb{C}$ the Segre cone has the same dimension $2n^{2}-1$ and the same rank-one locus, but the cone is the complex cone of a complex variety, and the real points of the rank-one locus are the products of real lines, as in *The Two-Sided Operators and the Real Segre Cone*.

**The count is a count of tensors.** The algebra $\operatorname{End}(M_n)$ is $M_n\otimes M_n^{\mathrm{op}}$, so a decomposition of $T$ into two-sided operators is a decomposition of a tensor into pure tensors. For a two-way tensor the least number of pure tensors is the rank of the tensor as a matrix, in any basis, and that number is the same over $\mathbb{R}$ and over $\mathbb{C}$.

## Summary

The length of $T\in\operatorname{End}(M_n(\mathbb{R}))$ is the least number of two-sided operators whose sum is $T$. It equals the rank of the coefficient matrix of $T$ in the basis $T_{E_{ij},E_{kl}}$, so it is an integer between $0$ and $n^{2}$. The two-sided operators are the operators of length one, the identity operator has length one, and the transpose has length $n^{2}$. The linear rank and the length are the ranks of two matrices related by a partial transposition, so neither bounds the other except through $\ell\ge\operatorname{rk}/n^{2}$. The operators of length below the maximum form the determinantal hypersurface $\{\det c=0\}$, so a generic operator has length $n^{2}$. The count is unchanged by complexification.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\ell(T)$ | the length, the least number of two-sided operators summing to $T$ |
| $T_{A,B}$ | the two-sided operator $X\mapsto AXB$ |
| $c(T)$ | the coefficient matrix of $T$ in the basis $T_{E_{ij},E_{kl}}$, of size $n^{2}\times n^{2}$ |
| $\operatorname{rk}T$ | the linear rank, the rank of $T$ as a map on $\mathbb{R}^{n^{2}}$ |
| $\tau$ | the transpose operator $X\mapsto X^{\mathsf T}$, of length $n^{2}$ |
| $k(2n^{2}-k)$ | the dimension of the operators of length at most $k$ |
| $\{\det c=0\}$ | the hypersurface of operators of length less than $n^{2}$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the tensor product $M_n\otimes M_n^{\mathrm{op}}$ and the decomposition into pure tensors.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the rank, the minors and the Kronecker product.
- [The Two-Sided Operators and the Real Segre Cone](the-two-sided-operators-and-the-real-segre-cone.html), for the cone, its rank formula and its two rulings.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the matrix units and the rank.
- [The Symmetric and Antisymmetric Parts of the Operator Space](the-symmetric-and-antisymmetric-parts-of-the-operator-space-over-r.html), for the decomposition of the operator space and its dimensions.
