# __Remarkable Subspaces under the Symmetric Plain Algebra of Biquaternions__

## Introduction

The symmetric plain algebra of $\mathbb{B}$ carries the product $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ of *Introduction to the Symmetric Plain Algebra of Biquaternions*. The algebra carries remarkable real subspaces, and this article reads the product on each of them: whether it stays inside, and the rule it follows where it does; the units and the idempotents it contains; and its isotropic elements. The remarkable subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$ of *Introduction to the Remarkable Subspaces*, with their natural real bases.

The reading follows the pattern of *Remarkable Subspaces under the General Plain Algebra of Biquaternions*, and the subspaces themselves, their bases and their relations are *Introduction to the Remarkable Subspaces* and *Comparison of the Remarkable Subspaces*. The products of the four general products on the same remarkable subspaces are *Remarkable Subspaces and the Four General Products*; the isotropic set of the block is the isotropic cone of *Biquaternion Norm and Invertibility*; and the idempotents are those of *Idempotents of the General Plain Algebra*. This article owns the product $\bullet$ on the remarkable subspaces and the table that gathers the readings.

**Conventions and the criterion.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$ and central scalar imaginary $i$, and the product is $\bullet$. An element is $\tilde Q=Q_0e_0+\mathbf{Q}$. The remarkable subspaces are real and their natural real bases are the ones of *Introduction to the Remarkable Subspaces*:

$$
\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\},\quad
\mathrm{Vect}(\mathbb{B})=\mathrm{span}_{\mathbb{R}}\{e_k,ie_k\}_{k=1}^{3},\quad
\mathbb{H}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,e_1,e_2,e_3\},
$$

$$
i\mathbb{H}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{ie_0,ie_1,ie_2,ie_3\},\quad
\mathbb{M}_+=\mathrm{span}_{\mathbb{R}}\{e_0,ie_1,ie_2,ie_3\},\quad
\mathbb{M}_-=\mathrm{span}_{\mathbb{R}}\{ie_0,e_1,e_2,e_3\}.
$$

A **unit** and an **idempotent** of the block are as in *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*: a unit is an element with $N(\tilde Q)\neq0$, an idempotent an element with $\tilde Q\bullet\tilde Q=\tilde Q$. An element is **isotropic** when its generic norm vanishes, $N(\tilde Q)=\sum_\mu Q_\mu^2=0$; the isotropic elements of a subspace are those of its elements that are isotropic.

## The Centre $\mathbb{C}_{\mathbb{B}}$

### The Product Rule and the Closure

An element of the centre is a scalar $Ae_0$, $A\in\mathbb{C}$, and the product rule is

$$
(Ae_0)\bullet(Be_0)=ABe_0 .
$$

The rule is the multiplication of the complex numbers, restricted to the scalar line. The centre is therefore **closed** under $\bullet$: it is a one-dimensional complex subspace, and with the product $\bullet$ it is the field $\mathbb{C}$ read inside the block. It is the smallest of the three closed subspaces and a Jordan subalgebra of the block.

### Units, Idempotents and Isotropic Elements

The generic norm of a central element is $N(Ae_0)=A^2$, so the **units** of the centre are the non-zero scalars, $A\neq0$, and the element $Ae_0$ with $A\neq0$ is invertible in the block with inverse $A^{-1}e_0$. The **idempotents** of the centre are the solutions of $A^2=A$, namely $0$ and $e_0$; these are the two trivial idempotents of the block, and no non-trivial idempotent is central, because a non-trivial idempotent $\tfrac12(e_0+\xi i)$ has the non-central element $\xi i$ in its vector part. The **isotropic** elements are the solutions of $A^2=0$, namely $0$ alone: the centre contains no non-zero isotropic element. Verified on the coordinate rule.

## The Vector Subspace $\mathrm{Vect}(\mathbb{B})$

### The Product Rule and the Failure of Closure

Two vector parts $\mathbf{P},\mathbf{Q}$ (pure elements in the sense of *Introduction to the Remarkable Subspaces*) multiply as

$$
\mathbf{P}\bullet\mathbf{Q}=-\bigl(\mathbf{P},\mathbf{Q}\bigr)e_0,
$$

because the mixed vector part $P_0\mathbf{Q}+Q_0\mathbf{P}$ vanishes when both elements are pure and the cross term is absent. The value is a **central** element, so

