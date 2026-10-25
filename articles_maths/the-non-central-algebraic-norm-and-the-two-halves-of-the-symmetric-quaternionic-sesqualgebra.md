# __The Non-Central Algebraic Norm and the Two Halves of the Symmetric Quaternionic Sesqualgebra__

## Introduction

The symmetric quaternionic sesquilinear product of *Introduction to the Symmetric Quaternionic Sesqualgebra* is the multiplication of this block, and its algebraic norm $\tilde Q\star\tilde Q$ is the object that tells the block apart from its companions. Two of the four symmetric parts have central algebraic norms: the quaternionic bilinear one, $\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}e_t$, and the plain sesquilinear one, whose algebraic norm is the positive Hermitian form $(|Q_t|^{2}+\sum_{\mu\in\{x,y,z\}}|Q_\mu|^{2})$ times $e_t$. The plain square is already non-central in general, $(e_t+\vec e_x)^{2}=2\vec e_x$, and the block's algebraic norm is non-central too, but with its own shape: it carries a complex scalar part and a vector part side by side, and at $e_t+\vec e_x$ it is $-2\vec e_x$, an element of the vector subspace. The reason is structural: the product is the half-sum of the two orders $\tilde Q_1^{\natural}\tilde Q_2^{*}$ and $\tilde Q_2^{*}\tilde Q_1^{\natural}$, and at the two equal arguments the two orders are the same product read twice, whose scalar parts agree and whose vector parts carry the cross product with opposite signs. The half-sum therefore keeps the scalar part and the *mixed* vector part and loses the cross product, and the mixed vector part does not vanish.

This article reads the algebraic norm as an element and not as a number. Its scalar part is the Krein form $\langle\tilde Q,\tilde Q\rangle_{\natural*}$, its vector part is $-Q_t\overline{\vec Q}-\overline{Q_t}\vec Q$, and its vanishing is the criterion of centrality. The article then reads the two halves of the algebraic norm, the two orders $\tilde Q^{\natural}\tilde Q^{*}$ and $\tilde Q^{*}\tilde Q^{\natural}$, whose sum is twice the algebraic norm and whose difference is twice the antisymmetric companion; it reads the elements of square zero and the idempotents, both families in full; and it reads the absence of a unit and the two one-sided actions that the algebraic norm carries. The reconstruction of the general quaternionic sesquilinear product from its two halves is the introduction's and is not repeated here.

The product itself is *Introduction to the Symmetric Quaternionic Sesqualgebra*; the general quaternionic sesquilinear product and its square are *Introduction to the General Quaternionic Sesqualgebra*; the antisymmetric companion $\mathrm{AQS}$ is Block 8 of the batch and is defined in *Symmetric and Antisymmetric Decomposition of the Four General Products*; the form $\langle\cdot,\cdot\rangle_{\natural*}$ and its isotropic elements are *The Krein Norm of the Biquaternion Algebra*; the zero divisors of the algebra are *Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*; and the norm is *Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra*.

## The Algebraic Norm as an Element

**Theorem (the algebraic norm).** For every biquaternion,

$$
\boxed{\;
\tilde Q\star\tilde Q=\langle\tilde Q,\tilde Q\rangle_{\natural*}e_t-Q_t\overline{\vec Q}-\overline{Q_t}\vec Q,
\qquad
\langle\tilde Q,\tilde Q\rangle_{\natural*}=|Q_t|^{2}-\sum_{\mu\in\{x,y,z\}}|Q_\mu|^{2}
\;}.
$$

The scalar part is real and the vector part is $-2\mathrm{Re}(Q_t\overline{\vec Q})=-2\sum_{\mu\in\{x,y,z\}}\mathrm{Re}(Q_t\overline{Q_\mu})\vec e_\mu$, a real vector.

*Proof.* Put $\tilde Q_1=\tilde Q_2=\tilde Q$ in the scalar–vector form of *Introduction to the Symmetric Quaternionic Sesqualgebra*: the scalar part becomes $Q_t\overline{Q_t}-(\vec Q,\overline{\vec Q})=|Q_t|^{2}-\sum_{\mu\in\{x,y,z\}}|Q_\mu|^{2}$, a real number, and the vector part becomes $-Q_t\overline{\vec Q}-\overline{Q_t}\vec Q=-2\mathrm{Re}(Q_t\overline{\vec Q})$, a real vector.

