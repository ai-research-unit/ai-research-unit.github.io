# __The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra__

## Introduction

The vector space $\mathbb{B}$ carries the Hermitian form $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu\overline{Q_\mu}$ of *Biquaternion Norm and Invertibility*, and the operation of the block has values in the vector subspace, so the form can be applied to the values. This article reads the two pairings that result: the **sesqui-trilinear pairing** $H(\tilde P\diamond\tilde Q,\tilde R)$, $\mathbb{C}$-linear in the first argument and conjugate-linear in the second and the third, and the **quadratic form** $H(\tilde P\diamond\tilde Q,\tilde P\diamond\tilde Q)$ of the value with itself, which is the square of the value read by the form. Around the two it computes the trace form, which vanishes and is checked here and not assumed, the Gram matrix of the block on the basis pairs, which has rank three and a radical of dimension thirteen, and the space of the forms $\beta$ that are invariant under the block in the sense $\beta(\tilde P\diamond\tilde Q,\tilde R)=-\overline{\beta(\tilde P,\tilde Q\diamond\tilde R)}$, which is one-complex-dimensional and spanned by the scalar-slot form, so that the invariance of $H$ itself fails.

Two structural facts organise the reading. The first is the compatibility of the block with the sesquilinear sandwich of the row, $S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X^{*}\tilde Q^{*}$ of *The Sesquilinear Sandwich on the Biquaternions*: the left operator of the block is the **vector part** of the sandwich with second parameter $e_0$, which is the left multiplication of the general plain sesqualgebra, and the sandwich with the two parameters equal is that left multiplication followed by the right multiplication. The second is the positivity: on the values the form $H$ is positive definite, its vanishing is exactly the vanishing of the value, and the set of the values that the form cannot separate is therefore the single value $0$. No length, no distance and no limit enters either reading; the form is algebraic throughout, and the positivity that is used is the positivity of the diagonal $H(\tilde Q,\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2}$ on the ordered real part.

The setting and the notation are those of *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions*; the product that is split is *Introduction to the General Plain Sesqualgebra of Biquaternions*; the general construction of the two parts is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*; the form $H$, its positivity and its cone are *Biquaternion Norm and Invertibility*; the sandwich and its operators are *The Sesquilinear Sandwich on the Biquaternions* and *The Adjoint of the Sesquilinear Sandwich on the Biquaternions*; the left multiplication of the row is *The Left and Right Multiplications of the Biquaternion Sesqualgebra*; the trace form and the four pairings of the algebra are *Comparison Between the Four General Products* and *The Four Pairings of the Biquaternion Algebra*; and the six subspaces are *Introduction to the Six Subspaces*.

**Conventions.** As in the two articles above: $\tilde Q=Q_0e_0+\mathbf{Q}$, $\overline{\mathbf{Q}}$ the coefficientwise conjugate of the vector part, $(\mathbf{P},\overline{\mathbf{R}})=\sum_kP_k\overline{R_k}$ the Hermitian pairing of the vector parts, $(\mathbf{P},\mathbf{R})=\sum_kP_kR_k$ the complex bilinear one, and $[\mathbf{P},\mathbf{Q},\mathbf{R}]$ the complex trilinear scalar triple product $(\mathbf{P}\times\mathbf{Q},\mathbf{R})$.

## The Pairing with the Form

**Theorem (the pairing).** For all biquaternions,

$$
H\bigl(\tilde P\diamond\tilde Q,\tilde R\bigr)
=-P_0\,(\overline{\mathbf{Q}},\overline{\mathbf{R}})+\overline{Q_0}\,(\mathbf{P},\overline{\mathbf{R}})-[\mathbf{P},\overline{\mathbf{Q}},\overline{\mathbf{R}}],
$$

a map that is additive in each argument, $\mathbb{C}$-linear in $\tilde P$, and conjugate-linear in $\tilde Q$ and in $\tilde R$.

*Proof.* Since the value $\tilde P\diamond\tilde Q$ is pure vector, only the vector part of $\tilde R$ contributes and $H(\tilde P\diamond\tilde Q,\tilde R)=\sum_k(P\diamond Q)_k\overline{R_k}$. Substituting the coordinate rule of the block and distributing the sum gives the three terms: the first is $-P_0\sum_k\overline{Q_k}\overline{R_k}=-P_0(\overline{\mathbf{Q}},\overline{\mathbf{R}})$, the second is $\overline{Q_0}\sum_kP_k\overline{R_k}=\overline{Q_0}(\mathbf{P},\overline{\mathbf{R}})$, and the third is $-\sum_k(\mathbf{P}\times\overline{\mathbf{Q}})_k\overline{R_k}=-[\mathbf{P},\overline{\mathbf{Q}},\overline{\mathbf{R}}]$. The parities are the parities of the three scalar rules of the product. $\square$

