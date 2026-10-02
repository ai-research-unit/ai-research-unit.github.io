
# __The Graded Adjoint Action on a Module over the Algebra of Random Variables__

## Introduction

A graded module over the algebra of random variables is a module split into an even and an odd part, $M=M_{\bar0}\oplus M_{\bar1}$, on which the graded algebra acts by the **graded action** $\rho$, linear on each part and satisfying the Koszul sign rule
$$
\rho_a\rho_b=(-1)^{|a||b|}\rho_{ab},\qquad \rho_\varepsilon=\mathrm{id} ,
$$
where $|a|$ is the parity of $a$. This article builds the **graded adjoint** of that action: with respect to a graded, nondegenerate form on $M$, the adjoint $\rho_a^\dagger$ is defined by
$$
\langle\rho_a x,y\rangle=(-1)^{|a||x|}\langle x,\rho_a^\dagger y\rangle ,
$$
it is anti-linear in the parameter $a$, the map $a\mapsto\rho_a^\dagger$ is an anti-representation of the graded algebra, and on the regular module with the form of the category the Koszul sign **cancels** and the graded adjoint is the graded action of the twisted image,
$$
\rho_a^\dagger=\rho_{\delta(a)},\qquad \delta=\sigma\alpha ,
$$
the graded action adjoint being a graded action after all. The article gives the data, the representation law, the adjoint, the cancellation of the Koszul sign, the self-adjointness of the parity operator, and the comparison with the involution on the elements; the graded action itself, without the adjoint, is *The Graded Action on a Module over the Algebra of Random Variables*, earlier in this category, and the adjoint of the signed left multiplication, the odd generator of the action, is *The Signed Adjoint of the Left Multiplication on the Algebra of Random Variables*, the preceding article of this category.

The conventions are those of the category: $\mathcal{A}=L^\infty(\Omega,\mathcal F,\mathbb P)$ with the pointwise product, the conjugation $\sigma(a)=\bar a$, the state $\varphi(a)=\mathbb E[a]$, the form of the category $\langle x,y\rangle=\varphi(xy^*)$, the grade involution $\alpha$, the grading $\mathcal{A}=\mathcal{A}_{\bar0}\oplus\mathcal{A}_{\bar1}$ and the twisted involution $\delta=\sigma\alpha$, as fixed in *The Signed Sandwich on the Algebra of Random Variables*, earlier in this category. The graded module and the graded action are *The Graded Action on a Module over the Algebra of Random Variables*, earlier in this category; the signed left multiplication is *The Signed Left Multiplication on the Algebra of Random Variables*, earlier in this category, and its adjoint is *The Signed Adjoint of the Left Multiplication on the Algebra of Random Variables*, the preceding article of this category; the signed sandwiches and their adjoints are *The Signed Adjoint Sandwich on the Algebra of Random Variables*, earlier in this category; the operator-algebra involution is *The Involution on the Operator Algebra of a Process*, earlier in this category. The graded adjoint action over a general graded ring is *The Graded Adjoint Action on a Module over a Graded Algebra*, written, and the arithmetic counterpart is *The Graded Adjoint Action on a Module over the Algebra of Arithmetic Functions*, written. No physics is invoked.

Throughout, $\mathcal{A}$ is the graded algebra of random variables, $M=M_{\bar0}\oplus M_{\bar1}$ is a graded module, $\rho_a$ is the graded action of $a$, $\langle\cdot,\cdot\rangle$ is a graded form on $M$ (vanishing between the opposite parities), and $\delta=\sigma\alpha$. The regular module is $M=\mathcal{H}=L^2(\Omega,\mathbb P)$ with the form of the category.

## The Graded Module and the Graded Action

### The data

**Definition.** A **graded module** over $\mathcal{A}$ is a module $M$ with a decomposition $M=M_{\bar0}\oplus M_{\bar1}$ such that $\mathcal{A}_{\bar i}M_{\bar j}\subseteq M_{\overline{i+j}}$; the **graded action** is the homomorphism $\rho:\mathcal{A}\to\mathrm{End}(M)$ with
$$
\rho_a(m)=(-1)^{|a||m|}a\cdot m
$$
on the homogeneous elements, extended by linearity.

