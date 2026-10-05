# __Biquaternion Other Algebraic Element Representations__

## Introduction

The algebra article defined the biquaternion algebra $\mathbb{B}$, its conjugations, and its six distinguished real subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$. This article describes the two **algebraic realizations** of $\mathbb{B}$ that are not the subject of a dedicated article of their own:

1. **Clifford algebra representation.** A biquaternion as an element of the even Clifford algebra $\mathrm{Cl}_{1,3}^+$.
2. **Conjugation action.** A biquaternion as an inner automorphism $\tilde T \mapsto \tilde{Q}\tilde T\tilde{Q}^{-1}$ of the algebra.

A structure of a different kind is treated here as well. A **rectangular array of several biquaternions** is not a realization of $\mathbb{B}$ — its entries are biquaternions, and the array is an object of the larger ring $M_n(\mathbb{B})$ when it is square — but its image under $\Phi$, taken entry by entry, is a complex matrix of twice the size, and it is the array that the applied articles put on a machine. It is treated in the section *Matrix Representations of Several Biquaternions*, after the two realizations.

The remaining realizations of the same algebra are the subjects of their own articles:

| realization | article |
|---|---|
| complex four-vector | *Biquaternion Four-Vector Element Representation* |
| $2\times2$ matrix | *Biquaternion 2×2 Matrix Element Representation* |
| $4\times4$ regular matrix | *Biquaternion 4×4 Regular Matrix Element Representation* |

and the polar realizations, which use the exponential and the roots of $-1$, of *Biquaternion Polar Element Representation* and *Biquaternion Partial Polar Element Representations*. Each of those articles owns its realization, its derivation and its relations with the others; this article records only the relations that involve the two realizations studied here.

The spinor module, and the action of the algebra on two-component spinors, are not a realization of this article: they are developed in *Biquaternion Spin Geometry*, with the operator theory in *Biquaternion Twisted Spinor Operator Representation*.

The word "representation" is used throughout in the sense of "a concrete realization of the algebra as a collection of computable objects." It is not used in the technical sense of algebra representation theory, in which a representation of an algebra $A$ is a vector space $V$ together with an algebra homomorphism $\rho : A \to \mathrm{End}(V)$. The two uses are related — the conjugation action below is a representation in both senses — but they are not the same. We use the word in the first sense.

The word "algebraic" is used to contrast with "polar," not with "matrix." The realizations in this article use only the algebra operations, the scalar imaginary, and the underlying complex vector space structure. They do not use the exponential, the roots of $-1$, or any analytic construction.

**Objects and operators.** A realization writes the element as an array and decides nothing about how the array is used. The same $2\times2$ matrix $\Phi(\tilde{Q})$ is the biquaternion written as an **object** — an array whose entries are its coordinates — and, as soon as a column is placed beside it, the **operator** acting on that column. Neither reading is a property of the size of the array, and neither is a property of the realization: a four-component object built from the algebra (the coefficient four-vector; an element of the algebra read as a vector of the underlying eight-dimensional real space) has an image in the four-vector, the $2\times2$ and the $4\times4$ realization alike, and none of those three images is an operator by itself. An operator appears exactly where an action on a carrier is specified, and the carrier may be $\mathbb{C}^2$, a space of four-component objects, or the algebra itself. The two maps met in this article and in *Biquaternion Rotations and Lorentz Transformations*, the conjugation and the dagger sandwich, are therefore not more operator-like than a matrix array: they are maps of the algebra to itself, which is a different carrier, not a different kind of array. The objects of the corpus are written in these realizations and are not operators; an object acts only once an action has been attached to it, and one matrix realization can carry both the object and the action on it.

Throughout, we use the notation of the algebra article: a biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3,
$$

or, more compactly, as

$$
\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu, \qquad Q_\mu \in \mathbb{C},
$$

with $e_0 = 1$ and $e_1, e_2, e_3$ the quaternion units. The scalar imaginary is $i$, which commutes with the quaternion units. Each complex coefficient is written $Q_\mu = q_\mu + i q'_\mu$ with $q_\mu, q'_\mu \in \mathbb{R}$.

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

