# __The Spin of the Principal Pair of $M_3(\mathbb{C})$: A Worked Computation__

## Introduction

The table of cases in *The General Definition of Spin* has the following row.

| algebra | base field | pair | elementary spins | adjoint content |
|---|---|---|---|---|
| $M_3(\mathbb{C})$ | $\mathbb{C}$ | principal | $0,1,2$ | $0,1,2$ |

This article computes every entry of the row. The result is stated first, then derived.

### The Result

**The spin of $\mathbb{C}^3$ is $1$.** The defining module is the space of columns. The spin element $S$ acts diagonally, with eigenvalues $1,0,-1$, and the largest is $1$.

**The spin of $\mathbb{C}I$ is $0$.** The centre is fixed by the adjoint action, so every weight is $0$.

**The spin of $\mathfrak{sl}_3$ is $2$.** The traceless part is irreducible under the adjoint action. Its largest $S$-weight is $2$, on the unit $E_{13}$.

**The adjoint content is $0,1,2$.** As a module for the triple, $\mathfrak{gl}_3=W_0\oplus W_1\oplus W_2$, of dimensions $1+3+5=9$.

| carrier | action | dimension | spin |
|---|---|---|---|
| $\mathbb{C}^3$ | left multiplication | $3$ | $1$ |
| $\mathbb{C}I$ | adjoint | $1$ | $0$ |
| $\mathfrak{sl}_3$ | adjoint | $8$ | $2$ |
| $\mathfrak{gl}_3$ | adjoint | $9$ | content $0,1,2$ |

The last line is not a fourth elementary carrier. It records the decomposition of the adjoint module; it has no single spin of its own.

### What Has to Be Computed

Four steps produce the row.

1. Write the pair and check the three relations. This gives the triple $(S,U,V)$.
2. Act with $S$ on the defining module and on the nine matrix units. This gives the weights.
3. Count the weights. The multiplicity formula gives the decomposition of the adjoint module.
4. Identify the elementary carriers and read off their spins.

The two right-hand columns of the row are different invariants. The **elementary spins** are the spins of the irreducible carriers: one simple left module, and the irreducible stable subspaces of the adjoint module. The **adjoint content** is the decomposition of the whole nine-dimensional adjoint module into irreducible modules of the triple. At $n=3$ they happen to be the same set.

## The Pair

### The Three Matrices

**Definition (principal pair).** For $n\ge2$, the principal pair of $M_n(\mathbb{C})$ is

$$
S=\operatorname{diag}\left(\frac{n+1}{2}-k\right)_{k=1}^{n},\qquad
U=\sum_{k=1}^{n-1}\sqrt{k(n-k)}\,E_{k,k+1},\qquad
V=\sum_{k=1}^{n-1}\sqrt{k(n-k)}\,E_{k+1,k}.
$$

For $n=3$ the diagonal entries of $S$ are $1,0,-1$, and the two coefficients are $\sqrt2$. Hence

$$
S=\begin{pmatrix}1&0&0\\0&0&0\\0&0&-1\end{pmatrix},\qquad
U=\begin{pmatrix}0&\sqrt2&0\\0&0&\sqrt2\\0&0&0\end{pmatrix},\qquad
V=\begin{pmatrix}0&0&0\\\sqrt2&0&0\\0&\sqrt2&0\end{pmatrix}.
$$

In matrix units,

$$
S=E_{11}-E_{33},\qquad U=\sqrt2\,(E_{12}+E_{23}),\qquad V=\sqrt2\,(E_{21}+E_{32}).
$$

### The Three Relations

Because $S$ is diagonal, $[S,E_{ij}]=(s_i-s_j)E_{ij}$ with $s=(1,0,-1)$. Hence

$$
[S,E_{12}]=E_{12},\qquad [S,E_{23}]=E_{23},\qquad [S,E_{21}]=-E_{21},\qquad [S,E_{32}]=-E_{32},
$$

and therefore

