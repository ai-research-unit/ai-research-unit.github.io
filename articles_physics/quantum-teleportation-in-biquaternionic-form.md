# __Quantum Teleportation in Biquaternionic Form__

## Introduction

**Quantum teleportation** is the transmission of an unknown quantum state from one party to another using a pre-shared entangled state and two bits of classical communication. Alice holds the unknown qubit; she and Bob share an entangled pair, one half each. Alice measures her unknown qubit jointly with her half of the pair, in the basis of the four maximally entangled two-qubit states. Each of the four outcomes leaves Bob's half of the pair in one of four *unitary images* of the unknown state. Alice announces the outcome — two classical bits — and Bob applies the matching unitary correction. He then holds the unknown state exactly, and no copy of it exists anywhere: Alice's measurement has destroyed the original.

This article writes that protocol in the biquaternion language of the companion articles. The protocol is worth writing out because it is the one place in the framework where four of its constructions meet at once, and where the difference between them is forced into the open:

- the **state** is a positive element $\tilde{Ϛ}$ of the Hermitian subspace $\mathbb{M}_+\subset\mathbb{B}$, normalised by $\langle\tilde{Ϛ},e_t\rangle_{*}=\tfrac12$ (trace one in the $2\times2$ image);
- the **entangled resource** is a Bell idempotent $\tilde\Pi_{\epsilon}$ of the tensor square $\mathbb{B}\otimes\mathbb{B}$ — idempotent and Hermitian, but *not* unitary;
- the **Bell measurement** is the four-outcome projective measurement whose projectors correspond to those same idempotents on the pair;
- the **corrections** are unitary elements of $\mathbb{B}$ — gates, in the sense of the companion article on gates and circuits — and they are *not* idempotents.

The protocol is therefore a controlled collision between two kinds of object that the framework elsewhere keeps apart: the idempotents that resolve a measurement, and the unitaries that generate reversible motion. The distinction does real work in the correction table, where the same elements $\vec e_x,\vec e_y,\vec e_z$ enter the resource idempotent as $\vec e_k\otimes \vec e_k$ and the correction gates as $i\vec e_k$, and the two kinds of object behave quite differently.

**Established, and recomputed below.** The shared Bell idempotent $\tilde\Pi_{\Phi^+}$ resolves the initial three-qubit state into four orthogonal branches, one per Bell outcome; each branch is the product of the outcome idempotent with a single conjugation of the unknown state; each outcome occurs with probability $\tfrac14$; and the correction equal to the (Hermitian, involutive) Pauli gate $\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$ restores the state exactly. Averaged over the outcomes without the classical record, Bob's qubit is the maximally mixed state $\tfrac12 e_t$ — the protocol transfers nothing on its own — and with the record and the correction the net state map on the teleported qubit is the identity channel, a gate of Kraus rank one, realised through a measurement of Kraus rank four. Alice's qubit is left maximally mixed, so no copy survives. Each of the four identities was recomputed separately, on input states other than the $\Phi^+$ case that fixes the labelling.

**Gap, left visible.** The two classical bits are *not* an element of the algebra. The algebra represents the outcome label — the joint eigenvalue of the stabiliser observables — and it represents the conditional correction; it does not contain the arithmetic by which the label reaches Bob. The protocol is a statement about the algebra *plus* a classical channel, and the classical channel is where the non-algebraic step sits. The status of the tensor-product arena $\mathbb{B}\otimes\mathbb{B}$ is the open question inherited from the companion articles and is not resolved here.

The article is organised as follows. The next section fixes the three-qubit arena and says which algebra each object of the protocol lives in. The section after that fixes the resource and the measurement. The following section proves the teleportation identity, first as a vector identity and then as the projected operator identity that gives the probabilities and Bob's state. The next section reads off the four corrections and records them in terms of the stabiliser observables. Two shorter sections treat no-signalling and the channel-theoretic interpretation of the protocol. The article closes with what the reformulation does and does not claim, and with open questions.

## The Three-Qubit Arena and the Objects of the Protocol

Three qubits are involved, and it matters which is which:

- qubit $1$ is Alice's unknown qubit, in the state $\tilde{Ϛ}_\psi$;
- qubits $2$ and $3$ carry the shared Bell idempotent $\tilde\Pi_{\Phi^+}$, qubit $2$ with Alice, qubit $3$ with Bob;
- the Bell measurement acts on qubits $1$ and $2$;
- the correction acts on qubit $3$ alone.

The arena is therefore $\mathbb{B}^{\otimes3}\cong M_8(\mathbb{C})$, with the trace the product of the factor traces, $\mathrm{Tr}(x\otimes y\otimes z)=\mathrm{Tr}_\mathbb{B}(x)\mathrm{Tr}_\mathbb{B}(y)\mathrm{Tr}_\mathbb{B}(z)$. The unknown state is written

$$
\tilde{Ϛ}_\psi=\tfrac12\left(e_t+i\vec r\right),
\qquad
\vec r=\sum_{k=1}^{3}r_k\,\vec e_k,\qquad |\vec r|\leq 1 ,
$$

with $|\vec r|=1$ exactly when the state is pure and $\vec r=0$ when it is maximally mixed. The initial three-qubit state is the single element

