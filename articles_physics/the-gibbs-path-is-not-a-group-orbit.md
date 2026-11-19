# __The Gibbs Path Is Not a Group Orbit__

## Introduction

A state at temperature $1/\beta$ is a point of the Bloch ball, and the family over $\beta$ is a curve in it. The question of this article is what kind of curve. The answer decides whether a temperature change is a motion of the reversible group or an operation of the channel category, and the two answers are mutually exclusive.

The curve is a diameter through the centre. Under the congruence group it is an orbit: a boost along its axis translates $\beta$ exactly, by the amount $\theta/\lvert\vec h_\Psi\rvert$. That fact is true and it is worthless, because the same group sends any state to any state — the action is transitive, measuring radii from $0.100949$ to $0.997636$, so *every* curve is an orbit and the word says nothing.

What distinguishes the thermal path is the affine structure. A congruence is affine exactly when it is a rotation, and a rotation fixes the radius, hence the temperature. So no group element that changes the temperature is a channel. The channel that does change it is affine and is not a group element. Each category supplies exactly one half of what a thermal change needs, and neither supplies both. That is the content of the title: the thermal path is not an orbit in the category where orbits mean something.

The findings are stated in advance.

1. **The path is a geodesic of both metrics of the ball.** The Klein distance from the centre is $\beta\lvert\vec h_\Psi\rvert$ exactly, so the thermal parameter is the arc length; the Bures distance is $\tfrac12\arcsin(\tanh\beta\lvert\vec h_\Psi\rvert)$, also exactly, and the path is a geodesic in both.
2. **The two metrics differ only in the density of arc length.** The Klein density is constant, $\lvert\vec h_\Psi\rvert$; the Bures density is $\tfrac12\lvert\vec h_\Psi\rvert\operatorname{sech}(\beta\lvert\vec h_\Psi\rvert)$, which decays and is integrable. The total Bures length of the half-path is $\pi/4$, and that integrability is the third law.
3. **The congruence group acts on the ball projectively, and the action is genuine.** Composition holds to $4.3\times10^{-16}$ for boosts and $1.0\times10^{-16}$ for rotations.
4. **The action is transitive.** From one state the boosts reach every radius in the interior, measured from $0.100949$ to $0.997636$ on four hundred draws.
5. **A boost along the axis is a translation of the thermal parameter.** $\beta'=\beta-\theta/\lvert\vec h_\Psi\rvert$, verified to $4.6\times10^{-16}$ on two hundred random pairs; the state passes through infinite temperature into negative temperature, and the parameter is translated, not rescaled.
6. **That translation is not affine, and therefore not a channel.** The non-affinity of a projected boost is $0.101822$ at rapidity $0.3$, $0.141042$ at $1$ and $0.070345$ at $2$; for a rotation it is $3.0\times10^{-16}$.
7. **The channel that changes the temperature is affine and is not a group element.** It is a mixture with the identity, its semigroup law is exact, it decreases the purity at the rate $-2\gamma(P-\tfrac12)$ — measured $-0.379999810$ against $-0.380000000$ — and its fixed point is the state of the bath: the centre for the fully depolarising member, the pole for damping, and any prescribed Gibbs state for the thermal member.

The notation is that of the companions. The state is $\tilde{Ϛ}_{\Psi}=\tfrac12(e_t+i\vec s_{\Psi})$; the Gibbs state of the Hamiltonian $\vec h_\Psi$ is $\vec s_{\Psi}=-\tanh(\beta\lvert\vec h_\Psi\rvert)\vec u_\Psi$; the radius is $r=\lvert\vec s_\Psi\rvert=\tanh(\beta\lvert\vec h_\Psi\rvert)$; the congruence is $\mathrm{Cg}_{\tilde U}:\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$; the trace of the $2\times2$ image is $2\,\mathrm{Sc}$; the linear entropy is $N=\tfrac14(1-r^{2})$.

Two conventions carry weight. The projected map is the congruence followed by normalisation, $\mathrm{Rp}_{\tilde U}(\vec s)=\mathrm{Vec}\bigl(\tilde U\tilde{Ϛ}_{\Psi}(\vec s)\tilde U^{*}\bigr)/\mathrm{Sc}\bigl(\tilde U\tilde{Ϛ}_{\Psi}(\vec s)\tilde U^{*}\bigr)$, and it is the map that acts on the state space. The sample value of the Hamiltonian magnitude is $\lvert\vec h_\Psi\rvert=1.7$ wherever a table needs one; every formula is homogeneous in it.

