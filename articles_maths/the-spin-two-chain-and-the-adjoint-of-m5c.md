# __The Spin-Two Chain and the Adjoint $1+3+5+7+9$ of $M_5(\mathbb{C})$__

## Introduction

The adjoint decomposition of *The Spin Chain and the Adjoint Decomposition of $M_5(\mathbb{C})$* is

$$
\mathfrak{gl}_5=V_0\oplus V_1\oplus V_2\oplus V_3\oplus V_4,
\qquad 1+3+5+7+9=25,
$$

with $V_j$ the irreducible module of highest weight $j$. This article exhibits the **chain**: an explicit highest weight vector $X_j\in V_j$ for each $j$, the lowering formula for the adjoint action of $J_-$, and the weight diagram of the whole algebra. The highest weight vectors are

$$
X_0=I,\qquad X_1=J_+,\qquad X_2=2E_{13}+\sqrt6E_{24}+2E_{35},\qquad X_3=E_{14}+E_{25},\qquad X_4=E_{15},
$$

of weights $0,1,2,3,4$. The lowering operator acts on the matrix units by

$$
(\operatorname{ad}_{J_-})E_{ij}=c_iE_{i+1,j}-c_{j-1}E_{i,j-1},
\qquad c_k=\sqrt{k(5-k)},
$$

with the conventions $c_0=c_5=0$ and the terms omitted when an index leaves $\{1,\dots,5\}$. The formula is the **ladder**: it moves the row index down with coefficient $c_i$ and the column index left with coefficient $c_{j-1}$, and the two moves are the two ways a weight can drop by one.

The chain is the spin-two chain of the carrier, read on the adjoint. The carrier itself is $V_2=\mathbb{C}^5$ with the weights $2,1,0,-1,-2$; the adjoint is $V_2\otimes V_2=V_0\oplus V_1\oplus V_2\oplus V_3\oplus V_4$. The five summands are the five **highest-weight sectors**: the scalar, the vector, the spin two, the spin three and the spin four. The article computes each sector, its highest weight vector and its weight content, and compares the chain with the biquaternion case $n=2$.

The article assumes the carrier, the matrices $J_3,J_+,J_-$ and the Clebsch–Gordan decomposition of *The Spin Chain and the Adjoint Decomposition of $M_5(\mathbb{C})$*. The modules and the minimal left ideals are *The Modules and the Minimal Left Ideals of $M_5(\mathbb{C})$*; the explicit matrices of the carrier are repeated here for the computation of the chain.

## The Lowering Formula

### The Action on the Matrix Units

**Theorem.** For $1\le i,j\le5$,

$$
(\operatorname{ad}_{J_3})E_{ij}=(j-i)E_{ij},\qquad
(\operatorname{ad}_{J_-})E_{ij}=c_iE_{i+1,j}-c_{j-1}E_{i,j-1},
$$

$$
(\operatorname{ad}_{J_+})E_{ij}=c_{i-1}E_{i-1,j}-c_jE_{i,j+1},
$$

with $c_k=\sqrt{k(5-k)}$ and $c_0=c_5=0$; a term is omitted when its row or column index is outside $\{1,\dots,5\}$.

**Proof.** The weight is $[J_3,E_{ij}]=(m_i-m_j)E_{ij}=(3-i-(3-j))E_{ij}=(j-i)E_{ij}$, where $m_k=3-k$. For the lowering operator, $J_-=\sum_{k=1}^4c_kE_{k+1,k}$. Then

$$
J_-E_{ij}=\sum_{k=1}^{4}c_kE_{k+1,k}E_{ij}=c_iE_{i+1,j}
$$

because $E_{k+1,k}E_{ij}=\delta_{k,i}E_{k+1,j}$, and

$$
E_{ij}J_-=\sum_{k=1}^{4}c_kE_{ij}E_{k+1,k}=c_{j-1}E_{i,j-1}
$$

because $E_{ij}E_{k+1,k}=\delta_{j,k+1}E_{i,k}$. Subtract. The formula for $J_+$ is the transpose, or the same computation with the roles of the rows and columns exchanged.

**Corollary.** The lowering formula preserves the weight minus one:

$$
\operatorname{ad}_{J_3}\bigl((\operatorname{ad}_{J_-})E_{ij}\bigr)=(j-i-1)(\operatorname{ad}_{J_-})E_{ij},
$$

