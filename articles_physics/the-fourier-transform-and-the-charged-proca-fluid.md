# __The Fourier Transform and the Charged Proca Fluid: The Constraint Is the Amplitude__

## Introduction

**The coupled Proca constraint is the only constraint in the block that is nonlinear in the momentum space.** Its covariant half is a multiplier: $\mathrm{Sc}(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A)=0$ transforms to a linear condition on the amplitude at each label. Its ordinary half is not: the constraint fixes the multiplier $\mathrm{Sc}(\tilde\nabla^{\natural}\tilde A)$ to equal $-\frac{iϙ}{\hbar}\langle\tilde A\rangle_\natural$, a product, and a product transforms to a **correlation** of the amplitude with its own conjugate. **So the constraint equates a label-local expression to a label-delocal one**, and that asymmetry is the article's finding.

**The immediate consequence is that the constraint cannot be solved label by label.** Every other constraint in the block — the Lorenz condition of the free vector fluid, the mass shell of the scalar, the transversality of a polarisation — is a condition on the amplitude at one point of the momentum space, and it determines that amplitude there. This one is one scalar equation per label whose right-hand side is an integral over all labels. No change of basis removes the correlation, because a correlation is the multiplication in the position variable and the multiplication is the physical product of two field values.

**The second finding is that the free fluid's incompressibility is the statement that the constraint is label-local.** At $ϙ=0$ the right-hand side vanishes identically and the constraint becomes a multiplier on both sides; **the mass's gift is therefore a locality in the momentum space**, which is the sharpest form the fluid article's sentence can take.

**The third finding is that the mode basis of the charged Proca fluid is a basis of the chart and not of the field.** The chart's scale is an amplitude and not the field's norm, because $\tilde A\tilde A^{\natural}=r^{2}e^{2i\vartheta_{\mathrm{pha}}}$ is complex and the invariant $\mathrm{Sc}(\tilde A^{*}\tilde A^{\natural})$ is $r^{2}$ only where the rotor is trivial. **An amplitude at a label is therefore a coordinate**, and the transform's support is a property of the description.

**Position in the block.** This is the charged companion of [The Fourier Transform and the Proca Fluid](the-fourier-transform-and-the-proca-fluid.html) and the Fourier companion of [The Charged Proca Fluid: Three Currents and a Compressibility](the-charged-proca-fluid.html). It closes the eight Fourier articles of the fluid block.

## Conventions

The charged Proca fluid's: $\tilde A=r\,e^{i\vartheta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ with $r>0$, eight real parameters for the eight real components, the coupling $ϙ$, and

$$
\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{iϙ}{\hbar}\tilde A_\Phi ,
\qquad
\tilde F=\tfrac12\bigl(\tilde\nabla^{\natural}_{\mathrm{gco}}\tilde A-\tilde\nabla_{\mathrm{gco}}\tilde A\bigr)_{V},
\qquad
\tilde\nabla_{\mathrm{gco}}\tilde F=k_m^{2}\tilde A .
$$

The transform carries a subscript and no accent, as the series requires: the transform of a glyph is written with $\mathrm{trf}$, so the amplitude is $\tilde A_{\mathrm{trf}}(\tilde K_\Phi)$ and its correlation with its conjugate is $\tilde A_{\mathrm{trf}}*\tilde A_{\mathrm{trf}}^{\natural}$. The field itself is $\tilde A$.

The symbol rule is the scalar rung's, and the product rule is the one proved in [The Fourier Transform and the Coupled Dirac Equation in Biquaternionic Polar Variables](the-fourier-transform-and-the-coupled-dirac-equation-in-biquaternionic-polar-variables.html): a product in the position variable transforms to a convolution of the two transforms, with the residual there measured at $1.4\times10^{-15}$.

## The Two Halves of the Constraint, and Their Two Shapes

**The trace of the coupled equation forces the covariant condition, exactly and blindly to the frame, and the ordinary divergence is then the amplitude.**

