# __Curie's Law and the Saturation of the Bloch Radius__

## Introduction

The Gibbs state of a two-level Hamiltonian has a radius $\lvert\vec s_\Psi\rvert=\tanh\Theta$ with $\Theta=\beta\lvert\vec h_\Psi\rvert$. That single line contains two laws and they live at opposite ends of the same curve. At small $\Theta$ the tangent is its own argument and the radius is proportional to the inverse temperature: that is Curie's law. At large $\Theta$ the tangent is its own asymptote and the radius approaches the bound without reaching it: that is saturation. **The article's subject is the whole curve, and the reason it is worth a separate article is that the two ends fail in different ways and neither failure is a defect of the framework.**

The findings are stated in advance.

1. **Curie's law is the linear term, and its error is known.** $\lvert\vec s_\Psi\rvert\approx\Theta$ with relative error $\Theta^{2}/3$, measured at $3.3332\times10^{-5}$ for $\Theta=0.01$ against a predicted $3.3333\times10^{-5}$, and within four parts in a thousand at $\Theta=0.1$.
2. **The susceptibility is the impurity, up to a factor.** $\chi=\partial\lvert\vec s_\Psi\rvert/\partial\lvert\vec h_\Psi\rvert=\beta\operatorname{sech}^{2}\Theta$, and $\operatorname{sech}^{2}\Theta=4N$ exactly, so $\chi/\beta=4N$. The response to the field and the distance to the centre are the same number.
3. **Curie's law is the statement $\chi/\beta=1$**, and the first correction is $-\Theta^{2}$ relative, measured at $9.9337\times10^{-3}$ for $\Theta=0.1$.
4. **The saturation is exact and exponential.** $1-\lvert\vec s_\Psi\rvert=2e^{-2\Theta}/(1+e^{-2\Theta})$, so the gap to the boundary halves for every increment $\Delta\beta=\ln 2/(2\lvert\vec h_\Psi\rvert)$. The measured halving step in $\Theta$ is $\ln 2/2=0.346574$ to nine digits over six decades.
5. **The two gaps are not comparable.** At $\Theta=16$ the radius gap is $2.5\times10^{-14}$ while the temperature is still a sixteenth of the Hamiltonian's own scale. The boundary is exponentially close in the radius and only linearly far in the temperature, which is why the third law is an unattainability statement and not a limit.
6. **There is no Curie law when the Hamiltonian is central.** $\lvert\vec h_\Psi\rvert=0$ gives $\lvert\vec s_\Psi\rvert=0$ at every $\beta$, a constant zero response; the law has a domain and the domain is not all Hamiltonians.
7. **The framework fixes $J=\tfrac12$, and that fixes the Curie constant.** At the same saturation moment the two-level constant is three times the classical one, and three is $(J+1)/J$ at $J=\tfrac12$; the classical limit itself is outside the algebra.

The notation is that of the companions. The state is $\tilde{Ϛ}_{\Psi}=\tfrac12(e_t+i\vec s_{\Psi})$; the Hamiltonian is $\tilde H_\Psi=h_t+\vec h_\Psi$ with vector part $\vec h_\Psi$ and central part $h_t$; the Gibbs state is $\vec s_\Psi=-\tanh(\beta\lvert\vec h_\Psi\rvert)\vec u_\Psi$ with $\vec u_\Psi=\vec h_\Psi/\lvert\vec h_\Psi\rvert$; the thermal rapidity is $\Theta=\beta\lvert\vec h_\Psi\rvert$. The impurity is $N=\tfrac14(1-\lvert\vec s_\Psi\rvert^{2})$, and on the Gibbs family $N=\tfrac14\operatorname{sech}^{2}\Theta$.

One convention fixes the signs. The magnetisation is the signed vector, $\vec s_\Psi$, and it is antiparallel to $\vec h_\Psi$; the radius is $\lvert\vec s_\Psi\rvert$ and carries no sign. Curie's law is a statement about the radius, and the sign is the statement that the response opposes the field.

## The Expansion

### The linear term

**For small $\Theta$ the radius is the rapidity.** Expanding $\tanh\Theta=\Theta-\Theta^{3}/3+\dots$,
$$
\lvert\vec s_\Psi\rvert=\frac{\lvert\vec h_\Psi\rvert}{k_B T}\Bigl(1-\frac{\Theta^{2}}{3}+\dots\Bigr) ,
$$
so the leading term is $\lvert\vec h_\Psi\rvert/(k_BT)$ and the relative error of the linear approximation is $\Theta^{2}/3$.

