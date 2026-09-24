# __The Hydrogen Atom in Biquaternionic Form — The Relativistic Case__

## Introduction

The relativistic hydrogen atom is the **Dirac–Coulomb problem**: a spin-$\tfrac12$ particle of mass $m$ bound by the central potential

$$
V(r) = -\frac{\kappa}{r}, \qquad \kappa = \frac{Ze^2}{4\pi\epsilon_0},
$$

with $Z$ the nuclear charge. It is the relativistic completion of the problem treated in the companion article *The Hydrogen Atom in Biquaternionic Form — The Non-Relativistic Case*, and the differences are structural rather than quantitative. There the Coulomb Hamiltonian was the central scalar $\tilde H = h_0e_0$; the spin was a spectator, the orbital and spin operators occupied complementary slots that commuted, and the level depended on $n$ alone. Here the Hamiltonian is no longer central, the spin is dynamical, and the level depends on $n$ and $j$.

The article asks what the biquaternion framework contributes to this problem, and the honest answer is stated before the derivation.

- **Algebraic, and recomputed here.** The total angular momentum $\tilde J_k = \tilde L_k + \tilde S_k$, with the orbital part in the scalar slot and the spin part in the vector slots, closes on the angular-momentum algebra. The spin–orbit operator $\tilde L_k\tilde S_k$ is a Hermitian element of the informational sector $\mathbb{M}_+$; it commutes with $\tilde J_k$, but not with $\tilde L_k$ or $\tilde S_k$ separately, which is the algebraic statement that the spin is no longer a spectator. The relativistic level is labelled by $(n,j)$ and not by $(n,l)$: the $l$-degeneracy is lifted, and at fixed $n$ and $j$ the two states $l = j\pm\tfrac12$ are degenerate. All of this is checked below.
- **Transcribed, not derived.** The exact bound-state energies are the standard Sommerfeld–Dirac spectrum, quoted in full in its place. The transcription reproduces them and predicts no deviation. Its non-relativistic limit and fine structure are worked through in the companion article *The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit* and its exercise, which is where the elimination of the small component lives; the exact bound-state solution itself is the standard radial Dirac–Coulomb one, and it is not reproduced anywhere in the corpus. No independent biquaternionic derivation is claimed.
- **Gap, left visible.** The corpus's biquaternion Dirac equation carries the **linear**, chirality-off-diagonal mass pair $\tilde\nabla\tilde\Psi_R = m\tilde\Psi_L$, $\bar{\tilde\nabla}\tilde\Psi_L = m\tilde\Psi_R$, and this mass term passes through a local central phase: the central $U(1)$ (fermion number) is exact for the massive field, and the symmetry the mass breaks is the axial one. The algebra-level electromagnetic coupling is therefore available in the massive case, and its precise form is set out in the companion article *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*, which derives the coupled equation and proves it gauge covariant. What the corpus does not supply is the radial Dirac–Coulomb solution inside the algebra; the Coulomb field is introduced here in the **spinor-module transcription**, where the algebra and the module agree, and the spectrum is transcribed. This is the gap that remains, and it is not closed by notation.

The title covers the relativistic case as the framework's algebraic structures reach it; it is not a claim that the framework derives the Sommerfeld spectrum from its own algebra-level equation. That derivation is not carried out in the corpus, so the claim is not made.

