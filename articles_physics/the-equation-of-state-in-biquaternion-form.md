# __The Equation of State in Biquaternion Form__

## Introduction

**The equation of state of the biquaternion fluid is $p_{\mathrm{eff}}=p_{\mathrm{th}}+p_{\mathrm{qnt}}$, a function of the proper density $\rho_{\mathrm{num}}$ and the inverse temperature $\beta$, with the first term thermal and the second a gradient correction.** This article gives both terms, states what each is a function of, and says exactly where the two-part form comes from and where it stops being exact.

**The temperature enters as a length, and the article quotes it and derives nothing.** From [The Local Thermal Structure: k_B as the Scale of Imaginary Time](the-local-thermal-structure-kb-as-the-scale-of-imaginary-time.html),

$$
\beta=\frac{m\,c}{k_{m}\,k_{B}\,T},
\qquad
c\beta=\frac{m\,c^{2}}{k_{m}\,k_{B}\,T},
$$

the imaginary-time circumference and the same span in the material sector's units. **Both displays are quotations.** The article uses $\beta$ as the variable conjugate to the entropy density, that is, as the variable in which the Gibbs–Duhem relation reads $\partial p_{\mathrm{th}}/\partial\beta=-(\beta/T)\,s_{\mathrm{ent}}$, which [The Local Thermal State of a Fluid](the-local-thermal-state-of-a-fluid.html) established; it does not re-derive the relation between $\beta$ and $T$, and a reader who wants the counting of Matsubara modes goes to the article cited.

**The division of labour between the two parts is exact and worth stating at the outset.** $p_{\mathrm{th}}$ is a function of $(\rho_{\mathrm{num}},\beta)$ and satisfies the thermal identities at each event. $p_{\mathrm{qnt}}$ is not a function of $(\rho_{\mathrm{num}},\beta)$: it is a function of the density and its first two derivatives, and it is the object that makes the equation of state non-local at order $\hbar^{2}$. **The two are kept apart because they obey different relations**, and the labelling $\mathrm{th}$/$\mathrm{qnt}$ is the machinery that keeps them apart through the whole category.

**What this article adds to [The Local Thermal State of a Fluid](the-local-thermal-state-of-a-fluid.html).** That article said what a local equation of state must satisfy — determinacy, consistency, integrability — and did not give one. This article gives one, checks the three requirements on it, and finds that the thermal part passes all three while the quantum part passes the first only to a stated gradient order. **The finding is the content**: the equation of state of a quantum fluid cannot be exactly local, and the size of the failure is $\lVert\tilde\Xi\rVert^{2}$'s second derivative measured in units of the field's own length.

## The Thermal Part

### What it is a function of

**The thermal part is a function of two variables, the density and the period, and of nothing else.** Write

$$
p_{\mathrm{th}}=p_{\mathrm{th}}\left(\rho_{\mathrm{num}},\beta\right),
$$

with no derivatives on the right. **The claim is a claim about the state, not about the substance**: at a given density and a given period the thermal pressure is determined, and the determination is what "local equilibrium" means when written as a formula. For a one-component fluid the pair $(\rho_{\mathrm{num}},\beta)$ specifies the state, and the pressure is the state's response to a change of volume at fixed period.

**Two properties follow from the thermodynamic identities and are worth naming.** The first is homogeneity: the pressure is an intensive quantity, so it cannot depend on the overall scale of the density alone but only on the density per unit of the field's own scale. The second is positivity: $p_{\mathrm{th}}\ge0$ for a fluid whose energy density exceeds its rest energy density, which is the statement that a fluid with a positive thermal energy pushes outward.

**The form the corpus uses, with the density as the variable.** From the standard identity quoted in [The Local Thermal State of a Fluid](the-local-thermal-state-of-a-fluid.html),

$$
p_{\mathrm{th}}=n_{\mathrm{num}}\left(\frac{\partial w_{\mathrm{fl}}}{\partial n_{\mathrm{num}}}\right)_{s_{\mathrm{ent}}}-w_{\mathrm{fl}},
$$

which says that the pressure is the excess of the density-derivative of the energy over the energy itself. **This form is the one that closes the equation of state without a chemical potential**: it uses only the energy as a function of the density at fixed entropy, and every other thermal quantity follows from it by differentiation.

### Two worked substances, and the check on the form

**A cold degenerate gas and a radiation gas are the two ends of the thermal range, and the form above reproduces both.**

