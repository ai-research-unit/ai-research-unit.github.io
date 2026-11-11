# __The Standard Model Lagrangian Assembled: Four Sectors in One Expression__

## Introduction

**The claim.** The Standard Model is one Lagrangian, and it is the sum of four sectors. This article writes the four, then the sum. It writes them in the corpus's coordinates, with the unit metric and the derivative $\partial/\partial R_\mu$, and it fixes once the one rule by which a display in this bookkeeping equals a display in the standard bookkeeping.

**The standing.** The expression is standard theory. It is transcribed, not derived, and no term in it follows from the biquaternion algebra. What the article adds to a textbook display is three things: one notation, one sign rule stated and proved, and one audit of gauge invariance carried out term by term.

**Why assembling is not a transcription exercise.** A reader may object that the sum of four published pieces proves nothing, and the objection is correct as stated. The value of the assembly is what it makes possible. Gauge invariance is a property of the sum and not of the pieces: the fermion kinetic term is invariant only if the covariant derivative is built from the same three connections that the gauge kinetic terms carry, and the Yukawa sector is invariant only if the conjugate doublet is used with the right hypercharge. Those are statements about the assembly, and they are checked below, term by term, in one notation.

**Two results, stated now.** The assembly yields two quantitative results that no single-sector article states.

- **The sign rule.** The corpus's bookkeeping and the standard one differ by one identity, $\sum_\mu X_\mu Y_\mu = -X_\mu Y^\mu$, and with it every display below is the standard display. The scalar kinetic term carries a minus sign in the corpus and a plus sign in a standard text, and both are the same term.
- **The redundancy.** Written out, the four sectors and the vacuum-angle term carry sixty real parameters. Physical content is nineteen. Forty-one parameters are removed by field redefinitions that change no physics, and the removal is graded: twenty-six in the quark sector, fifteen in the lepton sector.

**The order.** The four sectors and why there are four, then the dictionary, then the sectors one at a time, then the sum, then the audit, then the count, then what the expression omits, then the corpus's own action beside the standard one.

## Why Four Sectors

**The division is by what each piece needs in order to be invariant.** A term in the Lagrangian is allowed when it is a Lorentz scalar and invariant under $SU(3)_c\times SU(2)_L\times \mathrm{U}(1)_Y$. Terms sort by which of the three connections they carry, and by whether they carry the scalar.

| Sector | Symbol | Carries | Its parameters |
|---|---|---|---|
| Strong | $\mathcal{L}_{\mathrm{QCD}}$ | the colour connection | $g_s$, $\theta_{\mathrm{QCD}}$, six quark masses through the Yukawa sector |
| Electroweak gauge and kinetic | $\mathcal{L}_{\mathrm{EW}}$ | the weak and hypercharge connections | $g$, $g_{\mathrm Y}$, and the fermion kinetic normalisations |
| Scalar | $\mathcal{L}_{H}$ | all three connections, through $D_\mu\varphi$ | $\mu^2$, $\lambda$ |
| Yukawa | $\mathcal{L}_{\mathrm{Yuk}}$ | no connection | the three coupling matrices |

**Why the fourth is not part of the third.** The scalar potential $V(\varphi)$ is invariant on its own, since it depends only on $\varphi^\dagger\varphi$. The Yukawa couplings are invariant only in combination with the fermions and the scalar together. The two are separated because they are fixed by different measurements: the potential by the boson masses, the couplings by the fermion masses and mixings.

**The counting of sectors is a choice of grouping, and a conventional one.** The four-group division is the division of the literature, and it is used here because each group has its own renormalisation and its own set of measurements. A finer division into six or eight pieces would change nothing but the bookkeeping.

## The Dictionary

**One rule governs every display of this article.** The corpus writes coordinates $R_\mu$ with $R_t=Q_t=i q'_t$ on the four components, so the coefficient of the temporal basis element carries the central imaginary and the three spatial coefficients do not. Two consequences follow, and both are proved in one line.

**The rule.** For two sets of four coefficients $X_\mu$, $Y_\mu$ written this way,

$$
-\sum_\mu X_\mu Y_\mu = X_\mu Y^\mu ,
$$

where the right-hand side is contracted with the metric $(+,-,-,-)$ of the interval, $X_0$ is the physical temporal component, and $X_t=iX_0$.

**The proof.** The temporal term is $X_tY_t=(iX_0)(iY_0)=-X_0Y_0$ and the spatial ones are $\sum_\eta X_kY_k$, so the sum $\sum_\mu X_\mu Y_\mu$ equals $-X_0Y_0+\sum_\eta X_kY_k$ and the leading minus makes the left-hand side $X_0Y_0-\sum_\eta X_kY_k$. On the right, the metric $(+,-,-,-)$ gives $X_kY^k=-X_kY_k$, so $X_\mu Y^\mu=X_0Y^0+\sum_\eta X_kY^k=X_0Y_0-\sum_\eta X_kY_k$. The two sides are the same expression.

