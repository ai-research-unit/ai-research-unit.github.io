
# __Quaternion 2x2 Matrix Representation__

## Introduction

The quaternion algebra has no faithful representation by real $2\times2$ matrices, but it has a faithful representation by complex ones, and the representation becomes an isomorphism after complexification: $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C})$. This article develops that representation. It gives the isomorphism, the images of the basis, the trace and the determinant, the inner product and the Euclidean norm, the matrix form of quaternion conjugation, the images of the scalar and vector subspaces, and the reason there is no real $2\times2$ representation. It is the quaternion member of the family's small-matrix pair; the counterpart is the $2\times2$ complex representation of the biquaternion algebra, which is an isomorphism already over $\mathbb{C}$ because the algebra itself is complex.

The article depends on *Quaternion Algebra* for the basis and relations, on *Quaternion Norm and Invertibility* for the quaternion norm and the invertibility criterion, and on *The Scalar and Vector Subspaces of $\mathbb{H}$* for the two subspaces. The larger matrix representation is in *Quaternion 4x4 Regular Matrix Representation*, and the coordinate description of the product in *Quaternion Four-Vector Representation*. The Clifford identification of the complexification is sketched in *Quaternion Other Algebraic Representations*.

The corpus's default base is a commutative ring with identity. The representation by complex matrices is stated over $\mathbb{R}$ and then over $\mathbb{C}$ after scalar extension; the quaternion norm is positive definite over $\mathbb{R}$, and the determinant statements are the algebraic identities that remain valid after extending the coefficient field.

Throughout, $\mathbb{H}$ is the quaternion algebra with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, $e_1e_2 = e_3$; a quaternion is $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ with real $q_\mu$ in the definite statements; the conjugate is $\bar{\tilde q} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$ and the quaternion norm is $N(\tilde q) = \tilde q\bar{\tilde q}$. The Pauli matrices are

$$
\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad
\sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad
\sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},
$$

with $i$ the imaginary unit of $\mathbb{C}$.

## The Complexification

**Definition.** The **complexification** of the quaternion algebra is the $\mathbb{C}$-algebra $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}$, the scalar extension of $\mathbb{H}$ from $\mathbb{R}$ to $\mathbb{C}$, with the same basis $e_0,e_1,e_2,e_3$ and the same relations, the coefficients now taken in $\mathbb{C}$.

**Proposition.** The complexification is a four-dimensional $\mathbb{C}$-algebra, hence an eight-dimensional real algebra, and it is the complex quaternion algebra; the central imaginary unit of the extension is $i$ itself, which commutes with the $e_k$.

*Proof.* The tensor product of a four-dimensional real algebra with $\mathbb{C}$ is four-dimensional over $\mathbb{C}$; the element $i = 1\otimes i$ is central and satisfies $i^2 = -1$.

**Theorem.** The complexification of the quaternion algebra is the full matrix algebra,

$$
\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C}),
$$

an isomorphism of $\mathbb{C}$-algebras.

*Proof.* The $\mathbb{R}$-linear map $\iota : \mathbb{H}\to M_2(\mathbb{C})$ given by $\iota(\tilde q) = q_0I - i(q_1\sigma_1+q_2\sigma_2+q_3\sigma_3)$ is multiplicative, since the Pauli matrices satisfy $\sigma_j\sigma_k = \delta_{jk}I + i\sum_l\epsilon_{jkl}\sigma_l$, which is the quaternion multiplication rule under the correspondence $e_k\leftrightarrow -i\sigma_k$. It is injective with four-dimensional real image, so its $\mathbb{C}$-linear extension $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\to M_2(\mathbb{C})$ is a surjective map of four-dimensional $\mathbb{C}$-algebras, hence an isomorphism.

**Definition.** In the general element $\tilde Q = \sum_\mu Q_\mu e_\mu$ of the complexification the coefficients $Q_\mu$ lie in $\mathbb{C}$; the map $\Phi : \mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\to M_2(\mathbb{C})$ extends $\iota$ by $\mathbb{C}$-linearity.

## The Images of the Basis

**Theorem.** The isomorphism $\Phi$ can be fixed by

$$
\Phi(e_0) = I, \quad \Phi(e_1) = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}, \quad \Phi(e_2) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \quad \Phi(e_3) = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix},
$$

so that on a general element