$$
\tilde{Ϛ}^{(0)}=\tilde{Ϛ}_\psi^{(1)}\otimes \tilde\Pi_{\Phi^+}^{(23)}\in\mathbb{M}_+\otimes\mathbb{M}_+\otimes\mathbb{M}_+ ,
\qquad
\mathrm{Tr}\left(\tilde{Ϛ}^{(0)}\right)=1\cdot 1=1 ,
$$

where the superscripts record which factor each element occupies.

It is worth stating explicitly which algebra each object belongs to, because the protocol puts them side by side and they are not interchangeable.

| Object | Algebra | Algebraic type |
|---|---|---|
| $\tilde{Ϛ}_\psi$ | $\mathbb{B}$ | Hermitian, positive, $\langle\tilde{Ϛ},e_t\rangle_{*}=\tfrac12$ (trace one in the image); $\mathbb{M}_+$ |
| $\tilde\Pi_{\Phi^+}$, $\tilde\Pi_\epsilon$ | $\mathbb{B}\otimes\mathbb{B}$ | Hermitian idempotent of trace one; $\mathbb{M}_+\otimes\mathbb{M}_+$ |
| $S_1,S_3$ | $\mathbb{B}\otimes\mathbb{B}$ | Hermitian involutions; $\mathbb{M}_+\otimes\mathbb{M}_+$ |
| $\tilde\Pi_\epsilon\otimes e_t$ | $\mathbb{B}^{\otimes3}$ | Hermitian idempotent on factors $(1,2)$ |
| $\tilde U_\epsilon$ | $\mathbb{B}$ | Unitary (Hermitian Pauli); a gate |
| the classical record | — | two bits, not an element of any of the above |

Two distinctions in the table do the work of the whole article. First, the resource $\tilde\Pi_{\Phi^+}$ and the idempotents of the measurement $\tilde\Pi_\epsilon\otimes e_t$ are **idempotent** and **not unitary**: $\tilde\Pi_\epsilon^{*}\tilde\Pi_\epsilon=\tilde\Pi_\epsilon\neq e_t\otimes e_t$ on the pair (and $\tilde\Pi_\epsilon^{(12)}\neq e_t\otimes e_t\otimes e_t$ on three factors). They are the objects that resolve a measurement, and they are trace-one, not unimodular. Second, the corrections $\tilde U_\epsilon$ are **unitary** and **not idempotent** (except for the identity): they are gates, and their conjugation action is reversible. The tensor square $\mathbb{B}\otimes\mathbb{B}$ is a matrix algebra, not a division algebra; it contains idempotents and zero divisors, and an element of $\mathbb{B}\otimes\mathbb{B}$ is not a state of a single qubit. The protocol is written below so that each line says which of these types is being used.

## The Resource and the Bell Measurement

**The resource.** The shared pair is the Bell idempotent of $|\Phi^+\rangle_{*}$,

$$
\tilde\Pi_{\Phi^+}=\tfrac14\left(e_t\otimes e_t-\vec e_x\otimes \vec e_x+\vec e_y\otimes \vec e_y-\vec e_z\otimes \vec e_z\right),
\qquad \epsilon=(-1,+1,-1),
$$

an element of $\mathbb{M}_+\otimes\mathbb{M}_+$ with $\tilde\Pi_{\Phi^+}^2=\tilde\Pi_{\Phi^+}$, $\tilde\Pi_{\Phi^+}^{*}=\tilde\Pi_{\Phi^+}$ and $\mathrm{Tr}(\tilde\Pi_{\Phi^+})=1$. Its defining property for the protocol is that both its partial traces are maximally mixed, $\mathrm{Tr}_1(\tilde\Pi_{\Phi^+})=\mathrm{Tr}_2(\tilde\Pi_{\Phi^+})=\tfrac12 e_t$: neither party, holding one half, has any local information about the pair. This is the same idempotent that the companion article on the Bell basis singles out as a member of the Bell idempotent basis, and the same one that the companion article on gates and circuits produces from $|00\rangle$ by a Hadamard and a CNOT.

**The measurement.** Alice measures the pair $(1,2)$ in the Bell basis, that is, she measures the four projectors

$$
\tilde\Pi_\epsilon^{(12)}=\tilde\Pi_\epsilon\otimes e_t^{(3)},
\qquad \epsilon\in\{\Phi^+,\Phi^-,\Psi^+,\Psi^-\} ,
$$

where $\tilde\Pi_\epsilon$ is the Bell idempotent on factors $(1,2)$ and $e_t$ acts as the identity on Bob's qubit. The four projectors inherit from the Bell idempotent basis the four properties that make them a projective measurement:

$$
\left(\tilde\Pi_\epsilon^{(12)}\right)^2=\tilde\Pi_\epsilon^{(12)},\qquad
\left(\tilde\Pi_\epsilon^{(12)}\right)^{*}=\tilde\Pi_\epsilon^{(12)},\qquad
\tilde\Pi_\epsilon^{(12)}\tilde\Pi_{\epsilon_2}^{(12)}=\delta_{\epsilon\epsilon_2}\tilde\Pi_\epsilon^{(12)},\qquad
\sum_\epsilon \tilde\Pi_\epsilon^{(12)}=e_t\otimes e_t\otimes e_t .
$$

Equivalently, and this is the form in which the outcome label is read, the measurement is the joint measurement of the two commuting Hermitian involutions $S_1^{(12)}=-\vec e_x\otimes \vec e_x\otimes e_t$ and $S_3^{(12)}=-\vec e_z\otimes \vec e_z\otimes e_t$. Their joint eigen-idempotents are the projectors, with

