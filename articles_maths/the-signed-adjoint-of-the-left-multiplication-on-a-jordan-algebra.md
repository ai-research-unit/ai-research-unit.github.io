# __The Signed Adjoint of the Left Multiplication on a Jordan Algebra__

## Introduction

The **signed left multiplication** of a Jordan algebra with a grade involution is the one-sided operator obtained from the left multiplication by precomposition with the involution; intrinsically it is

$$
\ell^{\alpha}_a = L_a\circ\alpha , \qquad \ell^{\alpha}_a(x) = a\bullet\alpha(x) ,
$$

the Jordan form of the signed one-sided action of *The Signed Left Multiplication on a Jordan Algebra*, whose associative model is $\ell^{\alpha}_a(x) = a\,\alpha(x)$ on a special algebra $J = A^+$. The present article computes the **adjoint** of this operator with respect to the **natural pairing** of the category, the trace form $T(x,y) = \operatorname{tr}(L_{x\bullet y})$ of *The Adjoint of the Left Multiplication on a Jordan Algebra*, and relates it to the signed sandwich of *The Signed Adjoint Sandwich on a Jordan Algebra*.

The trace form is associative, $T(x\bullet y,z) = T(x,y\bullet z)$, so the left multiplication is self-adjoint, $L_a^{\dagger} = L_a$, and the grade involution is an isometry, $\alpha^{\dagger} = \alpha$; the adjoint of the composite is therefore the composite of the adjoints in the reverse order, and since $\alpha$ is an automorphism with $\alpha L_a\alpha^{-1} = L_{\alpha(a)}$,

$$
\bigl(\ell^{\alpha}_a\bigr)^{\dagger} = \bigl(L_a\circ\alpha\bigr)^{\dagger} = \alpha\circ L_a = L_{\alpha(a)}\circ\alpha = \ell^{\alpha}_{\alpha(a)} .
$$

The adjoint of the signed left multiplication is thus the signed left multiplication by the **image of the parameter under the grade involution**; it is **self-adjoint exactly when $\alpha(a) = a$**, and it is **unitary exactly when the unsigned left multiplication is an involution, $L_a^2 = \mathrm{id}$**, that is, when $a$ is a symmetry. The signed sandwich is the product of a signed and an unsigned one-sided action, $S^{\alpha}_{a,b} = \rho_b\ell^{\alpha}_a$, and the adjoint of that product is computed from the adjoints of its factors, recovering the rule of the signed adjoint sandwich.

The article assumes *The Signed Left Multiplication on a Jordan Algebra* for the signed one-sided action, its homogeneity and the fixed elements; *The Signed Adjoint Sandwich on a Jordan Algebra* for the signed sandwich and its adjoint; *The Adjoint of the Left Multiplication on a Jordan Algebra* for the trace form, its associativity and the self-adjointness of $L_a$ and $U_a$; *The Left and Right Multiplication Operators on a Jordan Algebra* for the quadratic representation and the symmetries; and *The Operators on an Algebra* for the ambient endomorphism algebra. Throughout, $J = A^+$ is a special unital Jordan algebra over a commutative ring $R$ in which $2$ is invertible, $\alpha$ is a grade involution of $A$, $L_a$ is the Jordan left multiplication, $\ell^{\alpha}_a = L_a\circ\alpha$ is the signed left multiplication, $T$ is the trace form and ${}^{\dagger}$ its adjoint; no norm, form, distance or geometric reflection occurs.

## The Signed Left Multiplication and Its Adjoint

### The Definition and the Unsigned Case

**Definition.** The **signed left multiplication** by $a$ is $\ell^{\alpha}_a = L_a\circ\alpha$, $\ell^{\alpha}_a(x) = a\bullet\alpha(x)$; for $\alpha = \mathrm{id}$ it is the ordinary left multiplication $L_a$.

**Theorem (the unsigned adjoint).** The unsigned left multiplication is self-adjoint, $L_a^{\dagger} = L_a$, and the adjoint of the signed left multiplication is the signed left multiplication at the image of the parameter:

$$
\bigl(\ell^{\alpha}_a\bigr)^{\dagger} = \ell^{\alpha}_{\alpha(a)} .
$$

