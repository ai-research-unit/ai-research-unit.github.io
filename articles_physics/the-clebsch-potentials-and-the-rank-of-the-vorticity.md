# __The Clebsch Potentials and the Rank of the Vorticity__

## Introduction

**A rotational flow cannot be written with one potential, and the reason is a classification and not an obstruction.** A gradient is one function; a rotational velocity in three dimensions needs three; a vorticity that is not simple needs five. The gradient is the bottom of a family, the family is indexed by the rank of the vorticity two-form, and the question this article answers is what each rank costs.

**A fluid can also carry an orientation, and that is a second and independent generalisation.** A medium whose material points carry a triad as well as a position — a Cosserat medium, also called a micropolar fluid, and in the relativistic literature a Weyssenhoff–Raabe spin fluid — has two vorticities and an antisymmetric stress. The ordinary fluid is the case in which the orientation is not independent, and a potential flow is the further case in which there is no orientation at all.

**The article separates two questions that the word "rotational" runs together.** One is whether the velocity carries a potential representation, and that is a question about the *rank* of the vorticity two-form. The other is whether the medium carries an orientation, and that is a question about the *degrees of freedom* at a point. The two are independent: a rotational flow is rank two and carries no orientation, and a medium can carry an orientation while its velocity is a gradient.

**Both generalisations are classical, and both are older than the field theory that needs them.** Clebsch wrote the potential representation of a rotational velocity in 1857, the Cosserats wrote the medium with an independent triad in 1909, and Eringen gave the micropolar fluid its modern form. The field reading of the next blocks is where the two meet: a bispinor has an orientation among its data, and its velocity is not a gradient, so its fluid is the case that both generalisations describe at once.

## What Actually Fails

**What fails is the claim that a rotational flow is a gradient flow with extra bookkeeping.** A velocity field is three functions; a potential is one; the two excess functions are the rotational part, and they are not disposable. The Helmholtz decomposition of [The Vorticity Form and the Irrotational Condition](the-vorticity-form-and-the-irrotational-condition.html) states the excess, and the Clebsch representation states what it costs to keep it.

**What also fails is that a fluid has no orientation.** Euler's equation describes a medium whose only kinematic datum at a point is the velocity. A medium whose points also carry a triad has a second vorticity, an antisymmetric stress and a couple stress, and no velocity field can represent it. The two failures are independent, and §*The Spinning Fluid* is the second.

**Neither failure is a defect of the classical theory.** Both are statements about how much structure a given medium carries: three functions for a rotational velocity in three dimensions, five in four, and a triad on top when the medium has one. The potential flow is the case with the least structure, and the error to avoid is to read it as the general case.

## The Clebsch Representation

**Every velocity one-form that carries a vorticity can still be written with potentials, and the representation is classical.** In the form used by Clebsch and by Lin, a velocity one-form is

$$
v_{\Phi,\mu}=\frac{\partial\phi_{\mathrm{clb}}}{\partial R_\mu}
+\alpha_{\mathrm{clb}}\frac{\partial\beta_{\mathrm{clb}}}{\partial R_\mu},
$$

with three functions in place of the one function of a gradient. The three names are the Clebsch scalar and the Clebsch pair, and the label $\mathrm{clb}$ distinguishes them from the scalar potential of the electrostatic and Higgs sections, which writes $\phi$.

**The vorticity of a Clebsch field is the wedge of the pair, and this is the whole content of the representation.** Taking the exterior derivative,

$$
\omega_{\mu\nu}=\frac{\partial v_{\Phi,\nu}}{\partial R_\mu}-\frac{\partial v_{\Phi,\mu}}{\partial R_\nu}
=\frac{\partial\alpha_{\mathrm{clb}}}{\partial R_\mu}\frac{\partial\beta_{\mathrm{clb}}}{\partial R_\nu}
-\frac{\partial\alpha_{\mathrm{clb}}}{\partial R_\nu}\frac{\partial\beta_{\mathrm{clb}}}{\partial R_\mu},
$$

so $\omega=\mathrm{d}\alpha_{\mathrm{clb}}\wedge\mathrm{d}\beta_{\mathrm{clb}}$ and the scalar $\phi_{\mathrm{clb}}$ drops out. **The Clebsch scalar carries no vorticity and the pair carries all of it.** A gradient is the case in which the pair is constant, and irrotationality is therefore not the absence of the representation but a degenerate value of its two potentials.

