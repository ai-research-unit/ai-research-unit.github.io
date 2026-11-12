# __The Vorticity Form and the Irrotational Condition__

## Introduction

**Irrotationality is not an assumption about how fluids behave; it is the statement that three components of the velocity are one datum.** A flow whose curl vanishes is the gradient of a scalar, so its three velocity components are the three derivatives of one function. A flow whose curl does not vanish carries two further numbers at each point, and those two numbers have no place in a description that carries only a density and a potential. This article states the obstruction, states the exception, and says which curl is meant.ne case the algebra was built for.

**The obstruction is a lemma, not a physical law.** If $\vec v=\nabla\Phi$ then $\nabla\times\vec v=0$ identically; conversely, if $\nabla\times\vec v=0$ on a simply connected domain then $\Phi$ exists. The converse is the Poincaré lemma, and its hypothesis is topological: the domain, not the flow. A flow with vanishing curl on a domain with a hole has a potential that is defined only up to a period around the hole. That period is the circulation, and it is the second subject of this article.

**The exception is topological, and it is a hole in the domain.** On a domain that is not simply connected the potential exists and is not single-valued: a loop that encircles the hole returns the potential to itself plus a constant, and that constant is the circulation. The point of the present article is that this exception is not a repair of the obstruction: it is the case in which the velocity *is* a gradient and the obstruction is the domain's, not the flow's.

**The article also fixes which curl is meant.** A flow can be read on the three-velocity or on the four-velocity, and the two readings' curls differ by a term that no relabelling removes. §*The Curl of the Two Readings* states the difference, and the rest of the article uses the Galilean curl, because the fluid of this section is Galilean.

## The Two Forms of Vorticity

**The vorticity is a two-form in the relativistic reading and a three-vector in the Galilean one.** The relativistic object is

$$
\omega_{\mu\nu}=\partial_\mu u_{\nu}-\partial_\nu u_{\mu},
$$

the exterior derivative of the four-velocity one-form, with $u_{\mu}$ the components of the normalised four-velocity. The Galilean object is

$$
\vec\omega_{\mathrm{vrt}}=\nabla\times\vec v,
$$

the curl of the three-velocity of [The Euler and Continuity Equations in Biquaternionic Form](the-euler-and-continuity-equations-in-biquaternionic-form.html).

**The two-form is the closure condition and the three-vector is its three-dimensional shadow.** A one-form is closed exactly when its exterior derivative vanishes, and $\omega_{\mu\nu}$ is that derivative; so $\omega_{\mu\nu}=0$ is the statement that $u_{\mu}$ is locally a gradient, which is the Poincaré lemma in four dimensions. In three dimensions the same lemma reads $\vec v=\nabla S/m$ exactly when $\vec\omega_{\mathrm{vrt}}=0$ on a simply connected domain.

**The 2-form is built on the four-velocity, which has four components, and the three-vector on the three-velocity.** That is the whole of the difference between them, and the next section computes it.

## The Curl of the Two Readings

**The two curls differ by a term in the gradient of the Lorentz factor.** The identity is

$$
\nabla\times\bigl(\gamma\vec v\bigr)=\gamma\,\nabla\times\vec v+\nabla\gamma\times\vec v ,
$$

which is the product rule for the curl applied to the product of a scalar and a vector. It is checked by expanding both sides in components, and it is exact for every differentiable pair $(\gamma,\vec v)$.

**So a flow that is irrotational in one reading need not be irrotational in the other.** The two curls agree only where $\nabla\gamma$ is parallel to $\vec v$, and a flow accelerated from rest has $\nabla\gamma$ transverse to $\vec v$ in general. The curl of $\vec v$ need not vanish even though $\omega_{\mu\nu}=0$, because $\gamma\vec v$ and not $\vec v$ is the spatial part of a four-vector.

**The classical fluid's vorticity is the Galilean one, and that is a choice with a cost.** An ordinary fluid's Euler equation is written on $\vec v$, not on $\gamma\vec v$, so the fluid's vorticity is $\nabla\times\vec v$ and the obstruction to a potential is $\nabla\times\vec v\ne0$. The cost is that the statement is frame-dependent: a change of frame changes $\gamma$ and therefore changes the Galilean curl. A covariant statement needs the 2-form, and a covariant fluid theory uses it.

**One consequence is worth stating because it is easy to get wrong.** A reader who takes the 2-form as the fluid's vorticity will call a flow irrotational that the fluid calls rotational, and the difference is a real term $\nabla\gamma\times\vec v$, not a convention. The two statements are both exact and they are statements about different objects.

## The Gradient Condition

**The vanishing of the curl is exactly the existence of a potential on a simply connected domain.** If $\vec\omega_{\mathrm{vrt}}=0$ everywhere on a domain that can be contracted to a point, there is a scalar $S$ with

$$
\vec v=\nabla\Phi ,
$$

