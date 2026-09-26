# __The Scalar Fock Space in Biquaternionic Form__

## Introduction

The companion article *Canonical Quantization of the Biquaternion Klein–Gordon Field* builds the scalar Fock space as the symmetric algebra of the one-particle space, and the companion article *The Quantized Scalar Field in Biquaternionic Form* exhibits the field operator that acts on it. This article asks what that state space is in the framework: what its one-particle space is as a module, how its symmetric algebra is organised, what its vacuum and its gradings are, and whether any of it is an object of the algebra $\mathbb{B}$.

The general construction is not in question and is not re-derived. The companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* fixes it once for the whole series: a one-particle space $\mathcal{H}_1$, the direct sum of its tensor powers projected onto the symmetry type selected by the statistics, creation and annihilation operators raising and lowering the degree, and a number operator whose eigenvalues are the occupation numbers. For bosons the projection is symmetric and the bracket is a commutator. What is specific to the scalar sector is which module the construction starts from and what the algebra contributes to it. Three answers organise the article.

1. **The one-particle space is a module over the center of the algebra, and carries the trivial action of its spin part.** The positive-frequency solutions of the parent equation transform in the trivial representation of the Lorentz group; no spinor index is carried. The trace-free part of $\mathbb{B}$, which carries the Lorentz/spin content, therefore annihilates a spin-$0$ state, and only the central scalars act nontrivially. The irreducible modules of $\mathbb{B}\cong M_2(\mathbb{C})$ are the spinor modules, and the scalar state space is not one of them: it is a module for the center, in contrast with the spinor module, on which the whole algebra acts. This is the state-space form of the statement that spin $0$ escapes the biquaternion state module.
2. **The Fock space is the symmetric algebra of that module, and it is not an object of $\mathbb{B}$.** The occupation basis is the standard bosonic one; the vacuum is the degree-zero term; the number operator grades by total occupation. None of these is a subalgebra or a subspace of the four-dimensional algebra, and the companion Fock-space article proves the exclusion by the trace of a commutator: no pair $\tilde a,\tilde a^\dagger\in\mathbb{B}$ satisfies $[\tilde a,\tilde a^\dagger]=e_0$.
3. **The state space carries a $\mathbb{N}$-grading by number and a $\mathbb{Z}$-grading by charge, and no $\mathbb{Z}/2$ parity grading.** The scalar Fock space is graded by particle number and, for the complex field, by the $U(1)$ charge, whose sectors are the fixed-particle-number, fixed-charge subspaces. There is no bosonic analogue of the fermion parity that the Dirac case needs, because the bosonic operators commute and no graded-commutativity is imposed.

The article is organised as follows. The next section fixes the one-particle space and its module structure. The following section builds the symmetric algebra and the occupation basis. The next section treats the vacuum. The section after that treats the number operator and the two gradings. The next section states the obstruction to a Fock space inside $\mathbb{B}$, verifies the dimension count, and contrasts it with the bounded fermionic case. A section connects the Fock construction to the informational sector and the trace formula. A short section treats coherent states and the central phase. The article closes with the standard/open separation.

- Companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, for the Fock construction, the trace argument against a bosonic mode in $\mathbb{B}$, and the fermionic one-mode result the scalar case is measured against.
- Companion article *Canonical Quantization of the Biquaternion Klein–Gordon Field*, for the mode algebra, the Hamiltonian and the charge whose spectrum the Fock space diagonalizes.
- Companion article *The Quantized Scalar Field in Biquaternionic Form*, for the field operator that acts on the Fock space.
- Companion article *The Klein–Gordon Equation in Biquaternionic Form*, for the one-particle solutions and their two branches.
- Companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the Hermitian sector, the states, and the trace formula of the Born rule.
- Companion article *The Vacuum State and the Casimir Effect in Biquaternionic Form*, for the vacuum energy and its regularization.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$, and $i$ is the central scalar imaginary. The material and informational sectors are $\mathbb{M}_-$ and $\mathbb{M}_+$, with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ and $i\mathbb{M}_\pm=\mathbb{M}_\mp$; the center is $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$. The trace formula is $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$, normalized so that $\mathrm{Tr}(e_0)=2$, and the isomorphism used for the capacity count is $\mathbb{B}\cong M_2(\mathbb{C})$. Natural units $\hbar=c=1$ are used throughout, with $E_{\mathbf{p}}=\sqrt{\mathbf{p}^2+\mu^2}$ and $\mu=mc/\hbar$.