**Conventions.** The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_je_k = \epsilon_{jkl}e_l$ for $j \neq k$; the scalar imaginary $i$ is central with $i^2 = -e_0$. The anti-Hermitian subspace $\mathbb{M}_-$ is the material sector (imaginary scalar, real vector) and the Hermitian subspace $\mathbb{M}_+$ is the informational sector (real scalar, imaginary vector), with $\mathbb{B} = \mathbb{M}_+\oplus\mathbb{M}_-$ and $i\mathbb{M}_\pm = \mathbb{M}_\mp$. The real quaternion subspace is $\mathbb{H}_{\mathbb{B}}$, the centre is $\mathbb{C}_{\mathbb{B}} = \operatorname{span}_\mathbb{R}\{e_0, ie_0\}$, and the trace is normalised so that $\mathrm{Tr}(\tilde P\tilde H) = 2\,\mathrm{Sc}(\tilde P\tilde H)$. The gradient is $\tilde\nabla = e_0\partial_{ict} + e_k\partial_k$, its quaternion conjugate is $\bar{\tilde\nabla} = e_0\partial_{ict} - e_k\partial_k$, and $\Box = \tilde\nabla\bar{\tilde\nabla} = \bar{\tilde\nabla}\tilde\nabla$. The isomorphism is $\Phi(e_0) = I_2$, $\Phi(e_k) = -i\sigma_k$, $\Phi(i) = iI_2$, so that $\Phi(ie_k) = \sigma_k$. The idempotents are $\tilde P_\pm(\hat\mu) = \tfrac12(e_0 \pm i\hat\mu)$. The orbital operators are $\tilde L_k = \hat L_k e_0$ with $\hat L_k = -i\hbar\epsilon_{klm}x_l\partial_m$, the spin operators are $\tilde S_k = \tfrac{\hbar}{2}ie_k$, and $\tilde J_k = \tilde L_k + \tilde S_k$. The rest of the notation is inherited from the read-list articles unchanged.

## The Dirac–Coulomb Problem

### The potential in the framework's notation

The framework's four-potential is the material-sector object

$$
\tilde A = \frac{i\phi}{c}\,e_0 + \mathbf{A} \in \mathbb{M}_-,
$$

and a static point nucleus is the special case $\mathbf{A} = 0$ with $\phi = Ze/(4\pi\epsilon_0 r)$, so that the potential energy of a charge $q$ in it is $q\phi = -\kappa/r$ for the electron. Two honest remarks, both inherited from the non-relativistic article, belong here. First, the $1/r$ form is **input**: the companion Maxwell article produces the field of a point charge as an imaginary vector in $\mathbb{M}_+$, but the point-charge source is supplied, not derived. Second, the framework does not supply the value of $\kappa$ or of the dimensionless coupling

$$
\alpha = \frac{e^2}{4\pi\epsilon_0\hbar c}, \qquad \kappa = Z\alpha\,\hbar c,
$$

which enters the spectrum as a parameter.

### The module transcription

The framework's states are spinors in the minimal left ideal $\mathbb{B}\tilde P \cong \mathbb{C}^2$, and a position-space treatment extends this to a spinor field $\psi(t,\mathbf{x}) \in \mathbb{B}\tilde P \cong \mathbb{C}^2$ whose argument carries the position dependence. In this transcription the Dirac–Coulomb problem is the standard one,

$$
i\hbar\,\partial_t\psi = \Bigl[\,c\,\boldsymbol\alpha\cdot\hat{\mathbf p} + \beta mc^2 + V(r)\,\Bigr]\psi,
\qquad \boldsymbol\alpha^k = \gamma^0\gamma^k, \quad \beta = \gamma^0,
$$

with $V(r) = q\phi = -\kappa/r$. The biquaternion field $\tilde\Psi \in \mathbb{B}$ is the algebra-level representative of this spinor, and the free part is the corpus's biquaternion Dirac equation

$$
\tilde\nabla\tilde\Psi_R = m\tilde\Psi_L, \qquad \bar{\tilde\nabla}\tilde\Psi_L = m\tilde\Psi_R, \qquad \tilde\Psi^\flat = -\tilde\Psi^\dagger .
$$

The Coulomb term is a **central scalar**, $V(r)e_0 \in \mathbb{C}_{\mathbb{B}}$, so it multiplies the field without ambiguity of order, and in this respect its placement is the same as the non-relativistic potential's.

A structural caveat must accompany this transcription. The matrix $\beta$ is an **odd** element of the Clifford algebra $\mathrm{Cl}_{1,3}$, while $\mathbb{B}$ is isomorphic to the **even** subalgebra $\mathrm{Cl}^+_{1,3}$. The module transcription therefore uses structure that the algebra-level field $\tilde\Psi$ does not contain: $\beta$ has no representative in the even subalgebra. The algebra-level equation carries the same linear mass as the spinor module, so the transcription is not forced by an obstruction at the mass term; the two descriptions agree on the mass, and the module supplies the Clifford-odd structure that the Hamiltonian's Foldy–Wouthuysen reduction needs. The transcription is the one the corpus's electron and solutions articles use, and it is adopted here on that basis, with the caveat recorded rather than hidden.

## The Hamiltonian Leaves the Scalar Slot

