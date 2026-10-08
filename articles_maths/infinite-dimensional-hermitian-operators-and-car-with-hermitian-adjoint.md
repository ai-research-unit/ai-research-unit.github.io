
# __Infinite-Dimensional Hermitian Operators and CAR with Hermitian Adjoint__

## Introduction

Passing from a finite-dimensional Hermitian Clifford module to an infinite-dimensional one changes the operator theory in four ways at once, and the purpose of this article is to name them. The algebra becomes the **canonical anticommutation relation algebra**, or CAR algebra; the Hermitian form becomes the inner product of a Hilbert space and the module becomes its **Fock space**; the operators become unbounded, so the dagger is defined on a domain and the self-adjointness of an operator is a statement about the domain as well as the formula; and the finite trace, which was the sum of the diagonal entries, no longer exists as a positive linear functional defined on all of the algebra, so the **positivity** and the **states** of the theory take over the role the trace had in the finite case. The two structural facts that survive, and that organise the infinite theory, are that the dagger remains a positive involution, so that $c(f)^{\ast}c(f)\geq0$ and the positivity still comes from squares, and that the **unitaries of the one-particle space** still act on the algebra by automorphisms, the **Bogoliubov transformations**, whose implementability by a unitary of the Fock space is decided by a Hilbert–Schmidt condition, the theorem of Shale and Stinespring.

The article develops the infinite Hermitian Clifford module and its adjoint, the CAR algebra with its dagger, the Fock module and the number operator, the Bogoliubov transformations and their implementability, and the unbounded operators into which the finite statements grow. It is the infinite-dimensional companion of *Infinite-Dimensional Clifford Algebras and CAR with Inner Conjugation*, which develops the same algebra for the involutive structure alone; the difference is the dagger and the positivity, and the consequence is that the inner conjugation of that article is replaced here by the **Hermitian adjoint** on the one-particle Hilbert space, the bounded and unbounded operators replace the endomorphisms of the module, and the trace is replaced by the states.

The finite-dimensional theory is *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint*, *The Blade Form and the Hermitian Structure with Hermitian Adjoint* and *Positivity and the Hermitian Cone of a Hermitian Algebra with Hermitian Adjoint*; the operator spectrum is *The Spectra of Self-Adjoint Operators with Hermitian Adjoint*; the unbounded operators, the spectral theorem and Stone's theorem are *Unbounded Operators and Spectral Measures*; the CAR algebra for the involutive structure is *Infinite-Dimensional Clifford Algebras and CAR with Inner Conjugation*; the Dirac operator is *Dirac Operators with Hermitian Adjoint*; the operator-algebraic framework and the Fredholm theory are *Operator Algebras* and *Fredholm Theory*; and the finite truncation used as the anchor is the Clifford algebra $\mathrm{Cl}_{0,2n}(\mathbb{R})$ of the even-dimensional definite space.

## The Infinite-Dimensional Hermitian Module

### The Hilbert Space and the Adjoint

**Definition.** Let $\mathcal{H}$ be a complex Hilbert space with inner product $\langle\,,\rangle$, conjugate-linear in the first variable. The **one-particle space** is $\mathcal{H}$, the Hermitian form of the finite-dimensional theory is the inner product, and the **Hermitian Clifford module** is the Fock space $\mathcal{F} = \Lambda^{\bullet}\mathcal{H}$ of the next section.

