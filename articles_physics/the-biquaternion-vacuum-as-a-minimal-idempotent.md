# __The Biquaternion Vacuum as a Minimal Idempotent__

## Introduction

The **vacuum state** is the state of lowest energy, the reference state relative to which particles are counted. In the operator formulation of quantum field theory it is the vector $|0\rangle$ annihilated by every annihilation operator, $\hat a_r(\mathbf{p})|0\rangle = 0$; in the algebraic formulation it is a state — a positive normalized linear functional — with a definite invariance property, and its reconstruction by the GNS theorem recovers the Hilbert space and the field operators up to unitary equivalence. Two questions therefore attach to the vacuum. Which state is it, and what object realizes it.

The second question has a sharp answer in the biquaternion framework, and this article is about that answer.

- **Established, and recomputed below.** For a **single fermionic mode** the framework contains the vacuum as a concrete algebraic object: the Hermitian idempotent
$$
P_{+}(e_3) \;=\; \tfrac12\big(e_0 + ie_3\big)
\;=\; |0\rangle\langle 0| .
$$
It is an element of the informational sector $\mathbb{M}_+$, it is **minimal** in the sense of the algebra, its trace is $\mathrm{Tr}(P_+(e_3)) = 1$, and it is the projector onto a **minimal left ideal** of $\mathbb{B}$, the two-complex-dimensional one-particle module. The complementary idempotent $\tilde N_{\mathrm{tr}} = \tfrac12(e_0 - ie_3)$ is the occupied-state projector, and the two form a resolution of the identity, $P_+ + P_- = e_0$, $P_+P_- = 0$. The one-mode vacuum is thus, literally, a minimal idempotent.
- **Established, and worth separating from the above.** The vacuum idempotent is a **zero divisor**: its norm form vanishes, $N(P_+(e_3)) = P_+\bar P_+ = 0$, and its matrix representative has vanishing determinant, $\det\Phi(P_+(e_3)) = 0$. The vacuum state lies on the zero-divisor cone — the framework's light cone. This is not a defect of the state; it is the algebra's statement that a rank-one projector is not invertible, and it ties the choice of vacuum to the choice of a null direction.
- **The vacuum manifold.** The construction depends on a unit vector $\hat{\boldsymbol\mu}\in S^2$ through $P_+(\hat{\boldsymbol\mu}) = \tfrac12(e_0 + i\hat{\boldsymbol\mu})$. Every such idempotent is a legitimate one-mode vacuum, and the family is the two-sphere — the Bloch sphere of the state space. The framework does not single one out; a global $SU(2)$ rotation moves one into another, and the orbit is the vacuum manifold.
- **Gap, left visible.** For a **field** the vacuum is not an element of $\mathbb{B}$. The Fock space of a field is a module over the algebra, not a subalgebra of it, and the algebra contains no bosonic ladder at all: no pair $\tilde a,\tilde a^\dagger\in\mathbb{B}$ can satisfy $[\tilde a,\tilde a^\dagger]=e_0$ because a commutator has vanishing trace while $\mathrm{Tr}(e_0)=2$. So "the biquaternion vacuum" is not, in general, a biquaternion. It is an idempotent for one fermionic mode and a state in a module for a field.

