# __The Coefficient Matrix of a Two-Sided Operator: A Worked Computation__

## Introduction

**The purpose.** This article carries out one coefficient computation in full. It takes a concrete $4\times4$ matrix, computes its sixteen coefficients in the basis $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$, assembles the coefficient matrix, finds its rank, factors it, and reconstructs the matrix. Every step is written out, with the matrices displayed.

**The matrix.**
$$
M=\begin{pmatrix}1&2&0&0\\0&1&0&0\\0&0&1&2\\0&0&0&1\end{pmatrix}.
$$
It is upper triangular, all diagonal entries are $1$, so $\det M=1$ and $\operatorname{rank}M=4$. Its only nonzero entries are
$$
M_{11}=1,\quad M_{12}=2,\quad M_{22}=1,\quad M_{33}=1,\quad M_{34}=2,\quad M_{44}=1 .
$$

**The punchline, stated first.** The ordinary rank is $4$, the maximal value. The length is $2$: the matrix is a sum of two two-sided operators, and not of one. The two numbers measure different things, and the ordinary rank gives no information about the length. The coefficient rank does.

**The method and its source.** The basis, the orthogonality theorem and the length theorem are *The Two-Sided Operators Method to Build $M_4(\mathbb{C})$*. This article is the computation that accompanies it.

## The Formula

**The coefficient.** For $A\in M_4(\mathbb{C})$ and $\mu,\nu\in\{t,x,y,z\}$,
$$
c_{\mu\nu}(A)=\tfrac14\operatorname{tr}\bigl(L_{\mathrm{axf},e_\mu}{R_{\mathrm{axf},e_\nu}}^{*}A\bigr).
$$

**Why the factor four.** The matrices $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$ are orthogonal for the Hilbert–Schmidt form:
$$
\operatorname{tr}\bigl(L_{\mathrm{axf},e_\mu}{R_{\mathrm{axf},e_\nu}}^{*}L_{\mathrm{axf},e_\rho}R_{\mathrm{axf},e_\sigma}\bigr)=4\,\delta_{\mu\rho}\delta_{\nu\sigma}.
$$
The square norm of each is four, so the coefficient carries the factor $\tfrac14$.

**The matrices are real.** Every $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$ is a real signed permutation matrix, so $L_{\mathrm{axf},e_\mu}{R_{\mathrm{axf},e_\nu}}^{*}=L_{\mathrm{axf},e_\mu}{R_{\mathrm{axf},e_\nu}}^{\mathsf T}$ and
$$
\operatorname{tr}\bigl(L_{\mathrm{axf},e_\mu}{R_{\mathrm{axf},e_\nu}}^{*}A\bigr)=\sum_{i,j}(L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu})_{ij}A_{ij}.
$$
In practice: read the four nonzero positions of $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$, add the corresponding entries of $A$ with their signs, divide by four. No matrix product is needed, though two are shown below as a check.

**The index order.** The labels $t,x,y,z$ correspond to the rows and columns $1,2,3,4$. The first index of $c_{\mu\nu}$ is the left parameter, the second the right parameter. The order is part of the definition; swapping it transposes the coefficient matrix and returns the wrong operator.

## The Sixteen Traces

### The four diagonal matrices

**$L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}=\mathrm{I}_4$.** The nonzero positions are the diagonal, all with sign $+1$:
$$
\operatorname{tr}(L_{\mathrm{axf},e_t}{R_{\mathrm{axf},e_t}}^{\mathsf T}M)=M_{11}+M_{22}+M_{33}+M_{44}=1+1+1+1=4,
\qquad c_{tt}=1 .
$$

**$L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_x}=\operatorname{diag}(-1,-1,1,1)$.** The signs are $-,-,+,+$:
$$
\operatorname{tr}(L_{\mathrm{axf},\vec e_x}{R_{\mathrm{axf},\vec e_x}}^{\mathsf T}M)=-1-1+1+1=0,
\qquad c_{xx}=0 .
$$

