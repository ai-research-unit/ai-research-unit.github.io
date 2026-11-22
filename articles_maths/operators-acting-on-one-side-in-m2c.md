# __Operators Acting on One Side in $M_2(\mathbb{C})$__

## Introduction

**The question.** Multiplication by a fixed element on the left, and multiplication by a fixed element on the right, are two operators of the algebra. This article asks what the two operators are as arrays, what their kernels and images are, when they are invertible, and how the two families sit inside each other.

**Why it is the same statement.** This is the in-depth matrix reading of [Operators Acting on One Side](operators-acting-on-one-side.html). The display carries the left and right multiplications of $\mathbb{B}$ onto the two families $\{A\otimes\mathrm I_2\}$ and $\{\mathrm I_2\otimes A\}$, or in the Peirce frame onto $\mathrm I_2\otimes A$ and $B^{\mathsf T}\otimes\mathrm I_2$; the kernels, the images, the ranks, the inverse and the two commutants are carried with them. The statements are the same statements and only the writing is new: each operator becomes a $4\times4$ array with half of its entries zero, and each theorem becomes a statement about that array.

**What the article proves.** In this order. The two arrays are Kronecker products with an identity factor, and each is a copy of $M_2(\mathbb{C})$ inside $M_4(\mathbb{C})$. The two laws hold as array products, and the two copies generate the same four-dimensional algebra. The kernel of $L_A$ is the set of matrices whose columns lie in $\ker A$, of dimension $4-2\operatorname{rank}A$; the image is the set of matrices whose columns lie in $\operatorname{im}A$. The rank is twice the rank of $A$, taking the values $4,2,0$ and never $1$ or $3$. The operator is invertible exactly when $\det A\neq0$, with inverse $L_{A^{-1}}$, and $\det L_A=(\det A)^2$. The exchange is the transpose-and-flip, $\sigma(M)=FM^{\mathsf T}F$, which carries $L_A$ to $R_A$; the plain flip carries $L_A$ to $R_{A^{\mathsf T}}$. The commutant of the left copy is the right copy and conversely, the intersection is the scalars, and the sum is seven-dimensional and not a subalgebra.

**What the article does not do.** It does not treat the two-sided operators, which is [Operators Acting on Two Sides in $M_2(\mathbb{C})$](operators-acting-on-two-sides-in-m2c.html); it does not treat the Hermitian pairs, which is [The Hermitian Pair of Operators Acting on One Side in $M_2(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-one-side-in-m2c.html); and it does not classify the structures, which is [Classification of the Structures of the Operators of the Biquaternion Algebra in $M_2(\mathbb{C})$](classification-of-the-structures-of-the-operators-of-the-biquaternion-algebra-in-m2c.html).

**Conventions.** The display is $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$, with trace $2Q_t$ and determinant $N(\tilde Q)=Q_t^2+Q_x^2+Q_y^2+Q_z^2$. The carrier is read in the Peirce frame with coordinate column $(y_{11},y_{21},y_{12},y_{22})^{\mathsf T}$, so that left and right multiplication are the Kronecker products $\mathrm I_2\otimes A$ and $B^{\mathsf T}\otimes\mathrm I_2$. Any $4\times4$ array printed here is the axis-free array and not the Pauli array: the axis-free family is the unique representative, among the $96$ signed-permutation bases, whose sixteen operator arrays are signed permutations, so its entries are the multiplication table read aloud and every identity checked in it is an integer check ([$M_4(\mathbb{C})$ Axis-Free Representation : Operators](m4c-axis-free-representation-operators.html)). The Pauli and gamma arrays are a translation and are refused as primary, because one entry of one of their matrices is diagonal by privilege, which puts a spatial direction into the notation; the privilege is canonical and fixes no invariant.

**Boundaries.** The two families and their identification with $\operatorname{End}(M_2(\mathbb{C}))$ are [$\operatorname{End}(M_2(\mathbb{C}))$ as an Algebra: the Regular Representation](end-m2c-as-an-algebra-the-regular-representation.html). The summary of the two copies is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html). The adjoint pair is [Adjoint Pair of $L$ and $R$ Operators in $M_2(\mathbb{C})$](adjoint-pair-of-l-and-r-operators-in-m2c.html).

