
# __The Signed Adjoint of the Left Multiplication on the Algebra of Random Variables__

## Introduction

The signed left multiplication is the product of the left multiplication by the grade involution,
$$
T^\alpha_a=L_a\alpha,\qquad T^\alpha_a(x)=a\,\alpha(x),
$$
and this article computes its **adjoint** with respect to the form of the category,
$$
\langle x,y\rangle=\varphi(xy^*)=\mathbb E\bigl[x\bar y\bigr].
$$
The adjoint is again a signed left multiplication,
$$
\bigl(T^\alpha_a\bigr)^*=T^\alpha_{\delta(a)}=\alpha\,L_{a^*},\qquad \delta=\sigma\alpha=\alpha\sigma ,
$$
the signed left multiplication by the **twisted image** $\delta(a)$ of the parameter, where $\delta$ is the composite of the conjugation and the grade involution. The formula is the same as in the noncommutative signed theory of *The Signed Left Multiplication on a Ring*, in Part I, but the derivation differs: there the twisted involution performs the reversal of the product, while here the product is commutative, the adjoint of the ordinary left multiplication is the left multiplication by the conjugate, and the twist $\delta$ on the parameter completes the computation. The article gives the closed form, the behaviour under products and squares, the conditions for self-adjointness, isometry and unitarity, and the comparison of the adjoint with the involution on the elements, which agree exactly up to the twisted involution $\delta$.

The conventions are those fixed in *The Signed Sandwich on the Algebra of Random Variables*, earlier in this category: $\mathcal{A}=L^\infty(\Omega,\mathcal F,\mathbb P)$ with the pointwise product, the conjugation $\sigma(a)=\bar a$, the state $\varphi(a)=\mathbb E[a]$, the form of the category $\langle x,y\rangle=\varphi(xy^*)$, the grade involution $\alpha$, the grading and the twisted involution $\delta=\sigma\alpha=\alpha\sigma$. The signed left multiplication and its products are *The Signed Left Multiplication on the Algebra of Random Variables*, earlier in this category; the signed sandwich, of which it is the case $b=1$, and its adjoint are *The Signed Sandwich on the Algebra of Random Variables*, earlier in this category, and *The Signed Adjoint Sandwich on the Algebra of Random Variables*, the preceding article of this category; the reflections and their adjoints are *Reflections as Signed Two-Sided Operators on the Algebra of Random Variables*, earlier in this category, and *The Signed Adjoint of the Reflection on the Algebra of Random Variables*, the preceding article of this category; the adjoint of the unsigned left multiplication is *The Adjoint of the Left Multiplication on the Algebra of Random Variables*, earlier in this category; the operator-algebra involution is *The Involution on the Operator Algebra of a Process*, earlier in this category; and the graded adjoint action is *The Graded Adjoint Action on a Module over the Algebra of Random Variables*, the next article of this category. No physics is invoked.

Throughout, $\mathcal{A}$ is the algebra of random variables, $\mathcal{H}=L^2(\Omega,\mathbb P)$ with the form $\langle x,y\rangle=\varphi(xy^*)$ is the Hilbert space of the category, $T^\alpha_a=L_a\alpha$ is the signed left multiplication, and $\delta=\sigma\alpha$; the twisted involution satisfies $\delta^2=\mathrm{id}$, $\delta\alpha=\alpha\delta=\sigma$ and $\delta\sigma=\sigma\delta=\alpha$.

## The Signed Adjoint

### Definition and closed form

**Definition.** The **signed adjoint** of the signed left multiplication is the operator $(T^\alpha_a)^*$ with
$$
\langle T^\alpha_a x,y\rangle=\langle x,(T^\alpha_a)^*y\rangle\qquad\text{for all }x,y\in\mathcal{H}.
$$

