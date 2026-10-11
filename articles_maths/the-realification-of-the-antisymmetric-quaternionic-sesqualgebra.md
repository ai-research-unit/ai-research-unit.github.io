# __The Realification of the Antisymmetric Quaternionic Sesqualgebra__

## Introduction

The Antisymmetric Quaternionic Sesqualgebra is one of the twelve algebraic structures that the biquaternion space $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ carries, the structure carried by the product
$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}\bigr)=\mathbf{P}\times\overline{\mathbf{Q}},
$$
the operation $\mathrm{AQS}$ of *The 12 Products of the Biquaternion Complex Space*; it is the only one of the twelve whose value is the conjugate cross product alone. Its complex reading is *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions*. Read over $\mathbb{R}$ the same product on the same set is an $\mathbb{R}$-algebra on the eight-dimensional real space $\mathbb{R}^8$, and this article owns that real reading.

The general construction is not repeated here. The realification of a vector space, of a linear map and of a form, the doubling of the dimension, the complex structure $J$ and the table of the four effects are *The Realification and the Effect of the Change of Scalars*; This article gives what is specific to this product: its real bilinear reading with its two images, the law of its second slot over the centre, the realification of the pairing with the Krein form and the absence of a form of its own, the real part with the count of ten and the subalgebras the passage adds, and its real operators with their trace form.

## The Product Read over $\mathbb{R}$

**Theorem.** The product is $\mathbb{R}$-bilinear, so that $\mathbb{B}$ is an $\mathbb{R}$-algebra, in the broad sense of a module with a bilinear multiplication, on the eight-dimensional real space
$$
\mathbb{R}^8=\operatorname{span}_{\mathbb{R}}\{e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3\}.
$$
In that algebra conjugate-alternation holds, the Jacobi identity fails, there is no unit, and the scalar part vanishes.

*Proof.* The product is $\mathbb{C}$-sesquilinear over $\mathbb{C}$, hence additive in each argument and linear over $\mathbb{R}$ in each, hence $\mathbb{R}$-bilinear; this is §*The Effect on the Twelve Algebraic Structures* of *The Realification and the Effect of the Change of Scalars*. The dimension is the doubling of the complex basis. The four properties are statements about the ring and are the element theory of the block, quoted from *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions*: conjugate-alternation $\tilde P\diamond\tilde Q=-\overline{\tilde Q\diamond\tilde P}$; the Jacobi failure with the witness $(e_1,e_1,ie_2)$, whose cyclic sum is $-2ie_2$, the only one of the twelve whose failure is invisible on the quaternion subspace and needs an element outside it; the absence of a unit on either side; and the vanishing of the scalar part, the antisymmetrisation killing the scalar part of the general product of its family.

**The ring theory does not move.** Every statement about the ring — written with the addition, the product, $e_0$ and quantification over the elements alone — has the same truth value in the two readings, by the dictionary of the same article. The element theory of the block is therefore read unchanged over $\mathbb{R}$: the idempotent set is the origin alone; every nonzero element is a two-sided zero divisor, so the zero-divisor set is the whole space with the origin removed; the nilpotent indices are two and four and never three; and the group of units is empty. What the real reading adds is the shape of the product and its operators; what it changes of the block is nothing but the field and the dimension. The three statements are the content of *Zero Divisors of the Antisymmetric Quaternionic Sesqualgebra*, *Norm and Invertibility in the Antisymmetric Quaternionic Sesqualgebra* and *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Quaternionic Sesqualgebra*.

