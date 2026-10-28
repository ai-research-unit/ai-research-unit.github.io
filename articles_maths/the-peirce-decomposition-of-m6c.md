# __The Peirce Decomposition__

## Introduction

A complete orthogonal family of idempotents cuts an algebra into corners, and the product respects the cut. For $M_6(\mathbb{C})$ the family is the six Lagrange projectors of a root, and the cut is the finest one: thirty-six lines, one for each ordered pair of eigenvalues. Grouping the lines by a single projector gives the coarse cut of a rank-one idempotent, with corners of dimensions $1,5,5,25$. This article states both cuts, the multiplication rule between the corners, the corner isomorphisms, and the comparison with the four lines of $M_2(\mathbb{C})$.

The article is a decomposition and nothing else. **A Peirce space is a subspace of the algebra, not a spinor.** No minimal left ideal, no column and no element of a Peirce line is called a spinor here; the modules are *The Modules and the Minimal Left Ideals*, and the carrier of the spin chain is *The Spin Chain and the Adjoint Decomposition*.

The article assumes the root and its Lagrange projectors of *Roots of Unity and the Lagrange Idempotents*, and the algebra $M_6(\mathbb{C})$ of *The Matrix Algebra $M_6(\mathbb{C})$*. It uses no form and no topology. The general Peirce theory is *Complementary Idempotents and the Peirce Decomposition*; the corner dimensions for the other ranks are *The Rank-Two and Rank-Three Splits*; the idempotent geometry is *The Geometry of the Idempotents*.

## The Peirce Decomposition of a Complete Family

### The General Construction

**Definition.** Let $A$ be an associative algebra with unit and let $e_1,\dots,e_n$ be a complete orthogonal family of idempotents: $e_i^2=e_i$, $e_ie_j=0$ for $i\neq j$, and $\sum_ie_i=1$. The **Peirce spaces** of the family are

$$
A_{ij}=e_iAe_j=\{e_ia e_j:a\in A\},
\qquad i,j=1,\dots,n .
$$

**Proposition (the direct sum).** $A=\bigoplus_{i,j}A_{ij}$.

**Proof.** For every $a\in A$,

$$
a=\Bigl(\sum_ie_i\Bigr)a\Bigl(\sum_je_j\Bigr)=\sum_{i,j}e_iae_j,
$$

so the sum covers $A$. If $\sum_{ij}a_{ij}=0$ with $a_{ij}\in A_{ij}$, multiply on the left by $e_r$ and on the right by $e_s$: the only surviving term is $a_{rs}$, so every $a_{rs}=0$.

**Proposition (the multiplication rule).** $A_{ij}A_{kl}\subseteq\delta_{jk}A_{il}$.

**Proof.** $e_ia e_j\cdot e_kb e_l=e_ia(e_je_k)be_l=\delta_{jk}e_i(ab)e_l$.

The rule is the whole content of the Peirce decomposition: the corners multiply like the entries of a matrix, and a product of two corners is zero unless the inner indices match.

### The Six Lines of the Root

Let $H$ be a root and $P_1,\dots,P_6$ its Lagrange projectors, as in *Roots of Unity and the Lagrange Idempotents*. The family is complete and orthogonal, so the general construction applies.

**Theorem.** The Peirce spaces of the family $(P_1,\dots,P_6)$ are the thirty-six lines

$$
A_{kl}=P_kM_6(\mathbb{C})P_l=\mathbb{C}E_{kl},
$$

where $E_{kl}$ is the matrix unit of the eigenbasis of $H$. They satisfy

$$
M_6(\mathbb{C})=\bigoplus_{k,l=1}^{6}A_{kl},
\qquad
\dim_{\mathbb{C}}A_{kl}=1,
\qquad
A_{kl}A_{mn}\subseteq\delta_{lm}A_{kn}.
$$

**Proof.** The space $A_{kl}$ is the image of the map $A\mapsto P_kAP_l$. Since $P_k$ and $P_l$ are rank-one projections onto $V_k$ and $V_l$, the map has rank one, and its image is spanned by any nonzero sandwich, for instance $v_kv_l^{\vee}=E_{kl}$ in the eigenbasis. The direct sum is the general proposition, and the product rule is the general rule with $e_k=P_k$.