**Theorem (the representation law).** The graded action is a representation of the graded algebra,
$$
\rho_a\rho_b=(-1)^{|a||b|}\rho_{ab},\qquad \rho_\varepsilon=\mathrm{id},\qquad \rho_a(M_{\bar j})\subseteq M_{\overline{|a|+j}} ,
$$
and on a homogeneous element $\rho_a$ is an isomorphism of the graded pieces.

*Proof.* Apply the definition twice: $\rho_a\rho_b(m)=(-1)^{|a|(|b|+|m|)}a\cdot((-1)^{|b||m|}b\cdot m)=(-1)^{|a||b|}(-1)^{(|a|+|b|)|m|}ab\cdot m=(-1)^{|a||b|}\rho_{ab}(m)$, and $\rho_\varepsilon=I$; the preservation of the grading is the inclusion $\mathcal{A}_{\bar i}M_{\bar j}\subseteq M_{\overline{i+j}}$.

### The graded form

**Theorem (the form is graded).** The form of the category on the regular module $\mathcal{H}=L^2(\Omega,\mathbb P)$ is graded, $\langle x_{\bar i},y_{\bar j}\rangle=0$ for $i\ne j$, and on the regular module the graded action is the signed left multiplication for the odd parameters and the ordinary left multiplication for the even ones,
$$
\rho_a=\begin{cases}L_a,&|a|=\bar0,\\ T^\alpha_a=L_a\alpha,&|a|=\bar1.\end{cases}
$$

*Proof.* The even and the odd parts of $L^2$ are orthogonal for the form because the expectation of a product of opposite parities vanishes, $\varphi(x_{\bar0}y_{\bar1}^*)=0$ by the parity of the measure-preserving involution; the identification of the action is the definition of the grading on the regular module, where the odd parameters act with the grade involution inserted.

## The Graded Adjoint

### Definition and the anti-representation

**Definition.** Let $\langle\cdot,\cdot\rangle$ be a graded form on $M$. The **graded adjoint** of $\rho_a$ is the operator $\rho_a^\dagger$ with
$$
\langle\rho_a x,y\rangle=(-1)^{|a||x|}\langle x,\rho_a^\dagger y\rangle\qquad\text{for all homogeneous }x,y.
$$

**Theorem (existence and the anti-representation).** If the graded form is nondegenerate, the graded adjoint exists and is unique for every $a$; it is anti-linear in $a$,
$$
(\rho_{\lambda a+\mu b})^\dagger=\bar\lambda\rho_a^\dagger+\bar\mu\rho_b^\dagger ,
$$
and the map $a\mapsto\rho_a^\dagger$ is an anti-representation of the graded algebra,
$$
(\rho_a\rho_b)^\dagger=(-1)^{|a||b|}\rho_b^\dagger\rho_a^\dagger .
$$

*Proof.* The adjoint is defined by the nondegeneracy of the form, which gives a conjugate-linear isomorphism $M\to M^*$; the anti-linearity in $a$ is the conjugate-linearity of the defining identity; the anti-representation is the computation $\langle\rho_a\rho_b x,y\rangle=(-1)^{|a||b|}\langle x,\rho_b^\dagger\rho_a^\dagger y\rangle$ using the sign rule twice.

### The cancellation of the Koszul sign

**Theorem (the cancellation).** On the regular module with the form of the category the Koszul sign of the graded adjoint cancels and the graded adjoint of a homogeneous element is the graded action of the **twisted image**,
$$
\rho_a^\dagger=\rho_{\delta(a)},\qquad \delta=\sigma\alpha=\alpha\sigma ,
$$
so the graded adjoint action is the graded action after all, and the map $\delta$ is an isomorphism of the graded algebra.

*Proof.* For the even $a$ the operator is $L_a$, whose adjoint is $L_{a^*}=L_{\delta(a)}$ with $\delta(a)=a^*$, an even element, and the sign $(-1)^{|a||x|}=1$ vanishes; for the odd $a$ the operator is $T^\alpha_a=L_a\alpha$, whose adjoint is $T^\alpha_{\delta(a)}$ by *The Signed Adjoint of the Left Multiplication on the Algebra of Random Variables*, the preceding article, and the Koszul sign $(-1)^{|a||x|}$ cancels against the grade involution inserted in $T^\alpha_{\delta(a)}$. Both are the graded action of $\delta(a)$; the map $\delta$ is an involutive automorphism because $\sigma$ and $\alpha$ commute and each is involutive.

