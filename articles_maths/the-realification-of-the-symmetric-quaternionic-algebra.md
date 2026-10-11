# __The Realification of the Symmetric Quaternionic Algebra__

## Introduction

The Symmetric Quaternionic Algebra is the structure that the biquaternion ring $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries when the multiplication is the quaternion form $N$ of the quaternionic family read as a product,
$$
\tilde P\star\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P\bigr)=N(\tilde P,\tilde Q)\,e_0,\qquad N(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q),
$$
the operation that is commutative, central-valued and devoid of a unit (*Introduction to the Symmetric Quaternionic Algebra of Biquaternions*). Over $\mathbb{C}$ it is the row $\mathrm{SQA}$ of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; read over $\mathbb{R}$ the same operation on the same elements is an $\mathbb{R}$-bilinear product on the eight-dimensional real space, and this article owns that real reading. The operation is written $\star$ in this entry, the mark of the block; *The Specificities of the Symmetric Quaternionic Algebra* writes it $\bullet$, and the two marks denote one multiplication.

The general construction is not repeated here. The realification of a vector space, of a linear map and of a form, the doubling of the dimension, the complex structure $J$, the two rules for forms and the table of the four effects are *The Realification and the Effect of the Change of Scalars*, whose sibling for the plain product is *The Realification of the General Plain Algebra*. The form of this block and its realified signature are computed in *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*, §*The Realification and the Signature*; the operators are *The Multiplication Operators of the Symmetric Quaternionic Algebra*; the subspaces are *Remarkable Subspaces under the Symmetric Quaternionic Algebra of Biquaternions*. Those articles are cited and not repeated. What this article adds is the change of scalars framed for this block: the collapse read over $\mathbb{R}$, the subalgebras that only the real reading has, and the real trace of the multiplication.

## The Change of Scalars for This Block

Over $\mathbb{C}$ the space is $\mathbb{B}$, of complex dimension four on the basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$, and the centre is the line $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$. Read over $\mathbb{R}$ the same set is
$$
\mathbb{R}^8=\operatorname{span}_{\mathbb{R}}\{e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3\},
$$
of real dimension eight, and the product is the same table on the same elements, $e_\mu\star e_\nu=\delta_{\mu\nu}e_0$. The complex structure is the multiplication by the central element $i$,
$$
J:\tilde Y\mapsto i\tilde Y,\qquad J^2=-\mathrm{id},
$$
an $\mathbb{R}$-linear endomorphism of $\mathbb{R}^8$ that is $\mathbb{C}$-linear, since it commutes with the complex scalars, $J(i\tilde Y)=iJ(\tilde Y)$, and therefore not conjugate-linear, the conjugate-linear maps being the ones that anticommute with it.

**The dictionary.** Every notion the block reads from the ring alone is unchanged: the commutativity, the failure of associativity, of power-associativity, of the Jordan identity and of the Jacobi identity, the centrality of the value, the image, the absence of a unit, and the idempotents, the nilpotents and the zero divisors. Such a notion is a polynomial identity with integer coefficients in the structure constants, or a condition quantified over the elements of $\mathbb{B}$, and it is evaluated on the same additive group and the same product in the two readings; the carrier of the invariance is the central element $i\in\mathbb{B}$ (*The Realification and the Effect of the Change of Scalars*, §*The Four Effects on a Structure*). What moves is every notion that names the field, the first of them the dimension: the block is a $\mathbb{C}$-algebra of complex dimension four and an $\mathbb{R}$-algebra of real dimension eight.

**The collapse, read in the field.** The product is central-valued, so its image is the central line $\mathbb{C}_{\mathbb{B}}$, of complex dimension one. Read over $\mathbb{R}$ that image is the realification of the line, the real plane spanned by $e_0$ and $ie_0$, of real dimension two, while the space is $\mathbb{R}^8$. The collapse is accordingly an $\mathbb{R}$-bilinear map whose image is the real plane of the centre, the same plane for every pair of arguments. The two numbers to keep are the two of the image and the eight of the space; the six belongs to the kernel, in §*The Real Operators* below.

## The Product Read over $\mathbb{R}$

