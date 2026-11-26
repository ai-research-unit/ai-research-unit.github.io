# __The $\mathrm{SU}(4)$ Instanton: A Matrix Transcription Outside the Algebra__

## Introduction

**The question.** Does the primordial phase have non-perturbative structure, and can that structure be written in the algebra the corpus derives $\mathrm{SU}(2)$ from?

**The answer.** It has one, and it cannot.

$$
\boxed{\;S_{\mathrm{inst}}=\frac{8\pi^{2}}{g_4^{2}}=\frac{2\pi}{\alpha_4(M_X)}=108.2,
\qquad
e^{-S}=1.1\times10^{-47},\qquad
\theta_{4}\ \text{periodic with period }2\pi .\;}
$$

**The instanton exists, is enormous, and is transcribed rather than derived.** Its action is fixed by the same coupling that runs in [The Primordial Coupling](the-primordial-coupling.html), and the $\theta_4$ that weights it is a free coefficient of the Lagrangian — **and, as the last section shows, a redundant one above $M_C$, where the sixteen are massless.**

**Why "outside the algebra" and not merely "hard".** The instanton is a configuration of a connection on a four-dimensional space whose second Chern number is one. **Its existence is a statement about a $4\times4$ matrix field and about $\pi_3(\mathrm{SU}(4))=\mathbb{Z}$**, and the algebra $\mathbb{B}$ has compact group $\mathrm{U}(2)$ of real dimension four — far too small to contain fifteen generators, let alone a winding sector of them. **The instanton therefore stands exactly where the action stands: on the transcribed side of the ceiling**, and this article is where that placement is made explicit.

**What this article does.** It writes the topological term, computes the action and the suppression, counts the moduli, states the size-modulus cutoff, and locates the whole construction relative to the algebra.

**What it does not do.** It does not compute the $\theta_4$ dependence of any observable, does not build a dilute-gas model, and does not discuss the strong-$CP$ problem except to say why it does not arise above $M_C$.

## The Topological Term

**One term, one coefficient, one periodicity.**

$$
\mathcal{L}_{\theta}=\theta_{4}\,\frac{g_4^{2}}{16\pi^{2}}\operatorname{tr}\bigl(\mathbb{F}_{\imath\jmath}\tilde{\mathbb{F}}_{\imath\jmath}\bigr),
\qquad
\tilde{\mathbb{F}}_{\imath\jmath}=\tfrac12\varepsilon_{\imath\jmath\kappa\lambda}\mathbb{F}_{\kappa\lambda},
$$

with $\mathbb{F}=\sum_{a}F_{a}t_{a}$ the matrix-valued curvature and the trace over the spatial block, which for a Hermitian matrix is the whole of the contraction. **The $t_{a}$ are the normalised Hermitian generators of the block**, $t_{a}=iG_{a}/\sqrt{2n_{a}}$ on the anti-Hermitian printed arrays, with $n_{a}=\operatorname{tr}(G_{a}^{\dagger}G_{a})$ equal to $2$ for the fourteen and $12$ for the corner, so that $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$, $\mathbb{F}$ is Hermitian and $\operatorname{tr}(\mathbb{F}\tilde{\mathbb{F}})$ is real.

**The normalisation is the one that makes the integral an integer.**

$$
\frac{g_4^{2}}{16\pi^{2}}\int\operatorname{tr}\bigl(\mathbb{F}\tilde{\mathbb{F}}\bigr)\in\mathbb{Z}
\quad\text{equivalently}\quad
\frac{g_4^{2}}{32\pi^{2}}\int F_{a,\imath\jmath}\tilde F_{a,\imath\jmath}\in\mathbb{Z}
$$

