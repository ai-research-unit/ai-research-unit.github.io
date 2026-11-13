# __The Domain of the Fluid Reading__

## Introduction

**The polar word exists exactly on the elements of nonzero norm, and that set is not the whole algebra.** The word is a parametrisation of the units, so it is defined where the element is invertible and nowhere else. The complement is the zero-divisor cone: the set of elements whose quaternionic norm vanishes. On the cone the field is not zero, the density is usually not zero, and the chart nevertheless fails. That is the article's subject.

**The cone is a complex hypersurface and not a real one.** The norm is a complex number, so its vanishing is two real conditions on eight real parameters and the cone has six real dimensions. It is the set of singular matrices in the algebra's matrix representation, and its real codimension is two. The word "cone" is exact: the set is invariant under multiplication by any central scalar.

**The fluid is not empty where the chart fails.** Two families of fields lie on the cone with a density that is nowhere zero: the elements of definite value, and the one-sided plane waves. So the failure of the chart is not a failure of the field, and a fluid reading that identified the two would report a vacuum where the field is at its loudest.

**What the article is and is not.** It states the domain, proves its geometry, exhibits the two families, and lists the three places where the reading is a limit rather than an identity. It adds no dynamics: the domain is a condition on the field at an event, and the field can leave the domain without leaving the equation. The boundary of the reading is the article's whole content, and the closing section states it as a boundary and not as a defect.

## The Domain

### The Statement

**The word exists if and only if the norm does not vanish.**

*Theorem.* The polar word $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ exists on $\tilde\Xi$ if and only if $N(\tilde\Xi)\neq0$.

*Proof.* The word divides by the modulus $\Rho$, and $\Rho^{2}=N(\tilde\Xi)$. A division by $\Rho$ is a division by zero exactly where $N$ vanishes. Conversely, where $N\neq0$ the modulus is a nonzero central number and the element $\tilde\Xi/\Rho$ is a unit; the polar decomposition of a unit into a Hermitian boost and a real rotor is [The Relativistic Quantum Space as a Fluid](the-relativistic-quantum-space-as-a-fluid.html)'s proposition, and it applies to every unit.

**The word's existence is therefore a property of the element and not of the field's equation.** Nothing in the field equation enters the statement. The equation decides which elements occur; the algebra decides which occur in the chart.

### The Extractions That Need It

**All four of the word's extractions divide by the modulus, and each fails with it.** The density is $r^{2}=\lvert N\rvert$, the velocity is the inverse square of the boost, the spin direction is the rotor's image of the declared axis, and the phase is $\tfrac12\arg N$. None is defined where $N=0$:

| extraction | formula | fails because |
| --- | --- | --- |
| density | $\rho=r^{2}$ | $r=0$ on the cone |
| phase | $\theta_{\mathrm{pha}}=\tfrac12\arg N$ | $\arg0$ is undefined |
| velocity | $\tilde V_{\Phi}=ic\tilde U_{\Psi,\mathrm b}^{-2}$ | the boost is not extracted |
| spin | $\vec s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$ | the rotor is not extracted |

**The failure is a single failure and not four.** The three frames are read from one unit, and the unit is what the modulus normalises. So the chart either exists whole or not at all, and there is no partial word that keeps the density and drops the velocity.

**This is the sharp form of the difference between a chart and a field.** A field has a value at every event; a chart has a value only where its coordinates exist. The two are identified in the interior of the domain and must not be identified on its boundary.

## The Geometry of the Cone

### Codimension Two

**The norm is complex, so its vanishing is two real conditions.** For $\tilde Q=Q_t e_t+\vec Q$,

$$
N(\tilde Q)=Q_t^{2}+\vec Q\cdot\vec Q,
$$

and both $Q_t$ and $\vec Q$ are complex. The right-hand side is complex, so $N=0$ is two real equations on the eight real parameters of the element, and the solution set has six real dimensions.

**Checked by perturbing a zero divisor along each of the eight real coordinate directions.** The element $e_t+i\vec e_z$ has $N=0$. Adding $0.1$ to one coefficient at a time gives $\lvert N\rvert=0.21$, $0.2002$, $0.01$, $0.01$, $0.01$, $0.01$, $0.2002$, $0.21$ for the perturbations of $\mathrm{Re}\,Q_t$, $\mathrm{Im}\,Q_t$, $\mathrm{Re}\,Q_x$, $\mathrm{Im}\,Q_x$, $\mathrm{Re}\,Q_y$, $\mathrm{Im}\,Q_y$, $\mathrm{Re}\,Q_z$ and $\mathrm{Im}\,Q_z$. Every direction leaves the element off the cone, so the cone has no open neighbourhood anywhere.