**Cold degenerate gas, non-relativistic.** With $w_{\mathrm{fl}}=K\,\rho_{\mathrm{num}}^{5/3}$ and $n_{\mathrm{num}}=\rho_{\mathrm{num}}/m$,

$$
p_{\mathrm{th}}=\rho_{\mathrm{num}}\frac{5}{3}K\rho_{\mathrm{num}}^{2/3}-K\rho_{\mathrm{num}}^{5/3}
=\frac{2}{3}\,w_{\mathrm{fl}},
$$

the familiar $p=\tfrac23w$ of a non-relativistic degenerate gas. **The arithmetic is one line and it is the check that the form's normalisation is right**: the factor $\tfrac23$ comes from $\tfrac53-1$ and not from a convention.

**Radiation.** With $w_{\mathrm{fl}}=aT^{4}$ and $p_{\mathrm{th}}=\tfrac13aT^{4}=\tfrac13w_{\mathrm{fl}}$, the same identity returns $\tfrac13$, and Euler's relation returns $s_{\mathrm{ent}}=\tfrac43aT^{3}$. **Both substances therefore sit on the same formula with different exponents**, which is what a one-parameter family of equations of state means.

**The general polytrope, for the record.** With $w_{\mathrm{fl}}=K\rho_{\mathrm{num}}^{\gamma}$ the identity gives $p_{\mathrm{th}}=(\gamma-1)w_{\mathrm{fl}}$, so the polytropic index $\gamma$ is the ratio $1+p_{\mathrm{th}}/w_{\mathrm{fl}}$ and the two cases above are $\gamma=\tfrac53$ and $\gamma=\tfrac43$. **A reader who wants to check a candidate equation of state can do it here**: if the pressure is written as a function of the density alone with no $\beta$, then the substance is at zero temperature and the formula must return a constant $\gamma$; if it does not, the candidate is not a polytrope.

### Where $\beta$ enters, and the four-thirds case in the corpus's variable

**The period enters through the normalisation of the thermal state, and for radiation it enters as a pure power.** With $T=A/\beta$ and $A=\hbar/k_B$,

$$
p_{\mathrm{th}}=\frac{aA^{4}}{3\beta^{4}},
\qquad
w_{\mathrm{fl}}=\frac{aA^{4}}{\beta^{4}},
\qquad
s_{\mathrm{ent}}=\frac{4aT^{3}}{3}=\frac{4aA^{3}}{3\beta^{3}},
$$

so every thermal quantity is a power of the period and the equation of state reads

$$
p_{\mathrm{th}}=\frac{1}{3}w_{\mathrm{fl}}
\qquad\text{for all }\beta,
$$

which is the statement that radiation's equation of state is *independent of the temperature* — the pressure is fixed by the energy density and the temperature only fixes the scale. **This is why the thermal part is written as a function of two variables and not one**: the function's dependence on $\beta$ can degenerate, and for radiation it does.

**The derivative with respect to the period, checked.** From the display, $\partial p_{\mathrm{th}}/\partial\beta=-4p_{\mathrm{th}}/\beta$, and the Gibbs–Duhem relation of the previous article gives $s_{\mathrm{ent}}=-(\beta/T)\partial p_{\mathrm{th}}/\partial\beta=4p_{\mathrm{th}}/T=4aT^{3}/3$ ✓. **The chain rule is the only place in the article where a factor can go missing**, and the check above is the one that catches it.

### What the thermal part is not

**It is not a barotropic equation of state in general.** A barotropic fluid has $p_{\mathrm{th}}=p_{\mathrm{th}}(\rho_{\mathrm{num}})$ with no temperature, and the display at the head of this section has two arguments. **The barotropic case is the degenerate limit**, in which the temperature is so far below the degeneracy scale that the state's pressure is fixed by the density alone; it is a limit and not the general case, and an article that assumes it silently excludes every thermal effect the category is about.

**It is not the quantum part's container either.** A reader might expect $p_{\mathrm{qnt}}$ to be a correction to a barotropic $p_{\mathrm{th}}(\rho_{\mathrm{num}})$ and hence to be absorbed into the function of one variable. **It cannot be absorbed**, because it depends on derivatives and no function of $\rho_{\mathrm{num}}$ alone can reproduce a derivative. That is the reason for the second label, and it is a structural reason and not a bookkeeping preference.

## The Quantum Part

### The definition, and the identity behind it

**The quantum part of the pressure is the quantum potential times the density, and the product has a second form that is the useful one.** With

