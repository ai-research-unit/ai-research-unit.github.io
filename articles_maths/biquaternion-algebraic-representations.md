# __Biquaternion Algebraic Representations__

## Introduction

The basic algebra article defined the biquaternion algebra $\mathbb{B}$, its conjugations, and its six distinguished real subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, and $\mathbb{M}_-$. This article describes the **algebraic representations** of the biquaternion algebra: concrete ways of writing biquaternions as objects we can compute with, using only the algebra operations and the underlying vector space structure.

The word "representation" is used here in the sense of "a concrete realization of the algebra as a collection of computable objects." It is not used in the technical sense of algebra representation theory, in which a representation of an algebra $A$ is a vector space $V$ together with an algebra homomorphism $\rho : A \to \mathrm{End}(V)$. The two uses are related — the spinor representation below is a representation in both senses — but they are not the same. We use the word in the first sense throughout.

The word "algebraic" is used to contrast with "polar." The representations in this article use only the algebra operations, the scalar imaginary, and the underlying complex vector space structure. They do not use the exponential, the roots of $-1$, or any analytic construction. The polar representations, which do use the exponential and the roots of $-1$, are treated in the companion article on biquaternion polar representations.

The representations we discuss in this article are:

1. **Complex four-vector representation.** A biquaternion as a complex four-vector.
2. **$2 \times 2$ matrix representation.** A biquaternion as a $2 \times 2$ complex matrix.
3. **Spinor representation.** A biquaternion as an operator on two-component spinors.
4. **Clifford algebra representation.** A biquaternion as an element of the even Clifford algebra $\mathrm{Cl}_{1,3}^+$.

Throughout, we use the notation of the basic algebra article: a biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3,
$$

or, more compactly, as

$$
\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu, \qquad Q_\mu \in \mathbb{C},
$$

with $e_0 = 1$ and $e_1, e_2, e_3$ the quaternion units. The scalar imaginary is $i$, which commutes with the quaternion units. Each complex coefficient is written $Q_\mu = q_\mu + i q'_\mu$ with $q_\mu, q'_\mu \in \mathbb{R}$.

## The Complex Four-Vector Representation

### Definition

A biquaternion $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ can be written as a complex four-vector

$$
Q^\mu = (Q^0, Q^1, Q^2, Q^3),
$$

with

$$
Q^0 = Q_0, \qquad (Q^1, Q^2, Q^3) = (Q_1, Q_2, Q_3).
$$

The scalar part of the biquaternion becomes the time component of the four-vector; the vector part becomes the spatial components. This is the most direct representation.

### Multiplication in Four-Vector Form

The product of two biquaternions in four-vector form separates into a scalar part and a vector part:

$$
(\tilde{Q} \circ \tilde{R})^0 = Q^0 R^0 - \sum_{k=1}^{3} Q^k R^k,
$$

$$
(\tilde{Q} \circ \tilde{R})^i = Q^0 R^i + R^0 Q^i + \sum_{j,k=1}^{3} \epsilon^{i j k} Q^j R^k, \qquad i = 1, 2, 3,
$$

where $\epsilon^{i j k}$ is the Levi-Civita symbol on the spatial indices $1, 2, 3$. The time component of the product is the scalar part; the spatial components are the vector part. This is the four-vector expression of the quaternion product formula.

### Conjugation in Four-Vector Form

Quaternion conjugation negates the spatial components:

$$
\bar{Q}^\mu = (Q^0, -Q^1, -Q^2, -Q^3).
$$

Complex conjugation conjugates all components:

$$
(Q^*)^\mu = ((Q^0)^*, (Q^1)^*, (Q^2)^*, (Q^3)^*).
$$

Hermitian conjugation combines the two:

$$
(Q^\dagger)^\mu = ((Q^0)^*, -(Q^1)^*, -(Q^2)^*, -(Q^3)^*).
$$

### The Six Subspaces in Four-Vector Form