and the raising formula preserves the weight plus one. The two terms of the lowering formula are the two moves of a weight: down one row, or left one column.

**Proof.** Each term has weight $j-i-1$: $E_{i+1,j}$ has weight $j-(i+1)=j-i-1$, and $E_{i,j-1}$ has weight $(j-1)-i=j-i-1$. The raising case is the transpose.

### The Explicit Matrices

The generators are

$$
J_3=\operatorname{diag}(2,1,0,-1,-2),\qquad
J_+=\begin{pmatrix}
0&2&0&0&0\\
0&0&\sqrt6&0&0\\
0&0&0&\sqrt6&0\\
0&0&0&0&2\\
0&0&0&0&0
\end{pmatrix},
\qquad
J_-=J_+^{\mathsf T}.
$$

The lowering formula can be read from the two nonzero entries of each row and column of $J_-$: the entry $c_i$ in row $i+1$ moves the row index, and the entry $c_{j-1}$ in column $j-1$ moves the column index.

## The Highest Weight Vectors

### The Five Vectors

**Definition.** The **chain vectors** are

$$
X_0=I,\qquad X_1=J_+,\qquad X_2=2E_{13}+\sqrt6E_{24}+2E_{35},\qquad X_3=E_{14}+E_{25},\qquad X_4=E_{15}.
$$

**Theorem.** For each $j=0,\dots,4$, the vector $X_j$ is a highest weight vector of weight $j$:

$$
\operatorname{ad}_{J_3}X_j=jX_j,\qquad \operatorname{ad}_{J_+}X_j=0.
$$

**Proof.** The weights are read on the matrix units: $I$ has weight $0$; $J_+=\sum_kc_kE_{k,k+1}$ is a sum of units of weight $+1$; $X_2$ is a sum of units $E_{13},E_{24},E_{35}$ of weight $2$; $X_3$ is a sum of units $E_{14},E_{25}$ of weight $3$; $X_4=E_{15}$ has weight $4$. The annihilation by $\operatorname{ad}_{J_+}$ is checked term by term.

For $X_0=I$: $\operatorname{ad}_{J_+}I=J_+I-IJ_+=0$.

For $X_1=J_+$: $\operatorname{ad}_{J_+}J_+=[J_+,J_+]=0$.

For $X_2$: using the raising formula,

$$
\operatorname{ad}_{J_+}E_{13}=-c_3E_{14}=-\sqrt6E_{14},
$$

$$
\operatorname{ad}_{J_+}E_{24}=c_1E_{14}-c_4E_{25}=2E_{14}-2E_{25},
$$

$$
\operatorname{ad}_{J_+}E_{35}=c_2E_{25}=\sqrt6E_{25}.
$$

Hence

$$
\operatorname{ad}_{J_+}X_2=2(-\sqrt6E_{14})+\sqrt6(2E_{14}-2E_{25})+2(\sqrt6E_{25})=0.
$$

For $X_3$:

$$
\operatorname{ad}_{J_+}E_{14}=-c_4E_{15}=-2E_{15},\qquad
\operatorname{ad}_{J_+}E_{25}=c_1E_{15}=2E_{15},
$$

so $\operatorname{ad}_{J_+}X_3=0$.

For $X_4=E_{15}$:

$$
\operatorname{ad}_{J_+}E_{15}=0.
$$

**Remark.** The vector $X_2$ is the unique highest weight vector of weight $2$ up to scale in the span of $E_{13},E_{24},E_{35}$; the coefficients solve the two equations $2b=\sqrt6a$ and $\sqrt6c=2b$. The vector $X_3$ is the unique one of weight $3$ in the span of $E_{14},E_{25}$, with equal coefficients. The vectors $X_0,X_1,X_4$ are the obvious highest weight vectors of the scalar, the raising operator and the top corner.

### The Cyclic Modules

**Theorem.** The cyclic module $V(j)=\mathbb{C}[J_-,J_3]X_j$ is irreducible of highest weight $j$, of dimension $2j+1$. The five modules $V(0),\dots,V(4)$ are the summands of the adjoint decomposition.