**$L_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}=\operatorname{diag}(-1,1,-1,1)$:**
$$
-1+1-1+1=0,
\qquad c_{yy}=0 .
$$

**$L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_z}=\operatorname{diag}(-1,1,1,-1)$:**
$$
-1+1+1-1=0,
\qquad c_{zz}=0 .
$$

**The reading.** The four diagonal matrices see only the diagonal of $M$. Three of the four sums vanish because the diagonal of $M$ is constant.

### Two full matrix products

**The matrix $L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},e_t}$.** Its nonzero positions are $(1,2)=-1$, $(2,1)=+1$, $(3,4)=-1$, $(4,3)=+1$:
$$
L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},e_t}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},
\qquad
L_{\mathrm{axf},\vec e_x}{R_{\mathrm{axf},e_t}}^{\mathsf T}=\begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix}.
$$

**The product, row by row.** Row $1$ of $L_{\mathrm{axf},\vec e_x}{R_{\mathrm{axf},e_t}}^{\mathsf T}$ is $(0,1,0,0)$, so the first row of the product is row $2$ of $M$. Row $2$ is $(-1,0,0,0)$, so the second row is minus row $1$ of $M$. Row $3$ is $(0,0,0,1)$, so the third row is row $4$ of $M$. Row $4$ is $(0,0,-1,0)$, so the fourth row is minus row $3$ of $M$:
$$
L_{\mathrm{axf},\vec e_x}{R_{\mathrm{axf},e_t}}^{\mathsf T}M=
\begin{pmatrix}
0&1&0&0\\
-1&-2&0&0\\
0&0&0&1\\
0&0&-1&-2
\end{pmatrix}.
$$
The trace is $0+(-2)+0+(-2)=-4$, hence
$$
c_{xt}=\tfrac14(-4)=-1 .
$$

**The dot-product check.** The signed positions of $L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},e_t}$ give
$$
(-1)M_{12}+(+1)M_{21}+(-1)M_{34}+(+1)M_{43}
=-2+0-2+0=-4 .
$$

**The matrix $L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x}$.** Its nonzero positions are $(1,2)=-1$, $(2,1)=+1$, $(3,4)=+1$, $(4,3)=-1$:
$$
L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},
\qquad
L_{\mathrm{axf},e_t}{R_{\mathrm{axf},\vec e_x}}^{\mathsf T}=\begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix}.
$$
The product is
$$
L_{\mathrm{axf},e_t}{R_{\mathrm{axf},\vec e_x}}^{\mathsf T}M=
\begin{pmatrix}
0&1&0&0\\
-1&-2&0&0\\
0&0&0&-1\\
0&0&1&2
\end{pmatrix},
$$
whose trace is $0+(-2)+0+2=0$. Hence
$$
c_{tx}=0 .
$$

**The trap.** The two matrices agree in the first two rows and differ in the last two, and the two coefficients are different: $c_{xt}=-1$ and $c_{tx}=0$. A computation that prints $L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x}$ and transposes $L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},e_t}$ returns $c_{tx}=-1$, transposes the coefficient matrix, and then fails at the reconstruction. The labels are not symmetric.

### The ten remaining off-diagonal matrices

**The table.** Each row gives the signed positions of $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$ and the resulting sum. Every corresponding entry of $M$ is zero except in the last row.