**The pair is not a computational trick, it is the general solution of the closure question.** Asking for $v_{\Phi,\mu}=\partial_\mu S$ is asking that a one-form be exact, which is one function's worth of data. Asking for the Clebsch form is asking nothing: it is available wherever the flow is defined, and it costs two functions at each event. The count is the point of the next section.

## The Rank of the Vorticity

**The vorticity is a two-form, and two-forms are classified by rank.** In four dimensions the rank is $0$, $2$ or $4$. Rank zero is the closed one-form; rank two is a two-form that is the wedge of two one-forms; rank four is neither. The classical name for the rank-two case is *simple*, and the test is one scalar.

**The test is the product of the electric and magnetic parts.** Split $\omega$ into $\omega_{0i}$, which is electric, and $\omega_{ij}$, which is magnetic, in the pattern of the field strength of the Maxwell block:

$$
\vec E_{\mathrm{vrt}}=(\omega_{01},\omega_{02},\omega_{03}),
\qquad
\vec B_{\mathrm{vrt}}=(\omega_{23},\omega_{31},\omega_{12}).
$$

Then the four-form $\omega\wedge\omega$ is proportional to one number, and the number is their dot product. In four dimensions the identity is exact,

$$
\omega\wedge\omega=(\vec E_{\mathrm{vrt}}\cdot\vec B_{\mathrm{vrt}})\,\mathrm{d}V,
\qquad
\det\omega=(\vec E_{\mathrm{vrt}}\cdot\vec B_{\mathrm{vrt}})^{2},
$$

both checked symbolically on a general antisymmetric array. **So simplicity is $\vec E_{\mathrm{vrt}}\cdot\vec B_{\mathrm{vrt}}=0$, and the rank is four exactly when that product is not zero.**

**The hierarchy is a table, and the last column is the number of functions the velocity costs.**

| rank of $\omega$ | condition | potentials | what it costs |
| --- | --- | --- | --- |
| $0$ | $\omega=0$ | $\phi_{\mathrm{clb}}$ alone | one function |
| $2$ | $\vec E_{\mathrm{vrt}}\cdot\vec B_{\mathrm{vrt}}=0$ | $\phi_{\mathrm{clb}}$, $\alpha_{\mathrm{clb}}$, $\beta_{\mathrm{clb}}$ | three functions |
| $4$ | $\vec E_{\mathrm{vrt}}\cdot\vec B_{\mathrm{vrt}}\ne0$ | two pairs | five functions |

**A potential flow is the first row and nothing else is.** Its velocity is $\partial_\mu\Phi$, a closed one-form, so it is rank zero exactly and its vorticity vanishes identically — the statement [The Vorticity Form and the Irrotational Condition](the-vorticity-form-and-the-irrotational-condition.html) proves. A rotational flow is the second row, and a flow whose vorticity is not simple is the third.

**In three spatial dimensions the third row does not occur, and this is why a Galilean fluid cannot show the effect.** A two-form on a three-dimensional space has three independent components and its four-form vanishes identically, so every Galilean vorticity is simple: $\vec\omega_{\mathrm{vrt}}$ is always the curl of something and a Clebsch pair always exists. A Galilean fluid therefore cannot exhibit the rank-four case, and the whole hierarchy collapses to its first two rows.

**The rank is one scalar of the flow, it is decidable on any solution, and for a vorticity it is decided in advance.** Split the velocity's derivative into its vorticity and its acceleration, $\omega_{\mu\nu}=\omega_{\mathrm{vrt},\mu\nu}+v_{\Phi,\mu}a_\nu-v_{\Phi,\nu}a_\mu$ with $a_\nu=v_{\Phi}^{\ \mu}\partial_\mu v_{\Phi,\nu}$. The vorticity proper annihilates the velocity, $v_{\Phi}^{\ \mu}\omega_{\mathrm{vrt},\mu\nu}=0$, so it is a two-form on the three dimensions of the rest space, and every two-form on three dimensions is simple. So $\omega_{\mathrm{vrt}}\wedge\omega_{\mathrm{vrt}}=0$ **identically, for every flow in four dimensions as much as in three**, and the rank of a vorticity is always two.

