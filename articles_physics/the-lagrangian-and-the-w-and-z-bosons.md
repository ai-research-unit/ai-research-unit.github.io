# __The Lagrangian and the W and Z Bosons__

## Introduction

This article writes the massive vector bosons of the electroweak sector as the extremum of one action, and shows that their masses are not parameters of that action but products of a coupling and a vacuum value. It is the action-first companion of *The $W$, $Z$ and $W_R$ Bosons in Biquaternionic Form*, which states the fields, the mixing and the masses; this article asks what functional produces the Proca-like equations of the two bosons, and where the masses in it come from.

Its place in the sector. The functional here is the gauge and scalar part of the sector's complete action, written in [The Lagrangian and the Electroweak Theory](the-lagrangian-and-the-electroweak-theory.html). That article is the sector's action; this one is the $W$–$Z$ reading of it, and it stops at the two curvatures and the scalar's gradient term.

The equation. The parent's equations are the Yang–Mills equations for $W_{a,\mu}$ and $B_\mu$ with a source,

$$
D_\nu W_{a,\mu\nu}=\frac{g}{2}\,\omicron_{\mathrm{hgs}}^{\dagger}\tau_{a} i\!\overleftrightarrow{D_\mu}\omicron_{\mathrm{hgs}} ,
\qquad
\partial_\nu B_{\mu\nu}=g_{\mathrm Y}\,Y_{\mathrm{hch}}\,\omicron_{\mathrm{hgs}}^{\dagger}i\!\overleftrightarrow{D_\mu}\omicron_{\mathrm{hgs}} ,
$$

where the right sides are the currents of the scalar doublet evaluated at its vacuum value, and the mass terms are what those currents become when $\omicron_{\mathrm{hgs}}$ sits at the minimum of its potential.

Three things are established.

*First, the action.* With $W_{a,\mu\nu}$ and $B_{\mu\nu}$ the curvatures of $SU(2)_L\times\mathrm{U}(1)_Y$ and $\omicron_{\mathrm{hgs}}$ the doublet,

$$
S=\int d^4r\;\Bigl[-\tfrac14\sum_{a,\mu,\nu}W_{a,\mu\nu}W_{a,\mu\nu}-\tfrac14\sum_{\mu,\nu}B_{\mu\nu}B_{\mu\nu}
+\sum_\mu\bigl(D_\mu\omicron_{\mathrm{hgs}}\bigr)^{\dagger}\bigl(D_\mu\omicron_{\mathrm{hgs}}\bigr)-V(\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}})\Bigr],
$$

varying $W_{a,\mu}$ and $B_\mu$ gives the parent's equations with the scalar current as source, and evaluating the scalar at its minimum turns the kinetic term into a mass term for two of the four gauge fields.

*Second, the masses are forced by one number.* Every mass in the sector is $g\,v/2$ or $\sqrt{g^2+g_{\mathrm Y}^2}\,v/2$, and the ratio is fixed at one,

$$
\rho=\frac{M_W^2}{M_Z^2\cos^2\theta_W}=1 ,
$$

because one doublet of weak isospin $\tfrac12$ produces both masses from the same $v$. The relation is a consequence of the action's structure and not a fit.

*Third, the group is the algebra's and the representation is imported.* The algebra carries $\mathrm{U}(1)$ exactly, and it carries $\mathrm{SU}(2)$ exactly as well, since the compact factor is the spin group $\mathrm{Spin}(3)=S^{3}$; what it cannot supply is the doublet, a representation chosen independently of the spin, nor the chiral split on one letter. So this article's action is written in components and the biquaternionic translation is claimed only where it holds. The status of each line is stated at the line.

The electroweak action is standard and is imported whole. What the corpus contributes is the exact $\mathrm{U}(1)$ line, the identification of the Higgs mass formula with the abelian one, and the statement of where the algebra stops.

## Conventions

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_\eta^{2}=-e_t$, used for the fermion and scalar elements; the gauge fields are written in components, because the $SU(2)$ factor is not carried by a single algebra element.

