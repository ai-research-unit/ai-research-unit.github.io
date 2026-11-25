# __Three Diagrams of the $\mathrm{SU}(4)$ Model: The Kaon, the Proton Chain, and a Gluon Exchange__

## Introduction

**Three diagrams, and each is chosen to exercise one part of the rules that the corpus had not previously applied.** [The rules article](the-feynman-rules-of-the-su4-model-the-vertices-of-the-fifteen-and-the-sixteen.html) prints the vertices; this article puts three of them on external legs and carries each to a number, a power, or a colour factor.

- **$K_L\to\mu e$ at tree level.** Two leptoquark vertices and one heavy propagator. **It produces a number**, and the number is $3.5\times10^{-12}$ against a measured limit of $4.7\times10^{-12}$ — under one assumption that the article names and does not hide.
- **The proton chain.** Three leptoquark vertices and no diquark. **It produces a power**, $M_X^{-10}$ against the $M_X^{-4}$ of a dimension-six operator, and the power is why the gauge sector is not bounded by proton decay.
- **Gluon exchange between two quarks.** One vertex at each end and the eight colour arrays in the middle. **It produces a colour factor**, and the factor is $C_F=\tfrac43$, computed here from the corpus's own eight arrays rather than quoted.

**What the three have in common is the ledger.** Each is a transcription of standard theory's diagrammatic content onto the model's field content, and none of the three is a prediction of the frame beyond what the field content forces. **The kaon diagram's rate is an assumption about a matrix the frame never writes; the proton chain's power is a consequence of the absence of one field; the gluon factor is standard $\mathrm{SU}(3)$ in the corner of $\mathrm{SU}(4)$.**

**What the article does not do.** It does not compute a loop, it does not compute a hadronic matrix element beyond the decay constant, and it does not choose a generation matrix. **Each of the three omissions is the same omission in a different place**: the frame supplies the vertices and the group, and the numbers it cannot supply are the ones that live in a matrix, a form factor, or a counterterm.

## Conventions and the Three Vertices Used

**The vertices, restated so the diagrams can be read without turning back.**

$$
\Gamma_{a,\imath}=-ig_{4}\gamma_{\imath}\bigl(t_{a}\otimes\mathbb{1}_{2}\bigr),
$$

**with $t_{a}$ the normalised generator of [the rules article](the-feynman-rules-of-the-su4-model-the-vertices-of-the-fifteen-and-the-sixteen.html)'s normalisation section, and the heavy propagator in the limit $k^{2}\ll M_X^{2}$**
$$
\frac{i}{k^{2}-M_X^{2}}\ \longrightarrow\ \frac{-i}{M_X^{2}} .
$$
**Every diagram below is at energies far below $M_X$, so every leptoquark propagator is a constant and every diagram is a contact term.** That is the reason a two-vertex diagram and a three-vertex diagram differ by a power of $M_X$ and by nothing else.

**The coupling, and there is one.** $g_4$ at every vertex, the gluon's included: **the gluon vertex is $g_4$ restricted to the corner block, so the question whether $g_s$ equals $g_4$ is not a question here.** The value stays symbolic, and no diagram below needs it: the kaon rate carries $g_4^{4}$, the proton power carries none, and the colour factor is a ratio.

## Diagram One: $K_L\to\mu e$

**The external state.** $K_L$ is the odd combination of $K^{0}=d\bar s$ and $\bar K^{0}=\bar d s$, and the final state is $\mu^{-}e^{+}$ or $\mu^{+}e^{-}$. **The diagram has two quark legs in, two lepton legs out, and two leptoquark vertices joined by one propagator.**

**In the model's indices, and this is where the diagram becomes a matrix statement.** The $d$ and the $s$ are both colour-line states with $B-L=+\tfrac13$; the $\mu$ and the $e$ are both lepton-line states with $B-L=-1$. **So each quark leg needs an entry that carries $\Delta(B-L)=-\tfrac43$ into the lepton, and the only entries with that value are the six mixed planes.** Two legs, two vertices, two entries, one colour:

$$
d^{\,a}\ \xrightarrow{\ A_{ta}\ }\ e^{-},\qquad
s^{\,a}\ \xrightarrow{\ A_{ta}\ }\ \mu^{-},
\qquad
\text{the same }a\in\{r,g,b\}\ \text{for both},
$$

**and the same-colour condition is the whole of the colour factor.**

