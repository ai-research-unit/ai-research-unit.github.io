# __The Biquaternion Vacuum as a Minimal Idempotent__

## Introduction

The **vacuum state** is the state of lowest energy, the reference state relative to which particles are counted. In the operator formulation of quantum field theory it is the vector $|0\rangle$ annihilated by every annihilation operator, $a_r^{\mathrm{fop}}(\vec p)|0\rangle = 0$; in the algebraic formulation it is a state — a positive normalized linear functional — with a definite invariance property, and its reconstruction by the GNS theorem recovers the Hilbert space and the field operators up to unitary equivalence. Two questions therefore attach to the vacuum. Which state is it, and what object realises it?

The second question has a sharp answer in the biquaternion framework, and this article is about that answer.

- **Established, and recomputed below.** For a **single fermionic mode** the framework contains the vacuum as a concrete algebraic object: the Hermitian idempotent
$$
\tilde\Pi_+ \;=\; \tfrac12\big(e_t + i\vec e_z\big)
\;=\; |0\rangle\langle 0| .
$$

Here $i\vec e_z$ is a root of $+1$, $(i\vec e_z)^2=e_t$, and $\tilde\Pi_+$ and $\tilde\Pi_-$ are its two associated idempotents.
It is an element of the informational sector $\mathbb{M}_+$, it is **minimal** in the sense of the algebra, its trace is $\mathrm{Tr}(\tilde\Pi_+) = 1$, and it is the projector onto a **minimal left ideal** of $\mathbb{B}$, the two-complex-dimensional one-particle module. The complementary idempotent $\tilde\Pi_- = \tfrac12(e_t - i\vec e_z)$ is the occupied-state idempotent, and the two form a resolution of the identity, $\tilde\Pi_+ + \tilde\Pi_- = e_t$, $\tilde\Pi_+\tilde\Pi_- = 0$. The one-mode vacuum is thus, literally, a minimal idempotent.
- **Established, and worth separating from the above.** The vacuum idempotent is a **zero divisor**: its biquaternion norm vanishes, $\langle\tilde\Pi_+\rangle_{\natural} = \tilde\Pi_+\tilde\Pi_+^{\natural} = 0$, and its matrix representative has vanishing determinant, $\det\mathsf{M}_2(\tilde\Pi_+) = 0$. The vacuum state lies on the zero-divisor cone — the framework's light cone. This is not a defect of the state; it is the algebra's statement that a rank-one idempotent is not invertible, and it ties the choice of vacuum to the choice of a null direction.
- **The vacuum manifold.** The construction depends on a unit vector $\vec u\in S^2$ through $\tilde\Pi(\vec u) = \tfrac12(e_t + i\vec u)$. Every such idempotent is a legitimate one-mode vacuum, and the family is the two-sphere — the Bloch sphere of the state space. The framework does not single one out; a global $SU(2)$ rotation moves one into another, and the orbit is the vacuum manifold.
- **Gap, left visible.** For a **field** the vacuum is not an element of $\mathbb{B}$. The Fock space of a field is a module over the algebra, not a subalgebra of it, and the algebra contains no bosonic ladder at all: no pair $a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}\in\mathbb{B}$ can satisfy $[a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}]=e_t$ because a commutator has vanishing trace while $\mathrm{Tr}(e_t)=2$. So "the biquaternion vacuum" is not, in general, a biquaternion. It is an idempotent for one fermionic mode and a state in a module for a field.

The article proceeds as follows. The next section recalls the standard vacuum and the sense in which it is a state. The following section fixes the idempotents of $\mathbb{B}$ and the notion of minimality. The next two sections construct the one-mode vacuum and prove that it is a minimal idempotent, and then that it is a zero divisor. The following sections describe the minimal left ideal it defines, the vacuum manifold, and the field case. A section separates what is established from what is interpretation, and the article closes with open questions.

## The Vacuum as a State

In the standard formulation the vacuum is characterized in two equivalent ways, and it is worth keeping both in view because the biquaternion interpretation uses one and not the other.