**Theorem (the bounded operators).** The adjoint $T^{\ast}$ of a bounded operator is defined by $\langle Ts,t\rangle = \langle s,T^{\ast}t\rangle$ and makes $B(\mathcal{H})$ a $C^{\ast}$-algebra; the self-adjoint, skew-adjoint, unitary and normal operators are the bounded operators with $T^{\ast} = T$, $T^{\ast} = -T$, $T^{\ast} = T^{-1}$ and $TT^{\ast} = T^{\ast}T$. The **Hilbert–Schmidt** operators satisfy $\mathrm{Tr}(T^{\ast}T) < \infty$ and its ideal is $\mathcal{B}_2(\mathcal{H})$, the **trace-class** operators satisfy $\mathrm{Tr}|T| < \infty$ and its ideal is $\mathcal{B}_1(\mathcal{H})$; the trace is defined on $\mathcal{B}_1(\mathcal{H})$ and the pairing $\langle S,T\rangle = \mathrm{Tr}(S^{\ast}T)$ is the infinite-dimensional Hilbert–Schmidt form on $\mathcal{B}_2(\mathcal{H})$. Every bounded $T$ has the **polar decomposition** $T = U|T|$, $|T| = (T^{\ast}T)^{1/2}$, with $U$ a partial isometry, and the self-adjoint $T$ satisfies $- \|T\|\,I\leq T\leq\|T\|\,I$. These are the infinite-dimensional forms of *Self-Adjoint and Skew Operators with Hermitian Adjoint*, with the finite trace replaced by the trace on the trace class.

### The Failure of the Trace and the Role of the States

**Remark (what the finite trace becomes).** In the finite-dimensional theory the scalar part $\mathrm{Sc}$ was a positive tracial functional defined on the whole algebra and the form was its polarisation; in infinite dimensions the trace is defined only on the trace class and is **not** finite on the identity of $B(\mathcal{H})$. The replacement is the notion of a **state**: a positive linear functional $\omega$ with $\omega(1) = 1$, defined on the whole $C^{\ast}$-algebra, and the GNS construction that turns it into a Hilbert space and a representation. So the positivity of the finite theory becomes the positivity of the functionals, and the cone of positive elements is described by the states that they dominate. The finite statement "the trace form is non-degenerate and positive" becomes "the algebra carries a separating family of states"; the positivity is no longer a single trace form but a family.

**Proposition (positivity from squares).** The dagger remains a positive involution: $a^{\ast}a\geq0$ for every $a$ in the algebra, and every positive element is a sum of such squares. So the operator-theoretic positivity of the module and the algebraic positivity of the algebra coincide in the infinite case exactly as in the finite one, and the criterion "positive iff a sum of squares" — the finite form of the cone of *Positivity and the Hermitian Cone of a Hermitian Algebra with Hermitian Adjoint* — is the definition of the positive cone of the $C^{\ast}$-algebra.

## The CAR Algebra with the Dagger

### The Relations

**Definition.** Let $\mathcal{H}$ be a complex Hilbert space with its inner product. The **canonical anticommutation relation algebra** $\mathcal{A}(\mathcal{H})$ is the $\ast$-algebra generated by the **annihilation** operators $c(f)$, $f\in\mathcal{H}$, subject to

$$
c(f)^{\ast} = c^{\ast}(f), \qquad \{c(f),c(g)^{\ast}\} = \langle g,f\rangle\,1, \qquad \{c(f),c(g)\} = 0 ,
$$

so that the antilinear map $f\mapsto c(f)$ and its adjoint $f\mapsto c^{\ast}(f)$ are the **creation** and **annihilation** operators, $c(f)^{2} = 0$, and $c(f)^{\ast}c(f)\geq0$. The relations were verified in the finite truncation: in $\mathrm{Cl}_{0,2n}(\mathbb{R})$ with the **Witt basis**

$$
a_j = \tfrac12\bigl(e_{2j-1} + i\,e_{2j}\bigr), \qquad a_j^{\ast} = \tfrac12\bigl(-e_{2j-1}+i\,e_{2j}\bigr) = a_j^{\dagger} ,
$$

one has $\{a_j,a_k^{\ast}\} = \delta_{jk}$, $\{a_j,a_k\} = 0$ and $a_j^{2} = 0$ for all $j,k$; here the dagger of the Clifford algebra *is* the CAR adjoint, which is the precise sense in which the Hermitian-adjoint Clifford algebra is the CAR algebra in finite dimensions.

### The Fock Module and the Vacuum

