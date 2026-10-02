
# __Biquaternion 4×4 Regular Matrix Element Representation__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is the four-dimensional complex algebra with basis $e_0 = 1, e_1, e_2, e_3$, where $e_k^2 = -e_0$ and $e_j e_k = -e_k e_j$ for $j \neq k$, and with a central scalar imaginary $i$ satisfying $i^2 = -1$. A general element is $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$. The algebra, its biquaternion norm, its conjugations, its six distinguished subspaces and its matrix realization are those of *Biquaternion Algebra*, *Biquaternion Four-Vector Element Representation* and *Biquaternion 2×2 Matrix Element Representation*.

This article presents the **regular representation** of $\mathbb{B}$: the algebra acting on itself on the left, and the $4 \times 4$ matrix of that action in the coefficient space of *Biquaternion Four-Vector Element Representation*. The word *representation* is used here in both senses at once, the concrete realization and the technical representation of an algebra on a vector space, because the action is the object of study. The article is the third and last of the group, and it uses both predecessors: the coefficient space of the first article, on which the operator is written, and the simple module $V$ of the second, because the algebra is $V \oplus V$ as a left module and the regular representation is therefore reducible. It is the first reducible realization met in this subcategory.

The article owns the $4 \times 4$ regular matrix, the left and right multiplication operators, the relation between them, including the plausible identity that is false, the decomposition $\mathbb{B} = I_1 \oplus I_2 \cong V \oplus V$, and the centralizer statement. It deliberately does not treat the regular representation of the real quaternions $\mathbb{H}$, which belongs to *Quaternion Element Representations* and is cited once as the restriction to a real subalgebra; it does not treat the eigenvalues, the Cayley–Hamilton identity or the eigenspace dimensions of the regular matrix, which belong to *Biquaternion Spectral Theory*, later in this chapter; and it does not treat the idempotents and the Peirce decomposition, which belong to *Biquaternion Ideals and Peirce Decomposition*, except to cite the idempotent that splits the algebra into its two minimal left ideals. No physical vocabulary is used: the two-sided action of the unit-norm group is a group action on a real vector space preserving a quadratic form, and the double cover is a group homomorphism with kernel of order two; it is not a spinor, a chirality or a handedness of a physical particle.

One comparative item is added beyond the regular matrix itself: a second $4 \times 4$ realization of $\mathbb{B}$ taken from the literature on eigenvector bundles, recorded with the multiplicative quadratic map it carries, because it is the natural contrast with both the regular realization and the congruence-shaped operator of *Biquaternion 4×4 Regular Matrix Operator Representation*.

## The Left Regular Representation

**Definition.** The **left regular representation** of $\mathbb{B}$ is the map

$$
\rho_L : \mathbb{B} \longrightarrow \operatorname{End}_{\mathbb{C}}(\mathbb{B}), \qquad \rho_L(\tilde{Q})(\tilde{R}) = \tilde{Q}\tilde{R}.
$$

For each $\tilde{Q}$, the map $\tilde{R} \mapsto \tilde{Q}\tilde{R}$ is $\mathbb{C}$-linear because multiplication is bilinear, so $\rho_L(\tilde{Q})$ is a $\mathbb{C}$-linear endomorphism of the four-dimensional space $\mathbb{B}$. Writing each endomorphism as a matrix in the basis $e_0, e_1, e_2, e_3$, the same symbol $\rho_L(\tilde{Q})$ denotes the matrix acting on the $4 \times 1$ column $R$ of *Biquaternion Four-Vector Element Representation*:

$$
\widetilde{\tilde{Q}\tilde{R}} \longleftrightarrow \rho_L(\tilde{Q})\, R .
$$

**Proposition (the regular matrix is the Cayley matrix).** In the basis $e_0, e_1, e_2, e_3$,

$$
\rho_L(\tilde{Q}) = \begin{pmatrix}
Q_0 & -Q_1 & -Q_2 & -Q_3 \\
Q_1 & Q_0 & -Q_3 & Q_2 \\
Q_2 & Q_3 & Q_0 & -Q_1 \\
Q_3 & -Q_2 & Q_1 & Q_0
\end{pmatrix}.
$$

Each entry is a single coefficient of $\tilde{Q}$ carrying a sign, and **no entry is a sum of two or more coefficients**, because in this basis each product of basis elements is one basis element times a sign.

**Proof.** The columns of the matrix are the images $\rho_L(\tilde{Q})(e_m) = \tilde{Q}e_m$, expressed in the basis. For $m = 0$ the image is $\tilde{Q}$ itself, giving the first column $(Q_0, Q_1, Q_2, Q_3)$. For $m = k \geq 1$ one uses $e_0 e_k = e_k$ and $e_j e_k = \epsilon^{ijk} e_i$ for $j \neq k$ with $\{i, j, k\} = \{1, 2, 3\}$, so that

$$
\rho_L(\tilde{Q})(e_k) = Q_0 e_k + Q_k e_k^2 + \sum_{j \neq k} Q_j e_j e_k = Q_0 e_k - Q_k e_0 + \sum_{j \neq k} \epsilon^{ijk} Q_j e_i .
$$

Expanding with $e_1 e_2 = e_3$, $e_2 e_3 = e_1$, $e_3 e_1 = e_2$ gives the displayed columns, hence the matrix.

**Remark (the same four for a different reason).** The matrix above is $4 \times 4$, and the coefficient space of *Biquaternion Four-Vector Element Representation* has complex dimension $4$. These are the same four for the same reason and not because of a coincidence: the algebra has complex dimension $4$, and the regular representation is the algebra acting on itself, so the space and the index set of the matrix are the same object. In *Biquaternion 2×2 Matrix Element Representation* the number $2$ appears both as the dimension of the simple module and as the size of the matrix algebra, for the parallel reason that the algebra is the algebra of endomorphisms of that module.

**Example.** For the element $\tilde{Q} = (2+i)e_0 + (1-i)e_1 + 3e_2 + ie_3$, so that $(Q_0, Q_1, Q_2, Q_3) = (2+i, 1-i, 3, i)$, the regular matrix is

$$
\rho_L(\tilde{Q}) = \begin{pmatrix}
2+i & -1+i & -3 & -i \\
1-i & 2+i & -i & 3 \\
3 & i & 2+i & -1+i \\
i & -3 & 1-i & 2+i
\end{pmatrix}.
$$

The column of $\tilde{R} = e_0 + e_1$, namely $R = (1, 1, 0, 0)$, is carried by this matrix to the column $(1+2i, 3, 3+i, -3+i)$, which is the four-vector of the product $\tilde{Q}\tilde{R}$ computed by the component formula of *Biquaternion Four-Vector Element Representation*.

## The Left Representation Is a Homomorphism

**Theorem (multiplicativity).** For all $\tilde{Q}, \tilde{R} \in \mathbb{B}$,

$$
\rho_L(\tilde{Q})\,\rho_L(\tilde{R}) = \rho_L(\tilde{Q}\tilde{R}).
$$