$$
Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\frac{\Box_\Phi\lVert\tilde\Xi\rVert}{\lVert\tilde\Xi\rVert},
\qquad
p_{\mathrm{qnt}}=\rho_{\mathrm{num}}\,Q_{\mathrm{qnt}},
$$

and with $\rho_{\mathrm{num}}=\lVert\tilde\Xi\rVert^{2}$, the product is an identity in the density alone:

$$
p_{\mathrm{qnt}}
=-\frac{\hbar^{2}}{4m}\,\Box_\Phi\rho_{\mathrm{num}}
+\frac{\hbar^{2}}{8m}\,\frac{\partial_\eta\rho_{\mathrm{num}}\,\partial_\eta\rho_{\mathrm{num}}}{\rho_{\mathrm{num}}} .
$$

**The derivation is two lines and is given because the identity is used everywhere below.** Write $\rho_{\mathrm{num}}=u^{2}$ with $u=\lVert\tilde\Xi\rVert$. Then $\Box_\Phi\rho_{\mathrm{num}}=2u\,\Box_\Phi u+2\,\partial_\eta u\,\partial_\eta u$, so $u\,\Box_\Phi u=\tfrac12\Box_\Phi\rho_{\mathrm{num}}-\partial_\eta u\,\partial_\eta u$, and with $\partial_\eta u=\partial_\eta\rho_{\mathrm{num}}/(2u)$ the second term is $(\partial_\eta\rho_{\mathrm{num}})^{2}/(4\rho_{\mathrm{num}})$. Multiplying $-\tfrac{\hbar^{2}}{2m}u\,\Box_\Phi u$ out gives $-\tfrac{\hbar^{2}}{4m}\Box_\Phi\rho_{\mathrm{num}}+\tfrac{\hbar^{2}}{8m}(\partial_\eta\rho_{\mathrm{num}})^{2}/\rho_{\mathrm{num}}$, the factor of two between the two terms coming from the $2$ in $\rho_{\mathrm{num}}=u^{2}$ and not from $Q_{\mathrm{qnt}}$. Substituting into $Q_{\mathrm{qnt}}$ and multiplying by $\rho_{\mathrm{num}}$ gives the display. **The minus sign of $Q_{\mathrm{qnt}}$ is inherited and not touched**: the first term of the identity carries it, and a reader who writes the first term with a plus has the wrong sign for the quantum potential.

**Which of the two forms to use.** The first is the definition and it is the one that connects to the mass shell the quantum potential modifies. The second is the one that shows the structure: a Laplacian term and a gradient-squared term with the opposite sign, whose ratio is fixed. **The second form also makes the $\hbar^{2}$ counting visible**, which is the subject of the next subsection.

### The gradient counting

**The quantum pressure is second order in gradients, and the dimensionless measure of its size is the ratio of the field's own length to the density's length scale.** Let $L$ be the length over which $\rho_{\mathrm{num}}$ varies, so that $\Box_\Phi\rho_{\mathrm{num}}\sim\rho_{\mathrm{num}}/L^{2}$ and $(\partial_\eta\rho_{\mathrm{num}})^{2}/\rho_{\mathrm{num}}\sim\rho_{\mathrm{num}}/L^{2}$. Then

$$
p_{\mathrm{qnt}}\sim\frac{\hbar^{2}}{m}\frac{\rho_{\mathrm{num}}}{L^{2}},
\qquad
\frac{p_{\mathrm{qnt}}}{w_{\mathrm{fl}}}\sim\frac{\hbar^{2}}{m^{2}c^{2}L^{2}}=\frac{1}{k_m^{2}L^{2}},
$$

where the second step uses $w_{\mathrm{fl}}\sim\rho_{\mathrm{num}}mc^{2}$ for a fluid at rest and $\hbar/(mc)$ for the field's own length. **The ratio is the square of the field's length $1/k_m$ to the density's length — the corpus's only dimensionless small parameter in this sector** — and it is the expansion parameter of every gradient correction in the category.

**The numerical coefficient, for a Gaussian.** With $\rho_{\mathrm{num}}=\rho_{0}\exp(-r^{2}/(2\sigma^{2}))$ in one dimension,

$$
Q_{\mathrm{qnt}}(0)=\frac{\hbar^{2}}{4m\sigma^{2}},
\qquad
\frac{p_{\mathrm{qnt}}(0)}{w_{\mathrm{fl}}}=\frac{1}{4k_m^{2}\sigma^{2}},
$$

