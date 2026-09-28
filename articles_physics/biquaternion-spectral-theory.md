# __Biquaternion Spectral Theory__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is unital and associative but neither commutative nor a division algebra, and both failures complicate the notion of a spectrum. Several inequivalent definitions of "spectrum" are in use, and the main source of error in the subject is the silent switching between them. We state, for every definition, exactly which set it defines; and "spectrum" without qualification always means the spectrum of the biquaternion defined by invertibility, that is, its set of eigenvalues in $\mathbb{C}$.

Physically this is the algebra of measurement. The Hermitian elements are the observables, their spectra are the values a measurement can return, the spectral theorem is the statement that an observable has an orthonormal eigenbasis, and the functional calculus is how one forms a function of an observable. The article is therefore the algebraic backbone of the quantum-mechanical articles, and it is written so that the reader can always tell which spectrum — complex, left, right, or S — a statement uses.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$, central scalar imaginary $i$, and general element $\tilde{Q}=\sum_\mu Q_\mu e_\mu$, written $\tilde{Q}=Q_0e_0+\mathbf{Q}$. The two polar forms, the four conjugations and the six subspaces are those of *Biquaternion Algebra*; the norm and the invertibility criterion are *Biquaternion Norm and Invertibility*; the zero divisors are *Biquaternion Zero Divisors*; the exponential and the logarithm are *Biquaternion Elementary Functions*. The Hermitian idempotents used in the spectral theorem are classified in *Biquaternion Idempotents and Projections*.

## The Spectrum of an Element of an Algebra

Let $A$ be a unital associative algebra over a field $F$, with unit $1_A$.

**Definition 1.1.** The **spectrum** of $a \in A$ is $\sigma_A(a) = \{\lambda \in F : a - \lambda 1_A \text{ is not invertible in } A\}$. It is also called the **point spectrum** when $A$ is a finite-dimensional algebra of operators. The definition is intrinsic: it uses only invertibility.

**Proposition 1.2.** If $A$ is a finite-dimensional unital algebra over $\mathbb{C}$ with $A \neq 0$, and $L_a(x) = ax$ is left multiplication, then $\sigma_A(a)$ is exactly the set of eigenvalues of $L_a$, and is nonempty.

**Proof.** $b$ is invertible iff $L_b$ is bijective. The characteristic polynomial of $L_a$ has a root $\mu \in \mathbb{C}$, and $L_a - \mu\,\mathrm{id} = L_{a-\mu 1_A}$ is singular, so $\mu \in \sigma_A(a)$; conversely $\lambda \in \sigma_A(a)$ makes $L_{a-\lambda 1_A}$ non-bijective, hence $\lambda$ an eigenvalue.

**Corollary 1.3.** For $A = M_n(\mathbb{C})$, $\sigma(M) = \{\lambda \in \mathbb{C} : \det(\lambda I - M) = 0\}$.

In finite dimension left and right invertibility coincide, since $ab = 1_A$ makes $L_a$ bijective; in infinite dimension they need not. This is the origin of the left/right distinction below, which cannot occur here.

## Left and Right Eigenvalues

Let $D$ be a division ring and $M \in M_n(D)$, acting on column vectors $D^n$. For $\lambda \in D$ and $v \in D^n$ the products $\lambda v$ and $v\lambda$ differ in general.

**Definition 2.1.** A scalar $\lambda \in D$ is a **right eigenvalue** of $M$ if $Mv = v\lambda$ for some nonzero $v \in D^n$, and a **left eigenvalue** if $Mv = \lambda v$ for some nonzero $v$. The sets of such $\lambda$ are the **right spectrum** $\sigma_R(M)$ and the **left spectrum** $\sigma_L(M)$.

**Proposition 2.2.** $\lambda \in \sigma_L(M)$ iff $M - \lambda I$ is singular.

**Proof.** $Mv = \lambda v \iff (M-\lambda I)v = 0$, and a square matrix over a division ring is singular iff it has a nonzero kernel vector.

Thus $\sigma_L(M)$ is exactly the spectrum of Definition 1.1 with scalars in $D$. The right problem does not reduce this way, since $v\lambda \neq \lambda v$ in general; note that $\sigma_R(M)$ is a union of conjugacy classes, because $Mv = v\lambda$ gives $M(vw) = (vw)(w^{-1}\lambda w)$ for every nonzero $w$.

**Example 2.3.** For $D = \mathbb{H}$, $n = 1$, $M = [q]$, the equation $qv = \lambda v$ forces $\lambda = q$, so $\sigma_L([q]) = \{q\}$, while $\sigma_R([q]) = \{v^{-1}qv : v \in \mathbb{H}^\times\}$ is a point for real $q$ and a $2$-sphere otherwise. Thus $\sigma_L([q]) \neq \sigma_R([q])$ for non-real $q$.

**Proposition 2.4.** If $D$ is a field, then $\sigma_L(M) = \sigma_R(M) = \{\lambda : \det(\lambda I - M) = 0\}$.

