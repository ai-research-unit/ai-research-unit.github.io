# __The W and Z Bosons in Biquaternionic Form__

## Introduction

In the electricity-and-magnetism subcategory the framework reaches the photon exactly: the massless, neutral, spin-one field is the self-dual part of the material bivector, and the companion article *The Photon in Biquaternionic Form* identifies it with the propagating solution of the biquaternionic Maxwell system. The W and Z are the other half of the same multiplet structure. They are the **massive** spin-one fields of the weak interaction: the charged $W^\pm$ and the neutral $Z$, with masses of order $80$ and $91$ GeV, plus the massless photon with which the Z mixes in the neutral sector. This article asks what the framework has for them.

The answer has three layers, and the article is organised around them. The first layer is **kinematic, and the framework reaches it.** A single W or Z is a massive spin-one field with three polarizations, and the massive spin-one field is the Proca field of the companion articles; its carrier in the framework is the material sector and its quantization is the Proca quantization. The charged and neutral *labels* are the eigenvalues of the Cartan generator of the compact factor acting by the adjoint action, so the framework's adjoint action on the material sector realizes the charges $\pm1$ and $0$ that the W and Z carry. The mixing of the Z with the photon is a rotation of the two commuting directions of $\mathrm{U}(2)$, which the algebra contains. The second layer is **mass generation, and the framework reaches only part of it.** The standard mass relations, $M_W=gv/2$ and $M_Z=\sqrt{g^2+g_{\mathrm Y}^2}\,v/2$, follow from a scalar multiplet that is a doublet of $SU(2)$ with hypercharge $1/2$; the framework's scalars are central, hence singlets, and the abelian Higgs mechanism it does support generates a mass only in the neutral, central direction. The third layer is **the chiral coupling, and the framework does not reach it.** The W couples to the $L$ part of a fermion field and not to the $R$ part, and the framework's gauge actions on a field that carries a gauge index are the central phase, the adjoint action on the material sector, and left multiplication on the algebra — none of which separates the two parts named by the subscript, because the adjoint is real and left multiplication keeps the letter, so the two parts of a field sit in equivalent representations and $SU(2)$ is pseudoreal. The companion article *Chiral Fermions in the Biquaternion Framework* establishes that a central gauge action cannot be chiral and records the non-central case as the open question; what the framework's available non-central actions do not supply is the asymmetric left/right assignment that the W requires.

The article is organised as follows. A first section transcribes the standard electroweak vector-boson physics — the gauge group, the fields, the mixing, the masses, the currents, the self-couplings and the measured values — with citations to the standard literature. A second section locates the charged and neutral fields in the algebra and identifies the eigenvalue problem that supplies their charges. A third section treats the mass generation and fixes precisely what the framework supplies and what it does not. A fourth treats the currents and the vector-like obstruction. A fifth treats the trilinear and quartic gauge self-couplings, which the non-abelian structure of the material sector does supply. A closing section separates the three layers, and after it one closing section prints the older gamma display beside the axis-free one, for comparison with the literature; the argument itself needs no frame, and the summary and the notation table close the article.

We use the conventions of the companion articles: the algebra, the units, the sectors, the gradient and the d'Alembertian are those of *Algebra and Element Conventions*, *Frame and Metric Conventions* and *Operator and Calculus Conventions*, and none is restated here. The compact factor is
$$
\mathrm{U}(2)=\mathbb{R}(ie_t)\oplus\mathrm{SU}(2),
\qquad
\mathrm{SU}(2)=\mathrm{span}_\mathbb{R}\{\vec e_x,\vec e_y,\vec e_z\}\subset\mathbb{B}_{\Phi} ,
$$
of real dimension four, with the commutator $[e_a,e_b]$ read from the multiplication table of *Algebra and Element Conventions* and generators $T_a=\tfrac12 e_a$. The connection components are taken in the unnormalized basis $e_a$, in which the structure constants are $f_{abc}=2\varepsilon_{abc}$; in the normalized basis $T_a=\tfrac12e_a$ the same algebra reads $[T_a,T_b]=\sum_c\varepsilon_{abc}T_c$, with $f_{abc}=\varepsilon_{abc}$; and in the Hermitian-generator realization $T_a=ie_a\in\mathbb{B}_{\Psi}$ of the BRST companion it reads $[T_a,T_b]=2i\sum_c\varepsilon_{abc}T_c=i\sum_c f_{abc}T_c$, the central $i$ relating the two realizations. The Cartan generator of the compact factor is $T_3=\tfrac12\vec e_z$, whose Hermitian partner is $iT_3=\tfrac12i\vec e_z$; the charge operator is the adjoint action $\tilde S_{\Psi,\mathrm{adj},3}=\tfrac12\mathrm{ad}_{i\vec e_z}=\mathrm{ad}_{\,iT_3}$, whose eigenvalues and eigenvectors on the material basis are derived below.
Spacetime indices are written low and every contraction is an explicit sum, in the $i r'_t$ device of *Physics Units and Common Elements Conventions*; with that device the plain sum $\sum_\mu W_\mu W_\mu$ is already the invariant. The one metric a display needs is the unit metric $\delta_{\mu\nu}=(1,1,1,1)$ of *Frame and Metric Conventions*, the same in both frames, and the polarization sums below use it; the one minus of the interval is the square of the $i$ in $Q_t=i q'_t$. Every framework formula carries $c$ and $\kappa=\frac{ϙ}{\hbar}$ explicitly, and no unit is set to one; in the electroweak formulae the standard symbols $g,g_{\mathrm Y},v,\theta_W$ carry the standard normalization, while the framework's coupling is $\kappa=\frac{ϙ}{\hbar}$ where it appears in the algebra's expressions.

- Companion article *Electroweak Theory under the Biquaternion Framework — A Research Agenda*, for the boundary statement and the list of open problems.
- Companion article *The Standard Model under the Biquaternion Framework — A Research Agenda*, for the placement of the electroweak sector in the larger structure.
- Companion article *The Proca Equation: Massive Spin 1 in Biquaternionic Form*, for the massive spin-one field equation and the Lorenz condition.
- Companion article *Canonical Quantization of the Biquaternion Proca Field*, for the three polarizations, the constraint structure and the propagator.
- Companion article *The Higgs Mechanism in Biquaternionic Form*, for the abelian Higgs mechanism in the algebra and the central scalar.
- Companion article *Goldstone's Theorem in Biquaternionic Form*, for the would-be Goldstone mode and its removal.
- Companion article *Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form*, for the adjoint action as the spin-one representation and the charge eigenvalues.
- Companion article *Non-Abelian Gauge Fields in Biquaternionic Form*, for the connection, the curvature and the Yang–Mills density.
- Companion article *The Yang–Mills Equation in Biquaternionic Form*, for the field equation and the covariant conservation of the current.
- Companion article *Chiral Fermions in the Biquaternion Framework*, for the obstruction to a chiral coupling from a central action.
- Companion article *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*, for the covariant derivative and the current.
- Companion article *The Gauge Principle in Biquaternionic Form*, for the derivation of the gauge structure from the central phase.
- Companion article *The Photon in Biquaternionic Form*, for the massless neutral vector field and the self-dual split.