**Proof.** Each $X_j$ is a highest weight vector, so the module it generates is irreducible of highest weight $j$ by the standard highest-weight theory of $\mathfrak{sl}_2$; the dimension is $2j+1$. The five modules have dimensions $1,3,5,7,9$, whose sum is $25=\dim\mathfrak{gl}_5$. Their characters are $\sum_{m=-j}^{j}t^m$, whose sum is

$$
\sum_{j=0}^{4}\sum_{m=-j}^{j}t^m=\sum_{r=-4}^{4}(5-|r|)t^r,
$$

which is the character of $\mathfrak{gl}_5$ under $\operatorname{ad}_{J_3}$. Since both modules are semisimple and have the same character, the sum of the five cyclic modules is the whole algebra and the decomposition is direct. The summand $V(j)$ is the $V_j$ of the Clebsch–Gordan decomposition.

**Corollary.** The highest weights $0,1,2,3,4$ occur once each, and the chain vectors are a set of highest weight vectors, one per summand. The adjoint module is multiplicity-free.

**Proof.** The five cyclic modules are irreducible, their highest weights are distinct and their dimensions sum to $25$; a multiplicity would make the sum exceed $25$ or the character differ.

## The Ladder

### The Lowering of the Chain Vectors

**Proposition.** The lowering operator acts on the chain vectors by

$$
\operatorname{ad}_{J_-}X_0=0,\qquad
\operatorname{ad}_{J_-}X_1=-2J_3,\qquad
\operatorname{ad}_{J_-}X_4=2E_{25}-2E_{14},
$$

$$
\operatorname{ad}_{J_-}X_3=\sqrt6(E_{35}-E_{13}),
$$

$$
\operatorname{ad}_{J_-}X_2=-2\sqrt6E_{12}-2E_{23}+2E_{34}+2\sqrt6E_{45}.
$$

**Proof.** Apply the lowering formula term by term.

For $X_1=J_+=\sum_kc_kE_{k,k+1}$, the lowering of each simple unit is

$$
\operatorname{ad}_{J_-}E_{k,k+1}=c_kE_{k+1,k+1}-c_kE_{k,k},
$$

so

$$
\operatorname{ad}_{J_-}J_+=\sum_{k=1}^{4}c_k^2(E_{k+1,k+1}-E_{kk})=-2J_3,
$$

because $c_k^2=k(5-k)$ and the telescoping sum gives the diagonal entries $2(3-k)=2m_k$.

For $X_4=E_{15}$: $\operatorname{ad}_{J_-}E_{15}=c_1E_{25}-c_4E_{14}=2E_{25}-2E_{14}$.

For $X_3=E_{14}+E_{25}$:

$$
\operatorname{ad}_{J_-}E_{14}=c_1E_{24}-c_3E_{13}=2E_{24}-\sqrt6E_{13},
$$

$$
\operatorname{ad}_{J_-}E_{25}=c_2E_{35}-c_4E_{24}=\sqrt6E_{35}-2E_{24},
$$

and the sum is $\sqrt6(E_{35}-E_{13})$.

For $X_2=2E_{13}+\sqrt6E_{24}+2E_{35}$:

$$
2\operatorname{ad}_{J_-}E_{13}=4E_{23}-2\sqrt6E_{12},
$$

$$
\sqrt6\operatorname{ad}_{J_-}E_{24}=6E_{34}-6E_{23},
$$

$$
2\operatorname{ad}_{J_-}E_{35}=2\sqrt6E_{45}-4E_{34},
$$

and the sum is $-2\sqrt6E_{12}-2E_{23}+2E_{34}+2\sqrt6E_{45}$.

### The Weight Diagram

The weights of $\mathfrak{gl}_5$ under $\operatorname{ad}_{J_3}$ and their multiplicities are

| weight $r$ | $-4$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|---|---|---|---|---|
| multiplicity | $1$ | $2$ | $3$ | $4$ | $5$ | $4$ | $3$ | $2$ | $1$ |

The five summands contribute the following weights:

| module | dimension | weights |
|---|---|---|
| $V_0$ | $1$ | $0$ |
| $V_1$ | $3$ | $-1,0,1$ |
| $V_2$ | $5$ | $-2,-1,0,1,2$ |
| $V_3$ | $7$ | $-3,-2,-1,0,1,2,3$ |
| $V_4$ | $9$ | $-4,-3,-2,-1,0,1,2,3,4$ |