**Biquaternion norm.** The Clifford norm on the even subalgebra corresponds to the biquaternion norm.

**Relation to $M_2(\mathbb{C})$.** The even subalgebra $\mathrm{Cl}_{1,3}^+$ is isomorphic to $M_2(\mathbb{C})$ as a real algebra, which is the algebraic content of the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ of *Biquaternion 2×2 Matrix Element Representation*. The full Clifford algebra $\mathrm{Cl}_{1,3}$ is isomorphic to $M_2(\mathbb{H})$, the $2\times 2$ matrices over the quaternions, as a real algebra (equivalently, $\mathrm{Cl}_{1,3} \otimes_{\mathbb{R}} \mathbb{C} \cong M_4(\mathbb{C})$), and its even subalgebra is the single copy of $M_2(\mathbb{C})$ on which the biquaternions are modeled. The opposite-sign algebra is the real matrix algebra, $\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$; the two are distinct over $\mathbb{R}$ but share the even part. The same identification under the companion labelling, $\mathbb{B}\cong\mathrm{Cl}_{3,1}^+$, together with the volume element as central scalar, the outer product and the grades, the matrix model, the idempotents, the Peirce decomposition and the ideals, is developed in *The Clifford Structure of the Biquaternion Algebra*, which is the dedicated article on the Clifford identification.

### Why the Clifford Algebra Representation Is Useful

The Clifford algebra representation is useful because:

1. **It connects the algebra to the Clifford algebra of the underlying form.** The biquaternion algebra is the even part of $\mathrm{Cl}_{1,3}$.
2. **It makes the geometry explicit.** The Clifford algebra is the natural algebraic structure on a vector space with a quadratic form. In the case of $\mathrm{Cl}_{1,3}$, that form has signature $(1,3)$: one generator squares to $+1$ and three to $-1$.
3. **It generalizes.** The Clifford algebra construction works in any dimension and any signature. The biquaternion algebra is the specific case of dimension $4$ and signature $(1,3)$ — the complex sesquilinear form of the algebra, since the Clifford vectors correspond to the Hermitian subspace $\mathbb{M}_+$ — and the general theory places it in a broader context.

## The Conjugation Action

### Definition

The third two-sided action of a unit on the algebra replaces the Hermitian conjugate of the sandwich by the inverse:

$$
\operatorname{Ad}_{\tilde{Q}}(\tilde T) = \tilde{Q}\,\tilde T\,\tilde{Q}^{-1}, \qquad \langle\tilde{Q},\tilde{Q}\rangle_{\natural} \neq 0 .
$$

The two differ in what they require of the algebra. The inverse uses the product and the biquaternion norm alone, so $\operatorname{Ad}_{\tilde{Q}}$ is built from the algebra operations; the dagger needs the coefficient conjugation as well, and this is why $\operatorname{Ad}_{\lambda\tilde{Q}} = \operatorname{Ad}_{\tilde{Q}}$ for every nonzero central $\lambda$ while the sandwich is not invariant under that rescaling. The name is the standard one: $\operatorname{Ad}_{\tilde{Q}}$ is the **adjoint action** of the group of units on the algebra.

This is the realization that satisfies the technical definition of a representation in the strict sense: a homomorphism of the group of units into the automorphism group of $\mathbb{B}$, which is itself a group of linear maps of $\mathbb{B}$. It is the action the corpus calls the inner automorphisms, and it is the *reference and the contrast* of the dagger sandwich, which is placed beside it in *Biquaternion Rotations and Lorentz Transformations*.

### It Is an Algebra Automorphism

For a unit $\tilde{Q}$ and any $\tilde T, \tilde S$,

$$
\operatorname{Ad}_{\tilde{Q}}(\tilde T\tilde S) = \tilde{Q}\,\tilde T\tilde S\,\tilde{Q}^{-1} = \bigl(\tilde{Q}\tilde T\tilde{Q}^{-1}\bigr)\bigl(\tilde{Q}\tilde S\tilde{Q}^{-1}\bigr) = \operatorname{Ad}_{\tilde{Q}}(\tilde T)\,\operatorname{Ad}_{\tilde{Q}}(\tilde S),
$$

