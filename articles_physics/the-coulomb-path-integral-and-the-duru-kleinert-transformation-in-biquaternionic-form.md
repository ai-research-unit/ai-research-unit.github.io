# __The Coulomb Path Integral and the Duru–Kleinert Transformation in Biquaternionic Form__

## Introduction

The path integral for the Coulomb problem — the hydrogen atom, a charge bound by the potential $V(r)=-\kappa/r$ — is the elementary case that the standard time-slicing construction does not reach. Feynman's short-time kernel presumes that the potential is bounded over the short interval between slices, and the $1/r$ singularity at the origin destroys that presumption: paths that pass near the origin give an action whose potential term diverges faster than the kinetic term can compensate, and the limit of the sliced integral does not exist as written. The remedy, found by Duru and Kleinert in 1979, is a transformation of the path integral in two parts: the physical time $t$ is replaced by a **path-dependent pseudo-time**, and the position is carried by a **coordinate transformation** that renders the transformed action harmonic, hence exactly integrable.

The corpus already owns the Coulomb problem on the operator side and the classical side. *The Hydrogen Atom in Biquaternionic Form — The Non-Relativistic Case* separates the Coulomb Hamiltonian in $\mathbb{M}_+$ and obtains the spectrum; *Coulomb Scattering and Rutherford's Formula in Biquaternionic Form* treats the unbound case; and *The Classical Coulomb Problem and Its Hidden SO(4) Symmetry in Biquaternionic Form* owns the classical degeneracy and its $\mathrm{SO}(4)$ algebra. Nothing in the corpus constructs the Coulomb path integral, and nothing mentions the pseudo-time or the Duru–Kleinert transformation. This article supplies that route and records what the algebra contributes to it.

The contribution is a reading, and it is a sharper one than the neighbouring path-integral articles.

- **Established (algebra).** The Coulomb potential $V(r)e_0=-(\kappa/r)e_0$ is a **central scalar**: a function of $r$ alone times the identity. The Coulomb problem is therefore a central-scalar configuration in the sense of *The Central Scalar Field: Classical Dynamics in the Biquaternion Center* and *The Central-Scalar Limit of Classical Mechanics in Biquaternionic Form*, and the whole of the algebra's sector structure — the split $\mathbb{M}_-\oplus\mathbb{M}_+$, the location of the phase, the trace pairing — is invisible to it. The singularity that defeats the time slicing is a singularity of a central scalar function, not of the algebra.
- **Established (algebra).** The coordinate transformation of Duru and Kleinert is the square root of the position in the quaternion algebra. In the Kustaanheimo–Stiefel (KS) coordinates $u\in\mathbb{R}^4$ the position satisfies $r=|\mathbf{x}|=N(u)$, the **quaternion norm** of $u$; the $1/r$ singularity is the inverse norm $1/N(u)$, and the pseudo-time $dt=r\,ds$ makes the potential term constant, $\int V\,dt=-\kappa\int ds$, while the kinetic term becomes the quadratic form $2m\int|\dot u|^2ds$. What remains, with the energy term $-\int E\,dt=-E\int N(u)\,ds$, is the harmonic form that the transformation is named for.
- **Established (algebra).** The pseudo-time is a monotone, path-dependent relabeling of the material time, along the same $ict$ axis on which the phase exponent of *The Path Integral in Biquaternionic Form* lies and along which *The Wick Rotation in the Biquaternion Universe* rotates. It is a relabeling of a coordinate and not a new dimension, and the algebra names the axis without supplying the reparametrisation.
- **Standard, and transcribed.** The Duru–Kleinert transformation itself, the choice of pseudo-time, the KS map, the reduction to the four-dimensional isotropic oscillator, and the use of the oscillator's Mehler kernel to obtain the Coulomb Green's function. The algebra supplies none of these.
- **Not supplied.** The functional measure and its transformation law under the coordinate change and the pseudo-time. The transformation is a change of the integration variable and of the measure, and the measure is the algebra's standing gap; the Jacobian of the transformation is exactly the object the algebra cannot write. The path integral's exact integrability is therefore imported whole.

