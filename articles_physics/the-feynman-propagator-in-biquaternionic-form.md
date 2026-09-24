# __The Feynman Propagator in Biquaternionic Form__

## Introduction

The companion article *Canonical Quantization of the Biquaternion Dirac Field* quantizes the biquaternion Dirac field on its spinor module: it promotes the field to an operator-valued distribution, imposes the equal-time anticommutators, expands the field in the plane-wave solutions, and builds the Fock space. It closes with an explicit accounting of what is standard and what remains open, and it concludes that the construction is a transcription of ordinary canonical quantization rather than a derivation from the algebra $\mathbb{B}$.

This article is about the next object in that construction: the **two-point function** of the quantized field, the Feynman propagator

$$
S_F(x-y) \;=\; \langle 0|\,T\,\hat{\psi}(x)\,\bar{\hat{\psi}}(y)\,|0\rangle ,
$$

with $T$ the fermionic time-ordering operator. The two-point function is where the boundary condition of the theory is stored. Its momentum-space amplitude is not a function but a distribution, and what makes it the *Feynman* amplitude rather than the retarded or advanced one is a contour prescription in the complex energy plane — the $i\epsilon$.

The specific question this article asks is a question about the algebra. The biquaternion framework already carries a complex structure: the scalar imaginary $i$ is a fixed central element with $i^2=-1$, it is what turns the material time coordinate into $ict$, and it is what lets the mass shell be written as the single quadratic condition $\tilde{k}\bar{\tilde{k}}=-m^2c^2/\hbar^2$ whose two solutions in the frequency are the positive- and negative-frequency branches (the particle and antiparticle modes in the standard reading). The Feynman prescription is also an insertion of $i$: $m^2\mapsto m^2-i\epsilon$. Are these the same $i$ doing the same work? Is the contour deformation the algebra's own complex structure, or is it an independent analytic input that the algebra can only write down?

We answer this on a concrete case, by computing the pole structure and the contour explicitly and by recomputing every displayed formula on a momentum chosen for the purpose. The finding is stated at the outset because it is the article's content. **The algebra supplies the complex plane in which the contour is drawn, and a natural notation for the prescription — the deformed mass-shell scalar $\tilde{k}\bar{\tilde{k}}+m^2-i\epsilon$, whose imaginary part lies along the $ict$ direction of the material sector — but it does not select the contour.** The deformation's *axis* is algebraically natural; its *orientation*, which is what distinguishes the Feynman propagator from the retarded and advanced ones, is an analytic boundary condition. In this problem the algebra adds notation and a home for the $i\epsilon$, not the physics that fixes it. If that is all it adds, we say so.

**Conventions.** We use those of the read-list articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$, and $i$ is the scalar imaginary with $i^2=-1$. The material and informational sectors are $\mathbb{M}_-$ (anti-Hermitian) and $\mathbb{M}_+$ (Hermitian), with $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$; $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace (the fixed-point set of complex conjugation) and $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ is the center. The biquaternionic gradient is $\tilde{\nabla}=e_0\partial_{ict}+e_1\partial_x+e_2\partial_y+e_3\partial_z$, with $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\bar{\tilde{\nabla}}\tilde{\nabla}$. On the spinor module the biquaternion Dirac equation reads $(i\gamma^\mu\partial_\mu-m)\psi=0$, with $\bar\psi=\psi^\dagger\gamma^0$, the Clifford metric $g=\mathrm{diag}(+1,-1,-1,-1)$, the spacetime metric $\eta=\mathrm{diag}(-1,+1,+1,+1)=-g$ of the $ict$ gradient, and $\not p=\gamma^0E-\boldsymbol{\gamma}\cdot\mathbf{p}$ for $p^\mu=(E,\mathbf{p})$. The wave biquaternion is $\tilde{k}=iE\,e_0+\mathbf{p}$ (natural units $\hbar=c=1$), with $\tilde{k}\bar{\tilde{k}}=-E^2+\mathbf{p}^2=-p^2$ and mass shell $\tilde{k}\bar{\tilde{k}}=-m^2$. The trace pairing is $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$.

