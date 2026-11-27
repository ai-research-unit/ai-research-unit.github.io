# __The Chemical Potential Is the Phase's Frequency__

## Introduction

**The claim.** The chemical potential of this corpus's fluid is not a new field: it is the rate at which the polar word's phase advances. Written out, $\mu_{\mathrm{chm}}=-\partial_{t'}S=\frac{h}{2\pi}\omega_\mu$ with $\omega_\mu=-\partial_{t'}\theta_{\mathrm{pha}}$ the phase's frequency. **Two things follow, and both are already claims the corpus makes without this article.** The chemical potential is not an independent datum, which is why the local thermal state has three independent fields and not four; and the thermal weight's $\mu$ is a holonomy, the phase's advance around one turn of the imaginary-time circle. This article states the identification, carries the constants, and says what it does not give.

**What is established.** Four things. First, the identification is exact in the corpus's letters, and it is a *reading* of the energy slot rather than a new equation: the phase's temporal gradient is the energy per particle, its spatial gradient is the momentum. Second, $\mu$ is derived and not postulated, so the count of independent data at an event stays at three. Third, the dimensionless combination $\beta\omega_\mu$ is the twist of the thermal circle's boundary condition, and with $\beta=\frac{h}{2\pi k_BT}$ it is $\frac{\mu_{\mathrm{chm}}}{k_BT}$ — the standard exponent, obtained as a number of turns. Fourth, Gibbs–Duhem's $\mu$-derivative has a sign opposite to its $\beta$-derivative for a reason that is now visible: a higher $\mu$ is a faster phase and a higher pressure, a longer $\beta$ is a lower temperature and a lower pressure.

**The identification is general; the count is the scalar column's.** $\mu_{\mathrm{chm}}=-\partial_{t'}S$ is a statement about a phase, so it applies wherever the word has one — and a word with several phases has several potentials. **The matrix rung's word carries four diagonal phases and therefore four chemical potentials**, which is the chemical-potential row of [The Rung Dictionary](the-rung-dictionary-what-the-general-symbols-mean-at-each-rung.html); the count three that this article justifies is the one-component column's. **A reader who needs the multi-component case reads the four potentials as the same identification applied four times**, and the reason the count still adds no independent field is unchanged: each potential is a rate of a phase, not a field.

**What is not new.** That a condensate's chemical potential is the frequency of its phase is standard — it is the statement $\psi=\sqrt ne^{-i\mu t/\hbar}$ in every treatment of the Gross–Pitaevskii equation. **What the corpus adds is the bookkeeping**: which constant sits between the frequency and the energy, why the count of local data survives, and the reading of $\mu$ as a holonomy that unifies the real-time and imaginary-time statements of the same object.

**Where it sits.** After [the local thermal state](the-local-thermal-state-of-a-fluid.html), whose list of three fields this article justifies, and before [the free-energy functional](the-free-energy-functional-at-finite-temperature.html), which uses $\mu$ as the Lagrange multiplier of a charge constraint. **The three articles are one chain**: the state's data, the potential conjugate to the charge among them, and the functional that generates all of them.

## The Identification, With the Constants Carried

**The word, in the letters the reverse map uses.** The polar decomposition of the field is written

$$
\tilde\Xi=n_{\mathrm{num}}\,e^{\frac{2\pi iS}{h}},
$$

with $n_{\mathrm{num}}$ the amplitude — the square of which is the proper density, $n_{\mathrm{num}}^{2}=\rho_{\mathrm{num}}$ — and $S$ the action, in joule-seconds. **The exponent is a number** because $S$ carries the action's unit and $h$ carries it too; the corpus's rule that an exponent is dimensionless is what forces the $\frac{2\pi}{h}$ rather than a bare $S$.

**Two gradients, two fluid quantities, and no new object.** Differentiating the word gives

