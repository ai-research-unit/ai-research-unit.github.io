
# __The Adjoint of the Left Multiplication on the Algebra of Random Variables__

## Introduction

The left multiplication of the algebra of random variables is the operator $L_af=af$, acting on the Hilbert space $\mathcal{H}=L^2(\Omega,\mathbb P)$ with the form of the category,
$$
\langle f,g\rangle=\varphi(fg^*)=\mathbb E\bigl[f\bar g\bigr].
$$
Its **adjoint** is the cleanest statement in the category, and it is a point of contrast with the whole of the arithmetic theory: here
$$
L_a^*=L_{a^*} ,
$$
the adjoint of the left multiplication is the left multiplication by the conjugate, **always** and without exception. In the algebra of arithmetic functions under the coefficient form the adjoint of $L_a$ is the transposed multiplication $\Theta_a$, and $L_a^*=L_{a^*}$ only for the scalar multiples of the identity; here the two coincide for every $a$. The reason is the invariance of the form, which is the traciality of the state in the commutative algebra: the expectation satisfies $\varphi(fg)=\varphi(gf)$ for all $f,g$, and the identity $\varphi(afg^*)=\varphi(f(\bar ag)^*)$ is then a direct computation. This article proves the formula, identifies the adjoint with the left multiplication by the conjugate, derives the self-adjointness, the unitarity and the spectrum, and states the comparison between the involution on the elements and the adjoint on the operators: the representation $\pi(a)=L_a$ is a $*$-representation, and the agreement is proved, never assumed.

The conventions are those of the category: the algebra of random variables $\mathcal{A}=L^\infty(\Omega,\mathcal F,\mathbb P)$ with the conjugation $a^*=\bar a$, the state $\varphi(a)=\mathbb E[a]$ and the form $\langle f,g\rangle=\varphi(fg^*)$ of *The Involution on the Algebra of Random Variables*, earlier in this category. The adjoint of a left multiplication on a general Hilbert algebra, where the same formula holds under the Hermitian hypothesis, is *The Adjoint of the Left Multiplication on a Hilbert Algebra*, written, and the general adjoint on an algebra is *The Adjoint of the Left Multiplication on an Algebra*, written; the arithmetic counterpart, with the transpose in place of the multiplication, is *The Adjoint of the Left Multiplication on the Algebra of Arithmetic Functions*, written. The signed left multiplication and its adjoint are *The Signed Left Multiplication on the Algebra of Random Variables*, earlier in this category, and *The Signed Adjoint of the Left Multiplication on the Algebra of Random Variables*, later in this category; the refinement of the spectrum by a reversing symmetry is *Reversible Operators and Self-Adjointness*, later in this category; the operator-algebra involution is *The Involution on the Operator Algebra of a Process*, earlier in this category. No physics is invoked.

Throughout, $\mathcal{A}=L^\infty(\Omega,\mathcal F,\mathbb P)$ is the algebra of random variables, $\mathcal{H}=L^2(\Omega,\mathcal F,\mathbb P)$ is the Hilbert space with the form $\langle f,g\rangle=\varphi(fg^*)$, and $L_a$ is the left multiplication on $\mathcal{H}$, $L_af=af$, a bounded operator with $\|L_a\|=\|a\|_\infty$. The right multiplication is $R_af=fa$, equal to $L_a$ because the algebra is commutative, and the involution on the elements is $a^*=\bar a$.

## The Adjoint of the Left Multiplication

### Definition and formula

**Definition.** The **adjoint** $L_a^*$ is the bounded operator on $\mathcal{H}$ characterised by
$$
\langle L_af,g\rangle=\langle f,L_a^*g\rangle\qquad\text{for all }f,g\in\mathcal{H}.
$$

**Theorem (the adjoint formula).** For every $a\in\mathcal{A}$,
$$
L_a^*=L_{a^*}=L_{\bar a},
$$
and the left multiplications therefore form a $*$-algebra of operators under the adjoint.

*Proof.* Compute
$$
\langle af,g\rangle=\varphi\bigl(afg^*\bigr)=\varphi\bigl(f\bar a g^*\bigr)=\varphi\bigl(f(\bar ag)^*\bigr)=\langle f,\bar ag\rangle ,
$$
using the commutativity of the product in the step $afg^*=f\bar ag^*$ and the identity $(a^*g)^*=g^*a$. Comparing with the definition of the adjoint gives $L_a^*=L_{\bar a}=L_{a^*}$.

**Theorem (the tracial invariance).** The agreement $L_a^*=L_{a^*}$ is equivalent to the invariance of the form under the multiplication,
$$
\varphi(afg^*)=\varphi(f\bar ag^*)\qquad\text{for all }f,g\in\mathcal{H},
$$
which holds because the state is tracial in the commutative algebra, $\varphi(uv)=\varphi(vu)$.

