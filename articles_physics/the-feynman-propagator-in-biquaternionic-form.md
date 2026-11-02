# __The Feynman Propagator in Biquaternionic Form__

## Introduction

The companion article *Canonical Quantization of the Biquaternion Dirac Field* quantizes the biquaternion Dirac field on its spinor module: it promotes the field to an operator-valued distribution, imposes the equal-time anticommutators, expands the field in the plane-wave solutions, and builds the Fock space. It closes with an explicit accounting of what is standard and what remains open, and it concludes that the construction is a transcription of ordinary canonical quantization rather than a derivation from the algebra $\mathbb{B}$.

The dynamics is the one-sided chiral pair

$$
\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L,\qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R .
$$

The framework now carries two equations under that name, and they must not be read as one. This pair is the definition. The gradient acts by left multiplication, the field lies in $\Delta=S\oplus S^{\mathrm{c}}$, and the mass is the off-diagonal pairing of the two chiral halves. The **two-sided** form of *The Dirac Equation in Biquaternionic Form* is a single equation on $\mathbb{B}$,

$$
\mathcal{N}F=\Big(i\frac{\partial}{\partial t'}+D_3\Big)F-mi\,\overline{F}\,\vec e_z=0,
$$

in which $D_3$ is the spatial Dirac operator of that article, the mass term acts by right multiplication through $\vec e_z$, and the conjugation supplies the antilinear part. The two forms are related by the dictionary $A$ of that article, and they are not the same operator. Everything below is written for the one-sided pair, whose spinor-module representative is the ordinary $(\slashed p-m)\psi=0$; the two-sided form differs by the place of the mass and by the conjugation, and its free solutions obey the same mass-shell condition.

Natural units $\hbar=c=1$ are used throughout, so the four-momentum is $\tilde P=iEe_t+\vec p$ and the mass shell is $\tilde P\tilde P^\natural=-m^2$.

This article is about the next object in that construction: the **two-point function** of the quantized field on the spinor-module representative, the Feynman propagator

$$
\boxed{\;S_F(x-y)\;=\;\langle 0|\,T\,\psi^{\mathrm{fop}}(x)\,\bar{\psi^{\mathrm{fop}}}(y)\,|0\rangle\;},
$$

with $T$ the fermionic time-ordering operator. The two-point function is where the boundary condition of the theory is stored. Its momentum-space amplitude is not a function but a distribution, and what makes it the *Feynman* amplitude rather than the retarded or advanced one is a contour prescription in the complex energy plane — the $i\epsilon$.

The specific question this article asks is a question about the algebra. The biquaternion framework already carries a complex structure: the scalar imaginary $i$ is a fixed central element with $i^2=-1$, it is what turns the material time coordinate into $ict'$, and it is what lets the mass shell be written as the single quadratic condition $\tilde P\tilde P^{\natural}=-m^2$ whose two roots in the energy are the positive- and negative-frequency branches (the particle and antiparticle modes in the standard interpretation). The Feynman prescription is also an insertion of $i$: $m^2\mapsto m^2-i\epsilon$. Are these the same $i$ doing the same work? Is the contour deformation the algebra's own complex structure, or is it an independent analytic input that the algebra can only write down?

We answer this on a concrete case, by computing the pole structure and the contour explicitly and by recomputing every displayed formula on a momentum chosen for the purpose. The finding is stated at the outset because it is the article's content. **The algebra supplies the complex plane in which the contour is drawn, and a natural notation for the prescription — the deformed mass-shell scalar $\tilde P\tilde P^{\natural}+m^2-i\epsilon$, whose shift $-i\epsilon\,e_t$ is a central element along the $ict'$ axis of the material sector — but it does not select the contour.** The deformation's *axis* is algebraically natural; its *orientation*, which is what distinguishes the Feynman propagator from the retarded and advanced ones, is an analytic boundary condition. In this problem the algebra adds notation and a home for the $i\epsilon$, not the physics that fixes it. If that is all it adds, we say so.

## The Two-Point Function of the Quantized Dirac Field

The quantized field of the companion article is

$$
\psi^{\mathrm{fop}}(x)=\int\!\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\vec p}}}
\sum_{r=1}^{2}\Big[a_r^{\mathrm{fop}}(\vec p)\,w^{(r)}(\vec p)\,\exp(-ip\cdot x)
+b_r^{\mathrm{fop}\dagger}(\vec p)\,v^{(r)}(\vec p)\,\exp(+ip\cdot x)\Big],
$$