## The Standard Electroweak Vector Bosons

### The Gauge Fields and the Mixing

The electroweak gauge sector is the product group $SU(2)_L\times \mathrm{U}(1)_Y$, with three gauge fields $W_{\mu a}$ $(a=1,2,3)$ of coupling $g$ and one field $B_\mu$ of coupling $g_{\mathrm Y}$. The kinetic terms are
$$
\mathcal{L}_{\mathrm{kin}}=-\tfrac14\sum_{a,\mu,\nu}W_{\mu\nu a}W_{\mu\nu a}-\tfrac14\,\sum_{\mu,\nu}B_{\mu\nu}B_{\mu\nu},
$$
$$
W_{\mu\nu a}=\frac{\partial W_{\nu a}}{\partial R_\mu}-\frac{\partial W_{\mu a}}{\partial R_\nu}+g\sum_{b,c}\varepsilon_{abc}W_{\mu b}W_{\nu c},
\qquad
B_{\mu\nu}=\frac{\partial B_\nu}{\partial R_\mu}-\frac{\partial B_\mu}{\partial R_\nu}.
$$
The W fields are charged under the electromagnetic subgroup and the physical charged combinations are
$$
W^\pm_\mu=\frac{1}{\sqrt{2}}\left(W_{\mu 1}\mp i W_{\mu 2}\right),
\qquad
W^-_\mu=(W^+_\mu)^\dagger ,
$$
with electric charge $\pm1$. The two neutral fields mix through the **Weinberg angle** $\theta_W$,
$$
Z_\mu=\cos\theta_W\,W_{\mu 3}-\sin\theta_W\,B_\mu,
\qquad
A_\mu=\sin\theta_W\,W_{\mu 3}+\cos\theta_W\,B_\mu,
\qquad
\tan\theta_W=\frac{g_{\mathrm Y}}{g},
$$
The mixing is the statement that the two neutral gauge fields have different masses, so that the mass matrix is diagonalized in the rotated basis; the electromagnetic field is the massless combination and the Z is the massive one.

### The Masses and the Electroweak Scale

The masses arise from the Higgs sector, which is standard physics and is transcribed here as such. A complex scalar doublet $\xi_{\mathrm{scl}}$, of components ${\xi_{\mathrm{scl}}}^+$ and ${\xi_{\mathrm{scl}}}^0$ and of hypercharge $Y_{\mathrm{scl},\xi}=\tfrac12$, with the potential $V=\lambda\big(|{\xi_{\mathrm{scl}}}^+|^2+|{\xi_{\mathrm{scl}}}^0|^2-v^2/2\big)^2$ and the vacuum expectation values
$$
\langle{\xi_{\mathrm{scl}}}^+\rangle=0,
\qquad
\langle{\xi_{\mathrm{scl}}}^0\rangle=\frac{v}{\sqrt2},
\qquad
v=246.22\ \mathrm{GeV},
$$
gives, through the covariant kinetic term $|D_\mu\xi_{\mathrm{scl}}|^2$, the squared norm summed over the two components, with $D_\mu=\partial/\partial R_\mu+ig\sum_a T_aW_{\mu a}+i\,g_{\mathrm Y}Y_{\mathrm{scl},\xi} B_\mu$, the mass terms
$$
M_W=\frac{gv}{2},
\qquad
M_Z=\frac{\sqrt{g^2+g_{\mathrm Y}^2}\,v}{2}=\frac{M_W}{\cos\theta_W},
\qquad
M_\gamma=0 .
$$
The electromagnetic coupling is the combination that the unbroken generator carries,
$$
e=g\sin\theta_W=g_{\mathrm Y}\cos\theta_W ,
\qquad
\alpha=\frac{e^2}{4\pi},
$$
and the Fermi constant fixes the scale,
$$
\frac{G_F}{\sqrt{2}}=\frac{g^2}{8M_W^2}=\frac{1}{2v^2},
\qquad
G_F=1.1663787\times 10^{-5}\ \mathrm{GeV}^{-2},
\qquad
v=( \sqrt{2}\,G_F )^{-1/2}=246.22\ \mathrm{GeV}.
$$
The masses obey the tree-level relation
$$
\rho\equiv\frac{M_W^2}{M_Z^2\cos^2\theta_W}=1 ,
$$
which holds for a scalar multiplet of weak isospin $1/2$ and hypercharge $1/2$; the measured value, $\rho=1.00038\pm0.00020$, defined with the on-shell mixing angle, is consistent with it. The measured masses are $M_W=80.377\pm0.012$ GeV and $M_Z=91.1876\pm0.0021$ GeV, and the measured weak mixing angle is $\sin^2\theta_W=0.23122\pm0.00004$ in the $\overline{\mathrm{MS}}$ scheme. These values are the empirical input of the sector; the tree-level relations above are identities, and the difference between the tree-level expressions and the measured masses is the radiative correction $\Delta r$, which is standard.

The framework's mass formula for an abelian charged scalar, $\mathcal{L}\supset-\sum_{\mu,\nu}g_{\mu\nu}(D_\mu\xi_{\mathrm{scl}})^*(D_\nu\xi_{\mathrm{scl}})$ with $D_\mu=\partial/\partial R_\mu+i\kappa A_\mu$ and $\langle|\xi_{\mathrm{scl}}|\rangle=v/\sqrt2$, is
$$
\boxed{\;M_A=\frac{ϙ\,v}{\hbar}=\kappa v\;},
$$
as the Higgs companion derives; the standard $M_W=gv/2$ is the same formula with the effective charge $ϙ=g/2$, because the W couples to the doublet through $T_3=\pm1/2$. The factor of one-half is the isospin of the scalar, not of the W. This distinction is the crux of the third section.

### The Z Pole and the Effective Mixing Angle

