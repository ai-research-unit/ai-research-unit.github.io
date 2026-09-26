# __The Stern–Gerlach Experiment in Biquaternionic Form__

## Introduction

The Stern–Gerlach experiment passes a beam of neutral atoms through an inhomogeneous magnetic field and finds the beam split into a discrete number of components rather than smeared into a continuum. For a spin-1/2 atom the beam splits into exactly two, and the two deflections are equal and opposite. The experiment is the original demonstration of **space quantisation**, and it is the canonical physical realisation of a projective measurement of a spin component.

This article carries the experiment into the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ of the companion articles. It is not an article about new physics: the Stern–Gerlach effect is standard and well established, and its two spot pattern is reproduced here exactly. The article is about **where** the experiment lives within the algebra, and which structural features of the framework its analysis exposes.

The findings are stated here in advance, so that the reader can hold them against the text.

1. **The field coupling is a Hermitian element of $\mathbb{M}_+$.** The magnetic Hamiltonian $\tilde{H} = -\gamma B_z\,\tilde{S}_3$ is an element of the Hermitian subspace, as are the force operator and the observable whose measurement the apparatus performs. The field does not couple to the material sector directly; it couples to the informational sector, and the material sector carries only the resulting centre-of-mass motion.
2. **The two beams are the two idempotents of $\tilde{S}_3$.** The spin part of the apparatus performs the spectral decomposition $\tilde{S}_3 = \tfrac{\hbar}{2}\tilde{P}_+(\hat{z}) - \tfrac{\hbar}{2}\tilde{P}_-(\hat{z})$, and the two outgoing beams are the two idempotents, correlated with the two spatial directions of deflection. The force eigenvalues are the eigenvalues of $\tilde{S}_3$, which is the algebraic content of space quantisation.
3. **The beam intensities are the Born pair.** For an incident state $\tilde{\rho} = \tfrac12(e_0 + i\mathbf{r})$, the two intensities are $\mathrm{Tr}(\tilde{P}_\pm\tilde{\rho}) = \tfrac12(1\pm r_3)$, the trace pairing of the framework.
4. **The measurement destroys the transverse coherence.** The Stern–Gerlach apparatus entangles the spin with the centre-of-mass coordinate; tracing the position out leaves the spin state with its off-diagonal (transverse) Bloch components erased, $\mathbf{r} = (0,0,r_3)$. The coherence that survives is exactly the component along the field, and the lost components are the ones the apparatus cannot read.
5. **A rotated apparatus gives the $\cos^2(\theta/2)$ law**, and the rotation that carries one analyser direction into another is a rotor in the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$ acting by conjugation.

The article uses the read-list notation throughout. Throughout, the algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_0 = 1, e_1, e_2, e_3$ and $e_k^2 = -e_0$, the scalar imaginary is $i$, the Hermitian and anti-Hermitian subspaces are $\mathbb{M}_+$ and $\mathbb{M}_-$, the observables are $\tilde{H} = h_0 e_0 + i\mathbf{h} \in \mathbb{M}_+$, the pure states are the idempotents $\tilde{P}_\pm(\hat{\mu}) = \tfrac12(e_0 \pm i\hat{\mu})$ for a unit pure real quaternion $\hat{\mu}$, and the trace formula is $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ with $\mathrm{Tr}(e_0) = 2$.

The companion articles supply the pieces:
- Companion article *Spin-1/2 Quantum Mechanics in Biquaternionic Form*, for the spin operators, the idempotents and the Born rule.
- Companion article *Exercise: Measuring Spin Along an Arbitrary Direction*, for the rotated-analyser probabilities.
- Companion article *Exercise: Successive Measurements of Spin*, for the algebra of successive measurements.
- Companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the trace formula and the pure-state idempotents.
- Companion article *The Measurement Problem in Algebraic Form*, for the projective rule and the fate of the coherence.

## The Experiment and the Standard Account

### The Inhomogeneous Field and the Magnetic Force

A neutral atom with magnetic moment $\boldsymbol{\mu} = \gamma\mathbf{S}$ placed in a magnetic field $\mathbf{B}$ has potential energy

$$
U = -\boldsymbol{\mu}\cdot\mathbf{B} = -\gamma\,\mathbf{S}\cdot\mathbf{B},
$$

where $\gamma$ is the gyromagnetic ratio and $\mathbf{S}$ the spin operator. If the field is directed along $z$ with a gradient along the same direction,

