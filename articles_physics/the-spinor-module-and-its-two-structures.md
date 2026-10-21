# __The Spinor Module and Its Two Structures__

## Introduction

The spinor space of the biquaternion framework is the minimal left ideal

$$
S=\mathbb{B}\tilde\Pi_+=\mathbb{C}\{\tilde\Pi_+,\vec\Upsilon_y\},\qquad
\tilde\Pi_+=\tfrac12(e_t+i\vec e_z),\quad \vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y),
$$

of complex dimension two. The algebra acts on it by left multiplication, and the action carries the defining representation of the double cover of the Lorentz group. That is one structure. The same carrier also carries a positive definite Hermitian form and a Born pairing, and that is a second structure, belonging to a different product of the same algebra.

The article's thesis is that the two structures are **not two views of one object**. They belong to two different products: the module structure to the plain bilinear product $\tilde Q_1\tilde Q_2$, whose menu label is **composition**, and the Hilbert structure to the plain sesquilinear product $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$, whose menu label is **probability**. The sharpest evidence is that the algebra's own bilinear form is **degenerate on the carrier**: its Gram matrix is $\operatorname{diag}(\tfrac12,0)$. The module has no norm of its own, and the metric is added by the second slot.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The plain product as the only associative unital law of the twelve, and left alternativity as its threshold | [The Specificities of the Biquaternion Algebra](../articles_maths/the-specificities-of-the-biquaternion-algebra.html) |
| The idempotents, the Peirce decomposition, the minimal left ideals and the matrix units | [Ideals and Peirce Decomposition of the Biquaternion Algebra](../articles_maths/ideals-and-peirce-decomposition-of-the-biquaternion-algebra.html) |
| The module theory: the simple module, $\mathbb{B}\cong S\oplus S$ and $\mathbb{B}\cong\operatorname{End}_{\mathbb{C}}(S)$ | [Modules over the Biquaternion Algebra](../articles_maths/modules-over-the-biquaternion-algebra.html) |
| The column ideal of a matrix ring: one idempotent and $n-1$ nilpotents | [The Column Ideals of a Matrix Ring: One Idempotent and $n-1$ Nilpotents](../articles_maths/the-column-ideals-of-a-matrix-ring.html) |
| The canonical Hermitian form on the regular module, its positivity and its Gram matrix | [The Canonical Hermitian Form on the Regular Module of the Biquaternioid Algebra](../articles_maths/the-canonical-hermitian-form-on-the-regular-module-of-the-biquaternioid-algebra.html) |
| The four forms of the twelve products, their Gram matrices and their signatures | [The 4 Forms over the Biquaternion $\mathbb{C}$ Space](../articles_maths/the-4-forms-over-the-biquaternion-c-space.html) |
| The forms of the products, their Gram matrices and their isometry groups | [The 4 Forms over the Biquaternion $\mathbb{C}$ Space](../articles_maths/the-4-forms-over-the-biquaternion-c-space.html) |
| The algebraic norms of the products | [The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space](../articles_maths/the-4-algebraic-norms-over-the-biquaternion-c-space.html) |
| The embedding of the algebra in $\operatorname{End}_{\mathbb{C}}(S)$ | [Modules over the Biquaternion Algebra](../articles_maths/modules-over-the-biquaternion-algebra.html) |

## The Carrier and Its Forced Basis

The two idempotents $\tilde\Pi_+$ and $\tilde\Pi_-=e_t-\tilde\Pi_+$ are orthogonal and complete in the plain product, and the Peirce decomposition cuts the algebra into four one-dimensional complex corners:

$$
\tilde\Pi_+\mathbb{B}\tilde\Pi_+=\mathbb{C}\tilde\Pi_+,\quad
\tilde\Pi_+\mathbb{B}\tilde\Pi_-=\mathbb{C}\vec\Upsilon_x,\quad
\tilde\Pi_-\mathbb{B}\tilde\Pi_+=\mathbb{C}\vec\Upsilon_y,\quad
\tilde\Pi_-\mathbb{B}\tilde\Pi_-=\mathbb{C}\tilde\Pi_-.
$$

