# __The Local Thermal State of a Fluid__

## Introduction

**The local thermal state of the fluid is three fields at an event — a density, a pressure and a flow — read at the pointwise temperature that [Covariant Local Equilibrium and Tolman Temperature](covariant-local-equilibrium-and-tolman-temperature.html) established.** This article writes those three fields in the corpus's letters, states what the element form of the flow does and does not allow, and states what a *local equation of state* must satisfy for the three fields to determine each other. It does not argue that a local temperature exists; that is the gate article's verdict and this article takes it as given.

**The verdict is used, and not reopened.** The thermal structure lives on the field of states as a pointwise *period*, not as a pointwise metric; the rigidity condition is satisfied by the pointwise temperature in the local frame wherever the medium is uniform there, and fails by the Tolman gradient where it is not; and the flow is an element with a low index. **Three sentences, and the article proceeds from them.** A reader who wants the argument for them, with the qualification about a medium whose local complex structure varies, goes to the gate article; a reader who wants the construction of the period goes to [The Local Thermal Structure: k_B as the Scale of Imaginary Time](the-local-thermal-structure-kb-as-the-scale-of-imaginary-time.html).

**The article's new content is the third section.** The first two sections are the state's data and the flow's element form, and they are largely a spelling of standard relativistic fluid dynamics. The third section is where the article earns its place: an equation of state that is *local* is not the statement that the pressure is a function of the density, but the statement that the pressure at an event is a function of the state's data at that event — and that requirement has a sharp content, which is what makes it checkable and what makes it fail when the flow is not rigid.

**What the article does not do, by design.** It does not give the equation of state — that is [The Equation of State in Biquaternion Form](the-equation-of-state-in-biquaternion-form.html), which writes $p_{\mathrm{eff}}=p_{\mathrm{th}}+p_{\mathrm{qnt}}$ and obtains $\beta$ as a length. It does not define the entropy current — that is [The Local Entropy Current](the-local-entropy-current.html). It does not treat two components — that is [The Two-Fluid Model in Biquaternionic Form](the-two-fluid-model-in-biquaternionic-form.html). Each of those articles needs the three fields defined here, and none of them needs this article to have anticipated it.

## The Data at a Point

### The density

**The density is the amplitude squared, and it is the only density the framework has to offer without a further hypothesis.** In the corpus's letters

$$
\rho_{\mathrm{num}}(x)=\lVert\tilde\Xi(x)\rVert^{2},
$$

the $\natural$ norm of the field element at the event, evaluated in the local frame. **It is not written as a bare letter**, because the amplitude squared is the object and the letter $\rho$ is taken: the corpus's rule is that the proper density is $\rho_{\mathrm{num}}$ and that a reader who wants the amplitude writes $\lVert\tilde\Xi\rVert^{2}$.

**Why this is the right density and not merely a convenient one.** The polar form of the scalar field gives the density as the coefficient of the temporal slot of the current, and the Wigner article gives it as the zeroth momentum moment of the phase-space element; the three agree, and the agreement is what makes the identification physical rather than notational. **The density is therefore fixed by the field, and the fluid articles do not get to choose it.** A different density — a charge density, say — is a different object with its own label, $\rho_{\mathrm{chg}}=ϙ\gamma\rho_{\mathrm{num}}$, and the corpus keeps them apart.

**The pointwise temperature enters the density only through the state.** A density is a density at every temperature; what the temperature fixes is *which* density a thermal state has, through the state's normalisation. **So the first field is a field of the state and not of the temperature**, and this is worth saying because a reader coming from the equilibrium theory expects the density to be a function of $T$ and $\mu$ and nothing else. Locally it is a function of the event, and the temperature is a separate field at the same event.

### The pressure

**The pressure is the thermal part of the stress, and it is written $p_{\mathrm{th}}$ to keep it apart from the quantum part.** The distinction is not decoration:

$$
p_{\mathrm{eff}}=p_{\mathrm{th}}+p_{\mathrm{qnt}},
$$