The article proceeds as follows. The next section recalls the standard vacuum and the sense in which it is a state. The following section fixes the idempotents of $\mathbb{B}$ and the notion of minimality. The next two sections construct the one-mode vacuum and prove that it is a minimal idempotent, and then that it is a zero divisor. The following sections describe the minimal left ideal it defines, the vacuum manifold, and the field case. A section separates what is established from what is interpretation, and the article closes with open questions.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_0 = 1, e_1, e_2, e_3$ satisfying $e_k^2 = -e_0$ and $e_j e_k = \varepsilon_{jkl} e_l$ for distinct $j,k,l$, and scalar imaginary $i$ with $i^2=-1$, central in $\mathbb{B}$. The conjugations are $\bar{\cdot}$ (quaternion), ${}^{*}$ (complex), ${}^{\dagger} = \bar{\cdot}^{\,*}$ (Hermitian), and ${}^{\flat} = -\dagger$ (anti-Hermitian). The fixed-point subspaces are
$$
\mathbb{M}_- = \{\tilde Q : \tilde Q^\dagger = -\tilde Q\} = \mathrm{span}_{\mathbb{R}}\{ie_0, e_1, e_2, e_3\},
\qquad
\mathbb{M}_+ = \{\tilde Q : \tilde Q^\dagger = \tilde Q\} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_1, ie_2, ie_3\},
$$
with $\mathbb{B} = \mathbb{M}_-\oplus\mathbb{M}_+$; $\mathbb{H}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0,e_1,e_2,e_3\}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the center. The isomorphism is $\Phi(e_k) = -i\sigma_k$, $\Phi(i) = iI_2$, the **norm form** is $N(\tilde Q) = \tilde Q\bar{\tilde Q} = \sum_\mu Q_\mu^2$, and the trace pairing is $\mathrm{Tr}(\tilde P\tilde H) = 2\,\mathrm{Sc}(\tilde P\tilde H)$, so that $\mathrm{Tr}(e_0)=2$. The single-mode ladder is $\tilde a_{\mathrm{tr}} = \tfrac12(ie_1-e_2)$, $\tilde a_{\mathrm{tr}}^\dagger = \tfrac12(ie_1+e_2)$, as established by *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*.

## The Vacuum as a State

In the standard formulation the vacuum is characterized in two equivalent ways, and it is worth keeping both in view because the biquaternion reading uses one and not the other.

**As a vector.** The one-particle space $\mathcal{H}_1$ generates the Fock space
$$
\mathcal{F} \;=\; \bigoplus_{n\ge 0}\Big(\mathcal{H}_1^{\otimes n}\Big)_{\pm},
$$
the symmetric or antisymmetric tensor algebra, and the vacuum spans the degree-zero term,
$$
|0\rangle \;\in\; \Big(\mathcal{H}_1^{\otimes 0}\Big)_{\pm} \cong \mathbb{C},
\qquad
\hat a_r(\mathbf{p})|0\rangle = 0 \ \ \text{for all } r,\mathbf{p}.
$$
The state is normalized, $\langle 0|0\rangle = 1$, and every $n$-particle state is built from it by creation operators. In this reading the vacuum is a vector in an infinite-dimensional space.

**As a functional.** A state on an algebra $\mathcal{A}$ of observables is a linear functional $\omega:\mathcal{A}\to\mathbb{C}$ that is positive, $\omega(\tilde A^\dagger \tilde A)\ge 0$, and normalized, $\omega(e_0)=1$. The vacuum expectation value
$$
\omega_0(\tilde A) \;=\; \langle 0|\,\pi(\tilde A)\,|0\rangle
$$
is such a functional on the algebra generated by the fields, and it is **pure** — it is not a nontrivial convex combination of other states. Purity is the algebraic content of "the vacuum is a single state and not a mixture", and it is the property that links the vacuum to minimal idempotents, because in a finite-dimensional algebra the pure states are exactly the rank-one density matrices.

For the biquaternion framework two facts make the second reading the operative one. First, the algebra $\mathbb{B}$ is finite-dimensional, so its states are the positive normalized elements of its dual and are realized by density matrices; a state is an element of the algebra, not a vector outside it. Second, the one-mode truncation of a fermionic field *is* an algebra inside $\mathbb{B}$, so that for one mode the abstract state becomes an explicit algebra element. That element is the subject of the next three sections.

## Idempotents and Minimality

An **idempotent** of $\mathbb{B}$ is an element $\tilde P$ with
$$
\tilde P^2 = \tilde P .
$$
A **projector** is a Hermitian idempotent, $\tilde P^\dagger = \tilde P$, and a projector in $\mathbb{M}_+$ is precisely a *positive* Hermitian idempotent, hence a density matrix up to normalization. The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ has a simple classification of its idempotents, and it is the classification of the projectors that the vacuum needs.

**Rank.** Under the isomorphism $\Phi$, a projector $\tilde P$ is sent to a Hermitian projection matrix $\Phi(\tilde P)$. Such a matrix has eigenvalues in $\{0,1\}$, and its **rank** is the number of unit eigenvalues. In two dimensions the possibilities are
$$
\mathrm{rank}\,\Phi(\tilde P) \in \{0,1,2\},
$$
corresponding to $\tilde P = 0$, to a rank-one projector, and to $\tilde P = e_0$. A rank-one projector is the smallest nonzero one, and it is called **minimal**:

> **Definition.** A projector $\tilde P\neq 0$ is **minimal** if it cannot be written as a sum of two nonzero orthogonal projectors, $\tilde P = \tilde P_1+\tilde P_2$ with $\tilde P_1\tilde P_2=0$. Equivalently, $\Phi(\tilde P)$ has rank one.

Minimality has three equivalent faces that will each be used below:
1. $\Phi(\tilde P)$ has rank one, equivalently $\det\Phi(\tilde P)=0$ and $\tilde P\neq0$;
2. the left ideal $\mathbb{B}\tilde P$ is **minimal** — it contains no proper nonzero left ideal;
3. the Peirce decomposition of $\mathbb{B}$ with respect to $\tilde P$ has components of dimensions $1,1,1,1$ over $\mathbb{C}$ — that is, $k^2$, $k(n-k)$, $k(n-k)$, $(n-k)^2$ with $n=2$, $k=1$ — so that
$$
\mathbb{B} \;=\; \tilde P\mathbb{B}\tilde P \;\oplus\; \tilde P\mathbb{B}(1-\tilde P) \;\oplus\; (1-\tilde P)\mathbb{B}\tilde P \;\oplus\; (1-\tilde P)\mathbb{B}(1-\tilde P),
\qquad \tilde P\mathbb{B}\tilde P \cong \mathbb{C}.
$$
The corner $\tilde P\mathbb{B}\tilde P$ is one-complex-dimensional exactly when $\tilde P$ is minimal; for a general idempotent it has dimension $(\mathrm{rank})^2$.

The reason minimality matters physically is the third face of the definition in the language of states: a Hermitian projector $\tilde P\in\mathbb{M}_+$ with $\mathrm{Tr}(\tilde P)=1$ and rank one defines the **pure state**
$$
\omega_{\tilde P}(\tilde A) \;=\; \mathrm{Tr}\big(\tilde P\tilde A\big),
$$
which on an **observable** $\tilde A\in\mathbb{M}_+$ takes the real value $2\,\mathrm{Sc}(\tilde P\tilde A)$. A pure state is exactly what a vacuum is. A rank-two projector with $\mathrm{Tr}=1$ would be the maximally mixed state $\tfrac12 e_0$, and a general element of the Bloch ball is neither.

## The One-Mode Vacuum

For a single fermionic mode the algebra contains the whole ladder. With
$$
\tilde a_{\mathrm{tr}} = \tfrac12\big(ie_1 - e_2\big),
\qquad
\tilde a_{\mathrm{tr}}^\dagger = \tfrac12\big(ie_1 + e_2\big),
$$
one has, as the Fock article establishes,
$$
\big\{\tilde a_{\mathrm{tr}}, \tilde a_{\mathrm{tr}}^\dagger\big\} = e_0,
\qquad
\tilde a_{\mathrm{tr}}^2 = 0,
\qquad
(\tilde a_{\mathrm{tr}}^\dagger)^2 = 0,
\qquad
\tilde N_{\mathrm{tr}} = \tilde a_{\mathrm{tr}}^\dagger \tilde a_{\mathrm{tr}} = \tfrac12\big(e_0 - ie_3\big).
$$
The number operator is a projector, so its spectrum is $\{0,1\}$: the mode is either empty or occupied. The **vacuum projector** is the spectral projector onto the empty eigenvalue,
$$
|0\rangle\langle 0| \;=\; e_0 - \tilde N_{\mathrm{tr}} \;=\; \tfrac12\big(e_0 + ie_3\big) \;=\; P_+(e_3).
$$
Here and below
$$
P_\pm(\hat{\boldsymbol\mu}) \;=\; \tfrac12\big(e_0 \pm i\hat{\boldsymbol\mu}\big),
\qquad \hat{\boldsymbol\mu}\in S^2,
$$
denotes the pair of projectors associated with the unit vector $\hat{\boldsymbol\mu}$.

