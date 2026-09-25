
# __Biquaternion 4×4 Regular Matrix Representation__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is the four-dimensional complex algebra with basis $e_0 = 1, e_1, e_2, e_3$, where $e_k^2 = -e_0$ and $e_j e_k = -e_k e_j$ for $j \neq k$, and with a central scalar imaginary $i$ satisfying $i^2 = -1$. A general element is $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$. The algebra, its norm form, its conjugations, its six distinguished subspaces and its matrix realization are those of *Biquaternion Algebra*, *Biquaternion Four-Vector Representation* and *Biquaternion 2×2 Matrix Representation*.

This article presents the **regular representation** of $\mathbb{B}$: the algebra acting on itself on the left, and the $4 \times 4$ matrix of that action in the coefficient space of *Biquaternion Four-Vector Representation*. The word *representation* is used here in both senses at once, the concrete realization and the technical representation of an algebra on a vector space, because the action is the object of study. The article is the third and last of the group, and it uses both predecessors: the coefficient space of the first article, on which the operator is written, and the simple module $V$ of the second, because the algebra is $V \oplus V$ as a left module and the regular representation is therefore reducible. It is the first reducible realization met in this subcategory.

The article owns the $4 \times 4$ regular matrix, the left and right multiplication operators, the relation between them, including the plausible identity that is false, the decomposition $\mathbb{B} = I_1 \oplus I_2 \cong V \oplus V$, and the centralizer statement. It deliberately does not treat the regular representation of the real quaternions $\mathbb{H}$, which belongs to *Quaternion Representations* and is cited once as the restriction to a real subalgebra; it does not treat the eigenvalues, the Cayley–Hamilton identity or the eigenspace dimensions of the regular matrix, which belong to *Biquaternion Spectral Theory*, later in this chapter; and it does not treat the idempotents and the Peirce decomposition, which belong to *Biquaternion Ideals and Peirce Decomposition*, except to cite the idempotent that splits the algebra into its two minimal left ideals. No physical vocabulary is used: the two-sided action of the unit-norm group is a group action on a real vector space preserving a quadratic form, and the double cover is a group homomorphism with kernel of order two; it is not a spinor, a chirality or a handedness of a physical particle.

## The Left Regular Representation

**Definition.** The **left regular representation** of $\mathbb{B}$ is the map

$$
\rho_L : \mathbb{B} \longrightarrow \operatorname{End}_{\mathbb{C}}(\mathbb{B}), \qquad \rho_L(\tilde{Q})(\tilde{R}) = \tilde{Q}\tilde{R}.
$$

For each $\tilde{Q}$, the map $\tilde{R} \mapsto \tilde{Q}\tilde{R}$ is $\mathbb{C}$-linear because multiplication is bilinear, so $\rho_L(\tilde{Q})$ is a $\mathbb{C}$-linear endomorphism of the four-dimensional space $\mathbb{B}$. Writing each endomorphism as a matrix in the basis $e_0, e_1, e_2, e_3$, the same symbol $\rho_L(\tilde{Q})$ denotes the matrix acting on the $4 \times 1$ column $R$ of *Biquaternion Four-Vector Representation*:

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

Expanding with $e_1 e_2 = e_3$, $e_2 e_3 = e_1$, $e_3 e_1 = e_2$ gives the displayed columns, hence the matrix. $\square$

**Remark (the same four for a different reason).** The matrix above is $4 \times 4$, and the coefficient space of *Biquaternion Four-Vector Representation* has complex dimension $4$. These are the same four for the same reason and not because of a coincidence: the algebra has complex dimension $4$, and the regular representation is the algebra acting on itself, so the space and the index set of the matrix are the same object. In *Biquaternion 2×2 Matrix Representation* the number $2$ appears both as the dimension of the simple module and as the size of the matrix algebra, for the parallel reason that the algebra is the algebra of endomorphisms of that module.

**Example.** For the element $\tilde{Q} = (2+i)e_0 + (1-i)e_1 + 3e_2 + ie_3$, so that $(Q_0, Q_1, Q_2, Q_3) = (2+i, 1-i, 3, i)$, the regular matrix is

