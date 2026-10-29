# __The Spin of the Principal Pair of $M_4(\mathbb{C})$: A Worked Computation__

## Introduction

The table of cases in *The General Definition of Spin* has the following row.

| algebra | base field | pair | elementary spins | adjoint content |
|---|---|---|---|---|
| $M_4(\mathbb{C})$ | $\mathbb{C}$ | principal | $0,\tfrac32,3$ | $0,1,2,3$ |

This article computes every entry of the row.

### The Result

**The spin of $\mathbb{C}^4$ is $\tfrac32$.** The defining module is the space of columns, and $S$ has eigenvalues $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$.

**The spin of $\mathbb{C}I$ is $0$.** The centre is fixed by the adjoint action.

**The spin of $\mathfrak{sl}_4$ is $3$.** The traceless part is irreducible under the adjoint action, and its largest $S$-weight is $3$, on the unit $E_{14}$.

**The adjoint content is $0,1,2,3$.** As a module for the triple, $\mathfrak{gl}_4=W_0\oplus W_1\oplus W_2\oplus W_3$, of dimensions $1+3+5+7=16$.

| carrier | action | dimension | spin |
|---|---|---|---|
| $\mathbb{C}^4$ | left multiplication | $4$ | $\tfrac32$ |
| $\mathbb{C}I$ | adjoint | $1$ | $0$ |
| $\mathfrak{sl}_4$ | adjoint | $15$ | $3$ |
| $\mathfrak{gl}_4$ | adjoint | $16$ | content $0,1,2,3$ |

The elementary list and the content are different sets: $\{0,\tfrac32,3\}$ against $\{0,1,2,3\}$. Only $0$ and $3$ are shared.

### The Difference From $M_3(\mathbb{C})$

At $n=3$ the two columns of the row coincide; at $n=4$ they do not. The reason is arithmetic. The defining spin is $(n-1)/2$, which is an integer exactly when $n$ is odd. The adjoint content is always the integers $0,\dots,n-1$. For $n=4$ the half-integer $\tfrac32$ enters the list, and the interval $0,1,2,3$ enters the content, and the two sets separate.

## The Pair

### The Three Matrices

For $n=4$ the principal pair is

$$
S=\operatorname{diag}\left(\tfrac32,\tfrac12,-\tfrac12,-\tfrac32\right),\qquad
U=\sqrt3\,E_{12}+2E_{23}+\sqrt3\,E_{34},\qquad
V=\sqrt3\,E_{21}+2E_{32}+\sqrt3\,E_{43}.
$$

The coefficients are $\sqrt{k(4-k)}$: $\sqrt3,2,\sqrt3$ for $k=1,2,3$.

### The Three Relations

$S$ has entries $s_i=\tfrac52-i$, so on a matrix unit $[S,E_{ij}]=(s_i-s_j)E_{ij}=(j-i)E_{ij}$. Hence $[S,E_{k,k+1}]=E_{k,k+1}$ and $[S,E_{k+1,k}]=-E_{k+1,k}$, and summing with the coefficients gives

$$
[S,U]=U,\qquad [S,V]=-V.
$$

For the third relation, the products of the ladders are diagonal:

$$
UV=\sum_{k=1}^{3}c_k^2E_{kk}=\operatorname{diag}(3,4,3,0),\qquad
VU=\sum_{k=1}^{3}c_k^2E_{k+1,k+1}=\operatorname{diag}(0,3,4,3),
$$

with $c_k=\sqrt{k(4-k)}$. The difference is

$$
[U,V]=\operatorname{diag}(3,1,-1,-3)=2S.
$$

**Result.** The pair satisfies the three relations with zero residual. The diagonal entries of $[U,V]$ are $c_1^2,c_2^2-c_1^2,c_3^2-c_2^2,-c_3^2$, which are twice the entries of $S$.

## The Defining Module: Spin $\tfrac32$

On $\mathbb{C}^4$ with basis $e_1,\dots,e_4$,

$$
Se_1=\tfrac32e_1,\quad Se_2=\tfrac12e_2,\quad Se_3=-\tfrac12e_3,\quad Se_4=-\tfrac32e_4.
$$

The weights are $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$; their sum is $0$. They form one string, which is the weight string of $W_{3/2}$.

**Result.** The defining module is $W_{3/2}$, and its spin is $\tfrac32$.

## The Adjoint Action

With the conventions $c_0=c_4=0$ and $c_k=\sqrt{k(4-k)}$, the two ladders act on the matrix units by

$$
\operatorname{ad}_U(E_{ij})=c_{i-1}E_{i-1,j}-c_jE_{i,j+1},\qquad
\operatorname{ad}_V(E_{ij})=c_iE_{i+1,j}-c_{j-1}E_{i,j-1}.
$$

The formula is read from $UE_{ij}=c_{i-1}E_{i-1,j}$, $E_{ij}U=c_jE_{i,j+1}$, $VE_{ij}=c_iE_{i+1,j}$ and $E_{ij}V=c_{j-1}E_{i,j-1}$, each a single unit. Three rows show the pattern.