Hence $\rho_L$ is an algebra homomorphism and the coefficient space is a left $\mathbb{B}$-module under it.

**Proof.** Both sides are $\mathbb{C}$-linear in the second factor and are computed on the basis. For every $m$, associativity of the algebra gives

$$
\rho_L(\tilde{Q})\bigl(\rho_L(\tilde{R})(e_m)\bigr) = \tilde{Q}(\tilde{R}e_m) = (\tilde{Q}\tilde{R})e_m = \rho_L(\tilde{Q}\tilde{R})(e_m),
$$

so the two matrices agree on a basis.

**Example (a concrete check).** For $\tilde{Q} = e_0 + e_1$ and $\tilde{R} = e_0 + e_2$ the product is $\tilde{Q}\tilde{R} = e_0 + e_1 + e_2 + e_3$ and the two matrices are

$$
\rho_L(\tilde{Q}) = \begin{pmatrix} 1 & -1 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & 1 & 1 \end{pmatrix},
\qquad
\rho_L(\tilde{R}) = \begin{pmatrix} 1 & 0 & -1 & 0 \\ 0 & 1 & 0 & 1 \\ 1 & 0 & 1 & 0 \\ 0 & -1 & 0 & 1 \end{pmatrix}.
$$

The product of the two matrices is the matrix of $\rho_L(\tilde{Q}\tilde{R})$, whose first column is $(1, 1, 1, 1)$ and which is reproduced by the multiplication rule. The reversed order gives $\rho_L(\tilde{R})\rho_L(\tilde{Q}) = \rho_L(\tilde{R}\tilde{Q})$, and the four-vector of $\tilde{R}\tilde{Q}$ is $(1, 1, 1, -1)$, read off the first column of $\rho_L(\tilde{R}\tilde{Q})$; the two orders therefore differ, exactly as $\tilde{Q}\tilde{R} \neq \tilde{R}\tilde{Q}$.

## The Right Regular Representation

**Definition.** The **right regular representation** of $\mathbb{B}$ is the map

$$
\rho_R : \mathbb{B} \longrightarrow \operatorname{End}_{\mathbb{C}}(\mathbb{B}), \qquad \rho_R(\tilde{Q})(\tilde{R}) = \tilde{R}\tilde{Q},
$$

the matrix of right multiplication in the basis $e_0, e_1, e_2, e_3$.

**Proposition (the right regular matrix).** In the basis $e_0, e_1, e_2, e_3$,

$$
\rho_R(\tilde{Q}) = \begin{pmatrix}
Q_0 & -Q_1 & -Q_2 & -Q_3 \\
Q_1 & Q_0 & Q_3 & -Q_2 \\
Q_2 & -Q_3 & Q_0 & Q_1 \\
Q_3 & Q_2 & -Q_1 & Q_0
\end{pmatrix}.
$$

**Proof.** The columns are the images $e_m \tilde{Q}$, and one expands as in the left case with the factors in the opposite order. Alternatively, since each $e_m$ is either $e_0$ or one of the $e_k$, and $e_k e_j = -e_j e_k$ for $j \neq k$, the matrix is the transpose of the left matrix conjugated by the fixed sign matrix of the next section, $\rho_R(\tilde{Q}) = D\,\rho_L(\tilde{Q})^{\mathsf T}D$, and direct computation of the four products confirms the display.

**Theorem (the right representation is an anti-homomorphism).** For all $\tilde{Q}, \tilde{R} \in \mathbb{B}$,

$$
\rho_R(\tilde{Q})\,\rho_R(\tilde{R}) = \rho_R(\tilde{R}\tilde{Q}).
$$

Hence $\rho_R$ is an algebra **anti**-homomorphism, and it is the regular representation of the opposite algebra $\mathbb{B}^{\mathrm{op}}$, not a second representation of $\mathbb{B}$.

**Proof.** For every $\tilde{S}$, associativity gives

$$
\rho_R(\tilde{Q})\bigl(\rho_R(\tilde{R})(\tilde{S})\bigr) = (\tilde{S}\tilde{R})\tilde{Q} = \tilde{S}(\tilde{R}\tilde{Q}) = \rho_R(\tilde{R}\tilde{Q})(\tilde{S}),
$$

which is the displayed identity. An anti-homomorphism is by definition a homomorphism from the opposite algebra, and the underlying linear map is the same.

**Remark (which side is which).** The left and right regular representations are the two actions of a non-commutative algebra on itself. Since quaternion conjugation is an anti-automorphism, the composite $\tilde{Q} \mapsto \rho_L(\tilde{Q}^{\natural})$ is an **anti**-homomorphism, that is, a homomorphism from $\mathbb{B}^{\mathrm{op}}$ into $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$; it is therefore the right regular representation up to a fixed change of basis, and the next section identifies that change of basis and shows that it is not the identity. The two representations differ as soon as the algebra is non-commutative.

## Transposition and the Two Representations

**Proposition (transposition is quaternion conjugation).** For every biquaternion $\tilde{Q}$,

$$
\rho_L(\tilde{Q})^{\mathsf{T}} = \rho_L(\tilde{Q}^{\natural}),
$$

where the transpose is taken in the basis $e_0, e_1, e_2, e_3$ fixed above.

**Proof.** Transposing the displayed closed form of $\rho_L(\tilde{Q})$ gives

$$
\rho_L(\tilde{Q})^{\mathsf{T}} = \begin{pmatrix}
Q_0 & Q_1 & Q_2 & Q_3 \\
-Q_1 & Q_0 & Q_3 & -Q_2 \\
-Q_2 & -Q_3 & Q_0 & Q_1 \\
-Q_3 & Q_2 & -Q_1 & Q_0
\end{pmatrix},
$$

and replacing $Q_k$ by $-Q_k$ in that same closed form reproduces this matrix.

**Remark (the false identity).** The right regular matrix is **not** the transpose of the left one:

$$
\rho_R(\tilde{Q}) \neq \rho_L(\tilde{Q})^{\mathsf{T}} \quad \text{in general}.
$$

For $\tilde{Q} = e_1$ the left matrix is $\rho_L(e_1) = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$, whose transpose is $\begin{pmatrix} 0 & 1 & 0 & 0 \\ -1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & -1 & 0 \end{pmatrix}$, while the right matrix is $\rho_R(e_1) = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & -1 & 0 \end{pmatrix}$: the two differ in the sign of the upper-left block. The proposition above gives the reason: the transpose is the left multiplication of the quaternion conjugate, $\rho_L(\tilde{Q})^{\mathsf{T}} = \rho_L(\tilde{Q}^{\natural})$, so it is a left multiplication and equals the right multiplication only on the centre. The variant that replaces $\tilde{Q}$ by $\tilde{Q}^{\natural}$ is not a second identity, since $\tilde{Q} \mapsto \tilde{Q}^{\natural}$ is a bijection of the algebra.

**Theorem (the correct relation).** Let $D = \operatorname{diag}(-1, 1, 1, 1)$, so that $D^2 = I$. Then for every biquaternion $\tilde{Q}$,