$$
\rho_L(\tilde{Q}) = \begin{pmatrix}
2+i & -1+i & -3 & -i \\
1-i & 2+i & -i & 3 \\
3 & i & 2+i & -1+i \\
i & -3 & 1-i & 2+i
\end{pmatrix}.
$$

The column of $\tilde{R} = e_0 + e_1$, namely $R = (1, 1, 0, 0)$, is carried by this matrix to the column $(1+2i, 3, 3+i, -3+i)$, which is the four-vector of the product $\tilde{Q}\tilde{R}$ computed by the component formula of *Biquaternion Four-Vector Representation*.

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

so the two matrices agree on a basis. $\square$

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

**Proof.** The columns are the images $e_m \tilde{Q}$, and one expands as in the left case with the factors in the opposite order. Alternatively, since each $e_m$ is either $e_0$ or one of the $e_k$, and $e_k e_j = -e_j e_k$ for $j \neq k$, the matrix is the transpose of the left matrix conjugated by the fixed sign matrix of the next section, $\rho_R(\tilde{Q}) = D\,\rho_L(\tilde{Q})^{\mathsf T}D$, and direct computation of the four products confirms the display. $\square$

**Theorem (the right representation is an anti-homomorphism).** For all $\tilde{Q}, \tilde{R} \in \mathbb{B}$,

$$
\rho_R(\tilde{Q})\,\rho_R(\tilde{R}) = \rho_R(\tilde{R}\tilde{Q}).
$$

Hence $\rho_R$ is an algebra **anti**-homomorphism, and it is the regular representation of the opposite algebra $\mathbb{B}^{\mathrm{op}}$, not a second representation of $\mathbb{B}$.

**Proof.** For every $\tilde{S}$, associativity gives

$$
\rho_R(\tilde{Q})\bigl(\rho_R(\tilde{R})(\tilde{S})\bigr) = (\tilde{S}\tilde{R})\tilde{Q} = \tilde{S}(\tilde{R}\tilde{Q}) = \rho_R(\tilde{R}\tilde{Q})(\tilde{S}),
$$

which is the displayed identity. An anti-homomorphism is by definition a homomorphism from the opposite algebra, and the underlying linear map is the same. $\square$

**Remark (which side is which).** The left and right regular representations are the two actions of a non-commutative algebra on itself. Since quaternion conjugation is an anti-automorphism, the composite $\tilde{Q} \mapsto \rho_L(\bar{\tilde{Q}})$ is an **anti**-homomorphism, that is, a homomorphism from $\mathbb{B}^{\mathrm{op}}$ into $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$; it is therefore the right regular representation up to a fixed change of basis, and the next section identifies that change of basis and shows that it is not the identity. The two representations differ as soon as the algebra is non-commutative.

## Transposition and the Two Representations

**Proposition (transposition is quaternion conjugation).** For every biquaternion $\tilde{Q}$,

$$
\rho_L(\tilde{Q})^{\mathsf{T}} = \rho_L(\bar{\tilde{Q}}),
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

and replacing $Q_k$ by $-Q_k$ in that same closed form reproduces this matrix. $\square$

**Remark (the false identity).** The right regular matrix is **not** the transpose of the left one:

$$
\rho_R(\tilde{Q}) \neq \rho_L(\tilde{Q})^{\mathsf{T}} \quad \text{in general}.
$$

For $\tilde{Q} = e_1$ the left matrix is $\rho_L(e_1) = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$, whose transpose is $\begin{pmatrix} 0 & 1 & 0 & 0 \\ -1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & -1 & 0 \end{pmatrix}$, while the right matrix is $\rho_R(e_1) = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & -1 & 0 \end{pmatrix}$: the two differ in the sign of the upper-left block. The proposition above gives the reason: the transpose is the left multiplication of the quaternion conjugate, $\rho_L(\tilde{Q})^{\mathsf{T}} = \rho_L(\bar{\tilde{Q}})$, so it is a left multiplication and equals the right multiplication only on the centre. The variant that replaces $\tilde{Q}$ by $\bar{\tilde{Q}}$ is not a second identity, since $\tilde{Q} \mapsto \bar{\tilde{Q}}$ is a bijection of the algebra.

