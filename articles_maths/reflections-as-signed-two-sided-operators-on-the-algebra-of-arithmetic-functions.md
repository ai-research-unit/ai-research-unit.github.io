
# __Reflections as Signed Two-Sided Operators on the Algebra of Arithmetic Functions__

## Introduction

Let $\mathcal{A}$ be the algebra of arithmetic functions under Dirichlet convolution, graded by the parity of the number of prime factors $\Omega$, with grade involution $\alpha(f)=\lambda f$. For a unit $u$ of $\mathcal{A}$ the **reflection** is the signed two-sided operator $r_u(f)=u*\alpha(f)*u^{-1}$; it is the arithmetic form of the reflection of the written theory of a ring with involution, and it is the operator that reverses the grading while conjugating by the unit. The purpose of this article is to determine the reflections, to describe the correspondence between a unit and the involution it defines, and to record the failure of that correspondence in the commutative case. The answer is sharp: every unit defines the same reflection, namely $\alpha$ itself, so the correspondence is constant and the reflections form a single operator. The general signed sandwich of which the reflection is a special case is treated in *The Signed Sandwich on the Algebra of Arithmetic Functions*, this category; the noncommutative theory, where the correspondence is nontrivial, is *Reflections as Signed Two-Sided Operators on a Ring*, written in an earlier part.

The notation is that fixed for the category. The form is the coefficient form $\langle f,g\rangle=\sum_nf(n)\overline{g(n)}$ on $\mathcal{H}=\ell^2$. The unit group is $\mathcal{A}^\times=\{u:u(1)\ne0\}$, so a general unit is an arbitrary arithmetic function with $u(1)\ne0$ and infinite support. The coefficient involution is $\sigma(f)=\overline{f}$, the grade involution is $\alpha(f)=\lambda f$, and $\delta=\sigma\alpha$. Nothing here reads a distance as an object.

## The Reflection of a Unit

### Definition

**Definition.** For $u\in\mathcal{A}^\times$ the **reflection** is the signed two-sided operator
$$
r_u:\mathcal{A}\to\mathcal{A},\qquad r_u(f)=u*\alpha(f)*u^{-1},
$$
where $u^{-1}$ is the Dirichlet inverse of $u$.

**Theorem.** For every unit $u$,
$$
r_u=\alpha .
$$
Consequently the reflection of a unit is independent of the unit, the map $u\mapsto r_u$ is constant on $\mathcal{A}^\times$, and the signed inner conjugation
$$
\operatorname{conj}_u(x)=u*x*u^{-1}
$$
of the graded algebra satisfies $\operatorname{conj}_u\circ\alpha=\alpha\circ\operatorname{conj}_u$ and $\operatorname{conj}_u=\mathrm{id}$ on $\mathcal{A}$.

**Proof.** The algebra is commutative, so $u*\alpha(f)*u^{-1}=\alpha(f)*(u*u^{-1})=\alpha(f)*\varepsilon=\alpha(f)$; hence $r_u=\alpha$. The inner conjugation is $u*x*u^{-1}=x*(u*u^{-1})=x$ because $*$ is commutative. The commutation with $\alpha$ is the multiplicativity of $\alpha$ together with commutativity.

### Properties of the reflection

**Theorem.** The operator $\alpha$ is an involutive unitary algebra automorphism of $\mathcal{A}$:
$$
\alpha^2=\mathrm{id},\qquad \alpha(x*y)=\alpha(x)*\alpha(y),\qquad \alpha^*=\alpha,\qquad \alpha^*\alpha=\alpha\alpha^*=\mathrm{id},
$$
and it reverses the grading, $\alpha(\mathcal{A}_{\bar i})=\mathcal{A}_{\bar{1-i}}$. Its fixed algebra is the even part, $\mathcal{A}^\alpha=\mathcal{A}_{\bar0}$, and its $(-1)$-eigenspace is the odd part, $\mathcal{A}_{\bar1}$.

