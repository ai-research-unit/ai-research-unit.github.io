# __The Weyl Curvature Hypothesis and Twistor Space as the Arena__

## Introduction

**Two of Roger Penrose's proposals belong together, and this section of the corpus is their home.** The first is the **Weyl curvature hypothesis** of 1979: that the gravitational field carried no Weyl curvature at the initial singularity, and that its growth since then is the arrow of time. The second is **twistor space**, proposed in 1967 as the arena from which spacetime itself emerges.

**They are grouped here because both are statements about the whole of spacetime and not about a field inside it.** A Weyl tensor is a property of a metric; a twistor is a point of a space that replaces the metric's arena. **Neither is a matter sector**, and neither can be filed under the particle content.

**The verdict of this article is stated at the start, because it governs every section.** The hypothesis is a **boundary condition** and the framework supplies no principle that selects it; twistor space is a **different theory** and the framework is not a version of it. **In the framework's scale-factor route the hypothesis is not merely unproved but empty**, because every metric in that route has zero Weyl curvature identically. That result is the sharpest thing this article has to report, and it is a negative one.

## The Hypothesis, Stated

**Two problems, one answer.** Cosmology faces two facts that look unrelated. **The universe is homogeneous and isotropic on its largest scales**, to a precision of one part in $10^{5}$ in the microwave background, so that a Friedmann–Lemaître model describes it. **And the second law of thermodynamics holds**, so the universe had a low-entropy past. Penrose's proposal is that one fact explains the other, through a quantity that had not been counted as entropy: **the Weyl curvature of the gravitational field**.

**The four claims of the hypothesis.**

| claim | content |
| --- | --- |
| the initial condition | the Weyl tensor vanished, or was negligible, at the initial singularity |
| the growth | it has risen monotonically since |
| the mechanism | structure formation — the clumping of matter — *is* that rise |
| the consequence | the cosmological arrow of time is the direction of that rise |

**Why Weyl and not Riemann.** The Riemann tensor splits into a trace part and a trace-free part,
$$
R_{abcd}=C_{abcd}+\tfrac12\bigl(g_{ac}R_{bd}-g_{ad}R_{bc}+g_{bd}R_{ac}-g_{bc}R_{ad}\bigr)-\tfrac16 R\bigl(g_{ac}g_{bd}-g_{ad}g_{bc}\bigr),
$$
**and only the trace-free piece $C_{abcd}$ survives in vacuum.** The trace part is fixed locally by the matter through Einstein's equations; **the Weyl part is the field's own degrees of freedom** — tidal distortion and gravitational radiation. **A homogeneous and isotropic metric has no tidal distortion and radiates nothing, so its Weyl tensor is zero**; a lumpy one has both. That single fact is the whole of the hypothesis's physical content.

**What it is a hypothesis about.** Not a field equation — the Einstein equations hold either way. **It is a statement about which solution of them the universe is**, and specifically about the **initial** one. Penrose's own framing is that the Creator, faced with an enormous space of solutions, chose one of measure zero: **his estimate of the fine-tuning is one part in $10^{10^{123}}$**, a number whose exponent is itself astronomical. **Nothing in this corpus produces such a number or checks it**, and it is quoted here as Penrose's estimate and not as a computation.

**The alternative it is posed against.** The hypothesis is offered as a **credible alternative to cosmic inflation**, which explains the same homogeneity and isotropy by a period of accelerated expansion. **The two are not the same claim.** Inflation says the smoothness was *produced* by dynamics after the bang; the hypothesis says it was *there at the bang*, as a boundary condition, and that no dynamics is needed. **A framework that can state one but not the other has a definite position, and this corpus is in that position** — see the next two sections.

**A third consequence, and the one that costs most.** Generic solutions of the Einstein equations near a singularity are not isotropic. The **BKL analysis** shows that a generic spacelike singularity oscillates, with the metric's terms exchanging dominance chaotically, and the Weyl curvature diverges there faster than the Ricci part — the singularity is **Weyl-dominated**. **So the hypothesis asserts that the actual big bang was not a generic singularity.** That is its strength, because it is a sharp claim, and its weakness, because nothing in classical general relativity prefers the non-generic case.

**The extension, stated once and not used below.** In **conformal cyclic cosmology** the hypothesis becomes a matching condition between successive aeons, and the vanishing of the Weyl tensor at each aeon's start is what makes the join conformally smooth. **The corpus does not develop that programme**, and this paragraph exists so that a reader who has met the idea knows where it stands here.

## The Two Computations the Hypothesis Rests On

