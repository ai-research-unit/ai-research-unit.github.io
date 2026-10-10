# __The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ and its four-vector coordinates are those of *Biquaternions as a Vector Space over $\mathbb{C}$* and *The Four-Vector Element Representation of Biquaternions*.

Two $4\times4$ matrices carry the multiplication of $\mathbb{B}$ in the basis $e_0, e_1, e_2, e_3$. The **left regular matrix** $\mathsf{M}_4^{L}(\tilde Q)$ is the matrix whose $m$-th column is the coordinate column of the product $\tilde Q e_m$; the **right regular matrix** $\mathsf{M}_4^{R}(\tilde Q)$ is the matrix whose $m$-th column is the coordinate column of the product $e_m \tilde Q$. Both are complex $4\times4$ matrices, both carry a letter, and neither is the default: the companion article *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* writes $\mathsf{M}_4$ for $\mathsf{M}_4^{L}$, and the letter $L$ is restored here so that the two stand on the same footing.

The **left regular matrix** $\mathsf{M}_4^{L}(\tilde Q)$ in the basis $e_0,e_1,e_2,e_3$, its multiplicativity and injectivity, the trace $\operatorname{Tr}\mathsf{M}_4^{L}(\tilde Q)=4Q_0$ and the determinant $\det\mathsf{M}_4^{L}(\tilde Q)=N(\tilde Q)^2$, and the remarkable subspaces in the regular model are *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*; they are used here and not restated.

The image of the left regular matrix is written $M_4(\mathbb{C})_L$: it is the subspace of $M_4(\mathbb{C})$ of the matrices $\mathsf{M}_4^{L}(\tilde Q)$, of complex dimension $4$ inside the $16$ of $M_4(\mathbb{C})$, and it is the object of this article.

This article is the further development of that representation. It owns the right regular matrix and the relation between the two matrices, the module structure and the decomposition $\mathbb{B}=I_1\oplus I_2\cong V\oplus V$, the double centralizer, the $8\times8$ real form, the sandwich read in the regular basis, and a second $4\times4$ realization with the sixteen products of the biparavectors. It is the first reducible realization met in this subcategory. It does not treat the eigenvalues, the Cayley–Hamilton identity or the eigenspace dimensions of the regular matrix, which belong to *Biquaternion Spectral Theory*; and it does not treat the idempotents and the Peirce decomposition, which belong to *Idempotents of the General Plain Algebra* and *Biquaternion Ideals and Peirce Decomposition*, except to cite the idempotents that split the algebra into its two minimal left ideals. No physical vocabulary is used: the two-sided action of the group of elements of $N=1$ on the Hermitian subspace is a statement of algebra, not a spinor, a chirality or a handedness of a physical particle.

One comparative item is added beyond the representation itself: a second $4 \times 4$ realization of $\mathbb{B}$ taken from the literature on eigenvector bundles, recorded with the multiplicative quadratic map it carries, because it is the natural contrast with both the regular realization and the congruence-shaped quadratic map of *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*.

## The Left and the Right Regular Matrices

**Definition (the left regular matrix).** The **left regular matrix** is the isomorphism written $\mathsf{M}_4^{L}$. It converts a biquaternion into a $4 \times 4$ complex matrix,

$$
\mathsf{M}_4^{L} : \mathbb{B} \longrightarrow M_4(\mathbb{C}),
$$

and it is fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity. In the basis $e_0, e_1, e_2, e_3$, the $m$-th column of $\mathsf{M}_4^{L}(\tilde Q)$ is the coordinate column of $\tilde Q e_m$:

$$
\mathsf{M}_4^{L}(\tilde{Q}) = \begin{pmatrix}
Q_0 & -Q_1 & -Q_2 & -Q_3 \\
Q_1 & Q_0 & -Q_3 & Q_2 \\
Q_2 & Q_3 & Q_0 & -Q_1 \\
Q_3 & -Q_2 & Q_1 & Q_0
\end{pmatrix}.
$$

This is the Cayley matrix of *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*, written $\mathsf{M}_4(\tilde Q)$ there; every entry is a single coefficient of $\tilde Q$ with a sign, and no entry is a sum of two or more coefficients.

**Proposition (the left regular matrix is multiplicative).** For all $\tilde{P}, \tilde{Q} \in \mathbb{B}$,

$$
\mathsf{M}_4^{L}(\tilde{P})\,\mathsf{M}_4^{L}(\tilde{Q}) = \mathsf{M}_4^{L}(\tilde{P}\tilde{Q}), \qquad \mathsf{M}_4^{L}(\tilde{Q}) = 0 \iff \tilde{Q} = 0,
$$

so the assignment is an injective algebra homomorphism, of complex dimension $4$; its trace is $4Q_0$ and its determinant is $N(\tilde{Q})^2$. The proof and the remarkable subspace conditions are those of the companion article and are not repeated.

**Definition (the right regular matrix).** The **right regular matrix** is the assignment written $\mathsf{M}_4^{R}$. It converts a biquaternion into a $4 \times 4$ complex matrix,

$$
\mathsf{M}_4^{R} : \mathbb{B} \longrightarrow M_4(\mathbb{C}),
$$

also fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity. In the same basis, the $m$-th column of $\mathsf{M}_4^{R}(\tilde Q)$ is the coordinate column of $e_m \tilde Q$:

$$
\mathsf{M}_4^{R}(\tilde{Q}) = \begin{pmatrix}
Q_0 & -Q_1 & -Q_2 & -Q_3 \\
Q_1 & Q_0 & Q_3 & -Q_2 \\
Q_2 & -Q_3 & Q_0 & Q_1 \\
Q_3 & Q_2 & -Q_1 & Q_0
\end{pmatrix}.
$$

**Proposition (the right regular matrix).** The columns are the images $e_m \tilde{Q}$, and one expands as in the left case of *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* with the factors in the opposite order. Alternatively, since each $e_m$ is either $e_0$ or one of the $e_k$, and $e_k e_j = -e_j e_k$ for $j \neq k$, the matrix is the transpose of the left matrix conjugated by the fixed sign matrix of the next section, $\mathsf{M}_4^{R}(\tilde{Q}) = D\,\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf T}D$, and direct computation of the four general products confirms the display.

**Theorem (the right regular matrix is anti-multiplicative).** For all $\tilde{Q}, \tilde{R} \in \mathbb{B}$,

$$
\mathsf{M}_4^{R}(\tilde{Q})\,\mathsf{M}_4^{R}(\tilde{R}) = \mathsf{M}_4^{R}(\tilde{R}\tilde{Q}).
$$

Hence the right regular matrix is an algebra **anti**-homomorphism, and its image is the regular representation of the opposite algebra $\mathbb{B}^{\mathrm{op}}$, not a second representation of $\mathbb{B}$.

**Proof.** Write $\operatorname{col}(\tilde S)$ for the coordinate column of $\tilde S$. The defining property of the right matrix is $\mathsf{M}_4^{R}(\tilde{Q})\operatorname{col}(\tilde S) = \operatorname{col}(\tilde S\tilde{Q})$, because the $m$-th column of $\mathsf{M}_4^{R}(\tilde{Q})$ is $\operatorname{col}(e_m\tilde{Q})$ and a column is a linear combination of the $e_m$. Hence, for each $m$,

$$
\mathsf{M}_4^{R}(\tilde{Q})\,\mathsf{M}_4^{R}(\tilde{R})\operatorname{col}(e_m) = \mathsf{M}_4^{R}(\tilde{Q})\operatorname{col}(e_m\tilde{R}) = \operatorname{col}\bigl((e_m\tilde{R})\tilde{Q}\bigr) = \operatorname{col}\bigl(e_m(\tilde{R}\tilde{Q})\bigr) = \mathsf{M}_4^{R}(\tilde{R}\tilde{Q})\operatorname{col}(e_m),
$$

the third step being associativity. The two matrices therefore agree on the four columns $\operatorname{col}(e_m)$, which are the standard basis of $\mathbb{C}^4$, so they are equal. An anti-homomorphism is by definition a homomorphism from the opposite algebra, and the underlying linear assignment is the same.