with $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ in the first form — **the normalisation the whole block uses**, on the Hermitian $t_{a}$ and not on the printed anti-Hermitian $G_{a}$ whose norms are $2$ and $12$, as [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html) fixes it. **Two conventions and one integer**: one BPST instanton gives $\int F_{a}\tilde F_{a}=32\pi^{2}/g_4^{2}$, so the sum-over-generators form integrates to $g_4^{2}/(32\pi^{2})\times32\pi^{2}/g_4^{2}=1$ and the trace form to $g_4^{2}/(16\pi^{2})\times\tfrac12\times32\pi^{2}/g_4^{2}=1$. **The factor of two between the two displays is the trace's, not the group's.** Dropping the $g_4^{2}$ while keeping the trace is the error that turns the integer $1$ into $1/g_4^{2}$.

**The coefficient $\theta_4$ is free and the group does not fix it.** A total derivative does not affect the equations of motion, but it does affect the action of a configuration with nonzero winding, **so $\theta_4$ weights every winding sector and no argument in the group selects its value.** The $2\pi$ periodicity follows from the integrality above: a sector of winding $n$ carries the weight $e^{i\theta_4 n}$, and shifting $\theta_4$ by $2\pi$ multiplies it by $e^{2\pi i n}=1$, **for every integer $n$ at once — which is what makes the shift a symmetry of the whole sum and not of one term.**

**Whether that weight is observable is a separate question**, and it is the one the last section answers: the term is present in the Lagrangian and, above $M_C$, removable from the phase.

**Why the trace is the matrix trace and not a sum over generators.** $\operatorname{tr}(\mathbb{F}\tilde{\mathbb{F}})=\frac12F_{a}\tilde F_{a}$ by the normalisation, so the two agree as densities; **but the integrality statement is about the matrix trace of a bundle, and the sum over generators carries no bundle.** The distinction is the same one the parent article makes about the action's density, and it is sharper here: **a sum over fifteen generators of fifteen numbers is not a Chern class.**

## The Action and Its Size

**One number, and it is the largest dimensionless number in the coupling block.**

$$
S_{\mathrm{inst}}=\frac{8\pi^{2}}{g_4^{2}}=\frac{2\pi}{\alpha_4},
\qquad
\alpha_4(M_X)=0.0581
\quad\Longrightarrow\quad
S=108.2 ,
\qquad
e^{-S}=1.1\times10^{-47} .
$$

**The action is independent of the instanton's size at tree level**, because the classical $\mathrm{SU}(4)$ theory with massless content is scale invariant. **The size dependence enters only through the running coupling**, evaluated at the inverse size:

$$
S(\rho)=\frac{2\pi}{\alpha_4(1/\rho)},
\qquad
\alpha_4(1/\rho)\ \text{decreasing as}\ \rho\ \text{decreases} .
$$

**So smaller instantons have larger action and are more suppressed**, and the density $dn\sim d\rho\,\rho^{-5}e^{-S(\rho)}$ is dominated by the largest allowed size. **The largest allowed size is set by the phase's own end:**

$$
\rho_{\mathrm{inst}}\lesssim\frac{1}{M_C},
$$

**because an instanton larger than the transition scale would have to live in a phase that does not exist there.** That is the cutoff, and it is a statement about the model and not about the integral.

**What the number means, stated without inflation.** $1.1\times10^{-47}$ per unit four-volume in units of $M_C$ is not zero, and in a cosmological setting it would matter; **inside the phase, no observable of the block depends on it at any accuracy the block claims, and the warrant is one line: every instanton-induced quantity carries at least one factor of $e^{-S}$, and $10^{-47}$ is forty-five orders below the few per cent at which the one-loop running is known.** The article's point is not that the effect is negligible but that it is computable and large, **which is the opposite of the usual situation in a strongly coupled theory where the semi-classical expansion fails.**

**The value at the transition, for completeness.** $S(M_C)=2\pi/\alpha_4(M_C)=2\pi/0.05776=108.8$, **six tenths larger than at $M_X$**, because the coupling has barely moved over the interval between them. **The suppression is the same to two significant figures everywhere in the phase**, which is why the article quotes one number.

