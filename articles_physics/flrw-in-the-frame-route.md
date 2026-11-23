# __FLRW in the Frame Route__

## Introduction

The cosmology article says that the frame route carries the FLRW metric, and it says it in a paragraph. This article says it in a computation. The difference matters, because "carried" is the word that does the most work in the corpus's gravitational writing and the easiest word to leave unearned. A metric is carried when a frame field exists whose Gram matrix is that metric, and that is a statement that can be exhibited rather than asserted.

There is a specific reason to exhibit it here. The FLRW line element is diagonal with two functions, a lapse and a scale factor, and the *local-scale route* of the parent article — the one-function reading of the speed of light — is also diagonal with one function. The two look like the same class and they are not, and the difference is what this article establishes: the frame route carries an arbitrary scale factor with no condition on it, while the local-scale class carries no expansion at all. A time-dependent local $c$ produces a metric that is identically flat, and that was checked here by computing the Riemann tensor of $c(t)=2+\sin t$ and finding every component zero.

The article's result is therefore narrow and complete. The frame exists, explicitly, for flat and curved spatial slices. The scale factor stays free, and nothing in the framework fixes it. And the local-scale reading of the same diagonal form is not a cosmology but a reparametrisation of time.

## The Frame, Written Out

The material sector is $\mathbb{B}_{\Phi}=\{i r'_t e_t+r_x\vec e_x+r_y\vec e_y+r_z\vec e_z\}$, and its bilinear form is $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{\natural})$, with the $i$ on the time slot carrying the one minus. Take

$$
\tilde E_{\Phi,0}=iN(r'_t)\,e_t,
\qquad
\tilde E_{\Phi,i}=a(r'_t)\,\vec e_i,\qquad i=1,2,3,
$$

with a lapse $N$ and a scale factor $a$, both functions of the time coordinate only. The four legs are elements of $\mathbb{B}_{\Phi}$, the first with a scale on the time axis and the three with a common scale on the space axes. Their Gram matrix is immediate from the form,

$$
g_{\imath\jmath}=\langle\tilde E_{\Phi,\imath},\tilde E_{\Phi,\jmath}\rangle_{\natural}
=\mathrm{diag}\bigl(-N^{2},\,a^{2},\,a^{2},\,a^{2}\bigr),
$$

because $\langle i e_t,i e_t\rangle_{\natural}=-1$, $\langle \vec e_i,\vec e_j\rangle_{\natural}=\delta_{ij}$, and the time leg is orthogonal to the spatial legs. The three cross terms vanish without any condition on $N$ or $a$: the algebra's form makes the time axis orthogonal to the spatial triple once, and no choice of the two functions can spoil it. This was checked numerically at $N=1.7$, $a=2.3$, where the Gram matrix came out as $\mathrm{diag}(-2.89,\,5.29,\,5.29,\,5.29)$.

So a spatially flat FLRW metric with an arbitrary lapse and an arbitrary scale factor is the Gram matrix of a frame that can be written in one line. The lapse is pure gauge in this reading — a reparametrisation of the time coordinate multiplies $N$ by a function and leaves the geometry alone — so the frame carries one physical function and one gauge choice, which is exactly the count the metric has.

## Spatial Curvature at No Extra Cost

The flat-slice case is the easy half, and the interesting question is whether the frame route needs anything new for $k=\pm1$. It does not, and the reason is a finite-dimensional fact about positive-definite forms.

For a spatial slice of constant curvature $k$ the three-metric is

$$
\gamma_{ij}(x)=a^{2}\,\bar\gamma_{ij}(x),
\qquad
\bar\gamma_{ij}=\frac{4\,\delta_{ij}}{\bigl(1+k\,r^{2}\bigr)^{2}},
\qquad r^{2}=x_{1}^{2}+x_{2}^{2}+x_{3}^{2},
$$

in stereographic coordinates, with $\bar\gamma$ the unit sphere ($k=+1$), the flat metric ($k=0$), or the unit hyperboloid ($k=-1$). The factor $a^{2}\bar\gamma$ is positive definite, so it has a Cholesky factor $L$ with $L L^{\mathsf T}=a^{2}\bar\gamma$, and the frame

$$
\tilde E_{\Phi,i}=\sum_{j}L_{ij}\,\vec e_j
$$

has Gram matrix $\langle\tilde E_{\Phi,i},\tilde E_{\Phi,j}\rangle_{\natural}=\sum_{\imath\in\{x,y,z\}}L_{i\imath}L_{j\imath}=(LL^{\mathsf T})_{ij}=a^{2}\bar\gamma_{ij}$. The frame is a pointwise linear map from the tangent space of the slice into the spatial triple, and it exists because both forms are positive definite and three-dimensional: no curvature obstructs a pointwise isometry between two positive-definite quadratic spaces of the same dimension.

Two checks were run. The Cholesky reconstruction reproduces $a^{2}\bar\gamma$ exactly. And the metric $\bar\gamma$ with $k=+1$ is the pullback of the unit-sphere embedding $X=(2x_{1},2x_{2},2x_{3},r^{2}-1)/(1+r^{2})$ in $\mathbb{R}^{4}$, confirmed by differentiating the embedding and comparing the induced metric to $4\delta_{ij}/(1+r^{2})^{2}$; the image has unit norm, so the sphere is the unit sphere and its scalar curvature is the standard $6$. Scaling by $a^{2}$ rescales the curvature by $a^{-2}$, and a direct computation of the three-dimensional Ricci scalar of $a^{2}\bar\gamma$ gave $6.0000$ at $a=1$, $2.6667$ at $a=1.5$ and $1.5000$ at $a=2$ for $k=+1$, and the negatives $-6.0000$ and $-2.6667$ for $k=-1$, which is $6k/a^{2}$ in every case.

So the curved-slice FLRW metric is carried, with the same one-line construction and one extra algebraic step.

The cost is smaller than the general case suggests, and it is worth saying why. In stereographic coordinates the slice metric is conformally flat, $a^{2}\bar\gamma=a^{2}f(x)\,\delta_{ij}$ with $f=4/(1+kr^{2})^{2}$, so the Cholesky factor is diagonal and the frame is $\tilde E_{\Phi,i}=a\sqrt{f(x)}\,\vec e_i$: one function of position and three constants. A general slicing would need the full factor, with six independent entries, and the pointwise rotation freedom $L\mapsto OL$, $O\in SO(3)$, would remove three of them, leaving the three independent components of $\gamma$. The FLRW slices are cheap because they are conformally flat, not because the construction is trivial in general.

For $k=-1$ the stereographic chart covers $r<1$, where $\bar\gamma$ is positive definite and the Cholesky factor is real; beyond the coordinate horizon the chart fails before the construction does, which is a property of the chart and not of the carrier.

## What the Frame Buys: the Expansion

With the frame in hand, the kinematic quantities of a cosmology are ordinary computations on the Gram metric.

The comoving congruence is the time leg, $u=\tilde E_{\Phi,0}$, normalised so that $u\cdot u=-1$ when $N=1$. Its expansion is

$$
\theta=\sum_{\imath}(g^{-1})_{\imath\imath}\,\nabla_{\imath}u_{\imath}
=\frac{1}{N a^{3}}\,\partial_{t}\bigl(N a^{3}\bigr),
$$

and with $N=1$ this is $\theta=3\dot a/a$. The value was computed directly from the connection for $a=1+\tfrac12 t$ and came out as $3\dot a/a=1$ at $t=1$, matching the formula. The shear vanishes identically, because the spatial frame is $\tilde E_{\Phi,i}=a\vec e_i$ with a single common scale, so the congruence is shear-free and the anisotropy of the expansion is zero — which is the algebraic content of isotropy at this level.

The Raychaudhuri equation then gives the standard acceleration relation once the curvature term is supplied, and the two Friedmann equations are what the Einstein equations become on this ansatz. That last step is not available here, and this article does not take it: the framework has no Einstein equation, so it has no Friedmann equation either. The cosmological article says the same and marks the Friedmann equations as a transcription. The frame route supplies the left-hand side of the kinematic identities and none of the dynamics.

What the frame does supply, and this is the honest positive result, is that **nothing about the scale factor is obstructed** at the level of the carrier. An arbitrary $a(t)$ gives a frame, an arbitrary $N(t)$ gives a frame, and the curved-slice cases give frames too. The route is a carrier and not a filter.

## Why the Local-Scale Route Cannot Do This

The same diagonal form appears in the parent article's local-scale reading, and it is worth being precise about why that reading produces no cosmology.

Take $c_{\mathrm{loc}}=c_{\mathrm{loc}}(r'_t)$ and the metric $g=\mathrm{diag}\bigl(-c_{\mathrm{loc}}(r'_t)^{2},1,1,1\bigr)$. The substitution $d\tau=c_{\mathrm{loc}}(r'_t)\,dr'_t$ turns it into $-d\tau^{2}+dr_{x}^{2}+dr_{y}^{2}+dr_{z}^{2}$, so it is the flat metric in a different time coordinate; this is not an argument but a change of variable, and the Riemann tensor computed from the connection for $c_{\mathrm{loc}}=2+\sin r'_t$ is zero in every component. The spatial metric is untouched at $1$, so there is no scale factor, no expansion, and no Hubble rate: a function on the time axis rescales time and nothing else.

Take instead a spatially varying $c_{\mathrm{loc}}=c_{\mathrm{loc}}(\vec r)$. That class is genuinely curved, but its spatial slices stay flat, $g_{ij}=\delta_{ij}$, so no member has a non-constant scale factor or a non-zero spatial curvature. And within the class Ricci-flatness forces $c_{\mathrm{loc}}$ affine and the metric flat, which is the parent's result and the reason the local-scale reading carries no vacuum geometry either.

The two readings of the same diagonal form therefore have opposite characters. The frame route's $a$ multiplies the spatial triple and produces expansion. The local-scale route's $c$ multiplies the time axis and produces a reparametrisation. They are not the same object under another name, and the sign of the difference is a factor of $i$: the frame's time leg is $iN e_t$, so its scale enters the interval squared with a minus, while the local $c$ enters as a coefficient of $dt^{2}$ with no $i$ at all. The corpus's own note that the one minus is the square of the $i$ in $Q_t$ is the same statement.

## What Is Carried and What Is Not

**Carried.** The FLRW metric for any $k$, any $a(t)$ and any lapse, with an explicit frame; the induced three-metric and its scalar curvature $6k/a^{2}$; the expansion $3\dot a/a$; the shear-free property of the comoving congruence; the volume element $\sqrt{|g|}=N a^{3}\sqrt{\bar\gamma}$ as a Gram determinant. Each of these is a computation on the frame, and each was checked.

**Not carried, and not derived.** The scale factor itself: no equation fixes $a(t)$, and the article's $a$ is a supplied function throughout. The Friedmann equations: they are the Einstein equations on this ansatz, and the framework has neither. The equation of state: the source cannot be written, because the natural packaging of a rank-two tensor collapses to its trace.

**Homogeneity has no home.** Isotropy does: the spatial frame $a\vec e_i$ is invariant under the unit real quaternions acting on the left, which is the algebraic form of a three-parameter rotation symmetry. Homogeneity does not, because it is a statement about a translation group acting transitively on a slice, and the algebra has no translations. This asymmetry is the cosmology article's finding and it survives the frame construction: the frame carries a *homogeneous* metric because the metric is given, not because the algebra noticed the homogeneity.

## Summary

The FLRW metric is inside the frame route, and the article has exhibited the frame rather than asserting membership. With $\tilde E_{\Phi,0}=iN e_t$ and $\tilde E_{\Phi,i}=a\vec e_i$ the Gram matrix is $\mathrm{diag}(-N^{2},a^{2},a^{2},a^{2})$ for arbitrary $N$ and $a$; for curved slices the spatial frame is the Cholesky factor of $a^{2}\bar\gamma$, which exists because the form is positive definite, and the three-scalar curvature came out as $6k/a^{2}$. The comoving expansion is $3\dot a/a$ and the shear vanishes.

The boundary in the other direction is exact and was computed: a time-dependent local $c$ gives a Riemann tensor that is identically zero, so the local-scale reading of the same diagonal form carries no expansion, and a spatially varying $c$ curves the metric while leaving the slices flat. The frame route's scale factor is a scale on the spatial triple; the local-scale route's $c$ is a scale on the time axis. Only the first is a cosmology.

What remains outside is everything dynamical: no equation fixes $a$, no Friedmann equation follows, and no source can be written. The article therefore closes the first item of the cosmology article — the explicit frame, for $k=0$ and for $k=\pm1$ — and leaves the rest of that ledger untouched.

## Further Reading

- [Cosmology in the Biquaternion Framework: The Carried Metric and the Missing Source](cosmology-in-the-biquaternion-framework-the-carried-flrw-metric-and-the-missing-source.html), for the FLRW targets, the rank-two obstruction to the source, and the list of obstacles this article's first item sits in.
- [Curved Spacetime and the Biquaternion Framework](curved-spacetime-and-the-biquaternion-framework.html), for the local-scale route, its Ricci-flatness-forces-flatness result, and the comparison the last section uses.
- [The Gram Matrix as the Only Metric](the-gram-matrix-as-the-only-metric.html), for why the Gram matrix is a congruence and what Sylvester's law does and does not permit.
- [The Kerr–Schild Sub-class and the Vacuum Wave](the-kerr-schild-sub-class-and-the-vacuum-wave.html), for the other exact class the frame route carries and the vacuum wave the local-scale route cannot.
- [The Einstein Field Equations in the Biquaternion Framework: The Linearised Dictionary and the Non-Linear Gap](the-einstein-field-equations-in-the-biquaternion-framework-the-linearised-dictionary-and-the-non-linear-gap.html), for the dynamics the Friedmann equations would require.
- *Curvature and Geodesics*, for the curvature conventions in which $6k/a^{2}$ and $3\dot a/a$ are computed.