## The Path

### The Gibbs family as a curve

**The family over $\beta$ is a straight segment through the centre of the ball.** With the axis read off the Hamiltonian, $\vec s_{\Psi}(\beta)=-\tanh(\beta\lvert\vec h_\Psi\rvert)\vec u_\Psi$, and the only thing that changes with $\beta$ is the radius. At $\beta=0$ the state is the centre, the maximally mixed state; as $\beta\to\infty$ it approaches the pole $-\vec u_\Psi$; for $\beta<0$ it approaches $+\vec u_\Psi$ and the populations are inverted. The curve is a diameter and the two ends of the diameter are the two poles.

**Every thermodynamic quantity is a function of the one parameter.** The radius is $r=\tanh(\beta\lvert\vec h_\Psi\rvert)$, the linear entropy is $N=\tfrac14(1-r^{2})=\tfrac14\operatorname{sech}^{2}(\beta\lvert\vec h_\Psi\rvert)$, and the spectral entropy is a function of $N$. Nothing else in the state varies, so the path carries one degree of freedom and the whole of the thermodynamics of this family is the thermodynamics of a single number.

**The numbers, for $\lvert\vec h_\Psi\rvert=1.7$.**

| $\beta$ | $r$ | $N$ | $S_{\mathrm{vN}}$ | $d_{K}$ from the centre | $d_{B}$ from the centre | Bures density |
| --- | --- | --- | --- | --- | --- | --- |
| $0.0$ | $0.000000000$ | $0.250000000$ | $1.000000000$ | $0.000000000$ | $0.000000000$ | $0.850000000$ |
| $0.2$ | $0.327477395$ | $0.223189639$ | $0.921196015$ | $0.340000000$ | $0.166816257$ | $0.803130162$ |
| $0.5$ | $0.691069470$ | $0.130605747$ | $0.620902735$ | $0.850000000$ | $0.381483826$ | $0.614370091$ |
| $1.0$ | $0.935409071$ | $0.031252468$ | $0.205775994$ | $1.700000000$ | $0.604707140$ | $0.300532247$ |
| $2.0$ | $0.997774928$ | $0.001111298$ | $0.012520285$ | $3.400000000$ | $0.752037275$ | $0.056671440$ |
| $4.0$ | $0.999997519$ | $0.000001240$ | $0.000026129$ | $6.800000000$ | $0.784284389$ | $0.001893415$ |

**Read the two distance columns against each other.** The Klein distance grows without bound and is exactly the thermal parameter times the Hamiltonian. The Bures distance converges: at $\beta=4$ it is already $0.784284$, and the limit is $\pi/4=0.785398$. The same path, the same points, and one ruler says the end is infinitely far while the other says it is a quarter of a radian away.

### The two arc lengths

**The Klein distance is the thermal parameter, exactly, for every pair.** Along the axis the signed coordinate is $z=s_{z}=-\tanh(\beta\lvert\vec h_\Psi\rvert)$, and $\operatorname{artanh}z=-\beta\lvert\vec h_\Psi\rvert$ for both signs. Hence
$$
d_{K}\bigl(\vec s(\beta_1),\vec s(\beta_2)\bigr)=\lvert\vec h_\Psi\rvert\,\lvert\beta_2-\beta_1\rvert ,
$$
with no case split, because the signed coordinate is monotone in $\beta$. The numbers at $\beta=0.2$ and $0.9$ are $1.190000000$ against $1.190000000$, and across the centre, from $\beta=-1$ to $\beta=2.5$, they are $5.950000000$ against $5.950000000$.

**The Bures distance is bounded, and it is also exact.** For two points of the family the lifts are in the plane spanned by the centre and the axis, so
$$
d_{B}\bigl(\vec s(\beta_1),\vec s(\beta_2)\bigr)
=\tfrac12\bigl\lvert\arcsin(\tanh\beta_2\lvert\vec h_\Psi\rvert)-\arcsin(\tanh\beta_1\lvert\vec h_\Psi\rvert)\bigr\rvert .
$$
The path is a geodesic in this metric as well, with no case split: from $\beta=-1$ to $\beta=2.5$ the direct distance is $1.375842036883$ and the distance through any of six intermediate points is the same to $2.2\times10^{-16}$. The two ends of the whole path, $\beta=\mp40$, are at $1.570796326795=\pi/2$, so the family is a geodesic of length $\pi/2$ and the half-family has length $\pi/4$.

