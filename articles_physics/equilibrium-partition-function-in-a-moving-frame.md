# __Equilibrium Partition Function in a Moving Frame__

## Introduction

**The partition function of an equilibrium state does not change when the state is boosted; what changes is the thermal element that appears in its exponent, and with it the temperature a boosted observer reads.** This article writes that statement in the corpus's letters and does nothing else.

**The rest-frame object is [The Partition Function in Biquaternionic Form](the-partition-function-in-biquaternionic-form.html)'s, and this article adds the boost and the frame dependence.** The trace, the identification of the trace with twice the scalar part, the thermal operator, the free energy, the internal energy and the entropy are all that article's; they are quoted here as needed and not re-derived. **This is standard relativistic thermodynamics in the corpus's letters, with no framework interpretation.**

**Two things are easy to get wrong and are the article's real content.** The first is to think that boosting a thermal state changes its partition function. It does not: $Z$ is a trace of an operator whose exponent is a Lorentz scalar, so $Z$ is a scalar, and a scalar is the same number in every frame. The second is to think that the temperature is invariant. It is not: the temperature is the reciprocal of a period, the period is the temporal component of a vector, and a boost stretches it. **Both mistakes come from treating the symbol $\beta$ as a number when it is a direction with a length attached.**

**The order of business.** The thermal element is defined first, as an element of the material sector with a norm and a temporal component, and the boost is written on it. The exponent of the thermal weight is then shown to be the contraction of that element with the flow momentum, which is a scalar, which is why $Z$ is a scalar. The partition function itself is written in the moving frame and reduced to the rest-frame one. The Matsubara condition is written along the tilted thermal circle. Then the thermodynamic quantities are read in the moving frame — temperature, energy density, pressure, entropy, free energy — with the numerical checks the corpus expects. The article closes with the status section, which records what is transcription and what is the corpus's reading, and with the summary and the notation.

## The Thermal Element of a Moving Frame

### The inverse temperature as a period

**The inverse temperature is a length, and the corpus fixes it once.** From [The Local Thermal Structure: k_B as the Scale of Imaginary Time](the-local-thermal-structure-kb-as-the-scale-of-imaginary-time.html),

$$
\beta=\frac{\hbar}{k_{B}\,T},
\qquad
c\beta=\frac{\hbar\,c}{k_{B}\,T},
$$

with $\beta$ the imaginary-time circumference, a length in these letters, and $c\beta$ the corresponding span in the material sector's units. **The display is quoted and not re-derived**: the article cited establishes that the imaginary-time direction is compact with circumference $\beta$ in the coordinate $r'_t$, and that the identity above is exact. Here the only use made of it is that $\beta$ is a *period* and not a number: it is a length measured along a direction, and the direction is what the boost acts on.

**The direction is the material sector's imaginary-time axis, and in the rest frame the period lies along it.** In the rest frame of the fluid the thermal displacement is

$$
\tilde\beta_{\Phi,0}=\beta\,i\,e_t,
\qquad
\langle\tilde\beta_{\Phi,0}\rangle_{\natural}=-\beta^{2},
$$

an element of $\mathbb{B}_{\Phi}$ whose only component is the temporal one and whose norm is the negative square of the period. **It is an element and not a vector**: no component is raised, the index is carried low when components are written, and the norm is the corpus's $\natural$ norm with the minus sign that the material sector's temporal slot supplies.

### The boost

**Boosting the state rotates the thermal element into the temporal-and-spatial direction of the flow, and the result is the flow element times the period.** With the velocity element of the conventions,

$$
\tilde V_{\Phi}=\gamma\left(i c\,e_t+\vec v\right)
=\gamma c\left(i e_t+\vec\beta_{\mathrm{vel}}\right),
\qquad
\vec\beta_{\mathrm{vel}}=\frac{\vec v}{c},
\qquad
\langle\tilde V_{\Phi}\rangle_{\natural}=-c^{2},
$$

the thermal element of the moving state is

$$
\tilde\beta_{\Phi}=\frac{\beta}{c}\,\tilde V_{\Phi}
=\beta\,\gamma\left(i e_t+\vec\beta_{\mathrm{vel}}\right),
$$