**The rank-four row therefore belongs to the raw derivative and to the acceleration, not to the vorticity.** Since the projected part is simple, the four-form of the whole derivative is proportional to $v_{\Phi}\wedge a\wedge\omega_{\mathrm{vrt}}$, and it vanishes exactly when the acceleration has no component along the vorticity axis: for an irrotational flow, for a geodesic one, and for any flow whose acceleration is orthogonal to its vorticity. A relativistic flow that accelerates about an axis it also rotates about reaches the third row and costs two pairs of potentials; a flow that does either alone does not. The checked example is the unit field with rapidity $r_xr_z$ and direction angles $r_y+r'_t$ and $r_zr_x$, where the rest-frame product $\vec E_{\mathrm{vrt}}\cdot\vec B_{\mathrm{vrt}}$ of the projected vorticity was $10^{-19}$ and the same product for the raw derivative was $-0.106$.

## The Spinning Fluid

**A medium that carries an orientation at each material point is a Cosserat medium.** Its kinematics are a position field and, independently, an orientation field: at each point a triad $\vec e_{\mathrm{mic},i}$ that rotates as the point moves. The modern continuum name is a micropolar fluid, the nineteenth-century name is the Cosserat brothers' elasticum, and the relativistic name is the Weyssenhoff–Raabe spin fluid. The three name the same kinematics.

**It has two vorticities and the classical fluid has one.** The first is the curl of the velocity, the same object as before. The second is the curl of the orientation field, the *wryness*, the continuum-mechanics name for the density of disclinations:

$$
\kappa_{\mu\nu}=\frac{\partial\chi_{\mathrm{mic},\nu}}{\partial R_\mu}-\frac{\partial\chi_{\mathrm{mic},\mu}}{\partial R_\nu},
$$

with $\chi_{\mathrm{mic},\mu}$ the infinitesimal rotation vector of the triad. **A medium whose triad is constant in space and time is a classical fluid; a medium whose triad varies has a second vorticity that the velocity knows nothing about.**

**Its stress is not symmetric, and the antisymmetry is a torque and not a force.** For a Cosserat medium the force balance is the usual one and the moment balance is separate. Writing $\sigma_{ij}$ for the stress, $\mu_{\mathrm{cpl},ij}$ for the couple stress, and

$$
\tau_i=\varepsilon_{ijk}\sigma_{jk}
$$

for the torque density that the antisymmetric part of the stress exerts, the moment balance is

$$
\partial_j\mu_{\mathrm{cpl},ij}=-\tau_i .
$$

**With no couple stress the stress is symmetric and the fluid is classical.** With a couple stress the antisymmetric part of the stress is fixed by the divergence of the couple stress, and it is a density of internal angular momentum rather than a force. The classical instance is a suspension of oriented particles or a liquid crystal, and the relativistic instance is the spin fluid, where the Frenkel condition plays the part of the constraint.

**The count of a Cosserat medium is seven data at a point, and eight with the energy.** A mass density, a velocity and an orientation triad give $1+3+3=7$; the eighth is the internal energy per unit mass. So the medium's kinematics and its thermodynamics close at eight, which is the same total an element of the algebra carries — a scale, an angle, a boost and a rotor — and the coincidence is the reason the field reading can be stated in this vocabulary.

**The wryness is what a triad contributes and a velocity cannot.** A medium can be at rest and carry a non-zero $\kappa_{\mu\nu}$: a solid with a density of disclinations does, and so does a liquid crystal with a twist. The macro-vorticity is blind to it. So the second vorticity is not a rewriting of the first, and a medium that carries it needs one more equation than a classical fluid does — the moment balance above.

## The Classical Fluid as the Constrained Case

**The classical fluid is not a different theory; it is the constrained Cosserat medium.** Cosserat and Cosserat, and later Koiter, observed that if the microrotation is not independent but tied to the velocity gradient — the triad carried and rotated by the deformation — then the couple stress is determined, the antisymmetric part of the stress vanishes, and the medium reduces to the classical one with a symmetric stress. The constraint is the classical limit, and the classical fluid is its image.

**The constraint has a name in the classical theory: the triad is tied to the velocity gradient.** If the microrotation is not independent but carried and rotated by the deformation, the couple stress is determined by the velocity and the medium reduces to the classical one. The two cases are therefore not two theories but one theory read at two values of a constraint.

**The reduction is in two independent steps, and the table separates them.**

| case | velocity | orientation | vorticity rank | stress |
| --- | --- | --- | --- | --- |
| potential flow | a gradient | none | $0$ | symmetric |
| classical rotational fluid | a Clebsch field | none | $2$ in three dimensions | symmetric |
| Cosserat medium | a Clebsch field or any field | an independent triad | $0$, $2$ or $4$ | antisymmetric |

