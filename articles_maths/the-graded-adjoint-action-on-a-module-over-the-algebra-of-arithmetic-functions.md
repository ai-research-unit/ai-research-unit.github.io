
# __The Graded Adjoint Action on a Module over the Algebra of Arithmetic Functions__

## Introduction

The algebra of arithmetic functions is $\mathbb{Z}/2$-graded by the number of prime factors, and every module over it inherits the grading with the Koszul sign convention of the superalgebra theory. The **graded adjoint action** is the adjoint of the graded action of an element with respect to a graded Hermitian form, the $\mathbb{Z}/2$-graded refinement of the adjoint of *The Adjoint of the Left Multiplication on the Algebra of Arithmetic Functions*. Its content is a cancellation: on the regular module the Koszul sign removes exactly the grade involution of *The Signed Adjoint of the Left Multiplication on the Algebra of Arithmetic Functions*, and the graded adjoint action turns out to be the plain transposed multiplication for every element, of either parity. This article defines the graded adjoint action, proves the cancellation, computes the products and the parity operator, and records the degenerate cases in which the graded structure and the adjoint structure decouple. Nothing here reads a distance as an object.

## The Graded Module and the Graded Action

### The data

**Definition.** A **graded module** over $\mathcal{A}$ is a module $M=M_0\oplus M_1$ on which every element of $\mathcal{A}$ acts by endomorphisms preserving the grading; a **graded Hermitian form** is a Hermitian form $\langle\cdot,\cdot\rangle_M$ with $\langle M_i,M_j\rangle_M=0$ for $i+j\ne0$. The **graded action** of $a$ is
$$
\rho_a(m)=(-1)^{|a||m|}\,a\cdot m,\qquad |a|=\Omega(a)\bmod2,\quad |m|\in\mathbb{Z}/2 ,
$$
the Koszul-signed multiplication.

**Theorem.** The graded action is a representation of the graded algebra: $\rho_a\rho_b=(-1)^{|a||b|}\rho_{ab}$, and $\rho_\varepsilon=\mathrm{id}$. On the regular module $M=\mathcal{A}$ with the coefficient form, the even and the odd parts of $\mathcal{A}$ are orthogonal, so the coefficient form is a graded form; and $\rho_a$ is the signed left multiplication $L_a\alpha$ when $a$ is odd and the plain $L_a$ when $a$ is even.

**Proof.** The Koszul identity is the definition; the orthogonality of the even and the odd parts of the regular module is the remark that an even-supported and an odd-supported arithmetic function are supported on disjoint sets. On the regular module the grading of an element is $\Omega$, so $\rho_a$ is the signed left multiplication $L_a\alpha$ for odd $a$ and the plain left multiplication $L_a$ for even $a$. This is the graded algebra of *The Graded Action on a Module over the Algebra of Arithmetic Functions*.

### The graded adjoint

**Definition.** The **graded adjoint** of the graded action is the operator $\rho_a^\dagger$ characterised by
$$
\langle\rho_am,n\rangle_M=(-1)^{|a||m|}\,\langle m,\rho_a^\dagger n\rangle_M\quad\text{for all graded }m,n\in M .
$$

**Theorem.** The graded adjoint exists and is unique when the graded form is nondegenerate; it is anti-linear in $a$; and the map $a\mapsto\rho_a^\dagger$ is an anti-representation of $\mathcal{A}$,
$$
(\rho_a^\dagger)^\dagger=\rho_a,\qquad \rho_a^\dagger\rho_b^\dagger=\rho_{a*b}^\dagger ,
$$
so the graded adjoint action is the action of the transposed algebra.

**Proof.** Uniqueness is the nondegeneracy of the form; the anti-linearity is the conjugation of the form; the anti-representation property is the computation $(\rho_a\rho_b)^\dagger=\rho_b^\dagger\rho_a^\dagger$ and the estimate $\rho_a^\dagger\rho_b^\dagger=\rho_{a*b}^\dagger$ on the regular module, by the multiplicativity of the transposed multiplication $\Theta_c\Theta_d=\Theta_{c*d}$. The identification $\rho_a^\dagger=\Theta_{\text{transpose}(a)}$ is the standard algebra-anti-isomorphism of the adjointable operators.

## The Cancellation

**Theorem (the cancellation of the Koszul sign).** On the regular module with the coefficient form,
$$
\rho_a^\dagger=\Theta_a\quad\text{for every }a\in\mathcal{A},
$$
independently of the parity of $a$; that is, the Koszul sign of the definition cancels the grade involution of the graded action exactly, and the graded adjoint action is the plain transposed multiplication.

**Proof.** The graded action of $a$ factors as $\rho_a=(-1)^{|a||m|}a\cdot m$; bringing the factor $(-1)^{|a||m|}$ to the left of the form and using that the coefficient form is graded, $\langle am,n\rangle=\langle m,\Theta_an\rangle$, gives $\rho_a^\dagger=\Theta_a$. The sign is its own inverse and appears on both sides of the defining identity. This is the graded version of the computation of *The Adjoint of the Left Multiplication on the Algebra of Arithmetic Functions*.

**Corollary (the parity operator).** The parity operator $P$ of the grading, $P|_{M_i}=(-1)^i$, is self-adjoint for every graded nondegenerate form, $P^\dagger=P$, and it commutes with the graded adjoint action: $P\rho_a^\dagger=\rho_{\alpha(a)}^\dagger P$. The graded adjoint action carries the grading through the grade involution of the parameter.