**Theorem (the correct relation).** Let $D = \operatorname{diag}(-1, 1, 1, 1)$, so that $D^2 = I$. Then for every biquaternion $\tilde{Q}$,

$$
\rho_R(\tilde{Q}) = D\,\rho_L(\tilde{Q})^{\mathsf{T}}\,D = D\,\rho_L(\bar{\tilde{Q}})\,D .
$$

Hence the right representation is the contragredient of the left one up to the fixed change of basis $D$.

**Proof.** Apply $D$ on the left and on the right to the transpose of the closed form of $\rho_L(\tilde{Q})$. Left multiplication by $D$ negates the first row, and right multiplication by $D$ negates the first column; the corner entry lies in both and is negated twice, hence unchanged. The resulting matrix is the closed form of $\rho_R(\tilde{Q})$ displayed above. The second equality uses the transpose proposition. $\square$

**Corollary (the difference vanishes exactly on the centre).** The difference $\rho_L(\tilde{Q}) - \rho_R(\tilde{Q})$ is the zero matrix if and only if $\tilde{Q} \in \mathbb{C}_{\mathbb{B}} = \mathbb{C} e_0$.

**Proof.** If $\tilde{Q} = \lambda e_0$ then $\rho_L(\tilde{Q}) = \rho_R(\tilde{Q}) = \lambda I$, since scalar multiplication is central. Conversely, if the two matrices agree then $\tilde{Q}\tilde{R} = \tilde{R}\tilde{Q}$ for every $\tilde{R}$, so $\tilde{Q}$ lies in the centre, which is the scalar subspace by *Biquaternion 2×2 Matrix Representation*. Comparing the two closed forms directly, the entries in the three last rows and columns agree only when $Q_1 = Q_2 = Q_3 = 0$. $\square$

**Remark (what left and right mean).** The two representations differ **because the algebra is non-commutative**. The matrix $\rho_L(\tilde{Q}) - \rho_R(\tilde{Q})$ is the operator $\tilde{R} \mapsto \tilde{Q}\tilde{R} - \tilde{R}\tilde{Q}$ written in the basis, so its $m$-th column is the coordinate column of the commutator $[\tilde{Q}, e_m]$; the difference vanishes on $\mathbb{C}_{\mathbb{B}}$ and nowhere else. This is the sense in which the left and right regular representations of $\mathbb{B}$ are distinct, and the sense in which the row of *Biquaternion Four-Vector Representation* carries the right action and not a further left one.

## The Module Structure and Reducibility

The regular representation is the first reducible realization in this subcategory, and its reduction is the decomposition of the algebra into two minimal left ideals.

**Definition.** Let

$$
p = \tfrac{1}{2}(e_0 + i e_3), \qquad q = \tfrac{1}{2}(e_0 - i e_3).
$$

**Lemma (orthogonal idempotents).** The elements $p$ and $q$ satisfy

$$
p^2 = p, \qquad q^2 = q, \qquad pq = qp = 0, \qquad p + q = e_0,
$$

so that $\mathbb{B} = \mathbb{B}p \oplus \mathbb{B}q$ as a direct sum of left ideals.

**Proof.** Because $i$ is central, $e_3^2 = -e_0$ and $i^2 = -1$, one computes $p^2 = \tfrac{1}{4}(e_0^2 + 2ie_3 + i^2 e_3^2) = \tfrac{1}{4}(e_0 + 2ie_3 + e_0) = \tfrac{1}{2}(e_0 + ie_3) = p$, and similarly $q^2 = q$, while $pq = \tfrac{1}{4}(e_0^2 - i^2e_3^2) = \tfrac{1}{4}(e_0 - e_0) = 0$. The sum is $e_0$, and the two ideals meet only in $0$: an element lying in both satisfies $\tilde{X} = \tilde{X}q = 0$, because membership of $\mathbb{B}q$ gives $\tilde{X}q = \tilde{X}$ while $pq = 0$. The sum is therefore direct. The idempotents and the Peirce decomposition are the subject of *Biquaternion Ideals and Peirce Decomposition*; the statement is used here only to split the module. $\square$