**Definition.** The **Peirce coordinates** of $A\in M_6(\mathbb{C})$ in the root frame are the thirty-six numbers $a_{kl}$ defined by

$$
A=\sum_{k,l}a_{kl}E_{kl},
\qquad a_{kl}\in\mathbb{C}.
$$

The matrix $(a_{kl})$ is the matrix of $A$ in the eigenbasis $(v_0,\dots,v_5)$ of $H$, with $v_k$ a generator of $V_k$. **The Peirce coordinates are the entries of the matrix in the frame, and nothing more.**

### A Worked Example

Take the root $H=\operatorname{diag}(\zeta_0,\dots,\zeta_5)$ and the element

$$
A=\begin{pmatrix}
1&2&0&0&0&0\\
3&4&5&0&0&0\\
0&6&7&0&0&0\\
0&0&0&8&0&0\\
0&0&0&0&9&0\\
0&0&0&0&0&10
\end{pmatrix}.
$$

Its Peirce coordinates are its entries: $a_{00}=1$, $a_{01}=2$, $a_{10}=3$, $a_{11}=4$, $a_{12}=5$, $a_{21}=6$, $a_{22}=7$, $a_{33}=8$, $a_{44}=9$, $a_{55}=10$, and all other $a_{kl}=0$. The Peirce decomposition records which entries vanish and which do not; it does not change the matrix.

## The Coarse Split by a Rank-One Idempotent

### The Four Corners

Let $P$ be a rank-one idempotent and $Q=I_6-P$ its complement. The pair $(P,Q)$ is a complete orthogonal family with two members, and the general construction gives four corners:

$$
M_6(\mathbb{C})=P M_6P\oplus P M_6Q\oplus Q M_6P\oplus Q M_6Q .
$$

**Theorem (the corner dimensions).** With $\operatorname{rank}P=1$ and $\operatorname{rank}Q=5$,

$$
\dim PM_6P=1,\qquad
\dim PM_6Q=5,\qquad
\dim QM_6P=5,\qquad
\dim QM_6Q=25,
$$

and

$$
1+5+5+25=36 .
$$

**Proof.** Choose linear coordinates in which $P=\operatorname{diag}(1,0,0,0,0,0)$ and $Q=\operatorname{diag}(0,1,1,1,1,1)$. Then $PAP$ has only the $(1,1)$ entry, $PAQ$ only the first row and the last five columns, $QAP$ only the first column and the last five rows, and $QBQ$ only the bottom-right $5\times5$ block. The dimensions are the numbers of entries in those blocks.

**Corollary.** The four corners are the images of the four projections $A\mapsto PAQ$ and so on, and they are the entries of the block matrix

$$
A=\begin{pmatrix}
\alpha & r\\
c & B
\end{pmatrix},
\qquad
\alpha\in\mathbb{C},\ r\in\mathbb{C}^{1\times5},\ c\in\mathbb{C}^{5\times1},\ B\in\mathbb{C}^{5\times5}.
$$

The map $A\mapsto(\alpha,r,c,B)$ is an isomorphism of vector spaces, and it is the coarse Peirce coordinate system.

### The Corner Isomorphisms

**Theorem.** Let $P$ be a rank-one idempotent and $Q=I_6-P$. Then:

- $P M_6P\cong\mathbb{C}$, by $\lambda P\mapsto\lambda$;
- $Q M_6Q\cong M_5(\mathbb{C})$, as unital algebras with unit $Q$;
- $P M_6Q\cong\operatorname{Hom}(\operatorname{im}Q,\operatorname{im}P)\cong\mathbb{C}^5$;
- $Q M_6P\cong\operatorname{Hom}(\operatorname{im}P,\operatorname{im}Q)\cong\mathbb{C}^5$.

