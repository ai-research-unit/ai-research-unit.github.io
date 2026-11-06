# __The One-Sided Operators of $M_n(\mathbb{C})$__

## Introduction

**The question.** A matrix $A$ acts on the matrix algebra by left multiplication, $X\mapsto AX$, and a matrix $B$ acts by right multiplication, $X\mapsto XB$. Both are operators on the $n^{2}$ complex dimensions of $M_{n}(\mathbb{C})$, hence matrices of size $n^{2}$. This article computes those matrices, their rank, their trace and their determinant, and describes the two subsets of $\operatorname{End}(M_{n})$ that they fill.

**The result in one line.** Left multiplication is $\mathrm I_{n}\otimes A$, right multiplication is $B^{\mathsf T}\otimes\mathrm I_{n}$, the two subsets are copies of $M_{n}$ and of $M_{\mathrm{opp},n}$ that commute and meet in the scalars, and each is the commutant of the other.

**Why the article is needed.** The two-sided operators are built from the two one-sided families, and every count of the companion articles starts from the dimensions $n^{2}+n^{2}-1=2n^{2}-1$ and $n^{4}$. The one-sided case is also the only case in which the invariants of the operator are read off the parameter without any tensor rank computation: the rank of $L_{A}$ is $n$ times the rank of $A$, and the determinant is the $n$-th power.

**Boundaries.** The algebra and its trace and determinant are *The Matrix Algebra $M_n(\mathbb{C})$*. The general construction is *The Regular Representation in Dimension $n$*. The two-sided products are *The Two-Sided Operators and the Segre Cone of $M_n(\mathbb{C})$*. At $n=2$ the same matrices in the Peirce frame are the two four-dimensional copies of *$M_4(\mathbb{C})$ Pauli Representation : Operators*, and the pair description is *$M_2(\mathbb{C})$ Pauli Representation : Operators*.

**Conventions.** The algebra is $A=M_{n}(\mathbb{C})$, of complex dimension $N=n^{2}$. An element $X$ is written as a column $\operatorname{vec}X$ by stacking its columns, so that $\operatorname{vec}(AX)=(\mathrm I_{n}\otimes A)\operatorname{vec}X$ and $\operatorname{vec}(XB)=(B^{\mathsf T}\otimes\mathrm I_{n})\operatorname{vec}X$. An operator on the algebra is an $N\times N$ matrix; the identity operator is $\mathrm I_{N}$. The transpose of a matrix is ${}^{\mathsf T}$ and the conjugate transpose is ${}^{*}$.

## The Left Multiplication

### The Matrix

**Proposition (the Kronecker form).** In the column-stacking basis,
$$
[L_{A}]=\mathrm I_{n}\otimes A,
$$
the block matrix of $n^{2}$ blocks of size $n$, with $A$ on the diagonal and zeros elsewhere.

*Proof.* The column $\operatorname{vec}(AX)$ is the stack of the columns of $AX$. The $j$-th column of $AX$ is $A$ times the $j$-th column of $X$, so the operator acts as $A$ on each block of $n$ consecutive coordinates and does not mix the blocks. This is the block-diagonal matrix with $n$ copies of $A$.

**The display.** For $n=2$ and $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$,
$$
[L_{A}]=\begin{pmatrix}
a&b&0&0\\
c&d&0&0\\
0&0&a&b\\
0&0&c&d
\end{pmatrix},
$$
which is the form used in the biquaternion articles, where $A=\mathsf M_{2}(\tilde Q)$ and the four entries are the coordinates of the element.

### The Invariants

**Theorem (rank, trace, determinant).** For every $A\in M_{n}(\mathbb{C})$,
$$
\operatorname{rank}L_{A}=n\operatorname{rank}A,\qquad
\operatorname{tr}L_{A}=n\operatorname{tr}A,\qquad
\det L_{A}=(\det A)^{n}.
$$

*Proof.* The matrix $\mathrm I_{n}\otimes A$ is block diagonal with $n$ blocks equal to $A$, so its rank is the sum of the ranks, its trace the sum of the traces, and its determinant the product of the determinants.

**The spectrum.** If the eigenvalues of $A$ are $\lambda_{1},\dots,\lambda_{n}$ with algebraic multiplicities, then the eigenvalues of $L_{A}$ are the same numbers, each repeated $n$ times. The spectral projector of $L_{A}$ at $\lambda$ is the left multiplication $L_{P}$ by the spectral projector of $A$ at $\lambda$, because $\mathrm I_{n}\otimes P$ is the matrix of $L_{P}$.

