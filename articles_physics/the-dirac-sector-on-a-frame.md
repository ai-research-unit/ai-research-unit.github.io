# __The Dirac Sector on a Frame__

## Introduction

The Dirac field is the only matter in the corpus that sees the frame rather than only the metric, and that single fact is what makes this article the section's test of its own central claim. The preceding article showed that a source built from the metric is a symmetric rank-two object and that the frame variation of a metric-built action is symmetric by construction. The Dirac field's action is not metric-built. It contains the dual frame and a spin connection, and the third route of the dictionary therefore opens.

The question this article answers is what the frame variation produces, and the answer has a clean shape.

**The canonical stress of the Dirac field is not symmetric, and its antisymmetric part is a total divergence.** For a single plane wave the field has constant spin, the antisymmetric part vanishes, and the stress is rank one — a dust. For a superposition of two plane waves the spin varies in space–time, the antisymmetric part is nonzero, and it equals minus one half the divergence of the spin tensor to $2.2\times10^{-10}$ relative. That is the Belinfante relation, which the corpus imports with its factor and sign stated; this article confirms both.

**The consequence for the frame variation is exact in its form and conditional in its reading.** An antisymmetric part that is a total divergence carries no charge: its integral over a localised field is a boundary term. So the *charge* of the frame variation is symmetric whether or not the density is, and the torsion-free reading of the source is obtained by discarding the antisymmetric part with no loss. In the torsion reading the same part is the source of the spin connection's torsion, and its coefficient is the one the spin tensor sets.

**What is not established, and it is the sector's peculiar gap.** The spin connection is not derived from the matter action's stationarity. The corpus states this in the spin-half article in its own words: $\vec\Omega_{\imath}$ is what the polar form's fourth bracket supplies, and the equation for it is open. So the sector delivers the *form* of the frame variation — symmetric part plus a divergence of the spin — and not the connection that the antisymmetric part would source.

## Conventions

The conventions are the corpus's, and the Dirac ones are stated because the article's numbers depend on them.

The algebra and the frame are the preceding articles'. The field is a biquaternion-valued spinor $\tilde\Xi$ in the informational sector $\mathbb{B}_{\Psi}$, differentiated by the frame's operator

$$
\tilde F_{\Phi,\imath}D_{\imath}=\tilde F_{\Phi,\imath}\left(\partial_{\imath}+\vec\Gamma_{\imath}\right),
$$

with $\tilde F_{\Phi,\imath}$ the dual frame and $\vec\Gamma_{\imath}$ the spin connection valued in the six-dimensional Lie subspace. **This is the third route**: the dual frame's presence is the frame entering through the inverse metric, and $\vec\Gamma_{\imath}$'s presence is the frame entering through a connection that $g_{\imath\jmath}$ alone does not determine.

**The standard-theory conventions used for the check.** The Clifford algebra is $\{\gamma^{a},\gamma^{b}\}=2\eta^{ab}$ with $\eta=\mathrm{diag}(1,-1,-1,-1)$; a plane wave is $\psi=u\,e^{-ik\cdot x}$ with $(\slashed k-m)u=0$; the canonical stress is

$$
T_{\mathrm{can}}^{ab}=\tfrac{i}{2}\bar\psi\gamma^{a}\partial^{b}\psi-\tfrac{i}{2}\left(\partial^{b}\bar\psi\right)\gamma^{a}\psi,
$$

and the spin tensor and its generator are

$$
S^{cab}=\bar\psi\,\gamma^{c}\,\Sigma^{ab}\,\psi,
\qquad
\Sigma^{ab}=\tfrac{i}{2}\left[\gamma^{a},\gamma^{b}\right].
$$

The Belinfante relation asserted by the corpus is

$$
T_{\mathrm{can}}^{[ab]}=-\tfrac12\,\partial_{c}S^{cab},
$$

with the factor $\tfrac12$ and the minus sign, quoted from the standard treatment. The only thing this article adds to it is the verification.

## The Frame Variation of a Spinor Action

**The action.** The Dirac action on a frame is

$$
S_{\mathrm{D}}[\tilde\Xi;\tilde E_{\Phi}]=\int d^{4}x\,\sqrt{|g|}\;\bar{\tilde\Xi}\left(\tilde F_{\Phi,\imath}D_{\imath}-m\right)\tilde\Xi,
$$

and its dependence on the frame is of three kinds at once.

*Through the measure*, $\sqrt{|g|}$, as for every field.

*Through the dual frame*, $\tilde F_{\Phi,\imath}=G_{\imath\jmath}\tilde E_{\Phi,\jmath}$, which is the metric entering a first-order operator. This part of the variation is a function of $g$ and produces a symmetric contribution, exactly as in the scalar sector.

*Through the connection*, $\vec\Gamma_{\imath}$, which is not a function of $g$ alone. Local Lorentz invariance fixes the *form* of the connection's transformation but not the connection: any $\vec\Gamma$ differing by a $g$-compatible contortion gives the same $g$ and a different action. This is the route that can produce an antisymmetric frame variation, and it is the reason this sector is the one that tests the claim.

