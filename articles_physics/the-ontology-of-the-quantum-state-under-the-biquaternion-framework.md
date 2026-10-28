# __The Ontology of the Quantum State under the Biquaternion Framework__

## Introduction

What is the quantum state? The question is as old as the formalism, and it is usually posed as a choice among interpretations: is the state a real physical entity, a catalogue of an observer's knowledge, or a relation between a system and a measurement context? This article asks the question inside the biquaternion framework of the companion articles, where the state is not a primitive to be interpreted on its own but an **element of a fixed algebra**.

The framework's answer is a split one, and the split is the subject of the article. The algebra determines *what the element is* with unusual precision: a positive element of the Hermitian subspace $\mathbb{M}_+$ normalised by $\langle\tilde{Ϛ},e_t\rangle_{*}=\tfrac12\langle e_t\rangle_{*}$ — trace one in the $2\times2$ image — a point of the Bloch ball, with purity an idempotence condition and mixedness a single scalar. The algebra does not determine *what the element is an element of*: that is the informational-sector hypothesis of *The Informational Sector: States, Observables and Probability*, labelled there as a hypothesis and not a result. The ontology of the state is therefore not a self-contained question. It is the ontology of $\mathbb{M}_+$.

This article is interpretive, and it keeps the boundary between what the algebra establishes and what is interpretation explicit in every section. The interpretive statements are labelled as interpretations, and where an interpretation is not forced by the algebra, that is said rather than smoothed over.

The material is inherited, unchanged, from the read list. From *Quantum Physics in Biquaternionic Form*: the states are the positive elements of $\mathbb{M}_+$ normalised by $\langle\tilde{Ϛ},e_t\rangle_{*}=\tfrac12$, the pure states are the idempotents $\tilde\Pi_{1,2}(\vec u)=\tfrac12(e_t\pm i\vec u)$, the mixed states are the interior of the Bloch ball $\tilde{Ϛ}=\tfrac12(e_t+i\vec r)$ with $|\vec r|<1$, and the Born rule is the normalised Hermitian form $\langle\tilde{Ϛ},\tilde{H}\rangle_{*}/\langle\tilde{Ϛ},e_t\rangle_{*}$, read as $\mathrm{Tr}(\tilde{Ϛ}\tilde{H}^{*})$ in the $2\times2$ image. From *The Bloch Ball as the Normalised Slice of the Future Light Cone*: the state space is the intersection of the normalisation hyperplane $\langle\tilde{Ϛ},e_t\rangle_{*}=\tfrac12$ (the trace-one hyperplane in the image) with the future light cone of the biquaternion norm $\langle\tilde{H}\rangle_{\natural}=\tilde{H}\tilde{H}^{\natural}$, and the pure states are the zero divisors at trace one. From *The Measurement Problem in Algebraic Form*: the element is **provenance-blind** and carries no index of the realised outcome. From *Decoherence as Idempotent Projection*: decoherence is the deformation of an idempotent into a non-idempotent positive normalised element (trace one in the image), with $\tilde{Ϛ}^2-\tilde{Ϛ}=\tfrac14(|\vec r|^2-1)e_t$. From *The Material Sector: Four-Vectors, Interval and Lorentz Action*: the anti-Hermitian subspace carries the four-vectors and is complementary to $\mathbb{M}_+$.

The article proceeds as follows. The next four sections collect the established structure of the state as an element: its definition and geometry; its cohabitation with the observables in one space; its convex structure; and its purity as idempotence and as zero-divisorhood. Two further sections state what the element does not carry and what it is not. The last three sections separate the ontological interpretations the algebra permits, state the sector hypothesis under which they acquire physical content, and list the questions the algebra leaves open.

## The State as an Element of $\mathbb{M}_+$

A state of the informational sector is an element of the Hermitian subspace

$$
\tilde{Ϛ}=\tfrac12\left(e_t+i\,\vec r\right),\qquad \vec r=r_1 \vec e_x+r_2 \vec e_y+r_3 \vec e_z\in\mathbb{R}^3,
$$

with the positivity condition $|\vec r|\leq1$. Its scalar part is real and its vector part purely imaginary, so $\tilde{Ϛ}\in\mathbb{M}_+$ by the definition of that subspace. Its normalisation is $\langle\tilde{Ϛ},e_t\rangle_{*}=\tfrac12\langle e_t\rangle_{*}$, which the trace reads as $\mathrm{Tr}(\tilde{Ϛ})=1$; it is a Hermitian element that is positive and normalized.

