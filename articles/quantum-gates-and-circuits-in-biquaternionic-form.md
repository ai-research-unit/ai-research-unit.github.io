# __Quantum Gates and Circuits in Biquaternionic Form__

## Introduction

A quantum gate is a reversible operation on a quantum state. In the biquaternion framework the state of a qubit is an element of the Hermitian subspace $\mathbb{M}_+$ of the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, namely a positive trace-one element

$$
\tilde{\rho} = \tfrac{1}{2}\left(e_0 + i\,\mathbf{r}\right), \qquad \mathbf{r} \in \mathbb{R}^3,
$$

and a gate is a **single element of the algebra** acting on it by conjugation:

$$
\tilde{\rho} \;\longmapsto\; \tilde{U}\,\tilde{\rho}\,\tilde{U}^\dagger, \qquad \tilde{U}\tilde{U}^\dagger = e_0 .
$$

The acting element $\tilde{U}$ is a **unitary biquaternion**; the unitaries form the group $U(2) \subset \mathbb{B}$. A circuit is then a **product** of such elements. Composing two gates is multiplying two unitaries, and the effect of a whole circuit is a single conjugation by that product. The algebraic product in $\mathbb{B}$ (or in the tensor product $\mathbb{B}^{\otimes n}$ for $n$ qubits) is what the wiring of a circuit expresses.

This formulation is the one already used in the companion articles: states and observables in $\mathbb{M}_+$, reversible evolution by rotor conjugation, irreversible measurement by the sandwich operation. The companion article *Quantum Channels and the Reversible/Irreversible Dichotomy* established that the reversible state maps are exactly the conjugations by unitary biquaternions — the channels of Kraus rank one — and that everything else is a sum of conjugations. The present article reads the standard gate and circuit notation through that result: **a gate is a Kraus-rank-one channel, a circuit of gates is again a gate, and the moment a circuit contains a measurement it is a channel and no longer a gate.**

Two warnings are in order at the outset, both inherited from the companion articles.

First, the mathematics below is **standard quantum information theory** transcribed into biquaternion notation. Nothing here depends on the physical hypothesis that $\mathbb{M}_+$ is a distinct sector of the world. The reformulation is structural: it says where the objects of quantum computation live in the algebra and which algebraic operation each circuit ingredient is.

Second, the word "rotor conjugation" is used for the gate action, and it must be distinguished sharply from the Lorentz rotor of the material sector. Both actions have the same form $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$, but the condition on the acting element is different. The material-sector rotor satisfies the **unit-norm-form** condition $\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$ and generates $SL(2,\mathbb{C})$; a gate satisfies the **matrix-unitarity** condition $\tilde{U}\tilde{U}^\dagger = e_0$ and generates $U(2)$. A Lorentz boost is Hermitian and therefore satisfies $\tilde{\Lambda}\tilde{\Lambda}^\dagger = \tilde{\Lambda}^2 \neq e_0$: it is a perfectly good rotor on $\mathbb{M}_-$ but **not** a gate on $\mathbb{M}_+$, because it does not preserve the trace. The two groups sit in the same algebra, and keeping them apart is the main technical discipline of this article.

The article is organised as follows. The gate group and its structure are described first. Then the standard single-qubit gate set is exhibited in biquaternion form. Then composition is treated as the algebra product, including the Clifford group. Then multi-qubit gates are built in the tensor-product arena, with the controlled gate, CNOT, CZ, and SWAP. Then a simple circuit — the preparation of a Bell state — is worked through algebraically. Then the reversible gates are contrasted with the irreversible channels of the read list. The article closes with what the reformulation does and does not claim, and with open questions.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_j e_k = \epsilon_{jkl} e_l$ for distinct $j,k$; the scalar imaginary is $i$, central and with $i^2 = -1$; the fixed-point subspaces are $\mathbb{C}_{\mathbb{B}}$ (the complex subspace, the center), $\mathbb{H}_{\mathbb{B}}$ (the real-quaternion subspace), $\mathbb{M}_+$ (Hermitian), and $\mathbb{M}_-$ (anti-Hermitian). The trace is $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$, and the trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is the Born rule. The isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ is the one fixed by the companion article on quantum mechanics,

$$
e_0 \mapsto I_2, \qquad e_1 \mapsto -i\sigma_1, \qquad e_2 \mapsto -i\sigma_2, \qquad e_3 \mapsto -i\sigma_3, \qquad i \mapsto i I_2 ,
$$

with $\sigma_1,\sigma_2,\sigma_3$ the Pauli matrices. Under it, $\sigma_k$ is the image of $i e_k$, and the idempotent $\tfrac{1}{2}(e_0 + i\hat{\mu})$ is the spin-up projector along $\hat{\mu}$.

## The Gate Group

### Gates as Unitary Elements

**Definition.** A **gate** is a unitary element of $\mathbb{B}$,

$$
\mathcal{U} \;=\; \{\tilde{U} \in \mathbb{B} : \tilde{U}\tilde{U}^\dagger = e_0\} \;\cong\; U(2),
$$

acting on a state $\tilde{\rho} = \tfrac{1}{2}(e_0 + i\mathbf{r})$ by **rotor conjugation**

$$
\Phi_{\tilde{U}}(\tilde{\rho}) = \tilde{U}\,\tilde{\rho}\,\tilde{U}^\dagger .
$$

The image is again Hermitian, positive, and of trace one: since $\tilde{\rho}^\dagger = \tilde{\rho}$ and $\tilde{U}^\dagger\tilde{U} = e_0$,

$$
\Phi_{\tilde{U}}(\tilde{\rho})^\dagger = \tilde{U}\tilde{\rho}\tilde{U}^\dagger = \Phi_{\tilde{U}}(\tilde{\rho}),
\qquad
\mathrm{Tr}\!\left(\Phi_{\tilde{U}}(\tilde{\rho})\right) = \mathrm{Tr}(\tilde{\rho}) = 1 .
$$

So a gate maps states to states.

**The gate is a channel of Kraus rank one.** In the language of the companion article on quantum channels, $\Phi_{\tilde{U}}$ has the single Kraus operator $\tilde{K} = \tilde{U}$ with $\tilde{K}^\dagger\tilde{K} = e_0$. It is therefore completely positive and trace preserving, and it is exactly the class of channels that are **invertible within the channels**, with inverse $\Phi_{\tilde{U}}^{-1} = \Phi_{\tilde{U}^\dagger}$ (whose Kraus operator is $\tilde{U}^\dagger$); it is also exactly the class that **preserves purity**, $\mathrm{Tr}(\Phi_{\tilde{U}}(\tilde{\rho})^2) = \mathrm{Tr}(\tilde{\rho}^2)$. A gate is a reversible process, and conversely every reversible process of the informational sector is a gate.

### Why Matrix-Unitarity and Not Unit Norm Form

