# __The Photon in Biquaternionic Form__

## Introduction

The photon is the quantum of the electromagnetic field: massless, chargeless, of spin one, with two transverse polarizations and helicities $\pm 1$, and its own antiparticle. In the biquaternion framework of this series the electromagnetic field is the **biquaternion Maxwell field** $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ of the companion article *Maxwell's Equations in the Biquaternionic Formulation*, and its quantization is the Gupta–Bleuler construction of *Canonical Quantization of the Biquaternion Maxwell Field*. The photon is the one-particle state of that field.

A framework that reformulates known physics can be read generously or carefully. Read generously, every correct statement about light becomes a statement the framework "contains"; read carefully, most of them are properties of Maxwell's equations and of canonical quantization that the framework transcribes, and the specific facts attached to the photon must be supplied from outside. This article takes the second interpretation and asks the question that the quantization article leaves explicitly open: **do the two transverse polarizations, and their helicities, have a native meaning in the algebra — for instance, in the vector part of the material sector?**

The answer, stated at the outset, has three positive parts and four negative ones. The positive parts are these.

1. **The polarization space is the material sector.** The four polarization vectors of the covariant treatment are the four directions of $\mathbb{M}_-$, and the indefinite metric $\zeta = (-1,+1,+1,+1)$ of Gupta–Bleuler is the biquaternion norm of $\mathbb{M}_-$ that the framework already carries. The two physical polarizations are the plane in the vector part of $\mathbb{M}_-$ orthogonal to the propagation direction $\vec u_k$.
2. **Circular polarization is the algebra's complex structure acting on the propagation direction.** The two circular polarization vectors are the eigenvectors of left multiplication by $\vec u_k$ with eigenvalues $\mp i$. The **helicity operator** is $\lambda = \vec u_k\cdot\vec S = i\,\mathrm{Vect}(\vec u_k\,\cdot\,) = \tfrac{i}{2}\mathrm{ad}_{\vec u_k}$, represented by the Hermitian element $i\vec u_k$ of the informational sector $\mathbb{M}_+$, with spectral values $\{+1,0,-1\}$. Its $\pm1$ eigenvectors are exactly the two physical polarizations, and its $0$ eigenvector is the longitudinal direction $\vec u_k$, which the gauge structure removes.
3. **The two helicities are the two halves of the field strength.** They are the self-dual and anti-self-dual parts of $\tilde{F}$, in the decomposition established in *The Field-Strength Biquaternion and Its Invariants*.

The negative parts are equally specific.

4. **No ladder.** There is no bosonic creation or annihilation operator in $\mathbb{B}$ (the trace of a commutator vanishes, while $\mathrm{Tr}(e_0)=2$), so the photon number operator $N_\gamma$ is not an element of the algebra. The ladder algebra is imported, as *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* records.
5. **No gauge-fixing principle.** The algebra offers no reason to prefer one gauge to another, so although the transverse plane is native, the *reduction* from four polarizations to two is imposed from outside.
6. **Masslessness is inserted.** Nothing in the algebra fixes $m=0$. Masslessness is what makes helicity Lorentz invariant and what makes the third helicity unphysical; the framework represents the massive (Proca) alternative as readily as the massless one.
7. **Interactions, and any empirical signature that would distinguish the framework from standard electrodynamics, lie outside** the free field treated here.

A second, less comfortable point belongs in the introduction. Almost every statement the framework makes about "the photon" is a statement about a general massless spin-one field. The algebra does not single the photon out; it describes a massless gluon in the abelian idealization, a massive Proca field if a mass is added, and any other spin-one field by the same objects.

**Conventions.** The notation is inherited unchanged from the read list. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, $e_je_k=\epsilon_{jkl}e_l$ for $j\neq k$, and central scalar imaginary $i$ with $i^2=-1$. The material and informational sectors are

$$
\mathbb{M}_- = \{\tilde{Q} : \tilde{Q}^{*} = -\tilde{Q}\} = \mathrm{span}_\mathbb{R}\{ie_0, e_1, e_2, e_3\},
\qquad
\mathbb{M}_+ = \{\tilde{Q} : \tilde{Q}^{*} = \tilde{Q}\} = \mathrm{span}_\mathbb{R}\{e_0, ie_1, ie_2, ie_3\},
$$

with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ and $i\mathbb{M}_\pm=\mathbb{M}_\mp$. The isomorphism with $M_2(\mathbb{C})$ is $\mathsf{M}_2(e_k)=-i\sigma_k$, $\mathsf{M}_2(ie_k)=\sigma_k$, and the trace formula is $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H}) = 2\langle\tilde{P},\tilde{H}\rangle$. The biquaternionic gradient is $\tilde{\nabla}=e_0\partial_{ict}+e_1\partial_x+e_2\partial_y+e_3\partial_z$, the field strength is $\tilde{F}=i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H$, and for the free field we set $\epsilon=\epsilon_0$, $\mu=\mu_0$ and use natural units $\hbar=c=1$, in which $c=1/\sqrt{\epsilon\mu}$ gives $\tilde{F}=i\vec E-\vec H$. The Riemann–Silberstein vector is $\vec N=\vec E+ic\vec B$ with $\vec B=\mu\vec H$, so that $\tilde{F}=i\sqrt{\epsilon}\,\vec N$. The spacetime metric of the $ict$ sector is $\eta=\mathrm{diag}(-1,+1,+1,+1)$.

