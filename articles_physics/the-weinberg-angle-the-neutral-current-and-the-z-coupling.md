# __The Weinberg Angle, the Neutral Current and the $Z$ Coupling__

## Introduction

**The claim.** The angle $\theta_W$ is not a third coupling. It is the one angle by which the two neutral gauge fields must be rotated to make the photon couple as pure electric charge, and once it is so defined the $Z$ coupling follows with no further freedom:

$$
\mathcal{L}_Z=\frac{g}{\cos\theta_W}Z_\mu\sum_f\bar f\gamma^\mu\Big[\big(T_{3f}-Q_f\sin^2\theta_W\big)P_L-Q_f\sin^2\theta_W\,P_R\Big]f .
$$

The appearance of $\sin^2\theta_W$ in that bracket is therefore not a second convention. It is the residue of the rotation, and §*The Rotation, and Why the Angle Appears Squared* proves it in three lines.

**The standing.** Standard theory, transcribed. The framework supplies two free couplings and no embedding, so neither the angle nor the electric-charge relation follows, and the corpus's own agenda classifies the row *no route yet*. This article does not soften that; it states what would settle it.

**Three results that the companion articles do not state.**

- **The angle is defined by one condition, and it explains the square.** Demanding that the photon coupling contain no $T_3$ fixes $\tan\theta_W=g_{\mathrm Y}/g$; the $Z$ coupling then comes out as $T_3-\sin^2\theta_WQ$ automatically, with the square arising because $\sin^2\theta_W=g_{\mathrm Y}^2/(g^2+g_{\mathrm Y}^2)$ is the hypercharge share of the two couplings' strength.
- **The neutrino's $Z$ coupling is free of the angle.** Its vector and axial couplings are both $\tfrac12$, whatever the mixing, so the invisible width counts neutrinos without knowing $\sin^2\theta_W$. That is why the three-neutrino result is the sharpest fact of the $Z$ pole.
- **The three angles, and their ratios.** The on-shell value is $0.22305$, the $\overline{\mathrm{MS}}$ value $0.23122$ and the effective leptonic value $0.23148$; the ratios are $\kappa_{\mathrm{OS}}=0.9647$ and $\kappa_{\mathrm{eff}}=1.0011$, and the first is dominated by the hadronic vacuum polarisation.

**The order.** The two neutral currents before mixing; the rotation and the two conditions; the couplings of every fermion, tabulated; the low-energy neutral current and its two historic measurements; the three angles and why they differ; the $Z$ pole, its widths and its asymmetries; what the neutral current measures that the charged current cannot; and the framework's position.

## The Two Neutral Currents

**Before mixing there are two.** The electroweak sector carries four gauge fields, and two of them are neutral: $W^3_\mu$ of $SU(2)_L$ and $B_\mu$ of $\mathrm{U}(1)_Y$. Their couplings to matter are fixed by the quantum numbers of article 1 and by nothing else,

$$
\mathcal{L}_{\mathrm{neutral}}=g\,W^3_\mu J^3_\mu+g_{\mathrm Y}B_\mu J^Y_\mu ,
\qquad
J^3_\mu=\sum_f T_{3f}\,\bar f\gamma_\mu f ,
\qquad
J^Y_\mu=\sum_f Y_f\,\bar f\gamma_\mu f ,
$$

with $T_{3f}$ the weak isospin of the left part and $Y_f$ the hypercharge. Both currents are diagonal in the mass basis, because both generators commute with the unbroken charge; that is why the neutral sector needs no mixing matrix and the charged sector does.

**Two currents, one measured combination.** Neither $J^3$ nor $J^Y$ is separately observable: a $W^3$ or a $B$ boson does not propagate as a mass eigenstate, since the mass matrix of article 4 mixes them. What is observable is the coupling of the fields that do propagate, and there are two of them: the massless one and the massive one.

**The counting already fixes part of the answer.** Two neutral fields, two mass eigenstates, one of them massless. The massless one couples to a conserved current with no axial part, because a massless vector has two polarisations and a non-conserved current would require the third. So the massless combination must be the one whose axial coupling cancels, and that is a condition on the rotation angle. The next section turns it into an equation.

**The two invariants of the rotation.** A rotation of the pair $(W^3,B)$ has one angle, and the two physical couplings are the two combinations the rotation produces: one must be pure vector and pure $Q$, the other carries what is left. Two states, one angle, and therefore no freedom beyond the angle itself.

## The Rotation, and Why the Angle Appears Squared

**The rotation.** Write the physical fields as

$$
A_\mu=\sin\theta_W\,W^3_\mu+\cos\theta_W\,B_\mu ,
\qquad
Z_\mu=\cos\theta_W\,W^3_\mu-\sin\theta_W\,B_\mu ,
$$

with the inverse

$$
W^3_\mu=\sin\theta_W\,A_\mu+\cos\theta_W\,Z_\mu ,
\qquad
B_\mu=\cos\theta_W\,A_\mu-\sin\theta_W\,Z_\mu .
$$

The angle is so far a free parameter of the notation; the two conditions below fix it and then fix the $Z$ coupling.

**Substituting, in one step.** Using $Y_f=Q_f-T_{3f}$, the neutral Lagrangian becomes

$$
\mathcal{L}_{\mathrm{neutral}}=A_\mu\Big[\big(g\sin\theta_W-g_{\mathrm Y}\cos\theta_W\big)J^3_\mu+g_{\mathrm Y}\cos\theta_W\,J^{Q}_\mu\Big]
+Z_\mu\Big[\big(g\cos\theta_W+g_{\mathrm Y}\sin\theta_W\big)J^3_\mu-g_{\mathrm Y}\sin\theta_W\,J^{Q}_\mu\Big] ,
$$

