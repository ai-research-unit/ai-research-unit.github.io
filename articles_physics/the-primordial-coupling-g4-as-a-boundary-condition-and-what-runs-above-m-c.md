# __The Primordial Coupling: $g_4$ as a Boundary Condition, and What Runs Above $M_C$__

## Introduction

The model has one connection coupling, and this article says where its value comes from, which way the running faces, and what the coefficient of that running is.

**What was missing.** *The One Coupling That Returns the Standard Model* fixes $g_4$ from below, by matching the strong coupling at the leptoquark scale,

$$
g_4^{2}=4\pi\,\alpha_s(M_X) ,
$$

and then uses the value to turn the $K_L\to\mu e$ rate into a mass bound. **Nothing in the corpus integrates the same coupling upward.** Above $M_C$ the group is $\mathrm{SU}(4)$, the content is the fifteen connections, the sixteen Weyl fields and the scalar, and the coefficient that governs the coupling there is written nowhere. That coefficient is a two-line computation and its absence left the phase described but not computed.

**What this article supplies.**

- *The coefficient.* $b_0=\tfrac{26}{3}=8.67$ for $\mathrm{SU}(4)$ with this content, in the same convention in which QCD's is $11-\tfrac23N_f$.
- *The direction.* $b_0>0$, so the coupling falls as the scale rises: the primordial phase is asymptotically free, and it is weakest where the corpus needs it, at the transition.
- *The numbers.* $\alpha_4(M_X)=0.058$, $\alpha_4(M_{P})=0.0165$, and the pole at $885\ \mathrm{MeV}$ that lies far below the transition and therefore outside the theory's claim.
- *The ledger.* The value is imported; the coefficient is computed; the running is computed; the pole is a boundary of the description and not a prediction.
- *The diagnostic.* The scalar term depends on which scalar the model has, so $b_0$ reads the scalar content: the Hermitian matrix gives $\tfrac{26}{3}$, a complex one would give $8$, a matrix with a two-valued label would give $\tfrac{20}{3}$, and each doubling of the count costs more than the two-loop term the article omits.

**What the article does not do.** It does not compute the two-loop coefficient, the matching beyond leading order, or the anomalous dimensions of the matter fields. Each is named where it would enter and none is attempted.

## Conventions

**The group and the coupling.** $g_4$ multiplies every one of the fifteen generators in the single covariant derivative $D_{\imath}=\partial_{\imath}-ig_4\sum_{a=1}^{15}A_{a,\imath}t_{a}$, with $t_{a}$ Hermitian and $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ fixed as in *The Lagrangian and the Primordial Force*. **The $i$ in the derivative and the Hermiticity are one convention**: the printed arrays $G_{a}$ of the boson block are anti-Hermitian, and $t_{a}=iG_{a}/\sqrt{2\operatorname{tr}(G_{a}^{\dagger}G_{a})}$ is what makes the kinetic term canonical, and §*The Normalisation* of the parent article is where the passage is made. **The normalisation matters here and only here**: it is what makes the coefficient below a number rather than a rescaling.

**The expansion parameter.** $\alpha_4=g_4^{2}/4\pi$, so that $\alpha_4=\alpha_s$ at the matching scale and the two symbols carry one number there.

**The coefficient's convention.** $b_0$ is defined by

$$
\beta_{g_4}=\mu\frac{dg_4}{d\mu}=-\frac{g_4^{3}}{16\pi^{2}}b_0 ,
\qquad\text{equivalently}\qquad
\mu\frac{d\alpha_4}{d\mu}=-\frac{b_0}{2\pi}\alpha_4^{2} ,
$$

**the same convention QCD's article uses**, so that the number $\tfrac{26}{3}$ below can be set beside $11-\tfrac23N_f$ without a conversion.

**The mass scale.** $M_X^{2}=16g_4^{2}v_C^{2}$ with $Ξ_0=v_CD$, and $M_X\gtrsim3.7\times10^{-5}\ \mathrm{J}$, which is $2.3\times10^{5}\ \mathrm{GeV}$ or $230\ \mathrm{TeV}$; the conversion is $1\ \mathrm{J}=6.24\times10^{9}\ \mathrm{GeV}$ and it is used once, here. **Every number below uses $M_X=3.73\times10^{-5}\ \mathrm{J}$**, the row of the coupling article's table that sits at the $K_L\to\mu e$ limit, and the choice is the conservative one: a larger $M_X$ gives a smaller $\alpha_4$ and a weaker phase.

