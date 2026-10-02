
# __The Signed Adjoint of the Left Multiplication on a Lie Algebra__

## Introduction

The **signed left multiplication** on a Lie algebra is $\ell^{\alpha}_a = \operatorname{ad}_a\circ\alpha$, the operator $x\mapsto[a,\alpha(x)]$, and its adjoint with respect to the invariant Hermitian form is the signed left multiplication by the image of the parameter under the involution with a change of sign. The result separates the even and the odd parameters exactly: for an **odd** parameter the signed left multiplication is **self-adjoint**, and for an **even** parameter it is **skew-adjoint**, the sign being the parity of the parameter. The article computes the adjoint, records this parity dichotomy, relates the operator to the signed sandwich of the two-sided theory, and gives the degenerate cases.

This article treats the adjoint of the signed left multiplication on a Lie algebra, its explicit expression and its relation to the signed sandwich. It is the fifth article of the `- * Operator Theory` group of the category; the signed left multiplication and its kernel are *The Signed Left Multiplication on a Lie Algebra*, the signed sandwich is *The Signed Sandwich on a Lie Algebra*, both above in the category, the adjoint of the sandwich is *The Signed Adjoint Sandwich on a Lie Algebra*, above, the invariant form is *Hermitian Forms on a Lie Algebra*, and the module case is *The Graded Adjoint Action on a Module over a Lie Algebra*, below.

The article assumes the signed left multiplication, its factorisation and its kernel from *The Signed Left Multiplication on a Lie Algebra*, the adjoint operation, the skew-adjoint multiplications and the explicit adjoint of the sandwich from *The Signed Adjoint Sandwich on a Lie Algebra*, the invariant Hermitian form and its positive definite case from *Hermitian Forms on a Lie Algebra*, the grading and the grade involution from *Graded Lie Algebras with an Involution*, and the centraliser from *Lie Algebras*. The form is an instrument; the geometry of the form is Part IV.

## The Adjoint

### The Computation

**Definition.** Let $H$ be a non-degenerate invariant Hermitian form on $\mathrm{G}$, preserved by the grade involution, and let $\ell^{\alpha}_a = L_a\alpha$ be the signed left multiplication. The **adjoint** is the operator $(\ell^{\alpha}_a)^{*}$ with $H(\ell^{\alpha}_ax,y) = H(x,(\ell^{\alpha}_a)^{*}y)$.

**Theorem (the explicit adjoint).** The adjoint of the signed left multiplication is the signed left multiplication by the negative of the image of the parameter,

$$
\bigl(\ell^{\alpha}_a\bigr)^{*} = \alpha^{*}L_a^{*} = -\alpha L_a = -L_{\alpha(a)}\alpha = \ell^{\alpha}_{-\alpha(a)} = -\ell^{\alpha}_{\alpha(a)} .
$$

*Proof.* The adjoint reverses the order, so $(\ell^{\alpha}_a)^{*} = \alpha^{*}L_a^{*}$; the involution is a self-adjoint isometry, $\alpha^{*} = \alpha$, and the left multiplication is skew-adjoint, $L_a^{*} = -L_a$, as in *The Signed Adjoint Sandwich on a Lie Algebra*; hence the adjoint is $-\alpha L_a$, and the naturality $\alpha L_a = L_{\alpha(a)}\alpha$ together with the linearity in the parameter gives the forms displayed.

### The Parity Dichotomy

**Theorem (self-adjoint and skew-adjoint).** The signed left multiplication is self-adjoint exactly for the odd parameters and skew-adjoint exactly for the even parameters:

$$
\bigl(\ell^{\alpha}_a\bigr)^{*} = \ell^{\alpha}_a \iff \alpha(a) = -a \iff a\in\mathrm{G}^{-} ,
$$
$$
\bigl(\ell^{\alpha}_a\bigr)^{*} = -\ell^{\alpha}_a \iff \alpha(a) = a \iff a\in\mathrm{G}^{+} .
$$

*Proof.* The adjoint is $\ell^{\alpha}_{-\alpha(a)}$; it equals $\ell^{\alpha}_a$ exactly when $-\alpha(a) = a$, and it equals $-\ell^{\alpha}_a = \ell^{\alpha}_{-a}$ exactly when $-\alpha(a) = -a$; the two conditions are the definitions of the odd and the even parts.

**Corollary.** The ordinary left multiplication is skew-adjoint, $L_a^{*} = -L_a$, and it is the case of the even parameter with the trivial grading; the signed left multiplication by an odd parameter is the self-adjoint modification of the ordinary one, and the modification consists of the single change of sign on the odd part of the argument.

*Proof.* The first statement is the skew-adjointness of the multiplication; the identification with the case of the trivial grading is immediate, and the last statement is the formula $\ell^{\alpha}_a = L_a(\mathrm{id}-2\pi^{-})$ of *The Signed Left Multiplication on a Lie Algebra*.

