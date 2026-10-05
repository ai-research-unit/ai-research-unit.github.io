# __Biquaternion 4×4 Regular Matrix Element Representation__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ and its four-vector coordinates are those of *Biquaternions as a Vector Space over $\mathbb{C}$* and *Biquaternion Four-Vector Element Representation*.

The **left regular representation** $\rho_L(\tilde Q)(\tilde R)=\tilde Q\tilde R$, its matrix in the basis $e_0,e_1,e_2,e_3$, its multiplicativity and injectivity, the trace $\operatorname{Tr}\rho_L(\tilde Q)=4Q_0$ and the determinant $\det\rho_L(\tilde Q)=N(\tilde Q)^2$, and the six distinguished subspaces in the regular model are *Introduction to the 4×4 Regular Matrix Representation of Biquaternions*; they are used here and not restated.

This article is the further development of that representation. It owns the right multiplication and the relation between the two representations, the module structure and the decomposition $\mathbb{B}=I_1\oplus I_2\cong V\oplus V$, the double centralizer, the $8\times8$ real form, and a second $4\times4$ realization with the sixteen products of the biparavectors. It is the first reducible realization met in this subcategory. It does not treat the eigenvalues, the Cayley–Hamilton identity or the eigenspace dimensions of the regular matrix, which belong to *Biquaternion Spectral Theory*; and it does not treat the idempotents and the Peirce decomposition, which belong to *Biquaternion Idempotents and Projections* and *Biquaternion Ideals and Peirce Decomposition*, except to cite the idempotents that split the algebra into its two minimal left ideals. No physical vocabulary is used: the two-sided action of the group of elements of $N=1$ on the Hermitian subspace is a statement of algebra, not a spinor, a chirality or a handedness of a physical particle.

One comparative item is added beyond the representation itself: a second $4 \times 4$ realization of $\mathbb{B}$ taken from the literature on eigenvector bundles, recorded with the multiplicative quadratic map it carries, because it is the natural contrast with both the regular realization and the congruence-shaped operator of *Biquaternion 4×4 Regular Matrix Operator Representation*.

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

**Proof.** The columns are the images $e_m \tilde{Q}$, and one expands as in the left case of *Introduction to the 4×4 Regular Matrix Representation of Biquaternions* with the factors in the opposite order. Alternatively, since each $e_m$ is either $e_0$ or one of the $e_k$, and $e_k e_j = -e_j e_k$ for $j \neq k$, the matrix is the transpose of the left matrix conjugated by the fixed sign matrix of the next section, $\rho_R(\tilde{Q}) = D\,\rho_L(\tilde{Q})^{\mathsf T}D$, and direct computation of the four products confirms the display.

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

where the transpose is taken in the basis $e_0, e_1, e_2, e_3$ of the corpus.

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

**Proof.** If $\tilde{Q} = \lambda e_0$ then $\rho_L(\tilde{Q}) = \rho_R(\tilde{Q}) = \lambda I$, since scalar multiplication is central. Conversely, if the two matrices agree then $\tilde{Q}\tilde{R} = \tilde{R}\tilde{Q}$ for every $\tilde{R}$, so $\tilde{Q}$ lies in the centre, which is the scalar subspace. Comparing the two closed forms directly, the entries in the three last rows and columns agree only when $Q_1 = Q_2 = Q_3 = 0$.

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

of $\mathbb{B}$, the left regular matrix of $\tilde{Q}$ is

$$
\rho_L(\tilde{Q}) \sim \begin{pmatrix}
Q_0 - iQ_3 & -Q_1 + iQ_2 & 0 & 0 \\
Q_1 + iQ_2 & Q_0 + iQ_3 & 0 & 0 \\
0 & 0 & Q_0 + iQ_3 & -Q_1 - iQ_2 \\
0 & 0 & Q_1 - iQ_2 & Q_0 - iQ_3
\end{pmatrix},
$$

with the four corner entries zero: the subspaces spanned by $\tilde\Pi_1, e_1\tilde\Pi_1$ and by $\tilde\Pi_2, e_1\tilde\Pi_2$ are invariant under $\rho_L(\tilde{Q})$, and on each of them the action is that of a minimal left ideal, hence a copy of the simple module $V$, and

$$
\rho_L \cong V \oplus V
$$

as a left $\mathbb{B}$-module. The regular representation is therefore reducible, and it is the first reducible realization in this subcategory.