whose norm is $\langle\tilde\beta_{\Phi}\rangle_{\natural}=(\beta^{2}/c^{2})(-c^{2})=-\beta^{2}$. **The norm is unchanged by the boost, and that is the whole of the statement that the period is a scalar.** What the boost changes is the *direction* of the displacement: it acquires a spatial part $\beta\gamma\vec\beta_{\mathrm{vel}}$, so the thermal circle is tilted in any frame in which the fluid moves.

**The components, written low.** With $\tilde\beta_{\Phi}=\beta_{\Phi,t}e_t+\beta_{\Phi,x}\vec e_x+\beta_{\Phi,y}\vec e_y+\beta_{\Phi,z}\vec e_z$,

$$
\beta_{\Phi,t}=i\beta\gamma,
\qquad
\beta_{\Phi,\eta}=\beta\gamma\,\beta_{\mathrm{vel},\eta},
$$

and the rest frame is $\gamma=1$, $\vec\beta_{\mathrm{vel}}=0$. **The temporal component is $i$ times a length, and the factor $i$ is the element's**, exactly as $p_{\Phi,t}=iE/c$ carries the $i$ of the same slot. The product of two $i$'s is what makes the contraction below real.

### The contraction with the flow momentum, and why $Z$ is a scalar

**The thermal exponent is the contraction of the thermal element with the flow momentum, divided by the action quantum, and the contraction is a scalar.** Write

$$
-\frac{1}{\hbar}\,\beta_{\Phi,\nu}\,p_{\Phi,\nu},
\qquad
p_{\Phi,\nu}=m\,\tilde V_{\Phi,\nu},
\qquad
\beta_{\Phi,\nu}=\frac{\beta}{c}\,\tilde V_{\Phi,\nu},
$$

so that

$$
-\frac{1}{\hbar}\,\beta_{\Phi,\nu}p_{\Phi,\nu}
=-\frac{\beta}{c\hbar}\,m\,\langle\tilde V_{\Phi}\rangle_{\natural}
=-\frac{\beta}{c\hbar}\,m\,(-c^{2})
=\frac{\beta\,m\,c}{\hbar}=\beta\,k_m .
$$

**The result is independent of $\gamma$ and of $\vec v$, which is the statement that the thermal weight of a state is the same in every frame.** The three ingredients are: the norm of the flow element, which is $-c^{2}$ by the corpus's definition; the norm of the thermal element, which is $-\beta^{2}$; and the identity $1/k_m=\hbar/(mc)$. The cancellation of $\gamma$ is not an accident of the algebra but the content of the statement: a boost rotates both the thermal element and the momentum element the same way, so their contraction is invariant.

**Read in the rest frame, the display is the expected one.** There $\beta_{\Phi,\nu}p_{\Phi,\nu}=\beta\,i\,e_t\cdot i\,m\,c=-\beta mc$, so the exponent is $+\beta mc/\hbar=\beta k_m$, the ratio of the imaginary-time circumference to the reduced Compton length $1/k_m$ of the field. **That ratio is the single number the rest-frame thermal weight exponentiates**, and it is the corpus's dimensionless thermal parameter: it is $\beta$ measured in units of the field's own length.

**Read in the moving frame, the display splits into two pieces and both are physical.** Expanding the contraction with the components above,

$$
-\frac{1}{\hbar}\beta_{\Phi,\nu}p_{\Phi,\nu}
=\frac{1}{\hbar}\left(\beta\gamma\,\frac{E}{c}-\beta\gamma\,\vec\beta_{\mathrm{vel}}\cdot\vec p\right)
=\frac{\beta\gamma}{\hbar}\left(\frac{E}{c}-\vec\beta_{\mathrm{vel}}\cdot\vec p\right),
$$

where $p_{\Phi,t}=iE/c$ and the two $i$'s have been multiplied out; the factor $c$ in the first term is the one the temporal slot carries, and it is what makes the two terms have the same dimensions. **On the flow's own momentum the bracket collapses**: with $E=\gamma mc^{2}$ and $\vec p=\gamma m\vec v$, the bracket is $\gamma mc(1-\beta_{\mathrm{vel}}^{2})=mc/\gamma$, so the exponent is $-\beta\gamma\,mc/(\gamma\hbar)=-\beta mc/\hbar=-\beta k_m$, the frame-independent value of the display above. **The second term is a chemical potential for momentum**: in the moving frame the thermal weight favours the momenta that move with the fluid, with a coefficient $\beta\gamma\beta_{\mathrm{vel},\eta}$. It vanishes on the flow's momentum only when combined with the first term, and that cancellation is the invariance. This is the standard reading of a boost as a momentum chemical potential, quoted.