**Measured against predicted.**

| $\Theta$ | $\lvert\vec s_\Psi\rvert$ | measured $1-r/\Theta$ | $\Theta^{2}/3$ | ratio |
| --- | --- | --- | --- | --- |
| $0.01$ | $0.009999666680$ | $3.3332\times10^{-5}$ | $3.3333\times10^{-5}$ | $0.999960$ |
| $0.05$ | $0.049958374958$ | $8.3250\times10^{-4}$ | $8.3333\times10^{-4}$ | $0.999001$ |
| $0.1$ | $0.099667994625$ | $3.3201\times10^{-3}$ | $3.3333\times10^{-3}$ | $0.996016$ |
| $0.2$ | $0.197375320225$ | $1.3123\times10^{-2}$ | $1.3333\times10^{-2}$ | $0.984255$ |
| $0.5$ | $0.462117157260$ | $7.577\times10^{-2}$ | $8.333\times10^{-2}$ | $0.909188$ |

**The last row is the domain statement.** At $\Theta=0.5$ the linear law is already $7.6$ per cent wrong, and at $\Theta=1$ it is $23.8$ per cent wrong. Curie's law is a law about $\Theta\ll1$, and the corpus's temperature range for a two-level system is not small in that sense unless the temperature is above the splitting.

### The susceptibility

**The response to the field is the derivative, and it closes.**
$$
\chi=\frac{\partial\lvert\vec s_\Psi\rvert}{\partial\lvert\vec h_\Psi\rvert}=\beta\operatorname{sech}^{2}\Theta .
$$
Verified at five values of $\Theta$: $1.000000$, $0.786448$, $0.419974$, $0.070651$ and $0.009866$ at $\Theta=0$, $0.5$, $1$, $2$ and $3$.

**Curie's law in this language is the statement $\chi/\beta=1$.** The relative defect is $1-\operatorname{sech}^{2}\Theta$, measured at $9.9337\times10^{-3}$ for $\Theta=0.1$ against the predicted $\Theta^{2}=10^{-2}$, a ratio of $0.993371$; the defect is therefore the square of the same small parameter and Curie's law is the same approximation read differentially.

**The susceptibility and the impurity are one number.** Since $N=\tfrac14\operatorname{sech}^{2}\Theta$ on the Gibbs family,
$$
\frac{\chi}{\beta}=4N .
$$
At $\Theta=1$ the two sides are $0.419974341614$; at $\Theta=2$, $0.070650824853$; the identity is exact and not an approximation. **A state far from the centre is a state with a small response to its field and a large impurity; a state near the centre is the opposite.** The two names, disorder and susceptibility, are one coordinate.

**This is the article's only structural claim.** Everything else is the arithmetic of one function. But the identity is worth having: it says that the Curie constant is not a separate material parameter, because in this algebra there is only one material parameter, the magnitude of the Hamiltonian's vector part, and it sets the scale of $\Theta$ and nothing else.

## The Saturation

### The exact gap

**The distance to the boundary has a closed form.** From $\tanh\Theta=(1-e^{-2\Theta})/(1+e^{-2\Theta})$,
$$
1-\lvert\vec s_\Psi\rvert=\frac{2e^{-2\Theta}}{1+e^{-2\Theta}} ,
$$
which is exact for every $\Theta$ and not an asymptotic statement. Its ratio to $2e^{-2\Theta}$ is $0.880797$ at $\Theta=1$, $0.982014$ at $2$, $0.997527$ at $3$ and $0.999954602$ at $5$.

**The gap halves for a fixed increment of inverse temperature.** Since the gap is $2e^{-2\Theta}$ to leading order, each $\Delta\Theta=\ln 2/2$ halves it, which is
$$
\Delta\beta=\frac{\ln 2}{2\lvert\vec h_\Psi\rvert} .
$$
Measured over six decades: the gap $10^{-6}$ is reached at $\Theta=7.254329119$ and $10^{-12}$ at $\Theta=14.162084148$, a difference of $6.907755029$, which is $\ln 2/2$ times the $19.93$ halvings that six decades contain. **The approach is geometric in $\beta$, and that is the precise sense in which it never arrives.**

### The two gaps are not comparable

**The radius gap is exponential and the temperature gap is not.**

