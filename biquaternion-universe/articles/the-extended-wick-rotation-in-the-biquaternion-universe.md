
# The Extended Wick Rotation in the Biquaternion Universe

## Introduction

The companion article described the **standard Wick rotation** as it is used in physics: the analytic continuation $t \to -i\tau$ of the time coordinate, which converts the Lorentzian structure of spacetime into a Euclidean one and turns the Feynman path integral into a statistical-mechanical partition function. The companion article presented this rotation as a **trick** — a contour deformation in the complex time plane, justified by Cauchy's theorem when the fields extend analytically, but not a theorem of quantum field theory.

This article is about a **different** operation. In the biquaternion algebra $\mathbb{B}$, the two complementary four-dimensional subspaces $\mathbb{M}_-$ and $\mathbb{M}_+$ are exchanged by multiplication by the scalar imaginary $i$:

$$
i\,\mathbb{M}_- = \mathbb{M}_+, \qquad i\,\mathbb{M}_+ = \mathbb{M}_-.
$$

This multiplication by $i$ is a **global algebraic operation** on the biquaternion coordinate: it acts on all four coefficients, not just on the time component. We call it the **extended Wick rotation**.

The extended Wick rotation is not the standard Wick rotation. The two operations share the same scalar factor $i$, but they act differently: the standard rotation is a change of a single coordinate within a sector (or within Minkowski space), while the extended rotation is a switch between the two sectors of the biquaternion algebra. The purpose of this article is to define the extended rotation, to describe what changes under it, and to state the hypothesis that it has physical content.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with the three subspaces $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_-$, $\mathbb{M}_+$. Throughout, $c$ denotes the speed of light in the medium.

## A Brief Recap of the Standard Trick

The standard Wick rotation is the substitution

$$
t \to -i\tau, \qquad \tau \in \mathbb{R},
$$

in the time coordinate of relativistic field theory. It is applied to convert oscillatory path integrals into convergent Euclidean ones. The justification is analytic continuation of the integrand in the complex time plane, valid when the fields extend holomorphically in a suitable domain. It is a **trick**: it works in a large class of physically relevant problems, but it is not derived from first principles, and its validity is not guaranteed in general.

The key feature of the standard trick is that **only the time coordinate is rotated**. The spatial coordinates $x, y, z$ are unchanged.

## The Extended Wick Rotation

We now define a different operation.

### Definition

Let $\tilde{Q}$ be a biquaternion. The **extended Wick rotation** is the multiplication of $\tilde{Q}$ by the scalar imaginary $i$:

$$
\tilde{Q} \;\longmapsto\; i\,\tilde{Q}.
$$

The operation acts on the whole biquaternion, not on a single coordinate.

### The Exchange of Sectors

Multiplication by $i$ exchanges the two complementary subspaces:

$$
i\,\mathbb{M}_- = \mathbb{M}_+, \qquad i\,\mathbb{M}_+ = \mathbb{M}_-.
$$

So the extended Wick rotation sends a point of the material sector $\mathbb{M}_-$ to a point of the informational sector $\mathbb{M}_+$, and vice versa.

### Concretely

Take a point of the material sector with physical coordinates

$$
\tilde{Q}_- = i c t\, e_0 + x\, e_1 + y\, e_2 + z\, e_3 \in \mathbb{M}_-.
$$

Applying the extended Wick rotation gives

$$
i\,\tilde{Q}_- = -c t\, e_0 + i x\, e_1 + i y\, e_2 + i z\, e_3 \in \mathbb{M}_+.
$$

Writing the result in the standard form of $\mathbb{M}_+$, whose general element is $q_0\, e_0 + i q'_1\, e_1 + i q'_2\, e_2 + i q'_3\, e_3$ with real $q_0, q'_k$, we identify:

$$
q_0 = -c t, \qquad q'_1 = x, \qquad q'_2 = y, \qquad q'_3 = z.
$$

