
# Biquaternion Algebraic Representations

## Introduction

The basic algebra article defined the biquaternion algebra $\mathbb{B}$, its conjugations, and its four fixed-point subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, and $\mathbb{M}_-$. This article describes the **algebraic representations** of the biquaternion algebra: concrete ways of writing biquaternions as objects we can compute with, using only the algebra operations and the underlying vector space structure.

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

### The Four Subspaces in Four-Vector Form

The four fixed-point subspaces have a simple characterization in the four-vector representation.

- **Complex subspace $\mathbb{C}_{\mathbb{B}}$:** four-vectors of the form $Q^\mu = (Q^0, 0, 0, 0)$ with $Q^0 \in \mathbb{C}$.
- **Quaternion subspace $\mathbb{H}_{\mathbb{B}}$:** four-vectors with real components, $Q^\mu \in \mathbb{R}^4$.
- **Hermitian subspace $\mathbb{M}_+$:** four-vectors of the form $Q^\mu = (q_0, i q'_1, i q'_2, i q'_3)$ with $q_0, q'_1, q'_2, q'_3 \in \mathbb{R}$. Real time component, purely imaginary spatial components.
- **Anti-Hermitian subspace $\mathbb{M}_-$:** four-vectors of the form $Q^\mu = (i q'_0, q_1, q_2, q_3)$ with $q'_0, q_1, q_2, q_3 \in \mathbb{R}$. Purely imaginary time component, real spatial components.

### The Norm Form in Four-Vector Form

The norm form $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ is

$$
N(\tilde{Q}) = (Q^0)^2 + (Q^1)^2 + (Q^2)^2 + (Q^3)^2.
$$

On the anti-Hermitian subspace $\mathbb{M}_-$, the norm form restricts to

$$
N(\tilde{Q}) = -(q'_0)^2 + q_1^2 + q_2^2 + q_3^2,
$$

which is the indefinite quadratic form of signature $(3, 1)$ or $(1, 3)$, depending on sign convention. This is the form that is invariant under the linear transformations preserving the quadratic form.

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
\tilde{Q} \mapsto \begin{pmatrix} Q_0 - i Q_3 & -i Q_1 - Q_2 \\ -i Q_1 + Q_2 & Q_0 + i Q_3 \end{pmatrix}.
$$

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
\bar{\tilde{Q}} \mapsto \begin{pmatrix} Q_0 + i Q_3 & i Q_1 + Q_2 \\ i Q_1 - Q_2 & Q_0 - i Q_3 \end{pmatrix},
$$

which is the **adjugate** (or classical adjoint) of the matrix: it is the matrix whose entries are the cofactors of the original matrix.

**Complex conjugation** $\tilde{Q}^*$ conjugates all entries of the matrix.

**Hermitian conjugation** $\tilde{Q}^\dagger$ is the conjugate transpose of the matrix:

$$
\tilde{Q}^\dagger \mapsto \begin{pmatrix} Q_0^* + i Q_3^* & i Q_1^* + Q_2^* \\ i Q_1^* - Q_2^* & Q_0^* - i Q_3^* \end{pmatrix} = \begin{pmatrix} \overline{Q_0 - i Q_3} & \overline{-i Q_1 + Q_2} \\ \overline{-i Q_1 - Q_2} & \overline{Q_0 + i Q_3} \end{pmatrix}.
$$

**Anti-Hermitian conjugation** $\tilde{Q}^\flat = -\tilde{Q}^\dagger$ is the negative of the conjugate transpose.

### The Four Subspaces in Matrix Form

The four fixed-point subspaces have a simple characterization in the matrix representation.

- **Complex subspace $\mathbb{C}_{\mathbb{B}}$:** diagonal matrices of the form $Q_0 I$ with $Q_0 \in \mathbb{C}$.
- **Quaternion subspace $\mathbb{H}_{\mathbb{B}}$:** matrices of the form $\begin{pmatrix} q_0 - i q_3 & -i q_1 - q_2 \\ -i q_1 + q_2 & q_0 + i q_3 \end{pmatrix}$ with $q_\mu \in \mathbb{R}$. These are the matrices of the form $\begin{pmatrix} z & w \\ -\bar{w} & \bar{z} \end{pmatrix}$ with $z, w \in \mathbb{C}$.
- **Hermitian subspace $\mathbb{M}_+$:** matrices that are Hermitian, i.e., equal to their conjugate transpose.
- **Anti-Hermitian subspace $\mathbb{M}_-$:** matrices that are anti-Hermitian, i.e., equal to the negative of their conjugate transpose.

The identifications of $\mathbb{M}_+$ with the Hermitian matrices and $\mathbb{M}_-$ with the anti-Hermitian matrices follow directly from the isomorphism: if $\tilde{Q}$ maps to $M$, then $\tilde{Q}^\dagger$ maps to $M^\dagger$ (the conjugate transpose). Indeed, the imaginary quaternion units satisfy $\phi(i e_k) = \sigma_k$, and the Pauli matrices $\sigma_k$ are Hermitian, while the quaternion units themselves satisfy $\phi(e_k) = -i \sigma_k$, which is skew-Hermitian. Combined with the fact that complex conjugation of the scalar coefficients is compatible with conjugate transposition of the matrix, this gives that the fixed points of $\dagger$ are exactly the matrices with $M = M^\dagger$, i.e., the Hermitian matrices, and the fixed points of $\flat$ are exactly the matrices with $M = -M^\dagger$, i.e., the anti-Hermitian matrices.

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

### Transformation Under the Lorentz Group

Spinors transform under the Lorentz group in a simple way. The $(1/2,0)$ representation of $SL(2,\mathbb{C})$ restricts to the fundamental representation of $SU(2)$ on $\mathbb{C}^2$, which is the rotation subgroup; the full Lorentz-group action is obtained by passing from $SU(2)$ to its complexification $SL(2,\mathbb{C})$.

The vector representation of the Lorentz group, i.e., the action on the four-dimensional space $\mathbb{M}_-$, is the **tensor product of the spinor representation with its conjugate**: a vector is a bilinear object of the form $\psi \otimes \bar{\phi}$, i.e., a $2 \times 2$ matrix built from a spinor and a conjugate spinor. Equivalently, a 4-vector can be represented as a $2 \times 2$ Hermitian matrix; the space of such matrices is the tensor product $\mathbb{C}^2 \otimes \overline{\mathbb{C}^2}$. In representation-theoretic notation, the spinor representation is the $(\tfrac{1}{2}, 0)$ of $SL(2, \mathbb{C})$, its conjugate is the $(0, \tfrac{1}{2})$, and the vector representation is the $(\tfrac{1}{2}, \tfrac{1}{2})$.

The group of biquaternions with unit norm form, $SL(2, \mathbb{C})$, is the double cover of the proper orthochronous Lorentz group $SO^+(1,3)$. The compact subgroup $SU(2) \subset SL(2, \mathbb{C})$ is the double cover of the spatial rotation group $SO(3)$.

This is the algebraic content of the statement that spinors are the fundamental representation of the Lorentz group, and it is the reason spinors appear in the Dirac equation and in quantum field theory.

### Why the Spinor Representation Is Useful

The spinor representation is useful because:

1. **It connects to the Dirac equation.** The Dirac equation describes spin-$\frac{1}{2}$ particles and is naturally written in terms of $2 \times 2$ matrices. Biquaternions provide a natural algebraic framework for these matrices.
2. **It makes Lorentz invariance manifest.** Spinors transform under the Lorentz group in a simple way, and the biquaternion action is Lorentz-invariant.
3. **It is the natural representation for quantum fields.** In quantum field theory, the fundamental fermionic fields are spinorial, and the biquaternion algebra is their natural algebraic home.

## The Clifford Algebra Representation

### Definition

The Clifford algebra $\mathrm{Cl}_{1,3}(\mathbb{R})$ is generated by four elements $\gamma^0, \gamma^1, \gamma^2, \gamma^3$ satisfying the anticommutation relations

$$
\gamma^\mu \gamma^\nu + \gamma^\nu \gamma^\mu = 2 \eta^{\mu\nu} I,
$$

where $\eta = \mathrm{diag}(-1, +1, +1, +1)$ (or its negative, depending on convention). The algebra has real dimension $2^4 = 16$. A real basis is given by the identity, the four vectors $\gamma^\mu$, the six bivectors $\gamma^\mu \gamma^\nu$ with $\mu < \nu$, the four trivectors $\gamma^\mu \gamma^\nu \gamma^\rho$ with $\mu < \nu < \rho$, and the pseudoscalar $\gamma^0 \gamma^1 \gamma^2 \gamma^3$.

The **even subalgebra** $\mathrm{Cl}_{1,3}^+$ consists of products of an even number of generators. It has real dimension $8$, and it is spanned by the identity, the six bivectors $\gamma^\mu \gamma^\nu$ with $\mu < \nu$, and the pseudoscalar $\gamma^0 \gamma^1 \gamma^2 \gamma^3$.

**Theorem.** The biquaternion algebra is isomorphic to the even subalgebra of the Clifford algebra $\mathrm{Cl}_{1,3}$:

$$
\mathbb{B} \cong \mathrm{Cl}_{1,3}^+(\mathbb{R}).
$$

The isomorphism is given by mapping the quaternion units and the scalar imaginary to

$$
e_1 \mapsto \gamma^2 \gamma^3, \qquad e_2 \mapsto \gamma^3 \gamma^1, \qquad e_3 \mapsto \gamma^2 \gamma^1, \qquad i \mapsto \gamma^0 \gamma^1 \gamma^2 \gamma^3,
$$

where the last identification is with the pseudoscalar. The three spacelike bivectors $\gamma^2 \gamma^3, \gamma^3 \gamma^1, \gamma^2 \gamma^1$ correspond to the quaternion units and the pseudoscalar corresponds to the scalar imaginary. The three remaining bivectors $\gamma^0 \gamma^1, \gamma^0 \gamma^2, \gamma^0 \gamma^3$ correspond to the imaginary quaternion units $i e_1, i e_2, i e_3$ up to sign:

$$
\omega \cdot (\gamma^2 \gamma^3) = -\gamma^0 \gamma^1, \qquad
\omega \cdot (\gamma^3 \gamma^1) = -\gamma^0 \gamma^2, \qquad
\omega \cdot (\gamma^2 \gamma^1) = +\gamma^0 \gamma^3,
$$

where $\omega = \gamma^0 \gamma^1 \gamma^2 \gamma^3$. With the alternative convention $i \mapsto -\omega$, the first two become $+\gamma^0 \gamma^1$ and $+\gamma^0 \gamma^2$ while the third becomes $-\gamma^0 \gamma^3$; no choice of sign of $i$ makes all three simultaneously $+\gamma^0 \gamma^k$. The signs are a consequence of the chosen handedness of the correspondence $e_1, e_2, e_3 \mapsto \gamma^2 \gamma^3, \gamma^3 \gamma^1, \gamma^2 \gamma^1$ and are absorbed into the identification of the imaginary quaternion units with the timelike bivectors.

**Verification.** Each spacelike bivector squares to $-1$: $(\gamma^j \gamma^k)^2 = \gamma^j \gamma^k \gamma^j \gamma^k = -\gamma^j \gamma^j \gamma^k \gamma^k = -(1)(1) = -1$ for $j \neq k$ in $\{1, 2, 3\}$. The pseudoscalar also squares to $-1$: $(\gamma^0 \gamma^1 \gamma^2 \gamma^3)^2 = -1$ in signature $(1,3)$. The products reproduce the quaternion relations: for example, $e_1 e_2 \mapsto (\gamma^2 \gamma^3)(\gamma^3 \gamma^1) = \gamma^2 (\gamma^3 \gamma^3) \gamma^1 = \gamma^2 \gamma^1$, matching $e_1 e_2 = e_3$ in the quaternion algebra.

### Properties

**Multiplication.** The Clifford product of two even elements is even, so the even subalgebra is closed under multiplication. Under the isomorphism, the Clifford product corresponds to the biquaternion product.

**Norm.** The Clifford norm on the even subalgebra corresponds to the biquaternion norm form.

**Relation to $M_2(\mathbb{C})$.** The even subalgebra $\mathrm{Cl}_{1,3}^+$ is isomorphic to $M_2(\mathbb{C})$ as a real algebra, which is the algebraic content of the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$. The full Clifford algebra $\mathrm{Cl}_{1,3}$ is isomorphic to $M_2(\mathbb{H})$ as a real algebra (equivalently, $\mathrm{Cl}_{1,3} \otimes_{\mathbb{R}} \mathbb{C} \cong M_4(\mathbb{C})$), and its even subalgebra is the single copy of $M_2(\mathbb{C})$ on which the biquaternions are modeled.

### Why the Clifford Algebra Representation Is Useful

The Clifford algebra representation is useful because:

1. **It connects to the Dirac algebra.** The gamma matrices of the Dirac equation generate the Clifford algebra. The biquaternion algebra is the even part of this, which is the part that acts on spinors.
2. **It makes the geometry explicit.** The Clifford algebra is the natural algebraic structure on a vector space with a quadratic form. In the case of $\mathrm{Cl}_{1,3}$, the quadratic form is the Minkowski metric.
3. **It generalizes.** The Clifford algebra construction works in any dimension and any signature. The biquaternion algebra is the specific case of dimension $4$ and signature $(1,3)$ or $(3,1)$, and the general theory places it in a broader context.

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

## Summary of Representations

| Representation | Biquaternion as | Useful for |
|---|---|---|
| Complex four-vector | $Q^\mu = (Q^0, \mathbf{Q})$ | Tensor formalism, indefinite quadratic forms, Lorentz group |
| $2 \times 2$ matrix | $\begin{pmatrix} Q_0 - i Q_3 & -i Q_1 - Q_2 \\ -i Q_1 + Q_2 & Q_0 + i Q_3 \end{pmatrix}$ | Concrete computation, isomorphism with $M_2(\mathbb{C})$ |
| Spinor | Operator on $\begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix}$ | Dirac equation, Lorentz invariance, quantum fields |
| Clifford algebra | Element of $\mathrm{Cl}_{1,3}^+$ | Dirac algebra, geometry, generalization |

The four-vector representation is the one most familiar from standard physics. The matrix, spinor, and Clifford representations are more algebraic and reveal more of the structure. The choice of representation depends on what is being computed, and the four are related by explicit isomorphisms.

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra perspective.
- J. P. Ward, *Quaternions and Cayley Numbers* (Kluwer, 1997), Chapter 3, for the matrix representations of biquaternions.
- S. J. Sangwine, T. A. Ell, N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* 21 (2011) 607–636, for the applied representation theory.