**Proof.** The two ideals $\mathbb{B}\tilde\Pi_1$ and $\mathbb{B}\tilde\Pi_2$ are stable under $\rho_L(\tilde{Q})$, because $\rho_L(\tilde{Q})(\tilde{S}\tilde\Pi_1) = (\tilde{Q}\tilde{S})\tilde\Pi_1$ for every $\tilde{S}$; hence the matrix is block diagonal in any basis adapted to the decomposition. The ideal $\mathbb{B}\tilde\Pi_1$ has the basis $\tilde\Pi_1, e_1\tilde\Pi_1$, since $e_2 \tilde\Pi_1 = i e_1 \tilde\Pi_1$ and $e_3 \tilde\Pi_1 = -i\tilde\Pi_1$. Its multiplication by the basis elements is read from

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
\chi_{\rho_L(\tilde{Q})}(\lambda) = \bigl( \lambda^2 - 2Q_0\lambda + N(\tilde{Q}) \bigr)^2,
$$

which the form of the theorem above gives at once. The eigenvalues themselves, the Cayley–Hamilton identity, the eigenspace dimensions and the doubling of the multiplicities that the square produces are the subject of *Biquaternion Spectral Theory*, later in this chapter, and are cited from there rather than developed here.

**Remark (the irreducible submodules are the minimal left ideals).** The two invariant subspaces are the two minimal left ideals $I_1 = \mathbb{B}\tilde\Pi_1$ and $I_2 = \mathbb{B}\tilde\Pi_2$ of the algebra. Both afford the module $V$, and the fact that $V$ is the only simple module is the classification of the simple modules. The decomposition $\mathbb{B} = I_1 \oplus I_2$ is therefore the same fact as the diagonal form of the regular matrix, read as ideals rather than as a matrix; the same decomposition is stated in *Modules over the Biquaternion Algebra*, where the simple module is written $S$, as $\mathbb{B} \cong S \oplus S$.

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

**Remark (why the dimension doubles).** The real dimension doubles because $\mathbb{B}$ is a complex vector space and is regarded as a real vector space by restriction of scalars: the correspondence $\operatorname{Res}_{\mathbb{C}/\mathbb{R}} \mathbb{C}^4 = \mathbb{R}^8$ replaces each complex coordinate by its real and imaginary parts. The same doubling applies to the module $V$, whose realification $S$ has real dimension $4$, so over $\mathbb{R}$ the regular representation is $\rho_L^{\mathbb{R}} \cong \operatorname{Res}_{\mathbb{C}/\mathbb{R}}(V \oplus V)$, and the decomposition of the complex case survives with each part doubled in size. Restricted to the real subalgebra $\mathbb{H}_{\mathbb{B}}$, and read on $\mathbb{H}_{\mathbb{B}}$ itself, the same construction is the $4 \times 4$ real regular representation of the quaternions, which is the subject of *Quaternion Element Representations*; complexifying the algebra doubles both its real dimension and the size of the regular matrix.

## A Second $4 \times 4$ Realization, and the Multiplicative Map

The regular matrix is not the only $4 \times 4$ realization of $\mathbb{B}$ in use, and the second one worth recording comes from a question with no algebra in it: the eigenvectors of a parameterised family of matrices. Its shape is different enough that the difference is instructive, and the object it is built for — a multiplicative quadratic map into the real matrices, with no counterpart in the regular realization — is the reason for recording it here rather than in a dedicated article.

**The realization.** In the basis $e_0, ie_1, ie_2, ie_3$, for which

$$
(ie_1)^2 = (ie_2)^2 = (ie_3)^2 = e_0, \qquad (ie_1)(ie_2) = i(ie_3), \qquad (ie_2)(ie_3) = i(ie_1), \qquad (ie_3)(ie_1) = i(ie_2) ,
$$

the map on complex coefficients

$$
\Phi'(A_0, A_1, A_2, A_3) = \begin{pmatrix} A_0 & A_1 & A_2 & A_3 \\ A_1 & A_0 & -iA_3 & iA_2 \\ A_2 & iA_3 & A_0 & -iA_1 \\ A_3 & -iA_2 & iA_1 & A_0 \end{pmatrix}
$$