**The two places it bites.** The rule fixes the sign of a kinetic term and nothing else in this article.

- **The scalar.** A text in the standard metric writes $+\tfrac12\partial_\mu\xi\partial^\mu\xi$ for a real scalar. The rule turns it into $-\tfrac12\sum_\mu\partial_\mu\xi\,\partial_\mu\xi$, which is exactly the corpus's scalar Lagrangian of [Stress–Energy Conservation Laws and the Field Action](stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.html), whose expansion $-\tfrac12[-\left(\partial\xi/\partial r'_t\right)^2+(\nabla\xi)^2]$ is the standard $\tfrac12\dot\xi^2-\tfrac12(\nabla\xi)^2$.
- **The gauge field.** A text writes $-\tfrac14F_{\mu\nu}F^{\mu\nu}$. The rule turns it into $-\tfrac14\sum_{\mu,\nu}F_{\mu\nu}F_{\mu\nu}$, which is the corpus's display. Here the sign is unchanged, because the double sum over two indices cancels the single flip.

**The check that the two writings are one Lagrangian.** With $A_t=iA_0$ and $F_{\mu\nu}=\partial A_\nu/\partial R_\mu-\partial A_\mu/\partial R_\nu$, the temporal components are $F_{t\eta}=iE_\eta$ and the spatial ones are $F_{\eta l}=\epsilon_{\eta lm}B_m$. Then $\sum_{\mu\nu}F_{\mu\nu}F_{\mu\nu}=2\sum_\eta F_{t\eta}F_{t\eta}+\sum_{\eta l}F_{\eta l}F_{\eta l}=-2E^2+2B^2$, and $-\tfrac14$ of that is $\tfrac12(E^2-B^2)$, which is the standard $-\tfrac14F_{\mu\nu}F^{\mu\nu}$ evaluated on the same fields. The energy comes out positive in both writings; the corpus's own stress–energy article fixes the sign on that requirement.

**The derivative.** The corpus writes $\partial/\partial R_\mu$, and the time derivative of a material coordinate is $\partial/\partial r'_t=-i\,\partial/\partial R_t$. The two are never mixed in one display. A fermion bilinear's sign, which the rule does not fix because the bilinear carries the spin structure, is the subject of [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) and is quoted there rather than restated here.

## The Gauge Sector

**The field strengths.** Each factor of the product carries one,

$$
G^a_{\mu\nu}=\frac{\partial G^a_\nu}{\partial R_\mu}-\frac{\partial G^a_\mu}{\partial R_\nu}+g_s\sum_{b,c}f_{abc}G^b_\mu G^c_\nu ,
$$

$$
W^a_{\mu\nu}=\frac{\partial W^a_\nu}{\partial R_\mu}-\frac{\partial W^a_\mu}{\partial R_\nu}+g\sum_{b,c}\varepsilon_{abc}W^b_\mu W^c_\nu ,
\qquad
B_{\mu\nu}=\frac{\partial B_\nu}{\partial R_\mu}-\frac{\partial B_\mu}{\partial R_\nu} .
$$

The colour structure constants are $f_{abc}$ and the weak ones are $\varepsilon_{abc}$ in the normalised basis. The two non-abelian curvatures carry the same commutator term in the same form; the abelian one does not, because its structure constants vanish.

**The kinetic terms.** Three, one per factor,

$$
\mathcal{L}_{\mathrm{gauge}}=-\tfrac14\sum_{a,\mu,\nu}G^a_{\mu\nu}G^a_{\mu\nu}-\tfrac14\sum_{a,\mu,\nu}W^a_{\mu\nu}W^a_{\mu\nu}-\tfrac14\sum_{\mu,\nu}B_{\mu\nu}B_{\mu\nu} .
$$

The three coefficients are equal because each factor's gauge field is normalised so that its kinetic term has unit coefficient. That normalisation is what makes the three couplings independent numbers; a rescaling of any one field moves a constant between the kinetic term and the coupling, and the product $g_sF$ is what the physics sees.

**Three, not one.** The three kinetic terms do not mix. A term $G_{\mu\nu}W_{\mu\nu}$ would be forbidden by the product structure, since the two fields carry different quantum numbers and no invariant contraction exists. Mixing of the neutral fields happens at the level of the mass matrix and the currents, not at the level of the kinetic terms, and the mixing is a rotation of $W^3_\mu$ and $B_\mu$ that leaves the kinetic terms in the form above.

## The Fermion Sector

**The term.** One term per Weyl field, in the form

