
# __The Signed Adjoint of the Reflection on an Ordered Algebra__

## Introduction

The **reflection** of a graded algebra is the signed conjugation

$$
\tau_a(x) = a\,\alpha(x)\,a^{-1} = \Theta^{\alpha}_{a,a^{-1}}(x) ,
$$

the signed sandwich with the parameter $b = a^{-1}$; it is an involution exactly when $a$ is a **reflection element**, $\alpha(a) = a^{-1}$. The article computes its **adjoint** for the trace form by specialising the adjoint of the signed sandwich:

$$
(\tau_a)^{*} = \tau_{\alpha(a^{*})} ,
$$

so the adjoint of a reflection is again a reflection, with the parameter replaced by the $\alpha$-twist of the adjoint. The two special cases are the ones to remember: for the identity grade involution the adjoint of the ordinary conjugation by $a$ is the conjugation by $a^{*}$, and for a reflection element the adjoint is the reflection with the parameter $\alpha(a^{*})$, which is the twist of the adjoint that keeps the operator inside the reflection family. The article states the formula, identifies the **self-adjoint reflections** ($a = \alpha(a^{*})$ up to a central factor) and the **skew-adjoint** ones, and describes the interaction with the **order**: a reflection with a positive grade involution and positive invertible parameter is positive, hence so is its adjoint, and the order is an invariant of the adjoint involution.

The reflection is the operator of the family that has an algebraic meaning in the outer automorphism group: $\tau_a = \operatorname{Inn}_a\circ\alpha$ is the composite of the inner automorphism and the grade involution, two reflection elements give the same reflection exactly when their ratio is central, and the realised reflections are the composites of the grade involution with the inner automorphisms. The adjoint computation of the article is therefore not only an operator identity but a statement about the **outer class** of the reflection: the adjoint of $\operatorname{Inn}_a\circ\alpha$ is $\operatorname{Inn}_{\alpha(a^{*})}\circ\alpha$, an inner automorphism conjugated with the grade involution, and the adjoint preserves the outer class.

The reflections and the reflection elements are *Reflections as Signed Two-Sided Operators on an Ordered Algebra*; the signed sandwich and its adjoint are *The Signed Sandwich on an Ordered Algebra* and *The Signed Adjoint Sandwich on an Ordered Algebra*; the signed left multiplication is *The Signed Left Multiplication on an Ordered Algebra*; the graded action is *The Graded Action on a Module over an Ordered Algebra*; the adjoint and the positivity are *The Adjoint of a Positive Operator*; the order of the elements is *Self-Adjoint Elements and the Order*; the two-sided multiplications are *The Adjoint of the Left Multiplication on an Ordered Algebra*; the automorphisms are *The Involution on the Order Automorphisms*; the order is *Ordered Vector Spaces and the Order Unit* and *Positive Operators on an Ordered Space*; the grading is *Superalgebras and Graded Structures* of Part I; and the algebra is *Ordered Involutive Algebras*.

## The Adjoint of the Reflected Operator

**Definition.** The **reflected signed two-sided operator** (the reflection) is

$$
\tau_a : A\to A, \qquad \tau_a(x) = a\,\alpha(x)\,a^{-1} = \Theta^{\alpha}_{a,\,a^{-1}}(x) ;
$$

it is the signed conjugation by $a$, and it is an **involution** exactly when $a$ is a reflection element, $\alpha(a) = a^{-1}$.

**Theorem (the adjoint of the reflection).** For the trace form the adjoint of the reflection is the reflection with the $\alpha$-twisted adjoint parameter,

$$
(\tau_a)^{*} = \tau_{\alpha(a^{*})} ;
$$

in particular the adjoint of a reflection is again a reflection, the adjoint of $\tau_a$ is the ordinary conjugation by $a^{*}$ when the grade involution is the identity, and the family of the reflections is **closed under the adjoint**.

