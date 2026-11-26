# __An Introduction to Flavour: Mass, Lifetime, Decay Pattern, the Three Handles__

*Ledger note.* Every mass and every lifetime in this article is measured data, transcribed from the Particle Data Group and marked as data where it is used. A mass is used here as an input and never as a prediction. The one exception is the arithmetic of *Lifetime: the One Relation Phase Space Computes*, which is ordinary phase space.

## Introduction

The classification of one generation is a closed list. Sixteen cells, one name per cell, one charge per row, and no room left for a question. The question arrives the moment a second copy is written beside the first, because the copy is identical in every column but one: the mass.

**A warning before the reader starts, because the vocabulary is the weak sector's.** This model has a two-valued copy index and no generation label: **its sixteen fields are eight, counted twice, and the copy index is the weak-doublet slot.** The three-column table below is measured data and describes the weak sector below $M_C$; **what this article establishes is why no gauge measurement could ever explain the columns, which is a statement about the group.**

This article is about that second copy and the third. It asks what distinguishes a generation from its neighbours, and it gets exactly three answers. Charge, colour, weak isospin and $B-L$ are the same in all three columns, so they cannot distinguish anything. Mass differs, lifetime differs, and the decay pattern differs. Those three differences are the whole of flavour, and the first task is to show that they are not three independent things.

The order of the article follows the order of the argument. *Three Words, Used Precisely* fixes the vocabulary. *Why the Index Is Inert* shows why no gauge measurement can see the generation index at all, which is the structural fact the rest depends on. *The Sixteen Rows* and 4 draw the table and separate the six independent masses from the eighteen entries that colour and chirality multiply them into. *Mass: the Column the Model Does Not Compute*, 6 and 7 take the three handles one at a time. *How Each Handle Is Seen* says what each handle looks like in a detector. *The One Sharp Prediction: Sameness* and 10 record the one sharp prediction the model makes in this sector and the one place where a flavour label is measured to change.

A companion article, [The Excitation Ladder Theory of Flavour](the-excitation-ladder-theory-of-flavour.html), takes the same three handles and asks whether the columns are levels of one tower. That question is deliberately absent here. This article is the introduction, and an introduction should leave the reader with the phenomena and no theory of them.

## Three Words, Used Precisely

Generation, flavour and family name one object from three directions, and the corpus keeps the directions apart.

*Generation* is the index. It is the column of the particle table, and it takes the values one, two and three.

*Flavour* is the basis. It is the label in which the mass matrix is not diagonal, and it is the label that a charged current can change and a neutral current cannot.

*Family* is the informal word for the set of three columns taken together, and it carries no technical content.

The distinction between the first two is the whole content of *The One Sharp Prediction: Sameness* and 10. A generation is a bookkeeping device that is always diagonal. A flavour is a basis that can be misaligned with the mass basis, and the misalignment is what makes oscillation and mixing possible.

## Why the Index Is Inert

**The theorem first, and it is one line of algebra.** Let the fermions of one sector be the module $S$ of the symmetry group, and let a copy index of dimension $n$ multiply it:

$$
S\;\longrightarrow\;S\otimes\mathbb C^{n},
\qquad
\tilde Q\cdot(\Xi\otimes f)=(\tilde Q\cdot\Xi)\otimes f .
$$

**Every operator the model builds from the symmetry group is therefore $O\otimes\mathbb 1_{n}$**, and the operators that commute with the whole algebra are all of $M_{n}(\mathbb C)$. **The index factor is the commutant, and nothing in the algebra selects a direction inside it.**

**In this model $S$ is the sixteen and $n=2$.** The copy index is the weak-doublet slot, the algebra is $\mathfrak{su}(4)$, and

$$
Q\otimes\mathbb 1_{2}=\begin{pmatrix}q&0\\0&q\end{pmatrix},
\qquad
\bigl[X\otimes\mathbb 1_{2},\,\mathbb 1_{4}\otimes M\bigr]=0\ \ \text{for every }M .
$$

**The copy index carries a global $\mathrm{U}(2)$ that the sector cannot see**, which is the statement [the vertex article](the-fermion-gauge-vertex-in-the-quartet-basis-the-fifteen-read-on-the-sixteen.html) proves as a commutation relation.

**Three consequences follow, and they organise everything else in this article.**

