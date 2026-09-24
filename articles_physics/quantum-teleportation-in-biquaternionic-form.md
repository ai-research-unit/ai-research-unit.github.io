# __Quantum Teleportation in Biquaternionic Form__

## Introduction

**Quantum teleportation** is the transmission of an unknown quantum state from one party to another using a pre-shared entangled state and two bits of classical communication. Alice holds the unknown qubit; she and Bob share an entangled pair, one half each. Alice measures her unknown qubit jointly with her half of the pair, in the basis of the four maximally entangled two-qubit states. Each of the four outcomes leaves Bob's half of the pair in one of four *unitary images* of the unknown state. Alice announces the outcome — two classical bits — and Bob applies the matching unitary correction. He then holds the unknown state exactly, and no copy of it exists anywhere: Alice's measurement has destroyed the original.

This article writes that protocol in the biquaternion language of the companion articles. The protocol is worth writing out because it is the one place in the framework where four of its constructions meet at once, and where the difference between them is forced into the open:

- the **state** is a positive trace-one element $\tilde{\rho}$ of the Hermitian subspace $\mathbb{M}_+\subset\mathbb{B}$;
- the **entangled resource** is a Bell idempotent $P_{\epsilon}$ of the tensor square $\mathbb{B}\otimes\mathbb{B}$ — idempotent and Hermitian, but *not* unitary;
- the **Bell measurement** is the four-outcome projective measurement whose projectors are those same idempotents on the pair;
- the **corrections** are unitary elements of $\mathbb{B}$ — gates, in the sense of the companion article on gates and circuits — and they are *not* idempotents.

The protocol is therefore a controlled collision between two kinds of object that the framework elsewhere keeps apart: the idempotents that resolve a measurement, and the unitaries that generate reversible motion. The distinction does real work in the correction table, where the same elements $e_1,e_2,e_3$ enter the resource idempotent as $e_k\otimes e_k$ and the correction gates as $ie_k$, and the two kinds of object behave quite differently.

**Established, and recomputed below.** The shared Bell idempotent $P_{\Phi^+}$ resolves the initial three-qubit state into four orthogonal branches, one per Bell outcome; each branch is the product of the outcome idempotent with a single conjugation of the unknown state; each outcome occurs with probability $\tfrac14$; and the correction equal to the (Hermitian, involutive) Pauli gate $\{e_0,ie_1,ie_2,ie_3\}$ restores the state exactly. Averaged over the outcomes without the classical record, Bob's qubit is the maximally mixed state $\tfrac12 e_0$ — the protocol transfers nothing on its own — and with the record and the correction the net state map on the teleported qubit is the identity channel, a gate of Kraus rank one, realised through a measurement of Kraus rank four. Alice's qubit is left maximally mixed, so no copy survives. Each of the four identities was recomputed separately, on input states other than the $\Phi^+$ case that fixes the labelling.

**Gap, left visible.** The two classical bits are *not* an element of the algebra. The algebra represents the outcome label — the joint eigenvalue of the stabiliser observables — and it represents the conditional correction; it does not contain the arithmetic by which the label reaches Bob. The protocol is a statement about the algebra *plus* a classical channel, and the classical channel is where the non-algebraic step sits. The status of the tensor-product arena $\mathbb{B}\otimes\mathbb{B}$ is the open question inherited from the companion articles and is not resolved here.

The article is organised as follows. The next section fixes the three-qubit arena and says which algebra each object of the protocol lives in. The section after that fixes the resource and the measurement. The following section proves the teleportation identity, first as a vector identity and then as the projected operator identity that gives the probabilities and Bob's state. The next section reads off the four corrections and records them in terms of the stabiliser observables. Two shorter sections treat no-signalling and the channel-theoretic reading of the protocol. The article closes with what the reformulation does and does not claim, and with open questions.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion units $e_0=1,e_1,e_2,e_3$ satisfying $e_k^2=-e_0$ and the cyclic relations $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$, and with $i$ the scalar imaginary, $i^2=-1$, commuting with every $e_k$. The Hermitian subspace is $\mathbb{M}_+$ with real basis $\{e_0,ie_1,ie_2,ie_3\}$; a single-qubit **state** is a Hermitian, positive, trace-one element of $\mathbb{M}_+$. The $n$-qubit arena is the tensor square $\mathbb{B}^{\otimes n}\cong M_{2^n}(\mathbb{C})$, with trace $\mathrm{Tr}(x\otimes y)=\mathrm{Tr}_\mathbb{B}(x)\cdot\mathrm{Tr}_\mathbb{B}(y)$, where $\mathrm{Tr}_\mathbb{B}(e_0)=2$ and $\mathrm{Tr}_\mathbb{B}(e_k)=0$, and with the partial traces $\mathrm{Tr}_1,\mathrm{Tr}_2$ of the companion article on entangled subsystems. The four **Bell idempotents** of $\mathbb{B}\otimes\mathbb{B}$ are $P_\epsilon=\tfrac14(e_0\otimes e_0+\epsilon_1 e_1\otimes e_1+\epsilon_2 e_2\otimes e_2+\epsilon_3 e_3\otimes e_3)$ with $\epsilon_1\epsilon_2\epsilon_3=+1$, in the labelling of the companion article on the Bell basis; the **stabiliser involutions** are $S_1=-e_1\otimes e_1$ and $S_3=-e_3\otimes e_3$, with $S_kP_\epsilon=-\epsilon_kP_\epsilon$. The **gates** are the unitary elements $\tilde{U}\tilde{U}^\dagger=e_0$ of $\mathbb{B}$, with Pauli representatives $\tilde{X}=ie_1$, $\tilde{Y}=ie_2$, $\tilde{Z}=ie_3$ and Hadamard $\tilde{H}=\tfrac{i}{\sqrt2}(e_1+e_3)$. The single-factor trace formula $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged.

