# __The Theta Parameter and Strong CP in Biquaternionic Form__

## Introduction

*The Semiclassical Expansion and the Instanton Gas in Biquaternionic Form* showed that the sum over topological sectors forces a dependence on an angle, and *Electric–Magnetic Duality and the Modular Group in Biquaternionic Form* showed that the shift of that angle by $2\pi$ is one generator of the duality group. This article takes the angle seriously as a **parameter of the theory** and follows its consequences: the theta term in the action, its periodicity, and the strong CP problem that its non-observation creates.

The framework's contribution to this subject is unusually direct, and it rests on a result established earlier in the series. In the abelian sector the topological density is not a foreign object: it is proportional to the framework's second invariant, $I_2=\vec E\cdot\vec B$.

**Frame.** Displays are read in the $\mathbb{B}$ frame of *Frame and Metric Conventions*, with the $i r'_t$ convention for sums over indices: the labels are summed directly, and the four-index symbol is the all-low orientation density of *Operator and Calculus Conventions*.

$$
\tfrac14\sum_{\mu,\nu,\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}
=\tfrac12\,\sum_{\mu,\nu}F_{\mu\nu}F_{\mathrm{dual},\mu\nu}
=\frac{2i}{c}\,I_2 \quad(\text{Lorentzian}),
\qquad
I_2=\vec E\cdot\vec B ,
$$

as *Instantons and Solitons in Biquaternionic Form* recomputed from the component conventions of *The Field-Strength Biquaternion and Its Invariants*. The quarter-density is one half of the full density $\sum_{\mu,\nu}F_{\mu\nu}F_{\mathrm{dual},\mu\nu}=\frac{4i}{c}I_2$ used below, because the $\tfrac12$ in the definition of the dual is counted once there and twice in $\tfrac14\sum\epsilon FF$. Both displays are written out, so that neither is read as the other. The theta term of the Maxwell sector is therefore proportional to the integral of one of the framework's own invariants, and it is specifically the **parity-odd** invariant: $I_1=\vec E^2-c^2\vec B^2$ is parity-even and $I_2$ is parity-odd. The CP-odd character of the theta term, which is the source of the strong CP problem, is thus visible in the algebra as the parity of the second invariant.

$$
Ϙ=\frac{1}{8\pi^2}\int\mathrm{Tr}\bigl(F\wedge F\bigr)\in\mathbb Z ,
\qquad
S_\theta=\frac{\theta}{32\pi^2}\int \sum_{\mu,\nu}F_{\mu\nu}F_{\mathrm{dual},\mu\nu} ,
\qquad
F_{\mathrm{dual},\mu\nu}=\tfrac12\sum_{\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}F_{\rho\sigma} ,
$$

with all indices summed in the $i r'_t$ convention as in the companion gauge articles. A quantisation statement carries the factor $\frac{k_m}{m\,c}$ beside the charge product. The trace $\mathrm{Tr}$ is the matrix trace on the gauge factor, distinguished from the trace of an element of the algebra, and it is taken in the fundamental representation with $\mathrm{Tr}(T^aT^b)=\tfrac12\delta^{ab}$; that normalization is what makes $Ϙ$ an integer.

Two things follow, and the article states them separately. The framework **supplies** the theta term's density and its discrete periodicity; it **does not supply** the value of $\theta$, because $\theta$ is a parameter labelling the vacuum and not an output of a complexified classical algebra. The strong CP problem is the statement that the observed near-vanishing of the physical theta parameter is not explained by the framework — or by the Standard Model without additional structure. This is reported as the boundary of what the algebra can address.

**Notation.** The imaginary unit is the central $i$, with $i^2=-1$; it commutes with the four units, so wherever two central units meet in a product they are reduced before the display is read. Every field equation of this article is written with the **biquaternionic gradient** $\tilde\nabla$ of *Operator and Calculus Conventions*, an element of the algebra whose coefficients are derivatives; it acts from the left, its conjugate is $\tilde\nabla^{\natural}$, and the **d'Alembertian** $\Box$ is its quaternionic norm. The derivative on the material sector, the time coefficient included, is that article's.

