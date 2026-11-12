# __The Spin Energy-Momentum Tensor__

## Introduction

**The stress of a spinorial field has two parts, a symmetric part that carries the energy and momentum and an antisymmetric part that carries the spin, and only the first of them is a conserved density.** That division is the article's subject. The symmetric part has ten independent components, the antisymmetric part six, the general tensor sixteen. An element of $\mathbb{B}$ has eight real components and can hold four of them.

**The count looks like a defeat and it is not one.** The antisymmetric part of the canonical stress is, by the Belinfante relation, the divergence of the spin tensor. A total divergence carries no charge, so the antisymmetric part contributes nothing to the total energy–momentum of a localised field. The object that a fluid needs is the conserved four-vector, and one element holds exactly that: the energy density in its scalar slot and the momentum density in its vector slot. The limitation and the choice coincide.

**What the element holds of the spin is the density and not the current.** The spin tensor $S^{\lambda\mu\nu}$ has twenty-four components, the Frenkel condition cuts it to twelve, and its time slice at a point is an antisymmetric pair with six, which the condition cuts to three. Those three are the vector slots of one Hermitian element whose scalar slot vanishes. So one element per event holds the spin density exactly, and the spin current needs three more.

**The pair of laws is the rotor's equation read twice.** The energy–momentum law is the conservation of the symmetric part. The spin law is the divergence of the spin current equalling a torque, and the torque is the rotor connection contracted with the spin. When the connection turns about the spin's own axis the torque vanishes, and that is the free rotor's conservation law in components.

**What this article does not do.** It does not reconstruct the sixteen-component tensor as elements, it does not derive the Belinfante relation, and it does not compute the value of the spin. The relation is a theorem of the standard theory and is imported with its convention stated; what the article adds is where each object lands among the algebra's slots and what the slots cannot hold.

## The Count

### Sixteen Against Eight

**A general rank-two tensor in four dimensions has sixteen components, a symmetric one ten and an antisymmetric one six.** An element of $\mathbb{B}$ has eight real components, so no element can be a general stress and no element can be a symmetric stress with its full spatial block.

| object | components | slot in one element |
| --- | --- | --- |
| general $T^{\mu\nu}$ | 16 | not available |
| symmetric part | 10 | not available |
| antisymmetric part | 6 | not available |
| energy and momentum density | 4 | the four slots |

**The four available are the conserved ones.** Energy and the three momentum densities are the components whose conservation laws a fluid uses, and they are exactly the four slots the element has. The three momentum densities are, for a symmetric tensor, the same objects as the three energy fluxes, so a fluid that carries an energy density and an energy flux carries the four-vector and not the flux separately.

**The spatial block is recovered and not stored.** The pressure is the trace of the spatial block and it enters through the equation of state; the shear enters through the transport coefficients of a dissipative theory. Neither is a slot. That is the arrangement [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html) states for the scalar case and [Spin Conservation and the Frenkel Condition](spin-conservation-and-the-frenkel-condition.html) states as a limitation of the category.

### Why the Count Is Not a Defeat

**An antisymmetric part that is a total divergence carries no charge.** That is the content of the Belinfante relation: the antisymmetric part of the canonical stress equals minus one half the divergence of the spin tensor,

$$
T^{[\mu\nu]}_{\mathrm{can}}=-\tfrac12\,\partial_\lambda S^{\lambda\mu\nu},
$$

with $S^{\lambda\mu\nu}$ antisymmetric in its last two indices. Integrating over a localised field, the divergence integrates to a boundary term and vanishes, so the antisymmetric part contributes nothing to the total energy or momentum.

**The relation is imported, and its convention is stated.** The factor $\tfrac12$ and the sign are those of the standard treatment, quoted in [The Gordon Decomposition of the Dirac Current in Biquaternionic Form](the-gordon-decomposition-of-the-dirac-current-in-biquaternionic-form.html) §*The Belinfante improvement*. The article does not re-derive it and does not claim it as framework content.