The six distinguished subspaces have a simple characterization in the four-vector representation, each condition being read off from the conjugation rules of the preceding section: the centre by $Q^1 = Q^2 = Q^3 = 0$, the vector subspace by $Q^0 = 0$, the quaternion and anti-quaternion subspaces by the four coefficients being all real or all purely imaginary, and the two sectors by the scalar coefficient being real with the vector coefficients purely imaginary, or the reverse. The six are developed one at a time in the **Subspaces** group of the series, *Biquaternion Centre Subspace* and its companions, with their coordinate conditions, bases and intersections collected in *Biquaternion Relations Between Subspaces*.

### The Norm Form in Four-Vector Form

The norm form $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ is

$$
N(\tilde{Q}) = (Q^0)^2 + (Q^1)^2 + (Q^2)^2 + (Q^3)^2.
$$

On the anti-Hermitian subspace $\mathbb{M}_-$, the norm form restricts to

$$
N(\tilde{Q}) = -(q'_0)^2 + q_1^2 + q_2^2 + q_3^2,
$$

which is the indefinite quadratic form of signature $(3,1)$: three positive directions and one negative. On the Hermitian subspace $\mathbb{M}_+$ the same form reads $q_0^2 - (q'_1)^2 - (q'_2)^2 - (q'_3)^2$, of signature $(1,3)$, and the two signs are exchanged by multiplication by $i$, since $N(i\tilde{Q}) = -N(\tilde{Q})$. It is this indefinite form that is invariant under the linear transformations preserving the quadratic form.

### Why the Four-Vector Representation Is Useful

The four-vector representation is the bridge between the algebraic biquaternion and the standard tensor formalism. It is the representation in which:

- The group of linear transformations preserving the indefinite quadratic form acts in the standard way.
- The indefinite quadratic form on $\mathbb{M}_-$ is expressed as a Lorentzian norm.
- The differential operator $\partial_\mu \partial^\mu$ associated with the indefinite form is defined.

It is also the representation in which the biquaternion looks least like a biquaternion. The algebraic structure — the non-commutative product, the two conjugations, the zero divisors — is hidden. This is why the four-vector representation, while useful, is not the fundamental one.

## The $2 \times 2$ Matrix Representation

### Definition

The biquaternion algebra is isomorphic to the algebra of $2 \times 2$ complex matrices:

$$
\mathbb{B} \cong M_2(\mathbb{C}).
$$

An explicit isomorphism is given by mapping the quaternion units to the matrices

$$
e_0 \mapsto \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \quad
e_1 \mapsto \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}, \quad
e_2 \mapsto \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \quad
e_3 \mapsto \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix}.
$$

Each of these matrices squares to $-I$, and they satisfy the quaternion multiplication rules. (Verification: with $e_1 \mapsto -i\sigma_1$, $e_2 \mapsto -i\sigma_2$, $e_3 \mapsto -i\sigma_3$, we have $e_1 e_2 \mapsto (-i\sigma_1)(-i\sigma_2) = -\sigma_1\sigma_2 = -i\sigma_3$, which is the image of $e_3$.)

The map extends to an algebra isomorphism $\mathbb{B} \to M_2(\mathbb{C})$, under which a biquaternion $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ maps to the matrix

$$
\Phi(\tilde{Q}) = \begin{pmatrix} Q_0 - i Q_3 & -i Q_1 - Q_2 \\ -i Q_1 + Q_2 & Q_0 + i Q_3 \end{pmatrix}.
$$

The isomorphism is written $\Phi$ throughout, and its four basis images are $\Phi(e_0) = I$, $\Phi(e_k) = -i\sigma_k$ for $k = 1, 2, 3$, with the scalar imaginary acting as $\Phi(i\tilde{Q}) = i\,\Phi(\tilde{Q})$. The assignment is fixed by these four images, and the residual freedom is a unitary change of basis of $\mathbb{C}^2$ and nothing further.

### The Trace and Determinant

Two invariants of the matrix representation are particularly important.

**Trace.** The trace of the matrix is

$$
\mathrm{Tr}(\tilde{Q}) = (Q_0 - i Q_3) + (Q_0 + i Q_3) = 2 Q_0.
$$