**The free equation and the massive one.** The free equation is first order in one field, $\tilde\nabla\tilde F=0$. The massive equation is not, because $\tilde\nabla^2$ is not scalar: $e_t$ commutes with the three spatial units, so the two orders of a mixed derivative add a vector term instead of cancelling, and the diagonal part is not the d'Alembertian either. The massive equation is the **chiral pair**

$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L},
\qquad
\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R},
$$

both acting from the left, and each half satisfies $\Box\tilde{Ξ}_{\mathrm{sp}}=k_m^{2}\tilde{Ξ}_{\mathrm{sp}}$ by the other. A source that writes the mass as a right multiplication prints a two-sided equation related to the pair by a change of variable, not a second dynamics (*The Dirac Equation in Biquaternionic Form*). The corpus writes the pair, and no one-field first-order massive equation is written here. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

**The field and its two values.** The field is an element $\tilde{Ξ}_{\mathrm{sp}}$ of $\mathbb{B}$. Its two parts carry the chirality subscript of *Special Element Conventions*, §*The Chirality Convention*: $\tilde{Ξ}_{\mathrm{sp},L}$ is the part of value $-1$ and $\tilde{Ξ}_{\mathrm{sp},R}$ the part of value $+1$, and only the zero element carries both. The label belongs to the element and not to a state, so a product and a unit carry it as well. A central phase multiplies the two parts alike. The axial rotation of §*The Chiral Rotation and the Invariance of the Physical Parameter* does not, and that difference is what moves the physical parameter.

- Companion article *The Field-Strength Biquaternion and Its Invariants*, for the invariant $I_2=\vec E\cdot\vec B$.
- Companion article *The Semiclassical Expansion and the Instanton Gas in Biquaternionic Form*, for the theta vacuum and its periodicity.
- Companion article *Electric–Magnetic Duality and the Modular Group in Biquaternionic Form*, for the modular action on the charges.

## The Theta Term and Its Density

The theta term of a non-abelian gauge theory is

$$
\boxed{\;S_\theta=\frac{\theta}{32\pi^2}\int d^4r\,\sum_{\mu,\nu,a}F_{\mu\nu a}F_{\mathrm{dual},\mu\nu a}
=\frac{\theta}{8\pi^2}\int\mathrm{Tr}\bigl(F\wedge F\bigr)\;},
$$

so that $S_\theta=\theta\,Ϙ$ with the charge normalisation used here, since $\int\sum_{\mu,\nu,a}F_{\mu\nu a}F_{\mathrm{dual},\mu\nu a}=4\int\mathrm{Tr}(F\wedge F)=32\pi^2Ϙ$. It is a total derivative,

$$
\sum_{\mu,\nu,a}F_{\mu\nu a}F_{\mathrm{dual},\mu\nu a}
=\langle\tilde\nabla,\tilde J_{\Phi,\mathrm{CS}}\rangle_{\natural} ,
\qquad
J_{\mathrm{CS},\mu}=\sum_{\nu,\rho,\sigma}\sum_a\epsilon_{\mu\nu\rho\sigma}\Bigl(A_{\nu a}F_{\rho\sigma a}
-\tfrac{g}{3}\sum_{b,c}f_{abc}A_{\nu a}A_{\rho b}A_{\sigma c}\Bigr),
$$

the standard non-abelian Chern–Simons current, whose abelian part is the primitive $J_{\mathrm{CS},\mu}=\sum_{\nu,\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}A_\nu F_{\rho\sigma}$ of *Instantons and Solitons in Biquaternionic Form* and whose form identity $F\wedge F=d\Omega_{\mathrm{CS}}$ is that article's. Two consequences of the total-derivative property are stated there and are used here: the integral depends only on the boundary data, hence on the instanton number, and the local equations of motion are unaffected by the theta term, so its effects are topological and quantum-mechanical rather than classical.

**The abelian density is the framework's invariant.** In the Maxwell sector the density collapses to the second invariant,

