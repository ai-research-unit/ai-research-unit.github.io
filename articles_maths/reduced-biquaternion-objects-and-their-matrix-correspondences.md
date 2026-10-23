# __Reduced Biquaternion Objects and Their Matrix Correspondences__

## Introduction

The reduced biquaternion algebra is the commutative algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$ of basis $1,i,j,ij$, with element $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ and idempotent coordinates $(Q_{+},Q_{-})=(Q_{\blacktriangle}+Q_{\blacktriangledown},Q_{\blacktriangle}-Q_{\blacktriangledown})$. The regular representation, developed in *Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions*, sends $\breve Q$ to the matrix of the left multiplication $L_{\breve Q}$ in the basis $1,j$,

$$
\mathsf{M}(\breve Q)=\begin{pmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix},
$$

and the change of basis to the idempotent coordinates diagonalises it. This article is the catalogue: it takes the objects of the algebra — the elements, the four forms and their norms, the idempotents, the zero divisors, the groups, the ideals, the operators — and writes the matrix that corresponds to each, records which classical invariant of a matrix computes which object, and states which correspondences are special to the commutative case.

The first correspondence is the reason the model is simple: in the idempotent basis the algebra acts by diagonal matrices, so the eigenvalues of $\mathsf{M}(\breve Q)$ are exactly the idempotent coordinates, the determinant is exactly the reduced norm and the trace is twice the scalar part, and the spectrum of the element is the pair of its idempotent coordinates. The second is the failure of the model to see everything: because the matrices are diagonal, the left and the right multiplications coincide, the minimal left ideals of the model are the coordinate lines rather than the columns, and the two-sided multipliers span only the diagonal endomorphisms, of real dimension four, not the sixteen-dimensional space of all real-linear endomorphisms.

The article owns the dictionary and the list of objects. The model and the map on the basis are *Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions*; the algebra read in the model is *The Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions*; the representations among themselves are *Reduced Biquaternion Other Algebraic Element Representations*; the multiplication operators are *The Multiplication Operators of the Algebra of the Reduced Biquaternions*; the forms and the norms are *The Four Products, Their Forms and Their Algebraic Norms*; the ideals and the Peirce decomposition are *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*; the groups are *The Group of Units of the Algebra of the Reduced Biquaternions*, *The Unitary Group of the Reduced Biquaternion Algebra* and *Reduced Biquaternion Versors and the Orthogonal Group*. The non-commutative companion, where the same dictionary has a different shape because left and right multiplication differ, is *Biquaternion Objects and Their Matrix Correspondences*.

## The Element and Its Matrix

**Proposition (the matrix of an element).** In the basis $1,j$ the matrix of the left multiplication by $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ is

$$
\boxed{\;
\mathsf{M}(\breve Q)=\begin{pmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix}
\;},
$$

of trace $2Q_{\blacktriangle}$ and determinant $Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$; its eigenvalues are $Q_{\blacktriangle}+Q_{\blacktriangledown}=Q_{+}$ and $Q_{\blacktriangle}-Q_{\blacktriangledown}=Q_{-}$, with eigenvectors $1+j$ and $1-j$; and the change of basis to $(\Pi_+,\Pi_-)$ conjugates it to the diagonal form

$$
\boxed{\;
\mathsf{M}_{\mathrm{d}}(\breve Q)=\begin{pmatrix}Q_{+}&0\\ 0&Q_{-}\end{pmatrix}
\;}.
$$

**Proof.** $L_{\breve Q}(1)=\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ and $L_{\breve Q}(j)=\breve Q j=Q_{\blacktriangledown}+Q_{\blacktriangle}j$, giving the two columns; the trace and the determinant are read from the matrix; the eigenvector $1+j$ has $L_{\breve Q}(1+j)=Q_{\blacktriangle}+Q_{\blacktriangledown}+(Q_{\blacktriangle}+Q_{\blacktriangledown})j=Q_{+}(1+j)$, and likewise $1-j$; the change of basis is the involution $\left(\begin{smallmatrix}1&1\\ 1&-1\end{smallmatrix}\right)$ up to the factor $\tfrac12$, and it diagonalises the matrix.

**Corollary (the spectrum is the idempotent pair).** The spectrum of the element, that is of the operator $L_{\breve Q}$, is the pair $\{Q_{+},Q_{-}\}$ of its idempotent coordinates; the reduced norm is the determinant, $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{+}Q_{-}=\det\mathsf{M}(\breve Q)$; the scalar part is half the trace, $Q_{\blacktriangle}=\tfrac12\operatorname{tr}\mathsf{M}(\breve Q)$; and the spectral radius is $\max(|Q_{+}|,|Q_{-}|)$.

