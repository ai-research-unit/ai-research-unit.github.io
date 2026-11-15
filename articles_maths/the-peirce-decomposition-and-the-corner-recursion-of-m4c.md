# __The Peirce Decomposition and the Corner Recursion of $M_4(\mathbb{C})$__

## Introduction

**The corner $EM_4E$ of a rank-$k$ idempotent is a copy of $M_k(\mathbb{C})$ with unit $E$, and the whole algebra is rebuilt from the corner, its complement and the two rectangular blocks: $16=k^{2}+(4-k)^{2}+2k(4-k)$, with the trace adding over the two corners and the determinant obeying the Schur formula.**

The article identifies the corner with a matrix algebra, proves the block reassembly and the multiplication rules, writes the trace and the determinant in Peirce coordinates with the Schur complement, works the two recursions at $k=2$ and at $k=1$, tabulates the Peirce basis, and reads the recursion at $k=2$ as the Kronecker factorisation $M_4\cong M_2\otimes M_2$.

It assumes *The Peirce Decomposition and the Two Halves at $n=4$* for the spaces and *The Kronecker Factorisation $M_4(\mathbb{C})\cong M_2(\mathbb{C})\otimes M_2(\mathbb{C})$* for the tensor reading. The model at order two is *The Peirce Decomposition and the Corner Recursion of $M_2(\mathbb{C})$*.

## The Corner Is a Matrix Algebra

**Theorem.** For an idempotent $E$ of rank $k$ the corner $EM_4E$, with the multiplication of the algebra and the unit $E$, is isomorphic to $M_k(\mathbb{C})$.

**Proof.** Conjugate so that $E=\operatorname{diag}(1,\dots,1,0,\dots,0)$. Then $EME$ consists of the matrices with arbitrary $k\times k$ block in the top left and zeros elsewhere, and the map that keeps that block is an algebra isomorphism onto $M_k(\mathbb{C})$, carrying $E$ to $\mathrm I_k$.

**Corollary.** The complement $(1-E)M(1-E)$ is a copy of $M_{4-k}(\mathbb{C})$ with unit $1-E$, and the two corners are independent matrix algebras.

**Proof.** The same argument on the other block.

**Corollary.** $E$ is the identity of the corner and zero on the complement; an element $X$ is in the corner exactly when $EXE=X$.

**Proof.** $E(EAE)E=EAE$ and $E(1-E)M(1-E)E=0$.

**The idempotent as a projection.** The corner is the image of the projection $X\mapsto EXE$, and the complement is the image of $X\mapsto(1-E)X(1-E)$.

**Proof.** Both maps are idempotent linear maps with the images named.

## The Block Reassembly

**Theorem.** $M_4=V_{11}\oplus V_{10}\oplus V_{01}\oplus V_{00}$ as vector spaces, and in the corresponding block notation
$$
X=\begin{pmatrix}A&B\\ C&D\end{pmatrix},\qquad A\in M_k,\ B\in M_{k\times(4-k)},\ C\in M_{(4-k)\times k},\ D\in M_{4-k},
$$
the product is the block product and the dimensions are $k^{2}+k(4-k)+k(4-k)+(4-k)^{2}=16$.

**Proof.** Every matrix has a unique block decomposition, and the block product rule is the definition of the matrix product.

**Corollary.** The algebra is rebuilt from the two corner algebras and the two rectangular bimodules, and the multiplication of the pieces is the table $V_{ij}V_{kl}\subseteq\delta_{jk}V_{il}$.

**Proof.** The block product: the $B$ block multiplies into the $C$ block and the $C$ block multiplies into the $B$ block, which are the only two nonvanishing mixed products.

**The recursion in words.** $M_4$ is $M_k$ and $M_{4-k}$ glued by two rectangular blocks, and each gluing block is simultaneously a left module over one corner and a right module over the other.

**Proof.** $B$ is acted on by $A$ on the left and by $D$ on the right, and $C$ the other way round.

**Corollary.** The recursion terminates at matrices of size one, which are the scalars, so the algebra is built from the scalars by four gluing steps.

**Proof.** Repeated bisection of the index set reaches singletons.

## Trace and Determinant in Peirce Coordinates

**Proposition.** $\operatorname{tr}X=\operatorname{tr}A+\operatorname{tr}D$; the two mixed blocks do not contribute.

**Proof.** The diagonal of $X$ is the diagonal of $A$ followed by the diagonal of $D$.