Three identities carry the whole of the state's structure. Expanding the square in the algebra,

$$
\tilde{Ϛ}^2=\tfrac14\left(\left(1+|\vec r|^2\right)e_t+2i\,\vec r\right),
$$

so the deviation from idempotency is a pure scalar,

$$
\boxed{\;\tilde{Ϛ}^2-\tilde{Ϛ}=\tfrac14\left(|\vec r|^2-1\right)e_t\;},
$$

and the biquaternion norm is

$$
\langle\tilde{Ϛ}\rangle_{\natural}=\tilde{Ϛ}\tilde{Ϛ}^{\natural}=\tfrac14\left(1-|\vec r|^2\right)e_t .
$$

The three are consistent: the eigenvalues of $\tilde{Ϛ}$ are $\lambda_\pm=\tfrac12(1\pm|\vec r|)$, so positivity is exactly $|\vec r|\leq1$, which is exactly $\langle\tilde{Ϛ}\rangle_{\natural}\geq0$, which is exactly membership of the future light cone of the biquaternion norm. The state space is therefore the state slice of that cone,

$$
\boxed{\;\{\text{states}\}=\left\{\tilde{Ϛ}\in\mathbb{M}_+:\ \langle\tilde{Ϛ},e_t\rangle_{*}=\tfrac12\langle e_t\rangle_{*},\ \langle\tilde{Ϛ}\rangle_{\natural}\geq0\right\}\;},
$$

the Bloch ball of radius one.

**Established, and recomputed.** The state is an element of $\mathbb{M}_+$; positivity, normalisation, and the biquaternion-norm condition are one condition; the deviation from idempotency is a single real scalar. These were checked on randomly generated states, not on the example that suggested them.

**Interpretation begins only at the next question.** The algebra says which elements are states and how they are related. It does not say that these elements are physical, or what they are physical states *of*. That question is held back until the sector hypothesis, taken up in a later section.

## The State Is the Square of an Amplitude

The state is not only an element of $\mathbb{M}_+$; it is the Hermitian square of another element. Every nonzero biquaternion $\tilde Q$ defines one by

$$
\boxed{\;\tilde{Ϛ}_{\tilde Q}=\frac{\tilde Q\tilde Q^{*}}{2\langle\tilde Q,\tilde Q\rangle_{*}},
\qquad
\tilde Q_H=\sqrt{\tilde Q\tilde Q^{*}},
\qquad
\tilde{Ϛ}_{\tilde Q}=\tilde Q_{\mathrm n}^{2}\;},
$$

where $\tilde Q_{\mathrm n}=\tilde Q_H/\sqrt{2\langle\tilde Q_H,\tilde Q_H\rangle_{*}}$ is the bracket-normalised amplitude. The amplitude $\tilde Q_H$ is Hermitian positive semidefinite; the state is its square. The square root of the state exists and is positive, so the statement is not merely formal: every state has a positive amplitude, namely $\sqrt{\tilde{Ϛ}}$.

This gives the ontology a second layer. If the operator is taken as primitive, the state is derived: it is what remains of the operator after the unitary factor and the overall scale are forgotten. If the state is taken as primitive, the amplitude is derived: it is the positive square root. The algebra permits both directions and decides neither. What it does decide is that the two objects are not the same, and that the passage from the operator to the state loses the phase and the scale.

Two consequences follow.

- **The amplitude is not unique as an operator factor.** The state determines $\tilde Q_{\mathrm n}$, because the positive square root is unique, but it does not determine the operator: neither the scale of $\tilde Q_H$ nor the unitary factor $\tilde U$ in $\tilde Q=\tilde Q_H\tilde U$ is fixed by the state. The fibre is a positive scale times the unitary group.
- **The square is not a product of two states.** $\tilde{Ϛ}_Q=\tilde Q_{\mathrm n}^{2}$ is the square of a positive element, not the product of two copies of the state; the two coincide only when the state is pure.

**The boundary.** The reading "the state is the square of an amplitude" is an algebraic identity, not an ontology. It says that a state can always be presented as a squared positive element, and that an operator presents it that way canonically. It does not say that the amplitude is more real than the state, and it does not supply a dynamics for either. The operator-to-state map is developed in *The General Polar Decomposition, the Amplitude and the Operator-to-State Map*.

## The State and the Observable in One Space

A general observable of the informational sector is an element

$$
\tilde{H}=h_t e_t+i\,\vec h,\qquad h_t\in\mathbb{R},\quad \vec h\in\mathbb{R}^3,
$$