**Proposition (the real algebra).** The operation $\star$ is $\mathbb{R}$-bilinear, hence an algebra over $\mathbb{R}$ on $\mathbb{R}^8$ in the broad sense, the sense of a module with a bilinear multiplication. In it commutativity holds, associativity fails, power-associativity fails, the Jordan identity fails and the Jacobi identity fails, and there is no one-sided unit.

*Proof.* The class is the one recorded for the $A$ family of the twelve (*The Realification and the Effect of the Change of Scalars*, §*The Effect on the Twelve Algebraic Structures*), and each law is the corresponding statement of *Introduction to the Symmetric Quaternionic Algebra of Biquaternions*, §*The Laws of the Operation* and §*The Image and the Unit*; being a statement about the ring, each is unchanged by the dictionary above. The witness of the failure of associativity, $\tilde P=\tilde Q=e_1$, $\tilde R=e_0$, has $(\tilde P\star\tilde Q)\star\tilde R=e_0\ne0=\tilde P\star(\tilde Q\star\tilde R)$, and it lies in the real span, so it serves in the real reading as in the complex one.

**Proposition (the coefficient over $\mathbb{R}$).** Read over $\mathbb{R}$, the coefficient $N$ is a symmetric $\mathbb{R}$-bilinear pairing of $\mathbb{R}^8\times\mathbb{R}^8$ into the centre $\mathbb{C}$, and it is nondegenerate: the only element paired to zero with every element of $\mathbb{R}^8$ is $0$. Its real part is the realification of the form, of rank eight and signature $(4,4)$, with Gram matrix $\operatorname{diag}(\mathrm{I}_4,-\mathrm{I}_4)$; its imaginary part is the companion of the split pair of §*The Realification of a Form*, a second real symmetric form of the same signature $(4,4)$, with Gram matrix the swap block $\left(\begin{smallmatrix}0&\mathrm{I}_4\\ \mathrm{I}_4&0\end{smallmatrix}\right)$. The two-sided annihilator of the product is $\{0\}$.

*Proof.* The pairings $\tilde R\mapsto N(\tilde A,\tilde R)$ vanish on the whole real basis exactly when $N(\tilde A,e_\mu)=A_\mu=0$ and $N(\tilde A,ie_\mu)=iA_\mu=0$ for every $\mu$, which forces $\tilde A=0$; the same computation on the complex basis is the radical $\{0\}$ of $N$ over $\mathbb{C}$. The realified Gram matrix $\operatorname{diag}(\mathrm{I}_4,-\mathrm{I}_4)$ is invertible, so the realification is nondegenerate of rank eight and signature $(4,4)$ by §*The Realified Form* below; the annihilator of the product is the radical of the pairing (*The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*).

**Proposition (the centre is a subalgebra).** For central elements, $(\lambda e_0)\star(\mu e_0)=\lambda\mu\,e_0$, so the centre $\mathbb{C}_{\mathbb{B}}$ is a subalgebra, of real dimension two and isomorphic to $\mathbb{C}$, and the real line $\mathbb{R}e_0$ is a subalgebra of real dimension one.

*Proof.* The product of two elements of the central line lies on the central line, and $N(\lambda e_0,\mu e_0)=\lambda\mu$; the real line is the intersection of the central line with the real reading of the coefficient field.

## The Second Slot and the Centre

Over $\mathbb{C}$ the operation is $\mathbb{C}$-bilinear, so the block is an algebra and not a sesqualgebra, and its two slots are linear. Read over $\mathbb{R}$ the operation remains $\mathbb{R}$-bilinear, and its second slot is $\mathbb{C}_{\mathbb{B}}$-linear: by §*The Realification of a Linear Map* of *The Realification and the Effect of the Change of Scalars*, the multiplication by a central element $\lambda$ commutes with the complex structure, $L_\lambda J=J L_\lambda$, which is the criterion for $\mathbb{C}_{\mathbb{B}}$-linearity. The passage therefore does not change the kind of this product; the block is an algebra over $\mathbb{C}$ and an algebra over $\mathbb{R}$.