| $\Theta$ | $1-\lvert\vec s_\Psi\rvert$ | $T\lvert\vec h_\Psi\rvert^{-1}$ |
| --- | --- | --- |
| $1$ | $2.384\times10^{-1}$ | $1$ |
| $2$ | $3.597\times10^{-2}$ | $0.5$ |
| $4$ | $6.707\times10^{-4}$ | $0.25$ |
| $8$ | $2.251\times10^{-7}$ | $0.125$ |
| $16$ | $2.533\times10^{-14}$ | $0.0625$ |

**Read the two columns against each other.** Sixteen units of rapidity buy fourteen orders of magnitude in the radius and one factor of sixteen in the temperature. A state can therefore be as close to the boundary as double precision allows while its temperature is still a sixteenth of the Hamiltonian's own scale.

**That asymmetry is the third law, and it is why the third law is stated as unattainability.** If the two gaps vanished at the same rate, cooling would approach absolute zero in the ordinary sense and the statement "no finite sequence of operations reaches it" would be a technicality about infinite processes. They do not vanish at the same rate, and the radius is the coordinate in which the boundary is *reachable in the limit* while the temperature is the coordinate in which it is *not*. The companion's third-law article takes this up; the present article supplies the numbers.

**Double precision agrees, and it is the framework's own illustration.** At $\Theta=18$ the computed gap is $4.44\times10^{-16}$ and the exact one $4.64\times10^{-16}$; at $\Theta=18.7$ both are one unit in the last place; at $\Theta=19$ the subtraction returns zero. **A machine that carries sixteen digits cannot distinguish a state at $\Theta=19$ from the boundary**, which is a numerical restatement of the unattainability and not a defect of the arithmetic.

### What saturation is not

**Saturation is not the state reaching a pure state, and the difference matters.** The bound $\lvert\vec s_\Psi\rvert\le1$ is the purity bound of the ball, and $\lvert\vec s_\Psi\rvert=1$ is a pure state. Approaching the bound is approaching purity, and the companion's impurity article shows that no boost and no finite temperature completes that approach. The present article adds only that the approach is geometric with a computable step, so the prohibition is quantitative.

**Saturation is also not a failure of the two-level model.** A real magnet saturates because its moments are finite; the two-level model saturates because its Hilbert space is two-dimensional. The two mechanisms coincide in the algebra — one qubit, one unit of radius — and the coincidence is the reason the model reproduces the shape.

## Where the Law Fails

### The central Hamiltonian

**If the Hamiltonian has no vector part there is no Curie law at all.** With $\lvert\vec h_\Psi\rvert=0$ the Hamiltonian is $h_t$ times the identity, the Gibbs state is $\tfrac12e_t$ at every $\beta$, and $\lvert\vec s_\Psi\rvert=0$ for $\beta=0.1$, $1$ and $10$ alike. The radius is constant, the susceptibility is zero, and no expansion in $\beta$ has a linear term.

**The failure is a domain statement and not a pathology.** Curie's law is a statement about a splitting; no splitting, no law. The corpus's degeneracy remark makes the same point from the thermodynamic side: a degenerate Hamiltonian has no thermal path, because the path is a single point at the centre.

### The central part drops out

**The scalar part of the Hamiltonian changes nothing, and this is exact.** A Hamiltonian $\tilde H=h_t+\vec h_\Psi$ has eigenvalues $h_t\pm\lvert\vec h_\Psi\rvert$, and the Gibbs state depends on the difference alone. On a hundred draws with $h_t$ uniform on $[-3,3]$, $\beta$ on $[0.05,4]$ and $\vec h_\Psi$ random with magnitude on $[0.2,2]$, the state matches $-\tanh(\beta\lvert\vec h_\Psi\rvert)\vec u_\Psi$ to $1.5\times10^{-15}$.

**So the Curie constant is set by the vector part and by nothing else.** An overall shift of the energy scale is invisible, which is the framework's version of the elementary fact that only differences of energy enter a Gibbs state. The statement is worth making because the corpus writes the Hamiltonian as a full element, and a reader might expect $h_t$ to appear in the thermodynamics. It does not.

### Negative temperature

**The radius is even in $\beta$.** Since $\lvert\vec s_\Psi\rvert=\lvert\tanh(\beta\lvert\vec h_\Psi\rvert)\rvert$, the values at $\beta=\pm1$ coincide at $0.935409070603099$, and at $\beta=\pm0.4$ at $0.591519395431816$. The formal negative-temperature branch retraces the same radii in the opposite order, and Curie's law holds on both sides as $\lvert\vec s_\Psi\rvert\approx\lvert\beta\rvert\lvert\vec h_\Psi\rvert$.

