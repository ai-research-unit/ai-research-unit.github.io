# __The Lagrangian and the Electroweak Theory__

## Introduction

What the corpus has and what it lacks. The corpus has the electroweak group, its hypercharge assignment, its doublet, its potential, its gauge-boson masses, its quotient and its parity lock. It does not have the electroweak Lagrangian in one display, and this family has no quantised electroweak theory at all. This article writes the one Lagrangian in its two phases — unbroken and broken — and states what the variational principle says about each.

The answer in five sentences. The unbroken action is the gauge action of $SU(2)\times U(1)$ with one complex doublet and its potential. Its variation gives the Yang–Mills equations with the doublet's currents, the scalar's equation and the constraint that Gauss's law becomes for each generator. At the potential's minimum the doublet's gradient term becomes a mass term for three of the four gauge fields, and the count of degrees of freedom is preserved because the three would-be Goldstone modes become the longitudinal polarisations. The masses are therefore products of a coupling and a vacuum expectation value, not parameters. Nothing in the article is quantised: no gauge fixing, no ghost, no loop, no running.

Why both phases in one article. Because the breaking is a classical statement about a potential's minimum, and the corpus can make it exactly. A reader who has been told that the corpus "does not do the Standard Model" should see precisely what it does do: the classical action, its two phases, and the mass relation $m_W=gv/2$ with the count that forces it.

## Conventions

The conventions are the corpus's, and they are the ones the menu's convention articles fix. The gauge group is $SU(2)_L\times U(1)_Y$ with couplings $g$ and $g_{\mathrm Y}$; the gauge fields are $W_{\mu,a}$ for $a=1,2,3$ and $B_\mu$; the field strengths are $W_{a,\mu\nu}=\partial_\mu W_{a,\nu}-\partial_\nu W_{a,\mu}+g\epsilon_{abc}W_{b,\mu} W_{c,\nu}$ and $B_{\mu\nu}=\partial_\mu B_\nu-\partial_\nu B_\mu$. The doublet is $\Phi$, a complex two-component column with hypercharge $Y_\varphi=+\tfrac12$; its covariant derivative is

$$
D_\mu\Phi=\Bigl(\partial_\mu+i\,g\,\tau_{a}W_{a,\mu}+i\,g_{\mathrm Y}Y_\varphi B_\mu\Bigr)\Phi ,
$$

with $\tau_{a}=\sigma_{a}/2$ the generators in the doublet, so that $T_3$ has eigenvalues $\pm\tfrac12$ and the electric charge is $Q=T_3+Y$. The potential is $V(\Phi)=-\mu^{2}\Phi^{\dagger}\Phi+\lambda(\Phi^{\dagger}\Phi)^{2}$ with $\mu^{2}>0$ and $\lambda>0$. The measure is $\mathrm{d}^{4}x$; a repeated low index is summed with the weight $\varepsilon=(1,-1,-1,-1)$, so $(D_\mu\Phi)^{\dagger}D_\mu\Phi=\sum_\mu\varepsilon_\mu(D_\mu\Phi)^{\dagger}D_\mu\Phi$ carries the sign the mostly-minus literature carries; and the biquaternionic writing of the $U(1)$ connection is the Maxwell article's.

Two conventions, both settled by the corpus. The hypercharge here is $Y$, not the reference tables' $Y_W=2Y$: the corpus writes $Q=T_3+Y$ with $Y_\varphi=+\tfrac12$, as [The Electroweak Gauge Group and the Hypercharge Assignment in the Four Colours Left–Right Model: The Group and the Derived $Y$](the-electroweak-gauge-group-and-the-hypercharge-assignment.html) fixes it and as [Electroweak Symmetry Breaking](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-gauge-boson-masses.html) uses it. Only the product $g_{\mathrm Y}Y$ enters any display, so a reader who arrives with $Y_W$ must halve every hypercharge and change no physical statement. The sign of the coupling in $D_\mu$ is likewise the corpus's, $+ig$; the opposite choice, $-ig$, is the same theory with $g\mapsto-g$, and every mass below is quadratic in $g$ and unchanged.

**One convention is a warning.** The corpus's biquaternion algebra carries the $U(1)$ connection exactly, and it carries the $SU(2)$ group exactly too: the compact factor is $SU(2)$ itself, the unit real quaternions $\mathrm{Spin}(3)=S^{3}$, so the connection the algebra writes is the one electroweak theory needs. What it does not carry is the way electroweak theory uses that group — a doublet chosen independently of the spin, and a chiral action on one letter. The electroweak articles state both halves. So the displays below are in the component dictionary, which is exact, and the biquaternionic translation is claimed only where the electroweak articles claim it.

