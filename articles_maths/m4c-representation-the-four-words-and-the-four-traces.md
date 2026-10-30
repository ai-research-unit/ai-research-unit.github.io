# __$M_4(\mathbb{C})_{\mathbb{B}}$ Representation : The Four Words and the Four Traces__

## Introduction

The four products of the biquaternion algebra become four words in the regular matrix and its transpose and dagger. The four forms become the four traces of those words, with the normalization fixed by the size of the matrix: the scalar part is one quarter of the $4\times4$ trace, not one half.

This article writes the dictionary. It is the $4\times4$ counterpart of *$M_2(\mathbb{C})$ Representation : The Four Words and the Four Traces*, and the proof is the same trace identity with the normalization changed.

**Conventions.** The algebra and the model are those of *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant*. Write
$$
X=\mathsf{M}_4^{L}(\tilde P),\qquad Y=\mathsf{M}_4^{L}(\tilde Q),\qquad \operatorname{Sc}\tilde R=\tfrac14\operatorname{Tr}\mathsf{M}_4^{L}(\tilde R).
$$
The two matrix involutions are the transpose and the conjugate transpose. By *$M_4(\mathbb{C})_{\mathbb{B}}$ Representation : The Conjugations and the Adjoints*,
$$
\mathsf{M}_4^{L}(\tilde P^{\natural})=X^{\mathsf T},\qquad \mathsf{M}_4^{L}(\tilde P^{*})=X^{\dagger}.
$$

**Boundaries.** The four products and their relations are *The Four General Products and Their Relations over the Biquaternion Algebra*; the four forms are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the conjugations are *$M_4(\mathbb{C})_{\mathbb{B}}$ Representation : The Conjugations and the Adjoints*; the trace and determinant are *$M_4(\mathbb{C})_{\mathbb{B}}$ Representation : Trace, Determinant and the Biquaternion Norm*.

**Frame.** This article uses the coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, because that is the basis in which quaternion conjugation is transposition: $\mathsf M_4^{L}(\tilde Q^{\natural})=M^{\mathsf T}$. The canonical frame of *Conventions of the Matrix Models*, §*The Matrix Models*, is the Peirce frame, where $\mathsf M_4^{L}(\tilde Q)=I_2\otimes\mathsf M_2(\tilde Q)$; the two displays differ by the change $S$ of *The Product, the Trace and the Determinant*. In the canonical frame the same involution is $M\mapsto C\,M^{\mathsf T}\,C^{-1}$ with $C=-\sigma_2\otimes\sigma_2$, the signed reversal of the four Peirce coordinates.

## The Two Matrices and the Two Involutions

Write
$$
X=\mathsf{M}_4^{L}(\tilde P),\qquad Y=\mathsf{M}_4^{L}(\tilde Q).
$$
The two involutions of the model are the adjugate and the conjugate transpose:
$$
\operatorname{adj}X=\det(X)\,X^{-1},\qquad
X^{\dagger}=\overline{X^{\mathsf T}}.
$$
They are the images of quaternion conjugation and of Hermitian conjugation:
$$
\mathsf{M}_4^{L}(\tilde P^{\natural})=N^{-1}\operatorname{adj}X,\qquad
\mathsf{M}_4^{L}(\tilde P^{*})=X^{\dagger},
$$
where $N=\langle\tilde P\rangle_{\natural}$. The scalar is forced by the size: the adjugate of a $4\times4$ matrix is homogeneous of degree three, while $\mathsf{M}_4^{L}(\tilde P^{\natural})$ is linear, so the two differ by the quadratic norm. The adjugate is an anti-automorphism, $\operatorname{adj}(XY)=\operatorname{adj}(Y)\operatorname{adj}(X)$, and it satisfies $X\operatorname{adj}X=(\det X)\mathrm I_4$. The dagger is an anti-automorphism of the real algebra, $(XY)^{\dagger}=Y^{\dagger}X^{\dagger}$. Both are involutions: $\operatorname{adj}(\operatorname{adj}X)=X$ and $(X^{\dagger})^{\dagger}=X$.

## The Four Words

**Each product is one word in $X$, $Y$ and the two involutions.**