The group and the couplings. $SU(2)_L$ with coupling $g$ and generators $\tau_{a}=\sigma_{a}/2$ in the doublet; $\mathrm{U}(1)_Y$ with coupling $g_{\mathrm Y}$ and hypercharge $Y$. The doublet has $Y_{\mathrm{hch}}=\tfrac12$ and $T_3=\pm\tfrac12$ on its two components.

The curvatures. $W_{a,\mu\nu}=\partial_\mu W_{a,\nu}-\partial_\nu W_{a,\mu}+g\sum_{b,c}\varepsilon_{abc}W_{b,\mu} W_{c,\nu}$ and $B_{\mu\nu}=\partial_\mu B_\nu-\partial_\nu B_\mu$, with $\partial_\mu=\partial/\partial R_\mu$.

The vacuum. $\langle\omicron_{\mathrm{hgs}}\rangle=(0,\;v/\sqrt2)^{T}$ with $v=246.22$ GeV; the potential is $V=\lambda(\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}}-v^2/2)^2$, so that $\partial V/\partial\omicron_{\mathrm{hgs}}^{\dagger}=0$ at the minimum and the mass of the radial mode is $\sqrt{2\lambda}\,v$.

The sign convention. The curvature terms enter with $-\tfrac14$, the scalar kinetic term with a plus sign, and the potential with a minus sign, so that the Hamiltonian is positive and the potential's minimum is the vacuum. Every sign below follows from that choice.

## The Action in Element Form

The gauge sector. Two curvatures and their squares,

$$
\mathcal{L}_{\mathrm{gauge}}=-\tfrac14\sum_{a,\mu,\nu}W_{a,\mu\nu}W_{a,\mu\nu}-\tfrac14\sum_{\mu,\nu}B_{\mu\nu}B_{\mu\nu},
$$

with no mass term. A mass term $\tfrac12M^2W_\mu W_\mu$ would break the local symmetry explicitly and make the theory non-renormalizable, so the action cannot contain the masses at this stage; they must come from somewhere else, and the next paragraph is that somewhere.

The scalar sector. One doublet with a covariant derivative and a potential,

$$
\mathcal{L}_{\mathrm{scalar}}=\sum_\mu\bigl(D_\mu\omicron_{\mathrm{hgs}}\bigr)^{\dagger}\bigl(D_\mu\omicron_{\mathrm{hgs}}\bigr)-\lambda\Bigl(\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}}-\frac{v^2}{2}\Bigr)^{2},
\qquad
D_\mu=\partial_\mu+ig\sum_a\tau_{a} W_{a,\mu}+i g_{\mathrm Y}Y_{\mathrm{hch}} B_\mu .
$$

The covariant derivative is where the masses live: it contains the gauge fields multiplied by the generators, and when $\omicron_{\mathrm{hgs}}$ is replaced by its vacuum value the product becomes a constant matrix times $W_\mu W_\mu$.

The mass term from the vacuum. Writing $\omicron_{\mathrm{hgs}}=\langle\omicron_{\mathrm{hgs}}\rangle+\eta$ and keeping the quadratic terms,

$$
\sum_\mu\bigl(D_\mu\omicron_{\mathrm{hgs}}\bigr)^{\dagger}\bigl(D_\mu\omicron_{\mathrm{hgs}}\bigr)\supset\frac{v^2}{8}\Bigl[g^2\bigl(W_{1,\mu} W_{1,\mu}+W_{2,\mu} W_{2,\mu}\bigr)+\bigl(gW_{3,\mu}-g_{\mathrm Y}B_\mu\bigr)^{2}\Bigr],
$$

which is a mass matrix for the four gauge fields. It is rank three: one combination is massless, and that combination is the photon.

The diagonalization. With

