# __Association and the Transpose on the Biquaternion Algebra__

## Introduction

The linear endomorphisms of the biquaternion algebra carry two involutions. The first is the **dagger**, the adjoint with respect to the positive definite complex sesquilinear form, treated in *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*. The second is **association**, and it is the involution that makes a linear function transposable; it is the adjoint with respect to the **complex bilinear form** $\langle\tilde R,\tilde S\rangle = \mathrm{Sc}(\tilde R\tilde S)$ of signature $(1,3)$ rather than with respect to the Hermitian one.

The two agree on the group elements that the corpus uses, and this is the reason the source literature can treat them interchangeably. Off those elements they differ, and the corpus keeps them apart. This article holds the association construction and the scalar form it belongs to; they were a section of *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure*, extracted here because they are a form and its duality, not algebra.

## The Scalar Bilinear Form

Let $\mathrm{Sc}$ be the scalar part. The **complex bilinear form** is

$$
\langle\tilde R,\tilde S\rangle = \mathrm{Sc}(\tilde R\tilde S) = R_0S_0 - R_1S_1 - R_2S_2 - R_3S_3 .
$$

It is symmetric and non-degenerate, and it is **indefinite**, of signature $(1,3)$, with Gram matrix

$$
D = \operatorname{diag}(1,-1,-1,-1)
$$

in the basis $e_0,e_1,e_2,e_3$. It is the form whose polarisation is the complex bilinear form $N$ of *The Bilinear Form on the Biquaternion Algebra*: on the coordinate basis the two agree, and $B$ is the quadratic form $N$ read on the Conway operator basis.

## Function Association

The **associate** $F^{\approx}$ of a linear function $F$ is defined by

$$
\mathrm{Sc}\bigl(F(\tilde R)\,\tilde S\bigr) = \mathrm{Sc}\bigl(\tilde R\, F^{\approx}(\tilde S)\bigr)
\qquad \text{for all } \tilde R, \tilde S \in \mathbb{B},
$$

equivalently $\langle F\tilde R,\tilde S\rangle = \langle\tilde R,F^{\approx}\tilde S\rangle$. Association is the **transpose** with respect to $B$.

**Proposition (association reverses the factors).** On the Conway operator basis $e_n[\,]e_m$ of *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure*, §*The Conway Operator Basis*,

$$
\bigl(e_n[\,]e_m\bigr)^{\approx} = e_m[\,]e_n ,
\qquad\text{so}\qquad
\Bigl(\sum_{n,m} A_{nm}\, e_n[\,]e_m\Bigr)^{\approx} = \sum_{n,m} A_{nm}\, e_m[\,]e_n ,
$$

and in particular $\bigl(a[\,]b\bigr)^{\approx} = b[\,]a$, so that $L_a^{\approx} = R_a$ and $R_b^{\approx} = L_b$.

*Proof.* $B\bigl((a[\,]b)(\tilde R), \tilde S\bigr) = \mathrm{Sc}(a\tilde Rb\tilde S) = \mathrm{Sc}(\tilde Rb\tilde Sa) = B\bigl(\tilde R, (b[\,]a)(\tilde S)\bigr)$ by the invariance of the scalar part under cyclic permutation, and $B$ is non-degenerate.

**Proposition (the matrix of association).** The transpose with respect to $B$ is

$$
F^{\approx} = D\,F^{\mathsf T}D ,
$$

for $F^{\mathsf T}$ the plain matrix transpose. The two agree exactly when $D$ acts trivially, in particular for the operators that fix $e_0$ and preserve the vector part.

## Association and the Hermitian Adjoint

**Proposition (coefficient conjugation).** Let $\bar F( ) = \sum \bar A_{nm} e_n[\,]e_m$ be the function obtained by conjugating the coefficients, and let $F^{*}$ be the adjoint of $F$ with respect to the complex sesquilinear form $(\tilde R, \tilde S) = \mathrm{Sc}(\tilde R^{*}\tilde S) = \sum_\mu \tilde R_{\bar\mu}\tilde S_\mu$ of *The Hermitian Form on the Biquaternion Algebra*, so that $(\tilde F(\tilde R),\tilde S) = (\tilde R,F^{*}(\tilde S))$. Then