**Letters.** The array of an element is $A=\mathsf M_2(\tilde Q)$, its adjoint is $A^{\mathsf T}$ (transpose) and its Hermitian adjoint $A^{\dagger}=\bar A^{\mathsf T}$. The two arrays of the operators are $L_A=\mathrm I_2\otimes A$ and $R_B=B^{\mathsf T}\otimes\mathrm I_2$. The flip of the two tensor factors is $F$, and the exchange is $\sigma(M)=FM^{\mathsf T}F$.

## The Two Maps as Arrays

**The left map.** Left multiplication is

$$
L_A(Y)=AY,
$$

and on the coordinate column it is the array

$$
L_A=\mathrm I_2\otimes A=
\begin{pmatrix}
a_{11}&a_{12}&0&0\\
a_{21}&a_{22}&0&0\\
0&0&a_{11}&a_{12}\\
0&0&a_{21}&a_{22}
\end{pmatrix}.
$$

The array has two identical blocks on the diagonal and zeros in the two off-diagonal blocks: it acts on the row index of $Y$ and leaves the column index alone.

**The right map.** Right multiplication is

$$
R_B(Y)=YB,
$$

and on the coordinate column it is

$$
R_B=B^{\mathsf T}\otimes\mathrm I_2=
\begin{pmatrix}
b_{11}&0&b_{21}&0\\
0&b_{11}&0&b_{21}\\
b_{12}&0&b_{22}&0\\
0&b_{12}&0&b_{22}
\end{pmatrix}.
$$

The array has the entries of $B^{\mathsf T}$ with the identity interleaved: it acts on the column index of $Y$ and leaves the row index alone.

**Why the transpose on the right.** The coordinate column lists $y_{11},y_{21},y_{12},y_{22}$, that is column first and row second. Right multiplication acts on the second index, so its array carries $B^{\mathsf T}$ and not $B$. The transpose is a bookkeeping artefact of the column-major order and not a property of the algebra; in the row-major order the two arrays would be $A\otimes\mathrm I_2$ and $\mathrm I_2\otimes B$.

**The two images.** The left family is the set of all $\mathrm I_2\otimes A$, of complex dimension four; the right family is the set of all $B^{\mathsf T}\otimes\mathrm I_2$, also four-dimensional. Each is a copy of $M_2(\mathbb{C})$ inside $M_4(\mathbb{C})$, and the two copies are the images of the two regular representations.

**A basis of each.** The four arrays

$$
\mathrm I_2\otimes\mathrm I_2,\quad \mathrm I_2\otimes(-i\sigma_1),\quad \mathrm I_2\otimes(-i\sigma_2),\quad \mathrm I_2\otimes(-i\sigma_3)
$$

span the left family, and the four arrays with $(-i\sigma_k)^{\mathsf T}$ in place of $-i\sigma_k$ span the right family. In the axis-free frame these eight arrays are signed permutation matrices, and a basis is read off the multiplication table.

## The Two Laws

**The left law.** For all $A,C$,

$$
L_AL_C=\mathrm I_2\otimes A\cdot\mathrm I_2\otimes C=\mathrm I_2\otimes AC=L_{AC},
$$

by the multiplicativity of the Kronecker product.

**The right law.** For all $B,D$,

$$
R_BR_D=B^{\mathsf T}\otimes\mathrm I_2\cdot D^{\mathsf T}\otimes\mathrm I_2=(DB)^{\mathsf T}\otimes\mathrm I_2=R_{DB},
$$

with the order reversed inside the transpose. The two laws are opposite: the left family is a copy of the algebra and the right family is a copy of the opposite algebra.

**The reading.** The map $A\mapsto L_A$ is an algebra isomorphism of $M_2(\mathbb{C})$ onto the left family, and $B\mapsto R_B$ is an algebra anti-isomorphism onto the right family. Both are injective, because $\mathrm I_2\otimes A=0$ forces $A=0$, and both are surjective onto their images by definition. The two laws were checked on a hundred random pairs with residual below $2\cdot10^{-14}$.