In the non-relativistic problem the Hamiltonian is a scalar multiple of the identity, $\tilde H = h_0e_0$, and its vanishing vector part is what makes the spin a spectator. The relativistic corrections change this, and the change is algebraic: they occupy the vector slots of $\mathbb{M}_+$.

At relative order $c^{-2}$ the elimination of the small component produces the effective large-component Hamiltonian

$$
\hat H = \frac{\boldsymbol\pi^2}{2m} + q\Phi - \frac{q\hbar}{2m}\,\boldsymbol\sigma\cdot\mathbf B
- \frac{\boldsymbol\pi^4}{8m^3c^2}
+ \frac{\hbar^2}{8m^2c^2}\nabla^2V
- \frac{q\hbar}{4m^2c^2}\,\boldsymbol\sigma\cdot(\mathbf E\times\boldsymbol\pi),
$$

whose last three terms are the relativistic kinetic correction, the Darwin term, and the spin–orbit coupling. It is derived in the companion exercise on the Pauli equation, which checks the coefficients against the exact spectrum; it is quoted here only for its structure. The **spin–orbit** term is the one that changes the character of the Hamiltonian. For a central potential it reads

$$
-\frac{q\hbar}{4m^2c^2}\,\boldsymbol\sigma\cdot(\mathbf E\times\boldsymbol\pi)
= \frac{1}{2m^2c^2}\frac{1}{r}\frac{dV}{dr}\,\mathbf L\cdot\mathbf S ,
$$

and in the framework's operators the scalar coupling is

$$
\tilde L_k\tilde S_k = \frac{\hbar}{2}\,i\,\hat L_k e_k \in \mathbb{M}_+ .
$$

This is a Hermitian element of the informational sector: its scalar part vanishes and its vector part is purely imaginary. It is therefore **not central** — a central element lies in the complex line $\mathbb{C}_{\mathbb{B}}$, and $\tilde L_k\tilde S_k$ has a nonzero imaginary vector part whenever the orbital motion is non-trivial. The relativistic Coulomb Hamiltonian is not a scalar multiple of $e_0$.

**The spin is no longer a spectator.** The algebraic statement of this is the commutator structure of the spin–orbit operator. It is rotationally invariant,

$$
\bigl[\tilde L_k\tilde S_k,\ \tilde J_j\bigr] = 0,
$$

so that the total angular momentum remains conserved, but it does not commute with the orbital or the spin operators separately,

$$
\bigl[\tilde L_k\tilde S_k,\ \tilde L_j\bigr] \neq 0, \qquad
\bigl[\tilde L_k\tilde S_k,\ \tilde S_j\bigr] \neq 0 .
$$

The first of these is the statement that $l$ is no longer a good quantum number; the second is the statement that the spin has become dynamical. Both were recomputed in an explicit $\tfrac12 \otimes 1$ representation, where the $6\times6$ operators satisfy $[\tilde J_i,\tilde J_j] = i\hbar\epsilon_{ijk}\tilde J_k$, the operator $\tilde L_k\tilde S_k$ commutes with every $\tilde J_j$, and its commutators with $\tilde L_j$ and $\tilde S_j$ are nonzero; the eigenvalues of $\tilde L_k\tilde S_k$ are the two values $+\tfrac{\hbar^2}{2}$ and $-\hbar^2$ for $j = \tfrac32$ and $j = \tfrac12$ respectively, in agreement with the general formula below.

## Total Angular Momentum and the Good Quantum Numbers

The **total angular-momentum operator** is the sum of the orbital and spin parts,

$$
\tilde J_k = \tilde L_k + \tilde S_k = \hat L_k\,e_0 + \frac{\hbar}{2}\,i e_k ,
\qquad
\Phi(\tilde J_k) = \hat L_k I_2 + \frac{\hbar}{2}\sigma_k .
$$

Because the two parts commute and each satisfies the angular-momentum algebra, so does the sum:

$$
[\tilde J_i,\tilde J_j] = i\hbar\,\epsilon_{ijk}\tilde J_k .
$$

The Casimir takes the value

$$
\tilde J^{\,2} \;\longrightarrow\; \hbar^2 j(j+1), \qquad j = l \pm \tfrac12 \ \ (l \ge 1), \qquad j = \tfrac12 \ \ (l = 0),
$$

