# __Matrix Representations : The Four Words and the Four Traces__

## Introduction

The four products of the biquaternion algebra become four words in a matrix, its transpose and its dagger. The four forms become the four traces of those words.

**The dictionary does not change with the size.** The four words are $XY$, $X^{\mathsf T}Y$, $XY^{\dagger}$ and $X^{\mathsf T}Y^{\dagger}$ in the $2\times2$ model and in the $4\times4$ model. What changes is the normalization: the scalar part is one half of the $2\times2$ trace and one quarter of the $4\times4$ trace, because the identity has trace $2$ in the first and $4$ in the second.

**The scope.** In the $2\times2$ model every matrix is an element, so the words are defined on all of $M_2(\mathbb{C})$. In the $4\times4$ model they are defined on the image, and the transpose is the image of quaternion conjugation only in the coefficient frame.

**Conventions.** The algebra and the model are those of *Matrix Representations : The Product, the Trace and the Determinant*. Write
$$
X=\mathsf{M}_4^{L}(\tilde P),\qquad Y=\mathsf{M}_4^{L}(\tilde Q),\qquad \operatorname{Sc}\tilde R=\tfrac14\operatorname{Tr}\mathsf{M}_4^{L}(\tilde R).
$$
The two matrix involutions are the transpose and the conjugate transpose. By *Matrix Representations : The Conjugations and the Adjoints*,
$$
\mathsf{M}_4^{L}(\tilde P^{\natural})=X^{\mathsf T},\qquad \mathsf{M}_4^{L}(\tilde P^{*})=X^{\dagger}.
$$

**Boundaries.** The four products and their relations are *The Four General Products and Their Relations over the Biquaternion Algebra*; the four forms are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the conjugations are *Matrix Representations : The Conjugations and the Adjoints*; the trace and determinant are *Matrix Representations : Trace, Determinant and the Biquaternion Norm*.

**Frame.** This article uses the coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, because that is the basis in which quaternion conjugation is transposition: $\mathsf M_4^{L}(\tilde Q^{\natural})=M^{\mathsf T}$. The canonical frame of *Matrix Representations Conventions*, §*The Matrix Models*, is the Peirce frame, where $\mathsf M_4^{L}(\tilde Q)=I_2\otimes\mathsf M_2(\tilde Q)$; the two displays differ by the Peirce change $C_{\Pi}$ of *The Product, the Trace and the Determinant*. In the canonical frame the same involution is $M\mapsto C\,M^{\mathsf T}\,C^{-1}$ with $C=-\sigma_2\otimes\sigma_2$, the signed reversal of the four Peirce coordinates.

## Common Aspects

The four products of the biquaternion algebra become four words in a matrix, its transpose and its dagger; the four forms become the four traces of those words. The dictionary is the same at both sizes. What changes is the normalization: the scalar part is one half of the $2\times2$ trace and one quarter of the $4\times4$ trace, because the identity has trace $2$ in the first and $4$ in the second.

**The four words.** Each product is one word in $X$, $Y$ and the two involutions:

| Product | First slot | Second slot | Matrix word |
|---|---|---|---|
| general plain | $X$ | $Y$ | $XY$ |
| general quaternionic | $X^{\mathsf T}$ | $Y$ | $X^{\mathsf T}Y$ |
| general plain sesquilinear | $X$ | $Y^{\dagger}$ | $XY^{\dagger}$ |
| general quaternionic sesquilinear | $X^{\mathsf T}$ | $Y^{\dagger}$ | $X^{\mathsf T}Y^{\dagger}$ |

The first slot carries the choice of conjugation on the left factor, the second the choice on the right; the two choices are independent. The words are not all distinct as matrices: they coincide where the involutions act trivially, $X^{\mathsf T}=X$ on the quaternion subspace and $Y^{\dagger}=Y$ on the Hermitian subspace, and both on the centre. The table is a table of operations, not of values.

**The four forms.** The four forms are the four words closed by a trace. On the coefficients,

$$
\langle\tilde P,\tilde Q\rangle=P_tQ_t-\vec P\cdot\vec Q,\qquad
\langle\tilde P,\tilde Q\rangle_{\natural}=P_tQ_t+\vec P\cdot\vec Q,
$$

$$
\langle\tilde P,\tilde Q\rangle_{*}=P_t\overline{Q_t}+\vec P\cdot\overline{\vec Q},\qquad
\langle\tilde P,\tilde Q\rangle_{\natural*}=P_t\overline{Q_t}-\vec P\cdot\overline{\vec Q}.
$$

The first two are complex bilinear, the last two Hermitian in the second slot.

**The signatures.** Realifying the complex forms,