$$
\boxed{\;\sum_{\mu,\nu}F_{\mu\nu}F_{\mathrm{dual},\mu\nu}=\frac{4i}{c}I_2\ \ (\text{Lorentzian}),
\qquad
\sum_{\mu,\nu}F_{\mu\nu}F_{\mathrm{dual},\mu\nu}=4I_2\ \ (\text{Euclidean}),
\qquad
I_2=\vec E\cdot\vec B\;},
$$

so the theta term of the abelian theory is

$$
S_\theta^{\text{ab}}=\frac{\theta}{32\pi^2}\int d^4r\,\frac{4i}{c}I_2
=\frac{i\theta}{8\pi^2 c}\int d^4r\,I_2 .
$$

The theta term is thus the integral of the framework's own parity-odd invariant, with the factor $i$ that the $i r'_t$ convention attaches to it. This is the genuine affirmative content of the article: in the abelian sector the CP-odd term is not an object the framework lacks; it is $I_2$, already present in *The Field-Strength Biquaternion and Its Invariants*.

**The same invariant, read from the element.** The array above is a contraction, and the invariant it contracts to is one component of a norm. In vacuum the two medium factors of the companion are one, so $c=1$ there; the quaternionic norm of the field-strength element is $-(I_1+2iI_2)$ (*The Field-Strength Biquaternion and Its Invariants*), so the parity-odd invariant is minus one half of its imaginary part,

$$
I_2=-\tfrac12\,\mathrm{Im}\,\langle\tilde F\rangle_{\natural}\qquad(\text{vacuum}),
$$

and the theta density is a component of the norm of one element. The reading needs no array: the entries of $F_{\mu\nu}$ and the four coefficients of $\tilde F$ carry the same number, and the second carries it as the imaginary component of $\langle\tilde F\rangle_{\natural}$, the norm of the field element.

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

The small-$\theta_{\mathrm{vac}}$ dependence of the vacuum energy is the same as in the semiclassical article,

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

The reason $\bar\theta$ and not $\theta$ is the physical parameter is the anomaly. The common axial rotation of the quark fields multiplies the two values of the subscript by opposite central phases,

$$
\tilde{Ξ}_{\mathrm{sp},L}\longmapsto \exp(-i\alpha)\tilde{Ξ}_{\mathrm{sp},L} ,
\qquad
\tilde{Ξ}_{\mathrm{sp},R}\longmapsto \exp(+i\alpha)\tilde{Ξ}_{\mathrm{sp},R} .
$$

Both multipliers have modulus one, so the rotation is periodic in $\alpha$: it is a rotation and not a boost. The two lines are one operation read on the two values; the field is one element, and the rotation multiplies each of its parts by its own phase.

**The mass, and the phase it takes.** The mass is the term that couples the two values: in the chiral pair it is the only term that carries the field from one value to the other. The two values are rotated in opposite senses, so a term that joins them takes twice the phase. With $M_q$ the quark mass matrix — a flavour-space matrix, imported from the Standard Model and not a display of the algebra — the rotation gives

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

**What the framework contributes.** The axial rotation is the pair of opposite phases on the two values, and the mass is the term that couples them. The algebra makes the structure visible — two values, one coupling, one phase difference — and it costs no further object: no grading, no second unit and no side enters the description. A central phase is the contrast that matters. It multiplies the two values alike, so it cannot move one against the other, and only a rotation in opposite senses can move the mass phase against the theta phase. The shift of $\theta$ is therefore a rotation of the two values against each other, and the invariance of $\bar\theta$ is the statement that the physics depends only on the product of the theta phase and the mass-matrix phase. The anomaly that makes the rotation non-trivial for the measure is imported from the quantum theory.

## Summary

The theta term $S_\theta=\frac{\theta}{32\pi^2}\int \sum_{\mu,\nu}F_{\mu\nu}F_{\mathrm{dual},\mu\nu}$ is the integral of a total derivative, hence depends only on the instanton number, and in the abelian sector its density is proportional to the framework's parity-odd invariant $I_2=\vec E\cdot\vec B$:

$$
\sum_{\mu,\nu}F_{\mu\nu}F_{\mathrm{dual},\mu\nu}=\frac{4i}{c}\,I_2 \quad(\text{Lorentzian}),
\qquad
\sum_{\mu,\nu}F_{\mu\nu}F_{\mathrm{dual},\mu\nu}=4\,I_2 \quad(\text{Euclidean}),
\qquad
I_2=-\tfrac12\,\mathrm{Im}\,\langle\tilde F\rangle_{\natural}\ \ (\text{vacuum}).
$$

Because it is the integral of a parity-odd density, the theta term violates $P$ and $T$ unless $\theta=0$ or $\pi$. The theta dependence enters through the instanton sum $Z(\theta)=\sum_Ϙ\exp(iϘ\theta)Z_Ϙ$ and is periodic with period $2\pi$, verified to machine precision; the periodicity is the $T$ generator of the modular group and originates in the integrality of the topological charge.

The physical theta parameter is $\bar\theta=\theta+\arg\det M_q$, and the neutron electric dipole moment bounds it by $|\bar\theta|\lesssim10^{-10}$, which is the strong CP problem: the framework, like the Standard Model without additional structure, gives no reason for the near-vanishing. The framework supplies the CP-odd density as the invariant $I_2$, read as the imaginary component of the norm of the field element, and supplies the periodicity and the vacuum structure, but it does not supply the value of $\theta$, which is a coefficient in the action and not an element of the algebra; the resolution is imported.

The field content is carried by the gradient and by the chirality subscript: the gradient acts from the left, the mass is the one term that couples the two values, and the massive equation is the chiral pair $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R}$, since $\tilde\nabla^2$ is not scalar.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb B$ | The biquaternion algebra, as fixed in *Algebra and Element Conventions* |
| $\tilde F$ | Field strength, the one fixed field of *Algebra and Element Conventions*; an element, not the tensor $F_{\mu\nu}$ |
| $I_1=\vec E^2-c^2\vec B^2$ | First invariant (parity-even, scalar) |
| $I_2=\vec E\cdot\vec B$ | Second invariant (parity-odd); the theta density; in vacuum $I_2=-\tfrac12\mathrm{Im}\langle\tilde F\rangle_{\natural}$ |
| $\theta$ | Theta angle; coefficient of the topological term |
| $S_\theta=\frac{\theta}{32\pi^2}\int\sum_{\mu,\nu}F_{\mu\nu}F_{\mathrm{dual},\mu\nu}$ | Theta term of the action |
| $F_{\mathrm{dual},\mu\nu}=\frac12\sum_{\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}F_{\rho\sigma}$ | Hodge dual field strength |
| $Ϙ=\frac{1}{8\pi^2}\int\mathrm{Tr}(F\wedge F)$ | Topological charge, $Ϙ\in\mathbb Z$ |
| $J_{\mathrm{CS},\mu}$ | Chern–Simons current, $\sum_{\mu,\nu}F_{\mu\nu}F_{\mathrm{dual},\mu\nu}=\langle\tilde\nabla,\tilde J_{\Phi,\mathrm{CS}}\rangle_{\natural}$ |
| $Z(\theta)=\sum_Ϙ \exp(iϘ\theta)Z_Ϙ$ | Theta-dependent partition function, period $2\pi$ |
| $\bar\theta=\theta+\arg\det M_q$ | Physical CP-violating parameter |
| $M_q$ | Quark mass matrix in flavour space (imported); not a display of the algebra |
| $\tilde\nabla$ | The biquaternionic gradient of *Operator and Calculus Conventions*; an element with derivative coefficients, acting from the left |
| $\tilde\nabla^{\natural}$ | Its quaternion conjugate |
| $\Box$ | The d'Alembertian of the same article, the quaternionic norm of the gradient; scalar |
| $\tilde{Ξ}_{\mathrm{sp}}$, $\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{Ξ}_{\mathrm{sp},R}$ | The field, an element of $\mathbb B$, and its two parts: $L$ is the value $-1$, $R$ the value $+1$ |
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
