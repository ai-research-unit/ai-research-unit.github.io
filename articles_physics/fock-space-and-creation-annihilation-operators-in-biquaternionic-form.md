# __Fock Space and Creation/Annihilation Operators in Biquaternionic Form__

## Introduction

The two companion articles on canonical quantization each end by leaving the same object unspecified. *Canonical Quantization of the Biquaternion Dirac Field* promotes the spinor-module representative of the biquaternion Dirac field to an operator-valued field, imposes the equal-time anticommutators, expands the field in the parent article's plane waves, builds the mode algebra, and obtains a Fock space — and then records that "the biquaternion Fock space" is not constructed. *Canonical Quantization of the Biquaternion Maxwell Field* does the same for the electromagnetic field by Gupta–Bleuler and records that whether there is a Fock space native to $\mathbb{B}$ is the subject of the planned companion article on the Fock space. This is that article.

Its question is exact: what does "Fock space and creation/annihilation operators in biquaternionic form" name? Three answers are available, they are not the same answer, and the article separates them at the outset.

1. **The transcription.** The mode operators supplied by the two quantizations generate a Fock space on a module over $\mathbb{B}$: the exterior algebra of the Dirac one-particle space, the symmetric algebra of the Maxwell polarization space. This part is standard, and the parents already carry it out. It is restated here only far enough to ask where its objects live.

2. **The finite-dimensional core.** The part of the construction that is genuinely an object of $\mathbb{B}$ itself. Here the article has a sharp result. The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is, exactly, the operator algebra of **one fermionic mode**: it contains raising and lowering operators satisfying $\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t$ and $\vec\Upsilon_x^2=\vec\Upsilon_y^2=0$, the number operator is an idempotent of the form $\tfrac12(e_t-i\vec u)$ with $\vec u$ a unit pure quaternion, and the fermion-parity grading is realized inside the algebra as conjugation by a Hermitian element. The identification is the oscillator article's two-level truncation, read for what it is rather than for what it fails to be.

3. **The gap.** There is **no Fock space in $\mathbb{B}$.** The Fock space of a single mode is the two-dimensional fundamental module of $\mathbb{B}$, not a subalgebra of it; the Fock space of two modes already has dimension four while the operator algebra of two modes has dimension sixteen; and the Fock space of a field is infinite-dimensional. The phrase "biquaternion Fock space" therefore cannot mean a Fock space inside the algebra. It has to mean a Fock space built from a $\mathbb{B}$-module, and that is what the parents construct. The title of this article promises a Fock space in biquaternionic form; what the framework contains is one mode of one, inside $\mathbb{B}$, with everything beyond it built the standard way on the outside.

The remaining obstruction is the bosonic one, and it is parallel to the fermionic result. One bosonic mode requires $[a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}]=e_t$. No such pair exists in $\mathbb{B}$: the trace of a commutator vanishes while $\mathrm{Tr}(e_t)=2$, so the only relation of the form $[a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}]=c\,e_t$ that can hold in $\mathbb{B}$ has $c=0$. The finite-dimensional algebra carries the fermionic canonical relation exactly and the bosonic canonical relation not at all. The Maxwell Fock space is consequently a standard construction on an imported module, and the framework adds nothing to it beyond the notation.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_t=1,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_k^2=-e_t$, and $i$ is the scalar imaginary with $i^2=-1$. The material (anti-Hermitian) subspace is $\mathbb{M}_-$ and the informational (Hermitian) subspace is $\mathbb{M}_+$; they satisfy $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ and $i\mathbb{M}_\pm=\mathbb{M}_\mp$. The trace is normalized by the matrix representation, $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$, so that $\mathrm{Tr}(e_t)=2$. The isomorphism with $M_2(\mathbb{C})$ is the one fixed in the companion articles, $\mathsf{M}_2(\vec e_k)=-i\sigma_k$, $\mathsf{M}_2(i)=iI_2$, hence $\mathsf{M}_2(i\vec e_k)=\sigma_k$. The fermionic and bosonic mode operators are those established by the two quantization articles and are not rederived.

## Fock Space and Its Operator Algebra

The standard construction, fixed once so that the biquaternion question can be posed against it, is the following.

