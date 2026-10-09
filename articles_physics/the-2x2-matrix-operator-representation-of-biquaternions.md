# __The 2×2 Matrix Operator Representation of Biquaternions__

## Introduction

Physically this is the realization in which the Lorentz transformation of a four-vector is the congruence of the Hermitian matrix that represents it, which is the standard matrix form of the transformation written elsewhere in the corpus with rotors.

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is the four-dimensional complex algebra with basis $e_0 = 1, e_1, e_2, e_3$, where $e_k^2 = -e_0$ and $e_1e_2 = e_3$, with central scalar imaginary $i$, and with general element $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$. The matrix realization $\Phi : \mathbb{B} \to M_2(\mathbb{C})$, with $\Phi(e_k) = -i\sigma_k$, $\det\Phi(\tilde{Q}) = N(\tilde{Q})$ and $\operatorname{Tr}\Phi(\tilde{Q}) = 2Q_0$, is that of *The 2×2 Matrix Element Representation of Biquaternions*, together with the simple module $V = \mathbb{C}^2$ on which the matrices act and which carries the two chiralities of the framework.

The element article answers *what is* $\tilde{Q}$ by displaying its matrix. This article answers *what does* $\tilde{Q}$ *do*, and it answers it in the smallest space that carries an action at all: the algebra is $M_2(\mathbb{C})$, and the Hermitian sandwich of *Biquaternion Rotations and Lorentz Transformations* acts on it by the **congruence**

$$
X \longmapsto M X M^{\dagger}, \qquad M = \Phi(\tilde{Q}) .
$$

This is the realization in which the operator is a single familiar operation of matrix algebra, and in which the two regimes of the operator — invertible congruence, or collapse — become the two cases of the rank of one matrix.

The article owns the identification of the sandwich with the congruence, the fact that $\Phi$ carries the dagger to the conjugate transpose, the preservation of rank, the scaling of the determinant, the preservation of the two Hermitian sectors, the positive Hermitian form attached to the identity, and the separation of the two regimes at the level of $\Phi(\tilde{Q})$, including the collapse of a null congruence onto one Hermitian line. The component computation of the same operator is *The Four-Vector Operator Representation of Biquaternions*; its matrix on the coefficient space, with the determinant $\lvert N\rvert^{4}$ and the trace $4\lvert Q_0\rvert^{2}$, is *The 4×4 Regular Matrix Operator Representation of Biquaternions*; the module side belongs to another coordinate system and is not repeated here. The module $V$ and the left action of the algebra on it are cited from the element article and not re-derived.

**Conventions.** The matrix of the element is $M = \Phi(\tilde{Q}) = \begin{pmatrix} Q_0 - iQ_3 & -iQ_1 - Q_2 \\ -iQ_1 + Q_2 & Q_0 + iQ_3 \end{pmatrix}$; the dagger on matrices is the conjugate transpose, written $M^{\dagger}$; the two Hermitian sectors are $\mathbb{M}_+$ and $\mathbb{M}_-$, whose images are the Hermitian and the skew-Hermitian matrices; and $V = \mathbb{C}^2$ is the simple module.

## The Congruence

**Lemma ($\Phi$ carries the dagger to the conjugate transpose).** For every $\tilde{Q}$,

$$
\Phi(\tilde{Q}^{*}) = \Phi(\tilde{Q})^{\dagger} .
$$

**Proof.** Both sides are conjugate-linear in $\tilde{Q}$ and additive, so it suffices to check the eight real basis elements. On $e_0$ both sides are $I_2$. On $e_k$ one has $e_k^{*} = -e_k$ and $\Phi(e_k)^{\dagger} = (-i\sigma_k)^{\dagger} = i\sigma_k^{\dagger} = i\sigma_k = \Phi(-e_k)$, since the Pauli matrices are Hermitian; so both sides are $i\sigma_k$. On $ie_0$ the left side is $\Phi(-ie_0) = -iI_2$ and the right is $(iI_2)^{\dagger} = -iI_2$. On $ie_k$, $(i(-i\sigma_k))^{\dagger} = (\sigma_k)^{\dagger} = \sigma_k$, which is also the left side. Hence the two agree on a basis.

