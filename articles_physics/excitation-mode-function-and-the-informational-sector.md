# __Excitation, Mode Function, and the Informational Sector__

## Introduction

In the second quantization of a free field, two different objects are routinely called "the state", and the biquaternion framework places them in different sectors. The first is a **mode function**: one definite solution of the free wave equation, carrying a definite momentum and a definite spin or polarization label,

$$
u^{(r)}(\mathbf p)\,e^{-ip\cdot x},\qquad v^{(r)}(\mathbf p)\,e^{+ip\cdot x},\qquad r=1,2 .
$$

The second is an **excitation**: one quantum occupying such a mode, the state $\hat a_r^\dagger(\mathbf p)|0\rangle$, or a superposition of occupations. The mode function says *which* mode; the excitation says *how many* quanta the mode contains. The subject of this article is where each of the two lives in the biquaternion algebra $\mathbb{B}$, and in particular whether the informational sector $\mathbb{M}_+$ is their natural home.

The answer has two parts, and the parts should be separated before any algebra is written.

1. **The occupation state is in $\mathbb{M}_+$, and this can be checked.** For one fermionic mode the occupation-number operator $\tilde N=\hat a^\dagger\hat a$ and the density matrix $\tilde\rho$ of the mode are Hermitian elements of $\mathbb{B}$, and they lie in $\mathbb{M}_+$ exactly. This is the assertion that "the informational sector carries the state", stated in the only form in which it is true.

2. **The mode function is not in $\mathbb{M}_+$.** A mode function is a definite solution: one element of the space of solutions of the free equation. That solution space is a module over $\mathbb{B}$ (the spinor module, for the Dirac field) or, for the Maxwell potential and its polarizations, a subspace of the material sector $\mathbb{M}_-$. The only spinor of the Dirac solution space that is Hermitian is the projector itself, a one-dimensional ray.

The distinction is not a technicality; it is the content of the words *definite solution* and *occupation*. A definite solution fixes a point of the one-particle solution space and says nothing about how many quanta are present; the occupation is that number, and it is the occupation data, not the solution, that the informational sector carries. The same mode function can be occupied zero times, once, or in a superposition, and it serves all cases unchanged. A framework that assigned the mode function and the occupation to the same sector would be unable to express the difference between "this solution" and "one quantum in this solution".

Because "the informational sector carries the state" is precisely the kind of claim that gets asserted and then never checked, the article states separately what is asserted to be in $\mathbb{M}_+$ and verifies each assertion by recomputation. It also counts the degrees of freedom on the two sides. That count closes for exactly one fermionic mode and fails otherwise: two fermionic modes require a sixteen-dimensional operator space and a bosonic mode requires an infinite-dimensional one, against the four real dimensions of $\mathbb{M}_+$. The mismatch is recorded as a finding, not smoothed over.

**Conventions.** The notation is inherited unchanged from the read list. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with quaternion basis $e_0=1,e_1,e_2,e_3$ satisfying $e_k^2=-e_0$ and $e_je_k=\epsilon_{jkl}e_l$ for $j\neq k$, and central scalar imaginary $i$ with $i^2=-1$. The material and informational sectors are

$$
\mathbb{M}_-=\{\tilde Q:\tilde Q^\dagger=-\tilde Q\}=\mathrm{span}_\mathbb{R}\{ie_0,e_1,e_2,e_3\},
\qquad
\mathbb{M}_+=\{\tilde Q:\tilde Q^\dagger=\tilde Q\}=\mathrm{span}_\mathbb{R}\{e_0,ie_1,ie_2,ie_3\},
$$

with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ and $i\mathbb{M}_\pm=\mathbb{M}_\mp$. The isomorphism with $M_2(\mathbb{C})$ is $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$, hence $\Phi(ie_k)=\sigma_k$, and the trace is normalized by $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$, so that $\mathrm{Tr}(e_0)=2$. The **spinor module** is the minimal left ideal $\mathbb{B}p$, with

