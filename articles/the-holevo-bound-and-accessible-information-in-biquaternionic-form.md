# __The Holevo Bound and Accessible Information in Biquaternionic Form__

## Introduction

A quantum source produces a state drawn from an ensemble. The receiver may perform any measurement the algebra admits, and from the outcome tries to recover the index of the state that was sent. How much of the source's classical information can be extracted in this way is the **accessible information** of the ensemble, and its universal upper bound is the **Holevo bound**. This article develops both in the biquaternion language of the informational sector.

The two objects at issue are the ensemble and the measurement. In the framework both are elements of the Hermitian subspace: the ensemble is a family of positive trace-one elements $\tilde{\rho}_x$ with weights $p_x$, and the measurement is a family of positive elements $\tilde{E}_y$ summing to the identity, the **POVM** developed in the companion article on the positive cone. The outcome probabilities are the trace pairing

$$
p(y|x) = \mathrm{Tr}\bigl(\tilde{\rho}_x\tilde{E}_y\bigr) = 2\,\mathrm{Sc}\bigl(\tilde{\rho}_x\tilde{E}_y\bigr),
$$

which is the Born rule. The accessible information is the classical mutual information of this channel, maximized over measurements; the Holevo quantity is the entropy difference

$$
\chi = S(\bar{\tilde{\rho}}) - \sum_x p_x\,S(\tilde{\rho}_x),
\qquad
\bar{\tilde{\rho}} = \sum_x p_x\,\tilde{\rho}_x ,
$$

and the Holevo bound is $I_{\mathrm{acc}}\leq\chi$.

The biquaternion reading locates the ingredients algebraically. The average state is an element of $\mathbb{M}_+$; for a qubit its entropy is a function of its norm form, $S(\bar{\tilde{\rho}}) = H(N(\bar{\tilde{\rho}}))$, so the Holevo quantity of a pure-state ensemble is a single norm-form function. The measurement is a completely positive trace-preserving map carrying the state to a commutative subalgebra; the accessible information is what survives that map. The content of the Holevo bound is then the data-processing inequality: a measurement cannot increase the classical information available about the source. The framework reproduces the bound and exposes which algebraic invariant it is about; it does not change the number it gives.

The article proceeds as follows. Ensembles and POVMs are set up on $\mathbb{M}_+$, and the accessible information is defined. The Holevo quantity is introduced and its basic properties are derived, including the qubit form in terms of the norm form. The Holevo bound is stated and its proof is sketched through the data-processing inequality, with the biquaternion reading of each step. Worked examples follow: orthogonal states, where the bound is saturated, and two non-orthogonal pure states, where it is not. A closing section separates what is algebraic from what is standard information theory.

## Ensembles and Measurements in $\mathbb{M}_+$

### Ensembles

An **ensemble** is a finite family of states with weights:

$$
\mathcal{E} = \bigl\{p_x,\ \tilde{\rho}_x\bigr\}_{x\in\mathcal{X}},
\qquad p_x\geq0, \quad \sum_x p_x = 1, \qquad
\tilde{\rho}_x = \tfrac{1}{2}\bigl(e_0 + i\mathbf{r}_x\bigr), \quad |\mathbf{r}_x|\leq1 .
$$

The **average state** is the convex combination

$$
\bar{\tilde{\rho}} = \sum_x p_x\,\tilde{\rho}_x = \tfrac{1}{2}\bigl(e_0 + i\bar{\mathbf{r}}\bigr),
\qquad \bar{\mathbf{r}} = \sum_x p_x\,\mathbf{r}_x ,
$$

which is again a state, since convexity preserves positivity and trace. The norm form of the average state is $\tfrac14(1-|\bar{\mathbf{r}}|^2)e_0$, a function of the mean Bloch vector. Its entropy is, for a qubit,

$$
S(\bar{\tilde{\rho}}) = h\!\left(\frac{1+|\bar{\mathbf{r}}|}{2}\right),
\qquad h(p) = -p\log p-(1-p)\log(1-p),
$$