**The two small values are the tangent plane, and they confirm the count.** The $x$ and $y$ directions displace $N$ quadratically, $\lvert N\rvert=d^{2}=0.01$ at $d=0.1$, while the temporal and $z$ directions displace it linearly, $\lvert N\rvert=2d+d^{2}=0.21$. So the tangent space of the cone at this element contains the $x$ and $y$ directions and the other six are transverse: two directions are flat and six are not, which is real codimension two measured at a point.

**The matrix picture gives the same count.** The algebra is the complex $2\times2$ matrices in its standard representation, and $N$ is the determinant up to a factor. The cone is the singular matrices, a complex hypersurface of complex dimension three and real dimension six.

**The word "hypersurface" therefore needs its qualifier.** It is a hypersurface over $\mathbb{C}$ and a codimension-two set over $\mathbb{R}$. A sentence that calls it a real hypersurface is off by one dimension, and the difference matters in the perturbation check above: a real hypersurface would be left by a generic perturbation in one direction and a codimension-two set is left by every direction.

### It Is a Cone

**The set is invariant under multiplication by any central scalar.** $N(c\tilde Q)=c^{2}N(\tilde Q)$, so if $\tilde Q$ is a zero divisor then so is $c\tilde Q$ for every central $c$. The set is therefore a union of complex lines through the origin, which is what makes the name exact and what makes the failure uniform in amplitude: a zero divisor is a zero divisor at every scale.

**Checked on a family.** For the element $\tilde X=e_t+i\vec e_z$ scaled by $0.3$, $1$ and $5$, the norm is $0$ in all three cases and the Hermitian norm is $0.18$, $2$ and $50$. The field grows and the chart never returns.

## Two Families on the Cone

### Elements of Definite Value

**An element that is an eigenvector of right multiplication by $\vec e_z$ is a zero divisor, and it is one at every amplitude.** For $\tilde X$ with $\tilde X\vec e_z=\pm i\tilde X$,

$$
\tilde X\bigl(\vec e_z\mp ie_t\bigr)=0,
\qquad
\vec e_z\mp ie_t\neq0,
$$

so $\tilde X$ annihilates a nonzero element and is a zero divisor. The annihilation is the algebra's own statement and it does not depend on the size of $\tilde X$.

**This family is the field of definite chirality.** The eigenvalue equation is the projection onto one chiral piece, so the family is the set of fields carrying a single chirality, and the theorem says that such a field has no word at any amplitude. That is not a statement about small fields: a chiral field of any strength is outside the chart.

**The density on this family is not zero.** The Hermitian norm of the scaled element is $0.18$, $2$ and $50$ above, so the density grows with the amplitude while the word stays undefined. A reader who equated "no word" with "no field" would be wrong by the whole amplitude.

### One-Sided Plane Waves

**A null wavevector produces a field that is a zero divisor everywhere and is nowhere zero.** With $\tilde K_{\Phi}$ null, $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=0$, the plane wave $\tilde\Xi=\tilde\Xi_{0}e^{i\tilde K_{\Phi}\cdot\tilde X}$ satisfies the field equation with $\tilde\Xi_{0}$ a nonzero zero divisor, and

$$
N(\tilde\Xi)=N(\tilde\Xi_{0})\,e^{2i\tilde K_{\Phi}\cdot\tilde X}=0
$$

at every event, because a nonzero zero divisor multiplied by anything is a zero divisor.

**This is the massless one-sided wave and it is the second family.** It differs from the first in kind: the first is a pointwise condition on the value and the second is a condition on the wavevector that holds at every event of a solution. Both are on the cone and both have non-vanishing density.

**The two families are the answer to the obvious objection.** The objection says that the cone is a set of measure zero and can be ignored. The answer is that two physically named families live on it, one of them the chiral fields and the other the one-sided massless waves, so the set is not a curiosity of the parameter space but a place where standard fields sit.

## The Cone Against the Nodal Set

**The nodal set is where the field vanishes and the cone is where its norm vanishes, and the second contains the first and is strictly larger.** For the scalar field the two coincide, because the centre's norm is $\Xi_t^{2}$ and a vanishing norm is a vanishing field. For the spinor field they do not.

**The scalar case is the exception and it is worth stating why.** On the centre the element is a single complex number, the norm is its square, and the norm vanishes exactly when the number does. So the scalar fluid's chart fails exactly at the wave's nodes, and there the density vanishes too, which is why the scalar fluid can be read as a fluid with vortices rather than as a chart with holes. [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html) works that case and the difference is its subject.

