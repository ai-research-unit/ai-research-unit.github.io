
# __Complexified Spacetime with a Local Complex Structure__

## Core Proposal

The fundamental arena of physics is **not** the Minkowski space $\mathbb{R}^{3,1}$, but the **biquaternion algebra** $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$. A **point in the complexified spacetime** is an element of $\mathbb{B}$, written as a biquaternionic coordinate

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3,
$$

where $e_0 = 1$ and $e_1, e_2, e_3$ are the quaternion units. The four coefficients $Q_\mu$ are complex numbers, and they split naturally into two sectors, as described below. The complex structure — the identification of which direction is "real" and which is "imaginary" — is **local**, determined by the electromagnetic properties of the medium at each point. This is the central proposal of this article.

## Two Sectors: Material and Informational

The biquaternion algebra splits naturally into two complementary four-dimensional real subspaces, the fixed-point sets of the Hermitian and anti-Hermitian conjugations:

$$
\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+.
$$

These two subspaces have distinct physical roles:

- **$\mathbb{M}_-$ is the material sector.** Its coordinates are **$ict$** (an imaginary temporal coordinate, c being the speed of light) and **$x, y, z$** (three real spatial coordinates). This is the home of the four-vectors of relativistic physics. The imaginary time coordinate reflects a simple fact: time can be measured, but it cannot be touched, held, or moved through. The companion article *$\mathbb{M}_-$ as the Material Space* develops this sector.
- **$\mathbb{M}_+$ is the informational sector.** Its coordinates are **$ct'$** (a real temporal coordinate) and **$ix', iy', iz'$** (three imaginary spatial coordinates). This is the home of the Hermitian operators that act on the material sector — the boost biquaternions, the pure-state projectors, the observables. The imaginary spatial directions reflect a mirror fact: they are the directions of a space that is *organised* rather than *extended*. The companion article *$\mathbb{M}_+$ as the Informational Space* develops this sector.

The complex structure makes the two sectors complementary: the material sector has three real spatial directions and one imaginary temporal direction; the informational sector has three imaginary spatial directions and one real temporal direction.

## The Complex Coordinates

Writing the biquaternion coordinate in terms of its material and informational parts,

$$
\tilde{Q} = \underbrace{(ict)\,e_0 + (x\,e_1 + y\,e_2 + z\,e_3)}_{\in\,\mathbb{M}_-} \;+\; \underbrace{(ct')\,e_0 + (ix'\,e_1 + iy'\,e_2 + iz'\,e_3)}_{\in\,\mathbb{M}_+},
$$

the coefficients $Q_0, Q_1, Q_2, Q_3$ take the explicit form

$$
Q_0 = ct' + ict, \qquad Q_1 = x + i x', \qquad Q_2 = y + i y', \qquad Q_3 = z + i z'.
$$

The **real parameters** $(t, x, y, z)$ describe the material sector, and the **real parameters** $(t', x', y', z')$ describe the informational sector. Each sector is four-dimensional, and the full complexified spacetime is the direct sum of the two.

### The Vacuum Limit

In vacuum, $c = c_0$, and the material time coordinate becomes $ic_0 t$ — the familiar $ict$ form with the vacuum speed of light. The $ict$ convention is therefore the vacuum limit of the more general local structure. In a material medium, the complex structure uses $c$, the local speed of light, and varies from point to point. This makes the complex structure **local**, in the same spirit as the metric in general relativity.

## The Metric

The natural quadratic form on the biquaternion algebra is the complex bilinear form

$$
d\tilde{Q} \circ d\tilde{Q} = \sum_{\mu=0}^{3} (dQ_\mu)^2,
$$

where $\circ$ is the biquaternion product. Expanding in real and imaginary parts,

