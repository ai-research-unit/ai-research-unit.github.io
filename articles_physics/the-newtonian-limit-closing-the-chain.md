# __The Newtonian Limit: Closing the Chain__

## Introduction

The preceding article fixed the source: the derivative of a matter action with respect to the frame is a symmetric rank-two array, and the dictionary that produces it was verified to one part in $10^{10}$. This article runs that source the rest of the way, through the transcribed field equation, to the one place where the framework's gravity can be checked against the oldest measurement in physics.

The chain has four links and one break, and the break is at the front.

$$
\underbrace{\rho}_{\text{a density}}\;\longrightarrow\;\underbrace{\bar h_{00}=\frac{4GM}{c^{2}r}}_{\text{the transcribed equation}}\;\longrightarrow\;\underbrace{g_{00}=-\left(1-\frac{r_{s}}{r}\right)}_{\text{trace reversal}}\;\longrightarrow\;\underbrace{\Phi=-\frac{GM}{r}}_{\text{the interval}}\;\longrightarrow\;\underbrace{\ddot{\vec r}=-\nabla\Phi}_{\text{free fall}}
$$

Everything from the first arrow onward is computed here and is standard. The break is the arrow's *source*: the equation $\Box_{\Phi}\bar h_{\imath\jmath}=-\tfrac{16\pi G}{c^{4}}T_{\imath\jmath}$ is transcribed into the framework's letters, not derived from an algebra action, and no article of the corpus claims otherwise. The word "closing" in this article's title refers to the chain, and not to that break.

Three results, and they are of three different strengths.

**The chain runs, and its output is the observed potential.** A static density $\rho$ produces $\bar h_{00}=4GM/(c^{2}r)$, the trace reversal turns that into $h_{00}=r_{s}/r$, the interval becomes $g_{00}=-(1-r_{s}/r)$, and the potential read off it is $\Phi=-GM/r$ with $r_{s}=2GM/c^{2}$. The constant $16\pi G/c^{4}$ is not chosen: it is what makes the chain end at the measured $G$.

**The spatial part is fixed by the same step, and it is $\gamma=1$.** The trace reversal is a single operation applied once, and it gives $h_{ij}=(r_{s}/r)\delta_{ij}$ with no further choice. The parameter $\gamma$ of the parametrised post-Newtonian form is therefore *one*, which is general relativity's value, and it is a consequence of the transcribed equation rather than a separate posit. This is the sharpest available statement of the framework's empirical equivalence in the static weak field.

**Matter falls with the potential it produced.** The potential in $g_{00}$ is the potential in the geodesic equation, and the two are the same function because they are the same component of the same array. The chain therefore closes on itself: a density sources $\Phi$ and a test mass responds to $\Phi$ with $\ddot{\vec r}=-\nabla\Phi$. That self-consistency is what makes the Newtonian limit a *test* of the framework rather than a restatement of it, and it is what a theory with two independent halves — a source side and a response side — has to demonstrate.

**What is not established is repeated at the end, not softened.** The chain closes given the equation. The equation is not derived. The non-linear completion is not reached. The cosmological constant has no reading here. None of those absences is repaired by anything below.

## Conventions

The conventions are the gravity articles' and none is redefined, and the two that matter are stated in full because every sign below depends on them.

