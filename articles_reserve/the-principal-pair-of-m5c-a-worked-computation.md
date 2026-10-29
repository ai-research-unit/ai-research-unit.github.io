# __The Spin of the Principal Pair of $M_5(\mathbb{C})$: A Worked Computation__

## Introduction

The table of cases in *The General Definition of Spin* has the following row.

| algebra | base field | pair | elementary spins | adjoint content |
|---|---|---|---|---|
| $M_5(\mathbb{C})$ | $\mathbb{C}$ | principal | $0,2,4$ | $0,1,2,3,4$ |

This article computes every entry of the row.

### The Result

**The spin of $\mathbb{C}^5$ is $2$.** The defining module has weights $2,1,0,-1,-2$.

**The spin of $\mathbb{C}I$ is $0$.** The centre is fixed by the adjoint action.

**The spin of $\mathfrak{sl}_5$ is $4$.** The traceless part is irreducible under the adjoint action, and its largest $S$-weight is $4$, on the unit $E_{15}$.

**The adjoint content is $0,1,2,3,4$.** As a module for the triple, $\mathfrak{gl}_5=W_0\oplus W_1\oplus W_2\oplus W_3\oplus W_4$, of dimensions $1+3+5+7+9=25$.

| carrier | action | dimension | spin |
|---|---|---|---|
| $\mathbb{C}^5$ | left multiplication | $5$ | $2$ |
| $\mathbb{C}I$ | adjoint | $1$ | $0$ |
| $\mathfrak{sl}_5$ | adjoint | $24$ | $4$ |
| $\mathfrak{gl}_5$ | adjoint | $25$ | content $0,1,2,3,4$ |

The list $\{0,2,4\}$ is contained in the content $\{0,1,2,3,4\}$: every elementary spin is also a summand of the adjoint, and the content has the two extra values $1,3$. The containment is a property of odd $n$: the defining spin $(n-1)/2$ is an integer in the interval $0,\dots,n-1$.

### What Changes From $M_3(\mathbb{C})$

At $n=3$ every integer $0,1,2$ occurs both as an elementary carrier and as a summand of the adjoint. At $n=5$ the interval $0,\dots,4$ has five values, but there are only three elementary carriers. The reason is that the traceless part $\mathfrak{sl}_5$ is irreducible under $\operatorname{ad}(M_5(\mathbb{C}))$: it contains the summands $W_1,W_2,W_3,W_4$ of the triple, but they are components of one carrier, not four carriers. Its spin is the top one, $4$.

## The Pair

### The Three Matrices

For $n=5$ the principal pair is

$$
S=\operatorname{diag}(2,1,0,-1,-2),\qquad
U=2E_{12}+\sqrt6\,E_{23}+\sqrt6\,E_{34}+2E_{45},\qquad
V=2E_{21}+\sqrt6\,E_{32}+\sqrt6\,E_{43}+2E_{54}.
$$

The coefficients are $\sqrt{k(5-k)}$: $2,\sqrt6,\sqrt6,2$ for $k=1,2,3,4$.

### The Three Relations

$S$ has entries $s_i=3-i$, so $[S,E_{ij}]=(j-i)E_{ij}$, and $[S,E_{k,k+1}]=E_{k,k+1}$, $[S,E_{k+1,k}]=-E_{k+1,k}$. Summing gives

$$
[S,U]=U,\qquad [S,V]=-V.
$$

The products of the ladders are diagonal:

$$
UV=\sum_{k=1}^{4}c_k^2E_{kk}=\operatorname{diag}(4,6,6,4,0),\qquad
VU=\sum_{k=1}^{4}c_k^2E_{k+1,k+1}=\operatorname{diag}(0,4,6,6,4),
$$

and their difference is

$$
[U,V]=\operatorname{diag}(4,2,0,-2,-4)=2S.
$$