**As a vector.** The one-particle space $\mathcal{H}_1$ generates the Fock space
$$
\mathcal{F} \;=\; \bigoplus_{n\ge 0}\Big(\mathcal{H}_1^{\otimes n}\Big)_{\pm},
$$
the symmetric or antisymmetric tensor algebra, and the vacuum spans the degree-zero term,
$$
|0\rangle \;\in\; \Big(\mathcal{H}_1^{\otimes 0}\Big)_{\pm} \cong \mathbb{C},
\qquad
a_r^{\mathrm{fop}}(\vec p)|0\rangle = 0 \ \ \text{for all } r,\vec p.
$$
The state is normalized, $\langle 0|0\rangle = 1$, and every $n$-particle state is built from it by creation operators. In this interpretation the vacuum is a vector in an infinite-dimensional space.

**As a functional.** A state on an algebra $\mathcal{A}$ of observables is a linear functional $\omega:\mathcal{A}\to\mathbb{C}$ that is positive, $\omega(\tilde Q_3^{*} \tilde Q_3)\ge 0$, and normalized, $\omega(e_t)=1$. The vacuum expectation value
$$
\omega_0(\tilde Q_3) \;=\; \langle 0|\,\pi(\tilde Q_3)\,|0\rangle
$$
is such a functional on the algebra generated by the fields, and it is **pure** — it is not a nontrivial convex combination of other states. Purity is the algebraic content of "the vacuum is a single state and not a mixture", and it is the property that links the vacuum to minimal idempotents, because in a finite-dimensional algebra the pure states are exactly the rank-one density matrices.

For the biquaternion framework two facts make the second interpretation the operative one. First, the algebra $\mathbb{B}$ is finite-dimensional, so its states are the positive normalized elements of its dual and are realized by density matrices; a state is an element of the algebra, not a vector outside it. Second, the one-mode truncation of a fermionic field *is* an algebra inside $\mathbb{B}$, so that for one mode the abstract state becomes an explicit algebra element. That element is the subject of the next three sections.

## Idempotents and Minimality

An **idempotent** of $\mathbb{B}$ is an element $\tilde\Pi$ with
$$
\tilde\Pi^2 = \tilde\Pi .
$$
A **Hermitian idempotent** is an idempotent fixed by the star, $\tilde\Pi^{*} = \tilde\Pi$, and in $\mathbb{M}_+$ it is a *positive* idempotent, hence a density matrix up to normalization. The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ has a simple classification of its idempotents, and it is the classification of the idempotents that the vacuum needs.

**Rank.** Under the isomorphism $\mathsf{M}_2$, an idempotent $\tilde\Pi$ is sent to a projection matrix $\mathsf{M}_2(\tilde\Pi)$. Such a matrix has eigenvalues in $\{0,1\}$, and its **rank** is the number of unit eigenvalues. In two dimensions the possibilities are
$$
\mathrm{rank}\,\mathsf{M}_2(\tilde\Pi) \in \{0,1,2\},
$$
corresponding to $\tilde\Pi = 0$, to a rank-one idempotent, and to $\tilde\Pi = e_t$. A rank-one idempotent is the smallest nonzero one, and it is called **minimal**:

> **Definition.** An idempotent $\tilde\Pi\neq 0$ is **minimal** if it cannot be written as a sum of two nonzero orthogonal idempotents, $\tilde\Pi = \tilde\Pi_1+\tilde\Pi_2$ with $\tilde\Pi_1\tilde\Pi_2=0$. Equivalently, $\mathsf{M}_2(\tilde\Pi)$ has rank one.

Minimality has three equivalent faces that will each be used below:
1. $\mathsf{M}_2(\tilde\Pi)$ has rank one, equivalently $\det\mathsf{M}_2(\tilde\Pi)=0$ and $\tilde\Pi\neq0$;
2. the left ideal $\mathbb{B}\tilde\Pi$ is **minimal** — it contains no proper nonzero left ideal;
3. the Peirce decomposition of $\mathbb{B}$ with respect to $\tilde\Pi$ has components of dimensions $1,1,1,1$ over $\mathbb{C}$ — that is, $k^2$, $k(n-k)$, $k(n-k)$, $(n-k)^2$ with $n=2$, $k=1$ — so that
$$
\mathbb{B} \;=\; \tilde\Pi\mathbb{B}\tilde\Pi \;\oplus\; \tilde\Pi\mathbb{B}(1-\tilde\Pi) \;\oplus\; (1-\tilde\Pi)\mathbb{B}\tilde\Pi \;\oplus\; (1-\tilde\Pi)\mathbb{B}(1-\tilde\Pi),
\qquad \tilde\Pi\mathbb{B}\tilde\Pi \cong \mathbb{C}.
$$
The corner $\tilde\Pi\mathbb{B}\tilde\Pi$ is one-complex-dimensional exactly when $\tilde\Pi$ is minimal; for a general idempotent it has dimension $(\mathrm{rank})^2$.

