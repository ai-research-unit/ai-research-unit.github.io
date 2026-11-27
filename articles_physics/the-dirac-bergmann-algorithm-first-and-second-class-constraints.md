# __The Dirac–Bergmann Algorithm: First- and Second-Class Constraints__

## Introduction

**The claim.** When a Legendre transform is singular, the Hamiltonian formulation does not fail: it gains constraints, and the constraints carry the whole of the gauge structure. The algorithm that extracts them — primary, then secondary by a consistency condition, then the split into first and second class, then the bracket that replaces the Poisson bracket — is Dirac's and Bergmann's, and in this corpus it does two jobs. It supplies the numbers that the fluid block's closure test has been quoting in components, and it distinguishes the polar frame from the gauge transformation, which is the distinction the criterion article could name but not derive.

**What is established.** Four things. First, a singular Hessian produces primary constraints, and the consistency condition produces the secondary ones, with a definite stopping rule. Second, first-class constraints generate a redundancy and second-class ones do not, and the difference is one bracket. Third, the second-class set replaces the Poisson bracket by the Dirac bracket, which is the operation that makes the algebra of gauge-invariant quantities well defined. Fourth, the count of degrees of freedom is a formula, and the corpus's three quoted counts — two polarizations at the Maxwell rung, three at the Proca rung, thirty of sixty at the primordial one — are its values.

**What is not new.** Every step is in Dirac's 1950 lectures and in Bergmann's papers of the same years, and the modern formulation is Henneaux and Teitelboim. **What the corpus adds is the reading of its own numbers**: the fluid block's *corank*, its *family of fluids*, and its *state slot* are the constraint count, the gauge orbit and the secondary constraint, and the block has been using those words without the machinery behind them.

**Why it comes after the Hamiltonian.** [The Hamiltonian article](hamiltonian-field-theory-in-biquaternionic-form.html) establishes that the scalar field's Legendre transform is regular, and it names the two fields for which it is not: the Dirac field, with a second-class constraint, and the Maxwell field, with two first-class ones. **This article is what happens when that regularity is absent**, and it is why the Hamiltonian article's remark about the scalar case is a remark about a case and not about the formalism.

## The Singular Hessian

**The Hessian, and what its rank decides.** Write the density in first-order form, with $\dot\xi_a=\partial\xi_a/\partial r'_t$, and define

$$
W_{ab}:=\frac{\partial^2\mathcal L}{\partial\dot\xi_a\,\partial\dot\xi_b}.
$$

The Legendre transform $\pi_a=\partial\mathcal L/\partial\dot\xi_a$ is invertible exactly when $W$ is invertible. **When $W$ is singular the velocities are not determined by the momenta**, and the directions in its kernel are the theory's primary constraints.

**Why a kernel direction is a constraint and not a variable.** Let $v_a$ lie in the kernel, $W_{ab}v_b=0$. Then $\pi_av_a=\partial\mathcal L/\partial\dot\xi_a\,v_a$ is independent of $\dot\xi$ along $v$, so the combination $\pi_av_a$ is a function of the fields and not of the velocities. **That function is a constraint**: the phase-space point must lie on its zero set, because no velocity would otherwise produce that momentum.

**The two cases the corpus meets.**

| field | Hessian | primary constraints |
| --- | --- | --- |
| central scalar, Klein–Gordon | $W=1$, invertible | none; the transform is regular |
| Dirac spinor | first order in the time derivative, so $W=0$ in the spinor indices | $\pi-i\tilde\Xi^{\dagger}\approx0$, one per spinor component |
| Maxwell connection | $W^{\imath\jmath}$ has the temporal row and column zero, because $F_{\imath\jmath}$ carries no $\dot A_t$ | $\pi^0\approx0$ |

**The Dirac field is the extreme case and it is worth naming.** Its density is first order in the time derivative, so the Hessian vanishes identically and the momentum is not an independent variable at all: it is fixed by the field. **A first-order density has no velocity to invert**, which is why its constraint is not a restriction on a pair but the statement that the pair has half the components one expected.