$$
p=\tfrac12(e_0+ie_3),\qquad q=\tfrac12(e_0-ie_3),\qquad
x=\tfrac12(ie_1-e_2),\qquad y=\tfrac12(ie_1+e_2),
$$

and basis $\{p,y\}$ for $\mathbb{B}p$; the matrix-unit relations $xy=p$, $yx=q$, $x^2=y^2=0$ hold. The field expansion, the mode operators, and the Fock construction are those of the companion quantization and Fock-space articles and are not rederived here.

## The Mode Function Is a Definite Solution

The Dirac field of the companion articles expands on the spinor module as

$$
\hat\psi(x)=\int\!\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_{r=1}^{2}
\Big[\hat a_r(\mathbf p)\,u^{(r)}(\mathbf p)\,e^{-ip\cdot x}
+\hat b_r^\dagger(\mathbf p)\,v^{(r)}(\mathbf p)\,e^{+ip\cdot x}\Big],
$$

with the mode operators and spinors of the parent article. Each term of the expansion is a **mode function**: the positive-frequency mode functions are $u^{(r)}(\mathbf p)e^{-ip\cdot x}$ and the negative-frequency ones $v^{(r)}(\mathbf p)e^{+ip\cdot x}$. Three labels specify a mode function completely — the momentum $\mathbf p$, the spin index $r$, and the sign of the frequency — and the mode function is a solution of the free equation with those labels.

The word *definite* in "definite solution" means that the mode function is a single element of the solution space, not a general superposition. The general solution is the integral over all modes; a mode function is one basis vector of that integral. In the biquaternion reading of the parent article, a mode function is the module representative of a biquaternion plane wave $\tilde\Psi_0\exp(\tilde k\tilde X)$: the four-wavevector $\tilde k=i\omega/c\,e_0+\mathbf k$ is an element of the material sector $\mathbb{M}_-$ (it appears in the table of four-vectors of *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*), and the amplitude $\tilde\Psi_0$ is a spinor, i.e. an element of the module $\mathbb{B}p$. Both pieces are therefore objects attached to the material sector and to the module. Neither is an element of the Hermitian subspace $\mathbb{M}_+$.

The Maxwell case is structurally the same and algebraically simpler. The one-particle space at fixed momentum is the space of transverse polarization amplitudes, two real dimensions, and the companion photon article identifies the polarization directions with the plane in $\mathrm{Vect}(\mathbb{M}_-)$ orthogonal to the propagation direction $\hat{\mathbf k}$. The mode function of the potential, $\varepsilon_\mu(\mathbf k)e^{-ik\cdot x}$, is a four-vector with a definite **linear** polarization; its polarization vector is then a direction in $\mathbb{M}_-$. Again the definite solution lives on the material side. The photon article states the structural reason: the polarization directions are real spatial vectors and sit in the material sector, while the helicity operator is represented by the Hermitian element $i\hat{\mathbf k}$ of $\mathbb{M}_+$ and is an *observable* of the mode, not the mode function itself.

It is worth stating plainly what a mode function does not carry. It carries no occupation number. A single mode function is consistent with the vacuum, with one quantum, with two quanta (for a boson), and with any superposition of these; the expansion coefficient $\hat a_r(\mathbf p)$ is precisely the datum that the mode function omits and the operator supplies. The mode function is the *label*; the occupation is the *coordinate* attached to the label. The two must be assigned to sectors separately, and the rest of the article does that.

## The Excitation Is an Occupation

An excitation is an occupation. Acting on the vacuum with a creation operator produces the state with one quantum in the chosen mode,

$$
|1_{\mathbf p,r}\rangle=\hat a_r^\dagger(\mathbf p)|0\rangle,
$$

and the occupation-number operator

$$
\hat N=\sum_{r}\int\!\frac{d^3p}{(2\pi)^3}\ \hat a_r^\dagger(\mathbf p)\,\hat a_r(\mathbf p)
$$

counts the quanta, with $[\hat N,\hat a_r^\dagger]=+\hat a_r^\dagger$ and $[\hat N,\hat a_r]=-\hat a_r$. The excitation is not a solution of the wave equation and is not a mode function; it is a state in the many-particle space, and its defining datum is the integer eigenvalue of $\hat N$.

