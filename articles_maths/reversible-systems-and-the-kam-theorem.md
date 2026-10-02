# __Reversible Systems and the KAM Theorem__

## Introduction

The **KAM theorem** states that a small perturbation of an integrable system does not destroy all its invariant tori: those whose frequency vector is **Diophantine** survive, as a Cantor set of tori of positive measure, and on them the motion remains conditionally periodic. The theorem is a theorem of stability of the integrable structure, and it was discovered in the Hamiltonian setting, where the tori carry the invariant symplectic form and the perturbation is a Hamiltonian one. Its **reversible** version, due to Moser, replaces the Hamiltonian hypothesis by a **reversing symmetry**: a reversible system that is a perturbation of an integrable reversible one has, for small perturbations and Diophantine frequencies, invariant tori that are themselves invariant under the reversor. The point of the reversible theorem is that reversibility is a weaker and more flexible hypothesis than the symplectic one — a reversible map need not preserve a form, and the reversor may be an arbitrary involution — and that the reversal supplies the frequency data, the nondegeneracy (a twist) and the cancellation of the small denominators without an action functional. The reversible KAM theory is therefore the natural setting of the conservative dynamics of systems with a time-reversal symmetry, of which the reversible twist maps and the reversible perturbations of the harmonic oscillator are the standard models.

The article treats the reversible KAM theorem and the symmetry of the surviving tori. It defines the reversible twisted system, the reversible action-angle model and the **reversible nondegeneracy** condition; it states the **KAM theorem** in its Hamiltonian form, quoted from *Lagrangian and Hamiltonian Systems*, and the **reversible KAM theorem** of Moser, with the role of the reversor in the proof and the Diophantine condition on the frequencies; it describes the **symmetry of the surviving tori**: an invariant torus of a reversible system carries the reversor if it is symmetric, the reversor acts on it as a reflection, the symmetric tori are those meeting the symmetry sets, and the reversible integrable model has its tori arranged in the symmetry structure; it treats the reversible Birkhoff normal form and the reversible frequency map; and it gives the examples — the reversible twist maps of the standard-map type, the reversible perturbation of the pendulum and of the oscillator, and the reversible Hill equation — with the golden-mean torus as the most robust and the numerical thresholds as literature values.

The KAM theorem, the action-angle coordinates, the Liouville–Arnold theorem, the Diophantine conditions and the survival of the tori are those of *Lagrangian and Hamiltonian Systems*, which states the Hamiltonian KAM theorem and hands the stability and destruction of the tori to this category; the reversible systems, the reversors, the fixed sets and the symmetric periodic orbits are those of *Reversible Dynamical Systems and Time-Reversal Symmetry* and *Symmetric Periodic Orbits and the Involution*, immediately preceding; the twist maps, the rotation number and the annulus are those of *Topological Dynamics* and *Billiards and Related Systems*; the Diophantine approximation, the continued fractions and the Hurwitz constant are those of *Diophantine Approximation and Continued Fractions*. The reversible normal form and the reversible singularity theory are *Equivariant Bifurcation Theory*, and the symmetric tori of the equivariant case are *Invariant Tori under an Involution*, both later in this category; the operator form of the involution is *Reversible Operators and the Involution*, in the `- * Operator Theory` group.

No physics is invoked.

## The Reversible Integrable Model

### Reversible Twisted Systems

**Definition.** A **reversible twisted system** is a smooth map $T$ of a product manifold $N\times\mathbb{T}^n$ (or an annulus, for $n=1$) with a reversor $R$ of the form

$$
R(x,\theta)=(R_0(x),-\theta+\varphi(x)),
$$

where $R_0$ is an involution of $N$ and $\varphi$ a smooth function; the system is **twisted** if the frequency map of the integrable model is nondegenerate, $\det\partial\omega/\partial I\neq0$, in action-angle coordinates $(I,\theta)$. The model case is the reversible map of the annulus with a **symmetry line**, the fixed set $\mathrm{Fix}(R)$ a finite union of curves, as in the reversible theory of *Symmetric Periodic Orbits and the Involution*.