$$
S_1^{(12)}\tilde\Pi_\epsilon^{(12)}=-\epsilon_1\tilde\Pi_\epsilon^{(12)},\qquad
S_3^{(12)}\tilde\Pi_\epsilon^{(12)}=-\epsilon_3\tilde\Pi_\epsilon^{(12)} .
$$

The outcome label can therefore be recorded either as the Bell sign pattern $\epsilon=(\epsilon_1,\epsilon_2,\epsilon_3)$ or, equivalently, as the pair of stabiliser eigenvalues

$$
(s_1,s_3)=(-\epsilon_1,-\epsilon_3)\in\{\pm1\}^2 .
$$

Both labels are used below. Note again the type: $S_1,S_3$ are Hermitian **observables** (and involutions, hence also unitary), while the projectors onto their joint eigenspaces are Hermitian idempotent operators and not unitary. It is the projectors, not the observables, that enter the protocol's projection step.

## The Teleportation Identity

### The Bell decomposition of the resource

The whole protocol rests on one algebraic fact, which says how the shared resource factors when the unknown qubit is grouped with Alice's half of the pair.

**Lemma (Bell decomposition).** Let $|\psi\rangle_1$ be any single-qubit vector and let $|\Phi^+\rangle_{23}$ be the shared pair. Then

$$
|\psi\rangle_1|\Phi^+\rangle_{23}
=\tfrac12\Bigl[\,|\Phi^+\rangle_{12}|\psi\rangle_3
+|\Phi^-\rangle_{12}\,Z|\psi\rangle_3
+|\Psi^+\rangle_{12}\,X|\psi\rangle_3
+|\Psi^-\rangle_{12}\,(XZ)|\psi\rangle_3\,\Bigr] .
$$

*Proof.* Write $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$ and expand the left-hand side in the computational basis:

$$
|\psi\rangle_1|\Phi^+\rangle_{23}
=\tfrac{1}{\sqrt2}\Bigl(\alpha|000\rangle+\alpha|011\rangle+\beta|100\rangle+\beta|111\rangle\Bigr).
$$

Grouping the first two tensor slots and projecting onto the four Bell vectors of the pair $(1,2)$ gives the four coefficients

$$
|\Phi^+\rangle_{12}:\ \tfrac12\left(\alpha|0\rangle+\beta|1\rangle\right)=\tfrac12|\psi\rangle_3,
\qquad
|\Phi^-\rangle_{12}:\ \tfrac12\left(\alpha|0\rangle-\beta|1\rangle\right)=\tfrac12 Z|\psi\rangle_3,
$$

$$
|\Psi^+\rangle_{12}:\ \tfrac12\left(\beta|0\rangle+\alpha|1\rangle\right)=\tfrac12 X|\psi\rangle_3,
\qquad
|\Psi^-\rangle_{12}:\ \tfrac12\left(\alpha|1\rangle-\beta|0\rangle\right)=\tfrac12 (XZ)|\psi\rangle_3 .
$$

Collecting the four terms gives the stated identity.

The four operators appearing on the right are the Pauli gates $I,X,Z,XZ$, and in biquaternion representatives (companion article on gates and circuits) they are

$$
I\leftrightarrow e_t,\qquad
X\leftrightarrow i\vec e_x,\qquad
Z\leftrightarrow i\vec e_z,\qquad
XZ\leftrightarrow \vec e_y\sim i\vec e_y.
$$
The last equivalence is a statement about **gates**, not about elements: $\vec e_y$ and $i\vec e_y$ differ by the central phase $-i$, which cancels in every conjugation, so they define the same unitary action. We use the Hermitian representative $i\vec e_y$ below.

### The projected identity

Taking the outer product of the lemma with itself gives the operator identity
$$
\tilde{Ϛ}_\psi^{(1)}\otimes \tilde\Pi_{\Phi^+}^{(23)}
=\tfrac14\sum_{\epsilon,\epsilon_2}\Omega_{\epsilon\epsilon_2}^{(12)}\otimes
\left(\tilde{U}_\epsilon\,\tilde{Ϛ}_\psi\,\tilde{U}_{\epsilon_2}^{*}\right)^{(3)},
$$

where $\tilde{U}_{\Phi^+}=e_t$, $\tilde{U}_{\Phi^-}=i\vec e_z$, $\tilde{U}_{\Psi^+}=i\vec e_x$, $\tilde{U}_{\Psi^-}=i\vec e_y$, and $\Omega_{\epsilon\epsilon_2}$ denotes the matrix unit spanning the one-dimensional Peirce component $\tilde\Pi_\epsilon(\mathbb{B}\otimes\mathbb{B})\tilde\Pi_{\epsilon_2}$ of the Bell idempotent basis, with $\Omega_{\epsilon\epsilon}=\tilde\Pi_\epsilon$. The identity is stated for a pure $\tilde{Ϛ}_\psi$; a general mixed state follows by linearity in $\tilde{Ϛ}_\psi$, since both sides are linear and every state is a convex combination of pure ones.

Now project onto the outcome $\epsilon_0$. Because the $\tilde\Pi_\epsilon$ are orthogonal idempotents, $\tilde\Pi_{\epsilon_0}\Omega_{\epsilon\epsilon_2}\tilde\Pi_{\epsilon_0}=\delta_{\epsilon_0\epsilon}\,\delta_{\epsilon_0\epsilon_2}\tilde\Pi_{\epsilon_0}$, and the double sum collapses to a single term. This is the teleportation identity.

