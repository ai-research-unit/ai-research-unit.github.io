
# __The Graded Action on a Module over the Algebra of Arithmetic Functions__

## Introduction

Let $\mathcal{A}$ be the algebra of arithmetic functions under Dirichlet convolution, graded by the parity of $\Omega$, the number of prime factors counted with multiplicity, and let $M$ be a graded module over $\mathcal{A}$. The **graded action** of a homogeneous element $a$ on a homogeneous element $m$ carries the Koszul sign, $\rho_a(m)=(-1)^{|a||m|}a\cdot m$; it is the action that appears whenever a graded algebra acts on a graded object, and it is the form in which the algebra of arithmetic functions acts on the graded objects of analytic number theory. The purpose of this article is to state the action, to compute its products and its adjoints, to say exactly when it is a representation and when it is only a projective one, and to identify the point at which the commutative algebra of arithmetic functions makes the graded structure degenerate. The two principal questions are the sign in the product law and the relation between the involution on the elements and the adjoint on the operators; both answers are sharp over a commutative algebra.

The conventions are those fixed for the category. The algebra $\mathcal{A}$ is $\mathbb{Z}/2$-graded by the parity of $\Omega$, $\alpha(f)=\lambda f$ is the grade involution, $\sigma(f)=\overline{f}$ is the coefficient involution, and $\delta=\sigma\alpha$. The form of the category on the regular module is the coefficient form $\langle f,g\rangle=\sum_nf(n)\overline{g(n)}$. The signed one-sided and two-sided operators on the regular module are treated in *The Signed Left Multiplication on the Algebra of Arithmetic Functions* and *The Signed Sandwich on the Algebra of Arithmetic Functions*, this category. Nothing here reads a distance as an object.

## The Graded Action

### Definition

**Definition.** A **graded module** over $\mathcal{A}$ is an $\mathcal{A}$-module $M$ with a decomposition $M=M_{\bar0}\oplus M_{\bar1}$ such that $\mathcal{A}_{\bar i}\cdot M_{\bar j}\subseteq M_{\overline{i+j}}$. For homogeneous $a\in\mathcal{A}$ and $m\in M$ of degrees $|a|,|m|\in\mathbb{Z}/2$, the **graded action** is
$$
\rho_a(m)=(-1)^{|a||m|}\,a\cdot m,
$$
extended by linearity.

**Proposition (the regular and the Hilbert modules).** The algebra $\mathcal{A}$ is a graded module over itself with $M=\mathcal{A}$ and the product of $\mathcal{A}$, and $\rho_a$ is then the signed left multiplication $T_a$ for odd $a$ and the ordinary left multiplication $L_a$ for even $a$. The space $\mathcal{H}=\ell^2$ is a graded module for the same grading, and $\rho_a$ is bounded on $\mathcal{H}$ for $a\in\ell^1$.

**Proof.** Both statements are the definition; the degree of $\alpha(f)$ is $|f|+1$, since $\lambda$ is odd at each prime, and this is what makes the graded action differ from the ordinary one exactly on the odd elements.

### The product law

**Theorem.** For homogeneous $a,b$ and every $m$,
$$
\rho_a\rho_b(m)=(-1)^{|a||b|}\rho_{a*b}(m).
$$
Hence the graded action is a representation of $\mathcal{A}$ if and only if $(-1)^{|a||b|}=1$ for all pairs arising from the module; in general it is a projective representation with cocycle $(-1)^{|a||b|}\in\{\pm1\}$. If $\mathcal{A}$ carried the Koszul sign in its own product, the two signs would cancel and the action would be a representation; the commutative algebra does not, and this is the source of the discrepancy.