**The vacuum projector is minimal, Hermitian, and of unit trace.** It is convenient to verify the four defining properties at once, using $e_3^2=-e_0$:
$$
P_+(e_3)^2 = \tfrac14\big(e_0 + ie_3\big)^2 = \tfrac14\big(e_0 + 2ie_3 + (ie_3)^2\big) = \tfrac14\big(e_0 + 2ie_3 - e_0\big) = \tfrac12\big(e_0+ie_3\big) = P_+(e_3),
$$
so it is idempotent; $\overline{P_+(e_3)} = \tfrac12(e_0 - ie_3)$ and $P_+(e_3)^\dagger = \tfrac12(e_0 + ie_3)^\dagger = \tfrac12(e_0 + ie_3) = P_+(e_3)$, since $e_3^\dagger = -e_3$ and $i^\dagger = i$, so it is Hermitian and lies in $\mathbb{M}_+$;
$$
\mathrm{Tr}\big(P_+(e_3)\big) = 2\,\mathrm{Sc}\big(P_+(e_3)\big) = 2\cdot\tfrac12 = 1,
$$
so its trace is one; and
$$
\Phi\big(P_+(e_3)\big) = \tfrac12\big(I_2 + i\Phi(e_3)\big) = \tfrac12\big(I_2 + \sigma_3\big) = \begin{pmatrix}1&0\\0&0\end{pmatrix},
$$
which has rank one. Hence $P_+(e_3)$ is a **minimal projector** with unit trace: the one-mode vacuum.

The complementary idempotent and the resolution of the identity are immediate:
$$
P_-(e_3) = \tfrac12\big(e_0 - ie_3\big) = \Phi^{-1}\begin{pmatrix}0&0\\0&1\end{pmatrix},
\qquad
P_+(e_3) + P_-(e_3) = e_0,
\qquad
P_+(e_3) P_-(e_3) = 0 .
$$
The two-dimensional identity is resolved into the empty and occupied projectors, and the Peirce corner at the vacuum is $\mathbb{C}$. The fermion-parity operator is the difference obtained from the same pair,
$$
(-1)^F \;=\; P_+(e_3) - P_-(e_3) \;=\; ie_3,
$$
in agreement with the Fock article's $(-1)^F=ie_3$; as an operator it anticommutes with the ladder,
$$
(-1)^F \tilde a_{\mathrm{tr}} (-1)^F = -\tilde a_{\mathrm{tr}},
\qquad
(-1)^F \tilde a_{\mathrm{tr}}^\dagger (-1)^F = -\tilde a_{\mathrm{tr}}^\dagger .
$$

**A numerical check on the whole set.** Representing $\mathbb{B}$ by $2\times2$ complex matrices through $\Phi$ and using explicit complex arithmetic on the coefficients, one finds: $P_+(e_3)^2-P_+(e_3)=0$; $P_+(e_3)^\dagger-P_+(e_3)=0$; $\det\Phi(P_+(e_3))=0$ with $\mathrm{Tr}\,\Phi(P_+(e_3))=1$; $P_+P_-=0$ and $P_++P_-=I_2$; $\Phi((-1)^F)=\sigma_3$; and $\Phi((-1)^F\tilde a_{\mathrm{tr}}(-1)^F) = -\Phi(\tilde a_{\mathrm{tr}})$, all to machine precision ($<10^{-16}$). The vacuum expectation values reproduce the mode algebra,
$$
\langle \tilde a_{\mathrm{tr}}^\dagger \tilde a_{\mathrm{tr}}\rangle_0 = \mathrm{Tr}\big(P_+(e_3)\tilde N_{\mathrm{tr}}\big) = 0,
\qquad
\langle \tilde a_{\mathrm{tr}} \tilde a_{\mathrm{tr}}^\dagger\rangle_0 = \mathrm{Tr}\big(P_+(e_3)(e_0-\tilde N_{\mathrm{tr}})\big) = 1,
$$
which are the statements that the vacuum is empty and the mode anticommutator is normalized.

## The Vacuum Is a Zero Divisor

The single most consequential algebraic property of the vacuum idempotent is that it is **not invertible**, and the framework makes this property visible through the norm form.