as follows from the spectrum $\tfrac12(1\pm|\bar{\mathbf{r}}|)$; the entropy is read from the norm form of the average state and from the norm forms of the individual states, $S(\tilde{\rho}_x) = h\!\left(\tfrac{1+|\mathbf{r}_x|}{2}\right)$.

### Measurements as POVMs

A **measurement** with outcome label $y$ is a **positive operator-valued measure**: a family of Hermitian elements

$$
\tilde{E}_y \geq 0, \qquad \sum_y \tilde{E}_y = e_0 ,
$$

each of which is an **effect**, $0\leq\tilde{E}_y\leq e_0$. The probability of outcome $y$ given the state $\tilde{\rho}_x$ is the trace pairing $p(y|x) = \mathrm{Tr}(\tilde{\rho}_x\tilde{E}_y)$; positivity of the effect ensures $p(y|x)\geq0$ and $\sum_y \tilde{E}_y = e_0$ ensures $\sum_y p(y|x) = \mathrm{Tr}(\tilde{\rho}_x) = 1$. A projective measurement is the special case in which the effects are orthogonal idempotents, $\tilde{E}_y = \tilde{P}_y$ with $\tilde{P}_y^2 = \tilde{P}_y$ and $\tilde{P}_y\tilde{P}_{y'} = \delta_{yy'}\tilde{P}_y$. The cone of effects and its geometry are the subject of the companion article on POVMs and the positive cone; only these facts are used here.

For every measurement, the outcome distribution is $p_y = \sum_x p_x p(y|x) = \mathrm{Tr}(\bar{\tilde{\rho}}\tilde{E}_y)$, so the average state determines the marginal statistics. This is the reason the average state, and not the individual members, controls the first-order behaviour of the ensemble.

### The accessible information

Treat the ensemble index $X$ and the outcome $Y$ as classical random variables, with joint distribution $p(x,y) = p_x\,p(y|x)$. The **accessible information** is the mutual information maximized over all measurements,

$$
I_{\mathrm{acc}}(\mathcal{E}) = \max_{\{\tilde{E}_y\}} I(X:Y),
\qquad
I(X:Y) = H(X) - H(X|Y) = H(Y) - H(Y|X),
$$

where the entropies are the Shannon entropies of the distributions $p_x$, $p_y$, and $p(y|x)$. It is the largest amount of classical information about the source that any physical measurement can recover, and it is the operational quantity that the Holevo bound controls.

## The Holevo Quantity

### Definition and non-negativity

The **Holevo quantity** of the ensemble is

$$
\chi(\mathcal{E}) = S(\bar{\tilde{\rho}}) - \sum_x p_x\,S(\tilde{\rho}_x).
$$

It is a difference of two entropies of states in $\mathbb{M}_+$. It is non-negative by the concavity of the entropy: the entropy of the average is at least the average of the entropies,

$$
S\!\left(\sum_x p_x\tilde{\rho}_x\right) \;\geq\; \sum_x p_x\,S(\tilde{\rho}_x),
$$

which is the statement that mixing cannot decrease information. For a pure-state ensemble each $S(\tilde{\rho}_x) = 0$, and the Holevo quantity is simply the entropy of the average state,

$$
\chi = S(\bar{\tilde{\rho}}) = h\!\left(\frac{1+|\bar{\mathbf{r}}|}{2}\right)
= H\bigl(N(\bar{\tilde{\rho}})\bigr),
$$

a function of the norm form of the average state alone. This is the case of greatest interest, because a source of pure states is what a preparation device most naturally produces and because the maximal accessible information is achieved with pure states.

### The entropy of the classical-quantum state

The Holevo quantity is the quantum mutual information of a state that records the source index classically. Introduce an orthonormal register $\{|x\rangle\}$ and form

$$
\rho_{XQ} = \sum_x p_x\,|x\rangle\langle x| \otimes \tilde{\rho}_x .
$$

This is a **classical-quantum state**: block diagonal in the register, with the quantum states on the diagonal. Its entropies are

$$
S(\rho_{XQ}) = H(X) + \sum_x p_x\,S(\tilde{\rho}_x),
\qquad S(\rho_X) = H(X), \qquad S(\rho_Q) = S(\bar{\tilde{\rho}}),
$$

