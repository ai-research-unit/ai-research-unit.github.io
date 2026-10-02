
# __The Signed Adjoint Sandwich on a Banach Algebra__

## Introduction

The **signed sandwich** $\Sigma^\alpha_{a,b}(x) = a\,\alpha(x)\,b$ is the two-sided multiplication twisted by the grade involution $\alpha$, and its adjoint with respect to the form of the category is the signed sandwich of the **conjugate parameters**: $(\Sigma^\alpha_{a,b})^\dagger = \Sigma^\alpha_{\delta(a),\delta(b)}$, where $\delta = \sigma\alpha$ is the composite of the involution $\sigma$ with the grade involution. The formula is the adjoint of the general two-sided operator, and the unsigned, reflection and one-sided cases are its specialisations; from it one reads the whole dictionary — the inverse, the composition, the unitarity and the self-adjointness — and one meets the first genuinely signed phenomenon: the unitarity of the signed sandwich is governed not by the unitarity of the parameters but by the centrality of the defect $\delta(a)\alpha(a)$. This article computes the adjoint of the signed sandwich, derives the composition and unitarity conditions, and identifies the specialisations.

The article assumes the signed sandwich on a Banach algebra, its composition table, its inverse and its group of units from *The Signed Sandwich on a Banach Algebra*, which owns the operator; the grade involution $\alpha$ and the automorphism it induces from *The Grade Involution on a Banach Algebra*; the form of the category, the adjoint and the self-adjoint and skew operators from *The Involution on the Operator Algebra*; the adjoint of the left and right multiplications from *The Adjoint of the Left Multiplication on an Involutive Banach Algebra*; the involution $\sigma$ and the self-adjoint and unitary elements from *Adjoints in a Banach Algebra*; and the composite $\delta = \sigma\alpha$ from *The Adjoint of the Left Multiplication on an Involutive Banach Algebra* and *The Signed Left Multiplication on an Involutive Banach Algebra*. The graded module case is *The Graded Adjoint Action on a Graded Module*.

Throughout, $A$ is a unital Banach algebra over $\mathbb{C}$ with the **grade involution** $\alpha$, an automorphism of order two, and the **involution** $\sigma$, a continuous anti-automorphism of order two, with $\sigma\alpha = \alpha\sigma$, so that $\delta = \sigma\alpha = \alpha\sigma$ is a continuous anti-automorphism of order two; the form of the category is $\{x,y\} = \tau(x\sigma(y))$ for a continuous $\sigma$-invariant trace $\tau$, assumed also **$\alpha$-invariant**, $\tau\circ\alpha = \tau$, and $\alpha$ is assumed **self-adjoint** for the form, $\{\alpha x,y\} = \{x,\alpha y\}$, equivalently $\alpha^\dagger = \alpha$; the signed sandwich is

$$
\Sigma^\alpha_{a,b} = L_aR_b\alpha , \qquad \Sigma^\alpha_{a,b}(x) = a\,\alpha(x)\,b ,
$$

with $L_a(x) = ax$ and $R_b(x) = xb$; the **conjugate parameters** of $(a,b)$ are $(\delta(a),\delta(b))$.

## The Adjoint of the Signed Sandwich

**Theorem (the explicit form).** For all $a,b$ the signed sandwich is adjointable, with

$$
\bigl(\Sigma^\alpha_{a,b}\bigr)^\dagger = \Sigma^\alpha_{\delta(a),\delta(b)} ,
$$

the signed sandwich of the conjugate parameters $(\delta(a),\delta(b))$; the order of the parameters is restored rather than reversed.

**Proof.** The adjoint is anti-multiplicative, and $\alpha$, $L$, $R$ have adjoints $\alpha^\dagger = \alpha$, $(L_a)^\dagger = L_{\sigma(a)}$, $(R_b)^\dagger = R_{\sigma(b)}$, so

$$
\bigl(L_aR_b\alpha\bigr)^\dagger = \alpha^\dagger R_b{}^\dagger L_a{}^\dagger = \alpha R_{\sigma(b)}L_{\sigma(a)} = \alpha L_{\sigma(a)}R_{\sigma(b)} ,
$$

using that the left and right multiplications commute. Moving $\alpha$ to the right through $L_{\sigma(a)}$ and $R_{\sigma(b)}$ gives $\alpha L_{\sigma(a)}R_{\sigma(b)} = L_{\alpha(\sigma(a))}R_{\alpha(\sigma(b))}\alpha = L_{\delta(a)}R_{\delta(b)}\alpha$, which is $\Sigma^\alpha_{\delta(a),\delta(b)}$; the adjoint exists and is this operator by the nondegeneracy of the form. $\square$

**Corollary (the specialisations).** The adjoint of the unsigned sandwich $\Sigma_{a,b} = L_aR_b$ is $\Sigma_{\sigma(a),\sigma(b)}$, recovered by $\alpha = \mathrm{id}$; the adjoint of the reflection $\rho_u = \Sigma^\alpha_{u,u^{-1}}$ is $\rho_{\delta(u)}$; and the adjoint of the signed left multiplication $\ell_a = \Sigma^\alpha_{a,1}$ is $\ell_{\delta(a)}$. The three computations agree with the direct ones on the one-sided and reflection operators.