**The unit and the inverse.** $L_{\mathrm I_2}=R_{\mathrm I_2}=\mathrm I_4$, and when $A$ is invertible, $L_AL_{A^{-1}}=\mathrm I_4=R_{A^{-1}}R_A$. Each family is therefore a subgroup of $\mathrm{GL}_4(\mathbb{C})$ isomorphic to $\mathrm{GL}_2(\mathbb{C})$, the second with the opposite multiplication.

**The two laws together.** Since the left and right arrays commute, a product of one from each is determined by the pair and not by the order:

$$
L_AR_B=B^{\mathsf T}\otimes A=R_BL_A .
$$

This is associativity in the array language, and it is the statement that the sixteen arrays $L_{e_\mu}R_{e_\nu}$ are the products of two independent families.

## Kernel and Image

**The kernel of the left map.** For a $2\times2$ matrix $Y$,

$$
L_A(Y)=0\iff AY=0\iff\text{every column of }Y\text{ lies in }\ker A .
$$

The kernel is therefore $\ker A\otimes\mathbb{C}^2$ in the coefficient space, of complex dimension $2\dim\ker A=4-2\operatorname{rank}A$. It is the **right annihilator** $\operatorname{Ann}_r(A)=\{Y:AY=0\}$ of the source.

**The kernel of the right map.** In the same way,

$$
R_B(Y)=0\iff YB=0\iff\text{every row of }Y\text{ lies in the left null space of }B ,
$$

of dimension $2\dim\ker B^{\mathsf T}=4-2\operatorname{rank}B$. It is the **left annihilator** $\operatorname{Ann}_l(B)=\{Y:YB=0\}$.

**The two annihilators differ.** At $A=E_{11}$ the right annihilator $\{Y:AY=0\}$ is the set of matrices with first row zero, and the left annihilator $\{Y:YA=0\}$ the set with first column zero. The matrix unit $E_{21}$ lies in the right annihilator and not in the left. The name records the side on which the argument stands, which is opposite to the side of the multiplication.

**The image of the left map.** The image is

$$
\operatorname{im}L_A=A\,M_2(\mathbb{C})=\{AY\},
$$

the set of matrices whose columns lie in the column space of $A$; it is the right ideal $A\mathbb{B}$ of the source, of dimension $2\operatorname{rank}A$.

**The image of the right map.** The image is

$$
\operatorname{im}R_B=M_2(\mathbb{C})\,B=\{YB\},
$$

the set of matrices whose rows lie in the row space of $B$; it is the left ideal $\mathbb{B}B$, of the same dimension.

**The rank theorem.** The rank of each operator is twice the rank of its matrix:

$$
\operatorname{rank}L_A=\operatorname{rank}R_B=2\operatorname{rank}A\in\{0,2,4\}.
$$

*Proof.* The image of $L_A$ is $\operatorname{im}A\otimes\mathbb{C}^2$, of dimension $2\dim\operatorname{im}A$. The same count on the other side gives the second equality, and $2\operatorname{rank}B$ replaces $2\operatorname{rank}A$ there.

**The three cases.** The rank takes three values:

| the element | $\operatorname{rank}A$ | $\operatorname{rank}L_A$ | dimension of each annihilator |
|---|---|---|---|
| invertible | $2$ | $4$ | $0$ |
| zero divisor, nonzero | $1$ | $2$ | $2$ |
| zero | $0$ | $0$ | $4$ |

The values $1$ and $3$ never occur. This is the first consequence of the tensor structure: a one-sided operator is the identity on one factor, so its rank is a multiple of the dimension of that factor.

**The rank-nullity check.** The two columns add to four in every row of the table, which is rank-nullity for a $4\times4$ array. The statement is not new, and the table is the source's trichotomy read as a rank count.

## Invertibility

**The criterion.** $L_A$ is invertible exactly when $A$ is invertible, and the same for $R_B$.

*Proof.* If $L_A$ is invertible, then $A$ has a right inverse in the algebra, since $AY=\mathrm I_2$ has a solution; a one-sided inverse of a square matrix is two-sided, so $A$ is invertible. Conversely $L_AL_{A^{-1}}=\mathrm I_4$.

**The determinant.** For every $A$,

$$
\det L_A=\det(\mathrm I_2\otimes A)=(\det A)^2=N(\tilde Q)^2,
$$

