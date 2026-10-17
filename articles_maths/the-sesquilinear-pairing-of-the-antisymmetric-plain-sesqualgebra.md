# __The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra__

## Introduction

The vector space $\mathbb{B}$ carries the Hermitian form $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu\overline{Q_\mu}$ of *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*, and the operation of the block has values in the vector subspace, so the form can be applied to the values. This article reads the two pairings that result: the **sesqui-trilinear pairing** $\langle\tilde P\diamond\tilde Q,\tilde Q_3\rangle_{*}$, $\mathbb{C}$-linear in the first argument and conjugate-linear in the second and the third, and the **quadratic form** $\langle\tilde P\diamond\tilde Q,\tilde P\diamond\tilde Q\rangle_{*}$ of the value with itself, which is the square of the value read by the form. Around the two it computes the trace form, which vanishes and is checked here and not assumed, the Gram matrix of the block on the basis pairs, which has rank three and a radical of dimension thirteen, and the space of the forms $\beta$ that are invariant under the block in the sense $\beta(\tilde P\diamond\tilde Q,\tilde Q_3)=-\overline{\beta(\tilde P,\tilde Q\diamond\tilde Q_3)}$, which is one-complex-dimensional and spanned by the scalar-slot form, so that the invariance of $\langle\cdot,\cdot\rangle_{*}$ itself fails.

Two structural facts organise the reading. The first is the compatibility of the block with the sesquilinear sandwich of the row, $S_{\tilde P,\tilde Q}(\tilde Q_1)=\tilde P\tilde Q_1^{*}\tilde Q^{*}$ of *The Sesquilinear Sandwich on the Biquaternioid*: the left operator of the block is the **vector part** of the sandwich with second parameter $e_t$, which is the left multiplication of the general plain sesqualgebra, and the sandwich with the two parameters equal is that left multiplication followed by the right multiplication. The second is the positivity: on the values the form $\langle\cdot,\cdot\rangle_{*}$ is positive definite, its vanishing is exactly the vanishing of the value, and the set of the values that the form cannot separate is therefore the single value $0$. No length, no distance and no limit enters either reading; the form is algebraic throughout, and the positivity that is used is the positivity of the diagonal $\langle\tilde Q,\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ on the ordered real part.

The setting and the notation are those of *Introduction to the Antisymmetric Plain Sesqualgebra*; the product that is split is *Introduction to the General Plain Sesqualgebra*; the general construction of the two parts is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*; the form $\langle\cdot,\cdot\rangle_{*}$, its positivity and its cone are *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*; the sandwich and its operators are *The Sesquilinear Sandwich on the Biquaternioid* and *The Adjoint of the Sesquilinear Sandwich on the Biquaternioid*; the left multiplication of the row is *The Left and Right Multiplications of the Biquaternioid Sesqualgebra*; the trace form and the four pairings of the algebra are *Comparison Between the Four General Products* and *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*; and the remarkable subspaces are *Introduction to the Remarkable Subspaces*.

**Conventions.** As in the two articles above: $\tilde Q=Q_te_t+\vec Q$, $\overline{\vec Q}$ the coefficientwise conjugate of the vector part, $(\vec P,\overline{\vec R})=\sum_{\mu\in\{x,y,z\}}P_\mu\overline{R_\mu}$ the Hermitian pairing of the vector parts, $(\vec P,\vec R)=\sum_{\mu\in\{x,y,z\}}P_\mu R_\mu$ the complex bilinear one, and $[\vec P,\vec Q,\vec R]$ the complex trilinear scalar triple product $(\vec P\times\vec Q,\vec R)$.

## The Pairing with the Form

**Theorem (the pairing).** For all biquaternions,

$$
H\bigl(\tilde P\diamond\tilde Q,\tilde Q_3\bigr)
=-P_t\,(\overline{\vec Q},\overline{\vec R})+\overline{Q_t}\,(\vec P,\overline{\vec R})-[\vec P,\overline{\vec Q},\overline{\vec R}],
$$