### Unitarity

**Theorem.** The signed left multiplication is unitary for $H$ exactly when the ordinary left multiplication is a complex structure,

$$
\bigl(\ell^{\alpha}_a\bigr)^{*}\ell^{\alpha}_a = \mathrm{id} \iff L_a^{2} = -\mathrm{id} \ \text{and}\ L_{\alpha(a)}^{2} = -\mathrm{id} ,
$$

and in that case the operator is a unitary complex structure on the algebra.

*Proof.* Compute $(\ell^{\alpha}_a)^{*}\ell^{\alpha}_a = \ell^{\alpha}_{-\alpha(a)}\ell^{\alpha}_a = -\ell^{\alpha}_{\alpha(a)}\ell^{\alpha}_a$; using the square of *The Signed Sandwich on a Lie Algebra*, $-\ell^{\alpha}_{\alpha(a)}\ell^{\alpha}_a = -L_{\alpha(a)}L_{\alpha(a)} = -L_{\alpha(a)}^{2}$; the product is the identity exactly when $L_{\alpha(a)}^{2} = -\mathrm{id}$, and the analogous computation for the reversed product gives $L_a^{2} = -\mathrm{id}$.

## Relation to the Signed Sandwich

**Theorem.** The signed sandwich is the signed left multiplication followed by a signed right multiplication, $\Sigma^{\alpha}_{a,b} = \ell^{\alpha}_aR_{\alpha(b)}$, and its adjoint is the product of the adjoints of the two factors in the reverse order,

$$
\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{*} = \bigl(R_{\alpha(b)}\bigr)^{*}\bigl(\ell^{\alpha}_a\bigr)^{*} = R_{\alpha(b)}\,\ell^{\alpha}_{\alpha(a)} ,
$$

which agrees with the explicit form $\alpha R_bL_a$ of *The Signed Adjoint Sandwich on a Lie Algebra*, since $\alpha R_bL_a = R_{\alpha(b)}\alpha L_a = R_{\alpha(b)}L_{\alpha(a)}\alpha$.

*Proof.* The factorisation is that of *The Signed Left Multiplication on a Lie Algebra*; the adjoint of a product is the product of the adjoints in the reverse order; the signs of the two skew-adjoint factors cancel, and the identification with the explicit form is the naturality of the involution.

**Corollary.** The adjoint of the signed sandwich is the signed left multiplication by $\alpha(a)$ followed by the ordinary right multiplication by $\alpha(b)$, and it is self-adjoint exactly when the carrying pair commutes; the one-sided adjoint is therefore the building block of the two-sided adjoint, in parallel with the Jordan case of *The Signed Adjoint of the Left Multiplication on a Jordan Algebra*.

*Proof.* Read the formula $R_{\alpha(b)}\ell^{\alpha}_{\alpha(a)}$ and apply the self-adjointness criterion of *The Signed Adjoint Sandwich on a Lie Algebra*.

## The Form and the Degenerate Cases

### The Form Defined by the Operator

**Theorem.** The sesquilinear defect

$$
H_{\ell}(x,y) = H\bigl(\ell^{\alpha}_ax,y\bigr) - H\bigl(x,\ell^{\alpha}_ay\bigr)
$$

vanishes identically exactly for the odd parameter; the signed left multiplication is therefore an infinitesimal symmetry of the form for every odd element, and it is an infinitesimal anti-symmetry for every even element.

*Proof.* The defect vanishes exactly when the operator is self-adjoint, which is the odd case by the parity dichotomy.

### The Identity Involution

**Proposition.** If $\alpha = \mathrm{id}$ the signed left multiplication is the ordinary one and it is skew-adjoint for every parameter; there is no self-adjoint case, the defect form is $2H(L_ax,y)$, and the operator is unitary exactly when $L_a^2 = -\mathrm{id}$.

*Proof.* Substitute $\alpha = \mathrm{id}$ in the adjoint formula and in the computations.

### The Inner Involution

**Proposition.** If the involution is inner, $\alpha = e^{\operatorname{ad}_w}$, then the adjoint is $(\ell^{\alpha}_a)^{*} = -\ell^{\alpha}_{\alpha(a)}$ with the parameter transformed by the inner involution, and the parity dichotomy holds with respect to the eigenspaces of the inner involution rather than with respect to the grading.

*Proof.* The adjoint formula does not use the special form of $\alpha$ beyond its being an isometric involution; the eigenspaces of an inner involution replace the graded parts.

### The Degenerate Form

**Proposition.** If $H$ is degenerate, the adjoint of the signed left multiplication is defined only on a subspace and the operator need not have an adjoint; if the involution is not an isometry the adjoint is $-\alpha L_a$ with a defect $2(\mathrm{id}-\alpha^{*}\alpha)$, and the parity dichotomy holds only for the isometric involution.