**In the spinor case the chart fails where the fluid is loudest.** Both families above have a non-vanishing density on part of their extent, so the chart's boundary cuts through the region where a fluid reading would be most confident. That is a structural fact about the algebra and it is the reason this article exists.

## The Two-Factor Decomposition

**What survives on the cone is the two-factor decomposition, and it is defined on the whole algebra.** Every element factors as

$$
\tilde\Xi=\tilde\Xi_{H}\tilde\Xi_{0},
$$

with $\tilde\Xi_{H}$ Hermitian positive semidefinite and $\tilde\Xi_{0}$ a partial isometry. The factorisation is defined where the four-factor word is not, because it divides by the *nonzero* singular values of the element rather than by its norm.

**What the two factors carry and what they do not.** The Hermitian factor carries the scale, and the partial isometry carries the direction; the split between the velocity and the spin is not made, because it needs the modulus to normalise two frames against each other.

**So the loss is specific.** The chart loses the separation of the two frames and keeps the separation of scale from direction. A fluid needs the first separation and not only the second, which is why the two-factor form is a fallback for the algebra and not a substitute for the fluid.

**The count says the same thing.** The two-factor form has the scale and the partial isometry's parameters; the four-factor word has those plus two independent frames. On the cone the extra parameters are what the division by the modulus would have given, and the division is what fails.

## The Flow Does Not Preserve the Cone

**The domain is a condition at each event and is not conserved by any of the corpus's flows except the Schrödinger one.** The Klein–Gordon flow does not preserve it because the equation is second order; the Dirac flow does not preserve it because the mass couples the two chiral pieces.

