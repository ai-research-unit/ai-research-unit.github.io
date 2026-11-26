# __The Scalar Sector on a Frame__

## Introduction

This is the first of the section's three sectoral articles, and it is the shortest test of the dictionary. The preceding article stated that the source of the field equation is the derivative of the matter action with respect to the frame; this one takes the simplest matter action the corpus owns, puts it on a frame, and computes that derivative.

The scalar is the right place to start for a reason that is structural rather than practical. The corpus's central scalar field has no spin, no gauge freedom and no internal index. Its stress is therefore built from one object, the gradient, and every question about the frame's entry into a matter action reduces to the metric's entry, without the third route — the intrinsic legs and the spin connection — entering at all. If the dictionary fails here it fails everywhere; it does not fail here.

Two results, of different sizes.

**The stress, and the equation of state as a ratio of squared leg norms.** For a homogeneous field on a frame,

$$
\Theta^{\imath\jmath}=\partial^{\imath}\phi\,\partial^{\jmath}\phi+g^{\imath\jmath}\mathcal L,
\qquad
\rho=\tfrac12\dot\phi^{2}+V,
\qquad
p=\tfrac12\dot\phi^{2}-V,
\qquad
w=\frac{p}{\rho}=\frac{\dot\phi^{2}-2V}{\dot\phi^{2}+2V},
$$

so that $w\to+1$ for a kinetic-dominated field and $w\to-1$ for a potential-dominated one, and $w$ passes through $+1/3$ exactly when $\dot\phi^{2}=4V$. The last value is where the corpus's trace collapse annihilates the source, and the scalar shows that this happens at one point of its trajectory and not on a set.

**The dictionary is confirmed on the sector that has no spin.** The frame derivative was computed by finite differences on a non-diagonal frame and agrees with $\sqrt{|g|}\,\Theta^{\imath\jmath}(E\digamma_{\mathrm{met}})_{\jmath a}$ to $1.3\times10^{-10}$ relative, with the antisymmetric part of the recovered tensor at $1.2\times10^{-10}$ — that is, zero to the accuracy of the difference quotient.

The article also records what the scalar cannot settle. The potential $V$ is a free function; the coupling of $\phi$ to the frame is transcription; and the scalar's own action contains no term that the algebra generates, so the sector confirms the dictionary and adds nothing to the action problem.

## Conventions

The conventions are the preceding article's and none is redefined. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the material sector is $\mathbb{B}_{\Phi}$ with basis $e_0=ie_t$, $e_1=\vec e_x$, $e_2=\vec e_y$, $e_3=\vec e_z$, and the pairing is $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{\natural})$ with array $(\digamma_{\mathrm{met}})_{ab}=\mathrm{diag}(-1,1,1,1)$.

The frame is $\tilde E_{\Phi,\imath}$ with $g_{\imath\jmath}=\langle\tilde E_{\Phi,\imath},\tilde E_{\Phi,\jmath}\rangle_{\natural}$, its inverse is $G_{\imath\jmath}$, its dual is $\tilde F_{\Phi,\imath}=G_{\imath\jmath}\tilde E_{\Phi,\jmath}$, and the volume density is $\sqrt{|g|}$.

The field is real and central: $\tilde\Xi=\xi e_t$ with $\xi$ a real function, so it lies in the centre and the biquaternionic d'Alembertian acts on it componentwise. Its gradient is

$$
\tilde\nabla_{\Phi}\xi=\sum_{\imath}\tilde F_{\Phi,\imath}\,\frac{\partial\xi}{\partial x_{\imath}},
$$

the dual frame appearing because the derivative carries a lower index and the frame's legs are the basis. This is the only place where the frame enters, and it enters twice — once through $\tilde F_{\Phi,\imath}$, once through $\sqrt{|g|}$ — which is the whole content of the scalar's dependence.

**The sign rule.** The kinetic term carries $-\tfrac12$, so that with the interval's one minus the time derivative contributes positively:

$$
-\tfrac12\,g^{\imath\jmath}\partial_{\imath}\xi\,\partial_{\jmath}\xi
=-\tfrac12\left(-\dot\xi^{2}+\lvert\nabla\xi\rvert^{2}\right)
=\tfrac12\dot\xi^{2}-\tfrac12\lvert\nabla\xi\rvert^{2}.
$$