| $(i,j)$ | $\operatorname{ad}_U(E_{ij})$ | $\operatorname{ad}_V(E_{ij})$ |
|---|---|---|
| $(1,1)$ | $-\sqrt3\,E_{12}$ | $\sqrt3\,E_{21}$ |
| $(1,4)$ | $0$ | $\sqrt3\,(E_{24}-E_{13})$ |
| $(4,4)$ | $\sqrt3\,E_{34}$ | $-\sqrt3\,E_{43}$ |

The zero at $(1,4)$ is structural: $E_{14}$ is a highest weight vector, killed by every raising step. The unit $E_{41}$ is the lowest weight vector, killed by every lowering step.

### The Weights

Since $S$ is diagonal, $\operatorname{ad}_S(E_{ij})=(j-i)E_{ij}$. The weights are the integers $j-i$ with $\lvert j-i\rvert\le3$, and the multiplicity of $m$ is the number of pairs with $j-i=m$, which is $4-\lvert m\rvert$:

| $m$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|---|---|---|
| $\mu(m)$ | $1$ | $2$ | $3$ | $4$ | $3$ | $2$ | $1$ |

The multiplicities sum to $16$.

### The Content

With $\mu(m)$ as above and the multiplicity formula $m_j=\mu(j)-\mu(j+1)$,

$$
m_0=4-3=1,\qquad m_1=3-2=1,\qquad m_2=2-1=1,\qquad m_3=1-0=1.
$$

**Result.** $\mathfrak{gl}_4\cong W_0\oplus W_1\oplus W_2\oplus W_3$, of dimensions $1+3+5+7=16$. The adjoint content is $0,1,2,3$.

## The Four Chains

### The Highest Weight Vectors

A highest weight vector of weight $j$ satisfies $\operatorname{ad}_Sh=jh$ and $\operatorname{ad}_Uh=0$. The four are

$$
h_0=I,\qquad h_1=E_{12}+\tfrac{2}{\sqrt3}E_{23}+E_{34},\qquad h_2=E_{13}+E_{24},\qquad h_3=E_{14}.
$$

The coefficients of $h_1$ are forced by $\operatorname{ad}_Uh_1=0$: the coefficient of $E_{13}$ is $c_1a_2-c_2a_1=2-2=0$ with $a_1=a_3=1$ and $a_2=2/\sqrt3$, and the coefficient of $E_{24}$ is $c_2a_3-c_3a_2=2-2=0$. For $h_2$ the two raising steps cancel, since $c_1=c_3=\sqrt3$.

### The Chains

Applying $\operatorname{ad}_V$:

| $j$ | chain length |
|---|---|
| $0$ | $1$ |
| $1$ | $3$ |
| $2$ | $5$ |
| $3$ | $7$ |

The lengths are $2j+1$, the dimensions of $W_j$. The chain of $h_3=E_{14}$ begins

$$
E_{14}\mapsto\sqrt3\,(E_{24}-E_{13})\mapsto 2\sqrt3\,(E_{12}-\sqrt3\,E_{23}+E_{34}).
$$

### Independence

The $16$ chain vectors, ordered by $j$ and then by lowering, form a basis of $\mathfrak{gl}_4$. In the basis order $(E_{11},E_{12},\dots,E_{44})$ the determinant of the matrix of columns is

$$
-2^{28}3^{8}5^{5}\neq0.
$$

**Result.** The chains are independent and their sum is direct:

$$
\mathfrak{gl}_4=W_0\oplus W_1\oplus W_2\oplus W_3.
$$

## The Adjoint Carriers

The $\operatorname{ad}(M_4(\mathbb{C}))$-stable subspaces are the ideals $0$, $\mathbb{C}I$, $\mathfrak{sl}_4$ and $\mathfrak{gl}_4$; the irreducible ones are $\mathbb{C}I$ and $\mathfrak{sl}_4$.

The centre has spin $0$. On $\mathfrak{sl}_4$ the weights are those of the $16$ units minus one diagonal unit of weight $0$:

| $m$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|---|---|---|
| $\mu_{\mathfrak{sl}_4}(m)$ | $1$ | $2$ | $3$ | $3$ | $3$ | $2$ | $1$ |

Hence $m_0=3-3=0$, $m_1=3-2=1$, $m_2=2-1=1$, $m_3=1-0=1$, so

$$
\mathfrak{sl}_4=W_1\oplus W_2\oplus W_3,
$$

of dimensions $3+5+7=15$. The top weight is $3$.

**Result.** The adjoint elementary carriers are $\mathbb{C}I$ (spin $0$) and $\mathfrak{sl}_4$ (spin $3$).

### The List

| carrier | action | dimension | content | spin |
|---|---|---|---|---|
| $\mathbb{C}^4$ | left multiplication | $4$ | $W_{3/2}$ | $\tfrac32$ |
| $\mathbb{C}I$ | adjoint | $1$ | $W_0$ | $0$ |
| $\mathfrak{sl}_4$ | adjoint | $15$ | $W_1\oplus W_2\oplus W_3$ | $3$ |

**Result.** The elementary spin list is $\Sigma=\{0,\tfrac32,3\}$.