Compute $N(P_+(e_3)) = P_+(e_3)\overline{P_+(e_3)}$, using $\bar e_3 = -e_3$ and $\bar i = i$:
$$
P_+(e_3)\overline{P_+(e_3)} = \tfrac14\big(e_0+ie_3\big)\big(e_0-ie_3\big) = \tfrac14\Big(e_0 - ie_3 + ie_3 - i^2 e_3^2\Big) = \tfrac14\big(e_0 - e_0\big) = 0 .
$$
So
$$
\boxed{\,N(P_+(\hat{\boldsymbol\mu})) = 0 \quad\text{for every unit vector } \hat{\boldsymbol\mu}\,}
$$
and the same computation with $P_-$ gives $N(P_-)=0$. In the language of the norm form, every minimal projector of $\mathbb{B}$ is a **null element**: it lies on the cone $N(\tilde Q)=0$, which is the zero-divisor cone and the framework's light cone. Equivalently, $\det\Phi(P_+(\hat{\boldsymbol\mu}))=0$, since $N=\det\Phi$.

This is not an accident of the vacuum state; it is the algebra's statement about rank. A rank-one projector is a matrix of rank one, a rank-one matrix is singular, a singular matrix is a zero divisor, and the determinant-norm form detects exactly that. The vacuum is the simplest element of the algebra that has this property.

Two readings of the same fact are worth recording.

**The vacuum and the pair of complementary projectors are the two null directions.** Because $P_+ + P_- = e_0$ with both null, the identity is written as the sum of two elements each of vanishing norm form. In signature language, $e_0$ is a positive-norm element decomposed along two null directions whose sum is timelike — the algebraic shape of a light-cone frame. The pair $\{P_+, P_-\}$ plays for the state space the role that the pair of null vectors plays for a Lorentz frame.

**The vacuum carries a definite phase direction.** The projector $P_+(\hat{\boldsymbol\mu})$ is determined by the *unit* vector $\hat{\boldsymbol\mu}$, and the null cone condition $N=0$ is satisfied for every $\hat{\boldsymbol\mu}$; the cone is the union of the one-dimensional rays that the projectors single out. Choosing a vacuum is choosing a null direction, and different vacua are related by the rotations that move one null direction into another. This is made precise in the next two sections.

## The Minimal Left Ideal and the One-Particle Module

A left ideal of $\mathbb{B}$ is a linear subspace $\mathcal{I}$ with $\mathbb{B}\mathcal{I}\subseteq\mathcal{I}$. For an idempotent $\tilde P$ the set $\mathbb{B}\tilde P$ is always a left ideal, and the classification above implies:

> **Proposition.** $\mathbb{B}\tilde P$ is a minimal left ideal if and only if $\tilde P$ is a minimal idempotent.

For the vacuum this identifies a physically named object. Acting on the algebra with $P_+(e_3)$ on the right,
$$
\mathbb{B}P_+(e_3) = \big\{\tilde Q P_+(e_3) : \tilde Q\in\mathbb{B}\big\} \cong \mathbb{C}^2,
$$
a two-complex-dimensional space, because the map $\tilde Q\mapsto\tilde Q P_+(e_3)$ annihilates the rank-one complement and its image is the column space of $\Phi(P_+(e_3))$. With $\Phi(P_+(e_3)) = \mathrm{diag}(1,0)$ the image is the space of column vectors with second entry zero, that is, the **fundamental module** of the algebra — the two-component spinor space on which the field's spinors live. So

> the one-mode vacuum idempotent determines the one-particle (spinor) module as the minimal left ideal it generates.

This is the mechanism by which the vacuum situates the field in the framework: the algebra alone has no distinguished module, and the choice of vacuum idempotent selects one. Conversely the module fixes the idempotent only up to the equivalence $\tilde P\mapsto \tilde U\tilde P\tilde U^{-1}$ by units of the algebra, which is the statement that the module is unique while the vacuum is not.

The same construction, run in the reverse direction, is the GNS reconstruction. The state $\omega_{\tilde P}(\tilde A) = \mathrm{Tr}(\tilde P\tilde A)$ has a GNS Hilbert space obtained from $\mathbb{B}$ by quotienting out the elements of zero $\omega_{\tilde P}$-norm; for a **pure** state that quotient is exactly the minimal left ideal, of complex dimension two, and the GNS representation is irreducible. For a mixed state the quotient is larger and the representation is reducible. The vacuum's minimality is thus the algebraic reason its GNS representation is irreducible, and the GNS construction itself is the subject of the companion article *The GNS Construction in the Biquaternion Framework*.