**What the relation means for the algebra is that the missing six are missing from the charge and not from the description.** A fluid's energy and momentum are the symmetric part's conserved four-vector; the antisymmetric part describes a redistribution inside the field and no transport of charge. So an element that holds four and not sixteen holds everything a fluid conserves, and the rest is either a divergence or a transport coefficient.

**The framework's own statement of the same fact.** The polar word separates the orbital part of the angular momentum into the boost and the intrinsic part into the rotor, so the two are separated by construction and there is no improvement to make. That is the Frenkel article's observation, and this article's count is its arithmetic form.

## The Two Parts

### The Symmetric Part

**The symmetric part is the energy–momentum tensor and its conservation law is the fluid's equation of motion.** In the element $\tilde\Sigma_\Psi=w_{\mathrm{fl}}e_t+\tfrac{i}{c}\vec S_{\mathrm P}$ the scalar slot is the energy density and the vector slot the energy flux; the momentum density is the same object in the other slot of the symmetric tensor.

**The element is Hermitian and that is forced.** The scalar slot is real and the three vector slots are purely imaginary, so the element lies in the informational sector. Without the central $i$ it would not be Hermitian and its scalar divergence would not be a single real law.

**The fluid reads it as an energy current and not as a force.** The quantum stress article's result is that the divergence of the stress is the quantum force and that the part of the energy density carrying the quantum potential integrates to $\int\rho\lvert\nabla\ln\rho\rvert^{2}$, which is positive. That is the scalar case's whole content, and it is symmetric throughout: no antisymmetric part arises there because the rotor is trivial.

### The Antisymmetric Part

**The antisymmetric part exists exactly when the spin varies.** For a field of constant spin the spin tensor is constant, its divergence vanishes, and the canonical stress is symmetric. For a field whose spin direction or spin magnitude varies from event to event, the divergence is non-zero and the canonical stress has an antisymmetric part.

**The tensor's antisymmetry is the spin's, and the algebra states it without a new field.** The spin density is an antisymmetric pair of labels because it is an angular momentum density; the element that carries it is Hermitian with a vanishing scalar slot, and its three vector slots are exactly the three independent components of an antisymmetric pair constrained by the flow.

**The spin's antisymmetry is why the torque is a commutator.** The connection's symmetric part cannot couple to an antisymmetric object, so the source of the spin law is built from the antisymmetric part of the connection alone. That is an algebraic statement about the index structure and it is the reason the source has the form it has.

## The Spin Tensor as One Element

### Twenty-Four, Twelve and Three

**The spin current has twenty-four components and the polar word can hold three of them at a point.** The counting is the article's sharpest statement and it is short.

| stage | object | components |
| --- | --- | --- |
| the tensor | $S^{\lambda\mu\nu}$, antisymmetric in $\mu\nu$ | 24 |
| the Frenkel condition | $S^{\lambda\mu\nu}v_{\Phi,\nu}=0$ | 12 |
| the time slice at an event | $S^{0ij}$ | 3 |
| the polar element | $\rho\tfrac{\hbar}{2}i\hat s$ | 3 |

**The first cut is the condition and the second is a slice.** The Frenkel condition removes, for each $\lambda$, the one component along the flow, leaving twelve. Of the twelve, the slice at an event with the flow's own time direction is the spin density and has three independent components; the other nine are the spatial current of the spin, and they are not slots of the element that carries the density.

**So one element per event holds the spin density exactly, and the spin current needs three more.** The corpus has no article that assembles the four, and this one does not either. What it states is the arithmetic: the element's four slots hold the density after the condition, because the condition is the vanishing of the scalar slot.

### What One Element Cannot Hold

**The spatial current of the spin is not a slot of the density's element, and there is no second slot to borrow.** The element is the density at a point; a current needs a direction as well, and the direction would have to be an index, not a slot. The corpus's arithmetic for the stress and for the spin is the same arithmetic: an element is a value at a point, and a tensor with free indices needs one element per index value.

**The temptation is to write the spin current as one element with a vector index, and it fails on the count.** With $\lambda$ free there are four elements, each with three slots after the condition, which is twelve: the count of the table's second row. So the spin current is four elements and not one, and each of the four is the density's element with a different direction contracted into it.