since the inserted $\tilde{Q}^{-1}\tilde{Q}$ is the unit. The map fixes $e_0$ and is inverted by $\operatorname{Ad}_{\tilde{Q}^{-1}}$, so it is an algebra automorphism of $\mathbb{B}$. Multiplicativity here is unconditional, in contrast with the sandwich, which is multiplicative exactly on the unitary elements; the criterion is taken up below.

### The Kernel Is the Centre

The automorphism is the identity exactly when $\tilde{Q}$ commutes with every element of the algebra:

$$
\operatorname{Ad}_{\tilde{Q}} = \mathrm{id} \iff \tilde{Q}\tilde T = \tilde T\tilde{Q}\ \text{ for all } \tilde T \iff \tilde{Q} \in \mathbb{C}_{\mathbb{B}} .
$$

The action therefore depends on $\tilde{Q}$ only through its class in the quotient $\mathbb{B}^{\times} / \mathbb{C}_{\mathbb{B}}^{\times}$ of the group of units by the scalar subgroup. Under the matrix isomorphism that quotient is $GL_2(\mathbb{C})/\mathbb{C}^{\times} = PGL_2(\mathbb{C}) \cong PSL_2(\mathbb{C})$, and every automorphism of $\mathbb{B} \cong M_2(\mathbb{C})$ is inner, so the image of the action is the whole automorphism group and not a proper subgroup of it. That group, its real forms, and the derivations of the algebra are the subject of *Biquaternion Automorphisms and Derivations*; the property used here is quoted rather than proved.

### Relation to the Sandwich

For a unitary element the dagger is the inverse, $\tilde{Q}^{*} = \tilde{Q}^{-1}$, so

$$
\operatorname{H}_{\tilde{Q}} = \operatorname{Ad}_{\tilde{Q}} \qquad (\tilde{Q}^{*}\tilde{Q} = e_0) .
$$

On the unitary elements the sandwich **is** the conjugation action, and it is this automorphism that its multiplicativity criterion detects. For a general unit, written $\tilde{Q} = \lambda\tilde{U}$ with $\lambda$ central and $\tilde{U}$ unitary,

$$
\operatorname{H}_{\lambda\tilde{U}}(\tilde T) = \lambda\tilde{U}\,\tilde T\,\bar{\lambda}\tilde{U}^{*} = |\lambda|^2\operatorname{Ad}_{\tilde{U}}(\tilde T),
$$

a central dilation of an inner automorphism by the square of the modulus. Off the unitary slice the sandwich is therefore not a second automorphism but one automorphism, scaled; what it loses there is multiplicativity, not its connection with conjugation.

### The Action on the Six Subspaces

The centre is fixed pointwise, because its elements are the scalars, and the vector subspace $\mathrm{Vect}(\mathbb{B}) = [\mathbb{B}, \mathbb{B}]$ is preserved, because an algebra automorphism carries commutators to commutators. The remaining four subspaces are preserved exactly by the units that are central multiples of a real quaternion:

| subspace | preserved by $\operatorname{Ad}_{\tilde{Q}}$ for |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | every unit $\tilde{Q}$, pointwise |
| $\mathrm{Vect}(\mathbb{B})$ | every unit $\tilde{Q}$ |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | $\tilde{Q}$ a central multiple of a real quaternion |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | $\tilde{Q}$ a central multiple of a real quaternion |

The two rows for the halves and the sectors carry the same condition, and the condition can be read off the element: $\tilde{Q}$ is such a multiple exactly when $\tilde{Q}^{*}\tilde{Q}$ is central, that is, when $\tilde{Q}^{*}$ is a central multiple of $\tilde{Q}^{-1}$, which is what preserving $\mathbb{M}_{\pm}$ requires. This is the same class of operators that *Biquaternion Rotations and Lorentz Transformations* records as the ones preserving the whole subspace structure, and the action here is the automorphism that this class generates. For a unit outside the class the four subspaces are not merely moved among themselves: the image of each is a four-real-dimensional subspace in general position, lying in none of the six.