**Proposition (teleportation identity).** For every Bell outcome $\epsilon$, with the Hermitian representatives $\tilde U_\epsilon\in\{e_t,\,i\vec e_x,\,i\vec e_y,\,i\vec e_z\}$ of the four Pauli gates,

$$
\boxed{\;\left(\tilde\Pi_\epsilon^{(12)}\otimes e_t\right)\tilde{Ϛ}^{(0)}\left(\tilde\Pi_\epsilon^{(12)}\otimes e_t\right)
=\tfrac14\,\tilde\Pi_\epsilon^{(12)}\otimes\left(\tilde U_\epsilon\,\tilde{Ϛ}_\psi\,\tilde U_\epsilon^{*}\right)^{(3)}\;}.
$$

Two consequences follow immediately by taking traces and partial traces.

**The probabilities are uniform.** Taking the trace of both sides, and using $\mathrm{Tr}(\tilde\Pi_\epsilon)=1$ and $\mathrm{Tr}(\tilde U_\epsilon\tilde{Ϛ}_\psi\tilde U_\epsilon^{*})=1$,

$$
\boxed{\;p_\epsilon=\mathrm{Tr}\!\left[\left(\tilde\Pi_\epsilon^{(12)}\otimes e_t\right)\tilde{Ϛ}^{(0)}\right]=\tfrac14\;},
$$

for each of the four outcomes. The outcome distribution is uniform and independent of $\tilde{Ϛ}_\psi$: the record alone carries no information about the state. The state is transferred to Bob's qubit by the projection itself, and the record's only role is to tell him which Pauli image he now holds and hence which correction to apply.

**Bob's conditional state.** Since $\mathrm{Tr}_{12}$ sends $\tilde\Pi_\epsilon\otimes X$ to $\mathrm{Tr}(\tilde\Pi_\epsilon)X=X$, the post-measurement reduced state of qubit $3$ is

$$
\mathrm{Tr}_{12}\!\left[(\tilde\Pi_\epsilon^{(12)}\otimes e_t)\,\tilde{Ϛ}^{(0)}\,(\tilde\Pi_\epsilon^{(12)}\otimes e_t)\right]
=\tfrac14\,\tilde U_\epsilon\,\tilde{Ϛ}_\psi\,\tilde U_\epsilon^{*} ,
\qquad
\frac{1}{p_\epsilon}\mathrm{Tr}_{12}(\cdots)=\tilde U_\epsilon\,\tilde{Ϛ}_\psi\,\tilde U_\epsilon^{*} .
$$

So each outcome leaves Bob's qubit in a unitary image of the unknown state, with the unitary determined by the outcome. The normalisation is the standard conditional-state normalisation; the unnormalised branch has trace $\tfrac14$, the probability of that outcome.

The four identities of the proposition are four distinct statements, one per outcome; each was recomputed directly in $\mathbb{B}^{\otimes3}$, on two pure and one mixed input state, not merely on the $\Phi^+$ outcome that organises the labelling.

## The Correction Gates

Bob's uncorrected state is $\tilde U_\epsilon\tilde{Ϛ}_\psi\tilde U_\epsilon^{*}$. To recover $\tilde{Ϛ}_\psi$ he applies the inverse gate, which acts by the conjugation $\tilde{Ϛ}\mapsto\tilde U_\epsilon^{*}\tilde{Ϛ}\,\tilde U_\epsilon$. Since each $\tilde U_\epsilon$ is a Hermitian involution, $\tilde U_\epsilon^{*}=\tilde U_\epsilon$ and $\tilde U_\epsilon^2=e_t$;

$$
\tilde U_\epsilon^{*}\left(\tilde U_\epsilon\,\tilde{Ϛ}_\psi\,\tilde U_\epsilon^{*}\right)\tilde U_\epsilon=\tilde{Ϛ}_\psi .
$$

The correction is therefore the same Pauli element that appears in Bob's uncorrected state, and the pair (outcome, correction) is as follows.

| Bell outcome | $\epsilon=(\epsilon_1,\epsilon_2,\epsilon_3)$ | stabiliser record $(s_1,s_3)$ | Bob's uncorrected state | correction $\tilde U_\epsilon$ |
|---|---|---|---|---|
| $\tilde\Pi_{\Phi^+}$ | $(-1,+1,-1)$ | $(+1,+1)$ | $\tilde{Ϛ}_\psi$ | $e_t$ |
| $\tilde\Pi_{\Phi^-}$ | $(+1,-1,-1)$ | $(-1,+1)$ | $i\vec e_z\,\tilde{Ϛ}_\psi\,i\vec e_z$ | $i\vec e_z$ |
| $\tilde\Pi_{\Psi^+}$ | $(-1,-1,+1)$ | $(+1,-1)$ | $i\vec e_x\,\tilde{Ϛ}_\psi\,i\vec e_x$ | $i\vec e_x$ |
| $\tilde\Pi_{\Psi^-}$ | $(+1,+1,+1)$ | $(-1,-1)$ | $i\vec e_y\,\tilde{Ϛ}_\psi\,i\vec e_y$ | $i\vec e_y$ |

In terms of the stabiliser record the correction has the compact form, up to the central phase that does not affect a gate,

