# __The Limits of the Expansion: Gauge Fixing, Asymptotic Series and Strong Coupling__

## Introduction

**The claim.** The method of [the four stages](the-lagrangian-method-from-a-truncated-effective-lagrangian-to-the-feynman-diagram.html) stops being an approximation in three places, and each is located. The quadratic part may not be invertible, and then there is no propagator until a representative is fixed. The series may be asymptotic, and then a fixed-order truncation is an approximation whose error grows past an optimal order. And the coupling may be large, and then the expansion parameter is of order one and the route says nothing.

**Three, not four.** An earlier statement of this article listed a fourth: the divergence of the loop integrals. That was a category error, and the correction is the reason [Renormalisation as an Operation](renormalisation-as-an-operation-the-arbitrary-scale.html) now stands between the diagram expansion and this article. A boundary is a place where the method stops applying *even when performed perfectly*. Gauge fixing, asymptotic series and strong coupling are such places. The divergences are not: the scale is an operation the method performs, correctly or incorrectly, in every theory and at every order. Filing it as a boundary made the method look fragile and hid the one operation a reader must master before the boundaries can be stated.

**Non-renormalisability is not a fourth boundary either, and the reason is the same.** An effective Lagrangian carries operators above the marginal degree, so its divergences need the operators of each order and the list does not close. That is the price of the label, stated in [the parameterised action](the-parameterised-action-an-ordered-family-of-effective-field-theories.html) and paid at every order by [the operation](renormalisation-as-an-operation-the-arbitrary-scale.html). A method that filed it as a boundary would have to file every truncation as a failure, and every calculation in this section is a truncation.

**Why the article exists.** A method stated without its failures is a claim of universal competence, and this method has none. The corpus's discipline is that a computation states its domain; [Five Steps from a Lagrangian to Fluid Equations](five-steps-from-a-lagrangian-to-fluid-equations.html) states its five failures the same way, one per step. This article does it for the four stages, one per boundary, with the repairing object named where a repair exists.

**The strongest objection.** *If it fails three ways, why use it.* Because each failure is a boundary and not a refutation, and a boundary that is known is a computation with a stated domain. The alternatives — a lattice, a bootstrap, a holographic dual — are different methods with their own boundaries, and none of them is the corpus's. The method's case is that it answers a large class of questions exactly at each order, with the error of truncation and the regime of validity both stated.

**Position.** The section's last article, and the one that keeps the section from overclaiming. It cites the corpus's articles that own each repair and adds no new physics to them.

## The First Boundary: The Quadratic Part Is Not Invertible

**A gauge field's quadratic kernel has a zero eigenvalue, and the zero mode is the orbit.** For the connection, the unfixed kernel is $p^{2}\delta_{\imath\jmath}-p_{\imath}p_{\jmath}$, and it annihilates the momentum itself,

$$
\bigl(p^{2}\delta_{\imath\jmath}-p_{\imath}p_{\jmath}\bigr)p_{\jmath}=p^{2}p_{\imath}-p_{\imath}p^{2}=0 ,
$$

so there is no inverse and no propagator. The statement is not numerical: the kernel's spectrum is $\{p^{2},p^{2},0\}$ exactly, since $p^{2}p_{\imath}-p_{\imath}(p\cdot p)=0$ identically, so $p$ is a zero eigenvector for every momentum and the zero is not a coincidence of rounding. Adding $M^{2}\delta_{\imath\jmath}$ moves that eigenvalue to $M^{2}$ and leaves the other two at $p^{2}+M^{2}$, so the deformed kernel is invertible and its smallest eigenvalue is $M^{2}$. The zero mode is the orbit of the local symmetry seen at the level of the free theory.

**The repair is a fixing condition, and the price is two new sectors.** Adding $-\frac{1}{2\zeta}(\partial\cdot A)^{2}$ makes the kernel invertible, and the Faddeev–Popov identity supplies the ghost determinant that keeps unitarity. The resulting propagator is the $R_{\xi}$ family,

$$
\frac{P}{\Pi-M^{2}}+\frac{\zeta L}{\Pi-\zeta M^{2}},
$$

