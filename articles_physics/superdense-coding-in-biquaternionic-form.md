# __Superdense Coding in Biquaternionic Form__

## Introduction

Superdense coding is the protocol by which one qubit, sent from Alice to Bob, carries two classical bits, provided the two parties share a maximally entangled pair beforehand. It is the operational proof that entanglement is a resource for classical communication: a single qubit can transmit at most one bit on its own, and the shared entanglement doubles that. The protocol is the dual of quantum teleportation, which uses two classical bits and a shared entangled pair to transmit one qubit.

In the biquaternion framework the protocol has an exceptionally clean form. The shared resource is a Bell state, i.e. one of the four Bell idempotents $\tilde\Pi_\epsilon$ that form an idempotent basis of the two-qubit algebra $\mathbb{B}\otimes\mathbb{B}$, as fixed by the companion article *The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$*. Alice's encoding is a **local operation on one factor**, and the four available operations are conjugation by the four unit quaternions $e_t,\vec e_x,\vec e_y,\vec e_z$ — the Pauli operations $I,\sigma_1,\sigma_2,\sigma_3$ under the series identification $i\vec e_k\leftrightarrow\sigma_k$, the central phase in which the two differ cancelling in conjugation — acting on her half of the pair. These four operations permute the four Bell idempotents, so the encoded state is again one of the four Bell states, and the codewords are **orthogonal**. Bob's decoding is the Bell measurement, i.e. the joint measurement of the commuting stabilizers $S_1 = -\vec e_x\otimes \vec e_x$ and $S_3 = -\vec e_z\otimes \vec e_z$, which distinguishes the four orthogonal codewords perfectly. The two classical bits are thus the four elements of the encoding group, and the algebra's Bell idempotent basis is both the message alphabet and the decoding basis.

This article develops the protocol in that language: the resource, the encoding as conjugation by the unit quaternions, the decoding as the joint stabilizer measurement, and the explicit permutation of the Bell states produced by each operation. The channel-capacity statement — that without entanglement the qubit carries at most $\log 2 = 1$ bit, while with the shared pair it carries $2$ bits — is recalled as the Holevo bound and its entanglement-assisted generalization. Every algebraic step is verified by recomputation: the four encoded states are computed explicitly and found to be orthogonal, and the permutation is tabulated.

## The Resource

### The Bell idempotent basis

The two-qubit algebra $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$ carries four Bell idempotents

$$
\tilde\Pi_\epsilon = \tfrac{1}{4}\bigl(e_t\otimes e_t + \epsilon_1\,\vec e_x\otimes \vec e_x + \epsilon_2\,\vec e_y\otimes \vec e_y + \epsilon_3\,\vec e_z\otimes \vec e_z\bigr),
\qquad \epsilon_j = \pm1, \quad \epsilon_1\epsilon_2\epsilon_3 = +1 ,
$$

which satisfy $\tilde\Pi_\epsilon \tilde\Pi_{\epsilon'} = \delta_{\epsilon\epsilon'}\tilde\Pi_\epsilon$ and $\sum_\epsilon \tilde\Pi_\epsilon = e_t\otimes e_t$. They are the joint spectral idempotents of the commuting stabilizers

$$
S_1 = -\vec e_x\otimes \vec e_x, \qquad S_3 = -\vec e_z\otimes \vec e_z,
\qquad
S_1\tilde\Pi_\epsilon = -\epsilon_1\tilde\Pi_\epsilon, \qquad S_3\tilde\Pi_\epsilon = -\epsilon_3\tilde\Pi_\epsilon .
$$

The four idempotents correspond to the four Bell states

$$
|\Psi^-\rangle,\quad |\Phi^+\rangle,\quad |\Phi^-\rangle,\quad |\Psi^+\rangle
$$

according to the sign pattern $\epsilon$; the companion article fixes the correspondence. The resource shared by Alice and Bob is one of these, conventionally $\tilde\Pi_{\Phi^+}$.

### The resource as an element of the algebra