**Remark (which side is which).** The two matrices are the two ways a non-commutative algebra multiplies its own basis. The left matrix is multiplicative and the right matrix anti-multiplicative. Since quaternion conjugation is an anti-automorphism, the matrix $\mathsf{M}_4^{L}(\tilde{Q}^{\natural})$ depends anti-multiplicatively on $\tilde Q$; it is therefore the right regular matrix up to a fixed change of basis, and the next section identifies that change of basis and shows that it is not the identity. The two matrices differ as soon as the algebra is non-commutative.

## Transposition and the Two Matrices

**Proposition (transposition is quaternion conjugation).** For every biquaternion $\tilde{Q}$,

$$
\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}} = \mathsf{M}_4^{L}(\tilde{Q}^{\natural}),
$$

where the transpose is taken in the basis $e_0, e_1, e_2, e_3$ of the corpus.

**Proof.** Transposing the displayed closed form of $\mathsf{M}_4^{L}(\tilde{Q})$ gives

$$
\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}} = \begin{pmatrix}
Q_0 & Q_1 & Q_2 & Q_3 \\
-Q_1 & Q_0 & Q_3 & -Q_2 \\
-Q_2 & -Q_3 & Q_0 & Q_1 \\
-Q_3 & Q_2 & -Q_1 & Q_0
\end{pmatrix},
$$

and replacing $Q_k$ by $-Q_k$ in that same closed form reproduces this matrix.

**Remark (the false identity).** The right regular matrix is **not** the transpose of the left one:

$$
\mathsf{M}_4^{R}(\tilde{Q}) \neq \mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}} \quad \text{in general}.
$$

For $\tilde{Q} = e_1$ the left matrix is $\mathsf{M}_4^{L}(e_1) = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$, whose transpose is $\begin{pmatrix} 0 & 1 & 0 & 0 \\ -1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & -1 & 0 \end{pmatrix}$, while the right matrix is $\mathsf{M}_4^{R}(e_1) = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & -1 & 0 \end{pmatrix}$: the two differ in the sign of the upper-left block. The proposition above gives the reason: the transpose is the left regular matrix of the quaternion conjugate, $\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}} = \mathsf{M}_4^{L}(\tilde{Q}^{\natural})$, so it is a left regular matrix and equals a right regular matrix only on the centre. The variant that replaces $\tilde{Q}$ by $\tilde{Q}^{\natural}$ is not a second identity, since $\tilde{Q} \mapsto \tilde{Q}^{\natural}$ is a bijection of the algebra.

**Theorem (the correct relation).** Let $D = \operatorname{diag}(-1, 1, 1, 1)$, so that $D^2 = I$. Then for every biquaternion $\tilde{Q}$,

$$
\mathsf{M}_4^{R}(\tilde{Q}) = D\,\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}}\,D = D\,\mathsf{M}_4^{L}(\tilde{Q}^{\natural})\,D .
$$

Hence the right regular matrix is the contragredient of the left one up to the fixed change of basis $D$.

**Proof.** Apply $D$ on the left and on the right to the transpose of the closed form of $\mathsf{M}_4^{L}(\tilde{Q})$. Left multiplication by $D$ negates the first row, and right multiplication by $D$ negates the first column; the corner entry lies in both and is negated twice, hence unchanged. The resulting matrix is the closed form of $\mathsf{M}_4^{R}(\tilde{Q})$ displayed above. The second equality uses the transpose proposition.

**Corollary (the difference vanishes exactly on the centre).** The difference $\mathsf{M}_4^{L}(\tilde{Q}) - \mathsf{M}_4^{R}(\tilde{Q})$ is the zero matrix if and only if $\tilde{Q} \in \mathbb{C}_{\mathbb{B}} = \mathbb{C} e_0$.

**Proof.** If $\tilde{Q} = \lambda e_0$ then $\mathsf{M}_4^{L}(\tilde{Q}) = \mathsf{M}_4^{R}(\tilde{Q}) = \lambda I$, since scalar multiplication is central. Conversely, if the two matrices agree then $\tilde{Q}\tilde{R} = \tilde{R}\tilde{Q}$ for every $\tilde{R}$, so $\tilde{Q}$ lies in the centre, which is the scalar subspace. Comparing the two closed forms directly, the entries in the three last rows and columns agree only when $Q_1 = Q_2 = Q_3 = 0$.

**Remark (what left and right mean).** The two matrices differ **because the algebra is non-commutative**. The $m$-th column of the difference $\mathsf{M}_4^{L}(\tilde{Q}) - \mathsf{M}_4^{R}(\tilde{Q})$ is the coordinate column of $\tilde{Q}e_m - e_m\tilde{Q}$, the commutator $[\tilde{Q}, e_m]$; the difference vanishes on $\mathbb{C}_{\mathbb{B}}$ and nowhere else. This is the sense in which the left and right regular matrices of $\mathbb{B}$ are distinct, and the sense in which the row of *The Four-Vector Element Representation of Biquaternions* carries the right action and not a further left one.

## The Module Structure and Reducibility

The regular representation is the first reducible realization in this subcategory, and its reduction is the decomposition of the algebra into two minimal left ideals.

**Definition.** Let

$$
\tilde\Pi_1 = \tfrac{1}{2}(e_0 + i e_3), \qquad \tilde\Pi_2 = \tfrac{1}{2}(e_0 - i e_3).
$$

**Lemma (orthogonal idempotents).** The elements $\tilde\Pi_1$ and $\tilde\Pi_2$ satisfy

$$
\tilde\Pi_1^2 = \tilde\Pi_1, \qquad \tilde\Pi_2^2 = \tilde\Pi_2, \qquad \tilde\Pi_1\tilde\Pi_2 = \tilde\Pi_2\tilde\Pi_1 = 0, \qquad \tilde\Pi_1 + \tilde\Pi_2 = e_0,
$$

so that $\mathbb{B} = \mathbb{B}\tilde\Pi_1 \oplus \mathbb{B}\tilde\Pi_2$ as a direct sum of left ideals.

**Proof.** Because $i$ is central, $e_3^2 = -e_0$ and $i^2 = -1$, one computes $\tilde\Pi_1^2 = \tfrac{1}{4}(e_0^2 + 2ie_3 + i^2 e_3^2) = \tfrac{1}{4}(e_0 + 2ie_3 + e_0) = \tfrac{1}{2}(e_0 + ie_3) = \tilde\Pi_1$, and similarly $\tilde\Pi_2^2 = \tilde\Pi_2$, while $\tilde\Pi_1\tilde\Pi_2 = \tfrac{1}{4}(e_0^2 - i^2e_3^2) = \tfrac{1}{4}(e_0 - e_0) = 0$. The sum is $e_0$, and the two ideals meet only in $0$: an element lying in both satisfies $\tilde{Q} = \tilde{Q}\tilde\Pi_2 = 0$, because membership of $\mathbb{B}\tilde\Pi_2$ gives $\tilde{Q}\tilde\Pi_2 = \tilde{Q}$ while $\tilde\Pi_1\tilde\Pi_2 = 0$. The sum is therefore direct. The idempotents and the Peirce decomposition are the subject of *Biquaternion Ideals and Peirce Decomposition*; the statement is used here only to split the module.

**Theorem (the left regular matrix is $V \oplus V$).** In the basis

$$
\tilde\Pi_1, \quad e_1 \tilde\Pi_1, \quad \tilde\Pi_2, \quad e_1 \tilde\Pi_2
$$

of $\mathbb{B}$, the left regular matrix of $\tilde{Q}$ is

$$
\mathsf{M}_4^{L}(\tilde{Q}) \sim \begin{pmatrix}
Q_0 - iQ_3 & -Q_1 + iQ_2 & 0 & 0 \\
Q_1 + iQ_2 & Q_0 + iQ_3 & 0 & 0 \\
0 & 0 & Q_0 + iQ_3 & -Q_1 - iQ_2 \\
0 & 0 & Q_1 - iQ_2 & Q_0 - iQ_3
\end{pmatrix},
$$