**Theorem (the regular representation is $V \oplus V$).** In the basis

$$
p, \quad e_1 p, \quad q, \quad e_1 q
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

and each block has trace $2Q_0$ and determinant $N(\tilde{Q})$. Consequently each block is similar to the matrix $\Phi(\tilde{Q})$ of *Biquaternion 2×2 Matrix Representation*, each block is a copy of the simple module $V$, and

$$
\rho_L \cong V \oplus V
$$

as a left $\mathbb{B}$-module. The regular representation is therefore reducible, and it is the first reducible realization in this subcategory.

**Proof.** The two ideals $\mathbb{B}p$ and $\mathbb{B}q$ are stable under $\rho_L(\tilde{Q})$, because $\rho_L(\tilde{Q})(\tilde{S}p) = (\tilde{Q}\tilde{S})p$ for every $\tilde{S}$; hence the matrix is block diagonal in any basis adapted to the decomposition. The ideal $\mathbb{B}p$ has the basis $p, e_1p$, since $e_2 p = i e_1 p$ and $e_3 p = -ip$. Its multiplication by the basis elements is read from

$$
e_1 p = e_1p, \quad e_2 p = ie_1p, \quad e_3 p = -ip, \qquad e_1(e_1p) = -p, \quad e_2(e_1p) = ip, \quad e_3(e_1p) = ie_1p,
$$

so in the basis $p, e_1p$ the three units act by the matrices
$\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$,
$\begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}$ and
$\begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix}$, and carrying out the sum $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ gives the displayed block $A_+$; the same computation on the basis $q, e_1q$ of $\mathbb{B}q$ gives $A_-$. The trace of each block is $2Q_0$ by inspection and the determinant is computed as in the matrix realization,

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

for every $\tilde{Q}$: both sides are $\mathbb{C}$-linear in $\tilde{Q}$, so it suffices to compare them on the four basis elements $e_0, e_1, e_2, e_3$, where the two displayed formulas agree elementwise. Both conjugating matrices are invertible, since $\det\Phi(u_+) = (1-i)(1+i) = 2 = \det\Phi(u_-)$, and consequently each block is similar to $\Phi(\tilde{Q})$ for every $\tilde{Q}$, including the elements whose vector part is nonzero while $Q_1^2 + Q_2^2 + Q_3^2 = 0$ and the block has a repeated eigenvalue. Both blocks therefore have the characteristic polynomial $\lambda^2 - 2Q_0\lambda + N(\tilde{Q})$ of $\Phi(\tilde{Q})$, as the similarity requires, and each realizes the simple module $V$ of *Biquaternion 2×2 Matrix Representation*; the regular module is $V \oplus V$. $\square$

**Remark (the characteristic polynomial).** In the block basis of the theorem above the regular matrix is block diagonal with the two blocks $A_+$ and $A_-$, each similar to $\Phi(\tilde{Q})$, so its characteristic polynomial is the square of that of the simple module,

$$
\chi_{\rho_L(\tilde{Q})}(\lambda) = \bigl( \lambda^2 - 2Q_0\lambda + N(\tilde{Q}) \bigr)^2,
$$

which the block form of the theorem above gives at once. The eigenvalues themselves, the Cayley–Hamilton identity, the eigenspace dimensions and the doubling of the multiplicities that the square produces are the subject of *Biquaternion Spectral Theory*, later in this chapter, and are cited from there rather than developed here.

**Remark (the irreducible submodules are the minimal left ideals).** The two blocks are the two minimal left ideals $I_1 = \mathbb{B}p$ and $I_2 = \mathbb{B}q$ of the algebra. Both are isomorphic to the module $V$ of *Biquaternion 2×2 Matrix Representation*, and the fact that $V$ is the only simple module is the classification of *Biquaternion Representation Theory*. The decomposition $\mathbb{B} = I_1 \oplus I_2$ is therefore the same fact as the two-block form of the regular matrix, read as ideals rather than as a matrix; the same decomposition is stated in *The Defining Module of the Biquaternion Algebra*, where the simple module is written $S$, as $\mathbb{B} \cong S \oplus S$.

## The Determinant and the Trace