A one-particle space $\mathcal{H}_1$ is a complex vector space with a Hermitian form, positive definite in the standard case; for a field it is the space of positive-frequency solutions of the one-particle equation. The **Fock space** is the direct sum of the tensor powers of $\mathcal{H}_1$ projected onto the symmetry type selected by the statistics,

$$
\mathcal{F}=\bigoplus_{n\ge0}\Big(\mathcal{H}_1^{\otimes n}\Big)_{\pm},
$$

the antisymmetric projection for fermions and the symmetric projection for bosons. The vacuum $|0\rangle$ spans the $n=0$ term. **Creation and annihilation operators** $a^{\mathrm{fop}\dagger}_i,a^{\mathrm{fop}}_i$ raise and lower the degree, and their brackets are the canonical ones,

$$
\{a^{\mathrm{fop}}_i,a^{\mathrm{fop}\dagger}_j\}=\delta_{ij},\qquad
[a^{\mathrm{fop}}_i,a^{\mathrm{fop}\dagger}_j]=\delta_{ij},
$$

for fermions and bosons respectively, with all other brackets vanishing. The **number operator** is

$$
N=\sum_ia^{\mathrm{fop}\dagger}_ia^{\mathrm{fop}}_i,
$$

with $[N,a^{\mathrm{fop}\dagger}_i]=+a^{\mathrm{fop}\dagger}_i$ and $[N,a^{\mathrm{fop}}_i]=-a^{\mathrm{fop}}_i$ in both cases. The Fock space is graded by $N$, with the occupation basis $|n_1,n_2,\dots\rangle$ diagonalizing it; the fermionic occupation numbers are restricted to $n_i\in\{0,1\}$ by the vanishing of $(a^{\mathrm{fop}\dagger}_i)^2$, itself a consequence of the anticommutation relations, which is the algebraic form of Pauli exclusion.

Two features of this construction govern everything below. First, the **statistics is carried by the bracket**, not by the Fock space: the symmetric and antisymmetric projections are consequences of $[\;,\;]$ or $\{\;,\;\}$. Second, the **operator algebra is generated by the modes**, and the Fock space is a module for that algebra. Both facts are standard; the second is what makes the biquaternion question sharper than it first appears, because $\mathbb{B}$ is finite-dimensional and the algebra generated by the modes of a field is not.

## The One-Particle Space and the Field Expansions

In the biquaternion framework the one-particle space is a module. The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ has, up to equivalence, one nontrivial irreducible module, the two-dimensional complex **spinor module** on which it acts by matrix multiplication; the isomorphism $\mathbb{B}\cong\mathrm{End}(\mathbb{C}^2)$ of the algebraic-representations article is exactly this statement. The one-particle space of the Dirac field is a module of this type: at each momentum the positive-frequency solutions span a two-dimensional complex space, the antiparticle branch is a second copy, and the full one-particle space is the completion of the solution space over all momenta. The many-particle space is its **antisymmetric tensor algebra**, as the Dirac quantization article establishes.

The Maxwell case is the same in structure and different in statistics. The one-particle space at each momentum is the four-dimensional polarization space, carrying the indefinite form $\zeta=(-1,+1,+1,+1)$ inherited from the covariant treatment, and the Fock space is its **symmetric** algebra. The Fock space built on all four polarizations has indefinite norm; the physical subspace selected by the subsidiary condition $(a^{\mathrm{fop}}_0-a^{\mathrm{fop}}_3)|\psi\rangle=0$ (for momentum along $\vec e_z$, as in the parent) has positive-semidefinite norm, positive-definite on the quotient by its zero-norm states, and carries exactly the two transverse polarizations. The parent article gives the mode expansion, the commutators and the polarization sum; none of it is repeated here.

The structural point is the same for both:

> The one-particle space is a module over $\mathbb{B}$; the Fock space is an algebra built from that module. Neither is a subalgebra of $\mathbb{B}$.

This is the sense in which the parents already construct a biquaternionic Fock space, and it is also the sense in which they do not: the Fock space is not an object of the algebra, only a construction that starts from one of its modules.

## Creation and Annihilation Operators from the Two Quantizations

We collect the mode operators that the parents supply, because the rest of the article asks which of them can be elements of $\mathbb{B}$.

**Fermionic (Dirac).** The field expands as

