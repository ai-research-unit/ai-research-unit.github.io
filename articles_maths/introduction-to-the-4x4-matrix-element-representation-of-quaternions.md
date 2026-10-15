# __Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{R})_L$ of Quaternions__

## Introduction

The left multiplications of the quaternion algebra give, in the basis $e_0,e_1,e_2,e_3$, a four-dimensional real representation by $4\times4$ matrices: the map sends $\tilde q$ to the matrix of $\tilde r\mapsto \tilde q\tilde r$. This article presents the map, its multiplicativity, the trace and the determinant of the image, the images of the scalar and vector subspaces, and the two regular representations, left and right. The element and the basis are those of *Quaternion Algebra*; the left and right multiplications are $L_{\tilde p}$ and $R_{\tilde q}$ of *The Quaternions as a Vector Space over $\mathbb{R}$*; the companion matrix article is *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Quaternions*, above this article in this category.

Here the norm is definite and the set $N(\tilde q)=1$ maps into the group of matrices satisfying $\mathsf{M}_4(\tilde q)^{\mathsf T}\mathsf{M}_4(\tilde q)=I$ of determinant one. The article owns the map, the Cayley matrix, the multiplicativity, the trace, the determinant and the two subspace images; the regular representation as an operator and its bi-module structure are *The Enveloping Operator Algebra of the Quaternion Algebra and the Bi-module Structure*, below this article in this category.

## The Left Regular Representation

**Definition.** The **left regular representation** is the map
$$
\mathsf{M}_4:\mathbb{H}\longrightarrow M_4(\mathbb{R}), \qquad \mathsf{M}_4(\tilde q)=\text{the matrix of }\tilde r\mapsto \tilde q\tilde r
$$
in the basis $(e_0,e_1,e_2,e_3)$. Its $j$-th column, $j=0,1,2,3$, is the coordinate column of $\tilde q e_j$:
$$
\mathsf{M}_4(\tilde q)=\bigl(\ \tilde q e_0\ \big|\ \tilde q e_1\ \big|\ \tilde q e_2\ \big|\ \tilde q e_3\ \bigr),
$$
the columns written as coordinate columns in the basis. This is the **Cayley matrix** of $\tilde q$. For a general $\tilde q=q_0e_0+q_1e_1+q_2e_2+q_3e_3$ it reads
$$
\mathsf{M}_4(\tilde q)=
\begin{pmatrix}
q_0&-q_1&-q_2&-q_3\\
q_1&q_0&-q_3&q_2\\
q_2&q_3&q_0&-q_1\\
q_3&-q_2&q_1&q_0
\end{pmatrix}.
$$
The matrix is the one of the left multiplication $L_{\tilde q}$, and the map $\mathsf{M}_4$ is $\mathbb{R}$-linear and injective, since the first column is $\tilde q$ itself.

## Multiplicativity

**Theorem.** For all $\tilde p,\tilde q$,
$$
\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q)=\mathsf{M}_4(\tilde p\tilde q).
$$
The map $\mathsf{M}_4$ is therefore an injective $\mathbb{R}$-algebra homomorphism, whose image is a four-dimensional subalgebra of $M_4(\mathbb{R})$.

**Proof.** The matrix of a composition is the product of the matrices, and $L_{\tilde p}\circ L_{\tilde q}=L_{\tilde p\tilde q}$ because $\tilde p(\tilde q\tilde r)=(\tilde p\tilde q)\tilde r$; in coordinates, $\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q)$ acts on a column vector as $L_{\tilde p} L_{\tilde q}$, which is $L_{\tilde p\tilde q}$. Injectivity is the first column.

Associativity is thus the single fact behind the multiplicativity, and the representation is a faithful realization of $\mathbb{H}$ inside the real matrices. The right multiplication $R_{\tilde q}$ gives a second representation, treated below; the two commute and together generate the enveloping algebra of *The Enveloping Operator Algebra of the Quaternion Algebra and the Bi-module Structure*, below this article in this category.

## The Trace, the Determinant and the Transpose Identity