**Proof.** $\alpha^2(f)=\lambda^2f=f$ because $\lambda(n)=\pm1$; the multiplicativity is the complete multiplicativity of $\lambda$, $\lambda(mn)=\lambda(m)\lambda(n)$; the self-adjointness is $\langle\alpha f,g\rangle=\sum_n\lambda(n)f(n)\overline{g(n)}=\sum_nf(n)\overline{\lambda(n)g(n)}=\langle f,\alpha g\rangle$ because $\lambda$ is real. The grading statement and the eigenspace description are the definitions.

## The Correspondence with the Involutions

### The involutive signed sandwiches

**Theorem.** Write $S^\alpha_c=L_c\alpha=L_{\alpha(c)}$ for the signed left multiplication by $c$, and note $L_c\alpha=\alpha L_{\alpha(c)}$. Then $S^\alpha_c$ is an involution if and only if $c*c=\varepsilon$, and the involutive signed sandwiches are exactly the maps $S^\alpha_c$ with $c$ a unit of $\mathcal{A}$ satisfying $c*c=\varepsilon$. The only such sandwich that is also unitary is $\gamma\alpha$ with $|\gamma|=1$.

**Proof.** $\bigl(S^\alpha_c\bigr)^2=L_c\alpha L_c\alpha=L_cL_c\alpha^2=L_{c*c}$, so $S^\alpha_c$ is an involution exactly when $c*c=\varepsilon$. The unitarity statement is the computation of unitarity for the signed sandwiches in *The Signed Sandwich on the Algebra of Arithmetic Functions*: a unitary sandwich is $c=\gamma\varepsilon$.

**Corollary (the correspondence).** The **reflection** $r_u$ corresponds to the unit $u$, but the corrrespondence is not injective: the fibre of the map $u\mapsto r_u$ is the whole unit group $\mathcal{A}^\times$, and the image is the single element $\alpha$. Equivalently, the involutive signed sandwiches are exactly $\alpha$ and $-\alpha$, corresponding to the two solutions $c=\pm\varepsilon$ of $c*c=\varepsilon$ in the unit group.

**Proof.** The first statement is the theorem. For the second, telescoping the equations $(c*c)(n)=0$ for $n>1$ shows that $c(n)=0$ for every $n>1$, so the only solutions in $\mathcal{A}^\times$ are $c=\pm\varepsilon$, giving the sandwiches $\pm\alpha$.

### The degenerate failure

**Theorem (failure in the commutative case).** Over the commutative algebra $\mathcal{A}$ the following hold. The signed inner automorphism group is trivial, since $\operatorname{conj}_u=\mathrm{id}$ for every unit. The reflection group is generated by $\alpha$ and is $\mathbb{Z}/2\mathbb{Z}$. The correspondence between the elements acting by an involution and the involutions is many-to-one, and it carries the whole unit group to one map. No two-sided operator of the form $f\mapsto u\,\alpha(f)\,u^{-1}$ distinguishes the units.

**Proof.** Every assertion is the computation $u*\alpha(f)*u^{-1}=\alpha(f)$. The first and the last are restatements since $u*u^{-1}=\varepsilon$ and $*$ is commutative.

**Remark (the comparison with the noncommutative theory).** In the noncommutative ring of *Reflections as Signed Two-Sided Operators on a Ring* the map $u\mapsto r_u$ has the whole unit group as its domain and its fibres are the cosets of the central units; the reflections form a large group and the correspondence with the involutions carries real information. The commutativity of $\mathcal{A}$ destroys exactly this information, and the destruction is total rather than partial: the unit group is as large as possible and the image is as small as possible. This is the degenerate case of the whole family of signed structures over a commutative algebra.

## Worked Examples

**Example ($u=\delta_p$).** $r_{\delta_p}(f)=\delta_p*\alpha(f)*\delta_{p^{-1}}$; but $\delta_p^{-1}$ does not exist, since $\delta_p(1)=0$; the operator is not a reflection. This shows that the signed two-sided operator is defined only on the unit group, and that the convolution by a nonunit can be an involution without being a reflection.