For a single fermionic mode this can be reduced to an object of the finite-dimensional algebra, because $\mathbb{B}\cong M_2(\mathbb{C})$ is exactly the operator algebra of one fermionic mode. The parent Fock-space article exhibits the ladder operators in the algebra as the matrix units

$$
\tilde a=x=\tfrac12(ie_1-e_2),\qquad
\tilde a^\dagger=y=\tfrac12(ie_1+e_2),
$$

which satisfy $\{\tilde a,\tilde a^\dagger\}=e_0$ and $\tilde a^2=(\tilde a^\dagger)^2=0$. The occupation-number operator of the single mode is then

$$
\tilde N=\tilde a^\dagger\tilde a=yx=q=\tfrac12(e_0-ie_3),
$$

and the vacuum projector is its complement

$$
e_0-\tilde N=\tilde a\,\tilde a^\dagger=xy=p=\tfrac12(e_0+ie_3).
$$

These are the one-mode operators of the Fock-space and harmonic-oscillator articles, written in the module realization of this article.

Two remarks about the operators are needed before the sector question is posed. First, the **excitation operator is not Hermitian**: $\tilde a^\dagger=x^\dagger=y\neq\tilde a$ and $\tilde a^\dagger\neq-\tilde a$, since $\tilde a$ has the Hermitian part $\tfrac12 ie_1$ and the anti-Hermitian part $-\tfrac12 e_2$, so it lies in neither sector. Creation and annihilation operators are not observables, and no sector claim about them is being made. What lies in a sector is the number operator $\tilde N$, which is Hermitian, and the state, which is Hermitian and positive. Second, the number operator is an **idempotent**: $\tilde N^2=\tilde N$ and $\tilde N^\dagger=\tilde N$. It is a projector, and it is the operator form of the occupation "one". The pair $\{e_0-\tilde N,\tilde N\}$ is the pair of orthogonal idempotents $p,q$ whose Peirce decomposition splits the spinor module into its two components.

## Three Objects, Three Homes

The phrase "an excitation and its state" packs three different objects together, and the sector question is only answerable if they are separated. The separation is the following.

| Object | Definition | Algebraic home |
|---|---|---|
| Mode function | A definite solution $u^{(r)}(\mathbf p)e^{-ip\cdot x}$ | Spinor module $\mathbb{B}p$ (Dirac); $\mathrm{Vect}(\mathbb{M}_-)$ (Maxwell polarization) |
| Excitation operator | $\tilde a^\dagger$ (or $\hat a_r^\dagger(\mathbf p)$) | Neither $\mathbb{M}_+$ nor $\mathbb{M}_-$; not Hermitian |
| Occupation state | $\vert n\rangle$, or the density matrix $\tilde\rho$ | State vector: the module; density matrix and $\tilde N$: $\mathbb{M}_+$ (one fermionic mode) |

The third row is the assertion that needs care. The **state vector** $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$ of one mode is an element of the two-dimensional occupation Hilbert space, which is the fundamental module $S\cong\mathbb{C}^2$, not the algebra; it is not an element of $\mathbb{M}_+$. It is the **density matrix**

$$
\tilde\rho=\tfrac12\big(e_0+i\mathbf r\big),\qquad \mathbf r\in\mathbb{R}^3,\quad |\mathbf r|\leq 1,
$$

of the mode, and the occupation-number observable $\tilde N$, that are elements of the algebra, and they are elements of $\mathbb{M}_+$. So the precise reading of "the informational sector carries the state" is: it carries the *state as a density matrix*, not the *state as a vector*, and it carries the observables. This is the distinction the ontology companion draws when it says that the state is an element of $\mathbb{M}_+$: the object meant there is the density matrix, and the same article records that the algebra does not decide the interpretation of that element.

## What Is Asserted to Lie in $\mathbb{M}_+$, and Its Verification

The assertions to be checked are now explicit. Each is verified by recomputation from the definitions, on randomly generated elements as well as on the cases that suggested them.

