
# __The Graded Adjoint Action on a Module over a Lie Algebra__

## Introduction

A graded module over a graded Lie algebra carries a **graded action**, the action composed with the parity operator, $m\mapsto x\cdot(\beta m)$, and the **adjoint** of this action — its adjoint operator with respect to an invariant Hermitian form on the module — obeys a sign rule fixed by the parity of the acting element: the graded action is **skew-adjoint** for an even element and **self-adjoint** for an odd element. The sign rule is the module form of the parity dichotomy of the one-sided operators, and it is forced by the two compatibility requirements of the graded theory, the invariance of the form under the action and the isometry of the parity operator. The article defines the adjoint action, computes its adjoint, records the compatibility with the grading and derives the sign rule.

This article treats the adjoint action of a graded module over a Lie algebra, its compatibility with the grading and the sign rule. It is the sixth and last article of the `- * Operator Theory` group of the category; the graded module and its parity operator are *The Graded Action on a Module over a Lie Algebra*, above in the category, the adjoints of the one-sided operators are *The Signed Adjoint of the Left Multiplication on a Lie Algebra* and *The Signed Adjoint of the Reflection on a Lie Algebra*, above, the invariant forms and the unitary representations are *Hermitian Forms on a Lie Algebra* and *Unitary Representations and the Adjoint Operator*, above, and the module operations are *Representations of Lie Algebras*.

The article assumes the graded module, the parity operator, the sign rule and the enveloping algebra from *The Graded Action on a Module over a Lie Algebra*, the adjoint operation, the skew-adjointness of the generators and the unitarity condition from *Unitary Representations and the Adjoint Operator*, the invariant Hermitian form and its positive definite case from *Hermitian Forms on a Lie Algebra*, the grading and the grade involution from *Graded Lie Algebras with an Involution*, and the exterior algebra and the Clifford module from *The Exterior Algebra* and *Spin Representations and Clifford Modules with Inner Conjugation*. The form and the adjoint are instruments of the article; the geometry of the module is Part IV, and the representations as analytic objects belong to *Unitary Representations of a Lie Group*.

## The Action and Its Adjoint

### The Setting

**Definition.** Let $\mathrm{G}$ be a graded Lie algebra with the grade involution $\alpha$ and let $M = M^{+}\oplus M^{-}$ be a graded module over $\mathrm{G}$ with the parity operator $\beta$ equal to $\pm\mathrm{id}$ on the two pieces. Let $(\cdot,\cdot)$ be a Hermitian form on $M$ that is **graded**, $(M^{\epsilon},M^{\delta}) = 0$ for $\epsilon\neq\delta$, and **invariant** under the action, $(x\cdot m,n) + (m,x\cdot n) = 0$ for all homogeneous $x$ and all $m,n$.

**Definition.** The **action operators** are the endomorphisms $\rho(x)$ with $\rho(x)m = x\cdot m$, and the **graded action operators** are the composites

$$
\rho^{\alpha}(x) = \rho(x)\circ\beta , \qquad \rho^{\alpha}(x)m = x\cdot(\beta m) ;
$$

the operator $\rho^{\alpha}(x)$ is the signed one-sided action of the module.

**Proposition.** The parity operator is a self-adjoint unitary involution of the form, $\beta^{*} = \beta = \beta^{-1}$, because it is an isometry exchanging the two orthogonal pieces; the adjoint of the action operator is the negative of the action operator,

$$
\rho(x)^{*} = -\rho(x) ,
$$

which is the infinitesimal unitarity condition of the module.

*Proof.* The graded form makes the two pieces orthogonal and $\beta$ acts by $\pm1$ on them, so $\beta$ is a self-adjoint isometry and an involution; the invariance of the form is the identity $(\rho(x)m,n) = -(m,\rho(x)n)$, which is the skew-adjointness of the action operator.

### The Adjoint of the Graded Action

**Theorem (the sign rule).** The adjoint of the graded action is a signed multiple of the graded action,

$$
\bigl(\rho^{\alpha}(x)\bigr)^{*} = \beta^{*}\rho(x)^{*} = -\beta\rho(x) = (-1)^{\lvert x\rvert+1}\rho^{\alpha}(x),
$$

so that

$$
\bigl(\rho^{\alpha}(x)\bigr)^{*} = -\rho^{\alpha}(x) \quad (x\ \text{even}), \qquad \bigl(\rho^{\alpha}(x)\bigr)^{*} = \rho^{\alpha}(x) \quad (x\ \text{odd}) :
$$

the **graded action is skew-adjoint for the even elements and self-adjoint for the odd elements**.