**Remark (the two $3$'s).** The $3$ of the list is the spin of the whole traceless part. The $3$ of the content is the top summand $W_3$ inside it. They are the same number attached to different objects.

## The Two Actions on the Algebra

**Left multiplication.** $SE_{ij}=s_iE_{ij}$ with $s_i=\tfrac52-i$, independent of $j$. Each weight $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$ occurs with multiplicity $4$, so

$$
M_4(\mathbb{C})=4W_{3/2},
$$

with spin $\tfrac32$.

**The adjoint action.** $\operatorname{ad}_S(E_{ij})=(j-i)E_{ij}$, which gives $W_0\oplus W_1\oplus W_2\oplus W_3$.

**Result.** The left module sees only the defining spin; the adjoint sees the whole interval. The row uses both actions.

## Checks

### The Casimir

On $\mathbb{C}^4$,

$$
C=S^2+\tfrac12(UV+VU)=\tfrac{15}{4}I,
$$

and $\tfrac{15}{4}=j(j+1)$ for $j=\tfrac32$.

On $\mathfrak{gl}_4$ the characteristic polynomial of the image of $C$ is

$$
\lambda(\lambda-12)^7(\lambda-6)^5(\lambda-2)^3.
$$

The eigenvalues are $0,2,6,12$, which are $j(j+1)$ for $j=0,1,2,3$, with multiplicities $1,3,5,7$.

**Result.** The Casimir recovers the content $0,1,2,3$ without counting weights.

### The Table of Checks

| check | result |
|---|---|
| $[S,U]-U$ | $0$ |
| $[S,V]+V$ | $0$ |
| $[U,V]-2S$ | $0$ |
| $\sum_m\mu(m)$ | $16$ |
| $(m_0,m_1,m_2,m_3)$ | $(1,1,1,1)$ |
| chain lengths | $1,3,5,7$ |
| determinant of the $16$ vectors | $-2^{28}3^85^5$ |
| characteristic polynomial on $\mathfrak{gl}_4$ | $\lambda(\lambda-12)^7(\lambda-6)^5(\lambda-2)^3$ |
| $\rho_{3/2}(C)$ | $\tfrac{15}{4}I$ |

## Summary

- The pair is $S=\operatorname{diag}(\tfrac32,\tfrac12,-\tfrac12,-\tfrac32)$, $U=\sqrt3E_{12}+2E_{23}+\sqrt3E_{34}$, $V=U^{\mathsf T}$.
- It satisfies the three relations; $[U,V]=\operatorname{diag}(3,1,-1,-3)=2S$.
- The defining module is $W_{3/2}$, of spin $\tfrac32$.
- The adjoint weights are $j-i$ with multiplicities $1,2,3,4,3,2,1$; the content is $0,1,2,3$.
- The highest weight vectors are $I$, $E_{12}+\tfrac{2}{\sqrt3}E_{23}+E_{34}$, $E_{13}+E_{24}$, $E_{14}$; the chains have lengths $1,3,5,7$ and are independent.
- The elementary carriers are $\mathbb{C}I$ (spin $0$), $\mathbb{C}^4$ (spin $\tfrac32$) and $\mathfrak{sl}_4$ (spin $3$); the list is $0,\tfrac32,3$.
- The list and the content differ at $n=4$: the half-integer $\tfrac32$ is not in the content, and $1,2$ are not in the list.
- The Casimir is $\tfrac{15}{4}I$ on $\mathbb{C}^4$, with eigenvalues $0,2,6,12$ on $\mathfrak{gl}_4$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $M_4(\mathbb{C})$ | matrix algebra, $1$-based indices |
| $E_{ij}$ | matrix unit |
| $c_k$ | $\sqrt{k(4-k)}$, the ladder coefficient |
| $S$ | spin element $\operatorname{diag}(\tfrac32,\tfrac12,-\tfrac12,-\tfrac32)$ |
| $U,V$ | ladders $U^{\mathsf T}=V$ |
| $\operatorname{ad}_X$ | $Y\mapsto XY-YX$ |
| $W_j$ | irreducible carrier, dimension $2j+1$ |
| $\mu(m)$ | multiplicity of the weight $m$ |
| $m_j$ | multiplicity of $W_j$ |
| $h_j$ | highest weight vector of weight $j$ |
| $C$ | Casimir element $S^2+\tfrac12(UV+VU)$ |

## Further Reading

- [The General Definition of Spin](../articles_maths/the-general-definition-of-spin.html), for the definition and the table of cases.
- [The Spin Chain and the Adjoint Decomposition of $M_4(\mathbb{C})$](../articles_maths/the-spin-chain-and-the-adjoint-decomposition-of-m4c.html), for the adjoint decomposition.
- [The Spin of the Principal Pair of $M_3(\mathbb{C})$](the-principal-pair-of-m3c-a-worked-computation.html), for the case where the two columns agree.
- [Representations of Lie Algebras](../articles_maths/representations-of-lie-algebras.html), for the highest weight classification.
- [The Casimir Operator](../articles_maths/the-casimir-operator.html), for the eigenvalue $j(j+1)$.