a map that is additive in each argument, $\mathbb{C}$-linear in $\tilde P$, and conjugate-linear in $\tilde Q$ and in $\tilde Q_3$.

*Proof.* Since the value $\tilde P\diamond\tilde Q$ is pure vector, only the vector part of $\tilde Q_3$ contributes and $\langle\tilde P\diamond\tilde Q,\tilde Q_3\rangle_{*}=\sum_{\mu\in\{x,y,z\}}(\tilde P\diamond\tilde Q)_\mu\overline{R_\mu}$. Substituting the coordinate rule of the block and distributing the sum gives the three terms: the first is $-P_t\sum_{\mu\in\{x,y,z\}}\overline{Q_\mu}\overline{R_\mu}=-P_t(\overline{\vec Q},\overline{\vec R})$, the second is $\overline{Q_t}\sum_{\mu\in\{x,y,z\}}P_\mu\overline{R_\mu}=\overline{Q_t}(\vec P,\overline{\vec R})$, and the third is $-\sum_{\mu\in\{x,y,z\}}(\vec P\times\overline{\vec Q})_\mu\overline{R_\mu}=-[\vec P,\overline{\vec Q},\overline{\vec R}]$. The parities are the parities of the three scalar rules of the product.

**Corollary (the centre in the third argument drops).** The pairing depends on $\tilde Q_3$ through its vector part alone, $\langle\tilde P\diamond\tilde Q,\tilde Q_3\rangle_{*}=\langle\tilde P\diamond\tilde Q,\mathrm{Vect}(\tilde Q_3)\rangle_{*}$, since the value is pure vector. In the first argument the centre is active: at $\tilde P=\lambda e_t$ the pairing is $-\lambda(\overline{\vec Q},\overline{\vec R})$, and it vanishes for every $\tilde Q_3$ exactly when $\vec Q=0$, that is when $\tilde Q$ is central.

**Corollary (the value with itself).** For all biquaternions,

$$
H\bigl(\tilde P\diamond\tilde Q,\tilde P\diamond\tilde Q\bigr)=\sum_{\mu\in\{x,y,z\}}\bigl\lvert(\tilde P\diamond\tilde Q)_\mu\bigr\rvert^{2},
$$

which is a nonnegative real number, equal to zero exactly when $\tilde P\diamond\tilde Q=0$. The form is therefore **positive definite on the values**: the block has no isotropic value off $0$, and the radical of the restriction of $\langle\cdot,\cdot\rangle_{*}$ to the image is trivial.

*Proof.* The first display is the definition of $\langle\cdot,\cdot\rangle_{*}$ on a pure-vector element; the sum of the three squares of the moduli of the components is nonnegative by the positivity of the square of a real number, and vanishes exactly when the three components vanish.

**Remark (the norm of the value is an element).** The quantity $\langle\tilde P\diamond\tilde Q,\tilde P\diamond\tilde Q\rangle_{*}$ is the form at the two equal arguments, an element of the ordered real part and not a length; it is the algebraic square of the value, and it is the same quantity that the positivity theory of *Positivity and the Hermitian Cone of the Biquaternioid Algebra with Hermitian Adjoint* attaches to the element $\tilde P\diamond\tilde Q$. The multiplicative element norm of the value, $\tilde Q\tilde Q^{*}$ and its $\diamond$-companion, is a different object, and the two are separated as everywhere in the corpus.

## The Trace Form

**Proposition (the trace form vanishes).** For all biquaternions,

$$
\mathrm{Sc}\bigl(\tilde P\diamond\tilde Q\bigr)=0 .
$$

The **trace form** of the block, which is the scalar part of its multiplication, is therefore identically zero, and it is checked here by the computation and not assumed from the shape of the coordinate rule.

*Proof.* The coordinate rule gives $\tilde P\diamond\tilde Q=-P_t\overline{\vec Q}+\overline{Q_t}\vec P-\vec P\times\overline{\vec Q}$, each of whose three terms is a vector part; the scalar part of a vector part is zero.