The sum of the multiplicities in each weight is the multiplicity in the table: at weight $0$, all five modules contribute, $1+1+1+1+1=5$; at weight $1$, the modules $V_1,V_2,V_3,V_4$ contribute, $4$; at weight $4$, only $V_4$ contributes, $1$.

**Proposition.** The weight multiplicities determine the chain: the multiplicity of $V_j$ is the difference of the multiplicities of the weights $j$ and $j+1$,

$$
m_j=5-|j|-(5-|j+1|)=1,\qquad j=0,1,2,3,4.
$$

**Proof.** In a sum of highest-weight modules, the multiplicity of the weight $r$ is $\sum_{j\ge|r|}m_j$; subtracting consecutive weights gives $m_j$. The values are $5-4=1$, $4-3=1$, $3-2=1$, $2-1=1$, $1-0=1$.

### The Chain from $E_{15}$

The top vector $E_{15}$ has weight $4$. The first lowering is

$$
E_{15}\longmapsto 2E_{25}-2E_{14},
$$

of weight $3$, and the next is

$$
2E_{25}-2E_{14}\longmapsto 2(\sqrt6E_{35}-2E_{24})-2(2E_{24}-\sqrt6E_{13})
=2\sqrt6E_{13}-8E_{24}+2\sqrt6E_{35},
$$

of weight $2$. The chain continues through weights $1,0,-1,-2,-3,-4$, with one vector at each weight in the module $V_4$; the nine vectors span the nine-dimensional summand. The lower weights are reached by the two moves of the formula, down a row and left a column; the chain is the orbit of $E_{15}$ under $\operatorname{ad}_{J_-}$.

**Remark.** The chain from $E_{15}$ is **not** the simple list $E_{15},E_{25},E_{35},E_{45},E_{55}$: the lowering also moves the column index, and the orbit at weight $0$ is not $E_{55}$ alone. The correct orbit is the full nine-dimensional module; the five-vector list is only the "row" part of the chain, and it omits the "column" part. The formula displays both moves, and the weight diagram displays the result.

## The Comparison with $n=2$

### The Biquaternion Chain

For $n=2$ the generators are

$$
J_3=\frac12\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
J_+=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
J_-=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
$$

The carrier is $\mathbb{C}^2=V_{1/2}$, of weights $\pm\tfrac12$, and the adjoint is

$$
\mathfrak{gl}_2=V_0\oplus V_1,\qquad 1+3=4 .
$$

The chain vectors are $X_0=I$ and $X_1=J_+$; the lowering is $\operatorname{ad}_{J_-}J_+=-2J_3$, $\operatorname{ad}_{J_-}J_3=J_-$, $\operatorname{ad}_{J_-}J_-=0$. The chain is $J_+\to-2J_3\to-2J_-$, of weights $1,0,-1$; rescaling the last vector gives $J_+\to-2J_3\to J_-$.

**Proof.** The matrices satisfy the $\mathfrak{sl}_2$ relations with $c_1=1$; the formulas are the $n=2$ case of the lowering formula. The adjoint dimensions are $1+3=4=\dim\mathfrak{gl}_2$.

### The Absence of Chirality

**Theorem.** For $n=5$ the carrier $V_2=\mathbb{C}^5$ is self-conjugate and has no chirality: its weights are symmetric under $m\mapsto-m$, and the adjoint decomposition $1+3+5+7+9$ is multiplicity-free. There is no pair of inequivalent half-spin modules.

**Proof.** The weights of $V_2$ are $2,1,0,-1,-2$, symmetric under $m\mapsto-m$. The dual of $V_2$ is isomorphic to $V_2$ by the invariant apolar pairing. The five summands of the adjoint have highest weights $0,1,2,3,4$, each once; there is no half-integer highest weight and no pair of modules exchanged by conjugation. The half-integer weights occur only at $n=2$, where the carrier is the spinor $V_{1/2}$; at $n=5$ the carrier is the spin-2 module $V_2$.

**Corollary.** The spin-two chain is a single self-conjugate chain of integer weights. The word *chirality* does not apply to $M_5(\mathbb{C})$; the carrier is a real (self-conjugate) module, and the adjoint is the tensor square $V_2\otimes V_2$, the sum of the symmetric square $V_0\oplus V_2\oplus V_4$ and the exterior square $V_1\oplus V_3$, decomposed without chirality.