and $\Phi$ is unique up to an additive constant. The potential carries the dimension of a velocity times a length, which is the dimension its gradient must have.

**The count is three to one.** A velocity with vanishing curl is fixed by one scalar; a velocity with non-vanishing curl needs the scalar and two more functions. The Helmholtz decomposition states the split exactly,

$$
\vec v=\nabla\Phi+\nabla\times\vec A ,
$$

with $\vec A$ a vector potential defined up to a gradient. In three dimensions the curl of a vector has three components but only two are independent, because $\nabla\cdot(\nabla\times\vec A)=0$; those two are the data the potential cannot carry.

**So the obstruction is a count and not a dynamical statement.** A rotational flow is not forbidden, unstable or unphysical. It carries two numbers per point that a description in two data has nowhere to put, and that is the whole of the difficulty.

## The Domain and the Winding

**On a domain with a hole the potential exists and is not single-valued.** Take an annulus around an obstacle. The curl vanishes on the annulus, so $\Phi$ exists locally; a loop that encircles the hole returns $\Phi$ to itself plus a constant, and the constant is the circulation

$$
\Gamma_{\mathrm{cir}}=\oint\vec v\cdot\mathrm{d}\vec r=\oint\nabla\Phi\cdot\mathrm{d}\vec r=\Delta\Phi .
$$

The circulation is the period of the potential, and it is not fixed by the local equations.

**In a classical fluid the period is free.** Potential flow around a cylinder has an arbitrary circulation, and the lift on the cylinder is $\rho_{\mathrm{mass}}U\Gamma_{\mathrm{cir}}$ with $U$ the free-stream speed. Nothing in the fluid equations fixes $\Gamma_{\mathrm{cir}}$; the Kutta condition of aerofoil theory is an extra hypothesis, added to select one value among a continuum.

**A period that is fixed rather than free requires a potential that is an angle.** An angle is defined modulo a full turn, so a loop that returns it to itself plus a whole number of turns fixes the circulation at a discrete set of values. That is a different class of fluid: the potential is a phase, the flow carries a quantised invariant, and the integer is the winding. This article states the free case, and the fixed case is a property of the reading rather than of the equations written here.

## What a Rotational Flow Is

**A rotational flow is the generic case, and its vorticity is dynamically active.** Plane Poiseuille flow between plates at $y=\pm H$ has $\vec v=U(1-y^{2}/H^{2})\,\vec e_x$ and

$$
\vec\omega_{\mathrm{vrt}}=\nabla\times\vec v=\frac{2Uy}{H^{2}}\,\vec e_z ,
$$

which vanishes only on the centreline. A vortex sheet has vorticity concentrated on a surface, and the Kelvin–Helmholtz instability is the statement that the sheet rolls up. Both are flows whose discarded data are not idle: the vorticity is what the instability feeds on.

**So the two discarded components are not a bookkeeping excess.** A description in two data per point has no room for them, and a fluid that has them evolves them by its own equation. The vorticity equation in two dimensions is