**The colour factor is one, and the corpus says so with a reason.** The quark legs contract over the triplet index of the $\mathbf{4}$; the leptoquark propagator is diagonal in colour, because the two vertices carry the same index $a$ and the propagator is $\delta_{ab}$; **so the contraction gives one and not three**: there is no sum over colours to make, and the diagram is not the $N_c=3$ of an $s$-channel annihilation. **A reader who expects three has imported the wrong topology**: here the two vertices sit on the same colour line and the line is carried through, not summed.

**The amplitude, and its shape.**

$$
i\mathcal{M}=i\,\frac{g_4^{2}}{2M_X^{2}}\Bigl[(\bar q\,\gamma^{\imath}P_L\ell)(\bar q'\,\gamma_{\imath}P_L\ell')+(L\to R)\Bigr],
$$

**with the factor $\tfrac12$ carried in the corpus's operator; it is not a colour sum**, and the colour sum was disposed of in the paragraph above. The $V-A$ at each vertex is the model's: the left-handed block couples $P_{L}$, the right-handed block $P_{R}$, and both appear because both chiralities of the mixed plane exist. **The operator is the one the corpus prints in [the lepton-flavour article](lepton-flavour-in-the-su4-model-nothing-turns-the-lepton.html), and the $L\to R$ line is not an afterthought**: it is the second of the two planes of the pair.

**Why $K_L$ and not $K_S$.** The kaon is a pseudoscalar, so only the axial part of a $V-A$ current contributes, and the axial matrix element is odd under $K^{0}\leftrightarrow\bar K^{0}$. **With $K_S$ the symmetric combination and $K_L$ the odd one, the odd combination survives and the even one cancels**: the frame predicts $K_L\to\mu e$ and forbids $K_S\to\mu e$ at leading order, with a residue at the $|\epsilon_K|^{2}$ level near $10^{-20}$. **That is a selection rule of the algebra plus one fact about a kaon, and neither is adjustable.**

**The rate, and its shape.**
$$
\Gamma(K_L\to\mu e)=\frac{g_4^{4}\,\lvert U_{de}U_{s\imath}\rvert^{2}f_K^{2}m_\mu^{2}m_K}{128\pi\,M_X^{4}} .
$$
**Four powers of the mass, one helicity suppression, one decay constant, and one entry of a matrix the frame does not write.** The $M_X^{-4}$ is the dimension-six shape; the $m_\mu^{2}$ is the chirality flip that a pseudoscalar decay needs; the $f_K$ is the one hadronic number the corpus takes from outside.

**The number, and the assumption under it.** At $M_X=4.01\times10^{-5}\ \mathrm{J}$ with $|U_{de}U_{s\imath}|=1$ the rate is $3.5\times10^{-12}$, against the measured limit $4.7\times10^{-12}$. **So the corner of parameter space where the generation matrix is maximal sits at the experimental limit**, which is where the corpus's quoted scale comes from.

**The assumption, stated plainly because the article's honesty depends on it.** If $U$ is the identity, every entry vanishes, the rate is zero at every mass, and no kaon measurement constrains $M_X$. **The number $3.5\times10^{-12}$ is therefore a statement about a maximal matrix and not a prediction**, and a null result is what the minimal model predicts. **The frame fixes everything in the formula except the one object that decides whether the formula is nonzero.**

## Diagram Two: The Proton Chain

**Why three vertices and not one.** Each leptoquark vertex converts one quark into one lepton, and each carries away $B-L=\pm\tfrac43$. **A proton has three quarks and each must be converted, so the leading diagram has three vertices.** The alternative — one vertex converting two quarks at once — needs a diquark coupling, and the fifteen's colour triplets carry $B-L=\pm\tfrac43$ while a $qq$ pair carries $+\tfrac23$, so no entry of the fifteen supplies it.

**The chain, in the model's indices.**

$$
u^{\,a}\to e^{+},\qquad u^{\,b}\to e^{+},\qquad d^{\,c}\to\nu,
\qquad
a\neq b\neq c,
$$

**and the colour indices must be distinct because the three quarks of a proton are in an antisymmetric colour state.** The three vertices therefore use three different mixed planes, and their colour indices are contracted with the proton's $\epsilon_{abc}$ and the final state's. **That contraction is where the power of $M_X$ comes from and where the colour factor differs from the kaon's**: three lines, three different colours, and one antisymmetric invariant.

**The power comes from the operator's dimension and not from a count of propagators.** A six-fermion operator has dimension nine, so its coefficient has dimension $4-9=-5$ and is $1/\Lambda^{5}$; the rate of a three-body decay from a dimension-$d$ operator carries
$$
\Gamma\ \propto\ \frac{m_p^{\,2d-7}}{\Lambda^{\,2d-8}},
\qquad
d=9:\ \ \Gamma\propto\frac{m_p^{11}}{M_X^{10}} .
$$
**For the dimension-six comparison the same formula gives $d=6$ and $m_p^{5}/M_X^{4}$**, which is why the six extra powers appear on the rate and not on the amplitude. **The corpus prints $M_X^{-10}$ and that is this rule**, not a literal product of three propagators; a reader who counts propagators instead of dimensions will get a different exponent, and the operator rule is the one that holds.

