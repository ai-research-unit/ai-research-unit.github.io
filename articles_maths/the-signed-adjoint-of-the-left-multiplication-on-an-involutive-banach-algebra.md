
# __The Signed Adjoint of the Left Multiplication on an Involutive Banach Algebra__

## Introduction

The **signed left multiplication** by an element $r$ is the operator $\ell_r(x) = r\,\alpha(x)$, the left multiplication twisted by the grade involution; it is the one-sided operator of the signed theory, and its adjoint with respect to the form of the category is the signed left multiplication by the **conjugate element**, $(\ell_r)^\dagger = \ell_{\delta(r)}$, $\delta = \sigma\alpha$. From this formula the dictionary of the signed block follows: the signed left multiplication is self-adjoint exactly when $\delta(r) = r$ modulo the kernel, it is unitary exactly when the **defect** $\delta(r)\alpha(r)$ is the unit, and the two-sided signed sandwich is the composite of the signed left multiplication with a right multiplication. This article computes the adjoint of the signed left multiplication, derives its dictionary, and assembles the one-sided and two-sided operators.

The article assumes the signed left multiplication, its composition and its action on the regular module from *The Signed Left Multiplication on an Involutive Banach Algebra*; the grade involution $\alpha$, the composite $\delta = \sigma\alpha$ and the reflection from *The Grade Involution on a Banach Algebra* and *The Signed Left Multiplication on an Involutive Banach Algebra*; the form of the category, the adjoint and the self-adjoint and skew operators from *The Involution on the Operator Algebra*; the adjoint of the (unsigned) left multiplication from *The Adjoint of the Left Multiplication on an Involutive Banach Algebra*; the adjoint of the signed sandwich from *The Signed Adjoint Sandwich on a Banach Algebra*; and the involution $\sigma$, the unitary elements and the Cayley transform from *Adjoints in a Banach Algebra*. The graded module case is *The Graded Adjoint Action on a Graded Module*.

Throughout, $A$ is a unital Banach algebra over $\mathbb{C}$ with the grade involution $\alpha$ and the involution $\sigma$, with $\sigma\alpha = \alpha\sigma$ and $\delta = \sigma\alpha = \alpha\sigma$; the form of the category is $\{x,y\} = \tau(x\sigma(y))$ with $\tau$ a continuous $\sigma$-invariant and $\alpha$-invariant trace, and $\alpha^\dagger = \alpha$; the **signed left multiplication** and the **signed right multiplication** are

$$
\ell_r(x) = r\,\alpha(x) , \qquad \varrho_s(x) = \alpha(x)\,s ,
$$

and the **defect** of $r$ is $\delta(r)\alpha(r)$; the signed sandwich is $\Sigma^\alpha_{r,s} = L_rR_s\alpha$.

## The Adjoint of the Signed Left Multiplication

**Theorem (the explicit form).** For every $r$, the signed left multiplication is adjointable with

$$
(\ell_r)^\dagger = \ell_{\delta(r)} , \qquad (\ell_r)^\dagger(x) = \delta(r)\,\alpha(x) ,
$$

and the signed right multiplication satisfies $(\varrho_s)^\dagger = \varrho_{\delta(s)}$; hence the adjoint of a signed one-sided multiplication is the signed one-sided multiplication by the conjugate parameter.

**Proof.** $\ell_r = L_r\alpha = \Sigma^\alpha_{r,1}$, so its adjoint is $\Sigma^\alpha_{\delta(r),\delta(1)} = \Sigma^\alpha_{\delta(r),1} = \ell_{\delta(r)}$ by *The Signed Adjoint Sandwich on a Banach Algebra*, using $\delta(1) = 1$; the right-handed computation is the mirror, $\varrho_s = R_s\alpha = \Sigma^\alpha_{1,\delta^{-1}(s)}$ with the conjugate parameter $\delta(s)$. $\square$

**Corollary (the regular graded module).** The algebra $A$ is a graded left module over itself through $\ell$, and the map $r \mapsto \ell_r$ is a homomorphism of the graded algebra into the graded operator algebra: $\ell_{rs} = \ell_r\ell_{\delta^{-1}(s)}$, and the involution and the adjoint agree on the image, $(\ell_r)^\dagger = \ell_{\delta(r)}$. The signed sandwich is the one-sided operator followed by a right multiplication,

$$
\Sigma^\alpha_{r,s} = \ell_r\,R_s ,
$$

so the adjoint of the two-sided operator is read from the one-sided and the right multiplication.

**Proof.** $\ell_r\ell_{t}(x) = \ell_r(t\alpha(x)) = r\alpha(t\alpha(x)) = r\alpha(t)x = \Sigma^\alpha_{r\alpha(t),1}(x)$, giving the composition law $\ell_r\ell_t = \ell_{r\alpha(t)}$, that is $\ell_{rs} = \ell_r\ell_{\delta^{-1}(s)}$ after the substitution $s = \alpha(t)$; the sandwich identity is associativity, and the adjoint of the composite is the composite of the adjoints by anti-multiplicativity. $\square$

## The Dictionary

**Theorem (self-adjoint, unitary, involutive).** For every $r$,

$$
\ell_r \text{ self-adjoint} \iff \delta(r) = r \ (\text{modulo the kernel}) , \qquad \ell_r \text{ unitary} \iff \delta(r)\,\alpha(r) = 1 ,
$$