## The Partition Function

### The trace in the moving frame

**The partition function is the trace of the thermal operator, and its value is the rest-frame value.** With the thermal element of the moving state,

$$
Z=\mathrm{Tr}\left(\exp\left(-\frac{1}{\hbar}\beta_{\Phi,\nu}p_{\Phi,\nu}\right)\right),
$$

and since the exponent in the trace is $\beta k_m$ independently of the boost, as the previous section showed, the trace is the same number in every frame:

$$
Z(\beta,\vec\beta_{\mathrm{vel}})=Z(\beta,\vec 0)=2\,\mathrm{Sc}\bigl(\exp(-\beta k_m)\bigr),
$$

the last equality being [The Partition Function in Biquaternionic Form](the-partition-function-in-biquaternionic-form.html)'s identification of the trace with twice the scalar part, quoted at normalisation. **This is the article's main result and it is a negative one**: the moving frame does not have its own partition function.

**Why the trace cannot see the boost, in one sentence.** A trace is a sum over states of a scalar weight; a boost relabels the states — it maps each momentum to another — but it is a unitary relabelling, and a sum over a complete set is invariant under a unitary relabelling. **The partition function is therefore frame-independent for the same reason the dimension of a Hilbert space is.**

**What is not frame-independent is the decomposition of $Z$.** The free energy $F=-(1/\beta)\log Z$ is a scalar if $\beta$ is taken as the scalar period; the internal energy $E$, the momentum $\vec p$, the entropy and the pressure are components of elements and do change. The next section reads them.

### The rest frame as the special case

**Setting $\vec\beta_{\mathrm{vel}}=0$ returns the rest-frame article exactly, and this is the check that the boost has been inserted and nothing else.** At $\gamma=1$ the thermal element is $\beta i e_t$, the exponent is $\beta k_m$, and every display of [The Partition Function in Biquaternionic Form](the-partition-function-in-biquaternionic-form.html) is recovered with no modification. **The article therefore adds one parameter, $\vec\beta_{\mathrm{vel}}$, and one structural fact, that the thermal element is an element with a direction.** It adds nothing else, and a reader who wants the trace's biquaternion reading, the imaginary-time discussion, or the non-Hermitian extension is directed to the rest-frame article.

**One difference of emphasis, and it is the reason the moving case is worth an article.** In the rest frame the thermal element and the temporal axis coincide, so the statement "$\beta$ is a period along the imaginary time" and the statement "$\beta$ is a number" cannot be distinguished. In the moving frame they separate: the period is a length along a tilted direction, and the number a boosted observer measures is only its temporal component. **That separation is the content of the whole subject**, and it is invisible in the rest frame.

### The Matsubara condition along a tilted circle

**The periodicity of the fields is periodicity along the thermal element, and in a moving frame that is periodicity along a tilted line.** The Matsubara condition of [The Matsubara Thermal Formalism in Biquaternionic Form](the-matsubara-thermal-formalism-in-biquaternionic-form.html) is

$$
\tilde\Xi\left(\tilde R_\Phi+\tilde\beta_\Phi\right)=\pm\,\tilde\Xi\left(\tilde R_\Phi\right),
$$

with the plus sign for bosonic and the minus for fermionic fields, and $\tilde\beta_\Phi$ the thermal element rather than the rest-frame displacement $\beta i e_t$. **In the rest frame the two are the same and the condition reads as periodicity in $r'_t$**; in the moving frame the shift has a spatial part, and the condition identifies field values at points separated by a spacelike displacement as well as a timelike one.

**The frequencies are the ones conjugate to the tilted circle, and their spacing is set by the invariant length.** Writing the shift as $\tilde\beta_\Phi=\beta\gamma\left(ie_t+\vec\beta_{\mathrm{vel}}\right)$, the condition says that a mode $e^{ik_{\Phi,\nu}r_\nu}$ is allowed when $k_{\Phi,\nu}\beta_{\Phi,\nu}=2\pi n$. **The contraction is again a scalar**, so the spacing is $2\pi/\beta$ in the rest frame and $2\pi/(\beta\gamma)$ in a frame where the fluid moves — but the physical frequencies are not the rest-frame ones, because the mode's own wave vector is also boosted. **The invariant statement is the contraction, and it is the only statement that survives the boost without bookkeeping.**

