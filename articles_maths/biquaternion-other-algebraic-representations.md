# __Biquaternion Other Algebraic Representations__

## Introduction

The algebra article defined the biquaternion algebra $\mathbb{B}$, its conjugations, and its six distinguished real subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$. This article describes the three **algebraic realizations** of $\mathbb{B}$ that are not the subject of a dedicated article of their own:

1. **Spinor representation.** A biquaternion written on two-component spinors, its $2\times2$ image acting by matrix multiplication on a column.
2. **Clifford algebra representation.** A biquaternion as an element of the even Clifford algebra $\mathrm{Cl}_{1,3}^+$.
3. **Conjugation action.** A biquaternion as an inner automorphism $x \mapsto \tilde{Q}x\tilde{Q}^{-1}$ of the algebra.

The remaining realizations of the same algebra are the subjects of their own articles:

| realization | article |
|---|---|
| complex four-vector | *Biquaternion Four-Vector Representation* |
| $2\times2$ matrix | *Biquaternion 2×2 Matrix Representation* |
| $4\times4$ regular matrix | *Biquaternion 4×4 Regular Matrix Representation* |
| operator on the algebra | *Biquaternion Operator Representation* |

and the polar realizations, which use the exponential and the roots of $-1$, of *Biquaternion Polar Representation* and *Biquaternion Partial Polar Representations*. Each of those articles owns its realization, its derivation and its relations with the others; this article records only the relations that involve the three realizations studied here.

The word "representation" is used throughout in the sense of "a concrete realization of the algebra as a collection of computable objects." It is not used in the technical sense of algebra representation theory, in which a representation of an algebra $A$ is a vector space $V$ together with an algebra homomorphism $\rho : A \to \mathrm{End}(V)$. The two uses are related — the spinor representation below is a representation in both senses — but they are not the same. We use the word in the first sense.

The word "algebraic" is used to contrast with "polar," not with "matrix." The realizations in this article use only the algebra operations, the scalar imaginary, and the underlying complex vector space structure. They do not use the exponential, the roots of $-1$, or any analytic construction.

**Objects and operators.** A realization writes the element as an array and decides nothing about how the array is used. The same $2\times2$ matrix $\Phi(\tilde{Q})$ is the biquaternion written as an **object** — an array whose entries are its coordinates — and, as soon as a column is placed beside it, the **operator** acting on that column. Neither reading is a property of the size of the array, and neither is a property of the realization: a four-component object built from the algebra (the coefficient four-vector; an element of the algebra read as a vector of the underlying eight-dimensional real space) has an image in the four-vector, the $2\times2$ and the $4\times4$ realization alike, and none of those three images is an operator by itself. An operator appears exactly where an action on a carrier is specified, and the carrier may be $\mathbb{C}^2$, a space of four-component objects, or the algebra itself. The two maps met in this article and in *Biquaternion Operator Representation*, the conjugation and the dagger sandwich, are therefore not more operator-like than a matrix array: they are maps of the algebra to itself, which is a different carrier, not a different kind of array. The objects of the corpus are written in these realizations and are not operators; an object acts only once an action has been attached to it, and one matrix realization can carry both the object and the action on it.

Throughout, we use the notation of the algebra article: a biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3,
$$

or, more compactly, as

$$
\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu, \qquad Q_\mu \in \mathbb{C},
$$

with $e_0 = 1$ and $e_1, e_2, e_3$ the quaternion units. The scalar imaginary is $i$, which commutes with the quaternion units. Each complex coefficient is written $Q_\mu = q_\mu + i q'_\mu$ with $q_\mu, q'_\mu \in \mathbb{R}$.

## The Spinor Representation

### Definition

A **spinor** is an element of the two-dimensional complex vector space $\mathbb{C}^2$, written as a column vector

$$
\psi = \begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix}, \qquad \psi_1, \psi_2 \in \mathbb{C}.
$$

A biquaternion $\tilde{Q}$ acts on a spinor by matrix multiplication, via the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ of *Biquaternion 2×2 Matrix Representation*:

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

The spinor module is the defining module of the group of units: a biquaternion of unit norm acts on $\mathbb{C}^2$ by the same $2 \times 2$ matrices, so $SL(2,\mathbb{C})$ acts on spinors. The structure attached to that action — the weights $(\tfrac{1}{2}, 0)$ and $(0, \tfrac{1}{2})$ of the defining module and its conjugate, the vector representation as the tensor product of the spinor with its conjugate, the double covers of the rotation and Lorentz groups, the Clebsch--Gordan rule, and the unitary representations — is not treated here. The present section supplies the realization only: the algebra as operators on $\mathbb{C}^2$, and the module structure that the action defines. The module itself — its two chiral halves, its dual and its conjugate, the spinor contraction, the reality conditions on it, and the Clifford multiplication in the matrix model — is developed in *Spinors and the Biquaternion Spinor Module*, which is the dedicated article on the spinor module.

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