**Proof.** Set $\alpha = \mathrm{id}$ in the theorem for the unsigned case, giving $\delta = \sigma$; set $b = a^{-1}$ and use that $\Sigma^\alpha_{a,a^{-1}}$ is the reflection; set $b = 1$. $\square$

## Composition, Inverse and Unitarity

**Theorem (composition and inverse).** The signed sandwiches form a monoid under composition with

$$
\Sigma^\alpha_{p,q}\circ\Sigma^\alpha_{r,s} = \Sigma^\alpha_{p\,\alpha(r),\,\alpha(s)\,q} ,
$$

as in the operator theory of the signed sandwich; the inverse of $\Sigma^\alpha_{a,b}$ for invertible $a,b$ is $\Sigma^\alpha_{\alpha(a)^{-1},\alpha(b)^{-1}}$, and the adjoint of the inverse is $(\Sigma^\alpha_{a,b})^{\dagger\,-1} = \Sigma^\alpha_{\delta(a)^{-1},\delta(b)^{-1}} = \bigl(\Sigma^\alpha_{a,b}{}^{-1}\bigr)^\dagger$ when $a,b$ and $\delta(a),\delta(b)$ are invertible.

**Proof.** The composition table is the computation $\Sigma^\alpha_{p,q}\Sigma^\alpha_{r,s} = L_pR_q\alpha L_rR_s\alpha = L_pR_qL_{\alpha(r)}R_{\alpha(s)}\alpha^2 = L_{p\alpha(r)}R_{\alpha(s)q}$, using $\alpha L_r = L_{\alpha(r)}\alpha$, $R_qL_{\alpha(r)} = L_{\alpha(r)}R_q$ and $\alpha^2 = \mathrm{id}$; the inverse is the two-sided application, and the adjoint of the inverse is the inverse of the adjoint because the adjoint is an anti-automorphism of order two. $\square$

**Theorem (the unitarity defect).** The signed sandwich $\Sigma^\alpha_{a,b}$ is **unitary**, $\bigl(\Sigma^\alpha_{a,b}\bigr)^\dagger\Sigma^\alpha_{a,b} = \Sigma^\alpha_{a,b}\bigl(\Sigma^\alpha_{a,b}\bigr)^\dagger = \mathrm{id}$, if and only if the **defect** $\delta(a)\alpha(a)$ is a central unit and

$$
\alpha(b)\,\delta(b) = \bigl(\delta(a)\,\alpha(a)\bigr)^{-1} .
$$

Equivalently, $\Sigma^\alpha_{a,b}$ is unitary if and only if $\delta(a)\alpha(a)$ is central and $\alpha(b)\delta(b)$ is its inverse; in particular, when the parameters are **unitary** and $\delta = \sigma\alpha$ acts as inversion on them, $\delta(a)\alpha(a) = 1 = \alpha(b)\delta(b)$ and the sandwich is unitary.

**Proof.** By the composition table, $\bigl(\Sigma^\alpha_{a,b}\bigr)^\dagger\Sigma^\alpha_{a,b} = \Sigma^\alpha_{\delta(a),\delta(b)}\Sigma^\alpha_{a,b} = \Sigma^\alpha_{\delta(a)\alpha(a),\,\alpha(b)\delta(b)}$. The operator $\Sigma^\alpha_{u,v} = L_uR_v$ evaluated on $1$ is $uv$, so $\Sigma^\alpha_{u,v} = \mathrm{id}$ forces $uv = 1$ and hence $v = u^{-1}$ and $u$ central (from the identity $uxv = x$ for all $x$); thus the product is the identity exactly when $u = \delta(a)\alpha(a)$ is a central unit with inverse $v = \alpha(b)\delta(b)$. The second product gives the same condition, and the specialisation is $\delta(a)\alpha(a) = \sigma(\alpha(a))\alpha(a) = 1$ when $\alpha(a)$ is unitary. $\square$

## Examples

**Example ($\alpha = \mathrm{id}$: the unsigned sandwich).** The signed sandwich reduces to $L_aR_b$, the adjoint to $\Sigma_{\sigma(a),\sigma(b)}$, and the unitarity condition to $a$ and $b$ unitary with $\sigma$ the inverse; the unsigned case is *The Adjoint of the Left Multiplication on an Involutive Banach Algebra*.

**Example ($b = a^{-1}$: the reflection).** The reflection $\rho_u = \Sigma^\alpha_{u,u^{-1}}$ has adjoint $\rho_{\delta(u)}$, so it is self-adjoint exactly when $\rho_{\delta(u)} = \rho_u$, that is when the defect $\delta(u)u^{-1}$ is central; a computation deferred to *The Signed Adjoint of the Reflection on a Banach Algebra*.