**Corollary (the fixed elements).** The graded adjoint action fixes the $\delta$-invariant elements, and the graded action of $a$ is self-adjoint for the graded form exactly when $a=\delta(a)$, that is when $a$ is $\alpha$-Hermitian.

*Proof.* The adjoint is $\rho_{\delta(a)}$, which equals $\rho_a$ exactly when $a=\delta(a)$; the injectivity of the graded action on the regular module gives the criterion, and $\alpha$-Hermiticity is the identity $\alpha(a)=a^*$.

### The parity operator

**Theorem (the parity operator).** The parity operator $P$ with $P|_{M_{\bar i}}=(-1)^i$ is self-adjoint for every graded nondegenerate form, $P^\dagger=P$, and it commutes with the graded adjoint action in the sense
$$
P\rho_a^\dagger=\rho_{\alpha(a)}^\dagger P ,
$$
so the graded adjoint action carries the grading through the grade involution of the parameter.

*Proof.* The parity operator is an involution of the graded form and a self-adjoint operator because it is a self-adjoint projection up to sign on each graded piece; the commutation is the computation of the parity of $\rho_a^\dagger$ and the definition of $\alpha$ on the parameters.

## The Comparison with the Involution

**Theorem (the involution and the graded adjoint).** On the regular module the graded adjoint is the graded action of the twisted image $\delta(a)$, so it is not the graded action of a **transformed element** in the sense of the plain involution: the element is $\delta(a)=\alpha(a^*)$, and the involutions $\sigma$ and $\alpha$ both enter. Only when the grading is trivial, $\alpha=\mathrm{id}$, is the graded adjoint the graded action of the conjugate, $\sigma(a)=a^*$.

*Proof.* The cancellation theorem gives $\rho_a^\dagger=\rho_{\delta(a)}$, and $\delta=\sigma\alpha$; the case $\alpha=\mathrm{id}$ reduces $\delta$ to $\sigma$, which is *The Adjoint of the Left Multiplication on the Algebra of Random Variables*, earlier in this category.

**Corollary (the comparison with the arithmetic case).** Over the algebra of arithmetic functions the graded adjoint action is not the graded action of a transformed element in general, because the coefficient form is not invariant under the multiplication and the transposed multiplication is not a left multiplication; here the invariance of the expectation form makes the graded adjoint a graded action, and the difference is exactly the traciality of the state.

*Proof.* The arithmetic statement is that of *The Graded Adjoint Action on a Module over the Algebra of Arithmetic Functions*, written, and the comparison is the invariance of the form.

## Worked Examples

**Example (the two-atom module).** For $\Omega=\{\omega_-,\omega_+\}$ with the uniform probability the regular module splits into the even and the odd functions, and the graded action of the even element $a=(a_-,a_+)$ with $a_-=a_+$ is the diagonal multiplication; the graded action of the odd element with $a_-=-a_+$ is the swap multiplied by the diagonal; the graded adjoint is the graded action of $\delta(a)=(\bar a_+,\bar a_-)$, matching the direct computation of the preceding article.

**Example (the circle grading).** On $\Omega=\mathbb R/\mathbb Z$ with the Lebesgue measure and $\alpha(x)(\theta)=x(-\theta)$, the even and the odd functions are orthogonal for the form, and the parameter $a(\theta)=e^{2\pi i\theta}$ is odd with $\delta(a)=a$; the graded adjoint of $\rho_a$ is $\rho_a$ itself, so $\rho_a$ is self-adjoint and unitary, the involution $x(\theta)\mapsto e^{2\pi i\theta}x(-\theta)$ of the circle.

**Example (the trivial grading).** For $\alpha=\mathrm{id}$ the graded module is the ungraded one, the Koszul signs are all $1$, the graded adjoint is $\rho_{\sigma(a)}$ and the graded action is the ordinary left multiplication; this is the boundary at which the graded adjoint action is the module form of *The Adjoint of the Left Multiplication on the Algebra of Random Variables*, earlier in this category.