The state $\tilde\Pi_{\Phi^+}$ has the following properties, all used in the protocol:

- it is **pure**, $\tilde\Pi_{\Phi^+}^2 = \tilde\Pi_{\Phi^+}$, and positive, with trace one;
- it is **maximally entangled**: its partial traces are both maximally mixed, $\mathrm{Tr}_B \tilde\Pi_{\Phi^+} = \mathrm{Tr}_A \tilde\Pi_{\Phi^+} = \tfrac12 e_t$;
- it is a **maximal-uncertainty** state with respect to every local basis: the reduced state of either qubit alone carries no information, $\mathrm{Tr}(\tilde\Pi(\vec u)\,\mathrm{Tr}_B \tilde\Pi_{\Phi^+}) = \tfrac12$ for every direction $\vec u$.

The last property is what makes the protocol worth performing: **Alice's half, on its own, contains no information about anything**, so all the transmitted information must be created by her local operation and revealed only by Bob's joint measurement. This is the operational meaning of maximal entanglement in the algebra.

## Encoding by Local Conjugation

### The four operations

Alice acts on her factor with a local unitary. The available unitaries are the unit quaternions and their central multiples; since a central phase cancels in conjugation, the distinct operations are the four coset representatives

$$
e_t,\ \vec e_x,\ \vec e_y,\ \vec e_z \in Q_8/\{\pm e_t\} \cong \mathbb{Z}_2\times\mathbb{Z}_2 ,
\qquad
\text{mapping to } I,\ -i\sigma_1,\ -i\sigma_2,\ -i\sigma_3 .
$$

Each is unitary, $\vec e_k\,\vec e_k^{*} = \vec e_k(-\vec e_k) = e_t$, and Hermitian up to the central $i$; each acts on the state by

$$
\tilde{Ϛ} = \tilde\Pi_{\Phi^+} \ \longmapsto\ (\vec e_k\otimes e_t)\,\tilde{Ϛ}\,(\vec e_k\otimes e_t)^{*} .
$$

Because $\vec e_k$ is a unit quaternion, the map is an inner automorphism of the first factor tensored with the identity on the second: it is a **local unitary of the algebra**, and it preserves the spectrum, the trace, and the idempotency of the state.

### The permutation of the Bell basis

Conjugation by $\vec e_k\otimes e_t$ permutes the four Bell idempotents. Explicit computation gives


| $\text{operation}$ | $\text{state received by Bob}$ |
|---|---|
| $e_t\ \ (I)$ | $\tilde\Pi_{\Phi^+}$ |
| $\vec e_x\ \ (\sigma_1)$ | $\tilde\Pi_{\Psi^+}$ |
| $\vec e_y\ \ (\sigma_2)$ | $\tilde\Pi_{\Psi^-}$ |
| $\vec e_z\ \ (\sigma_3)$ | $\tilde\Pi_{\Phi^-}$ |


so that the four operations produce the four distinct Bell states, one for each. The map $k\mapsto$ (Bell state) is a bijection of the four-element encoding set onto the four-element Bell basis: the encoding is the **regular action** of the Klein four-group on its own elements, a sharply transitive abelian group of permutations. Each operation acts as an involution, since conjugation by $\vec e_k$ twice is conjugation by the central element $\vec e_k^2 = -e_t$, which is trivial; the codeword is the group element Alice applied.

### Orthogonality of the codewords

The crucial property for decoding is that the four codewords are mutually orthogonal:

$$
\mathrm{Tr}\bigl(\tilde\Pi_{\Phi^+}\tilde\Pi_{\Psi^+}\bigr) = \mathrm{Tr}\bigl(\tilde\Pi_{\Phi^+}\tilde\Pi_{\Psi^-}\bigr) = \mathrm{Tr}\bigl(\tilde\Pi_{\Phi^+}\tilde\Pi_{\Phi^-}\bigr) = 0,
$$

and likewise among all pairs, with the diagonal equal to one. Orthogonal states are perfectly distinguishable, so a single measurement on Bob's two qubits can identify the codeword with certainty. This is why the protocol transmits two bits and not merely one: the four codewords live in a four-dimensional space and are orthogonal there, while any four states confined to a single qubit could not be.