**Theorem (the sandwich is the congruence by $M$).** Under $\Phi$, the sandwich of $\tilde{Q}$ is the congruence by $M = \Phi(\tilde{Q})$:

$$
\Phi\bigl(\operatorname{H}_{\tilde{Q}}(\tilde R)\bigr) = \Phi(\tilde{Q})\,\Phi(\tilde R)\,\Phi(\tilde{Q})^{\dagger} = M\,\Phi(\tilde R)\,M^{\dagger} .
$$

**Proof.** $\Phi$ is an algebra isomorphism, so $\Phi(\tilde{Q}\tilde R\tilde{Q}^{*}) = \Phi(\tilde{Q})\Phi(\tilde R)\Phi(\tilde{Q}^{*})$, and the lemma replaces the last factor by $M^{\dagger}$.

The operator on $M_2(\mathbb{C})$ is thus a **congruence**: the same matrix $M$ on the left and its conjugate transpose on the right. Three consequences are immediate and are the reason this realization is the clearest one.

The operator is $\mathbb{C}$-**linear** in $X$, because left and right multiplication by fixed matrices are linear. The coefficients of $\tilde{Q}$ enter through $M$ and $M^{\dagger}$, so the operator is quadratic in $\tilde{Q}$.

The operator is **not** a similarity unless $M$ is unitary: the two conjugating factors must be inverse for that, and $M^{\dagger} = M^{-1}$ is the unitarity condition, which is the matrix form of the fact that the sandwich is multiplicative exactly on the rotations.

The two-sided space is **four-dimensional over $\mathbb{C}$**, so the operator is an element of $\operatorname{End}_{\mathbb{C}}(M_2(\mathbb{C})) \cong M_4(\mathbb{C})$; that is the same four-dimensional carrier as in the coefficient realization, and the two matrices are conjugate, which is the content of *The 4×4 Regular Matrix Operator Representation of Biquaternions*.

## Rank, Determinant and the Hermitian Form

The congruence preserves the rank of its argument and scales its determinant, and both statements are the matrix forms of invariants of the operator.

**Proposition (rank and determinant under the congruence).** For every $\tilde R$ with image $\tilde T = \tilde{Q}\tilde R\tilde{Q}^{*}$,

$$
\operatorname{rank}\Phi(\tilde T) \leq \operatorname{rank}\Phi(\tilde R), \qquad\text{with equality if } N(\tilde{Q}) \neq 0,
$$

$$
\det\Phi(\tilde T) = \lvert\det M\rvert^{2}\det\Phi(\tilde R), \qquad\text{that is}\qquad N(\tilde T) = \langle\tilde T,\tilde T\rangle_{\natural} = \lvert N(\tilde{Q})\rvert^{2}N(\tilde R) .
$$

**Proof.** Left and right multiplication by any matrices cannot increase rank, and multiplication by invertible matrices on either side preserves it; that gives the rank statement off the light cone. For the determinant, $\det(MXM^{\dagger}) = \det M\cdot\det X\cdot\det M^{\dagger} = \lvert\det M\rvert^{2}\det X$ by multiplicativity, and $\det\Phi = N$ by the element article.

The rank of the congruence is limited by the rank of $M$ itself. A matrix of rank one can raise no rank, and this is the mechanism of the collapse: a null element has a rank-one matrix, so its congruence has image of rank at most one however large the rank of the argument.

The determinant identity is the interval statement of the framework in matrix form: the image of a four-vector has its interval multiplied by $\lvert N(\tilde{Q})\rvert^{2}$, which is $\lvert \det M\rvert^{2}$, and the interval is unchanged exactly when $M$ is unimodular, that is, on the unit-norm slice of the rotors.

**Proposition (the Hermitian form of the identity).** The image of $e_0$ under the sandwich is $\operatorname{H}_{\tilde{Q}}(e_0) = \tilde{Q}\tilde{Q}^{*}$, whose matrix is the Gram matrix

$$
M M^{\dagger} = \begin{pmatrix} \lvert M_{11}\rvert^{2} + \lvert M_{12}\rvert^{2} & M_{11}\bar{M}_{21} + M_{12}\bar{M}_{22} \\ M_{21}\bar{M}_{11} + M_{22}\bar{M}_{12} & \lvert M_{21}\rvert^{2} + \lvert M_{22}\rvert^{2} \end{pmatrix},
$$