**No gauge measurement distinguishes the two copies.** A charge measurement returns $q$ twice, and the copies are distinguished only by mass. **That is the structural fact the whole of flavour rests on**, and here it is visible in a $2\times2$ matrix.

**No connection changes the index at tree level.** A connection vertex is $\mathbb 1_{n}$ on the index, so a vertex that joins two different sectors is the product of two different rotations, $X^{\dagger}Y$, and only a vertex that changes the sector can leave a misalignment. **In this model there is no such vertex at all**, because no generator carries $\alpha$; the misalignment exists only below $M_C$, where a charged current joins two doublet slots.

**The only free object in the sector is the Yukawa matrix.** Since no generator can distinguish the copies, the difference between them must sit where the algebra does not constrain — [the Yukawa article](the-yukawa-sector-of-the-su4-model-one-matrix-and-its-diagonalisation.html) is that place, and it holds two numbers.

**What the lemma does not give, and the honest sentence.** The measured flavour data are a *three*-column table, and **this model has a two-valued index and no generation label**: the three columns describe the weak sector, and every number below is data. **The lemma is quoted because it is the reason no gauge measurement can ever explain them**, not because it produces them.

**The symbols to avoid, and why.** Writing $\mathbf{16}\otimes\mathbb C^{3}$ and multiplying a weak-isospin generator into the family space imports the weak sector: **the $\mathbf{16}$ is not a representation of $\mathfrak{su}(4)$, and no weak-isospin generator is one of the fifteen.** **The theorem survives the translation, and the symbols do not.**

## The Sixteen Rows

The classification article's two octets stack into sixteen rows, and each generation needs a name, a mass and a lifetime. The whole table is therefore sixteen rows by twelve columns, and it is drawn here in full, because the repetition is the point. Masses are in kilograms and lifetimes in seconds, both measured.

| # | field | $Q$ | name $i=1$ | $m_1$ | $\tau_1$ | name $i=2$ | $m_2$ | $\tau_2$ | name $i=3$ | $m_3$ | $\tau_3$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $1$ | $\xi_{\mathrm{neu},eL}$ | $0$ | electron neutrino | $<1.43\times10^{-36}$ | stable | muon neutrino | $<1.43\times10^{-36}$ | stable | tau neutrino | $<1.43\times10^{-36}$ | stable |
| $2$ | $e_{L}$ | $-1$ | electron | $9.109\times10^{-31}$ | stable | muon | $1.883\times10^{-28}$ | $2.20\times10^{-6}$ | tau | $3.167\times10^{-27}$ | $2.90\times10^{-13}$ |
| $3$ | $u^{r}_{L}$ | $+\tfrac23$ | up, red | $3.850\times10^{-30}$ | stable | charm, red | $2.264\times10^{-27}$ | $1.03\times10^{-12}$ | top, red | $3.079\times10^{-25}$ | $5.0\times10^{-25}$ |
| $4$ | $d^{r}_{L}$ | $-\tfrac13$ | down, red | $8.325\times10^{-30}$ | stable | strange, red | $1.665\times10^{-28}$ | $8.98\times10^{-11}$ | bottom, red | $7.452\times10^{-27}$ | $1.52\times10^{-12}$ |
| $5$ | $u^{g}_{L}$ | $+\tfrac23$ | up, green | $3.850\times10^{-30}$ | stable | charm, green | $2.264\times10^{-27}$ | $1.03\times10^{-12}$ | top, green | $3.079\times10^{-25}$ | $5.0\times10^{-25}$ |
| $6$ | $d^{g}_{L}$ | $-\tfrac13$ | down, green | $8.325\times10^{-30}$ | stable | strange, green | $1.665\times10^{-28}$ | $8.98\times10^{-11}$ | bottom, green | $7.452\times10^{-27}$ | $1.52\times10^{-12}$ |
| $7$ | $u^{b}_{L}$ | $+\tfrac23$ | up, blue | $3.850\times10^{-30}$ | stable | charm, blue | $2.264\times10^{-27}$ | $1.03\times10^{-12}$ | top, blue | $3.079\times10^{-25}$ | $5.0\times10^{-25}$ |
| $8$ | $d^{b}_{L}$ | $-\tfrac13$ | down, blue | $8.325\times10^{-30}$ | stable | strange, blue | $1.665\times10^{-28}$ | $8.98\times10^{-11}$ | bottom, blue | $7.452\times10^{-27}$ | $1.52\times10^{-12}$ |
| $9$ | $\xi_{\mathrm{neu},eR}$ | $0$ | electron neutrino | $<1.43\times10^{-36}$ | stable | muon neutrino | $<1.43\times10^{-36}$ | stable | tau neutrino | $<1.43\times10^{-36}$ | stable |
| $10$ | $e_{R}$ | $-1$ | electron | $9.109\times10^{-31}$ | stable | muon | $1.883\times10^{-28}$ | $2.20\times10^{-6}$ | tau | $3.167\times10^{-27}$ | $2.90\times10^{-13}$ |
| $11$ | $u^{r}_{R}$ | $+\tfrac23$ | up, red | $3.850\times10^{-30}$ | stable | charm, red | $2.264\times10^{-27}$ | $1.03\times10^{-12}$ | top, red | $3.079\times10^{-25}$ | $5.0\times10^{-25}$ |
| $12$ | $d^{r}_{R}$ | $-\tfrac13$ | down, red | $8.325\times10^{-30}$ | stable | strange, red | $1.665\times10^{-28}$ | $8.98\times10^{-11}$ | bottom, red | $7.452\times10^{-27}$ | $1.52\times10^{-12}$ |
| $13$ | $u^{g}_{R}$ | $+\tfrac23$ | up, green | $3.850\times10^{-30}$ | stable | charm, green | $2.264\times10^{-27}$ | $1.03\times10^{-12}$ | top, green | $3.079\times10^{-25}$ | $5.0\times10^{-25}$ |
| $14$ | $d^{g}_{R}$ | $-\tfrac13$ | down, green | $8.325\times10^{-30}$ | stable | strange, green | $1.665\times10^{-28}$ | $8.98\times10^{-11}$ | bottom, green | $7.452\times10^{-27}$ | $1.52\times10^{-12}$ |
| $15$ | $u^{b}_{R}$ | $+\tfrac23$ | up, blue | $3.850\times10^{-30}$ | stable | charm, blue | $2.264\times10^{-27}$ | $1.03\times10^{-12}$ | top, blue | $3.079\times10^{-25}$ | $5.0\times10^{-25}$ |
| $16$ | $d^{b}_{R}$ | $-\tfrac13$ | down, blue | $8.325\times10^{-30}$ | stable | strange, blue | $1.665\times10^{-28}$ | $8.98\times10^{-11}$ | bottom, blue | $7.452\times10^{-27}$ | $1.52\times10^{-12}$ |