$$
\psi^{\mathrm{fop}}(x)=\int\!\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\vec p}}}\sum_{r=1}^{2}
\Big[a^{\mathrm{fop}}_r(\vec p)w^{(r)}(\vec p)\exp(-ip\cdot x)
+b^{\mathrm{fop}\dagger}_r(\vec p)v^{(r)}(\vec p)\exp(+ip\cdot x)\Big],
$$

with $a^{\mathrm{fop}}_r$ annihilating particles and $b^{\mathrm{fop}}_r$ annihilating antiparticles. The mode algebra is

$$
\{a^{\mathrm{fop}}_r(\vec p),a^{\mathrm{fop}\dagger}_s(\vec k)\}
=\{b^{\mathrm{fop}}_r(\vec p),b^{\mathrm{fop}\dagger}_s(\vec k)\}
=(2\pi)^3\delta_{rs}\delta^{(3)}(\vec p-\vec k),
$$

with all other anticommutators vanishing. The particle number, antiparticle number, the total number of quanta and the electric charge are

$$
N_a=\sum_r\int\!\frac{d^3p}{(2\pi)^3}a^{\mathrm{fop}\dagger}_ra^{\mathrm{fop}}_r,\qquad
N_b=\sum_r\int\!\frac{d^3p}{(2\pi)^3}b^{\mathrm{fop}\dagger}_rb^{\mathrm{fop}}_r,\qquad
F=N_a+N_b,\qquad
Ϙ^{\mathrm{fop}}=N_a-N_b,
$$

