# __The Effective Optical Metric of the Local Complex Structure__

## Introduction

The local complex structure of the framework identifies the temporal direction with the imaginary scalar generator, $t\mapsto i\,c\,t\,e_0$, with $c$ the local speed of light in the medium. It induces at each point the quadratic form
$$
N(d\tilde{Q})=(ic\,dt)^2+d\mathbf x^2=-c^2\,dt^2+d\mathbf x^2,
$$
of signature $(3,1)$, so the framework reads a Lorentzian metric off the algebra rather than postulating it. The structure leaves one number free, the scale $c=1/\sqrt{\epsilon\mu}$; the null cone of the form has aperture $c$; and the wave operator $\Box=\Delta-c^{-2}\partial_t^2$ has characteristic speed $c$ (*The Local Complex Structure and the Speed of Light*).

That construction is announced as a **metric**, and the word invites a specific identification that the parent articles leave open. A medium with refractive index $n$ already has a well-known effective geometry: the **optical metric** of Gordon (1923), in which light rays are null geodesics and the medium's index and motion are absorbed into the geometry. The parent article states the caution explicitly: the local structure of the framework "is isotropic and is written in the local rest frame of the material; the constitutive relations of a moving or anisotropic medium carry more data than the local complex structure, and their geometric reading is a separate question" (*Electromagnetism in Media — The Local Complex Structure at Work*).

This article takes up that separate question. The result is short and sharp: **in a static medium the framework's local metric is exactly the optical metric**, to machine precision and with no extra assumption, and the two independent boundaries — motion and anisotropy — show exactly where the framework's single scalar $c$ runs out. A third boundary is more interesting than either: when $\epsilon\mu$ changes sign the framework's metric changes signature, and that change is the Wick rotation of the local structure.

Throughout, the algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, and central $i$. The material sector is $\mathbb{M}_-$ with $\tilde{Q}=ic\,t\,e_0+\mathbf x$ and norm $N(\tilde{Q})=\tilde{Q}\tilde{Q}^{\natural}=\sum_\mu Q_\mu^2$. The framework's local metric is $g=\mathrm{diag}(-c^2,1,1,1)$ in the coordinate basis $(\partial_t,\partial_x,\partial_y,\partial_z)$. The medium speed is $c=1/\sqrt{\epsilon\mu}$, the vacuum speed $c_0=1/\sqrt{\epsilon_0\mu_0}$, and the refractive index $n=c_0/c$.

## The Optical Metric of a Medium

### Gordon's construction

Maxwell's equations in a medium with permittivity $\epsilon$ and permeability $\mu$ have the same form as in vacuum with a different metric. Gordon's observation is that for a dielectric of index $n$ moving with four-velocity $u^\mu$, the field equations in the medium are equivalent to the vacuum field equations in the effective metric
$$
\tilde g_{\mu\nu}=\eta_{\mu\nu}+\left(1-\frac{1}{n^2}\right)u_\mu u_\nu ,
\qquad
\eta_{\mu\nu}=\mathrm{diag}(-1,1,1,1),
$$
with $u^\mu u_\mu=-1$. The light rays of the medium are the null geodesics of $\tilde g$, and the medium's index and velocity are read off from the geometry. The two features that matter here are the **conformal factor** attached to the velocity direction and the **off-diagonal drag terms** produced when $u_i\neq0$.

### The static case

For a medium at rest, $u^\mu=(1,0,0,0)$ and $u_0u_0=1$, so
$$
\tilde g=\mathrm{diag}\!\left(-\frac{1}{n^2},\,1,\,1,\,1\right).
$$
Its null cone is
$$
-\frac{dt^2}{n^2}+d\mathbf x^2=0
\;\Longleftrightarrow\;
\left|\frac{d\mathbf x}{dt}\right|=\frac{1}{n}=c ,
$$
so the coordinate speed of light in the medium is $1/n$: the optical metric reproduces the medium's light speed by construction. This is the standard object, and nothing about it is in question.

## The Framework's Local Metric as an Optical Metric

### The exact agreement