*Proof.* Apply the adjoint formula of the signed sandwich to $\Theta^{\alpha}_{a,a^{-1}}$:
$$
(\tau_a)^{*} = \Theta^{\alpha}_{\alpha(a^{*}),\,\alpha((a^{-1})^{*})} = \Theta^{\alpha}_{\alpha(a^{*}),\,\alpha(a^{*})^{-1}} = \tau_{\alpha(a^{*})} ,
$$
using $\alpha((a^{-1})^{*}) = \alpha(a^{-1})^{*} = \alpha(a^{*})^{-1}$ and the definition of the reflection. The identity grade involution gives $(\tau_a)^{*} = \tau_{a^{*}}$, the conjugation by the adjoint.

**Corollary (the adjoint of a reflection element).** If $a$ is a reflection element, $\alpha(a) = a^{-1}$, then

$$
(\tau_a)^{*} = \tau_{\alpha(a^{*})} = \tau_{a^{-*}} ,
$$

and the adjoint of the realised reflection $\tau_a = \operatorname{Inn}_a\circ\alpha$ is the realised reflection $\operatorname{Inn}_{\alpha(a^{*})}\circ\alpha$; the adjoint preserves the set of the realised reflections and acts on the reflection elements by $a\mapsto\alpha(a^{*})$.

*Proof.* The first statement is the theorem applied to the reflection element; for the realised-reflection statement, $\tau_{\alpha(a^{*})} = \operatorname{Inn}_{\alpha(a^{*})}\circ\alpha$ by the composite formula of *Reflections as Signed Two-Sided Operators on an Ordered Algebra*, and the map $a\mapsto\alpha(a^{*})$ on the reflection elements is well defined because $\alpha(\alpha(a^{*})) = a^{*} = \alpha(a)^{*} = (a^{-1})^{*} = \alpha(a^{*})^{-1}$, so $\alpha(a^{*})$ is again a reflection element.

**Corollary (the adjoint of the grade involution).** The grade involution is the reflection $\tau_1$; its adjoint is $(\tau_1)^{*} = \tau_{\alpha(1^{*})} = \tau_1$, so the grade involution is **self-adjoint** for the trace form. More generally the reflection $\tau_a$ is self-adjoint exactly when the reflection $\tau_a$ and $\tau_{\alpha(a^{*})}$ coincide, that is, when $a^{-1}\alpha(a^{*})$ is **central**.

*Proof.* The grade involution is $\tau_1$ and $\alpha(1) = 1$; the self-adjointness criterion is the theorem together with the fibre statement of the reflections, which says that two reflection parameters give the same reflection exactly when their ratio is central.

## Self-Adjointness and Skew-Adjointness

**Proposition (the self-adjoint reflections).** The reflection is **self-adjoint**,

$$
(\tau_a)^{*} = \tau_a ,
$$

when the parameter is **$\alpha$-Hermitian**, $a = \alpha(a^{*})$; conversely, the self-adjoint reflections are the reflections $\tau_a$ with $a^{-1}\alpha(a^{*})$ central, so the self-adjointness of the reflection depends on the parameter only through its class in the centre of the algebra.

*Proof.* If $a = \alpha(a^{*})$ then $\tau_{\alpha(a^{*})} = \tau_a$, so the adjoint is the reflection itself; conversely, if $(\tau_a)^{*} = \tau_a$ then $\tau_{\alpha(a^{*})} = \tau_a$, and the fibre statement gives the centrality of $a^{-1}\alpha(a^{*})$.

**Corollary (the skew-adjoint reflections).** The reflection is **skew-adjoint**, $(\tau_a)^{*} = -\tau_a$, exactly when $\tau_{\alpha(a^{*})} = -\tau_a$, which happens for the parameters with $\alpha(a^{*}) = -a$ up to the centre; in particular an **odd** reflection element with $a^{2} = -1$ in a graded algebra with a positive grade involution gives a reflection whose adjoint is the reflection with the parameter $-a^{*} = \alpha(a^{*})$, and the reflection is skew-adjoint exactly when $a$ is skew with respect to $\alpha$.

