# __The Einstein Product of Reduced Biquaternion Tensors__

## Introduction

A tensor over the reduced biquaternion algebra is an array $A$ of elements of $\mathbb{B}_{\mathrm{r}}$ indexed by several modes, and a product of two tensors is a rule that sums one set of indices of the first against one set of the second. The **Einstein product** sums the trailing indices of the first tensor against the leading indices of the second, pair by pair, each pair over the same range. It is the Einstein summation convention read as an operation on arrays.

The article defines the product, proves that it is associative and unital, and proves that the **matricisation** carries it to the matrix product. It then reads the units and the zero divisors through that matricisation and proves the one-sided inverse theorem: a square tensor with a right inverse has a left inverse, and the two coincide. The theorem does not rest on a commutative product, which the Einstein product is not; after the reduction to the two complex coordinates it is the statement for matrices over a field, where a right inverse is an inverse.

**The results.** The product of a tensor of order $m+n$ and a tensor of order $n+s$ has order $m+s$; it is bilinear over the algebra, associative, and unital in the square case. The matricisation is a bijection onto the matrices and satisfies $\mathrm{mat}(AB)=\mathrm{mat}(A)\mathrm{mat}(B)$, so the square tensors of order $2m$ form an associative algebra isomorphic to $M_{N}(\mathbb{B}_{\mathrm{r}})$, $N=n_{1}\cdots n_{m}$, which is unital and, for $N\ge2$, not commutative. A square tensor is a unit exactly when its two complex coordinate matrices are nonsingular, and then its inverse is the pair of the two complex inverses; a nonzero square tensor is a zero divisor exactly when one coordinate matrix is singular, and a tensor whose entries are all units may still be a zero divisor.

**Boundaries.** The tensor, its slices, its coefficient tensors and its Frobenius norm are *Reduced Biquaternion Tensors as a Vector Space*, above this article. The t-product of the third-order tensors is *The t-Product of Reduced Biquaternion Tensors*, below this article; it is a different product on a different class. The tensor product $\otimes$ of *Tensor Products of Algebras* is a product of algebras, not the contraction of arrays, and it is not the product of this article. The zero divisors of the element algebra are *Zero Divisors of the Algebra of the Reduced Biquaternions*; those of the t-product algebra are *Zero Divisors of the Reduced Biquaternion Tensor Algebra*, below this article.

**Conventions.** A tensor is a plain capital typed by its exponent, $A\in\mathbb{B}_{\mathrm{r}}^{n_{1}\times\cdots\times n_{m}\times c_{1}\times\cdots\times c_{n}}$ as in the definition of the product, the order carried by the type and never by a script letter; its entries are lower case, $a_{p_{1}\cdots p_{m}l_{1}\cdots l_{n}}$, and the sizes of the modes are $n_{i}$, $c_{j}$ and $d_{k}$. A multi-index $P=(p_{1},\dots,p_{m})$ is written as one capital letter, and $a_{PL}$ abbreviates the entry with the row multi-index $P$ and the column multi-index $L$. The four real coefficient tensors are $A_{0},A_{1},A_{2},A_{3}$, the tensor being $A=A_{0}+A_{1}i+A_{2}j+A_{3}ij$, and the two complex coordinate tensors are
$$
A_{(1)}=A_{0}+A_{2}+i(A_{1}+A_{3}),\qquad A_{(2)}=A_{0}-A_{2}+i(A_{1}-A_{3}),
$$
these are the components written $X^{+}$ and $X^{-}$ in *Least Squares and Total Least Squares over the Reduced Biquaternions*; they satisfy $A=A_{(1)}\Pi_++A_{(2)}\Pi_-$ with $\Pi_+=\tfrac12(1+j)$ and $\Pi_-=\tfrac12(1-j)$. The **Einstein product is written by juxtaposition**, $AB$, as the matrix product is: the source writes it $\ast$, and the corpus keeps the mark $\ast$ for the t-product, so the two products are not confused. The identity tensor is $\mathrm I$.

## The Product

**Definition.** Let $A$ be a tensor of order $m+n$, with modes of sizes $n_{1},\dots,n_{m}$ before the contracted modes of sizes $c_{1},\dots,c_{n}$, and let $B$ be a tensor of order $n+s$, with the same contracted modes first and then modes of sizes $d_{1},\dots,d_{s}$. Their **Einstein product** is the tensor $AB$ of order $m+s$ with entries
$$
(AB)_{p_{1}\cdots p_{m}q_{1}\cdots q_{s}}=\sum_{l_{1},\dots,l_{n}}a_{p_{1}\cdots p_{m}l_{1}\cdots l_{n}}\,b_{l_{1}\cdots l_{n}q_{1}\cdots q_{s}},
$$
or, in the multi-index notation, $(AB)_{PQ}=\sum_{L}a_{PL}b_{LQ}$, where $P$ runs over the free modes of $A$ and $Q$ over the free modes of $B$.

