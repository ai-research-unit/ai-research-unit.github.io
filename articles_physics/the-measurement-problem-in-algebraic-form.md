# __The Measurement Problem in Algebraic Form__

## Introduction

The measurement problem is the unresolved question of how the definite, single outcomes of measurement are related to a formalism whose states evolve deterministically and linearly. It has been argued for a century, and it is not settled. The biquaternion framework of the companion articles is a **reformulation of standard quantum mechanics**: it reproduces the standard predictions, introduces no new empirical content, and therefore cannot settle an interpretive or empirical dispute that standard quantum mechanics does not settle. This article proposes no solution.

What it does is narrower, and worth doing carefully. A reformulation changes which notions are primitive, and the measurement problem is stated in terms of primitive notions. The question here is: **stated in the objects of the framework, what is the measurement problem, and what does the restatement change?**

The answer, in advance, is one change in form and no change in physics. In its usual statement the problem is a clash between **two kinds of time evolution** — a unitary evolution and a projection — with no rule saying when each applies. In the framework both are instances of the **same bilinear operation**, $X \mapsto \tilde{A} X \tilde{A}^\dagger$ (with renormalization in the measurement case), applied with an acting element $\tilde{A} \in \mathbb{B}$ of one of two algebraic types: **unitary** ($\tilde{A}\tilde{A}^\dagger = e_0$) or **Hermitian idempotent** ($\tilde{A}^2 = \tilde{A} = \tilde{A}^\dagger$). The two kinds of time evolution are thus one operation form applied to two classes of element. That is an exact restatement, and it moves the centre of gravity of the problem — from a boundary between physical regimes to a choice of acting element — without supplying a rule for the choice.

The residue is stated below as the algebraic form of the problem. The companion article *Decoherence as Idempotent Projection* is then used to say exactly what the framework's dephasing model of decoherence does in this language: it supplies a unique channel that removes the coherences while preserving the outcome statistics, and that channel's output is the **average** of the outcomes, not one of them. The difference between the mixture and the outcome is thereby a difference between a segment of the Bloch ball and an endpoint of that segment. What the framework cannot do is make the endpoint a function of the state. That failure is the selection problem in algebraic form, and no change of notation removes it.

The article proceeds as follows: the problem in standard terms; the algebraic vocabulary of acting elements; the problem stated in algebraic form; what decoherence supplies; the selection step; the preferred basis and the cut; what the restatement changes, and what it does not.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; $\mathbb{M}_+$ is the Hermitian subspace of states and observables, $\mathbb{M}_-$ the anti-Hermitian subspace of generators, and $\mathbb{H}_{\mathbb{B}}$ the real-quaternion subspace. The quaternion units are $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, and $i$ is the central scalar imaginary. Traces are the matrix-representation traces, with $\mathrm{Tr}(\tilde{H}) = 2\,\mathrm{Sc}(\tilde{H})$ and the trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$.

## The Problem in Standard Terms

It is worth separating the strands that the single phrase "the measurement problem" runs together, because the framework bears on them unequally. In the standard formulation:

1. **Two evolutions.** The theory has a unitary evolution for isolated systems and a projective update for measurement, with no rule fixing when each applies. This is the "when does the projection happen" or "cut" question.
2. **The preferred basis.** A unitary interaction of a system with an apparatus generically entangles them; the formalism does not by itself say in which basis the apparatus registers a definite value.
3. **The selection of an outcome.** After decoherence, the reduced state is a mixture. A mixture is not a single outcome: it does not say which value was realised, and the formalism does not supply the missing fact. This is sometimes called the "and/or" problem.
4. **The probabilities.** The Born rule assigns numbers to outcomes; why those numbers are frequencies, and why there is probability at all in a deterministic theory, is a further question.
5. **The regress.** Attempting to place the cut inside the physical world — treating the apparatus, or the observer, as another quantum system — shifts the question to the enlarged system rather than answering it. This is the von Neumann chain.