**Consequence for the biquaternions.** Since the centre of $\mathbb{B}$ is $\mathbb{C}$, complex scalars commute with everything; if eigenvalues are required to lie in $\mathbb{C}$, the left and right problems for a biquaternion coincide and agree with the matrix spectrum below. If eigenvalues may be arbitrary elements of $\mathbb{B}$, the two spectra can differ, but that problem is not studied here.

## The Biquaternion Spectrum

A biquaternion is written $\tilde{Q} = \sum_{\mu=0}^3 Q_\mu e_\mu$. Its **trace** and **biquaternion norm** functionals are

$$
T(\tilde{Q}) = 2Q_0, \qquad D(\tilde{Q}) = N(\tilde{Q}) = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 .
$$

Write $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ and let $B = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}$ be a fixed square root, the **complex norm of the vector part**; replacing $B$ by $-B$ changes nothing.

**Definition 3.1.** The **spectrum** of $\tilde{Q}$ is $\sigma(\tilde{Q}) = \{\lambda \in \mathbb{C} : \tilde{Q} - \lambda e_0 \text{ is not invertible in } \mathbb{B}\}$, the spectrum of Definition 1.1. Its characteristic polynomial is

$$
p_{\tilde{Q}}(\lambda) = \lambda^2 - 2Q_0\lambda + N(\tilde{Q}) = \lambda^2 - 2Q_0\lambda + Q_0^2 + B^2 = (\lambda - Q_0 - iB)(\lambda - Q_0 + iB),
$$

so

$$
\sigma(\tilde{Q}) = \{Q_0 + iB, \, Q_0 - iB\},
$$

the two roots coinciding exactly when $B = 0$.

**Consistency with invertibility.** Since $N(\tilde{Q} - \lambda e_0) = (Q_0-\lambda)^2 + Q_1^2 + Q_2^2 + Q_3^2 = p_{\tilde{Q}}(\lambda)$, the spectrum contains $0$ exactly when $N(\tilde{Q}) = 0$, i.e. when $\tilde{Q}$ is zero or a zero divisor. The spectrum of left multiplication on $\mathbb{B} \cong \mathbb{C}^4$ is the same set, with doubled multiplicity (§*Eigenspaces and Their Dimensions*).

**Physical reading: the measured values.** The spectrum is the set of two complex numbers a measurement of the element can return. Its characteristic polynomial is the one-qubit structure: the two eigenvalues $Q_0 \pm iB$ are the two outcomes, their sum $2Q_0$ is twice the mean and their product $N(\tilde{Q})$ the determinant. That the spectrum empties of nothing and is finite is the algebraic statement that a finite-dimensional algebra has a bounded set of measurement outcomes. The zero-divisor criterion — zero is in the spectrum exactly for a zero divisor — is the statement that the "measurement values" of a null element include $0$, which is the algebraic shadow of the null cone of *Biquaternion Norm and Invertibility*.

## Cayley–Hamilton and the Trace and Determinant Functionals

**Theorem 4.1 (Cayley–Hamilton).** Every $\tilde{Q} \in \mathbb{B}$ satisfies $\tilde{Q}^2 - 2Q_0\tilde{Q} + N(\tilde{Q})e_0 = 0$, i.e. $\tilde{Q}^2 - T(\tilde{Q})\tilde{Q} + D(\tilde{Q})e_0 = 0$.

**Proof.** With $\tilde{Q} = Q_0e_0 + \mathbf{Q}$ and $\mathbf{Q}^2 = -B^2 e_0$,

$$
\tilde{Q}^2 = Q_0^2 e_0 + 2Q_0\mathbf{Q} - B^2 e_0 = 2Q_0\tilde{Q} - (Q_0^2 + B^2)e_0 = 2Q_0\tilde{Q} - N(\tilde{Q})e_0.
$$

**Corollary 4.2.** If $N(\tilde{Q}) \neq 0$, then $\tilde{Q}^{-1} = (2Q_0e_0 - \tilde{Q})/N(\tilde{Q}) = \bar{\tilde{Q}}/N(\tilde{Q})$.

**Proposition 4.3.** The functionals $T, D$ satisfy

$$
T(\tilde{P}+\tilde{Q}) = T(\tilde{P})+T(\tilde{Q}), \quad T(\lambda\tilde{Q}) = \lambda T(\tilde{Q}), \quad T(\tilde{P}\tilde{Q}) = T(\tilde{Q}\tilde{P}), \quad T(e_0) = 2,
$$

$$
D(\tilde{P}\tilde{Q}) = D(\tilde{P})D(\tilde{Q}), \quad D(\lambda\tilde{Q}) = \lambda^2 D(\tilde{Q}), \quad D(e_0) = 1,
$$

and both are invariant under similarity. The determinant $D = N$ is multiplicative, the trace is linear and cyclic but not multiplicative, and $D(\exp\tilde{Q}) = e^{T(\tilde{Q})}$.

**Proof.** Direct computation from the definitions, with $T(\tilde{Q}) = 2Q_0$ and $D(\tilde{Q}) = N(\tilde{Q})$.