$$
W^{\pm}_\mu=\frac{1}{\sqrt2}\bigl(W_{1,\mu}\mp iW_{2,\mu}\bigr),
\qquad
Z_\mu=\cos\theta_W\,W_{3,\mu}-\sin\theta_W\,B_\mu,
\qquad
A_\mu=\sin\theta_W\,W_{3,\mu}+\cos\theta_W\,B_\mu,
\qquad
\tan\theta_W=\frac{g_{\mathrm Y}}{g},
$$

the mass matrix is diagonal and

$$
M_W=\frac{gv}{2},
\qquad
M_Z=\frac{\sqrt{g^2+g_{\mathrm Y}^2}\,v}{2}=\frac{M_W}{\cos\theta_W},
\qquad
M_A=0 .
$$

The mixing angle is not a new parameter: it is $\arctan(g_{\mathrm Y}/g)$, fixed by the two couplings the action already carries.

Why the linear combination and not another. The mass matrix in the $(W_3,B)$ plane is $\frac{v^2}{8}\bigl(\begin{smallmatrix}g^2&-gg_{\mathrm Y}\\-gg_{\mathrm Y}&g_{\mathrm Y}^2\end{smallmatrix}\bigr)$, whose determinant is zero. A rank-one $2\times2$ matrix has one zero eigenvalue and one nonzero one, and the zero eigenvector is $(g_{\mathrm Y},g)$-normalized, which is the photon. The vanishing determinant is the statement that the unbroken subgroup is one-dimensional, and it is a consequence of the rank of the doublet's generator set and not of a tuning.

**The pairing is the Hermitian norm, and it is what makes the scalar's kinetic term real and positive.** $\sum_\mu(D_\mu\omicron_{\mathrm{hgs}})^{\dagger}(D_\mu\omicron_{\mathrm{hgs}})$ is a sum of squared norms, real and non-negative term by term. The gauge kinetic terms are real because $W_{a,\mu\nu}$ and $B_{\mu\nu}$ are real in components and their squares carry the corpus's sign rule.

Why the scalar needs the dagger and the gauge fields do not. The scalar is complex, so its kinetic term needs a conjugate to be real; the gauge fields are real, so theirs does not. The asymmetry is a statement about the representations and not about the pairing.

Three coefficients: two couplings and one vacuum value. $g$ and $g_{\mathrm Y}$ are dimensionless; $v$ has dimension of mass. The masses are products $g\,v$, so their dimensions are right by construction, and the ratio $M_Z/M_W$ is a pure number fixed by the two couplings.

The potential's coefficients are not independent of them. $\lambda$ sets the radial mass and $v$ sets the minimum; the combination $\sqrt{2\lambda}\,v$ is the Higgs mass, and it is the one number of the sector that the action does not relate to the gauge couplings. That independence is why the Higgs mass is a measurement and the $W$ and $Z$ masses are predictions.

The selection rule is local $SU(2)_L\times\mathrm{U}(1)_Y$ invariance, and it forbids exactly two things. A gauge mass term is forbidden, which is why the masses come from the scalar; a bare fermion mass is forbidden, which is why the Yukawa couplings exist. Every term in the action is the most general one of dimension four invariant under the group, and the count of those terms is the count of parameters the sector has.

Reality does not buy the masses, the mixing angle or $\rho=1$. Three things the reality of the action does not supply:

- *No mass without a vacuum.* The action is real and symmetric; the masses appear only when a field takes a value. The symmetry of the action and the asymmetry of the vacuum are compatible because the vacuum is one of infinitely many.
- *No prediction of $v$.* The vacuum value is measured, through $G_F$; the action accepts it.
- *No protection of $\rho$.* The relation $\rho=1$ requires the doublet to be a single $\tfrac12$ representation; a second scalar multiplet would break it, and the action permits one.

## The Variation: The Currents Are the Sources

The variation with respect to the gauge fields. Varying $W_{a,\mu}$ and integrating by parts,

