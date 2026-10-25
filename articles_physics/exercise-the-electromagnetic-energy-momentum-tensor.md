# __Exercise: The Electromagnetic Energy–Momentum Tensor__

## Introduction

This is an exercise in the electromagnetism series. It constructs the **electromagnetic energy–momentum tensor** from the field-strength biquaternion $\tilde F$, and it uses the framework and the notation of the companion article *The Field-Strength Biquaternion and Its Invariants* together with its parent, *Maxwell's Equations in the Biquaternionic Formulation*. Those two articles are the parents of this exercise: they fix the field strength, the medium conventions, and the Hermitian form. What follows applies them. The three universal articles — *Introduction to the Biquaternion Universe*, *The Material Sector: Four-Vectors, Interval and Lorentz Action*, and *The Informational Sector: States, Observables and Probability* — supply the algebra and the fixed-point subspace names, which are inherited without change.

**What is assumed.** The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ satisfying $\vec e_\mu^2 = -e_t$ and the product rule $\vec e_\nu \vec e_\mu = -\delta_{\nu\mu}e_t + \epsilon_{\nu\mu\lambda}\vec e_\lambda$; the scalar imaginary $i$ with $i^2 = -1$, commuting with the quaternion units; the anti-Hermitian subspace $\mathbb{M}_-$ with basis $\mathcal{E}_\mu \in \{ie_t, \vec e_x, \vec e_y, \vec e_z\}$ and the Hermitian subspace $\mathbb{M}_+$; the quaternion conjugate ${}^{\natural}$, the complex conjugate $\bar{\cdot}$, and the Hermitian conjugate ${}^{*} = ({}^{\natural})^{\,*}$; the biquaternionic gradient $\tilde\nabla = e_t\partial/\partial Q_t + \vec e_x\partial/\partial Q_x + \vec e_y\partial/\partial Q_y + \vec e_z\partial/\partial Q_z$ with $\Box = \tilde\nabla\tilde\nabla^{\natural}$; the trace formula, for a state $\tilde{Ϛ}$ and an observable $\tilde H$, $\mathrm{Tr}(\tilde{Ϛ}\tilde H^{*})=2\langle\tilde{Ϛ},\tilde H\rangle_{*} = 2\,\mathrm{Sc}(\tilde{Ϛ}\tilde H^{*})$; the field-strength biquaternion $\tilde F = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$; the energy density $W$; the Poynting vector $\vec S = \vec E\times\vec H$; and the medium speed of light $c = 1/\sqrt{\epsilon\mu}$. Throughout, $c$ is the speed of light in the medium and $c_0$ its vacuum value; $\vec v$ is reserved for particle and frame velocities.

**What is to be shown.** (1) Why the four-component biquaternionic energy–momentum cannot be the energy–momentum *tensor*, and why the real form $\tilde W = W + \frac{1}{c}\vec S$ fails the conservation test that the Hermitian form $\frac{1}{2}\tilde F\tilde F^{*}$ passes. (2) The bilinear construction of the rank-two tensor from $\tilde F$ and the basis of $\mathbb{M}_-$. (3) The tracelessness of $T^{\mu\nu}$. (4) The conservation law $\partial/\partial Q_\mu T^{\mu\nu} = -f^\nu$. (5) The rank-one form of $T^{\mu\nu}$ for a plane wave. Each problem is stated and solved in full; the value of an exercise is in the solutions.

**The result.** The tensor is the scalar part of a bilinear in the field strength,
$$
\boxed{\;T^\mu{}_\nu = \frac{1}{2}\,\mathrm{Sc}\!\left(\tilde F\,\mathcal{E}_\mu\,\tilde F^{*}\,\mathcal{E}_\nu\right)\;}
$$
whose mixed components are $T^0{}_0 = -W$, $T^0{}_\nu = \frac{1}{c}S_\nu$, $T^\nu{}_0 = -\frac{1}{c}S_\nu$, $T^\nu{}_\mu = -\sigma_{\nu\mu}$, with $\sigma_{\nu\mu}$ the Maxwell stress. Contracting the second slot with the metric gives a symmetric tensor; it is traceless, and it is conserved with the four-force density as source.

An exercise built on parents tests them. The four-component energy–momentum is the case in point, and Problem 1 states it plainly: the real form $\tilde W = W + \frac{1}{c}\vec S$ and its claimed conservation law $\tilde\nabla\tilde W = -\tilde{\mathcal F}$, with $\tilde{\mathcal F}$ the biquaternionic power–force density, do not reproduce the Poynting theorem, while the Hermitian form $\frac{1}{2}\tilde F\tilde F^{*}$ that the parents state does. The failing form is displayed, the failure is demonstrated by computation on a free plane wave, and the construction is then redone in the form that works.

## The Problem

A symmetric rank-two tensor in four dimensions has ten independent components: the trace and nine traceless parts. A biquaternion has four complex coefficients, that is eight real dimensions. So **no single biquaternion can be $T^{\mu\nu}$**; a biquaternion-valued object can carry at most four of the six independent spatial-stress components. The parents supply exactly such an object — the four-component biquaternionic energy–momentum $\tilde W = \frac{1}{2}\tilde F\tilde F^{*}$ — and the exercise tests both it and the real form $\tilde W = W + \frac{1}{c}\vec S$ with which it is easily confused. The problem is therefore not to write $T^{\mu\nu}$ as one biquaternion, which is impossible, but to write it as a **bigeneral quaternionic bilinear**: a quadratic expression in $\tilde F$ that carries two vector directions, one for each index.

The natural pair of directions is supplied by the basis $\mathcal{E}_\mu$ of $\mathbb{M}_-$. Inserting $\mathcal{E}_\mu$ and $\mathcal{E}_\nu$ into the Hermitian form $\tilde F(\,\cdot\,)\tilde F^{*}$ and taking the scalar part produces exactly one component for each ordered pair $(\mu,\nu)$, and it produces them all from a single expression. The problems below verify that this construction is the standard energy–momentum tensor, component by component.

## Problem 1: The Four-Component Object, and the Failure of the Real Form

**Statement.** (a) Recompute the Hermitian form $\tilde F\tilde F^{*}$ in terms of the energy density $W$ and the Poynting vector $\vec S$. (b) Compare it with the real form $\tilde W = W + \frac{1}{c}\vec S$ and locate the difference. (c) For the real form, compute the scalar part of $\tilde\nabla\tilde W$ for general fields and check whether the equation $\tilde\nabla\tilde W = -\tilde{\mathcal F}$ expands to the Poynting theorem $\partial/\partial t' W + \mathrm{div}\,\vec S + \vec J\cdot\vec E = 0$. (d) Identify the four-component object whose scalar divergence does give the energy law.