$$
\rho_R(\tilde{Q}) = D\,\rho_L(\tilde{Q})^{\mathsf{T}}\,D = D\,\rho_L(\tilde{Q}^{\natural})\,D .
$$

Hence the right representation is the contragredient of the left one up to the fixed change of basis $D$.

**Proof.** Apply $D$ on the left and on the right to the transpose of the closed form of $\rho_L(\tilde{Q})$. Left multiplication by $D$ negates the first row, and right multiplication by $D$ negates the first column; the corner entry lies in both and is negated twice, hence unchanged. The resulting matrix is the closed form of $\rho_R(\tilde{Q})$ displayed above. The second equality uses the transpose proposition.

**Corollary (the difference vanishes exactly on the centre).** The difference $\rho_L(\tilde{Q}) - \rho_R(\tilde{Q})$ is the zero matrix if and only if $\tilde{Q} \in \mathbb{C}_{\mathbb{B}} = \mathbb{C} e_0$.

**Proof.** If $\tilde{Q} = \lambda e_0$ then $\rho_L(\tilde{Q}) = \rho_R(\tilde{Q}) = \lambda I$, since scalar multiplication is central. Conversely, if the two matrices agree then $\tilde{Q}\tilde{R} = \tilde{R}\tilde{Q}$ for every $\tilde{R}$, so $\tilde{Q}$ lies in the centre, which is the scalar subspace by *Biquaternion 2×2 Matrix Element Representation*. Comparing the two closed forms directly, the entries in the three last rows and columns agree only when $Q_1 = Q_2 = Q_3 = 0$.

**Remark (what left and right mean).** The two representations differ **because the algebra is non-commutative**. The matrix $\rho_L(\tilde{Q}) - \rho_R(\tilde{Q})$ is the operator $\tilde{R} \mapsto \tilde{Q}\tilde{R} - \tilde{R}\tilde{Q}$ written in the basis, so its $m$-th column is the coordinate column of the commutator $[\tilde{Q}, e_m]$; the difference vanishes on $\mathbb{C}_{\mathbb{B}}$ and nowhere else. This is the sense in which the left and right regular representations of $\mathbb{B}$ are distinct, and the sense in which the row of *Biquaternion Four-Vector Element Representation* carries the right action and not a further left one.

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

**Theorem (the regular representation is $V \oplus V$).** In the basis

$$
\tilde\Pi_1, \quad e_1 \tilde\Pi_1, \quad \tilde\Pi_2, \quad e_1 \tilde\Pi_2
$$

of $\mathbb{B}$, the left regular matrix of $\tilde{Q}$ is block diagonal,

$$
\rho_L(\tilde{Q}) \sim \begin{pmatrix} A_+(\tilde{Q}) & 0 \\ 0 & A_-(\tilde{Q}) \end{pmatrix},
\qquad
A_+(\tilde{Q}) = \begin{pmatrix} Q_0 - iQ_3 & -Q_1 + iQ_2 \\ Q_1 + iQ_2 & Q_0 + iQ_3 \end{pmatrix},
$$

$$
A_-(\tilde{Q}) = \begin{pmatrix} Q_0 + iQ_3 & -Q_1 - iQ_2 \\ Q_1 - iQ_2 & Q_0 - iQ_3 \end{pmatrix},
$$

and each block has trace $2Q_0$ and determinant $N(\tilde{Q})$. Consequently each block is similar to the matrix $\Phi(\tilde{Q})$ of *Biquaternion 2×2 Matrix Element Representation*, each block is a copy of the simple module $V$, and

$$
\rho_L \cong V \oplus V
$$

as a left $\mathbb{B}$-module. The regular representation is therefore reducible, and it is the first reducible realization in this subcategory.

**Proof.** The two ideals $\mathbb{B}\tilde\Pi_1$ and $\mathbb{B}\tilde\Pi_2$ are stable under $\rho_L(\tilde{Q})$, because $\rho_L(\tilde{Q})(\tilde{S}\tilde\Pi_1) = (\tilde{Q}\tilde{S})\tilde\Pi_1$ for every $\tilde{S}$; hence the matrix is block diagonal in any basis adapted to the decomposition. The ideal $\mathbb{B}\tilde\Pi_1$ has the basis $\tilde\Pi_1, e_1\tilde\Pi_1$, since $e_2 \tilde\Pi_1 = i e_1 \tilde\Pi_1$ and $e_3 \tilde\Pi_1 = -i\tilde\Pi_1$. Its multiplication by the basis elements is read from

$$
e_1 \tilde\Pi_1 = e_1\tilde\Pi_1, \quad e_2 \tilde\Pi_1 = ie_1\tilde\Pi_1, \quad e_3 \tilde\Pi_1 = -i\tilde\Pi_1, \qquad e_1(e_1\tilde\Pi_1) = -\tilde\Pi_1, \quad e_2(e_1\tilde\Pi_1) = i\tilde\Pi_1, \quad e_3(e_1\tilde\Pi_1) = ie_1\tilde\Pi_1,
$$

so in the basis $\tilde\Pi_1, e_1\tilde\Pi_1$ the three units act by the matrices
$\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$,
$\begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}$ and
$\begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix}$, and carrying out the sum $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ gives the displayed block $A_+$; the same computation on the basis $\tilde\Pi_2, e_1\tilde\Pi_2$ of $\mathbb{B}\tilde\Pi_2$ gives $A_-$. The trace of each block is $2Q_0$ by inspection and the determinant is computed as in the matrix realization,

$$
\det A_+ = (Q_0 - iQ_3)(Q_0 + iQ_3) - (-Q_1 + iQ_2)(Q_1 + iQ_2) = N(\tilde{Q}),
$$

and likewise $\det A_- = N(\tilde{Q})$. The similarity is then exhibited by an explicit change of basis. With

$$
u_+ = e_0 + e_3, \qquad u_- = e_1 + e_2,
$$

and hence

$$
\Phi(u_+) = \begin{pmatrix} 1-i & 0 \\ 0 & 1+i \end{pmatrix}, \qquad \Phi(u_-) = \begin{pmatrix} 0 & -1-i \\ 1-i & 0 \end{pmatrix},
$$

one has

$$
A_+(\tilde{Q}) = \Phi(u_+)\,\Phi(\tilde{Q})\,\Phi(u_+)^{-1}, \qquad A_-(\tilde{Q}) = \Phi(u_-)\,\Phi(\tilde{Q})\,\Phi(u_-)^{-1}
$$

for every $\tilde{Q}$: both sides are $\mathbb{C}$-linear in $\tilde{Q}$, so it suffices to compare them on the four basis elements $e_0, e_1, e_2, e_3$, where the two displayed formulas agree elementwise. Both conjugating matrices are invertible, since $\det\Phi(u_+) = (1-i)(1+i) = 2 = \det\Phi(u_-)$, and consequently each block is similar to $\Phi(\tilde{Q})$ for every $\tilde{Q}$, including the elements whose vector part is nonzero while $Q_1^2 + Q_2^2 + Q_3^2 = 0$ and the block has a repeated eigenvalue. Both blocks therefore have the characteristic polynomial $\lambda^2 - 2Q_0\lambda + N(\tilde{Q})$ of $\Phi(\tilde{Q})$, as the similarity requires, and each realizes the simple module $V$ of *Biquaternion 2×2 Matrix Element Representation*; the regular module is $V \oplus V$.