## The Three-Qubit Arena and the Objects of the Protocol

Three qubits are involved, and it matters which is which:

- qubit $1$ is Alice's unknown qubit, in the state $\tilde{\rho}_\psi$;
- qubits $2$ and $3$ carry the shared Bell idempotent $P_{\Phi^+}$, qubit $2$ with Alice, qubit $3$ with Bob;
- the Bell measurement acts on qubits $1$ and $2$;
- the correction acts on qubit $3$ alone.

The arena is therefore $\mathbb{B}^{\otimes3}\cong M_8(\mathbb{C})$, with the trace the product of the factor traces, $\mathrm{Tr}(x\otimes y\otimes z)=\mathrm{Tr}_\mathbb{B}(x)\mathrm{Tr}_\mathbb{B}(y)\mathrm{Tr}_\mathbb{B}(z)$. The unknown state is written

$$
\tilde{\rho}_\psi=\tfrac12\left(e_0+i\mathbf{r}\right),
\qquad
\mathbf{r}=\sum_{k=1}^{3}r_k\,e_k,\qquad |\mathbf{r}|\leq 1 ,
$$

with $|\mathbf{r}|=1$ exactly when the state is pure and $\mathbf{r}=0$ when it is maximally mixed. The initial three-qubit state is the single element

$$
\tilde{\rho}^{(0)}=\tilde{\rho}_\psi^{(1)}\otimes P_{\Phi^+}^{(23)}\in\mathbb{M}_+\otimes\mathbb{M}_+\otimes\mathbb{M}_+ ,
\qquad
\mathrm{Tr}\left(\tilde{\rho}^{(0)}\right)=1\cdot 1=1 ,
$$

where the superscripts record which factor each element occupies.

It is worth stating explicitly which algebra each object belongs to, because the protocol puts them side by side and they are not interchangeable.

| Object | Algebra | Algebraic type |
|---|---|---|
| $\tilde{\rho}_\psi$ | $\mathbb{B}$ | Hermitian, positive, trace one; $\mathbb{M}_+$ |
| $P_{\Phi^+}$, $P_\epsilon$ | $\mathbb{B}\otimes\mathbb{B}$ | Hermitian idempotent of trace one; $\mathbb{M}_+\otimes\mathbb{M}_+$ |
| $S_1,S_3$ | $\mathbb{B}\otimes\mathbb{B}$ | Hermitian involutions; $\mathbb{M}_+\otimes\mathbb{M}_+$ |
| $P_\epsilon\otimes e_0$ | $\mathbb{B}^{\otimes3}$ | Hermitian idempotent on factors $(1,2)$ |
| $\tilde{\kappa}_\epsilon$ | $\mathbb{B}$ | Unitary (Hermitian Pauli); a gate |
| the classical record | — | two bits, not an element of any of the above |

Two distinctions in the table do the work of the whole article. First, the resource $P_{\Phi^+}$ and the measurement projectors $P_\epsilon\otimes e_0$ are **idempotent** and **not unitary**: $P_\epsilon^\dagger P_\epsilon=P_\epsilon\neq e_0\otimes e_0$ on the pair (and $P_\epsilon^{(12)}\neq e_0\otimes e_0\otimes e_0$ on three factors). They are the objects that resolve a measurement, and they are trace-one, not unimodular. Second, the corrections $\tilde{\kappa}_\epsilon$ are **unitary** and **not idempotent** (except for the identity): they are gates, and their conjugation action is reversible. The tensor square $\mathbb{B}\otimes\mathbb{B}$ is a matrix algebra, not a division algebra; it contains idempotents and zero divisors, and an element of $\mathbb{B}\otimes\mathbb{B}$ is not a state of a single qubit. The protocol is written below so that each line says which of these types is being used.

## The Resource and the Bell Measurement

**The resource.** The shared pair is the Bell idempotent of $|\Phi^+\rangle$,

$$
P_{\Phi^+}=\tfrac14\left(e_0\otimes e_0-e_1\otimes e_1+e_2\otimes e_2-e_3\otimes e_3\right),
\qquad \epsilon=(-1,+1,-1),
$$