$$
\partial_{t'}S=-E,\qquad \vec\nabla_\Phi S=\vec p ,
$$

the energy and the momentum of the mode, and the guidance relation turns the second into the flow, $\vec v=\vec p/m=\vec\nabla_\Phi S/m$. **The temporal partner of the guidance relation has been in the corpus all along and has not been named**: it is

$$
\boxed{\;\mu_{\mathrm{chm}}=-\partial_{t'}S=\frac{h}{2\pi}\,\omega_\mu,\qquad \omega_\mu:=-\partial_{t'}\theta_{\mathrm{pha}}\;}
$$

with $\theta_{\mathrm{pha}}=\frac{2\pi S}{h}$ the phase angle. **The chemical potential is the fourth component of the same gradient whose spatial components are the momentum.** It is the energy per particle, read at a point, and it is a frequency times the action quantum.

**The constants, one per slot, which is the corpus's habit.**

| quantity | read from the word | the constant that converts | what it is conjugate to |
| --- | --- | --- | --- |
| density | $n_{\mathrm{num}}^{2}=\rho_{\mathrm{num}}$ | none; a modulus squared | the chemical potential |
| flow | $\vec\nabla_\Phi S$ | $1/m$, the mass | the momentum |
| energy per particle | $-\partial_{t'}S$ | none; already an energy | the time |
| phase frequency | $-\partial_{t'}\theta_{\mathrm{pha}}$ | $\frac{h}{2\pi}$ | the phase's shift |
| temperature | the period $\beta$ | $k_B$ | the entropy |

**The table's fourth row is the article's claim and the fifth is its context.** The corpus's other article on which constant each field carries makes the same point for the reverse map; this one makes it for the phase's *rate*, which is the row the reverse map does not display because the map is written at fixed time.

**Why the sign is what it is.** A plane wave that advances in time with positive energy has $\theta_{\mathrm{pha}}=\frac{2\pi}{h}(-Et+\vec p\cdot\vec r)$, so $-\partial_{t'}S=+E$. **The minus in the definition is the statement that a positive-energy mode's phase decreases**, and a reader who drops it gets a chemical potential of the wrong sign in every Euler relation below.

## Why It Is Not an Independent Field

**The count, and the sentence it justifies.** [The local thermal state](the-local-thermal-state-of-a-fluid.html) lists the state as a triple $(\rho_{\mathrm{num}},p_{\mathrm{th}},\tilde V_\Phi)$ plus the temperature, and states that *the chemical potential is not independent — it is what the thermodynamic identity gives once the other data are fixed*. **This article says what it is instead**: a derivative of the configuration's phase, hence a function of the field and not a datum beside it.

**The test that makes the statement sharp.** Suppose $\mu$ were independent. Then a configuration could be changed at fixed density, pressure and flow while $\mu$ moved, and the Euler relation would be a constraint on that change rather than an identity. **In fact no such change exists**: at fixed $n_{\mathrm{num}}$ the word has one phase, its rate is fixed by the field equation, and $\mu$ moves only when the configuration moves. **The independence would require a second phase, and the polar word has one per diagonal entry.**

**The neutral case, and it is the cleanest check.** A real field has $\theta_{\mathrm{pha}}\equiv0$ by reality, so $\omega_\mu=0$ and $\mu_{\mathrm{chm}}=0$: a real scalar has no chemical potential, no charge and no phase current. **The identification predicts this without an extra rule**, which an independent field would not.

**The matrix rung, where the count is visible.** At the primordial rung the word's phase is the diagonal one, and the diagonal of $\mathrm{U}(4)$ carries the four eigenvalue phases. **So $\mu$ is four numbers there, one per density**, and the conservation of each is the Noether charge of the corresponding diagonal $\mathrm{U}(1)$. The criterion article's remark that continuity at the top rung collapses through the $\mathrm{U}(1)^{4}$ quotient is the same structure read as a continuity law. **A fluid with four densities has four chemical potentials, and the count still adds no independent field.**

## The Twist: μ as the Holonomy of the Thermal Circle

**The thermal circle, and what a phase does around it.** At temperature $T$ the imaginary-time direction is a circle of circumference $\beta=\frac{h}{2\pi k_BT}$, a period in seconds. **Transport the phase once around that circle and it does not return to itself**: over the period it advances by

$$
\theta_{\mathrm{pha}}(\tau+\beta)-\theta_{\mathrm{pha}}(\tau)=-\frac{2\pi\beta}{h}\,\mu_{\mathrm{chm}}=-\beta\omega_\mu ,
$$

a pure number. **So the boundary condition on the field is twisted**, and the twist angle is $\beta\omega_\mu$.

**The same number as the Boltzmann exponent.** With $\beta=\frac{h}{2\pi k_BT}$,

$$
\beta\omega_\mu=\frac{\mu_{\mathrm{chm}}}{k_BT},
$$

so the field is multiplied by $e^{-\mu_{\mathrm{chm}}/(k_BT)}$ on going once around. **That multiplier is the fugacity**, and the grand-canonical weight $\exp\bigl(-(E-\mu_{\mathrm{chm}}N)/(k_BT)\bigr)$ is now a statement about turns of the phase: each particle carries one turn's worth of phase, and one turn costs $-\mu_{\mathrm{chm}}/(k_BT)$ of exponent.

**The two statements of one object, and the corpus uses both.** In the imaginary-time language the twist is a **holonomy**: the Matsubara frequencies are shifted, and the shift is the background connection's temporal component integrated around the circle. In the real-time language the twist is a **frequency**: the phase rotates, and $\mu$ is its rate. **Neither is more fundamental**, and the identification $\mu=-\partial_{t'}S$ is what makes them the same number.

**The two circles, and why the state is doubly periodic.** The temperature supplies a period and the chemical potential a frequency; the first is a circumference and the second a rate. **A local thermal state is therefore specified by one period and one twist**, and $\beta$ and $\mu$ are not two independent thermodynamic fields but the length and the holonomy of the same circle. That is the geometric content of the pair $(\beta,\mu)$ that the Euler relation treats as two variables.

**Why this is worth stating in a fluid article.** The fluid's local state is a state at a point, and a point has no circle. **What the point carries is the period and the twist of its own imaginary-time neighbourhood**, which is exactly the finite-temperature structure the corpus's Tolman article makes local. A reader who thinks of $\mu$ as a density-like field will over-count the local data; a reader who thinks of it as a twist will count three.

## Gibbs–Duhem, Read as a Statement About Rates

**The two derivatives, and their opposite signs.** With $w_{\mathrm{fl}}$ the energy density, $s_{\mathrm{ent}}$ the entropy density, $n_{\mathrm{num}}$ the number density and $p_{\mathrm{th}}$ the thermal pressure, the corpus's Gibbs–Duhem relation is

$$
d p_{\mathrm{th}}=s_{\mathrm{ent}}\,dT+n_{\mathrm{num}}\,d\mu_{\mathrm{chm}} .
$$

Holding $T$ fixed, $n_{\mathrm{num}}=\partial p_{\mathrm{th}}/\partial\mu_{\mathrm{chm}}>0$: **a faster phase is a higher pressure at fixed temperature.** Holding $\mu$ fixed, $s_{\mathrm{ent}}=\partial p_{\mathrm{th}}/\partial T$ in the temperature variable and $s_{\mathrm{ent}}=-\frac{\beta}{T}\,\partial p_{\mathrm{th}}/\partial\beta$ in the period variable, where $\partial p_{\mathrm{th}}/\partial\beta<0$ — **the pressure falls as the period lengthens**, because a longer period is a colder state, and the entropy density is positive in both writings. **The two signs are one statement**: pressure rises with both rates, and one rate is written as its reciprocal.

**Euler's relation, and where it comes from.** With $w_{\mathrm{fl}}$ the energy per unit proper volume,

$$
w_{\mathrm{fl}}+p_{\mathrm{th}}=T\,s_{\mathrm{ent}}+\mu_{\mathrm{chm}}\,n_{\mathrm{num}} .
$$

This is Euler's theorem on a function homogeneous of degree one in the extensive data, and the field-theoretic content is that the action's density carries no length scale except the mass. **A scale-invariant fluid saturates it with $w_{\mathrm{fl}}=3p_{\mathrm{th}}$ and $\mu_{\mathrm{chm}}n_{\mathrm{num}}=0$**, the radiation check the local-state article performs; a massive fluid carries the mass in $\mu_{\mathrm{chm}}$, which is why $\mu_{\mathrm{chm}}$ has a rest-energy offset at zero temperature.

**The offset, stated so that it is not mistaken for an error.** For a non-relativistic condensate the frequency $\omega_\mu$ is measured from the rest energy, and $\mu_{\mathrm{chm}}=mc^{2}+\frac{h}{2\pi}\omega_\mu$ with $\omega_\mu$ the non-relativistic frequency. **The corpus's mass wave number $2\pi\nu_m=\frac{mc}{\hbar}$ is exactly this offset written as a rate**, which is why the mass term in the density is the same object as the zero of the chemical potential. A reader who forgets the offset finds $\mu_{\mathrm{chm}}=mc^{2}$ for a fluid at rest and concludes that the pressure is nonzero at zero temperature.

**Consistency with the state's count.** Euler's relation and Gibbs–Duhem are two statements about one potential, so they are not independent — the third test of the local-state article, integrability, is the statement that they are the same. **Because $\mu$ is a derivative of the configuration and not a datum, the two relations constrain nothing that the field did not already fix**; they are identities of the state, and that is why a fluid whose pressure is fitted rather than derived violates a Maxwell relation somewhere.

## What It Does Not Give

**It does not give $\mu$ as a function of $(T,n_{\mathrm{num}})$.** That is the equation of state, and the identification is compatible with every equation of state: it says what $\mu$ *is* at a configuration, not how it varies across configurations.

**It does not give the value of $\mu$ in a given state.** The value is read from the solution — from the phase's rate — and a state at rest with a given density has whatever $\mu$ its field equation demands. **The identification is a reading, not a prediction.**

**It does not add a conservation law.** The charge conjugate to $\mu$ is the phase's Noether charge, which [the Noether article](noethers-theorem-in-biquaternionic-form.html) already derives. **What this article adds is that the conjugate pair $(\mu,n_{\mathrm{num}})$ is the temporal pair of the guidance relation**, so the conservation of charge and the transport of number are one statement read twice.

**It does not fix the sign convention across the corpus.** The corpus writes some phases with $+iS$ and some with $-iS$; the identification is stated for the convention in which a positive-energy mode's phase decreases, and a reader working in the other convention must carry the sign consistently through every Euler relation. **This is the one place where a convention error is invisible in a modulus**, and it is worth a line in any article that uses $\mu$.

**It does not extend to a gauge charge without a choice.** For a gauged $U(1)$ the phase is a gauge-dependent object, and $\mu$ is physical only through the twisted boundary condition — which is gauge invariant precisely because it is a holonomy. **The covariant statement is the holonomy, and the frequency is its flat-space reading.**

## Summary

The chemical potential is the rate of the polar word's phase: $\mu_{\mathrm{chm}}=-\partial_{t'}S=\frac{h}{2\pi}\omega_\mu$ with $\omega_\mu=-\partial_{t'}\theta_{\mathrm{pha}}$. **It is the temporal component of the same gradient whose spatial components are the momentum**, so it is read from the configuration and is not an independent field — which is what makes the local thermal state's count three and not four. A real field has no phase and no chemical potential, and the matrix rung has four, one per diagonal phase.

Around the thermal circle the phase does not return to itself: it advances by $\beta\omega_\mu=\frac{\mu_{\mathrm{chm}}}{k_BT}$ turns, so the boundary condition is twisted and the fugacity $e^{-\mu_{\mathrm{chm}}/(k_BT)}$ is the holonomy. **The imaginary-time holonomy and the real-time frequency are one number**, and the pair $(\beta,\mu)$ is a circumference and a twist rather than two independent fields.

Gibbs–Duhem then reads as a statement about rates: the pressure rises with both, and the apparent sign difference between the $T$ and $\beta$ derivatives is the reciprocal. Euler's relation is homogeneity of the action's density, and the mass is the zero of $\mu$ — the offset the corpus's mass wave number writes as a rate.

The identification gives no equation of state, no value, no new conservation law and no sign convention. It gives the object, and the object is a derivative.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde\Xi=n_{\mathrm{num}}e^{\frac{2\pi iS}{h}}$ | The polar word in the reverse map's letters; $n_{\mathrm{num}}$ the amplitude, $n_{\mathrm{num}}^2=\rho_{\mathrm{num}}$ |
| $S$ | The action, in joule-seconds; the exponent's numerator |
| $\theta_{\mathrm{pha}}=\frac{2\pi S}{h}$ | The phase angle, dimensionless |
| $\omega_\mu=-\partial_{t'}\theta_{\mathrm{pha}}$ | The phase's frequency, in inverse seconds |
| $\mu_{\mathrm{chm}}=-\partial_{t'}S=\frac{h}{2\pi}\omega_\mu$ | The chemical potential, an energy per particle |
| $\partial_{t'}=c\,\partial_{r'_t}$ | The derivative with respect to the time $t'=r'_t/c$ |
| $\beta=\frac{h}{2\pi k_BT}$ | The thermal period, a time; the circumference of the imaginary-time circle |
| $\beta\omega_\mu=\frac{\mu_{\mathrm{chm}}}{k_BT}$ | The twist of the thermal circle's boundary condition; the fugacity's exponent |
| $e^{-\mu_{\mathrm{chm}}/(k_BT)}$ | The fugacity; the phase's multiplier on one turn of the thermal circle |
| $2\pi\nu_m=\frac{mc}{\hbar}$ | The mass wave number as a rate; the rest-energy offset of $\mu_{\mathrm{chm}}$ |
| $w_{\mathrm{fl}},p_{\mathrm{th}},s_{\mathrm{ent}},n_{\mathrm{num}}$ | Energy density, thermal pressure, entropy density, number density |
| $n_{\mathrm{num}}=\rho_{\mathrm{num}}$ | The identification at rest, where the proper density is the number density |

## Further Reading

- Lev P. Pitaevskii and Sandro Stringari, *Bose–Einstein Condensation* (Oxford University Press, 2003), for the condensate's chemical potential as the phase's frequency, $\psi=\sqrt n\,e^{-i\mu t/\hbar}$, and the identification's use in the Gross–Pitaevskii equation.
- Alexander L. Fetter and John Dirk Walecka, *Quantum Theory of Many-Particle Systems* (McGraw-Hill, 1971), for the grand-canonical weight, the fugacity and the Matsubara frequency shift at finite chemical potential.
- Joseph I. Kapusta and Charles Gale, *Finite-Temperature Field Theory* (2nd ed., Cambridge University Press, 2006), for the twisted boundary condition, the Polyakov loop and the holonomy reading of $\mu$.
- L. D. Landau and E. M. Lifshitz, *Statistical Physics, Part 1* (3rd ed., Pergamon, 1980), §24, for the Euler and Gibbs–Duhem relations and the homogeneity argument.
- [The Local Thermal State of a Fluid](the-local-thermal-state-of-a-fluid.html), for the triple of data and the count this article justifies.
- [The Equation of State in Biquaternion Form](the-equation-of-state-in-biquaternion-form.html), for $\mu$ as a variable of the equation of state, which this article does not supply.
- [The Free-Energy Functional at Finite Temperature](the-free-energy-functional-at-finite-temperature.html), for $\mu$ as the Lagrange multiplier of the charge constraint.
- [The Matsubara Thermal Formalism in Biquaternionic Form](the-matsubara-thermal-formalism-in-biquaternionic-form.html), for the imaginary-time circle whose twist this article identifies.
- [Noether's Theorem in Biquaternionic Form](noethers-theorem-in-biquaternionic-form.html), for the phase's charge, which is the conjugate of the chemical potential.
- [The Fluid–Wave Correspondence: Which Constant Each Field Carries](the-fluid-wave-correspondence-which-constant-each-field-carries.html), for the same bookkeeping applied to the reverse map's other slots.