**The general shape of the result.** Write the variation as

$$
\frac{\delta S_{\mathrm{D}}}{\delta E_{\imath a}}=\sqrt{|g|}\left[\Theta^{(\mathrm{sym})}_{\imath\jmath}+\Xi_{\imath\jmath}\right](E\digamma_{\mathrm{met}})_{\jmath a},
$$

with $\Theta^{(\mathrm{sym})}$ symmetric and $\Xi$ antisymmetric. Then the dictionary of the first article applies to the symmetric part unchanged, and $\Xi$ is a genuinely new term: it is the part of the frame derivative that six of the sixteen frame directions do not see, and it is what a torsion equation would balance.

**Why the antisymmetric part cannot be dropped by an argument from the count.** It is six numbers at a point and it is not the six-dimensional redundancy. The redundancy is the *kernel* of the frame-to-metric map; $\Xi$ is a nonzero value of the derivative in directions the redundancy does not span. The two sevens are different: one is a kernel, the other is a value. Conflating them is the mistake the first article warns against, and this sector is where the confusion would be fatal.

## The Antisymmetric Part Is a Divergence

**The statement.** For the Dirac field the antisymmetric part of the canonical stress is not an independent object. It is a total divergence, and the corpus's Belinfante relation states which:

$$
T_{\mathrm{can}}^{[ab]}=-\tfrac12\,\partial_{c}S^{cab}.
$$

**The verification.** Two plane waves with momenta $k_1=(2.104,\,1.2,\,0.8,\,0.6)$ and $k_2=(1.700,\,-0.4,\,1.0,\,0.9)$, on shell for $m=1$, with random normalised positive-energy spinors, were superposed and the canonical stress computed at the origin:

| quantity | value |
| --- | --- |
| largest entry of $T_{\mathrm{can}}-T_{\mathrm{can}}^{\mathsf T}$, one plane wave | $4.4\times10^{-16}$ |
| largest entry of $T_{\mathrm{can}}-T_{\mathrm{can}}^{\mathsf T}$, two plane waves | $0.812$ |
| relative error of $T_{\mathrm{can}}^{[ab]}=-\tfrac12\partial_{c}S^{cab}$, two plane waves | $2.2\times10^{-10}$ |

The first row is the corpus's "one mode is a dust" and it is exact: a single plane wave's canonical stress is symmetric, so the field of constant spin has no antisymmetric part. The second row is the same statement contrapositively: two waves with different momenta have a spin density that varies in space, and the antisymmetric part appears. The third row is the relation itself, with the corpus's factor and sign, confirmed to ten digits.

**The two consequences, and they must be separated.**

*Conserved charge.* A total divergence integrates to a boundary term, which vanishes for a localised field. So $\int d^{3}x\,\Xi_{0\imath}=0$, and the antisymmetric part contributes nothing to the total energy–momentum. This is why the symmetric part is the conserved density and the antisymmetric part is not, and it is the statement the corpus makes in *The Spin-Half Energy-Momentum Tensor*.

*Local density.* At a point the antisymmetric part is as real as the symmetric one. It is not measurable as a charge, but it is the source that a torsion equation would have, and it does not vanish except for constant spin.

That division is the sector's contribution to the section: **the frame variation's antisymmetric part exists, is a divergence, carries no charge, and is nevertheless the local source of torsion.**

## The Spin Tensor, the Frenkel Condition and the Torque

The corpus carries the spin tensor as twenty-four components cut to twelve by the Frenkel condition, and it carries the torque as a commutator. This article quotes those results rather than re-deriving them, and records how they sit against the frame variation.

**The count.** $S_{k\imath\jmath}$ is antisymmetric in its last two indices, so $4\times6=24$ components; the Frenkel condition $S_{k\imath\jmath}u^{\imath}=0$ removes twelve; the remaining twelve are the spin density and its flux. Equivalently, $\Sigma^{ab}$ has six independent entries and $\gamma^{c}$ four, so the bilinear $\bar\psi\gamma^{c}\Sigma^{ab}\psi$ spans at most twenty-four, and the corpus's point is that one algebra element — eight real dimensions — holds only the density slice.

**The Frenkel condition on a frame.** It is the vanishing of the scalar part of the spin current along the flow, and *Spin Conservation and the Frenkel Condition* derives it as exactly that. On a frame it is a condition on the dual frame's contraction with the spin current, so it inherits the frame's six-dimensional redundancy in the same way the source does.

**The torque.** *The Spin-Half Energy-Momentum Tensor* records the spin law as

$$
\sum_{\imath\in\{x,y,z\}}\partial_{\imath}S_{\Psi,k,k\jmath}=\tau_{k\jmath},
\qquad
\tau_{k\jmath}=\tfrac12\left(\sum_{\rho}\varepsilon_{\rho}\Omega_{k\rho}S_{\rho\jmath}-\sum_{\rho}\varepsilon_{\rho}\Omega_{\jmath\rho}S_{\rho k}\right),
$$