**Proof.** Every element of $P M_6P$ is $PAP=\lambda P$ with $\lambda\in\mathbb{C}$, because $P$ has rank one and its image is a line; the map is a unital algebra isomorphism onto $\mathbb{C}$ when $\mathbb{C}$ is read with unit $1$. The corner $Q M_6Q$ acts faithfully on $\operatorname{im}Q$, a space of dimension five, and every endomorphism of $\operatorname{im}Q$ is of the form $QBQ$ on that space; so $Q M_6Q\cong\operatorname{End}(\operatorname{im}Q)\cong M_5(\mathbb{C})$. An element $PAQ$ is a linear map from $\operatorname{im}Q$ to $\operatorname{im}P$: it kills $\ker Q$ and lands in $\operatorname{im}P$; the map $PAQ\mapsto(PAQ)|_{\operatorname{im}Q}$ is an isomorphism onto $\operatorname{Hom}(\operatorname{im}Q,\operatorname{im}P)$, a space of dimension $5$. The fourth statement is the same with the roles exchanged.

**Corollary (the diagonal corners are the two blocks).** The diagonal corner $P M_6P$ is the line of scalars of the first block, and $Q M_6Q$ is the full matrix algebra of the second block. **The coarse split is not symmetric in the two diagonal corners**: one is a line, the other is $M_5$.

### The Peirce Table

The multiplication of the four corners is the block multiplication of the matrix above. The table gives the corner containing the product; the entry $0$ means that every product of an element of the row corner with an element of the column corner vanishes.

| $\cdot$ | $PMP$ | $PMQ$ | $QMP$ | $QMQ$ |
|---|---|---|---|---|
| $PMP$ | $PMP$ | $PMQ$ | $0$ | $0$ |
| $PMQ$ | $0$ | $0$ | $PMP$ | $PMQ$ |
| $QMP$ | $QMP$ | $QMQ$ | $0$ | $0$ |
| $QMQ$ | $0$ | $0$ | $QMP$ | $QMQ$ |

**Proof.** Read the table off the general rule $A_{ij}A_{kl}\subseteq\delta_{jk}A_{il}$ with $i,j,k,l\in\{+,-\}$, $+=P$ and $-{}=Q$. The nonvanishing entries are the compositions of composable arrows $+\to-$, $-\to+$, $+\to+$ and $-\to-$.

The block product is

$$
\begin{pmatrix}\alpha&r\\c&B\end{pmatrix}
\begin{pmatrix}\alpha'&r'\\c'&B'\end{pmatrix}
=
\begin{pmatrix}
\alpha\alpha'+rc' & \alpha r'+rB'\\
c\alpha'+Bc' & cr'+BB'
\end{pmatrix},
$$

with $rc'$ the pairing of a row and a column, and the four entries are the four corners.

### The All-Ones Example

**Example.** Let $u=(1,1,1,1,1,1)$, $P=\tfrac16uu^{\mathsf T}=\tfrac16J$ the orthogonal projection onto the line spanned by $u$, and $Q=I_6-P$ the projection onto the hyperplane $\{x:\sum_ix_i=0\}$. Then

$$
PAP=\frac{\sigma(A)}{6}P,\qquad \sigma(A)=\sum_{i,j}A_{ij},
$$

and the four corners are described by the row and column sums:

| Corner | Description | Dimension |
|---|---|---|
| $PMP$ | multiples of $P$, coordinate $\sigma(A)/6$ | $1$ |
| $PMQ$ | matrices all of whose rows are equal and whose row sum is zero | $5$ |
| $QMP$ | matrices all of whose columns are equal and whose column sum is zero | $5$ |
| $QMQ$ | matrices with every row sum and every column sum zero | $25$ |

**Proof.** $PAP=(J/6)A(J/6)=(1^{\mathsf T}A1)J/36=(\sigma(A)/6)P$. The corner $PMQ$ is $(J/6)AQ$: the rows of $JA$ are all equal to $1^{\mathsf T}A$, and right multiplication by $Q$ removes the mean of each row, so every row becomes the same zero-sum row. The corner $QMP$ is the same computation with rows exchanged for columns. The corner $QMQ$ is $QAQ$: left multiplication by $Q$ makes every column sum zero, right multiplication makes every row sum zero. The dimensions are the dimensions of the spaces of zero-sum rows, zero-sum columns and matrices with both sums zero, namely $5,5,25$.

For the concrete matrix

