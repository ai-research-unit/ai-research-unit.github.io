# __Two-Sided Operators on the General Plain Algebra of Quaternions__

## Introduction

The two-sided operators are the products of a left and a right multiplication, $T_{\tilde a,\tilde b}=L_{\tilde a}R_{\tilde b}$, $\tilde q\mapsto\tilde a\tilde q\tilde b$. They are the elementary tensors of the enveloping algebra, and they carry the whole operator calculus of the block: a composition law with the parameters reversed in the second place, a transpose that swaps the two parameters, a criterion for an operator of the family to preserve the plain form, and a criterion for it to be multiplicative. Both criteria are stated with the algebra product alone; no norm and no form is invoked to state them. The operators themselves are *One-Sided Operators on the General Plain Algebra of Quaternions*, below this article in this category; the enveloping algebra and the operator basis are *The Enveloping Operator Algebra of the General Plain Algebra and the Bi-module Structure*, above this article in this category; the transpose and the matrix formula are *Association and the Transpose on the General Plain Algebra*, above this article in this category.

## The Family

**Definition.** For $\tilde a,\tilde b\in\mathbb{H}$ the **two-sided operator** is $T_{\tilde a,\tilde b}=L_{\tilde a}R_{\tilde b}$, the map $\tilde q\mapsto\tilde a\tilde q\tilde b$. The family is $\mathcal T=\{T_{\tilde a,\tilde b}\}=\{L_{\tilde a}R_{\tilde b}\}$.

**Proposition.** $\mathcal T$ is a linear subspace of $\operatorname{End}_\mathbb{R}(\mathbb{H})$ of dimension $16$, namely the whole of it.

*Proof.* The map $(\tilde a,\tilde b)\mapsto T_{\tilde a,\tilde b}$ is bilinear and its image is the span of the sixteen sandwiches $e_n[\,]e_m$; the enveloping algebra is identified with the endomorphisms in *The Enveloping Operator Algebra of the General Plain Algebra and the Bi-module Structure*, above this article in this category, and has dimension $16$, equal to the dimension of the endomorphisms, so the family is everything.

**Corollary.** Every real-linear operator of $\mathbb{H}$ is a two-sided operator, and the four-dimensional space $\mathbb{H}$ is simple over the algebra $\mathcal T$.

*Proof.* The proposition and the identification.

## Composition

**Theorem (composition law).** $T_{\tilde a,\tilde b}T_{\tilde c,\tilde d}=T_{\tilde a\tilde c,\tilde d\tilde b}$.

*Proof.* Apply the left side to $\tilde q$: $\tilde a(\tilde c\tilde q\tilde d)\tilde b=(\tilde a\tilde c)\tilde q(\tilde d\tilde b)$, which is the right side. The second parameter is reversed because the second factor is read through the opposite algebra.

**Proposition (when two sandwiches agree).** The sandwich $L_{\tilde a}R_{\tilde b}$ is zero exactly when $\tilde a=0$ or $\tilde b=0$. For nonzero parameter pairs, $L_{\tilde a}R_{\tilde b}=L_{\tilde c}R_{\tilde d}$ exactly when $(\tilde c,\tilde d)=(\lambda\tilde a,\lambda^{-1}\tilde b)$ for a real $\lambda\neq0$.

*Proof.* At $\tilde q=e_0$ the equality $L_{\tilde a}R_{\tilde b}=0$ gives $\tilde a\tilde b=0$, so one factor vanishes. Assume all four parameters nonzero and $\tilde a\tilde q\tilde b=\tilde c\tilde q\tilde d$ for all $\tilde q$; left multiplying by $\tilde a^{-1}$ and writing $\gamma=\tilde a^{-1}\tilde c$ gives $\tilde q\tilde b=\gamma\tilde q\tilde d$, so $\tilde b=\gamma\tilde d$ at $\tilde q=e_0$ and $(\tilde q\gamma-\gamma\tilde q)\tilde d=0$ for all $\tilde q$, whence $\gamma$ is central, that is a real $\lambda\neq0$; then $\tilde c=\lambda\tilde a$ and $\tilde d=\lambda^{-1}\tilde b$. Conversely the central scalar gives $L_{\lambda\tilde a}R_{\lambda^{-1}\tilde b}=L_{\tilde a}R_{\tilde b}$.

**Corollary (the materialised semigroup).** $\mathcal T$ is a monoid under composition, with identity $T_{e_0,e_0}=L_{e_0}R_{e_0}=\mathrm{id}$; the map $(\tilde a,\tilde b)\mapsto T_{\tilde a,\tilde b}$ is a surjective homomorphism of monoids from the product $\mathbb{H}\times\mathbb{H}^{\mathrm{op}}$, and its kernel is the one-parameter group $\{(\lambda,\lambda^{-1}):\lambda\in\mathbb{R}^{\times}\}$.