So the extended Wick rotation acts on the coordinates by:

- $i c t \;\longmapsto\; c t'$ with $t' = -t$ (the time coefficient changes from imaginary to real, with a sign flip),
- $x\,e_k \;\longmapsto\; i x'\, e_k$ with $x' = x$ (each spatial coefficient changes from real to imaginary, with the numerical value unchanged).

The **algebraic character** of the coordinates changes: what was imaginary on $\mathbb{M}_-$ becomes real on $\mathbb{M}_+$, and what was real becomes imaginary. This is the content of the exchange of the two sectors.

## The Inverse Operation

The extended Wick rotation is a bijection from $\mathbb{M}_-$ to $\mathbb{M}_+$, and from $\mathbb{M}_+$ to $\mathbb{M}_-$. Its inverse is not the same operation: multiplication by $i$ applied twice gives

$$
i\,(i\,\tilde{Q}) = -\tilde{Q}.
$$

So the square of the extended Wick rotation is $-\mathrm{id}$. The operation is **not involutive**: applying it twice does not return the original element, but its negative.

The inverse operation is multiplication by $-i$:

$$
\tilde{Q} \;\longmapsto\; -i\,\tilde{Q}.
$$

This sends $\mathbb{M}_-$ to $\mathbb{M}_+$ (via $-i$) and $\mathbb{M}_+$ to $\mathbb{M}_-$ (via $-i$), and it is the inverse of the extended Wick rotation.

## Difference from the Standard Wick Rotation

The extended Wick rotation and the standard Wick rotation share the scalar factor $i$, but they act differently.

**Standard Wick rotation.**
- Acts on **one coordinate**: the time coordinate.
- The spatial coordinates are left unchanged.
- The rotation is a **change of the coordinate system** within a fixed sector (or within Minkowski space).
- The justification is **analytic continuation**: the integrand of the path integral is deformed in the complex time plane.
- The operation is a **trick**.

**Extended Wick rotation.**
- Acts on the **entire biquaternion coordinate**.
- All four coordinates are affected: the time coefficient changes from imaginary to real, and the three spatial coefficients change from real to imaginary.
- The rotation is a **switch between two sectors** of the biquaternion algebra: $\mathbb{M}_-$ and $\mathbb{M}_+$.
- The operation is purely **algebraic**: it is multiplication by $i$, with no analyticity conditions.

The extended Wick rotation is **not** the standard Wick rotation, and it is **not** a reformulation of it. It is a different operation that acts on a different object.

## The Physical Reading

The extended Wick rotation is a well-defined algebraic operation. Its physical interpretation is the hypothesis of this article.

### The Material Sector and the Informational Sector

The two subspaces $\mathbb{M}_-$ and $\mathbb{M}_+$ have complementary structures:

- **$\mathbb{M}_-$ (material sector).** The first coordinate is imaginary ($ict$), the three remaining coordinates are real ($x, y, z$). The signature of the quadratic form is $(3, 1)$.
- **$\mathbb{M}_+$ (informational sector).** The first coordinate is real ($ct'$), the three remaining coordinates are imaginary ($i x', i y', i z'$). The signature of the quadratic form is $(1, 3)$.

The two signatures are mirror images. The extended Wick rotation exchanges them.

### The Hypothesis

The hypothesis of this article is that the extended Wick rotation has **physical content**: that it corresponds to a genuine transformation between the material sector of physical spacetime and the informational sector, and that the informational sector is not merely a mathematical complement of the material sector but a physical arena with its own structure.

This hypothesis is motivated by the structural complementarity of the two sectors, and by the earlier observation that the informational sector carries the algebraic structure of a quantum-informational system (the spin-1/2 identification developed in the companion article). It is **not** derived from established physics.

### What the Hypothesis Does and Does Not Claim

**It does claim:**