**Proposition.** For every $\tilde q$,
$$
\operatorname{Tr}\mathsf{M}_4(\tilde q)=4q_0 , \qquad \det\mathsf{M}_4(\tilde q)=N(\tilde q)^2=\bigl(q_0^2+q_1^2+q_2^2+q_3^2\bigr)^2 .
$$
Moreover
$$
\mathsf{M}_4(\tilde q)^{\mathsf T}=\mathsf{M}_4(\tilde q^{\natural}) , \qquad \mathsf{M}_4(\tilde q)\mathsf{M}_4(\tilde q)^{\mathsf T}=N(\tilde q)\,I_4 ,
$$
so that for $\tilde q\neq0$ the matrix $N(\tilde q)^{-1/2}\mathsf{M}_4(\tilde q)$ satisfies $A^{\mathsf T}A=I_4$.

**Proof.** The trace is the sum of the diagonal entries, $4q_0$ by the displayed matrix. The determinant is computed by expansion and equals $N(\tilde q)^2$; it is the square of the quaternion norm of *The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*, below this article in this category. For the transpose, the transpose of the displayed matrix is obtained by reversing the signs of $q_1,q_2,q_3$ throughout, which is exactly the displayed matrix of $\tilde q^{\natural}$; that is $\mathsf{M}_4(\tilde q)^{\mathsf T}=\mathsf{M}_4(\tilde q^{\natural})$. The second identity follows from $\mathsf{M}_4(\tilde q)\mathsf{M}_4(\tilde q^{\natural})=\mathsf{M}_4(\tilde q\tilde q^{\natural})=\mathsf{M}_4(N(\tilde q)e_0)=N(\tilde q)I_4$.

The determinant is the **square** of the norm, not the norm: this is the doubling the $4\times4$ representation pays for being real, against the single determinant $N(\tilde q)$ of the $2\times2$ representation, and it makes the determinant positive. The transpose identity carries the unit sphere of $\mathbb{H}$ into a group of matrices: $\mathsf{M}_4$ restricted to $N(\tilde q)=1$ is a homomorphism into the group satisfying $\mathsf{M}_4^{\mathsf T}\mathsf{M}_4=I$, of determinant $N(\tilde q)^2=1$.

## The Images of the Two Subspaces

| subspace | image under $\mathsf{M}_4$ | description |
|---|---|---|
| $\mathbb{R}_{\mathbb{H}}$ | $\left\{sI_4:s\in\mathbb{R}\right\}$ | the real scalar matrices, dimension one |
| $\mathrm{Vect}(\mathbb{H})$ | $\left\{A:A^{\mathsf T}=-A,\ \operatorname{Tr}A=0\right\}$ intersected with the image | the skew-symmetric matrices of the image, dimension three |
| $\mathbb{H}$ | the full image | dimension four |

On the scalar line the representation is scalar, $\mathsf{M}_4(s)=sI_4$, with determinant $s^4$ and trace $4s$. On the vector subspace the matrices are skew-symmetric and traceless, and they form the three-dimensional Lie algebra of the image; the square of a pure quaternion being the scalar $-N(\vec q)$, the matrix of $\vec q^2$ is $-|\vec q|^2I_4$. The trace separates the two subspaces exactly as in the $2\times2$ article, and the skew-symmetry is the reading of $\vec q^{\natural}=-\vec q$ through the transpose identity above.

## The Left and the Right Regular Representations

**Definition.** The **right regular representation** is
$$
\mathsf{M}_4^{R}(\tilde q)=\text{the matrix of }\tilde r\mapsto \tilde r\tilde q , \qquad \mathsf{M}_4^{R}(\tilde q)=\bigl(\ e_0\tilde q\ \big|\ e_1\tilde q\ \big|\ e_2\tilde q\ \big|\ e_3\tilde q\ \bigr),
$$
the columns being the coordinate columns of $e_jq$.

**Proposition.** The two representations commute and the right one is anti-multiplicative:
$$
\mathsf{M}_4(\tilde p)\mathsf{M}_4^{R}(\tilde q)=\mathsf{M}_4^{R}(\tilde q)\mathsf{M}_4(\tilde p) , \qquad \mathsf{M}_4^{R}(\tilde p)\mathsf{M}_4^{R}(\tilde q)=\mathsf{M}_4^{R}(\tilde q\tilde p) .
$$
The right representation also satisfies $\mathsf{M}_4^{R}(\tilde q)^{\mathsf T}=\mathsf{M}_4^{R}(\tilde q^{\natural})$ and $\mathsf{M}_4^{R}(\tilde q)\mathsf{M}_4^{R}(\tilde q)^{\mathsf T}=N(\tilde q)I_4$.