**A caution the corpus's letters require.** The Matsubara frequencies are usually quoted as $\omega_n=2\pi n/\beta$, and in a moving frame this is the spacing along the tilted circle and not the spacing of the energy. The energy spacing in a moving frame is $\gamma$ times larger, by the time dilation of the period, and the two statements are consistent because the mode's wave vector tilts with the circle. **A reader who quotes $2\pi n/\beta$ in a moving frame without the tilt has the right spacing and the wrong axis.**

## What the Boost Does to the Thermodynamic Quantities

### The temperature a boosted observer reads

**The temperature a boosted observer reads is $T/\gamma$, and the reason is that the observer reads the temporal component of the thermal element.** With $\beta_{\Phi,t}=i\beta\gamma$ and $\beta$ the rest-frame period, the period the observer measures is $\gamma$ times the rest-frame one:

$$
\beta_{\mathrm{obs}}=\gamma\,\beta,
\qquad
T_{\mathrm{obs}}=\frac{T}{\gamma},
$$

since the temperature is what the period is reciprocal to. **The product is invariant**, $\beta_{\mathrm{obs}}T_{\mathrm{obs}}=\beta T$, and that invariance is the check that the two statements are one: a period and a temperature cannot both change unless their product stays fixed.

**The reading is the one the corpus's letters force, and it is worth saying why.** $\beta$ is a length along the imaginary-time direction and the direction is an element. An observer in relative motion resolves that element into a temporal component and a spatial one. The temporal component is what the observer's own clock measures as the period, and it is $\gamma$ times larger — the same time dilation that lengthens any interval. So the observer reads a *longer* period and hence a *lower* temperature. **The alternative reading, in which a moving body is hotter by $\gamma$, comes from boosting the exchanged heat rather than the period**; the corpus adopts the period reading because $\beta$ is defined as a period, and the article says so once rather than arguing it.

**The limit is the right one.** At $\beta_{\mathrm{vel}}\to0$ the factor is one and the rest-frame value is recovered; at $\beta_{\mathrm{vel}}\to1$ the observed temperature goes to zero, which is the statement that an ultra-relativistic observer sees the thermal circle stretched without bound. **There is no frame in which the temperature is negative and none in which the period is zero**, so the map is a bijection on the physical range.

### The table

**The three quantities that carry the boost were computed for three velocities, with the rest-frame temperature fixed at $300\,\mathrm{K}$, the rest-frame equation of state $w_{\mathrm{fl}}=3p_{\mathrm{th}}$, and the rest-frame circumference taken as the unit, $\beta=1$, so that the last column is a number a reader can reproduce.**

| $\beta_{\mathrm{vel}}$ | $\gamma$ | $T_{\mathrm{obs}}$ | $T_{\mathrm{obs}}/T$ | $w_{\mathrm{fl}}/w_{\mathrm{fl,rest}}$ | $s_{\mathrm{ent}}/s_{\mathrm{ent,rest}}$ | $\beta_{\mathrm{obs}}T_{\mathrm{obs}}$ |
|---|---|---|---|---|---|---|
| $0.6000$ | $1.250\,000\,000\,000$ | $240.000\,000\,000\,0$ | $0.800\,000\,000\,000$ | $1.750\,000\,000$ | $1.250\,000\,000$ | $300.000\,000\,000\,000$ |
| $0.8000$ | $1.666\,666\,666\,667$ | $180.000\,000\,000\,0$ | $0.600\,000\,000\,000$ | $3.370\,370\,370$ | $1.666\,666\,667$ | $300.000\,000\,000\,000$ |
| $0.979\,795\,897$ | $5.000\,000\,000\,000$ | $60.000\,000\,000\,00$ | $0.200\,000\,000\,000$ | $33.000\,000\,00$ | $5.000\,000\,000$ | $300.000\,000\,000\,000$ |

**The last column is constant to twelve decimal places, and it is the check.** The entropy density grows by $\gamma$, the energy density grows by $(w_{\mathrm{fl}}+p_{\mathrm{th}})\gamma^{2}-p_{\mathrm{th}}$ divided by $w_{\mathrm{fl}}$, and the temperature falls by $\gamma$; only the product $\beta_{\mathrm{obs}}T_{\mathrm{obs}}$ is invariant, and it is invariant identically because $\beta\propto1/T$. **A table with the product drifting would indicate an error in the boost of the thermal element**, and in particular a missing factor of $\gamma$ in the temporal component would show up as a constant offset of $1/\gamma$ in the same column.

