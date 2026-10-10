# __The Local Thermal Structure: k_B as the Scale of Imaginary Time__

## Introduction

The local complex structure of the framework attaches one number to the algebraic imaginary-time direction: the local speed of light $c=1/\sqrt{\epsilon\mu}$. The imaginary phase is the algebra's fixed $i$, the scale is $c$, and the map $t\mapsto i\,c\,t\,e_0$ is what turns "the temporal direction is imaginary" into a statement about lengths. The positivity of $c$ is what makes it a rescaling of the imaginary axis rather than a rotation of it (*The Local Complex Structure and the Speed of Light*).

Thermodynamics attaches a second number to the same direction. The KMS condition says that the correlation functions of a thermal state at inverse temperature
$$
\beta=\frac{\hbar}{k_BT}
$$
extend analytically to a strip of width $\beta$ in the complex time plane, and that the imaginary-time direction is therefore periodic, with the thermal circle of circumference $\beta$ (*The KMS Condition and the Biquaternion Framework*). In the material sector's units the thermal circle has circumference $\hbar c/(k_BT)$.

The article *Action, Units, and the Constants of the Biquaternion Universe* records the resulting question as its open question 3:

> **3. Is $k_B$ a scale of the same kind as $c$?** The thermal circle has circumference $\hbar c/(k_BT)$ in the material sector's units, and its direction is the algebraic imaginary-time direction. This makes $k_B$ look like $c$: a scale attached to an imaginary coordinate, without which that coordinate has no size. Whether that parallel can be made precise — whether there is a "local thermal structure" — is open.

This article answers that question. The answer has two halves, and they point in opposite directions. **Yes**: $k_B$ is a scale attached to the same fixed algebraic direction, of the same local character as $c$, and the parallel can be made precise as a *local thermal structure* on the field of states. **No**: it is not the same kind of scale as $c$, because $c$ is required by the algebra and $k_B$ is required by no algebraic structure. The framework's thermal scale is a scale of a state, not of the algebra, and that difference is the content of the reading.

Throughout, the algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with central $i$, the material sector is $\mathbb{M}_-$ with $\tilde{Q}=ic\,t\,e_0+\mathbf x$ and norm $N(\tilde{Q})=\sum_\mu Q_\mu^2$, and the framework's local metric is $g=\mathrm{diag}(-c^2,1,1,1)$. $\hbar$ is the reduced Planck constant, $k_B$ Boltzmann's constant, $T$ the temperature and $\beta=\hbar/(k_BT)$ the inverse temperature.

## The Local Complex Structure, Recalled

Two ingredients of the local complex structure are used below, and it is worth separating them because the thermal structure will have an analogue of one and not of the other.

**The phase.** The imaginary unit is the algebra's own $i$, central, with $i^2=-1$. It is the same at every point, and it is what supplies the minus sign of the Minkowski interval: the $i^2$ of $(ic\,dt)^2$ is the signature. Nothing physical follows from the phase alone.

**The scale.** The one free number is $c$. It is what makes the statement "the temporal direction is imaginary" dimensionally meaningful, because $ict$ is a length and $t$ is a time. It is local, $c=c(\mathbf x)$ in an inhomogeneous medium, and the structure is global only in the limit in which $c$ is constant. The metric it induces is $g=\mathrm{diag}(-c^2,1,1,1)$.

The formal shape to carry away is: **a fixed algebraic direction, plus one real positive scale attached to it locally**. The scale is real and positive so that it rescales the imaginary axis rather than rotating it; the structure is pointwise rather than holomorphic; and it requires a scale, since without one the statement "the temporal direction is imaginary" has no metric content.

## The Thermal Structure of the Same Direction

The KMS condition is a statement about the *same* algebraic direction, and its scale is $\beta$. Three facts fix the parallel.

**The direction is the algebraic one.** The KMS strip is a strip in the *complex* time plane, and the direction along which the correlation functions are continued is the imaginary one — the direction of $ict$ in the material sector, spanned by the coefficient $ict$ that is imaginary by construction (*The KMS Condition and the Biquaternion Framework*). The shift $t\mapsto t+i\beta$ moves the real parameter along that algebraic direction.