Four readings of this table are facts about the field content rather than facts about the measurements.

The charge column does not change across a row. That is *Why the Index Is Inert*, read off a table. Every row carries one charge for all three generations.

The name, mass and lifetime columns do not change between a row and its colour copies. Rows 3, 5, 7 carry one number three times, because colour is unbroken and the three colours are one particle.

The same columns do not change between a chiral pair. Rows 2 and 10 carry one number twice, because a mass is a property of the Dirac particle and not of a chirality.

So the sixteen rows carry four distinct masses per generation, and twelve distinct masses in the whole table: nine electrically charged fermion masses and three neutrino masses. **That is the entire flavour content of the measured table**, and it is what the three handles below have to explain. **This model supplies none of the twelve numbers**, and the one it does supply, $m_{\ell}=3m_{q}$, is wrong by a factor $27$ in [the Yukawa article](the-yukawa-sector-of-the-su4-model-one-matrix-and-its-diagonalisation.html).

**The rows name particles, and the masses are the particles'.** Charge conjugation does not add a row: the antiparticle of a field is a conjugate mode of that same field, with the same mass, the opposite $Q$, the opposite $B-L$ and conjugate colour, and the charges are listed in [The Fermions of One Generation](classification-of-the-fermions-in-the-su4-model-sixteen-weyl-fields-closed-under-c-and-cp.html), §*The Antiparticle Quantum Numbers*. So the sixteen rows are the whole of the matter and the antiparticles add no mass, no lifetime and no branching ratio. **Antiparticles are not a fourth handle.** They are the same three handles with the signs of the charges reversed, which is why they are mentioned here once and not tabulated twice.