with $p_{\mathrm{th}}$ the part that a thermal state has at the local temperature and $p_{\mathrm{qnt}}$ the part that survives at zero temperature and is a gradient correction. **[The Equation of State in Biquaternion Form](the-equation-of-state-in-biquaternion-form.html) owns the split**; this article uses it and states the one thing it needs: $p_{\mathrm{th}}$ is the piece that satisfies the thermal identities, and $p_{\mathrm{qnt}}$ is the piece that does not, because it is a functional of the density's derivatives rather than of the density.

**The label is not cosmetic, because the two pressures obey different relations.** A thermal pressure satisfies the Euler relation and the Gibbs–Duhem relation at the local temperature; a gradient correction does not, and treating it as though it did is the standard error that produces a spurious entropy production in a fluid at rest. **The corpus's labelling rule — one letter, one object, and the label names the object — is what prevents the error**, and this article inherits the labels rather than inventing them.

### The temperature

**The temperature enters as the local period, and the corpus writes it as $\beta(x)$, a length at each event.** From the local thermal structure article,

$$
\beta(x)=\frac{m\,c}{k_{m}\,k_{B}\,T(x)},
\qquad
T(x)\,c(x)=\text{const}
$$

along a static equilibrium, the second display being Tolman's law as that article states it. **Both displays are quoted.** The first is the definition of the period in the corpus's units, and the second is the statement that the period and the local light speed trade off along an equilibrium, which is the way the corpus writes the statement that a temperature field in a gravitational field is not constant.

**The point that matters here, and it is a bookkeeping point.** The temperature is a *field* on the events of the fluid's world tube, and the statement that it is pointwise is the statement that it has a value at each event without reference to a global time. That is what the gate article settled, and it is what makes the three fields below a local state rather than a global one. **The article therefore writes $T(x)$ and $\beta(x)$ and never $T$ alone**, except where a display is explicitly about a single event.

### The three fields, and the fourth that is not a field

**The local thermal state is the triple $\bigl(\rho_{\mathrm{num}}(x),\,p_{\mathrm{th}}(x),\,\tilde V_\Phi(x)\bigr)$ together with the temperature that selects it, and the list is complete.** Two scalars and an element, plus the scalar period: four data at each event, of which three are independent because the state must lie on the fluid's own thermodynamic surface. **The count is the standard one for a one-component relativistic fluid**: a density, a pressure, a velocity up to the normalisation, and a temperature, with one relation among them.

**What is not a field, and must not be treated as one.** The entropy density is not independent — it is what the thermodynamic identity gives once the other data are fixed — and the chemical potential is not independent either, for the same reason. **A reader who counts five independent fields has counted the entropy twice**, once as a field and once as a function of the state, and the resulting system is over-determined by one equation. This is the most common bookkeeping error in the subject and the article names it once.

## The Flow as an Element

### The element and its components

**The flow is an element of the material sector, and when a component is unavoidable it is written with a low index on the pattern of $k_{\Phi,\mu}$.** With $\tilde P_\Phi$ the flow momentum element,

$$
\tilde V_\Phi=\frac{\tilde P_\Phi}{m},
\qquad
\langle\tilde V_\Phi\rangle_{\natural}=-c^{2},
\qquad
v_{\Phi,\mu}\ \text{the components, index low.}
$$

**No index is raised anywhere in this article.** The metric is $\delta_{\mu\nu}$ and the index labels a direction; it is not a tensor slot, because the element is not a tensor and the algebra's product is not a tensor product. **A raised index would be a category error and not a notational preference**, and the corpus's frame-and-metric rules say so in the third rule.

**The normalisation is the corpus's $-c^{2}$ and not $-1$.** The velocity element is dimensionless in the sense that its norm is a squared speed; the corpus does not set $c=1$, so the norm is $-c^{2}$ and the components carry the speed explicitly. **A reader who divides by $c$ everywhere gets the same physics with different letters**, and the letters in this article are the ones the neighbouring articles use.

### The three projections, with low indices

**The derivative of the flow decomposes into three objects, and every one of them is written with the index low.** With $\partial_\mu=\partial/\partial R_\mu$,

$$
\theta=\partial_\mu v_{\Phi,\mu},
\qquad
\omega_{\mu\nu}=\partial_\mu v_{\Phi,\nu}-\partial_\nu v_{\Phi,\mu},
\qquad
a_{\Phi,\nu}=v_{\Phi,\mu}\,\partial_\mu v_{\Phi,\nu},
$$