## The Photon as the Quantum of the Biquaternion Maxwell Field

The classical theory is the single equation $\tilde{\nabla}\tilde{F}=-\tilde{R}$ for the field strength; the sources vanish for the free field, and the equation is then $\tilde{\nabla}\tilde{F}=0$. A plane-wave solution with four-wavevector $\tilde{K}=i\omega\,e_0+\vec k$ and complex amplitude $\vec F$ has

$$
\omega = c|\vec k|, \qquad \vec k\cdot\vec F = 0,
$$

the first the massless dispersion and the second the transversality inherited from $\mathrm{div}\,\vec D=0$ and $\mathrm{div}\,\vec B=0$. The one-particle space at each momentum is the space of transverse amplitudes, and it is two-dimensional; the photon states are the vectors of this space.

The dictionary that places the photon's data in the algebra is the following.

| Photon datum | Biquaternion object |
|---|---|
| The field | $\tilde{F}=i\sqrt{\epsilon}\,\vec N\in\mathbb{B}$, vanishing scalar part, mixed real/imaginary vector part |
| Free equation | $\tilde{\nabla}\tilde{F}=0$ |
| Potential | $\tilde{A}=i\phi/c\,e_0+\vec A\in\mathbb{M}_-$ |
| Polarization directions | the four basis directions $\{ie_0,e_1,e_2,e_3\}$ of $\mathbb{M}_-$ |
| Physical polarizations | the plane in $\mathrm{Vect}(\mathbb{M}_-)$ orthogonal to $\vec u_k$ |
| Helicity states | the $\pm1$ eigenvectors $\varepsilon^{\mathrm{fop}}_\pm$ of the $\mathbb{M}_+$ element $i\vec u_k$ |
| Helicity observable | $\lambda=\tfrac{i}{2}\mathrm{ad}_{\vec u_k}$, represented by the $\mathbb{M}_+$ element $i\vec u_k$ |
| Conserved energy–momentum | $\tilde{W}=\tfrac12\tilde{F}\tilde{F}^{*}=W+\tfrac{i}{c}\vec S\in\mathbb{M}_+$, with $\vec S$ the **Poynting vector** |
| Photon number | $N_\gamma$ (transverse sum) — **not** in $\mathbb{B}$ |

Two structural observations follow from the table. The field-strength-like datum $\tilde{F}$ is in neither sector: it has vanishing scalar part and a vector part that is part electric (imaginary) and part magnetic (real), which is why it is not an element of $\mathbb{M}_-$ even though it is built from the potentials. The polarization *directions*, by contrast, are real spatial vectors and do sit in the material sector; this is the observation that the quantization article invited, and the next section makes it precise.

## The Polarization Space Is the Material Sector

The covariant quantization expands the potential in four polarizations,

$$
A_\mu(x) = \int \frac{d^3k}{(2\pi)^3}\frac{1}{\sqrt{2\omega_k}}\sum_{r=0}^{3}\Bigl(a^{\mathrm{fop}}_r(\vec k)\,\epsilon^{(r)}_\mu(\vec k)\,\exp(-ik\cdot x) + a^{\mathrm{fop}\dagger}_r(\vec k)\,\epsilon^{(r)*}_\mu(\vec k)\,\exp(+ik\cdot x)\Bigr),
$$

with $\eta_{\mu\nu}\epsilon^{(r)\mu}\epsilon^{(s)\nu}=\zeta_r\delta_{rs}$ and $\zeta=(-1,+1,+1,+1)$. The vectors $\epsilon^{(1)},\epsilon^{(2)}$ are the two real spatial directions transverse to $\vec u_k$, $\epsilon^{(3)}=\vec u_k$ is longitudinal, and $\epsilon^{(0)}$ is timelike.

The point of the framework is that these four directions are already present in the algebra, in the material sector. Writing a general element of $\mathbb{M}_-$ as $\tilde{Q}=iq_0e_0+\vec q$ with $q_0$ real and $\vec q$ a real pure quaternion, its biquaternion norm is

$$
\langle\tilde{Q}\rangle_{\natural} = |\vec q|^2 - q_0^2 ,
$$

an indefinite quadratic form of signature $(-1,+1,+1,+1)$. The four basis directions are $ie_0$ (the timelike direction, matching $\epsilon^{(0)}$) and $e_1,e_2,e_3$ (the spatial directions, matching $\epsilon^{(1)},\epsilon^{(2)},\epsilon^{(3)}$). So:

> **The polarization vectors of the covariant quantization are the four directions of the material sector $\mathbb{M}_-$, and the indefinite metric $\zeta=(-1,+1,+1,+1)$ is the biquaternion norm of $\mathbb{M}_-$.**

This is the precise sense in which the polarization space is native. The framework does not merely "also have" an indefinite four-dimensional space; it is the same space, with the same metric, that appears in the Gupta–Bleuler expansion.

The physical polarizations are the two spatial directions orthogonal to the propagation direction. Let $\vec u_k$ be the unit vector along $\vec k$, and let $\varepsilon^{\mathrm{fop}}_1,\varepsilon^{\mathrm{fop}}_2$ be a right-handed orthonormal pair with $(\varepsilon^{\mathrm{fop}}_1,\varepsilon^{\mathrm{fop}}_2,\vec u_k)$ a right-handed triad. Transversality is the statement that the physical amplitudes lie in the orthogonal complement of $\vec u_k$ inside the vector part of $\mathbb{M}_-$, whose projector is

$$
P_{ij} = \delta_{ij} - \vec u_k_i \vec u_k_j, \qquad \sum_{r=1}^{2}\varepsilon^{\mathrm{fop}( r)}_i \varepsilon^{\mathrm{fop}(r)}_j = P_{ij}.
$$

The polarization sum that the parent article records is thus the statement that the physical polarization space is the $\vec u_k$-orthogonal plane, an object defined by the algebra's own biquaternion norm.

The statement was checked on a direction that did not suggest it. On the axis $\vec u_k=(0,0,1)$ the projector is $\mathrm{diag}(1,1,0)$; on the tilted rational direction $\vec u_k=(3,4,0)/5$ and on $\vec u_k=(1,2,2)/3$ the polarization sums reproduce $\delta_{ij}-\vec u_k_i\vec u_k_j$ exactly, with rational orthonormal frames chosen independently for each case (details in the companion).

## Circular Polarization and the Complex Structure of the Propagation Direction

The two linear polarizations are real; the two circular polarizations are the combinations

$$
\varepsilon^{\mathrm{fop}}_\pm = \frac{1}{\sqrt 2}\bigl(\varepsilon^{\mathrm{fop}}_1 \pm i\,\varepsilon^{\mathrm{fop}}_2\bigr),
$$

which are complex combinations and therefore do not lie in $\mathbb{M}_-$ itself, but in its complexification, the vector part of $\mathbb{B}$. Their defining property is a statement about quaternion multiplication by the propagation direction. Using $e_je_k=\epsilon_{jkl}e_l$ for $j\neq k$ together with the definition of the circular combination, one computes

$$
\vec u_k\,\varepsilon^{\mathrm{fop}}_\pm = \mp\, i\,\varepsilon^{\mathrm{fop}}_\pm .
$$

**The two circular polarization vectors are the eigenvectors of left multiplication by $\vec u_k$, with eigenvalues $\mp i$.** Equivalently, left multiplication by the Hermitian element $i\vec u_k$ acts on the complexified vector part as the identity on $\varepsilon^{\mathrm{fop}}_+$, as minus the identity on $\varepsilon^{\mathrm{fop}}_-$, and carries the longitudinal vector to the scalar direction: $i\vec u_k\,\varepsilon^{\mathrm{fop}}_\pm=\pm\varepsilon^{\mathrm{fop}}_\pm$ and $i\vec u_k\,\vec u_k=-i\,e_0$.

This is a native characterization of circular polarization, and it is worth naming what plays which role. The algebra's scalar imaginary $i$ is the complex structure; the propagation direction $\vec u_k$ is a real unit quaternion, an element of the material sector; and left multiplication by $\vec u_k$ is the operation whose $\pm i$ eigenvectors the circular polarizations are. The two signs are the two senses of rotation about the propagation axis, and they are the two helicities.

The circular basis is complete in the same plane. With $\varepsilon^{\mathrm{fop}}_+\!\cdot\!\varepsilon^{\mathrm{fop}}_-=1$ and $\varepsilon^{\mathrm{fop}}_\pm\!\cdot\!\varepsilon^{\mathrm{fop}}_\pm=0$ (the complex-bilinear dot product), one has

$$
\varepsilon^{\mathrm{fop}(+)}_i \varepsilon^{\mathrm{fop}(-)}_j + \varepsilon^{\mathrm{fop}(-)}_i \varepsilon^{\mathrm{fop}(+)}_j = \delta_{ij} - \vec u_k_i\vec u_k_j ,
$$

the same transverse projector as before, now written in the circular basis.

Both the eigenvalue relation and the circular completeness relation were checked exactly on three independent directions — $\vec u_k=(0,0,1)$, $(3,4,0)/5$, and $(1,2,2)/3$ — in an exact arithmetic over $\mathbb{Q}(\sqrt2)$ so that the $\sqrt2$ of the circular combinations is kept exactly. The second and third directions were chosen after the relation was written down, not from the case that suggested it, and both hold.

## Helicity as an Observable in the Informational Sector