**Theorem (the closed form).** For every $a\in\mathcal{A}$,
$$
\bigl(T^\alpha_a\bigr)^*=T^\alpha_{\delta(a)}=\alpha\,L_{a^*},\qquad \delta=\sigma\alpha ,
$$
so the adjoint of a signed left multiplication is a signed left multiplication, of the twisted parameter.

*Proof.* The operator is $L_a\alpha$, and the adjoint of a product is the product of the adjoints in reverse order, $(L_a\alpha)^*=\alpha^*L_a^*$. By *The Adjoint of the Left Multiplication on the Algebra of Random Variables*, earlier in this category, $L_a^*=L_{a^*}$, and $\alpha^*=\alpha$ because the grade involution is self-adjoint; hence $(T^\alpha_a)^*=L_{a^*}\alpha$. Using $L_{a^*}\alpha=L_{\alpha(a^*)}\alpha^2=\alpha L_{a^*}$ and $\alpha(a^*)=\delta(a)$, this is $T^\alpha_{\delta(a)}$.

**Corollary (the adjoint is a signed left multiplication).** The adjoint operation preserves the class of the signed left multiplications and acts on the parameter by the twisted involution,
$$
T^\alpha_a\mapsto T^\alpha_{\delta(a)},\qquad \delta^2=\mathrm{id},
$$
so the signed adjoint is an involution on the class of the operators.

*Proof.* The formula exhibits the adjoint as a signed left multiplication; applying it twice gives the identity because $\delta^2=\mathrm{id}$, and the adjoint of the adjoint is the original by the general theory.

### Products and the square

**Theorem (products).** The signed left multiplications multiply by
$$
T^\alpha_a\,T^\alpha_b=L_{a\alpha(b)},
$$
an **unsigned** left multiplication, and the adjoint reverses the product, $(T^\alpha_aT^\alpha_b)^*=T^\alpha_{\delta(b)}T^\alpha_{\delta(a)}$; the square is
$$
\bigl(T^\alpha_a\bigr)^2=L_{a\,\alpha(a)} ,
$$
which is the identity exactly when $a\,\alpha(a)=1$.

*Proof.* The product is $L_a\alpha L_b\alpha=L_aL_{\alpha(b)}\alpha^2=L_{a\alpha(b)}$; the anti-multiplicativity of the adjoint and the closed form give the reversal; the square is the product with $b=a$.

## Self-Adjointness and Unitarity

**Corollary (self-adjointness, isometry and unitarity).** For $a\in\mathcal{A}$,
$$
T^\alpha_a\ \text{is self-adjoint}\iff a=\delta(a)\iff\alpha(a)=a^* ,
$$
and
$$
T^\alpha_a\ \text{is an isometry}\iff|a|=1 ,
$$
in which case it is unitary with the inverse $T^\alpha_{\alpha(a)^{-1}}$; the self-adjoint unitary signed left multiplications are the unimodular $\alpha$-Hermitian elements, $\alpha(a)=a^*$ and $|a|=1$.

*Proof.* Self-adjointness is $T^\alpha_a=T^\alpha_{\delta(a)}$; the map $a\mapsto T^\alpha_a$ is injective, so the two are equal exactly when $a=\delta(a)$, that is $a=\alpha(a)^*$, equivalently $\alpha(a)=a^*$. For the isometry, $(T^\alpha_a)^*T^\alpha_a=T^\alpha_{\delta(a)}T^\alpha_a=L_{\delta(a)\alpha(a)}=L_{\alpha(a^*)\alpha(a)}=L_{\alpha(a^*a)}=L_{|a|^2}$, the identity exactly when $|a|=1$; the unitary statement is the same computation in the other order, and the inverse of $T^\alpha_a$ for a unit $a$ is $T^\alpha_{\alpha(a)^{-1}}$.

**Theorem (the unitary group).** The unitary signed left multiplications form the group
$$
\{T^\alpha_a:|a|=1\}\cong L^\infty(\Omega,\mathbb T),
$$
Abelian, and the self-adjoint unitary members are the unimodular $\alpha$-Hermitian elements; the map $a\mapsto T^\alpha_a$ is injective, so the group is isomorphic to the group of the unimodular random variables.