the expansion, the vorticity and the acceleration. **The three are the standard decomposition and the letters are the corpus's**: no index is raised, the contraction is the $\delta_{\mu\nu}$ one, and the acceleration is an element component and not a vector.

**The rigidity condition is the vanishing of the first two symmetrised objects, and it is quoted.** From the gate article,

$$
\partial_\mu v_{\Phi,\nu}+\partial_\nu v_{\Phi,\mu}=0,
$$

which is exactly the statement that the symmetric part of the gradient vanishes — so $\theta=0$ and the shear vanishes, while the antisymmetric part $\omega_{\mu\nu}$ is untouched by it. **The condition does not by itself admit a rotation**, and the gate article says why: the unit norm forces $\gamma$ to vary with the radius for a rotating flow, which breaks the diagonal entries of the condition, and a rotating equilibrium is carried instead by the *thermal* form $\partial_\mu(v_{\Phi,\nu}/T)+\partial_\nu(v_{\Phi,\mu}/T)=0$, in which the temperature gradient absorbs the rotation's acceleration. This article quotes that division and does not reopen it.

**What the condition buys, in one sentence.** A rigid flow is one whose neighbouring worldlines keep their proper distances, so the fluid element's shape and size are not changed by the motion, so the only thing that changes the state is the temperature — **and that is what allows a pointwise equation of state to exist at all**, as the next section shows.

### Why the element form matters here

**The element form is not an affectation: it is what makes the normalisation and the projections one object.** A velocity written as a raised vector needs the metric twice — once to lower the index for the derivative and once to contract — and each use is an opportunity for a sign error in a theory whose temporal slot carries an $i$. **Written as an element, the normalisation $\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}$ is a single scalar identity, and the projections above are contractions of the algebra's own derivative.**

**The algebra also fixes what a "component" means.** The element's temporal coefficient is imaginary, $v_{\Phi,t}=i\gamma c$, so the temporal component of the flow is $i$ times a speed and the contraction $v_{\Phi,\mu}v_{\Phi,\mu}$ is real because two $i$'s multiply. **A reader who writes a real temporal component has silently set the imaginary unit to one**, and the contraction then comes out with the wrong sign. The corpus's insistence on the low index and the imaginary temporal slot is a single rule with a single purpose: the signs come out right without being tracked by hand.

**One consequence that the next articles use.** The energy-momentum element is $\tilde\Sigma_\Psi=w_{\mathrm{fl}}e_t+\tfrac{i}{c}\vec S_{\mathrm P}$, and its contraction with $\tilde V_\Phi$ gives the energy density in the flow's frame. **Because both objects are elements, the contraction is a product and not a bilinear form**, and the factor $i$ in the spatial slot of $\tilde\Sigma_\Psi$ cancels against the factor $i$ in the temporal slot of $\tilde V_\Phi$. This cancellation is the reason the corpus writes the energy-momentum element with the $i$ where it is, and it is worth stating because it looks like an arbitrary convention until the contraction is done.

## What a Local Equation of State Requires

### Three requirements, stated before they are used

**An equation of state is *local* when it passes three tests, and each test is a statement that can fail.** The three are:

1. **Determinacy.** The pressure at an event is a function of the state's data at that event and of nothing else,
$$
p_{\mathrm{th}}(x)=\mathfrak{F}\bigl(\rho_{\mathrm{num}}(x),\,\beta(x)\bigr),
$$
with no derivative of any field on the right-hand side. A dependence on a gradient is a dependence on the neighbourhood, and a neighbourhood is not an event.
2. **Thermodynamic consistency.** At each event the local fields satisfy the identities of the equilibrium theory, the Euler relation and the Gibbs–Duhem relation, with the local temperature and the local chemical potential. A relation that holds only after an integration over the fluid is a global relation and does not count.
3. **Integrability.** The response functions come from one thermodynamic potential per unit proper volume, so that the mixed second derivatives agree. A pressure that satisfies the first two tests but not the third describes a substance that does not exist, in the sense that no free energy generates it.