with $J^Q_\mu=\sum_fQ_f\bar f\gamma_\mu f$ the electromagnetic current. Two brackets, and the whole article is in them.

**The first condition.** The photon must couple as $eQ$ with no $T_3$ admixture, because the electromagnetic current is the only conserved current with no axial part and the photon is massless. Setting the $J^3$ coefficient to zero,

$$
g\sin\theta_W=g_{\mathrm Y}\cos\theta_W
\qquad\Longrightarrow\qquad
\tan\theta_W=\frac{g_{\mathrm Y}}{g} .
$$

That is the definition of the angle: **it is the rotation that makes the photon pure charge.** Nothing else defines it.

**The second condition is not a condition.** Given the first, the photon coupling is

$$
g_{\mathrm Y}\cos\theta_W=\frac{g\,g_{\mathrm Y}}{\sqrt{g^2+g_{\mathrm Y}^2}}=g\sin\theta_W\equiv e ,
$$

which is the electric charge expressed through either coupling, and the $Z$ bracket becomes

$$
Z_\mu\sqrt{g^2+g_{\mathrm Y}^2}\left[J^3_\mu-\frac{g_{\mathrm Y}\sin\theta_W}{\sqrt{g^2+g_{\mathrm Y}^2}}J^Q_\mu\right]
=Z_\mu\sqrt{g^2+g_{\mathrm Y}^2}\left[J^3_\mu-\sin^2\theta_W\,J^Q_\mu\right] .
$$

**The square, and where it comes from.** The coefficient of $J^Q$ in the $Z$ coupling is

$$
\frac{g_{\mathrm Y}\sin\theta_W}{\sqrt{g^2+g_{\mathrm Y}^2}}
=\frac{g_{\mathrm Y}^2}{g^2+g_{\mathrm Y}^2}=\sin^2\theta_W ,
$$

using $\sin\theta_W=g_{\mathrm Y}/\sqrt{g^2+g_{\mathrm Y}^2}$. Two powers of $g_{\mathrm Y}$ appear in the numerator and one in each term of the denominator, and that is the whole reason the neutral current carries $\sin^2\theta_W$ and not $\sin\theta_W$. The square is a bookkeeping fact about which coupling sits in which slot; it is not a second mixing.

**Four symbols, two numbers.** The neutral sector is written with $g$, $g_{\mathrm Y}$, $\cos\theta_W$ and $\sin\theta_W$. Two relations act on them, $\sin^2\theta_W+\cos^2\theta_W=1$ and $\tan\theta_W=g_{\mathrm Y}/g$, so the four symbols carry two independent numbers. Two, and not three: the angle is not a third parameter, it is the ratio of the two that exist. The model's count has three gauge couplings in total, of which these two are the neutral ones, and the rotation neither adds to that count nor takes from it.

**The overall $Z$ coupling.** With $\sqrt{g^2+g_{\mathrm Y}^2}=g/\cos\theta_W=e/(\sin\theta_W\cos\theta_W)$, the Lagrangian reads

$$
\mathcal{L}_Z=\frac{g}{\cos\theta_W}Z_\mu\left(J^3_\mu-\sin^2\theta_WJ^Q_\mu\right)
=\frac{e}{\sin\theta_W\cos\theta_W}Z_\mu\left(J^3_\mu-\sin^2\theta_WJ^Q_\mu\right),
$$

which is the standard form, and the combination $e/(\sin\theta_W\cos\theta_W)$ is the one measured by the $Z$ couplings to fermions.

**The chiral decomposition.** Because $T_3$ acts only on left-handed fields and $Q$ acts on both, the bracket separates by chirality:

$$
J^3_\mu-\sin^2\theta_WJ^Q_\mu=\sum_f\bar f\gamma_\mu\Big[\big(T_{3f}-Q_f\sin^2\theta_W\big)P_L-Q_f\sin^2\theta_WP_R\Big]f ,
\qquad
P_{L,R}=\tfrac12\left(1\mp\gamma^5\right).
$$

The two coefficients are the left and right couplings, and their sum and difference are the vector and axial couplings:

$$
g_{Lf}=T_{3f}-Q_f\sin^2\theta_W ,
\qquad
g_{Rf}=-Q_f\sin^2\theta_W ,
\qquad
g_{Vf}=T_{3f}-2Q_f\sin^2\theta_W ,
\qquad
g_{Af}=T_{3f} .
$$

**The axial coupling is the isospin, exactly.** The axial coupling is $T_3$ with no correction, because $\sin^2\theta_W$ multiplies $Q$ in both chiralities and cancels in the difference. That single fact is the reason the $Z$ pole measures isospin so cleanly, and it is why the neutrino's coupling is angle-free.

**The two normalisations used in the literature, and the one used here.** The Lagrangian above is written with the overall factor $g/\cos\theta_W$ and the bracket $g_LP_L+g_RP_R$. An equivalent form puts the factor $\tfrac{g}{2\cos\theta_W}$ outside and the bracket $\tfrac12(g_V-g_A\gamma^5)$; the two differ by a factor two distributed between the overall constant and the couplings. This article uses $g_L$, $g_R$, $g_V=T_3-2Q\sin^2\theta_W$ and $g_A=T_3$, which is the convention in which the partial width is

$$
\Gamma\left(Z\to f\bar f\right)=\frac{G_FM_Z^3}{6\sqrt2\,\pi}\left(g_{Vf}^2+g_{Af}^2\right)N_c\,\left(1+\frac{\alpha_s}{\pi}+\cdots\right) ,
$$

with $N_c=3$ for quarks and the QCD bracket absent for leptons. A reader who takes $g_V$ and $g_A$ from a source with the other normalisation will find every width off by a factor four.

