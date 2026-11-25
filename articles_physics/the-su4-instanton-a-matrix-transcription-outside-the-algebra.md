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

**The instanton exists, is enormous, and is transcribed rather than derived.** Its action is fixed by the same coupling that runs in [The Primordial Coupling](the-primordial-coupling-g4-as-a-boundary-condition-and-what-runs-above-m-c.html), and the $\theta_4$ that weights it is a free parameter of the model.

**Why "outside the algebra" and not merely "hard".** The instanton is a configuration of a gauge field on a four-dimensional space whose second Chern number is one. **Its existence is a statement about a $4\times4$ matrix field and about $\pi_3(\mathrm{SU}(4))=\mathbb{Z}$**, and the algebra $\mathbb{B}$ has compact group $\mathrm{U}(2)$ of real dimension four — far too small to contain fifteen generators, let alone a winding sector of them. **The instanton therefore stands exactly where the action stands: on the transcribed side of the ceiling**, and this article is where that placement is made explicit.

**What this article does.** It writes the topological term, computes the action and the suppression, counts the moduli, states the size-modulus cutoff, and locates the whole construction relative to the algebra.

**What it does not do.** It does not compute the $\theta_4$ dependence of any observable, does not build a dilute-gas model, and does not discuss the strong-$CP$ problem except to say why it does not arise here in the same form.

## The Topological Term

**One term, one coefficient, one periodicity.**

$$
\mathcal{L}_{\theta}=\theta_{4}\,\frac{g_4^{2}}{32\pi^{2}}\operatorname{tr}\bigl(\mathbb{F}_{\imath\jmath}\tilde{\mathbb{F}}_{\imath\jmath}\bigr),
\qquad
\tilde{\mathbb{F}}_{\imath\jmath}=\tfrac12\varepsilon_{\imath\jmath\kappa\lambda}\mathbb{F}_{\kappa\lambda},
$$

with $\mathbb{F}=\sum_{a}F_{a}T_{a}$ the matrix-valued curvature and the trace over colour, which for a Hermitian matrix is the whole of the contraction.

**The normalisation is the one that makes the integral an integer.**

$$
\frac{g_4^{2}}{32\pi^{2}}\int\operatorname{tr}\bigl(\mathbb{F}\tilde{\mathbb{F}}\bigr)\in\mathbb{Z}
\quad\text{equivalently}\quad
\frac{1}{16\pi^{2}}\int\operatorname{tr}\bigl(F_{\imath\jmath}\tilde F_{\imath\jmath}\bigr)\in\mathbb{Z}
$$

with $\operatorname{tr}(T_{a}T_{b})=\tfrac12\delta_{ab}$ in the second form — **the normalisation the whole block uses**, established from the printed arrays in [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html). **Two conventions and one integer**: the factor of two between them is the trace's, not the group's.

**The coefficient $\theta_4$ is free and the group does not fix it.** A total derivative does not affect the equations of motion, but it does affect the action of a configuration with nonzero winding, **so $\theta_4$ is a parameter of the phase and not a redundancy of the description.** The $2\pi$ periodicity follows from the integrality above: shifting $\theta_4$ by $2\pi$ multiplies the weight of every winding sector by $e^{2\pi i}=1$.

**Why the trace is the matrix trace and not a sum over generators.** $\operatorname{tr}(\mathbb{F}\tilde{\mathbb{F}})=\frac12F_{a}\tilde F_{a}$ by the normalisation, so the two agree as densities; **but the integrality statement is about the matrix trace of a bundle, and the sum over generators carries no bundle.** The distinction is the same one the parent article makes about the action's density, and it is sharper here: **a sum over fifteen generators of fifteen numbers is not a Chern class.**

## The Action and Its Size

**One number, and it is the largest number in the block.**

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