on the coupled states. These are the framework's own statements, established in the companion article on angular momentum and spin; they are used here, not rederived.

The relativistic Coulomb eigenstates are the coupled states $|n,l,j,m_j\rangle$ built with the Clebsch–Gordan coefficients of $\tfrac12\otimes l$. The good quantum numbers are

$$
n, \quad j, \quad m_j, \qquad j = \tfrac12, \tfrac32, \dots, n-\tfrac12, \qquad m_j = -j,\dots,+j ,
$$

together with the parity. The orbital quantum number $l$ is not among them: at fixed $n$ and $j$ the states $l = j-\tfrac12$ and $l = j+\tfrac12$ are degenerate, and they are the two members of a single relativistic level. This is the precise form of the statement that the $l$-degeneracy is lifted relativistically.

**What is algebraic and what is not.** The framework's contribution to this section is the spin factor: the $\tilde S_k = \tfrac{\hbar}{2}ie_k$ in the vector slots, the commutator $[\tilde S_i,\tilde S_j] = i\hbar\epsilon_{ijk}\tilde S_k$, and the Hermitian placement of $\tilde J_k$ in $\mathbb{M}_+$. The orbital factor is carried by the position dependence of the field, not by the finite-dimensional algebra, and the Clebsch–Gordan coefficients are the standard ones. As the companion article records, the algebra $\mathbb{B} \cong M_2(\mathbb{C})$ realises as modules only $j = 0$ and $j = \tfrac12$; the orbital representation is external structure on which the algebra's spin acts. The coupling of the two, which is what makes this problem relativistic, is therefore only partly algebraic.

## The Exact Spectrum

### The Sommerfeld–Dirac formula

The companion non-relativistic article already quotes the following formula in its closing bridge to this case. It is restated here because the present article is where its labels, its domain, its degeneracy bookkeeping, and its derivation status are developed; the formula itself is inherited from that article and from the standard solution, not rederived.

The exact bound-state energies of the Dirac–Coulomb problem are

$$
E_{nj} = mc^2\left[1 + \frac{(Z\alpha)^2}{\bigl(n - \delta_j\bigr)^2}\right]^{-1/2},
\qquad
\delta_j = j + \tfrac12 - \sqrt{\bigl(j + \tfrac12\bigr)^2 - (Z\alpha)^2},
$$

with the labels of the previous section. The spectrum depends on $n$ and $j$ only, which is the analytic statement of the degeneracy pattern: the two $l$ values at fixed $j$ share an energy, and the $2j+1$ values of $m_j$ do as well.

The formula is the standard exact Dirac–Coulomb result. It is quoted, not derived here, and it is not derived anywhere in the corpus: the companion solutions article and its exercise carry out the non-relativistic limit and the $c^{-2}$ corrections, and check those corrections against this formula, but the exact bound-state solution — the radial Dirac–Coulomb equations and their confluent-hypergeometric solution — is standard material that is not reproduced. The domain of the formula is

$$
Z\alpha < j + \tfrac12 ,
$$

since otherwise the square root is imaginary. For the lowest value $j = \tfrac12$ this is $Z < 137$; a point-Coulomb Dirac problem beyond that coupling has no bound states in this formula, and the description of the supercritical regime is outside the article.

### The non-relativistic limit and the fine structure

Expanding in powers of $(Z\alpha)^2$ reproduces the non-relativistic spectrum at leading order and the fine structure at the next. In units of $mc^2$,

$$
E_{nj} = mc^2 - \frac{mc^2(Z\alpha)^2}{2n^2}
- \frac{mc^2(Z\alpha)^4}{2n^3}\left(\frac{1}{j+\tfrac12} - \frac{3}{4n}\right)
+ O\bigl((Z\alpha)^6\bigr).
$$

The leading term is the non-relativistic $E_n$ of the companion article,

$$
E_n = -\frac{m\kappa^2}{2\hbar^2 n^2} = -\frac{mc^2(Z\alpha)^2}{2n^2},
$$

and the next is the **fine structure**

$$
\Delta E_{\text{fs}} = -\frac{mc^2(Z\alpha)^4}{2n^3}\left(\frac{1}{j+\tfrac12} - \frac{3}{4n}\right),
$$