of the same subspace $\mathbb{M}_+$. The state $\tilde{Ϛ}=\tfrac12(e_t+i\vec r)$ is a particular case: an observable with $h_t=\tfrac12$ and $\vec h=\tfrac12\vec r$, positive and normalised, $\langle\tilde{Ϛ},e_t\rangle_{*}=\tfrac12$. **States are positive normalised observables** (trace one in the $2\times2$ image). The standard formalism also represents states and observables by operators, but there the state is standardly read as a functional — a positive normalized linear map on observables — while the observable enters as the object acted upon. In the biquaternion framework the distinction is not one of kind and not one of dual space: it is the conjunction of two conditions, positivity and normalisation, imposed on elements of one four-dimensional real space.

Two facts make the cohabitation exact. First, the Hermitian form $\langle\tilde{Ϛ},\tilde{H}\rangle_{*}=\mathrm{Sc}(\tilde{Ϛ}\tilde{H}^{*})$ is a positive-definite symmetric form on $\mathbb{M}_+$, with Gram matrix the identity in the basis $\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$; with the state normalised against the unit, the Born weight is

$$
\boxed{\;\frac{\langle\tilde{Ϛ},\tilde{H}\rangle_{*}}{\langle\tilde{Ϛ},e_t\rangle_{*}}=h_t+\vec r\cdot\vec h\;},
$$

and the trace reads it as $\mathrm{Tr}(\tilde{Ϛ}\tilde{H}^{*})=h_t+\vec r\cdot\vec h$, with $\mathrm{Tr}(e_t)=2$. Second — and this is the point for the ontology — because the form is positive definite, the map

$$
\tilde{Ϛ}\ \longmapsto\ \left(\tilde{H}\mapsto \frac{\langle\tilde{Ϛ},\tilde{H}\rangle_{*}}{\langle\tilde{Ϛ},e_t\rangle_{*}}\right)
$$

is injective: an element of $\mathbb{M}_+$ is determined by its pairings with observables. So the state, regarded as a functional on observables, is an element of the very space on which it is a functional; $\mathbb{M}_+$ is its own dual under the plain form (equivalently under the trace in the $2\times2$ image), and there is no second space in which the state lives.

That the state is a *positive* functional is part of the same structure. If $\tilde{H}\geq0$, meaning $h_t\geq|\vec h|$, then

$$
\mathrm{Tr}(\tilde{Ϛ}\tilde{H}^{*})=h_t+\vec r\cdot\vec h\ \geq\ |\vec h|-|\vec r|\,|\vec h|=\left(1-|\vec r|\right)|\vec h|\ \geq\ 0 .
$$

Positivity of the functional is thus not an extra postulate; it is the positivity condition $|\vec r|\leq1$ of the state seen from the dual side.

**Interpretation.** The cohabitation of states and observables is a structural fact; what it means is an interpretation. The natural interpretation is that the framework refuses a dualistic picture in which "states of information" inhabit a different kind of object from "physical quantities". A more cautious interpretation is that the coincidence is a feature of working in $\mathbb{B}\cong M_2(\mathbb{C})$, where states and effects are both matrices. The algebra does not decide between these interpretations, and the fact that it does not is itself a datum: it locates the ontological question elsewhere than in a state/observable dichotomy.

## Convexity, Extremality, and the Superposition Principle

The states form a **convex set**. If $\tilde{Ϛ}_1,\tilde{Ϛ}_2$ are states and $\lambda\in[0,1]$, then $\lambda\tilde{Ϛ}_1+(1-\lambda)\tilde{Ϛ}_2$ is Hermitian, normalised, and positive — a state. In Bloch coordinates this is the convexity of the ball. The **pure** states, $|\vec r|=1$, are its **extreme points**: if a pure state is written as a nontrivial convex combination of two states, the two must coincide with it. For distinct unit vectors $\vec r_1\neq\vec r_2$ and $\lambda\in(0,1)$ one has $|\lambda\vec r_1+(1-\lambda)\vec r_2|<1$ strictly, by the triangle inequality, with equality only for $\vec r_1=\vec r_2$. Every mixed state, $|\vec r|<1$, is an interior point and admits a nontrivial decomposition; its spectral decomposition

$$
\tilde{Ϛ}=\lambda_+\tilde\Pi_1(\vec u_r)+\lambda_-\tilde\Pi_2(\vec u_r),\qquad \lambda_\pm=\tfrac12\left(1\pm|\vec r|\right),
$$