and Pauli exclusion is the algebraic identity $(a^{\mathrm{fop}\dagger}_r(\vec p))^2=0$. Here $Ϙ^{\mathrm{fop}}=N_a-N_b$ is the conserved fermion number (the corpus's $\mathrm{U}(1)$ charge), while $F=N_a+N_b$ is the **total number of quanta**, whose parity is the Dirac article's fermion parity $(-1)^F$; the two agree modulo 2, which is why the parity can be written with either. The notation $Ϙ^{\mathrm{fop}}$ is the Dirac quantization article's; $F$ is introduced here.

**Bosonic (Maxwell).** The potential expands in four polarizations with

$$
\big[a^{\mathrm{fop}}_r(\vec k),a^{\mathrm{fop}\dagger}_s(\vec k')\big]
=\zeta_r\,\delta_{rs}\,(2\pi)^3\delta^{(3)}(\vec k-\vec k'),
\qquad
(\zeta_0,\zeta_1,\zeta_2,\zeta_3)=(-1,+1,+1,+1),
$$

and all other commutators vanishing. The timelike mode has negative norm; the physical subspace is defined by the subsidiary condition and carries the two transverse polarizations with positive norm. The physical photon number is the transverse sum

$$
N_\gamma=\sum_{\lambda=1}^{2}\int\!\frac{d^3k}{(2\pi)^3}a^{\mathrm{fop}\dagger}_\lambda a^{\mathrm{fop}}_\lambda,
$$

which is non-negative on the physical subspace. The negative-norm states that the timelike mode builds are removed by the subsidiary condition; on the physical subspace the number operator is the transverse sum above.

None of the operators in this section is new. They are displayed together for one reason: every one of them acts on a module or on a Fock space built from a module, and the question "in biquaternionic form" is the question of which of them, if any, is an element of $\mathbb{B}$.

## The Number Operator and the Born Rule

For a single mode the number operator meets the framework's Born rule, and this is the one place where the Fock construction and the informational sector touch directly. An element of $\mathbb{M}_+$ is Hermitian; $N=a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}$ is Hermitian; and for a state $\tilde{Ϛ}\in\mathbb{M}_+$ that is positive and of trace one, the trace formula gives

$$
\langle N\rangle_{\tilde{Ϛ}}=\mathrm{Tr}(\tilde{Ϛ}\,N)=2\,\mathrm{Sc}(\tilde{Ϛ}\,N).
$$

For one fermionic mode, whose explicit realization is given in the next section, $N$ is an **idempotent** rather than a counting operator: its spectrum is $\{0,1\}$, and $N^2=N$ is the algebraic statement that a mode is either empty or occupied. The trace formula then returns the occupation probability of the mode, which is the Born rule for the two-valued observable "is the mode occupied". For a field, $N$ acts on an infinite-dimensional Fock space and is not an element of $\mathbb{B}$; the trace formula applies to its finite-dimensional truncations only. The distinction is the same one the whole article turns on, and it is visible here in the simplest possible object.

## Three Gradings

The word "grading" is used in this corpus for three different structures, and they must not be conflated. The exercise article on the non-relativistic limit already warns that the Foldy–Wouthuysen grading by $\beta$ is not the $\mathbb{M}_\pm$ grading by ${}^{*}$; a third grading, the fermion parity, is a third thing again.

**1. The fixed-point splitting.** The decomposition $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ is the $\pm1$ eigenspace splitting of the Hermitian conjugation ${}^{*}$. It is a splitting of $\mathbb{B}$ as a real vector space, and it is **not an algebra grading**: the product of two Hermitian elements need not be Hermitian. The smallest counterexample is the one the informational-space article uses to show that $\mathbb{M}_+$ is not a subalgebra,

$$
(i\vec e_x)(i\vec e_y)=i^2\vec e_x\vec e_y=-\vec e_z\in\mathbb{M}_-,
$$

whereas a grading would require $\mathbb{M}_+\cdot\mathbb{M}_+\subseteq\mathbb{M}_+$. What the splitting *does* grade is the **symmetrized** product: for $\tilde Q,\tilde Q_2$ Hermitian the anticommutator $\{\tilde Q,\tilde Q_2\}$ is Hermitian, for $\tilde{Q},\tilde Q_1$ anti-Hermitian it is Hermitian, and for one of each it is anti-Hermitian, so that $\mathbb{B}$ is $\mathbb{Z}/2$-graded as a Jordan algebra by the splitting and not as an associative one. This was checked on random elements of each subspace and is recorded because "the $\mathbb{M}_\pm$ grading" is a phrase the corpus uses loosely.

**2. The number grading.** The Fock space is $\mathbb{N}$-graded by total particle number, with $N$ the degree operator. For fermions the degree is bounded per mode by Pauli exclusion; for bosons it is unbounded. This grading lives on the Fock space, never on $\mathbb{B}$.

**3. The parity grading.** The fermion parity $(-1)^F$ makes the **operator algebra** $\mathbb{Z}/2$-graded: it is $+1$ on states of even total fermion number and $-1$ on states of odd total fermion number, and

$$
(-1)^Fa^{\mathrm{fop}}\,(-1)^F=-a^{\mathrm{fop}},\qquad
(-1)^F|0\rangle=|0\rangle .
$$

The operators split into an even part commuting with $(-1)^F$ and an odd part anticommuting with it, and "fermionic operators anticommute" is precisely the statement that the algebra is graded-commutative. The Dirac quantization article supplies this grading on the mode algebra and records that embedding it in $\mathbb{B}$ is not done. The next section does the one case where it can be done.

The three structures are distinct in every case. The parity grading is an algebra grading; the sector splitting is not, though it grades the symmetrized product; the number grading is a grading of the state space by a non-negative integer. The grading of the ambient Clifford algebra that carries the parity, with the twist as the conjugation by the volume element and the composition of two odd steps, is *The Graded Algebra, Fermion Parity and the Two Sectors with Signed Inner Conjugation in Biquaternionic Form*; the graded bracket and the odd extension of the algebra are *The Superalgebra Reading and the Odd Extension with Signed Inner Conjugation in Biquaternionic Form*.

## What the Algebra Itself Hosts: One Fermionic Mode

We now ask the question the article is named for in its sharpest finite-dimensional form: which creation and annihilation operators are elements of $\mathbb{B}$?

### The Capacity of the Algebra

The algebra $\mathbb{B}$ has complex dimension four. A fermionic mode is a pair $a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}$ satisfying the canonical anticommutation relations

$$
\{a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}\}=e_t,\qquad a^{\mathrm{fop}}^2=0,\qquad (a^{\mathrm{fop}\dagger})^2=0 .
$$

The algebra these generate is the one-mode canonical anticommutation (CAR) algebra, which is $M_2(\mathbb{C})$: using $a^{\mathrm{fop}}^2=(a^{\mathrm{fop}\dagger})^2=0$ the only monomials are $e_t,a^{\mathrm{fop}},a^{\mathrm{fop}\dagger},a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}$, and a nonzero mode generates this four-dimensional simple algebra faithfully. Its complex dimension is four, equal to $\dim_\mathbb{C}\mathbb{B}$, so the one-mode algebra is all of $\mathbb{B}$. Conversely, $N$ independent fermionic modes generate the algebra $\mathrm{Cl}(2N)\cong M_{2^N}(\mathbb{C})$ of complex dimension $4^N$, which for $N\ge2$ exceeds four. The conclusion is a dimension count and is therefore exact:

> Up to the automorphisms of the algebra, $\mathbb{B}$ carries exactly **one** fermionic mode, and it is the whole algebra.

For $N=1$, $\dim_\mathbb{C}M_2(\mathbb{C})=4=\dim_\mathbb{C}\mathbb{B}$; for $N=2$ the operator algebra is $M_4(\mathbb{C})$, dimension sixteen, and there is no room for it. No algebra of two fermionic modes is a subalgebra of $\mathbb{B}$. A Fock space is in any case a state space rather than an operator algebra, so the statement "the Fock space is in $\mathbb{B}$" can only mean that the state space is the fundamental module and the operators on it lie in the algebra — which is what happens for one mode and fails for two.

### The Explicit Operators

The single mode is already in the corpus. The harmonic oscillator article constructs the two-level truncation of a mode,

$$
\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y),\qquad
\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y),\qquad
\tilde\Pi_-=\vec\Upsilon_y\vec\Upsilon_x=\tfrac12(e_t-i\vec e_z),
$$