The neutrino rows are the ones that are not numbers. A light neutrino mass is bounded and not measured, $m_\beta<8.02\times10^{-37}$ kg from tritium decay (the 2024 KATRIN limit) and $\sum m_{\xi_{\mathrm{neu}}}<2.14\times10^{-37}$ kg from cosmology, so the entries read stable and the oscillation is treated separately in *The One Exception: Oscillation*. The bound applies to the light eigenstates only. The right-handed row is the one that carries no bound at all: in the model's spectrum $\xi_{\mathrm{neu},R}$ is a gauge singlet, its mass is not constrained by tritium decay, and the seesaw of *Mass: the Column the Model Does Not Compute* places it at a scale that is not written anywhere in this table.

## The Three Handles

Read the table by column instead of by row and the tripling appears as three differences.

| handle | what it is | is it independent? |
|---|---|---|
| mass | the eigenvalues of the Yukawa matrix ($3\times3$ below $M_C$; $2\times2$ here) | yes, one arbitrary matrix |
| lifetime | the inverse width | no, a function of the mass |
| decay pattern | which channels are open | no, a function of the mass |

Only the first is independent. A width is fixed once the mass is known and the open channels are counted, and the open channels are fixed by the same mass against the thresholds of the possible final states. Lifetime and decay pattern are therefore the mass seen at two coarser resolutions, and the flavour sector of the model contains one free object rather than three. The title says three handles, and the table says only one of them is independent; that is the section's point and not an inconsistency.

This is the article's central structural claim, and it is worth stating in the form a reader can check. Given the three masses of a sector, the three lifetimes and the three decay patterns follow. Given the three lifetimes, the three masses do not follow.

## Mass: the Column the Model Does Not Compute

The masses of the table are input. Nine of them belong to electrically charged fermions and are measured directly; the remaining three are neutrino masses, and those are bounded rather than measured. Measured, the charged set spans five orders of magnitude in the lepton sector and five in the quark sector:

$$
\frac{m_\mu}{m_e}=206.77,\qquad
\frac{m_\tau}{m_\mu}=16.82,\qquad
\frac{m_t}{m_u}=7.99\times10^{4}.
$$

Where they come from is a short story with an unsatisfying end. The mass matrix is the Yukawa matrix times the scalar's value, $m_i=y_iv/\sqrt2$, in the basis where $Y$ is diagonal. The matrix itself is a generic complex $3\times3$,

$$
Y=\begin{pmatrix}y_{11}&y_{12}&y_{13}\\ y_{21}&y_{22}&y_{23}\\ y_{31}&y_{32}&y_{33}\end{pmatrix},
\qquad
Y=U\operatorname{diag}(y_1,y_2,y_3)V^{\dagger}.
$$

Nine complex entries are eighteen real numbers. Field redefinitions remove nine of the eighteen, leaving nine invariant combinations: three masses, three angles and three phases. For one sector alone only the three masses are observable, because the angles and phases can be absorbed into the fields. Comparing two sectors leaves four, since the relative rotation $V_{\mathrm{CKM}}=W_u^{\dagger}W_d$ carries three angles and one phase.

| sector | parameters | derived? |
|---|---|---|
| charged-lepton masses | $3$ | no |
| up-type quark masses | $3$ | no |
| down-type quark masses | $3$ | no |
| quark mixing | $3$ angles and $1$ phase | no |
| lepton mixing | $3$ angles, $1$ Dirac and $2$ Majorana phases | no |

The negative result is the headline. A generic matrix has no preferred spectrum, so the hierarchy $1:206.8:3477$ is as unexplained here as it is in the Standard Model. Nothing in the model prefers one set of eigenvalues to another, and no argument inside the model selects the observed set.

Two structural remarks do belong to the model. The right-handed neutrino slot exists, so the seesaw mechanism needs no field the model does not already have. And because the scalar sector is fixed and small, the number of Yukawa matrices is finite and small, though small is not the same as few.

## Lifetime: the One Relation Phase Space Computes

A lifetime is the inverse width, $\tau=\frac{h}{2\pi \Gamma}$, and the width is fixed by the mass and by the open channels. For the muon and the tau the final state is the same, $\ell\to e\bar\xi_{\mathrm{neu},e}\jmath_\ell$, and the parent mass is far above every threshold. The width then scales as the fifth power of the parent mass:

$$
\frac{\Gamma(\tau\to e\bar\xi_{\mathrm{neu},e}\xi_{\mathrm{neu},\tau})}{\Gamma(\mu\to e\bar\xi_{\mathrm{neu},e}\xi_{\mathrm{neu},\imath})}=\left(\frac{m_\tau}{m_\mu}\right)^{5}.
$$

