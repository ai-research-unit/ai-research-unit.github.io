# __The Realification of the Antisymmetric Plain Algebra__

## Introduction

The Antisymmetric Plain Algebra is one of the twelve algebraic structures that the biquaternion space $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ carries, the structure carried by the product
$$
\tilde P\wedge\tilde Q=\tfrac12\bigl(\tilde P\tilde Q-\tilde Q\tilde P\bigr)=\mathbf{P}\times\mathbf{Q},
$$
the cross product of the two vector parts. It is the antisymmetric plain bilinear entry of the table of *The 12 Products of the Biquaternion Complex Space*, and it is the Lie product of that table: it alone of the twelve operations satisfies the Jacobi identity. Read over $\mathbb{R}$, the same product on the same set is an $\mathbb{R}$-algebra on the eight-dimensional real space $\mathbb{R}^8$, and this article owns that real reading.

The general construction is not repeated here. The realification of a vector space, of a linear map and of a form, the doubling of the dimension, the complex structure $J$ and the table of the four effects are *The Realification and the Effect of the Change of Scalars*; This article gives what is specific to this product: its real bilinear reading, the law of its second slot over the centre, the realification of the two forms it carries with the signatures that follow, and its real operators, its real derivations and its real automorphisms.

## The Product Read over $\mathbb{R}$

**Theorem.** The product is $\mathbb{R}$-bilinear, so that $\mathbb{B}$ is an $\mathbb{R}$-algebra, in the broad sense of a module with a bilinear multiplication, on the eight-dimensional real space
$$
\mathbb{R}^8=\operatorname{span}_{\mathbb{R}}\{e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3\}.
$$
In that algebra alternation holds, the Jacobi identity holds, there is no unit, and the scalar part vanishes.

*Proof.* The $\mathbb{R}$-bilinearity is §*The Effect on the Twelve Algebraic Structures* of *The Realification and the Effect of the Change of Scalars*. The rest are statements about the ring, written with the addition, the product and quantification over the elements, and the dictionary of the same article leaves them unchanged. The dimension is the doubling of the basis.

**The centre and the derived algebra.** The centre of the bracket read over $\mathbb{R}$ is the realified centre $\mathbb{C}_{\mathbb{B}}=\mathbb{R}e_0\oplus\mathbb{R}(ie_0)$, of real dimension two, and the derived algebra is the realified vector subspace $\mathrm{Vect}(\mathbb{B})$, of real dimension six, because a $\mathbb{C}$-subspace is an $\mathbb{R}$-subspace of even real dimension and the passage changes no dimension of one. The centre, the derived algebra, the ideals and the real forms are *The Lie Algebra of the Antisymmetric Plain Algebra*.

**A subalgebra of the real reading.** The real span
$$
\mathbb{R}\{e_1,e_2,e_3\}\cong\mathfrak{su}(2)
$$
is closed, because $e_1\wedge e_2=e_3$, $e_2\wedge e_3=e_1$ and $e_3\wedge e_1=e_2$, and it is of real dimension three. An odd-dimensional real space is not a complex subspace, so **this subalgebra has no complex counterpart**; the imaginary triple is not closed, $ie_1\wedge ie_2=-e_3$, so the gain is not the doubling of a complex subalgebra. The passage adds subalgebras exactly as it adds subspaces, and the ones it adds of odd real dimension are the ones the complex reading cannot name.

## The Second Slot and the Centre

Over $\mathbb{C}$ the product is $\mathbb{C}$-bilinear, so it is an **algebra** and not a sesqualgebra, and its second slot is $\mathbb{C}$-linear. Read over $\mathbb{R}$ the product remains $\mathbb{R}$-bilinear and its second slot is $\mathbb{C}_{\mathbb{B}}$-linear: by §*The Realification of a Linear Map* of *The Realification and the Effect of the Change of Scalars*, every left multiplication commutes with the complex structure, $L_{\tilde X}J=JL_{\tilde X}$, which is the criterion for $\mathbb{C}_{\mathbb{B}}$-linearity. Centrality of the left factor is not needed: the reason is the linearity of the second slot, which holds for every factor. The passage therefore **does not change the kind** of this product: the block belongs to the $A$ family of the twelve, whose six products keep their second slot $\mathbb{C}_{\mathbb{B}}$-linear in the two readings.