**A1. The occupation-number operator is in $\mathbb{M}_+$.** With $\tilde N=\tfrac12(e_0-ie_3)$, compute $\tilde N^\dagger=\tfrac12(e_0^\dagger+(-ie_3)^\dagger)=\tfrac12(e_0-ie_3)=\tilde N$, so $\tilde N\in\mathbb{M}_+$. Its square is $\tilde N^2=\tfrac14(e_0-ie_3)^2=\tfrac14(e_0^2-2ie_3+(ie_3)^2)=\tfrac14(e_0-2ie_3+e_0)=\tfrac12(e_0-ie_3)=\tilde N$, using $(ie_3)^2=e_0$. So the number operator is a Hermitian idempotent — a projector onto the occupied state — and it lies in $\mathbb{M}_+$. The same two computations with $\mu$ any unit pure real quaternion, $\tilde N_\mu=\tfrac12(e_0-i\mu)$, give $\tilde N_\mu^\dagger=\tilde N_\mu$ and $\tilde N_\mu^2=\tilde N_\mu$; this was checked on twenty random unit $\mu$, not only on $\mu=e_3$.

**A2. The vacuum projector is in $\mathbb{M}_+$.** The complement $e_0-\tilde N=\tfrac12(e_0+ie_3)=p$ is Hermitian and idempotent by the same computation, so $p\in\mathbb{M}_+$. More generally $\tfrac12(e_0+i\mu)$ is Hermitian, idempotent, and of trace one for every unit pure quaternion $\mu$. These are the pure-state projectors of *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, and the single-mode occupation basis is exactly this pair.

**A3. The density matrix of the mode is in $\mathbb{M}_+$.** For $\tilde\rho=\tfrac12(e_0+i\mathbf r)$ with $\mathbf r\in\mathbb{R}^3$, the scalar part is real and the vector part is purely imaginary, so $\tilde\rho\in\mathbb{M}_+$ by the definition of the sector. Direct computation gives
$$
\tilde\rho^2-\tilde\rho=\tfrac14\big(|\mathbf r|^2-1\big)e_0,\qquad
\mathrm{Tr}(\tilde\rho)=1,\qquad
\tilde\rho^\dagger=\tilde\rho,
$$
and the eigenvalues are $\lambda_\pm=\tfrac12(1\pm|\mathbf r|)$, so positivity is exactly $|\mathbf r|\leq1$. These identities were checked on thirty random $\mathbf r$, including the interior point $\mathbf r=(0.6,-0.2,0.3)$ and the boundary point $\mathbf r=(1,0,0)$, not only on $\mathbf r=0$. The set of such $\tilde\rho$ is the Bloch ball, a three-dimensional subset of the four-dimensional real space $\mathbb{M}_+$.

**A4. The ladder operators are not in either sector.** For $\tilde a=\tfrac12(ie_1-e_2)$ one has $\tilde a^\dagger=\tfrac12(ie_1+e_2)=\tilde a^\dagger\neq\tilde a$, and $\tilde a^\dagger\neq-\tilde a$; splitting into Hermitian and anti-Hermitian parts,
$$
\tilde a=\tfrac12 ie_1+\big(-\tfrac12 e_2\big),\qquad
\tilde a^\dagger=\tfrac12 ie_1+\tfrac12 e_2,
$$
with the first term of each in $\mathbb{M}_+$ and the second in $\mathbb{M}_-$. So the excitation operator is a sum of one element of each sector and is an element of neither. This is not a defect; it is the statement that raising and lowering are not observables.

**A5. The canonical relation holds once, and in the fermionic form.** The matrix-unit relations give $\{\tilde a,\tilde a^\dagger\}=xy+yx=p+q=e_0$, $\tilde a^2=x^2=0$, $(\tilde a^\dagger)^2=y^2=0$, and $\tilde N=\tilde a^\dagger\tilde a=yx=q$. All were recomputed in the quaternion basis. The bosonic relation $[\tilde a,\tilde a^\dagger]=e_0$ cannot hold for any pair in $\mathbb{B}$, because the trace of a commutator vanishes while $\mathrm{Tr}(e_0)=2$; this is the obstruction recorded in the Fock-space and photon articles and is not reopened here.