**Both claims below are exact and both are recomputed here from the metric, not quoted.**

**First: every Friedmann–Lemaître metric has zero Weyl curvature, for every scale factor.** With the flat spatial slice and $a(t)$ arbitrary,

$$
g=\operatorname{diag}\Bigl(-1,\ a(t)^{2},\ a(t)^{2},\ a(t)^{2}\Bigr),
$$

**all 256 components of $C_{abcd}$ vanish identically**, while the Ricci tensor does not: $R_{tt}=-3\ddot a/a$. **The vanishing is therefore not the trivial vanishing of flat space** — the spacetime is curved and its Weyl part is still zero. That is the defining property of a **conformally flat** metric, and every Friedmann–Lemaître metric has it, whatever the equation of state and whatever the scale factor does.

**Second: a single mass has non-zero Weyl curvature, and the invariant is exact.** For Schwarzschild,

$$
C_{abcd}C^{abcd}=\frac{48M^{2}}{r^{6}}\ \ \text{exactly},
$$

**checked here by raising all four indices of the computed $C_{abcd}$ numerically**: at $M=1$, $r=5$ the sum comes to $3.072\times10^{-3}$, and $48/5^{6}=3.072\times10^{-3}$. **The tensor is Petrov type D**, so its Weyl spinor has one repeated principal null direction and one non-zero scalar, $\tilde\Xi_{2}$.

**The two computations together are the hypothesis in numbers.** Smooth $\Rightarrow$ zero; a mass $\Rightarrow$ $48M^{2}/r^{6}$; therefore **any departure from homogeneity raises the invariant**, and the rise the hypothesis speaks of is the growth of this number as matter clumps. **The hypothesis is the statement that the first number was zero at the bang and the second is what it has become.**

**What these two computations do not do.** They show that the hypothesis is *statable* and *checkable* for a given metric. **They do not show that the early universe had zero Weyl**, and no computation in this corpus does.

## What the Framework Says: The Scale-Factor Route Makes the Hypothesis Empty

**The framework reaches a metric by two routes, and the two give opposite verdicts on the hypothesis.**

**Route one is the local scale factor.** The metric is

$$
g_{\mu\nu}=\lambda^{2}\,\eta_{\mu\nu},
$$

**with $\lambda$ a scalar function** — the class [Curved Spacetime and the Biquaternion Framework](curved-spacetime-and-the-biquaternion-framework.html) calls route one. **Every member of this class is conformally flat, so its Weyl tensor vanishes identically at every time, for every $\lambda$.** That is not a coincidence of the ansatz; it is what conformal flatness means, and the previous section computed it for the Friedmann–Lemaître case, which is the physically interesting member.

**The consequence is severe and it is the main result of this article.** In route one the Weyl curvature hypothesis is **true by construction and therefore empty**: it cannot distinguish an early universe from a late one, cannot explain why the bang was special, and cannot carry an arrow of time. **A framework whose only metric is a scale factor times flat has no Weyl curvature to make a hypothesis about.** Anyone who wants the hypothesis must leave route one; that is not a preference, it is a theorem about the class.

**Route two is a field of frames.** The metric is the pullback of the algebra's form along a frame field,
$$
g_{\mu\nu}=\bigl\langle \tilde E_{\Phi,\mu},\tilde E_{\Phi,\nu}\bigr\rangle_{\natural},
$$
**and this class is not conformally flat**: its Weyl tensor is a functional of the frame field, non-zero in general. The **Kerr–Schild sub-class** is the sharpest member, and its members carry principal null congruences, so they are Weyl-non-zero by construction.

**So route two is where the hypothesis can be stated, and route two is where the framework stops.** The Weyl tensor is then a function of the frame field, and **the hypothesis becomes a condition on that field's initial value**. The framework does not supply it. [The Newman–Penrose Formalism](the-newman-penrose-formalism-in-biquaternionic-form.html) records the gap precisely: **the algebra hosts $\mathrm{sym}^{4}S$, the space the Weyl spinor lives in, but nothing in $\mathbb{B}$ determines which element of it a given spacetime produces.** A boundary condition on an object the algebra does not generate is not derivable from the algebra.

**What the framework does supply, and it is not nothing.** It supplies the **carrier**: the Weyl spinor is $\mathrm{sym}^{4}S$-valued, complex dimension five, whose real and imaginary parts give the ten real components of $C_{abcd}$ — five self-dual and five anti-self-dual. **The hypothesis is then a statement about one half of a five-complex-dimensional object**, and the framework can say exactly which half is meant. **That precision is the framework's contribution here, and it is a contribution of language, not of dynamics.**