**The scale above.** $M_{P}=1.22\times10^{19}\ \mathrm{GeV}$ is used only as a far end at which to evaluate the solution. **No claim is made that the primordial phase survives to it**, and §*The Pole Below the Transition* says what would end it.

## The Coupling the Model Has, and What It Is Not

**$g_4$ is one number for the whole group.** Three consequences follow and each is a departure from what a reader expects:

- *No ratio to fix.* With one coupling there is no $\alpha_1/\alpha_2$ to match and no unification condition to impose; the matching at $M_C$ is a set of equalities among derived couplings and not a constraint on $g_4$.
- *No free parameter in the connection.* The value enters every vertex and every rate, so a measurement of any one of them fixes it. The corpus uses $K_L\to\mu e$, because it is the one channel the model predicts at tree level with no unknown matrix beyond the generation entries.
- *Nothing for it to protect.* $\rho=1$ at tree level is unaffected by the value of $g_4$ and is not a relation among couplings; it is a property of the scalar sector, and [The Custodial Symmetry and the $\rho$ Parameter](custodial-symmetry-and-the-rho-parameter.html) owns that argument and states what it does and does not establish.

**The value is imported, and the import is not a derivation.** $\alpha_s(M_X)$ is obtained by running the measured $\alpha_s(M_Z)=0.1179$ up through the Standard Model's content. **That running uses the strong sector's own coefficient and not $\mathrm{SU}(4)$'s**, so the identification $g_4^{2}=4\pi\alpha_s(M_X)$ is a matching statement: it says the two theories are the same theory at $M_X$. **The corpus imposes it at $M_X$ while a strict matching is at $M_C$**, and the two differ by one interval of running.

**How large the difference is.** Between $M_C$ and $M_X$ the strong coupling runs with $b_0=7$ at six flavours and the primordial coupling with $b_0=\tfrac{26}{3}$, so the two inverse couplings separate by

$$
\Delta\Bigl(\frac{1}{\alpha}\Bigr)=\frac{\tfrac{26}{3}-7}{2\pi}\ln\frac{M_X}{M_C}=0.265\,\ln\frac{M_X}{M_C} .
$$

**The size, in three cases.** At the corpus's own pair, $M_X=2.33\times10^{5}\ \mathrm{GeV}$ and $M_C=2.5\times10^{5}\ \mathrm{GeV}$, $\lvert\ln(M_X/M_C)\rvert=0.071$, so the shift is $0.019$ against $1/\alpha_4\approx17.2$, a tenth of a per cent. **For a factor of two it is $0.18$, or one per cent**, and for $M_C$ a decade above $M_X$ it is $0.61$, or $3.5$ per cent. **The sign is not fixed, because the ordering of the two scales is not**: the first two cases are smaller than the two-loop term the article omits and the third is comparable to it. The corpus's choice of scale is therefore consistent with its own truncation, and it is stated here so that no later article has to guess which scale the identification uses.

## The Coefficient Above $M_C$

**One formula, three contributions, and the answer is a simple fraction.**

$$
b_0=\frac{11}{3}C_{A}-\frac{4}{3}T_{R}N_{f}-\frac{1}{6}T_{S}n_{s} ,
$$

with $C_{A}=N=4$ for $\mathrm{SU}(4)$, $T_{R}=\tfrac12$ for a fundamental fermion, $N_{f}$ the number of Dirac fermions, and $T_{S}n_{s}$ the total Dynkin index of the scalars counted as **real** fields, $n_{s}=1$ for the one real adjoint. **The three terms are the connection's antiscreening, the fermions' screening, and the scalars' screening**, in that order and with that sign pattern.

| contribution | what counts | the count | its term in $b_0$ |
|---|---|---|---|
| the fifteen connections | $C_{A}=4$ | $1$ adjoint | $+\tfrac{44}{3}=+14.667$ |
| the sixteen Weyl fields | $N_{f}=8$ Dirac | $2\cdot\mathbf4\oplus2\cdot\bar{\mathbf4}$ | $-\tfrac{16}{3}=-5.333$ |
| the scalar | $T_{S}=4$ | $\mathbf{15}\oplus\mathbf1$, sixteen real | $-\tfrac{2}{3}=-0.667$ |
| **total** | | | $\mathbf{\tfrac{26}{3}=8.667}$ |