So the trace is twice the scalar part of the biquaternion. It transforms under the four conjugations as

$$
\mathrm{Tr}(\bar{\tilde{Q}}) = \mathrm{Tr}(\tilde{Q}), \qquad \mathrm{Tr}(\tilde{Q}^*) = (\mathrm{Tr}(\tilde{Q}))^*,
$$

$$
\mathrm{Tr}(\tilde{Q}^\dagger) = (\mathrm{Tr}(\tilde{Q}))^*, \qquad \mathrm{Tr}(\tilde{Q}^\flat) = -(\mathrm{Tr}(\tilde{Q}))^*.
$$

So the trace is invariant under quaternion conjugation, complex-conjugated under complex and Hermitian conjugation, and negated-and-conjugated under anti-Hermitian conjugation.

**Determinant.** The determinant of the matrix is

$$
\det(\tilde{Q}) = (Q_0 - i Q_3)(Q_0 + i Q_3) - (-i Q_1 - Q_2)(-i Q_1 + Q_2)
$$

$$
= (Q_0^2 + Q_3^2) - [(-i Q_1)^2 - Q_2^2] = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = N(\tilde{Q}).
$$

So the determinant is the **norm form** of the biquaternion. This is a crucial fact: the norm form, which we defined algebraically as $\tilde{Q}\bar{\tilde{Q}}$, is exactly the determinant of the corresponding matrix. In particular, the norm form is multiplicative because the determinant is multiplicative.

### The Hermitian Form

The **Hermitian form** of the biquaternion is the biquaternion

$$
\tilde{Q}\tilde{Q}^\dagger.
$$

This is a Hermitian element of $\mathbb{B}$, not a real scalar in general: its scalar part is non-negative, but its vector part need not vanish. For example, for $\tilde{Q} = e_1 + i e_2$, one has $\tilde{Q}^\dagger = -e_1 + i e_2$ and $\tilde{Q}\tilde{Q}^\dagger = 2 e_0 + 2 i e_3$, which has a nonzero vector part.

**Scalar part.** The scalar part of the Hermitian form is