## The Couplings of Every Fermion

**The table.** At $\sin^2\theta_W=0.23122$, with $T_3$ the isospin of the left part:

| Fermion | $T_3$ | $Q$ | $g_L$ | $g_R$ | $g_V$ | $g_A$ | $A_f$ |
|---|---|---|---|---|---|---|---|
| $\nu_e,\nu_\mu,\nu_\tau$ | $+1/2$ | $0$ | $0.5000$ | $0$ | $0.5000$ | $0.5000$ | $1.0000$ |
| $e,\mu,\tau$ | $-1/2$ | $-1$ | $-0.2688$ | $0.2312$ | $-0.0376$ | $-0.5000$ | $0.1494$ |
| $u,c,t$ | $+1/2$ | $+2/3$ | $0.3459$ | $-0.1541$ | $0.1917$ | $0.5000$ | $0.6686$ |
| $d,s,b$ | $-1/2$ | $-1/3$ | $-0.4229$ | $0.0771$ | $-0.3459$ | $-0.5000$ | $0.9357$ |

**Four rows cover twelve fermions.** The couplings depend on $T_3$ and $Q$ only, and those are the same within each row, so the fifteen fields of article 1 collapse to four patterns. The mass does not enter: the $Z$ couples to all three generations identically in the gauge sector, and the differences between generations appear only through the fermion masses in the loop corrections and through the mixing in the charged current.

**The right-handed neutrino.** It is absent from the table because it is a singlet of all three groups and couples to nothing. A reader who adds it for neutrino masses finds that it does not change one line of this section.

**The electron's near-cancellation, and why it matters.** The electron's vector coupling is $-0.0376$, seven per cent of its axial coupling, and the smallness is not an accident: it is small because $\sin^2\theta_W$ happens to be near $\tfrac14$. The value $\sin^2\theta_W=\tfrac14$ gives $g_V=0$ exactly for a charge-one left-handed doublet member, and the measured value sits $0.019$ away. That near-cancellation is what makes the electron's $A_f$, and therefore the leptonic asymmetries, small and hard to measure, and it is why the hadronic asymmetries are the sharp ones.

**The $A_f$ column.** The asymmetry parameter is

$$
A_f=\frac{2\,g_{Vf}\,g_{Af}}{g_{Vf}^2+g_{Af}^2} ,
$$

which is the fractional left-right polarisation of the $Z$ coupling to that fermion: $+1$ for a purely left-handed coupling and $-1$ for a purely right-handed one. The neutrino is $+1$ exactly, which is the statement that the $Z$ couples to the neutrino only through its left part.

**A check on the arithmetic.** Each row satisfies $g_V=g_L+g_R$ and $g_A=g_L-g_R$. For the electron, $-0.2688+0.2312=-0.0376$ and $-0.2688-0.2312=-0.5000$. The check is trivial and it catches the commonest error in the table, which is a sign on $g_R$.

**What the table does not contain.** No mixing angle between generations, no phase, no fermion mass. The neutral current is flavour-diagonal and universal, and the Glashow–Iliopoulos–Maiani mechanism extends that to the one-loop level: the box amplitude sums $V_{id}V^{*}_{is}$ against the internal masses, the sum over $V$ vanishes by unitarity, and what survives is the mass difference. [Meson Mixing, Rare Decays and the Unitarity Triangle as a Closure Test](meson-mixing-rare-decays-and-the-unitarity-triangle-as-a-closure-test.html) carries the one-loop argument in full; nothing in it changes the tree table above.

## The Low-Energy Neutral Current

**Below the $Z$ mass, the current is a contact interaction.** At momenta small compared with $M_Z$ the $Z$ propagator contracts to $1/M_Z^2$, and the neutral current Lagrangian becomes a four-fermion interaction of strength

$$
\frac{g^2}{2M_Z^2\cos^2\theta_W}=\frac{4G_F}{\sqrt2}=2\sqrt2\,G_F ,
$$

using $G_F/\sqrt2=g^2/(8M_W^2)$ and $M_W=M_Z\cos\theta_W$. The coefficient $4G_F/\sqrt2$ is the one the charged-current Fermi Lagrangian carries, so the two currents enter a low-energy calculation with equal strength; what differs is the shape, vector–axial here and purely left-handed there. That equality is what made the 1973 experiments interpretable: a neutral current weaker than the charged one by an unknown factor would have needed a second parameter, and it did not.

**The effective Lagrangian.** With the table's couplings,

$$
\mathcal{L}_{\mathrm{NC}}^{\mathrm{eff}}=-\frac{4G_F}{\sqrt2}\sum_{f,f'}J^{Z}_{\mu,f}J^{Z}_{\mu,f'} ,
\qquad
J^Z_{\mu,f}=\bar f\gamma_\mu\left(g_{Vf}+g_{Af}\gamma^5\right)f ,
$$

and every low-energy neutral-current experiment is a measurement of a product of these couplings.

**Neutrino–electron scattering.** The two processes $\nu_ee\to\nu_ee$ and $\bar\nu_ee\to\bar\nu_ee$ have cross sections whose ratio determines a combination of the electron's couplings. With $g_V=-\tfrac12+2\sin^2\theta_W$ and $g_A=-\tfrac12$ for the electron, the measured values are consistent with the table and bound $\sin^2\theta_W$ to a few per cent. The channel is clean and the statistics are poor, which is why it is a confirmation and not a precision measurement.

**Neutrino–nucleon scattering and the Paschos–Wolfenstein relation.** The classic measurement used deep inelastic scattering on an isoscalar target, and its strength is that it compares a difference of differences rather than a ratio of ratios. Define