$$
\mathcal{L}_{\mathrm{ferm}}=\sum_{\psi}\bar{\tilde\Xi}_{\mathrm{sp},\psi}\,i\,\tilde\nabla_{\psi}\,\tilde\Xi_{\mathrm{sp},\psi} ,
$$

with $\bar{\tilde\Xi}_{\mathrm{sp}}=\tilde\Xi_{\mathrm{sp}}^{*}i\vec e_x$ the Dirac adjoint of the corpus, and $\tilde\nabla_\psi$ the covariant gradient carrying the three connections in the representation of $\psi$. The display states the structure; the component form of $\tilde\nabla_\psi$ and the sign of the bilinear are the Dirac article's, where the massless pair is $\tilde\nabla_\Phi\tilde\Xi_{\mathrm{sp},R}=0$ and $(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_{\mathrm{sp},L}=0$.

**The covariant gradient.** Its action on a field in the representation $(\mathbf{3}$ or $\mathbf{1},\mathbf{2}$ or $\mathbf{1},Y)$ is

$$
\tilde\nabla_{\psi}\tilde\Xi_{\mathrm{sp},\psi}=\tilde\nabla_\Phi\tilde\Xi_{\mathrm{sp},\psi}+\frac{i\,ϙ}{\hbar}\Bigl(\sum_a T^a_\psi G^a+\sum_a\tau^a_\psi W^a+Y_\psi B\Bigr)\tilde\Xi_{\mathrm{sp},\psi} ,
$$

with $T^a_\psi$ the colour generators in the representation of $\psi$ and $\tau^a_\psi$ the weak ones. The bracket is the connection in that representation, and it is the same object for all fifteen fields of a generation, differing only in which generators act and with which hypercharge.

**Why the term is one term and not fifteen.** The fifteen Weyl fields of a generation carry fifteen different connections and fifteen different hypercharges, so the display above is fifteen terms in one line. That is the whole of the fermion sector: a kinetic term per field, and no mass term.

**No mass term.** The reason is recorded in article 1 and repeated here because it is the hinge of the assembly. A term $m\bar{\tilde\Xi}_{\mathrm{sp}}\tilde\Xi_{\mathrm{sp}}$ couples a left-handed field to a right-handed one, and the two carry different $SU(2)_L$ representations and different hypercharges, so no invariant contraction exists. The mass must wait for the scalar, and it arrives through the Yukawa sector.

## The Scalar Sector

**The field and its potential.** One complex doublet,

$$
\varphi=\begin{pmatrix}\varphi^+\\ \varphi^0\end{pmatrix},
\qquad
Y_\varphi=\tfrac12 ,
$$

with the potential and the kinetic term

$$
\mathcal{L}_{H}=-\sum_\mu\left(D_\mu\varphi\right)^{\dagger}\left(D_\mu\varphi\right)+\mu^2\varphi^{\dagger}\varphi-\lambda\left(\varphi^{\dagger}\varphi\right)^2 ,
\qquad
D_\mu\varphi=\frac{\partial\varphi}{\partial R_\mu}+i\frac{g}{2}\sum_a\tau_aW^a_\mu\varphi+i\frac{g_{\mathrm Y}}{2}B_\mu\varphi .
$$

The signs are the corpus's, by the rule of §*The Dictionary*: the kinetic term carries the minus, and the potential appears with $+\mu^2$ and $-\lambda$ because $\mathcal{L}\supset -V$.

**The sign of $\mu^2$.** A positive $\mu^2$ gives a potential with a maximum at the origin and a circle of minima away from it. That sign is the whole content of spontaneous breaking: the field settles on the circle, and the theory is read around a point of it. A negative $\mu^2$ would give a single minimum at the origin and no breaking.

**The minimum.** The potential depends on $\varphi$ only through $\varphi^\dagger\varphi$, so its minima form a three-sphere in the four real components. Writing $\varphi^\dagger\varphi=\tfrac12v^2$,

$$
v^2=\frac{\mu^2}{\lambda} ,
\qquad
\langle\varphi\rangle=\frac{1}{\sqrt2}\begin{pmatrix}0\\ v\end{pmatrix},
\qquad
v=246.22\ \mathrm{GeV} .
$$

The value of $v$ is not computed here; it is the entry 18 of the parameter table of article 1, fixed by the Fermi constant.

**What the sector supplies.** Three things, and they are computed in [Electroweak Symmetry Breaking: the Doublet, the Potential and the Gauge-Boson Masses](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-gauge-boson-masses.html) rather than here: the masses $M_W=\tfrac12gv$ and $M_Z=\tfrac12\sqrt{g^2+g_{\mathrm Y}^2}\,v$, the massless photon, and the scalar mass $M_H=\sqrt{2\lambda}\,v$. Recomputed from the table, $\lambda=M_H^2/(2v^2)=0.1291$ for $M_H=125.09$ GeV, and the three masses then follow from $g$, $g_{\mathrm Y}$, $v$ and $\lambda$.