**Why conjugation preserves the idempotent structure.** The operation $\vec e_k\otimes e_t$ is unitary and, on each factor, multiplicative; conjugating an idempotent by a unitary returns an idempotent of the same rank, because

$$
\bigl(U\tilde\Pi U^{*}\bigr)^2 = U\tilde\Pi U^{*} U\tilde\Pi U^{*} = U\tilde\Pi^2U^\dagger = U\tilde\Pi U^{*},
\qquad
\mathrm{Tr}\bigl(U\tilde\Pi U^{*}\bigr) = \mathrm{Tr}(\tilde\Pi) = 1 .
$$

Hence the image of $\tilde\Pi_{\Phi^+}$ is again a rank-one idempotent, i.e. again a pure state, and since the local unitary preserves the algebra it maps the Bell basis into itself. The four images $\vec e_k\otimes e_t$ acting on the resource exhaust the Bell idempotents because the conjugation action of the group $Q_8/\{\pm e_t\}\cong\mathbb{Z}_2\times\mathbb{Z}_2$ on the four-element Bell basis is transitive: the stabilizer of any Bell idempotent in this action is trivial, so the orbit has four elements, one for each coset. This is the algebraic reason no fifth codeword is available and no third bit can be sent: the orbit of the resource under the local group has exactly four elements.

## Decoding

### The Bell measurement

Bob, holding both qubits, measures the commuting stabilizers $S_1$ and $S_3$. Since $\{S_1,S_3\}$ is a complete set of commuting observables with the four Bell idempotents as its joint eigenbasis, the measurement has four outcomes $\epsilon$ with probabilities

$$
p_\epsilon = \mathrm{Tr}\bigl(\tilde{Ϛ}\,\tilde\Pi_\epsilon\bigr),
$$

where $\tilde{Ϛ}$ is the received state. If Alice applied $\vec e_k$, then $\tilde{Ϛ} = \tilde\Pi_{\epsilon(k)}$ for the corresponding sign pattern $\epsilon(k)$, and

$$
p_\epsilon = \delta_{\epsilon,\epsilon(k)} ,
$$

so the outcome identifies the operation with certainty. Bob recovers two bits: the pair of eigenvalues of $S_1$ and $S_3$, or equivalently the Klein-group element Alice applied.

### Why the measurement can be joint

The measurement is a joint measurement on the two-qubit module. It is not a pair of local measurements, and it could not be: no local measurement on either qubit alone can distinguish the Bell states, because the reduced states are all maximally mixed, $\mathrm{Tr}_B \tilde\Pi_\epsilon = \mathrm{Tr}_A \tilde\Pi_\epsilon = \tfrac12 e_t$. The information is stored entirely in the **correlations**, which are accessible only to a joint measurement. This is the operational content of maximal entanglement in the framework: the local reductions are informationless, and the whole message lives in the tensor structure.

## Why Entanglement Helps

Without shared entanglement, the classical information that one qubit can carry is bounded by the Holevo quantity of the ensemble Alice prepares, and for a single qubit this is at most

$$
\log_2 2 = 1 \ \text{bit} .
$$

Superdense coding transmits two bits per qubit, so the shared pair has doubled the capacity. The general statement is that the **entanglement-assisted classical capacity** of a noiseless qubit channel is

$$
C_E = 2 \log_2 2 = 2 \ \text{bits per channel use},
$$

the maximum being attained by the protocol above. Two features of this statement belong in the framework's terms.

- The resource is the **maximally entangled idempotent** $\tilde\Pi_{\Phi^+}$, whose reduced states are maximally mixed. A less entangled resource gives less; a product state gives no advantage, and then the capacity reduces to the Holevo bound of one bit.
- The resource is **consumed**. After one use of the protocol Alice's qubit has been transmitted and both halves of the pair are in Bob's possession, so no entanglement remains distributed between the two parties; a fresh Bell pair must be shared before the protocol can be run again. The protocol uses up one ebit per two bits transmitted.