### The Two Minimal Left Ideals

The algebra is $M_2(\mathbb{C})$ and its simple module appears inside it as a minimal left ideal, as in *Biquaternion 2×2 Matrix Element Representation*. With $\tilde\Pi_1 = \tfrac12(e_0 + ie_3)$, so that $e_3\tilde\Pi_1 = i\tilde\Pi_1$ and $1-\tilde\Pi_1 = \tfrac12(e_0 - ie_3)$, the two halves of the algebra are the minimal left ideals $\mathbb{B}\tilde\Pi_1$ and $\mathbb{B}(1-\tilde\Pi_1)$. Left multiplication preserves each of them, while the conjugation action carries each to a minimal left ideal, because it is an automorphism:

$$
\operatorname{Ad}_{\tilde{Q}}\bigl(\mathbb{B}\tilde\Pi_1\bigr) = \mathbb{B}\bigl(\tilde{Q}\tilde\Pi_1\tilde{Q}^{-1}\bigr),
\qquad
\tilde{Q}\tilde\Pi_1\tilde{Q}^{-1} = \tilde\Pi_1 \iff \tilde{Q}\tilde\Pi_1 = \tilde\Pi_1\tilde{Q}.
$$

A unit that does not commute with $\tilde\Pi_1$ therefore moves the halving, and $\tilde{Q}\tilde\Pi_1\tilde{Q}^{-1}$ is again an idempotent of the algebra, generating the minimal left ideal $\mathbb{B}(\tilde{Q}\tilde\Pi_1\tilde{Q}^{-1})$. The two halves are **exchanged** by $\tilde{Q} = ie_1$, for which

$$
(ie_1)\,\tilde\Pi_1\,(ie_1)^{-1} = 1 - \tilde\Pi_1 ,
$$

and for a generic unit the image is a third idempotent, neither $\tilde\Pi_1$ nor $1-\tilde\Pi_1$: the exchange of the two halves is the special case, not the rule. The units that leave the halving untouched are exactly those commuting with $\tilde\Pi_1$, that is, the elements of $\mathrm{span}_{\mathbb{C}}\{e_0, e_3\}$; being unitary is not sufficient for that, since $e_1$ is unitary and does not commute with $\tilde\Pi_1$.

The dagger sandwich exchanges them as well, $\operatorname{H}_{ie_1}(\tilde\Pi_1) = 1 - \tilde\Pi_1$. Neither action is a map of left modules over the algebra — $\operatorname{H}_{\tilde{Q}}(\tilde B\tilde T) \neq \tilde B\operatorname{H}_{\tilde{Q}}(\tilde T)$ in general, and the same is true of $\operatorname{Ad}_{\tilde{Q}}$ — but only the automorphism is multiplicative, and it is multiplicativity that makes the exchange of the halves a statement about the algebra rather than about one element.

## Matrix Representations of Several Biquaternions

### Definition

Every realization met so far writes **one** element. The corpus also uses the case of **several** elements at once, arranged in a rectangular array, which the applied articles call a matrix-valued biquaternion. An array of size $n\times m$ with entries in $\mathbb{B}$ is written

$$
\tilde{\mathcal{Q}} = \bigl(\tilde Q_{ij}\bigr) \in \mathbb{B}^{n\times m}, \qquad \tilde Q_{ij} \in \mathbb{B}.
$$

This is not a realization of the algebra $\mathbb{B}$: the entries are biquaternions, and the array is an object of the larger structure — the ring $M_n(\mathbb{B})$ when it is square. It is recorded here because it is assembled from the realization $\Phi$ of *Biquaternion 2×2 Matrix Element Representation*, and because the corpus uses it — it is the form in which the algebra is put on a machine, and the arithmetic of that form is the subject of the companion physics article *The Computational Cost of Biquaternion Arithmetic*.

Two writings of the same array are used. In the **entrywise writing** it is a collection of $nm$ biquaternions. In the **component writing** it is a collection of four complex matrices, one per quaternion unit,

