# __The Ontology of the Quantum State under the Biquaternion Framework__

## Introduction

What is the quantum state? The question is as old as the formalism, and it is usually posed as a choice among readings: is the state a real physical entity, a catalogue of an observer's knowledge, or a relation between a system and a measurement context? This article asks the question inside the biquaternion framework of the companion articles, where the state is not a primitive to be interpreted on its own but an **element of a fixed algebra**.

The framework's answer is a split one, and the split is the subject of the article. The algebra determines *what the element is* with unusual precision: a positive trace-one element of the Hermitian subspace $\mathbb{M}_+$, a point of the Bloch ball, with purity an idempotence condition and mixedness a single scalar. The algebra does not determine *what the element is an element of*: that is the informational-sector hypothesis of *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, labelled there as a hypothesis and not a result. The ontology of the state is therefore not a self-contained question. It is the ontology of $\mathbb{M}_+$.

This article is interpretive, and it keeps the boundary between what the algebra establishes and what is interpretation explicit in every section. The established facts are recomputed from the definitions, not inherited on authority. The interpretive readings are labelled as readings, and where a reading is not forced by the algebra, that is said rather than smoothed over.

The material is inherited, unchanged, from the read list. From *Quantum Mechanics in Biquaternionic Form*: the states are the positive trace-one elements of $\mathbb{M}_+$, the pure states are the idempotents $\tilde{P}_\pm(\hat{\mu})=\tfrac12(e_0\pm i\hat{\mu})$, the mixed states are the interior of the Bloch ball $\tilde{\rho}=\tfrac12(e_0+i\mathbf{r})$ with $|\mathbf{r}|<1$, and the Born rule is the trace pairing $\mathrm{Tr}(\tilde{\rho}\tilde{H})$. From *The Bloch Ball as the Trace-One Slice of the Future Light Cone*: the state space is the intersection of the trace-one hyperplane with the future light cone of the norm form $N(\tilde{H})=\tilde{H}\bar{\tilde{H}}$, and the pure states are the zero divisors at trace one. From *The Measurement Problem in Algebraic Form*: the element is **provenance-blind** and carries no index of the realised outcome. From *Decoherence as Idempotent Projection*: decoherence is the deformation of an idempotent into a non-idempotent positive trace-one element, with $\tilde{\rho}^2-\tilde{\rho}=\tfrac14(|\mathbf{r}|^2-1)e_0$. From *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*: the anti-Hermitian subspace carries the four-vectors and is complementary to $\mathbb{M}_+$.

The article proceeds as follows. The next four sections collect the established structure of the state as an element: its definition and geometry; its cohabitation with the observables in one space; its convex structure; and its purity as idempotence and as zero-divisorhood. Two further sections state what the element does not carry and what it is not. The last three sections separate the ontological readings the algebra permits, state the sector hypothesis under which they acquire physical content, and list the questions the algebra leaves open.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$, and $i$ is the scalar imaginary, $i^2=-1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector), with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$; $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$ is the center of the algebra. The Hermitian conjugation is $\dagger=\bar{\cdot}^{\,*}$, and the trace is the matrix-representation trace, $\mathrm{Tr}(\tilde{H})=2\,\mathrm{Sc}(\tilde{H})$, with the trace formula $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ inherited unchanged.

## The State as an Element of $\mathbb{M}_+$

A state of the informational sector is an element of the Hermitian subspace

$$
\tilde{\rho}=\tfrac12\left(e_0+i\,\mathbf{r}\right),\qquad \mathbf{r}=r_1 e_1+r_2 e_2+r_3 e_3\in\mathbb{R}^3,
$$

with the positivity condition $|\mathbf{r}|\leq1$. Its scalar part is real and its vector part purely imaginary, so $\tilde{\rho}\in\mathbb{M}_+$ by the definition of that subspace. Its trace is $\mathrm{Tr}(\tilde{\rho})=1$, and it is an observable — a Hermitian element — that is positive and normalized.

Three identities carry the whole of the state's structure. Expanding the square in the algebra,

$$
\tilde{\rho}^2=\tfrac14\left(\left(1+|\mathbf{r}|^2\right)e_0+2i\,\mathbf{r}\right),
$$