$$
\mathrm{Vect}(\mathbb{B})\bullet\mathrm{Vect}(\mathbb{B})\subseteq\mathbb{C}_{\mathbb{B}},
$$

and the vector subspace is **not closed** under $\bullet$: its square lands in the centre. The smallest witnesses are

$$
e_1\bullet e_1=-e_0,\qquad e_1\bullet e_2=0,
$$

the first of which leaves the vector subspace and the second of which stays in it, so the failure is the rule and not an accident of one pair.

### Units, Idempotents and Isotropic Elements

A vector element $\mathbf{P}$ has $N(\mathbf{P})=(\mathbf{P},\mathbf{P})$, so the **units** of the vector subspace are the elements with $(\mathbf{P},\mathbf{P})\neq0$; the elements with $(\mathbf{P},\mathbf{P})=0$ are isotropic, and the non-zero ones among them are exactly the zero divisors inside the subspace. The **idempotents** are the solutions of $\mathbf{P}\bullet\mathbf{P}=\mathbf{P}$, that is $-\bigl(\mathbf{P},\mathbf{P}\bigr)e_0=\mathbf{P}$, and since the left side is central and the right side is a vector part, both must vanish: $\mathbf{P}=0$. So the vector subspace contains no non-zero idempotent. The **isotropic** elements are the isotropic cone of the vector subspace, $\{(\mathbf{P},\mathbf{P})=0\}$, and it is non-empty: for instance $e_1+ie_1$ has $(e_1+ie_1,e_1+ie_1)=1+i^2=0$. Verified on the coordinate rule.

**Remark (the isotropic elements of the vector subspace are of square zero).** On the vector subspace the generic norm is the dot form itself, $N(\mathbf{P})=(\mathbf{P},\mathbf{P})$, so an isotropic vector is exactly a vector of square zero: $\mathbf{P}\bullet\mathbf{P}=-(\mathbf{P},\mathbf{P})e_0=0$. **On the vector subspace the isotropic elements and the elements of square zero are the same set**, and both are the isotropic cone of the dot form; on the block as a whole the two sets differ, as *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra* records. Verified on the rule.

## The Quaternion Subspace $\mathbb{H}_{\mathbb{B}}$

### The Product Rule and the Closure

The quaternion subspace is the real span of the four units, and on its elements the conjugated product $\tilde Q^{\natural}\tilde R$ of *Introduction to the General Quaternionic Algebra of Biquaternions* is the ordinary quaternion product. The product $\bullet$ reads there as the **symmetrised quaternion product**,

$$
h\bullet k=\tfrac12(hk+kh)=h_0k_0-(\mathbf{h},\mathbf{k})+h_0\mathbf{k}+k_0\mathbf{h},
$$

the quaternion product with the cross term $-\mathbf{h}\times\mathbf{k}$ dropped. The value lies in $\mathbb{H}_{\mathbb{B}}$, so the subspace is **closed** under $\bullet$, and with the product it is a Jordan subalgebra of the block.

**Remark (the quaternion subspace is a Jordan division algebra).** On the real quaternions the generic norm is the sum of squares $N(h)=\sum_\mu h_\mu^2$, which is positive definite and vanishes only at $h=0$. **The quaternion subspace contains no non-zero isotropic element, and every non-zero element of it is a unit**, so the quaternion subspace is a Jordan division algebra; this is the case the whole block fails, since the block carries the zero divisors of $\mathbb{C}$.

### Units, Idempotents and Isotropic Elements

The **units** are all the non-zero elements, by the positive-definiteness of the norm. The **idempotents** are the solutions of $h\bullet h=h$, that is $h^2=h$, or $h(h-e_0)=0$; the quaternions have no zero divisors, so $h=0$ or $h=e_0$. Thus the quaternion subspace contains exactly the two trivial idempotents $0$ and $e_0$, and the non-trivial idempotents of the block — the Hermitian idempotents and the mixed ones — are not in it. The **isotropic** elements are the solutions of $N(h)=\sum_\mu h_\mu^2=0$, namely $0$ alone. Verified on the coordinate rule.

## The Anti-Quaternion Subspace $i\mathbb{H}_{\mathbb{B}}$

### The Product Rule and the Failure of Closure

The anti-quaternion subspace consists of the elements $i\mu$ with $\mu$ a real quaternion, and two of them multiply as

$$
(i\mu)\bullet(i\nu)=\tfrac12\bigl(i\mu\cdot i\nu+i\nu\cdot i\mu\bigr)=i^2\tfrac12(\mu\nu+\nu\mu)=-(\mu\bullet\nu),
$$