$$
\Phi(\tilde Q) = Q_0 I - i(Q_1\sigma_1+Q_2\sigma_2+Q_3\sigma_3) = \begin{pmatrix} Q_0-iQ_3 & -iQ_1-Q_2 \\ -iQ_1+Q_2 & Q_0+iQ_3 \end{pmatrix}.
$$

*Proof.* The four images satisfy the quaternion relations, as the basis relations are checked directly: $\Phi(e_1)^2 = -I$, $\Phi(e_2)^2 = -I$, $\Phi(e_3)^2 = -I$ and $\Phi(e_1)\Phi(e_2) = \Phi(e_3)$, with the reversed products negative; the four images are linearly independent over $\mathbb{C}$, so the extension is an isomorphism.

**Remark (the choice).** The correspondence $e_k\mapsto-i\sigma_k$ is the corpus's choice, held fixed once and for all. It is not canonical: another isomorphism differs from this one by conjugation by an invertible matrix, and all the invariants below are unchanged. The Pauli matrices appear only as a shorthand for the images of $e_1,e_2,e_3$.

**Corollary.** The images of the basis are, up to the factor $-i$, the Pauli matrices, and the image of the real quaternion algebra $\iota(\mathbb{H})$ is the set

$$
\left\{ \begin{pmatrix} z & w \\ -\bar w & \bar z \end{pmatrix} : z, w\in\mathbb{C} \right\},
$$

a four-dimensional real subspace of $M_2(\mathbb{C})$.

*Proof.* Write $z = q_0-iq_3$, $w = -iq_1-q_2$ for real $q_\mu$; then the lower-left entry is $-i q_1+q_2 = -\bar w$ and the lower-right is $q_0+iq_3 = \bar z$. Conversely every such matrix arises from the real quadruple $(q_0,q_1,q_2,q_3) = (\operatorname{Re}z, -\operatorname{Re}w, -\operatorname{Im}w, -\operatorname{Im}z)$.

## Trace and Determinant

**Theorem.** For every element of the complexification,

$$
\operatorname{tr}\Phi(\tilde Q) = 2Q_0, \qquad \det\Phi(\tilde Q) = Q_0^2+Q_1^2+Q_2^2+Q_3^2 = N(\tilde Q).
$$

*Proof.* The trace is the sum of the diagonal entries $Q_0-iQ_3$ and $Q_0+iQ_3$, namely $2Q_0$. The determinant is

$$
(Q_0-iQ_3)(Q_0+iQ_3) - (-iQ_1-Q_2)(-iQ_1+Q_2) = (Q_0^2+Q_3^2) - (-Q_1^2-Q_2^2) = \sum_\mu Q_\mu^2 .
$$

**Corollary.** Over $\mathbb{R}$ an element $\tilde q$ is a unit exactly when $\det\iota(\tilde q)\neq0$, and then $\iota(\tilde q^{-1}) = \iota(\tilde q)^{-1}$; the matrix image of the unit group $\mathbb{H}^{\times}$ is the set of matrices in $\iota(\mathbb{H})$ of non-zero determinant, and the image of the norm-one subgroup $Sp(1)$ is the group of matrices in $\iota(\mathbb{H})$ of determinant $1$.

*Proof.* Invertibility is non-vanishing norm by *Quaternion Norm and Invertibility*, and the determinant is the quaternion norm; multiplicativity of $\iota$ gives $\iota(\tilde q^{-1}) = \iota(\tilde q)^{-1}$. A norm-one element has $N(\tilde q) = 1$, so its determinant is $1$, and conversely a determinant-$1$ matrix in $\iota(\mathbb{H})$ is the image of a norm-one element.

**Theorem.** The restriction of $\iota$ to the unit sphere is an isomorphism of groups

$$
Sp(1)\cong SU(2),
$$

where $SU(2)$ is the group of $2\times2$ complex unitary matrices of determinant one.

*Proof.* By the corollary the image of $Sp(1)$ is the set of matrices in $\iota(\mathbb{H})$ that are unitary of determinant one, and this set is $SU(2)$: it is contained in $SU(2)$ by definition, and the two are three-dimensional connected groups, so the containment is an equality. The map $\iota$ is injective and multiplicative, so it restricts to a group isomorphism.

**Remark.** The trace is twice the scalar coordinate and the determinant is the whole norm. This is the matrix expression of the facts that the scalar subspace has dimension one and that the trace of a pure quaternion image vanishes.