**The middle row is the one the fluid layer of this block carries.** Euler and continuity, the vorticity form, viscosity, the equation of state and the reverse maps are all written for a medium with a velocity and no triad, so their vorticity is a property of the flow alone. A Cosserat medium differs from them in the second and fourth columns, and a potential flow differs from both in the first.

**This is the sense in which a potential flow is not the general case but its lowest member.** It has the smallest possible value of every entry in the table. A reader who meets it first and then meets a medium with an orientation has not met a contradiction, and the count of the two is consistent once the table is read.

## What the Criterion Becomes

**The first two clauses merge into one and it is a statement about rank.** "The velocity is a gradient" and "the flow is irrotational" are the same clause, the second being the component spelling of the first, and the general clause is that the vorticity has a rank the potentials can carry. At rank zero one potential suffices; at rank two one pair does, three functions in all; at rank four one pair no longer suffices and two are needed.

**The third clause becomes two clauses, and the second of them is the couple stress's.** "Every force is a gradient" is a statement about the longitudinal part of the stress. The departure of a medium with an orientation is in the transverse part: the stress has an antisymmetric piece, and the moment balance, not the force balance, is what fixes it. A criterion written for a symmetric stress cannot see this, and it is the clause that a potential flow satisfies vacuously because it has no triad to source an antisymmetric stress.

**The fourth clause is untouched, and it is the one that decides whether the fluid is a reading of a free or an interacting equation.** A potential that is a function of the density makes the wave equation nonlinear; a potential that is not makes it linear. The scalar fluid is linear and the Gross–Pitaevskii fluid is not, and the rank of the vorticity has nothing to do with which.

**So the criterion generalises in the direction of more structure, not less.** The scalar case is the member with one potential, no triad and a symmetric stress, and every clause of the general criterion reduces to the corresponding clause of the four-item form on that member.

## The Invariant

**The conserved quantity of the rank-zero case is the circulation, and its general counterpart is the helicity.** For an irrotational flow the circulation around a loop is the period of the potential and is fixed only by the boundary conditions. For a rotational flow the same integral is not an invariant at all, and what survives as an invariant of the motion is the helicity

$$
\mathcal H=\int\vec v\cdot\vec\omega_{\mathrm{vrt}}\,\mathrm{d}V ,
$$

conserved for a barotropic inviscid flow and not for a general one.

**For a medium with an orientation the invariant is built from the spin and the vorticity together.** The helicity of the spinning fluid is conserved when the spin current's divergence vanishes, and in the relativistic case the corresponding charge is the one the axial current carries. The spin-hydrodynamics literature states the identification, and **it is quoted here as the classical counterpart and not derived**, because the derivation needs the spin current's equation, which is [Spin Conservation and the Frenkel Condition](spin-conservation-and-the-frenkel-condition.html).

**The change from a topological invariant to a differential one is the right expectation and not a loss.** A rank-zero flow has a topological invariant because its velocity is one function with a period; a rank-two flow has a differential invariant because its velocity is three functions with none. The potential flow is special in having a topological charge, and that specialness is why its circulation is a conserved quantity of the flow and not of the medium.

## What Is Established and What Is Interpretation

**Established.** The Clebsch representation and its vorticity, $\omega=\mathrm{d}\alpha_{\mathrm{clb}}\wedge\mathrm{d}\beta_{\mathrm{clb}}$, which is an identity. The rank classification and its test, $\omega\wedge\omega=(\vec E_{\mathrm{vrt}}\cdot\vec B_{\mathrm{vrt}})\,\mathrm{d}V$ and $\det\omega=(\vec E_{\mathrm{vrt}}\cdot\vec B_{\mathrm{vrt}})^{2}$, checked symbolically on a general antisymmetric array. That every two-form in three dimensions is simple, so that a Galilean fluid has no rank-four case. That the moment balance of a medium with a couple stress is $\partial_j\mu_{\mathrm{cpl},ij}=-\tau_i$ with $\tau_i=\varepsilon_{ijk}\sigma_{jk}$, so that a vanishing couple stress forces a symmetric stress. That the count of a Cosserat medium is seven data plus the internal energy, one density, three velocity and three orientation functions. That a projected vorticity is always simple, $\omega_{\mathrm{vrt}}\wedge\omega_{\mathrm{vrt}}=0$, so the rank of a vorticity is two and the third row belongs to the raw derivative and to the acceleration.