## The Action in Element Form

The unbroken action, in four terms.

$$
S=\int\mathrm{d}^{4}x\;\Bigl\{-\tfrac14 W_{a,\mu\nu}W_{a,\mu\nu}-\tfrac14 B_{\mu\nu}B_{\mu\nu}+(D_\mu\Phi)^{\dagger}D_{\mu}\Phi-V(\Phi)+\mathcal{L}_{\mathrm{matter}}\Bigr\},
$$

with $\mathcal{L}_{\mathrm{matter}}$ the fermion kinetic terms with their covariant derivatives and the Yukawa couplings, which this article names and does not expand.

Why each term is what it is. The two gauge terms are the Yang–Mills and Maxwell terms: quadratic in the field strengths, gauge invariant, and fixed in normalisation by the same requirement that fixes the Maxwell term — the charge that appears in the covariant derivative must be the charge that appears in the current. The scalar term is the Klein–Gordon kinetic term with the derivative covariantised, which is the same minimal-coupling step the coupled scalar article performs, applied twice because the group has two factors. The potential is the only term with a negative mass squared, and it is the term that decides the phase.

The two phases, and why the same action has them. The potential's minimum is at $\Phi^{\dagger}\Phi=\mu^{2}/2\lambda\equiv v^{2}/2$, a circle of minima and not a point. If $\mu^{2}<0$ the minimum is at $\Phi=0$ and the action's ground state is symmetric; if $\mu^{2}>0$ it is not. The action does not change between the phases; the vacuum does. That is the classical content of "spontaneous breaking", and the corpus can state it exactly.

The broken phase, written in the unitary chart. Choose the vacuum $\Phi=\frac{1}{\sqrt{2}}\binom{0}{v+h}$ with $h$ the physical scalar. Then the scalar's gradient term becomes

$$
(D_\mu\Phi)^{\dagger}D_{\mu}\Phi\supset\frac{v^{2}}{8}\Bigl[g^{2}\bigl((W_{1,\mu})^{2}+(W_{2,\mu})^{2}\bigr)+(gW_{3,\mu}-g_{\mathrm Y}B_\mu)^{2}\Bigr]+\frac{g^{2}v}{2}h\,W^{+}W^{-}+\cdots ,
$$

which is a mass term for the combinations $W^{\pm}=(W_1\mp iW_2)/\sqrt2$ and $Z=(gW_3-g_{\mathrm Y}B)/\sqrt{g^{2}+g_{\mathrm Y}^{2}}$, and none for $A=(g_{\mathrm Y}B+gW_3)/\sqrt{g^{2}+g_{\mathrm Y}^{2}}$. The masses are $m_W=gv/2$, $m_Z=\sqrt{g^{2}+g_{\mathrm Y}^{2}}\,v/2$ and $m_A=0$.

**What the display is not.** It is not a gauge-fixing term and not a quantisation. It is the same action, evaluated at a chosen vacuum, with the scalar's fluctuations kept. The chart is called unitary because it keeps only the physical scalar; the quantised theory's $R_\xi$ charts are a different construction and are not in this article.

## The Variation

Three variations and the constraint each produces. Varying $W_{a,\mu}$ and $B_\mu$ gives the Yang–Mills and Maxwell equations with the currents of the doublet and the fermions as sources,

$$
D_\mu W_{a,\mu\nu}=J_{a,\nu},
\qquad
\partial_\mu B_{\mu\nu}=J^{Y}_{\nu},
$$

with the covariant divergence on the left because the field strength is non-Abelian. Varying $\Phi^{\dagger}$ gives the covariant Klein–Gordon equation with the potential's derivative,

$$
D_\mu D_{\mu}\Phi=-\frac{\partial V}{\partial\Phi^{\dagger}} ,
$$

and varying the fermions gives their covariant Dirac equations.

The constraint. Take the time component of the gauge equations and the divergence of their spatial part. The $\mu=0$ components are Gauss's law for each generator, four constraints and not evolution equations; the divergence of the spatial equations reproduces them, because the currents are covariantly conserved by the matter equations. The non-Abelian case adds a term: the current's conservation is $D_\mu J_{a,\mu}=0$ with the connection in the derivative, and the constraint's consistency uses exactly that.

The boundary term. Each variation is first or second order as its parent is; the gauge variations are second order and their surface terms are killed by holding the field and its normal derivative fixed. The scalar's variation is second order and the same condition applies.

**What the variation does not give.** It does not give the ghost terms, the gauge-fixing terms or the BRST structure. Those belong to the quantised theory, which this family does not contain; the corpus's $R_\xi$ article states them for the standard theory and is not this family's.