**Proof.** Compute
$$
\rho_a\rho_b(m)=(-1)^{|a|(|b|+|m|)+|b||m|}(ab)\cdot m,\qquad \rho_{a*b}(m)=(-1)^{(|a|+|b|)|m|}(ab)\cdot m,
$$
and divide; the exponent difference is $|a|(|b|+|m|)+|b||m|-(|a|+|b|)|m|=|a||b|$, which is the displayed sign. The representation case is the vanishing of the sign, and the cancellation remark is the definition of the Koszul sign in the product.

### The parity operator

**Theorem.** The action of $\varepsilon$ is the **parity operator**
$$
P=\rho_\varepsilon,\qquad P(m)=(-1)^{|m|}m .
$$
It is an involutive unitary operator on the graded module, it satisfies $P\rho_a=(-1)^{|a|}\rho_aP$, and on the regular module it is the grade involution, $P=\alpha$.

**Proof.** $\rho_\varepsilon(m)=(-1)^{|m|}\varepsilon\cdot m=(-1)^{|m|}m$. The commutation with $\rho_a$ is the sign computation $P\rho_a=(-1)^{|a|}\rho_aP$, which holds by the product law. The remaining statements are the properties of $\alpha$ on the regular module.

## The Adjoint of the Graded Action

### The formula

**Theorem.** On the regular module with the coefficient form, the adjoint of the graded action is
$$
\rho_a^*=\alpha^{|a|}\,\Theta_a ,
$$
that is $\rho_a^*=\Theta_a$ for even $a$ and $\rho_a^*=\alpha\Theta_a$ for odd $a$, where $\Theta_c$ is the transposed multiplication, $(\Theta_cg)(k)=\sum_m\overline{c(m)}g(mk)$.

**Proof.** For even $a$, $\rho_a=L_a$ and $L_a^*=\Theta_a$. For odd $a$, $\rho_a=L_a\alpha$ and $(L_a\alpha)^*=\alpha\Theta_a$, by the computation for the signed left multiplication. The display collects the two cases.

**Corollary (the two structures).** The involution on the elements, $a\mapsto a^*$, and the adjoint on the operators, $\rho_a\mapsto\rho_a^*$, do not coincide: in general $\rho_a^*$ is neither $\rho_{a^*}$ nor $\rho_{\alpha(a)}$. The equality $\rho_a^*=\rho_{a^*}$ holds for all $a$ only for the augmentation form, of rank one, and it fails for the coefficient form used here; this is the same obstruction as in *The Adjoint of the Left Multiplication on the Algebra of Arithmetic Functions*. In the graded setting the two structures are independent, and the article proves their relation rather than assuming it.

### The graded commutator

**Definition.** The **graded commutator** of homogeneous elements is $[a,b]_{gr}=a*b-(-1)^{|a||b|}b*a$.

**Theorem.** In the commutative algebra $\mathcal{A}$,
$$
[a,b]_{gr}=a*b\bigl(1-(-1)^{|a||b|}\bigr)=
\begin{cases}0 & \text{if at least one of } a,b \text{ is even},\\ 2\,a*b & \text{if both are odd}.\end{cases}
$$
Hence $\mathcal{A}$ is graded-commutative exactly when its odd part consists of zero divisors of the even part, which is not the case; in particular the odd part carries a nonzero bracket and the graded algebra is not super-commutative.

**Proof.** Commutativity gives $b*a=a*b$, so the graded commutator is $a*b(1-(-1)^{|a||b|})$, and the factor is $0$ unless both degrees are odd, in which case it is $2$. Because $\mathcal{A}$ is an integral domain, $2ab\ne0$ for nonzero odd $a,b$.

## Worked Examples

**Example (the regular module).** $M=\mathcal{A}$, and the graded action of $\delta_p$ (odd, since $\Omega(p)=1$) is $\rho_{\delta_p}=L_{\delta_p}\alpha=T_{\delta_p}$, the signed left multiplication, an isometry of $\mathcal{H}$ with cokernel the functions vanishing on the multiples of $p$.