with $E_{\vec p}=+\sqrt{\vec p^2+m^2}$. Its adjoint is $\bar{\psi^{\mathrm{fop}}}=\psi^{\mathrm{fop}\dagger}iR_{\vec e_x}$: the Hermitian conjugate, then the timelike cell of the reference frame.

Write $L_a\psi=a\psi$ and $R_b\psi=\psi b$ for the two multiplications of $\mathbb{B}$, and

$$
\slashed p\;:=\;iR_{\vec e_x}p_0-\sum_{k=1}^{3}iL_{\vec e_k}R_{\vec e_y}p_k
$$

for the **momentum cell**, the four frame cells combined with the metric signs, chosen so that the cell squares to the Lorentz square of the momentum,

$$
(\slashed p)^2=p^2\,\mathbf{1},\qquad p^2=p_0^2-\vec p^2.
$$

The signs are not free: they are the signs of the cell anticommutator

$$
\{iL_{e_\mu}R_{\vec e_{\nu(\mu)}},iL_{e_\nu}R_{\vec e_{\nu(\nu)}}\}=2g_{\mu\nu}\mathbf{1},
\qquad g=\mathrm{diag}(+1,-1,-1,-1),\qquad \mathbf{1}=L_{e_t}R_{e_t},
$$

with $\mathbf{1}$ the identity cell. The body is written in these cells; section *The Gamma Formulation* gives their standard names.

The mode operators obey

$$
\{a_r^{\mathrm{fop}}(\vec p),a_s^{\mathrm{fop}\dagger}(\vec k)\}
=\{b_r^{\mathrm{fop}}(\vec p),b_s^{\mathrm{fop}\dagger}(\vec k)\}
=(2\pi)^3\delta_{rs}\delta^{(3)}(\vec p-\vec k),
$$

with all other anticommutators vanishing. The parent article's spinors satisfy

$$
\bar w^{(r)}w^{(s)}=2m\,\delta_{rs},\qquad \bar v^{(r)}v^{(s)}=-2m\,\delta_{rs},
$$

and the two spin sums

$$
\sum_{r=1}^2 w^{(r)}\bar w^{(r)}=\slashed p+m,\qquad
\sum_{r=1}^2 v^{(r)}\bar v^{(r)}=\slashed p-m ,
$$

the momentum cell being on the mass shell, $p_0=E_{\vec p}$.

Contracting the mode operators against the vacuum gives the two elementary two-point functions. The **positive-frequency** piece is

$$
W_+(x-y)\;=\;\langle 0|\,\psi^{\mathrm{fop}}(x)\,\bar{\psi^{\mathrm{fop}}}(y)\,|0\rangle
=\int\!\frac{d^3p}{(2\pi)^3}\frac{1}{2E_{\vec p}}\,\big(\slashed p+m\big)\,\exp(-ip\cdot(x-y)),
$$

in which only the $a^{\mathrm{fop}} a^{\mathrm{fop}\dagger}$ contraction survives, and the **negative-frequency** piece is

$$
W_-(x-y)\;=\;\langle 0|\,\bar{\psi^{\mathrm{fop}}}(y)\,\psi^{\mathrm{fop}}(x)\,|0\rangle
=\int\!\frac{d^3p}{(2\pi)^3}\frac{1}{2E_{\vec p}}\,\big(\slashed p-m\big)\,\exp(+ip\cdot(x-y)),
$$

in which only $b^{\mathrm{fop}} b^{\mathrm{fop}\dagger}$ survives. In both expressions the momentum cell is on shell, because the free mode expansion contains the on-shell modes and nothing else. These two objects are not yet the propagator; each is a boundary value of an analytic function, and it is the time ordering that combines them into $S_F$.

Time ordering for a fermion field carries the anticommutation sign:

$$
S_F(x-y)=\theta(x_0-y_0)\,W_+(x-y)-\theta(y_0-x_0)\,W_-(x-y).
$$

The relative minus is not a convention; it is the statement that the two field operators anticommute. Every sign in what follows traces back to it, and it is the quantity a recomputation must reproduce.

## The Pole Structure and the Contour

The two $\theta$ functions can be represented by a single four-dimensional integral. The standard result, and the object whose biquaternion form is the subject of this article, is

$$
\boxed{\;S_F(x-y)\;=\;i\int\!\frac{d^4p}{(2\pi)^4}\;
\exp(-ip\cdot(x-y))\;\frac{\slashed p+m}{p^2-m^2+i\epsilon},
\qquad \epsilon\to0^+\;}.
$$

The overall $i$ and the $i\epsilon$ are fixed by requiring that the $p_0$ integral reproduce the two branches, with the normalization of the time-ordered product and the fermionic relative sign. It is worth performing that check explicitly, because it is where a sign can silently go wrong.

