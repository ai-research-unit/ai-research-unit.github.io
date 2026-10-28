# __The Element, the Coordinates and the Trace of $M_3(\mathbb{C})$__

## Introduction

An element of $M_{3}(\mathbb{C})$ is a $3\times3$ array of complex numbers, a linear map $\mathbb{C}^{3}\to\mathbb{C}^{3}$, and a bilinear form on $\mathbb{C}^{3}$ read through the standard dot product. The three readings carry the same nine complex coordinates and the same product; they differ in which structure is emphasised. This article sets out the coordinates, the split into a scalar and a traceless part, the Jordan decomposition, the real and imaginary parts, and the trace pairing.

The **scalar part** of $A$ is $\tfrac13(\operatorname{tr}A)I$, and the **traceless part** is
$$
A_{0}=A-\tfrac13(\operatorname{tr}A)I.
$$
The two commute, the trace of $A_{0}$ is zero, and the algebra splits as a vector space:
$$
M_{3}(\mathbb{C})=\mathbb{C}I\oplus\mathfrak{sl}_{3}(\mathbb{C}),\qquad 9=1+8,
$$
where $\mathfrak{sl}_{3}(\mathbb{C})$ is the traceless part. The split is the first step of the structure theory; the second step is the Jordan decomposition $A=S+N$ into a semisimple and a nilpotent part.

The article assumes the matrix units and the product of *The Matrix Algebra $M_{3}(\mathbb{C})$*, the Peirce coordinates of *The Peirce Decomposition of $M_{3}(\mathbb{C})$*, and the characteristic cubic of *The Cubic, the Discriminant and the Spectral Strata of $M_3(\mathbb{C})$*. The positive definite Hermitian form $\operatorname{tr}(A^{*}B)$ is *The Involution and the Hermitian Structure of $M_3(\mathbb{C})$*; the trace pairing $\operatorname{tr}(AB)$ of this article is complex bilinear and is not positive definite.

## The Coordinates

**Definition.** In the standard frame, an element is
$$
A=\sum_{i,j=1}^{3}\alpha_{ij}E_{ij}
=\begin{pmatrix}
\alpha_{11}&\alpha_{12}&\alpha_{13}\\
\alpha_{21}&\alpha_{22}&\alpha_{23}\\
\alpha_{31}&\alpha_{32}&\alpha_{33}
\end{pmatrix},
\qquad \alpha_{ij}\in\mathbb{C}.
$$
The nine numbers $\alpha_{ij}$ are the **coordinates** of $A$ in the frame. In a general normalized frame $E_{ij}$ they are the Peirce coordinates of *The Peirce Decomposition of $M_{3}(\mathbb{C})$*; the standard frame is the case $E_{ij}$ the coordinate matrix units.

**The coordinate rule for the product.** The product is
$$
(AB)_{ij}=\sum_{k=1}^{3}\alpha_{ik}\beta_{kj},
$$
which is the matrix product in the coordinates. The unit is $\delta_{ij}$, and the associativity is the associativity of the product of the arrays.

**The trace and the determinant.** The trace is
$$
\operatorname{tr}A=\sum_{i=1}^{3}\alpha_{ii},
$$
and the determinant is
$$
\det A=\sum_{\sigma\in S_{3}}\operatorname{sgn}(\sigma)\prod_{i=1}^{3}\alpha_{i,\sigma(i)}.
$$
Both are polynomial in the nine coordinates; the trace is linear and the determinant is homogeneous of degree three. The characteristic polynomial is
$$
\chi_{A}(\lambda)=\lambda^{3}-t\lambda^{2}+s\lambda-d,
\qquad
t=\operatorname{tr}A,\quad
s=\tfrac12(t^{2}-\operatorname{tr}A^{2}),\quad
d=\det A,
$$
as in *The Cubic, the Discriminant and the Spectral Strata of $M_3(\mathbb{C})$*.

**The coordinates of a linear map.** If $A$ is read as the linear map $v\mapsto Av$ on $\mathbb{C}^{3}$ with the standard basis, the $j$-th column of the array is the image of the $j$-th basis vector:
$$
Ae_{j}=\sum_{i=1}^{3}\alpha_{ij}e_{i}.
$$
The kernel is the set of vectors whose coordinates are killed by the array; the image is the span of the columns; the rank is the dimension of either. The determinant is the volume scaling of the map, and the trace is the trace of the map.