$$
\mathrm{Sc}\!\left(\tilde{Q}\tilde{Q}^\dagger\right) = \sum_{\mu=0}^{3} |Q_\mu|^2 = \sum_{\mu=0}^{3}(q_\mu^2 + q'^2_\mu).
$$

This is a **non-negative real number**, and it vanishes if and only if $\tilde{Q} = 0$.

**Trace.** In the matrix representation, the trace of the Hermitian form is

$$
\mathrm{Tr}\!\left(\tilde{Q}\tilde{Q}^\dagger\right) = 2 \sum_{\mu=0}^{3} |Q_\mu|^2.
$$

This is twice the scalar part. It also equals the **sum of the squared moduli of the four entries of the matrix**, i.e., the Frobenius norm squared of the matrix:

$$
\mathrm{Tr}\!\left(\tilde{Q}\tilde{Q}^\dagger\right) = |Q_0 - i Q_3|^2 + |Q_0 + i Q_3|^2 + |-i Q_1 - Q_2|^2 + |-i Q_1 + Q_2|^2 = \|M\|_F^2.
$$

**Euclidean norm.** The Euclidean norm of the biquaternion is defined from the scalar part of the Hermitian form:

$$
\|\tilde{Q}\|_E = \sqrt{\mathrm{Sc}\!\left(\tilde{Q}\tilde{Q}^\dagger\right)} = \sqrt{\sum_{\mu=0}^{3} |Q_\mu|^2}.
$$

This is a genuine norm on the real vector space $\mathbb{B} \cong \mathbb{R}^8$: positive-definite, subadditive, and homogeneous of degree one. It is **not** multiplicative with respect to the biquaternion product.

### Conjugation in Matrix Form

**Quaternion conjugation** $\bar{\tilde{Q}}$ corresponds to the matrix

$$
\Phi(\bar{\tilde{Q}}) = \begin{pmatrix} Q_0 + i Q_3 & i Q_1 + Q_2 \\ i Q_1 - Q_2 & Q_0 - i Q_3 \end{pmatrix},
$$

which is the **adjugate** (or classical adjoint) of the matrix: it is the matrix whose entries are the cofactors of the original matrix.

**Complex conjugation** $\tilde{Q}^*$ does **not** act entrywise on the matrix. The representation is built with the same $i$ that conjugates the coefficients, so the two operations compete: conjugating the entries of $M(\tilde{Q})$ sends $-i\sigma_1 \mapsto +i\sigma_1$, the image of $e_1$ to its negative, while the image of $e_2$ is preserved. Entrywise conjugation of $M(\tilde{Q})$ is therefore not $M(\tilde{Q}^*)$, and it is not the image of any of the four involutions. The correct correspondence dresses the conjugation with the antisymmetric form $\epsilon = i\sigma_2$:

$$
\Phi(\tilde{Q}^*) = \epsilon\,\overline{\Phi(\tilde{Q})}\,\epsilon^{-1}, \qquad \epsilon = i\sigma_2 = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = \Phi(-e_2).
$$

With the same $\epsilon$, quaternion conjugation reads $\Phi(\bar{\tilde{Q}}) = \epsilon\,\Phi(\tilde{Q})^{\mathsf{T}}\epsilon^{-1}$, which is the adjugate statement above, since $\epsilon M^{\mathsf{T}}\epsilon^{-1} = \mathrm{adj}(M)$ for $2 \times 2$ matrices.

**Hermitian conjugation** $\tilde{Q}^\dagger$ is the conjugate transpose of the matrix:

$$
\Phi(\tilde{Q}^\dagger) = \begin{pmatrix} Q_0^* + i Q_3^* & i Q_1^* + Q_2^* \\ i Q_1^* - Q_2^* & Q_0^* - i Q_3^* \end{pmatrix} = \begin{pmatrix} \overline{Q_0 - i Q_3} & \overline{-i Q_1 + Q_2} \\ \overline{-i Q_1 - Q_2} & \overline{Q_0 + i Q_3} \end{pmatrix}.
$$

**Anti-Hermitian conjugation** $\tilde{Q}^\flat = -\tilde{Q}^\dagger$ is the negative of the conjugate transpose.

### The Six Subspaces in Matrix Form

The six distinguished subspaces have a simple characterization in the matrix representation: the centre consists of the scalar matrices, the vector subspace of the traceless matrices, the quaternion and anti-quaternion subspaces of the two quaternion patterns of the matrix realization, and the two sectors of the Hermitian and the anti-Hermitian matrices. Each is developed in the **Subspaces** group of the series, and its matrix image is the subject of the corresponding section of its article in that group.

The identifications of $\mathbb{M}_+$ with the Hermitian matrices and $\mathbb{M}_-$ with the anti-Hermitian matrices follow directly from the isomorphism: if $\tilde{Q}$ maps to $M$, then $\tilde{Q}^\dagger$ maps to $M^\dagger$ (the conjugate transpose). Indeed, the imaginary quaternion units satisfy $\Phi(i e_k) = \sigma_k$, and the Pauli matrices $\sigma_k$ are Hermitian, while the quaternion units themselves satisfy $\Phi(e_k) = -i \sigma_k$, which is skew-Hermitian. Combined with the fact that complex conjugation of the scalar coefficients is compatible with conjugate transposition of the matrix, this gives that the fixed points of $\dagger$ are exactly the matrices with $M = M^\dagger$, i.e., the Hermitian matrices, and the fixed points of $\flat$ are exactly the matrices with $M = -M^\dagger$, i.e., the anti-Hermitian matrices. The center and the vector subspace are the two eigenspaces of the adjugate operation $\Phi(\tilde{Q}) \mapsto \mathrm{adj}\,\Phi(\tilde{Q})$, with $+1$ on the center and $-1$ on the traceless matrices.

### Structural Consequences of the Isomorphism

The isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ has several structural consequences.

**Simplicity.** An algebra is **simple** if it has no nontrivial two-sided ideals. The algebra $M_2(\mathbb{C})$ is simple, because any nonzero two-sided ideal contains a matrix of rank one, and the products of such a matrix with arbitrary matrices generate the whole algebra. So the biquaternion algebra is simple.

**Center.** The center of $M_2(\mathbb{C})$ is the set of scalar matrices, which is isomorphic to $\mathbb{C}$. So the center of the biquaternion algebra is the complex subspace $\mathbb{C}_{\mathbb{B}}$.

**Endomorphism algebra.** The algebra $M_2(\mathbb{C})$ is the algebra of endomorphisms of a two-dimensional complex vector space. So the biquaternion algebra is the algebra of endomorphisms of $\mathbb{C}^2$.

**Zero divisors.** The zero divisors of $\mathbb{B}$ correspond to the singular matrices of $M_2(\mathbb{C})$, i.e., the matrices with vanishing determinant. This is the content of the article on biquaternion zero divisors, translated into matrix language.

## The Spinor Representation

### Definition

A **spinor** is an element of the two-dimensional complex vector space $\mathbb{C}^2$, written as a column vector

$$
\psi = \begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix}, \qquad \psi_1, \psi_2 \in \mathbb{C}.
$$