| Matrix | Signed positions | Sum | Coefficient |
|---|---|---|---|
| $L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_y}$ | $(1,3){-}1$, $(2,4){-}1$, $(3,1){+}1$, $(4,2){+}1$ | $0$ | $0$ |
| $L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z}$ | $(1,4){-}1$, $(2,3){+}1$, $(3,2){-}1$, $(4,1){+}1$ | $0$ | $0$ |
| $L_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},e_t}$ | $(1,3){-}1$, $(2,4){+}1$, $(3,1){+}1$, $(4,2){-}1$ | $0$ | $0$ |
| $L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},e_t}$ | $(1,4){-}1$, $(2,3){-}1$, $(3,2){+}1$, $(4,1){+}1$ | $0$ | $0$ |
| $L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y}$ | $(1,4){+}1$, $(2,3){-}1$, $(3,2){-}1$, $(4,1){+}1$ | $0$ | $0$ |
| $L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_z}$ | $(1,3){-}1$, $(2,4){-}1$, $(3,1){-}1$, $(4,2){-}1$ | $0$ | $0$ |
| $L_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_x}$ | $(1,4){-}1$, $(2,3){-}1$, $(3,2){-}1$, $(4,1){-}1$ | $0$ | $0$ |
| $L_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_z}$ | $(1,2){+}1$, $(2,1){+}1$, $(3,4){-}1$, $(4,3){-}1$ | $+2+0-2+0=0$ | $0$ |
| $L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_x}$ | $(1,3){+}1$, $(2,4){-}1$, $(3,1){+}1$, $(4,2){-}1$ | $0$ | $0$ |
| $L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}$ | $(1,2){-}1$, $(2,1){-}1$, $(3,4){-}1$, $(4,3){-}1$ | $-2-0-2-0=-4$ | $-1$ |

**The two cancellations.** $L_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_z}$ and $L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}$ are the only off-diagonal matrices whose signed positions meet nonzero entries of $M$, and they meet the same two entries with opposite signs. The sum is $+2-2=0$ for $L_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_z}$ and $-2-2=-4$ for $L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}$. The cancellation in $L_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_z}$ is not an accident of this matrix: it is the sign difference between $L$ and $R$ on the same pair of indices.

### The coefficient matrix

**The result.**
$$
c(M)=
\begin{pmatrix}
1&0&0&0\\
-1&0&0&0\\
0&0&0&0\\
0&0&-1&0
\end{pmatrix}.
$$

**The nonzero entries.** Only three: $c_{tt}=1$, $c_{xt}=-1$, $c_{zy}=-1$. All the others vanish.

## The Rank

**The rows.** Only rows $t$, $x$ and $z$ are nonzero, and rows $t$ and $x$ are proportional: row $x$ is minus row $t$. So the rank is at most $2$.

**A minor.** Take rows $\{t,z\}$ and columns $\{t,y\}$:
$$
\det\begin{pmatrix}c_{tt}&c_{ty}\\c_{zt}&c_{zy}\end{pmatrix}
=\det\begin{pmatrix}1&0\\0&-1\end{pmatrix}=-1\ne0 .
$$
So the rank is exactly $2$.

**The length.**
$$
\ell(M)=\operatorname{rank}c(M)=2 .
$$

**What the minor does not show.** The minor shows that two rows and two columns are independent. It does not show which factorisation is simplest; that is the next section.

## Reconstruction

**The expansion.** Since the only nonzero coefficients are $c_{tt}=1$, $c_{xt}=-1$ and $c_{zy}=-1$,
$$
M=L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}-L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},e_t}-L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}.
$$

**The three matrices.**
$$
L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},
\qquad
-L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},e_t}=\begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},
\qquad
-L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}=\begin{pmatrix}0&1&0&0\\1&0&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}.
$$

**The row sums.**
$$
\begin{aligned}
\text{row }1&:\ (1,0,0,0)+(0,1,0,0)+(0,1,0,0)=(1,2,0,0),\\
\text{row }2&:\ (0,1,0,0)+(-1,0,0,0)+(1,0,0,0)=(0,1,0,0),\\
\text{row }3&:\ (0,0,1,0)+(0,0,0,1)+(0,0,0,1)=(0,0,1,2),\\
\text{row }4&:\ (0,0,0,1)+(0,0,-1,0)+(0,0,1,0)=(0,0,0,1).
\end{aligned}
$$
Each row is the row of $M$. The reconstruction is correct.

