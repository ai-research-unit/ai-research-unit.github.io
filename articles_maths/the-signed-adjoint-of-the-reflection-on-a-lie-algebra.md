
# __The Signed Adjoint of the Reflection on a Lie Algebra__

## Introduction

A **reflection** of a graded Lie algebra is the signed conjugation $\rho_a = e^{\operatorname{ad}_a}\alpha$, and its adjoint with respect to an invariant Hermitian form that the grade involution preserves is its inverse: $\rho_a^{*} = \alpha e^{-\operatorname{ad}_a} = \rho_a^{-1}$. The reflection is therefore always a **unitary** operator of the form, and it is **self-adjoint** exactly when it is an involution, that is when $a + \alpha(a)$ is central; the reflection by an odd element satisfies this automatically, while the reflection by an even element need not. The article computes the adjoint, identifies the self-adjoint reflections with the involutive ones, and examines the three ways in which the self-adjointness fails.

This article treats the adjoint of a reflection read as a signed operator on a Lie algebra, the self-adjointness of the reflections and its failure in the degenerate case. It is the fourth article of the `- * Operator Theory` group of the category; the reflection and its involution condition are *Reflections as Signed Two-Sided Operators on a Lie Algebra*, the signed sandwich which realises it is *The Signed Sandwich on a Lie Algebra*, both above in the category, the adjoint of the sandwich is *The Signed Adjoint Sandwich on a Lie Algebra*, above, the invariant form is *Hermitian Forms on a Lie Algebra*, and the remaining adjoints are *The Signed Adjoint of the Left Multiplication on a Lie Algebra* and *The Graded Adjoint Action on a Module over a Lie Algebra*, below in this group.

The article assumes the reflection, the signed conjugation and the carrying elements from *Reflections as Signed Two-Sided Operators on a Lie Algebra*, the adjoint operation and the adjoints of the one-sided multiplications from *The Signed Adjoint Sandwich on a Lie Algebra*, the invariant Hermitian form and its positive definite case from *Hermitian Forms on a Lie Algebra*, the inner automorphisms and the exponential from *The Lie Correspondence and the Adjoint Representation*, and the grading and the grade involution from *Graded Lie Algebras with an Involution*. The form is used as an instrument; the geometric reflection in a hyperplane, which needs a metric, is Part IV.

## The Adjoint of a Reflection

### The Computation

**Definition.** Let $H$ be a non-degenerate invariant Hermitian form on the Lie algebra $\mathrm{G}$, preserved by the grade involution, and let $\rho_a = e^{\operatorname{ad}_a}\alpha$ be the signed conjugation. The **adjoint** is the operator $\rho_a^{*}$ with $H(\rho_ax,y) = H(x,\rho_a^{*}y)$.

**Theorem (the reflection is unitary).** The adjoint of the signed conjugation is its inverse,

$$
\rho_a^{*} = \alpha e^{-\operatorname{ad}_a} = \rho_a^{-1} ,
$$

so that $\rho_a^{*}\rho_a = \rho_a\rho_a^{*} = \mathrm{id}$: every reflection preserves the form $H$.

*Proof.* The adjoint of the composite is the composite of the adjoints in the reverse order, $\rho_a^{*} = \alpha^{*}\bigl(e^{\operatorname{ad}_a}\bigr)^{*}$; the isometry $\alpha$ has $\alpha^{*} = \alpha$, and the exponential of the skew-adjoint $\operatorname{ad}_a$ has adjoint the exponential of $-\operatorname{ad}_a$, $\bigl(e^{\operatorname{ad}_a}\bigr)^{*} = e^{-\operatorname{ad}_a}$; hence $\rho_a^{*} = \alpha e^{-\operatorname{ad}_a}$, which is the inverse of $e^{\operatorname{ad}_a}\alpha$ computed in *Reflections as Signed Two-Sided Operators on a Lie Algebra*.

**Corollary.** The reflection is a unitary operator of the form and its adjoint is another reflection, the signed conjugation by $-\alpha(a)$,

$$
\rho_a^{*} = \rho_{-\alpha(a)} ,
$$

since $\alpha e^{-\operatorname{ad}_a} = e^{-\operatorname{ad}_{\alpha(a)}}\alpha = e^{\operatorname{ad}_{-\alpha(a)}}\alpha$.

