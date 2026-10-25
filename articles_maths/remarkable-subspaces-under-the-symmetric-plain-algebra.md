# __Remarkable Subspaces under the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra of $\mathbb{B}$ carries the product $\tilde Q_1\bullet\tilde Q_2=\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$ of *Introduction to the Symmetric Plain Algebra*. The algebra carries remarkable real subspaces, and this article reads the product on each of them: whether it stays inside, and the rule it follows where it does; the units and the idempotents it contains; and its isotropic elements. The remarkable subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$ of *Introduction to the Remarkable Subspaces*, with their natural real bases.

The reading follows the pattern of *Remarkable Subspaces and the Four General Products, Forms and Norms*, and the subspaces themselves, their bases and their relations are *Introduction to the Remarkable Subspaces* and *Comparison of the Remarkable Subspaces*. The products of the four general products on the same remarkable subspaces are read in the same article; the isotropic set of the block is the isotropic cone of *Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra*; and the idempotents are those of *Idempotents of the General Plain Algebra*. This article owns the product $\bullet$ on the remarkable subspaces and the table that gathers the readings.

**Conventions and the criterion.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$ and central scalar imaginary $i$, and the product is $\bullet$. An element is $\tilde Q=Q_te_t+\vec Q$. The remarkable subspaces are real and their natural real bases are the ones of *Introduction to the Remarkable Subspaces*:

$$
\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_t,ie_t\},\quad
\mathrm{Vect}(\mathbb{B})=\mathrm{span}_{\mathbb{R}}\{\vec e_k,i\vec e_k\}_{k=1}^{3},\quad
\mathbb{H}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_t,\vec e_x,\vec e_y,\vec e_z\},
$$

$$
i\mathbb{H}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{ie_t,i\vec e_x,i\vec e_y,i\vec e_z\},\quad
\mathbb{M}_+=\mathrm{span}_{\mathbb{R}}\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\},\quad
\mathbb{M}_-=\mathrm{span}_{\mathbb{R}}\{ie_t,\vec e_x,\vec e_y,\vec e_z\}.
$$

A **unit** and an **idempotent** of the block are as in *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*: a unit is an element with $\langle\tilde Q\rangle_{\natural}\neq0$, an idempotent an element with $\tilde Q\bullet\tilde Q=\tilde Q$. An element is **isotropic** when its generic norm vanishes, $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2=0$; the isotropic elements of a subspace are those of its elements that are isotropic.

## The Centre $\mathbb{C}_{\mathbb{B}}$

### The Product Rule and the Closure

An element of the centre is a scalar $Ae_t$, $A\in\mathbb{C}$, and the product rule is

$$
(Ae_t)\bullet(Be_t)=ABe_t .
$$

The rule is the multiplication of the complex numbers, restricted to the scalar line. The centre is therefore **closed** under $\bullet$: it is a one-dimensional complex subspace, and with the product $\bullet$ it is the field $\mathbb{C}$ read inside the block. It is the smallest of the three closed subspaces and a Jordan subalgebra of the block.

### Units, Idempotents and Isotropic Elements

The generic norm of a central element is $\langle Ae_t\rangle_{\natural}=A^2$, so the **units** of the centre are the non-zero scalars, $A\neq0$, and the element $Ae_t$ with $A\neq0$ is invertible in the block with inverse $A^{-1}e_t$. The **idempotents** of the centre are the solutions of $A^2=A$, namely $0$ and $e_t$; these are the two trivial idempotents of the block, and no non-trivial idempotent is central, because a non-trivial idempotent is $\tfrac12(e_t+\vec q)$ with $\vec q$ a non-zero pure root of $+1$, whose vector part $\tfrac12\vec q$ is non-central. The **isotropic** elements are the solutions of $A^2=0$, namely $0$ alone: the centre contains no non-zero isotropic element.

## The Vector Subspace $\mathrm{Vect}(\mathbb{B})$

### The Product Rule and the Failure of Closure

Two vector parts $\vec Q_1,\vec Q_2$ (pure elements in the sense of *Introduction to the Remarkable Subspaces*) multiply as

$$
\vec Q_1\bullet\vec Q_2=-\bigl(\vec Q_1,\vec Q_2\bigr)e_t,
$$

because the mixed vector part $Q_{1t}\vec Q_2+Q_{2t}\vec Q_1$ vanishes when both elements are pure and the cross term is absent. The value is a **central** element, so

$$ \boxed{\; \mathrm{Vect}(\mathbb{B})\bullet\mathrm{Vect}(\mathbb{B})\subseteq\mathbb{C}_{\mathbb{B}} \;}, $$

