
# __The Signed Adjoint Sandwich on the Algebra of Arithmetic Functions__

## Introduction

The signed sandwich $S^\alpha_{a,b}(f)=a*\alpha(f)*b$ is the two-sided operator in which the grade involution is inserted between two multiplications, and its adjoint for the coefficient form is the **signed adjoint sandwich**
$$
S^{\alpha*}_{a,b}=\bigl(S^\alpha_{a,b}\bigr)^*=\alpha\,\Theta_{a*b}=\Theta_{\alpha(a*b)}\,\alpha ,
$$
where $\Theta_c$ is the transposed multiplication. This article studies the adjoint operator as an object in its own right: its closed form, its products, its kernel, its relation to the transposed algebra, and the criteria under which the signed sandwich is self-adjoint or unitary. The signed sandwich itself is *The Signed Sandwich on the Algebra of Arithmetic Functions*; the one-sided adjoints are *The Adjoint of the Left Multiplication on the Algebra of Arithmetic Functions* and *The Signed Adjoint of the Left Multiplication on the Algebra of Arithmetic Functions*. Nothing here reads a distance as an object.

## The Signed Adjoint Sandwich

### Definition and closed form

**Definition.** The **signed adjoint sandwich** is
$$
S^{\alpha*}_{a,b}=S^{\alpha\dagger}_{a,b}:\mathcal{A}\to\mathcal{A},\qquad S^{\alpha\dagger}_{a,b}=\bigl(S^\alpha_{a,b}\bigr)^* ,
$$
the adjoint being taken with respect to the coefficient form $\langle f,g\rangle=\sum_nf(n)\overline{g(n)}$.

**Theorem.** For all $a,b$,
$$
S^{\alpha\dagger}_{a,b}=L_{\alpha(a*b)}^*=\alpha\,\Theta_{a*b}=\Theta_{\alpha(a*b)}\,\alpha ,
$$
and explicitly
$$
\bigl(S^{\alpha\dagger}_{a,b}g\bigr)(k)=\lambda(k)\sum_{m\ge1}\overline{(a*b)(m)}\,g(mk).
$$
The operator is anti-linear in the pair $(a,b)$ through the product $a*b$; it depends on $a,b$ only through $a*b$; and it is the transposed multiplication by $\alpha(a*b)$ composed with the grade involution.

**Proof.** The signed sandwich factors as $S^\alpha_{a,b}=L_{a*b}\alpha=\alpha L_{\alpha(a*b)}$ on the commutative algebra; the adjoint of a composite is the composite of the adjoints in the reverse order, so $S^{\alpha\dagger}_{a,b}=\alpha^*L_{a*b}^*=\alpha\Theta_{a*b}$, and $\alpha\Theta_c=\Theta_{\alpha(c)}\alpha$ by the computation of the transposed multiplication.

### Products and involution

**Theorem.** The signed adjoint sandwich satisfies
$$
\bigl(S^{\alpha\dagger}_{a,b}\bigr)^2=\alpha\Theta_c\alpha\Theta_c=\Theta_{\alpha(c)}\,\Theta_c=\Theta_{\alpha(c)*c},\qquad \bigl(S^{\alpha\dagger}_{a,b}\bigr)^*=S^\alpha_{a,b},
$$
more precisely
$$
\bigl(S^{\alpha\dagger}_{a,b}\bigr)^2=\Theta_{a*b}\Theta_{a*b}\alpha^2=\Theta_{a*b}^2 ,
$$
and the two products with the signed sandwich are $S^{\alpha\dagger}S^\alpha=\Theta_{\alpha(c)}L_{c}$ and $S^\alpha S^{\alpha\dagger}=L_{\alpha(c)}\Theta_{c}$ with $c=a*b$, the grade involution cancelling in the definition of the adjoint.

**Proof.** The identity $\alpha\Theta_c\alpha=\Theta_{\alpha(c)}$ and the multiplicativity $\Theta_c\Theta_d=\Theta_{c*d}$ give $(\alpha\Theta_c)^2=\alpha\Theta_c\alpha\Theta_c=\Theta_{\alpha(c)}\Theta_c=\Theta_{\alpha(c)*c}$; the products with the sandwich are computed by inserting the definitions, and the $\alpha$'s cancel because $\alpha^2=\mathrm{id}$.

**Corollary (self-adjointness and unitarity).** The signed sandwich is self-adjoint exactly when $c=a*b$ is a real scalar multiple of the identity,
$$
S^\alpha_{a,b}=S^{\alpha\dagger}_{a,b}\iff \Theta_c=L_c\iff c=\gamma\varepsilon,\ \gamma\in\mathbb{R},
$$
and it is unitary exactly when
$$
S^\alpha_{a,b}\ \text{unitary}\iff \Theta_{\alpha(c)}L_c=L_{\alpha(c)}\Theta_c=\mathrm{id}\iff c=\gamma\varepsilon,\ |\gamma|=1 .
$$
Thus the balanced signed adjoint sandwich with $c=\varepsilon$ is the grade involution $\alpha$, self-adjoint and unitary.

**Proof.** $S^\alpha_{a,b}=S^{\alpha\dagger}_{a,b}$ is $\alpha L_c=\alpha\Theta_c$, that is $\Theta_c=L_c$, whose solution is $c=\gamma\varepsilon$ with $\gamma$ real; unitarity is the two product identities, as in *The Signed Sandwich on the Algebra of Arithmetic Functions*.