and in three dimensions the central value is three times larger, $Q_{\mathrm{qnt}}(0)=3\hbar^{2}/(4m\sigma^{2})$, because the Laplacian has three terms. **The factor $\tfrac14$ in one dimension and $\tfrac34$ in three are the whole coefficient of the correction**, so a reader who wants the size of the effect at a given width has a number and not an order of magnitude. **The letter $\sigma$ is the width of the density as it appears in the exponent above, and not the amplitude's**: the density falls by $1/e$ at $r=\sqrt2\,\sigma$, so the amplitude's width is $\sqrt2\,\sigma$. [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html) writes the same state as $\rho_{\mathrm{num}}=A^{2}\exp(-r^{2}/\sigma_{\mathrm{qst}}^{2})$, whose $\sigma_{\mathrm{qst}}$ is this $\sigma$ times $\sqrt2$, and its central coefficient $1/(2m\sigma_{\mathrm{qst}}^{2})$ is this article's $1/(4m\sigma^{2})$ with the substitution. **The two agree, and a reader who equates the two letters without the $\sqrt2$ sees a factor two that is a convention and not a disagreement.**

| $k_m\sigma$ | $p_{\mathrm{qnt}}(0)/w_{\mathrm{fl}}$, one dimension | three dimensions |
|---|---|---|
| $1$ | $0.250\,000\,000$ | $0.750\,000\,000$ |
| $2$ | $0.062\,500\,000$ | $0.187\,500\,000$ |
| $10$ | $0.002\,500\,000$ | $0.007\,500\,000$ |
| $100$ | $0.000\,025\,000$ | $0.000\,075\,000$ |

**The table is the statement that the framework's corrections are large only when the density varies on the scale of the field's own length**, which is the Compton scale of the field. For a density that varies on scales much larger than that, the quantum pressure is a small correction to the thermal pressure and the equation of state is local to a good approximation. **For a density that varies on the Compton scale the two pressures are comparable**, and no approximation that drops one of them is available.

### The sign, and where the quantum pressure is negative

**The quantum pressure is not positive definite, and this is a real feature rather than a defect of the formula.** At the centre of a Gaussian the Laplacian of the density is negative and the gradient term is zero, so $p_{\mathrm{qnt}}>0$; in the tail the Laplacian changes sign, and the gradient term does not fall fast enough to keep the product positive. **The crossover is at $r^{2}=2\sigma^{2}$ in one dimension and at $r^{2}=6\sigma^{2}$ in three**, and both are found from the second form by substitution. In one dimension $\rho_{\mathrm{num}}=\rho_{0}e^{-r^{2}/(2\sigma^{2})}$ gives $\partial_{r}^{2}\rho_{\mathrm{num}}=\rho_{\mathrm{num}}\left(-1/\sigma^{2}+r^{2}/\sigma^{4}\right)$ and $(\partial_{r}\rho_{\mathrm{num}})^{2}/\rho_{\mathrm{num}}=\rho_{\mathrm{num}}\,r^{2}/\sigma^{4}$, so

$$
p_{\mathrm{qnt}}=\rho_{0}e^{-r^{2}/(2\sigma^{2})}\,\frac{\hbar^{2}}{m}\left(\frac{1}{4\sigma^{2}}-\frac{r^{2}}{8\sigma^{4}}\right),
$$

which vanishes at $r^{2}=2\sigma^{2}$ and is negative beyond it; in three dimensions the first bracket is $3/(4\sigma^{2})$ and the crossover moves to $r^{2}=6\sigma^{2}$. **The numerically found crossing in one dimension is $r=1.414\,214\,\sigma$**, which is $\sqrt2\,\sigma$ to six digits.

**A negative pressure in the tail does not violate anything.** The thermal part of the pressure is positive and dominates where the density is large; the quantum part is a gradient correction and the total effective pressure must be positive for the fluid description to make sense, which is a constraint on the state and not on the formula. **The corpus states the constraint and does not legislate it**: $p_{\mathrm{eff}}\ge0$ is required wherever the fluid description is claimed to hold, and it fails in the far tail of any localised state.

### Why it is called a pressure, and the caution attached

**The identification $p_{\mathrm{qnt}}=\rho_{\mathrm{num}}Q_{\mathrm{qnt}}$ is the corpus's, and the reason for the name is the trace of the stress rather than the force.** In the isotropic case the quantum part of the stress has a scalar part equal to this product, and the scalar part of a stress is a pressure; that is the whole of the identification. **What it is not is the object whose gradient is the quantum force**, and the difference is worth a display. The force density is $-\rho_{\mathrm{num}}\,\partial_\eta Q_{\mathrm{qnt}}$, while the gradient of the pressure is