$$
\tilde U_{(s_1,s_3)}=(i\vec e_z)^{(1-s_1)/2}\,(i\vec e_x)^{(1-s_3)/2},
$$

that is, $i\vec e_z$ if the $S_1$ outcome is $-1$ and $i\vec e_x$ if the $S_3$ outcome is $-1$; when both are $-1$ the product is $\tilde Q_z\tilde Q_x=-\tilde Q_x\tilde Q_z\sim\tilde Q_y$, the fourth Pauli. The four corrections are precisely the Pauli gates modulo phase; they lie in the Pauli group, hence in the Clifford group, of the companion article on gates and circuits. The protocol consumes only these four gates and a Bell-basis measurement.

Two remarks about the table. First, the fourth row is the one where the naive correspondence is easiest to get wrong: the standard decomposition produces $XZ$ for the outcome $|\Psi^-\rangle$, and $XZ=-i\sigma_y$ is *not* the element $\tilde Q_y=i\vec e_y$ but differs from it by the central phase $-i$. As a **gate** the two agree, and the row is written with the Hermitian representative; it was checked by conjugating a state by both, which gives the same result. Second, the table is not symmetric between $\Phi$ and $\Psi$ outcomes: the $\Phi^+$ row is the identity, and the others are the three non-identity Paulis, but the assignment of which Pauli goes with which outcome depends on the shared resource. It is a statement about the pair (resource, outcome), not about the outcome alone.

**A general Bell resource.** The choice $\tilde\Pi_{\Phi^+}$ is a convention; any resource of the form $(e_t\otimes\tilde{V})\tilde\Pi_{\Phi^+}(e_t\otimes\tilde{V}^{*})$ with $\tilde{V}$ a single-qubit unitary on Bob's factor works, and Bob's uncorrected state becomes $\tilde{V}\tilde U_\epsilon\tilde{Ϛ}_\psi\tilde U_\epsilon^{*}\tilde{V}^{*}$, so that the correction is $\tilde U_\epsilon^{*}\tilde{V}^{*}$. For $\tilde{V}=\tilde Q_x$ — which conjugates the resource to another Bell idempotent — this was verified outcome by outcome: the probabilities are still $\tfrac14$, Bob's state is the stated conjugation, and the stated correction restores $\tilde{Ϛ}_\psi$. The general statement is the standard local-unitary covariance of the protocol; it is recorded here as an inherited fact, with the one case checked.

## No-Signalling, and Why There Is No Copy

Before the classical record reaches Bob, his qubit carries no information about $\tilde{Ϛ}_\psi$. Write $\text{post}_\epsilon=\tilde\Pi_\epsilon^{(12)}\otimes(\tilde U_\epsilon\tilde{Ϛ}_\psi\tilde U_\epsilon^{*})^{(3)}$ for the normalised post-measurement state on the branch $\epsilon$, so that $\mathrm{Tr}_{12}[\text{post}_\epsilon]=\tilde U_\epsilon\tilde{Ϛ}_\psi\tilde U_\epsilon^{*}$. Averaging these over the outcomes, with their probabilities $p_\epsilon=\tfrac14$ and *without* any correction,

$$
\sum_\epsilon p_\epsilon\,\mathrm{Tr}_{12}\!\left[\text{post}_\epsilon\right]
=\tfrac14\sum_\epsilon \tilde U_\epsilon\,\tilde{Ϛ}_\psi\,\tilde U_\epsilon^{*} .
$$
The sum over the four Pauli gates is the elementary Pauli twirl, and it is computed directly on the Bloch vector. Conjugation by $i\vec e_x$ is a rotation by $\pi$ about $\vec e_x$, which fixes $r_1$ and reverses $r_2,r_3$; conjugation by $i\vec e_y$ reverses $r_1,r_3$; conjugation by $i\vec e_z$ reverses $r_1,r_2$; and $e_t$ changes nothing. Adding the four,
$$
\begin{aligned}
(r_1,r_2,r_3)&+(r_1,-r_2,-r_3)+(-r_1,r_2,-r_3)+(-r_1,-r_2,r_3)\\
&=(0,0,0),
\end{aligned}
$$

so the four terms cancel, and the average is

$$
\boxed{\;\tfrac14\sum_\epsilon \tilde U_\epsilon\,\tilde{Ϛ}_\psi\,\tilde U_\epsilon^{*}=\tfrac12 e_t\;}.
$$

Bob's unconditional state is the maximally mixed state, independent of $\tilde{Ϛ}_\psi$: Alice's measurement on her pair, however it comes out, has not changed the marginal statistics available to Bob. This is the no-signalling statement of the companion article on entangled subsystems, here in the specific form the protocol needs: all the dependence on the unknown state sits in the *record* $\epsilon$, and none of it sits in Bob's qubit until the record is used.

The same computation explains why the protocol does not clone. Alice's own qubit is left, after the measurement, in the state

$$
\mathrm{Tr}_{23}\!\left[\text{post}_\epsilon\right]
=\mathrm{Tr}_2(\tilde\Pi_\epsilon)\,\mathrm{Tr}_\mathbb{B}\!\left(\tilde U_\epsilon\tilde{Ϛ}_\psi\tilde U_\epsilon^{*}\right)
=\tfrac12 e_t ,
$$

since $\mathrm{Tr}_2(\tilde\Pi_\epsilon)=\tfrac12 e_t$. Her qubit is maximally mixed for every outcome: the state is destroyed locally, not copied, and the single surviving copy is the one reconstructed at Bob's qubit. The two classical bits carry exactly the information that the measured qubit no longer does.

