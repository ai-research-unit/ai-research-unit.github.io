# __Exercise: Plane-Wave Propagation in a Medium__

## Introduction

This is an exercise in the electromagnetism series. It applies the conventions of *Electromagnetism in Media — The Local Complex Structure at Work*, the article that fixes the medium objects and whose plane-wave section declares that it "fixes the conventions for the later exercise on plane-wave propagation in a medium". The exercise uses the field-strength biquaternion, the source, the medium speed and impedance, and the medium gradient exactly as that article fixes them, with the algebra of the three universal articles and of *Maxwell's Equations in the Biquaternionic Formulation* inherited unchanged. Nothing is renamed and nothing is rederived from the algebra; what is rederived is what the parent asserts about a plane wave.

**What is assumed.** The algebra, the sectors, the conjugations, the gradient and the d'Alembertian are those of *Algebra and Element Conventions*, *Operator and Calculus Conventions* and *Frame and Metric Conventions*, and none is restated here. The field-strength biquaternion $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ (a pure vector), the four-current $\tilde J_{\Phi} = ic\rho\,e_t + \vec J$, whose normalised source is $\sqrt{\mu}\,\tilde J_{\Phi} = \frac{i\rho}{\sqrt{\epsilon}}e_t + \sqrt{\mu}\,\vec J$, the Maxwell equation $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}_{\Phi}$, the potential $\tilde{A}_{\Phi} = i\,a'_te_t + \vec A$, and the medium speed and impedance
$$
c = \frac{1}{\sqrt{\epsilon\mu}}, \qquad Z = \sqrt{\frac{\mu}{\epsilon}}, \qquad c_0 = \frac{1}{\sqrt{\epsilon_0\mu_0}}, \qquad n(\omega) = \frac{c_0}{c(\omega)};
$$
the constitutive relations $\vec D = \epsilon\vec E$ and $\vec B = \mu\vec H$, so that $\vec H = \vec B/\mu$; the Riemann–Silberstein combination $\tilde{F} = i\sqrt{\epsilon}\,\vec N$ with $\vec N = \vec E + ic\vec B$; the energy density $W = \frac{1}{2}(\epsilon\,\vec E^2 + \mu\,\vec H^2)$, the Poynting vector $\vec S = \vec E\times\vec H$, and the halved Hermitian form
$$
\tilde{W}_{\Psi} = \frac{1}{2}\tilde{F}\tilde{F}^{*} = W\,e_t + \frac{i}{c}\,\vec S;
$$
and the Hermitian form with its trace reading is that of *Norm and Pairing Conventions*, with the star inert on $\mathbb{B}_{\Psi}$ and the unstarred trace $\operatorname{Tr}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi)$ real, and non-negative when $\tilde R_\Psi\ge0$. Throughout, $c$ is the speed of light in the medium and $c_0$ its vacuum value; $\vec v$ is reserved for particle and frame velocities. 

**What is to be shown.** Five things. (1) The four algebraic plane-wave conditions the parent states, and the dispersion relation $k_\Phi = \omega/c$, follow from the single biquaternionic equation $\tilde{\nabla}\tilde{F} = 0$. (2) The amplitude $\tilde{F}_0$ is a null field, hence a zero divisor, and it is annihilated by the (null) four-wavevector biquaternion. (3) The impedance relation and the balance of the two normalised halves of $\tilde{F}_0$. (4) The energy density, the energy flux, their time averages, and the energy–momentum biquaternion of the wave. (5) The dispersive case: phase velocity, group velocity, the spectral complex structure, and the vacuum limit. Each problem is stated and solved in full, and the exercise closes by naming what the parent does not establish.

**The result.** For a source-free monochromatic plane wave
$$
\tilde{F}(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z,r'_t) = \tilde{F}_0\,\exp(\,i(\vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)-\omega r'_t/c)),
\qquad
\tilde{F}_0 = i\sqrt{\epsilon}\,\vec E_0 - \sqrt{\mu}\,\vec H_0,
$$
the equation $\tilde{\nabla}\tilde{F} = 0$ reduces to
$$
\vec k_\Phi\cdot\vec E_0 = 0, \qquad \vec k_\Phi\cdot\vec H_0 = 0, \qquad \vec k_\Phi\times\vec E_0 = \omega\mu\,\vec H_0, \qquad \vec k_\Phi\times\vec H_0 = -\omega\epsilon\,\vec E_0
$$
and, for a nonzero field, these force the dispersion relation
$$
\vec k_\Phi^2 = \omega^2\epsilon\mu = \frac{\omega^2}{c^2}
$$
and then $\vec H_0 = Z^{-1}\,\vec u_\eta\times\vec E_0$, with $\vec u_\eta = \vec k_\Phi/|\vec k_\Phi|$. The amplitude satisfies $|\vec E_0| = Z|\vec H_0| = c|\vec B_0|$, the two normalised halves $i\sqrt{\epsilon}\,\vec E_0$ and $-\sqrt{\mu}\,\vec H_0$ have equal magnitude, and the field-strength amplitude is null,
$$
\langle\tilde{F}_0\rangle_{\natural} = \sum_{\eta=1}^{3}(F_{t\eta})^2 = 0,
$$
so a free plane wave in a medium is $N$-degenerate, a zero divisor of $\mathbb{B}$, exactly as the parent states.

An exercise built on parents tests them. The parent states the conditions above and the nullness without deriving them, so the exercise derives them from $\tilde{\nabla}\tilde{F}=0$ and then checks them on cases the parent did not use: oblique propagation, elliptical polarisation, and media with $\epsilon \neq \mu$. The parent's plane-wave results survive all of them. The exercise also records what the parent leaves open: a restricted real normalisation, an energy expression that is non-dispersive, and a label — "Lorentz invariants" — that the parent's own medium setting does not establish. These are collected in the section *Where the Parent Leaves a Gap*, and none of them is smoothed over.

## The Problem

The parent's plane-wave section fixes the conventions and quotes the consequences. The problem here is to *apply* them: to take the single biquaternionic Maxwell equation with no source, substitute the plane-wave ansatz, and obtain every downstream statement by computation rather than by quotation. The natural objects are the ones the parent fixes — the field-strength biquaternion $\tilde{F}$, the medium speed $c$, the impedance $Z$, the Riemann–Silberstein vector $\vec N$ — and the natural operator is $\tilde{\nabla}$ with its medium entry $\partial/\partial R_t = -i\partial/\partial r'_t$.

The calculation is an eigenvalue problem. A plane wave is an eigenfunction of every $\partial/\partial R_\mu$, so $\tilde{\nabla}$ acts on it by left multiplication by a constant biquaternion, and $\tilde{\nabla}\tilde{F} = 0$ becomes a purely algebraic annihilation condition. That condition is what the exercise solves, and the four conditions and the dispersion relation fall out of its scalar and vector parts.

Two points of discipline are kept in view. First, the field strength is a pure vector with **complex** amplitude components, so every condition must be read as a complex equation and every amplitude relation as a modulus relation; checking only a linearly polarised real wave would test a case narrower than the algebra. Second, the parent is treated as a source of assertions until the computation has been done, and the computation is run on a case other than the one that suggested the statement.

