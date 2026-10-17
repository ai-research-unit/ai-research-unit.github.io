# __Two-Sided Operators on the Quaternion Algebra__

## Introduction

The two-sided operators are the products of a left and a right multiplication, $T_{\tilde q_3,\tilde q_4}=L_{\tilde q_3}R_{\tilde q_4}$, $\tilde q\mapsto\tilde q_3\tilde q\tilde q_4$. They are the elementary tensors of the enveloping algebra, and they carry the whole operator calculus of the block: a composition law with the parameters reversed in the second place, a transpose that swaps the two parameters, a criterion for an operator of the family to preserve the plain form, and a criterion for it to be multiplicative. Both criteria are stated with the algebra product alone; no norm and no form is invoked to state them. The operators themselves are *One-Sided Operators on the Quaternion Algebra*, below this article in this category; the enveloping algebra and the operator basis are *The Enveloping Operator Algebra of the Quaternion Algebra and the Bi-module Structure*, above this article in this category; the transpose and the matrix formula are *Association and the Transpose on the Quaternion Algebra*, above this article in this category.

## The Family

**Definition.** For $\tilde q_3,\tilde q_4\in\mathbb{H}$ the **two-sided operator** is $T_{\tilde q_3,\tilde q_4}=L_{\tilde q_3}R_{\tilde q_4}$, the map $\tilde q\mapsto\tilde q_3\tilde q\tilde q_4$. The family is $\mathcal T=\{T_{\tilde q_3,\tilde q_4}\}=\{L_{\tilde q_3}R_{\tilde q_4}\}$.

**Proposition.** $\mathcal T$ is a linear subspace of $\operatorname{End}_\mathbb{R}(\mathbb{H})$ of dimension $16$, namely the whole of it.

*Proof.* The map $(\tilde q_3,\tilde q_4)\mapsto T_{\tilde q_3,\tilde q_4}$ is bilinear and its image is the span of the sixteen sandwiches $e_n[\,]e_m$; the enveloping algebra is identified with the endomorphisms in *The Enveloping Operator Algebra of the Quaternion Algebra and the Bi-module Structure*, above this article in this category, and has dimension $16$, equal to the dimension of the endomorphisms, so the family is everything.

**Corollary.** Every real-linear operator of $\mathbb{H}$ is a two-sided operator, and the four-dimensional space $\mathbb{H}$ is simple over the algebra $\mathcal T$.

*Proof.* The proposition and the identification.

## Composition

**Theorem (composition law).** $T_{\tilde q_3,\tilde q_4}T_{\tilde q_5,\tilde d}=T_{\tilde q_3\tilde q_5,\tilde d\tilde q_4}$.

*Proof.* Apply the left side to $\tilde q$: $\tilde q_3(\tilde q_5\tilde q\tilde d)\tilde q_4=(\tilde q_3\tilde q_5)\tilde q(\tilde d\tilde q_4)$, which is the right side. The second parameter is reversed because the second factor is read through the opposite algebra.

**Proposition (when two sandwiches agree).** The sandwich $L_{\tilde q_3}R_{\tilde q_4}$ is zero exactly when $\tilde q_3=0$ or $\tilde q_4=0$. For nonzero parameter pairs, $L_{\tilde q_3}R_{\tilde q_4}=L_{\tilde q_5}R_{\tilde d}$ exactly when $(\tilde q_5,\tilde d)=(\lambda\tilde q_3,\lambda^{-1}\tilde q_4)$ for a real $\lambda\neq0$.

*Proof.* At $\tilde q=e_t$ the equality $L_{\tilde q_3}R_{\tilde q_4}=0$ gives $\tilde q_3\tilde q_4=0$, so one factor vanishes. Assume all four parameters nonzero and $\tilde q_3\tilde q\tilde q_4=\tilde q_5\tilde q\tilde d$ for all $\tilde q$; left multiplying by $\tilde q_3^{-1}$ and writing $\gamma=\tilde q_3^{-1}\tilde q_5$ gives $\tilde q\tilde q_4=\gamma\tilde q\tilde d$, so $\tilde q_4=\gamma\tilde d$ at $\tilde q=e_t$ and $(\tilde q\gamma-\gamma\tilde q)\tilde d=0$ for all $\tilde q$, whence $\gamma$ is central, that is a real $\lambda\neq0$; then $\tilde q_5=\lambda\tilde q_3$ and $\tilde d=\lambda^{-1}\tilde q_4$. Conversely the central scalar gives $L_{\lambda\tilde q_3}R_{\lambda^{-1}\tilde q_4}=L_{\tilde q_3}R_{\tilde q_4}$.