and reads them as an unfaithful truncation of a **bosonic** oscillator: the commutator is $[\vec\Upsilon_x,\vec\Upsilon_y]=i\vec e_z\ne e_t$, which is a failure of the bosonic canonical relation. That interpretation is correct, and nothing here contradicts it. Asked the fermionic question instead, the same operators answer exactly. Direct computation gives

$$
\vec\Upsilon_x^2=0,\qquad (\vec\Upsilon_y)^2=0,\qquad
\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t,\qquad
\tilde\Pi_-^2=\tilde\Pi_-,
$$

so the truncated ladder satisfies the **fermionic** canonical anticommutation relations with no truncation error at all. The operators are the angular-momentum article's spin ladder up to the factor $\hbar$, $\tilde S_+=\tfrac{\hbar}{2}(i\vec e_x-\vec e_y)$; the annihilation and creation operators of the single mode are the spin-raising and spin-lowering operators of the informational sector. Under the isomorphism $\mathsf{M}_2(\vec e_k)=-i\sigma_k$ they have the images

$$
\mathsf{M}_2(\vec\Upsilon_x)=|0\rangle\langle1|,\qquad
\mathsf{M}_2(\vec\Upsilon_y)=|1\rangle\langle0|,\qquad
\mathsf{M}_2(\tilde\Pi_-)=|1\rangle\langle1|,\qquad
\mathsf{M}_2(i\vec e_z)=\sigma_3,
$$

where $|0\rangle=(1,0)^{\mathsf T}$ and $|1\rangle=(0,1)^{\mathsf T}$ in the module.

Three consequences follow at once, all of them recomputed above.

- **The Fock space is the fundamental module.** The single-mode Fock space is the two-dimensional spinor module $\mathbb{C}^2$, on which $\mathbb{B}=\mathrm{End}(\mathbb{C}^2)$ acts irreducibly. The vacuum and the occupied state are its two rays; their idempotents are $\tilde\Pi_+=\tfrac12(e_t+i\vec e_z)$ and $\tilde\Pi_-=\tfrac12(e_t-i\vec e_z)$, the two associated with the root of $+1$ $i\vec e_z$ since $(i\vec e_z)^2=e_t$, and $\tilde\Pi_-=\tilde\Pi_-$. The number operator of a single fermionic mode is a pure-state idempotent of the informational sector.
- **The grading is an element of the algebra.** Fermion parity for one mode is

$$
(-1)^F=e_t-2\tilde\Pi_-=i\vec e_z,
$$

