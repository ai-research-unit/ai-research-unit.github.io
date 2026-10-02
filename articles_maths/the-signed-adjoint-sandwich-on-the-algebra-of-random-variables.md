
# __The Signed Adjoint Sandwich on the Algebra of Random Variables__

## Introduction

The signed sandwich is the two-sided operator twisted by the grade involution,
$$
S^\alpha_{a,b}(x)=a\,\alpha(x)\,b ,
$$
and this article computes its **adjoint** with respect to the form of the category,
$$
\langle x,y\rangle=\varphi(xy^*)=\mathbb E\bigl[x\bar y\bigr].
$$
The result is
$$
\bigl(S^\alpha_{a,b}\bigr)^*=S^\alpha_{\delta(a),\delta(b)},\qquad \delta=\sigma\alpha=\alpha\sigma ,
$$
the signed sandwich of the **twisted images** of the two parameters, where $\delta$ is the composite of the conjugation and the grade involution. The formula is the same as in the noncommutative signed theory of *The Signed Adjoint Sandwich on a Ring*, in Part I, but the reason is different: there the twisted involution $\delta$ performs the reversal of the product, while here the product is commutative and the invariance of the expectation form alone yields $L_c^*=L_{c^*}$, after which the twist $\delta$ on the parameters completes the computation. The article gives the closed form of the adjoint, the behaviour under products, the self-adjointness, the isometry, the unitarity and the involutions of the signed sandwiches, and the comparison with the unsigned sandwich and with the ring case.

The conventions are those fixed in *The Signed Sandwich on the Algebra of Random Variables*, earlier in this category: $\mathcal{A}=L^\infty(\Omega,\mathcal F,\mathbb P)$ with the pointwise product, the conjugation $\sigma(a)=\bar a$, the state $\varphi(a)=\mathbb E[a]$, the form of the category $\langle x,y\rangle=\varphi(xy^*)$, the grade involution $\alpha$ (an involutive, unitary, self-adjoint automorphism commuting with the conjugation), the grading $\mathcal{A}=\mathcal{A}_{\bar0}\oplus\mathcal{A}_{\bar1}$, and the twisted involution $\delta=\sigma\alpha=\alpha\sigma$. The signed sandwich collapses on the commutative algebra to $S^\alpha_c$ with $c=ab$ and $S^\alpha_c=L_c\alpha$, which is *The Signed Sandwich on the Algebra of Random Variables*, earlier in this category; the signed left multiplication is $T^\alpha_a=S^\alpha_{a,1}=L_a\alpha$, *The Signed Left Multiplication on the Algebra of Random Variables*, earlier in this category, and its adjoint is *The Signed Adjoint of the Left Multiplication on the Algebra of Random Variables*, the later article of this category; the reflections are *Reflections as Signed Two-Sided Operators on the Algebra of Random Variables*, earlier in this category, and their adjoints are *The Signed Adjoint of the Reflection on the Algebra of Random Variables*, later in this category. The adjoint of the unsigned left multiplication is *The Adjoint of the Left Multiplication on the Algebra of Random Variables*, earlier in this category, and the operator-algebra involution is *The Involution on the Operator Algebra of a Process*, earlier in this category. No physics is invoked.

Throughout, $\mathcal{A}$ is the algebra of random variables, $\mathcal{H}=L^2(\Omega,\mathbb P)$ with the form $\langle x,y\rangle=\varphi(xy^*)$ is the Hilbert space of the category, $\alpha$ is the grade involution and $\delta=\sigma\alpha$. The signed sandwich is $S^\alpha_{a,b}(x)=a\,\alpha(x)\,b$, the unsigned sandwich is $S_{a,b}(x)=axb$, and the twisted involution satisfies $\delta^2=\mathrm{id}$, $\delta\sigma=\sigma\delta=\alpha$ and $\delta\alpha=\alpha\delta=\sigma$.

## The Signed Adjoint Sandwich

### Definition and closed form