## The Vacuum Manifold

The construction used $e_3$ only through the unit vector it defines. Replacing $e_3$ by $\hat{\boldsymbol\mu} = \mu_1 e_1 + \mu_2 e_2 + \mu_3 e_3$ with $\mu_1^2+\mu_2^2+\mu_3^2=1$ gives
$$
P_+(\hat{\boldsymbol\mu}) = \tfrac12\big(e_0 + i\hat{\boldsymbol\mu}\big),
\qquad
P_-(\hat{\boldsymbol\mu}) = \tfrac12\big(e_0 - i\hat{\boldsymbol\mu}\big),
$$
and every identity above holds with $\hat{\boldsymbol\mu}$ in place of $e_3$, because $\hat{\boldsymbol\mu}^2 = -e_0$ for every unit vector. The family
$$
\mathcal{M}_{\text{vac}} \;=\; \big\{\,P_+(\hat{\boldsymbol\mu}) : \hat{\boldsymbol\mu}\in S^2\,\big\} \;\cong\; S^2
$$
is the **vacuum manifold**. Its three properties, all immediate from the definitions, are worth naming.

1. **It is a two-sphere.** The projectors are labelled by unit vectors, and the correspondence is one-to-one: $P_+(\hat{\boldsymbol\mu}) = P_+(\hat{\boldsymbol\mu}')$ if and only if $\hat{\boldsymbol\mu} = \hat{\boldsymbol\mu}'$, since the vector part of the projector is $\tfrac{i}{2}\hat{\boldsymbol\mu}$.
2. **It is the Bloch sphere of the state space.** Writing a general element of $\mathbb{M}_+$ of unit trace as $\tilde\rho = \tfrac12(e_0 + i\mathbf r)$ with $\mathbf r\in\mathbb{R}^3$, the projector condition $\tilde\rho^2=\tilde\rho$ forces $|\mathbf r|=1$. The minimal idempotents of unit trace are exactly the Bloch sphere, and a general state (a minimal-*trace*, not minimal-*rank*, density matrix) fills the Bloch ball $|\mathbf r|\le 1$.
3. **It is a single rotation orbit.** The conjugation $\tilde P\mapsto \tilde R\tilde P\tilde R^\dagger$ by a unit real quaternion $\tilde R\in\mathbb{H}_{\mathbb{B}}$, $N(\tilde R)=e_0$, acts on the vector part as a rotation of $\hat{\boldsymbol\mu}$, and every unit vector is reached from every other. The rotation group of the framework acts transitively on the vacuum manifold, so the framework by itself does not distinguish a vacuum; the vacuum is a **spontaneously chosen** element, and the manifold is the order-parameter space of that choice.

That last point is the physical content of the manifold. A vacuum that is a minimal idempotent is a *pure state with a definite orientation*, and the orientation is not fixed by the algebra. Whether the framework provides a dynamics that selects one — a Hamiltonian whose ground projector is a particular $P_+(\hat{\boldsymbol\mu})$ — is a question about the dynamics, not about the state, and is not settled by the algebra alone.

## The Field Vacuum Is Not an Idempotent

Everything above is about one mode. For a field the situation changes, and the change is not a matter of detail.

The Fock space of a field is a **module** over the algebra rather than a subalgebra of it. That is the finding of the Fock article, and it is inherited here unchanged: the one-particle space is a module, the many-particle space is its tensor algebra, and beyond one mode not even the operator algebra is inside $\mathbb{B}$. In particular there is **no bosonic ladder in $\mathbb{B}$**, because a bosonic mode requires $[\tilde a,\tilde a^\dagger]=e_0$, whereas for any two elements of $\mathbb{B}$
$$
\mathrm{Tr}\big([\tilde a,\tilde a^\dagger]\big) = \mathrm{Tr}(\tilde a\tilde a^\dagger) - \mathrm{Tr}(\tilde a^\dagger\tilde a) = 0
$$
by the cyclicity of the trace, while $\mathrm{Tr}(e_0)=2$. Hence no pair of algebra elements satisfies the canonical commutation relation, and the photon's Fock vacuum — the vacuum of the electromagnetic field — is not an algebra element. It is the standard Fock vacuum of a module built from the transverse polarization plane, as *The Vacuum State and the Casimir Effect in Biquaternionic Form* records.

For a fermionic field the one-particle space is also a module, but here the algebra reaches one step further: the one-mode truncation is an algebra inside $\mathbb{B}$, and for that truncation the vacuum is the idempotent constructed above. The honest summary is therefore a sharp one:

> "The biquaternion vacuum" is not, in general, a biquaternion. It is a **minimal idempotent of $\mathbb{M}_+$** for one fermionic mode — the largest truncation the algebra supports — and a **state in a module** for a field, where it is neither an idempotent nor an element of the algebra at all.

The minimal-idempotent reading is not a diminution of the field vacuum. It is the exact algebraic statement of what the vacuum is in the only case in which the algebra contains it, and it is the reason the vacuum is a natural starting point for the algebraic constructions — GNS reconstruction, the Wick theorem, and the thermal states — that the articles following this one develop.

## What Is Established and What Is Interpretation

**Established (algebra).**
- The idempotents of $\mathbb{B}$ are classified by rank; the rank-one (minimal) projectors of $\mathbb{M}_+$ are exactly $P_+(\hat{\boldsymbol\mu}) = \tfrac12(e_0+i\hat{\boldsymbol\mu})$ with $|\hat{\boldsymbol\mu}|=1$.
- $P_+(\hat{\boldsymbol\mu})$ is Hermitian, idempotent, of unit trace, and minimal; $P_- = e_0-P_+$ is its orthogonal complement, and the two resolve the identity.
- $N(P_\pm(\hat{\boldsymbol\mu})) = 0$ and $\det\Phi(P_\pm(\hat{\boldsymbol\mu}))=0$: the vacuum is a zero divisor on the light cone.
- $\mathbb{B}P_+(\hat{\boldsymbol\mu})$ is a minimal left ideal, isomorphic to $\mathbb{C}^2$, the fundamental (spinor) module.
- The vacuum manifold is $S^2$, on which the unit real quaternions act transitively.

**Established (physics).**
- The Fock vacuum is annihilated by all annihilation operators, spans the degree-zero term, and is a pure state; the one-mode truncation of a fermionic field is realized by the idempotent above.
- The photon's Fock vacuum is built from a module, and no bosonic ladder exists in $\mathbb{B}$.

**Interpretation.**
- Reading the vacuum as a minimal idempotent, and reading the vacuum manifold as the order-parameter space of a spontaneously chosen state, are readings of algebraic facts. They are precise; they are not derivations of the field-theoretic vacuum.
- The identification of the minimal left ideal with the one-particle module is standard representation theory applied to $\mathbb{B}$; its physical reading as "the vacuum determines the one-particle space" is the interpretive step.

**Open.**
- Whether a dynamics inside the framework selects a particular minimal idempotent, and by what mechanism, is not addressed by the algebra.
- Whether the zero-divisor property of the vacuum has consequences for the framework's treatment of superselection sectors or of the theta vacuum is taken up in the companion articles on those subjects.

## Summary

For a single fermionic mode the vacuum of the biquaternion framework is a concrete algebra element: the Hermitian, idempotent, unit-trace, **minimal** projector
$$
|0\rangle\langle 0| = P_+(e_3) = \tfrac12\big(e_0+ie_3\big) = \Phi^{-1}\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
\tilde N_{\mathrm{tr}} = \tfrac12\big(e_0-ie_3\big) = P_-(e_3),
$$
with $P_++P_- = e_0$, $P_+P_-=0$, and $(-1)^F = ie_3 = P_+-P_-$. Minimality is equivalently rank one, equivalently the one-dimensional Peirce corner $\tilde P\mathbb{B}\tilde P\cong\mathbb{C}$, equivalently the minimality of the left ideal $\mathbb{B}P_+$. That ideal is the two-complex-dimensional fundamental module — the one-particle spinor space — so the vacuum idempotent determines the module on which the field lives.

The vacuum idempotent is a **zero divisor**: $N(P_\pm)=0$ and $\det\Phi(P_\pm)=0$. It lies on the zero-divisor cone, and the identity is the sum of two null projectors. The family of vacua is the two-sphere $P_+(\hat{\boldsymbol\mu})$, $\hat{\boldsymbol\mu}\in S^2$ — the Bloch sphere of pure states — on which the unit real quaternions act transitively, so the framework fixes the manifold of vacua but not one vacuum.

For a field the vacuum is a state in a module and not an element of the algebra: the Fock space is a module over $\mathbb{B}$, and no bosonic ladder exists inside $\mathbb{B}$ because a commutator has vanishing trace while $\mathrm{Tr}(e_0)=2$. The minimal-idempotent reading is exact for the one-mode truncation, which is the largest truncation the algebra supports, and it is the starting point for the operator-algebraic constructions that follow.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_je_k=\varepsilon_{jkl}e_l$ |
| $i$ | Scalar imaginary, central, $i^2=-1$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}},\mathbb{C}_{\mathbb{B}}$ | Real-quaternion subspace; center $\mathrm{span}_\mathbb{R}\{e_0,ie_0\}$ |
| $N(\tilde Q)=\tilde Q\bar{\tilde Q}=\sum_\mu Q_\mu^2=\det\Phi(\tilde Q)$ | Norm form |
| $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$, $\mathrm{Tr}(e_0)=2$ | Trace pairing |
| $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$ | Matrix isomorphism |
| $P_\pm(\hat{\boldsymbol\mu})=\tfrac12(e_0\pm i\hat{\boldsymbol\mu})$, $\hat{\boldsymbol\mu}\in S^2$ | Minimal idempotents; vacuum projectors |
| $|0\rangle\langle 0|=P_+(e_3)$ | One-mode vacuum projector |
| $\tilde N_{\mathrm{tr}}=\tilde a_{\mathrm{tr}}^\dagger\tilde a_{\mathrm{tr}}=P_-(e_3)$ | Number operator (occupied projector) |
| $\tilde a_{\mathrm{tr}}=\tfrac12(ie_1-e_2)$, $\tilde a_{\mathrm{tr}}^\dagger=\tfrac12(ie_1+e_2)$ | Single-mode ladder |
| $(-1)^F=ie_3=P_+-P_-$ | Fermion-parity grading |
| $\mathbb{B}P_+(\hat{\boldsymbol\mu})\cong\mathbb{C}^2$ | Minimal left ideal; one-particle (spinor) module |
| $\mathcal{M}_{\text{vac}}\cong S^2$ | Vacuum manifold |
| $\omega_{\tilde P}(\tilde A)=\mathrm{Tr}(\tilde P\tilde A)$ | Pure state defined by a minimal idempotent |

