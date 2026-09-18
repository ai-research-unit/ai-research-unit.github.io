
# Entangled Subsystems in the Biquaternion Framework: What the Reformulation Changes and What It Does Not

## Introduction

Entanglement is the part of quantum mechanics where the conceptual debates are sharpest. The EPR argument, Bell's theorem, the measurement problem, the tension between instantaneous correlations and relativistic causality, and the dispute over whether "classical entanglement" deserves the name — all of these have been argued for decades, and none of them is settled. When a new formulation of quantum mechanics appears, it is natural to ask whether it brings new light to these debates.

This article asks that question for the biquaternion framework developed in the companion articles. The honest answer, stated up front, is: **the framework reframes the debates; it does not resolve them.** It is a reformulation of standard quantum mechanics, not a new theory, and it reproduces all of the standard predictions. It cannot settle an empirical dispute that standard quantum mechanics does not already settle, and it cannot supply a mechanism where standard quantum mechanics has none. What it does do is change the language in which the debates are stated, and in a few places the change of language makes the structure of the problem more visible.

The article is organized as follows. First, the biquaternion description of an entangled subsystem is recalled: the singlet as a single algebraic object, the reduced state as a partial trace, the correlation function as a bilinear pairing, and no-signaling as an identity satisfied by the partial trace. Then the five debates are revisited one by one, with a clear statement of what the framework does and does not contribute to each. Then the structural features of the framework that are genuinely new — as structure, not as physics — are collected. The article closes with the open questions that would have to be answered before the framework could be said to bring more than a change of notation.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$. The quaternion units are $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, and $i$ is the scalar imaginary. The two-qubit state space is the tensor product $\mathbb{B}\otimes\mathbb{B} \cong M_4(\mathbb{C})$, with the trace $\mathrm{Tr}(x\otimes y) = \mathrm{Tr}_\mathbb{B}(x)\cdot\mathrm{Tr}_\mathbb{B}(y)$.

## The Entangled Subsystem in the Biquaternion Language

### The singlet as one algebraic object

In the standard formulation, the singlet state is a single vector $|\Psi^-\rangle$ in $\mathbb{C}^2\otimes\mathbb{C}^2$. In the biquaternion formulation, it is a single idempotent of the tensor product:

$$
P_{\mathrm{singlet}} = \tfrac{1}{4}\left(e_0\otimes e_0 + e_1\otimes e_1 + e_2\otimes e_2 + e_3\otimes e_3\right).
$$

This is the same object viewed in a different language, but the language matters for how the correlations are read. The singlet is not a pair of systems that then has to be correlated; it is one element of the tensor-product algebra, and its correlations are built into the tensor-product terms $e_j\otimes e_j$. There is no pair of "two separate things" whose correlation has to be explained; the algebraic object itself is not separable.

The same is true in Hilbert-space language, since $|\Psi^-\rangle$ is also a single vector. But the biquaternion formulation makes the point more vivid, because the idempotents are the canonical objects of the algebra and the tensor product is the natural algebraic operation, not an additional postulate. In the biquaternion reading, the entanglement is a fact about the *pairing structure* of the algebra, not about a dynamical influence passing between two systems.

### The reduced state as a partial trace

The state of one subsystem is obtained by tracing out the other:

$$
\rho_1 = \mathrm{Tr}_2(P_{\mathrm{singlet}}) = \tfrac{1}{2}e_0.
$$

This is the maximally mixed state of a qubit, at the center of the Bloch ball. Its purity is $\mathrm{Tr}(\rho_1^2) = \tfrac{1}{2}$ and its von Neumann entropy is $\log 2$. In the biquaternion formulation, this mixedness is read off directly: the off-diagonal tensor-product terms $e_j\otimes e_j$ in the singlet, after tracing out the second factor, produce the scalar-only element $\tfrac{1}{2}e_0$, which is not idempotent. The mixedness of the reduced state is the algebraic trace of the entanglement of the joint state.

### The correlation function as a bilinear pairing

The spin correlation function, computed in full in *Exercise 6*, is