In the real basis the criterion takes a block form. If the complex matrix of the product on a $\mathbb{C}$-basis is $A+iB$, the real matrix on the doubled basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ is
$$
\begin{pmatrix}A&-B\\B&A\end{pmatrix},
$$
the shape that commutes with $J=\begin{pmatrix}0&-\mathrm{I}\\\mathrm{I}&0\end{pmatrix}$. For this product the two blocks are cross products by the two real vectors of the vector part: writing $\tilde X$ with vector part $\mathbf{X}=\mathbf{a}+i\mathbf{b}$, the real matrix of $\tilde Y\mapsto\tilde X\wedge\tilde Y$ carries the matrix of $\mathbf{a}\times$ on its two diagonal blocks and the matrix of $\mathbf{b}\times$ below the diagonal, with its negative above, and it kills the scalar coordinate.

## The Forms the Block Carries over $\mathbb{R}$

The form of an operation is its **scalar part** (*The 4 Forms over the Biquaternion $\mathbb{C}$ Space*), and the antisymmetrisation kills the scalar part of the general product of its family, so this product carries the **zero form** — a vanishing scalar part is counted as no form rather than as a fifth — and there is nothing for the realification of a form to act on. The two invariant symmetric forms the block does carry, read in *Norm and Invertibility in the Antisymmetric Plain Algebra*, do realify, and their realifications are the content of this section:
$$
K(\tilde A,\tilde B)=\operatorname{Tr}\bigl(L_{\tilde A}L_{\tilde B}\bigr)=-2\,\mathbf{A}\cdot\mathbf{B},
\qquad
\varphi(\tilde P,\tilde Q)=P_0Q_0 .
$$
$K$ is the operator trace form, of complex rank three, with radical the centre; it is at once the Killing form of the block in the normalisation of *The Killing Form of the Antisymmetric Plain Algebra*, where the adjoint is read with the block's own halved bracket, $\kappa(\tilde A,\tilde B)=\operatorname{Tr}(\operatorname{ad}_{\tilde A}\operatorname{ad}_{\tilde B})$. $\varphi$ is the scalar-part form, of complex rank one, with radical the vector subspace; the two are independent and span the invariant symmetric forms of the block; and their combination
$$
\varphi+\tfrac12K=\mathrm{Sc}(\tilde P\tilde Q)=B
$$
is the general plain bilinear form of the parent product.

Each of the three is a symmetric $\mathbb{C}$-bilinear form, and a symmetric bilinear form over $\mathbb{C}$ is classified by its rank alone, so the realification applies the first of the two rules of §*The Realification of a Form* of *The Realification and the Effect of the Change of Scalars*: the real part and the imaginary part of the form are two real symmetric bilinear forms, the Gram matrix consists of two opposite blocks, and a $\mathbb{C}$-bilinear form of complex rank $r$ realifies to the **split** signature $(r,r)$. On the real basis,

| form | complex reading | realified signature | radical over $\mathbb{R}$ |
|---|---|---|---|
| $K$ | symmetric bilinear, complex rank $3$, radical the centre | $(3,3)$ | the realified centre, real dimension $2$ |
| $\varphi$ | symmetric bilinear, complex rank $1$, radical the vector subspace | $(1,1)$ | the realified vector subspace, real dimension $6$ |
| $B=\varphi+\tfrac12K$ | symmetric bilinear, complex rank $4$ | $(4,4)$ | $0$ |

and the realified Gram matrices in the basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ are
$$
\operatorname{diag}(0,-2,-2,-2,0,2,2,2),
\qquad
\operatorname{diag}(1,0,0,0,-1,0,0,0),
\qquad
\operatorname{diag}(1,-1,-1,-1,-1,1,1,1).
$$
The first is the real Gram matrix of the invariant form of the block, of signature $(3,3)$ on the derived algebra, read in *The Killing Form of the Antisymmetric Plain Algebra*; the third is the realified Gram matrix $\operatorname{diag}(\mathrm{D},-\mathrm{D})$ of the general plain bilinear form, with $\mathrm{D}=\operatorname{diag}(1,-1,-1,-1)$ and the signs $+,-,-,-,-,+,+,+$, of *The Realification of the Four Forms*. The signatures add, $(1,1)\oplus(3,3)=(4,4)$, because $K$ and $\varphi$ are carried by complementary coordinates, the vector directions and the scalar ones.