**The coordinates of a bilinear form.** The same array defines the bilinear form
$$
B_{A}(u,v)=u^{\mathsf T}Av=\sum_{i,j=1}^{3}u_{i}\alpha_{ij}v_{j},
$$
which is $\mathbb{C}$-bilinear but not Hermitian. The form is symmetric when $A=A^{\mathsf T}$ and alternating when $A=-A^{\mathsf T}$; every array splits uniquely as
$$
A=\tfrac12(A+A^{\mathsf T})+\tfrac12(A-A^{\mathsf T}),
$$
the symmetric and the skew-symmetric parts. The trace of $B_{A}$ with respect to an orthonormal basis is $\operatorname{tr}A$, and the determinant is the volume form of the form. The Hermitian form is a different object: it uses the conjugate transpose $A^{*}$, not the transpose, and it is treated in *The Involution and the Hermitian Structure of $M_3(\mathbb{C})$*.

**The gauge of the coordinates.** A change of normalized frame $E_{ij}\mapsto(t_{i}/t_{j})E_{ij}$ changes the coordinates by
$$
\alpha_{ij}\longmapsto\frac{t_{j}}{t_{i}}\alpha_{ij},
$$
as in *The Two-Parameter Gauge of $M_3(\mathbb{C})$*. The trace, the determinant and the characteristic polynomial are invariant; the individual off-diagonal coordinates are not. The nine coordinates are a coordinate system on the algebra, not a canonical list of nine numbers attached to $A$.

## The Scalar and Traceless Parts

**Definition.** The **scalar part** of $A$ is
$$
A_{\mathrm{s}}=\tfrac13(\operatorname{tr}A)I,
$$
and the **traceless part** is
$$
A_{0}=A-\tfrac13(\operatorname{tr}A)I.
$$

**Proposition.** The decomposition
$$
A=A_{\mathrm{s}}+A_{0},\qquad \operatorname{tr}A_{0}=0,
$$
is unique, the two parts commute, and it is the direct sum
$$
M_{3}(\mathbb{C})=\mathbb{C}I\oplus\mathfrak{sl}_{3}(\mathbb{C}),\qquad 9=1+8,
$$
where $\mathfrak{sl}_{3}(\mathbb{C})=\{A:\operatorname{tr}A=0\}$.

**Proof.** The trace is linear, so $\operatorname{tr}(A-\tfrac13(\operatorname{tr}A)I)=\operatorname{tr}A-\tfrac13(\operatorname{tr}A)\cdot3=0$. If $A=\lambda I+B$ with $\operatorname{tr}B=0$, taking traces gives $3\lambda=\operatorname{tr}A$, so $\lambda=\tfrac13\operatorname{tr}A$ and $B=A_{0}$; the decomposition is unique. The scalar matrix commutes with every matrix, so the two parts commute.

**The trace pairing on the split.** The trace form
$$
\langle A,B\rangle=\operatorname{tr}(AB)
$$
is symmetric and $\mathbb{C}$-bilinear. The scalar line is orthogonal to the traceless part:
$$
\langle I,B\rangle=\operatorname{tr}B=0\qquad(B\in\mathfrak{sl}_{3}).
$$
The restriction of the trace form to the scalar line is $\langle I,I\rangle=3$, and its restriction to $\mathfrak{sl}_{3}$ is nondegenerate. The two restrictions are nondegenerate, so the split is orthogonal for the trace form.

**The norm squared.** For $A=\lambda I+B$ with $\lambda=\tfrac13\operatorname{tr}A$ and $\operatorname{tr}B=0$,
$$
\operatorname{tr}(A^{2})=3\lambda^{2}+\operatorname{tr}(B^{2})
=\frac{(\operatorname{tr}A)^{2}}{3}+\operatorname{tr}(A_{0}^{2}).
$$
The two terms are the scalar and traceless contributions. The trace form is not positive definite over $\mathbb{C}$: $\operatorname{tr}(E_{12}^{2})=0$ with $E_{12}\neq0$. The positive definite form is the Hermitian form of *The Involution and the Hermitian Structure of $M_3(\mathbb{C})$*, not the complex bilinear trace form.