$$
[S,U]=U,\qquad [S,V]=-V.
$$

For the third relation, use $E_{ab}E_{cd}=\delta_{bc}E_{ad}$:

$$
UV=2(E_{11}+E_{22}),\qquad VU=2(E_{22}+E_{33}),
$$

so

$$
[U,V]=UV-VU=2(E_{11}-E_{33})=2S.
$$

**Result.** The pair $(U,V)$ satisfies

$$
[S,U]=U,\qquad [S,V]=-V,\qquad [U,V]=2S,\qquad S=\tfrac12[U,V],
$$

with zero residual. It is a spin pair, and $(S,U,V)$ is a spin triple spanning a copy of $\mathfrak{sl}_2(\mathbb{C})$.

## The Defining Module: Spin $1$

The defining module is $\mathbb{C}^3$, with basis $e_1,e_2,e_3$. The triple acts by left multiplication. Since $S$ is diagonal,

$$
Se_1=e_1,\qquad Se_2=0,\qquad Se_3=-e_3.
$$

The weights of $S$ are $1,0,-1$. Their sum is $0$, which is $\operatorname{tr}S$.

The highest weight vector is $e_1$: it has weight $1$, and $Ue_1=\sqrt2\,e_2$ moves it down, so no vector of weight $2$ exists. The three weights are one string $1,0,-1$, which is the weight string of $W_1$.

**Result.** The defining module is $W_1$. Its spin is $1$. This is the first $1$ of the row.

## The Adjoint Action

### The Images of the Matrix Units

The adjoint action is $\operatorname{ad}_X(Y)=XY-YX$. For the two ladders,

$$
\operatorname{ad}_U(E_{ij})=\sqrt2\left(\delta_{i2}E_{1j}+\delta_{i3}E_{2j}-\delta_{j1}E_{i2}-\delta_{j2}E_{i3}\right),
$$

$$
\operatorname{ad}_V(E_{ij})=\sqrt2\left(\delta_{i1}E_{2j}+\delta_{i2}E_{3j}-\delta_{j2}E_{i1}-\delta_{j3}E_{i2}\right).
$$

Substituting the nine pairs $(i,j)$ gives the table.

| $(i,j)$ | $\operatorname{ad}_U(E_{ij})$ | $\operatorname{ad}_V(E_{ij})$ |
|---|---|---|
| $(1,1)$ | $-\sqrt2\,E_{12}$ | $\sqrt2\,E_{21}$ |
| $(1,2)$ | $-\sqrt2\,E_{13}$ | $\sqrt2\,(E_{22}-E_{11})$ |
| $(1,3)$ | $0$ | $\sqrt2\,(E_{23}-E_{12})$ |
| $(2,1)$ | $\sqrt2\,(E_{11}-E_{22})$ | $\sqrt2\,E_{31}$ |
| $(2,2)$ | $\sqrt2\,(E_{12}-E_{23})$ | $\sqrt2\,(E_{32}-E_{21})$ |
| $(2,3)$ | $\sqrt2\,E_{13}$ | $\sqrt2\,(E_{33}-E_{22})$ |
| $(3,1)$ | $\sqrt2\,(E_{21}-E_{32})$ | $0$ |
| $(3,2)$ | $\sqrt2\,(E_{22}-E_{33})$ | $-\sqrt2\,E_{31}$ |
| $(3,3)$ | $\sqrt2\,E_{23}$ | $-\sqrt2\,E_{32}$ |

**Result.** The two zero entries sit at the top and the bottom of the weight string: $E_{13}$ is killed by $\operatorname{ad}_U$, and $E_{31}$ is killed by $\operatorname{ad}_V$. Every other unit is moved one step by each ladder.

### The Weight Shift

If $X$ has weight $m$, then $\operatorname{ad}_UX$ has weight $m+1$ and $\operatorname{ad}_VX$ has weight $m-1$. The proof is the Jacobi identity: $\operatorname{ad}_S\operatorname{ad}_U=\operatorname{ad}_U\operatorname{ad}_S+\operatorname{ad}_{[S,U]}$, and $[S,U]=U$.

