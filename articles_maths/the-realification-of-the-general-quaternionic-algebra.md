# __The Realification of the General Quaternionic Algebra__

## Introduction

The General Quaternionic Algebra is one of the twelve algebraic structures that the biquaternion space $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ carries, the structure carried by the product
$$
\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q,
$$
the general quaternionic bilinear product of *The 12 Products of the Biquaternion Complex Space*, the structure of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. It is an $A$ structure: the product is $\mathbb{C}$-bilinear in both slots. Read over $\mathbb{R}$, the same product on the same set is an $\mathbb{R}$-algebra on the eight-dimensional real space $\mathbb{R}^8$, and this article owns that real reading.

The general construction is not repeated here. The realification of a vector space, of a linear map and of a form, the two rules for forms and the table of the four effects are *The Realification and the Effect of the Change of Scalars*; and the four realified signatures are *The Realification of the Four Forms*. This article gives what is specific to this product: its real bilinear reading, the law of its second slot over the centre, the realification of the form it carries, its real operators and trace form, and the real structures the passage creates.

## The Change of Scalars

$\mathbb{B}$ is the complex vector space of dimension four on the basis $e_0,e_1,e_2,e_3$, with $e_1e_2=e_3$, and the field of scalars is read in the centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$. Read over $\mathbb{R}$ the same set is the real vector space
$$
\mathbb{R}^8=\operatorname{span}_\mathbb{R}\{e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3\},
$$
and the product is the same multiplication table on the same elements. **Restriction of scalars** takes the $\mathbb{C}$-algebra to an $\mathbb{R}$-algebra; there is no new multiplication, only a smaller field. The complex structure is the operator
$$
J:\tilde Y\mapsto i\tilde Y,\qquad J^2=-\mathrm{id},
$$
an $\mathbb{R}$-linear endomorphism of $\mathbb{R}^8$ that has no real eigenvalue, and it is the realification of the central scalar $i$: it is left multiplication by $i$, so $J=L_i$ in the notation of §*The Real Operators and the Trace Form*. It is $\mathbb{C}$-linear as well, since
$$
J(\lambda\tilde Y)=i\lambda\tilde Y=\lambda\,i\tilde Y=\lambda J(\tilde Y)\qquad(\lambda\in\mathbb{C}),
$$
by the centrality of $i$: $J$ commutes with itself, so the criterion for $\mathbb{C}$-linearity of §*The Realification of a Linear Map* is met trivially. What the passage to $\mathbb{R}$ adds is not a new operator but the **visibility** of this one: over $\mathbb{C}$ it is nothing but the scalar $i$, and it is in the real reading that the $\mathbb{C}$-linear maps are singled out as exactly those commuting with it.

Every property written with the addition, the product and quantification over the elements is a statement about the **ring** and does not move when the scalars are restricted to $\mathbb{R}$. For this product the inventory is short and it is worth recalling in one paragraph. The product is **neither associative nor commutative**; $e_0$ is a **left unit** and there is **no right unit**, so there is no two-sided unit and no group of units of the product; the **centre** of the product is trivial; the **idempotents** are $0$ and $e_0$; the **zero divisors** are the nonzero solutions of $N=0$; the **nilpotents** coincide with the zero divisors, the square being $\tilde Q\star\tilde Q=N(\tilde Q)e_0$; and the **left ideals** of the product are exactly the left ideals of the plain product (*Introduction to the General Quaternionic Algebra of Biquaternions*, *The Specificities of the General Quaternionic Algebra*). Each of these is the same set, with the same proof, in the two readings.

What moves is every notion that names the field or the linear structure. The dimension is $8$ over $\mathbb{R}$ against $4$ over $\mathbb{C}$. The centre of the ring, which is $\mathbb{C}_{\mathbb{B}}$ and not the product's own centre, is a field of real dimension two, strictly larger than $\mathbb{R}e_0$; the ring is therefore **central simple over $\mathbb{C}$** and **simple but not central over $\mathbb{R}$**, while the product's own centre is trivial in both readings.

## The Second Slot and the Centre