which is positive semidefinite of rank $\operatorname{rank}M$, with

$$
\operatorname{Tr}\bigl(MM^{\dagger}\bigr) = 2\sum_{\mu=0}^{3}\lvert Q_\mu\rvert^{2} = 2\,\mathrm{Sc}\bigl(\tilde{Q}\tilde{Q}^{*}\bigr) .
$$

**Proof.** $MM^{\dagger}$ is a Gram matrix, hence positive semidefinite, and its rank equals the rank of $M$. Its trace is the sum of the squared moduli of the four entries; expanding the entries of $M = \Phi(\tilde{Q})$ gives $\lvert M_{11}\rvert^{2} + \lvert M_{22}\rvert^{2} = 2(\lvert Q_0\rvert^{2}+\lvert Q_3\rvert^{2})$ and $\lvert M_{12}\rvert^{2}+\lvert M_{21}\rvert^{2} = 2(\lvert Q_1\rvert^{2}+\lvert Q_2\rvert^{2})$, whose sum is twice the sum of the squared moduli of the coefficients. That sum is the scalar component of $\tilde{Q}\tilde{Q}^{*}$ by *The Four-Vector Operator Representation of Biquaternions*, and $\operatorname{Tr}\Phi(\cdot) = 2\,\mathrm{Sc}(\cdot)$ closes the computation.

**Corollary (the sectors).** The congruence maps the Hermitian matrices to the Hermitian matrices and the skew-Hermitian matrices to the skew-Hermitian matrices, because $(MXM^{\dagger})^{\dagger} = MXM^{\dagger}$ when $X^{\dagger} = X$ and $= -MXM^{\dagger}$ when $X^{\dagger} = -X$. These are the two sectors $\mathbb{M}_+$ and $\mathbb{M}_-$ of the algebra, and they are the only pair of the six distinguished subspaces that every congruence preserves. Physically, the material four-vectors are Hermitian matrices of a definite sign pattern and the congruence is the action of the group of units on them, which is why the four-vector transformation and the matrix congruence are the same statement.

## The Case $N(\tilde{Q}) \neq 0$

**Theorem (the invertible congruence).** Let $N(\tilde{Q}) \neq 0$. Then $M$ is invertible, the congruence $X \mapsto MXM^{\dagger}$ is a bijection of $M_2(\mathbb{C})$ that preserves the rank of every matrix, the operator has rank $4$ on the four-dimensional space, and $\det = \lvert N(\tilde{Q})\rvert^{4}$, $\operatorname{Tr} = 4\lvert Q_0\rvert^{2}$.

**Proof.** $M$ is invertible because $\det M = N(\tilde{Q}) \neq 0$; the inverse congruence is $X \mapsto M^{-1}X(M^{\dagger})^{-1}$, so the map is a bijection; multiplication by an invertible matrix on either side preserves rank, so rank is preserved, the strata of $M_2(\mathbb{C})$ being the zero matrix, the nonzero matrices of rank one, and the full-rank matrices; the rank and the invariants are *The 4×4 Regular Matrix Operator Representation of Biquaternions*.

The matrix $M$ has two eigenvalues $\lambda_1, \lambda_2$, nonzero in this case, and the operator has the four eigenvalues $\lambda_i\bar{\lambda}_j$; the determinant is their product and the trace their sum. The congruence preserves the rank, so each rank stratum of $M_2(\mathbb{C})$ — the zero matrix, the nonzero matrices of rank one, and the full-rank matrices — is carried into itself, and the operator on the four-dimensional matrix space has rank $4$ in this case.

**Example.** For $\tilde{Q} = e_0 + e_1$ one has $N = 2$, $M = \begin{pmatrix} 1 & -i \\ -i & 1 \end{pmatrix}$, of determinant $2$ and eigenvalues $1 \pm i$. The congruence is invertible, the operator has eigenvalues $\{(1+i)(1-i), (1+i)^{2}, (1-i)^{2}, (1-i)(1+i)\} = \{2, 2i, -2i, 2\}$, of determinant $16 = \lvert N\rvert^{4}$ and trace $4 = 4\lvert Q_0\rvert^{2}$. The same four eigenvalues appear as the spectrum of the $4 \times 4$ operator matrix of the coefficient realization for the same operand, as the conjugacy of the two matrices requires.