the scalar $i$ central and $i^2=-1$. The value is a real quaternion and lies in $\mathbb{H}_{\mathbb{B}}$, so

$$
i\mathbb{H}_{\mathbb{B}}\bullet i\mathbb{H}_{\mathbb{B}}\subseteq\mathbb{H}_{\mathbb{B}},
$$

and the anti-quaternion subspace is **not closed** under $\bullet$. The smallest witness is

$$
(ie_1)\bullet(ie_1)=(ie_1)^2=i^2e_1^2=e_0,
$$

a central element outside the anti-quaternion subspace. In the mixed products the subspace is stable, $i\mathbb{H}_{\mathbb{B}}\bullet\mathbb{H}_{\mathbb{B}}\subseteq i\mathbb{H}_{\mathbb{B}}$, so the failure is confined to the product of two anti-quaternion elements.

### Units, Idempotents and Isotropic Elements

An anti-quaternion element $i\mu$ has $N(i\mu)=-(\mu,\mu)=-|\mu|^2$, so the **units** are all the non-zero elements, as in the quaternion subspace, and the **isotropic** elements are $0$ alone. The **idempotents** are the solutions of $(i\mu)\bullet(i\mu)=i\mu$; the square is the real quaternion $-(\mu\bullet\mu)$, lying in $\mathbb{H}_{\mathbb{B}}$, while $i\mu$ lies in $i\mathbb{H}_{\mathbb{B}}$, and the two subspaces meet only at $0$; so $\mu\bullet\mu=0$ and $\mu=0$. The anti-quaternion subspace contains no non-zero idempotent. Verified on the coordinate rule.

## The Hermitian Subspace $\mathbb{M}_+$

### The Product Rule and the Closure

The Hermitian subspace is the set of elements fixed by the Hermitian conjugation, $\tilde Q^{*}=\tilde Q$, of the form $\tilde Q=P_0e_0+\sum_k iP'_ke_k$ with $P_0,P'_k$ real. The star is an anti-automorphism of the algebra, $(\tilde P\tilde Q)^{*}=\tilde Q^{*}\tilde P^{*}$, so for Hermitian $\tilde P,\tilde Q$,

$$
(\tilde P\bullet\tilde Q)^{*}=\tfrac12\bigl((\tilde P\tilde Q)^{*}+(\tilde Q\tilde P)^{*}\bigr)=\tfrac12\bigl(\tilde Q\tilde P+\tilde P\tilde Q\bigr)=\tilde P\bullet\tilde Q,
$$

and the Hermitian subspace is **closed** under $\bullet$. It is a Jordan subalgebra of the block, and it is the **Hermitian Jordan algebra** $J(\mathbb{B})$ of *The 12 Products of the Biquaternion Complex Space*.

### Units, Idempotents and Isotropic Elements