A biquaternion $\tilde{Q}$ acts on a spinor by matrix multiplication, via the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$:

$$
\psi \mapsto \tilde{Q} \psi = \begin{pmatrix} (Q_0 - i Q_3)\psi_1 + (-i Q_1 - Q_2)\psi_2 \\ (-i Q_1 + Q_2)\psi_1 + (Q_0 + i Q_3)\psi_2 \end{pmatrix}.
$$

This is the **spinor representation** of the biquaternion algebra: the biquaternion acts as a linear operator on the space of spinors.

A spinor is not a biquaternion, and it should be distinguished clearly from the biquaternion that acts on it. The biquaternion is an algebra element; the spinor is an element of the module on which the algebra acts. The relation between them is the module structure.

### Properties

**Linearity.** The action is complex-linear in $\psi$: $\tilde{Q}(\lambda \psi + \mu \phi) = \lambda \tilde{Q}\psi + \mu \tilde{Q}\phi$ for $\lambda, \mu \in \mathbb{C}$.

**Composition.** The action is compatible with multiplication: $\tilde{Q}(\tilde{R}\psi) = (\tilde{Q} \circ \tilde{R})\psi$. This is the module structure, and it is the reason the spinor representation is a representation in both senses of the word.

**Hermitian inner product.** The space of spinors carries a natural Hermitian inner product

$$
\langle \psi, \phi \rangle = \psi_1^* \phi_1 + \psi_2^* \phi_2.
$$

The biquaternion action preserves this inner product when $\tilde{Q}$ is unitary, i.e., when $\tilde{Q}^\dagger \tilde{Q} = 1$. The unitary biquaternions form the group $U(2)$.

**Determinant.** The subgroup of $U(2)$ consisting of elements with determinant $1$ is $SU(2)$. This is the group of unit quaternions, and it is the double cover of the rotation group $SO(3)$.

### Relation to the Representation Theory Article

The spinor module is the defining module of the group of units: a biquaternion of unit norm acts on $\mathbb{C}^2$ by the same $2 \times 2$ matrices, so $SL(2,\mathbb{C})$ acts on spinors. The structure attached to that action — the weights $(\tfrac{1}{2}, 0)$ and $(0, \tfrac{1}{2})$ of the defining module and its conjugate, the vector representation as the tensor product of the spinor with its conjugate, the double covers of the rotation and Lorentz groups, the Clebsch--Gordan rule, and the unitary representations — is not treated here. The present section supplies the realization only: the algebra as operators on $\mathbb{C}^2$, and the module structure that the action defines.

## The Clifford Algebra Representation

### Definition

The Clifford algebra $\mathrm{Cl}_{1,3}(\mathbb{R})$ is generated by four elements $\gamma^0, \gamma^1, \gamma^2, \gamma^3$ satisfying the anticommutation relations

