
# __The Graded Action on a Module over the Algebra of Random Variables__

## Introduction

The algebra of random variables carries a grading, its even part the random variables fixed by the grade involution and its odd part those negated by it, and the signed operators of this category are the components of a **graded action**: an algebra element of degree $|a|$ acts on a graded module by multiplication with the Koszul sign $(-1)^{|a||m|}$,
$$
\rho_a(m)=(-1)^{|a||m|}\,a\cdot m .
$$
On the algebra read as a module over itself the graded action is the unsigned left multiplication for an even element and the signed left multiplication for an odd one, so the graded action packages the two families of the preceding articles into one graded representation. This article defines the graded module and the graded action, proves the product law with its Koszul sign, identifies the regular module and the Hilbert module of the category, computes the adjoint of the graded action with respect to the form of the category, and shows that the Koszul sign in the adjoint cancels, leaving the plain adjoint $\rho_a^*=\rho_{\delta(a)}$ with $\delta=\sigma\alpha$. The cancellation is the graded form of the agreement between the involution and the adjoint that the invariance of the expectation form produces, and it is the reason the graded action over the algebra of random variables behaves as the noncommutative theory dictates while the arithmetic one does not.

The conventions are those of *The Signed Sandwich on the Algebra of Random Variables*, earlier in this category: $\mathcal{A}=L^\infty(\Omega,\mathcal F,\mathbb P)$ with the pointwise product, the conjugation $\sigma(x)=\bar x$, the state $\varphi(x)=\mathbb E[x]$, the form $\langle x,y\rangle=\varphi(xy^*)$ on $\mathcal{H}=L^2(\Omega,\mathbb P)$, the grade involution $\alpha$, the grading $\mathcal{A}=\mathcal{A}_{\bar0}\oplus\mathcal{A}_{\bar1}$, and the twisted involution $\delta=\sigma\alpha$. The graded action over the algebra of arithmetic functions, whose Koszul signs behave differently, is *The Graded Action on a Module over the Algebra of Arithmetic Functions*, written; the graded action over a ring is *The Graded Action on a Module over a Ring*, in Part I; the signed left multiplication is the preceding article of this category, and the adjoint of the unsigned left multiplication is *The Adjoint of the Left Multiplication on the Algebra of Random Variables*, later in this category. No physics is invoked.

Throughout, $\mathcal{A}$ is the algebra of random variables with its grading $\mathcal{A}=\mathcal{A}_{\bar0}\oplus\mathcal{A}_{\bar1}$, the degree of a homogeneous element is written $|a|\in\mathbb{Z}/2$, and a **graded module** is a module $M=M_{\bar0}\oplus M_{\bar1}$ over $\mathcal{A}$ with $\mathcal{A}_{\bar i}\cdot M_{\bar j}\subseteq M_{\overline{i+j}}$. The form on the regular module is the form of the category, and the Hilbert module is $\mathcal{H}=L^2(\Omega,\mathbb P)$ with the same form.

## The Graded Action

### Definition

**Definition.** Let $M$ be a graded module over the graded algebra $\mathcal{A}$. For a homogeneous $a\in\mathcal{A}$ and a homogeneous $m\in M$ of degrees $|a|,|m|$, the **graded action** is
$$
\rho_a(m)=(-1)^{|a||m|}\,a\cdot m ,
$$
extended linearly to all of $M$. Thus $\rho_a$ is the ordinary left action $m\mapsto a\cdot m$ for even $a$ and the signed action $m\mapsto a\cdot\alpha(m)$ for odd $a$, where $\alpha$ acts on $M$ by the grade involution of the module.

### The regular and the Hilbert modules

**Proposition (the regular module).** Let $M=\mathcal{A}$ with the product of $\mathcal{A}$ as the action and the grading of $\mathcal{A}$ as the module grading. Then
$$
\rho_a=L_a\ (|a|=0),\qquad \rho_a=L_a\alpha=T^\alpha_a\ (|a|=1),
$$
so the graded action of an even element is the unsigned left multiplication and that of an odd element is the signed left multiplication of the preceding article. On the whole algebra the two families together are the graded action.

*Proof.* For homogeneous $m$ the definition gives $\rho_a(m)=(-1)^{|a||m|}a\,m$, which is $am$ for even $a$ and $(-1)^{|m|}am=a\alpha(m)$ for odd $a$, since $\alpha(m)=(-1)^{|m|}m$ on the homogeneous $m$; the extension to a general $m$ is the linearity of $\alpha$.

