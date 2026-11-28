# __The Failure Modes of the Diagram Expansion: Gauge Fixing, Renormalisation, Asymptotic Series and Strong Coupling__

## Introduction

**The claim.** The method of [the four stages](the-lagrangian-method-from-the-collected-lagrangian-to-the-feynman-diagram.html) fails in four ways, and each failure is located. The quadratic part may not be invertible, and then there is no propagator until a representative is fixed. The series may be asymptotic, and then a fixed-order truncation is an approximation whose error grows past an optimal order. The loops may diverge, and then the parameters must be redefined order by order. And the coupling may be large, and then the expansion parameter is of order one and the route says nothing.

**Why the article exists.** A method stated without its failures is a claim of universal competence, and this method has none. The corpus's discipline is that a computation states its domain; [Five Steps from a Lagrangian to Fluid Equations](five-steps-from-a-lagrangian-to-fluid-equations.html) states its five failures the same way, one per step. This article does it for the four stages, one per failure, with the repairing object named.

**The strongest objection.** *If it fails four ways, why use it.* Because each failure is a boundary and not a refutation, and a boundary that is known is a computation with a stated domain. The alternatives — a lattice, a bootstrap, a holographic dual — are different methods with their own boundaries, and none of them is the corpus's. The method's case is that it answers a large class of questions exactly at each order, with the error of truncation and the regime of validity both stated.

**Position.** The section's last article, and the one that keeps the section from overclaiming. It cites the corpus's articles that own each repair and adds no new physics to them.

## The First Failure: The Quadratic Part Is Not Invertible

**A gauge field's quadratic kernel has a zero eigenvalue, and the zero mode is the orbit.** For the connection, the unfixed kernel is $p^{2}\delta_{\imath\jmath}-p_{\imath}p_{\jmath}$, and it annihilates the momentum itself,

$$
\bigl(p^{2}\delta_{\imath\jmath}-p_{\imath}p_{\jmath}\bigr)p_{\jmath}=p^{2}p_{\imath}-p_{\imath}p^{2}=0 ,
$$

so there is no inverse and no propagator. The statement was checked on one hundred random momenta: the residual $\lVert Kp\rVert/\lVert p\rVert$ never exceeded $1.1\times10^{-15}$ and the kernel's smallest eigenvalue never exceeded $2\times10^{-15}$, while adding $M^{2}\delta_{\imath\jmath}$ gave smallest eigenvalue $M^{2}$ to machine precision. The zero mode is not a numerical accident; it is the local symmetry seen at the level of the free theory.

**The repair is a fixing condition, and the price is two new sectors.** Adding $-\frac{1}{2\zeta}(\partial\cdot A)^{2}$ makes the kernel invertible, and the Faddeev–Popov identity supplies the ghost determinant that keeps unitarity. The resulting propagator is the $R_{\xi}$ family,

$$
\frac{P}{\Pi-M^{2}}+\frac{\zeta L}{\Pi-\zeta M^{2}},
$$

with $\zeta=1$ the Feynman–'t Hooft choice, $\zeta=0$ the Landau choice and $\zeta\to\infty$ the Proca propagator. [Fixing the Representative in the Electroweak Theory](fixing-the-representative-in-the-electroweak-theory-r-xi-conditions-ghosts-and-the-goldstone-equivalence-theorem.html) states the three and the $\zeta$-pole that the Goldstone and the ghost share; [The Connection Path Integral](the-connection-path-integral-in-biquaternionic-form.html) states the identity; [BRST Symmetry](brst-symmetry-in-biquaternionic-form.html) states why the ghost's minus sign preserves unitarity.

**The failure is structural and it is not the algebra's.** The kernel is singular because the density is invariant under a local transformation, and that invariance is a property of any transcription. What the algebra adds is the axis of the deformation, not the existence of the zero mode.

| the parameter | the propagator | what it is |
|---|---|---|
| $\zeta=1$ | $\delta_{\imath\jmath}/(\Pi-M^{2})$ | Feynman–'t Hooft, the pole at the physical mass |
| $\zeta=0$ | $P/(\Pi-M^{2})$ | Landau, the transverse part alone |
| $\zeta\to\infty$ | the Proca form | the unitary gauge, the Goldstones removed |

## The Second Failure: The Series Is Asymptotic

