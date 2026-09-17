
# The Quantum-Relativity Tension and the Biquaternion Framework

I think your instinct is right, and it's worth being precise about where the difficulty lies and what the biquaternion framework might offer.

## The tension

Quantum mechanics and relativity do not sit comfortably together. The difficulties are structural, not technical:

- **Time is a parameter in QM, a coordinate in relativity.** In the Schrödinger equation, $t$ is an external parameter, not an observable. In relativity, time is one coordinate among four, and it transforms with the others. This asymmetry is the origin of many of the "problems of time" in quantum gravity.
- **The Born rule is axiomatic.** The probability interpretation of the wave function is postulated, not derived. There is no structural reason for $|\psi|^2$ inside the standard formalism.
- **Spin–statistics is a theorem that requires QFT.** The connection between spin and statistics cannot be derived in non-relativistic QM; it requires the relativistic framework and the spin–statistics theorem.
- **Measurement is outside the formalism.** The unitary evolution is smooth and deterministic; the collapse is discontinuous and probabilistic. The two do not fit into a single equation.
- **Quantization is a recipe, not a derivation.** There is no unique procedure that takes a classical theory to its quantum version. Canonical quantization, path integral quantization, and deformation quantization give different (though sometimes equivalent) results, and the choice is not derived from first principles.
- **The path integral requires a trick.** The oscillatory path integral is not convergent, and the standard way to make sense of it is the Wick rotation — which is a trick, as we discussed.
- **Non-locality and causality are in tension.** Entanglement correlations appear to be non-local, but relativistic causality forbids superluminal signalling. Reconciling the two requires care.

Each of these has been addressed in various ways. None is fully resolved.

## What the biquaternion framework has

The biquaternion framework has a small number of structural features that standard QM does not have. They are worth listing precisely.

**1. States and observables live in the same subspace.** In standard QM, states are vectors in a Hilbert space and observables are Hermitian operators on that space. They are different kinds of objects, related by the Born rule. In the biquaternion framework, the states are the idempotents of $\mathbb{M}_+$, and the observables are the Hermitian elements of $\mathbb{M}_+$. They are both elements of the same subspace, and they are related algebraically by the trace formula.

**2. Symmetries and operators are the same.** In standard QM, the symmetries of the theory (the Lorentz group, the Poincaré group) act on the Hilbert space, while the observables are separately given. In the biquaternion framework, the Lorentz rotors live in $\mathbb{M}_+$, which is the same subspace as the observables. The symmetry group and the operator algebra are aspects of the same structure.

**3. The Born rule is algebraic.** For spin-1/2, the trace formula $\mathrm{Tr}(PH) = 2\mathrm{Sc}(PH)$ gives the Born rule. It is a consequence of the algebra, not an independent postulate. Whether this extends to larger systems is an open question, but the fact that it holds for the elementary case is significant.

**4. Time is intrinsic.** In the material sector $\mathbb{M}_-$, the time coordinate is $ict$. The imaginary character of time is algebraic, not a computational device. The "problem of time" in QM arises from the asymmetry between a parametric time and a coordinate time; in the biquaternion framework, this asymmetry is resolved by the algebra itself.

**5. The reversible–irreversible distinction is structural.** In standard QM, unitary evolution and measurement collapse are two different kinds of processes, and the distinction is added by hand (via the measurement postulate). In the biquaternion framework, unitary elements and idempotent elements are two natural classes of elements of $\mathbb{M}_+$, distinguished algebraically: unitary elements preserve the norm form, idempotent elements do not. The distinction is structural.

**6. The spin–statistics structure is algebraic.** Fermions live in the fundamental module of the algebra (spinor representation), and bosons may naturally live in the vector or Hermitian subspaces. If this can be made precise, the connection between spin and statistics might be derivable from the algebra.

**7. The framework is already relativistic.** The Lorentz group acts on the material sector $\mathbb{M}_-$ by rotor conjugation, and the rotors are in $\mathbb{M}_+$. The framework is not a non-relativistic theory that needs to be made relativistic; it is relativistic from the start.