**Theorem (the Fock representation).** There is an irreducible $\ast$-representation, the **Fock representation**, on the **Fock space** $\mathcal{F} = \Lambda^{\bullet}\mathcal{H}$, in which $c^{\ast}(f)$ is exterior multiplication by $f$ and $c(f)$ is its adjoint, the interior product (contraction); the **vacuum** is the vector $\Omega$ with $c(f)\Omega = 0$ for all $f$, it is cyclic, and the representation carries the inner product for which these operators are adjoints. The **vacuum idempotent** is the projection onto $\mathbb{C}\Omega$, and in the finite truncation it was verified that the elements
$$
f_{\mathrm{vac}} = \prod_{j=1}^{n}a_ja_j^{\ast} = \prod_{j=1}^{n}a_j^{\ast}a_j = \prod_{j=1}^{n}\bigl(1-a_j^{\ast}a_j\bigr)
$$
are self-adjoint idempotents; the three expressions agree because $a_ja_j^{\ast} = 1-a_j^{\ast}a_j$ is the consequence of $\{a_j,a_j^{\ast}\} = 1$.

**Theorem (the number operator).** The **number operator** $N = \sum_jc^{\ast}(f_j)c(f_j)$ over an orthonormal basis $(f_j)$ is self-adjoint and positive, with spectrum the non-negative integers; in the finite truncation its eigenvalues on $\Lambda^{\bullet}\mathbb{C}^n$ are $0,1,\dots,n$ with multiplicity the binomial coefficient $\binom{n}{k}$, the dimension of the $k$-th exterior power. So the Hermitian Clifford module of the infinite theory is graded by the exterior degree, the grading is the **occupation number**, and the self-adjoint operator $N$ is the infinite-dimensional form of the chirality grading of the finite spinor module.

### The Algebra and its Positivity

**Proposition (the $C^{\ast}$-completion and its trace).** For $\mathcal{H}$ separable the Fock representation is the GNS representation of the **vacuum state** $\omega(a) = \langle\Omega,a\Omega\rangle$, determined by the two-point function $\omega(c(g)c(f)^{\ast}) = \langle f,g\rangle$ and Wick's theorem; the norm completion is a **uniformly hyperfinite** $C^{\ast}$-algebra, the CAR algebra, and $\omega$ is a **pure** state whose GNS representation is irreducible. The algebra carries the **gauge action** $\gamma_\theta(c(f)) = e^{i\theta}c(f)$, a one-parameter group of automorphisms, and the number operator is its generator, $\gamma_\theta(a) = e^{i\theta N}ae^{-i\theta N}$; the finite algebra has the corresponding one-parameter group of inner automorphisms $t(S) = e^{i\theta N}te^{-i\theta N}$ studied in *Mixed Inner Conjugation and Hermitian Adjoint*. The **quasi-free states** are the states determined by an operator $T$ with $0\leq T\leq1$ through $\omega_T(c(g)c(f)^{\ast}) = \langle f,Tg\rangle$, and this operator is the Hermitian form of the state; the positivity of the state is the positivity $0\leq T\leq1$ of the form, which is the infinite-dimensional form of the Hermitian cone.

## Bogoliubov Transformations

### The Automorphisms from the One-Particle Unitaries

**Theorem (Bogoliubov).** Let $U$ be a unitary of $\mathcal{H}$. Then there is an automorphism $\alpha_U$ of the CAR algebra with
$$
\alpha_U\bigl(c(f)\bigr) = c(Uf),
$$
and the assignment $U\mapsto\alpha_U$ is a homomorphism from the unitary group to the automorphism group. The map is the infinite-dimensional analogue of the conjugation of the Clifford algebra by the units of the slice, and it is the action that makes the CAR algebra the carrier of the fermionic second quantisation: the one-particle unitary acts on the algebra, and its image in the automorphism group is the group of free evolutions.

### Implementability and the Hilbert–Schmidt Condition