**Not claimed.** That a given flow reaches the third row; the condition is the acceleration's alignment with the vorticity, the test is written down, and no solution of a field equation is examined here. That a potential flow is the only fluid of the layer satisfying the four-item criterion in its original form; the Gross–Pitaevskii fluid also does, being irrotational, and the criterion's fourth clause is what distinguishes them. That the helicity of the spinning fluid is the axial charge; the identification is quoted from the literature and is not derived here. That any particular Cosserat constitutive law is the right one for a given medium; the kinematics is fixed and the closure is open.

**Interpretation.** That a medium with an orientation is the general case of the fluid layer, in the sense that its kinematics are those of a Weyssenhoff–Raabe spin fluid and its stress has the structure of one. The identification is of kinematics and of stress, and a constitutive law would be a further statement.

## Summary

**The criterion's first clause is the rank-zero member of a family, and the family is indexed by the rank of the vorticity.** Rank zero is the closed one-form, one potential, the scalar fluid. Rank two is the simple two-form, three functions, the classical rotational flow. Rank four is the general two-form, two pairs and five functions, and no single pair of Clebsch potentials reaches it.

**Rotational and spinning are two facts and they are independent.** The first is a statement about the rank of the vorticity and the second about the degrees of freedom at a point. A classical rotational fluid is rank two with no orientation, and a medium with an orientation carries it whether its vorticity is simple or not.

**The general medium with an orientation is the Cosserat medium, and the ordinary fluid is its constrained case.** A triad at each point gives a second vorticity, an antisymmetric stress and a couple stress; the constraint that ties the triad to the velocity gradient removes all three and returns the classical fluid. A potential flow is the further case of no triad at all.

**The count of a Cosserat medium is seven data plus the energy, and that is the cleanest statement of how the layer's vocabulary falls short of it.** One density, three velocity and three orientation functions; the ordinary fluid keeps four of the seven because it has no triad.

**The invariant changes with the rank.** A rank-zero flow has a circulation that is the potential's period and can be a topological charge when the potential is an angle; a rank-two flow has a helicity; and a medium with an orientation has a spin contribution on top of the helicity, which this article quotes and does not compute.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\phi_{\mathrm{clb}},\alpha_{\mathrm{clb}},\beta_{\mathrm{clb}}$ | the Clebsch scalar and pair |
| $\omega_{\mu\nu}$ | the vorticity two-form |
| $\vec E_{\mathrm{vrt}},\vec B_{\mathrm{vrt}}$ | its electric and magnetic parts |
| $\kappa_{\mu\nu}$ | the wryness, the curl of the orientation field |
| $\chi_{\mathrm{mic},\mu}$ | the infinitesimal rotation vector of the triad |
| $\vec e_{\mathrm{mic},i}$ | the orientation triad |
| $\sigma_{ij}$ | the stress |
| $\mu_{\mathrm{cpl},ij}$ | the couple stress |
| $\tau_i$ | the torque density of the antisymmetric stress |
| $\mathcal H$ | the helicity |

## Further Reading

- A. Clebsch, *Über eine allgemeine Transformation der hydrodynamischen Gleichungen*, J. Reine Angew. Math. **54** (1857), 293–312 — the potential representation of a rotational velocity.
- C. C. Lin, *Hydrodynamics of Helium II*, in *Liquid Helium*, Proc. Int. Sch. Phys. Enrico Fermi **21** (1963), 93–146 — the Clebsch form with its constraints, and the reason it is the natural variable set for a rotational flow.
- E. Cosserat and F. Cosserat, *Théorie des corps déformables*, Hermann, Paris, 1909 — the medium with an independent triad.
- A. C. Eringen, *Theory of Micropolar Fluids*, J. Math. Mech. **16** (1966), 1–18 — the modern formulation, with the couple stress and the moment balance.
- J. Weyssenhoff and A. Raabe, *Relativistic Dynamics of Spin-Fluids and Spin-Particles*, Acta Phys. Pol. **9** (1947), 7–18 — the relativistic spinning fluid, and the Frenkel condition as its constraint.
- H. K. Moffatt, *Magnetic Field Generation in Electrically Conducting Fluids*, Cambridge University Press, 1978 — the helicity and its conservation, which is the invariant of the rank-two case.
- J. L. Ericksen, "Theory of anisotropic fluids," *Transactions of the Society of Rheology* **4** (1960) 29–39, for the anisotropic fluid and the orientation field that a triad carries.