which is Hermitian, squares to $e_t$, and satisfies $(-1)^F\vec\Upsilon_x(-1)^F=-\vec\Upsilon_x$ and $(-1)^F\tilde\Pi_-(-1)^F=\tilde\Pi_-$. The $\mathbb{Z}/2$ grading the Dirac quantization article had to impose on the mode algebra is, for one mode, realized **inside** $\mathbb{B}$: it is the inner automorphism by the Hermitian involution $(-1)^F\in\mathbb{M}_+$, and its odd subspace is the two-complex-dimensional span of the ladder and its adjoint.
- **The grading is not unique.** The choice $i\vec e_z$ is the choice of a mode; for any unit pure quaternion $\vec u$ the element $i\vec u$ is Hermitian, squares to $e_t$, and defines a grading whose odd part consists of the ladder operators in the corresponding plane, with $\tilde\Pi_-=\tfrac12(e_t-i\vec u)$. This was checked on $\vec u=(\vec e_x+\vec e_y+\vec e_z)/\sqrt3$, a direction chosen after the claim rather than the $\vec e_z$ direction that suggested it. The family is parametrized by the unit pure quaternions, that is, by a two-sphere, with $\vec u$ and $-\vec u$ giving the same grading.

### What the Capacity Statement Does and Does Not Say

It does say that the fermionic canonical anticommutation relations, the one-mode number operator, the vacuum idempotent, and the fermion-parity grading all exist as elements of $\mathbb{B}$, and that this is forced by the dimension count rather than chosen: one mode saturates the algebra, so no other choice of single mode is inequivalent, and no second mode can be added.

It does not say that the framework **derives** fermionic statistics, or statistics at all. The anticommutation relations are imposed on $\vec\Upsilon_x,\vec\Upsilon_y$; the identification exhibits a realization, not a derivation. Whether the framework selects the fermionic structure, or merely happens to have the dimension that hosts one fermionic mode, is the open question of the article and is recorded as such in the closing section. The dimension coincidence $4=4$ is exact but it is a coincidence of dimensions until something more is said.

## The Bosonic Case

A bosonic mode is a pair satisfying $[a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}]=e_t$. In a finite-dimensional algebra this is impossible for a reason that does not depend on $\mathbb{B}$. A canonical commutator would have to be a central scalar, $[a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}]=c\,e_t$; but the trace of a commutator vanishes, so

$$
0=\mathrm{Tr}\big([a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}]\big)=c\,\mathrm{Tr}(e_t)=2c,
$$

and hence $c=0$. The trace formula $\mathrm{Tr}(e_t)=2\,\mathrm{Sc}(e_t)=2$ is what makes the right-hand side nonzero, and it is the only central scalar available: the centre of $\mathbb{B}=M_2(\mathbb{C})$ is exactly the complex span of $e_t$, so there is no other candidate for a canonical commutator. The oscillator article reaches the same conclusion through the scalar part of the bracket of two Hermitian elements; the trace argument is the stronger statement, because it rules out any finite-dimensional realization of the Heisenberg pair at all.

The consequence for the framework is worth stating plainly. The Maxwell quantization's Fock space is the symmetric algebra of a module, and its creation and annihilation operators are **not** elements of $\mathbb{B}$: they are elements of the Weyl algebra of the polarization space, which is infinite-dimensional, or of a specific finite truncation of it. The framework contributes to that construction the module on which it is built and the notation in which the polarization sum is written; it contributes no ladder algebra of its own, because it has none to contribute. The indefinite metric, the subsidiary condition and the physical-subspace quotient are imported, exactly as the Maxwell article records. The bosonic case is therefore not the fermionic case with a sign changed; it is a case in which the finite-dimensional algebra has no native structure at all.

## Fermionic Versus Bosonic in the Framework

| | Fermionic | Bosonic |
|---|---|---|
| Canonical bracket | $\{a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}\}=e_t$ | $[a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}]=e_t$ |
| Realizable in $\mathbb{B}$? | Yes, exactly one mode | No, not one mode |
| Mode operator algebra | $\mathrm{Cl}(2)\cong M_2(\mathbb{C})=\mathbb{B}$ | Weyl algebra, infinite-dimensional |
| Single-mode Fock space | fundamental module $\mathbb{C}^2$ | $\ell^2(\mathbb{N})$ |
| Field Fock space | antisymmetric algebra of the module | symmetric algebra of the module |
| Number operator | idempotent for one mode; spectrum $\{0,1\}$ | unbounded spectrum; not in $\mathbb{B}$ |
| $\mathbb{Z}/2$ parity grading | nontrivial; an element of $\mathbb{B}$ for one mode | exists on the Fock space, but the modes commute and no anticommutation is imposed |
| What $\mathbb{B}$ supplies | the whole one-mode algebra | the module, and nothing algebraic |