the first by block diagonality and the trace property, and the third because tracing out the register leaves the average state. Hence the quantum mutual information is exactly the Holevo quantity,

$$
I(X:Q) = S(\rho_X) + S(\rho_Q) - S(\rho_{XQ})
= H(X) + S(\bar{\tilde{\rho}}) - H(X) - \sum_x p_x S(\tilde{\rho}_x)
= \chi.
$$

This identity is the conceptual core: **the Holevo quantity is the mutual information between the source index and the quantum carrier, before any measurement is made.** A measurement is a further processing of the quantum system, and the Holevo bound says that it cannot increase this information. The register is bookkeeping external to $\mathbb{B}$; the quantum part of the state is an element of $\mathbb{M}_+$, and the identity uses only the trace and the block structure.

### Bounds

Because the register entropy is at most $\log|\mathcal{X}|$ and the quantum entropy at most $\log\dim_{\mathbb{C}}S = \log 2$, the Holevo quantity obeys

$$
0 \;\leq\; \chi \;\leq\; \min\bigl\{H(X),\ \log 2\bigr\} .
$$

The lower bound is attained when the average state equals a pure state, so that the ensemble is trivial; the upper bound $\log2$ is the qubit's one-bit ceiling and is attained by an ensemble of two orthogonal pure states with equal weights, as the examples below show. The bound $\chi\leq H(X)$ is the statement that the source index's own entropy limits the information carried, and it is an instance of $I(X:Q)\leq H(X)$.

## The Holevo Bound

### Statement

For every ensemble $\mathcal{E}$ and every measurement $\{\tilde{E}_y\}$,

$$
I(X:Y) \;\leq\; \chi(\mathcal{E}) = S(\bar{\tilde{\rho}}) - \sum_x p_x\,S(\tilde{\rho}_x),
$$

and therefore

$$
I_{\mathrm{acc}}(\mathcal{E}) = \max_{\{\tilde{E}_y\}} I(X:Y) \;\leq\; \chi(\mathcal{E}) .
$$

This is the Holevo bound, sometimes called the Holevo–Schumacher–Westmoreland information bound. Its content is that no measurement can extract more classical information about a quantum ensemble than the Holevo quantity, which is computed from the ensemble itself and involves no optimization over measurements.

### Proof through data processing

The standard proof has two steps, both of which are theorems about entropy under maps.

**Step 1: the measurement is a quantum channel.** A measurement with POVM $\{\tilde{E}_y\}$ followed by the recording of the outcome is a completely positive trace-preserving map carrying the quantum state to a classical state. In the Kraus language, choosing any square roots $\tilde{M}_y = \tilde{E}_y^{1/2}$ gives $\tilde{E}_y = \tilde{M}_y^\dagger\tilde{M}_y$ and

$$
\Phi(\tilde{\rho}) = \sum_y \mathrm{Tr}\bigl(\tilde{M}_y\tilde{\rho}\tilde{M}_y^\dagger\bigr)\,|y\rangle\langle y| ,
$$

a channel from $\mathbb{M}_+$ to the diagonal (commutative) subalgebra of the register, with Kraus rank at most the number of outcomes. The measured classical state is $\Phi(\bar{\tilde{\rho}})$.

**Step 2: the data-processing inequality.** For any channel $\Phi$ and any state $\rho_{XQ}$ with a classical register,

$$
I(X:Y) \;\leq\; I(X:Q),
$$

the **data-processing inequality** for the quantum mutual information: processing the quantum system cannot increase the information it shares with the register. Applying it to the state of the previous section and using $I(X:Q)=\chi$ gives the bound.

Both steps are standard. The first is the Stinespring form of a measurement, developed in this subcategory in the article on quantum channels; the second is a theorem about the relative entropy, whose standard form is that $S(\Phi(\rho)\|\Phi(\sigma))\leq S(\rho\|\sigma)$ for a trace-preserving completely positive map, together with the identity $I(X:Q) = S(\rho_{XQ}\|\rho_X\otimes\rho_Q)$. The biquaternion transcription changes the vocabulary — states and effects are elements of $\mathbb{M}_+$, the channel is a completely positive map on $\mathbb{B}\cong M_2(\mathbb{C})$ — but not the content.