**Corollary (the centre in the third argument drops).** The pairing depends on $\tilde R$ through its vector part alone, $H(\tilde P\diamond\tilde Q,\tilde R)=H(\tilde P\diamond\tilde Q,\mathrm{Vect}(\tilde R))$, since the value is pure vector. In the first argument the centre is active: at $\tilde P=\lambda e_0$ the pairing is $-\lambda(\overline{\mathbf{Q}},\overline{\mathbf{R}})$, and it vanishes for every $\tilde R$ exactly when $\mathbf{Q}=0$, that is when $\tilde Q$ is central.

**Corollary (the value with itself).** For all biquaternions,

$$
H\bigl(\tilde P\diamond\tilde Q,\tilde P\diamond\tilde Q\bigr)=\sum_{k=1}^{3}\bigl\lvert(P\diamond Q)_k\bigr\rvert^{2},
$$

which is a nonnegative real number, equal to zero exactly when $\tilde P\diamond\tilde Q=0$. The form is therefore **positive definite on the values**: the block has no isotropic value off $0$, and the radical of the restriction of $H$ to the image is trivial.

*Proof.* The first display is the definition of $H$ on a pure-vector element; the sum of the three squares of the moduli of the components is nonnegative by the positivity of the square of a real number, and vanishes exactly when the three components vanish. $\square$

**Remark (the norm of the value is an element).** The quantity $H(\tilde P\diamond\tilde Q,\tilde P\diamond\tilde Q)$ is the diagonal of the form, an element of the ordered real part and not a length; it is the algebraic square of the value, and it is the same quantity that the positivity theory of *Biquaternion Norm and Invertibility* attaches to the element $\tilde P\diamond\tilde Q$. The multiplicative element norm of the value, $\tilde Q\tilde Q^{*}$ and its $\diamond$-companion, is a different object, and the two are separated as everywhere in the corpus.

## The Trace Form

**Proposition (the trace form vanishes).** For all biquaternions,

$$
\mathrm{Sc}\bigl(\tilde P\diamond\tilde Q\bigr)=0 .
$$

The **trace form** of the block, which is the scalar part of its multiplication, is therefore identically zero, and it is checked here by the computation and not assumed from the shape of the coordinate rule.

*Proof.* The coordinate rule gives $\tilde P\diamond\tilde Q=-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}$, each of whose three terms is a vector part; the scalar part of a vector part is zero. $\square$

**Remark (the comparison with the row).** In the symmetric half of the same row the trace form is the whole multiplication, $\mathrm{Sc}(\mathrm{SPS}(\tilde P,\tilde Q))=H(\tilde P,\tilde Q)$, and the rank-one structure of the block follows from it; here the trace form is the zero form, and the block contributes nothing to the scalar part of the algebra. The two halves are the two extreme cases of the general statement of *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, §*The Symmetrisation and the Antisymmetrisation*, where the symmetric half carries the whole scalar form and the antisymmetric half carries none.

## The Gram Matrix on the Basis Pairs

**Definition.** The **basis pairs** are the sixteen pairs $(e_I,e_J)$ of the $\mathbb{C}$-basis $(e_0,e_1,e_2,e_3)$, and the **Gram matrix** of the block on the basis pairs is the Hermitian matrix

$$
G_{(I,J),(K,L)}=H\bigl(e_I\diamond e_J,\;e_K\diamond e_L\bigr),
$$

whose entries are computed from the basis table of *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions* and the form. The **radical** of $G$ is the set of the complex combinations of the values $e_I\diamond e_J$ that the form cannot separate from zero.

**Proposition (rank three, radical thirteen).** The sixteen values $e_I\diamond e_J$ span the vector subspace $\mathrm{Vect}(\mathbb{B})$, of complex dimension three. The Gram matrix therefore has rank three, and its radical has complex dimension thirteen.