and the same for $R_A$. The square is structural: the array is the identity on one factor and $A$ on the other, so its determinant is the determinant of $A$ raised to the dimension of the other factor. The operator determinant is the square of the element determinant, and the two vanish together.

**The inverse.** When $A$ is invertible,

$$
(L_A)^{-1}=L_{A^{-1}}=\mathrm I_2\otimes A^{-1},\qquad
(R_B)^{-1}=R_{B^{-1}}.
$$

The inverse stays in the family, so each family is a subgroup and the operator inverse is the algebra inverse read on the operator. In the display $A^{-1}=(\det A)^{-1}\operatorname{adj}A$, and the inverse array is the Kronecker product of the identity with that matrix.

**The eigenvalues.** The eigenvalues of $L_A$ are the eigenvalues of $A$, each twice; the eigenvalues of $R_B$ are the eigenvalues of $B$, each twice. The determinant is the product of the four, that is the square of the product of the two, and the trace is twice the trace of $A$. Neither the eigenvalues nor the determinant see the element's singular values, which is the distinction of [The SVD Decomposition of Endomorphisms of the Biquaternion Algebra in $M_2(\mathbb{C})$](the-svd-decomposition-of-endomorphisms-of-the-biquaternion-algebra-in-m2c.html).

## The Exchange of the Two Sides

**The array.** The exchange is

$$
\sigma(M)=F\,M^{\mathsf T}F,
\qquad
F=\begin{pmatrix}1&0&0&0\\0&0&1&0\\0&1&0&0\\0&0&0&1\end{pmatrix},
$$

the transpose followed by the flip of the two tensor factors. It is an involution and an anti-automorphism of $M_4(\mathbb{C})$, and it carries each family onto the other:

$$
\sigma(L_A)=F(\mathrm I_2\otimes A^{\mathsf T})F=A^{\mathsf T}\otimes\mathrm I_2=R_A,
\qquad
\sigma(R_B)=L_B .
$$

Both identities were checked on a hundred random elements with residual below $10^{-15}$.

**What the exchange is.** It is the composition of the flip, which is the inner automorphism $M\mapsto FMF$, with the transpose, which is not inner. The composition reverses products, so it is not inner either: no array $\mathsf S$ satisfies $\sigma(M)=\mathsf S M\mathsf S^{-1}$ for all $M$. The exchange is an operation on operators and not a change of basis.

**The plain flip.** The flip alone carries $L_A$ to $A\otimes\mathrm I_2=R_{A^{\mathsf T}}$. The two statements differ by the transpose of the parameter, which is exactly the bookkeeping transpose of the right array. The exchange $\sigma$ is the version that keeps the parameter, and it is the one the source calls $S$.

**The exchange and the invariants.** The exchange preserves the rank, the determinant, the trace and the spectrum, because a transpose and an inner conjugation preserve all four. It does not preserve the left family, which is its point, and it maps the seven-dimensional sum onto itself because it swaps the two summands.

**What the exchange is not.** It is not the adjoint: the adjoint of $L_A$ with respect to the Frobenius form is $L_{A^{\dagger}}$, not $R_A$. It is not the inverse: $L_A^{-1}=L_{A^{-1}}$, which is again in the left family. And it is not the conjugation by the element involution $\natural$, which moves the parameter as well as the side, as [The Transposition of the Two Sides in $M_2(\mathbb{C})$](the-transposition-of-the-two-sides-in-m2c.html) explains.

## The Two Families Together

**The commutation.** For all $A,B$,

$$
L_AR_B=(\mathrm I_2\otimes A)(B^{\mathsf T}\otimes\mathrm I_2)=B^{\mathsf T}\otimes A=(B^{\mathsf T}\otimes\mathrm I_2)(\mathrm I_2\otimes A)=R_BL_A .
$$

The arrays of the two families commute, so the order of a mixed product is immaterial and the pair of parameters determines the operator.

**The commutant of the left copy.** An array $T$ commutes with every $\mathrm I_2\otimes A$ exactly when it is of the form $C\otimes\mathrm I_2$:

$$
\{\mathrm I_2\otimes A\}'=\{C\otimes\mathrm I_2\}=R(\mathbb{B}).
$$