so the deviation from idempotency is a pure scalar,

$$
\tilde{\rho}^2-\tilde{\rho}=\tfrac14\left(|\mathbf{r}|^2-1\right)e_0 ,
$$

and the norm form is

$$
N(\tilde{\rho})=\tilde{\rho}\bar{\tilde{\rho}}=\tfrac14\left(1-|\mathbf{r}|^2\right)e_0 .
$$

The three are consistent: the eigenvalues of $\tilde{\rho}$ are $\lambda_\pm=\tfrac12(1\pm|\mathbf{r}|)$, so positivity is exactly $|\mathbf{r}|\leq1$, which is exactly $N(\tilde{\rho})\geq0$, which is exactly membership of the future light cone of the norm form. The state space is therefore the trace-one slice of that cone,

$$
\{\text{states}\}=\left\{\tilde{\rho}\in\mathbb{M}_+:\ \mathrm{Tr}(\tilde{\rho})=1,\ N(\tilde{\rho})\geq0\right\},
$$

the Bloch ball of radius one.

**Established, and recomputed.** The state is an element of $\mathbb{M}_+$; positivity, trace normalization, and the norm-form condition are one condition; the deviation from idempotency is a single real scalar. These were checked on randomly generated states, not on the example that suggested them.

**Interpretation begins only at the next question.** The algebra says which elements are states and how they are related. It does not say that these elements are physical, or what they are physical states *of*. That question is held back until the sector hypothesis, taken up in a later section.

## The State and the Observable in One Space

A general observable of the informational sector is an element

$$
\tilde{H}=h_0 e_0+i\,\mathbf{h},\qquad h_0\in\mathbb{R},\quad \mathbf{h}\in\mathbb{R}^3,
$$

of the same subspace $\mathbb{M}_+$. The state $\tilde{\rho}=\tfrac12(e_0+i\mathbf{r})$ is a particular case: an observable with $h_0=\tfrac12$ and $\mathbf{h}=\tfrac12\mathbf{r}$, positive and of trace one. **States are positive trace-one observables.** The standard formalism also represents states and observables by operators, but there the state is standardly read as a functional — a positive normalized linear map on observables — while the observable enters as the object acted upon. In the biquaternion framework the distinction is not one of kind and not one of dual space: it is the conjunction of two conditions, positivity and trace, imposed on elements of one four-dimensional real space.

Two facts make the cohabitation exact. First, the trace pairing

$$
\mathrm{Tr}(\tilde{\rho}\tilde{H})=h_0+\mathbf{r}\cdot\mathbf{h}
$$

is a positive-definite symmetric form on $\mathbb{M}_+$, with Gram matrix diagonal in the basis $\{e_0,ie_1,ie_2,ie_3\}$; up to the normalization $\mathrm{Tr}(e_0)=2$ it is the Euclidean pairing. Second — and this is the point for the ontology — because the pairing is positive definite, the map

$$
\tilde{\rho}\ \longmapsto\ \left(\tilde{H}\mapsto \mathrm{Tr}(\tilde{\rho}\tilde{H})\right)
$$

is injective: an element of $\mathbb{M}_+$ is determined by its pairings with observables. So the state, regarded as a functional on observables, is an element of the very space on which it is a functional; $\mathbb{M}_+$ is its own dual under the trace pairing, and there is no second space in which the state lives.

That the state is a *positive* functional is part of the same structure. If $\tilde{H}\geq0$, meaning $h_0\geq|\mathbf{h}|$, then

$$
\mathrm{Tr}(\tilde{\rho}\tilde{H})=h_0+\mathbf{r}\cdot\mathbf{h}\ \geq\ |\mathbf{h}|-|\mathbf{r}|\,|\mathbf{h}|=\left(1-|\mathbf{r}|\right)|\mathbf{h}|\ \geq\ 0 .
$$

Positivity of the functional is thus not an extra postulate; it is the positivity condition $|\mathbf{r}|\leq1$ of the state seen from the dual side. The pairing formula, the positivity inequality, and the injectivity were all recomputed on randomly generated states and observables.