*Proof.* The values are the columns and the rows of the basis table: the column of $e_0$ is $-e_J$ and reaches all three vector units, so the span contains $\mathrm{Vect}(\mathbb{B})$, and since every value is a vector part the span is exactly $\mathrm{Vect}(\mathbb{B})$, of dimension three. The Gram matrix of a set of vectors has rank the dimension of their span, by the non-degeneracy of the form $H$; hence rank three and radical dimension $16-3=13$. $\square$

**Remark (the radical is the span of the dependencies).** The radical is not a subspace of the space but a subspace of the space of the sixteen formal pairs: it is the module of the linear relations among the values, and the single value $0$ is the only element of $\mathrm{Vect}(\mathbb{B})$ that the form cannot separate from zero. The Gram matrix is therefore the form read on the sixteen operations of the basis, and its rank three is the statement that those sixteen operations generate a three-dimensional image and no more.

## The Invariance Forms

**Definition.** A sesquilinear form $\beta:\mathbb{B}\times\mathbb{B}\to\mathbb{C}$ is **invariant** under the block when

$$
\beta\bigl(\tilde P\diamond\tilde Q,\tilde R\bigr)=-\overline{\beta\bigl(\tilde P,\tilde Q\diamond\tilde R\bigr)}
$$

for all $\tilde P,\tilde Q,\tilde R$. The sign and the conjugation are the sign and the conjugation of the operation, and the condition is the exact analogue of the invariance $\beta(\tilde P\tilde Q,\tilde R)=\beta(\tilde P,\tilde Q\tilde R)$ of an invariant form of an associative product.

**Theorem (the space of the invariants, and the degeneracy).** The space of the forms $\beta$ satisfying the invariance is one-complex-dimensional, spanned by

$$
\beta(\tilde X,\tilde Y)=X_0\overline{Y_0},
$$

the form that reads the two scalar parts. On that form the invariance holds **degenerately**: both members vanish identically, because the scalar part of every value of the block is zero. The form $H$ itself is **not** invariant.

*Proof.* Write $\beta(\tilde X,\tilde Y)=\sum_{\mu,\nu}\beta_{\mu\nu}X_\mu\overline{Y_\nu}$ and impose the condition on the triples of the real basis: the resulting linear system in the sixteen complex coefficients $\beta_{\mu\nu}$ has solution space of complex dimension one, spanned by $\beta_{00}=1$ and the other coefficients zero. The members vanish on the solution because $\mathrm{Sc}(\tilde P\diamond\tilde Q)=0$ and $\mathrm{Sc}(\tilde Q\diamond\tilde R)=0$. For $H$ the witness is the triple $(e_1,e_1,e_0)$: on the left $H(e_1\diamond e_1,e_0)=H(0,e_0)=0$, on the right $-\overline{H(e_1,e_1\diamond e_0)}=-\overline{H(e_1,e_1)}=-1$. $\square$

**Remark (the invariance is empty).** The space is not empty, but its invariance carries no information: the block annihilates the scalar slot of every value, so any form that reads only the scalar slot satisfies the condition for free. That is the structural difference from the Lie case $\mathrm{APA}=\mathbf{P}\times\mathbf{Q}$, whose invariant forms are the multiples of the dot product and carry the Killing form of *The Unitary Lie Algebra*; the block has no Jacobi identity and no such carrier, and the computation above is the substitute that its brief asks for: the invariants are computed, they are one-dimensional, and they are degenerate. The vanishing of the trace form of the preceding section is the same phenomenon read on the diagonal of a form.

**Remark (the alternating and the symmetric parts).** A sesquilinear form on $\mathbb{B}$ over $(\mathbb{C},\bar{\cdot})$ is not symmetric in the bilinear sense, and the words *symmetric* and *alternating* do not apply to $\beta$ as they apply to a bilinear form; the corpus carries the two conjugate-symmetric readings in *Hermitian and Skew-Hermitian Elements*, where the fixed and the anti-fixed elements of the involution are separated. Here the point is simply that the two readings of the invariant form coincide with the single scalar-slot form, and there is no room for a symmetric/alternating split.

## The Compatibility with the Sandwich

**Definition.** The **sesquilinear sandwich** of *The Sesquilinear Sandwich on the Biquaternions* is the operator

$$
S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X^{*}\tilde Q^{*},
$$

conjugate-linear in the middle variable, $\mathbb{C}$-linear in the first parameter and conjugate-linear in the second.

**Theorem (the block is the vector part of the sandwich with $e_0$).** For every biquaternion $\tilde A$,