### The biquaternion reading of the bound

Collecting the ingredients, the Holevo bound in the framework says:

- the **ensemble** is a convex decomposition of the average state in $\mathbb{M}_+$;
- the **Holevo quantity** is the concave functional $\chi = S(\bar{\tilde{\rho}}) - \sum_x p_x S(\tilde{\rho}_x)$ on that decomposition, which for pure-state ensembles is the norm-form function $H(N(\bar{\tilde{\rho}}))$;
- the **measurement** is a channel from $\mathbb{M}_+$ onto a commutative subalgebra generated by idempotents;
- the **bound** is the monotonicity of the quantum mutual information under that channel.

In this reading the Holevo quantity measures how much of the average state's mixedness is *classical* — attributable to the ensemble weights rather than to the individual states. If the ensemble states are pure, all of the average state's entropy is classical and $\chi = S(\bar{\tilde{\rho}})$; if the states are themselves mixed, part of the average entropy is quantum, and that part is unavailable to any measurement.

## Worked Examples

### Orthogonal pure states: saturation

Let the ensemble be two orthogonal pure states with equal weights,

$$
p_0 = p_1 = \tfrac12, \qquad
\tilde{\rho}_0 = \tilde{P}_+(\hat{e}_3), \qquad \tilde{\rho}_1 = \tilde{P}_-(\hat{e}_3) .
$$

The average state is $\bar{\tilde{\rho}} = \tfrac12 e_0$, with Bloch vector $\bar{\mathbf{r}} = 0$ and norm form $\tfrac14 e_0$, so

$$
\chi = S(\tfrac12 e_0) = \log 2 .
$$

The projective measurement in the basis $\{\tilde{P}_\pm(\hat{e}_3)\}$ gives $p(y|x) = \delta_{xy}$, a noiseless channel, so $I(X:Y) = \log 2 = H(X)$. The bound is saturated: $I_{\mathrm{acc}} = \chi = \log2$. This is the maximal value for a qubit, and it is attained exactly when the ensemble is an orthogonal decomposition with weights equal to the probabilities of a projective measurement.

### Two non-orthogonal pure states

Let the ensemble be two pure states with equal weights and overlap

$$
c = \bigl|\langle \psi_0|\psi_1\rangle\bigr| \in [0,1] .
$$

The average state has Bloch vector of length $c$, so its norm form is $\tfrac14(1-c^2)e_0$ and

$$
\chi = S(\bar{\tilde{\rho}}) = h\!\left(\frac{1+c}{2}\right).
$$

The accessible information of this ensemble is known: for two pure states with equal priors the optimal measurement is the square-root measurement, which here coincides in value with the Helstrom minimum-error measurement, and it gives

$$
I_{\mathrm{acc}} = \log 2 - h\!\left(\frac{1-\sqrt{1-c^2}}{2}\right) .
$$

The bound is not saturated for $0<c<1$. The following values were obtained by explicit computation of the two expressions; they use the natural logarithm, so the ceiling is $\log 2 = 0.693147$.

| $c$ | $\chi = h\!\left(\frac{1+c}{2}\right)$ | $I_{\mathrm{acc}} = \log2 - h\!\left(\frac{1-\sqrt{1-c^2}}{2}\right)$ |
|---|---|---|
| $0.0$ | $0.693147$ | $0.693147$ |
| $0.3$ | $0.647447$ | $0.583538$ |
| $0.6$ | $0.500402$ | $0.368064$ |
| $0.9$ | $0.198515$ | $0.098263$ |

The gap is the price of non-orthogonality: as the two states become more alike, both the ceiling and the accessible information fall, and the fraction of the ceiling actually accessible shrinks. At $c=0$ the bound is met; as $c\to1$ both quantities vanish and the ensemble carries no information.

### A mixed-state ensemble

For an ensemble of mixed states the Holevo quantity is strictly less than the entropy of the average state, because the individual entropies are subtracted. Take two states with Bloch vectors of length $r$ along opposite directions, equally weighted:

$$
\tilde{\rho}_\pm = \tfrac12\bigl(e_0 \pm i\,r\,\hat{e}_3\bigr), \qquad p_\pm = \tfrac12 .
$$

The average is $\tfrac12 e_0$, so $S(\bar{\tilde{\rho}}) = \log2$, while each state has entropy $h\!\left(\tfrac{1+r}{2}\right)$. Hence

$$
\chi = \log 2 - h\!\left(\frac{1+r}{2}\right),
$$

which is smaller than $\log2$ for $r<1$, rises to the saturated value $\log2$ at $r=1$, where the members are pure and orthogonal, and vanishes at $r=0$, where both members are maximally mixed and the ensemble carries no information about the index at all. This shows the two contributions to $\chi$ explicitly: the norm form of the average state supplies the first term, and the norm forms of the members supply the subtracted second term.

## What Is Algebraic and What Is Standard

**Algebraic, or made precise here.**

- The ensemble and the measurement are both families of positive elements of $\mathbb{M}_+$, paired by the trace formula; the outcome probabilities are the Born rule.
- The average state is an element of $\mathbb{M}_+$, and for a qubit its entropy is a function of its norm form, so the Holevo quantity of a pure-state ensemble is a norm-form function.
- The Holevo quantity is the quantum mutual information of the classical-quantum state, $I(X:Q)=\chi$; the measurement is a channel onto a commutative subalgebra, and the bound is data processing.
- The maximal Holevo quantity of a qubit is $\log2$, attained by an orthogonal pure-state ensemble of maximal entropy average.

**Standard, and imported.**

- The Holevo bound itself, and its proof through the data-processing inequality, are standard quantum information theory (Holevo 1973; Schumacher–Westmoreland). The biquaternion form transcribes the bound; it does not re-derive it from the algebra.
- The accessible information of two pure states, and the optimality of the square-root measurement for that ensemble, are standard results.
- The Shannon entropy of the classical distributions is classical information theory.
- Nothing here depends on the interpretive hypothesis that $\mathbb{M}_+$ is a physical sector; the transcription is exact for the operator algebra of a qubit.

## Open Questions

**1. A norm-form inequality.** The Holevo quantity of a pure-state ensemble is $H(N(\bar{\tilde{\rho}}))$, and the bound is $I_{\mathrm{acc}}\leq H(N(\bar{\tilde{\rho}}))$. Is there a direct algebraic proof of the bound for a qubit that uses only the norm form and the trace pairing, without passing through the general data-processing inequality?

**2. Many-qubit ensembles.** For $n$ qubits the average state lives in $\mathbb{M}_+^{\otimes n}$ and its entropy is no longer a function of a single norm form. What replaces the norm-form reading of $\chi$, and is there a tensor-product norm form that controls it?

**3. The role of entanglement.** The Holevo bound applies to an ensemble of *separable* states with no shared entanglement. With a shared entangled resource the accessible information can exceed the bound — this is the content of superdense coding — and the framework's algebraic account of that resource is a separate question.

**4. Continuity and the infinite ensemble.** The bounds and the saturation arguments assume a finite ensemble. The extension to continuous ensembles, and the algebraic meaning of the measure on $\mathbb{M}_+$, is open.

**5. Empirical content.** The Holevo form in the framework is the standard bound transcribed; it predicts nothing new.

## Summary

An ensemble in the informational sector is a family of states $\{p_x,\tilde{\rho}_x\}$ in $\mathbb{M}_+$ with an average state $\bar{\tilde{\rho}} = \sum_x p_x\tilde{\rho}_x$. A measurement is a POVM $\{\tilde{E}_y\}$ of effects summing to $e_0$, and the outcome probabilities are the trace pairing $p(y|x) = \mathrm{Tr}(\tilde{\rho}_x\tilde{E}_y)$. The accessible information is the maximum classical mutual information $I(X:Y)$ over measurements, and the Holevo quantity is

$$
\chi(\mathcal{E}) = S(\bar{\tilde{\rho}}) - \sum_x p_x S(\tilde{\rho}_x),
$$