This is a statement the model predicts without knowing anything, and it is exact enough to fail, which is why it is worth checking.

$$
\left(\frac{m_\tau}{m_\mu}\right)^{5}=\left(16.817\right)^{5}=1.3451\times10^{6},
$$

and from the measured lifetime of the tau, $\tau_\tau=2.903\times10^{-13}$ s, its electronic branching ratio $0.1782$, and the measured muon lifetime $2.1969811\times10^{-6}$ s,

$$
\frac{\Gamma(\tau\to e\bar\xi_{\mathrm{neu}}\xi_{\mathrm{neu}})}{\Gamma(\mu\to\mathrm{all})}
=\frac{0.1782\times h/2.903\times10^{-13}}{h/2.1969811\times10^{-6}}
=1.3486\times10^{6}.
$$

The numerator is a partial width and the denominator a total width, which is legitimate only because the muon has one channel, so its total width is its partial width to $e\bar\xi_{\mathrm{neu},e}\xi_{\mathrm{neu},\imath}$. The check uses the full precision values; the table rounds them to three figures.

The two agree to $0.26$ parts in a thousand. The fifth power is confirmed, and what it confirms is that the lifetime difference between the muon and the tau is nothing but the mass difference. Two of the three handles are one handle.

The same shift applied to quarks fails, and the failure is the informative part.

$$
\left(\frac{m_c}{m_s}\right)^{5}=4.65\times10^{5},
\qquad
\frac{\tau_s}{\tau_c}=\frac{8.98\times10^{-11}}{1.03\times10^{-12}}=87 .
$$

Four orders of magnitude apart, because the final states are not the same. A strange quark decays to three bodies with a small release; a charm quark has open channels a strange quark does not. The fifth-power law assumes a common final state and a mass far above threshold, so the check tests the assumption as much as the arithmetic. It holds where the assumption holds and fails where it does not, and reporting the failure is more useful than choosing the pair that works.

The three lifetimes, in one line: the tau lives $2.90\times10^{-13}$ s, the muon $2.20\times10^{-6}$ s, the electron forever. Seven orders of magnitude, all of it the mass ratio to the fifth power, and none of it a new parameter.

The top quark is the extreme case of the same statement. Its width is so large that it decays before it can hadronise, at about $5\times10^{-25}$ s, an order of magnitude shorter than the hadronisation time. A particle that decays before it dresses is the cleanest possible demonstration that its lifetime is its mass.

## Decay Pattern: Which Channels Are Open

A decay pattern is the mass column filtered through the conservation laws. Charge, colour and $B-L$ are conserved, so a channel opens exactly when the quantum numbers match and the kinematics allow it.

| particle | open channels | why so few, or so many |
|---|---|---|
| $\mu$ | $e\bar\xi_{\mathrm{neu},e}\xi_{\mathrm{neu},\imath}$ only | $m_\mu$ lies below every hadronic threshold |
| $\tau$ | $e\bar\xi_{\mathrm{neu}}\xi_{\mathrm{neu}}$, $\mu\bar\xi_{\mathrm{neu}}\xi_{\mathrm{neu}}$, $\pi\xi_{\mathrm{neu}}$, $\rho\xi_{\mathrm{neu}}$, $a_1\xi_{\mathrm{neu}}$, and more | $m_\tau$ lies above the two-pion threshold |
| $t$ | $Wb$ only | the charged current is the only route, and $m_t>m_W+m_b$ |

The branching ratios are the fingerprint, and they are what a detector measures. For the tau, roughly $17.8$ per cent electronic, $17.4$ per cent muonic, and the remainder hadronic. That is a distribution rather than a number, which is why a single tau event is identified by its topology and not by its mass.

The muon's single channel is why it is the cleanest laboratory in the model. One final state means one width, one lifetime, and no channel-dependent correction. Every precision statement about lepton universality is a statement about that single channel.

Production is the other half of the pattern. Strong and electromagnetic production conserve the label, so a flavour is made in pairs: $e^+e^-\to\mu^+\mu^-$, $\to c\bar c$, $\to b\bar b$. A single muon cannot be produced without a $\mu^+$, which is why the thresholds that reveal a new flavour are pair thresholds.

## How Each Handle Is Seen