**Result.** $\operatorname{ad}_U$ raises the weight by $1$, and $\operatorname{ad}_V$ lowers it by $1$. The table above is therefore a raising-and-lowering pattern, and the two zeros are forced.

## The Weights and the Adjoint Content

### The Nine Weights

Since $S$ is diagonal, $\operatorname{ad}_S(E_{ij})=(s_i-s_j)E_{ij}=(j-i)E_{ij}$. The weight of $E_{ij}$ is $j-i$. The nine weights form the matrix

| | $j=1$ | $j=2$ | $j=3$ |
|---|---|---|---|
| $i=1$ | $0$ | $1$ | $2$ |
| $i=2$ | $-1$ | $0$ | $1$ |
| $i=3$ | $-2$ | $-1$ | $0$ |

In the basis order $(E_{11},E_{12},E_{13},E_{21},E_{22},E_{23},E_{31},E_{32},E_{33})$ the operator is $\operatorname{ad}_S=\operatorname{diag}(0,1,2,-1,0,1,-2,-1,0)$.

### The Multiplicities

| $m$ | $-2$ | $-1$ | $0$ | $1$ | $2$ |
|---|---|---|---|---|---|
| $\mu(m)$ | $1$ | $2$ | $3$ | $2$ | $1$ |

The multiplicities sum to $9$. The weighted sum is $0$, which is $\operatorname{tr}\operatorname{ad}_S$.

### The Content

**Proposition (multiplicity formula).** If $W\cong\bigoplus_j m_jW_j$ and $\mu(m)$ is the multiplicity of the weight $m$, then

$$
\mu(m)=\sum_{j\ge\lvert m\rvert,\ j-m\in\mathbb{Z}}m_j,\qquad
m_j=\mu(j)-\mu(j+1).
$$

*Proof.* The module $W_j$ has the weights $j,j-1,\dots,-j$, one each. It contributes one to $\mu(m)$ exactly when $j\ge\lvert m\rvert$ and $j-m$ is an integer. Subtract the formula for $j+1$ from the formula for $j$; every term cancels except $m_j$.

Apply it:

$$
m_0=\mu(0)-\mu(1)=3-2=1,\qquad
m_1=\mu(1)-\mu(2)=2-1=1,\qquad
m_2=\mu(2)-\mu(3)=1-0=1.
$$

**Result.** $\mathfrak{gl}_3\cong W_0\oplus W_1\oplus W_2$, of dimensions $1+3+5=9$. The adjoint content is $0,1,2$. This is the last entry of the row.

## The Three Chains

### The Highest Weight Vectors

A highest weight vector of weight $j$ is a nonzero $h$ with $\operatorname{ad}_Sh=jh$ and $\operatorname{ad}_Uh=0$. The three candidates are

$$
h_0=I,\qquad h_1=E_{12}+E_{23},\qquad h_2=E_{13}.
$$

From the table of §*The Images of the Matrix Units*,

$$
\operatorname{ad}_UI=0,\qquad
\operatorname{ad}_U(E_{12}+E_{23})=-\sqrt2E_{13}+\sqrt2E_{13}=0,\qquad
\operatorname{ad}_UE_{13}=0,
$$

and

$$
\operatorname{ad}_SI=0,\qquad
\operatorname{ad}_S(E_{12}+E_{23})=E_{12}+E_{23},\qquad
\operatorname{ad}_SE_{13}=2E_{13}.
$$

### The Chains

Applying $\operatorname{ad}_V$:

| $j$ | chain |
|---|---|
| $0$ | $I\mapsto0$ |
| $1$ | $E_{12}+E_{23}\mapsto\sqrt2(E_{33}-E_{11})\mapsto-2(E_{21}+E_{32})\mapsto0$ |
| $2$ | $E_{13}\mapsto\sqrt2(E_{23}-E_{12})\mapsto2(E_{11}-2E_{22}+E_{33})\mapsto6\sqrt2(E_{21}-E_{32})\mapsto24E_{31}\mapsto0$ |