## The Inner Product and the Euclidean Norm

**Definition.** The **inner product** of two quaternions is $\langle p,\tilde q\rangle = \mathrm{Sc}(p\bar{\tilde q})$; the **Euclidean norm** is $|\tilde q| = \sqrt{N(\tilde q)}$. The one-variable expression $\tilde q\bar{\tilde q}$ is the **Hermitian form**, which here coincides with the quaternion norm.

**Theorem.** The matrix image intertwines the quaternion norm and the determinant and the inner product and the Frobenius form:

$$
N(\tilde q) = \det\iota(\tilde q), \qquad \operatorname{tr}\bigl(\iota(p)\iota(\tilde q)^{\dagger}\bigr) = 2\,\langle p,\tilde q\rangle, \qquad \operatorname{tr}\bigl(\iota(\tilde q)\iota(\tilde q)^{\dagger}\bigr) = 2\,|\tilde q|^2,
$$

where ${}^{\dagger}$ is the conjugate transpose.

*Proof.* The determinant identity is the determinant theorem. For the trace identities, note that for a matrix with real quaternion coefficients, transposition combined with conjugation of the entries reverses the signs of the three vector coordinates, so

$$
\iota(\tilde q)^{\dagger} = \iota(\bar{\tilde q}).
$$

Hence $\iota(\tilde q)^{\dagger}\iota(\tilde q) = \iota(\bar{\tilde q} \tilde q) = \iota(N(\tilde q)) = N(\tilde q)I$, whose trace is $2N(\tilde q) = 2|\tilde q|^2$; and $\iota(p)\iota(\tilde q)^{\dagger} = \iota(p\bar{\tilde q})$, whose trace is $2\mathrm{Sc}(p\bar{\tilde q}) = 2\langle p,\tilde q\rangle$.

**Corollary.** The image $\iota(\mathbb{H})$ consists of those matrices $\iota(\tilde q)$ for which $\iota(\tilde q)^\dagger\iota(\tilde q)$ is a scalar matrix, namely $|\tilde q|^2 I$; the map $\tilde q\mapsto |\tilde q|^{-1}\iota(\tilde q)$ for $\tilde q\neq0$ is an isometric embedding of the unit sphere $Sp(1)$ into the unitary group $U(2)$.

*Proof.* $\iota(\tilde q)^\dagger\iota(\tilde q) = \iota(\bar{\tilde q})\iota(\tilde q) = \iota(\bar{\tilde q} \tilde q) = \iota(N(\tilde q)) = N(\tilde q)I$, so the columns of $\iota(\tilde q)$ are orthogonal and of equal length $|\tilde q|$; after normalising, $\iota(\tilde q)$ is unitary.

## The Conjugations in Matrix Form

**Theorem.** Quaternion conjugation is the adjugate:

$$
\iota(\bar{\tilde q}) = \operatorname{adj}\iota(\tilde q) = \begin{pmatrix} q_0+iq_3 & iq_1+q_2 \\ iq_1-q_2 & q_0-iq_3 \end{pmatrix}.
$$

*Proof.* For a $2\times2$ matrix $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ the adjugate is $\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$. Applying this to $\iota(\tilde q)$ gives the displayed matrix, which is $\iota(q_0-q_1e_1-q_2e_2-q_3e_3) = \iota(\bar{\tilde q})$.

**Definition.** The **antisymmetric form** is

$$
\epsilon = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = i\sigma_2 = -\Phi(e_2), \qquad \epsilon^{T} = -\epsilon, \quad \epsilon^2 = -I .
$$

**Theorem.** Quaternion conjugation is transposition dressed with the antisymmetric form:

$$
\iota(\bar{\tilde q}) = \epsilon\,\iota(\tilde q)^{T}\,\epsilon^{-1}.
$$

*Proof.* Compute $\epsilon M^{T}\epsilon^{-1}$ for $M = \iota(\tilde q)$ with $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$. Since $\epsilon^{-1} = -\epsilon$, one has $\epsilon M^{T}\epsilon^{-1} = -\epsilon M^{T}\epsilon$, and a direct multiplication gives $\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$, which is the adjugate of $M$ and equals $\iota(\bar{\tilde q})$ by the preceding theorem.