**Worked example.** For
$$
A=\begin{pmatrix}1&2&3\\4&5&6\\7&8&9\end{pmatrix},
$$
the trace is $15$, so the scalar part is $5I$ and the traceless part is
$$
A_{0}=\begin{pmatrix}-4&2&3\\4&0&6\\7&8&4\end{pmatrix}.
$$
The trace of $A_{0}$ is $-4+0+4=0$. The trace of $A^{2}$ is $261$, and
$$
\operatorname{tr}(A_{0}^{2})=261-\frac{15^{2}}{3}=261-75=186.
$$
The scalar contribution is $75$ and the traceless contribution is $186$; their sum is $261$.

## The Jordan Decomposition

**Theorem (the Jordan decomposition).** Every $A\in M_{3}(\mathbb{C})$ has a unique decomposition
$$
A=S+N,
$$
where $S$ is semisimple (diagonalisable), $N$ is nilpotent, and $SN=NS$. Moreover $S$ and $N$ are polynomials in $A$.

**Proof.** The algebra $\mathbb{C}[A]$ is isomorphic to $\mathbb{C}[x]/(\chi_{A})$, where $\chi_{A}$ is the characteristic polynomial. Write
$$
\chi_{A}(x)=\prod_{i=1}^{r}(x-\lambda_{i})^{m_{i}}
$$
with distinct $\lambda_{i}$ and $m_{i}\geq1$. By the Chinese remainder theorem,
$$
\mathbb{C}[A]\cong\prod_{i=1}^{r}\mathbb{C}[x]/((x-\lambda_{i})^{m_{i}}).
$$
Let $S$ be the image of $x$ under the projection to $\prod_{i}\mathbb{C}[x]/(x-\lambda_{i})\cong\mathbb{C}^{r}$; then $S$ is semisimple, because its minimal polynomial $\prod_{i}(x-\lambda_{i})$ has distinct roots. Let $N=A-S$. In each factor, $N$ is the image of $x-\lambda_{i}$ modulo $(x-\lambda_{i})^{m_{i}}$, which is nilpotent of index at most $m_{i}$; hence $N$ is nilpotent. Both $S$ and $N$ are polynomials in $A$, so they commute. If $A=S'+N'$ is another such decomposition, then $S'$ commutes with $A$ and hence with $S$ and $N$; the semisimple part of $A$ is unique by the uniqueness of the primary decomposition, so $S'=S$ and $N'=N$.

**The Jordan form.** The decomposition is the algebraic form of the Jordan normal form: in a suitable basis, $S$ is diagonal with the eigenvalues on the diagonal, and $N$ is block diagonal with the nilpotent Jordan blocks
$$
J_{m}(\lambda)=\lambda I_{m}+N_{m},\qquad N_{m}=\begin{pmatrix}0&1&&\\&\ddots&\ddots&\\&&\ddots&1\\&&&0\end{pmatrix}.
$$
For $M_{3}$ the possible nilpotent blocks are $0$, $N_{2}$, $N_{3}$, and the direct sums $N_{2}\oplus0$; the possible Jordan forms are the diagonal form, the forms with one block of size two, the form with one block of size three, and the scalar forms. The spectral strata of *The Cubic, the Discriminant and the Spectral Strata of $M_3(\mathbb{C})$* are the sets of matrices with a fixed multiplicity pattern of the eigenvalues; the Jordan decomposition refines each stratum by the sizes of the nilpotent blocks.

**The nilpotent part and the spectrum.** The eigenvalues of $A$ are the diagonal entries of $S$; the nilpotent part $N$ has no eigenvalues other than zero. The characteristic polynomial of $A$ is the characteristic polynomial of $S$, and the minimal polynomial is $\prod_{i}(x-\lambda_{i})^{m_{i}}$ where $m_{i}$ is the size of the largest nilpotent block at $\lambda_{i}$. The element is semisimple exactly when $N=0$, equivalently when the minimal polynomial has distinct roots.

**Worked examples.** For the matrix $A$ of the previous section the eigenvalues are distinct, so $S=A$ and $N=0$. For the nilpotent matrix $E_{12}$, the only eigenvalue is $0$, $S=0$ and $N=E_{12}$, with $N^{2}=0$. For the Jordan block
$$
J_{2}(a)=\begin{pmatrix}a&1\\0&a\end{pmatrix}\oplus(a),
$$
the semisimple part is $aI$ and the nilpotent part is $E_{12}$ on the first two coordinates, of index two.