**Corollary (determinant and trace).** For every biquaternion $\tilde{Q}$,

$$
\det \rho_L(\tilde{Q}) = N(\tilde{Q})^2, \qquad \operatorname{Tr} \rho_L(\tilde{Q}) = 4Q_0 .
$$

The determinant of the regular matrix is the **square** of the norm form, and it is not the norm form.

**Proof.** In the block basis of the preceding theorem the matrix is block diagonal with the two blocks $A_+$ and $A_-$, so the determinant is the product $\det A_+ \det A_- = N(\tilde{Q}) \cdot N(\tilde{Q}) = N(\tilde{Q})^2$, and the trace is the sum $\operatorname{Tr} A_+ + \operatorname{Tr} A_- = 2Q_0 + 2Q_0 = 4Q_0$. Both quantities are unchanged by the change of basis. $\square$

**Example.** For $\tilde{Q} = (2+i)e_0 + (1-i)e_1 + 3e_2 + ie_3$ one has $N(\tilde{Q}) = 11 + 2i$ and

$$
\det \rho_L(\tilde{Q}) = (11+2i)^2 = 117 + 44i, \qquad \operatorname{Tr}\rho_L(\tilde{Q}) = 4(2+i) = 8 + 4i,
$$

in agreement with the two blocks $A_+(\tilde{Q}) = \begin{pmatrix} 3+i & -1+4i \\ 1+2i & 1+i \end{pmatrix}$ and $A_-(\tilde{Q}) = \begin{pmatrix} 1+i & -1-2i \\ 1-4i & 3+i \end{pmatrix}$ on this element, each of trace $4+2i$ and determinant $11+2i$.

**Remark (the determinant is not the norm form).** The determinant of the regular matrix is $N^2$, and the difference from $N$ is a genuine feature of the regular representation and not a notational slip. The simple module carries the norm form as its determinant, $\det\Phi(\tilde{Q}) = N(\tilde{Q})$, and the regular module is the direct sum of two copies of it, so its determinant is the product of two norm forms. The square appears because the regular representation acts on a space of dimension twice that of the simple module; it is the algebraic shadow of the factor $2$ between the two dimensions.

## The Double Centralizer

**Theorem (the centralizer is the right copy).** The algebra of endomorphisms of the left regular module is the image of the right regular representation,

$$
\operatorname{End}_{\mathbb{B}}(\mathbb{B}) = \rho_R(\mathbb{B}),
$$

and consequently the centralizer of $\rho_L(\mathbb{B})$ in $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ is $\rho_R(\mathbb{B})$, of complex dimension $4$.

**Proof.** An endomorphism $f$ of the left module $\mathbb{B}$ is determined by $f(e_0)$, since $f(\tilde{R}) = f(\tilde{R}e_0) = \tilde{R}f(e_0)$ for every $\tilde{R}$; writing $\tilde{Q} = f(e_0)$ gives $f(\tilde{R}) = \tilde{R}\tilde{Q} = \rho_R(\tilde{Q})(\tilde{R})$, so $f = \rho_R(\tilde{Q})$ and the endomorphisms are exactly the right multiplications. Conversely every $\rho_R(\tilde{Q})$ is a module endomorphism, because right and left multiplication associate. For the centralizer, a matrix commuting with $\rho_L(\tilde{R})$ for every $\tilde{R}$ is exactly an element of $\operatorname{End}_{\mathbb{B}}(\mathbb{B})$, which is $\rho_R(\mathbb{B})$. The right copy has complex dimension $4$ because $\rho_R$ is injective: $\rho_R(\tilde{Q}) = 0$ forces $\tilde{Q} = \rho_R(\tilde{Q})(e_0) = 0$. $\square$

**Remark.** The theorem is the regular-module case of the double centralizer phenomenon, and it mirrors the statement $\mathbb{B} = \operatorname{End}_{\mathbb{C}}(V)$ of *The Defining Module of the Biquaternion Algebra*: the algebra is recovered as the centralizer of the opposite copy acting on itself. The two copies commute and together generate the full matrix algebra $\operatorname{End}_{\mathbb{C}}(\mathbb{B}) \cong M_4(\mathbb{C})$.