**The period is $\beta$, and the length is $c\beta$.** The imaginary-time direction is compact with circumference $\beta$ *in the coordinate $t$*, so the thermal circle has circumference $c\beta=\hbar c/(k_BT)$ in the material sector's units. The identity
$$
c\beta=\frac{\hbar c}{k_BT}
$$
is exact, and it was checked numerically for $T=2.725$, $300$ and $1000\,\mathrm{K}$: the ratio $(\hbar c/k_BT)/(\beta c)$ is $1$ to twelve decimal places. So the two scales multiply, and they are independent: $c$ comes from $\epsilon\mu$ and $\beta$ from $T$.

**The same shape: a fixed direction with one real positive scale.** Here is the parallel in its sharp form. The thermal structure is *also* a fixed algebraic direction — the algebra's imaginary-time axis — with *one real positive scale attached to it locally*, namely $\beta(\mathbf x)=\hbar/(k_BT(\mathbf x))$. It is pointwise: a temperature field is a field of local scales. It is global only in equilibrium, when $T$ is constant, exactly as the local complex structure is global only when $c$ is constant. And it requires a scale: without $k_B$ the statement "the imaginary time is periodic" has no period.

## The Parallel and the Disanalogy

The parallel is now precise, and so is its limit.

| | Local complex structure | Local thermal structure |
|---|---|---|
| Fixed algebraic direction | the imaginary-time axis, phase $i$ | the imaginary-time axis, phase $i$ |
| Scale attached to it | $c=1/\sqrt{\epsilon\mu}$ | $\beta=\hbar/(k_BT)$ |
| Character of the scale | real, positive, local | real, positive, local |
| Global in the limit | $c$ constant | $T$ constant (equilibrium) |
| What the algebra requires | $c$ is required: without it the quadratic form has no length | none: the imaginary direction exists without $k_B$ |

The last row is the disanalogy, and it is decided by the role each constant plays in the algebra. The biquaternion norm on the material sector is $N(\tilde{Q})=(ic\,t)^2+\mathbf x^2$, and the scale $c$ is what gives the temporal term a physical size; without a scale the form is a formal expression in mixed units. $c$ is therefore a scale of the **algebra**: the algebra cannot state its own quadratic form without one, and the corpus records the constants article's result that $c$ "must appear for the algebra to state its own quadratic form" (*Action, Units, and the Constants of the Biquaternion Universe*).

$k_B$ is not of that kind. The imaginary-time direction exists without it; the algebra's $i$ and the material sector's $ict$ are there whether or not any temperature is defined. $k_B$ enters only when an **energy is compared with a temperature**, that is, only on a state. The corpus's own formulation is that "$k_B$ must appear for a temperature to be a time", and that the algebra cannot produce it, because a dimensionful constant is a unit conversion and not a statement about the algebra.

The consequence is the honest verdict on the open question: **$k_B$ is a scale of the same kind as $c$ at the level of a scale attached to the algebraic imaginary-time direction, and not of the same kind at the level of the algebra.** The scale of the local complex structure is data of the algebra; the scale of the thermal structure is data of a state. A local thermal structure exists, and it is a structure on the *field of states*, not on the manifold: a pointwise period, not a pointwise metric.

## The Local Thermal Structure

That distinction has a checkable consequence, because the pointwise character of the thermal scale can be exhibited.

**Tolman's law on the framework's metric.** In a static metric the local temperature satisfies $T\sqrt{-g_{00}}=\text{const}$. With the framework's $g_{00}=-c^2$ this reads
$$
T\,c=\text{const},
\qquad\text{so}\qquad
T\propto\frac{1}{c}\propto n .
$$
The local temperature is inversely proportional to the local speed of light: where the medium is optically denser, the local temperature is higher. The relation was checked directly: with a reference $T_0=300\,\mathrm{K}$ at $c_1=1$, a point at $c_2=1.5$ carries $T=200\,\mathrm{K}$, and $Tc=300$ at both points. The pointwise character is the same as that of $c$: the temperature varies from point to point precisely as the local complex structure does, and the two variations are tied by the metric.