**The expansion in the coupling has zero radius of convergence, and the reason is the growth of the coefficients.** The standard illustration is the integral $\int_{-\infty}^{\infty}\mathrm{d}x\,\exp\bigl(-\tfrac12x^{2}-\lambda x^{4}\bigr)$, whose expansion in $\lambda$ has coefficients growing factorially. Computing them to one hundred orders gave $\lvert a_{k}\rvert^{1/k}$ equal to $54.25$, $111.11$, $284.97$ and $577.20$ at $k=10,20,50,100$, so the radius is zero: the coefficients outrun any exponential.

**The consequence is visible in one number.** At $\lambda=0.1$ the exact integral is $2.1497$ and the series' terms are $0.752$, $-1.316$, $4.343$ and $-21.17$, so the partial sums run $1.7546$, $3.0706$, $-1.2721$ and $19.8987$. They do not approach the answer; they leave it, and continue to leave it. A fixed-order truncation is therefore an approximation whose error falls until an optimal order and then grows, and the optimal order is not known without a non-perturbative estimate.

**The honest statement, in one sentence.** The method computes each order exactly and never computes the sum exactly. That is the same sentence as the corpus's general statement about the method, and it is the one a reader should be able to repeat.

**What is not a failure.** The per-order exactness is real: the coefficient at order $n$ is right, and it is right for all $n$ that anyone computes. The series' divergence is a statement about the limit and not about any term.

## The Third Failure: The Loops Diverge

**The loop integrals are divergent, and the divergence is power-counting's.** The one-loop two-point integral grows like $\Lambda^{2}$, as [stage $4$](the-feynman-rules-and-the-diagram-expansion-propagators-vertices-loops-and-symmetry-factors.html) records with the ratio to $\Lambda^{2}$ approaching $\pi^{2}$; the four-point integral grows like $\log\Lambda$; and in a non-renormalisable theory the divergences multiply with the order.

**The repair is absorption, and the criterion is that the absorption works at every order.** Write the bare parameters as physical ones plus counterterms, choose the counterterms to cancel the divergences order by order, and the criterion of renormalisability is that finitely many counterterms suffice at every order. Where it does, the theory has predictive content: finitely many measurements fix the parameters and every other number is a prediction. Where it does not, the theory is an effective one with a cutoff and a stated range.

**The absorbed divergence becomes a flow, and the flow is the theory's scale dependence.** [The Renormalization Group](the-renormalization-group-in-biquaternionic-form.html) states the Wetterich equation, the shell integration and the beta functions; [The Conformal Anomaly](the-conformal-anomaly-in-biquaternionic-form.html) states the one-loop trace anomaly that no classical symmetry forbids; [The Index Theorem and the Zero-Mode Count](the-index-theorem-and-the-zero-mode-count-in-biquaternionic-form.html) states the topological half. The corpus's position on all three is the same and it is stated in each: the flow, the coefficients and the fixed points are transcribed, and what the algebra supplies is the central scalar that makes the cutoff sector-blind.

**The failure is a property of the integral and not of the density.** A divergence is what an integral over infinitely many modes does; every transcription meets it.

## The Fourth Failure: Strong Coupling

**The expansion parameter is the coupling, so a coupling of order one ends the method.** When $g\gtrsim1$ the terms of the series do not fall, the optimal truncation is at order zero, and the diagrams say nothing. The failure is not a lack of ingenuity; it is the statement that the series was organised by a parameter that is not small.

**Four classes of physics are invisible order by order, and each has a name.** Confinement: the potential between two charges grows with separation, which no finite set of exchanged gluons produces. Chiral symmetry breaking: the pseudoscalar octet's masslessness in the chiral limit is a property of the vacuum and not of any vertex. Instantons and monopoles: solutions of the classical equation that are not connected to the perturbative vacuum and therefore appear in no Taylor coefficient. Phase transitions: a non-analyticity in a parameter, which a power series cannot represent.

**The corpus's position is that these are cited and not derived.** [Hadron Structure from QCD](hadron-structure-from-qcd-the-bound-state-problem.html) states the bound-state gap; [The Skyrme Model and the Topological Baryon](the-skyrme-model-and-the-topological-baryon-in-biquaternionic-form.html) states the topological sector as the corpus's nearest approach to a non-perturbative object; and the strong sector's numbers in the corpus are transcriptions.

**The failure is the method's, not the algebra's.** Nothing in $\mathbb B$ makes a coupling large or small; the coupling is a coefficient in a density, and the density is physics.

