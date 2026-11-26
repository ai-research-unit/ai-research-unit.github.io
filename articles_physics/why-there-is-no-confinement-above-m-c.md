# __Why There Is No Confinement Above $M_C$__

## Introduction

**The question.** $\mathrm{SU}(4)$ is asymptotically free. Asymptotic freedom is usually paired with confinement in the infrared. **So why does the primordial force not confine?**

**The short answer.** Because confinement needs the coupling to reach order one *inside a phase that exists*, and the primordial phase ends long before its coupling gets there. **At $M_C$ the coupling is $0.058$; it would reach order one only at about $1.8\ \mathrm{GeV}$, which is five decades below the transition and in a theory where $\mathrm{SU}(4)$ is not a symmetry at all.**

**The two conditions, stated separately, because the literature usually runs them together.**

| condition | statement | holds here? |
| --- | --- | --- |
| the coupling reaches order one | $1/\alpha_4(\mu)\sim1$ for some $\mu$ in the phase | **no**: it needs $\mu\approx1.8\ \mathrm{GeV}$ |
| the phase exists at that scale | $\mu>M_C$ | **no**: $M_C\gtrsim250\ \mathrm{TeV}$ |

**Either failure alone is enough, and both fail.** This article computes the first and cites the leptoquark bound for the second.

**What the article does not claim.** It does not prove that no confining phase exists anywhere. **It proves that the one-loop coupling of this content does not become strong inside the phase the model describes**, which is a narrower and checkable statement.

## Asymptotic Freedom Is Not the Argument

**A positive coefficient says the coupling falls as the scale rises; read downwards it says the coupling grows.**

$$
\frac{1}{\alpha_4(\mu)}=\frac{1}{\alpha_4(M_X)}+\frac{b_0}{2\pi}\ln\frac{\mu}{M_X},
\qquad
b_0=\frac{26}{3},
\qquad
\frac{b_0}{2\pi}=1.379 .
$$

**Because $b_0>0$, $\alpha_4$ increases as $\mu$ decreases**, exactly as $\alpha_s$ does in QCD. **So asymptotic freedom is not an argument against confinement; it is the premise of confinement.** The argument must be quantitative, and it is the next section.

**What would make confinement automatic.** A theory with $b_0<0$ — too much matter — has a coupling that grows in the ultraviolet and is free in the infrared; it confines nowhere. **This model is not of that kind**, and it is worth saying because the phrase "asymptotically free" is sometimes used as if it settled the infrared question. It does not.

## The Coupling Never Gets There

**From the matching value, downwards.**

| scale | $1/\alpha_4$ | $\alpha_4$ |
| --- | --- | --- |
| $M_X=2.33\times10^{5}\ \mathrm{GeV}$ | $17.21$ | $0.058$ |
| $M_C=2.5\times10^{5}\ \mathrm{GeV}$ | $17.31$ | $0.058$ |
| $1.83\ \mathrm{GeV}$, where $\alpha_4=1$ | $1.00$ | $1.00$ |
| $885\ \mathrm{MeV}$, the one-loop pole | $0$ | $\infty$ |

**The third row is computed and not fitted.**

$$
\ln\frac{\mu_{1}}{\mu_{0}}=-\frac{1/\alpha_4(\mu_{0})-1}{b_0/2\pi}
=-\frac{17.21-1}{1.379}=-11.76 ,
\qquad
\mu_{1}=2.33\times10^{5}\times e^{-11.76}=1.8\ \mathrm{GeV} .
$$

**Nearly twelve e-folds, or a factor $1.4\times10^{5}$ in scale, separate the transition from the scale at which the coupling would be strong.** The transition is at $250\ \mathrm{TeV}$ and the strong-coupling scale is at $1.8\ \mathrm{GeV}$; the ratio is $1.4\times10^{5}$.

**And below the transition the line is not the theory's line.** The coefficient becomes the Standard Model's, the group becomes $\mathrm{SU}(3)\times\mathrm{U}(1)$, and the running that would produce a strong $\mathrm{SU}(4)$ coupling is not the running the world follows. **Inside the phase, $\alpha_4$ never exceeds $0.058$.**

**The comparison with QCD, computed the same way.**

$$
\frac{1}{\alpha_s(M_Z)}=\frac{1}{0.1179}=8.48,
\qquad
\frac{b_0^{\mathrm{QCD}}}{2\pi}=\frac{7}{2\pi}=1.114,
\qquad
\ln\frac{M_Z}{\Lambda}= -\frac{8.48-1}{1.114}=-6.71 ,
$$

so QCD's coupling reaches order one at $91.2\times e^{-6.71}=0.111\ \mathrm{GeV}$, **which is the familiar order of $\Lambda_{\mathrm{QCD}}$ and is seven e-folds from the $Z$ mass.** The primordial coupling starts weaker ($1/\alpha=17.2$ against $8.5$), and that head start is what buys the extra e-folds: it needs $11.8$ against $6.7$. **The factor is $1.8$, and most of it is the starting value**, since the two coefficients differ by about a quarter.

## What Confinement Would Require

**Three statements, and each is a requirement rather than a description.**

- *A string tension.* Confinement is the statement that the potential between two static charges rises linearly, $\sigma r$, with $\sigma$ of order $\Lambda^{2}$. **That needs $\Lambda$ inside the phase**, and here $\Lambda$ would be $1.8\ \mathrm{GeV}$.
- *A spectrum of bound states.* Glueballs and colour-singlet composites need the theory to exist at the scale where they form. **At $1.8\ \mathrm{GeV}$ the relevant theory is the Standard Model's strong sector**, whose own bound states are the hadrons.
- *A phase transition, or none.* QCD confines without a transition; the primordial theory would have to confine across one, and it does not reach the scale.