Write the $p_0$ integral at fixed $\vec p$, and put $\Delta t=x_0-y_0$ and $\Delta\vec x=\vec x-\vec y$. Since

$$
p^2-m^2=p_0^2-\vec p^2-m^2=p_0^2-E_{\vec p}^2,
$$

the integrand has poles where

$$
\boxed{\;p_0^2-E_{\vec p}^2+i\epsilon=0,
\qquad\text{i.e.}\qquad
p_0=\pm\sqrt{E_{\vec p}^2-i\epsilon}
=\pm\Big(E_{\vec p}-\frac{i\epsilon}{2E_{\vec p}}\Big)+O(\epsilon^2)\;}.
$$

The sign is worth fixing once explicitly. Let $p_0=E_{\vec p}+\delta$. Then the denominator is $2E_{\vec p}\delta+i\epsilon$, and it vanishes at $\delta=-i\epsilon/(2E_{\vec p})$, which is **below** the axis. At $p_0=-E_{\vec p}+\delta$ the denominator is $-2E_{\vec p}\delta+i\epsilon$, and it vanishes at $\delta=+i\epsilon/(2E_{\vec p})$, which is **above** it.

This is the whole content of the prescription: the two poles are displaced in *opposite* directions. The decay of $\exp(-ip_0\Delta t)$ then selects one pole or the other:

- for $\Delta t>0$, close the contour in the lower half-plane and pick up the pole at $+E_{\vec p}$;
- for $\Delta t<0$, close in the upper half-plane and pick up the pole at $-E_{\vec p}$.

Write $p_+=(E_{\vec p},\vec p)$ and $p_-=(-E_{\vec p},\vec p)$. The residues are

$$
\mathrm{Res}_{p_0=+E_{\vec p}}\frac{\slashed p+m}{p_0^2-E_{\vec p}^2}
=\frac{\slashed p_++m}{2E_{\vec p}},
\qquad
\mathrm{Res}_{p_0=-E_{\vec p}}\frac{\slashed p+m}{p_0^2-E_{\vec p}^2}
=\frac{\slashed p_-+m}{-2E_{\vec p}},
$$

with $\slashed p_\pm=iR_{\vec e_x}(\pm E_{\vec p})-\sum_k iL_{\vec e_k}R_{\vec e_y}p_k$.

The contour contributes $-2\pi i$ when it closes below and $+2\pi i$ when it closes above. With the residues above and the overall factor $i$ of $S_F$, the two cases are

$$
\Delta t>0:\quad (-2\pi i)\cdot\frac{\slashed p_++m}{2E_{\vec p}}\cdot i
=\frac{2\pi}{2E_{\vec p}}\big(\slashed p_++m\big),
$$

$$
\Delta t<0:\quad (+2\pi i)\cdot\frac{\slashed p_-+m}{-2E_{\vec p}}\cdot i
=\frac{2\pi}{2E_{\vec p}}\big(\slashed p_-+m\big).
$$

Both carry the same **positive** weight $2\pi/(2E_{\vec p})$: the sign of the half-plane and the sign inside the residue cancel. The fermionic minus is therefore not in the contour, and it must come from the numerator. For $\Delta t>0$ the $p_0$ integral is already the positive-frequency integrand of $W_+$. For $\Delta t<0$ it is

$$
\frac{\slashed p_-+m}{2E_{\vec p}}\,\exp(+iE_{\vec p}\Delta t+i\vec p\cdot\Delta\vec x),
$$

and after $\vec p\to-\vec p$, with $p_+(-\vec p)=(E_{\vec p},-\vec p)$, the numerator identity

$$
\slashed p_-+m=-\big(\slashed p_+(-\vec p)-m\big)
$$

turns it into the negative-frequency integrand of $-W_-$. The single covariant expression, with its single factor of $i$ in front, therefore reproduces both the time ordering and the fermionic minus.

Three things are conflated in the phrase "the $i\epsilon$ does the time ordering", and they are worth separating.

1. The $i\epsilon$ fixes which pole lies in which half-plane; that is the boundary condition, and its sign is the choice of propagator.
2. The overall $i$ fixes the normalization of the amplitude relative to the two $\theta$ terms.
3. The minus in front of $W_-$ is carried by the numerator, through the spin sums $\sum w\bar w=\slashed p+m$ and $\sum v\bar v=\slashed p-m$. It is the two-point form of the anticommutation, and it has no counterpart in the scalar case, where the two residues share one numerator and the time-ordered combination is $\theta W_++\theta W_-$.

