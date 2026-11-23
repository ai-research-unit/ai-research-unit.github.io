# __The Standard Model and the Lagrangian: Four Sectors in One Expression__

## Introduction

The claim. The Standard Model is one Lagrangian, and it is the sum of four sectors. This article writes the four, then the sum. It writes them in the corpus's coordinates, with the unit metric and the derivative $\partial/\partial R_{\imath}$, and it fixes once the one rule by which a display in this bookkeeping equals a display in the standard bookkeeping.

The standing. The expression is standard theory. It is transcribed, not derived, and no term in it follows from the biquaternion algebra. What the article adds to a textbook display is three things: one notation, one sign rule stated and proved, and one audit of gauge invariance carried out term by term.

Why assembling is not a transcription exercise. A reader may object that the sum of four published pieces proves nothing, and the objection is correct as stated. The value of the assembly is what it makes possible. Gauge invariance is a property of the sum and not of the pieces: the fermion kinetic term is invariant only if the covariant derivative is built from the same three connections that the gauge kinetic terms carry, and the Yukawa sector is invariant only if the conjugate doublet is used with the right hypercharge. Those are statements about the assembly, and they are checked below, term by term, in one notation.

Two results, stated now. The assembly yields two quantitative results that no single-sector article states.

- The sign rule. The corpus's bookkeeping and the standard one differ by one identity, $\sum_{\imath} X_{\imath} Y_{\imath} = -X\cdot Y$, and with it every display below is the standard display. The dot is the text's contraction, written without an index placement; the series never prints it as a raised index. The scalar kinetic term carries a minus sign in the corpus and a plus sign in a standard text, and both are the same term.
- The redundancy. Written out, the four sectors and the vacuum-angle term carry sixty real parameters. Physical content is nineteen. Forty-one parameters are removed by field redefinitions that change no physics, and the removal is graded: twenty-six in the quark sector, fifteen in the lepton sector.

The order. The four sectors and why there are four, then the dictionary, then the sectors one at a time, then the sum, then the audit, then the count, then what the expression omits, then the corpus's own action beside the standard one.

## Why Four Sectors

**The division is by what each piece needs in order to be invariant.** A term in the Lagrangian is allowed when it is a Lorentz scalar and invariant under $SU(3)_c\times SU(2)_L\times \mathrm{U}(1)_Y$. Terms sort by which of the three connections they carry, and by whether they carry the scalar.

| Sector | Symbol | Carries | Its parameters |
|---|---|---|---|
| Strong | $\mathcal{L}_{\mathrm{QCD}}$ | the colour connection | $g_s$, $\theta_{\mathrm{QCD}}$, six quark masses through the Yukawa sector |
| Electroweak gauge and kinetic | $\mathcal{L}_{\mathrm{EW}}$ | the weak and hypercharge connections | $g$, $g_{\mathrm Y}$, and the fermion kinetic normalisations |
| Scalar | $\mathcal{L}_{H}$ | all three connections, through $D_{\imath}\omicron_{\mathrm{hgs}}$ | $\mu^2$, $\varpi_{\mathrm{cpl}}$ |
| Yukawa | $\mathcal{L}_{\mathrm{Yuk}}$ | no connection | the three coupling matrices |

Why the fourth is not part of the third. The scalar potential $V(\omicron_{\mathrm{hgs}})$ is invariant on its own, since it depends only on $\omicron_{\mathrm{hgs}}^\dagger\omicron_{\mathrm{hgs}}$. The Yukawa couplings are invariant only in combination with the fermions and the scalar together. The two are separated because they are fixed by different measurements: the potential by the boson masses, the couplings by the fermion masses and mixings.

The counting of sectors is a choice of grouping, and a conventional one. The four-group division is the division of the literature, and it is used here because each group has its own renormalisation and its own set of measurements. A finer division into six or eight pieces would change nothing but the bookkeeping.

## The Dictionary

One rule governs every display of this article. The corpus writes coordinates $R_{\imath}$ with $R_t=Q_t=i q'_t$ on the four components, so the coefficient of the temporal basis element carries the central imaginary and the three spatial coefficients do not. Two consequences follow, and both are proved in one line.

**The rule.** For two sets of four coefficients $X_{\imath}$, $Y_{\imath}$ written this way,

$$
-\sum_{\imath} X_{\imath} Y_{\imath} = X\cdot Y ,
$$

where the right-hand side is contracted with the metric $(+,-,-,-)$ of the interval, $X_0$ is the physical temporal component, and $X_t=iX_0$.

The proof. The temporal term is $X_tY_t=(iX_0)(iY_0)=-X_0Y_0$ and the spatial ones are $\sum_{\imath\in\{x,y,z\}} X_\imathY_\imath$, so the sum $\sum_{\imath} X_{\imath} Y_{\imath}$ equals $-X_0Y_0+\sum_{\imath\in\{x,y,z\}} X_\imathY_\imath$ and the leading minus makes the left-hand side $X_0Y_0-\sum_{\imath\in\{x,y,z\}} X_\imathY_\imath$. On the right, the text's contraction carries the metric $(+,-,-,-)$, which puts a minus on each spatial term, so $X\cdot Y=X_0Y_0-\sum_{\imath\in\{x,y,z\}} X_\imathY_\imath$. The two sides are the same expression.