**Theorem (Shale–Stinespring).** A Bogoliubov automorphism $\alpha_U$ is implemented by a unitary of the Fock space, $\alpha_U(a) = VaV^{-1}$ for some unitary $V$, **exactly when the off-diagonal block of $U$ with respect to the polarisation $(J)$ is Hilbert–Schmidt**. So the automorphisms of the CAR algebra that arise from one-particle unitaries split into two kinds: the **implementable** ones, those with Hilbert–Schmidt off-diagonal part, which act by a unitary of the module and preserve the vacuum up to a vector, and the **non-implementable** ones, which do not come from a unitary of the module and which change the representation. The implementable ones form the **restricted unitary group** $U(\mathcal{H};J)$, a subgroup of $U(\mathcal{H})$, and the quotient by the unitaries diagonal with respect to the polarisation is the **Fredholm** part, whose index classes are measured by the **index** of a Fredholm operator. The finite-dimensional analogue of the obstruction is the failure of the defect $uu^{\dagger}$ to be the identity in *Unitary Equivalence and Congruence of Operators with Hermitian Adjoint*: off the slice the sandwich is not an automorphism of the module, and in infinite dimensions the corresponding failure is the non-implementability.

**Remark (the index and the eightfold way).** The splitting of the one-particle unitaries by the Hilbert–Schmidt condition, and the index that measures the failure of implementability, is the analytic form of the $\mathbb{Z}$-grading of the restricted unitary group and of the mod-two periodicity of the Clifford algebra; it is the infinite-dimensional counterpart of the chirality grading of the finite spinor module and of the index of the Dirac operator, and the applications to the index theorem are *Fredholm Theory* and *The Atiyah–Singer Index Theorem and K-Theory*.

## The Unbounded Operators

**Remark (the operators are unbounded).** In infinite dimensions the operators of the article are **unbounded**: the **number operator** $N$ of the Fock module and the one-particle **Dirac Hamiltonian** $D$ are defined on a dense subspace of $\mathcal{F}$ rather than on the whole space, so their self-adjointness and their spectra are statements about that subspace as well as about the formula. What the Hermitian structure supplies at this layer is unchanged, and it is what the article uses: the dagger is a positive involution, $N$ is positive, and the spectrum of a self-adjoint operator is real with orthogonal eigenspaces for distinct eigenvalues.

**Remark (the boundary).** The analytic theory of the unbounded operators — the densely defined symmetric operators with their graphs and adjoints, the deficiency indices and the self-adjoint extensions, the spectral theorem and its projection-valued measure, the functional calculus, Stone's theorem and the one-parameter groups — is *Unbounded Operators and Spectral Measures*, quoted here for the operators of the CAR module and not rederived; the finite-dimensional bounded statements are those of *The Spectra of Self-Adjoint Operators with Hermitian Adjoint*. The measure and the integral on which that theory rests are Part III's, and no formula of it is reproduced here.

**Remark (the Fermi projection and the index).** The positive part of the spectrum of a self-adjoint operator gives the **Fermi projection** of the polarisation, and its rank is the index that appears in the theorem of Shale–Stinespring, quoted from *Unbounded Operators and Spectral Measures* and *Fredholm Theory*. So the positive spectrum and the Fermi projection are the infinite-dimensional form of the inertia of a Hermitian form, and the finite Sylvester law of *Unitary Equivalence and Congruence of Operators with Hermitian Adjoint* becomes the index of a pair of projections in the infinite theory.

## Worked Anchor: The Finite Truncation

Every statement of the article whose finite shadow is computable was checked in the finite Clifford algebra. In $\mathrm{Cl}_{0,2n}(\mathbb{R})$ with the Witt basis $a_j = \tfrac12(e_{2j-1}+ie_{2j})$: the CAR relations $\{a_j,a_k^{\ast}\} = \delta_{jk}$, $\{a_j,a_k\} = 0$, $a_j^{2} = 0$; the CAR adjoint is the Clifford dagger; the number operator $N = \sum_ja_j^{\ast}a_j$ is self-adjoint; the identity $a_ja_j^{\ast} = 1-a_j^{\ast}a_j$ holds; the vacuum idempotent $\prod_ja_ja_j^{\ast}$ is a self-adjoint idempotent; and the Fock space is the exterior algebra of the creation operators, with the number operator grading it by the exterior degree. These are the finite anchors of the infinite statements, and they are the reason the finite Hermitian Clifford algebra is the right model of the fermionic Fock space.