**Example ($u=\mathbf 1$).** $\mathbf 1$ is a unit with $\mathbf 1^{-1}=\mu$, and $r_{\mathbf 1}(f)=\mathbf 1*\alpha(f)*\mu$; by the theorem this is $\alpha(f)$, and indeed $\mathbf 1*\mu=\varepsilon$.

**Example ($u=\lambda$).** $\lambda$ is completely multiplicative, hence a unit with inverse $\mu\lambda$, and $r_\lambda(f)=\lambda*\alpha(f)*\mu\lambda=\alpha(f)$; the unit $u=\lambda$ gives the same reflection as $u=\mathbf 1$.

**Example (the involution $c*c=\varepsilon$).** For $c=\varepsilon$ and $c=-\varepsilon$, $S^\alpha_c=\alpha$ and $-\alpha$; both are involutions, and the second is not a reflection because the reflection of the unit $u$ has $c=u*u^{-1}=\varepsilon$ and the value $-\alpha$ is not attained by any unit.

## Failure of the Degenerate Cases

The failures are recorded above; collected, they are the following. First, the reflection is unique, so the correspondence between the units and the reflections is constant and carries no information. Second, the signed inner automorphism group is trivial, so every signed two-sided operator of the form $f\mapsto u\,\alpha(f)\,u^{-1}$ is the same one. Third, the involutive signed sandwiches $S^\alpha_c$ with $c*c=\varepsilon$ are not reflections, because their $c$ need not be of the form $u*u^{-1}=\varepsilon$; the set of involutions is therefore strictly larger than the set of reflections, and the extra involutions $-\alpha$ and the general $c*c=\varepsilon$ are the degenerate cases. Fourth, the operator $r_u$ is defined only for units, and the convolution by a nonunit may be an involution without being a reflection, which is the failure at the boundary of the unit group. All four are consequences of the commutativity of the algebra of arithmetic functions.

## Summary

For a unit $u$ of the algebra of arithmetic functions the reflection is $r_u(f)=u*\alpha(f)*u^{-1}$, and the commutativity of the Dirichlet convolution gives $r_u=\alpha$ for every unit, so the reflection is unique and is the grade involution. The reflection is an involutive unitary algebra automorphism, self-adjoint for the coefficient form, reversing the grading, with fixed algebra the even part and $(-1)$-eigenspace the odd part. The involutive signed sandwiches are the operators $S^\alpha_c=L_c\alpha$ with $c*c=\varepsilon$, and the only unitary ones are $\gamma\alpha$ with $|\gamma|=1$. The correspondence between the units and the reflections is constant with fibre the whole unit group, the signed inner automorphism group is trivial, and the correspondence with the involutions is many-to-one: these are the degenerate failures of the family over a commutative algebra, in contrast with the noncommutative ring where the same construction carries the multiplicative structure of the unit group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha(f)(n)=\lambda(n)f(n)$ | Grade involution |
| $r_u(f)=u*\alpha(f)*u^{-1}$ | Reflection of the unit $u$ |
| $r_u=\alpha$ | The reflection is unique |
| $\operatorname{conj}_u(x)=u*x*u^{-1}=x$ | The signed inner conjugation is trivial |
| $S^\alpha_c=L_c\alpha$ | Signed left multiplication |
| $(S^\alpha_c)^2=L_{c*c}$ | Square of a signed left multiplication |
| $c*c=\varepsilon$ | The involution condition |
| $c=\gamma\varepsilon$, $|\gamma|=1$ | The unitary condition |
| $\mathcal{A}^\alpha=\mathcal{A}_{\bar0}$ | The fixed algebra |

## Further Reading

- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the reflections and the involutions of a ring.
- Israel Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the inner automorphisms and the reflections.
- Tsit Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for the classification of the involutions.
- Paul Halmos, *A Hilbert Space Problem Book* (Springer, 1982), for the involutive unitary operators and their fixed spaces.
- Sterling Berberian, *Introduction to Hilbert Space* (Oxford University Press, 1961), for the reflection operators and the symmetry groups.