No sesqualgebra appears in the real reading. A sesqualgebra over $\mathbb{R}$ requires a nontrivial involution of $\mathbb{R}$, and the only automorphism of $\mathbb{R}$ is the identity, so a sesquilinear law whose involution is the identity is a bilinear law; the count of sesqualgebras over $\mathbb{R}$ among the twelve is zero (*The Realification and the Effect of the Change of Scalars*, §*The Effect on the Twelve Algebraic Structures*). The distinction between the linear and the conjugate-linear second slot, where it survives, is read over the centre $\mathbb{C}_{\mathbb{B}}$, and this block stands on the linear side, so the distinction does not touch it.

In the real basis the criterion takes the block shape: if $A+iB$ is the complex matrix of the multiplication on the complex basis, the real matrix on the doubled basis is
$$
\begin{pmatrix}A&-B\\ B&A\end{pmatrix},
$$
the shape that commutes with $J$.

## The Realified Form

The form carried by the product is the quaternion form $N$, and its realification is computed in the block and quoted here. In the real basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ the realified form is
$$
\operatorname{diag}(\mathrm{I}_4,-\mathrm{I}_4),
$$
of signature $(4,4)$ and index four, and the complex structure reverses the realification,
$$
\Phi_{\mathbb{R}}(JP,JQ)=-\Phi_{\mathbb{R}}(P,Q),
$$
which is the statement of the two opposite blocks of the Gram matrix; the verification is *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*, §*The Realification and the Signature*. The restriction to the quaternion subspace is positive definite, of signature $(4,0)$, the restriction to the anti-quaternion subspace is negative definite, of signature $(0,4)$, and the two Hermitian subspaces carry the two real light cones (*Remarkable Subspaces under the Symmetric Quaternionic Algebra of Biquaternions*).

The isotropic set $\{N=0\}$ has complex dimension three and real dimension six, and its nonzero elements are exactly the square-zero elements of the block and the zero-divisor set that the four general products share. That set is strictly smaller than the zero-divisor set of the block itself, which is everything but the origin, so the isotropic cone, the square-zero elements and the block's zero divisors are three different sets and are kept apart (*Zero Divisors of the Symmetric Quaternionic Algebra*, *Nilpotents of the Symmetric Quaternionic Algebra*). A fourth set is distinguished from all three: the null cone of the realified form, the real hypersurface $\{\operatorname{Re}N=0\}$ of dimension seven, which contains the complex isotropic cone and is the zero set of the real form and not the square-zero set of the block (*The Realification of the Four Forms*, §*The Realified Null Cones*).

## The Real Operators

The product is commutative, so the left and the right multiplication by an element coincide,
$$
L_{\tilde A}\tilde R=R_{\tilde A}\tilde R=N(\tilde A,\tilde R)\,e_0,
$$
and both are $\mathbb{R}$-linear endomorphisms of $\mathbb{R}^8$. In the complex basis the matrix of $L_{\tilde A}$ carries the four coordinates of $\tilde A$ in its first row and carries zero elsewhere; for $\tilde A\ne0$ the complex rank is one and the real rank is two, the image is the central line $\mathbb{C}_{\mathbb{B}}$ — the same real plane for every nonzero $\tilde A$ — and the kernel is the hyperplane $\{\tilde R:N(\tilde A,\tilde R)=0\}$, of real dimension six. The passage to $\mathbb{R}$ doubles the rank of a $\mathbb{C}$-linear map and turns the complex line of the image into a real plane.

**Proposition (the two traces).** For every $\tilde A$,
$$
\operatorname{Tr}_{\mathbb{C}}\bigl(L_{\tilde A}\bigr)=A_0=\operatorname{Sc}(\tilde A),\qquad
\operatorname{Tr}_{\mathbb{R}}\bigl(L_{\tilde A}\bigr)=2\operatorname{Re}A_0=2\operatorname{Re}\operatorname{Sc}(\tilde A),
$$
and the determinant vanishes in both readings.

*Proof.* Only the entry $(0,0)=A_0$ of the complex matrix is diagonal, so the complex trace is $A_0$; the real trace of the realification of a $\mathbb{C}$-linear map is twice the real part of its complex trace, and the determinant vanishes because the rank is one on a complex space of dimension four (*The Multiplication Operators of the Symmetric Quaternionic Algebra*, §*The Operators, Their Matrices and Their Ranks*).