with the four corner entries zero: the subspaces spanned by $\tilde\Pi_1, e_1\tilde\Pi_1$ and by $\tilde\Pi_2, e_1\tilde\Pi_2$ are invariant under $\mathsf{M}_4^{L}(\tilde{Q})$, and on each of them the action is that of a minimal left ideal, hence a copy of the simple module $V$, so that the left regular representation is

$$
\mathbb{B} \cong V \oplus V
$$

as a left $\mathbb{B}$-module. The regular representation is therefore reducible, and it is the first reducible realization in this subcategory.

**Proof.** The two ideals $\mathbb{B}\tilde\Pi_1$ and $\mathbb{B}\tilde\Pi_2$ are stable under left multiplication by $\tilde Q$, because $\tilde{Q}(\tilde{S}\tilde\Pi_1) = (\tilde{Q}\tilde{S})\tilde\Pi_1$ for every $\tilde{S}$; hence the matrix is block diagonal in any basis adapted to the decomposition. The ideal $\mathbb{B}\tilde\Pi_1$ has the basis $\tilde\Pi_1, e_1\tilde\Pi_1$, since $e_2 \tilde\Pi_1 = i e_1 \tilde\Pi_1$ and $e_3 \tilde\Pi_1 = -i\tilde\Pi_1$. Its multiplication by the basis elements is read from

$$
e_1 \tilde\Pi_1 = e_1\tilde\Pi_1, \quad e_2 \tilde\Pi_1 = ie_1\tilde\Pi_1, \quad e_3 \tilde\Pi_1 = -i\tilde\Pi_1, \qquad e_1(e_1\tilde\Pi_1) = -\tilde\Pi_1, \quad e_2(e_1\tilde\Pi_1) = i\tilde\Pi_1, \quad e_3(e_1\tilde\Pi_1) = ie_1\tilde\Pi_1,
$$

so in the basis $\tilde\Pi_1, e_1\tilde\Pi_1$ the sum $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ acts by the first two rows and columns of the displayed matrix, and the same computation on the basis $\tilde\Pi_2, e_1\tilde\Pi_2$ of $\mathbb{B}\tilde\Pi_2$ gives the last two. The trace of the matrix is $4Q_0$ by inspection and the determinant is the product of its two diagonal groups,

$$
(Q_0 - iQ_3)(Q_0 + iQ_3) - (-Q_1 + iQ_2)(Q_1 + iQ_2) = N(\tilde{Q}),
$$

each of the two diagonal groups contributing the same factor, so that the determinant of the regular matrix is $N(\tilde{Q})^2$.

**Remark (the characteristic polynomial).** In the adapted basis of the theorem above the regular matrix is diagonal in the two invariant subspaces, so its characteristic polynomial is the square of that of the simple module,

$$
\chi_{\mathsf{M}_4^{L}(\tilde{Q})}(\lambda) = \bigl( \lambda^2 - 2Q_0\lambda + N(\tilde{Q}) \bigr)^2,
$$

which the form of the theorem above gives at once. The eigenvalues themselves, the Cayley–Hamilton identity, the eigenspace dimensions and the doubling of the multiplicities that the square produces are the subject of *Biquaternion Spectral Theory*, later in this chapter, and are cited from there rather than developed here.

**Remark (the irreducible submodules are the minimal left ideals).** The two invariant subspaces are the two minimal left ideals $I_1 = \mathbb{B}\tilde\Pi_1$ and $I_2 = \mathbb{B}\tilde\Pi_2$ of the algebra. Both afford the module $V$, and the fact that $V$ is the only simple module is the classification of the simple modules. The decomposition $\mathbb{B} = I_1 \oplus I_2$ is therefore the same fact as the diagonal form of the regular matrix, read as ideals rather than as a matrix; the same decomposition is stated in *Modules over the General Plain Algebra of Biquaternions*, where the simple module is written $S$, as $\mathbb{B} \cong S \oplus S$.

## The Double Centralizer

**Theorem (the centralizer is the right copy).** The centralizer of the image $\mathsf{M}_4^{L}(\mathbb{B})$ in $M_4(\mathbb{C})$,

$$
\bigl\{ C \in M_4(\mathbb{C}) \;:\; C\,\mathsf{M}_4^{L}(\tilde{R}) = \mathsf{M}_4^{L}(\tilde{R})\,C \ \text{ for every } \tilde{R} \in \mathbb{B} \bigr\},
$$

is the image $\mathsf{M}_4^{R}(\mathbb{B})$, of complex dimension $4$.

**Proof.** Write $\operatorname{col}(\tilde S)$ for the coordinate column of $\tilde S$. The defining property of the left matrix is $\mathsf{M}_4^{L}(\tilde{R})\operatorname{col}(\tilde S) = \operatorname{col}(\tilde{R}\tilde{S})$, and in particular $\mathsf{M}_4^{L}(\tilde{R})\operatorname{col}(e_0) = \operatorname{col}(\tilde{R})$. Let $C$ be in the centralizer and let $\mathbf{u} = C\operatorname{col}(e_0)$ be its first column; write $\tilde{Q}$ for the element of that coordinate column. Then, for every $\tilde{R}$,

$$
C\operatorname{col}(\tilde{R}) = C\,\mathsf{M}_4^{L}(\tilde{R})\operatorname{col}(e_0) = \mathsf{M}_4^{L}(\tilde{R})\,C\operatorname{col}(e_0) = \mathsf{M}_4^{L}(\tilde{R})\operatorname{col}(\tilde{Q}) = \operatorname{col}(\tilde{R}\tilde{Q}) = \mathsf{M}_4^{R}(\tilde{Q})\operatorname{col}(\tilde{R}),
$$

the last step being the defining property of the right matrix. The four columns $\operatorname{col}(\tilde{R})$ span $\mathbb{C}^4$, so $C = \mathsf{M}_4^{R}(\tilde{Q})$ and the centralizer is contained in $\mathsf{M}_4^{R}(\mathbb{B})$. Conversely every $\mathsf{M}_4^{R}(\tilde{Q})$ commutes with every $\mathsf{M}_4^{L}(\tilde{R})$, because $(\tilde{R}\tilde{S})\tilde{Q} = \tilde{R}(\tilde{S}\tilde{Q})$ is associativity; hence the centralizer is exactly $\mathsf{M}_4^{R}(\mathbb{B})$. It has complex dimension $4$ because $\mathsf{M}_4^{R}$ is injective: $\mathsf{M}_4^{R}(\tilde{Q}) = 0$ forces its first column, which is the coordinate column of $\tilde Q$, to vanish.

**Remark.** The theorem is the regular-module case of the double centralizer phenomenon, and it is the mirror of the identification of $\mathbb{B}$ with the matrix algebra of the simple module in *Modules over the General Plain Algebra of Biquaternions*: the algebra is recovered as the centralizer of the opposite copy. The two images $\mathsf{M}_4^{L}(\mathbb{B})$ and $\mathsf{M}_4^{R}(\mathbb{B})$ commute, and the products of one matrix from each already span the full matrix algebra $M_4(\mathbb{C})$, as the section on the sixteen products shows.

## The Real Form

**Proposition (the real regular matrix).** Regarded over $\mathbb{R}$ in the real basis

$$
e_0, e_1, e_2, e_3, i e_0, i e_1, i e_2, i e_3,
$$

of the eight-dimensional real space underlying $\mathbb{B}$, the left regular matrix becomes an $8 \times 8$ real matrix $\mathsf{M}_4^{L,\mathbb{R}}(\tilde{Q})$, with

$$
\det \mathsf{M}_4^{L,\mathbb{R}}(\tilde{Q}) = |N(\tilde{Q})|^4, \qquad \operatorname{Tr}\mathsf{M}_4^{L,\mathbb{R}}(\tilde{Q}) = 8 \operatorname{Re}(Q_0).
$$

