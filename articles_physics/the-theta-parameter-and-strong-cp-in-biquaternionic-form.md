# __The Theta Parameter and Strong CP in Biquaternionic Form__

## Introduction

*The Semiclassical Expansion and the Instanton Gas in Biquaternionic Form* showed that the sum over topological sectors forces a dependence on an angle, and *Electric–Magnetic Duality and the Modular Group in Biquaternionic Form* showed that the shift of that angle by $2\pi$ is one generator of the duality group. This article takes the angle seriously as a **parameter of the theory** and follows its consequences: the theta term in the action, its periodicity, and the strong CP problem that its non-observation creates.

The framework's contribution to this subject is unusually direct, and it rests on a result established earlier in the series. In the abelian sector the topological density is not a foreign object: it is proportional to the framework's second invariant,

$$
\tfrac14\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}
=\tfrac12\,F_{\mu\nu}\star F^{\mu\nu}
=\frac{2i}{c}\,I_2 \quad(\text{Lorentzian}),
\qquad
I_2=\vec E\cdot\vec B ,
$$

as *Instantons and Solitons in Biquaternionic Form* recomputed from the component conventions of *The Field-Strength Biquaternion and Its Invariants*. The coefficient is fixed by the identity $\tfrac14\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}=\tfrac12 F_{\mu\nu}\star F^{\mu\nu}$, so that the quarter-density carries half the coefficient of $F_{\mu\nu}{F^{\mathrm{dual}}}^{\mu\nu}=\frac{4i}{c}I_2$ used below; the two are not to be "aligned". The theta term of the Maxwell sector is therefore proportional to the integral of one of the framework's own invariants, and it is specifically the **pseudoscalar** invariant: $I_1=\vec E^2-c^2\vec B^2$ is parity-even and $I_2$ is parity-odd. The CP-odd character of the theta term, which is the source of the strong CP problem, is thus visible in the algebra as the parity of the second invariant.

Two things follow, and the article states them separately. The algebra **supplies** the theta term's density and its discrete periodicity; it **does not supply** the value of $\theta$, because $\theta$ is a parameter labelling the vacuum and not an output of a complexified classical algebra. The strong CP problem is the statement that the observed near-vanishing of the physical theta parameter is not explained by the framework — or by the Standard Model without additional structure. This is reported as the boundary of what the algebra can address.

$$
Ϙ=\frac{1}{8\pi^2}\int\mathrm{Tr}\bigl(F\wedge F\bigr)\in\mathbb Z ,
\qquad
S_\theta=\frac{\theta}{32\pi^2}\int F_{\mu\nu}{F^{\mathrm{dual}}}^{\mu\nu} ,
\qquad
{F^{\mathrm{dual}}}^{\mu\nu}=\tfrac12\epsilon^{\mu\nu\rho\sigma}F_{\rho\sigma} ,
$$

with all indices summed in the $ict'$ convention as in the companion gauge articles. Charges are in units $\hbar=c=1$ where a quantisation statement is made. The trace $\mathrm{Tr}$ is the matrix trace on the gauge factor, distinguished from the informational trace formula.

- Companion article *The Field-Strength Biquaternion and Its Invariants*, for the invariant $I_2=\vec E\cdot\vec B$.
- Companion article *The Semiclassical Expansion and the Instanton Gas in Biquaternionic Form*, for the theta vacuum and its periodicity.
- Companion article *Electric–Magnetic Duality and the Modular Group in Biquaternionic Form*, for the modular action on the charges.

## The Theta Term and Its Density

The theta term of a non-abelian gauge theory is

$$
\boxed{\;S_\theta=\frac{\theta}{32\pi^2}\int d^4x\,F^a_{\mu\nu}{F^{\mathrm{dual}}}^{a\,\mu\nu}
=\frac{\theta}{8\pi^2}\int\mathrm{Tr}\bigl(F\wedge F\bigr)\;},
$$

so that $S_\theta=\theta\,Ϙ$ with the charge normalisation used here, since $\int F^a{F^{\mathrm{dual}}}^a=4\int\mathrm{Tr}(F\wedge F)=32\pi^2Ϙ$. It is a total derivative,

$$
F^a_{\mu\nu}{F^{\mathrm{dual}}}^{a\,\mu\nu}=\langle\tilde\nabla,\tilde J_{\mathrm{CS}}\rangle_{\natural} ,
\qquad
J_{\mathrm{CS}}^\mu=\epsilon^{\mu\nu\rho\sigma}\Bigl(A^a_\nu F^a_{\rho\sigma}
-\tfrac{g}{3}\,\epsilon^{abc}A^a_\nu A^b_\rho A^c_\sigma\Bigr),
$$