The mixing angle is not directly measurable; it is extracted from asymmetries and rates at the Z resonance, and the extraction is scheme dependent in a way worth recording because it fixes what the empirical numbers mean. The combination that the couplings determine is
$$
a_f=T_{3f} ,
\qquad
v_f=T_{3f}-2Q_f\sin^2\theta_W ,
$$
the axial and vector couplings of the fermion $f$ to the Z; the measured left–right and forward–backward asymmetries, and the Z partial widths, determine the products $a_fv_f$, $v_f^2+a_f^2$ and hence an **effective** mixing angle at the Z pole,
$$
\sin^2\theta^{\rm eff}_{\rm lept}=0.23148\pm0.00016 ,
\qquad
\sin^2\theta_{\mathrm{msb},W}(M_Z)=0.23122\pm0.00004 ,
\qquad
\sin^2\theta_{\mathrm{OS}}=1-\frac{M_W^2}{M_Z^2}=0.22305 ,
$$
the effective angle being the asymmetry result, the second the $\overline{\mathrm{MS}}$ value, and the third the on-shell angle built from the measured masses. They are three different quantities, separated by amounts of the size of the known radiative corrections, and the corrections carry one into another; that the corrections close the gap is a nontrivial consistency check of the standard theory. The framework has nothing to add to this: the couplings $T_{3f}$ and $Q_f$ are the imported fermion data of the spin-$\tfrac12$ subcategory, and the scheme dependence is a property of the standard radiative corrections. The point of recording it is that the empirical mixing angle is an effective parameter, so the framework's imported $\theta_W$ should be understood in the same effective sense and not as a bare algebra parameter.

### The Currents and the Self-Couplings

The currents below are written with the action of the frame on the field and with the two values of the chirality subscript. The generator of the coordinate $x_\mu$ acts by
$$
\tilde{Ξ}_{\mathrm{sp}}\longmapsto i\,\tilde{Ξ}_{\mathrm{sp}}\,\vec e_\mu\,\vec e_{\nu(\mu)},
\qquad
\nu(t)=x,\quad \nu(\eta)=y ,
$$
and the Dirac adjoint is the pairing $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}i\vec e_x$, written with its right factor in position. The chirality of a field is the slot its basis operator occupies, and the subscript records the value: a field is $L$ or $R$, $L$ is the $-1$ eigenvalue of the basis operator $-iR_{\vec e_z}$ and $R$ the $+1$ eigenvalue, the basis operator being one example of the right slot, every field is a sum of one of each, and only the zero field is both. Left multiplication keeps the letter and a product takes the letter of its right factor, so
$$
\tilde{Ξ}_{\mathrm{sp},\mathrm L}=\tfrac12\big(\tilde{Ξ}_{\mathrm{sp}}+i\tilde{Ξ}_{\mathrm{sp}}\vec e_z\big),
\qquad
\tilde{Ξ}_{\mathrm{sp},\mathrm R}=\tfrac12\big(\tilde{Ξ}_{\mathrm{sp}}-i\tilde{Ξ}_{\mathrm{sp}}\vec e_z\big),
\qquad
i\vec e_\mu\,\tilde{Ξ}_{\mathrm{sp},\mathrm L}\,\vec e_{\nu(\mu)}\ \text{is of letter } R,
\qquad
i\vec e_\mu\,\tilde{Ξ}_{\mathrm{sp},\mathrm R}\,\vec e_{\nu(\mu)}\ \text{is of letter } L .
$$
A frame basis operator therefore carries each part of a field into the other, and the $L$ part of a frame basis operator applied to an $L$ field is zero. A term built from one field alone is consequently not chiral; the coupling of the W is chiral because it reads one part of one of the two fields of a doublet. The two letter statements were verified on the four frame basis operators as maps of the algebra.

The charged current interaction is
$$
\mathcal{L}_{\mathrm{cc}}=-\frac{g}{\sqrt{2}}\Big(\sum_\mu W^+_\mu J^{+}_\mu+\mathrm{h.c.}\Big),
\qquad
J^+_\mu=\sum_{\text{doublets}}\mathrm{Sc}\Big(\tilde{Ξ}_{\mathrm{sp},\mathrm u}^*\,i\,\big(i\vec e_\mu\,\tilde{Ξ}_{\mathrm{sp},\mathrm d,\mathrm L}\,\vec e_{\nu(\mu)}\big)\vec e_x\Big),
$$
with the sum running over the lepton and quark doublets with the appropriate quark mixing matrix, $\tilde{Ξ}_{\mathrm{sp},\mathrm u}$ and $\tilde{Ξ}_{\mathrm{sp},\mathrm d}$ the up and down members of a doublet, and $\tilde{Ξ}_{\mathrm{sp},\mathrm d,\mathrm L}$ the $L$ part of the down field. The selection is what makes the coupling chiral: it is applied to the down field, so that of the two parts of that field only the $L$ one reaches the W. The neutral current interaction is
$$
\mathcal{L}_{\mathrm{nc}}=-\frac{g}{\cos\theta_W}\sum_\mu Z_\mu J_{Z\mu} ,
\qquad
J_{Z\mu}=\sum_f\mathrm{Sc}\Big(f^{*}\,i\,\big(i\vec e_\mu\,(T_{3f}f_{\mathrm L}-Q_f\sin^2\theta_W\,f)\,\vec e_{\nu(\mu)}\big)\vec e_x\Big),
$$
where $T_{3f}$ is the weak isospin of the fermion and $Q_f$ its electric charge. The bracket is the Z-pole combination of the previous section written on the two parts, $\tfrac12(v_f+a_f)f_{\mathrm L}+\tfrac12(v_f-a_f)f_{\mathrm R}$ with $v_f$ and $a_f$ the vector and axial couplings, so the two sections use one set of couplings. The coupling of the photon is $eQ_f$, with $Q_f=T_{3f}+Y_f$. The non-abelian structure produces the gauge self-couplings, whose Lorentz structure is standard:
$$
\mathcal{L}_{3}=ig\cos\theta_W\Big[\big(W^+_{\mu\nu}W^-_\mu-W^-_{\mu\nu}W^+_\mu\big)Z_\nu+W^+_\mu W^-_\nu Z_{\mu\nu}\Big]
+ie\Big[\big(W^+_{\mu\nu}W^-_\mu-W^-_{\mu\nu}W^+_\mu\big)A_\nu+W^+_\mu W^-_\nu A_{\mu\nu}\Big],
$$
$$
W^\pm_{\mu\nu}=\frac{\partial W^\pm_\nu}{\partial R_\mu}-\frac{\partial W^\pm_\mu}{\partial R_\nu},
\qquad
Z_{\mu\nu}=\frac{\partial Z_\nu}{\partial R_\mu}-\frac{\partial Z_\mu}{\partial R_\nu},
\qquad
A_{\mu\nu}=\frac{\partial A_\nu}{\partial R_\mu}-\frac{\partial A_\mu}{\partial R_\nu},
$$
$$
\mathcal{L}_{4}=-\frac{g^2}{4}\Big[\big(\sum_{a,\mu}W^a_\mu W^a_\mu\big)^2-\sum_{a,b}\big(\sum_\mu W^a_\mu W^b_\mu\big)^2\Big],
$$
$$
=-\frac{g^2}{2}\Big[\big(\sum_\mu W^+_\mu W^-_\mu\big)^2-\big(\sum_\mu W^+_\mu W^+_\mu\big)\big(\sum_\nu W^-_\nu W^-_\nu\big)\Big]
-g^2\Big[\big(\sum_\mu W^+_\mu W^-_\mu\big)\big(\sum_\nu W^3_\nu W^3_\nu\big)-\big(\sum_\mu W^+_\mu W^3_\mu\big)\big(\sum_\nu W^-_\nu W^3_\nu\big)\Big],
$$
repeated $a,b$ summed; the second form splits the first into the four-charged-W piece and the piece that carries the neutral field. Both forms were checked against the direct expansion of $-\tfrac14\sum_{a,\mu,\nu}W^a_{\mu\nu}W^a_{\mu\nu}$ to machine precision. With $W^3_\mu=\cos\theta_W Z_\mu+\sin\theta_W A_\mu$ the second bracket gives the $WWZZ$ vertex with coefficient $-g^2\cos^2\theta_W$, the $WW\gamma\gamma$ vertex with $-g^2\sin^2\theta_W=-e^2$, and the $WWZ\gamma$ vertex with $-2g^2\sin\theta_W\cos\theta_W=-2eg\cos\theta_W$. Two features of the trilinear term are worth naming, because a compact writing of it loses one of them. The neutral field enters once through its field strength $Z_{\mu\nu}$, not only through the derivative $\partial Z$: the two are different tensors, and only the antisymmetric one reproduces the vertex that the field strength $W_{\mu\nu a}$ generates — with the bare derivative the identity fails. And the photon couples with $e=g\sin\theta_W$, the same structure constants reduced by the mixing, so the $WW\gamma$ vertex is the $Z$ vertex with $\cos\theta_W$ replaced by $\sin\theta_W$ and the neutral field by the photon. The vertices are of the same $f_{abc}$ type as the ones the framework's non-abelian structure supplies; this is the part of the electroweak sector that the algebra reaches without qualification.