*Proof.* The skew-adjointness is the equation $\tau_{\alpha(a^{*})} = -\tau_a$; the odd reflection-element case uses $\alpha(a) = -a$ and $\alpha(a) = a^{-1}$, so $\alpha(a^{*}) = (a^{-1})^{*} = -a^{*}$ holds exactly when $a^{*} = -a$, the skewness. The centrality ambiguity is the fibre as before.

**Proposition (the decomposition and the square).** Every reflection decomposes into the self-adjoint and the skew-adjoint parts with respect to the adjoint,

$$
\tau_a = \tfrac12\bigl(\tau_a + \tau_{\alpha(a^{*})}\bigr) + \tfrac12\bigl(\tau_a - \tau_{\alpha(a^{*})}\bigr) ,
$$

and when $a$ is a reflection element the square is the identity, $\tau_a^{2} = \mathrm{id}$, so the adjoint of the square is the identity and the reflection is an isometry of the quadratic order exactly when it is self-adjoint.

*Proof.* The decomposition is the standard one; the square statement is the reflection theorem of *The Signed Sandwich on an Ordered Algebra*; the isometry statement follows because a reflection preserves the quadratic order exactly when it is an order automorphism commuting with the adjoint, which for an involution is the self-adjointness.

## The Adjoint and the Order

**Theorem (the positivity of the reflection and of its adjoint).** If the grade involution is **positive** and the parameter $a$ is positive and invertible, then the reflection $\tau_a$ is **positive** and its adjoint $\tau_{\alpha(a^{*})}$ is positive:

$$
\alpha\geq0, \quad a\geq0\ \text{invertible} \implies \tau_a\geq0 \ \text{ and } \ (\tau_a)^{*}\geq0 .
$$

If the grade involution is not positive then the reflection of positive parameters need not be positive, and the obstruction is the sign of $\alpha$ on the odd part of the cone.

*Proof.* The reflection is the signed sandwich $\Theta^{\alpha}_{a,a^{-1}}$; with $\alpha$ positive and $a\geq0$ invertible, so that $a^{-1}\geq0$, the positivity criterion of the signed sandwich gives $\tau_a\geq0$; the positivity of the adjoint is the general positivity preservation of the adjoint of *The Adjoint of a Positive Operator*. The failure in the non-positive case is the positivity proposition of the signed sandwich.

**Corollary (the order and the outer class).** The reflections that are positive form a subset of the realised reflections closed under the adjoint; the order-reversing reflections are the ones whose adjoint is their negative up to the centre; and the adjoint action on the realised reflections preserves both the positive and the order-reversing classes, because it preserves the positivity of the operators. This is the order-theoretic statement of the outer-class computation: the adjoint is an order automorphism of the reflection family whose action on the outer classes is the $\alpha$-twist of the parameter.

*Proof.* The closure of the positive reflections under the adjoint is the theorem; the order-reversing case is the sign condition; the outer-class statement is the corollary on the adjoint of the realised reflection.

## Worked Cases

### The Matrix Algebra

Let $A = M_n(\mathbb{R})$ with the identity grade involution. The reflection elements are the involutions $a^{2} = 1$, the reflected operator is the conjugation $\tau_a(x) = axa^{-1}$, and its adjoint is the conjugation by $a^{*} = a^{\mathsf{T}}$; the reflections are self-adjoint exactly for the symmetric involutions $a = a^{\mathsf{T}}$, and the fibre over the trivial reflection is the set of the central involutions $\{\pm I\}$. The adjoint therefore acts on the reflection parameters by the transpose, which is the identity on the symmetric involutions.

### The Biquaternion Algebra

Let $A = \mathbb{B} = M_2(\mathbb{C})$ with the $\operatorname{diag}(1,-1)$ grading and its inner grade involution. An odd element with $a^{2} = -1$ realises the signed conjugation, and the adjoint of $\tau_a$ is the reflection with parameter $\alpha(a^{*}) = -a^{*}$, which is again an odd reflection element; the ordinary conjugation by $a$ and its negative coincide with the sign of the parity, and the adjoint is the reflection realised by the adjoint of the parameter, so the adjoint is the $\alpha$-twist of the parameter involution. The example exhibits the adjoint formula in the smallest inner-graded case.