The reason minimality matters physically is the third face of the definition in the language of states: a Hermitian idempotent $\tilde\Pi\in\mathbb{M}_+$ with $\mathrm{Tr}(\tilde\Pi)=1$ and rank one defines the **pure state**
$$
\omega_{\tilde\Pi}(\tilde Q_3) \;=\; \mathrm{Tr}\big(\tilde\Pi\tilde Q_3\big),
$$
which on an **observable** $\tilde H\in\mathbb{M}_+$ takes the real value $2\,\mathrm{Sc}(\tilde\Pi\tilde H^{*}) = 2\langle\tilde\Pi,\tilde H\rangle_{*}$. A pure state is exactly what a vacuum is. A rank-two state with $\mathrm{Tr}=1$ would be the maximally mixed state $\tfrac12 e_t$, and a general element of the Bloch ball is neither.

## The One-Mode Vacuum

For a single fermionic mode the algebra contains the whole ladder. With
$$
\vec\Upsilon_x = \tfrac12\big(i\vec e_x - \vec e_y\big),
\qquad
\vec\Upsilon_y = \tfrac12\big(i\vec e_x + \vec e_y\big),
$$
one has, as the Fock article establishes,
$$
\big\{\vec\Upsilon_x, \vec\Upsilon_y\big\} = e_t,
\qquad
\vec\Upsilon_x^2 = 0,
\qquad
(\vec\Upsilon_y)^2 = 0,
\qquad
\tilde\Pi_- = \vec\Upsilon_y \vec\Upsilon_x = \tfrac12\big(e_t - i\vec e_z\big).
$$
The number operator is a projector, so its spectrum is $\{0,1\}$: the mode is either empty or occupied. The **vacuum projector** is the spectral projector onto the empty eigenvalue,
$$
\boxed{\;|0\rangle\langle 0| \;=\; e_t - \tilde\Pi_- \;=\; \tfrac12\big(e_t + i\vec e_z\big) \;=\; \tilde\Pi_+\;}.
$$
Here and below
$$
\tilde\Pi(\pm\vec u) \;=\; \tfrac12\big(e_t \pm i\vec u\big),
\qquad \vec u\in S^2,
$$
denotes the pair of Hermitian idempotents associated with the unit vector $\vec u$.

**The vacuum idempotent is minimal, Hermitian, and of unit trace.** It is convenient to verify the four defining properties at once, using $\vec e_z^2=-e_t$:
$$
\tilde\Pi_+^2 = \tfrac14\big(e_t + i\vec e_z\big)^2 = \tfrac14\big(e_t + 2i\vec e_z + (i\vec e_z)^2\big) = \tfrac14\big(e_t + 2i\vec e_z - e_t\big) = \tfrac12\big(e_t+i\vec e_z\big) = \tilde\Pi_+,
$$
so it is idempotent; $\bar{\tilde\Pi_+} = \tfrac12(e_t - i\vec e_z)$ and $\tilde\Pi_+^{*} = \tfrac12(e_t + i\vec e_z)^{*} = \tfrac12(e_t + i\vec e_z) = \tilde\Pi_+$, since $\vec e_z^{*} = -\vec e_z$ and $i^{*} = -i$, so it is Hermitian and lies in $\mathbb{M}_+$;
$$
\mathrm{Tr}\big(\tilde\Pi_+\big) = 2\,\mathrm{Sc}\big(\tilde\Pi_+\big) = 2\cdot\tfrac12 = 1,
$$
so its trace is one; and
$$
\mathsf{M}_2\big(\tilde\Pi_+\big) = \tfrac12\big(I_2 + i\mathsf{M}_2(\vec e_z)\big) = \tfrac12\big(I_2 + \sigma_3\big) = \begin{pmatrix}1&0\\0&0\end{pmatrix},
$$
which has rank one. Hence $\tilde\Pi_+$ is a **minimal idempotent** with unit trace: the one-mode vacuum.