whose $j$-dependence is the $l$-splitting read off the exact formula. The expansion was recomputed exactly, in rational arithmetic, for every $n \le 4$ and every $j$ allowed at that $n$: the coefficient of $(Z\alpha)^2$ is $-1/(2n^2)$ and the coefficient of $(Z\alpha)^4$ is $-\tfrac{1}{2n^3}(\tfrac{1}{j+1/2}-\tfrac{3}{4n})$ in every case, with no discrepancy.

The fine-structure shift decomposes into three physical contributions — the relativistic kinetic correction, the spin–orbit term, and the Darwin term — which the companion exercise obtains from the Foldy–Wouthuysen expansion. Their sum equals the exact $(Z\alpha)^4$ coefficient for every level with $n \le 6$, which was rechecked here in exact rational arithmetic; that agreement is the quantitative sense in which the framework's spin–orbit operator $\tilde L_k\tilde S_k$ carries the right coupling. The Darwin term is a pure scalar (its origin is the $l = 0$ value of the same elimination) and the kinetic term is scalar; only the spin–orbit term is a non-central $\mathbb{M}_+$ observable, which is why the spin anomaly of the spectrum is the one the sector structure makes visible.

### Degeneracy and its redistribution

The relativistic spectrum has the same **total** state count at each $n$ as the non-relativistic one, redistributed across the new labels. At fixed $n$ the values of $j$ are $\tfrac12, \tfrac32, \dots, n-\tfrac12$. For each $j < n - \tfrac12$ there are two orbital values $l = j \mp \tfrac12$ and $2j+1$ magnetic values; for $j = n-\tfrac12$ only $l = n-1$ is available. Counting,

$$
2\sum_{j=1/2}^{n-3/2}(2j+1) \;+\; \bigl(2(n-\tfrac12)+1\bigr) = 2n^2 ,
$$

which was verified for $n \le 6$. So the framework's state space is not enlarged or reduced by the relativistic treatment; what changes is the **splitting** of the $2n^2$ states into levels $E_{nj}$ that depend on $j$ as well as $n$. The non-relativistic $l$-degeneracy among states of the same $n$ is gone, replaced by the $l = j \mp \tfrac12$ degeneracy at fixed $j$; in the limit $Z\alpha \to 0$ the $\delta_j$ corrections collapse and the full non-relativistic degeneracy is restored.

## Minimal Coupling and the Massive Sector

The Coulomb field is an electromagnetic field, and in a gauge theory it is introduced by minimal coupling. The framework's biquaternion Dirac equation carries a linear, chirality-off-diagonal mass pair, and the coupling is available at the algebra level: the central phase passes through the mass term.

Let $\lambda = e^{iq\Gamma/\hbar}$ be a central phase. The covariant derivative

$$
D = \tilde\nabla + \frac{iq}{\hbar}\tilde A, \qquad D\tilde\Psi \longmapsto \lambda\, D\tilde\Psi ,
$$

transforms homogeneously, with the consistent connection transformation $\tilde A' = \tilde A - \tilde\nabla\Gamma$ that the abelian gauge structure of the framework provides. This covariance, together with the Leibniz rule it needs, was machine-checked by finite differences at a point not used to fix the conventions. The mass term of the parent's equation is linear, so it carries the same factor: for the pair

$$
D\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \bar{D}\tilde{\Psi}_L = m\tilde{\Psi}_R ,
$$

the transformed left-hand side is $\lambda\,D\tilde\Psi_R$ and the transformed right-hand side is $m\lambda\tilde\Psi_L$, because the central phase commutes with the mass. The two sides transform identically, so the massive coupled equation is **form-invariant** under the local phase and holds in every gauge when it holds in one. **Every local central phase is allowed, and the central $U(1)$ (fermion number) is exact for the massive field.**

The object the phase cannot pass through is not the mass but the algebra's real structure: a coupling built on $\flat = -\dagger$, which is antilinear, transforms as $(\lambda\tilde\Psi)^\flat = \lambda^{*}\tilde\Psi^\flat$, so a Majorana-type mass $m\tilde\Psi^\flat$ would acquire the factor $e^{2iq\Gamma/\hbar}$ and be form-invariant only for $\lambda = \pm1$. That is a statement about the real structure, not about the parent's mass term, and it belongs to the companion articles on the neutrino and on chirality. What the mass breaks is the **axial** symmetry,