Two points about the reach of A1–A3 belong immediately after them. First, the assertions are about **one mode**. Both $x,y$ and the Peirce idempotents are attached to a single pair of orthogonal idempotents and to a single mode; there is no second pair commuting with the first in the four-dimensional algebra, hence no second fermionic mode. Second, the assertions are about the **density matrix** and the **number operator**, not about the state vector. The state vector is in the module, and the module is not $\mathbb{M}_+$: the two are different subspaces of $\mathbb{B}$ that meet in a ray. The next section makes that intersection precise.

## In What Sense $\mathbb{M}_+$ Is a Hilbert Space

The phrase "the state space is $\mathbb{M}_+$" invites the reading that $\mathbb{M}_+$ is a Hilbert space of state vectors. That reading is false, and the qualifications matter.

- **$\mathbb{M}_+$ is not a complex vector space.** Multiplication by $i$ exchanges the sectors, $i\mathbb{M}_+=\mathbb{M}_-$, so $\mathbb{M}_+$ has no complex structure inherited from $\mathbb{B}$. It is a real vector space of dimension four.
- **$\mathbb{M}_+$ is not closed under multiplication.** $(ie_1)(ie_2)=-e_3\in\mathbb{M}_-$ is the standard counterexample. The product of two Hermitian elements is Hermitian only if they commute; the symmetrized product $\tfrac12(\tilde P\tilde H+\tilde H\tilde P)$ does remain in $\mathbb{M}_+$, which is the sense in which $\mathbb{M}_+$ is a Jordan (not associative) algebra.
- **$\mathbb{M}_+$ is a real Hilbert space under the trace pairing.** On the basis $\{e_0,ie_1,ie_2,ie_3\}$ one has $\mathrm{Tr}(ie_j\,ie_k)=2\delta_{jk}$ and $\mathrm{Tr}(e_0\,ie_k)=0$, so the pairing $\langle\tilde P,\tilde H\rangle=\tfrac12\mathrm{Tr}(\tilde P\tilde H)=\mathrm{Sc}(\tilde P\tilde H)$ is the standard Euclidean inner product in the four real coordinates $(p_0,p_1,p_2,p_3)$, hence positive definite. In this sense $\mathbb{M}_+$ is a four-dimensional real Hilbert space, and $\Phi$ identifies it with the Hermitian $2\times2$ matrices with the Hilbert–Schmidt product.
- **$\mathbb{M}_+$ is not a Hilbert space under the norm form.** The norm form $N(\tilde Q)=\tilde Q\bar{\tilde Q}$ restricts to $N(h_0e_0+i\mathbf h)=h_0^2-|\mathbf h|^2$, of signature $(1,3)$; it is indefinite, and it vanishes on the cone $h_0^2=|\mathbf h|^2$. The positivity condition on states is the norm-form (light-cone) condition, not the trace-pairing one, so the two natural forms on $\mathbb{M}_+$ do different work.

The correct statement is therefore: $\mathbb{M}_+$ is a four-dimensional **real** Hilbert space under the Hilbert–Schmidt (trace) pairing, whose elements are the Hermitian operators on the two-dimensional module; the density matrices of one fermionic mode form a three-dimensional subset of it; and it is not the module itself, which is a complex two-dimensional space of state vectors. The qualification "in the sense of the trace pairing" is not optional, because under the other natural form the space is not even positive definite.

## Counting the Degrees of Freedom

The sector claim becomes quantitative when the dimensions are counted on the two sides. The counting unit is one mode: a fixed momentum together with a fixed spin or polarization label.

On the **excitation** side, the occupation space of one fermionic mode is two-dimensional over $\mathbb{C}$ (the states $|0\rangle$ and $|1\rangle$), hence four-dimensional over $\mathbb{R}$. The operators on that space are the $2\times2$ complex matrices, of which the Hermitian ones form $\mathbb{M}_+$, of four real dimensions; the density matrices are the positive trace-one elements, a three-dimensional ball. For one bosonic mode the occupation space is instead the whole of $\ell^2(\mathbb{N})$, infinite-dimensional, and the operator space is infinite-dimensional as well.