**The coordinates.** The material coordinates are $x_{\imath}=(r'_{t},r_x,r_y,r_z)$, the time coordinate in metres, $r'_{t}=ct$. The interval's array is $\digamma_{\mathrm{met}}=\mathrm{diag}(-1,1,1,1)$, its one minus on the time slot being the square of the $i$ in $e_0=ie_t$.

**The operators.** The biquaternionic d'Alembertian read in the material coordinates is

$$
\Box_{\Phi}=-\frac{\partial^{2}}{\partial {r'_{t}}^{2}}+\frac{\partial^{2}}{\partial r_x^{2}}+\frac{\partial^{2}}{\partial r_y^{2}}+\frac{\partial^{2}}{\partial r_z^{2}},
$$

which is the corpus's $\Box_{\Phi}=\tilde\nabla_{\Phi}(\tilde\nabla_{\Phi})^{\natural}$ written out, with the sign of the time term the square of the $i$ in $\partial/\partial R_t=-i\,\partial/\partial r'_{t}$ multiplied by the $i$ of the basis. In the static problem it reduces to the three-dimensional Laplacian $\Delta_{\Phi}$.

The frame, the metric, the inverse $G_{\imath\jmath}$, the dual frame $\tilde F_{\Phi,\imath}$ and the volume density $\sqrt{|g|}$ are those of the preceding article. The perturbation is $h_{\imath\jmath}$ with $|h_{\imath\jmath}|\ll1$, its trace is $h=\sum_{\imath}\digamma_{\imath\imath}h_{\imath\imath}=-h_{00}+h_{11}+h_{22}+h_{33}$, and the trace-reversed variable is $\bar h_{\imath\jmath}=h_{\imath\jmath}-\tfrac12\digamma_{\imath\jmath}h$. Two identities of that variable are used and both are checked below: $\bar h=-h$, and its inverse $h_{\imath\jmath}=\bar h_{\imath\jmath}-\tfrac12\digamma_{\imath\jmath}\bar h$.

The gravitational constant enters once, through $\kappa^{2}=16\pi G/c^{4}$, and $r_{s}=2GM/c^{2}$ is the length the chain produces.

## The Source in the Static Weak Field

**The source.** A static, non-relativistic distribution of matter has one component that matters: the energy density. In the frame letters, $T_{00}=\rho c^{2}$, where $\rho$ is the mass density, and every other component is smaller than $T_{00}$ by at least one power of $v/c$ or is zero. This is the standard Newtonian truncation, and it is where the corpus's transcription begins.

**The equation.** The corpus's linearised equation, as written in *Linearized Gravity in Biquaternionic Form* and used again in *Gravitational Waves in Biquaternionic Form*, is

$$
\Box_{\Phi}\bar h_{\imath\jmath}=-\frac{16\pi G}{c^{4}}\,T_{\imath\jmath}
$$

in the harmonic fixing condition, where $\mathcal G_{\imath\jmath}=-\tfrac12\Box_{\Phi}\bar h_{\imath\jmath}$ is the linearised Einstein tensor of the array $h_{\imath\jmath}$ and $G$ is Newton's constant. Static fields have no time dependence, so $\Box_{\Phi}\to\Delta_{\Phi}$ and the time-time entry is a Poisson equation,

$$
\Delta_{\Phi}\bar h_{00}=-\frac{16\pi G}{c^{4}}\,\rho c^{2}=-\frac{16\pi G}{c^{2}}\,\rho .
$$

**The solution.** With $\Delta_{\Phi}(1/r)=-4\pi\delta^{(3)}(\vec r)$ and a point mass $M$ at the origin, the solution vanishing at infinity is

$$
\bar h_{00}=\frac{16\pi G}{c^{2}}\,M\cdot\frac{1}{4\pi r}=\frac{4GM}{c^{2}r}=\frac{2r_{s}}{r}.
$$

**The trace reversal.** Only $\bar h_{00}$ is nonzero at this order, so $\bar h=\digamma_{00}\bar h_{00}=-\bar h_{00}=-2r_{s}/r$, and the inverse transformation gives

$$
h_{00}=\bar h_{00}-\tfrac12\digamma_{00}\bar h=\frac{2r_{s}}{r}-\tfrac12(-1)\left(-\frac{2r_{s}}{r}\right)=\frac{2r_{s}}{r}-\frac{r_{s}}{r}=\frac{r_{s}}{r},
$$

$$
h_{ij}=\bar h_{ij}-\tfrac12\digamma_{ij}\bar h=0-\tfrac12(+1)\left(-\frac{2r_{s}}{r}\right)=+\frac{r_{s}}{r}\qquad(i=j\in\{x,y,z\}),
$$

the spatial entry being the same arithmetic with $\digamma_{ij}=+1$ and the opposite overall sign, and the off-diagonal entries zero because $\bar h_{ij}$ vanishes off the diagonal at this order.

**The interval and the potential.** Adding the perturbation to the flat array,

$$
g_{00}=-1+\frac{r_{s}}{r}=-\left(1-\frac{r_{s}}{r}\right),
\qquad
g_{ij}=\left(1+\frac{r_{s}}{r}\right)\delta_{ij}.
$$

Comparing with the Newtonian form $g_{00}=-(1+2\Phi/c^{2})$,

$$
\frac{2\Phi}{c^{2}}=-\frac{r_{s}}{r}=-\frac{2GM}{c^{2}r}
\qquad\Longrightarrow\qquad
\Phi=-\frac{GM}{r}.
$$

The chain ends on Newton's potential, and nothing was inserted between the density and the potential except the transcribed equation and one trace reversal.

**The count of what was needed.** One equation, one source component, one trace reversal, one identification. Three of the four are arithmetic. The equation is the imported input, and it is the only imported input.

## The Constant Is Calibrated, Not Chosen

The coefficient $\kappa^{2}=16\pi G/c^{4}$ deserves separate treatment, because it is the one place where a number enters and because the corpus is repeatedly asked where it comes from.

**It is fixed by the chain.** Carry $\kappa^{2}$ through as an unknown. The Poisson equation becomes $\Delta_{\Phi}\bar h_{00}=-\kappa^{2}\rho c^{2}$, whose solution is $\bar h_{00}=\kappa^{2}Mc^{2}/(4\pi r)$, and the potential read off at the end is

$$
\Phi=-\frac{\kappa^{2}Mc^{4}}{16\pi r},
$$

the factor sixteen rather than eight coming from the trace reversal, which halves the time-time entry at this order: $\bar h_{00}=2h_{00}$, and $\Phi$ reads $h_{00}$ and not $\bar h_{00}$. Matching $\Phi=-GM/r$ then gives $\kappa^{2}=16\pi G/c^{4}$ — one equation, one unknown, and the transcribed value is the only one that ends at the measured potential. The check that matters is not the arithmetic of the factor but its *uniqueness*: $\Phi$ is linear in $\kappa^{2}$ and the mass is fixed, so no other value produces $-\nabla\Phi$ with the measured $G$.

**It is not fixed by the algebra, and that is the corpus's position.** The field-equations article lists this as an open item in exactly these terms: the coupling constant is transcribed, and whether any normalisation intrinsic to the algebra — a preferred trace identity, a bilinear, an inner product on the Lie subspace — fixes it, is not known. Nothing in this article contradicts that. What the article adds is the *reason the question is not urgent*: a theory that fixes the form of the response and leaves one constant to be measured is in the same position as general relativity, whose $G$ is also measured. The framework's gap is that it has not shown its constant to be forced; it is not that the constant is arbitrary.

**One honesty clause, because the alternative is tempting.** A derivation of $\kappa^{2}$ from the algebra would be a genuine result and would make the framework predictive rather than transcriptionally faithful. The Newtonian limit cannot produce it, because $\Phi$ is linear in $\kappa^{2}$: any value reproduces *some* $G$-like constant, and only the measured $G$ picks out the physical one. A derivation must come from the action, and the action is absent.

## The Spatial Part, and $\gamma=1$ for Free

The trace reversal did two things at once, and the second is easy to miss.

**The result.** $h_{ij}=(r_{s}/r)\delta_{ij}$ came out of the same operation that gave $h_{00}=r_{s}/r$, with no additional input. In the parametrised post-Newtonian form for a static, spherically symmetric source,

$$
g_{00}=-\left(1-\frac{2GM}{c^{2}r}\right),
\qquad
g_{ij}=\left(1+2\gamma\,\frac{GM}{c^{2}r}\right)\delta_{ij},
$$

and $2GM/(c^{2}r)=r_{s}/r$, so the framework's carried metric has $\gamma=1$.

**Why that is not nothing.** The parameter $\gamma$ is measured: the Shapiro delay, the deflection of light and the Cassini bound all constrain it, and the bound is at the $10^{-5}$ level. A framework that carried an arbitrary $\gamma$ would be constrained by those measurements; this one is not, because the single trace reversal that produces the potential also produces $\gamma=1$. The equality is not a coincidence of the ansatz — it follows from $\bar h_{\imath\jmath}$ having one nonzero entry, which follows from $T_{\imath\jmath}$ having one, which follows from the Newtonian truncation. Given the equation, $\gamma=1$ is forced.

**The qualification.** $\gamma=1$ is exactly general relativity's value, and the article's tone should not obscure what that means: the framework, in this sector, makes *no* prediction that differs from general relativity. It reproduces the static weak field identically. That is the sense in which the corpus's gravity is empirically equivalent, and it is the sense the article *The Empirical Status of the Biquaternion Framework* uses.

## The Frames That Carry It

A metric is carried when a frame exists whose Gram matrix is that metric, and both the weak-field and the exact static metrics are carried explicitly. Writing them out is short, and it discharges the corpus's standing obligation that "carried" be exhibited rather than asserted.

**The weak-field frame.** In isotropic coordinates,

$$
\tilde E_{\Phi,0}=i\sqrt{1-\frac{r_{s}}{r}}\;e_t,
\qquad
\tilde E_{\Phi,k}=\sqrt{1+\frac{r_{s}}{r}}\;\vec e_k,\qquad k\in\{x,y,z\},
$$

whose Gram matrix is $\mathrm{diag}\big(-(1-r_{s}/r),\,1+r_{s}/r,\,1+r_{s}/r,\,1+r_{s}/r\big)$ by the two values $\langle ie_t,ie_t\rangle_{\natural}=-1$ and $\langle\vec e_k,\vec e_l\rangle_{\natural}=\delta_{kl}$, the cross terms vanishing because the time leg is orthogonal to the spatial triple. That is the interval of the previous section, to first order in $h$.

**The exact frame.** The Schwarzschild exterior in its standard coordinates is

$$
ds^{2}=-f^{2}c^{2}dt^{2}+\frac{dr^{2}}{f^{2}}+r^{2}d\Omega^{2},
\qquad
f^{2}=1-\frac{r_{s}}{r},
$$

the same line element as the corpus's *Curved Spacetime and the Biquaternion Framework* records for the widened class, and it is carried by

$$
\tilde E_{\Phi,0}=i f\,e_t,
\qquad
\tilde E_{\Phi,r}=\frac{1}{f}\,\vec e_r,
\qquad
\tilde E_{\Phi,\theta}=r\,\vec e_\theta,
\qquad
\tilde E_{\Phi,\phi}=r\sin\theta\,\vec e_\phi,
$$

with $\vec e_r,\vec e_\theta,\vec e_\phi$ the unit vectors of the spherical frame expanded in $\vec e_x,\vec e_y,\vec e_z$ by the ordinary rotation. The Gram matrix is $\mathrm{diag}\big(-f^{2},\,1/f^{2},\,r^{2},\,r^{2}\sin^{2}\theta\big)$, and the point of writing it is that the radial leg is *free*: it is $1/f$, not $f$, and the freedom is exactly the one the parent article identifies as the difference between a metric class that can hold a vacuum solution and one that cannot.

**The check.** The exact frame was evaluated at $r=3r_{s}$ and $r=10r_{s}$ with $\theta=0.9$, $\phi=1.3$. The diagonal entries reproduce $-f^{2}$, $1/f^{2}$ and $r^{2}$ to machine precision, and the largest off-diagonal entry at $r=10r_{s}$ is $3.5\times10^{-8}$ against $g_{\theta\theta}=8.7\times10^{8}$ — a relative $4\times10^{-17}$, which is the round-off of the arithmetic and not a residual of the frame.

## Matter Falls With the Potential It Made

The chain so far runs from $\rho$ to $\Phi$. The last link runs from $\Phi$ back to matter, and it is what makes the whole thing a theory rather than a parametrisation.

**The geodesic.** For the static weak metric, $\Gamma^{k}_{00}=-\tfrac12\partial_k g_{00}=\partial_k\Phi/c^{2}$ to first order, and the geodesic equation for a slow test mass, with $x^{0}=ct$ and $dx^{0}/d\tau\approx c$,

$$
\frac{d^{2}x^{k}}{d\tau^{2}}=-\Gamma^{k}_{00}\left(\frac{dx^{0}}{d\tau}\right)^{2}\approx-\partial_{k}\Phi ,
$$

so $\ddot{\vec r}=-\nabla\Phi$: a test mass accelerates toward the source with the potential the source produced.

**The same function, and why that is the content.** The $\Phi$ in the acceleration is the $\Phi$ in $g_{00}$, and $g_{00}$ is the component the density produced. There is no second potential and no second constant. A framework whose source side and whose force side were independent would have to show that they agree; this one shows it in one line, because both read the same entry of the same array.

**The conservation statement behind it.** The same conclusion follows from the source side alone, and the corpus's *Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form* records the identity: the divergence of the symmetric stress vanishes on shell, $\sum_{\imath}\partial_{\imath}T_{\imath\jmath}=0$, as the Noether statement of translation invariance. For dust, $T_{\imath\jmath}=\rho u_{\imath}u_{\jmath}$, the time component is the continuity equation and the spatial components give Euler's equation with $\dot{\vec u}=-\nabla\Phi$. The conservation law and the geodesic equation are the same statement in two vocabularies, and in a frame formulation that is not an accident: the frame that is sourced and the frame that is followed are the same field.

## What the Chain Closes and What It Does Not

**Closed.** The chain from a static density to the measured potential, with one constant calibrated and $\gamma=1$ forced. The frames that carry both the weak-field and the exact static metrics, exhibited and checked. The self-consistency of source and force, in one line of geodesic arithmetic.

**Not closed, and it is the head of the chain.** The equation $\Box_{\Phi}\bar h_{\imath\jmath}=-\tfrac{16\pi G}{c^{4}}T_{\imath\jmath}$ is transcribed. An action for the frame would replace transcription by derivation, and its variation would be the first term of the stationary condition written in the preceding article. That action does not exist in the corpus, and the field-equations article states in its own words that the non-linear equation is not reached.

**Not closed, and it is downstream.** The non-linear completion: the chain above is first order in $h$, and a solution that is exact in $r_{s}/r$ requires the full equation. The exact frame is carried, but the equation that would select it is not derived, so the exactness of the frame is exactness of the *carrier* and not of a solution.

**Not closed, and it is cosmological.** A constant term has no reading here. The cosmology article states it at length: there is no field equation for a $\Lambda$ to sit in, no trace-free structure to make it an integration constant, and no framework quantity with its dimensions. The Newtonian limit says nothing about it, and this article does not either.

**Not closed, and it is empirical.** Nothing in the chain predicts a deviation from general relativity. The one framework-adjacent prediction the corpus records is external — the spatially varying speed-of-light programme's screening of the static field — and its deviation from general relativity is of order $(r_{s}/r)^{2}$, which at the solar surface is $1.8\times10^{-11}$ and is far below the precision of the classical tests. On its own carried metrics, the framework is indistinguishable from general relativity, and the Newtonian limit is the clearest demonstration of that: it reproduces $\gamma=1$ without trying to.

## Summary

The chain from a static density to Newton's potential runs, and it runs entirely inside the framework's letters. A density $\rho$ gives $\bar h_{00}=4GM/(c^{2}r)$ through the transcribed equation; the trace reversal gives $h_{00}=r_{s}/r$ and, in the same step, $h_{ij}=(r_{s}/r)\delta_{ij}$; the interval gives $g_{00}=-(1-r_{s}/r)$ and $\Phi=-GM/r$; and the geodesic of that interval gives $\ddot{\vec r}=-\nabla\Phi$. One equation, one trace reversal, one identification.

The constant $16\pi G/c^{4}$ is calibrated by the chain and not chosen by it: the potential is linear in it, so the measured $G$ fixes it uniquely, and no other value reproduces Newton. It is not fixed by the algebra, and the article says so in the corpus's own terms rather than claiming a derivation.

The parameter $\gamma$ comes out one, forced by the same trace reversal that produces the potential, which means the framework reproduces the static weak field identically to general relativity and predicts no deviation in it.

Both frames are exhibited: the weak-field isotropic frame and the exact Schwarzschild frame with a free radial leg, the second checked to a relative $4\times10^{-17}$ in its off-diagonal entries.

The head of the chain is the break. The field equation is transcribed, and no action for the frame exists in the corpus to derive it from. Everything downstream of that break is closed, and everything upstream of it is the section's remaining work.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\rho$ | mass density of the static source |
| $T_{00}=\rho c^{2}$ | the only source component at Newtonian order |
| $\bar h_{\imath\jmath}$ | trace-reversed metric perturbation |
| $h_{\imath\jmath}$ | metric perturbation |
| $\kappa^{2}=16\pi G/c^{4}$ | coupling constant of the transcribed equation |
| $r_{s}=2GM/c^{2}$ | the length the chain produces |
| $f^{2}=1-r_{s}/r$ | lapse function of the exact static frame |
| $\Phi$ | Newtonian potential, $\Phi=-GM/r$ |
| $\gamma$ | post-Newtonian spatial parameter, equal to one here |
| $\Gamma^{k}_{00}$ | the connection entry that gives the Newtonian acceleration |

## Further Reading

- [Matter Into the Frame: The Variation That Defines the Source](matter-into-the-frame-the-variation-that-defines-the-source.html), for the source dictionary this article's chain begins from.
- [Linearized Gravity in Biquaternionic Form](linearized-gravity-in-biquaternionic-form.html), for the transcribed equation, the harmonic fixing condition and the trace-reversal carried by the frame.
- [Gravitational Waves in Biquaternionic Form](gravitational-waves-in-biquaternionic-form.html), for the same equation in its inhomogeneous reading and the quadrupole power that follows from it.
- [The Kerr–Schild Sub-class and the Vacuum Wave](the-kerr-schild-sub-class-and-the-vacuum-wave.html), for the exact vacuum members the frame route reaches, of which the static exterior here is the simplest.
- [The Lagrangian and Linearised Gravity](the-lagrangian-and-linearised-gravity.html), for the quadratic action, its variation and the normalisation that article quotes and this one calibrates.
- [The Einstein Field Equations in the Biquaternion Framework: The Linearised Dictionary and the Non-Linear Gap](the-einstein-field-equations-in-the-biquaternion-framework-the-linearised-dictionary-and-the-non-linear-gap.html), for the absent action and the non-linear equation not reached.
- [The Empirical Status of the Biquaternion Framework](the-empirical-status-of-the-biquaternion-framework.html), for the domain-by-domain agreement and the one external prediction of order $(r_{s}/r)^{2}$.
- [Cosmology in the Biquaternion Framework: The Carried Metric and the Missing Source](cosmology-in-the-biquaternion-framework-the-carried-metric-and-the-missing-source.html), for what a constant term would need and does not have.