## Summary

The infinite-dimensional Hermitian Clifford module is the **Fock space** $\Lambda^{\bullet}\mathcal{H}$ of a Hilbert space, and its operators are the **bounded** operators of $B(\mathcal{H})$ with the adjoint, the Hilbert–Schmidt and trace-class ideals, and the **unbounded** self-adjoint operators, whose analytic theory is *Unbounded Operators and Spectral Measures*. The algebra is the **CAR algebra**, with the CAR relations $\{c(f),c(g)^{\ast}\} = \langle g,f\rangle$, $\{c(f),c(g)\} = 0$, and the dagger is a positive involution, $c(f)^{\ast}c(f)\geq0$; the relations, the Fock representation and the vacuum are verified in the finite truncation $\mathrm{Cl}_{0,2n}(\mathbb{R})$ with the Witt basis. The **number operator** is self-adjoint positive with spectrum the non-negative integers, the **vacuum** is the cyclic vector annihilated by the annihilators and its projection is a self-adjoint idempotent, and the **quasi-free states** are the states whose two-point function is a Hermitian form $0\leq T\leq1$, the infinite-dimensional form of the Hermitian cone.

The **Bogoliubov transformations** $\alpha_U(c(f)) = c(Uf)$ are the automorphisms of the algebra coming from the unitaries of the one-particle space, and the theorem of **Shale–Stinespring** states that such an automorphism is implemented by a unitary of the Fock space exactly when the off-diagonal part of $U$ is **Hilbert–Schmidt**; the implementable unitaries form the restricted unitary group, and the failure of implementability is measured by the **index** of a Fredholm operator, the infinite-dimensional form of the defect and of the inertia of the finite theory. The finite trace of the algebra is replaced by the **states** and the GNS construction, and the positivity of the theory is carried by the functionals and by $a^{\ast}a\geq0$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{F}=\Lambda^{\bullet}\mathcal{H}$ | Fock space of the one-particle Hilbert space |
| $c(f)$, $c^{\ast}(f)$ | Annihilation and creation operators |
| $\{c(f),c(g)^{\ast}\}=\langle g,f\rangle$, $\{c(f),c(g)\}=0$ | CAR relations |
| $c(f)^{\ast}=c^{\ast}(f)$, $c(f)^{\ast}c(f)\geq0$ | The dagger is a positive involution |
| $\Omega$, $c(f)\Omega=0$ | Vacuum; $c^{\ast}(f)$ is exterior multiplication |
| $N=\sum_jc^{\ast}(f_j)c(f_j)$ | Number operator, spectrum $\mathbb{N}_0$ |
| $\omega(a)=\langle\Omega,a\Omega\rangle$ | Vacuum state; GNS representation |
| $\omega_T(c(g)c(f)^{\ast})=\langle f,Tg\rangle$, $0\leq T\leq1$ | Quasi-free states and their forms |
| $\alpha_U(c(f))=c(Uf)$ | Bogoliubov transformation |
| $U$ implementable $\iff$ off-diagonal part Hilbert–Schmidt | Shale–Stinespring |

## Further Reading

- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics 2* (Springer, 2nd ed. 1997), for the CAR algebra, its Fock representation, the quasi-free states and the Bogoliubov transformations.
- John T. Cannon and Arthur S. Wightman (eds.), *Constructive Quantum Field Theory*, and the survey of Shale–Stinespring, for the implementability criterion of the Bogoliubov automorphisms.
- David E. Evans and Yasuyuki Kawahigashi, *Quantum Symmetries on Operator Algebras*, Oxford Mathematical Monographs (Clarendon Press, 1998), for the restricted unitary group, its index classes and the connection with Clifford algebra periodicity.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic Press, 1980), for the unbounded self-adjoint operators, the deficiency indices, the spectral theorem and Stone's theorem.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford University Press, 4th ed. 1958), and Bernd Thaller, *The Dirac Equation* (Springer, 1992), for the one-particle Dirac Hamiltonian and its self-adjointness.