These strands are not independent, but they are distinct, and a reformulation can bear on one and not another. The remainder of the article states each in the framework's terms and says, for each, what the restatement does and does not change.

## The Algebraic Vocabulary

Recall from *Quantum Mechanics in Biquaternionic Form* that a state of the informational sector is an element

$$
\tilde{\rho} = \tfrac{1}{2}\left(e_0 + i\,\mathbf{r}\right), \qquad \mathbf{r} \in \mathbb{R}^3, \quad |\mathbf{r}| \leq 1,
$$

that a general observable is a Hermitian element

$$
\tilde{H} = h_0\, e_0 + i\,\mathbf{h}, \qquad \mathbf{h} \in \mathbb{R}^3,
$$

and that a pure state is an idempotent

$$
\tilde{P}_\pm(\hat{\mu}) = \tfrac{1}{2}\left(e_0 \pm i\,\hat{\mu}\right), \qquad \hat{\mu} \text{ a unit pure real quaternion},
$$

with $\tilde{P}_\pm^2 = \tilde{P}_\pm$, $\tilde{P}_\pm^\dagger = \tilde{P}_\pm$, $\mathrm{Tr}(\tilde{P}_\pm) = 1$, $\tilde{P}_+ + \tilde{P}_- = e_0$, and $\tilde{P}_+\tilde{P}_- = 0$. The Born rule is the trace formula

$$
p_\pm = \mathrm{Tr}\!\left(\tilde{P}_\pm(\hat{\mathbf{h}})\,\tilde{\rho}\right) = \tfrac{1}{2}\left(1 \pm \hat{\mathbf{h}}\cdot\mathbf{r}\right),
$$

where $\hat{\mathbf{h}} = \mathbf{h}/|\mathbf{h}|$ is the measurement direction.

### One Operation Form, Two Kinds of Element

The central algebraic observation for the present subject is this. For any $\tilde{A} \in \mathbb{B}$ define the **conjugation**

$$
\Gamma_{\tilde{A}}: X \;\longmapsto\; \tilde{A}\,X\,\tilde{A}^\dagger .
$$

The framework's two fundamental operations are both instances of $\Gamma_{\tilde{A}}$, distinguished only by an algebraic property of $\tilde{A}$:

- **Unitary element.** If $\tilde{A} = \tilde{U}$ with $\tilde{U}\tilde{U}^\dagger = e_0$, then $\Gamma_{\tilde{U}}(\tilde{\rho}) = \tilde{U}\tilde{\rho}\tilde{U}^\dagger$ is the reversible evolution of the state (equivalently, of any observable in the Heisenberg picture). It preserves the trace pairing, hence the Born probabilities, and it preserves the norm form; it is an algebra automorphism. It is generated by a Hermitian element: $\tilde{U}(t) = \exp(-i\tilde{H}t/\hbar)$.
- **Idempotent element.** If $\tilde{A} = \tilde{P}_\pm(\hat{\mathbf{h}})$, then, since $\tilde{P}_\pm^\dagger = \tilde{P}_\pm$, the conjugation is the **sandwich**

$$
\Gamma_{\tilde{P}_\pm}(\tilde{\rho}) = \tilde{P}_\pm\,\tilde{\rho}\,\tilde{P}_\pm = p_\pm \tilde{P}_\pm,
$$

using $\tilde{P}_\pm^2 = \tilde{P}_\pm$ and $\mathrm{Tr}(\tilde{P}_\pm\tilde{\rho}) = p_\pm$. As a linear map on the four-dimensional real space $\mathbb{M}_+$, this has rank one: its image is the single ray spanned by $\tilde{P}_\pm$. It does not preserve the norm form unless $\tilde{P}_\pm = e_0$, and it is not invertible.

The measurement update of *Quantum Mechanics in Biquaternionic Form* is the normalized version of the idempotent case,