**Relation to $M_2(\mathbb{C})$.** The even subalgebra $\mathrm{Cl}_{1,3}^+$ is isomorphic to $M_2(\mathbb{C})$ as a real algebra, which is the algebraic content of the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ of *Biquaternion 2×2 Matrix Representation*. The full Clifford algebra $\mathrm{Cl}_{1,3}$ is isomorphic to $M_2(\mathbb{H})$, the $2\times 2$ matrices over the quaternions, as a real algebra (equivalently, $\mathrm{Cl}_{1,3} \otimes_{\mathbb{R}} \mathbb{C} \cong M_4(\mathbb{C})$), and its even subalgebra is the single copy of $M_2(\mathbb{C})$ on which the biquaternions are modeled. The opposite-sign algebra is the real matrix algebra, $\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$; the two are distinct over $\mathbb{R}$ but share the even part. The same identification under the companion labelling, $\mathbb{B}\cong\mathrm{Cl}_{3,1}^+$, together with the volume element as central scalar, the outer product and the grades, the matrix model, the idempotents, the Peirce decomposition and the ideals, is developed in *The Biquaternion Algebra as a Clifford Algebra*, which is the dedicated article on the Clifford identification.

### Why the Clifford Algebra Representation Is Useful

The Clifford algebra representation is useful because:

1. **It connects the algebra to the Clifford algebra of the underlying form.** The biquaternion algebra is the even part of $\mathrm{Cl}_{1,3}$, and the even part is what acts on spinors.
2. **It makes the geometry explicit.** The Clifford algebra is the natural algebraic structure on a vector space with a quadratic form. In the case of $\mathrm{Cl}_{1,3}$, that form has signature $(1,3)$: one generator squares to $+1$ and three to $-1$.
3. **It generalizes.** The Clifford algebra construction works in any dimension and any signature. The biquaternion algebra is the specific case of dimension $4$ and signature $(1,3)$ — the Hermitian form of the algebra, since the Clifford vectors correspond to the Hermitian subspace $\mathbb{M}_+$ — and the general theory places it in a broader context.

## The Conjugation Action

### Definition

The third two-sided action of a unit on the algebra replaces the Hermitian conjugate of the sandwich by the inverse:

$$
\operatorname{Ad}_{\tilde{Q}}(x) = \tilde{Q}\,x\,\tilde{Q}^{-1}, \qquad N(\tilde{Q}) \neq 0 .
$$

The two differ in what they require of the algebra. The inverse uses the product and the norm form alone, so $\operatorname{Ad}_{\tilde{Q}}$ is built from the algebra operations; the dagger needs the coefficient conjugation as well, and this is why $\operatorname{Ad}_{\lambda\tilde{Q}} = \operatorname{Ad}_{\tilde{Q}}$ for every nonzero central $\lambda$ while the sandwich is not invariant under that rescaling. The name is the standard one: $\operatorname{Ad}_{\tilde{Q}}$ is the **adjoint action** of the group of units on the algebra.

This is the realization that satisfies the technical definition of a representation in the strict sense: a homomorphism of the group of units into the automorphism group of $\mathbb{B}$, which is itself a group of linear maps of $\mathbb{B}$. It is the action the corpus calls the inner automorphisms, and it is the *reference and the contrast* of *Biquaternion Operator Representation*, where it is placed beside the dagger sandwich.

### It Is an Algebra Automorphism

For a unit $\tilde{Q}$ and any $x, y$,

$$
\operatorname{Ad}_{\tilde{Q}}(xy) = \tilde{Q}\,xy\,\tilde{Q}^{-1} = \bigl(\tilde{Q}x\tilde{Q}^{-1}\bigr)\bigl(\tilde{Q}y\tilde{Q}^{-1}\bigr) = \operatorname{Ad}_{\tilde{Q}}(x)\,\operatorname{Ad}_{\tilde{Q}}(y),
$$