**Remark (the algebraic norm is a real element).** Both the scalar and the vector part of the algebraic norm are real, so the algebraic norm always lies in the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$, whatever element one starts from. A general element of the block has two complex components in each slot, but its square has only real ones. The reason is the conjugate-commutativity: the algebraic norm is its own conjugate, $\tilde Q\star\tilde Q=\overline{\tilde Q\star\tilde Q}$, and the fixed elements of the coefficientwise conjugation are exactly the real quaternions.

## The Criterion of Centrality

**Theorem (centrality of the algebraic norm).** $\tilde Q\star\tilde Q$ lies in the centre exactly when

$$ \boxed{\; Q_t\overline{Q_\mu}\in i\mathbb{R}\quad\text{for every }\mu\in\{x,y,z\} \;}, $$

that is, when $Q_t\overline{\vec Q}$ is a purely imaginary vector, and in particular when $Q_t=0$.

*Proof.* The centre is $\mathbb{C}e_t$, so the algebraic norm is central exactly when its vector part vanishes. The $\mu$-th component of the vector part is $-Q_t\overline{Q_\mu}-\overline{Q_t}Q_\mu=-2\mathrm{Re}(Q_t\overline{Q_\mu})$, which vanishes exactly when $\mathrm{Re}(Q_t\overline{Q_\mu})=0$, that is when $Q_t\overline{Q_\mu}$ is purely imaginary. If $Q_t=0$ the three conditions hold.

**Corollary (the two witnesses).** On the two elements

$$
\vec e_x,
\qquad
\vec e_x+i\vec e_y
$$

the algebraic norm is central, and the values are $-e_t$ and $-2e_t$ respectively: $\langle \vec e_x,\vec e_x\rangle_{\natural*}=-1$, $\langle \vec e_x+i\vec e_y,\vec e_x+i\vec e_y\rangle_{\natural*}=-1-1=-2$, and in both cases $Q_t=0$, so the mixed term vanishes. On the element

$$
e_t+\vec e_x
$$

the algebraic norm is not central: $\langle e_t+\vec e_x,e_t+\vec e_x\rangle_{\natural*}=1-1=0$ and the vector part is $-1\cdot \vec e_x-1\cdot \vec e_x=-2\vec e_x$, so $(e_t+\vec e_x)\star(e_t+\vec e_x)=-2\vec e_x$.

**Remark (what the two witnesses show).** The two elements named in the menu comment of the introduction are the vector directions $\vec e_x$ and $\vec e_x+i\vec e_y$, and on both the algebraic norm is the *complex scalar multiple* of $e_t$ given by the form: $-e_t$ and $-2e_t$. Both are central, so the choice of these two as the witnesses of non-centrality is itself the departure: they lie in the vector subspace $\mathbf{e}$, on which the block's algebraic norm is central, and not only on $\mathbb{C}\vec e_x$ and the line through $\vec e_x+i\vec e_y$. The element that shows the block's own obstruction is $e_t+\vec e_x$, whose scalar coefficient is nonzero and whose $Q_t\overline{Q_x}=1$ is real and not purely imaginary; the general criterion is the display above.

## The Two Halves of the Algebraic Norm

**Theorem (the two orders).** The two orders whose half-sum is the algebraic norm are

$$
\boxed{\;
\tilde Q^{\natural}\tilde Q^{*}
\quad\text{and}\quad
\tilde Q^{*}\tilde Q^{\natural}
\;},
$$

their sum is $2\,\tilde Q\star\tilde Q$, their difference is $2\vec Q\times\overline{\vec Q}$, and their scalar parts are equal to $\langle\tilde Q,\tilde Q\rangle_{\natural*}$.

*Proof.* The definitions give $\tilde Q^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde Q^{\natural}=2\,\tilde Q\star\tilde Q$ and $\tilde Q^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde Q^{\natural}=2\,\vec Q\times\overline{\vec Q}$, the second by the identification of the antisymmetric part with the cross product. The scalar parts are equal because $\mathrm{Sc}(XY)=\mathrm{Sc}(YX)$ for the plain product.

**Corollary (when one half vanishes).** The two orders are equal exactly when $\vec Q\times\overline{\vec Q}=0$, and their sum vanishes exactly when the two are opposite, $\tilde Q^{\natural}\tilde Q^{*}=-\tilde Q^{*}\tilde Q^{\natural}$.