**Example (a physical boost).** For the rotor $\tilde{Q} = \tfrac53e_0 + \tfrac43ie_3$, of norm one, one has $M = \mathrm{diag}(3,\tfrac13)$ and the congruence is $X \mapsto \mathrm{diag}(3,\tfrac13)X\,\mathrm{diag}(3,\tfrac13)$, which multiplies the diagonal entries by $9$ and $\tfrac19$ and leaves the off-diagonal ones alone: the eigenvalue $9 = e^{\psi}$ with $\psi = 2\ln 3$ is the doubled rapidity, the operand storing the half-rapidity $e^{\psi/2} = 3$, and the trace of the operator is $\tfrac{100}{9} = 4\lvert Q_0\rvert^{2}$.

On the unit-norm slice the congruence by $M \in SL(2,\mathbb{C})$ is the action of the double cover on the Hermitian matrices, and on the four-vectors it is the proper orthochronous Lorentz transformation; the kernel is $\{\pm I_2\}$, which is the double cover. The geometric statement is *Biquaternion Rotations and Lorentz Transformations*.

## The Case $N(\tilde{Q}) = 0$

On the light cone the matrix $M$ has rank one, and a congruence by a rank-one matrix annihilates everything except one line.

**Theorem (the collapse of a null congruence).** Let $N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 0$ and $\tilde{Q} \neq 0$, so that $\operatorname{rank}M = 1$. Write $M = uv^{\dagger}$ with nonzero column vectors $u, v \in \mathbb{C}^{2}$. Then for every $X$,

$$
M X M^{\dagger} = \bigl(v^{\dagger}Xv\bigr)\, u\,u^{\dagger} .
$$

Consequently the image of the congruence is the single complex line $\mathbb{C}\, uu^{\dagger}$ spanned by the rank-one **Hermitian** matrix $uu^{\dagger}$, the operator has rank $1$, and

$$
\operatorname{H}_{\tilde{Q}} \circ \operatorname{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2}\,\operatorname{H}_{\tilde{Q}} .
$$

The element corresponding to the Hermitian matrix $uu^{\dagger}$, normalised, is a minimal idempotent of $\mathbb{B}$; the operator is nilpotent when $Q_0 = 0$ and a scaled projection when $Q_0 \neq 0$.

**Proof.** $MXM^{\dagger} = uv^{\dagger}X(vu^{\dagger}) = u(v^{\dagger}Xv)u^{\dagger}$, the parenthesis being a scalar; so every image is a multiple of $uu^{\dagger}$, which is nonzero and Hermitian, and the image has complex dimension one. The rank statement and the square are *The 4×4 Regular Matrix Operator Representation of Biquaternions*, and the identification of $uu^{\dagger}$ with a minimal idempotent is the statement that an idempotent of $M_2(\mathbb{C})$ is a rank-one projection.

**Example (nilpotent).** For $\tilde{Q} = e_1 + ie_2$, a zero divisor with $Q_0 = 0$,

$$
M = \begin{pmatrix} 0 & -2i \\ 0 & 0 \end{pmatrix} = uv^{\dagger}, \qquad u = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad v = \begin{pmatrix} 0 \\ 2i \end{pmatrix},
$$

and the congruences of the four matrix units are

$$
E_{11} \mapsto 0, \qquad E_{12} \mapsto 0, \qquad E_{21} \mapsto 0, \qquad E_{22} \mapsto 4E_{11} ,
$$

so the image is the line $\mathbb{C}E_{11} = \mathbb{C}\Phi(\tilde\Pi_1)$ with $\tilde\Pi_1 = \tfrac12(e_0 + ie_3)$, and the image depends on $X$ only through its second diagonal entry, since $v^{\dagger}Xv = 4X_{22}$. The operator has trace $0$ and all four eigenvalues zero: it is nilpotent, and the collapse is the loss of rank, not the vanishing of the entries of a diagonal.