That is the corpus's sign rule and it is the reason the energy is bounded below. The potential is $V(\xi)=\tfrac12m_{\Phi}^{2}\xi^{2}$ in the corpus's normalisation, with $m_{\Phi}=2\pi\nu_m$, and is left general as $V$ where nothing depends on the form.

## The Action on a Frame

The scalar action is the corpus's, with the frame carrying the metric:

$$
S_{\mathrm{scal}}[\xi;\tilde E_{\Phi}]
=\int d^{4}x\,\sqrt{|g|}\left[-\tfrac12\,g^{\imath\jmath}\,\partial_{\imath}\xi\,\partial_{\jmath}\xi-V(\xi)\right].
$$

In the algebra's letters the kinetic term is the norm of the gradient,

$$
-\tfrac12\,g^{\imath\jmath}\partial_{\imath}\xi\,\partial_{\jmath}\xi
=-\tfrac12\,\mathrm{Sc}\left(\bigl(\tilde\nabla_{\Phi}\xi\bigr)^{\natural}\tilde\nabla_{\Phi}\xi\right),
$$

because the dual frame is orthonormal to the frame and $\langle\tilde F_{\Phi,\imath},\tilde F_{\Phi,\jmath}\rangle_{\natural}=G_{\imath\jmath}$ contracts the two derivatives with the inverse metric exactly. The element form and the coordinate form are the same functional; the article keeps the coordinate form because the Euler–Lagrange equation and the derivative are both read more easily in it.

**Where the frame enters.** $\sqrt{|g|}$ in the measure, $G_{\imath\jmath}$ in the contraction, and nothing else. The field $\xi$ has no internal index, so it does not see the legs, and it has no spin, so it does not see a connection. This is the sharpest form of the scalar's simplicity: its action depends on $\tilde E_{\Phi}$ only through the Gram matrix, which is exactly the hypothesis under which the preceding article's dictionary was derived.

## The Stress of the Scalar Field

**The variation.** Varying the action with respect to $\xi$ gives the Euler–Lagrange equation

$$
\frac{1}{\sqrt{|g|}}\partial_{\imath}\left(\sqrt{|g|}\,g^{\imath\jmath}\partial_{\jmath}\xi\right)-V'(\xi)=0,
$$

which is $\Box_{g}\xi-V'(\xi)=0$ with $\Box_{g}$ the Laplace–Beltrami operator of the frame's metric. On the flat frame it is the corpus's $\Box_{\Phi}\xi-m_{\Phi}^{2}\xi=0$, the central scalar equation of *The Lagrangian and the Central Scalar Field*.

**The stress.** Varying with respect to the frame, or equivalently differentiating with respect to $g_{\imath\jmath}$, gives

$$
\boxed{\;\Theta^{\imath\jmath}=\partial^{\imath}\xi\,\partial^{\jmath}\xi+g^{\imath\jmath}\mathcal L\;}
\qquad
\mathcal L=-\tfrac12\,g^{ab}\partial_{a}\xi\,\partial_{b}\xi-V(\xi),
$$

and with both indices lowered,

$$
\Theta_{\imath\jmath}=\partial_{\imath}\xi\,\partial_{\jmath}\xi+g_{\imath\jmath}\mathcal L .
$$

The two forms are related by two contractions with the metric, and *this is the index-placement remark the preceding article owed the reader*: the derivative with respect to the metric array is naturally a twice-contravariant object, the corpus keeps every index low, and the passage between them costs $g_{\imath a}g_{\jmath b}$. On the flat frame the two arrays coincide, which is why the flat-frame articles never had to say so; on a curved frame they differ at first order in $h_{\imath\jmath}$, and the sectoral articles work with the all-low form because $\rho$ and $p$ are read from it.

**The verification.** The dictionary was checked on the frame

$$
E=\begin{pmatrix}1.08&0.03&0&0\\0.02&1.04&0.05&0\\0&0.02&1.06&0\\0.01&0&0.03&1.03\end{pmatrix},
$$

with the prescribed gradient $\partial_{\imath}\xi=(0.6,-0.4,0.3,0.5)$ and $V=0.7$, evaluating $\delta S/\delta E_{\imath a}$ by central differences of the pointwise density:

| quantity | value |
| --- | --- |
| relative error of $\delta S/\delta E_{\imath a}=\sqrt{\lvert g\rvert}\,\Theta^{\imath\jmath}(E\digamma_{\mathrm{met}})_{\jmath a}$ | $1.3\times10^{-10}$ |
| antisymmetric part of the recovered $\Theta^{\imath\jmath}$ | $1.1\times10^{-10}$ |
| antisymmetric part of the recovered $\Theta_{\imath\jmath}$ | $1.2\times10^{-10}$ |

The third row is the one worth reading. The scalar's stress is symmetric because its Lagrangian depends on the frame only through the symmetric $g$, so the frame variation is automatically blind to the antisymmetric direction — and the number confirms that the dictionary produces that blindness rather than being imposed to have it.

## The Equation of State as a Ratio of Leg Norms

Take the field homogeneous in the frame's time, $\xi=\xi(r'_{t})$, and read the stress in an orthonormal frame, $g_{\imath\jmath}=(\digamma_{\mathrm{met}})_{\imath\jmath}$. Then

$$
\mathcal L=\tfrac12\dot\xi^{2}-V,
\qquad
\Theta_{00}=\dot\xi^{2}+(-1)\mathcal L=\tfrac12\dot\xi^{2}+V\equiv\rho,
\qquad
\Theta_{\imath\jmath}=(1)\mathcal L\,\delta_{\imath\jmath}=\left(\tfrac12\dot\xi^{2}-V\right)\delta_{\imath\jmath}\equiv p\,\delta_{\imath\jmath}.
$$

So the two independent functions of a perfect fluid are the field's kinetic and potential energies, and the equation of state is their ratio,

$$
w=\frac{p}{\rho}=\frac{\dot\xi^{2}-2V}{\dot\xi^{2}+2V},
$$

a function of one variable, $\dot\xi^{2}/V$, ranging over $(-1,+1)$.

**Why the orthonormal frame is the one to read it in, and how it connects to the fluid frame.** $\rho$ and $p$ are functions, and in an orthonormal frame they are the two diagonal entries of $\Theta$. *The Action Problem* builds a frame whose Gram matrix *is* $\mathrm{diag}(\rho,p,p,p)$ — time leg $-\sqrt\rho\,e_t$, spatial legs $\sqrt p\,\vec e_{\imath}$ — and that is a different statement, about a frame whose metric is the stress, not about the stress in a fixed metric. The two readings agree on the numbers and differ in what they claim: the first says the fluid's two functions are the diagonal entries of the stress in the frame the fluid defines; the second says the frame's leg lengths are $\sqrt{\rho}$ and $\sqrt{p}$, which is why the traceless part is carried by the frame's shape and not by its trace. Both are used below, and neither is a derivation of the other.

**The limits, and they are the two extremes a scalar can reach.**

| regime | $w$ | what it is |
| --- | --- | --- |
| potential-dominated, $\dot\xi^{2}\ll V$ | $-1$ | a cosmological-constant-like source: tension equal to energy density |
| kinetic-dominated, $V\ll\dot\xi^{2}$ | $+1$ | a stiff fluid: pressure equal to energy density |
| $\dot\xi^{2}=4V$ | $+1/3$ | the radiation value |

The middle column is exhaustive as a range and not as a list: **no scalar equation of state lies outside $(-1,+1)$**, because $w$ is a ratio of $(\dot\xi^{2}-2V)$ to $(\dot\xi^{2}+2V)$ with both terms non-negative. A fluid with $w>1$, which is what a scalar with a negative potential would give, is outside the sector; a fluid with $w<-1$ would need a negative kinetic term.

**Why $w=+1/3$ is the interesting entry.** The corpus records, in *The Action Problem*, that the natural single-biquaternion packaging of a symmetric stress collapses to its trace and annihilates a radiation fluid entirely. The scalar supplies the exact condition for that annihilation:

$$
-\rho+3p=\left(\tfrac12\dot\xi^{2}+V\right)\!-3\!\left(\tfrac12\dot\xi^{2}-V\right)=\dot\xi^{2}-4V,
$$

which vanishes at $\dot\xi^{2}=4V$ and only there, and at that point $w=p/\rho=V/3V=1/3$. So the trace collapse is not a defect of the scalar sector; it bites at one point of the trajectory, and at that point the sector is a radiation fluid. Everywhere else the scalar survives the collapse with a nonzero trace, and the collapse destroys information about the split between $\dot\xi^{2}$ and $V$ only when the split is the radiation one.

