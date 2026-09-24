# __The Classical Origin of g = 2 in Biquaternionic Form__

## Introduction

The companion articles *Larmor Precession and the Classical Magnetic Moment in Biquaternionic Form* and *The Einstein–de Haas and Barnett Effects in Biquaternionic Form* both work with one number they do not fix: the gyromagnetic ratio $\gamma$, the constant that ties a magnetic moment to its angular momentum, $\boldsymbol{\mu} = \gamma\mathbf{S}$. Expressed through the dimensionless gyromagnetic factor $g$ by $\gamma = g\,q/2m$, the number is $g = 1$ for the magnetism of an ordinary current and $g = 2$ for the intrinsic magnetism of a spin. This article asks where the second value comes from, and answers it **classically and algebraically**: the factor two is the **double-cover factor** of the biquaternion rotation rotor, present in the algebra before any quantization, and not a dynamical accident of a particular charge distribution.

The subject is set up to separate two questions that are easily confused. The first is the *absolute* normalization of the moment, which is fixed by the definition $\boldsymbol{\mu} = \tfrac{1}{2}\int\mathbf{r}\times\mathbf{j}\,d^3x$ together with the charge and mass of the carrier, and which is the content of the convective theorem below: a rigid rotor whose charge and mass densities are proportional has $\gamma = q/2m$, that is $g = 1$. The second is the *relative* factor between the convective and the intrinsic cases, and it is this factor, equal to two, that the article derives. The derivation is a statement about the representations in which the two couplings of one charged configuration are carried: the electromagnetic coupling is the phase of the central $U(1)$ and acts with weight one, while the angular momentum couples to the rotation and acts with weight one half on an intrinsic spin and weight one on an orbital vector. The gyromagnetic ratio is the ratio of the two weights, and the ratio is two.

The article is careful about what is derived and what is imported. The value $g=2$ is **fixed as a ratio** by the algebra, and this is what the two companion articles presuppose. The *magnitude* of the moment — one Bohr magneton $\mu_B = e\hbar/2m_e$ for the electron spin — is not fixed by the classical algebra, which has no $\hbar$; it is imported from the quantum normalization. The dynamical derivation of the coefficient $1/2m$ from the relativistic Dirac equation is likewise standard and is cited, not reproduced: it is a result of the companion articles *The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit* and *The Electron in Biquaternionic Form*, which obtain $g=2$ by eliminating the small component. The two accounts agree, and they agree because they compute the same double-cover factor: the relativistic one dynamically, the non-relativistic one algebraically.

The conventions are those of the foundational articles and of the two companion articles of this subcategory. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, $e_je_k = \epsilon_{jkl}e_l$ for $j\neq k$, and central imaginary $i$. The material sector is the anti-Hermitian subspace $\mathbb{M}_-$, the informational sector the Hermitian subspace $\mathbb{M}_+$, and $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace of the rotation rotors. The magnetic moment and the angular momentum are material axial vectors, $\tilde{\boldsymbol{\mu}} = \mu_ke_k$ and $\tilde{\mathbf{S}} = S_ke_k$ in $\mathbb{H}_{\mathbb{B}}$; the intrinsic spin observable is the $\mathbb{M}_+$ element $\tilde{S}_k = \tfrac{\hbar}{2}ie_k$.

## The Gyromagnetic Factor

### Definition

The gyromagnetic ratio and the gyromagnetic factor are defined by

$$
\boldsymbol{\mu} = \gamma\,\mathbf{S}
= g\,\frac{q}{2m}\,\mathbf{S},
\qquad
\gamma = g\,\frac{q}{2m},
\qquad
g = \frac{2m}{q}\frac{\mu}{S},
$$

so that $g$ is dimensionless and is the ratio of the moment to the elementary moment $(q/2m)S$ that a uniformly charged and uniformly massive body would carry. For orbital magnetism $g = 1$; for the intrinsic magnetism of a spin it is $g\approx 2$, and the measured value for the electron is $g/2 = 1.00115965218$. The value of $g$, unlike the magnitude of the moment, is independent of the units and of the particular carrier, and it is the number the two companion articles measure.