## The Protocol as a Channel

The protocol can be read through the reversible/irreversible dichotomy of the companion article on quantum channels. Three interpretations are available, and they differ in what is treated as the output.

**Without the record: an irreversible channel of Kraus rank four.** Averaging the branches over the outcomes gives the state map

$$
\tilde{Ϛ}_\psi\ \longmapsto\ \tfrac14\sum_\epsilon \tilde U_\epsilon\,\tilde{Ϛ}_\psi\,\tilde U_\epsilon^{*}=\tfrac12 e_t ,
$$

which is the replacement channel to the maximally mixed state. In Kraus form it has the four linearly independent operators $\tilde{K}_\epsilon=\tfrac12\tilde U_\epsilon$, normalised by $\sum_\epsilon \tilde{K}_\epsilon^{*}\tilde{K}_\epsilon=\tfrac14\sum_\epsilon e_t=e_t$. It has Kraus rank four, it does not preserve purity, and it is not a gate: the protocol by itself is irreversible and, as the previous section shows, informationless.

**With the record: a selective gate on each branch.** Conditioned on the outcome $\epsilon$, the map from Alice's preparation to Bob's qubit is

$$
\tilde{Ϛ}_\psi\ \longmapsto\ \tilde U_\epsilon\,\tilde{Ϛ}_\psi\,\tilde U_\epsilon^{*} ,
$$

a single conjugation by the unitary gate $\tilde U_\epsilon$. Each branch is therefore a rank-one, purity-preserving, reversible map; the outcomes differ only by which Pauli conjugation is applied.

**With the record and the correction: the identity channel.** Applying the correction $\tilde U_\epsilon^{*}$ on each branch and summing the corrected branches with their probabilities,

$$
\tilde{Ϛ}_\psi\ \longmapsto\ \tfrac14\sum_\epsilon \tilde U_\epsilon^{*}\left(\tilde U_\epsilon\,\tilde{Ϛ}_\psi\,\tilde U_\epsilon^{*}\right)\tilde U_\epsilon=\tilde{Ϛ}_\psi ,
$$

which is the identity channel. Written in Kraus form it has the four normalised operators $\tilde{K}_\epsilon=\tfrac12\tilde U_\epsilon^{*}\tilde U_\epsilon=\tfrac12 e_t$, with $\sum_\epsilon\tilde{K}_\epsilon^{*}\tilde{K}_\epsilon=4\cdot\tfrac14 e_t=e_t$; the four are proportional, so the Kraus rank is one and the channel is conjugation by the single unitary $\tilde{K}=e_t$. The net state map on the teleported qubit is therefore a **gate** in the sense of the companion article: a single conjugation, purity-preserving and invertible.

The three interpretations are not in conflict; they are the instrument, its branches, and its completed action. What they show is that teleportation is *not* a counterexample to the reversible/irreversible dichotomy but an illustration of it. The measurement is a rank-four irreversible step; the classical record is what permits the rank-four step to be undone by a conditional rank-one step; and the completed protocol is the identity gate. Teleportation transfers a state; it does not compute on it. The cost of the transfer is the shared Bell idempotent, which is consumed by the measurement, together with the two classical bits, which are not an algebraic object at all.

## What the Reformulation Does and Does Not Claim

**It does provide:**

- A single algebraic home for every object of the protocol: the unknown state in $\mathbb{M}_+$, the resource as a Bell idempotent of $\mathbb{M}_+\otimes\mathbb{M}_+$, the measurement idempotents as $\tilde\Pi_\epsilon\otimes e_t$, and the corrections as unitary Pauli elements of $\mathbb{B}$.
- The teleportation identity as an algebraic identity per outcome, $(\tilde\Pi_\epsilon\otimes e_t)\tilde{Ϛ}^{(0)}(\tilde\Pi_\epsilon\otimes e_t)=\tfrac14 \tilde\Pi_\epsilon\otimes(\tilde U_\epsilon\tilde{Ϛ}_\psi\tilde U_\epsilon^{*})$, with the four outcomes and the four Pauli corrections displayed in one table and the record expressed as stabiliser eigenvalues.
- The uniform probability $\tfrac14$ for every outcome and the conditional state $\tilde U_\epsilon\tilde{Ϛ}_\psi\tilde U_\epsilon^{*}$ as direct traces and partial traces of that identity.
- No-signalling and the absence of a copy as two partial-trace computations, and the channel interpretation of the protocol as the rank-four instrument, its rank-one branches, and its rank-one completion.

**It does not claim:**

- A new theory of teleportation or of quantum information. The protocol is the standard one of Bennett et al., written in biquaternion notation; the reformulation is empirically empty by itself.
- An algebraic representation of the classical channel. The two bits are an outcome label outside the algebra; the algebra represents the label and the conditional correction, not their transmission.
- A resolution of the measurement problem. The protocol exhibits the conditional operation and the unconditional channel as two different algebraic objects, in the manner of the companion article on the measurement problem in algebraic form; it does not supply the fact of which branch occurred.
- A justification of the tensor-product arena $\mathbb{B}\otimes\mathbb{B}$. The whole protocol is a statement inside that arena once the arena is granted, and the companion articles leave its status open.
- A derivation of dense coding, of entanglement-swapping networks, or of any resource theory; none is developed here.