### The Clifford Algebra

Let $A = \mathrm{Cl}(V,q)$ with the parity grading and its positive grade involution. A vector $e$ with $e^{2} = -1$ is an odd reflection element and $\tau_e$ is a reflection of the algebra restricting to a reflection of $V$; the adjoint of $\tau_e$ is $\tau_{\alpha(e^{*})} = \tau_{-e^{*}}$, the reflection realised by the twist of the adjoint vector, and the pair $e$, $-e$ realises the same reflection modulo the sign. The Clifford case is the geometric instance in which the adjoint of the reflection is the reflection of the adjoint.

## Summary

The **reflection** $\tau_a(x) = a\alpha(x)a^{-1} = \Theta^{\alpha}_{a,a^{-1}}(x)$ of a graded ordered involutive algebra has, for the trace form, the adjoint

$$
(\tau_a)^{*} = \tau_{\alpha(a^{*})} ,
$$

so the adjoint of a reflection is again a reflection, the adjoint of the ordinary conjugation by $a$ is the conjugation by $a^{*}$ (the identity grade involution), and the family of the reflections is **closed under the adjoint**. The reflection is **self-adjoint** exactly when the parameter is $\alpha$-Hermitian, $a = \alpha(a^{*})$, up to a **central** factor, and **skew-adjoint** for the skew parameters; it decomposes into the self-adjoint and the skew-adjoint parts, and an involutive reflection is an isometry of the quadratic order exactly when it is self-adjoint. The adjoint acts on the realised reflections by the $\alpha$-twist of the parameter, $\operatorname{Inn}_a\circ\alpha\mapsto\operatorname{Inn}_{\alpha(a^{*})}\circ\alpha$, preserving the outer class, and it preserves the **positivity**: a reflection with a positive grade involution and a positive invertible parameter is positive, hence so is its adjoint. The reflections are *Reflections as Signed Two-Sided Operators on an Ordered Algebra*; the sandwich and its adjoint are *The Signed Sandwich on an Ordered Algebra* and *The Signed Adjoint Sandwich on an Ordered Algebra*; the adjoint is *The Adjoint of a Positive Operator*; the order is *Self-Adjoint Elements and the Order* and *Ordered Vector Spaces and the Order Unit*; the two-sided multiplications are *The Adjoint of the Left Multiplication on an Ordered Algebra*; the automorphisms are *The Involution on the Order Automorphisms*; and the grading is *Superalgebras and Graded Structures*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tau_a(x) = a\alpha(x)a^{-1}$ | Reflection (signed conjugation) |
| $\alpha(a) = a^{-1}$ | Reflection element |
| $(\tau_a)^{*} = \tau_{\alpha(a^{*})}$ | Adjoint of a reflection |
| $(\tau_a)^{*} = \tau_{a^{*}}$ | The identity grade involution |
| $a = \alpha(a^{*})$ | $\alpha$-Hermitian parameter, the self-adjoint case |
| $a^{-1}\alpha(a^{*})$ central | The self-adjointness up to the fibre |
| $\tau_a = \operatorname{Inn}_a\circ\alpha$ | Outer-class form of the reflection |
| $\tau_1 = \alpha$ | The grade involution, self-adjoint |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the reflections realised by the conjugation, their adjoints and the parity grading.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the graded reflections and the reflection elements of a Clifford algebra.
- Richard Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the adjoints, the involutions and the order.
- Gert K. Pedersen, *C\*-Algebras and their Automorphism Groups* (Academic Press, 1979), for the inner automorphisms, the order-two automorphisms and the positivity.
- Max Koecher, *The Minnesota Notes on Jordan Algebras and their Applications* (Springer, 1999), for the reflections and the sandwich operators of the Jordan structures.