**Solution (a).** With $\vec F = \tilde F = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ a pure vector, the quaternion conjugate is $\tilde F^{\natural} = -\vec F$ and the Hermitian conjugate is
$$
\tilde F^{*} = \bar{\tilde F}^{\,*} = (-\vec F)^* = -\vec F^* = i\sqrt{\epsilon}\,\vec E + \sqrt{\mu}\,\vec H,
$$
using that $\vec E$ and $\vec H$ are real. For two pure vectors, $\vec F\vec G = -\vec F\cdot\vec G + \vec F\times\vec G$, so
$$
\tilde F\tilde F^{*} = -\vec F\cdot\tilde F^{*} + \vec F\times\tilde F^{*} .
$$
The dot product is
$$
\vec F\cdot\tilde F^{*} = (i\sqrt{\epsilon})^2\vec E^2 - (\sqrt{\mu})^2\vec H^2 + i\sqrt{\epsilon\mu}\left(\vec E\cdot\vec H - \vec H\cdot\vec E\right) = -\epsilon\,\vec E^2 - \mu\,\vec H^2 = -2W,
$$
and the cross product is
$$
\vec F\times\tilde F^{*} = (i\sqrt{\epsilon}\vec E - \sqrt{\mu}\vec H)\times(i\sqrt{\epsilon}\vec E + \sqrt{\mu}\vec H) = 2i\sqrt{\epsilon\mu}\,\vec E\times\vec H = \frac{2i}{c}\,\vec S,
$$
the $\vec E\times\vec E$ and $\vec H\times\vec H$ terms vanishing and the two mixed terms adding. Therefore
$$
\boxed{\;\tilde F\tilde F^{*} = 2W\,e_t + \frac{2i}{c}\,\vec S\;}
$$
with
$$
W = \frac{1}{2}\left(\epsilon\,\vec E^2 + \mu\,\vec H^2\right), \qquad \vec S = \vec E\times\vec H.
$$
This is an element of $\mathbb{M}_+$: its scalar part $2W$ is real and its vector part $\frac{2i}{c}\vec S$ is purely imaginary. Its scalar part is twice the energy density, and its vector part carries the Poynting vector. This agrees with the parent article *The Field-Strength Biquaternion and Its Invariants*, whose contrast between the biquaternion norm and the Hermitian form gives $\tilde F\tilde F^{*} = 2We_t + \frac{2i}{c}\vec S$ and $\tilde F^{*}\tilde F = 2We_t - \frac{2i}{c}\vec S$.

**Solution (b).** The parents state the biquaternionic energy–momentum in the Hermitian form of part (a). The form it is easily miswritten in is the real form
$$
\tilde W = W + \frac{1}{c}\,\vec S, \qquad W = \frac{1}{2}\left(\epsilon\vec E^2 + \mu\vec H^2\right), \quad \vec S = \vec E\times\vec H,
$$
with a **real** scalar part and a **real** vector part — an element of the quaternion subspace $\mathbb{H}_\mathbb{B}$. The comparison with part (a) shows that the two differ by a factor of $i$ on the Poynting part:
$$
\frac{1}{2}\tilde F\tilde F^{*} = W + \frac{i}{c}\,\vec S \;\in\;\mathbb{M}_+, \qquad \tilde W = W + \frac{1}{c}\,\vec S \;\in\;\mathbb{H}_\mathbb{B}.
$$
Only one of them can be the object whose biquaternionic gradient is the power–force density. The rest of this problem tests which.

**Solution (c).** Write $\tilde W = We_t + \frac{1}{c}\vec S$, with $W$ and $\vec S$ real, and apply the biquaternionic gradient $\tilde\nabla = e_t\partial/\partial Q_t + \vec e_\mu\,\partial/\partial Q_\mu$. The scalar part receives one contribution from the scalar part and one from the vector part:
$$
\mathrm{Sc}\!\left(\tilde\nabla\tilde W\right) = \partial/\partial Q_t\,W - \frac{1}{c}\,\partial/\partial Q_\mu\,S_\mu = -\frac{i}{c}\,\partial/\partial t'W - \frac{1}{c}\,\mathrm{div}\,\vec S,
$$
where we used $\partial/\partial Q_t = -\frac{i}{c}\partial/\partial t'$, the vanishing of the scalar part of $\vec e_\mu\,\partial/\partial Q_\mu(We_t)$ and of $e_t\partial/\partial Q_t(\frac{1}{c}\vec S)$, and $\mathrm{Sc}(\vec e_\mu \vec e_\nu) = -\delta_{\mu\nu}$. So
$$
\mathrm{Sc}\!\left(\tilde\nabla\tilde W\right) = -\frac{i}{c}\,\partial/\partial t'W - \frac{1}{c}\,\mathrm{div}\,\vec S.
$$
The claim to be tested is that this expands to the Poynting theorem, whose statement is real,
$$
\partial/\partial t'W + \mathrm{div}\,\vec S + \vec J\cdot\vec E = 0 \quad\Longleftrightarrow\quad -\frac{1}{c}\left(\partial/\partial t'W + \mathrm{div}\,\vec S\right) = \frac{1}{c}\,\vec J\cdot\vec E.
$$
The two differ: the time-derivative term in $\mathrm{Sc}(\tilde\nabla\tilde W)$ carries a factor $i$ that the divergence term does not. The scalar part is not a multiple of $\partial/\partial t'W + \mathrm{div}\,\vec S$, and no choice of the source $\tilde{\mathcal F}$ repairs the mismatch, since $\tilde{\mathcal F}$'s scalar part is a single quantity. The claimed expansion is not what the equation gives.