$$
\partial_\mu j_5^\mu = 2im\,\bar\psi\gamma_5\psi ,
$$

which vanishes only at $m = 0$, while the vector current is conserved for the massive field; this was verified numerically in the Noether article on a superposition of two on-shell plane waves (axial ratio $1.000000$, vector divergence $5.3\times10^{-10}$, both currents conserved at $m = 0$).

The consequences should be stated plainly. The Coulomb potential can be inserted into the algebra-level equation $D\tilde\Psi_R = m\tilde\Psi_L$, $\bar{D}\tilde\Psi_L = m\tilde\Psi_R$ by the standard minimal coupling, and the central phase passes through the mass term; the charge is carried by the massive sector. The precise algebra-level transcription of the electromagnetic coupling — the biquaternion form of $\hat{\mathbf p} \to \hat{\mathbf p} - q\mathbf A$ and $i\hbar\partial_t \to i\hbar\partial_t - q\Phi$ — is set out in the companion article *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*, which derives the coupled equation and proves it gauge covariant. What the corpus does not supply is the radial Dirac–Coulomb solution inside the algebra. Until it is supplied, the relativistic hydrogen atom in biquaternionic form is a transcription of the standard solution into the framework's algebra, not a derivation from the framework's own field equation.

## What the Framework Supplies and What It Does Not

The accounting can be put in one table, in the form used by the companion electron article.

| Feature of the relativistic Coulomb problem | Status | Where it comes from |
|---|---|---|
| Total angular momentum $\tilde J_k$, its algebra, $\tilde J^{\,2} \to \hbar^2 j(j+1)$ | Algebraic (inherited, rechecked) | $\tilde S_k = \tfrac{\hbar}{2}ie_k$ in the vector slots; quaternion product |
| Spin–orbit operator $\tilde L_k\tilde S_k$ and its eigenvalues | Algebraic (inherited, rechecked) | $[\tilde J_i,\tilde J_j] = i\hbar\epsilon_{ijk}\tilde J_k$; Casimir identity |
| $l$-degeneracy lifted; $j$ good, $l$ not; $(n,j)$ label | Derived from the spectrum and the algebra | exact $E_{nj}$; $[\tilde L_k\tilde S_k,\tilde S_j] \neq 0$ |
| Total state count $2n^2$ preserved, redistributed | Recomputed | sum over $j$ of $(2j+1)\times(\text{number of } l)$ |
| Exact spectrum $E_{nj}$ (Sommerfeld–Dirac) | Transcribed | standard Dirac–Coulomb solution; companion solutions article |
| Fine-structure shift and its decomposition | Verified (transcribed) | companion Pauli exercise; exact rational check |
| Coulomb potential $V = -\kappa/r$, coupling $\kappa$, $\alpha$, $Z$ | Input | point-charge source; values inserted |
| Algebra-level minimal coupling of the massive field | Worked out; massive case covariant | linear chiral pair; central phase passes through the mass; minimal-coupling article |
| Deviation from standard physics | None found | the spectrum is the standard one |

Two entries deserve a sentence. The first is that the algebraic content is real but narrow: the framework supplies the spin algebra, the sector placement of the spin–orbit coupling, and the bookkeeping of the levels; it does not supply the orbital dynamics, the radial equation, or the coupling constant. The second is the step that remains: the algebra-level coupling is consistent and covariant, so the obstacle is no longer the mass term; what the corpus does not supply is the radial Dirac–Coulomb solution inside the algebra, and that is the step that would turn the transcription into a derivation. That is the sense in which the title overpromises if read as "derived", and the article does not sign for it.

## Open Questions

1. **The algebra-level minimal coupling.** The coupled massive equation $D\tilde\Psi_R = m\tilde\Psi_L$, $\bar{D}\tilde\Psi_L = m\tilde\Psi_R$ is set out in *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*, and is proved there to be gauge covariant. The choice of matter representation — left versus right action — remains open in that article and in the parent's open question 7.
2. **The nature of the mass term.** The parent's mass term is the linear, chirality-off-diagonal pair; the algebra's real structure $\flat$ is retained separately, and a coupling built on it — a Majorana-type mass — is a neutral-field pairing. Whether the real form of $\mathbb{B}$ forces a second, neutral massive sector alongside the charged one is open, and the two readings have different consequences for the charge sectors.