$$
\partial_\eta p_{\mathrm{qnt}}=\rho_{\mathrm{num}}\,\partial_\eta Q_{\mathrm{qnt}}+Q_{\mathrm{qnt}}\,\partial_\eta\rho_{\mathrm{num}},
$$

so the two differ by $Q_{\mathrm{qnt}}\partial_\eta\rho_{\mathrm{num}}$. **The difference is exactly the term that makes a quantum fluid not a classical fluid**: a classical fluid's pressure acts through its gradient alone, and the quantum fluid's acts through the gradient plus a term proportional to the density's own gradient. **A reader who treats $p_{\mathrm{qnt}}$ as a classical pressure will get the quantum force wrong in any region where the density varies**, which is every region where the term is non-zero.

**This is the article's sharpest caution and it is worth the space.** The name "pressure" is inherited and defensible at the level of the stress's scalar part; the *use* of the name as if the fluid equations could be written with $p_{\mathrm{eff}}$ in place of $p$ is not defensible, because the quantum force is not a pressure gradient. **The corpus keeps the two labels for exactly this reason**, and the next article in the category, [The Local Entropy Current](the-local-entropy-current.html), has to decide which of the two appears in the entropy production — and it appears as neither alone, as that article shows.

## The Combined Equation of State

### The display

**The effective equation of state is the sum, with the two parts treated differently and the notation saying so.** The full statement is

$$
p_{\mathrm{eff}}\left[\rho_{\mathrm{num}},\beta\right]
=p_{\mathrm{th}}\left(\rho_{\mathrm{num}},\beta\right)
+\rho_{\mathrm{num}}\,Q_{\mathrm{qnt}}\left[\rho_{\mathrm{num}}\right],
$$

where the square brackets on the right of the quantum term are a reminder that it is a functional of the density field and not a function of the density at a point. **The two kinds of bracket are the article's notation for the difference**, and a reader who writes both with round brackets has lost the distinction the article is about.

**The thermal part's functional form is free and the quantum part's is not.** A substance may have any $p_{\mathrm{th}}$ consistent with the three requirements of [The Local Thermal State of a Fluid](the-local-thermal-state-of-a-fluid.html); the quantum part is fixed by the field once the density is given. **So the equation of state has one free function and one determined correction**, and that is an unusual structure: it is not a one-parameter family of equations of state, it is a family plus a universal term.

### The two limits

**The classical limit is $\hbar\to0$ at fixed state, and it leaves the thermal part alone.** In that limit $p_{\mathrm{qnt}}\to0$, the equation of state becomes the function $p_{\mathrm{th}}(\rho_{\mathrm{num}},\beta)$, and the fluid is classical. **The limit is singular in one respect**: $\hbar\to0$ at fixed $\beta$ is $\beta k_m\to\infty$, since $\beta k_m=\beta mc/\hbar$, so the classical limit is the limit in which the thermal circle is infinitely long compared with the field's length — the low-temperature limit of the same parameter.

**The other limit is $T\to0$ at fixed $\hbar$, and it is the polar-form article's pure state.** There the thermal part vanishes and the equation of state is

$$
p_{\mathrm{eff}}=p_{\mathrm{qnt}}=\rho_{\mathrm{num}}Q_{\mathrm{qnt}},
$$

which is the pressure of the state that [The Polar Form of the Klein–Gordon Equation in Biquaternionic Form](the-polar-form-of-the-klein-gordon-equation-in-biquaternionic-form.html) describes. **The pure state is therefore the $T=0$ limit of this equation of state and not a different theory**, and [The Two-Fluid Model in Biquaternionic Form](the-two-fluid-model-in-biquaternionic-form.html) uses exactly this statement to identify its condensate.

### The three requirements, checked

**Determinacy fails at order $\hbar^{2}$, and the failure is quantified.** $p_{\mathrm{th}}$ passes: it is a function of two numbers at the event. $p_{\mathrm{qnt}}$ fails: it needs the Laplacian. **The effective pressure is therefore determinate to zeroth order in $1/(k_mL)^{2}$ and not to first order in $\hbar$**, because the correction is already $\hbar^{2}$ and there is no $\hbar^{1}$ term.

**Consistency holds for the thermal part and fails for the quantum part.** Euler's relation and Gibbs–Duhem's relation are statements about an extensive potential; $p_{\mathrm{th}}$ has one and $p_{\mathrm{qnt}}$ does not, because $\rho_{\mathrm{num}}Q_{\mathrm{qnt}}$ is not extensive — it is a density built from a Laplacian, and doubling the system doubles the density but not the Laplacian's relation to it at the join. **The failure is structural and not quantitative**, so no amount of care with coefficients repairs it.