## The Constraints the Action Imposes

Four Gauss laws, one per generator, and one orbit. The unbroken action's constraints are the four $\mu=0$ gauge equations, $D_j W_{a,j0}=\rho_{a}$ and $\partial_j B^{j0}=\rho^{Y}$, conditions on the initial data for each generator. The gauge orbit is the four-function local group, acting on the gauge fields and the doublet together.

The count, before and after. Before breaking: four gauge fields, two polarisations each if massless — eight; one complex doublet, four real scalars; total twelve. After breaking: three massive vectors, three polarisations each — nine; one massless vector, two — two; one physical scalar — one; total twelve. The count is preserved, and the three that moved are the three would-be Goldstone modes, which became the longitudinal polarisations.

Why the constraint is not the gauge choice. As in the Maxwell article, the constraint is the action's content and the gauge choice is a representative's selection. The unitary chart is a choice: it fixes the gauge by putting the Goldstone modes inside the vectors. A reader who confuses the two will think that the breaking removed degrees of freedom; the count above shows it did not.

**What the massive vectors' constraint is.** A massive vector's time component is still constrained — the Proca article's statement — so the three polarisations are two transverse and one longitudinal, and the longitudinal one is the Goldstone mode in the chart. The corpus can therefore state the Higgs mechanism as a count and not as a metaphor.

## The Structural Consequence: The Masses Are Couplings Times a Vacuum Value

The claim. $m_W=gv/2$ and $m_Z=\sqrt{g^{2}+g_{\mathrm Y}^{2}}\,v/2$ are not free parameters of the broken action. They are the coefficients that the scalar's gradient term produces when the doublet is expanded about its minimum, and each is a product of one coupling and one number.

The hand check. Expand $\Phi=\frac{1}{\sqrt2}\binom{0}{v}$ in the gradient term. The term is $(D_\mu\Phi)^{\dagger}D_{\mu}\Phi$, with the $1/\sqrt2$ already inside $\Phi$; the $W$ parts give $\frac{g^{2}v^{2}}{8}[(W_1)^{2}+(W_2)^{2}]$, which is $\frac12 m_W^{2}(W_1W_1+W_2W_2)$ with $m_W=gv/2$; the neutral part gives $\frac{v^{2}}{8}(gW_3-g_{\mathrm Y}B)^{2}=\frac12 m_Z^{2}Z^{2}$ with $m_Z^{2}=(g^{2}+g_{\mathrm Y}^{2})v^{2}/4$. The massless combination is orthogonal to $Z$ and reads $A=(g_{\mathrm Y}B+gW_3)/\sqrt{g^{2}+g_{\mathrm Y}^{2}}$, the photon.

What follows without a further assumption. The ratio $m_W/m_Z=\cos\theta_W$ with $\tan\theta_W=g_{\mathrm Y}/g$; the photon's masslessness, because $A$ is the direction the doublet does not see; and the $W$'s and $Z$'s coupling to the scalar, $\frac{g^{2}v}{2}hW^{+}W^{-}=2M_W^{2}hW^{+}W^{-}/v$, which is the same $v$ and therefore the same $g$.

**What the claim forbids.** It forbids treating the vector masses as independent parameters and then adding a scalar with a tuned coupling: the action has one $v$, one $g$, one $g_{\mathrm Y}$, and the masses and the trilinear couplings are all read from them. An action that produced $m_W$ and $m_Z$ with independent coefficients would not be a gauge theory's broken phase; it would be a Proca theory with two masses.

## The Noether Currents and the Sign of the Charge

Three currents and one combination that survives the breaking. The $SU(2)$ currents $J_{a,\mu}$ and the hypercharge current $J_{Y,\mu}$ are conserved in the unbroken phase; after breaking, the three combinations that correspond to the broken generators are not conserved, and the combination

$$
Q=T_3+Y
$$

is. Its current is the electromagnetic one, and the photon is its gauge field.

The sign. The sign of the electric charge is the sign of the eigenvalue of $Q$, and $Q$'s normalisation is fixed by the scalar's hypercharge $Y_\varphi=+\tfrac12$ and by $T_3=\pm\tfrac12$ on the doublet. The electron sits in the lepton doublet, whose hypercharge is $-\tfrac12$, and its $T_3=-\tfrac12$; the two sum to the observed $Q=-1$. The assignment is the corpus's electroweak articles', not this article's choice.