The condition $\tilde{U}\tilde{U}^\dagger = e_0$ must not be confused with the unit-norm-form condition $\tilde{U}\bar{\tilde{U}} = e_0$ that defines the Lorentz rotors $SL(2,\mathbb{C})$. The two conditions pick out two different subgroups of the same algebra, and only the first is a group of gates.

The distinction is visible in a single example. A **boost biquaternion**

$$
\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}}
$$

is Hermitian, $\tilde{\Lambda}^\dagger = \tilde{\Lambda}$, and has unit norm form, $\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$. Hence $\tilde{\Lambda}\tilde{\Lambda}^\dagger = \tilde{\Lambda}^2 \neq e_0$, and conjugation by $\tilde{\Lambda}$ does not preserve the trace:

$$
\mathrm{Tr}\!\left(\tilde{\Lambda}\tilde{\rho}\tilde{\Lambda}^\dagger\right) \neq \mathrm{Tr}(\tilde{\rho}) \quad \text{in general}.
$$

A boost is a rotor on the material sector $\mathbb{M}_-$ and **not** a gate on the informational sector $\mathbb{M}_+$. The distinction is not a technicality: it is the algebraic expression of the fact that the Lorentz group and the gate group are different groups inside one algebra, related to the two complementary subspaces.

The two actions are collected here for contrast.

| | Material sector (Lorentz) | Informational sector (gates) |
|---|---|---|
| Acting element | $\tilde{\Lambda}\in\mathbb{B}$, $\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$ | $\tilde{U}\in\mathbb{B}$, $\tilde{U}\tilde{U}^\dagger = e_0$ |
| Group | $SL(2,\mathbb{C})$ | $U(2)$ |
| Acting on | $\tilde{X}\in\mathbb{M}_-$ | $\tilde{\rho}\in\mathbb{M}_+$ |
| Action | $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ | $\tilde{\rho}\mapsto\tilde{U}\tilde{\rho}\tilde{U}^\dagger$ |
| Pure boost | Hermitian, in $\mathbb{M}_+$, not unitary | not a gate |

### The Structure of the Gate Group

Every unitary biquaternion factorises into a central phase and a unit real quaternion:

$$
U(2) \;=\; U(1)\cdot SU(2), \qquad
\tilde{U} = e^{i\phi}\,\tilde{R}, \qquad \phi\in\mathbb{R}, \quad \tilde{R}\in\mathbb{H}_{\mathbb{B}}, \quad \tilde{R}\bar{\tilde{R}} = e_0 .
$$

Under the isomorphism, the unit real quaternions are exactly the image of $SU(2) \subset M_2(\mathbb{C})$, since $\det \tilde{R} = \tilde{R}\bar{\tilde{R}} = 1$. The phase $e^{i\phi}$ lies in the center $\mathbb{C}_{\mathbb{B}}$, and $i\mathbb{M}_+ = \mathbb{M}_-$ for the anti-Hermitian generators.

The phase is **not observable in the action**. Conjugation by a central element is trivial:

$$
(e^{i\phi}\tilde{R})\,\tilde{\rho}\,(e^{i\phi}\tilde{R})^\dagger
= e^{i\phi}\tilde{R}\,\tilde{\rho}\,\tilde{R}^\dagger e^{-i\phi}
= \tilde{R}\,\tilde{\rho}\,\tilde{R}^\dagger .
$$

Hence the kernel of $\tilde{U}\mapsto\Phi_{\tilde{U}}$ is the unit circle $U(1)\subset\mathbb{C}_{\mathbb{B}}$, and the effective group of gates is

$$
U(2)/U(1) \;\cong\; PU(2) \;\cong\; SO(3),
$$

acting on the Bloch ball by rotations. This is the algebraic form of the unobservability of the global phase: two unitaries that differ by a central phase define the same gate.

**The action on the Bloch vector.** Writing the state as $\tilde{\rho} = \tfrac{1}{2}(e_0 + i\mathbf{r})$, a gate acts as

$$
\mathbf{r} \;\longmapsto\; R(\tilde{U})\,\mathbf{r}, \qquad R(\tilde{U}) \in SO(3),
$$

a proper rotation of $\mathbb{R}^3$. The scalar part of the state is fixed, the norm $|\mathbf{r}|$ is preserved, and with it the purity $\mathrm{Tr}(\tilde{\rho}^2) = \tfrac{1}{2}(1 + |\mathbf{r}|^2)$ and the spectrum $\lambda_\pm = \tfrac{1}{2}(1\pm|\mathbf{r}|)$. A gate rotates the Bloch ball rigidly; it never contracts it.

**Rotation gates.** The unit real quaternion with axis $\hat{\mathbf{n}}$ and angle $\theta$,

$$
\tilde{R}_{\hat{\mathbf{n}}}(\theta) = \cos\frac{\theta}{2}\,e_0 + \sin\frac{\theta}{2}\,\hat{\mathbf{n}},
\qquad \hat{\mathbf{n}}^2 = -e_0 ,
$$

acts on the Bloch vector as the rotation by $\theta$ about $\hat{\mathbf{n}}$ (the Rodrigues formula). The half-angle is the double cover: $\tilde{R}_{\hat{\mathbf{n}}}(\theta + 2\pi) = -\tilde{R}_{\hat{\mathbf{n}}}(\theta)$, which is the same rotation and, since $-e_0$ is a central phase, the same gate. The general gate is $e^{i\phi}\tilde{R}_{\hat{\mathbf{n}}}(\theta)$, and modulo the phase it is a rotation.

### Involutions: The Hermitian Unitaries

A unitary can be Hermitian, $\tilde{U} = \tilde{U}^\dagger$. Then $\tilde{U}^2 = \tilde{U}\tilde{U}^\dagger = e_0$, so a Hermitian unitary is an **involution**. Apart from $\pm e_0$, the Hermitian unitaries are exactly

$$
\tilde{U} = \pm\, i\hat{\mathbf{n}}, \qquad \hat{\mathbf{n}} \text{ a unit pure real quaternion},
$$

since $(i\hat{\mathbf{n}})^\dagger = -i\hat{\mathbf{n}}^\dagger = i\hat{\mathbf{n}}$ and $(i\hat{\mathbf{n}})^2 = -\hat{\mathbf{n}}^2 = e_0$. They lie in $\mathbb{M}_+$, and as rotations they are the **$\pi$-rotations** of the Bloch sphere: conjugation by $i\hat{\mathbf{n}}$ sends $\mathbf{r}\mapsto 2(\hat{\mathbf{n}}\cdot\mathbf{r})\hat{\mathbf{n}} - \mathbf{r}$. The Pauli gates and the Hadamard gate below are of this type; the phase and $T$ gates are not.

