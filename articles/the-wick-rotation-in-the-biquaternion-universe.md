
# The Wick Rotation in the Biquaternion Universe

## Introduction

The **Wick rotation** is a computational procedure used throughout quantum field theory, statistical mechanics, and condensed-matter physics. It consists of the analytic continuation $t \to -i\tau$ of the time coordinate to imaginary values, and it converts the oscillating phase of the Feynman path integral into a decaying exponential. The procedure is usually presented as a **trick**: it is justified by analytic continuation of the integrand in the complex time plane, it works for a large class of physically relevant problems, and it fails for others, without a general theorem that settles when it works and when it does not.

This article proposes a structural reading of the Wick rotation, in terms of the biquaternion algebra. The main observation is the following: the Wick rotation, in the $ict$ convention, sends the imaginary time coefficient $ict$ to the real value $c\tau$, while leaving the spatial coordinates $x, y, z$ unchanged. The result is a point of the **quaternion subspace** $\mathbb{H}_{\mathbb{B}}$, whose four coefficients are all real. So the Wick rotation is an **identification** of the material sector $\mathbb{M}_-$ with the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, obtained by relabeling the imaginary coefficient $ict$ as a real one.

This reading explains, in a single structural fact, why the trick is useful and why it sometimes fails. The subspace $\mathbb{H}_{\mathbb{B}}$ is better behaved than $\mathbb{M}_-$: it has a positive-definite quadratic form, no zero divisors, a division-algebra structure, an elliptic differential operator, and a compact symmetry group. When the physics of a problem depends on the Lorentzian structure of $\mathbb{M}_-$ — the light cone, the causal ordering, the phase — the transfer to $\mathbb{H}_{\mathbb{B}}$ destroys this structure, and the trick fails. When the physics is insensitive to the Lorentzian structure — equilibrium, correlation, statistical weight — the transfer is harmless and the resulting problem on $\mathbb{H}_{\mathbb{B}}$ is easier.

The article is organized as follows. First the three natural subspaces of $\mathbb{B}$ are recalled: the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the material sector $\mathbb{M}_-$, and the informational sector $\mathbb{M}_+$. Then the standard Wick rotation is recalled, and its action on the coordinates is written explicitly. Then the identification with $\mathbb{H}_{\mathbb{B}}$ is developed, with the properties of the two subspaces compared. Then the reading is applied to the standard applications of the Wick rotation, and a split is proposed between applications that transfer harmlessly and applications that resist. The article closes with the status of the reading.

Throughout, $c$ denotes the speed of light in the medium, and the biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$.

## The Three Subspaces of $\mathbb{B}$

The biquaternion algebra $\mathbb{B}$ contains three distinguished four-dimensional real subspaces: the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the material sector $\mathbb{M}_-$, and the informational sector $\mathbb{M}_+$. All three are real vector spaces of dimension 4, and all three are subspaces of the same algebra.

**The quaternion subspace $\mathbb{H}_{\mathbb{B}}$.** An element has the form

$$
\tilde{Q} = q_0\, e_0 + q_1\, e_1 + q_2\, e_2 + q_3\, e_3, \qquad q_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

All four coefficients are **real**. The quadratic form

$$
N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = q_0^2 + q_1^2 + q_2^2 + q_3^2
$$

has signature $(4, 0)$. The subspace is a subalgebra of $\mathbb{B}$ isomorphic to the quaternion algebra $\mathbb{H}$, and it is a division algebra: every nonzero element is invertible, and there are no zero divisors.

**The material sector $\mathbb{M}_-$.** An element has the form

$$
\tilde{Q} = i q'_0\, e_0 + q_1\, e_1 + q_2\, e_2 + q_3\, e_3, \qquad q'_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

The first coefficient is **imaginary**, the three remaining coefficients are **real**. The quadratic form