**The margin, in numbers.** $M_X^{-10}$ against $M_X^{-4}$ at the same $M_X$ is a factor of $(M_X/m_p)^{6}$ times the mass factors, and at $M_X$ of order $10^{-5}$ J the three-vertex channel is beyond any conceivable experiment. **So the conclusion the corpus draws is not sensitive to the counting**: the gauge sector is unobservable in proton decay at any $M_X$ the kaon channel allows.

**The consequence, and it is the reason proton decay does not bite.** At $M_X$ of order $10^{-5}$ J the three-vertex rate is unobservable at any conceivable experiment, so **the gauge sector is not bounded by the proton's stability** — and the bound that does exist on $M_X$, the kaon one, comes from the two-vertex diagram above. **The corpus's strongest statement about the fourth colour is therefore not a proton-decay bound, and a reader who looks for one will find a null result where they expected a constraint.**

**The channel that the frame forbids, stated once more because it is the one a reader will ask about.** $p\to e^{+}\pi^{0}$ needs a $\pi^{0}$ in the final state, a $\pi^{0}$ is two quarks, and two quarks in the final state need a diquark coupling at one of the vertices. **No field in the frame supplies one**, so the channel has no gauge contribution at any order, and the final state is three leptons.

## Diagram Three: Gluon Exchange, and the Colour Factor

**The diagram.** Two quarks exchange one gluon, $q\bar q\to q\bar q$, with a vertex from the corner at each end and the eight gluon propagators in between. **The Lorentz and spinor parts are QED's with $C_F$ in place of $1$; the model's content is the eight arrays and the factor they produce.**

**The eight arrays of the corner.** Restricted to the colour block $\{x,y,z\}$, the eight are
$$
A_{xy},\ iS_{xy},\ A_{xz},\ iS_{xz},\ A_{yz},\ iS_{yz},\ d_{2},\ d_{3},
$$
**and restricted to the colour block they span $\mathfrak{su}(3)$, which is eight-dimensional, one array per dimension.** The colour block is closed under the bracket, which is the content of the corpus's statement that the first breaking leaves the colour algebra standing. **On the quartet the same eight arrays carry a zero $t$ row and column**, so the eight dimensions are visible only inside the $3\times3$ block.

**The normalisation, and the one place it bites.** The rules article's Gram matrix is not diagonal: $\langle d_{2},d_{3}\rangle=-1$. **So the eight are not orthonormal as printed, and the two orthogonal combinations are**
$$
c_{2}=d_{2}+d_{3}=i\operatorname{diag}(0,1,0,-1)\ \text{of norm}^{2}\ 2,
\qquad
c_{3}=d_{2}-d_{3}=i\operatorname{diag}(0,1,-2,1)\ \text{of norm}^{2}\ 6 .
$$
**With $t_{a}=G_{a}/\sqrt{2\operatorname{tr}(G_{a}^{\dagger}G_{a})}$ on the six planes and on $c_{2}$, $c_{3}$, the eight are orthonormal at $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$, and the sum of squares is a single number:**
$$
\sum_{a=1}^{8}t_{a}^{2}=-\tfrac43\,\mathbb{1},
\qquad
\sum_{a=1}^{8}T_{a}^{2}=+\tfrac43\,\mathbb{1}\ \text{for hermitian }T_{a}=it_{a}.
$$
**The colour factor is $\tfrac43$ and it was computed from the corpus's own eight arrays**, not imported: the three values $-\tfrac43$ on the colour block, with $0$ on the lepton line, are the whole check, and the sign is the anti-hermitian convention's.

**The identity behind a one-gluon exchange is the completeness relation, and it is worth printing because it is the whole colour content of the diagram.** On the normalised eight,
$$
\sum_{a=1}^{8}(t_{a})_{ij}(t_{a})_{kl}=-\tfrac12\Bigl(\delta_{il}\delta_{kj}-\tfrac13\delta_{ij}\delta_{kl}\Bigr),
$$
**verified entry by entry on the $8\times81$ products to $6\times10^{-17}$.** The second term is the $1/N_c$ piece, and it annihilates a colour-singlet contraction because every $t_{a}$ is traceless, $\operatorname{tr}t_{a}=0$; **what survives on an external quark line is the first term, and its eigenvalue there is $C_F=\tfrac43$.**