## The Four in One Table

| failure | the symptom | the repair, or the regime | the article that owns it |
|---|---|---|---|
| the quadratic part is not invertible | the kernel has a zero eigenvalue on the orbit | gauge fixing and ghosts; the $R_{\xi}$ family | [$R_{\xi}$](fixing-the-representative-in-the-electroweak-theory-r-xi-conditions-ghosts-and-the-goldstone-equivalence-theorem.html) |
| the series is asymptotic | coefficients grow factorially; zero radius | truncate and estimate; the error is bounded by the first omitted term | this article's section on the second failure |
| the loops diverge | power divergences at every order | counterterms, order by order; renormalisability as the criterion | [the renormalization group](the-renormalization-group-in-biquaternionic-form.html) |
| the coupling is large | the expansion parameter is of order one | a different method; diagrams say nothing | [hadron structure](hadron-structure-from-qcd-the-bound-state-problem.html) |

**The four are independent, and a computation can meet two at once.** QCD at low momentum meets the fourth and, through its bound states, the fourth's consequences; QED meets the second and the third and never the first or the fourth at accessible energies.

## What the Four Have in Common

**Each is a property of the method and none is a property of the algebra.** That is the article's close and the section's. The zero mode, the factorial growth, the divergence and the large coupling would be there in any transcription of the same integral, because they are properties of the integral. What the algebra changes is where each one is *read*: the zero mode is the orbit in $\mathbb B_\Phi$, the divergence is regulated on the central scalar, and the coupling is a coefficient in a density built from the corpus's pairings.

**The ledger, therefore, is not a scoreboard of successes and failures.** It is a list of what each stage reads and what it does not. A reader who wants the corpus's honest position on the method reads this article with the other six, and the position is: four stages, one exact inversion, one asymptotic series, four located failures, and no claim that any of it is derived from $\mathbb B$.

## Summary

**The method fails in four ways, and each failure has a location and a repair.** The quadratic kernel may be singular on the gauge orbit, and fixing plus ghosts repairs it. The series may diverge factorially, and there is no repair beyond truncation with a stated error. The loops may diverge, and counterterms absorb them order by order where the theory is renormalisable. The coupling may be large, and then the method has nothing to say.

**Each failure was illustrated with a computation in this article's section.** The kernel's zero mode had residual $1.1\times10^{-15}$ and smallest eigenvalue $2\times10^{-15}$; the toy series' coefficients had $\lvert a_{k}\rvert^{1/k}$ rising to $577$ at $k=100$ and its partial sums left the exact value; and the one-loop integral's ratio to $\Lambda^{2}$ approached $\pi^{2}$.

**All four are properties of the method and not of the algebra.** The corpus's contribution is to read each one in its own terms and to cite the article that owns the repair, and that is what this section claims and no more.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\zeta$ | the gauge-fixing parameter, $\xi$ in the older literature |
| $M$, $\Pi$ | the mass and the positive momentum invariant of the $R_{\xi}$ propagator |
| $P$, $L$ | the transverse and longitudinal projectors |
| $a_{k}$ | the $k$-th coefficient of the toy integral's expansion |
| $\Lambda$ | a momentum cutoff |
| $g$ | a coupling, the expansion parameter |

## Further Reading

- [Fixing the Representative in the Electroweak Theory: $R_{\xi}$ Conditions, Ghosts and the Goldstone Equivalence Theorem](fixing-the-representative-in-the-electroweak-theory-r-xi-conditions-ghosts-and-the-goldstone-equivalence-theorem.html), the first failure and its repair.
- [The Connection Path Integral in Biquaternionic Form](the-connection-path-integral-in-biquaternionic-form.html), the Faddeev–Popov identity and the ghost determinant.
- [BRST Symmetry in Biquaternionic Form](brst-symmetry-in-biquaternionic-form.html), why the ghost's sign preserves unitarity.
- [The Renormalization Group in Biquaternionic Form](the-renormalization-group-in-biquaternionic-form.html), the third failure's repair and the flow it defines.
- [Hadron Structure from QCD: The Bound-State Problem](hadron-structure-from-qcd-the-bound-state-problem.html), the fourth failure in the corpus's own strong sector.
- [The Lagrangian Method: From the Collected Lagrangian to the Feynman Diagram](the-lagrangian-method-from-the-collected-lagrangian-to-the-feynman-diagram.html), the method whose four failures these are.