$$
\tilde{\rho} \;\longmapsto\; \frac{\tilde{P}_\pm\,\tilde{\rho}\,\tilde{P}_\pm}{\mathrm{Tr}\!\left(\tilde{P}_\pm\tilde{\rho}\right)} = \tilde{P}_\pm ,
$$

and the reversible evolution is the unitary case. So the reversible/irreversible dichotomy, which the standard formalism states as a distinction between two postulated dynamics, is here a distinction between two classes of element of one algebra, acting through one operation form.

This restatement is exact. It is also only a restatement: membership in one class or the other is a property of an element, and an element does not act unless something selects it. The selection of the element is what the algebra does not supply, and that is the subject of the next section.

## The Problem in Algebraic Form

Fix a state $\tilde{\rho} \in \mathbb{M}_+$ and an observable $\tilde{H} = h_0 e_0 + i\mathbf{h}$ with spectral idempotents $\tilde{P}_\pm = \tfrac{1}{2}(e_0 \pm i\hat{\mathbf{h}})$ and Born probabilities $p_\pm = \mathrm{Tr}(\tilde{P}_\pm\tilde{\rho})$. The framework places three algebraic objects at our disposal:

1. **The reversible evolution** $\Gamma_{\tilde{U}}(\tilde{\rho}) = \tilde{U}\tilde{\rho}\tilde{U}^\dagger$, with $\tilde{U}\tilde{U}^\dagger = e_0$.
2. **The two conditional outcomes** $\Gamma_{\tilde{P}_\pm}(\tilde{\rho}) = p_\pm \tilde{P}_\pm$; normalized, the post-measurement state is $\tilde{P}_\pm$ itself, produced on the branch labelled $\pm$.
3. **Their statistical average**, the element

$$
\tilde{\rho}_d \;=\; p_+\,\tilde{P}_+ + p_-\,\tilde{P}_- \;=\; \tfrac{1}{2}\left(e_0 + i\,(\hat{\mathbf{h}}\cdot\mathbf{r})\,\hat{\mathbf{h}}\right) .
$$

The third object is the fully dephased state of *Decoherence as Idempotent Projection*, restricted to the measurement direction $\hat{\mathbf{h}}$; it is developed in the next section. It is the element obtained when the outcome is not retained.

**The algebraic form of the measurement problem** is then the following demand, and its unsatisfiability within the algebra:

> The algebra contains both classes of acting element and both operations. It contains no element and no operation that selects the unitary case over the idempotent case, that selects $\tilde{P}_+$ over $\tilde{P}_-$, or that carries the index $\pm$ of the realised outcome. The state $\tilde{\rho}$ determines the *numbers* $p_\pm$ but not *which* of $\tilde{P}_\pm$ occurs.

The last sentence is the selection strand of the problem in algebraic form, and it is worth making exact. The outcome-indexed candidate states are the two idempotents $\tilde{P}_\pm$, with weights $p_\pm$. Among elements of $\mathbb{M}_+$ that (i) are diagonal in the pointer basis of $\hat{\mathbf{h}}$ — that is, carry no coherence between the $\tilde{P}_\pm$ — and (ii) reproduce the Born probabilities, there is exactly one:

$$
\tfrac{1}{2}\left(1 + \hat{\mathbf{h}}\cdot\mathbf{r}\right)\tilde{P}_+ + \tfrac{1}{2}\left(1 - \hat{\mathbf{h}}\cdot\mathbf{r}\right)\tilde{P}_- = \tilde{\rho}_d .
$$

Condition (i) says the outcome has been decided in the pointer basis; condition (ii) says the decision has the correct statistics. The unique element satisfying both is the **mixture**, not either outcome. A single outcome is an endpoint of the pointer diameter; the statistics determine an interior point of it. Putting (i) and (ii) together determines the segment, never the endpoint, whenever $0 < p_\pm < 1$.

This is a statement about elements, and it does not by itself say that no *process* can select. The next sections make the corresponding statement about processes precise, using the dephasing channel.

## What Decoherence Supplies