**The two images.** The product is pure vector valued, and its values span the vector subspace,
$$
\mathrm{im}(\diamond)=\mathrm{Vect}(\mathbb{B})=\operatorname{span}_{\mathbb{C}}\{e_1,e_2,e_3\},\qquad\text{of real dimension }6,
$$
while the square map has the smaller image
$$
\{\tilde X\diamond\tilde X\}=\operatorname{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\},\qquad\text{of real dimension }3,
$$
the real three-plane that the complex reading describes as the purely imaginary real vectors. The diagonal itself is the conjugate cross product of the vector part with itself,
$$
\tilde Q\diamond\tilde Q=\mathbf{Q}\times\overline{\mathbf{Q}},
$$
equal to $-2i\,\mathbf{a}\times\mathbf{b}$ when $\mathbf{Q}=\mathbf{a}+i\mathbf{b}$ with $\mathbf{a},\mathbf{b}$ real, hence to $-2ie_3$ at $e_1+ie_2$, and it vanishes exactly on the complex multiples of the real directions. The criterion for a square root of an element is the membership of the real three-plane above, a real condition that survives the passage verbatim; it is *Square Roots of a General Element in the Antisymmetric Quaternionic Sesqualgebra*, and the diagonal, its cone and the Jacobi witness are *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra*.

## The Second Slot and the Centre

Over $\mathbb{C}$ the product is $\mathbb{C}$-sesquilinear: it is linear in the first slot and conjugate-linear in the second, because the second slot is read through the star ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, whose restriction to the centre is $i\mapsto-i$, the Galois conjugation of $\mathbb{C}$ over $\mathbb{R}$. The structure is therefore a sesqualgebra over $(\mathbb{C},\varsigma)$ with $\varsigma={}^{*}$ on the centre, and not an algebra.

Read over $\mathbb{R}$, the involution disappears: the only automorphism of $\mathbb{R}$ is the identity, and a sesquilinear law with the identity involution is a bilinear law. The product is therefore an **$\mathbb{R}$-algebra**, and its second slot is $\mathbb{C}_{\mathbb{B}}$-conjugate-linear, by §*The Realification of a Linear Map* of *The Realification and the Effect of the Change of Scalars*. The passage therefore **changes the kind** of this product — sesqualgebra over $\mathbb{C}$, algebra over $\mathbb{R}$ — and the distinction migrates from the field to the centre.

**Theorem (the two block shapes).** The left multiplication $L_{\tilde X}:\tilde Y\mapsto\tilde X\diamond\tilde Y$ is conjugate-linear over $\mathbb{C}$,
$$
L_{\tilde X}J=-JL_{\tilde X},
$$
and in the real basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ its matrix has the anticommuting block shape
$$
\begin{pmatrix}A&B\\ B&-A\end{pmatrix}.
$$
The right multiplication $R_{\tilde X}:\tilde Y\mapsto\tilde Y\diamond\tilde X$ is $\mathbb{C}$-linear over $\mathbb{C}$,
$$
R_{\tilde X}J=JR_{\tilde X},
$$
and its matrix has the commuting block shape
$$
\begin{pmatrix}A&-B\\ B&A\end{pmatrix}.
$$

*Proof.* The second-slot criterion of §*The Realification of a Linear Map* of *The Realification and the Effect of the Change of Scalars*, applied to the product read with the centre $\mathbb{C}_{\mathbb{B}}$ in place of $\mathbb{C}$: a conjugate-linear law gives a conjugate-linear left multiplication, of the anticommuting shape, and a linear one gives a linear right multiplication, of the commuting shape. In coordinates, $L_{\tilde X}$ sends the coefficient $i$ of the argument to $-i$ in front of the value while $R_{\tilde X}$ keeps it. Computed on the real basis, on the $64$ basis pairs.

The two slots of the one product thus carry opposite linearities, and the two block shapes are the two halves of it: the block is the instance of the twelve in which the left multiplication is $\mathbb{R}$-linear and not $\mathbb{C}$-linear, which is the point of the real reading. The matrix, the rank and the kernel of the two operators are the content of *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*; this article keeps the two shapes and the trace form that follows.

## The Realified Form