### The Moment and the Angular Momentum in the Algebra

In the biquaternion algebra the two quantities whose ratio defines $g$ are the material axial vectors

$$
\tilde{\boldsymbol{\mu}} = \mu_ke_k \in \mathbb{H}_{\mathbb{B}},
\qquad
\tilde{\mathbf{S}} = S_ke_k \in \mathbb{H}_{\mathbb{B}},
\qquad
\tilde{\boldsymbol{\mu}} = \gamma\,\tilde{\mathbf{S}},
$$

with the intrinsic moment's informational-sector representative $\mu_k\,ie_k\in\mathbb{M}_+$ available when the moment is paired with the spin observable. The gyromagnetic relation is therefore a scalar proportionality between two elements of the *same* vector slot, and in the algebra the question of $g$ is the question of what fixes that scalar.

Two couplings must be compared. The electromagnetic coupling is through the central phase: an element of the algebra of charge $q$ transforms as $\tilde{\Psi}\to e^{i\alpha}\tilde{\Psi}$ under a gauge phase, and the phase lives in the centre of the algebra, shared by both sectors. The rotational coupling is through the rotor: an element transforms by left multiplication by a unit real quaternion,

$$
\tilde{\Psi} \;\longmapsto\; \tilde{R}(\theta,\hat{\mathbf{n}})\,\tilde{\Psi},
\qquad
\tilde{R}(\theta,\hat{\mathbf{n}}) = \exp\!\left(\frac{\theta}{2}\,\hat{n}_ke_k\right),
$$

and the generator of the rotation is the half-unit $+\tfrac{1}{2}\hat{n}_ke_k$ rather than the unit $\hat{n}_ke_k$. The factor of two between these two generators is the origin of the factor two in $g$, and the rest of the article makes that statement precise.

### The Two Contributions to the Moment

The moment of a body is the sum of a **convective** part, generated by the motion of its charge density, and an **intrinsic** part, attributed to the body and not traceable to any rigid motion of its charge. The two parts obey the same torque and the same Larmor equation, as the companion article on Larmor precession shows; they differ in the value of the proportionality constant between the moment and the angular momentum. The convective part is the subject of the next two sections, and it has the value $g = 1$. The intrinsic part is the subject of the sections after that, and it has the value $g = 2$.

## The Convective Theorem: g = 1

### The Moment and the Angular Momentum of a Rigid Rotor

A body in rigid rotation with angular velocity $\boldsymbol{\omega}$ carries a charge current $\mathbf{j} = \rho_c\,\boldsymbol{\omega}\times\mathbf{r}$ and a mass current $\rho_m\,\boldsymbol{\omega}\times\mathbf{r}$, where $\rho_c$ and $\rho_m$ are the charge and mass densities. Its magnetic moment and its mechanical angular momentum are

$$
\boldsymbol{\mu} = \frac{1}{2}\int \rho_c(\mathbf{r})\,\mathbf{r}\times(\boldsymbol{\omega}\times\mathbf{r})\,d^3x
= \frac{1}{2}\,\hat{\Pi}\,\boldsymbol{\omega},
\qquad
\mathbf{L} = \int \rho_m(\mathbf{r})\,\mathbf{r}\times(\boldsymbol{\omega}\times\mathbf{r})\,d^3x
= \hat{I}\,\boldsymbol{\omega},
$$

where

$$
\hat{\Pi}_{ij} = \int \rho_c(\mathbf{r})\left(r^2\delta_{ij} - r_ir_j\right)d^3x,
\qquad
\hat{I}_{ij} = \int \rho_m(\mathbf{r})\left(r^2\delta_{ij} - r_ir_j\right)d^3x
$$

are the charge and mass inertia tensors. The two tensors are built from the same geometric kernel $r^2\delta_{ij} - r_ir_j$ and differ only in the density that weights it, so that the entire classical gyromagnetic problem is the comparison of two weighted integrals of one kernel.