On the **mode-function** side, the space of positive-frequency solutions of the Dirac equation at fixed momentum is the two-dimensional complex spinor module, again four real dimensions; it is the module $\mathbb{B}p$, whose intersection with $\mathbb{M}_+$ is the single real line $\mathbb{R}p$, as computed below. A single definite mode function is one vector of this space, a complex ray.

The counts are summarised in the table. Dimensions are over $\mathbb{R}$ except where marked.

| Object | Dimension | Home |
|---|---|---|
| $\mathbb{M}_+$ (Hermitian elements) | $4$ | the sector |
| $\mathbb{M}_-$ (anti-Hermitian elements) | $4$ | the sector |
| Spinor module $\mathbb{B}p$ (one-particle solutions at fixed $\mathbf p$, Dirac) | $4$ | module |
| $\mathbb{B}p\cap\mathbb{M}_+$ | $1$ (the ray $\mathbb{R}p$) | overlap |
| Occupation space, one fermionic mode | $4$ | module $\cong\mathbb{C}^2$ |
| Occupation space, one bosonic mode | $\infty$ | $\ell^2(\mathbb{N})$ |
| Hermitian operators on one fermionic mode | $4$ | $\mathbb{M}_+$ |
| Density matrices of one fermionic mode | $3$ | Bloch ball $\subset\mathbb{M}_+$ |
| Occupation space, two fermionic modes | $8$ | $\mathbb{C}^4$ |
| Hermitian operators on two fermionic modes | $16$ | $\mathrm{Herm}(4,\mathbb{C})\not\subset\mathbb{B}$ |

The count **closes for exactly one fermionic mode**: the operator space of one fermionic mode has four real dimensions and is $\mathbb{M}_+$ under the fixed isomorphism $\Phi$ — $\Phi(\mathbb{M}_+)$ is exactly the Hermitian $2\times2$ matrices — and the density matrices form a three-dimensional subset. Every other case fails, and the failure is structural rather than an inconvenience.

- **Two fermionic modes.** The occupation space is $\mathbb{C}^4$, real dimension eight, and the Hermitian operators on it form $\mathrm{Herm}(4,\mathbb{C})$, of real dimension sixteen. The four-dimensional $\mathbb{M}_+$ cannot contain this operator space, and $\mathbb{B}\cong M_2(\mathbb{C})$ has only four complex dimensions, so it contains no copy of a sixteen-real-dimensional operator space either. The two-mode state is not in the sector.
- **One bosonic mode.** The occupation space is infinite-dimensional, so its operator space is infinite-dimensional; no finite-dimensional sector can carry it. This is the state-side face of the Fock-space article's finding that no bosonic ladder exists in $\mathbb{B}$: not only is there no creation operator, there is no room for the states one would create.
- **A field.** A global state of the field is a density matrix on Fock space, with infinitely many modes and their correlations. It is not an element of $\mathbb{B}$ and hence not of $\mathbb{M}_+$; only a single-mode factor can be represented there.

The mismatch is a real finding and is stated as one. It does not contradict the sector hypothesis; it bounds it. The informational sector $\mathbb{M}_+$ is the home of the state of **one fermionic mode**, exactly, and the framework's own finite-dimensional algebra does not extend that home to a second mode or to a boson. Whether the single-mode fit is a structural selection or the smallest dimension coincidence, the Fock-space article's question, is not settled by the count; the count only shows that if it is a coincidence, it is the same coincidence seen from the state side.

## Where the Mode Function Actually Lives

The counting is only half the structural statement; the other half is the exact location of the definite solution, and it is not $\mathbb{M}_+$.