**Interpretation.** The cohabitation of states and observables is a structural fact; what it means is a reading. The natural reading is that the framework refuses a dualistic picture in which "states of information" inhabit a different kind of object from "physical quantities". A more cautious reading is that the coincidence is a feature of working in $\mathbb{B}\cong M_2(\mathbb{C})$, where states and effects are both matrices. The algebra does not decide between these readings, and the fact that it does not is itself a datum: it locates the ontological question elsewhere than in a state/observable dichotomy.

## Convexity, Extremality, and the Superposition Principle

The states form a **convex set**. If $\tilde{\rho}_1,\tilde{\rho}_2$ are states and $\lambda\in[0,1]$, then $\lambda\tilde{\rho}_1+(1-\lambda)\tilde{\rho}_2$ is Hermitian, of trace one, and positive — a state. In Bloch coordinates this is the convexity of the ball. The **pure** states, $|\mathbf{r}|=1$, are its **extreme points**: if a pure state is written as a nontrivial convex combination of two states, the two must coincide with it. For distinct unit vectors $\mathbf{r}_1\neq\mathbf{r}_2$ and $\lambda\in(0,1)$ one has $|\lambda\mathbf{r}_1+(1-\lambda)\mathbf{r}_2|<1$ strictly, by the triangle inequality, with equality only for $\mathbf{r}_1=\mathbf{r}_2$. Every mixed state, $|\mathbf{r}|<1$, is an interior point and admits a nontrivial decomposition; its spectral decomposition

$$
\tilde{\rho}=\lambda_+\tilde{P}_+(\hat{\mathbf{r}})+\lambda_-\tilde{P}_-(\hat{\mathbf{r}}),\qquad \lambda_\pm=\tfrac12\left(1\pm|\mathbf{r}|\right),
$$

is one, and the spectral decomposition is unique for $\mathbf{r}\neq0$.

The state space is a convex body, not a vector space, and the difference matters. The sum of two states is not a state: $\mathrm{Tr}(\tilde{\rho}_1+\tilde{\rho}_2)=2$, and a scalar multiple of a state is not a state either. In particular the **superposition principle is not a statement about the state space**. Superposition belongs to the spinor module of $\mathbb{B}$ — the complex two-dimensional module entering the correspondence of *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* — which is a vector space; the states are the positive trace-one elements built from that module, and they form the convex ball. The framework's state is therefore not a vector to be added and not a ray to be projected: it is a convex element whose extreme points are the pure states.

**Interpretation.** Convexity gives a precise sense to "the state is a mixture": a mixed state is literally a convex combination of pure states in its own space, and the combination is an element of that space, not a classical probability distribution placed alongside it. This is a suggestive picture — the state as a point of a convex body whose extreme points are the pure states — but it is a picture. It does not by itself say whether the convex point is a real object or a representation of ignorance; and since the decomposition into non-orthogonal pure states is not unique (the next section), the same convex point can be presented as many different mixtures.

## The Pure State Is an Idempotent and a Zero Divisor

A state is pure exactly when $\tilde{\rho}^2=\tilde{\rho}$, which is exactly $|\mathbf{r}|=1$, which is exactly $N(\tilde{\rho})=0$. The last equality says that the pure states of trace one are exactly the **zero divisors** of $\mathbb{B}$ on the trace-one slice: a pure state is a nonzero element that annihilates a nonzero element, explicitly

$$
\tilde{P}_+(\hat{\mu})\,\tilde{P}_-(\hat{\mu})=0,\qquad \tilde{P}_\pm(\hat{\mu})=\tfrac12\left(e_0\pm i\hat{\mu}\right),
$$

with $\hat{\mu}$ a unit pure real quaternion, and $\tilde{P}_++\tilde{P}_-=e_0$. In the matrix representation $\mathbb{B}\cong M_2(\mathbb{C})$ a pure state is a rank-one projector, with vanishing determinant, while a mixed state is invertible and of rank two, with $\det=N(\tilde{\rho})=\tfrac14(1-|\mathbf{r}|^2)\neq0$. Purity, idempotence, extremality, and being a zero divisor are the same condition on the element.