A caution about representatives. A gate is a coset $\tilde{U}\cdot U(1)$; the representative can be chosen Hermitian only when the gate is an involution. Membership of the representative in $\mathbb{M}_+$ or in $\mathbb{H}_{\mathbb{B}}$ is therefore a property of the chosen representative, not an invariant of the gate. The one representative-independent statement is the factorisation $\tilde{U} = e^{i\phi}\tilde{R}$: **every gate is a central phase times a rotation, and no gate is anything else.**

## The Standard Single-Qubit Gate Set

Under the isomorphism $e_k \mapsto -i\sigma_k$, the image of $i e_k$ is $\sigma_k$. The standard gate set therefore reads as follows. In each row the second column is a biquaternion representative; a representative differing by a central phase gives the same gate.

| Gate | Biquaternion representative | Matrix image | Action on $\mathbf{r}=(r_1,r_2,r_3)$ |
|---|---|---|---|
| $X$ (Pauli) | $\tilde{X} = i e_1$ | $\sigma_1$ | $(r_1,-r_2,-r_3)$ |
| $Y$ (Pauli) | $\tilde{Y} = i e_2$ | $\sigma_2$ | $(-r_1,r_2,-r_3)$ |
| $Z$ (Pauli) | $\tilde{Z} = i e_3$ | $\sigma_3$ | $(-r_1,-r_2,r_3)$ |
| $H$ (Hadamard) | $\tilde{H} = \dfrac{i}{\sqrt{2}}\left(e_1+e_3\right)$ | $\dfrac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ | $(r_3,-r_2,r_1)$ |
| $S$ (phase) | $\tilde{S} = \dfrac{1}{\sqrt{2}}\left(e_0+e_3\right)$ | $\operatorname{diag}(e^{-i\pi/4},e^{i\pi/4})$ | $(-r_2,r_1,r_3)$ |
| $T$ ($\pi/8$) | $\tilde{T} = \cos\dfrac{\pi}{8}e_0 + \sin\dfrac{\pi}{8}e_3$ | $\operatorname{diag}(e^{-i\pi/8},e^{i\pi/8})$ | rotation by $\pi/4$ about $e_3$ |
| $R_{\hat{\mathbf{n}}}(\theta)$ | $\cos\dfrac{\theta}{2}e_0 + \sin\dfrac{\theta}{2}\hat{\mathbf{n}}$ | $e^{-i\theta\,\hat{\mathbf{n}}\cdot\boldsymbol{\sigma}/2}$ | rotation by $\theta$ about $\hat{\mathbf{n}}$ |

The matrix column is the image under $\mathbb{B}\cong M_2(\mathbb{C})$. For $S$ and $T$ the displayed matrices are $\operatorname{diag}(e^{-i\pi/4},e^{i\pi/4})$ and $\operatorname{diag}(e^{-i\pi/8},e^{i\pi/8})$, which are the standard $S$ and $T$ up to the central phases $e^{i\pi/4}$ and $e^{i\pi/8}$; equivalently, $S$ and $T$ are represented exactly by the unit real quaternions shown. This is the representative-dependence noted above.

### The Pauli Gates

The three Pauli gates are the Hermitian unitaries along the coordinate axes:

$$
\tilde{X} = i e_1, \qquad \tilde{Y} = i e_2, \qquad \tilde{Z} = i e_3 .
$$

Each satisfies $\tilde{X}^2 = \tilde{Y}^2 = \tilde{Z}^2 = e_0$, so each is an involution and a $\pi$-rotation; the actions on the Bloch vector in the table are the corresponding reflections through the coordinate axes. Their products reproduce the Pauli algebra as an algebra identity:

$$
\tilde{X}\tilde{Y} = i\tilde{Z}, \qquad \tilde{Y}\tilde{Z} = i\tilde{X}, \qquad \tilde{Z}\tilde{X} = i\tilde{Y}, \qquad \tilde{X}\tilde{Z} = -\tilde{Z}\tilde{X},
\qquad \tilde{X}\tilde{Y}\tilde{Z} = i e_0 .
$$

The central factor $i e_0$ is the price of writing the Pauli matrices in a basis of *real* quaternions: the standard Pauli matrices obey $\sigma_1\sigma_2 = i\sigma_3$ with the same scalar imaginary, and the isomorphism carries that scalar imaginary to the central element $i e_0$ of $\mathbb{B}$. The sign of the product is what distinguishes the two orders, $\tilde{X}\tilde{Z} = -\tilde{Z}\tilde{X}$: this is the algebraic origin of the non-commutativity that makes gates into a group rather than a set.

### The Hadamard Gate

The Hadamard gate is the Hermitian unitary along the diagonal axis:

$$
\tilde{H} = \frac{i}{\sqrt{2}}\left(e_1 + e_3\right),
\qquad
\tilde{H}^2 = e_0,
\qquad
\tilde{H}^\dagger = \tilde{H}.
$$

It is the $\pi$-rotation about $\hat{\mathbf{n}} = (e_1+e_3)/\sqrt{2}$, so on the Bloch vector it exchanges the $e_1$ and $e_3$ axes and reverses $e_2$:

$$
\tilde{H}\,\tilde{Z}\,\tilde{H} = \tilde{X}, \qquad
\tilde{H}\,\tilde{X}\,\tilde{H} = \tilde{Z}, \qquad
\tilde{H}\,\tilde{Y}\,\tilde{H} = -\tilde{Y}.
$$

All three identities were recomputed directly from the quaternion product. The first two are exact identities among elements of $\mathbb{B}$; the third carries a sign, and since $-e_0$ is central, $\tilde{H}\tilde{Y}\tilde{H} = -\tilde{Y}$ and $\tilde{Y}$ define the **same gate**. This is a small but representative point: an algebraic identity of representatives need not be an identity of gates, and the discrepancy is always a central phase.

### The Phase and $T$ Gates

The phase gate is the rotation by $\pi/2$ about $e_3$:

$$
\tilde{S} = \frac{1}{\sqrt{2}}\left(e_0 + e_3\right) = \tilde{R}_{\hat{e}_3}\!\left(\frac{\pi}{2}\right),
\qquad
\tilde{S}^2 = e_3 .
$$

The element $e_3$ is not $Z = i e_3$; it differs from it by the central phase $-i$, so $\tilde{S}^2$ and $\tilde{Z}$ define the same gate. In the standard normalisation, $S^2 = Z$ exactly; in the biquaternion representative, $S^2 = Z$ **up to a central phase**, which is the honest statement.

The $T$ gate is the rotation by $\pi/4$ about $e_3$:

$$
\tilde{T} = \cos\frac{\pi}{8}\,e_0 + \sin\frac{\pi}{8}\,e_3 = \tilde{R}_{\hat{e}_3}\!\left(\frac{\pi}{4}\right),
\qquad
\tilde{T}^2 = \tilde{S}, \qquad
\tilde{T}^{8} = -e_0, \qquad
\tilde{T}^{16} = e_0 .
$$