**Why the fermion count is eight and not sixteen.** A Weyl field contributes half a Dirac field's screening, and the sixteen Weyl fields are eight Dirac fields once the copies are paired. **The pairing is exact above $M_C$**, because the content is vector-like there and a Dirac field is what a pair of conjugate Weyl fields is. The count is explicit: the content is $2\cdot\mathbf4\oplus2\cdot\bar{\mathbf4}$, so the two quartets and the two antiquartets pair as $2\times(\mathbf4+\bar{\mathbf4})=8$, each Dirac field being one $\mathbf4$ Weyl field and one $\bar{\mathbf4}$ Weyl field. **Below $M_C$ the count changes** and the same sixteen fields are counted with the Standard Model's hypercharges; that running is the coupling article's and not this one's.

**Why the scalar term is two thirds.** The scalar is $\mathbf{15}\oplus\mathbf1$ in the indices, so its Dynkin index is that of the adjoint, $T_{S}=C_{A}=4$, plus the singlet's zero:

$$
\tfrac16 T_{S}n_{s}=\tfrac16\times\bigl(\underbrace{4}_{\mathbf{15}}+\underbrace{0}_{\mathbf1}\bigr)=\tfrac{2}{3} .
$$

**The weight is one sixth and not one third because the field is real.** $Ξ$ is Hermitian, so its sixteen components are sixteen real fields and not eight complex ones; a complex multiplet would enter at $-\tfrac13T_S$ per unit of Dynkin index, which is twice the screening of a real one. **The formula's $n_s$ counts real scalars for exactly that reason**, and [The Heavy Sector Below Its Threshold](the-heavy-sector-below-its-threshold-decoupling-matching-and-the-one-loop.html) states the coefficient in precisely this form, with $n_s$ the number of real scalars.

**There is no second index to multiply by.** $Ξ$ is a Hermitian matrix with a lower and an upper index and nothing else: sixteen real components, fifteen of them the adjoint and one the trace. **A count that doubles this — a complex matrix, or a matrix with a label no generator acts on — is counting components the algebra does not have**, and the row below shows what that does to $b_0$.

**The scalar term is the one term that reads the model's content, and it reads it sharply.** The three candidate scalar sectors give three coefficients:

| scalar sector | real components | $T_{S}n_{s}$ | scalar term | $b_0$ |
|---|---|---|---|---|
| the Hermitian $\mathbf{15}\oplus\mathbf1$, the model's | $16$ | $4$ | $-\tfrac23$ | $\tfrac{26}{3}=8.667$ |
| a complex $\mathbf{15}\oplus\mathbf1$ | $32$ | $8$ | $-\tfrac43$ | $8$ |
| a complex matrix with a two-valued label | $64$ | $16$ | $-\tfrac83$ | $\tfrac{20}{3}=6.667$ |

**Each doubling of the scalar count doubles the scalar term**, by $\tfrac23$ and then by another $\tfrac43$, and the table is the shortest statement of why the count has to be right: the running, the pole and the Planck-scale value all move with it. **The first row is the algebra's count**: $\mathbf{15}\oplus\mathbf1$ is $15+1=16$ real, and $15=\dim\mathrm{SU}(4)$.

**Set beside QCD.** $b_0^{\mathrm{QCD}}=11-\tfrac23\times6=7$ at six flavours. **The primordial coefficient is larger by $\tfrac53$**, and the arithmetic is transparent: $\tfrac{11}{3}\times4$ against $\tfrac{11}{3}\times3$ gains $\tfrac{11}{3}=3.667$, while the extra matter — two more Dirac fields, eight against six, costing $\tfrac43$, and the scalar, costing $\tfrac23$ — subtracts $2$, netting $+\tfrac53=1.667$. **A larger coefficient means a faster approach to freedom**, and the difference is one part in five.

### What the Coefficient Does Not Read

**Three quantities the representation decides and $b_0$ does not see.**

- *How the connection acts on $Ξ$*: the commutator $[T_{a},Ξ]$, fixed by the matrix index, and not a multiplication.
- *How many directions are eaten at $M_C$*: six, one per broken generator of $\mathrm{SU}(4)$.
- *How many components survive*: ten, of which eight are a octet.