**Definition (reversible nondegeneracy).** Let $T_0(I,\theta)=(I,\theta+\omega(I))$ be the integrable reversible model with reversor $R_0(I,\theta)=(I,-\theta)$. The system is **reversibly nondegenerate** at $I_0$ if the frequency map $\omega$ has invertible derivative at $I_0$, $\det\partial\omega/\partial I(I_0)\neq0$; the condition is the **twist** condition of the reversible theory, and it is the hypothesis under which the frequencies can be prescribed and the small denominators controlled.

### Diophantine Frequencies

**Definition.** A vector $\omega\in\mathbb{R}^n$ is **Diophantine** if there are constants $\gamma>0$ and $\tau\ge n-1$ with

$$
|\langle k,\omega\rangle|\ge\frac{\gamma}{|k|^{\tau}} \qquad \text{for all } k\in\mathbb{Z}^n\setminus\{0\},
$$

so that the frequency is not only nonresonant but nonresonant at an algebraic rate.

**Theorem (the Diophantine set has full measure, quoted).** The set of Diophantine vectors has full Lebesgue measure in $\mathbb{R}^n$; its complement is a set of measure zero, and the vectors that fail the condition for every $\tau$ are the resonant and the Liouville vectors. The golden mean $\gamma_0=(\sqrt5-1)/2$ is the extremal one-dimensional example: its continued fraction is $[0;1,1,1,\dots]$, verified from its definition, and by the Hurwitz theorem of *Diophantine Approximation and Continued Fractions* the constant in the bound $|q\gamma_0-p|>c/q$ is best possible at $c=1/\sqrt5$, so the golden mean is the worst-approximable number and its rotation number is the last to lose its invariant curve.

*Proof.* Quoted. The continued fraction of $\gamma_0$ was recomputed: the partial quotients of $(\sqrt5-1)/2$ are all $1$, as the expansion $x=1/(1+x)$ shows; and Hurwitz's theorem is the sharp form of the Dirichlet approximation theorem, stated and proved in *Diophantine Approximation and Continued Fractions*.

## The KAM Theorems

### The Hamiltonian Theorem

**Theorem (KAM, quoted).** Let $H_0(I)$ be an integrable Hamiltonian on $N\times\mathbb{T}^n$ with nondegenerate frequency map $\omega(I)=\partial H_0/\partial I$, and let $H_\varepsilon=H_0+\varepsilon H_1$ be a small smooth perturbation. Then for every $\omega$ Diophantine and every sufficiently small $\varepsilon$ there is an invariant torus of $H_\varepsilon$ close to the torus $\{I=I_0\}$ of frequency $\omega(I_0)=\omega$, and the union of the surviving tori has positive measure in the phase space; the conjugacy is a smooth (or, for the analytic case, an analytic) embedding, and the motion on the tori is conditionally periodic.

*Proof.* Quoted as standard from *Lagrangian and Hamiltonian Systems*, where the Kolmogorov–Arnold–Moser theorem, the small-denominator estimates, the Newton iteration and the measure estimate are stated and attributed. The present article does not reproduce the proof; it uses the theorem as the Hamiltonian background of the reversible version.

### The Reversible Theorem

**Theorem (reversible KAM, Moser).** Let $T_\varepsilon$ be a smooth family of diffeomorphisms of $N\times\mathbb{T}^n$ that are **reversible** with respect to a fixed reversor $R$, with $T_0(I,\theta)=(I,\theta+\omega(I))$ the integrable reversible model and with the reversible nondegeneracy $\det\partial\omega/\partial I\neq0$. Then for every Diophantine $\omega$ and every sufficiently small $\varepsilon$ there is a torus $\mathcal{T}_\omega$, close to the torus of frequency $\omega$ of the model, that is invariant under $T_\varepsilon$; the surviving tori are **reversible** in that $R(\mathcal{T}_\omega)=\mathcal{T}_\omega$, and their union has positive measure in the phase space.

