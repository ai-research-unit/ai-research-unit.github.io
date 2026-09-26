# __The Vacuum State and the Casimir Effect in Biquaternionic Form__

## Introduction

The **vacuum state** $|0\rangle$ is the no-particle state of a quantized field, and the **zero-point energy** is what the field costs when it is in that state: half a quantum of energy per mode, summed over all modes. In ordinary quantum field theory that sum is quartically divergent and is discarded by normal ordering, but its **dependence on the boundary conditions** is finite, universal, and observable. Two parallel conducting plates, separated by a distance $a$ and otherwise isolating a region of the vacuum, change the permitted modes; the resulting change in the zero-point energy is the **Casimir energy**, and the force that follows is the **Casimir force**. This article asks what the biquaternion framework of this series says about the vacuum state and about that force, and it separates sharply what the algebra supplies from what the standard theory supplies.

The subject has a well-known trap, and this article is built around it. The naive mode sum for the Casimir energy **diverges** — quartically, as the fourth power of an imposed cutoff — and the familiar finite answer does not follow from the divergent sum by any rearrangement. The finite part appears only after a regularisation that must be justified rather than asserted. This article therefore does not present the number first and the justification afterwards. It exhibits the divergent sum, shows exactly where the divergence sits and how it is removed, and verifies the final force on two independent routes. Where the justification of a step is incomplete, that is said plainly.

A second trap is a factor of two. The bookkeeping of polarisations in the covariant quantisation of the Maxwell field is notoriously easy to get wrong, and the framework has something precise to say about it: the indefinite metric of the covariant treatment is the norm form of the material sector $\mathbb{M}_-$, and the sum of its signs fixes the effective number of polarisations. The article is explicit about which modes are counted.

The division between what is established and what is interpretation is stated here and kept throughout.

- **Established, and recomputed below.** The one-mode vacuum state of the framework is an idempotent of the informational sector $\mathbb{M}_+$, and the trace formula $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ gives vacuum expectation values for one fermionic mode. The zero-point energy of the free Maxwell field is a **central scalar** — a multiple of $e_0$ — so it commutes with everything and is unobservable as a constant, exactly as the harmonic-oscillator article records for the trace part of a Hamiltonian. Its dependence on the plate separation, however, is not constant. The bare mode sum diverges; the spectral-zeta route and the heat-kernel route give, independently,
$$
\frac{E_{\mathrm{EM}}}{A}=-\frac{\pi^{2}\hbar c}{720\,a^{3}},\qquad
\frac{F_{\mathrm{EM}}}{A}=-\frac{\pi^{2}\hbar c}{240\,a^{4}},
$$
with the force **attractive**. The factor of two between the electromagnetic result and the Dirichlet-scalar result is fixed by the two physical transverse polarisations, whose sum reproduces the norm form of $\mathbb{M}_-$.
- **Interpretation.** Reading the vacuum energy as the trace part, or scalar part, of the field Hamiltonian, and reading the framework's local complex structure as a possible home for boundaries, are readings of algebraic facts. The first is precise and is developed below; the second is a suggestion, flagged as such.
- **Gaps, left visible.** There is no bosonic ladder in $\mathbb{B}$, so the photon's Fock vacuum is a standard construction on an imported module rather than an object of the algebra. The perfectly conducting plates and their boundary conditions have no native description in the framework. The algebra does not select a regularisation. And the framework reproduces the standard Casimir result rather than modifying it, so it supplies no empirical discriminator here.

The article is organised as follows. The next section fixes the vacuum state in the framework. The section after that treats the zero-point energy and its central-scalar character. The following section sets up the parallel-plate configuration and exhibits the divergent mode sum. Two sections then regularise it by two independent routes. A section accounts for the polarisations and the factor of two. A section states the force, its sign, and its verification. A section separates what the framework supplies from what it imports, a short section treats boundaries and the local complex structure as an open direction, and the article closes with open questions.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the quaternion basis is $e_0=1,e_1,e_2,e_3$ with $e_k^{2}=-e_0$, and $i$ is the scalar imaginary with $i^{2}=-1$. The material (anti-Hermitian) and informational (Hermitian) sectors are
$$
\mathbb{M}_-=\{\tilde Q:\tilde Q^{\dagger}=-\tilde Q\}=\mathrm{span}_{\mathbb{R}}\{ie_0,e_1,e_2,e_3\},\qquad
\mathbb{M}_+=\{\tilde Q:\tilde Q^{\dagger}=\tilde Q\}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_1,ie_2,ie_3\},
$$
with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ and $i\mathbb{M}_\pm=\mathbb{M}_\mp$. The trace formula is $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$, normalised so that $\mathrm{Tr}(e_0)=2$ in the matrix representation $\mathbb{B}\cong M_2(\mathbb{C})$. The biquaternionic gradient is $\tilde\nabla=e_0\partial_{ict}+e_1\partial_x+e_2\partial_y+e_3\partial_z$, the potential and field strength are $\tilde A=i\phi/c\,e_0+\mathbf{A}$ and $\tilde F=i\sqrt{\epsilon}\,\mathbf{E}-\sqrt{\mu}\,\mathbf{H}$, and the single Maxwell equation is $\tilde\nabla\tilde F=-\tilde R$. For the free field we set $\epsilon=\epsilon_0$, $\mu=\mu_0$ and use natural units $\hbar=c=1$ where only the algebra is at issue; the dimensionful factors are restored in every displayed physical result. The spacetime metric of the $ict$ sector is $\eta=\mathrm{diag}(-1,+1,+1,+1)$, the norm form of $\mathbb{M}_-$; the indefinite metric of the covariant quantisation is $\zeta=(-1,+1,+1,+1)$, which is the same object.

