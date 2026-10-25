# __The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra__

## Introduction

The block $\tilde Q_1\diamond\tilde Q_2=\vec Q_1\times\overline{\vec Q_2}$ of *Introduction to the Antisymmetric Quaternionic Sesqualgebra* is pure-vector-valued, so it can be paired with the elements of the space by the Krein form

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}\bigr)=\sum_{\mu}\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}
=Q_{1t}\overline{Q_{2t}}-\sum_{\mu\in\{x,y,z\}}Q_{1\mu}\overline{Q_{2\mu}},\qquad\varepsilon=(1,-1,-1,-1),
$$

the form of *The Krein Norm of the Biquaternion Algebra*, written there $\langle\cdot,\cdot\rangle_{\natural*}$, linear in its first argument and conjugate-linear in its second. This article reads the block against that form: the pairing of a value with a third element, the pairing of a value with itself, the Gram matrix of the sixteen basis pairs with its rank and its radical, the forms $\beta$ invariant under the block, the trace form, and the restriction of the form to the remarkable subspaces with the signs it carries there. The reading is the analogue for the block of the pairings of the two general sesquilinear products and of the block of the plain row, and it is the form side of the multiplication.

The form and its isotropic structure are *The Krein Norm of the Biquaternion Algebra*; the remarkable subspaces are *Introduction to the Remarkable Subspaces*; the product the block splits is *Introduction to the General Quaternionic Sesqualgebra*; the general construction of a sesqualgebra part is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*; and the companion readings of the same form are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra* for the four forms on the remarkable subspaces and *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra* for the plain-row companion of the block. This article owns the pairing itself.

## The Pairing of a Value with a Third Element

**Proposition (the pairing in coordinates).** For all biquaternions,

$$
\boxed{\;
K\bigl(\tilde Q_1\diamond\tilde Q_2,\tilde Q_3\bigr)
=-\sum_{\mu\in\{x,y,z\}}\bigl(\vec Q_1\times\overline{\vec Q_2}\bigr)_\mu\,\overline{Q_{3\mu}}
=-\bigl(\vec Q_1\times\overline{\vec Q_2},\overline{\vec Q_3}\bigr)
\;},
$$

where the bracket on the right is the complex bilinear dot product of the value with the conjugate of the vector part of the third argument.

*Proof.* The value $\vec Q_1\times\overline{\vec Q_2}$ is pure vector, so the scalar term of $\langle\cdot,\cdot\rangle_{\natural*}$ drops and only the three vector terms remain, with the sign $\varepsilon_\mu=-1$ and the conjugation on the third argument.

**Proposition (the self-pairing is non-positive).** For all biquaternions,

$$
\boxed{\;
K\bigl(\tilde Q_1\diamond\tilde Q_2,\tilde Q_1\diamond\tilde Q_2\bigr)
=-\bigl|\vec Q_1\times\overline{\vec Q_2}\bigr|^{2}\le0
\;},
$$

and it vanishes exactly when the value of the block vanishes, that is exactly when $\tilde Q_1\diamond\tilde Q_2=0$.

*Proof.* The self-pairing of a pure vector $\vec V$ is $-\sum_{\mu\in\{x,y,z\}}V_\mu\overline{V_\mu}=-|\vec V|^{2}$, a non-positive real number, and it vanishes exactly when $\vec V=0$.

**Remark (the value on the negative side).** The self-pairing is never positive, and it is strictly negative exactly on the nonzero values of the block. The values of the block lie in the vector subspace, which is the negative definite row of the form, so the block never carries a value on which the form is positive or null except the value zero. The pairing of the block with the form is therefore a map into the negative cone of the form, conjugate-linear in the third argument, and the relation of the block to the norm of its value is the statement $\langle\tilde Q_1\diamond\tilde Q_2,\tilde Q_1\diamond\tilde Q_2\rangle_{\natural*}=-|\tilde Q_1\diamond\tilde Q_2|^{2}$. The paired value is null exactly on the elements of square zero of the block, which are the elements whose vector part lies on the quadric cone of the diagonal of *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra*: the self-pairing vanishes on $\tilde Q_1\diamond\tilde Q_2$ exactly when $\vec Q_1$ and $\overline{\vec Q_2}$ are $\mathbb{C}$-linearly dependent; in particular the diagonal self-pairing $\langle\tilde Q_2\diamond\tilde Q_2,\tilde Q_2\diamond\tilde Q_2\rangle_{\natural*}$ vanishes exactly at the elements whose vector part is a complex multiple of a real vector, which are the square-zero elements of the block, and the self-pairing vanishes for every $\tilde Q_2$ only when $\tilde Q_1$ is central.