The two places it bites. The rule fixes the sign of a kinetic term and nothing else in this article.

- The scalar. A text in the standard metric writes $+\tfrac12\partial\xi\cdot\partial\xi$ for a real scalar. The rule turns it into $-\tfrac12\sum_{\imath}\partial_{\imath}\xi\,\partial_{\imath}\xi$, which is exactly the corpus's scalar Lagrangian of [Stress–Energy Conservation Laws and the Field Action](stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.html), whose expansion $-\tfrac12[-\left(\partial\xi/\partial r'_t\right)^2+(\vec\nabla_\Phi\xi)^2]$ is the standard $\tfrac12\dot\xi^2-\tfrac12(\vec\nabla_\Phi\xi)^2$.
- The gauge field. A text writes $-\tfrac14F\cdot F$. The rule turns it into $-\tfrac14\sum_{\imath,\jmath}\varepsilon_{\imath}\varepsilon_{\jmath} F_{\imath\jmath}F_{\imath\jmath}$, which is the corpus's display. Here the sign is unchanged, because the weight over the two indices cancels the flip.

The check that the two writings are one Lagrangian. With $A_t=iA_0$ and $F_{\imath\jmath}=\partial A_{\jmath}/\partial R_{\imath}-\partial A_{\imath}/\partial R_{\jmath}$, the temporal components are $F_{tk}=iE_\imath$ and the spatial ones are $F_{\imath l}=\epsilon_{k l\,n_{\mathrm{idx}}}B_m$. Then $\sum_{\imath\jmath}F_{\imath\jmath}F_{\imath\jmath}=2\sum_{\imath\in\{x,y,z\}} F_{tk}F_{tk}+\sum_{\imath l}F_{\imath l}F_{\imath l}=-2E^2+2B^2$, and $-\tfrac14$ of that is $\tfrac12(E^2-B^2)$, which is the standard $-\tfrac14F\cdot F$ evaluated on the same fields. The energy comes out positive in both writings; the corpus's own stress–energy article fixes the sign on that requirement.

The derivative. The corpus writes $\partial/\partial R_{\imath}$, and the time derivative of a material coordinate is $\partial/\partial r'_t=-i\,\partial/\partial R_t$. The two are never mixed in one display. A fermion bilinear's sign, which the rule does not fix because the bilinear carries the spin structure, is the subject of [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) and is quoted there rather than restated here.

## The Gauge Sector

The field strengths. Each factor of the product carries one,

$$
G_{a,\imath\jmath}=\frac{\partial G_{a,\jmath}}{\partial R_{\imath}}-\frac{\partial G_{a,\imath}}{\partial R_{\jmath}}+g_s\sum_{b,c}f_{abc}G_{b,\imath} G_{c,\jmath} ,
$$

$$
W_{a,\imath\jmath}=\frac{\partial W_{a,\jmath}}{\partial R_{\imath}}-\frac{\partial W_{a,\imath}}{\partial R_{\jmath}}+g\sum_{b,c}\varepsilon_{abc}W_{b,\imath} W_{c,\jmath} ,
\qquad
B_{\imath\jmath}=\frac{\partial B_{\jmath}}{\partial R_{\imath}}-\frac{\partial B_{\imath}}{\partial R_{\jmath}} .
$$

The colour structure constants are $f_{abc}$ and the weak ones are $\varepsilon_{abc}$ in the normalised basis. The two non-abelian curvatures carry the same commutator term in the same form; the abelian one does not, because its structure constants vanish.

The kinetic terms. Three, one per factor,

$$
\mathcal{L}_{\mathrm{gauge}}=-\tfrac14\sum_{a,\imath,\jmath}G_{a,\imath\jmath}G_{a,\imath\jmath}-\tfrac14\sum_{a,\imath,\jmath}W_{a,\imath\jmath}W_{a,\imath\jmath}-\tfrac14\sum_{\imath,\jmath}B_{\imath\jmath}B_{\imath\jmath} .
$$

The three coefficients are equal because each factor's gauge field is normalised so that its kinetic term has unit coefficient. That normalisation is what makes the three couplings independent numbers; a rescaling of any one field moves a constant between the kinetic term and the coupling, and the product $g_sF$ is what the physics sees.

**Three, not one.** The three kinetic terms do not mix. A term $G_{\imath\jmath}W_{\imath\jmath}$ would be forbidden by the product structure, since the two fields carry different quantum numbers and no invariant contraction exists. Mixing of the neutral fields happens at the level of the mass matrix and the currents, not at the level of the kinetic terms, and the mixing is a rotation of $W_{3,\imath}$ and $B_{\imath}$ that leaves the kinetic terms in the form above.

## The Fermion Sector

The term. One term per Weyl field, in the form

$$
\mathcal{L}_{\mathrm{ferm}}=\sum_{\psi}\bar{\tilde\Xi}_{\psi}\,i\,\tilde\nabla_{\mathrm{gco},\Phi}\,\tilde\Xi_{\psi} ,
$$

