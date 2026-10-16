# __Reduced Biquaternion Objects and Their Matrix Correspondences__

## Introduction

The reduced biquaternion algebra is the commutative algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$ of basis $1,i,j,ij$, with element $T=A+Bj$ and idempotent coordinates $(q_1,q_2)=(A+B,A-B)$. The regular representation, developed in *Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions*, sends $T$ to the matrix of the left multiplication $L_{T}$ in the basis $1,j$,

$$
\mathsf{M}(T)=\begin{pmatrix}A&B\\ B&A\end{pmatrix},
$$

and the change of basis to the idempotent coordinates diagonalises it. This article is the catalogue: it takes the objects of the algebra — the elements, the four forms and their norms, the idempotents, the zero divisors, the groups, the ideals, the operators — and writes the matrix that corresponds to each, records which classical invariant of a matrix computes which object, and states which correspondences are special to the commutative case.

The first correspondence is the reason the model is simple: in the idempotent basis the algebra acts by diagonal matrices, so the eigenvalues of $\mathsf{M}(T)$ are exactly the idempotent coordinates, the determinant is exactly the reduced norm and the trace is twice the scalar part, and the spectrum of the element is the pair of its idempotent coordinates. The second is the failure of the model to see everything: because the matrices are diagonal, the left and the right multiplications coincide, the minimal left ideals of the model are the coordinate lines rather than the columns, and the two-sided multipliers span only the diagonal endomorphisms, of real dimension four, not the sixteen-dimensional space of all real-linear endomorphisms.

The article owns the dictionary and the list of objects. The model and the map on the basis are *Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions*; the algebra read in the model is *The General Plain Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions*; the representations among themselves are *Reduced Biquaternion Other Algebraic Element Representations*; the multiplication operators are *The Multiplication Operators of the General Plain Algebra of the Reduced Biquaternions*; the forms and the norms are *The Four Products, Their Forms and Their Algebraic Norms*; the ideals and the Peirce decomposition are *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions*; the groups are *The Group of Units of the General Plain Algebra of the Reduced Biquaternions*, *The Unitary Group of the Reduced Biquaternion Algebra* and *Reduced Biquaternion Versors and the Orthogonal Group*. The non-commutative companion, where the same dictionary has a different shape because left and right multiplication differ, is *Biquaternion Objects and Their Matrix Correspondences*.

## The Element and Its Matrix

**Proposition (the matrix of an element).** In the basis $1,j$ the matrix of the left multiplication by $T=A+Bj$ is

$$
\mathsf{M}(T)=\begin{pmatrix}A&B\\ B&A\end{pmatrix},
$$

of trace $2A$ and determinant $A^{2}-B^{2}$; its eigenvalues are $A+B=q_1$ and $A-B=q_2$, with eigenvectors $1+j$ and $1-j$; and the change of basis to $(\Pi_{1},\Pi_{2})$ conjugates it to the diagonal form

$$
\mathsf{M}_{\mathrm{d}}(T)=\begin{pmatrix}q_1&0\\ 0&q_2\end{pmatrix}.
$$

**Proof.** $L_{T}(1)=T=A+Bj$ and $L_{T}(j)=Tj=B+Aj$, giving the two columns; the trace and the determinant are read from the matrix; the eigenvector $1+j$ has $L_{T}(1+j)=A+B+(A+B)j=q_1(1+j)$, and likewise $1-j$; the change of basis is the involution $\left(\begin{smallmatrix}1&1\\ 1&-1\end{smallmatrix}\right)$ up to the factor $\tfrac12$, and it diagonalises the matrix.

**Corollary (the spectrum is the idempotent pair).** The spectrum of the element, that is of the operator $L_{T}$, is the pair $\{q_1,q_2\}$ of its idempotent coordinates; the reduced norm is the determinant, $\langle T\rangle_{\natural}=q_1q_2=\det\mathsf{M}(T)$; the scalar part is half the trace, $A=\tfrac12\operatorname{tr}\mathsf{M}(T)$; and the spectral radius is $\max(|q_1|,|q_2|)$.

**Proof.** The eigenvalues are $q_1$ and $q_2$ by the proposition, the product and the half-sum give the determinant and the trace, and the spectral radius is the largest modulus of an eigenvalue.

