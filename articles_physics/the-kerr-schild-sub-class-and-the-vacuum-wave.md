# __The Kerr–Schild Sub-class and the Vacuum Wave__

## Introduction

The frame route carries any Lorentzian metric, and its verdict is that the algebra contributes nothing beyond a bilinear form. There is one family of frames in which it contributes a little more, and it happens to be the family in which the exact solutions the corpus's neighbouring articles work with are written. It is the **Kerr–Schild form**,

$$
g_{\imath\jmath} = \delta_{\imath\jmath} + 2h\,\ell_{\imath} \ell_{\jmath},
\qquad
\sum_{\imath} \ell_{\imath}^2 = 0,
$$

with $\ell_{\imath}$ a null covector and $h$ a scalar function, both otherwise free. Every array in this article is a set of components in the coordinate $Q_{\imath}$, with $Q_t=i q'_t$ and $Q_{\imath}=q_{\imath}$, so the flat form is the unit metric $\delta_{\imath\jmath}=(1,1,1,1)$ and the one minus of the material interval is the square of the $i$ in $Q_t$; a null covector has $\sum_{\imath} \ell_{\imath}^2=0$, its time component imaginary. Kerr, Kerr–Newman and Schwarzschild are all of this shape, with $\ell_{\imath}$ the repeated principal null direction of the congruence the solution is built on.

The article exists because this class is the sharpest available demonstration of a boundary inside the programme itself. The local-scale route of the parent article has one free function, the speed of light, and inside it **Ricci-flatness forces flatness**: a metric that route can write down at all cannot be a non-flat Ricci-flat spacetime, and so cannot carry a vacuum gravitational wave or a vacuum black-hole exterior. The frame route carries one, and this sub-class carries one in closed form, with a single harmonic function. That contrast is the reason the article is written, and it is stated without apology: the frame route reaches further than the one-function class, and the difference is a vacuum wave.

The claim of the article is exact and narrow. The family is the orbit of the flat form under a **shear along a null direction**; the shear's generator is square-zero because a null direction is a zero divisor; and the properties usually listed one at a time for the family are the faces of that single vanishing square. Nothing is claimed about content: $h$ and $\ell_{\imath}$ stay free, and no equation of the framework fixes them.

One convention is needed for the components, and it is the one the index rules impose: every index stays low, and no weight is written, because the sign is in the coordinate. The units are $e_t,\vec e_x,\vec e_y,\vec e_z$ and the natural form on them is $\delta_{\imath\jmath}$, so the datum $\ell_{\imath}$ names an element of $\mathbb{B}_{\Phi}$, its time component imaginary as the material reading requires,

$$
\tilde{\mathcal L}_{\Phi,\mathrm{null}} = \sum_{\imath} \ell_{\imath}\,e_{\imath} \in \mathbb{B}_{\Phi},
\qquad
\langle e_{\imath},\tilde{\mathcal L}_{\Phi,\mathrm{null}}\rangle_\natural = \ell_{\imath},
\qquad
\langle\tilde{\mathcal L}_{\Phi,\mathrm{null}}\rangle_\natural = \sum_{\imath} \ell_{\imath}^2 = 0 ,
$$

and the null covector is exactly the element of vanishing norm. Normalised this way, $\tilde{\mathcal L}_{\Phi,\mathrm{null}}$ makes the shear below reproduce $g_{\imath\jmath} = \delta_{\imath\jmath} + 2h\,\ell_{\imath} \ell_{\jmath}$, with the unit metric as its only coefficient. (The companion article *The Algebrodynamical Programme* writes the same deformation as $\delta_{\imath\jmath} + h\,\ell_{\imath} \ell_{\jmath}$, so its profile is half of this one.)

## The Operator a Null Element Defines

The vanishing of the norm is the corpus's own criterion for a zero divisor, and the light cone is the zero-divisor cone. What the Kerr–Schild form uses is not the element but one operator built from it,

$$
N_{\tilde{\mathcal L}_{\Phi,\mathrm{null}}} : \mathbb{B}_{\Phi} \to \mathbb{B}_{\Phi},
\qquad
N_{\tilde{\mathcal L}_{\Phi,\mathrm{null}}}(X) = \tilde{\mathcal L}_{\Phi,\mathrm{null}}\,\langle X,\tilde{\mathcal L}_{\Phi,\mathrm{null}}\rangle_\natural ,
$$

a real-linear map of $\mathbb{B}_{\Phi}$ into itself, the scalar $\langle X,\tilde{\mathcal L}_{\Phi,\mathrm{null}}\rangle_\natural$ being real on $\mathbb{B}_{\Phi}$. Its square vanishes,