non-negative by concavity, equal to the quantum mutual information $I(X:Q)$ of the classical-quantum state, and equal for a pure-state ensemble to the entropy of the average state, which for a qubit is the norm-form function $H(N(\bar{\tilde{\rho}}))$. The **Holevo bound** is

$$
I_{\mathrm{acc}}(\mathcal{E}) \;\leq\; \chi(\mathcal{E}) \;\leq\; \log 2 ,
$$

its proof being the data-processing inequality applied to the measurement channel. The bound is saturated by an orthogonal pure-state ensemble, where $\chi = I_{\mathrm{acc}} = \log2$; for two non-orthogonal pure states with overlap $c$ it is not saturated, with $\chi = h\!\left(\tfrac{1+c}{2}\right)$ and $I_{\mathrm{acc}} = \log2 - h\!\left(\tfrac{1-\sqrt{1-c^2}}{2}\right)$. The framework locates the ensemble, the measurement, and the bound in the algebra of $\mathbb{M}_+$; the numerical content is the standard quantum information theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{M}_+$ | Hermitian subspace (states and effects) |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion units, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary |
| $\tilde{\rho}_x = \tfrac12(e_0 + i\mathbf{r}_x)$ | Ensemble state |
| $\bar{\tilde{\rho}} = \sum_x p_x\tilde{\rho}_x$ | Average state |
| $\tilde{E}_y \geq 0$, $\sum_y\tilde{E}_y = e_0$ | POVM (effects) |
| $p(y|x) = \mathrm{Tr}(\tilde{\rho}_x\tilde{E}_y) = 2\,\mathrm{Sc}(\tilde{\rho}_x\tilde{E}_y)$ | Outcome probability (Born rule) |
| $I_{\mathrm{acc}} = \max_{\{\tilde{E}_y\}} I(X:Y)$ | Accessible information |
| $\chi = S(\bar{\tilde{\rho}}) - \sum_x p_x S(\tilde{\rho}_x)$ | Holevo quantity |
| $S(\tilde{\rho}) = h\!\left(\tfrac{1+|\mathbf{r}|}{2}\right)$ | Von Neumann entropy of a qubit state |
| $N(\bar{\tilde{\rho}}) = \tfrac14(1-|\bar{\mathbf{r}}|^2)e_0$ | Norm form of the average state |
| $\chi = H(N(\bar{\tilde{\rho}}))$ (pure ensemble) | Holevo quantity as a norm-form function |
| $\rho_{XQ} = \sum_x p_x|x\rangle\langle x|\otimes\tilde{\rho}_x$ | Classical-quantum state, $I(X:Q)=\chi$ |
| $I(X:Y)\leq\chi\leq\log2$ | Holevo bound and qubit ceiling |
| $c = |\langle\psi_0|\psi_1\rangle|$ | Overlap of two pure states |

## Further Reading

- A. S. Holevo, "Bounds for the quantity of information transmitted by a quantum communication channel," *Problemy Peredachi Informatsii* **9** (1973) 3–11, for the original Holevo bound.
- B. Schumacher and M. D. Westmoreland, "Sending classical information via noisy quantum channels," *Physical Review A* **56** (1997) 131–138, for the accessible-information form of the bound and its operational meaning.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the Holevo bound, its proof via the data-processing inequality, and the classical-quantum state construction.
- M. Ohya and D. Petz, *Quantum Entropy and Its Use* (Springer, 1993), for the monotonicity of relative entropy and the data-processing inequality.
- C. A. Fuchs, "Distinguishability and accessible information in quantum theory," Ph.D. thesis, University of New Mexico (1996), for the accessible information of two pure states and the role of the square-root measurement.
- A. Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), for POVMs and the operational meaning of the outcome probabilities.
- T. M. Cover and J. A. Thomas, *Elements of Information Theory* (Wiley, 2006), for the classical mutual information and the Shannon entropy.
- The companion articles of this series: *Quantum Mechanics in Biquaternionic Form*, *The Born Rule as a Trace Formula — Derivation and Comparison*, *The Bloch Ball as the Trace-One Slice of the Future Light Cone*, *Quantum Channels and the Reversible/Irreversible Dichotomy*, and *Entangled Subsystems in the Biquaternion Framework*.