since the inserted $\tilde{Q}^{-1}\tilde{Q}$ is the unit. The map fixes $e_0$ and is inverted by $\operatorname{Ad}_{\tilde{Q}^{-1}}$, so it is an algebra automorphism of $\mathbb{B}$. Multiplicativity here is unconditional, in contrast with the sandwich, which is multiplicative exactly on the unitary elements; the criterion is taken up below.

### The Kernel Is the Centre

The automorphism is the identity exactly when $\tilde{Q}$ commutes with every element of the algebra:

$$
\operatorname{Ad}_{\tilde{Q}} = \mathrm{id} \iff \tilde{Q}x = x\tilde{Q}\ \text{ for all } x \iff \tilde{Q} \in \mathbb{C}_{\mathbb{B}} .
$$

The action therefore depends on $\tilde{Q}$ only through its class in the quotient $\mathbb{B}^{\times} / \mathbb{C}_{\mathbb{B}}^{\times}$ of the group of units by the scalar subgroup. Under the matrix isomorphism that quotient is $GL_2(\mathbb{C})/\mathbb{C}^{\times} = PGL_2(\mathbb{C}) \cong PSL_2(\mathbb{C})$, and every automorphism of $\mathbb{B} \cong M_2(\mathbb{C})$ is inner, so the image of the action is the whole automorphism group and not a proper subgroup of it. That group, its real forms, and the derivations of the algebra are the subject of *Biquaternion Automorphisms and Derivations*; the property used here is quoted rather than proved.

### Relation to the Sandwich

For a unitary element the dagger is the inverse, $\tilde{Q}^{\dagger} = \tilde{Q}^{-1}$, so

$$
\operatorname{H}_{\tilde{Q}} = \operatorname{Ad}_{\tilde{Q}} \qquad (\tilde{Q}^{\dagger}\tilde{Q} = e_0) .
$$

On the unitary elements the sandwich **is** the conjugation action, and it is this automorphism that its multiplicativity criterion detects. For a general unit, written $\tilde{Q} = \lambda\tilde{U}$ with $\lambda$ central and $\tilde{U}$ unitary,

$$
\operatorname{H}_{\lambda\tilde{U}}(x) = \lambda\tilde{U}\,x\,\lambda^{*}\tilde{U}^{\dagger} = |\lambda|^2\operatorname{Ad}_{\tilde{U}}(x),
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

The two rows for the halves and the sectors carry the same condition, and the condition can be read off the element: $\tilde{Q}$ is such a multiple exactly when $\tilde{Q}^{\dagger}\tilde{Q}$ is central, that is, when $\tilde{Q}^{\dagger}$ is a central multiple of $\tilde{Q}^{-1}$, which is what preserving $\mathbb{M}_{\pm}$ requires. This is the same class of operators that *Biquaternion Operator Representation* records as the ones preserving the whole subspace structure, and the action here is the automorphism that this class generates. For a unit outside the class the four subspaces are not merely moved among themselves: the image of each is a four-real-dimensional subspace in general position, lying in none of the six.

### The Two Minimal Left Ideals

The algebra is $M_2(\mathbb{C})$ and its simple module appears inside it as a minimal left ideal, as in *Biquaternion 2×2 Matrix Representation*. With $\tilde\Pi_1 = \tfrac12(e_0 + ie_3)$, so that $e_3\tilde\Pi_1 = i\tilde\Pi_1$ and $1-\tilde\Pi_1 = \tfrac12(e_0 - ie_3)$, the two halves of the algebra are the minimal left ideals $\mathbb{B}\tilde\Pi_1$ and $\mathbb{B}(1-\tilde\Pi_1)$. Left multiplication preserves each of them, while the conjugation action carries each to a minimal left ideal, because it is an automorphism:

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

The dagger sandwich exchanges them as well, $\operatorname{H}_{ie_1}(\tilde\Pi_1) = 1 - \tilde\Pi_1$. Neither action is a map of left modules over the algebra — $\operatorname{H}_{\tilde{Q}}(bx) \neq b\operatorname{H}_{\tilde{Q}}(x)$ in general, and the same is true of $\operatorname{Ad}_{\tilde{Q}}$ — but only the automorphism is multiplicative, and it is multiplicativity that makes the exchange of the halves a statement about the algebra rather than about one element. Since the spinor module of this article is one of the two halves, the two-sided actions either preserve the spinor module or exchange it with its opposite; this is the algebraic origin of the conjugate spinor, the second of the two chiral components.

## Relations Between the Representations