*Proof.* The identity of the two sides is the computation above read as the invariance; the traciality is the commutativity $\varphi(uv)=\mathbb E[uv]=\mathbb E[vu]=\varphi(vu)$, which holds for all bounded $u,v$. In the arithmetic case the augmentation is not tracial and the form is not translation-invariant, which is why the adjoint is the transpose there.

### The comparison with the involution

**Theorem (the $*$-representation).** The map $\pi(a)=L_a$ is a $*$-representation of the algebra of random variables on $\mathcal{H}$:
$$
\pi(ab)=\pi(a)\pi(b),\qquad \pi(a^*)=\pi(a)^*,\qquad \pi(1)=I ,
$$
and on the elements it realises the involution exactly, $\pi(a^*)=L_{a^*}=L_a^*$.

*Proof.* The multiplicativity is $L_{ab}=L_aL_b$, the unit is the identity operator, and the involutivity is the formula above; the representation is faithful, since $L_a=0$ implies $a=0$, so the algebra of random variables is isomorphic to the algebra of the left multiplications as a $*$-algebra.

**Corollary (the comparison with the arithmetic case).** In the algebra of arithmetic functions under the coefficient form the adjoint of $L_a$ is the transposed multiplication $\Theta_a$, the identity $L_a^*=L_{a^*}$ holds only for the scalar multiples of the identity of the algebra, and the representation by the multiplications is not a $*$-representation. The difference is the product and the form: the pointwise product and the faithful tracial state here, the convolution and the non-tracial augmentation there.

*Proof.* The arithmetic statement is that of *The Adjoint of the Left Multiplication on the Algebra of Arithmetic Functions*, written; the comparison isolates the traciality as the cause of the agreement here.

## Self-Adjointness, Unitarity and Spectrum

**Theorem (the conditions).** For $a\in\mathcal{A}$,
$$
L_a\ \text{is self-adjoint}\iff a=a^*\iff a\text{ is real},\qquad L_a\ \text{is an isometry}\iff L_a\ \text{is unitary}\iff|a|=1 ,
$$
and every $L_a$ is normal, $L_aL_a^*=L_a^*L_a$, because the multiplications commute and the adjoint is the multiplication by the conjugate.

*Proof.* Self-adjointness is $L_a=L_{a^*}$, which by the injectivity of $\pi$ is $a=a^*$; the unitary condition is $L_a^*L_a=L_{a^*}L_a=L_{|a|^2}=I$, which is $|a|=1$, and a multiplication by a unimodular function is invertible with the inverse $L_{\bar a}$, so the isometries are exactly the unitaries; the normality is the commutation $L_{|a|^2}=L_{a^*}L_a=L_aL_{a^*}$.

**Theorem (the spectrum).** The spectrum of $L_a$ is the essential range of $a$,
$$
\operatorname{spec}(L_a)=\operatorname{ess\,range}(a)=\{\lambda:\mathbb P(|a-\lambda|<\varepsilon)>0\text{ for every }\varepsilon>0\},
$$
and the spectral measure of $L_a$ for a real $a$ is the distribution of the random variable $a$.

*Proof.* The multiplication operator $L_a$ is the multiplication by the function $a$ on $L^2$, and the spectrum of a multiplication operator is the essential range of the multiplier; the spectral measure is the projection onto the sets where $a$ takes its values, whose scalar measure is the law of $a$ by the spectral theorem of *The Involution on the Algebra of Random Variables*, earlier in this category.

**Corollary (the functional calculus).** For every bounded Borel $F$ on the spectrum,
$$
F(L_a)=L_{F(a)},
$$
the functional calculus of the multiplication, and for a real $a$ the operator $L_a$ is self-adjoint with the spectral decomposition $L_a=\int\lambda\,dE_{\mu_a}(\lambda)$, the scalar measure being the law of $a$.

*Proof.* The functional calculus of a multiplication operator sends $F$ to the multiplication by $F\circ a$; the self-adjointness and the spectral decomposition are the theorem applied to a real $a$.

## The Two Sides

**Theorem (the right multiplication).** Because the algebra is commutative, $R_a=L_a$; the adjoint of the right multiplication is the right multiplication by the conjugate, $R_a^*=R_{a^*}=L_{a^*}$, and the two-sided multiplication and its adjoint coincide with the one-sided ones. The left ideal $\mathcal{A}a$ is a right ideal, and the adjoint operation preserves the ideals.

*Proof.* The commutation $R_a=L_a$ is the commutativity; the adjoint is the formula above, and an ideal is preserved because $L_a^*=L_{a^*}$ maps into the same principal ideal.

## Worked Examples

**Example (the multiplications on the two-atom algebra).** For $\mathcal{A}\cong\mathbb{C}^2$ with the form $\langle f,g\rangle=\frac12(f_-\bar g_-+f_+\bar g_+)$ the left multiplication by $a=(a_-,a_+)$ is the diagonal operator with the entries $a_\pm$; its adjoint is the diagonal operator with the entries $\bar a_\pm$, the multiplication by $a^*$, and the operator is self-adjoint exactly when $a$ is real, unitary exactly when $|a_\pm|=1$.