**Corollary (the materialised semigroup).** $\mathcal T$ is a monoid under composition, with identity $T_{e_t,e_t}=L_{e_t}R_{e_t}=\mathrm{id}$; the map $(\tilde q_3,\tilde q_4)\mapsto T_{\tilde q_3,\tilde q_4}$ is a surjective homomorphism of monoids from the product $\mathbb{H}\times\mathbb{H}^{\mathrm{opp}}$, and its kernel is the one-parameter group $\{(\lambda,\lambda^{-1}):\lambda\in\mathbb{R}^{\times}\}$.

*Proof.* The law is associative, the identity is as displayed, and $(\tilde q_3,\tilde q_4)\mapsto T_{\tilde q_3,\tilde q_4}$ is multiplicative by the law. The map is **not** injective: $T_{\lambda\tilde q_3,\lambda^{-1}\tilde q_4}=T_{\tilde q_3,\tilde q_4}$ for every real $\lambda\neq0$, because the real scalar is central. The kernel is read from the agreement criterion at $(\tilde q_5,\tilde d)=(e_t,e_t)$, namely $\tilde q_3=\lambda e_t$ and $\tilde q_4=\lambda^{-1}e_t$, which is the displayed group; so $\mathcal T$ is a quotient of $\mathbb{H}\times\mathbb{H}^{\mathrm{opp}}$ and not the product itself.

**Corollary (the units).** $T_{\tilde q_3,\tilde q_4}$ is invertible exactly when $\tilde q_3\neq0$ and $\tilde q_4\neq0$, with inverse $T_{\tilde q_3^{-1},\tilde q_4^{-1}}$.

*Proof.* In the product monoid an element $(\tilde q_3,\tilde q_4)$ is invertible exactly when both factors are, and the inverse is $(\tilde q_3^{-1},\tilde q_4^{-1})$; in the operator monoid the inverse is $T_{\tilde q_3^{-1},\tilde q_4^{-1}}$.

## The Adjoint that Swaps the Parameters

**Theorem.** With respect to the plain form $\langle\tilde q_1,\tilde q_2\rangle=\mathrm{Sc}(\tilde q_1\tilde q_2)$ the transpose of a two-sided operator swaps the parameters:

$$
T_{\tilde q_3,\tilde q_4}^{\sim}=T_{\tilde q_4,\tilde q_3}=L_{\tilde q_4}R_{\tilde q_3}.
$$

*Proof.* The transpose is an anti-automorphism, so $T_{\tilde q_3,\tilde q_4}^{\sim}=(L_{\tilde q_3}R_{\tilde q_4})^{\sim}=R_{\tilde q_4}^{\sim}L_{\tilde q_3}^{\sim}=L_{\tilde q_4}R_{\tilde q_3}$, using $L_{\tilde q_3}^{\sim}=R_{\tilde q_3}$ and $R_{\tilde q_4}^{\sim}=L_{\tilde q_4}$ from *Association and the Transpose on the Quaternion Algebra*, above this article in this category.

**Corollary.** $T_{\tilde q_3,\tilde q_4}$ is self-transpose exactly when $\tilde q_4\in\mathbb{R}\tilde q_3$ or $\tilde q_3\in\mathbb{R}\tilde q_4$.

*Proof.* $T_{\tilde q_3,\tilde q_4}=T_{\tilde q_4,\tilde q_3}$ exactly when $\tilde q_3\tilde q\tilde q_4=\tilde q_4\tilde q\tilde q_3$ for all $\tilde q$, which is the sandwich criterion of *Association and the Transpose on the Quaternion Algebra*, above this article in this category.

## The Criterion of Form Preservation