$$
E(\hat{a}, \hat{b}) = \mathrm{Tr}\!\left(P_{\mathrm{singlet}}\circ\bigl((i\hat{a})\otimes(i\hat{b})\bigr)\right) = -\hat{a}\cdot\hat{b}.
$$

This is the tensor-product trace pairing between the state idempotent and the correlation observable. It is the same algebraic operation — the trace pairing — that gives the Born rule for a single qubit. The correlation function is not a separate postulate; it is the natural pairing between two elements of the tensor-product algebra.

### Steering as a conditional idempotent

The phenomenon of EPR steering — that measuring one particle's spin determines the conditional state of the other — has a particularly clean form in the biquaternion language. Suppose Alice measures particle 1 along $\hat{a}$ and obtains the outcome $+$. The unnormalized post-measurement joint state is

$$
\bigl(P_+(\hat{a})\otimes e_0\bigr)\circ P_{\mathrm{singlet}}\circ\bigl(P_+(\hat{a})\otimes e_0\bigr),
$$

where $P_+(\hat{a}) = \tfrac{1}{2}(e_0 + i\hat{a})$. Computing directly, using $P_+(\hat{a})\,e_k\,P_+(\hat{a}) = \tfrac{1}{2}a_k(\hat{a} - ie_0)$ and $\hat{a} - ie_0 = -2iP_+(\hat{a})$, gives

$$
\bigl(P_+(\hat{a})\otimes e_0\bigr)\circ P_{\mathrm{singlet}}\circ\bigl(P_+(\hat{a})\otimes e_0\bigr) = \tfrac{1}{2}\,P_+(\hat{a})\otimes P_-(\hat{a}),
$$

where $P_-(\hat{a}) = \tfrac{1}{2}(e_0 - i\hat{a})$. The normalized post-measurement state is therefore the product state

$$
P_+(\hat{a})\otimes P_-(\hat{a}).
$$

The joint state is now a product: particle 1 is in the pure idempotent $P_+(\hat{a})$, and particle 2 is in the pure idempotent $P_-(\hat{a})$ — spin-down along the direction Alice chose to measure, irrespective of any distance between the particles.

This is the biquaternion expression of EPR steering. The collapse of the joint state under a local projector factorizes the joint idempotent into a product of idempotents, one on each factor. The "spooky" character is that the direction $\hat{a}$ chosen by Alice appears in the conditional state of particle 2; the "non-spooky" character is that this is a *conditional* statement, not a signal, because the unconditional reduced state of particle 2 is unchanged.

### No-signaling as a partial-trace identity

The last observation is the algebraic content of the no-communication theorem. If Alice applies a local unitary operation $\tilde{U}\otimes e_0$ to the joint state, the reduced state of particle 2 is unchanged:

$$
\mathrm{Tr}_1\!\left((\tilde{U}\otimes e_0)\,\tilde{\rho}\,(\tilde{U}^\dagger\otimes e_0)\right) = \mathrm{Tr}_1(\tilde{\rho}),
$$

where $\mathrm{Tr}_1$ denotes the partial trace over particle 1. This is a direct consequence of the cyclicity of the trace: for any element $\tilde{\rho} = \sum_i a_i\otimes b_i$ of the tensor product,

$$
\mathrm{Tr}_1\!\left((\tilde{U}\otimes e_0)\,\tilde{\rho}\,(\tilde{U}^\dagger\otimes e_0)\right) = \sum_i \mathrm{Tr}_\mathbb{B}(\tilde{U}a_i\tilde{U}^\dagger)\,b_i = \sum_i \mathrm{Tr}_\mathbb{B}(a_i)\,b_i = \mathrm{Tr}_1(\tilde{\rho}).
$$

No-signaling is not a dynamical theorem in this reading; it is the cyclicity of the trace, applied to the partial trace. It says that correlations are real, that they are a property of the joint state, and that no local operation on one factor can be detected by measurements on the other.

## The Five Debates, Revisited

With the algebraic structure of the entangled subsystem in place, we can ask what the framework contributes to each of the five debates.

### 1. Local realism and "spooky action at a distance"