The companion article *Decoherence as Idempotent Projection* constructs the dephasing channel along a pointer axis $\hat{\mathbf{n}}$ at strength $p \in [0,1]$,

$$
\Phi^{\mathrm{deph}}_p(\tilde{\rho}) = (1-p)\,\tilde{\rho} + p\left(\tilde{P}_+(\hat{\mathbf{n}})\,\tilde{\rho}\,\tilde{P}_+(\hat{\mathbf{n}}) + \tilde{P}_-(\hat{\mathbf{n}})\,\tilde{\rho}\,\tilde{P}_-(\hat{\mathbf{n}})\right),
$$

with Kraus operators $\tilde{K}_0 = \sqrt{1-p}\,e_0$ and $\tilde{K}_{1,2} = \sqrt{p}\,\tilde{P}_\pm(\hat{\mathbf{n}})$, acting on the Bloch vector by

$$
\mathbf{r} \;\longmapsto\; (1-p)\,\mathbf{r} + p\,(\hat{\mathbf{n}}\cdot\mathbf{r})\,\hat{\mathbf{n}} .
$$

Two properties of its fully dephased limit ($p = 1$) matter here. In the measurement setting the pointer axis is the eigendirection of the measured observable, $\hat{\mathbf{n}} = \hat{\mathbf{h}}$, so that the pointer idempotents $\tilde{P}_\pm(\hat{\mathbf{n}})$ coincide with the spectral idempotents $\tilde{P}_\pm$ of $\tilde{H}$ and $p_\pm = \mathrm{Tr}(\tilde{P}_\pm\tilde{\rho})$ are the Born probabilities.

**First, the fully dephased element is unique given the statistics and the absence of coherence.** At $p = 1$ the channel is

$$
\Phi^{\mathrm{deph}}_1(\tilde{\rho}) = \tilde{P}_+\,\tilde{\rho}\,\tilde{P}_+ + \tilde{P}_-\,\tilde{\rho}\,\tilde{P}_- = p_+\,\tilde{P}_+ + p_-\,\tilde{P}_- = \tilde{\rho}_d ,
$$

the diagonal part of $\tilde{\rho}$ in the pointer basis. As the preceding section showed, no other element of $\mathbb{M}_+$ carries the Born statistics and is simultaneously coherence-free in that basis.

**Second, $\tilde{\rho}_d$ is the outcome-weighted average of the two selection operations.** Let $\Lambda_\pm$ denote the constant (reset) channels onto the two outcomes,

$$
\Lambda_\pm(\tilde{X}) = \mathrm{Tr}(\tilde{X})\,\tilde{P}_\pm .
$$

Each $\Lambda_\pm$ is completely positive, trace preserving, and idempotent as a channel; each is what "select the outcome $\pm$" means as an operation. For every state $\tilde{\rho}$ (so $\mathrm{Tr}(\tilde{\rho}) = 1$),

$$
\Phi^{\mathrm{deph}}_1(\tilde{\rho}) = p_+\,\Lambda_+(\tilde{\rho}) + p_-\,\Lambda_-(\tilde{\rho}) ,
$$

since $\Lambda_\pm(\tilde{\rho}) = \tilde{P}_\pm$ and $p_\pm = \mathrm{Tr}(\tilde{P}_\pm\tilde{\rho})$. The fully dephased element is exactly the convex average of the two possible outcomes with their Born weights. Two differences between $\Lambda_\pm$ and $\Phi^{\mathrm{deph}}_1$ are decisive for the problem:

- **The selection channels do not preserve the Born statistics.** $\Lambda_+$ sends every state to $\tilde{P}_+$, so it assigns probability $1$ to the outcome $+$ regardless of $\tilde{\rho}$, whereas the Born probability is $p_+$. A selection channel is a legitimate operation, but it is not a statistics-preserving description of the ensemble.
- **The dephasing channel is a conditional expectation; the selection channels are not.** $\Phi^{\mathrm{deph}}_1$ is the trace-preserving conditional expectation onto the commutative pointer subalgebra $A = \mathbb{C}\tilde{P}_+(\hat{\mathbf{n}}) \oplus \mathbb{C}\tilde{P}_-(\hat{\mathbf{n}})$, hence an orthogonal projection with respect to the trace pairing. The reset channels $\Lambda_\pm$ are idempotent but fail the module property $\Lambda(\tilde{A}\tilde{X}\tilde{B}) = \tilde{A}\,\Lambda(\tilde{X})\,\tilde{B}$ for $\tilde{A}, \tilde{B} \in A$; for example $\Lambda_+(\tilde{\rho}\,\tilde{P}_-) = p_-\,\tilde{P}_+$ while $\Lambda_+(\tilde{\rho})\,\tilde{P}_- = 0$. So "idempotent channel" does not by itself identify the statistics-preserving operation, and the two operations that the problem contrasts — the average and the selection — are both present in the algebra as channels, with different properties.

Geometrically the situation is exact and easy to see. Under $\Phi^{\mathrm{deph}}_p$ the Bloch vector moves along a straight line toward the pointer axis; at $p = 1$ it lands on the pointer diameter at the interior point $(\hat{\mathbf{n}}\cdot\mathbf{r})\,\hat{\mathbf{n}}$. The two outcomes are the endpoints $\pm\hat{\mathbf{n}}$ of that diameter. So the passage from "the measurement has interacted with the environment" to "the measurement has an outcome" is the passage from the segment to an endpoint — a passage that the statistics-preserving channel does not make, and that the algebra does not otherwise perform. That is the sharpened algebraic statement of the "and/or" strand of the measurement problem.

## The Selection Step

The selection step, stated algebraically, is the choice of one Kraus branch of the measurement. The measurement channel in the framework is

$$
\tilde{\rho} \;\longmapsto\; \tilde{P}_+\,\tilde{\rho}\,\tilde{P}_+ + \tilde{P}_-\,\tilde{\rho}\,\tilde{P}_- = \tilde{\rho}_d ,
$$

and its two summands are the two unnormalized branches, with traces $p_\pm$. The physical measurement outcome is obtained by retaining one branch and renormalizing; the renormalized branch is $\tilde{P}_\pm$. The framework therefore contains the conditional operation, and it contains the unconditional channel; what it does not contain is the fact of which branch occurred.

Three observations keep this honest.

**The statistics are a function of the state; the outcome is not.** The element $\tilde{\rho}$ determines the pair $(p_+, p_-)$ — a point of the probability simplex — but not the realised index $\pm$. No element of $\mathbb{M}_+$ at the single-qubit level carries that index: the two outcomes are the endpoints $\pm\hat{\mathbf{n}}$ of the pointer diameter, they exist as elements of the state space, and $\tilde{\rho}$ carries no label saying which of them occurred. This is the algebraic reading of the standard observation that a mixture (proper or improper) does not single out an outcome.

**Enlarging the algebra does not remove the demand; it relocates it.** The index can be carried by a record — an apparatus, or an environment — and in the framework a record is another element of the algebra, which means passing to a tensor product $\mathbb{B}\otimes\mathbb{B}$ (equivalently, a state in $\mathbb{M}_+^{(A)}\otimes\mathbb{M}_+^{(B)}$). The joint state can be taken pure, and its reduced states can be the mixtures $\tilde{\rho}_d$. But the same structure then reappears one level up: the joint object contains the correlations and no rule selecting a definite record value. This is the von Neumann chain in algebraic form. The framework has no algebraic fixed point that terminates it, because the operation that would terminate it — selection — is exactly what is missing.