## The One-Particle Space and Its Module Structure

The one-particle space of the scalar field is the space of positive-frequency solutions of the parent equation, completed in the Lorentz-invariant inner product. At each momentum it is one complex dimension, so

$$
\mathcal{H}_1=\overline{\left\{f:\mathbb{R}^3\to\mathbb{C}\right\}}^{\ \langle\cdot,\cdot\rangle},
\qquad
\langle f,g\rangle=\int\!\frac{d^3p}{(2\pi)^3\,2E_{\mathbf{p}}}\,f^*(\mathbf{p})\,g(\mathbf{p}),
$$

and it is a complex Hilbert space on which the orthochronous Lorentz group acts by the trivial (spin-$0$) representation, the translation group by a central phase, and the $U(1)$ by the phase generated by the charge.

The module-theoretic statement is worth making precisely, because it is where the framework's structure enters the state space. The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ has, up to equivalence, one irreducible module: the two-dimensional spinor module on which it acts by matrix multiplication. The scalar one-particle space is **not** that module. Since the scalar state transforms trivially under the Lorentz group, no non-central element of $\mathbb{B}$ can act on it without mixing it into a higher-spin sector; the only elements that preserve the spin-$0$ subspace are the central scalars. Hence

$$
\tilde A\in\mathbb{C}_{\mathbb{B}}\ \text{acts as a scalar},\qquad
\tilde A\notin\mathbb{C}_{\mathbb{B}}\ \text{does not act on a spin-}0\ \text{state},
$$

and the scalar one-particle space is a module over the center. At the level of the generators every commutator $[\tilde A,\tilde B]$ acts as zero, so only the central part of an element contributes and the spin part of the algebra is invisible on a spin-$0$ state. In the associative sense no nonzero action of the whole algebra exists, and the reason is one line: the trace-free part generates $\mathbb{B}$, so if $e_1$ acted as zero then $e_1^2=-e_0$ would force the identity to act as zero as well, and with it every element. The irreducible biquaternion modules are the spinor modules; the scalar state space is a module for the center and for the mode algebra, not for $\mathbb{B}$. This is the representation-theoretic content of "spin $0$ lives in the center", stated at the level of the state space rather than the field.

The complex structure that makes $\mathcal{H}_1$ a complex vector space is the central scalar imaginary $i$; the $U(1)$ phase it generates is the internal symmetry of the charged field. In the framework's conjugation language, the Hermitian conjugation ${}^\dagger$ fixes the real subspace of the one-particle space and exchanges the particle and antiparticle branches; the algebra's real structure $\flat=-\dagger$ acts on the central values and not on the module. The one-particle space thus inherits the center's complex structure and nothing of the spinor structure.

## The Little Group and One State per Momentum

The one-particle space is fixed up to unitary equivalence by two inputs: the mass shell and the little-group representation. The on-shell momenta of mass $\mu$ form the orbit of a representative momentum under the orthochronous Lorentz group, and the stability group of that representative is the rotation group $SO(3)$, the little group of a massive particle. A particle of spin $s$ transforms in the $(2s+1)$-dimensional irreducible representation of the little group, and the one-particle space is the space of square-integrable functions on the mass shell with values in that representation. For the scalar field $s=0$, and the little-group representation is the **trivial** one,

$$
|\mathbf{p}\rangle=\hat a_{\mathbf{p}}^\dagger|0\rangle,
\qquad
U(\Lambda)|\mathbf{p}\rangle=|\Lambda\mathbf{p}\rangle ,
$$

one state per momentum, with no polarization label, no discrete index and no Wigner rotation. The framework's rotor group acts through the trivial representation for the same algebraic reason as the field: the scalar is the singlet of the rotor conjugation, $\tilde\Lambda e_0\tilde\Lambda^\dagger=e_0$. The invariant measure

$$
\int\!\frac{d^3p}{(2\pi)^3\,2E_{\mathbf{p}}}
$$

is the Lorentz-invariant measure on the mass shell, and it is the measure appearing in the inner product of $\mathcal{H}_1$; the factor $1/(2E_{\mathbf{p}})$ is fixed by that invariance and not by a convention. This is the state-space form of the trivial spin: one degree of freedom per momentum, with no finite label to carry the representation.

## The Symmetric Algebra and the Occupation Basis

The Fock space is the symmetric algebra of $\mathcal{H}_1$,

$$
\mathcal{F}=\bigoplus_{n\ge0}\mathrm{Sym}^n\mathcal{H}_1,
\qquad
\mathrm{Sym}^n\mathcal{H}_1=\Big(\mathcal{H}_1^{\otimes n}\Big)_{+},
$$