## The Two-Point Function of the Quantized Dirac Field

The quantized field of the companion article is

$$
\hat{\psi}(x)=\int\!\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}
\sum_{r=1}^{2}\Big[\hat a_r(\mathbf p)\,u^{(r)}(\mathbf p)\,e^{-ip\cdot x}
+\hat b_r^\dagger(\mathbf p)\,v^{(r)}(\mathbf p)\,e^{+ip\cdot x}\Big],
$$

with $E_{\mathbf p}=+\sqrt{\mathbf p^2+m^2}$, and its adjoint is obtained by Hermitian conjugation and multiplication by $\gamma^0$. The mode operators obey

$$
\{\hat a_r(\mathbf p),\hat a_s^\dagger(\mathbf q)\}
=\{\hat b_r(\mathbf p),\hat b_s^\dagger(\mathbf q)\}
=(2\pi)^3\delta_{rs}\delta^{(3)}(\mathbf p-\mathbf q),
$$

with all other anticommutators vanishing. The parent article's spinors satisfy

$$
\bar u^{(r)}u^{(s)}=2m\,\delta^{rs},\qquad \bar v^{(r)}v^{(s)}=-2m\,\delta^{rs},
\qquad
\sum_{r=1}^2 u^{(r)}\bar u^{(r)}=\not p+m,\qquad
\sum_{r=1}^2 v^{(r)}\bar v^{(r)}=\not p-m .
$$

Contracting the mode operators against the vacuum gives the two elementary two-point functions. The **positive-frequency** piece is

$$
W_+(x-y)\;=\;\langle 0|\,\hat\psi(x)\,\bar{\hat\psi}(y)\,|0\rangle
=\int\!\frac{d^3p}{(2\pi)^3}\frac{1}{2E_{\mathbf p}}\,\big(\not p+m\big)\,e^{-ip\cdot(x-y)},
$$

in which only the $\hat a\hat a^\dagger$ contraction survives, and the **negative-frequency** piece is

$$
W_-(x-y)\;=\;\langle 0|\,\bar{\hat\psi}(y)\,\hat\psi(x)\,|0\rangle
=\int\!\frac{d^3p}{(2\pi)^3}\frac{1}{2E_{\mathbf p}}\,\big(\not p-m\big)\,e^{+ip\cdot(x-y)},
$$

in which only $\hat b\hat b^\dagger$ survives. In both expressions $\not p$ is **on shell**, $\not p=\gamma^0E_{\mathbf p}-\boldsymbol\gamma\cdot\mathbf p$, because the spatial integral retains only the mass-shell modes. These two objects are not yet the propagator; each is a boundary value of an analytic function, and it is the time ordering that combines them into $S_F$.

Time ordering for a fermion field carries the anticommutation sign:

$$
S_F(x-y)=\theta(x^0-y^0)\,W_+(x-y)-\theta(y^0-x^0)\,W_-(x-y).
$$

The relative minus is not a convention; it is the statement that the two field operators anticommute. Every sign in what follows traces back to it, and it is the quantity a recomputation must reproduce.

## The Pole Structure and the Contour on a Chosen Case

The two $\theta$ functions can be represented by a single four-dimensional integral. The standard result, and the object whose biquaternion form is the subject of this article, is

$$
S_F(x-y)\;=\;i\int\!\frac{d^4p}{(2\pi)^4}\;
e^{-ip\cdot(x-y)}\;\frac{\not p+m}{p^2-m^2+i\epsilon},
\qquad \epsilon\to0^+ .
$$

The overall $i$ and the $i\epsilon$ are fixed by requiring that the $p^0$ integral reproduce the two branches with their relative sign. It is worth performing that check explicitly, because it is where a sign can silently go wrong.

Write the $p^0$ integral at fixed $\mathbf p$. Since $p^2-m^2=(p^0)^2-E_{\mathbf p}^2$, the integrand has poles where