### The energy density and the pressure

**The energy density of the moving state is the standard perfect-fluid combination, and it follows from the element without a new assumption.** With the energy-momentum element of the corpus, $\tilde\Sigma_{\Psi}=w_{\mathrm{fl}}e_t+\tfrac{i}{c}\vec S_{\mathrm P}$, and with the flow element of the state, the scalar part in the moving frame is

$$
w_{\mathrm{fl}}=\left(w_{\mathrm{fl,rest}}+p_{\mathrm{th}}\right)\gamma^{2}-p_{\mathrm{th}},
\qquad
p_{\mathrm{th}}=p_{\mathrm{th,rest}},
$$

the pressure being a scalar under a boost along the flow. **The two displays are one statement about the element**: the energy density is the flow-contracted energy-momentum, and the contraction of two elements gives the $\gamma^{2}$ combination. At $\gamma=1$ the rest-frame value is recovered, and at $\beta_{\mathrm{vel}}\to1$ the energy density grows without bound while the pressure stays fixed — the statement that a relativistic fluid's energy is dominated by its momentum.

**The pressure's invariance is worth a line, because it is not obvious.** A boost along the flow leaves the transverse stresses untouched and transforms only the temporal-temporal and longitudinal components. The trace of the stress is a scalar, so if the energy density grows by $\gamma^{2}$ and the trace is fixed, the pressure must be fixed too. **In the corpus's letters, the scalar part of $\tilde\Sigma_\Psi$ is $w_{\mathrm{fl}}$ and the trace statement is the statement that $\tilde\Sigma_\Psi$ has a fixed $\natural$ norm structure under the boost.**

### The entropy

**The entropy density carries one factor of $\gamma$ and the total entropy is a scalar.** The entropy is the temporal component of the entropy current, so under a boost along the flow

$$
s_{\mathrm{ent}}=\gamma\,s_{\mathrm{ent,rest}},
\qquad
S=\int d^{3}r\;s_{\mathrm{ent}}=\text{scalar},
$$

the second statement being the standard one that the total entropy of an isolated system is frame-independent: the density grows by $\gamma$ and the volume contracts by $1/\gamma$, and the two cancel. **The cancellation is the reason the second law can be stated in any frame**, and it is the reason [The Local Entropy Current](the-local-entropy-current.html) can write its inequality with a scalar reading and no frame label.

**One caution, in the corpus's letters.** The entropy density $s_{\mathrm{ent}}$ and the total entropy $S$ share a letter with the action and with the spin element, and the corpus's rule is that every occurrence is labelled. The table above uses $s_{\mathrm{ent}}$ throughout, and the total entropy appears only in the display where it is called $S$ with no subscript and the context is the integral.

### The free energy

**The free energy is a scalar because $Z$ is a scalar and $\beta$ is a scalar, and this is the sharpest contrast with the energy density.** With $F=-(1/\beta)\log Z$ and both $Z$ and $\beta$ invariant,

$$
F_{\mathrm{obs}}=F_{\mathrm{rest}}=-\,p_{\mathrm{th}}\,V_{0},
$$

where the second equality is the standard relativistic identification of the free energy with minus the pressure times the *proper* volume, and both factors on the right are scalars. **So the free energy is invariant for the same reason the pressure is**: it is $-p_{\mathrm{th}}$ times a volume measured in the fluid's own frame, and a boost changes neither.

**The density-level identity is where a reader goes wrong, and the article says how.** The relation $F=E-TS$ holds in the rest frame with the rest-frame $E$ and $S$. In a moving frame the energy *density* is the $\gamma^{2}$ combination and the entropy *density* is $\gamma$ times the rest value, and substituting those into $E-TS$ does not return $F$: at $\gamma=2$, with $w_{\mathrm{fl,rest}}=1$, $p_{\mathrm{th}}=1/3$, $s_{\mathrm{ent,rest}}=1$ and $T=1$ in the rest frame, the substitution gives $5-\tfrac12\cdot2=4$ whereas the invariant value is $-p_{\mathrm{th}}V_{0}=-1/3$. **The discrepancy is not an error and it is not a paradox**: the boosted densities carry the $pV$ work of the boost, and $E-TS$ is only a scalar when its three terms are contracted with the same flow — which is what makes $F$ a scalar in the first place. A reader who wants the frame-independent statement should use $F=-p_{\mathrm{th}}V_{0}$ and not the density identity.