*Proof (sketch).* The proof is Moser's: one linearises the invariance equation around a torus of the model and solves it by a Newton iteration in the class of reversible maps; the reversible structure supplies the reflection $\theta\mapsto-\theta$ that halves the unknowns and removes the resonant component, and the small denominators $\langle k,\omega\rangle$ are controlled by the Diophantine condition exactly as in the Hamiltonian case. The nondegeneracy makes the frequency map invertible so that a prescribed Diophantine $\omega$ is carried by a torus; the measure estimate is the standard estimate of the complement of the Diophantine set intersected with the frequency range under the map $\omega$. The complete proof and the reversible Birkhoff normal form are in the references (Moser; Sevryuk); no new proof is attempted here.

**Remark (the reversor replaces the symplectic form).** The reversible theorem does not assume that $T_\varepsilon$ preserves a volume or a symplectic form. What replaces the Hamiltonian and its action functional is the reversor: the invariance equation is posed in the class of maps commuting with $R$, the reflection acts as an involution on the space of corrections and removes the components in the image of the linearised operator, and the small denominators are the same as in the Hamiltonian case. The reversible theorem is therefore strictly more general than the Hamiltonian one when the reversor exists, and it applies to dissipative reversible maps as well as to conservative ones, provided the twist nondegeneracy holds.

**Example (the reversible twist map).** The reversible standard map $S_k(\theta,I)=(\theta+I+k\sin\theta,\,I+k\sin\theta)$ of the preceding articles is a reversible perturbation of the integrable twist map $S_0(\theta,I)=(\theta+I,I)$, which has $R_0(\theta,I)=(-\theta,I)$ as reversor; since the frequency map of $S_0$ is the identity, the model is reversibly nondegenerate, and the reversible KAM theorem gives invariant curves with rotation number $\omega$ for every Diophantine $\omega$ and small $k$. The verification that $S_k$ is reversible with reversor $R(\theta,I)=(-\theta,I+k\sin\theta)$ was carried out numerically in *Reversible Dynamical Systems and Time-Reversal Symmetry*, and the reversibility is the hypothesis of the theorem.

## The Symmetry of the Surviving Tori

### Symmetric and Reversible Tori

**Definition.** An invariant torus $\mathcal{T}$ of a reversible map $T$ is **symmetric** (or **reversible**) if $R(\mathcal{T})=\mathcal{T}$; the reversor then acts on the torus as an orientation-reversing involution, and in the coordinates in which the torus is a linear flow with frequency $\omega$ the action of $R$ is the reflection of the angle, $\theta\mapsto-\theta+\delta$ up to a translation. The torus is **maximally symmetric** if it meets the fixed set $\mathrm{Fix}(R)$; the intersection is the fixed set of the induced reflection, a finite union of points and subtori of $\mathcal{T}$, and in the annulus case it is the set of the two points where the symmetric curve crosses the two symmetry lines.

**Theorem (the reversor acts as a reflection).** Let $\mathcal{T}$ be an $R$-invariant invariant torus of a reversible system, parametrised by a torus embedding so that the dynamics is the translation by $\omega$. Then the reversor, conjugated to the model torus, is the reflection $\theta\mapsto-\theta+\delta$ for the corresponding displacement $\delta$; the fixed set of that reflection inside $\mathcal{T}$ is the finite set $\{\theta:2\theta=\delta\}$ (a finite union of subtori when the reflection is partial), and it is precisely the intersection of the torus with the **symmetry sets** of the reversor, carried by the conjugacy.

*Proof.* The reversor reverses the time of the linear flow, so in the angle coordinates it maps the flow to its inverse, hence is an affine orientation-reversing involution of the torus, that is, a reflection $\theta\mapsto-\theta+\delta$; the fixed set of that reflection is the finite set stated, and it is the intersection of $\mathcal{T}$ with $\mathrm{Fix}(R)$ because the conjugacy carries the fixed set of $R$ to the fixed set of the model reflection under the symmetry hypothesis.

