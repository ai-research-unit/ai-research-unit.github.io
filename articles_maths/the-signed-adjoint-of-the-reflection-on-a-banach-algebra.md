
# __The Signed Adjoint of the Reflection on a Banach Algebra__

## Introduction

The **reflection** at a unit $u$ is the signed sandwich $\rho_u(x) = u\,\alpha(x)\,u^{-1}$, the operator that conjugates by $u$ in the graded sense; it is an automorphism of the algebra of order two exactly when $u$ is a graded involution, and it is the operator whose adjoint exhibits the signed phenomenon most sharply. Its adjoint with respect to the form of the category is the reflection at the conjugate parameter, $\rho_u^\dagger = \rho_{\delta(u)}$, $\delta = \sigma\alpha$; the reflection is therefore self-adjoint exactly when $\rho_{\delta(u)} = \rho_u$, that is when the **defect** $\delta(u)u^{-1}$ is central, and this can fail: the signed adjoint of the reflection is the first operator of the block whose self-adjointness is a condition on the parameter and not a tautology. This article computes the adjoint of the reflection, derives the self-adjointness and unitarity conditions, and records the failure.

The article assumes the reflection, its composition, its inverse and its group from *The Signed Reflection on a Banach Algebra* and *The Signed Sandwich on a Banach Algebra*; the grade involution $\alpha$ and the composite $\delta = \sigma\alpha$ from *The Grade Involution on a Banach Algebra* and *The Signed Left Multiplication on an Involutive Banach Algebra*; the form of the category and the adjoint from *The Involution on the Operator Algebra*; the adjoint of the signed sandwich from *The Signed Adjoint Sandwich on a Banach Algebra*; the involution $\sigma$, the unitary elements and the Cayley transform from *Adjoints in a Banach Algebra*; and the operator theory of the reflection from *Reflections as Signed Two-Sided Operators on a Banach Algebra*. The graded module case is *The Graded Adjoint Action on a Graded Module*.

Throughout, $A$ is a unital Banach algebra over $\mathbb{C}$ with the grade involution $\alpha$ and the involution $\sigma$, with $\sigma\alpha = \alpha\sigma$ and $\delta = \sigma\alpha = \alpha\sigma$; the form of the category is $\{x,y\} = \tau(x\sigma(y))$ with $\tau$ a continuous $\sigma$-invariant and $\alpha$-invariant trace, and $\alpha^\dagger = \alpha$; the **reflection** at the unit $u$ is

$$
\rho_u = \Sigma^\alpha_{u,u^{-1}} , \qquad \rho_u(x) = u\,\alpha(x)\,u^{-1} ;
$$

the **defect** of $u$ is $\delta(u)u^{-1}$; and the **conjugate parameter** is $\delta(u)$.

## The Adjoint of the Reflection

**Theorem (the explicit form).** For every unit $u$, the reflection is adjointable and

$$
(\rho_u)^\dagger = \rho_{\delta(u)} , \qquad (\rho_u)^\dagger(x) = \delta(u)\,\alpha(x)\,\delta(u)^{-1} .
$$

The adjoint of a reflection is the reflection at the image of the parameter under the composite $\delta = \sigma\alpha$.

**Proof.** The reflection is the signed sandwich $\Sigma^\alpha_{u,u^{-1}}$, whose adjoint is $\Sigma^\alpha_{\delta(u),\delta(u^{-1})} = \Sigma^\alpha_{\delta(u),\delta(u)^{-1}}$ by *The Signed Adjoint Sandwich on a Banach Algebra*; this is exactly $\rho_{\delta(u)}$. $\square$

**Corollary (the reflection group and the adjoint).** The adjoint map $u \mapsto \delta(u)$ on the reflection group is an automorphism, $(\rho_u\rho_v)^\dagger = \rho_{\delta(u)}\rho_{\delta(v)}$ and $(\rho_u)^{-1\,\dagger} = \rho_{\delta(u)^{-1}}$; the reflection group maps under the adjoint by the automorphism $\delta$ of the unit group, and the reflection $\rho_1 = \mathrm{id}$ has adjoint $\rho_1$.

**Proof.** The adjoint is anti-multiplicative on the operators and multiplicative on the parameters, and $\rho_u\rho_v = \Sigma^\alpha_{u,u^{-1}}\Sigma^\alpha_{v,v^{-1}} = \rho_{uv}$; the identity reflection is fixed. $\square$

## Self-Adjointness and Unitarity

**Theorem (the centrality criterion).** The reflection $\rho_u$ is self-adjoint if and only if the defect $\delta(u)u^{-1}$ is central:

$$
(\rho_u)^\dagger = \rho_u \iff \delta(u)u^{-1} \in Z(A) \quad (\text{a central unit}) .
$$

Hence $\rho_u$ is self-adjoint whenever $\delta(u) = u$, and in particular whenever $u$ is a fixed point of $\delta$; the self-adjointness fails for a unit whose defect is not central.

**Proof.** $\rho_{\delta(u)} = \rho_u$ iff the two parametrising units differ by a central unit, because the parametrisation of the reflection group has kernel the central units: $\rho_p = \rho_q$ iff $q^{-1}p$ is central. With $p = \delta(u)$ and $q = u$ this is the centrality of $u^{-1}\delta(u)$, equivalently of $\delta(u)u^{-1}$. $\square$

**Theorem (unitarity).** The reflection $\rho_u$ is unitary, $(\rho_u)^\dagger\rho_u = \rho_u(\rho_u)^\dagger = \mathrm{id}$, if and only if the defect is central and $\delta(u) = u^{-1}$ modulo the centre; equivalently, $\rho_u$ is unitary if and only if $\rho_{\delta(u)} = \rho_{u^{-1}}$, that is the adjoint is the inverse reflection.