$$
\mathbf{B} = B(z)\,\hat{z}, \qquad B'(z) = \frac{\partial B}{\partial z},
$$

then the force on the atom along $z$ is the negative gradient of the potential,

$$
F_z = -\frac{\partial U}{\partial z} = \gamma\,\frac{\partial B}{\partial z}\,S_z = \gamma B'\,S_z .
$$

Strictly, a field of the form $\mathbf{B} = B(z)\hat{z}$ alone is not a static magnetic field: $\nabla\cdot\mathbf{B} = 0$ requires $\partial B_z/\partial z = -\partial B_x/\partial x - \partial B_y/\partial y$, so a longitudinal gradient must be accompanied by transverse components, which make the direction of the local field depend on position. Across the width of the beam in the Stern–Gerlach geometry those components are small, and the standard treatment retains $F_z = \gamma B' S_z$ for the deflection; the same idealisation is made here.

This is the standard result, and it is standard in a second sense: $S_z$ is an operator, so the force is an operator. Its eigenvalues are $\pm\tfrac{\hbar}{2}\gamma B'$, and a beam with its spin in an eigenstate of $S_z$ is deflected by an amount proportional to that eigenvalue.

### Deflection and the Two Beams

For a beam of speed $v$ crossing a field region of length $L$, the atom spends a time $t = L/v$ in the field, and the transverse displacement is