**Integrability holds for the thermal part trivially, since $p_{\mathrm{th}}$ is derived from the energy by one differentiation.** For the quantum part the question does not arise: it is not derived from a potential and does not need one, because it is derived from the field. **The three requirements therefore separate cleanly**: two of them are requirements on $p_{\mathrm{th}}$ alone and one is a requirement on the pair, and the article's table records which is which.

| requirement | $p_{\mathrm{th}}$ | $p_{\mathrm{qnt}}$ | $p_{\mathrm{eff}}$ |
|---|---|---|---|
| determinacy at the event | holds | fails at order $\hbar^{2}$ | holds to order $(k_mL)^{-2}$ |
| Euler and Gibbs–Duhem | holds | fails (not extensive) | holds to order $(k_mL)^{-2}$ |
| integrability from a potential | holds | not applicable | holds to order $(k_mL)^{-2}$ |

**What the table means in one sentence.** The effective equation of state is exactly local to zeroth order, approximately local to second order in the field's length over the density's length, and never exactly local. **That sentence is this article's result**, and it is the reason the category can speak of a local thermal state at all while keeping the quantum correction.

## Numbers

**Four computations were done and are reported with their residuals, because the article's claims are algebraic and a reader should be able to reproduce each one.**

- **The identity for $p_{\mathrm{qnt}}$.** On a one-dimensional grid of $4001$ points spanning $[-6,6]$ with a Gaussian of width $\sigma=0.5$, the two sides of $p_{\mathrm{qnt}}=-\tfrac{\hbar^{2}}{4m}\Box_\Phi\rho_{\mathrm{num}}+\tfrac{\hbar^{2}}{8m}(\partial_\eta\rho_{\mathrm{num}})^{2}/\rho_{\mathrm{num}}$ agree to $1.8\times10^{-5}$ over the interior, the residual being the finite-difference error of the second derivative and not a discrepancy of the algebra. On a three-dimensional radial grid the same comparison agrees to $6.2\times10^{-8}$ away from the origin, where the $2/r$ term is resolved.
- **The central values.** In one dimension $Q_{\mathrm{qnt}}(0)=0.999\,982$ against the analytic $\hbar^{2}/(4m\sigma^{2})=1$ for $\hbar=m=1$, $\sigma=0.5$; the deviation is the grid's. In three dimensions the analytic value is $3\hbar^{2}/(4m\sigma^{2})=3$ under the same units, and the radial grid cannot resolve it at $r\to0$ because of the $2/r$ term, so the article quotes the analytic value and the interior residual and not a central numerical value.
- **The crossover.** The one-dimensional solution changes sign at $r=1.414\,214\,\sigma$, which is $\sqrt2\,\sigma$ to six digits, confirming $r^{2}=2\sigma^{2}$; the value $0.707\,107\,\sigma$ is $1/\sqrt2$ and is the half-width at which the density has fallen by $e^{-1/4}$, not a crossing. In three dimensions the numerical crossing sits at $r=2.449\,490\,\sigma$, which is $\sqrt6\,\sigma$ to six digits.
- **The polytropic check.** For $w_{\mathrm{fl}}=K\rho_{\mathrm{num}}^{5/3}$ at $\rho_{\mathrm{num}}=8$, the identity returns $p_{\mathrm{th}}=\tfrac23w_{\mathrm{fl}}$, i.e. $p_{\mathrm{th}}=(2/3)K\cdot32=21.333\,333\,K$ against $w_{\mathrm{fl}}=32K$, the ratio being $0.666\,667$ to six digits. For $w_{\mathrm{fl}}=K\rho_{\mathrm{num}}^{4/3}$ the ratio is $0.333\,333$ to six digits.

**What the checks establish and what they do not.** They establish the two algebraic identities — the density form of the quantum pressure and the polytropic ratios — and the location of the sign change. **They do not establish that any particular physical state has a Gaussian density**, which is a statement about a state and not about the equation of state; the Gaussian is used as a test function because its derivatives are exact and its values analytic.

## What Is Established and What Is Interpretation