**Remark (the comparison with the row).** In the symmetric half of the same row the trace form is the whole multiplication, $\mathrm{Sc}(\mathrm{SPS}(\tilde P,\tilde Q))=\langle\tilde P,\tilde Q\rangle_{*}$, and the rank-one structure of the block follows from it; here the trace form is the zero form, and the block contributes nothing to the scalar part of the algebra. The two halves are the two extreme cases of the general statement of *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, §*The Symmetrisation and the Antisymmetrisation*, where the symmetric half carries the whole scalar form and the antisymmetric half carries none.

## The Gram Matrix on the Basis Pairs

**Definition.** The **basis pairs** are the sixteen pairs $(e_I,e_J)$ of the $\mathbb{C}$-basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, and the **Gram matrix** of the block on the basis pairs is the Hermitian matrix

$$
G_{(I,J),(K,L)}=H\bigl(e_I\diamond e_J,\;e_K\diamond e_L\bigr),
$$

whose entries are computed from the basis table of *Introduction to the Antisymmetric Plain Sesqualgebra* and the form. The **radical** of $G$ is the set of the complex combinations of the values $e_I\diamond e_J$ that the form cannot separate from zero.

**Proposition (rank three, radical thirteen).** The sixteen values $e_I\diamond e_J$ span the vector subspace $\mathrm{Vect}(\mathbb{B})$, of complex dimension three. The Gram matrix therefore has rank three, and its radical has complex dimension thirteen.

*Proof.* The values are the columns and the rows of the basis table: the column of $e_t$ is $-e_J$ and reaches all three vector units, so the span contains $\mathrm{Vect}(\mathbb{B})$, and since every value is a vector part the span is exactly $\mathrm{Vect}(\mathbb{B})$, of dimension three. The Gram matrix of a set of vectors has rank the dimension of their span, by the non-degeneracy of the form $\langle\cdot,\cdot\rangle_{*}$; hence rank three and radical dimension $16-3=13$.

**Remark (the radical is the span of the dependencies).** The radical is not a subspace of the space but a subspace of the space of the sixteen formal pairs: it is the module of the linear relations among the values, and the single value $0$ is the only element of $\mathrm{Vect}(\mathbb{B})$ that the form cannot separate from zero. The Gram matrix is therefore the form read on the sixteen operations of the basis, and its rank three is the statement that those sixteen operations generate a three-dimensional image and no more.

## The Invariance Forms

**Definition.** A sesquilinear form $\beta:\mathbb{B}\times\mathbb{B}\to\mathbb{C}$ is **invariant** under the block when

$$
\beta\bigl(\tilde P\diamond\tilde Q,\tilde Q_3\bigr)=-\overline{\beta\bigl(\tilde P,\tilde Q\diamond\tilde Q_3\bigr)}
$$

for all $\tilde P,\tilde Q,\tilde Q_3$. The sign and the conjugation are the sign and the conjugation of the operation, and the condition is the exact analogue of the invariance $\beta(\tilde P\tilde Q,\tilde Q_3)=\beta(\tilde P,\tilde Q\tilde Q_3)$ of an invariant form of an associative product.

**Theorem (the space of the invariants, and the degeneracy).** The space of the forms $\beta$ satisfying the invariance is one-complex-dimensional, spanned by

$$
\beta(\tilde Q_1,\tilde Q_2)=Q_{1t}\overline{Q_{2t}},
$$

the form that reads the two scalar parts. On that form the invariance holds **degenerately**: both members vanish identically, because the scalar part of every value of the block is zero. The form $\langle\cdot,\cdot\rangle_{*}$ itself is **not** invariant.