**Proposition (the Hilbert module).** Let $M=\mathcal{H}=L^2(\Omega,\mathbb P)$ with the grading inherited from $\mathcal{A}$ and the same form. Then for every $a\in\mathcal{A}$ the graded action is bounded, $\|\rho_a\|\le\|a\|_\infty$, and it agrees with the regular action on the dense subspace $\mathcal{A}\subseteq\mathcal{H}$.

*Proof.* The multiplication by a bounded function is bounded with norm $\|a\|_\infty$, and the grade involution is unitary, so the product $\rho_a$ is bounded by $\|a\|_\infty$; the two actions agree on the dense subalgebra $\mathcal{A}$ by the definition of the extension.

### The product law

**Theorem (the Koszul sign).** For homogeneous $a,b\in\mathcal{A}$,
$$
\rho_a\rho_b=(-1)^{|a||b|}\rho_{ab}.
$$

*Proof.* For homogeneous $m$,
$$
\rho_a\rho_b(m)=(-1)^{|a||\,b\cdot m|+|b||m|}ab\,m=(-1)^{|a||b|+|a||m|+|b||m|}ab\,m,
$$
and
$$
(-1)^{|a||b|}\rho_{ab}(m)=(-1)^{|a||b|}(-1)^{|ab||m|}ab\,m=(-1)^{|a||b|+|a||m|+|b||m|}ab\,m,
$$
the same; the two agree on the homogeneous elements and hence on all of $M$.

**Corollary (commutativity of the graded action).** On the commutative algebra the graded actions commute pairwise,
$$
\rho_a\rho_b=\rho_b\rho_a ,
$$
because the Koszul sign is symmetric, $(-1)^{|a||b|}=(-1)^{|b||a|}$, and the algebra is commutative, $ab=ba$. The Koszul sign is visible in the product law $\rho_a\rho_b=(-1)^{|a||b|}\rho_{ab}$ and not in a failure of commutativity; the family of all graded actions is commutative, and the grading shows in the relation between the product and the composite.

*Proof.* The two products are $(-1)^{|a||b|}\rho_{ab}$ and $(-1)^{|b||a|}\rho_{ba}$, which are equal term by term; for homogeneous $a,b$ this is the computation of the product law, and the linear extension gives it in general.

### The parity operator

**Theorem (the parity operator).** The **parity operator** of the graded module is the involution $\epsilon$ with $\epsilon|_{M_{\bar0}}=\mathrm{id}$ and $\epsilon|_{M_{\bar1}}=-\mathrm{id}$; on the regular module it is the grade involution $\alpha$ itself. It satisfies
$$
\epsilon\rho_a\epsilon=(-1)^{|a|}\rho_a
$$
for homogeneous $a$.

*Proof.* On the regular module $\epsilon(m)=m_{\bar0}-m_{\bar1}=\alpha(m)$. For homogeneous $a$ and homogeneous $m$,
$$
\epsilon\rho_a\epsilon(m)=\epsilon\bigl((-1)^{|m|}(-1)^{|a||m|}a\,m\bigr)=(-1)^{|m|}(-1)^{|a||m|}(-1)^{|a|+|m|}am=(-1)^{|a||m|+|a|}am=(-1)^{|a|}\rho_a(m),
$$
using $2|m|=0$ in $\mathbb{Z}/2$; the two sides agree on the homogeneous elements and hence everywhere. The operator $\epsilon$ is the parity operator of the graded module, and $\rho_1=\mathrm{id}$.

## The Adjoint of the Graded Action

### The formula

**Theorem (the adjoint).** On the regular module with the form of the category, the adjoint of the graded action is
$$
\rho_a^*=\rho_{\delta(a)},\qquad \delta=\sigma\alpha=\alpha\sigma ,
$$
for every $a\in\mathcal{A}$.

*Proof.* For homogeneous $a$ the operator is $L_a$ when $a$ is even and $L_a\alpha=T^\alpha_a$ when $a$ is odd. For even $a$, $\rho_a^*=L_a^*=L_{a^*}=\rho_{a^*}$ and $\delta(a)=\alpha(a^*)=a^*$ because $a^*$ is even; for odd $a$, $\rho_a^*=(L_a\alpha)^*=T^\alpha_{\delta(a)}=\rho_{\delta(a)}$ by the adjoint of the signed left multiplication, using that $\delta(a)$ is odd. The two cases agree with the formula, and the linear extension gives it for every $a$.