**Remark (the two-sided multiplier and its rank).** A two-sided multiplier $T\mapsto P\,T\,Q$ acts in the diagonal model by $\operatorname{diag}(p q\,q_1,\;p'q'\,q_2)$ where $p,p'$ and $q,q'$ are the idempotent coordinates of $P$ and $Q$; the space of two-sided multipliers is therefore the two-dimensional space of diagonal endomorphisms of the algebra, of complex dimension two, a proper subspace of the space of complex-linear endomorphisms, of complex dimension four, while the space of $\mathbb{R}$-linear endomorphisms has real dimension sixteen.

**Proof.** In the idempotent basis the multiplication is diagonal with the two coordinates acting independently, so $P\,T\,Q$ has coordinates $p\,q\,q_1$ and $p'q'\,q_2$; the two complex parameters $p q$ and $p'q'$ are the two diagonal entries of the matrix and the two off-diagonal entries remain zero, which is the statement about the dimensions. In the biquaternion case the analogue spans the sixteen-dimensional space, which is the difference between a commutative and a non-commutative algebra.

## The Objects and Their Matrices

**The dictionary.** The following table records each object of the algebra against its matrix image and against the classical invariant that computes it.

| object | matrix image | invariant |
|---|---|---|
| element $T$ | $\mathsf{M}_{\mathrm{d}}(T)=\operatorname{diag}(q_1,q_2)$ | the diagonal entries |
| scalar part $A$ | $\mathsf{M}_{\mathrm{d}}(T)$ | $\tfrac12\operatorname{tr}$ |
| reduced norm $\langle T\rangle_{\natural}=q_1q_2$ | $\mathsf{M}_{\mathrm{d}}(T)$ | $\det$ |
| topological norm $\langle T\rangle_{\natural*}$ | $\mathsf{M}_{\mathrm{d}}(T)$ | $\tfrac12\lVert\cdot\rVert_{F}^{2}$, the Frobenius norm |
| indefinite norm $\langle T\rangle_{*}=\operatorname{Re}(q_1\bar q_2)$ | $\mathsf{M}_{\mathrm{d}}(T)$ | $\operatorname{Re}$ of the Hermitian pairing of the eigenvalues |
| spectrum | $\mathsf{M}_{\mathrm{d}}(T)$ | the eigenvalue set $\{q_1,q_2\}$ |
| idempotent $\Pi_{1}$ | $\operatorname{diag}(1,0)$ | the first matrix unit |
| idempotent $\Pi_{2}$ | $\operatorname{diag}(0,1)$ | the second matrix unit |
| zero divisor | singular matrix | $\det=0$, rank $\leq1$ |
| unit | invertible diagonal matrix | $\det\neq0$ |
| inverse $T^{-1}$ | $\operatorname{diag}(1/q_1,1/q_2)$ | the inverse |
| versor, $\langle\cdot\rangle_{\natural}=1$ | diagonal matrix of determinant $1$ | $\det=1$ |
| unitary element, $P^{\natural}P^{*}=1$ | diagonal unitary matrix | the singular values all $1$ |
| left multiplication $L_{T}$ | left multiplication by $\mathsf{M}_{\mathrm{d}}(T)$ | $\max(|q_1|,|q_2|)$ |
| right multiplication $R_{T}$ | the same | the same |
| two-sided multiplier $P\,(\cdot)\,Q$ | $\operatorname{diag}(pq,p'q')$ | a complex-linear endomorphism |
| coefficient conjugation $\bar{\cdot}$ | entrywise conjugation of the diagonal | $\mathsf{M}_{\mathrm{d}}(T)\mapsto\overline{\mathsf{M}_{\mathrm{d}}(T)}$ |
| natural sign ${}^{\natural}$ | conjugation by the swap matrix $W$ | $W\mathsf{M}_{\mathrm{d}}(T)W$ |
| star ${}^{*}$ | conjugation by $W$ and entrywise conjugation | $W\overline{\mathsf{M}_{\mathrm{d}}(T)}W$ |
| bilinear form $\langle T,U\rangle_{\natural}$ | the pair of matrices | $\tfrac12\operatorname{tr}\bigl(\mathsf{M}_{\mathrm{d}}(T)\,W\,\mathsf{M}_{\mathrm{d}}(U)\,W\bigr)$ |