$$
\delta S=\int d^4r\;\Bigl[\delta W_{a,\mu}\Bigl(D_\nu W_{a,\mu\nu}-j_{a,\mu}\Bigr)\Bigr],
\qquad
j_{a,\mu}=\frac{g}{2}\,\omicron_{\mathrm{hgs}}^{\dagger}\tau_{a} i\!\overleftrightarrow{D_\mu}\omicron_{\mathrm{hgs}}+\text{(fermion terms)},
$$

so that the stationarity condition is $D_\nu W_{a,\mu\nu}=j_{a,\mu}$, and analogously for $B_\mu$. The current contains the scalar's contribution and the fermions', and the two enter on the same footing.

The variation with respect to the scalar. Varying $\omicron_{\mathrm{hgs}}^{\dagger}$ gives

$$
-D_\mu D_\mu\omicron_{\mathrm{hgs}}-\frac{\partial V}{\partial\omicron_{\mathrm{hgs}}^{\dagger}}=0 ,
$$

the gauged Klein–Gordon equation with a potential. At the vacuum this equation is satisfied identically, which is the statement that the vacuum is stationary and that the masses computed above are consistent with it.

**The self-consistency that the two variations must satisfy.** The current must be conserved, $D_\mu j_{a,\mu}=0$, or the equation for $W_{a,\mu}$ is inconsistent because the left side is divergenceless by the Bianchi identity. The conservation is not assumed: it follows from the scalar's equation combined with the antisymmetry of $W_{a,\mu\nu}$, and it holds because the scalar's covariant derivative is the same object in both equations. A mass term written by hand would break this, which is the technical reason the masses must come from the scalar.

The check that would catch a factor. At the vacuum, $j_{a,\mu}=0$ for the unbroken directions and nonzero for the broken ones; the equation then reduces to $D_\nu W_{a,\mu\nu}=0$ with $W_{a,\mu}$ satisfying a Proca equation. The coefficient of the mass must be $\frac{g^2v^2}{4}$ and not $\frac{g^2v^2}{8}$, because the $\overleftrightarrow{D}$ convention carries a factor two; the boxed masses above are the check.

## The Constraints the Action Imposes: Four Gauss Laws and One Massless Mode

The constraint structure. Each gauge field brings a first-class constraint, the Gauss law $D_j W_{a,0j}=j_{a,0}$, so four constraints act on eight gauge components, and the three Goldstones are not removed by the constraints but absorbed as longitudinal modes. Counting polarisation states before and after the breaking,

$$
\underbrace{8}_{\text{four vectors, massless}}+\underbrace{4}_{\text{four scalars}}\;=\;\underbrace{9}_{\text{three massive vectors}}+\underbrace{2}_{\text{photon}}+\underbrace{1}_{\text{radial scalar}}\;=\;12 ,
$$

so no mode is lost and none is added: three of the four scalars become the longitudinal modes of the three vectors that acquire a mass, and what remains is three massive vectors of three modes each, a massless vector of two and one radial scalar. In particles rather than modes the same spectrum is five states, $W^{+}$, $W^{-}$, $Z$, $A$ and $h$. The count is the same in any gauge; the distribution is not.

Why the Goldstones are removed and not the modes. The scalar's four components are three Goldstones and one radial mode, and the three Goldstones become the longitudinal polarizations of the three massive gauge fields. The bookkeeping is exact: three massless gauge fields would have six polarizations in total counting the photon, and three massive ones have nine, so three polarizations must be supplied, and the Goldstones supply them.

The one massless combination. The photon's masslessness is the vanishing eigenvalue of the mass matrix, and it is a constraint in the technical sense: the unbroken $\mathrm{U}(1)_{\mathrm{em}}$ generator annihilates the vacuum, so its Gauss law survives as a constraint and the corresponding field stays massless. That is the same mechanism as in the electromagnetic article, with the generator being the combination $Q=T_3+Y$.

The check that the count is gauge independent. In the $R_\xi$ gauge the Goldstones are kept with $\xi$-dependent masses and the same twelve modes over the same five states appear; in the unitary gauge they are removed and the gauge propagators take their Proca form. The two descriptions differ in what is counted and agree in what is physical, which is the content of the gauge-fixing article for this sector.