| Form | Inertia over $\mathbb{C}$ | Signature over $\mathbb{R}$ |
|---|---|---|
| plain | $(2,2)$ | $(4,4)$ |
| quaternionic | $(2,2)$ | $(4,4)$ |
| Hermitian | $(4,0)$ | $(8,0)$ |
| Krein | $(1,3)$ | $(2,6)$ |

The signatures are invariants of the algebra and do not depend on the representation. What changes is the dimension of the matrix that carries them, not the form.

**The words compose.** The product of two words is a word, and the composition is the matrix product: $(\operatorname{adj}X\,Y)(Z^{\dagger})=\operatorname{adj}X\,YZ^{\dagger}$, the word of the quaternionic sesquilinear product with the middle factor $Y$. The twelve operations of the two chapters are the twelve ways of putting two involutions and two factors in a word; the four products are the four words with one factor in each slot, and the remaining eight are the compositions and the symmetrisations.

**The conjugate of a word.** The Hermitian adjoint reverses the order and exchanges the two involutions:

$$
(XY)^{\dagger}=Y^{\dagger}X^{\dagger},\qquad
(X^{\mathsf T}Y)^{\dagger}=Y^{\dagger}\overline{X},\qquad
(X^{\mathsf T}Y^{\dagger})^{\dagger}=Y\overline{X}.
$$

The four words are therefore closed under the dagger up to the exchange of the arguments and the entrywise conjugation, which is the matrix form of the Klein group of the four involutions.

## The $S_3$ Frame

**The frame.** The coefficient frame is the frame in which quaternion conjugation is transposition: $\mathsf M_4^{L}(\tilde P^{\natural})=X^{\mathsf T}$ and $\mathsf M_4^{L}(\tilde P^{*})=X^{\dagger}$, with $X=\mathsf M_4^{L}(\tilde P)$ and $Y=\mathsf M_4^{L}(\tilde Q)$. The scalar part is one quarter of the trace, $\operatorname{Sc}\tilde R=\tfrac14\operatorname{Tr}\mathsf M_4^{L}(\tilde R)$.

**The four quarter-traces.** For all $\tilde P,\tilde Q$,

$$
\tfrac14\operatorname{Tr}(XY)=\langle\tilde P,\tilde Q\rangle,\qquad
\tfrac14\operatorname{Tr}(X^{\mathsf T}Y)=\langle\tilde P,\tilde Q\rangle_{\natural},
$$

$$
\tfrac14\operatorname{Tr}(XY^{\dagger})=\langle\tilde P,\tilde Q\rangle_{*},\qquad
\tfrac14\operatorname{Tr}(X^{\mathsf T}Y^{\dagger})=\langle\tilde P,\tilde Q\rangle_{\natural*}.
$$

The proof is the trace identity: the scalar part of a product is one quarter of its $4\times4$ trace, because $\operatorname{Tr}\mathsf M_4^{L}(\tilde R)=4R_t$. The four products are $\tilde P\tilde Q$, $\tilde P^{\natural}\tilde Q$, $\tilde P\tilde Q^{*}$ and $\tilde P^{\natural}\tilde Q^{*}$, and their matrices are the four words.

**The Gram matrices.** On the coefficient basis $e_t,\vec e_x,\vec e_y,\vec e_z$,

$$
G_{\mathrm{plain}}=G_{\natural*}=\operatorname{diag}(1,-1,-1,-1),
\qquad
G_{\natural}=G_{*}=\mathrm I_4.
$$

The entries are the four forms evaluated on the basis elements: the plain form is $1$ on $e_t$ and $-1$ on each $\vec e_k$, the quaternionic form has the signs reversed, and the two Hermitian forms agree because the basis is real.

**The plain pairing and its isometry group.** The plain form is the trace pairing $\langle\tilde P,\tilde Q\rangle=\tfrac14\operatorname{Tr}(XY)=\tfrac14\operatorname{Tr}(YX)$. Its isometry group on the coefficient space is
$$
\{T\in GL_4(\mathbb{C}):T^{\mathsf T}G_{\mathrm{plain}}T=G_{\mathrm{plain}}\}\cong O_4(\mathbb{C}),
$$
of complex dimension $6$. The unit group of the algebra is $GL_2(\mathbb{C})$, of complex dimension $4$, and it is not the isometry group: the plain form is not the algebra product.

**Invariance.** The pairing is invariant under both one-sided multiplications,
$$
\langle\tilde P\tilde X,\tilde Q\rangle=\langle\tilde X,\tilde P^{\natural}\tilde Q\rangle,
\qquad
\langle\tilde X\tilde P,\tilde Q\rangle=\langle\tilde X,\tilde Q\tilde P^{\natural}\rangle,
$$
which in matrices is the cyclicity of the trace,
$$
\operatorname{Tr}(X_PX_XY_Q)=\operatorname{Tr}(X_XX_P^{\mathsf T}Y_Q),
$$
together with $X_P^{\mathsf T}=\mathsf M_4^{L}(\tilde P^{\natural})$. This invariance is the reason the trace pairing is the natural duality of the regular bimodule.