**Proof.** A chirality is a splitting of a spinor module into two halves exchanged by the conjugation. At $n=5$ there is no spinor module: the carrier $V_2$ has integer weights and no half-integer highest weight. The adjoint decomposition is multiplicity-free, so there is no pair of conjugate half-spin modules to exchange. The self-conjugacy is the apolar pairing.

**Remark.** **The comparison is a comparison of the carrier, not of the algebra.** At $n=2$ the carrier is the spinor and the algebra is the biquaternion model; at $n=5$ the carrier is the spin-two module and the algebra is $M_5$. The adjoint chain $1+3$ at $n=2$ and $1+3+5+7+9$ at $n=5$ are the same construction applied to the two carriers; the difference of the weights, half-integer versus integer, is the difference of the two spin chains.

## Summary

The adjoint decomposition of $\mathfrak{gl}_5$ is exhibited by the five highest weight vectors

$$
X_0=I,\quad X_1=J_+,\quad X_2=2E_{13}+\sqrt6E_{24}+2E_{35},\quad X_3=E_{14}+E_{25},\quad X_4=E_{15},
$$

of weights $0,1,2,3,4$. The cyclic modules have dimensions $1,3,5,7,9$, and their sum is $25$:

$$
\boxed{\ \mathfrak{gl}_5=V_0\oplus V_1\oplus V_2\oplus V_3\oplus V_4,\qquad 1+3+5+7+9=25.\ }
$$

The lowering formula is

$$
(\operatorname{ad}_{J_-})E_{ij}=c_iE_{i+1,j}-c_{j-1}E_{i,j-1},\qquad c_k=\sqrt{k(5-k)},
$$

with $c_0=c_5=0$. The weight multiplicities are $1,2,3,4,5,4,3,2,1$; the chain from $E_{15}$ is the nine-dimensional module $V_4$; the lower summands are generated by $X_3,X_2,X_1,X_0$. The chain is multiplicity-free, and the carrier is self-conjugate: there is no chirality at $n=5$.

| Module | Highest weight vector | Highest weight | Dimension |
|---|---|---|---|
| $V_0$ | $I$ | $0$ | $1$ |
| $V_1$ | $J_+$ | $1$ | $3$ |
| $V_2$ | $2E_{13}+\sqrt6E_{24}+2E_{35}$ | $2$ | $5$ |
| $V_3$ | $E_{14}+E_{25}$ | $3$ | $7$ |
| $V_4$ | $E_{15}$ | $4$ | $9$ |
| Total | | | $25$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J_3,J_+,J_-$ | The spin-two generators, with $J_-=J_+^{\mathsf T}$ |
| $c_k=\sqrt{k(5-k)}$ | The ladder coefficients $2,\sqrt6,\sqrt6,2$ |
| $X_j$ | The highest weight vector of the summand $V_j$ |
| $V_j$ | The irreducible module of highest weight $j$, dimension $2j+1$ |
| $\operatorname{ad}_{J_-}$ | The lowering operator of the adjoint representation |
| $E_{ij}$ | The matrix unit, of weight $j-i$ |

## Further Reading

- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the highest-weight classification, the Clebsch–Gordan decomposition and the weight diagrams of $\mathfrak{sl}_2$.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the highest weight vectors, the cyclic modules and the character argument.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, second edition, 2015), for the compact real form and the $*$-unitary generators.
- [The Spin Chain and the Adjoint Decomposition of $M_5(\mathbb{C})$](the-spin-chain-and-the-adjoint-decomposition-of-m5c.html), for the carrier, the generators and the Clebsch–Gordan proof of the decomposition.
- [The Peirce Decomposition of $M_5(\mathbb{C})$](the-peirce-decomposition-of-m5c.html), for the matrix units and the Peirce lines that carry the weights.
- [The Frame, the Simple Nilpotents and the Gauge of $M_5(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-of-m5c.html), for the gauge that rescales the simple nilpotents and the ladder coefficients.
- [The Modules and the Minimal Left Ideals of $M_5(\mathbb{C})$](the-modules-and-the-minimal-left-ideals-of-m5c.html), for the carrier as a module and the distinction between the carrier and the Peirce lines.