*Proof.* The associativity of the trace form says $T(L_ax,y) = T(x,L_ay)$, so $L_a^{\dagger} = L_a$; the grade involution is an isometry, $T(\alpha x,y) = T(x,\alpha y)$, so $\alpha^{\dagger} = \alpha$. Hence $(\ell^{\alpha}_a)^{\dagger} = (L_a\circ\alpha)^{\dagger} = \alpha^{\dagger}\circ L_a^{\dagger} = \alpha\circ L_a$. Since $\alpha$ is an automorphism, $\alpha L_a = L_{\alpha(a)}\alpha$, so $\alpha\circ L_a = L_{\alpha(a)}\circ\alpha = \ell^{\alpha}_{\alpha(a)}$. $\square$

### Self-Adjointness

**Proposition.** The signed left multiplication is self-adjoint exactly when its parameter is fixed by the grade involution:

$$
\bigl(\ell^{\alpha}_a\bigr)^{\dagger} = \ell^{\alpha}_a \iff \alpha(a) = a .
$$

*Proof.* The adjoint is $\ell^{\alpha}_{\alpha(a)}$; the two are equal exactly when $L_{\alpha(a)} = L_a$, which for a non-degenerate trace form holds exactly when $\alpha(a) = a$. $\square$

**Corollary.** The signed left multiplication by an **even** element is self-adjoint and coincides with the unsigned left multiplication, $\ell^{\alpha}_a = L_a$ for $a$ even; for an odd element $\ell^{\alpha}_a = L_a\circ\alpha$ is the negative of the ordinary action conjugated by $\alpha$ on the argument, and it is not self-adjoint.

### Unitarity

**Theorem.** The signed left multiplication is unitary with respect to the adjoint exactly when the unsigned left multiplication is an involution:

$$
\bigl(\ell^{\alpha}_a\bigr)^{\dagger}\ell^{\alpha}_a = \ell^{\alpha}_a\bigl(\ell^{\alpha}_a\bigr)^{\dagger} = \mathrm{id} \iff L_a^2 = \mathrm{id} ,
$$

that is, exactly when $a$ is a **symmetry**.

*Proof.* $\ell^{\alpha\dagger}_a\ell^{\alpha}_a = \ell^{\alpha}_{\alpha(a)}\ell^{\alpha}_a = L_{\alpha(a)}\alpha L_a\alpha = L_{\alpha(a)}L_{\alpha(a)}\alpha^2 = L_{\alpha(a)}^2$, and similarly $\ell^{\alpha}_a\ell^{\alpha\dagger}_a = L_a^2$; the two are the identity exactly when $L_a^2 = L_{\alpha(a)}^2 = \mathrm{id}$, which is the symmetry condition. $\square$

## Relation to the Signed Sandwich

**Theorem.** The signed sandwich is the product of a signed and an unsigned one-sided action, $S^{\alpha}_{a,b} = \rho_b\ell^{\alpha}_a = \ell_a\rho^{\alpha}_b$, and its adjoint is

$$
\bigl(S^{\alpha}_{a,b}\bigr)^{\dagger} = \ell^{\alpha\dagger}_a\rho_b^{\dagger} = \ell^{\alpha}_{\alpha(a)}\rho_{\alpha(b)} ,
$$

which is the signed sandwich $\Sigma^{\alpha}_{\alpha(a),\alpha(b)}$ after the symmetrisation, in agreement with *The Signed Adjoint Sandwich on a Jordan Algebra*.

*Proof.* The anti-multiplicativity of the adjoint gives $(S^{\alpha}_{a,b})^{\dagger} = (\rho_b\ell^{\alpha}_a)^{\dagger} = \ell^{\alpha\dagger}_a\rho_b^{\dagger} = \ell^{\alpha}_{\alpha(a)}L_{\alpha(b)}$; the symmetrisation of $\rho_b\ell^{\alpha}_a$ over the outer parameter is the signed sandwich $U_{a,b}\circ\alpha$, and its adjoint is $U_{\alpha(a),\alpha(b)}\circ\alpha$ by *The Signed Adjoint Sandwich on a Jordan Algebra*. $\square$