The article proceeds as follows. A section states why the time slicing fails, in the framework's terms. A section defines the pseudo-time and derives its two consequences for the potential and the kinetic term. A section defines the KS transformation, exhibits the norm identity $r=N(u)$, and gives the reduction to the harmonic action. A section reads the transformation in the algebra and states the limit of the reading. A section separates what the algebra supplies from what it imports, and the article closes with open questions.

**Conventions.** We use those of the companion articles, in particular *The Path Integral in Biquaternionic Form* and *The Hydrogen Atom in Biquaternionic Form — The Non-Relativistic Case*. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, and central imaginary $i$. The material coordinate is $\tilde Q=ict\,e_0+\mathbf{x}$, with $\mathbf{x}=xe_1+ye_2+ze_3$ and $r=|\mathbf{x}|$; the $ict$ metric is $\eta=\mathrm{diag}(-1,+1,+1,+1)$ and the material sector is $\mathbb{M}_-=i\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B})_{\mathbb{R}}$. The Coulomb parameter is $\kappa=Ze^2/(4\pi\epsilon_0)$, the Hamiltonian is $\tilde H=\mathbf{p}^2/(2m)+\tilde V$ with $\tilde V=-(\kappa/r)e_0\in\mathbb{C}_{\mathbb{B}}$, and the bound-state energies are $E_n=-m\kappa^2/(2\hbar^2n^2)$. The real bilinear form is $\langle\tilde Q,\tilde Y\rangle=\mathrm{Re}\,\mathrm{Tr}(\tilde Q^\dagger\tilde Y)$ and the trace is $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$. The KS coordinates are written $u=(u_1,u_2,u_3,u_4)\in\mathbb{R}^4$, and the quaternion norm of the corresponding $u=u_1e_1+u_2e_2+u_3e_3+u_4e_0\in\mathbb{H}$ is $N(u)=\bar uu=\lvert\mathbf{u}\rvert^2$.

## Why the Time Slicing Fails

