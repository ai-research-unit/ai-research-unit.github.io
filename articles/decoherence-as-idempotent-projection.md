# __Decoherence as Idempotent Projection__

## Introduction

The biquaternion framework identifies the **pure states** of a qubit with the **idempotents** of the Hermitian subspace $\mathbb{M}_+$: those elements $\tilde{P}$ satisfying $\tilde{P}^2 = \tilde{P}$. A mixed state is a positive trace-one element that is *not* idempotent, and the amount by which it fails to be idempotent is a single scalar, the scalar part of $\tilde{\rho}^2 - \tilde{\rho}$. **Decoherence** — the loss of the phase relations between the components of a superposition — is therefore, in this language, the deformation of an idempotent into a non-idempotent positive trace-one element. That deformation is the subject of this article.

The title couples "idempotent" to "projection", and the coupling is not innocent. Two different objects can be called an idempotent projection, and they are not the same:

1. An **idempotent element** of the algebra: an operator $\tilde{P}$ with $\tilde{P}^2 = \tilde{P}$. Its action on a state, $\tilde{\rho} \mapsto \tilde{P}\tilde{\rho}\tilde{P}$ (followed by normalization), is a projective measurement. A pure state is such an element, by definition.
2. An **idempotent channel**: a map $\Phi$ on the state space with $\Phi \circ \Phi = \Phi$. This is a statement about an *operation*, not about an element.

A pure state satisfies the first condition by definition. The dephasing channel satisfies the second condition only in one limit, at full strength. For partial dephasing, dephasing twice is *not* the same as dephasing once: $\Phi_p \circ \Phi_p = \Phi_{2p - p^2} \neq \Phi_p$ whenever $0 < p < 1$. Since decoherence as a physical process is generically partial, the honest reading of the title is:

> **Decoherence destroys the idempotency of a state, and it is itself an idempotent projection only in the fully decohered limit. At every intermediate strength it is a contractive, information-losing channel, not a projection.**

Making that distinction exact — saying precisely where the projection metaphor holds and where it fails — is the spine of this article. The framework supplies the vocabulary for the distinction; it does not license the stronger claim that the title, read naively, would make.

The article applies the dephasing channel derived in the companion article *Quantum Channels and the Reversible/Irreversible Dichotomy*. It does not re-derive that channel: the Kraus form, the Bloch-vector formula, and the limiting cases are taken from that article and used. The treatment is operational throughout: the states and channels are elements of and maps on $\mathbb{M}_+$, in the sense of *Quantum Mechanics in Biquaternionic Form*, and the interpretive hypothesis that $\mathbb{M}_+$ is a distinct physical sector is not required for anything below. The relation to *The Quantum–Classical Divide in the Biquaternion Framework* is taken up in a dedicated section.

The article proceeds as follows: the idempotent characterization of pure states and the mixedness scalar; the dephasing channel and its effect on idempotency; the trajectory from the Bloch sphere into the ball; the two-sided answer to the title's question; the pointer basis and einselection; the relation to the quantum–classical divide; and an explicit account of what the framework does and does not explain.

## The Idempotent and the State

A state of the informational sector is an element of the Hermitian subspace

$$
\tilde{\rho} = \tfrac{1}{2}\left(e_0 + i\,\mathbf{r}\right), \qquad \mathbf{r} \in \mathbb{R}^3,
$$

with positivity equivalent to $|\mathbf{r}| \leq 1$. The states form the **Bloch ball**; the trace is $\mathrm{Tr}(\tilde{\rho}) = 2\,\mathrm{Sc}(\tilde{\rho}) = 1$.

A state is **pure** if and only if it is an idempotent:

$$
\tilde{\rho}^2 = \tilde{\rho} \qquad \Longleftrightarrow \qquad |\mathbf{r}| = 1 .
$$

For $\mathbf{r} \neq 0$ the pure state is the rank-one projector $\tilde{P}_+(\hat{\mathbf{r}}) = \tfrac{1}{2}(e_0 + i\hat{\mathbf{r}})$, with $\hat{\mathbf{r}} = \mathbf{r}/|\mathbf{r}|$ a unit pure real quaternion; the complementary idempotent $\tilde{P}_-(\hat{\mathbf{r}}) = \tfrac{1}{2}(e_0 - i\hat{\mathbf{r}})$ corresponds to the antipodal point. The pure states are the boundary sphere of the Bloch ball, which is also the trace-one slice of the future light cone of the norm form, since

$$
N(\tilde{\rho}) = \tfrac{1}{4}\left(1 - |\mathbf{r}|^2\right)e_0 .
$$

For a general state, a direct expansion gives

$$
\tilde{\rho}^2 = \tfrac{1}{4}\left(\left(1 + |\mathbf{r}|^2\right)e_0 + 2i\,\mathbf{r}\right),
$$