**Remark (the characteristic polynomial).** In the block basis of the theorem above the regular matrix is block diagonal with the two blocks $A_+$ and $A_-$, each similar to $\Phi(\tilde{Q})$, so its characteristic polynomial is the square of that of the simple module,

$$
\chi_{\rho_L(\tilde{Q})}(\lambda) = \bigl( \lambda^2 - 2Q_0\lambda + N(\tilde{Q}) \bigr)^2,
$$

which the block form of the theorem above gives at once. The eigenvalues themselves, the Cayley–Hamilton identity, the eigenspace dimensions and the doubling of the multiplicities that the square produces are the subject of *Biquaternion Spectral Theory*, later in this chapter, and are cited from there rather than developed here.

**Remark (the irreducible submodules are the minimal left ideals).** The two blocks are the two minimal left ideals $I_1 = \mathbb{B}\tilde\Pi_1$ and $I_2 = \mathbb{B}\tilde\Pi_2$ of the algebra. Both are isomorphic to the module $V$ of *Biquaternion 2×2 Matrix Element Representation*, and the fact that $V$ is the only simple module is the classification of the simple modules. The decomposition $\mathbb{B} = I_1 \oplus I_2$ is therefore the same fact as the two-block form of the regular matrix, read as ideals rather than as a matrix; the same decomposition is stated in *Modules over the Biquaternion Algebra*, where the simple module is written $S$, as $\mathbb{B} \cong S \oplus S$.

## The Determinant and the Trace

**Corollary (determinant and trace).** For every biquaternion $\tilde{Q}$,

$$
\det \rho_L(\tilde{Q}) = N(\tilde{Q})^2, \qquad \operatorname{Tr} \rho_L(\tilde{Q}) = 4Q_0 .
$$

The determinant of the regular matrix is the **square** of the biquaternion norm, and it is not the biquaternion norm.

**Proof.** In the block basis of the preceding theorem the matrix is block diagonal with the two blocks $A_+$ and $A_-$, so the determinant is the product $\det A_+ \det A_- = N(\tilde{Q}) \cdot N(\tilde{Q}) = N(\tilde{Q})^2$, and the trace is the sum $\operatorname{Tr} A_+ + \operatorname{Tr} A_- = 2Q_0 + 2Q_0 = 4Q_0$. Both quantities are unchanged by the change of basis.

**Example.** For $\tilde{Q} = (2+i)e_0 + (1-i)e_1 + 3e_2 + ie_3$ one has $N(\tilde{Q}) = 11 + 2i$ and

$$
\det \rho_L(\tilde{Q}) = (11+2i)^2 = 117 + 44i, \qquad \operatorname{Tr}\rho_L(\tilde{Q}) = 4(2+i) = 8 + 4i,
$$

in agreement with the two blocks $A_+(\tilde{Q}) = \begin{pmatrix} 3+i & -1+4i \\ 1+2i & 1+i \end{pmatrix}$ and $A_-(\tilde{Q}) = \begin{pmatrix} 1+i & -1-2i \\ 1-4i & 3+i \end{pmatrix}$ on this element, each of trace $4+2i$ and determinant $11+2i$.

**Remark (the determinant is not the biquaternion norm).** The determinant of the regular matrix is $N^2$, and the difference from $N$ is a genuine feature of the regular representation and not a notational slip. The simple module carries the biquaternion norm as its determinant, $\det\Phi(\tilde{Q}) = N(\tilde{Q})$, and the regular module is the direct sum of two copies of it, so its determinant is the product of two biquaternion norms. The square appears because the regular representation acts on a space of dimension twice that of the simple module; it is the algebraic shadow of the factor $2$ between the two dimensions.

## The Double Centralizer

**Theorem (the centralizer is the right copy).** The algebra of endomorphisms of the left regular module is the image of the right regular representation,

$$
\operatorname{End}_{\mathbb{B}}(\mathbb{B}) = \rho_R(\mathbb{B}),
$$

and consequently the centralizer of $\rho_L(\mathbb{B})$ in $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ is $\rho_R(\mathbb{B})$, of complex dimension $4$.

**Proof.** An endomorphism $f$ of the left module $\mathbb{B}$ is determined by $f(e_0)$, since $f(\tilde{R}) = f(\tilde{R}e_0) = \tilde{R}f(e_0)$ for every $\tilde{R}$; writing $\tilde{Q} = f(e_0)$ gives $f(\tilde{R}) = \tilde{R}\tilde{Q} = \rho_R(\tilde{Q})(\tilde{R})$, so $f = \rho_R(\tilde{Q})$ and the endomorphisms are exactly the right multiplications. Conversely every $\rho_R(\tilde{Q})$ is a module endomorphism, because right and left multiplication associate. For the centralizer, a matrix commuting with $\rho_L(\tilde{R})$ for every $\tilde{R}$ is exactly an element of $\operatorname{End}_{\mathbb{B}}(\mathbb{B})$, which is $\rho_R(\mathbb{B})$. The right copy has complex dimension $4$ because $\rho_R$ is injective: $\rho_R(\tilde{Q}) = 0$ forces $\tilde{Q} = \rho_R(\tilde{Q})(e_0) = 0$.

**Remark.** The theorem is the regular-module case of the double centralizer phenomenon, and it mirrors the statement $\mathbb{B} = \operatorname{End}_{\mathbb{C}}(V)$ of *Modules over the Biquaternion Algebra*: the algebra is recovered as the centralizer of the opposite copy acting on itself. The two copies commute and together generate the full matrix algebra $\operatorname{End}_{\mathbb{C}}(\mathbb{B}) \cong M_4(\mathbb{C})$.

## The Real Form

**Proposition (the real regular representation).** Regarded over $\mathbb{R}$ in the real basis

$$
e_0, e_1, e_2, e_3, i e_0, i e_1, i e_2, i e_3,
$$

of the eight-dimensional real space underlying $\mathbb{B}$, the left regular representation is an $8 \times 8$ real matrix $\rho_L^{\mathbb{R}}(\tilde{Q})$, with

$$
\det \rho_L^{\mathbb{R}}(\tilde{Q}) = |N(\tilde{Q})|^4, \qquad \operatorname{Tr}\rho_L^{\mathbb{R}}(\tilde{Q}) = 8 \operatorname{Re}(Q_0).
$$