**The action of the complex structure.** On all three forms the realification reverses $J$,
$$
\Phi_{\mathbb{R}}\bigl(J\tilde P,J\tilde Q\bigr)=-\Phi_{\mathbb{R}}\bigl(\tilde P,\tilde Q\bigr),
$$
the same statement as the two opposite blocks $\mathrm{D}$ and $-\mathrm{D}$ of the Gram matrix, and the rule of the bilinear kind: none of the three is Hermitian. On the derived algebra the two halves of $K$ carry opposite signs, $\operatorname{diag}(-2,-2,-2)$ on the real vector directions and $\operatorname{diag}(2,2,2)$ on the imaginary ones, which is the reading of the same form on the quaternion and the anti-quaternion subspace in the table of *The Killing Form of the Antisymmetric Plain Algebra*.

## The Real Operators

**Definition.** The left and the right multiplications by an element are the maps
$$
L_{\tilde X}:\tilde Y\mapsto\tilde X\wedge\tilde Y,
\qquad
R_{\tilde X}:\tilde Y\mapsto\tilde Y\wedge\tilde X,
$$
and over $\mathbb{R}$ they are $\mathbb{R}$-linear endomorphisms of $\mathbb{R}^8$, by §*The Realification of a Linear Map* of *The Realification and the Effect of the Change of Scalars*.

**Theorem (the two operators and their traces).** The product is alternating, so
$$
R_{\tilde X}=-L_{\tilde X},
\qquad
\operatorname{Tr}_{\mathbb{R}}\bigl(L_{\tilde X}\bigr)=\operatorname{Tr}_{\mathbb{C}}\bigl(L_{\tilde X}\bigr)=0 .
$$

*Proof.* Alternation gives $\tilde Y\wedge\tilde X=-(\tilde X\wedge\tilde Y)$. The operator $L_{\tilde X}$ kills the scalar coordinate and acts on the derived algebra by the skew matrix $\mathbf{Y}\mapsto\mathbf{X}\times\mathbf{Y}$, whose complex trace vanishes; the real trace of a $\mathbb{C}$-linear endomorphism is twice the real part of its complex trace, so it vanishes too. Computed on the basis. **The trace row of the table of the four effects is not this row.** That row, $\operatorname{Tr}_{\mathbb{C}}(L_{\tilde P})=4\,\mathrm{Sc}(\tilde P)$ and $\operatorname{Tr}_{\mathbb{R}}(L_{\tilde P})=8\operatorname{Re}\mathrm{Sc}(\tilde P)$, is the row of the products of the table whose element $e_0$ is a **left unit** — the general plain, the symmetric plain and the general quaternionic product; on the other nine, this one included, it fails, and on this one both traces vanish.

**Theorem (the operator trace form in the two readings).** For all $\tilde A,\tilde B$,
$$
\operatorname{Tr}_{\mathbb{R}}\bigl(L_{\tilde A}L_{\tilde B}\bigr)=2\operatorname{Re}K(\tilde A,\tilde B),
$$
twice the realified invariant form.

*Proof.* The composition is $\mathbb{C}$-linear, and the real trace of a $\mathbb{C}$-linear endomorphism is twice the real part of its complex trace; that complex trace is $K(\tilde A,\tilde B)$ by the definition of the operator trace form. Computed on the basis, on all $64$ pairs. The factor $2$ is the ratio of the two traces, $\operatorname{Tr}_{\mathbb{R}}=2\operatorname{Re}\operatorname{Tr}_{\mathbb{C}}$, the factor of the trace row of the table of the four effects.

**Proposition (the adjoint for the three realified forms).** For each of the three forms of the previous section,
$$
\Phi_{\mathbb{R}}\bigl(L_{\tilde X}\tilde Y,\tilde Z\bigr)+\Phi_{\mathbb{R}}\bigl(\tilde Y,L_{\tilde X}\tilde Z\bigr)=0,
$$
so the real adjoint of $L_{\tilde X}$ is $-L_{\tilde X}$.

*Proof.* The second slot is $\mathbb{C}_{\mathbb{B}}$-linear, so $L_{\tilde X}$ is $\mathbb{C}_{\mathbb{B}}$-linear, and as the adjoint of the block's own bracket it is skew for the invariant form $K$, which is the invariance of the form in *The Killing Form of the Antisymmetric Plain Algebra*; on $\varphi$ both terms vanish, since every value of the product is a pure vector and the scalar part of a pure vector is zero. Computed on the basis. The adjoints, the inner and outer derivations and the reading of the operators on the remarkable subspaces are *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*.

