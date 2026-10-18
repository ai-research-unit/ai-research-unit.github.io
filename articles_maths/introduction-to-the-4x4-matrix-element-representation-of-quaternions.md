# __Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{R})_L$ of Quaternions__

## Introduction

The left multiplications of the quaternion algebra give, in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, a four-dimensional real representation by $4\times4$ matrices: the map sends $\tilde q$ to the matrix of $\tilde q_3\mapsto \tilde q\tilde q_3$. This article presents the map, its multiplicativity, the trace and the determinant of the image, the images of the scalar and vector subspaces, and the two regular representations, left and right. The element and the basis are those of *Quaternion Algebra*; the left and right multiplications are $L_{\tilde p}$ and $R_{\tilde q}$ of *Quaternion Algebra*; the companion matrix article is *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Quaternions*, above this article in this category.

Here the norm is definite and the set $\langle\tilde q\rangle_{\natural}=1$ maps into the group of matrices satisfying $\mathsf{M}_4(\tilde q)^{\mathsf T}\mathsf{M}_4(\tilde q)=I$ of determinant one. The article owns the map, the Cayley matrix, the multiplicativity, the trace, the determinant and the two subspace images; the regular representation as an operator and its bi-module structure are *The Enveloping Operator Algebra of the Quaternion Algebra and the Bi-module Structure*, below this article in this category.

## The Left Regular Representation

**Definition.** The **left regular representation** is the map
$$
\mathsf{M}_4:\mathbb{H}\longrightarrow M_4(\mathbb{R}), \qquad \mathsf{M}_4(\tilde q)=\text{the matrix of }\tilde q_3\mapsto \tilde q\tilde q_3
$$
in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$. Its $\mu$-th column, $\mu\in\{t,x,y,z\}$, is the coordinate column of $\tilde q e_\mu$:
$$
\mathsf{M}_4(\tilde q)=\bigl(\ \tilde q e_t\ \big|\ \tilde q \vec e_x\ \big|\ \tilde q \vec e_y\ \big|\ \tilde q \vec e_z\ \bigr),
$$
the columns written as coordinate columns in the basis. This is the **Cayley matrix** of $\tilde q$. For a general $\tilde q=q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ it reads
$$
\mathsf{M}_4(\tilde q)=
\begin{pmatrix}
q_t&-q_x&-q_y&-q_z\\
q_x&q_t&-q_z&q_y\\
q_y&q_z&q_t&-q_x\\
q_z&-q_y&q_x&q_t
\end{pmatrix}.
$$
The matrix is the one of the left multiplication $L_{\tilde q}$, and the map $\mathsf{M}_4$ is $\mathbb{R}$-linear and injective, since the first column is $\tilde q$ itself.

## Multiplicativity

**Theorem.** For all $\tilde q_2,\tilde q_1$,
$$
\mathsf{M}_4(\tilde q_2)\mathsf{M}_4(\tilde q_1)=\mathsf{M}_4(\tilde q_2\tilde q_1).
$$
The map $\mathsf{M}_4$ is therefore an injective $\mathbb{R}$-algebra homomorphism, whose image is a four-dimensional subalgebra of $M_4(\mathbb{R})$.

**Proof.** The matrix of a composition is the product of the matrices, and $L_{\tilde q_2}\circ L_{\tilde q_1}=L_{\tilde q_2\tilde q_1}$ because $\tilde q_2(\tilde q_1\tilde q_3)=(\tilde q_2\tilde q_1)\tilde q_3$; in coordinates, $\mathsf{M}_4(\tilde q_2)\mathsf{M}_4(\tilde q_1)$ acts on a column vector as $L_{\tilde q_2} L_{\tilde q_1}$, which is $L_{\tilde q_2\tilde q_1}$. Injectivity is the first column.

Associativity is thus the single fact behind the multiplicativity, and the representation is a faithful realization of $\mathbb{H}$ inside the real matrices. The right multiplication $R_{\tilde q}$ gives a second representation, treated below; the two commute and together generate the enveloping algebra of *The Enveloping Operator Algebra of the Quaternion Algebra and the Bi-module Structure*, below this article in this category.

## The Trace, the Determinant and the Transpose Identity