The spinor space is one column, the sum of a diagonal corner and an off-diagonal one:

$$
S=\tilde\Pi_+\mathbb{B}\tilde\Pi_+\oplus\tilde\Pi_-\mathbb{B}\tilde\Pi_+
=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_y .
$$

The basis is therefore not a choice. A minimal left ideal is one column of the matrix model, and a column of a rank-two matrix algebra is one diagonal corner plus one off-diagonal corner. The diagonal corner contributes the idempotent $\tilde\Pi_+$; the off-diagonal corner contributes a nilpotent, $\vec\Upsilon_y$. Every element of an off-diagonal corner is square-zero, because $(fae)(fae)=fa(ef)ae=0$ for orthogonal idempotents $e,f$. In rank $n$ the same count gives one idempotent and $n-1$ nilpotents; the spinor space is the case $n=2$.

> **The basis of the spinor space is one idempotent and one nilpotent, and the nilpotency is structural.** It is not a property of the particular column, and it is not a choice of coordinates.

The physical reading of the basis is the first statement of the article. The idempotent is the **state** direction of the column, and the nilpotent is the **shift** direction, the off-diagonal element that raises or lowers the column index. The two directions are what a two-level carrier needs: one projection and one shift. The algebra supplies both, and it supplies them in that proportion.

## The Module Structure: Composition

The plain product makes $S$ a left $\mathbb{B}$-module. On the basis $(\tilde\Pi_+,\vec\Upsilon_y)$ the left multiplications by the four basis elements are

$$
L_{\tilde\Pi_+}=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
L_{\tilde\Pi_-}=\begin{pmatrix}0&0\\0&1\end{pmatrix},\qquad
L_{\vec\Upsilon_x}=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
L_{\vec\Upsilon_y}=\begin{pmatrix}0&0\\1&0\end{pmatrix},
$$

the matrices of $\mathsf{M}_2(\mathbb{C})$ in the model $\mathsf{M}_2(\vec e_k)=-i\sigma_k$. The module is literally the column space $\mathbb{C}^2$ on which the algebra acts by matrix multiplication.

Three module-theoretic facts carry the reading.

- **The module is simple and unique.** $\mathbb{B}\cong M_2(\mathbb{C})$ is simple and finite-dimensional, so its modules are completely reducible and there is, up to isomorphism, exactly one simple module. By Schur's lemma $\operatorname{End}_{\mathbb{B}}(S)=\mathbb{C}$.
- **The algebra is the endomorphism algebra.** $\mathbb{B}\cong\operatorname{End}_{\mathbb{C}}(S)$, and the left regular module splits as $\mathbb{B}\cong S\oplus S$. The algebra is the algebra of all linear maps of the carrier, and the regular module is two copies of it.
- **The Lorentz action is the left action.** A unit-norm biquaternion $\tilde U$, $\tilde U\tilde U^{\natural}=e_t$, acts by $\psi\mapsto\tilde U\psi$, and the action is the defining representation of $SL(2,\mathbb{C})$.

The third fact is the physical content of the module structure. The action is faithful, and it does not descend to the Lorentz group: $-e_t$ acts as $-\mathrm{id}$ on $S$ while it acts trivially by conjugation on the four-vectors of $\mathbb{M}_-$. The double cover therefore appears on the module side and not on the four-vector side, and **spin-$\tfrac12$ is a module datum**. It is a property of how the algebra acts on the carrier, not of a form on the carrier.

One caution belongs here, because it is easy to state wrongly. **A single minimal left ideal is one chirality, not two.** The ideals $\mathbb{B}\tilde\Pi_+$ and $\mathbb{B}\tilde\Pi_-$ are both isomorphic to $S$ and carry the same defining representation. The two Weyl halves are $S$ and its conjugate module $\bar S$, which are non-isomorphic as complex representations. The complement article treats the second ideal and the conjugate module; this article treats one carrier and its two structures.

## The Probability Structure: the Second Slot