*Proof.* Move $\alpha$ past the exponential with $\alpha e^{-\operatorname{ad}_a} = e^{-\operatorname{ad}_{\alpha(a)}}\alpha$.

### Self-Adjointness

**Theorem (the self-adjoint reflections).** The reflection is self-adjoint if and only if it is an involution,

$$
\rho_a^{*} = \rho_a \iff \rho_a^{2} = \mathrm{id} \iff a + \alpha(a)\in Z(\mathrm{G}) ,
$$

and the self-adjoint reflections are exactly the involutive reflections; in particular the reflection by an **odd** element is self-adjoint.

*Proof.* The reflection is unitary, so $\rho_a^{*} = \rho_a^{-1}$; the identity $\rho_a^{-1} = \rho_a$ is the involution, whose criterion is the centrality of $a+\alpha(a)$ from *Reflections as Signed Two-Sided Operators on a Lie Algebra*. For an odd element $a + \alpha(a) = 0$, which is central.

**Corollary.** The reflection by an even element is self-adjoint exactly when $2a$ is central; the reflection by a mixed pair reduces to the even and the odd cases componentwise, and the reflection by the zero element is the grade involution $\alpha$, which is self-adjoint and an involution.

*Proof.* For an even element $\alpha(a) = a$ and the criterion is $2a$ central; the componentwise statement is the linearity of the map $a\mapsto a+\alpha(a)$; the zero case is immediate.

### The Fixed Subalgebra and the Form

**Theorem.** The fixed subalgebra of a self-adjoint reflection is the orthogonal complement of the image of the operator $\mathrm{id} - \rho_a$,

$$
\operatorname{Fix}(\rho_a) = \bigl(\operatorname{im}(\mathrm{id}-\rho_a)\bigr)^{\perp} ,
$$

and for an involutive reflection the algebra decomposes into the fixed subalgebra and its complement on which the reflection acts by $-\mathrm{id}$.

*Proof.* A self-adjoint operator has its fixed set equal to the orthogonal complement of the image of $\mathrm{id}-\rho_a$, because $H((\mathrm{id}-\rho_a)x, y) = H(x,(\mathrm{id}-\rho_a)y)$; for an involution the operator $\mathrm{id}-\rho_a$ is twice the projection onto the anti-fixed part.

## The Failure of Self-Adjointness

### The Even Carrying Element

**Proposition.** For an even carrying element $a$ with $2a$ not central the reflection is unitary but not self-adjoint; the defect

$$
\rho_a - \rho_a^{*} = \rho_a - \rho_a^{-1}
$$

does not vanish, and the reflection is a unitary operator whose inverse is a different reflection, $\rho_a^{*} = \rho_{-\alpha(a)} = \rho_{-a}$.

*Proof.* The self-adjointness criterion is not satisfied, and the adjoint is the reflection by the negative of the parameter; the two reflections differ exactly when the involution condition fails.

### The Inner Involution

**Proposition.** If the grade involution is inner, $\alpha = e^{\operatorname{ad}_w}$, then the reflection is the inner automorphism $e^{\operatorname{ad}_{a+w}}$, which is unitary; it is self-adjoint exactly when it is an involution, that is when $2(a+w)$ is central, and in the generic case it is unitary but not self-adjoint.

*Proof.* Substitute $\alpha = e^{\operatorname{ad}_w}$; the reflection is the inner automorphism of the sum, and the criterion is the centrality of the doubled generator.

### The Degenerate Form

**Proposition.** If the form $H$ is degenerate, the adjoint of a reflection need not exist, and if the grade involution is not an isometry of $H$ the adjoint of the reflection is not its inverse: in the first case the operator has no adjoint on the radical, and in the second the reflection fails to preserve the form, so it is not unitary; the reflection is unitary and self-adjoint exactly in the non-degenerate isometric case and under the involution condition.

*Proof.* The adjoint exists for every operator exactly when $H$ is non-degenerate; the unitarity of $\rho_a$ uses $\alpha^{*} = \alpha$, which is the isometry of the involution. The Heisenberg algebra with its degenerate form is the standard example, as in *The Signed Adjoint Sandwich on a Lie Algebra*.

### The Non-Unitary Reflection

**Proposition.** If the involution is not an isometry, the adjoint of the reflection is $\rho_a^{*} = \alpha^{*}e^{-\operatorname{ad}_a}$, which differs from $\rho_a^{-1}$ by the defect $\alpha^{*}\alpha^{-1}$, and the reflection is then only a similarity of the form with the defect of the involution; the reflection is unitary exactly when the involution is.