$$
\tilde{\mathcal{Q}} = e_0Q_0 + e_1Q_1 + e_2Q_2 + e_3Q_3, \qquad Q_\mu \in \mathbb{C}^{n\times m},
$$

where $Q_\mu$ gathers the $\mu$-th coefficients of all the entries and the product by $e_\mu$ is entrywise. The two writings carry the same information: an $n\times m$ array holds $4nm$ complex numbers, that is $8nm$ real numbers, in either reading.

### The Array Ring

For $n = m$, entrywise addition and entrywise multiplication make $\mathbb{B}^{n\times n}$ a unital associative ring: the full matrix ring $M_n(\mathbb{B})$. Multiplication is noncommutative for two independent reasons — the entries are multiplied in the algebra $\mathbb{B}$, which is itself noncommutative, and the array product is the matrix product, which is noncommutative for $n \ge 2$ even over a commutative coefficient ring. Since $\mathbb{B}$ is not a division algebra, the array ring is not one either; it has zero divisors already at $n = 1$, from the zero divisors of the algebra itself.

The structure of the ring is fixed by the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$:

$$
M_n(\mathbb{B}) \;\cong\; M_n\bigl(M_2(\mathbb{C})\bigr) \;\cong\; M_{2n}(\mathbb{C}).
$$

So an $n\times n$ array of biquaternions **is** the full complex matrix algebra of twice the size. That is the precise sense in which several biquaternions have a matrix representation, and it is the array-level form of the element-level isomorphism of the 2×2 article. Every statement about $M_n(\mathbb{B})$ that is invariant under isomorphism is therefore a statement about complex matrices of size $2n$, and the array writing is a way of holding the same algebra in $n^2$ biquaternion slots rather than $4n^2$ complex ones.

### The Image of an Array

The realization of the 2×2 article extends to arrays entry by entry: replace every entry by its $2\times2$ matrix, and read the result as a complex matrix of size $2n\times2m$,

$$
\Phi(\tilde{\mathcal{Q}}) = \sum_{\mu=0}^{3} \Phi(e_\mu)\otimes Q_\mu,
$$

where $\otimes$ is the Kronecker product, $\Phi(e_0) = I_2$, and $\Phi(e_k) = -i\sigma_k$. The order of the two factors fixes which index of the image runs where, and the two orders are exchanged by a permutation of indices; we keep $\Phi(e_\mu)$ first, so that the **indices of $\Phi$ are the block indices** of the image — the quadrants of the image, of size $n\times m$ — and the array indices run inside each block. The other order assembles the same data with the array indices outside instead, $\sum_\mu Q_\mu\otimes\Phi(e_\mu) = \bigl(\Phi(\tilde Q_{ij})\bigr)$; in it the block in position $(i,j)$ is $\Phi(\tilde Q_{ij})$, so that the image is the array of the images. The properties below hold in both orders, and only the block reading differs.

Three properties carry the whole correspondence, and each is exact:

1. **Products.** The map is a ring isomorphism: the image of the array product is the product of the images, $\Phi(\tilde{\mathcal{P}}\tilde{\mathcal{Q}}) = \Phi(\tilde{\mathcal{P}})\Phi(\tilde{\mathcal{Q}})$, when the sizes match. This is the explicit form of $M_n(\mathbb{B}) \cong M_{2n}(\mathbb{C})$;
2. **Trace.** For a square array the trace of the image is twice the trace of the scalar component matrix, $\mathrm{tr}\,\Phi(\tilde{\mathcal{Q}}) = 2\,\mathrm{tr}\,Q_0$, which is the algebra trace $2\,\mathrm{Sc}$ summed over the diagonal. It is a complex number, and it vanishes for a traceless scalar component;
3. **Dagger.** Transposing the array and applying the Hermitian conjugation to each entry, $(\tilde{\mathcal{Q}}^{\dagger})_{ij} = (\tilde Q_{ji})^{*}$, carries the image to the conjugate transpose, $\Phi(\tilde{\mathcal{Q}}^{\dagger}) = \Phi(\tilde{\mathcal{Q}})^{\dagger}$.