an element of $\mathbb{M}_+\otimes\mathbb{M}_+$ with $P_{\Phi^+}^2=P_{\Phi^+}$, $P_{\Phi^+}^\dagger=P_{\Phi^+}$ and $\mathrm{Tr}(P_{\Phi^+})=1$. Its defining property for the protocol is that both its partial traces are maximally mixed, $\mathrm{Tr}_1(P_{\Phi^+})=\mathrm{Tr}_2(P_{\Phi^+})=\tfrac12 e_0$: neither party, holding one half, has any local information about the pair. This is the same idempotent that the companion article on the Bell basis singles out as a member of the Bell idempotent basis, and the same one that the companion article on gates and circuits produces from $|00\rangle$ by a Hadamard and a CNOT.

**The measurement.** Alice measures the pair $(1,2)$ in the Bell basis, that is, she measures the four projectors

$$
P_\epsilon^{(12)}=P_\epsilon\otimes e_0^{(3)},
\qquad \epsilon\in\{\Phi^+,\Phi^-,\Psi^+,\Psi^-\} ,
$$

where $P_\epsilon$ is the Bell idempotent on factors $(1,2)$ and $e_0$ acts as the identity on Bob's qubit. The four projectors inherit from the Bell idempotent basis the four properties that make them a projective measurement:

$$
\left(P_\epsilon^{(12)}\right)^2=P_\epsilon^{(12)},\qquad
\left(P_\epsilon^{(12)}\right)^\dagger=P_\epsilon^{(12)},\qquad
P_\epsilon^{(12)}P_{\epsilon'}^{(12)}=\delta_{\epsilon\epsilon'}P_\epsilon^{(12)},\qquad
\sum_\epsilon P_\epsilon^{(12)}=e_0\otimes e_0\otimes e_0 .
$$

Equivalently, and this is the form in which the outcome label is read, the measurement is the joint measurement of the two commuting Hermitian involutions $S_1^{(12)}=-e_1\otimes e_1\otimes e_0$ and $S_3^{(12)}=-e_3\otimes e_3\otimes e_0$. Their joint eigen-idempotents are the projectors, with

$$
S_1^{(12)}P_\epsilon^{(12)}=-\epsilon_1P_\epsilon^{(12)},\qquad
S_3^{(12)}P_\epsilon^{(12)}=-\epsilon_3P_\epsilon^{(12)} .
$$

The outcome label can therefore be recorded either as the Bell sign pattern $\epsilon=(\epsilon_1,\epsilon_2,\epsilon_3)$ or, equivalently, as the pair of stabiliser eigenvalues

$$
(s_1,s_3)=(-\epsilon_1,-\epsilon_3)\in\{\pm1\}^2 .
$$

Both labels are used below. Note again the type: $S_1,S_3$ are Hermitian **observables** (and involutions, hence also unitary), while the projectors onto their joint eigenspaces are Hermitian **idempotents** and not unitary. It is the projectors, not the observables, that enter the protocol's projection step.

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

Collecting the four terms gives the stated identity. $\square$

The four operators appearing on the right are the Pauli gates $I,X,Z,XZ$, and in biquaternion representatives (companion article on gates and circuits) they are

$$
I\leftrightarrow e_0,\qquad
X\leftrightarrow \tilde{X}=ie_1,\qquad
Z\leftrightarrow \tilde{Z}=ie_3,\qquad
XZ\leftrightarrow e_2\sim ie_2=\tilde{Y}.
$$

The last equivalence is a statement about **gates**, not about elements: $e_2$ and $ie_2$ differ by the central phase $-i$, which cancels in every conjugation, so they define the same unitary action. We use the Hermitian representative $ie_2$ below.

### The projected identity

Taking the outer product of the lemma with itself gives the operator identity