is one, and the spectral decomposition is unique for $\vec r\neq0$.

The state space is a convex body, not a vector space, and the difference matters. The sum of two states is not a state: $\langle\tilde{Ϛ}_1+\tilde{Ϛ}_2,e_t\rangle_{*}=\langle e_t\rangle$, and a scalar multiple of a state is not a state either. In particular the **superposition principle is not a statement about the state space**. Superposition belongs to the spinor module of $\mathbb{B}$ — the complex two-dimensional module entering the correspondence of *The Informational Sector: States, Observables and Probability* — which is a vector space; the states are the positive normalised elements built from that module, and they form the convex ball. The framework's state is therefore not a vector to be added and not a ray to be projected: it is a convex element whose extreme points are the pure states.

**Interpretation.** Convexity gives a precise sense to "the state is a mixture": a mixed state is literally a convex combination of pure states in its own space, and the combination is an element of that space, not a classical probability distribution placed alongside it. This is a suggestive picture — the state as a point of a convex body whose extreme points are the pure states — but it is a picture. It does not by itself say whether the convex point is a real object or a representation of ignorance; and since the decomposition into non-orthogonal pure states is not unique (the next section), the same convex point can be presented as many different mixtures.

## The Pure State Is an Idempotent and a Zero Divisor

A state is pure exactly when $\tilde{Ϛ}^2=\tilde{Ϛ}$, which is exactly $|\vec r|=1$, which is exactly $\langle\tilde{Ϛ}\rangle_{\natural}=0$. The last equality says that the pure states at the normalisation $\langle\tilde{Ϛ},e_t\rangle_{*}=\tfrac12$ (trace one in the $2\times2$ image) are exactly the **zero divisors** of $\mathbb{B}$ on that slice: a pure state is a nonzero element that annihilates a nonzero element, explicitly

$$
\tilde\Pi_1(\vec u)\,\tilde\Pi_2(\vec u)=0,\qquad \tilde\Pi_{1,2}(\vec u)=\tfrac12\left(e_t\pm i\vec u\right),
$$

with $\vec u$ a unit pure real quaternion, and $\tilde\Pi_1+\tilde\Pi_2=e_t$. In the matrix representation $\mathbb{B}\cong M_2(\mathbb{C})$ a pure state is a rank-one projector, with vanishing determinant, while a mixed state is invertible and of rank two, with $\det=\langle\tilde{Ϛ}\rangle_{\natural}=\tfrac14(1-|\vec r|^2)\neq0$. Purity, idempotence, extremality, and being a zero divisor are the same condition on the element.

**Established, and recomputed.** For random pure states the idempotence, the vanishing biquaternion norm, the annihilation identity, and the vanishing determinant all hold; for random mixed states the failure of idempotence and the non-vanishing determinant hold. The determinant identity $\det\varphi(\tilde{Q})=\langle\tilde{Q}\rangle_{\natural}$ for the matrix representation $\varphi$ was checked on random biquaternions, which is what identifies the biquaternion-norm-zero set with the singular, hence zero-divisor, set.

**Interpretation.** Purity as an annihilation property is a genuinely algebraic way to state what purity is, and it is suggestive: a pure state is an element blind to its complement, in the exact sense that $\tilde\Pi_1$ annihilates $\tilde\Pi_2$. Whether that blindness should be read as a feature of physical reality or as a feature of the algebra is not decided by the algebra, and it is one of the interpretations the next sections leave open.

## What the Element Does Not Carry

Two negative facts about the state element are as structural as the positive ones.

**Provenance-blindness.** The state carries no record of how it was prepared. The algebra shows this directly: a mixed state has many ensemble decompositions. For a state with Bloch vector $\vec r$, $|\vec r|<1$, and a unit direction $\vec u$ orthogonal to $\vec r$, put $t=\sqrt{1-|\vec r|^2}$, so that $\vec r_\pm=\vec r\pm t\vec u$ are unit vectors. Then

$$
\tilde{Ϛ}=\tfrac12\,\tilde\Pi_1(\vec r_+)+\tfrac12\,\tilde\Pi_1(\vec r_-)
$$

