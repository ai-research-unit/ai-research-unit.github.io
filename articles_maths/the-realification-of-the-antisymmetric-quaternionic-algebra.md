# __The Realification of the Antisymmetric Quaternionic Algebra__

## Introduction

The Antisymmetric Quaternionic Algebra is one of the twelve algebraic structures that the biquaternion space of $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ carries, the structure $\mathrm{AQA}$ of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. Its product, the antisymmetric quaternionic bilinear product, is
$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P\bigr)=P_0\vec Q-Q_0\vec P-\vec P\times\vec Q,
$$
and this article owns it read over $\mathbb{R}$: the same product on the same set is an $\mathbb{R}$-algebra on the eight-dimensional real space $\mathbb{R}^8$.

The general construction is not repeated here. The realification of a vector space, of a linear map and of a form, the two rules for forms, the table of the four effects and the dictionary of the statements about the ring and of the statements about the scalars are *The Realification and the Effect of the Change of Scalars*. This article gives what is specific to this product: its real bilinear reading and the properties that do not move, the law of its second slot over the centre, the realification of the two forms the block carries, its real operators, and the features that only the real reading shows.

## The Product Read over $\mathbb{R}$

The product is antisymmetric quaternionic bilinear over $\mathbb{C}$, hence $\mathbb{R}$-bilinear, by §*The Effect on the Twelve Algebraic Structures* of *The Realification and the Effect of the Change of Scalars*. It is therefore an **$\mathbb{R}$-algebra** on $\mathbb{R}^8$ in the broad sense, the sense of a module with a bilinear multiplication. In that algebra alternation holds, the Jacobi identity fails, there is no unit, and the scalar part vanishes.

Every ring-theoretic property of the product is the same in the two readings, by the dictionary of the same article, §*The Four Effects on a Structure*: a condition written with the addition, the product, $e_0$ and quantification over the elements is a statement about the ring, and the change of scalars leaves the additive group, the product and the identity untouched. The vanishing of the square, the alternation, the absence of a unit on either side, the vanishing of the scalar part and the failure of the Jacobi identity are of that kind, and the witness of the failure is the same in the two readings: the cyclic sum of the block is a polynomial identity with integer coefficients in the structure constants, so the triple $(e_0,e_1,e_2)$ of the complex basis has the cyclic sum $-e_3$ over $\mathbb{R}$ as well (*Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*, §*The Jacobi Identity*).

What the real reading adds is the real shape of the objects the product carries. The image of the product is the vector subspace $\mathrm{Vect}(\mathbb{B})$, of complex dimension three and **real dimension six**, and the centre $\mathbb{C}_{\mathbb{B}}$, of real dimension two, meets it at the origin alone: the two dimensions are the two readings of one subspace. The features that the real reading brings and the complex reading does not are gathered in §*What Is Specific to the Real Interpretation*.

## The Second Slot and the Centre

Over $\mathbb{C}$ the product is $\mathbb{C}$-bilinear, so it is an **algebra** and not a sesqualgebra, and its second slot is $\mathbb{C}$-linear. Read over $\mathbb{R}$, the product remains $\mathbb{R}$-bilinear and its second slot is $\mathbb{C}_{\mathbb{B}}$-linear: by §*The Realification of a Linear Map* of *The Realification and the Effect of the Change of Scalars*, the left multiplication commutes with the complex structure,
$$
L_{\tilde X}J=JL_{\tilde X},\qquad J=L_i ,
$$
which is the criterion for $\mathbb{C}_{\mathbb{B}}$-linearity. The passage therefore **does not change the kind** of this product: it is an algebra over $\mathbb{C}$ and an algebra over $\mathbb{R}$, with the same linearity of the second slot once the centre is named as the field.

In the real basis the criterion takes a block form. The matrix of $L_{\tilde X}$ in the real basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ is
$$
\begin{pmatrix} A & -B \\ B & A \end{pmatrix},
$$
the matrix of a $\mathbb{C}$-linear map in a real basis adapted to a complex structure, where $A+iB$ is its matrix in the complex basis $e_0,e_1,e_2,e_3$; the shape commutes with $J=\begin{pmatrix}0&-\mathrm{I}\\ \mathrm{I}&0\end{pmatrix}$. The matrix of the block is displayed in this form in *The Adjoint Operators of the Antisymmetric Quaternionic Algebra*, §*The Left Multiplication Operator*.

## The Forms the Block Carries over $\mathbb{R}$

