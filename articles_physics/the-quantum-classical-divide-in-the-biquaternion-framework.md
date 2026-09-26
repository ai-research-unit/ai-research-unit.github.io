# __The Quantum–Classical Divide in the Biquaternion Framework__

## Introduction

The dispute over whether "classical entanglement" is genuine entanglement has been argued for over two decades, and it shows no sign of settling. On one side, Eberly and collaborators have argued that entanglement is a **vector-space property** — present in any theory whose states live in a tensor-product vector space — so that there is no essential distinction between quantum and classical entanglement. On the other side, Karimi and Boyd have responded that "entanglement is a property of the quantum world; classical systems need not apply," pointing to the absence of non-locality in the classical cases. Both sides can point to experiments that support their reading, and the dispute has become partly substantive and partly terminological.

A recent paper by Korolkova, Sánchez-Soto, and Leuchs (arXiv:2405.15692, 2024) proposes a way out of this impasse. Their claim is operational: the distinction between quantum and classical non-separability is not in the states, not in the non-locality, not in the number of particles involved, and not in the mathematical non-separability itself. It is in **the operations performed**. Quantum entanglement involves **two projective measurements** on the two partitions of the Hilbert space, producing statistical correlations between their outcomes. Classical non-separability involves **one projective measurement** plus one **unitary filtering or sorting operation**, producing deterministic correlations between the filter setting and the single measurement outcome. The paper presents this as the decisive criterion.

This article asks a specific question: does the biquaternion framework developed in the companion articles have a natural home for the operational criterion, and if so, does it add anything to it?

The answer to the first part is yes. The framework already distinguishes between two kinds of operation: unitary elements $\tilde{U}$ (with $\tilde{U}\tilde{U}^\dagger = e_0$) generate reversible evolution by rotor conjugation; idempotent elements $\tilde{P}$ (with $\tilde{P}^2 = \tilde{P}$) generate irreversible projection by the sandwich operation. The operational criterion of Korolkova, Sánchez-Soto, and Leuchs — count the idempotents applied to the two partitions — is exactly the framework's reversible/irreversible dichotomy applied to the specific setting of non-separability. The framework gives the criterion an algebraic home.

The answer to the second part is a qualified **not yet**. The framework expresses the criterion cleanly, and it suggests a structural reason for *why* the criterion works — the material/informational split $\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+$. But it does not yet predict anything the operational criterion does not already predict, and it does not yet specify the dynamics of the cross-sector coupling that would be needed to make the structural reason a dynamical reason. The framework sharpens the criterion; it does not extend it.

The article is organized as follows. Section 2 presents the operational criterion in the paper's own terms. Section 3 gives the criterion in the framework's language: idempotent/unitary on the two partitions. Section 4 maps the paper's four subsets (I, IIa, IIb, III) to the framework's algebra. Section 5 discusses the *fundamental versus derived* distinction that the framework suggests but the operational criterion does not require. Section 6 states what the framework adds and what remains open. Section 7 concludes.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$. The quaternion units are $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, and $i$ is the scalar imaginary. The trace of an element of $\mathbb{M}_+$ is twice its scalar part: $\mathrm{Tr}(\tilde{H}) = 2\,\mathrm{Sc}(\tilde{H})$. Two-qubit states live in $\mathbb{B}\otimes\mathbb{B} \cong M_4(\mathbb{C})$, with the tensor-product trace $\mathrm{Tr}(x\otimes y) = \mathrm{Tr}_\mathbb{B}(x)\cdot\mathrm{Tr}_\mathbb{B}(y)$.

## The Operational Criterion

The criterion of Korolkova, Sánchez-Soto, and Leuchs can be stated concisely.

Consider a bipartite non-separable state $\tilde{\rho}$ on the tensor product $\mathcal{H}_A \otimes \mathcal{H}_B$, with partitions $A$ and $B$ chosen in some physically meaningful way. The question is whether the non-separability of $\tilde{\rho}$ is quantum or classical in nature. The criterion does not look at $\tilde{\rho}$. It looks at the operations performed on the two partitions.

**Quantum entanglement.** Both partitions support **projective measurements**. A measurement is performed on partition $A$ and a measurement is performed on partition $B$. The two outcomes are correlated statistically, and the correlation function requires an ensemble of runs to be measured. The prototypical example is the singlet state with spin measurements on the two particles: two idempotents, one on each factor, joint statistics from the trace pairing.