**Four real components, three eaten.** The doublet carries four real fields. Three are the Goldstones that the $W^+$, $W^-$ and $Z$ absorb as longitudinal polarisations; the fourth is the physical scalar. The degree-of-freedom count closes: twenty-eight before breaking, twenty-eight after.

## The Yukawa Sector

**The term.** Three coupling matrices, one per fermion type,

$$
\mathcal{L}_{\mathrm{Yuk}}=-\sum_{a,b}\Bigl(\bar Q_{L,a}\varphi\,Y^{d}_{ab}\,d_{R,b}+\bar Q_{L,a}\tilde\varphi\,Y^{u}_{ab}\,u_{R,b}+\bar L_{L,a}\varphi\,Y^{e}_{ab}\,e_{R,b}\Bigr)+\text{h.c.},
$$

with $a,b=1,2,3$ the generation labels and $Y^{u}$, $Y^{d}$, $Y^{e}$ general complex $3\times3$ matrices.

**The conjugate doublet.** The up-type term cannot use $\varphi$, and this is the one place in the assembly where a second scalar object is needed. The conjugate doublet is

$$
\tilde\varphi=\begin{pmatrix}\varphi^{0*}\\ -\varphi^{+*}\end{pmatrix},
\qquad
Y_{\tilde\varphi}=-\tfrac12 ,
$$

and it is not an independent field: it is the same doublet read through the conjugate. Its hypercharge is the negative of $\varphi$'s, and that is what makes the up-type term invariant.

**The hypercharge audit.** Each term must carry total hypercharge zero, and each does:

| Term | $Y$ of the left factor | $Y$ of the scalar | $Y$ of the right factor | Sum |
|---|---|---|---|---|
| $\bar Q_L\varphi\,d_R$ | $-1/6$ | $+1/2$ | $-1/3$ | $0$ |
| $\bar Q_L\tilde\varphi\,u_R$ | $-1/6$ | $-1/2$ | $+2/3$ | $0$ |
| $\bar L_L\varphi\,e_R$ | $+1/2$ | $+1/2$ | $-1$ | $0$ |

**The masses after breaking.** With $\langle\varphi\rangle=(0,v/\sqrt2)$, each matrix becomes a mass matrix,

$$
M_f=\frac{v}{\sqrt2}\,Y^{f},
\qquad
f=u,d,e ,
$$

and the physical masses are the singular values of $M_f$, obtained by bi-unitary diagonalisation. That step, and the two unitary factors that survive it as the CKM and PMNS matrices, is the subject of [The Yukawa Sector: Fermion Mass Matrices and Their Diagonalisation](the-yukawa-sector-fermion-mass-matrices-and-their-diagonalisation.html).

**Why the sector exists at all.** Without it the fermions are massless, which the world is not. With it, the masses are free parameters, which is the price. There is no third option inside the renormalisable model: a mass term without the scalar is forbidden by the gauge symmetry, and a mass term generated in any other way requires new fields.

## The Assembled Expression

**The sum.** The four sectors add to

$$
\boxed{\;
\begin{aligned}
\mathcal{L}_{\mathrm{SM}}={}&-\tfrac14\sum_{a,\mu,\nu}G^a_{\mu\nu}G^a_{\mu\nu}-\tfrac14\sum_{a,\mu,\nu}W^a_{\mu\nu}W^a_{\mu\nu}-\tfrac14\sum_{\mu,\nu}B_{\mu\nu}B_{\mu\nu}\\[2pt]
&+\sum_{\psi}\bar{\tilde\Xi}_{\mathrm{sp},\psi}\,i\,\tilde\nabla_{\psi}\,\tilde\Xi_{\mathrm{sp},\psi}\\[2pt]
&-\sum_\mu\left(D_\mu\varphi\right)^{\dagger}\left(D_\mu\varphi\right)+\mu^2\varphi^{\dagger}\varphi-\lambda\left(\varphi^{\dagger}\varphi\right)^2\\[2pt]
&-\sum_{a,b}\Bigl(\bar Q_{L,a}\varphi\,Y^{d}_{ab}\,d_{R,b}+\bar Q_{L,a}\tilde\varphi\,Y^{u}_{ab}\,u_{R,b}+\bar L_{L,a}\varphi\,Y^{e}_{ab}\,e_{R,b}\Bigr)+\text{h.c.}\\[2pt]
&+\frac{\theta_{\mathrm{QCD}}}{32\pi^2}\sum_{\mu,\nu,a}G^a_{\mu\nu}G^a_{\mathrm{dual},\mu\nu} .
\end{aligned}
\;}
$$