$$
\mathrm{Sc}\bigl(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A\bigr)=0
\qquad\Longrightarrow\qquad
\mathrm{Sc}\bigl(\tilde\nabla^{\natural}\tilde A\bigr)
=-\frac{iϙ}{\hbar}\langle\tilde A\rangle_{\natural}
=-\frac{iϙ}{\hbar}\,r^{2}e^{2i\vartheta_{\mathrm{pha}}} .
$$

**Transform the two sides and they have different shapes.**

$$
\underbrace{\tilde K_\Phi\cdot\tilde A_{\mathrm{trf}}(\tilde K_\Phi)}_{\text{a multiplier, label-local}}
\qquad\text{equals}\qquad
\underbrace{-\frac{iϙ}{\hbar}\bigl(\tilde A_{\mathrm{trf}}*\tilde A_{\mathrm{trf}}^{\natural}\bigr)(\tilde K_\Phi)}_{\text{a correlation, label-delocal}} .
$$

The left side is a linear operator applied pointwise, so it constrains this component of the amplitude at this label. The right side is a quadratic functional of the whole measure, so it is an integral over every label at once. **The constraint is therefore one scalar equation per label whose right-hand side is not a datum of that label**, and no diagonalisation of the field changes that, because the correlation is the multiplication in the position variable and the multiplication is the physical product of two field values.

**The stated objection, and the answer.** The objection is that the right-hand side is $r^{2}e^{2i\vartheta}$, so it is a known function once the field is known, and one may impose the constraint by iteration rather than by correlation. The answer is that this is exactly the statement that the constraint is not label-local: an iteration over the whole measure is what a correlation is, and the number of iterations is the number of terms in the expansion of the exponential. **A label-local constraint needs one pass; this one needs the measure.**

**The quantities are the parent's and the shapes are the article's.** The parent proves both displays and reads them as a constraint and a compressibility; this article's contribution is that the two are not the same *kind* of statement, and that the momentum space is where the difference is visible.

## The Free Case Is a Locality in the Momentum Space

**At $ϙ=0$ the right-hand side of the ordinary divergence vanishes identically, so the constraint becomes a multiplier on both sides.**

$$
ϙ=0:\qquad
\mathrm{Sc}\bigl(\tilde\nabla^{\natural}\tilde A\bigr)=0
\qquad\Longleftrightarrow\qquad
\tilde K_\Phi\cdot\tilde A_{\mathrm{trf}}(\tilde K_\Phi)=0\ \text{at each label}.
$$

**The free companion's finding is the same statement and this display is its sharpest form.** There the Lorenz condition of a mode is $k_\mu u^\mu=0$, the transversality of the polarisation, checked at $2.2\times10^{-16}$; here the same condition is read as a locality. **The free fluid's incompressibility is therefore not a physical property of a medium but a property of the constraint's symbol**: the divergence is a multiplier, a multiplier is diagonal in the label, and a diagonal condition is one condition per label.

**With the coupling the symbol is no longer diagonal, and the fluid acquires the compressibility the parent names.** The parent says the free incompressibility was the mass's gift and is the $ϙ=0$ case. This article says what the gift is: **the mass is what makes the constraint's right-hand side vanish at $ϙ=0$, and a vanishing right-hand side is a diagonal condition.** A nonzero right-hand side is a product, and a product is a convolution.

**That is also the momentum-space reading of the parent's "three currents".** A conservation law is the vanishing of a divergence, and in the momentum space a divergence is the component along the label; so conservation is a statement about one component of a measure at each label, and it is diagonal. **The constraint's ordinary half is not diagonal and the charge's conservation is**, which is why the parent finds three currents and only one conserved.

## The Amplitude Is a Coordinate

**The chart's scale is not the field's norm, and the momentum space shows what that costs.**

$$
\tilde A\tilde A^{\natural}=r^{2}e^{2i\vartheta_{\mathrm{pha}}},
\qquad
\mathrm{Sc}\bigl(\tilde A^{*}\tilde A^{\natural}\bigr)=r^{2}\ \text{only where the rotor is trivial}.
$$