The helicity of a spin-one particle is the projection of its spin along the momentum. In the algebra, spin is the adjoint action on the imaginary quaternions: the rotation generators are the real pure quaternions $e_k\in\mathbb{M}_-\cap\mathbb{H}_{\mathbb{B}}$, acting by $\mathrm{ad}_{e_k}/2 = e_k\times$ (the angular-momentum article normalizes the same generators as $g_k=-\tfrac12 e_k$, so its generator is $-e_k/2$ where this section uses $e_k$), and the observable is $i$ times the generator, exactly as the spin-$\tfrac12$ observable is $\tfrac{\hbar}{2}ie_k$ in the angular-momentum article. The helicity observable is therefore

$$
\lambda = \frac{i}{2}\,\mathrm{ad}_{\vec u_k} = i\,\mathrm{Vect}(\vec u_k\,\cdot\,) = \vec u_k\cdot\vec S,
$$

where $\vec S$ is the **spin** vector of the angular-momentum article (a different object from the Poynting vector $\vec S$ of the energy–momentum table above, which this auxiliary symbol unfortunately shares). On the complexified vector part, $\lambda$ is the vector part of left multiplication by the Hermitian element $i\vec u_k\in\mathbb{M}_+$: $\lambda = \mathrm{Vect}\circ(\text{left multiplication by } i\vec u_k)$. Its action on the circular basis is diagonal:

$$
\lambda\,\varepsilon^{\mathrm{fop}}_\pm = \pm\,\varepsilon^{\mathrm{fop}}_\pm, \qquad \lambda\,\vec u_k = 0 .
$$

So the helicity operator has spectrum $\{+1,0,-1\}$ on the complexified vector part. The $\pm1$ eigenvectors are the two circular polarizations; the $0$ eigenvector is the longitudinal direction $\vec u_k$ itself.

This gives a clean algebraic account of the two facts that distinguish the photon's spin from a generic spin-one.

First, **the two physical polarizations are the two nonzero-helicity states**, and they are exactly the states that survive the transverse projector of the previous section. The longitudinal state $\vec u_k$ has helicity zero and is the state the gauge structure removes.

Second, **there is no physical helicity-zero photon**. For a massless field the helicity is Lorentz invariant, and only the $\pm1$ states are physical; the helicity-zero state is the longitudinal mode removed by the gauge. The algebra exhibits the third eigenvector — it is the propagation direction — but the algebra does not, by itself, remove it. That removal is the gauge-fixing step that the canonical-quantization article identifies as unavailable from inside the algebra. The contrast is sharpened by the massive alternative: for a Proca field the gauge freedom is absent and the longitudinal, helicity-zero polarization becomes physical, with helicity no longer Lorentz invariant. The framework writes both cases equally well; masslessness, which selects the two-state spectrum, is an input.

A structural observation about *where* the objects sit. For spin-$\tfrac12$ the states are idempotents of $\mathbb{M}_+$ and the observables are Hermitian elements of $\mathbb{M}_+$; state and observable live in the same sector. For the photon the helicity observable has its representative in $\mathbb{M}_+$, but the polarization states $\varepsilon^{\mathrm{fop}}_\pm$ are not idempotents and are not in $\mathbb{M}_+$: the linear polarizations are in the vector part of $\mathbb{M}_-$ and the circular combinations in its complexification. The reason is that the spin-one representation appears in the biquaternion framework as the **adjoint action** on the imaginary quaternions, which is not a module over $\mathbb{B}$, whereas the spin-$\tfrac12$ representation is the fundamental module. The angular-momentum article states this distinction; here it has a concrete face: the photon's "state" space and its "observable" space are not the same subspace, and the familiar spin-$\tfrac12$ state/observable dictionary does not transfer. I record this as a structural finding, and I flag that it is not a defect of the polarization description but a property of the representation.

All of the helicity statements were checked exactly on the same three independent directions as the circular basis. On each, $\lambda\varepsilon^{\mathrm{fop}}_\pm=\pm\varepsilon^{\mathrm{fop}}_\pm$, $\lambda\vec u_k=0$, and the identity $\lambda=\tfrac{i}{2}\mathrm{ad}_{\vec u_k}$ hold as exact algebraic identities, not merely on the axis.

## Helicity and the Self-Dual Split of the Field Strength

The field-strength article establishes that the Riemann–Silberstein vector $\vec N=\vec E+ic\vec B$ is the self-dual half of the field: under the Hodge decomposition $\star(\vec E,\vec B)=(c\vec B,-\vec E/c)$ with $\star^2=-1$, the combination $F+i\star F$ corresponds to $\vec N$ and $F-i\star F$ to its complex conjugate $\vec N^*$; the two pieces are the two three-dimensional complex representations of the Lorentz group. The helicity of the plane wave is exactly the label of these two pieces.

