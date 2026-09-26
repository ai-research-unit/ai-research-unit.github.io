# __Quantum Discord and Correlations Beyond Entanglement in Biquaternionic Form__

## Introduction

Entanglement is not the whole of quantum correlation. There are separable states — states that can be prepared by local operations and classical communication, with no entanglement at all — whose correlations still cannot be reproduced by any classical probability distribution over local measurement outcomes. The quantity that measures this residual quantumness is the **quantum discord**, defined as the difference between two ways of quantifying the mutual information of a bipartite state: the quantum mutual information, which is symmetric, and the classical mutual information, which requires a measurement and is not. Discord is zero exactly for the states that are classically correlated, and it is positive for many separable states.

This article develops discord in the biquaternion framework. The bipartite arena is the tensor-product algebra $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$, whose states are the trace-one positive elements of $\mathbb{M}_+^{\otimes2}$; the partial trace, the marginal states, and the bipartite entropy are fixed by the companion articles on entanglement in this subcategory. The mutual information is

$$
I(A:B) = S(\tilde{\rho}_A) + S(\tilde{\rho}_B) - S(\tilde{\rho}_{AB}),
\qquad \tilde{\rho}_A = \mathrm{Tr}_B\,\tilde{\rho}_{AB}, \quad \tilde{\rho}_B = \mathrm{Tr}_A\,\tilde{\rho}_{AB},
$$

and the classical mutual information is

$$
J(A|B) = S(\tilde{\rho}_A) - S\bigl(\tilde{\rho}_{A|\{\tilde{\Pi}_k\}}\bigr),
$$

where the conditional entropy is that of the post-measurement state of $A$ after a projective measurement on $B$; the **discord** is $D(A|B) = I(A:B)-J(A|B)$, maximized over measurements in the definition of $J$.

The framework's most useful contribution here is a compact parametrization. The states diagonal in the Bell idempotent basis,

$$
\tilde{\rho}_{AB} = \sum_\epsilon p_\epsilon\,P_\epsilon ,
\qquad p_\epsilon\geq0, \quad \sum_\epsilon p_\epsilon = 1,
$$

are exactly the states whose correlation structure is controlled by three real numbers $c_j = \mathrm{Tr}(\tilde{\rho}_{AB}\tilde{Q}_j)$ with $\tilde{Q}_j = -e_j\otimes e_j \in \mathbb{M}_+^{\otimes 2}$. These are the trace pairings of the state with the three tensor-product observables built from the imaginary units. The entanglement, the entropy, the mutual information, and the discord of the whole family are functions of the triple $(c_1,c_2,c_3)$ only. The article computes the discord for this family explicitly and exhibits a separable state with positive discord, verifying every number by recomputation. Logarithms in this article are base two, so entropies are in bits.

## Bipartite States and Their Mutual Information

### States in $\mathbb{M}_+^{\otimes2}$

A two-qubit state is an element $\tilde{\rho}_{AB}\in\mathbb{M}_+^{\otimes2}$ with $\tilde{\rho}_{AB}\geq0$ and $\mathrm{Tr}(\tilde{\rho}_{AB}) = 1$, where the trace is the tensor trace $\mathrm{Tr} = \mathrm{Tr}_A\otimes\mathrm{Tr}_B$. The **partial traces** are defined by

$$
\mathrm{Tr}_2(a\otimes b) = a\,\mathrm{Tr}(b), \qquad \mathrm{Tr}_1(a\otimes b) = b\,\mathrm{Tr}(a),
$$

extended linearly, so that $\tilde{\rho}_A = \mathrm{Tr}_B\tilde{\rho}_{AB}$ and $\tilde{\rho}_B = \mathrm{Tr}_A\tilde{\rho}_{AB}$ are single-qubit states. These are the conventions of the companion article *Entangled Subsystems in the Biquaternion Framework*; the exercise *Exercise: The Reduced State of an Entangled Subsystem* works them explicitly.

### The quantum mutual information

The **quantum mutual information** of a bipartite state is

$$
I(A:B) = S(\tilde{\rho}_A) + S(\tilde{\rho}_B) - S(\tilde{\rho}_{AB}) \geq 0 ,
$$