$$
A=\begin{pmatrix}
1&2&3&4&5&6\\
7&8&9&10&11&12\\
13&14&15&16&17&18\\
19&20&21&22&23&24\\
25&26&27&28&29&30\\
31&32&33&34&35&36
\end{pmatrix},
$$

the total sum is $\sigma(A)=666$, so $PAP=111P$. The column means are $(16,17,18,19,20,21)$, whose own mean is $18.5$; the corner $PMQ$ is the matrix whose six rows all equal

$$
(16,17,18,19,20,21)-18.5\,(1,1,1,1,1,1)=(-2.5,-1.5,-0.5,0.5,1.5,2.5).
$$

The row means are $(3.5,9.5,15.5,21.5,27.5,33.5)$, whose own mean is again $18.5$; the corner $QMP$ is the matrix whose six columns all equal

$$
(-15,-9,-3,3,9,15).
$$

The corner $QMQ$ is $A$ minus the three displayed parts, and its row and column sums vanish.

**Remark.** The example is the rank-one Hermitian idempotent of the diagonal action of $S_6$ on $\mathbb{C}^6$. It shows that the coarse split is available for any rank-one idempotent, not only for a coordinate one, and that the four corners have intrinsic descriptions: the mean, the zero-sum row, the zero-sum column and the doubly zero-sum part.

## The Refinement of the Coarse Split

**Theorem.** The fine Peirce decomposition refines the coarse one. With $P=P_1$ and $Q=P_2+\cdots+P_6$,

$$
PMP=A_{11},\qquad
PMQ=\bigoplus_{l=2}^{6}A_{1l},\qquad
QMP=\bigoplus_{k=2}^{6}A_{k1},\qquad
QMQ=\bigoplus_{k,l=2}^{6}A_{kl}.
$$

**Proof.** $P_1M P_1=A_{11}$. The corner $P_1MQ$ is the sum of the lines $P_1MP_l$ for $l\neq1$, because $Q$ is the sum of the $P_l$ with $l\neq1$ and the $P_l$ are orthogonal. The other two statements are the same computation.

The refinement is therefore a partition of the coarse corners into lines:

| Coarse corner | Fine lines | Number | Dimension |
|---|---|---|---|
| $PMP$ | $A_{11}$ | $1$ | $1$ |
| $PMQ$ | $A_{12},\dots,A_{16}$ | $5$ | $5$ |
| $QMP$ | $A_{21},\dots,A_{61}$ | $5$ | $5$ |
| $QMQ$ | $A_{kl}$, $k,l\neq0$ | $25$ | $25$ |

The coarse split forgets the distinction between the five lines inside each off-diagonal corner and between the twenty-five lines inside $QMQ$. **The fine split is the one that sees the root; the coarse split sees only one idempotent.**

## The Comparison with the Four Lines of $M_2(\mathbb{C})$

The biquaternion algebra is $\mathbb{B}\cong M_2(\mathbb{C})$, and its Peirce decomposition relative to a complete pair of primitive idempotents has four corners, each a line. The coarse split by one rank-one idempotent gives the same four lines.

**Proposition.** Let $P$ be a rank-one idempotent of $M_2(\mathbb{C})$ and $Q=I_2-P$. Then

$$
\dim PM_2P=\dim PM_2Q=\dim QM_2P=\dim QM_2Q=1,
$$

so the coarse corners are $1+1+1+1$.

**Proof.** The dimension formula for $M_n(\mathbb{C})$ with $\operatorname{rank}P=p$ is $p^2+p(n-p)+(n-p)p+(n-p)^2=n^2$; at $n=2$, $p=1$ it gives $1+1+1+1=4$.

**Corollary (coarse equals fine).** In $M_2(\mathbb{C})$ the coarse split by a rank-one idempotent coincides with the fine Peirce decomposition relative to the complete pair $(P,Q)$. There is no room for a further refinement: both diagonal corners are lines, as are the two off-diagonal corners.

**Proof.** The four coarse corners have dimensions $1,1,1,1$, and the fine decomposition has one line for each ordered pair; the four lines are the same four corners.