**Two local temperatures of established physics.** The two temperatures the corpus already treats are local in exactly this sense. The **Unruh temperature** of an accelerated observer,
$$
T=\frac{\hbar\,a}{2\pi c\,k_B},
$$
is fixed by the local acceleration $a$ and the local light speed $c$, hence pointwise. The **Hawking temperature**,
$$
T_H=\frac{\hbar c^3}{8\pi G M k_B},
$$
is fixed by the local surface gravity of the horizon. Both read the same scale $\hbar/(k_BT)$ against the same algebraic imaginary-time direction, and both are owned elsewhere in the corpus (*Hawking Radiation in Biquaternionic Form*).

**The thermal circle and the Matsubara direction.** The compactness of the imaginary-time direction with period $\beta$ is what makes the Fourier modes discrete: the bosonic Matsubara frequencies are $2\pi n/\beta$ and the fermionic ones $(2n+1)\pi/\beta$. The thermal structure's scale is therefore what the spectral structure of the imaginary-time direction is measured in (*The Matsubara Formalism in Biquaternionic Form*). This is the thermal analogue of the statement that $c$ is the scale the *spatial* spectral structure of the local complex structure is measured in.

## The Wick Rotation of the Thermal Structure

The thermal structure and the framework's Euclidean continuation are two readings of one operation. The Wick rotation transfers the material sector to the real-quaternion subspace, replacing the imaginary time coordinate $ict$ by a real one (*The Wick Rotation in the Biquaternion Universe*), and the central rotation $t\mapsto e^{i\theta}t$ is the same generator read on the time coordinate (*Conventions in the Biquaternion Universe*, §*The Central Map and Its Six Restrictions*). The KMS circle is the compact form of the imaginary-time direction, and the Euclidean formulation of thermal field theory is the theory on that compact direction.

The reading is that the thermal structure is the **compactification** of the same algebraic direction that the local complex structure leaves open, and that the scale of the compactification is $\hbar/(k_BT)$. In the medium, the sign of $\epsilon\mu$ decides whether the direction is Lorentzian or Euclidean (*The Effective Optical Metric of the Local Complex Structure*); in the state, the temperature decides the period. The two are independent, and they meet in one algebra.

## What Is Established and What Is Interpretation

**Established (physics).** The KMS condition and its strip of width $\beta=\hbar/(k_BT)$; the compactness of the imaginary-time direction and the Matsubara frequencies; Tolman's law $T\sqrt{-g_{00}}=\text{const}$ in a static metric; the Unruh and Hawking temperatures; the numerical identities $c\beta=\hbar c/(k_BT)$ and $Tc=\text{const}$ on the framework's metric.

**Established (algebra).** The local complex structure with its phase $i$ and its scale $c$; the material sector with the imaginary time coordinate $ict$; the fact that the thermal direction is the same algebraic direction; the corpus's result that $c$ is required by the algebra and $k_B$ is not.

**Interpretation.** That the parallel is precise enough to be called a *local thermal structure*; that this structure lives on the field of states and not on the manifold; that the thermal structure is the compactification of the same direction the local complex structure leaves open; and that the disanalogy — algebra scale against state scale — is the answer to the open question.

**Open.** Whether the state-dependence of the thermal scale can be given an algebraic home, for instance whether the modular Hamiltonian of the state plays the role that the central imaginary plays for the algebra; and whether the local thermal structure has consequences beyond the restatement of Tolman's law and the KMS condition.

## Physical Readings

The thermal scale reads as the **local complex structure's partner on the state side**. The algebra fixes the imaginary-time direction, the medium fixes its length through $c$, and the state fixes its period through $\beta=\hbar/(k_BT)$: three data for one direction, one of them algebraic and two of them pointwise and physical. Read on the medium, the temperature is a field tied to the local light speed by Tolman's law, $T\propto1/c$, so a denser medium is locally hotter and the thermal and optical structures vary together (*The Effective Optical Metric of the Local Complex Structure*). Read on the state, the thermal scale is what the imaginary time's periodicity is measured in, so the Matsubara spectrum is the spectrum of the algebra's own imaginary direction read with the state's scale (*The Matsubara Formalism in Biquaternionic Form*). Read on the class of scales, the reading is the sharp answer to the constants article's question: $k_B$ is a scale of the same kind as $c$ as a scale *attached to the imaginary-time direction*, and not of the same kind as $c$ as a scale *required by the algebra*, because the algebra states its quadratic form only with $c$ and states its imaginary direction with no help from $k_B$ (*Action, Units, and the Constants of the Biquaternion Universe*).