**Physical reading.** The trace and the determinant are the two invariants a physical transformation may not change: the cyclic trace is what makes a rotation preserve the norm of a vector, and the multiplicative determinant is what makes the group of unit-norm elements closed under multiplication. That the determinant of the exponential is the exponential of the trace is the algebraic reason the group of unit-norm elements is the Lie group whose algebra is the trace-free part, developed in *Biquaternion Lie Algebra* and *Biquaternion Lie Group and Exponential Structure*.

## The Commutative Subalgebra Generated by a Single Biquaternion

The functionals of the previous section are the coefficients of the vanishing polynomial, and this makes the algebra generated by a single element transparent. For $\tilde{Q} \in \mathbb{B}$, the **commutative subalgebra generated by $\tilde{Q}$** is the $\mathbb{C}$-linear span of $\{e_0, \tilde{Q}, \tilde{Q}^2, \dots\}$, denoted $\mathbb{C}[\tilde{Q}]$; it is the smallest subalgebra of $\mathbb{B}$ containing $e_0$ and $\tilde{Q}$, and it is the image of the algebra homomorphism

$$
\mathbb{C}[x] \longrightarrow \mathbb{B}, \qquad x \longmapsto \tilde{Q}.
$$

**The minimal polynomial.** The kernel of this homomorphism is the principal ideal $(m_{\tilde{Q}})$ generated by the **minimal polynomial** $m_{\tilde{Q}}$, the monic polynomial of least degree with $m_{\tilde{Q}}(\tilde{Q}) = 0$. By Cayley–Hamilton $m_{\tilde{Q}}$ divides the characteristic polynomial $x^2 - 2Q_0x + N(\tilde{Q})$, so $\deg m_{\tilde{Q}} \in \{1, 2\}$, and

$$
\mathbb{C}[\tilde{Q}] \cong \mathbb{C}[x]/(m_{\tilde{Q}}), \qquad \mathbb{C}[\tilde{Q}] = \operatorname{span}_{\mathbb{C}}\{e_0, \tilde{Q}\}.
$$

**The two cases.** Let $\Delta = -4B^2$ be the discriminant of the characteristic polynomial.

- **$\Delta \neq 0$ ($B \neq 0$).** $m_{\tilde{Q}} = x^2 - 2Q_0x + N(\tilde{Q})$ splits, with roots $Q_0 \pm iB$, and the Chinese remainder theorem gives $\mathbb{C}[\tilde{Q}] \cong \mathbb{C} \times \mathbb{C}$, evaluation at the two roots. This is the semisimple case; $\tilde{Q}$ is diagonalisable with eigenvalues $Q_0 \pm iB$.
- **$\Delta = 0$ and $\mathbf{Q} \neq 0$ ($B = 0$).** $m_{\tilde{Q}} = (x - Q_0)^2$, and $\mathbb{C}[\tilde{Q}] \cong \mathbb{C}[\epsilon]/(\epsilon^2)$ with $\epsilon = \tilde{Q} - Q_0e_0$ nilpotent of order two. This is the local, non-semisimple case.
- **$\mathbf{Q} = 0$.** $m_{\tilde{Q}} = x - Q_0$ and $\mathbb{C}[\tilde{Q}] = \mathbb{C}e_0$, of dimension one.

So $\dim_{\mathbb{C}} \mathbb{C}[\tilde{Q}]$ is $2$ in the first two cases and $1$ in the scalar case, and the isomorphism type is the same dichotomy as the conjugacy classification of §*Similarity Classes and the Eigenvalue Dichotomy*.

**The functional calculus.** Since $\mathbb{C}[\tilde{Q}] \cong \mathbb{C}[x]/(m_{\tilde{Q}})$, every power series $F(z) = \sum_n a_n z^n$ with complex coefficients has $F(\tilde{Q}) = \alpha e_0 + \beta \tilde{Q}$ for scalars $\alpha, \beta$ determined by the data of $F$ on the roots: the two values $F(Q_0 \pm iB)$ in the semisimple case, and $F(Q_0)$ together with $F'(Q_0)$ in the local case. Consequently $F(\tilde{Q})$ converges if and only if $F$ converges at the root or roots (in the local case, $F$ and its derivative). Every elementary function of a single biquaternion is an instance, and the standard identities of complex analysis hold in $\mathbb{C}[\tilde{Q}]$ because it is commutative; this is the structural fact behind *Biquaternion Elementary Functions*.

**Physical reading: one element at a time.** The subalgebra $\mathbb{C}[\tilde{Q}]$ is the commutative world a single observable carries with it: within it, all the algebra one needs for that observable — its powers, its exponential, its functions — behaves like complex numbers. That the subalgebra is two-dimensional in the interesting case and the functional calculus is determined by the values at the two eigenvalues is why a function of a single qubit observable is fixed by two numbers. The one-qubit calculus the quantum-mechanical articles use — exponentiating a Hamiltonian, forming a unitary from an observable — is exactly this calculus, restricted to the two-dimensional subalgebra generated by the observable.