## The Gram Matrix on the Basis Pairs

**Proposition (the sixteen values).** The sixteen values $e_\mu\diamond e_\nu$ of the basis pairs are the six signed vector units

$$
\vec e_x\diamond \vec e_y=\vec e_z,\quad \vec e_x\diamond \vec e_z=-\vec e_y,\quad \vec e_y\diamond \vec e_x=-\vec e_z,\quad
\vec e_y\diamond \vec e_z=\vec e_x,\quad \vec e_z\diamond \vec e_x=\vec e_y,\quad \vec e_z\diamond \vec e_y=-\vec e_x,
$$

the ten remaining pairs being zero.

*Proof.* The sixteen products of the basis of the introduction to the block.

**Theorem (the Gram matrix).** The Gram matrix of the block on the sixteen basis pairs, with entries $\langle e_\mu\diamond e_\nu,e_\alpha\diamond e_\beta\rangle_{\natural*}$, has rank $3$ over $\mathbb{C}$, and its radical has complex dimension $13$. Over $\mathbb{R}$ the induced form is negative semidefinite of rank $6$.

*Proof.* The sixteen values span the vector subspace, of complex dimension $3$, and on that subspace the form $\langle\cdot,\cdot\rangle_{\natural*}$ is negative definite, of real signature $(0,6)$ by *The Krein Norm of the Biquaternion Algebra*. The Gram matrix of a non-degenerate form restricted to a spanning set of complex dimension $3$ has rank $3$ over $\mathbb{C}$ and rank $6$ over $\mathbb{R}$; the radical consists of the linear relations among the sixteen values, of complex dimension $16-3=13$.

**Remark (the radical of the Gram matrix).** The radical is spanned by the relations among the sixteen pairs, and it is not the radical of the form, which is zero on the whole algebra. It is the failure of the sixteen pairs to be independent: the ten vanishing pairs and the antisymmetry relations $e_\mu\diamond e_\nu=-e_\nu\diamond e_\mu$ generate it, and the form itself keeps its non-degeneracy on the span of the values. The same phenomenon is the degeneracy of the Gram matrix of a map and not of its form.

## The Invariant Forms of the Block

**Definition.** A form $\beta$ is **invariant under the block** when

$$
\beta\bigl(\tilde Q_1\diamond\tilde Q_2,\tilde Q_3\bigr)=-\overline{\beta\bigl(\tilde Q_1,\tilde Q_2\diamond\tilde Q_3\bigr)}
$$

for all $\tilde Q_1,\tilde Q_2,\tilde Q_3$. The condition is the one of the corpus for a sesquilinear invariant, read with the conjugate of the value because the block is conjugate-linear in its second slot.

**Theorem (the invariant forms form a line).** In each of the four homogeneous classes of forms of the block — complex-bilinear, linear in the first slot and conjugate-linear in the second, conjugate-linear in the first and linear in the second, and conjugate-linear in both — the forms $\beta$ invariant under the block form a space of complex dimension $1$ and real dimension $2$. In every one of the four the space is spanned by the central form

$$
\boxed{\;
\beta_0(\tilde Q_1,\tilde Q_2)=Q_{1t}\overline{Q_{2t}},
\qquad\text{or}\qquad
\beta_0(\tilde Q_1,\tilde Q_2)=Q_{1t}Q_{2t}
\;},
$$

or the corresponding doubly conjugate-linear form according to the class, and it contains no other form of that class.

*Proof.* Write $\beta$ with a coefficient matrix $G$, of sixteen complex entries in the homogeneous classes, and impose the displayed identity on the triples of the **real** basis $e_t,\vec e_x,\vec e_y,\vec e_z,ie_t,i\vec e_x,i\vec e_y,i\vec e_z$, that is on the $8^{3}=512$ real triples. The identity is multilinear over $\mathbb{R}$ and not over $\mathbb{C}$, because the conjugation of the second slot of the block and the conjugations that define the class are not complex-linear; the four-element complex basis of each slot does not suffice, and a check reduced to its $4^{3}=64$ triples reports spurious solutions — the form $i\,(Q_{x}\overline{Q_{2x}}+Q_{y}\overline{Q_{2y}}+Q_{z}\overline{Q_{2z}})$, for instance, passes the $64$ triples and fails the ordinary triple $(\vec e_x,i\vec e_y,\vec e_z)$. The linear system over $\mathbb{R}$ built on the real basis has a solution space of real dimension $2$ in each of the four classes, spanned by the central form above with coefficient $1$ and with coefficient $i$. The computation shows that every solution is supported on the entry $(0,0)$ alone, that is, depends only on the scalar coordinates of the two arguments.