$$
N_{\tilde{\mathcal L}_{\Phi,\mathrm{null}}}^{\,2}(X) = \tilde{\mathcal L}_{\Phi,\mathrm{null}}\,\langle X,\tilde{\mathcal L}_{\Phi,\mathrm{null}}\rangle_\natural\,\langle\tilde{\mathcal L}_{\Phi,\mathrm{null}}\rangle_\natural = 0 ,
$$

and the only step worth naming is the one that makes it vanish: $\langle X,\tilde{\mathcal L}_{\Phi,\mathrm{null}}\rangle_\natural$ is a scalar, hence central, so it passes through $\tilde{\mathcal L}_{\Phi,\mathrm{null}}$ and leaves the norm behind. The trace carries the same condition, $\mathrm{tr}\,N_{\tilde{\mathcal L}_{\Phi,\mathrm{null}}} = \langle\tilde{\mathcal L}_{\Phi,\mathrm{null}}\rangle_\natural = 0$, and the rank is one.

**The distinction from left multiplication must be kept.** For an element of $\mathbb{B}_{\Phi}$ that map is never square-zero unless $\tilde{\mathcal L}_{\Phi,\mathrm{null}} = 0$: a null $\tilde{\mathcal L}_{\Phi,\mathrm{null}} = i r'_t\,e_t + \vec r_\Phi$ with $r'_t \ne 0$ satisfies $\tilde{\mathcal L}_{\Phi,\mathrm{null}}^2 = 2i r'_t\tilde{\mathcal L}_{\Phi,\mathrm{null}}$, which is the Cayley–Hamilton identity $M^2 = (\mathrm{tr}\,M)M$ of the $2\times2$ image at vanishing determinant, while $r'_t = 0$ forces $\vec r_\Phi = 0$ by the null condition, so the only nilpotent element of $\mathbb{B}_{\Phi}$ is zero. Nilpotent null elements do exist in the algebra at large — $\vec e_x + i\vec e_y$ has square zero and vanishing norm — but they are not material elements, their spatial coefficients being complex. The operator that is square-zero for every null direction of $\mathbb{B}_{\Phi}$ is the rank-one $N_{\tilde{\mathcal L}_{\Phi,\mathrm{null}}}$, and the distinction is the one the corpus already draws between the square-zero cone and the zero-divisor cone. The Kerr–Schild shear is built on the second operator, not the first.

## The Frame It Produces, and Four Properties That Are One

The frame is the rigid frame carried by the shear, and the shear is the exponential of the square-zero operator:

$$
T=\exp\bigl(hN_{\tilde{\mathcal L}_{\Phi,\mathrm{null}}}\bigr)=\mathrm{id}+hN_{\tilde{\mathcal L}_{\Phi,\mathrm{null}}},
$$

the series terminating at the linear term. On the rigid frame,

$$
Te_{\imath}=e_{\imath}+h\,\tilde{\mathcal L}_{\Phi,\mathrm{null}}\,\langle e_{\imath},\tilde{\mathcal L}_{\Phi,\mathrm{null}}\rangle_\natural=e_{\imath}+h\,\ell_{\imath}\,\tilde{\mathcal L}_{\Phi,\mathrm{null}},
$$

and the metric is the Gram matrix of the result. The computation is one line, and its two cross terms are the same term twice:

$$
\langle Te_{\imath},Te_{\jmath}\rangle_\natural
=\delta_{\imath\jmath}+2h\,\ell_{\imath}\ell_{\jmath}+h^2\ell_{\imath}\ell_{\jmath}\langle\tilde{\mathcal L}_{\Phi,\mathrm{null}}\rangle_\natural
=\delta_{\imath\jmath}+2h\,\ell_{\imath}\ell_{\jmath}.
$$

The four properties usually listed for the class are the single vanishing $N^2=0$, read in four places.