**Proposition (the conjugation correspondences).** Under the map $\mathsf{M}$ the coefficient conjugation is the entrywise conjugation, the natural sign is the conjugation by the permutation matrix $W=\left(\begin{smallmatrix}0&1\\ 1&0\end{smallmatrix}\right)$, and the star is their composite; these are the only three of the eight algebra automorphisms that are visible as matrix operations on the diagonal model.

**Proof.** The coefficient conjugation conjugates the two diagonal entries, as the elementary computation $\overline{\operatorname{diag}(q_1,q_2)}=\operatorname{diag}(\bar q_1,\bar q_2)$ gives; the natural sign exchanges them, and the permutation matrix $W$ conjugates a diagonal matrix into the diagonal matrix with exchanged entries; the star is the composite by its definition.

**Remark (the commutativity visible in the table).** The entries for $L_{T}$ and $R_{T}$ are the same row, the reason being that the algebra is commutative and its regular representation is by diagonal matrices. In the biquaternion model the two rows are different, the left and the right multiplications differ, and the difference is the whole non-commutative content of the model.

## The Forms, the Norms and the Determinants

**Proposition (the forms in the model).** In the diagonal model

$$
\langle T\rangle_{\natural*}=\tfrac12\operatorname{tr}\bigl(\mathsf{M}_{\mathrm{d}}(T)^{*}\mathsf{M}_{\mathrm{d}}(T)\bigr)=\tfrac12\lVert\mathsf{M}_{\mathrm{d}}(T)\rVert_{F}^{2},
$$

and $\langle T\rangle_{*}=\operatorname{Re}(q_1\bar q_2)$, the real part of the Hermitian pairing of the two eigenvalues, while the algebraic norm is the determinant.

**Proof.** $\operatorname{tr}(\operatorname{diag}(\bar q_1,\bar q_2)\operatorname{diag}(q_1,q_2))=|q_1|^{2}+|q_2|^{2}$, and $\langle\cdot\rangle_{\natural*}=\tfrac12(|q_1|^{2}+|q_2|^{2})$; the second identity is the computation of $\langle\cdot\rangle_{*}$ in the idempotent coordinates. The algebraic norm is an element of the algebra and is the determinant, the topological norm is a positive real and is half the squared Frobenius norm, and the two are different objects.

**Corollary (the Cauchy–Schwarz defect).** The algebraic norm is multiplicative and the topological norm is not, so the determinant of a product is the product of the determinants while the Frobenius norm of a product need not be the product of the Frobenius norms; the two statements are the matrix form of the warning that the algebraic and the topological norms are distinct.

**Proof.** $\det(\mathsf{M}(T)\mathsf{M}(W))=\det\mathsf{M}(T)\det\mathsf{M}(W)$, which is $\langle TW\rangle_{\natural}=\langle T\rangle_{\natural}\langle W\rangle_{\natural}$; the Frobenius norm is not multiplicative in general.

## The Groups in the Model

**Proposition (the groups).** The group of units is the diagonal subgroup of $GL_{2}(\mathbb{C})$; the norm-one group is its determinant-one part; the unitary group $U(\mathbb{B}_{\mathrm{r}})$ is the group of diagonal unitary matrices, which is a maximal torus of the unitary group $U(2)$; and the versors of the bilinear form are the determinant-one diagonal matrices without the modulus restriction.

**Proof.** Every unit is $\operatorname{diag}(q_1,q_2)$ with $q_1q_2\neq0$, and these form the diagonal subgroup; the conditions $\langle\cdot,\cdot\rangle_{\natural}=1$ and $|q_1|=|q_2|=1$ cut the determinant-one part and the diagonal unitary group; the diagonal unitary matrices are the diagonal matrices inside $U(2)$, which is a maximal torus because it is a maximal abelian subgroup consisting of diagonalisable elements.

## The Ideals, the Idempotents and the Zero Divisors

**Proposition (the ideals and the minimal ideals).** The minimal left ideals of the algebra correspond to the two coordinate lines of the diagonal model; the two-sided ideals are $\{0\}$, the two lines, and the algebra; and the zero divisors are the singular elements, that is the matrices of rank one and the zero matrix.