**Worked witness pairs.** The two named pairs separate the halves.

- On $\tilde Q_1=-i\vec e_z$, $\tilde Q_2=-ie_t$: both orders equal $-\vec e_z$, so the difference vanishes and $\tilde Q_1\star\tilde Q_2=-\vec e_z$ is the first half alone.
- On $\tilde Q_1=\vec e_y$, $\tilde Q_2=\vec e_x$: the first order is $-\vec e_z$ and the second is $\vec e_z$, so the sum vanishes and $\tilde Q_1\star\tilde Q_2=0$, while the two orders differ by $-2\vec e_z$, that is twice the antisymmetric companion $\mathrm{AQS}(\tilde Q_1,\tilde Q_2)=\vec Q_1\times\overline{\vec Q_2}=-\vec e_z$.

The two pairs show the two extreme cases of the split: the two orders coincident, and the two orders opposite.

**Remark.** The half-difference is the algebraic norm of Block 8, $\mathrm{AQS}(\tilde Q_1,\tilde Q_2)=\vec Q_1\times\overline{\vec Q_2}$; the reconstruction $\tilde Q_1^{\natural}\tilde Q_2^{*}=\tilde Q_1\star\tilde Q_2+\vec Q_1\times\overline{\vec Q_2}$ is the introduction's, and here only the case of two equal arguments is read.

## The Named Classes, Carried by the Algebraic Norm

The two named classes of the block are the equations in which the algebraic norm is put against a fixed element, and both are the object of a Common Theory server of the block; this section records only what the algebraic norm itself contributes to them, and cites the computations.

**The square-zero elements.** The equation $\tilde Q\star\tilde Q=0$ is the nilpotent equation of the block; its solution set, the index-two theorem and the conjugation table are *Nilpotents of the Symmetric Quaternionic Sesqualgebra*. The formula for the algebraic norm is what makes the equation readable: it splits $\tilde Q\star\tilde Q=0$ into the scalar condition $\langle\tilde Q,\tilde Q\rangle_{\natural*}=0$ and the centrality condition $Q_t\overline{Q_\mu}\in i\mathbb{R}$ for each $\mu$, and the second condition is the vanishing of the mixed vector part of the algebraic norm.

**The idempotents.** The equation $\tilde Q\star\tilde Q=\tilde Q$ is the idempotent equation; its solution set, the non-orthogonality theorem and the comparison with the plain idempotents are *Idempotents of the Symmetric Quaternionic Sesqualgebra*. The algebraic norm contributes the scalar condition $\langle\tilde\Pi,\tilde\Pi\rangle_{\natural*}=\alpha$, which forces the scalar coordinate of the nontrivial family.

**Remark (the two classes and the algebraic norm).** The idempotents of the block lie in the real quaternion subspace, where the algebraic norm is real-valued; the nilpotents $\alpha(e_t+i\vec u)$ do not, and their algebraic norm vanishes. Both classes are the meeting of the non-central algebraic norm of this article with the element theory of the block.

**Remark (square zero is not isotropy).** The square-zero elements are strictly inside the isotropic set of $\langle\cdot,\cdot\rangle_{\natural*}$, which is $\{\langle\tilde Q,\tilde Q\rangle_{\natural*}=0\}$ and also contains the elements with a nonzero mixed vector part, for instance $e_t+\vec e_x$, which is regular. The isotropic structure is *The Krein Norm of the Biquaternion Algebra*, and the zero divisors of the block are *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

## The Absence of a Unit Carried by the Algebraic Norm

**Theorem (the two one-sided actions).** The two conjugations appear as the two one-sided actions of $e_t$:

$$
e_t\star\tilde Q=\tilde Q^{*},
\qquad
\tilde Q\star e_t=\tilde Q^{\natural}.
$$

On the algebraic norm $\tilde Q\star\tilde Q$ of an element, the two actions give the two conjugations of that element, $\tilde Q^{*}$ and $\tilde Q^{\natural}$, which agree exactly when $\tilde Q$ is real.

*Proof.* $e_t$ is the identity of the plain product, so $e_t\star\tilde Q=\tfrac12(\tilde Q^{*}+\tilde Q^{*})=\tilde Q^{*}$, and the right action is the conjugate-commutative mirror, or the same computation with the factors exchanged. The two conjugations agree exactly when $\overline{\tilde Q}=\tilde Q$, that is when $\tilde Q$ is real.