## The Structural Consequence: Masses Are Couplings Times a Vacuum Value

The relation, and why it is structural. Both masses are the same vacuum value times a coupling, and the coupling is the one that already appears in the covariant derivative. Nothing new is introduced: $M_W=gv/2$ uses $g$ from $D_\mu$ and $v$ from the potential, and $M_Z$ uses the orthogonal combination. The statement "the mass is not a parameter of the theory" is the statement that the action has no mass term and that the masses are computable from the terms it does have.

The ratio, and the isospin that fixes it. The two masses differ because the doublet's generators differ: $T_3=\pm\tfrac12$ gives the $W$ its $g/2$, and the neutral combination gives $\sqrt{g^2+g_{\mathrm Y}^2}$ with a factor $\tfrac12$ from the same normalization. The factor $\tfrac12$ is the isospin of the scalar, not a property of the vector, and that is the point the parent's mass-formula discussion makes.

The abelian formula is the same formula. The corpus's charged-scalar formula $M_A=\kappa v$ for a $\mathrm{U}(1)$ charge $\kappa$ reproduces $M_W=gv/2$ with $\kappa=g/2$, which is the effective charge of the doublet's component. The two derivations agree, and the agreement is the check that the mass mechanism is one mechanism and not two.

**What the structure predicts and what it does not.** It predicts the ratio $\rho=1$ and the relation $e=g\sin\theta_W$; it does not predict $v$, $g$ or $g_{\mathrm Y}$, which are three measurements written as two couplings and one scale. The count of the sector's parameters is the Yukawa article's, and this article's contribution to it is that the gauge masses add none.

## The Noether Currents: The Electroweak Currents and the Sign of the Charge

The currents of the global group. Before gauging, the action is invariant under constant $SU(2)_L\times\mathrm{U}(1)_Y$, and the Noether currents are

$$
J_{a,\mu}=\frac{g}{2}\,\omicron_{\mathrm{hgs}}^{\dagger}\tau_{a} i\!\overleftrightarrow{D_\mu}\omicron_{\mathrm{hgs}}+\bar\psi\gamma_\mu\tau_{a}\psi ,
\qquad
J^{Y}_\mu=g_{\mathrm Y}\,Y_{\mathrm{hch}}\,\omicron_{\mathrm{hgs}}^{\dagger}i\!\overleftrightarrow{D_\mu}\omicron_{\mathrm{hgs}}+\bar\psi\gamma_\mu Y\psi ,
$$

which are exactly the sources in the equations of motion. The identification of the two is not a coincidence: it is the statement that gauging a global symmetry makes its Noether current the source of the gauge field, and it is the reason the variation with respect to the gauge field and the Noether construction give the same object.

The electromagnetic current. The combination that survives the breaking is

$$
J^{\mathrm{em}}_\mu=J^3_\mu+J^{Y}_\mu ,
$$

with the charge operator $Q=T_3+Y$, and its conservation is exact because the unbroken generator annihilates the vacuum. The charged current $J^{\pm}_\mu=J_{1,\mu}\mp iJ_{2,\mu}$ is conserved as an equation of motion but not as a symmetry of the vacuum, and that difference is the reason the $W$ is massive and the photon is not.

The sign of the charge. The covariant derivative's sign convention $D_\mu=\partial_\mu+ig\tau_{a}W_{a,\mu}$ fixes the sign of the current, and the corpus's opposite-sign convention would reverse every current without changing the physics. The convention is declared once in *Conventions* so that the sign is checkable rather than inherited silently.

Energy–momentum. Translation invariance gives $T_{\mu\nu}$ with contributions from the gauge and scalar sectors, and its trace is the measure of the breaking: the trace is nonzero in the broken phase because the mass terms are not conformally invariant, and the trace is the anomaly's classical part. The quantum trace is the precision-observables article's.