is a representation of $\mathbb{B}$. Its first row and column coincide, since $\Phi'$ is symmetric in the coefficients, which the Cayley matrix of *Introduction to the 4×4 Regular Matrix Representation of Biquaternions* is not; the price is the scalar imaginary scattered through the lower block. The change of basis is what makes the squares $+e_0$: the generators of this realization are the elements $ie_k$, not the $e_k$, and the difference is a change of orientation, the two choices being interchanged by the coefficient conjugation, not two different algebras.

**The realization is equivalent to the regular one.** Both are faithful four-dimensional linear realizations of $\mathbb{B} \cong M_2(\mathbb{C})$, and by the module structure of the section above every such realization is two copies of the simple module, $V \oplus V$; so an invertible intertwining matrix exists, and one was exhibited and checked on $100$ random elements, with maximum residual $1.9 \times 10^{-15}$. Nothing in the representation theory of the two distinguishes them, and everything the corpus says about $\rho_L$ as a module carries over.

**What the realization brings.** Each of $ie_1, ie_2, ie_3$ is skew-symmetric, and the products of the basis elements give a second Hermitian basis of $M_4(\mathbb{C})$: the sixteen matrices

$$
I,\; ie_1K_1,\; ie_2K_2,\; ie_3K_3,\quad ie_1,\; K_1,\; ie_2K_3,\; ie_3K_2,\quad ie_2,\; K_2,\; ie_1K_3,\; ie_3K_1,\quad ie_3,\; K_3,\; ie_1K_2,\; ie_2K_1 ,
$$

with $K_1, K_2, K_3$ the coefficient conjugates of $ie_1, ie_2, ie_3$, each squaring to $I$ and each Hermitian, so that real linear combinations of them are exactly the Hermitian $4 \times 4$ matrices; every one but $I$ is traceless. This was checked entry by entry. The same basis contains generators of the complex Clifford algebra $\mathbb{C}\ell(4)$, namely $ie_1, ie_2, ie_3K_1, ie_3K_2$, which anticommute pairwise to $\delta_{ij}I$ up to the conventional factor, so the realization also places $\mathbb{B}$ inside $M_4(\mathbb{C})$ in the Clifford manner of *Biquaternion Other Algebraic Element Representations*.

**The transposition identity is exact in this basis, and these are the matrices of the Maxwell literature.** The realization is the one in which the two $D$'s of the theorem of the transposition section disappear, and this is worth stating because it separates two things that the first basis runs together. Write the left regular matrix of the element $\tilde{Q} = A_0 e_0 + A_1 ie_1 + A_2 ie_2 + A_3 ie_3$ as

$$
\rho_L(\tilde{Q}) = A_0 I + cF(\mathbf{A}), \qquad
cF(\mathbf{A}) := \begin{pmatrix} 0 & \mathbf{A}^{\mathsf{T}} \\ \mathbf{A} & i[\mathbf{A}]_\times \end{pmatrix}, \qquad \mathbf{A} = (A_1, A_2, A_3),
$$

with $[\mathbf{u}]_\times$ the matrix of $\mathbf{v} \mapsto \mathbf{u} \times \mathbf{v}$; this is $\Phi'$ of the display above, and it is the same $cF$ that a matrix formulation of Maxwell's equations multiplies into the operator column $(-\partial_t, \nabla)^{\mathsf{T}}$. In this basis the right regular matrix is **exactly the transpose**,

$$
\rho_R(\tilde{Q}) = \rho_L(\tilde{Q})^{\mathsf{T}} ,
$$

with no sign matrix, where in the basis $e_0, e_1, e_2, e_3$ of the transposition section the relation read $\rho_R = D\rho_L^{\mathsf{T}}D$ instead. Both were recomputed over $100$ random elements, the first to $0$ and the second to $0$, and the change of basis between the two conventions was checked explicitly too: with $C = \operatorname{diag}(1, -i, -i, -i)$ carrying the coefficients of the corpus basis into those of this one, $C\rho_L(\tilde{Q})C^{-1}$ and $C\rho_R(\tilde{Q})C^{-1}$ are the two matrices displayed here, at residual $0$. So the *false identity* remark of the transposition section is a statement about a basis and not about the algebra: in the basis whose vector units square to $-e_0$ the transpose of the left matrix is a left multiplication of the conjugate, while in the basis whose vector units square to $+e_0$ it is the right multiplication, exactly, and the two $D$'s are the price of the first basis. The sixteen-matrix basis above is the same object read on the other side: as matrices it is $I$, the three $cF(\mathbf{e}_i)$, their complex conjugates and the pairwise products $cF(\mathbf{e}_i)(cF(\mathbf{e}_j))^{\natural}$, which are Hermitian and involutive with square $I$, traceless except for $I$, and orthogonal under the trace, $\operatorname{tr}(M_kM_l) = 4\delta_{kl}$ — all checked exactly — and the three $cF(\mathbf{e}_i)$ anticommute pairwise with $cF(\mathbf{e}_1)cF(\mathbf{e}_2) = i\,cF(\mathbf{e}_3)$.