## The Derivations and the Automorphisms over $\mathbb{R}$

**Theorem (the derivations grow).** The $\mathbb{R}$-linear derivations of the bracket are
$$
\operatorname{Der}_{\mathbb{R}}(\mathfrak{g})\cong\mathfrak{sl}(2,\mathbb{C})\oplus\operatorname{End}_{\mathbb{R}}\bigl(\mathbb{C}_{\mathbb{B}}\bigr),
$$
of real dimension $6+4=10$, against the complex $\operatorname{Der}_{\mathbb{C}}(\mathfrak{g})\cong\mathfrak{sl}(2,\mathbb{C})\oplus\mathbb{C}$ of real dimension $6+2=8$. The extra two dimensions are conjugate-linear and act on the centre alone.

*Proof.* A derivation preserves the centre, because the centre is the annihilator and the Leibniz rule carries an annihilated element to an annihilated one, and it preserves the derived algebra, by the Leibniz rule and the stability of the image; so it is the sum of its two restrictions. The restrictions to the derived algebra are the derivations of the simple $\mathfrak{sl}(2,\mathbb{C})$ read over $\mathbb{R}$, hence the inner ones $\operatorname{ad}_{\mathbf{P}}$, of real dimension six, which is the factor $\mathfrak{sl}(2,\mathbb{C})$. A map vanishing on the derived algebra is a derivation exactly when it preserves the centre, and the centre is abelian of real dimension two, so every $\mathbb{R}$-linear endomorphism of it occurs: that is the factor $\operatorname{End}_{\mathbb{R}}(\mathbb{C}_{\mathbb{B}})$, of real dimension four, whose $\mathbb{C}$-linear half is the complex scalars $\mathbb{C}$ and completes the $\mathbb{C}$-linear part to $\mathfrak{sl}(2,\mathbb{C})\oplus\mathbb{C}$. Computed on the basis. The identity $\operatorname{Der}_{\mathbb{R}}=\operatorname{Der}_{\mathbb{C}}$ of the associative parent does not carry over, **because a derivation of a bracket is not a derivation of the ring**: a ring derivation kills $i$, from $i^2=-1$ and $D(-1)=0$, while a bracket derivation is free to move $i$ inside the centre, and here that freedom is two real dimensions.

**Proposition (the automorphisms grow at the centre).** An $\mathbb{R}$-automorphism of the bracket preserves the centre and the derived algebra, so
$$
\operatorname{Aut}_{\mathbb{R}}(\mathfrak{g})\cong GL_2(\mathbb{R})\times\operatorname{Aut}_{\mathbb{R}}\bigl(\mathrm{Vect}(\mathbb{B}),\wedge\bigr),
$$
which contains $GL_2(\mathbb{R})\times PGL(2,\mathbb{C})$, while the $\mathbb{C}$-linear group is $\operatorname{Aut}_{\mathbb{C}}(\mathfrak{g})\cong\mathbb{C}^{\times}\times PGL(2,\mathbb{C})$ (*The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*). The centre contributes the whole of $GL_2(\mathbb{R})$ in place of the complex scalars, and the derived algebra contributes, beside its $\mathbb{C}$-linear automorphisms, the conjugate-linear conjugation $\mathbf{X}\mapsto\bar{\mathbf{X}}$.

*Proof.* The centre and the derived algebra are characteristic, so an automorphism is a pair of an automorphism of each, and any such pair is an automorphism, because the bracket vanishes between the centre and the derived algebra and is internal to the derived algebra. The centre is abelian of real dimension two, so its automorphism group is the whole of $GL_2(\mathbb{R})$, of real dimension four, whose $\mathbb{C}$-linear part is $\mathbb{C}^{\times}$. On the derived algebra the complex automorphisms are $PGL(2,\mathbb{C})$, of real dimension six, and the conjugation of the coordinates is a further $\mathbb{R}$-automorphism, conjugate-linear and not in the complex group.

## Summary