The second structure uses the plain sesquilinear product. Its scalar part is the Hermitian form

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\operatorname{Sc}(\tilde Q_1\tilde Q_2^{*}),
$$

which is positive definite on the algebra. Restricted to the carrier, its Gram matrix on the basis $(\tilde\Pi_+,\vec\Upsilon_y)$ is

$$
G=\begin{pmatrix}\langle\tilde\Pi_+,\tilde\Pi_+\rangle_{*} & \langle\tilde\Pi_+,\vec\Upsilon_y\rangle_{*}\\[2pt]\langle\vec\Upsilon_y,\tilde\Pi_+\rangle_{*} & \langle\vec\Upsilon_y,\vec\Upsilon_y\rangle_{*}\end{pmatrix}
=\tfrac12 I_2 .
$$

The carrier is therefore a two-dimensional Hilbert space with the standard metric, and the two basis spinors are orthogonal and of equal norm. The form is invariant under the unitary slice $\mathrm{U}(2)=\{\tilde U:\tilde U\tilde U^{*}=e_t\}$; inside $SL(2,\mathbb{C})$ the invariance is the compact subgroup $SU(2)$, and a generic phase $e^{i\theta}e_t$ is an isometry of the Hilbert structure that lies outside $SL(2,\mathbb{C})$. The Hilbert form is therefore invariant under a group that is not the Lorentz group, and the difference is exactly the phase. In module coordinates the same form is the spinor inner product $h(\psi,\phi)=\psi^{\dagger}\phi$. The **Born pairing** is the trace formula

$$
\operatorname{Tr}(\tilde\Pi\tilde H^{*})=2\operatorname{Sc}(\tilde\Pi\tilde H),
$$

which pairs a state idempotent with an observable. The normalisation $\langle\psi,\psi\rangle_{*}=1$ is a condition on the Hilbert structure alone.

The physical reading of the second structure is the one the informational sector has built. A **state** is a Hilbert vector, an **observable** is a Hermitian element, and the pairing is the probability. The ray, not the vector, is the state: $\psi$ and $e^{i\alpha}\psi$ define the same ray and the same probabilities, and the Hilbert form is blind to the phase.

The sharpest way to see that this is a second structure and not a second view is the behaviour of the **algebra's own form** on the same carrier. The symmetric bilinear form

$$
\langle\tilde Q_1,\tilde Q_2\rangle=\operatorname{Sc}(\tilde Q_1\tilde Q_2)=Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)
$$

is non-degenerate on $\mathbb{B}$, of signature $(4,4)$ on the real space. On the carrier its Gram matrix is

$$
B_S=\begin{pmatrix}\tfrac12&0\\0&0\end{pmatrix},
$$

of rank one, with radical $\mathbb{C}\vec\Upsilon_y$. The nilpotent is orthogonal to both basis spinors and to every element of $S$: it has zero scalar part and squares to zero. **The algebra's own form cannot separate the two basis spinors and cannot produce a norm on the carrier.** Positivity is not a property of the plain product at all; it needs the second slot.

## The Two Structures Side by Side

| job | structure | the algebra's part | the physical carrier |
| --- | --- | --- | --- |
| composition | module | plain left multiplication | the Lorentz action and the double cover |
| probability | Hilbert space | the plain sesquilinear pairing | the norm, the normalisation and the Born rule |

The table is the article in one line. The module structure makes the carrier an **arena**: the algebra is the algebra of operators and the carrier is what they act on. The Hilbert structure makes the arena a **probability space**: the form is what can be evaluated on a state and squared into a number. Neither structure alone gives the pair. A module without a form has no numbers; a form without an action has no observables.

The two structures separate the two physical data of a spinor.

- **The spin is a module datum.** The double cover acts faithfully on the module, $-e_t$ acts as $-\mathrm{id}$, and that is where spin-$\tfrac12$ lives.
- **The ray is a Hilbert datum.** The form is blind to the sign and to the phase, so the state is a ray and not a vector.
- **The vacuum is a module datum.** The choice of idempotent $\tilde\Pi_+$ selects the module, and the module is fixed only up to the equivalence of idempotents.
- **The normalisation is a Hilbert datum.** $\langle\psi,\psi\rangle_{*}=1$ is a condition on the form and makes the amplitudes into probabilities.

