# __$M_2(\mathbb{C})$ Representation : The Four Words and the Four Traces__

## Introduction

The biquaternion algebra carries four products and four forms. In the matrix model each product becomes a word in the two matrices of its arguments and in the two involutions of the model, and each form becomes the trace of that word. The correspondence is exact and finite: four products, four words, four half-traces.

This article writes the dictionary. It is the matrix form of *The Four General Products and Their Relations over the Biquaternion Algebra* and of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the algebra-side statements are cited and not repeated.

**Conventions.** The algebra and the model are those of *$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure*: $\tilde Q=Q_te_t+\vec Q$, $B^2=Q_x^2+Q_y^2+Q_z^2$, $\mathsf{M}_2(\vec e_k)=-i\sigma_k$, and $\epsilon=\mathsf{M}_2(-\vec e_y)$. The four products are

$$
\tilde P\tilde Q,\qquad \tilde P^{\natural}\tilde Q,\qquad \tilde P\tilde Q^{*},\qquad \tilde P^{\natural}\tilde Q^{*},
$$

the general plain, the general quaternionic, the general plain sesquilinear and the general quaternionic sesquilinear product. The four forms are their scalar parts, written $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$.

**Boundaries.** The products and their relations are *The Four General Products and Their Relations over the Biquaternion Algebra*; the forms and their algebraic norms are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the involutions are *$M_2(\mathbb{C})$ Representation : The Conjugations and the Adjoints*; the trace and the determinant are *$M_2(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm*.

## The Two Matrices and the Two Involutions

Write

$$
X=\mathsf{M}_2(\tilde P),\qquad Y=\mathsf{M}_2(\tilde Q).
$$

The two involutions of the model are the adjugate and the conjugate transpose:

$$
\operatorname{adj}X=\begin{pmatrix}d&-b\\-c&a\end{pmatrix}\quad\text{for}\quad X=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\qquad
X^{\dagger}=\overline{X^{\mathsf T}}.
$$

They are the images of quaternion conjugation and of Hermitian conjugation:

$$
\mathsf{M}_2(\tilde P^{\natural})=\operatorname{adj}X,\qquad
\mathsf{M}_2(\tilde P^{*})=X^{\dagger}.
$$

The adjugate is an anti-automorphism, $\operatorname{adj}(XY)=\operatorname{adj}(Y)\operatorname{adj}(X)$, and it satisfies $X\operatorname{adj}X=(\det X)\mathrm I_2$. The dagger is an anti-automorphism of the real algebra, $(XY)^{\dagger}=Y^{\dagger}X^{\dagger}$. Both are involutions: $\operatorname{adj}(\operatorname{adj}X)=X$ and $(X^{\dagger})^{\dagger}=X$.

## The Four Words

**Each product is one word in $X$, $Y$ and the two involutions.**

| Product | First slot | Second slot | Matrix word |
|---|---|---|---|
| general plain | $X$ | $Y$ | $XY$ |
| general quaternionic | $\operatorname{adj}X$ | $Y$ | $\operatorname{adj}X\,Y$ |
| general plain sesquilinear | $X$ | $Y^{\dagger}$ | $XY^{\dagger}$ |
| general quaternionic sesquilinear | $\operatorname{adj}X$ | $Y^{\dagger}$ | $\operatorname{adj}X\,Y^{\dagger}$ |

The table is the matrix form of the definition of the four products: the first slot carries the choice of conjugation on the left factor, the second slot the choice on the right factor. The two choices are independent, and their four combinations are the four products.

**The words are not all distinct as matrices.** For particular elements they may coincide; the identities $\operatorname{adj}X=X^{\dagger}$, $\operatorname{adj}X=X$ and $X^{\dagger}=X$ hold on the quaternion subspace, on the centre and on the Hermitian subspace respectively. The table is a table of operations, not of values.

**The symmetric and antisymmetric halves.** For any word $W(X,Y)$, the symmetric part is $\tfrac12(W(X,Y)+W(Y,X))$ and the antisymmetric part is $\tfrac12(W(X,Y)-W(Y,X))$. Applied to the four words, the operation produces the symmetric and antisymmetric products of *Symmetric and Antisymmetric Decomposition of the Four General Products*. The matrix form makes the symmetrisation a symmetrisation of words, and the two halves are read off by adding and subtracting the two matrices.

## The Four Traces

**The four forms are four half-traces.**

$$
\tfrac12\operatorname{Tr}(XY)=\langle\tilde P,\tilde Q\rangle,\qquad
\tfrac12\operatorname{Tr}(\operatorname{adj}X\,Y)=\langle\tilde P,\tilde Q\rangle_{\natural},
$$

$$
\tfrac12\operatorname{Tr}(XY^{\dagger})=\langle\tilde P,\tilde Q\rangle_{*},\qquad
\tfrac12\operatorname{Tr}(\operatorname{adj}X\,Y^{\dagger})=\langle\tilde P,\tilde Q\rangle_{\natural*}.
$$

*Proof.* The scalar part of a product is half its trace, $\operatorname{Sc}\tilde R=\tfrac12\operatorname{Tr}\mathsf{M}_2(\tilde R)$, because the trace is $2R_t$. The four products have scalar parts $\operatorname{Sc}(\tilde P\tilde Q)$, $\operatorname{Sc}(\tilde P^{\natural}\tilde Q)$, $\operatorname{Sc}(\tilde P\tilde Q^{*})$ and $\operatorname{Sc}(\tilde P^{\natural}\tilde Q^{*})$, and the images of the factors are $X$, $\operatorname{adj}X$, $Y$ and $\operatorname{adj}Y$ in the combinations of the table. The trace of the product of the images is the image of the trace, and the four identities follow.

Written on the coefficients, the four forms are

$$
\langle\tilde P,\tilde Q\rangle=P_tQ_t-\vec P\cdot\vec Q,\qquad
\langle\tilde P,\tilde Q\rangle_{\natural}=P_tQ_t+\vec P\cdot\vec Q,
$$

$$
\langle\tilde P,\tilde Q\rangle_{*}=P_t\overline{Q_t}+\vec P\cdot\overline{\vec Q},\qquad
\langle\tilde P,\tilde Q\rangle_{\natural*}=P_t\overline{Q_t}-\vec P\cdot\overline{\vec Q}.
$$

The first two are complex bilinear, the last two are Hermitian in the second slot. The first and the fourth have the sign matrix $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$ as Gram matrix on the coefficient basis; the second and the third have the identity $\mathrm I_4$.

**The signatures of the realifications.** The complex bilinear forms realify to signatures $(4,4)$: each complex direction contributes one positive and one negative real direction. The Hermitian form $\langle\cdot,\cdot\rangle_{*}$ has inertia $(4,0)$ and realifies to the Euclidean signature $(8,0)$. The Krein form $\langle\cdot,\cdot\rangle_{\natural*}$ has inertia $(1,3)$ and realifies to the signature $(2,6)$. These are the four signatures of the four forms, and they separate the four forms as sharply as the words do.

**The null sets.** The plain and quaternionic bilinear forms vanish on complex cones of real dimension six. The Hermitian form is definite and has no null set. The Krein form vanishes on a real quadric of real dimension seven. The dimensions are those of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, §*What the Four Algebraic Norms Separate*.

## The Trace Pairing

**The plain bilinear form is the trace pairing.**

$$
\langle\tilde P,\tilde Q\rangle=\tfrac12\operatorname{Tr}(XY)=\tfrac12\operatorname{Tr}(YX).
$$

It is symmetric because the trace is cyclic, and it is non-degenerate: if $\langle\tilde P,\tilde Q\rangle=0$ for every $\tilde Q$, then $X=0$. Its Gram matrix on the coefficient basis is

$$
\mathrm E=\operatorname{diag}(1,-1,-1,-1),
$$

so its isometry group is

$$
\{T\in GL_4(\mathbb{C}):T^{\mathsf T}\mathrm E\,T=\mathrm E\}\cong O_4(\mathbb{C}).
$$

This group is the isometry group of the form, not the group of units of the algebra. The unit group is $GL_2(\mathbb{C})$, of complex dimension four; the isometry group is of complex dimension six. The two act on the same four-dimensional space and are not the same group. The distinction is the matrix form of the statement that the plain bilinear form is not the algebra product.

**Why the trace pairing is the right one.** It is the unique, up to a scalar, symmetric bilinear form on $\mathbb{B}$ that is invariant under both one-sided multiplications. The invariance is the identity $\operatorname{Tr}(L_{\tilde P}X)=\operatorname{Tr}(X L_{\tilde P})$, which is the cyclicity of the trace. The form is the trace form of the regular representation, and it is the pairing used to dualise the algebra in *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*.

**The real forms.** The complex group $O_4(\mathbb{C})$ has real forms, and they are exhibited by the two antilinear structures of the algebra. Hermitian conjugation ${}^{*}$ is an antilinear reversal of the pairing whose fixed space is $\mathbb M_+$, of restriction signature $(4,0)$; the automorphisms that commute with it form the real orthogonal group $O(4)$. Coefficient conjugation has fixed space the quaternion subspace, of signature $(1,3)$, and exhibits $O(1,3)$. The group of real-linear automorphisms of the realified form is the larger $O(4,4)$, which is not the group the form defines over $\mathbb{C}$. On the matrices, the conjugation $M\mapsto UMU^{-1}$ by a unit and the transposition $M\mapsto M^{\mathsf T}$ are automorphisms, because $\operatorname{Tr}(UMU^{-1}\cdot UNU^{-1})=\operatorname{Tr}(MN)$ and $\operatorname{Tr}(M^{\mathsf T}N^{\mathsf T})=\operatorname{Tr}(MN)$; the inner automorphisms and the transposition together form a proper subgroup of $O_4(\mathbb{C})$.

## The Four Words in the Algebra

**The words compose.** The product of two words is a word, and the composition is the matrix product. For example,

$$
(\operatorname{adj}X\,Y)(Z^{\dagger})=\operatorname{adj}X\,YZ^{\dagger},
$$

which is the word of the quaternionic sesquilinear product with the middle factor $Y$. The twelve operations of the two chapters are the twelve ways of putting two involutions and two factors in a word; the four products are the four words with one factor in each slot, and the remaining eight are the compositions and the symmetrisations.

**The words and the four forms.** The four forms are the four words closed by a trace. The trace kills the antisymmetric part of a word, so the form of a product and the form of its symmetrisation agree; the antisymmetric part contributes only to the bracket. This is why the four forms are symmetric or conjugate-symmetric while the four products are not.

## The Conjugate of a Word

The two involutions reverse a word, and the conjugation identities of *The Four General Products and Their Relations over the Biquaternion Algebra*, §*The Conjugate of a Product*, are matrix identities. The two pure rules are

$$
\operatorname{adj}(XY)=\operatorname{adj}(Y)\operatorname{adj}(X),
\qquad
(XY)^{\dagger}=Y^{\dagger}X^{\dagger},
$$

and the two mixed rules that exchange the factors are

$$
(XY^{\dagger})^{\dagger}=YX^{\dagger},
\qquad
\operatorname{adj}\bigl(\operatorname{adj}(X)Y\bigr)=\operatorname{adj}(Y)X .
$$

Two further mixed rules read

$$
\operatorname{adj}(XY^{\dagger})=\operatorname{adj}(Y)^{\dagger}\operatorname{adj}(X),
\qquad
\operatorname{adj}\bigl(\operatorname{adj}(X)Y^{\dagger}\bigr)=\operatorname{adj}(Y)^{\dagger}X,
$$

$$
\bigl(\operatorname{adj}(X)Y\bigr)^{\dagger}=Y^{\dagger}\operatorname{adj}(X^{\dagger}),
\qquad
\bigl(\operatorname{adj}(X)Y^{\dagger}\bigr)^{\dagger}=Y\operatorname{adj}(X^{\dagger}).
$$

The first two are the adjugate rules for the two mixed words, and the last two are the dagger rules. Each identity is an anti-automorphism rule applied to the corresponding word, and none of them uses an extra entrywise conjugation: the algebra conjugation is the adjugate, and the Hermitian conjugation is the dagger.

## Summary

The matrix model turns the four products into four words: $XY$, $\operatorname{adj}X\,Y$, $XY^{\dagger}$ and $\operatorname{adj}X\,Y^{\dagger}$. The four forms are the four half-traces of those words, and on the coefficients they are the plain and quaternionic bilinear forms and the plain and quaternionic Hermitian forms. The trace pairing is the plain bilinear form; its Gram matrix is $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$, and its isometry group is $O_4(\mathbb{C})$, not the unit group. The realifications have signatures $(4,4)$, $(4,4)$, $(8,0)$ and $(2,6)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X=\mathsf{M}_2(\tilde P)$, $Y=\mathsf{M}_2(\tilde Q)$ | the two matrices |
| $\operatorname{adj}X$ | the adjugate, the image of ${}^{\natural}$ |
| $X^{\dagger}$ | the conjugate transpose, the image of ${}^{*}$ |
| $XY$, $\operatorname{adj}X\,Y$, $XY^{\dagger}$, $\operatorname{adj}X\,Y^{\dagger}$ | the four words |
| $\tfrac12\operatorname{Tr}$ | the scalar part of a product |
| $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$ | the Gram matrix of the plain bilinear form |
| $O_4(\mathbb{C})$ | the isometry group of the trace pairing |

## Further Reading

- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the four products
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the four forms and their norms
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the symmetrisation
- [$M_2(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm](m2c-representation-trace-determinant-and-the-biquaternion-norm.html), for the trace and the determinant
- [$M_2(\mathbb{C})$ Representation : The Conjugations and the Adjoints](m2c-representation-the-conjugations-and-the-adjoints.html), for the two involutions
- [Bilinear Forms](bilinear-forms.html), [Hermitian Forms and Unitary Geometry](hermitian-forms-and-unitary-geometry.html)