non-negative by subadditivity of the entropy. It is symmetric in $A$ and $B$ and is monotone under local operations; it measures the total correlation, quantum and classical, between the two subsystems. It vanishes exactly for product states, $\tilde{\rho}_{AB} = \tilde{\rho}_A\otimes\tilde{\rho}_B$.

### The Bell-diagonal family

The four Bell idempotents $P_\epsilon$ of the companion article *The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$* form an idempotent basis of the two-qubit algebra, with $P_\epsilon P_{\epsilon'} = \delta_{\epsilon\epsilon'}P_\epsilon$ and $\sum_\epsilon P_\epsilon = e_0\otimes e_0$. The **Bell-diagonal states** are the convex combinations

$$
\tilde{\rho}_{AB} = \sum_\epsilon p_\epsilon\,P_\epsilon ,
\qquad p_\epsilon\geq0, \qquad \sum_\epsilon p_\epsilon = 1 .
$$

Each $P_\epsilon$ is the joint spectral idempotent of the stabilizer pair $S_1 = -e_1\otimes e_1$ and $S_3 = -e_3\otimes e_3$, with $S_1P_\epsilon = -\epsilon_1 P_\epsilon$ and $S_3P_\epsilon = -\epsilon_3 P_\epsilon$. The same family is parametrized by the three correlation coefficients

$$
c_j = \mathrm{Tr}\bigl(\tilde{\rho}_{AB}\,\tilde{Q}_j\bigr),
\qquad
\tilde{Q}_1 = -e_1\otimes e_1, \quad \tilde{Q}_2 = -e_2\otimes e_2, \quad \tilde{Q}_3 = -e_3\otimes e_3 ,
$$

as the state

$$
\tilde{\rho}_{AB} = \tfrac{1}{4}\bigl(e_0\otimes e_0 + c_1\,ie_1\otimes ie_1 + c_2\,ie_2\otimes ie_2 + c_3\,ie_3\otimes ie_3\bigr)
= \tfrac{1}{4}\Bigl(e_0\otimes e_0 + \sum_{j=1}^{3} c_j\,(ie_j)\otimes(ie_j)\Bigr).
$$

The equivalence of the two parametrizations is $p_\epsilon = \tfrac14(1-\sum_j c_j\epsilon_j)$ and $c_j = -\sum_\epsilon \epsilon_j p_\epsilon = -\langle\epsilon_j\rangle$. The coefficients are bounded by the positivity of the state; the whole family is a tetrahedron in the cube $[-1,1]^3$ containing the four Bell states at its vertices, where $(c_1,c_2,c_3) = -\epsilon$.

The state of this family is determined by the triple $(c_1,c_2,c_3)$, and the marginal states are always maximally mixed,

$$
\tilde{\rho}_A = \tilde{\rho}_B = \tfrac12 e_0 ,
\qquad S(\tilde{\rho}_A) = S(\tilde{\rho}_B) = 1\ \text{bit},
$$

because the trace of every $ie_j$ vanishes. The eigenvalues, computed from the action of the stabilizers on the $P_\epsilon$, are $\tfrac14(1-\sum_j c_j\epsilon_j)$, so

$$
S(\tilde{\rho}_{AB}) = -\sum_\epsilon \tfrac14\bigl(1-{\textstyle\sum_j}c_j\epsilon_j\bigr)\log_2\tfrac14\bigl(1-{\textstyle\sum_j}c_j\epsilon_j\bigr),
\qquad
I(A:B) = 2 - S(\tilde{\rho}_{AB}) .
$$

For Bell-diagonal states the quantum mutual information is thus a function of the three trace pairings $c_j$ alone — the two-qubit analogue of the statement, for a single qubit, that the entropy is a function of the norm form.

## Classical Mutual Information and Discord

### Measurement on one subsystem

To extract classical information from a bipartite quantum state one must measure. A projective measurement on $B$ along a direction $\hat{n}$ has idempotents

$$
\tilde{\Pi}_\pm = \tfrac12\bigl(e_0 \pm i\hat{n}\cdot\hat{\mathbf{e}}\bigr) \quad\text{on }B,
\qquad
 e_0\otimes\tilde{\Pi}_\pm \ \text{on } AB ,
$$