The last pair is worth stating as a contrast. **The state space is normalised by the metric and selected by the vacuum**, and the two acts are of different kinds: one is a pairing, the other is a choice of generator. The reading is that the algebraic structures divide the labour of a state space between a form and a choice.

The two structures also meet the corpus's word **quantisation**. The insertion of the star into the second slot, the step from $\tilde Q_1\tilde Q_2$ to $\tilde Q_1\tilde Q_2^{*}$, is what turns the composition pairing into the probability pairing. Read on the carrier, the spinor space is **compositional before the step and probabilistic after it**. The step is not an added axiom; it is the choice of what to put in the second slot. The corpus's reading of that step is *The Four General Products: Composition, Probability, Causality, Gauge*, and the present article locates it between the two structures.

## What the Module Structure Does Not Carry

Three separations keep the article honest.

- **No positivity.** The algebra's form is indefinite on the real space and degenerate on $S$. The module has no canonical normalised state.
- **No Born rule.** The probability pairing is the scalar part of the sesquilinear product, not of the plain product. It belongs to the second structure.
- **No pairing of the carrier by the product.** The sesquilinear products do not preserve $S$: they couple a state to a conjugate slot and land outside the ideal. A sesquilinear product pairs the space; it does not act on it.

The other half of the algebra is the subject of *The Complementary Ideal and the Second State Space*: the complementary ideal $\mathbb{B}\tilde\Pi_-$ carries its own copy of both structures, and the mass is what mixes the two copies.

A fourth separation is about the sectors. The carrier meets each of $\mathbb{M}_\pm$ in one real dimension, so **the spinor space is not a sector**, and its two structures are not the material–informational split. The sector split is a third structure, real and independent, and it cuts across the ideal. The companion article uses that fact; here it is recorded to prevent the identification of the carrier with $\mathbb{M}_+$.

## Physical Readings

- **One carrier, two structures, two jobs.** The interpretation is that the framework's state space is not one structure but two: the composition structure that makes the algebra act, and the probability structure that makes the states pair. Boundary: a statement about the algebraic structures, and it adds no identity between composition and probability.
- **The module is composition.** The interpretation is that the plain product composes two elements, and the module is that composition read with one factor held fixed. Boundary: an interpretation of the algebra's law, not a dynamics.
- **The spin is a module datum, the ray is a Hilbert datum.** The interpretation is that the double cover acts faithfully on the module, while the Hilbert structure is blind to the phase and yields the ray. Boundary: a separation of two known facts by the two structures; it adds no new representation.
- **The observables are module endomorphisms.** The interpretation is that $\mathbb{B}\cong\operatorname{End}_{\mathbb{C}}(S)$, so the observables are the endomorphisms of the carrier and the trace formula is the pairing of the two structures. Boundary: the identification of the spinor and the qubit is not made; only the algebra of the pair is stated.
- **The carrier has no norm of its own.** The interpretation is that the algebra's form is degenerate on $S$, so an unnormalised spinor is what the module gives, and normalisation is added by the metric. Boundary: a statement about the two forms, not a claim about physical states.
- **The Born rule is a product, not a postulate.** The interpretation is that the probability pairing is the scalar part of the plain sesquilinear product, so positivity is the definiteness of a form and the trace formula is the scalar pairing. Boundary: the derivation and its bounds are *The Born Rule from the Hermitian Form — Derivation and Comparison*; this article only locates the rule among the structures.
- **The spinor and the qubit are one carrier read twice.** The interpretation is that the Weyl spinor of the Lorentz action and the two-level state of the informational sector inhabit one complex plane, once as the defining module and once as the Hilbert space. Boundary: the carrier is one; the physics of the two readings is not thereby identified.
- **Quantisation is the second slot.** The interpretation is that the step from the plain product to the plain sesquilinear product is exactly the step from the module structure to the Hilbert structure. Boundary: the algebra supplies the pairing and no equation of motion and no measure.