## The directions of research

I would rank the possible directions by how promising they seem, and by how much of the standard formalism they might replace.

### Direction 1 — The idempotent formalism for quantum states

**The idea.** Take seriously the identification: states are idempotents of $\mathbb{M}_+$ (or convex combinations of them), and observables are Hermitian elements of $\mathbb{M}_+$. Develop the quantum formalism in this language.

**Why it's promising.** The Born rule is already present as the trace formula. The distinction between pure and mixed states is algebraic (idempotent vs. non-idempotent Hermitian). The reversible–irreversible distinction is algebraic. Time evolution is generated by rotor conjugation. The framework is self-contained for the qubit.

**What's open.** How does this extend to more than one qubit? What is the tensor product in the biquaternion language? Does the resulting formalism reproduce standard QM, or does it differ?

**The risk.** This is essentially QM in the biquaternion language. It may not give new results, but it may clarify the structural content of QM.

### Direction 2 — Spin–statistics from the algebra

**The idea.** Fermions live in the fundamental module of $\mathbb{B}$ (the spinor representation). Bosons may naturally live in other representations — the vector representation of $\mathbb{M}_-$, or the Hermitian representation of $\mathbb{M}_+$. If this identification can be made precise, the connection between spin and statistics might follow from the algebra.

**Why it's promising.** The spin–statistics theorem in standard QFT is derived from the requirements of relativistic invariance and positivity of energy. In the biquaternion framework, these requirements might be expressible as algebraic constraints on the representations of the algebra. If so, the theorem would follow from the algebra, not from the field-theoretic axioms.

**What's open.** What is the bosonic representation of $\mathbb{B}$? How do commutation relations for bosons vs. anti-commutation relations for fermions emerge from the algebra? Is there a single structural statement that covers both?

**The risk.** The identification of bosons with a specific subspace of $\mathbb{B}$ is not obvious. Maxwell's field strength $\tilde{F}$ is not in $\mathbb{M}_-$ or $\mathbb{M}_+$; the energy–momentum $\tilde{W}$ is in $\mathbb{H}_{\mathbb{B}}$. So the bosonic sector may be spread over multiple subspaces.

### Direction 3 — Quantization from the algebra

**The idea.** Find a natural quantization procedure that uses the algebraic structure. The symmetry group of the theory is $SL(2,\mathbb{C})$ realized as unit-norm biquaternions; the Lie algebra is $\mathfrak{sl}(2,\mathbb{C})$; the natural operators are the elements of $\mathbb{M}_+$. Commutation relations might be the natural Lie-algebraic brackets.

**Why it's promising.** The quantization of a classical theory usually requires a choice: canonical, path-integral, deformation, etc. The biquaternion framework might provide a **canonical** choice, determined by the algebra. This would remove an ambiguity in the standard formalism.

**What's open.** What are the commutation relations that follow from the algebra? Do they reproduce the standard ones, or do they differ? What is the natural Hilbert space?

**The risk.** The framework may just reproduce standard QFT, with the same ambiguities. Or it may give something genuinely different, which would then need to be reconciled with the empirical success of QFT.

### Direction 4 — Tensor products and entanglement

**The idea.** Extend the framework to $\mathbb{B} \otimes \mathbb{B} \cong M_4(\mathbb{C})$, which is the algebra of a two-qubit system. Develop the two-qubit structure, and see how the entanglement of the two spins is expressed in the biquaternion language.

**Why it's promising.** Entanglement is the source of the tension between QM and relativity (Bell's theorem, non-locality, causality). If the biquaternion framework gives a geometric or algebraic interpretation of entanglement, it might illuminate the relationship between entanglement and spacetime.

**What's open.** What is the natural tensor product in the biquaternion framework? How does the two-qubit state space relate to the two-subsystem structure? Does the framework give a new interpretation of entanglement?

**The risk.** The tensor product is a standard construction; the biquaternion framework does not obviously enrich it. The new content, if any, would come from the geometric interpretation of the tensor product.

### Direction 5 — The path integral from the algebra