All three were checked on 100 random arrays of sizes up to $3\times3$ in exact arithmetic, with zero mismatches. The first also holds for non-square arrays whenever the sizes are conformable, and the second requires a square array.

### Examples

The smallest cases are the ones a reader meets, and each shows a different face of the correspondence. In the order we keep, the quadrants of the image are the blocks of $\Phi(e_\mu)$ and the array indices run inside them:

| Several biquaternions | Image | What it shows |
|---|---|---|
| the one-entry array $[\tilde Q]$ | $\Phi(\tilde Q)$, of size $2\times2$ | the 2×2 realization is the one-entry case of the array |
| the array unit, $e_0$ in position $(i,j)$ and zero elsewhere | $I_2\otimes E_{ij}$ | the array units carry the algebra identity |
| a single non-zero entry, $\tilde Q$ in position $(i,j)$ | $\Phi(\tilde Q)\otimes E_{ij}$ | the image of the entry sits in the block position of the entry |
| the constant diagonal array, every diagonal entry equal to $\tilde Q$ | $\Phi(\tilde Q)\otimes I_n$ | the algebra index and the array index assemble independently |
| a general $2\times2$ array of biquaternions | a general $4\times4$ complex matrix | the array already fills a full complex matrix of twice the size |

The one-entry case is worth stating separately: the 2×2 realization is not a different construction from the array, it is the array of size $1\times1$. The $4\times4$ array image is the first case in which the two index levels are visible at once, one level being the array and the other the matrix realization of the algebra; and the last row is the dimension count, a $2\times2$ array of biquaternions holding sixteen complex numbers, exactly as a general $4\times4$ complex matrix does. In the other order the table reads differently but the algebra is the same: the image is the array of the images, and the last four rows become statements about the blocks rather than about the quadrants.

### Which Realization the Array Is Not

The image $\Phi(\tilde{\mathcal{Q}})$ is **not** the left regular matrix of *Biquaternion 4×4 Regular Matrix Element Representation*. That matrix is the image of the operator of left multiplication by one element on the algebra, which is a $4\times4$ array of complex numbers for that element; the array image here is the image of the array's own entries. The two coincide in size only when the array is $2\times2$, and even then they are different objects: the regular matrix is block diagonal in a suitable basis, with $\Phi(\tilde Q)$ in both diagonal blocks, while the image of a general $2\times2$ array of biquaternions is a general $4\times4$ complex matrix. What the two share is the underlying isomorphism: both are the algebra $\mathbb{B} \cong M_2(\mathbb{C})$ or its array-level extension $M_n(\mathbb{B}) \cong M_{2n}(\mathbb{C})$ written out.

## Relations Between the Representations

**The minimal left ideals and the regular realization.** The left regular representation of *Biquaternion 4×4 Regular Matrix Element Representation* is not a third action but the left action on the two minimal left ideals taken twice. Since $\Phi(\tilde{Q}\tilde T) = \Phi(\tilde{Q})\Phi(\tilde T)$, reading the four entries of $\Phi(\tilde T)$ column by column exhibits an isomorphism of left $\mathbb{B}$-modules

$$
\mathbb{B} \longrightarrow \mathbb{C}^2 \oplus \mathbb{C}^2, \qquad
\tilde T \longmapsto \bigl(\text{first column of } \Phi(\tilde T),\ \text{second column of } \Phi(\tilde T)\bigr),
$$

on which $\tilde{Q}$ acts on each copy as $\Phi(\tilde{Q})$. The two copies are the two minimal left ideals of the section above, $\mathbb{B}\tilde\Pi_1$ and $\mathbb{B}(1-\tilde\Pi_1)$, each of real dimension $4$, and in the $\Phi$ picture they are the two column spaces. In a basis of $\mathbb{B}$ made of a basis of $\mathbb{B}\tilde\Pi_1$ followed by a basis of $\mathbb{B}(1-\tilde\Pi_1)$, the left-regular $4\times4$ matrix of $\tilde{Q}$ is therefore block diagonal with $\Phi(\tilde{Q})$ in both diagonal blocks. This is why the $2\times2$ and $4\times4$ accounts of the same algebra cannot disagree about the isomorphism $\Phi$: the second contains the first twice.