$$
\gamma^\mu \gamma^\nu + \gamma^\nu \gamma^\mu = 2 g^{\mu\nu} I,
$$

where $g = \mathrm{diag}(+1, -1, -1, -1)$. The algebra has real dimension $2^4 = 16$. A real basis is given by the identity, the four vectors $\gamma^\mu$, the six bivectors $\gamma^\mu \gamma^\nu$ with $\mu < \nu$, the four trivectors $\gamma^\mu \gamma^\nu \gamma^\rho$ with $\mu < \nu < \rho$, and the pseudoscalar $\gamma^0 \gamma^1 \gamma^2 \gamma^3$.

The **even subalgebra** $\mathrm{Cl}_{1,3}^+$ consists of products of an even number of generators. It has real dimension $8$, and it is spanned by the identity, the six bivectors $\gamma^\mu \gamma^\nu$ with $\mu < \nu$, and the pseudoscalar $\gamma^0 \gamma^1 \gamma^2 \gamma^3$.

**Theorem.** The biquaternion algebra is isomorphic to the even subalgebra of the Clifford algebra $\mathrm{Cl}_{1,3}$:

$$
\mathbb{B} \cong \mathrm{Cl}_{1,3}^+(\mathbb{R}).
$$

The isomorphism is given by mapping the quaternion units and the scalar imaginary to

$$
e_1 \mapsto \gamma^2 \gamma^3, \qquad e_2 \mapsto \gamma^3 \gamma^1, \qquad e_3 \mapsto \gamma^1 \gamma^2, \qquad i \mapsto -\omega = -\gamma^0 \gamma^1 \gamma^2 \gamma^3,
$$

where the last identification is with minus the pseudoscalar. The three spacelike bivectors $\gamma^2 \gamma^3, \gamma^3 \gamma^1, \gamma^1 \gamma^2$ correspond to the quaternion units, and (minus) the pseudoscalar corresponds to the scalar imaginary. The three remaining bivectors $\gamma^0 \gamma^1, \gamma^0 \gamma^2, \gamma^0 \gamma^3$ correspond to the imaginary quaternion units $i e_1, i e_2, i e_3$ **all with positive sign**:

$$
(-\omega) \cdot (\gamma^2 \gamma^3) = +\gamma^0 \gamma^1, \qquad
(-\omega) \cdot (\gamma^3 \gamma^1) = +\gamma^0 \gamma^2, \qquad
(-\omega) \cdot (\gamma^1 \gamma^2) = +\gamma^0 \gamma^3,
$$

where $\omega = \gamma^0 \gamma^1 \gamma^2 \gamma^3$. This is the clean form the mostly-minus convention allows: all six bivectors correspond to the quaternion units with positive signs, and the single sign is carried by $i$ itself. Under the opposite sign of the generators the correspondence has to be $e_3 \mapsto \gamma^2\gamma^1$, and the timelike signs then come out mixed; no choice of the sign of $i$ makes all three positive there.

**Verification.** Each spacelike bivector squares to $-1$: $(\gamma^j \gamma^k)^2 = \gamma^j \gamma^k \gamma^j \gamma^k = -\gamma^j \gamma^j \gamma^k \gamma^k = -(-1)(-1) = -1$ for $j \neq k$ in $\{1, 2, 3\}$, since $(\gamma^j)^2 = -1$ in signature $(1,3)$. The pseudoscalar also squares to $-1$: $(\gamma^0 \gamma^1 \gamma^2 \gamma^3)^2 = -1$. The products reproduce the quaternion relations: for example, $e_1 e_2 \mapsto (\gamma^2 \gamma^3)(\gamma^3 \gamma^1) = \gamma^2 (\gamma^3)^2 \gamma^1 = -\gamma^2 \gamma^1 = \gamma^1 \gamma^2$, matching $e_1 e_2 = e_3$ in the quaternion algebra.

