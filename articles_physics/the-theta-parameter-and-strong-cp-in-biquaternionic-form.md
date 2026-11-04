# __The Theta Parameter and Strong CP in Biquaternionic Form__

## Introduction

*The Semiclassical Expansion and the Instanton Gas in Biquaternionic Form* showed that the sum over topological sectors forces a dependence on an angle, and *Electric–Magnetic Duality and the Modular Group in Biquaternionic Form* showed that the shift of that angle by $2\pi$ is one generator of the duality group. This article takes the angle seriously as a **parameter of the theory** and follows its consequences: the theta term in the action, its periodicity, and the strong CP problem that its non-observation creates.

The framework's contribution to this subject is unusually direct, and it rests on a result established earlier in the series. In the abelian sector the topological density is not a foreign object: it is proportional to the framework's second invariant, $I_2=\vec E\cdot\vec B$.

**Frame.** Displays are read in the $\mathbb{B}$ frame, with the $ict'$ convention for sums over indices: the metric is the Kronecker delta, so the labels are summed directly. The four-index symbol is the all-low orientation density, $\epsilon_{0123}=+1$.

$$
\tfrac14\sum_{\mu,\nu,\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}
=\tfrac12\,\sum_{\mu,\nu}F_{\mu\nu}F^{\mathrm{dual}}_{\mu\nu}
=\frac{2i}{c}\,I_2 \quad(\text{Lorentzian}),
\qquad
I_2=\vec E\cdot\vec B ,
$$

as *Instantons and Solitons in Biquaternionic Form* recomputed from the component conventions of *The Field-Strength Biquaternion and Its Invariants*. The quarter-density is one half of the full density $\sum_{\mu,\nu}F_{\mu\nu}F^{\mathrm{dual}}_{\mu\nu}=\frac{4i}{c}I_2$ used below, because the $\tfrac12$ in the definition of the dual is counted once there and twice in $\tfrac14\sum\epsilon FF$. Both displays are written out, so that neither is read as the other. The theta term of the Maxwell sector is therefore proportional to the integral of one of the framework's own invariants, and it is specifically the **pseudoscalar** invariant: $I_1=\vec E^2-c^2\vec B^2$ is parity-even and $I_2$ is parity-odd. The CP-odd character of the theta term, which is the source of the strong CP problem, is thus visible in the algebra as the parity of the second invariant.

$$
Ϙ=\frac{1}{8\pi^2}\int\mathrm{Tr}\bigl(F\wedge F\bigr)\in\mathbb Z ,
\qquad
S_\theta=\frac{\theta}{32\pi^2}\int \sum_{\mu,\nu}F_{\mu\nu}F^{\mathrm{dual}}_{\mu\nu} ,
\qquad
F^{\mathrm{dual}}_{\mu\nu}=\tfrac12\sum_{\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}F_{\rho\sigma} ,
$$

with all indices summed in the $ict'$ convention as in the companion gauge articles. Charges are in units $\hbar=c=1$ where a quantisation statement is made. The trace $\mathrm{Tr}$ is the matrix trace on the gauge factor, distinguished from the informational trace formula, and it is taken in the fundamental representation with $\mathrm{Tr}(T^aT^b)=\tfrac12\delta^{ab}$; that normalization is what makes $Ϙ$ an integer.

Two things follow, and the article states them separately. The framework **supplies** the theta term's density and its discrete periodicity; it **does not supply** the value of $\theta$, because $\theta$ is a parameter labelling the vacuum and not an output of a complexified classical algebra. The strong CP problem is the statement that the observed near-vanishing of the physical theta parameter is not explained by the framework — or by the Standard Model without additional structure. This is reported as the boundary of what the algebra can address.

**Notation, once.** The tensor displays are read in the $\mathbb{B}$ frame, whose sums use the Kronecker delta. The imaginary unit is the central $i$, with $i^2=-1$; it commutes with the four units, so wherever two central units meet in a product they are reduced before the display is read. Every field equation of this article is written with the **biquaternionic gradient**,

$$
\tilde\nabla=e_t\frac{\partial}{\partial Q_t}+\vec e_x\frac{\partial}{\partial Q_x}+\vec e_y\frac{\partial}{\partial Q_y}+\vec e_z\frac{\partial}{\partial Q_z},
\qquad
\tilde\nabla^{\natural}=e_t\frac{\partial}{\partial Q_t}-\vec e_x\frac{\partial}{\partial Q_x}-\vec e_y\frac{\partial}{\partial Q_y}-\vec e_z\frac{\partial}{\partial Q_z},
$$