**Established, and recomputed.** For random pure states the idempotence, the vanishing norm form, the annihilation identity, and the vanishing determinant all hold; for random mixed states the failure of idempotence and the non-vanishing determinant hold. The determinant identity $\det\varphi(\tilde{X})=N(\tilde{X})$ for the matrix representation $\varphi$ was checked on random biquaternions, which is what identifies the norm-form-zero set with the singular, hence zero-divisor, set.

**Interpretation.** Purity as an annihilation property is a genuinely algebraic way to state what purity is, and it is suggestive: a pure state is an element blind to its complement, in the exact sense that $\tilde{P}_+$ annihilates $\tilde{P}_-$. Whether that blindness should be read as a feature of physical reality or as a feature of the algebra is not decided by the algebra, and it is one of the readings the next sections leave open.

## What the Element Does Not Carry

Two negative facts about the state element are as structural as the positive ones.

**Provenance-blindness.** The state carries no record of how it was prepared. The algebra shows this directly: a mixed state has many ensemble decompositions. For a state with Bloch vector $\mathbf{r}$, $|\mathbf{r}|<1$, and a unit direction $\hat{\mathbf{n}}$ orthogonal to $\mathbf{r}$, put $t=\sqrt{1-|\mathbf{r}|^2}$, so that $\mathbf{r}_\pm=\mathbf{r}\pm t\hat{\mathbf{n}}$ are unit vectors. Then

$$
\tilde{\rho}=\tfrac12\,\tilde{P}_+(\mathbf{r}_+)+\tfrac12\,\tilde{P}_+(\mathbf{r}_-)
$$

is an ensemble decomposition with two pure states of the same type, distinct from the spectral decomposition (which uses one $\tilde{P}_+$ and one $\tilde{P}_-$). The maximally mixed state is the sharpest case: $\tfrac12 e_0=\tfrac12\tilde{P}_+(\hat{\mathbf{n}})+\tfrac12\tilde{P}_-(\hat{\mathbf{n}})$ for *every* unit $\hat{\mathbf{n}}$. The element is the same under all of these preparations, so it cannot be a catalogue of which preparation occurred. This was recomputed on random mixed states. *The Measurement Problem in Algebraic Form* states the same fact as the provenance-blindness of the state, and uses it to explain why a proper and an improper mixture are the same element of $\mathbb{M}_+$.

**No outcome index.** The state determines the Born probabilities

$$
p_\pm=\mathrm{Tr}\!\left(\tilde{P}_\pm(\hat{\mathbf{h}})\,\tilde{\rho}\right)=\tfrac12\left(1\pm\hat{\mathbf{h}}\cdot\mathbf{r}\right)
$$

of a measurement along $\hat{\mathbf{h}}$, and nothing about which outcome occurs. No element of $\mathbb{M}_+$ and no operation of the algebra carries the index $\pm$; that is the selection problem in algebraic form, established in the measurement-problem article and not resolved here. In the geometric language of that article the statistics determine the segment — the pointer diameter — and the outcomes are its endpoints; the element is the segment.

**Established, inherited, and not repaired.** Both facts are properties of the element at the single-qubit level. They are stated here because they bound what any ontology of the state can claim: an element that carries neither provenance nor outcome cannot be a complete description of an individual measurement event, whatever else it is. In two clauses: the element is **operationally complete** — it determines every statistic and is determined by them — and **ontically incomplete** — it determines no outcome and records no preparation.

## The State Is Not a Spacetime Object, and Not a Spinor Ray

The complementarity $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ assigns the state to the informational side. The four-vectors of relativistic physics — position, velocity, momentum, potential, current — lie in $\mathbb{M}_-$, with imaginary scalar part and real vector part; the state has real scalar part and imaginary vector part, so it lies in $\mathbb{M}_+$ and has zero component in $\mathbb{M}_-$. The state is therefore not a configuration in spacetime and not a four-vector; it is an element of the complementary sector. Its relation to the material sector is not that of a configuration but that of an operator: the elements of $\mathbb{M}_+$ act on $\mathbb{M}_-$ by conjugation, and the norm-form-preserving, unit-norm-form ones among them are the Lorentz boost rotors. A state is not one of them. Its norm form is $N(\tilde{\rho})=\tfrac14(1-|\mathbf{r}|^2)\in[0,\tfrac14]$, never $1$, so no state has unit norm form; the state is not an action on spacetime either, but a normalized positive element of the operator subspace.