**What the number means, stated without inflation.** $1.1\times10^{-47}$ per unit four-volume in units of $M_C$ is not zero, and in a cosmological setting it would matter; **inside the phase, no observable of the block depends on it at any accuracy the block claims.** The article's point is not that the effect is negligible but that it is computable and large, **which is the opposite of the usual situation in a strongly coupled theory where the semi-classical expansion fails.**

**The value at the transition, for completeness.** $S(M_C)=2\pi/\alpha_4(M_C)=108.6$, **half a unit larger than at $M_X$**, because the coupling has barely moved over the interval between them. **The suppression is the same to two significant figures everywhere in the phase**, which is why the article quotes one number.

## The Moduli

**A single instanton has $4N=16$ parameters, and the split is exact for $\mathrm{SU}(N)$.**

| modulus | count | what it is |
| --- | --- | --- |
| translations | $4$ | where the instanton sits |
| dilatation | $1$ | its size $\rho$ |
| orientation | $11$ | how its $\mathrm{SU}(2)$ sits inside $\mathrm{SU}(4)$ |
| **total** | $\mathbf{16}$ | $4N$ with $N=4$ |

**The orientation count is $11$ and not $15$, and the difference is what the instanton does not use.** The solution is built by embedding an $\mathrm{SU}(2)$ in $\mathrm{SU}(4)$, so the orientation space is a coset and not the group; **eleven parameters are left after the stabiliser is quotiented out.** The arithmetic: $4N-5=11$.

**The instanton does not use all fifteen generators.** Its field strength lies in an $\mathrm{su}(2)$ subalgebra, so at any point in space the configuration excites three of the fifteen directions. **That is not a defect of the solution but its construction**, and it is worth stating because it bears on the article's main point: **the object that requires fifteen generators to be written at all uses three of them at a time.**

**The embedding is a choice, and the choice is not unique.** $\mathrm{SU}(4)$ has more than one conjugacy class of $\mathrm{SU}(2)$ subgroups, so there is more than one family of instanton-like solutions; **the standard one is the maximal embedding, and the others are not computed here.** The article's claim does not depend on which is chosen, because the action is the same for all of them.

## Why the Algebra Cannot Hold It

**Three statements, in order of strength.**

- *Dimension.* The compact group of $\mathbb{B}$ is $\mathrm{U}(2)$, of real dimension four. **Fifteen generators do not fit**, so the field the instanton is built from is not an algebra element.
- *Topology.* The instanton exists because $\pi_{3}(\mathrm{SU}(4))=\mathbb{Z}$. **A winding number is a property of a map from the three-sphere into a group**, and the algebra has no three-sphere to map.
- *The bundle.* The integrality of the topological charge is a statement about a principal bundle over compactified four-space. **The algebra's elements are matrices, and a matrix is not a bundle.**

**So the instanton sits with the action, the fifteen generators and the $\mathrm{SU}(4)$ group itself on the transcribed side of the ceiling**, and the corpus's derived side — $\mathrm{SU}(2)$ and its abelian factor — is untouched by it. **That placement is the article's contribution**: the non-perturbative sector of the primordial force is a transcribed object, and no argument in the corpus derives it.

**What would be needed to derive it.** A four-dimensional algebra whose compact group had a nontrivial third homotopy group and enough dimension for the content. **The corpus's theorem is that no four-dimensional algebra reaches $\mathrm{SU}(3)$**, so such an algebra does not exist among the ones the corpus considers, and the instanton inherits the ceiling rather than escaping it.

## $\theta_4$ and the Questions It Raises

**Three statements about the parameter, and a fourth about what is absent.**

- *It is free.* No argument in the corpus fixes $\theta_4$; the group admits the term and nothing selects its coefficient.
- *It is unobservable in this phase.* The phase does not extend to any scale at which it is measured, and its effects are weighted by $10^{-47}$.
- *It is not the strong-$CP$ parameter.* QCD's $\bar\theta$ is measured to be smaller than $10^{-10}$ by the neutron's electric dipole moment; **$\theta_4$ has no such measurement because the phase is not the one we live in**, and the two parameters are unrelated.
- *There is no axion in the model.* A Peccei–Quinn field would be a new scalar with a new scale, and the content is fixed at two fields. **The $\theta_4$ question is therefore not solved, it is relocated** to a phase where it does not matter.