an element of the algebra whose coefficients are derivatives, and it acts from the left, $\tilde\nabla\psi$; it is never applied on the right. On the material sector, where $Q_t=ict'$ and $Q_k=q_k$, its time coefficient is $\frac{\partial}{\partial Q_t}=-\frac{i}{c}\frac{\partial}{\partial t'}$, with the same element and the same side. Its norm against the conjugate is the d'Alembertian, $\Box=\tilde\nabla\tilde\nabla^{\natural}=\tilde\nabla^{\natural}\tilde\nabla=\partial^2/\partial Q_t^2+\Delta_Q$, which on the material sector is $\Delta-c^{-2}\partial^2/\partial {t'}^2$.

**The free equation and the massive one.** The free equation is first order in one field, $\tilde\nabla\tilde F=0$. The massive equation is not, because $\tilde\nabla^2$ is not scalar: $e_t$ commutes with the three spatial units, so the two orders of a mixed derivative add a vector term instead of cancelling, and the diagonal part is not the d'Alembertian either. The massive equation is the **chiral pair**

$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,
\qquad
\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R,
$$

both acting from the left, and each half satisfies $\Box\tilde\Psi=m^2\tilde\Psi$ by the other. A source that writes the mass as a right multiplication prints a two-sided equation related to the pair by a change of variable, not a second dynamics (*The Dirac Equation in Biquaternionic Form*). The corpus writes the pair, and no one-field first-order massive equation is written here.

**The pseudoscalar and the side.** The **pseudoscalar** of the algebra is $\omega=-\vec e_z$, with $\omega^2=-\vec e_t$; it is the element a two-sided source prints as $i$. That letter is not the central unit: it does not commute with the spatial units, and the source's spin plane applies it on the right, $\psi\mapsto-\psi\vec e_z$. The chirality operation used below multiplies on the right and not on the left. It is a map of the field, written with its side in the display and not identified with an element,

$$
\Gamma:\;\psi\longmapsto\psi\,(i\omega)=-i\psi\vec e_z ,
\qquad
\Gamma^2=\mathrm{id},
$$

an involution of the field, since $(i\omega)^2=i^2\omega^2=(-1)(-\vec e_t)=e_t$ and the right multiplier $e_t$ is the identity. The left multiplication $\psi\mapsto-\vec e_z\psi$ is a different map, and it is not the one meant: the two do not agree, so the side belongs to the definition. The material time enters through $Q_t=ict'$, so the corpus's time term carries $-\frac{i}{c}\partial/\partial t'$; a display that prints $+i\partial/\partial t'$ differs by that sign, and the corpus's sign is the one kept.

- Companion article *The Field-Strength Biquaternion and Its Invariants*, for the invariant $I_2=\vec E\cdot\vec B$.
- Companion article *The Semiclassical Expansion and the Instanton Gas in Biquaternionic Form*, for the theta vacuum and its periodicity.
- Companion article *Electric–Magnetic Duality and the Modular Group in Biquaternionic Form*, for the modular action on the charges.

## The Theta Term and Its Density

The theta term of a non-abelian gauge theory is

$$
\boxed{\;S_\theta=\frac{\theta}{32\pi^2}\int d^4x\,\sum_{\mu,\nu,a}F_{\mu\nu a}F^{\mathrm{dual}}_{\mu\nu a}
=\frac{\theta}{8\pi^2}\int\mathrm{Tr}\bigl(F\wedge F\bigr)\;},
$$

so that $S_\theta=\theta\,Ϙ$ with the charge normalisation used here, since $\int\sum_{\mu,\nu,a}F_{\mu\nu a}F^{\mathrm{dual}}_{\mu\nu a}=4\int\mathrm{Tr}(F\wedge F)=32\pi^2Ϙ$. It is a total derivative,