with $\bar{\tilde\Xi}=\tilde\Xi^{*}i\vec e_x$ the Dirac adjoint of the corpus, and $\tilde\nabla_{\mathrm{gco},\Phi}$ the gauge-covariant gradient, carrying the three connections in the representation of the field it acts on. The display states the structure; the component form of $\tilde\nabla_{\mathrm{gco},\Phi}$ and the sign of the bilinear are the Dirac article's, where the massless pair is $\tilde\nabla_\Phi\tilde\Xi_{R}=0$ and $(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_{L}=0$.

The covariant gradient. Its action on a field in the representation $(\mathbf{3}$ or $\mathbf{1},\mathbf{2}$ or $\mathbf{1},Y)$ is the one of *Operator and Calculus Conventions*, §*The Gradient*, and it reads

$$
\tilde\nabla_{\mathrm{gco},\Phi}\tilde\Xi_{\psi}=\tilde\nabla_\Phi\tilde\Xi_{\psi}+\frac{2\pi i\,ϙ}{h}\Bigl(\sum_a T_{a,\psi} G_{a}+\sum_a\tau_{a,\psi} W_{a}+Y_\psi B\Bigr)\tilde\Xi_{\psi} ,
$$

with $T_{a,\psi}$ the colour generators in the representation of $\psi$ and $\tau_{a,\psi}$ the weak ones. The bracket is the connection in that representation, and it is the same object for all fifteen fields of a generation, differing only in which generators act and with which hypercharge.

Why the term is one term and not fifteen. The fifteen Weyl fields of a generation carry fifteen different connections and fifteen different hypercharges, so the display above is fifteen terms in one line. That is the whole of the fermion sector: a kinetic term per field, and no mass term.

**No mass term.** The reason is recorded in article 1 and repeated here because it is the hinge of the assembly. A term $m\bar{\tilde\Xi}\tilde\Xi$ couples a left-handed field to a right-handed one, and the two carry different $SU(2)_L$ representations and different hypercharges, so no invariant contraction exists. The mass must wait for the scalar, and it arrives through the Yukawa sector.

## The Scalar Sector

The field and its potential. One complex doublet,

$$
\omicron_{\mathrm{hgs}}=\begin{pmatrix}\omicron_{\mathrm{hgs}}^+\ \omicron_{\mathrm{hgs}}^0\end{pmatrix},
\qquad
Y_{\mathrm{hch}}=\tfrac12 ,
$$

with the potential and the kinetic term

$$
\mathcal{L}_{H}=-\sum_{\imath}\left(D_{\imath}\omicron_{\mathrm{hgs}}\right)^{\dagger}\left(D_{\imath}\omicron_{\mathrm{hgs}}\right)+\mu^2\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}}-\varpi_{\mathrm{cpl}}\left(\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}}\right)^2 ,
\qquad
D_{\imath}\omicron_{\mathrm{hgs}}=\frac{\partial\omicron_{\mathrm{hgs}}}{\partial R_{\imath}}+i\frac{g}{2}\sum_a\tau_aW_{a,\imath}\omicron_{\mathrm{hgs}}+i\frac{g_{\mathrm Y}}{2}B_{\imath}\omicron_{\mathrm{hgs}} .
$$

The signs are the corpus's, by the rule of §*The Dictionary*: the kinetic term carries the minus, and the potential appears with $+\mu^2$ and $-\varpi_{\mathrm{cpl}}$ because $\mathcal{L}\supset -V$.

**The sign of $\mu^2$.** A positive $\mu^2$ gives a potential with a maximum at the origin and a circle of minima away from it. That sign is the whole content of spontaneous breaking: the field settles on the circle, and the theory is read around a point of it. A negative $\mu^2$ would give a single minimum at the origin and no breaking.

The minimum. The potential depends on $\omicron_{\mathrm{hgs}}$ only through $\omicron_{\mathrm{hgs}}^\dagger\omicron_{\mathrm{hgs}}$, so its minima form a three-sphere in the four real components. Writing $\omicron_{\mathrm{hgs}}^\dagger\omicron_{\mathrm{hgs}}=\tfrac12v^2$,

$$
v^2=\frac{\mu^2}{\varpi_{\mathrm{cpl}}} ,
\qquad
\langle\omicron_{\mathrm{hgs}}\rangle=\frac{1}{\sqrt2}\begin{pmatrix}0\ v\end{pmatrix},
\qquad
v=246.22\ \mathrm{GeV} .
$$

The value of $v$ is not computed here; it is the entry 18 of the parameter table of article 1, fixed by the Fermi constant.

What the sector supplies. Three things, and they are computed in [Electroweak Symmetry Breaking: the Doublet, the Potential and the Gauge-Boson Masses](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-gauge-boson-masses.html) rather than here: the masses $M_W=\tfrac12gv$ and $M_Z=\tfrac12\sqrt{g^2+g_{\mathrm Y}^2}\,v$, the massless photon, and the scalar mass $M_H=\sqrt{2\varpi_{\mathrm{cpl}}}\,v$. Recomputed from the table, $\varpi_{\mathrm{cpl}}=M_H^2/(2v^2)=0.1291$ for $M_H=125.09$ GeV, and the three masses then follow from $g$, $g_{\mathrm Y}$, $v$ and $\varpi_{\mathrm{cpl}}$.