$$
\Delta z = \frac{1}{2}\,a\,t^2 = \frac{F_z}{2m}\left(\frac{L}{v}\right)^2 = \frac{\gamma B' S_z L^2}{2 m v^2}.
$$

With $S_z = \pm\hbar/2$ the two displacements are

$$
\Delta z_\pm = \pm\frac{\hbar\gamma B' L^2}{4mv^2},
$$

so the two beams are separated by $\hbar\gamma B' L^2/(2mv^2)$. A classical magnetic moment of arbitrary orientation would give a continuous band of deflections; the observation of two discrete spots is the evidence of quantisation. The deflection is the same for every atom in one beam, so the experiment measures the eigenvalue of $S_z$ for each atom.

### Two Remarks on the Classical Limit

Two remarks on the classical limit clarify what is and is not quantum about the experiment. First, the force formula $F_z = \gamma B' S_z$ is classical in form; only the spectrum of $S_z$ is quantum. Second, the separation of the two spots is proportional to $\hbar$, so the two beams coalesce in the formal limit $\hbar \to 0$, when the quantum of action disappears. In the biquaternion framework this is the statement that the two idempotents $\tilde{P}_\pm(\hat{z})$, whose difference produces the splitting, are constructed from the algebra's complex structure: the $\hbar$ enters only in the scale of the observable $\tilde{S}_3 = \tfrac{\hbar}{2} i e_3$, and it is supplied to the framework from outside.

## The Field Coupling in the Informational Sector

### The Magnetic Hamiltonian

In the biquaternion framework the spin operators are the Hermitian elements

$$
\tilde{S}_k = \frac{\hbar}{2}\,i e_k \in \mathbb{M}_+, \qquad k = 1,2,3,
$$

which under the isomorphism $e_0 \mapsto I$, $e_j \mapsto -i_{\mathrm{mat}}\sigma_j$ (where $i_{\mathrm{mat}}$ is the matrix imaginary, the image of the scalar imaginary $i$) map to $\tfrac{\hbar}{2}\sigma_k$. The Hamiltonian of the atom in the field $\mathbf{B} = B(z)\hat{z}$ is the Hermitian element

$$
\tilde{H} = -\gamma B(z)\,\tilde{S}_3 = -\frac{\hbar\gamma B(z)}{2}\,i e_3 \in \mathbb{M}_+ .
$$

That the Hamiltonian is an element of $\mathbb{M}_+$ is the first structural fact of the article: the field couples to the **informational sector**, not to the material sector. The observable it multiplies, $\tilde{S}_3$, is a Hermitian element of the same subspace, and its eigenvectors are idempotents. The centre-of-mass coordinate $z$, by contrast, is a real spatial coordinate, hence a component of the material sector $\mathbb{M}_-$; the field gradient acts on the spin through $\mathbb{M}_+$ and the deflection is read in $\mathbb{M}_-$.

### The Force Operator

The force operator along $z$ is the negative gradient of the Hamiltonian with respect to the material coordinate,

$$
\tilde{F}_3 = -\frac{\partial \tilde{H}}{\partial z} = \gamma\,\frac{\partial B}{\partial z}\,\tilde{S}_3 = \frac{\hbar\gamma B'}{2}\,i e_3 .
$$

So the force is $\gamma B'$ times the spin observable, exactly as in the standard account, and it is again a Hermitian element of $\mathbb{M}_+$. Its spectral decomposition is inherited from that of $\tilde{S}_3$:

$$
\tilde{F}_3 = \gamma B'\,\tilde{S}_3 = \frac{\hbar\gamma B'}{2}\,\tilde{P}_+(\hat{z}) - \frac{\hbar\gamma B'}{2}\,\tilde{P}_-(\hat{z}).
$$

Each of the two eigenspaces is one-dimensional (the two idempotents are rank one and complementary), so each atom emerges in one of the two beams with a definite deflection. This is the algebraic content of the two-spot pattern: the number of beams is the number of terms in the spectral decomposition, and their deflections are the eigenvalues.

## The Spectral Decomposition of $\tilde{S}_3$

The observable $\tilde{S}_3 = \tfrac{\hbar}{2}i e_3$ has the spectral decomposition

$$
\tilde{S}_3 = \frac{\hbar}{2}\,\tilde{P}_+(\hat{z}) - \frac{\hbar}{2}\,\tilde{P}_-(\hat{z}),
\qquad
\tilde{P}_\pm(\hat{z}) = \tfrac12\left(e_0 \pm i e_3\right).
$$

The verification is a direct multiplication. Using $e_3^2 = -e_0$,

$$
\tilde{S}_3\,\tilde{P}_+(\hat{z}) = \frac{\hbar}{4}\,i e_3\left(e_0 + i e_3\right)
= \frac{\hbar}{4}\left(i e_3 - e_3^2\right)
= \frac{\hbar}{4}\left(i e_3 + e_0\right)
= \frac{\hbar}{2}\,\tilde{P}_+(\hat{z}),
$$

and the same computation with $e_3 \to -e_3$ gives $\tilde{S}_3\tilde{P}_- = -\tfrac{\hbar}{2}\tilde{P}_-$. The idempotents are Hermitian, idempotent, and of trace one, as required of pure-state projectors; their sum is $\tilde{P}_+ + \tilde{P}_- = e_0$ and their product vanishes, so they are the two complementary outcomes of the measurement.

### The General State and Its Resolution

An incident beam is in general not in an eigenstate of $\tilde{S}_3$. Its spin state is a Hermitian, positive, trace-one element of $\mathbb{M}_+$,

$$
\tilde{\rho} = \tfrac12\left(e_0 + i\mathbf{r}\right), \qquad \mathbf{r}\in\mathbb{R}^3, \quad |\mathbf{r}|\leq 1,
$$

with $\mathbf{r}$ the Bloch vector. The probabilities of the two outcomes are the trace pairings

$$
p_\pm = \mathrm{Tr}\!\left(\tilde{P}_\pm(\hat{z})\,\tilde{\rho}\right)
= \tfrac12\left(1 \pm r_3\right),
$$

since $\tilde{P}_\pm(\hat{z})\,\tilde{\rho} = \tfrac14(e_0 \pm i e_3)(e_0 + i\mathbf{r})$ has scalar part $\tfrac14(1 \pm r_3)$ — using $\mathrm{Sc}(e_3\mathbf{r}) = -\mathbf{r}\cdot\hat{z} = -r_3$ — and $\mathrm{Tr}(\cdot) = 2\,\mathrm{Sc}(\cdot)$. The two intensities sum to one, $p_+ + p_- = 1$, and they are equal for a beam polarised transversely to the field, as they must be by symmetry.

### Why the Resolution Is Not a Mixture

It is important to state what the spectral decomposition does **not** say. Writing $\tilde{\rho} = p_+ \tilde{P}_+ + p_- \tilde{P}_-$ is a decomposition of the *probabilities*, not of the *state*: the identity

$$
\tfrac12\left(e_0 + i\mathbf{r}\right)
= \tfrac{1+r_3}{2}\tilde{P}_+(\hat{z}) + \tfrac{1-r_3}{2}\tilde{P}_-(\hat{z})
$$

holds **if and only if** $r_1 = r_2 = 0$. For a state with a transverse Bloch component, the right-hand side is not equal to $\tilde{\rho}$: it is the diagonal part of $\tilde{\rho}$ in the $\hat{z}$ basis, and the difference

$$
\tilde{\rho} - \left[p_+\tilde{P}_+(\hat{z}) + p_-\tilde{P}_-(\hat{z})\right] = \tfrac12 i\left(r_1 e_1 + r_2 e_2\right)
$$

is the **coherence**. The apparatus separates the two diagonal components into two spatially distinct beams and makes no further use of the coherence; that is the physical meaning of the off-diagonal terms, and the next section states their fate precisely.

## The Two Beams and the Loss of Coherence

### Spin–Position Entanglement

The full state of an atom in the apparatus is not a spin state alone: the spin is correlated with the centre-of-mass coordinate $z$, which lives in the material sector. Write the initial state as a tensor product of a spin state and a spatial wavepacket, and let $\tilde{U}$ be the evolution through the field region. Because the Hamiltonian $\tilde{H} = -\gamma B(z)\tilde{S}_3$ is diagonal in the $\hat{z}$ spin basis, the evolution acts on the two spin components with opposite phase gradients and displaces them in opposite directions:

$$
\left(c_+ |{+z}\rangle + c_- |{-z}\rangle\right)\otimes|\phi\rangle
\;\longmapsto\;
c_+ |{+z}\rangle\otimes|\phi_+\rangle + c_- |{-z}\rangle\otimes|\phi_-\rangle ,
$$

with $|\phi_\pm\rangle$ wavepackets centred on the two deflections $\Delta z_\pm$. This is the standard description of a Stern–Gerlach measurement as a **pre-measurement**: the apparatus has not yet been read, and the two components are still coherent.

### The Reduced Spin State

If the two beams are separated and only one is retained (or if the position is simply traced out), the spin state is obtained by the partial trace over the spatial degree of freedom. Because the two wavepackets are orthogonal, $\langle\phi_+|\phi_-\rangle = 0$, the cross terms drop and the reduced state is

$$
\tilde{\rho}_{\mathrm{spin}} = |c_+|^2 \tilde{P}_+(\hat{z}) + |c_-|^2 \tilde{P}_-(\hat{z})
= \tfrac12\left(e_0 + i\,r_3 e_3\right),
\qquad r_3 = |c_+|^2 - |c_-|^2 .
$$

In biquaternion form the transverse components of the Bloch vector are erased, $\mathbf{r} = (0,0,r_3)$. This is the **decoherence** induced by the measurement, and it is exactly the loss of the coherence term identified above. The framework expresses it without a separate postulate: the two idempotents are the two outcomes, the position states that label them are orthogonal, and the cross terms in the partial trace vanish.

### The Post-Measurement State

If instead the apparatus is read and one outcome is selected — say the upper beam — the spin state is updated by the projective rule

$$
\tilde{\rho}' = \frac{\tilde{P}_+(\hat{z})\,\tilde{\rho}\,\tilde{P}_+(\hat{z})}{\mathrm{Tr}\!\left(\tilde{P}_+(\hat{z})\tilde{\rho}\right)} = \tilde{P}_+(\hat{z}),
$$

where the last equality uses $\tilde{P}_+\tilde{\rho}\tilde{P}_+ = p_+\tilde{P}_+$ for a rank-one idempotent, with $p_+ = \mathrm{Tr}(\tilde{P}_+\tilde{\rho})$. The post-measurement state is the idempotent itself. The Stern–Gerlach apparatus is therefore a physical realisation of the projective measurement rule of the informational sector: a Hermitian observable is resolved into its idempotents, and each outcome prepares the corresponding idempotent.

## Sequential Stern–Gerlach and the Rotation of the Analyser

### Rotating the Field Direction

Turn the analysing magnet so that its field lies in the $xz$-plane at an angle $\theta$ from the $z$-axis:

$$
\hat{n} = \sin\theta\, e_1 + \cos\theta\, e_3 .
$$

The observable measured by the rotated analyser is $\tilde{S}(\hat{n}) = \hat{n}_k\tilde{S}_k = \tfrac{\hbar}{2} i\hat{n}$, whose eigenstates are the idempotents $\tilde{P}_\pm(\hat{n}) = \tfrac12(e_0 \pm i\hat{n})$:

$$
\tilde{S}(\hat{n})\,\tilde{P}_\pm(\hat{n}) = \pm\frac{\hbar}{2}\,\tilde{P}_\pm(\hat{n}).
$$

The rotation that carries the $z$-direction into $\hat{n}$ is the real-quaternion rotor

$$
\tilde{R}(\theta) = \exp\!\left(\frac{\theta}{2}e_2\right) = \cos\frac{\theta}{2}\,e_0 + \sin\frac{\theta}{2}\,e_2 \in \mathbb{H}_{\mathbb{B}},
$$

and it acts on the observables by conjugation. Direct multiplication gives

$$
\tilde{R}(\theta)\,\tilde{S}_3\,\tilde{R}(\theta)^\dagger
= \frac{\hbar}{2}\,i\left(\sin\theta\, e_1 + \cos\theta\, e_3\right)
= \tilde{S}(\hat{n}),
$$

and correspondingly $\tilde{R}\tilde{P}_+(\hat{z})\tilde{R}^\dagger = \tilde{P}_+(\hat{n})$. So the rotation of the analyser is an $SU(2)$ rotor conjugation, and the space of analyser directions is the sphere of unit vectors $\hat{n}\in S^2$, which is the Bloch sphere of the idempotents.

### The $\cos^2(\theta/2)$ Law

An atom prepared spin-up along $z$ and passed through an analyser at angle $\theta$ is found spin-up along $\hat{n}$ with probability

$$
p_+ = \mathrm{Tr}\!\left(\tilde{P}_+(\hat{n})\,\tilde{P}_+(\hat{z})\right)
= 2\,\mathrm{Sc}\!\left(\tilde{P}_+(\hat{n})\,\tilde{P}_+(\hat{z})\right).
$$

Computing the product with $\hat{n} = \sin\theta\, e_1 + \cos\theta\, e_3$, $e_1e_3 = -e_2$, $e_3^2 = -e_0$,

$$
\tilde{P}_+(\hat{n})\,\tilde{P}_+(\hat{z})
= \tfrac14\left(e_0 + i\hat{n}\right)\left(e_0 + ie_3\right)
= \tfrac14\left[e_0 + ie_3 + i\hat{n} - \hat{n}e_3\right]
= \tfrac14\left[(1+\cos\theta)e_0 + ie_3 + i\hat{n} + \sin\theta\, e_2\right],
$$

whose scalar part is $\tfrac14(1+\cos\theta)$. Hence

$$
p_+ = \tfrac12\left(1+\cos\theta\right) = \cos^2\frac{\theta}{2},
$$

in agreement with the companion exercise *Exercise: Measuring Spin Along an Arbitrary Direction*. The result depends on the analyser direction only through $\hat{n}\cdot e_3 = \cos\theta$, which is the geometric content: the probability is a function of the angle between the preparation axis and the analysis axis, and of nothing else.

### Three Analysers and the Role of the Intermediate Measurement

The classic sequence $z$–$x$–$z$ shows the difference between a measurement and a rotation. With the middle analyser in place, the joint probability of "up" at both the first and the last stage is

$$
p(+,+) = \mathrm{Tr}\!\left(\tilde{P}_+(\hat{x})\tilde{P}_+(\hat{z})\right)\cdot\mathrm{Tr}\!\left(\tilde{P}_+(\hat{z})\tilde{P}_+(\hat{x})\right)
= \tfrac12\cdot\tfrac12 = \tfrac14,
$$

so the last analyser finds "up" and "down" with equal probability: the intermediate $x$-measurement has scrambled the $z$-information. If the middle analyser is removed, the sequence is a single rotation, the two $z$-stages are perfectly correlated, and the joint probability is $1$. In the algebra the difference is the insertion of the idempotent $\tilde{P}_+(\hat{x})$, which projects and destroys the coherence, versus the insertion of a rotor $\tilde{R}$, which does not. This is the same contrast the companion exercises draw between measurement and evolution; the Stern–Gerlach arrangement is its physical realisation.

## What the Algebra Adds and What It Does Not

**Standard physics, transcribed.** The magnetic coupling $U = -\boldsymbol{\mu}\cdot\mathbf{B}$, the force $F_z = \mu_z B'$, the deflection formula, the two-spot pattern, the $\cos^2(\theta/2)$ law and the three-magnet coherence experiment are all standard. None of them depends on the biquaternion structure beyond the identification of the spin observable with a Hermitian element of $\mathbb{M}_+$.

**What the biquaternion notation provides.**

- **A single home for the field coupling and the measurement.** The Hamiltonian, the force operator, and the observable that the apparatus reads are all elements of the same subspace $\mathbb{M}_+$; the states are the idempotents of that subspace; and the outcome probabilities are the trace pairing. The experiment does not require an object outside the algebra, except for the centre-of-mass coordinate that carries the deflection and the mass $m$ that enters the deflection formula.
- **Space quantisation as a spectral decomposition.** The finite number of beams is the finite number of terms in the spectral decomposition of the observable, and the deflection of each beam is the corresponding eigenvalue. In the algebra this is a statement about the rank-one idempotents of $\mathbb{M}_+$, which are automatically complete and orthogonal.
- **Decoherence as a partial trace with orthogonal labels.** The loss of the transverse Bloch components is the vanishing of the cross terms between two orthogonal spatial wavepackets. The algebra makes it visible that what is destroyed is exactly the coherence term $\tfrac12 i(r_1e_1+r_2e_2)$, and that the surviving component is the one along the field.
- **The rotation of the apparatus is a rotor.** The analyser direction is the axis $\hat{n}$ of the idempotent, and the passage from one axis to another is conjugation by a unit real quaternion. The analyser's parameter space is the Bloch sphere, the same sphere on which the states live.

**What the algebra does not provide.** The deflection formula contains the mass $m$, the beam speed $v$ and the field length $L$; these are properties of the centre-of-mass motion in the material sector and of the apparatus, not of the informational sector. The framework labels the material coordinate in which the deflection is measured but does not supply the deflection itself. Similarly, the scale $\hbar$ of the observable $\tilde{S}_3$ is supplied to the framework from outside; the algebra fixes the form of the observable but not the value of the quantum of action. The Stern–Gerlach experiment, like the rest of non-relativistic quantum mechanics in this series, is a transcription into the algebra and not a new prediction.

## Open Questions

1. **The continuous Stern–Gerlach effect.** When the field is not perfectly aligned and the beam is not perfectly collimated, the two spots acquire a small asymmetry and the measurement is weak rather than projective. Does the algebra's description of the weak-measurement limit — a partial entanglement with the position — have structural content beyond the partial trace used above?

2. **The spatial wavepacket as a material-sector object.** The deflection lives in the spatial part of $\mathbb{M}_-$, while the spin lives in $\mathbb{M}_+$. Is there a formulation in which the spin–position entanglement is written as an element of a single algebra, rather than as a tensor product of an informational and a material factor? The companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* leaves the coupling between the sectors open, and the Stern–Gerlach entanglement is a concrete instance of it.

3. **The role of the field gradient in the algebra.** The coupling $\tilde{H} = -\gamma B(z)\tilde{S}_3$ uses the material coordinate $z$ as a parameter multiplying an informational observable. Is there an algebraic object that generates this parameter dependence, or is the gradient an external field in the strict sense?

4. **Time-of-flight and the phase.** A Stern–Gerlach interferometer recombines the two beams after they have acquired different phases. The relative phase depends on the field integral and on the trajectory. Which of these phases are geometric and which dynamical is a distinction the algebra is able to draw, since the geometric part is the holonomy of a rotor and the dynamical part is generated by the central $ie_0$; the interferometric Stern–Gerlach arrangement is a natural place to look for it.

5. **Empirical contact.** As everywhere in the series, the reformulation predicts exactly what the standard account predicts; whether the framework's additional structure implies any deviation is open. Nothing in this article changes that.

## Summary

The Stern–Gerlach experiment passes a beam of spin-1/2 atoms through an inhomogeneous magnetic field and finds it split into two. In the biquaternion framework the magnetic coupling is the Hermitian element $\tilde{H} = -\gamma B(z)\tilde{S}_3 \in \mathbb{M}_+$, with $\tilde{S}_3 = \tfrac{\hbar}{2}ie_3$; the force is $\tilde{F}_3 = \gamma B'\tilde{S}_3$; and the two beams are the two idempotents in the spectral decomposition

$$
\tilde{S}_3 = \frac{\hbar}{2}\tilde{P}_+(\hat{z}) - \frac{\hbar}{2}\tilde{P}_-(\hat{z}),
\qquad
\tilde{P}_\pm(\hat{z}) = \tfrac12\left(e_0 \pm ie_3\right).
$$

The deflection of each beam is the corresponding eigenvalue, $\pm\hbar\gamma B'L^2/(4mv^2)$, so the number of beams and their separation are the spectral data of a Hermitian element of the informational sector. For an incident state $\tilde{\rho} = \tfrac12(e_0+i\mathbf{r})$ the intensities are the trace pairings $p_\pm = \tfrac12(1\pm r_3)$, and the two intensities sum to one.

The apparatus entangles the spin with the centre-of-mass coordinate, which lives in the material sector. When the position is traced out, the orthogonal spatial wavepackets erase the cross terms and the reduced spin state is $\tfrac12(e_0 + ir_3e_3)$: the transverse Bloch components are lost, and only the component along the field survives. The coherence that is destroyed is the term $\tfrac12 i(r_1e_1 + r_2e_2)$; the biquaternion form of the measurement shows this without an additional decoherence postulate.

A rotated analyser measures $\tilde{S}(\hat{n}) = \tfrac{\hbar}{2}i\hat{n}$ for $\hat{n} = \sin\theta\,e_1 + \cos\theta\,e_3$, and the rotation from the $z$-axis to $\hat{n}$ is the real-quaternion rotor $\tilde{R}(\theta) = e^{\theta e_2/2}$ acting by conjugation, $\tilde{R}\tilde{S}_3\tilde{R}^\dagger = \tilde{S}(\hat{n})$. The single-beam probability is $\cos^2(\theta/2)$, and the intermediate measurement in the $z$–$x$–$z$ sequence destroys the coherence and reduces the joint probability to $1/4$, whereas a rotation without an intermediate measurement leaves it at $1$. The experiment is a physical realisation of the two primitive operations of the algebraic formalism: projective measurement onto an idempotent, and reversible evolution by a rotor.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, central, $i^2 = -1$ |
| $\mathbb{M}_+$ | Hermitian (informational) subspace: observables, states, Hamiltonians |
| $\mathbb{M}_-$ | Anti-Hermitian (material) subspace: the centre-of-mass coordinate |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace; home of the rotation rotors |
| $\tilde{S}_k = \tfrac{\hbar}{2}ie_k$ | Spin observable along $\hat{k}$ |
| $\tilde{H} = -\gamma B(z)\tilde{S}_3$ | Magnetic Hamiltonian in the field $\mathbf{B} = B\hat{z}$ |
| $\tilde{F}_3 = \gamma B'\tilde{S}_3$ | Stern–Gerlach force operator |
| $\tilde{P}_\pm(\hat{\mu}) = \tfrac12(e_0 \pm i\hat{\mu})$ | Pure-state idempotent |
| $\tilde{\rho} = \tfrac12(e_0 + i\mathbf{r})$ | General (mixed) spin state; $\mathbf{r}$ the Bloch vector |
| $p_\pm = \mathrm{Tr}(\tilde{P}_\pm(\hat{z})\tilde{\rho}) = \tfrac12(1\pm r_3)$ | Beam intensities (Born rule) |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula |
| $\hat{n} = \sin\theta\,e_1 + \cos\theta\,e_3$ | Rotated analyser direction |
| $\tilde{R}(\theta) = \exp(\tfrac{\theta}{2}e_2)$ | Rotor carrying $\hat{z}$ to $\hat{n}$ |
| $\Delta z_\pm = \pm\hbar\gamma B'L^2/(4mv^2)$ | Deflections of the two beams |
| $\cos^2(\theta/2)$ | Probability of "up" at the rotated analyser |

## Further Reading

- W. Gerlach and O. Stern, "Der experimentelle Nachweis der Richtungsquantelung im Magnetfeld," *Zeitschrift für Physik* **9** (1922) 349–352, for the original experiment.
- W. Gerlach and O. Stern, "Das magnetische Moment des Silberatoms," *Zeitschrift für Physik* **9** (1922) 353–355, for the magnetic moment determination.
- D. Bohm, *Quantum Theory* (Prentice-Hall, 1951), for the wave-packet treatment of the Stern–Gerlach measurement and its criticism of the naive trajectory picture.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the standard treatment of spin-1/2, the Stern–Gerlach experiment, and successive measurements.
- M. O. Scully, B.-G. Englert, and H. Walther, "Quantum optical tests of complementarity," *Nature* **351** (1991) 111–116, for the which-path and coherence experiments with rotated analysers.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the Bloch sphere, projective measurement, and the partial trace.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for idempotents and the spin-1/2 representation.