the subscript denoting the projection onto the totally symmetric tensors. Creation and annihilation operators act by

$$
\hat a^\dagger(\mathbf{p}):\ \mathrm{Sym}^n\to\mathrm{Sym}^{n+1},
\qquad
\hat a(\mathbf{p}):\ \mathrm{Sym}^n\to\mathrm{Sym}^{n-1},
$$

and the **occupation basis** $|n_{\mathbf{p}_1},n_{\mathbf{p}_2},\dots\rangle$, with finitely many nonzero occupations, diagonalizes the single-family number operator $\hat n=\int\frac{d^3p}{(2\pi)^3}\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}$, whose eigenvalues are the total occupation of the particle modes; the total number operator of the complex field, below, adds the antiparticle family. The basis vectors are obtained from the vacuum by

$$
|n_{\mathbf{p}_1},n_{\mathbf{p}_2},\dots\rangle
=\prod_i\frac{\big(\hat a^\dagger_{\mathbf{p}_i}\big)^{n_i}}{\sqrt{n_i!}}\,|0\rangle ,
$$

and the normalization is the standard bosonic one, with $n_i\in\mathbb{N}$ unbounded above. For the complex field the creation operators come in two families, $\hat a^\dagger$ for particles and $\hat b^\dagger$ for antiparticles, and the basis is labelled by both occupations.

**Verification of the counting.** The dimension of the truncation of the $d$-mode symmetric algebra to total occupation at most $n_{\max}$ is $\binom{d+n_{\max}}{n_{\max}}$, and the direct enumeration of the occupation vectors agrees: for $d=2$, $n_{\max}=4$ the dimension is $15$; for $d=3$, $n_{\max}=3$ it is $20$; for $d=4$, $n_{\max}=3$ it is $35$. Each of these already exceeds the complex dimension $4$ of $\mathbb{B}$, which is the first indication of the obstruction made precise below.

The one-particle space carries the representation content of the field, and the symmetric algebra inherits it: the $n$-particle sector is the symmetric part of the $n$-fold tensor power of the trivial spin-$0$ representation, hence again trivial, and the $U(1)$ charge of an $n$-particle state is $n$ (or $n_a-n_b$ for the complex field). The Fock space is a module for the CCR algebra generated by the modes, not for $\mathbb{B}$; the center acts on it by scalars, and the spin part of the algebra acts trivially on it, so the whole apparatus of the spinor sectors is absent.

### The Symmetric Algebra as a Quotient, and its Completion

The symmetric algebra admits three equivalent descriptions, and the equivalence is worth recording because the obstruction below is a statement about dimensions. First, it is the quotient of the tensor algebra by the two-sided ideal generated by the commutators of vectors,

$$
\mathrm{Sym}(\mathcal{H}_1)=T(\mathcal{H}_1)\big/I,
\qquad
I=\Big\langle\,x\otimes y-y\otimes x\ \big|\ x,y\in\mathcal{H}_1\,\Big\rangle ,
$$

which is the algebraic encoding of bosonic statistics: the relations imposed on the tensor algebra are exactly the commutation of the one-particle states. Second, on a $d$-dimensional model space it is the algebra of polynomials in $d$ commuting variables, $\mathbb{C}[z_1,\dots,z_d]$. Third, its dimensions are generated by

$$
\sum_{n\ge0}\dim\mathrm{Sym}^n\mathbb{C}^d\;z^n=(1-z)^{-d}
=\sum_{n\ge0}\binom{d+n-1}{n}z^n ,
$$

so that the truncation to total occupation at most $n_{\max}$ has dimension $\sum_{n=0}^{n_{\max}}\binom{d+n-1}{n}=\binom{d+n_{\max}}{n_{\max}}$, the count verified above.

**The completion.** The direct sum $\bigoplus_n\mathrm{Sym}^n\mathcal{H}_1$ consists of states of finite total number, and it is dense in the **Fock space**, which is its completion in the inner product: the physical state space contains the square-summable superpositions of arbitrarily high but finite particle number. The distinction matters for unbounded operators. The number operator is essentially self-adjoint on the algebraic direct sum but not defined on the whole completion; the field operator is densely defined with the finite-particle subspace in its domain, and the smeared field maps that subspace into itself. Every operator of the theory is thus determined by its action on the finite-particle states, and the completion adds only the limits.

## The Vacuum State