3. **A framework derivation of the spectrum.** Can the radial Dirac–Coulomb equation be written and solved within the biquaternion algebra without passing to the spinor module, and does the Sommerfeld formula follow from the algebra's own operators?
4. **The supercritical regime.** For $Z\alpha$ beyond $j+\tfrac12$ the exact formula loses its bound states; how does the framework describe the diving of the level into the negative continuum?
5. **Radiative corrections.** The Lamb shift and the anomalous moment are loop effects; the framework's classical equation does not contain them (as the electron article records for $g-2$), and a framework account would require the quantized theory.
6. **Many-electron and finite-nuclear-size effects.** The article is for one electron in a fixed point-Coulomb field; the framework's account of the electron–electron interaction and of nuclear structure is not developed here.
7. **Empirical content.** The spectrum predicts nothing beyond standard relativistic quantum mechanics for hydrogen. Whether any framework-level effect distinguishes the two remains the standing open question.

## Summary

The relativistic hydrogen atom in biquaternionic form is the Dirac–Coulomb problem, and what the framework contributes to it is algebraic. The total angular momentum $\tilde J_k = \tilde L_k + \tilde S_k$ has its orbital part in the scalar slot and its spin part in the vector slots, and it closes on $[\tilde J_i,\tilde J_j] = i\hbar\epsilon_{ijk}\tilde J_k$ with $\tilde J^{\,2} \to \hbar^2 j(j+1)$. The spin–orbit operator $\tilde L_k\tilde S_k = \tfrac{\hbar}{2}i\hat L_ke_k$ is a Hermitian element of $\mathbb{M}_+$; it commutes with $\tilde J_j$ but not with $\tilde L_j$ or $\tilde S_j$, which is the algebraic content of "the spin is no longer a spectator". The relativistic level is labelled by $(n,j,m_j)$, the $l$-degeneracy is lifted, and the residual degeneracy joins $l = j\mp\tfrac12$ at fixed $j$, with the total count $2n^2$ unchanged.

The exact bound-state energies are the Sommerfeld–Dirac formula

$$
E_{nj} = mc^2\left[1 + \frac{(Z\alpha)^2}{\bigl(n-\delta_j\bigr)^2}\right]^{-1/2},
\qquad
\delta_j = j+\tfrac12 - \sqrt{\bigl(j+\tfrac12\bigr)^2 - (Z\alpha)^2},
$$

whose expansion

$$
E_{nj} = mc^2 - \frac{mc^2(Z\alpha)^2}{2n^2}
- \frac{mc^2(Z\alpha)^4}{2n^3}\left(\frac{1}{j+\tfrac12}-\frac{3}{4n}\right) + O\bigl((Z\alpha)^6\bigr)
$$

returns the non-relativistic $E_n$ at leading order and the fine structure at the next, the latter verified by exact rational arithmetic against the kinetic, spin–orbit, and Darwin terms of the companion exercise. The spectrum is the standard one and no deviation is predicted.