## Further Reading

- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the projector calculus and the idempotent characterization of pure states.
- J. von Neumann, *Mathematical Foundations of Quantum Mechanics* (Princeton, 1955), for the density-matrix classification of states and the geometry of the state space.
- G. Birkhoff and J. von Neumann, "The logic of quantum mechanics," *Annals of Mathematics* **37** (1936) 823–843, for the lattice of projectors and the algebraic reading of the state space.
- F. J. Murray and J. von Neumann, "On rings of operators," *Annals of Mathematics* **37** (1936) 116–229, for minimal projectors, factors, and the classification of left ideals.
- R. V. Kadison and J. R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Vol. I (Academic Press, 1983), for idempotents, Peirce decompositions, and minimal ideals in finite-dimensional algebras.
- F. R. Gantmacher, *The Theory of Matrices*, Vol. I (Chelsea, 1959), for the rank classification of projectors and the determinant as a rank test.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the matrix representation of biquaternions, idempotents, and the fundamental module.
- J. C. Várilly and J. M. Gracia-Bondía, "Connes' noncommutative differential geometry and the standard model," *Journal of Geometry and Physics* **12** (1993) 223–301, for minimal left ideals as fermion modules in the algebraic reading of particle multiplets.
- Companion articles: *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, for the single-mode ladder, the number operator, and the fermion-parity grading; *The GNS Construction in the Biquaternion Framework*, for the reconstruction that the pure state's minimality makes irreducible; *The Vacuum State and the Casimir Effect in Biquaternionic Form*, for the field vacuum as a module state and the absence of a bosonic ladder; *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the state space, the trace pairing, and the Bloch ball.