**Remark (the Cantor structure and the symmetric orbits).** The surviving tori form a Cantor set of positive measure, between them lie the gaps created by the resonances, and in each gap the symmetric periodic orbits of the preceding article continue to exist; the reversible structure is thus a two-layer description of the conservative dynamics, the continuous layer of the symmetric tori and the discrete layer of the symmetric periodic orbits, and the two layers are the reversible analogue of the KAM tori and the Birkhoff orbits of the Hamiltonian theory. The reversible KAM portrait is complemented by the destruction theory of the tori — the resonance overlapping and the transition to chaos — which is the same as in the Hamiltonian case and is cited.

### The Reversible Normal Form and the Frequency Map

**Definition.** Let $T$ be reversible about the origin of $\mathbb{R}^{2n}$ with reversor $R$, and suppose $R$ and $T$ are linear to first order with the reversible linear part $A$ and the involution $R_0$. The **reversible Birkhoff normal form** is the normal form of $T$ at the reversible fixed point obtained by removing, by a sequence of reversible changes of coordinates, all the monomials whose removal is permitted by the reversibility; the surviving monomials are those invariant under the simultaneous action of the linear reversor and the linear part, and the normal form is integrable in the sense of the **reversible Liouville–Arnold theorem**.

**Theorem (reversible frequency map and the nondegeneracy).** For a reversible integrable model in action-angle coordinates the frequency map $\omega:I\mapsto\omega(I)$ is the derivative of the angle advance along the actions, and the reversible KAM theorem requires its invertibility, $\det\partial\omega/\partial I\ne0$; the reversible Birkhoff normal form produces the frequency map as a formal series in the action variables, and its nondegeneracy is the only hypothesis of the reversible KAM theorem beyond the reversibility and the smallness. The reversible normal form and its availability at a resonance are *Equivariant Bifurcation Theory*, later in this category.

*Proof.* Quoted from the reversible normal form theory (Moser, Sevryuk); the construction removes the monomials that are not invariant, and the frequency map is the linear part of the integrable model in the action-angle variables. No proof is reproduced.

**Example (a reversible perturbation of the oscillator).** The reversible system $\dot x=y$, $\dot y=-x+\varepsilon F(x,y)$ with $F$ reversible about the reversor $(x,y)\mapsto(x,-y)$, that is, $F(x,-y)=F(x,y)$ (the field is even in $y$), is a reversible perturbation of the harmonic oscillator; the frequency map of the unperturbed oscillator is the constant $1$, which is degenerate in the action, and the reversible KAM theorem does not apply directly — the nonlinearity of $F$ is needed to make the frequency depend on the action, the reversible analogue of the anisochrony of an integrable Hamiltonian. The point is the reversible version of the classical requirement of a nonisochronous integrable system, and the nonlinear reversible oscillator with a nondegenerate frequency is the standard reversible KAM example.

## Summary