**Proof.** The real matrix is the realification of the complex-linear endomorphism $\rho_L(\tilde{Q})$ of the four-dimensional complex space $\mathbb{B}$. A complex-linear endomorphism with eigenvalues $\lambda_1, \ldots, \lambda_4$ has realification with eigenvalues $\lambda_1, \bar\lambda_1, \ldots, \lambda_4, \bar\lambda_4$, so its determinant is $|\lambda_1 \cdots \lambda_4|^2 = |\det \rho_L(\tilde{Q})|^2 = |N(\tilde{Q})^2|^2 = |N(\tilde{Q})|^4$, and its trace is $2\operatorname{Re}(\lambda_1 + \cdots + \lambda_4) = 2\operatorname{Re}(4Q_0) = 8\operatorname{Re}(Q_0)$.

**Remark (why the dimension doubles).** The real dimension doubles because $\mathbb{B}$ is a complex vector space and is regarded as a real vector space by restriction of scalars: the correspondence $\operatorname{Res}_{\mathbb{C}/\mathbb{R}} \mathbb{C}^4 = \mathbb{R}^8$ replaces each complex coordinate by its real and imaginary parts. The same doubling applies to the module $V$ of *Biquaternion 2×2 Matrix Element Representation*, whose realification $S$ has real dimension $4$, so over $\mathbb{R}$ the regular representation is $\rho_L^{\mathbb{R}} \cong \operatorname{Res}_{\mathbb{C}/\mathbb{R}}(V \oplus V)$, and the block decomposition of the complex case survives with each block doubled in size. Restricted to the real subalgebra $\mathbb{H}_{\mathbb{B}}$, and read on $\mathbb{H}_{\mathbb{B}}$ itself, the same construction is the $4 \times 4$ real regular representation of the quaternions, which is the subject of *Quaternion Element Representations*; complexifying the algebra doubles both its real dimension and the size of the regular matrix.

## A Second $4 \times 4$ Realization, and the Modulus-Squared Map

The regular matrix is not the only $4 \times 4$ realization of $\mathbb{B}$ in use, and the second one worth recording comes from a question with no algebra in it: the eigenvectors of a parameterised family of matrices. Its shape is different enough that the difference is instructive, and the object it is built for — a multiplicative quadratic map into the real matrices, with no counterpart in the regular realization — is the reason for recording it here rather than in a dedicated article.

**The realization.** In the basis $e_0, x, y, z$ with $x = ie_1$, $y = ie_2$, $z = ie_3$, so that

$$
x^2 = y^2 = z^2 = e_0, \qquad xy = iz, \qquad yz = ix, \qquad zx = iy ,
$$

the map on complex coefficients

$$
\Phi'(A_0, A_1, A_2, A_3) = \begin{pmatrix} A_0 & A_1 & A_2 & A_3 \\ A_1 & A_0 & -iA_3 & iA_2 \\ A_2 & iA_3 & A_0 & -iA_1 \\ A_3 & -iA_2 & iA_1 & A_0 \end{pmatrix}
$$

is a representation of $\mathbb{B}$. Its first row and column coincide, since $\Phi'$ is symmetric in the coefficients, which the Cayley matrix above is not; the price is the scalar imaginary scattered through the lower block. The change of basis is what makes the squares $+e_0$: the generators of this realization are the elements $ie_k$, not the $e_k$, and the difference is a change of orientation, the two choices being interchanged by the coefficient conjugation, not two different algebras.

**The realization is equivalent to the regular one.** Both are faithful four-dimensional linear realizations of $\mathbb{B} \cong M_2(\mathbb{C})$, and by the module structure of the section above every such realization is two copies of the simple module, $V \oplus V$; so an invertible intertwining matrix exists, and one was exhibited and checked on $100$ random elements, with maximum residual $1.9 \times 10^{-15}$. Nothing in the representation theory of the two distinguishes them, and everything the corpus says about $\rho_L$ as a module carries over.

**What the realization brings.** Each of $x, y, z$ is skew-symmetric for the Minkowski form of the real-form section, $M^{\mathsf{T}} = -DMD$ with $D = \operatorname{diag}(-1,1,1,1)$, and the products of the basis elements give a second Hermitian basis of $M_4(\mathbb{C})$: the sixteen matrices

$$
I,\; xX,\; yY,\; zZ,\quad x,\; X,\; yZ,\; zY,\quad y,\; Y,\; xZ,\; zX,\quad z,\; Z,\; xY,\; yX ,
$$

with $X, Y, Z$ the coefficient conjugates of $x, y, z$, each squaring to $I$ and each Hermitian, so that real linear combinations of them are exactly the Hermitian $4 \times 4$ matrices; every one but $I$ is traceless. This was checked entry by entry. The same basis contains generators of the complex Clifford algebra $\mathbb{C}\ell(4)$, namely $x, y, zX, zY$, which anticommute pairwise to $\delta_{ij}I$ up to the conventional factor, so the realization also places $\mathbb{B}$ inside $M_4(\mathbb{C})$ in the Clifford manner of *Biquaternion Other Algebraic Element Representations*.

**The transposition identity is exact in this basis, and these are the matrices of the Maxwell literature.** The realization is the one in which the two $D$'s of the theorem of the transposition section disappear, and this is worth stating because it separates two things that the first basis runs together. Write the left regular matrix of the element $\tilde{Q} = A_0 e_0 + A_1 x + A_2 y + A_3 z$ as

$$
\rho_L(\tilde{Q}) = A_0 I + cF(\mathbf{A}), \qquad
cF(\mathbf{A}) := \begin{pmatrix} 0 & \mathbf{A}^{\mathsf{T}} \\ \mathbf{A} & i[\mathbf{A}]_\times \end{pmatrix}, \qquad \mathbf{A} = (A_1, A_2, A_3),
$$

with $[\mathbf{u}]_\times$ the matrix of $\mathbf{v} \mapsto \mathbf{u} \times \mathbf{v}$; this is $\Phi'$ of the display above, and it is the same $cF$ that a matrix formulation of Maxwell's equations multiplies into the operator column $(-\partial_t, \nabla)^{\mathsf{T}}$. In this basis the right regular matrix is **exactly the transpose**,

$$
\rho_R(\tilde{Q}) = \rho_L(\tilde{Q})^{\mathsf{T}} ,
$$

with no sign matrix, where in the basis $e_0, e_1, e_2, e_3$ of the transposition section the relation read $\rho_R = D\rho_L^{\mathsf{T}}D$ instead. Both were recomputed over $100$ random elements, the first to $0$ and the second to $0$, and the change of basis between the two conventions was checked explicitly too: with $C = \operatorname{diag}(1, -i, -i, -i)$ carrying the coefficients of the corpus basis into those of this one, $C\rho_L(\tilde{Q})C^{-1}$ and $C\rho_R(\tilde{Q})C^{-1}$ are the two matrices displayed here, at residual $0$. So the *false identity* remark of the transposition section is a statement about a basis and not about the algebra: in the basis whose vector units square to $-e_0$ the transpose of the left matrix is a left multiplication of the conjugate, while in the basis whose vector units square to $+e_0$ it is the right multiplication, exactly, and the two $D$'s are the price of the first basis. The sixteen-matrix basis above is the same object read on the other side: as matrices it is $I$, the three $cF(\mathbf{e}_i)$, their complex conjugates and the pairwise products $cF(\mathbf{e}_i)(cF(\mathbf{e}_j))^{\natural}$, which are Hermitian and involutive with square $I$, traceless except for $I$, and orthogonal for the trace form $\operatorname{tr}(M_kM_l) = 4\delta_{kl}$ — all checked exactly — and the three $cF(\mathbf{e}_i)$ anticommute pairwise with $cF(\mathbf{e}_1)cF(\mathbf{e}_2) = i\,cF(\mathbf{e}_3)$.