## The Comparison with the Ring

**Theorem (comparison).** In a noncommutative ring with involution the signed adjoint sandwich of the pair $(a,b)$ is the signed sandwich of the pair $(\delta(a),\delta(b))$, $\delta=\sigma\alpha$, so that the adjoint is again a two-sided signed sandwich. Over the commutative algebra of arithmetic functions this fails:
$$
S^{\alpha\dagger}_{a,b}=\Theta_{\alpha(a*b)}\alpha
$$
is a **one-sided** signed operator, not a two-sided sandwich, and it cannot be written as $S^\alpha_{c,d}$ for any $c,d$ unless $c$ is a unit. The discrepancy is the commutativity of the algebra, which collapses the two sides into the product $a*b$ and leaves only the transposed multiplication.

**Proof.** The noncommutative formula is the computation of the adjoint of a two-sided product; in the commutative case the sandwich factors through the product and the adjoint is a single transposed multiplication, which is a left multiplication only for the units. This is the same obstruction as in *The Signed Sandwich on the Algebra of Arithmetic Functions*.

## Worked Examples

**Example ($c=\varepsilon$).** $S^{\alpha\dagger}_{\varepsilon,\varepsilon}=\Theta_\varepsilon\alpha=\alpha$, the grade involution; the balanced case.

**Example ($c=\delta_p$).** $S^{\alpha\dagger}_{a,b}=\Theta_{\alpha(\delta_p)}\alpha=\Theta_{-\delta_p}\alpha=\alpha S_p$, the signed adjoint of the isometry $\alpha D_p$; it is a co-isometry with $S^{\alpha\dagger}S^\alpha=P_p$ up to a sign.

**Example ($c=d$).** For $a=b=\mathbf 1$ the product is the divisor function $d$, and $S^{\alpha\dagger}=\Theta_{\alpha(d)}\alpha$, which is neither self-adjoint nor unitary nor a signed sandwich of an element.

## Failure of the Degenerate Cases

The signed adjoint sandwich fails in four degenerate configurations. First, it is not a two-sided sandwich: it has one multiplication and the grade involution on the outside, so the class of the signed operators is not closed under adjunction. Second, it is self-adjoint only for the real scalar products and unitary only for the unitary scalar products, so the "nice" signed adjoint sandwiches are the degenerate ones. Third, the transposed multiplication is not bounded on the finitely supported functions for a general $c$ and the adjoint must be taken on the appropriate domain. Fourth, the formula $S^{\alpha\dagger}=S^\alpha_{\delta(a),\delta(b)}$ of the ring theory cannot be restored by any nondegenerate form, because the only form making the convolution-invariant operators self-adjoint to a left multiplication is the rank-one augmentation form. These are the boundary cases of the adjoint sandwich.

## Summary

The signed adjoint sandwich $S^{\alpha\dagger}_{a,b}=(S^\alpha_{a,b})^*$ of the two-sided signed sandwich $S^\alpha_{a,b}(f)=a*\alpha(f)*b$ is the transposed multiplication $\alpha\Theta_{a*b}=\Theta_{\alpha(a*b)}\alpha$, depending on $a,b$ only through the product $a*b$; it is the adjoint of the adjoint, its square is $\Theta_{\alpha(c)*c}$, its products with the signed sandwich are $\Theta_{\alpha(c)}L_c$ and $L_{\alpha(c)}\Theta_c$ with $c=a*b$, and the signed sandwich is self-adjoint exactly for $c$ a real scalar and unitary exactly for $c$ a unitary scalar. The noncommutative adjoint formula $S^\alpha_{\delta(a),\delta(b)}$ fails, the adjoint sandwich is one-sided rather than two-sided, and the degenerate cases are the collapse to the product, the scalar self-adjointness, the unboundedness of the transposed multiplication and the rank-one augmentation form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S^\alpha_{a,b}(f)=a*\alpha(f)*b$ | Signed sandwich |
| $S^{\alpha\dagger}_{a,b}=(S^\alpha_{a,b})^*=\alpha\Theta_{a*b}$ | Signed adjoint sandwich |
| $(S^{\alpha\dagger}_{a,b}g)(k)=\lambda(k)\sum_m\overline{(a*b)(m)}g(mk)$ | Explicit form |
| $(S^{\alpha\dagger})^2=\Theta_{\alpha(c)*c}$ | The square |
| $S^{\alpha\dagger}S^\alpha=\Theta_{\alpha(c)}L_c$ | Product with the sandwich |
| $c=\gamma\varepsilon$, $\gamma\in\mathbb{R}$ | Self-adjointness |
| $c=\gamma\varepsilon$, $|\gamma|=1$ | Unitarity |
| $\delta=\sigma\alpha$ | The composite involution |

## Further Reading

- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the sandwich and its adjoint.
- Tsit Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for the transposed multiplication and the trace forms.
- Israel Gohberg and Mark Krein, *Theory of Volterra Operators in Hilbert Space* (American Mathematical Society, 1970), for the transposed convolution operators.
- Paul Halmos, *A Hilbert Space Problem Book* (Springer, 1982), for the adjointable operators.
- Einar Hille and Ralph Phillips, *Functional Analysis and Semi-Groups* (American Mathematical Society, 1957), for the convolution operators on the weighted spaces.