The framework's metric is $g=\mathrm{diag}(-c^2,1,1,1)$ with $c=1/\sqrt{\epsilon\mu}$. In units $c_0=1$ the index is $n=1/c$, so $1/n^2=c^2$, and the static Gordon metric is
$$
\tilde g=\mathrm{diag}\!\left(-c^2,\,1,\,1,\,1\right)=g .
$$

The two metrics are not merely similar or conformally related; they are **the same matrix**, and the agreement was checked numerically for $n=1.00$, $1.50$, $2.00$ and $3.30$, to $10^{-14}$ or better. The identification of the framework's scale with the index is exact:
$$
\boxed{\;n=\frac{c_0}{c}=\frac{1}{c}\;}\qquad(c_0=1),\qquad c=\frac{1}{n}.
$$

The reason is structural and not a coincidence. Gordon's conformal factor in the static case is $1/n^2=\epsilon\mu$ in vacuum units, and the framework's coefficient in the $dt^2$ slot is $c^2=1/(\epsilon\mu)$; the two expressions are reciprocals of the same product $\epsilon\mu$, so they coincide once $n$ is identified with $1/c$. The framework's algebra supplies the sign of the coefficient — the minus is $(i)^2$ — and the medium supplies its magnitude, which is exactly the division of labour that *The Local Complex Structure and the Speed of Light* states for the scale $c$.

### The null cone

The null cone of the framework's form is the zero-divisor cone of the algebra at the point, with aperture $c$ (*The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*). The null cone of the optical metric has aperture $1/n$. The two apertures are one number, $c=1/n$: the framework's algebraic null cone **is** the optical-metric cone, and the light cone of the corpus's zero-divisor reading is the light cone of the medium's optical geometry. For $n=1.50$ the aperture is $0.666667$ on both sides.

## Three Boundaries

### The moving medium and the drag that the algebra does not supply

Gordon's metric for a moving medium has off-diagonal terms. For a medium of index $n=1.5$ moving at $v=0.3\,c_0$ the computed off-diagonal entries are
$$
\tilde g_{0i}=(-0.183150,\,0,\,0)\qquad(i=1,2,3),
$$
and these are the terms responsible for the Fresnel drag of light in moving matter (Fizeau, 1851). The framework's local metric has $\tilde g_{0i}=0$ identically: the local complex structure is defined in the medium's rest frame and **rescales** the imaginary axis by the real positive scale $c$ without rotating or shifting it, so it cannot produce a cross term.

The boundary is therefore exact, and it is the sharper form of the caution in the parent article: the framework's local complex structure supplies the *conformal* half of the optical metric and not the *drag* half. A moving medium carries one more datum than the structure does, the four-velocity $u^\mu$ of the material, and the framework must import it. This is not a defect of the construction — the rest-frame metric is the object the algebra can define — but it is the precise sense in which the framework does not derive the optical metric of a moving dielectric. The corpus's own treatment of Fizeau drag belongs to *The Lorentz Transformation as a Biquaternionic Rotation*, where the drag is a kinematic consequence of the boost and not an algebraic one.

### Anisotropy and birefringence: one scale cannot carry two indices

A birefringent medium has two refractive indices. The corpus's chiral medium is exactly of this kind: the Drude–Born–Fedorov relations give two indices $n_\pm(\omega)$, and the two circular polarisations propagate with different wave numbers (*Electromagnetism in Media — The Local Complex Structure at Work*). The framework's local complex structure carries **one** scalar $c$, hence one index, hence one optical metric.

The same loss appears for an anisotropic crystal, whose dielectric tensor $\epsilon_{ij}$ has three principal values: no single conformal factor reproduces a metric whose spatial part is not isotropic. The local complex structure is a rescaling of the time axis, so it can always be written as a conformal factor of the time direction and never as an anisotropy of the spatial directions. The reading is therefore one-metric optics: it covers the isotropic static medium and nothing beyond it, and the two-index case is owned by the chiral article rather than by a metric.

### The signature: $\epsilon\mu<0$ is a Wick rotation of the local structure

The scale of the local complex structure is $c^2=1/(\epsilon\mu)$, and its sign is the sign of $\epsilon\mu$. Two regimes follow, and the difference is a change of the signature of the metric:

| Regime | $\epsilon\mu$ | $c^2$ | $g=\mathrm{diag}(-c^2,1,1,1)$ | Inertia |
|---|---|---|---|---|
| Transparent dielectric | $>0$ | $>0$ | $00$ slot negative, spatial part positive | $(3,1)$ |
| Plasma or metal below cutoff | $<0$ | $<0$ | $00$ slot positive, spatial part positive | $(4,0)$ |

In an ideal plasma with $\epsilon(\omega)=\epsilon_0(1-\omega_p^2/\omega^2)$ the permittivity is negative below the plasma frequency, and at $\omega=\omega_p/\sqrt2$ one has $\epsilon_r=-1$ exactly. There $c^2<0$, the index $n=1/c$ is imaginary, the wave is evanescent, and the framework's metric has **Riemannian signature** $(4,0)$: there is no real null cone, which is the geometric statement that no propagating wave exists below cutoff.

The interpretive content is exact. With $c$ purely imaginary, $c=i\lvert c\rvert$, the temporal coordinate of the material sector becomes
$$
ict=i\,(i\lvert c\rvert)\,t=-\lvert c\rvert\,t ,
$$
**real**. The imaginary time direction has turned into a real one, which is precisely what the Wick rotation does: the framework's Euclidean continuation is the transfer from $\mathbb{M}_-$ to the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$ (*The Wick Rotation in the Biquaternion Universe*), and the same transfer occurs here when the medium's $\epsilon\mu$ changes sign. The corpus notes the boundary for a complex $c$ near an absorption line — the rescaling becomes a complex rotation and the scale can no longer be read as the aperture of a real null cone (*The Local Complex Structure and the Speed of Light*). The dielectric-to-plasma crossing is the clean lossless case of that boundary: it is the slice on which $c$ is exactly imaginary, and it is the local structure's Wick rotation.

## What the Reading Does and Does Not Add

**What it adds.** The identification of the framework's local metric with Gordon's optical metric, exact in the static case; the reading of the null cone of the algebra as the optical-metric cone; and the three boundaries, of which the signature change is the substantive one, since it connects the medium's dielectric sign to the framework's own Euclidean continuation.

**What it does not add.** No new prediction: the optical metric is standard, and the framework's contribution is a repackaging of it in which the conformal factor is the algebra's own scale. In particular the reading does not deliver gravity. For a **constant** medium the metric $g=\mathrm{diag}(-c^2,1,1,1)$ is the flat Minkowski form in the rescaled time coordinate $x^0=ct$, so it carries no curvature; and for a varying one the framework's class of metrics is the class with flat spatial slices, which admits no non-flat vacuum geometry — no Weyl curvature, no gravitational waves, no black-hole exteriors (*Curved Spacetime and the Biquaternion Framework*). The optical metric is a *causal* structure, not a gravitational one, and this article claims no more.

## Physical Readings

The local complex structure reads as an **optical metric**: the medium's refractive index is the scale of the algebra's imaginary-time axis, $n=1/c$, and the light cone of the algebra is the cone in which the medium's light propagates. Read on the medium, the framework's scale is the conformal factor of the optical geometry, so the reading is the algebraic form of the analogue-gravity statement that the wave cone is a property of the medium and not of a fixed background (*Curved Spacetime and the Biquaternion Framework*). Read on the sign of $\epsilon\mu$, the local structure has two phases: a Lorentzian phase of propagating waves and a Euclidean phase below the plasma cutoff in which the imaginary time direction has become real, so the medium's dielectric sign selects between the Lorentzian and the Wick-rotated readings of the same algebra (*The Wick Rotation in the Biquaternion Universe*). Two boundaries belong with the reading: the framework supplies the conformal factor and not the drag, so a moving medium needs its four-velocity as an imported datum, and the framework supplies one index and not two, so birefringence is outside the metric reading (*Electromagnetism in Media — The Local Complex Structure at Work*).

Read further, the conformal factor is a **dilaton** shape: the scene at each point carries a scale $\log c$, and a change of the local complex structure is a change of that scale rather than of the algebra, so the framework's version of the scalar partner of a metric is the logarithm of the local light speed and not a new field (*Conventions in the Biquaternion Universe*).