**The honest statement of the limitation.** The algebra holds the density, the velocity, the spin direction and the phase at a point, and it holds the spin current as a family of four elements. It does not hold the stress, and no single element is the stress. That is a fact about the size of the algebra and not about the physics.

## The Pair of Conservation Laws

### The Energy–Momentum Law

**The conservation of the symmetric part is the vanishing of the scalar divergence of the element.** With $\tilde\Sigma_\Psi=w_{\mathrm{fl}}e_t+\tfrac{i}{c}\vec S_{\mathrm P}$ the law is

$$
\mathrm{Sc}\bigl(\tilde\nabla_\Phi^{\natural}\tilde\Sigma_\Psi\bigr)=0,
$$

which is $\partial_t w_{\mathrm{fl}}+\nabla\cdot\vec S_{\mathrm P}=0$ in the flat case: an energy density whose rate of change is the divergence of its flux. The quantum stress article proves that on solutions the flux carries the quantum potential and that the divergence of the quantum part is the quantum force.

**The law is one real equation and the element has four slots, so three of the four are not constrained by it.** That is not a defect: a conservation law constrains the four-vector's divergence and leaves its curl free, and the curl is the dynamics that the field equation supplies. The same division appears in the scalar fluid, where the continuity equation constrains the density and the mass shell supplies the momentum.

### The Spin Law

**The divergence of the spin current is a torque, and the torque is the rotor connection contracted with the spin.** With the rotor's logarithmic derivative $\tilde u_{\mathrm r}^{-1}\partial_\eta\tilde u_{\mathrm r}=\tfrac12\vec\Omega_\eta$, a real vector part,

$$
\partial_\eta S^{\eta\lambda\nu}_{\Psi,\mathrm{sp}}=\tau^{\lambda\nu},
\qquad
\tau^{\lambda\nu}=\tfrac12\bigl(\Omega^{\lambda}{}_{\rho}S^{\rho\nu}-\Omega^{\nu}{}_{\rho}S^{\rho\lambda}\bigr).
$$

**The display is the rotor's own equation in components.** The rotor's equation is $\partial_\eta\tilde u_{\mathrm r}=\tfrac12\vec\Omega_\eta\tilde u_{\mathrm r}$, and differentiating the spin direction $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$ gives the commutator of the connection with the spin. The conservation law is that statement with the indices put back. [Spin Conservation and the Frenkel Condition](spin-conservation-and-the-frenkel-condition.html) derives it and this article quotes it.

**The torque vanishes when the connection turns about the spin's own axis.** That is the free rotor's conservation, and it is a statement about the geometry of the rotation and not about the field equation.

*Check.* At rest, with the flow $v_{\Phi}=e_t$ and the spin along $\vec e_z$, the spin tensor is $S_{12}=+1$ and the rest of its components vanish. Take the connection's spatial part $\vec\Omega_{0}$ and compute all six components of $\tau$. For $\vec\Omega_{0}=(0,0,2)$ the maximum modulus of $\tau$ is $0.000000$; for $\vec\Omega_{0}=(1,0,0)$ it is $0.500000$; for the mixed $\vec\Omega_{0}=(1,0,1)$ it is $0.500000$. So the torque vanishes exactly when the connection is along the spin and not otherwise.

**What the check establishes and what it does not.** It establishes that the source of the spin law is a commutator and that its kernel is the connection along the spin. It does not establish that the connection is derivable from the field equation: $\vec\Omega_\eta$ is what the polar form's fourth bracket supplies, and the equation for it is the corpus's open question.

## The Gordon Spin Term and the Vorticity

**The Gordon decomposition splits the current into a convection part and a spin part, and the spin part is a bound current.** The identity is

$$
J_{\Phi,\mu}=\frac{\rho}{m}P_{\Phi,\mu}+\frac{1}{k_m}\partial_\nu\bigl(\bar{\tilde\Xi}\Sigma_{\mu\nu}\tilde\Xi\bigr),
$$