and therefore the **deviation from idempotency** is a pure scalar:

$$
\tilde{\rho}^2 - \tilde{\rho} = \tfrac{1}{4}\left(|\mathbf{r}|^2 - 1\right)e_0 .
$$

This is the central identity for the present subject. It says that all the mixedness of a qubit state is carried by a single real number, $\mathrm{Sc}(\tilde{\rho}^2 - \tilde{\rho}) = \tfrac14(|\mathbf{r}|^2 - 1) \leq 0$, which vanishes exactly on the pure states. Equivalently, the **purity** is

$$
\mathrm{Tr}(\tilde{\rho}^2) = \tfrac{1}{2}\left(1 + |\mathbf{r}|^2\right),
$$

so that purity and idempotency are the same condition: $\mathrm{Tr}(\tilde{\rho}^2) = 1 \Leftrightarrow \tilde{\rho}^2 = \tilde{\rho}$.

In these terms, decoherence is not the destruction of a vector in a Hilbert space, nor the diagonalization of a matrix by fiat. It is a definite algebraic deformation: it moves the scalar $\mathrm{Sc}(\tilde{\rho}^2 - \tilde{\rho})$ away from zero, equivalently shrinks $|\mathbf{r}|$ below one, equivalently drives the state off the zero-divisor cone of $\mathbb{M}_+$ and into its interior. The pure state was an idempotent; the decohered state is a positive trace-one element that is not. What remains to be seen is what kind of operation performs this deformation, and in what sense, if any, that operation is itself a projection.

## The Dephasing Channel

The companion article *Quantum Channels and the Reversible/Irreversible Dichotomy* constructs the canonical coherence-destroying channel and works out its properties. We recall its results and apply them.

Let $\hat{\mathbf{n}}$ be a unit pure real quaternion and let

$$
\tilde{P}_+(\hat{\mathbf{n}}) = \tfrac{1}{2}\left(e_0 + i\hat{\mathbf{n}}\right), \qquad
\tilde{P}_-(\hat{\mathbf{n}}) = \tfrac{1}{2}\left(e_0 - i\hat{\mathbf{n}}\right)
$$

be the complementary idempotents along $\hat{\mathbf{n}}$. For $p \in [0,1]$ the **dephasing channel** along $\hat{\mathbf{n}}$ is

$$
\Phi^{\mathrm{deph}}_p(\tilde{\rho})
= (1-p)\,\tilde{\rho}
+ p\left(\tilde{P}_+\,\tilde{\rho}\,\tilde{P}_+ + \tilde{P}_-\,\tilde{\rho}\,\tilde{P}_-\right).
$$

It is completely positive and trace preserving, with Kraus operators

$$
\tilde{K}_0 = \sqrt{1-p}\,e_0, \qquad
\tilde{K}_1 = \sqrt{p}\,\tilde{P}_+(\hat{\mathbf{n}}), \qquad
\tilde{K}_2 = \sqrt{p}\,\tilde{P}_-(\hat{\mathbf{n}}),
$$

whose normalization $\sum_l \tilde{K}_l^\dagger \tilde{K}_l = (1-p)e_0 + p(\tilde{P}_+ + \tilde{P}_-) = e_0$ holds because the idempotents are Hermitian and complementary. The channel is **unital**: it fixes the maximally mixed state $\tilde{\rho} = \tfrac12 e_0$, so it is not a depolarizing map that pushes states toward the center; it is a map that pushes them toward an *axis*.

On the Bloch vector the channel acts by