$$
R^-=\frac{\sigma\left(\nu N\to\nu X\right)-\sigma\left(\bar\nu N\to\bar\nu X\right)}{\sigma\left(\nu N\to\mu^-X\right)-\sigma\left(\bar\nu N\to\mu^+X\right)} ,
$$

the neutral-current excess over the charged-current excess. In the parton model, with the target an equal mix of protons and neutrons and the sea neglected,

$$
R^-=g_L^2-g_R^2 ,
\qquad
g_L^2=\left(g_L^u\right)^2+\left(g_L^d\right)^2 ,
\qquad
g_R^2=\left(g_R^u\right)^2+\left(g_R^d\right)^2 ,
$$

and evaluating with the table's couplings gives

$$
g_L^2=\frac12-\sin^2\theta_W+\frac59\sin^4\theta_W ,
\qquad
g_R^2=\frac59\sin^4\theta_W ,
\qquad
R^-=\frac12-\sin^2\theta_W .
$$

**The $\sin^4$ terms cancel, and that is the point of the construction.** Each of $g_L^2$ and $g_R^2$ carries $\tfrac59\sin^4\theta_W$, with the same coefficient and opposite signs, so the difference is linear in $\sin^2\theta_W$. A relation linear in the unknown needs no iteration and no second measurement to extract it, which is why this particular ratio was the one that fixed the angle in 1973 and not some other. The $\sin^4$ terms are not small at $\sin^2\theta_W=0.23$: $\tfrac59\sin^4\theta_W=0.0297$, which is eleven per cent of $R^-=0.2688$. Their exact cancellation is therefore numerically essential and not a nicety, and it is a property of the doublet's charges: the coefficients $\tfrac49$ and $\tfrac19$ of the up and down right-handed couplings are fixed by $Q_u$ and $Q_d$, and any other assignment would leave a residual quadratic term in a relation that is quoted as linear.

**The parton distributions cancel because the numerator and the denominator are built from the same valence difference.** Both excesses are proportional to the difference of the up and down valence distributions, so the ratio is independent of the nucleon's structure. That is what makes the relation a measurement of the angle rather than of the parton model, and it is why the early experiments could be interpreted before the parton distributions were known.

**The measurement that established the sector.** The neutral current was observed at Gargamelle in 1973, as the elastic scattering of muon neutrinos off electrons and the deep inelastic scattering off nuclei with no muon in the final state. Before that observation the electroweak theory's neutral-current sector was an untested prediction, and the angle was a free parameter of a model with no empirical anchor. After it, the sector had a measured parameter and the theory had survived its first test that was not a charged-current one.

**The structure, in one line.** The charged current is purely left-handed and measures one number; the neutral current has a left and a right part, and their difference is what $R^-$ isolates. The surviving $\tfrac12$ is the isoscalar bookkeeping of the doublet's two charges, and the surviving $-\sin^2\theta_W$ is the right-handed coupling's size. The relation is the low-energy form of what the $Z$ pole measures precisely, and the two agree.

**What the low-energy measurements establish.** That the neutral current exists, that it is chiral with the sign and the size the table predicts, and that its strength is the $Z$ exchange rather than something else. They do not measure the angle to the precision of the $Z$ pole, and they are not competitive with it; they are the confirmation that the sector is not an artefact of the resonance.

## The Three Angles

**One name, three quantities.** The literature quotes three numbers for $\sin^2\theta_W$, and they differ in the third digit. Each is a different definition, and the differences are the radiative corrections themselves. The table gives all three, with the definition and the value.

| Angle | Definition | Value |
|---|---|---|
| on-shell | $1-M_W^2/M_Z^2$ | $0.22305$ |
| $\overline{\mathrm{MS}}$ at $M_Z$ | the coupling ratio in modified minimal subtraction | $0.23122$ |
| effective leptonic | from $A_{FB}^{0,\ell}$ and $A_{LR}$ | $0.23148$ |

**Why the on-shell one is smallest, and by how much.** The on-shell angle is built from two masses, which are measured at low momentum transfer and include the hadronic vacuum polarisation. The $\overline{\mathrm{MS}}$ angle is defined by subtracting that polarisation into a running coupling. The ratio is

$$
\kappa_{\mathrm{OS}}\equiv\frac{\sin^2\theta_{\mathrm{OS}}}{\sin^2\theta_{\overline{\mathrm{MS}}}}=\frac{0.22305}{0.23122}=0.9647 ,
$$

so the on-shell angle is $3.5$ per cent the smaller. The quantity to compare is not the angle but the product, which is $\sin^2\theta_{\mathrm{OS}}\cos^2\theta_{\mathrm{OS}}=0.17330$ against $\sin^2\theta_{\overline{\mathrm{MS}}}\cos^2\theta_{\overline{\mathrm{MS}}}=0.17776$, a deficit of $2.5$ per cent. The step from the product to the angle is exact: since $\sin^2\cos^2$ responds to $\sin^2$ with the factor $(c^2-s^2)/c^2=0.713$, the inverse factor $c^2/(c^2-s^2)=1.40$ multiplies the product's shift, and $1.40\times(0.97492-1)=-0.0352$ against the actual $-0.0353$. That identity is the check; the cause is that the two definitions sit on different couplings, the on-shell one on the masses, hence on $\alpha(0)$, and the $\overline{\mathrm{MS}}$ one on $\alpha(M_Z)$, whose ratio is $0.9337$.

**The relation, written once and labelled as a rewriting.** The two definitions are connected by

$$
\sin^2\theta_{\mathrm{OS}}\cos^2\theta_{\mathrm{OS}}=\frac{\pi\,\alpha(0)}{\sqrt2\,G_F\,M_Z^2}\cdot\frac{1}{1-\Delta r} ,
$$