**Classical non-separability.** Only one partition supports a projective measurement. The other partition supports a **unitary filtering, sorting, or basis-choice operation**. The correlation between the filter setting and the single measurement outcome is *deterministic* — the filter setting predetermines the outcome on the other partition, without any statistical distribution. The prototypical example is a vector light beam with transverse spatial mode correlated with polarization: the spatial-mode selection is a unitary operation (a spatial light modulator, a mode sorter), and the polarization measurement outcome is fixed by the spatial-mode choice.

The criterion is operational in the sense that it does not require any prior commitment to what the "objects" in the two partitions are, whether the partitions are spatially separated, or whether the state is "really" non-separable. It requires only that the operations performed on the two partitions be classified.

Korolkova, Sánchez-Soto, and Leuchs emphasize three consequences:

1. **Non-locality is not the criterion.** Spatial separation is neither necessary nor sufficient. The singlet of two distant particles is quantum; the local entanglement of a single 2D oscillator is also quantum; a classically non-separable light beam with a spatially extended wavefront is classical.

2. **The number of particles is not the criterion.** A single photon incident on a beam splitter produces a non-separable state whose two output modes each support a measurement (via homodyne detection), and this case is quantum. A single mass on two springs (a 2D oscillator) is mathematically equivalent to two coupled 1D oscillators, and this case is also quantum.

3. **Mathematical non-separability is not the criterion.** A vector light beam with a non-separable mode-and-polarization structure is mathematically non-separable, and it is classical. The mathematics is not what makes the difference; the operations are.

The paper maps the landscape of non-separable states into four nested subsets (their Figure 1). The outermost set is all non-separable states. Inside it, the set of states on which two measurements can be performed. Inside that, the set of states that are non-local (spatially separated partitions). Inside that, the set of states with two distinct physical objects (two excitations). The four subsets correspond to progressively stronger properties, and the paper's paradigmatic examples populate the boundaries:

- **Subset I** (two objects): two electrons in a singlet, two photons in orthogonal polarizations. Two idempotents, one per particle. Quantum.
- **Subset IIa** (one excitation, split by a beam splitter): one photon incident on a beam splitter, with the two output modes individually measurable. Two idempotents, one per output mode. Quantum.
- **Subset IIb** (one excitation in two degrees of freedom): a single 2D harmonic oscillator, or a trapped ion with internal and motional states. Two idempotents, one per degree of freedom. Quantum.
- **Subset III** (non-separable mode functions without attached excitations): a vector light beam with mode-and-polarization non-separability. Only one partition supports an idempotent; the other supports only a unitary filter. Classical.

The paper's key move is to treat the "excitation" as the decisive feature. A mode function is a frame for an excitation; it is not itself an excitation. When there are two excitations, or one excitation shared across two measurable output modes, or one excitation in two internal degrees of freedom, there are two idempotents, and the case is quantum. When there is a mode function with no attached excitation, only one idempotent is available, and the case is classical.

## The Criterion in the Biquaternion Language

The biquaternion framework has a structural feature that maps directly onto this operational criterion. Two kinds of acting element are distinguished in the algebra:

- **Unitary elements** $\tilde{U} \in \mathbb{B}$ satisfy $\tilde{U}\tilde{U}^\dagger = e_0$ and act on states by **rotor conjugation**:
$$
\tilde{\rho} \;\longmapsto\; \tilde{U}\,\tilde{\rho}\,\tilde{U}^\dagger.
$$
The action is reversible. The unitary element is a rotor in the sense of geometric algebra, and its conjugation action is the algebraic form of a basis change, a mode rotation, a filter, or a sorter.

- **Idempotent elements** $\tilde{P} \in \mathbb{M}_+$ satisfy $\tilde{P}^2 = \tilde{P}$ and act on states by the **sandwich**:
$$
\tilde{\rho} \;\longmapsto\; \tilde{P}\,\tilde{\rho}\,\tilde{P}.
$$
The action is irreversible. The idempotent is a pure-state projector, and its sandwich action is the algebraic form of a projective measurement.

In the companion articles, this dichotomy is presented as a *structural* feature of the algebra: unitary and idempotent elements are the two classes of acting elements, and the reversible/irreversible distinction is read off from the algebra rather than postulated. In the specific setting of non-separability, the dichotomy acquires a direct operational meaning.