**Result.** The pair satisfies the three relations with zero residual. The entries of $[U,V]$ are $c_k^2-c_{k-1}^2$, with $c_0=c_5=0$, which is $6-2k=2(3-k)$, twice the $k$-th entry of $S$.

## The Defining Module: Spin $2$

On $\mathbb{C}^5$,

$$
Se_k=(3-k)e_k,\qquad k=1,\dots,5,
$$

so the weights are $2,1,0,-1,-2$. They form one string, which is the weight string of $W_2$.

**Result.** The defining module is $W_2$, and its spin is $2$.

## The Adjoint Action

With $c_0=c_5=0$ and $c_k=\sqrt{k(5-k)}$,

$$
\operatorname{ad}_U(E_{ij})=c_{i-1}E_{i-1,j}-c_jE_{i,j+1},\qquad
\operatorname{ad}_V(E_{ij})=c_iE_{i+1,j}-c_{j-1}E_{i,j-1}.
$$

Three rows show the pattern.

| $(i,j)$ | $\operatorname{ad}_U(E_{ij})$ | $\operatorname{ad}_V(E_{ij})$ |
|---|---|---|
| $(1,1)$ | $-2E_{12}$ | $2E_{21}$ |
| $(1,5)$ | $0$ | $2\,(E_{25}-E_{14})$ |
| $(5,5)$ | $2E_{45}$ | $-2E_{54}$ |

The unit $E_{15}$ is killed by $\operatorname{ad}_U$, and $E_{51}$ is killed by $\operatorname{ad}_V$.

### The Weights

The weight of $E_{ij}$ is $j-i$, an integer with $\lvert j-i\rvert\le4$, and the multiplicity of $m$ is $5-\lvert m\rvert$:

| $m$ | $-4$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|---|---|---|---|---|
| $\mu(m)$ | $1$ | $2$ | $3$ | $4$ | $5$ | $4$ | $3$ | $2$ | $1$ |

The multiplicities sum to $25$.

### The Content

With $m_j=\mu(j)-\mu(j+1)$,

$$
m_0=5-4=1,\quad m_1=4-3=1,\quad m_2=3-2=1,\quad m_3=2-1=1,\quad m_4=1-0=1.
$$

**Result.** $\mathfrak{gl}_5\cong W_0\oplus W_1\oplus W_2\oplus W_3\oplus W_4$, of dimensions $1+3+5+7+9=25$. The adjoint content is $0,1,2,3,4$.

## The Five Chains

### The Highest Weight Vectors

A highest weight vector of weight $j$ satisfies $\operatorname{ad}_Sh=jh$ and $\operatorname{ad}_Uh=0$. The five are

$$
h_0=I,\quad
h_1=E_{12}+\tfrac{\sqrt6}{2}E_{23}+\tfrac{\sqrt6}{2}E_{34}+E_{45},\quad
h_2=E_{13}+\tfrac{\sqrt6}{2}E_{24}+E_{35},\quad
h_3=E_{14}+E_{25},\quad
h_4=E_{15}.
$$

The coefficients are fixed by the cancellation of consecutive raising steps. In $h_1$ the ratio $a_{i+1}/a_i=c_{i+1}/c_i$ takes the values $\tfrac{\sqrt6}{2},1,\tfrac{\sqrt6}{3}$, so the coefficients are $1,\tfrac{\sqrt6}{2},\tfrac{\sqrt6}{2},1$. In $h_2$ the ratios are $\tfrac{\sqrt6}{2},\tfrac{\sqrt6}{3}$, so the coefficients are $1,\tfrac{\sqrt6}{2},1$. In $h_3$ the ratio is $1$, so the coefficients are $1,1$.

### The Chains

Applying $\operatorname{ad}_V$ gives chains of lengths $2j+1$:

| $j$ | chain length |
|---|---|
| $0$ | $1$ |
| $1$ | $3$ |
| $2$ | $5$ |
| $3$ | $7$ |
| $4$ | $9$ |