## Limits

- **No measurement postulate and no Born derivation.** The Born rule is cited from its owner; the article states where it sits among the structures.
- **No identification of the two physics.** The carrier is one, but the spinor index is not identified with the qubit's two levels, and the two readings are not merged.
- **No claim that the module is the whole spinor space.** The module structure is one of the two structures, and the metric, the conjugate module and the complement are the others.
- **The algebra's form is not the metric.** $\langle\tilde Q_1,\tilde Q_2\rangle$ is indefinite and degenerate on $S$; the positive definite form is $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$.
- **One ideal is one chirality.** The two ideals are isomorphic; the two Weyl halves are $S$ and $\bar S$. The article does not conflate the two uses of the word chirality.

## Summary

The spinor space $S=\mathbb{B}\tilde\Pi_+=\mathbb{C}\{\tilde\Pi_+,\vec\Upsilon_y\}$ is a minimal left ideal of the plain algebra, with a forced basis of one idempotent and one nilpotent, the idempotent from the diagonal Peirce corner and the nilpotent from the off-diagonal one. As a module it is the unique simple module, with $\operatorname{End}_{\mathbb{B}}(S)=\mathbb{C}$, $\mathbb{B}\cong S\oplus S$ and $\mathbb{B}\cong\operatorname{End}_{\mathbb{C}}(S)$; the left action is the defining representation of the double cover, and $-e_t$ acts as $-\mathrm{id}$, which is where spin-$\tfrac12$ lives.

The same carrier carries a second structure from the plain sesquilinear product: a positive definite Hermitian form of Gram matrix $\tfrac12 I_2$, the Born pairing and the normalisation. The two structures do not coincide: the algebra's own bilinear form is degenerate on the carrier, $\operatorname{diag}(\tfrac12,0)$, with radical the nilpotent line. The module is composition and the Hilbert space is probability; the spin is a module datum and the ray a Hilbert datum; the vacuum is a module choice and the normalisation a metric condition.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde\Pi_+=\tfrac12(e_t+i\vec e_z)$, $\tilde\Pi_-=e_t-\tilde\Pi_+$ | the two standard idempotents |
| $\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)$, $\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y)$ | the two off-diagonal nilpotents |
| $S=\mathbb{B}\tilde\Pi_+=\mathbb{C}\{\tilde\Pi_+,\vec\Upsilon_y\}$ | the spinor space, a minimal left ideal |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\operatorname{Sc}(\tilde Q_1\tilde Q_2^{*})$ | the Hilbert form of the second slot |
| $\langle\tilde Q_1,\tilde Q_2\rangle=\operatorname{Sc}(\tilde Q_1\tilde Q_2)$ | the algebra's own bilinear form |
| $B_S=\operatorname{diag}(\tfrac12,0)$ | the restriction of the algebra's form to $S$ |
| $\operatorname{End}_{\mathbb{B}}(S)=\mathbb{C}$ | the endomorphism ring of the simple module |
| $\mathrm{GPA}$, $\mathrm{GPS}$ | the plain algebra and the plain sesqualgebra |

## Further Reading

- [Ideals and Peirce Decomposition of the Biquaternion Algebra](../articles_maths/ideals-and-peirce-decomposition-of-the-biquaternion-algebra.html), for the corners, the matrix units and the minimal ideals.
- [Modules over the Biquaternion Algebra](../articles_maths/modules-over-the-biquaternion-algebra.html), for simplicity, the endomorphism ring and the regular module.
- [The Column Ideals of a Matrix Ring: One Idempotent and $n-1$ Nilpotents](../articles_maths/the-column-ideals-of-a-matrix-ring.html), for the structural count of the basis.
- [The Canonical Hermitian Form on the Regular Module of the Biquaternioid Algebra](../articles_maths/the-canonical-hermitian-form-on-the-regular-module-of-the-biquaternioid-algebra.html), for the positive definite form and its Gram matrix.
- *The Informational Sector: States, Observables and Probability* and *The Born Rule from the Hermitian Form — Derivation and Comparison*, for the probability structure.