**All three are the scalar articles' and none of them enters the running.** This article computes the coefficient, states which content it counts, and cites the census for everything else.

## The Solution, and the Numbers

**The one-loop solution is a straight line in the inverse coupling.**

$$
\frac{1}{\alpha_4(\mu)}=\frac{1}{\alpha_4(M_X)}+\frac{b_0}{2\pi}\ln\frac{\mu}{M_X} ,
\qquad
\frac{b_0}{2\pi}=\frac{26/3}{2\pi}=\frac{26}{6\pi}=1.379 .
$$

**The starting value.** With $g_4^{2}=0.730$ at $M_X=3.73\times10^{-5}\ \mathrm{J}$,

$$
\alpha_4(M_X)=\frac{0.730}{4\pi}=0.0581 ,
\qquad
\frac{1}{\alpha_4(M_X)}=17.21 .
$$

**Three evaluations, and what each one is for.**

| scale | $\mu$ in GeV | $1/\alpha_4$ | $\alpha_4$ | $g_4^{2}$ |
|---|---|---|---|---|
| $M_X$, the matching point | $2.3\times10^{5}$ | $17.21$ | $0.0581$ | $0.730$ |
| a decade above | $2.3\times10^{6}$ | $20.39$ | $0.0490$ | $0.616$ |
| the Planck scale | $1.22\times10^{19}$ | $60.79$ | $0.0165$ | $0.207$ |

**Every entry is the line evaluated, not a fit.** The slope between any two rows is $1.379$, and the fall from $0.058$ to $0.0165$ over fourteen decades is the whole content of the coefficient.

**Going down instead of up, and why the table stops at $M_X$.** The same line continued downward gives a *larger* coupling, and at $1\ \mathrm{TeV}$ it gives $\alpha_4=0.103$ — **a forbidden extrapolation, quoted only to show the direction, because below $M_C$ the group is not $\mathrm{SU}(4)$ and the coefficient is the Standard Model's.** The line is drawn only where the phase it belongs to exists.

## What the Running Says About the Phase

**Four statements, and each is a number rather than a slogan.**

- *The phase is weakly coupled at the transition.* $\alpha_4(M_X)=0.058$, so $\alpha_4/\pi=0.018$ and the one-loop expansion is good to a few per cent. **The two-loop term is about two per cent of the change**: one loop misses two by ten per cent at $\alpha_s\approx0.3$, the relative size scales as $\alpha$, and $10\%\times0.058/0.3\approx2\%$. **This is what makes the tree-level rates of the Feynman-rules article legitimate**, and it is the reason no resummation appears anywhere in the primordial block.
- *The phase is asymptotically free.* $b_0=\tfrac{26}{3}>0$, so $\alpha_4\to0$ as $\mu\to\infty$. The primordial force does not grow at short distances, and no Landau-pole cosmology is available to it: an asymptotically free sector cannot be strongly coupled in the early universe, so it can drive neither a confining transition nor a thermal relic abundance through its own connection interactions.
- *The coupling is weakest where the content is heaviest.* Antiscreening wins because the matter above $M_C$ is more than the Standard Model's per connection, and the coupling at $M_P$ is under a third of its value at $M_X$. **A unified description at a high scale would therefore be a weakly coupled one**, which is the opposite of the strong-coupling picture a GUT without asymptotic freedom would need.
- *Nothing confines, and the coefficient is why.* A confining phase needs the coupling to grow at long distances; here it grows downward only, and the phase ends at $M_C$ before the growth matters. **This is the quantitative half of *Why There Is No Confinement Above $M_C$***, which supplies the mechanism and cites this article for the number.

**What the running does not say.** It does not say that the three Standard Model couplings meet. **They do not, and the meeting is not a goal of the model**: $g_4$ is one number and the three below $M_C$ are derived from it by the matching relations, so a "unification" statement would be a statement about the matching and not about a crossing of lines. The corpus's coupling article draws the same distinction from the other side.

## The Pole Below the Transition

**Extending the line downward, $1/\alpha_4$ vanishes at a finite scale.**

$$
\ln\frac{\mu_{\mathrm{pole}}}{M_X}=-\frac{1}{\alpha_4(M_X)}\frac{2\pi}{b_0}
=-\frac{17.21}{1.379}=-12.48 ,
\qquad
\mu_{\mathrm{pole}}=885\ \mathrm{MeV} .
$$