**The fifth line.** The vacuum-angle term belongs to the strong sector and is separated for a reason: it is a total derivative, so it changes no equation of motion, and its effect is entirely quantum. It is written in the normalisation of [The Theta Parameter and Strong CP in Biquaternionic Form](the-theta-parameter-and-strong-cp-in-biquaternionic-form.html), with $G^a_{\mathrm{dual},\mu\nu}=\tfrac12\sum_{\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}G^a_{\rho\sigma}$.

**What the display is.** It is a Lagrangian density of dimension four, and every term in it is either a kinetic term or a term of the same dimension. That is not an accident of the list; it is the definition of renormalisability, and the next section counts what the condition permits.

**The two structural facts visible in the sum.** First, every term carrying a derivative carries a connection, and no term carries a connection without a derivative; that is the statement that the connections enter only through covariant derivatives and field strengths. Second, the only term that is not a modulus squared or a product of two field strengths is the $\theta$ term, and it is a total derivative. Those two facts are what make the audit of the next section short.

## The Gauge-Invariance Audit

**What is checked.** Each term of the sum is checked separately, under the three local transformations

$$
\psi\mapsto e^{iY_\psi\alpha(x)}\,U_c(x)\,U_L(x)\,\psi ,
\qquad
G_\mu\mapsto U_cG_\mu U_c^{\dagger}+\frac{i}{g_s}U_c\frac{\partial U_c^{\dagger}}{\partial R_\mu} ,
$$

and the analogous laws for $W_\mu$ with $U_L$ and for $B_\mu$ with the phase alone. $U_L$ acts as the identity on right-handed fields.

| Term | How it transforms | Why it is invariant |
|---|---|---|
| $-\tfrac14G^a_{\mu\nu}G^a_{\mu\nu}$ | $G_{\mu\nu}\mapsto U_cG_{\mu\nu}U_c^{\dagger}$ | the trace of a product is cyclic, and $U_c^{\dagger}U_c=1$ |
| $-\tfrac14W^a_{\mu\nu}W^a_{\mu\nu}$ | $W_{\mu\nu}\mapsto U_LW_{\mu\nu}U_L^{\dagger}$ | the same |
| $-\tfrac14B_{\mu\nu}B_{\mu\nu}$ | $B_{\mu\nu}\mapsto B_{\mu\nu}$ | the abelian curvature is a derivative of a scalar phase |
| fermion kinetic | $\bar{\tilde\Xi}\mapsto\bar{\tilde\Xi}U^{\dagger}$, $\tilde\nabla_\Phi\tilde\Xi\mapsto U\tilde\nabla_\Phi\tilde\Xi$ | $U^{\dagger}U=1$, and the derivative is covariant |
| scalar kinetic | $D_\mu\varphi\mapsto U_\varphi D_\mu\varphi$ | the same, with the scalar's representation |
| potential $\mu^2\varphi^\dagger\varphi-\lambda(\varphi^\dagger\varphi)^2$ | $\varphi^\dagger\varphi\mapsto\varphi^\dagger\varphi$ | the invariant is the modulus squared, a singlet |
| Yukawa, down type | the three factors transform by $U_Q^{\dagger}$, $U_\varphi$, $U_d$ | the product is $U_Q^{\dagger}U_\varphi U_d$, and the $SU(2)$ contraction is the singlet |
| Yukawa, up type | the same with $U_{\tilde\varphi}$ | $U_{\tilde\varphi}$ is the conjugate of $U_\varphi$, and the phase is opposite |
| $\theta$ term | invariant | $G_{\mu\nu}$ is adjoint-valued, and the epsilon contraction is a colour singlet |

**The three places where the audit could fail and does not.**

- **The fermion kinetic term needs all three connections.** If the covariant derivative carried only the hypercharge connection, the term would fail under $SU(2)_L$ and $SU(3)_c$. The invariance of this term is what forces the gauge fields to be the same objects that appear in the three kinetic terms, and that is the content of calling the theory a gauge theory rather than three separate ones.
- **The up-type Yukawa needs the conjugate doublet.** With $\varphi$ in place of $\tilde\varphi$, the total hypercharge would be $-1/6+1/2+2/3=+1$, and the term would not be invariant. The conjugate is forced.
- **The potential needs the modulus squared and nothing else.** A term $\varphi^T\varphi$ or $\varphi^\dagger\tau_a\varphi$ would fail; only $\varphi^\dagger\varphi$ is a singlet. That is why the potential has two parameters and not more.

**The one term that is not invariant, and must not be there.** A bare mass $m\bar{\tilde\Xi}_{\mathrm{sp}}\tilde\Xi_{\mathrm{sp}}$ fails the audit: the left factor transforms as a doublet and the right as a singlet, so the product carries an $SU(2)_L$ index that nothing contracts. A bare mass for the neutrino fails for the same reason. Their absence is a result of the audit and not an omission from it.