**Proof.** The real matrix is the realification of the complex matrix $\mathsf{M}_4^{L}(\tilde{Q})$, each complex entry being replaced by its real $2\times2$ block. A complex-linear map with eigenvalues $\lambda_1, \ldots, \lambda_4$ has realification with eigenvalues $\lambda_1, \bar\lambda_1, \ldots, \lambda_4, \bar\lambda_4$, so its determinant is $|\lambda_1 \cdots \lambda_4|^2 = |\det \mathsf{M}_4^{L}(\tilde{Q})|^2 = |N(\tilde{Q})^2|^2 = |N(\tilde{Q})|^4$, and its trace is $2\operatorname{Re}(\lambda_1 + \cdots + \lambda_4) = 2\operatorname{Re}(4Q_0) = 8\operatorname{Re}(Q_0)$.

**Remark (why the dimension doubles).** The real dimension doubles because $\mathbb{B}$ is a complex vector space and is regarded as a real vector space by restriction of scalars: the correspondence $\operatorname{Res}_{\mathbb{C}/\mathbb{R}} \mathbb{C}^4 = \mathbb{R}^8$ replaces each complex coordinate by its real and imaginary parts. The same doubling applies to the module $V$, whose realification $S$ has real dimension $4$, so over $\mathbb{R}$ the left regular matrix is $\mathsf{M}_4^{L,\mathbb{R}} \cong \operatorname{Res}_{\mathbb{C}/\mathbb{R}}(V \oplus V)$, and the decomposition of the complex case survives with each part doubled in size. Restricted to the real subalgebra $\mathbb{H}_{\mathbb{B}}$, and read on $\mathbb{H}_{\mathbb{B}}$ itself, the same construction is the $4 \times 4$ real regular matrix of the quaternions, which is the subject of *Quaternion Element Representations*; complexifying the algebra doubles both its real dimension and the size of the regular matrix.

## The Sandwich in the Regular Basis

The Hermitian sandwich $\tilde R \mapsto \tilde Q\tilde R\tilde Q^{*}$ of *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions* is read here as a single matrix.

**The sandwich matrix.** Put

$$
\mathsf{H}_{\tilde Q} := \mathsf{M}_4^{L}(\tilde{Q})\,\mathsf{M}_4^{R}(\tilde{Q}^{*}) .
$$

It is the matrix that carries the coordinate column of $\tilde{R}$ to the coordinate column of $\tilde{Q}\tilde{R}\tilde{Q}^{*}$: indeed $\mathsf{M}_4^{R}(\tilde{Q}^{*})\operatorname{col}(\tilde{R}) = \operatorname{col}(\tilde{R}\tilde{Q}^{*})$ and then $\mathsf{M}_4^{L}(\tilde{Q})\operatorname{col}(\tilde{R}\tilde{Q}^{*}) = \operatorname{col}(\tilde{Q}\tilde{R}\tilde{Q}^{*})$. In that sense it is the regular-basis reading of the sandwich, and it has three properties that no other realization shows.

**Lemma (the left regular matrix respects the dagger).** For every $\tilde{Q}$,

$$
\mathsf{M}_4^{L}(\tilde{Q}^{*}) = \mathsf{M}_4^{L}(\tilde{Q})^{\dagger} ,
$$

the conjugate transpose of the regular matrix.

**Proof.** Both sides are conjugate-linear in $\tilde{Q}$ and additive, so it suffices to check the eight real basis elements. On $e_0$ both sides are $I$ and on $ie_0$ both are $-iI$. On $e_k$ the left side is $-\mathsf{M}_4^{L}(e_k)$, and the right side is $\mathsf{M}_4^{L}(e_k)^{\dagger} = \mathsf{M}_4^{L}(e_k)^{\mathsf{T}} = -\mathsf{M}_4^{L}(e_k)$, because left multiplication by the vector unit $e_k$ is given by the products $e_ke_j$, whose four matrices are real and skew-symmetric. On $ie_k$ the left side is $i\mathsf{M}_4^{L}(e_k)$ and the right side is $(i\mathsf{M}_4^{L}(e_k))^{\dagger} = -i\mathsf{M}_4^{L}(e_k)^{\mathsf{T}} = i\mathsf{M}_4^{L}(e_k)$, the same skew-symmetry applied once more.

**Theorem (the sandwich matrix is a product of the two regular matrices).** For every $\tilde{Q}$,

$$
\mathsf{H}_{\tilde Q} = \mathsf{M}_4^{L}(\tilde{Q})\,\mathsf{M}_4^{R}(\tilde{Q}^{*}) ,
$$

the left regular matrix of $\tilde Q$ multiplied by the right regular matrix of its Hermitian conjugate, in that order.

**Proof.** For every $\tilde{R}$, $\mathsf{M}_4^{R}(\tilde{Q}^{*})\operatorname{col}(\tilde{R}) = \operatorname{col}(\tilde{R}\tilde{Q}^{*})$ and $\mathsf{M}_4^{L}(\tilde{Q})\operatorname{col}(\tilde{R}\tilde{Q}^{*}) = \operatorname{col}(\tilde{Q}\tilde{R}\tilde{Q}^{*})$, the defining properties of the two matrices applied in turn; the product therefore carries $\operatorname{col}(\tilde{R})$ to $\operatorname{col}(\tilde{Q}\tilde{R}\tilde{Q}^{*})$, which is what defines $\mathsf{H}_{\tilde Q}$.

The identity is the regular-basis reading of the double centralizer above: the two factors come from the two commuting images $\mathsf{M}_4^{L}(\mathbb{B})$ and $\mathsf{M}_4^{R}(\mathbb{B})$, and their order is immaterial because the images commute. It also says that the sandwich is a **congruence** and not a similarity: a similarity would pair $\tilde{Q}$ with $\tilde{Q}^{-1}$, whereas here the second factor is $\tilde{Q}^{*}$, equal to the inverse only on the unitary slice.

**Corollary (closed form in the coefficient basis).** For every $\tilde{Q}$,

$$
\mathsf{H}_{\tilde Q} = \mathsf{M}_4^{L}(\tilde{Q})\,D\,\mathsf{M}_4^{L}(\tilde{Q})^{*}\,D , \qquad D = \operatorname{diag}(-1,1,1,1) ,
$$

the star being the entrywise complex conjugate.

**Proof.** By the transposition theorem, $\mathsf{M}_4^{R}(\tilde{Q}^{*}) = D\,\mathsf{M}_4^{L}(\tilde{Q}^{*})^{\mathsf{T}}\,D$; by the lemma above, $\mathsf{M}_4^{L}(\tilde{Q}^{*}) = \mathsf{M}_4^{L}(\tilde{Q})^{\dagger}$, and the conjugate transpose is $(\mathsf{M}_4^{L}(\tilde{Q})^{*})^{\mathsf{T}}$. Substituting into the theorem gives the display. Every entry of $\mathsf{H}_{\tilde Q}$ is therefore sesquilinear in the four coefficients of $\tilde{Q}$, so the sandwich is quadratic in $\tilde Q$ and linear in the operand.

**Proposition (the real $8 \times 8$ invariants).** Write $\mathsf{H}_{\tilde Q}^{\mathbb{R}}$ for the realification of $\mathsf{H}_{\tilde Q}$ in the real basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$. Then

$$
\det\bigl(\mathsf{H}_{\tilde Q}^{\mathbb{R}}\bigr) = |N(\tilde{Q})|^{8}, \qquad \operatorname{Tr}\bigl(\mathsf{H}_{\tilde Q}^{\mathbb{R}}\bigr) = 8\,|Q_0|^{2} .
$$

