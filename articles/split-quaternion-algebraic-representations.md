
# Split-Quaternion Algebraic Representations

## Introduction

The basic algebra article defined the split quaternion algebra $\mathbb{H}_{\mathbb{D}}$, its conjugations, and its four fixed-point subspaces. This article describes the **algebraic representations** of the split quaternion algebra: concrete ways of writing split quaternions as objects we can compute with, using only the algebra operations and the underlying vector space structure.

The word "representation" is used here in the sense of "a concrete realization of the algebra as a collection of computable objects." It is not used in the technical sense of algebra representation theory, in which a representation of an algebra $A$ is a vector space $V$ together with an algebra homomorphism $\rho : A \to \mathrm{End}(V)$. The two uses are related — the module representation below is a representation in both senses — but they are not the same. We use the word in the first sense throughout.

The word "algebraic" is used to contrast with "polar." The representations in this article use only the algebra operations, the split complex unit, and the underlying vector space structure. They do not use the exponential or the roots of $-1$ as a primary tool. The polar representations, which do use the exponential and the roots of $-1$, are treated in the companion article on split quaternion polar representations.

The representations we discuss in this article are:

1. **Split complex four-vector representation.** A split quaternion as a split complex four-vector.
2. **Idempotent representation.** A split quaternion as a pair of ordinary quaternions.
3. **Module representation.** A split quaternion as an operator on a module over the quaternion algebra.
4. **Clifford algebra representation.** A split quaternion as an element of a Clifford algebra of split signature.

The matrix representation, which is the primary algebraic representation in the biquaternion case, is **not** available in the split quaternion case in the same form. The reason is discussed in a separate section: the split quaternion algebra is not isomorphic to a matrix algebra over $\mathbb{R}$ or over $\mathbb{D}$. The idempotent representation plays the role that the matrix representation plays in the biquaternion case, and it is the primary representation of the split quaternion algebra.

Throughout, we use the notation of the basic algebra article: a split quaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3,
$$

or, more compactly, as

$$
\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu, \qquad Q_\mu \in \mathbb{D},
$$

with $e_0 = 1$ and $e_1, e_2, e_3$ the quaternion units. The split complex unit is $j$, with $j^2 = +1$, and it commutes with the quaternion units. Each split complex coefficient is written $Q_\mu = q_\mu + j q'_\mu$ with $q_\mu, q'_\mu \in \mathbb{R}$.

The quaternion conjugate is $\bar{\tilde{Q}} = Q_0 e_0 - \mathbf{Q}$, where $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$. The split complex conjugate is $\tilde{Q}^* = Q_0^* e_0 + \mathbf{Q}^*$, where $Q_\mu^* = q_\mu - j q'_\mu$. The Hermitian conjugate is $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$, and the anti-Hermitian conjugate is $\tilde{Q}^\flat = -\tilde{Q}^\dagger$.

The idempotents of the split complex algebra are $e_+ = \tfrac{1}{2}(1 + j)$ and $e_- = \tfrac{1}{2}(1 - j)$. The idempotent decomposition of a split quaternion is

$$
\tilde{Q} = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-,
$$

with $\tilde{Q}_\pm = \tilde{Q} e_\pm \in \mathbb{H}$ ordinary quaternions.

## The Split Complex Four-Vector Representation

### Definition

A split quaternion $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ can be written as a split complex four-vector

$$
Q^\mu = (Q^0, Q^1, Q^2, Q^3),
$$

with

$$
Q^0 = Q_0, \qquad (Q^1, Q^2, Q^3) = (Q_1, Q_2, Q_3).
$$

The split scalar part of the split quaternion becomes the time component of the four-vector; the split vector part becomes the spatial components. This is the most direct representation.

### Multiplication in Four-Vector Form

The product of two split quaternions in four-vector form separates into a scalar part and a vector part:

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

Split complex conjugation conjugates all components:

$$
(Q^*)^\mu = ((Q^0)^*, (Q^1)^*, (Q^2)^*, (Q^3)^*).
$$