**What replaces confinement above $M_C$ is a weakly coupled plasma of the model's own content.** Fifteen massless vectors, thirty-two fermion states, sixteen scalars, all perturbative, with $\alpha_4/\pi=0.018$ at the transition. **The tree-level rates of the block are legitimate for exactly this reason**, and [The Primordial Coupling](the-primordial-coupling-g4-as-a-boundary-condition-and-what-runs-above-m-c.html) supplies the number.

## The Analogy That Fails, and Why It Is Worth Stating

**The strong sector's story has three steps: asymptotic freedom, growth in the infrared, confinement.** The primordial sector has the first and the second and not the third, because the third happens in a phase that does not extend far enough.

**A reader who transfers the QCD story wholesale will get the leptoquark spectrum wrong.** In QCD the lightest degrees of freedom at $100\ \mathrm{MeV}$ are pions; here there is no analogous scale, because the only scale is $M_C$ and it is six decades away. **The correct statement about the primordial sector's infrared is that it has none**: the phase's infrared limit is $M_C$, and at $M_C$ the description changes rather than the coupling.

**And the direction of the change matters.** At $M_C$ the group breaks, six vectors become heavy, and the coupling is matched to the Standard Model's. **The theory does not become strong; it becomes a different theory**, and the matching is where the primordial coupling's career ends.

## What This Does Not Prove

**Three boundaries, stated so the claim stays narrow.**

- *It is a one-loop statement.* $\alpha_4(M_C)=0.058$ is a one-loop value; a two-loop coefficient would move it by a few per cent and would not move the strong-coupling scale by five decades. **The conclusion is robust to the truncation in a way the numbers are not.**
- *It says nothing about a different content.* A model with twice as many scalars would have a smaller $b_0$ and a nearer strong-coupling scale; **the count of scalars is what decides the margin**, and [The Scalar Content](the-scalar-content-one-matrix-and-ten-survivors.html) is where that count is fixed.
- *It says nothing about non-perturbative effects at $M_C$.* Instantons and monopoles can be important without confinement; **the instanton action is computed in $M_C$ and is enormous**, which is a separate statement.

## The Checks

| claim | check | result |
| --- | --- | --- |
| $b_0$ positive | $\tfrac{44}{3}-\tfrac{16}{3}-\tfrac23$ | $+\tfrac{26}{3}$ |
| the direction | positive coefficient | $\alpha_4$ grows downward |
| $\alpha_4(M_C)$ at $250\ \mathrm{TeV}$ | $17.21+1.379\ln(2.5/2.33)$ | $0.058$ |
| the strong-coupling scale | $M_Xe^{-(17.21-1)/1.379}$ | $1.8\ \mathrm{GeV}$ |
| the e-folds from $M_C$ | $16.31/1.379$ | $11.8$ |
| the scale ratio | $2.5\times10^{5}/1.8$ | $1.4\times10^{5}$ |
| QCD's e-folds | $(8.48-1)/1.114$ | $6.7$ |
| QCD's strong scale | $91.2\,e^{-6.71}$ | $0.111\ \mathrm{GeV}$ |
| the ratio of e-folds | $11.8/6.7$ | $1.8$ |

**The last two rows are the comparison and not a proof.** They show that the same calculation gives the familiar answer in the familiar theory, which is what makes the primordial answer credible.

## Summary

**The primordial force does not confine, and asymptotic freedom is not the reason.** $b_0>0$ means the coupling grows downward, exactly as in QCD; what differs is the distance it has to travel.

**$11.8$ e-folds separate the transition from the scale where $\alpha_4$ would be one, and QCD needs $6.7$ from the $Z$ mass.** The primordial coupling starts weaker and holds that advantage all the way down, which puts its strong-coupling scale at $1.8\ \mathrm{GeV}$ — five decades below $M_C$, where $\mathrm{SU}(4)$ is no longer the symmetry.

**So the phase is perturbative throughout its existence**, with $\alpha_4/\pi=0.018$ at its lower end, and the tree-level rates of the block are legitimate. **What replaces confinement is not freedom but a different theory**: at $M_C$ the group breaks and the coupling is matched, and the primordial coupling has no infrared limit to speak of.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\alpha_4$ | $g_4^{2}/4\pi$, the primordial coupling |
| $b_0$ | $\tfrac{26}{3}$, the one-loop coefficient with the model's content |
| $\mu_{1}$ | the scale at which $\alpha_4=1$, computed as $1.8\ \mathrm{GeV}$ |
| $\Lambda$ | the would-be confinement scale; used only for comparison |
| $M_C$ | the transition, $\gtrsim250\ \mathrm{TeV}$ |
| $M_X$ | the matching scale, $2.33\times10^{5}\ \mathrm{GeV}$ |

## Further Reading

- [The Primordial Coupling](the-primordial-coupling-g4-as-a-boundary-condition-and-what-runs-above-m-c.html). The coefficient, the solution and the Landau pole this article's numbers come from.
- [Asymptotic Freedom and the Running of the Strong Force](asymptotic-freedom-and-the-running-of-the-strong-coupling.html). The QCD comparison row, and the coefficient $11-\tfrac23N_f$ set beside $\tfrac{20}{3}$.
- [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). What happens at $M_C$, where this article's phase ends.
- [The $\mathrm{SU}(4)$ Instanton](the-su4-instanton-a-matrix-transcription-outside-the-algebra.html). The non-perturbative effect that exists without confinement.