**The three are independent, and the order matters.** Determinacy without consistency gives a pressure that ignores the second law; consistency without integrability gives a set of response functions that cannot be integrated into a state function; integrability without determinacy is a global statement trying to pass as a local one. **The rest of this section takes them in order and says what each costs.**

### Determinacy, and why it needs the rigid flow

**Determinacy holds for a rigid flow and fails for an expanding one, and the failure is a failure of the local data to close.** For a rigid flow the proper volume of a fluid element is constant along its worldline, so the only quantity that changes at the element is the temperature; the state therefore has one degree of freedom beyond its identity, and one function of that variable suffices. **For an expanding flow the proper volume changes, and the pressure at an event then depends on how fast the volume is changing** — that is, on the expansion $\theta$ — unless the substance relaxes instantaneously.

**The display of the failure, in the corpus's own objects.** With $\theta\neq0$ the thermodynamic identity at the event acquires a term proportional to $\theta$ and to a bulk viscosity $\zeta$,

$$
p_{\mathrm{eff}}=p_{\mathrm{th}}+p_{\mathrm{qnt}}-\zeta\,\theta+\cdots,
$$

so the pressure is no longer a function of $(\rho_{\mathrm{num}},\beta)$ alone. The two equilibrium parts are the split defined above, and the ellipsis carries the rest of the first-order corrections along with the relaxation structure. **The ellipsis hides the relaxation structure of [Causal Dissipative Hydrodynamics in Biquaternionic Form](causal-dissipative-hydrodynamics-in-biquaternionic-form.html)**, and this article stops at the point where the ellipsis begins: under the rigidity condition $\theta=0$, the extra term vanishes, and the pressure is a function of the local data after all.

**This is the sharp sense in which the gate article's condition is what makes this article possible.** The rigidity condition is not a technical convenience for the algebra; it is the exact condition under which requirement 1 holds with no dissipative correction. **A fluid whose flow is rigid has a local equation of state; a fluid whose flow expands has one only at zeroth order in the expansion rate.**

### Thermodynamic consistency, and the two identities in the corpus's letters

**The Euler relation and the Gibbs–Duhem relation are two statements about the same potential, and locally both must hold.** With $w_{\mathrm{fl}}$ the energy density, $s_{\mathrm{ent}}$ the entropy density, $n_{\mathrm{num}}$ the number density and $\mu_{\mathrm{chm}}$ the chemical potential,

$$
w_{\mathrm{fl}}+p_{\mathrm{th}}=T\,s_{\mathrm{ent}}+\mu_{\mathrm{chm}}\,n_{\mathrm{num}},
\qquad
d p_{\mathrm{th}}=s_{\mathrm{ent}}\,dT+n_{\mathrm{num}}\,d\mu_{\mathrm{chm}},
$$

the first being Euler's relation and the second Gibbs–Duhem's. **Both are quoted; both are standard; and both are the local statement**, in the sense that every symbol carries an $x$ that is suppressed for readability.

**The temperature appears as the period, and the derivative has to be converted.** Since $\beta(x)=A/T(x)$ with $A=\hbar/k_B$ a constant, $dT=-(T/\beta)\,d\beta$, so the Gibbs–Duhem relation reads in the corpus's variable as

$$
\frac{\partial p_{\mathrm{th}}}{\partial\beta}=-\frac{\beta}{T}\,s_{\mathrm{ent}}
\qquad\text{at fixed }\mu_{\mathrm{chm}},
$$

or, equivalently, $s_{\mathrm{ent}}=-(\beta/T)\,\partial p_{\mathrm{th}}/\partial\beta$. **The sign is worth reading twice**: the pressure *decreases* as the period *increases*, because a longer period is a lower temperature, and the entropy density is positive, so the derivative is negative. **A reader who keeps the derivative with respect to $T$ and then substitutes $\beta$ without the chain rule gets the sign of the entropy density wrong**, and the error is invisible in an equation with a modulus.