The vacuum $|0\rangle$ spans the degree-zero term $\mathrm{Sym}^0\mathcal{H}_1=\mathbb{C}$ and is annihilated by every annihilation operator,

$$
\hat a_{\mathbf{p}}|0\rangle=0\quad\forall\mathbf{p},
\qquad
\langle0|0\rangle=1 ,
$$

with the phase fixed by convention. It is the unique normalizable state of zero total number, and (for the complex field) of zero charge. Every finite-particle state of the Fock space is obtained from it by a polynomial in the creation operators, and the whole Fock space is the closure of those states, so the vacuum is cyclic for the field algebra; this is the standard Fock property and is what makes the Fock representation the natural one. The distinction between the algebraic direct sum and its completion, recorded above, is the precise sense in which "obtained from it" is meant: the finite combinations are dense, and the general state is their limit.

The framework-specific question is whether the vacuum is an object of $\mathbb{B}$, and the answer is negative, in contrast with the fermionic one-mode case. The companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* records the contrast sharply: for one **fermionic** mode the vacuum projector is the rank-one idempotent $\tfrac12(e_0+ie_3)\in\mathbb{M}_+$, whose trace is one, and the Born rule pairs it with the number operator $\tfrac12(e_0-ie_3)$ to give the occupation probability, zero for the vacuum and one for the occupied state; the Fock space of one fermionic mode is the fundamental module $\mathbb{C}^2$ of $\mathbb{B}\cong\mathrm{End}(\mathbb{C}^2)$. For a **bosonic** mode there is no such element: the number operator is not idempotent, its spectrum is $\{0,1,2,\dots\}$ unbounded, and no pair in $\mathbb{B}$ realizes the ladder. The scalar vacuum is therefore a Fock vector constructed on an imported module, not a minimal idempotent of the algebra, and the contrast with the fermionic case is the difference between a finite-dimensional realization and an infinite-dimensional one.

One point of contact survives and is treated in a later section: a **truncated** bosonic mode, restricted to finitely many levels, can be represented by finite matrices, and the vacuum of the truncation is a vector in a finite-dimensional space; the trace formula then gives occupation probabilities for the truncated observables. The truncation is a computational device, not an object of $\mathbb{B}$.

## The Number Operator and the Two Gradings

The number operator grades the Fock space by total occupation,

$$
\hat N=\int\!\frac{d^3p}{(2\pi)^3}\left(\hat a_{\mathbf{p}}^\dagger\hat a_{\mathbf{p}}+\hat b_{\mathbf{p}}^\dagger\hat b_{\mathbf{p}}\right),
\qquad
\mathcal{F}=\bigoplus_{n\ge0}\mathcal{F}_n,
\qquad
\hat N\big|_{\mathcal{F}_n}=n ,
$$

and its commutators with the modes are $[\hat N,\hat a^\dagger_{\mathbf{p}}]=+\hat a^\dagger_{\mathbf{p}}$ and $[\hat N,\hat a_{\mathbf{p}}]=-\hat a_{\mathbf{p}}$, in the bosonic case exactly as in the fermionic one. The number grading is the $\mathbb{N}$-grading of the symmetric algebra.

The complex scalar field carries a second grading, by the conserved charge,

$$
\hat Q=\int\!\frac{d^3p}{(2\pi)^3}\left(\hat a_{\mathbf{p}}^\dagger\hat a_{\mathbf{p}}-\hat b_{\mathbf{p}}^\dagger\hat b_{\mathbf{p}}\right),
\qquad
\mathcal{F}=\bigoplus_{q\in\mathbb{Z}}\mathcal{F}_q,
\qquad
\hat Q\big|_{\mathcal{F}_q}=q .
$$

The charge grading is a $\mathbb{Z}$-grading, and it is the grading that separates the particle from the antiparticle sectors; a state of charge $q$ contains, in the simplest case, $q$ more particles than antiparticles. It is a superselection rule: the charge is central and conserved, so no local operator of the theory connects different $\mathcal{F}_q$, and the relative phase between charge sectors is unobservable. This is the bosonic counterpart of the fermionic charge; a process that creates a particle–antiparticle pair changes the total number by two and the charge by zero, so it moves within a fixed $\mathcal{F}_q$.