## The Charged and Neutral Directions in the Algebra

### The Cartan Decomposition of $\mathrm{U}(2)$

The compact factor of the algebra is $\mathrm{U}(2)=\mathbb{R}(ie_t)\oplus\mathrm{SU}(2)$, of real dimension four, matching the four electroweak gauge fields; at the level of Lie algebras $\mathfrak{u}(2)=\mathfrak{su}(2)\oplus\mathfrak{u}(1)$ is the electroweak algebra, and the global quotient that separates $\mathrm{U}(2)$ from $\mathrm{SU}(2)\times\mathrm{U}(1)$ is invisible to the algebra, which is why the group is listed as imported. Its Cartan subalgebra is two-dimensional, spanned by the central $ie_t$ and the material $\vec e_z$ (or $i\vec e_z$); the two commuting generators correspond to the two neutral fields, $B_\mu$ and $W_{\mu 3}$, before mixing. The off-diagonal generators are the charged combinations
$$
\boxed{\;W^\pm\;\longleftrightarrow\; \vec e_x\pm i \vec e_y\in\mathbb{B}\;},
$$
which are complex combinations of the two real material generators. The adjoint action of the Cartan generator $\tilde S_{\Psi,\mathrm{adj},3}=\tfrac12\mathrm{ad}_{i\vec e_z}=\mathrm{ad}_{\,iT_3}$, with $iT_3=\tfrac12i\vec e_z$ the Hermitian partner of the material Cartan generator $T_3=\tfrac12\vec e_z$, is diagonal on them:
$$
\boxed{\;[i\vec e_z,\vec e_x\pm i\vec e_y]=\pm 2\,(\vec e_x\pm i\vec e_y),
\qquad
\tilde S_{\Psi,\mathrm{adj},3}(\vec e_x\pm i\vec e_y)=\pm (\vec e_x\pm i\vec e_y)\;},
$$
where the coefficients are the double-$i$ collapse and nothing else: $[i\vec e_z,\vec e_x]=i[\vec e_z,\vec e_x]=2i\vec e_y$ on one side, and $i^2[\vec e_z,\vec e_y]=-[\vec e_z,\vec e_y]=2\vec e_x$ on the other, since $[\vec e_z,\vec e_y]=-2\vec e_x$. The charged generators therefore carry the eigenvalues $\pm1$ of the adjoint $\tilde S_{\Psi,\mathrm{adj},3}$. This is the same computation the companion article *Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form* performs for the spin-one representation, and it identifies the W as the spin-one excitation of the material sector: the connection $\mathcal{A}_\mu$ is $\mathfrak{su}(2)$-valued, its two off-diagonal components are the charged W's, and its diagonal component is the neutral $W^3$.

### The W and Z as Proca Fields

A free W or Z of mass $M$ is the Proca field $\tilde A_{\Phi}\in\mathbb{B}_{\Phi}$ of the companion articles; its component vector is written $V_\mu$ here, so that $A_\mu$ stays the photon of the mixing,
$$
\mathcal{L}=-\tfrac14\sum_{\mu,\nu}F_{\mu\nu}F_{\mu\nu}-\tfrac12 M^2 \sum_\mu V_\mu V_\mu,
\qquad
F_{\mu\nu}=\frac{\partial V_\nu}{\partial R_\mu}-\frac{\partial V_\mu}{\partial R_\nu},
$$
$$
\tilde\nabla_\Phi\tilde F-M^2\tilde A_{\Phi}=0,
\qquad
\langle\tilde\nabla_\Phi,\tilde A_{\Phi}\rangle_{\natural}=0 ,
$$
the second line being the Lorenz condition, which follows from the equation and is not a gauge choice in the massive theory. Its canonical quantization yields three polarizations, two transverse and one longitudinal, with the transverse sum $\mathcal{P}$,
$$
\sum_{r=1}^{3}\varepsilon_{r\mu}\varepsilon_{r\nu}=\mathcal{P}_{\mu\nu},
\qquad
\mathcal{P}_{\mu\nu}=\delta_{\mu\nu}+\frac{p_\mu p_\nu}{M^2},
\qquad
\sum_\rho \mathcal{P}_{\mu\rho}\mathcal{P}_{\rho\nu}=\mathcal{P}_{\mu\nu},
\qquad
\sum_\nu \mathcal{P}_{\mu\nu}p_\nu=0 .
$$
The metric contraction $\sum_{\mu,\nu}\delta_{\mu\nu}\mathcal{P}_{\mu\nu}=3$ counts the polarizations, and the timelike sign $\sum_\mu p_\mu p_\mu=-M^2$ on shell, whose one minus is the square of the $i$ that $p_t$ carries, is what makes the sum reproduce itself, so that the three polarizations are complete.

