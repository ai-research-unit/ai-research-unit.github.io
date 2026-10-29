# __The Spin of the Principal Pair of $M_2(\mathbb{C})$: A Worked Computation__

## Introduction

The table of cases in *The General Definition of Spin* has the following row.

| algebra | base field | pair | elementary spins | adjoint content |
|---|---|---|---|---|
| $M_2(\mathbb{C})$ | $\mathbb{C}$ | principal | $0,\tfrac12,1$ | $0,1$ |

This article computes every entry of the row. The result is stated first, then derived.

### The Result

**The spin of $\mathbb{C}^2$ is $\tfrac12$.** The defining module is the space of columns. The spin element $S$ acts diagonally, with eigenvalues $\tfrac12,-\tfrac12$.

**The spin of $\mathbb{C}I$ is $0$.** The centre is fixed by the adjoint action.

**The spin of $\mathfrak{sl}_2$ is $1$.** The traceless part is irreducible under the adjoint action, and its largest $S$-weight is $1$, on the unit $E_{12}$.

**The adjoint content is $0,1$.** As a module for the triple, $\mathfrak{gl}_2=W_0\oplus W_1$, of dimensions $1+3=4$.

| carrier | action | dimension | spin |
|---|---|---|---|
| $\mathbb{C}^2$ | left multiplication | $2$ | $\tfrac12$ |
| $\mathbb{C}I$ | adjoint | $1$ | $0$ |
| $\mathfrak{sl}_2$ | adjoint | $3$ | $1$ |
| $\mathfrak{gl}_2$ | adjoint | $4$ | content $0,1$ |

The last line records the decomposition of the adjoint module. It is not a fourth elementary carrier.

**The list and the content differ at $n=2$.** The elementary list is $\{0,\tfrac12,1\}$, with three values; the adjoint content is $\{0,1\}$, with two. The value $\tfrac12$ belongs to the defining module, not to the adjoint.

### Why This Row Is the Biquaternion's Row

At $n=2$ the principal pair is also the balanced Peirce pair of the idempotent $e=\operatorname{diag}(1,0)$: $S=e-\tfrac12$, $U=E_{12}$, $V=E_{21}$. It is therefore the frame pair of the biquaternion $\mathbb{B}\cong M_2(\mathbb{C})$. The row above is the matrix form of *The Spin of a Biquaternion*.

## The Pair

### The Three Matrices

For $n=2$ the principal pair of $M_2(\mathbb{C})$ is

$$
S=\operatorname{diag}\left(\tfrac12,-\tfrac12\right),\qquad U=E_{12},\qquad V=E_{21}.
$$

Explicitly,

$$
S=\begin{pmatrix}\tfrac12&0\\0&-\tfrac12\end{pmatrix},\qquad
U=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
V=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
$$

### The Three Relations

$S$ is diagonal with entries $s_1=\tfrac12$ and $s_2=-\tfrac12$; on a matrix unit $[S,E_{ij}]=(s_i-s_j)E_{ij}$. Hence

$$
[S,E_{12}]=\tfrac12E_{12}-\left(-\tfrac12\right)E_{12}=E_{12},\qquad
[S,E_{21}]=-E_{21}.
$$

Multiplying the units,

$$
UV=E_{12}E_{21}=E_{11},\qquad VU=E_{21}E_{12}=E_{22},
$$

so

$$
[U,V]=E_{11}-E_{22}=2S.
$$

**Result.** The pair satisfies

$$
[S,U]=U,\qquad [S,V]=-V,\qquad [U,V]=2S,\qquad S=\tfrac12[U,V],
$$

with zero residual. It is a spin pair, and $(S,U,V)$ is a spin triple spanning a copy of $\mathfrak{sl}_2(\mathbb{C})$.

## The Defining Module: Spin $\tfrac12$

The defining module is $\mathbb{C}^2$, with basis $e_1,e_2$. The triple acts by left multiplication, and $S$ is diagonal:

$$
Se_1=\tfrac12e_1,\qquad Se_2=-\tfrac12e_2.
$$

The weights are $\tfrac12,-\tfrac12$. Their sum is $0=\operatorname{tr}S$. The highest weight is $\tfrac12$; the two weights are one string, which is the weight string of $W_{1/2}$.

**Result.** The defining module is $W_{1/2}$, and its spin is $\tfrac12$.

## The Adjoint Action

### The Images of the Matrix Units

The adjoint action is $\operatorname{ad}_X(Y)=XY-YX$. For the two ladders the defining formulas are

$$
\operatorname{ad}_U(E_{ij})=U E_{ij}-E_{ij}U,\qquad
\operatorname{ad}_V(E_{ij})=V E_{ij}-E_{ij}V,
$$

and with $U=E_{12}$, $V=E_{21}$ the four cases give the table.

| $(i,j)$ | $\operatorname{ad}_U(E_{ij})$ | $\operatorname{ad}_V(E_{ij})$ |
|---|---|---|
| $(1,1)$ | $-E_{12}$ | $E_{21}$ |
| $(1,2)$ | $0$ | $E_{22}-E_{11}$ |
| $(2,1)$ | $E_{11}-E_{22}$ | $0$ |
| $(2,2)$ | $E_{12}$ | $-E_{21}$ |