Each handle has its own experimental signature, and the list is the operational content of the whole article.

| handle | signature | classic case |
|---|---|---|
| mass | a peak in the invariant-mass distribution | $J/Ξ_{\mathrm{wfn}}$ at $5.522\times10^{-27}$ kg, a narrow spike over a falling background |
| mass, as a threshold | a step in a cross-section | $e^+e^-$ into hadrons rising at the charm and beauty pair thresholds |
| lifetime, long | a track that stops | a muon coming to rest after a few centimetres |
| lifetime, short | a displaced vertex | a $b$ hadron flying a few hundred micrometres before decaying |
| lifetime, very short | a kink, or no track at all | a tau kink; a top that leaves no track of its own |
| decay pattern | a branching ratio | the tau's three-way split |

The historical order matches the table, and that is not a coincidence. The muon was found as a track that stopped where a track should not. The strange quark was found as a particle that lived too long for its mass. The charm and beauty quarks were found as thresholds and displaced vertices. The top was found as a resonance whose width exceeds the strong-interaction scale, so it decays before it can hadronise. In every case the discovery was a mass, and the confirmation was a lifetime or a branching ratio. No discovery in the list was a new charge.

That is the empirical shape of the tripling, and it matches *Why the Index Is Inert* exactly. Three columns that differ in nothing the sector sees can only be found by weighing them.

## The One Sharp Prediction: Sameness

Because the three columns couple identically, the $Z$ must decay into $e^+e^-$, $\mu^+\mu^-$ and $\tau^+\tau^-$ at the same rate. Measured at LEP:

| channel | width (J) | ratio to the electron channel |
|---|---|---|
| $Z\to e^+e^-$ | $1.3456\times10^{-11}$ | $1$ |
| $Z\to\mu^+\mu^-$ | $1.3457\times10^{-11}$ | $1.00011$ |
| $Z\to\tau^+\tau^-$ | $1.3472\times10^{-11}$ | $1.00121$ |

Two parts in a thousand, on a quantity the model says is exactly equal. The residual is understood as mass-dependent radiation, so the agreement is complete.

One precision note about the table. The quantities LEP measures directly are ratios of partial widths, and the widths in joules are extracted from those ratios under the assumption of the standard model's own couplings. The ratio column is therefore the test and the width column is the presentation, and a table that printed only the widths would hide which number was measured.

This is the model's only sharp prediction in this sector, and it is a prediction of sameness rather than of a number. It deserves the emphasis because it is easy to mistake for a triviality. A model in which the three columns coupled differently would pass every other test in this article and fail this one.

## The One Exception: Oscillation

Neutrino oscillation is the only measured change of flavour, and it exists because the neutrino mass matrix cannot be rotated away. For the charged leptons the rotation $V$ in $Y=U\operatorname{diag}(y)V^{\dagger}$ is a field redefinition of the Standard Model's own currents; in this frame it is one factor of the leptoquark mixing $K$. For the neutrinos the mass term is Majorana, so the same rotation leaves a physical residue:

$$
P(\xi_{\mathrm{neu},e}\to\xi_{\mathrm{neu},\imath})=\sin^{2}2\theta\,\sin^{2}\!\left(\frac{\Delta m^{2}L}{4E}\right).
$$

Read as a statement about this article's subject, the formula needs two things: a non-degenerate mass column, $\Delta m^{2}\neq0$, and a misaligned basis, $\theta\neq0$. Both are properties of the Yukawa matrix and of nothing else. Oscillation is therefore not an exception to the model's flavour blindness but the sharpest confirmation of it, since the blindness is exactly what makes the misalignment the only available source.

It is also the only place where a flavour label changes during propagation, with neither a charged current nor a loop involved.

## Negative Results, Stated Once

Four things this article does not have, listed so that no reader supplies them.

The number three is not derived. The multiplicity is free, so the algebra permits any number of generations. What fixes three is measurement: the $Z$ invisible width gives $N_{\xi_{\mathrm{neu}}}=2.984\pm0.008$, big-bang nucleosynthesis gives $N_{\mathrm{eff}}\approx3$, and direct search closes the rest. CP violation requires at least three generations, and that is a necessary condition rather than a sufficient one: with three generations the phase and the angles must also be non-zero, which is what the measured Jarlskog invariant says they are.