## Numerical Checks

**Four identities were checked numerically, and the results are reported here because a reader cannot check them from the displays alone.**

- **The contraction's frame independence.** For $\beta_{\mathrm{vel}}=0.6$, $0.8$ and $0.979\,795\,897$, the split $\beta\gamma(E/c-\vec\beta_{\mathrm{vel}}\cdot\vec p)$ was evaluated on the flow's own momentum with $E=\gamma mc^{2}$ and $\vec p=\gamma m\vec v$. The bracket is $\gamma mc(1-\beta_{\mathrm{vel}}^{2})=mc/\gamma$ to fifteen digits at each velocity, so the product $\beta\gamma\,mc/\gamma=\beta mc$ is the same at all three and equals the value the norm computation gives. **The check is a check of the split and not of the norm**, and the two agree because $1-\beta_{\mathrm{vel}}^{2}=1/\gamma^{2}$ is what the arithmetic uses.
- **The product $\beta_{\mathrm{obs}}T_{\mathrm{obs}}=\beta T$** at the three velocities of the table: constant to twelve decimal places, as printed.
- **The entropy density's factor.** $s_{\mathrm{ent}}/(\gamma\,s_{\mathrm{ent,rest}})=1$ to twelve places at each velocity, the ratio being $\gamma/\gamma$ by construction — a trivial check, recorded because a reader can reproduce it in a line and because it is the check that catches a missing factor of $\gamma$ in the current's temporal slot.
- **The energy density's combination.** $(w_{\mathrm{fl}}+p_{\mathrm{th}})\gamma^{2}-p_{\mathrm{th}}$ returns $w_{\mathrm{fl}}$ exactly at $\gamma=1$ for each row, and returns $33.000\,000\,00$ at $\gamma=5$ for $w_{\mathrm{fl}}=1$, $p_{\mathrm{th}}=1/3$, as printed.

**What the checks do and do not establish.** They establish that the arithmetic of the boost's factors is what the displays say. They do not establish the physical identification of the temporal component with the observed period, which is a reading and not an arithmetic fact, and they do not establish the sign of the temperature transformation, which is a convention the corpus fixes once and this article inherits rather than argues.

## What Is Established and What Is Interpretation

**What is established, and is transcription.** That the thermal state of a moving fluid is specified by a thermal element $\tilde\beta_\Phi$ whose norm is $-\beta^{2}$ and whose direction is the flow's; that the thermal exponent is $-\beta_{\Phi,\nu}p_{\Phi,\nu}/\hbar$; that this contraction equals $\beta k_m$ in every frame; that the partition function is therefore frame-independent; that the observed period is the temporal component $i\beta\gamma$ and the observed temperature is $T/\gamma$; that the energy density is $(w_{\mathrm{fl}}+p_{\mathrm{th}})\gamma^{2}-p_{\mathrm{th}}$ with the pressure unchanged; that the entropy density carries a factor $\gamma$ and the total entropy is a scalar; that the free energy is $-p_{\mathrm{th}}V_{0}$ and is a scalar. **Every one of these is standard relativistic thermodynamics, and the article's contribution is the letters.** This is standard relativistic thermodynamics in the corpus's letters, with no framework interpretation.

**What is the corpus's reading, and is marked as such.** That the temperature is read from the temporal component of a *period* rather than from a boosted heat exchange, and hence that a moving body is observed cooler by $\gamma$. The alternative reading exists in the literature and is not an error; it is a different question, and the corpus's answer follows from taking $\beta$ as a length along a direction, which is how the thermal articles define it. **A reader who prefers the other reading will find that every display of this article survives with $T\gamma$ in place of $T/\gamma$**, except the temperature row of the table; nothing structural depends on the choice.

**What is not established here.** That the imaginary-time direction is compact — that is [The Local Thermal Structure: k_B as the Scale of Imaginary Time](the-local-thermal-structure-kb-as-the-scale-of-imaginary-time.html)'s and is quoted. That the trace is twice the scalar part — that is [The Partition Function in Biquaternionic Form](the-partition-function-in-biquaternionic-form.html)'s and is quoted. That the Matsubara condition has the bosonic/fermionic sign — that is [The Matsubara Thermal Formalism in Biquaternionic Form](the-matsubara-thermal-formalism-in-biquaternionic-form.html)'s. That a moving thermal state is stable and that its entropy is maximal — that is a question about the state and not about its frame, and it belongs to [Causal Dissipative Hydrodynamics in Biquaternionic Form](causal-dissipative-hydrodynamics-in-biquaternionic-form.html) and to [The Local Entropy Current](the-local-entropy-current.html).