is an ensemble decomposition with two pure states of the same type, distinct from the spectral decomposition (which uses one $\tilde\Pi_1$ and one $\tilde\Pi_2$). The maximally mixed state is the sharpest case: $\tfrac12 e_t=\tfrac12\tilde\Pi_1(\vec u)+\tfrac12\tilde\Pi_2(\vec u)$ for *every* unit $\vec u$. The element is the same under all of these preparations, so it cannot be a catalogue of which preparation occurred. *The Measurement Problem in Algebraic Form* states the same fact as the provenance-blindness of the state, and uses it to explain why a proper and an improper mixture are the same element of $\mathbb{M}_+$.

**No outcome index.** The state determines the Born probabilities

$$
p_\pm=\frac{\langle\tilde\Pi_{1,2}(\vec u_h),\tilde{Ϛ}\rangle_{*}}{\langle\tilde{Ϛ},e_t\rangle_{*}}=\frac{\mathrm{Sc}(\tilde\Pi_{1,2}(\vec u_h)\tilde{Ϛ}^{*})}{\mathrm{Sc}(\tilde{Ϛ})}=\frac{\mathrm{Sc}(\tilde\Pi_{1,2}(\vec u_h)\tilde{Ϛ})}{\mathrm{Sc}(\tilde{Ϛ})}=\frac{\operatorname{Tr}(\tilde\Pi_{1,2}(\vec u_h)\tilde{Ϛ})}{\operatorname{Tr}(\tilde{Ϛ})}=\tfrac12\left(1\pm\vec u_h\cdot\vec r\right)
$$

of a measurement along $\vec u_h$, and nothing about which outcome occurs. No element of $\mathbb{M}_+$ and no operation of the algebra carries the index $\pm$; that is the selection problem in algebraic form, established in the measurement-problem article and not resolved here. In the geometric language of that article the statistics determine the segment — the pointer diameter — and the outcomes are its endpoints; the element is the segment.

**Established, inherited, and not repaired.** Both facts are properties of the element at the single-qubit level. They are stated here because they bound what any ontology of the state can claim: an element that carries neither provenance nor outcome cannot be a complete description of an individual measurement event, whatever else it is. In two clauses: the element is **operationally complete** — it determines every statistic and is determined by them — and **ontically incomplete** — it determines no outcome and records no preparation.

## The State Is Not a Spacetime Object, and Not a Spinor Ray

The complementarity $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ assigns the state to the informational side. The four-vectors of relativistic physics — position, velocity, momentum, potential, current — lie in $\mathbb{M}_-$, with imaginary scalar part and real vector part; the state has real scalar part and imaginary vector part, so it lies in $\mathbb{M}_+$ and has zero component in $\mathbb{M}_-$. The state is therefore not a configuration in spacetime and not a four-vector; it is an element of the complementary sector. Its relation to the material sector is not that of a configuration but that of an operator: the elements of $\mathbb{M}_+$ act on $\mathbb{M}_-$ by conjugation, and the biquaternion-norm-preserving, unit-norm ones among them are the Lorentz boost rotors. A state is not one of them. Its biquaternion norm is $\langle\tilde{Ϛ}\rangle_{\natural}=\tfrac14(1-|\vec r|^2)\in[0,\tfrac14]$, never $1$, so no state has unit norm; the state is not an action on spacetime either, but a normalized positive element of the operator subspace.

The state is equally not a spinor ray. In the correspondence of *The Informational Sector: States, Observables and Probability*, the spinor module of $\mathbb{B}$ corresponds to the Hilbert space $\mathbb{C}^2$ and the pure states correspond to the rank-one density operators. The framework's state is the second object, not the first: the pure state is the idempotent $\tilde\Pi_{1,2}(\vec u)$, and the passage from a module element to a state is the rank-one projection onto it. A central phase $\psi\mapsto \exp(i\theta)\psi$ leaves the idempotent unchanged, because $\exp(i\theta)$ lies in the centre $\mathbb{C}_{\mathbb{B}}$; the phase of the spinor is therefore not part of the state. So the framework's state is not a vector and not a ray: it is the idempotent built from the ray, with the phase already quotiented out, and for a mixed state there is no spinor to build it from at all.

**Established.** These are statements about which subspace the state lies in and which object the framework calls the state. The interpretive consequence — that a "wavefunction ontology" and a "density-operator ontology" are not merely two interpretations of one object but, in this framework, interpretations of two different objects — is an interpretation, and it is labelled as one.

## Ontological Readings and What the Algebra Decides

We can now separate what the algebra settles from what it leaves to interpretation.

**Settled by the algebra.**