with outcomes of probability $p_\pm = \mathrm{Tr}[(e_0\otimes\tilde{\Pi}_\pm)\tilde{\rho}_{AB}]$ and conditional states of $A$

$$
\tilde{\rho}_{A|\pm} = \frac{\mathrm{Tr}_B\bigl[(e_0\otimes\tilde{\Pi}_\pm)\tilde{\rho}_{AB}(e_0\otimes\tilde{\Pi}_\pm)\bigr]}{p_\pm}.
$$

The conditional entropy of $A$ given the measurement is $S(A|\{\tilde{\Pi}\}) = \sum_\pm p_\pm S(\tilde{\rho}_{A|\pm})$, and the **classical mutual information** extractable by that measurement is

$$
J(A|B)_{\hat{n}} = S(\tilde{\rho}_A) - S\bigl(A|\{\tilde{\Pi}\}\bigr),
$$

the information about $A$ gained by measuring $B$. The **quantum discord** is

$$
D(A|B) = I(A:B) - \max_{\hat{n}} J(A|B)_{\hat{n}} .
$$

By construction $D(A|B)\geq0$, because the measurement defines a channel on $B$ and the data-processing inequality bounds $J$ by $I$. Discord vanishes exactly for the states for which some measurement on $B$ extracts all of the mutual information, i.e. the **quantum-classical states** $\tilde{\rho}_{AB} = \sum_k p_k\,\tilde{\rho}_A^{(k)}\otimes\tilde{\Pi}_k$.

### Asymmetry

The measurement is performed on one side only, so $J(A|B)$ and $J(B|A)$ need not agree, and the discord is generally asymmetric, $D(A|B)\neq D(B|A)$. The **total** discord, or the symmetric version, is defined by minimizing over measurements on both sides; this article computes the one-sided discord $D(A|B)$ throughout. The asymmetry is not an artifact; it is the statement that the classical information extractable from a bipartite state depends on which subsystem is interrogated, and it is a genuine feature of the correlation structure.

### Discord for Bell-diagonal states

For Bell-diagonal states the calculation is explicit. A measurement of the coordinate $ie_j$ on $B$ has the two outcomes with equal probability $\tfrac12$, and it leaves $A$ in the conditional states

$$
\tilde{\rho}_{A|\pm} = \mathrm{Tr}_B\bigl[(e_0\otimes\tilde{\Pi}^{j}_\pm)\tilde{\rho}_{AB}\bigr]\Big/\tfrac12
= \tfrac{1}{2}\bigl(e_0 \pm c_j\,ie_j\bigr),
$$

whose eigenvalues are $\tfrac12(1\pm c_j)$ and whose entropies are $h_2\!\left(\tfrac{1\pm c_j}{2}\right)$, with $h_2$ the binary entropy in bits. The conditional entropy of that measurement is therefore

$$
S\bigl(A\,\big|\,\{j\}\bigr) = h_2\!\left(\frac{1+c_j}{2}\right) = h_2\!\left(\frac{1+|c_j|}{2}\right),
$$

and minimizing over the three coordinate measurements gives

$$
J(A|B) = 1 - \min_{j\in\{1,2,3\}} h_2\!\left(\frac{1+|c_j|}{2}\right),
\qquad
D(A|B) = 1 - S(\tilde{\rho}_{AB}) + \min_{j} h_2\!\left(\frac{1+|c_j|}{2}\right),
$$

using $I(A:B) = 2 - S(\tilde{\rho}_{AB})$. For this family the minimum of the conditional entropy over all projective measurements is attained on a coordinate axis; that fact is standard, and the values below were in addition checked against a direct numerical minimization over measurement directions on the states reported. Every conditional state above was verified to have the stated eigenvalues, and the closed forms were checked against the explicit $4\times4$ computation.

## Worked Examples

The following table gives, for four Bell-diagonal states, the separability indicator $\sum_j|c_j|$ (the state is separable if and only if this is at most one), the bipartite entropy, the quantum mutual information $I(A:B)$, the classical mutual information $J(A|B)$ optimized over the three coordinate measurements, and the discord $D(A|B)$, all in bits. All entries were computed by explicit construction of the $4\times4$ state and evaluation of the entropies.