Thus $T$ has order eight as a gate and order sixteen as an element of $SU(2)$. The relation $T^2 = S$ and the order were recomputed. Both $S$ and $T$ are represented by unit real quaternions, i.e. by elements of the rotation group, and neither is Hermitian; this is why their biquaternion representatives lie in $\mathbb{H}_{\mathbb{B}}$ rather than in $\mathbb{M}_+$, in contrast with the Pauli and Hadamard gates.

## Composition of Gates as Algebraic Product

### The Product Law

Let $\tilde{U}$ and $\tilde{V}$ be gates, and consider the physical process that applies $\tilde{U}$ first and $\tilde{V}$ second. The state passes through

$$
\tilde{\rho} \;\xrightarrow{\ \tilde{U}\ }\; \tilde{U}\tilde{\rho}\tilde{U}^\dagger
\;\xrightarrow{\ \tilde{V}\ }\; \tilde{V}\tilde{U}\tilde{\rho}\tilde{U}^\dagger\tilde{V}^\dagger
= (\tilde{V}\tilde{U})\,\tilde{\rho}\,(\tilde{V}\tilde{U})^\dagger .
$$

So the composite gate is the **product** $\tilde{W} = \tilde{V}\tilde{U}$, and the map on channels is

$$
\Phi_{\tilde{V}} \circ \Phi_{\tilde{U}} = \Phi_{\tilde{V}\tilde{U}} .
$$

The product is the biquaternion product (for several qubits, the product in $\mathbb{B}^{\otimes n}$). Because that product is associative, a circuit is well defined without any bracketing convention: it is one element, the ordered product of its gates, and its action is a single conjugation by that element. The identity gate is $e_0$; the inverse of $\tilde{U}$ is $\tilde{U}^\dagger = \tilde{U}^{-1}$; and the set of gates is closed under the product, which is the statement that the gate group is a group.

Two remarks make the product law precise.

First, the order is the reverse of the circuit reading. If a diagram is read left to right, the algebraic product is written right to left, as above. This is the standard convention for operator composition and carries no biquaternion-specific content.

Second, because the map $\tilde{U}\mapsto\Phi_{\tilde{U}}$ has kernel $U(1)$, the product law holds at the level of gates but the algebraic identity of representatives may fail by a central phase. If $\tilde{V}\tilde{U} = e^{i\phi}\tilde{W}$, then $\Phi_{\tilde{V}}\circ\Phi_{\tilde{U}} = \Phi_{\tilde{W}}$ nevertheless. Circuit identities in the framework are therefore identities **up to a central phase**, and the phase is unobservable.

### Worked Identities

The Hadamard conjugation of the Pauli gates is a compact illustration. The identity $\tilde{H}\tilde{Z}\tilde{H} = \tilde{X}$ already displayed says that the circuit "Hadamard, then $Z$, then Hadamard" realises the $X$ gate:

$$
\Phi_{\tilde{H}}\circ\Phi_{\tilde{Z}}\circ\Phi_{\tilde{H}} = \Phi_{\tilde{H}\tilde{Z}\tilde{H}} = \Phi_{\tilde{X}} .
$$

The identity $\tilde{H}\tilde{X}\tilde{H} = \tilde{Z}$ gives the reverse. These are exact as algebra identities, and they hold as gate identities. The identity $\tilde{H}\tilde{Y}\tilde{H} = -\tilde{Y}$ holds only up to the central phase $-e_0$; as gates, $\Phi_{\tilde{H}}\circ\Phi_{\tilde{Y}}\circ\Phi_{\tilde{H}} = \Phi_{\tilde{Y}}$.

Non-commuting gates give distinct circuits. For example, the two orderings of a Hadamard and a controlled gate differ, as they do in standard circuit notation; the framework expresses this as the failure of $\tilde{H}\otimes e_0$ and the controlled gate to commute in $\mathbb{B}\otimes\mathbb{B}$. Composition is the algebra product, and the algebra is non-commutative.

### The Clifford Group as an Algebraic Normaliser

The **single-qubit Pauli group** is the sixteen-element set

$$
\mathcal{P} = \{\pm e_0,\ \pm i e_0,\ \pm e_k,\ \pm i e_k : k=1,2,3\},
$$

which is closed under the biquaternion product and is the image of the standard Pauli group $\langle X,Y,Z\rangle$ under the isomorphism. The **Clifford group** is its normaliser in the gate group,

$$
\mathcal{C} = \{\tilde{U}\in U(2) : \tilde{U}\,\mathcal{P}\,\tilde{U}^\dagger = \mathcal{P}\},
$$

i.e. the set of gates that permute the Pauli group under conjugation, up to sign. The elementary gates $H$ and $S$ both lie in it, and in fact generate it; this is the biquaternion form of the standard statement that $H$ and $S$ generate the single-qubit Clifford group. Modulo the phase, the conjugation action of the Clifford group on the Bloch sphere is the rotation symmetry group of the octahedron, of order $24$; a direct enumeration of the group generated by the two rotation matrices $R(\tilde{H})$ and $R(\tilde{S})$ returns exactly $24$ distinct rotations. In the algebra, the octahedral symmetry is the symmetry of the Pauli axes $\{\pm i e_1,\pm i e_2,\pm i e_3\}$ that the Clifford gates permute.

The **$T$ gate is not Clifford**. Its conjugation of $\tilde{X}$ produces a rotation by $\pi/4$ about $e_3$, which does not return the Pauli axes to themselves. The standard statement that $\{H,T\}$ generates a dense subgroup of the gate group — the basis of the Solovay–Kitaev universality of single-qubit computation — is inherited unchanged by the reformulation; it is a statement about the group generated by a Hadamard involution and a rotation of order eight, and the biquaternion representatives are $i(e_1+e_3)/\sqrt{2}$ and $\cos(\pi/8)e_0+\sin(\pi/8)e_3$. This article does not re-derive universality; it records where the generators live.

## Multi-Qubit Gates and the Tensor Arena

### The $n$-Qubit Algebra

For $n$ qubits the arena is the tensor product

$$
\mathbb{B}^{\otimes n} \;\cong\; M_{2^n}(\mathbb{C}),
$$

with the trace $\mathrm{Tr}(x\otimes y) = \mathrm{Tr}_{\mathbb{B}}(x)\cdot\mathrm{Tr}_{\mathbb{B}}(y)$, where $\mathrm{Tr}_{\mathbb{B}}(e_0)=2$ and $\mathrm{Tr}_{\mathbb{B}}(e_k)=0$, and with the partial traces $\mathrm{Tr}_1,\mathrm{Tr}_2$ of the companion article on entangled subsystems. A **gate** is a unitary element of $\mathbb{B}^{\otimes n}$, acting on states (Hermitian, positive, trace-one elements of $\mathbb{M}_+^{\otimes n}$) by conjugation. The elementary gates of a circuit are of two kinds: **local gates** $\tilde{U}_1\otimes\tilde{U}_2\otimes\cdots$ on the factors, and **entangling gates**, which are not tensor products.

