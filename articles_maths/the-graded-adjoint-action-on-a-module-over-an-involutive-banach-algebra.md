
# __The Graded Adjoint Action on a Graded Module__

## Introduction

The signed left multiplication of the algebra on itself is the regular case of the **graded adjoint action** on a graded module: a graded left module $M$ over the signed Banach algebra $A$, with a form and a grading operator $\gamma$, carries the action $\ell_r^\pi(m) = \pi(r)\gamma(m)$, where $\pi$ is a representation of $A$ and $\gamma$ implements the grade involution of the module, and the adjoint of the action is the action by the conjugate element, $(\ell_r^\pi)^\dagger = \ell_{\delta(r)}^\pi$, provided the representation is a `*`-representation and the grading operator is self-adjoint. This is the module-level form of the whole `- * Operator Theory` block: the regular module $M = A$ recovers the signed left multiplication of the preceding article, the module structure carries the graded commutant, and the adjoint action is the operator that makes the module a `*`-module over the signed algebra. This article develops the graded module, the adjoint action, and the reduction to the regular case.

The article assumes the graded module, the representation and the grading operator from *The Graded Action on a Module over an Involutive Banach Algebra*, which owns the module; the signed left multiplication and the composite $\delta = \sigma\alpha$ from *The Signed Left Multiplication on an Involutive Banach Algebra* and *The Signed Adjoint of the Left Multiplication on an Involutive Banach Algebra*; the form of the category and the adjoint from *The Involution on the Operator Algebra*; the `*`-representation of the algebra and the self-adjoint operators from *Adjoints in a Banach Algebra* and *Self-Adjoint Operators of a Banach Algebra*; and the module theory of the operator algebra from *Modules over the Operator Algebra* and *Bimodules over the Operator Algebra*.

Throughout, $A$ is a unital Banach algebra over $\mathbb{C}$ with the grade involution $\alpha$ and the involution $\sigma$, with $\sigma\alpha = \alpha\sigma$ and $\delta = \sigma\alpha = \alpha\sigma$; the form of the category is $\{x,y\} = \tau(x\sigma(y))$ with $\tau$ a continuous $\sigma$-invariant and $\alpha$-invariant trace, and $\alpha^\dagger = \alpha$; $M$ is a graded left $A$-module with a form $\{\cdot,\cdot\}_M$ and a **grading operator** $\gamma \in \mathrm{End}(M)$, self-adjoint, $\gamma^2 = 1$, $\gamma^\dagger = \gamma$; $\pi : A \to \mathrm{End}(M)$ is a representation, assumed to be a `*`-representation $\pi(\sigma(r)) = \pi(r)^\dagger$ and **semilinear** for the grading, $\pi(\alpha(r))\gamma = \gamma\pi(r)$; and the **graded adjoint action** is

$$
\ell_r^\pi = \pi(r)\gamma , \qquad \ell_r^\pi(m) = \pi(r)\gamma(m) .
$$

## The Graded Module and the Adjoint Action

**Definition.** A **graded left $A$-module** is a module $M$ with a grading operator $\gamma$ of order two and a representation $\pi$ of $A$ that is semilinear for $\gamma$, $\pi(\alpha(r))\gamma = \gamma\pi(r)$; it is a **`*`-module** when $\pi$ is a `*`-representation for a form on $M$.

**Proposition (the module structure).** The graded adjoint action satisfies $\ell_{rs}^\pi = \ell_r^\pi\ell_{\delta^{-1}(s)}^\pi$ and $\ell_{r+t}^\pi = \ell_r^\pi + \ell_t^\pi$; with the grading operator $\gamma = \alpha$ on the regular module $M = A$ and $\pi$ the left regular representation, the action $\ell_r^\pi$ is the signed left multiplication $\ell_r$, so the regular case is recovered.

**Proof.** $\ell_r^\pi\ell_t^\pi = \pi(r)\gamma\pi(t)\gamma = \pi(r)\pi(\alpha(t))\gamma^2 = \pi(r\alpha(t))$, which is $\ell_{r\alpha(t)}^\pi$, giving the composition law after $\alpha(t) = \delta^{-1}(s)$; additivity is the linearity of $\pi$; and on the regular module $\pi(r) = L_r$, $\gamma = \alpha$, so $\ell_r^\pi = L_r\alpha = \ell_r$. $\square$

**Theorem (the adjoint of the graded action).** For every $r$, the graded adjoint action is adjointable and

$$
\bigl(\ell_r^\pi\bigr)^\dagger = \ell_{\delta(r)}^\pi , \qquad \bigl(\ell_r^\pi\bigr)^\dagger(m) = \pi(\delta(r))\gamma(m) ,
$$

the graded adjoint action by the conjugate element $\delta(r)$; the adjoint is the action conjugated by the composite involution.

**Proof.** The adjoint is anti-multiplicative, $\gamma^\dagger = \gamma$ and $\pi(\sigma(r)) = \pi(r)^\dagger$, so $\bigl(\pi(r)\gamma\bigr)^\dagger = \gamma^\dagger\pi(r)^\dagger = \gamma\pi(\sigma(r))$; by semilinearity $\gamma\pi(\sigma(r)) = \pi(\alpha(\sigma(r)))\gamma = \pi(\delta(r))\gamma$ (using $\alpha\sigma = \sigma\alpha$), which is $\ell_{\delta(r)}^\pi$. Uniqueness is the nondegeneracy of the module form. $\square$

## The Graded Commutant and the `*`-Structure

**Definition.** The **graded commutant** of the representation $\pi$ is