and the vector subspace is **not closed** under $\bullet$: its square lands in the centre. The smallest witnesses are

$$
\vec e_x\bullet \vec e_x=-e_t,\qquad \vec e_x\bullet \vec e_y=0,
$$

the first of which leaves the vector subspace and the second of which stays in it, so the failure is the rule and not an accident of one pair.

### Units, Idempotents and Isotropic Elements

A vector element $\vec Q$ has $\langle\vec Q\rangle_{\natural}=(\vec Q,\vec Q)$, so the **units** of the vector subspace are the elements with $(\vec Q,\vec Q)\neq0$; **every non-zero element of the subspace is a zero divisor of the block**, since the product of two pure elements is the scalar $-(\vec Q_1,\vec Q_2)$, which vanishes for the orthogonal $\vec Q_2$, and the isotropic elements are those with $(\vec Q,\vec Q)=0$ (*Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*). The **idempotents** are the solutions of $\vec Q\bullet\vec Q=\vec Q$, that is $-\bigl(\vec Q,\vec Q\bigr)e_t=\vec Q$, and since the left side is central and the right side is a vector part, both must vanish: $\vec Q=0$. So the vector subspace contains no non-zero idempotent. The **isotropic** elements are the isotropic cone of the vector subspace, $\{(\vec Q,\vec Q)=0\}$, and it is non-empty: for instance $\vec e_x+i\vec e_x$ has $(\vec e_x+i\vec e_x,\vec e_x+i\vec e_x)=1+i^2=0$.

**Remark (the isotropic elements of the vector subspace are of square zero).** On the vector subspace the generic norm is the dot form itself, $\langle\vec Q\rangle_{\natural}=(\vec Q,\vec Q)$, so an isotropic vector is exactly a vector of square zero: $\vec Q\bullet\vec Q=-(\vec Q,\vec Q)e_t=0$. **On the vector subspace the isotropic elements and the elements of square zero are the same set**, and both are the isotropic cone of the dot form; on the block as a whole the two sets differ, as *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra* records.

## The Quaternion Subspace $\mathbb{H}_{\mathbb{B}}$

### The Product Rule and the Closure

The quaternion subspace is the real span of the four units, and on its elements the conjugated product $\tilde Q_1^{\natural}\tilde Q_2$ of *Introduction to the General Quaternionic Algebra* is the ordinary quaternion product. The product $\bullet$ reads there as the **symmetrised quaternion product**,

$$
h\bullet k=\tfrac12(hk+kh)=h_tk_t-(\vec h,\vec k)+h_t\vec k+k_t\vec h,
$$

the quaternion product with the cross term $-\vec h\times\vec k$ dropped. The value lies in $\mathbb{H}_{\mathbb{B}}$, so the subspace is **closed** under $\bullet$, and with the product it is a Jordan subalgebra of the block.

**Remark (the quaternion subspace is a Jordan division algebra).** On the real quaternions the generic norm is the sum of squares $\langle h\rangle_{\natural}=\sum_\mu h_\mu^2$, which is positive definite and vanishes only at $h=0$. **The quaternion subspace contains no non-zero isotropic element, and every non-zero element of it is a unit**, so the quaternion subspace is a Jordan division algebra; this is the case the whole block fails, since the block carries the zero divisors of $\mathbb{C}$.

### Units, Idempotents and Isotropic Elements

The **units** are all the non-zero elements, by the positive-definiteness of the norm. The **idempotents** are the solutions of $h\bullet h=h$, that is $h^2=h$, or $h(h-e_t)=0$; the quaternions have no zero divisors, so $h=0$ or $h=e_t$. Thus the quaternion subspace contains exactly the two trivial idempotents $0$ and $e_t$, and the non-trivial idempotents of the block — the Hermitian idempotents and the mixed ones — are not in it. The **isotropic** elements are the solutions of $\langle h\rangle_{\natural}=\sum_\mu h_\mu^2=0$, namely $0$ alone.

## The Anti-Quaternion Subspace $i\mathbb{H}_{\mathbb{B}}$

### The Product Rule and the Failure of Closure

The anti-quaternion subspace consists of the elements $i\mathbf n$ with $\mathbf n$ a real quaternion, and two of them multiply as

$$
(i\mathbf n)\bullet(i\mathbf m)=\tfrac12\bigl(i\mathbf n\cdot i\mathbf m+i\mathbf m\cdot i\mathbf n\bigr)=i^2\tfrac12(\mathbf n\mathbf m+\mathbf m\mathbf n)=-(\mathbf n\bullet\mathbf m),
$$