**The minimal polynomial does not grow.** The minimal polynomial of $L_{A}$ is the minimal polynomial of $A$, of degree at most $n$, while $L_{A}$ has size $n^{2}$. For $n\ge2$ the degree is strictly smaller than the size, so **the regular matrix is never nonderogatory**: there is no vector $X$ whose images under the powers of $L_{A}$ fill the algebra. This is the operator form of the fact that the left multiplication sees the algebra through a single element, and it is why the two-sided operators are needed for a general endomorphism.

### The Kernel and the Image

**The kernel.** The operator $L_{A}$ kills exactly the matrices whose columns lie in the kernel of $A$:
$$
\ker L_{A}=\{X:AX=0\},\qquad \dim\ker L_{A}=n\,(n-\operatorname{rank}A)=N-n\operatorname{rank}A .
$$
The dimension is the complement of the rank, as it must be.

**The image.** The image is the set of matrices whose columns lie in the column space of $A$:
$$
\operatorname{im}L_{A}=A\cdot M_{n}(\mathbb{C})=\{AX\},
$$
of dimension $n\operatorname{rank}A$. In particular the image is the whole algebra exactly when $A$ is invertible, and the operator $L_{A}$ is invertible exactly then, with $L_{A}^{-1}=L_{A^{-1}}$.

**The left ideal.** The image is a **left ideal**: it is closed under left multiplication by any matrix, because $C(AX)=(CA)X$. The kernel is not an ideal: it is closed under right multiplication, $AX=0$ gives $AXC=0$. The two properties are the module-theoretic reading of the operator.

## The Right Multiplication

### The Matrix

**Proposition (the Kronecker form).** In the column-stacking basis,
$$
[R_{B}]=B^{\mathsf T}\otimes\mathrm I_{n}.
$$

*Proof.* The $j$-th column of $XB$ is $X$ times the $j$-th column of $B$, that is $\sum_{k}B_{kj}x_{k}$ with $x_{k}$ the $k$-th column of $X$. The $j$-th block of the output is therefore $\sum_{k}B_{kj}x_{k}$, whose coefficients in the input blocks are the $j$-th column of $B$; the block matrix of the operator is thus $B^{\mathsf T}$, and since each block is multiplied by $\mathrm I_{n}$ on the left, the matrix is $B^{\mathsf T}\otimes\mathrm I_{n}$.

**The display.** For $n=2$,
$$
[R_{B}]=\begin{pmatrix}
b_{11}&0&b_{21}&0\\
0&b_{11}&0&b_{21}\\
b_{12}&0&b_{22}&0\\
0&b_{12}&0&b_{22}
\end{pmatrix},
$$
a block matrix whose four blocks are scalar multiples of $\mathrm I_{2}$. The transpose is not cosmetic: it is the difference between the left copy and the right copy, and it disappears only in the scalar case.

**The transpose is the reason both letters are needed.** The left copy is block diagonal with the element repeated; the right copy is block scalar with the transpose. A matrix that is both is a scalar matrix, and this is the computation of the next section.

### The Invariants

**Proposition.** For every $B$,
$$
\operatorname{rank}R_{B}=n\operatorname{rank}B,\qquad
\operatorname{tr}R_{B}=n\operatorname{tr}B,\qquad
\det R_{B}=(\det B)^{n}.
$$

*Proof.* The matrix $B^{\mathsf T}\otimes\mathrm I_{n}$ has $n^{2}$ blocks, each a scalar multiple of $\mathrm I_{n}$. Its rank, trace and determinant are the same functions of $B^{\mathsf T}$ as those of $\mathrm I_{n}\otimes B$ are of $B$, and $\operatorname{rank}B^{\mathsf T}=\operatorname{rank}B$, $\operatorname{tr}B^{\mathsf T}=\operatorname{tr}B$, $\det B^{\mathsf T}=\det B$.

**The right copy is an anti-representation.** The composition is $R_{B}R_{C}=R_{CB}$, so the map $B\mapsto R_{B}$ reverses the order. The set $\{R_{B}\}$ is a subalgebra of $\operatorname{End}(M_{n})$, isomorphic to $M_{\mathrm{opp},n}$, and $M_{\mathrm{opp},n}\cong M_{n}$ through the transpose. **The transpose is therefore the canonical comparison between the two copies, and it is an isomorphism of algebras and not an identification of subsets.**

### The Flip