The two gradings are distinct and neither is the fermion parity. The parity grading of the Dirac sector is a $\mathbb{Z}/2$-grading of the **operator algebra**, because the fermionic modes anticommute and the algebra is graded-commutative; for the bosonic field the modes commute, no anticommutation is imposed, and there is no parity operator analogous to $(-1)^F$. The number grading is an $\mathbb{N}$-grading of the state space; the charge grading is a $\mathbb{Z}$-grading of the state space; the parity grading, where it exists, is a $\mathbb{Z}/2$-grading of the algebra. The three must not be conflated, and in the scalar sector only the first two are present.

### Normal Ordering and the Number Operator from the Field

The number operator of a mode is obtained from the field by normal ordering, and the construction makes the positivity of the spectrum explicit. With the positive- and negative-frequency parts of the companion field article,

$$
:\!\hat{\phi}^\dagger(x)\hat{\phi}(x)\!:
\,=\,\hat{\phi}^{(+)\dagger}(x)\,\hat{\phi}^{(+)}(x)
+\hat{\phi}^{(-)}(x)\,\hat{\phi}^{(-)\dagger}(x)
+\hat{\phi}^{(+)\dagger}(x)\,\hat{\phi}^{(-)}(x)
+\hat{\phi}^{(-)\dagger}(x)\,\hat{\phi}^{(+)}(x),
$$

the density in which every creation operator stands to the left of every annihilation operator. The first two terms are the particle and antiparticle number densities and the last two are the crossed particle–antiparticle terms; all four terms of $\hat\phi^\dagger\hat\phi$ appear, the antiparticle density displayed second being the one term whose operators are reversed relative to the unordered product $\hat\phi^{(-)\dagger}\hat\phi^{(-)}$. The normal-ordered density has vanishing vacuum expectation by construction, whereas the unordered product carries the c-number commutator $[\hat\phi^{(-)\dagger},\hat\phi^{(-)}]$; this is why the vacuum energy of the companion quantization is a contact term. Integrating the normal-ordered density over space and projecting onto a mode gives the mode number,

$$
\hat n_{\mathbf{p}}=\hat a_{\mathbf{p}}^\dagger\hat a_{\mathbf{p}} ,
\qquad
\langle\psi|\hat n_{\mathbf{p}}|\psi\rangle
=\big\|\hat a_{\mathbf{p}}\psi\big\|^2\ge0 ,
$$

so the expectation of the number is a sum of squared norms and the spectrum is non-negative and integer. The normal-ordered charge of the complex field is $\hat Q=\int\frac{d^3p}{(2\pi)^3}(\hat a^\dagger\hat a-\hat b^\dagger\hat b)$, and it is the difference of two positive operators, hence unbounded above and below; the normal-ordered Hamiltonian is their sum with weights $E_{\mathbf{p}}$, hence bounded below. The two statements together are the operator form of the statement that the Fock space's $\mathbb{N}$-grading is compatible with the Hamiltonian and that the $\mathbb{Z}$-grading is not bounded, as a charge must not be.

## Why There Is No Scalar Fock Space Inside Biquaternions

The obstruction has two forms, a trace identity and a dimension count, and they are the same statement seen twice.

**The trace identity.** If $\hat a,\hat a^\dagger$ were elements of $\mathbb{B}$ satisfying the canonical relation $[\tilde a,\tilde a^\dagger]=c\,e_0$, then taking the trace would give

$$
0=\mathrm{Tr}\big([\tilde a,\tilde a^\dagger]\big)
=c\,\mathrm{Tr}(e_0)=2c ,
\qquad\text{hence}\qquad c=0 .
$$

Since the centre of $\mathbb{B}=M_2(\mathbb{C})$ is exactly the complex span of $e_0$, there is no other candidate for the right-hand side of a canonical commutator. No pair in the four-dimensional algebra can therefore realize one bosonic mode. The companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* draws the consequence: $\mathbb{B}$ carries exactly one **fermionic** mode and no bosonic mode at all.

**The dimension count.** Even without the trace argument, the symmetric algebra cannot fit. The $d$-mode truncation to total occupation at most $n_{\max}$ has complex dimension $\binom{d+n_{\max}}{n_{\max}}$. A single bosonic mode truncated at $n_{\max}=1$ needs dimension $2$ and at $n_{\max}=2$ needs dimension $3$, both of which fit inside the four-dimensional algebra; but the full mode needs its infinite ladder, and every truncation with $n_{\max}\ge3$ reaches or passes the algebra's capacity: $n_{\max}=3$ gives dimension $4=\dim_\mathbb{C}\mathbb{B}$, $n_{\max}=4$ gives $5>4$, and the count grows without bound. The algebra's capacity is one fermionic mode because $M_2(\mathbb{C})$ is $\mathrm{Cl}(2)$; the bosonic ladder is the Weyl algebra, which is infinite-dimensional and admits no finite-dimensional representation at all. This is the general statement of which the trace identity is the $\mathbb{B}$-specific form.