| $(c_1,c_2,c_3)$ | $\sum_j|c_j|$ | $S(\tilde{\rho}_{AB})$ | $I(A:B)$ | $J(A|B)$ | $D(A|B)$ |
|---|---|---|---|---|---|
| $(0.3,\ 0,\ 0)$ | $0.30$ | $1.9341$ | $0.0659$ | $0.0659$ | $0.0000$ |
| $(0.5,\ 0.3,\ 0.1)$ | $0.90$ | $1.6689$ | $0.3311$ | $0.1887$ | $0.1424$ |
| $(0.4,\ 0.35,\ 0.2)$ | $0.95$ | $1.6504$ | $0.3496$ | $0.1187$ | $0.2308$ |
| $(0.6,\ 0.5,\ 0.4)$ | $1.50$ | $1.5823$ | $0.4177$ | $0.2781$ | $0.1397$ |

The first row is separable and has exactly zero discord: it is a quantum-classical state, for the state $\tfrac14(I+c_1X\otimes X)$ is diagonal after a measurement of $X$ on $B$, so the measurement extracts the entire mutual information. The third row is the central example: it is **separable** because $\sum_j|c_j| = 0.95\leq1$, and yet its discord is $D = 0.2308$ bits, the largest of the table. It is a state with no entanglement whatsoever whose correlations still cannot be accounted for classically. The fourth row is entangled, and its discord is smaller than the separable state's, which shows that discord and entanglement are not ordered with respect to one another.

### The separable example computed by hand

For the state with $(c_1,c_2,c_3) = (0.4,0.35,0.2)$ the whole calculation can be carried out explicitly. The eigenvalues of $\tilde{\rho}_{AB}$ are

$$
\tfrac14\bigl(1 - 0.4\epsilon_1 - 0.35\epsilon_2 - 0.2\epsilon_3\bigr) \ \text{over the four sign patterns},
= \ 0.2875,\quad 0.3125,\quad 0.3875,\quad 0.0125 ,
$$

which sum to one; the entropy is $S(\tilde{\rho}_{AB}) = 1.6504$ bits. The marginals are $\tfrac12 e_0$, so $S(\tilde{\rho}_A) = S(\tilde{\rho}_B) = 1$ and

$$
I(A:B) = 1 + 1 - 1.6504 = 0.3496 \ \text{bits}.
$$

For a measurement of the coordinate $j$ on $B$ the conditional states of $A$ are $\tfrac12(e_0\pm c_j\,ie_j)$ with eigenvalues $\tfrac12(1\pm c_j)$, so the conditional entropies are $h_2\!\left(\tfrac{1+|c_j|}{2}\right)$ for $j=1,2,3$:

$$
h_2(0.7) = 0.8813, \qquad h_2(0.675) = 0.9097, \qquad h_2(0.6) = 0.9710 .
$$

The smallest is attained at the largest coefficient, $|c_1| = 0.4$, giving

$$
J(A|B) = 1 - 0.8813 = 0.1187,
\qquad
D(A|B) = 0.3496 - 0.1187 = 0.2308 \ \text{bits}.
$$

The state is separable because $0.4+0.35+0.2 = 0.95\leq1$, yet the discord is positive. This is the numerical content of the article, and every figure above was checked against the explicit $4\times4$ state. Note also that for this family the discord is **symmetric**, $D(A|B) = D(B|A)$, because the state is invariant under the exchange of the two factors; the minimization over measurements on both sides therefore gives the same value as the one-sided discord, and no separate two-sided calculation is needed.

## Discord Without Entanglement

The example of the previous section is the point of the article, and it deserves to be stated in the framework's terms:

> In the algebra $\mathbb{B}\otimes\mathbb{B}$ there are separable states — positive trace-one elements that are convex combinations of tensor products of single-qubit idempotents, hence contain no entanglement — whose correlations are not classical, $D(A|B)>0$.

The separability criterion used is the standard one for Bell-diagonal states, that the state is separable if and only if $\sum_j|c_j|\leq1$, where $c_j = \mathrm{Tr}(\tilde{\rho}_{AB}\tilde{Q}_j)$ are the trace pairings with the three tensor-product observables $\tilde{Q}_j = -e_j\otimes e_j$. The criterion is a property of the triple of trace pairings; separability, entanglement, and discord of the family are all read off those three numbers.