with the second term a total divergence by construction and $\Sigma_{\mu\nu}$ the spin generator of the algebra. [The Gordon Decomposition of the Dirac Current in Biquaternionic Form](the-gordon-decomposition-of-the-dirac-current-in-biquaternionic-form.html) proves the identity on shell, in position space and in momentum space, and states that the spin term's own divergence vanishes identically because a symmetric derivative meets an antisymmetric object.

**A bound current is one whose divergence is zero, so it circulates.** The spin term is a curl of the spin density: it is non-zero exactly where the spin density varies from event to event, and its lines close on themselves. That is what makes it a magnetisation rather than a transport: it carries no charge from one place to another, and it is the current that a varying spin magnetisation produces.

**The vorticity is a different object and the two are not the same.** The vorticity 2-form $\omega_{\mu\nu}=\partial_\mu v_{\Phi,\nu}-\partial_\nu v_{\Phi,\mu}$ is the antisymmetrised gradient of the *frame*, and it is non-zero where the velocity varies; the spin term is the divergence of the *spin density*, non-zero where the spin varies. The two have different sources in the word: the vorticity is the gradient of the boost, which is what the velocity is built from, and the spin term is the gradient of the rotor, which is what the spin direction is built from. [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html) carries the split: the frame element that squares to the velocity is the boost and the rotor does not enter it at all, so a varying rotor produces a varying spin and no vorticity.

**Where they meet is the antisymmetric part of the stress.** The stress's antisymmetric part is the divergence of the spin tensor, and the spin tensor is built from the velocity and the spin direction together. So the antisymmetric part is where the varying frame and the varying spin are contracted, and its vanishing is the statement that the spin is transported without torque.

**The strongest objection is that this is bookkeeping.** The objection says that the antisymmetric part carries no charge, so its structure is a convention of how one writes the stress and not a physical object. The answer is that the spin density itself is physical and the antisymmetric part is where the canonical tensor shows it; the Belinfante improvement moves the spin's contribution into the symmetric part's orbital slot, and the total angular momentum is the same before and after. The bookkeeping is a choice; the spin is not.

## The Frenkel Condition as the Scalar Part's Vanishing

**The Frenkel condition says the spin has no component along the flow, and in the element it says the scalar slot is zero.** With the spin element $\tilde S_{\Psi,\mathrm{sp}}=\rho\tfrac{\hbar}{2}i\hat s$ and $\hat s$ a real vector, the scalar part is $\rho\tfrac{\hbar}{2}i\,\hat s_t$, which vanishes exactly when $\hat s$ has no temporal component.

*Proposition.* $\mathrm{Sc}\,\tilde S_{\Psi,\mathrm{sp}}=0$ if and only if $S^{\mu\nu}v_{\Phi,\nu}=0$ in the flow's rest frame.

*Proof.* In the rest frame $v_{\Phi}=e_t$, and the spin tensor of a spin vector $\hat s$ is $S_{\mu\nu}=\varepsilon_{\mu\nu\rho\sigma}v_{\Phi}^{\rho}\hat s^{\sigma}$, which has $S_{0i}=0$ exactly when $\hat s$ is spatial. The element's scalar part is the temporal component of $\hat s$, so the two conditions are the same condition.

**The condition is automatic in the polar word and that is the point.** The rotor is a real unit, so its image of the declared axis is a real vector with no temporal part; the scalar slot of the spin element therefore vanishes identically and the Frenkel condition is not a constraint to be imposed. That is the framework's simplification: a condition that other formulations impose is here a property of the decomposition.

**What the automatic condition costs.** It costs the ability to describe a spin with a temporal component. A field whose spin is not transverse to its flow has no word in this form; the corpus does not exhibit such a field, and it does not prove that none exists. The condition's automatic character is therefore a statement about the chart and not a theorem about matter.

## What Is Established and What Is Interpretation

**Established.** That a general stress has sixteen components, the symmetric part ten and the antisymmetric six, against the element's eight and its four usable slots. That the antisymmetric part of the canonical stress is the divergence of the spin tensor and therefore carries no total charge. That the spin tensor's twenty-four components are cut to twelve by the Frenkel condition and to three at an event. That the spin law is the rotor's equation in components, with a torque that vanishes when the connection is along the spin, checked in three configurations. That the spin element's scalar slot vanishes exactly when the Frenkel condition holds. That the Gordon spin term is a bound current, non-zero where the spin density varies.