**The Klein–Gordon check.** With $\Xi_t(0,x)=0$ and $\partial_{t'}\Xi_t(0,x)$ a unit packet of width $2$, $k_m=1$, and a $1+1$ evolution on a periodic grid of $4000$ points spanning $60$ with step $10^{-4}$, the field starts on the cone and its maximum modulus is $0.0500$ at $t=0.05$ and $0.1983$ at $t=0.2$. So the field leaves the cone immediately and returns to it only at isolated events.

**The Dirac check.** A field carrying one chiral piece alone is on the cone; after evolution the modulus of the determinant rises from zero to $0.196$ at $t=0.2$ and $0.369$ at $t=0.4$, because the mass couples the pieces and a field carrying one piece alone does not keep one piece alone. [Why Biquaternions?](why-biquaternions.html) records the check.

**The Schrödinger flow is the exception and the reason is multiplicative.** That flow is left multiplication by a unit, so it preserves the norm exactly: $N(\tilde U\tilde\Xi)=N(\tilde U)N(\tilde\Xi)$ and $N(\tilde U)\neq0$. A cone preserved by a flow is a cone preserved by a group of units, and the relativistic flows are not of that kind.

**The consequence for the reading is that the chart is local in time as well as in space.** A field's word at one event says nothing about the word at a nearby event: the chart can fail between two events at which it exists. A fluid reading is therefore a family of chart patches and not a global chart.

## The Limits of the Reading

### The Non-Relativistic Limit

**The word degenerates to a scale, a phase and a sign, and the fluid to a Madelung fluid.** With the boost at $e_t$ and the rotor at $\varepsilon e_t$ the velocity is zero and the spin is the declared axis; the brackets reduce to the scale and the phase, and the equation to a continuity equation and a Hamilton–Jacobi equation with the quantum potential. That limit is a limit of the reading and not of the field: a slow field still has a spin, and the reading drops it because the rotor's angle has no effect on the remaining brackets.

**The limit's error is of order the velocity squared over $c^{2}$ and is not uniform in the spin angle.** A sector field at a small spin angle has a small velocity and the non-relativistic reading is accurate; the same field at a large spin angle has a large velocity and the reading fails. The limit is therefore not a limit in the field's amplitude but in its motion.

### Zitterbewegung

**The reading's bilinears run at twice the field's phase, and the doubling does not disappear in any limit.** The norm's argument is $2\theta_{\mathrm{pha}}$ and the current is built from the boost, so the fluid's own variables oscillate at the doubled rate. A fluid description that resolves the motion finer than $1/(2\omega)$ sees the doubling; one that averages over it sees the mean.

**The limit is a coarse-graining and its scale is the Compton frequency.** That is why the fluid reading is a description of the field at scales long compared with the Compton wavelength, and why its transport coefficients are the ones a coarse-grained theory has.

### Rotor Precession

**The spin's precession is a motion of the chart's fourth factor and it has no counterpart in the scale and phase.** A reading that used only the two central brackets would see a fluid with no spin; the rotor's precession would be invisible. So the third limit is that the reading is a reading of *all four* brackets or it is not the spin fluid.

**The three limits are the article's honest accounting.** The non-relativistic limit drops the spin; the coarse-graining drops the doubling; the central-only reading drops the precession. Each is a limit of the reading and none is a limit of the field.

## The Boundary

**No dynamics is added by anything in this article.** The domain is the set where the chart exists, the two families are fields that lie outside it, and the non-preservation is a property of flows already given. The article's statements are one theorem, one count, and a list of checks.

**What a reader should not conclude.** That the chart's failure is a failure of the theory. The field equation is defined on the whole algebra, and only the reading is not. A formulation that took the chart for the theory would have to add a condition excluding the cone, and no such condition is in the corpus.

**What a reader should conclude.** That the fluid reading is exact on the interior of the domain, that its boundary is populated, and that the population is physically named. That is the precise sense in which the reading is a chart.

## What Is Established and What Is Interpretation

**Established.** That the word exists exactly on the elements of nonzero norm. That the cone is a complex hypersurface of real codimension two, checked along all eight coordinate directions at a zero divisor. That it is a cone, checked at three scales. That the two families lie on it with non-vanishing density. That the scalar case's cone is the nodal set and the spinor case's is strictly larger. That the Klein–Gordon and Dirac flows do not preserve the cone, checked at two times each. That the Schrödinger flow does.

**Interpretation.** That the two families are the chiral fields and the one-sided massless waves and are therefore physical. That the two-factor decomposition is a fallback rather than a substitute. That the three limits are coarse-grainings. Each is argued here and none is proved.

**Not claimed.** It is not claimed that the cone's complement is connected; only the two families are exhibited. It is not claimed that the chart can be extended to the cone by any limiting procedure; the corpus has none. It is not claimed that the non-preservation is a difficulty for the theory; it is a difficulty for a reader who treats a chart as a field.

## Summary

The polar word exists exactly on the elements of nonzero quaternionic norm. The complement is the zero-divisor cone, a complex hypersurface of real codimension two, invariant under central scaling.

Two families of fields lie on the cone with a non-vanishing density: the elements of definite value, which are the chiral fields at any amplitude, and the one-sided plane waves with a null wavevector. For the scalar field the cone coincides with the nodal set; for the spinor field it is strictly larger.

What survives on the cone is the two-factor decomposition into a Hermitian factor and a partial isometry, which separates the scale from the direction and not the velocity from the spin.

The domain is a condition at each event. The Klein–Gordon flow and the Dirac flow do not preserve it, checked at two times each; only the Schrödinger flow, being left multiplication by a unit, does. The reading is therefore a family of chart patches, exact on the interior and populated on the boundary, and it adds no dynamics of its own.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $N(\tilde Q)=Q_t^{2}+\vec Q\cdot\vec Q$ | Quaternionic norm |
| $\Rho$ | Modulus, $\Rho^{2}=N$ |
| $\rho=r^{2}$ | Density |
| $\tilde X\vec e_z=\pm i\tilde X$ | Element of definite value |
| $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=0$ | Null wavevector |
| $\tilde\Xi=\tilde\Xi_{H}\tilde\Xi_{0}$ | Two-factor decomposition |
| $\tilde U_{\Psi,\mathrm b}$, $\tilde u_{\mathrm r}$ | Boost and rotor of the four-factor word |

## Further Reading

- David Hestenes, "Space–time structure of the Dirac theory," in *Clifford Algebras and their Applications in Mathematical Physics* (Reidel, 1986), for the spinor as a frame and the extent of the frame description.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, vol. 1 (Cambridge University Press, 1984), for the null flag and the two-component spinor as a degenerate direction.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), for the nodal set of the non-relativistic fluid and the limits of the reading.
- The companion articles: [The Relativistic Quantum Space as a Fluid](the-relativistic-quantum-space-as-a-fluid.html), [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html), [The Klein–Gordon Fluid](the-klein-gordon-fluid.html), [The Dirac Fluid and the Takabayasi Correspondence](the-dirac-fluid-and-the-takabayasi-correspondence.html), [Physical Interpretation of Spectral Regularity and Degeneracy in the Biquaternion Algebra](physical-interpretation-of-spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html).