**Quantum entanglement: two idempotents.** A bipartite state $\tilde{\rho}$ on $\mathbb{B}\otimes\mathbb{B}$ undergoes two projective measurements, one on each partition. The joint probability of outcomes $i,j$ is

$$
p(i,j) = \mathrm{Tr}\!\left(\bigl(\tilde{P}_A^{(i)}\otimes \tilde{P}_B^{(j)}\bigr)\circ \tilde{\rho}\right),
$$

where $\tilde{P}_A^{(i)}$ and $\tilde{P}_B^{(j)}$ are the idempotents corresponding to the measurement outcomes. The joint distribution is the trace pairing of the state with a **product of two idempotents**. The pattern is exactly the one used in Exercise: The CHSH Inequality and Tsirelson's Bound and Q4: the Born rule applied twice, with the joint probability being the tensor-product trace pairing of the state with the joint idempotent. The result is a **statistical correlation** between the two outcomes.

**Classical non-separability: one idempotent, one unitary.** A bipartite state $\tilde{\rho}$ on $\mathbb{B}\otimes\mathbb{B}$ undergoes one unitary filtering operation on partition $A$ and one projective measurement on partition $B$. The conditional probability of outcome $j$ given filter setting $k$ is

$$
p(j\mid k) = \mathrm{Tr}\!\left(\bigl(e_0\otimes \tilde{P}_B^{(j)}\bigr)\circ\bigl(\tilde{U}_A^{(k)}\otimes e_0\bigr)\circ \tilde{\rho}\circ\bigl(\tilde{U}_A^{(k)\dagger}\otimes e_0\bigr)\right),
$$

using the cyclicity of the trace. This is a **single trace formula**, preceded by a unitary conjugation. For the classical non-separable states of interest — those in which the excitation is not attached to either partition — the trace over partition $A$ collapses, because $\tilde{U}_A^{(k)}$ acts only on $A$ and the trace is cyclic:

$$
p(j\mid k) = \mathrm{Tr}_{\mathbb{B}}\!\left(\tilde{P}_B^{(j)}\,\tilde{\rho}_B\right), \qquad \tilde{\rho}_B = \mathrm{Tr}_A \tilde{\rho}.
$$

The conditional probability is therefore **independent of the filter setting** $k$, and it equals $1$ only when the reduced state $\tilde{\rho}_B$ is pure — which makes $\tilde{\rho}$ separable. The general formula above gives the conditional probability for any state and any pair of operations, but it does not by itself reproduce the deterministic filter-outcome correlation of the classical configuration: that correlation is a feature of the one-idempotent-one-unitary setup itself, not a consequence of this trace formula.

The distinction in the framework's notation is therefore:

$$
\text{Quantum: } \tilde{P}_A \otimes \tilde{P}_B \qquad\qquad \text{Classical: } \tilde{U}_A \otimes \tilde{P}_B.
$$

Two idempotents, or one idempotent and one unitary. The framework's reversible/irreversible dichotomy is the operational criterion, stated in the framework's native vocabulary.

This is not a coincidence. It is a structural fact of the algebra: the two kinds of acting element are distinguished by their algebraic properties ($\tilde{U}\tilde{U}^\dagger = e_0$ vs. $\tilde{P}^2 = \tilde{P}$), and their physical roles (reversible evolution vs. irreversible measurement) follow from these properties. The operational criterion of Korolkova, Sánchez-Soto, and Leuchs is thus the *physical content*, in the setting of non-separability, of an algebraic distinction that the framework already contains.

## The Four Subsets Mapped to the Framework

The paper's Figure 1 partitions non-separable states into nested subsets according to four properties: two objects, non-locality, two measurements, mathematical non-separability. The framework has a natural reading of each subset, in terms of which of the two partitions supports an idempotent measurement.

### Subset I: Two objects

Two distinct excitations, one in each partition. The joint state is a non-separable element of $\mathbb{M}_+^{(A)} \otimes \mathbb{M}_+^{(B)}$, and each factor carries its own excitation structure. Both idempotents $\tilde{P}_A^{(i)}$ and $\tilde{P}_B^{(j)}$ are physically meaningful, and the joint probability is the tensor-product trace pairing.

The prototypical examples are the two-particle singlet and the two-photon polarization singlet. In the framework, the singlet is the idempotent