**Proof.** Realification replaces each complex eigenvalue by the pair formed with its conjugate, so the determinant is the squared modulus of the complex determinant and the trace is twice the real part of the complex trace. The sandwich has the four complex eigenvalues $\lambda_i\overline{\lambda_j}$, of product $\lvert\lambda_1\lambda_2\rvert^{4} = \lvert N(\tilde{Q})\rvert^{4}$ and of sum $\lvert\operatorname{tr}\mathsf{M}_4^{L}(\tilde{Q})\rvert^{2} = 4\lvert Q_0\rvert^{2}$ (*The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint*); the realification therefore gives $(\lvert N\rvert^{4})^{2} = \lvert N\rvert^{8}$ for the determinant and $2\cdot 4\lvert Q_0\rvert^{2} = 8\lvert Q_0\rvert^{2}$ for the trace. The two agree with the real form of the element above to the same exponents: the left regular matrix $\mathsf{M}_4^{L}(\tilde{Q})$ has $\lvert N\rvert^{4}$ and $8\operatorname{Re}Q_0$, the sandwich matrix has $\lvert N\rvert^{8}$ and $8\lvert Q_0\rvert^{2}$, and the second invariant of each is a modulus rather than a real part because the sandwich has lost the phase.

## A Second $4 \times 4$ Realization, and the Multiplicative Map

The regular matrix is not the only $4 \times 4$ realization of $\mathbb{B}$ in use, and the second one worth recording comes from a question with no algebra in it: the eigenvectors of a parameterised family of matrices. Its shape is different enough that the difference is instructive, and the object it is built for — a multiplicative quadratic map into the real matrices, with no counterpart in the regular realization — is the reason for recording it here rather than in a dedicated article.

**The realization.** In the basis $e_0, ie_1, ie_2, ie_3$, for which

$$
(ie_1)^2 = (ie_2)^2 = (ie_3)^2 = e_0, \qquad (ie_1)(ie_2) = i(ie_3), \qquad (ie_2)(ie_3) = i(ie_1), \qquad (ie_3)(ie_1) = i(ie_2) ,
$$

the matrix whose columns are the coordinate columns of $\tilde Q e_0, \tilde Q ie_1, \tilde Q ie_2, \tilde Q ie_3$, written $\mathsf{M}'_4$ for this second realization to keep it apart from the regular matrix $\mathsf{M}_4^{L}$,

$$
\mathsf{M}'_4(A_0, A_1, A_2, A_3) = \begin{pmatrix} A_0 & A_1 & A_2 & A_3 \\ A_1 & A_0 & -iA_3 & iA_2 \\ A_2 & iA_3 & A_0 & -iA_1 \\ A_3 & -iA_2 & iA_1 & A_0 \end{pmatrix}
$$

is a multiplicative realization of $\mathbb{B}$. Its first row and column coincide, since $\mathsf{M}'_4$ is symmetric in the coefficients, which the Cayley matrix of *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* is not; the price is the scalar imaginary scattered through the lower block. The change of basis is what makes the squares $+e_0$: the generators of this realization are the elements $ie_k$, not the $e_k$, and the difference is a change of orientation, the two choices being interchanged by the coefficient conjugation, not two different algebras.

**The realization is equivalent to the regular one.** Both are faithful four-dimensional linear realizations of $\mathbb{B} \cong M_2(\mathbb{C})$, and by the module structure of the section above every such realization is two copies of the simple module, $V \oplus V$; so an invertible intertwining matrix exists, and one was exhibited and checked on $100$ random elements, with maximum residual $1.9 \times 10^{-15}$. Nothing in the representation theory of the two distinguishes them, and everything the corpus says about the regular representation as a module carries over.

**What the realization brings.** Each of $ie_1, ie_2, ie_3$ is skew **for the Minkowski form** $D$ of the remark below, $M^{\mathsf T} = -DMD$, and not in the plain sense: it is the form's matrix, not the identity, that makes them skew. The products of the basis elements give a second Hermitian basis of $M_4(\mathbb{C})$: the sixteen matrices

$$
I,\; ie_1K_1,\; ie_2K_2,\; ie_3K_3,\quad ie_1,\; K_1,\; ie_2K_3,\; ie_3K_2,\quad ie_2,\; K_2,\; ie_1K_3,\; ie_3K_1,\quad ie_3,\; K_3,\; ie_1K_2,\; ie_2K_1 ,
$$

with $K_1, K_2, K_3$ the coefficient conjugates of $ie_1, ie_2, ie_3$, each squaring to $I$ and each Hermitian, so that real linear combinations of them are exactly the Hermitian $4 \times 4$ matrices; every one but $I$ is traceless. This was checked entry by entry. The same basis contains generators of the complex Clifford algebra $\mathbb{C}\ell(4)$, namely $ie_1, ie_2, ie_3K_1, ie_3K_2$, which anticommute pairwise to $\delta_{ij}I$ up to the conventional factor, so the realization also places $\mathbb{B}$ inside $M_4(\mathbb{C})$ in the Clifford manner of *The Clifford Algebra Representation*.

**The transposition identity is exact in this basis, and these are the matrices of the Maxwell literature.** The realization is the one in which the two $D$'s of the theorem of the transposition section disappear, and this is worth stating because it separates two things that the first basis runs together. Write the left regular matrix of the element $\tilde{Q} = A_0 e_0 + A_1 ie_1 + A_2 ie_2 + A_3 ie_3$ in this realization as

$$
\mathsf{M}'_4(\tilde{Q}) = A_0 I + cF(\mathbf{A}), \qquad
cF(\mathbf{A}) := \begin{pmatrix} 0 & \mathbf{A}^{\mathsf{T}} \\ \mathbf{A} & i[\mathbf{A}]_\times \end{pmatrix}, \qquad \mathbf{A} = (A_1, A_2, A_3),
$$

with $[\mathbf{u}]_\times$ the matrix of $\mathbf{v} \mapsto \mathbf{u} \times \mathbf{v}$; this is the display of the realization above, and it is the same $cF$ that a matrix formulation of Maxwell's equations multiplies into the column $(-\partial_t, \nabla)^{\mathsf{T}}$. In this basis the right regular matrix is **exactly the transpose**,

$$
\mathsf{M}'^{R}_4(\tilde{Q}) = \mathsf{M}'_4(\tilde{Q})^{\mathsf{T}} ,
$$

with no sign matrix, where in the basis $e_0, e_1, e_2, e_3$ of the transposition section the relation read $\mathsf{M}_4^{R} = D\,\mathsf{M}_4^{L}{}^{\mathsf{T}}D$ instead. Both were recomputed over $100$ random elements, the first to $0$ and the second to $0$, and the change of basis between the two conventions was checked explicitly too: with $C = \operatorname{diag}(1, -i, -i, -i)$ carrying the coefficients of the corpus basis into those of this one, $C\mathsf{M}_4^{L}(\tilde{Q})C^{-1}$ and $C\mathsf{M}_4^{R}(\tilde{Q})C^{-1}$ are the two matrices displayed here, at residual $0$. So the *false identity* remark of the transposition section is a statement about a basis and not about the algebra: in the basis whose vector units square to $-e_0$ the transpose of the left matrix is the left regular matrix of the conjugate, while in the basis whose vector units square to $+e_0$ it is the right regular matrix, exactly, and the two $D$'s are the price of the first basis. The sixteen-matrix basis above is the same object read on the other side: as matrices it is $I$, the three $cF(\mathbf{e}_i)$, their complex conjugates and the pairwise products $cF(\mathbf{e}_i)(cF(\mathbf{e}_j))^{\natural}$, which are Hermitian and involutive with square $I$, traceless except for $I$, and orthogonal under the trace, $\operatorname{tr}(M_kM_l) = 4\delta_{kl}$ — all checked exactly — and the three $cF(\mathbf{e}_i)$ anticommute pairwise with $cF(\mathbf{e}_1)cF(\mathbf{e}_2) = i\,cF(\mathbf{e}_3)$.

**The multiplicative map.** The object the realization is built for is

$$
m(A) = A A^{\natural}, \qquad A \in I + \mathbb{B},
$$

the **multiplicative map** $m(A) = A A^{\natural}$, named after the complex absolute value. Since $A^{\natural}$ commutes with $A$, the product is central, and in this realization it is the **scalar** matrix

$$
m(A) = \bigl(A_0^2 - A_1^2 - A_2^2 - A_3^2\bigr) I \;=\; \Delta(A)\, I ,
$$