The block carries no degree-two form of its own. Its scalar part vanishes — it is the antisymmetrisation of the general product of its family, and the antisymmetrisation kills the scalar part — so the third column of the table of *The 12 Products of the Biquaternion Complex Space* gives it the zero form, and the four realified signatures $(4,4)$, $(4,4)$, $(8,0)$, $(2,6)$ of *The Realification of the Four Forms* do not include it. What does realify is the **pairing** of its values with the Krein form of its row. The form
$$
K(\tilde P,\tilde Q)=\mathrm{Sc}\bigl(\tilde P^{\natural}\tilde Q^{*}\bigr)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}=P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}}),\qquad\varepsilon=(1,-1,-1,-1),
$$
is Hermitian of complex inertia $(1,3)$, and a Hermitian form realifies by the second rule of §*The Realification of a Form* of the general article: its realification $K_{\mathbb{R}}=\operatorname{Re}K$ is a real symmetric bilinear form of signature
$$
(2,6)
$$
on $\mathbb{R}^8$, preserved by the complex structure,
$$
K_{\mathbb{R}}(J\tilde P,J\tilde Q)=+K_{\mathbb{R}}(\tilde P,\tilde Q).
$$
The sign is the rule of the Hermitian kind: a Hermitian form doubles its inertia to $(2p,2q)$ and is preserved by $J$. The contrast is with the bilinear kind: the two $\mathbb{C}$-bilinear forms of the corpus, $B$ and $N$ of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*, realify to the split signature $(4,4)$ and are **reversed** by $J$, and the other Hermitian form $H$ realifies to $(8,0)$.

**Theorem (the pairing realifies).** The block is $K$-orthogonal to its own second argument,
$$
K(\tilde X\diamond\tilde Y,\tilde Y)=0,
$$
for all biquaternions, and the realification reads the same identity on $\mathbb{R}^8$. On the image, which is the vector subspace, the form is negative definite, of signature $(0,6)$, while on the centre it is positive definite, of signature $(2,0)$; the values of the block lie on the negative definite row of $K_{\mathbb{R}}$ and
$$
K_{\mathbb{R}}(\tilde X\diamond\tilde Y,\tilde X\diamond\tilde Y)=-\lvert\tilde X\diamond\tilde Y\rvert^{2}\le0,
$$
vanishing exactly when the value vanishes.

*Proof.* The identity is the specificities law of *The Specificities of the Antisymmetric Quaternionic Sesqualgebra*, a statement about the ring and so unchanged; the pairing is read on the image and on the centre in *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra*, where the Gram matrix of the sixteen basis pairs and the restrictions of the form are computed. The signatures follow from the sign vector $\varepsilon$, negative on the three vector coordinates and positive on the scalar one. The realified identity is the remark that $\operatorname{Re}$ is $\mathbb{R}$-linear.

**The invariant forms do not move.** A form $\beta$ is invariant under the block when
$$
\beta\bigl(\tilde P\diamond\tilde Q,\tilde R\bigr)=-\overline{\beta\bigl(\tilde P,\tilde Q\diamond\tilde R\bigr)}
$$
for all $\tilde P,\tilde Q,\tilde R$, and in each of the four homogeneous classes the invariant forms are a central line, of real dimension two, spanned by the central form $\beta_0(\tilde P,\tilde Q)=P_0\overline{Q_0}$ or $P_0Q_0$ according to the class; the enlarged class of all real-bilinear invariants has real dimension eight, the direct sum of the four central lines. Every invariant is central and the passage adds nothing to that space: the invariance condition is a statement about the ring and the realification changes neither the space nor its dimension. The whole of the computation is *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra*.

## The Real Part and the Subalgebras

On the quaternion subspace
$$
\mathbb{H}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{e_0,e_1,e_2,e_3\},
$$
of real dimension four, the block coincides with the antisymmetric plain algebra: for two real vector parts the conjugation is the identity, so
$$
\tilde P\diamond\tilde Q=\mathbf{P}\times\mathbf{Q}=\mathrm{APA}(\tilde P,\tilde Q),
$$
the ordinary cross product of the real vector parts. The coincidence holds because the conjugation of a real vector is the identity, and it disappears as soon as one argument leaves $\mathbb{H}_{\mathbb{B}}$ for a direction in $i\mathbb{R}^{3}$.

**The count of ten.** The coincidence, with its symmetric companion — the symmetric quaternionic product coinciding with the symmetric plain sesquilinear product on $\mathbb{H}_{\mathbb{B}}$ — is the reason the comment of *The 12 Products of the Biquaternion Complex Space* records a **count of ten**. On the four-dimensional real part the twelve operations reduce to ten, because the pair $(\mathrm{AQS},\mathrm{APA})$ and the pair $(\mathrm{SQA},\mathrm{SPS})$ each collapse to one operation there, the remaining eight staying distinct. The caution of the corpus applies: a computation restricted to the real part can hide the obstruction that separates the two members of a coincident pair, and twelve distinct operations require the full eight-dimensional real space.