with $\Delta r=0.0355$ of article 4. This is not an independent prediction: $\Delta r$ was defined through the same three quantities, so the equation is the definition rearranged. Its value is that it shows how the angle's value and $\Delta r$ are two views of one number, and it shows which input carries the difference. Solving it gives $0.22305$, which is the on-shell value by construction.

**Why the effective one is the largest, and by very little.** The effective leptonic angle is extracted from asymmetries at the $Z$ pole, and the extraction folds in the vertex corrections and the photon–$Z$ mixing that the asymmetries actually contain. Its ratio to the $\overline{\mathrm{MS}}$ value is

$$
\kappa_{\mathrm{eff}}\equiv\frac{\sin^2\theta_{\mathrm{eff}}}{\sin^2\theta_{\overline{\mathrm{MS}}}}=\frac{0.23148}{0.23122}=1.0011 ,
$$

one part in a thousand, and the sign is positive because the dominant absorbed correction is the $\gamma$–$Z$ mixing, whose size is set by the light-fermion contribution to the photon vacuum polarisation.

**The pattern in one sentence.** The on-shell angle differs from the $\overline{\mathrm{MS}}$ one because of the running of $\alpha$; the effective angle differs from the $\overline{\mathrm{MS}}$ one because of the vertex corrections; and the first difference is thirty times the second.

**What each is good for.** The on-shell angle is the one a tree-level calculation wants, because it is built from the masses that enter the tree Lagrangian. The $\overline{\mathrm{MS}}$ angle is the one a running coupling wants, because it is defined at a scale. The effective angle is the one an asymmetry wants, because it is what the asymmetry measures. Quoting one and comparing it with a measurement of another is a comparison of two different objects, and it is the commonest error in the literature of this sector.

**The lesson for the corpus.** Every number of this sector must carry its scheme, which is why the parameter table of article 1 has a scheme column and why article 4's $\Delta r$ could not be stated without naming which $\alpha$ it used. A bare $\sin^2\theta_W=0.23$ is not a value; it is a rounding of three values.

## The $Z$ Pole

**The resonance is the most precise laboratory in the sector.** At $\sqrt{s}=M_Z$ the cross section is dominated by $Z$ exchange, the initial-state radiation is calculable, and the four LEP experiments collected some $1.7\times10^7$ hadronic $Z$ decays between them. The measurements that follow are the sharpest tests the Standard Model has, and they are all measurements of the couplings of the table above.

**The partial widths.** Evaluating the width formula with the table's couplings at $\sin^2\theta_W=0.23122$, $M_Z=91.1876$ GeV and $\alpha_s=0.1186$:

| Channel | Computed (MeV) | Measured (MeV) |
|---|---|---|
| $\nu\bar\nu$ | $165.9$ | $167.0$ |
| $e^+e^-$ | $83.4$ | $83.91$ |
| $u\bar u$ and $c\bar c$, each | $296.2$ | $299.0$ |
| $d\bar d$ and $s\bar s$, each | $381.8$ | (in $R_\ell$) |
| $b\bar b$ | $381.8$ | $377.0$ |
| hadrons, total | $1737.6$ | $1744.4$ |
| invisible | $497.6$ | $499.0$ |
| total | $2485.5$ | $2495.2$ |

**The agreement is one per cent or better in every channel.** The residual is the missing higher-order terms and the quark-mass effects in the $b$ channel, which is where the largest discrepancy sits and where the top quark's loop enters. A tree-level calculation reproducing eight widths to that accuracy is the statement that the couplings of §*The Couplings of Every Fermion* are right.

**The invisible width and the number of neutrinos.** The neutrino's couplings are $\tfrac12$ and $\tfrac12$ whatever the angle, so the partial width per neutrino species is fixed by $G_F$ and $M_Z$ alone:

$$
\Gamma_{\nu\bar\nu}=\frac{G_FM_Z^3}{6\sqrt2\pi}\cdot\frac12=165.9\ \mathrm{MeV} ,
\qquad
N_\nu=\frac{\Gamma_{\mathrm{inv}}}{\Gamma_{\nu\bar\nu}}=\frac{499.0\pm1.5}{165.9}=3.008\pm0.009 .
$$

**The published $2.984$ and this $3.008$, and why they are both right.** The measured invisible width is $499.0\pm1.5$ MeV and it is divided, in the literature, by the *radiatively corrected* width per species, $167.2$ MeV, giving $2.984\pm0.008$. This article's denominator is the tree value $165.9$, so its ratio is larger by the $0.8$ per cent that the correction supplies — the same $0.8$ per cent visible in the first row of the table above, where $165.9$ sits against the measured $167.0$. Neither number is a fourth neutrino: a fourth light species would add a whole $165.9$ MeV to the invisible width, a hundred times the $1.5$ MeV error, so the species count is three to overwhelming precision and the gap between the two ratios is a bookkeeping of corrections rather than a counting of particles.

**That is the sharpest fact of the sector, and its sharpness is structural.** The number of light neutrinos is measured without knowing the mixing angle, the strong coupling, or any hadronic quantity, because the neutrino's $Z$ coupling contains no $Q$ and therefore no $\sin^2\theta_W$. Three is the answer, the fourth is excluded, and a fourth with a mass below $M_Z/2$ would have been seen.

**The asymmetries.** The $Z$ coupling is chiral, so its interference with the photon produces an angular asymmetry. On the pole,

$$
A_{FB}^{0,f}=\frac34A_eA_f ,
\qquad
A_{LR}=A_e ,
$$

with $A_f$ the column of the table. Computed with $\sin^2\theta_{\mathrm{eff}}=0.23148$ and compared with the measured values:

| Quantity | Computed | Measured |
|---|---|---|
| $A_{FB}^{0,e}$ | $0.0163$ | $0.0145$ |
| $A_{FB}^{0,\mu}$ | $0.0163$ | $0.0169$ |
| $A_{FB}^{0,\tau}$ | $0.0163$ | $0.0188$ |
| $A_{FB}^{0,b}$ | $0.1034$ | $0.0992$ |
| $A_{FB}^{0,c}$ | $0.0738$ | $0.0707$ |
| $A_{LR}$ | $0.1474$ | $0.1514$ |

**The pattern of the residuals is the interesting part.** The three leptonic asymmetries are one number repeated, $0.0163$, and they sit within about one and a half standard deviations of the measured $0.0145$, $0.0169$ and $0.0188$. The $b$ and $c$ asymmetries sit four per cent high, at $2.6$ and $0.9$ standard deviations. And $A_{LR}$, the sharpest single measurement of the set, sits three per cent low at $1.8$ standard deviations. The three cannot be brought into agreement by adjusting one number, and the failure is the long-standing $A_{LR}$–$A_{FB}^{0,b}$ tension: the two most precise determinations of $\sin^2\theta_{\mathrm{eff}}$ differ by about three standard deviations. Whether it is a statistical fluctuation, an experimental systematic, or a signal is unsettled, and it is one of the few places where the sector's precision exceeds the theory's.

**The ratios.** Two ratios of widths are quoted because they are insensitive to the overall normalisation:

$$
R_\ell=\frac{\Gamma_{\mathrm{had}}}{\Gamma_{\ell\ell}}=20.83\ \text{(computed)},
\qquad
R_b=\frac{\Gamma_{b\bar b}}{\Gamma_{\mathrm{had}}}=0.2197 ,
\qquad
R_c=\frac{\Gamma_{c\bar c}}{\Gamma_{\mathrm{had}}}=0.1704 ,
$$

against the measured $20.767$, $0.21629$ and $0.1721$. The $R_b$ value is the most informative: it is sensitive to the top quark's mass through the vertex correction, and it is the measurement that constrained the top mass before the top was found.

**The couplings the pole determines.** From the widths and asymmetries the four numbers $g_{Vf}$ and $g_{Af}$ for each fermion family are extracted, and they agree with the table. The extraction is the operational meaning of the table: the $Z$ couplings are not theoretical constructs but measured quantities with errors in the fourth digit.

**The $\rho$ link.** Article 4 defined $\rho=M_W^2/(M_Z^2\cos^2\theta_W)$ and found one by identity for the doublet. The same parameter appears here as the statement that the on-shell angle and the mass ratio are the same measurement. A deviation of $\rho$ from one would show as a mismatch between the on-shell angle and the effective one that no vertex correction can explain, and [Electroweak Precision Observables: the Oblique Parameters $S$, $T$, $U$](electroweak-precision-observables-the-oblique-parameters-s-t-u.html) organises the search for such a mismatch into the three oblique parameters.

## What the Neutral Current Measures That the Charged Current Cannot

**The charged current is one number.** The $W$ couples only to left-handed fermions, with strength $g/\sqrt2$ and no dependence on charge or isospin. Its measurement, through the muon lifetime, gives $G_F$ and hence $v$; it says nothing about the mixing, because there is nothing to mix.

**The neutral current is two numbers per fermion.** The $Z$ couples with $g_L$ and $g_R$, and their ratio depends on $Q$ and $\sin^2\theta_W$. That is why the neutral current measures the angle and the charged current does not: the neutral current is the only place where the two couplings of the product group appear in one vertex.

**The over-determination.** The sector's measured quantities are $M_W$, $M_Z$, $\sin^2\theta_W$ (three ways), $\alpha$, $G_F$, the eight $Z$ partial widths, the asymmetries and $\alpha_s$. The parameters are three, $g$, $g_{\mathrm Y}$ and $v$, plus $\alpha_s$. The ratio is more than ten to one, and the consistency of the over-determination is the strongest evidence the Standard Model has.

**The one place the over-determination bites hardest.** The relation $M_W=M_Z\cos\theta_W$ at tree level, corrected by $\Delta r$, ties the angle to the masses. A precision measurement of $M_W$ is therefore a measurement of the radiative corrections, and a discrepancy in $M_W$ is a discrepancy in the quantum sector rather than in the tree Lagrangian. That is why the $W$ mass remains the most sensitive single number in the sector and why its measurement at the LHC and at a future $e^+e^-$ collider is a search for new physics rather than a confirmation of the old.

## The Framework's Position

**The corpus's own classification.** [Electroweak Theory under the Biquaternionic Framework — A Research Agenda](electroweak-theory-under-the-biquaternion-framework-a-research-agenda.html) carries the row

| Quantity | Status | What would be needed |
|---|---|---|
| Weinberg angle, electric-charge relation $Q_{\mathrm{em}}=T_3+Y$ | **No route yet** | fixing both couplings and the embedding of $\mathrm{U}(1)$ in $\mathrm{U}(2)$; requires hypercharge |