**Example (projection).** For $\tilde{Q} = \tfrac12(e_0 - ie_3) = \tilde\Pi_2$, Hermitian, of norm zero and scalar part $\tfrac12$,

$$
M = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} = E_{22} = uv^{\dagger}, \qquad u = v = \begin{pmatrix} 0 \\ 1 \end{pmatrix},
$$

and the congruence sends $X$ to $X_{22}E_{22}$: it is exactly the projection onto the line of the idempotent $\tilde\Pi_2$. The trace of the operator is $4\lvert\tfrac12\rvert^{2} = 1$ and its square is itself. The same idempotent appears as the generator of the image in the four-vector realization, where the operator was found to send $\tilde R$ to $(R^0 + iR^3)\tilde\Pi_2$.

The two examples separate the two faces of the cone exactly as in the other realizations: both matrices have rank one and determinant zero, both congruences have a one-dimensional image spanned by a rank-one Hermitian matrix, and the value of the trace $4\lvert Q_0\rvert^{2}$ decides whether the surviving operator is nilpotent or a projection. The element $e_2 + ie_3$, a third null operand, has $M = \begin{pmatrix} 1 & -1 \\ 1 & -1 \end{pmatrix} = uv^{\dagger}$ with $u = (1,1)$ and $v = (1,-1)$, of scalar part zero, and its image is again the line of a minimal idempotent, this time $\tfrac12(e_0 + ie_1)$.

**Reading (the collapse as decoherence).** The rank-one congruence is the algebraic shape of information loss. Off the cone the matrix $M$ is invertible and the congruence is a bijection, so the transformation of the material sector is reversible; on the cone the image is a single Hermitian line, so every operand is mapped to a multiple of one idempotent and the distinctions between operands are erased. Read as a process, the collapse is an **irreversible** map — the rank drop is the loss of information — and the two faces of the cone are the two ends of it: the nilpotent operand ($Q_0 = 0$) annihilates, and the projection ($Q_0 \neq 0$) projects onto a fixed line, the minimal idempotent that the corpus reads as a single-mode vacuum. The reading is **phenomenological** and is labelled as such: here the loss is **geometric**, the nullness of the operand, and is not produced by tracing over an environment. The framework's own algebraic reading of decoherence as an idempotent projection is *Decoherence as Idempotent Projection*, and the vacuum identification is *The Biquaternion Vacuum as a Minimal Idempotent*; this article supplies the operator shape that both read.

**Reading (the congruence is a completely positive map).** The congruence $X\mapsto M X M^{\dagger}$ has the form $\sum_k A_k X A_k^{\dagger}$ with a single Kraus operator, $A = M$, so it is a **completely positive** map — the algebraic shape of a quantum channel or a measurement. Read physically, the sandwich is the operator form of a completely positive map on the state space, and the operand is the Kraus operator that defines it. The reading has a sharp condition and a sharp boundary. The map is **trace-preserving**, hence a genuine channel, exactly when $M$ is unitary, that is for the rotations; otherwise it is a positive map that rescales the trace. On the cone, where $M$ has rank one, the map is a **destructive measurement**: it projects onto a single line and destroys every other distinction, which is the rank-one collapse of the preceding reading. The algebra supplies the completely positive form and the unitarity condition and no probability rule for the outcomes.

## Physical Readings

The congruence reads as the Lorentz action on the Hermitian matrix that carries a four-vector, and it is the smallest form in which a change of frame can be computed. Read for invariance, a congruence preserves the signature, which is why the sign of the interval is frame-invariant while its normalisation is not, and why the probability form is the one the congruence cannot reach at all. Read on the clock, the matrix image of the central imaginary is a scalar matrix, which is the matrix reason that the exchange commutes with every change of frame.

## Summary

In the matrix realization the operator is a congruence. The map $\Phi$ carries the Hermitian conjugate to the conjugate transpose, so the sandwich $\operatorname{H}_{\tilde{Q}}(\tilde R) = \tilde{Q}\tilde R\tilde{Q}^{*}$ becomes

$$
X \longmapsto M X M^{\dagger}, \qquad M = \Phi(\tilde{Q}) \in M_2(\mathbb{C}),
$$

