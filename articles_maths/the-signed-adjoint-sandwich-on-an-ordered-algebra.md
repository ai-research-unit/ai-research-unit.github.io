
# __The Signed Adjoint Sandwich on an Ordered Algebra__

## Introduction

The **signed sandwich** of a graded algebra with grade involution $\alpha$ is the two-sided operator

$$
\Theta^{\alpha}_{a,b}(x) = a\,\alpha(x)\,b ,
$$

the unsigned sandwich $\Theta_{a,b}(x) = axb$ with the argument twisted by the grade involution. Its **adjoint** for the trace form is again a signed sandwich,

$$
\bigl(\Theta^{\alpha}_{a,b}\bigr)^{*} = \Theta^{\alpha}_{\alpha(a^{*}),\,\alpha(b^{*})} ,
$$

so the signed sandwich is **adjoint closed** on the family of the signed sandwiches, with the parameters replaced by their $\alpha$-twisted adjoints; the unsigned case is $\alpha = 1$ and gives $(\Theta_{a,b})^{*} = \Theta_{a^{*},b^{*}}$. The article proves this computation, reads off the self-adjointness ($\Theta^{\alpha}_{a,b}$ is self-adjoint exactly when the parameters are **$\alpha$-Hermitian**, $a = \alpha(a^{*})$, $b = \alpha(b^{*})$, up to a central factor), and describes the interaction with the **order**: the adjoint of a positive signed sandwich is positive, so the adjoint is an order isomorphism of the family, and the positivity criterion of the signed sandwich (the grade involution positive, the parameters positive) is transported by the adjoint.

The signed sandwich is the parent of the two-sided family of the category: the **reflection** $\tau_a = \Theta^{\alpha}_{a,a^{-1}}$ and the unsigned sandwich are its specialisations, and the signed one-sided multiplications are its factors, $\Theta^{\alpha}_{a,b} = L^{\alpha}_aR_{\alpha(b)}$. The adjoint computation of the article is therefore the computation from which the adjoints of the reflections and of the one-sided multiplications follow, and the fact that the adjoint **stays in the family** is what makes the adjoint involution a symmetry of the signed structure rather than an accident of the trace form.

The signed sandwich, its composition law and the reflection elements are *The Signed Sandwich on an Ordered Algebra*; the reflections are *Reflections as Signed Two-Sided Operators on an Ordered Algebra*; the signed one-sided multiplications are *The Signed Left Multiplication on an Ordered Algebra*; the graded action is *The Graded Action on a Module over an Ordered Algebra*; the order and the operator order are *Ordered Vector Spaces and the Order Unit* and *Positive Operators on an Ordered Space*; the adjoint and the positivity are *The Adjoint of a Positive Operator*; the order of the elements is *Self-Adjoint Elements and the Order*; the two-sided multiplications are *The Adjoint of the Left Multiplication on an Ordered Algebra*; the involutions and the automorphisms are *The Involution on the Order Automorphisms*; the grading is *Superalgebras and Graded Structures* of Part I; and the algebra is *Ordered Involutive Algebras*.

## The Adjoint of the Signed Sandwich

**Definition.** Let $A$ be an ordered involutive algebra with an involution $x\mapsto x^{*}$, a **grade involution** $\alpha$ (an algebra automorphism of order two commuting with the involution, $\alpha(x^{*}) = \alpha(x)^{*}$) and a faithful **invariant trace**, with the trace form $\langle x,y\rangle = \operatorname{tr}(x^{*}y)$. The **signed sandwich** of the parameters $a,b$ is

$$
\Theta^{\alpha}_{a,b} : A\to A, \qquad \Theta^{\alpha}_{a,b}(x) = a\,\alpha(x)\,b .
$$

**Theorem (the adjoint stays in the family).** The adjoint of a signed sandwich for the trace form is the signed sandwich

$$
\bigl(\Theta^{\alpha}_{a,b}\bigr)^{*} = \Theta^{\alpha}_{\alpha(a^{*}),\,\alpha(b^{*})} ,
$$

with the parameters replaced by the $\alpha$-twists of their adjoints; in particular the adjoint of a signed sandwich is a signed sandwich, and the family $\{\Theta^{\alpha}_{a,b}\}$ is **closed under the adjoint**.