The factor is two, not the four of the regular representation of the plain algebra and not the eight of its realification. The reason is that the multiplication of this block is the rank-one layer: the trace sees the scalar part of the multiplier and nothing else, the vector part being invisible to it, so the trace form of the block is not of the kind *The Realification of the General Plain Algebra* records for the plain product, where the trace of the composite is the nondegenerate form $8\operatorname{Re}B$. It is the trace of a composite,
$$
\operatorname{Tr}_{\mathbb{R}}\bigl(L_{\tilde A}L_{\tilde B}\bigr)=2\operatorname{Re}(A_0B_0),
$$
a real symmetric bilinear form of rank two whose radical is the vector subspace; it is degenerate, the trace form of the rank-one operator layer and not of a unital algebra.

**Proposition (composition and the adjoint).** The multiplications compose by
$$
L_{\tilde A}\circ L_{\tilde B}=A_0L_{\tilde B},\qquad\text{so}\qquad L_{\tilde A}^{2}=A_0L_{\tilde A},
$$
the map $\tilde A\mapsto L_{\tilde A}$ is injective and is not multiplicative, and the adjoint with respect to the realified form is the realification of the complex adjoint,
$$
\bigl(L_{\tilde A}\bigr)^{\dagger}\tilde Y=\sum_{\mu=0}^{3}A_\mu Y_0\,e_\mu ,
$$
which is self-adjoint exactly for a central multiplier. Every statement is the one of *The Multiplication Operators of the Symmetric Quaternionic Algebra*, §*Composition and the Algebra of Operators* and §*The Adjoint with Respect to the Form*, read in the real basis.

**The group of linear maps preserving the form.** Over $\mathbb{C}$ the maps preserving $N$ form the complex group $G_N$ of complex dimension six. Over $\mathbb{R}$ the $\mathbb{R}$-linear maps preserving the realified form are the linear maps preserving the split form $\operatorname{diag}(\mathrm{I}_4,-\mathrm{I}_4)$ on $\mathbb{R}^8$, of real dimension twenty-eight, and this group contains the realification of $G_N$, of real dimension twelve, as the subgroup of the maps that commute with $J$. The real form-preserving group is therefore the larger one, because a real map preserving $\operatorname{Re}N$ need not commute with the complex structure (*The Multiplication Operators of the Symmetric Quaternionic Algebra*, §*The Two Groups of Linear Maps*).

## What Is Specific to the Real Interpretation

Four features appear in the real reading of the block and not in its complex reading.

**The real subalgebras that are not complex subspaces.** Over $\mathbb{C}$ a subalgebra of the block is a complex subspace, hence of even real dimension. Over $\mathbb{R}$ the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and the Hermitian subspace $\mathbb{M}_+$ are subalgebras: the coefficient $N$ is real on each of them, so the product of two of their elements lies in the real line $\mathbb{R}e_0$ and stays inside. Neither is a complex subspace, since $ie_0$ leaves $\mathbb{H}_{\mathbb{B}}$ and $ie_1$ leaves $\mathbb{M}_+$, so neither is a subalgebra of the complex reading. There are also subalgebras of odd real dimension: the span
$$
\mathbb{R}\{e_0,\ e_1+ie_2,\ ie_1-e_2\}
$$
is kept inside itself, because $e_0$ pairs to zero with the two other generators and those two are isotropic and pair to zero with each other, so every product of two of the three generators is $0$ or in $\mathbb{R}e_0$; its real dimension is three, and it has no complex counterpart. The staying inside and the leaving of the six remarkable subspaces are tabulated in *Remarkable Subspaces under the Symmetric Quaternionic Algebra of Biquaternions*.

**The coincidence on the real part.** On the real subspace $\mathbb{H}_{\mathbb{B}}=\mathbb{R}e_0+\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3$ the symmetric quaternionic product and the symmetric plain sesquilinear product agree, $\mathrm{SQA}=\mathrm{SPS}$, because on real elements the Hermitian form $H$ equals the quaternion form $N$; off that subspace they differ. The twelve operations of the complex space therefore collapse to ten on the real part, and the block is not distinguished there from the row $\mathrm{SPS}$ (*Introduction to the Symmetric Quaternionic Algebra of Biquaternions*, §*The Placement Among the Twelve*; *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*).