### The one-bit ceiling without the resource

For a single qubit the ceiling follows directly from the Holevo quantity. If Alice prepares an ensemble $\{p_x,\tilde{Ϛ}_x\}$ on one qubit, the accessible information is bounded by

$$
\chi = S\Bigl(\sum_x p_x\tilde{Ϛ}_x\Bigr) - \sum_x p_x\,S(\tilde{Ϛ}_x) \ \leq\ S\Bigl(\sum_x p_x\tilde{Ϛ}_x\Bigr) \ \leq\ \log_2 2 = 1 \ \text{bit},
$$

because the von Neumann entropy of a qubit is at most one bit; for an ensemble of pure states the first inequality is an equality and the bound is $\chi = S(\tilde{Ϛ})\leq 1$. The reason is the dimension of the module: a qubit's defining module has complex dimension two, and at most two orthogonal rays can be accommodated, so at most one bit of perfectly distinguishable signal can be carried. With the shared pair, Bob's decoding space is the tensor-product module of dimension four, which holds four orthogonal codewords, hence two bits. The gain from entanglement is one bit, and it is exactly the logarithm of the ratio of the two module dimensions:

$$
2\ \text{bits} - 1\ \text{bit} = \log_2 4 - \log_2 2 = 1\ \text{bit}.
$$

This is the informational content of the protocol: the shared entanglement supplies the second qubit at the decoder, converting a two-dimensional module into a four-dimensional one, and the four Bell idempotents are the orthogonal basis that fills it.

The capacity formula is standard (the Bennett–Shor–Smolin–Thapliyal formula and the superdense coding theorem of Bennett and Wiesner). The framework transcribes the protocol; it does not change the numbers.

## Explicit Verification

All the algebraic claims above were verified by direct computation in the tensor-product algebra.

**The four encoded states.** Starting from the Bell idempotent $\tilde\Pi_{\Phi^+}$ and conjugating by $e_t\otimes e_t$, $\vec e_x\otimes e_t$, $\vec e_y\otimes e_t$, $\vec e_z\otimes e_t$, the four resulting states were computed as $4\times4$ matrices and identified by their overlaps with the four Bell states. The results are exactly the table above: $e_t\to|\Phi^+\rangle$, $\vec e_x\to|\Psi^+\rangle$, $\vec e_y\to|\Psi^-\rangle$, $\vec e_z\to|\Phi^-\rangle$, each with overlap one and zero overlap with the other three.