The form of an operation is its scalar part (*The 4 Forms over the Biquaternion $\mathbb{C}$ Space*), and the scalar part of the value is zero here, every value of the block being a pure vector; the table of *The 12 Products of the Biquaternion Complex Space* carries the entry $[0]$ in the scalar-part column of its row. The product therefore carries the **zero form**, counted as no form rather than as a fifth, and there is nothing for the realification of a form to act on; the coefficient form of the block, the bilinear form that would read that scalar part, is the zero form (*The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra*, §*The Trace Form Vanishes*).

The block does carry two two-argument objects of its own, and they are read off the invariance condition and the operators in *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra*: the invariant form
$$
\varphi(\tilde P,\tilde Q)=P_0Q_0 ,
$$
the unique $\mathbb{C}$-bilinear form invariant under the block, of rank one over $\mathbb{C}$ and of radical the vector subspace; and the operator trace form
$$
K(\tilde A,\tilde B)=\operatorname{Tr}\bigl(L_{\tilde A}L_{\tilde B}\bigr)=3A_0B_0-2\sum_{k=1}^{3}A_kB_k ,
$$
non-degenerate over $\mathbb{C}$ and **not** invariant. Both are symmetric $\mathbb{C}$-bilinear, and a symmetric bilinear form over $\mathbb{C}$ is classified by its rank alone, so each realifies by the first of the two rules of §*The Realification of a Form* of *The Realification and the Effect of the Change of Scalars*: the real part and the imaginary part of the form are two real symmetric bilinear forms, the realified Gram matrix consists of two opposite blocks $\operatorname{diag}(D,-D)$, with $D$ the Gram matrix of the complex form, and a complex form of rank $r$ realifies to the **split** signature $(r,r)$.

| form | complex reading | realified signature | radical over $\mathbb{R}$ |
|---|---|---|---|
| $\varphi$ | symmetric $\mathbb{C}$-bilinear, complex rank $1$, radical the vector subspace | $(1,1)$ | the realified vector subspace, real dimension $6$ |
| $K$ | symmetric $\mathbb{C}$-bilinear, complex rank $4$, radical $0$ | $(4,4)$ | $0$ |

On the real basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ the realified Gram matrices are
$$
\operatorname{diag}(1,0,0,0,-1,0,0,0),
\qquad
\operatorname{diag}(3,-2,-2,-2,-3,2,2,2).
$$
The first is the realification of the invariant form, whose entries are $1$ at $e_0$, $-1$ at $ie_0$ and zero elsewhere; the second is the realification of the operator trace form, non-degenerate, and it fails invariance exactly as $K$ does, at the triple $(e_0,e_1,e_1)$ with the value $-4$.

The complex structure reverses both realifications,
$$
\Phi_{\mathbb{R}}(J\tilde P,J\tilde Q)=-\Phi_{\mathbb{R}}(\tilde P,\tilde Q),
$$
the sign of the bilinear slot, and the two Gram matrices above are the two opposite blocks $D$ and $-D$ of the same rule. The signatures are the split ones of the table, $(1,1)$ and $(4,4)$. Neither realified form is one of the four forms of *The Realification of the Four Forms*, which are the forms of the space and not of the block, and the failure of $\operatorname{Re}K$ is the same obstruction as the Jacobi failure.

## The Real Operators

The left and the right multiplications by an element are the maps
$$
L_{\tilde X}:\tilde Y\mapsto\tilde X\diamond\tilde Y,\qquad R_{\tilde X}:\tilde Y\mapsto\tilde Y\diamond\tilde X,
$$
and over $\mathbb{R}$ they are $\mathbb{R}$-linear endomorphisms of $\mathbb{R}^8$, by §*The Realification of a Linear Map* of *The Realification and the Effect of the Change of Scalars*. Because the second slot is $\mathbb{C}_{\mathbb{B}}$-linear, the left multiplication is $\mathbb{C}_{\mathbb{B}}$-linear as well, and its real trace is twice the real part of its complex trace; the complex trace of the block is $3X_0$, the sum of the three diagonal entries $X_0$ on the vector lines (*The Adjoint Operators of the Antisymmetric Quaternionic Algebra*, §*The Trace, the Rank and the Characteristic Polynomial*), so
$$
\operatorname{Tr}_{\mathbb{R}}\bigl(L_{\tilde X}\bigr)=2\operatorname{Re}\operatorname{Tr}_{\mathbb{C}}\bigl(L_{\tilde X}\bigr)=6\operatorname{Re}X_0 .
$$
The factor is six and not the eight of the general plain algebra, whose regular representation has the complex trace $4\,\mathrm{Sc}$ and the real trace $8\operatorname{Re}\mathrm{Sc}$: for this block the scalar line does not contribute to the trace, and the three vector lines contribute one $X_0$ each.