The complementary idempotent and the resolution of the identity are immediate:
$$
\tilde\Pi_- = \tfrac12\big(e_t - i\vec e_z\big) = \mathsf{M}_2^{-1}\begin{pmatrix}0&0\\0&1\end{pmatrix},
\qquad
\tilde\Pi_+ + \tilde\Pi_- = e_t,
\qquad
\tilde\Pi_+ \tilde\Pi_- = 0 .
$$
The two-dimensional identity is resolved into the empty and occupied idempotents, and the Peirce corner at the vacuum is $\mathbb{C}$. The fermion-parity operator is the difference obtained from the same pair,
$$
(-1)^F \;=\; \tilde\Pi_+ - \tilde\Pi_- \;=\; i\vec e_z,
$$
in agreement with the Fock article's $(-1)^F=i\vec e_z$; as an operator it anticommutes with the ladder,
$$
(-1)^F \vec\Upsilon_x (-1)^F = -\vec\Upsilon_x,
\qquad
(-1)^F \vec\Upsilon_y (-1)^F = -\vec\Upsilon_y .
$$

**A numerical check on the whole set.** Representing $\mathbb{B}$ by $2\times2$ complex matrices through $\mathsf{M}_2$ and using explicit complex arithmetic on the coefficients, one finds: $\tilde\Pi_+^2-\tilde\Pi_+=0$; $\tilde\Pi_+^{*}-\tilde\Pi_+=0$; $\det\mathsf{M}_2(\tilde\Pi_+)=0$ with $\mathrm{Tr}\,\mathsf{M}_2(\tilde\Pi_+)=1$; $\tilde\Pi_+\tilde\Pi_-=0$ and $\tilde\Pi_++\tilde\Pi_-=I_2$; $\mathsf{M}_2((-1)^F)=\sigma_3$; and $\mathsf{M}_2((-1)^F\vec\Upsilon_x(-1)^F) = -\mathsf{M}_2(\vec\Upsilon_x)$, all to machine precision ($<10^{-16}$). The vacuum expectation values, $\langle\cdot\rangle_t=\mathrm{Tr}(\tilde\Pi_+\,\cdot\,)$, reproduce the mode algebra,
$$
\langle \vec\Upsilon_y \vec\Upsilon_x\rangle_t = \mathrm{Tr}\big(\tilde\Pi_+\tilde\Pi_-\big) = 0,
\qquad
\langle \vec\Upsilon_x \vec\Upsilon_y\rangle_t = \mathrm{Tr}\big(\tilde\Pi_+(e_t-\tilde\Pi_-)\big) = 1,
$$
which are the statements that the vacuum is empty and the mode anticommutator is normalized.

## The Vacuum Is a Zero Divisor

The single most consequential algebraic property of the vacuum idempotent is that it is **not invertible**, and the framework makes this property visible through the biquaternion norm.

Compute $\langle\tilde\Pi_+\rangle_{\natural} = \tilde\Pi_+\tilde\Pi_+^{\natural}$, using $\vec e_z^{\natural} = -\vec e_z$ and $i^{\natural} = i$:
$$
\tilde\Pi_+\tilde\Pi_+^{\natural} = \tfrac14\big(e_t+i\vec e_z\big)\big(e_t-i\vec e_z\big) = \tfrac14\Big(e_t - i\vec e_z + i\vec e_z - i^2 \vec e_z^2\Big) = \tfrac14\big(e_t - e_t\big) = 0 .
$$
So
$$
\boxed{\,\langle\tilde\Pi(\vec u)\rangle_{\natural} = 0 \quad\text{for every unit vector } \vec u\,}
$$
and the same computation with $\tilde\Pi_-$ gives $\langle\tilde\Pi_-\rangle_{\natural}=0$. In the language of the biquaternion norm, every minimal idempotent of $\mathbb{B}$ is a **null element**: it lies on the cone $\langle\tilde Q\rangle_{\natural}=0$, which is the zero-divisor cone and the framework's light cone. Equivalently, $\det\mathsf{M}_2(\tilde\Pi(\vec u))=0$, since the biquaternion norm is $\langle\tilde Q\rangle_{\natural}=\det\mathsf{M}_2(\tilde Q)$.