**Corollary.** The adjoint of the one-sided layer and the adjoint of the two-sided layer are the same rule at the images of the parameters; the signed left multiplication is thus the one-sided case of the signed sandwich adjoint, exactly as in the associative case of *The Signed Adjoint of the Left Multiplication on a Ring*.

## Examples

**Example (the identity grade involution).** For $\alpha = \mathrm{id}$ the signed left multiplication is the unsigned one, $\ell^{\alpha}_a = L_a$, which is self-adjoint for every $a$; the unitarity condition is $L_a^2 = \mathrm{id}$, the symmetry condition, and it holds for the symmetries.

**Example (the transpose involution).** Let $J = H_n(F)$ with the transpose grade involution on the ambient matrix algebra; then $\ell^{\alpha}_a(x) = a\bullet x^{\mathsf{T}}$, and its adjoint is $\ell^{\alpha}_{a^{\mathsf{T}}}$. The operator is self-adjoint exactly when $a$ is symmetric, and unitary exactly when $a$ is a symmetry of the Jordan algebra.

**Example (the odd element).** For an odd element $a$ the signed left multiplication is $\ell^{\alpha}_a = L_a\circ\alpha$, which is not self-adjoint: $\ell^{\alpha\dagger}_a = \ell^{\alpha}_{\alpha(a)} = \ell^{\alpha}_{-a} = -\ell^{\alpha}_a$, so an odd parameter gives a skew-adjoint signed left multiplication.

## Summary

The **signed left multiplication** on a Jordan algebra is $\ell^{\alpha}_a = L_a\circ\alpha$, $\ell^{\alpha}_a(x) = a\bullet\alpha(x)$; with respect to the **trace form** its adjoint is the signed left multiplication at the image of the parameter,

$$
\bigl(\ell^{\alpha}_a\bigr)^{\dagger} = \ell^{\alpha}_{\alpha(a)} ,
$$

because the left multiplication is self-adjoint, $L_a^{\dagger} = L_a$, and the grade involution is an isometry, $\alpha^{\dagger} = \alpha$. It is **self-adjoint exactly when $\alpha(a) = a$**, and **unitary exactly when $L_a^2 = \mathrm{id}$**, that is, when $a$ is a symmetry. The signed sandwich $S^{\alpha}_{a,b} = \rho_b\ell^{\alpha}_a$ has the adjoint computed from the adjoints of its factors, and its symmetrisation recovers $\Sigma^{\alpha}_{\alpha(a),\alpha(b)}$ of *The Signed Adjoint Sandwich on a Jordan Algebra*; the signed left multiplication is the one-sided case of that rule. The identity involution, the transpose involution and the odd element are the worked examples. No norm, form, distance or geometric reflection occurs.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_a(x) = a\bullet x$ | Jordan left multiplication |
| $\ell^{\alpha}_a = L_a\circ\alpha$ | Signed left multiplication |
| $\ell^{\alpha}_a(x) = a\bullet\alpha(x)$ | Jordan form; associative form $a\alpha(x)$ |
| $(\ell^{\alpha}_a)^{\dagger} = \ell^{\alpha}_{\alpha(a)}$ | Adjoint of the signed left multiplication |
| $\alpha(a) = a$ | Self-adjointness condition |
| $L_a^2 = \mathrm{id}$ | Unitarity condition (symmetry) |
| $S^{\alpha}_{a,b} = \rho_b\ell^{\alpha}_a$ | Signed sandwich as a product |
| $(S^{\alpha}_{a,b})^{\dagger} = \ell^{\alpha}_{\alpha(a)}\rho_{\alpha(b)}$ | Adjoint of the sandwich from the factors |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the left multiplications, the trace form and the symmetries.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the one-sided multiplications, the quadratic representation and the structure group.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the signed one-sided actions and their adjoints.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the multiplication algebra and the operators on an algebra.
- Hel Braun and Max Koecher, *The Jordan Algebra Approach to Bounded Symmetric Domains* (Springer, 1966), for the left multiplications, the symmetries and the trace form.