**The audit is complete.** Every term of the sum has been checked, and no term of dimension four compatible with the symmetries has been left out. The last claim is the one that needs the count of the next section, and the count is of operators and not of terms: the renormalisable operators are the ones built from at most four fields and at most one derivative each, and the list above exhausts them once the field content of article 1 is fixed.

## Sixty Parameters Written, Nineteen Physical

**Why the count matters.** The Lagrangian above is written with more numbers than the model has. Every field can be redefined, and a redefinition changes the coupling matrices without changing any observable. The count of what survives is the count of article 1, and the difference is the redundancy.

**What is written.** Counting real numbers,

| Object | Real parameters |
|---|---|
| $g_s$, $g$, $g_{\mathrm Y}$ | $3$ |
| $\mu^2$, $\lambda$ | $2$ |
| $\theta_{\mathrm{QCD}}$ | $1$ |
| $Y^{u}$, $Y^{d}$ | $2\times18=36$ |
| $Y^{e}$ | $18$ |
| **total written** | $\mathbf{60}$ |

Each $3\times3$ complex matrix carries nine complex entries, that is eighteen real numbers, and nothing constrains them.

**What removes them.** A field redefinition is a change of basis in flavour space, and the group that acts is a product of unitary groups, one factor per multiplet type, minus the factors that are symmetries of the whole theory.

| Sector | Written | Group acting | Stabiliser | Physical |
|---|---|---|---|---|
| quarks | $36$ | $U(3)_Q\times U(3)_u\times U(3)_d$, dimension $27$ | $U(1)_B$, dimension $1$ | $36-27+1=10$ |
| leptons | $18$ | $U(3)_L\times U(3)_e$, dimension $18$ | $U(1)^3$, dimension $3$ | $18-18+3=3$ |

**The rule of the count.** The physical number is the written number less the dimension of the group that acts, plus the dimension of the subgroup that leaves the couplings in their diagonal form. The last term is not a fudge: after diagonalisation a residual abelian group remains, and it acts on nothing.

**The quark result.** Ten is six masses plus three angles plus one phase. Rephasing absorbs the five relative phases of three quark fields, $2N-1=5$ for $N=3$, and the ten that remain are the entries of article 1.

**The lepton result.** Three is three masses and no mixing, because the minimal model has no right-handed neutrino and the lepton mixing matrix is then unobservable: it can be rotated away into the charged-lepton fields.

**The total.** The two flavour blocks give thirteen, and with the six of the gauge, scalar and vacuum sectors the count is nineteen, which is the table of article 1. The reduction is $60\to19$, and the forty-one removed numbers are not small corrections: they are the entire freedom of choice of flavour basis.

**What the count does not do.** It does not say that the nineteen are independent in nature; it says that the Lagrangian has nineteen degrees of freedom once the field basis is fixed. Relations among the nineteen — a mass ratio, a mixing angle predicted from masses — would be physics beyond the count, and the model supplies none.

**A second redundancy, inside the mass sector.** The pair $(\mu^2,\lambda)$ and the pair $(v,M_H)$ carry the same information, through $v^2=\mu^2/\lambda$ and $M_H^2=2\lambda v^2=2\mu^2$. Likewise $(g,g_{\mathrm Y})$ and $(e,\theta_W)$ through $e=g\sin\theta_W=g_{\mathrm Y}\cos\theta_W$. The count is of information and not of symbols, and a change of variables moves numbers between columns without changing the total.

## What the Expression Omits

**Three omissions, and each is a measurement.** The expression above is the renormalisable Standard Model with massless neutrinos and no dark sector. Each omission has an experimental warrant and a price.

- **Neutrino masses.** The dimension-five operator $\frac{c_{ab}}{\Lambda}\left(L_{L,a}^T\,i\tau_2\,\varphi\right)\left(L_{L,b}^T\,i\tau_2\,\varphi\right)$ is invariant under all three factors and gives a Majorana mass after breaking. The two insertions are $\varphi$ and not $\tilde\varphi$, because the hypercharge has to close: $-\tfrac12-\tfrac12+\tfrac12+\tfrac12=0$, whereas two conjugate doublets of hypercharge $-\tfrac12$ would give $-2$. The $i\tau_2$ contracts the two weak doublets into a singlet, and the transpose pairs the two left-handed spinors into a Lorentz scalar, so the operator is a singlet under every factor. It is the unique dimension-five operator the field content allows, and it is absent because it is not renormalisable. Adding it, or adding right-handed neutrinos, costs the seven or eight parameters that article 1 counts.
- **Gravity.** No term of the sum couples to the metric. The framework's own gravitational sector is a separate construction, and the Standard Model is written on a fixed background.
- **Dark matter and the matter excess.** No field in the content is a dark-matter candidate, and the $\theta$ term's $B+L$ violation is the only source of baryon-number violation in the expression. Both gaps are the subject of [What the Standard Model Does Not Explain: Dark Matter, Baryogenesis and the Sphaleron](what-the-standard-model-does-not-explain-dark-matter-baryogenesis-and-the-sphaleron.html).