This is not an accident of the vacuum state; it is the algebra's statement about rank. A rank-one projector is a matrix of rank one, a rank-one matrix is singular, a singular matrix is a zero divisor, and the determinant-biquaternion norm detects exactly that. The vacuum is the simplest element of the algebra that has this property.

Two interpretations of the same fact are worth recording.

**The vacuum and its complement are the two null directions.** Because $\tilde\Pi_+ + \tilde\Pi_- = e_t$ with both null, the identity is written as the sum of two elements each of vanishing biquaternion norm. In signature language, $e_t$ is a positive-norm element decomposed along two null directions whose sum is timelike — the algebraic shape of a light-cone frame. The pair $\{\tilde\Pi_+, \tilde\Pi_-\}$ plays for the state space the role that the pair of null vectors plays for a Lorentz frame.

**The vacuum carries a definite phase direction.** The idempotent $\tilde\Pi(\vec u)$ is determined by the *unit* vector $\vec u$, and the null-cone condition $\langle\tilde\Pi(\vec u)\rangle_{\natural}=0$ is satisfied for every $\vec u$; the cone is the union of the one-dimensional rays that the idempotents single out. Choosing a vacuum is choosing a null direction, and different vacua are related by the rotations that move one null direction into another. This is made precise in the next two sections.

## The Minimal Left Ideal and the One-Particle Module

A left ideal of $\mathbb{B}$ is a linear subspace $\mathcal{I}$ with $\mathbb{B}\mathcal{I}\subseteq\mathcal{I}$. For an idempotent $\tilde\Pi$ the set $\mathbb{B}\tilde\Pi$ is always a left ideal, and the classification above implies:

> **Proposition.** $\mathbb{B}\tilde\Pi$ is a minimal left ideal if and only if $\tilde\Pi$ is a minimal idempotent.

For the vacuum this identifies a physically named object. Acting on the algebra with $\tilde\Pi_+$ on the right,
$$
\mathbb{B}\tilde\Pi_+ = \big\{\tilde Q \tilde\Pi_+ : \tilde Q\in\mathbb{B}\big\} \cong \mathbb{C}^2,
$$
a two-complex-dimensional space, because the map $\tilde Q\mapsto\tilde Q \tilde\Pi_+$ annihilates the rank-one complement and its image is the column space of $\mathsf{M}_2(\tilde\Pi_+)$. With $\mathsf{M}_2(\tilde\Pi_+) = \mathrm{diag}(1,0)$ the image is the space of column vectors with second entry zero, that is, the **fundamental module** of the algebra — the two-component spinor space on which the field's spinors live. So

> the one-mode vacuum idempotent determines the one-particle (spinor) module as the Peirce carrier it generates, a minimal left ideal here.

This is the mechanism by which the vacuum situates the field in the framework: the algebra alone has no distinguished module, and the choice of vacuum idempotent selects one. Conversely the module fixes the idempotent only up to the equivalence $\tilde\Pi\mapsto \tilde Q\tilde\Pi\tilde Q^{*}$ by unitary units of the algebra, which is the statement that the module is unique while the vacuum is not.

The same construction, run in the reverse direction, is the Hermitian GNS reconstruction. The state $\omega_{\tilde\Pi}(\tilde Q_3) = \mathrm{Tr}(\tilde\Pi\tilde Q_3)$ has a GNS Hilbert space obtained from $\mathbb{B}$ by quotienting out the elements of zero $\omega_{\tilde\Pi}$-norm; for a **pure** state that quotient is exactly the minimal left ideal, of complex dimension two, and the GNS representation is irreducible. For a mixed state the quotient is larger and the representation is reducible. The vacuum's minimality is thus the algebraic reason its GNS representation is irreducible, and the GNS construction itself is the subject of the companion article *The Hermitian GNS Construction in the Biquaternion Framework*.

## The Vacuum Manifold

