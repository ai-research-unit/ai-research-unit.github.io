
# __The Signed Left Multiplication on the Algebra of Random Variables__

## Introduction

The signed left multiplication of the algebra of random variables is the operator obtained by multiplying by a random variable and applying the grade involution,
$$
T^\alpha_a(x)=a\,\alpha(x)=L_a\circ\alpha=\alpha\circ L_{\alpha(a)} ,
$$
the elementary signed operator out of which the signed sandwich is built. This article treats it: the two readings of the operator, its products, its invertibility and its image, its adjoint with respect to the form of the category, and the conditions for it to be self-adjoint, an isometry or unitary. The adjoint is the point at which the algebra of random variables parts company with the algebra of arithmetic functions. There the form of the category is the coefficient form, the transpose of a left multiplication is not a left multiplication, and the adjoint of $L_a\alpha$ is the transposed multiplication composed with $\alpha$. Here the form is the expectation form $\langle x,y\rangle=\varphi(xy^*)$, it is invariant under the conjugation, the adjoint of a left multiplication is exactly the left multiplication by the conjugate, $L_a^*=L_{a^*}$, and the adjoint of the signed left multiplication is again a signed left multiplication,
$$
\bigl(T^\alpha_a\bigr)^*=T^\alpha_{\delta(a)},\qquad \delta=\sigma\alpha=\alpha\sigma .
$$
The involution on the elements and the adjoint on the operators therefore agree up to the twisted involution $\delta$; the multiplication is a $*$-representation, and the signed operator carries the twist.

The conventions are those of *The Signed Sandwich on the Algebra of Random Variables*, earlier in this category: $\mathcal{A}=L^\infty(\Omega,\mathcal F,\mathbb P)$ with the pointwise product, the conjugation $\sigma(x)=\bar x$, the state $\varphi(x)=\mathbb E[x]$, the form $\langle x,y\rangle=\varphi(xy^*)$, the grade involution $\alpha$, the grading $\mathcal{A}=\mathcal{A}_{\bar0}\oplus\mathcal{A}_{\bar1}$, and the twisted involution $\delta=\sigma\alpha$. The reflections are the preceding article of this category, the graded action is the next, and the adjoint of the unsigned left multiplication, with the proof that $L_a^*=L_{a^*}$, is *The Adjoint of the Left Multiplication on the Algebra of Random Variables*, later in this category. The noncommutative signed left multiplication, whose adjoint is by $\delta$ as well but for a different reason, is *The Signed Left Multiplication on a Ring*, in Part I. No physics is invoked.

Throughout, $\mathcal{A}$ is the algebra of random variables, $\mathcal{H}=L^2(\Omega,\mathbb P)$ with the form $\langle x,y\rangle=\varphi(xy^*)$ is the Hilbert space of the category, and $\delta=\sigma\alpha$. The signed sandwich is $S^\alpha_{a,b}(x)=a\,\alpha(x)\,b$, which collapses to $T^\alpha_{ab}$ on this commutative algebra.

## The Operator and its Products

### Definition and the two readings

**Definition.** For $a\in\mathcal{A}$ the **signed left multiplication** is the operator
$$
T^\alpha_a:\mathcal{A}\to\mathcal{A},\qquad T^\alpha_a(x)=a\,\alpha(x).
$$
It is the signed sandwich with $b=1$, $T^\alpha_a=S^\alpha_{a,1}$, and it satisfies the two readings
$$
T^\alpha_a=L_a\circ\alpha=\alpha\circ L_{\alpha(a)},
$$
the second because $L_a\alpha=\alpha L_{\alpha(a)}$ for an involutive automorphism $\alpha$.

**Proposition (the signed sandwich re-read).** On the commutative algebra the signed sandwich is the signed left multiplication of the product,
$$
S^\alpha_{a,b}=T^\alpha_{ab},
$$
and the signed left multiplication is that operator in which the grade involution is inserted between the multiplication by $a$ and the identity.

*Proof.* The collapse of the preceding articles gives $S^\alpha_{a,b}=L_{ab}\alpha=T^\alpha_{ab}$.