**Conjugation and the sandwich.** The conjugation action is the multiplicative core of the dagger sandwich: the two coincide exactly on the unitary elements, $\operatorname{H}_{\tilde{Q}} = \operatorname{Ad}_{\tilde{Q}}$ for $\tilde{Q}^{*}\tilde{Q} = e_0$, and in general $\operatorname{H}_{\lambda\tilde{U}} = |\lambda|^2\operatorname{Ad}_{\tilde{U}}$ for $\tilde{Q} = \lambda\tilde{U}$ with central $\lambda$ and unitary $\tilde{U}$. *Biquaternion Rotations and Lorentz Transformations* reads the sandwich against this reference, and the two differ in exactly two respects: the sandwich is not multiplicative off the unitary slice, and it is not invariant under a rescaling of $\tilde{Q}$ by a central element, so that it distinguishes the class of $\tilde{Q}$ from $\tilde{Q}$ itself.

**Conjugation and the minimal left ideals.** Because it is an automorphism, the conjugation action permutes the two minimal left ideals, and it exchanges them for any unit not commuting with $\tilde\Pi_1$, for instance $ie_1$. A two-sided action either leaves the halving alone, when the acting unit commutes with $\tilde\Pi_1$, or carries $\mathbb{B}\tilde\Pi_1$ to another minimal left ideal, which is its opposite in the special case of $ie_1$ and a third ideal in general.

**With the realizations treated elsewhere.** The remaining relations are recorded in the articles that own those realizations:

- the four-vector realization and the $2\times2$ matrix realization are related by the explicit isomorphism that reads the components $Q_\mu$ off the matrix entries;
- the $2\times2$ matrix realization is related to the Clifford realization by $\mathrm{Cl}_{1,3}^+ \cong M_2(\mathbb{C})$, the same isomorphism that carries the bivectors to the matrices;
- the conjugation action is the automorphism group of the algebra acting on itself, and it is the reference against which the dagger sandwich is read;
- the $4\times4$ regular realization is the algebra acting on itself, and the dagger sandwich is the element as a linear operator on the algebra, both of them read against the matrix realization;
- the polar realizations are the algebraic realizations restricted to the unit-norm slice and factorised by the exponential.

All of them present the same algebra. The choice of realization is a choice of how to write it, and different choices are useful for different purposes.

## The Role of Choices

Each representation involves a choice, and different choices give equivalent but not identical representations.

- **Clifford algebra representation:** the choice of the gamma matrices, which is determined by the choice of the quaternion bilinear form and the basis of the underlying vector space.
- **Conjugation action:** the choice of the unit $\tilde{Q}$, which is redundant, since $\operatorname{Ad}_{\lambda\tilde{Q}} = \operatorname{Ad}_{\tilde{Q}}$ for every nonzero central $\lambda$; the action depends on $\tilde{Q}$ only through its class in $\mathbb{B}^{\times}/\mathbb{C}_{\mathbb{B}}^{\times}$.

The choices belonging to the other realizations are recorded in their own articles. Different choices give representations that are related by conjugation, and the algebraic structure of the biquaternion algebra is the same in all of them. The choices are a matter of convention and convenience, not of content.

## Summary

The biquaternion algebra admits two algebraic realizations that are not treated in dedicated articles of this series:

| Realization | the element is written as | the reading | Useful for |
|---|---|---|---|
| Clifford algebra | an element of $\mathrm{Cl}_{1,3}^+$ | object | Geometry, generalization in dimension and signature |
| Conjugation action | the map $\tilde T \mapsto \tilde{Q}\tilde T\tilde{Q}^{-1}$ | operator on the algebra | The automorphism group, the minimal left ideals, the reference for the dagger sandwich |

The first two columns are independent: the writing fixes an array, the reading fixes what is done with it, and the same matrix appears as an object and as an operator at once. The realization is a choice neither of size nor of role, which is why a four-vector, a $2\times2$ array and a $4\times4$ array can all carry the same object, and any of them can carry an action on it.

