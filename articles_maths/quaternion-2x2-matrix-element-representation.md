# __Quaternion 2x2 Matrix Element Representation__

## Introduction

The quaternion algebra has no faithful representation by real $2\times2$ matrices, but it has a faithful representation by complex ones, $\iota:\mathbb{H}\to M_2(\mathbb{C})$, whose image is a four-dimensional real subspace of the complex matrix algebra. This article develops that representation. It gives the images of the basis, the trace and the determinant, the inner product and the Euclidean norm, the matrix form of quaternion conjugation, the images of the scalar and vector subspaces, and the reason there is no real $2\times2$ representation.

The article depends on *Quaternion Algebra* for the basis and relations, on *Quaternion Norm and Invertibility* for the quaternion norm and the invertibility criterion, and on *The Scalar and Vector Subspaces of $\mathbb{H}$* for the two subspaces. The larger matrix representation is in *Quaternion 4x4 Matrix Element Representation $M_4(\mathbb{R})_L$*, and the coordinate description of the product in *Quaternion Four-Vector Element Representation*. The Clifford identification of the complex matrix algebra is sketched in *Quaternion Other Algebraic Element Representations*.

Throughout, $\mathbb{H}$ is the quaternion algebra with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, $e_1e_2 = e_3$; a quaternion is $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ with real $q_\mu$; the conjugate is $\tilde{q}^{\natural} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$ and the quaternion norm is $N(\tilde q) = \tilde q\tilde{q}^{\natural}$. The Pauli matrices are

$$
\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad
\sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad
\sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},
$$

with $i$ the imaginary unit of $\mathbb{C}$.

## The Representation by Complex Matrices

**Definition.** The **matrix representation** of the quaternion algebra is the real-linear map

$$
\iota : \mathbb{H}\longrightarrow M_2(\mathbb{C}), \qquad \iota(\tilde q) = q_0 I - i(q_1\sigma_1+q_2\sigma_2+q_3\sigma_3).
$$

**Theorem.** The map $\iota$ is an injective algebra homomorphism, and $\iota(\mathbb{H})$ is a four-dimensional real subspace of $M_2(\mathbb{C})$.

*Proof.* The Pauli matrices satisfy $\sigma_j\sigma_k = \delta_{jk}I + i\sum_l\epsilon_{jkl}\sigma_l$, which is the quaternion multiplication rule under the correspondence $e_k\leftrightarrow -i\sigma_k$, so $\iota$ is multiplicative; the four images are real-linearly independent, so $\iota$ is injective, and the image has real dimension four.

**Corollary.** On a quaternion,

$$
\iota(\tilde q) = \begin{pmatrix} q_0-iq_3 & -iq_1-q_2 \\ -iq_1+q_2 & q_0+iq_3 \end{pmatrix}.
$$

**Remark (the choice).** The correspondence $e_k\mapsto-i\sigma_k$ is the corpus's choice, held fixed once and for all. It is not canonical: another representation differs from this one by conjugation by an invertible matrix, and all the invariants below are unchanged. The Pauli matrices appear only as a shorthand for the images of $e_1,e_2,e_3$.

**Corollary.** The images of the basis are, up to the factor $-i$, the Pauli matrices, and the image of the quaternion algebra is the set

$$
\left\{ \begin{pmatrix} A & B \\ -\bar B & \bar A \end{pmatrix} : A, B\in\mathbb{C} \right\},
$$

a four-dimensional real subspace of $M_2(\mathbb{C})$.

*Proof.* Write $A = q_0-iq_3$, $B = -iq_1-q_2$ for real $q_\mu$; then the lower-left entry is $-i q_1+q_2 = -\bar B$ and the lower-right is $q_0+iq_3 = \bar A$. Conversely every such matrix arises from the real quadruple $(q_0,q_1,q_2,q_3) = (\operatorname{Re}A, -\operatorname{Re}B, -\operatorname{Im}B, -\operatorname{Im}A)$.

## Trace and Determinant

**Theorem.** For every quaternion,

$$
\operatorname{tr}\iota(\tilde q) = 2q_0, \qquad \det \iota(\tilde q) = q_0^2+q_1^2+q_2^2+q_3^2 = N(\tilde q).
$$

*Proof.* The trace is the sum of the diagonal entries $q_0-iq_3$ and $q_0+iq_3$, namely $2q_0$. The determinant is