**The trace factor.** The complex trace of the multiplication is the scalar part $A_0$ and the real trace is $2\operatorname{Re}A_0$; the factor two is the doubling of the realification, and the absence of the factors four and eight that the regular representation of the plain algebra carries is the rank-one nature of the block, a feature that the real reading shows and the complex reading hides.

**The conjugate-linear automorphisms.** Over $\mathbb{C}$ the automorphisms of the block are the $\mathbb{C}$-linear ones, and the natural conjugation is among them, because the block is commutative with central values. The star and the Hermitian conjugation preserve the product as well, and they are conjugate-linear; since the block is commutative, they are automorphisms of the $\mathbb{R}$-algebra and not of the $\mathbb{C}$-algebra, so the real automorphism group carries the extra conjugate-linear coset of the complex one, which the complex reading does not see. The block's article calls them *conjugations* of the block for this reason (*Norm and Invertibility in the Symmetric Quaternionic Algebra*).

## Summary

The Symmetric Quaternionic Algebra read over $\mathbb{R}$ is the same product on the same elements, an $\mathbb{R}$-algebra on $\mathbb{R}^8$ that is commutative, non-associative and without a unit, with image the real plane of the centre and with a coefficient form whose realification is nondegenerate of signature $(4,4)$ and reversed by the complex structure. Its second slot is $\mathbb{C}_{\mathbb{B}}$-linear, no sesqualgebra appears in the real reading, and every notion read from the ring alone is unchanged. The real reading adds the real subalgebras that are not complex subspaces, of which one has odd real dimension, the coincidence with the symmetric plain sesqualgebra on the real part, the rank-one trace of the multiplication, whose complex value is the scalar part and whose real value is twice its real part, and the conjugate-linear automorphisms, which make the real automorphism group twice the complex one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P\bigr)=N(\tilde P,\tilde Q)e_0$ | the product of the block |
| $\mathbb{R}^8$ | the realification of $\mathbb{B}$, basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre, the image of the product, a real plane over $\mathbb{R}$ |
| $J$ | the complex structure $L_i$, $\mathbb{R}$-linear and $\mathbb{C}$-linear, of square $-\mathrm{id}$ |
| $N$, $(4,4)$ | the coefficient form and the signature of its realification |
| $L_{\tilde A}$ | the multiplication, $\operatorname{Tr}_{\mathbb{C}}=A_0$, $\operatorname{Tr}_{\mathbb{R}}=2\operatorname{Re}A_0$, real rank two |
| $\mathbb{H}_{\mathbb{B}},\ \mathbb{M}_+$ | real subalgebras that are not complex subspaces |
| $\mathrm{SQA}=\mathrm{SPS}$ | the coincidence on the real part |

## Further Reading

- *The Realification and the Effect of the Change of Scalars* (`articles_maths/the-realification-and-the-effect-of-the-change-of-scalars.md`), for the general construction, the complex structure $J$, the two rules of the realification of a form and the table of the four effects.
- *The Realification of the General Plain Algebra* (`articles_maths/the-realification-of-the-general-plain-algebra.md`), the sibling entry for the plain product, whose real trace form $\tau=8\operatorname{Re}B$ this article contrasts with the rank-one trace of the block.
- *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra* (`articles_maths/the-quaternion-form-as-a-product-on-the-symmetric-quaternionic-algebra.md`), for the form $N$, its Gram matrix and the realified signature $(4,4)$.
- *The Realification of the Four Forms* (`articles_maths/the-realification-of-the-four-forms.md`), for the four realified Gram matrices, the four signatures, the four realified null cones and the distinction between a realified cone and a complex cone.
- *The Multiplication Operators of the Symmetric Quaternionic Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-algebra.md`), for the matrices, the ranks, the traces, the composition law, the adjoint and the two groups of linear maps.
- *Remarkable Subspaces under the Symmetric Quaternionic Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-symmetric-quaternionic-algebra-of-biquaternions.md`), for the product on each remarkable subspace and the table of their staying inside themselves.
- *Introduction to the Symmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-biquaternions.md`) and *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the operation, its laws, its placement among the twelve and the collapse of the twelve to ten on the real part.