**Proof.** The parity operator acts on the two homogeneous components by $\pm1$, so it is self-adjoint for a graded form because the form is diagonal in the grading; the commutation is the identity $\Theta_{\alpha(a)}=\alpha\Theta_a\alpha$ combined with the action of $P$.

## The Comparison with the Involution

**Theorem.** The graded adjoint action is not the graded action of a transformed element: on the regular module
$$
\rho_a^\dagger=\Theta_a\ne\rho_{a^*}=L_{a^*}\quad\text{unless }a=\gamma\varepsilon ,
$$
and
$$
\rho_a^\dagger=\varepsilon(a)\,\rho_{a^{\ddagger}}
$$
with the super-transpose element $a^{\ddagger}$ holds only on the free graded modules and not on the regular module, where the multiplication by an element is a left multiplication and the adjoint is a transposed multiplication. The structures that the grading and the adjoint put on the module therefore decouple on the regular module.

**Proof.** The comparison is the criterion $\Theta_a=L_b\iff a=\gamma\varepsilon$, $b=\bar\gamma\varepsilon$, and the super-transpose formula holds when the module is free and the form is the standard super-form, by the graded analogue of the transpose of a matrix; on the regular module the two sides are different operations. This is the same obstruction as in *The Signed Adjoint of the Left Multiplication on the Algebra of Arithmetic Functions*.

## Worked Examples

**Example (the parity operator).** $P=\alpha$ on the regular module, and $P^\dagger=P$; the parity operator is the degree operator of the category, self-adjoint and unitary.

**Example (an even element).** For $a$ even, $\rho_a=L_a$ and $\rho_a^\dagger=\Theta_a$; the graded adjoint reduces to the plain adjoint.

**Example (an odd element).** For $a$ odd, $\rho_a=L_a\alpha$ and $\rho_a^\dagger=\Theta_a$; the grade involution disappears from the graded adjoint, which is the plain transposed multiplication, whereas the plain adjoint of the same operator is $\alpha\Theta_a$.

**Example ($a=\delta_p$).** $T_{\delta_p}^\dagger=\Theta_{\delta_p}=S_p$, the section-division pair, with $S_pD_p=\mathrm{id}$ and $D_pS_p=P_p$; the graded adjoint of the isometry $\alpha D_p$ is the division operator.

## Failure of the Degenerate Cases

The graded adjoint action fails in four degenerate configurations. First, the Koszul sign cancels the grade involution on the regular module, so the graded adjoint action carries no grading: the map $a\mapsto\rho_a^\dagger$ is the same $\Theta_a$ for the even and the odd elements, and the super-structure is invisible. Second, the graded adjoint action is defined only for the nondegenerate graded forms; on a degenerate form the adjoint does not exist uniquely, and the module must be replaced by its reflexive hull. Third, the super-transpose formula holds on the free modules and fails on the regular module, exactly as the matrix transpose formula fails for the convolution operators; the failure is the commutativity of the algebra. Fourth, on the finitely supported functions the graded adjoint action is unbounded for a general element, and it must be taken on the weighted spaces of the category. These are the boundary cases of the graded adjoint action.

## Summary

On a graded module over the algebra of arithmetic functions with a graded Hermitian form, the graded action is the Koszul-signed multiplication $\rho_a(m)=(-1)^{|a||m|}a\cdot m$, and its graded adjoint is characterised by $\langle\rho_am,n\rangle=(-1)^{|a||m|}\langle m,\rho_a^\dagger n\rangle$; on the regular module the graded adjoint is the plain transposed multiplication $\rho_a^\dagger=\Theta_a$ for every element, of either parity, the Koszul sign cancelling the grade involution exactly. The graded adjoint action is an anti-representation, $(\rho_a^\dagger)^\dagger=\rho_a$ and $\rho_a^\dagger\rho_b^\dagger=\rho_{a*b}^\dagger$; the parity operator is self-adjoint; and the graded adjoint action is not the graded action of a transformed element unless the element is a scalar multiple of the identity. The degenerate cases are the cancellation of the sign, the degenerate forms, the failure of the super-transpose formula and the unboundedness.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M=M_0\oplus M_1$ | Graded module |
| $\langle\cdot,\cdot\rangle_M$ | Graded Hermitian form |
| $\rho_a(m)=(-1)^{|a||m|}a\cdot m$ | Graded action |
| $\rho_a\rho_b=(-1)^{|a||b|}\rho_{ab}$ | Koszul identity |
| $\langle\rho_am,n\rangle=(-1)^{|a||m|}\langle m,\rho_a^\dagger n\rangle$ | Graded adjoint |
| $\rho_a^\dagger=\Theta_a$ | The cancellation |
| $(\rho_a^\dagger)^\dagger=\rho_a$ | Adjoint of the adjoint |
| $\rho_a^\dagger\rho_b^\dagger=\rho_{a*b}^\dagger$ | Anti-representation |
| $P^\dagger=P$ | Self-adjoint parity operator |
| $a^{\ddagger}$ | Super-transpose element |

## Further Reading

- Pierre Deligne and John Morgan, *Notes on Supersymmetry* (American Mathematical Society, 1999), for the Koszul sign and the graded modules.
- Yuri Manin, *Gauge Field Theory and Complex Geometry* (Springer, 1988), for the graded algebras and their modules.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the transposed multiplication and the adjoint.
- Tsit Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for the graded rings and the super-transpose.
- Paul Halmos, *A Hilbert Space Problem Book* (Springer, 1982), for the adjointable operators and the parity operator.