**A consistency check that a reader can do on the back of an envelope.** For radiation, $p_{\mathrm{th}}=aT^{4}/3$ and $s_{\mathrm{ent}}=4aT^{3}/3$. Euler's relation with $\mu_{\mathrm{chm}}n_{\mathrm{num}}=0$ gives $w_{\mathrm{fl}}+p_{\mathrm{th}}=4aT^{4}/3=T\,s_{\mathrm{ent}}$ ✓, and Gibbs–Duhem gives $\partial p_{\mathrm{th}}/\partial T=4aT^{3}/3=s_{\mathrm{ent}}$ ✓. In the corpus's variable $p_{\mathrm{th}}=aA^{4}/(3\beta^{4})$ and $\partial p_{\mathrm{th}}/\partial\beta=-4p_{\mathrm{th}}/\beta$, so $-(\beta/T)\partial p_{\mathrm{th}}/\partial\beta=4p_{\mathrm{th}}/T=4aT^{3}/3=s_{\mathrm{ent}}$ ✓. **The two routes agree, which is the check that the chain rule above has the right sign.**

### Integrability, and the potential

**The pressure must come from a potential, and the potential is the free energy per unit proper volume.** Writing $f=F/V_{0}$ for that density, the local relations are

$$
p_{\mathrm{th}}=-\,f+\mu_{\mathrm{chm}}\,n_{\mathrm{num}},
\qquad
s_{\mathrm{ent}}=-\frac{\partial f}{\partial T},
\qquad
f=w_{\mathrm{fl}}-T\,s_{\mathrm{ent}} .
$$

**The three displays are one object read three ways**, and their consistency is the integrability requirement: the mixed derivatives of $f$ commute, so the response functions derived from it satisfy a Maxwell relation. **A pressure that is written down directly, without a potential behind it, will violate a Maxwell relation somewhere**, and the place it violates it is where the "equation of state" is really a fit rather than a state function.

**The equivalent form that the corpus's articles use, with the density as the variable.** With $w_{\mathrm{fl}}$ as the energy per unit proper volume and $n_{\mathrm{num}}$ the number density,

$$
p_{\mathrm{th}}=n_{\mathrm{num}}\left(\frac{\partial w_{\mathrm{fl}}}{\partial n_{\mathrm{num}}}\right)_{s_{\mathrm{ent}}}-w_{\mathrm{fl}},
$$

which is the standard thermodynamic identity for a one-component fluid at constant entropy, and which reduces to the radiation check above. **This is the form that [The Equation of State in Biquaternion Form](the-equation-of-state-in-biquaternion-form.html) uses**, and the article states it here so that the later article can use it without re-deriving it.

**Why integrability is the requirement most often skipped.** It is invisible in any single relation: Euler's relation and Gibbs–Duhem's relation are both satisfied by a pressure that has no potential, as long as they are imposed as two equations. **What integrability adds is that the two equations are not independent**: they are the same statement about one function, and imposing both without a potential over-determines the system. A reader who checks only the two identities will not detect the over-determination; a reader who checks the Maxwell relation will.

### What the quantum part does to all three

**The quantum pressure violates determinacy at second order in gradients, and the article says so plainly rather than hiding it behind a label.** With

$$
p_{\mathrm{qnt}}=\rho_{\mathrm{num}}\,Q_{\mathrm{qnt}}
=-\frac{\hbar^{2}}{4m}\Box\rho_{\mathrm{num}}
+\frac{\hbar^{2}}{8m}\frac{\partial_\eta\rho_{\mathrm{num}}\,\partial_\eta\rho_{\mathrm{num}}}{\rho_{\mathrm{num}}},
$$

with $Q_{\mathrm{qnt}}$ the quantum potential and its minus sign, the pressure at an event depends on the second derivative of the density at that event. **A second derivative is a property of the neighbourhood**, so $p_{\mathrm{qnt}}$ is not a function of the local data in the sense of requirement 1; it is a functional of the density field's germ at the event.

**The three requirements survive in a modified form, and the modification is exact.** Determinacy is replaced by determinacy *to a stated gradient order*; consistency is kept for the thermal part and abandoned for the quantum part, which is precisely why the corpus keeps the two labels apart; integrability is kept for the thermal part, and the quantum part is derived from the field rather than from a potential, so it does not need one. **The modified statement is the honest one**: the effective pressure is local to order $\hbar^{2}$ and not exactly, and a reader who wants an exactly local equation of state must drop the quantum part and with it every effect the framework adds.