**The multiplicative map.** The object the realization is built for is

$$
m(A) = A A^{\natural}, \qquad A \in I + \mathbb{B},
$$

the **multiplicative map** $m(A) = A A^{\natural}$, named after the complex absolute value. Its image consists of real matrices, and $m$ is multiplicative, $m(AB) = m(A)m(B)$. The reality is the point: for the matrices of the realization, $A^{\natural}$ commutes with $A$, so the product is real, and the read-off of the map is a quadratic map with no complex-linear analogue. What the corpus takes from the map is the existence of a *multiplicative* quadratic real map of this kind at all, next to the one it already owns: the operator of *Biquaternion 4×4 Regular Matrix Operator Representation* is the quadratic map of the same algebra that is **not** multiplicative, being a congruence rather than a product, and the two together show that the algebra carries a multiplicative and a non-multiplicative quadratic map.

## The Sixteen Products and the Biparavectors

The double centralizer of the earlier section says that the left and the right copies commute and that together they generate the whole endomorphism algebra. The basis that exhibits this is the set of products, and in the second realization it can be taken Hermitian.

**The products.** For the coordinate units put

$$
P_{ij} := \rho_L(e_i)\,\rho_R(e_j), \qquad i, j \in \{0, 1, 2, 3\}.
$$

In the second realization the right regular matrix is the transpose of the left, so $P_{ij}$ is the ordinary matrix product $\rho_L(e_i)\rho_L(e_j)^{\mathsf T}$; writing $E_i := \rho_L(e_i)$ for $i = 1, 2, 3$ and $E_0 = I$,

$$
P_{ij} = E_i E_j^{\mathsf T}.
$$

The three units satisfy $E_k^2 = I$ and anticommute pairwise, and their product is the complex structure of the realization, $E_1E_2 = iE_3$; the matrices $E_k$ are Hermitian, so $E_j^{\mathsf T}$ is its complex conjugate.

**Proposition (the sixteen products are an orthogonal basis).** The matrices $E_iE_j^{\mathsf T}$ are Hermitian, linearly independent over $\mathbb{C}$, and orthogonal under the trace, with a common normalisation:

$$
\operatorname{tr}\!\left(E_i E_j^{\mathsf T}\, E_k E_l^{\mathsf T}\right) = 4\,\delta_{ik}\delta_{jl}.
$$

This was checked entry by entry: the diagonal value is $4$ for each of the sixteen and every off-diagonal value is $0$. Independence follows, and the sixteen are a basis of $\mathbb{M}_4(\mathbb{C})$.

**The expansion.** By the orthogonality every complex matrix $M$ has the expansion

$$
M = \sum_{i,j} a_{ij}\,E_iE_j^{\mathsf T}, \qquad a_{ij} = \tfrac14\operatorname{tr}\!\left(M\,E_iE_j^{\mathsf T}\right),
$$

the coefficients being read off one at a time. Recomputing the expansion on a random complex $4 \times 4$ matrix returns it to $5 \times 10^{-16}$.

**Reading the expansion in the algebra.** The tensor square $\mathbb{B} \otimes_{\mathbb{C}} \mathbb{B}$ is spanned by the sixteen $e_i \otimes e_j$, and the expansion says that this space maps onto the endomorphisms of $\mathbb{B}$: the element $\sum a_{ij}\,e_i \otimes e_j$ is the linear transformation

$$
\tilde P \longmapsto \sum_{i,j} a_{ij}\, e_i \tilde P e_j,
$$