**One thing the article deliberately does not do.** It does not discuss the case in which the boost is not uniform — a fluid whose flow varies from point to point, so that $\tilde\beta_\Phi$ is a field. That case is [The Local Thermal State of a Fluid](the-local-thermal-state-of-a-fluid.html)'s, and it requires the rigidity condition of [Covariant Local Equilibrium and Tolman Temperature](covariant-local-equilibrium-and-tolman-temperature.html) before the thermal element can be assigned pointwise. **Here the boost is uniform and the fluid is in equilibrium**, so the thermal element is a single element and not a field, and the article stays inside that case.

## Summary

The thermal state of a moving fluid is specified by a thermal element, $\tilde\beta_\Phi=(\beta/c)\tilde V_\Phi=\beta\gamma\left(ie_t+\vec\beta_{\mathrm{vel}}\right)$, an element of the material sector with norm $-\beta^{2}$: the period $\beta$ of [The Local Thermal Structure: k_B as the Scale of Imaginary Time](the-local-thermal-structure-kb-as-the-scale-of-imaginary-time.html), carried along the flow. Its components are $\beta_{\Phi,t}=i\beta\gamma$ and $\beta_{\Phi,\eta}=\beta\gamma\beta_{\mathrm{vel},\eta}$, every index low; the boost lengthens the norm not at all and tilts the direction by $\gamma$.

The thermal exponent is the contraction $-\beta_{\Phi,\nu}p_{\Phi,\nu}/\hbar=-(\beta/c\hbar)m\langle\tilde V_\Phi\rangle_{\natural}=\beta mc/\hbar=\beta k_m$, independent of $\gamma$ and of $\vec v$. The partition function is that trace, so $Z(\beta,\vec\beta_{\mathrm{vel}})=Z(\beta,\vec 0)$: **the moving frame has no partition function of its own**, and the rest-frame article is the special case $\vec\beta_{\mathrm{vel}}=0$. What the boost changes is the reading of $Z$, not its value.

The observed quantities follow from the components. The observed period is $\beta_{\mathrm{obs}}=\gamma\beta$ and the observed temperature $T_{\mathrm{obs}}=T/\gamma$, with $\beta_{\mathrm{obs}}T_{\mathrm{obs}}=\beta T$ checked constant to twelve decimal places at three velocities. The energy density is $(w_{\mathrm{fl}}+p_{\mathrm{th}})\gamma^{2}-p_{\mathrm{th}}$, the pressure is unchanged, the entropy density is $\gamma$ times the rest value, and the free energy is $-p_{\mathrm{th}}V_{0}$, a scalar. At $300\,\mathrm{K}$ and $\gamma=5$ the observer reads $60\,\mathrm{K}$, the energy density of an $w=3p$ fluid is $33$ times its rest value, and the entropy density is $5$ times.

On the imaginary-time side the Matsubara condition becomes periodicity along the tilted thermal element, $\tilde\Xi(\tilde R_\Phi+\tilde\beta_\Phi)=\pm\tilde\Xi(\tilde R_\Phi)$, so the thermal circle is tilted in any frame where the fluid moves, and the invariant statement is the contraction $k_{\Phi,\nu}\beta_{\Phi,\nu}=2\pi n$ and not the spacing $2\pi n/\beta$.