**Interpretation.** That the symmetric part is the fluid's energy–momentum and the antisymmetric part its spin. That the spin term of the Gordon split is a magnetisation rather than a transport. That the vorticity and the spin's variation are two faces of the same connection. Each is argued where it is used and none is proved here.

**Not claimed.** It is not claimed that the sixteen-component tensor can be written as a small collection of elements; the corpus records the question as open and this article does not close it. It is not claimed that the Belinfante relation is framework content; it is imported with its convention. It is not claimed that the spin's magnitude is dynamical; it is a normalisation.

## Summary

The stress of a spinorial field divides into a symmetric part that carries the energy and momentum and an antisymmetric part that carries the spin. Of the sixteen components a general tensor has, an element of $\mathbb{B}$ holds four: the energy density and the three momentum densities, which are the conserved ones.

The count is not a defeat, because the antisymmetric part is the divergence of the spin tensor and a divergence carries no charge. The four components a fluid conserves are exactly the four the element holds, and the spatial block is recovered through the equation of state and the transport coefficients.

The spin tensor's twenty-four components are cut to twelve by the Frenkel condition and to three by taking the time slice at an event. Those three are the vector slots of one Hermitian element whose scalar slot vanishes, so one element per event holds the spin density exactly and the spin current needs four.

The pair of laws is the rotor's equation read twice: the energy–momentum law constrains the symmetric part's divergence, and the spin law equates the spin current's divergence to a torque built from the rotor connection and the spin. The torque vanishes exactly when the connection turns about the spin's own axis, which is the free rotor's conservation law.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Sigma_\Psi=w_{\mathrm{fl}}e_t+\tfrac{i}{c}\vec S_{\mathrm P}$ | Energy–momentum element: energy density and flux |
| $T^{\mu\nu}$, $T^{[\mu\nu]}$ | Stress and its antisymmetric part |
| $S^{\lambda\mu\nu}$ | Spin current, antisymmetric in the last two indices |
| $S_{\Psi,\mathrm{sp},\eta,\lambda\nu}$ | Its components in the corpus's letters |
| $\tilde S_{\Psi,\mathrm{sp}}=\rho\tfrac{\hbar}{2}i\hat s$ | Spin density element |
| $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$ | Spin direction |
| $\tilde u_{\mathrm r}^{-1}\partial_\eta\tilde u_{\mathrm r}=\tfrac12\vec\Omega_\eta$ | Rotor connection |
| $\tau^{\lambda\nu}$ | Torque, the spin law's source |
| $\omega_{\mu\nu}=\partial_\mu v_{\Phi,\nu}-\partial_\nu v_{\Phi,\mu}$ | Vorticity 2-form |
| $k_m=mc/\hbar$ | Mass wave number |
| $\rho=r^{2}$ | Density |

## Further Reading

- F. J. Belinfante, "On the spin angular momentum of mesons," *Physica* **6** (1939) 887–898, for the improvement that symmetrises the stress by a divergence of the spin tensor.
- L. Rosenfeld, "Sur le tenseur d'impulsion-énergie," *Mémoires de l'Académie Royale de Belgique* **18** (1940) 1–30, for the same construction in the electromagnetic case.
- J. Frenkel, "Die Elektrodynamik des rotierenden Elektrons," *Zeitschrift für Physik* **37** (1926) 243–262, for the condition that the spin has no component along the flow.
- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter, Part I. General theory," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, for the spin fluid whose stress carries the antisymmetric part.
- The companion articles: [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html), [Spin Conservation and the Frenkel Condition](spin-conservation-and-the-frenkel-condition.html), [The Gordon Decomposition of the Dirac Current in Biquaternionic Form](the-gordon-decomposition-of-the-dirac-current-in-biquaternionic-form.html), [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html), [The Current Algebra](the-current-algebra.html).