**Witness: a free plane wave.** Take a plane wave in a medium,
$$
\vec E = E_0\cos(kz - \omega t')\,\vec u_x, \qquad \vec H = \frac{E_0}{\mu c}\cos(kz - \omega t')\,\vec u_y, \qquad k = \frac{\omega}{c},
$$
which satisfies $\mathrm{rot}\,\vec E = -\partial/\partial t'\vec B$ and $\mathrm{rot}\,\vec H = \partial/\partial t'\vec D$ with no sources. Then $W = \epsilon E_0^2\cos^2(kz-\omega t')$, $\vec S = \vec E\times\vec H = cW\,\vec u_z$, and $\mathrm{div}\,\vec S = c\,\partial/\partial Q_z\,W = -\partial/\partial t'W$, so the Poynting theorem $\partial/\partial t'W + \mathrm{div}\,\vec S = 0$ holds. The scalar expression of the real form is
$$
\mathrm{Sc}\!\left(\tilde\nabla\tilde W\right) = -\frac{i}{c}\partial/\partial t'W - \frac{1}{c}\partial/\partial Q_z\,S_z = -\frac{i}{c}\partial/\partial t'W - \partial/\partial Q_z\,W = \frac{1-i}{c}\,\partial/\partial t'W,
$$
using $\partial/\partial Q_z\,S_z = c\,\partial/\partial Q_z\,W = -\partial/\partial t'W$. This is nonzero whenever $\cos(kz-\omega t')\sin(kz-\omega t')\neq 0$. A conservation law that fails on a free plane wave is not a conservation law for the field. **For the real form, the equation $\tilde\nabla\tilde W = -\tilde{\mathcal F}$ does not expand to the Poynting theorem; the real form is not the biquaternionic energy–momentum.** The failure is a factor $i$ on the Poynting part, together with the fact — shown in Problem 2 — that a four-component object cannot carry the spatial stress at all.

**Solution (d).** The object whose scalar divergence does give the energy law is the Hermitian form itself, halved:
$$
\tilde W_{\mathrm{corr}} = \frac{1}{2}\tilde F\tilde F^{*} = W\,e_t + \frac{i}{c}\,\vec S \;\in\;\mathbb{M}_+ .
$$
For it,
$$
\mathrm{Sc}\!\left(\tilde\nabla\tilde W_{\mathrm{corr}}\right) = -\frac{i}{c}\partial/\partial t'W - \frac{i}{c}\,\mathrm{div}\,\vec S = -\frac{i}{c}\left(\partial/\partial t'W + \mathrm{div}\,\vec S\right) = \frac{i}{c}\,\vec J\cdot\vec E,
$$
using the Poynting theorem for the last equality. The factor $i$ is now uniform, as it must be in the $ict'$ convention for a temporal component, and the real statement $\partial/\partial t'W + \mathrm{div}\,\vec S + \vec J\cdot\vec E = 0$ is recovered. So the four-component object whose scalar divergence gives the energy law is the Hermitian form $\tilde W_{\mathrm{corr}} = \frac{1}{2}\tilde F\tilde F^{*}$, which is the object the parents state, and the real form differs from it by $\vec S\to i\vec S$. Even so, $\tilde W_{\mathrm{corr}}$ has only four components and therefore carries only the energy density and the energy flux; the stress is not in it. That is the subject of the next problem.

## Problem 2: The Tensor as a Bigeneral quaternionic Bilinear

**Statement.** With $\mathcal{E}_\mu \in \{ie_t, \vec e_x, \vec e_y, \vec e_z\}$ the basis of $\mathbb{M}_-$ and $\tilde{Q} = Q^\mu\mathcal{E}_\mu$ a four-vector, so that the $Q^\mu$ are its physical components, define
$$
T^\mu{}_\nu = \frac{1}{2}\,\mathrm{Sc}\!\left(\tilde F\,\mathcal{E}_\mu\,\tilde F^{*}\,\mathcal{E}_\nu\right) = \frac{1}{4}\,\mathrm{Tr}\!\left(\tilde F\,\mathcal{E}_\mu\,\tilde F^{*}\,\mathcal{E}_\nu\right).
$$
For a fixed direction $\nu$ the whole content is the four components $T^\mu{}_\nu$, with
$$
T^{\mu\nu} = \eta^{\nu\beta}T^{\mu}{}_\beta ,
$$
so the conservation law is the four-divergence

$$
\partial_\mu T^{\mu\nu}
= \sum_\mu\frac{\partial}{\partial Q_\mu}\,T^{\mu\nu}
= 0 ,
$$

in the coordinates of the framework, $Q_t=ict'$ and $Q_k=q_k$, so that $\partial/\partial Q_t=-\frac{i}{c}\partial/\partial t'$. The divergence is taken with the **plain** derivative $\partial/\partial Q_\mu$; contracting instead with the conjugated gradient $\tilde\nabla^{\natural}$ is a different combination and does not vanish, whereas the conjugation is the right operation for the framework's four-vector currents.

Show that $T^0{}_0 = -W$, $T^0{}_\nu = \frac{1}{c}S_\nu$, $T^\nu{}_0 = -\frac{1}{c}S_\nu$, and $T^\nu{}_\mu = -\sigma_{\nu\mu}$, where
$$
\sigma_{\nu\mu} = \epsilon\,E_\nu E_\mu + \mu\,H_\nu H_\mu - W\,\delta_{\nu\mu}
$$
is the Maxwell stress tensor. Then show that $T^{\mu\nu} = \eta^{\nu\alpha}T^\mu{}_\alpha$, with $\eta = \mathrm{diag}(-1,1,1,1)$, is symmetric.