| Product | First slot | Second slot | Matrix word |
|---|---|---|---|
| general plain | $X$ | $Y$ | $XY$ |
| general quaternionic | $X^{\mathsf T}$ | $Y$ | $X^{\mathsf T}Y$ |
| general plain sesquilinear | $X$ | $Y^{\dagger}$ | $XY^{\dagger}$ |
| general quaternionic sesquilinear | $X^{\mathsf T}$ | $Y^{\dagger}$ | $X^{\mathsf T}Y^{\dagger}$ |

The table is the matrix form of the definition of the four products: the first slot carries the choice of conjugation on the left factor, the second the choice on the right. The two choices are independent.

**The words are not all distinct as matrices.** They coincide on the subspaces where the involutions act trivially: $X^{\mathsf T}=X$ on the quaternion subspace, $Y^{\dagger}=Y$ on the Hermitian subspace, and both hold on the centre. The table is a table of operations, not of values.

**The symmetric and antisymmetric halves.** For a word $W(X,Y)$, the symmetric part is $\tfrac12(W(X,Y)+W(Y,X))$ and the antisymmetric part is $\tfrac12(W(X,Y)-W(Y,X))$. Applied to the four words, the operation reproduces the twelve products of *Symmetric and Antisymmetric Decomposition of the Four General Products*. The matrix form makes the symmetrization a symmetrization of words.

## The Four Traces

**Theorem (the four forms are four quarter-traces).** For all $\tilde P,\tilde Q$,

$$
\tfrac14\operatorname{Tr}(XY)=\langle\tilde P,\tilde Q\rangle,\qquad
\tfrac14\operatorname{Tr}(X^{\mathsf T}Y)=\langle\tilde P,\tilde Q\rangle_{\natural},
$$

$$
\tfrac14\operatorname{Tr}(XY^{\dagger})=\langle\tilde P,\tilde Q\rangle_{*},\qquad
\tfrac14\operatorname{Tr}(X^{\mathsf T}Y^{\dagger})=\langle\tilde P,\tilde Q\rangle_{\natural*}.
$$

*Proof.* The scalar part of a product is one quarter of its $4\times4$ trace, because the trace of $\mathsf{M}_4^{L}(\tilde R)$ is $4R_t$. The four products are $\tilde P\tilde Q$, $\tilde P^{\natural}\tilde Q$, $\tilde P\tilde Q^{*}$ and $\tilde P^{\natural}\tilde Q^{*}$, and their matrices are the four words of the table. The trace of a product of images is the image of the trace, and the identities follow.

**The coefficient forms.** Written on the coefficients,

$$
\langle\tilde P,\tilde Q\rangle=P_tQ_t-\vec P\cdot\vec Q,\qquad
\langle\tilde P,\tilde Q\rangle_{\natural}=P_tQ_t+\vec P\cdot\vec Q,
$$

$$
\langle\tilde P,\tilde Q\rangle_{*}=P_t\overline{Q_t}+\vec P\cdot\overline{\vec Q},\qquad
\langle\tilde P,\tilde Q\rangle_{\natural*}=P_t\overline{Q_t}-\vec P\cdot\overline{\vec Q}.
$$

The first two are complex bilinear, the last two Hermitian in the second slot.

**The normalization.** In the $2\times2$ model the scalar part is one half of the trace. In the $4\times4$ model it is one quarter, because the identity has trace $4$. The forms themselves are unchanged: they live on the algebra, and the representation only changes the size of the trace that computes them.

## The Trace Pairing

**On the coefficient basis $e_t,\vec e_x,\vec e_y,\vec e_z$,**

$$
G_{\mathrm{plain}}=G_{\natural*}=\operatorname{diag}(1,-1,-1,-1),
\qquad
G_{\natural}=G_{*}=\mathrm I_4.
$$

*Proof.* The Gram entries are the four forms evaluated on the basis elements. For the plain form, $\langle e_\mu,e_\nu\rangle$ is $1$ on $e_t$, $-1$ on each $\vec e_k$, and $0$ across. For the quaternionic form the signs of the vector part are reversed, giving the identity. The two Hermitian forms have the same matrices because the basis is real, so conjugation acts trivially on the coefficients of the basis elements.

**The signatures.** Realifying the complex forms,

