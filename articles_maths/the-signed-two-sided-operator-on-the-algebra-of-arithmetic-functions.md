
# __The Signed Two-Sided Operator on the Algebra of Arithmetic Functions__

## Introduction

Let $\mathcal{A}$ be the algebra of arithmetic functions under Dirichlet convolution, with its coefficient involution and its grade involution, and let the form of the category be the coefficient form $\langle f,g\rangle=\sum_nf(n)\overline{g(n)}$ on $\mathcal{H}=\ell^2$. For fixed $a,b\in\mathcal{A}$ the **signed two-sided operator** is the operator $S^\alpha_{a,b}(f)=a*\alpha(f)*b$, obtained from the two-sided multiplication by inserting the grade involution in the middle. This is the arithmetic version of the signed two-sided operator of the written article on a ring, and it is the operator whose adjoint, unitarity and self-adjointness are the subject here. The algebra $\mathcal{A}$ is commutative, and this single fact changes the shape of the answers: the two-sided factors through the left multiplication by $a*b$, the two-sided operator is the same for all factorisations of the product, and the reflection associated with a unit is the same for every unit. The article states the general formulas, identifies the unitary and self-adjoint members, and records exactly where the commutative case degenerates.

The grade involution is $\alpha(f)(n)=\lambda(n)f(n)$, where $\lambda$ is the Liouville function, $\lambda(n)=(-1)^{\Omega(n)}$ and $\Omega(n)$ is the number of prime factors of $n$ counted with multiplicity. The coefficient involution is $\sigma(f)(n)=\overline{f(n)}$; $\alpha$ and $\sigma$ commute, and $\delta=\sigma\alpha$ is the composite $\delta(f)=\lambda\,f^{*}$. The algebra $\mathcal{A}$ is graded by the parity of $\Omega$, $\mathcal{A}=\mathcal{A}_{\bar0}\oplus\mathcal{A}_{\bar1}$, and $\alpha$ is the associated involution. The form is the one fixed for the whole category; the adjoint of the left multiplication is treated in *The Adjoint of the Left Multiplication on the Algebra of Arithmetic Functions*, later in this category. Nothing here reads a distance as an object.

## The Two-Sided Operator and its Adjoint

### The two-sided operator

**Definition.** For $a,b\in\mathcal{A}$ the **signed two-sided operator** is the operator
$$
S^\alpha_{a,b}:\mathcal{A}\to\mathcal{A},\qquad S^\alpha_{a,b}(f)=a*\alpha(f)*b .
$$
The **signed left multiplication** is $T_a=S^\alpha_{a,\varepsilon}$ and the **signed right multiplication** is $U_b=S^\alpha_{\varepsilon,b}$.

**Proposition.** $S^\alpha_{a,b}=L_{a*b}\circ\alpha=\alpha\circ L_{a*b}$ on the commutative algebra $\mathcal{A}$, where $L_cf=c*f$; the grading is reversed,
$$
S^\alpha_{a,b}(\mathcal{A}_{\bar i})\subseteq\mathcal{A}_{\overline{\,i+|a|+|b|+1\,}}\qquad (i=0,1),
$$
and $S^\alpha_{a,b}$ depends on $a$ and $b$ only through the product $a*b$.

**Proof.** Commutativity of $*$ gives $a*\alpha(f)*b=(a*b)*\alpha(f)$, and $\alpha$ is a homomorphism: $\alpha(x*y)=\alpha(x)*\alpha(y)$ because $\lambda$ is completely multiplicative. The grading statement is the definition $|f|=\Omega(n)$ mod $2$ on the support together with $\lambda(mn)=\lambda(m)\lambda(n)$. Dependence only on $a*b$ is immediate from the factorisation.

### The adjoint

**Theorem (the signed adjoint).** With respect to the form of the category, the adjoint of the signed two-sided operator is
$$
\boxed{\;\bigl(S^\alpha_{a,b}\bigr)^{*} = \alpha\circ\mathrm{Sd}_{a*b}\;},
$$
where $\mathrm{Sd}_c=L_c^*$ is the transposed multiplication,
$$
(\mathrm{Sd}_cg)(k)=\sum_{m\ge1}\overline{c(m)}\,g(mk).
$$
Equivalently $\bigl(S^\alpha_{a,b}\bigr)^{*}(g)(k)=\lambda(k)\sum_{m}\overline{(a*b)(m)}\,g(mk)$.

**Proof.** The grade involution is self-adjoint for the coefficient form: $\langle\alpha f,g\rangle=\sum_n\lambda(n)f(n)\overline{g(n)}=\sum_nf(n)\overline{\lambda(n)g(n)}=\langle f,\alpha g\rangle$, because $\lambda$ is real and $\lambda^2=1$. Hence $\alpha^*=\alpha$. The adjoint of a product is the product of the adjoints in the reverse order, $\bigl(L_{a*b}\alpha\bigr)^*=\alpha^*L_{a*b}^*=\alpha\mathrm{Sd}_{a*b}$. The explicit expression follows from $\mathrm{Sd}_cg=\lambda^\prime\ldots$ computed directly: $(\mathrm{Sd}_cg)(k)=\sum_m\overline{c(m)}g(mk)$, and $\alpha\mathrm{Sd}_cg=\lambda(k)\sum_m\overline{c(m)}g(mk)$.