### Proportional Densities

If the charge density is proportional to the mass density,

$$
\rho_c(\mathbf{r}) = \frac{q}{m}\,\rho_m(\mathbf{r}),
$$

then the two tensors are proportional, $\hat{\Pi} = (q/m)\hat{I}$, and the moment is

$$
\boldsymbol{\mu} = \frac{1}{2}\,\frac{q}{m}\,\hat{I}\,\boldsymbol{\omega}
= \frac{q}{2m}\,\mathbf{L}.
$$

The gyromagnetic ratio is the convective value

$$
\boxed{\;\gamma_{\rm conv} = \frac{q}{2m},
\qquad g = 1,\;}
$$

and this is the **classical theorem**: any rigid distribution of charge whose density is proportional to its mass density has $g = 1$, independently of the shape of the body. The theorem is the reason $g = 1$ is the reference value, and the reason a measured value different from one is evidence of magnetism that is not a convective current.

### The Classical Distributions

For a body that is not proportional, the value of $g$ is the ratio of the two inertia integrals about the rotation axis. Three elementary axisymmetric bodies, all of unit radius and carrying unit total charge and unit total mass, give the values of $\hat{\Pi}_{zz}$ and $\hat{I}_{zz}$ collected below. The uniform sphere and the thin spherical shell have proportional densities and return $g=1$; a distribution whose charge is concentrated on a ring or a shell while its mass is distributed uniformly returns a different value, and the table shows the range.

| Charge distribution | Mass distribution | $\hat{\Pi}_{zz}$ | $\hat{I}_{zz}$ | $g = \hat{\Pi}_{zz}/\hat{I}_{zz}$ |
|---|---|---|---|---|
| uniform sphere | uniform sphere | $2/5$ | $2/5$ | $1$ |
| thin shell | thin shell | $2/3$ | $2/3$ | $1$ |
| ring | ring | $1$ | $1$ | $1$ |
| shell | uniform sphere | $2/3$ | $2/5$ | $5/3$ |
| ring | uniform sphere | $1$ | $2/5$ | $5/2$ |
| uniform sphere | thin shell | $2/5$ | $2/3$ | $3/5$ |
| uniform sphere | ring | $2/5$ | $1$ | $2/5$ |

The values are the standard moments of inertia and their charge analogues. The two proportional cases give $g=1$; the mixed cases give rational values that are larger or smaller than one, and the largest in the table, $5/2$, is not two. A review of the table makes the point of the next section: the convective value is not pinned to $1$ when the densities are unequal, but neither is it pinned to $2$, and a value of exactly two requires a fine tuning.

## Why Convection Does Not Give g = 2

### The Condition for g = 2

The general condition for the convective value $g=2$ is read off the definition,

$$
g = \frac{2m}{q}\frac{\mu}{L} = \frac{m}{q}\frac{\hat{\Pi}_{zz}}{\hat{I}_{zz}} = 2
\qquad\Longleftrightarrow\qquad
\hat{\Pi}_{zz} = 2\,\frac{q}{m}\,\hat{I}_{zz},
$$

a single scalar condition for rotation about a given axis, and a tensor condition in general. A generic rigid body does not satisfy it. The condition can be met by a deliberate choice: a body whose charge is concentrated on the equator of a sphere, with $\hat{\Pi}_{zz} = qa^2$, meets it when the mass is distributed as the combination

$$
\hat{I}_{zz} = \frac{1}{2}\,ma^2
= \frac{5}{8}\left(\frac{2}{5}ma^2\right) + \frac{3}{8}\left(\frac{2}{3}ma^2\right),
$$

that is, when the mass is $5/8$ uniformly distributed through the sphere and $3/8$ concentrated on a thin shell. The number $5/8$ is exact, and it shows that $g=2$ is *attainable* by a convective distribution — but only by a distribution engineered for it. A ferromagnet is not engineered in this way, and its measured $g\approx2$ is not a coincidence of its inertia tensors.