| Form | Inertia over $\mathbb{C}$ | Signature over $\mathbb{R}$ |
|---|---|---|
| plain | $(2,2)$ | $(4,4)$ |
| quaternionic | $(2,2)$ | $(4,4)$ |
| Hermitian | $(4,0)$ | $(8,0)$ |
| Krein | $(1,3)$ | $(2,6)$ |

The signatures are those of the $2\times2$ article: they are invariants of the algebra and do not depend on the representation. What changes is the dimension of the matrix that carries them, not the form.


**The plain form is the trace pairing.**

$$
\langle\tilde P,\tilde Q\rangle=\tfrac14\operatorname{Tr}(XY)=\tfrac14\operatorname{Tr}(YX).
$$

It is symmetric, non-degenerate, and its isometry group on the coefficient space is
$$
\{T\in GL_4(\mathbb{C}):T^{\mathsf T}G_{\mathrm{plain}}T=G_{\mathrm{plain}}\}\cong O_4(\mathbb{C}),
$$
of complex dimension $6$. The unit group of the algebra is $GL_2(\mathbb{C})$, of complex dimension $4$, and it is not the isometry group. The two groups act on the same four-dimensional space and are different: the plain form is not the algebra product.

**The invariance.** The pairing is invariant under both one-sided multiplications:
$$
\langle\tilde P\tilde X,\tilde Q\rangle=\langle\tilde X,\tilde P^{\natural}\tilde Q\rangle,
\qquad
\langle\tilde X\tilde P,\tilde Q\rangle=\langle\tilde X,\tilde Q\tilde P^{\natural}\rangle.
$$
In matrices, these are the cyclicity of the trace,
$$
\operatorname{Tr}(X_PX_XY_Q)=\operatorname{Tr}(X_X X_P^{\mathsf T}Y_Q),
$$
and the transpose identity $X_P^{\mathsf T}=\mathsf{M}_4^{L}(\tilde P^{\natural})$. The invariance is the reason the trace pairing is the natural duality of the regular bimodule.

## The Four Words in the Algebra

**The words compose.** The product of two words is a word, and the composition is the matrix product. For example,
$$
(\operatorname{adj}X\,Y)(Z^{\dagger})=\operatorname{adj}X\,YZ^{\dagger},
$$
which is the word of the quaternionic sesquilinear product with the middle factor $Y$. The twelve operations of the two chapters are the twelve ways of putting two involutions and two factors in a word; the four products are the four words with one factor in each slot, and the remaining eight are the compositions and the symmetrisations.

**The words and the four forms.** The four forms are the four words closed by a trace. The trace kills the antisymmetric part of a word, so the form of a product and the form of its symmetrisation agree; the antisymmetric part contributes only to the bracket. This is why the four forms are symmetric or conjugate-symmetric while the four products are not. In the regular model the trace is four times the scalar part, and the four forms are the $2\times2$ forms read twice.

## The Conjugate of a Word

**Proposition.** The Hermitian adjoint of a word reverses the order and exchanges the two involutions:

$$
(XY)^{\dagger}=Y^{\dagger}X^{\dagger},\qquad
(X^{\mathsf T}Y)^{\dagger}=Y^{\dagger}\overline{X},
\qquad
(X^{\mathsf T}Y^{\dagger})^{\dagger}=Y\overline{X}.
$$

*Proof.* The dagger is an anti-automorphism and the transpose is an anti-automorphism; the two commute with each other, because both act entrywise after transposition. The entrywise conjugate is $\overline{X}=\mathsf{M}_4^{L}(\overline{\tilde P})$, and $(X^{\mathsf T})^{\dagger}=\overline{X}$.

The four words are therefore closed under the dagger up to the exchange of the two arguments and the entrywise conjugation, which is the matrix form of the Klein group of the four involutions.

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

- [$M_4(\mathbb{C})_{\mathbb{B}}$ Representation : The Conjugations and the Adjoints](m4c-representation-the-conjugations-and-the-adjoints.html), for the two involutions
- [$M_4(\mathbb{C})_{\mathbb{B}}$ Representation : Trace, Determinant and the Biquaternion Norm](m4c-representation-trace-determinant-and-the-biquaternion-norm.html), for the trace
- [$M_2(\mathbb{C})$ Representation : The Four Words and the Four Traces](m2c-representation-the-four-words-and-the-four-traces.html), for the $2\times2$ dictionary
- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the products
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the forms