**What is not omitted, and is often said to be.** The $\theta$ term is in the expression, and it is a parameter. Its smallness is a problem, not an omission.

**The status of the omissions.** They are not defects of the assembly. The assembly is complete as the renormalisable theory of the given field content, and the omissions are the statement that the given content is not the whole of nature.

## The Corpus's Own Action Beside the Standard One

**Three sectors out of four.** The corpus writes a gauge action, a scalar action and a fermion action, and the first two are the standard ones term for term.

| Standard object | Corpus object | Identity |
|---|---|---|
| $-\tfrac14F_{\mu\nu}F^{\mu\nu}$ | $-\tfrac14\sum_{\mu,\nu}F_{\mu\nu}F_{\mu\nu}$ | the same, by §*The Dictionary* |
| $+\tfrac12\partial_\mu\xi\partial^\mu\xi$ | $-\tfrac12\sum_\mu\partial_\mu\xi\,\partial_\mu\xi$ | the same, by §*The Dictionary* |
| $\lvert D_\mu\varphi\rvert^2$ | $-\sum_\mu(D_\mu\varphi)^\dagger(D_\mu\varphi)$ | the same |
| the Dirac kinetic term, $\bar\psi\,iD_\mu\psi$ | $\bar{\tilde\Xi}_{\mathrm{sp}}\,i\tilde\nabla_\kappa\tilde\Xi_{\mathrm{sp}}$ | the Dirac article's pair |
| $\varphi^\dagger\varphi$ | $\tilde\Xi\tilde\Xi^{\natural}$ | the norm of an element |

**The dictionary is a dictionary and not a theory.** Each row is an identity between two writings of one object, and none of them is a derivation. The corpus's contribution is that the objects have homes: the connection is a material-sector element, the curvature is its vector part under $\natural$, the scalar is an element and its modulus squared is the norm.

**The sector with no corpus counterpart.** The colour sector is the exception. The algebra's ceiling is $SU(2)$, reached as the norm-one part of the material sector, and no element of $\mathbb{B}$ carries three colours. The QCD Lagrangian is therefore written in this article in a notation the algebra supplies for the spacetime indices only; the colour indices are external to it. That is stated in [The Gauge Group Ceiling](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html) and in [The Gluon: An Octet Outside the Biquaternion Algebra](the-gluon-an-octet-outside-the-biquaternion-algebra.html), and it is the one structural asymmetry of the assembly.

**The parameter ledger, stated once.** Three of the four sectors are writable in the corpus's language and none of the nineteen parameters is fixed by it. The assembly therefore measures the boundary as sharply as the parameter table does: the algebra supplies the arena in which three of these four expressions are written, and it supplies no coefficient.

## Summary

The Standard Model Lagrangian is the sum of four sectors plus the vacuum-angle term: the three gauge kinetic terms $-\tfrac14\sum G G$, $-\tfrac14\sum W W$, $-\tfrac14\sum BB$; one fermion kinetic term per Weyl field, fifteen per generation, each built on the covariant gradient carrying the connection in that field's representation; the scalar kinetic term and the potential $-\sum_\mu(D_\mu\varphi)^\dagger(D_\mu\varphi)+\mu^2\varphi^\dagger\varphi-\lambda(\varphi^\dagger\varphi)^2$; and the three Yukawa matrices with the conjugate doublet $\tilde\varphi$ of hypercharge $-\tfrac12$ in the up-type term. The assembly is one notation and one sign rule.

The sign rule is $\sum_\mu X_\mu Y_\mu=-X_\mu Y^\mu$, proved in one line from $X_t=iX_0$ and the metric of the interval. It converts the corpus's $-\tfrac12\sum\partial\xi\partial\xi$ into the standard $+\tfrac12\partial_\mu\xi\partial^\mu\xi$, converts its $-\tfrac14\sum FF$ into the standard $-\tfrac14F_{\mu\nu}F^{\mu\nu}$ with no change of sign, and leaves the two writings one Lagrangian: the abelian check gives $\sum_{\mu\nu}F_{\mu\nu}F_{\mu\nu}=2(B^2-E^2)$ and hence $\tfrac12(E^2-B^2)$ on both sides.

The audit is term by term and it passes. The three kinetic terms are invariant because each curvature transforms in the adjoint; the fermion and scalar kinetic terms because each covariant derivative transforms with the same unitary that acts on its field; the potential because it depends only on the singlet $\varphi^\dagger\varphi$; the Yukawa terms because the total hypercharge vanishes in each of the three, $-1/6+1/2-1/3$, $-1/6-1/2+2/3$ and $+1/2+1/2-1$; and the vacuum-angle term because it is a colour singlet. A bare fermion mass fails the audit, and its absence is a result and not an omission.