**Remark.** Unlike the biquaternion case there is only one conjugation of the algebra to realise, namely quaternion conjugation, and it is the adjugate; the antisymmetric form is needed to write it as a dressed transposition because the matrix realisation uses the same $i$ that conjugates coefficients. Here the coefficients are real, so no complex conjugation of entries enters, and the single relation above is the whole correspondence.

## The Scalar and Vector Subspaces in Matrix Form

**Theorem.** Under $\iota$ the scalar subspace is the space of scalar matrices with real entries and the vector subspace is the space of traceless matrices:

$$
\iota(\mathbb{R}_{\mathbb{H}}) = \mathbb{R}\,I, \qquad
\iota(\operatorname{Im}\mathbb{H}) = \left\{ M\in\iota(\mathbb{H}) : \operatorname{tr}M = 0 \right\}.
$$

*Proof.* A scalar $s$ maps to $sI$, whose trace is $2s$ and which is scalar; a pure quaternion $\mathbf{q}$ maps to $-i(q_1\sigma_1+q_2\sigma_2+q_3\sigma_3)$, a traceless matrix. The trace vanishes exactly when $Q_0 = 0$, the vector condition.

**Corollary.** In matrix terms the decomposition is the splitting of $\iota(\mathbb{H})$ into its scalar part and its traceless part, and after complexification the algebra splits as $M_2(\mathbb{C}) = \mathbb{C}I\oplus\mathrm{SL}_2(\mathbb{C})$; the scalar subspace is the one-dimensional centre and the vector subspace the three-dimensional traceless summand.

*Proof.* The splitting $M = \tfrac12(\operatorname{tr}M)I + (M-\tfrac12(\operatorname{tr}M)I)$ separates the scalar and traceless parts, and the image of a quaternion under $\iota$ has trace twice its scalar coordinate.

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

**Corollary.** The quaternion algebra is not isomorphic to any full matrix algebra over $\mathbb{R}$, and the smallest faithful matrix representation over $\mathbb{R}$ is the four-dimensional one $L : \mathbb{H}\to M_4(\mathbb{R})$ of *Quaternion 4x4 Regular Matrix Representation*. The $2\times2$ representation exists only after the coefficient field is enlarged to $\mathbb{C}$.

*Proof.* The first statement is the theorem; a faithful representation makes $F^n$ a module over the division algebra $\mathbb{H}$, so $F^n\cong\mathbb{H}^k$ and $n$ is a multiple of $\dim_F\mathbb{H} = 4$, whence the minimal faithful real representation is the left regular one $L : \mathbb{H}\to M_4(F)$.

## Comparison with the Biquaternion and Split-Biquaternion Cases

**Theorem.** The biquaternion algebra is isomorphic to the matrix algebra over its own centre,

$$
\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C}),
$$

and it therefore has a $2\times2$ matrix representation over a commutative ring without any extension of coefficients.

*Proof.* The biquaternion algebra is the complexification of the quaternion algebra, so the isomorphism of this article is an equality of the algebra with $M_2(\mathbb{C})$.

**Theorem.** The split biquaternion algebra $\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$ is not isomorphic to a full $2\times2$ matrix algebra over any commutative ring.

*Proof.* The split-complex numbers decompose as $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$ through the idempotents $\Pi_\pm = \tfrac12(1\pm j)$, so $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$. A ring of the form $M_2(k)$ with $k$ commutative has no non-trivial central idempotent, since its centre is the scalar matrices; the product $\mathbb{H}\oplus\mathbb{H}$ has the two central idempotents $(1,0)$ and $(0,1)$. Hence $\mathbb{H}_{\mathbb{D}}$ is not isomorphic to any $M_2(k)$.

| Feature | $\mathbb{H}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|
| Algebra | division algebra | $\cong M_2(\mathbb{C})$ | $\cong\mathbb{H}\oplus\mathbb{H}$ |
| $2\times2$ representation | only over $\mathbb{C}$ | over $\mathbb{C}$, directly | none over a commutative ring |
| Determinant image | $N(\tilde q) = \sum q_\mu^2$ | $N(\tilde Q) = \sum Q_\mu^2$ | componentwise |
| Zero divisors | none | singular matrices | present in each summand |

