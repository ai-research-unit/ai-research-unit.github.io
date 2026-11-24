# __The Excitation Ladder Theory of Flavour__

*Ledger note.* Every mass, lifetime and ratio in this article is measured data, transcribed from the Particle Data Group and marked as data where it is used. No coupling statement is made here; the corpus's single scale-bearing coupling statement lives in [The One Coupling That Returns the Standard Model](the-one-coupling-that-returns-the-standard-model.html). What is tested is exact arithmetic on measured numbers, and the verdicts are stated as verdicts.

## Introduction

This article classifies nothing. It states one hypothesis about why the fermions come in three copies, and what that hypothesis does and does not explain. The classification of one generation is finished elsewhere, in [Particle Classification: Three Grids, One Name in Every Cell](particle-classification-three-grids-one-name-in-every-cell.html). That article names the sixteen cells, the twenty-one bosons and the twelve surviving scalars, and it says nothing about flavour. The separation is deliberate: the classification states a structure, flavour states a spectrum, and a nomenclature that absorbs both stops being a nomenclature.

The hypothesis is that there are no elementary particles, only fields and their levels of combined excitation. Flavour 1 is the ground level, flavour 2 the first combined level, and flavour 3 the second. The ladder has three rungs: the three copies are the whole of it, and there is no fourth.

The ontology is not new. Quantum field theory already holds that a particle is a pole of a propagator, that fields are primary, and that no object has a measured radius. What is new is only the second clause, that the flavours are rungs of a single tower, so that rung $n+1$ is built from the same medium as rung $n$. Everything below tests that clause and nothing else.

The verdict can be given first. The ladder fails if its rungs are counted in mass. It works if they are counted in the square root of the mass: the steps then grow by a constant factor, and three rungs follow from two numbers. That is a reading of the spacings and no derivation of them, and the two are kept apart throughout.

## Flavour Is a Level, Not a Charge

The claim rests on a fact the classification article established. The fermions of one generation form a module of the algebra, and the tripling is a tensor product with a space on which the algebra acts trivially:

$$
\mathbf{16}\;\longrightarrow\;\mathbf{16}\otimes\mathbb C^{3},
\qquad
\tilde Q\cdot(Ξ_{\mathrm{wfn}}\otimes f)=(\tilde Q\cdotΞ_{\mathrm{wfn}})\otimes f .
$$

Every operator the model builds from the group is therefore the same operator on every rung, $Q\otimes\mathbb 1_3$ and $T_3\otimes\mathbb 1_3$. No measurement of charge, colour, weak isospin or $B-L$ can distinguish one rung from another. Flavour cannot be a charge, and it must therefore be a quantity a spectrum produces: an energy, a mass, a level spacing.

There is a second reason to expect the rungs of a tower to be ordered rather than equivalent. A level decays only if a lower level exists with the same quantum numbers and enough phase space. Rung 1 is the bottom of its tower, so there is no lower rung to fall to, and it is stable by conservation rather than by accident. This is why $e$, $u$, $d$ and $\xi_{\mathrm{neu},e}$ sit at the top of their rows in the classification article: they are the ground states, and nothing beneath them carries their charges. No new dynamics is needed to stabilise rung 1, and none is claimed.

One word is used in a fixed sense. A resonance here means a pole of the propagator, not a geometric singularity. A rung is a pole with a real part and, above rung 1, a width.

## The Ladder Fails in Mass

A tower has a spacing, and the quantity to test is the step between consecutive rungs. For the charged leptons the two steps are

$$
\frac{m_\mu}{m_e}=206.77,
\qquad
\frac{m_\tau}{m_\mu}=16.82 .
$$

The step shrinks by a factor $12.3$. A geometric tower requires the steps to be equal; a tower of equal quanta requires the masses in integer ratio, $1:2:3$. Neither holds.

| the ladder in mass | predicted | measured | verdict |
|---|---|---|---|
| geometric, equal steps | $m_3/m_2=m_2/m_1$ | $16.82$ against $206.77$ | fails by $12.3$ |
| integer quanta, $1:2:3$ | $2$ and $3$ | $207$ and $3477$ | fails by $10^{2}$ and $10^{3}$ |

The naive form of the theory is therefore excluded, and it is worth saying so in its own section rather than burying it. A theory that survives must not count rungs in mass.