The EPR argument asks whether quantum mechanics is *complete*: whether the state description exhausts physical reality, or whether there are additional "elements of reality" that the formalism does not represent. The argument proceeds by assuming local realism — that physical properties are localized and that no influence propagates faster than light — and concludes that either quantum mechanics is incomplete or the assumption of local realism is wrong.

The biquaternion framework does not answer this question. What it does is state the entangled state in a language in which the correlations are visibly *structural* rather than visibly *dynamical*. The singlet is not two systems that then have to be correlated; it is one element of the tensor-product algebra, and the correlation function is a bilinear pairing between that element and a tensor-product observable. Nothing propagates between the particles; there is a pairing rule.

Whether this structural reading satisfies a local-realist depends on what "local realism" is taken to require. If local realism requires that all correlations be traceable to dynamical influences propagating through space, then the framework's reading of entanglement is incompatible with it — as is standard quantum mechanics. If local realism can be rephrased as a requirement on the *structure* of physical states, then the framework offers a language in which the requirement can be more sharply stated. The framework does not legislate which of these readings is correct; it merely makes the structural character of the correlations more explicit.

### 2. Violation of Bell's inequalities

Bell's theorem says that no local hidden-variable model can reproduce the quantum correlations of the singlet. The framework reproduces the standard correlation function $E(\hat{a}, \hat{b}) = -\hat{a}\cdot\hat{b}$ and the standard Tsirelson bound $2\sqrt{2}$ for the CHSH combination. Bell's theorem is untouched.

What the framework changes is the *location* of the non-classicality. In the Hilbert-space formalism, the Born rule is a postulate, and the violation of Bell's inequality is a fact about joint probabilities that follows from that postulate. In the biquaternion framework, the Born rule is the trace pairing on $\mathbb{M}_+$, and the correlation function is a bilinear pairing between a state idempotent and a tensor-product observable. The non-classicality is then a fact about the *pairing rule* of the algebra, not about an independent probabilistic postulate.

This is a clarification of where the quantum character sits, not a resolution of the tension. Bell's theorem stands: the algebra is not a local hidden-variable model, and its correlations cannot be simulated by any local classical model.

### 3. The measurement problem

The measurement problem is the fact that standard quantum mechanics has two kinds of time evolution — unitary and projective — and the formalism does not say when each applies. Various solutions have been proposed (many-worlds, decoherence, collapse models, relational quantum mechanics), but there is no consensus.

The biquaternion framework has something structural to offer here. In standard quantum mechanics, unitary evolution and projective collapse are different postulates, governing different types of process. In the biquaternion framework, both are properties of *acting elements* of the algebra:

- **Unitary elements** $\tilde{U}$ satisfy $\tilde{U}\tilde{U}^\dagger = e_0$ and generate reversible evolution by rotor conjugation.
- **Idempotent elements** $\tilde{P}$ satisfy $\tilde{P}^2 = \tilde{P}$ and generate irreversible projection by the sandwich operation.

The reversible/irreversible dichotomy is not an additional postulate; it is the algebraic dichotomy between two classes of elements of one algebra. This is a genuine reframing: the measurement problem is no longer "two incompatible dynamics glued together" but "one algebra with two classes of elements."

But the reframing does not solve the problem. The framework does not say which idempotent is selected in a given measurement, or why the transition from unitary to idempotent action occurs. The selection problem persists. What the framework offers is a cleaner *statement* of the problem, not a solution.

### 4. Instantaneous correlation versus no-communication

The conceptual tension is that measurements on one particle seem to instantaneously affect the state of a distant particle, while relativity forbids faster-than-light communication. The resolution is that the "effect" is conditional — the conditional state of particle 2 depends on Alice's choice, but the unconditional state does not — and the no-communication theorem shows that no signal can be transmitted.

In the biquaternion framework, this resolution has a clean algebraic form. The conditional statement (steering) is the factorization of the joint idempotent into a product under a local projector, as computed above. The unconditional statement (no-signaling) is the cyclicity of the partial trace. The two statements together show that the correlations are real but that the marginal statistics of each subsystem are invariant under local operations on the other.