Four real components, three eaten. The doublet carries four real fields. Three are the Goldstones that the $W^+$, $W^-$ and $Z$ absorb as longitudinal polarisations; the fourth is the physical scalar. The degree-of-freedom count closes: twenty-eight before breaking, twenty-eight after.

## The Yukawa Sector

The term. Three coupling matrices, one per fermion type,

$$
\mathcal{L}_{\mathrm{Yuk}}=-\sum_{a,b}\Bigl(\bar Q_{L,a}\omicron_{\mathrm{hgs}}\,Y_{d,ab}\,d_{R,b}+\bar Q_{L,a}\tilde\omicron_{\mathrm{hgs}}\,Y_{u,ab}\,u_{R,b}+\bar L_{L,a}\omicron_{\mathrm{hgs}}\,Y_{e,ab}\,e_{R,b}\Bigr)+\text{h.c.},
$$

with $a,b=1,2,3$ the generation labels and $Y_{u}$, $Y_{d}$, $Y_{e}$ general complex $3\times3$ matrices.

**The conjugate doublet.** The up-type term cannot use $\omicron_{\mathrm{hgs}}$, and this is the one place in the assembly where a second scalar object is needed. The conjugate doublet is

$$
\tilde\omicron_{\mathrm{hgs}}=\begin{pmatrix}\omicron_{\mathrm{hgs}}^{0*}\ -\omicron_{\mathrm{hgs}}^{+*}\end{pmatrix},
\qquad
Y_{\tilde\omicron_{\mathrm{hgs}}}=-\tfrac12 ,
$$

and it is not an independent field: it is the same doublet read through the conjugate. Its hypercharge is the negative of $\omicron_{\mathrm{hgs}}$'s, and that is what makes the up-type term invariant.

The hypercharge audit. Each term must carry total hypercharge zero, and each does:

| Term | $Y$ of the left factor | $Y$ of the scalar | $Y$ of the right factor | Sum |
|---|---|---|---|---|
| $\bar Q_L\omicron_{\mathrm{hgs}}\,d_R$ | $-1/6$ | $+1/2$ | $-1/3$ | $0$ |
| $\bar Q_L\tilde\omicron_{\mathrm{hgs}}\,u_R$ | $-1/6$ | $-1/2$ | $+2/3$ | $0$ |
| $\bar L_L\omicron_{\mathrm{hgs}}\,e_R$ | $+1/2$ | $+1/2$ | $-1$ | $0$ |

The masses after breaking. With $\langle\omicron_{\mathrm{hgs}}\rangle=(0,v/\sqrt2)$, each matrix becomes a mass matrix,

$$
M_f=\frac{v}{\sqrt2}\,Y_{f},
\qquad
f=u,d,e ,
$$

and the physical masses are the singular values of $M_f$, obtained by bi-unitary diagonalisation. That step, and the two unitary factors that survive it as the CKM and PMNS matrices, is the subject of [The Yukawa Sector: Fermion Mass Matrices and Their Diagonalisation](the-yukawa-sector-fermion-mass-matrices-and-their-diagonalisation.html).

Why the sector exists at all. Without it the fermions are massless, which the world is not. With it, the masses are free parameters, which is the price. There is no third option inside the renormalisable model: a mass term without the scalar is forbidden by the gauge symmetry, and a mass term generated in any other way requires new fields.

## The Assembled Expression

The sum. The four sectors add to

$$
\boxed{\;
\begin{aligned}
\mathcal{L}_{\mathrm{SM}}={}&-\tfrac14\sum_{a,\imath,\jmath}G_{a,\imath\jmath}G_{a,\imath\jmath}-\tfrac14\sum_{a,\imath,\jmath}W_{a,\imath\jmath}W_{a,\imath\jmath}-\tfrac14\sum_{\imath,\jmath}B_{\imath\jmath}B_{\imath\jmath}\\[2pt]
&+\sum_{\psi}\bar{\tilde\Xi}_{\psi}\,i\,\tilde\nabla_{\mathrm{gco},\Phi}\,\tilde\Xi_{\psi}\\[2pt]
&-\sum_{\imath}\left(D_{\imath}\omicron_{\mathrm{hgs}}\right)^{\dagger}\left(D_{\imath}\omicron_{\mathrm{hgs}}\right)+\mu^2\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}}-\varpi_{\mathrm{cpl}}\left(\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}}\right)^2\\[2pt]
&-\sum_{a,b}\Bigl(\bar Q_{L,a}\omicron_{\mathrm{hgs}}\,Y_{d,ab}\,d_{R,b}+\bar Q_{L,a}\tilde\omicron_{\mathrm{hgs}}\,Y_{u,ab}\,u_{R,b}+\bar L_{L,a}\omicron_{\mathrm{hgs}}\,Y_{e,ab}\,e_{R,b}\Bigr)+\text{h.c.}\\[2pt]
&+\frac{\theta_{\mathrm{QCD}}}{32\pi^2}\sum_{\imath,\jmath,a}G_{a,\imath\jmath}G_{a,\mathrm{dual},\imath\jmath} .
\end{aligned}
\;}
$$