$$
\sum_{\mu,\nu,a}F_{\mu\nu a}F^{\mathrm{dual}}_{\mu\nu a}
=\langle\tilde\nabla,\tilde J_{\mathrm{CS}}\rangle_{\natural} ,
\qquad
J_{\mathrm{CS},\mu}=\sum_{\nu,\rho,\sigma}\sum_a\epsilon_{\mu\nu\rho\sigma}\Bigl(A_{\nu a}F_{\rho\sigma a}
-\tfrac{g}{3}\sum_{b,c}f_{abc}A_{\nu a}A_{\rho b}A_{\sigma c}\Bigr),
$$

the standard non-abelian Chern–Simons current, whose abelian part is the primitive $J_{\mathrm{CS},\mu}=\sum_{\nu,\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}A_\nu F_{\rho\sigma}$ of *Instantons and Solitons in Biquaternionic Form* and whose form identity $F\wedge F=d\Omega_{\mathrm{CS}}$ is that article's. Two consequences of the total-derivative property are stated there and are used here: the integral depends only on the boundary data, hence on the instanton number, and the local equations of motion are unaffected by the theta term, so its effects are topological and quantum-mechanical rather than classical.

**The abelian density is the framework's invariant.** In the Maxwell sector the density collapses to the second invariant,

$$
\boxed{\;\sum_{\mu,\nu}F_{\mu\nu}F^{\mathrm{dual}}_{\mu\nu}=\frac{4i}{c}I_2\ \ (\text{Lorentzian}),
\qquad
\sum_{\mu,\nu}F_{\mu\nu}F^{\mathrm{dual}}_{\mu\nu}=4I_2\ \ (\text{Euclidean}),
\qquad
I_2=\vec E\cdot\vec B\;},
$$

so the theta term of the abelian theory is

$$
S_\theta^{\text{ab}}=\frac{\theta}{32\pi^2}\int d^4x\,\frac{4i}{c}I_2
=\frac{i\theta}{8\pi^2 c}\int d^4x\,I_2 .
$$

The theta term is thus the integral of the framework's own parity-odd invariant, with the factor $i$ that the $ict'$ convention attaches to the pseudoscalar. This is the genuine affirmative content of the article: in the abelian sector the CP-odd term is not an object the framework lacks; it is $I_2$, already present in *The Field-Strength Biquaternion and Its Invariants*.

**Parity.** Under parity $\vec E\mapsto-\vec E$ and $\vec B\mapsto+\vec B$, and under time reversal $\vec E\mapsto+\vec E$ and $\vec B\mapsto-\vec B$, so $I_2=\vec E\cdot\vec B\mapsto-I_2$ in both cases. Under either transformation the theta action changes sign, $S_\theta\mapsto-S_\theta$. A term linear in a parity-odd density with a real coefficient $\theta$ is therefore not invariant under parity unless $\theta=0$ or $\theta=\pi$ (mod $2\pi$), where the theta weight $\exp(i\theta Ϙ)$ is real for every integer $Ϙ$. For generic $\theta$ the theory violates $P$ and $T$, and by CPT it violates $CP$. The statement is purely algebraic in the abelian sector: the framework has one parity-even and one parity-odd derivative-free invariant, and the theta term is the integral of the odd one.

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

The reason $\bar\theta$ and not $\theta$ is the physical parameter is the anomaly. The generator of the common axial rotation of the quark fields is the chirality involution $\Gamma$ of the introduction, whose square is the identity, so the exponential $\exp(i\alpha\Gamma)$ is periodic in $\alpha$ — a rotation and not a boost. The rotation reads

$$
\exp(i\alpha\Gamma)\psi=\psi\,(\cos\alpha+\sin\alpha\,\vec e_z) .
$$

On the two chiral halves the same involution is a scalar phase, with opposite signs; split from the line above,

$$
\psi_L\longmapsto \exp(-i\alpha)\psi_L ,
\qquad
\psi_R\longmapsto \exp(+i\alpha)\psi_R .
$$

The two lines are one operation read on the two halves: $\Gamma$ is $-\mathrm{id}$ on $\psi_L$ and $+\mathrm{id}$ on $\psi_R$, so the single right multiplication becomes the pair of left phases. Under this rotation the mass matrix in the fermion bilinear $\psi_L^{\dagger}\,i\,(M_q\psi_R)\,\vec e_x$, in which the timelike insertion $i\vec e_x$ carries one chiral half into the other and is written on the right, transforms as

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