The construction used $\vec e_z$ only through the unit vector it defines. Replacing $\vec e_z$ by $\vec u = u_x \vec e_x + u_y \vec e_y + u_z \vec e_z$ with $u_x^2+u_y^2+u_z^2=1$ gives
$$
\tilde\Pi(\vec u) = \tfrac12\big(e_t + i\vec u\big),
\qquad
\tilde\Pi(-\vec u) = \tfrac12\big(e_t - i\vec u\big),
$$
and every identity above holds with $\vec u$ in place of $\vec e_z$, because $\vec u^2 = -e_t$ for every unit vector. The family
$$
\boxed{\;\mathcal{M}_{\text{vac}} \;=\; \big\{\,\tilde\Pi(\vec u) : \vec u\in S^2\,\big\} \;\cong\; S^2\;}
$$
is the **vacuum manifold**. Its three properties, all immediate from the definitions, are worth naming.

1. **It is a two-sphere.** The idempotents are labelled by unit vectors, and the correspondence is one-to-one: $\tilde\Pi(\vec u) = \tilde\Pi(\vec u_2)$ if and only if $\vec u = \vec u_2$, since the vector part of the idempotent is $\tfrac{i}{2}\vec u$.
2. **It is the Bloch sphere of the state space.** Writing a general element of $\mathbb{M}_+$ of unit trace as $\tilde{Ϛ} = \tfrac12(e_t + i\vec r)$ with $\vec r\in\mathbb{R}^3$, the idempotent condition $\tilde{Ϛ}^2=\tilde{Ϛ}$ forces $|\vec r|=1$. The minimal idempotents of unit trace are exactly the Bloch sphere, and a general state (a unit-*trace*, not rank-one, density matrix) fills the Bloch ball $|\vec r|\le 1$.
3. **It is a single rotation orbit.** The conjugation $\tilde\Pi\mapsto \tilde u\tilde\Pi\tilde u^{*}$ by a unit real quaternion $\tilde u\in\mathbb{H}_{\mathbb{B}}$, $\langle\tilde u\rangle_{\natural}=e_t$, acts on the vector part as a rotation of $\vec u$, and every unit vector is reached from every other. The rotation group of the framework acts transitively on the vacuum manifold, so the framework by itself does not distinguish a vacuum; the vacuum is a **spontaneously chosen** element, and the manifold is the order-parameter space of that choice.

That last point is the physical content of the manifold. A vacuum that is a minimal idempotent is a *pure state with a definite orientation*, and the orientation is not fixed by the algebra. Whether the framework provides a dynamics that selects one — a Hamiltonian whose ground projector is a particular $\tilde\Pi(\vec u)$ — is a question about the dynamics, not about the state, and is not settled by the algebra alone.

## The Field Vacuum Is Not an Idempotent

Everything above is about one mode. For a field the situation changes, and the change is not a matter of detail.

The Fock space of a field is a **module** over the algebra rather than a subalgebra of it. That is the finding of the Fock article, and it is inherited here unchanged: the one-particle space is a module, the many-particle space is its tensor algebra, and beyond one mode not even the operator algebra is inside $\mathbb{B}$. In particular there is **no bosonic ladder in $\mathbb{B}$**, because a bosonic mode requires $[a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}]=e_t$, whereas for any two elements of $\mathbb{B}$
$$
\mathrm{Tr}\big([a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}]\big) = \mathrm{Tr}(a^{\mathrm{fop}}a^{\mathrm{fop}\dagger}) - \mathrm{Tr}(a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}) = 0
$$
by the cyclicity of the trace, while $\mathrm{Tr}(e_t)=2$. Hence no pair of algebra elements satisfies the canonical commutation relation, and the photon's Fock vacuum — the vacuum of the electromagnetic field — is not an algebra element. It is the standard Fock vacuum of a module built from the transverse polarization plane, as *The Vacuum State and the Casimir Effect in Biquaternionic Form* records.

For a fermionic field the one-particle space is also a module, but here the algebra reaches one step further: the one-mode truncation is an algebra inside $\mathbb{B}$, and for that truncation the vacuum is the idempotent constructed above. The honest summary is therefore a sharp one:

> "The biquaternion vacuum" is not, in general, a biquaternion. It is a **minimal idempotent of $\mathbb{M}_+$** for one fermionic mode — the largest truncation the algebra supports — and a **state in a module** for a field, where it is neither an idempotent nor an element of the algebra at all.