**The modulus-squared map.** The object the realization is built for is

$$
m(A) = A A^{\natural}, \qquad A \in I + \mathbb{B},
$$

the **modulus-squared map**, named after the complex absolute value. Its image consists of real matrices, $m$ is multiplicative, $m(AB) = m(A)m(B)$, and it is a two-to-one map on the unit sphere. The reality is the point: for the matrices of the realization, $A^{\natural}$ commutes with $A$, so the product is real, and the read-off of the map is a quadratic map with no complex-linear analogue. The source's account of the images is as follows, and is recorded as the source's: the image of the unit $7$-sphere is the complex projective space $\mathbb{C}P^3$, the image of the unit real quaternions is $SO(3)$ with its two-to-one covering, the image of the unit-norm biquaternions is the proper Lorentz group $SO^+(1,3)$ — the same group that the two-sided action of the next section reaches by another route — and the image of the traceless part is read as the electromagnetic energy-momentum tensors, whose corpus home is *Exercise: The Electromagnetic Energy–Momentum Tensor*. The corpus's own checks confirm the three properties used in the sentence — reality, multiplicativity and orthogonality of the image of a unit real quaternion, at $4.4\times10^{-16}$, $4.3\times10^{-14}$ and $8.9\times10^{-16}$ over $100$ random elements — and nothing beyond them; the images are the source's and are not adopted.

What the corpus takes from the map is the existence of a *multiplicative* quadratic real form of this kind at all, next to the one it already owns: the operator of *Biquaternion 4×4 Regular Matrix Operator Representation* is the quadratic map of the same algebra that is **not** multiplicative, being a congruence rather than a product, and the two together show that the algebra carries a quadratic form of each type.

## The Sixteen Products and the Biparavectors

The double centralizer of the earlier section says that the left and the right copies commute and that together they generate the whole endomorphism algebra. The basis that exhibits this is the set of products, and in the second realization it can be taken Hermitian.

**The products.** For the coordinate units put

$$
P_{ij} := \rho_L(e_i)\,\rho_R(e_j), \qquad i, j \in \{0, 1, 2, 3\}.
$$

In the second realization the right regular matrix is the transpose of the left, so $P_{ij}$ is the ordinary matrix product $\rho_L(e_i)\rho_L(e_j)^{\mathsf T}$; writing $X_i := \rho_L(e_i)$ for $i = 1, 2, 3$ and $X_0 = I$,

$$
P_{ij} = X_i X_j^{\mathsf T}.
$$

The three units satisfy $X_k^2 = I$ and anticommute pairwise, and their product is the complex structure of the realization, $X_1X_2 = iX_3$; the matrices $X_k$ are Hermitian, so $X_j^{\mathsf T}$ is its complex conjugate.

**Proposition (the sixteen products are an orthogonal basis).** The matrices $X_iX_j^{\mathsf T}$ are Hermitian, linearly independent over $\mathbb{C}$, and orthogonal for the trace form, with a common normalisation:

$$
\operatorname{tr}\!\left(X_i X_j^{\mathsf T}\, X_k X_l^{\mathsf T}\right) = 4\,\delta_{ik}\delta_{jl}.
$$

This was checked entry by entry: the diagonal value is $4$ for each of the sixteen and every off-diagonal value is $0$. Independence follows, and the sixteen are a basis of $\mathbb{M}_4(\mathbb{C})$.

**The expansion.** By the orthogonality every complex matrix $M$ has the expansion

$$
M = \sum_{i,j} a_{ij}\,X_iX_j^{\mathsf T}, \qquad a_{ij} = \tfrac14\operatorname{tr}\!\left(M\,X_iX_j^{\mathsf T}\right),
$$

the coefficients being read off one at a time. Recomputing the expansion on a random complex $4 \times 4$ matrix returns it to $5 \times 10^{-16}$.

**Reading the expansion in the algebra.** The tensor square $\mathbb{B} \otimes_{\mathbb{C}} \mathbb{B}$ is spanned by the sixteen $e_i \otimes e_j$, and the expansion says that this space maps onto the endomorphisms of $\mathbb{B}$: the element $\sum a_{ij}\,e_i \otimes e_j$ is the linear transformation

$$
\tilde X \longmapsto \sum_{i,j} a_{ij}\, e_i \tilde X e_j,
$$

and every complex-linear transformation of the algebra arises this way. Such an element is a **biparavector** in the language of the paravector formulation. That the sixteen products already span the endomorphisms is the concrete form of the double centralizer: the left copy supplies the first index and the right copy the second, and the two fill $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ between them. Recomputing the action of the biparavector of a left–right sandwich $\tilde X \mapsto \tilde A\tilde X\tilde B$ against the sandwich itself returns $1.5 \times 10^{-14}$.

**Where the uniform normalisation comes from.** The constant $4$ in the trace relation is a property of the second realization and not of the regular basis. In the basis $e_0, e_1, e_2, e_3$ of the earlier sections the Gram matrix of the sixteen products is still diagonal, but its diagonal entries are $\pm 4$ rather than $4$, so the coefficient formula there carries the sign of $\operatorname{tr}(P_{ij}^2)$; it is the Hermitian realisation that makes the coefficients uniform. The Hermitian form of the basis and the tensor-square reading are the same objects as the sixteen matrices listed by the realization above, read as outer products rather than as products of the two units.

## The Two-Sided Action

One geometric statement can be made with what the regular representation supplies, and it uses both the left and the right copies at once.

**Definition.** The **unit-norm group** of $\mathbb{B}$ is

$$
\tilde{G} = \{ \tilde{A} \in \mathbb{B} : N(\tilde{A}) = 1 \}.
$$

It is a group, and under the isomorphism $\Phi$ of *Biquaternion 2×2 Matrix Element Representation* it is the special linear group $SL_2(\mathbb{C})$, since $N(\tilde{A}) = \det\Phi(\tilde{A})$.

**Proposition (the two-sided action).** The map

$$
\tilde{G} \times \mathbb{M}_+ \longrightarrow \mathbb{M}_+, \qquad (\tilde{A}, \tilde{Q}) \longmapsto \tilde{A} \tilde{Q} \tilde{A}^{*},
$$

is a group action of $\tilde{G}$ on the real vector space $\mathbb{M}_+$ of real dimension $4$, and it preserves the biquaternion norm restricted to $\mathbb{M}_+$:

$$
N(\tilde{A}\tilde{Q}\tilde{A}^{*}) = N(\tilde{Q}) .
$$