This is not a new resolution; it is the standard resolution stated in algebraic language. But the algebraic form makes vivid *why* the tension is conceptual and not physical: the correlations live in the joint state, the joint state is not accessible from either factor alone, and the partial trace that gives the reduced state of either factor is invariant under local operations on the other.

### 5. Quantum versus classical entanglement

The most contested debate in the list is whether "entanglement" is a strictly quantum phenomenon or whether analogous non-separable structures in classical wave optics and classical vector spaces deserve the name. The dispute is partly terminological and partly substantive, and the two are not always clearly separated.

The framework has something to say here, and the development is extensive enough to require a separate article. In brief, the framework contributes at two levels.

**Structurally**, the split $\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+$ suggests a candidate home for the distinction. Quantum entanglement is a property of states in the informational sector $\mathbb{M}_+$; classical non-separability is a property of classical field configurations, which live in the material sector $\mathbb{M}_-$ or in its complexification. Under this reading, the quantum state is a *fundamental* element of $\mathbb{M}_+^{\otimes n}$, while the classical coherence matrix is a *derived* element of the same space, obtained as a second-order correlation of a deeper classical field configuration.

**Operationally**, the framework has a natural algebraic home for the criterion recently proposed by Korolkova, Sánchez-Soto, and Leuchs (arXiv:2405.15692, 2024): the distinction between quantum and classical non-separability is the **number of idempotent operations** applied to the two partitions of the state.

- **Quantum entanglement** requires **two idempotents** — two projective measurements, one on each partition — and produces **statistical correlations** between the outcomes.
- **Classical non-separability** requires **one idempotent and one unitary** — one measurement and one filter, sorter, or basis choice — and produces **deterministic correlations** between the filter setting and the single measurement outcome.

In the framework's language, this is the algebraic dichotomy between

$$
\tilde{P}_A \otimes \tilde{P}_B \quad (\text{quantum}) \qquad \text{and} \qquad \tilde{U}_A \otimes \tilde{P}_B \quad (\text{classical}),
$$

which is the same reversible/irreversible dichotomy that the framework already uses to distinguish evolution from measurement (see Section 3 of this list).

The companion article, *The Quantum–Classical Divide in the Biquaternion Framework: An Operational Criterion*, develops this in detail. It engages with the Korolkova–Sánchez-Soto–Leuchs paper, maps the paper's four subsets (two objects; non-local; two measurements; non-separable) to the framework's algebra, distinguishes fundamental from derived elements of the tensor-product space, and states what the framework adds — a natural algebraic home for the criterion, and a structural reason for it — and what remains open — a dynamics of the cross-sector coupling, and an empirical prediction the operational criterion does not already have.

## What the Reformulation Makes Visible

Collecting the observations above, the biquaternion framework makes the following structural features of entanglement more visible than they are in the Hilbert-space formalism.

**1. The singlet is one algebraic object.** The entangled state is not a pair of systems whose correlation must be explained; it is one element of the tensor-product algebra, and its correlations are built into the tensor-product structure from the start.

**2. The correlation function is a bilinear pairing.** The correlation $E(\hat{a}, \hat{b})$ is the tensor-product trace pairing between the state idempotent and the correlation observable. It is the same algebraic operation that gives the Born rule for a single qubit. There is no additional probabilistic postulate.

**3. The reduced state's mixedness is the algebraic trace of entanglement.** The partial trace of the singlet produces $\tfrac{1}{2}e_0$, which is not idempotent. The mixedness of the reduced state is the algebraic residue of the entanglement of the joint state.

**4. Steering is a factorization of the joint idempotent.** A local projector applied to the singlet produces a product state $P_+(\hat{a})\otimes P_-(\hat{a})$, with the second factor determined by Alice's choice of direction. This is the biquaternion form of EPR steering.

**5. No-signaling is cyclicity of the trace.** The invariance of the reduced state under local unitaries is the cyclicity of the trace applied to the partial trace.

**6. The reversible/irreversible dichotomy is algebraic.** Unitary and idempotent elements are two classes of elements of one algebra, not two separate postulates.