**The trace of the decomposition.** The trace is unchanged by the nilpotent part, $\operatorname{tr}N=0$, because a nilpotent matrix has only the eigenvalue zero. Hence $\operatorname{tr}A=\operatorname{tr}S$, and the scalar part of $A$ is the scalar part of $S$. The determinant is $\det A=\det S$, because $N$ is nilpotent and $\det(I+S^{-1}N)=1$ when $S$ is invertible; at a singular $S$ the identity follows by continuity or from the characteristic polynomial. The trace and the determinant see the semisimple part only; the nilpotent part is invisible to them.

## The Real and Imaginary Parts

**The real coordinates.** Write each coordinate as
$$
\alpha_{ij}=x_{ij}+iy_{ij},\qquad x_{ij},y_{ij}\in\mathbb{R}.
$$
Then
$$
A=X+iY,\qquad X=(x_{ij}),\quad Y=(y_{ij}),
$$
with $X$ and $Y$ real $3\times3$ matrices. The real vector space $M_{3}(\mathbb{C})$ has dimension $18$, and the map $A\mapsto(X,Y)$ is a real linear isomorphism
$$
M_{3}(\mathbb{C})\cong M_{3}(\mathbb{R})\oplus M_{3}(\mathbb{R}),\qquad 18=9+9.
$$
The multiplication by $i$ is the complex structure $J(X,Y)=(-Y,X)$; it is a real linear map with $J^{2}=-I$.

**The realification.** Reading $A$ as a linear map $\mathbb{C}^{3}\to\mathbb{C}^{3}$ and then as a real map $\mathbb{R}^{6}\to\mathbb{R}^{6}$ gives the block matrix
$$
A_{\mathbb{R}}=\begin{pmatrix}X&-Y\\Y&X\end{pmatrix}.
$$
The trace and the determinant are
$$
\operatorname{tr}A_{\mathbb{R}}=2\operatorname{tr}X=2\operatorname{Re}\operatorname{tr}A,\qquad
\det A_{\mathbb{R}}=|\det A|^{2}.
$$
The first identity is the sum of the traces of the two diagonal blocks; the second is the determinant of the block matrix, which is $\det(X+iY)\det(X-iY)=|\det A|^{2}$.

**The real and imaginary parts are not the Hermitian decomposition.** The decomposition $A=X+iY$ separates the entries into their real and imaginary parts. The Hermitian decomposition separates $A$ into $\tfrac12(A+A^{*})$ and $\tfrac12(A-A^{*})$, which are Hermitian and skew-Hermitian; it is a different real decomposition, of $M_{3}(\mathbb{C})$ into two nine-dimensional real spaces. The two decompositions agree only on the real matrices, where $Y=0$ and $A=A^{*}$ if $A$ is symmetric. The Hermitian one is *The Involution and the Hermitian Structure of $M_3(\mathbb{C})$*.

**The complex structure and the real form.** The real algebra $M_{3}(\mathbb{C})$ is the complexification of the real algebra $M_{3}(\mathbb{R})$: every element is $X+iY$ with $X,Y$ real, and the product is the complex bilinear extension of the real product. The complex conjugation $A\mapsto\bar A$ is the real structure; its fixed points are $M_{3}(\mathbb{R})$, of real dimension $9$. The $*$-unitary real form is different: it is the skew-Hermitian part for the star, of real dimension $9$, and it is not the real matrices.

## The Trace Pairing

**Definition.** The **trace pairing** on $M_{3}(\mathbb{C})$ is
$$
\langle A,B\rangle_{\mathrm{tr}}=\operatorname{tr}(AB).
$$

**Proposition.** The trace pairing is symmetric, $\mathbb{C}$-bilinear and nondegenerate. It is invariant under the Lie bracket:
$$
\langle[A,B],C\rangle_{\mathrm{tr}}+\langle B,[A,C]\rangle_{\mathrm{tr}}=0.
$$