**Proposition.** For every $\tilde q$,
$$
\operatorname{Tr}\mathsf{M}_4(\tilde q)=4q_t, \qquad \det\mathsf{M}_4(\tilde q)=\langle\tilde q\rangle_{\natural}^2=\bigl(q_t^2+q_x^2+q_y^2+q_z^2\bigr)^2.
$$
Moreover
$$
\mathsf{M}_4(\tilde q)^{\mathsf T}=\mathsf{M}_4(\tilde q^{\natural}), \qquad \mathsf{M}_4(\tilde q)\mathsf{M}_4(\tilde q)^{\mathsf T}=\langle\tilde q\rangle_{\natural}\,I_4,
$$
so that for $\tilde q\neq0$ the matrix $\langle\tilde q\rangle_{\natural}^{-1/2}\mathsf{M}_4(\tilde q)$ satisfies $A^{\mathsf T}A=I_4$.

**Proof.** The trace is the sum of the diagonal entries, $4q_t$ by the displayed matrix. The determinant is computed by expansion and equals $\langle\tilde q\rangle_{\natural}^2$; it is the square of the quaternion norm of *Norm and Invertibility in the Quaternion Algebra*, below this article in this category. For the transpose, the transpose of the displayed matrix is obtained by reversing the signs of $q_x,q_y,q_z$ throughout, which is exactly the displayed matrix of $\tilde q^{\natural}$; that is $\mathsf{M}_4(\tilde q)^{\mathsf T}=\mathsf{M}_4(\tilde q^{\natural})$. The second identity follows from $\mathsf{M}_4(\tilde q)\mathsf{M}_4(\tilde q^{\natural})=\mathsf{M}_4(\tilde q\tilde q^{\natural})=\mathsf{M}_4(\langle\tilde q\rangle_{\natural}e_t)=\langle\tilde q\rangle_{\natural}I_4$.

The determinant is the **square** of the norm, not the norm: this is the doubling the $4\times4$ representation pays for being real, against the single determinant $\langle\tilde q\rangle_{\natural}$ of the $2\times2$ representation, and it makes the determinant positive. The transpose identity carries the unit sphere of $\mathbb{H}$ into a group of matrices: $\mathsf{M}_4$ restricted to $\langle\tilde q\rangle_{\natural}=1$ is a homomorphism into the group satisfying $\mathsf{M}_4^{\mathsf T}\mathsf{M}_4=I$, of determinant $\langle\tilde q\rangle_{\natural}^2=1$.

## The Images of the Two Subspaces

| subspace | image under $\mathsf{M}_4$ | description |
|---|---|---|
| $\mathbb{R}_{\mathbb{H}}$ | $\left\{sI_4:s\in\mathbb{R}\right\}$ | the real scalar matrices, dimension one |
| $\mathrm{Vect}(\mathbb{H})$ | $\left\{A:A^{\mathsf T}=-A,\ \operatorname{Tr}A=0\right\}$ intersected with the image | the skew-symmetric matrices of the image, dimension three |
| $\mathbb{H}$ | the full image | dimension four |

On the scalar line the representation is scalar, $\mathsf{M}_4(s)=sI_4$, with determinant $s^4$ and trace $4s$. On the vector subspace the matrices are skew-symmetric and traceless, and they form the three-dimensional Lie algebra of the image; the square of a pure quaternion being the scalar $-\langle \vec q\rangle_{\natural}$, the matrix of $\vec q^2$ is $-|\vec q|^2I_4$. The trace separates the two subspaces exactly as in the $2\times2$ article, and the skew-symmetry is the reading of $\vec q^{\natural}=-\vec q$ through the transpose identity above.

## The Left and the Right Regular Representations

**Definition.** The **right regular representation** is
$$
\mathsf{M}_4^{R}(\tilde q)=\text{the matrix of }\tilde q_3\mapsto \tilde q_3\tilde q, \qquad \mathsf{M}_4^{R}(\tilde q)=\bigl(\ e_t\tilde q\ \big|\ \vec e_x\tilde q\ \big|\ \vec e_y\tilde q\ \big|\ \vec e_z\tilde q\ \bigr),
$$
the columns being the coordinate columns of $e_\mu q$.

**Proposition.** The two representations commute and the right one is anti-multiplicative:
$$
\mathsf{M}_4(\tilde q_2)\mathsf{M}_4^{R}(\tilde q_1)=\mathsf{M}_4^{R}(\tilde q_1)\mathsf{M}_4(\tilde q_2), \qquad \mathsf{M}_4^{R}(\tilde q_2)\mathsf{M}_4^{R}(\tilde q_1)=\mathsf{M}_4^{R}(\tilde q_1\tilde q_2).
$$
The right representation also satisfies $\mathsf{M}_4^{R}(\tilde q)^{\mathsf T}=\mathsf{M}_4^{R}(\tilde q^{\natural})$ and $\mathsf{M}_4^{R}(\tilde q)\mathsf{M}_4^{R}(\tilde q)^{\mathsf T}=\langle\tilde q\rangle_{\natural}I_4$.