### The cancellation of the Koszul sign

**Theorem (cancellation).** The Koszul sign that appears in the adjoint of a graded representation cancels on the regular module with the form of the category: the graded adjoint coincides with the ordinary adjoint of the operator $\rho_a$, and it is $\rho_{\delta(a)}$.

*Proof.* A graded representation with the product law $\rho_a\rho_b=(-1)^{|a||b|}\rho_{ab}$ has, in general, an adjoint carrying a Koszul sign, $\rho_a^*=(-1)^{|a|}\rho_{\delta(a)}$ or its negative according to the parity convention. On the regular module the operator $\rho_a$ is $L_a\alpha^{|a|}$ and the direct computation of the preceding theorem produces $\rho_{\delta(a)}$ with the sign $+1$; the reason is that the form of the category is invariant under the conjugation, so the adjoint of a multiplication is a multiplication and the parity enters through $\delta$ alone. The sign therefore cancels, and the graded adjoint is the plain adjoint.

### The two structures

**Corollary (the involution and the adjoint).** The involution on the elements, $a\mapsto a^*$, and the adjoint on the operators, $\rho_a\mapsto\rho_a^*=\rho_{\delta(a)}$, do not coincide in general:
$$
\rho_a^*=\rho_{a^*}\iff\delta(a)=a^*\iff\alpha(a)=a ,
$$
that is, exactly when $a$ is even. On the even part the two structures agree, $\rho_a^*=\rho_{a^*}$ for even $a$, and on the odd part they differ by the grade involution; the agreement on the even part is the $*$-representation property produced by the invariance of the form. The discrepancy is the graded form of the two-structure statement of the corpus, and the object that measures it is the twist $\delta$.

*Proof.* Since $\rho$ is injective, $\rho_{\delta(a)}=\rho_{a^*}$ is $\delta(a)=a^*$, and $\delta(a)=\alpha(a^*)$; this equals $a^*$ exactly when $\alpha(a^*)=a^*$, that is when $a^*$ is even, that is when $a$ is even. The injectivity of $\rho$ on the regular module is the injectivity of the left multiplication.

## The Graded Commutator

**Definition.** For homogeneous $a,b$ the **graded commutator** is
$$
[a,b]_{gr}=a\,b-(-1)^{|a||b|}b\,a .
$$

**Theorem.** On the commutative algebra
$$
[a,b]_{gr}=ab\bigl(1-(-1)^{|a||b|}\bigr),
$$
so the graded commutator vanishes when $a$ or $b$ is even, and for both odd it is $[a,b]_{gr}=2ab$, the anticommutator. The graded commutator is the obstruction to the graded action being a representation without the Koszul sign, and it vanishes on the even subalgebra, which is central.

*Proof.* Commutativity gives $ab=ba$, so $[a,b]_{gr}=ab(1-(-1)^{|a||b|})$; the factor $1-(-1)^{|a||b|}$ is zero unless both degrees are one, and then it is two.

## Worked Examples

**Example (the swap on two atoms).** Let $\Omega=\{\omega_-,\omega_+\}$ with the uniform probability and $\alpha(x_-,x_+)=(x_+,x_-)$. The even part is the diagonal, the odd part the antidiagonal. On the regular module the graded action of an even $a=(a,a)$ is $L_a$, and of an odd $a=(a,-a)$ is $T^\alpha_a$; the product of two odd graded actions is $\rho_a\rho_b=(-1)\rho_{ab}=-\rho_{ab}$, the Koszul sign, and the adjoint is $\rho_a^*=\rho_{\delta(a)}$ with $\delta(a_-,a_+)=(a_+^*,a_-^*)$.

**Example (the circle reflection).** Let $\Omega=\mathbb R/\mathbb Z$ with the Lebesgue measure and $\alpha(x)(\theta)=x(-\theta)$. The even functions are the symmetric ones, the odd the antisymmetric; for odd $a$ the graded action is $T^\alpha_a$ and the adjoint is $T^\alpha_{\delta(a)}$, with $\delta(a)(\theta)=a(-\theta)^*$ equal to the reflection composed with the conjugation. The two structures differ on every odd $a$ that is not $\alpha$-Hermitian.