Written out, the four sectors and the vacuum-angle term carry sixty real parameters: three couplings, two scalar parameters, one vacuum angle, eighteen for $Y^e$ and thirty-six for the pair $Y^u,Y^d$. Field redefinitions remove forty-one of them — twenty-six in the quark sector through $U(3)_Q\times U(3)_u\times U(3)_d$ leaving ten, which is six masses and four mixing parameters, and fifteen in the lepton sector through $U(3)_L\times U(3)_e$ leaving three masses — so nineteen survive, which is the table of article 1. The redundancy is a freedom of flavour basis and not a small correction.

The expression omits neutrino masses, gravity and a dark sector, and each omission is a measurement rather than an oversight. The unique dimension-five operator the content allows is the neutrino mass, and it is absent only because the theory is written renormalisable. Three of the four sectors have corpus counterparts term for term, through the dictionary of this article; the colour sector has none, because the algebra's ceiling is $SU(2)$. The assembly therefore closes the ledger the parameter table opened: the arena is the algebra's, and all sixty coefficients written here are imported.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{L}_{\mathrm{QCD}}$, $\mathcal{L}_{\mathrm{EW}}$, $\mathcal{L}_{H}$, $\mathcal{L}_{\mathrm{Yuk}}$ | The four sectors |
| $G^a_\mu$, $W^a_\mu$, $B_\mu$ | Colour, weak and hypercharge gauge fields |
| $G^a_{\mu\nu}$, $W^a_{\mu\nu}$, $B_{\mu\nu}$ | Their field strengths |
| $f_{abc}$, $\varepsilon_{abc}$ | Colour and weak structure constants |
| $\tilde\nabla_\psi$ | The covariant gradient in the representation of $\psi$ |
| $\bar{\tilde\Xi}_{\mathrm{sp}}=\tilde\Xi_{\mathrm{sp}}^{*}i\vec e_x$ | The Dirac adjoint |
| $\varphi$, $\tilde\varphi$ | The scalar doublet of hypercharge $\tfrac12$ and its conjugate of hypercharge $-\tfrac12$ |
| $Y^{u}$, $Y^{d}$, $Y^{e}$ | The three Yukawa matrices, general complex $3\times3$ |
| $M_f=vY^{f}/\sqrt2$ | The mass matrix of the fermion type $f$ |
| $\mu^2$, $\lambda$ | The two parameters of the potential |
| $v^2=\mu^2/\lambda$ | The vacuum expectation value, $246.22$ GeV |
| $M_H=\sqrt{2\lambda}\,v$ | The scalar mass |
| $\theta_{\mathrm{QCD}}$ | The vacuum angle |
| $G^a_{\mathrm{dual},\mu\nu}=\tfrac12\sum_{\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}G^a_{\rho\sigma}$ | The dual field strength |
| $\sum_\mu X_\mu Y_\mu=-X_\mu Y^\mu$ | The sign rule of §*The Dictionary* |
| $\partial/\partial R_\mu$ | The corpus derivative, with $\partial/\partial r'_t=-i\partial/\partial R_t$ |

## Further Reading

- [The Standard Model: Content, Quantum Numbers and the Nineteen Parameters](the-standard-model-content-quantum-numbers-and-the-nineteen-parameters.html). The field content this expression is written for, and the nineteen that survive the count.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html). The connection, the covariant derivative and the curvature, from which the three kinetic terms are read.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html). The fermion pair and the covariant gradient, whose component form this article quotes and does not restate.
- [The Higgs Mechanism in Biquaternionic Form](the-higgs-mechanism-in-biquaternionic-form.html). The abelian case, which the scalar sector of this article generalises to the doublet.
- [Stress–Energy Conservation Laws and the Field Action in Biquaternionic Form](stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.html). The scalar action and the sign convention that fixes the dictionary.
- [The Theta Parameter and Strong CP in Biquaternionic Form](the-theta-parameter-and-strong-cp-in-biquaternionic-form.html). The normalisation of the fifth line and its status as a total derivative.
- [The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html). The one sector with no corpus counterpart.
- [The Gluon: An Octet Outside the Biquaternion Algebra](the-gluon-an-octet-outside-the-biquaternion-algebra.html). The colour sector at the level of the field.
- [The Standard Model under the Biquaternion Framework — A Research Agenda](the-standard-model-under-the-biquaternion-framework-a-research-agenda.html). Which terms the framework reaches and which it imports.

The three companions this article names but does not carry — the QCD Lagrangian, gauge fixing and the electroweak precision observables — are written, as articles 9, 7 and 8 of the series, and each is linked above at the point where it is invoked.