**Corollary (no unit).** There is no left unit and no right unit.

*Proof.* A left unit forces $\tilde E^{\natural}=e_t$ and hence $\tilde E=e_t$, but $e_t\star \vec e_x=-\vec e_x$; a right unit forces $e_t\star\tilde E=e_t$, that is $\tilde E^{*}=e_t$ and $\tilde E=e_t$, but $\vec e_x\star e_t=-\vec e_x$.

**Remark.** The algebraic norm carries the two actions in the following sense: the two orders of the algebraic norm are the two conjugations of the element read at the two slots, and the unit candidate is the only element whose two actions are conjugations. The one-sided actions of the general quaternionic sesquilinear product are *The Two One-Sided Actions and the Absence of a Unit*, and on the block they are the two displays above.

## Worked Examples

**A central algebraic norm off the centre.** $\tilde Q=2e_t+i\vec e_x$: $\langle\cdot\rangle_{\natural*}=4-1=3$ and the mixed term is $-Q_t\overline{Q_x}-\overline{Q_t}Q_x=-(2)(-i)-(2)(i)=2i-2i=0$; its vanishing makes the vector part $0$, so $\tilde Q\star\tilde Q=3e_t$, central with $Q_t\neq0$. The criterion is read on $Q_t\overline{Q_x}=2(-i)=-2i$, purely imaginary, and it is the imaginary character of $Q_t\overline{Q_\mu}$ — not its reality — that kills the mixed term.

**A square-zero element.** $\tilde Q=e_t+i\vec e_x$: $\langle\cdot,\cdot\rangle_{\natural*}=1-1=0$ and the mixed term $-e_t\overline{(i\vec e_x)}-\overline{e_t}(i\vec e_x)=-(-i)\vec e_x-(i)\vec e_x=i\vec e_x-i\vec e_x=0$, so $\tilde Q\star\tilde Q=0$; here $\alpha=1$ and $\vec c=\vec e_x$ with $|\vec c|^{2}=1=|\alpha|^{4}$.

**An idempotent.** $\tilde Q=-\tfrac12e_t+\tfrac{\sqrt3}{2}\vec e_x$: $|\vec u|^2=1$ and $\tilde Q\star\tilde Q=\tilde Q$; the norm is $\langle\tilde Q\rangle_{\natural}=\tfrac14+\tfrac34=1$.

**The two halves at a vector.** $\tilde Q=\vec e_x$: $\tilde Q^{\natural}\tilde Q^{*}=(-\vec e_x)(-\vec e_x)=-e_t$ and $\tilde Q^{*}\tilde Q^{\natural}=(-\vec e_x)(-\vec e_x)=-e_t$; the two orders coincide, the difference vanishes, and the algebraic norm is $-e_t$.

**Coincident and opposite orders.** $\tilde Q=2e_t+i\vec e_x$: $\tilde Q^{\natural}=2e_t-i\vec e_x$ and $\tilde Q^{*}=2e_t+i\vec e_x$ (the coefficientwise conjugation sends $Q_t$ to $2$ and $Q_x$ to $-i$, and the natural conjugation restores the vector coefficient to $+i$), so the first order is $(2e_t-i\vec e_x)(2e_t+i\vec e_x)=3e_t$ and the second is $(2e_t+i\vec e_x)(2e_t-i\vec e_x)=3e_t$; the two orders coincide, and the algebraic norm is the central value $3e_t$ read in the earlier example. For the pair $\tilde Q_1=\vec e_y$, $\tilde Q_2=\vec e_x$ the two orders are opposite, $-\vec e_z$ and $\vec e_z$, and their sum vanishes.

## Summary