the standard non-abelian Chern–Simons current, whose abelian part is the primitive $J_{\mathrm{CS}}^\mu=\epsilon^{\mu\nu\rho\sigma}A_\nu F_{\rho\sigma}$ of *Instantons and Solitons in Biquaternionic Form* and whose form identity $F\wedge F=d\Omega_{\mathrm{CS}}$ is that article's. Two consequences of the total-derivative property are stated there and are used here: the integral depends only on the boundary data, hence on the instanton number, and the local equations of motion are unaffected by the theta term, so its effects are topological and quantum-mechanical rather than classical.

**The abelian density is the framework's invariant.** In the Maxwell sector the density collapses to the second invariant,

$$
\boxed{\;F_{\mu\nu}{F^{\mathrm{dual}}}^{\mu\nu}=\frac{4i}{c}I_2\ \ (\text{Lorentzian}),
\qquad
F_{\mu\nu}{F^{\mathrm{dual}}}^{\mu\nu}=4I_2\ \ (\text{Euclidean}),
\qquad
I_2=\vec E\cdot\vec B\;},
$$

so the theta term of the abelian theory is

$$
S_\theta^{\text{ab}}=\frac{\theta}{32\pi^2}\int d^4x\,\frac{4i}{c}I_2
=\frac{i\theta}{8\pi^2 c}\int d^4x\,I_2 .
$$

The theta term is thus the integral of the framework's own parity-odd invariant, with the factor $i$ that the $ict'$ convention attaches to the pseudoscalar. This is the genuine affirmative content of the article: in the abelian sector the CP-odd term is not an object the framework lacks; it is $I_2$, already present in *The Field-Strength Biquaternion and Its Invariants*.

**Parity.** The transformation $I_2\to-I_2$ under parity, established with the other invariant properties of the field strength, is what makes the theta term a source of CP violation. A term linear in a parity-odd density, with a real coefficient $\theta$, is not invariant under parity unless $\theta$ takes the special values $0$ or $\pi$ (mod $2\pi$); the theory therefore violates $P$ and $T$, and by CPT, $CP$, for generic $\theta$. The statement is purely algebraic in the abelian sector: the framework has one parity-even and one parity-odd derivative-free invariant, and the theta term is the integral of the odd one.

## Periodicity and the Theta Vacuum

The theta dependence enters the partition function through the instanton sum of *The Semiclassical Expansion and the Instanton Gas in Biquaternionic Form*,

$$
Z(\theta)=\sum_{Ϙ\in\mathbb Z}\exp(iϘ\theta)Z_Ϙ ,
$$

and the integrality of the topological charge $Ϙ$ makes the partition function periodic,

$$
Z(\theta+2\pi)=\sum_Ϙ \exp(iϘ(\theta+2\pi))Z_Ϙ=\sum_Ϙ \exp(iϘ\theta)Z_Ϙ=Z(\theta),
$$

which was verified to machine precision on an explicit finite instanton sum in that article. The periodicity has two interpretations. Physically, $\theta$ and $\theta+2\pi$ label the same vacuum, so the angle is defined modulo $2\pi$ and the inequivalent vacua lie on a circle. Algebraically, the periodicity is the statement that the $T$ generator of the modular group, $T:\theta\to\theta+2\pi$, is a symmetry; it is the generator that *Electric–Magnetic Duality and the Modular Group in Biquaternionic Form* identified as the one requiring the integral topological charge. The periodicity is therefore not a property of the algebra but of the sum over the algebra's instanton sectors: it comes from $Ϙ\in\mathbb Z$, which comes from $\pi_3(SU(2))=\mathbb Z$ and hence from the Hopf total space.

The small-$\theta$ dependence of the vacuum energy is the same as in the semiclassical article,

$$
\mathcal E(\theta)=\mathcal E_0-2K\cos\theta\,\exp(-8\pi^2/g^2)+\cdots ,
$$

so the vacuum is CP-conserving at $\theta=0$ and $\theta=\pi$, and CP-violating elsewhere. The special value $\theta=\pi$ is the boundary between the two, and it is a genuine CP-conserving point because $\exp(iϘ\pi)=(-1)^Ϙ$ is real.

## Strong CP and the Value of Theta

The strong CP problem is the following. The theta term of quantum chromodynamics is not forbidden by any symmetry of the Standard Model, so its coefficient is expected to be of order unity; but the theta term violates CP, and CP violation in the strong sector is bounded by the electric dipole moment of the neutron. The physical, renormalisation-invariant parameter is