The spinor module is realized inside the algebra as the minimal left ideal $\mathbb{B}p$, with $p=\tfrac12(e_0+ie_3)$ and basis $\{p,y\}$, $y=\tfrac12(ie_1+e_2)$. A general spinor is therefore $\tilde\psi=\psi_1p+\psi_2y$ with $\psi_1,\psi_2\in\mathbb{C}$, a four-real-dimensional space. Its Hermitian conjugate is $\tilde\psi^\dagger=\overline{\psi_1}\,p+\overline{\psi_2}\,x$, using $y^\dagger=x$ and $p^\dagger=p$. The condition $\tilde\psi^\dagger=\tilde\psi$ forces, comparing coefficients in the independent directions $p,x,y$,

$$
\psi_2=0\qquad\text{and}\qquad \psi_1=\overline{\psi_1}\ \ (\psi_1\in\mathbb{R}).
$$

So the intersection of the definite-solution space with the informational sector is

$$
\mathbb{B}p\cap\mathbb{M}_+=\mathbb{R}\,p,
$$

a single real line, spanned by the projector itself. This was checked directly on real, imaginary, and generic complex $(\psi_1,\psi_2)$: the only Hermitian spinors are the real multiples of $p$. The upshot is sharp: away from the projector ray, a mode function is not an element of $\mathbb{M}_+$, and the representable definite solution that is Hermitian is exactly the pure state whose density matrix is $p$.

The Maxwell case is the same conclusion with a different home. The polarization vector of a **linearly polarized** mode function is a real spatial direction in $\mathrm{Vect}(\mathbb{M}_-)$ orthogonal to $\hat{\mathbf k}$, so it is in the material sector; the helicity observable, by contrast, is the Hermitian element $i\hat{\mathbf k}\in\mathbb{M}_+$. Once more the definite solution is material and the operator is informational. The division is consistent across the two fields: the *solution* is on the configuration side (the module, or $\mathbb{M}_-$ for vectors), and the *operator* is on the Hermitian side.

There is a reading of the mode function that belongs here as a reading and not as a result. Within the two-level truncation of one mode, the occupation axis and the phase axis are not independent structures: the states with definite occupation are the poles of the Bloch ball, where the density matrix is the projector $p$ or $q$, and a definite-phase superposition sits on the equator, where the density matrix has a non-zero vector part — precisely the part that the partition-function article shows the trace discards. On that reading, the mode function's definite phase and the excitation's definite number are two complementary axes of the same qubit in $\mathbb{M}_+$. The reading has two caveats and is offered subject to them: it holds only in the two-level truncation, which the count above shows is the only truncation the algebra supports, and for a fermionic mode the "definite-phase solution" is a Grassmann-valued coherent state, so the identification of a classical definite solution with an ordinary quantum state is not literal. Whether the phase of a definite solution is exactly the coherent (equatorial) axis of the single-mode qubit is left open.

## Summary

An excitation and a mode function are different objects and the biquaternion framework gives them different homes. A mode function is a definite solution of the free equation, one basis vector of the one-particle solution space; for the Dirac field that space is the spinor module $\mathbb{B}p\cong\mathbb{C}^2$, and for the Maxwell potential the polarization is a direction of the material sector $\mathbb{M}_-$. An excitation is an occupation: the state $|1_{\mathbf p,r}\rangle$ and the number operator $\hat N$. Its occupation-number operator $\tilde N=\tfrac12(e_0-i\mu)$ and its density matrix $\tilde\rho=\tfrac12(e_0+i\mathbf r)$ are Hermitian elements of $\mathbb{B}$, and they lie in $\mathbb{M}_+$ exactly; the excitation operator $\tilde a^\dagger=\tfrac12(ie_1+e_2)$, which is not Hermitian, lies in neither sector. "The informational sector carries the state" is therefore true of the state as a density matrix and of the observables, and false of the state vector, which lives in the module.

The mode function is not in $\mathbb{M}_+$: the solution space meets the sector in the single real ray $\mathbb{B}p\cap\mathbb{M}_+=\mathbb{R}p$, so away from the projector a definite solution is not Hermitian. The definite solution is on the configuration side and the occupation is on the informational side, which is exactly the division the words express.