*Proof.* The law is associative, the identity is as displayed, and $(\tilde a,\tilde b)\mapsto T_{\tilde a,\tilde b}$ is multiplicative by the law. The map is **not** injective: $T_{\lambda\tilde a,\lambda^{-1}\tilde b}=T_{\tilde a,\tilde b}$ for every real $\lambda\neq0$, because the real scalar is central. The kernel is read from the agreement criterion at $(\tilde c,\tilde d)=(e_0,e_0)$, namely $\tilde a=\lambda e_0$ and $\tilde b=\lambda^{-1}e_0$, which is the displayed group; so $\mathcal T$ is a quotient of $\mathbb{H}\times\mathbb{H}^{\mathrm{op}}$ and not the product itself.

**Corollary (the units).** $T_{\tilde a,\tilde b}$ is invertible exactly when $\tilde a\neq0$ and $\tilde b\neq0$, with inverse $T_{\tilde a^{-1},\tilde b^{-1}}$.

*Proof.* In the product monoid an element $(\tilde a,\tilde b)$ is invertible exactly when both factors are, and the inverse is $(\tilde a^{-1},\tilde b^{-1})$; in the operator monoid the inverse is $T_{\tilde a^{-1},\tilde b^{-1}}$.

## The Adjoint that Swaps the Parameters

**Theorem.** With respect to the plain form $\mathrm B(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p\tilde q)$ the transpose of a two-sided operator swaps the parameters:

$$
T_{\tilde a,\tilde b}^{\sim}=T_{\tilde b,\tilde a}=L_{\tilde b}R_{\tilde a}.
$$

*Proof.* The transpose is an anti-automorphism, so $T_{\tilde a,\tilde b}^{\sim}=(L_{\tilde a}R_{\tilde b})^{\sim}=R_{\tilde b}^{\sim}L_{\tilde a}^{\sim}=L_{\tilde b}R_{\tilde a}$, using $L_{\tilde a}^{\sim}=R_{\tilde a}$ and $R_{\tilde b}^{\sim}=L_{\tilde b}$ from *Association and the Transpose on the General Plain Algebra*, above this article in this category.

**Corollary.** $T_{\tilde a,\tilde b}$ is self-transpose exactly when $\tilde b\in\mathbb{R}\tilde a$ or $\tilde a\in\mathbb{R}\tilde b$.

*Proof.* $T_{\tilde a,\tilde b}=T_{\tilde b,\tilde a}$ exactly when $\tilde a\tilde q\tilde b=\tilde b\tilde q\tilde a$ for all $\tilde q$, which is the sandwich criterion of *Association and the Transpose on the General Plain Algebra*, above this article in this category.

## The Criterion of Form Preservation

**Theorem.** $T_{\tilde a,\tilde b}$ preserves the plain form, $\mathrm B(T\tilde p,T\tilde q)=\mathrm B(\tilde p,\tilde q)$ for all $\tilde p,\tilde q$, exactly when $\tilde b\tilde a=\pm e_0$.

*Proof.* For $T=T_{\tilde a,\tilde b}$ invertible, preservation of the form is equivalent to $T^{\sim}T=\mathrm{id}$; if $\tilde a=0$ or $\tilde b=0$ then $T=0$, which preserves the form only if the form were zero. Now by the composition law $T^{\sim}T=T_{\tilde b,\tilde a}T_{\tilde a,\tilde b}=T_{\tilde b\tilde a,\tilde b\tilde a}$, and $T_{\tilde c,\tilde d}=\mathrm{id}$ exactly when $\tilde c\tilde q\tilde d=\tilde q$ for all $\tilde q$; at $\tilde q=e_0$ this gives $\tilde c\tilde d=e_0$, so $\tilde d=\tilde c^{-1}$, and substituting gives $\tilde c\tilde q\tilde c^{-1}=\tilde q$ for all $\tilde q$, that is $\tilde c$ central. Hence $\tilde c=\tilde b\tilde a$ is central with $\tilde c^2=e_0$; a central element with $\tilde c^2=e_0$ is $\pm e_0$, so $\tilde b\tilde a=\pm e_0$. Conversely $\tilde b\tilde a=\pm e_0$ makes $\tilde b=\pm\tilde a^{-1}$, and then $T(\tilde q)=\tilde a\tilde q(\pm\tilde a^{-1})=\pm\tilde a\tilde q\tilde a^{-1}$, which preserves the form.

**Corollary.** The form-preserving two-sided operators are the operators $\pm\operatorname{Ad}_{\tilde a}$, where $\operatorname{Ad}_{\tilde a}(\tilde q)=\tilde a\tilde q\tilde a^{-1}$ is the inner automorphism by a unit; on the parameter the criterion reads $\tilde b=\pm\tilde a^{-1}$.

**Corollary.** The sign $+$ operators form the group $\operatorname{Ad}(\mathbb{H}^{\times})\cong\mathbb{H}^{\times}/\mathbb{R}^{\times}$ of inner automorphisms, and the sign $-$ operators are the negatives of these; the transpose on the form-preserving family is the inverse, $\operatorname{Ad}_{\tilde a}^{\sim}=\operatorname{Ad}_{\tilde a}^{-1}=\operatorname{Ad}_{\tilde a^{-1}}$.