$$
N(\tilde{Q}) = -(q'_0)^2 + q_1^2 + q_2^2 + q_3^2
$$

has signature $(3, 1)$. The subspace is not a subalgebra, and it contains a three-dimensional cone of zero divisors.

**The informational sector $\mathbb{M}_+$.** An element has the form

$$
\tilde{Q} = q_0\, e_0 + i q'_1\, e_1 + i q'_2\, e_2 + i q'_3\, e_3, \qquad q_0, q'_1, q'_2, q'_3 \in \mathbb{R}.
$$

The first coefficient is **real**, the three remaining coefficients are **imaginary**. The quadratic form

$$
N(\tilde{Q}) = q_0^2 - (q'_1)^2 - (q'_2)^2 - (q'_3)^2
$$

has signature $(1, 3)$, the mirror image of the signature on $\mathbb{M}_-$.

The three subspaces are distinct, and each has its own algebraic and analytic character. The specific form of the differential operators on each subspace — the gradient, the d'Alembertian, and the square of the gradient — has been developed in the companion articles on the biquaternion analysis.

## The Standard Wick Rotation

In relativistic field theory, a point of the material sector is written

$$
\tilde{Q}_- = i c t\, e_0 + x\, e_1 + y\, e_2 + z\, e_3 \in \mathbb{M}_-,
$$

where $t$ is the time coordinate, $x, y, z$ are the spatial coordinates, and the four coefficients are $ict, x, y, z$ respectively.

The **standard Wick rotation** is the substitution

$$
t \;\longmapsto\; -i\tau, \qquad \tau \in \mathbb{R},
$$

in the time coordinate. Under this substitution, the first coefficient of $\tilde{Q}_-$ changes as

$$
i c t \;\longmapsto\; i c\,(-i\tau) = c\tau,
$$

while the spatial coefficients $x, y, z$ are unchanged. The rotated point is

$$
\tilde{Q}_\mathbb{H} = c\tau\, e_0 + x\, e_1 + y\, e_2 + z\, e_3,
$$

with **all four coefficients real**.

So the standard Wick rotation is the identification

$$
\mathbb{M}_- \;\longrightarrow\; \mathbb{H}_{\mathbb{B}}, \qquad (ict, x, y, z) \;\longmapsto\; (c\tau, x, y, z),
$$

obtained by relabeling the imaginary coefficient $ict$ as a real coefficient $c\tau$. The transformation is real-linear, but it is not an isometry: the quadratic form changes sign in the time–time component. The signature changes from $(3, 1)$ to $(4, 0)$.

## The Trick as a Transfer from $\mathbb{M}_-$ to $\mathbb{H}_{\mathbb{B}}$

The standard Wick rotation is used to convert oscillatory integrals into convergent ones. The Lorentzian path integral

$$
Z = \int \mathcal{D}\phi\; e^{iS[\phi]/\hbar}
$$

has an oscillating integrand, and it is not absolutely convergent. After the Wick rotation, the path integral becomes

$$
Z_E = \int \mathcal{D}\phi\; e^{-S_E[\phi]/\hbar},
$$

with a decaying integrand, and it is convergent (at least formally). The basis of the procedure is that the wave operator of the Lorentzian formulation, $-\partial_t^2/c^2 + \Delta$, becomes the Euclidean Laplacian $\partial_\tau^2/c^2 + \Delta$, which is elliptic and well behaved.

In the biquaternion reading, the operation is the following. The Lorentzian field $\phi$ on $\mathbb{M}_-$ is transferred to a field $\phi_\mathbb{H}$ on $\mathbb{H}_{\mathbb{B}}$ by the relabeling $ict \mapsto c\tau$. The Lorentzian d'Alembertian on $\mathbb{M}_-$,

$$
\Box_{\mathbb{M}_-} = -\frac{1}{c^2}\frac{\partial^2}{\partial t^2} + \Delta,
$$

becomes the elliptic d'Alembertian on $\mathbb{H}_{\mathbb{B}}$,

$$
\Box_{\mathbb{H}} = \frac{1}{c^2}\frac{\partial^2}{\partial \tau^2} + \Delta.
$$

The oscillating phase $e^{iS}$ becomes the decaying exponential $e^{-S_E}$, where $S_E$ is the action of the transferred field. This is the standard trick, expressed in the biquaternion framework as a transfer between two subspaces of $\mathbb{B}$.

So the Wick rotation is a **trick** in the strict sense: it is a change of variable that is useful for some problems and not for others, and it does not correspond to a physical transformation. Its biquaternion content is that the material sector $\mathbb{M}_-$ and the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ are two four-dimensional subspaces of the same algebra, related by relabeling the imaginary first coefficient as a real one.

## Why the Transfer Works: the Properties of $\mathbb{H}_{\mathbb{B}}$

The reason the transfer is useful is that $\mathbb{H}_{\mathbb{B}}$ is better behaved than $\mathbb{M}_-$ in every relevant respect.

| Property | $\mathbb{H}_{\mathbb{B}}$ | $\mathbb{M}_-$ |
|---|---|---|
| Signature of the quadratic form | $(4, 0)$ positive-definite | $(3, 1)$ indefinite |
| d'Alembertian | $\partial_\tau^2/c^2 + \Delta$ (elliptic) | $-\partial_t^2/c^2 + \Delta$ (hyperbolic) |
| Zero divisors | None | Light cone |
| Division algebra | Yes | No |
| Symmetry group | $SO(4)$, compact | $SO(3, 1)$, non-compact |
| Analytic theory | Fueter quaternionic analysis | Lorentzian Clifford analysis |

The quaternion subspace is elliptic, has no zero divisors, is a division algebra, and admits a compact symmetry group. The material sector is hyperbolic, has a light cone of zero divisors, is not a division algebra, and has a non-compact symmetry group. The elliptic character of $\mathbb{H}_{\mathbb{B}}$ is what makes the transferred problem tractable: the elliptic Laplacian has a well-behaved fundamental solution, a Cauchy integral formula with a positive-definite kernel, a maximum principle, and a mean-value property, all of which are properties of elliptic operators and not of hyperbolic ones.

The transfer from $\mathbb{M}_-$ to $\mathbb{H}_{\mathbb{B}}$ therefore replaces a problem in a hyperbolic setting (with an indefinite quadratic form) by a problem in an elliptic setting (with a positive-definite quadratic form). The elliptic problem is easier: it has fewer pathologies, it has more structure, and its solutions behave better at infinity.

## Why the Transfer Sometimes Fails

The same transfer also destroys part of the structure of the original problem. The Lorentzian structure of $\mathbb{M}_-$ — the light cone, the causal ordering of events, the phase $e^{iS/\hbar}$ with its specific oscillation — is not preserved by the transfer to $\mathbb{H}_{\mathbb{B}}$. The signs are changed: the quadratic form becomes positive-definite, the hyperbolic operator becomes elliptic, the light cone disappears (there are no zero divisors on $\mathbb{H}_{\mathbb{B}}$).

When the physics of the problem depends on this Lorentzian structure, the transfer is fatal. The transferred problem is then not equivalent to the original one; it is a different problem, with a different physical content. This is the reason the Wick rotation sometimes fails: not because the calculation is technically difficult, but because the transfer changes the physics.

The two facts — that the transfer is useful (because $\mathbb{H}_{\mathbb{B}}$ is better behaved) and that the transfer changes the physics (because the Lorentzian structure is lost) — are two sides of the same coin. The subspace $\mathbb{H}_{\mathbb{B}}$ is better behaved precisely because it has given up the Lorentzian structure. So the usefulness of the trick and the possibility of its failure are the same fact, seen from two sides.

## A Prediction: Which Applications Transfer, Which Resist

The reading above suggests a classification of the applications of the Wick rotation by whether the physics of the problem depends on the Lorentzian structure or not.

**Applications that are essentially insensitive to the Lorentzian structure** (and therefore transfer harmlessly to $\mathbb{H}_{\mathbb{B}}$):

- The Euclidean path integral, in its role as a generating functional of correlation functions.
- Finite-temperature field theory, in its equilibrium aspects: the Matsubara formalism and the thermal partition function.
- Lattice gauge theory, in its static and equilibrium computations.
- The correspondence between quantum field theory and statistical mechanics, as a formal identity of partition functions.
- Stochastic quantization, as a stochastic process on the Euclidean sector.

**Applications that are essentially sensitive to the Lorentzian structure** (and therefore transfer problematically to $\mathbb{H}_{\mathbb{B}}$):

- Real-time dynamics: transport coefficients, relaxation, response functions.
- Massless-particle physics, where the light cone is essential.
- Non-equilibrium systems, which require real-time methods.
- The sign problem in finite-density QCD, where the complex phase cannot be projected out by the transfer.
- Quantum gravity, where the Euclidean action is unbounded below.
- Any process in which the causal ordering of events matters.

The split is not exact; some applications lie between the two lists. But the general pattern is as follows: whenever a problem is genuinely about **correlations and equilibrium**, the transfer to $\mathbb{H}_{\mathbb{B}}$ is harmless; whenever a problem is genuinely about **causality and dynamics**, the transfer destroys what the problem was about.

The split is observed in practice. The successful uses of the Wick rotation (lattice computations of equilibrium quantities, finite-temperature partition functions, instanton calculus) are all in the first list. The persistent difficulties (sign problem, real-time dynamics, quantum gravity) are all in the second list. The reading of the Wick rotation as a transfer from $\mathbb{M}_-$ to $\mathbb{H}_{\mathbb{B}}$ predicts this pattern.

## Status of the Reading

The reading of the Wick rotation as a transfer from $\mathbb{M}_-$ to $\mathbb{H}_{\mathbb{B}}$ is an **interpretation**, not an established result. What is established is the following.

- The biquaternion algebra contains three natural four-dimensional real subspaces: $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_-$, $\mathbb{M}_+$.
- The three subspaces have distinct signatures: $(4, 0)$, $(3, 1)$, $(1, 3)$.
- The standard Wick rotation acts on a point of $\mathbb{M}_-$ by relabeling the imaginary coefficient $ict$ as a real coefficient $c\tau$, leaving the spatial coefficients unchanged.
- The resulting point lies in $\mathbb{H}_{\mathbb{B}}$.

What is an **interpretation** is the following.

- That the standard Wick rotation is best read as the identification of $\mathbb{M}_-$ with $\mathbb{H}_{\mathbb{B}}$.
- That the usefulness of the trick is explained by the better-behaved character of $\mathbb{H}_{\mathbb{B}}$.
- That the failure of the trick is explained by the loss of the Lorentzian structure of $\mathbb{M}_-$ under the transfer.
- That the split of applications into "transfer harmlessly" and "resist" follows from the structural properties of the two subspaces.

The interpretation is consistent with the known behavior of the Wick rotation. It is not derived from established physics, and it does not constitute a prediction of new physics. It is a structural reading that clarifies the operation and organizes the applications.

## Summary

The standard Wick rotation is the analytic continuation $t \to -i\tau$ of the time coordinate, which converts the Lorentzian structure of spacetime into a Euclidean one and turns the oscillating phase of the Feynman path integral into a decaying exponential. It is usually presented as a trick.

In the biquaternion framework, the standard Wick rotation is the identification of the material sector $\mathbb{M}_-$ with the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, obtained by relabeling the imaginary coefficient $ict$ as a real coefficient $c\tau$ and leaving the spatial coefficients $x, y, z$ unchanged. Both subspaces are four-dimensional real subspaces of the same biquaternion algebra $\mathbb{B}$, and the identification between them is real-linear.

The quaternion subspace $\mathbb{H}_{\mathbb{B}}$ is better behaved than the material sector $\mathbb{M}_-$: it has a positive-definite quadratic form, no zero divisors, a division-algebra structure, an elliptic d'Alembertian, and a compact symmetry group. The Wick rotation is useful because the transferred problem on $\mathbb{H}_{\mathbb{B}}$ is easier than the original problem on $\mathbb{M}_-$.

The same transfer destroys the Lorentzian structure of $\mathbb{M}_-$ — the light cone, the causal ordering, the phase. When the physics of a problem depends on this structure, the transfer is fatal, and the Wick rotation fails. The usefulness of the trick and the possibility of its failure are the same fact.

The reading predicts a split of applications into those that transfer harmlessly to $\mathbb{H}_{\mathbb{B}}$ (equilibrium, correlation, statistical) and those that resist (real-time dynamics, causal propagation, massless particles, the sign problem, quantum gravity). The split is observed in practice.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion subspace: signature $(4, 0)$, elliptic |
| $\mathbb{M}_-$ | Material sector: signature $(3, 1)$, hyperbolic |
| $\mathbb{M}_+$ | Informational sector: signature $(1, 3)$, mirror hyperbolic |
| $c$ | Speed of light in the medium |
| $t$ | Time coordinate on $\mathbb{M}_-$ |
| $\tau$ | Euclidean coordinate on $\mathbb{H}_{\mathbb{B}}$ |
| $ict$ | Imaginary time coefficient on $\mathbb{M}_-$ |
| $t \to -i\tau$ | Standard Wick rotation |
| $\mathbb{M}_- \to \mathbb{H}_{\mathbb{B}}$ | The transfer as an identification of subspaces |

## Further Reading

- G. C. Wick, "Properties of Bethe-Salpeter wave functions," *Physical Review* **96** (1954) 1124–1134, for the original introduction of the standard Wick rotation.
- J. Schwinger, "On the Euclidean structure of relativistic field theory," *Proceedings of the National Academy of Sciences* **44** (1958) 956–965, for the Euclidean formulation of field theory.
- J. Glimm and A. Jaffe, *Quantum Physics: A Functional Integral Point of View* (Springer, 1987), for the rigorous Euclidean approach to constructive quantum field theory.
- M. Le Bellac, *Thermal Field Theory* (Cambridge, 1996), for the finite-temperature imaginary-time formalism.
- M. Creutz, *Quarks, Gluons and Lattices* (Cambridge, 1983), for lattice gauge theory.
- A. M. Polyakov, *Gauge Fields and Strings* (Harwood, 1987), for instantons and non-perturbative effects.
- R. Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta\Delta u = 0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* **7** (1934–35) 307–330, for the elliptic quaternionic analysis of the subspace $\mathbb{H}_{\mathbb{B}}$.
- Roger Penrose, *The Road to Reality* (Knopf, 2004), Chapters 18 and 33, for the complex structure of spacetime.

---