**Example ($b = 1$: the signed left multiplication).** The signed left multiplication $\ell_a = \Sigma^\alpha_{a,1}$ has adjoint $\ell_{\delta(a)}$, with unitarity condition the centrality of $\delta(a)\alpha(a)$, deferred to *The Signed Adjoint of the Left Multiplication on an Involutive Banach Algebra*.

**Example (the matrix algebra).** For $A = M_n(\mathbb{C})$ with the transpose-involution and the trace form, the signed sandwich displays the centrality condition concretely: the defect is a scalar multiple of the identity exactly when the sandwich is unitary, and the graded sandwich is unitary precisely when its matrix is orthogonal or unitary in the graded sense.

## The Central Defect and the Unitarity Condition

**Definition.** The **unitarity defect** of the pair $(a,b)$ is the pair of products

$$
u = \delta(a)\alpha(a) , \qquad v = \alpha(b)\delta(b) ,
$$

and the **self-adjointness defect** is the departure of the parameters from being fixed by $\delta$.

**Proposition (the defects govern unitarity and self-adjointness).** The sandwich $\Sigma^\alpha_{a,b}$ is unitary if and only if $u$ is central and $v = u^{-1}$; it is self-adjoint if and only if $\delta(a) = a$ and $\delta(b) = b$ modulo the central kernel of the parametrisation. If the parameters are fixed by $\delta$ and by $\alpha$ and are involutions, both conditions hold.

**Proof.** The unitarity condition is the theorem of the article. For self-adjointness, $(\Sigma^\alpha_{a,b})^\dagger = \Sigma^\alpha_{\delta(a),\delta(b)} = \Sigma^\alpha_{a,b}$ holds exactly when the two parameter pairs differ by the kernel of the parametrisation, which is the set of central parameters; and when $\alpha(a) = \delta(a) = a$ with $a^2 = 1$ the defect is $u = a^2 = 1$, central with inverse $1$. $\square$

**Corollary (the centrality obstruction).** The unitarity of the signed sandwich fails exactly when the defect $\delta(a)\alpha(a)$ is not central, and its self-adjointness fails exactly when $\delta$ moves a parameter by more than a central unit; both obstructions vanish for a commutative algebra and for the parameters fixed by $\delta$ with an $\alpha$-symmetric defect.

## Summary

The signed sandwich $\Sigma^\alpha_{a,b}(x) = a\alpha(x)b$ is adjointable with respect to the form of the category, and its adjoint is the signed sandwich of the conjugate parameters, $(\Sigma^\alpha_{a,b})^\dagger = \Sigma^\alpha_{\delta(a),\delta(b)}$, $\delta = \sigma\alpha$, provided the grade involution is self-adjoint for the form and $\alpha\sigma = \sigma\alpha$. The composition is $\Sigma^\alpha_{p,q}\circ\Sigma^\alpha_{r,s} = \Sigma^\alpha_{p\alpha(r),\alpha(s)q}$, the inverse is $\Sigma^\alpha_{\alpha(a)^{-1},\alpha(b)^{-1}}$, and the adjoint of the inverse is the inverse of the adjoint. The sandwich is unitary exactly when the defect $\delta(a)\alpha(a)$ is a central unit with inverse $\alpha(b)\delta(b)$; the unsigned case, the reflection and the signed left multiplication are the specialisations $\alpha = \mathrm{id}$, $b = a^{-1}$ and $b = 1$. The reflection case is *The Signed Adjoint of the Reflection on a Banach Algebra* and the one-sided case *The Signed Adjoint of the Left Multiplication on an Involutive Banach Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha$, $\sigma$, $\delta = \sigma\alpha = \alpha\sigma$ | Grade involution, involution, their composite |
| $\Sigma^\alpha_{a,b}(x) = a\alpha(x)b$ | The signed sandwich |
| $\bigl(\Sigma^\alpha_{a,b}\bigr)^\dagger = \Sigma^\alpha_{\delta(a),\delta(b)}$ | The adjoint of the signed sandwich |
| $\Sigma^\alpha_{p,q}\circ\Sigma^\alpha_{r,s} = \Sigma^\alpha_{p\alpha(r),\alpha(s)q}$ | Composition |
| $\Sigma^\alpha_{a,b}{}^{-1} = \Sigma^\alpha_{\alpha(a)^{-1},\alpha(b)^{-1}}$ | Inverse |
| $\delta(a)\alpha(a)$ central, $\alpha(b)\delta(b) = (\delta(a)\alpha(a))^{-1}$ | Unitarity condition |
| $\alpha = \mathrm{id}$, $b = a^{-1}$, $b = 1$ | Unsigned, reflection, signed left multiplication |

## Further Reading

- F. R. Gantmacher, *The Theory of Matrices, Volume I* (Chelsea, 1959), for the two-sided multiplications, the adjoint with respect to a trace form and the graded matrices.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the graded involutions and the two-sided operators.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume II* (Cambridge University Press, 2001), for the involutions and the adjoints of the multiplications.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the two-sided multiplications and the unitarity conditions.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the operators of a Banach algebra and their adjoints.