**Example (a module of rank one).** If $M=\mathcal{A}\cdot m$ with $m$ even, then the graded action of $a$ is $(-1)^{|a||m|}=1$ times $a\cdot m$, so the action is the ordinary one and the grading does not act; this is the degenerate module in which the Koszul sign is trivial.

**Example (the module of Dirichlet series).** The space of formal Dirichlet series with coefficients in $\mathbb{C}$ is a graded module over $\mathcal{A}$ by $M_h$, and the graded action of an odd $h$ is the signed multiplication $M_h\circ\alpha$; its adjoint is $\alpha\Theta_h$, so the adjoint of the graded multiplication by an odd element is not the graded multiplication by $h^*$.

## Failure of the Degenerate Cases

The graded action over the commutative algebra has four degenerate boundaries. First, the product law carries the nonzero cocycle $(-1)^{|a||b|}$ on the pairs of odd elements, so the action is not a representation but only a projective one; the cocycle is not a coboundary in general, and it cannot be removed by rescaling the action. Second, the graded commutator is twice the product on the odd part, so the algebra is not graded-commutative although it is commutative; the "graded" structure changes the answer by the factor $2$ and nothing else. Third, the module may fail to be graded and the grading of $M$ may be incompatible with the grading of $\mathcal{A}$; in that case the Koszul sign is not defined and the graded action reduces to the ordinary one. Fourth, the adjoint of the graded action is $\alpha^{|a|}\Theta_a$, which is a graded action only for the degenerate modules on which the grading is trivial; on the regular module the graded action of an odd element is not adjointable to a graded action of an element of $\mathcal{A}$. These four are the boundary cases of the graded family over a commutative algebra.

## Summary

For a graded module $M$ over the algebra of arithmetic functions, graded by the parity of $\Omega$, the graded action is $\rho_a(m)=(-1)^{|a||m|}a\cdot m$; it satisfies the projective product law $\rho_a\rho_b=(-1)^{|a||b|}\rho_{a*b}$, so it is a representation exactly when the Koszul sign is trivial on the relevant pairs, and it is the ordinary action on the even part. The action of $\varepsilon$ is the parity operator $P$, an involutive unitary operator commuting with $\rho_a$ up to the sign $(-1)^{|a|}$, equal to the grade involution on the regular module. The adjoint on the regular module with the coefficient form is $\rho_a^*=\alpha^{|a|}\Theta_a$, which is not the graded action of $a^*$; the involution on the elements and the adjoint on the operators are two independent structures. The graded commutator is $[a,b]_{gr}=2ab$ on the odd part and $0$ otherwise, so the commutative algebra is not graded-commutative, and the degenerate modules are those whose grading is trivial.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M=M_{\bar0}\oplus M_{\bar1}$ | Graded module |
| $\rho_a(m)=(-1)^{|a||m|}a\cdot m$ | Graded action |
| $\rho_a\rho_b=(-1)^{|a||b|}\rho_{a*b}$ | Projective product law |
| $P=\rho_\varepsilon$, $P(m)=(-1)^{|m|}m$ | Parity operator |
| $\rho_a^*=\alpha^{|a|}\Theta_a$ | Adjoint of the graded action |
| $[a,b]_{gr}=a*b-(-1)^{|a||b|}b*a$ | Graded commutator |
| $[a,b]_{gr}=2ab$ on the odd part | The graded commutator of $\mathcal{A}$ |
| $\alpha$, $\sigma$, $\delta=\sigma\alpha$ | The involutions |

## Further Reading

- Pierre Deligne and John Morgan, *Notes on Supersymmetry* (American Mathematical Society, 1999), for the Koszul sign and the graded modules.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the graded actions and the commutators.
- Charles Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Interscience, 1962), for the projective representations and the cocycles.
- Paul Halmos, *A Hilbert Space Problem Book* (Springer, 1982), for the parity operators and the graded Hilbert spaces.
- Tsit Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for the graded commutativity and the superalgebras.
