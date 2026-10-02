
# __The Signed Adjoint of the Left Multiplication on the Algebra of Arithmetic Functions__

## Introduction

The signed left multiplication is the operator $T_a=L_a\alpha$, the composition of the left multiplication by $a$ with the grade involution; it is the basic odd operator of the algebra of arithmetic functions. Its adjoint for the coefficient form, the **signed adjoint of the left multiplication**, is
$$
T_a^{\alpha\dagger}=T_a^*=\alpha\,\Theta_a=\Theta_{\alpha(a)}\,\alpha ,
$$
the composition of the transposed multiplication by $\alpha(a)$ with the grade involution. This article computes the signed adjoint, its products and its square, the self-adjointness and unitarity criteria, and the comparison with the left multiplication by $\delta(a)$, which fails exactly as in the non-graded case. The signed left multiplication itself is *The Signed Left Multiplication on the Algebra of Arithmetic Functions*; the adjoint of the plain left multiplication is *The Adjoint of the Left Multiplication on the Algebra of Arithmetic Functions*, and the two-sided version is *The Signed Adjoint Sandwich on the Algebra of Arithmetic Functions*. Nothing here reads a distance as an object.

## The Signed Adjoint

### Definition and closed form

**Definition.** For $a\in\mathcal{A}$ the **signed left multiplication** is $T_a=L_a\alpha$, and its **signed adjoint** is
$$
T_a^{\alpha\dagger}=T_a^*,\qquad T_a^{\alpha\dagger}=\alpha\,\Theta_a=\Theta_{\alpha(a)}\,\alpha .
$$

**Theorem.** With respect to the coefficient form,
$$
\langle T_af,g\rangle=\sum_n\Bigl(\sum_{mk=n}a(m)\lambda(k)f(k)\Bigr)\overline{g(n)}=\langle f,\alpha\Theta_ag\rangle ,
$$
so that $T_a^{\alpha\dagger}=\alpha\Theta_a=\Theta_{\alpha(a)}\alpha$, with the explicit form
$$
\bigl(T_a^{\alpha\dagger}g\bigr)(k)=\lambda(k)\sum_{m\ge1}\overline{a(m)}\,g(mk)=\sum_{m\ge1}\lambda(m)\overline{a(m)}\,\lambda(k)\,g(mk).
$$
The signed adjoint is anti-linear in $a$; it is the adjoint of the adjoint, $(T_a^{\alpha\dagger})^*=T_a$; and it is never of the form $T_b$ for a nondegenerate $a$.

**Proof.** Insert $T_a=L_a\alpha$, use $\alpha^*=\alpha$ and $L_a^*=\Theta_a$ from *The Adjoint of the Left Multiplication on the Algebra of Arithmetic Functions*, and the identity $\alpha\Theta_a=\Theta_{\alpha(a)}\alpha$ of the transposed multiplication. The anti-linearity is the conjugation in $\Theta_a$.

### Products and square

**Theorem.** The signed adjoints satisfy
$$
T_a^{\alpha\dagger}T_b^{\alpha\dagger}=\Theta_{\alpha(a)}\Theta_{\alpha(b)}=\Theta_{\alpha(a)*\alpha(b)}=\Theta_{\alpha(a*b)},\qquad \bigl(T_a^{\alpha\dagger}\bigr)^2=\Theta_{\alpha(a)*\alpha(a)},
$$
and the products with the signed left multiplication are
$$
T_a^{\alpha\dagger}T_b=\alpha\Theta_aL_b\alpha=\Theta_{\alpha(a)}L_b,\qquad T_aT_b^{\alpha\dagger}=L_a\Theta_{\alpha(b)} ,
$$
so the signed adjoints close under composition, forming the transposed algebra with the elements $\alpha(a)$.

**Proof.** The products are computed by inserting the definitions and cancelling $\alpha^2=\mathrm{id}$; the multiplicativity $\Theta_c\Theta_d=\Theta_{c*d}$ of the transposed multiplication gives the first display. This is the transposed-algebra computation of *The Adjoint of the Left Multiplication on the Algebra of Arithmetic Functions* with the twist $\alpha$.

**Corollary (self-adjointness and unitarity).** The signed left multiplication is self-adjoint exactly for the real scalar multiples of the identity,
$$
T_a=T_a^{\alpha\dagger}\iff L_{\alpha(a)}=\Theta_a\iff a=\gamma\varepsilon,\ \gamma\in\mathbb{R},
$$
and it is unitary exactly for the unitary scalar multiples of the identity,
$$
T_a\ \text{unitary}\iff \alpha\Theta_aL_a\alpha=L_a\Theta_a=\mathrm{id}\iff a=\gamma\varepsilon,\ |\gamma|=1 .
$$
It is an isometry exactly when $\Theta_aL_a=\mathrm{id}$, which holds for $a=\gamma\delta_p$, $|\gamma|=1$.

**Proof.** Test the self-adjointness on $\delta_1$: $T_a\delta_1=\alpha(a)$ and $T_a^{\alpha\dagger}\delta_1=\alpha\Theta_a\delta_1=\lambda(1)\overline{a(1)}\delta_1=\overline{a(1)}\delta_1$, so equality forces $a=\gamma\varepsilon$, and then $T_a=\gamma\alpha$, $T_a^{\alpha\dagger}=\overline\gamma\alpha$, equal exactly for $\gamma$ real; the unitarity is the product identity, as in *The Signed Left Multiplication on the Algebra of Arithmetic Functions*.