**Result.** The two zero entries are the highest and the lowest weight vectors: $E_{12}$ is killed by $\operatorname{ad}_U$, and $E_{21}$ is killed by $\operatorname{ad}_V$. Every other unit is moved one step.

### The Weight Shift

Since $[S,U]=U$, the Jacobi identity gives

$$
\operatorname{ad}_S\operatorname{ad}_U=\operatorname{ad}_U\operatorname{ad}_S+\operatorname{ad}_{[S,U]}=\operatorname{ad}_U\operatorname{ad}_S+\operatorname{ad}_U,
$$

so on a vector of weight $m$, $\operatorname{ad}_U$ raises the weight by $1$; similarly $\operatorname{ad}_V$ lowers it by $1$.

**Result.** The table is a raising-and-lowering pattern, and the two zeros are forced by the weights.

### The Four Weights

Since $S$ is diagonal, $\operatorname{ad}_S(E_{ij})=(s_i-s_j)E_{ij}=\left(\tfrac{3}{2}-i-\tfrac{3}{2}+j\right)E_{ij}=(j-i)E_{ij}$. The weights are

| $(i,j)$ | $(1,1)$ | $(1,2)$ | $(2,1)$ | $(2,2)$ |
|---|---|---|---|---|
| weight $j-i$ | $0$ | $1$ | $-1$ | $0$ |

The multiplicities are $\mu(-1)=1$, $\mu(0)=2$, $\mu(1)=1$.

### The Content

**Proposition (multiplicity formula).** If $W\cong\bigoplus_j m_jW_j$ and $\mu(m)$ is the multiplicity of the weight $m$, then

$$
\mu(m)=\sum_{j\ge\lvert m\rvert}m_j,\qquad m_j=\mu(j)-\mu(j+1).
$$

*Proof.* The module $W_j$ has exactly one weight at each of $j,j-1,\dots,-j$. It contributes to $\mu(m)$ exactly when $j\ge\lvert m\rvert$; subtracting the formula for $j+1$ leaves $m_j$.

Here $m_0=\mu(0)-\mu(1)=2-1=1$ and $m_1=\mu(1)-\mu(2)=1-0=1$.

**Result.** $\mathfrak{gl}_2\cong W_0\oplus W_1$, of dimensions $1+3=4$. The adjoint content is $0,1$.

## The Two Chains

### The Highest Weight Vectors

A highest weight vector of weight $j$ is a nonzero $h$ with $\operatorname{ad}_Sh=jh$ and $\operatorname{ad}_Uh=0$. The candidates are

$$
h_0=I,\qquad h_1=E_{12}.
$$

From the table of §*The Images of the Matrix Units*, $\operatorname{ad}_UI=0$, $\operatorname{ad}_UE_{12}=0$, $\operatorname{ad}_SI=0$ and $\operatorname{ad}_SE_{12}=E_{12}$.

### The Chains

Applying $\operatorname{ad}_V$:

| $j$ | chain |
|---|---|
| $0$ | $I\mapsto0$ |
| $1$ | $E_{12}\mapsto E_{22}-E_{11}\mapsto-2E_{21}\mapsto0$ |

The chain lengths are $1$ and $3$.

### Independence

The four vectors

$$
I;\qquad E_{12},\ E_{22}-E_{11},\ -2E_{21}
$$

form a basis of $\mathfrak{gl}_2$. In the basis order $(E_{11},E_{12},E_{21},E_{22})$ the determinant of the matrix of columns is $4$.

**Result.** The chains are independent and their sum is direct:

$$
\mathfrak{gl}_2=W_0\oplus W_1,\qquad \dim W_j=2j+1.
$$

## The Adjoint Carriers

An $\operatorname{ad}(M_2(\mathbb{C}))$-stable subspace is an ideal of $\mathfrak{gl}_2$. The ideals are $0$, $\mathbb{C}I$, $\mathfrak{sl}_2$ and $\mathfrak{gl}_2$; the irreducible ones are $\mathbb{C}I$ and $\mathfrak{sl}_2$.

The centre is fixed by $\operatorname{ad}_S$, so its spin is $0$. On $\mathfrak{sl}_2$ the weights are those of the four units, minus the diagonal unit of weight $0$:

| $m$ | $-1$ | $0$ | $1$ |
|---|---|---|---|
| $\mu_{\mathfrak{sl}_2}(m)$ | $1$ | $1$ | $1$ |

The multiplicity formula gives $m_0=1-1=0$ and $m_1=1-0=1$, so $\mathfrak{sl}_2=W_1$ and its spin is $1$.

**Result.** The adjoint elementary carriers are $\mathbb{C}I$ (spin $0$) and $\mathfrak{sl}_2$ (spin $1$).

### The List