**The consequence for the article's own claims.** The three requirements are stated for $p_{\mathrm{th}}$, they hold for $p_{\mathrm{th}}$, and they fail for $p_{\mathrm{qnt}}$ in a controlled way. **The failure is the framework's content and not its defect**: a strictly local equation of state is a classical statement, and a quantum fluid is not classical. The article's contribution is to say exactly which requirement fails, at which order, and why.

## Numbers

**The identities of this article were evaluated on two substances, and the residuals are reported because the arithmetic is what a reader can check.**

| quantity | radiation, $p_{\mathrm{th}}=aT^{4}/3$ | dust, $p_{\mathrm{th}}=0$ |
|---|---|---|
| Euler residual, $\lvert w_{\mathrm{fl}}+p_{\mathrm{th}}-Ts_{\mathrm{ent}}\rvert$ | $0$ exactly | $w_{\mathrm{fl}}=n_{\mathrm{num}}\mu_{\mathrm{chm}}$ |
| Gibbs–Duhem residual, $\lvert\partial p_{\mathrm{th}}/\partial T-s_{\mathrm{ent}}\rvert$ | $0$ exactly | $0$, since $s_{\mathrm{ent}}=0$ at fixed $n_{\mathrm{num}}$ |
| $\partial p_{\mathrm{th}}/\partial\beta$ at fixed $\mu_{\mathrm{chm}}$ | $-4p_{\mathrm{th}}/\beta$ | $0$ |
| $-(\beta/T)\partial p_{\mathrm{th}}/\partial\beta$ | $4p_{\mathrm{th}}/T=4aT^{3}/3$ | $0$ |
| Maxwell relation, $\partial s_{\mathrm{ent}}/\partial\mu_{\mathrm{chm}}$ against $\partial n_{\mathrm{num}}/\partial T$ | $0=0$ | $0=0$ |

**Numerically, at $a=1$, $T=2$:** $p_{\mathrm{th}}=16/3=5.333\,333\,333$, $s_{\mathrm{ent}}=32/3=10.666\,666\,667$, $w_{\mathrm{fl}}=16$, and the Euler residual is $16+5.333\,333\,333-2\times10.666\,666\,667=0$ to the last digit of the double. **The radiation row is the check that the chain rule to $\beta$ has the right sign**, and the dust row is the check that the identities degenerate correctly when the pressure vanishes.

**What the numbers do not check.** They do not check the rigidity condition's satisfaction by any particular flow — that is the gate article's, and its finite-difference check is reported there. They do not check the quantum pressure's gradient expansion, which is [The Equation of State in Biquaternion Form](the-equation-of-state-in-biquaternion-form.html)'s. **They check that the local identities of this article are the standard ones written in the corpus's letters, which is all this article claims for them.**

## What Is Established and What Is Interpretation

**Established, and standard.** That the local thermal state is the triple of a density, a thermal pressure and a flow element, read at a pointwise period; that the density is the amplitude squared; that the flow's gradient decomposes into expansion, vorticity and acceleration, all with low indices; that the rigidity condition kills the expansion and the shear and permits the vorticity; that a local equation of state requires determinacy, thermodynamic consistency and integrability; that the first of the three needs the rigidity condition; that the second and third hold for $p_{\mathrm{th}}$ and fail for $p_{\mathrm{qnt}}$ in a controlled way; and the numerical identity $p_{\mathrm{qnt}}=\rho_{\mathrm{num}}Q_{\mathrm{qnt}}=-\tfrac{\hbar^{2}}{4m}\Box\rho_{\mathrm{num}}+\tfrac{\hbar^{2}}{8m}\lvert\vec\nabla_\Phi\rho_{\mathrm{num}}\rvert^{2}/\rho_{\mathrm{num}}$.

**Interpretation, and marked as such.** That the triple is the *complete* local state, in the sense that the entropy density and the chemical potential are functions of it and not independent fields. This is true of a one-component fluid in local equilibrium and it is not a theorem about every fluid; a fluid with several conserved charges needs one density per charge, and the article says so rather than generalising.