**Proof.** The commutativity is associativity: $\tilde q_2(\tilde q_3\tilde q_1)=(\tilde q_2\tilde q_3)\tilde q_1$. The anti-multiplicativity is the order in $R_{\tilde q_2}\circ R_{\tilde q_1}=R_{\tilde q_1\tilde q_2}$, since $R_{\tilde q_2}(R_{\tilde q_1}(\tilde q_3))=(\tilde q_3\tilde q_1)\tilde q_2=\tilde q_3(\tilde q_1\tilde q_2)$; the transpose identities are as for $\mathsf{M}_4$.

The left representation is a homomorphism and the right one an anti-homomorphism; the pair is exactly the two-sided structure of the algebra, $\mathsf{M}_4(\tilde q_2)\mathsf{M}_4^{R}(\tilde q_1)$ being the operator $\tilde q_3\mapsto \tilde q_2\tilde q_3\tilde q_1$. The operator viewpoint, the enveloping algebra generated by the two families and the bi-module structure are *The Enveloping Operator Algebra of the Quaternion Algebra and the Bi-module Structure* and *The Quaternion Algebra in the 4×4 Matrix Element Representation $M_4(\mathbb{R})_L$*, below this article in this category.

## Summary

The left multiplication $\tilde q_3\mapsto \tilde q\tilde q_3$, in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, is the Cayley matrix $\mathsf{M}_4(\tilde q)$, with first column the coordinates of $\tilde q$. It is multiplicative, $\mathsf{M}_4(\tilde q_2)\mathsf{M}_4(\tilde q_1)=\mathsf{M}_4(\tilde q_2\tilde q_1)$, by associativity, and injective; its trace is $4q_t$, its determinant is the square of the quaternion norm, and $\mathsf{M}_4(\tilde q)^{\mathsf T}=\mathsf{M}_4(\tilde q^{\natural})$, so the image of the unit sphere is the group of matrices satisfying $\mathsf{M}_4^{\mathsf T}\mathsf{M}_4=I$. The scalar line goes to the real scalar matrices and the vector space to the skew-symmetric traceless matrices of the image. The right multiplication gives the commuting, anti-multiplicative representation $\mathsf{M}_4^{R}(\tilde q)$, and the pair $\mathsf{M}_4,\mathsf{M}_4^{R}$ carries the two-sided action $\tilde q_3\mapsto \tilde q_2\tilde q_3\tilde q_1$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathsf{M}_4(\tilde q)$ | the left regular representation, the Cayley matrix of $\tilde q_3\mapsto \tilde q\tilde q_3$ |
| $\mathsf{M}_4^{R}(\tilde q)$ | the right regular representation of $\tilde q_3\mapsto \tilde q_3\tilde q$ |
| $\operatorname{Tr}\mathsf{M}_4(\tilde q)=4q_t$ | the trace is four times the scalar part |
| $\det\mathsf{M}_4(\tilde q)=\langle\tilde q\rangle_{\natural}^2$ | the determinant is the square of the quaternion norm |
| $\mathsf{M}_4(\tilde q)^{\mathsf T}=\mathsf{M}_4(\tilde q^{\natural})$ | the transpose is the left multiplication by the conjugate |
| $M_4(\mathbb{R})_L$ | the image of $\mathsf{M}_4$, a four-dimensional subalgebra of $M_4(\mathbb{R})$ |

## Further Reading

- *Quaternion Algebra* (`articles_maths/quaternion-algebra.md`), for the element and the multiplication table.
- *Quaternion Algebra* (`articles_maths/quaternion-algebra.md`), for the left and right multiplications $L_{\tilde p}$ and $R_{\tilde q}$.
- *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Quaternions* (`articles_maths/introduction-to-the-2x2-matrix-element-representation-of-quaternions.md`), for the companion representation, where the determinant is $\langle\tilde q\rangle_{\natural}$.
- *The Enveloping Operator Algebra of the Quaternion Algebra and the Bi-module Structure* (`articles_maths/the-enveloping-operator-algebra-of-the-quaternion-algebra-and-the-bi-module-structure.md`), below this article in this category, for the operators and the two-sided structure.
