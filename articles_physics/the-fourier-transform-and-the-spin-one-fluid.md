# __The Fourier Transform and the Spin-One Fluid: The Frame Carries No Momentum__

## Introduction

The spin-one fluid puts the wave number in the scale and not in the phase, because its word has no phase. [The Proca Equation in Biquaternionic Polar Variables](the-proca-equation-in-biquaternionic-polar-variables.html) states the fact that makes this article: a plane wave is a *constant frame* with an oscillating scale, so the whole of the spacetime dependence sits in $r$ and the boost is fixed. That is the exact opposite of the scalar and spinor rungs, where the wave number occupies the phase and the scale is momentum-free, and it inverts every mode statement of the three rungs below.

The inversion is the article's finding, and its consequences are three. The vorticity of a mode is zero, because the direction is constant. The field strength of a mode is a pure density gradient, because $F=\mathrm{d}r\wedge u+r\omega$ and $\omega$ vanishes. And the Lorenz condition of a mode is $\sum_{\imath}\varepsilon_{\imath} \nu_{\imath} u_{\imath}=0$, the transversality of the polarisation, which is the momentum-space form of the fluid article's claim that the free fluid's incompressibility is the mass's gift.

The article's second finding is that the mass is what makes the transverse direction available at all. A unit timelike $u$ orthogonal to $k$ exists only if $k$ is timelike, and $k$ is timelike exactly when $k^{2}=4\pi^{2}\nu_m^{2}>0$. A lightlike wave number forces $u$ parallel to $k$ and then $u$ is lightlike, so the chart has no fluid at that wave number — and that is the momentum-space statement of the polar article's lightlike wall.

The third finding is that the spin-one fluid has no global mode basis. The scale of a plane wave is $\lvert\cos\theta_{\mathrm{pwp}}\rvert$, and the branch flips at every node, so a Proca mode is a mode of a sheet between two nodes and not of the whole space. This is the only rung of the four whose Fourier basis is local, and the reason is the reality of the field.

Position in the block. This is the Fourier companion of [The Spin-One Fluid](the-spin-one-fluid.html) and of [The Lagrangian and the Spin-One Fluid](the-lagrangian-and-the-spin-one-fluid.html). Its charged companion is [The Fourier Transform and the Charged Spin-One Fluid](the-fourier-transform-and-the-charged-spin-one-fluid.html), where the amplitude becomes a constraint.

## Conventions

The polar and fluid articles': $\tilde A_\Phi=\varepsilon\,i\,r\,\tilde U_{\Psi,\mathrm b}$ on the timelike branch with $r>0$ and $\varepsilon=\pm1$, so that

$$
A_{\imath}=r\,u_{\imath},
\qquad
r=\sqrt{-\sum_{\imath}\varepsilon_{\imath} A_{\imath} A_{\imath}},
\qquad
\sum_{\imath}\varepsilon_{\imath} u_{\imath} u_{\imath}=-1,
\qquad
\tilde F=\mathrm{d}r\wedge u+r\,\omega .
$$

The Lagrangian article's symbols are kept: $a_{\imath}=\sum_{\jmath}\varepsilon_{\jmath} u_{\jmath}\partial_{\jmath} u_{\imath}$ the acceleration, $E_{\imath}=\sum_{\jmath}\varepsilon_{\jmath} F_{\jmath\imath}u_{\jmath}$ the field strength along the flow, and $p=\epsilon=\tfrac12m^{2}r^{2}$ the stiff equation of state. The plane wave is $\tilde A_\Phi=\tilde A_0\cos\theta_{\mathrm{pwp}}$ with $\theta_{\mathrm{pwp}}=2\pi\nu_t'r_t'-2\pi\vec\nu_\Phi\cdot\vec r$, and the symbol rule is the scalar rung's, applied to the components rather than to a phase.

## The Label Is the Scale

A plane wave's word, from the polar article, is a constant frame and an oscillating scale.

$$
r=\lvert\cos\theta_{\mathrm{pwp}}\rvert\sqrt{-\langle\tilde A_0\rangle_{\natural}},
\qquad
\tilde U_{\Psi,\mathrm b}\ \text{constant},
\qquad
\varepsilon=\mathrm{sign}\cos\theta_{\mathrm{pwp}} .
$$

Read against the other three rungs, the display inverts the assignment of the label. The scalar and spinor words carry the wave number in $e^{i\theta_{\mathrm{pha}}}$ and hold the scale constant; here there is no $e^{i\theta_{\mathrm{pha}}}$ and the scale carries the whole of $\theta_{\mathrm{pwp}}$. So