with $\vec\Omega_{\imath}$ the rotor connection's logarithmic derivative. Its kernel is the connection along the spin: for a rotor turning about the spin axis the torque vanishes, and for any other axis it does not. The corpus records the check numerically — maximum torque $0$ for $\vec\Omega_0=(0,0,2)$ with the spin along $\vec e_z$, $0.5$ for $\vec\Omega_0=(1,0,0)$, $0.5$ for $(1,0,1)$.

**The link to the frame variation.** The torque is the antisymmetric object that *balances* the divergence of the spin current, and the frame variation's antisymmetric part is the same object read from the other side: the matter action's dependence on the connection produces $\Xi_{\imath\jmath}$, the spin law says its divergence is a commutator with $\vec\Omega$, and the two are the two halves of the torsion equation. In the torsion-free reading $\Xi$ is dropped and the spin law decouples; in the torsion reading the two are one equation.

## What the Sector Establishes and What It Leaves

**Established.**

1. The Dirac action on a frame depends on it in three ways — measure, dual frame, connection — and only the third can produce an antisymmetric frame variation.
2. The antisymmetric part of the canonical stress is a divergence: $T_{\mathrm{can}}^{[ab]}=-\tfrac12\partial_{c}S^{cab}$ verified to $2.2\times10^{-10}$, with the corpus's factor and sign.
3. It vanishes for constant spin (one plane wave, $4.4\times10^{-16}$) and is $0.812$ for a two-wave superposition: the spin variation is what creates it.
4. It carries no charge, being a total divergence, and it is nevertheless a local density and the torsion source.

**Left open.**

1. **The connection.** $\vec\Gamma_{\imath}$, equivalently $\vec\Omega_{\imath}$, is not determined by the matter action's stationarity. The corpus says so and the statement is not weakened here: the sector gives the form of $\Xi$ and not the equation its divergence obeys.
2. **The coefficient.** Whether the torsional coupling of the corpus's spin tensor reproduces $\Xi$ with a coefficient fixed by the Dirac action's own normalisation is not computed here. That is the quantitative half of the torsion route, and it needs the connection first.
3. **The gravitational side.** As everywhere in this section, the first term of the stationary condition is absent.

## Summary

The Dirac field is the sector that sees the frame and not only the metric, and its frame variation therefore has two parts. The symmetric part is the energy–momentum tensor and behaves exactly as the preceding articles' dictionary says. The antisymmetric part is new, exists exactly when the spin varies, and equals minus one half the divergence of the spin tensor — verified to $2.2\times10^{-10}$ with the corpus's factor and sign.

Because it is a divergence it carries no charge, which is why the conserved object is symmetric; because it is a divergence it is also the local source that a torsion equation would balance, which is why it cannot simply be declared absent. One plane wave has constant spin and no antisymmetric part — its stress is a dust, symmetric to $4.4\times10^{-16}$, rank one along the momentum. Two plane waves have $0.812$ of antisymmetry.

The sector's gap is the connection. The form of the antisymmetric part is computed; the equation that determines $\vec\Gamma_{\imath}$ is not, and the corpus names it as open. So this article closes the question "can the frame variation be antisymmetric, and what would it mean" and leaves open "what fixes the connection that makes it so".

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\tilde\Xi$ | biquaternion-valued spinor, informational sector |
| $\tilde F_{\Phi,\imath}D_{\imath}$ | frame's first-order operator, dual frame times covariant derivative |
| $\vec\Gamma_{\imath},\ \vec\Omega_{\imath}$ | spin connection and rotor logarithmic derivative |
| $T_{\mathrm{can}}^{ab}$ | canonical energy–momentum tensor |
| $S^{cab}=\bar\psi\gamma^{c}\Sigma^{ab}\psi$ | spin current |
| $\Sigma^{ab}=\tfrac{i}{2}[\gamma^{a},\gamma^{b}]$ | Lorentz generator |
| $\Theta^{(\mathrm{sym})},\ \Xi$ | symmetric and antisymmetric parts of the frame variation |
| $S_{k\imath\jmath}$ | the corpus's spin tensor, twenty-four components, twelve after Frenkel |

## Further Reading

- [The Spin-Half Energy-Momentum Tensor](the-spin-half-energy-momentum-tensor.html), for the symmetric and antisymmetric parts, the Belinfante relation as imported, the count sixteen against eight, and the torque's kernel.
- [Spin Conservation and the Frenkel Condition](spin-conservation-and-the-frenkel-condition.html), for the derivation of the spin law and the Frenkel condition as the vanishing of a scalar part.
- [Torsion, Contorsion and the Spin Connection in Biquaternionic Form](torsion-contorsion-and-the-spin-connection-in-biquaternionic-form.html), for the torsion side of the equation this article's antisymmetric part would source.
- [Matter Into the Frame: The Variation That Defines the Source](matter-into-the-frame-the-variation-that-defines-the-source.html), for the dictionary, the six directions that carry nothing, and the distinction between a kernel and a value.
- [The Maxwell Sector on a Frame](the-maxwell-sector-on-a-frame.html), for the sector where the algebraic packaging fails and the metric formula is needed.
- [Conservation as a Consequence](conservation-as-a-consequence.html), for the divergence statements this sector's antisymmetric part obeys.