**The order-three case.** For $A\in\mathbb{B}_{\mathrm{r}}^{n_{1}\times n_{2}\times n_{3}}$ and $B\in\mathbb{B}_{\mathrm{r}}^{n_{3}\times n_{4}\times n_{5}}$, the contracted mode having size $n_{3}$ in both, one has $m=s=2$ and $n=1$,
$$
(AB)_{pqrs}=\sum_{l}a_{pql}b_{lrs},
$$
and the product is of order four. The Einstein product consumes the contracted mode and appends the free modes of the second factor, so the product of two third-order tensors is not a third-order tensor.

**Proposition (bilinearity).** For tensors of the shapes of the definition, $(\alpha A)B=\alpha(AB)=A(\alpha B)$ for $\alpha\in\mathbb{B}_{\mathrm{r}}$, and the product is additive in each argument.

*Proof.* Every entry of the product is a finite sum of products of entries, and the scalar multiplies each product; the algebra is commutative and associative, so the three displays coincide entry by entry.

**Proposition (associativity).** For tensors $A,B,C$ whose shapes compose, $(AB)C=A(BC)$.

*Proof.* In the multi-index notation, $((AB)C)_{PQ}=\sum_{L}\bigl(\sum_{L'}a_{PL'}b_{L'L}\bigr)c_{LQ}$ and $(A(BC))_{PQ}=\sum_{L'}a_{PL'}\bigl(\sum_{L}b_{L'L}c_{LQ}\bigr)$; both are the finite sum $\sum_{L,L'}a_{PL'}b_{L'L}c_{LQ}$, by distributivity in the algebra.

**Proposition (the unit).** Let $A$ be square of order $2m$, with the same modes $n_{1},\dots,n_{m}$ on both sides. The tensor $\mathrm I$ of that order with entries $\delta_{p_{1}l_{1}}\cdots\delta_{p_{m}l_{m}}$ satisfies $A\mathrm I=A=\mathrm I A$.

*Proof.* In the multi-index notation $\mathrm I_{LQ}=\delta_{LQ}$, and $\sum_{L}a_{PL}\delta_{LQ}=a_{PQ}$.

**Remark (no commutativity).** The product inherits the non-commutativity of matrix multiplication, not the commutativity of the algebra. In the matrix case $E_{12}E_{21}=E_{11}$ while $E_{21}E_{12}=E_{22}$, and the same two matrix units, read as tensors of order $2m$ of which every other mode has size one, give the same witness.

## The Matricisation

**Definition.** Let $A$ have order $m+n$, with modes of sizes $n_{1},\dots,n_{m}$ and $c_{1},\dots,c_{n}$. Its **matricisation** is the matrix $\mathrm{mat}(A)$ of size $(n_{1}\cdots n_{m})\times(c_{1}\cdots c_{n})$ whose rows are indexed by the multi-indices $P=(p_{1},\dots,p_{m})$ and whose columns are indexed by the multi-indices $L=(l_{1},\dots,l_{n})$,
$$
\mathrm{mat}(A)_{PL}=a_{PL},
$$
the two index sets being read in row-major order when the matrix is written as a rectangular array.

**Lemma (bijection).** The matricisation is a bijection from $\mathbb{B}_{\mathrm{r}}^{n_{1}\times\cdots\times n_{m}\times c_{1}\times\cdots\times c_{n}}$ onto $M_{(n_{1}\cdots n_{m})\times(c_{1}\cdots c_{n})}(\mathbb{B}_{\mathrm{r}})$, and the inverse reads the entries back in the same order.

*Proof.* The row-major reading identifies the row multi-indices with $\{1,\dots,n_{1}\cdots n_{m}\}$ and the column multi-indices with $\{1,\dots,c_{1}\cdots c_{n}\}$, and the entries are unchanged.

**Theorem (multiplicativity).** For $A$ of order $m+n$ and $B$ of order $n+s$ with the shapes of the definition,
$$
\mathrm{mat}(AB)=\mathrm{mat}(A)\mathrm{mat}(B).
$$

*Proof.* The entry of the right-hand side at $(P,Q)$ is $\sum_{L}\mathrm{mat}(A)_{PL}\mathrm{mat}(B)_{LQ}=\sum_{L}a_{PL}b_{LQ}$, which is the entry of $\mathrm{mat}(AB)$ at the same place by the definition of the product.

**Corollary (the algebra of square tensors).** The square tensors of order $2m$, with the same modes on both sides, form a unital associative algebra over $\mathbb{B}_{\mathrm{r}}$, free of rank $N^{2}$ with $N=n_{1}\cdots n_{m}$, and the matricisation is an isomorphism onto $M_{N}(\mathbb{B}_{\mathrm{r}})$. The algebra is not commutative for $N\ge2$, and it is not a division algebra for any $N$, the algebra $\mathbb{B}_{\mathrm{r}}$ itself having zero divisors.

*Proof.* The bijection carries the product to the matrix product and the unit tensor to the identity matrix, so it is an isomorphism; the rank is that of the matrix algebra. The matrix units $E_{12}$ and $E_{21}$ do not commute, and $E_{11}E_{22}=0$, so the algebra is not commutative for $N\ge2$ and not a division algebra for $N\ge2$; for $N=1$ it is $\mathbb{B}_{\mathrm{r}}$, which has the zero divisors $\Pi_+$ and $\Pi_-$.

## Units and Zero Divisors

**Theorem (the unit criterion).** A square tensor $A$ is a unit of the algebra of square tensors if and only if both complex coordinate matrices $\mathrm{mat}(A_{(1)})$ and $\mathrm{mat}(A_{(2)})$ are nonsingular, and then the coordinate matrices of the inverse are their inverses,
$$
\mathrm{mat}\bigl((A^{-1})_{(1)}\bigr)=\mathrm{mat}(A_{(1)})^{-1},\qquad \mathrm{mat}\bigl((A^{-1})_{(2)}\bigr)=\mathrm{mat}(A_{(2)})^{-1}.
$$

*Proof.* A matrix over $\mathbb{B}_{\mathrm{r}}\cong\mathbb{C}\oplus\mathbb{C}$ is invertible exactly when both its components are nonsingular complex matrices, by *Least Squares and Total Least Squares over the Reduced Biquaternions*, §*The Solution as a Zero Divisor*, and the components of the product are the products of the components; the matricisation carries the product to the matrix product.

**Theorem (the one-sided inverse).** If $AB=\mathrm I$ for square tensors of the same order, then $BA=\mathrm I$.

*Proof.* By the multiplicativity of the matricisation, the identity $AB=\mathrm I$ gives $\mathrm{mat}(A_{(i)})\mathrm{mat}(B_{(i)})=\mathrm I$ for $i=1,2$. A square matrix over a field with a right inverse is invertible, and its right inverse is its inverse, so $\mathrm{mat}(B_{(i)})\mathrm{mat}(A_{(i)})=\mathrm I$; the matricisation is injective, so $BA=\mathrm I$.

**Remark (the proof of the source).** The source proves this theorem by interchanging the two factors in the product of the matricised matrices, $f(A)f(B)=f(B)f(A)$, where $f$ is its matricisation. The matrix product is not commutative, so that step does not follow; the conclusion does, because a square matrix with a right inverse is invertible, which is the argument above, and the determinant of the matricised matrix gives the same conclusion over the commutative algebra $\mathbb{B}_{\mathrm{r}}$.

**Proposition (the zero divisors).** A nonzero square tensor is a zero divisor if and only if one of its complex coordinate matrices is singular. In particular a tensor all of whose entries are units can be a zero divisor.

*Proof.* If $\mathrm{mat}(A_{(1)})$ is singular there is a nonzero complex vector $y$ with $\mathrm{mat}(A_{(1)})y=0$; the tensor $B$ whose matricisation has first coordinate the matrix with every column $y$ and second coordinate zero is nonzero, and $AB=0$. Conversely, if $AB=0$ or $BA=0$ with $B\neq0$, then $A_{(i)}B_{(i)}=0$ or $B_{(i)}A_{(i)}=0$ with $B_{(i)}\neq0$ for some $i$, and either relation makes the square matrix $\mathrm{mat}(A_{(i)})$ singular. For the last clause take $A$ the $2\times2$ tensor with every entry $1$ and $B=\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}$; every entry of $A$ is a unit and $AB=0$.