**Proof.** If $\tilde{Q}$ is Hermitian then $(\tilde{A}\tilde{Q}\tilde{A}^{*})^{\dagger} = \tilde{A}\tilde{Q}^{*}\tilde{A}^{*} = \tilde{A}\tilde{Q}\tilde{A}^{*}$, so $\mathbb{M}_+$ is preserved. The biquaternion norm is multiplicative, $N(\tilde{A}\tilde{Q}\tilde{A}^{*}) = N(\tilde{A})N(\tilde{Q})N(\tilde{A}^{*})$, and $N(\tilde{A}) = 1$ while $N(\tilde{A}^{*}) = N(\tilde{A})^{*} = 1$. Composition holds because $\tilde{A}_1(\tilde{A}_2\tilde{Q}\tilde{A}_2^{*})\tilde{A}_1^{*} = (\tilde{A}_1\tilde{A}_2)\tilde{Q}(\tilde{A}_1\tilde{A}_2)^{\dagger}$.

**Theorem (the double cover).** The action above defines a surjective group homomorphism

$$
\tilde{G} = SL_2(\mathbb{C}) \longrightarrow SO^+(1,3),
$$

onto the identity component $SO^+(1,3)$ of the orthogonal group of the form, with kernel $\{e_0, -e_0\}$, which is central of order two.

**Proof.** A real-linear map of $\mathbb{M}_+$ preserving the quadratic form of signature $(1,3)$ is an element of $O(1,3)$; the action is continuous in $\tilde{A}$ and $\tilde{G} = SL_2(\mathbb{C})$ is connected, so the image is a connected subgroup of $O(1,3)$ and therefore lies in the identity component $SO^+(1,3)$. The surjectivity onto that component is the standard fact that $SL_2(\mathbb{C})$ is the double cover of the restricted orthogonal group, cited from the standard theory of the orthogonal groups. For the kernel, $\tilde{A}$ acts trivially precisely when $\tilde{A}\tilde{Q}\tilde{A}^{*} = \tilde{Q}$ for every Hermitian $\tilde{Q}$. Taking $\tilde{Q} = e_0$ gives $\tilde{A}\tilde{A}^{*} = e_0$, that is, $\tilde{A}$ is unitary, and the condition then reads $\tilde{A}\tilde{Q} = \tilde{Q}\tilde{A}$ for every Hermitian $\tilde{Q}$. The Hermitian elements span $\mathbb{B}$ over $\mathbb{C}$, so $\tilde{A}$ commutes with every element of $\mathbb{B}$ and is therefore a central element $\lambda e_0$; the biquaternion norm condition $N(\lambda e_0) = \lambda^2 = 1$ leaves $\lambda = \pm 1$. Both central elements act trivially on $\mathbb{M}_+$, and no other element does. The same double cover is met in *Biquaternion Spin Geometry*, where it is read on the module; here it is read as the two-sided action of the regular representation, that is, as the left copy composed with the right copy of the conjugate transpose.

**Remark.** The statement above is a statement of algebra and of the geometry of a quadratic form: a group of linear transformations of a four-dimensional real space preserving a form of signature $(1,3)$, and a two-to-one homomorphism onto it. It is not a statement about a physical particle, and no vocabulary of physics is used. The two-sided action is the regular representation read twice, once through $\rho_L(\tilde{A})$ and once through the right action of $\tilde{A}^{*}$; it is the one place in this article where the left and right copies enter together.

## Summary

The left regular representation $\rho_L(\tilde{Q})(\tilde{R}) = \tilde{Q}\tilde{R}$ is the algebra acting on itself on the left, and in the basis $e_0, e_1, e_2, e_3$ its matrix is the Cayley matrix of quaternion multiplication, each entry of which is a single coefficient of $\tilde{Q}$ carrying a sign and none of which is a sum of coefficients. It is a homomorphism, its transpose is the left matrix of the quaternion conjugate, $\rho_L(\tilde{Q})^{\mathsf{T}} = \rho_L(\tilde{Q}^{\natural})$, its determinant is the square of the biquaternion norm, $\det\rho_L(\tilde{Q}) = N(\tilde{Q})^2$, and its trace is $4Q_0$.

The right regular representation $\rho_R(\tilde{Q})(\tilde{R}) = \tilde{R}\tilde{Q}$ is an anti-homomorphism and the regular representation of the opposite algebra. The naive identity $\rho_R(\tilde{Q}) = \rho_L(\tilde{Q})^{\mathsf{T}}$ is false — and the variant with $\tilde{Q}^{\natural}$ is the same statement, since $\rho_L(\tilde{Q}^{\natural})^{\mathsf{T}} = \rho_L(\tilde{Q})$ — while what holds is $\rho_R(\tilde{Q}) = D\rho_L(\tilde{Q})^{\mathsf{T}}D = D\rho_L(\tilde{Q}^{\natural})D$ with $D = \operatorname{diag}(-1,1,1,1)$. The difference $\rho_L - \rho_R$ vanishes exactly on the centre $\mathbb{C}_{\mathbb{B}}$, which is the precise sense in which left and right differ because the algebra is non-commutative.

The regular module is $\mathbb{B} = I_1 \oplus I_2$ with $I_1 = \mathbb{B}\tilde\Pi_1$, $I_2 = \mathbb{B}\tilde\Pi_2$ and $\tilde\Pi_1 = \tfrac{1}{2}(e_0 + ie_3)$, $\tilde\Pi_2 = \tfrac12(e_0 - ie_3)$; in the adapted basis $\tilde\Pi_1, e_1\tilde\Pi_1, \tilde\Pi_2, e_1\tilde\Pi_2$ the regular matrix is block diagonal with the two blocks $A_+$, $A_-$, each similar to $\Phi(\tilde{Q})$ and each a copy of the simple module $V$. So $\rho_L \cong V \oplus V$, the regular representation is reducible, and it is the first reducible realization of this subcategory. The centralizer of $\rho_L(\mathbb{B})$ is $\rho_R(\mathbb{B})$, the right copy, of complex dimension $4$. Over $\mathbb{R}$ the regular representation is $8 \times 8$ real with $\det = |N|^4$ and trace $8\operatorname{Re}(Q_0)$, the dimension doubling by restriction of scalars. The two-sided action of the unit-norm group on $\mathbb{M}_+$ preserves the biquaternion norm and gives a two-to-one homomorphism $SL_2(\mathbb{C}) \to SO^+(1,3)$ with kernel $\{\pm e_0\}$.