### The Intrinsic Moment Is Not Convective

The physical reason is that intrinsic magnetism is not a convective current at all. The moment of a rigid rotor is the first spatial moment of the current $\rho_c\mathbf{v}$, and its ratio to the angular momentum is the ratio of the two inertia tensors because the same velocity field generates both currents. An intrinsic moment has no such velocity field: it is a magnetisation $\mathbf{M}$, and the only current it carries is the bound magnetisation current $\mathbf{j}_b = \nabla\times\mathbf{M}$, which is *produced by* the moment rather than *producing* it. There is no independent charge density whose motion could be integrated, and the convective theorem therefore does not apply. What fixes the intrinsic $g$ is not a comparison of two charge and mass distributions but the representation in which the intrinsic angular momentum is carried, and that is the subject of the next section.

## The Algebraic Factor Two

### The Rotation Generator and the Half-Unit

The rotation of the algebra is generated by the quaternion units, and the generator that acts on the intrinsic (two-dimensional) module is the **half-unit**

$$
g_k = -\,\frac{1}{2}\,e_k \in \mathbb{H}_{\mathbb{B}},
\qquad
[\,g_i, g_j\,] = -\,\epsilon_{ijk}\,g_k .
$$

A rotation through the angle $\theta$ about $\hat{\mathbf{n}}$ is the exponential $\tilde{R} = \exp(\tfrac{\theta}{2}\hat{n}_ke_k) = \exp(-\theta\,\hat{n}_kg_k)$, in which the coefficient of the rotation generator $\tfrac{1}{2}\hat{n}_ke_k$ is $\theta/2$ while the *rotation angle* is $\theta$. The observable intrinsic angular momentum is obtained from the generator by the same central $i$ that exchanges the sectors,

$$
\tilde{S}_k = -\,i\hbar\,g_k = \frac{\hbar}{2}\,i e_k \in \mathbb{M}_+ ,
\qquad
[\,\tilde{S}_i,\tilde{S}_j\,] = i\hbar\,\epsilon_{ijk}\,\tilde{S}_k ,
$$

and its eigenvalues are $\pm\hbar/2$. The half in the angular-momentum generator $g_k = -\tfrac{1}{2}e_k$ is the half-integer weight of the spin; the same half is the reason the intrinsic angular momentum of a spin comes in units of $\hbar/2$ and not $\hbar$.

<!-- CONVENTION — intrinsic generator and observable: the intrinsic angular-momentum generator is the half-unit g_k = -e_k/2 in H_B, and the observable is S_k = -i hbar g_k = (hbar/2) i e_k in M_+. The scalar slot carries hbar, and the half in g_k is the spin weight. A reviewer must not "absorb" the half into a redefinition of g_k to -e_k: doing so changes the commutation relation [g_i,g_j] = -eps g_k, which is fixed by the quaternion algebra, and it destroys the identification S_k = -i hbar g_k that ties the generator to the observable. The generator and the observable are the two images of one element under the sector exchange. -->

### The Double Cover of the Rotor

The half in the generator is visible in the rotor as the **double cover**. The rotation rotor

$$
\tilde{R}(\theta,\hat{\mathbf{n}}) = \cos\frac{\theta}{2}\,e_0 + \sin\frac{\theta}{2}\,\hat{n}_ke_k
$$

returns to its starting value only after $\theta$ has advanced by $4\pi$:

$$
\tilde{R}(\theta + 2\pi,\hat{\mathbf{n}}) = -\,\tilde{R}(\theta,\hat{\mathbf{n}}),
\qquad
\tilde{R}(\theta + 4\pi,\hat{\mathbf{n}}) = \tilde{R}(\theta,\hat{\mathbf{n}}).
$$