### The Fermionic Contrast: Bounded Occupation

The obstruction is specific to bosons, and the contrast is exact. For fermionic modes the Fock space is the **exterior** algebra, the antisymmetric rather than the symmetric tensor projection,

$$
\mathcal{F}_{1/2}=\bigwedge\mathcal{H}_1 ,
\qquad
\dim\bigwedge\mathbb{C}^d=2^d ,
$$

and the anticommutation relations force each occupation number to be $0$ or $1$, so the algebra is finite-dimensional for finitely many modes. One fermionic mode therefore needs a two-dimensional space, spanned by $|0\rangle$ and $|1\rangle$, and the two-dimensional space is available inside $\mathbb{B}=M_2(\mathbb{C})$: the occupied state is the rank-one idempotent $\tfrac12(e_0-ie_3)$ and the vacuum is its complement, both in the informational sector, as the companion Fock-space and informational articles record. The fermionic ladder is thus an object of the algebra; the bosonic one is not. The dimension count displays the difference in one line: one fermionic mode is exactly two-dimensional and the count terminates, $\dim\bigwedge\mathbb{C}^1=2$; one bosonic mode is infinite-dimensional and every truncation is an approximation, the smallest one whose dimension exceeds that of the algebra being $n_{\max}=4$ with $\binom{5}{4}=5$. Bosonic capacity grows without bound in $n_{\max}$; fermionic capacity is bounded by $2^d$ and terminates at full occupancy.

**Verification.** The trace identity was checked on $500$ random pairs of biquaternions represented as $2\times2$ complex matrices: the scalar part of the commutator and its trace both vanished to machine precision, while $\mathrm{Tr}(e_0)=2$. The dimension counts were checked by direct enumeration against the binomial formula, and the fermionic count against $2^d$.

The consequence for the title of the article is plain. The scalar Fock space is the symmetric algebra of a module; it is not a subspace, a subalgebra, or an ideal of $\mathbb{B}$. The only sense in which there is a biquaternionic Fock space is the sense in which the construction begins from a module over the algebra and is written in the algebra's notation; for the scalar field the module is the center's, and the algebra contributes no ladder to it.

## The Informational Sector and the Trace Formula

The framework's Born rule is a trace over the informational sector: for a state $\tilde\rho\in\mathbb{M}_+$ that is positive and of trace one, the expectation of a Hermitian observable $\tilde O\in\mathbb{M}_+$ is

$$
\langle\tilde O\rangle_{\tilde\rho}=\mathrm{Tr}(\tilde\rho\,\tilde O)=2\,\mathrm{Sc}(\tilde\rho\,\tilde O).
$$

For a single **fermionic** mode this formula applies directly to the Fock number operator, which is the idempotent $\tfrac12(e_0-ie_3)$; its expectation is the occupation probability, and the vacuum and occupied projectors are the two pure states. For the **scalar** field the formula applies only to finite-dimensional truncations, because the full number operator acts on an infinite-dimensional space and is not an element of $\mathbb{B}$. On the $n$-level truncation of one mode, the number operator is the diagonal matrix $\mathrm{diag}(0,1,\dots,n)$ represented in the Fock basis, and the trace formula returns the mean occupation of the truncated state. Explicitly, a truncated state is a density matrix $\rho=\sum_{k,l}\rho_{kl}|k\rangle\langle l|$ with $\rho\ge0$ and $\mathrm{tr}\,\rho=1$, and

$$
\langle\hat N\rangle_{\rho}=\mathrm{tr}(\rho\,\hat N)=\sum_{k=0}^{n}k\,\rho_{kk},
$$

so the diagonal of the truncated density matrix is the occupation distribution. The vacuum of the truncation is $\rho_0=|0\rangle\langle0|$, with $\langle\hat N\rangle=0$, and the one-particle state is $\rho_1=|1\rangle\langle1|$, with $\langle\hat N\rangle=1$; the trace formula is exact for these finite matrices and is the only sense in which the Born rule applies to the scalar number operator.

The structural statement is the same one the whole article turns on, seen in the simplest object. The informational sector $\mathbb{M}_+$ is the space of states of the framework's finite-dimensional quantum mechanics; the scalar Fock space is not a subspace of it, and the scalar vacuum is not a density operator in it. The finite-mode truncations are the overlap of the two constructions, and the overlap shrinks to nothing as the truncation is removed. The companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* states the finite-dimensional side; the present article states that the scalar sector lies outside it.