1. **Identity.** A state is a positive element of $\mathbb{M}_+$ normalised by $\langle\tilde{Ϛ},e_t\rangle_{*}=\tfrac12\langle e_t\rangle_{*}$, equivalently a point of the Bloch ball, equivalently a normalised element of the future light cone of the biquaternion norm. The identification is canonical: the plain form and $e_t$ are intrinsic to the algebra, no choice of matrix representation enters, and the only convention is the scale $\langle e_t\rangle_{*}=1$.
2. **Determinacy of statistics.** The element determines every measurement statistic, through the plain form (the trace in the $2\times2$ image), and is determined by them, because the form is positive definite.
3. **Convex structure.** States form a convex body whose extreme points are the pure states; mixedness is a convex combination in the same space; purity is idempotence and zero-divisorhood; the mixedness of a state is the single scalar $\mathrm{Sc}(\tilde{Ϛ}^2-\tilde{Ϛ})$.
4. **Blindness.** The element carries neither provenance nor outcome index.

**Interpretations the algebra permits.** Four familiar interpretations can be stated in these terms.

- **State realism.** The element is a real, determinate feature of the world. The algebra is compatible: the element is canonical and observer-independent, and nothing in the framework introduces an observer or a preparation into its definition. The cost is that the element then does not determine the outcome, which is exactly the selection problem; a state-realist interpretation must therefore be one on which the state is not a complete description of an individual event.
- **Epistemic or statistical interpretation.** The element summarizes an agent's information or the statistics of an ensemble. The algebra is compatible: the element is provenance-blind and determines statistics. The cost is that there is no agent and no ensemble anywhere in the algebra, and the element is not a bookkeeping table but a geometric object in the same space as the observables, with a canonical inner product and a canonical cone. An epistemic interpretation must explain why a summary of information has the geometry of a convex body of operators.
- **Relational interpretation.** The state is defined relative to a measurement context. The algebra is compatible in that the state's meaning is exhausted by its pairings with observables; the cost is that the element itself is context-independent — the same element enters every pairing — so the relation would have to live in the act of pairing, which is not an object of the algebra.
- **Structural interpretation.** What is real is the structure — the algebra, its subspaces, its pairings, its convex state space — rather than any particular element. The algebra is compatible, and this interpretation asks least of it. The cost is the familiar one of structural realism: it must say what distinguishes the structure that is realised from the many that are not.

**What is not settled.** The algebra decides none of these interpretations. It decides what a state *is* and what it *does*; it does not decide what a state is *of*. An added structure — a selection rule, a space of beables, an observer index, a preferred decomposition — would decide among the interpretations, and the algebra contains no such structure. **This article takes no position among the four.** It claims only that the framework's contribution to the debate is to fix the disputed object more sharply than the standard formalism does, and thereby to relocate the dispute: the question "is the state real?" becomes the question "is $\mathbb{M}_+$ real?".

## The Informational-Sector Hypothesis and the Ontology of the State

The framework's own interpretive hypothesis is stated in *The Informational Sector: States, Observables and Probability*: that $\mathbb{M}_+$ is not only a mathematical structure but an **informational sector** of the world, physically realised as the material sector $\mathbb{M}_-$ is. That article is explicit that the algebraic identification of $\mathbb{M}_+$ with the observables of a qubit is established, while the physical realisation is a hypothesis.

Granting the hypothesis, the ontology of the state follows in one step. If $\mathbb{M}_+$ is a physical sector, then its elements are physical; a state, being positive and normalised, is a physical element of that sector; the Bloch ball is a physical convex body; and the interpretations above are interpretations of a physical object. This is a **sectorial realism** about the state: the state is real, but its reality is the reality of the sector, not a separate postulate. Denying the hypothesis, the state is a mathematical element of a reformulation of quantum physics — real only as mathematics — and the interpretations above are interpretations of a formalism.

The point of separating the two is that the algebra cannot make the choice. The same equations, the same identities, and the same state space serve under either interpretation; the difference is a commitment about the physical status of a subspace, and the algebra does not contain that commitment. **This is the article's central interpretive claim, and it is offered as a claim, not a result:** the ontology of the quantum state under the biquaternion framework is not an independent question but the ontology of $\mathbb{M}_+$, and the algebra relocates the question rather than answering it.

**A caution against over-reading.** The sector hypothesis does not by itself supply an outcome, a preferred basis, or a dynamics of the sector; those remain open in the parent article. Sectorial realism is therefore not a solution to the measurement problem, and it should not be presented as one. It is an interpretation of what the element is, not a completion of what the element does.

## What the Algebra Does Not Decide