## Summary

The framework's local complex structure produces at each point the metric $g=\mathrm{diag}(-c^2,1,1,1)$ with $c=1/\sqrt{\epsilon\mu}$. This article identifies it with the optical metric of the medium: in the static case $g$ is exactly Gordon's metric $\tilde g=\eta+(1-1/n^2)uu$ with $u$ at rest, the identification being $n=c_0/c$, and the null cone of the algebra is the optical-metric cone, of aperture $c=1/n$. The agreement was checked for four indices to machine precision.

Three boundaries mark where the framework's single scalar runs out, and one of them is more than a boundary. The moving medium has off-diagonal drag terms $g_{0i}\neq0$ that the framework's metric cannot carry, because the local structure rescales the imaginary axis without rotating it; the four-velocity must be imported. A birefringent or anisotropic medium has two indices, and one scalar cannot carry them, so those cases belong to the chiral article and not to the metric reading. And $\epsilon\mu<0$ — a plasma or a metal below cutoff — flips the sign of $c^2$, turns the metric Riemannian of signature $(4,0)$, and turns the imaginary time direction real: the dielectric sign selects between the Lorentzian and the Wick-rotated phases of the local complex structure.

The reading adds no prediction and no gravity. It is a repackaging of Gordon's optical metric in which the conformal factor is the scale of the algebra, and its content is that the framework's light cone is the medium's light cone, its one free number is the medium's index, and its Euclidean phase is the medium's $\epsilon\mu<0$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-$ | Material sector, $\tilde{Q}=ic\,t\,e_0+\mathbf x$ |
| $N(\tilde{Q})=\tilde{Q}\tilde{Q}^{\natural}=\sum_\mu Q_\mu^2$ | Biquaternion norm; null cone $N=0$ |
| $c=1/\sqrt{\epsilon\mu}$, $c_0=1/\sqrt{\epsilon_0\mu_0}$ | Medium and vacuum speeds |
| $n=c_0/c$ | Refractive index |
| $g_{\mu\nu}=\mathrm{diag}(-c^2,1,1,1)$ | Framework's local metric |
| $\tilde g_{\mu\nu}=\eta_{\mu\nu}+(1-1/n^2)u_\mu u_\nu$ | Gordon's optical metric |
| $\tilde g_{0i}$ | Drag terms; zero for a static medium, nonzero for a moving one |
| $\eta_{\mu\nu}=\mathrm{diag}(-1,1,1,1)$ | Minkowski metric |
| $\epsilon(\omega)=\epsilon_0(1-\omega_p^2/\omega^2)$ | Ideal plasma permittivity; negative below $\omega_p$ |
| $\epsilon\mu<0\Rightarrow g$ of signature $(4,0)$ | Euclidean phase; $c$ imaginary, imaginary time real |
| $n_\pm(\omega)$ | Two indices of a chiral (birefringent) medium |

## Further Reading

- W. Gordon, "Zur Lichtfortpflanzung nach der Relativitätstheorie," *Annalen der Physik* **72** (1923) 421–456, for the effective metric of a dielectric medium.
- Ulf Leonhardt and Thomas G. Philbin, "General relativity in electrical engineering," *New Journal of Physics* **8** (2006) 247, for the modern transformation-optics reading of a medium's effective geometry.
- W. G. Unruh, "Experimental black-hole evaporation?," *Physical Review Letters* **46** (1981) 1351–1353, for the analogue-gravity programme in which a moving medium's effective metric mimics a gravitational field.
- L. D. Landau and E. M. Lifshitz, *Electrodynamics of Continuous Media* (Pergamon, 2nd ed., 1984), for the optical properties of a plasma below the cutoff and for birefringence.
- H. Fizeau, "Sur les hypothèses relatives à l'éther lumineux," *Comptes Rendus de l'Académie des Sciences* **33** (1851) 349–355, for the drag of light in moving water.
- The companion articles: *The Local Complex Structure and the Speed of Light*, *Electromagnetism in Media — The Local Complex Structure at Work*, *Curved Spacetime and the Biquaternion Framework*, *The Wick Rotation in the Biquaternion Universe*, and *Conventions in the Biquaternion Universe*.