**The idea.** Express the path integral using the natural measure on the algebra. The group of unit-norm biquaternions is $SL(2,\mathbb{C})$, which has a natural Haar measure. The set of idempotents of $\mathbb{M}_+$ has a natural measure (the Bloch ball). Perhaps the path integral can be written in terms of these natural measures, avoiding the ad hoc measure of standard QFT.

**Why it's promising.** The measure problem is one of the most stubborn obstacles to rigorous QFT. A natural measure from the algebra would be a real advance.

**What's open.** How does the natural measure relate to the standard Feynman measure? Does it give convergent integrals? Does it reproduce the standard results?

**The risk.** The framework does not have a dynamics that generates the path integral from first principles. Without that, the measure is just a formal object.

### Direction 6 — The measurement problem and the informational sector

**The idea.** Interpret the measurement process as a transfer between the material and informational sectors. The idempotent projection $X \mapsto PXP$ is a natural operation on $\mathbb{M}_-$-valued fields, and it might be interpreted as the effect of an informational measurement on a material state.

**Why it's promising.** The measurement problem is the most conceptually difficult issue in QM. If the biquaternion framework gives a structural interpretation of measurement, it would be a significant step.

**What's open.** What triggers the projection? What selects the idempotent $P$? How does the projection interact with the unitary evolution? Does the framework give a consistent account of the classical limit?

**The risk.** The framework gives a natural mathematical operation (idempotent projection), but it does not explain when or why it occurs. Without additional structure, this is the same as the standard measurement postulate in different notation.

### Direction 7 — Time in quantum mechanics

**The idea.** Reformulate QM with the intrinsic imaginary time of $\mathbb{M}_-$. Since time is algebraic, not parametric, the framework might resolve the asymmetry between time and space that underlies the problem of time.

**Why it's promising.** The problem of time in quantum gravity is one of the deepest open issues. If the biquaternion framework gives a natural resolution, it would be significant.

**What's open.** How does the Schrödinger equation read in the biquaternion framework? What is the time–energy uncertainty relation in this setting? Does the framework give a natural arrow of time?

**The risk.** The framework may just reformulate the standard treatment. The "problem of time" may not be resolved by algebraic structure alone.

## What I would be careful about

**First**, the biquaternion framework is not yet a quantum theory. It is a classical algebraic framework that contains the kinematic structure of a spin-1/2 system. To become a quantum theory, it needs a dynamics, a Hilbert space, and a measurement postulate — or a structural replacement for each of these.

**Second**, the framework does not obviously give new predictions. If it reproduces standard QM, its value is structural and conceptual, not empirical. If it gives new predictions, they must be reconciled with the empirical success of standard QM.

**Third**, the framework is not yet developed as a quantum theory. The companion articles on the Dirac equation and relativistic mechanics treat the classical aspects. The quantization, the many-body structure, and the measurement theory are not developed.

**Fourth**, the framework sits in a crowded space. There are already several reformulations of QM: geometric algebra (Hestenes, Doran–Lasenby), algebraic QFT (Haag–Kastler), operational QM (Hardy, Chiribella), quantum information (Hardy, Barrett). The biquaternion framework has to say what it adds.

## My recommendation

I would start with **Direction 1 (the idempotent formalism)** and **Direction 2 (spin–statistics from the algebra)**, in that order. Direction 1 is the foundation: it establishes that the framework can carry the quantum structure. Direction 2 is the most promising direction for a genuinely new result: a structural derivation of the spin–statistics theorem from the algebra.

Direction 3 (quantization) and Direction 4 (entanglement) are natural extensions of Direction 1. Direction 5 (path integral) and Direction 6 (measurement) are more speculative. Direction 7 (time in QM) is the deepest but also the least developed.

The first step is to write down the idempotent formalism carefully. This is a well-defined mathematical task: express the standard qubit formalism in the language of $\mathbb{M}_+$-idempotents and $\mathbb{M}_+$-Hermitian elements, and see what structure emerges. If the structure is clean and reproduces the standard results, the formalism is viable. If it suggests new structure, we can develop it further.