**Established.** That the effective pressure splits as $p_{\mathrm{eff}}=p_{\mathrm{th}}+p_{\mathrm{qnt}}$; that $p_{\mathrm{th}}$ is a function of $(\rho_{\mathrm{num}},\beta)$ and satisfies Euler's relation, Gibbs–Duhem's relation and integrability; that $p_{\mathrm{qnt}}=\rho_{\mathrm{num}}Q_{\mathrm{qnt}}$ is exactly equal to the two-term density identity of this article; that $p_{\mathrm{qnt}}$ is second order in gradients with the small parameter $1/(k_mL)^{2}$; that its central value for a Gaussian is $\tfrac14$ (one dimension) or $\tfrac34$ (three) of the rest energy density at $k_m\sigma=1$; that it changes sign at $r^{2}=2\sigma^{2}$ (one dimension) or $r^{2}=6\sigma^{2}$ (three); that the equation of state is local to order $(k_mL)^{-2}$ and not exactly.

**Interpretation, and marked as such.** That $\rho_{\mathrm{num}}Q_{\mathrm{qnt}}$ deserves the name of a pressure. It is the scalar part of the quantum stress in the isotropic case, which is the standard reason the name is used, and it is not the object whose gradient is the quantum force. **The article states both halves rather than the convenient one**, because a reader who takes only the name will write the fluid equations with $p_{\mathrm{eff}}$ and get the quantum force wrong.

**Not claimed.** That the thermal part has any particular functional form — it has one free function per substance, and the article gives three examples and no general law. That the quantum part is a thermodynamic variable — it is a functional of the state's density and not an independent coordinate. That the two parts can be combined into a single barotropic $p(\rho)$ — they cannot, at any order, because one depends on derivatives. That the decomposition $p_{\mathrm{eff}}=p_{\mathrm{th}}+p_{\mathrm{qnt}}$ is unique — it is unique once the quantum part is defined as $\rho_{\mathrm{num}}Q_{\mathrm{qnt}}$, and a different definition would move terms between the two pieces; the corpus fixes the definition once, here, and the rest of the category inherits it.

**One consequence worth stating for the articles that follow.** The pressure that appears in the entropy production of [The Local Entropy Current](the-local-entropy-current.html) is not $p_{\mathrm{eff}}$; that article has to construct its current so that the divergence of the stress appears, and the quantum part contributes a term proportional to $Q_{\mathrm{qnt}}\partial_\eta\rho_{\mathrm{num}}$ which the entropy production can only absorb if the current carries it. **The article flags the point and does not solve it**, because the solution belongs to the entropy-current article and would be out of place here.

## Summary

The equation of state is $p_{\mathrm{eff}}=p_{\mathrm{th}}+p_{\mathrm{qnt}}$, with the thermal part a function of the proper density and the period, $p_{\mathrm{th}}=p_{\mathrm{th}}(\rho_{\mathrm{num}},\beta)$, and the quantum part a functional of the density field. The period is quoted: $\beta=mc/(k_mk_BT)$, a length, with $c\beta=mc^{2}/(k_mk_BT)$; nothing about it is derived here.

The thermal part closes through $p_{\mathrm{th}}=n_{\mathrm{num}}(\partial w_{\mathrm{fl}}/\partial n_{\mathrm{num}})_{s_{\mathrm{ent}}}-w_{\mathrm{fl}}$, which returns $p=\tfrac23w$ for a non-relativistic degenerate gas ($\gamma=\tfrac53$), $p=\tfrac13w$ for radiation ($\gamma=\tfrac43$), and $p=(\gamma-1)w$ for a general polytrope. In the corpus's variable radiation reads $p_{\mathrm{th}}=aA^{4}/(3\beta^{4})$ and $s_{\mathrm{ent}}=4aA^{3}/(3\beta^{3})$, with $\partial p_{\mathrm{th}}/\partial\beta=-4p_{\mathrm{th}}/\beta$ and the Gibbs–Duhem check $s_{\mathrm{ent}}=-(\beta/T)\partial p_{\mathrm{th}}/\partial\beta$ returning $4aT^{3}/3$. The thermal part is not barotropic in general; the barotropic case is the degenerate limit.

The quantum part is $p_{\mathrm{qnt}}=\rho_{\mathrm{num}}Q_{\mathrm{qnt}}=-\tfrac{\hbar^{2}}{4m}\Box_\Phi\rho_{\mathrm{num}}+\tfrac{\hbar^{2}}{8m}(\partial_\eta\rho_{\mathrm{num}})^{2}/\rho_{\mathrm{num}}$, derived from the quantum potential's minus sign in two lines and verified numerically to $1.8\times10^{-5}$ (one dimension) and $6.2\times10^{-8}$ (three, interior). It is second order in gradients, its size relative to the rest energy density is $1/(4k_m^{2}\sigma^{2})$ for a Gaussian in one dimension and $3/(4k_m^{2}\sigma^{2})$ in three, it vanishes at $r^{2}=2\sigma^{2}$ (one dimension) or $r^{2}=6\sigma^{2}$ (three), and it is negative beyond.