## The Comparison with the Involution

**Theorem (comparison).** The expected formula in which the signed adjoint is the signed left multiplication of the transformed element,
$$
T_a^{\alpha\dagger}=T_{\delta(a)}\quad\text{with}\quad\delta=\sigma\alpha,
$$
does not hold over the algebra of arithmetic functions; the right side is $T_{\delta(a)}=L_{\delta(a)}\alpha=\alpha L_{\alpha(\delta(a))}\alpha$ and the left side is $\alpha\Theta_a$, and the two differ whenever $a$ is not a scalar multiple of the identity. The signed adjoint is a transposed operation on the elements, not a multiplication by a transformed element.

**Proof.** The right side is $T_{\delta(a)}=L_{\delta(a)}\alpha=\alpha L_{\alpha(\delta(a))}$, a left multiplication conjugated by $\alpha$, while the left side is $\alpha\Theta_a$; the two coincide exactly when $\Theta_a=L_{\alpha(\delta(a))}$, which by the criterion of the corollary forces $a=\gamma\varepsilon$. This is the graded analogue of the obstruction of *The Sandwich on the Algebra of Arithmetic Functions*.

## Worked Examples

**Example ($a=\varepsilon$).** $T_\varepsilon=\alpha$ and $T_\varepsilon^{\alpha\dagger}=\alpha$; the grade involution, self-adjoint and unitary.

**Example ($a=\delta_p$).** $T_{\delta_p}^{\alpha\dagger}=\alpha\Theta_{\delta_p}=\alpha S_p$, the signed adjoint of the isometry $\alpha D_p$; the product $T^{\alpha\dagger}T=\alpha S_pD_p\alpha=P_p$ is the projection onto the multiples of $p$.

**Example ($a=\mathbf 1$).** $T_{\mathbf 1}^{\alpha\dagger}=\alpha\Theta_{\mathbf 1}$; the operator is unbounded on the finitely supported functions, and its square is $\Theta_{\alpha(\mathbf 1)*\alpha(\mathbf 1)}=\Theta_{\lambda*\lambda}$.

## Failure of the Degenerate Cases

The signed adjoint of the left multiplication fails in four degenerate configurations. First, it is not a signed left multiplication, so the class of the signed left multiplications is not closed under adjunction; the adjoints form the transposed class. Second, the self-adjointness and the unitarity hold only at the scalar elements, so the graded operators that are self-adjoint are the degenerate ones. Third, the transposed multiplication is unbounded for a general element and the adjoint requires a weighted space for its domain. Fourth, the involution formula $T_a^{\alpha\dagger}=T_{\delta(a)}$ fails in the same way as the formula $L_a^*=L_{a^*}$ fails for the plain left multiplication; the only form restoring it is the rank-one augmentation form, on which the whole operator theory collapses. These are the boundary cases of the signed adjoint.

## Summary

The signed left multiplication $T_a=L_a\alpha$ has the signed adjoint $T_a^{\alpha\dagger}=\alpha\Theta_a=\Theta_{\alpha(a)}\alpha$ for the coefficient form, anti-linear in $a$, with $(T_a^{\alpha\dagger})^*=T_a$, products $T_a^{\alpha\dagger}T_b^{\alpha\dagger}=\Theta_{\alpha(a*b)}$ and square $\Theta_{\alpha(a)*\alpha(a)}$. It is self-adjoint exactly for $a=\gamma\varepsilon$ with $\gamma$ real, unitary exactly for $|\gamma|=1$, and an isometry exactly when $\Theta_aL_a=\mathrm{id}$; the involution formula $T_a^{\alpha\dagger}=T_{\delta(a)}$ fails outside the scalars, because the adjoint is a transposed operation and not a multiplication. The degenerate cases are the non-closure of the class, the scalar self-adjointness, the unboundedness and the rank-one augmentation form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_a=L_a\alpha$ | Signed left multiplication |
| $T_a^{\alpha\dagger}=\alpha\Theta_a=\Theta_{\alpha(a)}\alpha$ | Signed adjoint |
| $(T_a^{\alpha\dagger}g)(k)=\lambda(k)\sum_m\overline{a(m)}g(mk)$ | Explicit form |
| $(T_a^{\alpha\dagger})^*=T_a$ | Adjoint of the adjoint |
| $T_a^{\alpha\dagger}T_b^{\alpha\dagger}=\Theta_{\alpha(a*b)}$ | Product |
| $(T_a^{\alpha\dagger})^2=\Theta_{\alpha(a)*\alpha(a)}$ | The square |
| $a=\gamma\varepsilon$, $\gamma\in\mathbb{R}$ | Self-adjointness |
| $a=\gamma\varepsilon$, $|\gamma|=1$ | Unitarity |
| $\delta=\sigma\alpha$ | The composite involution |

## Further Reading

- Sterling Berberian, *Introduction to Hilbert Space* (Oxford University Press, 1961), for the adjoints of the products of operators.
- Paul Halmos, *A Hilbert Space Problem Book* (Springer, 1982), for the self-adjoint and unitary operators.
- Israel Gohberg and Mark Krein, *Theory of Volterra Operators in Hilbert Space* (American Mathematical Society, 1970), for the transposed convolution operators.
- Tsit Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for the involution and the transformed elements.
- Hugh Montgomery and Robert Vaughan, *Multiplicative Number Theory I: Classical Theory* (Cambridge University Press, 2007), for the arithmetic convolution.