**Both metrics make the path a geodesic, and the difference is the density.** Differentiating the two expressions gives the arc-length densities
$$
\frac{d d_{K}}{d\beta}=\lvert\vec h_\Psi\rvert,
\qquad
\frac{d d_{B}}{d\beta}=\tfrac12\lvert\vec h_\Psi\rvert\operatorname{sech}\bigl(\beta\lvert\vec h_\Psi\rvert\bigr).
$$
The first is constant; the second decays like $e^{-\beta\lvert\vec h_\Psi\rvert}$, and its integral over the half-line is $\tfrac12\arcsin 1=\pi/4$.

**This is the third law in one line.** A ruler whose arc-length density is constant puts the pure boundary at infinity, and a ruler whose density is integrable puts it at a finite distance that no finite parameter reaches. The boundary is unreachable because the parameter must be infinite, not because the distance is infinite; the distance is $\pi/4$.

### The sign of $\beta$ is not a distance

**Cooling and heating are one path traversed in two directions, and neither metric can say which is which.** The state depends on $\beta$ through $\tanh(\beta\lvert\vec h_\Psi\rvert)$, so $\beta$ and $-\beta$ give the same radius and opposite populations. The radius is even in $\beta$, and both metrics are functions of the radius.

**The consequence is that the radius folds and the point does not.** Traversed from $-\infty$ to $+\infty$ the point runs monotonically from one pole to the other through the centre, while the radius falls to zero at $\beta=0$ and rises again. The state at $\beta$ and the state at $-\beta$ have the same radius and are antipodal: they are two points, not one, and the Klein distance between them is $2\lvert\beta\rvert\lvert\vec h_\Psi\rvert$.

**So the sign of the parameter is a position and not a distance.** It names the side of the centre, and the ball records it as the antipodal point of the same radius: $d_{B}(\beta,-\beta)=0.878632$ at $\beta=0.6$, which is the distance across the centre. Neither metric from the centre can tell a cooling from a heating, because both depend on $\beta$ only through $\lvert\beta\rvert$. The arrow is in the parameter and in the channel that drives it, not in the geometry of the state space.

## The Group Does Act

### The projective action is a genuine action

**The projected map is a group action on the ball, and the check is the composition law.** For two boosts,
$$
\lVert\mathrm{Rp}_{\tilde U_2}\mathrm{Rp}_{\tilde U_1}(\vec s)-\mathrm{Rp}_{\tilde U_2\tilde U_1}(\vec s)\rVert=4.3\times10^{-16},
$$
and for two rotations $1.0\times10^{-16}$. Normalisation is a quotient by a positive scalar, and a quotient of a linear action by a scalar is a well-defined action; the numbers confirm that the implementation respects it. So the ball does carry an action, and the vocabulary of orbits is available.

**The action is transitive.** From the state $-\tfrac12\vec e_z$ the projected boosts reach radii from $0.100949$ to $0.997636$ on four hundred random draws, and the directions are rotated continuously by the rotations. Every interior state is in the orbit of every other.

**A transitive action has one orbit, and it is the whole ball.** The word therefore cannot distinguish the thermal path from any other curve: a diameter, a circle, a spiral, all are orbits of one-parameter subgroups or of nothing in particular. Being an orbit is not a property a curve can fail to have.

### A boost along the axis is a translation

**What the group does to the thermal parameter is exact and simple, on the axis.** Take a Gibbs state with axis $\vec u_\Psi$ and a boost of rapidity $\theta$ along the same axis. The projected image is again a Gibbs state of the same axis, with
$$
\beta'=\beta-\frac{\theta}{\lvert\vec h_\Psi\rvert},
$$
verified to $4.6\times10^{-16}$ on two hundred random pairs. In radius form, $r'=\tanh\bigl(\theta-\operatorname{artanh}r\bigr)$, which is the statement that the boost adds to the rapidity of the state and re-reads the result as a radius.