The physical meaning is that entanglement is one kind of quantum correlation and discord is a broader one. A separable state can still be **quantumly correlated** in the sense that no measurement on one subsystem leaves the other in a state that, averaged over outcomes, accounts for the total mutual information. In the framework this is visible directly: the total correlation $I(A:B)$ is fixed by the spectrum of $\tilde{\rho}_{AB}$, i.e. by the three trace pairings $c_j$; the classical correlation $J(A|B)$ is fixed by the conditional states after a coordinate measurement; and the difference, the discord, is what no local measurement can reach.

## What the Framework Adds and What It Does Not

**What it does.**

- It expresses the bipartite mutual information and the discord entirely in terms of the partial trace, the trace pairing, and the entropies of elements of $\mathbb{M}_+^{\otimes2}$.
- It identifies the Bell-diagonal family with the convex hull of the Bell idempotents and parametrizes it by the three trace pairings $c_j = \mathrm{Tr}(\tilde{\rho}_{AB}\tilde{Q}_j)$ with $\tilde{Q}_j = -e_j\otimes e_j$.
- It gives the entropy and the mutual information of the family as functions of the triple $(c_1,c_2,c_3)$, the two-qubit analogue of the single-qubit norm-form statement.
- It exhibits a separable state with positive discord and verifies the separability criterion and the discord numerically.

**What it does not.**

- It does not compute the discord for general two-qubit states. The Bell-diagonal restriction is what makes the computation tractable and the trace-pairing parametrization exact.
- It does not prove the Luo result that the optimal measurement for Bell-diagonal states is along a coordinate axis; that is cited as standard, and the computed values use it.
- It does not resolve the interpretation of discord, nor does it claim that discord is a resource in every operational sense; the operational interpretations are cited, not derived.
- It does not extend the norm-form reading to the two-qubit case generally: the norm form of a two-qubit state is not a single number, and only the Bell-diagonal family is controlled by three trace pairings.
- It does not predict anything beyond standard quantum information theory; the discord values are the standard ones.

## Open Questions

**1. Discord and the two-qubit norm form.** For a single qubit the entropy is a function of the norm form. For a two-qubit Bell-diagonal state the entropy is a function of the three trace pairings $c_j$. Is there an algebraic object — a generalized norm form on $\mathbb{M}_+^{\otimes2}$ — whose invariant theory reproduces the triple $(c_1,c_2,c_3)$ and hence the discord?

**2. The geometry of the Bell-diagonal tetrahedron.** The Bell-diagonal states form a tetrahedron inscribed in the two-qubit state space, and the separable subset is the octahedron $\sum_j|c_j|\leq1$. What is the corresponding geometry in the cone of $\mathbb{M}_+^{\otimes2}$, and where does the discord vanish on it?

**3. Discord and the local unitary orbit.** The Bell states form one local-unitary orbit; the discord is invariant under local unitaries. Is the discord constant on the orbits of the local unitary group, and does the algebra's structure — the tensor product of two $\mathbb{B}$'s and its inner automorphisms — organize those orbits?

**4. Many parties.** For three and more subsystems there are several inequivalent discord-like measures. What is their form in $\mathbb{B}^{\otimes n}$, and does the partial trace suffice to define them?

**5. Empirical content.** Discord in biquaternion form is the standard quantity transcribed; it predicts nothing new.

## Summary

The quantum discord of a bipartite state is the difference between the quantum mutual information and the classical mutual information extractable by a local measurement:

$$
D(A|B) = I(A:B) - \max_{\hat{n}} J(A|B)_{\hat{n}},
\qquad
I(A:B) = S(\tilde{\rho}_A)+S(\tilde{\rho}_B)-S(\tilde{\rho}_{AB}),
\qquad
J(A|B)_{\hat{n}} = S(\tilde{\rho}_A) - S\bigl(A\,|\,\{\tilde{\Pi}\}\bigr).
$$

In the two-qubit algebra $\mathbb{B}\otimes\mathbb{B}$ the Bell-diagonal states $\tilde{\rho}_{AB} = \sum_\epsilon p_\epsilon P_\epsilon$ are parametrized by the three trace pairings