## Summary

The constants article asks whether $k_B$ is a scale of the same kind as $c$. This article's answer is two-sided. The parallel can be made precise: the KMS condition attaches the scale $\beta=\hbar/(k_BT)$ to the *same* fixed algebraic imaginary-time direction that the local complex structure attaches the scale $c$ to; both scales are real, positive and local, hence pointwise, hence global only in the limiting case of a constant value; and the identity $c\beta=\hbar c/(k_BT)$ between the material-sector circumference and the coordinate period is exact, checked for three temperatures.

The disanalogy is decided by the algebra's own requirement. The biquaternion norm $(ic\,t)^2+\mathbf x^2$ needs the scale $c$ to state a length, so $c$ is a scale of the algebra; the imaginary-time direction needs no scale at all, so $k_B$ is a scale of a state. The local thermal structure therefore exists, and it is a structure on the field of states: a pointwise period, not a pointwise metric. Its pointwise character is exhibited by Tolman's law on the framework's metric, $Tc=\text{const}$, so $T\propto1/c$: the local temperature varies with the local light speed, exactly as the local complex structure does, and the two are tied by the metric. The Unruh and Hawking temperatures are the two established local temperatures of the corpus read with the same scale, and the thermal circle is the compactified form of the algebraic imaginary-time direction, the same direction whose Lorentzian-or-Euclidean character is decided in the medium by the sign of $\epsilon\mu$ and in the state by the temperature.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $i$ | Central scalar imaginary, the fixed phase of the imaginary-time direction |
| $\mathbb{M}_-$ | Material sector, $\tilde{Q}=ic\,t\,e_0+\mathbf x$ |
| $N(\tilde{Q})=(ic\,t)^2+\mathbf x^2$ | Biquaternion norm; needs the scale $c$ to have a length |
| $c=1/\sqrt{\epsilon\mu}$ | Local speed of light: the algebra's scale |
| $g_{\mu\nu}=\mathrm{diag}(-c^2,1,1,1)$ | Framework's local metric |
| $\beta=\hbar/(k_BT)$ | Inverse temperature: the state's scale |
| $c\beta=\hbar c/(k_BT)$ | Thermal circle in the material sector's units |
| $Tc=\text{const}$ | Tolman's law on the framework's metric; $T\propto1/c\propto n$ |
| $T=\hbar a/(2\pi c\,k_B)$ | Unruh temperature: a local temperature |
| $T_H=\hbar c^3/(8\pi G M k_B)$ | Hawking temperature: a local temperature |
| $\omega_n=2\pi n/\beta$, $(2n+1)\pi/\beta$ | Bosonic and fermionic Matsubara frequencies |

## Further Reading

- R. Tolman, "On the weight of heat and thermal equilibrium in general relativity," *Physical Review* **35** (1930) 904–924, and R. Tolman and P. Ehrenfest, "Temperature equilibrium in a static gravitational field," *Physical Review* **36** (1930) 1791–1798, for the pointwise character of temperature in a static field.
- W. G. Unruh, "Notes on black-hole evaporation," *Physical Review D* **14** (1976) 870–892, for the Unruh temperature.
- S. W. Hawking, "Particle creation by black holes," *Communications in Mathematical Physics* **43** (1975) 199–220, for the Hawking temperature.
- R. Haag, N. M. Hugenholtz, and M. Winnink, "On the equilibrium states in quantum statistical mechanics," *Communications in Mathematical Physics* **5** (1967) 215–236, for the KMS characterization of equilibrium.
- M. Le Bellac, *Thermal Field Theory* (Cambridge, 1996), for the imaginary-time formalism and the Matsubara frequencies.
- The companion articles: *Action, Units, and the Constants of the Biquaternion Universe* (the open question this article answers), *The Local Complex Structure and the Speed of Light*, *The Effective Optical Metric of the Local Complex Structure*, *The KMS Condition and the Biquaternion Framework*, *The Matsubara Formalism in Biquaternionic Form*, *The Wick Rotation in the Biquaternion Universe*, and *Hawking Radiation in Biquaternionic Form*.