**Spinor and Clifford.** The two realizations of this article meet at the matrix algebra. The even subalgebra $\mathrm{Cl}_{1,3}^+$ is isomorphic to $M_2(\mathbb{C})$ as a real algebra, and the matrix algebra is exactly the algebra of complex-linear operators on the spinor space $\mathbb{C}^2$. Under the dictionary of the Clifford section the six bivectors are the matrices of the quaternion units and of the imaginary quaternion units, so the spinor realization is the module of the Clifford realization: the bivectors act on a spinor, and the action is the matrix multiplication. The algebra and its module belong together in the Clifford description, which is the reason that description is the one in which the spinor module is usually met.

**Spinor and the regular realization.** The left regular representation of *Biquaternion 4×4 Regular Matrix Representation* is not a third action but the spinor action taken twice. Since $\Phi(\tilde{Q}x) = \Phi(\tilde{Q})\Phi(x)$, reading the four entries of $\Phi(x)$ column by column exhibits an isomorphism of left $\mathbb{B}$-modules

$$
\mathbb{B} \longrightarrow \mathbb{C}^2 \oplus \mathbb{C}^2, \qquad
x \longmapsto \bigl(\text{first column of } \Phi(x),\ \text{second column of } \Phi(x)\bigr),
$$

on which $\tilde{Q}$ acts on each copy as $\Phi(\tilde{Q})$. The two copies are the two minimal left ideals of the section above, $\mathbb{B}\tilde\Pi_1$ and $\mathbb{B}(1-\tilde\Pi_1)$, each of real dimension $4$, and in the $\Phi$ picture they are the two column spaces. In a basis of $\mathbb{B}$ made of a basis of $\mathbb{B}\tilde\Pi_1$ followed by a basis of $\mathbb{B}(1-\tilde\Pi_1)$, the left-regular $4\times4$ matrix of $\tilde{Q}$ is therefore block diagonal with $\Phi(\tilde{Q})$ in both diagonal blocks. This is why the $2\times2$ and $4\times4$ accounts of the same algebra cannot disagree about the isomorphism $\Phi$: the second contains the first twice.

**Conjugation and the sandwich.** The conjugation action is the multiplicative core of the dagger sandwich: the two coincide exactly on the unitary elements, $\operatorname{H}_{\tilde{Q}} = \operatorname{Ad}_{\tilde{Q}}$ for $\tilde{Q}^{\dagger}\tilde{Q} = e_0$, and in general $\operatorname{H}_{\lambda\tilde{U}} = |\lambda|^2\operatorname{Ad}_{\tilde{U}}$ for $\tilde{Q} = \lambda\tilde{U}$ with central $\lambda$ and unitary $\tilde{U}$. *Biquaternion Operator Representation* reads the sandwich against this reference, and the two differ in exactly two respects: the sandwich is not multiplicative off the unitary slice, and it is not invariant under a rescaling of $\tilde{Q}$ by a central element, so that it distinguishes the class of $\tilde{Q}$ from $\tilde{Q}$ itself.

**Conjugation and the spinor module.** Because it is an automorphism, the conjugation action permutes the two minimal left ideals, and it exchanges them for any unit not commuting with $\tilde\Pi_1$, for instance $ie_1$. The spinor realization of this article is one of the two; a two-sided action either leaves the halving alone, when the acting unit commutes with $\tilde\Pi_1$, or carries the spinor module to another minimal left ideal, which is its opposite in the special case of $ie_1$ and a third module in general. This is the algebraic origin of the conjugate spinor.

**With the realizations treated elsewhere.** The remaining relations are recorded in the articles that own those realizations:

- the four-vector realization and the $2\times2$ matrix realization are related by the explicit isomorphism that reads the components $Q_\mu$ off the matrix entries;
- the $2\times2$ matrix realization is related to the Clifford realization by $\mathrm{Cl}_{1,3}^+ \cong M_2(\mathbb{C})$, the same isomorphism that carries the bivectors to the matrices;
- the conjugation action is the automorphism group of the algebra acting on itself, and it is the reference against which the operator realization is read;
- the $4\times4$ regular realization is the algebra acting on itself, and the operator realization is the element as a linear operator on the algebra, both of them read against the matrix realization;
- the polar realizations are the algebraic realizations restricted to the unit-norm slice and factorised by the exponential.

All of them present the same algebra. The choice of realization is a choice of how to write it, and different choices are useful for different purposes.

## The Role of Choices

Each representation involves a choice, and different choices give equivalent but not identical representations.