**Corollary (comparison with the two-sided case).** The signed two-sided operator is that two-sided operator in which the grade involution is inserted between two multiplications; in the noncommutative case of *The Signed Two-Sided Operator on a Ring* the adjoint is the two-sided operator $S^\alpha_{\delta(a),\delta(b)}$ with $\delta=\sigma\alpha$, whereas here the adjoint is the left multiplication by $\delta(a*b)$ composed with $\alpha$. The difference is the commutativity of the algebra: the product $a*b$ carries all the information, and the two-sided operator cannot distinguish the two sides.

## Self-Adjointness and Unitarity

### The conditions

**Theorem.** Write $c=a*b$. Then
$$
\boxed{\;S^\alpha_{a,b}\ \text{is self-adjoint} \iff \alpha\mathrm{Sd}_c=\alpha L_c \iff \mathrm{Sd}_c=L_c\;},
$$
and
$$
\boxed{\;S^\alpha_{a,b}\ \text{is an isometry} \iff \mathrm{Sd}_cL_c=\mathrm{id},\qquad S^\alpha_{a,b}\ \text{is unitary} \iff c=\gamma\varepsilon \text{ with } |\gamma|=1\;},
$$
the first equivalence holding because $\alpha$ is unitary and $\|S^\alpha_{a,b}f\|=\|L_cf\|$, and the second because a unitary convolution operator is a scalar multiple of the identity.

**Proof.** Self-adjointness is the equality $\alpha\mathrm{Sd}_c=\alpha L_c$, which is $\mathrm{Sd}_c=L_c$ after applying the invertible $\alpha$. Since $\alpha$ is unitary, $\|Sf\|=\|L_cf\|$, so $S$ is an isometry exactly when $\mathrm{Sd}_cL_c=\mathrm{id}$; it is unitary exactly when also $L_c\mathrm{Sd}_c=\mathrm{id}$, and applying that identity to $\delta_1$ gives $\overline{c(1)}\,c=\delta_1$, whence $c=\gamma\delta_1$ with $|\gamma|=1$.

**Corollary (the balanced two-sided operators).** If $a*b=\varepsilon$ then $S^\alpha_{a,b}=\alpha$, and $\alpha$ is unitary and self-adjoint. If $c=\gamma\delta_p$ for a prime $p$ and a scalar $\gamma$ with $|\gamma|=1$, then $\mathrm{Sd}_cL_c=\mathrm{id}$ and $S^\alpha_{a,b}$ is a nonunitary isometry with $S^\alpha_{a,b}(S^\alpha_{a,b})^*=P_p$; the unitary signed two-sided operators are exactly the maps $\gamma\alpha$ with $|\gamma|=1$, obtained from $c=\gamma\varepsilon$.

**Proof.** If $c=\varepsilon$ then $L_c=\mathrm{id}$ and $S^\alpha=\alpha$. If $c=\gamma\delta_p$ then $\mathrm{Sd}_cL_c=|\gamma|^2\mathrm{id}$ and $L_c\mathrm{Sd}_c=|\gamma|^2P_p$, by the computation for the shifts of *The Shift Operator on the Coefficients*; the first is the identity when $|\gamma|=1$ but the second is not, so the operator is an isometry and not unitary. The conditions $c*c=\varepsilon$ for an involution and $c=\gamma\varepsilon$ for a unitary are the two extreme cases of the general system.

### The general unitarity condition

**Proposition.** For finite support $c$ the equation $\mathrm{Sd}_cL_c=\mathrm{id}$ is equivalent to
$$
\sum_{m\ge1}|c(m)|^2=1 \quad\text{and}\quad \sum_{\substack{m\ge1:\ s\mid mk}}\overline{c(m)}\,c(mk/s)=0 \quad\text{for all } k\ge1 \text{ and } s\ne k.
$$
In particular a finite-support function always has finite-dimensional adjoint and the condition is a finite system of quadratic equations in the coefficients.

**Proof.** Expand $\mathrm{Sd}_cL_cf(k)=\sum_{s\mid\cdot}f(s)\sum_{m:s\mid mk}\overline{c(m)}c(mk/s)$; for the coefficient of $f(k)$ the sum is $\sum_m|c(m)|^2$, and for $s\ne k$ it is the second sum. Setting all coefficients of nonidentity $f$ to zero gives the displayed system.

## Worked Examples

**Example (the grade involution).** $a=b=\varepsilon$: $S^\alpha_{\varepsilon,\varepsilon}=\alpha$ is the grade involution, unitary and self-adjoint, and its fixed algebra is $\mathcal{A}_{\bar0}$.