One gap is load-bearing and is left visible. The corpus's biquaternion Dirac equation carries the linear, chirality-off-diagonal mass pair $\tilde\nabla\tilde\Psi_R = m\tilde\Psi_L$, $\bar{\tilde\nabla}\tilde\Psi_L = m\tilde\Psi_R$, through which a local central phase passes; the massive equation therefore admits the algebra-level minimal coupling, and the central $U(1)$ (fermion number) is exact for the massive field, with the axial symmetry broken instead. What the corpus does not supply is the radial Dirac–Coulomb solution inside the algebra: the algebra-level form of the coupling is set out in *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*, and the spectrum above is obtained in the spinor-module transcription, where the algebra and the module agree. The relativistic hydrogen atom is therefore, in this framework, an algebraically structured **transcription** of the standard solution — with the spin algebra, the sector placement, the good quantum numbers, and the level bookkeeping genuinely algebraic, and the derivation from the framework's own field equation an open problem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_je_k = \epsilon_{jkl}e_l$ $(j\neq k)$ |
| $i$ | Central scalar imaginary, $i^2 = -e_0$ |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material): imaginary scalar, real vector; $i\mathbb{M}_+ = \mathbb{M}_-$ |
| $\mathbb{M}_+$ | Hermitian subspace (informational): real scalar, imaginary vector |
| $\mathbb{H}_{\mathbb{B}}$ | Real quaternion subspace |
| $\mathbb{C}_{\mathbb{B}} = \operatorname{span}_\mathbb{R}\{e_0, ie_0\}$ | Centre of the algebra |
| $\Phi(e_k) = -i\sigma_k$, $\Phi(ie_k) = \sigma_k$ | Isomorphism with $M_2(\mathbb{C})$ |
| $\tilde\nabla = e_0\partial_{ict} + e_k\partial_k$ | Biquaternionic gradient (Dirac operator) |
| $\Box = \tilde\nabla\bar{\tilde\nabla} = \bar{\tilde\nabla}\tilde\nabla$ | d'Alembertian |
| $\tilde\Psi$, $\tilde\Psi^\flat = -\tilde\Psi^\dagger$ | Biquaternion Dirac field and anti-Hermitian conjugate (the algebra's real structure; not the mass term) |
| $\tilde A = i\phi/c\,e_0 + \mathbf{A} \in \mathbb{M}_-$ | Electromagnetic four-potential |
| $V(r) = q\phi = -\kappa/r$ | Coulomb potential energy |
| $\kappa = Ze^2/(4\pi\epsilon_0) = Z\alpha\,\hbar c$ | Coulomb coupling |
| $\alpha = e^2/(4\pi\epsilon_0\hbar c)$ | Fine-structure constant |
| $\hat L_k = -i\hbar\epsilon_{klm}x_l\partial_m$ | Orbital angular momentum |
| $\tilde L_k = \hat L_k e_0$ | Orbital operators, scalar slot, in $\mathbb{M}_+$ |
| $\tilde S_k = \tfrac{\hbar}{2}ie_k$ | Spin operators, vector slots, in $\mathbb{M}_+$ |
| $\tilde J_k = \tilde L_k + \tilde S_k$ | Total angular momentum; $[\tilde J_i,\tilde J_j] = i\hbar\epsilon_{ijk}\tilde J_k$ |
| $\tilde L_k\tilde S_k$ | Spin–orbit operator, in $\mathbb{M}_+$; eigenvalues $\tfrac{\hbar^2}{2}[j(j+1)-l(l+1)-\tfrac34]$ |
| $|n,l,j,m_j\rangle$ | Coupled relativistic basis |
| $E_{nj}$, $\delta_j$ | Exact Sommerfeld–Dirac energy and its $j$-dependent shift |
| $\Delta E_{\text{fs}} = -\frac{mc^2(Z\alpha)^4}{2n^3}\bigl(\frac{1}{j+1/2}-\frac{3}{4n}\bigr)$ | Fine-structure shift |
| $\mathbb{B}\tilde P \cong \mathbb{C}^2$ | Spinor module carrying the field $\psi$ |
| $\mathrm{Tr}(\tilde P\tilde H) = 2\,\mathrm{Sc}(\tilde P\tilde H)$ | Trace formula (Born rule) |

## Further Reading

- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original Dirac equation and its hydrogen solution.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the operator treatment of angular momentum and the relativistic hydrogen spectrum.
- H. A. Bethe and E. E. Salpeter, *Quantum Mechanics of One- and Two-Electron Atoms* (Springer, 1957), for the exact Dirac–Coulomb spectrum and its corrections.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the standard derivation of the Sommerfeld–Dirac formula.
- V. B. Berestetskii, E. M. Lifshitz, and L. P. Pitaevskii, *Relativistic Quantum Theory* (Pergamon, 1971), for the relativistic hydrogen atom and the supercritical discussion.
- Walter Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 1990), for the Dirac–Coulomb problem solved in detail.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the non-relativistic comparison and the fine structure.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the relation of biquaternions to $M_2(\mathbb{C})$ and the spinor representation.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of the Coulomb problem and the spin–orbit coupling.
- Companion articles: *The Hydrogen Atom in Biquaternionic Form — The Non-Relativistic Case*; *The Dirac Equation in Biquaternionic Form*; *The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit*; *Exercise: The Non-Relativistic Limit and the Pauli Equation*; *The Electron in Biquaternionic Form*; *Angular Momentum and Spin in Biquaternionic Form*; *Quantum Mechanics in Biquaternionic Form*; *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*; *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*.