**And the anomaly does not remove it.** A rotation of the fermions by a chiral phase shifts $\theta_4$ by an amount fixed by the anomaly coefficient, and the corpus's sixteen are paired so that the anomaly cancels — **which is why the shift is zero and $\theta_4$ is physical rather than removable.** A content with a nonzero anomaly would have let $\theta_4$ be rotated away, and this one does not.

## The Checks

| claim | check | result |
| --- | --- | --- |
| the normalisation | $\operatorname{tr}(T_{a}T_{b})=\tfrac12\delta_{ab}$ | $\frac{g^{2}}{32\pi^{2}}\int\operatorname{tr}F\tilde F\in\mathbb{Z}$ |
| the action | $8\pi^{2}/g_4^{2}$ | $108.2$ |
| the same from $\alpha_4$ | $2\pi/\alpha_4(M_X)$ | $108.2$ |
| the suppression | $e^{-108.2}$ | $1.1\times10^{-47}$ |
| the action at $M_C$ | $2\pi/0.0578$ | $108.6$ |
| the moduli | $4N$ with $N=4$ | $16=4+1+11$ |
| the orientation count | $4N-5$ | $11$ |
| the excited generators | an $\mathrm{su}(2)$ inside $\mathrm{su}(4)$ | $3$ of $15$ |
| the size cutoff | the phase's end | $\rho\lesssim1/M_C$ |
| the $\theta_4$ period | integrality of the charge | $2\pi$ |

## Summary

**The primordial phase has instantons with action $108.2$, and the exponential is $1.1\times10^{-47}$.** The number is fixed by the same coupling that runs in the rest of the block, and it is the largest number the block contains.

**Sixteen moduli, eleven of them orientation**, because the solution is an $\mathrm{SU}(2)$ inside $\mathrm{SU}(4)$ and excites three generators at a time. **The size modulus is cut off at $1/M_C$**, by the phase ending and not by the integral.

**$\theta_4$ is a free parameter with a $2\pi$ period, physical because the content is anomaly-free, and unobservable because the phase is not ours.** The strong-$CP$ problem is not solved; it is placed where it cannot be measured.

**And the whole construction is transcribed.** Winding numbers need a group with a three-sphere's worth of topology; $\mathrm{U}(2)$ has dimension four and fifteen generators do not fit in it. **The instanton is the clearest case in the corpus of a transcribed object with no derived counterpart**, and stating that is more useful than deriving a number that the algebra cannot hold.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mathbb{F}_{\imath\jmath}$ | $\sum_{a}F_{a,\imath\jmath}T_{a}$, the matrix-valued curvature |
| $\tilde{\mathbb{F}}$ | its dual, $\tfrac12\varepsilon\,\mathbb{F}$ |
| $\theta_{4}$ | the coefficient of the topological term, free, period $2\pi$ |
| $S_{\mathrm{inst}}$ | $8\pi^{2}/g_4^{2}$, the instanton action |
| $\rho$ | the instanton's size modulus |
| $\pi_{3}(\mathrm{SU}(4))$ | $\mathbb{Z}$, the reason a winding number exists |

## Further Reading

- [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html). The term $\theta_4$ multiplies, and the trace-versus-pairing argument this article inherits.
- [The Primordial Coupling](the-primordial-coupling-g4-as-a-boundary-condition-and-what-runs-above-m-c.html). The $\alpha_4$ from which the action is computed.
- [Why There Is No Confinement Above $M_C$](why-there-is-no-confinement-above-m-c.html). The perturbative phase this non-perturbative sector sits in without changing.
- [Why the Biquaternion Algebra Reaches $SU(2)$ but Not $SU(3)$](why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html). The ceiling this article places the instanton under.