*Proof.* The adjoint of a composite is the composite of the adjoints in the reverse order, so $(\rho^{\alpha}(x))^{*} = \beta^{*}\rho(x)^{*} = \beta(-\rho(x)) = -\beta\rho(x)$; the graded commutation $x\beta = (-1)^{\lvert x\rvert}\beta x$ of the action with the parity operator gives $\beta\rho(x) = (-1)^{\lvert x\rvert}\rho(x)\beta$, hence $-\beta\rho(x) = -(-1)^{\lvert x\rvert}\rho(x)\beta = (-1)^{\lvert x\rvert+1}\rho^{\alpha}(x)$; the parity cases are immediate.

### Unitarity

**Theorem.** The graded action operator is unitary exactly when it is an involution up to the sign of the adjoint; for an even element the operator is norm-preserving exactly when $\rho^{\alpha}(x)^2 = -\mathrm{id}$, and for an odd element exactly when $\rho^{\alpha}(x)^2 = \mathrm{id}$; the graded action by an odd element is therefore a symmetry of the form, and the graded action by an even element is a complex structure of the form.

*Proof.* For a self-adjoint or a skew-adjoint operator the operator is unitary exactly when its square is $\mp\mathrm{id}$, with the sign determined by the adjoint; the parity cases give the two statements.

## The Compatibility with the Grading

### The Graded Commutation

**Theorem.** The graded action graded-commutes with the parity operator,

$$
\rho^{\alpha}(x)\,\beta = (-1)^{\lvert x\rvert}\,\beta\,\rho^{\alpha}(x) ,
$$

so the graded action by an even element commutes with the grading operator and the graded action by an odd element anticommutes with it; the sign rule for the adjoint is the same sign as the graded commutation.

*Proof.* Compute $\rho^{\alpha}(x)\beta = \rho(x)\beta^2 = \rho(x)$ and $\beta\rho^{\alpha}(x) = \beta\rho(x)\beta = (-1)^{\lvert x\rvert}\rho(x)$; the two differ by the sign $(-1)^{\lvert x\rvert}$.

### The Decomposition

**Theorem.** The graded action preserves the decomposition of the module in the graded sense: for an even element it preserves each piece, and for an odd element it exchanges them;

$$
\rho^{\alpha}(x)M^{+}\subseteq M^{\lvert x\rvert}, \qquad \rho^{\alpha}(x)M^{-}\subseteq M^{1+\lvert x\rvert} .
$$

The operator $\rho^{\alpha}(x)$ is self-adjoint exactly on the odd elements and skew-adjoint exactly on the even ones, and the adjoint of the graded action is the graded action with the sign of the parity.

*Proof.* The inclusion is the commutation with $\beta$ written as the grading; the adjoint statement is the sign rule, and the last phrase is a restatement of the sign rule.

### The Action of the Enveloping Algebra

**Proposition.** The graded action extends to the enveloping algebra and the adjoint rule is multiplicative up to the parity,

$$
\bigl(\rho^{\alpha}(u)\bigr)^{*} = (-1)^{\lvert u\rvert}\,\rho^{\alpha}(u^{\star})
$$

on homogeneous $u\in U(\mathrm{G})$, where $u^{\star}$ is the star of the principal anti-automorphism; hence the graded action is a star-operation with the sign of the parity.

*Proof.* The action extends to $U(\mathrm{G})$ with the graded product; the adjoint of a product is the product of the adjoints in the reverse order with the sign rule of the parity, and the star of *The Involution on the Enveloping Algebra of a Lie Group* is the adjoint operation of the generators.

## The Sign Rule and the Structure

### The Invariant Form

**Theorem.** The graded action preserves the graded form up to the parity of the acting element,

$$
\bigl(\rho^{\alpha}(x)m,n\bigr) = (-1)^{\lvert x\rvert}\bigl(m,\rho^{\alpha}(x)n\bigr) ,
$$

and the form is invariant under the action exactly when the sign rule holds; the module is **unitary** when the form is positive definite, and the graded action is then a representation by unitary and self-adjoint operators on the odd part and by unitary and skew-adjoint operators on the even part.

*Proof.* From the adjoint identity $(\rho^{\alpha}(x)m,n) = (m,(\rho^{\alpha}(x))^{*}n)$ and the sign rule; the unitarity of the module is the positive definiteness of the form, and the self-adjointness or the skew-adjointness of the operators is the parity case of the sign rule.

### The Kernel and the Fixed Points

**Proposition.** The kernel of the graded action is the set of the $m$ with $x\cdot(\beta m) = 0$, that is the image under $\beta$ of the annihilator of $x$ in $M$; the fixed points of the graded action by an odd element are the elements of $M^{+}$ whose image under the action lies in $M^{-}$, and the fixed points of the graded action by an even element are the elements annihilated after the grading.

*Proof.* Compute the kernel and the fixed equation $\rho^{\alpha}(x)m = m$ from the definitions and the commutation with $\beta$.

## Examples

### The Adjoint Module