## The Real Form

**Proposition (the real regular representation).** Regarded over $\mathbb{R}$ in the real basis

$$
e_0, e_1, e_2, e_3, i e_0, i e_1, i e_2, i e_3,
$$

of the eight-dimensional real space underlying $\mathbb{B}$, the left regular representation is an $8 \times 8$ real matrix $\rho_L^{\mathbb{R}}(\tilde{Q})$, with

$$
\det \rho_L^{\mathbb{R}}(\tilde{Q}) = |N(\tilde{Q})|^4, \qquad \operatorname{Tr}\rho_L^{\mathbb{R}}(\tilde{Q}) = 8 \operatorname{Re}(Q_0).
$$

**Proof.** The real matrix is the realification of the complex-linear endomorphism $\rho_L(\tilde{Q})$ of the four-dimensional complex space $\mathbb{B}$. A complex-linear endomorphism with eigenvalues $\lambda_1, \ldots, \lambda_4$ has realification with eigenvalues $\lambda_1, \bar\lambda_1, \ldots, \lambda_4, \bar\lambda_4$, so its determinant is $|\lambda_1 \cdots \lambda_4|^2 = |\det \rho_L(\tilde{Q})|^2 = |N(\tilde{Q})^2|^2 = |N(\tilde{Q})|^4$, and its trace is $2\operatorname{Re}(\lambda_1 + \cdots + \lambda_4) = 2\operatorname{Re}(4Q_0) = 8\operatorname{Re}(Q_0)$. $\square$

**Remark (why the dimension doubles).** The real dimension doubles because $\mathbb{B}$ is a complex vector space and is regarded as a real vector space by restriction of scalars: the correspondence $\operatorname{Res}_{\mathbb{C}/\mathbb{R}} \mathbb{C}^4 = \mathbb{R}^8$ replaces each complex coordinate by its real and imaginary parts. The same doubling applies to the module $V$ of *Biquaternion 2×2 Matrix Representation*, whose realification $S$ has real dimension $4$, so over $\mathbb{R}$ the regular representation is $\rho_L^{\mathbb{R}} \cong \operatorname{Res}_{\mathbb{C}/\mathbb{R}}(V \oplus V)$, and the block decomposition of the complex case survives with each block doubled in size. Restricted to the real subalgebra $\mathbb{H}_{\mathbb{B}}$, and read on $\mathbb{H}_{\mathbb{B}}$ itself, the same construction is the $4 \times 4$ real regular representation of the quaternions, which is the subject of *Quaternion Representations*; complexifying the algebra doubles both its real dimension and the size of the regular matrix.

## The Two-Sided Action

One geometric statement can be made with what the regular representation supplies, and it uses both the left and the right copies at once.

**Definition.** The **unit-norm group** of $\mathbb{B}$ is

$$
\tilde{G} = \{ \tilde{A} \in \mathbb{B} : N(\tilde{A}) = 1 \}.
$$

It is a group, and under the isomorphism $\Phi$ of *Biquaternion 2×2 Matrix Representation* it is the special linear group $SL_2(\mathbb{C})$, since $N(\tilde{A}) = \det\Phi(\tilde{A})$.

**Proposition (the two-sided action).** The map

$$
\tilde{G} \times \mathbb{M}_+ \longrightarrow \mathbb{M}_+, \qquad (\tilde{A}, \tilde{X}) \longmapsto \tilde{A} \tilde{X} \tilde{A}^{\dagger},
$$

is a group action of $\tilde{G}$ on the real vector space $\mathbb{M}_+$ of real dimension $4$, and it preserves the norm form restricted to $\mathbb{M}_+$:

$$
N(\tilde{A}\tilde{X}\tilde{A}^{\dagger}) = N(\tilde{X}) .
$$