The top chain begins

$$
E_{15}\mapsto 2(E_{25}-E_{14})\mapsto 2\sqrt6\,\left(E_{13}-\tfrac{2\sqrt6}{3}E_{24}+E_{35}\right).
$$

### Independence

The $25$ chain vectors, ordered by $j$ and then by lowering, form a basis of $\mathfrak{gl}_5$. In the basis order $(E_{11},E_{12},\dots,E_{55})$ the determinant of the matrix of columns is

$$
-2^{55}3^{18}5^{10}7^{7}\sqrt6\neq0.
$$

**Result.** The chains are independent and their sum is direct:

$$
\mathfrak{gl}_5=W_0\oplus W_1\oplus W_2\oplus W_3\oplus W_4.
$$

## The Adjoint Carriers

The $\operatorname{ad}(M_5(\mathbb{C}))$-stable subspaces are the ideals $0$, $\mathbb{C}I$, $\mathfrak{sl}_5$ and $\mathfrak{gl}_5$; the irreducible ones are $\mathbb{C}I$ and $\mathfrak{sl}_5$.

The centre has spin $0$. On $\mathfrak{sl}_5$ the weights are those of the $25$ units minus one diagonal unit of weight $0$:

| $m$ | $-4$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|---|---|---|---|---|
| $\mu_{\mathfrak{sl}_5}(m)$ | $1$ | $2$ | $3$ | $4$ | $4$ | $4$ | $3$ | $2$ | $1$ |

Hence $m_0=4-4=0$, $m_1=4-3=1$, $m_2=3-2=1$, $m_3=2-1=1$, $m_4=1-0=1$, so

$$
\mathfrak{sl}_5=W_1\oplus W_2\oplus W_3\oplus W_4,
$$

of dimensions $3+5+7+9=24$. The top weight is $4$.

**Result.** The adjoint elementary carriers are $\mathbb{C}I$ (spin $0$) and $\mathfrak{sl}_5$ (spin $4$).

### The List

| carrier | action | dimension | content | spin |
|---|---|---|---|---|
| $\mathbb{C}^5$ | left multiplication | $5$ | $W_2$ | $2$ |
| $\mathbb{C}I$ | adjoint | $1$ | $W_0$ | $0$ |
| $\mathfrak{sl}_5$ | adjoint | $24$ | $W_1\oplus W_2\oplus W_3\oplus W_4$ | $4$ |

**Result.** The elementary spin list is $\Sigma=\{0,2,4\}$.

**Remark (the shared $2$).** The $2$ of the list is the defining module. The $2$ of the content is the summand $W_2$ inside $\mathfrak{sl}_5$. The traceless part contains a copy of the defining module as a triple module, but the two carriers are different objects: one is a column space under left multiplication, the other a subspace of matrices under the commutator.

## The Two Actions on the Algebra

**Left multiplication.** $SE_{ij}=s_iE_{ij}$ with $s_i=3-i$, independent of $j$. Each weight $2,1,0,-1,-2$ occurs with multiplicity $5$, so

$$
M_5(\mathbb{C})=5W_2,
$$

with spin $2$.

**The adjoint action.** $\operatorname{ad}_S(E_{ij})=(j-i)E_{ij}$, which gives $W_0\oplus W_1\oplus W_2\oplus W_3\oplus W_4$.

**Result.** The left module is five copies of the defining module; the adjoint is the full interval. The row uses both.

## Checks

### The Casimir

On $\mathbb{C}^5$,

$$
C=S^2+\tfrac12(UV+VU)=6I,
$$

and $6=j(j+1)$ for $j=2$.

On $\mathfrak{gl}_5$ the characteristic polynomial of the image of $C$ is

$$
\lambda(\lambda-20)^9(\lambda-12)^7(\lambda-6)^5(\lambda-2)^3.
$$

