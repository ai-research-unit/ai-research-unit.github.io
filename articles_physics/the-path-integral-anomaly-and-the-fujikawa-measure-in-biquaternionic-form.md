# __The Path-Integral Anomaly and the Fujikawa Measure in Biquaternionic Form__

## Introduction

**The object.** A classical symmetry can fail after quantisation. The classical current is conserved by the equations of motion; the one-loop diagram that computes its divergence is not zero; and the discrepancy is finite and unrenormalised. The **Fujikawa method** derives that failure from the path integral rather than from a diagram: the fermion measure is not invariant under the symmetry, the rotation of integration variables has a Jacobian, and the logarithm of that Jacobian is the anomaly.

**What this article is.** The general derivation, with no sector attached. It states the Jacobian, its regulated evaluation, the coefficient, and the index relation. Two anomalies exist and they play opposite roles: the chiral anomaly, which breaks a symmetry that the classical action has, and the gauge anomaly, which would break the symmetry that makes the theory consistent. Both are read off the same determinant, and both are stated here in general form.

**Where the applications are.** An anomaly is a property of whatever fermions circulate and of whatever representation they carry, so the application is always a sector calculation, and this category has one:

- The electroweak sector, where the fifteen fields of a generation sit in chiral representations and the four conditions $\sum Y=0$, $\sum Y^3=0$, $\sum YT_3^2=0$ and $\sum_{\mathrm{colour}}Y=0$ are the statement that the gauge anomaly cancels. The application is [Anomalies and Anomaly Cancellation: Four Conditions Become None](anomalies-and-anomaly-cancellation.html), which verifies all four generation by generation.
- The strong sector, where the same axial current is broken by the same mechanism and the survivor is the flavour-singlet current. The application is [The Theta Parameter and Strong CP in Biquaternionic Form](the-theta-parameter-and-strong-cp-in-biquaternionic-form.html), which uses the density this derivation produces.

## The Measure and the Chiral Rotation

The fermion path integral integrates over $Ξ_{\mathrm{wfn}}$ and $\barΞ_{\mathrm{wfn}}$ with a measure written formally as a product of coefficients in a complete basis,

$$
\mathcal{D}\barΞ_{\mathrm{wfn}}\,\mathcal{D}Ξ_{\mathrm{wfn}}=\prod_n da_n\,d\bar b_n .
$$

**The rotation.** A chiral rotation with constant parameter $\alpha$ acts on the fields by $Ξ_{\mathrm{wfn}}\mapsto e^{i\alpha\gamma_5}Ξ_{\mathrm{wfn}}$. In the basis the same rotation acts on the coefficients, so if the measure were invariant the transformation would be a symmetry of the integral.

**The Jacobian.** It is not. The rotation is a linear change of variables whose Jacobian is a formal determinant,

$$
\boxed{\;\mathcal{D}\barΞ_{\mathrm{wfn}}\,\mathcal{D}Ξ_{\mathrm{wfn}}\;\longmapsto\;\mathcal{D}\barΞ_{\mathrm{wfn}}\,\mathcal{D}Ξ_{\mathrm{wfn}}\;\exp\!\left(-2i\alpha\int d^4x\ \mathcal{A}(x)\right)\;}
$$

so the anomaly density $\mathcal{A}$ is the Jacobian per unit rotation angle. A determinant of an infinite matrix is not a number until it is regulated, and the whole content of the method is in how the regulation respects the symmetry it is measuring.

## The Regulated Trace

**The regulated determinant.** Regulate with a Hermitian operator whose eigenfunctions form the basis, and write the Jacobian as a trace:

$$
\mathcal{A}(x)=\lim_{M\to\infty}\sum_n\omicron_{\mathrm{pot},n}^{*}(x)\gamma_5\,\omicron_{\mathrm{pot},n}(x)\,e^{-\eta_n^2/M^2}
=\lim_{M\to\infty}\mathrm{Tr}\left(\gamma_5\,e^{\not D^2/M^2}\right)_{xx}.
$$

**The evaluation.** The heat kernel of $\not D^2$ is known to second order, and the trace over Dirac indices of $\gamma_5$ times the identity vanishes while the second-order term does not. The surviving term is proportional to the field strength contracted with its dual:

$$
\boxed{\;\partial_{\imath} j_{5,\imath}=\frac{1}{16\pi^2}\,\mathrm{Tr}\!\left(F_{\imath\jmath}\tilde F_{\imath\jmath}\right),
\qquad
\tilde F_{\imath\jmath}=\tfrac12\epsilon_{\imath\jmath\rho\sigma}F_{\rho\sigma}\;}
$$

with the trace over the gauge representation. The numerical coefficient is fixed by the heat-kernel expansion and by the dimension of the representation; no diagram is drawn, and no loop integral is performed.

**What the regulator must preserve.** The regulation must preserve the gauge symmetry while not preserving the chiral one; a regulator that preserved both would give zero and would be measuring the wrong thing. The choice is therefore a statement about which symmetry is being probed, and it is the reason the method gives the anomaly of the current that is actually broken.

**The index relation.** Integrating the density over a closed manifold relates the anomaly to the index of the Dirac operator,

$$
\int d^4x\ \partial_{\imath} j_{5,\imath}=\frac{1}{8\pi^2}\int\mathrm{Tr}\left(F\wedge F\right)=2\,n,
$$

so the change in the fermion number under a chiral rotation is an integer, and the anomaly is the local form of an index theorem. The same total derivative that makes the topological charge an integer makes the anomaly exact.

## What the Framework Supplies

The algebra enters at two points, and neither is the coefficient.

- **Supplied.** The chiral structure of the framework's spinor module, which fixes which current is axial, and the identification of the trace with twice the scalar part, $2\,\mathrm{Sc}=\operatorname{tr}$, whenever the representation is the algebra's own.
- **Imported.** The path-integral measure, the heat-kernel expansion, the regulator and the coefficient. These are standard field theory, transcribed.
- **Not supplied.** A spectrum. This article names no multiplet; which fermions circulate, and in which representation, is the sector's business.

**Where the applications are.** [Anomalies and Anomaly Cancellation: Four Conditions Become None](anomalies-and-anomaly-cancellation.html) applies the general coefficient to the electroweak spectrum and checks the four cancellation conditions. [The Theta Parameter and Strong CP in Biquaternionic Form](the-theta-parameter-and-strong-cp-in-biquaternionic-form.html) uses the density in the strong sector, where the broken current is the flavour-singlet axial one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha$ | the chiral rotation angle |
| $\mathcal{A}(x)$ | the anomaly density, the Jacobian per unit angle |
| $\eta_n$, $\omicron_{\mathrm{pot},n}$ | eigenvalues and eigenfunctions of the regulating operator |
| $M$ | the regulator mass |
| $\tilde F_{\imath\jmath}$ | the dual field strength |
| $n$ | the topological charge, an integer |

## Further Reading

- K. Fujikawa, "Path-Integral Measure for Gauge-Invariant Fermion Theories," *Physical Review Letters* **42** (1979) 1195–1198, the method.
- K. Fujikawa, "Path Integral for Gauge Theories with Fermions," *Physical Review D* **21** (1980) 2848, the coefficient.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory*, Chapter 19, for the diagrammatic comparison.