The construction of the kernel is the one of *The Path Integral in Biquaternionic Form*: divide the time $T$ into $N$ steps of length $\varepsilon=T/N$, use the short-time kernel
$$
K_\varepsilon(\mathbf{x}',\mathbf{x})=\Big(\frac{m}{2\pi i\hbar\varepsilon}\Big)^{3/2}
\exp\Big[\frac{i}{\hbar}\Big(\frac{m|\mathbf{x}'-\mathbf{x}|^2}{2\varepsilon}-\varepsilon\,V(\mathbf{x})\Big)\Big]+O(\varepsilon^2),
$$
and take the limit $N\to\infty$ of the product with the intermediate positions integrated.

**The failure.** For $V(\mathbf{x})=-\kappa/r$ the potential term is $+\kappa\varepsilon/r$ in the exponent, so for a path that passes within a distance $\lesssim\kappa\varepsilon/\hbar$ of the origin the phase is not small, and the expansion of the potential to first order in $\varepsilon$ — the step that produces the Schrödinger equation in *The Schrödinger Path Integral in Biquaternionic Form* — is not controlled. The Gaussian in the kinetic term has width $\sqrt{\hbar\varepsilon/m}$, so the slices that approach the origin are precisely the ones the kinetic term does not suppress, and the naive limit is not a well-defined kernel. This is the reason the source states that the time-sliced approximation "does not exist" for the Coulomb potential.

**The reading in the algebra is immediate, and it is negative.** The potential is $\tilde V(\mathbf{x})=-(\kappa/r)e_0$: a central scalar, whose value is a function of $r$ only, with no vector part and no dependence on the sector. The singularity is therefore a singularity of a **central scalar function** — of the real number $r$ — and nothing in the two-sector structure of $\mathbb{B}$ intervenes. The algebra neither causes the failure nor cures it: it is finite-dimensional and supplies no measure, no short-time kernel, and no slicing. The failure is analytic, in the real configuration space, and the remedy below is analytic too, with the algebra entering only in the reading of the coordinate transformation and the axis of the pseudo-time.

## The Pseudo-Time

The first half of the Duru–Kleinert transformation is a reparametrisation of the time. Replace the physical time $t$ by a **pseudo-time** $s$, path-dependent, according to
$$
dt=r(s)\,ds ,
\qquad\text{equivalently}\qquad
ds=\frac{dt}{r(t)} ,
$$
so that the pseudo-time is the integral of the inverse radius along the trajectory. The transformation is monotone along any trajectory that does not reach the origin, and it is defined where the path integral is; the origin, which the physical slicing could not handle, is where the pseudo-time flow is singular and where the transformed problem is regular, because the two singularities are reciprocal.

Two consequences follow by direct substitution.

**The potential becomes a constant.** The time integral of the Coulomb potential is
$$
\int V\,dt=-\kappa\int\frac{1}{r}\,dt=-\kappa\int\frac{1}{r}\,r\,ds=-\kappa\int ds ,
$$
a term linear in the pseudo-time and with no $1/r$. The singularity that defeated the slicing has been absorbed by the reparametrisation: it was the coefficient of the potential, and the pseudo-time was chosen to cancel it.

**The kinetic term becomes a quadratic form in the new coordinate.** Writing $\dot{\mathbf{x}}=d\mathbf{x}/dt$ and $d\mathbf{x}/ds=\dot{\mathbf{x}}\,(dt/ds)=\dot{\mathbf{x}}\,r$,
$$
\frac{m}{2}\int|\dot{\mathbf{x}}|^2dt
=\frac{m}{2}\int\Big|\frac{d\mathbf{x}}{ds}\Big|^2\frac{1}{r^2}\,r\,ds
=\frac{m}{2}\int\Big|\frac{d\mathbf{x}}{ds}\Big|^2\frac{1}{r}\,ds ,
$$
which still carries an inverse radius in the measure of the new coordinate. The second ingredient removes it.

**The reparametrisation is along the material time axis.** In the framework's coordinates the physical time enters the material coordinate as the coefficient $ict$, so the substitution $dt=r(s)\,ds$ is a path-dependent relabeling of the $ict$ direction — the same axis on which the phase exponent $iS/\hbar$ of *The Path Integral in Biquaternionic Form* lies, and the same axis whose relabeling as real is the Wick rotation of *The Wick Rotation in the Biquaternion Universe*. The pseudo-time is not a new dimension and not a new field; it is a reparametrisation of the one time the framework has, and the algebra names the axis without supplying the function $r(s)$. In this it is the closest analogue, on the configuration-space side, of the $i\epsilon$ of the propagator: the same $ict$ direction, carrying the analyticity that makes the integral converge.

## The Duru–Kleinert Transformation and the Harmonic Form

### The Kustaanheimo–Stiefel Coordinates

The second half is the coordinate transformation. Carry the three-dimensional position $\mathbf{x}$ by four coordinates $u=(u_1,u_2,u_3,u_4)$ through the **Kustaanheimo–Stiefel map**
$$
x_1=2(u_1u_3-u_2u_4),\qquad
x_2=2(u_1u_4+u_2u_3),\qquad
x_3=u_1^2+u_2^2-u_3^2-u_4^2 ,
$$
so that $\mathbf{x}=(x_1,x_2,x_3)$ is the image of $u\in\mathbb{R}^4$. The map is surjective onto $\mathbb{R}^3$ and two-to-one away from the origin.

**The norm identity, and the quaternion reading.** A direct expansion gives
$$
r=|\mathbf{x}|=u_1^2+u_2^2+u_3^2+u_4^2=|\mathbf{u}|^2=N(u),
$$
where $u=u_1e_1+u_2e_2+u_3e_3+u_4e_0\in\mathbb{H}$ and $N(u)=\bar uu$ is the quaternion (hence the biquaternion, with real coefficients) norm. The identity was checked numerically on random $u$ and holds to machine precision. Its differential companion is the statement that the map is a Riemannian submersion with one gauge direction: the Jacobian $J=\partial\mathbf{x}/\partial u$ satisfies
$$
J^{\mathsf T}J=4N(u)\big(I-\hat n\hat n^{\mathsf T}\big),
\qquad
\hat n\propto(u_2,-u_1,-u_4,u_3),
$$
with three eigenvalues equal to $4N(u)$ and one null direction. The null direction is the gauge direction of the two-to-one map — the **KS constraint** is $u_2\,du_1-u_1\,du_2-u_4\,du_3+u_3\,du_4=0$ — and on the constraint surface the induced metric of the physical three-space is conformal,
$$
\big|d\mathbf{x}\big|^2=4N(u)\,\big|du\big|^2 .
$$
This was checked numerically on random $u$: the eigenvalues of $J^{\mathsf T}J$ are $0,4N(u),4N(u),4N(u)$ to machine precision, and the kernel direction is proportional to $(u_2,-u_1,-u_4,u_3)$. The conformal identity is the one the kinetic term needs, and it holds precisely where the physical configuration space lies, on the constraint.

**The algebraic reading is that the KS map is a square root of the position.** The relation $r=N(u)$ says that the Euclidean radius, and with it the coordinate $\mathbf{x}$ up to the map's internal $O(4)$ freedom, is the **norm of a quaternion**; the map takes a square root of the position in the algebra. This is not an analogy: $N(u)=\bar uu$ is the algebra's own norm, and the identity says that the Coulomb singularity $1/r$ is $1/N(u)$, the reciprocal of the norm. The degeneracy that the map's internal $O(4)$ records — two values of $u$ for each $\mathbf{x}$, and the $\mathrm{SO}(4)$ of *The Classical Coulomb Problem and Its Hidden SO(4) Symmetry in Biquaternionic Form* — is the algebraic statement that the Coulomb problem has a square root, and that the square root carries a four-dimensional rotation symmetry the position does not.

### The Transformed Action

Substitute both transformations into the action. The kinetic term, using the conformal identity $|d\mathbf{x}|^2=4N(u)|du|^2$ on the KS constraint and the extra factor $1/r=1/N(u)$ from the pseudo-time, becomes
$$
\frac{m}{2}\int\Big|\frac{d\mathbf{x}}{ds}\Big|^2\frac{1}{r}\,ds
=\frac{m}{2}\int 4N(u)\Big|\frac{du}{ds}\Big|^2\frac{1}{N(u)}\,ds
=2m\int\Big|\frac{du}{ds}\Big|^2ds ,
$$
a free quadratic form in the four KS coordinates, with the inverse norm cancelled exactly. The potential term is the constant $-\kappa\int ds$ of the previous section. The fixed-energy term of the Jacobi action contributes $-\int E\,dt=-E\int N(u)\,ds$, which is quadratic in $u$ and, for a bound state $E<0$, supplies the harmonic potential. Collecting the three,
$$
S\;\longrightarrow\;\int ds\;\Big[\,2m\Big|\frac{du}{ds}\Big|^2-E\,N(u)-\kappa\,\Big],
$$
which is the action of an **isotropic harmonic oscillator in four dimensions**, with the energy-dependent coefficient of $N(u)=|u|^2$ playing the role of the oscillator's restoring term. That the transformed action is harmonic, and that the fixed-energy problem is thereby exactly integrable, is the content of the Duru–Kleinert transformation.

**The reduction is standard, and is transcribed here.** The transformation, the choice $dt=r\,ds$, the KS map, the reduction to the four-dimensional oscillator, and the conclusion that the Coulomb Green's function is obtained from the oscillator's Mehler kernel are the standard results of Duru and Kleinert and of Kleinert's treatise; they are not re-derived. What is recomputed here is only the algebra of the reduction: the norm identity $r=N(u)$, its differential companion $J^{\mathsf T}J=4N(u)(I-\hat n\hat n^{\mathsf T})$ with the constraint direction $\hat n\propto(u_2,-u_1,-u_4,u_3)$ (both checked numerically), and the cancellation of the inverse norm between the kinetic term and the pseudo-time Jacobian. The full kernel — the energy spectrum, the degeneracy $n^2$, and the wave functions — is the subject of the hydrogen articles, which obtain it on the operator side, and the value of the path-integral route is that it reaches the same spectrum through the oscillator, whose kernel the corpus owns in *The Harmonic Oscillator in Biquaternionic Form*.

**Why the harmonic form is the point.** The oscillator is the one nontrivial kernel that is exactly known and exactly integrable, and the transformation arranges that the singular problem be equivalent to it. In the algebra's reading the two facts line up: the pseudotime makes the potential constant because the potential was the inverse norm, and the coordinate transformation makes the kinetic term the norm's quadratic form because the transformation is the square root. The harmonic oscillator's centrality in the catalogue — the harmonic form is the one the algebra's own $SU(2)$ and rotor structure generates — is what makes the reduction natural, though the reduction is not derived from the algebra.

## What the Algebra Supplies, What It Imports, What It Does Not Supply

**Supplied by the algebra, and recomputed here.** The identification of the Coulomb potential as a **central scalar**, $V(r)e_0\in\mathbb{C}_{\mathbb{B}}$, so that the problem is a central-scalar configuration and the sector structure is invisible to it; the reading of the KS map as the **square root of the position in the quaternion algebra**, with the identity $r=N(u)$ and its differential companion $|d\mathbf{x}|^2=4N(u)|du|^2$ derived and checked; the identification of the Coulomb singularity $1/r=1/N(u)$ as the reciprocal of the algebra's norm; and the reading of the pseudo-time as a path-dependent relabeling of the $ict$ axis, the same axis as the phase exponent and the Wick rotation. These are the algebra's genuine contributions, and they are readings, not computations of the kernel.

**Imported, and left visible.** The Duru–Kleinert transformation and the choice of pseudo-time; the Kustaanheimo–Stiefel map and its surjectivity and two-to-oneness; the reduction to the four-dimensional isotropic oscillator; the Mehler kernel; the fixed-energy (Jacobi) formulation; and the extraction of the Coulomb Green's function and its spectrum from the oscillator. The analytic apparatus of the transformation is standard and is not rebuilt; the spectrum obtained by this route is the same one the hydrogen article obtains by separation, and the agreement is cited rather than re-derived.

**Not supplied.** The functional measure and its transformation law. The Duru–Kleinert transformation is a change of the integration variable — time-dependent, path-dependent, and nonlinear in the coordinate — and a change of variable in a functional integral brings a Jacobian, which is the object that makes the transformation exact and which the algebra cannot write. The measure and its Jacobian are the algebra's standing gap, the same one *The Functional Integral in Biquaternionic Form* records and *The Path Integral in Biquaternionic Form* inherits; the Coulomb path integral is the case where the gap is sharpest, because there the transformation's content is precisely the Jacobian that the algebra does not carry. Also not supplied is any empirical content; the transformation is a method, not a prediction.

## Open Questions

1. **The Jacobian of the Duru–Kleinert transformation in the algebra.** The transformation is exact because the pseudo-time and the coordinate change have a definite Jacobian, which is the measure-theoretic factor that *The Path Integral in Biquaternionic Form* names in the curved-space case. Can the Jacobian be written as the trace of an algebra element, in the way the Gaussian determinant is the trace of the kinetic operator, so that the transformation's content is algebraic rather than analytic?

2. **The square root as an element of the algebra.** The KS map takes a square root of the position: $r=N(u)$, with $\mathbf{x}$ recovered from $u$ up to an $O(4)$ frame. Is there a biquaternion element $\tilde U$ with $N(\tilde U)=\tilde Q$ for the material coordinate $\tilde Q=ict\,e_0+\mathbf{x}$, i.e. a square root in the full algebra rather than only in the spatial quaternion, and does the Coulomb problem's hidden $\mathrm{SO}(4)$ act on the space of such roots?

3. **The pseudo-time and the propagator's $i\epsilon$.** The pseudo-time lies along the same $ict$ axis as the propagator's deformation and the phase exponent. Is the pseudo-time's reciprocality — the potential's singularity becoming the pseudo-time's singularity — the configuration-space form of the momentum-space $i\epsilon$ prescription, and can the two be exhibited as one deformation of the $ict$ line?

4. **The oscillator's energy-dependent frequency and the framework's oscillator.** The transformed problem is a four-dimensional oscillator with an energy-dependent restoring term. The framework's own oscillator, *The Harmonic Oscillator in Biquaternionic Form*, has a fixed central frequency and a two-sector structure. Does the energy-dependent frequency of the transformed problem have a reading in the framework's oscillator, and does the four-dimensional character of the KS oscillator have any relation to the four real dimensions of a sector?

5. **The relativistic Coulomb path integral.** The Dirac and Klein–Gordon hydrogen problems have their own path integrals, with a different pseudo-time and a different (super)symmetry. The framework's relativistic hydrogen article is operator-based; is there a Duru–Kleinert-type transformation for it, and does the algebra's spinor module enter where the non-relativistic spatial quaternion entered?

6. **Empirical content.** As everywhere, the transformation is a method for computing a spectrum the framework already obtains. Whether the biquaternion reading of the square root imposes any constraint that the standard transformation does not is not established here.

## Summary

The Coulomb path integral is the elementary problem that Feynman's time slicing does not reach: the $1/r$ singularity at the origin makes the sliced integral, whose short-time kernel presumes a bounded potential, fail to converge. The Duru–Kleinert transformation removes the singularity in two parts. First, the physical time is replaced by a path-dependent pseudo-time,
$$
dt=r\,ds ,
$$
which makes the potential term constant, $\int V\,dt=-\kappa\int ds$, and leaves the kinetic term carrying an inverse radius, $\tfrac{m}{2}\int|\dot{\mathbf{x}}|^2dt=\tfrac{m}{2}\int|d\mathbf{x}/ds|^2(1/r)\,ds$. Second, the position is carried by the Kustaanheimo–Stiefel coordinates $u\in\mathbb{R}^4$, under which
$$
r=|\mathbf{x}|=N(u),\qquad J^{\mathsf T}J=4N(u)\big(I-\hat n\hat n^{\mathsf T}\big),
$$
so that on the KS constraint $\big|d\mathbf{x}\big|^2=4N(u)\big|du\big|^2$ and the inverse norm cancels. With the fixed-energy term $-\int E\,dt=-E\int N(u)\,ds$ the transformed action is
$$
S\;\longrightarrow\;\int ds\;\Big[\,2m\Big|\frac{du}{ds}\Big|^2-E\,N(u)-\kappa\,\Big],
$$
the action of a four-dimensional isotropic harmonic oscillator, whose Mehler kernel yields the Coulomb Green's function and the spectrum $E_n=-m\kappa^2/(2\hbar^2n^2)$ with the degeneracy $n^2$.

The algebra's contribution is a reading. The Coulomb potential is a **central scalar** $V(r)e_0$, so the problem is a central-scalar configuration and the sector structure plays no part. The KS transformation is the **square root of the position in the quaternion algebra**: the radius is the algebra's norm, $r=N(u)$, and the Coulomb singularity is $1/N(u)$, the reciprocal of that norm. The pseudo-time is a path-dependent relabeling of the **material time axis**, the same $ict$ direction as the phase exponent of the path-integral article and the Wick rotation. What the algebra does **not** supply is the transformation itself, the choice of pseudo-time, the KS map's detailed form, the reduction to the oscillator, the Mehler kernel — or the functional measure and its Jacobian, which is the object that makes the transformation exact and is the algebra's standing gap. The path-integral route reaches the spectrum the hydrogen article reaches by separation, and the algebra names why the route is natural — the potential is an inverse norm and the transformation is a square root — without deriving it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $\tilde Q=ict\,e_0+\mathbf{x}$ | Material coordinate; $r=\lvert\mathbf{x}\rvert$ |
| $\kappa=Ze^2/(4\pi\epsilon_0)$ | Coulomb parameter |
| $\tilde V=-(\kappa/r)e_0\in\mathbb{C}_{\mathbb{B}}$ | Coulomb potential; a central scalar |
| $E_n=-m\kappa^2/(2\hbar^2n^2)$ | Bound-state spectrum (from the hydrogen article) |
| $dt=r\,ds$, $ds=dt/r$ | Duru–Kleinert pseudo-time; path-dependent, along $ict$ |
| $u=(u_1,u_2,u_3,u_4)\in\mathbb{R}^4$ | Kustaanheimo–Stiefel coordinates |
| $u=u_1e_1+u_2e_2+u_3e_3+u_4e_0\in\mathbb{H}$ | The quaternion carried by $u$ |
| $N(u)=\bar uu=\lvert\mathbf{u}\rvert^2$ | Quaternion norm; equals $r$ |
| $x_1,x_2,x_3$ in terms of $u$ | The Kustaanheimo–Stiefel map; $u\mapsto\mathbf{x}$ |
| $J^{\mathsf T}J=4N(u)(I-\hat n\hat n^{\mathsf T})$, $\hat n\propto(u_2,-u_1,-u_4,u_3)$ | Riemannian submersion; one gauge direction |
| $u_2\,du_1-u_1\,du_2-u_4\,du_3+u_3\,du_4=0$ | KS constraint; the null (gauge) direction of the submersion |
| $S\to\int ds\,[\,2m\lvert du/ds\rvert^2-E N(u)-\kappa\,]$ | Transformed action; four-dimensional isotropic oscillator |
| $\mathcal{D}\mathbf{x}$, $r\,ds$ | Measures; the transformation's Jacobian is not supplied by the algebra |

## Further Reading

- İ. H. Duru and H. Kleinert, "Solution of the path integral for the H-atom," *Physics Letters B* **84** (1979) 185–188, for the pseudo-time transformation and the reduction of the Coulomb path integral to the oscillator.
- İ. H. Duru and H. Kleinert, "Quantum mechanics of H-atom from path integrals," *Fortschritte der Physik* **30** (1982) 401–435, for the full treatment.
- H. Kleinert, *Path Integrals in Quantum Mechanics, Statistics, Polymer Physics, and Financial Markets* (World Scientific, 2009), for the Kustaanheimo–Stiefel transformation, the pseudo-time, and the harmonic reduction in textbook form.
- P. Kustaanheimo and E. Stiefel, "Perturbation theory of Kepler motion based on spinor regularization," *Journal für die reine und angewandte Mathematik* **218** (1965) 204–219, for the original KS transformation and the regularization of the Kepler singularity.
- V. Fock, "Zur Theorie des Wasserstoffatoms," *Zeitschrift für Physik* **98** (1935) 145–154, for the four-dimensional oscillator and the $\mathrm{SO}(4)$ symmetry of the hydrogen atom.
- L. S. Schulman, *Techniques and Applications of Path Integration* (Wiley, 1981), for the time slicing, the singular potentials, and the curved-space measure.
- R. P. Feynman and A. R. Hibbs, *Quantum Mechanics and Path Integrals* (McGraw-Hill, 1965), for the short-time kernel and the time-slicing construction.
- Companion articles: *The Path Integral in Biquaternionic Form*, for the phase, the time slicing, the central imaginary, and the measure gap; *The Schrödinger Path Integral in Biquaternionic Form*, for the derivation of the Schrödinger equation from the sliced kernel; *The Wick Rotation in the Biquaternion Universe*, for the $ict$ axis and its relabeling; *The Harmonic Oscillator in Biquaternionic Form*, for the oscillator whose kernel the transformed problem uses; *The Hydrogen Atom in Biquaternionic Form — The Non-Relativistic Case*, for the spectrum and the eigenstates obtained by separation; *The Classical Coulomb Problem and Its Hidden SO(4) Symmetry in Biquaternionic Form*, for the classical degeneracy and the $O(4)$ internal freedom of the square root; *Coulomb Scattering and Rutherford's Formula in Biquaternionic Form*, for the unbound case; *The Central Scalar Field: Classical Dynamics in the Biquaternion Center* and *The Central-Scalar Limit of Classical Mechanics in Biquaternionic Form*, for the central-scalar configuration; *The Functional Integral in Biquaternionic Form*, for the measure and its gap.