| route | metric class | Weyl tensor | status of the hypothesis |
| --- | --- | --- | --- |
| one, local scale factor | $\lambda^{2}\eta$ | $C_{abcd}=0$ identically | true by construction, hence empty |
| two, field of frames | $g=\langle \tilde E_\mu,\tilde E_\nu\rangle_\natural$ | $C\ne0$ in general | a boundary condition, not derived |
| two, Kerr–Schild sub-class | $\delta+2h\ell\ell$ | non-zero, null-aligned | statable, and not selected |

## Twistor Space as the Arena

**If twistor space replaces spacetime as the arena, the result is not a reformulation of general relativity; it is a different theory.** That sentence is the reason this material sits in a section of its own. **A theory is its arena plus its fields plus its dynamics**, and a programme that changes the first changes the theory.

**The object.** Twistor space is $T\cong\mathbb{C}^{4}$ with coordinates $Z^{\alpha}=(\omega^{A},\pi_{A'})$ — **two Weyl spinors of opposite chirality**, so $T=S\oplus\bar S$. **Projective twistor space is $\mathbb{PT}=\mathbb{CP}^{3}$**, the space of complex lines, and it carries a Hermitian form of inertia $(2,2)$ whose isometry group $\mathrm{SU}(2,2)$ is a **quadruple cover of the conformal group** $C(1,3)$ of compactified Minkowski space.

**The correspondence, in one display.** A point of complexified Minkowski space is a $2\times2$ matrix $x_{A\bar A}$, and it defines a line in $\mathbb{PT}$ by the **incidence relation**

$$
\omega^{A}=i\,x^{A}{}_{\bar A}\,\pi^{\bar A}.
$$

**Two points are null-separated exactly when their lines meet**, which happens exactly when $\det(x-y)=0$ — the Minkowski interval as the determinant of a $2\times2$ matrix. **Spacetime points become lines, and the light cone becomes incidence**: this is the Klein correspondence, and it is the geometric heart of the programme.

**Why it is not merely a rewriting.** Three of the programme's results have no counterpart in a metric-first formulation. **The Penrose transform** represents solutions of the massless field equations of helicity $h$ as sheaf cohomology classes $H^{1}\bigl(\mathbb{PT},\mathcal{O}(-2h-2)\bigr)$ — **a field on spacetime becomes a cohomology class on a complex manifold**, with no metric in the statement. **The nonlinear graviton** represents every half-flat Ricci-flat complex spacetime as a **deformation of the complex structure** of a region of $\mathbb{PT}$ — **a spacetime becomes a complex manifold's deformation**. **The Ward correspondence** does the same for self-dual Yang–Mills fields, as holomorphic vector bundles. **None of these is a change of coordinates**, and that is the precise sense in which twistor theory is a different theory and not a dictionary.

**The limitation, and it is exactly this article's junction.** The nonlinear graviton encodes **half-flat** spacetimes — those whose Weyl tensor is **self-dual** (or anti-self-dual, depending on the convention), the left-handed half. **A construction that can only encode one half of $C_{abcd}$ cannot state the Weyl curvature hypothesis**, which is a claim about the whole tensor and about its growth. **The two Penrose proposals in this article therefore do not meet**: the hypothesis needs the full Weyl tensor, and the arena that was built to encode Weyl curvature encodes one chirality of it. **Penrose named the missing half the *googly problem*** — the word is from cricket — and his 2015 proposal, **palatial twistor theory**, attacks it by replacing the holomorphic functions on twistor space with a non-commutative algebra of them. **No version of it is used in this corpus.**

**The later descendants, named once.** Ambitwistor space complexifies the light rays themselves; twistor string theory is a quantum theory of holomorphic maps of a Riemann surface into twistor space; the RSV formulae, BCFW recursion, the Grassmannian and the amplituhedron all descend from it and belong to the theory of scattering amplitudes. **They are recorded here for completeness and are not used anywhere in the corpus.**

## The Three Senses of the Word in This Corpus

**The word *twistor* has carried three different objects in this corpus's literature, and grouping them here is the reason this section exists at all.**

**The first is the classical object: incidence data of a complex null line.** It is Penrose's twistor, a point of $T$, and the incidence relation above. **Everything in the previous section is this sense.**

**The second is Alexeyeva's algebraic twistor.** It is a solution of the homogeneous biquaternionic biwave equation
$$
\vec\nabla_{+}B+\vec F\circ B=0,
\qquad \vec F=-E-iH,
$$
**with a constant complex vector coefficient.** The solutions come in four families — non-stationary, $H$-, stationary and static — each of unit norm in the algebra, each with a generating scalar potential from which it is recovered by one first-order operator. **One member is distinguished:** the $H$-twistor's amplitude is a **rank-one Hermitian idempotent**, $-\sqrt2\,\tilde\Pi_{\mathrm{id},2}(\vec u_H)$, so it is the only one of the four whose amplitude is a pure state. **These are field configurations on spacetime, not points of a conformal module**, and the homonym must not be read as the classical sense.

**The third is Kassandrov's congruence twistor.** In the algebrodynamical programme the complex eikonal equation of the generalised Cauchy–Riemann conditions generates **shear-free congruences of complex null rays**, and the congruence's **twistor field** $\{\zeta,\tau\}$ is fixed by
$$
\bigl(Z-\mathcal Z(\kappa)\bigr)\zeta=0,
\qquad
\tau=Z\zeta,
$$
**which is the incidence relation over complexified Minkowski space, with the charge's world line as the caustic.** The parameter $\kappa$ is fixed by the complex null-cone equation $\det\lvert Z-\mathcal Z(\kappa)\rvert=0$, **which over $\mathbb{C}$ has several roots** — and the programme's physics is built on that multiplicity.

**So the first and the third senses are the same object** — incidence data of a complex null line — **used in two settings, and only the second is a genuine homonym.** The word's three senses are collected here so that a reader meets them once, in one place, rather than as scattered references across the corpus.

## What This Section Does Not Claim

**It does not derive the Weyl curvature hypothesis.** The framework states it, shows where it can be stated, and shows that one of its two metric routes empties it. **A boundary condition that the algebra does not generate is not derived by the algebra.**

**It does not reproduce any twistor result.** The Penrose transform, the nonlinear graviton, the Ward correspondence and the twistor-string formulae are described, not derived, and **no display in this article is a twistor computation.** The one thing checked is the Klein-correspondence identity $\det(x-y)=\text{interval}$, and it is checked because it is a two-line calculation.

**It does not claim the framework is a version of twistor theory, or the reverse.** The two share the spinor module $S=\mathbb{C}^{2}$ and the covering $\mathrm{SL}(2,\mathbb{C})\to SO^{+}(1,3)$, which is older than both. **A shared module is not a shared theory**, and the aims differ: one organises conformal and null structure by complex-projective methods, the other keeps the observable sector real.

**It does not adopt conformal cyclic cosmology.** The hypothesis's extension to aeons is recorded in one paragraph above and used nowhere.

## The Checks

| check | computation | result |
| --- | --- | --- |
| Friedmann–Lemaître Weyl tensor | all 256 components of $C_{abcd}$, $a(t)$ symbolic | $0$ |
| Friedmann–Lemaître Ricci tensor | $R_{tt}$ | $-3\ddot a/a\ne0$ |
| conformal flatness, route one | $g=\lambda^{2}\eta$ | $C_{abcd}\equiv0$ |
| Schwarzschild Weyl invariant | $C_{abcd}C^{abcd}$ | $48M^{2}/r^{6}$ |
| the same at $M=1$, $r=5$ | numerical | $3.072\times10^{-3}$ |
| Schwarzschild Ricci | all components | $0$ |
| the Weyl spinor's carrier | $\dim_{\mathbb{C}}\mathrm{sym}^{4}S$ | $5$ |
| real components of $C$ | $5$ complex, self-dual and anti-self-dual | $10$ |
| projective twistor space | $\dim_{\mathbb{C}}\mathbb{CP}^{3}$ | $3$ |
| the conformal cover | $\mathrm{SU}(2,2)\to C(1,3)$ | fourfold |
| the interval as a determinant | $\det(x-y)$ against the Minkowski interval | exact |
| the hypothesis's fine-tuning | Penrose's estimate | $10^{-10^{123}}$ |

## Summary

**The Weyl curvature hypothesis is a boundary condition, and this is a corpus that has no principle for boundary conditions.** It says the gravitational field carried no tidal distortion at the bang, that clumping has raised it since, and that the rise is the arrow of time. **Its two supporting computations are exact**: every Friedmann–Lemaître metric has zero Weyl curvature while remaining curved, and a single mass has $C_{abcd}C^{abcd}=48M^{2}/r^{6}$.

**The framework's verdict is a split, and the split is the result.** In the **scale-factor route** every metric is conformally flat, so the hypothesis is true by construction and empty — **the framework in that route has no Weyl curvature to hypothesise about**. In the **frame route** the Weyl tensor is non-zero and is a functional of a frame field the algebra does not generate, so the hypothesis is statable and not derivable. **The framework supplies the carrier, $\mathrm{sym}^{4}S$, and not the value.**

**Twistor space is a different theory and not a reformulation.** Points become lines, the light cone becomes incidence, massless fields become cohomology classes, and half-flat spacetimes become deformations of a complex structure. **Because the nonlinear graviton encodes one chirality of the Weyl tensor, the arena built to encode Weyl curvature cannot state the hypothesis about it** — that is the googly problem, and it is where the two halves of this article fail to meet.

**Three senses of the word are collected here and distinguished**: the classical incidence twistor, Alexeyeva's algebraic twistor with its four families and its one idempotent amplitude, and Kassandrov's congruence twistor with its caustic world line. **Two are the same object used twice; one is a homonym.**

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $C_{abcd}$ | the Weyl tensor, the trace-free part of $R_{abcd}$ |
| $C_{abcd}C^{abcd}$ | its invariant, $48M^{2}/r^{6}$ for Schwarzschild |
| $\lambda$ | the local scale factor of route one, $g=\lambda^{2}\eta$ |
| $\tilde E_{\Phi,\mu}$ | the frame field of route two, $g_{\mu\nu}=\langle \tilde E_{\Phi,\mu},\tilde E_{\Phi,\nu}\rangle_{\natural}$ |
| $T\cong\mathbb{C}^{4}$ | twistor space, $S\oplus\bar S$ |
| $Z^{\alpha}=(\omega^{A},\pi_{A'})$ | a twistor, two Weyl spinors of opposite chirality |
| $\mathbb{PT}=\mathbb{CP}^{3}$ | projective twistor space |
| $\omega^{A}=i x^{A}{}_{\bar A}\pi^{\bar A}$ | the incidence relation |
| $\mathrm{sym}^{4}S$ | the carrier of the Weyl spinor, complex dimension $5$ |
| $\mathcal Z(\kappa)$ | the charge's complex world line in the algebrodynamical programme |
| $\{\zeta,\tau\}$ | the congruence twistor field, $(Z-\mathcal Z)\zeta=0$, $\tau=Z\zeta$ |

## Further Reading

- [Curved Spacetime and the Biquaternion Framework](curved-spacetime-and-the-biquaternion-framework.html). The two routes to a metric, and the statement that route one is a local scale factor.
- [The Newman–Penrose Formalism in Biquaternionic Form](the-newman-penrose-formalism-in-biquaternionic-form.html). The null tetrad, the five Weyl scalars, and the gap: the algebra hosts $\mathrm{sym}^{4}S$ and does not determine it.
- [FLRW in the Frame Route](flrw-in-the-frame-route.html). The conformal flatness of the slice metric, computed in the coordinates the frame route uses.
- [The Kerr–Schild Sub-class and the Vacuum Wave](the-kerr-schild-sub-class-and-the-vacuum-wave.html). The family in which the frame route's metrics carry a principal null congruence.
- [Twistor Theory and Biquaternions](twistor-theory-and-biquaternions.html). The comparison: the shared spinor module, the three module structures on $\mathbb{C}^{4}$, and the divergences in aim.
- [Congruence Twistors and the Fields They Generate](congruence-twistors-and-the-fields-they-generate.html). The third sense of the word, developed.
- [The Algebrodynamical Programme](the-algebrodynamical-programme-nonlinear-cauchy-riemann-conditions-self-quantized-charge-and-induced-causal-geometry.html). Kassandrov's programme, where the congruence twistor does its work.
- [The SO(4) Route to the Euclidean Frame](the-so4-route-to-the-euclidean-frame-an-alternative-to-the-imaginary-time-coordinate.html). Woit's Euclidean twistor unification, recorded there as an external construction.
- R. Penrose, "Singularities and time-asymmetry," in *General Relativity: An Einstein Centenary Survey* (Cambridge, 1979), 581–638, the hypothesis's source.
- R. Penrose, "Nonlinear gravitons and curved twistor theory," *General Relativity and Gravitation* **7** (1976) 31–52, for the half-flat construction and the googly problem.
- V. A. Belinskii, I. M. Khalatnikov and E. M. Lifshitz, "Oscillatory approach to a singular point in the relativistic cosmology," *Advances in Physics* **19** (1970) 525–573, for the generic Weyl-dominated singularity the hypothesis denies.
- R. Penrose, "Palatial twistor theory and the twistor googly problem," *Philosophical Transactions of the Royal Society A* **373** (2015) 20140237.