The gaps are as much a part of the ontology as the results. Stated at the single-qubit level the framework supports:

1. **The selection of an outcome.** No element and no operation selects an outcome as a function of the state. The statistics are determined; the outcome is not. Sectorial realism does not repair this.
2. **The preferred basis.** The pointer direction is an input to decoherence, not an output of the algebra. A state with $\vec r\neq0$ has a canonical spectral decomposition, but its eigenbasis is not selected by any physical interaction, and it is not the pointer basis of a measurement.
3. **The provenance of ensembles and the proper/improper distinction.** The element does not distinguish a proper from an improper mixture; whether that distinction has physical content is not decided by the algebra, and the record that would carry it is not in $\tilde{Ϛ}$.
4. **Many-qubit ontology.** The state of $n$ qubits is a positive element of $\mathbb{M}_+^{\otimes n}$ with $\mathrm{Sc}(\tilde{Ϛ})=2^{-n}$ (trace one in the $2^n\times2^n$ image); the tensor product, the partial trace, and the reduced states are inherited rather than derived, and the ontology of a reduced state — its relation to the joint element — is treated in *Entangled Subsystems in the Biquaternion Framework* and is not developed here.
5. **Field-theoretic and relativistic states.** The state described is a single-qubit state. The Lorentz action is on $\mathbb{M}_-$; the state lives in $\mathbb{M}_+$ and is not a Lorentz-covariant object in the same sense. A relativistic, many-particle state is not developed here.
6. **Empirical content.** As everywhere in the framework, whether any of this yields a prediction distinguishing it from standard quantum physics is open. An interpretation of a formalism with the same predictions cannot be decided by experiment unless the formalism is extended.

## Summary

The quantum state in the biquaternion framework is a **positive element of the Hermitian subspace $\mathbb{M}_+$, normalised by $\langle\tilde{Ϛ},e_t\rangle_{*}=\tfrac12\langle e_t\rangle_{*}$**,

$$
\tilde{Ϛ}=\tfrac12\left(e_t+i\vec r\right),\qquad |\vec r|\leq1 ,
$$

equivalently a point of the Bloch ball, equivalently a normalised element of the future light cone of the biquaternion norm. Its purity is idempotence, $|\vec r|=1$, equivalently vanishing of the biquaternion norm and zero-divisorhood at that normalisation; its mixedness is the single scalar $\tilde{Ϛ}^2-\tilde{Ϛ}=\tfrac14(|\vec r|^2-1)e_t$. States and observables are elements of the same four-dimensional real space, distinguished only by positivity and normalisation; the normalised Hermitian form $\langle\tilde{Ϛ},\tilde{H}\rangle_{*}/\langle\tilde{Ϛ},e_t\rangle_{*}=h_t+\vec r\cdot\vec h$ makes the state a positive normalized functional on that space, its positive definiteness makes the space its own dual, and the trace $\mathrm{Tr}(\tilde{Ϛ}\tilde{H}^{*})=h_t+\vec r\cdot\vec h$ is the $2\times2$ reading of the same functional. The states form a convex body whose extreme points are the pure states, so superposition is a property of the spinor module, not of the state space.

Two negative facts bound the ontology. The element is **provenance-blind** — it has many ensemble decompositions, and the maximally mixed state has one for every basis — and it carries **no outcome index**, the probabilities $p_\pm$ being determined while the realised outcome is not. The state is not a spacetime object, lying in the sector complementary to the four-vectors; and it is not a spinor ray, being the idempotent built from the ray with the central phase already quotiented out. It is the Hermitian square of a positive amplitude, $\tilde{Ϛ}_Q=\tilde Q_{\mathrm n}^{2}$, and the passage from the operator to the state forgets the unitary fibre.