The corpus's own algebra gives an independent warning. The biquaternion algebra is a field-first framework with a module and spin structures, and it has no dispersion relation. It cannot produce a ladder in any variable, because a ladder is dynamics and the algebra is kinematics. That is the same reason the corpus cannot count generations, recorded as a negative result in [The Number of Generations and the Biquaternion Algebra](the-number-of-generations-and-the-biquaternion-algebra.html).

## The Ladder Works in the Square Root

Take the square root of the mass ratios, with rung 1 as the unit. Writing

$$
\rho_i:=\frac{m_i}{m_1},
$$

the ratio has $\rho_1=1$ and carries no unit anywhere. The ladder's variable is its root, $\sqrt{\rho_i}$, and the charged leptons give

$$
\sqrt{\rho_2}=14.379,\qquad \sqrt{\rho_3}=58.968 .
$$

The steps in the square root grow where the steps in mass shrank:

$$
14.379-1=13.379,
\qquad
58.968-14.379=44.589,
\qquad
\frac{44.589}{13.379}=3.3326 .
$$

The consecutive mass ratios fall by $12.3$; the steps in the square root grow by $3.3326$, which is $10/3$ to $0.02$ per cent. The second is the statement in which the two steps are comparable in size.

| variable | first value | second value | the change |
|---|---|---|---|
| $m_{i+1}/m_i$ | $206.77$ | $16.82$ | shrinks by $12.3$ |
| $\Delta\sqrt{m_i/m_1}$ | $13.379$ | $44.589$ | grows by $3.3326$ |
| $\Delta\ln(m_i/m_1)$ | $5.332$ | $2.822$ | shrinks by $1.889$ |

No column is constant, so the ladder is not an equal-spacing tower in any of these variables. That is the honest reading, and it moves the question from the spacing to the count.

**The square root has a name in the coupling sector.** The mass of a fermion is its Yukawa coupling to the vacuum value, $y_f=\sqrt2\,m_f/v$, and the ratios above are the ratios of couplings, $\rho_i=y_i/y_1$, whose roots $\sqrt{\rho_i}$ are the rungs; a mass ratio is dimensionless, so its root is a number and not a half power of a unit. No wave equation enters their definition. The variable is chosen because the two steps are then in a constant ratio; that is a property of the measured spectrum and not a derivation.

## Koide's Relation, Stated

Koide's relation, stated in 1981 for the charged leptons and not derived since, is a statement about two mass ratios and nothing else. Dividing numerator and denominator by $m_1$ turns every mass into a ratio to $m_1$ and every root into the root of that ratio, a dimensionless number; what remains is a function of two numbers. Writing

$$
\rho_2:=\frac{m_2}{m_1},\qquad \rho_3:=\frac{m_3}{m_1},
$$

the relation is

$$
Q=\frac{1+\rho_2+\rho_3}{\left(1+\sqrt{\rho_2}+\sqrt{\rho_3}\right)^{2}}=\frac{2}{3}.
$$

With the PDG masses $m_e=0.510\,998\,95$ MeV, $m_\mu=105.658\,375\,5$ MeV and $m_\tau=1776.86$ MeV, the two ratios, their roots and the ratio are

| quantity | value |
|---|---|
| $\rho_2=m_\mu/m_e$ | $206.768\,28$ |
| $\sqrt{\rho_2}$ | $14.379\,44$ |
| $\rho_3=m_\tau/m_e$ | $3477.228\,28$ |
| $\sqrt{\rho_3}$ | $58.968\,03$ |
| $1+\rho_2+\rho_3$ | $3684.996\,56$ |
| $\left(1+\sqrt{\rho_2}+\sqrt{\rho_3}\right)^{2}$ | $5527.545\,88$ |
| $Q$ | $0.666\,660\,51$ |

The measured $Q$ falls below $\tfrac23$ by $6.2\times10^{-6}$ in absolute value, which is $9.2$ parts per million of $\tfrac23$, on two measured ratios. Nothing in the display carries a unit: every quantity in it is a quotient of two masses, which is why the choice of mass unit or mass standard cancels.

**Why it is stated here.** The variable of this article is the square root of the mass ratio, $\sqrt{\rho_i}$ with $\rho_1=1$, so Koide's ratio is written in the ladder's own variable:

$$
Q=\frac{1+\rho_2+\rho_3}{(1+\sqrt{\rho_2}+\sqrt{\rho_3})^{2}}=\frac13\left(1+\left(\frac{\sigma}{\mu}\right)^{2}\right),
$$

with $\mu$ the mean of the three $\sqrt{\rho_i}$ and $\sigma$ their standard deviation. The bracket is an identity and not a fit, so $Q=\tfrac23$ is exactly the statement $\sigma/\mu=1$: the three roots are as spread as their own mean. The measured spread is $0.999\,990\,8$, not $1$ by $9\times10^{-6}$, and the same number read as an angle, $\arccos\left(1/\sqrt{3Q}\right)$, is $44.9997^{\circ}$.

**Why it is not evidence for the ladder.** The ladder sets an interval between neighbouring rungs and places no condition on a combination of the three masses, so Koide's relation is neither derived here nor used here. It is a measured arithmetic on three numbers, and the corpus records it as one. The numeral $\tfrac23$ also appears in the model as a trace ratio of one to three, in [Charge Quantisation from the Fourth Colour](charge-quantisation-from-the-fourth-colour-one-trace-one-third.html), and the two are not the same statement: one is a dimension of a representation and the other a ratio of masses. That they coincide in value is recorded and not explained.

## No Exact Closure

**The square-root ladder fixes spacings and predicts no sum, so this article claims no exact numerical closure.** A ladder sets the interval between neighbouring rungs. It places no condition on a combination of three masses. Koide's relation, stated above, is the sharpest case of such a combination: two measured ratios land near a simple fraction, the ladder neither derives it nor uses it, and it is not counted here as evidence.

**What the ladder gives is the growth of the steps and the count.** The two steps in the square root are $13.379$ and $44.589$, a growth of $3.3326$, and that growth is a property of the two spacings and of nothing else. *The Count Is Three* takes the count as measured. Those are the two things this article offers, and it stops there.

No mass and no scale is predicted. The arithmetic on the spacings and the fits that fix the count for the charged leptons are kept in [Flavour Research: The Ladder Arithmetic](../articles_internal/flavour-research.html), so that this article carries the idea and not its calculus.

## The Count Is Three

The ladder has three rungs, and the theory takes the count from the data. This is where the name comes from, and where the theory is most exposed.

A count costs no parameter: a tower of three rungs is described by two numbers, a scale and a starting phase, so the three rungs contain one prediction, and nothing is fitted.

Three is what the data answer. Three rungs reproduce the three measured masses, and every shorter count fails outright. No fourth rung can be added, because a closed ladder does not grow upward: extra rungs are squeezed between the ones already present, so a fourth rung would have to sit in a region already searched and already empty.

The bounds agree, and they agree on three:

| bound | value | what it constrains |
|---|---|---|
| $Z$ invisible width | $N_{\xi_{\mathrm{neu}}}=2.984\pm0.008$ | light neutrinos with standard couplings |
| big-bang nucleosynthesis | $N_{\mathrm{eff}}\approx3$ at $1.16\times10^{13}$ K | rungs light and coupled at $1.16\times10^{13}$ K |
| $H\to gg$, $H\to\gamma\gamma$ | matches three | families at any mass |
| direct search | none below about $1.6\times10^{-7}$ J | new charged or coloured states |

A fourth family is excluded at any mass and not only at low mass, because it does not decouple: the Yukawa grows with the mass, so its contribution to $H\to gg$ and $H\to\gamma\gamma$ approaches a constant, and the measured Higgs rates match three.

The same reading is taken for every tower. The count is three, it is a property of the measured spectrum, and nothing in the picture admits a fourth.

## The Early Universe

A medium at temperature $T$ populates a rung of mass $m$ by the Boltzmann factor,

$$
\frac{n_2}{n_1}=e^{-(m_2-m_1)/T},
$$

so the upper rungs are rare when the bath is cold and common when it is hot. For the charged leptons:

| $T$ | $n_{\imath}/n_e$ | $n_\tau/n_e$ |
|---|---|---|
| $2.32\times10^{10}$ K | $0$ | $0$ |
| $5.80\times10^{11}$ K | $0.122$ | $3.7\times10^{-16}$ |
| $1.16\times10^{12}$ K | $0.349$ | $1.9\times10^{-8}$ |
| $1.76\times10^{12}$ K | $0.501$ | $8.4\times10^{-6}$ |
| $5.80\times10^{12}$ K | $0.810$ | $2.9\times10^{-2}$ |
| $1.16\times10^{13}$ K | $0.900$ | $0.169$ |
| $2.97\times10^{13}$ K | $0.960$ | $0.500$ |
| $1.16\times10^{14}$ K | $0.990$ | $0.837$ |

Heavy rungs are rare and hot baths light them. That is not a hypothesis but the measured thermal history of the universe in inverse mass order: cooling removes the heavy rungs first.

Two corrections keep the reading honest. The ratio approaches parity and never passes it, so the bath stops penalising a heavy rung without ever favouring it. And detailed balance forbids accumulation, since the same agitation that builds a rung destroys it; exceeding equilibrium needs a conserved charge, a chemical potential, or a departure from equilibrium, and all three are compatible with a rung that is an elementary field.

One thing temperature cannot do is change the count. At every temperature above $2.32\times10^{10}$ K there are three generations. Temperature decides how many rungs are lit, never how many exist.

## What the Theory Owes

Three debts remain, and the theory is incomplete until they are paid.

The first is a dispersion relation. A medium has $\omega(k)$, and a tower is the eigenvalue problem of that relation; without one the spectrum is undefined and the rung count is not a well-posed question. The second is a composition rule that produces the constant step from its own structure and explains why the rungs are equally spaced in phase. The third is a width rule: *Flavour Is a Level, Not a Charge* settles rung 1 by conservation, and the theory must also say why rungs 2 and 3 have the widths they have, which for the charged leptons is the fifth-power law of [An Introduction to Flavour](an-introduction-to-flavour.html).

The corpus supplies exactly the ontology this theory wants, and none of the dynamics. The biquaternion algebra is field-first: a module, spin structures, no points. It has no dispersion relation, because it is kinematics. The first debt is therefore one the corpus cannot pay, and claiming otherwise would be the one unrecoverable error available here.

What the theory does not owe is a derivation of three. Three is what the charged-lepton tower measures; the count is an input, and a theory that owed three would have assumed its own answer.

## The Ledger

| item | status |
|---|---|
| why flavour is not a charge | explained by the model's structure, *Flavour Is a Level, Not a Charge* |
| why rung 1 is stable | explained by conservation, *Flavour Is a Level, Not a Charge* |
| why the naive mass ladder fails | quantified, *The Ladder Fails in Mass* |
| the square-root variable | chosen because the two steps are then in the ratio $10/3$; not derived, *The Ladder Works in the Square Root* |
| an exact numerical closure | none claimed, *No Exact Closure* |
| Koide's relation | stated, measured, not derived, *Koide's Relation, Stated* |
| why this tower counts three | measured, not derived, *The Count Is Three* |
| why no fourth rung is added | the ladder is closed, *The Count Is Three* |
| a derivation of the square-root step | absent |
| a derivation of the scale and phase | absent |
| a derivation of any quark mass | absent |

The square-root ladder reproduces the spacings of one tower and derives nothing further. What the theory adds is the count: rungs of one tower, spaced in the square root of the mass ratio, with the count fixed by measurement and not by principle.

The scope is equally plain. The quantum numbers of one generation are derived, in the classification article. The three copies and every flavour-breaking parameter are input, here. The theory adds a reading of the second and not a derivation of it.

## Falsification

One statement would end the theory as written, and one would confirm it.

A fourth family would end it, and that one is already excluded. The ladder is therefore a ladder of a medium and not of chiral families: it carries three rungs, and the exclusion of a fourth is a measured fact rather than a prediction of the theory.

A deviation from QED in $e^+e^-\to\mu^+\mu^-$ would confirm a medium, since a structure of size $1/\Lambda$ gives

$$
\sigma=\sigma_{\mathrm{QED}}\left(1+O\!\left(\frac{s}{\Lambda^{2}}\right)\right),
$$

and present data put $\Lambda>1.6\times10^{-6}$ J. Continued absence of such a signal pushes the structure out of reach and leaves the theory indistinguishable from three fields with three masses.