The algebraic norm of the block is the real element $\tilde Q\star\tilde Q=\langle\tilde Q,\tilde Q\rangle_{\natural*}e_t-Q_t\overline{\vec Q}-\overline{Q_t}\vec Q$, with real scalar part $|Q_t|^{2}-\sum_{\mu\in\{x,y,z\}}|Q_\mu|^{2}$ and real vector part $-2\sum_{\mu\in\{x,y,z\}}\mathrm{Re}(Q_t\overline{Q_\mu})\vec e_\mu$. It is central exactly when $Q_t\overline{Q_\mu}\in i\mathbb{R}$ for each $\mu$, and in particular on the whole vector subspace; the two witnesses $\vec e_x$ and $\vec e_x+i\vec e_y$ carry the central values $-e_t$ and $-2e_t$, and $e_t+\vec e_x$ carries the non-central value $-2\vec e_x$. The two halves of the algebraic norm are the two orders $\tilde Q^{\natural}\tilde Q^{*}$ and $\tilde Q^{*}\tilde Q^{\natural}$, with sum $2\,\tilde Q\star\tilde Q$, difference $2\vec Q\times\overline{\vec Q}$, and equal scalar parts; the witness pairs $(-i\vec e_z,-ie_t)$ and $(\vec e_y,\vec e_x)$ exhibit the coincident case and the opposite case. The two named classes of the block, the square-zero elements and the idempotents, are the equations carried by the algebraic norm and are computed in *Nilpotents of the Symmetric Quaternionic Sesqualgebra* and *Idempotents of the Symmetric Quaternionic Sesqualgebra*; the algebraic norm contributes the two conditions $\langle\tilde Q,\tilde Q\rangle_{\natural*}=0$, $Q_t\overline{Q_\mu}\in i\mathbb{R}$ for the first and $\langle\tilde\Pi,\tilde\Pi\rangle_{\natural*}=\alpha$ for the second. The two one-sided actions of $e_t$ are the two conjugations, $\tilde Q^{*}$ and $\tilde Q^{\natural}$, and the block has no unit.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q\star\tilde Q=\langle\tilde Q,\tilde Q\rangle_{\natural*}e_t-Q_t\overline{\vec Q}-\overline{Q_t}\vec Q$ | the algebraic norm, a real element |
| $Q_t\overline{Q_\mu}\in i\mathbb{R}$ for all $\mu$ | the criterion of centrality of the algebraic norm |
| $\vec e_x$, $\vec e_x+i\vec e_y$; $e_t+\vec e_x$ | the two central witnesses; the non-central witness |
| $\tilde Q^{\natural}\tilde Q^{*}$, $\tilde Q^{*}\tilde Q^{\natural}$ | the two halves of the algebraic norm, sum $2\tilde Q\star\tilde Q$, difference $2\vec Q\times\overline{\vec Q}$ |
| $\alpha e_t+(i\alpha/\lvert\alpha\rvert^{2})\vec c$, $\lvert\vec c\rvert^{2}=\lvert\alpha\rvert^{4}$ | the square-zero elements, computed in the nilpotent server |
| $-\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u$, $\lvert\vec u\rvert^{2}=1$ | the idempotents off $0$ and $e_t$, computed in the idempotent server |
| $e_t\star\tilde Q=\tilde Q^{*}$, $\tilde Q\star e_t=\tilde Q^{\natural}$ | the two one-sided actions; no unit |

## Further Reading

- [Introduction to the Symmetric Quaternionic Sesqualgebra](introduction-to-the-symmetric-quaternionic-sesqualgebra.html), for the product and the reconstruction of the general quaternionic sesquilinear product from its two halves.
- [Introduction to the General Quaternionic Sesqualgebra](introduction-to-the-general-quaternionic-sesqualgebra.html), for the unsplit product and its square.
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the antisymmetric companion and the table of the twelve operations.
- [The Two One-Sided Actions and the Absence of a Unit](the-two-one-sided-actions-and-the-absence-of-a-unit.html), for the one-sided actions of the general quaternionic sesquilinear product.
- [The Krein Norm of the Biquaternion Algebra](the-krein-norm-of-the-biquaternion-algebra.html), for the form and its isotropic elements, of which the square-zero family is a part.
- [The Non-Central Algebraic Norm and the Two Halves of the Symmetric Quaternionic Sesqualgebra](the-non-central-algebraic-norm-and-the-two-halves-of-the-symmetric-quaternionic-sesqualgebra.html), the server that owns the square-zero elements carried by the algebraic norm.
- [The Non-Central Algebraic Norm and the Two Halves of the Symmetric Quaternionic Sesqualgebra](the-non-central-algebraic-norm-and-the-two-halves-of-the-symmetric-quaternionic-sesqualgebra.html), the server that owns the idempotents carried by the algebraic norm.
- [Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra](quaternionic-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the norm $\langle\cdot\rangle_{\natural}$.
- [Remarkable Subspaces under the Symmetric Quaternionic Sesqualgebra](remarkable-subspaces-under-the-symmetric-quaternionic-sesqualgebra.html), for the closure of the remarkable subspaces under the product.