$$
\bar F^{\approx} = D\,F^{*}D .
$$

On the operators that fix $e_0$ and preserve the vector part — among them every $\mathrm{SU}(3)$ and $\mathrm{SU}(4)$ element of *Biquaternion Lie Group and Exponential Structure* — the matrix has no entries mixing the scalar slot with the vector slots, the conjugation by $D$ is invisible, and the identity collapses to

$$
\bar F^{\approx} = F^{*} = F^{-1} \qquad \text{for unitary } F ,
$$

which is the source's $G^{-1} = G^{+\approx} = G^{\dagger}$.

*Proof.* The Gram matrix of the complex sesquilinear form is the identity while that of $B$ is $D$, so the two transposes differ by a conjugation by $D$ on both sides, and conjugating the coefficients turns the transpose with respect to $B$ into the adjoint with respect to the complex sesquilinear form, again up to $D$. For a unitary $F$ the adjoint is the inverse.

**Remark (why the source's rule is safe there).** The source's group elements all fix the scalar unit and map the vector part to itself, so $D$ has no visible effect on their block form; this is why the source may use the plain transpose and the Hermitian adjoint interchangeably. For a general linear function the two involutions differ, and the corpus keeps them apart: association is the transpose for the **indefinite** scalar form, the dagger is the adjoint for the **positive Hermitian** form.

## Summary

The **complex bilinear form** $\langle\tilde R,\tilde S\rangle = \mathrm{Sc}(\tilde R\tilde S)$ is symmetric, non-degenerate and indefinite, and on the real quaternion subspace of signature $(1,3)$; its Gram matrix in the basis $e_0,e_1,e_2,e_3$ is $D = \operatorname{diag}(1,-1,-1,-1)$. It is the companion of the *bilinear form* $\langle\tilde{P},\tilde{Q}\rangle_{\natural} = \mathrm{Sc}(\tilde{P}\tilde{Q}^{\natural})$ of *The Bilinear Form on the Biquaternion Algebra*, which is a different pairing, the polarisation of the norm, of Gram matrix $\mathrm{I}_4$: **Association** $F^{\approx}$ is the transpose with respect to it, defined by $\mathrm{Sc}(F(\tilde R)\tilde S) = \mathrm{Sc}(\tilde R F^{\approx}(\tilde S))$; on the Conway basis it reverses the factors, $(e_n[\,]e_m)^{\approx} = e_m[\,]e_n$, and in matrix form $F^{\approx} = D F^{\mathsf T} D$. Combined with the conjugation of the coefficients it gives $\bar F^{\approx} = D F^{*} D$ against the Hermitian adjoint, which collapses to $\bar F^{\approx} = F^{*} = F^{-1}$ on the unitary elements that fix the scalar unit and preserve the vector part. This construction belonged to *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure* and now stands here; the enveloping algebra itself, the Conway basis and the bi-module structure are that article, and the Hermitian adjoint is *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde R,\tilde S\rangle = \mathrm{Sc}(\tilde R\tilde S)$ | The complex bilinear form; symmetric, indefinite of signature $(1,3)$ |
| $D = \operatorname{diag}(1,-1,-1,-1)$ | The Gram matrix of $B$; the fundamental symmetry up to sign |
| $F^{\approx}$ | The associate of $F$; the transpose for $B$, $F^{\approx} = D F^{\mathsf T} D$ |
| $\bar F^{\approx} = D F^{*} D$ | Association combined with coefficient conjugation, against the Hermitian adjoint |
| $(e_n[\,]e_m)^{\approx} = e_m[\,]e_n$ | Association on the Conway basis |

## Further Reading

- *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure* (`articles_maths/the-enveloping-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.md`), for the Conway operator basis and the bi-module structure
- *The Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-bilinear-form-on-the-biquaternion-algebra.md`), for the form whose duality this transpose is
- *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/two-sided-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the Hermitian adjoint
- *The Hermitian Form on the Biquaternion Algebra* (`articles_maths/the-hermitian-form-on-the-biquaternion-algebra.md`), for the positive definite form the adjoint uses
- *Biquaternion Lie Group and Exponential Structure* (`articles_maths/biquaternion-lie-group-and-exponential-structure.md`), for the group elements on which the two involutions agree