**Proposition (the closure criterion).** A real subspace $W$ of $\mathbb{R}^8$ is a subalgebra of the block exactly when $\tilde P\diamond\tilde Q\in W$ for all $\tilde P,\tilde Q\in W$. Every value of the block lies in the vector subspace, so the condition reads
$$
\tilde P\diamond\tilde Q\in W\cap\mathrm{Vect}(\mathbb{B})\qquad\text{for all }\tilde P,\tilde Q\in W:
$$
a subspace is closed exactly when its intersection with the vector subspace receives all the values of its pairs.

*Proof.* The first sentence is the definition. For the second, the value is $\mathbf{P}\times\overline{\mathbf{Q}}$, a pure vector, so the membership of the value in $W$ is the membership of the value in $W\cap\mathrm{Vect}(\mathbb{B})$.

**The notable subalgebras.** A subalgebra of the complex reading is a complex subspace closed under the product, of even real dimension; over $\mathbb{R}$ odd dimensions appear, and the block exhibits them at the smallest sizes.

| subalgebra | real dimension | type |
|---|---|---|
| $\mathbb{R}x$ with $x\diamond x=0$ | $1$ | zero product; among them $\mathbb{R}e_0$ and $\mathbb{R}ie_0$ |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{R}\{e_0,ie_0\}$ | $2$ | zero product, the centre |
| $\mathbb{R}\{e_1,e_2,e_3\}$ | $3$ | the ordinary cross product of real vectors, $\cong\mathfrak{so}(3,\mathbb{R})$ |
| $\mathbb{H}_{\mathbb{B}}=\mathbb{R}\{e_0,e_1,e_2,e_3\}$ | $4$ | the antisymmetric plain algebra |
| $\mathbb{M}_-=\mathbb{R}\{ie_0,e_1,e_2,e_3\}$ | $4$ | the ordinary cross product of the real vector parts |
| $\mathbb{R}\{e_0,e_1,e_2,e_3,ie_0\}$ | $5$ | the quaternion subspace with the scalar imaginary |
| $\mathrm{Vect}(\mathbb{B})=\mathbb{R}\{e_1,e_2,e_3,ie_1,ie_2,ie_3\}$ | $6$ | the image of the product |
| $\mathbb{R}\{e_0,e_1,e_2,e_3,ie_1,ie_2,ie_3\}$ | $7$ | the image with the real scalar |
| $\mathbb{R}^8$ | $8$ | the whole algebra |

The table lists the notable members and is not the whole lattice. The one-dimensional case is already a family: the line $\mathbb{R}x$ is closed exactly when $x\diamond x=0$, by the criterion, that is exactly when the vector part of $x$ is a complex multiple of a real vector, a cone of real dimension six; the lines through $e_0$ and through $ie_0$ are two of its members, and the lines through the imaginary vectors and through the sums $e_1+ie_1$ are others. The two-dimensional case contains the plane $\mathbb{R}\{e_1,ie_1\}$ as well as the centre, a zero-product plane outside the centre because $e_1\diamond ie_1=0$. The remaining dimensions of the table carry at least the listed members, of which the three-dimensional one is the ordinary cross product of the real vector directions, closed because $e_1\diamond e_2=e_3$, and it has no complex counterpart, since the smallest complex subspace containing it has dimension six.

The anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ and the Hermitian subspace $\mathbb{M}_+=\mathbb{R}\{e_0,ie_1,ie_2,ie_3\}$, both of real dimension four, are **not** closed: for two imaginary elements the value is a real vector, and the witness is $ie_1\diamond ie_2=e_3$, which leaves $i\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_+$ because their vector directions are imaginary. The four stable subspaces and the two failing ones, with the uniform reason, are *Remarkable Subspaces under the Antisymmetric Quaternionic Sesqualgebra of Biquaternions*.

## The Real Operators