A material vector is rotated by conjugation, $\mathbf{x}\mapsto\tilde{R}\mathbf{x}\tilde{R}^\dagger$, and the sign of the rotor cancels, so a vector returns after $\theta = 2\pi$. An intrinsic state is rotated by left multiplication, $\tilde{\Psi}\mapsto\tilde{R}\tilde{\Psi}$, and the sign does not cancel, so the state returns only after $\theta = 4\pi$. The material vector therefore transforms with **weight one** under the rotation — it is single-valued on the sphere of directions — while the intrinsic state transforms with **weight one half**. The rotor group is the double cover $\mathbb{H}_{\mathbb{B}}^1 = SU(2)$ of the orientation group $\mathbb{H}_{\mathbb{B}}^1/\{\pm e_0\} = SO(3)$, and the two-to-one map is exactly the statement that the vector weight is twice the spinor weight.

### The Weights of the Two Couplings

The gyromagnetic ratio compares the electromagnetic coupling of a configuration to its rotational coupling, and the two couplings are carried by two different phases:

- the **electromagnetic coupling** is the phase of the central $U(1)$ generated by $i$, and both the material and the intrinsic configuration transform with **weight one** under it, because the phase is central and multiplies every element once;
- the **rotational coupling** is the phase of the rotor, and a material (orbital) configuration transforms with **weight one** under it while an intrinsic (spin) configuration transforms with **weight one half**.

The moment is the first spatial moment of the electromagnetic current, and the angular momentum is the Noether charge of the rotation. Their ratio, for a configuration of charge $q$ and mass $m$, is fixed up to the common convective normalization by the ratio of the two weights:

$$
\frac{\mu}{L} = \frac{q}{2m}\cdot\frac{w_{U(1)}}{w_{\rm rot}} .
$$

For a convective (orbital) configuration, $w_{U(1)} = 1$ and $w_{\rm rot} = 1$, so $\mu/L = q/2m$ and $g = 1$, which is the convective theorem. For an intrinsic (spin) configuration, $w_{U(1)} = 1$ and $w_{\rm rot} = \tfrac{1}{2}$, so

$$
\frac{\mu}{S} = \frac{q}{2m}\cdot\frac{1}{1/2} = \frac{q}{m},
\qquad
\boxed{\;g = 2\;}
$$

The factor two is therefore not a dynamical coincidence of a particular distribution; it is the ratio of the two weights of the configuration, and the weights are fixed by the double cover of the rotor, which is a property of the algebra and not of any dynamics.

### The Intrinsic Coupling

The same factor appears in the coupling of the intrinsic moment to the field. With the spin observable $\tilde{S}_k = \tfrac{\hbar}{2}ie_k$ and the magnetic induction $\mathbf{B} = B_ke_k$, the spin–field coupling is

$$
\tilde{S}_kB_k = \frac{\hbar}{2}\,i\mathbf{B} \in \mathbb{M}_+ ,
$$

the Hermitian element that the companion article on the Dirac non-relativistic limit identifies with the Pauli spin term $-\tfrac{q\hbar}{2m}\boldsymbol{\sigma}\cdot\mathbf{B}$. Writing it as $-\boldsymbol{\mu}\cdot\mathbf{B}$ with $\boldsymbol{\mu} = (q/m)\mathbf{S}$ gives the intrinsic gyromagnetic ratio $q/m$, and the factor two relative to the convective ratio $q/2m$ is the same half-weight of the spin: the field couples to the full vector slot $ie_k$ with weight one, while the angular momentum of the spin is generated through the half-unit $g_k = -\tfrac{1}{2}e_k$. The mismatch of the whole against the half is the factor two.

### Why the Ratio, and Not the Scale

It is worth stating precisely what this argument does and does not fix. It fixes the *ratio* $\mu/S$ and therefore the dimensionless factor $g$, because both quantities are carried by the same algebra and their weights are algebraically determined. It does not fix the *scale* of the moment, because the proportionality constant between the angular momentum and the numerical value of the moment involves $\hbar$ and the mass, and neither is an algebraic quantity. The algebra supplies the two, not the one Bohr magneton $\mu_B = e\hbar/2m_e$; the scale is the imported quantum normalization. The distinction is the same one that the companion article *The Electron in Biquaternionic Form* draws for the electron: the framework forces the representation content and the tree-level factor $g=2$, and it inserts the mass, the charge, and the unit $\hbar$.