**Remark (the enlarged class is the sum of the four central lines).** If the class is enlarged to all real-bilinear complex-valued forms on the real space, of real dimension $128$, the invariant space has real dimension $8$, the direct sum of the four central lines of the theorem: the forms $a\,Q_{1t}Q_{2t}+b\,Q_{1t}\overline{Q_{2t}}+c\,\overline{Q_{1t}}Q_{2t}+d\,\overline{Q_{1t}}\,\overline{Q_{2t}}$ with $a,b,c,d\in\mathbb{C}$. Every invariant is central, and the enlargement adds the sums of one form of each class and no form outside the four lines. The reason is a vanishing forced on the real-bilinear class. Taking the third argument central in the displayed identity kills the right side and leaves $\beta(\tilde Q_1\diamond\tilde Q_2,\tilde Q_3)=0$ for a central $\tilde Q_3$ and an arbitrary value, so a real-bilinear form vanishes as soon as its first argument is a pure vector and its second is central; taking the first argument central gives the mirror vanishing, on the value that varies in the second slot; and on the pure vectors alone the identity leaves only the zero form. The two scalar coordinates are therefore the only entries that survive.

**Remark (why the invariant is central).** The block has zero scalar part and kills the centre in both slots. Its second slot is conjugate-linear, so the invariance condition carries a conjugate on the swapped value, and the only way a form can survive the three arguments is to read the two scalar coordinates alone: every vector index is carried by the block into the vector subspace, where the minus signs of the form and the conjugations of the slot are incompatible with the invariance. The space is therefore the central line, of complex dimension $1$.

**Remark (the discrepancy of the classes).** In the corpus the natural class of an invariant of a sesquilinear product is the class of that product, and the block is sesquilinear over $(\mathbb{C},\bar{\cdot})$. The computation shows that the space of invariants is the same in the sesquilinear class and in the bilinear class, so the class does not change the answer; and within the sesquilinear class the form is $\beta_0(\tilde Q_1,\tilde Q_2)=Q_{1t}\overline{Q_{2t}}$, which is the central part of the Hermitian form $\langle\cdot,\cdot\rangle_{*}$ and of the Krein form $\langle\cdot,\cdot\rangle_{\natural*}$ alike. The block has no non-degenerate invariant: every invariant is central and therefore has the whole vector subspace in its radical.

**Remark (one invariant and its conjugate).** The two real dimensions of the space are the form $\beta_0$ and the form $i\beta_0$, whose values are the values of $\beta_0$ multiplied by $i$; the two are the real and the imaginary parts of the one complex invariant. The invariant is central-valued, so it is a form on the centre only, and the block contributes to it nothing but the identity of the condition.

## The Trace Form

**Proposition.** The trace form $\tau(\tilde Q_1,\tilde Q_2)=\mathrm{Tr}(\tilde Q_1\diamond\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\diamond\tilde Q_2)$ vanishes identically on the block.

*Proof.* The block is pure vector and the trace of a pure vector is zero; equivalently the scalar part is zero.

**Remark (the block has no trace form).** Of the twelve operations, the ones that carry a non-degenerate trace form are the eight general and symmetric parts, of the two algebras and of the two sesqualgebras alike; the block, being pure vector with a conjugate-linear slot, has none, and it shares that vanishing with the other three antisymmetric parts. The vanishing is the form side of the absence of a unit and of the pure-vector image.

## The Restriction to the Remarkable Subspaces

The form $\langle\cdot,\cdot\rangle_{\natural*}$ is non-degenerate of signature $(2,6)$ on the whole algebra, and its restriction to each of the remarkable subspaces of *Introduction to the Remarkable Subspaces* is diagonal with the signs $\varepsilon$; the restriction table is the one of *Remarkable Subspaces under the General Quaternionic Sesqualgebra*.