## The Einstein Product Against the t-Product

The t-product of *The t-Product of Reduced Biquaternion Tensors* is defined on the third-order tensors, multiplies the frontal slices through the block circulant and returns a third-order tensor; the Einstein product of two third-order tensors is of order four and is defined by the contraction alone. The two agree at order two, where both are the matrix product, and they are different operations above it. The transform-based algorithms of the t-product, the slice-wise decomposition and the tubal rank, are not available here; the computations of this article are those of the matrix product read through the matricisation.

## Verification

The identities were checked by recomputation on random tensors of order four with modes of size two, over random complex entries in both idempotent coordinates, the deviations found at the level of the floating-point noise.

- The associativity $(AB)C=A(BC)$ and the unit $A\mathrm I=\mathrm I A=A$, on independent random factors.
- The multiplicativity of the matricisation, $\mathrm{mat}(AB)=\mathrm{mat}(A)\mathrm{mat}(B)$.
- The unit criterion, on random nonsingular pairs of complex coordinate matrices: the coordinate inverses multiply to the identity on either side.
- The zero-divisor example: the all-ones $2\times2$ tensor annihilates $\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}$, although every entry of the first is a unit.

## Summary

The **Einstein product** of an order-$m+n$ tensor and an order-$n+s$ tensor is the order-$m+s$ tensor of the display, the contraction of the trailing indices of the first against the leading indices of the second, written by juxtaposition and never with the mark of the t-product. It is bilinear over the algebra, associative, and unital in the square case; it is not commutative, even though the coefficient algebra is. The **matricisation** reads the two multi-indices in row-major order and is a bijection onto the matrices, and it is multiplicative, $\mathrm{mat}(AB)=\mathrm{mat}(A)\mathrm{mat}(B)$; consequently the square tensors of order $2m$ form the algebra $M_{N}(\mathbb{B}_{\mathrm{r}})$, $N=n_{1}\cdots n_{m}$, free of rank $N^{2}$, unital, associative, not commutative for $N\ge2$ and not a division algebra. A square tensor is a unit exactly when both complex coordinate matrices are nonsingular, and the inverse is the pair of the two complex inverses; a nonzero square tensor is a zero divisor exactly when one coordinate matrix is singular. The one-sided inverse theorem holds, $AB=\mathrm I$ implying $BA=\mathrm I$, by the reduction to the two complex coordinates and the finite-dimensional statement over a field. The Einstein product of two third-order tensors is of order four, while the t-product of two third-order tensors is of order three; the two products agree on the matrices and differ above them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | a tensor, a plain capital typed by its exponent |
| $a_{PL}$ | the entry at the row multi-index $P$ and the column multi-index $L$ |
| $AB$ | the Einstein product, the contraction of the trailing indices |
| $\mathrm I$ | the unit tensor of the square case, $\mathrm I_{LQ}=\delta_{LQ}$ |
| $\mathrm{mat}(A)$ | the matricisation, the array read as a matrix in row-major order |
| $A_{0},A_{1},A_{2},A_{3}$ | the four real coefficient tensors |
| $A_{(1)},A_{(2)}$ | the two complex coordinate tensors, $A=A_{(1)}\Pi_++A_{(2)}\Pi_-$ |
| $\Pi_+,\Pi_-$ | the idempotents $\tfrac12(1\pm j)$ |
| $N=n_{1}\cdots n_{m}$ | the side of the matrix algebra of the square case |

## Further Reading

- *Reduced Biquaternion Tensors as a Vector Space*, above this article, for the tensor, the slices, the coefficient tensors and the Frobenius norm.
- *Least Squares and Total Least Squares over the Reduced Biquaternions* (`articles_maths/least-squares-and-total-least-squares-over-the-reduced-biquaternions.md`), for the componentwise invertibility of a matrix over the algebra.
- *The t-Product of Reduced Biquaternion Tensors*, below this article, for the other product on the third-order tensors.
- Ting-Ting Liu and Shao-Wen Yu, "Some Properties of Reduced Biquaternion Tensors", *Symmetry* 16 (2024), 1260, for the real and complex representations, the one-sided inverse theorem, the eigenvalues and the Gershgorin theorem of the source.
- Tamara G. Kolda and Brett W. Bader, "Tensor Decompositions and Applications", *SIAM Review* 51 (2009), 455–500, for the matricisation, the n-mode products and the tensor decompositions of the real case.
- Y. C. Wang and Y. M. Wei, "Generalized eigenvalue for even order tensors via Einstein product and its applications in multilinear control systems", *Computational and Applied Mathematics* 41 (2022), 419, for the Einstein product eigenvalue problem of the real case.