- **Spinor representation:** the choice of the basis of $\mathbb{C}^2$, which is determined by the choice of the matrix realization.
- **Clifford algebra representation:** the choice of the gamma matrices, which is determined by the choice of the bilinear form and the basis of the underlying vector space.
- **Conjugation action:** the choice of the unit $\tilde{Q}$, which is redundant, since $\operatorname{Ad}_{\lambda\tilde{Q}} = \operatorname{Ad}_{\tilde{Q}}$ for every nonzero central $\lambda$; the action depends on $\tilde{Q}$ only through its class in $\mathbb{B}^{\times}/\mathbb{C}_{\mathbb{B}}^{\times}$.

The choices belonging to the other realizations are recorded in their own articles. Different choices give representations that are related by conjugation, and the algebraic structure of the biquaternion algebra is the same in all of them. The choices are a matter of convention and convenience, not of content.

## Summary

The biquaternion algebra admits three algebraic realizations that are not treated in dedicated articles of this series:

| Realization | the element is written as | the reading | Useful for |
|---|---|---|---|
| Spinor | the $2\times2$ matrix $\Phi(\tilde{Q})$ | object, and operator on a column $\begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix}$ | Module structure, the group of unit-norm elements, the Clifford multiplication |
| Clifford algebra | an element of $\mathrm{Cl}_{1,3}^+$ | object | Geometry, generalization in dimension and signature |
| Conjugation action | the map $x \mapsto \tilde{Q}x\tilde{Q}^{-1}$ | operator on the algebra | The automorphism group, the chiral halves, the reference for the dagger sandwich |

The first two columns are independent: the writing fixes an array, the reading fixes what is done with it, and the same matrix appears as an object and as an operator at once. The realization is a choice neither of size nor of role, which is why a four-vector, a $2\times2$ array and a $4\times4$ array can all carry the same object, and any of them can carry an action on it.

In the Clifford realization the isomorphism is fixed by $e_1 \mapsto \gamma^2\gamma^3$, $e_2 \mapsto \gamma^3\gamma^1$, $e_3 \mapsto \gamma^1\gamma^2$ and $i \mapsto -\gamma^0\gamma^1\gamma^2\gamma^3$ under the mostly-minus form $g = \mathrm{diag}(+1,-1,-1,-1)$, so that all six bivectors correspond to the quaternion units with positive signs, and it carries the Clifford product to the biquaternion product and the Clifford norm to the norm form on the even part; the $1,3$ form is the one carried by the Hermitian subspace $\mathbb{M}_+$.

The matrix, four-vector and regular realizations, the norm form read in each of them, and the explicit isomorphisms between them, are the subject of their own articles. Here only the three realizations above are derived, and the relations recorded are the ones they have with each other and with the realizations treated elsewhere.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $e_0, e_1, e_2, e_3$ | Algebra basis, $e_0 = 1$, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary |
| $Q_\mu = q_\mu + i q'_\mu$ | Complex coefficients of $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ | Quaternion subspace and Hermitian subspace of $\mathbb{B}$ |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form |
| $\psi$ | Spinor, an element of $\mathbb{C}^2$ |
| $\langle \psi, \phi \rangle = \psi_1^* \phi_1 + \psi_2^* \phi_2$ | Hermitian inner product on spinors |
| $\mathrm{Cl}_{1,3}$ | Clifford algebra of signature $(1,3)$; $\mathbb{B} \cong \mathrm{Cl}_{1,3}^+$ |
| $\gamma^\mu$ | Clifford generators, $(\gamma^0)^2 = +1$, $(\gamma^j)^2 = -1$ |
| $\omega = \gamma^0\gamma^1\gamma^2\gamma^3$ | Pseudoscalar, $\omega^2 = -1$, central in $\mathrm{Cl}_{1,3}^+$ |
| $\operatorname{Ad}_{\tilde{Q}}(x) = \tilde{Q}x\tilde{Q}^{-1}$ | Conjugation action of a unit, the inner automorphism |
| $\operatorname{H}_{\tilde{Q}}(x) = \tilde{Q}x\tilde{Q}^{\dagger}$ | The dagger sandwich of *Biquaternion Operator Representation* |
| $\tilde\Pi_1 = \tfrac12(e_0 + ie_3)$ | Idempotent, $\mathbb{B}\tilde\Pi_1$ a minimal left ideal of real dimension $4$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- J. P. Ward, *Quaternions and Cayley Numbers* (Kluwer, 1997), Chapter 3, for the matrix representations of biquaternions.
- S. J. Sangwine, T. A. Ell, N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* 21 (2011) 607–636, for the applied representation theory.

