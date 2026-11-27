# __The Closed-Time-Path Action: One Action on Two Branches__

## Introduction

**The claim.** A dissipative equation has no action on one history — that is [Helmholtz's theorem](the-inverse-problem-of-the-calculus-of-variations-helmholtz-conditions.html), and it is exact. It has an action on **two** histories: one forward along the contour and one backward, with the two branches identified at the final time. **The closed-time-path action is that object**, and it is how the corpus's dissipative fluid acquires a variational origin without pretending that the theorem does not hold.

**What is established.** Four things. First, the contour and the doubled field, and the normalisation identity that makes the doubling a bookkeeping device and not a second theory. Second, the variation on each branch, and the Keldysh rotation that turns the pair into a retarded, an advanced and a noise component. Third, where the dissipation went: into a branch-coupling term, the **influence functional**, whose real part is the Rayleigh function and whose imaginary part is the noise, related by the fluctuation–dissipation theorem. Fourth, what the theorem's price is: a doubled field, a pair of histories in place of one, and a noise that cannot be switched off while the dissipation is kept.

**Why it belongs in the departures.** The subsection's other articles write the constitutive form of a dissipative fluid — the relaxation times, the entropy production, the causal correction to the equation of state. **Those are the macroscopic face; this is the microscopic one**, and the relation between them is that the coefficients the hydrodynamic articles carry as parameters are the moments of the influence functional this article writes.

**What the algebra does and does not do.** The corpus is already a doubled object — two sectors, $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{\Psi}$ — and the temptation to identify that doubling with this one is the article's main warning. **They are different doublings with different meanings**, and §*Two Doublings That Are Not the Same* separates them.

## The Contour and the Doubled Field

**The contour.** Take the time axis from an initial time to $t_f$ and back. The field takes a value on the forward branch and a value on the backward branch, and the two agree at $t_f$ where the contour turns:

$$
\tilde\Xi_+(t_f)=\tilde\Xi_-(t_f).
$$

**The initial condition is not paired**: the state at the initial time is the density matrix, and the two branches leave it in opposite directions. **The contour is a closed loop with one open end**, which is exactly the structure a density matrix's evolution has.

**The generating functional.**

$$
Z[J_+,J_-]=\int\mathcal D\tilde\Xi_+\,\mathcal D\tilde\Xi_-\;
\exp\Bigl(iS[\tilde\Xi_+]-iS[\tilde\Xi_-]+i\!\int\!J_+\tilde\Xi_+-i\!\int\!J_-\tilde\Xi_-\Bigr),
$$

with $S$ in the units of the action quantum, as [the functional-integral article](the-functional-integral-in-biquaternionic-form.html) writes it. **The action is the difference of the branches' actions** — the forward evolution minus the backward one, which is what a trace over a density matrix produces.

**The identity that makes it a bookkeeping device.** Set $J_+=J_-=J$. Then the two branches' contributions cancel exactly, the contour closes, and

$$
Z[J,J]=1 .
$$

**A generating functional that equals one at coincident sources generates only connected correlations between different times**, which is the statement that the doubling has introduced no new dynamics: it has introduced a *bookkeeping* for the two ends of a correlation function. **That identity is the reason the formalism is safe**, and a reader who checks one equation in this article should check that one.

**The physical sources.** Write the combinations

$$
J_{\mathrm{cl}}=\tfrac12(J_++J_-),\qquad J_{\mathrm{q}}=J_+-J_- ,
$$

the mean source and the difference. **The difference is the one that couples to the quantum component**, and it is the one that is set to zero at the end: $J_{\mathrm{q}}=0$ is the statement that the two branches are treated alike, which is the statement that the evolution is unitary.

## The Variation on Each Branch

**Two variations, two equations.** Varying $Z$ with respect to $\tilde\Xi_+$ and $\tilde\Xi_-$ gives

$$
\frac{\delta S}{\delta\tilde\Xi_+}=J_+,\qquad
\frac{\delta S}{\delta\tilde\Xi_-}=J_- ,
$$

the field equation on each branch. **For a closed system these are two copies of one equation**, and the branches are coupled only through the final-time identification; nothing dissipative has appeared, and nothing should have.

**Where a dissipative equation comes from, stated precisely.** Couple the field to an environment and integrate the environment out. The result is an extra term in the exponent that depends on both branches,

$$
\exp\bigl(iS[\tilde\Xi_+]-iS[\tilde\Xi_-]\bigr)\;\longrightarrow\;
\exp\bigl(iS[\tilde\Xi_+]-iS[\tilde\Xi_-]\bigr)\;\mathcal F[\tilde\Xi_+,\tilde\Xi_-],
$$

with $\mathcal F$ the **influence functional**. **It is nonlocal in time, it is not a difference of two single-branch actions, and it is where every dissipative term in the corpus ultimately lives.** A reader who wants the origin of a transport coefficient should look here; a reader who wants its constitutive form should look in the hydrodynamic articles.

**The classical limit, and the equation it gives.** In the limit where the contour's width is small and the field is near-classical, the influence functional's variation with respect to the quantum component produces a **Langevin equation**: the deterministic part is the classical equation with a frictional term, and the stochastic part is a source whose correlation is fixed by the functional's imaginary part. **One action, two branches, and a stochastic equation as the classical limit** — the noise is not added, it is what remains of the other branch.

## The Keldysh Rotation, and the Three Equations

**Rotate to the physical combinations.** Define

$$
\tilde\Xi_{\mathrm{cl}}=\tfrac12\bigl(\tilde\Xi_++\tilde\Xi_-\bigr),\qquad
\tilde\Xi_{\mathrm{q}}=\tilde\Xi_+-\tilde\Xi_- ,
$$

the mean field and the difference. **The quadratic part of the doubled action then takes the standard form**

$$
S_{\mathrm{CTP}}^{(2)}=\int \tilde\Xi_{\mathrm{q}}\,\hat K_{\mathrm{adv}}\,\tilde\Xi_{\mathrm{cl}}
+\int \tilde\Xi_{\mathrm{cl}}\,\hat K_{\mathrm{ret}}\,\tilde\Xi_{\mathrm{q}}
+\int \tilde\Xi_{\mathrm{q}}\,\hat K_{\mathrm{K}}\,\tilde\Xi_{\mathrm{q}} ,
$$

with $\hat K_{\mathrm{ret}}$ and $\hat K_{\mathrm{adv}}$ the retarded and advanced kernels and $\hat K_{\mathrm{K}}$ the Keldysh one. **Three components, and each has a name and a role.**

| component | what it multiplies | what its variation gives | what it is |
| --- | --- | --- | --- |
| $\tilde\Xi_{\mathrm{q}}\hat K_{\mathrm{adv}}\tilde\Xi_{\mathrm{cl}}$ | mean field × difference | the mean field's equation, with the Keldysh term as its source | the **retarded** response |
| $\tilde\Xi_{\mathrm{cl}}\hat K_{\mathrm{ret}}\tilde\Xi_{\mathrm{q}}$ | difference × mean field | the difference's equation | the **advanced** response |
| $\tilde\Xi_{\mathrm{q}}\hat K_{\mathrm{K}}\tilde\Xi_{\mathrm{q}}$ | difference squared | the noise's correlation | the **Keldysh** component, the fluctuation |

**The structure is the content.** The first two components are the two orderings of one kernel, which is why the retarded and advanced responses are transposes of one another; the third is symmetric and quadratic in the difference, which is why **it is the only term that survives when the mean field is zero** — it is the fluctuation spectrum. **A single-branch action has no place for the third term**, because a single branch has no difference.

**The equations, read in the fluid's language.** Varying $\tilde\Xi_{\mathrm{q}}$ gives the mean field's transport equation with the influence functional's real part as a friction and its imaginary part as a source. Varying $\tilde\Xi_{\mathrm{cl}}$ gives the response equation. **The first is the fluid's equation of motion; the second is its linear response.** They are the two halves of one variation, and the corpus's linear-response articles use the second without naming the first.

**The fluctuation–dissipation theorem, as one sentence about the kernel.** The real and imaginary parts of $\hat K_{\mathrm{K}}$ are not independent: the symmetric part of the kernel is fixed by the antisymmetric part and the temperature. **That relation is the content of the Keldysh component**, and it is why a dissipative coefficient and a noise correlation are one number at a given temperature. A reader who wants the theorem should be told that it is the statement that $\hat K_{\mathrm{K}}$ comes from one kernel and not two.

## Where the Dissipation Went

**The Rayleigh function, and its place in this structure.** [Viscosity and the Rayleigh Dissipation Function](viscosity-and-the-rayleigh-dissipation-function.html) writes $\mathcal R=\tfrac12\gamma\dot\xi^{2}$, whose force $\partial\mathcal R/\partial\dot\xi$ enters the equation beside the conservative force. **In the doubled action $\mathcal R$ is the real part of the influence functional's kernel**, and the noise is its imaginary part: one kernel, two readings, and the reading is fixed by whether it multiplies $\tilde\Xi_{\mathrm{cl}}\tilde\Xi_{\mathrm{q}}$ or $\tilde\Xi_{\mathrm{q}}^{2}$.

**Why Helmholtz's theorem is not violated.** The theorem says there is no $\mathcal L(\xi,\dot\xi)$ whose variation gives the damped equation at a local multiplier. **It says nothing about a functional of two fields.** The doubled action's variation gives the damped equation only after the environment has been integrated out, and the equation so obtained is stochastic: **the deterministic damped equation is the mean of a Langevin equation, and it is not the variation of anything on one branch.** The theorem stands, and the CTP action is the object that lives beside it rather than against it.

**What the corpus's three sentences about the viscous term should now say.** *The viscous term has no action* is exactly right on one branch, and it is the reason the dissipative articles need a formalism of their own. **The corrected sentence is: the viscous term has no action on one history, and its action on two histories is the influence functional.** That is not a weakening of the claim; it is the claim plus its location.

**The price, in three parts.**

- **The field is doubled.** Every correlation function is a matrix of four components, and the physical one is an off-diagonal entry.
- **The object is a pair of histories, not a history.** A single path has no action; the pair does.
- **The noise is irreducible.** Setting the Keldysh component to zero while keeping the friction violates the fluctuation–dissipation theorem, so a "purely dissipative" CTP action is not a consistent truncation. **This is the formalism's honest statement that dissipation and fluctuation are one thing.**

## Two Doublings That Are Not the Same

**The corpus doubles in more than one place, and the doublings must not be conflated.** The algebra has two sectors; the CTP has two branches; the spinor has two chiralities. **Three doublings, three meanings**, and a table is the shortest way to keep them apart.

| doubling | what is doubled | the pairing that relates the copies | what the second copy means | the category error |
| --- | --- | --- | --- | --- |
| the sectors | the reality type: $\mathbb{B}_{\Phi}$ anti-Hermitian, $\mathbb{B}_{\Psi}$ Hermitian | the Hermitian form | the informational reading of the same element | reading a sector as a history |
| the closed time path | the history: forward and backward branches | the final-time identification and the influence functional | the other end of a correlation | reading a branch as a sector |
| the chirality | the spinor's two hands | the gamma structure | the other half of the representation | reading a chirality as a branch |

**Why the warning is needed.** The Schwinger–Keldysh article says that the branch doubling is *not* the algebra's doubling, and the sentence is easy to read past. **A reader who identifies them will expect the Keldysh component to be a sector projection**, which it is not: the Keldysh component is a correlation and the sector split is a reality type. **The test is one line**: a sector split is fixed by the field's Hermiticity and does not depend on the state; a branch split is fixed by the contour and the state's initial condition.

**The one honest overlap.** The algebra's doubling does supply a convenient place to put the doubled field: the pair $(\tilde\Xi_+,\tilde\Xi_-)$ can be carried in the two sectors' directions, and the corpus's path-integral article uses exactly that. **The overlap is a convenience of storage and not an identity of meaning**, which is the distinction the table's last column records.

## What It Does Not Give

**It does not give an action on one history.** That is impossible by Helmholtz, and this article does not claim otherwise.

**It does not give the transport coefficients in closed form.** It gives their origin as moments of the influence functional; the values require a model of the environment and a computation.

**It does not remove the noise.** A truncated CTP action with friction and no noise is inconsistent, and the corpus's dissipative articles must either carry both or state which limit they take.

**It does not settle the initial condition.** The contour's open end carries the density matrix, and a full treatment needs its specification. **The corpus's equilibrium articles take it thermal**, which is what makes the fluctuation–dissipation theorem applicable; a non-equilibrium initial state needs its own statement and this article does not supply one.

## Summary

A dissipative equation has no action on one history and has one on two. The closed-time-path action is the difference of the branches' actions plus an influence functional, its generating functional equals one at coincident sources, and its variation gives the field equation on each branch. **For a closed system nothing dissipative appears**; the dissipation is what an environment leaves behind, and it is nonlocal in time.

The Keldysh rotation splits the quadratic action into a retarded, an advanced and a noise component. The first two are one kernel's two orderings, the third is the fluctuation spectrum, and the fluctuation–dissipation theorem is the statement that the third is fixed by the first two and the temperature. **A single-branch action has no place for the third term**, which is exactly why the theorem of no-action-on-one-history holds.

The Rayleigh function is the real part of the influence functional's kernel and the noise is its imaginary part. **The corpus's sentence about the viscous term is therefore exact and incomplete**: exact on one branch, and located on two. The price is a doubled field, a pair of histories and an irreducible noise.

The corpus's own doubling — the two sectors — is a doubling of reality type and not of history, and the two must not be identified. The overlap is a place to store the pair, not a meaning.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde\Xi_+,\tilde\Xi_-$ | The field on the forward and backward branches of the contour |
| $\tilde\Xi_+(t_f)=\tilde\Xi_-(t_f)$ | The identification at the turning point; the initial end is left open |
| $Z[J_+,J_-]$ | The closed-time-path generating functional; $Z[J,J]=1$ |
| $J_{\mathrm{cl}}=\tfrac12(J_++J_-)$, $J_{\mathrm{q}}=J_+-J_-$ | The mean and difference sources; $J_{\mathrm{q}}=0$ is unitarity |
| $\mathcal F[\tilde\Xi_+,\tilde\Xi_-]$ | The influence functional, nonlocal in time, the trace of the environment |
| $\tilde\Xi_{\mathrm{cl}}=\tfrac12(\tilde\Xi_++\tilde\Xi_-)$ | The mean field, the physical component |
| $\tilde\Xi_{\mathrm{q}}=\tilde\Xi_+-\tilde\Xi_-$ | The difference, the quantum component |
| $\hat K_{\mathrm{ret}},\hat K_{\mathrm{adv}}$ | The retarded and advanced kernels, one kernel's two orderings |
| $\hat K_{\mathrm{K}}$ | The Keldysh kernel, the noise; its real and imaginary parts are related by the fluctuation–dissipation theorem |
| $\mathcal R=\tfrac12\gamma\dot\xi^{2}$ | Rayleigh's function, the real part of the influence functional's kernel |
| $\exp(iS)$ | The weight, with $S$ in units of the action quantum |

## Further Reading

- Julian Schwinger, "Brownian motion of a quantum oscillator," *Journal of Mathematical Physics* 2 (1961), 407–432, the contour's origin.
- Leonid V. Keldysh, "Diagram technique for nonequilibrium processes," *Soviet Physics JETP* 20 (1965), 1018–1026, the rotation and the three-component structure.
- Richard P. Feynman and Frank L. Vernon, "The theory of a general quantum system interacting with a linear dissipative system," *Annals of Physics* 24 (1963), 118–173, the influence functional and its real and imaginary parts.
- Alex Kamenev, *Field Theory of Non-Equilibrium Systems* (Cambridge University Press, 2011), for the modern formulation, the Keldysh rotation and the fluctuation–dissipation theorem.
- Esteban A. Calzetta and Bei-Lok B. Hu, *Nonequilibrium Quantum Field Theory* (Cambridge University Press, 2008), for the Kadanoff–Baym equations and the classical limit.
- [The Schwinger–Keldysh Formalism in Biquaternionic Form](the-schwinger-keldysh-formalism-in-biquaternionic-form.html), the corpus's own treatment of the contour and the rotation.
- [Viscosity and the Rayleigh Dissipation Function](viscosity-and-the-rayleigh-dissipation-function.html), the dissipation function this article places in the influence functional.
- [The Inverse Problem of the Calculus of Variations: Helmholtz's Conditions](the-inverse-problem-of-the-calculus-of-variations-helmholtz-conditions.html), the theorem that forbids a single-branch action and which the doubling does not violate.
- [Causal Dissipative Fluid Physics in Biquaternionic Form](causal-dissipative-fluid-physics-in-biquaternionic-form.html), the macroscopic face whose coefficients this article's functional generates.
- [The Free-Energy Functional at Finite Temperature](the-free-energy-functional-at-finite-temperature.html), the imaginary-time face of the same $Z$.