and every complex-linear transformation of the algebra arises this way. Such an element is a **biparavector** in the language of the paravector formulation. That the sixteen products already span the endomorphisms is the concrete form of the double centralizer: the left copy supplies the first index and the right copy the second, and the two fill $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ between them. Recomputing the action of the biparavector of a left–right sandwich $\tilde P \mapsto \tilde A\tilde P\tilde B$ against the sandwich itself returns $1.5 \times 10^{-14}$.

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

*Proof.* Direct computation of the sixteen operator matrices and comparison with the displays. The coordinate order is a genuine trap: the corpus's basis order is $(e_0,e_1,e_2,e_3)$, whereas the matrix displays put the scalar last, and in the corpus's order the same matrices appear shifted by one. Verified numerically: exact in the order $(e_1,e_2,e_3,e_0)$, and not in the order $(e_0,e_1,e_2,e_3)$.

**Remark (the source's sign).** The source writes the symmetric function with the two terms in the opposite order, $S\{s\}=\tfrac12 s[\,]s-D\{s_1^2,s_2^2,s_3^2\}$; its two displays of $S$ then differ by an overall sign. The corpus fixes the sign by the printed matrix, the one written here. $A\{a\}$ and $D\{d\}$ reproduce the source's displays exactly, with zero residual.

**Remark (the method degrades from three to four dimensions).** The antisymmetric, diagonal and diagonal-less symmetric functions exhaust the traceless part of $M_3(\mathbb C)$ in the order $(e_1,e_2,e_3,e_0)$, since each acts on the vector part and fixes the scalar. For a general traceless $\mathbb C^4\to\mathbb C^4$ map the same three families no longer suffice: the symmetric part needs a function that mixes the scalar and vector parts, and the source records that the expression for it is cumbersome and not useful. The four-dimensional unitary groups are therefore assembled from two $SO(4)$ factors rather than from a single quaternion closed form — the same asymmetry that the Lie-group article reads as the clean three-dimensional and less clean four-dimensional parametrizations.

## Summary

The left regular representation $\rho_L$ of *Introduction to the 4×4 Regular Matrix Representation of Biquaternions* is the algebra acting on itself on the left, with its Cayley matrix, its multiplicativity, its trace $4Q_0$ and its determinant $N(\tilde{Q})^2$ recorded there. Its transpose is the left matrix of the quaternion conjugate, $\rho_L(\tilde{Q})^{\mathsf{T}} = \rho_L(\tilde{Q}^{\natural})$.

The right regular representation $\rho_R(\tilde{Q})(\tilde{R}) = \tilde{R}\tilde{Q}$ is an anti-homomorphism and the regular representation of the opposite algebra. The naive identity $\rho_R(\tilde{Q}) = \rho_L(\tilde{Q})^{\mathsf{T}}$ is false — and the variant with $\tilde{Q}^{\natural}$ is the same statement, since $\rho_L(\tilde{Q}^{\natural})^{\mathsf{T}} = \rho_L(\tilde{Q})$ — while what holds is $\rho_R(\tilde{Q}) = D\rho_L(\tilde{Q})^{\mathsf{T}}D = D\rho_L(\tilde{Q}^{\natural})D$ with $D = \operatorname{diag}(-1,1,1,1)$. The difference $\rho_L - \rho_R$ vanishes exactly on the centre $\mathbb{C}_{\mathbb{B}}$, which is the precise sense in which left and right differ because the algebra is non-commutative.

The regular module is $\mathbb{B} = I_1 \oplus I_2$ with $I_1 = \mathbb{B}\tilde\Pi_1$, $I_2 = \mathbb{B}\tilde\Pi_2$ and $\tilde\Pi_1 = \tfrac{1}{2}(e_0 + ie_3)$, $\tilde\Pi_2 = \tfrac12(e_0 - ie_3)$; in the adapted basis $\tilde\Pi_1, e_1\tilde\Pi_1, \tilde\Pi_2, e_1\tilde\Pi_2$ the regular matrix is diagonal over the two invariant subspaces $I_1$, $I_2$, each a copy of the simple module $V$. So $\rho_L \cong V \oplus V$, the regular representation is reducible, and it is the first reducible realization of this subcategory. The centralizer of $\rho_L(\mathbb{B})$ is $\rho_R(\mathbb{B})$, the right copy, of complex dimension $4$. Over $\mathbb{R}$ the regular representation is $8 \times 8$ real with $\det = |N|^4$ and trace $8\operatorname{Re}(Q_0)$, the dimension doubling by restriction of scalars.

A second $4 \times 4$ realization, the one used in the literature on eigenvector bundles, is equivalent to $\rho_L$ as a module — every faithful four-dimensional complex realization is $V \oplus V$ — and it carries a multiplicative quadratic map $m(A) = A A^{\natural}$ to the real matrices which the regular realization does not have, in contrast with the congruence-shaped quadratic operator of *Biquaternion 4×4 Regular Matrix Operator Representation*. In that realization the sixteen products $\rho_L(e_i)\rho_R(e_j)$ are the Hermitian outer products $E_iE_j^{\mathsf T}$ and form a basis of $\mathbb{M}_4(\mathbb{C})$ orthogonal for the trace, $\operatorname{tr}(P_{ij}P_{kl}) = 4\delta_{ik}\delta_{jl}$; the expansion it gives is the tensor-square reading of the double centralizer, and it says that every complex-linear transformation of the algebra is a biparavector, the two-sided multiplication $\tilde P \mapsto \sum a_{ij}\,e_i\tilde P e_j$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | Biquaternion algebra |
| $e_0, e_1, e_2, e_3$ | Algebra basis, $e_0 = 1$, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ | Developed form, $Q_\mu \in \mathbb{C}$ |
| $Q^\mu = (Q^0, Q^1, Q^2, Q^3)$ | Four-vector; $Q^0 = Q_0$, $(Q^1, Q^2, Q^3) = (Q_1, Q_2, Q_3)$ |
| $\rho_L(\tilde{Q})$ | Matrix of left multiplication, the Cayley matrix of *Introduction to the 4×4 Regular Matrix Representation of Biquaternions* |
| $\rho_R(\tilde{Q})$ | Matrix of right multiplication |
| $D = \operatorname{diag}(-1,1,1,1)$ | Fixed sign matrix, $\rho_R(\tilde{Q}) = D\rho_L(\tilde{Q})^{\mathsf{T}}D$ |
| $N(\tilde{Q}) = \sum_\mu Q_\mu^2$ | The norm; $\det\rho_L(\tilde{Q}) = N(\tilde{Q})^2$ |
| ${}^{\natural}, \bar{\cdot}, {}^{*}, {}^{\flat}$ | Quaternion, complex, Hermitian and anti-Hermitian conjugations |
| $\mathbb{C}_{\mathbb{B}}$ | Centre, the scalar subspace $\mathbb{C} e_0$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real quaternion subalgebra; its restriction carries the quaternion regular representation of *Quaternion Element Representations* |
| $\tilde\Pi_1 = \tfrac{1}{2}(e_0 + ie_3)$, $\tilde\Pi_2 = \tfrac12(e_0 - ie_3)$ | Orthogonal idempotents, $\tilde\Pi_1 + \tilde\Pi_2 = e_0$, $\tilde\Pi_1\tilde\Pi_2 = 0$ |
| $I_1 = \mathbb{B}\tilde\Pi_1$, $I_2 = \mathbb{B}\tilde\Pi_2$ | The two minimal left ideals, $\mathbb{B} = I_1 \oplus I_2$ |
| $V = \mathbb{C}^2$ | Simple left $\mathbb{B}$-module, complex dimension $2$ |
| $\mathbb{B}^{\mathrm{op}}$ | Opposite algebra; $\rho_R$ is a homomorphism from it |
| $\epsilon^{ijk}$ | Levi-Civita symbol on the indices $1, 2, 3$ |
| $\operatorname{Res}_{\mathbb{C}/\mathbb{R}}$ | Restriction of scalars |
| $\operatorname{End}_{\mathbb{B}}(\mathbb{B}) = \rho_R(\mathbb{B})$ | Endomorphism algebra of the regular module |
| $\rho_L^{\mathbb{R}}(\tilde{Q})$ | Real $8 \times 8$ regular matrix |
| $\Phi'(A_0, A_1, A_2, A_3)$ | Second $4 \times 4$ realization, on the generators $ie_1, ie_2, ie_3$ with $(ie_1)^2 = (ie_2)^2 = (ie_3)^2 = e_0$ |
| $K_1, K_2, K_3$ | Coefficient conjugates of $ie_1, ie_2, ie_3$, used in the Hermitian basis of that realization |
| $m(A) = A A^{\natural}$ | The multiplicative map, $I + \mathbb{B} \to M_4(\mathbb{R})$; real and multiplicative |
| $P_{ij} = \rho_L(e_i)\rho_R(e_j) = E_iE_j^{\mathsf T}$ | The sixteen products; an orthogonal basis of $\mathbb{M}_4(\mathbb{C})$, $\operatorname{tr}(P_{ij}P_{kl}) = 4\delta_{ik}\delta_{jl}$ |
| $\sum a_{ij}\,e_i \otimes e_j$ | Biparavector, the two-sided transformation $\tilde P \mapsto \sum a_{ij}\,e_i\tilde P e_j$ |
| $\mathbb{M}_+$ | Hermitian subspace of real dimension $4$ |

## Further Reading

- *Introduction to the 4×4 Regular Matrix Representation of Biquaternions* (`articles_maths/introduction-to-the-4x4-regular-matrix-representation-of-biquaternions.md`), for the left regular operator, its Cayley matrix, the multiplicativity, the trace and the determinant, and the six subspace conditions

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the regular representation of an algebra and the identification of its endomorphism algebra.
- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Interscience, 1962), for the regular module, its decomposition into minimal left ideals and the double centralizer theorem.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules*, 2nd edition (Springer, 1992), for the regular module as a left module over itself and the centralizer of the left copy.
- William Fulton and Joe Harris, *Representation Theory: A First Course*, Graduate Texts in Mathematics 129 (Springer, 1991), for the regular representation as the direct sum of the simple modules with multiplicity equal to their dimensions.
- John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288 (Springer, 2021), for the regular representation of a quaternion algebra and its complexification.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the Cayley matrix of quaternion multiplication and its transpose.
- *The 4×4 Regular Matrix Representation under the Three Topologies* (`articles_maths/the-4x4-regular-matrix-representation-under-the-three-topologies.md`), for the matrix reading of the three forms and the structure attached to each.
- *Introduction to the 4×4 Regular Matrix Representation of Biquaternions* (`articles_maths/introduction-to-the-4x4-regular-matrix-representation-of-biquaternions.md`), for the regular matrix block diagonal in the basis of the two minimal left ideals, with the $2 \times 2$ matrix of the same element in each block, and for the six distinguished subspaces read in both models at once
- D. H. Gottlieb, "Eigenbundles, Quaternions, and Berry's Phase," arXiv:math/0304281 [math.AT] (2003), for the second $4 \times 4$ realization and the map $m(A) = A A^{\natural}$ of the section above; the paper's $4 \times 4$ matrices are Example 5 and the map $m(A) = A A^{\natural}$ is its section 5.
- D. H. Gottlieb, "Maxwell's equations" (1 August 2004, 12 pp.), for the matrix formulation of Maxwell's equations in which the field matrix is $A_0 I + cF$ of the realization above, the dual form in which the operators stand in the matrix and the field in the column, and the identity $\rho_R = \rho_L^{\mathsf{T}}$ which holds there without a sign matrix; cited for the identification of the second realization with the matrices of the Maxwell literature and for the transposition remark of that section. Its section 5 is the source of the sixteen-product basis and the biparavectors of the section above: the coefficient formula $a_{ij} = \tfrac14\operatorname{tr}(ME_iE_j^{\mathsf{T}})$, the orthogonality of the basis for the trace, and the reading of the products as the tensor square of the algebra acting on itself on both sides. The paper's potential-level equations (13) and (14) are recorded in *Maxwell's Equations in Biquaternionic Form* with their vector parts corrected.

- A. Gsponer, "Explicit closed-form parametrization of SU(3) and SU(4) in terms of complex quaternions and elementary functions," arXiv:math-ph/0211056v2, 2002, §2–4, for the Conway operators $e_n[\,]e_m$, the composition and association rules, the functions $A\{a\}$, $D\{d\}$, $S\{s\}$ and their $4\times4$ matrix displays (10′)–(13′), the rule $G^{-1}=G^{+\approx}=G^{\dagger}$ for the group elements, and the remark that the quaternion method loses power from three to four dimensions.
- A. W. Conway, "Quaternions and matrices," *Proceedings of the Royal Irish Academy* **A 50** (1945) 98–130, and J. L. Synge, "Quaternions, Lorentz transformations, and the Conway–Dirac–Eddington matrices," *Communications of the Dublin Institute for Advanced Studies* **A 21** (1972), for the Conway operator calculus in its original form.