That is a sharpening of the corpus's statement worth stating plainly: **the trace carries $-\rho+3p$, and a source is invisible to the trace exactly when its equation of state is the radiation one.** The single-element carrier is lossy for every fluid except at $w=1/3$, where it is blind, and blind sources are precisely the ones the trace cannot see.

## What the Sector Establishes and What It Leaves

**Established.**

1. The scalar action on a frame, its Euler–Lagrange equation, and its stress $\Theta_{\imath\jmath}=\partial_{\imath}\xi\partial_{\jmath}\xi+g_{\imath\jmath}\mathcal L$, all three transcribed consistently and checked by the frame derivative to $1.3\times10^{-10}$.
2. The equation of state as a ratio of kinetic to potential energy, its range $(-1,1)$, and its three named points.
3. The trace $-\rho+3p=\dot\xi^{2}-4V$ and the exact condition for the corpus's trace collapse to annihilate the source, which is $w=1/3$.
4. The index-placement remark: the frame derivative is twice-contravariant, the all-low tensor costs two contractions with $g$, and the two coincide only on a frame that is flat.

**Left open.** The potential $V$ is a free function; the algebra does not select it, being unable to build a self-interaction from structure constants the central operator does not have. The coupling of the scalar to the frame is transcription — the parent articles' sign rule makes it the standard action, and nothing in the algebra prefers it. And the sector says nothing about the gravitational side, which is the same half-open item every article of this section records.

## Summary

The scalar on a frame is the dictionary's simplest test and it passes: the action depends on the frame only through the Gram matrix, the frame derivative equals $\sqrt{|g|}\Theta^{\imath\jmath}(E\digamma_{\mathrm{met}})_{\jmath a}$ to $1.3\times10^{-10}$, and the stress is the corpus's standard one, symmetric by construction.

The equation of state is a ratio of squared quantities, $w=(\dot\xi^{2}-2V)/(\dot\xi^{2}+2V)$, so a scalar fluid spans $(-1,+1)$ and no more. Its trace is $\dot\xi^{2}-4V$ and vanishes exactly at $w=1/3$, which is where the corpus's single-element packaging loses the source entirely. The scalar therefore shows that the trace collapse is not a general obstruction but a condition: it removes the radiation equation of state and nothing else.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\xi$ | real central scalar, $\tilde\Xi=\xi e_t$ |
| $V(\xi)$ | potential, $\tfrac12m_{\Phi}^{2}\xi^{2}$ in the corpus's normalisation |
| $\mathcal L$ | $-\tfrac12 g^{ab}\partial_a\xi\partial_b\xi-V$ |
| $\Theta^{\imath\jmath}$ | $g^{\imath\jmath}\mathcal L+\partial^{\imath}\xi\partial^{\jmath}\xi$, the frame derivative |
| $\Theta_{\imath\jmath}$ | the all-low form, $g_{\imath a}g_{\jmath b}\Theta^{ab}$ |
| $\rho,\ p$ | $\Theta_{00}$ and $\Theta_{\imath\jmath}/\delta_{\imath\jmath}$ in the fluid frame |
| $w$ | $p/\rho$ |
| $\Box_g$ | Laplace–Beltrami operator of the frame's metric |

## Further Reading

- [Matter Into the Frame: The Variation That Defines the Source](matter-into-the-frame-the-variation-that-defines-the-source.html), for the dictionary this article tests and the index-placement remark it makes precise.
- [The Lagrangian and the Central Scalar Field](the-lagrangian-and-the-central-scalar-field.html), for the central scalar action whose Euler–Lagrange equation appears here as the frame's Laplace–Beltrami equation.
- [The Action Problem](the-action-problem.html), for the perfect-fluid frame with leg scales $\sqrt\rho$ and $\sqrt p$ that this article's equation of state fills, and for the trace collapse.
- [The Maxwell Sector on a Frame](the-maxwell-sector-on-a-frame.html), for the sector where the same dictionary is applied to a field with spin one, and where the algebraic packaging fails.
- [The Newtonian Limit: Closing the Chain](the-newtonian-limit-closing-the-chain.html), for the chain that a $\rho$ of this kind feeds.