**Proof.** Symmetry is $\operatorname{tr}(AB)=\operatorname{tr}(BA)$. Bilinearity is the linearity of the trace and of the product. For nondegeneracy, if $\operatorname{tr}(AB)=0$ for every $B$, take $B=E_{ij}$; then $\operatorname{tr}(AE_{ij})=a_{ji}=0$ for all $i,j$, so $A=0$. For invariance,
$$
\operatorname{tr}([A,B]C)=\operatorname{tr}(ABC-BAC)=\operatorname{tr}(ABC)-\operatorname{tr}(ACB),
$$
and
$$
\operatorname{tr}(B[A,C])=\operatorname{tr}(BAC-BCA)=\operatorname{tr}(BAC)-\operatorname{tr}(BCA).
$$
The two sums cancel by the cyclic property of the trace, $\operatorname{tr}(ABC)=\operatorname{tr}(BCA)=\operatorname{tr}(CAB)$ and $\operatorname{tr}(ACB)=\operatorname{tr}(CBA)=\operatorname{tr}(BAC)$.

**The Gram matrix.** In the basis $E_{ij}$,
$$
\langle E_{ij},E_{kl}\rangle_{\mathrm{tr}}=\operatorname{tr}(E_{ij}E_{kl})=\delta_{jk}\delta_{il}.
$$
The Gram matrix is the permutation matrix that swaps the two indices; its determinant is $-1$ in the ordered basis $E_{11},E_{12},\ldots,E_{33}$, so the form is nondegenerate. The form is not positive definite over $\mathbb{C}$: $\langle E_{12},E_{12}\rangle=0$.

**The Killing form.** The Killing form of $\mathfrak{gl}_{3}(\mathbb{C})$ is
$$
K(A,B)=6\operatorname{tr}(AB)-2\operatorname{tr}A\operatorname{tr}B,
$$
and on the traceless algebra $\mathfrak{sl}_{3}(\mathbb{C})$ it is $6\operatorname{tr}(AB)$. The trace form and the Killing form differ by the rank-one term $2\operatorname{tr}A\operatorname{tr}B$, which is supported on the scalar line. The trace form is the simpler pairing; the Killing form is the invariant form of the Lie algebra.

**The dual and the transpose.** The trace pairing identifies $M_{3}$ with its dual: the linear functional $B\mapsto\operatorname{tr}(AB)$ is represented by $A$. Under this identification the transpose $A^{\mathsf T}$ represents the functional $B\mapsto\operatorname{tr}(A^{\mathsf T}B)=\sum a_{ij}b_{ij}$, which is the Euclidean pairing of the entries. The Hermitian adjoint $A^{*}$ represents the functional $B\mapsto\operatorname{tr}(A^{*}B)$, which is the positive definite Hermitian pairing of *The Involution and the Hermitian Structure of $M_3(\mathbb{C})$*. The three pairings — trace, Euclidean, Hermitian — are different; only the last is positive definite.

**The element as a bilinear form and the trace pairing.** The element $A$ defines the bilinear form $B_{A}(u,v)=u^{\mathsf T}Av$; the trace pairing pairs two elements, not two vectors. The two are related by the identity
$$
B_{A}(u,v)=\operatorname{tr}(A\,vu^{\mathsf T}),
$$
because $vu^{\mathsf T}$ is the rank-one matrix with entries $v_{i}u_{j}$ and the trace of $A vu^{\mathsf T}$ is $u^{\mathsf T}Av$. So the bilinear form is the trace pairing of $A$ with the rank-one matrix $vu^{\mathsf T}$; the trace pairing is the universal pairing behind the form.

**Worked example.** For the matrix $A$ of the previous sections, $\operatorname{tr}(A^{2})=261$. The scalar part $5I$ contributes $75$ and the traceless part $A_{0}$ contributes $186$. The trace pairing of $A$ with $I$ is $\operatorname{tr}A=15$, which is the scalar component; the trace pairing of $A$ with $A_{0}$ is $\operatorname{tr}(AA_{0})=\operatorname{tr}(A_{0}^{2})=186$, because $A=A_{0}+5I$ and $\operatorname{tr}A_{0}=0$. The trace pairing of $A_{0}$ with itself is $186$, the square of the traceless norm.

## Summary