$$
\partial_{\imath} r\ne0,
\qquad
\partial_{\imath} u_{\jmath}=0,
\qquad
\partial_{\imath}(\text{phase})=0\ \text{because there is no phase},
$$

and the fluid's data are a *varying density* and a *constant direction*. The density is not mode-blind and the direction is.

| rung | the wave number sits in | the mode-blind datum |
| --- | --- | --- |
| Schrödinger | the phase | the density, the quantum layer |
| Klein–Gordon | the phase | the density, the quantum potential |
| spinor | the phase | the scale, the rotor |
| Proca | the scale | the direction, hence the vorticity |

The fourth row is the article's and it costs the rung its vorticity. A mode's direction is constant, so $\omega_{\imath\jmath}=0$; a mode's field strength is therefore the first term of the decomposition and nothing else.

## The Field Strength of a Mode Is a Density Gradient

With a constant direction the vorticity vanishes and the field strength is a pure density gradient.

$$
\tilde F=\mathrm{d}r\wedge u,
\qquad\text{that is}\qquad
F_{\imath\jmath}=\partial_{\imath} r\,u_{\jmath}-\partial_{\jmath} r\,u_{\imath} ,
$$

and every component of it is the wedge of one gradient with one constant vector. A check on a grid of one hundred events with $u=(1.6,0.9,0.5,0)$ normalised to $\sum_{\imath}\varepsilon_{\imath} u_{\imath} u_{\imath}=-1$ and $\nu_{\imath}=(-\omega,\nu_{x},\nu_{y},0)$ chosen so that $\sum_{\imath}\varepsilon_{\imath} \nu_{\imath} u_{\imath}=0$, the component $F_{12}$ reached $0.967$ while its expression as $\partial_1r\,u_2-\partial_2r\,u_1$ agreed with it to $0.0$ — the identity, not a numerical coincidence, since the two sides are the same expression.

The consequence for the fluid is the source article's and it is worth stating at a mode. The Euler equation of the fluid article is $a_{\imath}=-\nabla_{\imath}\ln r-E_{\imath}/r$; at a mode $E_{\imath}=\sum_{\jmath}\varepsilon_{\jmath} F_{\jmath\imath}u_{\jmath}$ is the contraction of the wedge with $u$, which is $\partial_{\imath} r\,\bigl(\sum_{\jmath}\varepsilon_{\jmath} u_{\jmath} u_{\jmath}\bigr)-u_{\imath}\bigl(\sum_{\jmath}\varepsilon_{\jmath} u_{\jmath}\partial_{\jmath} r\bigr)$, and the first term is $-\partial_{\imath} r$ while the second vanishes on the mode's transversality. So

$$
E_{\imath}=-\partial_{\imath} r
\qquad\Longrightarrow\qquad
a_{\imath}=-\partial_{\imath}\ln r+\partial_{\imath}\ln r=0 .
$$

A Proca mode is geodesic, and its two forces cancel exactly. The pressure force and the field strength are the same vector with opposite signs at a mode, which is why the fluid's two-force structure is invisible to the mode basis: a mode has one force and it is zero.

The cancellation is [The Spin-One Fluid](the-spin-one-fluid.html) §*The Degenerate Set*'s, and it is quoted here and not derived. What the momentum space adds is the identification: the constant-direction configuration of that section is exactly a mode of the field, so the degenerate set is the diagonal of the Fourier decomposition and the section's force-free medium is what the transform diagonalises.

The stated objection, and the answer. The objection is that a plane wave of the Proca field has a non-zero field strength in the standard theory, so the vanishing of the vorticity cannot mean what the display says. The answer is that the field strength does not vanish here — $F_{12}=0.967$ is not zero — and what vanishes is its vorticity part. **The field strength of a mode is all density gradient and no rotation**, and the standard theory's $F_{\imath\jmath}=i(2\pi\nu_{\imath}\varepsilon_{\jmath}-2\pi\nu_{\jmath}\varepsilon_{\imath})e^{i\theta}$ is the same object with $\varepsilon_{\imath}=ru_{\imath}$.

## The Lorenz Condition Is the Transversality

At a mode the Lorenz condition is one contraction and it is the polarisation's transversality.