$$
\partial_{t'}\omega_{\mathrm{vrt},z}+\vec v\cdot\nabla\omega_{\mathrm{vrt},z}=0
$$

for an inviscid barotropic flow in two dimensions, so the vorticity is carried by the flow; and in three dimensions the stretching term $\vec\omega_{\mathrm{vrt}}\cdot\nabla\vec v$ amplifies it. Neither term has a counterpart in a scalar field's equation, because neither has an object to act on.

**This is the sharp form of the obstruction.** It is not that a rotational flow is complicated. It is that a rotational flow conserves and amplifies a quantity that a two-data description does not contain, and a description that discarded it would have to explain why the conserved quantity never matters.

## The Count in Two Lines

**Irrotationality removes two data and the barotropic condition removes one.** A general fluid has five continuous data at a point; a barotropic one has four; a barotropic irrotational one has two, the density and the potential. The three removals are the three conditions of the section, and this article owns the two.

**The two removed here are the pair that a two-data description cannot hold.** The density and the potential are two real numbers, and so is any rewriting of the flow in two data. The reduction is exact when the two excess components are gone and fails when they are present, which is why the article states the obstruction before the section states the map.

**The pair has a classical representation, and a representation is not a target.** A rotational velocity is $\nabla\phi_{\mathrm{clb}}+\alpha_{\mathrm{clb}}\nabla\beta_{\mathrm{clb}}$ in the Clebsch form, and its vorticity is the wedge of the pair, so the two excess components are two potentials and not two irreducible objects. What a two-data description lacks is not the *representation* of the pair but the *room* for it: its two real numbers are already spent on the density and the potential of the same flow. Irrotationality is therefore the rank-zero member of a family indexed by the rank of the vorticity, and [The Clebsch Potentials and the Rank of the Vorticity](the-clebsch-potentials-and-the-rank-of-the-vorticity.html) states the family and the medium — a fluid with an orientation — whose description does have the room.

## What Is Established and What Is Interpretation

**Established.** That the vanishing of the Galilean curl is exactly the existence of a potential on a simply connected domain, and that on a domain with a hole the potential has a period equal to the circulation. That the relativistic 2-form and the Galilean curl differ by $\nabla\gamma\times\vec v$, by the product rule. That a rotational flow carries two independent components beyond the potential, by the Helmholtz decomposition. That a free circulation and a quantised one are two different classes of fluid, distinguished by whether the potential is a function or an angle.

**Interpretation.** That the two excess components are the obstruction to a two-data description. The count says they are excess; that the excess is *the* obstruction, rather than one obstruction among many, is the programme's step, and the later articles test it. That a rotational flow's conserved vorticity is evidence against a hidden wave equation is a reading of the conservation law, not a theorem.

**Not claimed.** It is not claimed that irrotational flows are the only flows a fluid can have. A rotational flow is the generic case, it carries its own conserved quantity, and nothing in this article forbids it. What is claimed is narrower: within this section's variables, irrotationality is the condition under which three velocity components collapse to one datum, and it is exactly the condition the count requires.

## Summary

A flow is irrotational when its curl vanishes, and on a simply connected domain that is exactly the condition for the velocity to be the gradient of a potential, $\vec v=\nabla\Phi$.

The relativistic vorticity is the 2-form $\omega_{\mu\nu}$ of the normalised four-velocity; the Galilean vorticity is the curl of $\vec v$. They differ by $\nabla\gamma\times\vec v$, so a flow can be irrotational in one reading and not in the other. The fluid of this section uses the Galilean one.

The obstruction is a count. A general velocity has three components; a gradient has one; the two that remain are the transverse part, and the Helmholtz decomposition exhibits them.

On a domain with a hole the potential is multi-valued and its period is the circulation. The period is free, and the lift on a body is proportional to it; every selection of one value is an extra condition and not a consequence of the equations.

A period that is fixed rather than free requires a potential that is an angle. An angle is defined modulo a full turn, so a loop that returns it to itself plus a whole number of turns fixes the circulation at a discrete set of values. That is a property of the reading and not of the equations written here, and it belongs to the wave's account of a fluid rather than to the fluid itself.

A rotational flow is the generic case, and its vorticity is conserved in two dimensions and stretched in three. A two-data description has no room for it, and a map that discarded it would have to explain why it never matters.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\vec v$ | Three-velocity |
| $\vec\omega_{\mathrm{vrt}}=\nabla\times\vec v$ | Galilean vorticity, the curl |
| $\omega_{\mu\nu}=\partial_\mu u_{\nu}-\partial_\nu u_{\mu}$ | Relativistic vorticity 2-form |
| $u_{\mu}$ | Components of the normalised four-velocity |
| $\gamma=1/\sqrt{1-\lvert\vec v\rvert^{2}/c^{2}}$ | Lorentz factor |
| $\Phi$ | Velocity potential; $\vec v=\nabla\Phi$ |
| $\vec A$ | Vector potential of the rotational part |
| $\Gamma_{\mathrm{cir}}=\oint\vec v\cdot\mathrm{d}\vec r$ | Circulation around a loop |
| $\rho_{\mathrm{num}}$ | Number density of markers |
| $U$ | Free-stream speed, in the cylinder example |
| $H$ | Half-separation of the plates, in the Poiseuille example |

## Further Reading

- Hermann von Helmholtz, "Über Integrale der hydrodynamischen Gleichungen, welche den Wirbelbewegungen entsprechen," *Journal für die reine und angewandte Mathematik* **55** (1858) 25–55, for the vorticity theorems and the conservation of circulation.
- Henri Poincaré, "Sur les résidus des intégrales doubles," *Acta Mathematica* **9** (1887) 321–380, and the lemma that carries his name, for the passage from a closed one-form to a potential.
- Horace Lamb, *Hydrodynamics*, 6th ed. (Cambridge University Press, 1932), ch. II and art. 45, for irrotational flow, the velocity potential and the circulation around an obstacle.
- George K. Batchelor, *An Introduction to Fluid Dynamics* (Cambridge University Press, 1967), §§2.7 and 7.2, for the Helmholtz decomposition and for vorticity dynamics.
- Andrew J. Majda and Andrea L. Bertozzi, *Vorticity and Incompressible Flow* (Cambridge University Press, 2002), ch. 1, for the vorticity equation and the stretching term.
- The companion articles: [The Euler and Continuity Equations in Biquaternionic Form](the-euler-and-continuity-equations-in-biquaternionic-form.html), [The Equation of State and the Barotropic Condition](the-equation-of-state-and-the-barotropic-condition.html), [The Reverse Madelung Map: Fluid to Nonlinear Wave](the-reverse-madelung-map-fluid-to-nonlinear-wave.html).
- The applications of this article's variables to the quantum theory are in the spin-zero and spin-one-half blocks of the index, where the circulation's quantum and the flow that is a frame rather than a gradient are worked out.