**Definition.** The **adjoint** of the signed sandwich is the operator $(S^\alpha_{a,b})^*$ with
$$
\langle S^\alpha_{a,b}x,y\rangle=\langle x,(S^\alpha_{a,b})^*y\rangle\qquad\text{for all }x,y\in\mathcal{H}.
$$

**Theorem (the closed form).** For all $a,b\in\mathcal{A}$,
$$
\bigl(S^\alpha_{a,b}\bigr)^*=S^\alpha_{\delta(a),\delta(b)}=S^\alpha_{\alpha(a^*),\alpha(b^*)},
$$
with $\delta=\sigma\alpha$; on the commutative algebra, where $S^\alpha_{a,b}=S^\alpha_{ab}$, this is $\bigl(S^\alpha_c\bigr)^*=S^\alpha_{\delta(c)}$.

*Proof.* The operator is the composite $S^\alpha_{a,b}=L_a\,\alpha\,R_b$, and the adjoint of a product is the product of the adjoints in reverse order, $(L_a\alpha R_b)^*=R_b^*\alpha^*L_a^*$. By *The Adjoint of the Left Multiplication on the Algebra of Random Variables*, earlier in this category, $L_a^*=L_{a^*}$ and $R_b^*=R_{b^*}=L_{b^*}$, and $\alpha^*=\alpha$ because the grade involution is self-adjoint; hence $(S^\alpha_{a,b})^*=L_{b^*}\alpha L_{a^*}$. Using $\alpha L_{a^*}=L_{\alpha(a^*)}\alpha$ and the commutativity, this is $L_{b^*\alpha(a^*)}\alpha$. A direct computation of $S^\alpha_{\delta(a),\delta(b)}=L_{\delta(a)}\alpha L_{\delta(b)}=L_{\delta(a)}L_{\alpha\delta(b)}\alpha$ gives the coefficient $\delta(a)\,\alpha\delta(b)$. Now $\delta(a)=(\alpha(a))^*=\alpha(a^*)$ because $\alpha$ commutes with the conjugation, and $\alpha\delta(b)=\alpha\sigma\alpha(b)=\sigma(b)=b^*$ because $\alpha^2=\mathrm{id}$ and $\alpha\sigma=\sigma\alpha$; the coefficient is therefore $\alpha(a^*)\,b^*=b^*\,\alpha(a^*)$ by the commutativity, which matches the coefficient $b^*\alpha(a^*)$ of $L_{b^*}\alpha L_{a^*}$.

**Corollary (the two readings).** The adjoint of the sandwich with the parameters $(a,b)$ is the sandwich with the parameters $(\alpha(a^*),\alpha(b^*))$; when $\alpha=\mathrm{id}$ this is the unsigned sandwich adjoint $S_{a,b}^*=S_{a^*,b^*}$, and the twist is the whole effect of the grading.

*Proof.* The formula with $\alpha=\mathrm{id}$ gives $\delta=\sigma$ and $S_{\delta(a),\delta(b)}=S_{a^*,b^*}$, the adjoint of the unsigned sandwich.

### Products and the involution

**Theorem (products).** The signed sandwiches compose by
$$
S^\alpha_{a,b}\,S^\alpha_{c,d}=S^\alpha_{a\alpha(c),\alpha(d)b},
$$
and the adjoint reverses the product, $(S^\alpha_{a,b}S^\alpha_{c,d})^*=(S^\alpha_{c,d})^*(S^\alpha_{a,b})^*$; the map $(a,b)\mapsto S^\alpha_{a,b}$ is a representation of the semidirect product of the algebra with its grade involution.

*Proof.* Composing, $(S^\alpha_{a,b}S^\alpha_{c,d})(x)=a\alpha(c\alpha(x)d)b=a\alpha(c)\,\alpha^2(x)\,\alpha(d)b=S^\alpha_{a\alpha(c),\alpha(d)b}(x)$; the anti-multiplicativity of the adjoint is the general property, and the representation statement is the multiplicativity just computed.