## Open Questions

**1. The classical record.** The two bits are the only element of the protocol that is not an element of the algebra. The outcome label is an eigenvalue pair of the commuting observables $S_1,S_3$, and the correction is the conditional gate selected by it; but the *selection* is not an algebraic operation on the algebra. Can the record be modelled inside the framework — as a decohered ancilla whose pointer basis is the stabiliser basis, as a controlled gate with the record as the control register, or as a conditional expectation — and does any of those interpretations say something the classical description does not?

**2. The coherent interpretation.** If Alice keeps the four outcomes coherent in a fourth register, the correction is a controlled unitary and the whole protocol is a single unitary element of $\mathbb{B}^{\otimes4}$. That interpretation makes teleportation a gate, at the price of treating the record as a quantum register and changing the resource accounting. Is there an algebraic criterion that identifies when the record is retained coherently and when it is discarded, or is the distinction again outside the algebra, as in the controlled-gate/measurement contrast of the companion article on gates?

**3. General resources.** The protocol was verified for the Bell resource $\tilde\Pi_{\Phi^+}$ and for one local-unitary image of it. For a general maximally entangled resource, the corrections are $\tilde U_\epsilon^{*}\tilde{V}^{*}$ with $\tilde{V}$ the local unitary relating the resource to $\tilde\Pi_{\Phi^+}$; is there a canonical statement of the outcome/correction correspondence in terms of the stabiliser group, and what happens when the resource is not maximally entangled at all?

**4. The tensor product.** As in the companion articles on the Bell basis and on gates, whether the three-qubit arena $\mathbb{B}^{\otimes3}$ is canonical for the framework or requires additional structure is unresolved. The teleportation identity inherits the contingency: it is a theorem about $\mathbb{B}^{\otimes3}$ once that arena is granted.

**5. The number of bits.** Why two classical bits suffice for one qubit — the dimension-counting content of the protocol — is a statement about the four Bell idempotents and the four Pauli gates modulo phase having the same number. Is that coincidence, or is the equality a structural feature of the framework that also constrains dense coding and other information protocols?

**6. Empirical content.** As everywhere in the framework, a rewriting of teleportation is not empirical content. What, if anything, distinguishes this formulation from standard quantum information is the central open question.

A source in the literature (Obojska, *Journal of Physics Communications* **4** (2020) 055018) proposes the same two directions as future work: a special unitary operation acting on biquaternions that reproduces teleportation, and an understanding of how rotations in $\mathbb{C}^4$ influence entanglement. The second is the subject of the companion articles on frame-dependent entanglement and on the Bell basis; the first is what this article carries out, for the Bell resource.

## Summary

Quantum teleportation in the biquaternion framework is the following chain of algebraic statements.

The resource is the Bell idempotent $\tilde\Pi_{\Phi^+}=\tfrac14(e_t\otimes e_t-\vec e_x\otimes \vec e_x+\vec e_y\otimes \vec e_y-\vec e_z\otimes \vec e_z)$ of $\mathbb{M}_+\otimes\mathbb{M}_+$, whose partial traces are both $\tfrac12 e_t$. The unknown single-qubit state is $\tilde{Ϛ}_\psi=\tfrac12(e_t+i\vec r)\in\mathbb{M}_+$, and the initial state is $\tilde{Ϛ}^{(0)}=\tilde{Ϛ}_\psi^{(1)}\otimes \tilde\Pi_{\Phi^+}^{(23)}$.

Alice measures the pair $(1,2)$ with the four Bell idempotents $\tilde\Pi_\epsilon^{(12)}=\tilde\Pi_\epsilon\otimes e_t$, equivalently with the commuting stabiliser observables $S_1=-\vec e_x\otimes \vec e_x$ and $S_3=-\vec e_z\otimes \vec e_z$, whose outcome pair is $(s_1,s_3)=(-\epsilon_1,-\epsilon_3)$. The teleportation identity

$$
\left(\tilde\Pi_\epsilon^{(12)}\otimes e_t\right)\tilde{Ϛ}^{(0)}\left(\tilde\Pi_\epsilon^{(12)}\otimes e_t\right)
=\tfrac14\,\tilde\Pi_\epsilon^{(12)}\otimes\left(\tilde U_\epsilon\,\tilde{Ϛ}_\psi\,\tilde U_\epsilon^{*}\right)^{(3)}
$$

holds for each of the four outcomes, with the Hermitian Pauli representatives $\tilde U_{\Phi^+}=e_t$, $\tilde U_{\Phi^-}=\tilde Q_z=i\vec e_z$, $\tilde U_{\Psi^+}=\tilde Q_x=i\vec e_x$, $\tilde U_{\Psi^-}=\tilde Q_y=i\vec e_y$. Its trace gives $p_\epsilon=\tfrac14$ for every outcome, and its partial trace gives Bob's conditional state $\tilde U_\epsilon\tilde{Ϛ}_\psi\tilde U_\epsilon^{*}$. Bob applies the correction $\tilde U_\epsilon^{*}=\tilde U_\epsilon$ and recovers $\tilde{Ϛ}_\psi$ exactly.