| Subspace | Restricted form | Signature |
|---|---|---|
| Centre $\mathbb{C}_{\mathbb{B}}$ | $\lvert Q_{1t}\rvert^{2}$ | $(2,0)$ |
| Vector $\mathrm{Vect}(\mathbb{B})$ | $-\sum_{\mu\in\{x,y,z\}}\lvert Q_{1\mu}\rvert^{2}$ | $(0,6)$ |
| Quaternion $\mathbb{H}_{\mathbb{B}}$ | $q_t^{2}-q_x^{2}-q_y^{2}-q_z^{2}$ | $(1,3)$ |
| Anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | $(q'_t)^{2}-(q'_x)^{2}-(q'_y)^{2}-(q'_z)^{2}$ | $(1,3)$ |
| Hermitian $\mathbb{M}_+$ | $q_t^{2}-(q'_x)^{2}-(q'_y)^{2}-(q'_z)^{2}$ | $(1,3)$ |
| Anti-Hermitian $\mathbb{M}_-$ | $(q'_t)^{2}-q_x^{2}-q_y^{2}-q_z^{2}$ | $(1,3)$ |

**Remark (the row the block reads).** The values of the block lie in the vector subspace, so the pairing of the block reads the **negative definite** row of the table and no other: on the vector subspace the form is $-\lvert\vec V\rvert^{2}$, and the pairing of a value with a third element is the complex bilinear dot product of the value with the conjugate of the vector part of the third element, with the sign $-$ and the conjugation on the third argument. The centre is the positive definite row, which the block does not reach; the four remaining rows are indefinite of signature $(1,3)$ and are reached only through their vector parts. The reading of the block on the remarkable subspaces themselves, with the vanishing on the centre and the failure of closure, is *Remarkable Subspaces under the Antisymmetric Quaternionic Sesqualgebra of Biquaternions*.

## Summary

Read against the Krein form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}$, the block pairs a value with a third element as $\langle\tilde Q_1\diamond\tilde Q_2,\tilde Q_3\rangle_{\natural*}=-(\vec Q_1\times\overline{\vec Q_2},\overline{\vec Q_3})$ and a value with itself as $\langle\tilde Q_1\diamond\tilde Q_2,\tilde Q_1\diamond\tilde Q_2\rangle_{\natural*}=-\lvert\tilde Q_1\diamond\tilde Q_2\rvert^{2}\le0$, so the block takes its values on the negative side of the form and is null there only when the value is zero. The Gram matrix of the sixteen basis pairs has rank $3$ over $\mathbb{C}$ and radical of complex dimension $13$, the values spanning the vector subspace, and the induced form is negative semidefinite of real rank $6$. The forms invariant under the block form a complex line of real dimension 2 in each of the four homogeneous classes of slot types, spanned by the central form $\beta_0(\tilde Q_1,\tilde Q_2)=Q_{1t}\overline{Q_{2t}}$ in the sesquilinear class and by $Q_{1t}Q_{2t}$ in the bilinear class; every invariant of a homogeneous class is central and degenerate on the vector subspace, while the enlarged class of all real-bilinear invariants has real dimension $8$, the direct sum of the four central lines. The trace form vanishes identically. On the remarkable subspaces the pairing reads the negative definite vector row, the block never reaching the positive definite centre.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}$ | the Krein form, linear in the first argument |
| $\langle\tilde Q_1\diamond\tilde Q_2,\tilde Q_3\rangle_{\natural*}$ | the pairing of a value with a third element |
| $\langle\tilde Q_1\diamond\tilde Q_2,\tilde Q_1\diamond\tilde Q_2\rangle_{\natural*}=-\lvert\tilde Q_1\diamond\tilde Q_2\rvert^{2}$ | the self-pairing of a value |
| the sixteen-by-sixteen Gram matrix | rank $3$ over $\mathbb{C}$, radical of complex dimension $13$ |
| $\beta(\tilde Q_1\diamond\tilde Q_2,\tilde Q_3)=-\overline{\beta(\tilde Q_1,\tilde Q_2\diamond\tilde Q_3)}$ | the invariance condition |
| the four homogeneous classes | complex-bilinear, the two mixed sesquilinear, and doubly conjugate-linear |
| $\beta_0(\tilde Q_1,\tilde Q_2)=Q_{1t}\overline{Q_{2t}}$, $\beta_0(\tilde Q_1,\tilde Q_2)=Q_{1t}Q_{2t}$ | the invariant form of a homogeneous class, of complex dimension $1$ |
| real dimension $8$ | the invariant space of the enlarged real-bilinear class, the direct sum of the four central lines |
| $\mathrm{Tr}=2\,\mathrm{Sc}=0$ | the vanishing trace form |
| $(2,0)$, $(0,6)$, $(1,3)$ | the signatures of the restrictions |

## Further Reading

- [The Krein Norm of the Biquaternion Algebra](the-krein-norm-of-the-biquaternion-algebra.html), for the form and its inertia.
- [Introduction to the Remarkable Subspaces](introduction-to-the-remarkable-subspaces.html), for the remarkable subspaces.
- [Introduction to the Antisymmetric Quaternionic Sesqualgebra](introduction-to-the-antisymmetric-quaternionic-sesqualgebra.html), for the block.
- [The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra](the-conjugate-cross-product-and-the-jacobi-failure-of-the-antisymmetric-quaternionic-sesqualgebra.html), for the diagonal and its cone.
- *Remarkable Subspaces under the Antisymmetric Quaternionic Sesqualgebra of Biquaternions*, for the reading of the block on the remarkable subspaces.