For a plane wave, Faraday's law gives $\vec B=\vec u_k\times\vec E$ (in vacuum natural units, $c=1$). Decompose the complex transverse amplitude as $\vec E=E_+\varepsilon^{\mathrm{fop}}_+ + E_-\varepsilon^{\mathrm{fop}}_-$. Using $\vec u_k\times\varepsilon^{\mathrm{fop}}_\pm=\mp i\varepsilon^{\mathrm{fop}}_\pm$,

$$
\vec B = -iE_+\varepsilon^{\mathrm{fop}}_+ + iE_-\varepsilon^{\mathrm{fop}}_-, \qquad\text{so}\qquad
\vec E+i\vec B = 2E_+\varepsilon^{\mathrm{fop}}_+, \qquad \vec E-i\vec B = 2E_-\varepsilon^{\mathrm{fop}}_- .
$$

The two combinations $\vec E\pm i\vec B$ therefore separate the helicity $+1$ from the helicity $-1$ amplitude: the first contains only $E_+$, the second only $E_-$. Since $\tilde{F}=i\sqrt{\epsilon}\,\vec N=i\sqrt{\epsilon}\,(\vec E+ic\vec B)$, the field-strength biquaternion of a definite-helicity plane wave is supported on the corresponding self-dual or anti-self-dual component.

> **The two helicities are the two self-dual halves of the field strength.** A positive-frequency plane wave of helicity $+1$ has its amplitude in the self-dual piece $\vec E+ic\vec B$ and vanishing anti-self-dual piece $\vec E-ic\vec B$; helicity $-1$ reverses the roles.

This is the algebraic content of "the photon has two helicity states and no third": the third would be a self-dual/anti-self-dual-neutral component along $\vec u_k$, which is exactly the longitudinal mode, and it is absent for the massless field because transversality forces the amplitude into the two chiral halves. The statement was checked on two independent directions, $(3,4,0)/5$ and $(1,2,2)/3$, in the same exact arithmetic; on each, $\vec E\propto\varepsilon^{\mathrm{fop}}_+$ gives $\vec E+i\vec B=2\vec E$ and $\vec E-i\vec B=0$, and $\vec E\propto\varepsilon^{\mathrm{fop}}_-$ gives the reverse, never both.

## What the Framework Does Not Supply

Two things are conspicuously absent, and both were established by the parent articles rather than by this one.

**The ladder.** The photon creation and annihilation operators satisfy $[a^{\mathrm{fop}}_r,a^{\mathrm{fop}\dagger}_s]=\zeta_r\delta_{rs}(2\pi)^3\delta^{(3)}(\vec k-\vec k')$, a bosonic canonical relation. The Fock article proves that no pair $\tilde a,\tilde a^\dagger\in\mathbb{B}$ satisfies $[\tilde a,\tilde a^\dagger]=e_0$: a commutator has vanishing trace, while $\mathrm{Tr}(e_0)=2$, so the only relation of the form $[\tilde a,\tilde a^\dagger]=c\,e_0$ that can hold in $\mathbb{B}$ has $c=0$. The photon's ladder algebra is therefore not native. It is not even a finite-dimensional object: the physical photon number is the transverse sum $N_\gamma=\sum_{r=1}^{2}\int a^{\mathrm{fop}\dagger}_ra^{\mathrm{fop}}_r$, acting on the symmetric algebra of the transverse polarization module, which is infinite-dimensional. What the algebra supplies here is the module — the transverse polarization plane of the previous sections — and nothing algebraic on top of it. This is a sharper negative than the spin-$\tfrac12$ case, where the algebra carries the one-mode fermionic relation exactly.

**The gauge.** The canonical-quantization article proves that the algebra gives no reason to prefer the Lorenz gauge $S=\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{A})=0$ to any other. The reduction from the four polarization directions of $\mathbb{M}_-$ to the two transverse physical directions is performed by a subsidiary condition, and the subsidiary condition is imported. So the framework's role is asymmetric: it *owns* the space in which the reduction happens (the material sector and its indefinite norm), and it *does not own* the principle by which the reduction is made. I regard this as the central unclosed gap of the article, and it is not closed by the polarization results above.

A third imported ingredient is the operator-valued character of the field. The parent articles leave undecided whether the quantized field should be $\mathbb{B}$-valued or valued in a complex-vector module; the polarization results here are indifferent to that choice, because they concern the classical polarization vectors, which are the same either way.

## Derived, Represented, Outside: An Accounting