$$
P_{\mathrm{singlet}} = \tfrac{1}{4}\left(e_0\otimes e_0 + e_1\otimes e_1 + e_2\otimes e_2 + e_3\otimes e_3\right),
$$

and the joint probability is the trace pairing with $\tilde{P}_A(\hat{a})\otimes \tilde{P}_B(\hat{b})$. This is the case treated in Exercise: Entanglement Entropy and the Partial Trace and Q6.

### Subset IIa: Single excitation split by a beam splitter

A single photon is incident on a beam splitter. The output state is a superposition of "photon in mode 1, vacuum in mode 2" and "vacuum in mode 1, photon in mode 2." Korolkova, Sánchez-Soto, and Leuchs emphasize that despite the single photon, both output modes carry definite excitation structure: the excited output mode contains a photon, and the other output mode contains vacuum fluctuations in a definite mode.

In the framework, both output modes are states of $\mathbb{M}_+$. The photon mode is an excited state; the vacuum mode is the ground state. Both can be acted on by idempotents in the appropriate basis. The measurement of quadratures via homodyne detection is a projective measurement on the mode's state. The framework as developed in the companion articles is finite-dimensional; the continuous-variable case requires extension, in which the projective measurements of homodyne detection correspond to the appropriate limits of idempotent operations. Two idempotents are available, one per output mode.

The framework reads this case as quantum, consistent with the resolution of the 2004 debate noted in the paper.

### Subset IIb: Single excitation in two degrees of freedom

A single 2D harmonic oscillator (one mass on two springs) is mathematically equivalent to two coupled 1D oscillators. A single trapped ion in a Schrödinger-cat-like state has internal (electronic) and external (motional) degrees of freedom. In both cases, a single physical object carries two independent excitations in its two degrees of freedom.

In the framework, the two degrees of freedom correspond to two partitions of the state space. Each partition supports its own idempotent measurement — the motion along $x$ and the motion along $y$ for the 2D oscillator; the internal electronic state and the motional state for the trapped ion. Two idempotents are available, one per partition.

The framework reads this case as quantum. The paper's point that non-locality is not required for entanglement is captured: the two partitions are two degrees of freedom of the same object, but each supports its own idempotent. This is the case of "local entanglement."

### Subset III: Non-separable mode functions without attached excitations

A vector light beam with a non-separable structure between its transverse spatial mode and its polarization. The beam has a definite excitation (the electromagnetic wave), but the excitation is not attached to either partition — it can be assigned to either partition by a choice of measurement scheme. The mode functions are frames for the excitation, not excitations themselves.

In the framework, the mode functions are **not** states of $\mathbb{M}_+$. A mode function is a frame, a basis vector, a degree of freedom; it is not an excitation, and it does not have a canonical sector assignment. A complex field configuration decomposes into a real part (in $\mathbb{M}_-$) and an imaginary part (in $\mathbb{M}_+$), but the mode function per se is a structural feature of the field, not a state of either sector.

This means only one partition supports an idempotent. The polarization mode carries the excitation, and a projective measurement on polarization is possible: an idempotent $\tilde{P}_B^{(H)}$ or $\tilde{P}_B^{(V)}$. The spatial mode does not carry an excitation, and no idempotent acts on it. The operation on the spatial mode is a unitary filter — a mode sorter, a spatial light modulator, a basis choice — which corresponds to a unitary element $\tilde{U}_A$.

The framework reads this case as classical: one idempotent, one unitary.

The paper's distinction between "mode functions" and "excitations" is thus given a natural home in the framework: an excitation is a state of $\mathbb{M}_+$; a mode function is not. The framework's split $\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+$ is the algebraic expression of the paper's observation that mode functions and excitations are different kinds of object.

## Fundamental versus Derived

The operational criterion, as Korolkova, Sánchez-Soto, and Leuchs present it, is a criterion about *operations*: count the idempotents. It does not require any commitment to the *role* of the state in the algebra. The framework suggests a refinement, which the paper's criterion does not require, and which is the place where the framework goes beyond the operational criterion.

**Quantum entanglement lives in a fundamental element.** In the quantum case, the non-separable joint state $\tilde{\rho}$ is a *fundamental* element of $\mathbb{M}_+^{(A)}\otimes \mathbb{M}_+^{(B)}$. It is the state. It is what measurements act on, and there is no deeper description of the joint system that the state is derived from. The two idempotents act directly on the state, and the joint probability is the trace pairing.