## The $2\times2$ $z$ Frame

**The half-traces.** In the entry model, with $X=\mathsf M_2(\tilde P)$ and $Y=\mathsf M_2(\tilde Q)$, the same theorem reads

$$
\tfrac12\operatorname{tr}(XY)=\langle\tilde P,\tilde Q\rangle,\qquad
\tfrac12\operatorname{tr}(X^{\mathsf T}Y)=\langle\tilde P,\tilde Q\rangle_{\natural},
$$

$$
\tfrac12\operatorname{tr}(XY^{\dagger})=\langle\tilde P,\tilde Q\rangle_{*},\qquad
\tfrac12\operatorname{tr}(X^{\mathsf T}Y^{\dagger})=\langle\tilde P,\tilde Q\rangle_{\natural*}.
$$

The four forms are the same four functions of the elements; the trace that computes them is the one of the display. The two normalizations agree because $\operatorname{tr}\mathsf M_4^{L}=2\operatorname{tr}\mathsf M_2$ and the regular word is two copies of the entry word.

**The entry words.** The table of four words is read on $M_2(\mathbb{C})$ without a qualifier, because the entry model is onto. The transpose is the entry transpose, and on the natural subspaces it coincides with the algebra involutions: it fixes the quaternion pattern and the Hermitian matrices where those conditions say it should. The half-trace is the scalar part, and the identity has trace $2$.

## The $4\times4$ $z$ Frame

**The block words.** In the Peirce frame $X=\mathrm I_2\otimes P$ and $Y=\mathrm I_2\otimes Q$ with $P=\mathsf M_2(\tilde P)$ and $Q=\mathsf M_2(\tilde Q)$. The plain and dagger words decompose blockwise:

$$
XY=\mathrm I_2\otimes(PQ),\qquad
XY^{\dagger}=\mathrm I_2\otimes(PQ^{\dagger}),
$$

and likewise $X^{\mathsf T}Y=\mathrm I_2\otimes(P^{\mathsf T}Q)$ and $X^{\mathsf T}Y^{\dagger}=\mathrm I_2\otimes(P^{\mathsf T}Q^{\dagger})$. Each word is two copies of the entry word.

**The transpose is the entry transpose.** The block display does not make $X^{\mathsf T}$ the image of $\tilde P^{\natural}$. In the Peirce frame quaternion conjugation is not entrywise transposition; it is $M\mapsto C M^{\mathsf T}C^{-1}$ with $C=-\sigma_2\otimes\sigma_2$, the signed reversal of the four Peirce coordinates. The naive transpose of the block is the entry transpose, which agrees with ${}^{\natural}$ only in the coefficient frame. The four words are therefore block words, and their identification with the four products is a statement about the coefficient frame.

**The normalization.** The trace of a block word is twice the trace of the entry word, so $\tfrac14\operatorname{Tr}=\tfrac12\operatorname{tr}$. Every form is computed by the same half-trace at size two and quarter-trace at size four, and the two agree. The block display shows the doubling directly: the identity is $\mathrm I_2\otimes\mathrm I_2$, of trace $4$, and the scalar part is one quarter of that.

## Summary

The four products are the four words $XY$, $X^{\mathsf T}Y$, $XY^{\dagger}$ and $X^{\mathsf T}Y^{\dagger}$, and the four forms are their quarter-traces. The Gram matrices are $\operatorname{diag}(1,-1,-1,-1)$ for the plain and Krein forms and the identity for the quaternionic and Hermitian forms. The signatures are those of the algebra, unchanged by the representation; only the normalization of the trace changes, from one half in the $2\times2$ model to one quarter in the $4\times4$ model.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X=\mathsf{M}_4^{L}(\tilde P)$, $Y=\mathsf{M}_4^{L}(\tilde Q)$ | the regular matrices |
| $X^{\mathsf T}=\mathsf{M}_4^{L}(\tilde P^{\natural})$ | the transpose as quaternion conjugation |
| $X^{\dagger}=\mathsf{M}_4^{L}(\tilde P^{*})$ | the conjugate transpose |
| $\tfrac14\operatorname{Tr}$ | the scalar part in the regular model |
| $G_{\mathrm{plain}},G_{\natural},G_{*},G_{\natural*}$ | the four Gram matrices |

## Further Reading

- [Matrix Representations : The Conjugations and the Adjoints](matrix-representations-the-conjugations-and-the-adjoints.html), for the two involutions
- [Matrix Representations : Trace, Determinant and the Biquaternion Norm](matrix-representations-trace-determinant-and-the-biquaternion-norm.html), for the trace and the norm
- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the products
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the forms