**What the framework contributes.** The axial rotation is generated by the involution $\Gamma$ of the introduction, whose square is the identity; it is $-\mathrm{id}$ on $\psi_L$ and $+\mathrm{id}$ on $\psi_R$, so the mass term is the chirality-off-diagonal coupling between the two halves, as *The Dirac Equation in Biquaternionic Form* records. The involution multiplies on the right, and the multiplier is the element $i\omega$; it is not the central grading, because $\omega$ anticommutes with $\vec e_x$ and $\vec e_y$, so the rotation cannot be absorbed into a redefinition of the central unit. The central object of the corpus is $\chi=i\tilde\Xi_{\mathrm{ad}}$, with $\tilde\Xi_{\mathrm{ad}}$ the adjoined central root of $-e_t$, so $\chi^2=e_t$ and $e_\pm=\tfrac12(e_t\pm\chi)$ are the two central idempotents; it commutes with every unit and is a different object from $\Gamma$, the two coinciding only in the one-mode truncation, where a single symbol represents both. The shift of $\theta$ is therefore a rotation of the two chiral halves against each other, and the invariance of $\bar\theta$ is the statement that the physics depends only on the product of the theta phase and the mass-matrix phase. The algebra makes the structure of the rotation visible — the pseudoscalar generator, the off-diagonal mass, the two halves — while the anomaly that makes the rotation non-trivial for the measure is imported from the quantum theory.

## Summary

The theta term $S_\theta=\frac{\theta}{32\pi^2}\int \sum_{\mu,\nu}F_{\mu\nu}F^{\mathrm{dual}}_{\mu\nu}$ is the integral of a total derivative, hence depends only on the instanton number, and in the abelian sector its density is proportional to the framework's parity-odd invariant $I_2=\vec E\cdot\vec B$:

$$
\sum_{\mu,\nu}F_{\mu\nu}F^{\mathrm{dual}}_{\mu\nu}=\frac{4i}{c}\,I_2 \quad(\text{Lorentzian}),
\qquad
\sum_{\mu,\nu}F_{\mu\nu}F^{\mathrm{dual}}_{\mu\nu}=4\,I_2 \quad(\text{Euclidean}).
$$

Because it is the integral of a parity-odd density, the theta term violates $P$ and $T$ unless $\theta=0$ or $\pi$. The theta dependence enters through the instanton sum $Z(\theta)=\sum_Ϙ\exp(iϘ\theta)Z_Ϙ$ and is periodic with period $2\pi$, verified to machine precision; the periodicity is the $T$ generator of the modular group and originates in the integrality of the topological charge.

The physical theta parameter is $\bar\theta=\theta+\arg\det M_q$, and the neutron electric dipole moment bounds it by $|\bar\theta|\lesssim10^{-10}$, which is the strong CP problem: the framework, like the Standard Model without additional structure, gives no reason for the near-vanishing. The framework supplies the CP-odd density as the invariant $I_2$ and supplies the periodicity and the vacuum structure, but it does not supply the value of $\theta$, which is a coefficient in the action and not an element of the algebra; the resolution is imported.