A second $4 \times 4$ realization, the one used in the literature on eigenvector bundles, is equivalent to $\rho_L$ as a module — every faithful four-dimensional complex realization is $V \oplus V$ — and it carries a multiplicative quadratic map $m(A) = A A^{\natural}$ to the real matrices which the regular realization does not have, in contrast with the congruence-shaped quadratic operator of *Biquaternion 4×4 Regular Matrix Operator Representation*. In that realization the sixteen products $\rho_L(e_i)\rho_R(e_j)$ are the Hermitian outer products $X_iX_j^{\mathsf T}$ and form an orthogonal basis of $\mathbb{M}_4(\mathbb{C})$ for the trace form, $\operatorname{tr}(P_{ij}P_{kl}) = 4\delta_{ik}\delta_{jl}$; the expansion it gives is the tensor-square reading of the double centralizer, and it says that every complex-linear transformation of the algebra is a biparavector, the two-sided multiplication $\tilde X \mapsto \sum a_{ij}\,e_i\tilde X e_j$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | Biquaternion algebra |
| $e_0, e_1, e_2, e_3$ | Algebra basis, $e_0 = 1$, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ | Developed form, $Q_\mu \in \mathbb{C}$ |
| $Q^\mu = (Q^0, Q^1, Q^2, Q^3)$ | Four-vector; $Q^0 = Q_0$, $(Q^1, Q^2, Q^3) = (Q_1, Q_2, Q_3)$ |
| $\rho_L(\tilde{Q})$ | Matrix of left multiplication, the Cayley matrix |
| $\rho_R(\tilde{Q})$ | Matrix of right multiplication |
| $D = \operatorname{diag}(-1,1,1,1)$ | Fixed sign matrix, $\rho_R(\tilde{Q}) = D\rho_L(\tilde{Q})^{\mathsf{T}}D$ |
| $N(\tilde{Q}) = \sum_\mu Q_\mu^2$ | Biquaternion norm; $\det\rho_L(\tilde{Q}) = N(\tilde{Q})^2$ |
| ${}^{\natural}, \bar{\cdot}, {}^{*}, {}^{\flat}$ | Quaternion, complex, Hermitian and anti-Hermitian conjugations |
| $\mathbb{C}_{\mathbb{B}}$ | Centre, the scalar subspace $\mathbb{C} e_0$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real quaternion subalgebra; its restriction carries the quaternion regular representation of *Quaternion Element Representations* |
| $\tilde\Pi_1 = \tfrac{1}{2}(e_0 + ie_3)$, $\tilde\Pi_2 = \tfrac12(e_0 - ie_3)$ | Orthogonal idempotents, $\tilde\Pi_1 + \tilde\Pi_2 = e_0$, $\tilde\Pi_1\tilde\Pi_2 = 0$ |
| $I_1 = \mathbb{B}\tilde\Pi_1$, $I_2 = \mathbb{B}\tilde\Pi_2$ | The two minimal left ideals, $\mathbb{B} = I_1 \oplus I_2$ |
| $A_+(\tilde{Q}), A_-(\tilde{Q})$ | The two $2 \times 2$ blocks of $\rho_L$ in the adapted basis |
| $u_+ = e_0 + e_3$, $u_- = e_1 + e_2$ | Conjugating elements, $A_\pm(\tilde{Q}) = \Phi(u_\pm)\Phi(\tilde{Q})\Phi(u_\pm)^{-1}$ |
| $V = \mathbb{C}^2$ | Simple left $\mathbb{B}$-module, complex dimension $2$ |
| $\mathbb{B}^{\mathrm{op}}$ | Opposite algebra; $\rho_R$ is a homomorphism from it |
| $\epsilon^{ijk}$ | Levi-Civita symbol on the indices $1, 2, 3$ |
| $\Phi(\tilde{Q})$ | Matrix realization of *Biquaternion 2×2 Matrix Element Representation* |
| $\operatorname{Res}_{\mathbb{C}/\mathbb{R}}$ | Restriction of scalars |
| $\operatorname{End}_{\mathbb{B}}(\mathbb{B}) = \rho_R(\mathbb{B})$ | Endomorphism algebra of the regular module |
| $\rho_L^{\mathbb{R}}(\tilde{Q})$ | Real $8 \times 8$ regular matrix |
| $\Phi'(A_0, A_1, A_2, A_3)$ | Second $4 \times 4$ realization, on the generators $x = ie_1$, $y = ie_2$, $z = ie_3$ with $x^2 = y^2 = z^2 = e_0$ |
| $X, Y, Z$ | Coefficient conjugates of $x, y, z$, used in the Hermitian basis of that realization |
| $m(A) = A A^{\natural}$ | Modulus-squared map, $I + \mathbb{B} \to M_4(\mathbb{R})$; multiplicative, two-to-one on the unit sphere |
| $P_{ij} = \rho_L(e_i)\rho_R(e_j) = X_iX_j^{\mathsf T}$ | The sixteen products; an orthogonal basis of $\mathbb{M}_4(\mathbb{C})$, $\operatorname{tr}(P_{ij}P_{kl}) = 4\delta_{ik}\delta_{jl}$ |
| $\sum a_{ij}\,e_i \otimes e_j$ | Biparavector, the two-sided transformation $\tilde X \mapsto \sum a_{ij}\,e_i\tilde X e_j$ |
| $\tilde{G} = \{\tilde{A} : N(\tilde{A}) = 1\}$ | Unit-norm group, $\cong SL_2(\mathbb{C})$ |
| $\mathbb{M}_+$ | Hermitian subspace of real dimension $4$ |
| $SO^+(1,3)$ | Identity component of the orthogonal group of signature $(1,3)$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the regular representation of an algebra and the identification of its endomorphism algebra.
- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Interscience, 1962), for the regular module, its decomposition into minimal left ideals and the double centralizer theorem.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules*, 2nd edition (Springer, 1992), for the regular module as a left module over itself and the centralizer of the left copy.
- William Fulton and Joe Harris, *Representation Theory: A First Course*, Graduate Texts in Mathematics 129 (Springer, 1991), for the regular representation as the direct sum of the simple modules with multiplicity equal to their dimensions.
- John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288 (Springer, 2021), for the regular representation of a quaternion algebra and its complexification.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the Cayley matrix of quaternion multiplication and its transpose.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd edition (Springer, 2015), for the double cover $SL_2(\mathbb{C}) \to SO^+(1,3)$ and the two-to-one homomorphism onto the orthogonal group of a form.
- D. H. Gottlieb, "Eigenbundles, Quaternions, and Berry's Phase," arXiv:math/0304281 [math.AT] (2003), for the second $4 \times 4$ realization and the modulus-squared map of the section above; the paper's $4 \times 4$ matrices are Example 5 and the map $m(A) = A A^{\natural}$ is its section 5.
- D. H. Gottlieb, "Maxwell's equations" (1 August 2004, 12 pp.), for the matrix formulation of Maxwell's equations in which the field matrix is $A_0 I + cF$ of the realization above, the dual form in which the operators stand in the matrix and the field in the column, and the identity $\rho_R = \rho_L^{\mathsf{T}}$ which holds there without a sign matrix; cited for the identification of the second realization with the matrices of the Maxwell literature and for the transposition remark of that section. Its section 5 is the source of the sixteen-product basis and the biparavectors of the section above: the coefficient formula $a_{ij} = \tfrac14\operatorname{tr}(MX_iX_j^{\mathsf{T}})$, the orthogonality of the basis for the trace form, and the reading of the products as the tensor square of the algebra acting on itself on both sides. The paper's potential-level equations (13) and (14) are recorded in *Maxwell's Equations in Biquaternionic Form* with their vector parts corrected.