**Equality of the containment.** The three spacelike bivectors generate a copy of $\mathbb{H}$ inside $\mathrm{Cl}_{1,3}^+$, and the pseudoscalar $\omega = \gamma^0\gamma^1\gamma^2\gamma^3$ is central in $\mathrm{Cl}_{1,3}^+$ with $\omega^2 = -1$, so it generates a central copy of $\mathbb{C}$ commuting with that copy. Hence $\mathbb{R}[\omega]\otimes_{\mathbb{R}}\mathbb{H} \cong \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H} = \mathbb{B}$ embeds in $\mathrm{Cl}_{1,3}^+$. Both sides have real dimension $8$, so the embedding is surjective; this is what makes the identification an equality of algebras rather than an identification of $\mathbb{B}$ with a proper subalgebra.

### Properties

**Multiplication.** The Clifford product of two even elements is even, so the even subalgebra is closed under multiplication. Under the isomorphism, the Clifford product corresponds to the biquaternion product.

**Norm.** The Clifford norm on the even subalgebra corresponds to the biquaternion norm form.

**Relation to $M_2(\mathbb{C})$.** The even subalgebra $\mathrm{Cl}_{1,3}^+$ is isomorphic to $M_2(\mathbb{C})$ as a real algebra, which is the algebraic content of the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$. The full Clifford algebra $\mathrm{Cl}_{1,3}$ is isomorphic to $M_2(\mathbb{H})$, the $2\times 2$ matrices over the quaternions, as a real algebra (equivalently, $\mathrm{Cl}_{1,3} \otimes_{\mathbb{R}} \mathbb{C} \cong M_4(\mathbb{C})$), and its even subalgebra is the single copy of $M_2(\mathbb{C})$ on which the biquaternions are modeled. The opposite-sign algebra is the real matrix algebra, $\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$; the two are distinct over $\mathbb{R}$ but share the even part.

### Why the Clifford Algebra Representation Is Useful

The Clifford algebra representation is useful because:

1. **It connects the algebra to the Clifford algebra of the underlying form.** The biquaternion algebra is the even part of $\mathrm{Cl}_{1,3}$, and the even part is what acts on spinors.
2. **It makes the geometry explicit.** The Clifford algebra is the natural algebraic structure on a vector space with a quadratic form. In the case of $\mathrm{Cl}_{1,3}$, that form has signature $(1,3)$: one generator squares to $+1$ and three to $-1$.
3. **It generalizes.** The Clifford algebra construction works in any dimension and any signature. The biquaternion algebra is the specific case of dimension $4$ and signature $(1,3)$ — the Hermitian form of the algebra, since the Clifford vectors correspond to the Hermitian subspace $\mathbb{M}_+$ — and the general theory places it in a broader context.

## Relations Between the Representations

The four representations are related as follows.

**Four-vector and matrix.** The four-vector representation and the matrix representation are related by the explicit isomorphism given above: the components $Q_\mu$ of the four-vector are the entries of the matrix, arranged in a specific pattern.

**Matrix and spinor.** The matrix representation and the spinor representation are related by the action of the matrix on a column vector: the matrix representation is the algebra of operators, and the spinor representation is the space on which they act.

**Matrix and Clifford algebra.** The matrix representation and the Clifford algebra representation are related by the isomorphism $\mathrm{Cl}_{1,3}^+ \cong M_2(\mathbb{C})$: the bivectors of the Clifford algebra map to the matrices that represent the quaternion units and the imaginary quaternion units.

**All four.** The four representations are different ways of presenting the same algebra. The choice of representation is a choice of how to write the algebra, and different choices are useful for different purposes. There is no canonical choice; the four-vector representation is the most familiar, and the matrix representation is the most computationally convenient, but the spinor and Clifford algebra representations reveal the deeper structure.

## The Role of Choices

Each representation involves a choice, and different choices give equivalent but not identical representations.

- **Four-vector representation:** the choice of the ordering of the components, i.e., which component is the time component and which are the spatial components.
- **Matrix representation:** the choice of the isomorphism, i.e., which matrices are assigned to the quaternion units. The choice made above is one of many; different choices are related by conjugation by an invertible matrix.
- **Spinor representation:** the choice of the basis of $\mathbb{C}^2$, which is determined by the choice of the matrix representation.
- **Clifford algebra representation:** the choice of the gamma matrices, which is determined by the choice of the bilinear form and the basis of the underlying vector space.