| Feature of the photon | Status in the framework | Where it comes from |
|---|---|---|
| The transverse polarization plane (the space of the two physical polarizations) | Derived | the $\vec u_k$-orthogonal plane in the vector part of $\mathbb{M}_-$ |
| Polarization space and its indefinite metric | Derived | $\mathbb{M}_-$ and its biquaternion norm; $\zeta=(-1,+1,+1,+1)$ |
| Circular polarizations as $\pm i$ eigenstates | Derived | left multiplication by $\vec u_k$; $e_je_k=\epsilon_{jkl}e_l$ |
| Helicity operator $\lambda=\tfrac{i}{2}\mathrm{ad}_{\vec u_k}$, spectral values $\{+1,0,-1\}$ | Derived | adjoint action on imaginary quaternions; representative $i\vec u_k\in\mathbb{M}_+$; $i$ as sector exchange |
| Two helicities = self-dual/anti-self-dual halves | Derived (from the field-strength article) | $\vec B=\vec u_k\times\vec E$; $\vec u_k\times\varepsilon^{\mathrm{fop}}_\pm=\mp i\varepsilon^{\mathrm{fop}}_\pm$ |
| Transverse polarization sum $\delta_{ij}-\vec u_k_i\vec u_k_j$ | Derived | orthogonality in the material sector |
| Mode expansion, commutators, Fock space | Transcribed | standard canonical quantization on a module |
| Indefinite metric sign $\zeta_0=-1$ | Derived | the signature of the biquaternion norm of $\mathbb{M}_-$ |
| Subsidiary condition, physical-subspace quotient | Imported | Gupta–Bleuler; no algebraic principle selects it |
| Photon ladder and number operator | Not available | no bosonic mode in $\mathbb{B}$ |
| Masslessness $m=0$ | Represented | an input; the Proca alternative is equally writable |
| Unit $\hbar$ | Represented | normalisation of the mode operators |
| Photon as the one-particle state | Represented | identification of the quantum, not derived |
| Photon is its own antiparticle | Represented | neutrality (reality of $\tilde{A}$); not derived |
| Helicity states related by parity, not by $C$ | Represented | standard discrete symmetries, transcribed |
| Interactions, radiative corrections | Outside | free-field treatment only |
| Any empirical discriminator | Outside | none is visible at this level |

Two rows of the table are short statements of one division, and the division is worth one sentence. The
algebra **owns** the transverse polarization plane, the two-dimensional space in the vector part of
$\mathbb{M}_-$ orthogonal to $\vec u_k$, together with its indefinite metric; the algebra does
**not own** the reduction that selects that plane out of the four polarization directions. The plane is
*Derived*, and the reduction is *Imported*, the subsidiary condition of the gauge row. The same division, an
object the algebra owns against a value it only represents, is the whole content of *The Null
Four-Momentum: What the Cone Derives and What It Does Not* for the massless shell and the rank, and it is
read across the twelve structures in *The Cone and the Massless Particles in the Biquaternioid Structures over $\mathbb{C}$*.

## The Gaps, Named

The gaps are of three kinds, and none is closed by better notation.

**Algebraic gaps.** There is no bosonic ladder in $\mathbb{B}$; the photon number operator is not an element of the algebra; and the gauge-fixing principle is absent. The first two are finite-dimensionality statements and are inherited from the Fock article. The third is the one the polarization results most nearly touch and do not reach: the algebra supplies the transverse plane and the longitudinal direction that must be removed, but not the rule for removing it.

**Represented quantities.** Masslessness is the sharpest. The photon is defined by $m=0$, and $m=0$ is what makes helicity Lorentz invariant and what removes the helicity-zero state; the framework represents $m=0$ and $m\neq0$ on the same footing and does not prefer either. The reason is structural rather than bookkeeping: the norm is homogeneous, so the cone is scale-invariant and the algebra carries no preferred scale with which to fix $m$. *The Null Four-Momentum: What the Cone Derives and What It Does Not* gives that argument, and gathers what the cone nevertheless derives — the massless shell as the zero-divisor cone, the frame-independence of $c$ from the multiplicativity of the norm, the absence of a rest frame for a null four-momentum, and the motion at $c$ for every momentum. The neutrality that makes the photon its own antiparticle is likewise an input. The unit $\hbar$ and the identification of the one-particle states as photons are inputs.

**Representation-theoretic caveats.** The spin-one representation appears as the adjoint action on the imaginary quaternions, not as a module over $\mathbb{B}$; the consequent separation of the photon's state space (material-sector vector part) from its observable space ($\mathbb{M}_+$) is a real structural feature, but whether the state/observable pairing of the adjoint representation can be given a probability interpretation analogous to $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H}) = 2\langle\tilde{P},\tilde{H}\rangle$ is not settled here. The transverse polarization states are not idempotents, so the Born rule of the informational sector does not apply to them directly.

**Empirical gap.** As with every article in this series, none of the framework's statements distinguishes it from standard electrodynamics. The photon is represented, not explained.