The table's last row is the article's finding in one line. The statistics is carried by the (anti)commutation rule — the Dirac article states this for the mode algebra — and the KMS article reaches the same point from the thermal side, where the statistics enters through the time-ordered correlation functions and the $\mathbb{Z}/2$ grading of the operator algebra rather than through the bracket of the mode operators itself. The finite-dimensional algebra can carry the fermionic bracket for a single mode and cannot carry the bosonic bracket for any mode. The asymmetry is not a preference of the framework for fermions. It is the finite dimension of $\mathbb{B}$ acting on a dimension count and a trace identity, and it disappears as soon as the construction moves to the infinite-dimensional module where the fields actually live, where both the exterior and the symmetric algebra are available on the same footing.

## What This Article Establishes and What It Does Not

**Established, and recomputed here.**

- The single fermionic mode is realized in $\mathbb{B}$: $\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)$ and $\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y)$ satisfy $\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t$ and are nilpotent, with $\tilde\Pi_-=\tfrac12(e_t-i\vec e_z)$ idempotent.
- The one-mode Fock space is the fundamental module of $\mathbb{B}$, and $\mathbb{B}$ is its endomorphism algebra.
- Fermion parity for one mode is the element $(-1)^F=i\vec e_z\in\mathbb{M}_+$, and conjugation by it is the $\mathbb{Z}/2$ grading; the grading is defined by the choice of a unit pure quaternion, a two-sphere of choices.
- The capacity of $\mathbb{B}$ is one fermionic mode: $N$ modes generate $M_{2^N}(\mathbb{C})$, of dimension $4^N$, which exceeds four for $N\ge2$.
- No bosonic mode exists in $\mathbb{B}$, by the trace of a commutator; the obstruction is the finite dimension, not the sector structure.
- The fixed-point splitting $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ is not an associative-algebra grading, though it grades the symmetrized product.

**Standard, and inherited from the parents.** The Fock-space construction, the exterior and symmetric algebras, the Dirac and Maxwell mode algebras, Pauli exclusion as $(a^{\mathrm{fop}\dagger})^2=0$, the charge $Ϙ^{\mathrm{fop}}=N_a-N_b$, the Gupta–Bleuler subsidiary condition and the two transverse polarizations. None of this is rederived here and none of it depends on the biquaternion structure beyond the kinematical conventions.

**Open.**

- **Whether the one-mode identification is a coincidence.** The equality $\dim_\mathbb{C}M_2(\mathbb{C})=\dim_\mathbb{C}\mathbb{B}=4$ is exact, but a dimension coincidence is not a derivation. Whether the framework singles out the fermionic canonical structure, or whether it merely has room for one instance of it, is not decided here.
- **The biquaternion Fock space as such.** The article's answer is negative for the algebra: there is no Fock space inside $\mathbb{B}$, and for more than one mode there is not even the operator algebra. A construction native to $\mathbb{B}$ that is not the exterior or symmetric algebra of a module is not exhibited, and the parents' phrase "the biquaternion Fock space" remains uninstantiated beyond the one-mode case.
- **Embedding the field grading in $\mathbb{B}$.** The single-mode grading is an element of the algebra; the field grading $(-1)^F$ is not, and no element of the four-dimensional algebra can represent it. Whether some other algebraic structure attached to $\mathbb{B}$ can, is open.
- **The spin–statistics theorem.** Whether this construction derives spin–statistics or only transcribes it is the subject of the dedicated companion article; nothing here decides it.
- **The vacuum energy and the empirical question.** Whether the algebra selects a regularization of the normal-ordering constant, and whether any of this yields a prediction distinguishing the framework from standard quantum field theory, remain open as in the parents.

## Summary