*Proof.* Write $\beta(\tilde Q_1,\tilde Q_2)=\sum_{\mu,\nu}\beta_{\mu\nu}Q_{1\mu}\overline{Q_{2\nu}}$ and impose the condition on the triples of the real basis: the resulting linear system in the sixteen complex coefficients $\beta_{\mu\nu}$ has solution space of complex dimension one, spanned by $\beta_{tt}=1$ and the other coefficients zero. The members vanish on the solution because $\mathrm{Sc}(\tilde P\diamond\tilde Q)=0$ and $\mathrm{Sc}(\tilde Q\diamond\tilde Q_3)=0$. For $\langle\cdot,\cdot\rangle_{*}$ the witness is the triple $(\vec e_x,\vec e_x,e_t)$: on the left $\langle \vec e_x\diamond \vec e_x,e_t\rangle_{*}=\langle 0,e_t\rangle_{*}=0$, on the right $-\overline{\langle \vec e_x,\vec e_x\diamond e_t\rangle_{*}}=-\overline{\langle \vec e_x,\vec e_x\rangle_{*}}=-1$.

**Remark (the invariance is empty).** The space is not empty, but its invariance carries no information: the block annihilates the scalar slot of every value, so any form that reads only the scalar slot satisfies the condition for free. That is the structural difference from the Lie case $\mathrm{APA}=\vec P\times\vec Q$, whose invariant forms are the multiples of the dot product and carry the Killing form of *The Unitary Lie Algebra*; the block has no Jacobi identity and no such carrier, and the computation above is the substitute that its brief asks for: the invariants are computed, they are one-dimensional, and they are degenerate. The vanishing of the trace form of the preceding section is the same phenomenon read at the two equal arguments of a form.

**Remark (the alternating and the symmetric parts).** A sesquilinear form on $\mathbb{B}$ over $(\mathbb{C},\bar{\cdot})$ is not symmetric in the bilinear sense, and the words *symmetric* and *alternating* do not apply to $\beta$ as they apply to a bilinear form; the corpus carries the two conjugate-symmetric readings in *Hermitian and Skew-Hermitian Elements*, where the fixed and the anti-fixed elements of the involution are separated. Here the point is simply that the two readings of the invariant form coincide with the single scalar-slot form, and there is no room for a symmetric/alternating split.

## The Compatibility with the Sandwich

**Definition.** The **sesquilinear sandwich** of *The Sesquilinear Sandwich on the Biquaternioid* is the operator

$$
S_{\tilde P,\tilde Q}(\tilde Q_1)=\tilde P\tilde Q_1^{*}\tilde Q^{*},
$$

conjugate-linear in the middle variable, $\mathbb{C}$-linear in the first parameter and conjugate-linear in the second.

**Theorem (the block is the vector part of the sandwich with $e_t$).** For every biquaternion $\tilde A$,

$$
L^{\diamond}_{\tilde A}=\mathrm{Vect}\circ S_{\tilde A,e_t},\qquad
S_{\tilde A,e_t}(\tilde Q_3)=\tilde A\tilde Q_3^{*}=L^{\diamond}_{\tilde A}(\tilde Q_3)+\langle\tilde A,\tilde Q_3\rangle_{*}\,e_t .
$$

*Proof.* $S_{\tilde A,e_t}(\tilde Q_3)=\tilde A\tilde Q_3^{*}e_t^{*}=\tilde A\tilde Q_3^{*}$, the left multiplication of the sesqualgebra by $\tilde A$, and $\tilde A\tilde Q_3^{*}=\mathrm{Sc}(\tilde A\tilde Q_3^{*})e_t+\mathrm{Vect}(\tilde A\tilde Q_3^{*})=\langle\tilde A,\tilde Q_3\rangle_{*}e_t+L^{\diamond}_{\tilde A}(\tilde Q_3)$.

**Corollary (the two-parameter sandwich).** $S_{\tilde Q,\tilde Q}(\tilde Q_3)=\tilde Q\tilde Q_3^{*}\tilde Q^{*}$ is the composite of the left multiplication by $\tilde Q$ with the right multiplication by $\tilde Q^{*}$,

$$
S_{\tilde Q,\tilde Q}=R_{\tilde Q}\circ S_{\tilde Q,e_t},\qquad
S_{\tilde Q,\tilde Q}(\tilde Q_3)=L^{\diamond}_{\tilde Q}(\tilde Q_3)\,\tilde Q^{*}+\langle\tilde Q,\tilde Q_3\rangle_{*}\,\tilde Q^{*},
$$