**So the amplitude at a label is a coordinate of the chart and not an observable.** The rotor is a real datum of the chart with no invariant that reads it, and a change of the chart's normalisation moves $r$ while leaving the field alone. **The mode basis of the charged Proca fluid is therefore a basis of the description and not of the field**, and that is the last rung's answer to the question the block has asked at each of the four: *what does the transform see?*

| rung | what the amplitude at a label is | does the transform see the field |
| --- | --- | --- |
| Schrödinger | the field's own modulus | yes |
| Klein–Gordon | the field's own modulus | yes |
| spinor | the carrier's element | yes, up to the phase |
| vector, free | the field's own norm | yes |
| vector, charged | a chart coordinate | no |

**The last row is the only "no" in the table, and it is the coupling's doing.** The free vector fluid's scale is $\sqrt{-A_\mu A^\mu}$, an invariant; the charged one's is an amplitude whose square is the modulus of a complex number times a phase. **The reality of the field was what made the scale an observable, and the phase that the coupling introduces is what stops it being one.**

**What survives is the response and the direction.** The response $m^{2}\tilde A$ has the field's own support, and the direction $\tilde A/r$ is the field's up to the chart's normalisation. **So the mode basis sees the response and cannot see which current is conserved**, which is the previous section's statement in the language of the three currents, and the two sections are one.

## What the Eight Articles Have in Common

**Each of the eight rungs asks one question — what does the Fourier decomposition see of the fluid — and each answers it with a single object that the decomposition cannot see.**

| rung | the one object the mode basis cannot carry |
| --- | --- |
| Schrödinger | the quantum potential, which is a cross term |
| charged Schrödinger | the curvature $\vec B$ |
| Klein–Gordon | the defect of the velocity's norm, which is $Q_{\mathrm{qnt}}$ |
| charged Klein–Gordon | the curvature $\tilde F$ |
| spinor | the vorticity and the spin precession |
| charged spinor | the rotor's response to the connection |
| vector, free | the vorticity, because the direction is constant |
| vector, charged | the constraint's quadratic half |

**The eight answers are one pattern in four settings.** The scalar rung's object is a cross term, the spinor rung's is a frame's gradient, the vector rung's is the direction's, and the charged rungs' are the connection's curvature. **So the invisible object is always either a product of two modes or a derivative of a structure that a mode holds constant**, and the two descriptions coincide because a product of two modes is what a derivative of a constant structure produces.

**The pattern's value is diagnostic.** A reader who wants to know whether a statement about a fluid is a statement about the field or about its mode basis has one test: **ask whether the object can be built from one label.** If it can, it is diagonal and the mode basis sees it; if it cannot, it is off-diagonal and the statement is about a pair, a neighbourhood or a curvature.

## Limits

**Constant coefficients.** The multiplier reading of the covariant half needs $\tilde A_\Phi$ to be constant, which the article assumes where it speaks of labels. The correlation on the right-hand side holds for every profile, since the product rule is general.

**The chart.** The word has eight parameters for eight components and its domain excludes $r=0$ only. Nothing above needs the domain further.

**The denial.** The transform carries $\mathbb{B}_\Phi$-valued fields to $\mathbb{B}_\Phi$-valued fields, and the amplitude at a label is one element of the material sector. No step carries the field out of its sector.

## Open Questions

1. **Whether the constraint can be solved by a transform of its own.** A constraint that is a multiplier on one side and a correlation on the other is a nonlinear equation for the measure. Whether some other transform — a logarithm, a scattering transform, a division by the amplitude — makes it linear is not known to the author, and it is the natural next question for this rung.

2. **The rotor's invisibility.** The chart has a rotor and no invariant reads it. Whether the rotor is a gauge freedom of the description, in the sense in which a redundant parameter is, or a physical datum that the invariants happen to miss, is not settled by the parent and is not settled here.

3. **The number of currents at a label.** The parent finds three currents and one conservation. Whether the other two have a momentum-space face at all, or whether they are exactly the ones the mode basis cannot see, is the question the last two sections circle and do not close.

## Summary