## The Moduli

**A single instanton has $4N=16$ parameters, and the split is exact for $\mathrm{SU}(N)$.**

| modulus | count | what it is |
| --- | --- | --- |
| translations | $4$ | where the instanton sits |
| dilatation | $1$ | its size $\rho$ |
| orientation | $11$ | how its $\mathrm{SU}(2)$ sits inside $\mathrm{SU}(4)$ |
| **total** | $\mathbf{16}$ | $4N$ with $N=4$ |

**The orientation count is $11$ and not $15$, and the difference is what the instanton does not use.** The count itself is the standard $4Nk$ at $k=1$, and the five removed are the four positions and the size. **The remaining eleven are not one coset**: the embedded $\mathrm{SU}(2)$ has stabiliser $\mathrm{SU}(2)\times\mathrm{SU}(2)\times\mathrm{U}(1)$ in $\mathrm{SU}(4)$ — dimension $3+3+1=7$ — so its orbit has dimension $15-7=8$, and the other three are the rotations of the instanton inside its own $\mathrm{SU}(2)$. **$8+3=11$, and $4+1+11=16$**, which is the table.

**The instanton does not use all fifteen generators.** Its field strength lies in an $\mathrm{su}(2)$ subalgebra; **the connection can be brought to a representative in which only three generators appear, and that is a choice of representative rather than a property of the solution** — in another fixing condition all fifteen components of $A_{\imath}$ can be nonzero while $F_{\imath\jmath}$ stays inside the $\mathrm{su}(2)$. **That is not a defect of the solution but its construction**, and it is worth stating because it bears on the article's main point: **the object that requires fifteen generators to be written at all uses three of them at a time.**

**The embedding is a choice, and the choice is not unique.** $\mathrm{SU}(4)$ has more than one conjugacy class of $\mathrm{SU}(2)$ subgroups, distinguished by how the $\mathbf4$ decomposes: $\mathbf2\oplus\mathbf1\oplus\mathbf1$, $\mathbf3\oplus\mathbf1$, $\mathbf2\oplus\mathbf2$, and the irreducible $\mathbf4$ of the principal embedding. **The standard one is the block embedding $\mathbf2\oplus\mathbf1\oplus\mathbf1$, which is the most reducible and not the maximal one** — the principal embedding is what "maximal" would name — and the others are not computed here. **The action and the topological charge are the same for all of them**, because both know only the winding number; **the moduli count and the fluctuation spectrum are not**, and the table above is the block embedding's.

## Why the Algebra Cannot Hold It

**Three statements, in order of strength.**

- *Dimension.* The compact group of $\mathbb{B}$ is $\mathrm{U}(2)$, of real dimension four. **Fifteen generators do not fit**, so the field the instanton is built from is not an algebra element.
- *Topology.* The instanton exists because $\pi_{3}(\mathrm{SU}(4))=\mathbb{Z}$. **A winding number is a property of a map from the three-sphere into a group**, and the algebra has no three-sphere to map.
- *The bundle.* The integrality of the topological charge is a statement about a principal bundle over compactified four-space. **The algebra's elements are matrices, and a matrix is not a bundle.**

**So the instanton sits with the action, the fifteen generators and the $\mathrm{SU}(4)$ group itself on the transcribed side of the ceiling**, and the corpus's derived side — $\mathrm{SU}(2)$ and its abelian factor — is untouched by it. **That placement is the article's contribution**: the non-perturbative sector of the primordial force is a transcribed object, and no argument in the corpus derives it.

**What would be needed to derive it.** A four-dimensional algebra whose compact group had a nontrivial third homotopy group and enough dimension for the content. **The corpus's theorem is that no four-dimensional algebra reaches $\mathrm{SU}(3)$**, so such an algebra does not exist among the ones the corpus considers, and the instanton inherits the ceiling rather than escaping it.

## $\theta_4$ and the Questions It Raises