Different choices give representations that are related by conjugation, and the algebraic structure of the biquaternion algebra is the same in all of them. The choices are a matter of convention and convenience, not of content.

## Summary

The biquaternion algebra admits four concrete algebraic representations, all of the same algebra and related by explicit isomorphisms:

| Representation | Biquaternion as | Useful for |
|---|---|---|
| Complex four-vector | $Q^\mu = (Q^0, \mathbf{Q})$ | Tensor formalism, indefinite quadratic forms, Lorentz group |
| $2 \times 2$ matrix | $\Phi(\tilde{Q}) = \begin{pmatrix} Q_0 - i Q_3 & -i Q_1 - Q_2 \\ -i Q_1 + Q_2 & Q_0 + i Q_3 \end{pmatrix}$ | Concrete computation, isomorphism with $M_2(\mathbb{C})$ |
| Spinor | Operator on $\begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix}$ | Module structure, tensor products, the group of unit-norm elements |
| Clifford algebra | Element of $\mathrm{Cl}_{1,3}^+$ | Geometry, generalization in dimension and signature |

In the matrix representation the isomorphism $\Phi$ is fixed by $\Phi(e_0) = I$ and $\Phi(e_k) = -i\sigma_k$, with $\Phi(i\tilde{Q}) = i\Phi(\tilde{Q})$; it carries the norm form to the determinant, the scalar part to half the trace, quaternion conjugation to the adjugate, Hermitian conjugation to the conjugate transpose, and the center to the scalar matrices and the vector subspace to the traceless matrices.

In the four-vector representation the norm form reads $N(\tilde{Q}) = (Q^0)^2 + (Q^1)^2 + (Q^2)^2 + (Q^3)^2$, restricting to signature $(3,1)$ on $\mathbb{M}_-$ and $(1,3)$ on $\mathbb{M}_+$, the two exchanged by multiplication by $i$; the Clifford representation uses the $(1,3)$ form on $\mathbb{M}_+$.

The four-vector representation is the one most familiar from the Lorentz-group literature. The matrix, spinor, and Clifford representations are more algebraic and reveal more of the structure. The choice of representation depends on what is being computed, and the four are related by explicit isomorphisms.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $e_0, e_1, e_2, e_3$ | Algebra basis, $e_0 = 1$, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary |
| $Q_\mu = q_\mu + i q'_\mu$ | Complex coefficients of $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ |
| $Q^\mu$ | Four-vector components in the four-vector representation |
| $\Phi$ | Algebra isomorphism $\mathbb{B} \to M_2(\mathbb{C})$, $\Phi(e_k) = -i\sigma_k$ |
| $\sigma_1, \sigma_2, \sigma_3$ | Pauli matrices |
| $\epsilon = i\sigma_2$ | Antisymmetric form realising complex conjugation, $\Phi(\tilde{Q}^*) = \epsilon\overline{\Phi(\tilde{Q})}\epsilon^{-1}$ |
| $N(\tilde{Q}) = \det\Phi(\tilde{Q})$ | Norm form |
| $\mathrm{Cl}_{1,3}$ | Clifford algebra of signature $(1,3)$; $\mathbb{B} \cong \mathrm{Cl}_{1,3}^+$ |
| $\gamma^\mu$ | Clifford generators, $(\gamma^0)^2 = +1$, $(\gamma^j)^2 = -1$ |
| $\omega = \gamma^0\gamma^1\gamma^2\gamma^3$ | Pseudoscalar, $\omega^2 = -1$, central in $\mathrm{Cl}_{1,3}^+$ |



## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- J. P. Ward, *Quaternions and Cayley Numbers* (Kluwer, 1997), Chapter 3, for the matrix representations of biquaternions.
- S. J. Sangwine, T. A. Ell, N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* 21 (2011) 607–636, for the applied representation theory.