$\mathbb{M}_+$ is a four-dimensional real Hilbert space under the trace pairing and not a complex vector space, not an associative subalgebra, and not a Hilbert space under the norm form, which is indefinite of signature $(1,3)$. The degrees of freedom close for exactly one fermionic mode — four real dimensions of operators, three of states — and fail beyond it: two fermionic modes require sixteen dimensions and a bosonic mode infinitely many. The sector is the home of the state of one fermionic mode, precisely and verifiably, and the mismatch for more is left visible as the bound on that home rather than absorbed into the prose.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_je_k=\epsilon_{jkl}e_l$ $(j\neq k)$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-$ | Anti-Hermitian (material) sector, $\mathrm{span}_\mathbb{R}\{ie_0,e_1,e_2,e_3\}$ |
| $\mathbb{M}_+$ | Hermitian (informational) sector, $\mathrm{span}_\mathbb{R}\{e_0,ie_1,ie_2,ie_3\}$ |
| $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$ | Isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ |
| $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ | Trace formula; $\mathrm{Tr}(e_0)=2$ |
| $p=\tfrac12(e_0+ie_3)$, $q=\tfrac12(e_0-ie_3)$ | Orthogonal idempotents, Peirce projectors |
| $x=\tfrac12(ie_1-e_2)$, $y=\tfrac12(ie_1+e_2)$ | Matrix units, $xy=p$, $yx=q$, $x^2=y^2=0$ |
| $\mathbb{B}p=\{ \psi_1p+\psi_2y\}$ | Spinor module (one-particle solutions), $\mathbb{B}p\cap\mathbb{M}_+=\mathbb{R}p$ |
| $u^{(r)}(\mathbf p)e^{-ip\cdot x}$, $v^{(r)}(\mathbf p)e^{+ip\cdot x}$ | Mode functions (positive/negative frequency) |
| $\hat a_r^\dagger(\mathbf p)$, $\hat a_r(\mathbf p)$ | Excitation (creation) and annihilation operators |
| $\tilde a=x$, $\tilde a^\dagger=y$ | One-mode ladder operators in $\mathbb{B}$ |
| $\tilde N=\tilde a^\dagger\tilde a=\tfrac12(e_0-i\mu)$ | Occupation-number operator (idempotent, in $\mathbb{M}_+$) |
| $\tilde\rho=\tfrac12(e_0+i\mathbf r)$, $|\mathbf r|\leq1$ | Density matrix of one mode (Bloch ball $\subset\mathbb{M}_+$) |
| $N(\tilde Q)=\tilde Q\bar{\tilde Q}$ | Norm form; signature $(1,3)$ on $\mathbb{M}_+$ |
| $\mathrm{Sc}(\tilde P\tilde H)$ | Hilbert–Schmidt pairing on $\mathbb{M}_+$ (positive definite) |

## Further Reading

- *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, for the one-mode ladder operators, the capacity bound, and the Fock space that the algebra does not contain.
- *Canonical Quantization of the Biquaternion Dirac Field*, for the field expansion, the mode functions $u^{(r)},v^{(r)}$, and the spinor-module setting.
- *Canonical Quantization of the Biquaternion Maxwell Field*, for the Gupta–Bleuler mode algebra and the physical-state condition.
- *The Photon in Biquaternionic Form*, for the identification of the polarization directions with the material sector and the helicity observable in $\mathbb{M}_+$.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the idempotents, the trace formula, and the operator-algebra reading of the sector.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the four-vectors, including the four-wavevector that labels a mode function.
- *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, for the realization of the module as the minimal left ideal $\mathbb{B}p$ and the matrix units $x,y$.
- *The Ontology of the Quantum State under the Biquaternion Framework*, for the state as an element of $\mathbb{M}_+$ and the limits of that reading.
- *The Partition Function in Biquaternionic Form*, for the thermal state as an element of $\mathbb{M}_+$ and the coherence that the trace discards.
- *The Harmonic Oscillator in Biquaternionic Form*, for the two-level truncation and the failure of the bosonic canonical relation.