Local gates on different factors commute, $(\tilde{U}\otimes e_0)(e_0\otimes\tilde{V}) = (e_0\otimes\tilde{V})(\tilde{U}\otimes e_0) = \tilde{U}\otimes\tilde{V}$, so the order of operations on disjoint wires is immaterial — the algebraic statement of the fact that commuting gates may be drawn in either order.

The status of the tensor product is the open question inherited from the companion articles. Everything below is a statement inside $\mathbb{B}^{\otimes n}$ once that algebra is granted; whether it is canonical for the framework is left open, exactly as in the companion article on the Bell basis.

### Controlled Gates

A **controlled gate** is built from the two fundamental objects of the framework: an idempotent on the control factor and a gate on the target factor. Along the control axis $\hat{\mathbf{n}}$, let $\tilde{P}_\pm(\hat{\mathbf{n}}) = \tfrac{1}{2}(e_0 \pm i\hat{\mathbf{n}})$ be the complementary idempotents, and let $\tilde{U}$ be any single-qubit gate. Define

$$
\tilde{C}_{\tilde{U}} = \tilde{P}_+(\hat{\mathbf{n}})\otimes e_0 + \tilde{P}_-(\hat{\mathbf{n}})\otimes \tilde{U} \;\in\; \mathbb{B}\otimes\mathbb{B}.
$$

This is a single element of the two-qubit algebra, and it is unitary:

$$
\tilde{C}_{\tilde{U}}\tilde{C}_{\tilde{U}}^\dagger
= \tilde{P}_+^2\otimes e_0 + \tilde{P}_+\tilde{P}_-\otimes\tilde{U}^\dagger + \tilde{P}_-\tilde{P}_+\otimes\tilde{U} + \tilde{P}_-^2\otimes\tilde{U}\tilde{U}^\dagger
= (\tilde{P}_+ + \tilde{P}_-)\otimes e_0 = e_0\otimes e_0 ,
$$

where the cross terms vanish because $\tilde{P}_+\tilde{P}_- = 0$ and the last step uses the resolution of the identity $\tilde{P}_+ + \tilde{P}_- = e_0$ together with $\tilde{U}\tilde{U}^\dagger = e_0$. The same computation with a general single-qubit $\tilde{U}$ shows that **any** unitary target operation is admitted, so the construction defines $\tilde{C}_{\tilde{U}}$ for every gate $\tilde{U}$.

The unitarity of the controlled gate uses exactly two properties: the idempotents are complementary and orthogonal, and the target element is unitary. It is worth pausing on this, because the same idempotents, used differently, are the operators of an irreversible measurement. The controlled gate is the **coherent** use of an idempotent: the two outcomes are kept, paired with two different target operations, and added inside a single unitary element. The measurement channel, in contrast, adds the two *conjugated states*,

$$
\tilde{\rho} \;\longmapsto\; \tilde{P}_+\tilde{\rho}\tilde{P}_+ + \tilde{P}_-\tilde{\rho}\tilde{P}_- ,
$$

which is a sum of conjugations and not a single conjugation. This is the algebraic distinction between a reversible gate and an irreversible measurement, and it is taken up again in the section on channels.

### CNOT, CZ, and SWAP

With the control axis $\hat{\mathbf{e}}_3$ — the $|0\rangle/|1\rangle$ basis of the control — the standard gates are:

| Gate | Biquaternion representative in $\mathbb{B}\otimes\mathbb{B}$ | Matrix image |
|---|---|---|
| $\mathrm{CNOT}$ | $\tilde{P}_+(\hat{\mathbf{e}}_3)\otimes e_0 + \tilde{P}_-(\hat{\mathbf{e}}_3)\otimes (i e_1)$ | $\lvert 0\rangle\langle 0\rvert\otimes I_2 + \lvert 1\rangle\langle 1\rvert\otimes\sigma_1$ |
| $\mathrm{CZ}$ | $\tilde{P}_+(\hat{\mathbf{e}}_3)\otimes e_0 + \tilde{P}_-(\hat{\mathbf{e}}_3)\otimes (i e_3)$ | $\lvert 0\rangle\langle 0\rvert\otimes I_2 + \lvert 1\rangle\langle 1\rvert\otimes\sigma_3$ |
| $\mathrm{SWAP}$ | $\dfrac{1}{2}\left(e_0\otimes e_0 - e_1\otimes e_1 - e_2\otimes e_2 - e_3\otimes e_3\right)$ | $\tfrac{1}{2}\left(I_4 + \sum_k \sigma_k\otimes\sigma_k\right)$ |

All three were verified to be unitary, Hermitian, and involutive. The CNOT is the controlled-$X$; the CZ is the controlled-$Z$. The SWAP form follows from the standard identity $\mathrm{SWAP} = \tfrac{1}{2}(I\otimes I + \sum_k\sigma_k\otimes\sigma_k)$ together with $e_k\otimes e_k = -(ie_k)\otimes(ie_k) = -\sigma_k\otimes\sigma_k$ under the isomorphism. The SWAP is not a controlled gate but a permutation of the two factors, and it satisfies the standard factor-exchange relation

$$
(\tilde{C}_{12})\,\mathrm{SWAP} = \mathrm{SWAP}\,(\tilde{C}_{21}),
$$

where $\tilde{C}_{12}$ is the CNOT with control on the first qubit and $\tilde{C}_{21}$ the CNOT with control on the second; this too was recomputed. It is the algebraic statement that swapping the qubits converts a control on one into a control on the other.

Two standard circuit identities express the relations among these gates, and both were verified in the tensor algebra:

$$
\mathrm{SWAP} = \tilde{C}_{12}\,\tilde{C}_{21}\,\tilde{C}_{12},
\qquad
\tilde{C}_{12} = (I_2\otimes \tilde{H})\,\mathrm{CZ}\,(I_2\otimes \tilde{H}).
$$

The first is the three-CNOT decomposition of the swap. The second is the conjugation of the CZ into the CNOT by a Hadamard on the target; equivalently, the same identity with the roles of CNOT and CZ exchanged on the other side. Each identity is a statement about the product of unitary elements of $\mathbb{B}\otimes\mathbb{B}$: the circuits are equal because the algebra products are equal.

## A Simple Circuit: Preparing a Bell State

The composition law is best seen in a circuit that produces something the algebra names. Consider two qubits prepared in the pure state

$$
\tilde{\rho}_0 = \tilde{P}_+(\hat{\mathbf{e}}_3)\otimes\tilde{P}_+(\hat{\mathbf{e}}_3) ,
$$

the biquaternion idempotent corresponding to $|00\rangle$. Apply the Hadamard to the first qubit and then the CNOT with the first qubit as control. As a circuit, the operation is the product