**Proof.** If $\tilde{X}$ is Hermitian then $(\tilde{A}\tilde{X}\tilde{A}^{\dagger})^{\dagger} = \tilde{A}\tilde{X}^{\dagger}\tilde{A}^{\dagger} = \tilde{A}\tilde{X}\tilde{A}^{\dagger}$, so $\mathbb{M}_+$ is preserved. The norm form is multiplicative, $N(\tilde{A}\tilde{X}\tilde{A}^{\dagger}) = N(\tilde{A})N(\tilde{X})N(\tilde{A}^{\dagger})$, and $N(\tilde{A}) = 1$ while $N(\tilde{A}^{\dagger}) = N(\tilde{A})^{*} = 1$. Composition holds because $\tilde{A}_1(\tilde{A}_2\tilde{X}\tilde{A}_2^{\dagger})\tilde{A}_1^{\dagger} = (\tilde{A}_1\tilde{A}_2)\tilde{X}(\tilde{A}_1\tilde{A}_2)^{\dagger}$. $\square$

**Theorem (the double cover).** The action above defines a surjective group homomorphism

$$
\tilde{G} = SL_2(\mathbb{C}) \longrightarrow SO^+(1,3),
$$

onto the identity component $SO^+(1,3)$ of the orthogonal group of the form, with kernel $\{e_0, -e_0\}$, which is central of order two.

**Proof.** A real-linear map of $\mathbb{M}_+$ preserving the quadratic form of signature $(1,3)$ is an element of $O(1,3)$; the action is continuous in $\tilde{A}$ and $\tilde{G} = SL_2(\mathbb{C})$ is connected, so the image is a connected subgroup of $O(1,3)$ and therefore lies in the identity component $SO^+(1,3)$. The surjectivity onto that component is the standard fact that $SL_2(\mathbb{C})$ is the double cover of the restricted orthogonal group, cited from the standard theory of the orthogonal groups. For the kernel, $\tilde{A}$ acts trivially precisely when $\tilde{A}\tilde{X}\tilde{A}^{\dagger} = \tilde{X}$ for every Hermitian $\tilde{X}$. Taking $\tilde{X} = e_0$ gives $\tilde{A}\tilde{A}^{\dagger} = e_0$, that is, $\tilde{A}$ is unitary, and the condition then reads $\tilde{A}\tilde{X} = \tilde{X}\tilde{A}$ for every Hermitian $\tilde{X}$. The Hermitian elements span $\mathbb{B}$ over $\mathbb{C}$, so $\tilde{A}$ commutes with every element of $\mathbb{B}$ and is therefore a central element $\lambda e_0$; the norm condition $N(\lambda e_0) = \lambda^2 = 1$ leaves $\lambda = \pm 1$. Both central elements act trivially on $\mathbb{M}_+$, and no other element does. The same double cover is met in *Spinors and the Biquaternion Spinor Module*, where it is read on the module; here it is read as the two-sided action of the regular representation, that is, as the left copy composed with the right copy of the conjugate transpose. $\square$

**Remark.** The statement above is a statement of algebra and of the geometry of a quadratic form: a group of linear transformations of a four-dimensional real space preserving a form of signature $(1,3)$, and a two-to-one homomorphism onto it. It is not a statement about a physical particle, and no vocabulary of physics is used. The two-sided action is the regular representation read twice, once through $\rho_L(\tilde{A})$ and once through the right action of $\tilde{A}^{\dagger}$; it is the one place in this article where the left and right copies enter together.

## Summary

The left regular representation $\rho_L(\tilde{Q})(\tilde{R}) = \tilde{Q}\tilde{R}$ is the algebra acting on itself on the left, and in the basis $e_0, e_1, e_2, e_3$ its matrix is the Cayley matrix of quaternion multiplication, each entry of which is a single coefficient of $\tilde{Q}$ carrying a sign and none of which is a sum of coefficients. It is a homomorphism, its transpose is the left matrix of the quaternion conjugate, $\rho_L(\tilde{Q})^{\mathsf{T}} = \rho_L(\bar{\tilde{Q}})$, its determinant is the square of the norm form, $\det\rho_L(\tilde{Q}) = N(\tilde{Q})^2$, and its trace is $4Q_0$.