$$
L^{\diamond}_{\tilde A}=\mathrm{Vect}\circ S_{\tilde A,e_0},\qquad
S_{\tilde A,e_0}(\tilde R)=\tilde A\tilde R^{*}=L^{\diamond}_{\tilde A}(\tilde R)+H(\tilde A,\tilde R)\,e_0 .
$$

*Proof.* $S_{\tilde A,e_0}(\tilde R)=\tilde A\tilde R^{*}e_0^{*}=\tilde A\tilde R^{*}$, the left multiplication of the sesqualgebra by $\tilde A$, and $\tilde A\tilde R^{*}=\mathrm{Sc}(\tilde A\tilde R^{*})e_0+\mathrm{Vect}(\tilde A\tilde R^{*})=H(\tilde A,\tilde R)e_0+L^{\diamond}_{\tilde A}(\tilde R)$. $\square$

**Corollary (the two-parameter sandwich).** $S_{\tilde Q,\tilde Q}(\tilde R)=\tilde Q\tilde R^{*}\tilde Q^{*}$ is the composite of the left multiplication by $\tilde Q$ with the right multiplication by $\tilde Q^{*}$,

$$
S_{\tilde Q,\tilde Q}=R_{\tilde Q}\circ S_{\tilde Q,e_0},\qquad
S_{\tilde Q,\tilde Q}(\tilde R)=L^{\diamond}_{\tilde Q}(\tilde R)\,\tilde Q^{*}+H(\tilde Q,\tilde R)\,\tilde Q^{*},
$$

so its vector part is the operator of the block followed by the right multiplication by $\tilde Q^{*}$, and its scalar part is the form $H(\tilde Q,\tilde R)$ times $\tilde Q^{*}$.

**Remark (the parities agree).** The block's operator $L^{\diamond}_{\tilde A}$ is conjugate-linear, the sandwich $S_{\tilde A,e_0}$ is conjugate-linear in the middle argument, and the right multiplication $R_{\tilde Q}$ is $\mathbb{C}$-linear; the composite two-parameter sandwich is therefore conjugate-linear, as *The Sesquilinear Sandwich on the Biquaternions* records, and the parity of the composite of two sandwiches is the parity of the product of two conjugate-linear maps, which is linear. The block is the conjugate-linear half of that monoid, and the relation above is the exact place where the operator of the block sits inside it: it is the vector part of the left multiplication, and the scalar part that accompanies it is the form $H(\tilde A,\cdot)$.

## The Pairing, the Norm of the Value and the Quadric

**Theorem (the pairing vanishes exactly on the kernel).** For all biquaternions,

$$
H\bigl(\tilde P\diamond\tilde Q,\tilde P\diamond\tilde Q\bigr)=0
\quad\Longleftrightarrow\quad
\tilde P\diamond\tilde Q=0 .
$$

The set of the pairs for which the quadratic form of the block vanishes is therefore the kernel of the operation, and it is not the quadric of the diagonal of *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*: the diagonal asks for the pairs with $\tilde Q=\tilde P$ on which $\mathrm{Vect}(\tilde Q\tilde Q^{*})=0$, while the pairing asks for the pairs on which $\mathrm{Vect}(\tilde P\tilde Q^{*})=0$, and the two conditions are different.

*Proof.* The pairing is the sum of the three squares of the moduli of the components of the value, by the corollary above, and a sum of three squares of moduli vanishes exactly when the three components vanish. $\square$

**Remark (the two conditions, compared).** At the diagonal $\tilde P=\tilde Q=e_1+ie_2$ of the introduction the value is $2ie_3\neq0$, so the pairing is positive there; at the pair $(e_1,ie_2)$ the value is $e_1\diamond(ie_2)=\bar{i}(e_1\diamond e_2)=ie_3\neq0$, positive again; at the pair $(e_1,e_1)$ the value is zero and so is the pairing. The quadric of the diagonal is the section $\tilde P=\tilde Q$ of the kernel of the block, and the pairing is its positive-definite carrier.

## The Restriction to the Six Subspaces