The fifth line. The vacuum-angle term belongs to the strong sector and is separated for a reason: it is a total derivative, so it changes no equation of motion, and its effect is entirely quantum. It is written in the normalisation of [The Theta Parameter and Strong CP in Biquaternionic Form](the-theta-parameter-and-strong-cp-in-biquaternionic-form.html), with $G_{a,\mathrm{dual},\imath\jmath}=\tfrac12\sum_{\rho,\sigma}\epsilon_{\imath\jmath\rho\sigma}G_{a,\rho\sigma}$.

What the display is. It is a Lagrangian density of dimension four, and every term in it is either a kinetic term or a term of the same dimension. That is not an accident of the list; it is the definition of renormalisability, and the next section counts what the condition permits.

**The two structural facts visible in the sum.** First, every term carrying a derivative carries a connection, and no term carries a connection without a derivative; that is the statement that the connections enter only through covariant derivatives and field strengths. Second, the only term that is not a modulus squared or a product of two field strengths is the $\theta$ term, and it is a total derivative. Those two facts are what make the audit of the next section short.

## The Gauge-Invariance Audit

What is checked. Each term of the sum is checked separately, under the three local transformations

$$
\psi\mapsto e^{iY_\psi\alpha(x)}\,U_c(x)\,U_L(x)\,\psi ,
\qquad
G_{\imath}\mapsto U_cG_{\imath} U_c^{\dagger}+\frac{i}{g_s}U_c\frac{\partial U_c^{\dagger}}{\partial R_{\imath}} ,
$$

and the analogous laws for $W_{\imath}$ with $U_L$ and for $B_{\imath}$ with the phase alone. $U_L$ acts as the identity on right-handed fields.

| Term | How it transforms | Why it is invariant |
|---|---|---|
| $-\tfrac14G_{a,\imath\jmath}G_{a,\imath\jmath}$ | $G_{\imath\jmath}\mapsto U_cG_{\imath\jmath}U_c^{\dagger}$ | the trace of a product is cyclic, and $U_c^{\dagger}U_c=1$ |
| $-\tfrac14W_{a,\imath\jmath}W_{a,\imath\jmath}$ | $W_{\imath\jmath}\mapsto U_LW_{\imath\jmath}U_L^{\dagger}$ | the same |
| $-\tfrac14B_{\imath\jmath}B_{\imath\jmath}$ | $B_{\imath\jmath}\mapsto B_{\imath\jmath}$ | the abelian curvature is a derivative of a scalar phase |
| fermion kinetic | $\bar{\tilde\Xi}\mapsto\bar{\tilde\Xi}U^{\dagger}$, $\tilde\nabla_\Phi\tilde\Xi\mapsto U\tilde\nabla_\Phi\tilde\Xi$ | $U^{\dagger}U=1$, and the derivative is covariant |
| scalar kinetic | $D_{\imath}\omicron_{\mathrm{hgs}}\mapsto U_{\omicron_{\mathrm{hgs}}} D_{\imath}\omicron_{\mathrm{hgs}}$ | the same, with the scalar's representation |
| potential $\mu^2\omicron_{\mathrm{hgs}}^\dagger\omicron_{\mathrm{hgs}}-\varpi_{\mathrm{cpl}}(\omicron_{\mathrm{hgs}}^\dagger\omicron_{\mathrm{hgs}})^2$ | $\omicron_{\mathrm{hgs}}^\dagger\omicron_{\mathrm{hgs}}\mapsto\omicron_{\mathrm{hgs}}^\dagger\omicron_{\mathrm{hgs}}$ | the invariant is the modulus squared, a singlet |
| Yukawa, down type | the three factors transform by $U_Q^{\dagger}$, $U_{\omicron_{\mathrm{hgs}}}$, $U_d$ | the product is $U_Q^{\dagger}U_{\omicron_{\mathrm{hgs}}} U_d$, and the $SU(2)$ contraction is the singlet |
| Yukawa, up type | the same with $U_{\tilde\omicron_{\mathrm{hgs}}}$ | $U_{\tilde\omicron_{\mathrm{hgs}}}$ is the conjugate of $U_{\omicron_{\mathrm{hgs}}}$, and the phase is opposite |
| $\theta$ term | invariant | $G_{\imath\jmath}$ is adjoint-valued, and the epsilon contraction is a colour singlet |

The three places where the audit could fail and does not.

- The fermion kinetic term needs all three connections. If the covariant derivative carried only the hypercharge connection, the term would fail under $SU(2)_L$ and $SU(3)_c$. The invariance of this term is what forces the gauge fields to be the same objects that appear in the three kinetic terms, and that is the content of calling the theory a gauge theory rather than three separate ones.
- The up-type Yukawa needs the conjugate doublet. With $\omicron_{\mathrm{hgs}}$ in place of $\tilde\omicron_{\mathrm{hgs}}$, the total hypercharge would be $-1/6+1/2+2/3=+1$, and the term would not be invariant. The conjugate is forced.
- The potential needs the modulus squared and nothing else. A term $\omicron_{\mathrm{hgs}}^T\omicron_{\mathrm{hgs}}$ or $\omicron_{\mathrm{hgs}}^\dagger\tau_a\omicron_{\mathrm{hgs}}$ would fail; only $\omicron_{\mathrm{hgs}}^\dagger\omicron_{\mathrm{hgs}}$ is a singlet. That is why the potential has two parameters and not more.