with $\zeta=1$ the Feynman–'t Hooft choice, $\zeta=0$ the Landau choice and $\zeta\to\infty$ the Proca propagator. [Fixing the Representative in the Electroweak Theory](fixing-the-representative-in-the-electroweak-theory-r-xi-conditions-ghosts-and-the-goldstone-equivalence-theorem.html) states the three and the $\zeta$-pole that the Goldstone and the ghost share; [The Connection Path Integral](the-connection-path-integral-in-biquaternionic-form.html) states the identity; [BRST Symmetry](brst-symmetry-in-biquaternionic-form.html) states why the ghost's minus sign preserves unitarity.

**The boundary is structural and it is not the algebra's.** The kernel is singular because the density is invariant under a local transformation, and that invariance is a property of any transcription. What the algebra adds is the axis of the deformation, not the existence of the zero mode.

| the parameter | the propagator | what it is |
|---|---|---|
| $\zeta=1$ | $\delta_{\imath\jmath}/(\Pi-M^{2})$ | Feynman–'t Hooft, the pole at the physical mass |
| $\zeta=0$ | $P/(\Pi-M^{2})$ | Landau, the transverse part alone |
| $\zeta\to\infty$ | the Proca form | the unitary gauge, the Goldstones removed |

## The Second Boundary: The Series Is Asymptotic

**The expansion in the coupling has zero radius of convergence, and the reason is the growth of the coefficients.** The standard illustration is the integral $\int_{-\infty}^{\infty}\mathrm{d}x\,\exp\bigl(-\tfrac12x^{2}-\lambda x^{4}\bigr)$, whose expansion in $\lambda$ has coefficients $a_{k}=(-1)^{k}(4k-1)!!\sqrt{2\pi}/k!$ growing factorially. Computing them in logarithms to one hundred orders gave $\lvert a_{k}\rvert^{1/k}$ equal to $49.49$, $106.12$, $279.78$ and $571.92$ at $k=10,20,50,100$ — rising like $\frac{16k}{e}$ — so the radius is zero: the coefficients outrun any exponential.

**The consequence is visible in one number.** At $\lambda=0.1$ the exact integral is $2.1497$ and the series' terms are $-0.752$, $1.316$, $-4.343$ and $21.17$, so the partial sums run $1.7546$, $3.0706$, $-1.2721$ and $19.8987$. They do not approach the answer; they leave it, and continue to leave it. A fixed-order truncation is therefore an approximation whose error falls until an optimal order and then grows, and the optimal order is not known without a non-perturbative estimate.

**The honest statement, in one sentence.** The method computes each order exactly and never computes the sum exactly. That is the same sentence as the corpus's general statement about the method, and it is the one a reader should be able to repeat.

**What is not a failure.** The per-order exactness is real: the coefficient at order $n$ is right, and it is right for all $n$ that anyone computes. The series' divergence is a statement about the limit and not about any term.

## The Third Boundary: Strong Coupling

**The expansion parameter is the coupling, so a coupling of order one ends the method.** When $g\gtrsim1$ the terms of the series do not fall, the optimal truncation is at order zero, and the diagrams say nothing. The failure is not a lack of ingenuity; it is the statement that the series was organised by a parameter that is not small.

**Four classes of physics are invisible order by order, and each has a name.** Confinement: the potential between two charges grows with separation, which no finite set of exchanged gluons produces. Chiral symmetry breaking: the pseudoscalar octet's masslessness in the chiral limit is a property of the vacuum and not of any vertex. Instantons and monopoles: solutions of the classical equation that are not connected to the perturbative vacuum and therefore appear in no Taylor coefficient. Phase transitions: a non-analyticity in a parameter, which a power series cannot represent.

**The corpus's position is that these are cited and not derived.** [Hadron Structure from QCD](hadron-structure-from-qcd-the-bound-state-problem.html) states the bound-state gap; [The Skyrme Model and the Topological Baryon](the-skyrme-model-and-the-topological-baryon-in-biquaternionic-form.html) states the topological sector as the corpus's nearest approach to a non-perturbative object; and the strong sector's numbers in the corpus are transcriptions.