**Theorem.** $T_{\tilde q_3,\tilde q_4}$ preserves the plain form, $\langle T\tilde q_1,T\tilde q_2\rangle=\langle\tilde q_1,\tilde q_2\rangle$ for all $\tilde q_1,\tilde q_2$, exactly when $\tilde q_4\tilde q_3=\pm e_t$.

*Proof.* For $T=T_{\tilde q_3,\tilde q_4}$ invertible, preservation of the form is equivalent to $T^{\sim}T=\mathrm{id}$; if $\tilde q_3=0$ or $\tilde q_4=0$ then $T=0$, which preserves the form only if the form were zero. Now by the composition law $T^{\sim}T=T_{\tilde q_4,\tilde q_3}T_{\tilde q_3,\tilde q_4}=T_{\tilde q_4\tilde q_3,\tilde q_4\tilde q_3}$, and $T_{\tilde q_5,\tilde d}=\mathrm{id}$ exactly when $\tilde q_5\tilde q\tilde d=\tilde q$ for all $\tilde q$; at $\tilde q=e_t$ this gives $\tilde q_5\tilde d=e_t$, so $\tilde d=\tilde q_5^{-1}$, and substituting gives $\tilde q_5\tilde q\tilde q_5^{-1}=\tilde q$ for all $\tilde q$, that is $\tilde q_5$ central. Hence $\tilde q_5=\tilde q_4\tilde q_3$ is central with $\tilde q_5^2=e_t$; a central element with $\tilde q_5^2=e_t$ is $\pm e_t$, so $\tilde q_4\tilde q_3=\pm e_t$. Conversely $\tilde q_4\tilde q_3=\pm e_t$ makes $\tilde q_4=\pm\tilde q_3^{-1}$, and then $T(\tilde q)=\tilde q_3\tilde q(\pm\tilde q_3^{-1})=\pm\tilde q_3\tilde q\tilde q_3^{-1}$, which preserves the form.

**Corollary.** The form-preserving two-sided operators are the operators $\pm\operatorname{Ad}_{\tilde q_3}$, where $\operatorname{Ad}_{\tilde q_3}(\tilde q)=\tilde q_3\tilde q\tilde q_3^{-1}$ is the inner automorphism by a unit; on the parameter the criterion reads $\tilde q_4=\pm\tilde q_3^{-1}$.

**Corollary.** The sign $+$ operators form the group $\operatorname{Ad}(\mathbb{H}^{\times})\cong\mathbb{H}^{\times}/\mathbb{R}^{\times}$ of inner automorphisms, and the sign $-$ operators are the negatives of these; the transpose on the form-preserving family is the inverse, $\operatorname{Ad}_{\tilde q_3}^{\sim}=\operatorname{Ad}_{\tilde q_3}^{-1}=\operatorname{Ad}_{\tilde q_3^{-1}}$.

*Proof.* The composition law gives $\operatorname{Ad}_{\tilde q_3}\operatorname{Ad}_{\tilde q_5}=\operatorname{Ad}_{\tilde q_3\tilde q_5}$ and $\operatorname{Ad}_{\tilde q_3}=\mathrm{id}$ exactly for central $\tilde q_3$, by the centre theorem; the transpose of $T_{\tilde q_3,\tilde q_3^{-1}}$ is $T_{\tilde q_3^{-1},\tilde q_3}=\operatorname{Ad}_{\tilde q_3^{-1}}$.

## The Criterion of Multiplicativity

**Theorem.** A non-zero two-sided operator $T_{\tilde q_3,\tilde q_4}$ is multiplicative, $T(\tilde q_1\tilde q_2)=T(\tilde q_1)T(\tilde q_2)$ for all $\tilde q_1,\tilde q_2$, exactly when $\tilde q_4=\tilde q_3^{-1}$; the non-zero multiplicative two-sided operators are the inner automorphisms $\operatorname{Ad}_{\tilde q_3}$. The zero operator, which occurs exactly for $\tilde q_3=0$ or $\tilde q_4=0$, is multiplicative as well, so it is the degenerate member of the family and the criterion is stated on the non-zero parameters.