The minimal-idempotent interpretation is not a diminution of the field vacuum. It is the exact algebraic statement of what the vacuum is in the only case in which the algebra contains it, and it is the reason the vacuum is a natural starting point for the algebraic constructions — GNS reconstruction, the Wick theorem, and the thermal states — that the articles following this one develop.

## What Is Established and What Is Interpretation

**Established (algebra).**
- The idempotents of $\mathbb{B}$ are classified by rank; the rank-one (minimal) Hermitian idempotents of $\mathbb{M}_+$ are exactly $\tilde\Pi(\vec u) = \tfrac12(e_t+i\vec u)$ with $|\vec u|=1$.
- $\tilde\Pi(\vec u)$ is Hermitian, idempotent, of unit trace, and minimal; $\tilde\Pi_- = e_t-\tilde\Pi_+$ is its orthogonal complement, and the two resolve the identity.
- $\langle\tilde\Pi(\pm\vec u)\rangle_{\natural} = 0$ and $\det\mathsf{M}_2(\tilde\Pi(\pm\vec u))=0$: the vacuum is a zero divisor on the light cone.
- $\mathbb{B}\tilde\Pi(\vec u)$ is a Peirce carrier, a minimal left ideal here, isomorphic to $\mathbb{C}^2$, the fundamental (spinor) module.
- The vacuum manifold is $S^2$, on which the unit real quaternions act transitively.

**Established (physics).**
- The Fock vacuum is annihilated by all annihilation operators, spans the degree-zero term, and is a pure state; the one-mode truncation of a fermionic field is realized by the idempotent above.
- The photon's Fock vacuum is built from a module, and no bosonic ladder exists in $\mathbb{B}$.

**Interpretation.**
- Reading the vacuum as a minimal idempotent, and reading the vacuum manifold as the order-parameter space of a spontaneously chosen state, are interpretations of algebraic facts. They are precise; they are not derivations of the field-theoretic vacuum.
- The identification of the Peirce carrier with the one-particle module, which here is a minimal left ideal, is standard representation theory applied to $\mathbb{B}$; its **physical interpretation** as "the vacuum determines the one-particle space" is the interpretive step.

**Open.**
- Whether a dynamics inside the framework selects a particular minimal idempotent, and by what mechanism, is not addressed by the algebra.
- Whether the zero-divisor property of the vacuum has consequences for the framework's treatment of superselection sectors or of the theta vacuum is taken up in the companion articles on those subjects.

## Summary

For a single fermionic mode the vacuum of the biquaternion framework is a concrete algebra element: the Hermitian, idempotent, unit-trace, **minimal** idempotent
$$
\boxed{\;|0\rangle_{*}\langle 0| = \tilde\Pi_+ = \tfrac12\big(e_t+i\vec e_z\big) = \mathsf{M}_2^{-1}\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
\tilde\Pi_- = \tfrac12\big(e_t-i\vec e_z\big) = \mathsf{M}_2^{-1}\begin{pmatrix}0&0\\0&1\end{pmatrix}\;}
$$
with $\tilde\Pi_++\tilde\Pi_- = e_t$, $\tilde\Pi_+\tilde\Pi_-=0$, and $(-1)^F = i\vec e_z = \tilde\Pi_+-\tilde\Pi_-$. Minimality is equivalently rank one, equivalently the one-dimensional Peirce corner $\tilde\Pi\mathbb{B}\tilde\Pi\cong\mathbb{C}$, equivalently the minimality of the left ideal $\mathbb{B}\tilde\Pi_+$. That ideal is the two-complex-dimensional fundamental module — the one-particle spinor space — so the vacuum idempotent determines the module on which the field lives.

The vacuum idempotent is a **zero divisor**: $\langle\tilde\Pi_+\rangle_{\natural}=0$ and $\det\mathsf{M}_2(\tilde\Pi_+)=0$. It lies on the zero-divisor cone, and the identity is the sum of two null idempotents. The family of vacua is the two-sphere $\tilde\Pi(\vec u)$, $\vec u\in S^2$ — the Bloch sphere of pure states — on which the unit real quaternions act transitively, so the framework fixes the manifold of vacua but not one vacuum.