**Why it is $\tfrac43$ and not $3$ or $\tfrac12$.** The factor attached to an external quark line that emits a gluon is $C_F$, the quadratic Casimir of the triplet; $3$ is the number of colours, which appears when a colour sum is made and none is made here; $\tfrac12$ is $T_R$, the normalisation of the trace, which appears when the gluon is the external state. **A reader who mixes the three gets a diagram wrong by a factor of $\tfrac83$ or $\tfrac{2}{3}$, and the rule is: $C_F$ per external quark line, $T_R$ per quark loop, $N_c$ per colour sum.**

**What the diagram does not test.** It does not test the mixed band, because no leptoquark appears, and **there is no weak sector to leave untested**: the model has no $\tau$, and the copy index is not gauged. **It tests exactly one thing: that the corner of $\mathrm{SU}(4)$ is an $\mathrm{SU}(3)$ with the standard Casimir**, and its value is a check on the normalisation rather than on the group.

**The comparison that the three diagrams make together.**

| diagram | vertices | propagators | colour factor | the number it produces |
| --- | --- | --- | --- | --- |
| $K_L\to\mu e$ | $2$ leptoquark | $1$ heavy, same line | $1$ | $3.5\times10^{-12}$ at $|U|=1$ |
| proton chain | $3$ leptoquark | $2$ heavy, three colours | $\epsilon_{abc}$ contraction | $M_X^{-10}$ |
| gluon exchange | $2$ gluon | $1$ massless | $C_F=\tfrac43$ | a Casimir, not a rate |

**The colour column is the article's summary in one line.** One line gives one; three distinct lines with an antisymmetric invariant give a power of the mass; a sum over eight generators gives the Casimir. **The three cases are the three ways colour can enter a diagram, and the model realises all three with the same eight arrays.**

## What the Three Diagrams Do Not Establish

**They do not establish that the fourth colour exists.** Every number above is computed from a field content that was declared, and the kaon rate's normalisation is an assumption about a matrix. **A reader who wants evidence has to go to the $K_L\to\mu e$ measurement and to the leptoquark searches, and the corpus's position is that the measurement is the decisive one**: the model fixes the operator and not the mixing, so only a measurement can decide.

**They do not establish a mass.** $M_X$ enters every formula as a free parameter, and the model supplies one value for it: $M_X^{2}=8g_4^{2}v^{2}$ from the adjoint mass matrix, **the only mass scale the model has** (the array-level value, before normalisation, is $32v^{2}$). A reader who wants $v$ has to take it from outside, and the kaon number uses the corner of parameter space as well.

**They do not establish a hierarchy, because there is none to establish.** The three diagrams have three different colour behaviours and one coupling, and **a single coupling cannot produce a ratio of couplings**: the old frame's $g_4$, $g_s$ and $g_L$ are one symbol here, and the mismatch they used to carry is a property of the successor.

**And they do not close the loop.** Every one is tree level. **The muon channels need a loop, a chirality flip and a GIM sum, and the corpus states the result without computing the coefficient**, which is the honest ceiling of the sector at present.

## The Checks

| check | computation | result |
| --- | --- | --- |
| the kaon rate at $M_X=4.01\times10^{-5}$ J, $|U|=1$ | $g_4^{4}f_K^{2}m_\mu^{2}m_K/(128\pi M_X^{4})$ | $3.5\times10^{-12}$ |
| the measured limit | experiment | $4.7\times10^{-12}$ |
| the colour factor of the kaon diagram | two vertices on one line, diagonal propagator | $1$ |
| the kaon channel selected | odd under $K^{0}\leftrightarrow\bar K^{0}$ | $K_L$ |
| the $K_S$ residue | $|\epsilon_K|^{2}$ | $\sim10^{-20}$ |
| the proton's vertex count | one quark converted per vertex | $3$ |
| the proton rate's power | dimension-nine operator, $m_p^{2d-7}/\Lambda^{2d-8}$ | $M_X^{-10}$ |
| the dimension-six comparison | $d=6$ in the same formula | $M_X^{-4}$ |
| the diquark's absence | $qq$ carries $B-L=+\tfrac23$, the triplets $\pm\tfrac43$ | no coupling |
| the colour Cartan's Gram matrix | $\langle d_{2},d_{3}\rangle$ | $-1$ |
| the eight orthogonalised | $c_{2}=d_{2}+d_{3}$, $c_{3}=d_{2}-d_{3}$ | norms$^{2}$ $2$ and $6$ |
| the sum of squares | $\sum_{a=1}^{8}t_{a}^{2}$ | $-\tfrac43\mathbb{1}$ |
| the Casimir, hermitian convention | $T_{a}=it_{a}$ | $C_F=\tfrac43$ |
| the completeness relation | $\sum_{a}(t_{a})_{ij}(t_{a})_{kl}$ | $-\tfrac12(\delta_{il}\delta_{kj}-\tfrac13\delta_{ij}\delta_{kl})$ |
| the singlet piece | $\operatorname{tr}t_{a}$ for the eight | $0$, so the $1/N_c$ term drops |