A Hermitian element has $N(\tilde P)=P_0^2-\sum_k(P'_k)^2$, so the **units** are the Hermitian elements with $P_0^2\neq\sum_k(P'_k)^2$, and the **isotropic** elements are those with $P_0^2=\sum_k(P'_k)^2$. The isotropic set is non-empty: the element $e_0+ie_1$ is Hermitian and $N(e_0+ie_1)=1+i^2=0$. The **idempotents** are the Hermitian idempotents of *Idempotents of the General Plain Algebra*,

$$
\tilde\Pi=\tfrac12(e_0\pm i\hat\mu),\qquad \hat\mu\in\mathbb{R}^3,\ |\hat\mu|=1,
$$

the pure states, together with the trivial $0$ and $e_0$.

**Remark (the trace form is definite but the norm is not).** The trace form of *The Trace Form and the Invariance of the Symmetric Plain Algebra* restricts to the Hermitian subspace as the **positive definite** form $P_0Q_0+\sum_kP'_kQ'_k$ of signature $(4,0)$; the generic norm restricts as $P_0^2-\sum_k(P'_k)^2$, of signature $(1,3)$. **On the Hermitian subspace the trace form is definite and the generic norm is indefinite**, and it is the generic norm that decides the isotropic elements and the units. Verified on the restriction.

## The Anti-Hermitian Subspace $\mathbb{M}_-$

### The Product Rule and the Failure of Closure

The anti-Hermitian subspace is the set of elements with $\tilde Q^{*}=-\tilde Q$, of the form $\tilde Q=iP'_0e_0+\sum_kP_ke_k$ with $P'_0,P_k$ real. The product of two anti-Hermitian elements is Hermitian,

$$
(\tilde P\bullet\tilde Q)^{*}=\tfrac12\bigl((\tilde P\tilde Q)^{*}+(\tilde Q\tilde P)^{*}\bigr)=\tfrac12\bigl(\tilde Q^{*}\tilde P^{*}+\tilde P^{*}\tilde Q^{*}\bigr)=\tfrac12\bigl(\tilde Q\tilde P+\tilde P\tilde Q\bigr)=\tilde P\bullet\tilde Q,
$$

so the value is Hermitian and leaves the anti-Hermitian subspace. The subspace is **not closed** under $\bullet$, and the smallest witness is

$$
(ie_0)\bullet(ie_0)=(ie_0)^2=i^2e_0^2=-e_0,
$$

a central Hermitian element.

### Units, Idempotents and Isotropic Elements

An anti-Hermitian element has $N(\tilde P)=-(P'_0)^2+\sum_kP_k^2$, so the **units** are the anti-Hermitian elements with $\sum_kP_k^2\neq(P'_0)^2$, and the **isotropic** elements are those with $\sum_kP_k^2=(P'_0)^2$, a non-empty set: the element $ie_0+e_1$ is anti-Hermitian and $N(ie_0+e_1)=-1+1=0$. The **idempotents** are the solutions of $\tilde P\bullet\tilde P=\tilde P$ with $\tilde P=iP'_0e_0+\mathbf{P}$. Writing the square as $\bigl((iP'_0)^2-(\mathbf{P},\mathbf{P})\bigr)e_0+2(iP'_0)\mathbf{P}$ and equating to $\tilde P$, the vector equation gives $2iP'_0\mathbf{P}=\mathbf{P}$; if $\mathbf{P}\neq0$ this forces $iP'_0=\tfrac12$, impossible because $iP'_0$ is purely imaginary, so $\mathbf{P}=0$, and the scalar equation gives $(iP'_0)^2=iP'_0$, with purely imaginary root $0$. The anti-Hermitian subspace contains no non-zero idempotent. Verified on the coordinate rule.

## The Table of the Remarkable Subspaces

| Subspace | Closed under $\bullet$? | Product rule | Unit | Idempotents | Isotropic elements |
|---|---|---|---|---|---|
| Centre $\mathbb{C}_{\mathbb{B}}$ | yes | $(Ae_0)\bullet(Be_0)=ABe_0$ | $Ae_0$, $A\neq0$ | $0,\ e_0$ | $0$ only |
| Vector $\mathrm{Vect}(\mathbb{B})$ | no | $\mathbf{P}\bullet\mathbf{Q}=-(\mathbf{P},\mathbf{Q})e_0$ | $(\mathbf{P},\mathbf{P})\neq0$ | $0$ only | $\{(\mathbf{P},\mathbf{P})=0\}$, non-empty |
| Quaternion $\mathbb{H}_{\mathbb{B}}$ | yes | $h\bullet k=h_0k_0-(\mathbf{h},\mathbf{k})+h_0\mathbf{k}+k_0\mathbf{h}$ | all $h\neq0$ | $0,\ e_0$ | $0$ only |
| Anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | no | $(i\mu)\bullet(i\nu)=-\mu\bullet\nu$ | all $i\mu\neq0$ | $0$ only | $0$ only |
| Hermitian $\mathbb{M}_+$ | yes | $(\tilde P\bullet\tilde Q)^{*}=\tilde P\bullet\tilde Q$ | $P_0^2\neq\sum_k(P'_k)^2$ | $0,\ e_0,\ \tfrac12(e_0\pm i\hat\mu)$ | $\{P_0^2=\sum_k(P'_k)^2\}$, non-empty |
| Anti-Hermitian $\mathbb{M}_-$ | no | $(\tilde P\bullet\tilde Q)^{*}=\tilde P\bullet\tilde Q$ | $\sum_kP_k^2\neq(P'_0)^2$ | $0$ only | $\{\sum_kP_k^2=(P'_0)^2\}$, non-empty |

**Remark (three of the remarkable subspaces are closed).** Exactly **three of the remarkable subspaces are closed under $\bullet$ — the centre, the quaternion subspace and the Hermitian subspace** — and each of the three is a Jordan subalgebra: the centre is the field $\mathbb{C}$, the quaternion subspace is the Jordan division algebra of the symmetrised quaternions, and the Hermitian subspace is the Hermitian Jordan algebra $J(\mathbb{B})$. The other three fail: the vector subspace squares into the centre, the anti-quaternion subspace into the quaternion subspace, and the anti-Hermitian subspace into the Hermitian subspace. **The three failures are the three sign changes $e_k^2=-e_0$, $i^2=-1$ and $(ie_0)^2=-e_0$**, each sending an element out of its subspace. Verified on the readings.

**Remark (isotropic and square zero on the remarkable subspaces).** The isotropic elements are non-zero in the vector, Hermitian and anti-Hermitian subspaces, and absent in the centre, the quaternion subspace and the anti-quaternion subspace. The elements of square zero are the **pure** isotropic elements, so on the vector subspace the two coincide and on the Hermitian and anti-Hermitian subspaces the isotropic elements $e_0+ie_1$ and $ie_0+e_1$ are isotropic without being of square zero. **The two notions agree on the vector subspace and differ on the two Hermitian sectors.** Verified on the witnesses.

## Summary

On the remarkable real subspaces the symmetric plain product is closed on the centre $\mathbb{C}_{\mathbb{B}}$, on the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and on the Hermitian subspace $\mathbb{M}_+$, which are the three Jordan subalgebras of the block — the field $\mathbb{C}$, the Jordan division algebra of the symmetrised quaternions, and the Hermitian Jordan algebra $J(\mathbb{B})$. It fails to close on the vector subspace, where $\mathbf{P}\bullet\mathbf{Q}=-(\mathbf{P},\mathbf{Q})e_0$ lands in the centre; on the anti-quaternion subspace, where $(i\mu)\bullet(i\nu)=-\mu\bullet\nu$ lands in the quaternion subspace; and on the anti-Hermitian subspace, where $(ie_0)^2=-e_0$ lands in the Hermitian subspace. The units are the non-zero scalars in the centre, all non-zero elements in the two quaternion subspaces, the elements of non-zero dot form in the vector subspace, and the elements of non-zero generic norm in the two Hermitian sectors. The idempotents are $0$ and $e_0$ in the centre and the quaternion subspace and the Hermitian idempotents $\tfrac12(e_0\pm i\hat\mu)$ in the Hermitian subspace, and $0$ alone in the other three. The isotropic elements are absent off zero in the centre and the two quaternion subspaces, and non-empty in the vector, Hermitian and anti-Hermitian subspaces; the elements of square zero agree with them on the vector subspace and are strictly smaller on the two Hermitian sectors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}_{\mathbb{B}},\ \mathrm{Vect}(\mathbb{B}),\ \mathbb{H}_{\mathbb{B}},\ i\mathbb{H}_{\mathbb{B}},\ \mathbb{M}_+,\ \mathbb{M}_-$ | the remarkable real subspaces |
| $\mathbf{P}\bullet\mathbf{Q}=-(\mathbf{P},\mathbf{Q})e_0$ | the product on the vector subspace, into the centre |
| $i\mathbb{H}_{\mathbb{B}}\bullet i\mathbb{H}_{\mathbb{B}}\subseteq\mathbb{H}_{\mathbb{B}}$ | the product of two anti-quaternion elements |
| $(\tilde P\bullet\tilde Q)^{*}=\tilde P\bullet\tilde Q$ | the closure of the Hermitian and the failure for the anti-Hermitian |
| $N(\tilde Q)=\sum_\mu Q_\mu^2$ | the generic norm, deciding units and isotropic elements |
| $\tfrac12(e_0\pm i\hat\mu)$, $|\hat\mu|=1$ | the Hermitian idempotents, in $\mathbb{M}_+$ |

## Further Reading

- *Introduction to the Remarkable Subspaces* and *Comparison of the Remarkable Subspaces*, for the remarkable subspaces, their bases and their relations.
- *Remarkable Subspaces under the General Plain Algebra of Biquaternions*, for the same remarkable subspaces under the general plain bilinear form, and *Remarkable Subspaces and the Four General Products*, for the readings of the four general products.
- *Biquaternion Norm and Invertibility*, for the generic norm, the units and the isotropic cone.
- *Idempotents of the General Plain Algebra*, for the idempotents and the pure states.
- *The 12 Products of the Biquaternion Complex Space*, for the Hermitian Jordan algebra $J(\mathbb{B})$ and the placement of the block.
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, for the isotropic cone of the block and the elements of square zero.