Over $\mathbb{C}$ the product is $\mathbb{C}$-bilinear, so it is an **algebra** and not a sesqualgebra, and its second slot is $\mathbb{C}$-linear. Read over $\mathbb{R}$ the product remains $\mathbb{R}$-bilinear and its second slot is $\mathbb{C}_{\mathbb{B}}$-linear: for every $\tilde Y$ the left multiplication
$$
L_{\tilde Y}:\tilde Z\mapsto\tilde Y\star\tilde Z
$$
is $\mathbb{C}$-linear over $\mathbb{C}$ — since ${}^{\natural}$ is $\mathbb{C}$-linear and the plain product is $\mathbb{C}$-bilinear, $\tilde Y\star(\lambda\tilde Z)=\lambda(\tilde Y\star\tilde Z)$ for $\lambda\in\mathbb{C}$ — and it is therefore $\mathbb{R}$-linear on $\mathbb{R}^8$ and commutes with the complex structure, $L_{\tilde Y}J=JL_{\tilde Y}$, which is the criterion for $\mathbb{C}_{\mathbb{B}}$-linearity (*The Realification and the Effect of the Change of Scalars*, §*The Realification of a Linear Map*). The passage therefore **does not change the kind** of this product.

Both slots are $\mathbb{C}$-linear here, so the right multiplication $R_{\tilde Y}:\tilde Z\mapsto\tilde Z\star\tilde Y$ commutes with $J$ as well, $R_{\tilde Y}J=JR_{\tilde Y}$, and the pair of commutations is the mark of the $A$ family. In the six $S$ structures of the twelve the second slot is conjugate-linear, so $L_{\tilde Y}$ anticommutes with $J$ there, and the two block shapes of the passage separate the families exactly as the criterion does.

In the real basis the criterion takes a block form. If the complex matrix of a $\mathbb{C}$-linear endomorphism on a $\mathbb{C}$-basis is $A+iB$, the real matrix of the same map on the doubled basis is
$$
\begin{pmatrix}A&-B\\ B&A\end{pmatrix},
$$
the shape that commutes with $J=\begin{pmatrix}0&-\mathrm{I}\\ \mathrm{I}&0\end{pmatrix}$, while a conjugate-linear map has the shape $\begin{pmatrix}A&B\\ B&-A\end{pmatrix}$, the one that anticommutes with it;
the two shapes are the two criteria of §*The Realification of a Linear Map* of *The Realification and the Effect of the Change of Scalars*. Both slots of this product are of the first kind, $\mathbb{C}$-linear and commuting with the structure.

## The Realified Form

The product carries the general quaternionic bilinear form, the scalar part of the general quaternionic product, quoted from *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*:
$$
N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q).
$$
Over $\mathbb{C}$ it is a symmetric bilinear form; a nondegenerate symmetric bilinear form over $\mathbb{C}$ is classified by its rank alone, so its realification is the **split** pair $(\operatorname{Re}N,\operatorname{Im}N)$ of §*The Realification of a Form* of *The Realification and the Effect of the Change of Scalars*, and on the real basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ its Gram matrix is
$$
\operatorname{diag}(\mathrm{I}_4,-\mathrm{I}_4),
$$
of signature $(4,4)$, the second row of the table of *The Realification of the Four Forms*, §*The Four Gram Matrices*. On the realification the complex structure **reverses** the form,
$$
N_{\mathbb{R}}(J\tilde P,J\tilde Q)=-N_{\mathbb{R}}(\tilde P,\tilde Q),
$$
which is the same statement as the two opposite blocks $\mathrm{I}_4$ and $-\mathrm{I}_4$ of the Gram matrix.

**Remark (the realified null set is not the nilpotent cone).** Writing $\tilde Q=\sum_\mu(a_\mu+ib_\mu)e_\mu$ with real $a_\mu,b_\mu$, the diagonal of the realified form is
$$
N_{\mathbb{R}}(\tilde Q,\tilde Q)=\sum_{\mu=0}^{3}\bigl(a_\mu^2-b_\mu^2\bigr),
$$
one real equation, so its zero set is a real hypersurface of dimension $7$ (*The Realification of the Four Forms*, §*The Realified Null Cones*). The $\star$-nilpotents are the solutions of the **complex** equation $N(\tilde Q)=0$, that is of the two real equations $\operatorname{Re}N=0$ and $\operatorname{Im}N=0$, a real cone of dimension $6$ off the apex. The realified null cone therefore strictly contains the nilpotent cone of the product, and the two objects must not be confused: the first is the zero set of the realified form, the second is the set of elements whose square vanishes (*The Isotropic Structure of the General Quaternionic Algebra*).

## The Real Operators and the Trace Form