An element of $M_{3}(\mathbb{C})$ has nine complex coordinates $\alpha_{ij}$, eighteen real coordinates $x_{ij},y_{ij}$, and the product
$$
(AB)_{ij}=\sum_{k=1}^{3}\alpha_{ik}\beta_{kj}.
$$
The trace and the determinant are
$$
\operatorname{tr}A=\sum_{i}\alpha_{ii},\qquad
\det A=\sum_{\sigma\in S_{3}}\operatorname{sgn}(\sigma)\prod_{i}\alpha_{i,\sigma(i)}.
$$

The scalar and traceless parts are
$$
\boxed{\;A=\tfrac13(\operatorname{tr}A)I+A_{0},\qquad \operatorname{tr}A_{0}=0,\qquad
M_{3}(\mathbb{C})=\mathbb{C}I\oplus\mathfrak{sl}_{3}(\mathbb{C}),\quad 9=1+8.\;}
$$
The split is orthogonal for the trace pairing $\operatorname{tr}(AB)$.

The Jordan decomposition is
$$
\boxed{\;A=S+N,\qquad S\text{ semisimple},\quad N\text{ nilpotent},\quad SN=NS,\;}
$$
with $S,N$ polynomials in $A$. The trace and the determinant see $S$ only.

The real and imaginary parts are $A=X+iY$ with $X,Y$ real; the realification is
$$
A_{\mathbb{R}}=\begin{pmatrix}X&-Y\\Y&X\end{pmatrix},\qquad
\operatorname{tr}A_{\mathbb{R}}=2\operatorname{Re}\operatorname{tr}A,\qquad
\det A_{\mathbb{R}}=|\det A|^{2}.
$$

The trace pairing is symmetric, nondegenerate and invariant, with Gram matrix $\delta_{jk}\delta_{il}$; it is not positive definite over $\mathbb{C}$. The positive definite Hermitian form is $\operatorname{tr}(A^{*}B)$.

| Quantity | Value for $M_{3}(\mathbb{C})$ |
|---|---|
| Complex dimension | $9$ |
| Real dimension | $18$ |
| Scalar part dimension | $1$ |
| Traceless part dimension | $8$ |
| Trace pairing | $\operatorname{tr}(AB)$, nondegenerate, indefinite |
| Hermitian form | $\operatorname{tr}(A^{*}B)$, positive definite |
| Jordan parts | semisimple $S$, nilpotent $N$, commuting |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha_{ij}$ | the nine complex coordinates in the standard frame |
| $x_{ij},y_{ij}$ | the real and imaginary parts of $\alpha_{ij}$ |
| $A_{\mathrm{s}}=\tfrac13(\operatorname{tr}A)I$ | the scalar part |
| $A_{0}=A-\tfrac13(\operatorname{tr}A)I$ | the traceless part |
| $\mathfrak{sl}_{3}(\mathbb{C})$ | the traceless matrices, dimension $8$ |
| $S,N$ | the semisimple and nilpotent parts of $A$ |
| $B_{A}(u,v)=u^{\mathsf T}Av$ | the bilinear form of $A$ |
| $\langle A,B\rangle_{\mathrm{tr}}=\operatorname{tr}(AB)$ | the trace pairing |
| $A_{\mathbb{R}}$ | the realification, a $6\times6$ real matrix |

## Further Reading

- [The Matrix Algebra $M_3(\mathbb{C})$](the-matrix-algebra-m3c.html), for the matrix units, the product, the trace and the determinant.
- [The Peirce Decomposition of $M_3(\mathbb{C})$](the-peirce-decomposition-of-m3c.html), for the coordinates in a general frame.
- [The Cubic, the Discriminant and the Spectral Strata of $M_3(\mathbb{C})$](the-cubic-the-discriminant-and-the-spectral-strata-of-m3c.html), for the characteristic polynomial.
- [The Involution and the Hermitian Structure of $M_3(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m3c.html), for the positive definite Hermitian form.
- [The Two-Parameter Gauge of $M_3(\mathbb{C})$](the-two-parameter-gauge-of-m3c.html), for the gauge of the coordinates.
- [Eigenvalues and Diagonalisation](eigenvalues-and-diagonalisation.html), for the Jordan form.
- [The Determinant and Alternating Forms](the-determinant-and-alternating-forms.html), for the determinant as an alternating form.