*Proof.* The product of two unitary signed left multiplications is unitary, being a product of unitaries; the inverse of $T^\alpha_a$ is $(T^\alpha_a)^*=T^\alpha_{\delta(a)}$ when $|a|=1$; the group is Abelian by the commutativity of the algebra; and the map is injective because $T^\alpha_a=0$ implies $a=0$.

## The Comparison with the Involution

### The twisted involution

**Theorem (the involution and the adjoint).** The adjoint of the signed left multiplication agrees with the multiplication of the **twisted image** of the parameter: on the elements, the map $a\mapsto\delta(a)=\alpha(a^*)$ is the composite of the involution $\sigma$ and the grade involution $\alpha$; the adjoint realises it, $T^\alpha_a\mapsto T^\alpha_{\delta(a)}$. The ordinary involution is realised by the adjoint **only when** $\alpha=\mathrm{id}$, in which case $\delta=\sigma$ and the adjoint of $L_a$ is $L_{a^*}$.

*Proof.* The closed form is the realisation of $\delta$ on the parameters; the case $\alpha=\mathrm{id}$ reduces $\delta$ to the conjugation, and the adjoint of $L_a$ is $L_{a^*}$, which is *The Adjoint of the Left Multiplication on the Algebra of Random Variables*, earlier in this category. The two structures, the involution on the elements and the adjoint on the operators, coincide up to the twist, and the twist is the grade involution.

### The arithmetic contrast

**Theorem (the comparison with the arithmetic case).** Over the algebra of arithmetic functions under the coefficient form the adjoint of $L_a\alpha$ is the transposed multiplication $\Theta_a$ composed with $\alpha$, and it is a signed left multiplication only when $\alpha(a)$ is a unit; here the adjoint is a signed left multiplication for every $a$. The discrepancy is the invariance of the expectation form, which returns $L_{a^*}$ for the adjoint of $L_a$ instead of the transpose.

*Proof.* The arithmetic statement is that of *The Adjoint of the Left Multiplication on the Algebra of Arithmetic Functions*, written, and *The Signed Left Multiplication on the Algebra of Arithmetic Functions*, written; the difference is the invariance of the form, which is the traciality of the state in the commutative algebra.

## Worked Examples

**Example (the two-atom swap).** For $\Omega=\{\omega_-,\omega_+\}$ with the uniform probability and $\alpha(x_-,x_+)=(x_+,x_-)$, the signed left multiplication by $a=(a_-,a_+)$ is $T^\alpha_a(x_-,x_+)=(a_-x_+,a_+x_-)$; its adjoint has the parameter $\delta(a)=(\bar a_+,\bar a_-)$ and acts by $(x_-,x_+)\mapsto(\bar a_+x_+,\bar a_-x_-)$, which is the direct adjoint of the coordinate action; the operator is self-adjoint exactly when $a_-=a_+$, that is when $a$ is even.

**Example (the circle phase).** On $\Omega=\mathbb R/\mathbb Z$ with the Lebesgue measure and $\alpha(x)(\theta)=x(-\theta)$, the parameter $a(\theta)=e^{2\pi i\theta}$ satisfies $\alpha(a)(\theta)=e^{-2\pi i\theta}=a(\theta)^*$, so $a$ is $\alpha$-Hermitian, $\delta(a)=a$, and $T^\alpha_a$ is self-adjoint and unitary; it is the operator $x(\theta)\mapsto e^{2\pi i\theta}x(-\theta)$, an involution of the circle.

**Example (the trivial grading).** For $\alpha=\mathrm{id}$ the signed left multiplication is the ordinary one, the closed form is $L_a^*=L_{a^*}$, self-adjointness is $a$ real and unitarity is $|a|=1$; this is the boundary at which the signed adjoint is the ordinary adjoint of *The Adjoint of the Left Multiplication on the Algebra of Random Variables*, earlier in this category.