$$
(q_0-iq_3)(q_0+iq_3) - (-iq_1-q_2)(-iq_1+q_2) = (q_0^2+q_3^2) - (-q_1^2-q_2^2) = \sum_\mu q_\mu^2 .
$$

**Corollary.** An element $\tilde q$ is a unit exactly when $\det\iota(\tilde q)\neq0$, and then $\iota(\tilde q^{-1}) = \iota(\tilde q)^{-1}$; the matrix image of the unit group $\mathbb{H}^{\times}$ is the set of matrices in $\iota(\mathbb{H})$ of non-zero determinant, and the image of the norm-one subgroup $Sp(1)$ is the group of matrices in $\iota(\mathbb{H})$ of determinant $1$.

*Proof.* Invertibility is non-vanishing norm by *Quaternion Norm and Invertibility*, and the determinant is the quaternion norm; multiplicativity of $\iota$ gives $\iota(\tilde q^{-1}) = \iota(\tilde q)^{-1}$. A norm-one element has $N(\tilde q) = 1$, so its determinant is $1$, and conversely a determinant-$1$ matrix in $\iota(\mathbb{H})$ is the image of a norm-one element.

**Theorem.** The restriction of $\iota$ to the unit sphere is an isomorphism of groups

$$
Sp(1)\cong SU(2),
$$

where $SU(2)$ is the group of $2\times2$ complex unitary matrices of determinant one.

*Proof.* By the corollary the image of $Sp(1)$ is the set of matrices in $\iota(\mathbb{H})$ that are unitary of determinant one, and this set is $SU(2)$: it is contained in $SU(2)$ by definition, and the two are three-dimensional connected groups, so the containment is an equality. The map $\iota$ is injective and multiplicative, so it restricts to a group isomorphism.

**Remark.** The trace is twice the scalar coordinate and the determinant is the whole norm. This is the matrix expression of the facts that the scalar subspace has dimension one and that the trace of a pure quaternion image vanishes.

## The Inner Product and the Euclidean Norm

**Definition.** The **inner product** of two quaternions is $\langle p,\tilde q\rangle = \mathrm{Sc}(p\tilde{q}^{\natural})$; the **Euclidean norm** is $|\tilde q| = \sqrt{N(\tilde q)}$. The one-variable expression $\tilde q\tilde{q}^{\natural}$ is the **Hermitian form**, which here coincides with the quaternion norm.

**Theorem.** The matrix image intertwines the quaternion norm and the determinant and the inner product and the Frobenius form:

$$
N(\tilde q) = \det\iota(\tilde q), \qquad \operatorname{tr}\bigl(\iota(p)\iota(\tilde q)^{\dagger}\bigr) = 2\,\langle p,\tilde q\rangle, \qquad \operatorname{tr}\bigl(\iota(\tilde q)\iota(\tilde q)^{\dagger}\bigr) = 2\,|\tilde q|^2,
$$

where $\dagger$ is the conjugate transpose.

*Proof.* The determinant identity is the determinant theorem. For the trace identities, note that transposition combined with conjugation of the entries reverses the signs of the three vector coordinates, so

$$
\iota(\tilde q)^{\dagger} = \iota(\tilde{q}^{\natural}).
$$

Hence $\iota(\tilde q)^{\dagger}\iota(\tilde q) = \iota(\tilde{q}^{\natural} \tilde q) = \iota(N(\tilde q)) = N(\tilde q)I$, whose trace is $2N(\tilde q) = 2|\tilde q|^2$; and $\iota(p)\iota(\tilde q)^{\dagger} = \iota(p\tilde{q}^{\natural})$, whose trace is $2\mathrm{Sc}(p\tilde{q}^{\natural}) = 2\langle p,\tilde q\rangle$.

**Corollary.** The image $\iota(\mathbb{H})$ consists of those matrices $\iota(\tilde q)$ for which $\iota(\tilde q)^\dagger\iota(\tilde q)$ is a scalar matrix, namely $|\tilde q|^2 I$; the map $\tilde q\mapsto |\tilde q|^{-1}\iota(\tilde q)$ for $\tilde q\neq0$ is an isometric embedding of the unit sphere $Sp(1)$ into the unitary group $U(2)$.