Read over $\mathbb{R}$ the Antisymmetric Plain Algebra is the same product on the same elements, an $\mathbb{R}$-algebra on $\mathbb{R}^8$ in which alternation and the Jacobi identity hold, there is no unit, and the scalar part vanishes; its centre is the realified centre, of real dimension two, and its derived algebra the realified vector subspace, of real dimension six. Its second slot is $\mathbb{C}_{\mathbb{B}}$-linear, so the passage does not change the kind of the product. The product carries no form, the antisymmetrisation killing the scalar part; the two invariant symmetric forms it does carry realify by the split rule, the operator trace form $K$ to signature $(3,3)$ with the realified centre as radical, the scalar-part form $\varphi$ to $(1,1)$ with the realified vector subspace as radical, and their combination $B$ to $(4,4)$. The real left multiplication is the negative of the real right one, both of trace zero, and the real trace of a composition is twice the realified invariant form. The passage adds the three-dimensional real subalgebra $\mathbb{R}\{e_1,e_2,e_3\}$, it lets the derivations grow by a conjugate-linear part of real dimension two, and it lets the automorphisms act on the centre by the whole of $GL_2(\mathbb{R})$; every ring-theoretic object, by contrast, is left as it was.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf{P}\times\mathbf{Q}$ | the product of the Antisymmetric Plain Algebra |
| $\mathbb{R}^8$ | the realification of $\mathbb{B}$, the eight real basis elements $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{R}e_0\oplus\mathbb{R}(ie_0)$ | the centre, of complex dimension one and real dimension two |
| $J$ | the complex structure, multiplication by $i$, of square $-1$ |
| $L_{\tilde X}$, $R_{\tilde X}=-L_{\tilde X}$ | the left and the right multiplications, $\mathbb{R}$-linear on $\mathbb{R}^8$, of vanishing trace |
| $K$, $\varphi$ | the operator trace form and the scalar-part form, the two invariant symmetric forms, with $\varphi+\tfrac12K=B$ |
| $(3,3)$, $(1,1)$, $(4,4)$ | the realified signatures of $K$, of $\varphi$ and of $B$ |
| $\operatorname{Der}_{\mathbb{R}}(\mathfrak{g})\cong\mathfrak{sl}(2,\mathbb{C})\oplus\operatorname{End}_{\mathbb{R}}(\mathbb{C}_{\mathbb{B}})$ | the derivations over $\mathbb{R}$, of real dimension $10$ |
| $\operatorname{Aut}_{\mathbb{R}}(\mathfrak{g})\cong GL_2(\mathbb{R})\times\operatorname{Aut}_{\mathbb{R}}(\mathrm{Vect}(\mathbb{B}),\wedge)$ | the automorphism group over $\mathbb{R}$, containing $GL_2(\mathbb{R})\times PGL(2,\mathbb{C})$ |
| $\operatorname{Aut}_{\mathbb{C}}(\mathfrak{g})\cong\mathbb{C}^{\times}\times PGL(2,\mathbb{C})$ | the automorphism group of the bracket, the complex one |

## Further Reading

- *The Realification and the Effect of the Change of Scalars* (`articles_maths/the-realification-and-the-effect-of-the-change-of-scalars.md`), for the general construction, the two rules of the realification of a form, the table of the four effects and the change of scalars from $\mathbb{C}$ to $\mathbb{R}$.
- *Norm and Invertibility in the Antisymmetric Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-antisymmetric-plain-algebra.md`), for the two invariant symmetric forms, their ranks and their radicals, and the absence of a norm.
- *The Killing Form of the Antisymmetric Plain Algebra* (`articles_maths/the-killing-form-of-the-antisymmetric-plain-algebra.md`), for the invariant form, its radical, its Gram matrix in the real basis, its signature and its restrictions to the remarkable subspaces.
- *The Lie Algebra of the Antisymmetric Plain Algebra* (`articles_maths/the-lie-algebra-of-the-antisymmetric-plain-algebra.md`), for the centre, the derived algebra, the ideals and the real forms.
- *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra* (`articles_maths/the-adjoint-operators-and-the-derivations-of-the-antisymmetric-plain-algebra.md`), for the adjoints, the inner and outer derivations, the automorphism group and the structure group.
- *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-12-algebraic-structures-over-the-biquaternion-c-space.md`) and *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternion-c-space.md`), for the twelve structures and the four forms, of which this article is the real reading of one row and of one column.
- *The Realification of the Four Forms* (`articles_maths/the-realification-of-the-four-forms.md`), for the four realified Gram matrices, their signatures, the restrictions to the remarkable subspaces and the realified null cones.