## Coherent States and the Central Phase

Although no oscillator lives in $\mathbb{B}$, the Fock space does carry the standard bosonic structures, and two of them touch the framework's phases. For one mode the **coherent state** is

$$
|\alpha\rangle=e^{-|\alpha|^2/2}\sum_{n\ge0}\frac{\alpha^n}{\sqrt{n!}}\,|n\rangle,
\qquad
\hat a|\alpha\rangle=\alpha|\alpha\rangle,
$$

and the **displacement** $D(\alpha)=\exp(\alpha\hat a^\dagger-\alpha^*\hat a)$ generates it from the vacuum. The central $U(1)$ acts on the Fock space through $\hat U_{\alpha_0}=e^{i\alpha_0\hat Q}$, the same generator as in the companion field article, and since $[\hat Q,\hat a^\dagger]=+\hat a^\dagger$ the coherent state is carried to $|\alpha\rangle\mapsto|e^{i\alpha_0}\alpha\rangle$; the coherent states are thus the orbit of the vacuum under the semidirect product of the displacement and phase groups, and the charge is the generator of the phase. The biquaternion content here is only that the phase is central: it multiplies the state by a central unitary and does not rotate any spinor index. There is no native displacement operator in $\mathbb{B}$, for the same trace reason, and the coherent-state construction is imported with the module.

## What Is Standard and What Is Open

**Standard, and transcribed.** The one-particle space and its Lorentz-invariant inner product; the symmetric algebra and the occupation basis; the creation and annihilation operators and their commutators; the vacuum and its cyclicity; Pauli's exclusion as the fermionic contrast; the number and charge operators and their spectra; coherent states and the displacement operator. None of this is new, and none of it depends on the biquaternion structure beyond the kinematical conventions.

**Open in the biquaternion framework.**

- **The module the Fock space starts from.** Whether the scalar one-particle space, a module for the center rather than for the algebra, is the only module available for a spin-$0$ Fock space, or whether a larger structure carrying the algebra can be attached, is not decided. The spin argument says that no non-central element can act on a spin-$0$ state; it does not say that no larger structure is relevant.
- **The bosonic gap.** The obstruction to a bosonic mode in $\mathbb{B}$ is the finite dimension of the algebra. Whether an infinite-dimensional algebra canonically attached to $\mathbb{B}$ — a completion, a crossed product, or a von Neumann algebra of the field net — carries the scalar ladder in a way that is intrinsic to the framework, rather than imported, is the structural question.
- **The vacuum.** Whether the framework's notion of a minimal idempotent, which gives the fermionic vacuum as an element of $\mathbb{M}_+$, has a scalar analogue in an enlarged structure is open; in $\mathbb{B}$ it does not.
- **The gradings.** Whether the charge grading, which is $\mathbb{Z}$-valued, is the only grading the scalar sector supports, or whether a hidden $\mathbb{Z}/2$ structure exists in an extension, is not settled.
- **Empirical content.** Whether the Fock construction as written yields a prediction distinguishing the framework from standard scalar field theory is open.

## Summary

The scalar Fock space is the symmetric algebra of the one-particle space, $\mathcal{F}=\bigoplus_{n\ge0}\mathrm{Sym}^n\mathcal{H}_1$, with $\mathcal{H}_1=L^2(\mathbb{R}^3,d^3p/(2\pi)^3 2E_{\mathbf{p}})$; its occupation basis, creation and annihilation operators, vacuum and number operator are the standard bosonic ones. The one-particle space is a module for the center: no non-central element acts on a spin-$0$ state without mixing it into another spin sector, so the whole algebra cannot act on it, in contrast with the spinor module that carries the fermionic sectors. The state space is a module for the CCR algebra, not for $\mathbb{B}$.

The scalar Fock space is not an object of $\mathbb{B}$. The obstruction is the trace of a commutator: a canonical relation $[\tilde a,\tilde a^\dagger]=c\,e_0$ inside the algebra would force $2c=\mathrm{Tr}([\tilde a,\tilde a^\dagger])=0$, hence $c=0$, so no bosonic mode exists in the four-dimensional algebra; the companion Fock-space article's fermionic one-mode result is the contrasting case, in which the vacuum is the idempotent $\tfrac12(e_0+ie_3)$. The dimension count says the same thing: the $d$-mode truncation to total occupation $n_{\max}$ has dimension $\binom{d+n_{\max}}{n_{\max}}$, which for a single mode reaches $4$ at $n_{\max}=3$ and exceeds it from $n_{\max}=4$ onward, and the symmetric algebra is infinite-dimensional.