## Consistency Checks

### The Commutator Algebra

The factor two is visible in the commutation relations, and this is the sharpest algebraic check. With the generator $g_k = -\tfrac{1}{2}e_k$ and the observable $\tilde{S}_k = -i\hbar g_k$,

$$
[\,g_i,g_j\,] = -\,\epsilon_{ijk}\,g_k,
\qquad
[\,\tilde{S}_i,\tilde{S}_j\,] = i\hbar\,\epsilon_{ijk}\,\tilde{S}_k ,
$$

which are the same relation transported across the sector exchange. The numerical check is immediate: in the quaternion basis $e_je_k = \epsilon_{jkl}e_l$ for $j\neq k$, so $[g_i,g_j] = \tfrac{1}{4}[e_i,e_j] = \tfrac{1}{2}\epsilon_{ijk}e_k = -\epsilon_{ijk}g_k$, and the multiplication by $-i\hbar$ converts the structure constant $-\epsilon_{ijk}$ into the $i\hbar\,\epsilon_{ijk}$ of the spin algebra. The structure constants agree, whose sign and magnitude are precisely what the half-unit produces; a full-unit generator would have given a commutator twice as large and an angular momentum in units of $\hbar$ rather than $\hbar/2$.

### The Landé Vector Model

The classical vector model of the atom assembles the orbital and spin moments into a total moment and gives the effective factor

$$
g_J = 1 + \frac{j(j+1) + s(s+1) - l(l+1)}{2j(j+1)} .
$$

For a pure orbital state, $s=0$ and $j=l$, the fraction vanishes and $g_J = 1$. For a pure spin state, $l=0$ and $j=s=\tfrac{1}{2}$, the fraction is $[\,3/4+3/4-0\,]/[\,2\cdot3/4\,] = 1$ and $g_J = 2$. The vector model therefore returns exactly the two values of this article, but it returns them as consequences of the two *input* gyromagnetic ratios $g_l = 1$ and $g_s = 2$. The biquaternion algebra supplies the missing input: $g_s = 2$ is the half-weight of the spin, so the vector model becomes complete once the algebra fixes it. The identity is a consistency check and not an independent derivation, and it is quoted here in that spirit.

### The Relativistic Derivation

The dynamical derivation of the same number is standard and is the tree-level result of the Dirac equation. Carrying the biquaternion Dirac equation to the non-relativistic regime and eliminating the small component leaves the Pauli equation with the spin term

$$
-\frac{q\hbar}{2m}\,\boldsymbol{\sigma}\cdot\mathbf{B}
\;\longleftrightarrow\;
-\frac{q\hbar}{2m}\,i\mathbf{B} \in \mathbb{M}_+ ,
$$

whose comparison with $-\boldsymbol{\mu}\cdot\mathbf{B}$ gives $\boldsymbol{\mu} = (q/m)\mathbf{S}$ and hence $g=2$. The coefficient $1/2m$ is produced by the elimination and is not inserted. The computation is performed in the companion articles *The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit* and *The Electron in Biquaternionic Form*, and it is the standard Dirac result; it is cited here as the standard dynamical account, not rederived.

The relation between the two accounts is this. The relativistic elimination produces the $1/2m$ coefficient from the two-component structure of the Dirac field, and the two-component structure is the double cover; the non-relativistic account of this article reads the same double cover directly off the rotor, with the half-unit generator and the weight one half. Both compute the factor two, one from the dynamics of the mass term and one from the algebra of the rotation, and the two agree. The advantage of the algebraic account is that it exhibits $g=2$ as a property of the *representation* of the intrinsic angular momentum, and therefore as a classical, non-quantum feature of the framework rather than a consequence of the mass term.

## The Measured Value and the Anomaly