In the framework the massive vector is an element of the material sector, $\tilde{A}_{\Phi}\in\mathbb{B}_{\Phi}$, whose massive wave equation is $(\Box-\mu^2)\tilde{A}_{\Phi}=0$ in the Lorenz gauge; the Proca companion writes it in that form. The W and Z are therefore carried by the same object as the photon — a material vector — with the mass term added; the difference between the photon and the Z is that the photon is the massless (self-dual) combination and the Z the massive one, and the difference between the Z and the W is the charge eigenvalue of the adjoint action.

### The Mixing as a Rotation of the Neutral Plane

The two commuting directions of $\mathrm{U}(2)$ are the central $ie_t$ and the Cartan material direction $\vec e_z$. Any two independent neutral combinations are a rotation of this plane,
$$
Z_\mu=\cos\theta_W\,W_{\mu 3}-\sin\theta_W\,B_\mu,
\qquad
A_\mu=\sin\theta_W\,W_{\mu 3}+\cos\theta_W\,B_\mu ,
$$
and the rotation angle is the Weinberg angle. The algebra contains the plane and therefore contains the rotation; what it does not contain is a *principle* that fixes the angle. The angle is fixed in the standard theory by the requirement that the photon be massless, that is by the mass matrix of the neutral sector, and the mass matrix is generated by the Higgs doublet. In the framework the rotation is available and the mechanism that determines it is imported, exactly as the mass is.

## Mass Generation: What the Framework Reaches

### The Standard Route and Its Ingredient

The standard masses $M_W=gv/2$, $M_Z=\sqrt{g^2+g_{\mathrm Y}^2}v/2$ come from the covariant kinetic term of a scalar doublet with $T_3=\pm1/2$, evaluated at its vacuum expectation value. The three ingredients are (i) a scalar field with a nonzero vacuum value, (ii) a scalar that transforms nontrivially under the non-abelian group, so that the kinetic term contains $g^2(T_3)^2|W|^2|\xi_{\mathrm{scl}}|^2$, and (iii) a potential that fixes the value. The framework supplies (i) and (iii) in the abelian case — the central scalar of the Higgs companion has a potential and a vacuum expectation value, and the companion derives the mass $M_A=\kappa v$ — but not (ii): a central scalar is a **singlet** of the compact factor, its adjoint action is zero, and its covariant kinetic term contains no $g^2|W|^2$ term. The non-abelian W's therefore receive no mass from the framework's central scalar. This is the precise content of the statement that the framework's scalar cannot break the non-abelian group.

### What an Adjoint Scalar Would Give

If the framework were to use a scalar in the adjoint of the compact factor — an element of $\mathrm{SU}(2)$ rather than of the centre — the covariant kinetic term would contain the adjoint action, whose Cartan eigenvalue on the charged directions is $\pm1$, so the W mass would be of order $gv$ rather than $gv/2$. The observed ratio $M_W=gv/2$ requires the eigenvalue $\pm1/2$, that is a scalar whose gauge index sits in the two-dimensional fundamental representation. The algebra does possess a carrier of that dimension — left multiplication preserves the letter and acts irreducibly on either of the two parts of an element, each of which has two components — but the same carrier serves the Lorentz action too, and the representation it carries there is a two-component one, not a scalar. The framework's Lorentz-scalar carriers are the algebra's own subspaces: the centre, on which the adjoint action vanishes, and the material and informational sectors, which carry the adjoint. None of them carries the fundamental of the compact factor while transforming trivially under the Lorentz group, so the framework supplies no gauge doublet that is also a Lorentz scalar; the companion articles *Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form* and *Chiral Fermions in the Biquaternion Framework* establish the two sides of this, that the algebra's native non-abelian action on the material sector has integer spin and that its central action is vector-like. Neither supplies the doublet.

### The Two Available Mechanisms and Their Limits

The framework therefore has exactly two ways to give a vector a mass, and neither reaches the charged W.

- **The abelian Higgs mechanism of the Higgs companion.** A central scalar with a potential and a vacuum value gives the central gauge field a mass $M_A=\kappa v$, and the would-be Goldstone mode is removed by the gauge transformation. This reaches only the abelian direction; applied to the neutral sector it can give mass to a combination of the central and Cartan directions, but it cannot give the charged W's a mass, and it cannot fix the mixing angle in the observed way.
- **The Stueckelberg mechanism.** A shift-symmetric central scalar paired with the abelian gauge field gives an invariant mass term with no potential and no vacuum value; this is the massive-vector mechanism that requires only the central scalar, and it is treated in the massive-vector subcategory. Like the abelian Higgs, it reaches the abelian direction and not the charged W's.

Both mechanisms are available for the *abelian* factor of the electroweak group; the mass of the W is imported, and with it the factor of one-half that is the isospin of the scalar. The framework reproduces the W's kinematics, its charge eigenvalues and its self-couplings, and it transcribes its mass; it does not generate it.

### The Longitudinal Mode and the Goldstone Equivalence

A massive vector has three polarizations, and the third — the longitudinal mode — is the one the mass term creates: at high energy its amplitude is the amplitude of the would-be Goldstone boson that the gauge transformation removed, the **Goldstone equivalence theorem**. In the standard theory the would-be Goldstone modes are the three components of the scalar doublet that the unbroken electromagnetic subgroup does not leave invariant, and the longitudinal W and Z are their high-energy avatars; this is why the scalar sector controls the longitudinal vector dynamics and why the theory would violate unitarity without it. In the framework the longitudinal mode of a Proca field is present as the propagating third polarization of the material vector, and the Proca companion's constraint analysis exhibits it: the Gauss law is deformed by the mass, the primary constraint is second class, and the physical Hilbert space carries three polarizations. What the framework does not supply is the scalar multiplet whose Goldstone modes the longitudinal W and Z are; the longitudinal mode is available as a mode of the massive field, but its high-energy identity with a Goldstone amplitude is a statement of the standard scalar sector and is imported. The Goldstone companion records the framework's treatment of the would-be Goldstone mode in the abelian case, where the central scalar supplies it.

## The Currents and the Vector-Like Obstruction