$$
(p^0)^2-E_{\mathbf p}^2+i\epsilon=0,
\qquad\text{i.e.}\qquad
p^0=\pm\sqrt{E_{\mathbf p}^2-i\epsilon}
=\pm\Big(E_{\mathbf p}-\frac{i\epsilon}{2E_{\mathbf p}}\Big)+O(\epsilon^2).
$$

The $+E_{\mathbf p}$ pole is displaced **below** the real axis and the $-E_{\mathbf p}$ pole **above** it. This is the whole content of the prescription: the two poles move in *opposite* directions. The decay of $e^{-ip^0(x^0-y^0)}$ then selects one pole or the other:

- for $x^0-y^0>0$, close the contour in the lower half-plane and pick up the pole at $+E_{\mathbf p}$;
- for $x^0-y^0<0$, close in the upper half-plane and pick up the pole at $-E_{\mathbf p}$.

The residues are

$$
\operatorname*{Res}_{p^0=+E_{\mathbf p}}\frac{\not p+m}{(p^0)^2-E_{\mathbf p}^2}
=\frac{\not p_{+}+m}{2E_{\mathbf p}},
\qquad
\operatorname*{Res}_{p^0=-E_{\mathbf p}}\frac{\not p+m}{(p^0)^2-E_{\mathbf p}^2}
=\frac{\not p_{-}+m}{-2E_{\mathbf p}},
$$

with $\not p_{+}=\gamma^0E_{\mathbf p}-\boldsymbol\gamma\cdot\mathbf p$ and $\not p_{-}=-\gamma^0E_{\mathbf p}-\boldsymbol\gamma\cdot\mathbf p$. Using the identity

$$
\not p_{-}+m=-\big(\not p_{+}(-\mathbf p)-m\big),
$$

and substituting $\mathbf p\to-\mathbf p$ in the spatial integral, the two contributions become exactly $+W_+$ for $x^0-y^0>0$ and $-W_-$ for $x^0-y^0<0$. The single covariant expression, with its single factor of $i$ in front, therefore reproduces both the time ordering and the fermionic minus. That the *same* $i$ does both is the reason the covariant form is not merely a notational convenience; it is the statement that the contour and the time ordering are one piece of data.

**A recomputation on a case chosen for it.** The claim that the contour integrates to the residues above was tested on a momentum not used to construct it. Take $m=0.7$ and $\mathbf p=(0.3,-0.9,1.1)$ in natural units, so that $|\mathbf p|=1.4525839046$ and $E_{\mathbf p}=1.6124515497$. Recomputing the Dirac spinors, the equations $(\not p-m)u^{(r)}=0$ and $(\not p+m)v^{(r)}=0$, the normalizations, and the spin sums $\sum_r u^{(r)}\bar u^{(r)}=\not p+m$ and $\sum_r v^{(r)}\bar v^{(r)}=\not p-m$ gives a maximum deviation of $4.4\times10^{-16}$; the matrix identity $(\not p-m)(\not p+m)=(p^2-m^2)I_4$, which uses $\not p^{\,2}=p^2I_4$, is exact. The Feynman poles for $\epsilon=10^{-3}$ come out at $+1.61245155-i\,3.10\times10^{-4}$ and $-1.61245155+i\,3.10\times10^{-4}$, that is, one on each side, as claimed. A direct numerical evaluation of the $p^0$ integral along the real axis reproduces the residue expressions for both signs of $x^0-y^0$ to about one percent at $\epsilon=10^{-2}$, where the discretization error is of that order. The relative minus sign was verified by evaluating both branches separately and comparing with $\theta(x^0-y^0)W_+-\theta(y^0-x^0)W_-$.

## Feynman, Retarded, and Advanced: What Selects the Contour

The pole structure makes the choice of propagator explicit. Three prescriptions are available, and they differ only in how the two poles are displaced:

| Prescription | Denominator | Poles (to first order in $\epsilon$) |
|---|---|---|
| Feynman | $(p^0)^2-E_{\mathbf p}^2+i\epsilon$ | $+E_{\mathbf p}$ below, $-E_{\mathbf p}$ above |
| Retarded | $(p^0+i\epsilon)^2-E_{\mathbf p}^2$ | $\pm E_{\mathbf p}-i\epsilon$ (both below) |
| Advanced | $(p^0-i\epsilon)^2-E_{\mathbf p}^2$ | $\pm E_{\mathbf p}+i\epsilon$ (both above) |

The three are distinguished by whether the displacements are **opposite** (Feynman) or **common** (retarded and advanced). For $\epsilon=10^{-3}$ and the same momentum, the retarded poles are at $1.61245155-i\,10^{-3}$ and $-1.61245155-i\,10^{-3}$, and the advanced poles at the same points with $+i\,10^{-3}$: both on the same side, as the table states. Closing the contour then shows at once why the retarded propagator vanishes for $x^0-y^0<0$ and the advanced one for $x^0-y^0>0$: with both poles on one side, one of the two half-planes contains no pole.

This is the physical content of the $i\epsilon$, and it is exactly the content the algebra does not supply. The Feynman choice encodes the time-ordered vacuum correlation; the retarded choice encodes causal response to a source; the advanced choice is its mirror. They solve the *same* differential equation off the source and differ only in support. A choice among them is a boundary condition on the distributional inverse, and boundary conditions are not algebraic data. The companion article on the biquaternion Maxwell equation meets the same situation in the first-order problem: it selects the retarded Green's function, and it notes explicitly that the retarded kernel is a different object from the elliptic Cauchy kernel of the analysis articles, related by the Wick rotation. The selection there is made on physical grounds, not read off the algebra, and the same is true here.

## The Biquaternion Form of the Prescription

The Feynman denominator has a compact biquaternion form. With the wave biquaternion $\tilde{k}=iE\,e_0+\mathbf p$ and its quaternion conjugate $\bar{\tilde{k}}=iE\,e_0-\mathbf p$, the quaternion product is

$$
\tilde{k}\bar{\tilde{k}}=(iE)^2+\mathbf p^2=-E^2+\mathbf p^2=-p^2 .
$$

Recomputed on the case above, $\tilde{k}\bar{\tilde{k}}=-0.49$ and $-(E_{\mathbf p}^2-\mathbf p^2)=-m^2=-0.49$, agreeing to machine precision. The mass shell is the single condition

$$
\tilde{k}\bar{\tilde{k}}=-m^2 \quad\Longleftrightarrow\quad E_{\mathbf p}^2=\mathbf p^2+m^2 ,
$$

whose two frequency branches $E=\pm E_{\mathbf p}$ are the two poles above. Inverting the relation gives the biquaternion form of the momentum-space amplitude,

$$
S_F(p)\;=\;\frac{i(\not p+m)}{p^2-m^2+i\epsilon}
\;=\;-\,\frac{i(\not p+m)}{\tilde{k}\bar{\tilde{k}}+m^2-i\epsilon},
$$

the denominator being the **deformed mass-shell operator** $\mathcal{M}(\tilde{k})=\tilde{k}\bar{\tilde{k}}+m^2$, shifted by $-i\epsilon$. The prescription is thus a deformation of the scalar on which the mass shell is defined, not an addition to the algebra.

The shift has a natural algebraic home. The deformation is $-i\epsilon\,e_0$, an element with purely imaginary scalar coefficient and zero vector part; by the definition of the material sector it lies in $\mathbb{M}_-$, and it lies in the center $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$. Written out, $-i\epsilon\,e_0$ is a displacement along the same $ict$ direction that the framework uses for the temporal coordinate of $\mathbb{M}_-$. So the algebra does three things here, and it is worth separating them:

1. it provides the complex plane in which the contour is drawn — the coefficient complex structure of $\mathbb{C}_{\mathbb{B}}$;
2. it locates the deformation direction, the $ict$ axis of $\mathbb{M}_-$;
3. it makes the undeformed mass shell a single algebraic condition $\tilde{k}\bar{\tilde{k}}=-m^2$, so that the two poles are the two branches of one equation rather than two unrelated objects.

What it does not do is choose the orientation. Replacing $\epsilon$ by $-\epsilon$ reverses the pole displacements, turning the Feynman propagator into the anti-Feynman one; replacing the opposite displacement by a common one gives the retarded or advanced propagator. All three denominators are built from the same $\tilde{k}\bar{\tilde{k}}+m^2$ and the same central $i$. The algebra cannot tell them apart, because the difference is not in the algebra; it is in which half-plane the contour closes, equivalently in which boundary condition the distribution is defined by. The $i\epsilon$ is therefore written *with* the algebra's complex structure and *lives in* its material sector, but it is not *produced* by either. The algebra names the axis; the physics chooses the direction.

The closest the complex structure comes to doing real work is the Wick rotation. In the $ict$ convention the hyperbolic operator $\Box=-\partial_t^2/c^2+\Delta$ becomes, after $t\to-i\tau$, the elliptic operator with all four directions on the same footing. The Euclidean Green's function of the elliptic operator is unique once one demands decay at infinity, and its analytic continuation back to real time is the Feynman propagator. In that route the complexification of time is exactly what makes the continuation available.

But the selection is still analytic, not algebraic. The step "continue the unique Euclidean Green's function" is the input: uniqueness rests on a decay condition in the Euclidean variables, and the direction of the rotation is a further choice, equivalent to the sign of $\epsilon$. Nothing in $\mathbb{B}$ prefers decaying-in-Euclidean over growing. So the Wick rotation exhibits the algebra's complex structure as a *necessary* carrier of the continuation, and the analytic input as the thing that fixes which continuation; it does not convert the algebra into a derivation of the Feynman prescription.

## The Propagator as a Distribution

It matters that $S_F$ is a distribution, and not only because the statement is true. The integral defining it converges for no real $p$ on the mass shell; the mass shell is precisely the pole set, and the unregulated expression $(\not p+m)/(p^2-m^2)$ is undefined there. The $i\epsilon$ is what turns the algebraic inverse of $\not p-m$ off the mass shell into a distributional inverse on all of momentum space. The propagator satisfies

$$
(i\not\partial_x-m)\,S_F(x-y)=i\,\delta^{(4)}(x-y)
$$

in the distributional sense, and this is a statement that holds for the Feynman, retarded, and advanced choices alike — because the difference between them is supported only on the mass shell and carries no additional source off it. The differential equation, therefore, does not determine the propagator. What determines it is the time-ordering prescription, which in momentum space is the contour and in configuration space is the split of support into $x^0\gtrless y^0$.

This is the sharpest way to see why the question "does the algebra supply the $i\epsilon$?" cannot be answered by finding an $i$ in the algebra. The equation of motion supplies a differential operator, and a differential operator has many distributional inverses; the algebra supplies the operator $\tilde{\nabla}$ (or its second-order companion $\tilde{\nabla}\bar{\tilde{\nabla}}$) and hence the same many inverses. Distinguishing the Feynman one requires a condition that is not an equation of motion. The complex structure enters when that condition is *represented* — as a contour in $\mathbb{C}_{\mathbb{B}}$, or as a point in the complexified time plane — and not when it is *chosen*.

## Relation to the Thermal Two-Point Function

One further structure is worth recording, because it is the place where the framework's complex time does carry a genuinely analytic condition. The companion article *The KMS Condition and the Biquaternion Framework* characterizes thermal equilibrium by the analyticity of the correlation function $F_{\hat A\hat B}(t)=\omega_\beta(\hat A\,\alpha_t(\hat B))$ in the strip $0<\mathrm{Im}(t)<\beta$, with boundary relation $F_{\hat A\hat B}(t+i\beta)=F_{\hat B\hat A}(-t)$; the imaginary-time direction is intrinsic to the material sector $\mathbb{M}_-$, and the companion quantization article shows that the anticommutator turns the boundary relation into the Fermi–Dirac distribution and the antiperiodic Matsubara frequencies $\omega_n=(2n+1)\pi/\beta$.