The real rank of $L_{\tilde X}$ is twice its complex rank, and the complex rank is three for a general element, two on the isotropic cone $N(\tilde X)=X_0^2+X_1^2+X_2^2+X_3^2=0$ off the origin, and zero at the origin (*The Adjoint Operators of the Antisymmetric Quaternionic Algebra*, §*The Kernel and the Image*). The real rank is therefore six, four and zero, and the real annihilator of the operator grows from real dimension two to real dimension four as the element crosses into the cone.

At the element $e_0$ the operator is the element-level specificity of the block read over $\mathbb{R}$: the left multiplication is the projection onto the realification of the vector subspace,
$$
L_{e_0}\tilde X=\vec X,\qquad L_{e_0}^2=L_{e_0},\qquad R_{e_0}=-L_{e_0},
$$
it has real rank six, its image is the realification of $\mathrm{Vect}(\mathbb{B})$ and its kernel is the realification of the centre, of real dimension two. The identity and its interpretation are *The Specificities of the Antisymmetric Quaternionic Algebra*. The block's own invariant form is too degenerate to determine the adjoint of a multiplication operator, the whole vector subspace lying in its radical (*The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra*, §*The Adjoint of the Operator with Respect to a Form*), so the block supplies no adjoint of its own; the adjoints the four realified forms of the space give to left multiplication are the four of *The Four General Products and Operators*, §*The Products Decide the Four Adjoints*, and they are identities of the plain product and not of this block.

## What Is Specific to the Real Interpretation

Four features appear in the real reading of the block and not in its complex reading.

**The real subalgebras that are not complex subspaces.** Over $\mathbb{C}$ a subalgebra of the block is a complex subspace, hence of even real dimension, and the complex reading sees only those. Over $\mathbb{R}$ the quaternion subspace $\mathbb{H}_{\mathbb{B}}=\mathbb{R}\{e_0,e_1,e_2,e_3\}$, of real dimension four, is a subalgebra (*Remarkable Subspaces under the Antisymmetric Quaternionic Algebra of Biquaternions*, §*The Quaternion Subspace*), and its image
$$
\mathbb{R}\{e_1,e_2,e_3\}=\bigl\{\tilde Q=\vec Q,\ \vec Q\ \text{with real coefficients}\bigr\}
$$
is a subalgebra as well, of real dimension three: on the vector subspace the operation is the negative of the cross product (*Remarkable Subspaces under the Antisymmetric Quaternionic Algebra of Biquaternions*, §*The Vector Subspace*), so the value of two real pure vectors is a real pure vector again. Neither of the two is a complex subspace, the element $ie_1$ leaving both, and the three-dimensional one has no counterpart in the complex reading at all. Closedness is not automatic for a real subspace: $\mathbb{R}\{e_1,e_2\}$ is not a subalgebra, since $e_1\diamond e_2=-e_3$ leaves it; and the anti-quaternion, Hermitian and anti-Hermitian subspaces fail closure, each with its own smallest witness (*Remarkable Subspaces under the Antisymmetric Quaternionic Algebra of Biquaternions*). The general statement is the subspace row of the table of the four effects: a real subspace closed under the product need not be closed under $J$, so the real reading has more subalgebras than the complex one (*The Realification and the Effect of the Change of Scalars*, §*The Four Effects on a Structure*).

**The coincidence on the real part.** On the real part of the space, the real span of $e_0,e_1,e_2,e_3$, exactly two pairs of the catalogue coincide, the antisymmetric plain product with the antisymmetric quaternionic sesquilinear product and the symmetric quaternionic product with the symmetric plain sesquilinear product, so ten operations are seen there. The block is not one of the coincident pairs: it remains distinct from each of the other eleven operations on the real part and on the whole real space.

**The trace factor.** The complex trace of a left multiplication is $3X_0$ and the real trace is $6\operatorname{Re}X_0$; the factor six is the doubling of the realification applied to the complex trace, and it is not the eight of the regular representation of the plain algebra, the scalar line contributing nothing to this trace. The complex reading shows the trace and hides its real factor; the real reading shows both.

**The conjugate-linear automorphism.** The coefficientwise conjugation $\bar{\cdot}$ is an automorphism of the block over $\mathbb{R}$: it is $\mathbb{R}$-linear, and the structure constants of the operation are real, so
$$
\overline{\tilde P\diamond\tilde Q}=\bar{\tilde P}\diamond\bar{\tilde Q} .
$$
It is conjugate-linear, so it is not an automorphism over $\mathbb{C}$, and composing it with the $\mathbb{C}$-linear automorphism group (*The Adjoint Operators of the Antisymmetric Quaternionic Algebra*, §*The Automorphism Group and the Structure Group*) gives the conjugate-linear coset $\bar{\cdot}\,\mathrm{Aut}_{\mathbb{C}}$ of the real automorphism group, which the complex reading does not see. The natural conjugation is not an automorphism of the block: at $(e_1,e_2)$ it gives ${}^{\natural}(e_1\diamond e_2)=e_3$ while ${}^{\natural}e_1\diamond{}^{\natural}e_2=-e_3$; the block reads its real automorphisms through the coefficientwise conjugation and not through the natural one.