**The wrong reconstruction.** With the transposed coefficient matrix one would write $M=L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}-L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x}-L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}$. The first two rows still agree, but the third and fourth do not:
$$
L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}-L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x}-L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}
=\begin{pmatrix}1&2&0&0\\0&1&0&0\\0&0&1&0\\0&0&2&1\end{pmatrix},
$$
which is not $M$. The two entries $M_{34}=2$ and $M_{43}=0$ are exchanged. This is the visible cost of the index slip.

## The Factorisation

**Split by rows.** The coefficient matrix is
$$
c(M)=e_t\,(1,0,0,0)+\vec e_x\,(-1,0,0,0)+\vec e_z\,(0,0,-1,0).
$$
The first two terms share the right vector $(1,0,0,0)$, so
$$
c(M)=(e_t-\vec e_x)\,(1,0,0,0)+\vec e_z\,(0,0,-1,0).
$$

**Read the two products.**
$$
a_1=e_t-\vec e_x,\quad b_1=e_t,\qquad
a_2=\vec e_z,\quad b_2=-\vec e_y .
$$
Hence
$$
M=L_{\mathrm{axf},e_t-\vec e_x}R_{\mathrm{axf},e_t}+L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},-\vec e_y}
=L_{\mathrm{axf},e_t-\vec e_x}-L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}
=L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}-L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},e_t}-L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}.
$$

**The two matrices.**
$$
L_{\mathrm{axf},e_t-\vec e_x}=\mathrm{I}_4-L_{\mathrm{axf},\vec e_x}=
\begin{pmatrix}1&1&0&0\\-1&1&0&0\\0&0&1&1\\0&0&-1&1\end{pmatrix},
\qquad
-L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}=-L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}=
\begin{pmatrix}0&1&0&0\\1&0&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}.
$$
Their sum is $M$.

**Why two is the minimum.** The coefficient matrix has rank $2$. A single product would give a coefficient matrix of rank one. So no single two-sided operator equals $M$, and length $2$ is exact.

**The two products are rank four.** Each of $L_{\mathrm{axf},e_t-\vec e_x}$ and $L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}$ is an invertible matrix. The sum of two invertible matrices can be singular or not; here it is invertible. The length counts the terms, not the rank of the terms.

## Ordinary Rank Is Not Length

**The two numbers.**
$$
\operatorname{rank}M=4,\qquad \ell(M)=2 .
$$

**Why the ordinary rank is four.** The matrix is upper triangular with unit diagonal, so $\det M=1$ and the four columns are independent.

**Why the length is two.** The coefficient matrix has rank two.

**The matrix is not a left regular matrix.** A left regular matrix $L_a$ has entries $(1,2)=-a_x$ and $(2,1)=+a_x$. The matrix $M$ has $M_{12}=2$ and $M_{21}=0$; it would need $a_x=-2$ and $a_x=0$. So $M$ is not of the form $L_a$: the right factor is needed. This is why the left regular model, of dimension four, cannot contain it.

**The lesson.** Ordinary rank measures the image of the matrix as a linear map. The length measures the least number of two-sided operators whose sum is the matrix. The two are independent: the identity has rank four and length one, the matrix unit $E_{11}$ has rank one and length four, and this matrix has rank four and length two.

## The Recipe

**The six steps.**

1. Compute the sixteen traces
$$
c_{\mu\nu}=\tfrac14\sum_{i,j}(L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu})_{ij}M_{ij}.
$$
2. Assemble the $4\times4$ coefficient matrix $c(M)$.
3. Compute its rank, by $2\times2$ minors or by row reduction. That rank is the length.
4. If the rank is one, factor $c=a\,b^{\mathsf T}$ and read off
$$
a=\sum_\mu a_\mu e_\mu,\qquad b=\sum_\nu b_\nu e_\nu,\qquad M=L_aR_b .
$$
5. If the rank is $r\ge2$, factor $c=UV$ with $U,V$ of size $4\times r$; the $r$ products are $L_{u_k}R_{v_k}$ for the columns $u_k$ of $U$ and $v_k$ of $V$.
6. Reconstruct $M=\sum_{\mu,\nu}c_{\mu\nu}L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$ as a check.