**Classical non-separability lives in a derived element.** In the classical case, the non-separable object — say, the coherence matrix $W_{ij}$ of a vector light beam — is a *derived* element of $\mathbb{M}_+^{\otimes 2}$ (after the appropriate reduction to a 2×2 problem). It is obtained as a second-order correlation of a classical field configuration:

$$
W_{ij} = \langle E_i^*\,E_j\rangle,
$$

where $E_i$ is a component of the classical field amplitude. The field configuration $E_i$ lives elsewhere in the algebra — it is a complex 3-vector, which decomposes into a real part (in $\mathbb{M}_-$) and an imaginary part (in $\mathbb{M}_+$) — and the coherence matrix is a *bilinear* summary of it.

The reason the operational criterion works — why only one idempotent is available in the classical case — is precisely this: the classical field configuration is not itself a state of $\mathbb{M}_+$ in the same sense. It carries the excitation, but the excitation is not attached to a partition. The partitions are mode decompositions of a field, and the field is the fundamental object.

In the quantum case, by contrast, the state is the fundamental object, and the two partitions carry independent excitation structures. There is no deeper field configuration from which the state is derived. The two idempotents act directly on a fundamental state of the tensor-product algebra.

So the operational criterion and the structural refinement are two faces of the same distinction:

- The **operational criterion** says: count the idempotents.
- The **structural refinement** says: the count reflects whether the non-separable element is a fundamental state of $\mathbb{M}_+^{\otimes n}$ (in which case two idempotents are available) or a derived coherence matrix of a deeper classical field configuration (in which case only one is available).

The structural refinement is not part of the paper's criterion, and the paper does not need it. But it is the framework's way of *explaining* why the criterion holds, and it is the place where the framework goes beyond the criterion as an operational prescription.

## What the Framework Adds, and What Remains Open

### What the framework adds

**1. A natural algebraic home for the criterion.** The operational criterion — count the idempotents applied to the two partitions — is the framework's reversible/irreversible dichotomy, applied to non-separable states. The framework already distinguishes unitary from idempotent acting elements for independent reasons, and the operational criterion emerges as the physical reading of this algebraic distinction in the specific setting of non-separability.

**2. A structural reason for the criterion.** The framework suggests that the count of idempotents reflects whether the non-separable element is fundamental (quantum) or derived (classical). This is not required by the operational criterion, and the criterion does not depend on it, but it gives the criterion a structural interpretation in terms of the material/informational split of the algebra.

**3. A candidate reading of "excitation" vs. "mode function."** The paper's distinction — an excitation is measurable, a mode function is a frame — is expressed in the framework as the distinction between elements of $\mathbb{M}_+$ (excitations) and elements of the general algebra $\mathbb{B}$ (mode functions and field configurations). This is a clean home for the paper's central observation.

### What remains open

**1. Specification of the admissible classical fields.** The framework does not yet specify what class of classical field configurations counts as "classical" for the purposes of the criterion. Linear electrodynamics? Monochromatic paraxial beams? Solutions of Maxwell's equations with specified boundary conditions? The criterion, as an operational prescription, does not require this. But the structural refinement — fundamental vs. derived — does, if it is to have content.

**2. Dynamics of the cross-sector coupling.** The framework does not yet specify a dynamics that couples the material sector (where classical fields live) to the informational sector (where quantum states live), beyond the standard Lorentz coupling via rotor conjugation. A genuinely new coupling would be where new physical content could reside.

**3. Empirical contact.** The framework expresses the operational criterion, and suggests a structural reason for it, but does not predict anything the operational criterion does not already predict. Until the framework produces a prediction that distinguishes it from the standard operational criterion, the framework is a refinement of the criterion's language, not an extension of its content.

**4. A dynamical question the framework makes sharper.** The operational criterion classifies a given non-separable state as quantum or classical, based on the operations available. But the framework suggests a question the criterion does not ask: can the *number of available idempotents* itself be a dynamical variable? Could a state transition from quantum to classical by the loss of an idempotent measurement channel — for example, through decoherence, through the classicalization of one partition, or through the emergence of a filter-only regime? The framework does not answer this, but the algebra makes the question well-posed in a way that the standard operational criterion does not.

## Summary