**Proof.** $\rho_u$ is unitary iff $(\rho_u)^\dagger = (\rho_u)^{-1} = \rho_{u^{-1}}$; by the explicit form of the adjoint this is $\rho_{\delta(u)} = \rho_{u^{-1}}$, that is $u\,\delta(u) = u\,\delta(u)$... the condition reads $\rho_{\delta(u)} = \rho_{u^{-1}}$; modulo the centre of the parametrisation this is $\delta(u) = u^{-1}$, and the defect $\delta(u)u^{-1} = u^{-2}$ being central is the centrality condition. $\square$

## The Failure and Examples

**Proposition (the failure of self-adjointness).** Let $u$ be a unit with $\delta(u)u^{-1}$ not central. Then $\rho_u$ is not self-adjoint and the signed adjoint of the reflection is a genuinely different reflection; the obstruction is the commutant of the defect, and it vanishes for a commutative algebra and for a unit fixed by $\delta$.

**Proof.** Immediate from the centrality criterion; a non-central defect gives $\rho_{\delta(u)} \neq \rho_u$, and the number of distinct reflections in the class of $u$ is measured by the class group of $A$ by the central units. $\square$

**Example (the matrix algebra).** For $A = M_n(\mathbb{C})$ with the transpose-involution and the trace form, the reflections are the conjugations $x \mapsto uxu^{-1}$ in the graded sense; the defect $\delta(u)u^{-1} = u^{-1}u^{-1}\cdot$... is central exactly when the corresponding conjugation is self-adjoint, and for a graded reflection with $u^2 = 1$ and $\delta(u) = u$ the operator is self-adjoint.

**Example (the commutative algebra).** For a commutative $A$ every unit is central, so every reflection is self-adjoint; the signed adjoint of the reflection is the reflection at $\delta(u)$, and on a commutative algebra the whole signed theory collapses to the unsigned one twisted by $\delta$.

**Example (the group algebra).** For the group algebra of a finite group with $\delta(g) = g^{-1}$ on the group elements, the reflection at a group element is the conjugation; the defect $g^{-2}$ is central exactly when $g^2$ is central, and the self-adjointness of the reflection is the condition that the conjugation by $g$ is a self-adjoint operator, a condition on the conjugacy class of $g$.

## The Reflection and the Cayley Transform

**Proposition (Cayley and the reflections).** From a self-adjoint signed left multiplication $\ell_r$ with $\delta(r) = r$, the Cayley transform produces the unitary $u = (r-i)(r+i)^{-1}$ of the graded algebra, and the corresponding reflection $\rho_u$ is self-adjoint. The failure of self-adjointness of a reflection is therefore a failure of its unitary to be fixed by $\delta$ modulo the centre, not a failure of the correspondence between the reflections and the unitaries.

**Proof.** The Cayley transform of a self-adjoint element is unitary, and since $\delta(r) = r$ and $\delta$ is a real-linear automorphism fixing $i$, one has $\delta(u) = u$, so the defect $\delta(u)u^{-1} = 1$ is central and $\rho_u$ is self-adjoint by the centrality criterion. $\square$

**Example (the unitary group and the reflections).** For a $\mathrm{C}^*$-algebra the Cayley transform maps the self-adjoint operators onto the unitary operators with $1$ removed, and the corresponding reflections form the self-adjoint part of the reflection group; the complement consists of the reflections at the unitaries whose defect $\delta(u)u^{-1}$ is not central.

## Summary

The reflection $\rho_u(x) = u\alpha(x)u^{-1}$ is adjointable with $(\rho_u)^\dagger = \rho_{\delta(u)}$, the reflection at the conjugate parameter $\delta = \sigma\alpha$; the adjoint map on the reflection group is the automorphism $\delta$ of the unit group, and it fixes the identity. The reflection is self-adjoint exactly when the defect $\delta(u)u^{-1}$ is central, so it is self-adjoint whenever $\delta(u) = u$, and it can fail: a unit with a non-central defect gives a reflection different from its adjoint, the obstruction vanishing for a commutative algebra and for the units fixed by $\delta$. The reflection is unitary when the defect is central and $\delta(u) = u^{-1}$ modulo the centre, that is when the adjoint is the inverse reflection. The operator theory of the reflection is *Reflections as Signed Two-Sided Operators on a Banach Algebra*, and the one-sided case is *The Signed Adjoint of the Left Multiplication on an Involutive Banach Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho_u(x) = u\alpha(x)u^{-1}$ | The reflection at the unit $u$ |
| $\delta = \sigma\alpha = \alpha\sigma$ | The composite involution |
| $(\rho_u)^\dagger = \rho_{\delta(u)}$ | The signed adjoint of the reflection |
| $\delta(u)u^{-1}$ | The defect |
| $\delta(u)u^{-1}$ central | Criterion for self-adjointness |
| $\rho_{\delta(u)} = \rho_{u^{-1}}$ | Criterion for unitarity |
| Failure | Non-central defect ⇒ $\rho_u$ not self-adjoint |
| Cayley $u = (r-i)(r+i)^{-1}$ | Unitary from self-adjoint $\ell_r$; $\rho_u$ self-adjoint |

## Further Reading

- F. R. Gantmacher, *The Theory of Matrices, Volume I* (Chelsea, 1959), for the conjugation operators and their adjoints with respect to a trace form.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the graded reflections and the central defects.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume II* (Cambridge University Press, 2001), for the involutions, the conjugations and their adjoints.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the inner automorphisms and the self-adjointness conditions.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the operators of a Banach algebra and the central units.