Let $M = \mathrm{G}$ be the adjoint module with the graded form and the parity operator $\beta = \alpha$; then the action operator is $\rho(x) = \operatorname{ad}_x = L_x$ and the graded action is $\rho^{\alpha}(x) = L_x\alpha = \ell^{\alpha}_x$, the signed left multiplication. The sign rule of the present article is then the parity dichotomy of *The Signed Adjoint of the Left Multiplication on a Lie Algebra*: skew-adjoint for the even elements and self-adjoint for the odd ones. The example shows that the module theory generalises the one-sided theory of the algebra.

### The Exterior Algebra

Let $V$ be odd and let $M = \Lambda(V)$ be the exterior algebra with its natural graded form; the action extends as a graded derivation, the graded action is the composition with the parity operator of the form, and the sign rule says that the odd elements act by self-adjoint operators while the even ones act by skew-adjoint operators. The form is the one of the exterior algebra of *The Exterior Algebra*, and the graded action is the one of *The Graded Action on a Module over a Lie Algebra*.

### The Clifford Module

Let $M$ be a Clifford module with the two chiralities $M^{\pm}$; the parity operator is the chirality operator, the action of the orthogonal Lie algebra is graded, and the graded action is a self-adjoint operator on the odd generators and a skew-adjoint operator on the even ones; the sign rule is the one of the Clifford relations of *Spin Representations and Clifford Modules with Inner Conjugation*.

### The Trivial Grading

If $\mathrm{G}$ is entirely even then the parity operator is the identity, the graded action is the action itself, and the sign rule gives the skew-adjointness of every generator; there is no self-adjoint case, and the graded theory reduces to the ungraded theory of *Unitary Representations and the Adjoint Operator*.

## Summary

On a graded module $M = M^{+}\oplus M^{-}$ over a graded Lie algebra with an invariant graded Hermitian form, the action operators are skew-adjoint, $\rho(x)^{*} = -\rho(x)$, and the parity operator is a self-adjoint unitary involution. The **graded action** $\rho^{\alpha}(x) = \rho(x)\beta$, acting by $m\mapsto x\cdot(\beta m)$, has the adjoint

$$
\bigl(\rho^{\alpha}(x)\bigr)^{*} = -\beta\rho(x) = (-1)^{\lvert x\rvert+1}\rho^{\alpha}(x) ,
$$

so it is **skew-adjoint for the even elements and self-adjoint for the odd elements**; this is the sign rule, and it is the same sign as the graded commutation $\rho^{\alpha}(x)\beta = (-1)^{\lvert x\rvert}\beta\rho^{\alpha}(x)$ with the parity operator. The graded action preserves the decomposition of the module in the graded sense, extending to the enveloping algebra with the adjoint rule $(\rho^{\alpha}(u))^{*} = (-1)^{\lvert u\rvert}\rho^{\alpha}(u^{\star})$, and the form is invariant exactly under the sign rule; the module is unitary when the form is positive definite, and the graded action is a representation by unitary operators, self-adjoint on the odd part and skew-adjoint on the even part. The adjoint module recovers the one-sided theory of the algebra, the exterior algebra and the Clifford module are the geometric examples, and the trivial grading reduces the theory to the ungraded case, where every generator is skew-adjoint.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M = M^{+}\oplus M^{-}$ | the graded module |
| $\beta$ | the parity operator, a self-adjoint unitary involution |
| $(\cdot,\cdot)$ | the invariant graded Hermitian form |
| $\rho(x)m = x\cdot m$ | the action operator |
| $\rho^{\alpha}(x) = \rho(x)\beta$ | the graded action, $m\mapsto x\cdot(\beta m)$ |
| $\rho(x)^{*} = -\rho(x)$ | skew-adjointness of the action operators |
| $(\rho^{\alpha}(x))^{*} = (-1)^{\lvert x\rvert+1}\rho^{\alpha}(x)$ | the sign rule |
| $\rho^{\alpha}(x)\beta = (-1)^{\lvert x\rvert}\beta\rho^{\alpha}(x)$ | the graded commutation |
| $(\rho^{\alpha}(u))^{*} = (-1)^{\lvert u\rvert}\rho^{\alpha}(u^{\star})$ | the adjoint rule on the enveloping algebra |
| $(\rho^{\alpha}(x)m,n) = (-1)^{\lvert x\rvert}(m,\rho^{\alpha}(x)n)$ | the invariance of the form |

## Further Reading

- Victor G. Kac, *Infinite Dimensional Lie Algebras* (Cambridge University Press, third edition, 1990), for the graded modules, the parity operator and the sign rule.
- Manfred Scheunert, *The Theory of Lie Superalgebras* (Springer Lecture Notes in Mathematics 716, 1979), for the graded modules, the adjoints and the enveloping algebra.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, second edition, 2015), for the adjoints of the action operators, the unitary conditions and the star-representations.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the graded involutions, the signed adjoints and the sign rules.
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984), for the modules over a Lie algebra, the adjoints and the graded structures.