**Proposition (the two copies are exchanged by the flip).** Let $\mathsf F$ be the flip of the two tensor slots, $\mathsf F(X\otimes Y)\mathsf F=Y\otimes X$, an involution of the $n^{2}$ dimensions with $\mathsf F=\mathsf F^{\mathsf T}=\mathsf F^{-1}$. Then
$$
\mathsf F\,[L_{A}]\,\mathsf F=[R_{A^{\mathsf T}}],\qquad
\mathsf F\,[R_{B}]\,\mathsf F=[L_{B^{\mathsf T}}].
$$

*Proof.* The flip sends $\mathrm I_{n}\otimes A$ to $A\otimes\mathrm I_{n}$, and $A\otimes\mathrm I_{n}=(A^{\mathsf T})^{\mathsf T}\otimes\mathrm I_{n}=[R_{A^{\mathsf T}}]$. The second identity is the first applied to $B^{\mathsf T}$.

**The flip is an operator and not an element.** It lives in $\operatorname{End}(M_{n}(\mathbb{C}))$ and not in the algebra, it exchanges the two copies, and it preserves neither the product of the algebra nor a single letter of the two families. In the biquaternion case the same role is played by the permutation $\mathsf S$ of the second and third coordinates of the frame, and the identity there reads $R_{\mathrm{pau}}(\tilde Q)=\mathsf S\,L_{\mathrm{pau}}(\tilde Q)^{\mathsf T}\mathsf S^{-1}$, which is the frame form of the proposition above.

## The Two Copies

### The Intersection

**Theorem (the two copies meet in the scalars).** For $n\ge2$,
$$
\{L_{A}\}\cap\{R_{B}\}=\mathbb{C}\cdot\mathrm I_{N}.
$$

*Proof.* Suppose $AX=XB$ for every $X$. With $X=I$ this gives $A=B$; then $AX=XA$ for every $X$, and the centre of $M_{n}(\mathbb{C})$ is $\mathbb{C}I$. Conversely a scalar matrix acts by the same scalar on the left and on the right.

**The dimension count.** Two subspaces of dimensions $n^{2}$ and $n^{2}$ with intersection of dimension one span a subspace of dimension $2n^{2}-1$. This is the third rung of the ladder, and it is also the dimension of the cone of two-sided products, although the two sets are different: the sum of the two copies is a subspace, the cone is not.

### The Double Centraliser

**Theorem.** Each copy is the commutant of the other in $\operatorname{End}(M_{n}(\mathbb{C}))$.

*Proof.* A right multiplication commutes with every left multiplication, because $A(XB)=(AX)B$. Conversely let $F$ commute with every $L_{C}$ and put $B=F(I)$; then $F(X)=F(L_{X}I)=L_{X}F(I)=XB$, so $F=R_{B}$.

**The reading.** The theorem says that **an operator that commutes with all left multiplications is a right multiplication**, and this is the reason the two-sided family is the natural next object: a general endomorphism is a sum of products of one member of each copy, and the number of terms needed is the length of the companion article.

### The Commutant of One Element

**Proposition.** Let $C(A)=\{Y\in M_{n}(\mathbb{C}):AY=YA\}$ be the centraliser of $A$ in the algebra. Then the commutant of $L_{A}$ in $\operatorname{End}(M_{n}(\mathbb{C}))$ is the set of operators $F(X)=\sum_{i}Y_{i}XZ_{i}$ with $Y_{i}\in C(A)$ and $Z_{i}$ arbitrary, of complex dimension
$$
n^{2}\dim C(A).
$$

*Proof.* Write an operator as $F=\sum_{i}Y_{i}\otimes Z_{i}$ in the tensor form $M_{n}\otimes M_{n}$, so that $F(X)=\sum_{i}Y_{i}XZ_{i}$. Then
$$
F(AX)-AF(X)=\sum_{i}Y_{i}A X Z_{i}-\sum_{i}AY_{i}XZ_{i}=\sum_{i}(Y_{i}A-AY_{i})XZ_{i},
$$
and $F$ commutes with $L_{A}$ exactly when $\sum_{i}(Y_{i}A-AY_{i})\otimes Z_{i}=0$. With the $Z_{i}$ independent this forces $Y_{i}\in C(A)$, and the space of such $F$ is $C(A)\otimes M_{n}$; the two factors give the same dimension.

**The two extremes.** For a cyclic element, $C(A)=\mathbb{C}[A]$ of dimension $n$, and the commutant of $L_{A}$ has dimension $n^{3}$. For a scalar element, $C(A)=M_{n}(\mathbb{C})$ of dimension $n^{2}$, and the commutant is the whole ambient space of dimension $n^{4}$. **The commutant of a single left multiplication is strictly larger than the right copy for every $n\ge2$ and every $A$, since $n^{2}\dim C(A)\ge n^{3}>n^{2}$, and its size is the size of the centraliser.**