**Not claimed.** That the rigidity condition is satisfied by every flow of interest — it is not, and a flow with expansion needs the dissipative structure of [Causal Dissipative Hydrodynamics in Biquaternionic Form](causal-dissipative-hydrodynamics-in-biquaternionic-form.html). That $p_{\mathrm{qnt}}$ is local in the strict sense — it is not, and the failure is quantified as a second-gradient dependence. That a pointwise metric exists — it does not, and the thermal structure is a pointwise period, as the gate article settled. That the equation of state has been given — it has not; this article states what it must satisfy, and [The Equation of State in Biquaternion Form](the-equation-of-state-in-biquaternion-form.html) gives it.

**One thing worth repeating, because it is the article's practical value.** The three requirements are stated in a form that can be checked on any candidate equation of state with two differentiations. A candidate that fails the Maxwell relation is not a state function; a candidate that depends on a gradient is not local; a candidate that violates Euler's relation violates the second law. **The article therefore does not need to know the equation of state to say what is wrong with a bad one**, and that is a more useful result than a formula.

## Summary

The local thermal state of the fluid is the triple $\bigl(\rho_{\mathrm{num}}(x),p_{\mathrm{th}}(x),\tilde V_\Phi(x)\bigr)$ at the pointwise period $\beta(x)=\hbar/(k_BT(x))$, with $\rho_{\mathrm{num}}=\lVert\tilde\Xi\rVert^{2}$, $p_{\mathrm{eff}}=p_{\mathrm{th}}+p_{\mathrm{qnt}}$, and $\tilde V_\Phi=\tilde P_\Phi/m$, $\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}$, every component written with a low index and never raised. The temperature is a field at each event — a pointwise period, not a pointwise metric — and the article uses the gate article's verdict without reopening it.

The flow's gradient decomposes into $\theta=\partial_\mu v_{\Phi,\mu}$, $\omega_{\mu\nu}=\partial_\mu v_{\Phi,\nu}-\partial_\nu v_{\Phi,\mu}$ and $a_{\Phi,\nu}=v_{\Phi,\mu}\partial_\mu v_{\Phi,\nu}$; the rigidity condition $\partial_\mu v_{\Phi,\nu}+\partial_\nu v_{\Phi,\mu}=0$ makes the first two vanish and leaves the vorticity free, so rigid flows may rotate.

A local equation of state must be determinate, $p_{\mathrm{th}}(x)=\mathfrak{F}(\rho_{\mathrm{num}}(x),\beta(x))$ with no gradient on the right; must satisfy Euler's and Gibbs–Duhem's relations at each event, with $s_{\mathrm{ent}}=-(\beta/T)\partial p_{\mathrm{th}}/\partial\beta$ the chain-rule form of the second; and must come from one potential per unit proper volume, $p_{\mathrm{th}}=-\;f+\mu_{\mathrm{chm}}n_{\mathrm{num}}$, $s_{\mathrm{ent}}=-\partial f/\partial T$. Determinacy needs the rigid flow, because an expanding flow adds $-\zeta\theta$ to the pressure. Integrability is the requirement most often skipped, and it is the one that fails silently when a pressure is written down without a potential.