**The framework's treatment is single-qubit.** The apparatus, the environment, and the macroscopic record are many-body objects; the framework as developed is a single-qubit formalism extended to finite tensor products, and the many-particle, field-theoretic setting in which a realistic apparatus would live is listed among its open problems (*Quantum Mechanics in Biquaternionic Form*, *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*). The algebraic statement of the selection problem given here is therefore the selection problem *for a qubit*; the apparatus version is inherited by tensor product and not developed. This limitation is recorded rather than papered over: the strand of the measurement problem that concerns a macroscopic apparatus is not addressed at the level the framework currently supports.

## The Preferred Basis and the Cut

The preferred-basis strand appears in the framework in a precise and limited form. The pointer direction $\hat{\mathbf{n}}$ is an input to the dephasing channel and to the observable whose idempotents figure in the measurement. The algebra supplies, once $\hat{\mathbf{n}}$ is given, the pointer idempotents, the commutative pointer subalgebra $A$, its $U(1)$ phase symmetry, the fixed states, and the decaying coherences. It does not supply $\hat{\mathbf{n}}$: *Decoherence as Idempotent Projection* states this limitation explicitly, and its reason is structural. The direction is fixed by the system–environment interaction, and the algebra of the operational description represents the consequence of that interaction (the channel and the subalgebra) without containing the interaction dynamics. So the preferred-basis problem is neither sharpened into a solution nor worsened: it is located, unchanged, at the point where the direction enters as data.

The cut strand behaves similarly. In the standard formulation the cut is a boundary between a quantum description and a classical description. In the framework the corresponding choice is the choice of acting element at each step — unitary or idempotent. That is a reformulation of the same freedom, not a derivation of it. The framework contains no condition that says when an interaction counts as a measurement; a physical measurement interaction of a system with an apparatus is, microscopically, a unitary interaction of the larger system, with the idempotent sandwich an effective description of the record. The idempotent is therefore a bookkeeping element for the outcome, not a second microscopic dynamics. That the two classes of element sit in one algebra does not say which one a given physical process realises.

## What the Reformulation Changes

The changes are changes in statement, not in physics, and they are worth setting out exactly.

1. **"Two incompatible dynamics" becomes "one operation form, two element types."** The standard problem is often stated as a clash between unitary evolution and projective collapse, two postulates of different character. In the framework both are $\Gamma_{\tilde{A}}$ for $\tilde{A}$ unitary or idempotent, and the dichotomy is a property of $\tilde{A}$. This does not remove the dichotomy and does not fix the cut; it changes what is primitive in its statement. Whether it reduces a "postulate count" is a question about exposition, not about the world.

2. **The mixedness of the decohered state is one scalar, and the residual gap is geometric.** $\tilde{\rho}^2 - \tilde{\rho} = \tfrac{1}{4}(|\mathbf{r}|^2 - 1)e_0$ measures the loss of idempotency, and full dephasing is the trace-preserving conditional expectation onto the pointer subalgebra. The gap between "mixture" and "outcome" is then exactly the gap between an interior point of the pointer diameter and its endpoints. This is a clean and exact way to state the strand it states; it is a picture, not a mechanism.

3. **The statistics-preserving and selection operations are separated exactly.** $\Phi^{\mathrm{deph}}_1$ is the unique coherence-free, statistics-preserving element-assignment, and for a state $\tilde{\rho}$ it is the convex average $p_+\Lambda_+ + p_-\Lambda_-$ of the two selection channels. The framework thus exhibits, as algebraic objects, both what decoherence gives and what it does not give, and the relation between them. This is a sharpening of the standard statement, not a change in its content.

4. **States and observables in one space make the provenance-blindness of the state explicit.** A state is an element of $\mathbb{M}_+$, and distinct preparations with the same Bloch vector give the same element. The framework thus makes it a statement about one subspace that no element distinguishes a proper from an improper mixture; the record that would distinguish them is not in $\tilde{\rho}$. This is inherited from *Quantum Mechanics in Biquaternionic Form* and *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, and it is a particularly direct statement of why the "and/or" problem is not a defect of bookkeeping.