a single familiar operation, linear in the argument and quadratic in the operand, and a similarity exactly when $M$ is unitary, that is, for the rotations. It preserves the two Hermitian sectors, because $(MXM^{\dagger})^{\dagger} = MXM^{\dagger}$ or its negative according to the sector of $X$, and it scales the determinant by $\lvert\det M\rvert^{2}$, which is the interval identity $N(\tilde T) = \langle\tilde T,\tilde T\rangle_{\natural} = \lvert N(\tilde{Q})\rvert^{2}N(\tilde R)$. The image of the identity is the Gram matrix $MM^{\dagger}$, positive semidefinite of rank $\operatorname{rank}M$.

The two regimes are the two ranks of $M$. Off the light cone $M$ is invertible, the congruence is a bijection preserving the four ranks of the two-by-two matrices, and the operator has rank $4$, determinant $\lvert N(\tilde{Q})\rvert^{4}$ and trace $4\lvert Q_0\rvert^{2}$, with the spectrum $\lambda_i\bar{\lambda}_j$ read from the eigenvalues of $M$. On the light cone $M = uv^{\dagger}$ has rank one and the congruence collapses the whole matrix algebra onto the single Hermitian line $\mathbb{C}uu^{\dagger}$, the line of a minimal idempotent: the operator has rank one, its square is $4\lvert Q_0\rvert^{2}$ times itself, and it is nilpotent for $Q_0 = 0$ and a scaled projection otherwise. The worked null operands $e_1 + ie_2$, $\tilde\Pi_2$ and $e_2 + ie_3$ show the three cases of the collapse, with images the lines of $\tilde\Pi_1$, $\tilde\Pi_2$ and $\tfrac12(e_0 + ie_1)$. The boost rotor $\tfrac53e_0 + \tfrac43ie_3$ shows the invertible case, with the half-rapidity of the operand appearing as the doubled rapidity of the congruence.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M = \Phi(\tilde{Q})$ | the matrix of the operand, $\det M = N(\tilde{Q})$, $\operatorname{Tr}M = 2Q_0$ |
| $\Phi(\tilde{Q}^{*}) = \Phi(\tilde{Q})^{\dagger}$ | $\Phi$ carries the dagger to the conjugate transpose |
| $X \mapsto MXM^{\dagger}$ | the sandwich as a congruence |
| $MM^{\dagger} = \Phi(\tilde{Q}\tilde{Q}^{*})$ | the image of the identity; the Gram matrix of $M$ |
| $\operatorname{rank}\Phi(\tilde{Q}\tilde R\tilde{Q}^{*}) \leq \operatorname{rank}\Phi(\tilde R)$ | rank never increases; preserved off the cone |
| $\det(MXM^{\dagger}) = \lvert\det M\rvert^{2}\det X$ | the determinant scales; $N(\tilde T) = \langle\tilde T,\tilde T\rangle_{\natural} = \lvert N(\tilde{Q})\rvert^{2}N(\tilde R)$ |
| $\operatorname{rank}\operatorname{H}_{\tilde{Q}} = (\operatorname{rank}M)^{2}$ | $4$ off the cone, $1$ on it, $0$ only at $\tilde{Q} = 0$ |
| $M = uv^{\dagger} \Rightarrow MXM^{\dagger} = (v^{\dagger}Xv)uu^{\dagger}$ | the collapse of a null congruence onto one Hermitian line |
| $uu^{\dagger} \leftrightarrow \tfrac12(e_0 + i\mathbf{n}\cdot\mathbf{e})$ | the generator of the image line is a minimal idempotent |
| $4\lvert Q_0\rvert^{2}$ | trace of the operator; vanishes exactly for the nilpotent case |
| $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ |
| $\langle\tilde{P},\tilde{Q}\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{P}\tilde{Q})$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2nd ed. 2013), for congruence, rank preservation under left and right multiplication, Gram matrices and rank-one projections.
- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge, 1991), for the eigenvalue products of a congruence and the singular value decomposition.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the identification of the biquaternion algebra with $M_2(\mathbb{C})$ and of its Hermitian elements with Hermitian matrices.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the Lorentz action written as a matrix congruence and the double cover $SL(2,\mathbb{C}) \to SO^{+}(1,3)$.