At finite temperature the time-ordered two-point function is not given by a vacuum contour integral but by the discrete Matsubara sum over the compact imaginary-time circle; the real-time retarded and advanced propagators still carry their own $\epsilon$ prescriptions, and they are obtained from the Matsubara sum by analytic continuation, not by an algebraic operation. The imaginary-time complexification that the algebra carries is a real feature of the thermal state — it is where the KMS analyticity lives — but it does not select the vacuum contour either. It is a consistency: the same imaginary direction that makes the mass shell algebraic is the direction in which the thermal correlation functions are analytic, and the vacuum contour is recovered as the $\beta\to\infty$ limit rather than derived from the algebra.

## What the Algebra Adds and What It Does Not

**Standard field theory, transcribed.** The mode expansion and the mode anticommutators of the companion article; the two elementary two-point functions $W_+$ and $W_-$ and their spin sums; the covariant representation of $S_F$ with its contour; the identification of the pole displacements with the Feynman, retarded, and advanced propagators; the distributional equation $(i\not\partial-m)S_F=i\delta$; and the finite-temperature reduction to the Matsubara sum. None of this is new, and none of it depends on the biquaternion structure beyond the kinematical conventions already fixed by the read-list articles.

**What the biquaternion notation provides.** The deformed mass-shell scalar $\tilde{k}\bar{\tilde{k}}+m^2-i\epsilon$; the pole set as the two branches of one algebraic condition; and the location of the deformation in the center $\mathbb{C}_{\mathbb{B}}$, along the $ict$ axis of the material sector $\mathbb{M}_-$.

**What remains open in the framework.**

- **The intrinsic operator.** Whether a genuinely $\mathbb{B}$-valued two-point function $\langle 0|T\tilde{\Psi}(X)\tilde{\Psi}^\flat(Y)|0\rangle$, paired with the trace $2\,\mathrm{Sc}(\cdot)$ or the norm form, exists and reproduces the spinor-module $S_F$. The companion quantization article leaves the intrinsic field open; this article inherits that gap.
- **Whether the algebra can *select* the contour.** We have argued that it cannot, on the ground that Feynman, retarded, and advanced differ only by boundary condition. A derivation of the Feynman prescription from an algebraic property of $\mathbb{B}$ alone would contradict that argument; we record the contrary as a possibility but do not claim it, and we have found no candidate.
- **The meaning of the $\mathbb{M}_-$ location.** That the deformation lies along the $ict$ direction may be a genuine structural fact — the same direction as the KMS strip — or an artifact of writing $\epsilon$ as a scalar. We have not distinguished the two.
- **Empirical content.** As with the rest of the framework, whether any of this yields a prediction distinguishing it from standard quantum field theory is open, and the present article changes nothing about it.

The honest summary of the algebra's role is the one we gave in the introduction. The complex structure of $\mathbb{B}$ is what makes the $i\epsilon$ writable, and it names the axis along which the deformation acts; it does not supply the orientation that defines the Feynman propagator. On this problem the biquaternion framework adds notation and a natural home for the prescription, not a derivation of it.

## Summary

The Feynman propagator of the biquaternion Dirac field is the time-ordered two-point function $S_F(x-y)=\langle 0|T\hat\psi(x)\bar{\hat\psi}(y)|0\rangle$. Its content is the contour prescription, and the prescription is fixed by time ordering together with the fermionic anticommutation sign:

$$
S_F(x-y)=i\int\!\frac{d^4p}{(2\pi)^4}\,e^{-ip\cdot(x-y)}\frac{\not p+m}{p^2-m^2+i\epsilon}.
$$