$$
\tilde{\rho}_\psi^{(1)}\otimes P_{\Phi^+}^{(23)}
=\tfrac14\sum_{\epsilon,\epsilon'}\Omega_{\epsilon\epsilon'}^{(12)}\otimes
\left(\tilde{U}_\epsilon\,\tilde{\rho}_\psi\,\tilde{U}_{\epsilon'}^\dagger\right)^{(3)},
$$

where $\tilde{U}_{\Phi^+}=e_0$, $\tilde{U}_{\Phi^-}=ie_3$, $\tilde{U}_{\Psi^+}=ie_1$, $\tilde{U}_{\Psi^-}=e_2$, and the $\Omega_{\epsilon\epsilon'}$ span the one-dimensional Peirce components $P_\epsilon(\mathbb{B}\otimes\mathbb{B})P_{\epsilon'}$ of the Bell idempotent basis, with $\Omega_{\epsilon\epsilon}=P_\epsilon$. The identity is stated for a pure $\tilde{\rho}_\psi$; a general mixed state follows by linearity in $\tilde{\rho}_\psi$, since both sides are linear and every state is a convex combination of pure ones.

Now project onto the outcome $\epsilon_0$. Because the $P_\epsilon$ are orthogonal idempotents, $P_{\epsilon_0}\Omega_{\epsilon\epsilon'}P_{\epsilon_0}=\delta_{\epsilon_0\epsilon}\,\delta_{\epsilon_0\epsilon'}P_{\epsilon_0}$, and the double sum collapses to a single term. This is the teleportation identity.

**Proposition (teleportation identity).** For every Bell outcome $\epsilon$, with the Hermitian representatives $\tilde{\kappa}_\epsilon\in\{e_0,\,ie_1,\,ie_2,\,ie_3\}$ of the four Pauli gates,

$$
\left(P_\epsilon^{(12)}\otimes e_0\right)\tilde{\rho}^{(0)}\left(P_\epsilon^{(12)}\otimes e_0\right)
=\tfrac14\,P_\epsilon^{(12)}\otimes\left(\tilde{\kappa}_\epsilon\,\tilde{\rho}_\psi\,\tilde{\kappa}_\epsilon^\dagger\right)^{(3)} .
$$

Two consequences follow immediately by taking traces and partial traces.

**The probabilities are uniform.** Taking the trace of both sides, and using $\mathrm{Tr}(P_\epsilon)=1$ and $\mathrm{Tr}(\tilde{\kappa}_\epsilon\tilde{\rho}_\psi\tilde{\kappa}_\epsilon^\dagger)=1$,

$$
p_\epsilon=\mathrm{Tr}\!\left[\left(P_\epsilon^{(12)}\otimes e_0\right)\tilde{\rho}^{(0)}\right]=\tfrac14 ,
$$

for each of the four outcomes. The outcome distribution is uniform and independent of $\tilde{\rho}_\psi$: the record alone carries no information about the state. The state is transferred to Bob's qubit by the projection itself, and the record's only role is to tell him which Pauli image he now holds and hence which correction to apply.

**Bob's conditional state.** Since $\mathrm{Tr}_{12}$ sends $P_\epsilon\otimes X$ to $\mathrm{Tr}(P_\epsilon)X=X$, the post-measurement reduced state of qubit $3$ is

$$
\mathrm{Tr}_{12}\!\left[(P_\epsilon^{(12)}\otimes e_0)\,\tilde{\rho}^{(0)}\,(P_\epsilon^{(12)}\otimes e_0)\right]
=\tfrac14\,\tilde{\kappa}_\epsilon\,\tilde{\rho}_\psi\,\tilde{\kappa}_\epsilon^\dagger ,
\qquad
\frac{1}{p_\epsilon}\mathrm{Tr}_{12}(\cdots)=\tilde{\kappa}_\epsilon\,\tilde{\rho}_\psi\,\tilde{\kappa}_\epsilon^\dagger .
$$

So each outcome leaves Bob's qubit in a unitary image of the unknown state, with the unitary determined by the outcome. The normalisation is the standard conditional-state normalisation; the unnormalised branch has trace $\tfrac14$, the probability of that outcome.

The four identities of the proposition are four distinct statements, one per outcome; each was recomputed directly in $\mathbb{B}^{\otimes3}$, on two pure and one mixed input state, not merely on the $\Phi^+$ outcome that organises the labelling.

## The Correction Gates

Bob's uncorrected state is $\tilde{\kappa}_\epsilon\tilde{\rho}_\psi\tilde{\kappa}_\epsilon^\dagger$. To recover $\tilde{\rho}_\psi$ he applies the inverse gate, which acts by the conjugation $\tilde{\rho}\mapsto\tilde{\kappa}_\epsilon^\dagger\tilde{\rho}\,\tilde{\kappa}_\epsilon$. Since each $\tilde{\kappa}_\epsilon$ is a Hermitian involution, $\tilde{\kappa}_\epsilon^\dagger=\tilde{\kappa}_\epsilon$ and $\tilde{\kappa}_\epsilon^2=e_0$;

$$
\tilde{\kappa}_\epsilon^\dagger\left(\tilde{\kappa}_\epsilon\,\tilde{\rho}_\psi\,\tilde{\kappa}_\epsilon^\dagger\right)\tilde{\kappa}_\epsilon=\tilde{\rho}_\psi .
$$

The correction is therefore the same Pauli element that appears in Bob's uncorrected state, and the pair (outcome, correction) is as follows.

| Bell outcome | $\epsilon=(\epsilon_1,\epsilon_2,\epsilon_3)$ | stabiliser record $(s_1,s_3)$ | Bob's uncorrected state | correction $\tilde{\kappa}_\epsilon$ |
|---|---|---|---|---|
| $P_{\Phi^+}$ | $(-1,+1,-1)$ | $(+1,+1)$ | $\tilde{\rho}_\psi$ | $e_0$ |
| $P_{\Phi^-}$ | $(+1,-1,-1)$ | $(-1,+1)$ | $\tilde{Z}\tilde{\rho}_\psi\tilde{Z}$ | $ie_3=\tilde{Z}$ |
| $P_{\Psi^+}$ | $(-1,-1,+1)$ | $(+1,-1)$ | $\tilde{X}\tilde{\rho}_\psi\tilde{X}$ | $ie_1=\tilde{X}$ |
| $P_{\Psi^-}$ | $(+1,+1,+1)$ | $(-1,-1)$ | $\tilde{Y}\tilde{\rho}_\psi\tilde{Y}$ | $ie_2=\tilde{Y}$ |

In terms of the stabiliser record the correction has the compact form, up to the central phase that does not affect a gate,

$$
\tilde{\kappa}_{(s_1,s_3)}=\tilde{Z}^{(1-s_1)/2}\,\tilde{X}^{(1-s_3)/2},
$$

that is, $\tilde{Z}$ if the $S_1$ outcome is $-1$ and $\tilde{X}$ if the $S_3$ outcome is $-1$; when both are $-1$ the product is $\tilde{Z}\tilde{X}=-\tilde{X}\tilde{Z}\sim\tilde{Y}$, the fourth Pauli. The four corrections are precisely the Pauli gates modulo phase; they lie in the Pauli group, hence in the Clifford group, of the companion article on gates and circuits. The protocol consumes only these four gates and a Bell-basis measurement.

Two remarks about the table. First, the fourth row is the one where the naive correspondence is easiest to get wrong: the standard decomposition produces $XZ$ for the outcome $|\Psi^-\rangle$, and $XZ=-i\sigma_y$ is *not* the element $\tilde{Y}=ie_2$ but differs from it by the central phase $-i$. As a **gate** the two agree, and the row is written with the Hermitian representative; it was checked by conjugating a state by both, which gives the same result. Second, the table is not symmetric between $\Phi$ and $\Psi$ outcomes: the $\Phi^+$ row is the identity, and the others are the three non-identity Paulis, but the assignment of which Pauli goes with which outcome depends on the shared resource. It is a statement about the pair (resource, outcome), not about the outcome alone.

**A general Bell resource.** The choice $P_{\Phi^+}$ is a convention; any resource of the form $(e_0\otimes\tilde{V})P_{\Phi^+}(e_0\otimes\tilde{V}^\dagger)$ with $\tilde{V}$ a single-qubit unitary on Bob's factor works, and Bob's uncorrected state becomes $\tilde{V}\tilde{\kappa}_\epsilon\tilde{\rho}_\psi\tilde{\kappa}_\epsilon^\dagger\tilde{V}^\dagger$, so that the correction is $\tilde{\kappa}_\epsilon^\dagger\tilde{V}^\dagger$. For $\tilde{V}=\tilde{X}$ — which conjugates the resource to another Bell idempotent — this was verified outcome by outcome: the probabilities are still $\tfrac14$, Bob's state is the stated conjugation, and the stated correction restores $\tilde{\rho}_\psi$. The general statement is the standard local-unitary covariance of the protocol; it is recorded here as an inherited fact, with the one case checked.

## No-Signalling, and Why There Is No Copy

Before the classical record reaches Bob, his qubit carries no information about $\tilde{\rho}_\psi$. Write $\text{post}_\epsilon=P_\epsilon^{(12)}\otimes(\tilde{\kappa}_\epsilon\tilde{\rho}_\psi\tilde{\kappa}_\epsilon^\dagger)^{(3)}$ for the normalised post-measurement state on the branch $\epsilon$, so that $\mathrm{Tr}_{12}[\text{post}_\epsilon]=\tilde{\kappa}_\epsilon\tilde{\rho}_\psi\tilde{\kappa}_\epsilon^\dagger$. Averaging these over the outcomes, with their probabilities $p_\epsilon=\tfrac14$ and *without* any correction,

$$
\sum_\epsilon p_\epsilon\,\mathrm{Tr}_{12}\!\left[\text{post}_\epsilon\right]
=\tfrac14\sum_\epsilon \tilde{\kappa}_\epsilon\,\tilde{\rho}_\psi\,\tilde{\kappa}_\epsilon^\dagger .
$$

The sum over the four Pauli gates is the elementary Pauli twirl, and it is computed directly on the Bloch vector. Conjugation by $ie_1$ is a rotation by $\pi$ about $e_1$, which fixes $r_1$ and reverses $r_2,r_3$; conjugation by $ie_2$ reverses $r_1,r_3$; conjugation by $ie_3$ reverses $r_1,r_2$; and $e_0$ changes nothing. Adding the four,

$$
\begin{aligned}
(r_1,r_2,r_3)&+(r_1,-r_2,-r_3)+(-r_1,r_2,-r_3)+(-r_1,-r_2,r_3)\\
&=(0,0,0),
\end{aligned}
$$

so each of the four rotations was used, and the average is

$$
\tfrac14\sum_\epsilon \tilde{\kappa}_\epsilon\,\tilde{\rho}_\psi\,\tilde{\kappa}_\epsilon^\dagger=\tfrac12 e_0 .
$$

Bob's unconditional state is the maximally mixed state, independent of $\tilde{\rho}_\psi$: Alice's measurement on her pair, however it comes out, has not changed the marginal statistics available to Bob. This is the no-signalling statement of the companion article on entangled subsystems, here in the specific form the protocol needs: all the dependence on the unknown state sits in the *record* $\epsilon$, and none of it sits in Bob's qubit until the record is used.

The same computation explains why the protocol does not clone. Alice's own qubit is left, after the measurement, in the state

$$
\mathrm{Tr}_{23}\!\left[\text{post}_\epsilon\right]
=\mathrm{Tr}_2(P_\epsilon)\,\mathrm{Tr}_\mathbb{B}\!\left(\tilde{\kappa}_\epsilon\tilde{\rho}_\psi\tilde{\kappa}_\epsilon^\dagger\right)
=\tfrac12 e_0 ,
$$

since $\mathrm{Tr}_2(P_\epsilon)=\tfrac12 e_0$. Her qubit is maximally mixed for every outcome: the state is destroyed locally, not copied, and the single surviving copy is the one reconstructed at Bob's qubit. The two classical bits carry exactly the information that the measured qubit no longer does.

## The Protocol as a Channel

The protocol can be read through the reversible/irreversible dichotomy of the companion article on quantum channels. Three readings are available, and they differ in what is treated as the output.

**Without the record: an irreversible channel of Kraus rank four.** Averaging the branches over the outcomes gives the state map

$$
\tilde{\rho}_\psi\ \longmapsto\ \tfrac14\sum_\epsilon \tilde{\kappa}_\epsilon\,\tilde{\rho}_\psi\,\tilde{\kappa}_\epsilon^\dagger=\tfrac12 e_0 ,
$$

which is the replacement channel to the maximally mixed state. In Kraus form it has the four linearly independent operators $\tilde{K}_\epsilon=\tfrac12\tilde{\kappa}_\epsilon$, normalised by $\sum_\epsilon \tilde{K}_\epsilon^\dagger\tilde{K}_\epsilon=\tfrac14\sum_\epsilon e_0=e_0$. It has Kraus rank four, it does not preserve purity, and it is not a gate: the protocol by itself is irreversible and, as the previous section shows, informationless.

**With the record: a selective gate on each branch.** Conditioned on the outcome $\epsilon$, the map from Alice's preparation to Bob's qubit is

$$
\tilde{\rho}_\psi\ \longmapsto\ \tilde{\kappa}_\epsilon\,\tilde{\rho}_\psi\,\tilde{\kappa}_\epsilon^\dagger ,
$$

a single conjugation by the unitary gate $\tilde{\kappa}_\epsilon$. Each branch is therefore a rank-one, purity-preserving, reversible map; the outcomes differ only by which Pauli conjugation is applied.

**With the record and the correction: the identity channel.** Applying the correction $\tilde{\kappa}_\epsilon^\dagger$ on each branch and summing the corrected branches with their probabilities,

$$
\tilde{\rho}_\psi\ \longmapsto\ \tfrac14\sum_\epsilon \tilde{\kappa}_\epsilon^\dagger\left(\tilde{\kappa}_\epsilon\,\tilde{\rho}_\psi\,\tilde{\kappa}_\epsilon^\dagger\right)\tilde{\kappa}_\epsilon=\tilde{\rho}_\psi ,
$$

which is the identity channel. Written in Kraus form it has the four normalised operators $\tilde{K}_\epsilon=\tfrac12\tilde{\kappa}_\epsilon^\dagger\tilde{\kappa}_\epsilon=\tfrac12 e_0$, with $\sum_\epsilon\tilde{K}_\epsilon^\dagger\tilde{K}_\epsilon=4\cdot\tfrac14 e_0=e_0$; the four are proportional, so the Kraus rank is one and the channel is conjugation by the single unitary $\tilde{K}=e_0$. The net state map on the teleported qubit is therefore a **gate** in the sense of the companion article: a single conjugation, purity-preserving and invertible.

The three readings are not in conflict; they are the instrument, its branches, and its completed action. What they show is that teleportation is *not* a counterexample to the reversible/irreversible dichotomy but an illustration of it. The measurement is a rank-four irreversible step; the classical record is what permits the rank-four step to be undone by a conditional rank-one step; and the completed protocol is the identity gate. Teleportation transfers a state; it does not compute on it. The cost of the transfer is the shared Bell idempotent, which is consumed by the measurement, together with the two classical bits, which are not an algebraic object at all.

## What the Reformulation Does and Does Not Claim

**It does provide:**

- A single algebraic home for every object of the protocol: the unknown state in $\mathbb{M}_+$, the resource as a Bell idempotent of $\mathbb{M}_+\otimes\mathbb{M}_+$, the measurement projectors as $P_\epsilon\otimes e_0$, and the corrections as unitary Pauli elements of $\mathbb{B}$.
- The teleportation identity as an algebraic identity per outcome, $(P_\epsilon\otimes e_0)\tilde{\rho}^{(0)}(P_\epsilon\otimes e_0)=\tfrac14 P_\epsilon\otimes(\tilde{\kappa}_\epsilon\tilde{\rho}_\psi\tilde{\kappa}_\epsilon^\dagger)$, with the four outcomes and the four Pauli corrections displayed in one table and the record expressed as stabiliser eigenvalues.
- The uniform probability $\tfrac14$ for every outcome and the conditional state $\tilde{\kappa}_\epsilon\tilde{\rho}_\psi\tilde{\kappa}_\epsilon^\dagger$ as direct traces and partial traces of that identity.
- No-signalling and the absence of a copy as two partial-trace computations, and the channel reading of the protocol as the rank-four instrument, its rank-one branches, and its rank-one completion.

**It does not claim:**

- A new theory of teleportation or of quantum information. The protocol is the standard one of Bennett et al., written in biquaternion notation; the reformulation is empirically empty by itself.
- An algebraic representation of the classical channel. The two bits are an outcome label outside the algebra; the algebra represents the label and the conditional correction, not their transmission.
- A resolution of the measurement problem. The protocol exhibits the conditional operation and the unconditional channel as two different algebraic objects, in the manner of the companion article on the measurement problem in algebraic form; it does not supply the fact of which branch occurred.
- A justification of the tensor-product arena $\mathbb{B}\otimes\mathbb{B}$. The whole protocol is a statement inside that arena once the arena is granted, and the companion articles leave its status open.
- A derivation of dense coding, of entanglement-swapping networks, or of any resource theory; none is developed here.

## Open Questions

**1. The classical record.** The two bits are the only element of the protocol that is not an element of the algebra. The outcome label is an eigenvalue pair of the commuting observables $S_1,S_3$, and the correction is the conditional gate selected by it; but the *selection* is not an algebraic operation on the algebra. Can the record be modelled inside the framework — as a decohered ancilla whose pointer basis is the stabiliser basis, as a controlled gate with the record as the control register, or as a conditional expectation — and does any of those readings say something the classical description does not?

**2. The coherent reading.** If Alice keeps the four outcomes coherent in a fourth register, the correction is a controlled unitary and the whole protocol is a single unitary element of $\mathbb{B}^{\otimes4}$. That reading makes teleportation a gate, at the price of treating the record as a quantum register and changing the resource accounting. Is there an algebraic criterion that identifies when the record is retained coherently and when it is discarded, or is the distinction again outside the algebra, as in the controlled-gate/measurement contrast of the companion article on gates?

**3. General resources.** The protocol was verified for the Bell resource $P_{\Phi^+}$ and for one local-unitary image of it. For a general maximally entangled resource, the corrections are $\tilde{\kappa}_\epsilon^\dagger\tilde{V}^\dagger$ with $\tilde{V}$ the local unitary relating the resource to $P_{\Phi^+}$; is there a canonical statement of the outcome/correction correspondence in terms of the stabiliser group, and what happens when the resource is not maximally entangled at all?

**4. The tensor product.** As in the companion articles on the Bell basis and on gates, whether the three-qubit arena $\mathbb{B}^{\otimes3}$ is canonical for the framework or requires additional structure is unresolved. The teleportation identity inherits the contingency: it is a theorem about $\mathbb{B}^{\otimes3}$ once that arena is granted.

**5. The number of bits.** Why two classical bits suffice for one qubit — the dimension-counting content of the protocol — is a statement about the four Bell idempotents and the four Pauli gates modulo phase having the same number. Is that coincidence, or is the equality a structural feature of the framework that also constrains dense coding and other information protocols?

**6. Empirical content.** As everywhere in the framework, a rewriting of teleportation is not empirical content. What, if anything, distinguishes this formulation from standard quantum information is the central open question.

## Summary

Quantum teleportation in the biquaternion framework is the following chain of algebraic statements.

The resource is the Bell idempotent $P_{\Phi^+}=\tfrac14(e_0\otimes e_0-e_1\otimes e_1+e_2\otimes e_2-e_3\otimes e_3)$ of $\mathbb{M}_+\otimes\mathbb{M}_+$, whose partial traces are both $\tfrac12 e_0$. The unknown single-qubit state is $\tilde{\rho}_\psi=\tfrac12(e_0+i\mathbf{r})\in\mathbb{M}_+$, and the initial state is $\tilde{\rho}^{(0)}=\tilde{\rho}_\psi^{(1)}\otimes P_{\Phi^+}^{(23)}$.

Alice measures the pair $(1,2)$ with the four Bell projectors $P_\epsilon^{(12)}=P_\epsilon\otimes e_0$, equivalently with the commuting stabiliser observables $S_1=-e_1\otimes e_1$ and $S_3=-e_3\otimes e_3$, whose outcome pair is $(s_1,s_3)=(-\epsilon_1,-\epsilon_3)$. The teleportation identity

$$
\left(P_\epsilon^{(12)}\otimes e_0\right)\tilde{\rho}^{(0)}\left(P_\epsilon^{(12)}\otimes e_0\right)
=\tfrac14\,P_\epsilon^{(12)}\otimes\left(\tilde{\kappa}_\epsilon\,\tilde{\rho}_\psi\,\tilde{\kappa}_\epsilon^\dagger\right)^{(3)}
$$

holds for each of the four outcomes, with the Hermitian Pauli representatives $\tilde{\kappa}_{\Phi^+}=e_0$, $\tilde{\kappa}_{\Phi^-}=\tilde{Z}=ie_3$, $\tilde{\kappa}_{\Psi^+}=\tilde{X}=ie_1$, $\tilde{\kappa}_{\Psi^-}=\tilde{Y}=ie_2$. Its trace gives $p_\epsilon=\tfrac14$ for every outcome, and its partial trace gives Bob's conditional state $\tilde{\kappa}_\epsilon\tilde{\rho}_\psi\tilde{\kappa}_\epsilon^\dagger$. Bob applies the correction $\tilde{\kappa}_\epsilon^\dagger=\tilde{\kappa}_\epsilon$ and recovers $\tilde{\rho}_\psi$ exactly.

The unconditioned average of the branches is the Pauli twirl $\tfrac14\sum_\epsilon\tilde{\kappa}_\epsilon\tilde{\rho}_\psi\tilde{\kappa}_\epsilon^\dagger=\tfrac12 e_0$, so no information reaches Bob before the record does — no-signalling in the protocol's own form — and Alice's qubit is left maximally mixed, so no copy is made. In the language of channels, the protocol without the record is a rank-four irreversible channel, each branch with the record is a rank-one gate, and the completed protocol with the record and the correction is the identity channel, a rank-one gate. Teleportation is thus the identity gate realised through a measurement of Kraus rank four, the resource and the record being its cost.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{M}_+$ | Hermitian subspace (states, observables) |
| $\mathbb{B}^{\otimes3}\cong M_8(\mathbb{C})$ | Three-qubit arena |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\tilde{\rho}_\psi=\tfrac12(e_0+i\mathbf{r})$ | Unknown single-qubit state |
| $P_\epsilon=\tfrac14(e_0\otimes e_0+\sum_k\epsilon_k e_k\otimes e_k)$ | Bell idempotent, $\epsilon_1\epsilon_2\epsilon_3=+1$ |
| $P_{\Phi^+}$, $\epsilon=(-1,+1,-1)$ | Shared resource (Bell idempotent) |
| $S_1=-e_1\otimes e_1$, $S_3=-e_3\otimes e_3$ | Stabiliser involutions; $(s_1,s_3)=(-\epsilon_1,-\epsilon_3)$ |
| $P_\epsilon^{(12)}=P_\epsilon\otimes e_0$ | Bell measurement projector on qubits $(1,2)$ |
| $\tilde{\rho}^{(0)}=\tilde{\rho}_\psi^{(1)}\otimes P_{\Phi^+}^{(23)}$ | Initial three-qubit state |
| $\tilde{\kappa}_\epsilon\in\{e_0,ie_1,ie_2,ie_3\}$ | Correction gate (Hermitian Pauli) |
| $\tilde{X}=ie_1,\ \tilde{Y}=ie_2,\ \tilde{Z}=ie_3$ | Pauli gates |
| $p_\epsilon=\tfrac14$ | Outcome probability |
| $\tilde{\kappa}_\epsilon\tilde{\rho}_\psi\tilde{\kappa}_\epsilon^\dagger$ | Bob's conditional state |
| $\mathrm{Tr}_2(P_\epsilon)=\mathrm{Tr}_1(P_\epsilon)=\tfrac12 e_0$ | Maximally mixed partial trace |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula (Born rule) |

## Further Reading

- C. H. Bennett, G. Brassard, C. Crépeau, R. Jozsa, A. Peres, and W. K. Wootters, "Teleporting an unknown quantum state via dual classical and Einstein–Podolsky–Rosen channels," *Physical Review Letters* **70** (1993) 1895–1899, for the original protocol.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the standard treatment of teleportation, the Bell basis, and the correction gates.
- A. Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), for the density-matrix and measurement formalism underlying the protocol.
- D. Bouwmeester, J.-W. Pan, K. Mattle, M. Eibl, H. Weinfurter, and A. Zeilinger, "Experimental quantum teleportation," *Nature* **390** (1997) 575–579, for the first experimental realisation.
- R. F. Werner, "All teleportation and dense coding schemes," *Journal of Physics A: Mathematical and General* **34** (2001) 7081–7094, for the classification of maximally entangled resources and the general local-unitary covariance of the corrections.
- C. H. Bennett and S. J. Wiesner, "Communication via one- and two-particle operators on Einstein–Podolsky–Rosen states," *Physical Review Letters* **69** (1992) 2881–2884, for dense coding, the dual protocol not developed here.
- K. Kraus, *States, Effects, and Operations* (Springer, 1983), for the instrument and Kraus-rank language used in the channel reading.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), and Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the rotor formulation of the corrections.
- The companion articles of this series: *Introduction to the Biquaternion Universe*, *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, *Quantum Mechanics in Biquaternionic Form*, *Spin-1/2 Quantum Mechanics in Biquaternionic Form*, *Entangled Subsystems in the Biquaternion Framework*, *The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$*, *Exercise: The Correlation Function of the Bell States*, *Exercise: The Reduced State of an Entangled Subsystem*, *Quantum Gates and Circuits in Biquaternionic Form*, *Quantum Channels and the Reversible/Irreversible Dichotomy*, *The Measurement Problem in Algebraic Form*, and *Decoherence as Idempotent Projection*.