The charged current interaction is chiral: the W couples to $J^{+}_\mu$ of §*The Currents and the Self-Couplings*, which reads the down field on its $L$ part only, and the neutral current has the parity-violating combination $T_{3f}f_{\mathrm L}-Q_f\sin^2\theta_W\,f$. The framework's gauge action on the algebra is the adjoint action, which is real and preserves the sector: it acts on the material sector as a rotation, and it is a difference of a left multiplication and a right multiplication by the same Cartan unit, each of which keeps the letter, so it acts on the two parts of a field alike. The companion article *Chiral Fermions in the Biquaternion Framework* shows that a gauge group drawn from the centre acts as a scalar and is therefore vector-like, and that chirality requires a non-central action. The non-central actions the framework possesses are the adjoint action on the material sector and left multiplication on the algebra; the adjoint is real, and left multiplication keeps the letter, so it carries an $L$ part and an $R$ part the same way; neither produces the asymmetric assignment the W requires. Two possibilities are recorded in the companion and are not resolved here: a chiral action built on a module that is not the material sector, and a real structure that pairs the two chiralities. Neither is supplied by the algebra as it stands. The result for the vector bosons is that the framework transcribes the charged and neutral currents but does not derive their chirality.

The electromagnetic current is a different case, and it is reached. The unbroken generator of the electroweak group is $Ϙ=T_3+Y$, its gauge field is the photon, and the coupling is $e=g\sin\theta_W=g_{\mathrm Y}\cos\theta_W$. The abelian gauge principle of the companion articles is the central phase, and the photon is the massless central-material combination. The framework reaches the photon exactly; it reaches the Z as a massive neutral material vector with a mixing angle that is imported; and it reaches the W as a massive charged adjoint excitation with a mass and a chiral coupling that are imported.

## The Gauge Self-Couplings

The trilinear and quartic vertices of the electroweak vector bosons come from the non-abelian curvature, and here the framework's structure is sufficient in form. The previous part writes the two vertices in their electroweak form, with the charged and neutral combinations already made; this section writes them in the general non-abelian form from which that specialization follows, so that the structure constants that appear are visibly the ones of the compact factor. Writing the curvature as
$$
F_{\mu\nu}=\frac{\partial\mathcal{A}_\nu}{\partial R_\mu}-\frac{\partial\mathcal{A}_\mu}{\partial R_\nu}+i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu],
$$
the cubic term in the action is linear in the commutator and the quartic term quadratic, so that
$$
\mathcal{L}_{3}\sim\kappa\sum_{a,b,c}f_{abc}\Big(\frac{\partial\mathcal{A}_{\nu a}}{\partial R_\mu}-\frac{\partial\mathcal{A}_{\mu a}}{\partial R_\nu}\Big)\mathcal{A}_{\mu b}\mathcal{A}_{\nu c},
\qquad
\mathcal{L}_{4}\sim\kappa^2\sum_{a,b,c,d}f_{abe}f_{cde}\mathcal{A}_{\mu a}\mathcal{A}_{\nu b}\mathcal{A}_{\mu c}\mathcal{A}_{\nu d},
$$
with the repeated $\mu,\nu$ summed, which are the three- and four-gauge-boson vertices with the structure constants $f_{abc}=2\varepsilon_{abc}$ of the compact factor in the unnormalized basis $e_a$. The derivative pair in the cubic term is the field strength of the curvature, and it is written antisymmetrized for a reason visible only in the electroweak form: there the neutral field enters through its field strength and not through a bare derivative, and only the antisymmetrized pair reproduces the vertex that the curvature generates. In this general form the antisymmetrization costs nothing, because $f_{abc}$ is antisymmetric in $b,c$ and the two orderings give the same vertex. For the charged and neutral combinations these become the $WWZ$ and $WW\gamma$ vertices, with the couplings $g\cos\theta_W$ and $e$ respectively, and the quartic $WWZZ$, $WW\gamma\gamma$, $WWZ\gamma$ vertices. The algebra supplies the Lorentz and Lie-algebraic structure of these vertices; the identification of the neutral combination with the Z and the photon, and the numerical values of the couplings, are imported, as is the mixing angle. Two points are specific to the framework.

- **The vertices are those of the adjoint action.** The structure constants $f_{abc}$ of the compact factor are the ones read from the quaternion commutator, and the four-point vertex is built from their products. In the algebra the cubic and quartic interactions are the expansion of the commutator, so the gauge self-couplings are a direct consequence of the non-commutativity of the generators in the material basis $e_a$.
- **The abelian factor does not self-couple.** The central direction has vanishing structure constants, so the abelian hypercharge field has no self-coupling; the $BBB$ and $BBBB$ vertices are absent. This is the algebra's statement of the abelian nature of the hypercharge factor.

## What the Algebra Supplies and What It Imports

**Supplied by the algebra, and recomputed here.** The carrier of the massive vector field, as an element of the material sector $\mathbb{B}_{\Phi}$; the three polarizations and the Proca equation, from the Proca companions; the charge eigenvalues of the charged W, as the eigenvalues $\pm1$ of the adjoint action of the Cartan generator $\tilde S_{\Psi,\mathrm{adj},3}=\tfrac12\mathrm{ad}_{i\vec e_z}$ on $\vec e_x\pm i\vec e_y$, verified in the defining representation; the neutral plane of $\mathrm{U}(2)$ and the mixing rotation within it; the non-abelian self-couplings, as the expansion of the quaternion commutator with $f_{abc}=2\varepsilon_{abc}$; and the absence of self-coupling for the central factor.

**Imported, and left visible.** The group $SU(2)_L\times \mathrm{U}(1)_Y$ and its hypercharge assignments; the Weinberg angle and the mixing; the Higgs doublet, its potential and its vacuum value; the mass relations $M_W=gv/2$, $M_Z=M_W/\cos\theta_W$ and $\rho=1$; the chiral charged and neutral currents and the fermion content; the electromagnetic coupling $e=g\sin\theta_W=g_{\mathrm Y}\cos\theta_W$; the measured masses and mixing angle; and the radiative corrections. All of these are transcribed from the standard electroweak theory and cited as standard.

**Not supplied.** The mass of the W and the Z is not generated by the algebra's central scalar; the doublet that the standard mechanism requires would have to be a Lorentz scalar carrying the fundamental of the compact factor, and the algebra's Lorentz-scalar carriers hold only the singlet and the adjoint; the chiral coupling of the W is not produced by any of the framework's gauge actions; the number of generations and the quark mixing matrix belong to the spin-$\tfrac12$ subcategory. As everywhere in the series, no empirical content is added.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}_{\mathrm{sp}}=a\tilde{Ξ}_{\mathrm{sp}}$ and $R_b\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}} b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},\quad \gamma_1=iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\quad \gamma_2=iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\quad \gamma_3=iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\quad \gamma_5=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x},\quad \gamma_1=iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\quad \gamma_2=iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\quad \gamma_3=iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\quad \gamma_5=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z} .
$$