checked exactly (all four entries equal, the off-diagonal ones vanishing). The image is therefore a real matrix exactly when the four coefficients $A_\mu$ are real, and $\Delta$ is then the Lorentzian square of the coefficient vector; for a genuinely complex element $\Delta$ need not be real — at $A = (1+i)e_0$ it is $2i$ — so it is the *centrality* that the commutation with $A^{\natural}$ delivers, and the reality of the image is a separate property of the real coefficient set. Multiplicativity follows from the centrality, $m(AB) = ABB^{\natural}A^{\natural} = A\cdot\Delta(B)\cdot A^{\natural} = \Delta(A)\Delta(B)I = m(A)m(B)$, and it was checked exactly as well. The read-off of the map is a quadratic map with no complex-linear analogue. What the corpus takes from the map is the existence of a *multiplicative* quadratic real map of this kind at all, next to the one it already owns: the congruence $Y\mapsto \mathsf{M}_2(\tilde{Q})\,Y\,\mathsf{M}_2(\tilde{Q})^{\dagger}$ of *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* is the quadratic map of the same algebra that is **not** multiplicative, being a congruence rather than a product, and the two together show that the algebra carries a multiplicative and a non-multiplicative quadratic map.

**The Minkowski form of the realization.** The real span of $e_0, ie_1, ie_2, ie_3$ carries a real form of signature $(1,3)$, whose matrix in the coefficient order $(e_0, ie_1, ie_2, ie_3)$ is

$$
D = \operatorname{diag}(-1, 1, 1, 1)
$$

— the same sign matrix as in the transposition theorem above, one negative square on the scalar slot and three positive ones on the vector slots.

**Proposition (the generators are the infinitesimal generators of $O(1,3)$).** Each of the three generators satisfies

$$
M^{\mathsf T} = -DMD, \qquad \text{equivalently} \qquad M^{\mathsf T}D + DM = 0,
$$

that is, $DM$ is skew-symmetric; the second form is the defining condition for an element of the Lie algebra $\mathfrak{o}(1,3)$ of $O(1,3)$.

**Proof.** Direct verification on the three matrices $ie_1, ie_2, ie_3$ of the realization, entry by entry and exactly, in each of the three equivalent forms. $\square$

The relation is a statement about the form and its orthogonal group, and the difference between it and the plain statement "$M$ is skew-symmetric" is the whole content: the three matrices are not skew in the plain sense, and it is $D$, not $I$, that makes them skew. Two real forms live here and they are different objects. The **general quaternionic bilinear form** $\langle\tilde{P},\tilde{Q}\rangle_{\natural} = \operatorname{Sc}(\tilde{P}\tilde{Q}^{\natural})$ is $\mathbb{C}$-bilinear and indefinite of signature $(4,4)$ on the eight-dimensional $\mathbb{B}_{\mathbb{R}}$, and it vanishes on the null elements; it is the form *of the algebra*, and it is owned by *The General Quaternionic Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*. The **Minkowski form** above is a real form of signature $(1,3)$ on the four-dimensional real slice spanned by $e_0, ie_1, ie_2, ie_3$, and it is the form *of the realization's real slice*, with orthogonal group $O(1,3)$; it is not a form of the eight-dimensional realification, whose four realified forms have signatures $(4,4)$, $(4,4)$, $(8,0)$ and $(2,6)$ (*The Realification of the Four Forms*).

## The Sixteen Products and the Biparavectors

The double centralizer of the earlier section says that the left and the right images commute and that together they span the whole matrix algebra. The basis that exhibits this is the set of products of one matrix from each image, and in the second realization it can be taken Hermitian.

**The products.** For the coordinate units put

$$
P_{ij} := \mathsf{M}_4^{L}(e_i)\,\mathsf{M}_4^{R}(e_j), \qquad i, j \in \{0, 1, 2, 3\}.
$$

In the second realization the right regular matrix is the transpose of the left, so $P_{ij}$ is the ordinary matrix product $\mathsf{M}'_4(e_i)\mathsf{M}'_4(e_j)^{\mathsf T}$; writing $E_i := \mathsf{M}'_4(e_i)$ for $i = 1, 2, 3$ and $E_0 = I$,

$$
P_{ij} = E_i E_j^{\mathsf T}.
$$

The three units satisfy $E_k^2 = I$ and anticommute pairwise, and their product is the complex structure of the realization, $E_1E_2 = iE_3$; the matrices $E_k$ are Hermitian, so $E_j^{\mathsf T}$ is its complex conjugate.

**Proposition (the sixteen products are an orthogonal basis).** The matrices $E_iE_j^{\mathsf T}$ are Hermitian, linearly independent over $\mathbb{C}$, and orthogonal under the trace, with a common normalisation:

$$
\operatorname{tr}\!\left(E_i E_j^{\mathsf T}\, E_k E_l^{\mathsf T}\right) = 4\,\delta_{ik}\delta_{jl}.
$$

This was checked entry by entry: the diagonal value is $4$ for each of the sixteen and every off-diagonal value is $0$. Independence follows, and the sixteen are a basis of $M_4(\mathbb{C})$.

**The expansion.** By the orthogonality every complex matrix $M$ has the expansion

$$
M = \sum_{i,j} a_{ij}\,E_iE_j^{\mathsf T}, \qquad a_{ij} = \tfrac14\operatorname{tr}\!\left(M\,E_iE_j^{\mathsf{T}}\right),
$$

the coefficients being read off one at a time. Recomputing the expansion on a random complex $4 \times 4$ matrix returns it to $5 \times 10^{-16}$.

**Reading the expansion in the algebra.** The tensor square $\mathbb{B} \otimes_{\mathbb{C}} \mathbb{B}$ is spanned by the sixteen $e_i \otimes e_j$, and the expansion says that these sixteen span the whole matrix algebra $M_4(\mathbb{C})$: the two-sided transformation $\tilde P \mapsto \sum_{i,j} a_{ij}\, e_i \tilde P e_j$ has matrix

$$
\sum_{i,j} a_{ij}\,\mathsf{M}_4^{L}(e_i)\,\mathsf{M}_4^{R}(e_j) = \sum_{i,j} a_{ij}\,P_{ij},
$$

and every complex matrix arises this way. Such an element $\sum a_{ij}\,e_i \otimes e_j$ is a **biparavector** in the language of the paravector formulation. That the sixteen products already span the matrices is the concrete form of the double centralizer: the left image supplies the first index and the right image the second, and the two fill $M_4(\mathbb{C})$ between them. Recomputing the matrix of the biparavector against the product $\mathsf{M}_4^{L}(\tilde A)\mathsf{M}_4^{R}(\tilde B)$ of a left–right sandwich returns $1.5 \times 10^{-14}$.

**Where the uniform normalisation comes from.** The constant $4$ in the trace relation is a property of the second realization and not of the regular basis. In the corpus basis $e_0, e_1, e_2, e_3$ the matrix of the sixteen products is still diagonal, but its diagonal entries are $\pm 4$ rather than $4$, so the coefficient formula there carries the sign of $\operatorname{tr}(P_{ij}^2)$; it is the Hermitian realisation that makes the coefficients uniform. The tensor-square reading is the same object as the sixteen matrices listed by the realization above, read as outer products rather than as products of the two units.

## The Three Classical Functions and Their Matrices

The Conway calculus singles out three linear functions of the algebra, of the antisymmetric, the diagonal and the diagonal-less symmetric type. In the coordinate order $(e_1,e_2,e_3,e_0)$ — vector part first, scalar last, the order of the displays — they are, with $t_1=s_2s_3$, $t_2=s_1s_3$ and $t_3=s_1s_2$,

$$
A\{a\}=\tfrac12\bigl(a[\,]-[\,]a\bigr)\ \longleftrightarrow\
\begin{pmatrix}0&-a_3&a_2&0\\a_3&0&-a_1&0\\-a_2&a_1&0&0\\0&0&0&0\end{pmatrix},
$$