*Proof.* Compute
$$
\langle \Theta^{\alpha}_{a,b}x,\,y\rangle = \operatorname{tr}\bigl((a\alpha(x)b)^{*}y\bigr) = \operatorname{tr}\bigl(b^{*}\alpha(x)^{*}a^{*}y\bigr) = \operatorname{tr}\bigl(b^{*}\alpha(x^{*})a^{*}y\bigr) ,
$$
using the commutation of $\alpha$ with the involution. By the cyclicity of the trace and the invariance $\operatorname{tr}(\alpha(u)v) = \operatorname{tr}(u\alpha^{-1}(v))$ of the trace under the automorphism $\alpha$,
$$
\operatorname{tr}\bigl(b^{*}\alpha(x^{*})a^{*}y\bigr) = \operatorname{tr}\bigl(\alpha(x^{*})a^{*}yb^{*}\bigr) = \operatorname{tr}\bigl(x^{*}\alpha^{-1}(a^{*}yb^{*})\bigr) = \operatorname{tr}\bigl(x^{*}\alpha(a^{*})\alpha(y)\alpha(b^{*})\bigr) ,
$$
and this is $\langle x,\Theta^{\alpha}_{\alpha(a^{*}),\alpha(b^{*})}y\rangle$ because $\alpha^{-1} = \alpha$ and $\alpha$ is an algebra homomorphism. Hence the adjoint is as displayed.

**Corollary (the unsigned case and the composition).** For the identity grade involution, $(\Theta_{a,b})^{*} = \Theta_{a^{*},b^{*}}$, which is the adjoint of the two-sided multiplication of *The Adjoint of the Left Multiplication on an Ordered Algebra*; in general the adjoint is an **anti-homomorphism** on the family of the signed sandwiches,

$$
\bigl(\Theta^{\alpha}_{a,b}\Theta^{\alpha}_{c,d}\bigr)^{*} = \bigl(\Theta^{\alpha}_{c,d}\bigr)^{*}\bigl(\Theta^{\alpha}_{a,b}\bigr)^{*} ,
$$

as for every family of operators, and the composition law of the signed sandwich makes the adjoint of a product again a signed sandwich with the twisted parameters in the reverse order.

*Proof.* The unsigned case is the formula with $\alpha = 1$; the anti-homomorphism property is general for operators with adjoints; the last statement combines the two.

## Self-Adjointness and Skew-Adjointness

**Proposition ($\alpha$-Hermitian parameters).** The signed sandwich is **self-adjoint**,

$$
\bigl(\Theta^{\alpha}_{a,b}\bigr)^{*} = \Theta^{\alpha}_{a,b} ,
$$

when the parameters are **$\alpha$-Hermitian**, $a = \alpha(a^{*})$ and $b = \alpha(b^{*})$; conversely, $\Theta^{\alpha}_{a,b}$ is self-adjoint if and only if $a = \alpha(a^{*})c$ and $b = \alpha(b^{*})c^{-1}$ for a **central** element $c$, so the ambiguity of the self-adjointness is the same as the ambiguity of the fibre of the signed sandwich, the centre of the algebra.

*Proof.* If the parameters are $\alpha$-Hermitian then $\alpha(a^{*}) = a$ and $\alpha(b^{*}) = b$, so the theorem gives $(\Theta^{\alpha}_{a,b})^{*} = \Theta^{\alpha}_{a,b}$; conversely, if the adjoints agree then $\Theta^{\alpha}_{\alpha(a^{*}),\alpha(b^{*})} = \Theta^{\alpha}_{a,b}$, and the equality of the signed sandwiches with the $a$-parameters differing by a central factor is the fibre statement of *The Signed Sandwich on an Ordered Algebra*.

**Corollary (the decomposition into self-adjoint and skew parts).** Every signed sandwich decomposes as the sum of an **$\alpha$-Hermitian** part and a **skew-$\alpha$-Hermitian** part in each parameter,

$$
\Theta^{\alpha}_{a,b} = \tfrac12\bigl(\Theta^{\alpha}_{a,b} + (\Theta^{\alpha}_{a,b})^{*}\bigr) + \tfrac12\bigl(\Theta^{\alpha}_{a,b} - (\Theta^{\alpha}_{a,b})^{*}\bigr) ,
$$