**The single-product test.** It is step 3 with threshold one. It has nothing to do with the ordinary rank of $M$.

**A remark on the factorisation.** The factorisation of $c$ is not unique: any invertible $r\times r$ matrix $G$ gives $c=(UG)(G^{-1}V)$, and the $r$ products change while their sum does not. The row-split factorisation used above is the one that keeps each product as simple as possible.

## Summary

| Quantity | Value |
|---|---|
| the matrix $M$ | $4\times4$ upper triangular, blocks $\begin{pmatrix}1&2\\0&1\end{pmatrix}$ |
| nonzero entries of $M$ | $M_{11}=1$, $M_{12}=2$, $M_{22}=1$, $M_{33}=1$, $M_{34}=2$, $M_{44}=1$ |
| nonzero coefficients | $c_{tt}=1$, $c_{xt}=-1$, $c_{zy}=-1$ |
| coefficient matrix | $\begin{pmatrix}1&0&0&0\\-1&0&0&0\\0&0&0&0\\0&0&-1&0\end{pmatrix}$ |
| rank of $c(M)$ | $2$, minor on rows $\{t,z\}$ and columns $\{t,y\}$ equal to $-1$ |
| length | $2$ |
| ordinary rank | $4$ |
| determinant | $1$ |
| minimal decomposition | $M=L_{\mathrm{axf},e_t-\vec e_x}R_{\mathrm{axf},e_t}-L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}=L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}-L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},e_t}-L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}$ |

**The punchline.** The ordinary rank is $4$, the maximal value, and the length is $2$. Ordinary rank gives no information about length; coefficient rank does.

**The two traps.** The index order is not symmetric: $c_{xt}=-1$ and $c_{tx}=0$, and a transposed coefficient matrix reconstructs a different matrix. The row split is not the column split: the terms combine as $(e_t-\vec e_x)(1,0,0,0)+\vec e_z(0,0,-1,0)$, not as $e_t(1,-1,0,0)+\vec e_z(0,0,-1,0)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the coefficient basis of $\mathbb{B}$, with $e_t=1$ and $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$ |
| $L_a$ | left multiplication $x\mapsto ax$ |
| $R_b$ | right multiplication $x\mapsto xb$ |
| $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$ | $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$, the sixteen basis matrices |
| $c_{\mu\nu}(A)$ | $\tfrac14\operatorname{tr}(L_{\mathrm{axf},e_\mu}{R_{\mathrm{axf},e_\nu}}^{*}A)$ |
| $c(A)$ | the $4\times4$ coefficient matrix |
| $\ell(A)$ | the length, $\operatorname{rank}c(A)$ |
| $L_{\mathrm{axf},\vec e_x}{R_{\mathrm{axf},e_t}}^{\mathsf T}$ | the transpose, equal to $L_{\mathrm{axf},\vec e_x}{R_{\mathrm{axf},e_t}}^{*}$ because the matrix is real |

## Further Reading

- [The Two-Sided Operators Method to Build $M_4(\mathbb{C})$](the-two-sided-operators-method-to-build-m4c.html), for the sixteen matrices, the multiplication tables, the orthogonality theorem and the length theorem.
- [Operators Acting 2 Side](operators-acting-2-side.html), for the construction.
- [The Matrix Algebra $M_4(\mathbb{C})$](the-matrix-algebra-m4c.html), for the algebra and the matrix units.
- [The Operators of the Peirce Decomposition of $M_4(\mathbb{C})$](the-operators-of-the-peirce-decomposition-of-m4c.html), for the same operators on the sixteen-dimensional algebra.