$$
\ell_r \text{ an involution} \iff \ell_r^2 = \mathrm{id} , \ \ell_r \text{ self-adjoint} .
$$

The self-adjoint signed left multiplications are those with $r$ fixed by $\delta$, the unitary ones are those with $\delta(r)\alpha(r) = 1$, and the involutions are the self-adjoint ones with $\ell_r^2 = \mathrm{id}$, that is $r\alpha(r) = 1$.

**Proof.** $\ell_r$ is self-adjoint iff $\ell_{\delta(r)} = \ell_r$, which is the kernel condition on the parametrisation of the one-sided operators, and it is the identity $\delta(r) = r$ modulo the kernel; $\ell_r$ is unitary iff $\ell_{\delta(r)}\ell_r = \ell_{\delta(r)\alpha(r)} = \mathrm{id}$, that is $\delta(r)\alpha(r) = 1$; and $\ell_r^2 = \mathrm{id}$ is $r\alpha(r) = 1$, with self-adjointness from the previous line. $\square$

**Theorem (assembly of the two-sided operator).** Every signed sandwich is the composite of a signed left multiplication and a signed right multiplication,

$$
\Sigma^\alpha_{r,s} = \ell_r\,R_s = L_r\,\varrho_s ,
$$

and its adjoint is $\Sigma^\alpha_{\delta(r),\delta(s)} = \ell_{\delta(r)}R_{\delta(s)}$, so the two-sided adjoint is recovered from the one-sided adjoints and the commutation of the left and right multiplications.

**Proof.** The identities are associativity; the adjoint of the composite is the composite of the adjoints by anti-multiplicativity, $(L_r\varrho_s)^\dagger = \varrho_{\delta(s)}^\dagger L_{\delta(r)}^\dagger = R_{\delta(s)}L_{\delta(r)} = \Sigma^\alpha_{\delta(r),\delta(s)}$. $\square$

## Examples

**Example (the matrix algebra).** For $A = M_n(\mathbb{C})$ with the transpose-involution and the trace form, the signed left multiplication by $X$ has adjoint the signed left multiplication by $\delta(X) = X^{\mathsf{T}}$ in the graded sense; the self-adjoint signed left multiplications are the symmetric graded multiplications, and the unitary ones satisfy $\delta(X)\alpha(X) = 1$.

**Example (the commutative algebra).** For a commutative $A$ the kernel of the one-sided parametrisation is trivial on the units, the self-adjoint signed left multiplication is exactly $\delta(r) = r$, and the unitarity condition reads $\delta(r)\alpha(r) = 1$; the Cayley transform of *Adjoints in a Banach Algebra* produces a family of unitary signed left multiplications from the self-adjoint ones.

**Example (the group algebra).** For the group algebra of a finite group with $\alpha(g) = g$, $\delta(g) = g^{-1}$ on the group elements, the signed left multiplication by a group element $g$ has adjoint the signed left multiplication by $g^{-1}$; it is unitary because $\delta(g)\alpha(g) = 1$, and the regular graded module is the group algebra acting on itself.

## Summary

The signed left multiplication $\ell_r(x) = r\alpha(x)$ is adjointable with $(\ell_r)^\dagger = \ell_{\delta(r)}$, and the signed right multiplication satisfies $(\varrho_s)^\dagger = \varrho_{\delta(s)}$; the adjoint sends the parameter to its conjugate under $\delta = \sigma\alpha$. The algebra is a graded left module over itself through $\ell$, the composition is $\ell_{rs} = \ell_r\ell_{\delta^{-1}(s)}$, and the signed sandwich is the composite $\Sigma^\alpha_{r,s} = \ell_rR_s$ of the one-sided and the right multiplication, so the two-sided adjoint is recovered from the one-sided ones. The dictionary holds: $\ell_r$ is self-adjoint exactly when $\delta(r) = r$ modulo the kernel, unitary exactly when the defect $\delta(r)\alpha(r)$ is the unit, and an involution exactly when it is self-adjoint with $r\alpha(r) = 1$. The reflection is the special case $s = \delta(r)^{-1}$ of *The Signed Adjoint of the Reflection on a Banach Algebra*, and the module case is *The Graded Adjoint Action on a Graded Module*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\ell_r(x) = r\alpha(x)$ | The signed left multiplication |
| $\varrho_s(x) = \alpha(x)s$ | The signed right multiplication |
| $\delta = \sigma\alpha = \alpha\sigma$ | The composite involution |
| $(\ell_r)^\dagger = \ell_{\delta(r)}$ | The signed adjoint of the left multiplication |
| $\ell_{rs} = \ell_r\ell_{\delta^{-1}(s)}$ | Composition of the signed left multiplications |
| $\delta(r) = r$ modulo kernel | Criterion for self-adjointness |
| $\delta(r)\alpha(r) = 1$ | Criterion for unitarity |
| $\Sigma^\alpha_{r,s} = \ell_rR_s$ | Assembly of the two-sided operator |

## Further Reading

- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the graded left multiplications and the involutions.
- F. R. Gantmacher, *The Theory of Matrices, Volume I* (Chelsea, 1959), for the one-sided multiplications and their adjoints with respect to a trace form.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume II* (Cambridge University Press, 2001), for the `*`-representations and the involutions of the multiplications.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the one-sided multiplications and their adjoints.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the operators of a Banach algebra and the adjoints with respect to a form.