**Orthogonality.** The pairwise overlaps of the four encoded states were computed and found to be $\delta_{\epsilon\epsilon'}$: the codewords are orthogonal, and the Bell measurement distinguishes them with probability one.

**The spectrum and the marginal.** Each encoded state has the spectrum of an idempotent, $(1,0,0,0)$, and partial trace $\tfrac12 e_t$ on both factors, confirming that the encoding preserves purity and maximal entanglement and that no local measurement can read the message.

**The capacity arithmetic.** The encoding set has four elements, so the message is $\log_2 4 = 2$ bits, while a single qubit without entanglement is bounded by $\log_2 2 = 1$ bit; the doubling is the algebraic statement that the four codewords are orthogonal vectors in a four-dimensional module rather than in a two-dimensional one.

## Duality with Teleportation

Superdense coding and quantum teleportation are exact duals, and the framework makes the duality a statement about the exchange of resources.

- **Superdense coding:** a shared Bell pair plus **one qubit** sent from Alice to Bob yields **two classical bits**. The protocol consumes one ebit of distributed entanglement and transmits one qubit.
- **Teleportation:** a shared Bell pair plus **two classical bits** sent from Alice to Bob yields **one qubit**, in Bob's hands. The protocol likewise consumes one ebit and transmits two bits.

The two protocols exchange the roles of the qubit and the pair of bits, and both are driven by the same algebraic mechanism: the Bell idempotent basis and the local action of the unit quaternions. In teleportation the encoding is Alice's Bell measurement, whose four outcomes she sends classically, and the decoding is a local operation conditioned on the two bits; in superdense coding the encoding is a local operation whose label is the message, and the decoding is the Bell measurement. The companion article *Quantum Teleportation in Biquaternionic Form* develops the first; the present article is its mirror image.

The duality is usually stated as the identity

$$
\text{one ebit} + \text{one qubit} \ \longleftrightarrow\ \text{two cbits},
$$

read in the two directions. It is a statement about the tensor-product algebra: the Bell measurement and the local unitary encoding are dual processes, both built from the idempotent basis $\{\tilde\Pi_\epsilon\}$ and the group of local unitaries acting on it.

## What the Framework Adds and What It Does Not

**What it does.**

- It identifies the shared resource with a Bell idempotent of the two-qubit algebra and states its maximal entanglement as the maximal mixedness of both partial traces.
- It identifies the encoding operations with conjugation by the four coset representatives $e_t,\vec e_x,\vec e_y,\vec e_z$ of $Q_8/\{\pm e_t\}$, i.e. with the local unitaries built from the imaginary units.
- It shows that the encoding is the regular action of the Klein four-group on the Bell idempotent basis, so the message is the group element and the codewords are the basis elements.
- It identifies the decoding with the joint measurement of the commuting stabilizers $S_1,S_3$, and shows that the codewords are orthogonal and hence perfectly distinguishable.
- It verifies the whole protocol explicitly in the tensor-product algebra.

**What it does not.**

- It does not derive the entanglement-assisted capacity formula; the values $1$ bit and $2$ bits are the standard Holevo and Bennett–Shor–Smolin–Thapliyal results, cited.
- It does not treat noisy channels, channel coding, or the multiplicity of uses; only the single-use noiseless protocol is developed.
- It does not construct the physical Bell measurement or the experimental realization; the measurement is specified algebraically as the joint stabilizer measurement.
- It does not predict anything beyond standard quantum information theory.

## Open Questions

**1. The encoding group in higher dimensions.** For a qudit the encoding group is larger and the codewords form an orthonormal basis of the composite. In the framework, is the encoding for $n$ qubits the action of a finite group — a Weyl–Heisenberg group in the Pauli/tensor structure — on an idempotent basis of $\mathbb{B}^{\otimes n}$?

**2. The resource and the biquaternion norm.** The Bell idempotent has the property that both its reduced states are maximally mixed, which is a statement about the partial traces rather than about the biquaternion norm. Is there an algebraic invariant of $\mathbb{M}_+^{\otimes2}$ that quantifies "how much" entanglement is available as a resource, and how does it relate to the biquaternion norm of the two-qubit state?

**3. Duality with teleportation.** Superdense coding and teleportation are duals: one exchanges a qubit for two bits, the other two bits for a qubit, both using a Bell pair. Is there a single algebraic statement — a kind of channel duality on $\mathbb{B}\otimes\mathbb{B}$ — from which both protocols follow?

**4. The role of the two sectors.** The protocol uses only $\mathbb{M}_+^{\otimes2}$. Does the material sector $\mathbb{M}_-$ play any role in the resource theory of entanglement, or is it inert for communication tasks?

**5. Empirical content.** Superdense coding is standard and experimentally realized; the framework reproduces it and adds no prediction.

## Summary

Superdense coding transmits two classical bits by sending one qubit, given a shared maximally entangled pair. In the biquaternion framework the resource is a Bell idempotent $\tilde\Pi_{\Phi^+}$ of the two-qubit algebra $\mathbb{B}\otimes\mathbb{B}$, whose partial traces are both maximally mixed; the encoding is conjugation on one factor by the four unit quaternions $e_t,\vec e_x,\vec e_y,\vec e_z$, i.e. by the Pauli operations $I,\sigma_1,\sigma_2,\sigma_3$ up to central phase, which permute the four Bell idempotents as

$$
e_t \to \tilde\Pi_{\Phi^+}, \quad \vec e_x \to \tilde\Pi_{\Psi^+}, \quad \vec e_y \to \tilde\Pi_{\Psi^-}, \quad \vec e_z \to \tilde\Pi_{\Phi^-} ;
$$

and the decoding is the joint measurement of the commuting stabilizers $S_1 = -\vec e_x\otimes \vec e_x$ and $S_3 = -\vec e_z\otimes \vec e_z$, whose joint eigenbasis is the Bell basis. The four codewords are mutually orthogonal, $\mathrm{Tr}(\tilde\Pi_\epsilon \tilde\Pi_{\epsilon'}) = \delta_{\epsilon\epsilon'}$, so the measurement identifies the message with certainty, and the encoding set has four elements, giving $\log_2 4 = 2$ bits. Without the shared entanglement a qubit carries at most $\log_2 2 = 1$ bit (the Holevo bound); the pair doubles the capacity, the entanglement-assisted capacity of the noiseless qubit channel being $2$ bits, and the resource is consumed in the process. The protocol is the algebraic statement that the encoding group acts regularly on the Bell idempotent basis; it is the dual of quantum teleportation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$ | Two-qubit algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion units; unit quaternions act as local unitaries |
| $i$ | Central scalar imaginary |
| $\tilde\Pi_\epsilon$ | Bell idempotents (idempotent basis) |
| $\tilde\Pi_{\Phi^+}$ | Shared resource (maximally entangled) |
| $\epsilon = (\epsilon_1,\epsilon_2,\epsilon_3)$, $\epsilon_1\epsilon_2\epsilon_3=+1$ | Bell sign pattern |
| $S_1 = -\vec e_x\otimes \vec e_x$, $S_3 = -\vec e_z\otimes \vec e_z$ | Stabilizer observables (decoding) |
| $S_1\tilde\Pi_\epsilon = -\epsilon_1\tilde\Pi_\epsilon$, $S_3\tilde\Pi_\epsilon=-\epsilon_3\tilde\Pi_\epsilon$ | Joint eigenvalues |
| $(\vec e_k\otimes e_t)\tilde{Ϛ}(\vec e_k\otimes e_t)^{*}$ | Local encoding operation |
| $\mathrm{Tr}(\tilde\Pi_\epsilon \tilde\Pi_{\epsilon'}) = \delta_{\epsilon\epsilon'}$ | Orthogonality of codewords |
| $p_\epsilon = \mathrm{Tr}(\tilde{Ϛ}\tilde\Pi_\epsilon)$ | Decoding probabilities (Born rule) |
| $1$ bit | Holevo bound for one qubit without entanglement |
| $2$ bits | Entanglement-assisted capacity (superdense coding) |

## Further Reading

- C. H. Bennett and S. J. Wiesner, "Communication via one- and two-particle operators on Einstein–Podolsky–Rosen states," *Physical Review Letters* **69** (1992) 2881–2884, for the superdense coding protocol.
- C. H. Bennett, P. W. Shor, J. A. Smolin, and A. V. Thapliyal, "Entanglement-assisted capacity of a quantum channel and the reverse Shannon theorem," *IEEE Transactions on Information Theory* **48** (2002) 2637–2655, for the entanglement-assisted classical capacity.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the protocol, the Bell basis, and the Holevo bound.
- K. Mattle, H. Weinfurter, P. G. Kwiat, and A. Zeilinger, "Dense coding in experimental quantum communication," *Physical Review Letters* **76** (1996) 4656–4659, for the experimental realization.
- C. H. Bennett, G. Brassard, C. Crépeau, R. Jozsa, A. Peres, and W. K. Wootters, "Teleporting an unknown quantum state via dual classical and Einstein–Podolsky–Rosen channels," *Physical Review Letters* **70** (1993) 1895–1899, for the dual protocol.
- A. Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), for joint measurements and the Bell basis.
- The companion articles of this series: *The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$*, *Quantum Teleportation in Biquaternionic Form*, *Quantum Gates and Circuits in Biquaternionic Form*, and *Entangled Subsystems in the Biquaternion Framework*.