The chain lengths are $1,3,5$.

### Independence

The nine vectors

$$
I;\quad E_{12}+E_{23},\ \sqrt2(E_{33}-E_{11}),\ -2(E_{21}+E_{32});\quad
E_{13},\ \sqrt2(E_{23}-E_{12}),\ 2(E_{11}-2E_{22}+E_{33}),\ 6\sqrt2(E_{21}-E_{32}),\ 24E_{31}
$$

form a basis of $\mathfrak{gl}_3$. In the basis order of §*The Nine Weights*, the determinant of the matrix of columns is

$$
27648\sqrt2\neq0.
$$

**Result.** The three chains are independent and their sum is direct:

$$
\mathfrak{gl}_3=W_0\oplus W_1\oplus W_2,\qquad \dim W_j=2j+1.
$$

The chain of $h_j$ spans $W_j$.

## The Adjoint Carriers

### The Stable Subspaces

An $\operatorname{ad}(M_3(\mathbb{C}))$-stable subspace is an ideal of the Lie algebra $\mathfrak{gl}_3$. The ideals are $0$, $\mathbb{C}I$, $\mathfrak{sl}_3$ and $\mathfrak{gl}_3$. The irreducible ones are $\mathbb{C}I$ and $\mathfrak{sl}_3$: the centre is one-dimensional, and $\mathfrak{sl}_3$ is simple.

The centre is fixed by $\operatorname{ad}_S$, so its spin is $0$. On $\mathfrak{sl}_3$ the weights are those of the nine units, minus the diagonal unit of weight $0$:

| $m$ | $-2$ | $-1$ | $0$ | $1$ | $2$ |
|---|---|---|---|---|---|
| $\mu_{\mathfrak{sl}_3}(m)$ | $1$ | $2$ | $2$ | $2$ | $1$ |

The multiplicity formula gives

$$
m_0=2-2=0,\qquad m_1=2-1=1,\qquad m_2=1-0=1.
$$

So $\mathfrak{sl}_3=W_1\oplus W_2$ as a module for the triple, and its largest weight is $2$.

**Result.** The adjoint elementary carriers are $\mathbb{C}I$ and $\mathfrak{sl}_3$. Their spins are $0$ and $2$.

### The List

| carrier | action | dimension | content | spin |
|---|---|---|---|---|
| $\mathbb{C}^3$ | left multiplication | $3$ | $W_1$ | $1$ |
| $\mathbb{C}I$ | adjoint | $1$ | $W_0$ | $0$ |
| $\mathfrak{sl}_3$ | adjoint | $8$ | $W_1\oplus W_2$ | $2$ |

**Result.** The elementary spin list is $\Sigma=\{0,1,2\}$. This is the fourth entry of the row.