The left and the right multiplications by an element,
$$
L_{\tilde X}:\tilde Y\mapsto\tilde X\star\tilde Y,\qquad R_{\tilde X}:\tilde Y\mapsto\tilde Y\star\tilde X,
$$
are $\mathbb{C}$-linear over $\mathbb{C}$ and hence $\mathbb{R}$-linear on $\mathbb{R}^8$, and both commute with $J$ by §*The Second Slot and the Centre*; in the real basis their matrices have the block shape above. Their traces carry the dimension ratio, the complex trace counting $\mathrm{Sc}$ with the factor $4$ and the real trace with the factor $8$,
$$
\operatorname{Tr}_{\mathbb{R}}(L_{\tilde X})=8\operatorname{Re}\mathrm{Sc}(\tilde X)=2\operatorname{Re}\operatorname{Tr}_{\mathbb{C}}(L_{\tilde X}).
$$

The trace form of the product is
$$
\tau(\tilde P,\tilde Q)=\operatorname{Tr}_{\mathbb{R}}\bigl(L_{\tilde P}L_{\tilde Q}\bigr).
$$
Since $L_{\tilde P}=L^{\mathrm{plain}}_{\tilde P^{\natural}}$, the composite is the plain left multiplication by $\tilde P^{\natural}\tilde Q^{\natural}$, and $\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{\natural})=\mathrm{Sc}\bigl((\tilde Q\tilde P)^{\natural}\bigr)=\mathrm{Sc}(\tilde Q\tilde P)=B(\tilde P,\tilde Q)$, so
$$
\tau(\tilde P,\tilde Q)=8\operatorname{Re}B(\tilde P,\tilde Q),
$$


## What Is Specific to the Real Interpretation

Three things exist over $\mathbb{R}$ for this product and have no complex counterpart.

**The real form closed under the product.** The quaternion subspace
$$
\mathbb{H}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{e_0,e_1,e_2,e_3\}
$$
is a real form of $\mathbb{B}$ — a real subspace of dimension four with $\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus J\mathbb{H}_{\mathbb{B}}$ — and it is **closed under the product**, on which the product is $h\star h'=\bar h\,h'$ (*The Quaternionic Product on the Quaternion Subspace*). The closure, together with the $\mathbb{C}$-bilinearity of the two slots, gives the four inclusions
$$
\mathbb{H}_{\mathbb{B}}\star\mathbb{H}_{\mathbb{B}}\subseteq\mathbb{H}_{\mathbb{B}},\qquad
\mathbb{H}_{\mathbb{B}}\star i\mathbb{H}_{\mathbb{B}}\subseteq i\mathbb{H}_{\mathbb{B}},\qquad
i\mathbb{H}_{\mathbb{B}}\star\mathbb{H}_{\mathbb{B}}\subseteq i\mathbb{H}_{\mathbb{B}},\qquad
i\mathbb{H}_{\mathbb{B}}\star i\mathbb{H}_{\mathbb{B}}\subseteq\mathbb{H}_{\mathbb{B}},
$$
so that $\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$ is a $\mathbb{Z}/2$-grading for the product (*Introduction to the General Quaternionic Algebra of Biquaternions*, §*The Quaternion Subspace and Its Imaginary*). Closure under the product is what makes a real form a real **subalgebra**, and the grading is the real reading of the complex structure exchanging the two summands; the complex reading has neither, because it cannot single out a real subspace.

**The odd-dimensional subalgebras.** A subalgebra of the complex reading is a complex subspace, of even real dimension; over $\mathbb{R}$ there is no parity restriction. The three-dimensional real subspace
$$
\mathbb{R}\{e_0,\ e_1+ie_2,\ ie_1-e_2\}
$$
is closed under the product: its two non-unit generators are orthogonal for $N$ and have vanishing square and vanishing product,
$$
(e_1+ie_2)\star(e_1+ie_2)=(ie_1-e_2)\star(ie_1-e_2)=(e_1+ie_2)\star(ie_1-e_2)=0,
$$
and $e_0$ acts on the left by the identity and on the right by the natural conjugation, which sends each generator to its negative; every product therefore stays in the span. This is the smallest illustration that the real reading carries subalgebras the complex reading cannot see.

**The trace form.** By §*The Real Operators and the Trace Form* the trace form of the product is $8\operatorname{Re}B(\tilde P,\tilde Q)$, a real symmetric bilinear form of signature $(4,4)$ and zero radical, the realified general plain bilinear form. It is the same real form as the trace form of the general plain algebra: the two products, one associative with a two-sided unit and one not associative with a left unit alone, have the same trace form, and the conjugation that separates them is invisible to the trace.