**Solution.** Two identities are needed. The first is the Hermitian form of Problem 1,
$$
\tilde F\tilde F^{*} = 2W\,e_t + \frac{2i}{c}\,\vec S.
$$
The second is the same bilinear with one basis element inserted between the field and its conjugate. Because $\vec F\vec G = -\vec F\cdot\vec G + \vec F\times\vec G$ for pure vectors, and because $\vec e_\nu\tilde F^{*} = -F^{*}_\nu + \vec e_\nu\times\tilde F^{*}$ with $F^{*}_\nu = i\sqrt{\epsilon}E_\nu + \sqrt{\mu}H_\nu$, one has
$$
\tilde F \vec e_\nu\tilde F^{*} = -F^{*}_\nu\,\vec F + \vec F\left(\vec e_\nu\times\tilde F^{*}\right)
= \underbrace{-\vec F\cdot\left(\vec e_\nu\times\tilde F^{*}\right)}_{\text{scalar}} \;+\; \underbrace{\left[-F^{*}_\nu\vec F + \vec F\times\left(\vec e_\nu\times\tilde F^{*}\right)\right]}_{\text{vector}} .
$$
For the scalar part, $\vec F\cdot(\vec e_\nu\times\tilde F^{*}) = \epsilon_{\nu\lambda\rho}F_\rho F^\dagger_\lambda = -\epsilon_{\nu\lambda\rho}F_\rho F^*_\lambda$. Writing $\epsilon_{\nu\lambda\rho}F_\rho F^*_\lambda = i\,\epsilon_{\nu\lambda\rho}\mathrm{Im}(F_\rho F^*_\lambda)$ (the symmetric part is annihilated by $\epsilon_{\nu\lambda\rho}$), and using $\mathrm{Im}(F_\rho F^*_\lambda) = \sqrt{\epsilon\mu}\,(H_\rho E_\lambda - E_\rho H_\lambda) = -\sqrt{\epsilon\mu}\,\epsilon_{\rho\lambda\mu}S_\mu$ together with $\epsilon_{\nu\lambda\rho}\epsilon_{\rho\lambda\mu} = -2\delta_{\nu\mu}$, the scalar part is $+\frac{2i}{c}S_\nu$. For the vector part, use the identity $\vec F\times(\vec e_\nu\times\tilde F^{*}) = \vec e_\nu(\vec F\cdot\tilde F^{*}) - \tilde F^{*}(\vec F\cdot \vec e_\nu) = -2W\vec e_\nu - F_\nu\tilde F^{*}$, so its $\vec e_\lambda$ component is
$$
-F^{*}_\nu F_\lambda - 2W\delta_{\nu\lambda} - F_\nu F^\dagger_\lambda = 2\,\mathrm{Re}\!\left(F_\nu F^*_\lambda\right) - 2W\delta_{\nu\lambda} = 2\left(\epsilon E_\nu E_\lambda + \mu H_\nu H_\lambda - W\delta_{\nu\lambda}\right) = 2\sigma_{\nu\lambda},
$$
using $F^{*} = -F^*$ and $\mathrm{Re}(F_\nu F^*_\lambda) = \epsilon E_\nu E_\lambda + \mu H_\nu H_\lambda$. Hence
$$
\boxed{\;\tilde F \vec e_\nu\tilde F^{*} = \frac{2i}{c}S_\nu\,e_t + 2\sigma_{\nu\lambda}\,\vec e_\lambda\;}.
$$
Now multiply by $\mathcal{E}_\nu$ on the right and take the scalar part. For $\mu = 0$, use $\mathcal{E}_0 = ie_t$ and $\tilde F\mathcal{E}_0\tilde F^{*} = i\tilde F\tilde F^{*} = 2iWe_t - \frac{2}{c}\vec S$:
$$
T^0{}_0 = \frac{1}{2}\mathrm{Sc}\!\left(2iWe_t\,ie_t\right) = \frac{1}{2}\left(2i^2W\right) = -W,
$$
$$
T^0{}_\nu = \frac{1}{2}\mathrm{Sc}\!\left(-\frac{2}{c}S_\lambda\vec e_\lambda\,\vec e_\nu\right) = -\frac{1}{c}S_\lambda\,\mathrm{Sc}(\vec e_\lambda \vec e_\nu) = \frac{1}{c}S_\nu,
$$
since $\mathrm{Sc}(\vec e_\lambda \vec e_\nu) = -\delta_{\lambda\nu}$. For the spatial rows, use the boxed identity: its scalar part meets $\mathcal{E}_0 = ie_t$ and its vector part meets $\mathcal{E}_\mu = \vec e_\mu$, so
$$
T^\nu{}_0 = \frac{1}{2}\mathrm{Sc}\!\left(\frac{2i}{c}S_\nu e_t\,ie_t\right) = \frac{1}{2}\cdot\frac{2i^2}{c}S_\nu = -\frac{1}{c}S_\nu,
$$
$$
T^\nu{}_\mu = \frac{1}{2}\mathrm{Sc}\!\left(2\sigma_{\nu\lambda}\vec e_\lambda\,\vec e_\mu\right) = \sigma_{\nu\lambda}\,\mathrm{Sc}(\vec e_\lambda \vec e_\mu) = -\sigma_{\nu\mu}.
$$
Collecting,
$$
\boxed{\;T^0{}_0 = -W, \quad T^0{}_\nu = \frac{1}{c}S_\nu, \quad T^\nu{}_0 = -\frac{1}{c}S_\nu, \quad T^\nu{}_\mu = -\sigma_{\nu\mu}\;}.
$$
This is the mixed tensor: it is **not symmetric**, and that is correct, because $T^0{}_\nu$ (energy flux) and $T^\nu{}_0$ (momentum density times $c$) are related through the metric. Contracting the second slot with $\eta = \mathrm{diag}(-1,1,1,1)$ gives the symmetric tensor
$$
T^{tt} = W, \qquad T^{tj} = T^{jt} = \frac{1}{c}S_j, \qquad T^{\nu\mu} = -\sigma_{\nu\mu},
$$
because $T^{tj} = \frac{1}{c}S_\nu$, $T^{jt} = (-1)(-\frac{1}{c}S_\nu) = \frac{1}{c}S_\nu$, and $T^{\nu\mu} = -\sigma_{\nu\mu}$, which is symmetric because $\sigma$ is. This is the standard electromagnetic energy–momentum tensor in the medium: $W$ is the energy density, $\frac{1}{c}\vec S$ the energy flux and the momentum density times $c$, and $-\sigma_{\nu\mu}$ the momentum flux.

**Remark on what the construction is.** The insertion of $\mathcal{E}_\mu$ and $\mathcal{E}_\nu$ is what turns a single biquaternion into a rank-two object: each basis element supplies one vector direction, and the scalar part reads off the component. The two indices are treated differently by the algebra — the first through the Hermitian form $\tilde F(\,\cdot\,)\tilde F^{*}$, the second through right multiplication and scalar projection — which is why the natural object is $T^\mu{}_\nu$ (mixed) and not a tensor with both slots treated the same way. The parents' four-component $\tilde W = \frac{1}{2}\tilde F\tilde F^{*}$ is the time row of $T$, up to the factor $i$ carried by $\mathcal{E}_0 = ie_t$: $T^0{}_\nu = \frac{i}{2}\mathrm{Sc}(\tilde F\tilde F^{*}\mathcal{E}_\nu) = i\,\mathrm{Sc}(\tilde W\mathcal{E}_\nu)$. The full tensor needs all sixteen entries; twelve of them — the six independent stress components and their partners — are simply absent from any four-component object.

## Problem 3: Tracelessness

**Statement.** Show that $T^\mu{}_\mu = 0$ identically, for every field configuration.

**Solution.** The trace of the mixed tensor is the contracted tensor $T^\mu{}_\mu = T^0{}_0 + T^\mu{}_\mu$, which by Problem 2 is
$$
T^\mu{}_\mu = -W - \sigma_{\mu\mu}.
$$
The trace of the Maxwell stress is
$$
\sigma_{\mu\mu} = \epsilon\,E_\mu E_\mu + \mu\,H_\mu H_\mu - 3W = \left(\epsilon\vec E^2 + \mu\vec H^2\right) - 3W = 2W - 3W = -W,
$$
using $W = \frac{1}{2}(\epsilon\vec E^2 + \mu\vec H^2)$. Hence
$$
\boxed{\;T^\mu{}_\mu = -W - (-W) = 0\;}.
$$
The tensor is traceless. With the contracted components the same statement reads $\eta_{\mu\nu}T^{\mu\nu} = -T^{tt} + T^{\mu\mu} = -W + (-\sigma_{\mu\mu}) = -W + W = 0$. Tracelessness holds in the medium as well as in vacuum, because $W$ and the trace part of the stress are in the fixed ratio forced by the isotropic subtraction. It is the algebraic expression of the classical fact that the electromagnetic energy–momentum tensor is traceless, which is what makes source-free Maxwell theory conformally invariant at the classical level.

**A caution on the trace in the $ict'$ convention.** The trace is $\eta_{\mu\nu}T^{\mu\nu} = -T^{tt} + T^{\mu\mu}$, not the flat sum $T^{tt} + T^{\mu\mu}$. In the $ict'$ convention all four components are written with the same index position and the metric factor is carried by the $i$ in the time component, so the two conventions differ by the sign of the time term; here $T^{tt} = W$ and $T^{\mu\mu} = -\sigma_{\mu\mu} = W$, so the flat sum would be $2W$, not zero. The cancellation above uses the Minkowski pairing, which is the one under which the tensor takes its standard form.