## The Vacuum State in the Framework

The Fock space of a field is the direct sum of the symmetric or antisymmetric tensor powers of the one-particle space, and the **vacuum** $|0\rangle$ spans its degree-zero term:
$$
\mathcal{F}=\bigoplus_{n\ge0}\Big(\mathcal{H}_1^{\otimes n}\Big)_{\pm},\qquad |0\rangle\ \text{spans the } n=0 \text{ term},
$$
annihilated by every annihilation operator, $\hat a_r|0\rangle=0$. In the covariant Maxwell case the physical vacuum is additionally annihilated by the subsidiary combination $(\hat a_0-\hat a_3)$ that removes the timelike and longitudinal excitations. None of this is specific to the biquaternion framework; it is the standard second-quantised vacuum, which the companion articles transcribe.

The question that is specific to the framework is: **is the vacuum state an object of $\mathbb{B}$?** The answer has a positive part and a negative part, and they apply to different things.

**The one-mode vacuum is native.** For a single fermionic mode the algebra contains the whole ladder, as *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* establishes. With
$$
\tilde a_{\mathrm{tr}}=\tfrac12\big(ie_1-e_2\big),\qquad
\tilde a_{\mathrm{tr}}^{\dagger}=\tfrac12\big(ie_1+e_2\big),\qquad
\{\tilde a_{\mathrm{tr}},\tilde a_{\mathrm{tr}}^{\dagger}\}=e_0,
$$
the number operator is the idempotent
$$
\tilde N_{\mathrm{tr}}=\tilde a_{\mathrm{tr}}^{\dagger}\tilde a_{\mathrm{tr}}=\tfrac12\big(e_0-ie_3\big)=P_-(e_3)\in\mathbb{M}_+,
$$
so the **vacuum projector** is the complementary idempotent
$$
\vert 0\rangle\langle 0\vert=e_0-\tilde N_{\mathrm{tr}}=\tfrac12\big(e_0+ie_3\big)=P_+(e_3)\in\mathbb{M}_+.
$$
The vacuum state is therefore realized, for one mode, as a pure-state projector of the informational sector, and the fermion parity is the Hermitian element $(-1)^F=e_0-2\tilde N_{\mathrm{tr}}=ie_3$. A vacuum expectation value of an observable $\tilde H\in\mathbb{M}_+$ is then the trace formula
$$
\langle\tilde H\rangle_{0}=\mathrm{Tr}\big(|0\rangle\langle 0|\,\tilde H\big)=2\,\mathrm{Sc}\big(P_+(e_3)\tilde H\big),
$$
which is the Born rule of the informational sector specialized to the vacuum. This is the one place where the framework's vacuum is genuinely algebraic rather than transcribed.

**The field vacuum is not.** For a field, the vacuum is the $n=0$ term of a Fock space built from a module, and the companion article's finding applies unchanged: the Fock space is not a subalgebra of $\mathbb{B}$, and beyond one mode not even the operator algebra is. In particular the **photon vacuum is not an element of $\mathbb{B}$**, because there is no bosonic mode in the algebra at all: no pair $\tilde a,\tilde a^{\dagger}\in\mathbb{B}$ satisfies $[\tilde a,\tilde a^{\dagger}]=e_0$, since a commutator has vanishing trace while $\mathrm{Tr}(e_0)=2$. The electromagnetic vacuum is therefore the standard Fock vacuum of the mode algebra of *Canonical Quantization of the Biquaternion Maxwell Field*; the framework contributes the module on which it is built (the transverse polarization plane in the vector part of $\mathbb{M}_-$) and the notation, but no native ladder.

The honest summary is this: "the biquaternion vacuum" is not a biquaternion. For one fermionic mode it is an idempotent of $\mathbb{M}_+$; for a field it is a state in a module, and the algebra supplies neither the bosonic ladder that creates the photons nor, as the next section shows, a reason to prefer one regularisation of its energy over another.

## The Zero-Point Energy and the Trace Part