*Proof.* $\iota(\tilde q)^\dagger\iota(\tilde q) = \iota(\tilde{q}^{\natural})\iota(\tilde q) = \iota(\tilde{q}^{\natural} \tilde q) = \iota(N(\tilde q)) = N(\tilde q)I$, so the columns of $\iota(\tilde q)$ are orthogonal and of equal length $|\tilde q|$; after normalising, $\iota(\tilde q)$ is unitary.

## The Conjugations in Matrix Form

**Theorem.** Quaternion conjugation is the adjugate:

$$
\iota(\tilde{q}^{\natural}) = \operatorname{adj}\iota(\tilde q) = \begin{pmatrix} q_0+iq_3 & iq_1+q_2 \\ iq_1-q_2 & q_0-iq_3 \end{pmatrix}.
$$

*Proof.* For a $2\times2$ matrix $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ the adjugate is $\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$. Applying this to $\iota(\tilde q)$ gives the displayed matrix, which is $\iota(q_0-q_1e_1-q_2e_2-q_3e_3) = \iota(\tilde{q}^{\natural})$.

**Definition.** The **antisymmetric form** is

$$
\epsilon = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = i\sigma_2 = -\iota(e_2), \qquad \epsilon^{T} = -\epsilon, \quad \epsilon^2 = -I .
$$

**Theorem.** Quaternion conjugation is transposition dressed with the antisymmetric form:

$$
\iota(\tilde{q}^{\natural}) = \epsilon\,\iota(\tilde q)^{T}\,\epsilon^{-1}.
$$

*Proof.* Compute $\epsilon M^{T}\epsilon^{-1}$ for $M = \iota(\tilde q)$ with $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$. Since $\epsilon^{-1} = -\epsilon$, one has $\epsilon M^{T}\epsilon^{-1} = -\epsilon M^{T}\epsilon$, and a direct multiplication gives $\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$, which is the adjugate of $M$ and equals $\iota(\tilde{q}^{\natural})$ by the preceding theorem.

Here the coefficients are real, so no complex conjugation of entries enters, and the single relation above is the whole correspondence.

## The Scalar and Vector Subspaces in Matrix Form

**Theorem.** Under $\iota$ the scalar subspace is the space of scalar matrices with real entries and the vector subspace is the space of traceless matrices:

$$
\iota(\mathbb{R}_{\mathbb{H}}) = \mathbb{R}\,I, \qquad
\iota(\operatorname{Im}\mathbb{H}) = \left\{ M\in\iota(\mathbb{H}) : \operatorname{tr}M = 0 \right\}.
$$

*Proof.* A scalar $s$ maps to $sI$, whose trace is $2s$ and which is scalar; a pure quaternion $\vec q$ maps to $-i(q_1\sigma_1+q_2\sigma_2+q_3\sigma_3)$, a traceless matrix. The trace vanishes exactly when $q_0 = 0$, the vector condition.

**Corollary.** In matrix terms the decomposition is the splitting of $\iota(\mathbb{H})$ into its scalar part and its traceless part; the scalar subspace is the one-dimensional centre and the vector subspace the three-dimensional traceless summand.

*Proof.* The splitting $M = \tfrac12(\operatorname{tr}M)I + (M-\tfrac12(\operatorname{tr}M)I)$ separates the scalar and traceless parts, and the image of a quaternion under $\iota$ has trace twice its scalar coordinate. For the quaternion $2+3\mathbf{i}+4\mathbf{j}+5\mathbf{k}$ the two pieces are

$$
\iota(2+3\mathbf{i}+4\mathbf{j}+5\mathbf{k})=\begin{pmatrix}2-5i&-4-3i\\4-3i&2+5i\end{pmatrix},\qquad \operatorname{tr}=4 ,
$$

$$
\mathbb{R}I\text{-part}=2I=\begin{pmatrix}2&0\\0&2\end{pmatrix},\qquad
\text{traceless part}=\begin{pmatrix}-5i&-4-3i\\4-3i&5i\end{pmatrix},
$$

the second of trace $0$, the two adding to the image.

## A Worked Image

**Example.** For the element

$$
\tilde q = 1 + 2e_1 - e_2 + 3e_3
$$

the matrix image is

$$
\iota(\tilde q) = \begin{pmatrix} 1-3i & 1-2i \\ -1-2i & 1+3i \end{pmatrix},
$$

with

$$
\operatorname{tr}\iota(\tilde q) = 2 = 2q_0, \qquad \det\iota(\tilde q) = (1-3i)(1+3i) - (1-2i)(-1-2i) = 10 - (-5) = 15 = N(\tilde q).
$$