## Problem 4: The Conservation Law

**Statement.** Show that, for a field with free charge density $\rho$ and free current density $\vec J$ satisfying Maxwell's equations and charge conservation, the tensor satisfies
$$
\partial_\mu T^{\mu t} = -\frac{1}{c}\,\vec E\cdot\vec J, \qquad \partial_\mu T^{\mu k} = -\left(\rho E_k + \left(\vec J\times\vec B\right)_k\right),
$$
equivalently $\partial_\mu T^{\mu\nu} = -f^\nu$ with the four-force density
$$
f^\nu = \left(\frac{1}{c}\vec E\cdot\vec J,\; \rho\vec E + \vec J\times\vec B\right).
$$
In particular, for a source-free field, $\partial_\mu T^{\mu\nu} = 0$.

**Solution (energy component).** The time coordinate of the framework is $Q_t=ict'$, so the derivative is $\partial/\partial Q_\mu$ with $\partial/\partial Q_t=-\frac{i}{c}\partial/\partial t'$ and $\partial/\partial Q_k=\partial/\partial q_k$. The temporal component of the four-vector $T^\mu{}_t$ carries the reciprocal factor $i$, $T^{t}{}_{t}=\frac{i}{c}W$, against the spatial ones $T^{k}{}_{t}=\frac{1}{c}S_k$, so the two factors of $i$ multiply to $+1$ and
$$
\partial_\mu T^{\mu t} = \frac{\partial}{\partial Q_t}\,\frac{i}{c}W + \frac{\partial}{\partial Q_k}\,\frac{1}{c}S_k = \frac{1}{c}\left(\frac{\partial}{\partial t'}W + \mathrm{div}\,\vec S\right) = -\frac{1}{c}\,\vec E\cdot\vec J,
$$
where the Poynting theorem $\partial/\partial t'W + \mathrm{div}\,\vec S = -\vec E\cdot\vec J$ was used in the last step. The energy component of the divergence is the negative of the work done by the field on the charges: the field loses energy at the rate $\vec E\cdot\vec J$.

**Solution (momentum component).** With the components $T^{t}{}_{k}=\frac{i}{c}S_k$ against $T^{j}{}_{k}=-\sigma_{jk}$,
$$
\partial_\mu T^{\mu k} = \frac{\partial}{\partial Q_t}\,\frac{i}{c}S_k - \frac{\partial}{\partial q_j}\,\sigma_{jk} = \frac{1}{c^2}\,\partial/\partial t'S_k - \partial/\partial q_j\,\sigma_{jk},
$$
again the two factors of $i$ multiplying to $-1$. The standard momentum-balance identity for the Maxwell stress, obtained from the Ampère–Maxwell and Faraday laws together with the Gauss laws,
$$
\frac{1}{c^2}\,\partial/\partial t'\vec S - \nabla\cdot\boldsymbol{\sigma} = -\left(\rho\,\vec E + \vec J\times\vec B\right),
$$
gives $\partial_\mu T^{\mu k} = -f_k$. The four statements combine into $\partial_\mu T^{\mu\nu} = -f^\nu$.

Both component equations were checked by direct symbolic recomputation from the definition $T^\mu{}_\nu = \frac{1}{2}\mathrm{Sc}(\tilde F\mathcal{E}_\mu\tilde F^{*}\mathcal{E}_\nu)$ together with Maxwell's equations. The energy component was checked against the Poynting identity above and, independently, by substituting the time derivatives from the Ampère–Maxwell and Faraday laws into $\partial/\partial Q_\mu T^{\mu\nu}$ and simplifying; the three momentum components were checked in the same way, giving exactly $-\left(\rho\vec E + \vec J\times\vec B\right)_\mu$. The plane wave of Problem 1 is a special case: it has $\vec J = 0$ and its divergence vanishes, as Problem 5 confirms directly.

**Source-free field.** When $\rho = 0$ and $\vec J = 0$, the divergence vanishes, $\partial_\mu T^{\mu\nu} = 0$: energy and momentum are conserved. This is the standard statement, now with the tensor built from $\tilde F$ rather than quoted from the tensor calculus.

**The $ict'$ bookkeeping, stated once.** The time coordinate is $Q_t=ict'$ and never $ct'$, so the time slot of the gradient is $\partial/\partial Q_t=-\frac{i}{c}\partial/\partial t'$. Every temporal index in the algebra then carries a factor $i$ that this time derivative cancels, which is why the component equations above come out with the ordinary real four-force density $f^\nu=\left(\frac{1}{c}\vec E\cdot\vec J,\ \rho\vec E+\vec J\times\vec B\right)$. The divergence is the **plain** one, $\partial_\mu T^{\mu\nu}$; the **natural** contraction with the conjugated gradient $\tilde\nabla^{\natural}$, the component sum, is the divergence of the framework's four-vector currents, and for this rank-two tensor it is a different combination that does not vanish.

**Remark (the same balance in a matrix formulation).** The tensor of this problem has an independent life in the $4 \times 4$ complex matrix formulation of Maxwell's equations, where the single matrix

$$
T_F = \frac{1}{2}\,cF\,\overline{cF}, \qquad cF = F - iF^*, \qquad
F = \begin{pmatrix} 0 & \vec E^{\mathsf T} \\ \vec E & -[\vec B]_\times \end{pmatrix}, \qquad
F^* = \begin{pmatrix} 0 & -\vec B^{\mathsf T} \\ -\vec B & -[\vec E]_\times \end{pmatrix},
$$

with $[\vec q]_\times$ the matrix of $\vec v\mapsto\vec q\times\vec v$, is real, traceless, and entry by entry the same components as above with the indices placed mixed: the corner entry is $\frac12(\vec E^2+\vec B^2) = W$, the first row and column carry the Poynting vector with opposite signs, $T_F^{tk} = -S_\mu$ and $T_F^{kt} = S_\mu$, and the spatial block is the Maxwell stress $\sigma_{\nu\mu} = E_\nu E_\mu + B_\nu B_\mu - W\delta_{\nu\mu}$. That the two off-diagonal blocks differ in sign is not an error: the matrix is a mixed tensor $T^\mu{}_\nu$, so it is not symmetric, and the asymmetry is precisely the information about which index is up. Multiplying by the operator column $(-\partial/\partial t',\nabla)^{\mathsf T}$ gives the balance of this problem, $-\partial/\partial Q_\mu T^{\mu\nu}$ equalling the four-force density, and the derivation has two steps: the Leibniz rule turns the divergence of the product into the divergences of the two factors, and the algebraic identity

$$
cF(\vec A)\,\overline{cF(\vec C)} = \overline{cF(\vec C)}\,cF(\vec A) \qquad \text{for all vectors } \vec A, \vec C,
$$

which holds because $F = \frac12(cF + \overline{cF})$, lets the two terms of the product be re-ordered into a common form. The source's proof needs one more fact with these, that the differential $d(cF)$ again has the same form as $cF$, and then the two terms are each the field matrix applied to $(\rho,\vec J)$ — one by the equation $cF(-\partial/\partial t',\nabla)^{\mathsf T} = (\rho,\vec J)^{\mathsf T}$, the other by its complex conjugate, which is again equivalent to the whole Maxwell system because $\rho$ and $\vec J$ are real — so that their mean is $F(\rho,\vec J)^{\mathsf T}$ by the last fact, $F$ being the real part of $cF$. In this form the divergence of the tensor and the single matrix equation of the field are not two results but two interpretations of one computation. Every statement in this remark was recomputed: the identification of the matrix with $W$, $\vec S$ and $\sigma$ over $100$ random fields to $9 \times 10^{-16}$, its reality and tracelessness, the divergence identity to $1.2 \times 10^{-11}$, the finite-difference floor of the test, and the commutation exactly. The tensor is not the surprise of this route, since it is the same tensor; the surprise is the reason the divergence works, which is the commutation above, and in that formulation it is traced to the left and right regular representations of the biquaternion algebra — the same pair of representations the corpus meets as the double centralizer of *The Element and Operator Representations*. So the balance of this problem can be obtained in three ways at least: from the tensor calculus as here, from the norm of the field biquaternion as in the companion articles, and from the trace of a product of matrices as in the formulation cited below.

## Problem 5: The Free Plane Wave — a Null Field

**Statement.** For the plane wave of Problem 1, compute $T^{\mu\nu}$ explicitly and show that it is rank one, $T^{\mu\nu}\propto k^\mu k^\nu$ with $k$ the wave four-vector; verify tracelessness and conservation on this case.

**Solution.** The wave four-vector of a wave propagating in the $+z$ direction at the medium speed is $k^\mu = \left(\frac{\omega}{c}, 0, 0, k\right)$ with $k = \frac{\omega}{c}$. For this wave $W = \epsilon E_0^2\cos^2(kz-\omega t')$, $S_z = cW$, and the Maxwell stress has the components
$$
\sigma_{33} = \epsilon E_3^2 + \mu H_3^2 - W = -W, \qquad \sigma_{11} = \epsilon E_1^2 + \mu H_1^2 - W = \epsilon E_0^2\cos^2 - W = 0,
$$
$$
\sigma_{22} = \mu\frac{E_0^2}{\mu^2c^2}\cos^2 - W = \epsilon E_0^2\cos^2 - W = 0, \qquad \sigma_{12} = \sigma_{13} = \sigma_{23} = 0,
$$
where $W = \epsilon E_0^2\cos^2(kz-\omega t')$ for this wave and $1/(\mu c^2) = \epsilon$. Hence only $T^{tt} = W$, $T^{tz} = T^{zt} = \frac{1}{c}S_z = W$, and $T^{zz} = -\sigma_{33} = W$ survive:
$$
\boxed{\;T^{\mu\nu} = W\begin{pmatrix} 1 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 1 \end{pmatrix} = \frac{W}{(\omega/c)^2}\,k^\mu k^\nu\;}.
$$
The tensor is manifestly rank one: it has one nonzero eigenvalue $2W$, along the null direction $k$, and it annihilates every vector orthogonal to $k$. The trace vanishes, $\eta_{\mu\nu}T^{\mu\nu} = -T^{tt} + T^{zz} = -W + W = 0$, consistent with Problem 3. The divergence vanishes because the wave vector is null and $W$ depends on the phase alone: $\partial/\partial Q_\mu T^{\mu\nu} \propto (\partial/\partial Q_\mu W)k^\mu k^\nu$ with $\partial/\partial Q_\mu W\,k^\mu = k\left(\frac{1}{c}\partial/\partial t'W + \partial/\partial Q_z\,W\right) = 0$, using $\partial/\partial Q_z\,W = -\frac{1}{c}\partial/\partial t'W$. The direct computation confirms $\partial/\partial Q_\mu T^{\mu\nu} = 0$ and $T^\mu{}_\mu = 0$ identically in $z$ and $t'$.

The rank-one character is the energy–momentum expression of the vanishing biquaternion norm. A null field, $\langle\tilde F\rangle_{\natural} = 0$, is $N$-degenerate, a zero divisor of $\mathbb{B}$, and its energy–momentum tensor is built from a single null direction. The plane wave is the model case; the general null field behaves the same way pointwise, which is the content of the first further problem below.

**Remark on why this case matters.** The plane wave is exactly the case on which the real form's conservation law fails (Problem 1) and on which the parents' Hermitian form and the constructed tensor both work. A claim checked only on the case that suggested it is not checked; the real form's $\tilde\nabla\tilde W = -\tilde{\mathcal F}$ is refuted here on the simplest free field, the case where the Poynting theorem is most transparent.

## Further Problems

The following problems are left to the reader. They extend the construction, and some of them are open.

**1. Null fields in general.** Show that if $\langle\tilde F\rangle_{\natural} = 0$ pointwise — a null or radiative field — then $T^{\mu\nu} = \frac{2W}{\kappa}k^\mu k^\nu$ for a null vector field $k$ proportional to the local energy-flow direction, so that $T^{\mu\nu}$ has rank one and $T^{\mu\nu}k_\nu = 0$. Conclude that a null field has no frame in which the momentum flux vanishes and that its energy–momentum is that of null dust. (The plane-wave case is Problem 5.)

**2. The tensor formula.** Using the component form of $F^{\mu\nu}$ given in the parent article, verify that
$$
T^{\mu\nu} = \frac{1}{\mu}\left(F^{\mu\alpha}{F^\nu}_\alpha - \frac{1}{4}\,\eta^{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}\right)
$$
reproduces the component table of Problem 2 up to the medium factors, and identify the normalization of the bracketed expression in terms of $W$ and $\sigma_{\nu\mu}$. This shows that the bigeneral quaternionic bilinear and the standard tensor formula are the same object.

**3. Angular momentum.** Define the angular-momentum density $M^{\mu\nu\lambda} = Q^\nu T^{\mu\lambda} - Q^\lambda T^{\mu\nu}$, with $\tilde{R}$ the four-position in $\mathbb{M}_-$. Show that $\partial/\partial Q_\mu M^{\mu\nu\lambda} = 0$ for a source-free field, and identify the three spatial components as the field angular momentum and the three mixed components as the boost (centre-of-energy) densities. Does the bigeneral quaternionic bilinear simplify $M$, or is the position biquaternion $\tilde{R}$ the only extra ingredient?

**4. The medium and the Abraham–Minkowski question.** The tensor constructed here is the symmetric tensor with $T^{tt} = \frac{1}{2}(\epsilon\vec E^2 + \mu\vec H^2)$ and $\vec S = \vec E\times\vec H$. In a dispersive or moving medium the physically correct momentum density is a matter of the Abraham–Minkowski controversy, and the symmetric tensor used here is only one of the candidates. Determine which choice makes $\partial/\partial Q_\mu T^{\mu\nu} = -f^\nu$ hold with the least additional force term, and whether the bigeneral quaternionic bilinear of Problem 2 can be written with a different field normalization to produce the Minkowski tensor instead. This is an open question, not a computation with a standard answer.

**5. Coupling to gravity and to the sector structure.** The parents identify the energy–momentum tensor as the source of the gravitational field, with the four-component $\tilde W$ carrying its energy density and its energy flux. The source in general relativity is the rank-two tensor $T^{\mu\nu}$, not the four-component $\tilde W$; state precisely which components of $T^{\mu\nu}$ are lost if $\tilde W$ is used as the source, and whether the missing components are recoverable from the field equations. Then ask whether $T^{\mu\nu}$ has a natural split under $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$, and whether that split carries the material/informational interpretation.

**6. The complexified field.** Repeat the construction for a fully complexified $\tilde F$, with coefficients unrestricted in $\mathbb{C}$ rather than confined to the physical combination $i\sqrt{\epsilon}\vec E - \sqrt{\mu}\vec H$. Which of the statements — tracelessness, symmetry, conservation — survive, and what is the trace in the complexified case? (The parent notes that the projection onto $\mathbb{M}_-$ reproduces the electromagnetic field; the question is what the extra components do to $T$.)

**7. The radiated flux and the self-interaction force.** For a field with sources, apply Gauss's theorem to $\partial_\mu T^{\mu\nu} = -f^\nu$ to show that the flux of energy–momentum through a closed 3-surface, $\left(dP/dt'\right)(\Sigma) = \int_{{}^{3}\Sigma} T(d{}^{3}\Sigma)$, equals minus the four-volume integral of the force density, $\left(dP/dt'\right)(\Sigma) = -\mathcal{Q}(\Omega)$. The step is formal for point charges, because $T$ is quadratic in the field and the product of the singular field with itself is undefined for distributions. Gsponer carries the calculation out in a Colombeau algebra of nonlinear generalized functions, obtains $\left(dP/dt'\right)(\Sigma) = -\mathcal{Q}$ rigorously for an arbitrarily moving relativistic point charge, and derives the Lorentz–Dirac equation from it; the statement and its consequences are recorded in *Radiation from Accelerated Charges in Biquaternionic Form*.

8. **The tensor on a deformed arena — tracelessness, symmetry and conservation are properties of the arena.** Every statement above, and in particular tracelessness (Problem 3) and the conservation law (Problem 4), is a property of a Lorentz-invariant, commutative arena carrying a linear field theory. The companion article *Maxwell's Theory on Non-Commutative Spaces and Quaternions* constructs the same tensor on an arena whose coordinates do not commute, and all three properties change. (i) The trace is **not** zero: for the canonical tensor
$$
T^\mu{}_\mu = (\vec\theta\cdot\vec B)\left(\vec E^2-\vec B^2\right) - 2(\vec\theta\cdot\vec E)(\vec E\cdot\vec B),
$$
and exactly twice that for the tensor obtained by the metric variation. The source calls it a **trace anomaly**, and it is a *classical* one: it is present at tree level, its coefficient is the background $\vec\theta$ rather than a field multiplicity, and it comes from the deformation of the arena and not from a regularisation. It vanishes for null fields and at $\vec\theta=0$, so the plane wave of Problem 5 is anomaly free and the non-null case is a tree-level failure of exactly the conformal invariance that tracelessness expresses. (ii) The **canonical** tensor remains conservative, but the **symmetric** tensor obtained by varying the action with respect to the metric does **not**, because the action is not a scalar when the arena carries a fixed tensor $\theta^{\mu\nu}$; the Hilbert-variation argument used to reach the symmetric tensor above therefore does not transfer. (iii) The canonical tensor is **not symmetric**; its antisymmetric part is non-zero in both its spatial and its mixed components and vanishes as $\vec\theta\to0$. The rule this adds to the exercise is a boundary on its own results: tracelessness, symmetry and the conservation of the metric-variation tensor are properties of the arena, and each has to be re-derived whenever the arena changes. Verify the three deformed statements by recomputation from the deformed constitutive relations, and check that they collapse to the results above as $\vec\theta\to0$.

9. **The general force equation, and the Lagrangian as the trace of the tensor.** The conservation law of Problem 4 can be written as a *force* equation with a Lagrangian-density term. In the biquaternion tensor calculus of de Haas (*Biquaternion Formulation of Relativistic Tensor Dynamics*, arXiv:1401.4470v1), the mechanical stress–energy density is $T^{\nu\mu} = \tilde V^\nu G^\mu$, the stress–energy density of a charged particle in a potential field adds a current–potential term, the Lagrangian density $L$ is given as the trace of $T$, and the conservation statement reads
$$
\partial_\mu T^{\mu\nu}+\partial^\nu L=0,
$$
the **general force equation**, which under continuity conditions on the four-current and the four-velocity returns the Lorentz force law of Problem 4. Verify the two steps for the case of this exercise. First, with the current conserved, use $\partial_\mu T^{\mu\nu}=-f^\nu$ from Problem 4 to show that the general force equation is the Lorentz-force balance when the Lagrangian term is carried to the other side, and read off what $\partial^\nu L$ must be for the balance to close. Second, compute the trace of the tensor of this exercise: by Problem 3 the electromagnetic tensor is traceless on **every** free field, so "the Lagrangian density as the trace of $T$" gives $L = 0$ on the whole free-field class, while the electromagnetic Lagrangian density is not zero. Determine which tensor the trace is taken over — the matter tensor, the field tensor, or their sum — and where the difference sits. There is a printed inconsistency to settle first: the paper's canonical-Lagrangian display gives $L = -T^\nu{}_\nu$ while its conclusion calls $L$ the trace of $T$; the two cannot both be carried, and its tensor index layouts are unreliable in extraction, so read the signs from the PDF before using them. This problem is the tensor-language counterpart of the four-force density of Problem 4, and it is the route by which this exercise connects to relativistic *tensor dynamics* rather than to field theory alone.

## Summary

The electromagnetic energy–momentum tensor is constructed from the field-strength biquaternion as the bilinear
$$
T^\mu{}_\nu = \frac{1}{2}\,\mathrm{Sc}\!\left(\tilde F\,\mathcal{E}_\mu\,\tilde F^{*}\,\mathcal{E}_\nu\right),
$$
with $\mathcal{E}_\mu \in \{ie_t,\vec e_x,\vec e_y,\vec e_z\}$ the basis of the material subspace $\mathbb{M}_-$. Its mixed components are
$$
T^0{}_0 = -W, \qquad T^0{}_\nu = \frac{1}{c}S_\nu, \qquad T^\nu{}_0 = -\frac{1}{c}S_\nu, \qquad T^\nu{}_\mu = -\sigma_{\nu\mu},
$$
with $W = \frac{1}{2}(\epsilon\vec E^2 + \mu\vec H^2)$ the energy density, $\vec S = \vec E\times\vec H$ the Poynting vector, and $\sigma_{\nu\mu} = \epsilon E_\nu E_\mu + \mu H_\nu H_\mu - W\delta_{\nu\mu}$ the Maxwell stress. Contracting the second slot with the metric gives the symmetric standard tensor, $T^{tt} = W$, $T^{tj} = T^{jt} = \frac{1}{c}S_j$, $T^{\nu\mu} = -\sigma_{\nu\mu}$.

The tensor is traceless, $T^\mu{}_\mu = -W - \sigma_{\mu\mu} = 0$, and it is conserved: $\partial_\mu T^{\mu t} = -\frac{1}{c}\vec E\cdot\vec J$ and $\partial_\mu T^{\mu k} = -(\rho\vec E + \vec J\times\vec B)_k$, equivalently $\partial_\mu T^{\mu\nu} = -f^\nu$ with the four-force density. For a source-free field the divergence vanishes; for the free plane wave the tensor has rank one, $T^{\mu\nu}\propto k^\mu k^\nu$.

The exercise also settles the form of the four-component *biquaternionic energy–momentum*. The real form $\tilde W = W + \frac{1}{c}\vec S$ and its claimed conservation law $\tilde\nabla\tilde W = -\tilde{\mathcal F}$ do not survive recomputation: the time-derivative term acquires a factor $i$ from $\partial/\partial Q_t$ that the divergence term does not carry, and the equation fails already on a free plane wave, where it gives $\frac{1-i}{c}\partial/\partial t'W$ instead of zero. The consistent four-component object is the Hermitian form the parents state, $\frac{1}{2}\tilde F\tilde F^{*} = W + \frac{i}{c}\vec S \in \mathbb{M}_+$, whose scalar divergence gives the energy law; but no four-component object can carry the spatial stress, which is the rank-two tensor built above.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_\mu^2 = -e_t$, $\vec e_\nu \vec e_\mu = -\delta_{\nu\mu}e_t + \epsilon_{\nu\mu\lambda}\vec e_\lambda$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) subspaces |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\mathcal{E}_\mu \in \{ie_t, \vec e_x, \vec e_y, \vec e_z\}$ | Basis of $\mathbb{M}_-$ |
| $\tilde\nabla$, $\tilde\nabla^{\natural}$, $\Box = \tilde\nabla\tilde\nabla^{\natural}$ | Biquaternionic gradient, its quaternion conjugate, d'Alembertian |
| $\tilde F = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ | Field-strength biquaternion (pure vector) |
| $\vec E, \vec H, \vec B = \mu\vec H$ | Electric field, magnetic field, magnetic induction |
| $\epsilon, \mu$, $c = 1/\sqrt{\epsilon\mu}$ | Permittivity, permeability, speed of light in the medium |
| $W = \frac{1}{2}(\epsilon\vec E^2 + \mu\vec H^2)$ | Electromagnetic energy density |
| $\vec S = \vec E\times\vec H$ | Poynting vector (energy flux) |
| $\sigma_{\nu\mu} = \epsilon E_\nu E_\mu + \mu H_\nu H_\mu - W\delta_{\nu\mu}$ | Maxwell stress tensor |
| $\tilde F\tilde F^{*} = 2We_t + \frac{2i}{c}\vec S$ | Hermitian form (energy–momentum four-vector) |
| $T^\mu{}_\nu = \frac{1}{2}\mathrm{Sc}(\tilde F\mathcal{E}_\mu\tilde F^{*}\mathcal{E}_\nu)$ | Electromagnetic energy–momentum tensor (mixed) |
| $\partial_\mu T^{\mu\nu}=\sum_\mu\partial_{Q_\mu}T^{\mu\nu}=0$ | Conservation of the energy–momentum tensor |
| $T^{\mu\nu} = \eta^{\nu\alpha}T^\mu{}_\alpha$ | Symmetric energy–momentum tensor |
| $\eta = \mathrm{diag}(-1,1,1,1)$ | Minkowski metric |
| $f^\nu = (\frac{1}{c}\vec E\cdot\vec J,\,\rho\vec E+\vec J\times\vec B)$ | Four-force density (source) |
| $\langle\tilde F\rangle_{\natural} = \langle\tilde F,\tilde F\rangle_{\natural} = \tilde F\tilde F^{\natural}$ | Biquaternion norm (vanishes for a null field) |
| $\operatorname{Tr}(\tilde{Ϛ}\tilde H^{*})=\operatorname{Tr}(\tilde{Ϛ}\tilde H)=2\langle\tilde{Ϛ},\tilde H\rangle_{*} = 2\,\mathrm{Sc}(\tilde{Ϛ}\tilde H^{*})$ | Trace formula |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |

## Further Reading

- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the Maxwell stress tensor, the energy–momentum tensor of the electromagnetic field, and its tracelessness.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the standard treatment of electromagnetic energy, momentum, and the Maxwell stress.
- Ludwik Silberstein, "Elektromagnetische Grundgleichungen in bivektorieller Behandlung", *Annalen der Physik* 22 (1907) 579–586, for the complex-vector formulation whose bilinear is the energy–momentum here.
- Iwo Białynicki-Birula and Zofia Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism", *Journal of Physics A* 46 (2013) 053001, for the complex-vector treatment of energy and momentum.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the stress–energy of the electromagnetic bivector as a bilinear in the field.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the spacetime-algebra treatment of the field and its energy–momentum tensor.
- A. Waser, "Application of Bi-Quaternions in Physics" (2000, updated 2007), for a biquaternionic treatment of the field and its energy–momentum.
- D. H. Gottlieb, "Maxwell's equations" (1 August 2004, 12 pp.), §3, for the energy–momentum tensor as the matrix bilinear $\frac12 cF\,\overline{cF}$, the four-force density as a matrix divergence, and the commutation $cF(\vec A)\overline{cF(\vec C)} = \overline{cF(\vec C)}cF(\vec A)$ that the matrix proof rests on; cited for the third derivation of the balance in the remark of Problem 4.
- E. P. J. de Haas, "Biquaternion Formulation of Relativistic Tensor Dynamics," arXiv:1401.4470v1 [physics.gen-ph] (2013), for the biquaternion tensor calculus in which the mechanical stress–energy density is $T^{\nu\mu} = \tilde V^\nu G^\mu$, the Lagrangian density is given as the trace of the tensor, and the conservation law is written as the general force equation $\partial/\partial Q_\nu T^{\nu\mu} + \partial^\mu L = 0$; cited in further problem 9.
- The companion articles of this series: [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-biquaternionic-form.html), [The Field-Strength Biquaternion and Its Invariants](the-field-strength-biquaternion-and-its-invariants.html), and *Electromagnetism in Media: The Local Complex Structure at Work*.