**Proof.** The commutativity is associativity: $\tilde p(\tilde r\tilde q)=(\tilde p\tilde r)\tilde q$. The anti-multiplicativity is the order in $R_{\tilde p}\circ R_{\tilde q}=R_{\tilde q\tilde p}$, since $R_{\tilde p}(R_{\tilde q}(\tilde r))=(\tilde r\tilde q)\tilde p=\tilde r(\tilde q\tilde p)$; the transpose identities are as for $\mathsf{M}_4$.

The left representation is a homomorphism and the right one an anti-homomorphism; the pair is exactly the two-sided structure of the algebra, $\mathsf{M}_4(\tilde p)\mathsf{M}_4^{R}(\tilde q)$ being the operator $\tilde r\mapsto \tilde p\tilde r\tilde q$. The operator viewpoint, the enveloping algebra generated by the two families and the bi-module structure are *The Enveloping Operator Algebra of the Quaternion Algebra and the Bi-module Structure* and *The Quaternion Algebra in the 4×4 Matrix Element Representation $M_4(\mathbb{R})_L$*, below this article in this category.

## Summary

The left multiplication $\tilde r\mapsto \tilde q\tilde r$, in the basis $e_0,e_1,e_2,e_3$, is the Cayley matrix $\mathsf{M}_4(\tilde q)$, with first column the coordinates of $\tilde q$. It is multiplicative, $\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q)=\mathsf{M}_4(\tilde p\tilde q)$, by associativity, and injective; its trace is $4q_0$, its determinant is the square of the quaternion norm, and $\mathsf{M}_4(\tilde q)^{\mathsf T}=\mathsf{M}_4(\tilde q^{\natural})$, so the image of the unit sphere is the group of matrices satisfying $\mathsf{M}_4^{\mathsf T}\mathsf{M}_4=I$. The scalar line goes to the real scalar matrices and the vector space to the skew-symmetric traceless matrices of the image. The right multiplication gives the commuting, anti-multiplicative representation $\mathsf{M}_4^{R}(\tilde q)$, and the pair $\mathsf{M}_4,\mathsf{M}_4^{R}$ carries the two-sided action $\tilde r\mapsto \tilde p\tilde r\tilde q$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathsf{M}_4(\tilde q)$ | the left regular representation, the Cayley matrix of $\tilde r\mapsto \tilde q\tilde r$ |
| $\mathsf{M}_4^{R}(\tilde q)$ | the right regular representation of $\tilde r\mapsto \tilde r\tilde q$ |
| $\operatorname{Tr}\mathsf{M}_4(\tilde q)=4q_0$ | the trace is four times the scalar part |
| $\det\mathsf{M}_4(\tilde q)=N(\tilde q)^2$ | the determinant is the square of the quaternion norm |
| $\mathsf{M}_4(\tilde q)^{\mathsf T}=\mathsf{M}_4(\tilde q^{\natural})$ | the transpose is the left multiplication by the conjugate |
| $M_4(\mathbb{R})_L$ | the image of $\mathsf{M}_4$, a four-dimensional subalgebra of $M_4(\mathbb{R})$ |

## Further Reading

- *Quaternion Algebra* (`articles_maths/quaternion-algebra.md`), for the element and the multiplication table.
- *The Quaternions as a Vector Space over $\mathbb{R}$* (`articles_maths/the-quaternioid-as-a-vector-space-over-r.md`), for the left and right multiplications $L_{\tilde p}$ and $R_{\tilde q}$.
- *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Quaternions* (`articles_maths/introduction-to-the-2x2-matrix-element-representation-of-quaternions.md`), for the companion representation, where the determinant is $N(\tilde q)$.
- *The Enveloping Operator Algebra of the Quaternion Algebra and the Bi-module Structure* (`articles_maths/the-enveloping-operator-algebra-of-the-quaternion-algebra-and-the-bi-module-structure.md`), below this article in this category, for the operators and the two-sided structure.