*Proof.* Compute the product $\rho_a^{*}\rho_a = \alpha^{*}e^{-\operatorname{ad}_a}e^{\operatorname{ad}_a}\alpha = \alpha^{*}\alpha$, which is the identity exactly when $\alpha$ is an isometry.

## Examples

### The Cartan Involution

For $a = 0$ the reflection is the grade involution $\rho_0 = \alpha$, which is an involution and an isometry, hence self-adjoint and unitary; this is the Cartan involution of *The Cartan Decomposition and the Cartan Involution* read as the simplest reflection, and its fixed subalgebra is the maximal compact subalgebra.

### The Odd Reflections

Let $\mathrm{G} = \mathrm{sl}_2(\mathbb{R})$ with the Cartan involution $\alpha$ as the grading and the invariant form of signature $(2,1)$; for an odd element $a$, that is a symmetric traceless matrix, the reflection $\rho_a = e^{\operatorname{ad}_a}\alpha$ is a self-adjoint unitary involution, its fixed subalgebra is one-dimensional, and the reflection is a hyperbolic involution of the algebra whose geometric reading is Part IV.

### The Even Reflection

Let $\mathrm{G} = \mathrm{gl}(n)$ with $\alpha = \mathrm{id}$ and $H(X,Y) = \operatorname{tr}(X\overline{Y})$; the reflection is the inner automorphism $e^{\operatorname{ad}_a}$, which is unitary for the form; it is self-adjoint exactly when $2a$ is central, so a reflection by a traceless diagonal element with distinct eigenvalues is unitary but not self-adjoint.

## Summary

With respect to a non-degenerate invariant Hermitian form preserved by the grade involution, the reflection $\rho_a = e^{\operatorname{ad}_a}\alpha$ has the adjoint $\rho_a^{*} = \alpha e^{-\operatorname{ad}_a} = \rho_a^{-1}$, so **every reflection is unitary** and its adjoint is the reflection by $-\alpha(a)$; the reflection is **self-adjoint exactly when it is an involution**, which is the centrality of $a+\alpha(a)$, and this holds automatically for every odd element, while for an even element it requires $2a$ central. The self-adjoint reflection has its fixed subalgebra equal to the orthogonal complement of the image of $\mathrm{id}-\rho_a$, and the algebra then splits into the fixed part and the anti-fixed part. The self-adjointness fails in the degenerate forms of the construction: for an even carrying element with $2a$ not central the reflection is unitary but not self-adjoint — the reflection by a generic inner automorphism — and for a degenerate form the adjoint need not exist, while for a non-isometric involution the reflection is not unitary at all, its defect being that of the involution. The Cartan involution is the reflection by the zero element, self-adjoint and unitary, and the reflections by the odd elements are the self-adjoint unitary involutions of the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H$ | the invariant Hermitian form, preserved by the involution |
| $\rho_a = e^{\operatorname{ad}_a}\alpha$ | the reflection, the signed conjugation |
| $\rho_a^{*} = \alpha e^{-\operatorname{ad}_a} = \rho_a^{-1}$ | the adjoint, the inverse |
| $\rho_a^{*} = \rho_{-\alpha(a)}$ | the adjoint as a reflection |
| $\rho_a^{*} = \rho_a \iff \rho_a^{2} = \mathrm{id}$ | the self-adjointness criterion |
| $a+\alpha(a)\in Z(\mathrm{G})$ | the involution condition |
| $\operatorname{Fix}(\rho_a) = (\operatorname{im}(\mathrm{id}-\rho_a))^{\perp}$ | the fixed subalgebra |
| $\rho_a^{*}\rho_a = \alpha^{*}\alpha$ | the defect of the non-isometric involution |
| degenerate $H$ | the failure of the existence of the adjoint |
| $\rho_0 = \alpha$ | the Cartan involution as a reflection |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for the Cartan involution, the invariant forms and their isometries.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, second edition, 2002), for the Cartan involutions, the symmetric pairs and the unitary operators of the form.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the involutions, their isometries and the adjoint of a signed operator.
- Ottmar Loos, *Symmetric Spaces*, Volume I (Benjamin, 1969), for the involutions of a Lie algebra, their fixed subalgebras and the symmetric decompositions.
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984), for the inner automorphisms, the invariant forms and the adjoints.