5. **The form of the Born rule is algebraic.** The probabilities $p_\pm$ are the trace pairing $\mathrm{Tr}(\tilde{P}_\pm\tilde{\rho})$. As the companion article *The Born Rule as a Trace Formula — Derivation and Comparison* argues, this derives the **form** of the rule and the objects it relates, not its empirical content: the identification of the pairing with observed frequency is not an algebraic consequence.

## What the Reformulation Does Not Change

The reformulation does not, and is not presented as, resolving the measurement problem. Explicitly, it does **not**:

- **Select an outcome.** No element of $\mathbb{M}_+$ and no operation in the algebra makes the realised outcome a function of the state. The statistics are determined; the outcome is not. This is the selection problem, restated and not solved.
- **Derive the preferred basis.** The pointer direction $\hat{\mathbf{n}}$ is an input; the framework represents einselection's structure but not its dynamics.
- **Fix the cut.** The choice of acting element is the framework's form of the cut, and it is not derived.
- **Explain probability.** The trace formula gives the numbers; it does not explain why they are frequencies or why a deterministic formalism has probabilities. This is the same division of labour as in the Born-rule article.
- **Terminate the regress.** Enlarging to a tensor product with a record relocates the selection demand; it does not satisfy it.
- **Distinguish the standard interpretations.** The framework is compatible with a structural reading and is not committed to Copenhagen, many-worlds, relational, or collapse readings; nothing in the algebra decides among them. In particular, the algebra contains both the unitary and the idempotent descriptions of a measurement, and it does not say which describes the world.
- **Predict anything new.** As with the rest of the framework, the empirical content of standard quantum mechanics is reproduced, and the question of a distinguishing prediction is open. A reformulation with the same predictions cannot settle an empirical dispute.

The honest summary is a division of labour. The algebraic form makes the *structure* of the problem unusually explicit: one operation form, two element types, a statistics-preserving average whose output is a mixture, and a selection operation that is not a function of the state. It does not make the problem go away, and the gap left open is exactly the gap that was there before, now with a name in the algebra: the element that would have to select is not in the algebra.

## Summary

The measurement problem, stated in the framework's own terms, is the demand that the biquaternion algebra supply a criterion for measurement — and its unsatisfiability. The framework offers a single operation form, $X \mapsto \tilde{A}X\tilde{A}^\dagger$, with the acting element either unitary ($\tilde{U}\tilde{U}^\dagger = e_0$, reversible evolution) or Hermitian idempotent ($\tilde{P}^2 = \tilde{P} = \tilde{P}^\dagger$, the projective sandwich). The Born rule is the trace pairing $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$. The unitary evolution produces no definite outcome; the idempotent sandwich produces one but comes with no rule selecting which idempotent acts, and no rule selecting the idempotent case over the unitary case.

Decoherence, in the framework's worked dephasing model, is the channel $\Phi^{\mathrm{deph}}_p$ of *Decoherence as Idempotent Projection*. At full strength it is the trace-preserving conditional expectation onto the pointer subalgebra, and it is the unique coherence-free assignment that reproduces the Born statistics: its output is the mixture $\tilde{\rho}_d = p_+\tilde{P}_+ + p_-\tilde{P}_-$, which, for a state $\tilde{\rho}$, is the convex average $p_+\Lambda_+ + p_-\Lambda_-$ of the two selection channels. The mixture is an interior point of the pointer diameter; the outcomes are its endpoints. Decoherence supplies the statistics and the segment, not the endpoint and not the index.