No mass is derived. The three masses of a sector are the eigenvalues of an arbitrary matrix. The hierarchy $1:206.8:3477$ is input.

No mixing angle and no phase is derived. Nine of the eighteen real parameters of $Y$ survive, and all nine are measured.

Flavour-changing neutral currents of the neutral connections are absent at tree level. That is a prediction rather than a gap, and its test is the LEP table of *The One Sharp Prediction: Sameness*. A leptoquark exchange is not one of them: it carries colour and charge, and the tree-level kaon channel is its business.

One thing the model does not settle, kept separate from the four. The leptoquarks carry one coupling for every generation, so in the gauge basis their vertex has no generation index. Whether that survives diagonalisation is a question about the Yukawa sector and not about the sector: this model has one Yukawa matrix, so its two sectors are aligned and no generation change exists at all, while a second matrix below $M_C$ would leave a mixing matrix the corpus does not write. **The model therefore cannot say whether charged-lepton flavour is violated, and it says so in [Lepton Flavour in the $\mathrm{SU}(4)$ Model](lepton-flavour-in-the-su4-model-nothing-turns-the-lepton.html).** That is the opposite of the mass problem: the model cannot say why the masses differ, and it can say that the bosons do not care that they do.

## Checks

Every number below was recomputed from the values in *The Sixteen Rows* before it was written.

| claim | check | result |
|---|---|---|
| one charge across a row | $Q$ column, rows $e$ and $u$ | equal |
| one mass across three colours | the three colour copies of $u$ | one number |
| one mass across two chiralities | $e_L$ and $e_R$ | one number |
| the muon-to-electron mass ratio | $105.66/0.511$ | $206.77$ |
| the tau-to-electron mass ratio | $1776.9/0.511$ | $3477.2$ |
| the tau-to-muon mass ratio | $1776.9/105.66$ | $16.82$ |
| the fifth power | $16.817^{5}$ | $1.3451\times10^{6}$ |
| the measured width ratio | $0.1782\times2.1969811\times10^{-6}/2.903\times10^{-13}$ | $1.3486\times10^{6}$ |
| muon and tau against the fifth power | $1.3451$ against $1.3486$ | agrees to $0.26$ per cent |
| the fifth power applied to quarks | $4.65\times10^{5}$ against $87$ | fails, final states differ |
| $Z$ universality | $83.993$ and $84.086$ against $83.984$ | $1.00011$ and $1.00121$ |
| the parameters of one Yukawa matrix | $18$ real, $9$ removed | $9$ survive |
| the independent masses in the table | $4$ per generation, $12$ total | matches the measured set |
| the antiparticles | $Q\to-Q$, $B-L\to-(B-L)$, colour $\to\bar 3$ | same masses, flipped charges |
| the states with antiparticles | $16$ fields per generation | $32$ states |

## Further Reading

- [The Fermions of One Generation](classification-of-the-fermions-in-the-su4-model-sixteen-weyl-fields-closed-under-c-and-cp.html). The sixteen cells of one generation, named, and no flavour.
- [The Excitation Ladder Theory of Flavour](the-excitation-ladder-theory-of-flavour.html). The companion article, which takes these three handles and asks whether the columns are levels of one tower.
- [The Number of Generations and the Biquaternion Algebra](the-number-of-generations-and-the-biquaternion-algebra.html). Why the algebra does not count them.
- [The Yukawa Sector of the $\mathrm{SU}(4)$ Model: One Matrix and Its Diagonalisation](the-yukawa-sector-of-the-su4-model-one-matrix-and-its-diagonalisation.html). Where the mass matrix is written and why its eigenvalues are input.
- [The CKM Matrix and CP Violation in Biquaternionic Form](the-ckm-matrix-and-cp-violation-in-biquaternionic-form.html). The misalignment between the flavour basis and the mass basis.
- [Lepton Flavour in the $\mathrm{SU}(4)$ Model: Nothing Turns the Lepton, and the Matrix That Would Have To](lepton-flavour-in-the-su4-model-nothing-turns-the-lepton.html). The flavour-blind coupling, its mixing matrix and its predicted pattern.

External data. The masses and lifetimes in *The Sixteen Rows* are the Particle Data Group values, Review of Particle Physics, and the $Z$ widths of *The One Sharp Prediction: Sameness* are the LEP line-shape results. Both are time-dependent compilations, so the numbers here should be quoted with a date when they are carried forward.