$$
\tilde{W} = \tilde{C}_{\tilde{X}}\,\left(\tilde{H}\otimes e_0\right), \qquad \tilde{C}_{\tilde{X}} = \tilde{P}_+(\hat{\mathbf{e}}_3)\otimes e_0 + \tilde{P}_-(\hat{\mathbf{e}}_3)\otimes (i e_1),
$$

and the output state is $\tilde{W}\tilde{\rho}_0\tilde{W}^\dagger$, a single conjugation because $\tilde{W}$ is a single gate.

**Step one: the Hadamard.** Since $\tilde{H}$ is Hermitian and $\tilde{H}^2 = e_0$, the conjugation of the first factor gives

$$
\tilde{H}\,\tilde{P}_+(\hat{\mathbf{e}}_3)\,\tilde{H} = \tilde{P}_+(\hat{\mathbf{e}}_1),
$$

computed directly from the quaternion product. So after the Hadamard the state is

$$
\left(\tilde{H}\otimes e_0\right)\tilde{\rho}_0\left(\tilde{H}\otimes e_0\right) = \tilde{P}_+(\hat{\mathbf{e}}_1)\otimes\tilde{P}_+(\hat{\mathbf{e}}_3),
$$

the product state $|{+}\rangle|0\rangle$.

**Step two: the CNOT.** Write $\tilde{A} = \tilde{P}_+(\hat{\mathbf{e}}_1)$, $\tilde{B} = \tilde{P}_+(\hat{\mathbf{e}}_3)$, $\tilde{P}_\pm = \tilde{P}_\pm(\hat{\mathbf{e}}_3)$, and $\tilde{C} = \tilde{C}_{\tilde{X}}$. Since $\tilde{C} = \tilde{C}^\dagger$ and $\tilde{C}^2 = e_0\otimes e_0$, conjugation by $\tilde{C}$ expands into four terms:

$$
\tilde{C}(\tilde{A}\otimes\tilde{B})\tilde{C}
= \tilde{P}_+\tilde{A}\tilde{P}_+ \otimes \tilde{B}
+ \tilde{P}_+\tilde{A}\tilde{P}_- \otimes \tilde{B}\,(ie_1)
+ \tilde{P}_-\tilde{A}\tilde{P}_+ \otimes (ie_1)\,\tilde{B}
+ \tilde{P}_-\tilde{A}\tilde{P}_- \otimes (ie_1)\,\tilde{B}\,(ie_1).
$$

The four projectors evaluate, using $\tilde{P}_\pm\tilde{A}\tilde{P}_\pm = \tfrac{1}{2}\tilde{P}_\pm$ (the transition probability $\tfrac{1}{2}(1 + \hat{\mathbf{e}}_3\cdot\hat{\mathbf{e}}_1) = \tfrac12$) and the Peirce components

$$
\tilde{P}_+\tilde{A}\tilde{P}_- = \tfrac{1}{4}\left(ie_1 - e_2\right),
\qquad
\tilde{P}_-\tilde{A}\tilde{P}_+ = \tfrac{1}{4}\left(ie_1 + e_2\right),
$$

while the target products are $\tilde{B}(ie_1) = \tfrac12(ie_1 - e_2)$ and $(ie_1)\tilde{B} = \tfrac12(ie_1 + e_2)$, and $(ie_1)\tilde{B}(ie_1) = \tilde{P}_-(\hat{\mathbf{e}}_3)$. Substituting,

$$
\tilde{C}(\tilde{A}\otimes\tilde{B})\tilde{C}
= \tfrac{1}{4}\left[e_0\otimes e_0 - e_1\otimes e_1 + e_2\otimes e_2 - e_3\otimes e_3\right].
$$

The right-hand side is the **Bell idempotent** $P_\epsilon$ of the companion article on the Bell basis, with sign pattern $\epsilon = (-1,+1,-1)$, which is the idempotent of $|\Phi^+\rangle$. The identification was verified independently by mapping both sides to $M_4(\mathbb{C})$: the biquaternion element equals $\tfrac{1}{2}(|00\rangle+|11\rangle)(\langle 00|+\langle 11|)$.

The whole circuit is thus the single element $\tilde{W} = \tilde{C}_{\tilde{X}}(\tilde{H}\otimes e_0)$ of $\mathbb{B}\otimes\mathbb{B}$, and its output is

$$
\tilde{W}\left[\tilde{P}_+(\hat{\mathbf{e}}_3)\otimes\tilde{P}_+(\hat{\mathbf{e}}_3)\right]\tilde{W}^\dagger
= \tfrac{1}{4}\left[e_0\otimes e_0 - e_1\otimes e_1 + e_2\otimes e_2 - e_3\otimes e_3\right].
$$

The output is not a product of idempotents; its partial trace is $\tfrac12 e_0$, the maximally mixed qubit state, by the computation of the companion article. The circuit has converted a product state into a maximally entangled state by a single conjugation, and every step of the conversion is an algebraic product and conjugation in $\mathbb{B}\otimes\mathbb{B}$.

## Gates and the Irreversible Channels

The read list for this article closes with *Quantum Channels and the Reversible/Irreversible Dichotomy*, and the contrast between the two is the conceptual content of the gate formalism.

A **state map** is a completely positive, trace-preserving map on $\mathbb{M}_+$, extended complex-linearly to $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ and written in Kraus form $\Phi(\tilde{\rho}) = \sum_l \tilde{K}_l\tilde{\rho}\tilde{K}_l^\dagger$ with $\sum_l\tilde{K}_l^\dagger\tilde{K}_l = e_0$. The dichotomy is:

$$
\text{reversible} \quad\Longleftrightarrow\quad \text{Kraus rank one} \quad\Longleftrightarrow\quad \Phi = \Phi_{\tilde{U}}\ \text{for a unitary } \tilde{U} \quad\Longleftrightarrow\quad \Phi \text{ is a gate.}
$$

Equivalently, a channel is a gate if and only if it preserves purity, and if and only if it is an inner automorphism of the algebra. Three consequences organise the distinction.

**Closure.** The composition of two gates is a gate, because the product of two unitaries is unitary. Hence **a circuit built only from gates is a gate**: it is one element, it has Kraus rank one, and it is invertible. The inverse circuit is the product of the inverses in the reverse order, which in the algebra is just $\tilde{W}^\dagger$. The Bell-preparation circuit above is reversible for exactly this reason, even though it creates entanglement: entanglement is not irreversibility.

**Irreversibility is a sum.** A channel is irreversible precisely when its Kraus rank is at least two, i.e. when it is a *sum* of conjugations rather than one conjugation. The canonical example is **dephasing** along $\hat{\mathbf{n}}$,

$$
\Phi^{\mathrm{deph}}_p(\tilde{\rho}) = (1-p)\tilde{\rho} + p\left(\tilde{P}_+\tilde{\rho}\tilde{P}_+ + \tilde{P}_-\tilde{\rho}\tilde{P}_-\right),
$$