The right regular representation $\rho_R(\tilde{Q})(\tilde{R}) = \tilde{R}\tilde{Q}$ is an anti-homomorphism and the regular representation of the opposite algebra. The naive identity $\rho_R(\tilde{Q}) = \rho_L(\tilde{Q})^{\mathsf{T}}$ is false — and the variant with $\bar{\tilde{Q}}$ is the same statement, since $\rho_L(\bar{\tilde{Q}})^{\mathsf{T}} = \rho_L(\tilde{Q})$ — while what holds is $\rho_R(\tilde{Q}) = D\rho_L(\tilde{Q})^{\mathsf{T}}D = D\rho_L(\bar{\tilde{Q}})D$ with $D = \operatorname{diag}(-1,1,1,1)$. The difference $\rho_L - \rho_R$ vanishes exactly on the centre $\mathbb{C}_{\mathbb{B}}$, which is the precise sense in which left and right differ because the algebra is non-commutative.

The regular module is $\mathbb{B} = I_1 \oplus I_2$ with $I_1 = \mathbb{B}p$, $I_2 = \mathbb{B}q$ and $p = \tfrac{1}{2}(e_0 + ie_3)$, $q = \tfrac12(e_0 - ie_3)$; in the adapted basis $p, e_1p, q, e_1q$ the regular matrix is block diagonal with the two blocks $A_+$, $A_-$, each similar to $\Phi(\tilde{Q})$ and each a copy of the simple module $V$. So $\rho_L \cong V \oplus V$, the regular representation is reducible, and it is the first reducible realization of this subcategory. The centralizer of $\rho_L(\mathbb{B})$ is $\rho_R(\mathbb{B})$, the right copy, of complex dimension $4$. Over $\mathbb{R}$ the regular representation is $8 \times 8$ real with $\det = |N|^4$ and trace $8\operatorname{Re}(Q_0)$, the dimension doubling by restriction of scalars. The two-sided action of the unit-norm group on $\mathbb{M}_+$ preserves the norm form and gives a two-to-one homomorphism $SL_2(\mathbb{C}) \to SO^+(1,3)$ with kernel $\{\pm e_0\}$.

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
| $N(\tilde{Q}) = \sum_\mu Q_\mu^2$ | Norm form; $\det\rho_L(\tilde{Q}) = N(\tilde{Q})^2$ |
| $\bar{\cdot}, {}^{*}, {}^{\dagger}, {}^{\flat}$ | Quaternion, complex, Hermitian and anti-Hermitian conjugations |
| $\mathbb{C}_{\mathbb{B}}$ | Centre, the scalar subspace $\mathbb{C} e_0$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real quaternion subalgebra; its restriction carries the quaternion regular representation of *Quaternion Representations* |
| $p = \tfrac{1}{2}(e_0 + ie_3)$, $q = \tfrac12(e_0 - ie_3)$ | Orthogonal idempotents, $p + q = e_0$, $pq = 0$ |
| $I_1 = \mathbb{B}p$, $I_2 = \mathbb{B}q$ | The two minimal left ideals, $\mathbb{B} = I_1 \oplus I_2$ |
| $A_+(\tilde{Q}), A_-(\tilde{Q})$ | The two $2 \times 2$ blocks of $\rho_L$ in the adapted basis |
| $u_+ = e_0 + e_3$, $u_- = e_1 + e_2$ | Conjugating elements, $A_\pm(\tilde{Q}) = \Phi(u_\pm)\Phi(\tilde{Q})\Phi(u_\pm)^{-1}$ |
| $V = \mathbb{C}^2$ | Simple left $\mathbb{B}$-module, complex dimension $2$ |
| $\mathbb{B}^{\mathrm{op}}$ | Opposite algebra; $\rho_R$ is a homomorphism from it |
| $\epsilon^{ijk}$ | Levi-Civita symbol on the indices $1, 2, 3$ |
| $\Phi(\tilde{Q})$ | Matrix realization of *Biquaternion 2×2 Matrix Representation* |
| $\operatorname{Res}_{\mathbb{C}/\mathbb{R}}$ | Restriction of scalars |
| $\operatorname{End}_{\mathbb{B}}(\mathbb{B}) = \rho_R(\mathbb{B})$ | Endomorphism algebra of the regular module |
| $\rho_L^{\mathbb{R}}(\tilde{Q})$ | Real $8 \times 8$ regular matrix |
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