| carrier | action | dimension | content | spin |
|---|---|---|---|---|
| $\mathbb{C}^2$ | left multiplication | $2$ | $W_{1/2}$ | $\tfrac12$ |
| $\mathbb{C}I$ | adjoint | $1$ | $W_0$ | $0$ |
| $\mathfrak{sl}_2$ | adjoint | $3$ | $W_1$ | $1$ |

**Result.** The elementary spin list is $\Sigma=\{0,\tfrac12,1\}$.

## The Two Actions on the Algebra

**Left multiplication.** $X\cdot Y=XY$. Then $SE_{ij}=s_iE_{ij}$, so the weight of $E_{ij}$ is $s_i=\tfrac32-i$, independent of $j$. The first row has weight $\tfrac12$ and the second row $-\tfrac12$, each with multiplicity $2$. Hence, as a left module,

$$
M_2(\mathbb{C})=2W_{1/2},
$$

with spin $\tfrac12$.

**The adjoint action.** $X\cdot Y=[X,Y]$. Then $\operatorname{ad}_S(E_{ij})=(j-i)E_{ij}$, and the weights depend on both indices. This gives $W_0\oplus W_1$, with content $0,1$.

**Result.** The two columns of the row refer to two actions. The elementary list uses the left action for the simple module and the adjoint action for the stable subspaces; the adjoint content uses the adjoint action only.

## Checks

### The Casimir

The Casimir element of the triple is

$$
C=S^2+\tfrac12(UV+VU).
$$

On $\mathbb{C}^2$,

$$
C=\tfrac14I+\tfrac12I=\tfrac34I.
$$

The eigenvalue is $j(j+1)=\tfrac34$ for $j=\tfrac12$, as it must be.

On the adjoint module the image of $C$ has characteristic polynomial

$$
\lambda(\lambda-2)^3,
$$

with eigenvalues $0$ and $2=j(j+1)$ for $j=0$ and $j=1$, of multiplicities $1$ and $3$.

**Result.** The Casimir confirms both decompositions.

### The Table of Checks

| check | result |
|---|---|
| $[S,U]-U$ | $0$ |
| $[S,V]+V$ | $0$ |
| $[U,V]-2S$ | $0$ |
| $\operatorname{ad}_U\operatorname{ad}_V-\operatorname{ad}_V\operatorname{ad}_U-2\operatorname{ad}_S$ | $0$ |
| $\sum_m\mu(m)$ | $4$ |
| $(m_0,m_1)$ | $(1,1)$ |
| chain lengths | $1,3$ |
| determinant of the four vectors | $4$ |
| characteristic polynomial on $\mathfrak{gl}_2$ | $\lambda(\lambda-2)^3$ |
| $\rho_{1/2}(C)$ | $\tfrac34I$ |

## Summary

- The pair is $S=\operatorname{diag}(\tfrac12,-\tfrac12)$, $U=E_{12}$, $V=E_{21}$.
- It satisfies $[S,U]=U$, $[S,V]=-V$, $[U,V]=2S$ with zero residual.
- The defining module $\mathbb{C}^2$ has weights $\tfrac12,-\tfrac12$; its spin is $\tfrac12$.
- The adjoint weights are $1,0,0,-1$; the multiplicity formula gives $m_0=m_1=1$, so the content is $0,1$ with dimensions $1,3$.
- The chains of $I$ and $E_{12}$ have lengths $1,3$, and the four vectors are independent.
- The elementary carriers are $\mathbb{C}I$ (spin $0$), $\mathbb{C}^2$ (spin $\tfrac12$) and $\mathfrak{sl}_2$ (spin $1$); the list is $0,\tfrac12,1$.
- The list and the content differ: $\tfrac12$ is the defining spin and is not in the adjoint content.
- The Casimir is $\tfrac34I$ on $\mathbb{C}^2$, with eigenvalues $0,2$ on $\mathfrak{gl}_2$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $M_2(\mathbb{C})$ | matrix algebra, $1$-based indices |
| $E_{ij}$ | matrix unit |
| $S$ | spin element $\tfrac12[U,V]=\operatorname{diag}(\tfrac12,-\tfrac12)$ |
| $U,V$ | ladders $E_{12},E_{21}$ |
| $\operatorname{ad}_X$ | $Y\mapsto XY-YX$ |
| $W_j$ | irreducible carrier, dimension $2j+1$ |
| $\mu(m)$ | multiplicity of the weight $m$ |
| $m_j$ | multiplicity of $W_j$ |
| $C$ | Casimir element $S^2+\tfrac12(UV+VU)$ |

## Further Reading

- [The General Definition of Spin](../articles_maths/the-general-definition-of-spin.html), for the definition and the table of cases.
- [The Spin of a Biquaternion](../articles_maths/the-spin-of-a-biquaternion.html), for the same row in the biquaternion frame.
- [The Spin Chain and the Adjoint Decomposition of $M_n(\mathbb{C})$](../articles_maths/the-spin-chain-and-the-adjoint-decomposition-mnc.html), for the general chain.
- [Representations of Lie Algebras](../articles_maths/representations-of-lie-algebras.html), for the highest weight classification.
- [The Casimir Operator](../articles_maths/the-casimir-operator.html), for the eigenvalue $j(j+1)$.