- The extended Wick rotation is a well-defined algebraic operation on the biquaternion algebra.
- It exchanges the two complementary sectors $\mathbb{M}_-$ and $\mathbb{M}_+$.
- Its square is $-\mathrm{id}$, and its inverse is multiplication by $-i$.
- Its physical interpretation as a switch between material and informational sectors is a hypothesis, motivated by the structural complementarity of the two sectors.

**It does not claim:**

- That the extended Wick rotation is the standard Wick rotation.
- That the Euclidean sector of the standard formulation is the informational sector.
- That the informational sector has been observed.
- That the extended Wick rotation has any empirical content.
- That the informational sector has a specified dynamics.

## Applications

The standard Wick rotation is applied to a wide range of problems: the Euclidean path integral, finite-temperature field theory, lattice gauge theory, instantons, and the correspondence between quantum field theory and statistical mechanics. The extended Wick rotation can be applied to the same problems, but each application is a **research direction**, not an established result. We describe the biquaternion reading for each, and flag what would need to be studied.

Each of the following deserves its own in-depth treatment. The present article only states the direction.

### The Euclidean Path Integral

**Standard treatment.** The Lorentzian path integral

$$
Z = \int \mathcal{D}\phi\; e^{iS[\phi]/\hbar}
$$

is oscillatory and not absolutely convergent. The standard Wick rotation $t \to -i\tau$ converts it to the Euclidean path integral

$$
Z_E = \int \mathcal{D}\phi\; e^{-S_E[\phi]/\hbar},
$$

which is convergent (at least formally). The Euclidean formulation is the basis of constructive quantum field theory, lattice gauge theory, and finite-temperature field theory.

**Biquaternion reading.** In the biquaternion framework, the Lorentzian path integral is an integral over fields on the material sector $\mathbb{M}_-$. The extended Wick rotation sends this to an integral over fields on the informational sector $\mathbb{M}_+$: the fields, defined as functions on the material sector, are transported to the informational sector, and the action $S$ becomes an action $S_+$ on $\mathbb{M}_+$.

**Direction for future study.** How does the Lorentzian path integral transform under the extended Wick rotation? What is the structure of the resulting integral over the informational sector? Is the resulting integral convergent, oscillatory, or of some other character? These questions require the development of field theory on the informational sector, which does not yet exist.

**What is unknown.** The physical interpretation of the action $S_+$ on the informational sector, and the relation between the Lorentzian path integral and its image under the extended Wick rotation.

### Finite-Temperature Field Theory

**Standard treatment.** At finite temperature $T$, quantum field theory is formulated on a Euclidean spacetime that is periodic in the imaginary time direction, with period $\beta = \hbar/(k_B T)$. The thermal partition function is

$$
Z(\beta) = \mathrm{Tr}\,e^{-\beta H} = \int \mathcal{D}\phi\; e^{-S_E[\phi]/\hbar},
$$

with the imaginary time variable ranging over $[0, \beta)$. The periodicity in the imaginary time gives the **Matsubara frequencies**: discrete Fourier modes in the compact time direction.

**Biquaternion reading.** In the biquaternion framework, the periodicity of the material sector in the imaginary time $ict$ becomes, under the extended Wick rotation, a periodicity of the informational sector in the real time $ct'$, with $t' = -t$. The thermal state of the material sector would be the counterpart of a periodic state in the informational sector.

**Direction for future study.** What is the precise form of the periodicity condition on the informational sector? Does the period of the informational time have a thermodynamic interpretation? What are the analogues of the Matsubara frequencies on the informational sector?

**What is unknown.** Whether the informational sector admits a natural notion of temperature, and whether the periodicity in the informational time direction corresponds to a thermodynamic state.

### Lattice Gauge Theory

**Standard treatment.** Non-perturbative computations in QCD and other gauge theories are performed on a Euclidean lattice in $\mathbb{R}^4$. The lattice discretization is introduced in the Euclidean setting, where the path integral is a convergent integral over the lattice fields. The continuum limit is taken by sending the lattice spacing to zero. At finite temperature, the lattice has a finite extent in the Euclidean time direction, identified with $\beta$.