**Corollary.** The trace splits over the corners, and the traceless part is the direct sum of the traceless parts of the two corners together with the two mixed blocks.

**Proof.** Subtract the two traces.

**Theorem (Schur).** If $A$ is invertible then
$$
\det X=\det A\cdot\det\bigl(D-CA^{-1}B\bigr),
$$
and the identity holds as a polynomial identity for all $X$.

**Proof.** The block factorisation
$$
\begin{pmatrix}A&B\\ C&D\end{pmatrix}=\begin{pmatrix}\mathrm I&0\\ CA^{-1}&\mathrm I\end{pmatrix}\begin{pmatrix}A&0\\0&D-CA^{-1}B\end{pmatrix}\begin{pmatrix}\mathrm I&A^{-1}B\\0&\mathrm I\end{pmatrix}
$$
has determinant $\det A\det(D-CA^{-1}B)$, since the two triangular factors have determinant one. Both sides are polynomials in the entries, and they agree on the open dense set where $A$ is invertible, hence everywhere.

**Corollary.** For a block triangular matrix, $C=0$ or $B=0$, the determinant is $\det A\det D$, and the determinant is multiplicative over the recursion.

**Proof.** The Schur complement reduces to $D$ or to $D-CA^{-1}B$ with one of the two mixed blocks zero.

**Corollary.** $\det X$ is the product of the corner determinant and the determinant of the Schur complement, which is the "effective" complement after eliminating the corner.

**Proof.** The theorem.

**The rank reading.** The rank of $X$ is at least the rank of $A$ plus the rank of the Schur complement, with equality when $A$ has full rank in its block.

**Proof.** The factorisation above exhibits $X$ as the product of three matrices of ranks $\operatorname{rank}A$, $\operatorname{rank}A+\operatorname{rank}(D-CA^{-1}B)$ and $4$, so the rank of $X$ is that of the middle factor.

## The Two Steps

**The step $k=2$.** $M_4=M_2\oplus M_2\oplus M_{2\times2}\oplus M_{2\times2}$ with the dimensions $4+4+4+4$, and the corner and the complement are both copies of $M_2$.

**Proof.** The dimension formula at $k=2$.

**Corollary.** At $k=2$ the two corners are the two factors of the Kronecker decomposition, and the mixed blocks are the off-diagonal parts of the tensor product.

**Proof.** With $E=\operatorname{diag}(1,0)\otimes\mathrm I_2$ the corner is $\operatorname{diag}(1,0)M_2\operatorname{diag}(1,0)\otimes M_2\cong\mathbb{C}\otimes M_2\cong M_2$.

**The step $k=1$.** $M_4=\mathbb{C}\oplus M_3\oplus\mathbb{C}^{3}\oplus(\mathbb{C}^{3})^{\ast}$ with the dimensions $1+9+3+3$, and the corner is the scalars while the complement is $M_3$.

**Proof.** The dimension formula at $k=1$.

**Corollary.** The step $k=1$ exhibits $M_4$ as $M_3$ with one row and one column adjoined, and the corner is the pivot of the elimination.

**Proof.** $B$ is a column, $C$ a row, and $A$ a scalar; the Schur complement is $D-CB/A$ with $A$ the pivot.

**The two steps together.** The recursion at $k=2$ splits the algebra into two halves of equal size, and the recursion at $k=1$ splits off one dimension at a time; the two are independent and neither refines the other.

**Proof.** The idempotents $\operatorname{diag}(1,1,0,0)$ and $\operatorname{diag}(1,0,0,0)$ are not nested in the sense of Peirce refinement, since the second is not in the corner of the first.

## The Peirce Basis and Its Table

**Definition.** The **Peirce basis** at $E=\operatorname{diag}(1,1,0,0)$ is the sixteen matrix units, grouped as $E_{ij}$ with $i,j\in\{1,2\}$ in $V_{11}$, $i\in\{1,2\}$, $j\in\{3,4\}$ in $V_{10}$, $i\in\{3,4\}$, $j\in\{1,2\}$ in $V_{01}$ and $i,j\in\{3,4\}$ in $V_{00}$.

**Proposition.** The product table in the Peirce basis is the matrix-unit table $E_{ij}E_{kl}=\delta_{jk}E_{il}$, and it is block diagonal in the four groups.

**Proof.** The matrix-unit rule, read with the indices grouped.

**Corollary.** The four groups are closed under the product exactly in the pattern $V_{ij}V_{kl}\subseteq\delta_{jk}V_{il}$, and the Peirce basis is the matrix-unit basis read in blocks.