The article's interpretive claim is that the algebra settles the identity, the statistics, the convex structure, and the blindness of the state, and settles nothing about its physical status. State realism, the epistemic interpretation, the relational interpretation, and the structural interpretation are all compatible with the algebra, and the algebra decides none of them; an added structure would be needed to do so, and there is none. The framework's own commitment is the informational-sector hypothesis, under which the state is a physical element of a physical sector — a sectorial realism offered as a hypothesis, not a result. The ontology of the quantum state is therefore the ontology of $\mathbb{M}_+$, and the algebra relocates the question rather than answering it. The selection of an outcome, the preferred basis, the proper/improper distinction, the many-qubit and field-theoretic extensions, and empirical contact remain open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $i$ | Scalar imaginary, $i^2 = -1$, central |
| $\mathbb{M}_+$ | Hermitian subspace (informational sector): real scalar, imaginary vector |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material sector): imaginary scalar, real vector |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}$ | Real-quaternion subspace; complex scalar centre |
| $\tilde{Ϛ} = \tfrac12(e_t + i\vec r)$ | State, $\lvert\vec r\rvert\leq1$ (Bloch ball) |
| $\tilde\Pi_{1,2}(\vec u) = \tfrac12(e_t \pm i\vec u)$ | Pure state (Hermitian idempotent, rank one, zero divisor) |
| $\tilde{H} = h_te_t + i\vec h$ | Observable (general Hermitian element) |
| $\langle\tilde{H}\rangle_{\natural} = \tilde{H}\tilde{H}^{\natural}$ | Biquaternion norm, signature $(1,3)$ on $\mathbb{M}_+$ |
| $\langle\tilde{Ϛ}\rangle_{\natural} = \tfrac14(1-\lvert\vec r\rvert^2)e_t$ | Biquaternion norm of a state; positivity $\Leftrightarrow\langle\tilde{Ϛ}\rangle_{\natural}\geq0$ |
| $\tilde{Ϛ}^2 - \tilde{Ϛ} = \tfrac14(\lvert\vec r\rvert^2-1)e_t$ | Deviation from idempotency (mixedness) |
| $\mathrm{Tr}(\tilde Q)=2\,\mathrm{Sc}(\tilde Q)$ | Trace |
| $\langle\tilde{Ϛ},\tilde H\rangle_{*}/\langle\tilde{Ϛ},e_t\rangle_{*} = h_t + \vec r\cdot\vec h$, with trace reading $\operatorname{Tr}(\tilde{Ϛ}\tilde{H}^{*})=\operatorname{Tr}(\tilde{Ϛ}\tilde{H})$ | Born rule; form first, trace at normalisation last |
| $\lambda_\pm = \tfrac12(1\pm\lvert\vec r\rvert)$ | Eigenvalues of $\tilde{Ϛ}$ |
| $\vec u, \vec u, \vec u_h, \vec u_r$ | Unit pure real quaternions (directions) |
| ${}^{*} = ({}^{\natural})^{\,*}$ | Hermitian conjugation |

## Further Reading

- [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html), for the algebra $\mathbb{B}$, its two sectors, and the conjunctions.
- [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), for the operator-algebra identification and the informational-sector hypothesis.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), for the four-vectors and the complementarity $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$.
- [Quantum Physics in Biquaternionic Form](quantum-physics-in-biquaternionic-form.html), for the state and observable formalism, the Bloch ball, and the Born rule.
- [The Bloch Ball as the Normalised Slice of the Future Light Cone](the-bloch-ball-as-the-trace-one-slice-of-the-future-light-cone.html), for the state space as a slice of the cone and purity as a boundary condition.
- [The Born Rule from the Hermitian Form — Derivation and Comparison](the-born-rule-as-a-trace-formula-derivation-and-comparison.html), for what the Hermitian form, read through the trace, derives and what it restates.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html) and [The Biquaternion Eigenvalue Decomposition](../articles_maths/the-biquaternion-eigenvalue-decomposition.html), for the algebraic structure of idempotents, rank-one elements, and zero divisors used in the purity section.
- [The Measurement Problem in Algebraic Form](the-measurement-problem-in-algebraic-form.html), for provenance-blindness, the missing outcome index, and the segment-versus-endpoint gap.
- [Decoherence as Idempotent Projection](decoherence-as-idempotent-projection.html), for the deformation of an idempotent into a mixed state.
- [Entangled Subsystems in the Biquaternion Framework](entangled-subsystems-in-the-biquaternion-framework.html), for reduced states and the tensor-product structure.
- [Quantum Channels and the Reversible/Irreversible Dichotomy](quantum-channels-and-the-reversible-irreversible-dichotomy.html), for the operation-form interpretation of evolution and measurement.
- [The Quantum–Classical Divide in the Biquaternion Framework](the-quantum-classical-divide-in-the-biquaternion-framework.html), for idempotent versus unitary operations.
- [Quantum Physics: Foundations and Structure](quantum-physics-foundations-and-structure.html), for the standard formulation and the structural checklist.
- [The General Polar Decomposition, the Amplitude and the Operator-to-State Map](the-general-polar-decomposition-amplitude-and-the-operator-to-state-map.html), for the state as the Hermitian square of the amplitude.