so its vector part is the operator of the block followed by the right multiplication by $\tilde Q^{*}$, and its scalar part is the form $\langle\tilde Q,\tilde Q_3\rangle_{*}$ times $\tilde Q^{*}$.

**Remark (the parities agree).** The block's operator $L^{\diamond}_{\tilde A}$ is conjugate-linear, the sandwich $S_{\tilde A,e_t}$ is conjugate-linear in the middle argument, and the right multiplication $R_{\tilde Q}$ is $\mathbb{C}$-linear; the composite two-parameter sandwich is therefore conjugate-linear, as *The Sesquilinear Sandwich on the Biquaternioid* records, and the parity of the composite of two sandwiches is the parity of the product of two conjugate-linear maps, which is linear. The block is the conjugate-linear half of that monoid, and the relation above is the exact place where the operator of the block sits inside it: it is the vector part of the left multiplication, and the scalar part that accompanies it is the form $\langle\tilde A,\cdot\rangle_{*}$.

## The Pairing, the Norm of the Value and the Quadric

**Theorem (the pairing vanishes exactly on the kernel).** For all biquaternions,

$$
H\bigl(\tilde P\diamond\tilde Q,\tilde P\diamond\tilde Q\bigr)=0
\quad\Longleftrightarrow\quad
\tilde P\diamond\tilde Q=0 .
$$

The set of the pairs for which the quadratic form of the block vanishes is therefore the kernel of the operation, and it is not the quadric of the diagonal of *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*: the diagonal asks for the pairs with $\tilde Q=\tilde P$ on which $\mathrm{Vect}(\tilde Q\tilde Q^{*})=0$, while the pairing asks for the pairs on which $\mathrm{Vect}(\tilde P\tilde Q^{*})=0$, and the two conditions are different.

*Proof.* The pairing is the sum of the three squares of the moduli of the components of the value, by the corollary above, and a sum of three squares of moduli vanishes exactly when the three components vanish.

**Remark (the two conditions, compared).** At the diagonal $\tilde P=\tilde Q=\vec e_x+i\vec e_y$ of the introduction the value is $2i\vec e_z\neq0$, so the pairing is positive there; at the pair $(\vec e_x,i\vec e_y)$ the value is $\vec e_x\diamond(i\vec e_y)=\bar{i}(\vec e_x\diamond \vec e_y)=i\vec e_z\neq0$, positive again; at the pair $(\vec e_x,\vec e_x)$ the value is zero and so is the pairing. The quadric of the diagonal is the section $\tilde P=\tilde Q$ of the kernel of the block, and the pairing is its positive-definite carrier.

## The Restriction to the Remarkable Subspaces

The remarkable subspaces are $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_t,ie_t\}$, $\mathrm{Vect}(\mathbb{B})=\mathrm{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z,i\vec e_x,i\vec e_y,i\vec e_z\}$, $\mathbb{H}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_t,\vec e_x,\vec e_y,\vec e_z\}$, $i\mathbb{H}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{ie_t,i\vec e_x,i\vec e_y,i\vec e_z\}$, $\mathbb{M}_+=\mathrm{span}_{\mathbb{R}}\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$ and $\mathbb{M}_-=\mathrm{span}_{\mathbb{R}}\{ie_t,\vec e_x,\vec e_y,\vec e_z\}$, by *Introduction to the Remarkable Subspaces*. The pairing is read on each; the values of the block lie in $\mathrm{Vect}(\mathbb{B})$, so the restrictions differ only through the two arguments and the vector part of the third.