**The boundary is the method's, not the algebra's.** Nothing in $\mathbb B$ makes a coupling large or small; the coupling is a coefficient in a density, and the density is physics.

## The Three in One Table

| failure | the symptom | the repair, or the regime | the article that owns it |
|---|---|---|---|
| the quadratic part is not invertible | the kernel has a zero eigenvalue on the orbit | gauge fixing and ghosts; the $R_{\xi}$ family | [$R_{\xi}$](fixing-the-representative-in-the-electroweak-theory-r-xi-conditions-ghosts-and-the-goldstone-equivalence-theorem.html) |
| the series is asymptotic | coefficients grow factorially; zero radius | truncate at the optimal order; the error there is of the order of the first omitted term | this article's section on the second failure |
| the coupling is large | the expansion parameter is of order one | a different method; diagrams say nothing | [hadron structure](hadron-structure-from-qcd-the-bound-state-problem.html) |

**The three are independent, and a computation can meet two at once.** QCD at low momentum meets the third and, through its bound states, the third's consequences; QED meets only the second at accessible energies — with a series that is asymptotic like every series in this method — and never the first or the third.

## What the Three Have in Common

**Each is a property of the method and none is a property of the algebra.** That is the article's close and the section's. The zero mode, the factorial growth and the large coupling would be there in any transcription of the same integral, because they are properties of the integral. What the algebra changes is where each one is *read*: the zero mode is the orbit in $\mathbb B_\Phi$, and the coupling is a coefficient in a density built from the corpus's pairings.

**The ledger, therefore, is not a scoreboard of successes and failures.** It is a list of what each stage reads and what it does not. A reader who wants the corpus's honest position on the method reads this article with the other six, and the position is: four stages, one exact inversion, one asymptotic series, three located boundaries, one operation that is not a boundary, and no claim that any of it is derived from $\mathbb B$.

## Summary

**The method stops being an approximation in three places, and each has a location and, where one exists, a repair.** The quadratic kernel may be singular on the orbit, and fixing plus ghosts repairs it. The series may diverge factorially, and there is no repair beyond truncation with a stated error. The coupling may be large, and then the method has nothing to say.

**Renormalisation is not among them.** It is an operation the method performs — define, fix, evolve — and its failure mode is an arithmetic error, not a limit.

**Two of the three were illustrated with a computation in this article's section.** The kernel's zero mode is exact rather than numerical — its spectrum is $\{p^{2},p^{2},0\}$ because $Kp=0$ identically, and the deformation moves the zero to $M^{2}$; and the toy series' coefficients had $\lvert a_{k}\rvert^{1/k}$ rising to $571.92$ at $k=100$, with partial sums that left the exact value $2.1497$.

**All three are properties of the method and not of the algebra.** The corpus's contribution is to read each one in its own terms and to cite the article that owns the repair, and that is what this section claims and no more.

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

- [Fixing the Representative in the Electroweak Theory: $R_{\xi}$ Conditions, Ghosts and the Goldstone Equivalence Theorem](fixing-the-representative-in-the-electroweak-theory-r-xi-conditions-ghosts-and-the-goldstone-equivalence-theorem.html), the first boundary and its repair.
- [The Connection Path Integral in Biquaternionic Form](the-connection-path-integral-in-biquaternionic-form.html), the Faddeev–Popov identity and the ghost determinant.
- [BRST Symmetry in Biquaternionic Form](brst-symmetry-in-biquaternionic-form.html), why the ghost's sign preserves unitarity.
- [Renormalisation as an Operation: The Arbitrary Scale](renormalisation-as-an-operation-the-arbitrary-scale.html), the fourth item that was previously listed here and is not a boundary.
- [Hadron Structure from QCD: The Bound-State Problem](hadron-structure-from-qcd-the-bound-state-problem.html), the third boundary in the corpus's own strong sector.
- [The Lagrangian Method: From a Truncated Effective Lagrangian to the Feynman Diagram](the-lagrangian-method-from-a-truncated-effective-lagrangian-to-the-feynman-diagram.html), the method whose three boundaries these are.