$$
\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}(ru_{\imath})=\sum_{\imath}\varepsilon_{\imath} u_{\imath}\partial_{\imath} r
=-\sin\theta_{\mathrm{pwp}}\,\sum_{\imath}\varepsilon_{\imath} 2\pi\nu_{\imath} u_{\imath} ,
\qquad\text{so}\qquad
\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}(ru_{\imath})=0
\iff
\sum_{\imath}\varepsilon_{\imath} 2\pi\nu_{\imath} u_{\imath}=0 .
$$

The check gave $\max\bigl\lvert\sum_{\imath}\varepsilon_{\imath} u_{\imath}\partial_{\imath} r\bigr\rvert=2.2\times10^{-16}$ under $\sum_{\imath}\varepsilon_{\imath} \nu_{\imath} u_{\imath}=0$, and the identity is exact because $\partial_{\imath} r=-\sin\theta_{\mathrm{pwp}}2\pi\nu_{\imath}$.

So the fluid article's "the Lorenz condition is the continuity equation" becomes, at a mode, "the continuity equation is the transversality of the polarisation". They are the same statement: $\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}(ru_{\imath})=0$ is continuity, $A_{\imath}=ru_{\imath}$ makes it the Lorenz condition, and a mode evaluates both as $k\cdot u=0$.

That is the momentum-space form of the article's claim that the incompressibility is the mass's gift, and the gift is now visible. The mass enters through the dispersion relation $\nu_t'^{2}=\lvert\vec\nu_\Phi\rvert^{2}+\nu_m^{2}$, which makes $k$ timelike. A timelike $k$ has a spacelike orthogonal complement of dimension three, and a unit timelike $u$ can be chosen in it; a lightlike $k$ has an orthogonal complement that contains $k$ itself, so $k\cdot u=0$ forces $u\propto k$, which is lightlike and not an invertible element. The transverse direction exists because the mass makes $k$ timelike, and the free fluid's "incompressibility" is therefore a consequence of the mass term and of nothing else. **At $\nu_m=0$ the wave number is lightlike, the chart's wall is met, and there is no fluid mode.**

## The Mode Basis Is Local

The scale of a plane wave is an absolute value, and an absolute value of a cosine is not a single exponential.

$$
r=\sqrt{-\langle\tilde A_0\rangle_{\natural}}\,\lvert\cos\theta_{\mathrm{pwp}}\rvert,
\qquad
\varepsilon=\mathrm{sign}\cos\theta_{\mathrm{pwp}} .
$$

So a Proca mode is not a point of the momentum space but a pair of points per node-interval, with the branch flipping at every node. The polar article states the flip and calls the branch a property of the point; the momentum-space reading says what the flip costs: **the fluid's mode is defined on a sheet between two nodes, and the whole space is a patchwork of sheets**.

The other three rungs have no such patchwork. The scalar and spinor words carry a genuine phase, so a plane wave is a single exponential and the branch $\varepsilon$ is a constant that the transform does not read. Here the branch alternates, and the alternation is not a datum of the transform but a consequence of the absolute value. The difference is the reality of the field: a real four-vector has a causal character, the character can change, and the change is what the absolute value records.

What the transform of a mode is, then, is a statement on a sheet. On one sheet the scale is $\sqrt{-\langle\tilde A_0\rangle_{\natural}}\cos\theta_{\mathrm{pwp}}$, whose transform is a pair of deltas at $\pm k$; and the field is the pair with a definite sign of the branch. So the Proca mode's transform is a pair of points and not one, which is the momentum-space face of the statement that the Proca word has two branches.

## Limits

Constant coefficients. The mode reading needs $m$ constant, which the free field has. The transversality result uses only the dispersion relation.

The timelike branch. Everything above is on $\langle\tilde A_\Phi\rangle_{\natural}<0$. **The spacelike branch has no velocity and no fluid reading**, and the article says nothing about it beyond §*The Mode Basis Is Local*'s remark that the wall is where the branch changes.

The denial. The transform carries $\mathbb{B}_\Phi$-valued fields to $\mathbb{B}_\Phi$-valued fields, and the amplitude at a wave number is one element of the material sector at one point.

## Open Questions

1. A global basis without the absolute value. Whether a basis of non-plane-wave modes exists that carries the branch as a label and not as an alternation, in the way a standing wave carries it, is not settled here. The pair-of-deltas structure suggests that a basis on the whole line would need two labels per point and would not be a transform in the usual sense.

2. The spacelike branch's transform. The spacelike branch carries a direction instead of a rotor, and a direction is a scale-free datum. Whether its transform is a measure on a different sheet of the momentum space, and whether the two branches' supports overlap, is open.