The six distinguished subspaces are $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$, $\mathrm{Vect}(\mathbb{B})=\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3,ie_1,ie_2,ie_3\}$, $\mathbb{H}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,e_1,e_2,e_3\}$, $i\mathbb{H}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{ie_0,ie_1,ie_2,ie_3\}$, $\mathbb{M}_+=\mathrm{span}_{\mathbb{R}}\{e_0,ie_1,ie_2,ie_3\}$ and $\mathbb{M}_-=\mathrm{span}_{\mathbb{R}}\{ie_0,e_1,e_2,e_3\}$, by *Introduction to the Six Subspaces*. The pairing is read on each; the values of the block lie in $\mathrm{Vect}(\mathbb{B})$, so the restrictions differ only through the two arguments and the vector part of the third.

- **On the centre.** For $\tilde P=\lambda e_0$ the value is the vector $-\lambda\overline{\mathbf{Q}}$, and the pairing with a central $\tilde R$ vanishes for every $\tilde Q$, since the third argument is central and the corollary above drops it. The restriction in which the third argument is central is therefore the zero form, as it must be for a block whose values are vector.
- **On the vector subspace.** For all three arguments in $\mathrm{Vect}(\mathbb{B})$ the two scalar coefficients $P_0,Q_0$ vanish, and the pairing reduces to the single term $- [\mathbf{P},\overline{\mathbf{Q}},\overline{\mathbf{R}}]$, the triple product of the vector parts, which is the complexification of the alternating triple product of the real vector triple; the values span $\mathrm{Vect}(\mathbb{B})$, of dimension three, by the Gram computation.
- **On the quaternion and anti-quaternion subspaces.** On the real span $\mathbb{H}_{\mathbb{B}}$ the coefficientwise conjugation is the identity on the coefficients, the pairing reads $-P_0(\mathbf{Q},\mathbf{R})+Q_0(\mathbf{P},\mathbf{R})-[\mathbf{P},\mathbf{Q},\mathbf{R}]$, and it is **definite on the values**: the block on the real part is a cross product, whose pairing with itself is the sum of three real squares. On $i\mathbb{H}_{\mathbb{B}}$, with $\tilde P=ip_0e_0+i\mathbf{p}$, $\tilde Q=iq_0e_0+i\mathbf{q}$ and $\tilde R=ir_0e_0+i\mathbf{r}$ for real $p_0,q_0,r_0$ and real vectors $\mathbf{p},\mathbf{q},\mathbf{r}$, the pairing is the purely imaginary number $i\bigl(p_0(\mathbf{q},\mathbf{r})-q_0(\mathbf{p},\mathbf{r})+[\mathbf{p},\mathbf{q},\mathbf{r}]\bigr)$, and it is again definite on the values.
- **On the Hermitian and anti-Hermitian subspaces.** Write the arguments of $\mathbb{M}_+$ as $\tilde P=P_0e_0+i\mathbf{p}$, $\tilde Q=Q_0e_0+i\mathbf{q}$, $\tilde R=R_0e_0+i\mathbf{r}$, with $P_0,Q_0,R_0$ real and $\mathbf{p},\mathbf{q},\mathbf{r}$ real vectors. Then the pairing is complex,

$$
H(\tilde P\diamond\tilde Q,\tilde R)=P_0(\mathbf{q},\mathbf{r})+Q_0(\mathbf{p},\mathbf{r})+i\,[\mathbf{p},\mathbf{q},\mathbf{r}],
$$

with the two real mixed terms in the real part and the triple product in the imaginary part. On $\mathbb{M}_-$, with the arguments $ip_0e_0+\mathbf{p}$, $iq_0e_0+\mathbf{q}$, $ir_0e_0+\mathbf{r}$, the same computation gives the mirror

$$
H(\tilde P\diamond\tilde Q,\tilde R)=-[\mathbf{p},\mathbf{q},\mathbf{r}]-i\bigl(p_0(\mathbf{q},\mathbf{r})+q_0(\mathbf{p},\mathbf{r})\bigr),
$$

so the two halves exchange the two mixed terms and the triple product. In both cases the diagonal $H(\tilde Q\diamond\tilde Q,\tilde Q\diamond\tilde Q)$ is nonnegative on every element and vanishes exactly where the diagonal value vanishes, that is on the quadric $\tilde Q\diamond\tilde Q=0$ of the preceding article.

**Remark (the table of the six).** The six restrictions are the pairing read on the six subspaces; because the block is pure vector, the third argument is read through its vector part alone, and every restriction is read on the value through the positive definite form. The restriction that vanishes identically is the one whose third argument is central, and on the other five the diagonal $H(\tilde P\diamond\tilde Q,\tilde P\diamond\tilde Q)$ vanishes exactly on the pairs whose value vanishes. The comparison with the same six subspaces read by the other forms of the row is *The Four Pairings of the Biquaternion Algebra*; the subspace-by-subspace reading of the operation itself, distinct from the pairing, is *The Six Subspaces under the Antisymmetric Plain Sesqualgebra of Biquaternions*, below in this block.