**Proof.** The eigenvalues are $Q_{+}$ and $Q_{-}$ by the proposition, the product and the half-sum give the determinant and the trace, and the spectral radius is the largest modulus of an eigenvalue.

**Remark (the two-sided multiplier and its rank).** A two-sided multiplier $\breve Q\mapsto P\,\breve Q\,Q$ acts in the diagonal model by $\operatorname{diag}(p q\,Q_{+},\;p'q'\,Q_{-})$ where $p,p'$ and $q,q'$ are the idempotent coordinates of $P$ and $Q$; the space of two-sided multipliers is therefore the two-dimensional space of diagonal endomorphisms of the algebra, of complex dimension two, a proper subspace of the space of complex-linear endomorphisms, of complex dimension four, while the space of $\mathbb{R}$-linear endomorphisms has real dimension sixteen.

**Proof.** In the idempotent basis the multiplication is diagonal with the two coordinates acting independently, so $P\,\breve Q\,Q$ has coordinates $p\,q\,Q_{+}$ and $p'q'\,Q_{-}$; the two complex parameters $p q$ and $p'q'$ are the two diagonal entries of the matrix and the two off-diagonal entries remain zero, which is the statement about the dimensions. In the biquaternion case the analogue spans the sixteen-dimensional space, which is the difference between a commutative and a non-commutative algebra.

## The Objects and Their Matrices

**The dictionary.** The following table records each object of the algebra against its matrix image and against the classical invariant that computes it.

| object | matrix image | invariant |
|---|---|---|
| element $\breve Q$ | $\mathsf{M}_{\mathrm{d}}(\breve Q)=\operatorname{diag}(Q_{+},Q_{-})$ | the diagonal entries |
| scalar part $Q_{\blacktriangle}$ | $\mathsf{M}_{\mathrm{d}}(\breve Q)$ | $\tfrac12\operatorname{tr}$ |
| reduced norm $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{+}Q_{-}$ | $\mathsf{M}_{\mathrm{d}}(\breve Q)$ | $\det$ |
| topological norm $\langle \breve Q\rangle_{\mathrm{ts}*}$ | $\mathsf{M}_{\mathrm{d}}(\breve Q)$ | $\tfrac12\lVert\cdot\rVert_{F}^{2}$, the Frobenius norm |
| indefinite norm $\langle \breve Q\rangle_{*}=\operatorname{Re}(Q_{+}\bar Q_{-})$ | $\mathsf{M}_{\mathrm{d}}(\breve Q)$ | $\operatorname{Re}$ of the Hermitian pairing of the eigenvalues |
| spectrum | $\mathsf{M}_{\mathrm{d}}(\breve Q)$ | the eigenvalue set $\{Q_{+},Q_{-}\}$ |
| idempotent $\Pi_+$ | $\operatorname{diag}(1,0)$ | the first matrix unit |
| idempotent $\Pi_-$ | $\operatorname{diag}(0,1)$ | the second matrix unit |
| zero divisor | singular matrix | $\det=0$, rank $\leq1$ |
| unit | invertible diagonal matrix | $\det\neq0$ |
| inverse $\breve Q^{-1}$ | $\operatorname{diag}(1/Q_{+},1/Q_{-})$ | the inverse |
| versor, $\langle\cdot\rangle_{\mathrm{ts}}=1$ | diagonal matrix of determinant $1$ | $\det=1$ |
| unitary element, $P_{\mathrm{ts}}P^{*}=1$ | diagonal unitary matrix | the singular values all $1$ |
| left multiplication $L_{\breve Q}$ | left multiplication by $\mathsf{M}_{\mathrm{d}}(\breve Q)$ | $\max(\lvert Q_{+}\rvert,\lvert Q_{-}\rvert)$ |
| right multiplication $R_{\breve Q}$ | the same | the same |
| two-sided multiplier $P\,(\cdot)\,Q$ | $\operatorname{diag}(pq,p'q')$ | a complex-linear endomorphism |
| coefficient conjugation $\bar{\cdot}$ | entrywise conjugation of the diagonal | $\mathsf{M}_{\mathrm{d}}(\breve Q)\mapsto\overline{\mathsf{M}_{\mathrm{d}}(\breve Q)}$ |
| tessarine sign ${}_{\mathrm{ts}}$ | conjugation by the swap matrix $W$ | $W\mathsf{M}_{\mathrm{d}}(\breve Q)W$ |
| star ${}^{*}$ | conjugation by $W$ and entrywise conjugation | $W\overline{\mathsf{M}_{\mathrm{d}}(\breve Q)}W$ |
| bilinear form $\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}}$ | the pair of matrices | $\tfrac12\operatorname{tr}\bigl(\mathsf{M}_{\mathrm{d}}(\breve Q_{1})\,W\,\mathsf{M}_{\mathrm{d}}(\breve Q_{2})\,W\bigr)$ |