**The one term that is not invariant, and must not be there.** A bare mass $m\bar{\tilde\Xi}\tilde\Xi$ fails the audit: the left factor transforms as a doublet and the right as a singlet, so the product carries an $SU(2)_L$ index that nothing contracts. A bare mass for the neutrino fails for the same reason. Their absence is a result of the audit and not an omission from it.

The audit is complete. Every term of the sum has been checked, and no term of dimension four compatible with the symmetries has been left out. The last claim is the one that needs the count of the next section, and the count is of operators and not of terms: the renormalisable operators are the ones built from at most four fields and at most one derivative each, and the list above exhausts them once the field content of article 1 is fixed.

## Sixty Parameters Written, Nineteen Physical

Why the count matters. The Lagrangian above is written with more numbers than the model has. Every field can be redefined, and a redefinition changes the coupling matrices without changing any observable. The count of what survives is the count of article 1, and the difference is the redundancy.

What is written. Counting real numbers,

| Object | Real parameters |
|---|---|
| $g_s$, $g$, $g_{\mathrm Y}$ | $3$ |
| $\mu^2$, $\varpi_{\mathrm{cpl}}$ | $2$ |
| $\theta_{\mathrm{QCD}}$ | $1$ |
| $Y_{u}$, $Y_{d}$ | $2\times18=36$ |
| $Y_{e}$ | $18$ |
| **total written** | $\mathbf{60}$ |

Each $3\times3$ complex matrix carries nine complex entries, that is eighteen real numbers, and nothing constrains them.

What removes them. A field redefinition is a change of basis in flavour space, and the group that acts is a product of unitary groups, one factor per multiplet type, minus the factors that are symmetries of the whole theory.

| Sector | Written | Group acting | Stabiliser | Physical |
|---|---|---|---|---|
| quarks | $36$ | $U(3)_Q\times U(3)_u\times U(3)_d$, dimension $27$ | $U(1)_B$, dimension $1$ | $36-27+1=10$ |
| leptons | $18$ | $U(3)_L\times U(3)_e$, dimension $18$ | $U(1)^3$, dimension $3$ | $18-18+3=3$ |

The rule of the count. The physical number is the written number less the dimension of the group that acts, plus the dimension of the subgroup that leaves the couplings in their diagonal form. The last term is not a fudge: after diagonalisation a residual abelian group remains, and it acts on nothing.

The quark result. Ten is six masses plus three angles plus one phase. Rephasing absorbs the five relative phases of three quark fields, $2N-1=5$ for $N=3$, and the ten that remain are the entries of article 1.

The lepton result. Three is three masses and no mixing, because the minimal model has no right-handed neutrino and the lepton mixing matrix is then unobservable: it can be rotated away into the charged-lepton fields.

**The total.** The two flavour blocks give thirteen, and with the six of the gauge, scalar and vacuum sectors the count is nineteen, which is the table of article 1. The reduction is $60\to19$, and the forty-one removed numbers are not small corrections: they are the entire freedom of choice of flavour basis.

What the count does not do. It does not say that the nineteen are independent in nature; it says that the Lagrangian has nineteen degrees of freedom once the field basis is fixed. Relations among the nineteen — a mass ratio, a mixing angle predicted from masses — would be physics beyond the count, and the model supplies none.

A second redundancy, inside the mass sector. The pair $(\mu^2,\varpi_{\mathrm{cpl}})$ and the pair $(v,M_H)$ carry the same information, through $v^2=\mu^2/\varpi_{\mathrm{cpl}}$ and $M_H^2=2\varpi_{\mathrm{cpl}} v^2=2\mu^2$. Likewise $(g,g_{\mathrm Y})$ and $(e,\theta_W)$ through $e=g\sin\theta_W=g_{\mathrm Y}\cos\theta_W$. The count is of information and not of symbols, and a change of variables moves numbers between columns without changing the total.

## What the Expression Omits

**Three omissions, and each is a measurement.** The expression above is the renormalisable Standard Model with massless neutrinos and no dark sector. Each omission has an experimental warrant and a price.

- Neutrino masses. The dimension-five operator $\frac{c_{ab}}{\Lambda}\left(L_{L,a}^T\,i\tau_2\,\omicron_{\mathrm{hgs}}\right)\left(L_{L,b}^T\,i\tau_2\,\omicron_{\mathrm{hgs}}\right)$ is invariant under all three factors and gives a Majorana mass after breaking. The two insertions are $\omicron_{\mathrm{hgs}}$ and not $\tilde\omicron_{\mathrm{hgs}}$, because the hypercharge has to close: $-\tfrac12-\tfrac12+\tfrac12+\tfrac12=0$, whereas two conjugate doublets of hypercharge $-\tfrac12$ would give $-2$. The $i\tau_2$ contracts the two weak doublets into a singlet, and the transpose pairs the two left-handed spinors into a Lorentz scalar, so the operator is a singlet under every factor. It is the unique dimension-five operator the field content allows, and it is absent because it is not renormalisable. Adding it, or adding right-handed neutrinos, costs the seven or eight parameters that article 1 counts.
- Gravity. No term of the sum couples to the metric. The framework's own gravitational sector is a separate construction, and the Standard Model is written on a fixed background.
- Dark matter and the matter excess. No field in the content is a dark-matter candidate, and the $\theta$ term's $B+L$ violation is the only source of baryon-number violation in the expression. Both gaps are the subject of [What the Standard Model Does Not Explain: Dark Matter, Baryogenesis and the Sphaleron](what-the-standard-model-does-not-explain-dark-matter-baryogenesis-and-the-sphaleron.html).