The $p^0$ integral has poles at $p^0=\pm(E_{\mathbf p}-i\epsilon/2E_{\mathbf p})$: the positive pole below the real axis and the negative pole above it. Closing below for $x^0-y^0>0$ and above for $x^0-y^0<0$ reproduces the positive- and negative-frequency pieces $W_\pm$ with the fermionic relative minus. Recomputed on $m=0.7$, $\mathbf p=(0.3,-0.9,1.1)$, the spinor identities and spin sums hold to machine precision, the poles lie on opposite sides as stated, and a direct numerical evaluation of the contour integral matches the residues to the discretization error.

Writing the wave biquaternion $\tilde{k}=iE\,e_0+\mathbf p$, so that $\tilde{k}\bar{\tilde{k}}=-p^2$, the propagator amplitude becomes

$$
S_F(p)=-\frac{i(\not p+m)}{\tilde{k}\bar{\tilde{k}}+m^2-i\epsilon},
$$

and the prescription is a deformation of the mass-shell scalar. The deformation $-i\epsilon\,e_0$ lies in the center $\mathbb{C}_{\mathbb{B}}$ and along the $ict$ axis of the material sector $\mathbb{M}_-$. The Feynman, retarded, and advanced propagators differ only in whether the two pole displacements are opposite or common; the algebra provides the complex plane and the axis of the deformation but not its orientation, which is a boundary condition on the distributional inverse. The algebra therefore adds notation and a natural home for the $i\epsilon$, not the selection of the Feynman contour.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace (fixed points of complex conjugation) |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | Center of $\mathbb{B}$ |
| $\tilde{\nabla}=e_0\partial_{ict}+\sum_k e_k\partial_k$ | Biquaternionic gradient (Dirac operator) |
| $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}$ | d'Alembertian |
| $\tilde{\Psi}$, $\tilde{\Psi}^\flat=-\tilde{\Psi}^\dagger$ | Biquaternion Dirac field and its anti-Hermitian conjugate |
| $\psi$, $\bar\psi=\psi^\dagger\gamma^0$ | Spinor-module representative and its adjoint |
| $\gamma^\mu$, $g=\mathrm{diag}(+1,-1,-1,-1)$ | Gamma matrices and Clifford metric |
| $\eta=\mathrm{diag}(-1,+1,+1,+1)=-g$ | Spacetime metric of the $ict$ gradient |
| $p^\mu=(E,\mathbf p)$, $\not p=\gamma^0E-\boldsymbol\gamma\cdot\mathbf p$ | Four-momentum and Feynman slash |
| $\hat\psi$, $\hat a_r(\mathbf p)$, $\hat b_r(\mathbf p)$ | Quantized field; particle and antiparticle modes |
| $u^{(r)}(\mathbf p),v^{(r)}(\mathbf p)$ | Positive- and negative-frequency plane-wave spinors |
| $\bar u u=2m$, $\bar v v=-2m$, $\sum_r u\bar u=\not p+m$, $\sum_r v\bar v=\not p-m$ | Parent article's normalizations and spin sums |
| $W_\pm(x-y)$ | Positive- and negative-frequency two-point functions |
| $S_F(x-y)=\langle 0|T\hat\psi(x)\bar{\hat\psi}(y)|0\rangle$ | Feynman propagator |
| $\tilde{k}=iE\,e_0+\mathbf p$ | Wave biquaternion, $\tilde{k}\bar{\tilde{k}}=-p^2$ |
| $\tilde{k}\bar{\tilde{k}}=-m^2$ | Biquaternion mass-shell condition |
| $\mathcal{M}(\tilde{k})=\tilde{k}\bar{\tilde{k}}+m^2$ | Mass-shell operator; Feynman shift $\mathcal{M}(\tilde{k})-i\epsilon$ |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace pairing |
| $\beta=\hbar/(k_BT)$, $\omega_\beta$, $\alpha_t$ | Inverse temperature, thermal state, Heisenberg evolution |
| $F_{\hat A\hat B}(t+i\beta)=F_{\hat B\hat A}(-t)$ | KMS condition |
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