## Similarity Classes and the Eigenvalue Dichotomy

**Definition 5.1.** Two biquaternions are **conjugate** (or **similar**) if $\tilde{Q}' = S\tilde{Q}S^{-1}$ for some invertible $S \in \mathbb{B}$. The functionals $T, D$ are the coefficients of the characteristic polynomial.

**Theorem 5.2 (classification).** Let $T = T(\tilde{Q})$, $D = D(\tilde{Q})$, and let $\Delta = T^2 - 4D = 4(Q_0^2 - N(\tilde{Q})) = -4B^2$ be the discriminant.

(1) **Distinct eigenvalues ($\Delta \neq 0$, i.e. $B \neq 0$).** $\tilde{Q}$ has the two distinct eigenvalues $Q_0 \pm iB$, and its conjugacy class is determined by the unordered pair of eigenvalues, equivalently by $(T,D)$.

(2) **Repeated eigenvalue ($\Delta = 0$, i.e. $B = 0$).** The only eigenvalue is $Q_0$, and there are exactly two conjugacy classes with $(T,D) = (2Q_0, Q_0^2)$: the **central class** $\mathbf{Q} = 0$ ($\tilde{Q} = Q_0e_0$) and the **non-semi-simple class** $\mathbf{Q} \neq 0$, $\mathbf{Q}^2 = 0$ (conjugate to the Jordan block with diagonal $Q_0$).

Thus $(T,D)$ determines the conjugacy class except on the repeated locus, where the separating invariant is whether $\mathbf{Q} = 0$.

**Proof.** (1) $p_{\tilde{Q}}$ has two distinct roots, so $\tilde{Q}$ is diagonalizable with them, and any two such elements are similar. (2) $B=0$ gives $\mathbf{Q}^2 = 0$; if $\mathbf{Q}\neq 0$ then $\tilde{Q} - Q_0e_0$ is nonzero with square $0$, so $\tilde{Q}$ is non-semi-simple and hence similar to the Jordan block with diagonal $Q_0$.

In case 2, $N(\tilde{Q}) = Q_0^2$, so the non-semi-simple element is a zero divisor exactly when $Q_0 = 0$.

**Physical reading.** Two elements are physically the same observable exactly when a change of internal frame — a similarity by an invertible element, the sandwich action — carries one to the other. The classification says the unordered pair of eigenvalues fixes the observable, except in the degenerate case where the extra invariant is whether the element is a scalar or has a nilpotent vector part. This is the algebraic statement that a two-level observable is fixed by its two measured values, with one exception at degeneracy: the nilpotent case, which is the algebra's form of two coincident levels that cannot be separated by any measurement. The sandwich action that implements the frame change is developed in *Biquaternion Rotations and Lorentz Transformations*.

## Eigenspaces and Their Dimensions

**Definition 6.1.** For $\lambda \in \sigma(\tilde{Q})$ the **eigenspace** is $E_\lambda = \{x \in \mathbb{B} : \tilde{Q}x = \lambda x\}$, the eigenspace of left multiplication by $\tilde{Q}$ on $\mathbb{B}$, and $\dim_\mathbb{C} E_\lambda$ is the **geometric multiplicity**.

**Proposition 6.2.** For $\lambda \in \sigma(\tilde{Q})$: (1) if $B \neq 0$ then $\dim_\mathbb{C} E_\lambda = 2$; (2) if $B = 0$ and $\mathbf{Q} = 0$ then $E_{Q_0} = \mathbb{B}$; (3) if $B = 0$ and $\mathbf{Q} \neq 0$ then $\dim_\mathbb{C} E_{Q_0} = 2$.

**Proof.** (1) Left multiplication by $\tilde{Q}$ is diagonalizable with the two distinct eigenvalues $Q_0 \pm iB$, each of algebraic multiplicity $2$, hence each eigenspace has dimension $2$. (2) $\tilde{Q} = Q_0e_0$ is central, so $\tilde{Q}x = Q_0x$ for every $x$. (3) Left multiplication by the nilpotent $\tilde{Q} - Q_0e_0$ has square $0$ and rank $2$, hence nullity $2$.

**Corollary 6.3.** In the regular module $\mathbb{B}$ the geometric multiplicity of an eigenvalue is $2$, except for a central element, where it is $4$; only for a nilpotent element does it fall below the algebraic multiplicity $4$.

**Real and complex eigenvalues.** A real eigenvalue does not force real eigenvectors: $E_\lambda \subseteq \mathbb{B}$ is still a complex subspace, of real dimension twice its complex dimension. In the Hermitian case both eigenvalues are real.

**Physical reading: degeneracy of a qubit.** Each eigenvalue of a generic element has a two-complex-dimensional eigenspace in the regular module: the two eigenvectors of a qubit observable form a pair, one per chirality or one per column, as *Biquaternion Ideals and Peirce Decomposition* explains. Only a central element — a pure phase — has the whole algebra as eigenspace, and only a nilpotent element has an eigenspace smaller than the algebraic multiplicity. The nilpotent case is the algebraic form of a degenerate two-level system whose two states cannot be resolved: this is the same degeneracy that makes a null element a zero divisor, and it is why degeneracy and the null cone are the same phenomenon in this framework.