**The pole is real arithmetic and not a physical object.** Three sentences fix its status:

- *It lies below $M_C$.* $M_C\gtrsim2.5\times10^{5}\ \mathrm{GeV}$ by the leptoquark bound, five and a half decades above the pole.
- *Below $M_C$ the coefficient is neither $\tfrac{26}{3}$ nor constant.* It is the Standard Model's, $7$ with six flavours and $5$ with five, and the line of this article is not the line the theory follows.
- *So the pole is a boundary of the description.* It marks where the primordial phase would become strong if it were extended, and the theory does not extend it. **It is the same kind of object as the Landau pole of QED, which the asymptotic-freedom article puts at $1.6\times10^{270}\ \mathrm{J}$**: a zero of a one-loop line, at a scale the truncation abandoned long before. **It is not the same kind of object as QCD's coupling reaching order one at $0.111\ \mathrm{GeV}$**: that one is physical, because the strong sector confines and the scale measures it, and nothing here does.

**What would be wrong is to read the pole as a prediction of new physics.** A confining or strong-coupling regime at $885\ \mathrm{MeV}$ is excluded by the Standard Model's own success there, and the exclusion is a statement that the primordial phase has already ended, not a tension in the model.

## What Is Imported and What Is Computed

**Four lines, and the gradings differ.**

| statement | status |
|---|---|
| $g_4$ has one value for all fifteen generators | structural, from the single covariant derivative |
| $g_4^{2}=4\pi\alpha_s(M_X)$ | imported, a matching to measured data |
| $b_0=\tfrac{26}{3}$ | computed, from the content and the group |
| $\alpha_4(M_P)=0.0165$ | computed, one logarithm from the imported value |
| the pole at $885\ \mathrm{MeV}$ | computed arithmetic, with no physical reading |

**Only one line is data.** The article's claim is not that the primordial coupling is predicted; it is that, given the one imported number, everything else about the coupling above $M_C$ follows and nothing else is free. **That is the difference between a coupling and a parameter**, and it is the sense in which the model has one of the first and not one of the second.

## The Checks

**Eleven numbers, each recomputed.**

| statement | value |
|---|---|
| $C_{A}$ for $\mathrm{SU}(4)$ | $4$ |
| the adjoint term $\tfrac{11}{3}C_{A}$ | $14.667$ |
| the fermion term $\tfrac43T_{R}N_{f}$ with $N_{f}=8$ | $5.333$ |
| the scalar Dynkin index, $\mathbf{15}+\mathbf1$ | $4+0=4$ |
| the scalar term $\tfrac16T_{S}n_{s}$ with $n_{s}=1$ real adjoint | $0.667$ |
| $b_0=\tfrac{44}{3}-\tfrac{16}{3}-\tfrac{2}{3}$ | $\tfrac{26}{3}=8.667$ |
| $b_0/2\pi$ | $1.379$ |
| $b_0$ against QCD's $7$ | larger by $\tfrac53$ |
| $1/\alpha_4(M_X)$ from $g_4^{2}=0.730$ | $17.21$ |
| $1/\alpha_4(M_P)$ at $1.22\times10^{19}\ \mathrm{GeV}$ | $60.79$ |
| $\mu_{\mathrm{pole}}$ | $885\ \mathrm{MeV}$ |

**The sum $14.667-5.333-0.667=8.667$ is the check that matters**, because each of the three terms is computed from a Dynkin index and a count rather than quoted. **The scalar term is the one that has changed** with the model's content, and the table of §*The Coefficient Above $M_C$* shows the three candidates side by side so that the difference is visible rather than asserted.

## Summary

The model has one connection coupling and this article computes what it does above $M_C$. **$b_0=\tfrac{26}{3}$**, from $\tfrac{44}{3}$ for the fifteen connections, $-\tfrac{16}{3}$ for the sixteen Weyl fields read as eight Dirac fields, and $-\tfrac23$ for the scalar, the last of which is the adjoint Dynkin index of a sixteen-component Hermitian multiplet taken at the weight of a real field.

**The running faces up.** $b_0>0$, so $\alpha_4$ falls from $0.0581$ at $M_X$ to $0.0165$ at the Planck scale, and the primordial phase is asymptotically free and weakly coupled everywhere it exists. **That is what makes the tree-level rates of the block legitimate and what forbids a confining primordial phase.**