*Proof.* The existence of the adjoint is the non-degeneracy, and the unitarity uses $\alpha^{*} = \alpha$; the defect is computed from $\alpha^{*}\alpha$.

## Examples

### The Compact Algebra

Let $\mathrm{G} = \mathrm{so}(3)$ with the positive definite invariant form $H(X,Y) = -\frac12\operatorname{tr}(XY)$; the grade involution is the identity, and every left multiplication is skew-adjoint and unitary only on a complex structure, which the compact algebra of odd dimension does not contain. The example shows the even case in its pure form.

### The Rank-One Algebra

Let $\mathrm{G} = \mathrm{sl}_2(\mathbb{R})$ with the Cartan involution as the grading and the invariant form of signature $(2,1)$. For an odd element $a$ the signed left multiplication $\ell^{\alpha}_a$ is self-adjoint, its kernel is the centraliser of $\alpha(a)$, and the defect form vanishes; for an even element it is skew-adjoint, which is the compact direction of the Cartan decomposition.

### The Heisenberg Algebra

Let $\mathrm{G}$ be the Heisenberg algebra with the grading with $Z$ even and $X,Y$ odd, and with the degenerate invariant form vanishing on the radical. The adjoint of the signed left multiplication is not defined on the whole algebra, the parity dichotomy holds on the quotient by the radical, and the central element acts by the zero operator, so the self-adjointness on the radical is vacuous.

## Summary

The adjoint of the signed left multiplication $\ell^{\alpha}_a = \operatorname{ad}_a\alpha$ with respect to a non-degenerate invariant Hermitian form preserved by the involution is

$$
\bigl(\ell^{\alpha}_a\bigr)^{*} = -\alpha L_a = \ell^{\alpha}_{-\alpha(a)} ,
$$

the signed left multiplication by the negative of the image of the parameter; it is **self-adjoint exactly for the odd parameters** and **skew-adjoint exactly for the even parameters**, so the parity dichotomy of the grading is the dichotomy of the self-adjointness. The signed left multiplication is unitary exactly when the ordinary left multiplication is a complex structure, $L_a^2 = -\mathrm{id}$, and the defect form $H(\ell^{\alpha}_ax,y) - H(x,\ell^{\alpha}_ay)$ vanishes exactly for the odd parameters. The signed sandwich is the product $\Sigma^{\alpha}_{a,b} = \ell^{\alpha}_aR_{\alpha(b)}$, and its adjoint is the product of the two adjoints in the reverse order, $R_{\alpha(b)}\ell^{\alpha}_{\alpha(a)}$, which agrees with the explicit form of *The Signed Adjoint Sandwich on a Lie Algebra*, so the one-sided adjoint is the building block of the two-sided one. The degenerate cases are the trivial grading, in which no parameter is self-adjoint, the inner involution, in which the eigenspaces of the involution replace the grading, and the degenerate or non-isometric form, in which the adjoint is not everywhere defined.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H$ | the non-degenerate invariant Hermitian form |
| $\ell^{\alpha}_a = L_a\alpha$ | the signed left multiplication |
| $(\ell^{\alpha}_a)^{*} = -\alpha L_a$ | the explicit adjoint |
| $(\ell^{\alpha}_a)^{*} = \ell^{\alpha}_{-\alpha(a)} = -\ell^{\alpha}_{\alpha(a)}$ | the adjoint as a signed left multiplication |
| $(\ell^{\alpha}_a)^{*} = \ell^{\alpha}_a \iff a\in\mathrm{G}^{-}$ | self-adjointness for the odd parameters |
| $(\ell^{\alpha}_a)^{*} = -\ell^{\alpha}_a \iff a\in\mathrm{G}^{+}$ | skew-adjointness for the even parameters |
| $L_a^{2} = -\mathrm{id}$ | the unitarity condition |
| $H_{\ell}(x,y)$ | the defect of the self-adjointness |
| $\Sigma^{\alpha}_{a,b} = \ell^{\alpha}_aR_{\alpha(b)}$ | the sandwich as a product |
| $(\Sigma^{\alpha}_{a,b})^{*} = R_{\alpha(b)}\ell^{\alpha}_{\alpha(a)}$ | the adjoint of the sandwich |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for the invariant forms, the skew-adjoint multiplications and the complex structures.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, second edition, 2002), for the invariant forms, the Cartan involution and the self-adjoint operators.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the parity dichotomy, the adjoints of the signed operators and the unitarity conditions.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, second edition, 2015), for the adjoints of the multiplication operators and the unitary conditions.
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984), for the invariant forms, the adjoints and the complex structures on a Lie algebra.