The state is equally not a spinor ray. In the correspondence of *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, the spinor module of $\mathbb{B}$ corresponds to the Hilbert space $\mathbb{C}^2$ and the pure states correspond to the rank-one density operators. The framework's state is the second object, not the first: the pure state is the idempotent $\tilde{P}_\pm(\hat{\mu})$, and the passage from a module element to a state is the rank-one projection onto it. A central phase $\psi\mapsto e^{i\theta}\psi$ leaves the idempotent unchanged, because $e^{i\theta}$ lies in the center $\mathbb{C}_{\mathbb{B}}$; the phase of the spinor is therefore not part of the state. So the framework's state is not a vector and not a ray: it is the idempotent built from the ray, with the phase already quotiented out, and for a mixed state there is no spinor to build it from at all.

**Established.** These are statements about which subspace the state lies in and which object the framework calls the state. The interpretive consequence — that a "wavefunction ontology" and a "density-operator ontology" are not merely two readings of one object but, in this framework, readings of two different objects — is a reading, and it is labelled as one.

## Ontological Readings and What the Algebra Decides

We can now separate what the algebra settles from what it leaves to interpretation.

**Settled by the algebra.**

1. **Identity.** A state is a positive trace-one element of $\mathbb{M}_+$, equivalently a point of the Bloch ball, equivalently a trace-one element of the future light cone of the norm form. The identification is canonical: no choice of basis or representation enters, and the same objects are singled out in every isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$.
2. **Determinacy of statistics.** The element determines every measurement statistic, through the trace pairing, and is determined by them, because the pairing is positive definite.
3. **Convex structure.** States form a convex body whose extreme points are the pure states; mixedness is a convex combination in the same space; purity is idempotence and zero-divisorhood; the mixedness of a state is the single scalar $\mathrm{Sc}(\tilde{\rho}^2-\tilde{\rho})$.
4. **Blindness.** The element carries neither provenance nor outcome index.

**Readings the algebra permits.** Four familiar readings can be stated in these terms.

- **State realism.** The element is a real, determinate feature of the world. The algebra is compatible: the element is canonical and observer-independent, and nothing in the framework introduces an observer or a preparation into its definition. The cost is that the element then does not determine the outcome, which is exactly the selection problem; a state-realist reading must therefore be one on which the state is not a complete description of an individual event.
- **Epistemic or statistical reading.** The element summarizes an agent's information or the statistics of an ensemble. The algebra is compatible: the element is provenance-blind and determines statistics. The cost is that there is no agent and no ensemble anywhere in the algebra, and the element is not a bookkeeping table but a geometric object in the same space as the observables, with a canonical inner product and a canonical cone. An epistemic reading must explain why a summary of information has the geometry of a convex body of operators.
- **Relational reading.** The state is defined relative to a measurement context. The algebra is compatible in that the state's meaning is exhausted by its pairings with observables; the cost is that the element itself is context-independent — the same element enters every pairing — so the relation would have to live in the act of pairing, which is not an object of the algebra.
- **Structural reading.** What is real is the structure — the algebra, its subspaces, its pairings, its convex state space — rather than any particular element. The algebra is compatible, and this reading asks least of it. The cost is the familiar one of structural realism: it must say what distinguishes the structure that is realised from the many that are not.

**What is not settled.** The algebra decides none of these readings. It decides what a state *is* and what it *does*; it does not decide what a state is *of*. An added structure — a selection rule, a space of beables, an observer index, a preferred decomposition — would decide among the readings, and the algebra contains no such structure. **This article takes no position among the four.** It claims only that the framework's contribution to the debate is to fix the disputed object more sharply than the standard formalism does, and thereby to relocate the dispute: the question "is the state real?" becomes the question "is $\mathbb{M}_+$ real?".

## The Informational-Sector Hypothesis and the Ontology of the State

The framework's own interpretive hypothesis is stated in *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*: that $\mathbb{M}_+$ is not only a mathematical structure but an **informational sector** of the world, physically realised as the material sector $\mathbb{M}_-$ is. That article is explicit that the algebraic identification of $\mathbb{M}_+$ with the operator algebra of a qubit is established, while the physical realisation is a hypothesis.