Hermitian conjugation combines the two:

$$
(Q^\dagger)^\mu = ((Q^0)^*, -(Q^1)^*, -(Q^2)^*, -(Q^3)^*).
$$

### The Four Subspaces in Four-Vector Form

The four fixed-point subspaces have a simple characterization in the four-vector representation.

- **Split complex subspace $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$:** four-vectors of the form $Q^\mu = (Q^0, 0, 0, 0)$ with $Q^0 \in \mathbb{D}$.
- **Quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$:** four-vectors with real components, $Q^\mu \in \mathbb{R}^4$.
- **Hermitian subspace $\mathbb{M}_+$:** four-vectors of the form $Q^\mu = (q_0, j q'_1, j q'_2, j q'_3)$ with $q_0, q'_1, q'_2, q'_3 \in \mathbb{R}$. Real time component, purely split-imaginary spatial components.
- **Anti-Hermitian subspace $\mathbb{M}_-$:** four-vectors of the form $Q^\mu = (j q'_0, q_1, q_2, q_3)$ with $q'_0, q_1, q_2, q_3 \in \mathbb{R}$. Purely split-imaginary time component, real spatial components.

### The Norm Form in Four-Vector Form

The norm form $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}}$ is

$$
N(\tilde{Q}) = (Q^0)^2 + (Q^1)^2 + (Q^2)^2 + (Q^3)^2,
$$

a split complex number. Writing $Q^\mu = q^\mu + j q'^\mu$, this expands to