**What changes at negative $\beta$ is the sign of the vector, not its length.** The corpus excludes $\mathrm{Re}\,\beta<0$ from the physical domain, and the exclusion is consistent with the evenness: a negative temperature is a reflection through the centre, and a reflection preserves the radius and the impurity. **The saturation statement is therefore one statement for both branches**, and the distinction between "hot" and "hotter than infinite" is carried by the sign of the magnetisation and not by its size.

## The Curie Constant and the Classical Limit

**The framework has one value of the spin and no parameter to change it.** The carrier is a single qubit, so $J=\tfrac12$ is fixed, and the Curie constant is correspondingly fixed. Comparing at the same saturation moment $\mu$,
$$
C_{1/2}=\frac{\mu^{2}}{k_B},\qquad C_{\mathrm{cl}}=\frac{\mu^{2}}{3k_B},\qquad \frac{C_{1/2}}{C_{\mathrm{cl}}}=3 .
$$
The slopes at the origin are exact: $\mathrm{d}\tanh\Theta/\mathrm{d}\Theta=1$ and $\mathrm{d}L/\mathrm{d}u=\tfrac13$ at $u=0$, and their ratio is $3$ exactly, which is the ratio of the two constants written above.

**The three is not an accident of normalisation; it is $(J+1)/J$ at $J=\tfrac12$.** The classical result is the $J\to\infty$ limit of $J(J+1)/3$, and the two-level system sits at the smallest $J$ where that factor is largest. Written as functions with the same saturation and the same Curie constant, the two laws are $\tanh\Theta$ and $L(3\Theta)$ where $L(u)=\coth u-1/u$; they differ by $0.002016$ at $\Theta=0.2$, $0.023992$ at $0.5$, $0.089958$ at $1$ and $0.130682$ at $2$.

**The difference is the article's honest limit.** The framework reproduces Curie's law exactly and the classical curve only in the limit $\Theta\to0$; between the two regimes the two-level system saturates faster, and it must, because it has only two levels to fill. **A reader who wants the Langevin curve wants a spin the algebra does not carry**, and that is a statement about the carrier and not about the temperature.

## The Strongest Objection

**The objection is that the article is the linear term of a hyperbolic tangent and adds nothing to the framework.** The objection is right about the derivation and wrong about the content. The derivation is one expansion; what the article establishes is that the expansion's two limits are the framework's two named ends of the ball — the centre at $\Theta=0$ and the boundary at $\Theta=\infty$ — and that both are reached with computable rates, $\Theta$ and $2e^{-2\Theta}$.

**A second objection is that $\chi/\beta=4N$ is a coincidence of the two-level case.** It is exact for the Gibbs family of any two-level Hamiltonian in this algebra, which is the whole family the algebra admits, so within the framework it is not a coincidence but the only case. Whether it survives in a larger carrier is a question the framework cannot pose, because a larger carrier is not an element of the algebra.

**A third objection is that the saturation numbers are a restatement of the third law rather than a result.** They are a restatement, with rates, and the rates are the content: $1-r\simeq2e^{-2\Theta}$ and $T\propto1/\Theta$ are two different answers to "how far from absolute zero", and the mismatch of the two is what makes unattainability a structural statement rather than a convention.

## What the Article Does Not Claim

**It does not explain the third law.** It computes the rate at which the boundary is approached and shows that the rate differs between the two coordinates. A finite-dimensional Gibbs state with a nondegenerate ground state has $S\to0$ as a theorem; the physical third law says more, and the companion says so.

**It does not claim that a real magnet is a qubit.** The framework's magnetisation is the Bloch vector of the state, and its saturation is the purity bound. A real magnet's saturation is a statement about a finite number of moments per unit volume. The shapes agree and the mechanisms do not.

**It does not extend the susceptibility identity beyond the Gibbs family.** $\chi/\beta=4N$ is a statement about the one-parameter thermal path, verified wherever the path is defined.

**It does not treat interacting systems.** One Hamiltonian, one state, no coupling; the Curie law of a lattice of coupled moments is a different calculation, and the framework's channel structure is where it would have to be posed.

## Summary