which acts on the Bloch vector as $\mathbf{r}\mapsto(1-p)\mathbf{r} + p(\hat{\mathbf{n}}\cdot\mathbf{r})\hat{\mathbf{n}}$. Its Bloch matrix is $\operatorname{diag}(1-p,1-p,1)$ in the eigenbasis of $\hat{\mathbf{n}}$, of determinant $(1-p)^2$. A gate acts by a rotation, whose Bloch matrix has determinant $+1$ and is orthogonal; hence for $0<p\leq 1$ the dephasing map **is not a gate**, and no representative of it is a single unitary conjugation. It is the canonical irreversible channel, and the companion article on decoherence analyses its effect on idempotency in detail.

**The same idempotents, used coherently and incoherently.** The sharpest contrast is between two objects built from the same complementary idempotents:

$$
\tilde{C}_{\tilde{U}} = \tilde{P}_+\otimes e_0 + \tilde{P}_-\otimes\tilde{U} \quad\text{(a gate)},
\qquad
\Phi(\tilde{\rho}) = \tilde{P}_+\tilde{\rho}\tilde{P}_+ + \tilde{P}_-\tilde{\rho}\tilde{P}_- \quad\text{(a channel)}.
$$

In the first, the idempotents sit inside a **single unitary element** and the sum is over the two control branches; both branches survive, the coherence between them is retained, and the result is reversible. In the second, the state itself is replaced by the sum of its two projected pieces; the coherence between the branches is discarded, the map contracts the Bloch ball, and the result is irreversible. This is the algebraic content of the familiar statement that a controlled gate is a measurement made coherent: the difference is not in the idempotents but in whether the sum is taken inside one element or between two conjugated states. It is the same reversible/irreversible dichotomy the framework already expresses as unitary versus idempotent acting elements.

The channel set is convex, with the gates among its extreme points; the companion article establishes this and the associated Stinespring picture, in which every irreversible channel is the reduction of a reversible evolution on a larger system after the environment is discarded. A circuit that contains a measurement, or a dephasing step, has left the gate group and is a general channel; it may still be drawn as a circuit, but it is no longer a single element of $\mathbb{B}^{\otimes n}$ and no longer invertible within the channels.

## What the Reformulation Does and Does Not Claim

**It does provide:**

- A single algebraic home for the objects of quantum computation: states are positive trace-one elements of $\mathbb{M}_+^{\otimes n}$, gates are unitary elements of $\mathbb{B}^{\otimes n}$, and a circuit is their product.
- The action of a gate as rotor conjugation, and reversibility as the property $\tilde{U}\tilde{U}^\dagger = e_0$ that makes the acting element unitary.
- The standard gate set in explicit biquaternion form: the Pauli and Hadamard gates as Hermitian unitaries in $\mathbb{M}_+$, and the phase and $T$ gates as rotations in $\mathbb{H}_{\mathbb{B}}$, with the global phase sitting in $\mathbb{C}_{\mathbb{B}}$ and acting trivially.
- The controlled gate as an algebraic construction from complementary idempotents and a target gate, and the reading of the controlled gate as the coherent use of an idempotent, in contrast with the measure-and-forget channel.
- The Clifford group as the normaliser of the Pauli group in the gate group, and its octahedral rotation image.
- The clean statement of the reversible/irreversible split as Kraus rank one versus higher rank, which is the algebra's own dichotomy rather than an additional postulate.

**It does not claim:**

- A new theory of quantum computation. The formalism is standard quantum information theory in biquaternion notation, and it is empirically empty by itself.
- A re-derivation of the universality theorems. The statement that $\{H,T\}$ generates a dense subgroup is inherited; the article records the generators but proves no approximation theorem.
- Any claim about fault tolerance, error correction, or resource theories; none of these is developed here.
- A resolution of the measurement problem. The controlled-gate-versus-channel contrast states the algebraic difference precisely; it does not say why a physical circuit contains one rather than the other.
- A justification of the tensor-product arena, whose status is the open question inherited from the companion articles.

## Open Questions

**1. The two groups in one algebra.** The gate group $U(2)$ and the Lorentz group $SL(2,\mathbb{C})$ both act on the framework, on $\mathbb{M}_+$ and $\mathbb{M}_-$ respectively, by the same form of conjugation. A boost is a rotor on $\mathbb{M}_-$ but not a gate on $\mathbb{M}_+$; a gate is unitary on $\mathbb{M}_+$ but has no norm-form-preserving interpretation on $\mathbb{M}_-$. What is the precise sense in which a physical operation can be one and not the other, and is there any process that is naturally described by both?

**2. The measurement as a gate.** Every channel is a generalized measurement followed by a state transformation. The controlled gate shows that an idempotent can be used coherently, and dephasing shows that it can be used incoherently. Is there an algebraic criterion, beyond Kraus rank, that distinguishes the two uses in terms of the elements involved?

**3. Universality in the algebra.** The density of $\langle H, T\rangle$ is a statement about two specific elements of $\mathbb{B}$. Does the biquaternion framework give a natural reason for the existence of dense finitely generated subgroups of the gate group, or is this the same statement in different notation?

**4. The tensor product.** As in the companion article on the Bell basis, whether $\mathbb{B}^{\otimes n}$ is canonical for the framework or requires additional structure is unresolved. Multi-qubit gates inherit the contingency.

**5. The $T$ gate and the non-compact directions.** The gates generated by $H$ and $T$ lie, modulo phase, in the compact subgroup $SU(2)$ of $SL(2,\mathbb{C})$. The non-compact directions of the algebra — the boosts — are not reachable as gates. Is there any operation on the informational sector that involves them, or is the gate group necessarily compact?

**6. Empirical content.** As everywhere in the framework, a reformulation of gates and circuits is empirically empty. What, if anything, distinguishes it from standard quantum computation is the central open question.

## Summary

A gate in the biquaternion framework is a **unitary element** $\tilde{U}\in\mathbb{B}$ with $\tilde{U}\tilde{U}^\dagger = e_0$, acting on a state $\tilde{\rho}\in\mathbb{M}_+$ by **rotor conjugation** $\tilde{\rho}\mapsto\tilde{U}\tilde{\rho}\tilde{U}^\dagger$. This is exactly the class of channels of Kraus rank one, and exactly the reversible, purity-preserving state maps. The gate group is $U(2) = U(1)\cdot SU(2)$: every gate is a central phase times a rotation, and the phase is unobservable, so the effective group is $PU(2)\cong SO(3)$ acting on the Bloch ball. The condition $\tilde{U}\tilde{U}^\dagger = e_0$ is **not** the unit-norm-form condition $\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$ of the Lorentz rotors: a boost is a rotor on $\mathbb{M}_-$ but not a gate on $\mathbb{M}_+$.