The pattern is that a $2\times2$ matrix realisation over a commutative ring exists exactly when the algebra is a full matrix algebra over that ring. The quaternion algebra becomes one only after complexification, the biquaternion algebra already is one, and the split biquaternion algebra never is: its decomposition into two division algebras is exactly what prevents it. The biquaternion account is in *Biquaternion 2×2 Matrix Representation*.

## Summary

The complexification $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}$ is a four-dimensional complex algebra isomorphic to $M_2(\mathbb{C})$, through the map sending $e_0\mapsto I$ and $e_k\mapsto-i\sigma_k$, with $\Phi(\tilde Q) = Q_0I-i\sum_k Q_k\sigma_k$; the choice is fixed once and is not canonical. The trace of an image is twice the scalar coordinate and the determinant is the quaternion norm, $N(\tilde Q) = \sum_\mu Q_\mu^2$, so invertibility over $\mathbb{R}$ is non-vanishing determinant, and the determinant is a perfect square no longer: over $\mathbb{C}$ it is an arbitrary complex number.

The image of the real quaternion algebra is the four-dimensional real space of matrices $\begin{pmatrix} z & w \\ -\bar w & \bar z \end{pmatrix}$, on which the quaternion norm is the determinant and the inner product matches half the Frobenius form, $\operatorname{tr}(\iota(\tilde q)\iota(\tilde q)^\dagger) = 2|\tilde q|^2$. Quaternion conjugation is the adjugate, equivalently the antisymmetric-form-dressed transpose $\iota(\bar{\tilde q}) = \epsilon\iota(\tilde q)^{T}\epsilon^{-1}$ with $\epsilon = i\sigma_2$; the scalar subspace maps to the real scalar matrices and the vector subspace to the traceless matrices, giving $M_2(\mathbb{C}) = \mathbb{C}I\oplus\mathrm{SL}_2(\mathbb{C})$ after complexification.

There is no injective homomorphism $\mathbb{H}\to M_2(\mathbb{R})$, because its image would be all of $M_2(\mathbb{R})$, which has zero divisors while $\mathbb{H}$ has none; the smallest real representation is the $4\times4$ regular one. The biquaternion algebra is $M_2(\mathbb{C})$ without extension of coefficients, and the split biquaternion algebra is $\mathbb{H}\oplus\mathbb{H}$, whose central idempotents rule out a $2\times2$ matrix realisation over any commutative ring.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Basis, $e_k^2 = -e_0$ |
| $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ | Quaternion, conjugate $\bar{\tilde q}$, norm $N(\tilde q)$ |
| $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}$ | Complexification, $\cong M_2(\mathbb{C})$ |
| $\iota : \mathbb{H}\to M_2(\mathbb{C})$ | Matrix representation of the real algebra |
| $\Phi : \mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\to M_2(\mathbb{C})$ | The $\mathbb{C}$-algebra isomorphism |
| $\sigma_1,\sigma_2,\sigma_3$ | Pauli matrices; $\Phi(e_k) = -i\sigma_k$ |
| $\operatorname{tr}\Phi(\tilde Q) = 2Q_0$ | Trace image of the scalar coordinate |
| $\det\Phi(\tilde Q) = N(\tilde Q)$ | Determinant image of the quaternion norm |
| $\dagger$ | Conjugate transpose; $\operatorname{tr}(\iota(\tilde q)\iota(\tilde q)^\dagger) = 2\lvert \tilde q\rvert^2$ |
| $\epsilon = i\sigma_2 = -\Phi(e_2)$ | Antisymmetric form; $\iota(\bar{\tilde q}) = \epsilon\iota(\tilde q)^{T}\epsilon^{-1}$ |
| $\mathbb{R}_{\mathbb{H}}, \operatorname{Im}\mathbb{H}$ | Scalar matrices and traceless matrices |
| $\mathrm{SL}_2(\mathbb{C})$ | Traceless matrices, the vector image in the complexification |
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$ | Split biquaternion algebra, $\cong\mathbb{H}\oplus\mathbb{H}$, no $2\times2$ realisation |

## Further Reading

- Bartel Leendert van der Waerden, *Algebra*, Vol. II (Springer, 1955), for the complexification of algebras and the structure of matrix algebras.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the matrix representation of central simple algebras and the Brauer group.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the Pauli-matrix realization of the quaternion algebra and its complexification.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for matrix algebras, idempotents and the absence of a real $2\times2$ representation.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the structure of matrix algebras and simple rings.