Each of the four generator basis operators is one factor of $i$ times a plain two-sided basis operator,
$$
i\,\gamma_\mu=-L_{\mathrm{pau},e_\mu}R_{\mathrm{pau},\vec e_{\nu(\mu)}} ,
$$

In the axis-free display:

$$
i\,\gamma_\mu=-L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},\vec e_{\nu(\mu)}} ,
$$

so that a product of two frame basis operators carries $i^2=-1$ and nothing further.

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame basis operator of the chirality $\Gamma$; the central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the basis operators span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the body cites.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$,
$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_\eta)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
\qquad \varepsilon=(1,-1,-1,-1),$$
$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d-\varepsilon_a\delta_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$

**The four contraction sums.** The bodies of the corpus use four contraction sums of frame basis operators. With every index contracted through the sign vector $\varepsilon$,
$$
\sum_\mu\varepsilon_\mu\,\gamma_\mu\gamma_\mu=4I_4,
\qquad
\sum_\mu\varepsilon_\mu\,\gamma_\mu\gamma_\alpha\gamma_\mu=-2\gamma_\alpha,
$$
$$
\sum_\mu\varepsilon_\mu\,\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\mu=4\varepsilon_\alpha\delta_{\alpha\beta}I_4,
\qquad
\sum_\mu\varepsilon_\mu\,\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\gamma\gamma_\mu=+2\gamma_\alpha\gamma_\beta\gamma_\gamma .
$$
They are fixed by the weight, because a basis operator's square is: with $i^2=-1$, $\left(iL_aR_b\right)^2=-L_{a^2}R_{b^2}$, and each of $a^2$ and $b^2$ is $\pm e_t$. With the summed index raised, $\gamma^\mu=-\varepsilon_\mu\gamma_\mu$, they read $-4I_4$, $+2\gamma_\alpha$, $-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $-2\gamma_\alpha\gamma_\beta\gamma_\gamma$. With every index low only the first keeps a closed form, the unweighted sum of the four squares being $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$, one $+1$ and three $-1$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{\mathrm{axf},e_\mu}=C_{\Pi}L_{\mathrm{pau},e_\mu}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a basis operator named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The W and Z are the massive spin-one fields of the weak interaction, with $W^\pm$ of charge $\pm1$ and the neutral Z mixing with the photon through the Weinberg angle. The framework reaches their kinematics: a massive vector is a material-sector element subject to the Proca equation $(\Box-\mu^2)\tilde{A}_{\Phi}=0$ with three polarizations; the charged W's are the off-diagonal components $\vec e_x\pm i\vec e_y$ of the compact factor, on which the adjoint action of $\tilde S_{\Psi,\mathrm{adj},3}=\tfrac12\mathrm{ad}_{i\vec e_z}$ has eigenvalues $\pm1$; the neutral plane is the two-dimensional Cartan subalgebra of $\mathrm{U}(2)$, spanned by the central $ie_t$ and the material $\vec e_z$, and the Z–photon mixing is a rotation within it; and the trilinear and quartic self-couplings are the expansion of the quaternion commutator with $f_{abc}=2\varepsilon_{abc}$, which also shows that the central factor does not self-couple.

The framework reaches the masses only through the abelian sector. The mass relations
$$
M_W=\frac{gv}{2},
\qquad
M_Z=\frac{\sqrt{g^2+g_{\mathrm Y}^2}\,v}{2}=\frac{M_W}{\cos\theta_W},
\qquad
\rho=\frac{M_W^2}{M_Z^2\cos^2\theta_W}=1,
\qquad
e=g\sin\theta_W=g_{\mathrm Y}\cos\theta_W ,
$$
all hold in the standard theory and were verified as identities with the standard inputs ($v=246.22$ GeV from $G_F$); the measured masses, $M_W=80.377$ GeV and $M_Z=91.1876$ GeV, differ from the tree-level expressions by the radiative correction. The framework's abelian Higgs mechanism gives a mass $M_A=\kappa v$ to the central direction, and the Stueckelberg mechanism gives an invariant mass to the abelian direction without a potential; neither reaches the charged W's, because the framework's scalar is central and its covariant kinetic term carries no adjoint action on the charged directions. An adjoint scalar would give a mass of order $gv$, not $gv/2$; the observed factor of one-half requires the doublet, that is a Lorentz scalar in the fundamental of the compact factor, and the algebra's Lorentz-scalar carriers hold only the singlet and the adjoint, so the doublet is not available.