**From the mode expansion.** The free Maxwell potential expands in four covariant polarisations,
$$
\hat A_\mu(x)=\int\!\frac{d^{3}k}{(2\pi)^{3}}\frac{1}{\sqrt{2\omega_k}}\sum_{r=0}^{3}
\Big(\hat a_r(\mathbf{k})\,\epsilon^{(r)}_\mu(\mathbf{k})\,e^{-ik\cdot x}
+\hat a_r^{\dagger}(\mathbf{k})\,\epsilon^{(r)*}_\mu(\mathbf{k})\,e^{+ik\cdot x}\Big),
\qquad
\big[\hat a_r(\mathbf{k}),\hat a_s^{\dagger}(\mathbf{k}')\big]=\zeta_r\,\delta_{rs}\,(2\pi)^{3}\delta^{(3)}(\mathbf{k}-\mathbf{k}'),
$$
with $\zeta=(-1,+1,+1,+1)$ and $\omega_k=|\mathbf{k}|$ for the massless field. The normal-ordered Hamiltonian is
$$
:\!\hat H\!:\,=\sum_{r=0}^{3}\int\!\frac{d^{3}k}{(2\pi)^{3}}\,\zeta_r\,\omega_k\,\hat a_r^{\dagger}(\mathbf{k})\hat a_r(\mathbf{k}),
$$
and the constant discarded in passing to the normal-ordered form is the zero-point energy.

**Its value.** Reordering the modes produces, per mode, the contribution $\sum_r\zeta_r\,\tfrac12\hbar\omega_k$. Since
$$
\sum_{r=0}^{3}\zeta_r=-1+1+1+1=2,
$$
the zero-point constant of the covariant field is that of **two** transverse modes, $\hbar\omega_k$ per mode, and the free vacuum energy is the quartically divergent integral
$$
E_0=\sum_{r=0}^{3}\zeta_r\sum_{\text{modes}}\tfrac12\hbar\omega_k
=2\,V\!\int\!\frac{d^{3}k}{(2\pi)^{3}}\,\tfrac12\hbar c\,\lvert\mathbf{k}\rvert
\;\xrightarrow[\ \Lambda\ ]{}\;
\frac{\hbar c\,\Lambda^{4}}{8\pi^{2}}\,V .
$$
The coefficient is the free-space density for two polarisations; the divergence is quartic and proportional to the volume $V$. This is the biquaternion transcription of the standard fact that the electromagnetic zero-point energy diverges as the fourth power of the cutoff. The Dirac parent is the mirror case: there the normal-ordering constant is *negative*,
$$
E_0^{\mathrm{D}}=-\,2V\!\int\!\frac{d^{3}p}{(2\pi)^{3}}\,E_{\mathbf p},
$$
also quartically divergent, as that article records. The sign difference (positive for bosons, negative for the two fermion branches) is the standard one and is not removed by the framework.

**The zero-point energy is a central scalar.** In the framework the zero-point coefficient multiplies the identity $e_0$: it is a real number, hence an element of the **center** $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$ of $\mathbb{B}$. A central scalar commutes with every biquaternion and, in the evolution $\tilde\rho\mapsto\tilde U\tilde\rho\tilde U^{\dagger}$ with $\tilde U=e^{-i\tilde Ht/\hbar}$, contributes only a phase that cancels. This is exactly the statement of *The Harmonic Oscillator in Biquaternionic Form*: the trace part $h_0$ of a Hamiltonian is a central scalar, and "the zero-point energy is unobservable and the trace part of the Hamiltonian is a central scalar are the same statement". The trace formula makes "trace part" literal, $\mathrm{Tr}(\tilde H)=2\,\mathrm{Sc}(\tilde H)$.

This gives the framework's reading of the vacuum energy, and it is the reason the Casimir effect is the right place to look for it. A **constant** central scalar is unobservable; but if the constant depends on an external parameter — here the plate separation $a$ — its gradient is a force. The Casimir force is precisely the gradient of a central scalar, and it is observable for that reason. The algebra does not make the zero-point energy observable; it makes the *variation* of a central scalar observable, and that is all the Casimir effect requires.

## The Parallel-Plate Configuration and the Divergent Sum

**The configuration.** Two perfectly conducting parallel plates of area $A$, separated by a distance $a$ along $e_3$, bound a region of the vacuum. The plates are idealised: they impose $E_\parallel=0$ and $B_\perp=0$ on their surfaces, which is a boundary condition on the field, not a property of the algebra. It should be said at the outset that **the framework has no native description of a boundary**: the free-field algebra of the companion articles is formulated on the whole of spacetime, and the conductors are external structure. What the framework does supply is the space in which the mode structure is counted, as the next section makes precise.

**The modes.** Between the plates the longitudinal wavevector is quantized, $k_3=n\pi/a$, and the transverse wavevector $\mathbf{k}_\perp$ is continuous. The electromagnetic modes separate into
$$
\text{TE}_n:\ n=1,2,\dots,\qquad
\text{TM}_n:\ n=1,2,\dots,\qquad
\text{TEM}:\ n=0,
$$
each with frequency $\omega=c\sqrt{\mathbf{k}_\perp^{2}+(\pi n/a)^{2}}$. The TE and TM families each carry **one** polarization for every $n\ge1$; the single $n=0$ mode is the transverse electromagnetic (TEM) mode with $\omega=c|\mathbf{k}_\perp|$, independent of $a$. The bare zero-point energy per unit area of the plates is therefore
$$
\frac{E(a)}{A}=\frac{\hbar c}{2}\int\!\frac{d^{2}k_\perp}{(2\pi)^{2}}
\Bigg[\,2\sum_{n=1}^{\infty}\sqrt{\mathbf{k}_\perp^{2}+\Big(\frac{\pi n}{a}\Big)^{2}}
\;+\;|\mathbf{k}_\perp|\,\Bigg].
$$

**Why it diverges, and where.** The factor $2$ multiplies the two polarization families; the last term is the $a$-independent TEM mode. The sum $\sum_{n\ge1}$ and the integral over $\mathbf{k}_\perp$ both diverge at large arguments, and the divergence is not a defect of the notation: a momentum cutoff $\Lambda$ on the free vacuum gives, as in the previous section, an energy density $\hbar c\,\Lambda^{4}/(8\pi^{2})$ per unit volume, so the bare zero-point energy of any region of volume $V$ diverges as $\hbar c\,\Lambda^{4}V/(8\pi^{2})$, together with surface terms of order $\Lambda^{2}$ and a possible logarithm. The quantity in the bare zero-point sum above is not a number; it is a cutoff-dependent expression.

**The physical subtraction.** The Casimir energy is not the bare sum but the *change* in the zero-point energy produced by the plates. In the mode-density formulation this is
$$
\frac{E_{\mathrm{cas}}(a)}{A}
=\frac{\hbar c}{2}\int\!\frac{d^{2}k_\perp}{(2\pi)^{2}}
\Bigg[\,2\sum_{n=1}^{\infty}\sqrt{\mathbf{k}_\perp^{2}+\Big(\frac{\pi n}{a}\Big)^{2}}
\;-\;2\,\frac{a}{\pi}\int_{0}^{\infty}dq\,\sqrt{\mathbf{k}_\perp^{2}+q^{2}}\,\Bigg],
$$
in which the continuum integral $2\,\frac{a}{\pi}\int_0^\infty dq\,(\cdots)$ is the free-space zero-point energy per unit length at the same transverse momentum — the factor $a/\pi$ is the mode density of the discrete $k_3=\pi n/a$, and without it the two terms are not commensurable — and the TEM term has been dropped because it is $a$-independent and its contribution to the force vanishes. The subtraction is what the physical statement "the energy of the vacuum in the bounded region minus the energy of the same vacuum without the plates" means, and it is the subtraction that removes the volume divergence: the leading $\Lambda^{4}$ term is identical in the two configurations and cancels. What survives of the surface terms is an $a$-independent plate self-energy — a constant in $a$ — and, beyond it, a finite remainder that depends on $a$.

It has to be said clearly that this subtracted expression is still not an evaluable expression term by term. The two terms separately diverge; only their difference is finite, and it must be defined by a regularisation. The rest of the article evaluates that difference by two routes, and this is where the well-known trap lies.

**The Euler–Maclaurin route does not close the problem by itself.** A natural attempt is to expand the sum in this subtracted expression by the Euler–Maclaurin formula. That expansion correctly exhibits the divergence structure — the cutoff powers $\Lambda^{4},\Lambda^{2}$ and the surface terms — and the companion records the expansion explicitly. But for the summand
$$
g(x)=\sqrt{\mathbf{k}_\perp^{2}+\Big(\frac{\pi x}{a}\Big)^{2}},
$$
which is **even** in $x$ and **linearly growing**, the finite part produced by the naive form of Euler–Maclaurin is not the physical one. The reason is exact and worth stating: the finite remainder is sensitive to (i) the branch cut of $g$ in the complex plane and (ii) the discreteness (the floor) hidden in the mode count, neither of which the derivative-at-zero terms see. Applied naively, the odd-derivative terms all vanish and the formula returns an $a$-independent finite part — a spurious zero for the force. This is recorded here as a **finding, not smoothed over**: the divergence bookkeeping by Euler–Maclaurin is valid, but the finite Casimir term must be obtained from a regularisation whose continuation is controlled, which is what the next two sections do. The two routes that follow are independent of each other and agree.

## First Route: the Spectral Zeta Function

The spectral zeta function of the Dirichlet-type problem is
$$
\zeta_3(s)=\sum_{n=1}^{\infty}\int\!\frac{d^{2}k_\perp}{(2\pi)^{2}}\,
\Big(\mathbf{k}_\perp^{2}+\Big(\frac{\pi n}{a}\Big)^{2}\Big)^{-s},
$$
defined for $\mathrm{Re}\,s>\tfrac32$ and continued from there. The transverse integral is elementary,
$$
\int\!\frac{d^{2}k_\perp}{(2\pi)^{2}}\,\big(\mathbf{k}_\perp^{2}+m^{2}\big)^{-s}
=\frac{1}{4\pi}\,\frac{\Gamma(s-1)}{\Gamma(s)}\,m^{2-2s},
$$
so with $m=\pi n/a$,
$$
\zeta_3(s)=\frac{1}{4\pi}\frac{\Gamma(s-1)}{\Gamma(s)}\Big(\frac{\pi}{a}\Big)^{2-2s}\zeta(2s-2),
$$
where $\zeta$ on the right is the Riemann zeta function. The bare zero-point energy per unit area of the Dirichlet-type problem is recovered by continuing to $s=-\tfrac12$,
$$
\frac{E_{\mathrm{Dir}}}{A}=\frac{\hbar c}{2}\,\zeta_3\!\left(-\tfrac12\right),
$$
because the exponent $s$ is conjugate to the frequency, and this is the sense in which the "sum of half-quantum-per-mode" is the zeta function at $s=-\tfrac12$.

**Where the divergence went.** The continued zeta function has a pole where $\zeta(2s-2)$ has its pole, at $2s-2=1$, that is $s=\tfrac32$; this is the quartic volume divergence in disguise, and it sits exactly at the lower edge of the domain of convergence of the defining series, the boundary line $\mathrm{Re}\,s=\tfrac32$ of the half-plane $\mathrm{Re}\,s>\tfrac32$ in which the series converges. The continuation past the pole is unique given the functional equation of $\zeta$, and it is that uniqueness which makes the finite value at $s=-\tfrac12$ meaningful. In the language of the previous section: the pole is the cutoff divergence, and the analytic continuation is the statement that the divergence is a **local** term (a volume term, plus lower local terms) which is subtracted by the physical mode-density subtraction; the remaining finite part is universal. This is the justification of the regularisation, and it is the standard one.

**The value.** Evaluating the continued zeta function at $s=-\tfrac12$ uses
$$
\frac{\Gamma(-3/2)}{\Gamma(-1/2)}=-\frac23,\qquad \zeta(-3)=\frac{1}{120},
$$
giving
$$
\frac{E_{\mathrm{Dir}}}{A}
=\frac{\hbar c}{2}\cdot\frac{1}{4\pi}\Big(-\frac23\Big)\Big(\frac{\pi}{a}\Big)^{3}\frac{1}{120}
=-\frac{\pi^{2}\hbar c}{1440\,a^{3}} .
$$
This is the Casimir energy per unit area of a **single** massless scalar degree of freedom with Dirichlet-type boundary conditions. Every factor has been recomputed; in particular $\zeta(-3)=1/120$ and the gamma ratio $-2/3$ were checked independently.

## Second Route: the Heat Kernel and the Modular Relation

The second route uses the heat kernel rather than the mode sum directly, and it is independent of the first: it evaluates a convergent integral and uses $\zeta(4)=\pi^{4}/90$, not $\zeta(-3)$.

**The heat kernel.** For the Dirichlet-type problem the heat kernel per unit area is
$$
K(t)=\sum_{n=1}^{\infty}\int\!\frac{d^{2}k_\perp}{(2\pi)^{2}}\,
e^{-t(\mathbf{k}_\perp^{2}+(\pi n/a)^{2})}
=\frac{1}{4\pi t}\sum_{n=1}^{\infty}e^{-(\pi n/a)^{2}t},
$$
and the free-space heat kernel, which is its $a\to\infty$ limit, is
$$
K_\infty(t)=\frac{1}{4\pi t}\cdot\frac{a}{2\sqrt{\pi t}}=\frac{a}{8\pi^{3/2}t^{3/2}} .
$$
The **Jacobi modular relation** for the theta function,
$$
\sum_{n=-\infty}^{\infty}e^{-\alpha n^{2}}=\sqrt{\frac{\pi}{\alpha}}\sum_{m=-\infty}^{\infty}e^{-\pi^{2}m^{2}/\alpha},
$$
with $\alpha=\pi^{2}t/a^{2}$, gives the exact difference
$$
K(t)-K_\infty(t)=-\frac{1}{8\pi t}
+\frac{a}{4\pi^{3/2}t^{3/2}}\sum_{m=1}^{\infty}e^{-a^{2}m^{2}/t}.
$$
The first term is $a$-independent: it is a constant energy, contributes nothing to the force, and is the vestige of the surface divergence. The second term is the **Casimir part**: it is exponentially small as $t\to0$, so its zeta integral converges without any subtraction, and it vanishes as $a\to\infty$, which is what a Casimir energy must do. Its appearance from a modular transformation is the precise sense in which the finite part comes from the "winding" of the free modes around the compact direction of size $a$, not from the divergent mode count.

**The value.** The Casimir energy per unit area is
$$
\frac{E_{\mathrm{cas}}}{A}=\frac{\hbar c}{2}\,\frac{1}{\Gamma(-1/2)}\int_{0}^{\infty}t^{-3/2}\big[K(t)-K_\infty(t)\big]_{\mathrm{cas}}dt,
$$
and with the Casimir part of the exact heat-kernel difference the $t$-integral is elementary,
$$
\int_{0}^{\infty}t^{-3}\,e^{-a^{2}m^{2}/t}\,dt=\frac{1}{a^{4}m^{4}} .
$$
Therefore
$$
\frac{E_{\mathrm{cas}}}{A}
=-\frac{\hbar c}{16\pi^{2}a^{3}}\sum_{m=1}^{\infty}\frac{1}{m^{4}}
=-\frac{\hbar c}{16\pi^{2}a^{3}}\cdot\frac{\pi^{4}}{90}
=-\frac{\pi^{2}\hbar c}{1440\,a^{3}},
$$
in agreement with the Dirichlet-scalar result. The agreement of two routes that use different special values ($\zeta(-3)$ versus $\zeta(4)$) and different manipulations (analytic continuation of a divergent sum versus a modular identity on a convergent difference) is the verification the subject requires. The modular route also makes the location of the divergence explicit: it is the $a$-independent term $-(8\pi t)^{-1}$, which is removed by the physical subtraction and carries no force.

**A different case, checked.** The same machinery on the one-dimensional problem — a massless scalar between two Dirichlet points — gives
$$
E_{1\mathrm{D}}=-\frac{\pi\hbar c}{24\,a},
$$
which the zeta route reproduces from $\zeta(-1)=-\tfrac1{12}$ and the heat-kernel route from $\zeta(2)$. Both the three-dimensional and the one-dimensional results were recomputed from the definitions, and the numerical value of the three-dimensional sum was confirmed against the closed form (details in the companion). The reason to check two cases is the discipline of the corpus: a formula that agrees with the case that suggested it is not thereby verified.

## The Polarizations and the Factor of Two

The two routes above computed the **Dirichlet-scalar** energy for a single massless scalar degree of freedom. The electromagnetic Casimir energy is **twice** it, and this factor is where the classic error lives. It has three equivalent descriptions, and they must be kept distinct.

**From the mode count.** In the bare zero-point sum above the factor $2$ multiplies $\sum_{n\ge1}$ and stands for the TE and TM families, one polarization each, both with $n\ge1$. The single remaining mode, the $n=0$ TEM mode, has frequency $c|\mathbf{k}_\perp|$ independent of $a$ and contributes nothing to the force. The $a$-dependent part of the electromagnetic zero-point sum is therefore exactly **two** Dirichlet-type sums, hence
$$
\frac{E_{\mathrm{EM}}}{A}=2\cdot\Big(-\frac{\pi^{2}\hbar c}{1440\,a^{3}}\Big)=-\frac{\pi^{2}\hbar c}{720\,a^{3}} .
$$

**From the indefinite metric.** In the covariant mode algebra the four polarisations carry the metric $\zeta=(-1,+1,+1,+1)$, and the zero-point constant is $\sum_r\zeta_r\,\tfrac12\hbar\omega=2\cdot\tfrac12\hbar\omega$. The timelike mode's negative sign is essential: summing four polarisations with a positive sign would give $4\cdot\tfrac12\hbar\omega$, **double** the correct zero-point energy. The indefinite metric is not a technicality of the covariant gauge; it is what makes the mode count come out right.

**From the algebra.** Both descriptions have the same home in the framework. The four polarization directions of the covariant treatment are the four directions $\{ie_0,e_1,e_2,e_3\}$ of the material sector, and the metric $\zeta$ is the norm form $N(\tilde X)=|\mathbf{q}|^{2}-q_0^{2}$ of $\mathbb{M}_-$, as *The Photon in Biquaternionic Form* establishes. The **two physical polarisations** are the plane in the vector part of $\mathbb{M}_-$ orthogonal to the propagation direction $\hat{\mathbf{k}}$, with projector $P_{ij}=\delta_{ij}-\hat k_i\hat k_j$. The factor of two is thus native: it is the dimension of the transverse plane fixed by the algebra's own norm form. What is **not** native is the **removal** of the timelike and longitudinal directions: the algebra supplies the indefinite metric and the transverse plane, but the subsidiary condition that discards the unphysical directions is imported, exactly as the canonical-quantisation article records.

The three descriptions agree, and the agreement is the check on the factor of two: the mode count gives $2$; the indefinite metric gives $\sum_r\zeta_r=2$; the algebra gives the two-dimensional transverse plane. A reader who counts four polarisations with positive weight, or who forgets that the TEM mode is $a$-independent, will be wrong by a factor of two or by an additive constant, and neither error is visible in the final number without this bookkeeping.

## The Casimir Force: Sign Convention and Two Verifications

**Sign convention.** Let $E(a)$ be the vacuum energy of the bounded region at separation $a$, per unit area. The force per unit area on a plate is
$$
\frac{F}{A}=-\frac{\partial}{\partial a}\frac{E(a)}{A},
$$
so a **negative** $F$ is a force that pulls the plates together (attractive), and the corresponding pressure between the plates is a tension. This is the convention used throughout.

**Route one.** Differentiating the electromagnetic energy, which is twice the Dirichlet-scalar result,
$$
\frac{E_{\mathrm{EM}}}{A}=-\frac{\pi^{2}\hbar c}{720\,a^{3}}
\quad\Longrightarrow\quad
\frac{F_{\mathrm{EM}}}{A}
=-\frac{\partial}{\partial a}\Big(-\frac{\pi^{2}\hbar c}{720\,a^{3}}\Big)
=-\frac{\pi^{2}\hbar c}{240\,a^{4}}<0 .
$$
The force is **attractive**. Note the sign chain: $E$ is negative and *increases* with $a$ (it goes to zero from below), so its derivative is positive and the force is negative.

**Route two.** The heat-kernel expression gives the same energy as a function of $a$ before any differentiation: the Casimir part of the exact heat-kernel difference scales as $a^{-3}$, so $E_{\mathrm{EM}}/A\propto a^{-3}$ and the force is $3$ times the energy per unit area divided by $a$,
$$
\frac{F_{\mathrm{EM}}}{A}=\frac{3}{a}\cdot\Big(-\frac{\pi^{2}\hbar c}{720\,a^{3}}\Big)=-\frac{\pi^{2}\hbar c}{240\,a^{4}} .
$$
The scaling argument uses only the $a^{-3}$ dependence that the modular relation exhibits term by term; it is genuinely independent of the differentiation of the zeta result.

Both routes give $-\pi^{2}\hbar c/(240a^{4})$, and both were recomputed symbolically along with the energies. The one-dimensional case gives the same structure, $E_{1\mathrm{D}}=-\pi\hbar c/(24a)$ and $F_{1\mathrm{D}}=-\pi\hbar c/(24a^{2})$, attractive, as a second case on which the sign convention was checked. The force is **attractive** in both. It is worth restating that this is the standard electromagnetic Casimir result, reproduced and not modified: the framework's contribution here is the polarisation bookkeeping and the central-scalar reading, not a new force.

## What the Framework Supplies and What It Imports

| Feature | Status in the framework | Where it comes from |
|---|---|---|
| Vacuum state (one fermionic mode) | Native | idempotent $P_+(e_3)=\tfrac12(e_0+ie_3)\in\mathbb{M}_+$; trace formula |
| Vacuum expectation values (one mode) | Native | $\langle\tilde H\rangle_0=2\,\mathrm{Sc}(P_+(e_3)\tilde H)$ |
| Fermion parity of the vacuum | Native | $(-1)^F=ie_3$ |
| Zero-point energy as a central scalar | Native (reading) | trace part of $\tilde H$; commutes |
| Two physical transverse polarisations | Native | $\hat{\mathbf{k}}$-orthogonal plane in $\mathrm{Vect}(\mathbb{M}_-)$ |
| Indefinite metric $\zeta=(-1,+1,+1,+1)$ | Native | norm form of $\mathbb{M}_-$ |
| Factor of two (EM vs Dirichlet scalar) | Native | $\sum_r\zeta_r=2$; two transverse polarisations |
| Photon Fock vacuum | Imported | no bosonic ladder in $\mathbb{B}$ |
| Field mode algebra and Fock space | Imported | standard quantisation on a module |
| Conducting plates and boundary conditions | Imported | no native description of a boundary |
| Gauge removal of timelike/longitudinal | Imported | subsidiary condition; no algebraic principle |
| Regularisation / analytic continuation | Imported | algebra selects no regularisation |
| The numerical Casimir coefficient | Standard | reproduced, not derived from $\mathbb{B}$ |

**What the algebra supplies.** The one-mode vacuum and its expectation values; the central-scalar character of the zero-point energy; the transverse plane and the indefinite metric that fix the polarisation count. These are genuine and are the framework's specific content for this problem.

**What the algebra does not supply.** The bosonic ladder (so the photon vacuum is not an algebra element); the boundary conditions imposed by the conductors; the regularisation that extracts the finite part of the divergent sum; and the gauge removal of the unphysical polarisations. It also supplies no modification of the numerical result: the Casimir force is reproduced.

## Boundaries, the Local Complex Structure, and the Lifshitz Direction

The one structural feature of the framework that bears on boundaries is the **local complex structure**. In the framework the speed of light in a medium, $c=1/\sqrt{\epsilon\mu}$, is local, and the material sector's complex structure is a local structure that changes from point to point; this is developed in *Electromagnetism in Media — The Local Complex Structure at Work*. An interface at which $\epsilon$ and $\mu$ jump is the framework's natural generalisation of a "plate": a boundary is a place where the local complex structure is discontinuous.

This suggests, but does not establish, a genuinely biquaternionic route to the finite-temperature and dielectric Casimir effect of **Lifshitz**: the force between two media characterised by reflection coefficients is obtained from the vacuum mode structure of a locally complex medium, and the framework's local $c$ is the parameter in which those interfaces are written. It is recorded here as a **direction, not a result**: no reflection coefficient has been computed from the algebra, no dielectric Casimir force has been derived, and the perfectly conducting plate used above is recovered only in the limit of an infinite-contrast interface. The suggestion is that the framework's local complex structure may be the natural home for the boundaries that the free-field algebra does not describe; whether it is remains open.

## Open Questions

1. **The regularisation principle.** The algebra contains no criterion selecting a regularisation; both routes above imported the standard analytic continuation. Is there any biquaternion structure — for instance, the uniqueness of the continuation of a sector-valued zeta function — that could select one, or is the choice irreducibly extrinsic? The parents record the same openness for the zero-point energy.

2. **The central-scalar reading.** The zero-point energy is a central scalar and its *variation* is observable. Is the identification of "vacuum energy" with "the scalar part of $\tilde H$" more than a reading, or does it have content — for example, a statement about which quantities can appear in a force?

3. **Native boundaries.** Can the conducting plate be described as an interface of the local complex structure, so that the boundary condition is derived rather than imposed? This is the most concrete route by which the framework might add something to the standard Casimir calculation, and it is not taken here.

4. **The sector straddle and the vacuum.** The canonical-quantisation article leaves undecided whether $\tilde A\in\mathbb{M}_-$ and $\tilde\pi\in\mathbb{M}_+$ has algebraic content. The vacuum is neutral under the sector structure in the sense that its projector lies in $\mathbb{M}_+$ while the potential lies in $\mathbb{M}_-$; whether the vacuum state straddles the sectors in a meaningful way is open.

5. **Fermionic vacuum energy and the sign.** The Dirac parent's normal-ordering constant is negative and quartically divergent. The framework gives the bosonic and fermionic constants opposite signs by transcription. Whether the algebra relates the two signs — supersymmetric cancellation, or a sector statement — is not addressed here.

6. **Thermal connection.** The vacuum is the zero-temperature endpoint of the thermal state of *The Partition Function in Biquaternionic Form*, whose imaginary time is the KMS direction of *The KMS Condition and the Biquaternion Framework*. Whether the Casimir energy is the $T\to0$ limit of a biquaternionic free energy, with the plate separation entering the modular parameter, is a natural question this article does not settle.

7. **Empirical content.** The Casimir force is reproduced, not modified, so this subject supplies no discriminator between the framework and standard quantum electrodynamics. As everywhere in the series, the framework-level question of empirical contact remains open.

## Summary

The **vacuum state** of the biquaternion framework is not a biquaternion. For a **single fermionic mode** it is genuinely algebraic: the vacuum projector is the idempotent $|0\rangle\langle 0|=P_+(e_3)=\tfrac12(e_0+ie_3)\in\mathbb{M}_+$, and vacuum expectation values are given by the trace formula $2\,\mathrm{Sc}(P_+(e_3)\tilde H)$. For a **field** it is the standard Fock vacuum of a module, because the algebra contains no bosonic ladder: no pair in $\mathbb{B}$ satisfies $[\tilde a,\tilde a^{\dagger}]=e_0$, since a commutator has vanishing trace while $\mathrm{Tr}(e_0)=2$.

The **zero-point energy** of the free Maxwell field is a central scalar — the trace part of the Hamiltonian, a multiple of $e_0$ — and is therefore unobservable as a constant, in the same sense as the harmonic oscillator's trace part. Its dependence on the plate separation is what is observable. The bare Casimir mode sum diverges quartically, with cutoff powers $\Lambda^{4}$ and $\Lambda^{2}$ and surface terms; the physical mode-density subtraction cancels the volume divergence and leaves behind only $a$-independent plate self-energies and a finite, $a$-dependent remainder.

That remainder was obtained by two independent regularisations. The **spectral zeta function** route continues $\zeta_3(s)$ from $s>\tfrac32$ through the pole of $\zeta(2s-2)$ at $s=\tfrac32$ to $s=-\tfrac12$, and gives, for one Dirichlet-type scalar degree of freedom, $-{\pi^{2}\hbar c}/({1440\,a^{3}})$. The **heat-kernel** route uses the Jacobi modular relation to write the exact difference between the bounded and free heat kernels, isolates the Casimir part as the exponentially small "winding" sum, and integrates it to the same value using $\zeta(4)=\pi^{4}/90$. The two routes use different special values and different manipulations; they agree.

The **electromagnetic** result is twice the Dirichlet-scalar result, $E_{\mathrm{EM}}/A=-{\pi^{2}\hbar c}/({720\,a^{3}})$, because the $a$-dependent mode count is the TE and TM families with one polarization each. Equivalently, the indefinite metric $\zeta=(-1,+1,+1,+1)$ of the covariant quantisation sums to $2$; and the framework identifies $\zeta$ with the norm form of the material sector $\mathbb{M}_-$ and the two physical polarisations with the transverse plane in its vector part. The factor of two is native; the gauge removal of the timelike and longitudinal directions is imported.

The **force** per unit area, with the convention $F/A=-\partial_a(E/A)$, is
$$
\frac{F_{\mathrm{EM}}}{A}=-\frac{\pi^{2}\hbar c}{240\,a^{4}},
$$
**attractive**; the one-dimensional scalar check gives the same sign. The result is the standard Casimir force, reproduced rather than modified.

Two gaps are left visible. The algebra has no native bosonic ladder, so the photon vacuum and its mode algebra are imported; and it has no native description of a boundary or of a regularisation, so the plates, the boundary conditions, and the analytic continuation are all external. The framework's own contribution is the one-mode vacuum, the central-scalar reading of the zero-point energy, and the polarisation bookkeeping — and the suggestion, left open, that the local complex structure is the natural home for boundaries.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_\mathbb{R}\{e_0,ie_0\}$ | Center of the algebra; home of the zero-point scalar |
| $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ | Trace formula; $\mathrm{Tr}(e_0)=2$ |
| $\tilde a_{\mathrm{tr}},\tilde a_{\mathrm{tr}}^\dagger$ | One-mode ladder, $\{\tilde a_{\mathrm{tr}},\tilde a_{\mathrm{tr}}^\dagger\}=e_0$ |
| $\tilde N_{\mathrm{tr}}=\tfrac12(e_0-ie_3)$ | One-mode number operator (idempotent) |
| $\vert 0\rangle\langle 0\vert=P_+(e_3)=\tfrac12(e_0+ie_3)$ | One-mode vacuum projector (idempotent in $\mathbb{M}_+$) |
| $(-1)^F=ie_3$ | Fermion parity (single mode) |
| $\vert 0\rangle$ | Field vacuum, degree-zero term of the Fock space |
| $\hat a_r,\hat a_r^\dagger$, $\epsilon^{(r)}_\mu$ | Covariant mode operators and polarization vectors |
| $\zeta=(-1,+1,+1,+1)$ | Indefinite metric; norm form $N(\tilde X)=\lvert\mathbf{q}\rvert^2-q_0^2$ of $\mathbb{M}_-$ |
| $\hat{\mathbf{k}}$ | Propagation direction; transverse plane $P_{ij}=\delta_{ij}-\hat k_i\hat k_j$ |
| $a$, $A$ | Plate separation and area |
| $a,n,k_3=\pi n/a$ | Plate separation; mode index; quantized longitudinal wavevector |
| $\mathbf{k}_\perp$ | Continuous transverse wavevector |
| $\omega=c\sqrt{\mathbf{k}_\perp^2+(\pi n/a)^2}$ | Mode frequency; $\omega=c\lvert\mathbf{k}_\perp\rvert$ for the $n=0$ TEM mode |
| $E(a)$, $E_{\mathrm{cas}}$ | Zero-point energy of the bounded region; Casimir energy |
| $F/A=-\partial_a(E/A)$ | Force per unit area; negative $=$ attractive |
| $\Lambda$ | Momentum cutoff (bare divergence) |
| $\zeta_3(s)$ | Spectral zeta function of the Dirichlet-type problem |
| $\zeta(s)$ | Riemann zeta; $\zeta(-3)=1/120$, $\zeta(-1)=-1/12$, $\zeta(4)=\pi^4/90$ |
| $K(t)$, $K_\infty(t)$ | Heat kernel of the bounded and free problems |
| $E_{\mathrm{EM}}/A=-\pi^2\hbar c/(720a^3)$ | Electromagnetic Casimir energy per unit area (attractive) |
| $F_{\mathrm{EM}}/A=-\pi^2\hbar c/(240a^4)$ | Electromagnetic Casimir force per unit area (attractive) |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- H. B. G. Casimir, "On the attraction between two perfectly conducting plates," *Proc. K. Ned. Akad. Wet.* **51** (1948) 793–795, for the original prediction.
- H. B. G. Casimir and D. Polder, "The influence of retardation on the London–van der Waals forces," *Physical Review* **73** (1948) 360–372, for the retarded van der Waals force and its relation to the plate result.
- E. M. Lifshitz, "The theory of molecular attractive forces between solids," *Soviet Physics JETP* **2** (1956) 73–83, for the general dielectric formulation and the reflection-coefficient route to boundaries.
- M. Bordag, U. Mohideen, and V. M. Mostepanenko, "New developments in the Casimir effect," *Physics Reports* **353** (2001) 1–205, for the modern review, the mode-density subtraction, and the zeta and heat-kernel regularisations used here.
- K. A. Milton, *The Casimir Effect: Physical Manifestations of Zero-Point Energy* (World Scientific, 2001), for the zero-point-energy derivation and its regularisation.
- S. K. Blau, M. Visser, and A. Wipf, "Zeta functions and the Casimir energy," *Nuclear Physics B* **310** (1988) 163–180, for the spectral-zeta treatment of Casimir energies.
- J. S. Dowker and R. Critchley, "Effective Lagrangian and energy–momentum tensor in de Sitter space," *Physical Review D* **13** (1976) 3224–3232, for the proper-time and heat-kernel method used in the second route.
- L. H. Ford, "Casimir force between a dielectric and a perfectly conducting wall," *Physical Review A* **48** (1993) 2962–2968, for the material dependence that a native boundary description would have to reproduce.
- P. W. Milonni, *The Quantum Vacuum: An Introduction to Quantum Electrodynamics* (Academic Press, 1994), for the zero-point energy, normal ordering, and the vacuum-energy interpretation.
- Companion articles: *Canonical Quantization of the Biquaternion Maxwell Field*; *Canonical Quantization of the Biquaternion Dirac Field*; *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*; *The Photon in Biquaternionic Form*; *The Harmonic Oscillator in Biquaternionic Form*; *The Partition Function in Biquaternionic Form*; *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*; *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*.