**Theorem (square and involution).** On the commutative algebra the sandwich is $S^\alpha_c$ with $c=ab$, its square is
$$
\bigl(S^\alpha_c\bigr)^2=S^\alpha_{c\,\alpha(c)},
$$
and it is an involution exactly when $c\,\alpha(c)=1$, that is when $c$ is an $\alpha$-cocycle; the involutive signed sandwiches form a group under multiplication.

*Proof.* The square is $(L_c\alpha)^2=L_c\alpha L_c\alpha=L_cL_{\alpha(c)}\alpha^2=L_{c\alpha(c)}=S^\alpha_{c\alpha(c)}$; the involution is the square equal to the identity, which is $c\alpha(c)=1$; the $\alpha$-cocycles are closed under multiplication and inversion because $\alpha$ is an involution.

## The Comparison with the Ring

**Theorem (the same formula, a different reason).** The adjoint of the signed sandwich on the algebra of random variables is the sandwich of the twisted images, exactly as on a ring; in the ring the formula arises from the reversal of the product by the transposition and the twist $\delta$, while here the product is commutative, the transposition is trivial, and the formula arises from the invariance of the expectation form, $L_a^*=L_{a^*}$, together with the twist $\delta$ on the parameters.

*Proof.* The ring statement is *The Signed Adjoint Sandwich on a Ring*, in Part I, where the adjoint of $S^\alpha_{a,b}$ is $S^\alpha_{\delta(a),\delta(b)}$ with $\delta=\sigma\alpha$; the commutative computation is the theorem above, and the comparison isolates the invariance of the form as the substitute for the transposition.

**Corollary (the arithmetic contrast).** Over the algebra of arithmetic functions under the coefficient form the adjoint of a signed sandwich is the transposed sandwich and is not a signed sandwich in general; here it is a signed sandwich for every pair of parameters, which is the commutativity and the traciality of the state.

*Proof.* The arithmetic statement is that of *The Signed Sandwich on the Algebra of Arithmetic Functions*, written, and *The Adjoint of the Left Multiplication on the Algebra of Arithmetic Functions*, written; the difference is the invariance of the form.

## Worked Examples

**Example (the signed left multiplication).** For $b=1$ the sandwich is $S^\alpha_{a,1}=T^\alpha_a=L_a\alpha$, and the formula gives $(T^\alpha_a)^*=S^\alpha_{\delta(a),1}=T^\alpha_{\delta(a)}$; this is the adjoint computed independently in *The Signed Adjoint of the Left Multiplication on the Algebra of Random Variables*, the later article of this category, and the agreement is the consistency of the two routes.

**Example (the grade involution).** For $a=b=1$ the sandwich is $\alpha=S^\alpha_1$, and $\delta(1)=1$, so $\alpha^*=\alpha$; the involution is self-adjoint, unitary and an involution, and its adjoint is itself.

**Example (the swapped two-atom algebra).** For $\Omega=\{\omega_-,\omega_+\}$ with the uniform probability, $\alpha(x_-,x_+)=(x_+,x_-)$ and the parameters $a=(a_-,a_+)$, $b=(b_-,b_+)$, the sandwich is $S^\alpha_{a,b}(x_-,x_+)=(a_-b_+x_+,a_+b_-x_-)$; the adjoint has the parameters $\delta(a)=(\bar a_+,\bar a_-)$ and $\delta(b)=(\bar b_+,\bar b_-)$, that is $S^\alpha_{\delta(a),\delta(b)}(x_-,x_+)=(\delta(a)_-\delta(b)_+x_+,\delta(a)_+\delta(b)_-x_-)=(\bar a_+\bar b_-x_+,\bar a_-\bar b_+x_-)$; the direct adjoint of the diagonal action $(x_-,x_+)\mapsto(a_-b_+x_+,a_+b_-x_-)$ is the diagonal action by the conjugates $(\overline{a_+b_-},\overline{a_-b_+})$ $=(\bar a_+\bar b_-,\bar a_-\bar b_+)$, in agreement.