## Summary

The Antisymmetric Quaternionic Algebra read over $\mathbb{R}$ is the same product on the same elements, an $\mathbb{R}$-algebra on $\mathbb{R}^8$ in which alternation holds, the square vanishes, there is no unit and the Jacobi identity fails with the witness $(e_0,e_1,e_2)$ of the complex reading; its second slot is $\mathbb{C}_{\mathbb{B}}$-linear, and its left multiplications have the block shape of a $\mathbb{C}$-linear map with real trace $6\operatorname{Re}X_0$. The product carries no form, its scalar part vanishing; the two forms the block does carry, the invariant form $\varphi$ of rank one and the operator trace form $K$, realify to the real symmetric bilinear forms of rank two and signature $(1,1)$, of radical the realified vector subspace, and of signature $(4,4)$ with zero radical, both reversed by the complex structure. At $e_0$ the left multiplication is the projection onto the realified vector subspace, of real rank six and of kernel the realification of the centre. In the real reading the block has subalgebras that are not complex subspaces, among them the real pure vectors $\mathbb{R}\{e_1,e_2,e_3\}$ of real dimension three; the real part of the space sees ten of the twelve operations, the block not being one of the two coincident pairs; and the coefficientwise conjugation is an automorphism of the block over $\mathbb{R}$ and not over $\mathbb{C}$, so the real automorphism group carries the conjugate-linear coset. The passage changes nothing of the product itself; it changes the field, the dimension and the linear structure, and for this product it adds the real reading of its two forms and of its operators.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P\bigr)$ | the product of the Antisymmetric Quaternionic Algebra |
| $\mathbb{R}^8$ | the realification of $\mathbb{B}$, the eight real basis elements $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre, the field of scalars $\mathbb{C}$ carried by the ring |
| $J=L_i$ | the complex structure, multiplication by $i$, of square $-1$ |
| $\mathbb{H}_{\mathbb{B}}=\mathbb{R}\{e_0,e_1,e_2,e_3\}$ | the quaternion subspace, a subalgebra of real dimension four |
| $\varphi(\tilde P,\tilde Q)=P_0Q_0$ | the invariant form of the block, of rank one, of realified signature $(1,1)$ |
| $K(\tilde A,\tilde B)=\operatorname{Tr}(L_{\tilde A}L_{\tilde B})=3A_0B_0-2\sum_kA_kB_k$ | the operator trace form, non-degenerate, of realified signature $(4,4)$ |
| $L_{\tilde X}$, $R_{\tilde X}$ | the left and the right multiplications, $\mathbb{R}$-linear on $\mathbb{R}^8$ |
| $\operatorname{Tr}_{\mathbb{R}}(L_{\tilde X})=6\operatorname{Re}X_0$ | the real trace, twice the real part of the complex trace $3X_0$ |
| $\bar{\cdot}$ | the coefficientwise conjugation, an $\mathbb{R}$-algebra automorphism of the block and not a $\mathbb{C}$-algebra one |

## Further Reading

- *The Realification and the Effect of the Change of Scalars* (`articles_maths/the-realification-and-the-effect-of-the-change-of-scalars.md`), for the general construction, the two rules of the realification of a form and the table of the four effects.
- *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the twelve structures and the families of the table of the twelve, of which the block of this article is the entry $\mathrm{AQA}$.
- *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-invariant-bilinear-forms-of-the-antisymmetric-quaternionic-algebra.md`), for the form $\varphi$, the vanishing of the coefficient form and the operator trace form $K$, whose realifications this article reads.
- *Remarkable Subspaces under the Antisymmetric Quaternionic Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-antisymmetric-quaternionic-algebra.md`), for the closure of the centre, the vector subspace and the quaternion subspace, the failure of closure of the other three, and the subspace that is the image of the whole operation.
- *The Adjoint Operators of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-adjoint-operators-of-the-antisymmetric-quaternionic-algebra.md`), for the matrix, the trace $3X_0$, the rank and the kernel of the left multiplication, cited here in the real basis.
- *The Realification of the Four Forms* (`articles_maths/the-realification-of-the-four-forms.md`), for the four Gram matrices and the four signatures of the realified forms of the space, against which the two realified forms of this block are placed.
- *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternioid-c-space.md`), for the four forms of the space, their Gram matrices, their signatures and the groups that preserve them.