## The Resolvent

**Definition 7.1.** The **resolvent** of $\tilde{Q}$ is $R(\lambda) = (\tilde{Q} - \lambda e_0)^{-1}$, defined for $\lambda \notin \sigma(\tilde{Q})$.

**Proposition 7.2.** For $\lambda \notin \sigma(\tilde{Q})$,

$$
R(\lambda) = \frac{(Q_0-\lambda)e_0 - \mathbf{Q}}{(Q_0-\lambda)^2 + B^2} = \frac{\overline{\tilde{Q} - \lambda e_0}}{p_{\tilde{Q}}(\lambda)}.
$$

**Proof.** $\tilde{Q} - \lambda e_0$ has conjugate $(Q_0-\lambda)e_0 - \mathbf{Q}$ and norm $(Q_0-\lambda)^2 + B^2 = p_{\tilde{Q}}(\lambda)$; apply Corollary 4.2.

**Corollary 7.3 (analyticity).** $R$ is rational in $\lambda$ with denominator $p_{\tilde{Q}}(\lambda)$, hence holomorphic on $\mathbb{C}\setminus\sigma(\tilde{Q})$, with poles exactly at the two eigenvalues. The pole is simple when $\tilde{Q}$ is diagonalisable, and double when $B = 0$ with $\mathbf{Q} \neq 0$, where $p_{\tilde{Q}} = (\lambda-Q_0)^2$ but the numerator at $\lambda = Q_0$ is $-\mathbf{Q} \neq 0$.

Finally, the resolvent satisfies $R(\lambda) - R(\mu) = (\lambda-\mu)R(\lambda)R(\mu)$, since with $A = \tilde{Q}-\lambda e_0$ and $B = \tilde{Q}-\mu e_0$ one has $A^{-1}-B^{-1} = A^{-1}(B-A)B^{-1}$; consequently $R'(\lambda) = R(\lambda)^2$.

**Physical reading.** The resolvent is the Green's function of the eigenvalue problem: it is the object whose poles are the measured values, and the double pole at a degenerate nilpotent element is the algebraic statement that such a system has a Jordan structure rather than a clean pair of levels. In the field-theoretic language the same object appears as the propagator, and the position of its poles is the spectrum of masses the theory can produce.

## The Spectral Radius

**Definition 8.1.** The **spectral radius** is $\rho(\tilde{Q}) = \max\{|\lambda| : \lambda \in \sigma(\tilde{Q})\} = \max\{|Q_0+iB|, |Q_0-iB|\}$.

**Proposition 8.2.** $\rho(\tilde{Q}) = 0$ iff $\tilde{Q}$ is nilpotent, equivalently $\tilde{Q}^2 = 0$, equivalently $Q_0 = 0$ and $B = 0$.

**Proof.** $\rho = 0$ iff $Q_0 = B = 0$, and then $p_{\tilde{Q}}(\lambda) = \lambda^2$, so $\tilde{Q}^2 = 0$ by Cayley–Hamilton; conversely $\tilde{Q}^2 = 0$ makes $0$ the only eigenvalue. The nonzero pure nilpotents $\mathbf{Q}$ with $\mathbf{Q}^2 = 0$, which are zero divisors, are a special case.

**Theorem 8.3 (Gelfand).** For any norm on the finite-dimensional algebra $\mathbb{B}$, $\rho(\tilde{Q}) = \lim_{k\to\infty}\|\tilde{Q}^k\|^{1/k}$, independently of the biquaternion norm; with the Euclidean norm this reads $\lim_k\|\tilde{Q}^k\|_E^{1/k}$.

**Physical reading.** The spectral radius is the largest measurement outcome, in modulus. The Gelfand formula makes it a growth rate: the asymptotic size of the powers of an element is governed by the largest eigenvalue. In the physical reading, this is the rate at which repeated application of a transformation amplifies — the algebraic statement behind stability and decay rates in the quantum-mechanical articles.

## The Exponential and the Logarithm

The exponential $\exp(\tilde{Q}) = \sum_n \tilde{Q}^n/n!$ is entire and is the value of $e^z$ at the spectrum, in the holomorphic functional calculus on $\mathbb{C}[\tilde{Q}] = \mathrm{span}_\mathbb{C}\{e_0,\tilde{Q}\}$. *Biquaternion Elementary Functions* gives $\exp(\tilde{Q}) = e^{Q_0}(\cos B\,e_0 + \sin B\,\hat{n})$ for $B \neq 0$ with $\hat{n} = \mathbf{Q}/B$, and $\exp(\tilde{Q}) = e^{Q_0}(e_0 + \mathbf{Q})$ for $B = 0$; the eigenvalues are $e^{Q_0 \pm iB}$ in the first case and the repeated $e^{Q_0}$ in the second.