What the reformulation changes is the form of the statement: two dynamics become one operation form over two element types; the mixture-versus-outcome gap becomes a segment-versus-endpoint gap; the statistics-preserving and selection operations are separated exactly; the provenance-blindness of the state becomes a statement about one subspace; and the form of the Born rule is algebraic. What it does not change is the physics or the difficulty: no outcome is selected, no preferred basis is derived, no cut is fixed, no probability is explained, no regress terminated, no interpretation decided, and no prediction changed. The algebraic form is a sharpened statement of the measurement problem, not a solution to it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{M}_+$ | Hermitian subspace (states and observables) |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (generators of reversible evolution) |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\tilde{\rho} = \tfrac{1}{2}(e_0 + i\mathbf{r})$ | State, $\|\mathbf{r}\| \leq 1$ (Bloch ball) |
| $\tilde{H} = h_0e_0 + i\mathbf{h}$ | Hermitian observable |
| $\tilde{P}_\pm(\hat{\mu}) = \tfrac{1}{2}(e_0 \pm i\hat{\mu})$ | Idempotent (pure state, projective outcome) |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula (Born rule) |
| $p_\pm = \mathrm{Tr}(\tilde{P}_\pm(\hat{\mathbf{h}})\tilde{\rho})$ | Outcome probabilities |
| $\hat{\mathbf{h}} = \mathbf{h}/\|\mathbf{h}\|$, $\hat{\mathbf{n}}$ | Measurement and pointer directions |
| $\Gamma_{\tilde{A}}(X) = \tilde{A}X\tilde{A}^\dagger$ | Conjugation; unitary evolution ($\tilde{A} = \tilde{U}$) or projective sandwich ($\tilde{A} = \tilde{P}_\pm$) |
| $\tilde{U}\tilde{U}^\dagger = e_0$ | Unitary element (reversible evolution) |
| $\tilde{P}_\pm^2 = \tilde{P}_\pm = \tilde{P}_\pm^\dagger$ | Hermitian idempotent (orthogonal projection; irreversible) |
| $\tilde{\rho}_d = p_+\tilde{P}_+ + p_-\tilde{P}_-$ | Fully dephased state (pointer-diagonal) |
| $\Phi^{\mathrm{deph}}_p$ | Dephasing channel along $\hat{\mathbf{n}}$ at strength $p$ |
| $\Lambda_\pm(\tilde{X}) = \mathrm{Tr}(\tilde{X})\tilde{P}_\pm$ | Selection (reset) channels onto the outcomes |
| $A = \mathbb{C}\tilde{P}_+ \oplus \mathbb{C}\tilde{P}_-$ | Pointer (commutative) subalgebra |
| $\mathrm{Tr}(\tilde{\rho}^2)$ | Purity; $= \tfrac{1}{2}(1 + \|\mathbf{r}\|^2)$ |
| $\tilde{\rho}^2 - \tilde{\rho} = \tfrac{1}{4}(\|\mathbf{r}\|^2 - 1)e_0$ | Deviation from idempotency (mixedness) |

## Further Reading

- John von Neumann, *Mathematical Foundations of Quantum Mechanics* (Princeton, 1932), for the projection postulate, the density matrix, and the regress that bears his name.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the foundational statement of the two evolutions.
- Asher Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), for non-selective versus selective measurement, the Bloch-ball geometry, and the measurement problem as a statement about ensembles.
- W. H. Zurek, "Decoherence, einselection, and the quantum origins of the classical," *Reviews of Modern Physics* **75** (2003) 715, for pointer bases, einselection, and the measurement problem in the decoherence setting.
- E. Joos and H. D. Zeh, "The emergence of classical properties through interaction with the environment," *Zeitschrift für Physik B* **59** (1985) 223, for the original environment-induced selection of a preferred basis.
- K. Kraus, *States, Effects, and Operations* (Springer, 1983), for measurement as a completely positive map with classical outcomes, and for conditional expectations.
- D. Petz, *Quantum Information Theory and Quantum Statistics* (Springer, 2008), for trace-preserving conditional expectations and the fixed-point structure of completely positive maps.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the Kraus representation, the dephasing channel, and the reset channel.
- The companion articles of this series: *Quantum Mechanics in Biquaternionic Form*, *The Born Rule as a Trace Formula — Derivation and Comparison*, *Decoherence as Idempotent Projection*, *The Quantum–Classical Divide in the Biquaternion Framework*, and *Entangled Subsystems in the Biquaternion Framework*.