the two summands being self-adjoint and skew-adjoint respectively; the operator is **normal** exactly when the two summands commute.

*Proof.* The decomposition is the standard one into the self-adjoint part $\frac12(T + T^{*})$ and the skew part $\frac12(T - T^{*})$; the normality criterion is the standard one, $TT^{*} = T^{*}T$.

## The Adjoint and the Order

**Theorem (the adjoint preserves the positivity of the signed sandwich).** The adjoint is an **order isomorphism** of the family of the signed sandwiches for the quadratic order: if the signed sandwich $\Theta^{\alpha}_{a,b}$ is positive, then its adjoint is positive,

$$
\Theta^{\alpha}_{a,b}\geq0 \implies \bigl(\Theta^{\alpha}_{a,b}\bigr)^{*}\geq0 ,
$$

and therefore if the grade involution is positive and the parameters $a,b$ are positive then the adjoint $\Theta^{\alpha}_{\alpha(a^{*}),\alpha(b^{*})}$ is positive.

*Proof.* The first statement is the general positivity of the adjoint of *The Adjoint of a Positive Operator*; the second combines the positivity criterion of the signed sandwich (the grade involution positive and $a,b\geq0$ give $\Theta^{\alpha}_{a,b}\geq0$) with the first statement.

**Corollary (the order of the family is adjoint invariant).** The positive cone of the family of the signed sandwiches generated by the $\Theta^{\alpha}_{a,b}$ with $a,b\geq0$ and $\alpha$ positive is invariant under the adjoint; the order interval at the identity, when the family contains it, is the set of the $\Theta^{\alpha}_{a,b}$ with $\Theta^{\alpha}_{a,b}\leq I$; and the adjoint preserves the order, so the adjoint is an order automorphism of the family. This is the signed counterpart of the order automorphism statement of *The Adjoint of the Left Multiplication on an Ordered Algebra*.

*Proof.* The invariance of the cone is the theorem; the interval and the order-automorphism statements are the definition of the order and the two-sided preservation.

**Proposition (the adjoint and the reflection elements).** If $a$ is a reflection element, $\alpha(a) = a^{-1}$, then the adjoint of the reflection $\tau_a = \Theta^{\alpha}_{a,a^{-1}}$ is the signed sandwich $\Theta^{\alpha}_{\alpha(a^{*}),\,\alpha((a^{-1})^{*})} = \Theta^{\alpha}_{\alpha(a^{*}),\,\alpha(a^{*})^{-1}}$, which is the reflection $\tau_{\alpha(a^{*})}$; the adjoint therefore carries a realised reflection to a realised reflection with the parameter $\alpha(a^{*})$, and the adjoint of the reflection is computed in *The Signed Adjoint of the Reflection on an Ordered Algebra* below.

*Proof.* The formula is the theorem applied to $b = a^{-1}$; the reflection-element statement uses $\alpha(a^{-*}) = \alpha(a^{*})^{-1}$, so the parameters of the adjoint are $\alpha(a^{*})$ and its inverse, which is the reflection-element condition for $\alpha(a^{*})$.

## Worked Cases

### The Matrix Algebra

Let $A = M_n(\mathbb{C})$ with the trace form and let $\alpha$ be the conjugation by $\operatorname{diag}(1,\dots,1,-1,\dots,-1)$, the parity grading. The signed sandwich $\Theta^{\alpha}_{a,b}$ is the operator $X\mapsto a\alpha(X)b$, and the adjoint is $X\mapsto \alpha(a^{*})\alpha(X)\alpha(b^{*})$; the two differ by the twist of the parameters, and they coincide exactly when the parameters are $\alpha$-Hermitian. The positive signed sandwiches are those with $\alpha$ positive and $a,b$ positive, and their adjoints are positive. This is the finite-dimensional model.

### The Biquaternion Algebra

Let $A = \mathbb{B} = M_2(\mathbb{C})$ with the $\operatorname{diag}(1,-1)$ grading. The signed sandwich is an unsigned sandwich with shifted parameters because the grade involution is inner, $\alpha(X) = UXU^{-1}$; the adjoint formula becomes the adjoint of the unsigned sandwich at the shifted parameters, and the self-adjointness criterion is the $\alpha$-Hermiticity of the parameters. The example shows that the adjoint formula is stable under the inner shift.