$$
\pi(A)^{\mathrm{g}} = \{T \in \mathrm{End}(M) : T\pi(r) = \pi(\delta(r))T \ \text{for all } r\} ,
$$

the operators that intertwine the representation with its conjugate; the **`*`-module structure** is the datum of $\pi$, $\gamma$ and the forms for which $\pi$ is a `*`-representation.

**Proposition (the commutant and the adjoint).** For a `*`-representation $\pi$ the graded commutant is closed under the adjoint when the module form is invariant, the adjoint of $\ell_r^\pi$ is $\ell_{\delta(r)}^\pi$, and $\ell_r^\pi$ is self-adjoint exactly when $\delta(r) = r$; it is unitary in the graded sense exactly when the defect $\delta(r)\alpha(r)$ is the unit of the module, i.e. $\pi(\delta(r)\alpha(r)) = \mathrm{id}_M$.

**Proof.** The adjoint of $\ell_r^\pi$ is $\ell_{\delta(r)}^\pi$; self-adjointness is $\pi(\delta(r)) = \pi(r)$, i.e. $\delta(r) = r$ on the image of $\pi$; unitarity is $\bigl(\ell_r^\pi\bigr)^\dagger\ell_r^\pi = \pi(\delta(r)\alpha(r)) = \mathrm{id}_M$ by the composition law. The closure of the commutant under the adjoint is the standard compatibility of an intertwining relation with the adjoint for a `*`-representation. $\square$

**Remark (the reduction to the regular module).** On the regular module $M = A$ with $\pi$ the left regular representation and $\gamma = \alpha$, the graded commutant is the set of $T$ with $T L_r = L_{\delta(r)}T$, the *-module structure is the form of the category, and the whole theory of *The Signed Adjoint of the Left Multiplication on an Involutive Banach Algebra* is the special case of the present article; the two-sided operators are the composites of the graded adjoint action with the right multiplications, *The Signed Adjoint Sandwich on a Banach Algebra*.

## Examples

**Example (the regular module).** $M = A$, $\pi$ the left regular representation, $\gamma = \alpha$: the graded adjoint action is the signed left multiplication, its adjoint is the action by $\delta(r)$, and the graded commutant is generated by the right multiplications (up to the kernel), giving the commutant description of the two-sided operators.

**Example (the matrix module).** $M = \mathbb{C}^n$ as a graded module over $A = M_n(\mathbb{C})$ with the grading $\gamma$ a self-adjoint involution, $\pi$ the defining representation: the graded adjoint action is the standard graded matrix action, its adjoint is the action of the transposed matrix, and the self-adjointness condition is the symmetry of the matrix in the graded sense.

**Example (the Hilbert module).** Let $M$ be a Hilbert space and $\pi$ a `*`-representation of a $\mathrm{C}^*$-algebra with $\gamma$ a self-adjoint unitary; the graded adjoint action is a bounded operator, its adjoint is the action by $\delta(r)$, and the graded commutant is a von Neumann algebra when $\pi(A)$ is closed, the graded commutant of *Involutive Operator Algebras and the Commutant*.

## Summary

A graded left module over the signed Banach algebra $A$ carries the grading operator $\gamma$, self-adjoint of order two, and the semilinear `*`-representation $\pi$; the graded adjoint action $\ell_r^\pi = \pi(r)\gamma$ is adjointable with $(\ell_r^\pi)^\dagger = \ell_{\delta(r)}^\pi$, the action by the conjugate element $\delta = \sigma\alpha$, under the hypotheses that $\pi$ is a `*`-representation and $\gamma$ is self-adjoint. The composition is $\ell_r^\pi\ell_t^\pi = \ell_{r\alpha(t)}^\pi$, and on the regular module $M = A$ with $\pi$ the left regular representation and $\gamma = \alpha$ the action reduces to the signed left multiplication of *The Signed Adjoint of the Left Multiplication on an Involutive Banach Algebra*, with the two-sided operators recovered as the composites with the right multiplications. The graded commutant consists of the operators intertwining $\pi$ with its conjugate, and for a `*`-representation it is closed under the adjoint; the action is self-adjoint exactly when $\delta(r) = r$ and unitary exactly when the defect $\delta(r)\alpha(r)$ acts as the identity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M$, $\gamma$, $\pi$ | Graded module, grading operator, representation |
| $\pi(\alpha(r))\gamma = \gamma\pi(r)$ | Semilinearity for the grading |
| $\ell_r^\pi = \pi(r)\gamma$ | The graded adjoint action |
| $\bigl(\ell_r^\pi\bigr)^\dagger = \ell_{\delta(r)}^\pi$ | The adjoint of the graded action |
| $\ell_r^\pi\ell_t^\pi = \ell_{r\alpha(t)}^\pi$ | Composition |
| $\pi(A)^{\mathrm{g}}$ | The graded commutant |
| $M = A$, $\pi = L$, $\gamma = \alpha$ | The regular module, reducing to 26 |
| $\delta(r) = r$; $\pi(\delta(r)\alpha(r)) = \mathrm{id}$ | Self-adjointness; unitarity |

## Further Reading

- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the graded modules and the graded commutants.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume II* (Cambridge University Press, 2001), for the `*`-representations and the modules over involutive Banach algebras.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the `*`-representations on Hilbert space and the commutants.
- F. R. Gantmacher, *The Theory of Matrices, Volume I* (Chelsea, 1959), for the graded matrix actions and their adjoints.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the representations, the modules and the adjoints with respect to a form.