$$
D\{d\}=\tfrac12\bigl(d_1e_1[\,]e_1+d_2e_2[\,]e_2+d_3e_3[\,]e_3\bigr)
\ \longleftrightarrow\
\tfrac12\begin{pmatrix}-d_1+d_2+d_3&0&0&0\\0&d_1-d_2+d_3&0&0\\0&0&d_1+d_2-d_3&0\\0&0&0&-(d_1+d_2+d_3)\end{pmatrix},
$$

$$
S\{s\}=D\{s_1^2,s_2^2,s_3^2\}-\tfrac12\,s[\,]s
\ \longleftrightarrow\
\begin{pmatrix}0&t_3&t_2&0\\t_3&0&t_1&0\\t_2&t_1&0&0\\0&0&0&0\end{pmatrix}.
$$

**Proposition (the matrix dictionary).** In the order $(e_1,e_2,e_3,e_0)$ the function $A\{a\}$ is the antisymmetric $3\times3$ block, $D\{d\}$ the traceless diagonal and $S\{s\}$ the diagonal-less symmetric $3\times3$ block, each with a vanishing fourth row and column, and the three families together span the traceless part of $M_3(\mathbb C)$.

*Proof.* Direct computation of the sixteen matrices and comparison with the displays. The coordinate order is a genuine trap: the corpus's basis order is $(e_0,e_1,e_2,e_3)$, whereas the matrix displays put the scalar last, and in the corpus's order the same matrices appear shifted by one. Verified numerically: exact in the order $(e_1,e_2,e_3,e_0)$, and not in the order $(e_0,e_1,e_2,e_3)$.

**Remark (the source's sign).** The source writes the symmetric function with the two terms in the opposite order, $S\{s\}=\tfrac12 s[\,]s-D\{s_1^2,s_2^2,s_3^2\}$; its two displays of $S$ then differ by an overall sign. The corpus fixes the sign by the printed matrix, the one written here. $A\{a\}$ and $D\{d\}$ reproduce the source's displays exactly, with zero residual.

**Remark (the method degrades from three to four dimensions).** The antisymmetric, diagonal and diagonal-less symmetric functions exhaust the traceless part of $M_3(\mathbb C)$ in the order $(e_1,e_2,e_3,e_0)$, since each acts on the vector part and fixes the scalar. For a general traceless $\mathbb C^4\to\mathbb C^4$ map the same three families no longer suffice: the symmetric part needs a function that mixes the scalar and vector parts, and the source records that the expression for it is cumbersome and not useful. The four-dimensional unitary groups are therefore assembled from two $SO(4)$ factors rather than from a single quaternion closed form — the same asymmetry that the Lie-group article reads as the clean three-dimensional and less clean four-dimensional parametrizations.

## Summary

The left regular matrix $\mathsf{M}_4^{L}$ of *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* is the Cayley matrix of the left multiplication, with its multiplicativity, its trace $4Q_0$ and its determinant $N(\tilde{Q})^2$ recorded there. Its transpose is the left regular matrix of the quaternion conjugate, $\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}} = \mathsf{M}_4^{L}(\tilde{Q}^{\natural})$.

The right regular matrix $\mathsf{M}_4^{R}$, whose $m$-th column is the coordinate column of $e_m\tilde Q$, is anti-multiplicative and is the regular representation of the opposite algebra. The naive identity $\mathsf{M}_4^{R}(\tilde{Q}) = \mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}}$ is false — and the variant with $\tilde{Q}^{\natural}$ is the same statement, since $\mathsf{M}_4^{L}(\tilde{Q}^{\natural})^{\mathsf{T}} = \mathsf{M}_4^{L}(\tilde{Q})$ — while what holds is $\mathsf{M}_4^{R}(\tilde{Q}) = D\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}}D = D\mathsf{M}_4^{L}(\tilde{Q}^{\natural})D$ with $D = \operatorname{diag}(-1,1,1,1)$. The difference $\mathsf{M}_4^{L} - \mathsf{M}_4^{R}$ vanishes exactly on the centre $\mathbb{C}_{\mathbb{B}}$, and its $m$-th column is the coordinate column of $[\tilde Q, e_m]$; that is the precise sense in which left and right differ because the algebra is non-commutative.

The regular module is $\mathbb{B} = I_1 \oplus I_2$ with $I_1 = \mathbb{B}\tilde\Pi_1$, $I_2 = \mathbb{B}\tilde\Pi_2$ and $\tilde\Pi_1 = \tfrac{1}{2}(e_0 + ie_3)$, $\tilde\Pi_2 = \tfrac12(e_0 - ie_3)$; in the adapted basis $\tilde\Pi_1, e_1\tilde\Pi_1, \tilde\Pi_2, e_1\tilde\Pi_2$ the left regular matrix is diagonal over the two invariant subspaces $I_1$, $I_2$, each a copy of the simple module $V$. So the regular module is $V \oplus V$, the regular representation is reducible, and it is the first reducible realization of this subcategory. The centralizer of $\mathsf{M}_4^{L}(\mathbb{B})$ is the right copy $\mathsf{M}_4^{R}(\mathbb{B})$, of complex dimension $4$. Over $\mathbb{R}$ the left regular matrix is $8 \times 8$ real with $\det = |N|^4$ and trace $8\operatorname{Re}(Q_0)$, the dimension doubling by restriction of scalars. The Hermitian sandwich $\tilde R \mapsto \tilde Q\tilde R\tilde Q^{*}$ has the matrix $\mathsf{H}_{\tilde Q} = \mathsf{M}_4^{L}(\tilde{Q})\,\mathsf{M}_4^{R}(\tilde{Q}^{*}) = \mathsf{M}_4^{L}(\tilde{Q})\,D\,\mathsf{M}_4^{L}(\tilde{Q})^{*}\,D$, a congruence and not a similarity; its realification has $\det = |N|^{8}$ and trace $8|Q_0|^{2}$.