**Example (the unitary sandwiches).** On the commutative algebra the sandwich $S^\alpha_c$ is unitary exactly when $|c|=1$ and self-adjoint exactly when $\alpha(c)=c^*$; the two conditions together give the unitary self-adjoint signed sandwiches, the moduli-one $\alpha$-Hermitian elements, among which the reflection $\alpha=S^\alpha_1$ is the trivial one and the unimodular cocycles $c\alpha(c)=1$ are the involutions.

## Failure of the Degenerate Cases

The signed adjoint sandwich degenerates in four configurations. First, the closed form holds for the form of the category and the grade involution; a different grade involution or a different form changes the twisted involution $\delta$ and the formula, and the adjoint is not a signed sandwich at all for a general form. Second, on the commutative algebra the two parameters of the sandwich collapse to the product $c=ab$, and the adjoint depends on $c$ alone; the two-sided information of the ring case is lost, so the adjoint cannot distinguish different factorisations of the same $c$. Third, the involution condition $c\alpha(c)=1$ is not the unitarity condition $|c|=1$; the involutive sandwiches and the unitary sandwiches are different families, intersecting in the moduli-one cocycles, and confusing the two is the standard error. Fourth, the self-adjointness $c=\delta(c)$ is the $\alpha$-Hermitian condition $\alpha(c)=c^*$, which is not the reality $c=c^*$ unless $\alpha=\mathrm{id}$; the grading shifts the self-adjointness of the signed operators off the real elements.

## Summary

The adjoint of the signed sandwich $S^\alpha_{a,b}(x)=a\alpha(x)b$ on the algebra of random variables with respect to the form $\langle x,y\rangle=\varphi(xy^*)$ is the signed sandwich of the twisted images of the parameters,
$$
\bigl(S^\alpha_{a,b}\bigr)^*=S^\alpha_{\delta(a),\delta(b)},\qquad \delta=\sigma\alpha=\alpha\sigma ,
$$
the same formula as on a noncommutative ring but derived here from the invariance of the expectation form, $L_a^*=L_{a^*}$, together with the twist $\delta$. The sandwiches compose by $S^\alpha_{a,b}S^\alpha_{c,d}=S^\alpha_{a\alpha(c),\alpha(d)b}$, the adjoint reverses the product, the square on the commutative algebra is $(S^\alpha_c)^2=S^\alpha_{c\alpha(c)}$, and the sandwich is an involution exactly for the $\alpha$-cocycles $c\alpha(c)=1$, self-adjoint exactly for the $\alpha$-Hermitian elements $\alpha(c)=c^*$, and unitary exactly for the moduli-one elements $|c|=1$. The signed left multiplication and its adjoint are *The Signed Adjoint of the Left Multiplication on the Algebra of Random Variables*, the later article of this category, and the reflections and their adjoints are *The Signed Adjoint of the Reflection on the Algebra of Random Variables*, the later article of this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S^\alpha_{a,b}(x)=a\alpha(x)b$ | the signed sandwich |
| $\langle x,y\rangle=\varphi(xy^*)$ | the form of the category |
| $\delta=\sigma\alpha=\alpha\sigma$ | the twisted involution |
| $(S^\alpha_{a,b})^*=S^\alpha_{\delta(a),\delta(b)}$ | the adjoint |
| $S^\alpha_{a,b}S^\alpha_{c,d}=S^\alpha_{a\alpha(c),\alpha(d)b}$ | the product |
| $(S^\alpha_c)^2=S^\alpha_{c\alpha(c)}$ | the square |
| $c\alpha(c)=1$ | the involutions |
| $\alpha(c)=c^*$ | the self-adjoint sandwiches |
| $|c|=1$ | the unitary sandwiches |

## Further Reading

- Jacques Dixmier, *C*-Algebras* (North-Holland, 1977), for the involutions, the twisted involutions and the representations.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Vol. I (Academic Press, 1983), for the adjoints and the $*$-representations.
- Sterling K. Berberian, *Baer *-Rings* (Springer, 1972), for the involutions, the twisted involutions and the inversive rings.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the graded operators and their adjoints.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the graded and twisted involutions.