## Checks

Every number below was recomputed from the measured masses before it was written.

| claim | check | result |
|---|---|---|
| the mass step, first | $105.658/0.511$ | $206.77$ |
| the mass step, second | $1776.86/105.658$ | $16.82$ |
| the steps against a geometric ladder | $206.77$ against $16.82$ | shrinks by $12.3$ |
| the ladder against integer quanta | $2$ and $3$ | off by $207$ and $3477$ |
| the gaps in the square root | $14.379-1$, $58.968-14.379$ | $13.379$, $44.589$ |
| the step ratio in the square root | $44.589/13.379$ | $3.3326$, against $10/3$ by $0.02\%$ |
| the logarithmic steps | $\ln 206.77$, $\ln 16.82$ | $5.332$, $2.823$ |
| the thermal ratio at $1.76\times10^{12}$ K | $e^{-(m_\mu-m_e)c^2/k_BT}$ | $0.501$ |
| the thermal ratio at $2.97\times10^{13}$ K | $e^{-(m_\tau-m_e)c^2/k_BT}$ | $0.500$ |
| the width ratio against the fifth power | $1.3486\times10^{6}$ against $1.3451\times10^{6}$ | agrees to 0.26 per cent |
| Koide's ratio | $(1+206.768\,28+3477.228\,28)/(1+14.379\,44+58.968\,03)^{2}$ | $0.666\,660\,51$ against $2/3$ |
| Koide's spread | $\sigma/\mu$ from $\sqrt{\rho_i}$ | $0.999\,990\,8$ |
| Koide's angle | $\arccos(1/\sqrt{3Q})$ | $44.9997^{\circ}$ |

## Summary of Notation

| symbol | meaning |
|---|---|
| $\rho_i$ | the mass ratio of rung $i$ to rung 1; $\rho_1=1$, $\rho_2=206.768\,28$, $\rho_3=3477.228\,28$ |
| $\sqrt{\rho_i}$ | the root of that ratio, the ladder's variable; $1$, $14.379\,44$, $58.968\,03$ |
| $Q$ | Koide's ratio, $(1+\rho_2+\rho_3)/(1+\sqrt{\rho_2}+\sqrt{\rho_3})^{2}$, measured $0.666\,660\,51$ |
| $\mu$, $\sigma$ | the mean and the standard deviation of the three roots $\sqrt{\rho_i}$; $\sigma/\mu=1$ is Koide |
| the rung count | three for every tower, measured and not derived |
| $i=1,2,3$ | the rung index |
| rung | a level of combined excitation, a pole with a mass |

The letter $\rho$ carries the mass ratio in this article and is given the subscript of the rung it belongs to, so that it cannot be read for the charge density of the field articles or the number density $\rho_{\mathrm{num}}$ of the polar ones.

## Further Reading

- [An Introduction to Flavour: Mass, Lifetime, Decay Pattern, the Three Handles](an-introduction-to-flavour.html). The phenomena this article theorises, with no theory of them.
- [Particle Classification: Three Grids, One Name in Every Cell](particle-classification-three-grids-one-name-in-every-cell.html). One generation, sixteen cells, three grids, and no flavour.
- [The Number of Generations and the Biquaternion Algebra](the-number-of-generations-and-the-biquaternion-algebra.html). Why the algebra does not count them.
- [The Yukawa Sector: Fermion Mass Matrices and Their Diagonalisation](the-yukawa-sector-fermion-mass-matrices-and-their-diagonalisation.html). Where the mass matrix is written and why its eigenvalues are input.
- [The CKM Matrix and CP Violation in Biquaternionic Form](the-ckm-matrix-and-cp-violation-in-biquaternionic-form.html). The misalignment between the flavour basis and the mass basis.
- [Lepton Flavour in the Four-Colours Model: Nothing Turns the Lepton, and One Generation Matrix Decides the Channels](lepton-flavour-in-the-four-colours-model-nothing-turns-the-lepton.html). The operator's chiral structure, and the question of the generation matrix that the mass sector leaves open.
- [The Four Colours Left–Right Model: Four Colours, $21$ Generators, One Declaration](the-four-colours-left-right-model.html). The frame whose module the ladder multiplies.