In the Clifford realization the isomorphism is fixed by $e_1 \mapsto \gamma^2\gamma^3$, $e_2 \mapsto \gamma^3\gamma^1$, $e_3 \mapsto \gamma^1\gamma^2$ and $i \mapsto -\gamma^0\gamma^1\gamma^2\gamma^3$ under the mostly-minus form $g = \mathrm{diag}(+1,-1,-1,-1)$, so that all six bivectors correspond to the quaternion units with positive signs, and it carries the Clifford product to the biquaternion product and the Clifford norm to the biquaternion norm on the even part; the $1,3$ form is the one carried by the Hermitian subspace $\mathbb{M}_+$.

One structure recorded here is not a realization of a single element. An **array of several biquaternions** is the ring $M_n(\mathbb{B}) \cong M_{2n}(\mathbb{C})$ for a square array, its entrywise image $\Phi(\tilde{\mathcal{Q}}) = \sum_\mu \Phi(e_\mu)\otimes Q_\mu$ is a complex matrix of twice the size, and that image preserves products, traces and daggers; the one-entry array is the $2\times2$ realization itself. The array is the form the applied articles compute with, and its arithmetic is developed in *The Computational Cost of Biquaternion Arithmetic*.

The matrix, four-vector and regular realizations, the biquaternion norm read in each of them, and the explicit isomorphisms between them, are the subject of their own articles. Here the two realizations above are derived, together with the array-level structure, which is not a realization of a single element; the relations recorded are the ones they have with each other and with the realizations treated elsewhere.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $e_0, e_1, e_2, e_3$ | Algebra basis, $e_0 = 1$, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary |
| $Q_\mu = q_\mu + i q'_\mu$ | Complex coefficients of $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ | Quaternion subspace and Hermitian subspace of $\mathbb{B}$ |
| $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm |
| $\mathrm{Cl}_{1,3}$ | Clifford algebra of signature $(1,3)$; $\mathbb{B} \cong \mathrm{Cl}_{1,3}^+$ |
| $\gamma^\mu$ | Clifford generators, $(\gamma^0)^2 = +1$, $(\gamma^j)^2 = -1$ |
| $\omega = \gamma^0\gamma^1\gamma^2\gamma^3$ | Pseudoscalar, $\omega^2 = -1$, central in $\mathrm{Cl}_{1,3}^+$ |
| $\operatorname{Ad}_{\tilde{Q}}(\tilde T) = \tilde{Q}\tilde T\tilde{Q}^{-1}$ | Conjugation action of a unit, the inner automorphism |
| $\operatorname{H}_{\tilde{Q}}(\tilde T) = \tilde{Q}\tilde T\tilde{Q}^{*}$ | The dagger sandwich of *Biquaternion Rotations and Lorentz Transformations* |
| $\tilde\Pi_1 = \tfrac12(e_0 + ie_3)$ | Idempotent, $\mathbb{B}\tilde\Pi_1$ a minimal left ideal of real dimension $4$ |
| $\Phi$ | The isomorphism $\mathbb{B} \to M_2(\mathbb{C})$ of *Biquaternion 2×2 Matrix Element Representation*, $\Phi(e_0) = I_2$, $\Phi(e_k) = -i\sigma_k$ |
| $\mathbb{B}^{n\times m}$ | Array of several biquaternions; for $n = m$ the ring $M_n(\mathbb{B}) \cong M_{2n}(\mathbb{C})$ |
| $\tilde{\mathcal{Q}} = e_0Q_0 + e_1Q_1 + e_2Q_2 + e_3Q_3$ | The array in component writing, $Q_\mu \in \mathbb{C}^{n\times m}$ the $\mu$-th coefficient matrix |
| $\Phi(\tilde{\mathcal{Q}}) = \sum_\mu \Phi(e_\mu)\otimes Q_\mu$ | Entrywise image, a $2n\times2m$ complex matrix; the array indices are the block indices |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- J. P. Ward, *Quaternions and Cayley Numbers* (Kluwer, 1997), Chapter 3, for the matrix representations of biquaternions.
- S. J. Sangwine, T. A. Ell, N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* 21 (2011) 607–636, for the applied representation theory.