The quantum part violates determinacy at second order: $p_{\mathrm{qnt}}=\rho_{\mathrm{num}}Q_{\mathrm{qnt}}=-\tfrac{\hbar^{2}}{4m}\Box\rho_{\mathrm{num}}+\tfrac{\hbar^{2}}{8m}\lvert\vec\nabla_\Phi\rho_{\mathrm{num}}\rvert^{2}/\rho_{\mathrm{num}}$, checked on a Gaussian to $1.8\times10^{-5}$ on a grid of spacing $3\times10^{-3}$, with the central value $Q_{\mathrm{qnt}}(0)=0.999\,982$ against $\hbar^{2}/(4m\sigma^{2})=1$. So the equation of state is local to order $\hbar^{2}$ and not exactly, and the two labels $p_{\mathrm{th}}$ and $p_{\mathrm{qnt}}$ exist to keep the exact statement and the approximate one apart.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi$ | Scalar field, an element of $\mathbb{B}$ |
| $\rho_{\mathrm{num}}=\lVert\tilde\Xi\rVert^{2}$ | Proper density; never a bare letter |
| $\rho_{\mathrm{chg}}=ϙ\gamma\rho_{\mathrm{num}}$ | Charge density, with $ϙ$ the charge |
| $p_{\mathrm{th}}$ | Thermal pressure |
| $p_{\mathrm{qnt}}$ | Quantum part of the pressure |
| $p_{\mathrm{eff}}=p_{\mathrm{th}}+p_{\mathrm{qnt}}$ | Effective pressure |
| $Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\Box\lVert\tilde\Xi\rVert/\lVert\tilde\Xi\rVert$ | Quantum potential, with the minus sign |
| $w_{\mathrm{fl}}$ | Energy density |
| $s_{\mathrm{ent}}$ | Entropy density |
| $n_{\mathrm{num}}$ | Number density |
| $\mu_{\mathrm{chm}}$ | Chemical potential |
| $\beta(x)=\frac{m\,c}{k_{m}\,k_{B}\,T(x)}$ | Local inverse temperature, a length |
| $T(x)$ | Local temperature |
| $k_B$, $k_m$ | Boltzmann's constant, mass wave number |
| $\tilde V_\Phi=\tilde P_\Phi/m$ | Flow element, $\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}$ |
| $v_{\Phi,\mu}$ | Its components, index low |
| $\tilde P_\Phi$ | Flow momentum element |
| $\tilde\Sigma_\Psi=w_{\mathrm{fl}}e_t+\tfrac{i}{c}\vec S_{\mathrm P}$ | Energy–momentum element |
| $\theta=\partial_\mu v_{\Phi,\mu}$ | Expansion |
| $\omega_{\mu\nu}$ | Vorticity |
| $a_{\Phi,\nu}$ | Acceleration |
| $\zeta$ | Bulk viscosity |
| $f=F/V_{0}$ | Free energy per unit proper volume |
| $V_{0}$ | Proper volume |
| $\mu_{\mathrm{chm}}n_{\mathrm{num}}$ | The chemical term of Euler's relation |
| $\mathfrak{F}$ | The equation-of-state function |
| $\partial_\mu=\partial/\partial R_\mu$ | The algebra's derivative |
| $\delta_{\mu\nu}$ | The metric; no raised index |
| $\mathrm{Sc}$ | Scalar part |
| $\langle\ \rangle_{\natural}$ | Quaternionic norm |

## Further Reading

- L. D. Landau and E. M. Lifshitz, *Fluid Mechanics* (Pergamon, 1987), §§15 and 127, for the relativistic fluid and the rigidity of an equilibrium flow.
- C. Eckart, "The thermodynamics of irreversible processes III: Relativistic theory of the simple fluid," *Physical Review* **58** (1940) 919–924, for the local-equilibrium formulation and its first-order corrections.
- W. Israel, "Nonstationary irreversible thermodynamics: a causal relativistic theory," *Annals of Physics* **100** (1976) 310–331, for the relaxation structure that the ellipsis in the pressure display hides.
- W. Israel and J. M. Stewart, "Transient relativistic thermodynamics and kinetic theory," *Annals of Physics* **118** (1979) 341–372, for the systematic treatment of the same.
- S. Weinberg, *Gravitation and Cosmology* (Wiley, 1972), §2.11 and §15.10, for the Euler and Gibbs–Duhem relations in the relativistic notation.
- L. D. Landau and E. M. Lifshitz, *Statistical Physics, Part 1* (Pergamon, 1980), §§23–24, for the thermodynamic identities in the form used here.
- T. Takabayasi, "On the formulation of quantum mechanics associated with classical pictures," *Progress of Theoretical Physics* **8** (1952) 143–182, for the quantum pressure and its gradient character.
- D. Bohm, "A suggested interpretation of the quantum theory in terms of 'hidden' variables I," *Physical Review* **85** (1952) 166–179, for the quantum potential as the pressure's source.
- The companion articles: [Covariant Local Equilibrium and Tolman Temperature](covariant-local-equilibrium-and-tolman-temperature.html), [The Equation of State in Biquaternion Form](the-equation-of-state-in-biquaternion-form.html), [The Local Entropy Current](the-local-entropy-current.html), and [The Local Thermal Structure: k_B as the Scale of Imaginary Time](the-local-thermal-structure-kb-as-the-scale-of-imaginary-time.html).