**The translation passes through the two ends of the parameter range.** A boost of $\theta=\beta\lvert\vec h_\Psi\rvert$ takes the state to the centre, that is, to infinite temperature; a larger boost takes it to negative $\beta$, where the populations are inverted, and the state approaches the opposite pole. For $\beta=0.5$ the value $\theta=0.85$ is exactly $\beta\lvert\vec h_\Psi\rvert$ and lands on the centre; $\theta=0.935$ gives $\beta'=-0.05$, and the populations are inverted.

**This is why the group looks like a thermal machine and is not one.** A translation of $\beta$ is exactly what a thermal contact does to a family at equilibrium, and the group produces it exactly. But the translation is a congruence, and no congruence that is not a rotation preserves $2\,\mathrm{Sc}$ on the whole slice. The translation therefore moves mixtures in a way that no physical process could, and the affinity test detects it.

**The translation is not the relativistic temperature transformation.** The companion on the partition function in a moving frame computes the temperature a moving observer reads, $T/\gamma$, from the period of the thermal element along imaginary time. The translation here is a property of the projected congruence of one state, and no period enters it. The two quantities answer different questions and the article does not identify them; both are exact, and both are kinematic.

### The Orbit of the One-Parameter Group

**The two statements hold together and they are not in tension.** The path is an orbit of a one-parameter group of projected boosts, exactly; and it is not an orbit in the sense that matters, because the action that produces it is transitive, so the orbit relation is the universal relation. A relation that holds between every pair of points carries no information about any pair.

**What the orbit picture does supply is the negative result.** If the thermal path were an orbit of a group of *channels*, then a temperature change would be a reversible operation, entropy would be conserved, and the second law would have nothing to say. The orbit picture is available only because the group is larger than the channel group, and the excess is exactly the part that moves the radius.

## The Affine Test

### Affine exactly on the rotations

**A map on the ball is affine when it preserves mixtures of states, and the congruence passes that test exactly when it is a rotation.** On two hundred random mixtures the deviation
$$
\bigl\lVert \mathrm{Rp}_{\tilde U}\bigl(\lambda\vec a+(1-\lambda)\vec b\bigr)-\bigl(\lambda\,\mathrm{Rp}_{\tilde U}\vec a+(1-\lambda)\mathrm{Rp}_{\tilde U}\vec b\bigr)\bigr\rVert
$$
is $3.0\times10^{-16}$ for a rotation of $40^\circ$ and $2.9\times10^{-16}$ for one of $120^\circ$; for a boost it is $0.101822$ at rapidity $0.3$, $0.141042$ at $1$ and $0.070345$ at $2$.

**The proof is the scalar part.** The congruence is linear and normalisation divides by $2\,\mathrm{Sc}$, so the map is affine exactly when the divisor is one, that is, when $2\,\mathrm{Sc}$ is preserved on the whole slice. The doubled scalar part under the congruence is $\cosh\theta_{\mathrm{rpd}}+s_{\parallel}\sinh\theta_{\mathrm{rpd}}$, which is constant in $\vec s$ only when $\sinh\theta_{\mathrm{rpd}}=0$. That is the theorem of the companion article, read as a statement about mixtures rather than about slices.

**The consequence is a prohibition.** An affine group element is a rotation, a rotation preserves the radius, and the radius is $\tanh(\beta\lvert\vec h_\Psi\rvert)$. So the only affine group elements that leave the temperature alone are the rotations, and they leave it alone exactly. **No group element that is a channel changes a temperature.**

### What an affine map would have to do

**A thermal operation must move the radius and preserve mixtures, and the two demands are compatible only outside the group.** The maps that satisfy both are the affine contractions of the ball toward a fixed point; they are not congruences, and their fixed point is the state the environment imposes.

**The prohibition is not an accident of this algebra.** It follows from the same line as the previous articles: the congruence is an action on the cone, the state space is a section of the cone, and an affine map of the section is a map that respects the section's affine structure. The group respects it only on the compact part. The compact part acts on the section, and it is the part that does not change the temperature.

## The Semigroup That Does the Work

### The mixture channel in the algebra

**The simplest channel that changes a radius is the mixture with the identity, and it has an exact biquaternion form.** For $\lambda\in[0,1]$,
$$
\mathcal E_\lambda(\tilde Q)=(1-\lambda)\tilde Q+\lambda\,\mathrm{Sc}(\tilde Q)\,e_t ,
$$
which on the slice reads $\vec s\mapsto(1-\lambda)\vec s$. It is affine by construction, it preserves $2\,\mathrm{Sc}$, and it fixes the centre.