**Example (the trivial grading).** For $\alpha=\mathrm{id}$ the odd part is zero, the Koszul sign is always $+1$, the product law is $\rho_a\rho_b=\rho_{ab}$, the adjoint is $\rho_a^*=\rho_{a^*}$, and the graded action is the ordinary multiplication; this is the boundary at which the graded representation is an ungraded one and the two structures coincide.

## Failure of the Degenerate Cases

The graded action degenerates in four configurations. First, the Koszul sign cancels in the adjoint, so the graded theory over the algebra of random variables does not exhibit the twisted adjoint that the general graded representation carries; the cancellation is caused by the invariance of the form, and the arithmetic case, with the coefficient form, keeps the twist visible. Second, the commutativity of the algebra makes the graded commutator a scalar multiple of the product, $2ab$ for two odd elements, and the graded Lie structure is exhausted by the product; nothing beyond the multiplication is seen. Third, the two structures agree on the even subalgebra and differ on the odd part by $\alpha$, so the only obstruction to a $*$-representation is the grade involution; when $\alpha=\mathrm{id}$ there is no obstruction and the graded theory collapses to the unsigned one. Fourth, the Hilbert module is bounded only for the multipliers in $\mathcal{A}=L^\infty$, and an unbounded multiplier has no graded action on $\mathcal{H}$; the boundedness of the random variables is the hypothesis that makes the module a Hilbert module rather than a formal one.

## Summary

A graded module over the algebra of random variables is a module $M=M_{\bar0}\oplus M_{\bar1}$ compatible with the grading of the algebra, and the graded action is $\rho_a(m)=(-1)^{|a||m|}a\cdot m$, which is the ordinary multiplication for even $a$ and the signed left multiplication for odd $a$; on the regular module the two families of the preceding articles are the two halves of the graded action, and on the Hilbert module the action is bounded by $\|a\|_\infty$. The product law is $\rho_a\rho_b=(-1)^{|a||b|}\rho_{ab}$ with the Koszul sign, and the parity operator $\epsilon$ satisfies $\epsilon\rho_a\epsilon=(-1)^{|a|}\rho_a$. The adjoint with respect to the form of the category is $\rho_a^*=\rho_{\delta(a)}$ with $\delta=\sigma\alpha$, the Koszul sign cancelling because the form is invariant under the conjugation; the involution on the elements and the adjoint on the operators therefore agree on the even part and differ on the odd part by $\alpha$, the two-structure statement of the corpus in graded form. The graded commutator is $[a,b]_{gr}=ab(1-(-1)^{|a||b|})$, equal to $2ab$ for two odd elements and vanishing on the even subalgebra. The unsigned adjoint is *The Adjoint of the Left Multiplication on the Algebra of Random Variables*, later in this category, and the graded action in the arithmetic case is *The Graded Action on a Module over the Algebra of Arithmetic Functions*, written.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M=M_{\bar0}\oplus M_{\bar1}$ | a graded module over the graded algebra $\mathcal{A}$ |
| $|a|,|m|$ | degrees in $\mathbb{Z}/2$ |
| $\rho_a(m)=(-1)^{|a||m|}a\cdot m$ | the graded action |
| $\rho_a=L_a\ (|a|=0)$, $\rho_a=T^\alpha_a\ (|a|=1)$ | the regular module |
| $\rho_a\rho_b=(-1)^{|a||b|}\rho_{ab}$ | the Koszul product law |
| $\epsilon$ | the parity operator, $\epsilon\rho_a\epsilon=(-1)^{|a|}\rho_a$ |
| $\rho_a^*=\rho_{\delta(a)}$, $\delta=\sigma\alpha$ | the adjoint; the Koszul sign cancels |
| $[a,b]_{gr}=ab-(-1)^{|a||b|}ba$ | the graded commutator |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Vol. I (Academic Press, 1983), for the representations and the adjoints of a graded algebra.
- Jacques Dixmier, *C*-Algebras* (North-Holland, 1977), for the involutions, the twisted representations and the graded tensor products.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the graded involutions and the Koszul signs.
- Yuri I. Manin, *Gauge Field Theory and Complex Geometry* (Springer, 1988), for the graded modules, the Koszul sign rule and the graded commutator.
- Pierre Deligne and John W. Morgan, "Notes on supersymmetry (following Joseph Bernstein)", in *Quantum Fields and Strings*, Vol. 1 (American Mathematical Society, 1999), for the Koszul sign convention in graded algebra.