$$
(dQ_\mu)^2 = (dq_\mu)^2 - (dq'_\mu)^2 + 2i\,dq_\mu\,dq'_\mu.
$$

The **real part** of $d\tilde{Q} \circ d\tilde{Q}$ reproduces the Lorentzian interval on the material sector. The minus sign in the time–time component arises algebraically from $i^2 = -1$ in the imaginary time coordinate $ict$, not from an independently postulated metric signature. The **imaginary part** couples the material and informational sectors through cross terms, and is where the physical content of the hypothesis resides.

## The Informational Hypothesis

The informational sector is not merely a mathematical mirror of the material one. Its algebraic structure is **exactly** that of the operator algebra of a two-state quantum system — the spin-1/2 system. The idempotents of $\mathbb{M}_+$ are pure-state projectors; the Hermitian elements are observables; the unitary elements are reversible transformations; the trace formula gives the Born rule. This identification is not an analogy: it is the same mathematics, expressed in the biquaternion algebra, and it is developed in detail in the companion article *Spin-1/2 Quantum Mechanics in Biquaternionic Form*.

The hypothesis of this blog is that this structural identification reflects a **physical fact** about the world: that beyond the material sector of observable physics there is an informational sector, whose elements are the operators acting on the material sector, and whose structure is the quantum-informational structure we have just described.

The informational sector is conjectured to carry the following three properties:

1. **Organization rather than dispersion.** Where the imaginary time direction $ict$ is associated with entropy increase, the real time direction $ct'$ is associated with information organization — possibly a decrease in entropy, or an increase in structural complexity.

2. **Phase-like character.** The imaginary spatial directions $ix', iy', iz'$ are naturally phase-like, in the same sense that imaginary time in Wick-rotated quantum field theory is thermodynamic and statistical in character.

3. **Coupling to the material sector.** The cross terms $2i\,dq_\mu\,dq'_\mu$ in the metric encode the coupling between the material and informational sectors. This coupling is where the physical content of the hypothesis would reside.

## Status and Open Questions

This is a **frontier hypothesis**, not established physics. The key open questions are:

1. **Dimensionality.** Why are the imaginary spatial directions of $\mathbb{M}_+$ not observed? A compactification or hiding mechanism is required.

2. **Causality.** How does causal structure in the material sector interact with the informational character of $\mathbb{M}_+$?

3. **Coupling.** What is the precise dynamical coupling between the two sectors? The Lorentz coupling via the boost biquaternion is established, but a genuinely new coupling would be needed to give the informational sector physical content.

4. **Dynamics of the informational sector.** Does $\mathbb{M}_+$ have its own dynamics? The biquaternion operators $\tilde{\nabla}$, $\bar{\tilde{\nabla}}$, and $\Box$ are available, but it is not clear which (if any) governs $\mathbb{M}_+$-valued fields.

5. **Empirical contact.** What quantitative prediction distinguishes this framework from standard physics?

The hypothesis is offered as a structural intuition: that the two natural subspaces of the biquaternion algebra have distinct physical roles — one material, one informational — and that the informational subspace is the natural arena for the operator algebra of quantum mechanics. The local speed of light $c = 1/\sqrt{\epsilon\mu}$ plays the role of the local scale factor of the complex structure, making the $ict$ convention a vacuum approximation of a more general local structure, in the same way that special relativity is a local approximation of general relativity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | Biquaternionic coordinate |
| $\mathbb{M}_-$ | Material sector: coordinates $(ict, x, y, z)$ |
| $\mathbb{M}_+$ | Informational sector: coordinates $(ct', x', y', z')$ |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium (local) |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum (global constant) |
| $v$ | Particle or frame velocity |

## Further Reading

- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover).
- Roger Penrose, *The Road to Reality* (Knopf, 2004), for the complex structure of spacetime.
- Edward Witten, "Anti-de Sitter Space and Holography" (1998), for the geometric interpretation of information.
- Vladimir V. Kassandrov, "Relativistic Algebra of Space-Time and Algebrodynamics" (2006), for a biquaternionic approach to complexified geometry.