**Remark (the contrast).** In $M_6(\mathbb{C})$ the same construction gives $1+5+5+25$, and the fine decomposition is strictly finer: the diagonal corner $QMQ$ is $M_5$, not a line. The biquaternion case is the case $n=2$, where the complement of a line is a line; the six-line case is the case $n=6$, where the complement of a line is five-dimensional. **The coincidence of coarse and fine is an accident of dimension two, and it is the reason the biquaternion Peirce decomposition has exactly four lines.**

## Summary

The Peirce decomposition of $M_6(\mathbb{C})$ relative to the six Lagrange projectors of a root is the direct sum of the thirty-six lines $A_{kl}=P_kM_6P_l=\mathbb{C}E_{kl}$, with the multiplication rule $A_{kl}A_{mn}\subseteq\delta_{lm}A_{kn}$.

The coarse split by a rank-one idempotent $P$, with $Q=I_6-P$, has four corners of dimensions $1,5,5,25$:

$$
M_6(\mathbb{C})=PMP\oplus PMQ\oplus QMP\oplus QMQ,
\qquad
PMP\cong\mathbb{C},\quad QMQ\cong M_5(\mathbb{C}),
$$

and the off-diagonal corners are the two spaces $\mathbb{C}^5$ of homomorphisms between the image line and the kernel hyperplane.

$$
\boxed{\ \text{The fine split has }36\text{ lines; the coarse split has }1+5+5+25\text{ and is the block form of a matrix.}\ }
$$

In $M_2(\mathbb{C})$ the coarse split is already the fine one, with four lines, because the complement of a line is a line. The refinement in $M_6$ replaces the corner $QMQ$ by the twenty-five lines $A_{kl}$ with $k,l\neq0$.

| Split | Corners | Dimensions |
|---|---|---|
| Fine, six projectors | $A_{kl}$, $k,l=1,\dots,6$ | $36\times1$ |
| Coarse, one rank-one $P$ | $PMP,PMQ,QMP,QMQ$ | $1+5+5+25$ |
| Coarse, $M_2$ | $PMP,PMQ,QMP,QMQ$ | $1+1+1+1$ |
| $\mathbb{Z}/6$ graded pieces | $A_r=\bigoplus_{k-l\equiv r}A_{kl}$ | $6+6+6+6+6+6$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P_k$ | the six Lagrange projectors of a root |
| $A_{kl}=P_kM_6P_l$ | the Peirce line of the pair $(k,l)$ |
| $a_{kl}$ | the Peirce coordinate of $A$ on $E_{kl}$ |
| $P,Q=I_6-P$ | a rank-one idempotent and its complement |
| $PMP$ etc. | the four coarse corners |
| $\alpha,r,c,B$ | the coarse Peirce coordinates, of sizes $1,1\times5,5\times1,5\times5$ |
| $\sigma(A)=\sum_{i,j}A_{ij}$ | the total sum in the all-ones example |

## Further Reading

- [Roots of Unity and the Lagrange Idempotents](roots-of-unity-and-the-lagrange-idempotents-of-m6c.html), for the root and the six projectors.
- [The Frame, the Simple Nilpotents and the Gauge](the-frame-the-simple-nilpotents-and-the-gauge-of-m6c.html), for the matrix units and the five-parameter gauge.
- [The Rank-Two and Rank-Three Splits](the-rank-two-and-rank-three-splits-of-m6c.html), for the coarse splits with corners $4+8+8+16$ and $9+9+9+9$.
- [The Modules and the Minimal Left Ideals](the-modules-and-the-minimal-left-ideals-of-m6c.html), for the modules generated by the idempotents.
- [Complementary Idempotents and the Peirce Decomposition](complementary-idempotents-and-the-peirce-decomposition.html), for the general Peirce theory.
- [Off-Diagonal Peirce Components and Noncentral Idempotents](off-diagonal-peirce-components-and-noncentral-idempotents.html), for the corner multiplication in the general case.
- [Primitive Idempotents and Minimal Left Ideals](primitive-idempotents-and-minimal-left-ideals.html), for the rank-one idempotents and their ideals.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition and the corner multiplication.
- Israel Nathan Herstein, *Noncommutative Rings* (Carus Mathematical Monographs, 1968), for the idempotent refinements and the matrix units.