*Proof.* The inclusion $\supseteq$ is the commutation. For the converse, the commutant of $\mathrm I_2\otimes M_2(\mathbb{C})$ in $M_2(\mathbb{C})\otimes M_2(\mathbb{C})$ is $M_2(\mathbb{C})\otimes\mathrm I_2$, which is the double-commutant theorem for the simple algebra $M_2(\mathbb{C})$. The direct proof uses the same probe as the source: applying $T(\mathrm I_2\otimes A)=(\mathrm I_2\otimes A)T$ to the identity gives $T(A)=A\,T(\mathrm I_2)$ for every $A$, so $T$ is right multiplication by $C=T(\mathrm I_2)$.

**The commutant of the right copy.** The same statement with the sides exchanged:

$$
\{B^{\mathsf T}\otimes\mathrm I_2\}'=\{A\otimes\mathrm I_2\}=L(\mathbb{B}).
$$

The proofs are one proof with the exchange $\sigma$ applied to it.

**The intersection.** An array that is at once $\mathrm I_2\otimes A$ and $B^{\mathsf T}\otimes\mathrm I_2$ is a scalar:

$$
L(\mathbb{B})\cap R(\mathbb{B})=\mathbb{C}\,\mathrm I_4 .
$$

*Proof.* Evaluating at the unit gives $A=B$. Then $A\otimes\mathrm I_2=\mathrm I_2\otimes A$ forces $A$ to commute with every matrix, so $A=\lambda\mathrm I_2$ and the array is $\lambda\mathrm I_4$. In the algebra language this is the statement that the centre of $M_2(\mathbb{C})$ is the scalars.

**The sum.** The two images are four-dimensional and meet in a line, so

$$
\dim\bigl(L(\mathbb{B})+R(\mathbb{B})\bigr)=4+4-1=7 .
$$

The sum is the set of arrays $B^{\mathsf T}\otimes A$ modulo the relation $(\lambda A,\lambda^{-1}B)$.

**The sum is not a subalgebra.** Both one-sided families lie in the sum, and the product of a left with a right multiplier generally does not. At $A=E_{12}$ and $B=E_{21}$ the two factors have coefficient arrays $e_2e_1^{\mathsf T}$ and $e_1e_3^{\mathsf T}$, both supported in the first column and the first row, but the product $L_{E_{12}}R_{E_{21}}$ has coefficient array $e_2e_3^{\mathsf T}$, supported at the entry $(2,3)$, which is outside both. The sum is closed under addition and not under composition.

**The chain.** The four subspaces sit in the chain

$$
\mathbb{C}\cdot\mathrm I_4\ \subset\ L(\mathbb{B}),\,R(\mathbb{B})\ \subset\ L(\mathbb{B})+R(\mathbb{B})\ \subset\ M_4(\mathbb{C}),
$$

of complex dimensions $1$, $4$ twice, $7$ and $16$, with the two middle terms incomparable.

## A Worked Example at $E_{11}$

**The element.** Take $A=E_{11}$, the idempotent of determinant zero whose rank is one. Every statement above is in its middle case.

**The two arrays.** The left array keeps the first row of $Y$ and kills the second; the right array keeps the first column and kills the second. In the Peirce frame,

$$
L_{E_{11}}=\operatorname{diag}(1,0,1,0),
\qquad
R_{E_{11}}=\operatorname{diag}(1,1,0,0).
$$

Both are diagonal, and their diagonals differ, so the two operators agree on $E_{11}$ and on no other basis element.

**The kernels.** The kernel of $L_{E_{11}}$ is the set of matrices with first row zero, $\operatorname{span}\{e_2,e_4\}$, of dimension two. The kernel of $R_{E_{11}}$ is the set of matrices with first column zero, $\operatorname{span}\{e_3,e_4\}$, also of dimension two.

**The images.** The image of $L_{E_{11}}$ is the set of matrices whose only possible nonzero row is the first, $\operatorname{span}\{e_1,e_3\}$, the right ideal $E_{11}M_2$. The image of $R_{E_{11}}$ is the set spanned by $e_1,e_2$, the left ideal $M_2E_{11}$.