The determinant is the quaternion norm and the trace is twice the scalar part, as the general theorem requires.

## The Absence of a $2\times2$ Real Representation

**Theorem.** There is no injective algebra homomorphism $\mathbb{H}\to M_2(\mathbb{R})$.

*Proof.* Suppose $\varphi : \mathbb{H}\to M_2(\mathbb{R})$ were injective. Then its image is a four-dimensional subalgebra of the four-dimensional algebra $M_2(\mathbb{R})$, hence all of $M_2(\mathbb{R})$, so $\mathbb{H}$ would be isomorphic to $M_2(\mathbb{R})$. But $M_2(\mathbb{R})$ has zero divisors — the matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ is non-zero and squares to zero — while $\mathbb{H}$ has none, a contradiction.

**Corollary.** The quaternion algebra is not isomorphic to any full matrix algebra over $\mathbb{R}$, and the smallest faithful matrix representation over $\mathbb{R}$ is the four-dimensional one $L : \mathbb{H}\to M_4(\mathbb{R})$ of *Quaternion 4x4 Matrix Element Representation $M_4(\mathbb{R})_L$*.

*Proof.* The first statement is the theorem; a faithful representation makes $F^n$ a module over the division algebra $\mathbb{H}$, so $F^n\cong\mathbb{H}^k$ and $n$ is a multiple of $\dim_F\mathbb{H} = 4$, whence the minimal faithful real representation is the left regular one $L : \mathbb{H}\to M_4(F)$.

## Summary

The image $\iota(\mathbb{H})$ is the four-dimensional real space of matrices $\begin{pmatrix} A & B \\ -\bar B & \bar A \end{pmatrix}$, on which the quaternion norm is the determinant and the inner product matches half the Frobenius form, $\operatorname{tr}(\iota(\tilde q)\iota(\tilde q)^\dagger) = 2|\tilde q|^2$.

The trace of an image is twice the scalar coordinate and the determinant is the quaternion norm, $N(\tilde q) = \sum_\mu q_\mu^2$, so invertibility is non-vanishing determinant. Quaternion conjugation is the adjugate, equivalently the antisymmetric-form-dressed transpose $\iota(\tilde{q}^{\natural}) = \epsilon\iota(\tilde q)^{T}\epsilon^{-1}$ with $\epsilon = i\sigma_2$; the scalar subspace maps to the real scalar matrices and the vector subspace to the traceless matrices.

There is no injective homomorphism $\mathbb{H}\to M_2(\mathbb{R})$, because its image would be all of $M_2(\mathbb{R})$, which has zero divisors while $\mathbb{H}$ has none; the smallest real representation is the $4\times4$ regular one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Basis, $e_k^2 = -e_0$ |
| $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ | Quaternion, conjugate $\tilde{q}^{\natural}$, norm $N(\tilde q)$ |
| $\iota : \mathbb{H}\to M_2(\mathbb{C})$ | Injective matrix representation of the algebra |
| $\sigma_1,\sigma_2,\sigma_3$ | Pauli matrices; $\iota(e_k) = -i\sigma_k$ |
| $\operatorname{tr}\iota(\tilde q) = 2q_0$ | Trace image of the scalar coordinate |
| $\det \iota(\tilde q) = N(\tilde q)$ | Determinant image of the quaternion norm |
| $\dagger$ | Conjugate transpose; $\operatorname{tr}(\iota(\tilde q)\iota(\tilde q)^\dagger) = 2\lvert \tilde q\rvert^2$ |
| $\epsilon = i\sigma_2 = -\iota(e_2)$ | Antisymmetric form; $\iota(\tilde{q}^{\natural}) = \epsilon\iota(\tilde q)^{T}\epsilon^{-1}$ |
| $\mathbb{R}_{\mathbb{H}}, \operatorname{Im}\mathbb{H}$ | Scalar matrices and traceless matrices |

## Further Reading

- Bartel Leendert van der Waerden, *Algebra*, Vol. II (Springer, 1955), for the structure of matrix algebras.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the matrix representation of central simple algebras and the Brauer group.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the Pauli-matrix realization of the quaternion algebra.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for matrix algebras, idempotents and the absence of a real $2\times2$ representation.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the structure of matrix algebras and simple rings.