**The coefficient is a diagnostic of the scalar sector.** Sixteen real components give $\tfrac{26}{3}$; a complex matrix doubles the term and gives $8$; a further label doubles it again and gives $\tfrac{20}{3}$. **Each doubling doubles the scalar term**, by $\tfrac23$ and then by $\tfrac43$, which is larger than the two-loop term the article omits, so the scalar count is not decoration in this section.

**The value is imported and the running is computed.** $g_4^{2}=4\pi\alpha_s(M_X)$ is a matching to measured data; the coefficient, the solution and the numbers are not. **The import is exact at $M_X$ and approximate as a matching at $M_C$**, by a tenth of a per cent at the corpus's own pair of scales and by one per cent for a factor of two between them, which is far inside the truncation the article already declares.

**The Landau pole at $885\ \mathrm{MeV}$ is arithmetic and not physics.** It lies five and a half decades below $M_C$, where the coefficient is the Standard Model's and the line of this article is not the line the theory follows.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $g_4$ | The primordial coupling, one value on the fifteen generators |
| $\alpha_4$ | $g_4^{2}/4\pi$; equal to $\alpha_s$ at the matching scale |
| $b_0$ | One-loop coefficient, $b_0=\tfrac{11}{3}C_{A}-\tfrac43T_{R}N_{f}-\tfrac16T_{S}n_{s}$ |
| $C_{A}=4$ | Quadratic Casimir of the adjoint of $\mathrm{SU}(4)$ |
| $T_{R}=\tfrac12$ | Dynkin index of the fundamental, for a fermion |
| $T_{S}=4$ | Total scalar Dynkin index, $\mathbf{15}$ giving $C_{A}=4$ and $\mathbf1$ giving $0$ |
| $N_{f}=8$ | Dirac fermions, the sixteen Weyl fields paired |
| $n_{s}=1$ | Real scalar multiplet, the Hermitian $\mathbf{15}\oplus\mathbf1$ of sixteen real components |
| $M_X$ | The leptoquark scale, $\gtrsim3.7\times10^{-5}\ \mathrm{J}=2.3\times10^{5}\ \mathrm{GeV}$ |
| $M_C$ | The transition scale, above the leptoquark bound |
| $M_{P}$ | $1.22\times10^{19}\ \mathrm{GeV}$, used only as a far end |
| $\mu_{\mathrm{pole}}$ | $885\ \mathrm{MeV}$, the zero of the extended one-loop line |
| $\zeta$ | The fixing parameter of the corpus's propagators; absent from everything in this article, which needs no fixing the representative |

## Further Reading

- [The One Coupling That Returns the Standard Model](the-one-coupling-that-returns-the-standard-model.html). The boundary condition, the $\tfrac38$ arithmetic, and the $K_L\to\mu e$ bound that fixes $M_X$.
- [The $\mathrm{SU}(4)$ Model: Four Lines, Fifteen Generators, Rank Three](the-su4-model-four-lines-fifteen-generators-one-declaration.html). The content whose Dynkin indices the coefficient counts.
- [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html). The action the coupling multiplies, and the normalisation $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ this article assumes.
- [Asymptotic Freedom and the Running of the Strong Force](asymptotic-freedom-and-the-running-of-the-strong-coupling.html). The same line for $\mathrm{SU}(3)$, whose coefficient $11-\tfrac23N_f$ this article's $b_0=\tfrac{26}{3}$ is set beside, and the QED Landau pole this article's pole is compared to.
- [Why There Is No Confinement Above $M_C$](why-there-is-no-confinement-above-m-c.html). The mechanism, which cites this article for the number.
- [The Scalar Content](the-scalar-content-one-matrix-and-ten-survivors.html). The census that fixes the scalar content the coefficient counts, and the article that establishes the multiplet is one Hermitian matrix and not a complex one.
- [The Custodial Symmetry and the $\rho$ Parameter](custodial-symmetry-and-the-rho-parameter.html). What $\rho=1$ does and does not rest on here, which is a statement about the scalar sector and not about $g_4$.
- [The Threshold Scales: $M_C$, $M_W$ and What Would Fix Them](the-threshold-scales-mc-mw-and-what-would-fix-them.html). The free scale this article takes from the leptoquark bound.