Granting the hypothesis, the ontology of the state follows in one step. If $\mathbb{M}_+$ is a physical sector, then its elements are physical; a state, being a positive trace-one element, is a physical element of that sector; the Bloch ball is a physical convex body; and the readings above are readings of a physical object. This is a **sectorial realism** about the state: the state is real, but its reality is the reality of the sector, not a separate postulate. Denying the hypothesis, the state is a mathematical element of a reformulation of quantum mechanics — real only as mathematics — and the readings above are readings of a formalism.

The point of separating the two is that the algebra cannot make the choice. The same equations, the same identities, and the same state space serve under either reading; the difference is a commitment about the physical status of a subspace, and the algebra does not contain that commitment. **This is the article's central interpretive claim, and it is offered as a claim, not a result:** the ontology of the quantum state under the biquaternion framework is not an independent question but the ontology of $\mathbb{M}_+$, and the algebra relocates the question rather than answering it.

**A caution against over-reading.** The sector hypothesis does not by itself supply an outcome, a preferred basis, or a dynamics of the sector; those remain open in the parent article. Sectorial realism is therefore not a solution to the measurement problem, and it should not be presented as one. It is a reading of what the element is, not a completion of what the element does.

## What the Algebra Does Not Decide

The gaps are as much a part of the ontology as the results. Stated at the single-qubit level the framework supports:

1. **The selection of an outcome.** No element and no operation selects an outcome as a function of the state. The statistics are determined; the outcome is not. Sectorial realism does not repair this.
2. **The preferred basis.** The pointer direction is an input to decoherence, not an output of the algebra. A state with $\mathbf{r}\neq0$ has a canonical spectral decomposition, but its eigenbasis is not selected by any physical interaction, and it is not the pointer basis of a measurement.
3. **The provenance of ensembles and the proper/improper distinction.** The element does not distinguish a proper from an improper mixture; whether that distinction has physical content is not decided by the algebra, and the record that would carry it is not in $\tilde{\rho}$.
4. **Many-qubit ontology.** The state of $n$ qubits is a positive trace-one element of $\mathbb{M}_+^{\otimes n}$; the tensor product, the partial trace, and the reduced states are inherited rather than derived, and the ontology of a reduced state — its relation to the joint element — is treated in *Entangled Subsystems in the Biquaternion Framework* and is not developed here.
5. **Field-theoretic and relativistic states.** The state described is a single-qubit state. The Lorentz action is on $\mathbb{M}_-$; the state lives in $\mathbb{M}_+$ and is not a Lorentz-covariant object in the same sense. A relativistic, many-particle state is not developed here.
6. **Empirical content.** As everywhere in the framework, whether any of this yields a prediction distinguishing it from standard quantum mechanics is open. A reading of a formalism with the same predictions cannot be decided by experiment unless the formalism is extended.

## Summary

The quantum state in the biquaternion framework is a **positive trace-one element of the Hermitian subspace $\mathbb{M}_+$**,

$$
\tilde{\rho}=\tfrac12\left(e_0+i\mathbf{r}\right),\qquad |\mathbf{r}|\leq1 ,
$$

equivalently a point of the Bloch ball, equivalently a trace-one element of the future light cone of the norm form. Its purity is idempotence, $|\mathbf{r}|=1$, equivalently vanishing of the norm form and zero-divisorhood at trace one; its mixedness is the single scalar $\tilde{\rho}^2-\tilde{\rho}=\tfrac14(|\mathbf{r}|^2-1)e_0$. States and observables are elements of the same four-dimensional real space, distinguished only by positivity and trace normalization; the trace pairing $\mathrm{Tr}(\tilde{\rho}\tilde{H})=h_0+\mathbf{r}\cdot\mathbf{h}$ makes the state a positive normalized functional on that space, and its positive definiteness makes the space its own dual. The states form a convex body whose extreme points are the pure states, so superposition is a property of the spinor module, not of the state space.

Two negative facts bound the ontology. The element is **provenance-blind** — it has many ensemble decompositions, and the maximally mixed state has one for every basis — and it carries **no outcome index**, the probabilities $p_\pm$ being determined while the realised outcome is not. The state is not a spacetime object, lying in the sector complementary to the four-vectors; and it is not a spinor ray, being the idempotent built from the ray with the central phase already quotiented out.