**Remark (the two $1$'s are attached to different objects).** The $1$ of the list is the defining module. The $1$ of the adjoint content is the summand $W_1$ inside $\mathfrak{sl}_3$. Likewise the $2$ of the list is the spin of the whole $\mathfrak{sl}_3$, while the $2$ of the content is the top summand of $\mathfrak{sl}_3$.

## The Two Actions on the Algebra

The algebra $M_3(\mathbb{C})$ carries two different triple structures, and they must not be confused.

**Left multiplication.** $(X\cdot Y)=XY$. Then $S E_{ij}=s_iE_{ij}$, so the weight of $E_{ij}$ is $s_i=2-i$, independent of $j$. Row $1$ has weight $1$ (three units), row $2$ weight $0$ (three units), row $3$ weight $-1$ (three units). Hence, as a left module,

$$
M_3(\mathbb{C})=3W_1,
$$

with spin $1$.

**The adjoint action.** $(X\cdot Y)=[X,Y]$. Then $\operatorname{ad}_S(E_{ij})=(j-i)E_{ij}$, and the weights depend on both indices. This gives $W_0\oplus W_1\oplus W_2$, with content $0,1,2$.

**Result.** The row's two columns refer to two actions. The elementary list uses the left action for the simple module and the adjoint action for the stable subspaces. The adjoint content uses the adjoint action only.

## Why the Two Columns Agree Only at $n=3$

### The General Case

For the principal pair of $M_n(\mathbb{C})$:

- the defining module $\mathbb{C}^n$ has weights $(n-1)/2,(n-3)/2,\dots,-(n-1)/2$, so its spin is $(n-1)/2$;
- the centre $\mathbb{C}I$ has spin $0$;
- the traceless part $\mathfrak{sl}_n$ is irreducible, with top weight $n-1$, so its spin is $n-1$;
- the adjoint content is $0,1,\dots,n-1$, each once.

Hence

$$
\Sigma=\left\{0,\ \frac{n-1}{2},\ n-1\right\},\qquad \text{content}=\{0,1,\dots,n-1\}.
$$

### The Comparison

| $n$ | defining spin | adjoint content | elementary list | equal? |
|---|---|---|---|---|
| $2$ | $\tfrac12$ | $0,1$ | $0,\tfrac12,1$ | no |
| $3$ | $1$ | $0,1,2$ | $0,1,2$ | yes |
| $4$ | $\tfrac32$ | $0,1,2,3$ | $0,\tfrac32,3$ | no |
| $5$ | $2$ | $0,1,2,3,4$ | $0,2,4$ | no |

**Proposition.** The two sets are equal only for $n=3$.

*Proof.* For even $n$, the defining spin $(n-1)/2$ is a half-integer and every element of the content is an integer. For odd $n\ge5$, the content contains $1$, while the list is $\{0,(n-1)/2,n-1\}$ with $(n-1)/2\ge2$. For $n=2$ the list is $\{0,\tfrac12,1\}$ and the content is $\{0,1\}$. For $n=3$ both are $\{0,1,2\}$.

**Result.** The equality of the two columns at $n=3$ is a coincidence of the smallest case. At $n=4$, for instance, the content has four summands $0,1,2,3$, but the elementary carriers have spins $0,\tfrac32,3$.

## Checks

### The Casimir

The Casimir element of the triple is

$$
C=S^2+\tfrac12(UV+VU).
$$

It is central in the span of $S,U,V$: it commutes with $S$ because $[UV,S]=U[V,S]+[U,S]V=-UV+UV=0$, and the brackets with $U$ and $V$ cancel in the same way, since $[UV,U]=-2US$ is balanced by $[VU,U]=-2SU$. On $\mathbb{C}^3$ it acts as

$$
C=S^2+\tfrac12(UV+VU)=\operatorname{diag}(1,0,1)+\operatorname{diag}(1,2,1)=2I.
$$

The eigenvalue is $j(j+1)=2$ for $j=1$, as it must be.

On the adjoint module, the image of $C$ is $\operatorname{ad}_S^2+\tfrac12(\operatorname{ad}_U\operatorname{ad}_V+\operatorname{ad}_V\operatorname{ad}_U)$. Its characteristic polynomial is

$$
\lambda(\lambda-6)^5(\lambda-2)^3.
$$

The eigenvalues are $0$, $2$ and $6$, with multiplicities $1$, $3$ and $5$. These are $j(j+1)$ for $j=0,1,2$, and the multiplicities are the dimensions $2j+1$. This gives the adjoint content $0,1,2$ a second time, without counting weights.

**Result.** The Casimir confirms both decompositions: $2$ on $\mathbb{C}^3$, and $0,2,6$ with multiplicities $1,3,5$ on $\mathfrak{gl}_3$.

### The Table of Checks

| check | result |
|---|---|
| $[S,U]-U$ | $0$ |
| $[S,V]+V$ | $0$ |
| $[U,V]-2S$ | $0$ |
| $\operatorname{ad}_U\operatorname{ad}_V-\operatorname{ad}_V\operatorname{ad}_U-2\operatorname{ad}_S$ | $0$ |
| $\sum_m\mu(m)$ | $9$ |
| $(m_0,m_1,m_2)$ | $(1,1,1)$ |
| chain lengths | $1,3,5$ |
| determinant of the nine vectors | $27648\sqrt2$ |
| characteristic polynomial on $\mathfrak{gl}_3$ | $\lambda(\lambda-6)^5(\lambda-2)^3$ |
| $\rho_1(C)$ | $2I$ |
| general $n=2,3,4,5$: the three relations | zero residual |
| general $n=2,3,4,5$: adjoint content | $0,\dots,n-1$ |

## Summary

- The pair is $S=\operatorname{diag}(1,0,-1)$, $U=\sqrt2(E_{12}+E_{23})$, $V=\sqrt2(E_{21}+E_{32})$.
- It satisfies $[S,U]=U$, $[S,V]=-V$, $[U,V]=2S$ with zero residual.
- The defining module $\mathbb{C}^3$ has weights $1,0,-1$; its spin is $1$.
- The adjoint weights of the nine units are $j-i$; the multiplicities are $1,2,3,2,1$.
- The multiplicity formula gives $m_0=m_1=m_2=1$, so the adjoint content is $0,1,2$ with dimensions $1,3,5$.
- The highest weight vectors $I$, $E_{12}+E_{23}$ and $E_{13}$ have chains of lengths $1,3,5$, and the nine vectors are independent.
- The adjoint elementary carriers are $\mathbb{C}I$ (spin $0$) and $\mathfrak{sl}_3$ (spin $2$); with $\mathbb{C}^3$ (spin $1$) the list is $0,1,2$.
- The elementary list and the adjoint content agree only at $n=3$.
- The Casimir is $2I$ on $\mathbb{C}^3$, and has eigenvalues $0,2,6$ with multiplicities $1,3,5$ on $\mathfrak{gl}_3$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $M_n(\mathbb{C})$ | matrix algebra, $1$-based indices |
| $E_{ij}$ | matrix unit |
| $S$ | spin element $\tfrac12[U,V]=\operatorname{diag}(1,0,-1)$ |
| $U,V$ | ladders |
| $\operatorname{ad}_X$ | $Y\mapsto XY-YX$ |
| $W_j$ | irreducible carrier, dimension $2j+1$ |
| $\mu(m)$ | multiplicity of the weight $m$ |
| $m_j$ | multiplicity of $W_j$ |
| $C$ | Casimir element $S^2+\tfrac12(UV+VU)$ |
| $\rho_1$ | defining representation on $\mathbb{C}^3$ |
| $\rho_{\mathrm{ad}}$ | adjoint representation on $\mathfrak{gl}_3$ |
| $\mathfrak{sl}_3$ | traceless part |
| $\Sigma$ | elementary spin list |

## Further Reading

- [The General Definition of Spin](../articles_maths/the-general-definition-of-spin.html), for the definition and the table of cases.
- [The Spin Chain and the Adjoint Decomposition of $M_n(\mathbb{C})$](../articles_maths/the-spin-chain-and-the-adjoint-decomposition-mnc.html), for the general chain.
- [The Triplet Spin One and the Adjoint of $M_3(\mathbb{C})$](../articles_maths/the-triplet-spin-one-and-the-adjoint-of-m3c.html), for the spin-one triplet.
- [Representations of Lie Algebras](../articles_maths/representations-of-lie-algebras.html), for the highest weight classification.
- [The Casimir Operator](../articles_maths/the-casimir-operator.html), for the eigenvalue $j(j+1)$.
- [The Weight of a Frame Root and the Spin Quantum Number](../articles_maths/the-weight-of-a-frame-root-and-the-spin-quantum-number.html), for the carrier, the weight and the root.