**Example (the parity operator).** On the regular module the parity operator $P$ is the multiplication by the sign of the parity, a self-adjoint unitary involution for the graded form; it commutes with the graded adjoint action through $\alpha$, $P\rho_a^\dagger=\rho_{\alpha(a)}^\dagger P$, which for the trivial grading is the plain commutation of $P$ with the left multiplications.

## Failure of the Degenerate Cases

The graded adjoint action degenerates in four configurations. First, the graded adjoint exists only when the graded form is nondegenerate; on a degenerate form the adjoint is defined only up to the radical, and the anti-representation fails. Second, the Koszul sign cancels on the regular module with the form of the category, and the temptation to drop the sign in general is the error the graded theory corrects: on a module with a non-invariant form the sign survives and the graded adjoint is not a graded action. Third, the graded action of an odd element is the signed left multiplication, whose products are the **unsigned** left multiplications; the class of the graded operators is closed under the adjoint but not under multiplication, so the anti-representation is of the graded algebra and not of a group. Fourth, the self-adjointness of the graded action is the $\alpha$-Hermiticity of the parameter, not the reality; the graded operators can be self-adjoint without being real, and the trivial grading is the boundary at which the two agree.

## Summary

The graded action of a graded module over the algebra of random variables is the representation $\rho_a(m)=(-1)^{|a||m|}a\cdot m$ satisfying the Koszul sign rule $\rho_a\rho_b=(-1)^{|a||b|}\rho_{ab}$, and on the regular module it is the ordinary left multiplication for the even parameters and the signed left multiplication $T^\alpha_a=L_a\alpha$ for the odd ones. Its **graded adjoint** $\rho_a^\dagger$, defined by $\langle\rho_a x,y\rangle=(-1)^{|a||x|}\langle x,\rho_a^\dagger y\rangle$, exists and is unique for a nondegenerate graded form, is anti-linear in $a$ and is an anti-representation, $(\rho_a\rho_b)^\dagger=(-1)^{|a||b|}\rho_b^\dagger\rho_a^\dagger$. On the regular module with the form of the category the Koszul sign **cancels** and the graded adjoint is the graded action of the twisted image, $\rho_a^\dagger=\rho_{\delta(a)}$ with $\delta=\sigma\alpha$, so the graded adjoint action is a graded action; it is self-adjoint exactly for the $\alpha$-Hermitian parameters, and the parity operator is self-adjoint and carries the grading through the grade involution, $P\rho_a^\dagger=\rho_{\alpha(a)}^\dagger P$. The graded adjoint is the graded action of a transformed element here because the form is invariant, which fails over the arithmetic algebra; the graded action itself is *The Graded Action on a Module over the Algebra of Random Variables*, earlier in this category, and the adjoint of its odd generator is *The Signed Adjoint of the Left Multiplication on the Algebra of Random Variables*, the preceding article of this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M=M_{\bar0}\oplus M_{\bar1}$ | the graded module |
| $\rho_a(m)=(-1)^{|a||m|}a\cdot m$ | the graded action |
| $\rho_a\rho_b=(-1)^{|a||b|}\rho_{ab}$ | the Koszul sign rule |
| $\langle\rho_a x,y\rangle=(-1)^{|a||x|}\langle x,\rho_a^\dagger y\rangle$ | the graded adjoint |
| $(\rho_a\rho_b)^\dagger=(-1)^{|a||b|}\rho_b^\dagger\rho_a^\dagger$ | the anti-representation |
| $\rho_a^\dagger=\rho_{\delta(a)}$ | the cancellation of the Koszul sign |
| $a=\delta(a)$ | self-adjointness of the graded action |
| $P$, $P\rho_a^\dagger=\rho_{\alpha(a)}^\dagger P$ | the parity operator |

## Further Reading

- Pierre Deligne and John Morgan, *Notes on Supersymmetry* (American Mathematical Society, 1999), for the Koszul sign and the graded modules.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the graded operators, their adjoints and the sign rules.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the graded algebras, the graded actions and the twisted involutions.
- Jacques Dixmier, *C*-Algebras* (North-Holland, 1977), for the involutions, the graded structures and the representations.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Vol. I (Academic Press, 1983), for the adjoints, the projections and the $*$-representations.