**The Maxwell case is the geometric one.** $\pi^0=0$ because the temporal component of the connection has no conjugate momentum: the curvature contains $\partial_tA_{\imath}$ only through the spatial components. **The constraint is the statement that $A_t$ is not a dynamical variable**, and every consequence of gauge theory follows from taking it seriously.

## The Consistency Condition

**A constraint must hold at every time, and that is a new equation.** If $\phi_a\approx0$ holds on the constraint surface, then its time derivative must vanish there too:

$$
\dot\phi_a=\{\phi_a,H_T\}+\frac{\partial\phi_a}{\partial r'_t}\approx0 ,
$$

with $H_T$ the total Hamiltonian — the canonical Hamiltonian plus a combination of the primary constraints with arbitrary multipliers. **This is the consistency condition**, and it has three outcomes:

1. it is satisfied identically, and $\phi_a$ is a constraint and nothing more;
2. it determines one of the arbitrary multipliers, and the constraint is *second class* in embryo;
3. it produces a new function of the fields, which must vanish, and that function is a **secondary constraint**.

**Iterate until the list closes.** Each new constraint is fed back into the consistency condition, and the process terminates for the theories the corpus uses. **The termination is the statement that the constraint surface is stable**, and a theory in which it does not terminate has an inconsistency rather than a constraint.

**The secondary constraint is where the physics is.** For the Maxwell field, the consistency of $\pi^0\approx0$ gives

$$
\{\pi^0,H_T\}=\mathrm{div}\,\vec\pi\approx0 ,
$$

which is Gauss's law. **It is secondary because it is not a restriction on the initial data of the transform but a consequence of the dynamics**, and it is the constraint that says the charge density is the divergence of the field momentum. For the Proca field the same step gives

$$
\mathrm{div}\,\vec\pi+m^{2}A_t\approx0 ,
$$

the massive version, in which the constraint *determines* $A^0$ instead of restricting it. **The mass turns the constraint from a restriction into a solution**, and that is the linear shadow of the statement that a massive vector has one more state than a massless one.

**A secondary constraint is not a weaker statement than a primary one.** Both hold on the constraint surface and both remove components. The difference is provenance — one from the Hessian, one from the dynamics — and the difference matters for the count only through the class, which is next.

## First Class and Second Class

**One bracket decides.** A constraint $\phi_a$ is **first class** when its bracket with every constraint vanishes on the constraint surface,

$$
\{\phi_a,\phi_b\}\approx0\quad\text{for all }b ,
$$

and **second class** otherwise. **The definition is a statement about the constraint set and not about the constraint alone**: a function that is first class against one set may be second class against a larger one, which is why the split is performed after the list has closed.

**What first class means.** A first-class constraint generates a transformation of the phase-space variables that leaves the constraint surface and the Hamiltonian invariant: it is a **redundancy of the description**, not a restriction on the physics. The Maxwell pair $\pi^0$ and $\partial_\imath\pi^{\imath}$ is first class, and together they generate the gauge transformation of $A_\imath$. **First class is gauge symmetry, stated in one bracket.**

**What second class means.** A second-class constraint does not generate a redundancy; it removes a pair of phase-space directions and leaves a bracket that must be modified. The Proca pair is second class, and so is the Dirac constraint. **Second class is a genuine restriction**, and the restriction is that the canonical pair is not canonical.

**Why the split is stable under the dynamics.** The bracket of two first-class constraints is first class by the Jacobi identity, so the first-class set is closed; the second-class set is not closed in the same sense, which is exactly why it needs its own bracket. **The asymmetry is not a defect of the classification; it is the classification.**

**The corpus's own pair, in its own letters.** The criterion article separates two objects that both look like transformations: $U_{\mathrm{frm}}$, the polar frame of $\Xi=U_{\mathrm{frm}}PU_{\mathrm{frm}}^{\dagger}$, which is a decomposition with twelve physical parameters and is *absent* from the covariant derivative; and $U_{\mathrm{gau}}(x)$, the local gauge transformation against which $D_\imath$ covariantises. **The Dirac–Bergmann split is what makes the sentence exact**: $U_{\mathrm{gau}}$ is generated by first-class constraints and is a redundancy; $U_{\mathrm{frm}}$ is a change of variables on the physical configuration and is not. A reader who conflates them will count the frame's twelve parameters as gauge and lose them from the fluid.

## The Dirac Bracket

**The problem the second-class set creates.** If $\phi_a$ are second class, the matrix $C_{ab}:=\{\phi_a,\phi_b\}$ is invertible on the constraint surface, and the ordinary Poisson bracket is inconsistent with the constraints: $\{\phi_a,\text{anything}\}$ need not vanish, so a bracket computed on the constraint surface differs from the bracket computed off it and then restricted. **The Dirac bracket is the repair**:

$$
\{A,B\}_{\mathrm D}:=\{A,B\}-\sum_{a,b}\{A,\phi_a\}\,(C^{-1})_{ab}\,\{\phi_b,B\},
\qquad \sum_b C_{ab}(C^{-1})_{bc}=\delta_{ac} ,
$$

with the sum over the second-class set. **It is the Poisson bracket projected onto the constraint surface**, and it is the unique bracket that (i) agrees with the Poisson bracket for first-class quantities, (ii) annihilates the second-class constraints, and (iii) satisfies the Jacobi identity.

**What it buys.** The Dirac bracket is the classical bracket of the physical variables. Quantising the Dirac bracket gives the commutators of the constrained theory directly, with no need to fix a gauge; **this is the route by which the Dirac field's anticommutators and the Maxwell field's physical commutators are obtained** in the corpus's quantisation articles.

**What it costs.** The bracket is nonlocal in the fields whenever $C^{-1}$ is, and for the Dirac field $C^{-1}$ is the inverse of the equal-time anticommutator, which is a delta function — so the bracket stays local but changes sign structure. **For a gauge theory whose second-class set arises from gauge fixing, $C^{-1}$ is the Green's function of the gauge condition**, and the bracket becomes nonlocal in exactly the way a gauge-fixed propagator does.

**The alternative, and why the corpus does not use it as the primary route.** One can fix the gauge first — impose $2\times(\text{first class})$ conditions and treat the reduced phase space — which is Bergmann's *coordinate conditions*. **The two routes are equivalent and not identical**: gauge fixing breaks the redundancy explicitly and makes the bracket nonlocal; the Dirac bracket keeps the redundancy and makes the algebra of invariants well defined. The corpus needs the second because its fluid reading is a reading of invariants: a divergence, a vorticity and a density are gauge-invariant objects, and the bracket they obey is the Dirac bracket.

## The Count

**One formula, four numbers.** On the constraint surface, with $f$ first-class and $s$ second-class constraints per point, the number of physical degrees of freedom per point is

$$
\boxed{\;N_{\mathrm{dof}}=\tfrac12\Bigl(N_{\mathrm{phase}}-2f-s\Bigr)\;}
$$

where $N_{\mathrm{phase}}$ is the number of phase-space components per point. **Each first-class constraint removes two components** — the constraint and the gauge direction it generates — and **each second-class removes one pair**, which is two components and one degree of freedom.

**The corpus's rungs, in the formula's terms.**

| rung | $N_{\mathrm{phase}}$ | primary | secondary | first class $f$ | second class $s$ | $N_{\mathrm{dof}}$ |
| --- | --- | --- | --- | --- | --- | --- |
| central scalar | $2$ (real $\xi$, $\pi$) | $0$ | $0$ | $0$ | $0$ | $1$ |
| Maxwell | $8$ ($A_\imath$, $\vec\pi$) | $1$: $\pi^0$ | $1$: $\mathrm{div}\,\vec\pi$ | $2$ | $0$ | $2$ |
| Proca | $8$ | $1$: $\pi^0$ | $1$: $\mathrm{div}\,\vec\pi+m^2A_t$ | $0$ | $2$ | $3$ |
| Dirac | $16$ (four complex $\xi$, four $\pi$) | $8$ real: $\pi-i\tilde\Xi^{\dagger}$ | $0$ | $0$ | $8$ | $4$ |
| primordial | $60$ | $15$: the Gauss laws' primary halves | $15$: the Gauss laws | $15$ | $0$ | $15$ |

**Three of these numbers are the corpus's own sentences.** The Maxwell rung's two polarizations, the Proca rung's three states, and the primordial rung's closure on thirty of sixty after fifteen first-class constraints remove thirty. **The fourth row corrects a reading the criterion article had to relabel**: "closes on fifteen" is the number of *degrees of freedom* after the count, and the thirty is the number of remaining phase-space components. Both are the formula's values at different stages.

**The Proca row is the one worth pausing on.** Its two constraints are second class, so it has one more degree of freedom than Maxwell's two: the longitudinal mode. **The mass converts a first-class pair into a second-class pair and the count rises by one**, which is the linear statement of the mechanism by which a would-be Goldstone mode becomes the third polarization of a massive vector.

**The Dirac row is the one the fluid block calls degenerate.** The corpus's corank four at the spinor rung is the second-class count read in complex components; the algorithm says the same thing in real components and says *why*: the momentum is not independent, so half the phase space is a constraint surface.

## What the Fluid Calls These

**The closure test is the count.** [The criterion article](criterion-for-a-fluid-equation-one-polar-coordinates-euler-lagrange-equation.html) distinguishes count closure — equations enough for coordinates — from rank closure — rates determined. **Rank closure is the nondegeneracy of the Hessian, and its failure is a constraint.** So the two closures are the regular and the singular case of one transform, and the Dirac–Bergmann algorithm is the singular case's bookkeeping.

**The "family of fluids" is the gauge orbit.** The criterion article says an under-determined set is a family of fluids and not a fluid. **The family is the orbit of the redundancy**, and its dimension is $2f$ per point in the formula above. A reader who wants a single fluid must fix the gauge, which is choosing one representative per orbit; a reader who wants the physics must take the invariants, which is the Dirac bracket's algebra.

**The state slot is the secondary constraint, solved.** The fluid's sixth slot is an algebraic relation between pressure, density and temperature. **At the Maxwell rung the secondary constraint is an algebraic relation between the charge density and the field momentum**, which is a constitutive statement of exactly that kind: it fixes one datum in terms of the others rather than transporting it. **A constraint is a state equation's field-theoretic form**, and that is why the corpus's *state* slot is the one slot that is never a transport law.

**The frame-gauge split is the class split.** Stated above and worth repeating as a summary: **first-class constraints are the redundancy the frame article calls $U_{\mathrm{gau}}$; the physical frame $U_{\mathrm{frm}}$ is what remains after the count.** The corpus's fluid has twelve frame parameters at the primordial rung because thirty of sixty components survive fifteen first-class removals, and twelve is the frame's share of the thirty.

## What the Algorithm Does Not Give

**It does not give the transport equations.** The algorithm produces the arena — which variables are independent, which brackets they obey — and says nothing about the constitutive relations that close the fluid's system. **A constraint is not a conservation law**, and the count is not a solution.

**It does not fix the gauge.** Bergmann's coordinate conditions are a choice, and different choices give different nonlocal brackets. **The corpus's invariants are the objects that do not depend on the choice**, and that is why it can afford to leave the choice open.

**It does not settle the global questions.** The split into first and second class is local; on a nontrivial bundle the constraint surface can have several sheets, and the gauge orbit can be of non-constant dimension — Gribov's problem. **The corpus's patched objects, such as the vorticity potential at the primordial rung, meet this limit**, and the algorithm is silent about it.

**It does not quantise.** The Dirac bracket is the classical input to a quantisation, and the quantisation of a constrained system has its own ordering and anomaly questions. **The corpus's promotion article takes the Dirac bracket over and does not re-derive it**, which is the correct division: the bracket is classical and the promotion is the postulate.

## Summary

A singular Hessian produces primary constraints; the consistency condition produces secondary ones and terminates; the bracket with the constraint set splits them into first class, which generates a redundancy, and second class, which restricts. **The first-class count is gauge symmetry and the second-class count is a genuine reduction**, and the Dirac bracket is the Poisson bracket projected onto the second-class surface, the classical algebra of the physical variables.

The count is one formula, $N_{\mathrm{dof}}=\tfrac12(N_{\mathrm{phase}}-2f-s)$, and the corpus's numbers are its values: two polarizations at Maxwell, three at Proca, four at Dirac, fifteen at the primordial rung after fifteen first-class constraints remove thirty of sixty components. **The Proca row is the mass converting a first-class pair into a second-class pair**, the Dirac row is the first-order density that leaves the momentum no independent life, and the primordial row is Gauss's law fifteen times over.

In the fluid's language the closure test is the count, the *family of fluids* is the gauge orbit, the *state* slot is a secondary constraint solved for one datum, and the frame–gauge split is the class split. **The algorithm supplies the words the fluid block had been using and the numbers it had been quoting.**

It gives no transport equation, no gauge choice, no global statement and no quantisation. It gives the arena, and the arena is what the fluid's rank test was measuring.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\xi_a$, $\pi_a$ | The configuration variables and their conjugate momenta, one pair per component |
| $W_{ab}=\partial^2\mathcal L/\partial\dot\xi_a\partial\dot\xi_b$ | The Hessian of the density in the velocities; its singularity is the source of primary constraints |
| $\phi_a\approx0$ | A constraint; $\approx$ is weak equality, on the constraint surface |
| $H_T$ | The total Hamiltonian, the canonical one plus primary constraints with multipliers |
| $\{\cdot,\cdot\}$ | The Poisson bracket, and $\{\cdot,\cdot\}_{\mathrm D}$ the Dirac bracket |
| $C_{ab}=\{\phi_a,\phi_b\}$ | The second-class matrix, invertible on the constraint surface |
| $f$, $s$ | The numbers of first-class and second-class constraints per point |
| $N_{\mathrm{phase}}$ | Phase-space components per point; $N_{\mathrm{dof}}=\tfrac12(N_{\mathrm{phase}}-2f-s)$ |
| $\pi^0\approx0$ | The Maxwell primary constraint; the secondary is $\mathrm{div}\,\vec\pi\approx0$ |
| $\mathrm{div}\,\vec\pi+m^2A_t\approx0$ | The Proca secondary constraint, which determines $A_t$ |
| $\pi-i\tilde\Xi^{\dagger}\approx0$ | The Dirac field's second-class constraint, one per spinor component |
| $U_{\mathrm{frm}}$, $U_{\mathrm{gau}}$ | The polar frame, physical and twelve-parameter; the gauge transformation, the redundancy |

## Further Reading

- Paul A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), the original algorithm, the class split and the bracket.
- Peter G. Bergmann, "Non-linear field theories," *Physical Review* 75 (1949), 680–685, and *Helvetica Physica Acta* Supplement 4 (1956), for the consistency condition and the coordinate conditions.
- Marc Henneaux and Claudio Teitelboim, *Quantization of Gauge Systems* (Princeton University Press, 1992), for the modern formulation, the count and the global questions.
- Kurt Sundermeyer, *Constrained Dynamics* (Springer, 1982), for the worked examples and the multiplier structure of the total Hamiltonian.
- Steven Weinberg, *The Quantum Theory of Fields*, vol. I (Cambridge University Press, 1995), §5.9, for the Proca field, its constraint structure and the third polarization that the mass restores.
- [Hamiltonian Field Theory in Biquaternionic Form](hamiltonian-field-theory-in-biquaternionic-form.html), for the regular transform and the two constrained fields this article takes up.
- [Criterion for a Fluid Equation](criterion-for-a-fluid-equation-one-polar-coordinates-euler-lagrange-equation.html), for the closure test, the corank and the family of fluids that this article identifies with the count and the orbit.
- [The Inverse Problem of the Calculus of Variations: Helmholtz's Conditions](the-inverse-problem-of-the-calculus-of-variations-helmholtz-conditions.html), for the question of an action, which is prior to the question of its constraints.
- [Canonical Quantization of the Biquaternion Klein–Gordon Field](canonical-quantization-of-the-biquaternion-klein-gordon-field.html), for the quantisation that imports the Dirac bracket.