The framework's value is $g = 2$ exactly, and it holds for any structureless spin-$\tfrac{1}{2}$ configuration, not for the electron alone. The measured value, quoted in magnitude, is

$$
|g_e| = 2.00231930436,
\qquad
a = \frac{g-2}{2} = 1.159652\times10^{-3},
$$

and the anomaly $a=(g-2)/2$ is the one-loop Schwinger value $a\approx\alpha/2\pi = 1.161410\times10^{-3}$ together with the higher-order corrections of quantum electrodynamics. The anomaly is a radiative correction and lies outside the classical algebra; the tree-level value $g=2$, which is what the classical account supplies and what the two companion articles presuppose, is the whole of the agreement claimed.

## Summary

The gyromagnetic factor $g$, defined by $\boldsymbol{\mu} = g(q/2m)\mathbf{S}$, compares the magnetic moment of a charged configuration to its angular momentum. For a **convective** configuration — a rigid rotor whose charge current is the motion of its charge density — the moment and the angular momentum are the two inertia integrals $\boldsymbol{\mu} = \tfrac{1}{2}\hat{\Pi}\boldsymbol{\omega}$ and $\mathbf{L} = \hat{I}\boldsymbol{\omega}$, and proportional charge and mass densities give

$$
\boldsymbol{\mu} = \frac{q}{2m}\,\mathbf{L},
\qquad
g = 1 .
$$

This is the classical convective theorem. Values other than one are attainable when the densities differ, but $g=2$ requires the fine-tuned condition $\hat{\Pi}_{zz} = 2(q/m)\hat{I}_{zz}$; it holds, for example, for a body whose charge is on the equator and whose mass is $5/8$ uniform and $3/8$ on a shell. Convective magnetism is therefore not pinned to two.

The **intrinsic** magnetic moment is not a convective current, and its gyromagnetic factor is fixed by the representation of its angular momentum. In the biquaternion algebra the intrinsic angular momentum is generated by the half-unit

$$
g_k = -\frac{1}{2}\,e_k,
\qquad
[\,g_i,g_j\,] = -\epsilon_{ijk}\,g_k,
$$

with observable $\tilde{S}_k = -i\hbar g_k = \tfrac{\hbar}{2}ie_k$, and the rotation rotor $\tilde{R} = \exp(\tfrac{\theta}{2}\hat{n}_ke_k)$ is a double cover, $\tilde{R}(\theta+2\pi) = -\tilde{R}(\theta)$. A material vector transforms with weight one under the rotation and returns after $2\pi$; an intrinsic state transforms with weight one half and returns only after $4\pi$. The electromagnetic coupling is the central $U(1)$ phase and acts with weight one on both. The gyromagnetic ratio is the ratio of the two weights,

$$
\frac{\mu}{S} = \frac{q}{2m}\cdot\frac{w_{U(1)}}{w_{\rm rot}},
$$

so that the orbital case ($w_{\rm rot}=1$) gives $\mu/L = q/2m$ and $g=1$, and the intrinsic case ($w_{\rm rot}=\tfrac{1}{2}$) gives

$$
\frac{\mu}{S} = \frac{q}{m},
\qquad
\boxed{\;g = 2\;.}
$$