The article is transcription: standard relativistic thermodynamics in the corpus's letters, with no framework interpretation. It adds the boost, the frame dependence of the thermal element, and the statement that $Z$ is a scalar — and nothing else.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\beta=\frac{\hbar}{k_{B}\,T}$ | Inverse temperature, the imaginary-time circumference; a length |
| $c\beta=\frac{\hbar\,c}{k_{B}\,T}$ | The same span in the material sector's units |
| $T$ | Temperature |
| $k_B$ | Boltzmann's constant |
| $\tilde\beta_\Phi$ | Thermal element of the moving state |
| $\tilde\beta_{\Phi,0}=\beta ie_t$ | Thermal element of the rest frame |
| $\beta_{\Phi,t}=i\beta\gamma$, $\beta_{\Phi,\eta}$ | Its components, index low |
| $\beta_{\mathrm{obs}}=\gamma\beta$ | Period the boosted observer measures |
| $T_{\mathrm{obs}}=T/\gamma$ | Temperature the boosted observer measures |
| $\tilde V_\Phi$ | Flow (velocity) element, $\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}$ |
| $\vec v$, $\vec\beta_{\mathrm{vel}}=\vec v/c$ | Velocity and its dimensionless form |
| $\gamma=(1-\beta_{\mathrm{vel}}^{2})^{-1/2}$ | Boost factor |
| $p_{\Phi,\nu}$ | Flow momentum components, $p_{\Phi,t}=iE/c$ |
| $E$ | Energy |
| $m$, $c$ | Mass and speed of light in the medium |
| $\hbar$ | Action quantum |
| $k_m$ | Mass wave number |
| $Z$ | Partition function, a scalar |
| $F=-(1/\beta)\log Z=-p_{\mathrm{th}}V_{0}$ | Free energy, a scalar |
| $V_{0}$ | Proper volume |
| $w_{\mathrm{fl}}$ | Energy density; its rest value is $w_{\mathrm{fl,rest}}$ |
| $p_{\mathrm{th}}$, $p_{\mathrm{th,rest}}$ | Thermal pressure, unchanged by the boost; the suffix marks the rest-frame value |
| $s_{\mathrm{ent}}$, $s_{\mathrm{ent,rest}}$ | Entropy density, $\gamma$ times its rest value |
| $S$ | Total entropy, a scalar |
| $\tilde\Sigma_\Psi=w_{\mathrm{fl}}e_t+\tfrac{i}{c}\vec S_{\mathrm P}$ | Energy–momentum element |
| $\tilde R_\Phi$ | Material four-position |
| $r'_t$ | Temporal coordinate, a length |
| $k_{\Phi,\nu}$ | Wave-vector components of a mode |
| $\mathrm{Sc}$ | Scalar part |
| $\langle\ \rangle_{\natural}$ | Quaternionic norm |
| $\mathbb{B}_\Phi$, $\mathbb{B}_\Psi$ | Material and informational sectors |

## Further Reading

- M. Planck, "Zur Dynamik bewegter Systeme," *Annalen der Physik* **26** (1908) 1–34, the original transformation of the thermodynamic quantities.
- A. Einstein, "Über das Relativitätsprinzip und die aus demselben gezogenen Folgerungen," *Jahrbuch der Radioaktivität und Elektronik* **4** (1907) 411–462, for the moving-body thermodynamics of the same period.
- H. Ott, "Lorentz-Transformation der Wärme und der Temperatur," *Zeitschrift für Physik* **175** (1963) 70–104, for the alternative reading of the temperature transformation.
- N. G. van Kampen, "Relativistic thermodynamics of moving systems," *Physical Review* **173** (1968) 295–301, for the covariant formulation that avoids the temperature paradox.
- C. K. Yuen, "Lorentz transformation of thermodynamic quantities," *American Journal of Physics* **38** (1970) 246–252, for the comparison of the readings.
- W. Israel, "Thermodynamics of relativistic systems," *Physica A* **106** (1981) 204–214, for the covariant thermal element and its equilibrium conditions.
- W. Israel, "Relativistic Thermodynamics, Thermofield Statistics and Superfluids," *Journal of Non-Equilibrium Thermodynamics* **11** (1986) 295, for the thermal element in the presence of a flow.
- N. P. Landsman and Ch. G. van Weert, "Real- and imaginary-time field theory at finite temperature and density," *Physics Reports* **145** (1987) 141–249, for the imaginary-time formulation and the tilted contour.
- J. I. Kapusta and C. Gale, *Finite-Temperature Field Theory: Principles and Applications* (Cambridge University Press, 2006), for the Matsubara formalism in the standard notation.
- The companion articles: [The Partition Function in Biquaternionic Form](the-partition-function-in-biquaternionic-form.html), [The Local Thermal Structure: k_B as the Scale of Imaginary Time](the-local-thermal-structure-kb-as-the-scale-of-imaginary-time.html), [The Matsubara Thermal Formalism in Biquaternionic Form](the-matsubara-thermal-formalism-in-biquaternionic-form.html), and [Covariant Local Equilibrium and Tolman Temperature](covariant-local-equilibrium-and-tolman-temperature.html).