$$
N(\tilde{Q}) = \sum_{\mu=0}^{3} ((q^\mu)^2 + (q'^\mu)^2) + 2j \sum_{\mu=0}^{3} q^\mu q'^\mu.
$$

On the anti-Hermitian subspace $\mathbb{M}_-$, the norm form restricts to the real quadratic form

$$
N(\tilde{Q}) = -(q'_0)^2 + q_1^2 + q_2^2 + q_3^2,
$$

which is indefinite of signature $(3, 1)$.

### Why the Four-Vector Representation Is Useful

The four-vector representation is the bridge between the algebraic split quaternion and the standard tensor formalism. It is the representation in which the split signature is most visible: the scalar and vector components enter with opposite signs in the norm form, and the indefinite form on the anti-Hermitian subspace is expressed as a Lorentzian norm.

It is also the representation in which the split quaternion looks least like a split quaternion. The algebraic structure — the non-commutative product, the two conjugations, the zero divisors — is hidden. This is why the four-vector representation, while useful, is not the fundamental one.

## The Idempotent Representation

### Definition

The **idempotent representation** of a split quaternion is the expression

$$
\tilde{Q} = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-,
$$

where $e_\pm = \tfrac{1}{2}(1 \pm j)$ are the idempotents of the split complex algebra, and

$$
\tilde{Q}_\pm = \tilde{Q} e_\pm \in \mathbb{H}
$$

are ordinary quaternions. The two quaternions $\tilde{Q}_\pm$ are the **idempotent components** of $\tilde{Q}$.

The map

$$
\varphi : \mathbb{H}_{\mathbb{D}} \to \mathbb{H} \oplus \mathbb{H}, \qquad \varphi(\tilde{Q}) = (\tilde{Q}_+, \tilde{Q}_-)
$$

is an algebra isomorphism, where the multiplication on $\mathbb{H} \oplus \mathbb{H}$ is componentwise.

### Explicit Form of the Components

Writing $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ with $Q_\mu = q_\mu + j q'_\mu$,

$$
\tilde{Q}_+ = \tilde{Q} e_+ = \sum_\mu Q_\mu e_\mu e_+ = \sum_\mu Q_\mu e_+ e_\mu = \sum_\mu (Q_\mu e_+) e_\mu.
$$

Since $Q_\mu e_+ = (q_\mu + j q'_\mu) e_+ = (q_\mu + q'_\mu) e_+$, we have

$$
\tilde{Q}_+ = \sum_\mu (q_\mu + q'_\mu) e_\mu,
$$

where the coefficients $q_\mu + q'_\mu$ are real. Similarly,

$$
\tilde{Q}_- = \sum_\mu (q_\mu - q'_\mu) e_\mu.
$$

So the idempotent components are the real quaternions

$$
\tilde{Q}_+ = \sum_\mu (q_\mu + q'_\mu) e_\mu, \qquad \tilde{Q}_- = \sum_\mu (q_\mu - q'_\mu) e_\mu.
$$

Conversely, given two real quaternions $\tilde{Q}_\pm = \sum_\mu q_\mu^\pm e_\mu$, the split quaternion is recovered by

$$
\tilde{Q} = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-,
$$

and the coefficients in the standard basis are

$$
q_\mu = \frac{q_\mu^+ + q_\mu^-}{2}, \qquad q'_\mu = \frac{q_\mu^+ - q_\mu^-}{2}.
$$

### Properties

**Isomorphism.** The map $\varphi$ is an algebra isomorphism. Multiplication is componentwise:

$$
\varphi(\tilde{Q} \tilde{R}) = (\tilde{Q}_+ \tilde{R}_+, \tilde{Q}_- \tilde{R}_-).
$$

**Addition.** Addition is componentwise:

$$
\varphi(\tilde{Q} + \tilde{R}) = (\tilde{Q}_+ + \tilde{R}_+, \tilde{Q}_- + \tilde{R}_-).
$$

**Conjugations.** The four conjugations act on the idempotent components as follows:

- **Quaternion conjugation** $\bar{\tilde{Q}}$: acts on each component by the quaternion conjugate, $\overline{(\tilde{Q}_+, \tilde{Q}_-)} = (\bar{\tilde{Q}}_+, \bar{\tilde{Q}}_-)$.
- **Split complex conjugation** $\tilde{Q}^*$: swaps the two components, $(\tilde{Q}_+, \tilde{Q}_-)^* = (\tilde{Q}_-, \tilde{Q}_+)$.
- **Hermitian conjugation** $\tilde{Q}^\dagger$: acts on each component by the quaternion conjugate and swaps the two: $(\tilde{Q}_+, \tilde{Q}_-)^\dagger = (\bar{\tilde{Q}}_-, \bar{\tilde{Q}}_+)$.
- **Anti-Hermitian conjugation** $\tilde{Q}^\flat$: $(\tilde{Q}_+, \tilde{Q}_-)^\flat = (-\bar{\tilde{Q}}_-, -\bar{\tilde{Q}}_+)$.

The split complex conjugation is the map that swaps the two components. This is the algebraic content of the idempotent decomposition.

**Norm form.** The norm form is

$$
N(\tilde{Q}) = N_{\mathbb{H}}(\tilde{Q}_+) e_+ + N_{\mathbb{H}}(\tilde{Q}_-) e_-,
$$

where $N_{\mathbb{H}}(\tilde{Q}_\pm) = \tilde{Q}_\pm \bar{\tilde{Q}}_\pm$ is the ordinary quaternion norm, which is a non-negative real number. In the standard basis, this is

$$
N(\tilde{Q}) = \frac{N_{\mathbb{H}}(\tilde{Q}_+) + N_{\mathbb{H}}(\tilde{Q}_-)}{2} + j \frac{N_{\mathbb{H}}(\tilde{Q}_+) - N_{\mathbb{H}}(\tilde{Q}_-)}{2}.
$$

**Invertibility.** The split quaternion $\tilde{Q}$ is invertible if and only if both idempotent components are nonzero:

$$
\tilde{Q} \text{ is invertible} \iff \tilde{Q}_+ \neq 0 \text{ and } \tilde{Q}_- \neq 0.
$$

This is the cleanest form of the invertibility criterion.

**Zero divisors.** The split quaternion $\tilde{Q}$ is a zero divisor if and only if it is nonzero and at least one idempotent component vanishes:

$$
\tilde{Q} \text{ is a zero divisor} \iff \tilde{Q} \neq 0 \text{ and } (\tilde{Q}_+ = 0 \text{ or } \tilde{Q}_- = 0).
$$

### Why the Idempotent Representation Is the Primary One

The idempotent representation plays the role in the split quaternion algebra that the matrix representation plays in the biquaternion algebra. It has the following advantages.

**It reveals the structure.** The isomorphism $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H} \oplus \mathbb{H}$ is the most important structural fact about the algebra: it shows that the algebra is semisimple, that it is the direct sum of two simple algebras, and that its representation theory is the representation theory of $\mathbb{H}$ taken twice.

**It simplifies the norm form.** In the idempotent representation, the norm form is the pair of ordinary quaternion norms of the two components, which are non-negative real numbers. This is much simpler than the split complex expression in the standard basis.

**It simplifies the invertibility criterion.** The invertibility criterion becomes the linear condition that both components are nonzero, in contrast to the quadratic condition in the biquaternion case.

**It simplifies the zero divisor analysis.** The zero divisor set is the union of the two subspaces $Z_+ = \{\tilde{Q}_+ = 0\}$ and $Z_- = \{\tilde{Q}_- = 0\}$, which are four-dimensional linear subspaces.

**It connects to the split complex algebra.** The idempotent decomposition of $\mathbb{H}_{\mathbb{D}}$ is the extension of the idempotent decomposition of $\mathbb{D}$. The two idempotents $e_+$ and $e_-$ are the same in both algebras, and they are the source of the semisimple structure.

## The Module Representation

### Definition

The split quaternion algebra acts on itself by left multiplication. This gives a representation of $\mathbb{H}_{\mathbb{D}}$ on the vector space $\mathbb{H}_{\mathbb{D}}$, which is a module over $\mathbb{H}$ in the following sense: the idempotent decomposition $\mathbb{H}_{\mathbb{D}} = \mathbb{H} e_+ \oplus \mathbb{H} e_-$ exhibits $\mathbb{H}_{\mathbb{D}}$ as a direct sum of two copies of the quaternion algebra $\mathbb{H}$, each of which is a left module over $\mathbb{H}$.

The **module representation** of $\mathbb{H}_{\mathbb{D}}$ is the pair of representations

$$
\rho_\pm : \mathbb{H}_{\mathbb{D}} \to \mathrm{End}_{\mathbb{H}}(\mathbb{H} e_\pm)
$$

given by

$$
\rho_\pm(\tilde{Q})(\tilde{R} e_\pm) = \tilde{Q} \tilde{R} e_\pm.
$$

In the idempotent basis, this is

$$
\rho_\pm(\tilde{Q}) = \tilde{Q}_\pm,
$$

so the representation $\rho_\pm$ is evaluation at the idempotent $e_\pm$.

### Properties

**The two representations are the two components.** The module representation of $\mathbb{H}_{\mathbb{D}}$ is the pair of the two components $\tilde{Q}_+$ and $\tilde{Q}_-$ acting on the corresponding copies of $\mathbb{H}$.

**Irreducibility.** Each of the two representations is irreducible as a representation of the algebra $\mathbb{H} \oplus \mathbb{H}$ on the corresponding summand.

**The analogue of the spinor representation.** In the biquaternion case, the spinor representation is the action of $\mathbb{B} \cong M_2(\mathbb{C})$ on $\mathbb{C}^2$. In the split quaternion case, the module representation is the action of $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H} \oplus \mathbb{H}$ on $\mathbb{H} \oplus \mathbb{H}$, which is the direct sum of the two natural actions on the two copies of $\mathbb{H}$.

## The Clifford Algebra Representation

### Definition

The split quaternion algebra is isomorphic to the even subalgebra of a Clifford algebra of split signature:

$$
\mathbb{H}_{\mathbb{D}} \cong \mathrm{Cl}_{2,2}^+(\mathbb{R}) \cong \mathrm{Cl}_{1,1,1,1}^+(\mathbb{R}),
$$

depending on the sign convention. The Clifford algebra $\mathrm{Cl}_{2,2}$ is generated by four elements $\gamma^0, \gamma^1, \gamma^2, \gamma^3$ satisfying

$$
\gamma^\mu \gamma^\nu + \gamma^\nu \gamma^\mu = 2 \eta^{\mu\nu},
$$

where $\eta = \mathrm{diag}(-1, -1, +1, +1)$ (or another split signature, depending on the convention). The even subalgebra has real dimension $2^3 = 8$, matching the real dimension of $\mathbb{H}_{\mathbb{D}}$.

The isomorphism is given by mapping the quaternion units to the bivectors:

$$
e_1 \mapsto \gamma^2 \gamma^3, \qquad e_2 \mapsto \gamma^3 \gamma^0, \qquad e_3 \mapsto \gamma^0 \gamma^1,
$$

and the split complex unit $j$ to another bivector, for example $\gamma^0 \gamma^2$. The precise assignment depends on the signature and the convention.

### Properties

**Multiplication.** The Clifford product of two even elements is even, so the even subalgebra is closed under multiplication. Under the isomorphism, the Clifford product corresponds to the split quaternion product.

**Norm.** The Clifford norm on the even subalgebra corresponds to the split quaternion norm form.

### Why the Clifford Algebra Representation Is Useful

The Clifford algebra representation is useful because:

1. **It places the split quaternion algebra in the general Clifford classification.** The split quaternion algebra is one of the real Clifford algebras, and the representation shows how it fits into the general theory.
2. **It connects to physics.** The Clifford algebra $\mathrm{Cl}_{2,2}$ appears in the study of conformal field theory in two dimensions and in the theory of twistors in $2+2$ dimensions.
3. **It generalizes.** The Clifford algebra construction works in any dimension and any signature.

## The Absence of a Matrix Representation

### Statement

Unlike the biquaternion algebra, which is isomorphic to the matrix algebra $M_2(\mathbb{C})$, the split quaternion algebra is **not** isomorphic to a matrix algebra over a field or a ring in the same way.

### Reason

The reason is the following. The quaternion algebra $\mathbb{H}$ is a division algebra over $\mathbb{R}$ and is central simple. It is not isomorphic to a matrix algebra over $\mathbb{R}$: the only central simple algebras over $\mathbb{R}$ are $\mathbb{R}$, $\mathbb{C}$, and $\mathbb{H}$, and the matrix algebras are $M_n(\mathbb{R})$, $M_n(\mathbb{C})$, and $M_n(\mathbb{H})$ for $n \geq 1$. The quaternion algebra $\mathbb{H}$ is not a matrix algebra over $\mathbb{R}$; it only becomes one after complexification: $\mathbb{H} \otimes_{\mathbb{R}} \mathbb{C} \cong M_2(\mathbb{C})$.

The split quaternion algebra is $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H} \cong \mathbb{H} \oplus \mathbb{H}$. It is semisimple but not simple, and its simple summands are both isomorphic to $\mathbb{H}$. It is not isomorphic to a matrix algebra over a field, because a matrix algebra over a field is simple (for $M_n$ with $n \geq 1$), and $\mathbb{H}_{\mathbb{D}}$ is not simple.

The algebra $\mathbb{H}_{\mathbb{D}}$ is isomorphic to a subalgebra of $M_2(\mathbb{H})$, namely the subalgebra of matrices of the form $\begin{pmatrix} \tilde{Q}_+ & 0 \\ 0 & \tilde{Q}_- \end{pmatrix}$ with $\tilde{Q}_\pm \in \mathbb{H}$. This is a faithful representation, but it is not surjective onto $M_2(\mathbb{H})$.

### Comparison with the Biquaternion Case

| | $\mathbb{B}$ (biquaternion) | $\mathbb{H}_{\mathbb{D}}$ (split quaternion) |
|---|---|---|
| Extra unit | $i$, $i^2 = -1$ | $j$, $j^2 = +1$ |
| Structure | Simple | Semisimple |
| Matrix representation | $\mathbb{B} \cong M_2(\mathbb{C})$ | $\mathbb{H}_{\mathbb{D}} \subset M_2(\mathbb{H})$, not surjective |
| Primary algebraic representation | Matrix | Idempotent |

The absence of a matrix representation is a consequence of the fact that the split quaternion algebra is semisimple, not simple. The two summands are copies of the quaternion algebra, which is not a matrix algebra over $\mathbb{R}$.

## Relations Between the Representations

The four representations are related as follows.

**Four-vector and idempotent.** The four-vector representation and the idempotent representation are related by the linear transformation

$$
Q^\mu = (q^\mu + j q'^\mu) \longleftrightarrow (\tilde{Q}_+, \tilde{Q}_-),
$$

with

$$
\tilde{Q}_+ = \sum_\mu (q^\mu + q'^\mu) e_\mu, \qquad \tilde{Q}_- = \sum_\mu (q^\mu - q'^\mu) e_\mu.
$$

This is a linear isomorphism $\mathbb{R}^8 \to \mathbb{H} \oplus \mathbb{H}$.

**Idempotent and module.** The idempotent representation and the module representation are the same representation viewed from two different angles: the idempotent representation is the pair of components, and the module representation is the action of the algebra on each component.

**Idempotent and Clifford algebra.** The idempotent representation and the Clifford algebra representation are related by the isomorphism $\mathbb{H}_{\mathbb{D}} \cong \mathrm{Cl}_{2,2}^+$. The idempotents $e_\pm$ correspond to the projectors onto the two summands of the Clifford algebra.

**All four.** The four representations are different ways of presenting the same algebra. The idempotent representation is the primary one, because it reveals the semisimple structure and simplifies the norm form, the invertibility criterion, and the zero divisor analysis. The four-vector representation is the most familiar from the tensor formalism. The module and Clifford algebra representations place the algebra in the larger contexts of module theory and Clifford algebra theory.

## The Role of Choices

Each representation involves a choice, and different choices give equivalent but not identical representations.

- **Four-vector representation:** the choice of the ordering of the components.
- **Idempotent representation:** the choice of the idempotents $e_+$ and $e_-$. There is a unique pair of nontrivial idempotents in $\mathbb{D}$, so there is no real choice here; the representation is canonical.
- **Module representation:** the choice of the module (left or right), which is a matter of convention.
- **Clifford algebra representation:** the choice of the gamma matrices and the signature.

Different choices give representations that are related by conjugation or by a change of basis, and the algebraic structure of the split quaternion algebra is the same in all of them. The choices are a matter of convention and convenience, not of content.

## Summary of Representations

| Representation | Split quaternion as | Useful for |
|---|---|---|
| Split complex four-vector | $Q^\mu = (Q^0, \mathbf{Q})$ | Tensor formalism, indefinite quadratic forms |
| Idempotent | $(\tilde{Q}_+, \tilde{Q}_-) \in \mathbb{H} \oplus \mathbb{H}$ | Structure, norm form, invertibility, zero divisors |
| Module | Operator on $\mathbb{H} e_+ \oplus \mathbb{H} e_-$ | Representation theory |
| Clifford algebra | Element of $\mathrm{Cl}_{2,2}^+$ | Clifford algebra classification, geometry |

The four-vector representation is the one most familiar from the tensor formalism. The idempotent representation is the primary algebraic representation, and it is the one that reveals the semisimple structure of the algebra. The module and Clifford algebra representations place the algebra in the larger contexts of representation theory and Clifford algebra theory.

Unlike the biquaternion algebra, the split quaternion algebra does **not** have a faithful matrix representation over a field or over $\mathbb{D}$ that is surjective. The idempotent representation plays the role that the matrix representation plays in the biquaternion case.

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions and their relatives.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra perspective.
- J. P. Ward, *Quaternions and Cayley Numbers* (Kluwer, 1997), Chapter 3, for the algebraic representations of split quaternions.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.