**Definition.** The left and the right multiplications by an element are the maps
$$
L_{\tilde X}:\tilde Y\mapsto\tilde X\diamond\tilde Y=\mathbf{X}\times\overline{\mathbf{Y}},
\qquad
R_{\tilde X}:\tilde Y\mapsto\tilde Y\diamond\tilde X=\mathbf{Y}\times\overline{\mathbf{X}},
$$
and over $\mathbb{R}$ they are $\mathbb{R}$-linear endomorphisms of $\mathbb{R}^8$.

**Theorem (the class and the traces).** The left multiplication is conjugate-linear over $\mathbb{C}$, of the anticommuting block shape and of vanishing real trace, the two diagonal blocks being opposite; the right multiplication is $\mathbb{C}$-linear, of the commuting block shape and of vanishing trace. For a non-central element both have real rank $4$ and nullity $4$, the kernel of the left multiplication is the complex plane
$$
\ker L_{\tilde X}=\mathbb{C}\overline{\mathbf{X}}\oplus\mathbb{C}e_0,\qquad\text{of real dimension }4,
$$
and its image is the complex plane of the values orthogonal to the vector part in the complex bilinear dot, $(\mathbf{W},\mathbf{X})=0$, the equation $\tilde X\diamond\tilde R=\tilde W$ being solvable exactly there; for a central element both multiplications vanish.

*Proof.* The class and the two shapes are the theorem of §*The Second Slot and the Centre*; the vanishing of the trace of a conjugate-linear map is the opposite diagonal blocks. The rank, the kernel and the image are computed in *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra* and in *Zero Divisors of the Antisymmetric Quaternionic Sesqualgebra*, on the $64$ basis pairs; the vanishing of the trace of $R$ is the trace of a $\mathbb{C}$-linear map, twice the real part of its complex trace, and the complex trace is zero because $e_j\mapsto e_j\times\overline{\mathbf{X}}$ has the two skew blocks of the cross product alone.

**Theorem (the operator trace form in the two readings).** For all $\tilde P,\tilde Q$,
$$
\kappa(\tilde P,\tilde Q)=\operatorname{Tr}_{\mathbb{C}}\bigl(L_{\tilde P}L_{\tilde Q}\bigr)=-2\,(\mathbf{P},\overline{\mathbf{Q}})=2\bigl(K(\tilde P,\tilde Q)-P_0\overline{Q_0}\bigr),
$$
the composition being $\mathbb{C}$-linear because it is the product of two conjugate-linear maps; $\kappa$ is a Hermitian form of complex inertia $(0,3)$ with the centre as radical, and its realification is the **real operator trace form**
$$
\kappa_{\mathbb{R}}(\tilde P,\tilde Q)=\operatorname{Re}\kappa(\tilde P,\tilde Q)=-2\operatorname{Re}\,(\mathbf{P},\overline{\mathbf{Q}}),
\qquad
\operatorname{Tr}_{\mathbb{R}}\bigl(L_{\tilde P}L_{\tilde Q}\bigr)=2\,\kappa_{\mathbb{R}}(\tilde P,\tilde Q),
$$
a real symmetric bilinear form of real rank $6$ and signature $(0,6)$, negative semidefinite with the centre as radical, equal to twice the restriction of $K_{\mathbb{R}}$ to the vector subspace.

*Proof.* The composition $L_{\tilde P}L_{\tilde Q}$ is the map $\tilde R\mapsto\mathbf{P}\times\overline{\mathbf{Q}\times\overline{\mathbf{R}}}$, and the two conjugations cancel, so it is $\mathbb{C}$-linear and has a complex trace; on the complex basis $e_0,e_1,e_2,e_3$ its matrix has trace $-2(\mathbf{P},\overline{\mathbf{Q}})$, computed on the $64$ basis pairs. The real trace of a $\mathbb{C}$-linear endomorphism is twice the real part of its complex trace, which is the factor $2$ and the same factor that relates the two readings of the trace of the left multiplication of the general plain product, $\operatorname{Tr}_{\mathbb{R}}(L_{\tilde P})=8\operatorname{Re}\mathrm{Sc}(\tilde P)$ against $\operatorname{Tr}_{\mathbb{C}}(L_{\tilde P})=4\,\mathrm{Sc}(\tilde P)$. The Hermitian form $-2(\mathbf{P},\overline{\mathbf{Q}})$ has the three vector coordinates negative and the scalar coordinate absent, hence inertia $(0,3)$ and radical the centre; a Hermitian form of inertia $(0,3)$ realifies to $(0,6)$ by the second rule of the realification of a form, and on the vector subspace $\kappa_{\mathbb{R}}=2K_{\mathbb{R}}$.

