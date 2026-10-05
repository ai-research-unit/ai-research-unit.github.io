# __The Trace Form of the Real Biquaternion Algebra__

## Introduction

The real biquaternion algebra carries a canonical symmetric bilinear form, its **trace form**, obtained from the regular representation: the left multiplication $L_{\tilde P}$ is a real endomorphism of the eight-dimensional algebra, and

$$
\tau(\tilde P,\tilde Q)=\operatorname{Tr}\!\left(L_{\tilde P}L_{\tilde Q}\right)
$$

is a symmetric bilinear form on $\mathbb B$ over $\mathbb R$. This article records it, its Gram matrix, its signature $(4,4)$, and its identity with the realified complex bilinear form up to the factor $8$.

## The Trace Form

**Definition.** For $\tilde P,\tilde Q\in\mathbb B$, the trace form is $\tau(\tilde P,\tilde Q)=\operatorname{Tr}(L_{\tilde P}L_{\tilde Q})$, the trace read on the eight-dimensional real representation $\tilde P\mapsto L_{\tilde P}$, $L_{\tilde P}(\tilde X)=\tilde P\tilde X$.

It is bilinear and symmetric, because $\operatorname{Tr}(L_{\tilde P}L_{\tilde Q})=\operatorname{Tr}(L_{\tilde Q}L_{\tilde P})$; it is invariant under the left and right multiplications by units in the following sense, that

$$
\tau(U\tilde P U^{-1},U\tilde Q U^{-1})=\tau(\tilde P,\tilde Q)\quad\text{for }U\in\mathbb B^\times,
$$

since conjugation of the representation does not change the trace; and it is non-degenerate.

## The Gram Matrix and the Signature

Because $L_{\tilde P\tilde Q}=L_{\tilde P}L_{\tilde Q}$ and the trace of $L_{\tilde X}$ is $8$ for $\tilde X=e_0$ and $0$ for $\tilde X=e_k$ or $\tilde X=ie_k$, the values on the real basis are

$$
\tau(e_\mu,e_\nu)=8\,\varepsilon_\mu\delta_{\mu\nu},\qquad
\tau(e_\mu,ie_\nu)=0,\qquad
\tau(ie_\mu,ie_\nu)=-8\,\varepsilon_\mu\delta_{\mu\nu},
$$

so the Gram matrix is

$$
8\cdot\operatorname{diag}(1,-1,-1,-1,-1,1,1,1),
$$

of **signature $(4,4)$**. The four positive directions are $e_0$, $ie_1$, $ie_2$, $ie_3$ and the four negative directions are $e_1,e_2,e_3,ie_0$.

## The Identity with the Realified Complex Bilinear Form

Comparing the two Gram matrices, the trace form is exactly **eight times the realification of the complex bilinear form**,

$$
\tau(\tilde P,\tilde Q)=8\,\mathrm{Re}\langle\tilde P,\tilde Q\rangle ,
\qquad
\langle\tilde P,\tilde Q\rangle=\sum_\mu\varepsilon_\mu P_\mu Q_\mu .
$$

This is the reason it is not an independent fifth form: read on the eight real dimensions it reproduces the realified complex bilinear form of *The Realification of the Four Forms*, up to the normalisation $8$ of the regular representation. The trace read on the complex four-dimensional module $\mathbb B\cong\mathbb C^4$ gives instead $4\,\mathrm{Re}\langle\tilde P,\tilde Q\rangle$, the same form with the factor $4$; the factor is the dimension of the carrier, and the form is the same.

## The Place among the Forms

The trace form is the natural form of the **real** algebra, and it is the one available before any of the four complex products is chosen: it uses only the regular representation and the trace, which are algebraic data. It is the real counterpart of the Hilbert–Schmidt pairing $\tfrac12\operatorname{Tr}(\Phi(\tilde P)^{\dagger}\Phi(\tilde Q))$ of the matrix model, which is the positive definite form; the trace form is the split form obtained from the same trace by dropping the adjoint. Its signature $(4,4)$ is the signature of the complex bilinear realification, and its relation to the four forms is tabulated in *The Realification of the Four Forms*.

## Summary

The trace form of the real biquaternion algebra is $\tau(\tilde P,\tilde Q)=\operatorname{Tr}(L_{\tilde P}L_{\tilde Q})$, symmetric, non-degenerate and invariant under conjugation by units. Its Gram matrix is $8\cdot\operatorname{diag}(1,-1,-1,-1,-1,1,1,1)$ and its signature is $(4,4)$. It is $8$ times the realification of the complex bilinear form, so it is not a new form but the same one read from the regular representation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tau(\tilde P,\tilde Q)=\operatorname{Tr}(L_{\tilde P}L_{\tilde Q})$ | the trace form, read over $\mathbb R$ |
| $8\cdot\operatorname{diag}(1,-1,-1,-1,-1,1,1,1)$ | its Gram matrix |
| $(4,4)$ | its signature |
| $\tau=8\,\mathrm{Re}\langle\cdot,\cdot\rangle$ | its identity with the realified complex bilinear form |

## Further Reading

- *The Realification of the Four Forms* (`articles_maths/the-realification-of-the-four-forms.md`), for the four realified forms
- *The Gram Matrix of the Complex Bilinear Form* (`articles_maths/the-gram-matrix-of-the-complex-bilinear-form.md`), for the complex bilinear form it reproduces
- *Biquaternions as a Module over Itself* (`articles_maths/biquaternions-as-a-module-over-itself.md`), for the regular representation