and the article does not improve on it. The statement is exact: the framework supplies two couplings, $\kappa$ for the non-abelian factor and $ϙ$ for the abelian one, both free, and no embedding that would relate them. ($\kappa$ here is the agenda's gauge coupling and has nothing to do with $\kappa_{\mathrm{OS}}$, which is a ratio of two angles; the corpus reuses the letter and the subscript is what separates them.)

**Why the angle is not merely a missing number.** An angle is a ratio, and a ratio can be derived from a structure even when the individual numbers cannot. What the framework lacks is therefore not the values of $g$ and $g_{\mathrm Y}$ but a structure in which the two form a pair. The two couplings sit on different objects — one on the compact factor $\mathrm{SU}(2)\subset\mathbb{B}_\Phi$, one on the central phase — and nothing in the algebra relates the two objects' normalisations.

**What the algebra does supply, and it is not nothing.** The rotation of this article is a rotation in a two-dimensional neutral space, and the algebra does contain a two-dimensional space of neutral directions: the Cartan subalgebra of $\mathfrak{su}(2)$ is one-dimensional, and the central direction adds a second. So the *arena* of the mixing exists. What is missing is the metric on it: the angle is a ratio of norms, and the algebra assigns no relative normalisation to the compact generator and the central one.

**The sharpest way to say it.** The mixing angle is the angle between two directions in the neutral space, measured in the metric that the kinetic terms define. The algebra supplies the directions and not the metric, and the free overall coefficient of each kinetic term is exactly the freedom that leaves the angle undetermined. A framework that fixed the relative normalisation of its two kinetic terms would have a prediction; this one does not fix either.

**What would settle it.** Two things, and they are the agenda's two.

- **A normalisation principle.** A reason why the central and compact kinetic terms carry equal coefficients. The standard model has such a principle only in the grand-unified setting, where the two factors sit in one simple group and the couplings meet at one scale; [Grand Unification and the Biquaternion Algebra Ceiling](grand-unification-and-the-biquaternion-algebra-ceiling.html) records that route — hypercharge as a generator of a simple group, its eigenvalues fixed by tracelessness, the couplings meeting at one scale — and states the negative half too: the framework's abelian factor is central and continuous, so it has neither the embedding nor the meeting.
- **An embedding.** A construction in which $\mathrm{U}(1)_Y$ and the Cartan of $SU(2)_L$ are two directions of one algebra. The framework's $\mathrm{U}(2)$ is a candidate arena and its Cartan is two-dimensional, so the second is not obviously impossible; it is unexplored.

**The vector-like obstruction applies here too.** The central phase acts as a scalar, so its charge is the same on both chiralities, and the neutral current of this article is chiral. A framework whose abelian factor cannot distinguish the two parts of a field cannot produce the $g_L\neq g_R$ of the table, whatever it does about normalisation. That is the same obstruction as in [The Electroweak Gauge Group and the Hypercharge Assignment](the-electroweak-gauge-group-and-the-hypercharge-assignment.html), seen at the level of the vertex rather than of the multiplet.

**What this article therefore is.** A computation about the model. Its value to the framework is the ledger: the angle is one number, over-determined by ten, and the framework supplies none of the over-determination. The count of what the algebra would have to produce to write this article from its own resources is three things — a chiral abelian factor, an embedding of the two neutral directions in one algebra, and a normalisation principle for the two kinetic terms — and all three are absent.

## Summary

The neutral sector has two gauge fields and one angle. Writing the physical fields as $A=\sin\theta_WW^3+\cos\theta_WB$ and $Z=\cos\theta_WW^3-\sin\theta_WB$, and demanding that the photon couple as pure electric charge with no $T_3$ admixture, fixes $\tan\theta_W=g_{\mathrm Y}/g$ and gives $e=g\sin\theta_W=g_{\mathrm Y}\cos\theta_W$. The $Z$ bracket then comes out as $\sqrt{g^2+g_{\mathrm Y}^2}(J^3-\sin^2\theta_WJ^Q)$ with no further freedom, and the square arises because the coefficient is $g_{\mathrm Y}^2/(g^2+g_{\mathrm Y}^2)$: two powers from the numerator and one from each term of the denominator. The angle is therefore defined by one condition, and its appearance squared in the neutral current is a consequence of that condition and not a second convention.

The chiral decomposition gives $g_L=T_3-Q\sin^2\theta_W$, $g_R=-Q\sin^2\theta_W$, $g_V=T_3-2Q\sin^2\theta_W$ and $g_A=T_3$. The axial coupling is the isospin exactly, because the mixing term cancels between chiralities, and that is why the neutrino's couplings are both $\tfrac12$ whatever the angle. At $\sin^2\theta_W=0.23122$ the electron's vector coupling is $-0.0376$, seven per cent of its axial coupling, a near-cancellation that makes the leptonic asymmetries small; the up quark's is $+0.1917$ and the down quark's $-0.3459$.

Below the $Z$ mass the current is a contact interaction of strength $4G_F/\sqrt2$, and the classic measurements are neutrino–electron scattering and the Paschos–Wolfenstein ratio of differences, $R^-=\tfrac12-\sin^2\theta_W$, in which the parton distributions cancel. The neutral current was observed at Gargamelle in 1973, and that observation turned the angle from a free parameter into a measured one.

Three angles carry the name. The on-shell $1-M_W^2/M_Z^2=0.22305$, the $\overline{\mathrm{MS}}$ value $0.23122$ and the effective leptonic value from the asymmetries $0.23148$ differ by the radiative corrections themselves: $\kappa_{\mathrm{OS}}=0.9647$, a $3.5$ per cent deficit whose origin is the running of $\alpha$ from $137.036$ to $127.95$, and $\kappa_{\mathrm{eff}}=1.0011$, one part in a thousand, dominated by photon–$Z$ mixing. The first difference is thirty times the second, and quoting one angle against a measurement of another is the commonest error in the sector.

At the pole the widths are reproduced to half a per cent: $165.9$ MeV per neutrino against $167.0$, $83.4$ against $83.91$ for electrons, $1737.6$ against $1744.4$ for hadrons, $2485.5$ against $2495.2$ in total. The invisible width gives $N_\nu=499.0/165.9=3.008\pm0.009$ against the published $2.984\pm0.008$, the difference being $165.9$ against the corrected $167.2$ MeV per species, and that number is sharp because the neutrino's $Z$ coupling contains no charge and therefore no mixing angle. The asymmetries $A_{FB}^{0,f}=\tfrac34A_eA_f$ and $A_{LR}=A_e$ agree for the leptons and disagree for $b$ quarks and for $A_{LR}$ at the three-sigma level, which is the sector's standing tension. The ratios $R_\ell=20.83$, $R_b=0.2197$ and $R_c=0.1704$ sit against $20.767$, $0.21629$ and $0.1721$.

The neutral current measures what the charged current cannot, because it is the only vertex in which both couplings of the product group appear: the charged current gives one number, $g$, while the neutral current gives two per channel, $g_L$ and $g_R$, whose ratio is the angle. The sector is over-determined by more than ten to one, and that over-determination is the strongest evidence the model has.

The framework has no route to the angle, and the corpus's agenda says so. The obstruction is not a missing number but a missing pair: the two couplings sit on different objects, the compact factor and the central phase, and nothing relates their normalisations, so the angle — which is a ratio of norms on a two-dimensional neutral space whose directions the algebra does supply — is undetermined. The framework's abelian factor is moreover vector-like, so it cannot produce $g_L\neq g_R$ at all. Three things are needed and all three are absent: a chiral abelian factor, an embedding of the two neutral directions in one algebra, and a normalisation principle for the two kinetic terms.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $W^3_\mu$, $B_\mu$ | The two neutral gauge fields before mixing |
| $A_\mu$, $Z_\mu$ | The photon and the neutral massive field |
| $\theta_W$ | $\tan\theta_W=g_{\mathrm Y}/g$, the rotation that makes the photon pure charge |
| $e$ | $g\sin\theta_W=g_{\mathrm Y}\cos\theta_W$ |
| $J^3_\mu$, $J^Y_\mu$, $J^Q_\mu$ | The isospin, hypercharge and electromagnetic currents |
| $T_{3f}$, $Q_f$, $Y_f$ | Isospin, charge and hypercharge of the fermion $f$ |
| $g_{Lf}$, $g_{Rf}$ | $T_3-Q\sin^2\theta_W$ and $-Q\sin^2\theta_W$, the chiral $Z$ couplings |
| $g_{Vf}$, $g_{Af}$ | $T_3-2Q\sin^2\theta_W$ and $T_3$, the vector and axial $Z$ couplings |
| $A_f$ | $2g_Vg_A/(g_V^2+g_A^2)$, the left-right asymmetry parameter |
| $A_{FB}^{0,f}$ | $\tfrac34A_eA_f$, the pole forward-backward asymmetry |
| $A_{LR}$ | $A_e$, the left-right asymmetry |
| $R_\ell$, $R_b$, $R_c$ | Ratios of $Z$ partial widths |
| $R^-$ | $\tfrac12-\sin^2\theta_W$, the Paschos–Wolfenstein ratio of differences |
| $\kappa_{\mathrm{OS}}$, $\kappa_{\mathrm{eff}}$ | $0.9647$ and $1.0011$, the ratios to the $\overline{\mathrm{MS}}$ angle |
| $\Delta r$ | $0.0355$, the correction relating $\alpha(0)$, $G_F$, $M_W$ and the angle |
| $\sin^2\theta_{\mathrm{eff}}$ | The effective leptonic angle, $0.23148$ |
| $N_\nu$ | The number of light neutrinos from the invisible width: $2.984$ published, $3.008$ from this article's tree widths |

## Further Reading

- [Electroweak Symmetry Breaking: the Doublet, the Potential and the Gauge-Boson Masses](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-gauge-boson-masses.html). The mass matrix from which the mixing angle is here recovered as the diagonalising angle.
- [The W and Z Bosons in Biquaternionic Form](the-w-and-z-bosons-in-biquaternionic-form.html). The same currents written with the algebra's scalar part, and the $Z$-pole section this article expands.
- [The Electroweak Gauge Group and the Hypercharge Assignment](the-electroweak-gauge-group-and-the-hypercharge-assignment.html). Why $Q=T_3+Y$ holds, which this article uses to eliminate $Y$.
- [The Standard Model Lagrangian Assembled: Four Sectors in One Expression](the-standard-model-lagrangian-assembled-four-sectors-in-one-expression.html). The neutral current in the assembled sum.
- [Electroweak Theory under the Biquaternionic Framework — A Research Agenda](electroweak-theory-under-the-biquaternion-framework-a-research-agenda.html). The *no route yet* row and the two settling objects.
- [The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html). The $\mathrm{U}(2)$ whose Cartan is the two-dimensional neutral space.
- [Anomalies and Anomaly Cancellation in Biquaternionic Form](anomalies-and-anomaly-cancellation-in-biquaternionic-form.html). The vector-like character of the framework's abelian factor, which blocks the chiral neutral current.
- [The Standard Model: Content, Quantum Numbers and the Nineteen Parameters](the-standard-model-content-quantum-numbers-and-the-nineteen-parameters.html). The couplings $g$ and $g_{\mathrm Y}$ in the count of nineteen.

The three companions named in the sections above are all in the corpus: [Electroweak Precision Observables: the Oblique Parameters $S$, $T$, $U$](electroweak-precision-observables-the-oblique-parameters-s-t-u.html) organises the $\rho$ and $A_{LR}$ statements, [Meson Mixing, Rare Decays and the Unitarity Triangle as a Closure Test](meson-mixing-rare-decays-and-the-unitarity-triangle-as-a-closure-test.html) carries the GIM extension to one loop, and [Grand Unification and the Biquaternion Algebra Ceiling](grand-unification-and-the-biquaternion-algebra-ceiling.html) carries the normalisation route the framework lacks.