**Example (the unit-generated two-sided operators).** For $a=\delta_p$, $b=\varepsilon$: $c=\delta_p$, $S^\alpha_{\delta_p,\varepsilon}=\alpha D_p$, unitary by the corollary; it is the signed left multiplication of *The Signed Left Multiplication on the Algebra of Arithmetic Functions*.

**Example (a nonunitary two-sided operator).** For $a=b=\mathbf 1$: $c=d$, the divisor function, and $S^\alpha_{\mathbf 1,\mathbf 1}=\alpha\,M_d$ with $M_d$ the convolution with $d$; it is neither self-adjoint nor unitary, because $\mathrm{Sd}_dL_d\ne\mathrm{id}$ and $\mathrm{Sd}_d\ne L_d$.

## Failure of the Degenerate Cases

Three degeneracies are intrinsic to the commutative case. First, the two-sided operator depends only on the product $a*b$, so the map $(a,b)\mapsto S^\alpha_{a,b}$ has fibres of dimension the whole kernel of the product map; the "two-sided" information is lost, and questions about $a$ and $b$ separately have no answer in terms of the operator. Second, the reflection generated by a unit, $S^\alpha_{u,u^{-1}}$, is the grade involution for **every** unit $u$; the correspondence between the units and the reflections is constant, so the distinguished class of reflections of the noncommutative theory collapses to a single element. Third, and most important, the adjoint formula $S^\alpha_{\delta(a),\delta(b)}$ of the noncommutative signed two-sided operator does not hold here, and it cannot be restored by any nondegenerate form: a form that is invariant under convolution, so that $L_a^*=L_{a^*}$, forces the grade involution to be non-adjointable, while a form that makes $\alpha$ self-adjoint destroys the convolution-invariance. The only form satisfying both is the augmentation form $\{f,g\}=f(1)\overline{g(1)}$, of rank one. This obstruction is in characteristic zero the statement that no nonzero trace annihilates the odd part; it is proved in *The Adjoint of the Left Multiplication on the Algebra of Arithmetic Functions* and used throughout the category.

## Summary

For $a,b$ in the algebra of arithmetic functions the signed two-sided operator is $S^\alpha_{a,b}(f)=a*\alpha(f)*b$, with $\alpha(f)=\lambda f$ the grade involution; on the commutative algebra it factors as $S^\alpha_{a,b}=\alpha L_{a*b}=L_{a*b}\alpha$ and depends on $a,b$ only through $a*b$. With respect to the coefficient form of the category its adjoint is $(S^\alpha_{a,b})^*=\alpha\mathrm{Sd}_{a*b}$, where $\mathrm{Sd}_c$ is the transposed multiplication $(\mathrm{Sd}_cg)(k)=\sum_m\overline{c(m)}g(mk)$; the two-sided operator is self-adjoint exactly when $\mathrm{Sd}_c=L_c$, an isometry exactly when $\mathrm{Sd}_cL_c=\mathrm{id}$, and unitary exactly when $c=\gamma\varepsilon$ with $|\gamma|=1$; the balanced two-sided operators with $a*b=\varepsilon$ give the grade involution, and the two-sided operators with $c=\gamma\delta_p$, $|\gamma|=1$, are nonunitary isometries. The noncommutative adjoint formula $S^\alpha_{\delta(a),\delta(b)}$ fails over the commutative algebra, and no nondegenerate form restores it: the only form for which both the convolution-invariance and the self-adjointness of $\alpha$ hold is the rank-one augmentation form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha(f)(n)=\lambda(n)f(n)$ | Grade involution |
| $S^\alpha_{a,b}(f)=a*\alpha(f)*b$ | Signed two-sided operator |
| $S^\alpha_{a,b}=\alpha L_{a*b}=L_{a*b}\alpha$ | Factorisation over a commutative algebra |
| $(S^\alpha_{a,b})^*=\alpha\mathrm{Sd}_{a*b}$ | The signed adjoint |
| $\mathrm{Sd}_cg(k)=\sum_m\overline{c(m)}g(mk)$ | Transposed multiplication |
| $\mathrm{Sd}_c=L_c$ | Self-adjointness condition |
| $\mathrm{Sd}_cL_c=\mathrm{id}$ | Unitarity condition |
| $S^\alpha_{u,u^{-1}}=\alpha$ | Balanced two-sided operator |
| $\delta=\sigma\alpha$ | The composite involution |

## Further Reading

- Hua Loo Keng, *Harmonic Analysis of Functions of Several Complex Variables in the Classical Domains* (American Mathematical Society, 1963), for the signed two-sided operators.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the involutions and the traces on a ring with involution.
- Tsit Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for the trace forms and the degenerate cases.
- Israel Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the behaviour of the two-sided operator in the presence of commutativity.
- Paul Halmos, *A Hilbert Space Problem Book* (Springer, 1982), for the adjointable operators and the positive forms.