**Biquaternion reading.** The lattice is naturally a discretization of a four-dimensional subspace in its Euclidean coordinates. Under the extended Wick rotation, the lattice is transported to the informational sector $\mathbb{M}_+$.

**Direction for future study.** What is the correct lattice formulation of the informational sector? Is there a natural discretization of the imaginary spatial coordinates? What is the continuum limit of such a discretization? Does the resulting structure have a natural interpretation, perhaps analogous to a spin network or a tensor-network structure?

**What is unknown.** Whether the informational sector admits a natural lattice formulation, and whether it would be computationally useful.

### Instantons and Tunneling

**Standard treatment.** In quantum mechanics and quantum field theory, tunneling phenomena are described by **instantons**: classical solutions of the Euclidean equations of motion. The tunneling amplitudes are obtained from the Euclidean action of these solutions. Examples include the double-well potential in quantum mechanics, the $\theta$-vacuum of QCD, and the anomalous breaking of chiral symmetry.

**Biquaternion reading.** An instanton is a solution of the field equations in a Euclidean setting. Under the extended Wick rotation, such a solution is transported to the informational sector.

**Direction for future study.** What are the analogues of instantons on the informational sector? Do the field equations on $\mathbb{M}_+$ have classical solutions? If so, what is the physical interpretation of their action?

**What is unknown.** Whether the informational sector admits a natural notion of tunneling, and whether the "informational instantons" have a physical interpretation.

### The Correspondence Between QFT and Statistical Mechanics

**Standard treatment.** The Euclidean path integral is formally identical to the partition function of a statistical-mechanical system, with the Euclidean action playing the role of the energy functional. A quantum field theory in $d$ spacetime dimensions is equivalent (in the Euclidean formulation) to a statistical-mechanical system in $d$ dimensions. This correspondence is the basis of the Wilsonian approach to effective field theory, of the renormalization group, and of the theory of critical phenomena.

**Biquaternion reading.** The correspondence is between fields on the material sector and statistical-mechanical systems on the informational sector. The "energy functional" of the statistical-mechanical system is the action $S_+$ on the informational sector.

**Direction for future study.** What is the precise form of the correspondence in the biquaternion framework? Is there a natural interpretation of the "informational action" $S_+$ in terms of entropy, Fisher information, or another information-theoretic quantity?

**What is unknown.** Whether the informational sector has a natural interpretation in terms of statistical mechanics.

### Stochastic Quantization

**Standard treatment.** The Euclidean path integral is equivalent to a stochastic differential equation (the Langevin equation) with a noise term, whose stationary distribution is $e^{-S_E}$. This is the basis of stochastic quantization.

**Biquaternion reading.** The stochastic process is naturally formulated on a Euclidean setting. Under the extended Wick rotation, it is transported to the informational sector, where the stationary distribution describes the material sector.

**Direction for future study.** What is the precise form of the stochastic process on the informational sector? Does the informational sector admit a natural notion of noise or stochasticity?

**What is unknown.** Whether the stochastic interpretation of the informational sector has physical content.

## Summary of the Status

**Established.**

- The biquaternion algebra and its two complementary four-dimensional subspaces.
- The exchange $i\,\mathbb{M}_- = \mathbb{M}_+$ and $i\,\mathbb{M}_+ = \mathbb{M}_-$.
- The specific form of the exchange on the coordinates: $ict \mapsto ct'$ with $t' = -t$, and $x_k \mapsto i x_k$.
- The square of the operation: $(i)^2 = -1$.
- The inverse: multiplication by $-i$.
- The mirror signatures of the two subspaces: $(3, 1)$ and $(1, 3)$.
- The standard Wick rotation, its applications, and its status as a trick.

**Hypothesis.**