**A recomputation on a case chosen for it.** Take $m=0.7$ and $\vec p=(0.3,-0.9,1.1)$, so that $|\vec p|=1.4525839046$ and $E_{\vec p}=1.6124515497$. Recomputing the spinors, the two equations $(\slashed p-m)w^{(r)}=0$ and $(\slashed p+m)v^{(r)}=0$, the normalizations and the spin sums gives a maximum deviation of $4.4\times10^{-16}$, and $1.7\times10^{-15}$ over nine further random on-shell momenta. The cell identity

$$
(\slashed p-m)(\slashed p+m)=(p^2-m^2)\mathbf{1}
$$

is exact. For $\epsilon=10^{-3}$ the Feynman poles come out at

$$
p_0=+1.61245155-i\,3.10\times10^{-4}
\qquad\text{and}\qquad
p_0=-1.61245155+i\,3.10\times10^{-4},
$$

that is, one on each side of the real axis, as claimed. A direct numerical evaluation of the $p_0$ integral along the real axis, with the grid refined near the poles and the range cut at $|p_0|=10^3$, reproduces the $\theta$-combination for both signs of $\Delta t$ to $4\times10^{-3}$ at $\epsilon=10^{-2}$ and $3\times10^{-4}$ at $\epsilon=10^{-3}$; the residual is the resolution of the two poles, which sit a distance $\epsilon/(2E_{\vec p})$ from the real axis. The relative minus was verified by evaluating the two branches separately and comparing with $\theta(x_0-y_0)W_+-\theta(y_0-x_0)W_-$.

## Feynman, Retarded, and Advanced: What Selects the Contour

The pole structure makes the choice of propagator explicit. Three prescriptions are available, and they differ only in how the two poles are displaced:

| Prescription | Denominator | Poles (to first order in $\epsilon$) |
|---|---|---|
| Feynman | $p_0^2-E_{\vec p}^2+i\epsilon$ | $+E_{\vec p}$ below, $-E_{\vec p}$ above |
| Retarded | $(p_0+i\epsilon)^2-E_{\vec p}^2$ | $\pm E_{\vec p}-i\epsilon$ (both below) |
| Advanced | $(p_0-i\epsilon)^2-E_{\vec p}^2$ | $\pm E_{\vec p}+i\epsilon$ (both above) |

The three are distinguished by whether the displacements are **opposite** (Feynman) or **common** (retarded and advanced). For $\epsilon=10^{-3}$ and the same momentum, the retarded poles are at $1.61245155-i\,10^{-3}$ and $-1.61245155-i\,10^{-3}$, and the advanced poles at the same points with $+i\,10^{-3}$: both on the same side, as the table states. Closing the contour then shows at once why the retarded propagator vanishes for $x_0-y_0<0$ and the advanced one for $x_0-y_0>0$: with both poles on one side, one of the two half-planes contains no pole.

The companion *The Klein–Gordon Propagator and Its Green's Functions in Biquaternionic Form* lists the same three displacements in the frequency $\omega$ and with the denominator written as $\vec p^2+\mu^2-\omega^2$, the negative of the one here; the pole positions agree.

This is the physical content of the $i\epsilon$, and it is exactly the content the algebra does not supply. The Feynman choice encodes the time-ordered vacuum correlation; the retarded choice encodes causal response to a source; the advanced choice is its mirror. They solve the *same* differential equation off the source and differ only in support. A choice among them is a boundary condition on the distributional inverse, and boundary conditions are not algebraic data. The companion article on the biquaternion Maxwell equation meets the same situation in the first-order problem: it selects the retarded Green's function, and it notes explicitly that the retarded kernel is a different object from the elliptic Cauchy kernel of the analysis articles, related by the Wick rotation. The selection there is made on physical grounds, not read off the algebra, and the same is true here.

## The Biquaternion Form of the Prescription

The Feynman denominator has a compact biquaternion form. With the four-momentum biquaternion $\tilde P=iE\,e_t+\vec p$ and its quaternion conjugate $\tilde P^{\natural}=iE\,e_t-\vec p$, the quaternion product is

$$
\tilde P\tilde P^{\natural}=(iE)^2+\vec p^2=-E^2+\vec p^2=-p^2 .
$$

Two signs enter, and they come from two different places. The scalar one is $i^2=-1$, which takes $(iE)^2$ to $-E^2$. The vector one is a **plus**: the vector part multiplies $-\vec p$, and $\vec p\,(-\vec p)=+\vec p^2$, because the quaternion square of a vector is $\vec p\,\vec p=-\vec p^2$ with $\vec p^2=p_x^2+p_y^2+p_z^2$ the Euclidean square. The last step is $p^2=E^2-\vec p^2$.