The state space carries two gradings, an $\mathbb{N}$-grading by total number and, for the complex field, a $\mathbb{Z}$-grading by charge whose sectors are the superselection sectors of the $U(1)$; there is no $\mathbb{Z}/2$ parity grading, because the bosonic modes commute and no graded-commutativity is imposed. The informational sector's trace formula applies to finite truncations only; the scalar vacuum is not a density operator in $\mathbb{M}_+$, and the coherent states are the imported bosonic construction on the module the algebra supplies.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Central scalar imaginary |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$ | Center; its scalars are the only elements acting on the scalar one-particle space |
| $\mathcal{H}_1=L^2(\mathbb{R}^3,\frac{d^3p}{(2\pi)^3 2E_{\mathbf{p}}})$ | Scalar one-particle space |
| $\mathcal{F}=\bigoplus_n\mathrm{Sym}^n\mathcal{H}_1$ | Scalar Fock space (symmetric algebra) |
| $\hat a_{\mathbf{p}},\hat a^\dagger_{\mathbf{p}},\hat b_{\mathbf{p}},\hat b^\dagger_{\mathbf{p}}$ | Mode operators (particle and antiparticle) |
| $\vert n_{\mathbf{p}_1},n_{\mathbf{p}_2},\dots\rangle$ | Occupation basis; $n_i\in\mathbb{N}$ |
| $\hat N=\int\frac{d^3p}{(2\pi)^3}(\hat a^\dagger\hat a+\hat b^\dagger\hat b)$ | Number operator ($\mathbb{N}$-grading) |
| $\hat Q=\int\frac{d^3p}{(2\pi)^3}(\hat a^\dagger\hat a-\hat b^\dagger\hat b)$ | Charge operator ($\mathbb{Z}$-grading) |
| $\mathrm{Sym}^n$, $\binom{d+n_{\max}}{n_{\max}}$ | Symmetric powers and their dimensions |
| $\mathrm{Tr}([\tilde A,\tilde B])=0$, $\mathrm{Tr}(e_0)=2$ | Trace identity; no bosonic mode in $\mathbb{B}$ |
| $\tfrac12(e_0+ie_3)$, $\tfrac12(e_0-ie_3)$ | Fermionic vacuum and occupied projectors (contrast case) |
| $\mathrm{Tr}(\tilde\rho\tilde O)=2\,\mathrm{Sc}(\tilde\rho\tilde O)$ | Trace formula (Born rule), for finite truncations |
| $D(\alpha)=\exp(\alpha\hat a^\dagger-\alpha^*\hat a)$, $\vert\alpha\rangle$ | Displacement operator and coherent state |
| $\hat U_\alpha=e^{i\alpha\hat Q}$, $\vert\alpha\rangle\mapsto\vert e^{+i\alpha}\alpha\rangle$ | Central $U(1)$ phase |

## Further Reading

- V. A. Fock, "Konfigurationsraum und zweite Quantelung," *Zeitschrift für Physik* **75** (1932) 622–647, for the original occupation-number construction of the many-particle space.
- P. Jordan and E. Wigner, "Über das Paulische Äquivalenzverbot," *Zeitschrift für Physik* **47** (1928) 631–651, for the creation and annihilation operators and the exclusion rule.
- F. A. Berezin, *The Method of Second Quantization* (Academic Press, 1966), for the exterior and symmetric algebras as the fermionic and bosonic Fock spaces.
- O. Bratteli and D. W. Robinson, *Operator Algebras and Quantum Statistical Mechanics* 2 (Springer, 1997), for the CCR algebra, its representations, and the Fock representation.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), and M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the scalar Fock space and the number and charge operators.
- R. F. Streater and A. S. Wightman, *PCT, Spin and Statistics, and All That* (Benjamin, 1964), for the reconstruction of the one-particle space from the vacuum correlations.
- J. R. Klauder and B.-S. Skagerstam, *Coherent States: Applications in Physics and Mathematical Physics* (World Scientific, 1985), for the displacement operator, the coherent states, and their group-theoretic orbit structure.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Clifford algebra $\mathrm{Cl}(2)\cong M_2(\mathbb{C})$ and the finite-dimensional modules of $\mathbb{B}$.