**Three statements about the parameter, and a fourth about what is absent.**

- *It is free in the Lagrangian.* No argument in the corpus fixes $\theta_4$; the group admits the term and nothing selects its coefficient.
- *It is not the strong-$CP$ parameter.* QCD's $\bar\theta$ is bounded below $10^{-10}$ by the neutron's electric dipole moment; **$\theta_4$ has no such measurement because the phase is not the one we live in**, and the two parameters are unrelated.
- *It is unobservable in this phase.* The phase does not extend to any scale at which it is measured — **and, more strongly, it is removable there**, which is what the next subsection shows.
- *There is no axion in the model, and none is needed.* A Peccei–Quinn field would be a new scalar at a new scale and the content is fixed at two fields; **but the absence is not a price paid, because the parameter such a field would relax is not physical above $M_C$.**

### The Anomaly Makes $\theta_4$ Removable, Not Physical

**Two anomalies are usually run together here, and only the second one concerns this term.**

- *The anomaly.* The triangle of three fixing condition currents vanishes for this content, because $\mathbf4$ and $\bar{\mathbf4}$ contribute oppositely and appear in equal number: $2A(\mathbf4)+2A(\bar{\mathbf4})=0$. **That is what makes the theory consistent**, and it is what *The $\mathrm{SU}(4)$ Model* proves by counting.
- *The axial anomaly.* The divergence of the axial current is proportional to $(g_4^{2}/16\pi^{2})\operatorname{tr}(F\tilde F)\sum_{f}2T(R_{f})$, **and every term in that sum is positive.** The two chiralities of a Dirac field add here instead of cancelling, so the coefficient is eight times a single fundamental Dirac field's, and it is not zero.

**So a chiral rotation does shift $\theta_4$, and above $M_C$ the shift costs nothing.** The sixteen are massless there: no Yukawa, because $\langle\Xi\rangle=0$, and no mass term, because the model sets $m=0$. A rotation that multiplies the $\mathbf4$ by $e^{i\alpha}$ and the $\bar{\mathbf4}$ by $e^{-i\alpha}$ then changes nothing in the Lagrangian except $\theta_4\to\theta_4+c\alpha$ with $c\ne0$, and $\alpha$ can be chosen to carry $\theta_4$ to zero. **Above $M_C$, then, $\theta_4$ is a coefficient of the Lagrangian and not a parameter of the phase.** The invariant is $\bar\theta_4=\theta_4+\arg\det m$, and setting $m=0$ fixes $\bar\theta_4$ at zero.

**What would make it physical is the mass term the phase does not write.** With massive fermions the rotation moves the phases of $m$ instead of removing $\theta_4$, and $\bar\theta_4$ becomes a genuine parameter — **that is QCD's situation and not this phase's.** Even then its effects would be weighted by $e^{-S}=1.1\times10^{-47}$, the estimate the previous section supplies.

**Two consequences, and both simplify the list above.** The unobservability is exact rather than an estimate: there is no $\theta_4$ dependence to suppress at $10^{-47}$. **And the missing axion is a non-issue rather than a cost** — a Peccei–Quinn field exists to relax a parameter, and this phase has none to relax. **The corpus does not thereby solve the strong-$CP$ problem**: $\theta_4$ above $M_C$ is not $\bar\theta$ below it, and the Standard Model's is the axion article's subject.

## The Checks