the scalar $i$ central and $i^2=-1$. The value is a real quaternion and lies in $\mathbb{H}_{\mathbb{B}}$, so

$$ \boxed{\; i\mathbb{H}_{\mathbb{B}}\bullet i\mathbb{H}_{\mathbb{B}}\subseteq\mathbb{H}_{\mathbb{B}} \;}, $$

and the anti-quaternion subspace is **not closed** under $\bullet$. The smallest witness is

$$
(i\vec e_x)\bullet(i\vec e_x)=(i\vec e_x)^2=i^2\vec e_x^2=e_t,
$$

a central element outside the anti-quaternion subspace. In the mixed products the subspace is stable, $i\mathbb{H}_{\mathbb{B}}\bullet\mathbb{H}_{\mathbb{B}}\subseteq i\mathbb{H}_{\mathbb{B}}$, so the failure is confined to the product of two anti-quaternion elements.

### Units, Idempotents and Isotropic Elements

An anti-quaternion element $i\mathbf n$ has $\langle i\mathbf n\rangle_{\natural}=-(\mathbf n,\mathbf n)=-|\mathbf n|^2$, so the **units** are all the non-zero elements, as in the quaternion subspace, and the **isotropic** elements are $0$ alone. The **idempotents** are the solutions of $(i\mathbf n)\bullet(i\mathbf n)=i\mathbf n$; the square is the real quaternion $-(\mathbf n\bullet\mathbf n)$, lying in $\mathbb{H}_{\mathbb{B}}$, while $i\mathbf n$ lies in $i\mathbb{H}_{\mathbb{B}}$, and the two subspaces meet only at $0$; so $\mathbf n\bullet\mathbf n=0$ and $\mathbf n=0$. The anti-quaternion subspace contains no non-zero idempotent.

## The Hermitian Subspace $\mathbb{M}_+$

### The Product Rule and the Closure

The Hermitian subspace is the set of elements fixed by the Hermitian conjugation, $\tilde Q^{*}=\tilde Q$, of the form $\tilde Q=Q_te_t+\sum_k iQ'_k\vec e_k$ with $Q_t,Q'_k$ real. The star is an anti-automorphism of the algebra, $(\tilde Q_1\tilde Q_2)^{*}=\tilde Q_2^{*}\tilde Q_1^{*}$, so for Hermitian $\tilde Q_1,\tilde Q_2$,

$$ \boxed{\; (\tilde Q_1\bullet\tilde Q_2)^{*}=\tfrac12\bigl((\tilde Q_1\tilde Q_2)^{*}+(\tilde Q_2\tilde Q_1)^{*}\bigr)=\tfrac12\bigl(\tilde Q_2\tilde Q_1+\tilde Q_1\tilde Q_2\bigr)=\tilde Q_1\bullet\tilde Q_2 \;}, $$

and the Hermitian subspace is **closed** under $\bullet$. It is a Jordan subalgebra of the block, and it is the **Hermitian Jordan algebra** $J(\mathbb{B})$ of *Symmetric and Antisymmetric Decomposition of the Four General Products*.

### Units, Idempotents and Isotropic Elements