## Summary

**Three diagrams and three different pieces of arithmetic.** The kaon diagram turns two leptoquark vertices and one heavy propagator into $3.5\times10^{-12}$, and it does so only if a generation matrix the frame never writes is maximal — so the number is a corner of parameter space and not a prediction. **Its colour factor is one, for a reason that is easy to get wrong**: the two vertices sit on the same colour line and there is no sum to make.

**The proton chain turns three vertices and the absence of a diquark into $M_X^{-10}$.** Six powers beyond the dimension-six shape, and the six are the difference of the two operator dimensions, doubled on the rate. **The consequence is negative and it is the corpus's most useful negative statement**: the fourth colour is not bounded by proton decay, and $p\to e^{+}\pi^{0}$ has no gauge contribution at any order.

**The gluon diagram turns the eight corner arrays into $C_F=\tfrac43$**, computed from the printed matrices after the one rotation the Gram matrix forces. **The factor is a check on the normalisation and not on the group**, and the rule that separates $C_F$, $T_R$ and $N_c$ is the one worth carrying away.

**What the three have in common is that each is complete as a transcription and incomplete as a measurement.** The vertices are exact, the colour factors are exact, the powers are exact, and the numbers that are not exact are the ones that live outside the algebra: a generation matrix, a decay constant, a coupling value.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $M_X$ | The leptoquark mass, $M_X^{2}=8g_4^{2}v^{2}$ from the adjoint mass matrix |
| $U_{qe}$ | The generation matrix entries, not written by the frame |
| $f_K$ | The kaon decay constant, an imported hadronic number |
| $P_{L}$, $P_{R}$ | The chiral projectors of the two halves, quartet and conjugate |
| $C_F$ | $\tfrac43$, the quadratic Casimir of the triplet |
| $T_R$ | $\tfrac12$, the trace normalisation |
| $N_c$ | $3$, the number of colours |
| $c_{2}$, $c_{3}$ | The orthogonal colour-Cartan combinations |
| $\epsilon_{abc}$ | The antisymmetric colour invariant of the proton |
| $m_p$ | The proton mass |
| $M_X^{-10}$ | The proton rate's suppression, against $M_X^{-4}$ |
| $1$, not $3$ | The kaon diagram's colour factor |

## Further Reading

- [The Feynman Rules of the $\mathrm{SU}(4)$ Model](the-feynman-rules-of-the-su4-model-the-vertices-of-the-fifteen-and-the-sixteen.html). The vertices these three diagrams use, and the normalisation that produced $C_F$.
- [The Fermion–Gauge Vertex in the Quartet Basis](the-fermion-gauge-vertex-in-the-quartet-basis-the-fifteen-read-on-the-sixteen.html). The matrices behind the two leptoquark vertices, with their charges.
- [Lepton Flavour in the $\mathrm{SU}(4)$ Model: Nothing Turns the Lepton](lepton-flavour-in-the-su4-model-nothing-turns-the-lepton.html). The operator, the rate, the $K_L$–$K_S$ selection and the assumption about $U$ in full.
- [The Sextet Put Aside](the-sextet-put-aside-six-leptoquarks-above-m-c-and-why-they-are-not-seen.html). The six states, the $B-L=\pm\tfrac43$, and the dimension-nine argument.
- [The Lagrangian and Quantum Chromodynamics: The Triplet, the Octet and the Feynman Rules](the-lagrangian-and-quantum-chromodynamics-the-triplet-the-octet-and-the-feynman-rules.html). The $C_F$, $T_R$, $N_c$ bookkeeping in its own setting.
- [The S-Matrix in Biquaternionic Form](the-s-matrix-in-biquaternionic-form.html). The contraction that turns a vertex into an amplitude.
- [The Feynman Propagator in Biquaternionic Form](the-feynman-propagator-in-biquaternionic-form.html). The heavy limit used at every leptoquark line.
- [The Commutation Table of the Fifteen Generators](the-commutation-table-of-the-fifteen-generators-225-entries-105-independent-80-nonzero-and-five-rules.html). The closure of the colour block that the gluon diagram relies on.