**The element trace form, and the distinction.** The **element** trace form of the block,
$$
\mathrm{Tr}\bigl(\tilde P\diamond\tilde Q\bigr)=2\,\mathrm{Sc}\bigl(\tilde P\diamond\tilde Q\bigr),
$$
vanishes identically, because the block is pure vector; the vanishing is the form side of the absence of a unit and of the pure-vector image, and it is *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra*. The operator trace form $\kappa_{\mathbb{R}}$ does not vanish: the two objects differ, one being the trace of the product and the other the trace of the composition of the two left multiplications, and only the second is a nondegenerate form on the vector subspace. The adjoints with respect to $K$, the derivations (of real dimension $7$) and the structure group of the block are *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*, whose statements are of the real-linear kind and hold unchanged.

**The general construction.** The reading is the instance of the operator trace form of the real biquaternion algebra. For the plain product that form is
$$
\tau(\tilde P,\tilde Q)=\operatorname{Tr}\bigl(L_{\tilde P}L_{\tilde Q}\bigr)=8\operatorname{Re}\langle\tilde P,\tilde Q\rangle,\qquad \operatorname{Tr}(L_{\tilde X})=8\operatorname{Re}\mathrm{Sc}(\tilde X),
$$
real symmetric of signature $(4,4)$, with the general factor $2$ between the real and the complex trace, $8=2\cdot4$; the same factor appears here as $\kappa_{\mathbb{R}}=\operatorname{Re}\kappa$ of $\operatorname{Tr}_{\mathbb{R}}=2\operatorname{Re}\operatorname{Tr}_{\mathbb{C}}$. What the block changes is the left multiplication, conjugate-linear in place of linear: the signature $(4,4)$ becomes the negative semidefinite $(0,6)$ and the trivial radical becomes the centre. the block shares the reality of its operator theory and not the Cartan structure, its operator calculus being conjugate-linear at every step.

## Summary