$$
\boxed{\;\mathbf{r} \;\longmapsto\; \mathbf{r}' = (1-p)\,\mathbf{r} + p\,(\hat{\mathbf{n}}\cdot\mathbf{r})\,\hat{\mathbf{n}}.\;}
$$

The component of $\mathbf{r}$ along $\hat{\mathbf{n}}$ is untouched; the transverse component is multiplied by $1-p$. In the eigenbasis of $\hat{\mathbf{n}}$, this is exactly the statement that the diagonal entries of the density matrix — the **populations** — are preserved, while the off-diagonal entries — the **coherences** — are scaled by $1-p$. Equivalently, the coherence is the pair of transverse Bloch components, which are the expectation values $\mathrm{Tr}(\tilde{\rho}\,i e_k)$ of the two traceless observables orthogonal to $\hat{\mathbf{n}}$.

### Composition, and the Failure of Idempotency

The channel's effect on the Bloch vector is linear in $\mathbf{r}$, with eigenvector $\hat{\mathbf{n}}$ of eigenvalue $1$ and two-dimensional transverse eigenspace of eigenvalue $1-p$. Composing two dephasing channels along the same axis therefore multiplies the transverse eigenvalues:

$$
\Phi^{\mathrm{deph}}_p \circ \Phi^{\mathrm{deph}}_q = \Phi^{\mathrm{deph}}_{p + q - pq},
$$

since $1 - (p+q-pq) = (1-p)(1-q)$. In particular, for equal strengths,

$$
\Phi^{\mathrm{deph}}_p \circ \Phi^{\mathrm{deph}}_p = \Phi^{\mathrm{deph}}_{2p - p^2}.
$$

Hence

$$
\Phi^{\mathrm{deph}}_p \text{ is idempotent} \quad \Longleftrightarrow \quad 2p - p^2 = p \quad \Longleftrightarrow \quad p \in \{0,1\}.
$$

Only the identity ($p=0$) and **full dephasing** ($p=1$) are idempotent. Every intermediate strength is not. This is the precise sense in which the title's phrase has to be qualified. Dephasing once is not the same as dephasing twice unless the dephasing is complete; dephasing twice is dephasing harder, with effective strength $2p - p^2 > p$. The operation is a **contraction** toward the pointer axis, and a contraction is not a projection.

The same conclusion in continuous time: if the coherence decays exponentially, $1 - p(t) = e^{-\Gamma t}$ with rate $\Gamma$, then the channels form a one-parameter semigroup,

$$
\Phi^{\mathrm{deph}}_{p(t_1)} \circ \Phi^{\mathrm{deph}}_{p(t_2)} = \Phi^{\mathrm{deph}}_{p(t_1 + t_2)},
$$

and the semigroup is idempotent only at the two ends, $t = 0$ and $t = \infty$. Physical decoherence always sits somewhere in between.

### The Fully Dephased Limit

At $p = 1$ the channel becomes

$$
\Phi^{\mathrm{deph}}_1(\tilde{\rho}) = \tfrac{1}{2}\left(e_0 + i\,(\hat{\mathbf{n}}\cdot\mathbf{r})\,\hat{\mathbf{n}}\right).
$$

Its image is the **diameter** of the Bloch ball along $\hat{\mathbf{n}}$: the set of states with $\mathbf{r} \parallel \hat{\mathbf{n}}$. It is non-unitary and it is idempotent, $(\Phi^{\mathrm{deph}}_1)^2 = \Phi^{\mathrm{deph}}_1$. It is also **measure-and-forget**: measuring the observable $\alpha = i\hat{\mathbf{n}}$ and discarding the outcome leaves precisely

$$
p_+\,\tilde{P}_+ + p_-\,\tilde{P}_- = \Phi^{\mathrm{deph}}_1(\tilde{\rho}),
\qquad
p_\pm = \mathrm{Tr}(\tilde{P}_\pm \tilde{\rho}) = \tfrac12\left(1 \pm \hat{\mathbf{n}}\cdot\mathbf{r}\right),
$$

the classical mixture of the two pointer outcomes. Full dephasing is a non-selective measurement: it records the populations $p_\pm$ and destroys the coherences, but it does not select one of the two outcomes. The output is a mixture, not a pure state.

## From the Bloch Sphere into the Ball

The trajectory picture is now immediate from the Bloch formula. Take a pure state with Bloch vector $\mathbf{r}_0$, $|\mathbf{r}_0| = 1$, and write $r_\parallel = \hat{\mathbf{n}}\cdot\mathbf{r}_0$, $\mathbf{r}_\perp = \mathbf{r}_0 - r_\parallel\hat{\mathbf{n}}$. Under repeated or continuous dephasing along $\hat{\mathbf{n}}$,

$$
\mathbf{r}(t) = r_\parallel\,\hat{\mathbf{n}} + e^{-\Gamma t}\,\mathbf{r}_\perp .
$$

The path is a straight line, perpendicular to the pointer axis, from the surface point $\mathbf{r}_0$ to the axial point $r_\parallel \hat{\mathbf{n}}$. It begins on the Bloch sphere and enters the ball immediately. The squared radius,

$$
|\mathbf{r}(t)|^2 = r_\parallel^2 + e^{-2\Gamma t}\,r_\perp^2,
$$

decreases monotonically to $r_\parallel^2$, so by the purity formula the purity $\mathrm{Tr}(\tilde{\rho}^2) = \tfrac12(1 + |\mathbf{r}|^2)$ decreases monotonically from $1$ toward $\tfrac12(1 + r_\parallel^2)$. Correspondingly the state's deviation from idempotency,

$$
\mathrm{Sc}\left(\tilde{\rho}(t)^2 - \tilde{\rho}(t)\right) = \tfrac14\left(|\mathbf{r}(t)|^2 - 1\right),
$$

descends from $0$ to $\tfrac14(r_\parallel^2 - 1) \leq 0$. The spectrum $\lambda_\pm = \tfrac12(1 \pm |\mathbf{r}(t)|)$ widens from the pure pair $(1,0)$, and the von Neumann entropy

$$
S(\tilde{\rho}) = -\lambda_+\log\lambda_+ - \lambda_-\log\lambda_-,
$$

which is a decreasing function of $|\mathbf{r}|$, increases strictly for any state with $r_\perp \neq 0$.

Two features of this trajectory matter for the projection question. First, the state leaves the sphere unless $r_\perp = 0$, i.e., unless it was already in the pointer basis. A generic pure state becomes mixed, and the idempotent it started as is deformed into a non-idempotent element; the only idempotents that survive full dephasing are the two pointer states $\tilde{P}_\pm(\hat{\mathbf{n}})$, at $r_\parallel = \pm1$. Second, the trajectory has a limit but the limit is reached only asymptotically: for every finite $t$ with $0 < e^{-\Gamma t} < 1$, the transverse component is nonzero and the state is not in the image of the fully dephasing map. The "projection" onto the pointer axis is the $t \to \infty$ endpoint of a contraction, not an operation performed at any finite time.

At full strength $p=1$, and only then, the contraction is total: the transverse component is annihilated, the image is the pointer diameter, and the map fixes its image pointwise. That is the precise sense in which the end product of complete decoherence is a projection of the Bloch ball onto a diameter. For $0 < p < 1$, the map is an *affine contraction toward that diameter*: its image is a squashed ellipsoid, strictly larger than the diameter, and its fixed-point set is the diameter itself.

## Is Decoherence a Projection?

We can now separate the senses cleanly.

### Sense 1: The input state is a projection

This is the sense in which "idempotent" attaches to the *state*. A pure state is an idempotent element $\tilde{P}^2 = \tilde{P}$, and decoherence is precisely the process that deforms it into a non-idempotent positive trace-one element. In this sense the title is a statement about what decoherence *acts on*: it acts on an idempotent, and it destroys the idempotency. The deviation scalar $\mathrm{Sc}(\tilde{\rho}^2 - \tilde{\rho})$ measures how much of the projection structure has been lost.

It is worth being explicit that this is exact and not a metaphor: the condition $\tilde{\rho}^2 = \tilde{\rho}$ is the condition $\mathrm{Tr}(\tilde{\rho}^2) = 1$, and decoherence makes the purity strictly less than one for every off-axis input.

### Sense 2: Full dephasing is an idempotent channel

At $p = 1$ the channel itself is idempotent, and the projection metaphor becomes exact in a strong operator-algebraic sense. Write $A$ for the complex span of the two pointer idempotents,

$$
A = \left\{ z_+\,\tilde{P}_+(\hat{\mathbf{n}}) + z_-\,\tilde{P}_-(\hat{\mathbf{n}}) \;:\; z_\pm \in \mathbb{C} \right\},
$$

a two-dimensional commutative $\dagger$-subalgebra of $\mathbb{B}$, isomorphic to $\mathbb{C} \oplus \mathbb{C}$ — the algebra of operators diagonal in the pointer basis. Then $\Phi^{\mathrm{deph}}_1$ has the following properties, all of them direct consequences of $\tilde{P}_\pm^2 = \tilde{P}_\pm$, $\tilde{P}_+\tilde{P}_- = 0$, and $\tilde{P}_+ + \tilde{P}_- = e_0$:

1. **Idempotent:** $(\Phi^{\mathrm{deph}}_1)^2 = \Phi^{\mathrm{deph}}_1$.
2. **Trace preserving:** $\mathrm{Tr}(\Phi^{\mathrm{deph}}_1(\tilde{X})) = \mathrm{Tr}(\tilde{X})$.
3. **Unital:** $\Phi^{\mathrm{deph}}_1(e_0) = e_0$.
4. **Module property:** $\Phi^{\mathrm{deph}}_1(\tilde{A}\tilde{X}\tilde{B}) = \tilde{A}\,\Phi^{\mathrm{deph}}_1(\tilde{X})\,\tilde{B}$ for all $\tilde{A}, \tilde{B} \in A$.
5. **Self-adjointness for the trace pairing:** $\mathrm{Tr}(\Phi^{\mathrm{deph}}_1(\tilde{X})\,\tilde{A}) = \mathrm{Tr}(\tilde{X}\,\tilde{A})$ for all $\tilde{A} \in A$.

Properties 1–5 are the defining properties of the **trace-preserving conditional expectation** onto $A$. Because the trace pairing $\mathrm{Tr}(\tilde{H}\tilde{K}) = 2(h_0k_0 + \mathbf{h}\cdot\mathbf{k})$ is positive definite on $\mathbb{M}_+$, property 5 says that, restricted to Hermitian elements, $\Phi^{\mathrm{deph}}_1$ is exactly the **orthogonal projection** of $\mathbb{M}_+$ onto the Hermitian part of $A$, namely $\mathrm{span}_{\mathbb{R}}\{e_0, i\hat{\mathbf{n}}\}$: it is the closest pointer-diagonal operator to $\tilde{X}$ in the Hilbert–Schmidt geometry. Equivalently, in the pointer basis,

$$
\Phi^{\mathrm{deph}}_1(\tilde{\rho}) = \mathrm{Tr}\!\left(\tilde{P}_+(\hat{\mathbf{n}})\,\tilde{\rho}\right)\tilde{P}_+(\hat{\mathbf{n}}) + \mathrm{Tr}\!\left(\tilde{P}_-(\hat{\mathbf{n}})\,\tilde{\rho}\right)\tilde{P}_-(\hat{\mathbf{n}}),
$$

the diagonal part of $\tilde{\rho}$ in that basis. This is the strongest sense in which "idempotent projection" is a correct description: full dephasing *is* a projection, in the exact sense of a trace-preserving conditional expectation, and its image is the set of states diagonal in the pointer basis.

### Sense 3: Partial dephasing is a contraction, not a projection

For $0 < p < 1$, none of the above survives as a characterization of a projection. The map is not idempotent. Its fixed points are the pointer diameter, but its image is strictly larger than that diameter: it is a strict contraction of the Bloch ball toward the pointer diameter, with the transverse component merely damped rather than annihilated.

There is a further, sharper way to see that it is not a projection, which also locates the irreversibility precisely. As a linear map on the Bloch vector, the transverse eigenvalue of $\Phi^{\mathrm{deph}}_p$ is $1-p \neq 0$, so $\Phi^{\mathrm{deph}}_p$ is **mathematically invertible** for every $p < 1$; its inverse simply scales the transverse components back up by $1/(1-p)$. But that inverse is **not a channel**: scaling transverse components *up* by more than one maps some states outside the Bloch ball, so the inverse is not positive, hence not completely positive. Dephasing for $0<p<1$ is therefore invertible as a linear map and irreversible as a physical process. Irreversibility here is not the same as mathematical non-invertibility; it is the failure of the inverse to be a valid quantum operation. Only at $p=1$ does the map become genuinely non-invertible — rank-deficient in the transverse direction — and it is exactly there that it also becomes a projection. The projection metaphor and true irreversibility arrive together, at full dephasing.

Two further caveats complete the honest accounting.

First, the non-selective character. Full dephasing is a *measurement without selection*: it produces the mixture $p_+\tilde{P}_+ + p_-\tilde{P}_-$ and does not choose between the outcomes. It is a projection in the operator-algebraic sense, not a collapse onto a single idempotent. The selective update $\tilde{\rho} \mapsto \tilde{P}_+$, discussed in *Quantum Mechanics in Biquaternionic Form*, is a different operation; decoherence as such does not perform it.

Second, idempotency alone does not single out dephasing. The completely depolarizing map at full strength, $\tilde{\rho} \mapsto \tfrac12 e_0$, is also idempotent and trace preserving, and it is a conditional expectation onto the scalars. In general, a trace-preserving idempotent channel on a qubit is a conditional expectation onto a $\dagger$-subalgebra of $\mathbb{B}$ (its Hermitian part lying in $\mathbb{M}_+$), and the nontrivial possibilities are the pointer subalgebras $A = \mathbb{C}\tilde{P}_+ \oplus \mathbb{C}\tilde{P}_-$ (dephasing in some basis) and the scalars $\mathbb{C}e_0$ (full depolarization), together with the identity. So "idempotent projection" is a class, not a synonym for decoherence; what distinguishes dephasing within that class is that its fixed algebra is non-central, i.e., it selects a basis rather than erasing all directions alike.

## Pointer Basis and Einselection

The dephasing channel is specified by a single unit vector $\hat{\mathbf{n}}$, and everything in the preceding section — the pointer subalgebra, the fixed set, the surviving idempotents — is organized around the basis it defines. This is the framework's rendering of the **pointer basis** and **einselection**, and it is worth stating exactly how far it goes.

The algebra supports the following statements once $\hat{\mathbf{n}}$ is fixed.

- **The pointer basis is a commutative subalgebra.** The two idempotents $\tilde{P}_\pm(\hat{\mathbf{n}})$ commute and generate $A \cong \mathbb{C}\oplus\mathbb{C}$. These are the minimal projections of $A$, and they are the only pure states fixed by the channel: the states on the pointer diameter that are pure are exactly $\mathbf{r} = \pm\hat{\mathbf{n}}$.
- **The pointer states are the robust states.** Under $\Phi^{\mathrm{deph}}_p$, the fixed states for every $p \in (0,1]$ are exactly the pointer-diagonal states $r_\perp = 0$; the populations of the pointer idempotents are invariants, $p_\pm = \mathrm{Tr}(\tilde{P}_\pm\tilde{\rho})$, while the coherences between them decay. The pointer states are the states whose measurement statistics are unaffected by the channel; superpositions are not.
- **The channel is invariant under the pointer phase rotation.** $\Phi^{\mathrm{deph}}_p$ commutes with conjugation by $e^{-i\theta\alpha}$, $\alpha = i\hat{\mathbf{n}}$, the one-parameter group of unitaries that fixes $\tilde{P}_\pm(\hat{\mathbf{n}})$. The symmetry group of the pointer basis is the $U(1)$ generated by the pointer observable $\alpha = i\hat{\mathbf{n}}$; the pointer idempotents are precisely the pure states invariant under it.

What the algebra does **not** supply is which $\hat{\mathbf{n}}$ is selected. The direction is an input to the dephasing channel, not an output of it. In the physical account of einselection, $\hat{\mathbf{n}}$ is determined by the system–environment interaction: the environment couples to a particular observable, and the pointer basis is the eigenbasis of that observable, the basis in which the interaction is diagonal. The biquaternion framework represents the *consequence* of that coupling — the channel $\Phi^{\mathrm{deph}}_p$ and the subalgebra $A$ — but it contains no dynamics of system–environment coupling from which $\hat{\mathbf{n}}$ could be derived. The framework therefore supports the *structure* of einselection (a preferred commutative subalgebra, stable idempotents, decaying coherences) without deriving the *selection* (why that subalgebra). That limitation is intrinsic to the operational reading, in which the channel is the data and the environment is not described.

## Relation to the Quantum–Classical Divide

The companion article *The Quantum–Classical Divide in the Biquaternion Framework* expresses the operational criterion of Korolkova, Sánchez-Soto, and Leuchs in the language of this series: quantum non-separability is signalled by **two idempotents** acting on the two partitions (two projective measurements), classical non-separability by **one idempotent and one unitary** (one measurement, one filter). The article closes by asking whether the *number of available idempotents* can itself be a dynamical variable — whether a configuration can lose an idempotent measurement channel through decoherence.

The dephasing channel answers that question in a precise and limited way. Two observations.

First, full dephasing *is* the operation the classical side of the criterion uses. At $p=1$, $\Phi^{\mathrm{deph}}_1$ is a non-selective idempotent operation on the partition: it is a projective measurement followed by discarding the outcome. An idempotent acting on one partition, with a unitary filter on the other, is exactly the classical pattern $\tilde{U}_A \otimes \tilde{P}_B$ of the divide article. So the fully decohered partition has, operationally, the classical profile: its only idempotent measurements are the commuting pointer ones, and its remaining structure is a classical probability distribution over them.

Second, partial dephasing explains how a partition gets there. For $0<p<1$, the coherence that the quantum case requires — the transverse Bloch components, which make two non-commuting measurements jointly informative — is damped but not erased. The map is a contraction toward the pointer diameter, and for every $0<p\le1$ the only pure states in its image are the two pointer idempotents; in the coarse-grained description, therefore, the idempotents surviving on a decohered partition are $\tilde{P}_\pm(\hat{\mathbf{n}})$, which commute and span only a commutative subalgebra, so no two *incompatible* idempotents remain and the partition's state space has become a classical simplex. In this operational sense the count of usable idempotents is indeed dynamical, as the divide article conjectured.

Two qualifications keep this honest. First, decoherence does not remove the idempotents from the algebra; it removes the *coherences between them* from the state. The non-commuting idempotents still exist mathematically; what fails is that a decohered state can still be used to violate the kind of joint-measurement structure the quantum case needs. Second, the divide article's structural refinement — that quantum non-separability lives in a *fundamental* element of $\mathbb{M}_+^{\otimes n}$ while classical non-separability lives in a *derived* coherence matrix — is echoed here but with a caveat. Decoherence makes the reduced/system state a classical probability distribution over pointer idempotents, which has the profile of a derived element. But by Stinespring dilation the full system-plus-environment state remains a fundamental state of a larger algebra; the classicality is a feature of the discarded description, not of the world. The framework can express that, but it does not supply the environment that would make it a physical statement rather than a formal one.

## What the Framework Does and Does Not Explain

**What it does explain, or make exact.**

- **The algebraic meaning of coherence and its loss.** Coherences are the transverse Bloch components, equivalently the off-diagonal entries in the pointer basis, equivalently the expectation values of the traceless observables orthogonal to $\hat{\mathbf{n}}$. Dephasing scales them by $1-p$ and preserves the populations. This is exact and derivable from the algebra.
- **Purity as idempotency, and decoherence as a deformation.** The identity $\tilde{\rho}^2 - \tilde{\rho} = \tfrac14(|\mathbf{r}|^2-1)e_0$ turns "loss of coherence" into a single scalar whose vanishing is purity. Decoherence is literally the deformation of an idempotent into a non-idempotent positive trace-one element.
- **The sense of the projection metaphor.** Full dephasing is a trace-preserving conditional expectation onto the pointer subalgebra, hence an orthogonal projection with respect to the trace pairing, hence an idempotent channel. This is where the title's phrase is exactly true.
- **The failure of the projection metaphor.** For $0<p<1$ the channel is not idempotent; dephasing twice is dephasing harder. It is a contraction of the Bloch ball toward the pointer diameter, and although mathematically invertible, its inverse is not completely positive, so it is physically irreversible. This is where the title's phrase, read as a description of the generic process, is false.
- **The pointer basis and einselection structure.** Once the pointer observable is fixed, the pointer idempotents, the commutative pointer subalgebra, its $U(1)$ symmetry, the fixed set, and the stable populations are all algebraically explicit.
- **The relation to the reversible/irreversible dichotomy.** Dephasing is a Kraus-rank-two channel for every $0 < p \leq 1$ (rank one only at $p=0$, where it is the identity), hence irreversible; the reversible channels are exactly the unitarily-conjugate, Kraus-rank-one maps. Irreversibility is a property of the channel's algebraic form, not an extra postulate.

**What it does not explain.**

- **Which pointer basis.** The direction $\hat{\mathbf{n}}$ is an input. The framework does not derive it, because it does not describe the system–environment interaction that selects it. Einselection's *dynamics* is outside the algebra.
- **The environment and the rate.** The decay parameter $p$, or the rate $\Gamma$, is a free input; the environment of the Stinespring dilation is formal. The framework provides no equation of motion for $\Gamma$, no coupling constants, no environmental spectral density.
- **The selection of an outcome.** Full dephasing is non-selective: it produces a classical mixture of the pointer outcomes and does not choose one. Decoherence by itself does not solve the measurement problem, and the framework does not claim that it does. The selection problem is untouched.
- **Why irreversibility is physical rather than merely mathematical.** That the dephasing inverse is not completely positive is a theorem; why the world's dynamics should be so structured, or why environments begin effectively unentangled, is not addressed.
- **Empirical content.** As with the rest of the operational framework, the dephasing channel in biquaternion notation is standard open-systems theory transcribed; it predicts nothing that the standard theory does not.
- **Extension.** The treatment is single-qubit. Many-qubit decoherence, entanglement between decohered qubits, and the field-theoretic setting are not developed here, and the tensor-product structure of the framework — the analogue of the partial trace that Stinespring dilation requires — is inherited rather than derived.

## Summary

A pure state of the informational sector is an idempotent element of $\mathbb{M}_+$: $\tilde{P}^2 = \tilde{P}$. Its mixedness is measured by the deviation $\tilde{\rho}^2 - \tilde{\rho} = \tfrac14(|\mathbf{r}|^2-1)e_0$, whose vanishing is exactly purity. Decoherence, in the form of the dephasing channel of the companion article, deforms an idempotent into a non-idempotent positive trace-one element: it preserves the populations and scales the coherences by $1-p$, sending the Bloch vector $\mathbf{r} \mapsto (1-p)\mathbf{r} + p(\hat{\mathbf{n}}\cdot\mathbf{r})\hat{\mathbf{n}}$ and carrying a pure state from the Bloch sphere into the ball along a straight line toward the pointer axis.

The title's phrase "idempotent projection" must therefore be read with care, and the distinction between an idempotent *element* and an idempotent *channel* is the spine of the subject:

- The **input state** is an idempotent; decoherence destroys that idempotency.
- **Full dephasing** ($p=1$) is an idempotent channel: a trace-preserving conditional expectation onto the pointer subalgebra, i.e., an orthogonal projection with respect to the trace pairing, whose image is the pointer diameter and whose Kraus rank is two.
- **Partial dephasing** ($0<p<1$) is not idempotent: $\Phi^{\mathrm{deph}}_p \circ \Phi^{\mathrm{deph}}_p = \Phi^{\mathrm{deph}}_{2p-p^2} \neq \Phi^{\mathrm{deph}}_p$. It is a contraction, not a projection; it is mathematically invertible but physically irreversible, because its inverse is not completely positive.

The pointer basis is the commutative $\dagger$-subalgebra of $\mathbb{B}$ generated by the two idempotents along $\hat{\mathbf{n}}$ (its Hermitian part lies in $\mathbb{M}_+$); its idempotents are the only pure states fixed by the channel, and the subalgebra is invariant under the $U(1)$ phase rotation they generate. The framework supplies this structure once $\hat{\mathbf{n}}$ is given, but it does not derive $\hat{\mathbf{n}}$, the environment, the rate, or the selection of an outcome. In the language of the quantum–classical divide, decoherence is the process by which a partition loses its incompatible idempotents — becoming, operationally, a classical simplex over the pointer states — while the underlying system-plus-environment state remains fundamental. That is what the algebra explains; what lies beyond it is the dynamics that the algebra does not contain.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{M}_+$ | Hermitian subspace (states and observables) |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (generators of reversible evolution) |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\tilde{\rho} = \tfrac12(e_0 + i\mathbf{r})$ | State with Bloch vector $\mathbf{r}$, $|\mathbf{r}|\leq1$ |
| $\tilde{P}_\pm(\hat{\mathbf{n}}) = \tfrac12(e_0 \pm i\hat{\mathbf{n}})$ | Pointer idempotents (pure states along $\hat{\mathbf{n}}$) |
| $\mathrm{Tr}(\tilde{H}) = 2\,\mathrm{Sc}(\tilde{H})$ | Trace |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula (Born rule) |
| $\mathrm{Tr}(\tilde{\rho}^2) = \tfrac12(1 + |\mathbf{r}|^2)$ | Purity |
| $\tilde{\rho}^2 - \tilde{\rho} = \tfrac14(|\mathbf{r}|^2-1)e_0$ | Deviation from idempotency (mixedness) |
| $N(\tilde{\rho}) = \tfrac14(1-|\mathbf{r}|^2)e_0$ | Norm form (positivity condition) |
| $\Phi^{\mathrm{deph}}_p$ | Dephasing channel of strength $p \in [0,1]$ along $\hat{\mathbf{n}}$ |
| $\Phi^{\mathrm{deph}}_p(\tilde{\rho}) = (1-p)\tilde{\rho} + p(\tilde{P}_+\tilde{\rho}\tilde{P}_+ + \tilde{P}_-\tilde{\rho}\tilde{P}_-)$ | Dephasing action on states |
| $\tilde{K}_0 = \sqrt{1-p}\,e_0,\ \tilde{K}_{1,2} = \sqrt{p}\,\tilde{P}_\pm$ | Kraus operators of dephasing |
| $\mathbf{r} \mapsto (1-p)\mathbf{r} + p(\hat{\mathbf{n}}\cdot\mathbf{r})\hat{\mathbf{n}}$ | Dephasing action on the Bloch vector |
| $\Phi^{\mathrm{deph}}_p \circ \Phi^{\mathrm{deph}}_q = \Phi^{\mathrm{deph}}_{p+q-pq}$ | Composition law |
| $\alpha = i\hat{\mathbf{n}}$, $\alpha^2 = e_0$ | Pointer observable |
| $A = \mathbb{C}\tilde{P}_+ \oplus \mathbb{C}\tilde{P}_-$ | Pointer (commutative) subalgebra |
| $S(\tilde{\rho}) = -\lambda_+\log\lambda_+ - \lambda_-\log\lambda_-$ | Von Neumann entropy, $\lambda_\pm = \tfrac12(1\pm|\mathbf{r}|)$ |
| $\Phi(\tilde{\rho}) = \sum_l \tilde{K}_l\tilde{\rho}\tilde{K}_l^\dagger$ | Kraus representation of a channel |

## Further Reading

- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for quantum channels, the Kraus representation, and the dephasing and depolarizing channels.
- K. Kraus, *States, Effects, and Operations* (Springer, 1983), for completely positive maps and the conditional-expectation structure of idempotent operations.
- W. H. Zurek, "Pointer basis of quantum apparatus: Into what mixture does the wave packet collapse?" *Physical Review D* **24** (1981) 1516, and "Decoherence, einselection, and the quantum origins of the classical," *Reviews of Modern Physics* **75** (2003) 715, for pointer bases and einselection.
- E. Joos and H. D. Zeh, "The emergence of classical properties through interaction with the environment," *Zeitschrift für Physik B* **59** (1985) 223, for the original decoherence mechanism.
- A. Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), for non-selective measurements, mixing, and the Bloch-ball geometry.
- G. Lindblad, "On the generators of quantum dynamical semigroups," *Communications in Mathematical Physics* **48** (1976) 119–130, for the semigroup form of continuous decoherence.
- D. Petz, *Quantum Information Theory and Quantum Statistics* (Springer, 2008), for trace-preserving conditional expectations and the fixed-point theory of completely positive maps.
- N. Korolkova, L. Sánchez-Soto, and G. Leuchs, "An operational distinction between quantum entanglement and classical non-separability," arXiv:2405.15692 (2024), for the operational criterion discussed in the companion article on the quantum–classical divide.
- The companion articles of this series: *Quantum Mechanics in Biquaternionic Form*, *Quantum Channels and the Reversible/Irreversible Dichotomy*, *The Quantum–Classical Divide in the Biquaternion Framework*, and *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*.