A second $4 \times 4$ realization, the one used in the literature on eigenvector bundles, is equivalent to the regular one as a module — every faithful four-dimensional complex realization is $V \oplus V$ — and it carries a multiplicative quadratic map $m(A) = A A^{\natural} = \Delta(A) I$ of the algebra into the scalar matrices, $\Delta = A_0^2 - A_1^2 - A_2^2 - A_3^2$, which is a real quadratic map on the real coefficients and which the regular realization does not have, in contrast with the congruence-shaped quadratic map of *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*. Its real slice $e_0, ie_1, ie_2, ie_3$ carries the Minkowski form $D = \operatorname{diag}(-1,1,1,1)$, of signature $(1,3)$, for which the three generators are the infinitesimal generators of $O(1,3)$, $M^{\mathsf T} = -DMD$; this is the form of the realization's real slice and must be distinguished from the general quaternionic bilinear form of signature $(4,4)$, which is the form of the eight-dimensional algebra. In that realization the sixteen products $\mathsf{M}_4^{L}(e_i)\mathsf{M}_4^{R}(e_j)$ are the Hermitian outer products $E_iE_j^{\mathsf T}$ and form a basis of $M_4(\mathbb{C})$ orthogonal for the trace, $\operatorname{tr}(P_{ij}P_{kl}) = 4\delta_{ik}\delta_{jl}$; the expansion it gives is the tensor-square reading of the double centralizer, and it says that every complex matrix is a biparavector, $\sum a_{ij}\,\mathsf{M}_4^{L}(e_i)\mathsf{M}_4^{R}(e_j)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | Biquaternion algebra |
| $e_0, e_1, e_2, e_3$ | Algebra basis, $e_0 = 1$, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ | Developed form, $Q_\mu \in \mathbb{C}$ |
| $Q^\mu = (Q^0, Q^1, Q^2, Q^3)$ | Four-vector; $Q^0 = Q_0$, $(Q^1, Q^2, Q^3) = (Q_1, Q_2, Q_3)$ |
| $\operatorname{col}(\tilde S)$ | Coordinate column of $\tilde S$ in the basis $e_0, e_1, e_2, e_3$ |
| $\mathsf{M}_4^{L}(\tilde{Q})$ | Left regular matrix, whose $m$-th column is $\operatorname{col}(\tilde Q e_m)$; written $\mathsf{M}_4(\tilde{Q})$ in *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* |
| $\mathsf{M}_4^{R}(\tilde{Q})$ | Right regular matrix, whose $m$-th column is $\operatorname{col}(e_m \tilde Q)$ |
| $D = \operatorname{diag}(-1,1,1,1)$ | Fixed sign matrix of the transposition theorem, $\mathsf{M}_4^{R}(\tilde{Q}) = D\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}}D$, and matrix of the Minkowski form of the second realization, $M^{\mathsf T} = -DMD$ |
| $N(\tilde{Q}) = \sum_\mu Q_\mu^2$ | The norm; $\det\mathsf{M}_4^{L}(\tilde{Q}) = N(\tilde{Q})^2$ |
| ${}^{\natural}, \bar{\cdot}, {}^{*}, {}^{\flat}$ | Quaternion, complex, Hermitian and anti-Hermitian conjugations |
| $\mathbb{C}_{\mathbb{B}}$ | Centre, the scalar subspace $\mathbb{C} e_0$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real quaternion subalgebra; its restriction carries the quaternion regular representation of *Quaternion Element Representations* |
| $\tilde\Pi_1 = \tfrac{1}{2}(e_0 + ie_3)$, $\tilde\Pi_2 = \tfrac12(e_0 - ie_3)$ | Orthogonal idempotents, $\tilde\Pi_1 + \tilde\Pi_2 = e_0$, $\tilde\Pi_1\tilde\Pi_2 = 0$ |
| $I_1 = \mathbb{B}\tilde\Pi_1$, $I_2 = \mathbb{B}\tilde\Pi_2$ | The two minimal left ideals, $\mathbb{B} = I_1 \oplus I_2$ |
| $V = \mathbb{C}^2$ | Simple left $\mathbb{B}$-module, complex dimension $2$ |
| $\mathbb{B}^{\mathrm{op}}$ | Opposite algebra; the right regular matrix is a homomorphism from it |
| $\epsilon^{ijk}$ | Levi-Civita symbol on the indices $1, 2, 3$ |
| $\operatorname{Res}_{\mathbb{C}/\mathbb{R}}$ | Restriction of scalars |
| $\operatorname{cent}_{M_4(\mathbb{C})}\mathsf{M}_4^{L}(\mathbb{B}) = \mathsf{M}_4^{R}(\mathbb{B})$ | The centralizer of the left image is the right copy, of complex dimension $4$ |
| $\mathsf{M}_4^{L,\mathbb{R}}(\tilde{Q})$ | Real $8 \times 8$ left regular matrix |
| $\mathsf{H}_{\tilde Q} = \mathsf{M}_4^{L}(\tilde{Q})\mathsf{M}_4^{R}(\tilde{Q}^{*})$ | The sandwich matrix, carrying $\operatorname{col}(\tilde R)$ to $\operatorname{col}(\tilde Q\tilde R\tilde Q^{*})$; closed form $\mathsf{M}_4^{L}(\tilde{Q})D\mathsf{M}_4^{L}(\tilde{Q})^{*}D$, realification with $\det = \lvert N\rvert^{8}$ and trace $8\lvert Q_0\rvert^{2}$ |
| $\mathsf{M}'_4(A_0, A_1, A_2, A_3)$ | Second $4 \times 4$ realization, on the generators $ie_1, ie_2, ie_3$ with $(ie_1)^2 = (ie_2)^2 = (ie_3)^2 = e_0$ |
| $K_1, K_2, K_3$ | Coefficient conjugates of $ie_1, ie_2, ie_3$, used in the Hermitian basis of that realization |
| $m(A) = A A^{\natural} = \Delta(A)I$ | The multiplicative map, $I + \mathbb{B} \to M_4(\mathbb{C})$; $\Delta = A_0^2 - A_1^2 - A_2^2 - A_3^2$, a real matrix for real coefficients, multiplicative |
| $\mathfrak{o}(1,3)$ | Lie algebra of $O(1,3)$, $\{M : M^{\mathsf T}D + DM = 0\}$, to which the generators $ie_k$ belong |
| $P_{ij} = \mathsf{M}_4^{L}(e_i)\mathsf{M}_4^{R}(e_j) = E_iE_j^{\mathsf T}$ | The sixteen products; an orthogonal basis of $M_4(\mathbb{C})$, $\operatorname{tr}(P_{ij}P_{kl}) = 4\delta_{ik}\delta_{jl}$ |
| $\sum a_{ij}\,e_i \otimes e_j$ | Biparavector, whose matrix is $\sum a_{ij}\,P_{ij}$ |
| $\mathbb{M}_+$ | Hermitian subspace of real dimension $4$ |

## Further Reading

- *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_maths/introduction-to-the-4x4-matrix-element-representation-of-biquaternions.md`), for the left regular matrix, its Cayley form, the multiplicativity, the trace and the determinant, and the remarkable subspace conditions

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the regular representation of an algebra and the identification of its centralizer.
- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Interscience, 1962), for the regular module, its decomposition into minimal left ideals and the double centralizer theorem.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules*, 2nd edition (Springer, 1992), for the regular module as a left module over itself and the centralizer of the left copy.
- William Fulton and Joe Harris, *Representation Theory: A First Course*, Graduate Texts in Mathematics 129 (Springer, 1991), for the regular representation as the direct sum of the simple modules with multiplicity equal to their dimensions.
- John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288 (Springer, 2021), for the regular representation of a quaternion algebra and its complexification.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the Cayley matrix of quaternion multiplication and its transpose.
- *The General Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/the-general-plain-algebra-in-the-4x4-matrix-element-representation.md`), the first of the four articles reading the four forms on the regular matrix, each with the structure attached to its form.
- D. H. Gottlieb, "Eigenbundles, Quaternions, and Berry's Phase," arXiv:math/0304281 [math.AT] (2003), for the second $4 \times 4$ realization and the map $m(A) = A A^{\natural}$ of the section above; the paper's $4 \times 4$ matrices are Example 5 and the map $m(A) = A A^{\natural}$ is its section 5.
- D. H. Gottlieb, "Maxwell's equations" (1 August 2004, 12 pp.), for the matrix formulation of Maxwell's equations in which the field matrix is $A_0 I + cF$ of the realization above, the dual form in which the derivatives stand in the matrix and the field in the column, and the identity $\mathsf{M}'^{R}_4 = \mathsf{M}'_4{}^{\mathsf{T}}$ which holds there without a sign matrix; cited for the identification of the second realization with the matrices of the Maxwell literature and for the transposition remark of that section. Its section 5 is the source of the sixteen-product basis and the biparavectors of the section above: the coefficient formula $a_{ij} = \tfrac14\operatorname{tr}(ME_iE_j^{\mathsf{T}})$, the orthogonality of the basis for the trace, and the reading of the products as the tensor square of the algebra acting on itself on both sides. The paper's potential-level equations (13) and (14) are recorded in *Maxwell's Equations in Biquaternionic Form* with their vector parts corrected.

- A. Gsponer, "Explicit closed-form parametrization of SU(3) and SU(4) in terms of complex quaternions and elementary functions," arXiv:math-ph/0211056v2, 2002, §2–4, for the Conway operators $e_n[\,]e_m$, the composition and association rules, the functions $A\{a\}$, $D\{d\}$, $S\{s\}$ and their $4\times4$ matrix displays (10′)–(13′), the rule $G^{-1}=G^{+\approx}=G^{\dagger}$ for the group elements, and the remark that the quaternion method loses power from three to four dimensions.
- A. W. Conway, "Quaternions and matrices," *Proceedings of the Royal Irish Academy* **A 50** (1945) 98–130, and J. L. Synge, "Quaternions, Lorentz transformations, and the Conway–Dirac–Eddington matrices," *Communications of the Dublin Institute for Advanced Studies* **A 21** (1972), for the Conway operator calculus in its original form.