The eigenvalues are $0,2,6,12,20$, which are $j(j+1)$ for $j=0,1,2,3,4$, with multiplicities $1,3,5,7,9$.

**Result.** The Casimir recovers the content $0,1,2,3,4$ without counting weights.

### The Table of Checks

| check | result |
|---|---|
| $[S,U]-U$ | $0$ |
| $[S,V]+V$ | $0$ |
| $[U,V]-2S$ | $0$ |
| $\sum_m\mu(m)$ | $25$ |
| $(m_0,\dots,m_4)$ | $(1,1,1,1,1)$ |
| chain lengths | $1,3,5,7,9$ |
| determinant of the $25$ vectors | $-2^{55}3^{18}5^{10}7^7\sqrt6$ |
| characteristic polynomial on $\mathfrak{gl}_5$ | $\lambda(\lambda-20)^9(\lambda-12)^7(\lambda-6)^5(\lambda-2)^3$ |
| $\rho_2(C)$ | $6I$ |

## Summary

- The pair is $S=\operatorname{diag}(2,1,0,-1,-2)$, $U=2E_{12}+\sqrt6E_{23}+\sqrt6E_{34}+2E_{45}$, $V=U^{\mathsf T}$.
- It satisfies the three relations; $[U,V]=\operatorname{diag}(4,2,0,-2,-4)=2S$.
- The defining module is $W_2$, of spin $2$.
- The adjoint weights are $j-i$ with multiplicities $1,2,3,4,5,4,3,2,1$; the content is $0,1,2,3,4$.
- The highest weight vectors are $I$, $h_1,h_2,h_3,h_4$ as above; the chains have lengths $1,3,5,7,9$ and are independent.
- The elementary carriers are $\mathbb{C}I$ (spin $0$), $\mathbb{C}^5$ (spin $2$) and $\mathfrak{sl}_5$ (spin $4$); the list is $0,2,4$.
- The list has three values; the content has five. The components $W_1,W_3$ of $\mathfrak{sl}_5$ are not separate carriers.
- The Casimir is $6I$ on $\mathbb{C}^5$, with eigenvalues $0,2,6,12,20$ on $\mathfrak{gl}_5$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $M_5(\mathbb{C})$ | matrix algebra, $1$-based indices |
| $E_{ij}$ | matrix unit |
| $c_k$ | $\sqrt{k(5-k)}$, the ladder coefficient |
| $S$ | spin element $\operatorname{diag}(2,1,0,-1,-2)$ |
| $U,V$ | ladders $U^{\mathsf T}=V$ |
| $\operatorname{ad}_X$ | $Y\mapsto XY-YX$ |
| $W_j$ | irreducible carrier, dimension $2j+1$ |
| $\mu(m)$ | multiplicity of the weight $m$ |
| $m_j$ | multiplicity of $W_j$ |
| $h_j$ | highest weight vector of weight $j$ |
| $C$ | Casimir element $S^2+\tfrac12(UV+VU)$ |

## Further Reading

- [The General Definition of Spin](../articles_maths/the-general-definition-of-spin.html), for the definition and the table of cases.
- [The Spin Chain and the Adjoint Decomposition of $M_5(\mathbb{C})$](../articles_maths/the-spin-chain-and-the-adjoint-decomposition-of-m5c.html), for the adjoint decomposition.
- [The Spin Two Chain and the Adjoint of $M_5(\mathbb{C})$](../articles_maths/the-spin-two-chain-and-the-adjoint-of-m5c.html), for the spin-two carrier.
- [The Spin of the Principal Pair of $M_3(\mathbb{C})$](the-principal-pair-of-m3c-a-worked-computation.html), for the case where the list and the content agree.
- [Representations of Lie Algebras](../articles_maths/representations-of-lie-algebras.html), for the highest weight classification.
- [The Casimir Operator](../articles_maths/the-casimir-operator.html), for the eigenvalue $j(j+1)$.