A Hermitian element has $\langle\tilde Q\rangle_{\natural}=Q_t^2-\sum_k(Q'_k)^2$, so the **units** are the Hermitian elements with $Q_t^2\neq\sum_k(Q'_k)^2$, and the **isotropic** elements are those with $Q_t^2=\sum_k(Q'_k)^2$. The isotropic set is non-empty: the element $e_t+i\vec e_x$ is Hermitian and $\langle e_t+i\vec e_x\rangle_{\natural}=1+i^2=0$. The **idempotents** are the Hermitian idempotents of *Idempotents of the General Plain Algebra*,

$$
\tilde\Pi=\tfrac12(e_t\pm \tilde\Xi),\qquad \vec u\in\mathbb{R}^3,\ |\vec u|=1,
$$

the pure states, together with the trivial $0$ and $e_t$.

**Remark (the trace form is definite but the norm is not).** The trace form of *The Trace Form and the Invariance of the Symmetric Plain Algebra* restricts to the Hermitian subspace as the **positive definite** form $Q_{1t}Q_{2t}+\sum_kQ'_{1k}Q'_{2k}$ of signature $(4,0)$; the generic norm restricts as $Q_t^2-\sum_k(Q'_k)^2$, of signature $(1,3)$. **On the Hermitian subspace the trace form is definite and the generic norm is indefinite**, and it is the generic norm that decides the isotropic elements and the units.

## The Anti-Hermitian Subspace $\mathbb{M}_-$

### The Product Rule and the Failure of Closure

The anti-Hermitian subspace is the set of elements with $\tilde Q^{*}=-\tilde Q$, of the form $\tilde Q=iQ'_te_t+\sum_kQ_k\vec e_k$ with $Q'_t,Q_k$ real. The product of two anti-Hermitian elements is Hermitian,

$$
(\tilde Q_1\bullet\tilde Q_2)^{*}=\tfrac12\bigl((\tilde Q_1\tilde Q_2)^{*}+(\tilde Q_2\tilde Q_1)^{*}\bigr)=\tfrac12\bigl(\tilde Q_2^{*}\tilde Q_1^{*}+\tilde Q_1^{*}\tilde Q_2^{*}\bigr)=\tfrac12\bigl(\tilde Q_2\tilde Q_1+\tilde Q_1\tilde Q_2\bigr)=\tilde Q_1\bullet\tilde Q_2,
$$

so the value is Hermitian and leaves the anti-Hermitian subspace. The subspace is **not closed** under $\bullet$, and the smallest witness is

$$
(ie_t)\bullet(ie_t)=(ie_t)^2=i^2e_t^2=-e_t,
$$

a central Hermitian element.

### Units, Idempotents and Isotropic Elements

An anti-Hermitian element has $\langle\tilde Q\rangle_{\natural}=-(Q'_t)^2+\sum_kQ_k^2$, so the **units** are the anti-Hermitian elements with $\sum_kQ_k^2\neq(Q'_t)^2$, and the **isotropic** elements are those with $\sum_kQ_k^2=(Q'_t)^2$, a non-empty set: the element $ie_t+\vec e_x$ is anti-Hermitian and $\langle ie_t+\vec e_x\rangle_{\natural}=-1+1=0$. The **idempotents** are the solutions of $\tilde Q\bullet\tilde Q=\tilde Q$ with $\tilde Q=iQ'_te_t+\vec Q$. Writing the square as $\bigl((iQ'_t)^2-(\vec Q,\vec Q)\bigr)e_t+2(iQ'_t)\vec Q$ and equating to $\tilde Q$, the vector equation gives $2iQ'_t\vec Q=\vec Q$; if $\vec Q\neq0$ this forces $iQ'_t=\tfrac12$, impossible because $iQ'_t$ is purely imaginary, so $\vec Q=0$, and the scalar equation gives $(iQ'_t)^2=iQ'_t$, with purely imaginary root $0$. The anti-Hermitian subspace contains no non-zero idempotent.

## The Table of the Remarkable Subspaces

| Subspace | Closed under $\bullet$? | Product rule | Unit | Idempotents | Isotropic elements |
|---|---|---|---|---|---|
| Centre $\mathbb{C}_{\mathbb{B}}$ | yes | $(Ae_t)\bullet(Be_t)=ABe_t$ | $Ae_t$, $A\neq0$ | $0,\ e_t$ | $0$ only |
| Vector $\mathrm{Vect}(\mathbb{B})$ | no | $\vec Q_1\bullet\vec Q_2=-(\vec Q_1,\vec Q_2)e_t$ | $(\vec Q,\vec Q)\neq0$ | $0$ only | $\{(\vec Q,\vec Q)=0\}$, non-empty |
| Quaternion $\mathbb{H}_{\mathbb{B}}$ | yes | $h\bullet k=h_tk_t-(\vec h,\vec k)+h_t\vec k+k_t\vec h$ | all $h\neq0$ | $0,\ e_t$ | $0$ only |
| Anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | no | $(i\mathbf n)\bullet(i\mathbf m)=-\mathbf n\bullet\mathbf m$ | all $i\mathbf n\neq0$ | $0$ only | $0$ only |
| Hermitian $\mathbb{M}_+$ | yes | $(\tilde Q_1\bullet\tilde Q_2)^{*}=\tilde Q_1\bullet\tilde Q_2$ | $Q_t^2\neq\sum_k(Q'_k)^2$ | $0,\ e_t,\ \tfrac12(e_t\pm \tilde\Xi)$ | $\{Q_t^2=\sum_k(Q'_k)^2\}$, non-empty |
| Anti-Hermitian $\mathbb{M}_-$ | no | $(\tilde Q_1\bullet\tilde Q_2)^{*}=\tilde Q_1\bullet\tilde Q_2$ | $\sum_kQ_k^2\neq(Q'_t)^2$ | $0$ only | $\{\sum_kQ_k^2=(Q'_t)^2\}$, non-empty |

**Remark (three of the remarkable subspaces are closed).** Exactly **three of the remarkable subspaces are closed under $\bullet$ — the centre, the quaternion subspace and the Hermitian subspace** — and each of the three is a Jordan subalgebra: the centre is the field $\mathbb{C}$, the quaternion subspace is the Jordan division algebra of the symmetrised quaternions, and the Hermitian subspace is the Hermitian Jordan algebra $J(\mathbb{B})$. The other three fail: the vector subspace squares into the centre, the anti-quaternion subspace into the quaternion subspace, and the anti-Hermitian subspace into the Hermitian subspace. **The three failures are the three sign changes $\vec e_k^2=-e_t$, $i^2=-1$ and $(ie_t)^2=-e_t$**, each sending an element out of its subspace.

**Remark (isotropic and square zero on the remarkable subspaces).** The isotropic elements are non-zero in the vector, Hermitian and anti-Hermitian subspaces, and absent in the centre, the quaternion subspace and the anti-quaternion subspace. The elements of square zero are the **pure** isotropic elements, so on the vector subspace the two coincide and on the Hermitian and anti-Hermitian subspaces the isotropic elements $e_t+i\vec e_x$ and $ie_t+\vec e_x$ are isotropic without being of square zero. **The two notions agree on the vector subspace and differ on the two Hermitian sectors.**

## Summary

On the remarkable real subspaces the symmetric plain product is closed on the centre $\mathbb{C}_{\mathbb{B}}$, on the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and on the Hermitian subspace $\mathbb{M}_+$, which are the three Jordan subalgebras of the block — the field $\mathbb{C}$, the Jordan division algebra of the symmetrised quaternions, and the Hermitian Jordan algebra $J(\mathbb{B})$. It fails to close on the vector subspace, where $\vec Q_1\bullet\vec Q_2=-(\vec Q_1,\vec Q_2)e_t$ lands in the centre; on the anti-quaternion subspace, where $(i\mathbf n)\bullet(i\mathbf m)=-\mathbf n\bullet\mathbf m$ lands in the quaternion subspace; and on the anti-Hermitian subspace, where $(ie_t)^2=-e_t$ lands in the Hermitian subspace. The units are the non-zero scalars in the centre, all non-zero elements in the two quaternion subspaces, the elements of non-zero dot form in the vector subspace, and the elements of non-zero generic norm in the two Hermitian sectors. The idempotents are $0$ and $e_t$ in the centre and the quaternion subspace and the Hermitian idempotents $\tfrac12(e_t\pm \tilde\Xi)$ in the Hermitian subspace, and $0$ alone in the other three. The isotropic elements are absent off zero in the centre and the two quaternion subspaces, and non-empty in the vector, Hermitian and anti-Hermitian subspaces; the elements of square zero agree with them on the vector subspace and are strictly smaller on the two Hermitian sectors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}_{\mathbb{B}},\ \mathrm{Vect}(\mathbb{B}),\ \mathbb{H}_{\mathbb{B}},\ i\mathbb{H}_{\mathbb{B}},\ \mathbb{M}_+,\ \mathbb{M}_-$ | the remarkable real subspaces |
| $\vec Q_1\bullet\vec Q_2=-(\vec Q_1,\vec Q_2)e_t$ | the product on the vector subspace, into the centre |
| $i\mathbb{H}_{\mathbb{B}}\bullet i\mathbb{H}_{\mathbb{B}}\subseteq\mathbb{H}_{\mathbb{B}}$ | the product of two anti-quaternion elements |
| $(\tilde Q_1\bullet\tilde Q_2)^{*}=\tilde Q_1\bullet\tilde Q_2$ | the closure of the Hermitian and the failure for the anti-Hermitian |
| $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ | the generic norm, deciding units and isotropic elements |
| $\tfrac12(e_t\pm \tilde\Xi)$, $|\vec u|=1$ | the Hermitian idempotents, in $\mathbb{M}_+$ |

## Further Reading

- [Introduction to the Remarkable Subspaces](introduction-to-the-remarkable-subspaces.html) and [Comparison of the Remarkable Subspaces](comparison-of-the-remarkable-subspaces.html), for the remarkable subspaces, their bases and their relations.
- [Remarkable Subspaces and the Four General Products, Forms and Norms](remarkable-subspaces-and-the-four-general-products-forms-and-norms.html), for the same remarkable subspaces under the general plain bilinear form, and for the readings of the four general products.
- [Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra](quaternionic-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the generic norm, the units and the isotropic cone.
- *Idempotents of the General Plain Algebra*, for the idempotents and the pure states.
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the Hermitian Jordan algebra $J(\mathbb{B})$ and the placement of the block.
- [The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra](the-square-the-idempotents-and-the-jordan-inverse-of-the-symmetric-plain-algebra.html), for the isotropic cone of the block and the elements of square zero.