The operator content is carried by the gradient and by one involution: the axial rotation is generated by $\Gamma$, right multiplication by the pseudoscalar $\omega=-\vec e_z$, and the massive equation is the chiral pair $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$, $\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R$, since $\tilde\nabla^2$ is not scalar.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb B=\mathbb C\otimes_{\mathbb R}\mathbb H$ | Biquaternion algebra |
| $\tilde F=i\sqrt{\epsilon}\vec E-\sqrt{\mu}\vec H$ | Field-strength biquaternion (an element, not the tensor $F_{\mu\nu}$) |
| $I_1=\vec E^2-c^2\vec B^2$ | First invariant (parity-even, scalar) |
| $I_2=\vec E\cdot\vec B$ | Second invariant (parity-odd, pseudoscalar); theta density |
| $\theta$ | Theta angle; coefficient of the topological term |
| $S_\theta=\frac{\theta}{32\pi^2}\int\sum_{\mu,\nu}F_{\mu\nu}F^{\mathrm{dual}}_{\mu\nu}$ | Theta term of the action |
| $F^{\mathrm{dual}}_{\mu\nu}=\frac12\sum_{\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}F_{\rho\sigma}$ | Hodge dual field strength |
| $Ϙ=\frac{1}{8\pi^2}\int\mathrm{Tr}(F\wedge F)$ | Topological charge, $Ϙ\in\mathbb Z$ |
| $J_{\mathrm{CS},\mu}$ | Chern–Simons current, $\sum_{\mu,\nu}F_{\mu\nu}F^{\mathrm{dual}}_{\mu\nu}=\langle\tilde\nabla,\tilde J_{\mathrm{CS}}\rangle_{\natural}$ |
| $Z(\theta)=\sum_Ϙ \exp(iϘ\theta)Z_Ϙ$ | Theta-dependent partition function, period $2\pi$ |
| $\bar\theta=\theta+\arg\det M_q$ | Physical CP-violating parameter |
| $M_q$ | Quark mass matrix (imported) |
| $\tilde\nabla=e_t\frac{\partial}{\partial Q_t}+\vec e_x\frac{\partial}{\partial Q_x}+\vec e_y\frac{\partial}{\partial Q_y}+\vec e_z\frac{\partial}{\partial Q_z}$ | Biquaternionic gradient; an element with derivative coefficients, acting from the left |
| $\tilde\nabla^{\natural}$ | Its quaternion conjugate, $e_t\frac{\partial}{\partial Q_t}-\vec e_x\frac{\partial}{\partial Q_x}-\vec e_y\frac{\partial}{\partial Q_y}-\vec e_z\frac{\partial}{\partial Q_z}$ |
| $\Box=\tilde\nabla\tilde\nabla^{\natural}$ | D'Alembertian, $\partial^2/\partial Q_t^2+\Delta_Q$; $\Delta-c^{-2}\partial^2/\partial {t'}^2$ on $\mathbb{M}_-$ |
| $\omega=-\vec e_z$ | Pseudoscalar, $\omega^2=-\vec e_t$; the source's $i$, kept distinct from the central unit |
| $\Gamma:\psi\mapsto\psi(i\omega)=-i\psi\vec e_z$ | Chirality involution; a right multiplication and not an element, $\Gamma^2=\mathrm{id}$, $-\mathrm{id}$ on $\psi_L$, $+\mathrm{id}$ on $\psi_R$ |
| $\psi_L,\psi_R$ | Chiral halves, the $\mp\mathrm{id}$ eigenspaces of $\Gamma$; the subscripts name the part and not a multiplication |
| $\chi=i\tilde\Xi_{\mathrm{ad}}$ | Central grading, the adjoined central root of $-e_t$; $\chi^2=e_t$, $e_\pm=\tfrac12(e_t\pm\chi)$; not the involution $\Gamma$ |
| $a,b,c$ | Colour indices, written low; every contraction over them is an explicit sum. The speed of light is also $c$ and is a scalar, not an index. |
| $f_{abc}$ | Structure constants of the gauge factor, written low |

## Further Reading

- Gerard 't Hooft, "Symmetry breaking through Bell–Jackiw anomalies", *Physical Review Letters* 37 (1976) 8–11, for the theta dependence and the anomaly.
- Roberto D. Peccei and Helen R. Quinn, "CP conservation in the presence of pseudoparticles", *Physical Review Letters* 38 (1977) 1440–1443, for the Peccei–Quinn mechanism that resolves strong CP.
- Steven Weinberg, "A new light boson?", *Physical Review Letters* 40 (1978) 223–226, and Frank Wilczek, "Problem of strong $P$ and $T$ invariance in the presence of instantons", *Physical Review Letters* 40 (1978) 279–282, for the axion.
- R. Jackiw and C. Rebbi, "Vacuum periodicity in a Yang–Mills quantum theory", *Physical Review Letters* 37 (1976) 172–175, and Curtis G. Callan, Roger F. Dashen and David J. Gross, "The structure of the gauge theory vacuum", *Physics Letters B* 63 (1976) 334–340, for the theta vacuum and its periodicity.
- Jihn E. Kim and Gianpaolo Carosi, "Axions and the strong CP problem", *Reviews of Modern Physics* 82 (2010) 557–601, for the experimental status of strong CP and the axion.
- C. A. Baker et al., "An improved experimental limit on the electric dipole moment of the neutron", *Physical Review Letters* 97 (2006) 131801, for the bound on the neutron electric dipole moment.
- Sidney Coleman, "The uses of instantons", in *Aspects of Symmetry* (Cambridge University Press, 1985), for the theta vacuum, its periodicity and the strong CP discussion.
- Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the theta term, the axial anomaly and the chiral rotation of the theta parameter.