**Proposition (the conjugation correspondences).** Under the map $\mathsf{M}$ the coefficient conjugation is the entrywise conjugation, the tessarine sign is the conjugation by the permutation matrix $W=\left(\begin{smallmatrix}0&1\\ 1&0\end{smallmatrix}\right)$, and the star is their composite; these are the only three of the eight algebra automorphisms that are visible as matrix operations on the diagonal model.

**Proof.** The coefficient conjugation conjugates the two diagonal entries, as the elementary computation $\overline{\operatorname{diag}(Q_{+},Q_{-})}=\operatorname{diag}(\bar Q_{+},\bar Q_{-})$ gives; the tessarine sign exchanges them, and the permutation matrix $W$ conjugates a diagonal matrix into the diagonal matrix with exchanged entries; the star is the composite by its definition.

**Remark (the commutativity visible in the table).** The entries for $L_{\breve Q}$ and $R_{\breve Q}$ are the same row, the reason being that the algebra is commutative and its regular representation is by diagonal matrices. In the biquaternion model the two rows are different, the left and the right multiplications differ, and the difference is the whole non-commutative content of the model.

## The Forms, the Norms and the Determinants

**Proposition (the forms in the model).** In the diagonal model

$$
\boxed{\;
\langle \breve Q\rangle_{\mathrm{ts}*}=\tfrac12\operatorname{tr}\bigl(\mathsf{M}_{\mathrm{d}}(\breve Q)^{*}\mathsf{M}_{\mathrm{d}}(\breve Q)\bigr)=\tfrac12\lVert\mathsf{M}_{\mathrm{d}}(\breve Q)\rVert_{F}^{2}
\;},
$$

and $\langle \breve Q\rangle_{*}=\operatorname{Re}(Q_{+}\bar Q_{-})$, the real part of the Hermitian pairing of the two eigenvalues, while the algebraic norm is the determinant.

**Proof.** $\operatorname{tr}(\operatorname{diag}(\bar Q_{+},\bar Q_{-})\operatorname{diag}(Q_{+},Q_{-}))=|Q_{+}|^{2}+|Q_{-}|^{2}$, and $\langle\cdot\rangle_{\mathrm{ts}*}=\tfrac12(|Q_{+}|^{2}+|Q_{-}|^{2})$; the second identity is the computation of $\langle\cdot\rangle_{*}$ in the idempotent coordinates. The algebraic norm is an element of the algebra and is the determinant, the topological norm is a positive real and is half the squared Frobenius norm, and the two are different objects.

**Corollary (the Cauchy–Schwarz defect).** The algebraic norm is multiplicative and the topological norm is not, so the determinant of a product is the product of the determinants while the Frobenius norm of a product need not be the product of the Frobenius norms; the two statements are the matrix form of the warning that the algebraic and the topological norms are distinct.

**Proof.** $\det(\mathsf{M}(\breve Q_{1})\mathsf{M}(\breve Q_{2}))=\det\mathsf{M}(\breve Q_{1})\det\mathsf{M}(\breve Q_{2})$, which is $\langle \breve Q_{1}\breve Q_{2}\rangle_{\mathrm{ts}}=\langle \breve Q_{1}\rangle_{\mathrm{ts}}\langle \breve Q_{2}\rangle_{\mathrm{ts}}$; the Frobenius norm is not multiplicative in general.

## The Groups in the Model

**Proposition (the groups).** The group of units is the diagonal subgroup of $GL_{2}(\mathbb{C})$; the norm-one group is its determinant-one part; the unitary group $\mathrm{U}(\mathbb{B}_{\mathrm{r}})$ is the group of diagonal unitary matrices, which is a maximal torus of the unitary group $\mathrm{U}(2)$; and the versors of the bilinear form are the determinant-one diagonal matrices without the modulus restriction.

**Proof.** Every unit is $\operatorname{diag}(Q_{+},Q_{-})$ with $Q_{+}Q_{-}\neq0$, and these form the diagonal subgroup; the conditions $\langle\cdot,\cdot\rangle_{\mathrm{ts}}=1$ and $|Q_{+}|=|Q_{-}|=1$ cut the determinant-one part and the diagonal unitary group; the diagonal unitary matrices are the diagonal matrices inside $\mathrm{U}(2)$, which is a maximal torus because it is a maximal abelian subgroup consisting of diagonalisable elements.

## The Ideals, the Idempotents and the Zero Divisors