**It is a semigroup, and the law is exact.** Composing two members gives $(1-\lambda_1)(1-\lambda_2)=1-(\lambda_1+\lambda_2-\lambda_1\lambda_2)$, which is the parameter of a third member; the numerical check returns $0.0$ and not a small residue, because the identity is algebraic.

**Its effect on the thermal parameter is a contraction and not a translation.** The Gibbs family maps into itself, with
$$
\tanh\bigl(\beta'\lvert\vec h_\Psi\rvert\bigr)=(1-\lambda)\tanh\bigl(\beta\lvert\vec h_\Psi\rvert\bigr),
$$
so $\beta'$ is defined for every $\beta$ and every $\lambda$, and $\beta'$ is closer to zero than $\beta$. For $\lvert\vec h_\Psi\rvert=1.7$, $\beta=1.2$ and $\lambda=0.5$ the new parameter is $\beta'=0.310222$, because $\tanh(1.2\cdot1.7)=0.966747$ becomes $0.483374$; for $\lambda=0.8$ it is $0.115185$, from $0.193349$. The map is monotone, it never crosses the centre, and it has the centre as its limit.

**So the group translates and the channel contracts.** The same path, two maps: one shifts $\beta$ by a constant and can invert the populations, the other scales $\tanh\beta\lvert\vec h_\Psi\rvert$ and cannot. Only the second is a physical operation on a state that an observer holds.

### The generator is not a derivation

**The one-parameter semigroup has a generator, and the generator is not a commutator.** Differentiating at $\lambda=0$ with rate $\gamma$ gives
$$
\frac{d\vec s}{dt}=-\gamma\,\vec s ,
$$
whose residual against a finite step is $1.8\times10^{-11}$ at $\Delta t=10^{-6}$. In the algebra the same statement is $\dot{\tilde Q}=-\gamma\bigl(\tilde Q-\mathrm{Sc}(\tilde Q)e_t\bigr)$.

**A derivation would preserve the purity and this does not.** For a commutator generator the radius is constant and the purity $\tfrac12(1+r^{2})$ is a constant of the motion; a rotation of $0.9$ rad changes the radius by $0.0$ exactly. The thermal generator gives
$$
\frac{d}{dt}\tfrac12(1+r^{2})=-2\gamma\bigl(P-\tfrac12\bigr),
$$
measured as $-0.379999810$ against the closed form $-0.380000000$ at $\gamma=1$ and $r^{2}=0.38$. The purity flows to the value $\tfrac12$ of the centre.

**The sign of the flow is the sign of the physics.** The purity decreases, so $\beta$ decreases in modulus, so the flow is toward infinite temperature. The depolarising channel is a heating channel and its fixed point is the centre.

### The fixed point is the state of the bath

**Which state a channel fixes is a property of the channel, and the family has a member for each choice.** The depolarising member fixes the centre; a damping member,
$$
\vec s\mapsto\sqrt{1-p}\,\vec s_{\perp}+(1-p)s_{\parallel}\vec e_z+p\,\vec e_z ,
$$
fixes the pole $+\vec e_z$, which is the ground state of the Hamiltonian along $-\vec e_z$; it is affine to $1.1\times10^{-16}$ and it fixes the pole exactly. An affine member with a prescribed fixed point can be written at once: with $\vec s_{*}=-r_{*}\vec e_z$,
$$
\vec s\mapsto\sqrt{1-p}\,\vec s_{\perp}+\bigl((1-p)s_{\parallel}-p\,r_{*}\bigr)\vec e_z
$$
returns $-r_{*}\vec e_z$ for every $p$, verified at $r_{*}=0.3$ and $0.7$. Complete positivity narrows the admissible $p$; the fixed point does not depend on which admissible value is chosen.

**The fixed point is the only place where the notion of equilibrium enters.** The path is the same for all three; the channel is different, and the difference is where it stops. A thermodynamics of states therefore needs two data and not one: the family, which is geometry, and the fixed point, which is the bath.

## The Two Categories, Side by Side

**The table is the article's claim in one object.**

| | the congruence group | the channels |
| --- | --- | --- |
| $2\,\mathrm{Sc}$ | moved by a boost | preserved |
| the map on the ball | projective, non-affine | affine |
| the affine members | the rotations, exactly | all |
| the orbit of a state | the whole ball | the sphere of constant radius |
| the action on $\beta$ | a translation, $\beta-\theta/\lvert\vec h_\Psi\rvert$ | a contraction toward the fixed point |
| the purity | constant, on any orbit | monotone |
| what it can do to a temperature | change it, not as an operation | change it, as an operation |
| the fixed point | none | the state of the bath |

**Each column is complete on one axis and empty on the other.** The group has the exact action and no physical operation; the channels have the operation and no group parameter. A thermal change needs the radius to move and the mixtures to be respected, and the two demands are met by different columns.

**The sphere of constant radius is the orbit in the second column, and the path crosses it once.** The unitary orbits are the spheres $\lvert\vec s\rvert=\mathrm{const}$, and the thermal path is a diameter, which meets each sphere in a pair of antipodal points, that is, once per value of $\lvert\beta\rvert$. The path is therefore a **transversal** to the orbit foliation of the reversible channel group, and moving along it is by construction leaving every reversible orbit.

**That is the precise sense in which the path is not an orbit.** The Gibbs path is not an orbit of the group of channels; it is the normal to the foliation by its orbits, and the Klein metric makes it a geodesic that meets every orbit orthogonally. A reversible operation moves within a sphere and cannot leave it; a thermal change is a motion between spheres.

## Objections

**The objection is that the boost does change the temperature, so the group does act on the thermal family and the article's title is false.** The objection is correct on its first clause and the article concedes it: the translation $\beta'=\beta-\theta/\lvert\vec h_\Psi\rvert$ is exact to $4.6\times10^{-16}$, and it is a group element.

**The answer is that the clause is not enough, because the same group changes every other family too.** The action is transitive, so the translation of $\beta$ is one instance of a map that carries any state anywhere. A group that can do everything cannot be the group of a thermodynamic process, because a thermodynamic process is constrained: it preserves $2\,\mathrm{Sc}$, it respects mixtures, and it cannot increase the purity for free. Those three constraints are the channel axioms, and the translation satisfies none of them.

**A second objection is that the affinity test is a convention about what counts as a mixture.** The answer is that a mixture is an operational notion: $\lambda\vec a+(1-\lambda)\vec b$ is the state of a system prepared by a coin flip, and any operation that treats a coin-flip preparation as a coin flip of the outcomes is affine. A non-affine map is one whose output depends on the preparation in a way no coin flip explains. The number $0.141042$ is the size of that dependence at rapidity $1$.

**A third objection is that both metrics make the path a geodesic, so the metric plays no role and the article's use of it is decorative.** The answer is that the metrics disagree on the only thing that matters at the boundary: the densities. A constant density puts the pure boundary at infinity; an integrable one puts it at $\pi/4$. The third law is not a statement about which curves are geodesics but about how fast the arc length accumulates, and the two metrics disagree there by the whole of the third law.

## What Is Not Claimed

**It does not say that the boost is unphysical.** A boost is a change of frame, and as a change of frame it is exact and useful. It is not an operation on a state that an observer performs on a system, and that is a different statement.

**It does not give a master equation.** The generator $\dot{\vec s}=-\gamma\vec s$ is the simplest member of the family, chosen because it is exactly solvable and exactly checkable. A derivation of a bath's $\gamma$ and of its fixed point is outside the article.

**It does not claim that the thermal family is unique.** Any one-parameter family of states with a fixed axis has the same geometry. What the article claims is about the temperature, which is the parameter of this family, and about the two categories.

**It does not prove that no other group element acts affinely.** It proves the equivalence with $2\,\mathrm{Sc}$ and quotes the computation of $\cosh\theta_{\mathrm{rpd}}+s_{\parallel}\sinh\theta_{\mathrm{rpd}}$; the equivalence is the proof.

## Summary

**The Gibbs family is a diameter of the ball, and it is a geodesic of both metrics.** The Klein distance from the centre is $\beta\lvert\vec h_\Psi\rvert$ exactly, the Bures distance is $\tfrac12\arcsin(\tanh\beta\lvert\vec h_\Psi\rvert)$ exactly, and the path is geodesic in both. The arc-length densities are $\lvert\vec h_\Psi\rvert$ and $\tfrac12\lvert\vec h_\Psi\rvert\operatorname{sech}(\beta\lvert\vec h_\Psi\rvert)$, so the boundary is at infinity for one ruler and at $\pi/4$ for the other.

**The congruence group acts on the ball, transitively, and the action is genuine.** Composition holds to $4.3\times10^{-16}$, radii from $0.100949$ to $0.997636$ are reached from one state, and a boost along the axis translates the parameter exactly, $\beta'=\beta-\theta/\lvert\vec h_\Psi\rvert$ to $4.6\times10^{-16}$, through infinite temperature into negative temperature.

**That is why the path is not an orbit in the sense that matters.** A transitive action has one orbit, so the orbit relation says nothing; and no group element that changes the temperature is affine, so no group element that changes the temperature is a channel. The non-affinity is $0.141042$ at rapidity $1$ and $3.0\times10^{-16}$ for a rotation.

**The channel that changes the temperature is a mixture with the identity, and its fixed point is the bath.** The semigroup law is exact, the purity falls at $-2\gamma(P-\tfrac12)$ and not at zero, and the fixed point can be placed at the centre, at a pole, or at any prescribed Gibbs state. The group translates and the channel contracts; the same path, and only one of the two is an operation.

**The thermal path is the transversal to the reversible orbits, not one of them.** The unitary orbits are the spheres of constant radius, the path is a diameter, and it meets each of them once. A reversible operation stays on a sphere; a thermal change is a motion between spheres, and that is the difference the title names.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\beta$ | the inverse temperature |
| $\vec u_\Psi$ | the axis of the Hamiltonian, the direction of the Gibbs state at $\beta\to\infty$ |
| $\lvert\vec h_\Psi\rvert$ | the magnitude of the Hamiltonian; $1.7$ in the tables |
| $r=\tanh(\beta\lvert\vec h_\Psi\rvert)$ | the radius, the modulus of the state vector |
| $N=\tfrac14(1-r^{2})$ | the linear entropy |
| $\mathrm{Rp}_{\tilde U}$ | the congruence followed by normalisation |
| $\mathcal E_\lambda$ | the mixture with the identity, $\vec s\mapsto(1-\lambda)\vec s$ |
| $\gamma$ | the rate of the semigroup generator |
| $P=\tfrac12(1+r^{2})$ | the purity |
| $d_{K}$, $d_{B}$ | the Klein and Bures distances |
| $\vec s_{*}$ | the fixed point of a channel, the state of the bath |

## Further Reading

- G. Lindblad, "On the generators of quantum dynamical semigroups", *Communications in Mathematical Physics* 48 (1976) 119–130 — the generator and its complete positivity
- V. Gorini, A. Kossakowski and E. C. G. Sudarshan, "Completely positive dynamical semigroups of $N$-level systems", *Journal of Mathematical Physics* 17 (1976) 821–825 — the same theorem from the other side
- R. Alicki and K. Lendi, *Quantum Dynamical Semigroups and Applications*, Springer, 2007 — the semigroup, the fixed point and the approach to it
- H. Spohn, "Entropy production for quantum dynamical semigroups", *Journal of Mathematical Physics* 19 (1978) 1227–1230 — entropy as a monotone under the semigroup
- D. Petz, "Monotone metrics on matrix spaces", *Linear Algebra and its Applications* 244 (1996) 81–96 — the monotone family and the Bures member
- A. Uhlmann, "The 'transition probability' in the state space of a $*$-algebra", *Reports on Mathematical Physics* 9 (1976) 273–279 — the fidelity and the geodesic structure behind $d_{B}$
- *Bures Isometries of the Bloch Ball: Rotations, the Slice and the Conformal Boundary* — the polar split, $2\,\mathrm{Sc}$ as the dividing line, and the finite distance $\pi/4$ to the boundary
- *The Lorentz Group on the Bloch Ball: Projective Action and Two Metrics* — the ball as the Klein model and $2\,\mathrm{Sc}$ as the running quantity
- *States, Observables and the Born Weight* — the Gibbs state, the linear entropy and the state as a section
- *Quantum Thermodynamics in Biquaternionic Form* — the thermal family, the potentials and the Schottky heat capacity
- *Quantum Channels and the Reversible/Irreversible Dichotomy* — the Kraus decomposition and the generator
- *Equilibrium Partition Function in a Moving Frame* — the temperature a moving observer reads, and why it is $T/\gamma$ and not the parameter used here
- *Velocity Space as Hyperbolic Geometry in Biquaternionic Form* — the Klein metric, its geodesics and the boundary at infinity