$$
\boxed{\;\bar\theta=\theta+\arg\det M_q\;},
$$

the sum of the gauge theta angle and the phase of the quark mass matrix (a chiral rotation of the quark fields shifts both, keeping $\bar\theta$ invariant), and the experimental bound on the neutron electric dipole moment requires

$$
|\bar\theta|\lesssim 10^{-10} .
$$

The problem is not that $\bar\theta$ is nonzero but that it is unnaturally small: the framework, like the Standard Model without additional structure, contains no reason for it to vanish. The standard dynamical solution is the Peccei–Quinn mechanism, in which $\bar\theta$ is promoted to a field whose potential is minimised at zero; the pseudo-Goldstone boson of that mechanism is the axion, which belongs to the spin-zero programme of the corpus and is not developed here.

**What the framework does and does not say.** The framework supplies the theta term's density, its parity-odd character as the invariant $I_2$, its periodicity and its role in the vacuum. It does not supply the value of $\theta$, because $\theta$ is not an element of the algebra: it is a coefficient in the action, and the algebra is a complexified classical structure with no action principle of its own. The strong CP problem is therefore a question the framework *poses* in its own language — why is the coefficient of the parity-odd invariant $I_2$ so small? — without answering it. Any answer must come from the dynamics, and in this corpus the dynamics of a scalar that could relax the coefficient is the axion programme, which is outside this subcategory. The honest statement is that the algebra's contribution is the identification of the CP-odd term with a known invariant, and that the resolution of strong CP is imported from beyond the algebra.

## The Chiral Rotation and the Invariance of the Physical Parameter

The reason $\bar\theta$ and not $\theta$ is the physical parameter is the anomaly. Consider a common axial rotation of the quark fields,

$$
\psi\;\longmapsto\;\exp(i\alpha\gamma_5)\,\psi ,
\qquad
\psi_L\mapsto \exp(-i\alpha)\psi_L ,
\qquad
\psi_R\mapsto \exp(+i\alpha)\psi_R ,
$$

under which the mass matrix in the fermion bilinear $\bar\psi_L M_q\psi_R$ transforms as

$$
M_q\;\longmapsto\;\exp(2i\alpha)M_q ,
\qquad
\arg\det M_q\;\longmapsto\;\arg\det M_q+2N_f\alpha ,
$$

for $N_f$ flavours. The classical action is invariant under this rotation for massless quarks, but the fermionic measure is not: the Jacobian of the rotation is non-trivial, and the anomaly shifts the theta angle by the compensating amount,

$$
\theta\;\longmapsto\;\theta-2N_f\alpha .
$$

The two shifts are opposite, and their sum is invariant:

$$
\bar\theta=\theta+\arg\det M_q
\;\longmapsto\;\bigl(\theta-2N_f\alpha\bigr)+\bigl(\arg\det M_q+2N_f\alpha\bigr)=\bar\theta .
$$

This is why $\bar\theta$ is the renormalisation-invariant physical parameter, and why a theory with $\theta=0$ and complex masses is equivalent to one with $\theta\ne0$ and real masses: the rotation moves the phase between the two terms without changing the physics. The invariance is the standard anomaly argument; the measure's non-invariance belongs to the spin-half programme of the corpus, where the anomalous divergence and the Jacobian are computed, and it is not re-derived here.

**What the framework contributes.** The axial rotation is generated by $\gamma_5$, whose biquaternionic realisation is the chirality grading that separates the two minimal left ideals of $\mathbb B\cong M_2(\mathbb C)$; the rotation acts on the two ideals with opposite phases, and the mass term is the chirality-off-diagonal coupling between them, as *The Dirac Equation in Biquaternionic Form* records. The shift of $\theta$ is therefore a rotation of the two chiral ideals against each other, and the invariance of $\bar\theta$ is the statement that the physics depends only on the product of the theta phase and the mass-matrix phase. The algebra makes the structure of the rotation visible — the axial generator, the off-diagonal mass, the two ideals — while the anomaly that makes the rotation non-trivial for the measure is imported from the quantum theory.

## Summary

The theta term $S_\theta=\frac{\theta}{32\pi^2}\int F_{\mu\nu}{F^{\mathrm{dual}}}^{\mu\nu}$ is a total derivative, hence dependent only on the instanton number, and in the abelian sector its density is proportional to the framework's parity-odd invariant $I_2=\vec E\cdot\vec B$:

$$
F_{\mu\nu}{F^{\mathrm{dual}}}^{\mu\nu}=\frac{4i}{c}\,I_2 \quad(\text{Lorentzian}),
\qquad
F_{\mu\nu}{F^{\mathrm{dual}}}^{\mu\nu}=4\,I_2 \quad(\text{Euclidean}).
$$

Because it is the integral of a parity-odd density, the theta term violates $P$ and $T$ unless $\theta=0$ or $\pi$. The theta dependence enters through the instanton sum $Z(\theta)=\sum_Ϙ\exp(iϘ\theta)Z_Ϙ$ and is periodic with period $2\pi$, verified to machine precision; the periodicity is the $T$ generator of the modular group and originates in the integrality of the topological charge.

The physical theta parameter is $\bar\theta=\theta+\arg\det M_q$, and the neutron electric dipole moment bounds it by $|\bar\theta|\lesssim10^{-10}$, which is the strong CP problem: the framework, like the Standard Model without additional structure, gives no reason for the near-vanishing. The framework supplies the CP-odd density as the invariant $I_2$ and supplies the periodicity and the vacuum structure, but it does not supply the value of $\theta$, which is a coefficient in the action and not an element of the algebra; the resolution is imported.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb B=\mathbb C\otimes_{\mathbb R}\mathbb H$ | Biquaternion algebra |
| $F^{\mathrm{dual}}=i\sqrt{\epsilon}\vec E-\sqrt{\mu}\vec H$ | Field-strength biquaternion |
| $F^{\mathrm{dual}}_\star=-iF^{\mathrm{dual}}$ | Dual field-strength biquaternion |
| $I_1=\vec E^2-c^2\vec B^2$ | First invariant (parity-even, scalar) |
| $I_2=\vec E\cdot\vec B$ | Second invariant (parity-odd, pseudoscalar); theta density |
| $\theta$ | Theta angle; coefficient of the topological term |
| $S_\theta=\frac{\theta}{32\pi^2}\int FF^{\mathrm{dual}}$ | Theta term of the action |
| ${F^{\mathrm{dual}}}^{\mu\nu}=\frac12\epsilon^{\mu\nu\rho\sigma}F_{\rho\sigma}$ | Hodge dual field strength |
| $Ϙ=\frac{1}{8\pi^2}\int\mathrm{Tr}(F\wedge F)$ | Topological charge, $Ϙ\in\mathbb Z$ |
| $J_{\mathrm{CS}}^\mu$ | Chern–Simons current, $FF^{\mathrm{dual}}=\langle\tilde\nabla,\tilde J_{\mathrm{CS}}\rangle_{\natural}$ |
| $Z(\theta)=\sum_Ϙ \exp(iϘ\theta)Z_Ϙ$ | Theta-dependent partition function, period $2\pi$ |
| $\bar\theta=\theta+\arg\det M_q$ | Physical CP-violating parameter |
| $M_q$ | Quark mass matrix (imported) |

## Further Reading

- Gerard 't Hooft, "Symmetry breaking through Bell–Jackiw anomalies", *Physical Review Letters* 37 (1976) 8–11, for the theta dependence and the anomaly.
- Roberto D. Peccei and Helen R. Quinn, "CP conservation in the presence of pseudoparticles", *Physical Review Letters* 38 (1977) 1440–1443, for the Peccei–Quinn mechanism that resolves strong CP.
- Steven Weinberg, "A new light boson?", *Physical Review Letters* 40 (1978) 223–226, and Frank Wilczek, "Problem of strong $P$ and $T$ invariance in the presence of instantons", *Physical Review Letters* 40 (1978) 279–282, for the axion.
- R. Jackiw and C. Rebbi, "Vacuum periodicity in a Yang–Mills quantum theory", *Physical Review Letters* 37 (1976) 172–175, and Curtis G. Callan, Roger F. Dashen and David J. Gross, "The structure of the gauge theory vacuum", *Physics Letters B* 63 (1976) 334–340, for the theta vacuum and its periodicity.
- Jihn E. Kim and Gianpaolo Carosi, "Axions and the strong CP problem", *Reviews of Modern Physics* 82 (2010) 557–601, for the experimental status of strong CP and the axion.
- C. A. Baker et al., "An improved experimental limit on the electric dipole moment of the neutron", *Physical Review Letters* 97 (2006) 131801, for the bound on the neutron electric dipole moment.
- Sidney Coleman, "The uses of instantons", in *Aspects of Symmetry* (Cambridge University Press, 1985), for the theta vacuum, its periodicity and the strong CP discussion.
- Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the theta term, the axial anomaly and the chiral rotation of the theta parameter.