**Proof.** The index condition $\delta_{jk}$ says that the second index of the first factor matches the first index of the second, which is exactly the block adjacency condition.

**The two-number table.** In the four groups the products of $E_{ij}$ with $E_{kl}$ vanish unless $j=k$, and then produce the unit with the outer indices; the number of nonzero products is the number of triples $(i,j,l)$ with the indices in the right groups.

**Proof.** The table, counted.

**Corollary.** The Peirce basis is not the axis-free basis: the sixteen axis-free elements are signed permutations and the Peirce elements are matrix units, and the change between them is a unitary matrix.

**Proof.** The two bases are orthonormal for the Hilbert–Schmidt form up to the scale two, and they differ.

## The Kronecker Reading

**Theorem.** At $k=2$ the recursion is the Kronecker factorisation: $M_4\cong M_2\otimes M_2$, where the first factor is generated by the corner and the complement and the second by the mixed blocks.

**Proof.** With $E=\operatorname{diag}(1,0)\otimes\mathrm I_2$ the corner is $\operatorname{diag}(1,0)M_2\operatorname{diag}(1,0)\otimes M_2$, the complement is $\operatorname{diag}(0,1)M_2\operatorname{diag}(0,1)\otimes M_2$, and the two mixed blocks are the off-diagonal parts of the first factor tensored with $M_2$.

**Corollary.** The two factors of the Kronecker decomposition are the two halves of the recursion, and the Peirce decomposition at $k=2$ is the block decomposition of the tensor product read along the first factor.

**Proof.** The tensor product of block matrices is the block matrix of the tensor products.

**The contrast.** At $k=1$ and at $k=3$ the recursion is not a tensor factorisation: the corner is $\mathbb{C}$ and the complement is $M_3$, and no tensor product of the two has dimension $16$ except the trivial one.

**Proof.** $1\cdot9=9\neq16$.

**Corollary.** The recursion is the general construction and the Kronecker factorisation is the case of the half rank, where the corner and the complement have the same size.

**Proof.** The identity $k^{2}+(4-k)^{2}+2k(4-k)=16$ is the dimension of a tensor product exactly when $k=4-k=2$.

## Summary

The corner of a rank-$k$ idempotent is a copy of $M_k$ with unit $E$, and the algebra is rebuilt from the corner, the complement $M_{4-k}$ and the two rectangular blocks, with $16=k^{2}+(4-k)^{2}+2k(4-k)$. The trace adds over the two corners and the mixed blocks contribute nothing.

The determinant obeys the Schur formula $\det X=\det A\det(D-CA^{-1}B)$, which is an identity of polynomials and reduces to a product for block triangular matrices. The recursion at $k=2$ gives two copies of $M_2$ and two copies of $M_{2\times2}$, and at $k=1$ gives $\mathbb{C}$, $M_3$ and the column and row spaces.

The Peirce basis is the matrix-unit basis read in blocks, with the product table $E_{ij}E_{kl}=\delta_{jk}E_{il}$ and the block adjacency condition. At $k=2$ the recursion is exactly the Kronecker factorisation, and at the other ranks it is not, so the factorisation is the balanced case of a construction that works at every rank.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E$ | idempotent of rank $k$ |
| $EME$ | the corner, a copy of $M_k$ |
| $B,C$ | the two rectangular blocks |
| $D-CA^{-1}B$ | the Schur complement |
| $k^{2}+(4-k)^{2}+2k(4-k)$ | the dimension count, equal to $16$ |
| $M_2\otimes M_2$ | the Kronecker reading at $k=2$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the Schur complement and the block determinant.
- [The Kronecker Factorisation $M_4(\mathbb{C})\cong M_2(\mathbb{C})\otimes M_2(\mathbb{C})$](the-kronecker-factorisation-of-m4c-into-m2c-tensor-m2c.html), for the tensor reading.
- [The Peirce Decomposition and the Two Halves at $n=4$](the-peirce-decomposition-and-the-two-halves-at-n-4.html), for the split of each Peirce space.
- [The Peirce Decomposition and the Corner Recursion of $M_2(\mathbb{C})$](the-peirce-decomposition-and-the-corner-recursion-of-m2c.html), for the recursion at order two.
- [The Ideals, the Centre and the Simplicity of $M_4(\mathbb{C})$](the-ideals-the-centre-and-the-simplicity-of-m4c.html), for the corner of the algebra and its two-sided ideals.