**The table.**

| $A$ | $\dim C(A)$ | $\dim\{F:FC=CF\}$ for $C=L_{A}$ | at $n=3$ |
|---|---|---|---|
| all left multiplications taken together | --- | $n^{2}$ | $9$ |
| a scalar element | $n^{2}$ | $n^{4}$ | $81$ |
| a cyclic element, e.g. a single Jordan block | $n$ | $n^{3}$ | $27$ |
| $\operatorname{diag}(1,1,2)$ at $n=3$ | $5$ | $45$ | $45$ |

**The first row is the theorem and the other three are propositions about a single element.** The commutant of the whole copy is the right copy of dimension $n^{2}$; the commutant of a single member is strictly larger for $n\ge2$, the least being $n^{3}$ at a cyclic element. The second row is the degenerate case in which $L_{A}$ is the identity operator and every operator commutes with it.

### The Compression

**The compression to the $2\times2$ model.** At $n=2$ the algebra is the biquaternion algebra and the element is a $2\times2$ matrix $\mathsf M_{2}(\tilde Q)$. In the $2\times2$ model the left matrix compresses to $A$ and the right matrix compresses to $B^{\mathsf T}$: each is two identical blocks of the same $2\times2$ matrix. The two-sided product does not compress, because it is the $4\times4$ product $B^{\mathsf T}\otimes A$ and both tensor factors are needed. **The two one-sided actions compress one at a time, and this is why the pair description of the biquaternion category is written with one matrix per side and a pair for the product.**

## Summary

Left multiplication by $A$ is the block-diagonal matrix $\mathrm I_{n}\otimes A$ with $n$ copies of $A$; right multiplication by $B$ is the block-scalar matrix $B^{\mathsf T}\otimes\mathrm I_{n}$. Both have rank $n\operatorname{rank}$, trace $n\operatorname{tr}$ and determinant $(\det)^{n}$ of the parameter, and both have the spectrum of the parameter repeated $n$ times.

The two families are copies of $M_{n}$ and of $M_{\mathrm{opp},n}$; they commute, they meet in the scalars, their sum has dimension $2n^{2}-1$, and each is the commutant of the other. The commutant of a single left multiplication is $C(A)\otimes M_{n}$, of dimension $n^{2}\dim C(A)$: $n^{3}$ for a cyclic element and $n^{4}$ for a scalar one.

The regular matrix is never nonderogatory for $n\ge2$, because its minimal polynomial has degree at most $n$ against a size of $n^{2}$. **The one-sided operators are the two ends of the construction, and the two-sided products of the next article are the smallest family that reaches the rest of the ambient space.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M_{n}(\mathbb{C})$ | the algebra, of complex dimension $N=n^{2}$ |
| $L_{A}(X)=AX$ | the left multiplication |
| $R_{B}(X)=XB$ | the right multiplication |
| $[L_{A}]=\mathrm I_{n}\otimes A$ | its matrix in the column-stacking basis |
| $[R_{B}]=B^{\mathsf T}\otimes\mathrm I_{n}$ | its matrix in the same basis |
| $\mathrm I_{N}$ | the identity operator |
| $\mathsf F$ | the flip of the two tensor slots |
| $C(A)$ | the centraliser of $A$ in $M_{n}(\mathbb{C})$ |
| $\operatorname{End}_{L}$, $\operatorname{End}_{R}$ | the two copies inside $\operatorname{End}(M_{n})$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge, 1991), for the Kronecker products, the identities $(\mathrm I\otimes A)$ and $(B^{\mathsf T}\otimes\mathrm I)$, and the invariants of a Kronecker product.
- Paul Richard Halmos, *Finite-Dimensional Vector Spaces* (Springer, 1974), for the regular representation and the double centraliser.
- [The Matrix Algebra $M_n(\mathbb{C})$](the-matrix-algebra-mnc.html), for the algebra, its centre and its trace.
- [The Regular Representation in Dimension $n$](the-regular-representation-in-dimension-n.html), for the abstract construction and its ladder.
- [The Two-Sided Operators and the Segre Cone of $M_n(\mathbb{C})$](the-two-sided-operators-and-the-segre-cone-of-mnc.html), for the products of the two copies.
- [$M_4(\mathbb{C})$ Pauli Representation : Operators](m4c-pauli-representation-operators.html), for the same matrices at $n=2$ in the Peirce frame.