The creation and annihilation operators of the biquaternion Dirac and Maxwell fields are the mode operators constructed in the two canonical-quantization articles; their Fock spaces are the exterior and symmetric algebras of the modules on which those operators act. Neither Fock space is an object of the algebra $\mathbb{B}$. The finite-dimensional part of the construction is exactly one fermionic mode: $\mathbb{B}\cong M_2(\mathbb{C})$ is the whole one-mode operator algebra, its Fock space is the fundamental module, its number operator $\tilde\Pi_-=\tfrac12(e_t-i\vec e_z)$ is an idempotent, and its fermion parity $(-1)^F=i\vec e_z$ is a Hermitian element whose conjugation is the $\mathbb{Z}/2$ grading. These are the oscillator article's truncated ladder operators; they satisfy the fermionic, not the bosonic, canonical relation.

The capacity is one mode and no more: $N$ fermionic modes generate $M_{2^N}(\mathbb{C})$ of dimension $4^N$, which leaves no room in a four-dimensional algebra as soon as $N\ge2$. The bosonic case is worse rather than analogous: no pair in $\mathbb{B}$ satisfies $[a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}]=e_t$, because the trace of a commutator vanishes, so the Maxwell ladder is not in the algebra at all. The statistics is carried by the bracket, and the framework's own algebra carries the fermionic bracket once.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) subspaces |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ | Trace formula; $\mathrm{Tr}(e_t)=2$ |
| $\mathsf{M}_2(\vec e_k)=-i\sigma_k$, $\mathsf{M}_2(i)=iI_2$ | Isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ |
| $\mathcal{H}_1$, $\mathcal{F}$ | One-particle space; Fock space |
| $a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}$ | Annihilation and creation operators (general) |
| $N=\sum_ia^{\mathrm{fop}\dagger}_ia^{\mathrm{fop}}_i$ | Number operator |
| $a^{\mathrm{fop}}_r(\vec p),b^{\mathrm{fop}}_r(\vec p)$ | Dirac particle and antiparticle mode operators (parent's notation) |
| $F=N_a+N_b$, $Ϙ^{\mathrm{fop}}=N_a-N_b$ | Total number of quanta (parity $(-1)^F$), and fermion number (= electric charge) |
| $a^{\mathrm{fop}}_r(\vec k)$, $\zeta=(-1,+1,+1,+1)$ | Maxwell mode operators and indefinite metric |
| $N_\gamma$ | Photon number (transverse sum) |
| $\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)$ | Single-mode annihilation operator in $\mathbb{B}$ |
| $\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y)$ | Single-mode creation operator in $\mathbb{B}$ |
| $\tilde\Pi_-=\tfrac12(e_t-i\vec e_z)$ | Single-mode number operator (idempotent) |
| $(-1)^F=i\vec e_z$ | Fermion parity (single mode); conjugation is the $\mathbb{Z}/2$ grading |
| $\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t$ | Canonical anticommutator, realized in $\mathbb{B}$ |
| $\mathrm{Cl}(2N)\cong M_{2^N}(\mathbb{C})$ | Mode algebra of $N$ fermionic modes |

## Further Reading

- V. A. Fock, "Konfigurationsraum und zweite Quantelung," *Zeitschrift für Physik* **75** (1932) 622–647, for the original occupation-number formulation of the many-particle space.
- P. Jordan and E. Wigner, "Über das Paulische Äquivalenzverbot," *Zeitschrift für Physik* **47** (1928) 631–651, for the anticommuting creation and annihilation operators and the exclusion rule as an algebraic identity.
- F. A. Berezin, *The Method of Second Quantization* (Academic Press, 1966), for the exterior and symmetric algebras as the fermionic and bosonic Fock spaces.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), and M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the mode expansions, the canonical brackets, and the number operators used here.
- O. Bratteli and D. W. Robinson, *Operator Algebras and Quantum Statistical Mechanics* 2 (Springer, 1997), for the CAR and CCR algebras and the Fock representations generated by finitely and infinitely many modes.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the occupation-number treatment of the oscillator and its two-level truncation.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), and H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton, 1989), for the Clifford algebras $\mathrm{Cl}(2N)$ and the isomorphism $\mathrm{Cl}(2)\cong M_2(\mathbb{C})$ used in the capacity count.
- Companion articles: *Canonical Quantization of the Biquaternion Dirac Field*; *Canonical Quantization of the Biquaternion Maxwell Field*; *The Harmonic Oscillator in Biquaternionic Form*; *Angular Momentum and Spin in Biquaternionic Form*; *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*.