### The products

**Theorem (the product law).** For all $a,b\in\mathcal{A}$,
$$
T^\alpha_a\,T^\alpha_b=L_{a\,\alpha(b)},
$$
so the product of two signed left multiplications is an unsigned left multiplication, and it is again a signed left multiplication only in the degenerate case: either $\alpha=\mathrm{id}$, or the multiplier $a\alpha(b)$ vanishes.

*Proof.* $T^\alpha_aT^\alpha_b(x)=a\,\alpha(b\,\alpha(x))=a\,\alpha(b)\,\alpha^2(x)=a\,\alpha(b)\,x$, using the multiplicativity of $\alpha$; hence the product is $L_{a\alpha(b)}$. If $L_c=T^\alpha_{c'}$ for some $c'$, then evaluating at $x=1$ gives $c=c'$ and then $cx=c\,\alpha(x)$ for all $x$, which forces $\alpha=\mathrm{id}$ wherever $c\ne0$.

**Corollary (commutativity of the family).** For a pair $a,b$ the two signed left multiplications commute, $T^\alpha_aT^\alpha_b=T^\alpha_bT^\alpha_a$, exactly when $a\,\alpha(b)=b\,\alpha(a)$. The whole family is commutative when $\alpha=\mathrm{id}$, where it is the family of the unsigned left multiplications, and also when the algebra is reduced to the constants; for a nontrivial $\alpha$ over a nontrivial algebra the family is not commutative.

*Proof.* The two products are $L_{a\alpha(b)}$ and $L_{b\alpha(a)}$, equal exactly when the multipliers are equal. If $\alpha=\mathrm{id}$ the equality is the commutativity of the algebra. For a nontrivial $\alpha$ choose $b$ even and $a$ odd with $ab\ne0$; then $a\alpha(b)=ab$ while $b\alpha(a)=-ba=-ab$, and the two differ.

### Invertibility and the image

**Theorem (injectivity and image).** $T^\alpha_a$ is injective exactly when $a\ne0$ in $\mathcal{A}$, and its image is the principal ideal
$$
T^\alpha_a(\mathcal{A})=a\,\mathcal{A} .
$$

*Proof.* The operator is $L_a\alpha$ with $\alpha$ bijective on $\mathcal{A}$, so it is injective exactly when $L_a$ is, that is exactly when $a\ne0$; a multiplication by a nonzero function of $\mathcal{A}$ vanishes only on the null set where the function is zero. The image is $L_a(\alpha(\mathcal{A}))=L_a(\mathcal{A})=a\mathcal{A}$.

**Theorem (invertibility).** $T^\alpha_a$ is invertible on $\mathcal{A}$ exactly when $a$ is a unit, and then
$$
\bigl(T^\alpha_a\bigr)^{-1}=T^\alpha_{\alpha(a)^{-1}}=\alpha\circ L_{a^{-1}} .
$$

*Proof.* The operator is the product of the bijection $\alpha$ and the multiplication $L_a$; the product is invertible exactly when $L_a$ is, which holds exactly when $a$ is a unit of $\mathcal{A}$. The inverse is $\alpha^{-1}L_a^{-1}=\alpha L_{a^{-1}}=L_{\alpha(a^{-1})}\alpha=T^\alpha_{\alpha(a^{-1})}$, and $\alpha(a^{-1})=\alpha(a)^{-1}$.

## The Adjoint

### The signed adjoint

**Theorem (the signed adjoint).** With respect to the form of the category,
$$
\bigl(T^\alpha_a\bigr)^*=T^\alpha_{\delta(a)}=\alpha\circ L_{a^*},\qquad \delta=\sigma\alpha=\alpha\sigma .
$$
Equivalently $\bigl(T^\alpha_a\bigr)^*(y)=\alpha(a^*y)$.

*Proof.* The operator is $L_a\alpha$, and the adjoint of a product is the product of the adjoints in reverse order,
$$
\bigl(L_a\alpha\bigr)^*=\alpha^*L_a^*=\alpha L_{a^*},
$$
using $\alpha^*=\alpha$ and $L_a^*=L_{a^*}$. Since $\alpha L_{a^*}=L_{\alpha(a^*)}\alpha$ and $\delta(a)=\alpha(a^*)$, the result is $T^\alpha_{\delta(a)}$.

**Corollary (comparison with the arithmetic case).** Over the algebra of arithmetic functions under the coefficient form the adjoint of $T_a$ is the transposed multiplication $\Theta_a$ composed with $\alpha$, and it is not a signed left multiplication unless $\alpha(a)$ is a unit. Here the adjoint is a signed left multiplication for every $a$, and the discrepancy between the two cases is exactly the invariance of the expectation form, which returns $L_{a^*}$ for the adjoint of $L_a$ instead of the transpose. The noncommutative signed left multiplication has the same adjoint $T^\alpha_{\delta(a)}$, because there the transpose is replaced by the right multiplication and the composite $\delta$ performs the reversal; the commutative case reaches the same formula by the invariance of the form alone.

### Self-adjointness, isometry and unitarity

**Theorem.** For $a\in\mathcal{A}$ the signed left multiplication satisfies
$$
T^\alpha_a\ \text{is self-adjoint}\iff a=\delta(a)\iff\alpha(a)=a^* ,
$$
$$
T^\alpha_a\ \text{is an isometry}\iff|a|=1,\qquad T^\alpha_a\ \text{is unitary}\iff|a|=1 ,
$$
and the unitary signed left multiplications are parametrised by the unimodular random variables.

*Proof.* Self-adjointness is $T^\alpha_a=T^\alpha_{\delta(a)}$, and since $T^\alpha_c=L_c\alpha$ the equality is $a=\delta(a)$, that is $\alpha(a)=a^*$. For the isometry, $\bigl(T^\alpha_a\bigr)^*T^\alpha_a=T^\alpha_{\delta(a)}T^\alpha_a=L_{\delta(a)\alpha(a)}=L_{\alpha(a^*)\alpha(a)}=L_{\alpha(a^*a)}=L_{|a|^2}$, the identity exactly when $|a|=1$; the other order gives $L_{|a|^2}$ as well, so the isometric and the unitary members coincide and are the unimodular ones.

**Corollary (the self-adjoint unitary members).** The signed left multiplications that are self-adjoint and unitary are exactly the $T^\alpha_a$ with $a$ unimodular and $\alpha$-Hermitian, $\alpha(a)=a^*$; among them are the constant phases $a=z$ with $|z|=1$ and $\alpha(z)=z$.

*Proof.* The two conditions are those of the theorem, and the constants satisfy both.

## Worked Examples

**Example (the swap on two atoms).** Let $\Omega=\{\omega_-,\omega_+\}$ with the uniform probability and $\alpha(x_-,x_+)=(x_+,x_-)$. The signed left multiplication by $a=(a_-,a_+)$ is $T^\alpha_a(x_-,x_+)=a\,\alpha(x)=(a_-x_+,a_+x_-)$; it is self-adjoint exactly when $a_-=a_+$, that is when $a$ is even, and unitary exactly when $|a_\pm|=1$. The self-adjoint unitary members are $a=(z,z)$ with $|z|=1$, a circle.

**Example (the circle reflection).** Let $\Omega=\mathbb R/\mathbb Z$ with the Lebesgue measure, $\alpha(x)(\theta)=x(-\theta)$. For $a(\theta)=e^{2\pi i\theta}$ one has $\alpha(a)(\theta)=e^{-2\pi i\theta}=a(\theta)^*$, so $a$ is $\alpha$-Hermitian and $T^\alpha_a$ is self-adjoint and unitary; it is the operator $x\mapsto e^{2\pi i\theta}x(-\theta)$, an involution of the circle.

**Example (the trivial grading).** For $\alpha=\mathrm{id}$ one has $T^\alpha_a=L_a$, the adjoint is $L_{a^*}$, self-adjointness is $a$ real, and unitarity is $|a|=1$; this is the boundary at which the signed left multiplication is the unsigned one.

**Example (a non-invertible case).** For $a$ vanishing on a set of positive probability, $T^\alpha_a$ is injective but not invertible, its image is the proper ideal $a\mathcal{A}$, and it is neither unitary nor an isometry. A non-unitary isometry does not occur here: the isometry condition is $|a|=1$, and a unimodular $a$ is a unit with $a^{-1}=a^*$, so every isometric signed left multiplication is unitary.

## Failure of the Degenerate Cases

The signed left multiplication degenerates in four configurations. First, the products close into unsigned left multiplications, so the family of signed left multiplications is not a subalgebra of the operators; the products stay signed only in the degenerate case $\alpha=\mathrm{id}$. Second, the family is commutative only when the twist is trivial, so the signed left multiplications do not form the commutative algebra that the unsigned ones do. Third, the invertibility coincides with the invertibility of the multiplier, and the image is always a principal ideal of the commutative algebra, so the image is never dense unless the multiplier is a unit; there is no Fredholm theory here, in contrast with the shift. Fourth, the isometric and the unitary members coincide, since a multiplication by a unimodular function is a unitary, and the notion of a non-unitary isometry, which exists for the shift operator of *The Shift Operator of a Process*, earlier in this category, has no example among the signed left multiplications; the difference is the invertibility of the multiplier.

## Summary

The signed left multiplication $T^\alpha_a(x)=a\,\alpha(x)$ is the product $L_a\alpha=\alpha L_{\alpha(a)}$, it is the signed sandwich with the second factor one, and the signed sandwich itself is $T^\alpha_{ab}$ on the commutative algebra. Its products are the unsigned left multiplications $T^\alpha_aT^\alpha_b=L_{a\alpha(b)}$, it is injective exactly when $a\ne0$ and invertible exactly when $a$ is a unit with inverse $T^\alpha_{\alpha(a)^{-1}}$, and its image is the principal ideal $a\mathcal{A}$. Its adjoint with respect to the expectation form is $T^\alpha_{\delta(a)}=\alpha L_{a^*}$ with $\delta=\sigma\alpha$, the same formula as in the noncommutative case but obtained here from the invariance of the form; it is self-adjoint exactly when $a=\delta(a)$, that is when $\alpha(a)=a^*$, and it is an isometry exactly when it is unitary, exactly when $|a|=1$. The unitary members are parametrised by the unimodular random variables, and the self-adjoint unitary ones by the unimodular $\alpha$-Hermitian elements. The conventions are those of *The Signed Sandwich on the Algebra of Random Variables*; the unsigned adjoint is *The Adjoint of the Left Multiplication on the Algebra of Random Variables*, later in this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T^\alpha_a(x)=a\,\alpha(x)$ | the signed left multiplication |
| $T^\alpha_a=L_a\alpha=\alpha L_{\alpha(a)}$ | its two readings |
| $S^\alpha_{a,b}=T^\alpha_{ab}$ | the signed sandwich as a signed left multiplication |
| $T^\alpha_aT^\alpha_b=L_{a\alpha(b)}$ | the product law |
| $a\mathcal{A}$ | the image, a principal ideal |
| $T^\alpha_{\alpha(a)^{-1}}$ | the inverse of an invertible one |
| $\bigl(T^\alpha_a\bigr)^*=T^\alpha_{\delta(a)}$ | the signed adjoint |
| $\delta=\sigma\alpha$ | the twisted involution |
| $a=\delta(a)$, $|a|=1$ | self-adjointness, isometry and unitarity |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Vol. I (Academic Press, 1983), for the multiplication operators and the $*$-representations of a commutative involutive algebra.
- Paul Halmos, *A Hilbert Space Problem Book* (Springer, 1982), for the isometries, the unitaries and the multiplication operators.
- John B. Conway, *A Course in Functional Analysis* (Springer, 2nd edition, 1990), for the multiplication operators on $L^2$ and their spectra.
- Jacques Dixmier, *C*-Algebras* (North-Holland, 1977), for the representations, the adjoints and the twisted involutions.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the twisted involutions of an algebra with involution.