**7. The quantum/classical divide has a candidate structural home.** The split $\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+$ suggests a structural criterion for where entanglement lives, and the reversible/irreversible dichotomy gives the operational criterion an algebraic home. The development of this criterion is treated in the companion article.

## What the Reformulation Does Not Claim

It is equally important to state what the framework does **not** do, since the temptation to over-read a reformulation is strong.

It does **not**:

1. **Resolve the EPR completeness question.** The framework does not say whether the state description is complete. It only states the state in a language in which the correlations are visibly structural.

2. **Change any Bell-inequality prediction.** The framework reproduces the standard correlation function and the standard Tsirelson bound. Bell's theorem stands.

3. **Solve the measurement problem.** The framework relocates the unitary/projective dichotomy into the algebra, but it does not say which idempotent is selected, or why the transition from unitary to idempotent action occurs. The selection problem persists.

4. **Provide a mechanism for the correlations, or a way to send signals.** There is no dynamical channel in the framework. The correlations are a pairing, and the pairing is invariant under local operations on one factor.

5. **Settle whether "classical entanglement" is genuine entanglement.** The framework offers a natural home for the operational criterion of Korolkova, Sánchez-Soto, and Leuchs, and a structural reason for it, but it does not yet predict anything the operational criterion does not already predict.

6. **Make an empirical prediction that distinguishes it from standard quantum mechanics.** As the companion articles emphasize, empirical contact is the central open problem. Until the framework predicts something that standard quantum mechanics does not, the debates are reframed, not resolved.

## Open Questions

The questions raised by this article are open, and they constitute a research agenda.

**1. Empirical contact.** What quantitative prediction distinguishes the biquaternion framework from standard quantum mechanics? This is the central question, and the one on which the eventual evaluation of the framework depends. Without it, the framework remains a reformulation.

**2. The dynamics of the two sectors.** The framework describes the algebraic structure of $\mathbb{M}_-$ and $\mathbb{M}_+$, but it does not specify a dynamics that couples them beyond the standard Lorentz coupling via rotor conjugation. A genuinely new coupling would be where new physical content could reside.

**3. The quantum/classical criterion.** Can the operational criterion of Korolkova, Sánchez-Soto, and Leuchs — two idempotents is quantum, one idempotent and one unitary is classical — be turned into a criterion with dynamical content, rather than a criterion about which operations are available? The companion article discusses this and the open questions it raises. The central open problem is whether the *number of available idempotents* can itself become a dynamical variable, and whether a state can transition from quantum to classical through the loss of an idempotent measurement channel.

**4. The measurement problem in the framework.** Does the algebraic dichotomy between unitary and idempotent elements suggest a resolution of the selection problem, or does it merely restate it?

**5. The status of the informational sector.** Is $\mathbb{M}_+$ physically realised as a distinct sector, or is it only a mathematical structure that happens to describe the operator algebra of a qubit? This is the question on which the interpretive content of the framework depends.

**6. Extension to many qubits and quantum field theory.** The framework is developed for a single qubit and for two-qubit systems. The extension to $n$ qubits, to second quantization, and to quantum field theory is the natural continuation, and it is the setting in which questions about entanglement, locality, and information acquire their full content.

## Summary

The biquaternion framework is a reformulation of quantum mechanics, not a new theory, and its contribution to the entanglement debates is a reframing, not a resolution.

It reformulates:

- The singlet as one element of the tensor-product algebra, with correlations built into the tensor-product structure.
- The correlation function as a bilinear pairing, the same trace pairing that gives the Born rule.
- The reduced state's mixedness as the algebraic residue of the entanglement of the joint state.
- Steering as a factorization of the joint idempotent under a local projector.
- No-signaling as the cyclicity of the partial trace.
- The reversible/irreversible dichotomy as the algebraic dichotomy between unitary and idempotent elements.
- The quantum/classical divide as a candidate structural distinction between $\mathbb{M}_-$ and $\mathbb{M}_+$, and as a natural algebraic home for the operational criterion of Korolkova, Sánchez-Soto, and Leuchs, as developed in the companion article.

It does not:

- Resolve the EPR completeness question.
- Change any Bell-inequality prediction.
- Solve the measurement problem.
- Provide a mechanism for the correlations.
- Settle the classical-entanglement dispute.
- Make an empirical prediction that distinguishes it from standard quantum mechanics.

The honest position is this. The framework makes certain structural features of entanglement more visible, and it gives a natural algebraic home to an operational criterion that the literature has already identified as decisive. Whether that visibility and that home constitute new light on the debates, or merely a more elegant notation for the same unresolved questions, is exactly the question that the framework's own "empirical contact" open problem poses. Until the framework predicts something that standard quantum mechanics does not, the debates are reframed, not resolved.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{M}_-$ | Material sector (anti-Hermitian): four-vectors of relativity |
| $\mathbb{M}_+$ | Informational sector (Hermitian): states and observables |
| $\mathbb{B}\otimes\mathbb{B}$ | Two-qubit tensor product, $\cong M_4(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $P_{\mathrm{singlet}} = \tfrac{1}{4}(e_0\otimes e_0 + \sum_k e_k\otimes e_k)$ | Singlet idempotent |
| $P_\pm(\hat{a}) = \tfrac{1}{2}(e_0 \pm i\hat{a})$ | Single-qubit idempotents along $\hat{a}$ |
| $\mathrm{Tr}_2(a\otimes b) = a\,\mathrm{Tr}_\mathbb{B}(b)$ | Partial trace over the second factor |
| $\rho_1 = \mathrm{Tr}_2(P_{\mathrm{singlet}}) = \tfrac{1}{2}e_0$ | Reduced state of particle 1 |
| $E(\hat{a}, \hat{b}) = \mathrm{Tr}(P_{\mathrm{singlet}}\circ((i\hat{a})\otimes(i\hat{b})))$ | Correlation function |
| $\tilde{U}\tilde{U}^\dagger = e_0$ | Unitary element (reversible evolution) |
| $\tilde{P}^2 = \tilde{P}$ | Idempotent element (irreversible projection) |
| $\mathrm{Tr}(x\otimes y) = \mathrm{Tr}_\mathbb{B}(x)\cdot\mathrm{Tr}_\mathbb{B}(y)$ | Tensor-product trace |
| $2\sqrt{2}$ | Tsirelson bound for the CHSH combination |

## Further Reading

- A. Einstein, B. Podolsky, N. Rosen, "Can quantum-mechanical description of physical reality be considered complete?" *Physical Review* **47** (1935) 777–780, for the original EPR argument.
- J. S. Bell, "On the Einstein–Podolsky–Rosen paradox," *Physics* **1** (1964) 195–200, for Bell's theorem.
- E. Schrödinger, "Discussion of probability relations between separated systems," *Mathematical Proceedings of the Cambridge Philosophical Society* **31** (1935) 555–563, for the original discussion of the reduced density matrix and steering.
- A. Aspect, P. Grangier, G. Roger, "Experimental tests of realistic local theories via Bell's theorem," *Physical Review Letters* **47** (1981) 460–463, and subsequent experiments, for the experimental violation of Bell's inequalities.
- N. Korolkova, L. Sánchez-Soto, and G. Leuchs, "An operational distinction between quantum entanglement and classical non-separability," arXiv:2405.15692 (2024), for the operational criterion discussed in Section 5 and developed in the companion article.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the standard treatment of entanglement, Bell states, and the no-communication theorem.
- Wojciech H. Zurek, "Decoherence, einselection, and the quantum origins of the classical," *Reviews of Modern Physics* **75** (2003) 715–775, for the modern understanding of the quantum/classical transition.
- Robert F. Spekkens, "Evidence for the epistemic view of quantum states: A toy theory," *Physical Review A* **75** (2007) 032110, and subsequent work, for a careful treatment of the quantum/classical divide.
- The companion articles of this series: *Introduction to the Biquaternion Universe*, *Why Complexify Spacetime?*, *$\mathbb{M}_-$ as the Material Space*, *$\mathbb{M}_+$ as the Informational Space*, *Quantum Mechanics in Biquaternionic Form*, *Exercises 1–6*, and *The Quantum–Classical Divide in the Biquaternion Framework: An Operational Criterion*.