**Proposition (the ideals and the minimal ideals).** The minimal left ideals of the algebra correspond to the two coordinate lines of the diagonal model; the two-sided ideals are $\{0\}$, the two lines, and the algebra; and the zero divisors are the singular elements, that is the matrices of rank one and the zero matrix.

**Proof.** $\mathbb{B}_{\mathrm{r}}\Pi_+=\mathbb{C}\Pi_+$ is a minimal left ideal, and in the model it is the span of the first matrix unit; a two-sided ideal is a sum of the two coordinate lines, and the only possible sums are the empty one, the two single lines and the whole algebra; the zero divisors are the elements with a vanishing coordinate, which are exactly the singular diagonal matrices.

**Remark (the difference from the biquaternion model).** In the biquaternion algebra the minimal left ideals are two-dimensional, being the columns of $M_{2}(\mathbb{C})$, and the algebra is simple, so it has no proper two-sided ideal; in the reduced algebra the minimal ideals are one-dimensional, the algebra is semisimple with two simple components, and the two lines are the two summands of the direct product.

## Summary

The matrix model of the reduced biquaternion algebra sends an element $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ to the two-by-two matrix $\left(\begin{smallmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{smallmatrix}\right)$, and the change of basis to the idempotents conjugates it to the diagonal matrix $\operatorname{diag}(Q_{+},Q_{-})$. The dictionary is then exact: the eigenvalues are the idempotent coordinates, the determinant is the reduced norm, half the trace is the scalar part, half the squared Frobenius norm is the topological norm, the indefinite norm is the real part of the Hermitian pairing of the eigenvalues, the idempotents are the matrix units, the zero divisors are the singular matrices, the units are the invertible diagonal matrices, the norm-one group is their determinant-one part, the unitary group is the diagonal unitary group, a maximal torus of $\mathrm{U}(2)$, and the left and the right multiplications coincide because the model is diagonal. The coefficient conjugation, the tessarine sign and the star are the entrywise conjugation, the conjugation by the swap matrix and their composite. The two-sided multipliers span exactly the diagonal endomorphisms, of complex dimension two, where in the biquaternion model they span the whole endomorphism algebra, of complex dimension sixteen; the minimal ideals are one-dimensional and the algebra is a direct product of two fields, which are the two lines visible as the two coordinate lines of the diagonal model.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}(\breve Q)=\left(\begin{smallmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{smallmatrix}\right)$ | the matrix of the left multiplication in the basis $1,j$ |
| $\mathsf{M}_{\mathrm{d}}(\breve Q)=\operatorname{diag}(Q_{+},Q_{-})$ | its diagonal form in the idempotent basis |
| $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$, $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$ | the eigenvalues, the idempotent coordinates |
| $\det\mathsf{M}_{\mathrm{d}}(\breve Q)=Q_{+}Q_{-}=\langle \breve Q\rangle_{\mathrm{ts}}$ | the reduced norm |
| $\tfrac12\operatorname{tr}\mathsf{M}_{\mathrm{d}}(\breve Q)=Q_{\blacktriangle}$ | the scalar part |
| $\tfrac12\lVert\mathsf{M}_{\mathrm{d}}(\breve Q)\rVert_{F}^{2}=\langle \breve Q\rangle_{\mathrm{ts}*}$ | the topological norm |
| $\operatorname{Re}(Q_{+}\bar Q_{-})=\langle \breve Q\rangle_{*}$ | the indefinite norm |
| $W=\left(\begin{smallmatrix}0&1\\ 1&0\end{smallmatrix}\right)$ | the swap matrix, giving the tessarine sign by conjugation |
| $L_{\breve Q}=R_{\breve Q}$ | the equality of the left and the right multiplication, the commutativity in the model |

## Further Reading

- [Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions](introduction-to-the-2x2-matrix-element-representation-of-reduced-biquaternions.html), for the construction of the model and the map on the basis.
- [The Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions](the-general-plain-algebra-in-the-2x2-matrix-element-representation-of-the-reduced-biquaternions.html), for the algebra read in the model.
- [Reduced Biquaternion Other Algebraic Element Representations](reduced-biquaternion-other-algebraic-element-representations.html), for the other presentations and their relations.
- [The Multiplication Operators of the Algebra of the Reduced Biquaternions](the-multiplication-operators-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the operators $L_{\breve Q}$ and $R_{\breve Q}$ and their norms.
- [The Four Products, Their Forms and Their Algebraic Norms](the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.html), for the forms, the norms and the Gram matrices.
- [Biquaternion Objects and Their Matrix Correspondences](biquaternion-objects-and-their-matrix-correspondences.html), for the companion in which the left and the right multiplications differ.