| claim | check | result |
| --- | --- | --- |
| the normalisation | $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$, Hermitian $t_{a}$ | $\frac{g^{2}}{16\pi^{2}}\int\operatorname{tr}F\tilde F=\frac{g^{2}}{32\pi^{2}}\int F_{a}\tilde F_{a}=1$ |
| the action | $8\pi^{2}/g_4^{2}$ | $108.2$ |
| the same from $\alpha_4$ | $2\pi/\alpha_4(M_X)$ | $108.2$ |
| the suppression | $e^{-108.2}$ | $1.1\times10^{-47}$ |
| the action at $M_C$ | $2\pi/\alpha_4(M_C)$ at $0.05776$ | $108.8$ |
| the moduli | $4N$ with $N=4$ | $16=4+1+11$ |
| the orientation count | $15-\dim[\mathrm{SU}(2)^{2}\times\mathrm{U}(1)]+3$ | $15-7+3=11$ |
| the excited generators | an $\mathrm{su}(2)$ inside $\mathrm{su}(4)$ | $3$ of $15$, in one representative |
| the size cutoff | the phase's end | $\rho\lesssim1/M_C$ |
| the $\theta_4$ period | $e^{2\pi i n}=1$ for integer $n$ | $2\pi$ |
| the anomaly | $2A(\mathbf4)+2A(\bar{\mathbf4})$ | $0$ |
| the axial coefficient | one per Weyl pair, all positive | $8$, not $0$ |

## Summary

**The primordial phase has instantons with action $108.2$, and the exponential is $1.1\times10^{-47}$.** The number is fixed by the same coupling that runs in the rest of the block, and it is the largest exponent the block contains.

**Sixteen moduli, eleven of them orientation**, because the solution is an $\mathrm{SU}(2)$ inside $\mathrm{SU}(4)$ and excites three generators at a time, in the representative that shows it. **The size modulus is cut off at $1/M_C$**, by the phase ending and not by the integral.

**$\theta_4$ is free in the Lagrangian with a $2\pi$ period, and redundant above $M_C$**: the anomaly cancels, the axial one does not, and massless fermions let the rotation remove the angle. **The strong-$CP$ problem is neither solved nor inherited** — $\theta_4$ is not $\bar\theta$, and the Standard Model's is another article's.

**And the whole construction is transcribed.** Winding numbers need a group with a three-sphere's worth of topology; $\mathrm{U}(2)$ has dimension four and fifteen generators do not fit in it. **The instanton is the clearest case in the corpus of a transcribed object with no derived counterpart**, and stating that is more useful than deriving a number that the algebra cannot hold.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mathbb{F}_{\imath\jmath}$ | $\sum_{a}F_{a,\imath\jmath}t_{a}$, the matrix-valued curvature, Hermitian |
| $\tilde{\mathbb{F}}$ | its dual, $\tfrac12\varepsilon\,\mathbb{F}$ |
| $\theta_{4}$ | the coefficient of the topological term: free in the Lagrangian, period $2\pi$, redundant above $M_C$ |
| $\bar\theta_4$ | $\theta_4+\arg\det m$, the rotation-invariant combination, zero here because $m=0$ |
| $S_{\mathrm{inst}}$ | $8\pi^{2}/g_4^{2}$, the instanton action |
| $\rho$ | the instanton's size modulus |
| $\pi_{3}(\mathrm{SU}(4))$ | $\mathbb{Z}$, the reason a winding number exists |

## Further Reading

- [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html). The term $\theta_4$ multiplies, and the trace-versus-pairing argument this article inherits.
- [The Primordial Coupling](the-primordial-coupling.html). The $\alpha_4$ from which the action is computed.
- [The Sixteen Weyl Fields Above $M_C$](the-sixteen-weyl-fields-above-m-c.html). The masslessness that makes $\theta_4$ removable, and the $m=0$ the removability is a statement about.
- [The Axion and the Peccei–Quinn Mechanism](the-axion-and-the-peccei-quinn-mechanism-in-biquaternionic-form.html). The parameter $\theta_4$ is not.
- [No Confinement Above $M_C$: Eleven E-Folds of Perturbative Coupling](no-confinement-above-m-c.html). The perturbative phase this non-perturbative sector sits in without changing.
- [The Compact Sector of the Biquaternions Is $\mathfrak{u}(2)$](the-compact-sector-of-the-biquaternions-is-u2.html). The ceiling this article places the instanton under.