## Problem 1: The Plane-Wave Conditions and the Dispersion Relation

**Statement.** (a) With the ansatz $\tilde{F} = \tilde{F}_0\,\exp(i(\vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)-\omega r'_t/c))$ and $\tilde{F}_0$ a pure vector, show that the gradient acts by left multiplication by a constant biquaternion, and identify it. (b) Show that $\tilde{\nabla}\tilde{F} = 0$ is equivalent to the four conditions of the parent and to the dispersion relation $k_\Phi = \omega/c$. (c) Derive the impedance relation and the amplitude relations $|\vec E_0| = Z|\vec H_0| = c|\vec B_0|$.

**Solution (a).** The partial derivatives act on the exponential by
$$
\partial/\partial R_t\,\exp(\,i(\vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)-\omega r'_t/c)) = -\frac{\omega}{c}\,\exp(\,i(\vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)-\omega r'_t/c)),
\qquad
\partial/\partial R_j\,\exp(\,i(\vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)-\omega r'_t/c)) = i k_j\,\exp(\,i(\vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)-\omega r'_t/c)),
$$
using $\partial/\partial R_t = -i\partial/\partial r'_t$ and $\partial/\partial r'_t \to -i\omega/c$. Hence
$$
\tilde{\nabla}\tilde{F} = \left(-\frac{\omega}{c}\,e_t + i\vec k_\Phi\right)\tilde{F}_0\,\exp(\,i(\vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)-\omega r'_t/c)),
\qquad
\vec k_\Phi = k_{\Phi x}\vec e_x + k_{\Phi y}\vec e_y + k_{\Phi z}\vec e_z .
$$
The bracket is $i\tilde P_{\Phi}$, where
$$
\tilde P_{\Phi} = \frac{i\omega}{c}\,e_t + \vec k_\Phi
$$
is exactly the **four-wavevector** of the material space, whose scalar part $i\omega/c$ is purely imaginary and whose vector part $\vec k_\Phi$ is real, so that $\tilde P_{\Phi} \in \mathbb{B}_{\Phi}$. The operator eigenvalue identity is therefore
$$
\tilde{\nabla} \;\longrightarrow\; i\tilde P_{\Phi} = -\frac{\omega}{c}\,e_t + i\vec k_\Phi,
$$
and since $i$ is central and invertible, the source-free equation $\tilde{\nabla}\tilde{F} = 0$ is equivalent to the algebraic condition
$$
\boxed{\;\tilde P_{\Phi}\,\tilde{F}_0 = 0\;}.
$$

**Solution (b).** Write $\tilde{F}_0 = F_{tx}\vec e_x + F_{ty}\vec e_y + F_{tz}\vec e_z$. Because $\tilde P_{\Phi}$ has a scalar part and $\tilde{F}_0$ is a pure vector, the product separates by parts. For a scalar $\kappa$ and a vector $\vec q$, $\kappa\tilde{F}_0 = \kappa F_{t\eta}\vec e_\eta$ distributes over components, while the vector part of $\tilde P_{\Phi}$ multiplies by the quaternion rule $\vec k_\Phi\tilde{F}_0 = -\vec k_\Phi\cdot\tilde{F}_0 + \vec k_\Phi\times\tilde{F}_0$. Thus
$$
\tilde P_{\Phi}\tilde{F}_0 = \frac{i\omega}{c}\,\tilde{F}_0 - \vec k_\Phi\cdot\tilde{F}_0 + \vec k_\Phi\times\tilde{F}_0 .
$$
Its scalar part and its vector part must vanish separately:
$$
\vec k_\Phi\cdot\tilde{F}_0 = 0,
\qquad
\vec k_\Phi\times\tilde{F}_0 = -\frac{i\omega}{c}\,\tilde{F}_0 .
$$

Now substitute $\tilde{F}_0 = i\sqrt{\epsilon}\,\vec E_0 - \sqrt{\mu}\,\vec H_0$ into the vector equation. The left side is $i\sqrt{\epsilon}\,\vec k_\Phi\times\vec E_0 - \sqrt{\mu}\,\vec k_\Phi\times\vec H_0$, and the right side is $\frac{\omega}{c}\sqrt{\epsilon}\,\vec E_0 + \frac{i\omega}{c}\sqrt{\mu}\,\vec H_0$. Since $\sqrt{\epsilon}$ and $\sqrt{\mu}$ are real, separating the real and imaginary parts gives the two relations
$$
\sqrt{\epsilon}\,\vec k_\Phi\times\vec E_0 = \frac{\omega}{c}\sqrt{\mu}\,\vec H_0,
\qquad
-\sqrt{\mu}\,\vec k_\Phi\times\vec H_0 = \frac{\omega}{c}\sqrt{\epsilon}\,\vec E_0 .
$$
Using $c = 1/\sqrt{\epsilon\mu}$, the coefficients are $\frac{\omega\sqrt{\mu}}{c\sqrt{\epsilon}} = \omega\mu$ and $\frac{\omega\sqrt{\epsilon}}{c\sqrt{\mu}} = \omega\epsilon$, so
$$
\vec k_\Phi\times\vec E_0 = \omega\mu\,\vec H_0,
\qquad
\vec k_\Phi\times\vec H_0 = -\omega\epsilon\,\vec E_0,
$$
which are the parent's two curl conditions. Dotting the first with $\vec k_\Phi$ kills the left side and gives $\omega\mu\,\vec k_\Phi\cdot\vec H_0 = 0$, so $\vec k_\Phi\cdot\vec H_0 = 0$; dotting the second gives $\vec k_\Phi\cdot\vec E_0 = 0$. The transversality conditions of the parent's list are therefore consequences of the curl relations, not independent inputs, and the scalar equation $\vec k_\Phi\cdot\tilde{F}_0 = 0$ is then automatic.

Finally, take $\vec k_\Phi\times(\vec k_\Phi\times\vec E_0)$. Expanding the double cross product, and using $\vec k_\Phi\cdot\vec E_0 = 0$, gives $-k_\Phi^2\,\vec E_0$; substituting the first curl relation and then the second gives $\vec k_\Phi\times(\omega\mu\vec H_0) = \omega\mu(\vec k_\Phi\times\vec H_0) = -\omega^2\epsilon\mu\,\vec E_0$. Equating the two expressions,
$$
-k_\Phi^2\vec E_0 = -\omega^2\epsilon\mu\,\vec E_0
\quad\Longrightarrow\quad
\boxed{\;k_\Phi^2 = \omega^2\epsilon\mu = \frac{\omega^2}{c^2}, \qquad k_\Phi = \frac{\omega}{c} = \frac{n(\omega)\,\omega}{c_0}\;}
$$
for a nonzero field. This is the medium dispersion relation, and it is a consequence of the annihilation condition, not an extra assumption.

**Solution (c).** From $\vec k_\Phi\times\vec E_0 = \omega\mu\vec H_0$ and $\vec k_\Phi = k_\Phi\vec u_\eta$ with $k_\Phi = \omega/c$,
$$
\vec H_0 = \frac{1}{\omega\mu}\,\vec k_\Phi\times\vec E_0 = \frac{k_\Phi}{\omega\mu}\,\vec u_\eta\times\vec E_0 = \frac{1}{Z}\,\vec u_\eta\times\vec E_0,
$$
since $\frac{k_\Phi}{\omega\mu} = \frac{\sqrt{\epsilon\mu}}{\mu} = \sqrt{\frac{\epsilon}{\mu}} = \frac{1}{Z}$. Because $\vec E_0$ is transverse to the unit vector $\vec u_\eta$, the cross product has the same modulus: $|\vec u_\eta\times\vec E_0| = |\vec E_0|$. Hence
$$
|\vec H_0| = \frac{1}{Z}|\vec E_0|,
\qquad
|\vec B_0| = \mu|\vec H_0| = \frac{\mu}{Z}|\vec E_0| = \frac{1}{c}|\vec E_0|,
$$
because $\frac{\mu}{Z} = \mu\sqrt{\frac{\epsilon}{\mu}} = \sqrt{\epsilon\mu} = \frac{1}{c}$. Therefore
$$
|\vec E_0| = Z\,|\vec H_0| = c\,|\vec B_0|,
$$
which is the parent's amplitude statement, now derived. The last relation also shows $\vec E_0\cdot\vec B_0 = 0$: since $\vec B_0 = \mu\vec H_0 = \frac{1}{c}\vec u_\eta\times\vec E_0$,
$$
\vec E_0\cdot\vec B_0 = \frac{1}{c}\,\vec E_0\cdot(\vec u_\eta\times\vec E_0) = 0 .
$$
So both classical invariants of the amplitude vanish, $I_1 = \vec E_0^2 - c^2\vec B_0^2 = 0$ and $I_2 = \vec E_0\cdot\vec B_0 = 0$. That is the statement whose algebraic form is the next problem.

## Problem 2: The Null Amplitude and the Wave Biquaternion

**Statement.** (a) Show that the field-strength amplitude is null, $\langle\tilde{F}_0\rangle_{\natural} = 0$, hence that $\tilde{F}_0$ is $N$-degenerate, a zero divisor of $\mathbb{B}$. (b) Show that $\tilde P_{\Phi}$ is itself null and that it annihilates $\tilde{F}_0$ from the left. (c) Show by contrast that a standing wave in the same medium is not null, so that nullness is a property of the single running plane wave rather than of the Maxwell field in general.

**Solution (a).** Factor out the electric half. From $\vec H_0 = Z^{-1}\vec u_\eta\times\vec E_0$,
$$
-\sqrt{\mu}\,\vec H_0 = -\frac{\sqrt{\mu}}{Z}\,\vec u_\eta\times\vec E_0 = -\sqrt{\epsilon}\,\vec u_\eta\times\vec E_0 = i\sqrt{\epsilon}\left(i\,\vec u_\eta\times\vec E_0\right),
$$
because $\frac{\sqrt{\mu}}{Z} = \sqrt{\epsilon}$. Therefore
$$
\tilde{F}_0 = i\sqrt{\epsilon}\left(\vec E_0 + i\,\vec u_\eta\times\vec E_0\right) = i\sqrt{\epsilon}\,\vec N_0,
\qquad
\vec N_0 = \vec E_0 + i\,\vec u_\eta\times\vec E_0 ,
$$
which is the parent's form of the amplitude. For a pure-vector biquaternion the biquaternion norm is the general plain bilinear form $\langle\tilde{F}_0\rangle_{\natural} = \tilde{F}_0\tilde{F}^{\natural}_0 = \sum_\eta F_{t\eta}^2$, and $\langle i\sqrt{\epsilon}\vec N_0\rangle_{\natural} = (i\sqrt{\epsilon})^2\vec N_0\cdot\vec N_0 = -\epsilon\,\vec N_0\cdot\vec N_0$. Expand the complex dot product:
$$
\vec N_0\cdot\vec N_0 = \vec E_0^2 - (\vec u_\eta\times\vec E_0)^2 + 2i\,\vec E_0\cdot(\vec u_\eta\times\vec E_0).
$$
The last term vanishes identically, and the first two cancel because for a unit $\vec u_\eta$ and a transverse $\vec E_0$,
$$
(\vec u_\eta\times\vec E_0)^2 = (\vec u_\eta\cdot\vec u_\eta)\,\vec E_0^2 - (\vec u_\eta\cdot\vec E_0)^2 = \vec E_0^2,
$$
using the complex-bilinear identity $(\vec a\times\vec b)\cdot(\vec a\times\vec c) = (\vec a\cdot\vec a)(\vec b\cdot\vec c) - (\vec a\cdot\vec c)(\vec a\cdot\vec b)$ with $\vec a = \vec u_\eta$, $\vec b = \vec c = \vec E_0$, and $\vec u_\eta\cdot\vec u_\eta = 1$, $\vec u_\eta\cdot\vec E_0 = 0$. Hence
$$
\boxed{\;\langle\tilde{F}_0\rangle_{\natural} = -\epsilon\,\vec N_0\cdot\vec N_0 = 0\;}.
$$
Since $\tilde{F}_0$ is a pure vector, $\tilde{F}_0^2 = -\vec F_0\cdot\vec F_0 = -\langle\tilde{F}_0\rangle_{\natural} = 0$: the amplitude is **nilpotent**, and a nonzero nilpotent element of $\mathbb{B}$ is a zero divisor. This is the algebra of a nonzero null field, and it holds for every polarisation, linear or elliptical, because the argument used only $\vec u_\eta\cdot\vec E_0 = 0$.

**Solution (b).** The four-wavevector is null as well. Its biquaternion norm is
$$
\langle\tilde P_{\Phi}\rangle_{\natural} = \left(\frac{i\omega}{c}\right)^2 + \vec k_\Phi^2 = -\frac{\omega^2}{c^2} + k_\Phi^2 = 0
$$
by the dispersion relation of Problem 1. So $\tilde P_{\Phi}$ is a nonzero null element, hence a zero divisor, and Problem 1 established that
$$
\tilde P_{\Phi}\tilde{F}_0 = 0 .
$$
The statement has a clean interpretation: the field-strength amplitude is annihilated by the four-wavevector of the wave. Both objects lie on the zero-divisor cone, and their product vanishes. This is the algebraic content of the parent's sentence that a free plane wave is a zero divisor, made explicit: neither the nullness of $\tilde P_{\Phi}$ nor the nullness of $\tilde{F}_0$ alone is the whole statement — it is the annihilation $\tilde P_{\Phi}\tilde{F}_0 = 0$ of one null element by another. Since $\tilde P_{\Phi} \in \mathbb{B}_{\Phi}$ and $\tilde{F}_0$ is a pure vector with one Hermitian and one anti-Hermitian half, the product mixes the sectors; its two parts vanishing separately is exactly the transversality condition and the two curl relations.

**Solution (c).** Superpose two counter-propagating waves of the same frequency in the same medium, choosing a linear polarisation:
$$
\vec E = E_0\cos(k_\Phi z-\omega r'_t/c)\,\vec u_x + E_0\cos(k_\Phi z+\omega r'_t/c)\,\vec u_x = 2E_0\cos k_\Phi z\cos(\omega r'_t/c)\,\vec u_x .
$$
For the wave travelling in $-\vec u_z$ the magnetic field is $\vec H = Z^{-1}(-\vec u_z)\times\vec E$, so the two magnetic contributions subtract in the sum, giving
$$
\vec H = \frac{E_0}{Z}\left[\cos(k_\Phi z-\omega r'_t/c) - \cos(k_\Phi z+\omega r'_t/c)\right]\vec u_y = \frac{2E_0}{Z}\sin k_\Phi z\sin(\omega r'_t/c)\,\vec u_y .
$$
Then $\vec E\cdot\vec H = 0$, but
$$
\vec E^2 - c^2\vec B^2 = 4E_0^2\left(\cos^2 k_\Phi z\cos^2\omega r'_t/c - \sin^2 k_\Phi z\sin^2\omega r'_t/c\right),
$$
using $c^2\mu^2/Z^2 = c^2\epsilon\mu = 1$. This is not identically zero: at $k_\Phi z = \pi/4$, $\omega r'_t/c = 0$ it equals $2E_0^2$, while at $k_\Phi z = \pi/4$, $\omega r'_t/c = \pi/2$ it equals $-2E_0^2$. So $I_1 \neq 0$ and $\langle\tilde{F}\rangle_{\natural} \neq 0$ for the standing wave: it is not null and not a zero divisor. The nullness of Problem 2(a) is therefore specific to the single running plane wave, which is the case the parent treats. The standing wave, by contrast, is a superposition of two waves each of which is null, and it is the interference of their two null directions that removes the nullness — a reminder that the states classified by the invariants are fields, not modes.

## Problem 3: Energy, Flux, and the Energy–Momentum Biquaternion

**Statement.** (a) For the running wave, compute the instantaneous energy density $W$ and Poynting vector $\vec S$ and show $\vec S = cW\vec u_\eta$. (b) Compute the time averages $\langle W\rangle$ and $\langle\vec S\rangle$ and verify $|\langle\vec S\rangle| = c\langle W\rangle$. (c) Compute the energy–momentum biquaternion $\tilde{W}_{\Psi} = \frac{1}{2}\tilde{F}\tilde{F}^{*}$ for the wave, and show that it is conserved, $\tilde{\nabla}\tilde{W}_{\Psi} = 0$, and that it is itself null.

**Solution (a).** In terms of the real instantaneous fields,
$$
W = \frac{1}{2}\left(\epsilon\,\vec E^2 + \mu\,\vec H^2\right),
\qquad
\vec S = \vec E\times\vec H.
$$
Because $\vec H = Z^{-1}\vec u_\eta\times\vec E$ holds instantaneously for a single running wave (the relation is linear with the real coefficient $Z^{-1}$ and the phase factors cancel), the field vectors are mutually orthogonal in the sense of real 3-vectors: $\vec H\perp\vec E$, $\vec H\perp\vec u_\eta$, and
$$
|\vec H| = \frac{1}{Z}|\vec E|,
\qquad
|\vec B| = \frac{1}{c}|\vec E| .
$$
Hence $\mu\vec H^2 = \frac{\mu}{Z^2}\vec E^2 = \epsilon\vec E^2$, so $W = \epsilon\vec E^2$, and
$$
\vec S = \vec E\times\vec H = \vec E\times\left(\frac{1}{Z}\vec u_\eta\times\vec E\right)
= \frac{1}{Z}\left[\vec u_\eta\,\vec E^2 - \vec E(\vec E\cdot\vec u_\eta)\right]
= \frac{\vec E^2}{Z}\,\vec u_\eta = \frac{W}{\epsilon Z}\,\vec u_\eta = cW\,\vec u_\eta,
$$
using $\epsilon Z = \epsilon\sqrt{\mu/\epsilon} = \sqrt{\epsilon\mu} = 1/c$. So the energy flows along the wavevector with speed $c$, and $|\vec S| = cW$ at every instant.

**Solution (b).** With the complex amplitudes of the parent's convention, $\vec E(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z,r'_t) = \mathrm{Re}[\vec E_0 \exp(i(\vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)-\omega r'_t/c))]$, the time averages over a period are
$$
\langle W\rangle = \frac{1}{4}\left(\epsilon\,|\vec E_0|^2 + \mu\,|\vec H_0|^2\right),
\qquad
\langle\vec S\rangle = \frac{1}{2}\,\mathrm{Re}\!\left(\vec E_0\times\vec H_0^*\right).
$$
The first follows from $\langle\vec E^2\rangle = \frac{1}{2}|\vec E_0|^2$ and the analogous magnetic average. For the second, substitute $\vec H_0 = Z^{-1}\vec u_\eta\times\vec E_0$:
$$
\vec E_0\times\vec H_0^* = \frac{1}{Z}\,\vec E_0\times\left(\vec u_\eta\times\vec E_0^*\right)
= \frac{1}{Z}\left[\vec u_\eta\,(\vec E_0\cdot\vec E_0^*) - \vec E_0^*(\vec E_0\cdot\vec u_\eta)\right]
= \frac{|\vec E_0|^2}{Z}\,\vec u_\eta,
$$
which is already real, so $\langle\vec S\rangle = \frac{|\vec E_0|^2}{2Z}\vec u_\eta$. Meanwhile
$$
\langle W\rangle = \frac{1}{4}\left(\epsilon|\vec E_0|^2 + \mu\frac{|\vec E_0|^2}{Z^2}\right)
= \frac{|\vec E_0|^2}{4}\left(\epsilon + \frac{\mu}{Z^2}\right)
= \frac{|\vec E_0|^2}{4}\,(2\epsilon) = \frac{\epsilon|\vec E_0|^2}{2},
$$
because $\frac{\mu}{Z^2} = \epsilon$. Therefore $c\langle W\rangle = \frac{c\epsilon|\vec E_0|^2}{2} = \frac{|\vec E_0|^2}{2Z} = |\langle\vec S\rangle|$, since $c\epsilon = 1/Z$. This verifies the parent's relation $|\langle\vec S\rangle| = c\langle W\rangle$.

**Solution (c).** The energy–momentum biquaternion is the halved Hermitian form. Substituting $\vec S = cW\vec u_\eta$ into the general identity $\tilde{F}\tilde{F}^{*} = 2We_t + \frac{2i}{c}\vec S$ gives
$$
\boxed{\;\tilde{W}_{\Psi} = \frac{1}{2}\tilde{F}\tilde{F}^{*} = W\left(e_t + i\vec u_\eta\right)\;}.
$$
This is an element of $\mathbb{B}_{\Psi}$, as every Hermitian form is: its scalar part $W$ is real and its vector part $iW\vec u_\eta$ is purely imaginary. To compute $\tilde{\nabla}\tilde{W}_{\Psi}$, write $\theta_{\mathrm{pha}} = \vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) - \omega r'_t/c$ and $W = W(\theta_{\mathrm{pha}})$, the general form, which reduces to $W = W_0\cos^2\theta_{\mathrm{pha}}$ for an in-phase, linearly polarised wave. For a scalar, the gradient acts as $\tilde{\nabla}W = W_{\mathrm{pha},\theta}\,\tilde P_{\Phi}$, with $W_{\mathrm{pha},\theta} = \partial/\partial\theta_{\mathrm{pha}}\,W$ and $\tilde P_{\Phi} = \frac{i\omega}{c}e_t + \vec k_\Phi$ the four-wavevector: in the in-phase case, expanding $W = \frac{W_0}{2}(1 + \cos 2\theta_{\mathrm{pha}})$, the exponentials $\exp(\pm 2i\theta_{\mathrm{pha}})$ are eigenfunctions with eigenvalues $\pm 2i\tilde P_{\Phi}$, and their combination reproduces $W_{\mathrm{pha},\theta}\tilde P_{\Phi}$. Since $e_t + i\vec u_\eta$ is constant,
$$
\tilde{\nabla}\tilde{W}_{\Psi} = \left(\tilde{\nabla}W\right)\left(e_t + i\vec u_\eta\right)
= W_{\mathrm{pha},\theta}\,\tilde P_{\Phi}\left(e_t + i\vec u_\eta\right).
$$
Evaluating the product with $\vec k_\Phi = k_\Phi\vec u_\eta$, $k_\Phi = \omega/c$, and $\vec u_\eta^2 = -e_t$:
$$
\tilde P_{\Phi}\left(e_t + i\vec u_\eta\right)
= \left(\frac{i\omega}{c}e_t + \vec k_\Phi\right)\left(e_t + i\vec u_\eta\right)
= \frac{i\omega}{c}e_t - \frac{\omega}{c}\vec u_\eta + \vec k_\Phi + i\,\vec k_\Phi\vec u_\eta
= i\left(\frac{\omega}{c} - k_\Phi\right)e_t + \left(\vec k_\Phi - \frac{\omega}{c}\vec u_\eta\right) = 0,
$$
using $\vec k_\Phi\vec u_\eta = -k_\Phi e_t$. So $\tilde{\nabla}\tilde{W}_{\Psi} = 0$: the energy–momentum biquaternion of a free plane wave is conserved, which is the source-free case of the parent's law $\tilde{\nabla}\tilde{W}_{\Psi} = -\tilde{\mathcal F}$ with $\tilde{\mathcal F} = 0$.

Finally, the biquaternion norm of $\tilde{W}_{\Psi}$ is
$$
\langle\tilde{W}_{\Psi}\rangle_{\natural} = W^2\left(1 + (i\vec u_\eta)^2\right) = W^2\left(1 - \vec u_\eta\cdot\vec u_\eta\right) = W^2\left(1 - 1\right) = 0 .
$$
So the energy–momentum biquaternion of the wave is itself a **zero divisor**, on the null cone of $\mathbb{B}_{\Psi}$. The wave is null in the field strength and null in its energy–momentum simultaneously, and this is a consequence of the single null direction $\vec u_\eta$ that the plane wave carries.

## Problem 4: Dispersion and the Spectral Complex Structure

**Statement.** (a) For a homogeneous medium with frequency-dependent $\epsilon(\omega),\mu(\omega)$, identify the eigenvalue of $\partial/\partial R_t$ at frequency $\omega$ and state the sense in which the complex structure is spectral. (b) Derive the phase velocity and the group velocity from $k_\Phi = n(\omega)\omega/c_0$, and verify the group velocity on a two-frequency superposition. (c) Take the vacuum limit and check that every relation of Problems 1–3 reduces correctly.

**Solution (a).** The gradient's temporal component acts on a monochromatic wave as
$$
\partial/\partial R_t = -\frac{i}{c(\omega)}\,\partial/\partial r'_t \;\longrightarrow\; -\frac{i}{c(\omega)}\,(-i\omega) = -\frac{\omega}{c(\omega)},
$$
a **real** eigenvalue, so that the operator eigenvalue is $-\frac{\omega}{c(\omega)}e_t + i\vec k_\Phi$. The imaginary time axis $i r'_t = i\,c(\omega)\,r'_t$ is scaled by $c(\omega)$, which is different at each frequency; the algebra $\mathbb{B}$ and the scalar $i$ are fixed, and only the embedding of physical time into the imaginary direction changes. This is the precise sense in which the local complex structure is spectral as well as spatial, and it is why the dispersion relation must be imposed frequency by frequency.

**Solution (b).** With $n(\omega) = c_0/c(\omega)$ and $k_\Phi = \frac{n(\omega)\omega}{c_0}$, the phase velocity is
$$
v_p = \frac{\omega}{k_\Phi} = \frac{c_0}{n(\omega)} = c(\omega),
$$
and the group velocity is
$$
\boxed{\;v_g = \frac{d\omega}{dk} = \left(\frac{dk}{d\omega}\right)^{-1}
= \frac{c_0}{n(\omega) + \omega\,\dfrac{dn}{d\omega}}\;}.
$$
The distinction is not bookkeeping: a single monochromatic wave has no envelope and travels at $v_p$, while a narrow superposition travels at $v_g$. For two frequencies $\omega \pm \Delta\omega$ with wave numbers $k_\Phi \pm \Delta k_\Phi$, the sum of the two real waves factors as
$$
\cos\big((k_\Phi+\Delta k_\Phi)r_z - (\omega+\Delta\omega)r'_t/c\big) + \cos\big((k_\Phi-\Delta k_\Phi)r_z - (\omega-\Delta\omega)r'_t/c\big)
= 2\cos(\Delta k_\Phi\,r_z - \Delta\omega\,r'_t/c)\cos(k_\Phi z-\omega r'_t/c),
$$
an envelope $\cos(\Delta k_\Phi\,r_z-\Delta\omega\,r'_t/c)$ modulating the carrier. The envelope's speed is $\Delta\omega/\Delta k_\Phi$, which tends to $v_g = d\omega/dk_\Phi$ as $\Delta\omega\to0$. This shows that in a dispersive medium the physically transported energy moves at the group velocity, while the phase of the carrier moves at the phase velocity — a distinction the single-frequency statements of Problems 1–3 cannot display.

**Solution (c).** In vacuum $\epsilon = \epsilon_0$, $\mu = \mu_0$, so $c = c_0$, $Z = Z_0$, $n = 1$, and $dn/d\omega = 0$. Then the dispersion relation becomes $k_\Phi^2 = \omega^2/c_0^2$, the impedance relation becomes $\vec H_0 = Z_0^{-1}\vec u_\eta\times\vec E_0$, the amplitude relation becomes $|\vec E_0| = Z_0|\vec H_0| = c_0|\vec B_0|$, the nullness $\langle\tilde{F}_0\rangle_{\natural} = 0$ is unchanged, $v_p = v_g = c_0$, and the gradient's temporal eigenvalue becomes $-\omega/c_0$. Every relation reduces to the vacuum statement of the parent articles by the substitution $c\to c_0$, $Z\to Z_0$, as it must.

## Problem 5: The Monochromatic and Stationary Field

**Statement.** (a) With the harmonic time dependence $\tilde F = \tilde F_0(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\exp(-i\omega r'_t/c)$ and wave number $k_\Phi = \omega/c$, derive the equation satisfied by the complex amplitude and its radiating solution. (b) Take the time-independent limit, recover the Poisson equation and the Newton-potential solution, and exhibit the scalar and vector potentials of the stationary field.

**Solution (a).** In the corpus's three-vector form the field satisfies $\partial/\partial R_t\tilde F+\mathrm{rot}\,\tilde F=-\vec j$, with $\vec j = \sqrt{\mu}\,\vec J_{\mathrm{e}} - i\sqrt{\epsilon}\,\vec J_{\mathrm{m}}$ and $\partial/\partial R_t=-i\partial/\partial r'_t$. For the harmonic dependence $\partial/\partial R_t=-k_\Phi$, so

$$
\mathrm{rot}\,\tilde F - k_\Phi\,\tilde F = -\vec j,
\qquad k_\Phi = \frac{\omega}{c}.
$$

Applying the rotor and using $\mathrm{rot}\,\mathrm{rot} = \mathrm{grad}\,\mathrm{div} - \Delta$ turns this into the Helmholtz equation for the amplitude,

$$
\Delta\tilde F + k_\Phi^2\tilde F = \vec{\mathcal S},
\qquad
\vec{\mathcal S} = k_\Phi\,\vec j + \mathrm{rot}\,\vec j + \mathrm{grad}\,R_0,
\qquad
R_0 = i\rho/\sqrt{\epsilon},
$$

with $\rho$ fixed by charge conservation. Its radiating solution is

$$
4\pi\tilde F(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) = -\int \frac{\exp(ikR)}{R}\,\vec{\mathcal S}(\vec y)\,d^3 y,
\qquad R = \|r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z-\vec y\|,
$$

unique in the class of solutions satisfying the Sommerfeld radiation condition. The medium enters only through $k_\Phi = \omega/c$: the single constant $c$ replaces the pair $(\epsilon,\mu)$, exactly as in the parent's plane-wave dispersion.

**Solution (b).** For a time-independent field the equation becomes the static pair $\mathrm{rot}\,\tilde F = -\vec j$, $\mathrm{div}\,\tilde F = R_0$, hence the Poisson equation

$$
\boxed{\;\Delta\tilde F = \mathrm{rot}\,\vec j + \mathrm{grad}\,R_0\;},
$$

whose solution decaying at infinity is $\tilde F = -(4\pi R)^{-1} * (\mathrm{rot}\,\vec j + \mathrm{grad}\,R_0)$. With $\tilde F = c(\mathrm{grad}\,Ξ - \mathrm{rot}\,\tilde{Ξ}_{\mathrm{sp}})$ and $\mathrm{div}\,\tilde{Ξ}_{\mathrm{sp}} = 0$, the two potentials solve $\DeltaΞ = R_0/c$ and $\Delta\tilde{Ξ}_{\mathrm{sp}} = -\vec j/c$, so each is a Newton potential of its source. The energy density is $\tfrac{1}{2}\|\tilde F\|^2 = \tfrac{1}{2}(\epsilon\vec E^2 + \mu\vec H^2)$, and the Poynting vector is $\tfrac{1}{2} i c\,\tilde F\times\tilde F^*$. This is the frequency-domain and static counterpart of Problems 1–3: the same complex vector carries the electric and magnetic halves, and the two limits make the "single constant $c$" reading of the medium concrete.

## Where the Parent Leaves a Gap

An exercise that only confirms its parent has not tested it. The computations above confirm the parent's plane-wave *results* — the four conditions, the dispersion relation, the impedance and amplitude relations, the nullness, and the time-averaged energy relation all survived recomputation on oblique, elliptical, and $\epsilon\neq\mu$ cases. What the exercise does *not* find is equally worth recording: the parent's plane-wave section is correct where it is defined, and the gaps are gaps of coverage and of labelling, not false statements. They are stated here rather than smoothed over.

**1. The conditions are asserted, not derived.** The parent writes that for a source-free plane wave "$\tilde{\nabla}\tilde{F} = 0$ is equivalent to the four algebraic conditions", and then lists them. The exercise has derived them (Problem 1), and the derivation shows that the four conditions are not four independent inputs: the scalar part of $\tilde P_{\Phi}\tilde{F}_0 = 0$ and the vector part give two equations, from which the two curl relations follow, and the two transversality conditions then follow from the curl relations. The parent's phrasing suggests four parallel conditions; the algebra gives two, with the others as consequences. This is a difference of presentation, not of content, but it matters for a reader who wants to know what is assumed and what is derived.

**2. The normalisation must be real, and the absorbing case is outside the framework as written.** Every result above uses $\sqrt{\epsilon(\omega)}$ and $\sqrt{\mu(\omega)}$ as real numbers, which holds in a transparent frequency window. Near a resonance $\epsilon$ and $\mu$ become complex, the electric and magnetic halves of $\tilde{F}$ are no longer purely imaginary and purely real, the split into $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ fails, and $\tilde{F}$ becomes fully complex. The parent states this boundary and declines to pursue the absorbing case; the exercise does not close it either. The consequence for this exercise is explicit: the nullness $\langle\tilde{F}_0\rangle_{\natural} = 0$ of Problem 2, and with it the zero-divisor interpretation of a plane wave, are established for the *real* normalisation only. Whether they survive for complex $\sqrt{\epsilon},\sqrt{\mu}$, and which real slice is physical, are not determined here.

**3. The energy density is the non-dispersive one.** The parent's $W = \frac{1}{2}(\epsilon\vec E^2 + \mu\vec H^2)$ is the non-dispersive expression, and the parent notes that the standard dispersive energy density is the Brillouin form $W = \frac{1}{2}\big(\frac{d(\omega\epsilon)}{d\omega}\vec E^2 + \frac{d(\omega\mu)}{d\omega}\vec H^2\big)$. Problems 3 and 4 therefore prove the conservation law $\tilde{\nabla}\tilde{W}_{\Psi} = 0$ and the relation $|\langle\vec S\rangle| = c\langle W\rangle$ for the non-dispersive case, and the group-velocity statement of Problem 4(b) is a statement about the envelope of a superposition rather than about a modification of $\tilde{W}_{\Psi}$. How the Brillouin density sits with $\tilde{W}_{\Psi}$, and whether the dispersive correction also modifies the power–force density $\tilde{\mathcal F}$, are not worked out in the parent and are not worked out here.

**4. The label "Lorentz invariant" is inherited from the vacuum parent and is not established for the medium.** The parent's notation table lists $I_1 = \vec E^2 - c^2\vec B^2$ and $I_2 = \vec E\cdot\vec B$ as "Lorentz invariants of the field". In a medium with $c \neq c_0$ the medium singles out a rest frame, and the physical Lorentz group has invariant speed $c_0$, so the vacuum transformation law that establishes the invariance of these quantities does not carry over as a symmetry claim. The parent's body is careful here — it speaks of the wave cone and the zero-divisor cone and does not assert a medium Lorentz group — so the table's label is broader than the body supports. For the running plane wave the tension is harmless because both invariants vanish, $I_1 = I_2 = 0$, and the nullness is a direct computation (Problem 2); but the label should not be read as an established invariance for a general field in a medium. This is recorded as a gap and a doubt, not as a refutation.

The gap that the exercise most wants to flag is the first: a reader of the parent cannot tell which of its plane-wave statements are inputs and which are consequences without doing the derivation that Problem 1 supplies. That is the work this exercise was written to do.

## Further Problems

**1. Oblique incidence and Snell's law.** Use the parent's interface conditions — continuity of the tangential components of $\vec E$ and $\vec H$ and of the normal components of $\vec D$ and $\vec B$ — to derive Snell's law $n_1\sin\theta_1 = n_2\sin\theta_2$ and, at normal incidence, the Fresnel coefficients $r = (Z_2-Z_1)/(Z_2+Z_1)$, $r'_t = 2Z_2/(Z_1+Z_2)$ with $R+T=1$. Show where in the derivation the discontinuity of the biquaternionic normalisation $\sqrt{\epsilon},\sqrt{\mu}$ enters, since $\tilde{F}$ is not itself continuous across the interface.

**2. Evanescent waves.** In total internal reflection the transmitted wavevector has a component normal to the interface that is imaginary, so $\vec k_\Phi$ is no longer real. Repeat Problem 1 with one component of $\vec k_\Phi$ imaginary, and determine which of the parent's statements — transversality, the curl relations, the dispersion relation, the nullness $\langle\tilde{F}_0\rangle_{\natural} = 0$ — survive. The decay of the amplitude in the transverse direction is not radiative transport, and the energy relation of Problem 3 is expected to change; state precisely how.

**3. The absorbing case.** Let $\epsilon$ and $\mu$ be complex. Show explicitly that the electric and magnetic halves of $\tilde{F}$ leave $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ respectively, identify the obstacle to defining a real field strength, and determine what the framework's complexified extension requires to fix a physical real slice. This is the parent's declared boundary; it is not a computation with a settled answer in the framework as written.

**4. The Brillouin energy and the conservation law.** Replace the non-dispersive $W$ by the Brillouin expression and determine whether the biquaternionic energy–momentum and the source-free law $\tilde{\nabla}\tilde{W}_{\Psi} = 0$ still hold for a monochromatic wave in a dispersive medium, and what additional term the dispersive correction forces. This is the natural continuation of gap 3.

**5. The normalisation question.** The parent uses the absolute normalisation $\tilde{F} = i\sqrt{\epsilon}\vec E - \sqrt{\mu}\vec H$. Repeat the plane-wave construction with the vacuum-relative normalisation $\tilde{F} = i\sqrt{\epsilon/\epsilon_0}\vec E - \sqrt{\mu/\mu_0}\vec H$, which is common in optics, and determine which statements — the nullness, the equal-magnitude balance of the halves, the energy–momentum identity — are normalisation-independent and which are not.

**6. A wave packet and the group velocity.** Construct a normalised Gaussian superposition of plane waves around $\omega_0$ in a medium with a prescribed $n(\omega)$, compute the envelope motion to first order in the bandwidth, and check that it travels at $v_g$. Then ask whether the spectral family of embeddings $r'_t \mapsto i\,c(\omega)\,r'_t$ has any content beyond the bookkeeping of a family of distinct monochromatic problems.

**7. The chiral medium and the two wavenumbers.** Replace the constitutive relations of Problem 1 by the Drude–Born–Fedorov form $\vec D=\epsilon(\vec E+\beta\,\mathrm{rot}\,\vec E)$, $\vec B=\mu(\vec H+\beta\,\mathrm{rot}\,\vec H)$ of the parent's section *A Chiral Medium*. Show that a circularly polarized plane wave with $\vec u\times\vec E_0=-is\,\vec E_0$, $s=\pm1$, satisfies the two curl equations for the single wavenumber $k_\Phi^{s}=k_\Phi/(1-s k_\Phi\beta)$, so that the two handednesses carry the two refractive indices $n_s=1/(1-s\beta\omega/c)$, that is $k_\Phi^{s}=n_s\,\omega/c$, with $s=+1$ the branch $k_\Phi^-$ and $s=-1$ the branch $k_\Phi^+$ of *Maxwell’s Equations in Chiral Media*; the medium is then circularly birefringent; check that at $\beta=0$ the two branches collapse to Problem 1. Then diagonalize the system by setting $Ξ=\vec E/\sqrt{\mu}+i\vec H/\sqrt{\epsilon}$ and $\tilde{Ξ}_{\mathrm{sp}}=\vec E/\sqrt{\mu}-i\vec H/\sqrt{\epsilon}$: show that $Ξ$ and $\tilde{Ξ}_{\mathrm{sp}}$ are the field strength $\tilde F$ and its complex conjugate $\tilde F^{*}$ up to one constant, that they solve $(D_3-k_\Phi^-)Ξ=0$ and $(D_3+k_\Phi^+)\tilde{Ξ}_{\mathrm{sp}}=0$ with $k_\Phi^+=k_\Phi/(1+k_\Phi\beta)$, $k_\Phi^-=k_\Phi/(1-k_\Phi\beta)$, and that each is divergence-free and an eigenvector of the curl. Finally determine which of the plane-wave conclusions of Problems 1–3 survive the change of constitutive relations: the transversality conditions are unchanged, the nullness $\langle\tilde F_0\rangle_{\natural}=0$ survives for each circular polarization, and the impedance relation $\vec H_0=Z^{-1}\vec u_\eta\times\vec E_0$ is replaced by a handedness-dependent one.

## Summary

For a source-free monochromatic plane wave $\tilde{F} = \tilde{F}_0\,\exp(i(\vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)-\omega r'_t/c))$ in a homogeneous medium, the biquaternionic Maxwell equation reduces to the algebraic annihilation $\tilde P_{\Phi}\tilde{F}_0 = 0$, where $\tilde P_{\Phi} = \frac{i\omega}{c}e_t + \vec k_\Phi \in \mathbb{B}_{\Phi}$ is the four-wavevector. Its scalar and vector parts give the two curl conditions
$$
\vec k_\Phi\times\vec E_0 = \omega\mu\,\vec H_0,
\qquad
\vec k_\Phi\times\vec H_0 = -\omega\epsilon\,\vec E_0,
$$
from which the transversality conditions $\vec k_\Phi\cdot\vec E_0 = \vec k_\Phi\cdot\vec H_0 = 0$ and the dispersion relation $k_\Phi = \omega/c$ follow. The impedance relation $\vec H_0 = Z^{-1}\vec u_\eta\times\vec E_0$ gives $|\vec E_0| = Z|\vec H_0| = c|\vec B_0|$, the two normalised halves $i\sqrt{\epsilon}\vec E_0$ and $-\sqrt{\mu}\vec H_0$ have equal magnitude, and the amplitude is the null combination $\tilde{F}_0 = i\sqrt{\epsilon}(\vec E_0 + i\vec u_\eta\times\vec E_0)$.

The amplitude is a zero divisor: $\langle\tilde{F}_0\rangle_{\natural} = -\epsilon\,\vec N_0\cdot\vec N_0 = 0$ and $\tilde{F}_0^2 = 0$, and the null four-wavevector annihilates it, $\tilde P_{\Phi}\tilde{F}_0 = 0$, with $\langle\tilde P_{\Phi}\rangle_{\natural} = 0$. A standing wave in the same medium is not null, so the nullness is specific to the single running plane wave. The energy density and flux satisfy $\vec S = cW\vec u_\eta$ and, on time average, $|\langle\vec S\rangle| = c\langle W\rangle$; the energy–momentum biquaternion is $\tilde{W}_{\Psi} = W(e_t + i\vec u_\eta)$, it is conserved, $\tilde{\nabla}\tilde{W}_{\Psi} = 0$, and it is itself null, $\langle\tilde{W}_{\Psi}\rangle_{\natural} = 0$. In a dispersive medium the temporal eigenvalue of the gradient is $-\omega/c(\omega)$, the phase velocity is $c(\omega)$, the group velocity is $c_0/(n + \omega\,dn/d\omega)$, and the vacuum limit $c\to c_0$, $Z\to Z_0$, $n\to1$ recovers every statement. Problem 5 extends the same complex vector to harmonic and static fields: the complex amplitude obeys a Helmholtz equation with the radiating kernel $\exp(ik_\Phi R)/R$, its static limit is the Poisson equation solved by Newton potentials, and throughout the medium enters only through $k_\Phi = \omega/c$ — the "single constant $c$" interpretation made concrete.

The exercise confirms the parent's plane-wave results on cases the parent did not use, and it reports the parent's gaps rather than closing them: the conditions are derived here but asserted there; the absorbing case lies outside the real normalisation; the energy density used is non-dispersive; and the "Lorentz invariant" label of the notation table is inherited from the vacuum setting and is not established for a medium.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_\eta^2 = -e_t$, $\vec e_j \vec e_\eta = -\delta_{j\eta}e_t + \epsilon_{j\eta m}\vec e_m$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{B}_{\Phi}, \mathbb{B}_{\Psi}$ | Anti-Hermitian (material) and Hermitian (informational) subspaces |
| $\mathbb{B}_{H}, \mathbb{B}_{C}$ | Real-quaternion subspace, scalar subspace |
| $\tilde{\nabla}, \tilde{\nabla}^{\natural}, \Box = \tilde{\nabla}\tilde{\nabla}^{\natural}$ | Biquaternionic gradient, its quaternion conjugate, d'Alembertian |
| $\partial/\partial R_t = -i\partial/\partial r'_t$ | Temporal component of the gradient (medium) |
| $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ | Field-strength biquaternion (pure vector) |
| $\tilde{F}_0$ | Plane-wave amplitude of the field strength |
| $\vec E_0, \vec H_0, \vec B_0 = \mu\vec H_0$ | Complex amplitudes; $\vec B_0$ the magnetic induction amplitude |
| $\epsilon, \mu$ | Permittivity and permeability of the medium |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $Z = \sqrt{\mu/\epsilon}$, $Z_0$ | Wave impedance of the medium; in vacuum |
| $n(\omega) = c_0/c(\omega)$ | Refractive index |
| $\vec k_\Phi, \omega, \vec u_\eta = \vec k_\Phi/\lvert\vec k_\Phi\rvert$ | Wavevector, angular frequency, unit wavevector |
| $\tilde P_{\Phi} = \frac{i\omega}{c}e_t + \vec k_\Phi$ | Four-wavevector biquaternion, in $\mathbb{B}_{\Phi}$ |
| $\tilde{A}_{\Phi} = i\,a'_te_t + \vec A$ | Potential biquaternion |
| $\vec j = \sqrt{\mu}\,\vec J_{\mathrm{e}} - i\sqrt{\epsilon}\,\vec J_{\mathrm{m}}$ | Complex current of the field equation |
| $k_\Phi = \omega/c=n(\omega)\omega/c_0$ | Wave number in the medium |
| $k_\Phi^{\pm}=k_\Phi/(1\pm k_\Phi\beta)$ | The two chiral wave numbers; $k_\Phi^{s}$ with $s=\mp1$ |
| $Ξ, \tilde{Ξ}_{\mathrm{sp}}$ | Scalar and vector potentials of the stationary field |
| $\tilde J_{\Phi} = ic\rho\,e_t + \vec J$ | Four-current; the source is $\sqrt{\mu}\,\tilde J_{\Phi}$ |
| $\vec N = \vec E + ic\vec B$, $\tilde{F} = i\sqrt{\epsilon}\,\vec N$ | Riemann–Silberstein vector and the field strength |
| $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm (complex scalar) |
| $I_1 = \vec E^2 - c^2\vec B^2$, $I_2 = \vec E\cdot\vec B$ | Field invariants (see gap 4 on the medium setting) |
| $W = \frac{1}{2}(\epsilon\vec E^2 + \mu\vec H^2)$ | Electromagnetic energy density |
| $\vec S = \vec E\times\vec H$ | Poynting vector |
| $\tilde{W}_{\Psi} = \frac{1}{2}\tilde{F}\tilde{F}^{*} = W\,e_t + \frac{i}{c}\vec S$ | Energy–momentum biquaternion, in $\mathbb{B}_{\Psi}$ |
| $v_p = \omega/k_\Phi = c(\omega)$, $v_g = c_0/(n + \omega\,dn/d\omega)$ | Phase and group velocities |
| $\operatorname{Tr}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi^{*})=\operatorname{Tr}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi)=2\langle\tilde{Ϛ}_{\Psi},\tilde R_\Psi\rangle_{*} = 2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi^{*})$ | Trace formula |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |

## Further Reading

The further reading of this exercise is the parent and companion articles of this series, all present in `articles_physics/`; the standard textbook references for media, dispersion, and the Fresnel coefficients are listed in the Further Reading sections of those articles.

- [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html) — the algebra, the two sectors, and the local complex structure.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) — the four-vectors, including the four-wavevector, and the light cone as the zero-divisor cone.
- [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html) — the Hermitian subspace, the conjugation action, and the trace formula.
- [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html) — the field strength, the source, the gradient, the gauge structure, and the energy–momentum biquaternion.
- [The Field-Strength Biquaternion and Its Invariants](the-field-strength-biquaternion-and-its-invariants.html) — the biquaternion norm, the Riemann–Silberstein vector, and the invariant classification of the field.
- [Electromagnetism in Media — The Local Complex Structure at Work](electromagnetism-in-media-the-local-complex-structure-at-work.html) — the direct parent: the medium parameters, dispersion, interfaces, and the plane-wave conventions applied here.
- [Exercise: The Electromagnetic Energy–Momentum Tensor](exercise-the-electromagnetic-energy-momentum-tensor.html) — the rank-two energy–momentum tensor built from $\tilde{F}$, whose four-component biquaternionic counterpart appears in Problem 3.