**Non-injectivity.** Since $2\pi i n e_0$ is central, $\exp(\tilde{Q} + 2\pi i n e_0) = \exp(\tilde{Q})$ for every integer $n$; in particular $\exp(0) = \exp(2\pi i e_0) = e_0$, although $2\pi i e_0 \neq 0$.

**The logarithm.** A **logarithm** of $\tilde{Q}$ is any $\tilde{L}$ with $\exp(\tilde{L}) = \tilde{Q}$. *Biquaternion Elementary Functions* proves that every invertible biquaternion has one, so $\exp : \mathbb{B} \to \mathbb{B}^\times$ is surjective; not being injective, it has a multivalued inverse, and a branch must be chosen. Non-uniqueness comes from adding a commuting element of the kernel, in particular $2\pi i n e_0$, and from choosing a complex logarithm of each eigenvalue. No continuous, and hence no holomorphic, logarithm can exist on the whole group of units: one applied to $\lambda e_0$ and composed with the determinant would give a continuous logarithm of $\lambda^2$ on $\mathbb{C}^\times$, impossible because $\lambda^2$ winds twice around the origin.

**Physical reading: exponentiating a generator.** The exponential is how an infinitesimal transformation becomes a finite one: the spectrum of $\exp(\tilde{Q})$ is the exponential of the spectrum of $\tilde{Q}$, so an eigenvalue of the generator becomes a phase or a stretch of the transformation. The non-injectivity by $2\pi i n e_0$ is the statement that a global phase of $2\pi n$ is unobservable, and the two-to-one covering this creates is the double cover of the rotation group — the spinorial fact the framework reads in *Biquaternion Rotations and Lorentz Transformations* and in *The Spinor Module in Biquaternionic Form and Its Lorentz Action*. The group structure of the exponential and its domain are *Biquaternion Lie Group and Exponential Structure*.

## Hermitian and Normal Elements

**Definition 10.1.** $\tilde{Q}$ is **Hermitian** if $\tilde{Q}^\dagger = \tilde{Q}$, **unitary** if $\tilde{Q}^\dagger\tilde{Q} = \tilde{Q}\tilde{Q}^\dagger = e_0$, and **normal** if $\tilde{Q}\tilde{Q}^\dagger = \tilde{Q}^\dagger\tilde{Q}$. Hermitian and unitary elements are normal.

The Hermitian condition is a subspace condition: writing $\tilde{Q} = \sum_\mu Q_\mu e_\mu$, it says exactly that $Q_0 \in \mathbb{R}$ and $Q_k = iq'_k$ with $q'_k \in \mathbb{R}$. So the Hermitian elements of $\mathbb{B}$ are precisely the elements of the Hermitian subspace $\mathbb{M}_+$, and the anti-Hermitian elements are precisely those of $\mathbb{M}_-$; the Hermitian idempotents $\tilde\Pi_1, \tilde\Pi_2$ of Theorem 11.2 lie in $\mathbb{M}_+$.

**Proposition 10.3.** If $\tilde{Q}$ is Hermitian then $T(\tilde{Q})$, $D(\tilde{Q})$, and both eigenvalues are real.