The charged current is chiral, $J^{+}_\mu$ of §*The Currents and the Self-Couplings*, which reads the down field on its $L$ part only, and the framework's gauge actions — the central phase, the adjoint action on the material sector, and left multiplication — are vector-like, so none of them supplies the asymmetric assignment; the companion article on chiral fermions establishes the obstruction for a central action and records the non-central case as the open question. The W's mass and its chiral coupling are therefore imported, while its carrier, its charge, its polarizations and its self-couplings are supplied.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | The coefficient basis of the algebra; $e_t$ is its unit |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\mathbb{B}_{\Phi},\mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{B}_{C}$ | The centre of the algebra; the abelian factor |
| $\tilde{Ξ}_{\mathrm{sp}}\mapsto i\tilde{Ξ}_{\mathrm{sp}}\vec e_x$; $\tilde{Ξ}_{\mathrm{sp}}\mapsto i\tilde{Ξ}_{\mathrm{sp}}\vec e_\mu\vec e_{\nu(\mu)}$ with $\nu(t)=x$, $\nu(\eta)=y$; $\mathsf{V}_{\mathrm{vol}}=-iR_{\vec e_z}$ | The frame basis operators, written as actions on a field: the time basis operator, a generator basis operator, and the fifth basis operator whose two values are the chirality |
| $\tilde{Ξ}_{\mathrm{sp},\mathrm L}=\tfrac12(\tilde{Ξ}_{\mathrm{sp}}+i\tilde{Ξ}_{\mathrm{sp}}\vec e_z)$, $\tilde{Ξ}_{\mathrm{sp},\mathrm R}=\tfrac12(\tilde{Ξ}_{\mathrm{sp}}-i\tilde{Ξ}_{\mathrm{sp}}\vec e_z)$ | The two values of the chirality subscript: $L$ is the $-1$ value of $\mathsf{V}_{\mathrm{vol}}$, $R$ the $+1$ value |
| $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}i\vec e_x$, and $\mathrm{Sc}(\tilde{Ξ}_{\mathrm{sp}}^*iX\vec e_x)$ for its pairing with an element $X$ | Dirac adjoint; a pairing of two fields, with its right factor written in position |
| $\mathrm{U}(2)=\mathbb{R}(ie_t)\oplus\mathrm{SU}(2)$ | Compact factor, real dimension four |
| $\mathrm{SU}(2)=\mathrm{span}_\mathbb{R}\{\vec e_x,\vec e_y,\vec e_z\}$ | Compact gauge algebra |
| $T_a=\tfrac12e_a$, $[T_a,T_b]=\sum_c\varepsilon_{abc}T_c$ | The generators of the compact factor and their commutator |
| $f_{abc}=2\varepsilon_{abc}$ | Structure constants of the compact factor, in the unnormalized basis $e_a$ ($f_{abc}=\varepsilon_{abc}$ in the normalized basis $T_a=\tfrac12e_a$) |
| $\kappa=\frac{ϙ}{\hbar}$ | Framework gauge coupling |
| $\tilde S_{\Psi,\mathrm{adj},3}=\tfrac12\mathrm{ad}_{i\vec e_z}=\mathrm{ad}_{\,iT_3}$, $iT_3=\tfrac12i\vec e_z$ | Cartan generator of the adjoint action |
| $W^\pm\leftrightarrow \vec e_x\pm i\vec e_y$, $\tilde S_{\Psi,\mathrm{adj},3} W^\pm=\pm W^\pm$ | Charged directions and their eigenvalues |
| $Z_\mu=\cos\theta_W W_{\mu 3}-\sin\theta_W B_\mu$, $A_\mu=\sin\theta_W W_{\mu 3}+\cos\theta_W B_\mu$ | Neutral mixing |
| $\tan\theta_W=g_{\mathrm Y}/g$ | Weinberg angle |
| $M_W=gv/2$, $M_Z=M_W/\cos\theta_W$, $M_\gamma=0$ | Tree-level masses |
| $\rho=M_W^2/(M_Z^2\cos^2\theta_W)=1$ | Tree-level relation for a doublet |
| $e=g\sin\theta_W=g_{\mathrm Y}\cos\theta_W$ | Electromagnetic coupling |
| $v=( \sqrt{2}G_F)^{-1/2}=246.22$ GeV | Electroweak scale |
| $M_A=\kappa v=\frac{ϙ\,v}{\hbar}$ | Framework abelian mass from the central scalar |
| $J^{+}_\mu=\sum_{\text{doublets}}\mathrm{Sc}\big(\tilde{Ξ}_{\mathrm{sp},\mathrm u}^*\,i\,(i\vec e_\mu\tilde{Ξ}_{\mathrm{sp},\mathrm d,\mathrm L}\vec e_{\nu(\mu)})\vec e_x\big)$ | Charged current (chiral) |
| $J_{Z\mu}=\sum_f\mathrm{Sc}\big(f^{*}\,i\,(i\vec e_\mu(T_{3f}f_{\mathrm L}-Q_f\sin^2\theta_Wf)\vec e_{\nu(\mu)})\vec e_x\big)$ | Neutral current |
| $\mathcal{L}_3\sim\kappa\sum_{a,b,c}f_{abc}(\partial\mathcal{A}_{\nu a}/\partial R_\mu-\partial\mathcal{A}_{\mu a}/\partial R_\nu)\mathcal{A}_{\mu b}\mathcal{A}_{\nu c}$, $\mathcal{L}_4\sim\kappa^2\sum_{a,b,c,d}f_{abe}f_{cde}\mathcal{A}_{\mu a}\mathcal{A}_{\nu b}\mathcal{A}_{\mu c}\mathcal{A}_{\nu d}$ | Trilinear and quartic self-couplings, derivative pair antisymmetrized |
| $-\tfrac14\sum_{\mu,\nu}F_{\mu\nu}F_{\mu\nu}-\tfrac12M^2\sum_\mu V_\mu V_\mu$ | Proca Lagrangian of a massive vector $V$; $\langle\tilde\nabla_\Phi,\tilde A_{\Phi}\rangle_{\natural}=0$ |
| $\sum_r\varepsilon_{r\mu}\varepsilon_{r\nu}=\mathcal{P}_{\mu\nu}=\delta_{\mu\nu}+p_\mu p_\nu/M^2$ | Polarization completeness, $\mathcal{P}$ the transverse sum |
| $\delta_{\mu\nu}$ | The unit metric of *Frame and Metric Conventions*, $(1,1,1,1)$ on the four $Q_\mu$, the one metric the displays use |
| $W^\pm_{\mu\nu}$, $Z_{\mu\nu}$, $A_{\mu\nu}$ | Field strengths of the charged, neutral massive and electromagnetic fields |
| $a,b,c$; $\mu,\nu$ | Internal isospin and spacetime indices, written low; every contraction over them is an explicit sum |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- S. L. Glashow, "Partial-symmetries of weak interactions," *Nuclear Physics* **22** (1961) 579–588, for the $SU(2)\times \mathrm{U}(1)$ gauge structure and the neutral current.
- S. Weinberg, "A model of leptons," *Physical Review Letters* **19** (1967) 1264–1266, for the electroweak Lagrangian, the mixing and the mass relations.
- A. Salam, "Weak and electromagnetic interactions," in *Elementary Particle Theory*, ed. N. Svartholm (Almqvist and Wiksell, 1968), for the unified electroweak construction.
- S. Weinberg, *The Quantum Theory of Fields, Vol. II: Modern Applications* (Cambridge, 1996), for the electroweak currents, the gauge self-couplings and the radiative corrections.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the Higgs mechanism, the W and Z masses, the currents and the vertices.
- T. W. B. Kibble, "Symmetry breaking in non-Abelian gauge theories," *Physical Review* **155** (1967) 1554–1561, for the non-abelian Higgs mechanism and the would-be Goldstone modes.
- P. W. Higgs, "Broken symmetries and the masses of gauge bosons," *Physical Review Letters* **13** (1964) 508–509, for the mass generation mechanism.
- G. 't Hooft, "Renormalizable Lagrangians for massive Yang–Mills fields," *Nuclear Physics B* **35** (1971) 167–188, for the renormalizability of the massive non-abelian theory.
- Particle Data Group, R. L. Workman *et al.*, "Review of Particle Physics," *Progress of Theoretical and Experimental Physics* **2022** (2022) 083C01, for the measured masses, the mixing angle and the electroweak precision parameters.
- W. J. Marciano and A. Sirlin, "Precise $SU(2)\times \mathrm{U}(1)$ parameters and the $Z$ mass," *Physical Review D* **22** (1980) 2695–2700, for the relation between $G_F$, $v$ and the W mass and for the radiative correction $\Delta r$.