What is not omitted, and is often said to be. The $\theta$ term is in the expression, and it is a parameter. Its smallness is a problem, not an omission.

The status of the omissions. They are not defects of the assembly. The assembly is complete as the renormalisable theory of the given field content, and the omissions are the statement that the given content is not the whole of nature.

## The Corpus's Own Action Beside the Standard One

Three sectors out of four. The corpus writes a gauge action, a scalar action and a fermion action, and the first two are the standard ones term for term.

| Standard object | Corpus object | Identity |
|---|---|---|
| $-\tfrac14F\cdot F$ | $-\tfrac14\sum_{\imath,\jmath}\varepsilon_{\imath}\varepsilon_{\jmath} F_{\imath\jmath}F_{\imath\jmath}$ | the same, by §*The Dictionary* |
| $+\tfrac12\partial\xi\cdot\partial\xi$ | $-\tfrac12\sum_{\imath}\partial_{\imath}\xi\,\partial_{\imath}\xi$ | the same, by §*The Dictionary* |
| $\lvert D_{\imath}\omicron_{\mathrm{hgs}}\rvert^2$ | $-\sum_{\imath}(D_{\imath}\omicron_{\mathrm{hgs}})^\dagger(D_{\imath}\omicron_{\mathrm{hgs}})$ | the same |
| the Dirac kinetic term, $\bar\psi\,iD_{\imath}\psi$ | $\bar{\tilde\Xi}\,i\tilde\nabla_\Phi\tilde\Xi$ | the Dirac article's pair; a central shift, if wanted, is added as $\kappa$ and never carried in the glyph |
| $\omicron_{\mathrm{hgs}}^\dagger\omicron_{\mathrm{hgs}}$ | $\tilde\Xi\tilde\Xi^{\natural}$ | the norm of an element |

The dictionary is a dictionary and not a theory. Each row is an identity between two writings of one object, and none of them is a derivation. The corpus's contribution is that the objects have homes: the connection is a material-sector element, the curvature is its vector part under $\natural$, the scalar is an element and its modulus squared is the norm.

**The sector with no corpus counterpart.** The colour sector is the exception. The algebra's ceiling is $SU(2)$, reached as the norm-one part of the material sector, and no element of $\mathbb{B}$ carries three colours. The QCD Lagrangian is therefore written in this article in a notation the algebra supplies for the spacetime indices only; the colour indices are external to it. That is stated in [Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)](why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html) and in [The Gluon: An Octet Inside the Carrier's Group](the-gluon-an-octet-outside-the-biquaternion-algebra.html), and it is the one structural asymmetry of the assembly.

The parameter ledger, stated once. Three of the four sectors are writable in the corpus's language and none of the nineteen parameters is fixed by it. The assembly therefore measures the boundary as sharply as the parameter table does: the algebra supplies the arena in which three of these four expressions are written, and it supplies no coefficient.

## Summary

The Standard Model Lagrangian is the sum of four sectors plus the vacuum-angle term: the three gauge kinetic terms $-\tfrac14\sum G G$, $-\tfrac14\sum W W$, $-\tfrac14\sum BB$; one fermion kinetic term per Weyl field, fifteen per generation, each built on the covariant gradient carrying the connection in that field's representation; the scalar kinetic term and the potential $-\sum_{\imath}(D_{\imath}\omicron_{\mathrm{hgs}})^\dagger(D_{\imath}\omicron_{\mathrm{hgs}})+\mu^2\omicron_{\mathrm{hgs}}^\dagger\omicron_{\mathrm{hgs}}-\varpi_{\mathrm{cpl}}(\omicron_{\mathrm{hgs}}^\dagger\omicron_{\mathrm{hgs}})^2$; and the three Yukawa matrices with the conjugate doublet $\tilde\omicron_{\mathrm{hgs}}$ of hypercharge $-\tfrac12$ in the up-type term. The assembly is one notation and one sign rule.

The sign rule is $\sum_{\imath} X_{\imath} Y_{\imath}=-X\cdot Y$, proved in one line from $X_t=iX_0$ and the metric of the interval. It converts the corpus's $-\tfrac12\sum\partial\xi\partial\xi$ into the standard $+\tfrac12\partial\xi\cdot\partial\xi$, converts its $-\tfrac14\sum FF$ into the standard $-\tfrac14F\cdot F$ with no change of sign, and leaves the two writings one Lagrangian: the abelian check gives $\sum_{\imath\jmath}F_{\imath\jmath}F_{\imath\jmath}=2(B^2-E^2)$ and hence $\tfrac12(E^2-B^2)$ on both sides.