Korolkova, Sánchez-Soto, and Leuchs propose an operational criterion for the quantum–classical divide in non-separability: two idempotents is quantum, one idempotent and one unitary is classical. The biquaternion framework has a natural home for this criterion in its reversible/irreversible dichotomy — unitary elements vs. idempotent elements of the algebra — and it expresses the criterion in its native vocabulary.

Beyond expressing the criterion, the framework suggests a *structural reason* for it: the count of idempotents reflects whether the non-separable element is a fundamental state of the informational sector (quantum) or a derived coherence matrix of a deeper classical field configuration in the material sector (classical). This structural reading is not required by the operational criterion, but it is the framework's way of interpreting why the criterion holds.

The paper and the framework are complementary. The paper tells us what to look for operationally; the framework tells us where in the algebra the criterion lives. Together they sharpen the picture of the quantum–classical divide in non-separability, in a way that neither does alone. What remains open is the same open question as before: what dynamics generates the classical field configurations, and how does the cross-sector coupling work. Neither the paper nor the framework resolves that, and neither is likely to, until the framework produces an empirical prediction the standard operational criterion does not have.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{M}_-$ | Material sector (anti-Hermitian): four-vectors, classical fields |
| $\mathbb{M}_+$ | Informational sector (Hermitian): states, observables, excitations |
| $\mathbb{B}\otimes\mathbb{B}$ | Two-qubit tensor product, $\cong M_4(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\tilde{P}_A^{(i)}, \tilde{P}_B^{(j)}$ | Idempotents on partitions $A,B$ (measurements) |
| $\tilde{U}_A^{(k)}$ | Unitary on partition $A$ (filter, sorter, basis choice) |
| $p(i,j) = \mathrm{Tr}((\tilde{P}_A^{(i)}\otimes \tilde{P}_B^{(j)})\circ \tilde{\rho})$ | Joint probability, quantum case |
| $p(j\mid k) = \mathrm{Tr}((e_0\otimes \tilde{P}_B^{(j)})\circ(\tilde{U}_A^{(k)}\otimes e_0)\circ \tilde{\rho}\circ(\tilde{U}_A^{(k)\dagger}\otimes e_0))$ | Conditional probability, classical case |
| $\tilde{P}_A \otimes \tilde{P}_B$ | Quantum: two idempotents, statistical correlation |
| $\tilde{U}_A \otimes \tilde{P}_B$ | Classical: one idempotent, one unitary |
| $W_{ij} = \langle E_i^* E_j\rangle$ | Coherence matrix (derived element) |
| Fundamental element | Joint state of $\mathbb{M}_+^{\otimes n}$ (quantum) |
| Derived element | Coherence matrix from a classical field configuration (classical) |

## Further Reading

- N. Korolkova, L. Sánchez-Soto, and G. Leuchs, "An operational distinction between quantum entanglement and classical non-separability," arXiv:2405.15692 (2024), for the operational criterion developed in this article.
- R. J. C. Spreeuw, "A classical analogy of entanglement," *Foundations of Physics* **28** (1998) 361, and "Classical wave-optics analogy of quantum information processing," *Physical Review A* **63** (2001) 062302, for the original proposal of "classical entanglement."
- J. H. Eberly, X.-F. Qian, A. Al Qasimi, H. Ali, M. A. Alonso, R. Gutiérrez-Cuevas, B. J. Little, J. C. Howell, T. Malhotra, and A. N. Vamivakas, "Quantum and classical optics — emerging links," *Physica Scripta* **91** (2016) 063003, for the view that entanglement is a vector-space property.
- E. Karimi and R. W. Boyd, "Classical entanglement?" *Science* **350** (2015) 1172–1173, for the opposing view.
- A. Aiello, F. Töppel, C. Marquardt, E. Giacobino, and G. Leuchs, "Quantum-like nonseparable structures in optical beams," *New Journal of Physics* **17** (2015) 043024, for the mathematical structure of classical non-separability.
- A. Z. Khoury, "Bell-like inequality for the spin–orbit separability of a laser beam," *Physical Review A* **82** (2010) 033833, for Bell-type experiments with classically non-separable light.
- A. Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), §5-4, for the 2D harmonic oscillator example used in Subset IIb.
- The companion articles of this series: *Introduction to the Biquaternion Universe*, *Why Complexify Spacetime?*, *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, *Quantum Mechanics in Biquaternionic Form*, *The Exercise Articles of This Series*, and *Entangled Subsystems in the Biquaternion Framework: What the Reformulation Changes and What It Does Not*.