**What there is not.** No baryon number current from this action; the $B$ and $L$ currents are the fermion sector's and are anomalous, which the anomaly article treats.

## What the Principle Adds and What It Relabels

Adds.

- *The masses' origin in one place.* The action shows that the mass terms are the scalar's kinetic term evaluated at a value, and that no separate mass term is needed or allowed.
- *The identity of the two variations.* The Noether current and the equation's source are the same object, and the action is what makes that visible.
- *A reason for the photon's masslessness.* The vanishing eigenvalue of the mass matrix is a property of the generator algebra, readable from the action's quadratic form.

Relabels.

- *The "Higgs mechanism".* It is not a mechanism added to the gauge theory; it is what the scalar's kinetic term does when the scalar is not zero. The action contains no separate Higgs sector.
- *The mixing angle.* It is not a parameter; it is $\arctan(g_{\mathrm Y}/g)$.
- *The mass matrix.* It is not an object to be diagonalized by choice; its rank is fixed by the representation content, and the diagonalization is a change of basis in the same action.

The distinction that matters. The action is symmetric and the vacuum is not. Everything structural in this sector follows from that one sentence: the masses, the mixing, the Goldstone count and $\rho=1$.

## Open Questions

**Why one doublet?** The action permits any number of scalars; the $\rho=1$ relation and the absence of flavour-changing neutral currents select one at tree level. Whether the algebra constrains the count is not established.

## Summary

The action. Gauge kinetic terms plus one scalar's covariant kinetic term and potential. Varying the gauge fields gives the Yang–Mills equations with the scalar current as source; evaluating the scalar at its minimum turns the kinetic term into masses $M_W=gv/2$ and $M_Z=M_W/\cos\theta_W$.

The three findings. The masses are not parameters but products of a coupling and the vacuum value, so the action needs no mass term and forbids one. The ratio $\rho=1$ is a consequence of the single doublet. The photon's masslessness is the zero eigenvalue of a rank-three mass matrix.

The boundary. Both lines are carried by the algebra, since the compact factor is the spin group; what is transcribed is the doublet's representation and its chiral split. The value of $v$ and the number of scalars are not derived.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $W_{a,\mu}$, $B_\mu$ | $SU(2)_L$ triplet and $\mathrm{U}(1)_Y$ field |
| $W_{a,\mu\nu}$, $B_{\mu\nu}$ | their curvatures |
| $g$, $g_{\mathrm Y}$ | the two couplings |
| $\omicron_{\mathrm{hgs}}$ | scalar doublet, $Y_{\mathrm{hch}}=\tfrac12$ |
| $v$ | vacuum value, $246.22$ GeV |
| $\theta_W$ | $\arctan(g_{\mathrm Y}/g)$ |
| $W^\pm_\mu$, $Z_\mu$, $A_\mu$ | mass eigenstates |
| $\rho$ | $M_W^2/(M_Z^2\cos^2\theta_W)$ |

## Further Reading

- [The $W$, $Z$ and $W_R$ Bosons in Biquaternionic Form](the-w-and-z-bosons-in-biquaternionic-form.html) — the parent: the mixing, the pole observables and the effective angle.
- [The Lagrangian and the Electroweak Theory](the-lagrangian-and-the-electroweak-theory.html) — the same action in element form, with the four Gauss constraints written out.
- [Electroweak Symmetry Breaking: the Doublet, the Potential and the Gauge-Boson Masses](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-gauge-boson-masses.html) — the vacuum and the potential's minimum.
- [The Standard Model and the Lagrangian: Four Sectors in One Expression](the-standard-model-and-the-lagrangian-four-sectors-in-one-expression.html) — this sector inside the assembled action.
- [Gauge Fixing in the Electroweak Theory: $R_\xi$ Gauges, Ghosts and the Goldstone Equivalence Theorem](gauge-fixing-in-the-electroweak-theory-r-xi-gauges-ghosts-and-the-goldstone-equivalence-theorem.html) — the gauge-dependent bookkeeping of the same count.