*Proof.* The condition is $\tilde q_3\tilde q_1\tilde q_2\tilde q_4=\tilde q_3\tilde q_1\tilde q_4\tilde q_3\tilde q_2\tilde q_4$ for all $\tilde q_1,\tilde q_2$, that is, after cancelling a left $\tilde q_3$ and a right $\tilde q_4$ (legitimate when $\tilde q_3,\tilde q_4\neq0$), $\tilde q_2=\tilde q_4\tilde q_3\tilde q_2$ for all $\tilde q_2$, that is $\tilde q_4\tilde q_3=e_t$, the criterion $\tilde q_4=\tilde q_3^{-1}$. If $\tilde q_3=0$ or $\tilde q_4=0$ the operator is the zero map, which is multiplicative because both sides of the identity vanish; the criterion is therefore stated on the non-zero parameters. Then $T(\tilde q)=\tilde q_3\tilde q\tilde q_3^{-1}$, the inner automorphism.

**Corollary.** A non-zero two-sided operator is multiplicative exactly when it is form-preserving with the positive sign; the non-zero multiplicative ones are a group under composition, and they are the algebra automorphisms of $\mathbb{H}$ that lie in the family; the zero operator is multiplicative but is not form-preserving.

*Proof.* The two criteria; the group statement is the corollary above.

**Corollary (automorphisms are inner).** Every $\mathbb{R}$-algebra automorphism of $\mathbb{H}$ is a two-sided operator and is inner: $\operatorname{Aut}(\mathbb{H})=\operatorname{Ad}(\mathbb{H}^{\times})\cong\mathbb{H}^{\times}/\mathbb{R}^{\times}$.

*Proof.* An automorphism is a real-linear operator, hence of the family; it is multiplicative, hence of the form $\operatorname{Ad}_{\tilde q_3}$; conversely each $\operatorname{Ad}_{\tilde q_3}$ is an automorphism. Every automorphism of a central simple algebra is inner by the Skolem–Noether theorem, quoted as standard, and the two descriptions agree.

## Summary

The two-sided operators $T_{\tilde q_3,\tilde q_4}(\tilde q)=\tilde q_3\tilde q\tilde q_4$ form the whole $16$-dimensional algebra of real-linear operators of $\mathbb{H}$, with the composition law $T_{\tilde q_3,\tilde q_4}T_{\tilde q_5,\tilde d}=T_{\tilde q_3\tilde q_5,\tilde d\tilde q_4}$, the identity $T_{e_t,e_t}$, and invertibility exactly when both parameters are non-zero. The transpose with respect to the plain form swaps the parameters, $T_{\tilde q_3,\tilde q_4}^{\sim}=T_{\tilde q_4,\tilde q_3}$, and the operator is self-transpose exactly when the parameters are real multiples of one another. It preserves the form exactly when $\tilde q_4\tilde q_3=\pm e_t$, that is when it is $\pm$ an inner automorphism, and for non-zero parameters it is multiplicative exactly when $\tilde q_4=\tilde q_3^{-1}$, that is when it is an inner automorphism, the zero operator being the only other multiplicative member; the form-preserving family is the group of inner automorphisms together with its negative, and every algebra automorphism of $\mathbb{H}$ is inner. Neither criterion needs the norm to be stated.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_{\tilde q_3,\tilde q_4}=L_{\tilde q_3}R_{\tilde q_4}$ | Two-sided operator, $\tilde q\mapsto\tilde q_3\tilde q\tilde q_4$ |
| $\mathcal T$ | The family of two-sided operators, $=\operatorname{End}_\mathbb{R}(\mathbb{H})$ |
| $T_{\tilde q_3,\tilde q_4}^{\sim}$ | Transpose with respect to $\mathrm B$ |
| $\operatorname{Ad}_{\tilde q_3}$ | Inner automorphism $\tilde q\mapsto\tilde q_3\tilde q\tilde q_3^{-1}$ |
| $\langle\tilde q_1,\tilde q_2\rangle=\mathrm{Sc}(\tilde q_1\tilde q_2)$ | The plain form |

## Further Reading

- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the sandwich operators and their composition.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the inner automorphisms of a central simple algebra and the Skolem–Noether theorem.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the unit group of a division ring and its centre.