**The rank and the inverse.** Both arrays have rank two and determinant zero, consistent with $\operatorname{rank}=2\operatorname{rank}E_{11}=2$ and $\det A=0$. Neither operator is invertible, and the two kernels are different subspaces of the same dimension.

**The exchange on the example.** Since $\sigma$ fixes $E_{11}$, it satisfies $\sigma L_{E_{11}}\sigma=R_{E_{11}}$, which on the diagonals is the exchange of the second and third entries: $\operatorname{diag}(1,0,1,0)\mapsto\operatorname{diag}(1,1,0,0)$. This is the matrix form of the source's identity on a diagonal matrix.

## Where $n=2$ Differs

**The number of factors.** The carrier is $M_2(\mathbb{C})$, so the operator algebra is $M_2(\mathbb{C})\otimes M_2(\mathbb{C})$ and each one-sided family is four-dimensional. At order $n$ each family is $n^2$-dimensional and the sum is $2n^2-1$.

**The rank.** The possible ranks of a one-sided operator are the multiples of $2$ up to $4$, so $0,2,4$. At order $n$ they are the multiples of $n$ up to $n^2$.

**The determinant.** The determinant of a one-sided array is the $2$-nd power of the element determinant. At order $n$ it is the $n$-th power, because the array is the identity on a factor of dimension $n$.

**The annihilators.** Each annihilator has dimension $2\dim\ker A$, which is the product of the nullity with the dimension of the other factor. At order $n$ it is $n\dim\ker A$, and the two annihilators are different subspaces of that same dimension.

**Nothing else differs.** The two laws, the commutants, the intersection and the exchange are statements about the tensor square, and they hold at every order with the same proofs.

## Summary

Left and right multiplication are the arrays $\mathrm I_2\otimes A$ and $B^{\mathsf T}\otimes\mathrm I_2$, each a copy of $M_2(\mathbb{C})$ inside $M_4(\mathbb{C})$ with half of its entries zero. The two laws hold as array products, with the order reversed in the second family.

The kernel of $L_A$ is the set of matrices whose columns lie in $\ker A$, of dimension $4-2\operatorname{rank}A$, and the image is the set of matrices whose columns lie in $\operatorname{im}A$; the rank of the operator is twice the rank of the element and takes only the values $0,2,4$. The operator is invertible exactly when $\det A\neq0$, and its determinant is $(\det A)^2$.

The exchange $\sigma(M)=FM^{\mathsf T}F$ is the transpose followed by the flip; it is an anti-automorphism, it is not inner, and it carries $L_A$ to $R_A$. The two families commute, each is the commutant of the other, they meet in the scalars and their sum is seven-dimensional and not a subalgebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_A=\mathrm I_2\otimes A$ | left multiplication by $A$ |
| $R_B=B^{\mathsf T}\otimes\mathrm I_2$ | right multiplication by $B$ |
| $\sigma(M)=FM^{\mathsf T}F$ | the exchange of the two sides |
| $F$ | the flip of the two tensor factors |
| $\operatorname{Ann}_r(A)$ | the right annihilator $\{Y:AY=0\}$ |
| $\operatorname{Ann}_l(A)$ | the left annihilator $\{Y:YA=0\}$ |
| $A^{\dagger}=\bar A^{\mathsf T}$ | the Hermitian adjoint |
| $E_{ij}$ | the matrix units of the Peirce frame |
| $L(\mathbb{B})$, $R(\mathbb{B})$ | the two regular images |

## Further Reading

- [Operators Acting on One Side](operators-acting-on-one-side.html), for the source definitions, the two laws and the two commutants.
- [$\operatorname{End}(M_2(\mathbb{C}))$ as an Algebra: the Regular Representation](end-m2c-as-an-algebra-the-regular-representation.html), for the two regular images and their identification with the algebra.
- [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html), for the summary of the two copies and their ranks.
- [The Transposition of the Two Sides in $M_2(\mathbb{C})$](the-transposition-of-the-two-sides-in-m2c.html), for the exchange and its two identities.
- [Operators Acting on Two Sides in $M_2(\mathbb{C})$](operators-acting-on-two-sides-in-m2c.html), for the products of the two families and the cone they span.
- [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html), for the display in which the arrays are written.