**Example (the non-self-adjoint phase).** For the parameter $a(\theta)=e^{2\pi i\theta}$ with the **trivial** grading the operator $L_a$ is unitary but not self-adjoint; with the reflection grading it is self-adjoint. The example shows that the same operator can be self-adjoint or not according as the grading is present, the adjoint being computed with respect to the same form.

## Failure of the Degenerate Cases

The signed adjoint of the left multiplication degenerates in four configurations. First, the closed form is a consequence of the invariance of the expectation form; for a non-tracial state or a non-commutative algebra the adjoint is a right multiplication up to the modular correction, and the twist $\delta$ alone does not describe it. Second, the self-adjointness condition $a=\delta(a)$ is the $\alpha$-Hermiticity, not the reality $a=a^*$; the graded elements can be self-adjoint without being real, and the constant phases of the circle example are the simplest case. Third, the isometry condition $|a|=1$ is separate from the self-adjointness; the unitary and the self-adjoint members of the signed left multiplications intersect in the unimodular $\alpha$-Hermitian elements, and the general unitary is not self-adjoint. Fourth, the products of two signed left multiplications are **unsigned**; the class of the signed operators is not closed under multiplication, only under the adjoint, and confusing the two closure properties is the standard error of the graded theory.

## Summary

The adjoint of the signed left multiplication $T^\alpha_a=L_a\alpha$ of the algebra of random variables with respect to the form $\langle x,y\rangle=\varphi(xy^*)$ is the signed left multiplication of the twisted parameter,
$$
\bigl(T^\alpha_a\bigr)^*=T^\alpha_{\delta(a)}=\alpha L_{a^*},\qquad \delta=\sigma\alpha=\alpha\sigma ,
$$
so the adjoint operation preserves the class of the signed left multiplications and acts on the parameter by the twisted involution, the same formula as in the noncommutative ring but derived here from the invariance of the form. The products are the unsigned left multiplications, $T^\alpha_aT^\alpha_b=L_{a\alpha(b)}$, the square is $(T^\alpha_a)^2=L_{a\alpha(a)}$, the operator is self-adjoint exactly when $a$ is $\alpha$-Hermitian, $\alpha(a)=a^*$, and it is an isometry or unitary exactly when $|a|=1$, the unitary group being the unimodular random variables. The adjoint agrees with the involution on the elements **up to the twisted involution** $\delta$, and coincides with it only when the grading is trivial. The unsigned adjoint is *The Adjoint of the Left Multiplication on the Algebra of Random Variables*, earlier in this category; the sandwich case is *The Signed Adjoint Sandwich on the Algebra of Random Variables*, the preceding article of this category; and the module case is *The Graded Adjoint Action on a Module over the Algebra of Random Variables*, the next article of this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T^\alpha_a=L_a\alpha$ | the signed left multiplication |
| $\langle x,y\rangle=\varphi(xy^*)$ | the form of the category |
| $\delta=\sigma\alpha=\alpha\sigma$ | the twisted involution |
| $(T^\alpha_a)^*=T^\alpha_{\delta(a)}=\alpha L_{a^*}$ | the signed adjoint |
| $T^\alpha_aT^\alpha_b=L_{a\alpha(b)}$ | the products, unsigned |
| $(T^\alpha_a)^2=L_{a\alpha(a)}$ | the square |
| $\alpha(a)=a^*$ | self-adjointness |
| $|a|=1$ | isometry and unitarity |

## Further Reading

- Jacques Dixmier, *C*-Algebras* (North-Holland, 1977), for the involutions, the twisted involutions and the representations.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Vol. I (Academic Press, 1983), for the adjoints, the unitaries and the $*$-representations.
- Sterling K. Berberian, *Baer *-Rings* (Springer, 1972), for the involutions, the graded rings and the adjoints.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the twisted involutions and the graded structures.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the graded operators and their adjoints.