- **On the centre.** For $\tilde P=\lambda e_t$ the value is the vector $-\lambda\overline{\vec Q}$, and the pairing with a central $\tilde Q_3$ vanishes for every $\tilde Q$, since the third argument is central and the corollary above drops it. The restriction in which the third argument is central is therefore the zero form, as it must be for a block whose values are vector.
- **On the vector subspace.** For all three arguments in $\mathrm{Vect}(\mathbb{B})$ the two scalar coefficients $P_t,Q_t$ vanish, and the pairing reduces to the single term $- [\vec P,\overline{\vec Q},\overline{\vec R}]$, the triple product of the vector parts, which is the complexification of the alternating triple product of the real vector triple; the values span $\mathrm{Vect}(\mathbb{B})$, of dimension three, by the Gram computation.
- **On the quaternion and anti-quaternion subspaces.** On the real span $\mathbb{H}_{\mathbb{B}}$ the coefficientwise conjugation is the identity on the coefficients, the pairing reads $-P_t(\vec Q,\vec R)+Q_t(\vec P,\vec R)-[\vec P,\vec Q,\vec R]$, and it is **definite on the values**: the block on the real part is a cross product, whose pairing with itself is the sum of three real squares. On $i\mathbb{H}_{\mathbb{B}}$, with $\tilde P=ip_te_t+i\vec p$, $\tilde Q=iq_te_t+i\vec q$ and $\tilde Q_3=ir_te_t+i\vec r$ for real $p_t,q_t,r_t$ and real vectors $\vec p,\vec q,\vec r$, the pairing is the purely imaginary number $i\bigl(p_t(\vec q,\vec r)-q_t(\vec p,\vec r)+[\vec p,\vec q,\vec r]\bigr)$, and it is again definite on the values.
- **On the Hermitian and anti-Hermitian subspaces.** Write the arguments of $\mathbb{M}_+$ as $\tilde P=P_te_t+i\vec p$, $\tilde Q=Q_te_t+i\vec q$, $\tilde Q_3=R_te_t+i\vec r$, with $P_t,Q_t,R_t$ real and $\vec p,\vec q,\vec r$ real vectors. Then the pairing is complex,

$$
\langle\tilde P\diamond\tilde Q,\tilde Q_3\rangle_{*}=P_t(\vec q,\vec r)+Q_t(\vec p,\vec r)+i\,[\vec p,\vec q,\vec r],
$$

with the two real mixed terms in the real part and the triple product in the imaginary part. On $\mathbb{M}_-$, with the arguments $ip_te_t+\vec p$, $iq_te_t+\vec q$, $ir_te_t+\vec r$, the same computation gives the mirror

$$
\langle\tilde P\diamond\tilde Q,\tilde Q_3\rangle_{*}=-[\vec p,\vec q,\vec r]-i\bigl(p_t(\vec q,\vec r)+q_t(\vec p,\vec r)\bigr),
$$

so the two halves exchange the two mixed terms and the triple product. In both cases the diagonal $\langle\tilde Q\diamond\tilde Q,\tilde Q\diamond\tilde Q\rangle_{*}$ is nonnegative on every element and vanishes exactly where the diagonal value vanishes, that is on the quadric $\tilde Q\diamond\tilde Q=0$ of the preceding article.

**Remark (the table of the remarkable subspaces).** The restrictions are the pairing read on the remarkable subspaces; because the block is pure vector, the third argument is read through its vector part alone, and every restriction is read on the value through the positive definite form. The restriction that vanishes identically is the one whose third argument is central, and on the other five the diagonal $\langle\tilde P\diamond\tilde Q,\tilde P\diamond\tilde Q\rangle_{*}$ vanishes exactly on the pairs whose value vanishes. The comparison with the same remarkable subspaces read by the other forms of the row is *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*; the subspace-by-subspace reading of the operation itself, distinct from the pairing, is *Remarkable Subspaces under the Antisymmetric Plain Sesqualgebra of Biquaternions*, below in this block.

## Summary