The other two real objects of the ring — the Galois-twisted automorphism group $\operatorname{Aut}_{\mathbb{R}}(\mathbb{B})=\operatorname{Aut}_{\mathbb{C}}(\mathbb{B})\rtimes\mathbb{Z}/2$ and the real models $M_2(\mathbb{C})$, $M_4(\mathbb{C})_L$ and $\mathrm{Cl}^+_{1,3}(\mathbb{R})$ — are shared by the twelve products and belong to the **ring** and not to this product: the automorphisms and the models are §*What Is Specific to the Real Interpretation* of *The Realification of the General Plain Algebra*. They are cited here and not repeated.

## Summary

Read over $\mathbb{R}$ the General Quaternionic Algebra is the same product on the same elements, an $\mathbb{R}$-algebra on $\mathbb{R}^8$ that is neither associative nor commutative, has the left unit $e_0$ and no right one, has trivial centre, and has $0$ and $e_0$ for its only idempotents; the zero divisors are the nonzero solutions of $N=0$, and the left ideals are the left ideals of the plain product. Its second slot is $\mathbb{C}_{\mathbb{B}}$-linear, and both multiplications commute with $J$. It carries the general quaternionic bilinear form $N$, whose realification has Gram matrix $\operatorname{diag}(\mathrm{I}_4,-\mathrm{I}_4)$ and signature $(4,4)$, is reversed by $J$, and has a null cone of dimension $7$ strictly larger than the complex nilpotent cone of dimension $6$. Its trace form is $8\operatorname{Re}B$, the same real form as the plain algebra's, and the conjugation twist is invisible to it. Three things are genuinely real: the real form $\mathbb{H}_{\mathbb{B}}$ closed under the product with the grading $\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$, the odd-dimensional subalgebras such as $\mathbb{R}\{e_0,e_1+ie_2,ie_1-e_2\}$, and the trace form itself, which exists only as a form of the real regular representation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ | the product of the General Quaternionic Algebra |
| $\mathbb{R}^8$ | the realification of $\mathbb{B}$, basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre of the ring, the field of scalars read over $\mathbb{R}$ |
| $J=L_i$ | multiplication by $i$, the complex structure, of square $-1$ |
| $N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$ | the general quaternionic bilinear form carried by the product |
| $B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)$ | the general plain bilinear form, the form of the trace form |
| $\operatorname{diag}(\mathrm{I}_4,-\mathrm{I}_4)$ | Gram matrix of the realified form $N$, of signature $(4,4)$ |
| $L_{\tilde X}$, $R_{\tilde X}$ | the left and the right multiplications, $\mathbb{C}_{\mathbb{B}}$-linear on $\mathbb{R}^8$ |
| $\tau(\tilde P,\tilde Q)=\operatorname{Tr}_{\mathbb{R}}(L_{\tilde P}L_{\tilde Q})$ | the trace form, $=8\operatorname{Re}B(\tilde P,\tilde Q)$, signature $(4,4)$ |
| $\mathbb{H}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{e_0,e_1,e_2,e_3\}$ | the real form closed under the product, with $\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$ |

## Further Reading

- *The Realification and the Effect of the Change of Scalars* (`articles_maths/the-realification-and-the-effect-of-the-change-of-scalars.md`), for the general construction, the two rules of the realification of a form and the table of the four effects.
- *The Realification of the Four Forms* (`articles_maths/the-realification-of-the-four-forms.md`), for the four realified Gram matrices, the four signatures and the realified null cones.
- *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-12-algebraic-structures-over-the-biquaternion-c-space.md`) and *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternion-c-space.md`), for the twelve structures and the four forms of which this article is the real reading of one row.
- *Introduction to the General Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-biquaternions.md`) and *The Specificities of the General Quaternionic Algebra* (`articles_maths/the-specificities-of-the-general-quaternionic-algebra.md`), for the complex reading of the product, its ring inventory and the left ideals, which the passage to $\mathbb{R}$ does not change.
- *The Realification of the General Plain Algebra* (`articles_maths/the-realification-of-the-general-plain-algebra.md`), for the real reading of the ring itself, its trace form and its models $M_2(\mathbb{C})$, $M_4(\mathbb{C})_L$ and $\mathrm{Cl}^+_{1,3}(\mathbb{R})$, which are shared by the twelve products.
- *The Isotropic Structure of the General Quaternionic Algebra* (`articles_maths/the-isotropic-structure-of-the-general-quaternionic-algebra.md`), for the complex null cone of $N$, the zero divisors and the totally isotropic planes, which this article's realified cone strictly contains.