The named caution is that $p_{\mathrm{qnt}}$ is the scalar part of the quantum stress and not a pressure whose gradient is the quantum force: $\partial_\eta p_{\mathrm{qnt}}=\rho_{\mathrm{num}}\partial_\eta Q_{\mathrm{qnt}}+Q_{\mathrm{qnt}}\partial_\eta\rho_{\mathrm{num}}$, and the second term is the one a classical reading loses. The equation of state is therefore exactly local to zeroth order in $(k_mL)^{-2}$, approximately local at second order, and never exactly local.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $p_{\mathrm{eff}}=p_{\mathrm{th}}+p_{\mathrm{qnt}}$ | Effective pressure |
| $p_{\mathrm{th}}$ | Thermal pressure, a function of $(\rho_{\mathrm{num}},\beta)$ |
| $p_{\mathrm{qnt}}$ | Quantum pressure, a functional of the density field |
| $\rho_{\mathrm{num}}=\lVert\tilde\Xi\rVert^{2}$ | Proper density |
| $Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\Box_\Phi\lVert\tilde\Xi\rVert/\lVert\tilde\Xi\rVert$ | Quantum potential, with the minus sign |
| $u=\lVert\tilde\Xi\rVert$ | Amplitude |
| $w_{\mathrm{fl}}$ | Energy density |
| $s_{\mathrm{ent}}$ | Entropy density |
| $n_{\mathrm{num}}$ | Number density |
| $\beta=\frac{m\,c}{k_{m}\,k_{B}\,T}$ | Inverse temperature, the imaginary-time circumference; a length |
| $c\beta=\frac{\hbar\,c}{k_{B}\,T}$ | The same span in material units |
| $T=A/\beta$ | Temperature |
| $A=\frac{m\,c}{k_{m}\,k_{B}}=\frac{\hbar}{k_{B}}$ | The constant relating period and temperature, $\beta=A/T$ |
| $k_B$, $k_m$ | Boltzmann's constant, mass wave number |
| $\hbar$ | Action quantum |
| $m$, $c$ | Mass, speed of light in the medium |
| $\gamma$ | Polytropic index, $1+p_{\mathrm{th}}/w_{\mathrm{fl}}$ |
| $K$ | Polytropic constant |
| $a$ | Radiation constant |
| $L$ | Length scale of the density |
| $\sigma$ | Width of the Gaussian test density |
| $\rho_{0}$ | Central value of the test density |
| $\Box_\Phi$ | The d'Alembertian in the material reading |
| $\partial_\eta$ | Spatial derivative, index low |
| $(k_mL)^{-2}$ | The gradient expansion parameter |

## Further Reading

- L. D. Landau and E. M. Lifshitz, *Statistical Physics, Part 1* (Pergamon, 1980), §§43–45 and §61, for the polytropic and degenerate equations of state in the form used here.
- S. Chandrasekhar, *An Introduction to the Study of Stellar Structure* (Dover, 1957), chapter X, for the degenerate electron gas and the $p\propto\rho^{5/3}$ law.
- C. Eckart, "The thermodynamics of irreversible processes III: Relativistic theory of the simple fluid," *Physical Review* **58** (1940) 919–924, for the thermodynamic identities in the local form.
- E. Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1926) 322–326, for the quantum potential and the quantum pressure.
- D. Bohm, "A suggested interpretation of the quantum theory in terms of 'hidden' variables I," *Physical Review* **85** (1952) 166–179, for the quantum potential's role in the trajectory picture.
- T. Takabayasi, "On the formulation of quantum mechanics associated with classical pictures," *Progress of Theoretical Physics* **8** (1952) 143–182, for the hydrodynamic reading of the quantum pressure.
- The companion articles: [The Local Thermal State of a Fluid](the-local-thermal-state-of-a-fluid.html), [The Local Thermal Structure: k_B as the Scale of Imaginary Time](the-local-thermal-structure-kb-as-the-scale-of-imaginary-time.html), [The Local Entropy Current](the-local-entropy-current.html), and [The Polar Form of the Klein–Gordon Equation in Biquaternionic Form](the-polar-form-of-the-klein-gordon-equation-in-biquaternionic-form.html).