## Summary

The pairing of the block with the Hermitian form is $H(\tilde P\diamond\tilde Q,\tilde R)=-P_0(\overline{\mathbf{Q}},\overline{\mathbf{R}})+\overline{Q_0}(\mathbf{P},\overline{\mathbf{R}})-[\mathbf{P},\overline{\mathbf{Q}},\overline{\mathbf{R}}]$, $\mathbb{C}$-linear in the first argument and conjugate-linear in the second and the third; the block is pure vector, so the centre of the third argument drops, and on the values the form is positive definite, $H(\tilde P\diamond\tilde Q,\tilde P\diamond\tilde Q)=0$ exactly when $\tilde P\diamond\tilde Q=0$. The trace form vanishes identically, checked by computation, and the block contributes nothing to the scalar part of the row; the Gram matrix on the sixteen basis pairs has rank three and radical of dimension thirteen, because the values span the vector subspace. The invariant forms $\beta(\tilde P\diamond\tilde Q,\tilde R)=-\overline{\beta(\tilde P,\tilde Q\diamond\tilde R)}$ form a one-complex-dimensional space spanned by the scalar-slot form $X_0\overline{Y_0}$, and their invariance is degenerate, both members vanishing with the scalar part of the block; the form $H$ itself is not invariant, with the witness $(e_1,e_1,e_0)$. The block is the vector part of the sesquilinear sandwich with second parameter $e_0$, which is the left multiplication of the row, and the two-parameter sandwich is that left multiplication followed by the right multiplication. On the six subspaces the pairing is read on the value through the positive definite form, the centre of the third argument is dead, and the restriction that vanishes identically is the one whose third argument is central.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})$ | the Hermitian form of *Biquaternion Norm and Invertibility* |
| $H(\tilde P\diamond\tilde Q,\tilde R)$ | the sesqui-trilinear pairing of the block with the form |
| $H(\tilde P\diamond\tilde Q,\tilde P\diamond\tilde Q)$ | the quadratic form of the value, positive definite |
| $\mathrm{Sc}(\tilde P\diamond\tilde Q)=0$ | the trace form of the block, identically zero |
| $G_{(I,J),(K,L)}=H(e_I\diamond e_J,e_K\diamond e_L)$ | the Gram matrix on the basis pairs, rank three |
| $\beta(\tilde P\diamond\tilde Q,\tilde R)=-\overline{\beta(\tilde P,\tilde Q\diamond\tilde R)}$ | the invariance of a form under the block |
| $X_0\overline{Y_0}$ | the unique invariant form up to a scalar, degenerate |
| $S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X^{*}\tilde Q^{*}$ | the sesquilinear sandwich of the row |
| $L^{\diamond}_{\tilde A}=\mathrm{Vect}\circ S_{\tilde A,e_0}$ | the operator of the block as the vector part of the left multiplication |

## Further Reading

- *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-sesqualgebra-of-biquaternions.md`), for the operation, the basis table and the trace-form statement
- *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-vector-part-of-the-square-and-the-jacobi-failure-of-the-antisymmetric-plain-sesqualgebra.md`), for the quadric of the diagonal, which the kernel of this article's pairing contains as the diagonal section
- *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-a-sesqualgebra-product.md`), for the scalar form of the two halves, of which the trace form here is the vanishing extreme
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the form $H$, its positivity, its trace and its cone
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`) and *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the four forms of the chapter read side by side
- *The Sesquilinear Sandwich on the Biquaternions* (`articles_maths/the-sesquilinear-sandwich-on-the-biquaternions.md`) and *The Adjoint of the Sesquilinear Sandwich on the Biquaternions* (`articles_maths/the-adjoint-of-the-sesquilinear-sandwich-on-the-biquaternions.md`), for the sandwich, its multiplication table and its adjoint
- *The Left and Right Multiplications of the Biquaternion Sesqualgebra* (`articles_maths/the-left-and-right-multiplications-of-the-biquaternion-sesqualgebra.md`), for the left multiplication of which the operator of the block is the vector part
- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six distinguished subspaces and their bases