**Curie's law is the linear term of the tangent, with a known error.** $\lvert\vec s_\Psi\rvert\approx\Theta$ and the relative error is $\Theta^{2}/3$, measured at $3.3332\times10^{-5}$ for $\Theta=0.01$; the law is $7.6$ per cent wrong at $\Theta=0.5$ and $23.8$ per cent wrong at $\Theta=1$.

**The susceptibility is $\beta\operatorname{sech}^{2}\Theta$, and $\chi/\beta=4N$ exactly.** The response to the field and the distance to the centre are one coordinate.

**Saturation is exact: $1-\lvert\vec s_\Psi\rvert=2e^{-2\Theta}/(1+e^{-2\Theta})$.** The gap halves every $\Delta\beta=\ln2/(2\lvert\vec h_\Psi\rvert)$, with the halving step $\ln 2/2$ confirmed to nine digits over six decades, and it reaches the last place of double precision at $\Theta\approx18.7$.

**The two gaps are not comparable**: at $\Theta=16$ the radius gap is $2.5\times10^{-14}$ and the temperature is a sixteenth of the Hamiltonian's scale. The boundary is exponentially close in the radius and only linearly far in the temperature, and that is the shape of unattainability.

**The law has a domain.** A central Hamiltonian gives a constant zero radius and no Curie law; the central part $h_t$ drops out of the state entirely, to $1.5\times10^{-15}$ on a hundred draws; and the radius is even in $\beta$, so the negative-temperature branch retraces it.

**The Curie constant is three times the classical one**, because $J=\tfrac12$ and $(J+1)/J=3$; the classical limit is outside the algebra, which carries one spin and no parameter to vary it.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\Theta=\beta\lvert\vec h_\Psi\rvert$ | the thermal rapidity |
| $\lvert\vec s_\Psi\rvert=\tanh\Theta$ | the Bloch radius, the magnetisation |
| $\vec s_\Psi=-\tanh\Theta\,\vec u_\Psi$ | the Gibbs state |
| $h_t$ | the central part of the Hamiltonian; drops out |
| $N=\tfrac14\operatorname{sech}^{2}\Theta$ | the impurity on the Gibbs family |
| $\chi=\beta\operatorname{sech}^{2}\Theta=4\beta N$ | the susceptibility |
| $1-\lvert\vec s_\Psi\rvert=\dfrac{2e^{-2\Theta}}{1+e^{-2\Theta}}$ | the gap to the boundary |
| $\Delta\beta=\dfrac{\ln2}{2\lvert\vec h_\Psi\rvert}$ | the increment that halves the gap |
| $L(u)=\coth u-1/u$ | the classical Langevin function |
| $J$ | the spin, fixed at $\tfrac12$ by the carrier |

## Further Reading

- P. Curie, "Lois expérimentales du magnétisme: propriétés magnétiques des corps à diverses températures", *Annales de Chimie et de Physique* **5** (1895) 289–405 — the original inverse-temperature law
- P. Langevin, "Magnétisme et théorie des électrons", *Annales de Chimie et de Physique* **5** (1905) 70–127 — the classical function and its Curie limit
- L. Brillouin, "Aimantation de corps ferromagnétiques et théorie du champ moléculaire", *Journal de Physique* **8** (1927) 74–84 — the spin-$J$ function whose $J=\tfrac12$ case is the tangent
- J. H. Van Vleck, *The Theory of Electric and Magnetic Susceptibilities*, Oxford University Press, 1932 — the Curie constants and the $J(J+1)$ factor
- N. F. Ramsey, "Thermodynamics and statistical mechanics at negative absolute temperatures", *Physical Review* **103** (1956) 20–28 — the negative-temperature branch and why the radius is unchanged
- C. Kittel and H. Kroemer, *Thermal Physics*, 2nd ed., W. H. Freeman, 1980 — the two-level system, its susceptibility and its approach to saturation
- R. K. Pathria and P. D. Beale, *Statistical Mechanics*, 3rd ed., Elsevier, 2011 — the same, with the Brillouin and Langevin functions side by side
- *Temperature Is a Rapidity* — the thermal parameter, the shift law and the two ends of the family
- §*The Third Law in Three Formulations* in *Quantum Thermodynamics in Biquaternionic Form* — the three formulations, which one is proved and which imported, and the residual entropy of the degenerate Hamiltonian
- *The Thermal Path Is Not an Orbit* — the family as a diameter and the affinity test
- *Quantum Thermodynamics in Biquaternionic Form* — the Gibbs state, the potentials and the limits