**Why only one combination survives.** A current is conserved after breaking if its generator annihilates the vacuum. The vacuum is neutral under $Q$ and not under $T_1,T_2$ or $T_3-Y$ separately, so exactly one combination of the four generators leaves it invariant. That is the same statement as the photon's masslessness, read from the currents rather than from the masses — two readings of one fact, and the article gives both because they are checkable independently.

The stress. The energy density is the sum of the gauge fields', the scalar's and the fermions'. In the broken phase the vector masses contribute $\frac12m^{2}A_0^{2}$ terms to it, and the positivity of the energy is the positivity of each term. There is no cross term of indefinite sign, and that is a property of the unitary chart: in a general chart the Goldstone modes' kinetic terms can look indefinite, and the chart is what removes the appearance.

## What the Principle Adds and What It Relabels

Adds. The two phases as one action, the mass relation as a computation, and the count as a consequence of the constraints and the orbit. Each of those is a statement a reader can check from the displays, and none of them needs a quantisation.

Relabels. The corpus's electroweak articles' statements — the group, the hypercharge, the doublet, the potential, the masses, the quotient, the parity lock — are all recoverable from the action, and the action adds no number to them.

**What it does not reach, and this family does not either.** The quantised theory: the gauge fixing and the ghosts, the $R_\xi$ charts, the Ward identities, the running of $g$ and $g_{\mathrm Y}$, the oblique parameters, the precision observables. The corpus has articles *about* those subjects and does not have the theory that computes them. A reader who wants the $S$-parameter will find its definition and not its value from this family.

The honest sentence. This family's electroweak content is a classical gauge theory with a classical breaking, exact and checkable, and it is not the Standard Model. The gap is quantisation, and the bridge article is where the gap is named.

## Summary

The electroweak Lagrangian is the $SU(2)\times U(1)$ gauge action with one complex doublet and its potential. Its variation gives the Yang–Mills equations with the doublet's currents, the covariant scalar equation and four Gauss constraints. At the potential's minimum the doublet's gradient term gives $m_W=gv/2$, $m_Z=\sqrt{g^{2}+g_{\mathrm Y}^{2}}v/2$ and $m_A=0$, and the count eight-plus-four becomes nine-plus-two-plus-one without loss. The surviving current is the electric one, $Q=T_3+Y$. Nothing is quantised, and the article says so.

$$
S=\int\mathrm{d}^{4}x\;\Bigl\{-\tfrac14W_{a,\mu\nu}W_{a,\mu\nu}-\tfrac14B_{\mu\nu}B_{\mu\nu}+(D_\mu\Phi)^{\dagger}D_{\mu}\Phi-V(\Phi)\Bigr\},
\qquad
V=-\mu^{2}\Phi^{\dagger}\Phi+\lambda(\Phi^{\dagger}\Phi)^{2}.
$$

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $g,\ g_{\mathrm Y}$ | $SU(2)_L$ and $U(1)_Y$ couplings |
| $W_{a,\mu},\ B_\mu$ | Gauge fields of the two factors |
| $W_{a,\mu\nu},\ B_{\mu\nu}$ | Field strengths, the first non-Abelian |
| $\Phi$ | Complex doublet, hypercharge $Y_\varphi=+\tfrac12$ |
| $D_\mu\Phi$ | Covariant derivative with both connections |
| $V(\Phi)$ | $-\mu^{2}\Phi^{\dagger}\Phi+\lambda(\Phi^{\dagger}\Phi)^{2}$ |
| $v=\sqrt{\mu^{2}/\lambda}$ | Vacuum expectation value |
| $W^{\pm},\ Z,\ A$ | Mass eigenstates of the neutral and charged sectors |
| $m_W=gv/2,\ m_Z=\sqrt{g^{2}+g_{\mathrm Y}^{2}}v/2$ | Vector masses |
| $Q=T_3+Y$ | Electric charge |
| $h$ | Physical scalar fluctuation |

## Further Reading

- *Electroweak Theory in the Biquaternion Framework: The U(2) Reach and the Chiral Wall*, for what the algebra carries and what it does not.
- *Electroweak Symmetry Breaking: The Doublet, the Potential and the Gauge Boson Masses*, for the masses and the count this article derives from the action.
- *The Electroweak Gauge Group and the Hypercharge Assignment in the Four Colours Left–Right Model: The Group and the Derived $Y$*, for the conventions.
- *Gauge Fixing in the Electroweak Theory: R-xi Gauges, Ghosts and the Goldstone Equivalence Theorem*, for the quantised structures this article does not contain.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. II*, for the quantised electroweak theory.
- Chris Quigg, *Gauge Theories of the Strong, Weak and Electromagnetic Interactions*, for the classical breaking and the mass relation.