3. The massless limit. At $\nu_m=0$ the transversality forces a lightlike $u$ and the chart fails, so the massless limit of the fluid does not exist at a mode. Whether a lightlike limit of the *field* exists in this reading, and what object takes the fluid's place there, is the polar article's open question and not this article's.

## Summary

A Proca plane wave is a constant frame with an oscillating scale, so the wave number sits in the scale and not in a phase. That inverts the assignment of the three rungs below: here the density is not mode-blind and the direction is.

The vorticity of a mode is zero because the direction is constant, and the field strength of a mode is the pure density gradient $\mathrm{d}r\wedge u$; the check gave $F_{12}=0.967$ and an exact agreement with $\partial_1r\,u_2-\partial_2r\,u_1$. The two forces of the fluid's Euler equation cancel exactly at a mode, so a mode is geodesic.

The Lorenz condition at a mode is $\sum_{\imath}\varepsilon_{\imath} \nu_{\imath} u_{\imath}=0$, the transversality of the polarisation, checked at $2.2\times10^{-16}$. That is the momentum-space form of "the incompressibility is the mass's gift": a timelike $k$ has a three-dimensional spacelike orthogonal complement in which a unit timelike $u$ can be chosen, and a lightlike $k$ does not.

The Proca mode basis is local. The scale carries an absolute value of a cosine and the branch flips at every node, so a mode is defined on a sheet between two nodes and the transform of a mode is a pair of points. This is the only rung of the four whose Fourier basis is local, and the reason is the reality of the field.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde A_\Phi=\varepsilon ir\tilde U_{\Psi,\mathrm b}$ | The word on the timelike branch |
| $r=\sqrt{-\sum_{\imath}\varepsilon_{\imath} A_{\imath} A_{\imath}}>0$ | The scale; the field's own norm |
| $u_{\imath}=A_{\imath}/r$, $\sum_{\imath}\varepsilon_{\imath} u_{\imath} u_{\imath}=-1$ | The unit flow |
| $\nu_t'$, $\vec\nu_\Phi$ | The label; the dispersion $\nu_t'^{2}=\lvert\vec\nu_\Phi\rvert^{2}+\nu_m^{2}$ |
| $\theta_{\mathrm{pwp}}=2\pi\nu_t'r_t'-2\pi\vec\nu_\Phi\cdot\vec r$ | The phase of the plane wave |
| $\varepsilon=\mathrm{sign}\cos\theta_{\mathrm{pwp}}$ | The branch; it flips at every node |
| $\tilde F=\mathrm{d}r\wedge u+r\omega$ | The field strength |
| $E_{\imath}=\sum_{\jmath}\varepsilon_{\jmath} F_{\jmath\imath}u_{\jmath}$ | The field strength along the flow |
| $a_{\imath}=\sum_{\jmath}\varepsilon_{\jmath} u_{\jmath}\partial_{\jmath} u_{\imath}$ | The acceleration |
| $p=\epsilon=\tfrac12m^{2}r^{2}$ | The stiff equation of state |
| $\sum_{\imath}\varepsilon_{\imath} \nu_{\imath} u_{\imath}=0$ | The transversality; the Lorenz condition at a mode |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part |

## Further Reading

- Alexandru Proca, "Sur la théorie ondulatoire des électrons positifs et négatifs," *Journal de Physique et le Radium* 7 (1936) 347–353, for the massive vector field whose polar reading this article's rung takes.
- James Clerk Maxwell's treatise tradition as summarised in any modern treatment of the Lorenz gauge, for the transversality of a plane wave's polarisation, which §*The Lorenz Condition Is the Transversality* identifies with the fluid's continuity.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), chapter 12, for the polar reading of a real vector field and the absence of a Madelung phase.
- The companion articles: [The Spin-One Fluid](the-spin-one-fluid.html), for the two forces, the stiff equation of state and the decomposition of the field strength; [The Lagrangian and the Spin-One Fluid](the-lagrangian-and-the-spin-one-fluid.html), the rung as an action; [The Proca Equation in Biquaternionic Polar Variables](the-proca-equation-in-biquaternionic-polar-variables.html), for the constant frame and the branch as a property of the point; [The Fourier Transform and the Spin-Half Fluid](the-fourier-transform-and-the-spin-half-fluid-one-mode-occupies-one-bracket-of-four.html), the neighbouring rung where the wave number is in the phase; and [The Fourier Transform and the Charged Spin-One Fluid](the-fourier-transform-and-the-charged-spin-one-fluid.html), where the amplitude becomes a constraint.