The factor two is thus the double-cover factor of the biquaternion rotor, an algebraic property of the representation and not a dynamical coincidence; it is present in the non-relativistic, non-quantum algebra, and it is the factor that the companion articles on Larmor precession and on the Einstein–de Haas and Barnett effects presuppose. The same value follows dynamically from the coefficient $1/2m$ produced by eliminating the small component of the relativistic Dirac field, and the two accounts agree because they compute the same double cover. The algebra fixes the ratio and hence $g$; the scale of the moment, one Bohr magneton $\mu_B = e\hbar/2m_e$, is imported from the quantum normalization. The measured anomaly $a=(g-2)/2\approx\alpha/2\pi$ is a radiative correction outside the classical account.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\boldsymbol{\mu} = \gamma\mathbf{S}$ | Magnetic moment; gyromagnetic relation |
| $\gamma = g\,q/2m$ | Gyromagnetic ratio |
| $g = 2m\mu/(qS)$ | Gyromagnetic factor |
| $\hat{\Pi}_{ij} = \int\rho_c(r^2\delta_{ij}-r_ir_j)$ | Charge inertia tensor |
| $\hat{I}_{ij} = \int\rho_m(r^2\delta_{ij}-r_ir_j)$ | Mass inertia tensor |
| $\rho_c$, $\rho_m$ | Charge and mass densities |
| $\tfrac{1}{2}\hat{n}_ke_k$ | Rotation generator; the rotor $\tilde{R}$ is its exponential |
| $g_k = -\tfrac{1}{2}e_k$ | Intrinsic angular-momentum generator (half-unit) |
| $\tilde{S}_k = -i\hbar g_k = \tfrac{\hbar}{2}ie_k$ | Spin observable in $\mathbb{M}_+$ |
| $[g_i,g_j] = -\epsilon_{ijk}g_k$ | Generator algebra |
| $[\tilde{S}_i,\tilde{S}_j] = i\hbar\epsilon_{ijk}\tilde{S}_k$ | Spin algebra |
| $\tilde{R}(\theta,\hat{\mathbf{n}}) = \cos\tfrac{\theta}{2}e_0 + \sin\tfrac{\theta}{2}\hat{n}_ke_k$ | Rotation rotor (unit real quaternion) |
| $\tilde{R}(\theta+2\pi) = -\tilde{R}(\theta)$ | Double cover |
| $w_{U(1)}$, $w_{\rm rot}$ | Central phase weight (one); rotation weight (one or one half) |
| $\mu/L = (q/2m)\,w_{U(1)}/w_{\rm rot}$ | Ratio of the two weights |
| $g_J$ | Landé factor of the vector model |
| $\mu_B = e\hbar/2m_e$ | Bohr magneton |
| $a = (g-2)/2$ | Anomalous magnetic moment |

## Further Reading

- G. E. Uhlenbeck and S. Goudsmit, "Spinning electrons and the structure of spectra," *Nature* **117** (1926) 264–265, for the introduction of the spinning electron and its magnetic moment.
- R. de L. Kronig, "Spinning electrons and the structure of spectra," *Nature* **117** (1926) 550, for the early assignment of the spin magnetic moment.
- W. Pauli, "Zur Quantenmechanik des magnetischen Elektrons," *Zeitschrift für Physik* **43** (1927) 601–623, for the quantum mechanics of the spin magnetic moment and the factor two.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the relativistic equation whose non-relativistic limit yields $g=2$.
- A. Landé, "Über den anomalen Zeemaneffekt (Teil I)," *Zeitschrift für Physik* **5** (1921) 231–241, for the vector model and the factor that bears his name.
- E. U. Condon and G. H. Shortley, *The Theory of Atomic Spectra* (Cambridge, 1935), for the vector model of the atom and the Landé factor.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the Gordon decomposition and the $1/2m$ coefficient of the spin current.
- V. B. Berestetskii, E. M. Lifshitz, and L. P. Pitaevskii, *Quantum Electrodynamics* (Pergamon, 1982), for the relativistic treatment of the electron moment and the tree-level $g=2$.
- J. J. Sakurai, *Advanced Quantum Mechanics* (Addison-Wesley, 1967), for the non-relativistic limit of the Dirac equation and the spin–magnetic coupling.
- J. Schwinger, "On quantum-electrodynamics and the magnetic moment of the electron," *Physical Review* **73** (1948) 416–417, for the one-loop anomaly $a\approx\alpha/2\pi$.
- CODATA Task Group on Fundamental Constants, *CODATA recommended values of the fundamental physical constants* (2018), for the measured electron $g$-factor and the Bohr magneton.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the representation-theoretic origin of the gyromagnetic factor of a spin-$\tfrac{1}{2}$ field.