Read over $\mathbb{R}$ the Antisymmetric Quaternionic Sesqualgebra is the same product on the same elements, an $\mathbb{R}$-algebra on $\mathbb{R}^8$ in which conjugate-alternation holds, the Jacobi identity fails with the witness $(e_1,e_1,ie_2)$, there is no unit, and the scalar part vanishes. Its ring theory is unchanged: the idempotent set the origin, every nonzero element a zero divisor, the nilpotent indices two and four, the group of units empty. Its values span the six real dimensions of the vector subspace, and its square spans the three real dimensions of $i\mathbb{R}^{3}$. Its second slot is $\mathbb{C}_{\mathbb{B}}$-conjugate-linear, so the left multiplication is conjugate-linear over the centre with the anticommuting block shape and the right multiplication is linear with the commuting one. The block carries no degree-two form; it pairs with the realified Krein form $K_{\mathbb{R}}$ of signature $(2,6)$, preserved by $J$, on which it is orthogonal to its own second argument and on whose negative definite vector row its values lie, and its invariants are the four central lines, of real dimension eight in the enlarged class. On the real part it is the antisymmetric plain algebra, and the collapse of the two coincident pairs there is the count of ten of the twelve operations, and the passage adds the odd-dimensional subalgebras, among them the three-dimensional ordinary cross product of the real directions. The operators of a non-central element have rank four and vanish in trace, and the operator trace form $\kappa_{\mathbb{R}}(\tilde P,\tilde Q)=-2\operatorname{Re}(\mathbf{P},\overline{\mathbf{Q}})$ is negative semidefinite of signature $(0,6)$ and radical the centre, distinct from the vanishing element trace form of the block.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}\bigr)=\mathbf{P}\times\overline{\mathbf{Q}}$ | the product of the Antisymmetric Quaternionic Sesqualgebra |
| $\mathbb{R}^8$ | the realification of $\mathbb{B}$, the eight real basis elements $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{R}e_0\oplus\mathbb{R}(ie_0)$ | the centre, the field of scalars $\mathbb{C}$ carried by the ring, of real dimension two |
| $J$ | the complex structure, multiplication by $i$, of square $-1$ |
| $L_{\tilde X}J=-JL_{\tilde X}$, $R_{\tilde X}J=JR_{\tilde X}$ | the conjugate-linear left and the $\mathbb{C}$-linear right multiplication, with the two block shapes |
| $K_{\mathbb{R}}=\operatorname{Re}K$, $(2,6)$ | the realified Krein form; $(0,6)$ on the image, $(2,0)$ on the centre |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_{+}$, $\mathbb{M}_{-}$ | the quaternion, anti-quaternion, Hermitian and anti-Hermitian subspaces |
| $\mathrm{Vect}(\mathbb{B})$, $\mathbb{R}\{e_1,e_2,e_3\}$ | the six-dimensional image of the product and the three-dimensional cross-product subalgebra |
| $\kappa=-2(\mathbf{P},\overline{\mathbf{Q}})=\operatorname{Tr}_{\mathbb{C}}(L_{\tilde P}L_{\tilde Q})$ | the complex operator trace form, Hermitian of inertia $(0,3)$ |
| $\kappa_{\mathbb{R}}=\operatorname{Re}\kappa$, $(0,6)$ | the real operator trace form, radical the centre, distinct from the vanishing element trace form |
| $\tau=\operatorname{Tr}(L_{\tilde P}L_{\tilde Q})$, $(4,4)$ | the operator trace form of the real biquaternion algebra, of the plain product, whose conjugate-linear instance is $\kappa_{\mathbb{R}}$ |

## Further Reading

- *The Realification and the Effect of the Change of Scalars* (`articles_maths/the-realification-and-the-effect-of-the-change-of-scalars.md`), for the general construction, the two rules of the realification of a form, the two block shapes and the table of the four effects.
- *The Realification of the Four Forms* (`articles_maths/the-realification-of-the-four-forms.md`), for the four realified Gram matrices, their signatures, the restrictions to the remarkable subspaces and the realified null cones.
- *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternion-c-space.md`) and *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the four forms $B$, $N$, $H$, $K$, the zero form of the block and the count of ten on the real part.
- *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the complex reading of the product, its class, its element theory and its placement among the twelve.
- *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/the-sesquilinear-pairing-of-the-antisymmetric-quaternionic-sesqualgebra.md`), for the pairing of the values with the Krein form, the invariant central lines and the vanishing element trace form.
- *The Specificities of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/the-specificities-of-the-antisymmetric-quaternionic-sesqualgebra.md`), for the law $K(\tilde X\diamond\tilde Y,\tilde Y)=0$.
- *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/the-conjugate-cross-product-and-the-jacobi-failure-of-the-antisymmetric-quaternionic-sesqualgebra.md`), for the conjugate cross product, the diagonal criterion and the Jacobi witness $(e_1,e_1,ie_2)$, all of which are statements about the ring and hold unchanged over $\mathbb{R}$.
- *Remarkable Subspaces under the Antisymmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-antisymmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the stability on the quaternion subspace and the failure of closure on the anti-quaternion and Hermitian subspaces.
- *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/the-adjoint-operators-of-the-antisymmetric-quaternionic-sesqualgebra.md`), for the matrix, the rank, the kernel and the image of the two multiplications, the adjoint for the Krein form, the derivations and the structure group.
- *Zero Divisors of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/zero-divisors-of-the-antisymmetric-quaternionic-sesqualgebra.md`), *Norm and Invertibility in the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/norm-and-invertibility-in-the-antisymmetric-quaternionic-sesqualgebra.md`) and *Square Roots of a General Element in the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/square-roots-of-a-general-element-in-the-antisymmetric-quaternionic-sesqualgebra.md`), for the element theory read unchanged over $\mathbb{R}$.