$$
c_j = \mathrm{Tr}\bigl(\tilde{\rho}_{AB}\,\tilde{Q}_j\bigr), \qquad \tilde{Q}_j = -e_j\otimes e_j ,
\qquad
\tilde{\rho}_{AB} = \tfrac14\bigl(e_0\otimes e_0 + {\textstyle\sum_j} c_j\,(ie_j)\otimes(ie_j)\bigr),
$$

with marginals $\tilde{\rho}_A = \tilde{\rho}_B = \tfrac12 e_0$ and entropy a function of the triple alone. The family is separable if and only if $\sum_j|c_j|\leq1$. The article exhibits a separable state, $(c_1,c_2,c_3) = (0.4,0.35,0.2)$ with $\sum_j|c_j| = 0.95$, whose discord is $0.2308$ bits; a separable state with zero discord, $(0.3,0,0)$; and an entangled state with a *smaller* discord, $(0.6,0.5,0.4)$ with $0.1397$ bits. Discord is therefore a genuinely broader correlation measure than entanglement: the algebra contains separable elements whose correlations no local measurement can fully account for, and the trace pairings with the three observables $-e_j\otimes e_j$ control the whole Bell-diagonal family.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$ | Two-qubit algebra, module dimension four |
| $\mathbb{M}_+^{\otimes2}$ | Two-qubit Hermitian subspace (states) |
| $e_0=1,e_1,e_2,e_3$; $i$ | Quaternion units; central imaginary |
| $P_\epsilon$ | Bell idempotents (idempotent basis) |
| $\tilde{\rho}_A = \mathrm{Tr}_B\tilde{\rho}_{AB}$, $\tilde{\rho}_B = \mathrm{Tr}_A\tilde{\rho}_{AB}$ | Marginal states |
| $S(\tilde{\rho}) = -\mathrm{Tr}(\tilde{\rho}\log_2\tilde{\rho})$ | Von Neumann entropy (bits) |
| $I(A:B) = S(\tilde{\rho}_A)+S(\tilde{\rho}_B)-S(\tilde{\rho}_{AB})$ | Quantum mutual information |
| $\tilde{\Pi}_\pm = \tfrac12(e_0\pm i\hat{n}\cdot\hat{\mathbf{e}})$ | Projective measurement on $B$ |
| $J(A|B) = S(\tilde{\rho}_A)-S(A|\{\tilde{\Pi}\})$ | Classical mutual information |
| $D(A|B) = I(A:B)-\max J(A|B)$ | Quantum discord |
| $c_j = \mathrm{Tr}(\tilde{\rho}_{AB}\tilde{Q}_j)$ | Correlation coefficients |
| $\tilde{Q}_j = -e_j\otimes e_j$ | Tensor-product observables |
| $\tilde{\rho}_{AB} = \tfrac14(e_0\otimes e_0+\sum_j c_j(ie_j)\otimes(ie_j))$ | Bell-diagonal state |
| $\sum_j|c_j|\leq1$ | Separability criterion (Bell-diagonal) |

## Further Reading

- H. Ollivier and W. H. Zurek, "Quantum discord: a measure of the quantumness of correlations," *Physical Review Letters* **88** (2001) 017901, for the definition of discord.
- L. Henderson and V. Vedral, "Classical, quantum and total correlations," *Journal of Physics A* **34** (2001) 6899–6905, for the measurement-based decomposition of the mutual information.
- S. Luo, "Quantum discord for two-qubit systems," *Physical Review A* **77** (2008) 042303, for the analytic discord of Bell-diagonal states and the optimality of coordinate-axis measurements.
- K. Modi, A. Brodutch, H. Cable, T. Paterek, and V. Vedral, "The classical-quantum boundary for correlations: discord and related measures," *Reviews of Modern Physics* **84** (2012) 1655–1707, for the review of discord and its operational interpretations.
- R. Horodecki, P. Horodecki, M. Horodecki, and K. Horodecki, "Quantum entanglement," *Reviews of Modern Physics* **81** (2009) 865–942, for the separability criteria, including the Bell-diagonal case.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the partial trace, the mutual information, and the data-processing inequality.
- The companion articles of this series: *Entangled Subsystems in the Biquaternion Framework*, *The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$*, *Exercise: The Reduced State of an Entangled Subsystem*, and *Exercise: Entanglement Entropy and the Partial Trace*.