**Proof.** Hermitian elements have $Q_0 \in \mathbb{R}$ and $Q_k = iq'_k$ with $q'_k \in \mathbb{R}$, so $B^2 = -\sum_k(q'_k)^2$ is real and non-positive, $iB$ is real, and $Q_0 \pm iB \in \mathbb{R}$.

**Proposition 10.4.** $\tilde{Q}$ is normal iff left multiplication by $\tilde{Q}$ is unitarily diagonalizable, i.e. iff $\mathbb{B}$ has an orthonormal basis of eigenvectors with respect to the Hermitian form. In particular a normal element with $B = 0$ must be central, and $\tilde{Q}$ is Hermitian iff it is normal with real spectrum. A unitary element is normal and has all eigenvalues of modulus $1$.

**Physical reading: observables, unitaries and normality.** Hermitian elements are the observables; their real spectrum, Proposition 10.3, is why a measurement returns a real number. Unitary elements are the symmetries — the evolutions and the frame changes — and their spectrum on the unit circle is why a symmetry preserves the norm. Normality is the exact condition for an element to be an observable or a symmetry in a common frame: the normal elements are the ones with an orthonormal eigenbasis, and it is this that makes them the physically admissible elements. That the Hermitian elements are exactly the Hermitian subspace $\mathbb{M}_+$, and the anti-Hermitian ones exactly $\mathbb{M}_-$, ties the spectral theory to the sector structure: the observables live in the informational sector, the generators of the symmetries in the material one, up to the factor of $i$ that the exponential supplies. The sector articles are *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* and *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*.

## The Spectral Theorem

**Theorem 11.1.** $M \in M_2(\mathbb{C})$ is normal iff $M = U\,\mathrm{diag}(\lambda_1,\lambda_2)\,U^\dagger$ with $U$ unitary and $\lambda_1,\lambda_2 \in \mathbb{C}$ its spectrum; if $M$ is Hermitian the $\lambda_i$ are real, and if $M$ is unitary they have modulus $1$.

**Theorem 11.2 (biquaternion form).** $\tilde{Q}$ is normal iff there are a unitary $\tilde{U} \in \mathbb{B}$ and $\lambda_1,\lambda_2 \in \mathbb{C}$ with

$$
\tilde{U}\tilde{Q}\tilde{U}^\dagger = \frac{\lambda_1+\lambda_2}{2}e_0 + \frac{i(\lambda_1-\lambda_2)}{2}e_3.
$$

Equivalently $\tilde{Q} = \lambda_1\tilde\Pi_1 + \lambda_2\tilde\Pi_2$ with Hermitian idempotents $\tilde\Pi_1,\tilde\Pi_2$ satisfying $\tilde\Pi_1+\tilde\Pi_2 = e_0$, $\tilde\Pi_1\tilde\Pi_2 = 0$, $\tilde\Pi_i^\dagger = \tilde\Pi_i$, $\tilde\Pi_i^2 = \tilde\Pi_i$; for $\lambda_1 \neq \lambda_2$,

$$
\tilde\Pi_1 = \frac{\tilde{Q}-\lambda_2e_0}{\lambda_1-\lambda_2}, \qquad \tilde\Pi_2 = \frac{\tilde{Q}-\lambda_1e_0}{\lambda_2-\lambda_1}.
$$

**Proof.** This is Theorem 11.1 transported to $\mathbb{B}$, identifying a normal element with its diagonal form $\frac{\lambda_1+\lambda_2}{2}e_0 + \frac{i(\lambda_1-\lambda_2)}{2}e_3$ and using that Hermitian conjugation is a $*$-involution on $\mathbb{B}$.

**Physical reading: the resolution of the identity.** The biquaternion spectral theorem is the resolution of the identity of a two-level system: an observable is a real combination of two orthogonal Hermitian idempotents — the two projectors of the measurement — and the projectors are recovered from the observable by the displayed formulas. This is the algebraic form of the Born rule's bookkeeping, and it is the reason the framework's observables are read as elements of $\mathbb{M}_+$ rather than as operators on an external Hilbert space. The idempotents themselves, their parametrisation by the Bloch sphere, and their classification are *Biquaternion Idempotents and Projections*; the two-projector decomposition of the algebra is *Biquaternion Ideals and Peirce Decomposition*.

## The S-Spectrum and the Quaternionic Spectral Theorem

§*The Spectral Theorem* works for biquaternions because $\mathbb{C}$ is central. When the scalars do not commute, as over $\mathbb{H}$, the left/right ambiguity returns and a different spectrum is needed: the **S-spectrum**.

**Definition 12.1.** For $T \in M_n(\mathbb{H})$, the **S-spectrum** is $\sigma_S(T) = \{s \in \mathbb{H} : T^2 - 2\mathrm{Re}(s)T + |s|^2I \text{ is not invertible}\}$. It rests on the identity $s^2 - 2\mathrm{Re}(s)s + |s|^2 = 0$, which holds because $s - \mathrm{Re}(s)$ is pure imaginary.

**Theorem 12.2.** For $T \in M_n(\mathbb{H})$, $\sigma_S(T) = \sigma_R(T)$.

**Proof (one direction).** If $Tv = vs$ then $(T^2 - 2\mathrm{Re}(s)T + |s|^2I)v = v(s^2 - 2\mathrm{Re}(s)s + |s|^2) = 0$, so the operator is singular; the converse is proved in the references.

For $T = [q]$ this gives the $2$-sphere $\sigma_S([q]) = \{v^{-1}qv : v \in \mathbb{H}^\times\}$ for non-real $q$; compare Example 2.3.

**Theorem 12.3.** If $T \in M_n(\mathbb{H})$ is normal, then $T = U\,\mathrm{diag}(\lambda_1,\dots,\lambda_n)\,U^*$ for a unitary $U$ and complex $\lambda_i$ in a fixed slice, and $\sigma_S(T) = \bigcup_{i=1}^n [\lambda_i]$, where $[\lambda]$ is the conjugacy class $\{v^{-1}\lambda v : v \in \mathbb{H}^\times\}$. For Hermitian $T$ the $\lambda_i$ are real; for unitary $T$ they have modulus $1$.

**Relation to the biquaternions.** For a real quaternion $q$ viewed as a biquaternion, the complex spectrum $\{q_0 \pm i|\mathbf{q}|\}$ is the slice $\sigma(q) = [q] \cap \mathbb{C}_i$ of the S-sphere $[q]$. Thus the S-spectrum plays for quaternionic matrices the role the complex spectrum plays for biquaternion matrices.

**Physical reading: the quaternionic form of the quantum spectrum.** Because the framework's scalars are biquaternions with a central $i$, the ordinary complex spectrum suffices and the S-spectrum is not needed: this is the spectral-theoretic content of the algebra being $M_2(\mathbb{C})$ over $\mathbb{C}$. The S-spectrum is what one must use if one tries to do the same physics with quaternionic scalars, and its coincidence with the right spectrum is the precise sense in which the quaternionic formulation is a re-parametrisation: an S-eigenvalue is a sphere of complex eigenvalues, exactly as a quaternionic eigenvalue is a conjugacy class. The framework's choice of a central $i$ is therefore a choice that the spectrum be a finite set of complex numbers rather than a union of spheres.

## Summary

The word "spectrum" is used in several inequivalent senses for $\mathbb{B}$, and the main source of error in the subject is the silent switching between them. Unqualified, the spectrum of a biquaternion means its spectrum under Definition 1.1: the two-element set

$$
\sigma(\tilde{Q}) = \{Q_0 + iB, \, Q_0 - iB\}, \qquad B = \sqrt{Q_1^2 + Q_2^2 + Q_3^2},
$$

the roots of the characteristic polynomial $\lambda^2 - 2Q_0\lambda + D(\tilde{Q})$, where $T(\tilde{Q}) = 2Q_0$ is the trace functional and $D(\tilde{Q}) = N(\tilde{Q})$ is the biquaternion norm. The two roots coincide exactly when $B = 0$; the set $\sigma(\tilde{Q})$ contains $0$ exactly when $\tilde{Q}$ is a zero divisor, by the invertibility criterion. Because $\mathbb{B}$ is noncommutative, the left and right spectra must be distinguished from it; they agree with $\sigma(\tilde{Q})$ as a set, with the multiplicities of the left spectrum (in the regular module) doubled.

The rest of the theory is intrinsic to $\mathbb{B}$: the commutative subalgebra generated by a single element and its functional calculus, Cayley–Hamilton, the similarity classification and the eigenvalue dichotomy, the eigenspace dimensions in the regular module, the resolvent and its expansion, the spectral radius, and the exponential and the logarithm. The spectral theorem takes the biquaternion form $\tilde{Q} = \lambda_1 \tilde\Pi_1 + \lambda_2 \tilde\Pi_2$ with Hermitian idempotents $\tilde\Pi_1, \tilde\Pi_2$ summing to $e_0$ and orthogonal; a Hermitian element has real spectrum, a unitary element spectrum on the unit circle. Physically the Hermitian elements are the observables and their spectra are the values a measurement returns; the normal elements are those diagonalisable in an orthonormal frame; and because the central $i$ makes the scalars commute, the ordinary complex spectrum suffices.

When the scalars do not commute, as over $\mathbb{H}$, the left/right ambiguity requires a different notion, the S-spectrum $\sigma_S(T) = \{s \in \mathbb{H} : T^2 - 2\operatorname{Re}(s)T + |s|^2 I$ is not invertible$\}$, which coincides with the right spectrum and, for a real quaternion viewed as a biquaternion, restricts to the complex spectrum as $\sigma(q) = [q] \cap \mathbb{C}_i$. The S-spectrum thus plays for quaternionic matrices the role the complex spectrum plays for biquaternion matrices.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ | General biquaternion |
| $B = \sqrt{Q_1^2+Q_2^2+Q_3^2}$ | Complex norm of the vector part |
| $T(\tilde{Q}) = 2Q_0$ | Trace functional |
| $D(\tilde{Q}) = N(\tilde{Q})$ | Determinant functional (norm) |
| $\sigma(\tilde{Q}) = \{Q_0 \pm iB\}$ | Spectrum (complex spectrum); the measured values |
| $\sigma_L, \sigma_R$ | Left and right spectra |
| $E_\lambda$ | Eigenspace in the regular module $\mathbb{B}$ |
| $R(\lambda)$ | Resolvent; poles at the spectrum |
| $\rho(\tilde{Q})$ | Spectral radius; the largest measurement outcome in modulus |
| $\sigma_S(T)$ | S-spectrum, for quaternionic scalars |
| $\tilde\Pi_1, \tilde\Pi_2$ | Hermitian idempotents in the biquaternion spectral theorem, $\tilde\Pi_1+\tilde\Pi_2 = e_0$, $\tilde\Pi_1\tilde\Pi_2 = 0$ |

## Further Reading

- F. R. Gantmacher, *The Theory of Matrices* (Chelsea, 1959), for the Jordan form and the similarity classification.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 1985), for eigenvalues, normal matrices and the spectral theorem.
- Nicholas J. Higham, *Functions of Matrices: Theory and Computation* (SIAM, 2008), for the matrix exponential, logarithm and functional calculus.
- Fuzhen Zhang, "Quaternions and matrices of quaternions", *Linear Algebra and its Applications* **251** (1997) 21–57, for left and right quaternionic eigenvalues.
- Fabrizio Colombo, Irene Sabadini and Daniele C. Struppa, *Noncommutative Functional Calculus* (Birkhäuser, 2011), for the S-spectrum.
- Vladimir V. Rodman, *Topics in Quaternion Linear Algebra* (Princeton University Press, 2014), for the spectral theory of quaternionic matrices.