*Proof.* The composition law gives $\operatorname{Ad}_{\tilde a}\operatorname{Ad}_{\tilde c}=\operatorname{Ad}_{\tilde a\tilde c}$ and $\operatorname{Ad}_{\tilde a}=\mathrm{id}$ exactly for central $\tilde a$, by the centre theorem; the transpose of $T_{\tilde a,\tilde a^{-1}}$ is $T_{\tilde a^{-1},\tilde a}=\operatorname{Ad}_{\tilde a^{-1}}$.

## The Criterion of Multiplicativity

**Theorem.** A non-zero two-sided operator $T_{\tilde a,\tilde b}$ is multiplicative, $T(\tilde p\tilde q)=T(\tilde p)T(\tilde q)$ for all $\tilde p,\tilde q$, exactly when $\tilde b=\tilde a^{-1}$; the non-zero multiplicative two-sided operators are the inner automorphisms $\operatorname{Ad}_{\tilde a}$. The zero operator, which occurs exactly for $\tilde a=0$ or $\tilde b=0$, is multiplicative as well, so it is the degenerate member of the family and the criterion is stated on the non-zero parameters.

*Proof.* The condition is $\tilde a\tilde p\tilde q\tilde b=\tilde a\tilde p\tilde b\tilde a\tilde q\tilde b$ for all $\tilde p,\tilde q$, that is, after cancelling a left $\tilde a$ and a right $\tilde b$ (legitimate when $\tilde a,\tilde b\neq0$), $\tilde q=\tilde b\tilde a\tilde q$ for all $\tilde q$, that is $\tilde b\tilde a=e_0$, the criterion $\tilde b=\tilde a^{-1}$. If $\tilde a=0$ or $\tilde b=0$ the operator is the zero map, which is multiplicative because both sides of the identity vanish; the criterion is therefore stated on the non-zero parameters. Then $T(\tilde q)=\tilde a\tilde q\tilde a^{-1}$, the inner automorphism.

**Corollary.** A non-zero two-sided operator is multiplicative exactly when it is form-preserving with the positive sign; the non-zero multiplicative ones are a group under composition, and they are the algebra automorphisms of $\mathbb{H}$ that lie in the family; the zero operator is multiplicative but is not form-preserving.

*Proof.* The two criteria; the group statement is the corollary above.

**Corollary (automorphisms are inner).** Every $\mathbb{R}$-algebra automorphism of $\mathbb{H}$ is a two-sided operator and is inner: $\operatorname{Aut}(\mathbb{H})=\operatorname{Ad}(\mathbb{H}^{\times})\cong\mathbb{H}^{\times}/\mathbb{R}^{\times}$.

*Proof.* An automorphism is a real-linear operator, hence of the family; it is multiplicative, hence of the form $\operatorname{Ad}_{\tilde a}$; conversely each $\operatorname{Ad}_{\tilde a}$ is an automorphism. Every automorphism of a central simple algebra is inner by the Skolem–Noether theorem, quoted as standard, and the two descriptions agree.

## Summary

The two-sided operators $T_{\tilde a,\tilde b}(\tilde q)=\tilde a\tilde q\tilde b$ form the whole $16$-dimensional algebra of real-linear operators of $\mathbb{H}$, with the composition law $T_{\tilde a,\tilde b}T_{\tilde c,\tilde d}=T_{\tilde a\tilde c,\tilde d\tilde b}$, the identity $T_{e_0,e_0}$, and invertibility exactly when both parameters are non-zero. The transpose with respect to the plain form swaps the parameters, $T_{\tilde a,\tilde b}^{\sim}=T_{\tilde b,\tilde a}$, and the operator is self-transpose exactly when the parameters are real multiples of one another. It preserves the form exactly when $\tilde b\tilde a=\pm e_0$, that is when it is $\pm$ an inner automorphism, and for non-zero parameters it is multiplicative exactly when $\tilde b=\tilde a^{-1}$, that is when it is an inner automorphism, the zero operator being the only other multiplicative member; the form-preserving family is the group of inner automorphisms together with its negative, and every algebra automorphism of $\mathbb{H}$ is inner. Neither criterion needs the norm to be stated.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_{\tilde a,\tilde b}=L_{\tilde a}R_{\tilde b}$ | Two-sided operator, $\tilde q\mapsto\tilde a\tilde q\tilde b$ |
| $\mathcal T$ | The family of two-sided operators, $=\operatorname{End}_\mathbb{R}(\mathbb{H})$ |
| $T_{\tilde a,\tilde b}^{\sim}$ | Transpose with respect to $\mathrm B$ |
| $\operatorname{Ad}_{\tilde a}$ | Inner automorphism $\tilde q\mapsto\tilde a\tilde q\tilde a^{-1}$ |
| $\mathrm B(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p\tilde q)$ | The plain form |

## Further Reading

- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the sandwich operators and their composition.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the inner automorphisms of a central simple algebra and the Skolem–Noether theorem.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the unit group of a division ring and its centre.