The mass shell is then the single algebraic condition

$$
\tilde P\tilde P^{\natural}=-m^2
\quad\Longleftrightarrow\quad
E^2-\vec p^2=-m^2
\quad\Longleftrightarrow\quad
E^2=\vec p^2+m^2 ,
$$

whose two frequency branches $E=\pm E_{\vec p}$ are the two poles above. Substituting $\tilde P\tilde P^{\natural}=-p^2$ in the amplitude gives the biquaternion form,

$$
\boxed{\;S_F(p)\;=\;\frac{i(\slashed p+m)}{p^2-m^2+i\epsilon}
\;=\;-\,\frac{i(\slashed p+m)}{\tilde{P}\tilde{P}^{\natural}+m^2-i\epsilon}\;},
$$

the denominator being the **deformed mass-shell operator** $\mathcal{M}(\tilde{P})=\tilde{P}\tilde{P}^{\natural}+m^2$, shifted by $-i\epsilon$. The prescription is thus a deformation of the scalar on which the mass shell is defined, not an addition to the algebra.

The shift has a natural algebraic home. The deformation is $-i\epsilon\,e_t$, an element with purely imaginary scalar coefficient and zero vector part; it is anti-Hermitian, so by the definition of the material sector it lies in $\mathbb{M}_-$, and it lies in the centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$. Written out, $-i\epsilon\,e_t$ is a displacement along the same $ie_t$ direction that the framework uses for the temporal coordinate of $\mathbb{M}_-$, the direction of $ict'$. So the algebra does three things here, and it is worth separating them:

1. It provides the complex plane in which the contour is drawn — the coefficient complex structure of $\mathbb{C}_{\mathbb{B}}$.
2. It locates the deformation direction, the $ict'$ axis of $\mathbb{M}_-$.
3. It makes the undeformed mass shell a single algebraic condition $\tilde{P}\tilde{P}^{\natural}=-m^2$, so that the two poles are the two branches of one equation rather than two unrelated objects.

What it does not do is choose the orientation. Replacing $\epsilon$ by $-\epsilon$ reverses the pole displacements, turning the Feynman propagator into the anti-Feynman one; replacing the opposite displacement by a common one gives the retarded or advanced propagator. All three denominators are built from the same $\tilde{P}\tilde{P}^{\natural}+m^2$ and the same central $i$. The algebra cannot tell them apart, because the difference is not in the algebra; it is in which half-plane the contour closes, equivalently in which boundary condition defines the distribution. The $i\epsilon$ is therefore written *with* the algebra's complex structure and *lives in* its material sector, but it is not *produced* by either. The algebra names the axis; the physics chooses the direction.

The closest the complex structure comes to doing real work is the Wick rotation. In the $ict'$ convention the hyperbolic operator