The coupled Proca constraint has two halves with different shapes in the momentum space. The covariant half is a multiplier, a linear condition at each label. The ordinary half fixes its own multiplier to a product, so the right-hand side is a correlation of the amplitude with its own conjugate. **This is the only constraint in the block that cannot be solved label by label.**

At $ϙ=0$ the right-hand side vanishes and the constraint becomes a multiplier on both sides, so the free fluid's incompressibility is a locality in the momentum space. The mass is what makes the right-hand side vanish, and a vanishing right-hand side is a diagonal condition; that is the sharpest form of the fluid article's claim that the incompressibility was the mass's gift.

The chart's scale is not the field's norm, because $\tilde A\tilde A^{\natural}=r^{2}e^{2i\vartheta_{\mathrm{pha}}}$ is complex. An amplitude at a label is therefore a coordinate, and the mode basis of this fluid is a basis of the description and not of the field — the only rung of the five in which the transform does not see the field.

What survives is the response $m^{2}\tilde A$, whose support is the field's, and the direction $\tilde A/r$. Conservation is the vanishing of a divergence, hence a diagonal statement, so the mode basis sees the response and cannot see which current is conserved.

Across the eight Fourier articles the invisible object is always either a product of two modes or a derivative of a structure a mode holds constant. **The test is one line: an object that can be built from a single label is visible to the transform, and an object that cannot is not.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $ϙ$ | The coupling |
| $\tilde A=r\,e^{i\vartheta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The eight-parameter word |
| $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+iϙ\tilde A_\Phi/\hbar$ | The covariant derivative |
| $\tilde F$ | The field strength, built from covariant gradients |
| $k_m=mc/\hbar$ | The mass wave number |
| $\mathrm{Sc}(\tilde\nabla^{\natural}\tilde A)=-(iϙ/\hbar)r^{2}e^{2i\vartheta_{\mathrm{pha}}}$ | The ordinary divergence; the amplitude |
| $\mathrm{Sc}(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A)=0$ | The covariant constraint; a multiplier |
| $\tilde K_\Phi$ | The label, the transform's variable |
| $\tilde A_{\mathrm{trf}}(\tilde K_\Phi)$ | The amplitude at a label, with no hat on the transform |
| $\langle\tilde A\rangle_\natural=\tilde A\tilde A^{\natural}$ | The natural norm; equal to $r^{2}$ only on the real slice |
| $\tilde A_{\mathrm{trf}}*\tilde A_{\mathrm{trf}}^{\natural}$ | The correlation of the amplitude with its own conjugate |
| $m^{2}\tilde A$, $\tilde A/r$, and the charge bilinear | The three currents |
| $r=\lvert\tilde A\rvert$ in the chart | A coordinate, not the field's norm |
| $\lambda=\exp(iϙ\Gamma/\hbar)$ | The gauge element |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part |

## Further Reading

- Alexandru Proca, "Sur la théorie ondulatoire des électrons positifs et négatifs," *Journal de Physique et le Radium* **7** (1936) 347–353, for the equation and the constraint.
- Fritz London, "On the problem of the molecular interpretation of the persistent current," *Physical Review* **54** (1938) 947–954, for the London response $J\propto A$ that the parent identifies with the mass term.
- Jan Łopuszański, "On the correspondence between the Proca and the Maxwell fields," *Acta Physica Polonica* **9** (1948) 205–218, for the massless limit and the constraint's behaviour in it.
- The companion articles: [The Charged Proca Fluid: Three Currents and a Compressibility](the-charged-proca-fluid.html), for the two displays this article transforms; [The Fourier Transform and the Proca Fluid](the-fourier-transform-and-the-proca-fluid.html), the free rung's transversality; [The Fourier Transform and the Coupled Dirac Equation in Biquaternionic Polar Variables](the-fourier-transform-and-the-coupled-dirac-equation-in-biquaternionic-polar-variables.html), for the product rule and the mode count; and the free companion [The Fourier Transform and the Dirac Equation in Biquaternionic Polar Variables](the-fourier-transform-and-the-dirac-equation-in-biquaternionic-polar-variables.html), for the four brackets the block's diagnostics are built on.