**A conflicting claim from the electro-gravimagnetic programme.** One external programme disputes precisely the step this section calls a gap. In the biquaternionic Maxwell thread of L. A. Alexeyeva — recorded in *The Electro-Gravimagnetic Field and the Magnetic-Charge–Mass Hypothesis* — the modified biquaternionic system is claimed to admit **longitudinal electromagnetic waves of different polarization**, with named solutions (a longitudinal magnetic wave, a longitudinal electric wave, Tesla's wave, and a torsion wave), and the paper states that such waves are *observed* but are not described by classical electrodynamics. This article's analysis is that the algebra supplies the longitudinal direction and *not* the rule that removes it: the longitudinal direction is the helicity-zero eigenvector, and its removal is an imported gauge condition. The two accounts therefore agree on the algebra and disagree on whether the physical solutions must be purely transverse. The physics that could decide between them is not in dispute and is not in the framework: free electromagnetic waves in vacuum are transverse, while longitudinal electromagnetic modes are established in **media** — plasma oscillations and modes in anisotropic or nonlinear media — which is where *Electromagnetism in Media — The Local Complex Structure at Work* and the plasma section of *Shock Electromagnetic Waves* operate. The open question the corpus records is therefore not which account is right but **whether the biquaternionic modification is doing the work a material medium does**: if the longitudinal solutions require an implicit medium, the modification is a material model in disguise, and the corpus's medium article is their test. The claim is recorded, not adopted.

## Boundaries

- **The subject is the photon as a quantum field.** This article owns the polarisation space and its indefinite metric, circular polarisation as the algebra's complex structure, the helicity operator, the self-dual split of the field strength, the absence of a bosonic ladder in $\mathbb{B}$, the gauge gap, and the accounting of the photon's derived, represented and outside features.
- **The null four-momentum is *The Null Four-Momentum: What the Cone Derives and What It Does Not*'s to define.** The mass shell as a norm condition, mass as the value of the invariant, the absence of a rest frame, the frame-independence of $c$, the scale-invariance argument and the verdict that the cone marks but does not choose masslessness are stated there, and this article states them as far as its masslessness row needs them; the owner is a pointer and not a prohibition on restating.
- **The cone across the products is *The Cone and the Massless Particles in the Biquaternioid Structures over $\mathbb{C}$*'s to define.** The cone's two jobs in the two bands, the rank of the left multiplication across the twelve rows, the nilpotent index and the roster of massless particles are stated there, and this article quotes them where it needs them.
- **The classical and mode-level objects are elsewhere.** The field-strength biquaternion and its invariants are *The Field-Strength Biquaternion and Its Invariants*; the Maxwell equation and the potential are *Maxwell's Equations in the Biquaternionic Formulation*; the mode expansion, the commutators and the Fock space are *Canonical Quantization of the Biquaternion Maxwell Field* and *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*.
- **Not claimed.** No dynamics, no interactions, no radiative corrections and no empirical discriminator. Masslessness and neutrality are represented, not derived; the identification of the one-particle states as photons is not derived here.

## Summary

The photon is the one-particle state of the biquaternion Maxwell field $\tilde{\nabla}\tilde{F}=0$, and its two transverse polarizations have a native meaning in the algebra. The four polarization vectors of the covariant quantization are the four directions of the material sector $\mathbb{M}_-$, and the indefinite metric $\zeta=(-1,+1,+1,+1)$ is the biquaternion norm $\langle\tilde{Q}\rangle_{\natural}=|\vec q|^2-q_0^2$ of that sector. The two physical polarizations are the plane in the vector part of $\mathbb{M}_-$ orthogonal to the propagation direction, with polarization sum $\sum_{r=1}^{2}\varepsilon^{\mathrm{fop}(r)}_i\varepsilon^{\mathrm{fop}(r)}_j=\delta_{ij}-\vec u_k_i\vec u_k_j$.

Circular polarization is the algebra's complex structure acting on the propagation direction: the circular vectors $\varepsilon^{\mathrm{fop}}_\pm=\tfrac{1}{\sqrt2}(\varepsilon^{\mathrm{fop}}_1\pm i\varepsilon^{\mathrm{fop}}_2)$ are the eigenvectors of left multiplication by $\vec u_k$, with $\vec u_k\varepsilon^{\mathrm{fop}}_\pm=\mp i\varepsilon^{\mathrm{fop}}_\pm$. The helicity operator is $\lambda=\vec u_k\cdot\vec S=\tfrac{i}{2}\mathrm{ad}_{\vec u_k}=i\,\mathrm{Vect}(\vec u_k\,\cdot\,)$, the vector part of left multiplication by the Hermitian element $i\vec u_k\in\mathbb{M}_+$, with spectral values $\{+1,0,-1\}$; its $\pm1$ eigenvectors are the two physical polarizations and its $0$ eigenvector is the longitudinal direction $\vec u_k$. The two helicities are the self-dual and anti-self-dual halves of the field strength: a definite-helicity plane wave is supported on $\vec E+ic\vec B$ or on $\vec E-ic\vec B$, never both.

What the framework does not supply is the ladder and the gauge. There is no bosonic creation or annihilation operator in $\mathbb{B}$, so the photon number operator is imported; and nothing in the algebra selects a gauge, so the reduction from four polarizations to two is imposed from outside even though the space in which it happens is native. Masslessness, the neutrality that makes the photon its own antiparticle, the unit $\hbar$, and the identification of the states as photons are all inputs. The photon is therefore represented in the biquaternion framework with a genuinely native polarization and helicity structure, but not derived, and the gauge-fixing gap remains open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_je_k=\epsilon_{jkl}e_l$ $(j\neq k)$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-$ | Anti-Hermitian (material) sector, $\mathrm{span}_\mathbb{R}\{ie_0,e_1,e_2,e_3\}$ |
| $\mathbb{M}_+$ | Hermitian (informational) sector, $\mathrm{span}_\mathbb{R}\{e_0,ie_1,ie_2,ie_3\}$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real quaternion subspace |
| $\mathsf{M}_2(e_k)=-i\sigma_k$, $\mathsf{M}_2(ie_k)=\sigma_k$ | Isomorphism with $M_2(\mathbb{C})$ |
| $\tilde{\nabla}=e_0\partial_{ict}+e_k\partial_k$ | Biquaternionic gradient |
| $\tilde{A}=i\phi/c\,e_0+\vec A$ | Potential biquaternion, in $\mathbb{M}_-$ |
| $\tilde{F}=i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H=i\sqrt{\epsilon}\,\vec N$ | Field-strength biquaternion (vanishing scalar part) |
| $\vec N=\vec E+ic\vec B$, $\vec B=\mu\vec H$ | Riemann–Silberstein vector; $\tilde{F}=i\sqrt{\epsilon}\,\vec N$ |
| $\vec u_k$ | Unit propagation direction (pure real quaternion) |
| $\varepsilon^{\mathrm{fop}}_1,\varepsilon^{\mathrm{fop}}_2$; $\varepsilon^{\mathrm{fop}}_\pm$ | Linear and circular polarization vectors |
| $\zeta=(-1,+1,+1,+1)$ | Indefinite metric of Gupta–Bleuler; biquaternion norm of $\mathbb{M}_-$ |
| $\lambda=\vec u_k\cdot\vec S=\tfrac{i}{2}\mathrm{ad}_{\vec u_k}$ | Helicity operator; representative $i\vec u_k\in\mathbb{M}_+$ |
| $\vec S$ (in $\tilde W=W+\tfrac{i}{c}\vec S$) | Poynting vector (Maxwell article) |
| $\vec S$ (in $\lambda=\vec u_k\cdot\vec S$) | Spin vector (angular-momentum article) |
| $g_k=-\tfrac12 e_k$ | Rotation generators in the angular-momentum article; this article writes the same generators as $e_k$ |
| $\epsilon^{(r)}_\mu$, $a^{\mathrm{fop}}_r,a^{\mathrm{fop}\dagger}_r$ | Polarization vectors and mode operators (imported) |
| $N_\gamma=\sum_{r=1}^{2}\int a^{\mathrm{fop}\dagger}_ra^{\mathrm{fop}}_r$ | Photon number (transverse sum), not in $\mathbb{B}$ |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H}) = 2\langle\tilde{P},\tilde{H}\rangle$ | Trace formula |
| $c=1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $\langle\tilde{P},\tilde{Q}\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\langle\tilde{Q}\rangle_{\natural}$ |
| $\langle\tilde{P},\tilde{Q}\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{P}\tilde{Q})$ |
| $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ |

## Further Reading

- S. N. Gupta, "Theory of longitudinal photons in quantum electrodynamics," *Proceedings of the Physical Society A* **63** (1950) 681–691, and K. Bleuler, "Eine neue Methode zur Behandlung der longitudinalen und skalaren Photonen," *Helvetica Physica Acta* **23** (1950) 567–586, for the indefinite-metric quantization and the subsidiary condition.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), and C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the canonical quantization of the electromagnetic field and the polarization vectors.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), and S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the Gupta–Bleuler construction, the physical-state condition, and the helicity of the massless vector field.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1998), for the polarization of plane waves, the Riemann–Silberstein construction, and the Stokes parameters.
- V. B. Berestetskii, E. M. Lifshitz, and L. P. Pitaevskii, *Quantum Electrodynamics* (Pergamon, 1982), and L. H. Ryder, *Quantum Field Theory* (Cambridge, 1996), for the photon, its helicity, and the spin-one representations of the Lorentz group.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the realization of $SU(2)$ and the vector representation in quaternion and Clifford algebras.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of circular polarization and self-duality.
- L. A. Alexeyeva, "Maxwell Equations, Their Hamiltonian and Biquaternionic Forms and Properties of Their Solutions", *Mathematical Journal* **16**(2) (2016) 90–103, for the claim that the modified biquaternionic system admits longitudinal electromagnetic waves and for the named Tesla and torsion waves; recorded as a conflicting claim in *The Gaps, Named* above.
- The companion articles of this series: *Maxwell's Equations in the Biquaternionic Formulation*; *The Field-Strength Biquaternion and Its Invariants*; *Canonical Quantization of the Biquaternion Maxwell Field*; *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*; *The Electron in Biquaternionic Form*; *Angular Momentum and Spin in Biquaternionic Form*; *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*; *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*; *The Null Four-Momentum: What the Cone Derives and What It Does Not*; *The Cone and the Massless Particles in the Biquaternioid Structures over $\mathbb{C}$*; *Introduction to the Biquaternion Universe*.