For a field the vacuum is a state in a module and not an element of the algebra: the Fock space is a module over $\mathbb{B}$, and no bosonic ladder exists inside $\mathbb{B}$ because a commutator has vanishing trace while $\mathrm{Tr}(e_t)=2$. The minimal-idempotent interpretation is exact for the one-mode truncation, which is the largest truncation the algebra supports, and it is the starting point for the operator-algebraic constructions that follow.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$, $\vec e_\mu \vec e_\nu=\varepsilon_{\mu\nu\lambda}\vec e_\lambda$ |
| $i$ | Scalar imaginary, central, $i^2=-1$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}},\mathbb{C}_{\mathbb{B}}$ | Real-quaternion subspace; centre $\mathrm{span}_\mathbb{R}\{e_t,ie_t\}$ |
| $\langle\tilde Q\rangle_{\natural} = \langle\tilde Q,\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^2=\det\mathsf{M}_2(\tilde Q)$ | Biquaternion norm |
| $\mathrm{Tr}(\tilde H_1\tilde H_2^{*})=2\langle\tilde H_1,\tilde H_2\rangle_{*} = 2\,\mathrm{Sc}(\tilde H_1\tilde H_2^{*})$, $\mathrm{Tr}(e_t)=2$ | Trace reading of the Hermitian form |
| $\mathsf{M}_2(\vec e_k)=-i\sigma_k$, $\mathsf{M}_2(i)=iI_2$ | Matrix isomorphism |
| $\tilde\Pi(\pm\vec u)=\tfrac12(e_t\pm i\vec u)$, $\vec u\in S^2$ | Minimal idempotents; vacuum idempotents |
| $|0\rangle\langle 0|=\tilde\Pi_+$ | One-mode vacuum idempotent |
| $\tilde\Pi_-=\vec\Upsilon_y\vec\Upsilon_x$ | Number operator (occupied idempotent) |
| $\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)$, $\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y)$ | Single-mode ladder |
| $(-1)^F=i\vec e_z=\tilde\Pi_+-\tilde\Pi_-$ | Fermion-parity grading |
| $\mathbb{B}\tilde\Pi(\vec u)\cong\mathbb{C}^2$ | Minimal left ideal; one-particle (spinor) module |
| $\mathcal{M}_{\text{vac}}\cong S^2$ | Vacuum manifold |
| $\omega_{\tilde\Pi}(\tilde Q_3)=\mathrm{Tr}(\tilde\Pi\tilde Q_3^{*})$ | Pure state defined by a minimal idempotent |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |

## Further Reading

- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the projector calculus and the idempotent characterization of pure states.
- J. von Neumann, *Mathematical Foundations of Quantum Mechanics* (Princeton, 1955), for the density-matrix classification of states and the geometry of the state space.
- G. Birkhoff and J. von Neumann, "The logic of quantum mechanics," *Annals of Mathematics* **37** (1936) 823–843, for the lattice of projectors and the algebraic interpretation of the state space.
- F. J. Murray and J. von Neumann, "On rings of operators," *Annals of Mathematics* **37** (1936) 116–229, for minimal projectors, factors, and the classification of left ideals.
- R. V. Kadison and J. R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Vol. I (Academic Press, 1983), for idempotents, Peirce decompositions, and minimal ideals in finite-dimensional algebras.
- F. R. Gantmacher, *The Theory of Matrices*, Vol. I (Chelsea, 1959), for the rank classification of projectors and the determinant as a rank test.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the matrix representation of biquaternions, idempotents, and the fundamental module.
- J. C. Várilly and J. M. Gracia-Bondía, "Connes' noncommutative differential geometry and the standard model," *Journal of Geometry and Physics* **12** (1993) 223–301, for minimal left ideals as fermion modules in the algebraic interpretation of particle multiplets.
- Companion articles: [Fock Space and Creation/Annihilation Operators in Biquaternionic Form](fock-space-and-creation-annihilation-operators-in-biquaternionic-form.html), for the single-mode ladder, the number operator, and the fermion-parity grading; [The Hermitian GNS Construction in the Biquaternion Framework](the-hermitian-gns-construction-in-the-biquaternion-framework.html), for the reconstruction that the pure state's minimality makes irreducible; [The Vacuum State and the Casimir Effect in Biquaternionic Form](the-vacuum-state-and-the-casimir-effect-in-biquaternionic-form.html), for the field vacuum as a module state and the absence of a bosonic ladder; [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), for the state space, the trace pairing, and the Bloch ball.