The pairing of the block with the Hermitian form is $\langle\tilde P\diamond\tilde Q,\tilde Q_3\rangle_{*}=-P_t(\overline{\vec Q},\overline{\vec R})+\overline{Q_t}(\vec P,\overline{\vec R})-[\vec P,\overline{\vec Q},\overline{\vec R}]$, $\mathbb{C}$-linear in the first argument and conjugate-linear in the second and the third; the block is pure vector, so the centre of the third argument drops, and on the values the form is positive definite, $\langle\tilde P\diamond\tilde Q,\tilde P\diamond\tilde Q\rangle_{*}=0$ exactly when $\tilde P\diamond\tilde Q=0$. The trace form vanishes identically, checked by computation, and the block contributes nothing to the scalar part of the row; the Gram matrix on the sixteen basis pairs has rank three and radical of dimension thirteen, because the values span the vector subspace. The invariant forms $\beta(\tilde P\diamond\tilde Q,\tilde Q_3)=-\overline{\beta(\tilde P,\tilde Q\diamond\tilde Q_3)}$ form a one-complex-dimensional space spanned by the scalar-slot form $Q_{1t}\overline{Q_{2t}}$, and their invariance is degenerate, both members vanishing with the scalar part of the block; the form $\langle\cdot,\cdot\rangle_{*}$ itself is not invariant, with the witness $(\vec e_x,\vec e_x,e_t)$. The block is the vector part of the sesquilinear sandwich with second parameter $e_t$, which is the left multiplication of the row, and the two-parameter sandwich is that left multiplication followed by the right multiplication. On the remarkable subspaces the pairing is read on the value through the positive definite form, the centre of the third argument is dead, and the restriction that vanishes identically is the one whose third argument is central.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$ | the Hermitian form of *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* |
| $\langle\tilde P\diamond\tilde Q,\tilde Q_3\rangle_{*}$ | the sesqui-trilinear pairing of the block with the form |
| $\langle\tilde P\diamond\tilde Q,\tilde P\diamond\tilde Q\rangle_{*}$ | the quadratic form of the value, positive definite |
| $\mathrm{Sc}(\tilde P\diamond\tilde Q)=0$ | the trace form of the block, identically zero |
| $G_{(I,J),(K,L)}=\langle e_I\diamond e_J,e_K\diamond e_L\rangle_{*}$ | the Gram matrix on the basis pairs, rank three |
| $\beta(\tilde P\diamond\tilde Q,\tilde Q_3)=-\overline{\beta(\tilde P,\tilde Q\diamond\tilde Q_3)}$ | the invariance of a form under the block |
| $Q_{1t}\overline{Q_{2t}}$ | the unique invariant form up to a scalar, degenerate |
| $S_{\tilde P,\tilde Q}(\tilde Q_1)=\tilde P\tilde Q_1^{*}\tilde Q^{*}$ | the sesquilinear sandwich of the row |
| $L^{\diamond}_{\tilde A}=\mathrm{Vect}\circ S_{\tilde A,e_t}$ | the operator of the block as the vector part of the left multiplication |

## Further Reading

- *Introduction to the Antisymmetric Plain Sesqualgebra* (`articles_maths/introduction-to-the-antisymmetric-plain-sesqualgebra.md`), for the operation, the basis table and the trace-form statement
- *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-vector-part-of-the-square-and-the-jacobi-failure-of-the-antisymmetric-plain-sesqualgebra.md`), for the quadric of the diagonal, which the kernel of this article's pairing contains as the diagonal section
- *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-a-sesqualgebra-product.md`), for the scalar form of the two halves, of which the trace form here is the vanishing extreme
- *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternioid-c-space.md`), for the form $\langle\cdot,\cdot\rangle_{*}$, its positivity, its trace and its cone
- *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternioid-c-space.md`) and *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the four forms of the chapter read side by side
- *The Sesquilinear Sandwich on the Biquaternioid* (`articles_maths/the-sesquilinear-sandwich-on-the-biquaternioid.md`) and *The Adjoint of the Sesquilinear Sandwich on the Biquaternioid* (`articles_maths/the-adjoint-of-the-sesquilinear-sandwich-on-the-biquaternioid.md`), for the sandwich, its multiplication table and its adjoint
- *The Left and Right Multiplications of the Biquaternioid Sesqualgebra* (`articles_maths/the-left-and-right-multiplications-of-the-biquaternioid-sesqualgebra.md`), for the left multiplication of which the operator of the block is the vector part
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the remarkable subspaces and their bases