**Example (the multiplication on the circle).** For the circle with the Lebesgue measure and $a(\theta)=e^{2\pi i\theta}$ the multiplication $L_a$ is unitary, $L_a^*=L_{\bar a}=L_a^{-1}$, and its spectrum is the unit circle; for $a(\theta)=\cos(2\pi\theta)$ the operator is self-adjoint with the spectrum $[-1,1]$ and the arcsine law as its spectral measure, the law of the random variable.

**Example (a non-invertible multiplication).** For $a$ vanishing on a set of positive measure the multiplication $L_a$ is injective but not invertible, its image is the proper ideal $a\mathcal{H}$, and it is neither an isometry nor unitary; the adjoint $L_{a^*}$ vanishes on the same set, and the range and the kernel are related by the orthogonality of the multiplication.

**Example (the comparison with the transpose).** In the algebra of arithmetic functions with $\varphi(f)=f(1)$ and the coefficient form, the left multiplication by $a$ has the adjoint $\Theta_a$ with $(\Theta_ag)(k)=\sum_{m\ge1}\overline{a(m)}g(mk)$; for $a\ne\gamma\varepsilon$ the operator $\Theta_a$ is not a left multiplication, so $L_a^*\ne L_{a^*}$, and the representation is not a $*$-representation. The example shows that the agreement here is a property of the form and not of the multiplication alone.

## Failure of the Degenerate Cases

The adjoint of the left multiplication degenerates in four configurations. First, the formula $L_a^*=L_{a^*}$ relies on the traciality of the state, and for a non-tracial state on a non-commutative algebra the adjoint of the left multiplication is the right multiplication by the conjugate up to the modular correction, not the left multiplication; the commutative algebra is the case where the modular correction is trivial. Second, the spectrum of $L_a$ is the essential range, and for a variable $a$ that is zero on a set of positive measure the spectrum contains the value $0$ and the operator is not invertible, with the kernel $L_a$ equal to the functions supported on the zero set. Third, the equality of the adjoint with the left multiplication by the conjugate holds for the form of the category; a different form on the same algebra, for instance the coefficient form of the arithmetic comparison, gives a different adjoint. Fourth, the functional calculus $F(L_a)=L_{F(a)}$ holds for the bounded Borel functions and fails for the unbounded ones without the domain conditions, as in the general spectral theorem.

## Summary

The adjoint of the left multiplication of the algebra of random variables with respect to the form $\langle f,g\rangle=\varphi(fg^*)$ is the left multiplication by the conjugate,
$$
L_a^*=L_{a^*},
$$
for every $a$, because the state is tracial in the commutative algebra and the form is invariant under the multiplication; the map $\pi(a)=L_a$ is therefore a faithful $*$-representation, $\pi(a^*)=\pi(a)^*$, and the involution on the elements and the adjoint on the operators coincide on the multiplications. The operator $L_a$ is self-adjoint exactly when $a$ is real, unitary exactly when $|a|=1$, normal for every $a$, and its spectrum is the essential range of the multiplier with the functional calculus $F(L_a)=L_{F(a)}$ and the law of a real $a$ as its spectral measure. In the arithmetic analogue under the coefficient form the adjoint is the transposed multiplication and the two structures differ, the commutativity and the traciality being exactly what is lost. The signed left multiplication and its adjoint are *The Signed Adjoint of the Left Multiplication on the Algebra of Random Variables*, later in this category, and the refinement of the spectrum by a reversing symmetry is *Reversible Operators and Self-Adjointness*, later in this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_af=af$ | the left multiplication |
| $\langle f,g\rangle=\varphi(fg^*)$ | the form of the category |
| $L_a^*=L_{a^*}=L_{\bar a}$ | the adjoint, a left multiplication |
| $\pi(a)=L_a$ | the $*$-representation by the multiplications |
| $\varphi(uv)=\varphi(vu)$ | the traciality of the state |
| $L_a$ self-adjoint $\iff a=a^*$ | self-adjointness |
| $L_a$ unitary $\iff|a|=1$ | unitarity and isometry |
| $\operatorname{spec}(L_a)=\operatorname{ess\,range}(a)$ | the spectrum |
| $F(L_a)=L_{F(a)}$ | the functional calculus |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Vol. I (Academic Press, 1983), for the multiplications, the $*$-representations and the spectral theorem.
- John B. Conway, *A Course in Functional Analysis* (Springer, 2nd edition, 1990), for the multiplication operators and their spectra.
- Sterling K. Berberian, *Lectures in Functional Analysis and Operator Theory* (Springer, 1974), for the multiplication operators, the essential range and the functional calculus.
- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for the tracial states, the modular theory and the Hilbert algebras.