The unconditioned average of the branches is the Pauli twirl $\tfrac14\sum_\epsilon\tilde U_\epsilon\tilde{Ϛ}_\psi\tilde U_\epsilon^{*}=\tfrac12 e_t$, so no information reaches Bob before the record does — no-signalling in the protocol's own form — and Alice's qubit is left maximally mixed, so no copy is made. In the language of channels, the protocol without the record is a rank-four irreversible channel, each branch with the record is a rank-one gate, and the completed protocol with the record and the correction is the identity channel, a rank-one gate. Teleportation is thus the identity gate realised through a measurement of Kraus rank four, the resource and the record being its cost.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{M}_+$ | Hermitian subspace (states, observables) |
| $\mathbb{B}^{\otimes3}\cong M_8(\mathbb{C})$ | Three-qubit arena |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\tilde{Ϛ}_\psi=\tfrac12(e_t+i\vec r)$ | Unknown single-qubit state |
| $\tilde\Pi_\epsilon=\tfrac14(e_t\otimes e_t+\sum_k\epsilon_k \vec e_k\otimes \vec e_k)$ | Bell idempotent, $\epsilon_1\epsilon_2\epsilon_3=+1$ |
| $\tilde\Pi_{\Phi^+}$, $\epsilon=(-1,+1,-1)$ | Shared resource (Bell idempotent) |
| $S_1=-\vec e_x\otimes \vec e_x$, $S_3=-\vec e_z\otimes \vec e_z$ | Stabiliser involutions; $(s_1,s_3)=(-\epsilon_1,-\epsilon_3)$ |
| $\tilde\Pi_\epsilon^{(12)}=\tilde\Pi_\epsilon\otimes e_t$ | Bell measurement idempotent on qubits $(1,2)$ |
| $\tilde{Ϛ}^{(0)}=\tilde{Ϛ}_\psi^{(1)}\otimes \tilde\Pi_{\Phi^+}^{(23)}$ | Initial three-qubit state |
| $\tilde U_\epsilon\in\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$ | Correction gate (Hermitian Pauli) |
| $i\vec e_x,\ i\vec e_y,\ i\vec e_z$ | Pauli-gate representatives |
| $p_\epsilon=\tfrac14$ | Outcome probability |
| $\tilde U_\epsilon\tilde{Ϛ}_\psi\tilde U_\epsilon^{*}$ | Bob's conditional state |
| $\mathrm{Tr}_2(\tilde\Pi_\epsilon)=\mathrm{Tr}_1(\tilde\Pi_\epsilon)=\tfrac12 e_t$ | Maximally mixed partial trace |
| $\operatorname{Tr}(\tilde{Ϛ}\tilde H^{*})=\operatorname{Tr}(\tilde{Ϛ}\tilde H)=2\,\mathrm{Sc}(\tilde{Ϛ}\tilde H^{*}) = 2\langle\tilde{Ϛ},\tilde{H}\rangle_{*}$ | Trace reading at normalisation: the $2\times2$ reading of the Born weight |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |

## Further Reading

- C. H. Bennett, G. Brassard, C. Crépeau, R. Jozsa, A. Peres, and W. K. Wootters, "Teleporting an unknown quantum state via dual classical and Einstein–Podolsky–Rosen channels," *Physical Review Letters* **70** (1993) 1895–1899, for the original protocol.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the standard treatment of teleportation, the Bell basis, and the correction gates.
- A. Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), for the density-matrix and measurement formalism underlying the protocol.
- D. Bouwmeester, J.-W. Pan, K. Mattle, M. Eibl, H. Weinfurter, and A. Zeilinger, "Experimental quantum teleportation," *Nature* **390** (1997) 575–579, for the first experimental realisation.
- R. F. Werner, "All teleportation and dense coding schemes," *Journal of Physics A: Mathematical and General* **34** (2001) 7081–7094, for the classification of maximally entangled resources and the general local-unitary covariance of the corrections.
- C. H. Bennett and S. J. Wiesner, "Communication via one- and two-particle operators on Einstein–Podolsky–Rosen states," *Physical Review Letters* **69** (1992) 2881–2884, for dense coding, the dual protocol not developed here.
- K. Kraus, *States, Effects, and Operations* (Springer, 1983), for the instrument and Kraus-rank language used in the channel interpretation.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), and Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the rotor formulation of the corrections.
- Lidia Obojska, "Patterns of maximally entangled states within the algebra of biquaternions," *Journal of Physics Communications* **4** (2020) 055018, for the proposal of a biquaternion unitary reproducing teleportation, noted in *Open Questions*.
- The companion articles of this series: [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html), [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), [Quantum Physics in Biquaternionic Form](quantum-physics-in-biquaternionic-form.html), [Spin-1/2 Quantum Physics in Biquaternionic Form](spin-1-2-quantum-physics-in-biquaternionic-form.html), [Entangled Subsystems in the Biquaternion Framework](entangled-subsystems-in-the-biquaternion-framework.html), *The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$*, [Exercise: The Correlation Function of the Bell States](exercise-the-correlation-function-of-the-bell-states.html), [Exercise: The Reduced State of an Entangled Subsystem](exercise-the-reduced-state-of-an-entangled-subsystem.html), [Quantum Gates and Circuits in Biquaternionic Form](quantum-gates-and-circuits-in-biquaternionic-form.html), [Quantum Channels and the Reversible/Irreversible Dichotomy](quantum-channels-and-the-reversible-irreversible-dichotomy.html), [The Measurement Problem in Algebraic Form](the-measurement-problem-in-algebraic-form.html), and [Decoherence as Idempotent Projection](decoherence-as-idempotent-projection.html).