The standard single-qubit gate set has explicit representatives: the Pauli gates are $\tilde{X}=ie_1$, $\tilde{Y}=ie_2$, $\tilde{Z}=ie_3$; the Hadamard is $\tilde{H}=\tfrac{i}{\sqrt2}(e_1+e_3)$; the phase and $T$ gates are the rotations $\tfrac{1}{\sqrt2}(e_0+e_3)$ and $\cos\tfrac{\pi}{8}e_0+\sin\tfrac{\pi}{8}e_3$; a general gate is $e^{i\phi}(\cos\tfrac{\theta}{2}e_0+\sin\tfrac{\theta}{2}\hat{\mathbf{n}})$. Apart from the identity gate, the Hermitian gates are the $\pi$-rotations $\pm i\hat{\mathbf{n}}$; the Pauli and Hadamard gates are of this type, the phase and $T$ gates are not.

**Composition** is the algebra product: applying $\tilde{U}$ then $\tilde{V}$ gives $\tilde{V}\tilde{U}$, and the whole circuit is a single element whose action is a single conjugation. The Pauli group is the sixteen-element set $\{\pm e_0,\pm ie_0,\pm e_k,\pm ie_k\}$, and the Clifford group is its normaliser in the gate group; $H$ and $S$ generate it, and its image in $PU(2)$ is the octahedral rotation group of order $24$.

In the **multi-qubit** arena $\mathbb{B}^{\otimes n}\cong M_{2^n}(\mathbb{C})$, the controlled gate is $\tilde{C}_{\tilde{U}} = \tilde{P}_+(\hat{\mathbf{n}})\otimes e_0 + \tilde{P}_-(\hat{\mathbf{n}})\otimes\tilde{U}$, unitary by the complementarity of the idempotents and the unitarity of $\tilde{U}$. The CNOT, CZ, and SWAP gates have explicit representatives, and the standard circuit identities hold as algebra identities. A worked circuit — Hadamard then CNOT on two qubits — produces the Bell idempotent $\tfrac14(e_0\otimes e_0 - e_1\otimes e_1 + e_2\otimes e_2 - e_3\otimes e_3)$ from a product state by a single conjugation.

The **contrast with the irreversible channels** is the Kraus-rank dichotomy. A circuit of gates is a gate, hence reversible; inserting a measurement or a dephasing step makes it a channel of Kraus rank at least two, represented by a *sum* of conjugations rather than one. The controlled gate and the measurement channel use the same idempotents; the difference is whether the sum over the outcomes is taken inside a single unitary element (coherent, reversible) or between conjugated states (incoherent, irreversible). The reformulation is standard quantum information theory in biquaternion notation: it makes the algebraic location of each circuit ingredient explicit without adding physical content.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{M}_+$ | Hermitian subspace (states, observables) |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (generators of reversible evolution) |
| $\mathbb{C}_{\mathbb{B}}$ | Complex subspace (center); home of the global phase |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace (rotation rotors, $SU(2)$) |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\tilde{\rho}=\tfrac12(e_0+i\mathbf{r})$ | State of a qubit |
| $\tilde{P}_\pm(\hat{\mathbf{n}})=\tfrac12(e_0\pm i\hat{\mathbf{n}})$ | Complementary idempotents |
| $\tilde{U}\tilde{U}^\dagger=e_0$ | Gate (matrix-unitary element); $U(2)$ |
| $\tilde{\Lambda}\bar{\tilde{\Lambda}}=e_0$ | Lorentz rotor (unit norm form); $SL(2,\mathbb{C})$, not a gate |
| $\Phi_{\tilde{U}}(\tilde{\rho})=\tilde{U}\tilde{\rho}\tilde{U}^\dagger$ | Rotor conjugation (gate action) |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula (Born rule) |
| $\tilde{X}=ie_1,\ \tilde{Y}=ie_2,\ \tilde{Z}=ie_3$ | Pauli gates |
| $\tilde{H}=\tfrac{i}{\sqrt2}(e_1+e_3)$ | Hadamard gate |
| $\tilde{S}=\tfrac{1}{\sqrt2}(e_0+e_3),\ \tilde{T}=\cos\tfrac{\pi}{8}e_0+\sin\tfrac{\pi}{8}e_3$ | Phase and $T$ gates |
| $\tilde{R}_{\hat{\mathbf{n}}}(\theta)=\cos\tfrac{\theta}{2}e_0+\sin\tfrac{\theta}{2}\hat{\mathbf{n}}$ | General rotation gate |
| $\mathcal{P}=\{\pm e_0,\pm ie_0,\pm e_k,\pm ie_k\}$ | Pauli group (16 elements) |
| $\tilde{C}_{\tilde{U}}=\tilde{P}_+\otimes e_0+\tilde{P}_-\otimes\tilde{U}$ | Controlled gate |
| $\mathrm{CNOT}=\tilde{P}_+(\hat{\mathbf{e}}_3)\otimes e_0+\tilde{P}_-(\hat{\mathbf{e}}_3)\otimes(ie_1)$ | Controlled-$X$ |
| $\mathrm{SWAP}=\tfrac12(e_0\otimes e_0-\sum_k e_k\otimes e_k)$ | Swap gate |
| $\Phi(\tilde{\rho})=\sum_l\tilde{K}_l\tilde{\rho}\tilde{K}_l^\dagger$ | Kraus representation of a channel |
| $\Phi^{\mathrm{deph}}_p$ | Dephasing channel (irreversible, not a gate) |

## Further Reading

- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the standard gate set, circuit identities, the Clifford group, and the Solovay–Kitaev theorem.
- John Preskill, *Quantum Computation* (California Institute of Technology lecture notes), for the circuit model, universality, and the stabiliser formalism.
- K. Kraus, *States, Effects, and Operations* (Springer, 1983), and M.-D. Choi, "Completely positive linear maps on complex matrices," *Linear Algebra and its Applications* **10** (1975) 285–290, for the Kraus representation and the rank criterion of reversibility.
- M. B. Ruskai, S. Szarek, and E. Werner, "An analysis of completely-positive trace-preserving maps on $2\times2$ matrices," *Linear Algebra and its Applications* **347** (2002) 159–187, for the Bloch-ball picture of qubit channels and the geometry of the reversible maps among them.
- Daniel Gottesman, "The Heisenberg representation of quantum computers" (1998), for the stabiliser formalism and the Clifford group in the Pauli normaliser picture.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the spin-1/2 formalism underlying the gate representatives.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), and Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of rotations used here.
- The companion articles of this series: *Introduction to the Biquaternion Universe*, *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, *Quantum Mechanics in Biquaternionic Form*, *Spin-1/2 Quantum Mechanics in Biquaternionic Form*, *Quantum Channels and the Reversible/Irreversible Dichotomy*, *The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$*, and *Decoherence as Idempotent Projection*.