The **reversible KAM theorem** of Moser states that a reversible perturbation of an integrable reversible system preserves invariant tori for every **Diophantine** frequency $\omega$, provided the frequency map is nondegenerate (the reversible **twist** condition), $\det\partial\omega/\partial I\neq0$; the reversor replaces the symplectic form of the Hamiltonian theorem — the proof is a Newton iteration in the class of reversible maps, the reflection $\theta\mapsto-\theta$ halves the equation and removes the resonant part, and the small denominators $|\langle k,\omega\rangle|$ are bounded by the Diophantine condition $|\langle k,\omega\rangle|\ge\gamma|k|^{-\tau}$. The Hamiltonian **KAM theorem**, the action-angle coordinates and the Diophantine measure statement are those of *Lagrangian and Hamiltonian Systems*; the golden mean $\gamma_0=(\sqrt5-1)/2$ is the extremal frequency, its continued fraction $[0;1,1,\dots]$ verified and its worst-approximability the Hurwitz theorem of *Diophantine Approximation and Continued Fractions*. The surviving tori are **reversible**, $R(\mathcal{T})=\mathcal{T}$, and the reversor acts on them as the reflection $\theta\mapsto-\theta+\delta$, so a symmetric torus meets the fixed set $\mathrm{Fix}(R)$ in the finite set fixed by the induced reflection; the symmetric tori and the symmetric periodic orbits in the gaps are the two layers of the reversible conservative portrait, and the reversible **Birkhoff normal form** and its frequency map supply the nondegeneracy of the theory. The standard map $S_k(\theta,I)=(\theta+I+k\sin\theta,\,I+k\sin\theta)$, verified reversible, is the model; the reversible perturbation of the oscillator requires a nonlinear term to acquire a nondegenerate frequency; and the destruction of the tori beyond the KAM threshold is the reversible form of the resonance-overlap theory. The equivariant tori are *Invariant Tori under an Involution*, the reversible normal form is *Equivariant Bifurcation Theory*, and the operator form of the involution is *Reversible Operators and the Involution*, all later in this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_\varepsilon$, $T_0$ | Reversible perturbation; integrable reversible model |
| $R$, $\mathrm{Fix}(R)$ | Reversor and its fixed set (the symmetry lines) |
| $(I,\theta)$ | Action-angle coordinates; $\omega(I)$ the frequency map |
| $\det\partial\omega/\partial I\neq0$ | Reversible nondegeneracy (twist condition) |
| $\|\langle k,\omega\rangle\|\ge\gamma|k|^{-\tau}$ | Diophantine condition |
| $\gamma_0=(\sqrt5-1)/2$ | Golden mean, the extremal frequency |
| $\mathcal{T}_\omega$, $R(\mathcal{T}_\omega)=\mathcal{T}_\omega$ | Reversible invariant torus and its symmetry |
| $\theta\mapsto-\theta+\delta$ | Action of the reversor on a symmetric torus |
| $S_k(\theta,I)$ | Reversible standard (twist) map |

## Further Reading

- Jürgen Moser, "On invariant curves of area-preserving mappings of an annulus", *Nachrichten der Akademie der Wissenschaften in Göttingen* (1962), 1–20, and "Convergent series expansions for quasi-periodic motions", *Mathematische Annalen* 169 (1967), 136–176, for the reversible twist theorem.
- Michael B. Sevryuk, *Reversible Systems* (Springer Lecture Notes in Mathematics 1211, 1986), for the reversible KAM theory and the reversible Birkhoff normal form.
- Vladimir I. Arnold, "Proof of a theorem of A. N. Kolmogorov on the preservation of conditionally periodic motions", *Russian Mathematical Surveys* 18 (1963), 9–36, and Vladimir I. Arnold, Valery V. Kozlov and Anatoly I. Neishtadt, *Mathematical Aspects of Classical and Celestial Mechanics* (Springer, 3rd ed. 2006), for the Hamiltonian KAM theorem and its measure theory.
- Jürgen Pöschel, "A lecture on the classical KAM theorem", *Proceedings of Symposia in Pure Mathematics* 69 (2001), 707–732, for the modern proof and the small-denominator estimates.
- H. Scott Dumas, *The KAM Story* (World Scientific, 2014), for the history and the reversible variants.
- John A. G. Roberts and G. R. W. Quispel, "Chaos and time-reversal symmetry", *Physics Reports* 216 (1992), 63–177, for the reversible conservative dynamics.
- J. M. Greene, "A method for determining a stochastic transition", *Journal of Mathematical Physics* 20 (1979), 1183–1201, for the numerical threshold of the standard map and the robustness of the golden-mean torus.
- Rafael de la Llave, "A tutorial on KAM theory", *Proceedings of Symposia in Pure Mathematics* 69 (2001), 175–292, for the reversible and the quasi-periodic theory.