- That the extended Wick rotation has physical content, i.e., that it corresponds to a genuine physical transformation.
- That the informational sector is a physical arena, not only a mathematical construction.
- That the structural complementarity of the two sectors has physical significance.

**Open directions.**

- The development of field theory on the informational sector.
- The interpretation of the action $S_+$ on $\mathbb{M}_+$.
- The applications listed above, each of which deserves its own study.
- The question of whether the extended Wick rotation has any empirical content.

## Summary

The extended Wick rotation is the multiplication by the scalar imaginary $i$ of the entire biquaternion coordinate. It exchanges the two complementary four-dimensional subspaces $\mathbb{M}_-$ and $\mathbb{M}_+$, converting the imaginary time and real space of the material sector into real time and imaginary space in the informational sector.

The extended Wick rotation is not the standard Wick rotation. The standard rotation acts on the time coordinate only and is justified by analytic continuation; it is a trick. The extended rotation acts on all four coordinates, is a purely algebraic operation, and corresponds to a switch between the two sectors of the biquaternion algebra.

The extended Wick rotation is a well-defined algebraic operation with the following properties: its square is $-\mathrm{id}$; its inverse is multiplication by $-i$; it exchanges the two sectors; it exchanges the two signatures $(3, 1)$ and $(1, 3)$.

The hypothesis of this article is that the extended Wick rotation has physical content — that it corresponds to a genuine physical transformation between the material and the informational sectors, and that the informational sector is a physical arena, not only a mathematical construction. This hypothesis is motivated by the structural complementarity of the two sectors and by the spin-1/2 identification of the informational sector, but it is not derived from established physics.

The applications of the extended Wick rotation — to the Euclidean path integral, finite-temperature field theory, lattice gauge theory, instantons, and stochastic quantization — are **directions for future study**. Each deserves its own treatment. The present article has only stated the operation and its structural content.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{M}_-$ | Material sector: imaginary time, real space |
| $\mathbb{M}_+$ | Informational sector: real time, imaginary space |
| $c$ | Speed of light in the medium |
| $t$ | Time on the material sector |
| $t'$ | Time on the informational sector, with $t' = -t$ |
| $\tilde{Q}_- = ict\,e_0 + x\,e_1 + y\,e_2 + z\,e_3$ | Material-sector biquaternion |
| $i\tilde{Q}_- = ct'\,e_0 + i x'\,e_1 + i y'\,e_2 + i z'\,e_3$ | Informational-sector biquaternion |
| $\tilde{Q} \mapsto i\tilde{Q}$ | Extended Wick rotation |
| $\tilde{Q} \mapsto -i\tilde{Q}$ | Inverse extended Wick rotation |
| $(i)^2 = -1$ | Square of the operation |

## Further Reading

- G. C. Wick, "Properties of Bethe-Salpeter wave functions," *Physical Review* **96** (1954) 1124–1134, for the original introduction of the standard Wick rotation.
- J. Schwinger, "On the Euclidean structure of relativistic field theory," *Proceedings of the National Academy of Sciences* **44** (1958) 956–965, for the Euclidean formulation of field theory.
- J. Glimm and A. Jaffe, *Quantum Physics: A Functional Integral Point of View* (Springer, 1987), for the rigorous Euclidean approach to constructive quantum field theory.
- M. Le Bellac, *Thermal Field Theory* (Cambridge, 1996), for the finite-temperature imaginary-time formalism.
- M. Creutz, *Quarks, Gluons and Lattices* (Cambridge, 1983), for lattice gauge theory.
- A. M. Polyakov, *Gauge Fields and Strings* (Harwood, 1987), for instantons and non-perturbative effects.
- Roger Penrose, *The Road to Reality* (Knopf, 2004), Chapters 18 and 33, for the complex structure of spacetime.
- V. V. Kassandrov, "Relativistic Algebra of Space-Time and Algebrodynamics" (2006), for a biquaternionic approach to complexified geometry.