**Proof.** $\mathbb{B}_{\mathrm{r}}\Pi_{1}=\mathbb{C}\Pi_{1}$ is a minimal left ideal, and in the model it is the span of the first matrix unit; a two-sided ideal is a sum of the two coordinate lines, and the only possible sums are the empty one, the two single lines and the whole algebra; the zero divisors are the elements with a vanishing coordinate, which are exactly the singular diagonal matrices.

**Remark (the difference from the biquaternion model).** In the biquaternion algebra the minimal left ideals are two-dimensional, being the columns of $M_{2}(\mathbb{C})$, and the algebra is simple, so it has no proper two-sided ideal; in the reduced algebra the minimal ideals are one-dimensional, the algebra is semisimple with two simple components, and the two lines are the two summands of the direct product.

## Summary

The matrix model of the reduced biquaternion algebra sends an element $T=A+Bj$ to the two-by-two matrix $\left(\begin{smallmatrix}A&B\\ B&A\end{smallmatrix}\right)$, and the change of basis to the idempotents conjugates it to the diagonal matrix $\operatorname{diag}(q_1,q_2)$. The dictionary is then exact: the eigenvalues are the idempotent coordinates, the determinant is the reduced norm, half the trace is the scalar part, half the squared Frobenius norm is the topological norm, the indefinite norm is the real part of the Hermitian pairing of the eigenvalues, the idempotents are the matrix units, the zero divisors are the singular matrices, the units are the invertible diagonal matrices, the norm-one group is their determinant-one part, the unitary group is the diagonal unitary group, a maximal torus of $U(2)$, and the left and the right multiplications coincide because the model is diagonal. The coefficient conjugation, the natural sign and the star are the entrywise conjugation, the conjugation by the swap matrix and their composite. The two-sided multipliers span exactly the diagonal endomorphisms, of complex dimension two, where in the biquaternion model they span the whole endomorphism algebra, of complex dimension sixteen; the minimal ideals are one-dimensional and the algebra is a direct product of two fields, which are the two lines visible as the two coordinate lines of the diagonal model.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}(T)=\left(\begin{smallmatrix}A&B\\ B&A\end{smallmatrix}\right)$ | the matrix of the left multiplication in the basis $1,j$ |
| $\mathsf{M}_{\mathrm{d}}(T)=\operatorname{diag}(q_1,q_2)$ | its diagonal form in the idempotent basis |
| $q_1=A+B$, $q_2=A-B$ | the eigenvalues, the idempotent coordinates |
| $\det\mathsf{M}_{\mathrm{d}}(T)=q_1q_2=\langle T\rangle_{\natural}$ | the reduced norm |
| $\tfrac12\operatorname{tr}\mathsf{M}_{\mathrm{d}}(T)=A$ | the scalar part |
| $\tfrac12\lVert\mathsf{M}_{\mathrm{d}}(T)\rVert_{F}^{2}=\langle T\rangle_{\natural*}$ | the topological norm |
| $\operatorname{Re}(q_1\bar q_2)=\langle T\rangle_{*}$ | the indefinite norm |
| $W=\left(\begin{smallmatrix}0&1\\ 1&0\end{smallmatrix}\right)$ | the swap matrix, giving the natural sign by conjugation |
| $L_{T}=R_{T}$ | the equality of the left and the right multiplication, the commutativity in the model |

## Further Reading

- *Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-element-representation-of-reduced-biquaternions.md`), for the construction of the model and the map on the basis.
- *The General Plain Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions* (`articles_maths/the-general-plain-algebra-in-the-2x2-matrix-element-representation-of-the-reduced-biquaternions.md`), for the algebra read in the model.
- *Reduced Biquaternion Other Algebraic Element Representations* (`articles_maths/reduced-biquaternion-other-algebraic-element-representations.md`), for the other presentations and their relations.
- *The Multiplication Operators of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/the-multiplication-operators-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the operators $L_{T}$ and $R_{T}$ and their norms.
- *The Four Products, Their Forms and Their Algebraic Norms* (`articles_maths/the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.md`), for the forms, the norms and the Gram matrices.
- *Biquaternion Objects and Their Matrix Correspondences* (`articles_maths/biquaternion-objects-and-their-matrix-correspondences.md`), for the companion in which the left and the right multiplications differ.