- **The deformation is affine in $h$.** The quadratic term is $\ell_{\imath}\ell_{\jmath}\langle\tilde{\mathcal L}_{\Phi,\mathrm{null}}\rangle_\natural$ and it vanishes with the null condition, so the family is a straight line through the flat form $\delta_{\imath\jmath}$ and not a nonlinear orbit. This is what makes the class an ansatz at all, and it is the null condition read at second order.
- **The metric is unimodular.** $T$ is unipotent, $\det T=\exp(h\,\mathrm{tr}\,N)=1$, hence $\det g=(\det T)^2\det\delta=\det\delta=1$ in the components of the coordinate $Q_{\imath}$; in the real coordinates $(r'_t,r_x,r_y,r_z)$ the same determinant reads $-1$, because the $i$ of $Q_t$ squares the time slot, and there $\sqrt{-\det g}=1$, so the Laplace–Beltrami operator of the curved Dirac article loses its measure factor. Unimodularity is the vanishing of $\operatorname{tr}N$, which is the null condition read as a trace.
- **The inverse is the flat inverse with the sign of the correction reversed.** $T^{-1}=\exp(-hN)=\mathrm{id}-hN$, so the metric of the inverse frame is $\delta_{\imath\jmath}-2h\,\ell_{\imath}\ell_{\jmath}$: the flat inverse array with the correction's sign reversed. The square, once more.
- **The direction is fixed, and it stays null.** $N\tilde{\mathcal L}_{\Phi,\mathrm{null}}=\tilde{\mathcal L}_{\Phi,\mathrm{null}}\langle\tilde{\mathcal L}_{\Phi,\mathrm{null}}\rangle_\natural=0$, so $T\tilde{\mathcal L}_{\Phi,\mathrm{null}}=\tilde{\mathcal L}_{\Phi,\mathrm{null}}$: the shear does not move the null element at all. The norm carries no frame, so $\tilde{\mathcal L}_{\Phi,\mathrm{null}}$ is null for the deformed metric exactly as it was for the flat one. At the level of arrays the inverse array sends $\ell_{\imath}$ where the flat array sends it, because its correction is $-2h\,\ell_{\imath}$ times the vanishing scalar $\sum_{\jmath}\ell_{\jmath}^2$; nullity is what makes the two agree, not an approximation. That is why the congruence of a Kerr–Schild solution is carried into the curved metric unchanged.

**The numerical check.** All four were recomputed on a hundred random null directions with four random values of $h$ each — the affineness, $\det g=\det\delta$, the closed-form inverse array, $T\tilde{\mathcal L}=\tilde{\mathcal L}$, and nullity in the deformed metric — together with the column form $Te_{\imath}=e_{\imath}+h\ell_{\imath}\tilde{\mathcal L}$ and the kernel $\tilde{\mathcal L}^{\perp}$ fixed pointwise; no residual exceeded $10^{-9}$. Unipotence was checked in its defining form, $(T-\mathrm{id})^2=h^2N^2=0$, which holds to $10^{-13}$; the spectrum $\{1\}$ follows from it, whereas an eigenvalue solver returns $1$ only to $10^{-7}$, the usual loss of half the digits on a Jordan block.

## What the Shear Leaves Alone

Since $N$ has rank one, its kernel is the hyperplane orthogonal to $\tilde{\mathcal L}_{\Phi,\mathrm{null}}$,

$$
\ker N=\left\{X\in\mathbb{B}_{\Phi}:\langle X,\tilde{\mathcal L}_{\Phi,\mathrm{null}}\rangle_\natural=0\right\}=\tilde{\mathcal L}_{\Phi,\mathrm{null}}^{\perp},
$$

so $T$ fixes $\tilde{\mathcal L}_{\Phi,\mathrm{null}}^{\perp}$ pointwise and shears only along the one remaining direction. In the real slice, where $h$ and the three spatial $\nu_{\Phi k}$ are real and $\nu_t$ is imaginary, so that $\tilde{\mathcal L}_{\Phi,\mathrm{null}}$ lies in $\mathbb{B}_{\Phi}$ and $g$ is a real Lorentzian metric, that is the whole geometric content: the shear is the identity on the degenerate three-plane that contains the null direction, and it moves nothing else.

**Complexified, the statement is sharper, and the complexification is the algebra's own.** $\mathbb{B}_{\Phi}$ is a real four-plane: its elements are $\sum_{\imath} Q_{\imath} e_{\imath}$ with $Q_t$ imaginary and $Q_{\imath}$ real, and its null cone is the ordinary light cone, in which the largest totally null subspace has dimension one. But $i\mathbb{B}_{\Phi}=\mathbb{B}_{\Psi}$ — the star is conjugate-linear, so $(i\tilde Q)^{*}=-i\tilde Q^{*}=i\tilde Q$ for $\tilde Q\in\mathbb{B}_{\Phi}$ — and therefore $\mathbb{B}_{\Phi}\otimes_{\mathbb{R}}\mathbb{C}=\mathbb{B}_{\Phi}\oplus i\mathbb{B}_{\Phi}=\mathbb{B}$. In that complex four-space the norm is complex and a null element lies in exactly **two** maximal totally null planes, each two-dimensional and both inside $\tilde{\mathcal L}_{\Phi,\mathrm{null}}^{\perp}$; they are the **left and right** null planes that the Kerr–Schild literature separates. Since the shear is the identity on the whole of $\tilde{\mathcal L}_{\Phi,\mathrm{null}}^{\perp}$, it fixes both planes **point by point**, so the null planes of the congruence are null for the curved metric without approximation. That is the algebraic content of the property the Kerr–Schild literature uses as a working tool.

## A Constant Direction, and a Vacuum Wave

With $h$ and $\ell_{\imath}$ constant, $T$ is a constant invertible map and $g$ is $\delta_{\imath\jmath}$ in the chart $y_\alpha=T_\alpha{}_{\imath} Q_{\imath}$; the metric is flat. The remark is small, and it marks a limit of the frame route's flatness criterion: a frame that is pure rotor is flat, but the converse fails. A constant shear is not a rotor, and it produces no curvature, because it is a change of chart rather than a change of frame. Flatness of the frame has at least these two independent sources, and the second is a diffeomorphism, the object the algebra does not have.

With $\ell_{\imath}$ constant and $h$ varying, the same family is curved, and its member is the wave the neighbouring articles meet as a gravitational wave. Take $\ell_{\imath}$ with $2\pi\nu_t=-i$ and $k_3=1$, null since $4\pi^{2}\nu_t^2+k_3^2=-1+1=0$, and pass to the real null coordinates $u=r'_t+r_z$ and $v=r'_t-r_z$, in which $\ell_{\imath}\,dR_{\imath}=du$ and the metric reads

$$
ds^2=-du\,dv+dx^2+dy^2+2h(u,x,y)\,du^2,
$$

and its Ricci tensor has a single independent component, in the curvature convention used throughout the category,

$$
\mathrm{Ric}_{uu}=-\left(\frac{\partial^2h}{\partial r_x^2}+\frac{\partial^2h}{\partial r_y^2}\right),
$$

all other components vanishing. The metric is therefore Ricci-flat exactly when $h$ is harmonic in the two transverse coordinates. For $h=x^2-y^2$ and for $h=e^x\cos y$ the Ricci tensor vanishes and the Riemann tensor does not, so both are vacuum solutions; for constant $h$ the Riemann tensor vanishes, as the chart argument requires. These are plane-fronted gravitational waves with a constant null direction, written in the algebra's own notation, with one free harmonic function.

**The contrast with the local-scale route, stated once more.** Within the local-scale class Ricci-flatness forces flatness, so that route carries no vacuum gravitational wave at all. The frame route carries one, and the Kerr–Schild sub-class carries one with a constant direction and a single harmonic function. What neither carries is a reason for the function: $h$ is inserted, and the algebra supplies the shape of the ansatz and the four identities that shape entails, and nothing else.

## What the Instance Is Worth

The instance is worth its algebra, and no more.

**It is worth the shape of the ansatz.** The frame route counts sixteen frame functions modulo six rotor parameters; the Kerr–Schild sub-class fixes the frame once and for all to be the rigid frame carried by one null shear, and the metric that results is governed, in a fixed chart, by three functions of position — the direction of $\ell_{\imath}$ up to scale and the amplitude $h$. Three functions rather than ten is an economy, not a content: all three remain free.

**It is worth the four identities**, which the literature states one at a time and which are one line here, and the unimodularity in particular, because in a Kerr–Schild chart $\sqrt{-\det g}=1$, so the Laplace–Beltrami operator inside the Lichnerowicz square carries no measure factor at all.

**It is worth the vacuum wave**, because it is the one object in the category that a competing route provably cannot produce, and because the wave's profile is one harmonic function of two transverse coordinates.

**What it is not worth is dynamics.** That a member is Ricci-flat is a property of the inserted function, checked and not produced. And the two objects that would carry the physical content sit outside the algebra: for the Kerr–Newman solution the null direction is the principal null congruence selected by the Kerr theorem, and $h$ is fixed by the Einstein–Maxwell equations. Both belong to the corpus elsewhere — the congruence to the twistor and algebrodynamical articles, the ring the solution carries to the article on the complex-displaced singularity — and in both the algebra enters as the language of the congruence, not as the source of the equation. On this sharper instance the article therefore repeats the conclusion of the frame route: **carrying is not deriving**.

## Summary

The Kerr–Schild family is the orbit of the flat form under a shear along a null direction, $g_{\imath\jmath}=\delta_{\imath\jmath}+2h\ell_{\imath}\ell_{\jmath}$ with $\ell$ null and $h$ free. The shear's generator is the rank-one operator $N(X)=\tilde{\mathcal L}\langle X,\tilde{\mathcal L}\rangle_\natural$, which is square-zero because the scalar $\langle X,\tilde{\mathcal L}\rangle_\natural$ is central and the norm $\langle\tilde{\mathcal L}\rangle_\natural$ vanishes. It is not left multiplication by $\tilde{\mathcal L}$, which is never nilpotent on $\mathbb{B}_{\Phi}$.

The shear is $T=\mathrm{id}+hN$ by the terminating exponential. The four properties of the class — affinity in $h$, unimodularity, the sign-reversed inverse, and the fixed null direction — are that one vanishing read in four places, and all four were checked numerically on random null directions to better than $10^{-9}$. The shear fixes the hyperplane orthogonal to $\tilde{\mathcal L}$ pointwise, which in the complexification is where the left and right null planes live, and that is why the congruence passes into the curved metric unchanged.

With a constant null direction and a varying profile the class is a plane-fronted vacuum wave, Ricci-flat exactly when the profile is harmonic in the two transverse coordinates. That is the object the local-scale route cannot carry: inside that class Ricci-flatness forces flatness. The class is the frame route's reach made concrete, and its limit is the same as the route's: the profile is inserted, and the algebra supplies the shape of the ansatz and not the equation that would fix it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q_{\imath}$ | coordinate with components $Q_t=iq'_t$, $Q_{\imath}=q_{\imath}$; the flat form is $\delta_{\imath\jmath}$ |
| $g_{\imath\jmath}=\delta_{\imath\jmath}+2h\ell_{\imath}\ell_{\jmath}$ | Kerr–Schild metric; $\ell_{\imath}$ null, $h$ free |
| $\tilde{\mathcal L}_{\Phi,\mathrm{null}}=\sum_{\imath}\ell_{\imath} e_{\imath}$ | the null element of $\mathbb{B}_{\Phi}$; $\langle\tilde{\mathcal L}_{\Phi,\mathrm{null}}\rangle_\natural=0$ |
| $N(X)=\tilde{\mathcal L}_{\Phi,\mathrm{null}}\langle X,\tilde{\mathcal L}_{\Phi,\mathrm{null}}\rangle_\natural$ | the square-zero rank-one shear generator |
| $T=\mathrm{id}+hN$ | the shear; unipotent, $\det T=1$ |
| $\tilde{\mathcal L}_{\Phi,\mathrm{null}}^{\perp}$ | the kernel of $N$; fixed pointwise by $T$ |
| $\mathrm{Ric}_{uu}=-\left(h_{,xx}+h_{,yy}\right)$ | the only nonzero component for a constant null direction |
| $u=r'_t+r_z$, $v=r'_t-r_z$ | null coordinates of the wave chart |

## Further Reading

- [Curved Spacetime and the Biquaternion Framework](curved-spacetime-and-the-biquaternion-framework.html), for the frame route this class sits inside, and for the local-scale route it leaves behind.
- [Gravitational Waves in Biquaternionic Form](gravitational-waves-in-biquaternionic-form.html), for the wave sector proper: the trace-reversed perturbation and the harmonic fixing condition.
- [The Light Cone as the Biquaternion Zero-Divisor Cone](the-light-cone-as-the-biquaternion-zero-divisor-cone.html), for nullity as the zero-divisor condition.
- [Zero Divisors as a Physical Locus in Biquaternionic Form](zero-divisors-as-a-physical-locus-in-biquaternionic-form.html), for the null cone as a locus and not merely an algebraic condition.
- [The Algebrodynamical Programme](the-algebrodynamical-programme-nonlinear-cauchy-riemann-conditions-self-quantized-charge-and-induced-causal-geometry.html), for the same deformation written with half the profile.
- [Congruence Twistors and the Fields They Generate](congruence-twistors-and-the-fields-they-generate.html), for the principal null congruence that a Kerr–Newman member carries.
- [The Complex-Displaced Singularity and the Circle Electron](the-complex-displaced-singularity-and-the-circle-electron.html), for the ring the member carries.
- [Null Electromagnetic Fields and the Shear-Free Congruence](null-electromagnetic-fields-and-the-shear-free-congruence.html), for the null congruence as an algebraic object.
- [Curvature and Geodesics](../articles_maths/curvature-and-geodesics.html), for the curvature convention in which $\mathrm{Ric}_{uu}$ is stated.
- [The Semisimple–Nilpotent Split of a Biquaternion](../articles_maths/the-semisimple-nilpotent-split-of-a-biquaternion.html), for the split that isolates the nilpotent part of any element.