The audit is term by term and it passes. The three kinetic terms are invariant because each curvature transforms in the adjoint; the fermion and scalar kinetic terms because each covariant derivative transforms with the same unitary that acts on its field; the potential because it depends only on the singlet $\omicron_{\mathrm{hgs}}^\dagger\omicron_{\mathrm{hgs}}$; the Yukawa terms because the total hypercharge vanishes in each of the three, $-1/6+1/2-1/3$, $-1/6-1/2+2/3$ and $+1/2+1/2-1$; and the vacuum-angle term because it is a colour singlet. A bare fermion mass fails the audit, and its absence is a result and not an omission.

Written out, the four sectors and the vacuum-angle term carry sixty real parameters: three couplings, two scalar parameters, one vacuum angle, eighteen for $Y_{e}$ and thirty-six for the pair $Y^u,Y_{d}$. Field redefinitions remove forty-one of them — twenty-six in the quark sector through $U(3)_Q\times U(3)_u\times U(3)_d$ leaving ten, which is six masses and four mixing parameters, and fifteen in the lepton sector through $U(3)_L\times U(3)_e$ leaving three masses — so nineteen survive, which is the table of article 1. The redundancy is a freedom of flavour basis and not a small correction.

The expression omits neutrino masses, gravity and a dark sector, and each omission is a measurement rather than an oversight. The unique dimension-five operator the content allows is the neutrino mass, and it is absent only because the theory is written renormalisable. Three of the four sectors have corpus counterparts term for term, through the dictionary of this article; the colour sector has none, because the algebra's ceiling is $SU(2)$. The assembly therefore closes the ledger the parameter table opened: the arena is the algebra's, and all sixty coefficients written here are imported.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{L}_{\mathrm{QCD}}$, $\mathcal{L}_{\mathrm{EW}}$, $\mathcal{L}_{H}$, $\mathcal{L}_{\mathrm{Yuk}}$ | The four sectors |
| $G_{a,\imath}$, $W_{a,\imath}$, $B_{\imath}$ | Colour, weak and hypercharge gauge fields |
| $G_{a,\imath\jmath}$, $W_{a,\imath\jmath}$, $B_{\imath\jmath}$ | Their field strengths |
| $f_{abc}$, $\varepsilon_{abc}$ | Colour and weak structure constants |
| $\tilde\nabla_{\mathrm{gco},\Phi}$ | The gauge-covariant gradient; the representation is that of the field it acts on |
| $\bar{\tilde\Xi}=\tilde\Xi^{*}i\vec e_x$ | The Dirac adjoint |
| $\omicron_{\mathrm{hgs}}$, $\tilde\omicron_{\mathrm{hgs}}$ | The scalar doublet of hypercharge $\tfrac12$ and its conjugate of hypercharge $-\tfrac12$ |
| $Y_{u}$, $Y_{d}$, $Y_{e}$ | The three Yukawa matrices, general complex $3\times3$ |
| $M_f=vY_{f}/\sqrt2$ | The mass matrix of the fermion type $f$ |
| $\mu^2$, $\varpi_{\mathrm{cpl}}$ | The two parameters of the potential |
| $v^2=\mu^2/\varpi_{\mathrm{cpl}}$ | The vacuum expectation value, $246.22$ GeV |
| $M_H=\sqrt{2\varpi_{\mathrm{cpl}}}\,v$ | The scalar mass |
| $\theta_{\mathrm{QCD}}$ | The vacuum angle |
| $G_{a,\mathrm{dual},\imath\jmath}=\tfrac12\sum_{\rho,\sigma}\epsilon_{\imath\jmath\rho\sigma}G_{a,\rho\sigma}$ | The dual field strength |
| $\sum_{\imath} X_{\imath} Y_{\imath}=-X\cdot Y$ | The sign rule of §*The Dictionary* |
| $\partial/\partial R_{\imath}$ | The corpus derivative, with $\partial/\partial r'_t=-i\partial/\partial R_t$ |

## Further Reading

- [The Standard Model: Content, Quantum Numbers and the Nineteen Parameters](the-standard-model-content-quantum-numbers-and-the-nineteen-parameters.html). The field content this expression is written for, and the nineteen that survive the count.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html). The connection, the covariant derivative and the curvature, from which the three kinetic terms are read.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html). The fermion pair and the covariant gradient, whose component form this article quotes and does not restate.
- [The Higgs Mechanism in Biquaternionic Form](the-higgs-mechanism-in-biquaternionic-form.html). The abelian case, which the scalar sector of this article generalises to the doublet.
- [Stress–Energy Conservation Laws and the Field Action in Biquaternionic Form](stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.html). The scalar action and the sign convention that fixes the dictionary.
- [The Theta Parameter and Strong CP in Biquaternionic Form](the-theta-parameter-and-strong-cp-in-biquaternionic-form.html). The normalisation of the fifth line and its status as a total derivative.
- [Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)](why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html). The one sector with no corpus counterpart.
- [The Gluon: An Octet Inside the Carrier's Group](the-gluon-an-octet-outside-the-biquaternion-algebra.html). The colour sector at the level of the field.
- [The Standard Model as the Low-Energy Phase: The U(2) Ceiling and the Four Unbuilt Sectors](the-standard-model-as-the-low-energy-phase.html). Which terms the framework reaches and which it imports.

The three companions this article names but does not carry — the QCD Lagrangian, gauge fixing and the electroweak precision observables — are written, as articles 9, 7 and 8 of the series, and each is linked above at the point where it is invoked.