$$
\Box=-\frac{1}{c^2}\frac{\partial^2}{\partial t'^2}+\Delta
$$

becomes, after $t'\to-i\tau$, the elliptic operator with all four directions on the same footing. The Euclidean Green's function of the elliptic operator is unique once one demands decay at infinity, and its analytic continuation back to real time is the Feynman propagator. In that route the complexification of time is exactly what makes the continuation available.

But the selection is still analytic, not algebraic. The step "continue the unique Euclidean Green's function" is the input: uniqueness rests on a decay condition in the Euclidean variables, and the direction of the rotation is a further choice, equivalent to the sign of $\epsilon$. Nothing in $\mathbb{B}$ prefers decaying-in-Euclidean over growing. So the Wick rotation exhibits the algebra's complex structure as a *necessary* carrier of the continuation, and the analytic input as the thing that fixes which continuation; it does not convert the algebra into a derivation of the Feynman prescription.

## The Propagator as a Distribution

It matters that $S_F$ is a distribution, and not only because the statement is true. The integral defining it converges for no real $p$ on the mass shell; the mass shell is precisely the pole set, and the unregulated amplitude $(\slashed p+m)/(p^2-m^2)$ is undefined there. The $i\epsilon$ is what turns the algebraic inverse of $\slashed p-m$ off the mass shell into a distributional inverse on all of momentum space.

The propagator on the spinor-module representative of the chiral pair satisfies

$$
(\mathbb{D}-m)\,S_F(x-y)=i\,\delta^{(4)}(x-y),
\qquad
S_F=(\mathbb{D}+m)\,G_F,
\qquad
(\Box-m^2)\,G_F=i\,\delta^{(4)},
$$

in the distributional sense, with $\mathbb{D}$ the pair operator of the conventions article, $\mathbb{D}\Psi=(\tilde\nabla\Psi_R,\tilde\nabla^{\natural}\Psi_L)$ and $\mathbb{D}^2=\Box$. The overall factor is a normalization: the conventions article writes the Green matrix $\mathcal{S}=(\mathbb{D}+m)G$ with $(\mathbb{D}-m)\mathcal{S}=\delta I$, whereas the time-ordered product of this article carries $S_F=i\mathcal{S}$; the companion Klein–Gordon article fixes $(\Box-\mu^2)G=-\delta^{(4)}$ at $\mu=m$, so its $G$ is $-i$ times the $G_F$ here. None of the three normalizations affects a pole position or a support. The differential equation holds for the Feynman, retarded, and advanced choices alike, because the difference between them is supported only on the mass shell and carries no additional source off it. The differential equation, therefore, does not determine the propagator. What determines it is the time-ordering prescription, which in momentum space is the contour and in configuration space is the split of support into $x_0>y_0$ and $x_0<y_0$.

This is the sharpest way to see why the question "does the algebra supply the $i\epsilon$?" cannot be answered by finding an $i$ in the algebra. The equation of motion supplies a differential operator, and a differential operator has many distributional inverses; the algebra supplies the operator $\tilde{\nabla}$ (or its second-order companion $\tilde{\nabla}\tilde{\nabla}^{\natural}$) and hence the same many inverses. Distinguishing the Feynman one requires a condition that is not an equation of motion. The complex structure enters when that condition is *represented* — as a contour in $\mathbb{C}_{\mathbb{B}}$, or as a point in the complexified time plane — and not when it is *chosen*.

## Relation to the Thermal Two-Point Function

One further structure is worth recording, because it is the place where the framework's complex time does carry a genuinely analytic condition. The companion article *The KMS Condition and the Biquaternion Framework* characterizes thermal equilibrium by the analyticity of the correlation function $F_{AB}(t')=\omega_\beta(A\,\alpha_{t'}(B))$ in the strip $0<\mathrm{Im}(t')<\beta$, with boundary relation $F_{AB}(t'+i\beta)=F_{BA}(-t')$; the imaginary-time direction is intrinsic to the material sector $\mathbb{M}_-$, and the companion quantization article shows that the anticommutator turns the boundary relation into the Fermi–Dirac distribution and the antiperiodic Matsubara frequencies $\omega_n=(2n+1)\pi/\beta$.

At finite temperature the time-ordered two-point function is not given by a vacuum contour integral but by the discrete Matsubara sum over the compact imaginary-time circle; the real-time retarded and advanced propagators still carry their own $\epsilon$ prescriptions, and they are obtained from the Matsubara sum by analytic continuation, not by an algebraic operation. The imaginary-time complexification that the algebra carries is a real feature of the thermal state — it is where the KMS analyticity lives — but it does not select the vacuum contour either. It is a consistency: the same imaginary direction that makes the mass shell algebraic is the direction in which the thermal correlation functions are analytic, and the vacuum contour is recovered as the $\beta\to\infty$ limit rather than derived from the algebra.

## What the Algebra Adds and What It Does Not

**Standard field theory, transcribed.** The mode expansion and the mode anticommutators of the companion article; the two elementary two-point functions $W_+$ and $W_-$ and their spin sums; the covariant representation of $S_F$ with its contour; the identification of the pole displacements with the Feynman, retarded, and advanced propagators; the distributional equation $(\mathbb{D}-m)S_F=i\delta$; and the finite-temperature reduction to the Matsubara sum. None of this is new, and none of it depends on the biquaternion structure beyond the kinematical conventions already fixed by the read-list articles.

**What the biquaternion notation provides.** The deformed mass-shell scalar $\tilde{P}\tilde{P}^{\natural}+m^2-i\epsilon$; the pole set as the two branches of one algebraic condition; and the location of the deformation in the centre $\mathbb{C}_{\mathbb{B}}$, along the $ict'$ axis of the material sector $\mathbb{M}_-$.

**What remains open in the framework.**

- **The intrinsic operator.** Whether a genuinely $\mathbb{B}$-valued two-point function $\langle 0|T\tilde{\Psi}(\tilde{Q})\tilde{\Psi}^\flat(\tilde{Q}_2)|0\rangle$, paired with the trace $2\,\mathrm{Sc}(\cdot)$ or the biquaternion norm, exists and reproduces the spinor-module $S_F$. The companion quantization article leaves the intrinsic field open; this article inherits that gap.
- **Whether the algebra can *select* the contour.** We have argued that it cannot, on the ground that Feynman, retarded, and advanced differ only by boundary condition. A derivation of the Feynman prescription from an algebraic property of $\mathbb{B}$ alone would contradict that argument; we record the contrary as a possibility but do not claim it, and we have found no candidate.
- **The meaning of the $\mathbb{M}_-$ location.** That the deformation lies along the $ict'$ direction may be a genuine structural fact — the same direction as the KMS strip — or an artifact of writing $\epsilon$ as a scalar. We have not distinguished the two.
- **Empirical content.** As with the rest of the framework, whether any of this yields a prediction distinguishing it from standard quantum field theory is open, and the present article changes nothing about it.

The honest summary of the algebra's role is the one we gave in the introduction. The complex structure of $\mathbb{B}$ is what makes the $i\epsilon$ writable, and it names the axis along which the deformation acts; it does not supply the orientation that defines the Feynman propagator. On this problem the biquaternion framework adds notation and a natural home for the prescription, not a derivation of it.

## The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{e_t}R_{\vec e_x},\quad \gamma_1=iL_{\vec e_x}R_{\vec e_y},\quad \gamma_2=iL_{\vec e_y}R_{\vec e_y},\quad \gamma_3=iL_{\vec e_z}R_{\vec e_y},\quad \gamma_5=-iL_{e_t}R_{\vec e_z} .
$$

The body's momentum cell then reads

$$
\slashed p=\gamma_0p_0-\sum_k\gamma_kp_k ,
$$

the spatial signs being those of $g=\mathrm{diag}(+1,-1,-1,-1)$.

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality $\Gamma$; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

## Summary

The Feynman propagator of the biquaternion Dirac field is the time-ordered two-point function

$$
S_F(x-y)=\langle 0|\,T\,\psi^{\mathrm{fop}}(x)\,\bar{\psi^{\mathrm{fop}}}(y)\,|0\rangle .
$$

Its content is the contour prescription, and the prescription is fixed by time ordering together with the fermionic anticommutation sign:

$$
S_F(x-y)=i\int\!\frac{d^4p}{(2\pi)^4}\,\exp(-ip\cdot(x-y))\frac{\slashed p+m}{p^2-m^2+i\epsilon},
\qquad \slashed p=iR_{\vec e_x}p_0-\sum_{k=1}^{3}iL_{\vec e_k}R_{\vec e_y}p_k .
$$

The $p_0$ integral has poles at $p_0=\pm\big(E_{\vec p}-i\epsilon/2E_{\vec p}\big)$: the positive pole below the real axis and the negative pole above it. Closing below for $x_0-y_0>0$ and above for $x_0-y_0<0$ gives the two branches with the same positive weight $2\pi/(2E_{\vec p})$, the sign of the half-plane cancelling the sign inside the residue; the fermionic relative minus is carried by the numerator, through $\slashed p_-+m=-(\slashed p_+(-\vec p)-m)$, which is the two-point form of the anticommutation.

Writing the four-momentum biquaternion $\tilde{P}=iE\,e_t+\vec p$, so that $\tilde{P}\tilde{P}^{\natural}=-p^2$, the propagator amplitude becomes

$$
S_F(p)=-\frac{i(\slashed p+m)}{\tilde{P}\tilde{P}^{\natural}+m^2-i\epsilon},
$$

and the prescription is a deformation of the mass-shell scalar. The deformation $-i\epsilon\,e_t$ lies in the centre $\mathbb{C}_{\mathbb{B}}$ and along the $ict'$ axis of the material sector $\mathbb{M}_-$. The Feynman, retarded, and advanced propagators differ only in whether the two pole displacements are opposite or common; the algebra provides the complex plane and the axis of the deformation but not its orientation, which is a boundary condition on the distributional inverse. The algebra therefore adds notation and a natural home for the $i\epsilon$, not the selection of the Feynman contour.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $e_t=1$, $\vec e_k^2=-e_t$ |
| $i$ | Scalar imaginary, central, $i^2=-1$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ | Centre of $\mathbb{B}$ |
| $L_a,R_b$ | Left and right multiplication, $L_a\psi=a\psi$, $R_b\psi=\psi b$, $L_aR_bL_cR_d=L_{ac}R_{db}$ |
| $\mathbf{1}=L_{e_t}R_{e_t}$ | Identity cell |
| $iL_{e_\mu}R_{\vec e_{\nu(\mu)}}$ | Frame cell of the coordinate $x_\mu$, with $\nu(t)=x$ and $\nu(k)=y$ |
| $g=\mathrm{diag}(+1,-1,-1,-1)$ | Clifford metric of the cells, $\{iL_{e_\mu}R_{\vec e_{\nu(\mu)}},iL_{e_\nu}R_{\vec e_{\nu(\nu)}}\}=2g_{\mu\nu}\mathbf{1}$ |
| $\slashed p=iR_{\vec e_x}p_0-\sum_k iL_{\vec e_k}R_{\vec e_y}p_k$ | Momentum cell, $(\slashed p)^2=p^2\mathbf{1}$ |
| $\tilde{\nabla}=e_t\partial/\partial Q_t+\sum_k \vec e_k\partial/\partial Q_k$ | Biquaternionic gradient; $Q_t$ is the time coordinate, $ict'$ on $\mathbb{M}_-$ |
| $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}$ | d'Alembertian |
| $\mathbb{D}$ | Pair operator of the conventions article, $\mathbb{D}\Psi=(\tilde\nabla\Psi_R,\tilde\nabla^{\natural}\Psi_L)$, $\mathbb{D}^2=\Box$ |
| $\tilde{\Psi}=\tilde{\Psi}_L+\tilde{\Psi}_R$, $\tilde{\Psi}^\flat=-\tilde{\Psi}^{*}$ | Biquaternion Dirac field on $\Delta=S\oplus S^{\mathrm c}$ and its anti-Hermitian conjugate |
| $\psi$, $\bar\psi=\psi^\dagger iR_{\vec e_x}$ | Spinor-module representative and its adjoint |
| $p_\mu=(E,\vec p)$, $p^2=E^2-\vec p^2$ | Four-momentum and its Lorentz square |
| $\psi^{\mathrm{fop}}$, $a_r^{\mathrm{fop}}(\vec p)$, $b_r^{\mathrm{fop}}(\vec p)$ | Quantized field; particle and antiparticle modes |
| $w^{(r)}(\vec p),v^{(r)}(\vec p)$ | Positive- and negative-frequency plane-wave spinors |
| $\bar w^{(r)}w^{(s)}=2m\delta_{rs}$, $\bar v^{(r)}v^{(s)}=-2m\delta_{rs}$ | Spinor normalizations |
| $\sum_r w^{(r)}\bar w^{(r)}=\slashed p+m$, $\sum_r v^{(r)}\bar v^{(r)}=\slashed p-m$ | Spin sums, on shell |
| $W_\pm(x-y)$ | Positive- and negative-frequency two-point functions |
| $S_F(x-y)=\langle 0|T\,\psi^{\mathrm{fop}}(x)\bar{\psi^{\mathrm{fop}}}(y)|0\rangle$ | Feynman propagator |
| $\tilde{P}=iE\,e_t+\vec p$ | Four-momentum biquaternion, $\tilde{P}\tilde{P}^{\natural}=-p^2$ |
| $\tilde{P}\tilde{P}^{\natural}=-m^2$ | Biquaternion mass-shell condition |
| $\mathcal{M}(\tilde{P})=\tilde{P}\tilde{P}^{\natural}+m^2$ | Mass-shell operator; Feynman shift $\mathcal{M}(\tilde{P})-i\epsilon$ |
| $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | Trace reading of the plain form |
| $\beta=\hbar/(k_BT)$, $\omega_\beta$, $\alpha_{t'}$ | Inverse temperature, thermal state, Heisenberg evolution |
| $F_{AB}(t'+i\beta)=F_{BA}(-t')$ | KMS condition |
| $\omega_n=(2n+1)\pi/\beta$ | Fermionic Matsubara frequencies |

## Further Reading

- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the derivation of the Feynman propagator from the time-ordered product and the contour prescription.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the pole structure, the retarded and advanced Green's functions, and their relation to the Feynman one.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the Dirac propagator in the convention used here, with the overall factor of $i$.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the distributional treatment of propagators and the role of boundary conditions.
- N. N. Bogoliubov and D. V. Shirkov, *Introduction to the Theory of Quantized Fields* (Interscience, 1959), for the analytic properties of the two-point functions and the connection to the Euclidean continuation.
- M. Le Bellac, *Thermal Field Theory* (Cambridge, 1996), and J. I. Kapusta and C. Gale, *Finite-Temperature Field Theory* (Cambridge, 2006), for the Matsubara formalism and the relation of the vacuum contour to the thermal sum.
- R. Haag, *Local Quantum Physics: Fields, Particles, Algebras* (Springer, 1996), for the algebraic setting in which propagators are distributions and states are functionals.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), and Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the Clifford-algebraic background to the biquaternion and spinor structures.