The article's interpretive claim is that the algebra settles the identity, the statistics, the convex structure, and the blindness of the state, and settles nothing about its physical status. State realism, the epistemic reading, the relational reading, and the structural reading are all compatible with the algebra, and the algebra decides none of them; an added structure would be needed to do so, and there is none. The framework's own commitment is the informational-sector hypothesis, under which the state is a physical element of a physical sector — a sectorial realism offered as a hypothesis, not a result. The ontology of the quantum state is therefore the ontology of $\mathbb{M}_+$, and the algebra relocates the question rather than answering it. The selection of an outcome, the preferred basis, the proper/improper distinction, the many-qubit and field-theoretic extensions, and empirical contact remain open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$, central |
| $\mathbb{M}_+$ | Hermitian subspace (informational sector): real scalar, imaginary vector |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material sector): imaginary scalar, real vector |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}$ | Real-quaternion subspace; complex scalar center |
| $\tilde{\rho} = \tfrac12(e_0 + i\mathbf{r})$ | State, $|\mathbf{r}|\leq1$ (Bloch ball) |
| $\tilde{P}_\pm(\hat{\mu}) = \tfrac12(e_0 \pm i\hat{\mu})$ | Pure state (idempotent, rank-one projector, zero divisor) |
| $\tilde{H} = h_0e_0 + i\mathbf{h}$ | Observable (general Hermitian element) |
| $N(\tilde{H}) = \tilde{H}\bar{\tilde{H}}$ | Norm form, signature $(1,3)$ on $\mathbb{M}_+$ |
| $N(\tilde{\rho}) = \tfrac14(1-|\mathbf{r}|^2)e_0$ | Norm form of a state; positivity $\Leftrightarrow N\geq0$ |
| $\tilde{\rho}^2 - \tilde{\rho} = \tfrac14(|\mathbf{r}|^2-1)e_0$ | Deviation from idempotency (mixedness) |
| $\mathrm{Tr}(\tilde{H}) = 2\,\mathrm{Sc}(\tilde{H})$ | Trace |
| $\mathrm{Tr}(\tilde{\rho}\tilde{H}) = h_0 + \mathbf{r}\cdot\mathbf{h}$ | Trace pairing (Born rule); positive definite |
| $\lambda_\pm = \tfrac12(1\pm|\mathbf{r}|)$ | Eigenvalues of $\tilde{\rho}$ |
| $\hat{\mu}, \hat{\mathbf{n}}, \hat{\mathbf{h}}, \hat{\mathbf{r}}$ | Unit pure real quaternions (directions) |
| $\dagger = \bar{\cdot}^{\,*}$ | Hermitian conjugation |

## Further Reading

- *Introduction to the Biquaternion Universe*, for the algebra $\mathbb{B}$, its two sectors, and the conjunctions.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the operator-algebra identification and the informational-sector hypothesis.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the four-vectors and the complementarity $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$.
- *Quantum Mechanics in Biquaternionic Form*, for the state and observable formalism, the Bloch ball, and the Born rule.
- *The Bloch Ball as the Trace-One Slice of the Future Light Cone*, for the state space as a slice of the cone and purity as a boundary condition.
- *The Born Rule as a Trace Formula — Derivation and Comparison*, for what the trace pairing derives and what it restates.
- *Biquaternion Zero Divisors* and *Biquaternion Spectral Theory*, for the algebraic structure of idempotents, rank-one elements, and zero divisors used in the purity section.
- *The Measurement Problem in Algebraic Form*, for provenance-blindness, the missing outcome index, and the segment-versus-endpoint gap.
- *Decoherence as Idempotent Projection*, for the deformation of an idempotent into a mixed state.
- *Entangled Subsystems in the Biquaternion Framework*, for reduced states and the tensor-product structure.
- *Quantum Channels and the Reversible/Irreversible Dichotomy*, for the operation-form reading of evolution and measurement.
- *The Quantum–Classical Divide in the Biquaternion Framework*, for idempotent versus unitary operations.
- *Quantum Mechanics: Foundations and Structure*, for the standard formulation and the structural checklist.