### The Clifford Algebra

Let $A = \mathrm{Cl}(V,q)$ with the parity grading and let $e$ be a vector with $e^{2} = -1$, an odd reflection element. The signed sandwich $\Theta^{\alpha}_{e,e^{-1}} = \tau_e$ is a reflection, and its adjoint $\tau_{\alpha(e^{*})}$ is again a reflection; the parameters of the adjoint are the $\alpha$-twists of the adjoint of $e$, and the whole computation reduces to the parity of $e$. The Clifford case is the geometric instance of the adjoint formula.

## Summary

The **signed sandwich** $\Theta^{\alpha}_{a,b}(x) = a\alpha(x)b$ of a graded ordered involutive algebra has, for the trace form, the adjoint

$$
\bigl(\Theta^{\alpha}_{a,b}\bigr)^{*} = \Theta^{\alpha}_{\alpha(a^{*}),\,\alpha(b^{*})} ,
$$

so the family of the signed sandwiches is **closed under the adjoint**, the adjoint is an anti-homomorphism on the family, and the unsigned case is $(\Theta_{a,b})^{*} = \Theta_{a^{*},b^{*}}$. The signed sandwich is **self-adjoint** exactly when the parameters are **$\alpha$-Hermitian**, $a = \alpha(a^{*})$, $b = \alpha(b^{*})$, up to a central factor; every signed sandwich decomposes into the self-adjoint and the skew-adjoint parts, and it is normal exactly when the parts commute. The adjoint **preserves the positivity** and is an **order isomorphism** of the family, so a signed sandwich with a positive grade involution and positive parameters has a positive adjoint; the adjoint of the reflection $\tau_a = \Theta^{\alpha}_{a,a^{-1}}$ is the reflection $\tau_{\alpha(a^{*})}$, computed in the next article. The signed sandwich is *The Signed Sandwich on an Ordered Algebra*; the reflections are *Reflections as Signed Two-Sided Operators on an Ordered Algebra*; the signed one-sided multiplications are *The Signed Left Multiplication on an Ordered Algebra*; the graded action is *The Graded Action on a Module over an Ordered Algebra*; the order is *Ordered Vector Spaces and the Order Unit* and *Positive Operators on an Ordered Space*; the adjoint is *The Adjoint of a Positive Operator*; the two-sided multiplications are *The Adjoint of the Left Multiplication on an Ordered Algebra*; and the automorphisms are *The Involution on the Order Automorphisms*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Theta^{\alpha}_{a,b}(x) = a\alpha(x)b$ | Signed sandwich |
| $(\Theta^{\alpha}_{a,b})^{*} = \Theta^{\alpha}_{\alpha(a^{*}),\alpha(b^{*})}$ | The adjoint stays in the family |
| $(\Theta_{a,b})^{*} = \Theta_{a^{*},b^{*}}$ | The unsigned case |
| $a = \alpha(a^{*})$ | $\alpha$-Hermitian parameter |
| $\Theta^{\alpha}_{a,b}\geq0\implies(\Theta^{\alpha}_{a,b})^{*}\geq0$ | The adjoint preserves the positivity |
| $\tau_a = \Theta^{\alpha}_{a,a^{-1}}$ | Reflection, a special signed sandwich |
| $(\tau_a)^{*} = \tau_{\alpha(a^{*})}$ | The adjoint of a reflection |

## Further Reading

- Richard Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the adjoints, the positivity and the trace forms.
- Gert K. Pedersen, *C\*-Algebras and their Automorphism Groups* (Academic Press, 1979), for the automorphisms, the graded structures and the order.
- Erik M. Alfsen and Frederik W. Shultz, *State Spaces of Operator Algebras* (Birkhäuser, 2001), for the sandwich operators, the order and the positivity.
- Max Koecher, *The Minnesota Notes on Jordan Algebras and their Applications* (Springer, 1999), for the sandwich operators of the Jordan structures and their adjoints.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the graded sandwiches and the reflections of the Clifford algebras.
